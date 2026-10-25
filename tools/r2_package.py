#!/usr/bin/env python3
"""Package the round 2 homepage kit after the writers' audit.
Each business lands in one of two groups:
  ready/            homepage written and contactable: the email is the business's own (as far as we can check) and it
                    has no live website. Flags to confirm with the owner are in CONFIRM_BEFORE_OUTREACH.csv.
  do_not_contact/   homepage written, but the email belongs to another business, the business already has a live
                    website, or it is not a kitchen and bath business. Kept for reference, with the reason.
Writes output/round2/R2_HOMEPAGE_KIT.zip with the brief, schema, README, index, CSVs and one folder per business
(content.json, content.md, brand.json, research.json, images.json, contact_sheet.jpg, images/).
Usage: r2_package.py"""
import csv, glob, json, os, zipfile

R = "/home/user/100homeimprovementsearch"
K, O = f"{R}/output/round2/kit", f"{R}/output/round2"

# from the writers' checks of each source page and my browser checks of the domains (see the session notes)
EMAIL_NOT_THEIRS = {
    "021": "email belongs to a Parker, CO company", "024": "email belongs to a Maryland woodworker",
    "026": "email and licence belong to Kings Custom Cabinetry, Rancho Cordova", "029": "email belongs to Empire Carpentry (AL)",
    "034": "email belongs to a Herrera Custom Cabinets in Los Angeles", "035": "email belongs to a Lakeside Renovations in Montana",
    "045": "email belongs to a wellness studio in Boston", "066": "email belongs to a realtor (parish bulletin)",
    "072": "email belongs to the cabinet maker Koch & Company", "081": "email belongs to a New Jersey A.C.E Carpentry",
    "082": "email belongs to another Happy Home Remodeling", "089": "email belongs to an FJ Remodeling in Cleveland",
    "090": "email belongs to Allen Custom Homes", "096": "email belongs to another page / a realtor",
    "108": "email belongs to an Austin, TX business with the same name", "109": "email belongs to a California Cabinet Shop",
    "111": "email belongs to a Houston store", "112": "email belongs to a Toronto company",
    "117": "email taken from an auction yard page", "120": "email and Instagram belong to DP removal services"}
HAS_SITE = {"037": "live Squarespace site jeff-james-s7u4.squarespace.com", "046": "live site mdcdesigncenter.com (Cherry Hill)",
            "067": "live site newcreation607.com", "110": "live site excellencerenovationllc.com"}
NOT_NICHE = {"060": "no kitchen or bath work found (doors, floors, decks, land clearing)"}
CONFIRM = {
    "007": "no town in any source", "010": "Facebook logo reads C&K Tile and Carpet Cleaning",
    "020": "email sbpoolleague@cox.net looks personal; sign shows ogdenwoodworking.com (not loading)",
    "025": "email spelling: card shows lhcarpentry6@gmail.com", "047": "town assumed from the 801 area code",
    "048": "town assumed from phone and email", "068": "dynastyimprovements.com would not load; confirm it is not theirs",
    "074": "email cleaned to modeltilellc@gmail.com", "079": "jankecustomtile.com shows 'domain not connected'",
    "080": "no town; kellyskandb.com would not load", "086": "email not seen on its source page",
    "088": "no town; email from a second Facebook page with another phone", "097": "email is Karolina Bell's (shares the business phone)",
    "098": "town assumed from the 919 area code", "099": "robertrepairstn.com returns 404", "106": "argentomarble.com shows nothing",
    "113": "armhomecare.com shows nothing", "114": "no town (859 area code)", "115": "no town (740 area code)",
    "013": "no phone on Google: calls to action use email", "089": "no phone on Google"}

