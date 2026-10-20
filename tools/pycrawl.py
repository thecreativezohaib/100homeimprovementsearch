#!/usr/bin/env python3
"""Fallback crawler for sites the Playwright crawl cannot reach (plain-HTTP hosts the agent proxy refuses to tunnel).
Writes the same record shape as tools/fullcrawl.js: {id, start_url, crawled, pages:[{url, http, title, meta_description,
og, headings, text, images, background_images, jsonld, outbound, tel, mailto}]}.
Usage: pycrawl.py <in.jsonl {id,url}> <out.jsonl> [max_pages]"""
import json, re, sys
from urllib.parse import urljoin, urlparse
import requests
from bs4 import BeautifulSoup

UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"}
PRI = re.compile(r"about|service|kitchen|bath|gallery|portfolio|project|process|contact|faq|review|testimonial|area|cabinet|design", re.I)
SKIP = re.compile(r"\.(jpg|jpeg|png|gif|webp|svg|pdf|zip|mp4|mp3|docx?)$|^mailto:|^tel:|#", re.I)


def page(url, r):
    s = BeautifulSoup(r.text, "html.parser")
    jsonld = []
    for t in s.find_all("script", type="application/ld+json"):
        try:
            jsonld.append(json.loads(t.string or ""))
        except Exception:
            pass
    for t in s(["script", "style", "noscript"]):
        t.decompose()
    links = [urljoin(url, a.get("href", "")) for a in s.find_all("a", href=True)]
    imgs = []
    for im in s.find_all("img"):
        src = im.get("src") or im.get("data-src")
        if not src:
            continue
        best = None
        if im.get("srcset"):
            best = urljoin(url, im["srcset"].split(",")[-1].strip().split(" ")[0])
        imgs.append({"src": urljoin(url, src), "srcset_largest": best, "alt": im.get("alt"), "w": im.get("width"), "h": im.get("height")})
    bg = sorted({urljoin(url, m) for m in re.findall(r"url\(['\"]?([^'\")]+)", r.text) if re.search(r"\.(jpe?g|png|webp)", m, re.I)})
    md = s.find("meta", attrs={"name": "description"})
    return {"url": url, "http": r.status_code, "title": (s.title.string or "").strip() if s.title else "",
            "meta_description": md.get("content") if md else None,
            "og": {m["property"]: m.get("content") for m in s.find_all("meta", property=re.compile("^og:"))},
            "headings": [{"tag": h.name, "text": h.get_text(" ", strip=True)} for h in s.find_all(["h1", "h2", "h3"])],
            "text": re.sub(r"\s+\n", "\n", s.get_text("\n", strip=True))[:40000],
            "images": imgs, "background_images": bg, "jsonld": jsonld,
            "outbound": sorted({l for l in links if urlparse(l).netloc and urlparse(l).netloc != urlparse(url).netloc}),
            "tel": sorted({l[4:] for l in links if l.startswith("tel:")}),
            "mailto": sorted({l for l in links if l.startswith("mailto:")}), "_links": links}


def crawl(cid, start, maxp):
    host = urlparse(start).netloc.replace("www.", "")
    queue, seen, pages = [start], {start}, []
    while queue and len(pages) < maxp:
        url = queue.pop(0)
        try:
            r = requests.get(url, headers=UA, timeout=40)
            if "html" not in r.headers.get("content-type", ""):
                continue
            p = page(r.url, r)
        except Exception as e:
            pages.append({"url": url, "error": str(e)[:200]}); continue
        new = []
        for l in p.pop("_links"):
            l = l.split("#")[0]
            if urlparse(l).netloc.replace("www.", "") == host and l not in seen and not SKIP.search(l):
                seen.add(l); new.append(l)
        queue += sorted(new, key=lambda u: 0 if PRI.search(u) else 1)
        queue.sort(key=lambda u: 0 if PRI.search(u) else 1)
        pages.append(p)
    return {"id": cid, "start_url": start, "crawled": len(pages), "pages": pages, "crawler": "pycrawl"}


if __name__ == "__main__":
    maxp = int(sys.argv[3]) if len(sys.argv) > 3 else 16
    with open(sys.argv[2], "a") as out:
        for line in open(sys.argv[1]):
            x = json.loads(line)
            rec = crawl(x["id"], x["url"], maxp)
            out.write(json.dumps(rec) + "\n"); out.flush()
            ok = [p for p in rec["pages"] if not p.get("error")]
            print(x["id"], len(ok), sum(len(p["images"]) for p in ok), sum(len(p["text"]) for p in ok))
