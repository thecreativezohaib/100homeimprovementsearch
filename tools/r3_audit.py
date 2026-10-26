#!/usr/bin/env python3
"""Audit a round 3 batch returned by Antigravity (batch_<k>/homepages/<n>_<slug>/...) before anything is reused.
Per homepage: valid content, real images (open, size, duplicates across businesses), testimonials named and present in
research.json, copy quality (cut-off titles and meta, "...", lower-case state codes, sentences repeated across pages
or across services, service blurb about a different service), banned phrases, em dashes, email MX and source page.
Writes <batch>/AUDIT.csv and prints a summary.
Usage: r3_audit.py <batch folder>"""
import csv, glob, hashlib, json, os, re, sys, collections
from PIL import Image

R = "/home/user/100homeimprovementsearch"
src = open(f"{R}/tools/r2_vet.py").read()
exec(src[:src.index("rows = []")])  # mx(), source_check(), FREE, BAD_SRC

B = sys.argv[1].rstrip("/")
BANNED = ("look no further", "one-stop shop", "we pride ourselves", "second to none", "top-notch", "unparalleled")
pages = sorted(glob.glob(f"{B}/homepages/*/content.json"))
sent_owner = collections.defaultdict(set)
hash_owner = collections.defaultdict(set)
data = {}
for f in pages:
    d = os.path.dirname(f)
    n = os.path.basename(d)
    c = json.load(open(f))
    r = json.load(open(f"{d}/research.json"))
    data[n] = (d, c, r)
    text = " ".join(s for s in re.findall(r'"([^"]{40,})"', json.dumps(c.get("intro", {})) + json.dumps(c.get("services", {}))
                                          + json.dumps(c.get("why_choose_us", {})) + json.dumps(c.get("about", {}))))
    for s in re.split(r"(?<=[.!?])\s+", text):
        s = re.sub(r"\s+", " ", s.lower().replace(r.get("business_name", "").lower(), "<name>")).strip()
        if len(s) > 50:
            sent_owner[s].add(n)
    for im in glob.glob(f"{d}/images/*"):
        hash_owner[hashlib.md5(open(im, "rb").read()).hexdigest()].add(n)

rows = []
for n, (d, c, r) in data.items():
    s = json.dumps(c, ensure_ascii=False)
    seo, hero = c.get("seo") or {}, c.get("hero") or {}
    imgs = glob.glob(f"{d}/images/*")
    good, small, broken = 0, 0, 0
    for im in imgs:
        try:
            w, h = Image.open(im).size
            if os.path.basename(im).startswith(("logo", "cover")):
                continue
            good += w >= 600
            small += w < 600
        except Exception:
            broken += 1
    shared = sum(1 for im in imgs if len(hash_owner[hashlib.md5(open(im, "rb").read()).hexdigest()]) > 1)
    tst = (c.get("testimonials") or {}).get("items") or []
    rv = " ".join(x.get("text", "") for x in r.get("reviews") or [])
    t_bad_name = sum(1 for t in tst if re.search(r"verified|client|customer|anonymous|google user", t.get("name", ""), re.I))
    t_not_in_research = sum(1 for t in tst if t.get("text", "")[:60] not in rv)
    repeated = sum(1 for k, v in sent_owner.items() if n in v and len(v) > 1)
    svc = (c.get("services") or {}).get("items") or []
    mismatch = sum(1 for it in svc if ("kitchen" in it.get("name", "").lower() and "bathroom" in it.get("blurb", "").lower()
                                       and "kitchen" not in it.get("blurb", "").lower()))
    blurb_starts = collections.Counter(" ".join(it.get("blurb", "").split()[:4]).lower() for it in svc)
    e = ((c.get("footer") or {}).get("email") or r.get("email") or "").strip()
    dom = e.split("@")[-1].lower() if "@" in e else ""
    row = {
        "folder": n, "business_name": r.get("business_name", ""), "email": e,
        "email_mx": mx(dom) if dom else "",
        "email_source_check": source_check(r.get("email_source", ""), e) if e else "no email",
        "email_source_fb_group": "facebook.com/groups" in (r.get("email_source") or ""),
        "real_images_600px": good, "small_images": small, "broken_images": broken, "images_shared_with_other_pages": shared,
        "testimonials": len(tst), "testimonial_bad_name": t_bad_name, "testimonial_not_in_research": t_not_in_research,
        "research_reviews": len(r.get("reviews") or []),
        "title_len": len(seo.get("title_tag", "")), "meta_len": len(seo.get("meta_description", "")),
        "title_cut": bool(re.search(r"[a-z]$", seo.get("title_tag", "")) and len(seo.get("title_tag", "")) >= 59),
        "meta_ellipsis": "..." in seo.get("meta_description", ""),
        "lowercase_state": bool(re.search(r"\b[A-Z][a-z]+ (Nc|Ar|Pa|Tx|Fl|Ga|Va|Md|Nj|Ny|Oh|Mi|Tn|Ky|Al|Sc|Co|Az|Ca|Wa|Or|Ma|Ct|Nh|Vt|Me|Ri|De|Wi|Mn|Ia|Mo|Ks|Ne|Ok|La|Ms|In|Il|Ut|Nv|Nm|Id|Mt|Wy|Sd|Nd|Ak|Hi|Wv)\b", s)),
        "service_blurb_mismatch": mismatch, "service_blurbs_same_opening": sum(v - 1 for v in blurb_starts.values() if v > 1),
        "sentences_shared_with_other_pages": repeated,
        "em_dash": s.count("—"), "banned": sum(s.lower().count(b) for b in BANNED),
        "free_claim": bool(re.search(r"\bfree\b", s, re.I)),
        "ai_slots": sum(1 for x in c.get("image_plan") or [] if x.get("source") == "ai"),
    }
    rows.append(row)
with open(f"{B}/AUDIT.csv", "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=list(rows[0]))
    w.writeheader()
    w.writerows(rows)
N = len(rows)
print("homepages", N)
for k in ("email_source_fb_group", "title_cut", "meta_ellipsis", "lowercase_state", "free_claim"):
    print(f"{k}: {sum(1 for x in rows if x[k] is True)}")
print("email source check", collections.Counter(x["email_source_check"] for x in rows), "| no MX", sum(1 for x in rows if x["email_mx"] is False))
print("pages with 0 testimonials", sum(1 for x in rows if x["testimonials"] == 0), "| research reviews total", sum(x["research_reviews"] for x in rows),
      "| testimonials with fake names", sum(x["testimonial_bad_name"] for x in rows), "| not found in research", sum(x["testimonial_not_in_research"] for x in rows))
print("real images >=600px per page", sorted(x["real_images_600px"] for x in rows), "| small", sum(x["small_images"] for x in rows),
      "| broken", sum(x["broken_images"] for x in rows), "| images also on another page", sum(x["images_shared_with_other_pages"] for x in rows))
print("pages sharing sentences with other pages", sum(1 for x in rows if x["sentences_shared_with_other_pages"]),
      "| service blurb about another service", sum(x["service_blurb_mismatch"] for x in rows),
      "| em dashes", sum(x["em_dash"] for x in rows), "| banned", sum(x["banned"] for x in rows), "| AI slots", sum(x["ai_slots"] for x in rows))
