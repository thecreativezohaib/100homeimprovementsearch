#!/usr/bin/env python3
"""Assemble the design reference pack (output/design_refs/pack) from the visual reviews.
Inputs: data/design_review_*.json (site reviews and section crops), data/design_concepts.json (gallery concepts and
extra live sites), captures in output/design_refs/raw*/ (newest capture of a site wins), and
output/design_refs/DIRECTION.md (the written design direction, placed at the top of the guide).
Outputs in output/design_refs/pack/:
  sites/NN_<id>/   desktop, tablet and mobile full pages plus on-screen shots, for each kept site ranked by score
  sections/<section>/  the best section crops (written by the reviewers)
  concepts/        the best gallery concepts (written by the concept curator)
  DESIGN_REFERENCES.md  the guide for the designer (direction, ranked sites with notes, section index, concept index)
  index.html       a visual gallery of everything, opened locally in a browser
Usage: build_design_pack.py"""
import glob, html, json, os, shutil
from PIL import Image

Image.MAX_IMAGE_PIXELS = None
R = "/home/user/100homeimprovementsearch"
P = f"{R}/output/design_refs/pack"
SECTION_ORDER = ["header_nav", "hero", "trust_bar", "services", "projects_gallery", "before_after", "testimonials",
                 "process", "about_owner", "stats", "service_area", "faq", "cta_band", "contact_form", "footer",
                 "mobile_sticky_cta", "mobile_menu_or_header"]
SHOTS = ["desktop_screen1", "desktop_screen2_scrolled", "desktop_full", "tablet_full", "mobile_screen1",
         "mobile_screen2_scrolled", "mobile_full"]


# sites whose stitched recapture came out worse than the first capture (reviewer's call)
PREFER = {"crdesignremodel_com": "raw2", "watermarkdesignbuild_com": "raw2"}


def raw_file(cid, shot):
    if cid in PREFER and os.path.exists(f"{R}/output/design_refs/{PREFER[cid]}/{cid}__{shot}.jpg"):
        return f"{R}/output/design_refs/{PREFER[cid]}/{cid}__{shot}.jpg"
    found = sorted(glob.glob(f"{R}/output/design_refs/raw*/{cid}__{shot}.jpg"), key=os.path.getmtime)
    return found[-1] if found else None


def copy_shot(src, dst, max_h=16000):
    im = Image.open(src).convert("RGB")
    if im.height > max_h:
        im = im.crop((0, 0, im.width, max_h))
    im.save(dst, quality=74, optimize=True)


def rel(path):
    return os.path.relpath(path, P)


