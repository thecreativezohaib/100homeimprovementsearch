#!/usr/bin/env python3
"""Round 3 strict qualification of all 200 leads. A business qualifies only when every gate passes:
  G1 no working website (Google listing, email domain, free builders all checked)
  G2 identity: a real Google listing with the same phone
  G3 email: published by the business itself and seen there (a page I opened, or its own Facebook/Instagram page as
     reported with the exact URL), matching the business or owner, domain with MX; never a group post or another
     business's page
  G4 its own Facebook or Instagram
  G5 at least 10 photos of its own work (checked by eye on contact sheets: Google photos plus photos from its own pages)
  G6 kitchen or bath work shown
  G7 established and likely to buy: Google rating >= 4.5 from >= 10 reviews, newest review within 24 months
  G8 no red flags (closed, serious complaints, identity doubts)
Writes output/round3/R3_STRICT.csv (every lead, verdict PASS / NEEDS / FAIL, reasons) and R3_STRICT_NEEDS.csv (what
would let a NEEDS business pass). Judgments that need eyes (photo counts, kitchen and bath, email evidence) are
recorded below with the reason.
Usage: r3_strict.py"""
import csv, glob, json, re

R = "/home/user/100homeimprovementsearch"
D = f"{R}/data/r3"

# G5: own-work photos counted on the contact sheets (Google Maps photos + photos from the business's own pages)
PHOTOS = {2: 7, 3: 8, 4: 7, 5: 2, 6: 10, 7: 10, 8: 15, 9: 10, 10: 2, 12: 5, 13: 13, 14: 2, 16: 13, 17: 11, 19: 12, 20: 5,
          21: 7, 22: 4, 24: 1, 25: 11, 26: 10, 27: 24, 28: 8, 29: 27, 30: 5, 31: 0, 32: 6, 33: 9, 34: 1, 35: 3, 37: 14,
          41: 5, 55: 0, 81: 10, 86: 11, 92: 10, 100: 14, 109: 5, 110: 3, 113: 7, 119: 2, 133: 0, 145: 2, 146: 6,
          150: 6, 162: 2, 167: 2, 169: 3, 193: 2, 196: 2, 88: 14, 95: 14, 97: 16, 99: 14, 89: 1, 90: 0, 93: 0, 96: 9}
# G6: no kitchen or bath work in category, photos or reviews
NOT_KB = {26: "handyman (fireplace walls, doors, decks)", 31: "painting", 34: "painting", 41: "painting and exteriors",
          55: "handyman (stoves, chimneys)", 92: "excavation and site work", 113: "home builder, no kitchen or bath shown",
          162: "building firm, deck and basement", 169: "construction, no kitchen or bath shown",
          193: "building restoration", 22: "handyman, no kitchen or bath photos", 35: "general contractor, decks"}
# G3: email evidence. ok = seen on a page I opened, or on the business's own Facebook/Instagram page with the exact URL
EMAIL = {6: ("ok", "HUD licensed installer list (PDF) shows it with the Google phone 531-333-1054"),
         8: ("ok", "Fearrington Cares vendor list shows it with the Google phone 919-542-3722; also on their own Facebook page"),
         4: ("ok", "their own Facebook page facebook.com/kurtzflooringsolutionsllc"),
         7: ("ok", "their own Facebook page facebook.com/FisherTileMT"),
         12: ("ok", "a post on their own Facebook page (id 100084219031246)"),
         26: ("ok", "their own Instagram post"),
         29: ("ok", "the owner's own Facebook profile (Von Dunbar), name matches AIOR Services"),
         30: ("ok", "their own Instagram profile instagram.com/qualityknb"),
         32: ("ok", "their own Instagram post"),
         37: ("ok", "their own Facebook page facebook.com/jgkhomeimprovement; email on their own domain"),
         2: ("proof", "only seen in a Facebook group post"), 9: ("proof", "only seen in a Facebook group post"),
         21: ("proof", "only seen in a Facebook group post"), 24: ("proof", "only seen in a Facebook group post"),
         86: ("proof", "only seen in a Facebook group post (Angi page gone)"),
         100: ("proof", "only seen in a Facebook group post (BBB page gone)"),
         113: ("proof", "only seen in a Facebook group post"),
         3: ("proof", "seen on another business's page (mrbacksplashusa)"),
         27: ("proof", "seen on a different Facebook page (bathtubreglazingspecialists)"),
         28: ("proof", "seen on a Facebook page id that is not their TileEnvyShowroom page")}
FLAGS = {14: "1-star review calls the owner a scam artist", 16: "1-star review: lying about a permit",
         33: "2.8 rating, damage complaint", 34: "Google photos show another company", 119: "3.0 rating",
         133: "3.0 rating, no photos", 193: "temporarily closed", 20: "email from another business's page",
         19: "email from another business's page", 169: "email belongs to MSP Renovation",
         110: "email from Philly's Finest Refinishing page", 196: "Facebook belongs to another business"}
