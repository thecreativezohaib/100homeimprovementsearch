#!/usr/bin/env python3
"""G4 social_post signals from accounts the company links from its own site (so the account is theirs):
LinkedIn company pages (anonymous JSON-LD SocialMediaPosting with datePublished, author = Organization),
YouTube channel RSS (<published>), Pinterest profile RSS (<pubDate>). Keeps every dated post found.
Usage: social.py <ids.txt> <out.jsonl> [workers]"""
import json, re, sys, html
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
import requests

sys.path.insert(0, "/home/user/100homeimprovementsearch/tools")
from decide import jl, D  # noqa: E402

UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                    "Chrome/126.0 Safari/537.36", "Accept-Language": "en-US,en;q=0.9"}
LI = re.compile(r'https?://(?:[a-z]{2,3}\.)?linkedin\.com/company/[^"\'?#<>\s]+', re.I)
YT = re.compile(r'https?://(?:www\.)?youtube\.com/(?:channel/UC[\w-]{22}|@[\w.-]+|user/[\w.-]+|c/[\w.-]+)', re.I)
PI = re.compile(r'https?://(?:[a-z]{2,3}\.)?pinterest\.[a-z.]+/(?!pin/)([\w.-]+)/?', re.I)


def get(url, t=25):
    try:
        r = requests.get(url, headers=UA, timeout=t, allow_redirects=True)
        return r.status_code, r.text
    except Exception as e:
        return None, type(e).__name__


def words(s, n=15):
    s = re.sub(r"\s+", " ", html.unescape(s or "")).strip()
    return " ".join(s.split()[:n])


def linkedin(url):
    st, h = get(url)
    out = []
    if st != 200:
        return out, f"HTTP {st}"
    for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>', h, re.S):
        try:
            d = json.loads(m.group(1))
        except Exception:
            continue
        for x in d.get("@graph", [d]):
            if x.get("@type") == "SocialMediaPosting" and (x.get("author") or {}).get("@type") == "Organization":
                out.append({"date": (x.get("datePublished") or "")[:10], "quote": words(x.get("text") or x.get("headline")),
                            "post_url": x.get("url") or url, "account": url, "platform": "LinkedIn company page",
                            "method": "anonymous LinkedIn company page, JSON-LD SocialMediaPosting datePublished"})
    return out, "ok"


def youtube(url):
    cid = re.search(r"channel/(UC[\w-]{22})", url)
    if cid:
        cid = cid.group(1)
    else:
        st, h = get(url)
        m = re.search(r'"(?:channelId|externalId)":"(UC[\w-]{22})"', h or "") if st == 200 else None
        if not m:
            return [], f"no channel id (HTTP {st})"
        cid = m.group(1)
    feed = f"https://www.youtube.com/feeds/videos.xml?channel_id={cid}"
    st, x = get(feed)
    if st != 200:
        return [], f"feed HTTP {st}"
    out = []
    for e in re.findall(r"<entry>(.*?)</entry>", x, re.S):
        pub = re.search(r"<published>([^<]+)</published>", e)
        ti = re.search(r"<title>([^<]*)</title>", e)
        li = re.search(r'<link rel="alternate" href="([^"]+)"', e)
        if pub:
            out.append({"date": pub.group(1)[:10], "quote": words(ti.group(1) if ti else ""), "post_url": li.group(1) if li else feed,
                        "account": url, "platform": "YouTube channel", "method": f"YouTube channel RSS {feed} <published>"})
    return out, "ok"


def pinterest(user, url):
    feed = f"https://www.pinterest.com/{user}/feed.rss"
    st, x = get(feed)
    if st != 200:
        return [], f"feed HTTP {st}"
    out = []
    for it in re.findall(r"<item>(.*?)</item>", x, re.S):
        pd = re.search(r"<pubDate>([^<]+)</pubDate>", it)
        ti = re.search(r"<title>(?:<!\[CDATA\[)?(.*?)(?:\]\]>)?</title>", it, re.S)
        li = re.search(r"<link>([^<]+)</link>", it)
        if pd:
            try:
                dt = parsedate_to_datetime(pd.group(1)).astimezone(timezone.utc).date().isoformat()
            except Exception:
                continue
            out.append({"date": dt, "quote": words(ti.group(1) if ti else ""), "post_url": li.group(1) if li else feed,
                        "account": url, "platform": "Pinterest profile", "method": f"Pinterest profile RSS {feed} <pubDate>"})
    return out, "ok"


def one(c):
    cid, home = c["id"], c["url"]
    rec = {"id": cid, "home": home, "retrieved": datetime.now(timezone.utc).isoformat(timespec="seconds"), "accounts": {}, "posts": []}
    st, h = get(home)
    if st != 200:
        rec["error"] = f"home HTTP {st}"
        return rec
    lis = sorted({u.rstrip("/") + "/" for u in LI.findall(h)})[:2]
    yts = sorted(set(YT.findall(h)))[:2]
    pis = sorted({m.group(1) for m in PI.finditer(h) if m.group(1).lower() not in ("pin", "search", "ideas", "business")})[:2]
    for u in lis:
        p, s = linkedin(u); rec["accounts"][u] = s; rec["posts"] += p
    for u in yts:
        p, s = youtube(u); rec["accounts"][u] = s; rec["posts"] += p
    for u in pis:
        acc = f"https://www.pinterest.com/{u}/"
        p, s = pinterest(u, acc); rec["accounts"][acc] = s; rec["posts"] += p
    return rec


if __name__ == "__main__":
    ids_file, outp = sys.argv[1], sys.argv[2]
    workers = int(sys.argv[3]) if len(sys.argv) > 3 else 12
    done = {x["id"] for x in jl(outp)}
    site = {}
    for f in ("site", "site_b", "site_c", "site_d", "site_render"):
        for x in jl(f"{D}/{f}.jsonl"):
            if x.get("final_url"):
                site[x["id"]] = x["final_url"]
    todo = [{"id": i, "url": site[i]} for i in (l.strip() for l in open(ids_file)) if i and i in site and i not in done]
    print("todo", len(todo), flush=True)
    with open(outp, "a") as fo, ThreadPoolExecutor(workers) as ex:
        for rec in ex.map(one, todo):
            fo.write(json.dumps(rec) + "\n"); fo.flush()
