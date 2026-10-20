#!/usr/bin/env python3
"""Check homepage content files against the brief. Usage: validate_content.py [ids...] (default: all in content/)."""
import glob, json, os, re, sys
K = "/home/user/100homeimprovementsearch/output/homepage_kit"
KEYS = ["seo", "hero", "intro", "services", "why_choose_us", "about", "process", "gallery", "testimonials", "service_area",
        "faq", "final_cta", "footer", "schema_jsonld", "conversion_notes", "facts_used", "missing"]
BAN = re.compile(r"look no further|one-stop shop|we pride ourselves|second to none|—", re.I)


def norm(t):
    return re.sub(r"[^a-z0-9 ]", "", re.sub(r"\s+", " ", (t or "").lower())).strip()


def check(cid):
    errs = []
    c = json.load(open(f"{K}/content/{cid}.json")); d = json.load(open(f"{K}/data/{cid}.json"))
    for k in KEYS:
        if k not in c:
            errs.append(f"missing key {k}")
    raw = json.dumps(c, ensure_ascii=False)
    for m in BAN.finditer(raw):
        errs.append(f"banned: {m.group(0)}")
    t = c.get("seo", {}).get("title_tag", ""); md = c.get("seo", {}).get("meta_description", "")
    if not 35 <= len(t) <= 65: errs.append(f"title_tag length {len(t)}")
    if not 120 <= len(md) <= 165: errs.append(f"meta_description length {len(md)}")
    if len(c.get("hero", {}).get("h1", "")) > 80: errs.append("h1 too long")
    # testimonials must be verbatim from captured review text or the Gemini first words
    corpus = norm(" ".join((r.get("text") or "") for r in d["google_business_profile"]["reviews_captured"]) + " " +
                  json.dumps(d["google_business_profile"].get("newest_review_from_gemini") or {}) + " " +
                  json.dumps((d["verified"].get("template_capture") or {}).get("reviews_3") or []) + " " +
                  " ".join(p.get("text", "") for p in d["crawl"]["pages"]))
    for it in c.get("testimonials", {}).get("items", []):
        if norm(it.get("text"))[:60] not in corpus:
            errs.append(f"testimonial not verbatim: {it.get('text', '')[:50]}")
    known = {i["url"] for i in d["images_on_site"]} | set(d["verified"]["original_project_photos"]) | \
            {u for p in d["crawl"]["pages"] for u in p.get("background_images", [])} | \
            set(((d["verified"].get("template_capture") or {}).get("gallery_urls_8")) or [])
    imgs = [c.get("hero", {}).get("image", {}).get("url")] + [i.get("image", {}).get("url") for i in c.get("services", {}).get("items", [])] + \
           [i.get("url") for i in c.get("gallery", {}).get("images", [])]
    for u in imgs:
        if u and u not in known:
            errs.append(f"image not from their site: {u[:80]}")
    if not c.get("facts_used"): errs.append("facts_used empty")
    return errs


def overlap():
    paras = {}
    for f in glob.glob(f"{K}/content/*.json"):
        c = json.load(open(f)); cid = os.path.basename(f)[:-5]
        for p in c.get("intro", {}).get("paragraphs", []) + [c.get("about", {}).get("text", "")] + [x.get("a", "") for x in c.get("faq", {}).get("items", [])]:
            n = norm(p)
            if len(n) > 60:
                paras.setdefault(n, []).append(cid)
    return {k[:80]: v for k, v in paras.items() if len(set(v)) > 1}


if __name__ == "__main__":
    ids = sys.argv[1:] or [os.path.basename(f)[:-5] for f in sorted(glob.glob(f"{K}/content/*.json"))]
    bad = 0
    for i in ids:
        try:
            e = check(i)
        except Exception as ex:
            e = [f"error {type(ex).__name__}: {ex}"]
        if e:
            bad += 1; print(i, "|", "; ".join(e[:6]))
    dup = overlap()
    print(f"checked {len(ids)}, with issues {bad}, duplicated paragraphs across firms {len(dup)}")
    for k, v in list(dup.items())[:5]: print("  dup:", k, v)
