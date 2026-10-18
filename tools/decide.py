#!/usr/bin/env python3
"""Fast-fail waterfall G1..G9 over all evidence files. Writes stage files and, with --final,
the deliverable CSVs. Every rejection is logged against the FIRST failing gate in order.

Statuses per gate: PASS / FAIL / PENDING (needs browser run or regional agent verification).
"""
import csv
import glob
import json
import os
import re
import sys
from collections import Counter, defaultdict
from datetime import date, datetime

sys.path.insert(0, os.path.dirname(__file__))
from common import D60, D90, M9, RUN_DATE, rel_window, within  # noqa: E402
from sitecheck import root_domain  # noqa: E402

ROOT = "/home/user/100homeimprovementsearch"
D, O = f"{ROOT}/data", f"{ROOT}/output"
TODAY = RUN_DATE.isoformat()

# G1: the exclusion block supplied in the brief contained only the unfilled placeholder line.
EXCLUSION_NAMES, EXCLUSION_DOMAINS = set(), set()

ACCEPT_PLATFORMS = {"Wix", "Squarespace", "GoDaddy", "Weebly", "Webflow", "WordPress"}
NONORPHAN_FRAMEWORKS = {"Next.js", "Gatsby", "Nuxt", "Framer", "Duda", "Shopify", "HubSpot CMS", "Joomla", "Drupal",
                        "Hostinger Builder", "Yola", "Site123", "Strikingly", "Jimdo", "Carrd", "Tilda",
                        "React/Vite SPA", "Angular"}


def jl(path):
    out = []
    for f in sorted(glob.glob(path)):
        for l in open(f):
            if l.strip():
                out.append(json.loads(l))
    return out


USER_REVIEWS = {}
SOCIAL = {}
USER_SOCIAL, USER_JOBS, USER_HINTS = {}, {}, {}
# website-builder template links (the platform's own accounts), not the company's
PLATFORM_ACCT = re.compile(r"linkedin\.com/company/(wix-com|squarespace|godaddy|weebly|duda|hubspot|wordpress)|youtube\.com/(user/wix|@wix|@squarespace|user/squarespace|@godaddy)|pinterest\.[a-z.]+/(v3|pin|wix|squarespace)/", re.I)


def load():
    ledger = {x["id"]: x for x in jl(f"{D}/ledger.jsonl")}
    site = {x["id"]: x for x in jl(f"{D}/site.jsonl") + jl(f"{D}/site_b.jsonl") + jl(f"{D}/site_c.jsonl") + jl(f"{D}/site_d.jsonl")}
    for x in jl(f"{D}/site_render.jsonl"):
        orig = site.get(x["id"], {})
        if x.get("g2") == "PASS":
            x["rendered"] = True
            x["route1"] = orig.get("g2_reason") or orig.get("g2_route")
            site[x["id"]] = x
        elif orig.get("g2") != "PASS":
            orig["render_fail"] = x.get("g2_reason") or x.get("route1_error")
            site[x["id"]] = orig
    maps = {}
    for x in jl(f"{D}/maps_*.jsonl"):
        if x["id"] not in maps or (x.get("title") and not maps[x["id"]].get("title")):
            maps[x["id"]] = x
    br = {x["id"]: x for x in jl(f"{D}/browser_*.jsonl") if "tested" in x}
    psi = {x["id"]: x for x in jl(f"{D}/psi.jsonl") + jl(f"{D}/psi_q?.jsonl") if "psi_score" in x}
    dns = {x["id"]: x for x in jl(f"{D}/dns.jsonl")}
    for x in jl(f"{D}/g8extra.jsonl"):
        if x["id"] in site:
            site[x["id"]]["g8extra"] = x
    manual = {}
    def wave_order(f):  # later waves win: R*.jsonl (waves 1 to 6), then W7..W13 by number, coord.jsonl last
        b = os.path.basename(f)
        m = re.match(r"W(\d+)_(\d+)", b)
        return (2, 0, 0, b) if b.startswith("coord") else (1, int(m[1]), int(m[2]), b) if m else (0, 0, 0, b)
    for f in sorted(glob.glob(f"{D}/manual/*.jsonl"), key=wave_order):
        for x in jl(f):
            manual.setdefault(x["id"], {}).update(x)
    pre = {x["id"]: x for x in jl(f"{D}/pregate_rejects.jsonl")}
    # newest Google review dates the user collected through Gemini (output/review_requests/)
    SOCIAL.clear()
    SOCIAL.update({x["id"]: x for x in jl(f"{D}/social.jsonl")})
    for name, dct in (("social_user", USER_SOCIAL), ("jobs_user", USER_JOBS), ("hints_user", USER_HINTS)):
        dct.clear()
        dct.update({x["id"]: x for x in jl(f"{D}/{name}.jsonl")})
    USER_REVIEWS.clear()
    USER_REVIEWS.update({x["id"]: x for x in jl(f"{D}/reviews_user.jsonl")})
    for x in jl(f"{D}/remeasure.jsonl"):
        if x["id"] in site:
            site[x["id"]]["remeasure"] = x
    for x in jl(f"{D}/g7verify.jsonl"):
        if x["id"] in site:
            site[x["id"]]["g7verify"] = x
    for x in jl(f"{D}/g7visual.jsonl"):
        if x["id"] in site:
            site[x["id"]]["g7visual"] = x
    # coordinator dedupe pass 2: same FINAL (post-redirect) root domain = same business
    byfinal = {}
    for cid in sorted(ledger):
        s = site.get(cid)
        if s and s.get("g2") == "PASS" and s.get("final_url"):
            fr = root_domain(s["final_url"])
            byfinal.setdefault(fr, []).append(cid)
    for fr, ids in byfinal.items():
        if len(ids) > 1:
            keep = fr if fr in ids else ids[0]
            for cid in ids:
                if cid != keep:
                    ledger[cid]["dup_of"] = keep
    return ledger, site, maps, br, psi, dns, manual, pre


