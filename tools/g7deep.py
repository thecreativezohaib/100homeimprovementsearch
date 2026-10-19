#!/usr/bin/env python3
"""Deeper G7 crawl for firms that failed the automated G7 check (home + one gallery page only).
Follows the firm's own portfolio / project / gallery / kitchen / bath pages (and project sub-pages linked from them),
then applies the same strict filters as g7verify.py: width >= 800 on the full image, stock signatures dropped,
graphics dropped (>55% near-white or <24 colour buckets), near-duplicates dropped (dHash Hamming <= 6).
Writes one g7verify.jsonl line per firm (newest line per id wins in decide.py) and a contact sheet for visual review.
A firm reaching 8 kept images still needs the coordinator's visual review before it can count.
Usage: g7deep.py <ids.txt> [workers]"""
import json, re, sys, signal
from concurrent.futures import ThreadPoolExecutor, as_completed
from io import BytesIO
from urllib.parse import urljoin, urlparse
import requests
from bs4 import BeautifulSoup
from PIL import Image, ImageDraw
sys.path.insert(0, "/home/user/100homeimprovementsearch/tools")
from decide import load, D, jl  # noqa: E402
from sitecheck import HDRS, collect_imgs, master_url, STOCK, SKIPIMG  # noqa: E402

PAGE = re.compile(r"gallery|portfolio|project|our-work|work|photos|kitchen|bath|remodel|before-after|case-stud|showcase", re.I)
SKIPPAGE = re.compile(r"blog|news|career|job|privacy|terms|contact|login|cart|tag/|category/|feed|wp-json|\.pdf$", re.I)
MAX_PAGES, MAX_CANDS, KEEP = 14, 45, 12


def dhash(im):
    g = im.convert("L").resize((9, 8))
    px = list(g.getdata())
    return sum(1 << i for i in range(64) if px[(i // 8) * 9 + i % 8] > px[(i // 8) * 9 + i % 8 + 1])


def flat(im):
    sm = im.convert("RGB").resize((64, 64))
    px = list(sm.getdata())
    white = sum(1 for p in px if min(p) > 235) / len(px)
    buckets = len({(p[0] // 32, p[1] // 32, p[2] // 32) for p in px})
    return white > 0.55 or buckets < 24


def get(sess, u, t=20):
    try:
        r = sess.get(u, headers=HDRS, timeout=t)
        return r.text if r.status_code == 200 else None
    except Exception:
        return None


def pages_for(sess, home):
    host = urlparse(home).netloc.replace("www.", "")
    h = get(sess, home)
    if not h:
        return [], None
    soup = BeautifulSoup(h, "lxml")
    first, seen = [], {home.rstrip("/")}
    for a in soup.find_all("a", href=True):
        u = urljoin(home, a["href"]).split("#")[0].rstrip("/")
        if urlparse(u).netloc.replace("www.", "") != host or u in seen or SKIPPAGE.search(u):
            continue
        if PAGE.search(u) or PAGE.search(a.get_text(" ", strip=True) or ""):
            seen.add(u)
            first.append(u)
    pages = first[:8]
    # one more level: project sub-pages linked from portfolio-type pages
    for p in first[:4]:
        if len(pages) >= MAX_PAGES:
            break
        ph = get(sess, p)
        if not ph:
            continue
        for a in BeautifulSoup(ph, "lxml").find_all("a", href=True):
            u = urljoin(p, a["href"]).split("#")[0].rstrip("/")
            if urlparse(u).netloc.replace("www.", "") == host and u not in seen and not SKIPPAGE.search(u) \
                    and re.search(r"project|portfolio|gallery|kitchen|bath", u, re.I) and u.count("/") > p.count("/"):
                seen.add(u)
                pages.append(u)
                if len(pages) >= MAX_PAGES:
                    break
    return [home] + pages, soup


def one(cid, home):
    signal.alarm(0)
    sess = requests.Session()
    pages, _ = pages_for(sess, home)
    cands, seenm = [], set()
    for p in pages:
        h = get(sess, p)
        if not h:
            continue
        for iu in collect_imgs(BeautifulSoup(h, "lxml"), p):
            mu = master_url(iu)
            if mu in seenm or STOCK.search(mu) or SKIPIMG.search(mu.split("/")[-1]):
                continue
            seenm.add(mu)
            cands.append((iu, mu, p))
    kept, hashes, dropped, ims = [], [], [], []
    for iu, mu, page in cands[:MAX_CANDS]:
        im = src = None
        for url in (mu, iu):
            try:
                r = sess.get(url, headers=HDRS, timeout=25)
                im = Image.open(BytesIO(r.content)); im.load(); src = url
                break
            except Exception:
                im = None
        if im is None:
            continue
        if im.size[0] < 800:
            dropped.append({"url": src, "why": f"width {im.size[0]}"}); continue
        if flat(im):
            dropped.append({"url": src, "why": "graphic/flat"}); continue
        hsh = dhash(im)
        if any(bin(hsh ^ x).count("1") <= 6 for x in hashes):
            dropped.append({"url": src, "why": "near-duplicate of a kept image"}); continue
        hashes.append(hsh)
        kept.append({"url": src, "w": im.size[0], "h": im.size[1], "page": page})
        ims.append(im)
        if len(kept) >= KEEP:
            break
    if len(kept) >= 8:
        sheet = Image.new("RGB", (4 * 300, 3 * 230), "white")
        for i, im in enumerate(ims[:12]):
            t = im.convert("RGB"); t.thumbnail((296, 210))
            sheet.paste(t, ((i % 4) * 300 + 2, (i // 4) * 230 + 2))
            ImageDraw.Draw(sheet).text(((i % 4) * 300 + 4, (i // 4) * 230 + 214), str(i + 1), fill="black")
        sheet.save(f"{D}/montage/{cid}.jpg", quality=70)
    return {"id": cid, "kept": kept, "dropped": dropped[:20], "candidates_checked": min(len(cands), MAX_CANDS),
            "pages_scanned": pages, "montage": f"data/montage/{cid}.jpg" if len(kept) >= 8 else None,
            "note": "g7deep: portfolio/project/gallery/kitchen/bath pages followed one level deep"}


if __name__ == "__main__":
    ids = [l.strip() for l in open(sys.argv[1]) if l.strip()]
    workers = int(sys.argv[2]) if len(sys.argv) > 2 else 12
    site = load()[1]
    done = {x["id"] for x in jl(f"{D}/g7deep_done.jsonl")}
    todo = [(i, site[i]["final_url"]) for i in ids if i in site and i not in done]
    print("todo", len(todo), flush=True)
    with open(f"{D}/g7verify.jsonl", "a") as out, open(f"{D}/g7deep_done.jsonl", "a") as dn, ThreadPoolExecutor(workers) as ex:
        futs = {ex.submit(one, i, u): i for i, u in todo}
        for f in as_completed(futs):
            i = futs[f]
            try:
                rec = f.result(timeout=600)
            except Exception as e:
                dn.write(json.dumps({"id": i, "error": type(e).__name__}) + "\n"); dn.flush(); continue
            if len(rec["kept"]) >= 8:  # only a deeper PASS replaces the earlier automated record
                out.write(json.dumps(rec) + "\n"); out.flush()
            dn.write(json.dumps({"id": i, "kept": len(rec["kept"])}) + "\n"); dn.flush()
            print(i, len(rec["kept"]), flush=True)
