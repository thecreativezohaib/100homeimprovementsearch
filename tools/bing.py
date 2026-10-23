#!/usr/bin/env python3
"""Free web search through Bing's HTML results (DuckDuckGo blocks this server). Returns real URLs (decoded from Bing's
redirect links), titles and snippets.
Usage: bing.py "<query>" [n]   (or import search())"""
import base64, html, re, sys, time, urllib.parse
import requests

UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36",
      "Accept-Language": "en-US,en;q=0.9"}


def real_url(u):
    u = html.unescape(u)
    m = re.search(r"[?&]u=a1([^&]+)", u)
    if m:
        s = m.group(1); s += "=" * (-len(s) % 4)
        try:
            return base64.urlsafe_b64decode(s).decode("utf-8", "ignore")
        except Exception:
            return u
    return u


def search(q, n=10, tries=3):
    for t in range(tries):
        try:
            r = requests.get("https://www.bing.com/search", params={"q": q, "setlang": "en", "cc": "US", "count": n}, headers=UA, timeout=30)
            items = re.findall(r'<li class="b_algo".*?<h2[^>]*><a[^>]+href="([^"]+)"[^>]*>(.*?)</a>.*?(?:<p[^>]*>(.*?)</p>|</li>)', r.text, re.S)
            out = [{"url": real_url(u), "title": html.unescape(re.sub("<.*?>", "", ti)),
                    "snippet": html.unescape(re.sub("<.*?>", "", sn or ""))} for u, ti, sn in items]
            if out or t == tries - 1:
                return out
        except Exception:
            pass
        time.sleep(3 * (t + 1))
    return []


if __name__ == "__main__":
    for x in search(sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else 10):
        print(x["url"][:100], "|", x["title"][:60], "|", x["snippet"][:200])
