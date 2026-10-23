#!/usr/bin/env python3
"""Turn google_social.js output into confirmed social links: resolve Google's /goto redirect links for results whose
snippet shows Facebook or Instagram, keep page or profile URLs (not posts), and keep the snippet text (it often holds
the Facebook Intro, follower counts and an email).
Usage: resolve_social.py <google_social out.jsonl> <resolved.jsonl>"""
import json, re, sys, concurrent.futures as cf
import requests

UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/141 Safari/537.36"}
FB = re.compile(r"https://(?:www\.|m\.)?facebook\.com/(?!sharer|groups/|events/|watch|share|photo|story\.php|permalink\.php|reel/|posts/)[^?#\s]+", re.I)
IG = re.compile(r"https://(?:www\.)?instagram\.com/(?!p/|reel/|reels/|explore/|stories/)[A-Za-z0-9._]+/?", re.I)


def resolve(u):
    if "google.com/goto" not in u and "google.com/url" not in u:
        return u
    try:
        r = requests.get(u, headers=UA, timeout=20, allow_redirects=False)
        return r.headers.get("location") or u
    except Exception:
        return u


def main(inp, out):
    recs = [json.loads(l) for l in open(inp)]
    jobs = []
    for r in recs:
        for k, v in r["queries"].items():
            for x in v.get("results") or []:
                if re.search(r"facebook|instagram", x["snippet"] + x["title"], re.I):
                    jobs.append(x)
    with cf.ThreadPoolExecutor(12) as ex:
        for x, u in zip(jobs, ex.map(lambda x: resolve(x["url"]), jobs)):
            x["resolved"] = u
    with open(out, "w") as f:
        for r in recs:
            res = [x for v in r["queries"].values() for x in v.get("results") or []]
            fb, ig = {}, {}
            for x in res:
                u = x.get("resolved") or ""
                m = FB.match(u)
                if m:
                    fb.setdefault(m.group(0).rstrip("/"), x["snippet"])
                m = IG.match(u)
                if m:
                    ig.setdefault(m.group(0).rstrip("/"), x["snippet"])
            r2 = {"id": r["id"], "name": r["name"], "facebook": fb, "instagram": ig, "emails_in_snippets": r.get("emails", []),
                  "email_snippets": [x["snippet"] for x in res if re.search(r"@[A-Za-z0-9-]+\.", x["snippet"])][:6],
                  "blocked": any(v.get("blocked") for v in r["queries"].values())}
            f.write(json.dumps(r2) + "\n")
    print(len(recs), "records;", sum(1 for l in open(out) if json.loads(l)["facebook"]), "with Facebook")


if __name__ == "__main__":
    main(*sys.argv[1:3])
