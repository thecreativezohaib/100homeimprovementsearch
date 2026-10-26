#!/usr/bin/env python3
"""Round 3: lint the written kit folders and package them.
Checks every output/round3/kit/<n>_<slug>/content.json (valid sections, image files exist, no em dash, banned phrases
only outside quoted reviews, testimonials word for word in the Google reviews, footer phone = Google phone, title,
meta and H1 lengths, no aggregateRating, gallery real photos only), then writes INDEX.csv, AI_IMAGE_PROMPTS.csv,
GEMINI_AI_IMAGES.md (one file for Gemini, globally unique image names <n>_<ai_file_name>), AI_IMAGES_MAP.csv,
README.md and the zip output/round3/<name>.zip with the folders, the needs list and those files.
Usage: r3_package.py <zip name> [n,n,... to include; default all written folders]"""
import csv, glob, json, os, re, sys, zipfile

R = "/home/user/100homeimprovementsearch"
K, O = f"{R}/output/round3/kit", f"{R}/output/round3"
name = sys.argv[1]
only = {int(x) for x in sys.argv[2].split(",")} if len(sys.argv) > 2 else None
BANNED = ("look no further", "one-stop shop", "we pride ourselves", "second to none", "top-notch", "unparalleled")
SIZES = {"16:9": "1920x1080", "4:3": "1600x1200", "4:5": "1200x1500", "21:9": "2520x1080"}


def digits(s):
    return re.sub(r"\D", "", s or "")[-10:]


def strings(o, path=""):
    if isinstance(o, dict):
        for k, v in o.items():
            yield from strings(v, f"{path}.{k}")
    elif isinstance(o, list):
        for i, v in enumerate(o):
            yield from strings(v, f"{path}[{i}]")
    elif isinstance(o, str):
        yield path, o


rows, prompts = [], []
folders = [d for d in sorted(glob.glob(f"{K}/[0-9]*_*")) if os.path.exists(f"{d}/content.json")
           and (only is None or int(os.path.basename(d)[:3]) in only)]
for d in folders:
    c, r = json.load(open(f"{d}/content.json")), json.load(open(f"{d}/research.json"))
    issues = []
    for p, s in strings(c):
        quoted = re.search(r"testimonials", p)
        if "—" in s:
            issues.append(f"em dash at {p}")
        if not quoted and not re.search(r"missing|facts_used|images_not_to_use", p):
            issues += [f"'{b}' at {p}" for b in BANNED if b in s.lower()]
    reviews = " ".join(x.get("text") or "" for x in r["google"].get("reviews") or [])
    norm = lambda s: re.sub(r"\s+", " ", s).strip()
    for t in (c.get("testimonials") or {}).get("items") or []:
        if norm(t.get("text", "")) not in norm(reviews):
            issues.append(f"testimonial not word for word: {t.get('name')}")
    if digits((c.get("footer") or {}).get("phone")) != digits(r["google"].get("phone")):
        issues.append("footer phone differs from Google")
    seo, hero = c.get("seo") or {}, c.get("hero") or {}
    if not 45 <= len(seo.get("title_tag", "")) <= 62:
        issues.append(f"title length {len(seo.get('title_tag', ''))}")
    if not 135 <= len(seo.get("meta_description", "")) <= 162 or seo.get("meta_description", "").endswith("..."):
        issues.append(f"meta length {len(seo.get('meta_description', ''))}")
    if len(hero.get("h1", "")) >= 70:
        issues.append("h1 too long")
    if (c.get("schema_jsonld") or {}).get("aggregateRating"):
        issues.append("aggregateRating")
    plan = c.get("image_plan") or []
    for e in plan:
        if e.get("file") and not os.path.exists(f"{d}/{e['file']}"):
            issues.append(f"missing file {e['file']}")
        if e.get("source") == "ai" and str(e.get("slot", "")).startswith("gallery"):
            issues.append("AI image in gallery")
        if e.get("source") == "ai" and not e.get("ai_prompt"):
            issues.append(f"AI slot without prompt {e.get('slot')}")
    folder = os.path.basename(d)
    real = len({e["file"] for e in plan if e.get("source") == "real" and e.get("file")})
    ai = [e for e in plan if e.get("source") == "ai"]
    for e in ai:
        ar = (re.findall(r"\b(16:9|4:3|4:5|21:9)\b", e["ai_prompt"]) or ["4:3"])[-1]
        pr = re.sub(r"[,.;]?\s*(aspect ratio|aspect)?\s*:?\s*\b(16:9|4:3|4:5|21:9)\b\s*(aspect ratio)?\s*\.?\s*$", "", e["ai_prompt"].strip(), flags=re.I)
        pr = re.sub(r"[,.;]?\s*aspect ratio\s*$", "", pr, flags=re.I).rstrip(" ,.;") + "."
        prompts.append({"file_name": f"{folder[:3]}_{e['ai_file_name']}", "aspect_ratio": ar, "size": SIZES[ar], "prompt": pr,
                        "folder": folder, "save_as": f"images/{e['ai_file_name']}", "business_name": r["business_name"],
                        "slot": e.get("slot")})
    rows.append({"folder": folder, "business_name": r["business_name"], "phone": r["google"].get("phone"),
                 "email": (c.get("footer") or {}).get("email", ""), "email_published_at": r["email"].get("published_at"),
                 "facebook": r.get("facebook_url") or "", "instagram": r.get("instagram_url") or "",
                 "google_maps": r["google"].get("maps_url"), "primary_keyword": seo.get("primary_keyword", ""),
                 "real_photos": real, "ai_slots": len(ai), "testimonials": len((c.get("testimonials") or {}).get("items") or []),
                 "to_confirm": " | ".join(str(m) for m in (c.get("missing") or [])[:4]),
                 "outreach_detail": (c.get("outreach") or {}).get("specific_detail", ""), "lint_issues": "; ".join(issues)})

