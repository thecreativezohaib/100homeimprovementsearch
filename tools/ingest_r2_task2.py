#!/usr/bin/env python3
"""Merge every Gemini task 2 report (PDF-parsed CSVs and pasted report text) into data/r2/task2_all.csv, record which
task 2 rows Gemini researched (a CSV line or a NOTHING_FOUND entry), and list the rows still to do in task 2 order.
Later reports win for a row that appears twice. Usage: ingest_r2_task2.py"""
import csv, glob, io, json, re

D = "/home/user/100homeimprovementsearch/data/r2"
G = "/home/user/100homeimprovementsearch/output/round2/gemini"
HEAD = ("row,business_name,facebook_url,instagram_url,email,email_source_url,email_source_quote,website_found,"
        "website_status,owner_name,facebook_followers,facebook_latest_post_date,instagram_followers,"
        "instagram_latest_post_date,photo_posts,sources_checked,notes").split(",")
recs, researched = {}, set()


def add(fields):
    if len(fields) < 15 or not fields[0].strip().isdigit():
        return
    fields = (fields + [""] * 17)[:17] if len(fields) <= 17 else fields[:16] + [",".join(fields[16:])]
    r = dict(zip(HEAD, [f.strip() for f in fields]))
    recs[r["row"]] = r
    researched.add(r["row"])


# PDF exports already rebuilt into CSV
for f in sorted(glob.glob(f"{D}/gemini_in/task2_r*.csv")):
    for fields in list(csv.reader(open(f)))[1:]:
        add(fields)
    raw = open(f.replace(".csv", "_raw.txt")).read()
    for m in re.finditer(r"NOTHING_FOUND:([\d,\s]+)", raw):
        researched |= set(re.findall(r"\d+", m.group(1)))

# pasted report text: CSV lines follow a header that may share a line with prose ("Code snippetrow,business_name,...")
for f in sorted(glob.glob(f"{D}/gemini_in/task2_batch*_paste.txt")):
    on = False
    for line in open(f).read().replace("​", "").split("\n"):
        if "row,business_name,facebook_url" in line:
            on = True
            continue
        if on and re.match(r"\s*\d+,", line):
            add(next(csv.reader(io.StringIO(line.strip()))))
        if "NOTHING_FOUND" in line:
            on = False
            m = re.search(r"NOTHING_FOUND:([\d,\s]*?)(?:LAST_ROW_DONE|$)", line)
            if m:
                researched |= set(re.findall(r"\d+", m.group(1)))

with open(f"{D}/task2_all.csv", "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=HEAD)
    w.writeheader()
    for k in sorted(recs, key=int):
        w.writerow(recs[k])

order = [r["row"] for r in csv.DictReader(io.StringIO(open(f"{G}/GEMINI_R2_TASK2.md").read().split("```csv\n")[-1].split("```")[0]))]
left = [r for r in order if r not in researched]
json.dump({"researched": sorted(researched, key=int), "left": left}, open(f"{D}/task2_progress.json", "w"))
print("records", len(recs), "researched", len(researched & set(order)), "of", len(order), "left", len(left))
