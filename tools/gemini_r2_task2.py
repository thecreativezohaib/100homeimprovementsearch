#!/usr/bin/env python3
"""Round 2, second one-file Gemini long task: output/round2/gemini/GEMINI_R2_TASK2.md.
Gate B screens the second Maps pool (data/r2/mapsb_out*.jsonl) and the first-pool listings gate A rejected with the gate A rules: listing found and open, no
website or only a Facebook/Instagram/Linktree link, a kitchen and bath category (or a general contractor category with
kitchen, bath, cabinet, countertop, tile, shower or tub in the name), 5 or more Google reviews (gate A asked for 15;
Facebook and Instagram fill in the content), and a phone number not already in round 2. New firms get row numbers from 1001 up (data/r2/gemini_rowmap_b.json).
The file lists, in order: task 1 firms with an email but no social account yet, task 1 firms whose website is dead,
gate B firms (a Facebook or Instagram link on the profile first, then by review count), and the task 1 firms Gemini
did not reach.
Usage: gemini_r2_task2.py"""
import csv, glob, io, json, re

R = "/home/user/100homeimprovementsearch"
D = f"{R}/data/r2"
CATS = {"Bathroom remodeler", "Remodeler", "Kitchen remodeler", "Tile contractor", "Cabinet maker", "Countertop store",
        "Granite supplier", "Countertop contractor", "Kitchen supply store", "Kitchen furniture store",
        "Bathroom supply store", "Countertop contractor", "Cabinet store", "Kitchen cabinet store"}
GENERAL = {"Construction company", "General contractor", "Contractor", "Handyman/Handywoman/Handyperson",
           "Flooring contractor", "Carpenter", "Tile store", "Marble contractor", "Woodworker"}
KB_NAME = re.compile(r"kitchen|bath|cabinet|countertop|tile|shower|\btubs?\b|granite|quartz|marble", re.I)
SOCIAL = re.compile(r"facebook\.com|instagram\.com|linktr\.ee", re.I)


def digits(p):
    return re.sub(r"\D", "", p or "")[-10:]


def phone(p):
    d = digits(p)
    return f"({d[:3]}) {d[3:6]}-{d[6:]}" if len(d) == 10 else ""


def reviews(label):
    m = re.search(r"\(([\d,]+)\)", label or "")
    return int(m.group(1).replace(",", "")) if m else 0


def social(lst, host):
    for u in lst or []:
        # keep the id of profile.php?id= links; drop tracking parameters elsewhere
        u = u if "profile.php?id=" in u else u.split("?")[0].rstrip("/")
        u = re.sub(r"(profile\.php\?id=\d+).*", r"\1", u)
        if host in u and not re.search(r"/(sharer|share|p|reel|posts|photo|groups)/", u):
            return u
    return ""


def town(addr, area):
    m = re.search(r",\s*([^,]+),\s*([A-Z]{2})\s+\d{5}", addr or "")
    return f"{m.group(1)}, {m.group(2)}" if m else (area or "").replace("Serves ", "")[:60]


def clean_addr(a):
    return (a or "").replace("", "").strip().replace(", United States", "") or "service-area business"


# task 1 state
gate_a = {g["id"]: g for g in json.load(open(f"{D}/gateA.json"))}
rowmap = json.load(open(f"{D}/gemini_rowmap.json"))
step1 = {r["row"]: r for r in csv.DictReader(open(f"{D}/gemini_in/step1.csv", encoding="utf-8-sig"))}
task1 = {r["row"]: r for r in csv.DictReader(open(f"{D}/gemini_in/task.csv"))}
verd = json.load(open(f"{D}/verdicts_task1.json"))
nothing = set(re.search(r"NOTHING_FOUND:([\d,\s]+)", open(f"{D}/gemini_in/raw.txt").read()).group(1).replace(" ", "").replace("\n", "").split(","))
done = set(task1) | nothing
OWN_SITE = {"1", "19", "66", "78", "91", "115", "293", "297", "320", "328", "338", "391", "406", "432", "436", "440", "482", "546"}
dead_domain = {"254": "hangliterres.com", "577": "lacustoms.us", "3": "primeconstruction.org", "64": "flooringandgranitecoppell.com",
               "552": "tommycuppremodeling.com", "42": "vlgranite.com", "538": "capirocorp.com", "149": "valuecabinetryreno.com",
               "238": "collinbryan.com", "491": "ecctileservices.com", "227": "kbtubrestoration.com", "504": "surfaceprostl.com",
               "441": "virginiashowerandbath.com", "41": "granitekingdomcountertops.com", "415": "amazingreglaze.com",
               "282": "remodelingbyparagon.com", "362": "graceremodelingconstruction.com", "69": "mcmichaelhomerepair.com",
               "219": "coutinorefinishingtubs.com", "96": "swartzcustoms.shadowmediagroup.com"}