folders = sorted(glob.glob(f"{K}/sites/[0-9]*_*") + glob.glob(f"{K}/reserves/[0-9]*_*"))
rows, ready, out = [], 0, []
for d in folders:
    name = os.path.basename(d)
    rank = name[:3]
    r = json.load(open(f"{d}/research.json"))
    c = json.load(open(f"{d}/content.json"))
    reason = EMAIL_NOT_THEIRS.get(rank) or HAS_SITE.get(rank) or NOT_NICHE.get(rank)
    group = "do_not_contact" if reason else "ready"
    ready += group == "ready"
    rows.append({"folder": f"{group}/{name}", "group": group, "original_tier": r["tier"], "business_name": r["business_name"],
                 "phone": r["google"]["phone"], "email": (c.get("footer") or {}).get("email") or "", "email_published_at": r["email"]["published_at"],
                 "facebook": r["facebook_url"] or "", "instagram": r["instagram_url"] or "", "google_maps": r["google"]["maps_url"],
                 "primary_keyword": (c.get("seo") or {}).get("primary_keyword", ""),
                 "gallery_images": len((c.get("gallery") or {}).get("images") or []),
                 "testimonials": len((c.get("testimonials") or {}).get("items") or []),
                 "reason_not_contactable": reason or "", "confirm_before_outreach": CONFIRM.get(rank, ""),
                 "outreach_detail": (c.get("outreach") or {}).get("specific_detail", "")})
    out.append((d, f"{group}/{name}"))

cols = list(rows[0])
for fn, sel in (("R2_KIT_INDEX.csv", rows), ("CONFIRM_BEFORE_OUTREACH.csv", [x for x in rows if x["group"] == "ready" and x["confirm_before_outreach"]])):
    with open(f"{K}/{fn}", "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=cols)
        w.writeheader()
        w.writerows(sel)

readme = f"""# Round 2 homepage kit: first websites for kitchen and bath businesses

{ready} businesses are ready (folder `ready/`), {len(rows) - ready} are kept for reference in `do_not_contact/`.

Each business folder holds:
- `content.json`: the full homepage copy in the master structure (`content_schema_r2.json`): SEO tags, hero, intro,
  services, why choose us, about, process, gallery, testimonials, service area, FAQ, final call to action, footer,
  schema markup, brand, outreach angle, `facts_used` (every claim with its source) and `missing` (what was not found)
- `content.md`: the same page as readable text
- `images/`: their own photos from Google Maps, Facebook and Instagram, `logo.jpg` and `cover.jpg` when found
  (check `images_not_to_use` in content.json and `brand.logo_file` before using a logo)
- `images.json`: where each photo came from; `contact_sheet.jpg`: all photos on one sheet
- `brand.json` and the `brand` block in content.json: palette, fonts, tagline
- `research.json`: everything collected about the business

Files at the top:
- `R2_KIT_INDEX.csv`: every business, contact details, keyword, counts and flags
- `CONFIRM_BEFORE_OUTREACH.csv`: ready businesses with something to confirm (town, email spelling, possible domain)
- `CONTENT_BRIEF_R2.md` and `content_schema_r2.json`: the rules and structure every page was written to

Notes
- Every review on the pages is quoted exactly from Google; Gemini's "reviews" were unrelated web text and none were used.
- No licence numbers, years, warranties or prices were invented; when not found they are listed under `missing`.
- `do_not_contact/` reasons: the email belongs to another business, the business already has a live website, or it
  does no kitchen and bath work. Their pages are written in case a correct email turns up.
"""
open(f"{K}/README.md", "w").write(readme)

zp = f"{O}/R2_HOMEPAGE_KIT.zip"
with zipfile.ZipFile(zp, "w", zipfile.ZIP_DEFLATED) as z:
    for f in ("README.md", "CONTENT_BRIEF_R2.md", "content_schema_r2.json", "R2_KIT_INDEX.csv", "CONFIRM_BEFORE_OUTREACH.csv"):
        z.write(f"{K}/{f}", f"R2_HOMEPAGE_KIT/{f}")
    for src, dst in out:
        for root, _, files in os.walk(src):
            for fn in files:
                p = os.path.join(root, fn)
                z.write(p, f"R2_HOMEPAGE_KIT/{dst}/{os.path.relpath(p, src)}")
print("ready", ready, "do_not_contact", len(rows) - ready, "zip MB", round(os.path.getsize(zp) / 1e6))