def ev(prospect, field, value, url, quote_or_method, rdate=TODAY):
    return {"prospect": prospect, "field": field, "value": value, "source_url": url,
            "quote_or_method": quote_or_method, "retrieval_date": rdate}


# ---------------------------------------------------------------- gates
def g1(c, s):
    n = c["norm_name"]
    hit = n in EXCLUSION_NAMES or any(d in EXCLUSION_DOMAINS for d in c["root_domains"])
    return ("FAIL" if hit else "PASS"), {"g1": "no match: exclusion block supplied was the unfilled placeholder (0 entries)"}


def g2(c, s, dns, br):
    if not s:
        return "PENDING", {"g2": "site not yet checked"}
    st = s.get("g2")
    if st == "PASS":
        e = {"g2_final_url": s["final_url"], "g2_http_status": s["http_status"], "g2_fetch_date": s["fetch_date"],
             "g2_route": s.get("g2_route") + (f" (route1 python-requests: {s['route1'][:120]})" if s.get("rendered") else ""),
             "g2_vantage": s.get("vantage")}
        if s.get("g2_cross_domain"):
            e["g2_cross_domain"] = s["g2_cross_domain"]
        return "PASS", e
    if st == "FAIL":
        return "FAIL", {"g2": s.get("g2_reason")}
    # RETRY_BROWSER / ERROR -> needs DNS-over-HTTPS confirmation or a real-browser fetch
    if s.get("render_fail"):
        return "FAIL", {"g2": f"route1 {s.get('g2_reason','')[:160]}; route3 Chromium render, US egress: {s['render_fail'][:160]}"}
    d = dns.get(c["id"])
    if d and d.get("nxdomain"):
        return "FAIL", {"g2": f"domain does not resolve: system resolver via proxy ({s.get('g2_reason','')[:120]}) "
                              f"and Google DNS-over-HTTPS {d.get('doh_url')} -> Status {d.get('status')}"}
    b = br.get(c["id"])
    if b:
        if b.get("status") and b["status"] < 400 and not b.get("error"):
            return "PENDING", {"g2": f"loads in real browser (HTTP {b['status']} {b.get('final_url')}) but blocks scripted fetch; "
                                     f"needs browser-route crawl", "g2_browser": b}
        return "FAIL", {"g2": f"route1 {s.get('g2_reason','')[:160]}; route3 Chromium US egress: "
                              f"{b.get('error') or 'HTTP ' + str(b.get('status'))}"}
    return "PENDING", {"g2": "awaiting retry route: " + (s.get("g2_reason") or "")[:160]}


