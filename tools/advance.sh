#!/bin/bash
# Advance every firm whose remaining automated gaps are G8/G9: browser capture + PSI for those missing them,
# then rebuild agent packets (packets.py) and the cumulative Gemini file. Safe to run repeatedly.
cd /home/user/100homeimprovementsearch/tools
python3 - <<'PY'
import json, sys
sys.path.insert(0, ".")
from decide import load, evaluate
d = load(); L, site, maps, br, psi, dns, man = d[:7]
disp = {l.strip() for l in open("../data/dispatched.txt")}
qb, qp = [], []
for cid, c in L.items():
    s, m = site.get(cid), maps.get(cid)
    if cid in man or cid in disp or not s or s.get("g2") != "PASS" or not m or not m.get("title") or c.get("dup_of"):
        continue
    ev = evaluate(c, d); g = ev["gates"]
    if ev.get("niche") == "FAIL" or g.get("G7") != "PASS":
        continue
    if [k for k, v in g.items() if v == "FAIL" and k != "G4"]:
        continue
    gal = [u for u in (s.get("pages_fetched") or {}).get("gallery", []) if u != s["final_url"]]
    row = {"id": cid, "url": s["final_url"], "gallery": gal[0] if gal else None}
    if cid not in br:
        qb.append(row)
    if not isinstance((psi.get(cid) or {}).get("psi_score"), int):
        qp.append(row)
for k in range(4):
    open(f"../data/bq_adv{k}.jsonl", "w").write("".join(json.dumps(x) + "\n" for x in qb[k::4]))
for k in range(4):
    open(f"../data/pq_adv{k}.jsonl", "w").write("".join(json.dumps(x) + "\n" for x in qp[k::4]))
print("browser", len(qb), "psi", len(qp))
PY
N=$(date +%s)
for k in 0 1 2 3; do [ -s ../data/bq_adv$k.jsonl ] && node browser.js ../data/bq_adv$k.jsonl ../data/browser_adv$N-$k.jsonl 2>> ../data/browser.log & done
for k in 0 1 2 3; do [ -s ../data/pq_adv$k.jsonl ] && python3 psi.py ../data/pq_adv$k.jsonl ../data/psi_q$((k+4)).jsonl > /dev/null 2>&1 & done
wait
rm -f ../data/packets/R?.json
python3 packets.py | tail -1
python3 gemini_next.py
echo ADVANCE_DONE
