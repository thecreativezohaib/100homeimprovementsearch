#!/usr/bin/env python3
"""Kit folders for backup businesses promoted to fill the 100 (output/round2/kit/extra/<rank>_<slug>/), built with
the same files as r2_bundles.py (which rebuilds sites/ and reserves/ from scratch, so it is not re-run once content
exists). These businesses had no Gemini content dive: research.json carries the Maps capture and the task 3 record.
Usage: r2_bundles_extra.py <row> [<row> ...]"""
import csv, json, os, re, sys, glob, shutil
src = open("/home/user/100homeimprovementsearch/tools/r2_bundles.py").read().split("for sub in (")[0]
exec(src)  # paths, loaded data and helpers (clean, slug, palette, sheet)
task3 = {r["row"]: r for r in csv.DictReader(open(f"{D}/gemini_in/task3_all.csv", encoding="utf-8-sig"))}
want = set(sys.argv[1:])
for r in fin:
    if r["row"] not in want:
        continue
    row, rank = r["row"], int(r["rank"])
    folder = f"{K}/extra/{rank:03d}_{slug(r['business_name'])}"
    shutil.rmtree(folder, ignore_errors=True)
    os.makedirs(f"{folder}/images", exist_ok=True)
    dp, v, t3 = deep.get(row, {}), vet.get(row, {}), task3.get(row, {})
    imgs = []
    for m in sorted([m for m in man if m["row"] == row], key=lambda m: m["name"]):
        dst = f"{folder}/images/{m['name']}.jpg"
        shutil.copy(m["file"], dst)
        rv = next((x for x in dp.get("reviews") or [] if any(m["url"].split("=")[0] in p for p in x.get("photos") or [])), None)
        imgs.append({"file": f"images/{m['name']}.jpg", "source": "Google Maps", "width": m.get("w"), "height": m.get("h"),
                     "url": m["url"], "from_review": {"reviewer": rv["reviewer"], "when": rv["when"]} if rv else None})
    json.dump(imgs, open(f"{folder}/images.json", "w"), indent=1)
    sheet([f"{folder}/{e['file']}" for e in imgs], f"{folder}/contact_sheet.jpg")
    json.dump({"logo_file": None, "palette_from": None, "palette": [], "tagline": None,
               "note": "no logo collected; propose a palette from the photos"}, open(f"{folder}/brand.json", "w"), indent=1)
    research = {
        "rank": rank, "tier": "extra", "row": row, "business_name": r["business_name"],
        "google": {"maps_url": r["maps_url"], "category": dp.get("category") or r["category"], "rating_label": dp.get("rating_label"),
                   "address": dp.get("address"), "service_area": dp.get("service_area"),
                   "phone": re.sub(r"^phone:tel:", "", dp.get("phone") or r["phone"] or ""),
                   "hours": [h.replace("", "").strip() for h in dp.get("hours") or [] if re.match(r"[A-Z][a-z]+day", h)],
                   "about_text": dp.get("about_text"), "overview_text": dp.get("overview_text"),
                   "reviews_captured_by_me": [{k: x.get(k) for k in ("reviewer", "when", "stars", "text", "owner_reply")} for x in dp.get("reviews") or []]},
        "email": {"address": r["email"], "published_at": r["email_source_url"], "quote": r["email_source_quote"], "check": r["email_check"]},
        "facebook_url": r["facebook_url"] or None, "instagram_url": r["instagram_url"] or None,
        "owner_name_from_research": clean(t3.get("owner_name")),
        "gemini_research_record": {k: clean(t3.get(k)) for k in ("facebook_followers", "facebook_latest_post_date", "instagram_followers",
                                    "website_found", "website_status", "sources_checked", "notes")},
        "note": "No Gemini content dive for this business: use the Google capture; gemini_research_record comes from the email search.",
    }
    json.dump(research, open(f"{folder}/research.json", "w"), indent=1)
    print(os.path.basename(folder), len(imgs), "images")
