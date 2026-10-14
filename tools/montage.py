#!/usr/bin/env python3
"""G7 visual spot-check: 4x2 contact sheet of the 8 qualifying images for each id given."""
import sys, requests
from io import BytesIO
from PIL import Image, ImageDraw
sys.path.insert(0, "/home/user/100homeimprovementsearch/tools")
from decide import load, evaluate, D
from sitecheck import HDRS
data = load()
for cid in sys.argv[1:]:
    r = evaluate(data[0][cid], data)
    urls = r["ev"].get("g7_urls") or []
    sheet = Image.new("RGB", (4 * 300, 2 * 230), "white")
    for i, u in enumerate(urls[:8]):
        try:
            im = Image.open(BytesIO(requests.get(u, headers=HDRS, timeout=30).content)).convert("RGB")
            im.thumbnail((296, 210))
            sheet.paste(im, ((i % 4) * 300 + 2, (i // 4) * 230 + 2))
            ImageDraw.Draw(sheet).text(((i % 4) * 300 + 4, (i // 4) * 230 + 214), f"{i+1}", fill="black")
        except Exception as e:
            ImageDraw.Draw(sheet).text(((i % 4) * 300 + 10, (i // 4) * 230 + 100), "ERR", fill="red")
    sheet.save(f"{D}/montage/{cid}.jpg", quality=70)
    print(cid, len(urls))
