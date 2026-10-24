#!/usr/bin/env python3
"""Round 2, one-file Gemini long task (Deep Research / Agent mode): output/round2/gemini/GEMINI_R2_TASK.md.
Keeps the step 1 row numbers, drops firms whose step 1 email came from their own live website, and orders the
rest strongest first: an email already found on a social or directory page, then a known Facebook or Instagram
(from step 1 or the Google profile), then everyone else by Google review count.
Usage: gemini_r2_task.py"""
import csv, io, json, re

R = "/home/user/100homeimprovementsearch"
gate = {g["id"]: g for g in json.load(open(f"{R}/data/r2/gateA.json"))}
rowmap = json.load(open(f"{R}/data/r2/gemini_rowmap.json"))
step1 = {r["row"]: r for r in csv.DictReader(open(f"{R}/data/r2/gemini_in/step1.csv", encoding="utf-8-sig"))}

# step 1 emails found on the firm's own website; each site was fetched and is live (rgvrc.com, row 99, is an empty
# "Just another WordPress site" placeholder, so that firm stays in)
OWN_SITE = {"1", "19", "66", "78", "91", "115", "293", "297", "320", "328", "338", "391", "406", "432", "436", "440",
            "482", "546"}


def known(val):
    return val if val and val != "UNKNOWN" else ""


def social(lst, host):
    for u in lst or []:
        u = u.split("?")[0].rstrip("/")
        if host in u and not re.search(r"/(sharer|share|p|reel|posts|photo|groups)/", u):
            return u
    return ""


def phone(p):
    d = re.sub(r"\D", "", p or "")[-10:]
    return f"({d[:3]}) {d[3:6]}-{d[6:]}" if len(d) == 10 else ""


rows = []
for row, cid in rowmap.items():
    if row in OWN_SITE:
        continue
    g, s = gate[cid], step1.get(row, {})
    fb = known(s.get("facebook_url")) or social(g.get("socials"), "facebook.com")
    ig = known(s.get("instagram_url")) or social(g.get("socials"), "instagram.com")
    em = known(s.get("email"))
    tier = 0 if em else 1 if (fb or ig) else 2
    addr = (g.get("address") or "").replace("", "").strip().replace(", United States", "")
    rows.append((tier, -(g.get("reviews_count") or 0), int(row), {
        "row": row, "business_name": g.get("title") or g.get("name"), "town": g.get("city") or "",
        "phone": phone(g.get("phone")), "address": addr or "service-area business",
        "google_maps": g["maps_url"], "known_facebook": fb or "none", "known_instagram": ig or "none",
        "known_email": f'{em} (seen at {s.get("email_source_url")})' if em else "none"}))
rows.sort(key=lambda t: t[:3])
n = len(rows)
tiers = [sum(1 for t in rows if t[0] == k) for k in range(3)]

buf = io.StringIO()
w = csv.DictWriter(buf, fieldnames=list(rows[0][3]), lineterminator="\n")
w.writeheader()
for t in rows:
    w.writerow(t[3])

HEADER = ("row,business_name,facebook_url,instagram_url,email,email_source_url,email_source_quote,website_found,"
          "owner_name,facebook_followers,facebook_latest_post_date,instagram_followers,instagram_latest_post_date,"
          "photo_posts,sources_checked,notes")

md = f"""# Round 2: one Gemini long task ({n} businesses, one file)

## What to do
1. Open ONE new Gemini chat and switch on the long-task mode: in the tools menu pick **Deep Research** (or **Agent**
   if your Gemini shows it). Upload this file and send it with the short message "Do the task in this file."
2. Gemini shows a research plan. Click **Start research** (do not edit the plan). It works on its own for a long
   time; leave the tab open.
3. When it finishes, open the report and click **Export to Docs** (or copy the CSV block at the end). Send me the
   Doc or the CSV, whichever is easier. I clean and check everything myself.
4. Only if the report ends with `LAST_ROW_DONE: <number>` before the last business: reply in the same chat
   "Continue from the next business after LAST_ROW_DONE, same rules, same columns" and send me both results.

## The task (Gemini: follow this exactly)
```
You are doing a long research task on {n} small kitchen and bathroom remodeling businesses in the United States.
They have a Google Business Profile but no website on it. I need to know which of them I can contact by email and
which have an active Facebook or Instagram account. The businesses are in the table at the end of this file, in
priority order. Work through them top to bottom and do NOT skip any.

FOR EACH BUSINESS, do all of these steps (do not stop at the first result):
1. Facebook: search Google for "<business_name>" <town> facebook, and for the phone number in quotes. Open the
   page you find and confirm it is the same business (same name AND same phone, town or owner). If known_facebook
   is given, open it and check it. On the page, read the Intro, the About / Page transparency / contact info, and
   the latest posts. Note followers and the date of the newest post.
2. Instagram: search "<business_name>" instagram and the handle shown on the Facebook page. Open the profile,
   confirm it is the same business, read the bio and contact button. Note followers and the newest post date.
3. Email: look for an email the BUSINESS ITSELF publishes. Check, in this order: the Facebook About / Intro /
   contact info and posts, the Instagram bio and contact button, the Google Business Profile, then BBB, Yelp,
   Houzz, Angi, Thumbtack, Nextdoor, Porch, BuildZoom, Manta, Alignable, Chamber of Commerce listings, the state
   contractor licence lookup, and Google results for "<business_name>" "@gmail.com" / "@yahoo.com" / email.
   If known_email is given, confirm it on that page or find it on a better page.
4. Website check: search "<business_name>" <town> and the phone number. If the business has its own working
   website anywhere (its own domain, Wix, Squarespace, GoDaddy, WordPress, Weebly and so on), put that URL in
   website_found. A Facebook, Instagram, Linktree, Yelp or other directory page is NOT a website. If none, write NONE.

RULES
- Never guess or build an email from a name pattern. Only copy an email you actually saw on a page, together with
  that page's URL (email_source_url) and a quote of 20 words or fewer from that page that contains the email
  (email_source_quote). If you did not see an email, write UNKNOWN.
- Only accept a Facebook page, Instagram profile or email if it clearly belongs to THIS business (same name and
  same phone, town or owner). If you are not sure, leave it out and explain in notes.
- Plain full URLs only: no [text](url) links, no google.com redirect links, no shortened links.
- sources_checked: list every source you actually opened for that business, separated by semicolons
  (for example: facebook; instagram; google profile; bbb; yelp; houzz; licence lookup).
- Keep each business's row number from the table.
- Do not stop to ask me anything and do not summarise. Spend your effort on research, not on writing prose.
- If you run out of room before the last business, finish the business you are on, output everything so far, and
  end with the line LAST_ROW_DONE: <row number>.

OUTPUT
The report must end with ONE CSV block (in a ```csv code block) with exactly this header:
{HEADER}
- One line for every business where you found at least one of: a Facebook page, an Instagram profile, an email,
  or a website. Unknown fields are UNKNOWN. Put any text containing a comma in double quotes.
- After the CSV block, one line: NOTHING_FOUND: followed by the row numbers of the businesses you researched and
  found nothing for, separated by commas.
```

## Businesses ({n}, in priority order)
- Rows 1 to {tiers[0]} of this list: an email was already found; confirm it and complete the rest.
- Next {tiers[1]}: a Facebook or Instagram account is already known; open it and look for the email.
- Last {tiers[2]}: nothing known yet, ordered by number of Google reviews.

```csv
{buf.getvalue()}```
"""
open(f"{R}/output/round2/gemini/GEMINI_R2_TASK.md", "w").write(md)
print(n, tiers)
