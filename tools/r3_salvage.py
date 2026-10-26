#!/usr/bin/env python3
"""Round 3: keep only what is really the business's own in a returned batch (READY homepages).
An image counts as theirs when its source page is their own Facebook page or Instagram profile (same page slug or
handle as in research.json), their Google Maps listing, or a Facebook/Instagram page whose title ("shows") carries the
business's name. Everything else (news sites, stock libraries, other people's posts found by a name search) is dropped.
Writes <batch>/salvage/<folder>/sheet.jpg (their images, numbered, for a visual check) and <batch>/SALVAGE.csv.
Usage: r3_salvage.py <batch folder>"""
import csv, glob, json, os, re, sys
from PIL import Image, ImageDraw

R = "/home/user/100homeimprovementsearch"
src = open(f"{R}/tools/r2_vet.py").read()
exec(src[:src.index("rows = []")])  # match()

B = sys.argv[1].rstrip("/")


def slug(u):
    m = re.search(r"(?:facebook|instagram)\.com/(?!groups/|photo|profile\.php|people/|share)([^/?#]+)", u or "", re.I)
    return m.group(1).lower() if m else ""


def pid(u):
    m = re.search(r"profile\.php\?id=(\d+)|/people/[^/]+/(\d+)", u or "")
    return (m.group(1) or m.group(2)) if m else ""


rows = []
for d in sorted(glob.glob(f"{B}/homepages/*")):
    r = json.load(open(f"{d}/research.json"))
    ims = json.load(open(f"{d}/images.json"))
    ims = ims if isinstance(ims, list) else ims.get("images", [])
    name = r.get("business_name", "")
    own_slugs = {s for s in (slug(r.get("facebook_url")), slug(r.get("instagram_url"))) if s}
    own_ids = {i for i in (pid(r.get("facebook_url")),) if i}
    keep = []
    for e in ims:
        sp, shows = e.get("source_page", ""), e.get("shows", "")
        ok = (slug(sp) in own_slugs or (pid(sp) and pid(sp) in own_ids) or "google.com/maps" in sp
              or (re.search(r"facebook\.com|instagram\.com", sp) and match(name, shows.replace(" ", "")) >= 0.5))
        f = f"{d}/{e['file']}" if not e["file"].startswith(d) else e["file"]
        if ok and os.path.exists(f):
            keep.append((os.path.basename(f), f))
    out = f"{B}/salvage/{os.path.basename(d)}"
    os.makedirs(out, exist_ok=True)
    if keep:
        cols = 6
        sheet = Image.new("RGB", (cols * 220, ((len(keep) - 1) // cols + 1) * 200), "white")
        dr = ImageDraw.Draw(sheet)
        for i, (fn, f) in enumerate(keep):
            try:
                im = Image.open(f)
                im.thumbnail((215, 180))
                sheet.paste(im, ((i % cols) * 220, (i // cols) * 200))
            except Exception:
                pass
            dr.text(((i % cols) * 220 + 3, (i // cols) * 200 + 183), fn, fill="red")
        sheet.save(f"{out}/sheet.jpg", quality=75)
    rows.append({"folder": os.path.basename(d), "business_name": name, "images_total": len(ims), "own_images": len(keep),
                 "own_files": " ".join(k[0] for k in keep), "facebook_url": r.get("facebook_url", ""),
                 "instagram_url": r.get("instagram_url", ""), "google_maps_url": r.get("google_maps_url", ""),
                 "email": r.get("email", ""), "email_source": r.get("email_source", ""), "reviews": len(r.get("reviews") or [])})
with open(f"{B}/SALVAGE.csv", "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=list(rows[0]))
    w.writeheader()
    w.writerows(rows)
print("homepages", len(rows), "| own images per page", sorted(r["own_images"] for r in rows),
      "| pages with 6+", sum(r["own_images"] >= 6 for r in rows))
