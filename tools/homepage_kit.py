#!/usr/bin/env python3
"""Homepage kit: one data file per prospect (output/homepage_kit/data/<id>.json) combining
- the full crawl of the firm's own site (data/fc_out*.jsonl from tools/fullcrawl.js): every page's text, headings,
  meta tags, images (URL, largest srcset entry, alt, size), background images, outbound links, tel, mailto, JSON-LD
- the Google Business Profile capture (maps): title, category text, address, phone, rating, overview, reviews
- the verified research: tier and loosened rules, owner, email, niche evidence, dated activity, original photos kept by
  the strict photo check and the coordinator's visual review, measured site defects, platform, scoring notes,
  template capture (strict tier), Gemini answers (newest review, social post dates)
- a short `digest` of the key facts for the content writer.
Usage: homepage_kit.py"""
import csv, glob, json, os, re, sys
sys.path.insert(0, "/home/user/100homeimprovementsearch/tools")
from decide import load, evaluate, jl, D, O  # noqa: E402

K = f"{O}/homepage_kit"
SOCIAL = re.compile(r"facebook\.com|instagram\.com|linkedin\.com|youtube\.com|youtu\.be|pinterest\.|houzz\.com|yelp\.com|tiktok\.com|"
                    r"twitter\.com|x\.com/|nextdoor\.com|bbb\.org|angi\.com|homeadvisor\.com|thumbtack\.com|google\.com/maps|g\.page|goo\.gl/maps", re.I)
SKIPSOC = re.compile(r"sharer|share\?|intent/|/plugins/|dialog/|/tr\?|/p/|/reel/|/posts/|/photo|/watch\?|/embed/|instagram\.com/(p|reel)$", re.I)


def last_by_id(pattern):
    out = {}
    for f in sorted(glob.glob(pattern)):
        for x in jl(f):
            out[x["id"]] = x
    return out