PLUGIN_CREDIT = re.compile(r"slider revolution|wpbakery|beaver builder|visual composer|elementor|site kit|yoast|"
                           r"all in one seo|aioseo|rank ?math|jetpack|wordpress|wix|squarespace|godaddy|weebly|webflow|"
                           r"woocommerce|gravity forms|wpforms|smash balloon|cookieyes|complianz|termly|recaptcha|"
                           r"google|cloudflare|wp engine|bluehost|siteground|flywheel|kinsta|litespeed", re.I)
EXTRA_COMMERCIAL_THEME = re.compile(r"godaddy|crocoblock|themelexus|themeforest|envato|themegoods|theme-?junkie|"
                                    r"wpopal|themebeez|themeinwp|athemes|themesgenerator|weblizar", re.I)


def credit_ok(cr, c):
    """True when the matched string is a real site-builder credit (not a plugin banner, alt text or JSON)."""
    if PLUGIN_CREDIT.search(cr["credit"]):
        return False
    ctx = cr["context"]
    if '\\"' in ctx or '\\u' in ctx or re.search(r'alt=|"alt"|\\"', ctx):
        return False
    first = re.sub(r"[^a-z]", "", (c["name"].split() or [""])[0].lower())
    if first and len(first) > 2 and first in cr["credit"].lower().replace(" ", ""):
        return False
    return True


def g3(c, s, man=None):
    v = (man or {}).get("g3_vendor_found")
    if isinstance(v, list):
        v = v[0] if v else None
    if isinstance(v, str):
        v = None if re.match(r"\s*(none|null|n/?a|no\b|unknown)", v, re.I) else {"vendor": v, "quote": v, "url": ""}
    if v:
        return "FAIL", {"g3": f"vendor credit found during manual review: {v.get('quote')} ({v.get('url')})",
                        "g3_vendor": v.get("vendor"), "g3_platform": s.get("platform")}
    vend = s.get("vendor_hits") or []
    cred = [cr for cr in (s.get("credits") or []) if credit_ok(cr, c)]
    plat = set(s.get("platform") or [])
    fw = [f for f in (s.get("frameworks") or []) if f in NONORPHAN_FRAMEWORKS]
    theme_agency = [t for t in (s.get("wp_theme_noncommercial") or [])
                    if not EXTRA_COMMERCIAL_THEME.search((t.get("Author") or "") + " " + (t.get("Author URI") or ""))]
    reasons = []
    vendor_named = None
    if vend:
        vendor_named = vend[0]["vendor"]
        reasons.append(f"vendor asset/credit '{vend[0]['vendor']}': ...{vend[0]['match'][:140]}...")
    if cred:
        vendor_named = vendor_named or cred[0]["credit"]
        reasons.append(f"credit string: \"{cred[0]['context'][:160]}\"")
    for t in theme_agency:
        a = (t.get("Author") or "").strip()
        if a and not re.search(r"^(admin|wordpress|me|developer|-|n/a|unknown)$", a, re.I):
            vendor_named = vendor_named or f"{a} (WP theme author)"
            reasons.append(f"WP theme header {t['url']}: Theme Name '{t.get('Theme Name')}', Author '{a}', "
                           f"Author URI '{t.get('Author URI')}'")
    for fl in (s.get("g8extra") or {}).get("footer_vendor_links", []):
        vendor_named = vendor_named or fl["text"] or fl["domain"]
        reasons.append(f"footer link to web/marketing vendor: text '{fl['text']}' -> {fl['href']}")
    if reasons:
        return "FAIL", {"g3": "; ".join(reasons), "g3_vendor": vendor_named, "g3_platform": sorted(plat)}
    bad_gen = [g for g in (s.get("generator") or []) if re.search(r"hubspot|duda|zoho|web studio|yola|site123|strikingly|jimdo|"
                                                               r"hostinger|zyro|framer|nuxt|gatsby|next\.js|astro|joomla|drupal|"
                                                               r"shopify|weblium|tilda|godaddy website builder", g, re.I)]
    if bad_gen:
        return "FAIL", {"g3": f"meta generator '{bad_gen[0]}' is not on the orphaned/self-managed accept list "
                              f"(WordPress traces present: {'WordPress' in plat})", "g3_vendor": None, "g3_platform": bad_gen}
    if fw and not (plat & ACCEPT_PLATFORMS):
        return "FAIL", {"g3": f"platform not on the orphaned/self-managed accept list: {', '.join(fw)}",
                        "g3_vendor": None, "g3_platform": fw}
    if plat & ACCEPT_PLATFORMS:
        p = sorted(plat & ACCEPT_PLATFORMS)
    else:
        if s.get("generator"):
            return "FAIL", {"g3": f"unrecognised generator {s['generator']}", "g3_vendor": None}
        p = ["Hand-coded HTML (no generator, no credit)"]
    return "PASS", {"g3_platform": p, "g3_generator": s.get("generator"), "g3_script_domains": s.get("script_domains"),
                    "g3_theme": [(t.get("Theme Name"), t.get("Author")) for t in s.get("wp_theme") or []],
                    "g3_check": "raw HTML, response headers, meta generator, script src domains, WP style.css header, "
                                "footer/tail credit regex: no vendor credit found"}


