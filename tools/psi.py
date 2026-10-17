#!/usr/bin/env python3
"""G8 PageSpeed Insights attempt: one call + one retry per URL, recording PSI_TIMEOUT on 429/timeout.
Usage: psi.py <in.jsonl id,url> <out.jsonl>"""
import json, os, sys, time, requests
from datetime import datetime, timezone
inp, outp = sys.argv[1], sys.argv[2]
done = set()
try:
    # retry ids whose earlier attempt ended in PSI_TIMEOUT; the newest line per id wins in decide.load
    done = {x["id"] for x in map(json.loads, open(outp)) if isinstance(x.get("psi_score"), int)}
except FileNotFoundError:
    pass
with open(outp, "a") as fo:
    for l in open(inp):
        c = json.loads(l)
        if c["id"] in done:
            continue
        api = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed"
        rec = {"id": c["id"], "tested_url": c["url"], "attempts": []}
        for attempt in (1, 2):
            t = datetime.now(timezone.utc).isoformat(timespec="seconds")
            try:
                r = requests.get(api, params={"url": c["url"], "strategy": "mobile", "category": "performance",
                                         **({"key": os.environ["GOOGLE_API_KEY"]} if os.environ.get("GOOGLE_API_KEY") else {})}, timeout=120)
                if r.status_code == 200:
                    sc = r.json()["lighthouseResult"]["categories"]["performance"]["score"]
                    rec.update(psi_score=round(sc * 100), psi_date=t)
                    rec["attempts"].append({"at": t, "http": 200})
                    break
                rec["attempts"].append({"at": t, "http": r.status_code, "msg": r.text[:140].replace(os.environ.get("GOOGLE_API_KEY") or "\0", "<key>")})
            except Exception as e:
                rec["attempts"].append({"at": t, "error": type(e).__name__})
            time.sleep(3)
        if "psi_score" not in rec:
            rec["psi_score"] = "PSI_TIMEOUT"
        fo.write(json.dumps(rec) + "\n"); fo.flush()
