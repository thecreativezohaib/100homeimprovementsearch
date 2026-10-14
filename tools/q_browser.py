#!/usr/bin/env python3
"""Queue for browser.js + psi.py: candidates still alive after cheap gates (>=1 auto G4 signal, G7 auto pass)."""
import json, sys
sys.path.insert(0, "/home/user/100homeimprovementsearch/tools")
from decide import load, niche, g3, g4, g5, g7, jl, D
data = load(); L = data[0]
done_b = {x["id"] for x in jl(f"{D}/browser*.jsonl")}
done_p = {x["id"] for x in jl(f"{D}/psi.jsonl")}
qb, qp = [], []
for cid, c in L.items():
    s, m = data[1].get(cid), data[2].get(cid)
    if not s or s.get("g2") != "PASS" or not m or not m.get("title"):
        continue
    if niche(c, s, None)[0] == "FAIL":
        continue
    st3, e3 = g3(c, s)
    if st3 != "PASS" and not e3.get("g3_vendor"):
        continue
    st4, e4 = g4(c, s, m, None)
    if not e4.get("g4_signals") or st4 == "FAIL":
        continue
    if g5(c, s, None)[0] == "FAIL" or g7(c, s, None)[0] != "PASS":
        continue
    gal = [u for u in (s.get("pages_fetched") or {}).get("gallery", []) if u != s["final_url"]]
    item = {"id": cid, "url": s["final_url"], "gallery": gal[0] if gal else None}
    if cid not in done_b: qb.append(item)
    if cid not in done_p: qp.append(item)
open(f"{D}/bq_queue.jsonl", "w").write("".join(json.dumps(x) + "\n" for x in qb))
open(f"{D}/psi_queue.jsonl", "w").write("".join(json.dumps(x) + "\n" for x in qp))
print("browser", len(qb), "psi", len(qp))
