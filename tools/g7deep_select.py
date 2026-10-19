#!/usr/bin/env python3
"""Pick firms for the deep G7 crawl: alive on every other automated gate (niche, G3 or vendor credit, G5, G8, G9 not FAIL)
but G7 FAIL on the home + gallery check, and not yet deep-crawled. Usage: g7deep_select.py <out ids.txt>"""
import sys
sys.path.insert(0, "/home/user/100homeimprovementsearch/tools")
from decide import load, evaluate, g3, jl, D  # noqa: E402

data = load()
L, site, pre = data[0], data[1], data[7]
done = {x["id"] for x in jl(f"{D}/g7deep_done.jsonl")}
out = []
for cid, c in L.items():
    if cid in pre or cid in done or c.get("dup_of") or cid not in site:
        continue
    r = evaluate(c, data)
    g = r["gates"]
    if g.get("G2") != "PASS" or r.get("niche") == "FAIL" or g.get("G7") != "FAIL":
        continue
    if g.get("G3") != "PASS" and not g3(c, site[cid])[1].get("g3_vendor"):
        continue
    if "FAIL" in (g.get("G1"), g.get("G5"), g.get("G8"), g.get("G9")):
        continue
    out.append(cid)
open(sys.argv[1], "w").write("\n".join(out) + "\n")
print("selected", len(out))
