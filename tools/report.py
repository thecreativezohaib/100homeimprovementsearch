#!/usr/bin/env python3
"""Build output/REPORT_data.json: counts and lists that the final report is written from."""
import csv, json, os, sys
from collections import Counter
sys.path.insert(0, os.path.dirname(__file__))
from decide import jl, D, O

f = json.load(open(f"{O}/funnel.json"))
rows = list(csv.DictReader(open(f"{O}/prospects100.csv")))
rej = list(csv.DictReader(open(f"{O}/rejected.csv")))
gate = Counter(r["failed_gate"] for r in rej)
defects = Counter(r["G8_defect"] for r in rows)
trig = Counter()
for r in rows:
    v = r.get("score_trigger_evidence") or ""
    trig["NONE FOUND" if v.startswith("NONE") else ("UNKNOWN" if v == "UNKNOWN" else "event")] += 1
temptations, cnc = [], Counter()
for x in jl(f"{D}/manual/R*.jsonl"):
    for t in x.get("inference_rejected") or []:
        temptations.append({"id": x["id"], "text": t if isinstance(t, str) else json.dumps(t)})
    for t in x.get("could_not_check") or []:
        cnc[(t if isinstance(t, str) else json.dumps(t))[:160]] += 1
out = {"funnel": f, "rejections_per_gate": dict(gate.most_common()), "passed": len(rows),
       "top10": [{k: r[k] for k in ("rank", "score_total", "business_name", "region", "score_trigger_evidence", "G8_defect")} for r in rows[:10]],
       "defects": dict(defects.most_common()), "trigger_summary": dict(trig),
       "g9_signals": dict(Counter(r["G9_signal"] for r in rows).most_common()),
       "temptations": temptations, "could_not_check": [k for k, _ in cnc.most_common(60)],
       "agents_manual_records": len(jl(f"{D}/manual/R*.jsonl"))}
json.dump(out, open(f"{O}/REPORT_data.json", "w"), indent=1)
print(json.dumps({k: v for k, v in out.items() if k not in ("temptations", "could_not_check")}, indent=1))
print("temptations", len(temptations))