def gbp_reviews(m):
    revs = (m or {}).get("reviews") or []
    out = []
    for r in revs:
        w = rel_window(r.get("when"))
        out.append({**r, "window": [str(w[0]), str(w[1])] if w else None})
    return out


def g4(c, s, m, man):
    signals = []
    mm = m or {}
    if mm.get("error") or not mm.get("title"):
        gbp_status = "GBP not retrieved"
    else:
        ov = mm.get("overview") or ""
        if re.search(r"Permanently closed|Temporarily closed", ov):
            return "FAIL", {"g4": "Google Business Profile shows " + re.search(r"Permanently closed|Temporarily closed", ov).group(0),
                            "g4_gbp": mm.get("gbp_url")}
        gbp_status = "listed"
    rej = json.dumps((man or {}).get("auto_signals_rejected") or "").lower()
    for r in gbp_reviews(m):
        if "google_review" in rej:
            break
        if within(r.get("when"), D90):
            signals.append({"type": "google_review", "date": f"{r['window'][0]}..{r['window'][1]}",
                            "url": mm.get("gbp_url"), "quote": f"{r['reviewer']}: '{r['when']}' (Google relative timestamp, retrieved {mm.get('retrieved','')[:10]})"})
            break
    for dcont in ((s or {}).get("dated_content") or []) if "site_dated_content" not in rej else []:
        try:
            dd = dcont["date"]
            dt = datetime.fromisoformat(dd[:19]).date() if re.match(r"\d{4}-\d{2}-\d{2}", dd or "") else \
                datetime.strptime(re.sub(r"\s+[+-]\d{4}$|\s+GMT$|\s+[A-Z]{3}$", "", dd.strip()), "%a, %d %b %Y %H:%M:%S").date()
        except Exception:
            continue
        if dt >= D90 and dt <= RUN_DATE and not re.search(r"/pages$", dcont["src"]):
            signals.append({"type": "site_dated_content", "date": str(dt), "url": dcont.get("link"),
                            "quote": f"{dcont['src']} published {dd}: '{(dcont.get('title') or '')[:80]}'"})
            break
    for x in (man or {}).get("g4_extra_signals") or []:
        try:
            dt = date.fromisoformat(x["date"][:10])
        except Exception:
            continue
        if D90 <= dt <= RUN_DATE and x.get("url"):
            signals.append(x)
    if "social_post" not in rej:
        # newest in-window post on an account linked from the company's own site (tools/social.py)
        posts = sorted((p for p in (SOCIAL.get(c["id"]) or {}).get("posts") or []
                        if re.match(r"\d{4}-\d{2}-\d{2}$", p.get("date") or "") and D90 <= date.fromisoformat(p["date"]) <= RUN_DATE
                        and not PLATFORM_ACCT.search(p.get("account") or "")),
                       key=lambda p: p["date"], reverse=True)
        if posts:
            p0 = posts[0]
            signals.append({"type": "social_post", "date": p0["date"], "url": p0["post_url"],
                            "quote": f"{p0['platform']} {p0['account']} post: '{' '.join(p0['quote'].split()[:12])}'",
                            "method": p0["method"]})
    if (USER_HINTS.get(c["id"]) or {}).get("gbp_closed"):
        return "FAIL", {"g4": "Google Business Profile shown as closed (user-supplied via Gemini)", "g4_gbp": (m or {}).get("gbp_url")}
    if "social_post" not in rej:
        for p in sorted((USER_SOCIAL.get(c["id"]) or {}).get("posts") or [], key=lambda p: p["date"], reverse=True):
            if D90 <= date.fromisoformat(p["date"]) <= RUN_DATE:
                signals.append({"type": "social_post", "date": p["date"], "url": p["account"], "source": p["method"],
                                "quote": f"{p['platform']} {p['account']} latest post {p['date']}" + (f": '{p['quote']}'" if p["quote"] else "")})
                break
    uj = USER_JOBS.get(c["id"])
    if uj and "job_posting" not in rej and D90 <= date.fromisoformat(uj["date"]) <= RUN_DATE:
        signals.append({"type": "job_posting", "date": uj["date"], "url": uj["url"], "source": uj["source"],
                        "quote": " ".join(f"job posting: {uj['title']}".split()[:15])})
    ur = USER_REVIEWS.get(c["id"])
    if ur and "google_review" not in rej:
        try:
            dt = date.fromisoformat(ur["date"])
        except Exception:
            dt = None
        if dt and D90 <= dt <= RUN_DATE:
            signals.append({"type": "google_review", "date": ur["date"], "url": ur["url"], "source": ur["source"],
                            "quote": ur["quote"]})
    types = {}
    for x in signals:
        types.setdefault(x["type"].replace("google_review", "google_review"), x)
    phone = phone_check(c, s, m)
    ev_ = {"g4_signals": list(types.values()), "g4_phone": phone, "g4_gbp_status": gbp_status}
    if len(types) >= 2:
        if phone["status"] == "FAIL":
            return "FAIL", {**ev_, "g4": "phone check failed: " + phone["detail"]}
        return "PASS", ev_
    if man and (man.get("g4_done") is True or man.get("stopped_at") == "G4"):
        return "FAIL", {**ev_, "g4": f"only {len(types)} dated signal type(s) inside 90 days could be evidenced "
                                     f"({', '.join(types) or 'none'}); regional search notes: {man.get('g4_notes','')[:200]}"}
    if len(types) == 0:
        return "FAIL", {**ev_, "g4": "no dated signal inside 90 days in the 3 Google reviews visible on the GBP (anonymous "
                                     "limited view) or in dated site content (WP REST / RSS); two signal types required, "
                                     "manual search for two further types not run"}
    return "PENDING", {**ev_, "g4": f"{len(types)} of 2 signal types evidenced; needs regional search"}


