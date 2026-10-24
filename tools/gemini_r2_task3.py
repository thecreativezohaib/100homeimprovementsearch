#!/usr/bin/env python3
"""Round 2, task 3: parallel Gemini files of 50 businesses (output/round2/gemini/task3_parts/, zipped).
Rows come in this order:
  E  an email is known but no Facebook or Instagram: find the social accounts only
  F  a Facebook or Instagram is known but no email: dig for the email only
  N  task 2 rows Gemini has not reached yet: all checks
Rows whose website Gemini found live, and rows that already qualify, are left out.
Usage: gemini_r2_task3.py [per_part=50]"""
import csv, io, json, math, os, re, sys, zipfile

R = "/home/user/100homeimprovementsearch"
D, G = f"{R}/data/r2", f"{R}/output/round2/gemini"
per = int(sys.argv[1]) if len(sys.argv) > 1 else 50
base = {r["row"]: r for r in csv.DictReader(io.StringIO(open(f"{G}/GEMINI_R2_TASK2.md").read().split("```csv\n")[-1].split("```")[0]))}
found = {r["row"]: r for r in csv.DictReader(open(f"{D}/task2_all.csv"))}
prog = json.load(open(f"{D}/task2_progress.json"))
qual = json.load(open(f"{D}/qualified.json"))
done = {q["row"] for q in qual}


def k(v):
    return v if v and v.strip().upper() not in ("UNKNOWN", "NONE", "N/A") else ""


rows = {"E": [], "F": [], "N": []}
for row in base:
    f = found.get(row)
    if row in done or not f or f["website_status"].strip().lower() == "live":
        continue
    soc = k(f["facebook_url"]) or k(f["instagram_url"])
    if k(f["email"]) and not soc:
        rows["E"].append(row)
    elif soc and not k(f["email"]):
        rows["F"].append(row)
rows["N"] = [r for r in prog["left"] if r not in done]

# task 1 rows with a social account but no email were not carried into task 2; add them as F rows
gate_a = {g["id"]: g for g in json.load(open(f"{D}/gateA.json"))}
rowmap = json.load(open(f"{D}/gemini_rowmap.json"))
dead1 = {x["row"] for x in json.load(open(f"{D}/verdicts_task1.json"))["dead_site_no_email"]}
for t in csv.DictReader(open(f"{D}/gemini_in/task.csv")):
    row = t["row"]
    if row in base or row in done or not (k(t["facebook_url"]) or k(t["instagram_url"])) or k(t["email"]):
        continue
    if k(t["website_found"]) and row not in dead1:
        continue
    g = gate_a[rowmap[row]]
    d = re.sub(r"\D", "", g.get("phone") or "")[-10:]
    addr = (g.get("address") or "").replace("\ue0c8", "").strip().replace(", United States", "")
    base[row] = {"business_name": g.get("title") or g.get("name"), "town": g.get("city") or "",
                 "phone": f"({d[:3]}) {d[3:6]}-{d[6:]}" if len(d) == 10 else "", "address": addr or "service-area business",
                 "google_maps": g["maps_url"], "known_facebook": "none", "known_instagram": "none", "known_email": "none",
                 "dead_website": "none"}
    found[row] = t | {"website_status": "dead" if row in dead1 else "NONE"}
    rows["F"].append(row)

out = []
for t in "EFN":
    for row in rows[t]:
        b, f = base[row], found.get(row, {})
        out.append({"row": row, "task": t, "business_name": b["business_name"], "town": b["town"], "phone": b["phone"],
                    "address": b["address"], "google_maps": b["google_maps"],
                    "known_facebook": k(f.get("facebook_url")) or b["known_facebook"],
                    "known_instagram": k(f.get("instagram_url")) or b["known_instagram"],
                    "known_email": (f"{f['email']} (seen at {f['email_source_url']})" if k(f.get("email")) else b["known_email"]),
                    "known_owner": k(f.get("owner_name")) or "none",
                    "dead_website": k(f.get("website_found")) if f.get("website_status", "").lower() == "dead" else b["dead_website"]})

HEADER = ("row,business_name,facebook_url,instagram_url,email,email_source_url,email_source_quote,website_found,"
          "website_status,owner_name,facebook_followers,facebook_latest_post_date,instagram_followers,"
          "instagram_latest_post_date,photo_posts,sources_checked,notes")
