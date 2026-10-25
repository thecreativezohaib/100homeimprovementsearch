#!/usr/bin/env python3
"""Round 2 kit inputs: one folder per business under output/round2/kit/sites/<rank>_<slug>/ (main 100) and
output/round2/kit/reserves/ (next 20), each with
  research.json  every fact the writer may use: Google profile (deep capture), Gemini content dive (summary, posts,
                 reviews), the verified email and where it was published, owner, rank
  images/        the business's photos (Maps cover/profile/review photos, Facebook and Instagram post photos),
                 renamed by source, plus logo and cover when found
  images.json    one entry per image: file, source, size, caption / post / review it came with
  brand.json     palette taken from the logo (or cover photo, or project photos), logo file, tagline
  contact_sheet.jpg  numbered thumbnails of every image, for choosing the hero and writing alt text
Usage: r2_bundles.py"""
import csv, json, os, re, shutil, glob, colorsys
from PIL import Image, ImageDraw, ImageOps

R = "/home/user/100homeimprovementsearch"
D, K = f"{R}/data/r2", f"{R}/output/round2/kit"
fin = list(csv.DictReader(open(f"{R}/output/round2/R2_FINALISTS.csv")))
deep = {r["row"]: r for f in glob.glob(f"{D}/deep_out*.jsonl") for r in map(json.loads, filter(str.strip, open(f)))}
content = list(csv.DictReader(open(f"{D}/gemini_in/content_all.csv", encoding="utf-8-sig")))
vet = {v["row"]: v for v in json.load(open(f"{D}/finalists_ranked.json"))}
man = [m for m in json.load(open(f"{D}/images_manifest.json")) if m["ok"]]


def clean(v):
    return v if v and v.strip().upper() not in ("UNKNOWN", "NONE", "N/A") else None


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")[:48]


def palette(path, n=4):
    """dominant colours, skipping near-white, near-black and grey background tones"""
    im = Image.open(path).convert("RGB")
    im.thumbnail((200, 200))
    q = im.quantize(colors=12, method=Image.Quantize.MEDIANCUT)
    pal, counts = q.getpalette(), sorted(q.getcolors(), reverse=True)
    out = []
    for c, i in counts:
        r, g, b = pal[i * 3:i * 3 + 3]
        h, l, s = colorsys.rgb_to_hls(r / 255, g / 255, b / 255)
        if l > 0.93 or l < 0.06 or (s < 0.12 and 0.2 < l < 0.85 and out):
            continue
        hx = "#%02X%02X%02X" % (r, g, b)
        if all(sum(abs(int(hx[k:k + 2], 16) - int(o[k:k + 2], 16)) for k in (1, 3, 5)) > 60 for o in out):
            out.append(hx)
        if len(out) == n:
            break
    return out