def digits(x):
    return re.sub(r"\D", "", x or "")[-10:]


def phone_check(c, s, m):
    gbp = digits((m or {}).get("phone") or c.get("phone_maps"))
    tels = {digits(t) for t in (s or {}).get("tel_links") or [] if len(digits(t)) == 10}
    detail = f"GBP phone {gbp or 'none'}; site tel: links {sorted(tels) or 'none'}"
    if gbp and gbp in tels:
        return {"status": "PASS", "detail": detail + "; same number published on GBP and own site. Not dial-tested."}
    if gbp or tels:
        return {"status": "PASS", "detail": detail + "; numbers published (not matched across sources). Not dial-tested."}
    return {"status": "FAIL", "detail": detail}


def g5(c, s, man):
    name = c["name"].lower()
    fr = (s or {}).get("franchise_hits") or []
    frp = (s or {}).get("franchise_phrases") or []
    in_name = [f for f in fr if f in name]
    if in_name or frp:
        return "FAIL", {"g5": f"franchise signal: name/brand {in_name or fr} phrases {frp}"}
    if man and isinstance(man.get("g5_pass"), bool):
        if not man["g5_pass"]:
            return "FAIL", {"g5": man.get("g5_evidence")}
        return "PASS", {"g5": man.get("g5_evidence"), "g5_brand_mentions": fr}
    if fr:
        return "PENDING", {"g5": f"brand mention(s) on site need review: {fr}"}
    return "PENDING", {"g5": "independence to be confirmed from about page"}


