#!/usr/bin/env python3
"""Owner scan for agent-confirmed kitchen and bath firms that stopped at G4 (agents never reached G6 for them).
Fetches the home page and the firm's own about / team / story / contact pages, and records every verbatim snippet
(at most 20 words) where a full name (two or more capitalised words) sits next to an ownership role
(owner, co-owner, founder, co-founder, president, CEO, principal, proprietor). Also records mailto / visible emails.
Every snippet is reviewed by the coordinator before use; nothing is inferred. Usage: dm_scan.py <ids.json> <out.jsonl>"""
import json, re, sys
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urljoin, urlparse
import requests
from bs4 import BeautifulSoup
sys.path.insert(0, "/home/user/100homeimprovementsearch/tools")
from sitecheck import HDRS  # noqa: E402
ROLE = r"(?:Co-?Owner|Owner|Co-?Founder|Founder|President|CEO|Principal|Proprietor)"
NAME = r"(?:[A-Z][a-z]+(?:\s+[A-Z]\.)?(?:\s+(?:[A-Z][a-z]+|Mc[A-Z][a-z]+|O'[A-Z][a-z]+)(?:-[A-Z][a-z]+)?){1,2})"
PATS = [re.compile(rf"\b({NAME})\s*(?:,|-|–|\||is the|is our|,\s*the|serves as)\s*(?:and\s+)?{ROLE}\b"),
        re.compile(rf"\b{ROLE}(?:\s*(?:&|and)\s*{ROLE})?\s*[:,\-–]?\s*({NAME})\b")]
PAGE = re.compile(r"about|team|story|who-we-are|meet|owner|founder|contact|staff|people|history", re.I)
EMAIL = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")


def get(sess, u):
    try:
        r = sess.get(u, headers=HDRS, timeout=20)
        return r.text if r.status_code == 200 else None
    except Exception:
        return None


def words(t, a, b):  # at most 20 whitespace words of verbatim text around the match
    w = t.split()
    pre = len(t[:a].split()); end = len(t[:b].split())
    lo = max(0, pre - (20 - (end - pre)) // 2)
    return " ".join(w[lo:lo + 20])


def one(cid, home):
    sess = requests.Session(); out = {"id": cid, "dm_candidates": [], "emails": [], "pages": []}
    h = get(sess, home)
    if not h:
        return out
    host = urlparse(home).netloc.replace("www.", "")
    pages = [home]
    for a in BeautifulSoup(h, "lxml").find_all("a", href=True):
        u = urljoin(home, a["href"]).split("#")[0]
        if urlparse(u).netloc.replace("www.", "") == host and u not in pages and (PAGE.search(u) or PAGE.search(a.get_text(" ", strip=True) or "")):
            pages.append(u)
    seen = set()
    for p in pages[:8]:
        html = h if p == home else get(sess, p)
        if not html:
            continue
        out["pages"].append(p)
        soup = BeautifulSoup(html, "lxml")
        for a in soup.select('a[href^="mailto:"]'):
            e = a["href"][7:].split("?")[0].strip()
            if e and e.lower() not in {x["email"].lower() for x in out["emails"]}:
                out["emails"].append({"email": e, "how": "mailto", "page": p})
        for t in soup(["script", "style", "noscript"]):
            t.decompose()
        text = re.sub(r"\s+", " ", soup.get_text(" "))
        for e in EMAIL.findall(text):
            if e.lower() not in {x["email"].lower() for x in out["emails"]} and not e.lower().endswith((".png", ".jpg", ".webp")):
                out["emails"].append({"email": e, "how": "visible text", "page": p})
        for pat in PATS:
            for m in pat.finditer(text):
                name = m.group(1)
                key = (name, p)
                if key in seen or name.split()[0] in ("Our", "The", "Meet", "About", "Contact", "Call", "Kitchen", "Bath", "Home"):
                    continue
                seen.add(key)
                out["dm_candidates"].append({"name": name, "page": p, "quote": words(text, m.start(), m.end())})
    return out


if __name__ == "__main__":
    from decide import load  # noqa: E402
    site = load()[1]
    ids = json.load(open(sys.argv[1]))
    with open(sys.argv[2], "w") as f, ThreadPoolExecutor(20) as ex:
        for rec in ex.map(lambda i: one(i, site[i]["final_url"]), ids):
            f.write(json.dumps(rec) + "\n"); f.flush()
