#!/usr/bin/env python3
"""Re-measure 'gallery images over 1MB' defects for passed prospects with two client profiles:
(a) Chrome-like Accept: image/avif,image/webp,*/*  (b) curl default Accept: */*. Full body downloaded, bytes counted."""
import csv, json, re, requests
O = "/home/user/100homeimprovementsearch/output"; D = "/home/user/100homeimprovementsearch/data"
CH = {"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_5 like Mac OS X) AppleWebKit/605.1.15 Version/17.5 Mobile/15E148 Safari/604.1",
      "Accept": "image/avif,image/webp,image/apng,image/*,*/*;q=0.8"}
CU = {"User-Agent": "curl/8.5.0", "Accept": "*/*"}
done = {json.loads(l)["id"] for l in open(f"{D}/remeasure.jsonl")} if __import__("os").path.exists(f"{D}/remeasure.jsonl") else set()
out = open(f"{D}/remeasure.jsonl", "a")
for r in csv.DictReader(open(f"{O}/prospects100.csv")):
    if not r["G8_defect"].startswith("gallery images") or r["prospect_id"] in done:
        continue
    urls = re.findall(r"(https?://\S+?) = [\d,]+ bytes", r["G8_measurement"])
    rec = {"id": r["prospect_id"], "measured_on": "2026-10-14", "images": []}
    for u in urls:
        row = {"url": u}
        for name, h in (("browser_accept", CH), ("curl_accept", CU)):
            try:
                b = requests.get(u, headers=h, timeout=60).content
                row[name] = len(b)
            except Exception as e:
                row[name] = f"error {type(e).__name__}"
        rec["images"].append(row)
    rec["over_1mb_browser"] = sum(1 for x in rec["images"] if isinstance(x.get("browser_accept"), int) and x["browser_accept"] > 1_000_000)
    rec["over_1mb_curl"] = sum(1 for x in rec["images"] if isinstance(x.get("curl_accept"), int) and x["curl_accept"] > 1_000_000)
    out.write(json.dumps(rec) + "\n"); print(rec["id"], rec["over_1mb_browser"], rec["over_1mb_curl"])
