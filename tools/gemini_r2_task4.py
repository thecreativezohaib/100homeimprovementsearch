#!/usr/bin/env python3
"""Round 2, task 4: gate the discovery round 20 listings (data/r2/mapsc_out*.jsonl) with the gate B rules and write
one Gemini file with the task 3 prompt (all checks, task N): output/round2/gemini/GEMINI_R2_T4.md.
New rows are numbered from 3001 (data/r2/gemini_rowmap_c.json). Usage: gemini_r2_task4.py"""
import csv, glob, io, json, re

R = "/home/user/100homeimprovementsearch"
D, G = f"{R}/data/r2", f"{R}/output/round2/gemini"
CATS = {"Bathroom remodeler", "Remodeler", "Kitchen remodeler", "Tile contractor", "Cabinet maker", "Countertop store",
        "Granite supplier", "Countertop contractor", "Kitchen supply store", "Kitchen furniture store",
        "Bathroom supply store", "Cabinet store", "Kitchen cabinet store"}
GENERAL = {"Construction company", "General contractor", "Contractor", "Handyman/Handywoman/Handyperson",
           "Flooring contractor", "Carpenter", "Tile store", "Marble contractor", "Woodworker"}
KB_NAME = re.compile(r"kitchen|bath|cabinet|countertop|tile|shower|\btubs?\b|granite|quartz|marble", re.I)
SOCIAL = re.compile(r"facebook\.com|instagram\.com|linktr\.ee", re.I)
digits = lambda p: re.sub(r"\D", "", p or "")[-10:]
used = {digits(g.get("phone")) for f in ("gateA.json", "gateB.json") for g in json.load(open(f"{D}/{f}"))}
town_of = {x["id"]: x.get("location") for x in json.load(open(f"{D}/pool_c.json"))}
rows, rowmap = [], {}
for f in sorted(glob.glob(f"{D}/mapsc_out*.jsonl")):
    for m in map(json.loads, filter(str.strip, open(f))):
        if m.get("error") or not m.get("title") or m.get("permanently_closed"):
            continue
        if m.get("website") and not SOCIAL.search(m["website"]):
            continue
        n = int((re.search(r"\(([\d,]+)\)", m.get("rating_label") or "") or [0, "0"])[1].replace(",", ""))
        kb = m.get("category") in CATS or (m.get("category") in GENERAL and KB_NAME.search(m["title"]))
        if not kb or n < 5 or digits(m.get("phone")) in used:
            continue
        used.add(digits(m.get("phone")))
        links = (m.get("socials") or []) + ([m["website"]] if m.get("website") else [])
        fb = next((u for u in links if "facebook.com" in u), "none")
        ig = next((u for u in links if "instagram.com" in u), "none")
        a = re.search(r",\s*([^,]+),\s*([A-Z]{2})\s+\d{5}", m.get("address") or "")
        d = digits(m.get("phone"))
        rows.append((0 if fb != "none" or ig != "none" else 1, -n, {
            "task": "N", "business_name": m["title"], "town": f"{a.group(1)}, {a.group(2)}" if a else town_of.get(m["id"], ""),
            "phone": f"({d[:3]}) {d[3:6]}-{d[6:]}" if len(d) == 10 else "",
            "address": (m.get("address") or "").replace("", "").strip().replace(", United States", "") or "service-area business",
            "google_maps": m["maps_url"], "known_facebook": fb, "known_instagram": ig, "known_email": "none",
            "known_owner": "none", "dead_website": "none", "_id": m["id"]}))
rows.sort(key=lambda t: t[:2])
out = []
for i, (_, _, r) in enumerate(rows):
    row = str(3001 + i)
    rowmap[row] = r.pop("_id")
    out.append({"row": row, **r})
json.dump(rowmap, open(f"{D}/gemini_rowmap_c.json", "w"))
tmpl = open(f"{G}/task3_parts/GEMINI_R2_T3_part01.md").read()
task = tmpl.split("## The task (Gemini: follow this exactly)\n")[1].split("## Businesses")[0]
task = re.sub(r"research task on \d+ small", f"research task on {len(out)} small", task)
buf = io.StringIO()
w = csv.DictWriter(buf, fieldnames=list(out[0]), lineterminator="\n")
w.writeheader()
w.writerows(out)
open(f"{G}/GEMINI_R2_T4.md", "w").write(f"""# Round 2: Gemini task 4 ({len(out)} new businesses from the last Maps discovery round)

## What to do
Same as the task 3 parts: a NEW Gemini chat, **Deep Research**, upload this file, send "Do the task in this file.",
click **Start research**, and send me the report with the others. If it ends with `LAST_ROW_DONE` before row
{out[-1]['row']}, reply "Continue with the businesses after LAST_ROW_DONE, same rules, same columns".

## The task (Gemini: follow this exactly)
{task}## Businesses ({len(out)}, in order)
```csv
{buf.getvalue()}```
""")
print(len(out), "rows;", sum(1 for t in rows if t[0] == 0), "with social")
