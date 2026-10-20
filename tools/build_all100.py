#!/usr/bin/env python3
"""Combine the homepage kit into single files.
- output/homepage_kit/ALL_100.json: every business, the full data record (crawl of every page, images, socials,
  Google Business Profile, verified research) plus its homepage content.
- output/homepage_kit/ALL_100_content.json: the lighter file for a page builder, digest plus homepage content.
- output/homepage_kit/ALL_100_content.md: the same copy as readable text, one section per business.
Usage: build_all100.py"""
import json, os, sys

K = "/home/user/100homeimprovementsearch/output/homepage_kit"


def md_block(c):
    h, out = c["hero"], []
    out.append(f"## {c['business_name']} ({c['id']})\n")
    out.append(f"- Title tag: {c['seo']['title_tag']}\n- Meta description: {c['seo']['meta_description']}")
    out.append(f"- Primary keyword: {c['seo']['primary_keyword']}\n")
    out.append(f"### Hero\n{h.get('eyebrow', '')}\n\n**{h['h1']}**\n\n{h.get('subheadline', '')}\n")
    for key in ("intro", "about", "service_area"):
        sec = c.get(key) or {}
        paras = sec.get("paragraphs") or ([sec["paragraph"]] if sec.get("paragraph") else [])
        out.append(f"### {sec.get('h2', key)}\n" + "\n\n".join(paras) + "\n")
    sv = c.get("services") or {}
    items = sv.get("items", sv) if isinstance(sv, dict) else sv
    out.append(f"### {sv.get('h2', 'Services') if isinstance(sv, dict) else 'Services'}")
    for s in items:
        out.append(f"- **{s.get('name') or s.get('title')}**: {s.get('blurb') or s.get('text')}")
    fq = c.get("faq") or {}
    out.append(f"\n### {fq.get('h2', 'FAQ') if isinstance(fq, dict) else 'FAQ'}")
    for q in (fq.get("items", []) if isinstance(fq, dict) else fq):
        out.append(f"- **{q.get('q') or q.get('question')}** {q.get('a') or q.get('answer')}")
    out.append("\n---\n")
    return "\n".join(out)


def main():
    index = json.load(open(f"{K}/index.json"))
    full, light, md, missing = [], [], ["# Homepage content for 100 businesses\n"], []
    for d in index:
        cid = d["id"]
        data = json.load(open(f"{K}/data/{cid}.json"))
        p = f"{K}/content/{cid}.json"
        content = json.load(open(p)) if os.path.exists(p) else None
        if content is None:
            missing.append(cid)
        full.append(data | {"homepage_content": content})
        light.append({"id": cid, "tier": data["tier"], "website": data["website"], "digest": data["digest"],
                      "google_business_profile": {k: v for k, v in data["google_business_profile"].items() if k != "reviews_captured"},
                      "socials": data["socials_found"], "original_project_photos": data["verified"]["original_project_photos"],
                      "homepage_content": content})
        if content:
            md.append(md_block(content))
    json.dump(full, open(f"{K}/ALL_100.json", "w"), indent=1)
    json.dump(light, open(f"{K}/ALL_100_content.json", "w"), indent=1)
    open(f"{K}/ALL_100_content.md", "w").write("\n".join(md))
    print("businesses", len(full), "with content", len(full) - len(missing), "missing", missing)


if __name__ == "__main__":
    sys.exit(main())
