#!/usr/bin/env python3
"""Download the round 2 images at original size into data/r2/images/<row>/ (kept out of git; the URL manifest
data/r2/images_manifest.json is committed so they can be fetched again). Sources: the Maps deep capture
(data/r2/deep_out*.jsonl) now, and the Gemini content dive (logo, cover, post images) when it arrives.
Usage: r2_fetch_images.py"""
import glob, hashlib, json, os, concurrent.futures as cf
import requests
from PIL import Image

D = "/home/user/100homeimprovementsearch/data/r2"
jobs = []
for f in glob.glob(f"{D}/deep_out*.jsonl"):
    for r in map(json.loads, filter(str.strip, open(f))):
        for i, u in enumerate(r.get("all_photos") or []):
            jobs.append({"row": r["row"], "kind": "maps", "url": u, "name": f"maps_{i + 1:02d}"})
extra = f"{D}/content_images.json"  # written by the Gemini content ingest: logo, cover and post images
if os.path.exists(extra):
    jobs += json.load(open(extra))


def get(j):
    d = f"{D}/images/{j['row']}"
    os.makedirs(d, exist_ok=True)
    path = f"{d}/{j['name']}.jpg"
    if os.path.exists(path):
        return {**j, "file": path, "ok": True}
    try:
        r = requests.get(j["url"], timeout=40, headers={"User-Agent": "Mozilla/5.0"})
        if r.status_code != 200 or len(r.content) < 5000:
            return {**j, "ok": False, "why": f"http {r.status_code} size {len(r.content)}"}
        open(path, "wb").write(r.content)
        im = Image.open(path)
        w, h = im.size
        if im.format not in ("JPEG", "JPG"):
            im.convert("RGB").save(path, "JPEG", quality=90)
        return {**j, "file": path, "ok": True, "w": w, "h": h, "sha1": hashlib.sha1(r.content).hexdigest()}
    except Exception as e:
        return {**j, "ok": False, "why": str(e)[:80]}


with cf.ThreadPoolExecutor(16) as ex:
    res = list(ex.map(get, jobs))
json.dump(res, open(f"{D}/images_manifest.json", "w"), indent=0)
print(len(res), "ok", sum(r["ok"] for r in res), "failed", sum(not r["ok"] for r in res))
