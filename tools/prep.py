#!/usr/bin/env python3
"""Split ledger into site-check queue vs. pre-gate rejects (no website / out-of-niche Maps category)."""
import json
D = "/home/user/100homeimprovementsearch/data"
BAD_CAT = {"Handyman/Handywoman/Handyperson", "Flooring store", "Flooring contractor", "Roofing contractor", "Countertop store",
           "Tile store", "Plumbing supply store", "Siding contractor", "Painter", "Home improvement store", "Deck builder",
           "Shower door shop", "Kitchen supply store", "Kitchen furniture store", "Bathroom supply store", "Plumber",
           "Window installation service", "HVAC contractor", "Furniture store", "Appliance store", "Granite supplier",
           "Countertop contractor", "Glass & mirror shop", "Pool contractor", "Fence contractor", "Landscaper",
           "Electrician", "Architect", "Real estate agency", "Building materials store", "Hardware store"}
q, pre = [], []
for l in open(f"{D}/ledger.jsonl"):
    x = json.loads(l)
    if x["category"] in BAD_CAT:
        pre.append({**x, "gate": "NICHE", "reason": f"Google Maps primary category '{x['category']}' is outside the niche"})
    elif not x["website"]:
        pre.append({**x, "gate": "G2", "reason": "no website listed on the Google Business Profile (listing only)"})
    else:
        q.append(x)
open(f"{D}/site_queue.jsonl", "w").write("".join(json.dumps(x) + "\n" for x in q))
open(f"{D}/pregate_rejects.jsonl", "w").write("".join(json.dumps(x) + "\n" for x in pre))
print(len(q), "queued;", len(pre), "pre-gate rejects")
