#!/usr/bin/env python3
"""Outreach base: one record per live homepage concept with every contact channel found in our data.
Sources: output/homepage_kit/data/<id>.json (Google profile, crawl of their site, verified owner and email) and
content/<id>.json (conversion notes). WhatsApp is recorded only when their own site links to wa.me / WhatsApp.
Usage: outreach_base.py <concept_map.json> <out.json>"""
import json, re, sys
from urllib.parse import unquote, urlparse

K = "/home/user/100homeimprovementsearch/output/homepage_kit"
JUNK = re.compile(r"pearlmx|google\.com/maps/search$|sharer|/share|intent/|wix\.com|squarespace|godaddy|elfsight|facebook\.com/?$|instagram\.com/?$|"
                  r"facebook\.com/(tr|plugins|dialog|photo|events|groups|watch|sharer|share)|/posts/|/videos/|instagram\.com/(p|reel|reels|tv|explore|stories)/|instagram\.com/(p|reel)$|youtube\.com/(watch|embed|shorts)|bbb\.org/?$|bbb\.org/?#|houzz\.com/?$", re.I)
FREE = {"gmail.com", "yahoo.com", "outlook.com", "hotmail.com", "aol.com", "icloud.com", "comcast.net", "att.net", "msn.com", "live.com", "me.com", "verizon.net", "sbcglobal.net", "bellsouth.net"}
EMAIL_JUNK = re.compile(r"example\.|sentry|wixpress|godaddy|domain\.com|yourname|email@|@mysite\.com|\.(png|jpg|webp)$", re.I)


def phone_fmt(p):
    d = re.sub(r"\D", "", p or "")
    d = d[1:] if len(d) == 11 and d.startswith("1") else d
    return f"({d[:3]}) {d[3:6]}-{d[6:]}" if len(d) == 10 else None


def main(cmap, out):
    rows = []
    for m in json.load(open(cmap)):
        d = json.load(open(f"{K}/data/{m['id']}.json")); c = json.load(open(f"{K}/content/{m['id']}.json"))
        g, v = d["google_business_profile"], d["verified"]
        links = {u.split("?")[0].rstrip("/") for p in d["crawl"]["pages"] for u in p.get("outbound", [])} | set(d.get("socials_found") or [])
        wa = sorted({u for u in links if re.search(r"wa\.me|whatsapp", u, re.I)})
        soc = {k: sorted({u for u in links if re.search(rx, u, re.I) and not JUNK.search(u)})
               for k, rx in {"facebook": r"facebook\.com/", "instagram": r"instagram\.com/", "linkedin": r"linkedin\.com/",
                             "youtube": r"youtube\.com/|youtu\.be", "houzz": r"houzz\.com/", "tiktok": r"tiktok\.com/",
                             "x_twitter": r"(twitter|x)\.com/", "yelp": r"yelp\.com/biz", "nextdoor": r"nextdoor\.com/",
                             "bbb": r"bbb\.org/.+", "angi": r"angi\.com/|homeadvisor\.com/", "pinterest": r"pinterest\.com/"}.items()}
        phones = []
        for p in [g.get("phone"), (c.get("footer") or {}).get("phone")] + list(d.get("phones_on_site") or []):
            f = phone_fmt(p)
            if f and f not in phones:
                phones.append(f)
        # keep only the firm's own addresses: its site domain, a domain it uses for mail elsewhere on its site, or free mail
        site_dom = re.sub(r"^www\.", "", urlparse(d["website"]).netloc.lower())
        brand = re.sub(r"[^a-z]", "", site_dom.split(".")[0])[:6]
        emails = []
        # the verified address's domain is theirs even when it differs from the website
        mail_doms = {unquote(v.get("email") or "").lower().split("@")[-1]} - {""}
        for e in [v.get("email")] + list(d.get("emails_on_site") or []):
            e = unquote(e or "").strip().lower().strip(".")
            dom = e.split("@")[-1]
            ok_dom = dom in mail_doms or dom == site_dom or dom.endswith("." + site_dom) or dom in FREE or (brand and brand in re.sub(r"[^a-z]", "", dom))
            if e and "@" in e and " " not in e and not EMAIL_JUNK.search(e) and ok_dom and e not in emails:
                emails.append(e)
        owner = v.get("owner") or {}
        pages = [p["url"] for p in d["crawl"]["pages"]]
        contact = next((u for u in pages if re.search(r"contact|get-started|estimate|consult|schedule|quote", u, re.I)), None)
        cn = c.get("conversion_notes") or {}
        rows.append({
            "n": m["n"], "id": m["id"], "business_name": c.get("business_name") or d["business_name"],
            "old_site": d["website"], "new_concept": m["concept"],
            "owner": owner.get("name"), "owner_role": owner.get("role"),
            "google_phone": phone_fmt(g.get("phone")), "all_phones": phones,
            "whatsapp_links_on_site": wa, "emails": emails, "verified_email": (v.get("email") or "").lower() or None,
            "email_source": v.get("email_source"), "contact_form_url": contact, "address": (c.get("footer") or {}).get("address") or g.get("address"),
            "google_profile": g.get("url"), "google_rating": (g.get("rating_label") or "").replace("\n", " "),
            "socials": {k: x for k, x in soc.items() if x},
            "primary_keyword": c["seo"]["primary_keyword"], "pagespeed_mobile": v.get("pagespeed_mobile"),
            "measured_defects": [x["defect"] + ": " + x["measurement"] for x in v.get("site_defects_measured") or []],
            "conversion_notes": cn,
        })
    json.dump(rows, open(out, "w"), indent=1)
    print(len(rows), "rows;", sum(1 for r in rows if r["emails"]), "with email;", sum(1 for r in rows if r["whatsapp_links_on_site"]), "with WhatsApp link;",
          sum(1 for r in rows if r["socials"].get("facebook")), "with Facebook;", sum(1 for r in rows if r["socials"].get("instagram")), "with Instagram")


if __name__ == "__main__":
    main(*sys.argv[1:3])
