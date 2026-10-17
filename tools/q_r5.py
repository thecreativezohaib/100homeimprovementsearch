#!/usr/bin/env python3
"""Round-5 queues for ids in data/site_queue_r5.jsonl that survive the cheap gates (G2, niche, G3, G5, G7),
with or without a G4 signal (review dates may come from the user later).
Usage: q_r5.py social|browser|psi"""
import json, sys
sys.path.insert(0, "/home/user/100homeimprovementsearch/tools")
from decide import load, niche, g3, g5, g7, jl, D
which = sys.argv[1]
import os
QF = os.environ.get("SITE_QUEUE", "site_queue_r5.jsonl")
ids = {json.loads(l)["id"] for l in open(f"{D}/{QF}")}
data = load(); L, site, maps, br, psi = data[:5]
alive = []
for cid in ids:
    c, s, m = L.get(cid), site.get(cid), maps.get(cid)
    if not c or c.get("dup_of") or not s or s.get("g2") != "PASS" or not m or not m.get("title"):
        continue
    if niche(c, s, None)[0] == "FAIL" or g3(c, s)[0] != "PASS" or g5(c, s, None)[0] == "FAIL" or g7(c, s, None)[0] != "PASS":
        continue
    gal = [u for u in (s.get("pages_fetched") or {}).get("gallery", []) if u != s["final_url"]]
    alive.append({"id": cid, "url": s["final_url"], "gallery": gal[0] if gal else None})
if which == "social":
    done = {x["id"] for x in jl(f"{D}/social.jsonl")}
    open(f"{D}/social_r5_ids.txt", "w").write("".join(x["id"] + "\n" for x in alive if x["id"] not in done))
elif which == "browser":
    q = [x for x in alive if x["id"] not in br]
    for k in range(4):
        open(f"{D}/bqr5_{k}.jsonl", "w").write("".join(json.dumps(x) + "\n" for x in q[k::4]))
elif which == "psi":
    q = [x for x in alive if not isinstance((psi.get(x["id"]) or {}).get("psi_score"), int)]
    for k in range(6):
        open(f"{D}/psir5_in{k}.jsonl", "w").write("".join(json.dumps(x) + "\n" for x in q[k::6]))
print(which, "alive", len(alive))