def g6(c, s, man):
    emails = (s or {}).get("emails") or []
    man = man or {}
    dm = man.get("decision_maker")
    conf = man.get("email_confirm")
    if "decision_maker" in man and not dm:
        return "FAIL", {"g6": "no named decision maker found on contact/about/team/footer/privacy/terms "
                              "(linked Facebook About not readable: login wall)", "g6_emails": emails}
    if "email_confirm" in man and not conf:
        if dm:
            return "CONTACT_ONLY", {"g6": "named decision maker found but no published email", "g6_dm": dm}
        return "FAIL", {"g6": "no published email and no named decision maker"}
    if not emails and not conf:
        return "PENDING", {"g6": "no published email in automatically fetched pages", "g6_emails": []}
    if not dm:
        return "PENDING", {"g6": "email found; decision maker to be confirmed", "g6_emails": emails}
    em = conf or emails[0]
    return "PASS", {"g6_dm": dm, "g6_email": em, "g6_emails": emails}


def g7(c, s, man):
    imgs = (s or {}).get("imgs_800") or []
    v = (s or {}).get("g7verify")
    if v:
        vis = s.get("g7visual")
        excl = set((vis or {}).get("exclude") or [])
        kept = [k for i, k in enumerate(v["kept"], 1) if i not in excl]
        if len(kept) < 8:
            return "FAIL", {"g7": f"strict check: {len(kept)} unique non-graphic images >=800px after near-duplicate removal "
                                  f"({v['candidates_checked']} candidates checked)", "g7_urls": [k['url'] for k in kept]}
        if vis and not vis["ok"]:
            return "FAIL", {"g7": "visual review of contact sheet: " + vis["note"], "g7_urls": [k['url'] for k in kept]}
        return "PASS", {"g7_count_checked": len(kept), "g7_urls": [k["url"] for k in kept[:8]],
                        "g7_dims": [f"{k['w']}x{k['h']}" for k in kept[:8]],
                        "g7_method": "img/srcset/data-src/CSS backgrounds on home+gallery pages; CMS resize segments stripped; "
                                     "full image downloaded and width read; stock filename/media-ID signatures, graphics "
                                     "(>55% white or <24 colour buckets) and near-duplicates (dHash<=6) removed; "
                                     + (f"contact sheet visually reviewed: {vis['note']}" if vis else "contact sheet NOT yet visually reviewed")}
    if man and man.get("g7_override") is not None:
        o = man["g7_override"]
        return ("PASS" if o.get("pass") else "FAIL"), {"g7": o.get("note"), "g7_urls": o.get("urls", [])}
    if len(imgs) >= 8:
        return "PASS", {"g7_count_checked": len(imgs), "g7_urls": [i["master"] for i in imgs[:8]],
                        "g7_dims": [f"{i['w']}x{i['h']}" for i in imgs[:8]],
                        "g7_method": "img src/srcset/data-src + CSS backgrounds on home & gallery pages; CMS resize "
                                     "segments stripped; pixel width read from image header; stock-library filename/"
                                     "media-ID signatures excluded"}
    return "FAIL", {"g7": f"only {len(imgs)} original-candidate images >=800px wide found on home+gallery pages "
                          f"(stock-signature images excluded: {len((s or {}).get('imgs_stock') or [])}); GBP owner photos not "
                          f"retrievable in anonymous Maps limited view", "g7_urls": [i["master"] for i in imgs]}


