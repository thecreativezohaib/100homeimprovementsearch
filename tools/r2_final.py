#!/usr/bin/env python3
"""Final round 2 homepage kit: pick the 100, lint every page, collect the AI image prompts, and zip.
Pool: every kit folder with a content.json (sites/, reserves/, extra/). A business is contactable unless its email
belongs to someone else (decided in the writers' and editors' checks), it already has a live website, or it does no
kitchen and bath work. Contactable businesses are ranked (email confirmed first, then distinct real photos and
testimonials) and the top 100 become 001..100; the rest are reserves; the others go to do_not_contact.
Writes output/round2/final/ (staging) and output/round2/R2_HOMEPAGE_KIT_FINAL.zip.
Usage: r2_final.py"""
import csv, glob, json, os, re, shutil, zipfile

R = "/home/user/100homeimprovementsearch"
K, O = f"{R}/output/round2/kit", f"{R}/output/round2"
F = f"{O}/final"

# email is not the business's own (writers' and editors' checks of the source pages)
NOT_THEIRS = {"021", "024", "026", "029", "034", "035", "045", "049", "066", "068", "072", "081", "082", "088", "089", "090",
              "096", "097", "108", "109", "111", "112", "117", "120", "122"}
HAS_SITE = {"037", "046", "067", "110"}
NOT_NICHE = {"060"}
REASON = {**{k: "email belongs to another business" for k in NOT_THEIRS}, **{k: "already has a live website" for k in HAS_SITE},
          **{k: "no kitchen or bath work" for k in NOT_NICHE}}


def digits(s):
    return re.sub(r"\D", "", s or "")[-10:]


def walk_strings(o, path=""):
    if isinstance(o, dict):
        for k, v in o.items():
            yield from walk_strings(v, f"{path}.{k}")
    elif isinstance(o, list):
        for i, v in enumerate(o):
            yield from walk_strings(v, f"{path}[{i}]")
    elif isinstance(o, str):
        yield path, o


def lint(d, c, r):
    issues = []
    ph = digits(r["google"]["phone"])
    fph = digits((c.get("footer") or {}).get("phone"))
    if ph and fph and ph != fph:
        issues.append("footer phone differs from Google")
    for p, s in walk_strings(c):
        if "—" in s and not re.search(r"testimonials|review|quote", p, re.I):
            issues.append(f"em dash at {p}")
        for bad in ("look no further", "one-stop shop", "we pride ourselves"):
            if bad in s.lower() and not re.search(r"testimonials|review|quote|missing", p, re.I):
                issues.append(f"'{bad}' at {p}")
        if re.search(r"PLACEHOLDER|TODO|lorem", s) and "missing" not in p:
            issues.append(f"placeholder at {p}")
    for e in c.get("image_plan") or []:
        if e.get("file") and not os.path.exists(f"{d}/{e['file']}"):
            issues.append(f"missing image file {e['file']}")
        if e.get("source") == "ai" and not e.get("ai_prompt"):
            issues.append(f"AI slot without prompt {e.get('slot')}")
        if e.get("source") == "ai" and str(e.get("slot", "")).startswith("gallery"):
            issues.append("AI image in gallery")
    if not c.get("image_plan"):
        issues.append("no image_plan")
    if (c.get("schema_jsonld") or {}).get("aggregateRating"):
        issues.append("aggregateRating in schema")
    return issues


def link_ai(o, dst):
    if isinstance(o, dict):
        if o.get("ai_file_name") and not o.get("file") and os.path.exists(f"{dst}/images/{o['ai_file_name']}"):
            o["file"] = f"images/{o['ai_file_name']}"
        for v in o.values():
            link_ai(v, dst)
    elif isinstance(o, list):
        for v in o:
            link_ai(v, dst)


pool = []
for d in sorted(glob.glob(f"{K}/sites/[0-9]*_*") + glob.glob(f"{K}/reserves/[0-9]*_*") + glob.glob(f"{K}/extra/[0-9]*_*")):
    if not os.path.exists(f"{d}/content.json"):
        continue
    c, r = json.load(open(f"{d}/content.json")), json.load(open(f"{d}/research.json"))
    name = os.path.basename(d)
    rank = name[:3]
    miss = " ".join(map(str, c.get("missing") or []))
    email = (c.get("footer") or {}).get("email")
    reason = REASON.get(rank) or ("email belongs to another business" if (not email or "EMAIL NOT THEIRS" in miss) else None)
    plan = c.get("image_plan") or []
    real = len({e["file"] for e in plan if e.get("source") == "real" and e.get("file")})
    ai = sum(1 for e in plan if e.get("source") == "ai")
    tst = len((c.get("testimonials") or {}).get("items") or [])
    # Brooksberry: a 1-star review says the location closed; ranked with the unconfirmed until it is confirmed open
    unconfirmed = "EMAIL UNCONFIRMED" in miss or rank == "128"
    pool.append({"dir": d, "name": name, "c": c, "r": r, "reason": reason, "real": real, "ai": ai, "tst": tst,
                 "unconfirmed": unconfirmed, "lint": lint(d, c, r), "email": email or "",
                 "score": (0 if unconfirmed else 1, min(real, 10) + 2 * min(tst, 3) + (3 if r.get("tier") == "main" else 0))})

