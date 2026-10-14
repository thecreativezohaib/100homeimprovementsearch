#!/usr/bin/env python3
"""Extra measured G8 checks: (a) mailto: domains with no MX and no A record (dead email link) via Google DoH;
(b) <form action> on home/contact pages pointing to a host that does not resolve or returns 404/410."""
import json, re, sys, requests
from urllib.parse import urljoin, urlparse
sys.path.insert(0, "/home/user/100homeimprovementsearch/tools")
from decide import load, jl, D
from sitecheck import HDRS
data = load(); site = data[1]
done = {x["id"] for x in jl(f"{D}/g8extra.jsonl")}
ids = [x["id"] for x in jl(f"{D}/bq_queue.jsonl")] + [l.strip() for l in open(f"{D}/g8extra_more.txt")] if __import__("os").path.exists(f"{D}/g8extra_more.txt") else [x["id"] for x in jl(f"{D}/bq_queue.jsonl")]
def doh(name, t):
    try:
        return requests.get(f"https://dns.google/resolve?name={name}&type={t}", timeout=15).json()
    except Exception:
        return {}
with open(f"{D}/g8extra.jsonl", "a") as fo:
    for cid in dict.fromkeys(ids):
        s = site.get(cid)
        if not s or cid in done or s.get("g2") != "PASS":
            continue
        rec = {"id": cid, "dead_mail": [], "dead_forms": [], "checked": "2026-10-14"}
        for m in s.get("mailto_links") or []:
            dom = requests.utils.unquote(m).split("@")[-1].split("?")[0].strip().lower()
            if not dom or "." not in dom:
                continue
            mx, a = doh(dom, "MX"), doh(dom, "A")
            if not mx.get("Answer") and not a.get("Answer"):
                rec["dead_mail"].append({"mailto": m, "domain": dom, "mx_status": mx.get("Status"), "a_status": a.get("Status"),
                                         "method": f"https://dns.google/resolve?name={dom}&type=MX and type=A: no answers"})
        # G3 supplement: agency credits without a "by" phrase, e.g. "(c) 2026 | ... - Top Floor Marketing"
        rec["footer_vendor_links"] = []
        try:
            h0 = requests.get(s["final_url"], headers=HDRS, timeout=20).text
            from bs4 import BeautifulSoup
            sp = BeautifulSoup(h0, "lxml")
            foot = sp.find_all("footer") or []
            scope = foot[-1] if foot else None
            anchors = scope.find_all("a", href=True) if scope else []
            if not anchors:
                tail = h0[int(len(h0) * 0.85):]
                anchors = BeautifulSoup(tail, "lxml").find_all("a", href=True)
            own = urlparse(s["final_url"]).hostname.replace("www.", "")
            for a in anchors:
                href = a["href"]; host = (urlparse(href).hostname or "").replace("www.", "")
                txt = a.get_text(" ", strip=True)[:80]
                if not host or own.split(".")[-2] in host or re.search(r"facebook|instagram|google|yelp|houzz|linkedin|twitter|x\.com|youtube|pinterest|tiktok|nextdoor|bbb\.org|angi|homeadvisor|thumbtack|guildquality|nari|nkba|wordpress|wix|squarespace|godaddy|weebly|webflow|elementor|apple|maps|bing|porch|buildzoom|trustindex|elfsight|privacy|termly|cookie|ada|accessib|nahb|remodelers|license|cslb|state\.|\.gov|mapquest", host + " " + txt, re.I):
                    continue
                if re.search(r"marketing|media|digital|design|web|studio|creative|seo|agency|interactive|solutions|sites|develop", host + " " + txt, re.I):
                    rec["footer_vendor_links"].append({"text": txt, "href": href[:150], "domain": host})
        except Exception:
            pass
        pages = [u for k in ("home", "contact") for u in (s.get("pages_fetched") or {}).get(k, [])]
        for u in pages[:3]:
            try:
                h = requests.get(u, headers=HDRS, timeout=20).text
            except Exception:
                continue
            for act in re.findall(r'<form[^>]*action=["\']([^"\']+)["\']', h, re.I):
                full = urljoin(u, act)
                host = urlparse(full).hostname
                if not host or full.startswith(("mailto:", "javascript:")):
                    continue
                d = doh(host, "A")
                if d.get("Status") == 3:
                    rec["dead_forms"].append({"page": u, "action": full, "result": "form action host does not resolve (DoH NXDOMAIN)"})
                    continue
                try:
                    r = requests.get(full, headers=HDRS, timeout=15, allow_redirects=True)
                    if r.status_code in (404, 410):
                        rec["dead_forms"].append({"page": u, "action": full, "result": f"GET form action -> HTTP {r.status_code}"})
                except Exception as e:
                    pass
        fo.write(json.dumps(rec) + "\n"); fo.flush()
