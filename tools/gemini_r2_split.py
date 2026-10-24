#!/usr/bin/env python3
"""Split the rows of GEMINI_R2_TASK2.md that Gemini has not reached into parallel files of N businesses, one per
Gemini chat: output/round2/gemini/task2_parts/GEMINI_R2_T2_partNN.md, plus a zip of all parts.
Each part keeps the task 2 prompt, with its own count and without the A and B row instructions it does not need.
Usage: gemini_r2_split.py <last_row_done> [per_part=100]"""
import csv, io, math, os, re, sys, zipfile

R = "/home/user/100homeimprovementsearch"
G = f"{R}/output/round2/gemini"
last, per = sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else 100
src = open(f"{G}/GEMINI_R2_TASK2.md").read()
prompt = src.split("## The task (Gemini: follow this exactly)\n")[1].split("## Businesses")[0]
table = src.split("```csv\n")[-1].split("```")[0]
rows = list(csv.DictReader(io.StringIO(table)))
start = next(i for i, r in enumerate(rows) if r["row"] == last) + 1
todo = rows[start:]
parts = math.ceil(len(todo) / per)
out = f"{G}/task2_parts"
os.makedirs(out, exist_ok=True)
# the A and B instructions only apply to rows already done
p = re.sub(r"- A \(\d+ rows\).*?- C \(\d+ rows\): new businesses\. Do all the checks below\.\n- D \(\d+ rows\): new to you as well\. Do all the checks below\.",
           "- C and D: new businesses. Do all the checks below for every one.", prompt, flags=re.S)
p = p.replace('The "task" column tells you what each row needs most:', 'The "task" column:')
names = []
for k in range(parts):
    chunk = todo[k * per:(k + 1) * per]
    buf = io.StringIO()
    w = csv.DictWriter(buf, fieldnames=list(chunk[0]), lineterminator="\n")
    w.writeheader()
    w.writerows(chunk)
    body = re.sub(r"long research task on \d+ small", f"long research task on {len(chunk)} small", p)
    md = f"""# Round 2: Gemini task 2, part {k + 1:02d} of {parts:02d} ({len(chunk)} businesses, rows {chunk[0]['row']} to {chunk[-1]['row']})

## What to do
1. Open a NEW Gemini chat for this part, pick **Deep Research** (or **Agent**), upload this file and send
   "Do the task in this file." Then click **Start research**.
2. You can run all parts at the same time, each in its own chat.
3. When a chat finishes, export the report (PDF or Docs) and keep it. Send me all reports together.
4. Only if a report ends with `LAST_ROW_DONE: <row>` before row {chunk[-1]['row']}: reply in that chat "Continue with
   the businesses after LAST_ROW_DONE, same rules, same columns" and keep that report too.

## The task (Gemini: follow this exactly)
{body}## Businesses ({len(chunk)}, in order)
```csv
{buf.getvalue()}```
"""
    name = f"GEMINI_R2_T2_part{k + 1:02d}.md"
    open(f"{out}/{name}", "w").write(md)
    names.append(name)
with zipfile.ZipFile(f"{G}/GEMINI_R2_T2_parts.zip", "w", zipfile.ZIP_DEFLATED) as z:
    for n in names:
        z.write(f"{out}/{n}", n)
print(len(todo), "rows in", parts, "parts")
