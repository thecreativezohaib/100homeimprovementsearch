#!/usr/bin/env python3
"""Put the AI images Gemini returns into the right homepage folders. Reads any number of zips or folders, matches
each image by its file name against output/round2/final/AI_IMAGES_MAP.csv, centre-crops it to the slot's aspect
ratio, saves it as JPEG at the page's file name (homepages/<NNN_slug>/images/ai_*.jpg) and reports missing images.
Usage: r2_import_ai.py <zip or folder> [...]"""
import csv, io, os, re, sys, zipfile
from PIL import Image, ImageOps

F = "/home/user/100homeimprovementsearch/output/round2/final"
M = {r["file_name"].lower(): r for r in csv.DictReader(open(f"{F}/AI_IMAGES_MAP.csv"))}
RATIO = {"16:9": 16 / 9, "4:3": 4 / 3, "4:5": 4 / 5, "21:9": 21 / 9}
found = {}


def take(name, data):
    # browsers may add " (1)" or change the extension; the NNN_ai_name part is what matters
    m = re.search(r"\d{3}_ai_[a-z0-9_]+", os.path.basename(name).lower())
    key = next((k for k in M if m and os.path.splitext(k)[0] == m.group(0)), None)
    if not key:
        return
    r = M[key]
    im = ImageOps.exif_transpose(Image.open(io.BytesIO(data))).convert("RGB")
    w, h = im.size
    target = RATIO[r["aspect_ratio"]]
    if abs(w / h - target) > 0.02:
        im = ImageOps.fit(im, (int(min(w, h * target)), int(min(h, w / target))))
    if max(im.size) > 2560:
        im.thumbnail((2560, 2560))
    dst = f"{F}/{r['folder']}/{r['save_as']}"
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    im.save(dst, "JPEG", quality=85, optimize=True, progressive=True)
    found[key] = dst


for src in sys.argv[1:]:
    if zipfile.is_zipfile(src):
        with zipfile.ZipFile(src) as z:
            for n in z.namelist():
                if n.lower().endswith((".jpg", ".jpeg", ".png", ".webp")):
                    take(n, z.read(n))
    else:
        for root, _, files in os.walk(src):
            for n in files:
                if n.lower().endswith((".jpg", ".jpeg", ".png", ".webp")):
                    take(n, open(os.path.join(root, n), "rb").read())
miss = sorted(set(M) - set(found))
print("placed", len(found), "of", len(M), "| missing:", ", ".join(miss[:40]) + (" ..." if len(miss) > 40 else ""))