ok = sorted([p for p in pool if not p["reason"]], key=lambda p: p["score"], reverse=True)
final, reserves, dnc = ok[:100], ok[100:], [p for p in pool if p["reason"]]
shutil.rmtree(F, ignore_errors=True)
rows, prompts = [], []
for group, items in (("homepages", final), ("reserves", reserves), ("do_not_contact", dnc)):
    for i, p in enumerate(items, 1):
        slug = p["name"][4:]
        new = f"{i:03d}_{slug}"
        dst = f"{F}/{group}/{new}"
        shutil.copytree(p["dir"], dst)
        c = p["c"]
        c["id"] = new
        # AI images generated so far (r2_import_ai.py keeps them by business slug): link each slot to its file
        ai_dir = f"{O}/ai_images/{slug}"
        if group == "homepages" and os.path.isdir(ai_dir):
            for f in os.listdir(ai_dir):
                shutil.copy(f"{ai_dir}/{f}", f"{dst}/images/{f}")
            link_ai(c, dst)
            md = open(f"{dst}/content.md").read()
            md = re.sub(r"AI image `(ai_[a-z0-9_]+\.jpg)`", lambda m: f"AI image `images/{m.group(1)}`" if os.path.exists(f"{dst}/images/{m.group(1)}")
                        else f"AI image `{m.group(1)}` (not generated yet)", md)
            open(f"{dst}/content.md", "w").write(md)
        json.dump(c, open(f"{dst}/content.json", "w"), indent=1, ensure_ascii=False)
        r = p["r"]
        rows.append({"group": group, "folder": f"{group}/{new}", "business_name": r["business_name"], "phone": r["google"]["phone"],
                     "email": p["email"], "email_status": "unconfirmed" if p["unconfirmed"] else ("not usable" if p["reason"] else "checked"),
                     "facebook": r.get("facebook_url") or "", "instagram": r.get("instagram_url") or "", "google_maps": r["google"]["maps_url"],
                     "primary_keyword": (c.get("seo") or {}).get("primary_keyword", ""), "real_photos": p["real"], "ai_slots": p["ai"],
                     "ai_images_missing": sum(1 for e in c.get("image_plan") or [] if e.get("source") == "ai" and not e.get("file")) if group == "homepages" else "",
                     "testimonials": p["tst"], "reason_not_contactable": p["reason"] or "",
                     "to_confirm": " | ".join(str(m) for m in (c.get("missing") or [])[:4]),
                     "outreach_detail": (c.get("outreach") or {}).get("specific_detail", ""), "lint_issues": "; ".join(p["lint"])})
        if group == "homepages":
            for e in c.get("image_plan") or []:
                if e.get("source") == "ai":
                    prompts.append({"folder": f"homepages/{new}", "business_name": r["business_name"], "slot": e.get("slot"),
                                    "save_as": f"images/{e.get('ai_file_name') or ''}", "prompt": e.get("ai_prompt"), "alt": e.get("alt", ""),
                                    "generated": "yes" if e.get("file") else "no"})

for fn, data in (("INDEX.csv", rows), ("AI_IMAGE_PROMPTS.csv", prompts)):
    with open(f"{F}/{fn}", "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(data[0]))
        w.writeheader()
        w.writerows(data)
for f in ("CONTENT_BRIEF_R2.md", "content_schema_r2.json"):
    shutil.copy(f"{K}/{f}", f"{F}/{f}")
nl = sum(1 for x in rows if x["group"] == "homepages" and x["lint_issues"])
n_ai_done = sum(1 for x in prompts if x["generated"] == "yes")
open(f"{F}/README.md", "w").write(f"""# Round 2 homepage kit (final)

- `homepages/001..{len(final):03d}`: the {len(final)} businesses to build and contact, best first.
- `reserves/`: {len(reserves)} more contactable businesses with pages written.
- `do_not_contact/`: {len(dnc)} businesses whose email belongs to someone else, that already have a website, or that do
  no kitchen and bath work (pages kept for reference).

Each folder: `content.json` (the page, with `image_plan`), `content.md` (readable copy + image plan + facts + what to
confirm), `images/` (their own photos, logo when found), `images.json`, `brand.json`, `research.json`, `contact_sheet.jpg`.

Images: every essential slot (hero, each service card, about, gallery, final CTA) has an image in `image_plan`. Real
photos are used wherever one fits. Where none does, the slot uses an AI image (`images/ai_*.jpg`, `"source": "ai"`,
already cropped to the slot's shape). {n_ai_done} of {len(prompts)} AI images are in place; any still to generate have
`"file": null` and are marked "no" in `AI_IMAGE_PROMPTS.csv` (prompt and file name included). Galleries use real photos
only, so no AI picture is ever presented as the business's own project, and AI image alt text never claims it is.

`INDEX.csv`: every business with contact details, email status, keyword, photo / AI / testimonial counts, the first
items to confirm, the outreach detail, and any lint findings ({nl} homepage(s) with a lint note).
""")
exec(open(f"{R}/tools/r2_ai_images_file.py").read(), {"__name__": "r2_ai_images_file"})  # name map + Gemini file
zp = f"{O}/R2_HOMEPAGE_KIT_FINAL.zip"
with zipfile.ZipFile(zp, "w", zipfile.ZIP_DEFLATED) as z:
    for root, _, files in os.walk(F):
        for fn in files:
            p = os.path.join(root, fn)
            z.write(p, "R2_HOMEPAGE_KIT/" + os.path.relpath(p, F))
print("homepages", len(final), "reserves", len(reserves), "do_not_contact", len(dnc), "ai prompts", len(prompts), "ai images in place", n_ai_done,
      "homepages with lint notes", nl, "unconfirmed emails in the 100", sum(p["unconfirmed"] for p in final),
      "zip MB", round(os.path.getsize(zp) / 1e6))
