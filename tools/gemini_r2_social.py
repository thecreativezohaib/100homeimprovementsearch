#!/usr/bin/env python3
"""Round 2 content dive for the 120 finalists (main + reserve): Gemini files of 10 businesses each
(output/round2/gemini/social_parts/, zipped). Asks for the brand (logo, cover photo, colours, tagline), the About
text and facts, up to 30 posts per platform with direct image links, and up to 15 Google reviews (this server only
sees Google's limited view). Usage: gemini_r2_social.py"""
import csv, io, os, zipfile

O = "/home/user/100homeimprovementsearch/output/round2"
PROMPT = """```
You are collecting real content to build a homepage for each small kitchen and bath remodeling business in the table
below. Use Google Search, Google Maps, Facebook and Instagram. For EVERY business, open its Google Maps listing, its
Facebook page (facebook_url) and its Instagram profile (instagram_url). If a link is "none", search for the account
by name + town + phone and use it only if it clearly belongs to this business.

Output THREE kinds of rows for each business, all in ONE CSV:

1) kind = summary (one row per business)
- logo_url: direct image link of the business logo (the Facebook profile picture or Instagram profile picture,
  full size), and logo_text: the words and colours you see in the logo
- cover_photo_url: direct image link of the Facebook cover photo
- brand_colors: the 2 or 3 main colours of the logo / cover / truck / signs, as hex codes if you can (e.g. #1F3A5F)
- tagline: a slogan they use (exact words) or UNKNOWN
- about_text: Facebook Intro/About and Instagram bio, copied exactly
- services: every service they show or name, separated by semicolons
- service_towns: every town, county or area they name, separated by semicolons
- owner_name, team_names, years_in_business, licence_or_insurance, warranty, free_estimate, financing, hours,
  phone, email: only what a page states (exact words for licence, warranty, years)
- google_rating, google_review_count, facebook_followers, instagram_followers
- videos_summary: what their videos/reels show (one line each, up to 5)

2) kind = post (up to 30 per platform, newest first)
- platform, post_url, post_date (as shown), caption (exact, up to 300 characters), project_type (kitchen, bathroom,
  shower, cabinets, countertops, tile, flooring, other), town (only if named)
- image_urls: the DIRECT full-size image links of the photos in the post (links that end in .jpg/.png or come from
  scontent / fbcdn / cdninstagram), separated by spaces. These are the most important part: I need the real project
  photos.
- is_before_after: yes or no

3) kind = review (up to 15 per business: Google reviews first, then Facebook recommendations)
- platform (google or facebook), reviewer (first name and last initial only), review_date (as shown), stars,
  review_text (exact), owner_reply (exact, or none)

RULES
- Never guess or invent. Unknown means UNKNOWN. Copy text exactly.
- Plain full URLs only (no [text](url), no google.com redirect links).
- Process every business in this file; do not stop to ask me. If you run out of room, finish the business you are
  on and end with: LAST_ROW_DONE: <row>.

OUTPUT: CSV in one ```csv block with exactly this header (put text containing commas in double quotes):
row,kind,platform,post_url,post_date,caption,project_type,town,image_urls,is_before_after,reviewer,review_date,stars,review_text,owner_reply,logo_url,logo_text,cover_photo_url,brand_colors,tagline,about_text,services,service_towns,owner_name,team_names,years_in_business,licence_or_insurance,warranty,free_estimate,financing,hours,phone,email,google_rating,google_review_count,facebook_followers,instagram_followers,videos_summary
Keep the business's row number on every line.
```"""
R = [r for r in csv.DictReader(open(f"{O}/R2_FINALISTS.csv")) if r["tier"] != "backup"]
d = f"{O}/gemini/social_parts"
os.makedirs(d, exist_ok=True)
for f in os.listdir(d):
    os.remove(f"{d}/{f}")
per, names = 10, []
tot = (len(R) + per - 1) // per
for i in range(0, len(R), per):
    ch, n = R[i:i + per], i // per + 1
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n")
    w.writerow(["row", "business_name", "phone", "address", "google_maps", "facebook_url", "instagram_url"])
    for r in ch:
        w.writerow([r["row"], r["business_name"], r["phone"], r["address"], r["maps_url"], r["facebook_url"] or "none", r["instagram_url"] or "none"])
    md = f"""# Round 2 homepage content dive, part {n:02d} of {tot:02d} ({len(ch)} businesses)

## What to do
1. A NEW Gemini chat for this part (Agent mode or Deep Research), upload this file, send "Do the task in this file."
2. Run all parts at the same time if you like. Send me all the CSVs (or reports) together.
3. If one stops early, reply "Continue with the next business, same rules, same columns".

## The task (Gemini: follow this exactly)
{PROMPT}

## Businesses
```csv
{buf.getvalue()}```
"""
    nm = f"GEMINI_R2_CONTENT_part{n:02d}.md"
    open(f"{d}/{nm}", "w").write(md)
    names.append(nm)
with zipfile.ZipFile(f"{O}/gemini/GEMINI_R2_CONTENT_parts.zip", "w", zipfile.ZIP_DEFLATED) as z:
    for nm in names:
        z.write(f"{d}/{nm}", nm)
print(len(R), "businesses in", len(names), "parts")