PROMPT = """```
You are doing a research task on {n} small kitchen and bathroom remodeling businesses in the United States. Each one
has a Google Business Profile but no working website. I need, for each one: a contact email that the business itself
has published, and its own Facebook page and/or Instagram profile. Work through the table at the end of this file
from top to bottom and do NOT skip any. Research every row BEFORE you write the report.

The "task" column says what each row needs:
- E: the email is already known (known_email). Find ONLY the business's own Facebook page and Instagram profile.
  Search "<business_name>" <town> facebook, "<business_name>" instagram, the phone number in quotes, the known email
  in quotes, and the owner's name (known_owner) with the business name. Check the Facebook and Instagram links shown
  on its Yelp, Houzz, Angi, BBB, Nextdoor, Thumbtack and Birdeye pages. Copy the known email into the email columns.
- F: the Facebook/Instagram is already known. Find ONLY a published email. Open the known page and read the Intro,
  About, contact info, Page transparency, and the captions of its posts, photos, flyers and business card images.
  Then search the phone number in quotes together with "@gmail.com", "@yahoo.com", "@aol.com", "@outlook.com",
  "@hotmail.com", "@icloud.com" and "email"; search "<business_name>" email; search the owner's name with "@".
  Check BBB, Yelp, Houzz, Angi, HomeAdvisor, Thumbtack, Nextdoor, Porch, BuildZoom, Manta, Alignable, Birdeye,
  Chamber of Commerce listings, the state contractor licence lookup, the state business registry (annual reports
  often show an email), USDOT/FMCSA records, local newspapers, church bulletins, realtor "preferred vendor" pages and
  supplier "find an installer" pages. If dead_website is given, read its archived pages on the Wayback Machine.
- N: new. Do all of the above: find the Facebook page, the Instagram profile and the email, and check for a website.

WEBSITE CHECK (every row): if the business has its own website that loads and shows the business, put it in
website_found with website_status = live. If a site exists but is down, parked, "coming soon", expired or a "domain not
connected" page, write website_status = dead. Facebook, Instagram, Linktree and directory pages are NOT websites.

RULES
- Never guess or build an email from a name pattern. Only copy an email you actually saw, with the page URL
  (email_source_url) and a quote of 20 words or fewer from that page containing it (email_source_quote).
- People-search and email-finder sites (ContactOut, RocketReach, ZoomInfo, Whitepages, TruePeopleSearch,
  FastPeopleSearch and similar) do NOT count.
- Accept a page, profile or email only if it clearly belongs to THIS business (same name and the same phone, town or
  owner). If unsure, leave it out and say why in notes.
- Plain full URLs only. sources_checked: every source you opened, separated by semicolons. Keep the row numbers.
- Keep the written part of the report to a few lines. Spend your effort on research, not on writing.
- If you run out of room, finish the business you are on and end with LAST_ROW_DONE: <row number>.

OUTPUT
End with ONE CSV block (in a ```csv code block) with exactly this header:
{header}
- One line for EVERY business in the table (also when nothing was found: then use UNKNOWN). Text containing a comma
  goes in double quotes.
- Then one line: LAST_ROW_DONE: <row number of the last business you finished>.
```"""

pdir = f"{G}/task3_parts"
os.makedirs(pdir, exist_ok=True)
for f in os.listdir(pdir):
    os.remove(f"{pdir}/{f}")
parts = math.ceil(len(out) / per)
names = []
for i in range(parts):
    chunk = out[i * per:(i + 1) * per]
    buf = io.StringIO()
    w = csv.DictWriter(buf, fieldnames=list(chunk[0]), lineterminator="\n")
    w.writeheader()
    w.writerows(chunk)
    kinds = ", ".join(f"{sum(1 for c in chunk if c['task'] == t)} {t}" for t in "EFN" if any(c["task"] == t for c in chunk))
    md = f"""# Round 2: Gemini task 3, part {i + 1:02d} of {parts:02d} ({len(chunk)} businesses: {kinds})

## What to do
1. Open a NEW Gemini chat for this part, pick **Deep Research**, upload this file, send "Do the task in this file."
   and click **Start research**. Run as many parts at the same time as you like.
2. When it finishes, copy the whole report (or export it) and keep it. Send me all of them together.
3. If a report ends with `LAST_ROW_DONE` before row {chunk[-1]['row']}, reply in that chat "Continue with the businesses
   after LAST_ROW_DONE, same rules, same columns" and keep that report too.

## The task (Gemini: follow this exactly)
{PROMPT.format(n=len(chunk), header=HEADER)}

## Businesses ({len(chunk)}, in order)
```csv
{buf.getvalue()}```
"""
    name = f"GEMINI_R2_T3_part{i + 1:02d}.md"
    open(f"{pdir}/{name}", "w").write(md)
    names.append(name)
with zipfile.ZipFile(f"{G}/GEMINI_R2_T3_parts.zip", "w", zipfile.ZIP_DEFLATED) as z:
    for n in names:
        z.write(f"{pdir}/{n}", n)
print({t: len(v) for t, v in rows.items()}, "rows", len(out), "parts", parts)
