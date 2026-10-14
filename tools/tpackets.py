#!/usr/bin/env python3
"""Template-capture packets for passed prospects not yet captured. Usage: tpackets.py <wave-tag>"""
import csv, json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from decide import load, evaluate, jl, D, O
tag = sys.argv[1]
data = load(); L, site, maps, br, psi, dns, manual, pre = data
done = {x["id"] for x in jl(f"{D}/template/*.jsonl")}
if os.path.exists(f"{D}/tdispatched.txt"):
    done |= {l.strip() for l in open(f"{D}/tdispatched.txt")}
by = {}
for r in csv.DictReader(open(f"{O}/prospects100.csv")):
    cid = r["prospect_id"]
    if cid in done:
        continue
    ev = evaluate(L[cid], data)["ev"]; m = maps.get(cid) or {}; man = manual.get(cid) or {}
    by.setdefault(r["region"], []).append({
        "id": cid, "name": r["business_name"], "website": r["final_url"], "pages_fetched": site[cid].get("pages_fetched"),
        "g7_urls": ev.get("g7_urls"), "gbp_reviews_visible": [{k: x.get(k) for k in ("reviewer", "when", "stars", "text")} for x in m.get("reviews") or []],
        "gbp_url": m.get("gbp_url"), "g8_defect": [r["G8_defect"], r["G8_measurement"]], "trigger": (man.get("score") or {}).get("trigger"),
        "decision_maker": man.get("decision_maker"), "assessment": man.get("assessment")})
ids = []
for reg, lst in by.items():
    json.dump(lst, open(f"{D}/packets/T_{reg}_{tag}.json", "w"), indent=1)
    ids += [x["id"] for x in lst]
    print(reg, len(lst))
open(f"{D}/tdispatched.txt", "a").write("".join(i + "\n" for i in ids))