def main():
    d = load(); L, site, maps, br, psi, dns, man, pre = d
    crawl = last_by_id(f"{D}/fc_out*.jsonl")
    g7 = last_by_id(f"{D}/g7verify.jsonl")
    vis = last_by_id(f"{D}/g7visual.jsonl")
    tmpl = {}
    for f in sorted(glob.glob(f"{D}/template/*.jsonl")):
        for x in jl(f):
            tmpl.setdefault(x["id"], {}).update(x)
    rev = last_by_id(f"{D}/reviews_user.jsonl"); soc = last_by_id(f"{D}/social_user.jsonl")
    strict = {r["prospect_id"]: r for r in csv.DictReader(open(f"{O}/prospects100.csv"))}
    relaxed = {r["prospect_id"]: r for r in csv.DictReader(open(f"{O}/prospects100_relaxed.csv"))}
    os.makedirs(f"{K}/data", exist_ok=True)
    index = []
    for cid in list(strict) + list(relaxed):
        c, s, m, mn = L[cid], site.get(cid) or {}, maps.get(cid) or {}, man.get(cid) or {}
        row = strict.get(cid) or relaxed.get(cid)
        tier = "strict" if cid in strict else "relaxed"
        ev = evaluate(c, d)["ev"]
        cr = crawl.get(cid) or {}
        pages = [p for p in cr.get("pages", []) if not p.get("error")]
        socials = sorted({u.split("?")[0].rstrip("/") for p in pages for u in p.get("outbound", []) if SOCIAL.search(u) and not SKIPSOC.search(u)}
                         | {u.split("?")[0].rstrip("/") for u in (s.get("facebook_links") or []) + (s.get("instagram_links") or []) if not SKIPSOC.search(u)})
        tels = sorted({t for p in pages for t in p.get("tel", [])})
        mails = sorted({mt[7:].split("?")[0] for p in pages for mt in p.get("mailto", [])})
        imgs = []
        seen = set()
        for p in pages:
            for im in p.get("images", []):
                u = im.get("srcset_largest") or im.get("src")
                if u and u not in seen:
                    seen.add(u); imgs.append({"url": u, "alt": im.get("alt"), "w": im.get("w"), "h": im.get("h"), "page": p["url"]})
        originals = [k["url"] for k in (g7.get(cid) or {}).get("kept", [])]
        owner = {"name": row.get("decision_maker"), "role": row.get("decision_maker_role"),
                 "url": row.get("decision_maker_source") or row.get("decision_maker_url"), "quote": row.get("decision_maker_quote")}
        rec = {
            "id": cid, "tier": tier, "loosened": row.get("loosened", ""),
            "business_name": m.get("title") or c["name"], "website": s.get("final_url") or c.get("website"),
            "google_business_profile": {
                "url": m.get("gbp_url"), "name": m.get("title"), "address": (m.get("address") or "").replace("", "").strip(),
                "phone": (m.get("phone") or "").replace("phone:tel:", ""), "rating_label": m.get("rating_label"),
                "category_from_search": c.get("category"), "overview_text": m.get("overview"), "website_on_profile": m.get("website"),
                "reviews_captured": [{k: r.get(k) for k in ("reviewer", "when", "stars", "text", "owner")} for r in m.get("reviews") or []],
                "retrieved": m.get("retrieved"),
                "newest_review_from_gemini": rev.get(cid), "social_post_from_gemini": soc.get(cid)},
            "verified": {
                "owner": owner, "email": row.get("email"), "email_source": row.get("email_source_url") or row.get("email_url"),
                "phone": row.get("phone"), "region": row.get("region"),
                "niche_evidence": {"url": row.get("niche_evidence_url"), "quote": row.get("niche_evidence_quote")} if tier == "relaxed" else mn.get("niche_evidence"),
                "dated_activity": [x for x in (ev.get("g4_signals") or [])],
                "platform": s.get("platform"), "site_title": s.get("title"),
                "original_project_photos": originals, "photo_review": (vis.get(cid) or {}).get("note"),
                "site_defects_measured": [{"defect": x[0], "measurement": x[1]} for x in (ev.get("g8_defects") or [])],
                "pagespeed_mobile": (psi.get(cid) or {}).get("psi_score"),
                "assessment_opinion": row.get("assessment_OPINION") or mn.get("assessment"),
                "scoring_notes": {k: row.get(k) for k in row if k.startswith("score_") and k.endswith("_evidence")} if tier == "strict" else {},
                "template_capture": tmpl.get(cid)},
            "socials_found": socials, "phones_on_site": tels, "emails_on_site": mails,
            "images_on_site": imgs[:400],
            "crawl": {"start_url": cr.get("start_url"), "crawled": cr.get("crawled"), "pages": pages},
        }
        town = ""
        mm = re.search(r",\s*([^,]+),\s*([A-Z]{2})\s+\d{5}", rec["google_business_profile"]["address"])
        if mm:
            town = f"{mm[1].strip()}, {mm[2]}"
        rec["digest"] = {
            "business_name": rec["business_name"], "tier": tier, "website": rec["website"], "gbp_city": town,
            "phone": rec["google_business_profile"]["phone"] or row.get("phone"), "email": row.get("email"),
            "owner": owner.get("name"), "owner_role": owner.get("role"), "google_rating": m.get("rating_label"),
            "pages_crawled": len(pages), "images_on_site": len(imgs), "original_project_photos": len(originals),
            "socials": socials, "measured_defects": [x[0] for x in (ev.get("g8_defects") or [])]}
        json.dump(rec, open(f"{K}/data/{cid}.json", "w"), indent=1)
        index.append(rec["digest"] | {"id": cid})
    json.dump(index, open(f"{K}/index.json", "w"), indent=1)
    print("wrote", len(index), "data files;", sum(1 for x in index if x["pages_crawled"]), "with crawl")


if __name__ == "__main__":
    main()