for fn, data in (("INDEX.csv", rows), ("AI_IMAGE_PROMPTS.csv", prompts), ("AI_IMAGES_MAP.csv", prompts)):
    with open(f"{K}/{fn}", "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(data[0]))
        w.writeheader()
        w.writerows(data)
md = [f"""# AI images for the round 3 homepages ({len(prompts)} images)

## How to use this file
1. Open a Gemini chat that can make images and upload this file.
2. Send: "Do the task in this file. Generate all {len(prompts)} images and give me one zip."
3. Download the zip (or save the chat page as "Webpage, Complete") and send it back.

## Instructions for Gemini (follow exactly)
```
Generate one photorealistic image per item below, in order, without asking questions. Realistic interior and
architectural photography, natural light, true-to-life materials, sharp focus, no 3D-render look. Never include
people's faces, readable text, logos, brand names, watermarks or frames. Use the given aspect ratio.
Name each file EXACTLY as its FILE NAME and write the FILE NAME on its own line directly under each image.
When done, put all images into one zip named ai_images_round3.zip with those exact names. If an image fails twice,
write "FAILED: <file name>" and continue.
```

## Images
"""]
for i, p in enumerate(prompts, 1):
    md.append(f"\n### Image {i}\nFILE NAME: {p['file_name']}\nASPECT RATIO: {p['aspect_ratio']} (about {p['size']} px)\nPROMPT: {p['prompt']}\n")
open(f"{K}/GEMINI_AI_IMAGES.md", "w").write("".join(md))
nl = sum(1 for x in rows if x["lint_issues"])
open(f"{K}/README.md", "w").write(f"""# Round 3 homepage kit ({len(rows)} businesses)

Each folder: `content.json` (the page in the round 2 structure, with `image_plan`), `content.md` (readable copy, image
plan, facts used, what to confirm), `images/` (their own Google Maps photos, plus their own Facebook photos where they
were verified), `images.json`, `research.json` (Google data and every Google review captured, email and where it was
published), `contact_sheet.jpg`.

- Testimonials are Google reviews quoted word for word with the reviewer and date as shown.
- Facts come from Google and the business's own posts. Anything only another AI reported is left out and listed in
  `missing` as "to confirm with owner". Towns taken from earlier research are used only when the phone's area code
  matches, and are flagged to confirm.
- Emails were published on Facebook or Instagram, which could not be opened from here: each page says "confirm email".
- AI slots (`"source": "ai"`) have a prompt and a file name; `GEMINI_AI_IMAGES.md` generates them all at once
  (names `<folder number>_<file>`). Galleries use real photos only.
- `INDEX.csv`: contacts, keyword, photo / AI / testimonial counts, first items to confirm ({nl} with lint notes).
- `R3_B1_NEEDS.csv`: the batch 1 businesses that need more photos, a Maps link or reviews before a page can be built.
""")
zp = f"{O}/{name}.zip"
with zipfile.ZipFile(zp, "w", zipfile.ZIP_DEFLATED) as z:
    for f in ("README.md", "INDEX.csv", "AI_IMAGE_PROMPTS.csv", "AI_IMAGES_MAP.csv", "GEMINI_AI_IMAGES.md"):
        z.write(f"{K}/{f}", f"{name}/{f}")
    z.write(f"{O}/R3_B1_NEEDS.csv", f"{name}/R3_B1_NEEDS.csv")
    for f in ("CONTENT_BRIEF_R2.md", "content_schema_r2.json"):
        z.write(f"{R}/output/round2/kit/{f}", f"{name}/{f}")
    for d in folders:
        for root, _, files in os.walk(d):
            for fn in files:
                p = os.path.join(root, fn)
                z.write(p, f"{name}/homepages/{os.path.relpath(p, K)}")
print("folders", len(rows), "| lint notes", nl, "| AI images", len(prompts), "| zip MB", round(os.path.getsize(zp) / 1e6, 1))
for x in rows:
    print(x["folder"], x["real_photos"], "real,", x["ai_slots"], "AI,", x["testimonials"], "reviews |", x["lint_issues"][:150])
