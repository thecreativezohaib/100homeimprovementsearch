#!/usr/bin/env python3
"""Apply the dm_scan.py owner and email patterns to rendered page text (render_text.js output).
Usage: dm_from_render.py <out.jsonl> <rt_out*.jsonl ...>"""
import json, re, sys
sys.path.insert(0, "/home/user/100homeimprovementsearch/tools")
from dm_scan import PATS, EMAIL, words  # noqa: E402
with open(sys.argv[1], "w") as f:
    for path in sys.argv[2:]:
        for l in open(path):
            r = json.loads(l); out = {"id": r["id"], "dm_candidates": [], "emails": [], "rendered": True}
            seen = set()
            for p in r.get("pages", []):
                text = re.sub(r"\s+", " ", p.get("text") or "")
                for h in p.get("mailto") or []:
                    e = h[7:].split("?")[0].strip()
                    if e and e.lower() not in {x["email"].lower() for x in out["emails"]}:
                        out["emails"].append({"email": e, "how": "mailto", "page": p["url"]})
                for e in EMAIL.findall(text):
                    if e.lower() not in {x["email"].lower() for x in out["emails"]} and not e.lower().endswith((".png", ".jpg", ".webp")):
                        out["emails"].append({"email": e, "how": "visible text", "page": p["url"]})
                for pat in PATS:
                    for m in pat.finditer(text):
                        name = m.group(1)
                        if (name, p["url"]) in seen or name.split()[0] in ("Our", "The", "Meet", "About", "Contact", "Call", "Kitchen", "Bath", "Home"):
                            continue
                        seen.add((name, p["url"]))
                        out["dm_candidates"].append({"name": name, "page": p["url"], "quote": words(text, m.start(), m.end())})
            f.write(json.dumps(out) + "\n")
