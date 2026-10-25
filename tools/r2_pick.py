#!/usr/bin/env python3
"""Rank the round 2 finalists and write output/round2/R2_FINALISTS.csv: 100 main, 20 reserves, the rest as backup.
Score: email confirmed on its source page by me (+2), qualified in the first rounds (+1), both Facebook and
Instagram (+0.5), Google reviews (up to +2, more reviews mean more homepage content).
Usage: r2_pick.py"""
import csv, json, re
D, O = "/home/user/100homeimprovementsearch/data/r2", "/home/user/100homeimprovementsearch/output/round2"
F = json.load(open(f"{D}/finalists.json"))
for x in F:
    x["score"] = round((2 if x["source_check"] == "verified" else 0) + (1 if x["origin"] == "qualified34" else 0)
                       + (0.5 if x["facebook_url"] and x["instagram_url"] else 0) + min(x["reviews_count"] or 0, 50) / 25, 2)
F.sort(key=lambda x: -x["score"])
cols = ["rank", "tier", "row", "business_name", "category", "phone", "address", "rating_label", "reviews_count",
        "email", "email_source_url", "email_source_quote", "email_check", "facebook_url", "instagram_url",
        "website_note", "maps_url", "score"]
with open(f"{O}/R2_FINALISTS.csv", "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=cols)
    w.writeheader()
    for i, x in enumerate(F, 1):
        w.writerow({"rank": i, "tier": "main" if i <= 100 else "reserve" if i <= 120 else "backup", "row": x["row"],
                    "business_name": x["title"] or x["business_name"], "category": x["category"],
                    "phone": re.sub(r"^phone:tel:", "", x["phone"] or ""), "address": x["address"] or "service area",
                    "rating_label": (x["rating_label"] or "").replace("\n", " "), "reviews_count": x["reviews_count"],
                    "email": x["email"], "email_source_url": x["email_source_url"], "email_source_quote": x["email_source_quote"],
                    "email_check": {"verified": "seen on source page", "unfetchable": "source is Facebook/Instagram or blocked (Gemini quote)",
                                    "missing": "source page did not show it (Gemini quote)"}[x["source_check"]] + "; mail server OK",
                    "facebook_url": x["facebook_url"], "instagram_url": x["instagram_url"],
                    "website_note": x["website_found"] or "none found", "maps_url": x["maps_url"], "score": x["score"]})
json.dump(F, open(f"{D}/finalists_ranked.json", "w"), indent=1)
print(len(F), "main 100, reserve", min(20, max(0, len(F) - 100)), "backup", max(0, len(F) - 120))
