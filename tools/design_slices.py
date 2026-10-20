#!/usr/bin/env python3
"""Design reference pack helpers.
  sheet <rawdir> <out.jpg> [ids...]  contact sheet: first desktop screen and first mobile screen of each captured site
  stitch <tiledir>                   join scroll-and-stitch tiles (tools/design_stitch.js) into <id>__<device>_full.jpg,
                                     plus <id>__<device>_screen1.jpg from the first tile
  slice <rawdir> <outdir> <id>...    cut each full-page capture into screen-sized slices (desktop 1440x1100, mobile
                                     780x1500 at 2x), so each slice shows one or two sections at readable size
Usage: design_slices.py sheet|slice ..."""
import glob, json, os, sys
from PIL import Image, ImageDraw

Image.MAX_IMAGE_PIXELS = None


def sheet(raw, out, ids):
    ids = ids or sorted({os.path.basename(f).split("__")[0] for f in glob.glob(f"{raw}/*__desktop_full.jpg")})
    tiles = []
    for i in ids:
        try:
            d = Image.open(f"{raw}/{i}__desktop_full.jpg"); m = Image.open(f"{raw}/{i}__mobile_full.jpg")
        except FileNotFoundError:
            continue
        d = d.crop((0, 0, 1440, min(d.height, 900))).resize((640, 400))
        m = m.crop((0, 0, 780, min(m.height, 1688))).resize((185, 400))
        t = Image.new("RGB", (845, 430), "white"); t.paste(d, (0, 30)); t.paste(m, (655, 30))
        ImageDraw.Draw(t).text((5, 8), f"{i}  desktop {Image.open(f'{raw}/{i}__desktop_full.jpg').height}px", fill="black")
        tiles.append(t)
    cols = 2; rows = (len(tiles) + cols - 1) // cols
    s = Image.new("RGB", (845 * cols, 430 * rows), "white")
    for n, t in enumerate(tiles):
        s.paste(t, ((n % cols) * 845, (n // cols) * 430))
    s.save(out, quality=70); print(out, len(tiles))


def cut(img, h, prefix):
    n, y, files = 1, 0, []
    while y < img.height:
        part = img.crop((0, y, img.width, min(y + h, img.height)))
        if part.height > 120:
            f = f"{prefix}_{n:02d}.jpg"; part.save(f, quality=78); files.append(f)
        y += h; n += 1
    return files


def slice_ids(raw, outdir, ids):
    for i in ids:
        os.makedirs(f"{outdir}/{i}", exist_ok=True)
        d = Image.open(f"{raw}/{i}__desktop_full.jpg").convert("RGB")
        m = Image.open(f"{raw}/{i}__mobile_full.jpg").convert("RGB")
        d.save(f"{outdir}/{i}/desktop_full.jpg", quality=72); m.save(f"{outdir}/{i}/mobile_full.jpg", quality=72)
        nd = cut(d, 1100, f"{outdir}/{i}/desktop"); nm = cut(m, 1500, f"{outdir}/{i}/mobile")
        print(i, len(nd), len(nm))


def stitch(d):
    for meta_file in sorted(glob.glob(f"{d}/*_tiles.json")):
        m = json.load(open(meta_file)); k = m["scale"]
        prefix = meta_file[:-len("_tiles.json")]
        first = Image.open(m["tiles"][0]["file"]).convert("RGB")
        W = first.width
        H = int(max(t["y"] for t in m["tiles"]) * k) + first.height
        out = Image.new("RGB", (W, H), "white")
        for t in m["tiles"]:  # later tiles over earlier ones; the last tile is aligned to the page bottom
            out.paste(Image.open(t["file"]).convert("RGB"), (0, int(t["y"] * k)))
        out.save(f"{prefix}_full.jpg", quality=75)
        first.save(f"{prefix}_screen1.jpg", quality=80)
        for t in m["tiles"]:
            os.remove(t["file"])
        print(os.path.basename(prefix), out.size, len(m["tiles"]))


if __name__ == "__main__":
    a = sys.argv[1:]
    if a[0] == "stitch":
        stitch(a[1])
    elif a[0] == "sheet":
        sheet(a[1], a[2], a[3:])
    else:
        slice_ids(a[1], a[2], a[3:])
