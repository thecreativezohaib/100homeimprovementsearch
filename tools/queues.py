#!/usr/bin/env python3
"""Build incremental queues: render (blocked / JS-only sites) and maps (G3 survivors)."""
import json, sys
sys.path.insert(0, "/home/user/100homeimprovementsearch/tools")
from decide import load, niche, g3, jl, D
which = sys.argv[1]
data = load(); L = data[0]
if which == "render":
    dns = {x["id"] for x in jl(f"{D}/dns.jsonl")}
    done = {x["id"] for x in jl(f"{D}/site_render.jsonl")}
    raw = {x["id"]: x for x in jl(f"{D}/site.jsonl") + jl(f"{D}/site_b.jsonl")}
    q = []
    for x in jl(f"{D}/site_queue.jsonl"):
        s = raw.get(x["id"])
        if not s or x["id"] in done:
            continue
        if (s.get("g2") in ("RETRY_BROWSER", "ERROR") and x["id"] not in dns) or \
           (s.get("g2") == "PASS" and (s.get("home_text_len") or 0) < 600):
            q.append(x)
    open(f"{D}/render_queue.jsonl", "w").write("".join(json.dumps(x) + "\n" for x in q))
    print("render queue", len(q))
else:
    done = {x["id"] for x in jl(f"{D}/maps_*.jsonl") if x.get("title")}
    q = []
    for cid, c in L.items():
        s = data[1].get(cid)
        if not s or s.get("g2") != "PASS" or not c.get("place_id") or cid in done:
            continue
        if niche(c, s, None)[0] == "FAIL" or g3(c, s)[0] != "PASS":
            continue
        q.append({"id": cid, "place_id": c["place_id"]})
    open(f"{D}/maps_queue.jsonl", "w").write("".join(json.dumps(x) + "\n" for x in q))
    print("maps queue", len(q))
