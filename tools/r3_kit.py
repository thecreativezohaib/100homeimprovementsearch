#!/usr/bin/env python3
"""Round 3: build a writer kit folder for each business that has enough real material.
Per business (output/round3/kit/<n>_<slug>/): research.json (Google Maps capture: category, rating, address, phone,
hours, overview and About text, every review with reviewer and date; email and where it was published; Facebook and
Instagram; Antigravity's notes kept only as leads), images/ (Maps photos and any photos checked as coming from the
business's own Facebook page, resized to 1600 px), images.json and contact_sheet.jpg.
Usage: r3_kit.py <batch folder> <n,n,...> [own Facebook image sets as n:prefix ...]"""
import csv, glob, json, os, re, shutil, sys
from PIL import Image, ImageDraw, ImageOps

R = "/home/user/100homeimprovementsearch"
B, ns = sys.argv[1].rstrip("/"), [int(x) for x in sys.argv[2].split(",")]
own_fb = {int(a.split(":")[0]) for a in sys.argv[3:]}
K = f"{R}/output/round3/kit"
maps = {}
for f in glob.glob(f"{R}/data/r3/*_maps_out*.jsonl"):
    for l in open(f):
        j = json.loads(l)
        maps[j["row"]] = j


def slugify(s):
    return re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", s.lower())).strip("-")[:50]


def save(src, dst):
    im = ImageOps.exif_transpose(Image.open(src)).convert("RGB")
    im.thumbnail((1600, 1600))
    im.save(dst, "JPEG", quality=80, optimize=True)
    return im.size


for n in ns:
    hp = glob.glob(f"{B}/homepages/{n:03d}_*")[0]
    ag = json.load(open(f"{hp}/research.json"))
    m = maps.get(n, {})
    d = f"{K}/{n:03d}_{slugify(m.get('title') or ag['business_name'])}"
    shutil.rmtree(d, ignore_errors=True)
    os.makedirs(f"{d}/images")
    imgs = []
    for f in sorted(glob.glob(f"{R}/data/r3/images/{n:03d}/*")):
        fn = os.path.basename(f)
        w, h = save(f, f"{d}/images/{fn}")
        imgs.append({"file": f"images/{fn}", "source": "Google Maps (owner or customer photo)", "width": w, "height": h})
    if n in own_fb:
        meta = json.load(open(f"{hp}/images.json"))
        for e in meta if isinstance(meta, list) else meta.get("images", []):
            f = f"{hp}/{e['file']}"
            if os.path.exists(f):
                fn = os.path.basename(f)
                w, h = save(f, f"{d}/images/{fn}")
                imgs.append({"file": f"images/{fn}", "source": "Facebook", "source_page": e.get("source_page", ""),
                             "post_text": e.get("shows", ""), "width": w, "height": h})
    phone = (m.get("phone") or "").replace("phone:tel:", "")
    research = {
        "n": n, "business_name": m.get("title") or ag["business_name"],
        "google": {"maps_url": m.get("maps_url") or ag.get("google_maps_url"), "category": m.get("category"),
                   "rating_label": m.get("rating_label"), "address": m.get("address"), "phone": phone,
                   "service_area": m.get("service_area"), "hours": m.get("hours"), "overview_text": m.get("overview_text"),
                   "about_text": m.get("about_text"), "reviews": m.get("reviews") or []},
        "email": {"address": ag.get("email"), "published_at": ag.get("email_source"),
                  "status": "confirm: published on Facebook, which could not be opened from here"},
        "facebook_url": ag.get("facebook_url"), "instagram_url": ag.get("instagram_url"),
        "antigravity_notes_unverified": {k: ag.get(k) for k in ("identity", "town", "state", "facts")},
    }
    json.dump(research, open(f"{d}/research.json", "w"), indent=1, ensure_ascii=False)
    json.dump(imgs, open(f"{d}/images.json", "w"), indent=1)
    if not imgs:
        print(os.path.basename(d), "no images", len(research["google"]["reviews"]), "reviews")
        continue
    cols = 6
    sheet = Image.new("RGB", (cols * 270, ((len(imgs) - 1) // cols + 1) * 240), "white")
    dr = ImageDraw.Draw(sheet)
    for i, e in enumerate(imgs):
        im = Image.open(f"{d}/{e['file']}")
        im.thumbnail((265, 215))
        sheet.paste(im, ((i % cols) * 270, (i // cols) * 240))
        dr.text(((i % cols) * 270 + 3, (i // cols) * 240 + 222), e["file"][7:], fill="red")
    sheet.save(f"{d}/contact_sheet.jpg", quality=80)
    print(os.path.basename(d), len(imgs), "images", len(research["google"]["reviews"]), "reviews")