def sheet(files, path):
    tw, th, cols = 260, 195, 6
    rows = (len(files) + cols - 1) // cols
    canvas = Image.new("RGB", (cols * tw, max(1, rows) * (th + 22)), "white")
    d = ImageDraw.Draw(canvas)
    for i, f in enumerate(files):
        try:
            im = ImageOps.fit(Image.open(f).convert("RGB"), (tw - 6, th - 6))
        except Exception:
            continue
        x, y = (i % cols) * tw, (i // cols) * (th + 22)
        canvas.paste(im, (x + 3, y + 3))
        d.text((x + 6, y + th + 4), os.path.basename(f), fill="black")
    canvas.save(path, "JPEG", quality=80)


for sub in ("sites", "reserves"):
    shutil.rmtree(f"{K}/{sub}", ignore_errors=True)
index = []
for r in fin:
    if r["tier"] == "backup":
        continue
    row, rank = r["row"], int(r["rank"])
    folder = f"{K}/{'sites' if r['tier'] == 'main' else 'reserves'}/{rank:03d}_{slug(r['business_name'])}"
    os.makedirs(f"{folder}/images", exist_ok=True)
    dp, v = deep.get(row, {}), vet.get(row, {})
    rows = [c for c in content if c["row"] == row]
    summ = next((c for c in rows if c["kind"] == "summary"), {})
    imgs = []
    for m in sorted([m for m in man if m["row"] == row], key=lambda m: (m["kind"] != "logo", m["kind"] != "cover", m["kind"] != "post", m["name"])):
        dst = f"{folder}/images/{m['name']}.jpg"
        shutil.copy(m["file"], dst)
        e = {"file": f"images/{m['name']}.jpg", "source": {"maps": "Google Maps", "post": "Facebook/Instagram post",
             "logo": "Facebook/Instagram profile picture", "cover": "Facebook cover photo"}[m["kind"]],
             "width": m.get("w"), "height": m.get("h"), "url": m["url"]}
        if m["kind"] == "post":
            e.update({"post_url": m.get("post_url"), "caption": m.get("caption"), "project_type": m.get("project_type"), "town": m.get("town")})
        if m["kind"] == "maps":
            rv = next((x for x in dp.get("reviews") or [] if any(m["url"].split("=")[0] in p for p in x.get("photos") or [])), None)
            e["from_review"] = {"reviewer": rv["reviewer"], "when": rv["when"]} if rv else None
        imgs.append(e)
    json.dump(imgs, open(f"{folder}/images.json", "w"), indent=1)
    sheet([f"{folder}/{e['file']}" for e in imgs if not e["file"].startswith("images/logo")], f"{folder}/contact_sheet.jpg")
    logo = next((e["file"] for e in imgs if e["file"].startswith("images/logo")), None)
    src = logo or next((e["file"] for e in imgs if e["file"].startswith("images/cover")), None)
    pal = palette(f"{folder}/{src}") if src else []
    brand = {"logo_file": logo, "logo_text_seen_by_gemini": clean(summ.get("logo_text")), "palette_from": src,
             "palette": pal, "brand_colors_reported_by_gemini": clean(summ.get("brand_colors")), "tagline": clean(summ.get("tagline"))}
    json.dump(brand, open(f"{folder}/brand.json", "w"), indent=1)
    research = {
        "rank": rank, "tier": r["tier"], "row": row, "business_name": r["business_name"],
        "google": {"maps_url": r["maps_url"], "category": dp.get("category") or r["category"], "rating_label": dp.get("rating_label"),
                   "address": dp.get("address"), "service_area": dp.get("service_area"),
                   "phone": re.sub(r"^phone:tel:", "", dp.get("phone") or r["phone"] or ""),
                   "hours": [h.replace("", "").strip() for h in dp.get("hours") or [] if re.match(r"[A-Z][a-z]+day", h)],
                   "about_text": dp.get("about_text"), "overview_text": dp.get("overview_text"),
                   "reviews_captured_by_me": [{k: x.get(k) for k in ("reviewer", "when", "stars", "text", "owner_reply")} for x in dp.get("reviews") or []]},
        "email": {"address": r["email"], "published_at": r["email_source_url"], "quote": r["email_source_quote"], "check": r["email_check"]},
        "facebook_url": r["facebook_url"] or None, "instagram_url": r["instagram_url"] or None,
        "owner_name_from_research": clean(v.get("owner_name")) if v else None,
        "gemini_summary": {k: clean(summ.get(k)) for k in ("about_text", "services", "service_towns", "owner_name", "team_names",
                           "years_in_business", "licence_or_insurance", "warranty", "free_estimate", "financing", "hours",
                           "google_rating", "google_review_count", "facebook_followers", "instagram_followers", "videos_summary", "tagline")},
        "gemini_posts": [{k: clean(c.get(k)) for k in ("platform", "post_url", "post_date", "caption", "project_type", "town", "is_before_after")} for c in rows if c["kind"] == "post"],
        "gemini_reviews": [{k: clean(c.get(k)) for k in ("platform", "reviewer", "review_date", "stars", "review_text", "owner_reply")} for c in rows if c["kind"] == "review"],
        "note": "gemini_* fields were collected by Gemini from the business's Facebook, Instagram and Google pages and are "
                "not re-verified; reviews_captured_by_me were read on Google Maps directly.",
    }
    json.dump(research, open(f"{folder}/research.json", "w"), indent=1)
    index.append({"rank": rank, "tier": r["tier"], "row": row, "folder": os.path.relpath(folder, K), "business_name": r["business_name"],
                  "images": len(imgs), "logo": bool(logo), "palette": pal, "posts": len(research["gemini_posts"]),
                  "reviews": len(research["gemini_reviews"]) + len(research["google"]["reviews_captured_by_me"])})
json.dump(index, open(f"{K}/index.json", "w"), indent=1)
print(len(index), "folders;", sum(1 for i in index if i["images"] == 0), "without images;", sum(i["logo"] for i in index), "with logo")
