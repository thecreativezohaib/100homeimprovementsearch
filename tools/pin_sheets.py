#!/usr/bin/env python3
"""Pinterest pins to numbered contact sheets for visual selection, and download of the chosen originals.
  sheets <pins.jsonl...> --out <dir>   dedupe pins by image, download 236px thumbnails, write numbered sheets
                                       (sheet_NN.jpg, 24 tiles each) and <dir>/catalog.json (number -> pin)
  fetch <dir> <picks.json> <outdir>    download the original image of each picked number, save as JPEG (max 2400
                                       px wide) named NNN_<query-slug>.jpg; picks.json is [{"n": 12, ...}, ...]
Usage: pin_sheets.py sheets|fetch ..."""
import io, json, os, re, sys, concurrent.futures as cf
import requests
from PIL import Image, ImageDraw

Image.MAX_IMAGE_PIXELS = None
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0 Safari/537.36"}
TW, TH = 236, 420


def thumb_url(u):
    return re.sub(r"/originals/|/\d+x\d*/", "/236x/", u)


def get(u, timeout=40):
    r = requests.get(u, headers=UA, timeout=timeout)
    r.raise_for_status()
    return r.content


def sheets(files, out):
    os.makedirs(f"{out}/thumbs", exist_ok=True)
    pins, seen = [], set()
    for f in files:
        for line in open(f):
            p = json.loads(line)
            key = (p.get("image") or "").split("/")[-1]
            if not p.get("image") or key in seen:
                continue
            seen.add(key); pins.append(p)
    for n, p in enumerate(pins, 1):
        p["n"] = n

    def dl(p):
        path = f"{out}/thumbs/{p['n']:04d}.jpg"
        if os.path.exists(path):
            return True
        try:
            Image.open(io.BytesIO(get(thumb_url(p["image"])))).convert("RGB").save(path, quality=80)
            return True
        except Exception:
            return False
    with cf.ThreadPoolExecutor(12) as ex:
        ok = list(ex.map(dl, pins))
    pins = [p for p, k in zip(pins, ok) if k]
    json.dump({p["n"]: p for p in pins}, open(f"{out}/catalog.json", "w"), indent=1)
    per = 24
    for s in range(0, len(pins), per):
        chunk = pins[s:s + per]
        sheet = Image.new("RGB", (6 * (TW + 8), 4 * (TH + 26)), "white")
        d = ImageDraw.Draw(sheet)
        for i, p in enumerate(chunk):
            im = Image.open(f"{out}/thumbs/{p['n']:04d}.jpg")
            im = im.crop((0, 0, im.width, min(im.height, TH)))
            x, y = (i % 6) * (TW + 8), (i // 6) * (TH + 26)
            sheet.paste(im, (x, y + 22))
            d.rectangle((x, y, x + 60, y + 20), fill="black"); d.text((x + 4, y + 4), f"#{p['n']}", fill="white")
        sheet.save(f"{out}/sheet_{s // per + 1:02d}.jpg", quality=72)
    print("pins", len(pins), "sheets", (len(pins) + per - 1) // per)


def fetch(d, picks_file, outdir):
    cat = json.load(open(f"{d}/catalog.json"))
    os.makedirs(outdir, exist_ok=True)
    for pk in json.load(open(picks_file)):
        p = cat[str(pk["n"])]
        slug = re.sub(r"[^a-z0-9]+", "-", p["q"].lower()).strip("-")[:40]
        path = f"{outdir}/{pk['n']:04d}_{slug}.jpg"
        try:
            im = Image.open(io.BytesIO(get(p["image"]))).convert("RGB")
            if im.width > 2400:
                im = im.resize((2400, int(im.height * 2400 / im.width)))
            im.save(path, quality=82)
            pk["file"] = path
        except Exception as e:
            pk["error"] = str(e)[:100]
        print(pk["n"], pk.get("file") or pk.get("error"))


if __name__ == "__main__":
    a = sys.argv[1:]
    if a[0] == "sheets":
        i = a.index("--out"); sheets(a[1:i], a[i + 1])
    else:
        fetch(a[1], a[2], a[3])
