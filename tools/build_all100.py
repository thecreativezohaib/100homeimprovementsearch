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
    """One business as readable text, every section in template order."""
    def items(sec, key):
        return (sec or {}).get(key, []) if isinstance(sec, dict) else (sec or [])
    h, o = c["hero"], []
    o.append(f"## {c['business_name']} ({c['id']})\n")
    o.append(f"- Title tag: {c['seo']['title_tag']}\n- Meta description: {c['seo']['meta_description']}")
    o.append(f"- Primary keyword: {c['seo']['primary_keyword']}\n- Secondary keywords: {', '.join(c['seo'].get('secondary_keywords', []))}\n")
    o.append(f"### Hero\n_{h.get('eyebrow', '')}_\n\n# {h['h1']}\n\n{h.get('subheadline', '')}\n")
    o.append(f"Buttons: {h['primary_cta']['label']} | {h['secondary_cta']['label']}  ")
    o.append("Trust badges: " + " / ".join(h.get("trust_badges", [])))
    o.append(f"Hero image: {(h.get('image') or {}).get('url')} (alt: {(h.get('image') or {}).get('alt')})\n")
    o.append(f"### {c['intro']['h2']}\n" + "\n\n".join(c["intro"].get("paragraphs", [])) + "\n")
    o.append(f"### {c['services']['h2']}")
    o += [f"- **{x['name']}**: {x['blurb']}" for x in items(c["services"], "items")]
    o.append(f"\n### {c['why_choose_us']['h2']}")
    o += [f"- **{x['title']}**: {x['text']}" for x in items(c["why_choose_us"], "items")]
    ab = c["about"]
    o.append(f"\n### {ab['h2']}\n{ab.get('text', '')}\n\n({ab.get('owner_name')}, {ab.get('owner_role')})\n")
    o.append(f"### {c['process']['h2']}")
    o += [f"{n}. **{x['title']}**: {x['text']}" for n, x in enumerate(items(c["process"], "steps"), 1)]
    o.append(f"\n### {c['gallery']['h2']}")
    o += [f"- {x['url']} | {x.get('alt')} | {x.get('caption', '')}" for x in items(c["gallery"], "images")]
    o.append(f"\n### {c['testimonials']['h2']}")
    o += [f"> {x['text']}\n> {x['name']}, {x.get('source')}\n" for x in items(c["testimonials"], "items")]
    sa = c["service_area"]
    o.append(f"### {sa['h2']}\n{sa.get('text', '')}\n\nTowns: {', '.join(sa.get('towns', []))}\n")
    o.append(f"### {c['faq']['h2']}")
    o += [f"- **{x['q']}** {x['a']}" for x in items(c["faq"], "items")]
    fc, ft = c["final_cta"], c["footer"]
    o.append(f"\n### {fc['h2']}\n{fc.get('text', '')}\n\nButton: {fc['button']['label']} ({fc['button']['href']})\n")
    o.append("Footer: " + " | ".join(str(ft.get(k) or f"no {k} listed") for k in ("name", "address", "phone", "email", "hours")) + "  ")
    o.append("Socials: " + ", ".join(ft.get("socials") or []) + "\n")
    cn = c.get("conversion_notes")
    if isinstance(cn, dict):
        o.append("**Conversion notes (not for the page)**")
        for k, v in cn.items():
            o.append(f"- {k}: " + ("; ".join(v) if isinstance(v, list) else str(v)))
    o.append("\n**Missing (left out, not invented):** " + "; ".join(c.get("missing", [])))
    o.append("\n---\n")
    return "\n".join(o)


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
