#!/usr/bin/env python3
"""Round 2 finalists: vetted passes plus the "check" rows accepted on review, minus rejects, with a free extra website
check (the obvious domains for the business name, e.g. reelandsons.com / reelandsonsllc.com, must not load a live
site of the business) and the Google profile facts for ranking. Writes data/r2/finalists.json, ranked.
Usage: r2_finalists.py"""
import json, re, sys, concurrent.futures as cf
sys.path.insert(0, "/home/user/100homeimprovementsearch/tools")
D = "/home/user/100homeimprovementsearch/data/r2"
exec(open("/home/user/100homeimprovementsearch/tools/r2_vet.py").read().split("rows = []")[0])  # live(), helpers

# "check" rows reviewed by hand: the social link is a numeric id, a short handle or the email shares the owner's
# other trade name, and Gemini matched it by phone or owner
ACCEPT = {"1405", "1592", "1640", "1667", "1699", "1905", "2324", "1086", "1740", "2219", "2297", "50", "356", "17",
          "581", "1121", "1169", "1340", "2122", "2229", "202"}
# rejected on review: email belongs to another business or person, social account of an unrelated business, duplicate
REJECT = {"1766": "email domain newsdrm.com is unrelated", "2375": "email is a family member's art address",
          "1569": "Facebook page is The Bargain Club", "1858": "Instagram glccabinet does not match",
          "2030": "Facebook page is Kitchens Plus SD", "163": "duplicate of row 1340"}
V = json.load(open(f"{D}/vetted.json"))
keep = [x for x in V if (x["status"] == "pass" or x["row"] in ACCEPT) and x["row"] not in REJECT]

maps = {}
for f in ("gateA.json", "gateB.json"):
    for g in json.load(open(f"{D}/{f}")):
        maps[g["id"]] = g
rowmap = json.load(open(f"{D}/gemini_rowmap.json")) | json.load(open(f"{D}/gemini_rowmap_b.json"))


def guesses(name):
    base = re.sub(r"\b(llc|inc|co|corp|l\.l\.c|company)\b\.?", "", name.lower())
    base = re.sub(r"[^a-z0-9& ]", "", base.split("|")[0].split(" - ")[0]).replace("&", "and")
    s = re.sub(r"\s+", "", base)
    return {f"{s}.com", f"{s}llc.com", f"{s.replace('and', '')}.com"} if len(s) > 5 else set()


def site_guess(x):
    for d in guesses(x["business_name"]):
        if live(d):
            return d
    return ""


with cf.ThreadPoolExecutor(12) as ex:
    hits = list(ex.map(site_guess, keep))
out = []
for x, h in zip(keep, hits):
    g = maps.get(rowmap.get(x["row"]), {})
    rv = g.get("reviews_count")
    if rv is None:
        m = re.search(r"\(([\d,]+)\)", g.get("rating_label") or "")
        rv = int(m.group(1).replace(",", "")) if m else 0
    out.append({**x, "guessed_live_site": h, "maps_id": rowmap.get(x["row"]), "maps_url": g.get("maps_url"),
                "title": g.get("title"), "category": g.get("category"), "phone": g.get("phone"),
                "address": (g.get("address") or "").replace("", "").strip(), "rating_label": g.get("rating_label"),
                "reviews_count": rv})
# guessed domains that loaded were opened in a browser: only these show the same business (its town or phone);
# the rest belong to other companies or are "under construction" / "coming soon" pages
SAME_SITE = {"2248", "1823", "1235", "1342", "213", "1376"}
fin = [o for o in out if o["row"] not in SAME_SITE]
fin.sort(key=lambda o: (o["source_check"] != "verified", o["origin"] != "qualified34", -(o["reviews_count"] or 0)))
json.dump(fin, open(f"{D}/finalists.json", "w"), indent=1)
print("kept", len(keep), "guessed live site", [(o["row"], o["guessed_live_site"]) for o in out if o["guessed_live_site"]], "finalists", len(fin))
