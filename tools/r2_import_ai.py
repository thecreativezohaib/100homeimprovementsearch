#!/usr/bin/env python3
"""Put the AI images Gemini returns into the right homepage folders. Reads any number of zips or folders, matches
each image by its file name against output/round2/final/AI_IMAGES_MAP.csv, centre-crops it to the slot's aspect
ratio, saves it as JPEG at the page's file name (homepages/<NNN_slug>/images/ai_*.jpg) and reports missing images.
A folder or zip may also hold a Gemini chat saved with Ctrl+S as "Webpage, Complete": each image is then matched to
the file name Gemini wrote under it.
Usage: r2_import_ai.py <zip or folder> [...] [--names-under | --names-above]"""
import csv, io, os, re, sys, tempfile, zipfile
from html.parser import HTMLParser
from urllib.parse import unquote
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


class Page(HTMLParser):
    """A Gemini chat saved with Ctrl+S (Webpage, Complete): images and the file names written next to them, in page order."""
    def __init__(self):
        super().__init__()
        self.events, self.seen = [], set()

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "img" and a.get("src") and a["src"] not in self.seen and not a["src"].startswith("data:image/svg"):
            self.seen.add(a["src"])
            self.events.append(("img", a["src"]))

    def handle_data(self, data):
        pos = 0
        for m in re.finditer(r"\b(\d{3}_ai_[a-z0-9_]+)\.(?:jpe?g|png|webp)\b", data, re.I):
            self.events += [("text", m.start() - pos), ("name", m.group(1).lower())]
            pos = m.end()
        self.events.append(("text", len(data) - pos))


def from_page(html):
    p = Page()
    p.feed(open(html, encoding="utf-8", errors="ignore").read())
    ev = []
    for t, v in p.events:  # keep only real pictures that were saved (icons and avatars are small)
        if t == "img":
            f = os.path.join(os.path.dirname(html), unquote(v.split("?")[0]))
            try:
                if os.path.isfile(f) and max(Image.open(f).size) >= 300:
                    ev.append((t, f))
            except Exception:
                pass
        else:
            ev.append((t, v))
    def gap(i, step):  # characters of page text between image i and the nearest name on one side
        n, j = 0, i + step
        while 0 <= j < len(ev) and ev[j][0] != "img":
            if ev[j][0] == "name":
                return n
            n += ev[j][1] if ev[j][0] == "text" else 0
            j += step
        return 10 ** 6
    imgs = [i for i, (t, _) in enumerate(ev) if t == "img"]
    # names written under the images, or above them: each image votes for the side its nearest name is on
    # (override with --names-under / --names-above after checking a few images against their prompts)
    under, above = sum(gap(i, 1) < gap(i, -1) for i in imgs), sum(gap(i, -1) < gap(i, 1) for i in imgs)
    step = 1 if "--names-under" in sys.argv else -1 if "--names-above" in sys.argv else (1 if under >= above else -1)
    n = 0
    for i, (t, f) in enumerate(ev):
        if t != "img":
            continue
        j = i + step
        while 0 <= j < len(ev) and ev[j][0] != "img":
            if ev[j][0] == "name":
                if ev[j][1] + ".jpg" not in found:
                    take(ev[j][1] + ".jpg", open(f, "rb").read())
                    n += 1
                break
            j += step
    print(os.path.basename(html), "images", len(imgs), "matched to a name", n, "| names", "under" if step == 1 else "above",
          f"the images (votes under {under}, above {above})")


for src in [a for a in sys.argv[1:] if not a.startswith("--")]:
    if zipfile.is_zipfile(src):
        tmp = tempfile.mkdtemp()
        zipfile.ZipFile(src).extractall(tmp)
        src = tmp
    for root, _, files in os.walk(src):
        for n in files:
            if n.lower().endswith((".html", ".htm")):
                from_page(os.path.join(root, n))
    for root, _, files in os.walk(src):
        for n in files:
            if n.lower().endswith((".jpg", ".jpeg", ".png", ".webp")):
                take(n, open(os.path.join(root, n), "rb").read())
miss = sorted(set(M) - set(found))
print("placed", len(found), "of", len(M), "| missing:", ", ".join(miss[:40]) + (" ..." if len(miss) > 40 else ""))
