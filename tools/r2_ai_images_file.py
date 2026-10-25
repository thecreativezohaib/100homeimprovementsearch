#!/usr/bin/env python3
"""One file for Gemini to generate every AI image of the round 2 homepages with an exact file name
(output/round2/final/GEMINI_AI_IMAGES.md), plus the name map (AI_IMAGES_MAP.csv) that r2_import_ai.py uses to put
the returned images into the right folders. File names are globally unique: <folder number>_<file name in the
page's image plan>, e.g. 004_ai_service_backsplash.jpg -> homepages/004_ck-tile-and-home-repair-llc/images/ai_service_backsplash.jpg
Usage: r2_ai_images_file.py [batch_size] (default: all images in one list)"""
import csv, os, re, sys

F = "/home/user/100homeimprovementsearch/output/round2/final"
per = int(sys.argv[1]) if len(sys.argv) > 1 else 10**6
rows = list(csv.DictReader(open(f"{F}/AI_IMAGE_PROMPTS.csv")))
SIZES = {"16:9": "1920x1080", "4:3": "1600x1200", "4:5": "1200x1500", "21:9": "2520x1080"}
items = []
for r in rows:
    num = os.path.basename(r["folder"])[:3]
    base = os.path.basename(r["save_as"])
    ar = (re.findall(r"\b(16:9|4:3|4:5|21:9)\b", r["prompt"]) or ["4:3"])[-1]
    prompt = re.sub(r"[,.;]?\s*(aspect ratio|aspect)?\s*:?\s*\b(16:9|4:3|4:5|21:9)\b\s*(aspect ratio)?\s*\.?\s*$", "", r["prompt"].strip(), flags=re.I)
    prompt = re.sub(r"[,.;]?\s*aspect ratio\s*$", "", prompt, flags=re.I).rstrip(" ,.;") + "."
    items.append({"file_name": f"{num}_{base}", "aspect_ratio": ar, "size": SIZES[ar], "prompt": prompt,
                  "folder": r["folder"], "save_as": r["save_as"], "business_name": r["business_name"], "slot": r["slot"]})
with open(f"{F}/AI_IMAGES_MAP.csv", "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=list(items[0]))
    w.writeheader()
    w.writerows(items)

batches = [items[i:i + per] for i in range(0, len(items), per)]
single = len(batches) == 1
out = [f"""# AI images for the 100 homepages ({len(items)} images{'' if single else f' in {len(batches)} batches'})

## How to use this file
1. Open a Gemini chat that can make images (Gemini app with image generation, or Google AI Studio with an image model).
2. Upload this file and send: "Do the task in this file. Generate all {len(items)} images and give me one zip."
3. If it stops before the end, reply "Continue from the next image, same rules" until every image is done.
4. Download the zip. If it shows images one by one instead, download each and make sure the saved file has EXACTLY
   the name shown under it (for example `004_ai_service_backsplash.jpg`).
5. Send me the zip. I put each image into the right business folder by its name.

## Instructions for Gemini (follow exactly)
```
You are generating photorealistic images for small kitchen and bath remodeling company websites. Below are numbered
images, each with an exact FILE NAME, an ASPECT RATIO and a PROMPT.

For every image:
- Generate exactly one image from its PROMPT, at its ASPECT RATIO (landscape unless the ratio says otherwise).
- Style: realistic architectural/interior photography, natural light, true-to-life materials, sharp focus, no
  illustration or 3D-render look, no fantasy elements.
- Never include: people's faces, readable text, logos, brand names, watermarks, signatures, frames or borders.
- Name the image file EXACTLY as its FILE NAME (lowercase, same underscores, .jpg). Never rename, number or shorten.
- Under each image, write its FILE NAME on its own line so it can be matched.
- Generate ALL images in this file, in order, in one go, without asking questions or stopping between images.
- When all are done, put every image into ONE zip named ai_images_all.zip, keeping the exact file names.
- If an image fails a safety or quality check, retry once with the same prompt; if it fails again, write
  "FAILED: <file name>" and continue.
```
"""]
for bi, b in enumerate(batches, 1):
    out.append(f"\n## Images\n" if single else f"\n## Batch {bi} of {len(batches)} ({len(b)} images)\n")
    for k, it in enumerate(b, 1):
        n = (bi - 1) * per + k
        out.append(f"\n### Image {n}\nFILE NAME: {it['file_name']}\nASPECT RATIO: {it['aspect_ratio']} (about {it['size']} px)\n"
                   f"PROMPT: {it['prompt']}\n")
open(f"{F}/GEMINI_AI_IMAGES.md", "w").write("".join(out))
print(len(items), "images in", len(batches), "batches")
