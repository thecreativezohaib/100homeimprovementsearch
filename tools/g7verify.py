#!/usr/bin/env python3
"""G7 strict verification: re-collect images from home + gallery pages (cap 30 candidates), master-URL correction,
width >= 800, drop stock signatures, drop near-duplicates (64-bit dHash, Hamming <= 6), drop flat/graphic images
(>55% near-white pixels or <24 distinct colour buckets), then write a contact sheet for visual review.
Usage: g7verify.py <id> [<id> ...]"""
import json, sys, requests
from io import BytesIO
from PIL import Image, ImageDraw
sys.path.insert(0, "/home/user/100homeimprovementsearch/tools")
from decide import load, D, jl
from sitecheck import HDRS, collect_imgs, master_url, STOCK, SKIPIMG
from bs4 import BeautifulSoup

def dhash(im):
    g = im.convert("L").resize((9, 8))
    px = list(g.getdata())
    return sum(1 << i for i in range(64) if px[(i // 8) * 9 + i % 8] > px[(i // 8) * 9 + i % 8 + 1])

def flat(im):
    sm = im.convert("RGB").resize((64, 64))
    px = list(sm.getdata())
    white = sum(1 for p in px if min(p) > 235) / len(px)
    buckets = len({(p[0] // 32, p[1] // 32, p[2] // 32) for p in px})
    return white > 0.55 or buckets < 24, round(white, 2), buckets

data = load(); site = data[1]
done = {x["id"] for x in jl(f"{D}/g7verify.jsonl")}
out = open(f"{D}/g7verify.jsonl", "a")
for cid in sys.argv[1:]:
    if cid in done: continue
    s = site[cid]
    pages = [(k, u) for k in ("home", "gallery") for u in (s.get("pages_fetched") or {}).get(k, [])]
    cands = []
    for k, u in pages:
        try:
            h = requests.get(u, headers=HDRS, timeout=25).text
        except Exception:
            continue
        for iu in collect_imgs(BeautifulSoup(h, "lxml"), u):
            mu = master_url(iu)
            if mu not in [c[1] for c in cands] and not STOCK.search(mu) and not SKIPIMG.search(mu.split("/")[-1]):
                cands.append((iu, mu, u))
    kept, hashes, dropped = [], [], []
    for iu, mu, page in cands[:30]:
        im = None
        for url in (mu, iu):
            try:
                r = requests.get(url, headers=HDRS, timeout=30)
                im = Image.open(BytesIO(r.content)); im.load(); src = url; break
            except Exception:
                im = None
        if im is None: continue
        if im.size[0] < 800:
            dropped.append({"url": src, "why": f"width {im.size[0]}"}); continue
        f, wfrac, nb = flat(im)
        if f:
            dropped.append({"url": src, "why": f"graphic/flat (white {wfrac}, colour buckets {nb})"}); continue
        h = dhash(im)
        if any(bin(h ^ x).count("1") <= 6 for x in hashes):
            dropped.append({"url": src, "why": "near-duplicate of a kept image"}); continue
        hashes.append(h); kept.append({"url": src, "w": im.size[0], "h": im.size[1], "page": page, "im": im})
        if len(kept) >= 12: break
    sheet = Image.new("RGB", (4 * 300, 3 * 230), "white")
    for i, k in enumerate(kept[:12]):
        t = k["im"].convert("RGB"); t.thumbnail((296, 210))
        sheet.paste(t, ((i % 4) * 300 + 2, (i // 4) * 230 + 2))
        ImageDraw.Draw(sheet).text(((i % 4) * 300 + 4, (i // 4) * 230 + 214), str(i + 1), fill="black")
    sheet.save(f"{D}/montage/{cid}.jpg", quality=70)
    rec = {"id": cid, "kept": [{k: v for k, v in x.items() if k != "im"} for x in kept], "dropped": dropped[:20],
           "candidates_checked": min(len(cands), 30), "montage": f"data/montage/{cid}.jpg"}
    out.write(json.dumps(rec) + "\n"); out.flush()
    print(cid, "kept", len(kept), "dropped", len(dropped))
