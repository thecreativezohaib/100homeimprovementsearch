#!/usr/bin/env python3
"""Round 3: check Gemini's 200 "no website" businesses (all_200_remodeling_homepages.json) before any page is built.
Per business: already in the round 2 kit (same phone), a live website of its own (any non-directory URL Gemini
reports, including free Wix / GoDaddy / Square / Google Sites pages, and the email's own domain), email syntax,
MX, made-up pattern, people-search source, whether the email's source page shows it (pages that are not behind a
login), the Maps link form, kitchen and bath fit, and how much usable material Gemini returned (real images, named
reviews). Writes data/r3/leads.json (Gemini's record + checks) and data/r3/vetted.csv.
Usage: r3_vet.py <all_200_remodeling_homepages.json>"""
import csv, glob, json, os, re, sys, concurrent.futures as cf

R = "/home/user/100homeimprovementsearch"
src = open(f"{R}/tools/r2_vet.py").read()
exec(src[:src.index("rows = []")])  # BAD_SRC, FREE, NOT_SITE, FAKE, mx(), live(), source_check(), match()
D = f"{R}/data/r3"

DIRECTORY = re.compile(r"rymaps|getcost|wallist|baltimoredirections|directions\.com|fredamendola|hud\.gov|fearringtoncares", re.I)
KB = re.compile(r"kitchen|bath|shower|tile|cabinet|counter|vanity|granite|quartz|backsplash|remodel", re.I)
URL = re.compile(r"https?://[^\s\"'),;]+|\b[a-z0-9-]+\.(?:wixsite\.com|godaddysites\.com|square\.site|squarespace\.com|weebly\.com|"
                 r"webflow\.io|business\.site|sites\.google\.com)[^\s\"'),;]*", re.I)


def digits(s):
    return re.sub(r"\D", "", s or "")[-10:]


r2_phones = {}
for f in glob.glob(f"{R}/output/round2/kit/*/*/research.json"):
    j = json.load(open(f))
    r2_phones[digits(j["google"]["phone"])] = j["business_name"]

d = json.load(open(sys.argv[1]))
os.makedirs(D, exist_ok=True)


def vet(i, x):
    e = (x.get("email") or "").strip().strip(".").replace(" ", "")
    dom = e.split("@")[-1].lower()
    c = x.get("content") or {}
    out = {"n": i, "business_name": x["business_name"], "phone": x.get("phone", ""), "email": e,
           "email_source": x.get("email_source", ""), "facebook_url": x.get("facebook_url", ""),
           "instagram_url": x.get("instagram_url", ""), "google_maps_url": x.get("google_maps_url", "")}
    out["in_round2"] = r2_phones.get(digits(out["phone"]), "")
    out["email_ok"] = bool(re.fullmatch(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", e))
    out["mx"] = mx(dom) if out["email_ok"] else False
    out["fake_email"] = bool(FAKE.search(e))
    out["bad_source"] = bool(BAD_SRC.search(out["email_source"]))
    out["source_check"] = source_check(out["email_source"], e) if out["email_ok"] else "no email"
    # every URL Gemini mentions that is not a directory or social page is a possible website
    text = " ".join([x.get("website_found") or "", out["email_source"], " ".join(x.get("other_profiles") or [])])
    # only URLs that carry the business's name count as its own site (not a realtor's or supplier's referral page)
    cands = {u.rstrip("/.") for u in URL.findall(text) if not NOT_SITE.search(u) and not DIRECTORY.search(u) and match(x["business_name"], u.replace("://", ".com/")) >= 0.5}
    if dom not in FREE and out["email_ok"]:
        cands.add(dom)
    out["site_candidates"] = " ".join(sorted(cands))
    out["live_site"] = next((s for s in sorted(cands) if live(s)), "")
    out["maps_place_id"] = "place_id:" in out["google_maps_url"]
    out["kb_fit"] = bool(KB.search(" ".join([x.get("category", ""), " ".join(x.get("services_found") or [])])))
    out["real_images"] = len(x.get("images") or [])
    out["named_reviews"] = sum(1 for r in x.get("reviews") or [] if not re.search(r"verified|client|customer|anonymous", r.get("name", ""), re.I))
    out["reviews"] = len(x.get("reviews") or [])
    out["has_content"] = bool(c)
    why = []
    if out["in_round2"]:
        why.append("already in round 2")
    if out["live_site"]:
        why.append(f"has a website ({out['live_site']})")
    if not out["email_ok"] or out["fake_email"] or out["bad_source"] or out["mx"] is False:
        why.append("email unusable")
    if out["source_check"] == "missing":
        why.append("email not on its source page")
    if not out["kb_fit"]:
        why.append("no kitchen or bath work listed")
    out["status"] = "drop" if why else ("pass" if out["source_check"] == "verified" else "check")
    out["why"] = "; ".join(why)
    return out


with cf.ThreadPoolExecutor(16) as ex:
    res = list(ex.map(lambda a: vet(*a), enumerate(d, 1)))
json.dump([{**x, "check": r} for x, r in zip(d, res)], open(f"{D}/leads.json", "w"), indent=1, ensure_ascii=False)
with open(f"{D}/vetted.csv", "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=list(res[0]))
    w.writeheader()
    w.writerows(res)
from collections import Counter
print(Counter(r["status"] for r in res))
print(Counter(w for r in res for w in r["why"].split("; ") if w and not w.startswith("has a website")),
      "has a website:", sum(bool(r["live_site"]) for r in res))
print("source check", Counter(r["source_check"] for r in res))
print("place_id links", sum(r["maps_place_id"] for r in res), "| real images", sum(r["real_images"] for r in res),
      "| named reviews", sum(r["named_reviews"] for r in res), "of", sum(r["reviews"] for r in res))