def g8(c, s, b, p):
    found = []
    psi_val = (p or {}).get("psi_score")
    psi_rec = None
    if p:
        psi_rec = {"tested_url": p["tested_url"], "result": psi_val,
                   "attempts": "; ".join(f"{a.get('at')} HTTP {a.get('http', a.get('error'))}" for a in p["attempts"])}
        if isinstance(psi_val, int) and psi_val < 60:
            found.append(("mobile performance score below 60", f"PSI mobile performance {psi_val}", p["tested_url"], p.get("psi_date")))
    if s and not s.get("viewport_meta"):
        found.append(("no <meta name=\"viewport\">", "raw HTML <head> contains no meta name=viewport (regex over fetched HTML)",
                      s["final_url"], s["fetch_date"]))
    if s and (s.get("final_scheme") == "http" or (s.get("https_check") or {}).get("https_error")):
        found.append(("not served over HTTPS / invalid certificate",
                      f"final URL scheme {s.get('final_scheme')}; https:// probe: {s.get('https_check')}", s["final_url"], s["fetch_date"]))
    if b and not b.get("error"):
        ox = b.get("overflow_vs_device_px")
        if ox is None:
            ox = 0
        if b.get("viewport") and ox >= 5:
            found.append(("horizontal overflow at 375px", f"375px-wide mobile viewport (iPhone UA, DPR 3): document width "
                          f"{max(b['scrollWidth'], b['innerWidth'])}px, i.e. {ox}px wider than the screen; elements past the "
                          f"right edge: {b.get('offenders', [])[:3]}", b.get("final_url"), b["tested"][:10]))
        big = b.get("served_images_over_1mb") or []
        if len(big) >= 2:
            found.append(("gallery images over 1MB each", "; ".join(f"{x['url']} = {x['bytes']:,} bytes" for x in big[:4]),
                          b.get("gallery_tested") or b.get("final_url"), b["tested"][:10]))
    if s:
        big = s.get("served_sizes_over_1mb") or []
        if len(big) >= 2 and not any(f[0].startswith("gallery images") for f in found):
            found.append(("gallery images over 1MB each", "; ".join(f"{x['url']} = {x['bytes']:,} bytes (HTTP Content-Length)" for x in big[:4]),
                          s["final_url"], s["fetch_date"]))
        gx = s.get("g8extra") or {}
        for dm in gx.get("dead_mail", []):
            if "%20" in dm["mailto"]:
                continue
            found.append(("dead phone or email link", f"mailto:{dm['mailto']} -> domain {dm['domain']} has no MX and no A record ({dm['method']})",
                          s["final_url"], gx.get("checked")))
            break
        for df in gx.get("dead_forms", []):
            found.append(("broken quote or estimate form", f"form on {df['page']} posts to {df['action']}: {df['result']}", df["page"], gx.get("checked")))
            break
        bad_tel = [t for t in s.get("tel_links") or [] if 0 < len(re.sub(r"\D", "", t)) < 10]
        bad_mail = [t for t in s.get("mailto_links") or [] if "@" not in t]
        if bad_tel or bad_mail:
            found.append(("dead phone or email link", f"tel: hrefs {bad_tel} mailto: hrefs {bad_mail}", s["final_url"], s["fetch_date"]))
    rm = (s or {}).get("remeasure")
    if rm and rm["over_1mb_browser"] < 2 and rm["over_1mb_curl"] < 2:
        found = [f for f in found if not f[0].startswith("gallery images")]
        note = (f"1MB-image defect did not reproduce on re-measurement ({rm['measured_on']}, full download, browser and curl "
                f"Accept headers): " + "; ".join(f"{i['url'][-50:]} = {i.get('browser_accept')}/{i.get('curl_accept')} bytes" for i in rm["images"]))
        if not found:
            return "FAIL", {"g8": note, "g8_psi": psi_rec}
    elif rm:
        found = [(f[0], f[1] + f" | re-measured {rm['measured_on']} (full download): " + "; ".join(
            f"{i['url'][-60:]} = {i.get('browser_accept'):,} bytes (browser Accept) / {i.get('curl_accept'):,} bytes (curl)"
            for i in rm["images"] if isinstance(i.get('browser_accept'), int) and isinstance(i.get('curl_accept'), int)), f[2], f[3])
                 if f[0].startswith("gallery images") else f for f in found]
    if not p or not b:
        if found:
            return "PASS", {"g8_defects": found, "g8_psi": psi_rec}
        return "PENDING", {"g8": "awaiting PSI/browser measurement", "g8_psi": psi_rec}
    if found:
        return "PASS", {"g8_defects": found, "g8_psi": psi_rec}
    return "FAIL", {"g8": "no measured defect: PSI " + str(psi_val) + "; viewport present; HTTPS valid; no 375px overflow; "
                          "<2 served images >1MB; tel/mailto links well-formed", "g8_psi": psi_rec}


