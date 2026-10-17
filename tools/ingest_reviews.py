#!/usr/bin/env python3
"""Merge user-supplied newest-review dates (Gemini via Google Maps) into data/reviews_user.jsonl.
Usage: ingest_reviews.py <targets.csv> <results.csv> [<results.csv> ...]
Rows join on `row`; only ISO dates (YYYY-MM-DD) with a non-empty review quote are kept. Newer files win per id."""
import csv, json, re, sys

D = "/home/user/100homeimprovementsearch/data"
targets = {r["row"]: r for r in csv.DictReader(open(sys.argv[1]))}
recs = {}
try:
    for l in open(f"{D}/reviews_user.jsonl"):
        x = json.loads(l)
        recs[x["id"]] = x
except FileNotFoundError:
    pass
added, skipped = 0, 0
for path in sys.argv[2:]:
    for r in csv.DictReader(open(path, encoding="utf-8-sig")):
        t = targets.get((r.get("row") or "").strip())
        d = (r.get("newest_review_when") or "").strip()
        q = (r.get("newest_review_first_words") or "").strip().strip('"')
        if not t or not re.match(r"\d{4}-\d{2}-\d{2}$", d) or q in ("", "UNKNOWN"):
            skipped += 1
            continue
        if (r.get("maps_url") or "").strip() and r["maps_url"].strip() != t["maps_url"]:
            skipped += 1
            continue
        recs[t["prospect_id"]] = {
            "id": t["prospect_id"], "row": int(t["row"]), "date": d, "url": t["maps_url"],
            "source": "Google Maps review data gathered with Gemini and supplied by the user, checked_on "
                      + (r.get("checked_on") or "UNKNOWN").strip() + "; not opened by the coordinator",
            "quote": " ".join(q.split()[:15]), "status_note": (r.get("status_note") or "").strip()}
        added += 1
with open(f"{D}/reviews_user.jsonl", "w") as f:
    for x in recs.values():
        f.write(json.dumps(x) + "\n")
print("added/updated", added, "skipped", skipped, "total", len(recs))
