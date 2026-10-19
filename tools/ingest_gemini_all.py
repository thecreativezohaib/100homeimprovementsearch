#!/usr/bin/env python3
"""Ingest Gemini answers for output/review_requests/all/GEMINI_ALL.md.
Usage: ingest_gemini_all.py <results.csv> [<results.csv> ...]
Writes (newest file wins per id):
- data/reviews_user.jsonl  newest Google review (ISO date + first words)            -> G4 google_review
- data/social_user.jsonl   latest Facebook / Instagram post, ONLY when that account is linked from the company's
                           own site (site check facebook_links / instagram_links)   -> G4 social_post
- data/jobs_user.jsonl     dated job posting (URL + date + title)                    -> G4 job_posting
- data/hints_user.jsonl    owner name/role/source and email/source as hints for the verification agents
                           (never used as evidence until an agent or the coordinator opens the page)."""
import csv, json, re, sys
sys.path.insert(0, "/home/user/100homeimprovementsearch/tools")
from decide import jl, D  # noqa: E402

ISO = re.compile(r"^\d{4}-\d{2}-\d{2}$")
from common import rel_window  # noqa: E402
from datetime import date  # noqa: E402
UNIT = {"d": "day", "w": "week", "m": "month", "y": "year", "h": "hour"}


def as_date(v, checked):
    """ISO dates pass through; Facebook-style relative stamps ('10w', '3d', '2 weeks ago') become the EARLIEST
    possible date on the checked_on day (common.rel_window), with a note. Anything else is dropped."""
    if ISO.match(v):
        return v, ""
    m = re.match(r"^(\d+)\s*([dwmyh])$", v.strip().lower())
    rel = f"{m[1]} {UNIT[m[2]]}s ago" if m else v
    try:
        w = rel_window(rel.replace("a week ago", "1 week ago"), retrieved=date.fromisoformat(checked))
    except ValueError:
        w = None
    return (w[0].isoformat(), f" (shown as '{v}' on {checked}; earliest possible date used)") if w else ("", "")
# rows refer to firms_complete.csv (GEMINI_COMPLETE.md); pass --old for answers to GEMINI_ALL_v2.md and its addenda
FIRMS = "firms.csv" if "--old" in sys.argv else "firms_complete.csv"
sys.argv = [a for a in sys.argv if a != "--old"]
firms = {r["row"]: r for r in csv.DictReader(open(f"/home/user/100homeimprovementsearch/output/review_requests/all/{FIRMS}"))}
site = {}
for f in ("site", "site_b", "site_c", "site_d", "site_e", "site_render"):
    for x in jl(f"{D}/{f}.jsonl"):
        site[x["id"]] = x


def load(name):
    return {x["id"]: x for x in jl(f"{D}/{name}.jsonl")}


def norm_acct(u):
    u = (u or "").lower().split("?")[0].rstrip("/")
    u = re.sub(r"^https?://(www\.|m\.|web\.)?", "", u)
    return u


def val(r, k):
    v = (r.get(k) or "").strip().strip('"').strip()
    return "" if v.upper() in ("", "UNKNOWN", "N/A", "NONE") else v


reviews, social, jobs, hints = load("reviews_user"), load("social_user"), load("jobs_user"), load("hints_user")
cnt = {"rows": 0, "review": 0, "social": 0, "social_not_linked": 0, "job": 0, "hint": 0, "closed": 0}
for path in sys.argv[1:]:
    for r in csv.DictReader(open(path, encoding="utf-8-sig")):
        f = firms.get((r.get("row") or "").strip())
        if not f:
            continue
        cid = f["prospect_id"]
        cnt["rows"] += 1
        chk = val(r, "checked_on") or "UNKNOWN"
        src = f"gathered with Gemini and supplied by the user, checked_on {chk}; not opened by the coordinator"
        if "closed" in (r.get("status") or "").lower():
            cnt["closed"] += 1
            hints.setdefault(cid, {"id": cid})["gbp_closed"] = True
        (d, drel), q = as_date(val(r, "newest_review_date"), chk), val(r, "newest_review_first_words")
        if d and q:
            reviews[cid] = {"id": cid, "row": int(f["row"]), "date": d, "url": f["maps_url"], "quote": " ".join(q.split()[:15]),
                            "source": "Google Maps review data" + drel + " " + src}
            cnt["review"] += 1
        s = site.get(cid) or {}
        linked = {norm_acct(u) for u in (s.get("facebook_links") or []) + (s.get("instagram_links") or [])}
        posts = []
        for plat, uk, dk, qk in (("Facebook page", "facebook_url", "facebook_latest_post_date", "facebook_post_first_words"),
                                 ("Instagram account", "instagram_url", "instagram_latest_post_date", None)):
            u, (dd, relnote) = val(r, uk), as_date(val(r, dk), chk)
            if not (u and dd):
                continue
            if norm_acct(u) not in linked:
                cnt["social_not_linked"] += 1
                continue
            posts.append({"date": dd, "platform": plat, "account": u, "quote": " ".join(val(r, qk).split()[:12]) if qk else "",
                          "method": f"{plat} latest post date{relnote} {src}; account linked from the company's own site"})
        if posts:
            social[cid] = {"id": cid, "posts": posts}
            cnt["social"] += 1
        ju, (jd, jrel) = val(r, "job_posting_url"), as_date(val(r, "job_posting_date"), chk)
        if ju and jd:
            jobs[cid] = {"id": cid, "url": ju, "date": jd, "title": val(r, "job_title"), "source": "job posting" + jrel + " " + src}
            cnt["job"] += 1
        h = hints.setdefault(cid, {"id": cid})
        for k in ("owner_name", "owner_role", "owner_source_url", "email", "email_source_url"):
            if val(r, k):
                h[k] = val(r, k)
        if len(h) > 1:
            cnt["hint"] += 1
for name, dct in (("reviews_user", reviews), ("social_user", social), ("jobs_user", jobs), ("hints_user", hints)):
    with open(f"{D}/{name}.jsonl", "w") as fo:
        for x in dct.values():
            fo.write(json.dumps(x) + "\n")
print(cnt)