def g9(c, s, b):
    sig = list((s or {}).get("paid_signals_raw") or [])
    out = [{"signal": x["signal"], "evidence": "raw HTML: " + x["snippet"]} for x in sig]
    for k, u in ((b or {}).get("net_signals") or {}).items():
        out.append({"signal": k, "evidence": "network request fired on page load (Chromium, US egress): " + u})
    if out:
        return "PASS", {"g9_signals": out}
    if not b:
        return "PENDING", {"g9": "no raw-HTML signal; awaiting browser network capture"}
    return "FAIL", {"g9": "no ad pixel, call tracking, paid review/trade platform or paid field software found in raw HTML "
                          "of fetched pages or in network requests on load"}


def niche(c, s, man):
    if man and "niche_ok" in man:
        return ("PASS" if man["niche_ok"] else "FAIL"), {"niche": man.get("niche_evidence")}
    n = (s or {}).get("niche_counts") or {}
    kb = min(n.get("kitchen", 0), n.get("bath", 0))
    other = max([n.get(k, 0) for k in ("roof", "plumb", "hvac", "handyman", "floor", "siding", "window", "pool", "solar", "custom home")] or [0])
    kbs = n.get("kitchen", 0) + n.get("bath", 0)
    if (s or {}).get("home_text_len", 0) < 600:
        return "PENDING", {"niche": f"home page has little server-rendered text ({(s or {}).get('home_text_len')} chars); counts {n}"}
    if n and kbs == 0:
        return "FAIL", {"niche": f"home page text mentions neither kitchens nor baths; word counts {n}"}
    if n and other > 5 and other > 2 * kbs:
        return "FAIL", {"niche": f"home page text dominated by other trades; word counts {n}"}
    return "PENDING", {"niche": f"counts {n}"}


ORDER = ["G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8", "G9"]


def evaluate(c, data):
    ledger, site, maps, br, psi, dns, manual, pre = data
    s, m, b, p, man = site.get(c["id"]), maps.get(c["id"]), br.get(c["id"]), psi.get(c["id"]), manual.get(c["id"])
    res = {"gates": {}, "ev": {}}
    res["gates"]["G1"], e = g1(c, s); res["ev"].update(e)
    res["gates"]["G2"], e = g2(c, s, dns, br); res["ev"].update(e)
    if res["gates"]["G2"] != "PASS":
        return res
    res["niche"], e = niche(c, s, man); res["ev"].update(e)
    res["gates"]["G3"], e = g3(c, s, man); res["ev"].update(e)
    res["gates"]["G4"], e = g4(c, s, m, man); res["ev"].update(e)
    res["gates"]["G5"], e = g5(c, s, man); res["ev"].update(e)
    res["gates"]["G6"], e = g6(c, s, man); res["ev"].update(e)
    res["gates"]["G7"], e = g7(c, s, man); res["ev"].update(e)
    res["gates"]["G8"], e = g8(c, s, b, p); res["ev"].update(e)
    res["gates"]["G9"], e = g9(c, s, b); res["ev"].update(e)
    return res


def first_fail(res, skip=()):
    for g in ORDER:
        if g in skip:
            continue
        st = res["gates"].get(g)
        if st is None:
            return None, None
        if st != "PASS":
            return g, st
    return None, "ALLPASS"


if __name__ == "__main__":
    data = load()
    ledger = data[0]
    stage = Counter()
    for cid, c in ledger.items():
        if cid in data[7]:
            stage["pregate:" + data[7][cid]["gate"]] += 1
            continue
        r = evaluate(c, data)
        if r.get("niche") == "FAIL":
            stage["NICHE"] += 1
            continue
        g, st = first_fail(r)
        stage[f"{g}:{st}" if g else st] += 1
    for k, v in sorted(stage.items()):
        print(k, v)
