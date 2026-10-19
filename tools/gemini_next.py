#!/usr/bin/env python3
"""Cumulative Gemini request file: output/review_requests/all/GEMINI_NEXT.md.
Adds every firm that passes all automated gates except G4 (any G7 state allowed only when PASS), has no Gemini answer yet,
and is not already listed in firms_complete.csv. New firms get the next row numbers in firms_complete.csv; the .md lists
every row that has no Gemini answer yet, so one file always holds all outstanding Gemini work.
Usage: gemini_next.py"""
import csv, io, glob, sys
sys.path.insert(0, "/home/user/100homeimprovementsearch/tools")
from decide import load, evaluate  # noqa: E402
O = "/home/user/100homeimprovementsearch/output/review_requests/all"
D = "/home/user/100homeimprovementsearch/data"
d = load(); L, site, maps, man = d[0], d[1], d[2], d[6]
fc = list(csv.DictReader(open(f"{O}/firms_complete.csv")))
listed = {r["prospect_id"] for r in fc}
answered = set()
for f in glob.glob(f"{D}/review_results/*.csv"):
    for r in csv.DictReader(open(f, encoding="utf-8-sig")):
        answered.add(r.get("row"))
disp = {l.strip() for l in open(f"{D}/dispatched.txt")}


def acct(lst):
    out = []
    for u in lst or []:
        u = u.split("?")[0].rstrip("/")
        if any(x in u for x in ("/sharer", "/share", "/intent", "/p/", "/reel", "/posts/", "/photo", "plugins", "/tr", "dialog")):
            continue
        if u.lower() not in [o.lower() for o in out]:
            out.append(u)
    return " ".join(out[:2]) or "none"


new = []
for cid, c in L.items():
    s, m = site.get(cid), maps.get(cid)
    if cid in listed or cid in man or cid in disp or not s or not m or not m.get("title") or c.get("dup_of"):
        continue
    ev = evaluate(c, d); g = ev["gates"]
    if ev.get("niche") == "FAIL" or g.get("G4") == "PASS" or g.get("G2") != "PASS":
        continue
    if [k for k, v in g.items() if v == "FAIL" and k != "G4"]:
        continue
    new.append((cid, c, s, m))
start = max(int(r["row"]) for r in fc) + 1
with open(f"{O}/firms_complete.csv", "a", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(fc[0].keys()))
    for i, (cid, c, s, m) in enumerate(new):
        w.writerow({"row": start + i, "priority": "NEXT", "prospect_id": cid, "business_name": m.get("title") or c["name"],
                    "address": (m.get("address") or "").replace("", "").strip(),
                    "phone": (m.get("phone") or "").replace("phone:tel:", ""), "website": s["final_url"],
                    "maps_url": m.get("gbp_url"), "have_already": "none"})
fc = list(csv.DictReader(open(f"{O}/firms_complete.csv")))
buf = io.StringIO(); w = csv.writer(buf, lineterminator="\n")
w.writerow(["row", "business_name", "address", "website", "maps_url", "facebook", "instagram"])
n = 0
for r in fc:
    if r["row"] in answered or r["priority"] != "NEXT":
        continue
    c = L.get(r["prospect_id"])
    if c:  # drop firms that have since failed another gate (e.g. G9 after the browser run)
        ev = evaluate(c, d)
        if ev.get("niche") == "FAIL" or [k for k, v in ev["gates"].items() if v == "FAIL" and k != "G4"] or ev["gates"].get("G4") == "PASS":
            continue
    s = site.get(r["prospect_id"]) or {}
    w.writerow([r["row"], r["business_name"], r["address"], r["website"], r["maps_url"], acct(s.get("facebook_links")), acct(s.get("instagram_links"))])
    n += 1
prompt = open(f"{O}/gemini_parallel/GEMINI_A.md").read().split("## Prompt")[1].split("## Companies")[0]
open(f"{O}/GEMINI_NEXT.md", "w").write(
    f"# Remodel 100: Gemini file NEXT ({n} firms, all outstanding)\n\nThis one file always holds every firm still waiting for Gemini. "
    f"It is rebuilt as new firms qualify, so download the newest copy each time. Split it across several Gemini chats if it is long "
    f"(about 100 rows per chat).\n\n## Prompt{prompt}## Companies\n```csv\n{buf.getvalue()}```\n")
print("added", len(new), "outstanding", n)