def k(v):
    return v if v and v.strip().upper() not in ("UNKNOWN", "NONE") else ""


def a_row(row, task):
    g = gate_a[rowmap[row]]
    t, s = task1.get(row, {}), step1.get(row, {})
    fb = k(t.get("facebook_url")) or k(s.get("facebook_url")) or social(g.get("socials"), "facebook.com")
    ig = k(t.get("instagram_url")) or k(s.get("instagram_url")) or social(g.get("socials"), "instagram.com")
    em = k(t.get("email")) or k(s.get("email"))
    return {"row": row, "task": task, "business_name": g.get("title") or g.get("name"), "town": g.get("city") or "",
            "phone": phone(g.get("phone")), "address": clean_addr(g.get("address")), "google_maps": g["maps_url"],
            "known_facebook": fb or "none", "known_instagram": ig or "none",
            "known_email": f"{em} (seen at {k(t.get('email_source_url')) or s.get('email_source_url')})" if em else "none",
            "dead_website": dead_domain.get(row, "none")}


rows = [a_row(x["row"], "A") for x in verd["email_need_social"]]
rows += [a_row(x["row"], "B") for x in verd["dead_site_no_email"]]

# gate B
used_phones = {digits(g.get("phone")) for g in gate_a.values()}
# the second pool, plus first-pool listings that only missed gate A on the stricter rules
recs = [json.loads(l) for f in sorted(glob.glob(f"{D}/mapsb_out*.jsonl")) + sorted(glob.glob(f"{D}/maps_out*.jsonl"))
        for l in open(f) if l.strip()]
recs = [m for m in recs if m["id"] not in gate_a]
gb = []
for m in recs:
    if m.get("error") or not m.get("title") or m.get("permanently_closed"):
        continue
    if m.get("website") and not SOCIAL.search(m["website"]):
        continue
    n = reviews(m.get("rating_label"))
    kb = m.get("category") in CATS or (m.get("category") in GENERAL and KB_NAME.search(m["title"]))
    if not kb or n < 5 or digits(m.get("phone")) in used_phones:
        continue
    used_phones.add(digits(m.get("phone")))
    links = (m.get("socials") or []) + ([m["website"]] if m.get("website") else [])
    m.update(reviews_count=n, fb=social(links, "facebook.com"), ig=social(links, "instagram.com"))
    gb.append(m)
gb.sort(key=lambda m: (0 if (m["fb"] or m["ig"]) else 1, -m["reviews_count"]))
json.dump(gb, open(f"{D}/gateB.json", "w"))
# service-area listings show no address; fall back to the town the Maps search was run in
search_town = {x["id"]: x.get("location") for f in ("pool.json", "pool_b.json") for x in json.load(open(f"{D}/{f}"))}
rowmap_b = {}
for i, m in enumerate(gb):
    row = str(1001 + i)
    rowmap_b[row] = m["id"]
    rows.append({"row": row, "task": "C", "business_name": m["title"], "town": town(m.get("address"), m.get("service_area")) or search_town.get(m["id"]) or "",
                 "phone": phone(m.get("phone")), "address": clean_addr(m.get("address")), "google_maps": m["maps_url"],
                 "known_facebook": m["fb"] or "none", "known_instagram": m["ig"] or "none", "known_email": "none",
                 "dead_website": "none"})
json.dump(rowmap_b, open(f"{D}/gemini_rowmap_b.json", "w"))

# task 1 rows Gemini did not reach, in the task 1 order
left = [r for r in rowmap if r not in OWN_SITE and r not in done]
left.sort(key=lambda r: -(gate_a[rowmap[r]].get("reviews_count") or 0))
rows += [a_row(r, "D") for r in left]

cnt = {t: sum(1 for r in rows if r["task"] == t) for t in "ABCD"}
buf = io.StringIO()
w = csv.DictWriter(buf, fieldnames=list(rows[0]), lineterminator="\n")
w.writeheader()
w.writerows(rows)

HEADER = ("row,business_name,facebook_url,instagram_url,email,email_source_url,email_source_quote,website_found,"
          "website_status,owner_name,facebook_followers,facebook_latest_post_date,instagram_followers,"
          "instagram_latest_post_date,photo_posts,sources_checked,notes")