def main():
    reviews = []
    for f in sorted(glob.glob(f"{R}/data/design_review_*.json")):
        reviews += json.load(open(f))
    best = {}
    for r in reviews:  # a site reviewed twice keeps its later review
        best[r["id"]] = r
    kept = sorted([r for r in best.values() if r.get("verdict") == "keep"], key=lambda r: -float(r.get("score") or 0))
    conc = json.load(open(f"{R}/data/design_concepts.json")) if os.path.exists(f"{R}/data/design_concepts.json") else {"concepts": []}

    if os.path.isdir(f"{P}/sites"):
        shutil.rmtree(f"{P}/sites")
    site_dirs = {}
    for n, r in enumerate(kept, 1):
        d = f"{P}/sites/{n:02d}_{r['id']}"
        os.makedirs(d)
        for s in SHOTS:
            src = raw_file(r["id"], s)
            if src:
                copy_shot(src, f"{d}/{s}.jpg")
        site_dirs[r["id"]] = d

    sections = {}
    for r in best.values():
        for s in r.get("sections", []):
            if s.get("file") and os.path.exists(s["file"]):
                sections.setdefault(s["section"], []).append(s | {"id": r["id"], "url": r["url"]})
    concepts = [c for c in conc.get("concepts", []) if os.path.exists(c["file"] if c["file"].startswith("/") else f"{P}/concepts/{os.path.basename(c['file'])}")]

    direction = open(f"{R}/output/design_refs/DIRECTION.md").read() if os.path.exists(f"{R}/output/design_refs/DIRECTION.md") else ""
    md = [direction, "\n## Full-site references, best first\n",
          "Each folder in `sites/` has the same page at three widths: `desktop_full.jpg` (1440 px), `tablet_full.jpg` "
          "(820 px) and `mobile_full.jpg` (390 px at 2x), plus on-screen shots: `*_screen1.jpg` is the first screen a "
          "visitor sees and `*_screen2_scrolled.jpg` is after scrolling (shows sticky headers and call bars).\n"]
    for n, r in enumerate(kept, 1):
        md.append(f"### {n}. {r['id'].replace('_', '.')} ({r['score']}/10): {r.get('style', '')}")
        md.append(f"- Live site: {r['url']}\n- Folder: `{rel(site_dirs[r['id']])}/`")
        md.append(f"- Palette: {r.get('palette', '')}. Type: {r.get('typography', '')}")
        md.append("- Borrow: " + "; ".join(r.get("what_to_borrow", [])))
        md.append("- Conversion: " + "; ".join(r.get("conversion_patterns", [])))
        md.append(f"- Mobile: {r.get('mobile_notes', '')}")
        if r.get("weaknesses"):
            md.append("- Avoid: " + "; ".join(r["weaknesses"]))
        md.append("")
    md.append("\n## Section-by-section examples\n")
    md.append("Each crop shows one section cut from a live site. Desktop crops are 1440 px wide; mobile crops are 780 px "
              "(390 px screen at 2x).\n")
    for sec in SECTION_ORDER + sorted(set(sections) - set(SECTION_ORDER)):
        if sec not in sections:
            continue
        md.append(f"### {sec.replace('_', ' ').title()}")
        for s in sections[sec]:
            md.append(f"- `{rel(s['file'])}` ({s['id'].replace('_', '.')}, {s['device']}): {s.get('why', '')}")
        md.append("")
    if concepts:
        md.append("\n## Concept designs from Dribbble, Behance, Pinterest and other galleries\n")
        md.append("Design concepts, not live sites: use them for look and layout ideas. Each links to its source page.\n")
        for c in concepts:
            f = c["file"] if c["file"].startswith("/") else f"{P}/concepts/{os.path.basename(c['file'])}"
            md.append(f"- `{rel(f)}` ({c.get('source')}, {c.get('type')}{', has mobile view' if c.get('has_mobile_view') else ''}): "
                      f"{c.get('style', '')}. Borrow: {'; '.join(c.get('what_to_borrow', []))}. Source: {c.get('source_url')}"
                      + (f" by {c['designer']}" if c.get("designer") else ""))
    open(f"{P}/DESIGN_REFERENCES.md", "w").write("\n".join(md) + "\n")

    # visual gallery
    h = ["<!doctype html><meta charset=utf-8><meta name=viewport content='width=device-width,initial-scale=1'>",
         "<title>Design References</title><style>body{font:15px/1.5 system-ui,sans-serif;margin:0;padding:24px;background:#f6f5f2;color:#1d1d1b}",
         "h1{font-size:28px}h2{margin-top:48px;border-top:1px solid #ccc;padding-top:24px}h3{margin:28px 0 6px}",
         ".row{display:flex;gap:16px;align-items:flex-start;overflow-x:auto}.row a img{display:block;border:1px solid #ddd;background:#fff}",
         ".d img{width:560px}.t img{width:260px}.m img{width:180px}.sec img{max-width:100%;width:720px}.secm img{width:260px}",
         ".note{max-width:900px;color:#444}.cap{font-size:12px;color:#666}@media(max-width:700px){.d img{width:320px}.sec img{width:100%}}</style>",
         "<h1>Design references: premium remodeling homepage</h1><p class=note>Open any image to see it full size. "
         "Guide: DESIGN_REFERENCES.md</p><h2>Full sites (desktop, tablet, mobile)</h2>"]
    for n, r in enumerate(kept, 1):
        d = site_dirs[r["id"]]
        h.append(f"<h3>{n}. {html.escape(r['id'].replace('_', '.'))} ({r['score']}/10) <span class=cap>{html.escape(r.get('style', ''))}</span></h3>")
        h.append(f"<p class=note>{html.escape('; '.join(r.get('what_to_borrow', [])[:4]))}</p><div class=row>")
        for s, cls in (("desktop_full", "d"), ("tablet_full", "t"), ("mobile_full", "m"), ("mobile_screen2_scrolled", "m")):
            if os.path.exists(f"{d}/{s}.jpg"):
                h.append(f"<a class={cls} href='{rel(d)}/{s}.jpg'><img loading=lazy src='{rel(d)}/{s}.jpg' alt='{s}'></a>")
        h.append("</div>")
    h.append("<h2>Sections</h2>")
    for sec in SECTION_ORDER + sorted(set(sections) - set(SECTION_ORDER)):
        if sec not in sections:
            continue
        h.append(f"<h3>{sec.replace('_', ' ').title()}</h3><div class=row>")
        for s in sections[sec]:
            cls = "secm" if s["device"] == "mobile" else "sec"
            h.append(f"<a class={cls} href='{rel(s['file'])}' title='{html.escape(s.get('why', ''))}'><img loading=lazy src='{rel(s['file'])}'></a>")
        h.append("</div>")
    if concepts:
        h.append("<h2>Concepts (Dribbble, Behance, Pinterest and more)</h2><div class=row style='flex-wrap:wrap'>")
        for c in concepts:
            f = rel(c["file"] if c["file"].startswith("/") else f"{P}/concepts/{os.path.basename(c['file'])}")
            h.append(f"<a class=t href='{f}' title='{html.escape(c.get('style', ''))}'><img loading=lazy src='{f}' style='width:340px'></a>")
        h.append("</div>")
    open(f"{P}/index.html", "w").write("\n".join(h))
    print("kept sites", len(kept), "sections", sum(len(v) for v in sections.values()), "concepts", len(concepts))


if __name__ == "__main__":
    main()