SITE = json.load(open(f"{D}/site_check.json"))
HAS_SITE = {int(k): v for k, v in list(SITE["live"].items()) + list(SITE["unclear"].items())}
HAS_SITE.update({145: "renovations.work", 108: "eaglecabinetsnc.com", 116: "surfacepaintingcompany.com (could not confirm)",
                 127: "restorationbuildercontractor.com (could not confirm)", 96: "grgranitequartz.com (could not confirm)"})
GOOGLE_UNPROVEN = {88, 89, 90, 93, 95, 97, 99}  # only a made-up Maps link so far

maps = {}
for f in glob.glob(f"{D}/*_maps_out*.jsonl"):
    for l in open(f):
        j = json.loads(l)
        if not j.get("error"):
            maps[j["row"]] = j


def gstats(j):
    m = re.search(r"([\d.]+)\s*\(([\d,]+)\)", (j.get("rating_label") or "").replace("\n", " "))
    rating, cnt = (float(m.group(1)), int(m.group(2).replace(",", ""))) if m else (None, 0)
    ages = []
    for r in j.get("reviews") or []:
        mm = re.search(r"(\d+|a|an)\s+(day|week|month|year)", r.get("when") or "")
        if mm:
            k = 1 if mm.group(1) in ("a", "an") else int(mm.group(1))
            ages.append({"day": k / 30, "week": k / 4.3, "month": k, "year": k * 12}[mm.group(2)])
    return rating, cnt, min(ages) if ages else None


leads = list(csv.DictReader(open(f"{R}/output/round3/R3_INPUT_200.csv")))
status = {}
for B in glob.glob("/tmp/claude-0/-home-user-100homeimprovementsearch/*/scratchpad/r3dl/b*/batch_*/INDEX.csv"):
    for r in csv.DictReader(open(B)):
        status[int(r["n"])] = r["status"]
rows, needs = [], []
for L in leads:
    n = int(L["n"])
    st = status.get(n, "")
    fail, need = [], []
    if st == "DUPLICATE":
        fail.append("already in round 2")
    elif st == "HAS_WEBSITE":
        fail.append("has a working website")
    elif n in HAS_SITE:
        (need if "could not confirm" in HAS_SITE[n] else fail).append(f"website on Google: {HAS_SITE[n]}")
    j = maps.get(n)
    rating, cnt, newest = gstats(j) if j else (None, 0, None)
    if not fail:
        if n in GOOGLE_UNPROVEN:
            need.append("Google Maps share link (maps.app.goo.gl) of their listing, same phone")
        elif not j:
            need.append("Google Maps share link (maps.app.goo.gl) of their listing, same phone (none found under this name)")
        else:
            if rating is None or rating < 4.5:
                fail.append(f"Google rating {rating}")
            elif cnt < 10:
                fail.append(f"only {cnt} Google reviews")
            if newest is not None and newest > 24:
                fail.append("no Google review in the last 2 years")
        if n in NOT_KB:
            fail.append(f"no kitchen or bath work ({NOT_KB[n]})")
        if n in FLAGS:
            fail.append(FLAGS[n])
        ph = PHOTOS.get(n, 0)
        if ph < 10:
            need.append(f"{10 - ph} or more photos of their own finished kitchen/bath work from their own Facebook or Instagram (have {ph})")
        ev = EMAIL.get(n, ("proof", "not verified"))
        if ev[0] != "ok":
            need.append(f"screenshot of the email on their own Facebook About, Instagram bio or Google profile ({ev[1]})")
    verdict = "FAIL" if fail else ("NEEDS" if need else "PASS")
    rows.append({"n": n, "verdict": verdict, "business_name": L["business_name"], "phone": L["phone"],
                 "google_rating": rating or "", "google_reviews": cnt or "", "newest_review_months": newest if newest is not None else "",
                 "own_work_photos": PHOTOS.get(n, ""), "email": L["email"], "email_evidence": EMAIL.get(n, ("", ""))[1],
                 "fail_reasons": "; ".join(fail), "needs": "; ".join(need)})
    if verdict == "NEEDS":
        needs.append({"n": n, "business_name": L["business_name"], "phone": L["phone"], "facebook_url": L["facebook_url"],
                      "instagram_url": L["instagram_url"], "email": L["email"], "needs": " | ".join(need)})
for fn, data in (("R3_STRICT.csv", rows), ("R3_STRICT_NEEDS.csv", needs)):
    with open(f"{R}/output/round3/{fn}", "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(data[0]))
        w.writeheader()
        w.writerows(data)
from collections import Counter
print(Counter(r["verdict"] for r in rows))
print("PASS:", [(r["n"], r["business_name"]) for r in rows if r["verdict"] == "PASS"])
print("NEEDS without Google issue:", [(r["n"], r["needs"][:80]) for r in rows if r["verdict"] == "NEEDS" and "share link" not in r["needs"]])
