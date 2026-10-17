#!/usr/bin/env python3
"""Coordinator gallery override: rebuild gallery_urls_8 from the strict-G7 kept list, dropping the contact-sheet
positions (1-based) that the visual review excluded (renderings, stock, badges, maps, people shots).
Appends to data/template/zz_coord.jsonl. Usage: gallery_fix.py"""
import json
D = "/home/user/100homeimprovementsearch/data"
EXCLUDE = {"remontremodel.com": [1, 2], "niptuckremodel.com": [8], "allexclusivepro.com": [1, 2, 3, 5],
           "kbfdesigngallery.com": [1, 5, 11], "ananiremodeling.com": [2], "degnandesignbuildremodel.com": [6],
           "newberryhome.com": [9], "sweeneydesign.com": [1, 2, 7], "cs-enterprises.net": [1, 2, 6, 9], "elmbuilds.com": [11], "alphagenco.com": [8, 12], "havenrenokc.com": [4, 8, 12]}
kept = {}
for l in open(f"{D}/g7verify.jsonl"):
    x = json.loads(l)
    kept[x["id"]] = x.get("kept") or []
with open(f"{D}/template/zz_coord.jsonl", "a") as f:
    for cid, ex in EXCLUDE.items():
        urls = [u for i, u in enumerate(kept[cid], 1) if i not in ex][:8]
        f.write(json.dumps({"id": cid, "gallery_urls_8": urls,
                            "coord_note": f"gallery rebuilt from strict-G7 kept images excluding contact-sheet positions {ex}"}) + "\n")
        print(cid, len(urls))
