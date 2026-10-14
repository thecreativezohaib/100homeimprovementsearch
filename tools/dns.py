#!/usr/bin/env python3
"""G2 second route for DNS failures: Google DNS-over-HTTPS lookup of the host (and its root)."""
import json, requests, sys
from urllib.parse import urlparse
D = "/home/user/100homeimprovementsearch/data"
done = set()
try:
    done = {json.loads(l)["id"] for l in open(f"{D}/dns.jsonl")}
except FileNotFoundError:
    pass
with open(f"{D}/dns.jsonl", "a") as fo:
    for l in open(f"{D}/site.jsonl"):
        s = json.loads(l)
        if s.get("g2") not in ("RETRY_BROWSER", "ERROR") or s["id"] in done:
            continue
        if "NameResolution" not in (s.get("g2_reason") or "") and "resolve host" not in (s.get("g2_reason") or ""):
            continue
        host = urlparse(s["input_url"]).hostname
        out = {"id": s["id"], "host": host}
        for h in dict.fromkeys([host, host[4:] if host.startswith("www.") else host]):
            u = f"https://dns.google/resolve?name={h}&type=A"
            r = requests.get(u, timeout=20).json()
            out.setdefault("lookups", []).append({"doh_url": u, "Status": r.get("Status"), "Answer": r.get("Answer")})
        out["nxdomain"] = all(x["Status"] == 3 or not x.get("Answer") for x in out["lookups"])
        out["doh_url"] = out["lookups"][0]["doh_url"]; out["status"] = out["lookups"][0]["Status"]
        fo.write(json.dumps(out) + "\n")