md = f"""# Round 2: Gemini long task 2 ({len(rows)} businesses, one file)

## What to do (same as last time)
1. Open ONE new Gemini chat, pick **Deep Research** (or **Agent**) in the tools menu, upload this file and send
   "Do the task in this file."
2. Click **Start research** on the plan and leave it running.
3. When it finishes, export it (PDF or Docs is fine, like last time) and send it to me.
4. If the report ends with `LAST_ROW_DONE: <row>`, reply in the same chat: "Continue with the businesses after
   LAST_ROW_DONE, same rules, same columns", and send me each report as it finishes.

## The task (Gemini: follow this exactly)
```
You are doing a long research task on {len(rows)} small kitchen and bathroom remodeling businesses in the United
States. Each one has a Google Business Profile but no working website. For each one I need: a contact email that the
business itself has published, and its Facebook page and/or Instagram profile. Work through the table at the end of
this file from top to bottom, in that order, and do NOT skip any.

The "task" column tells you what each row needs most:
- A ({cnt['A']} rows): the email is already known. Find the business's own Facebook page and Instagram profile.
- B ({cnt['B']} rows): the website in dead_website no longer works. Find the email: open the Wayback Machine
  (https://web.archive.org/web/2024*/<dead_website>*) and read the archived contact, about and home pages, then do
  the normal checks below. Also confirm the website is really down (website_status).
- C ({cnt['C']} rows): new businesses. Do all the checks below.
- D ({cnt['D']} rows): new to you as well. Do all the checks below.

CHECKS FOR EACH BUSINESS (do every step; do not stop at the first result):
1. Facebook: search Google for "<business_name>" <town> facebook, and for the phone number in quotes
   (for example "(352) 988-7800" and "352-988-7800"). Open the page and confirm it is the same business (same name
   AND same phone, town or owner). If known_facebook is given, open it. Read the Intro, About, Page transparency and
   contact info, and the captions of its latest posts and photos. Small contractors often write their email in a
   post caption, a photo caption, a flyer or a business card photo. Note followers and the newest post date.
2. Instagram: search "<business_name>" instagram and the handle from the Facebook page. Read the bio, the contact
   button and the latest captions. Note followers and the newest post date.
3. Email: search Google for the phone number together with "@gmail.com", "@yahoo.com", "@aol.com", "@outlook.com",
   "@hotmail.com" and "email". Then check the Google Business Profile, BBB, Yelp, Houzz, Angi, HomeAdvisor,
   Thumbtack, Nextdoor, Porch, BuildZoom, Manta, Alignable, Birdeye, MapQuest, Chamber of Commerce listings, the state
   contractor licence lookup, the state business registry, local newspaper articles, and supplier "find an
   installer" pages.
4. Website check: search "<business_name>" <town> and the phone number. If the business has its own website that
   loads and shows the business, put it in website_found and write website_status = live. If a site exists but is
   down, parked, "launching soon", expired or a "domain not connected" page, put it in website_found and write
   website_status = dead. A Facebook, Instagram, Linktree, Yelp or directory page is NOT a website. If none: NONE.

RULES
- Never guess or build an email from a name pattern. Only copy an email you actually saw on a page, with that page's
  URL (email_source_url) and a quote of 20 words or fewer from that page that contains it (email_source_quote).
  People-search and email-finder sites (ContactOut, RocketReach, ZoomInfo, Whitepages and similar) do NOT count.
- Accept a Facebook page, Instagram profile or email only if it clearly belongs to THIS business (same name and the
  same phone, town or owner). If unsure, leave it out and say why in notes.
- Plain full URLs only: no [text](url) links, no google.com redirect links, no shortened links.
- sources_checked: every source you actually opened for that business, separated by semicolons.
- Keep each business's row number from the table.
- Do not stop to ask me anything and do not write long prose. Spend your effort on the research. A short summary at
  the top is enough.
- If you run out of room before the last business, finish the one you are on, output everything so far, and end
  with the line LAST_ROW_DONE: <row number>.

OUTPUT
End the report with ONE CSV block (in a ```csv code block) with exactly this header:
{HEADER}
- One line for every business where you found at least one of: a Facebook page, an Instagram profile, an email or
  a website. Unknown fields are UNKNOWN. Put any text containing a comma in double quotes.
- After the CSV block, one line: NOTHING_FOUND: followed by the row numbers you researched and found nothing for,
  separated by commas.
```

## Businesses ({len(rows)}, in order)
```csv
{buf.getvalue()}```
"""
open(f"{R}/output/round2/gemini/GEMINI_R2_TASK2.md", "w").write(md)
print(len(rows), cnt, "gate B", len(gb), "with social", sum(1 for m in gb if m["fb"] or m["ig"]))
