#!/usr/bin/env python3
"""Site-level screening for gates G2, G3, G5 (site signals), G6, G7, G8 (static checks), G9 (raw HTML).

Usage: python3 sitecheck.py <candidates.jsonl> <out.jsonl> [workers]
Each input line needs: id, name, website. Output adds raw evidence per gate; the
waterfall decision is made later in decide.py so that every rejection is logged
against the FIRST failing gate in order.
"""
import html as htmlmod
import json
import re
import struct
import subprocess
import sys
import time
from concurrent.futures import ProcessPoolExecutor
from datetime import datetime, timezone
from io import BytesIO
from urllib.parse import urljoin, urlparse, urlunparse, parse_qsl, urlencode

import requests
from bs4 import BeautifulSoup

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36")
HDRS = {"User-Agent": UA, "Accept-Language": "en-US,en;q=0.9",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"}
TODAY = datetime.now(timezone.utc).strftime("%Y-%m-%d")

SOCIAL = ("facebook.com", "instagram.com", "yelp.com", "houzz.com", "linkedin.com",
          "nextdoor.com", "angi.com", "homeadvisor.com", "thumbtack.com", "google.com",
          "business.site", "g.page", "linktr.ee", "x.com", "twitter.com", "tiktok.com")

PARKED = [r"this domain (?:name )?(?:is|may be) for sale", r"buy this domain", r"domain is parked",
          r"sedoparking", r"hugedomains\.com", r"afternic", r"dan\.com/buy-domain",
          r"parked free", r"parkingcrew", r"bodis\.com", r"godaddy\.com/forsale",
          r"this site can.t be reached", r"account has been suspended", r"website (?:is )?(?:coming soon|under construction)",
          r"future home of", r"default web site page", r"index of /"]

# --- G3 vendor fingerprints (asset domains / strings) ---
VENDORS = {
    "Hibu": [r"hibu\.com", r"hibustudio", r"hibu-"],
    "Thryv": [r"thryv\.com", r"thryvcdn", r"mythryv"],
    "Web.com": [r"\bweb\.com\b", r"websites\.web\.com", r"wsimg-web\.com", r"yodle"],
    "Townsquare Interactive": [r"townsquareinteractive", r"tsi-cdn", r"townsquare interactive"],
    "LocaliQ / ReachLocal": [r"localiq", r"reachlocal", r"rlets\.com", r"rtrk\.com", r"gannett"],
    "Vivial": [r"vivial\.net", r"vivial"],
    "Netsertive": [r"netsertive"],
    "Scorpion": [r"scorpion\.co\b", r"scorpioncms", r"scorpion internet", r"scorpion\.com"],
    "Blue Corona": [r"bluecorona"],
    "Houzz Pro websites": [r"houzzsite", r"houzz\.com/pro/website", r"st\.hzcdn\.com/static.*site", r"houzzpro"],
    "Contractor Gorilla": [r"contractorgorilla"],
    "Builder Designs": [r"builderdesigns"],
    "Footbridge Media": [r"footbridgemedia", r"footbridge media"],
    "Hook Agency": [r"hookagency", r"hook agency"],
    "Contractor Dynamics": [r"contractordynamics", r"contractor dynamics"],
    "Angi-built site": [r"angi\.com/websites", r"angisites", r"homeadvisor\.com/websites", r"hasites"],
    "Yelp-built site": [r"yelp\.com/websites", r"yelpsites"],
    "Duda (agency reseller platform)": [r"irp\.cdn-website\.com", r"cdn-website\.com", r"dudamobile", r"multiscreensite"],
    "SiteSwan": [r"siteswan"],
    "Boostability": [r"boostability"],
    "ProBuilder/ProSites": [r"prosites\.com"],
    "Weave": [r"getweave\.com"],
    "GoHighLevel / LeadConnector (agency platform)": [r"leadconnectorhq", r"msgsndr\.com", r"gohighlevel"],
    "HubSpot CMS (agency-managed platform)": [r"hs-sites\.com", r"hubspotusercontent", r"hsappstatic"],
    "Leadpages": [r"leadpages"],
}
CREDIT_RE = re.compile(
    r"(?:(?:web\s*)?site\s+(?:designed|developed|created|built|design|powered|managed|maintained|hosted)?|website\s+design|"
    r"web\s*design|designed|developed|powered|marketing|design(?:ed)?\s+(?:and|&)\s+develop(?:ed|ment)|"
    r"seo|digital marketing)"
    r"\s+by\s*[:\-]?\s*(?:<[^>]{0,300}>\s*){0,4}([A-Z0-9][\w&.,' \-]{1,60})", re.I)
PLATFORM_WORDS = re.compile(r"^(wordpress|wix|wix\.com|squarespace|godaddy|go daddy|weebly|webflow|square|"
                            r"elementor|divi|astra|generatepress|the wordpress team|hostinger|wpengine|wp engine|"
                            r"cloudflare|google|bluehost|siteground|kinsta|jobber|squareup)\b", re.I)

FRANCHISE = ["re-bath", "rebath", "bath fitter", "kitchen tune-up", "kitchen tune up", "granite transformations",
             "dreammaker bath", "dreammaker", "monk's home improvement", "handyman connection",
             "normandy remodeling", "normandy designer", "window world", "renewal by andersen", "five star bath solutions",
             "bath planet", "luxury bath technologies", "luxury bath systems", "bath tune-up", "miracle method",
             "mr. handyman", "mr handyman", "ace handyman services", "case design/remodeling", "case handyman",
             "jacuzzi bath remodel", "bathwraps", "west shore home", "kitchen solvers", "kitchen saver", "closet factory",
             "4 seasons bath", "power home remodeling", "sears home services", "paul davis restoration", "puroclean",
             "bath concepts", "zen bathworks", "nexus home", "bath experts", "bath doctor", "kitchen wise"]
FRANCHISE_PHRASES = [r"independently owned and operated franchise", r"each franchise is independently",
                     r"franchise opportunit", r"own a franchise", r"find a location near you",
                     r"find (?:a|your) (?:local )?location", r"locations near you", r"franchisee",
                     r"independently owned and operated\.?\s*(?:by|franchise)", r"\ba [a-z0-9 &]{2,40} brands company",
                     r"\ba (?:division|subsidiary) of\b", r"operates under the names?", r"formerly known as [a-z0-9 ,&]+(?:llc|inc)",
                     r"locations? in \d{2,} states", r"cities served nationwide"]

NOT_NICHE = {"roof": r"\broof(?:ing|er|s)?\b", "plumb": r"\bplumb(?:ing|er)s?\b", "hvac": r"\bhvac\b|air condition",
             "handyman": r"\bhandym[ae]n\b", "floor": r"\bflooring\b", "cabinet": r"\bcabinet(?:s|ry)?\b",
             "siding": r"\bsiding\b", "window": r"\bwindows?\b", "pool": r"\bpools?\b", "solar": r"\bsolar\b",
             "custom home": r"custom homes?|new home construction|home ?builder"}

PIXELS = {
    "Google Ads conversion tag (AW-)": r"AW-\d{6,}",
    "googleadservices.com": r"googleadservices\.com",
    "Meta Pixel fbevents.js": r"connect\.facebook\.net/[^\"' ]*fbevents\.js",
    "Microsoft Ads UET bat.bing.com": r"bat\.bing\.com",
    "CallRail": r"callrail\.com|cdn\.callrail",
    "CallTrackingMetrics": r"calltrackingmetrics|tctm\.co",
    "WhatConverts": r"whatconverts",
    "Angi": r"angi\.com",
    "HomeAdvisor": r"homeadvisor",
    "Thumbtack": r"thumbtack\.com",
    "Houzz Pro": r"houzz\.com/pro",
    "GuildQuality": r"guildquality",
    "Podium": r"podium\.com|podiumwebchat",
    "Birdeye": r"birdeye\.com",
    "NiceJob": r"nicejob",
    "ReviewBuzz": r"reviewbuzz",
    "ServiceTitan": r"servicetitan",
    "Housecall Pro": r"housecallpro",
    "Jobber": r"getjobber\.com|jobber\.com",
    "JobNimbus": r"jobnimbus",
    "Buildertrend": r"buildertrend",
    "CoConstruct": r"coconstruct",
    "CompanyCam": r"companycam",
    "Hatch": r"usehatchapp|hatchapp",
}

STOCK = re.compile(r"shutterstock|istock|adobestock|adobe-stock|gettyimages|getty-images|unsplash|pexels|"
                   r"depositphotos|bigstock|dreamstime|123rf|stock[-_ ]?photo|nsplsh_|/11062b_|pixabay|freepik|"
                   r"canva|placeholder|dummy", re.I)
SKIPIMG = re.compile(r"logo|icon|favicon|sprite|badge|seal|award|bbb|houzz|angi|homeadvisor|yelp|google|facebook|"
                     r"instagram|map|avatar|\.svg|\.gif|pixel|spacer|blank|loader|arrow|button|star", re.I)

EMAIL_RE = re.compile(r"[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}")
BAD_EMAIL = re.compile(r"\.(png|jpe?g|gif|webp|svg|css|js)$|sentry|wixpress|example\.|domain\.com|email\.com|"
                       r"yourname|youremail|name@|user@|test@|@2x|@3x|godaddy|squarespace|wix\.com|"
                       r"cloudflare|jquery|bootstrap|w3\.org|schema\.org", re.I)

DM_RE = re.compile(r"([^.\n]{0,120}\b(?:owner|co-owner|founder|co-founder|president|ceo|principal|proprietor|"
                   r"owned and operated by|founded by|general manager)\b[^.\n]{0,120})", re.I)


SHARED_HOSTS = ("wixsite.com", "squarespace.com", "godaddysites.com", "weebly.com", "business.site", "netlify.app",
                "webflow.io", "wordpress.com", "square.site", "yolasite.com", "sites.google.com", "vercel.app",
                "myshopify.com", "carrd.co", "site123.me", "mystrikingly.com", "jimdosite.com", "github.io")


def root_domain(url):
    pu = urlparse(url if "//" in url else "http://" + url)
    h = (pu.hostname or "").lower()
    h = h[4:] if h.startswith("www.") else h
    for sh in SHARED_HOSTS:
        if h.endswith(sh):
            seg = pu.path.strip("/").split("/")[0] if sh in ("wixsite.com", "sites.google.com") else ""
            return (h + ("/" + seg if seg else "")).lower()
    parts = h.split(".")
    return ".".join(parts[-2:]) if len(parts) >= 2 else h


def clean_url(u):
    p = urlparse(u)
    q = [(k, v) for k, v in parse_qsl(p.query) if not k.lower().startswith(("utm_", "ref", "gclid", "fbclid"))
         and k.lower() not in ("y_source",)]
    return urlunparse((p.scheme or "http", p.netloc, p.path or "/", "", urlencode(q), ""))


RENDER = bool(__import__("os").environ.get("RENDER"))


class Rendered:
    def __init__(self, url):
        r = requests.get("http://127.0.0.1:8765/", params={"url": url}, timeout=120,
                         proxies={"http": None, "https": None})
        self.status_code = int(r.headers.get("X-Status") or 0) if r.status_code == 200 else 599
        if self.status_code == 0 and r.status_code == 200:
            self.status_code = 200
        self.url = requests.utils.unquote(r.headers.get("X-Final-Url") or url)
        self.text = r.text
        self.headers = {"Content-Type": "text/html", "X-Render-Error": r.headers.get("X-Error", "")}
        self.history = []


def page_get(session, url, timeout=20):
    if RENDER:
        return Rendered(url)
    return session.get(url, headers=HDRS, timeout=timeout)


def fetch(url, session, timeout=25):
    t = time.time()
    if RENDER:
        r = Rendered(url)
        return r, [r.url], round(time.time() - t, 2)
    r = session.get(url, headers=HDRS, timeout=timeout, allow_redirects=True)
    chain = [h.url for h in r.history] + [r.url]
    return r, chain, round(time.time() - t, 2)


def curl_fetch(url):
    """Second route: system curl with a different client stack."""
    out = subprocess.run(["curl", "-sSL", "-m", "30", "-A", "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5) "
                          "AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15",
                          "-w", "\n__STATUS__%{http_code} %{url_effective}", url],
                         capture_output=True, text=True, timeout=40)
    body, _, tail = out.stdout.rpartition("\n__STATUS__")
    code, _, eff = tail.partition(" ")
    return int(code or 0), eff.strip(), body, out.stderr.strip()[:200]


def decode_cfemail(hexs):
    k = int(hexs[:2], 16)
    return "".join(chr(int(hexs[i:i + 2], 16) ^ k) for i in range(2, len(hexs), 2))


def find_emails(raw, page_url, text=None):
    found = []
    for m in re.finditer(r'href=["\']mailto:([^"\'?]+)', raw, re.I):
        found.append({"email": htmlmod.unescape(m.group(1)).strip(), "how": "mailto", "raw": m.group(0)[:120], "page": page_url})
    for m in re.finditer(r'data-cfemail=["\']([0-9a-fA-F]+)["\']', raw):
        try:
            found.append({"email": decode_cfemail(m.group(1)), "how": "cloudflare data-cfemail", "raw": m.group(1), "page": page_url})
        except Exception:
            pass
    for m in re.finditer(r"[A-Za-z0-9._%+\-]+(?:&#0*64;|&#x0*40;|&commat;)[A-Za-z0-9.\-]+\.[A-Za-z]{2,}", raw):
        found.append({"email": htmlmod.unescape(m.group(0)), "how": "html entity", "raw": m.group(0), "page": page_url})
    text = text if text is not None else BeautifulSoup(raw, "lxml").get_text(" ")
    for m in EMAIL_RE.finditer(text):
        found.append({"email": m.group(0), "how": "plain text", "raw": m.group(0), "page": page_url})
    out, seen = [], set()
    for f in found:
        e = f["email"].strip().strip(".").lower()
        if not EMAIL_RE.fullmatch(e) or BAD_EMAIL.search(e) or e in seen:
            continue
        seen.add(e)
        f["email"] = e
        out.append(f)
    return out


def master_url(u):
    """CMS thumbnail correction per brief."""
    if "wixstatic.com" in u:
        u = re.sub(r"/v1/(?:fill|fit|crop)/[^/]+/[^/]+$", "", u)
    if "squarespace-cdn.com" in u or "squarespace.com" in u:
        u = u.split("?")[0]
    if "/wp-content/uploads/" in u:
        u = re.sub(r"-\d{2,5}x\d{2,5}(?=\.(?:jpe?g|png|webp)(?:$|\?))", "", u, flags=re.I)
        u = re.sub(r"-scaled(?=\.(?:jpe?g|png|webp))", "-scaled", u)
    if "img1.wsimg.com" in u:
        u = u.split("/:/")[0]
    return u


def img_dims(url, session):
    """Fetch the first bytes of an image and read its pixel size."""
    try:
        r = session.get(url, headers={**HDRS, "Range": "bytes=0-131071"}, timeout=20, stream=True)
        if r.status_code not in (200, 206):
            return None
        data = r.raw.read(131072, decode_content=True)
        clen = r.headers.get("Content-Range", "").split("/")[-1] if r.status_code == 206 else r.headers.get("Content-Length")
        r.close()
        from PIL import Image
        try:
            im = Image.open(BytesIO(data))
            return {"w": im.size[0], "h": im.size[1], "bytes": int(clen) if clen and clen.isdigit() else None}
        except Exception:
            return None
    except Exception:
        return None


def collect_imgs(soup, base):
    urls = []
    for im in soup.find_all(["img", "source"]):
        cands = []
        for attr in ("srcset", "data-srcset"):
            if im.get(attr):
                best = None
                for part in im[attr].split(","):
                    bits = part.strip().split()
                    if not bits:
                        continue
                    w = int(re.sub(r"\D", "", bits[1]) or 0) if len(bits) > 1 and bits[1].endswith("w") else 0
                    if best is None or w > best[0]:
                        best = (w, bits[0])
                if best:
                    cands.append(best[1])
        for attr in ("data-src", "data-lazy-src", "data-image", "src"):
            if im.get(attr) and not im[attr].startswith("data:"):
                cands.append(im[attr])
        if cands:
            urls.append(urljoin(base, cands[0]))
    for m in re.finditer(r"url\(['\"]?(https?://[^)'\"]+\.(?:jpe?g|png|webp)[^)'\"]*)", str(soup)):
        urls.append(m.group(1))
    for m in re.finditer(r"https?://static\.wixstatic\.com/media/[A-Za-z0-9_~.\-]+\.(?:jpe?g|png|webp)", str(soup)):
        urls.append(m.group(0))
    out, seen = [], set()
    for u in urls:
        if u not in seen and re.search(r"\.(jpe?g|png|webp)|wixstatic|squarespace-cdn|wsimg|format=", u, re.I):
            seen.add(u)
            out.append(u)
    return out


def detect_platform(raw, headers):
    low = raw.lower()
    gen = re.findall(r'<meta[^>]+name=["\']generator["\'][^>]*content=["\']([^"\']+)', raw, re.I)
    gen += re.findall(r'<meta[^>]+content=["\']([^"\']+)["\'][^>]*name=["\']generator', raw, re.I)
    plat = []
    if "static.wixstatic.com" in low or "_wixcssimports" in low or "wix.com" in low and "x-wix" in str(headers).lower():
        plat.append("Wix")
    if "static1.squarespace.com" in low or "squarespace.com" in low and "squarespace" in " ".join(gen).lower():
        plat.append("Squarespace")
    if "wsimg.com" in low:
        plat.append("GoDaddy")
    if "editmysite.com" in low or "weebly.com" in low:
        plat.append("Weebly")
    if "website-files.com" in low or "webflow" in " ".join(gen).lower():
        plat.append("Webflow")
    if "wp-content" in low or "wp-includes" in low:
        plat.append("WordPress")
    fw = []
    for k, pat in {"Next.js": r"__next_data__|/_next/static", "Gatsby": r"___gatsby", "Nuxt": r"__nuxt",
                   "Framer": r"framerusercontent|framer\.com", "Duda": r"cdn-website\.com",
                   "Shopify": r"cdn\.shopify\.com", "HubSpot CMS": r"hs-sites|hubspot\.net/hub",
                   "Joomla": r"/media/jui/|joomla", "Drupal": r"drupal", "Hostinger Builder": r"zyrosite|hostinger",
                   "Yola": r"yolacdn|yolasite", "Site123": r"site123", "Strikingly": r"strikingly",
                   "Jimdo": r"jimdo", "Carrd": r"carrd\.co", "Netlify": r"netlify", "Tilda": r"tildacdn",
                   "React/Vite SPA": r'<div id="root"></div>|<div id="app"></div>', "Angular": r"ng-version"}.items():
        if re.search(pat, low):
            fw.append(k)
    return plat, fw, gen


def wp_theme_header(raw, base, session):
    m = re.findall(r"/wp-content/themes/([A-Za-z0-9_\-]+)/", raw)
    out = []
    for theme in sorted(set(m))[:3]:
        url = urljoin(base, f"/wp-content/themes/{theme}/style.css")
        try:
            r = session.get(url, headers=HDRS, timeout=15)
            head = r.text[:3000] if r.status_code == 200 else ""
        except Exception:
            head = ""
        fields = {k: (re.search(rf"{k}\s*:\s*(.+)", head, re.I) or [None, ""])[1].strip()[:120]
                  for k in ("Theme Name", "Author", "Author URI", "Template", "Theme URI", "Description")}
        out.append({"theme_dir": theme, "url": url, **fields})
    return out


COMMERCIAL_THEME_AUTHORS = re.compile(
    r"elegant ?themes|brainstorm force|themefusion|elementor|wordpress team|themeisle|kadence|generatepress|tom usborne|"
    r"oceanwp|themeco|themegoods|qode|themify|studiopress|mikado|select-themes|select themes|ux-themes|ux themes|bricks|"
    r"oxygen|creativethemes|themenectar|kriesi|muffin|dream-theme|artbees|undsgn|wpexplorer|porto|athemes|themegrill|"
    r"themeforest|envato|themerex|axiomthemes|ancorathemes|themeum|wpzoom|themes4wp|cyberchimps|themepunch|"
    r"bold themes|boldthemes|thembay|code ?supply|pixelgrade|thrive themes|automattic|anariel|zozothemes|cmsmasters|"
    r"rockethemes|gt3themes|liquid themes|themegoods|fuelthemes|vamtam|nicdark|xtemos|g5theme|themesflat|"
    r"bowthemes|webgeniuslab|designthemes|wpopal|ThemeMove|thememove|iqonic|crumina|edge-themes|edge themes|"
    r"themeszone|themesgrove|ovatheme|theme-junkie|organic themes|meks|hashthemes|sparkle themes|precisionthemes|"
    r"mythemeshop|themepalace|catch themes|blossom themes|rara theme|wen themes|themeinwp|acme themes|"
    r"themesmatic|buzzthemes|themes kingdom|themezaa|themebeans|templatemonster|zemez|jegtheme|"
    r"designwall|wpbakery|beaver builder|fastlinemedia|astra|hello elementor|underscores|_s|the7|enfold|avada|divi|"
    r"betheme|salient|uncode|flatsome|bridge|x theme|pro theme", re.I)


def check_site(c):
    s = requests.Session()
    res = {"id": c["id"], "name": c["name"], "input_url": c["website"], "fetch_date": TODAY,
           "vantage": "US (Columbus, OH egress via agent proxy)"}
    url = clean_url(c["website"])
    if urlparse(url).hostname and any(urlparse(url).hostname.endswith(sd) for sd in SOCIAL):
        res.update(g2="FAIL", g2_reason=f"website field is a social/directory page: {url}")
        return res
    raw, route, status, final, err = None, None, None, None, None
    try:
        r, chain, secs = fetch(url, s)
        status, final, raw, route = r.status_code, r.url, r.text, ("Chromium render (Playwright, US egress), redirects followed"
                                                                   if RENDER else "python-requests GET (Chrome UA), redirects followed")
        res["redirect_chain"] = chain
        res["headers"] = {k: v for k, v in r.headers.items() if k.lower() in ("server", "x-powered-by", "x-generator", "x-wix-request-id", "x-served-by", "via", "x-hosted-by")}
        res["load_secs"] = secs
    except Exception as e:
        err = f"{type(e).__name__}: {str(e)[:200]}"
    if not RENDER and (raw is None or status >= 400) or (not RENDER and raw and re.search(r"just a moment|cf-chl|challenge-platform|attention required", raw[:5000], re.I)):
        res["route1_error"] = err or f"HTTP {status}"
        try:
            code, eff, body, cerr = curl_fetch(url)
            res["route2"] = f"curl -L (Safari UA): HTTP {code} {eff} {cerr}"
            if code and code < 400 and body:
                status, final, raw, route = code, eff, body, "curl -L (Safari UA), redirects followed (retry route)"
        except Exception as e:
            res["route2"] = f"curl error {e}"
    res["g2_route"] = route
    if raw is None or status is None or status >= 400:
        res.update(g2="RETRY_BROWSER", g2_reason=f"route1 {res.get('route1_error')}; route2 {res.get('route2')}")
        return res
    res.update(final_url=final, http_status=status)
    low = re.sub(r"[A-Za-z0-9+/=]{120,}", " ", raw.lower())
    soup = BeautifulSoup(raw, "lxml")
    title = (soup.title.get_text(strip=True) if soup.title else "")[:200]
    res["title"] = title
    visible = soup.get_text(" ", strip=True)
    res["home_text_len"] = len(visible)
    for pat in PARKED:
        if re.search(pat, low[:20000]) and len(visible) < 3000:
            res.update(g2="FAIL", g2_reason=f"parked/placeholder page matched '{pat}'")
            return res
    if root_domain(final) != root_domain(url):
        res["g2_cross_domain"] = f"{root_domain(url)} -> {root_domain(final)}"
        if any(root_domain(final).endswith(sd) for sd in SOCIAL):
            res.update(g2="FAIL", g2_reason=f"redirects to social/directory {final}")
            return res
    res["g2"] = "PASS"

    # ---------- gather extra pages ----------
    links = {}
    for a in soup.find_all("a", href=True):
        href = urljoin(final, a["href"].strip())
        if root_domain(href) != root_domain(final):
            continue
        txt = (a.get_text(" ", strip=True) + " " + href).lower()
        for key, pat in {"contact": r"contact", "about": r"about|our-story|our story|who-we-are|meet|team|owner",
                         "gallery": r"gallery|portfolio|project|our-work|our work|photos|before|recent work"}.items():
            if re.search(pat, txt) and key + "s" not in links:
                links.setdefault(key, [])
                if href not in links[key] and len(links[key]) < 3:
                    links[key].append(href.split("#")[0])
    pages = {"home": [(final, raw)]}
    extra = []
    for key in ("contact", "about", "gallery"):
        for u in links.get(key, [])[:2]:
            extra.append((key, u))
    base = f"{urlparse(final).scheme}://{urlparse(final).netloc}"
    for path in ("/privacy", "/privacy-policy", "/terms"):
        extra.append(("legal", base + path))
    fetched = set([final])
    for key, u in extra:
        if u in fetched:
            continue
        fetched.add(u)
        try:
            rr = page_get(s, u)
            if rr.status_code == 200 and "html" in rr.headers.get("Content-Type", "html"):
                if key == "legal" and root_domain(rr.url) != root_domain(final):
                    continue
                pages.setdefault(key, []).append((rr.url, rr.text))
        except Exception:
            pass
    res["pages_fetched"] = {k: [u for u, _ in v] for k, v in pages.items()}
    allraw = "\n".join(t for v in pages.values() for _, t in v)
    alllow = allraw.lower()

    # ---------- G3 ----------
    plat, fw, gen = detect_platform(raw, res.get("headers", {}))
    res.update(platform=plat, frameworks=fw, generator=gen)
    scripts = sorted(set(urlparse(urljoin(final, m)).hostname or "" for m in re.findall(r'<script[^>]+src=["\']([^"\']+)', raw, re.I)))
    res["script_domains"] = scripts
    vend = []
    for v, pats in VENDORS.items():
        for p in pats:
            m = re.search(p, low)
            if m:
                vend.append({"vendor": v, "match": low[max(0, m.start() - 60): m.end() + 60]})
                break
    credits = []
    footer_html = ""
    for tag in soup.find_all(["footer"]) or []:
        footer_html += str(tag)
    tail = raw[-25000:]
    for src in (footer_html, tail, " ".join(gen)):
        for m in CREDIT_RE.finditer(src):
            name = re.sub(r"\s+", " ", BeautifulSoup(m.group(1), "lxml").get_text(" ")).strip(" .,-|")
            ctx = re.sub(r"<[^>]+>", " ", src[max(0, m.start() - 40): m.end() + 80])
            ctx = re.sub(r"\s+", " ", htmlmod.unescape(ctx)).strip()
            if re.match(r"(appointment|the|our|a|an|you|your|homeowner|licensed|google|recaptcha)\b", name, re.I):
                if not re.search(r"(website|site|web design|designed|developed|marketing)\s+by", ctx, re.I):
                    continue
            if PLATFORM_WORDS.match(name):
                continue
            credits.append({"credit": name[:60], "context": ctx[:200]})
    # dedupe credits
    seen = set()
    res["credits"] = [cr for cr in credits if not (cr["credit"].lower() in seen or seen.add(cr["credit"].lower()))]
    res["vendor_hits"] = vend
    res["wp_theme"] = wp_theme_header(raw, final, s) if "WordPress" in plat else []
    agency_theme = [t for t in res["wp_theme"] if t.get("Author") and not COMMERCIAL_THEME_AUTHORS.search(
        t.get("Author", "") + " " + t.get("Theme Name", "") + " " + t.get("Template", ""))]
    res["wp_theme_noncommercial"] = agency_theme

    # ---------- G5 site signals ----------
    fr = [f for f in FRANCHISE if f in alllow]
    frp = [p for p in FRANCHISE_PHRASES if re.search(p, alllow)]
    res["franchise_hits"] = fr
    res["franchise_phrases"] = frp

    # ---------- niche ----------
    res["niche_counts"] = {"kitchen": len(re.findall(r"\bkitchens?\b", visible.lower())),
                           "bath": len(re.findall(r"\bbath(?:room)?s?\b", visible.lower())),
                           **{k: len(re.findall(p, visible.lower())) for k, p in NOT_NICHE.items()}}

    # ---------- G6 ----------
    parsed = {}
    for key, lst in pages.items():
        for u, t in lst:
            sp = soup if u == final else BeautifulSoup(t, "lxml")
            parsed[u] = (sp, sp.get_text("\n", strip=True))
    emails = []
    for key, lst in pages.items():
        for u, t in lst:
            emails += find_emails(t, u, parsed[u][1])
    seen = set()
    res["emails"] = [e for e in emails if not (e["email"] in seen or seen.add(e["email"]))]
    dm = []
    for key, lst in pages.items():
        if key == "legal":
            continue
        for u, t in lst:
            txt = parsed[u][1]
            for m in DM_RE.finditer(txt):
                snippet = re.sub(r"\s+", " ", m.group(1)).strip()
                if re.search(r"homeowner|owner'?s manual|ownership|owners?\b(?! and)", snippet, re.I) and not re.search(
                        r"\b(founder|president|ceo|principal|proprietor|owned and operated by|founded by|co-owner|owner,|owner/|owner of|owner and|is the owner|our owner)\b", snippet, re.I):
                    continue
                dm.append({"page": u, "snippet": snippet[:240]})
    res["dm_snippets"] = dm[:15]
    fb = sorted(set(re.findall(r"https?://(?:www\.)?facebook\.com/[A-Za-z0-9_.\-/?=]+", raw)))
    ig = sorted(set(re.findall(r"https?://(?:www\.)?instagram\.com/[A-Za-z0-9_.\-]+", raw)))
    res["facebook_links"] = [f for f in fb if not re.search(r"sharer|plugins|tr\?|dialog", f)][:5]
    res["instagram_links"] = ig[:5]
    res["tel_links"] = sorted(set(re.findall(r'href=["\']tel:([^"\']*)', allraw, re.I)))[:10]
    res["mailto_links"] = sorted(set(re.findall(r'href=["\']mailto:([^"\']*)', allraw, re.I)))[:10]

    # ---------- G7 ----------
    imgs = []
    for key in ("home", "gallery"):
        for u, t in pages.get(key, []):
            for iu in collect_imgs(parsed[u][0], u):
                imgs.append((key, iu))
    cand, seen = [], set()
    for key, iu in imgs:
        mu = master_url(iu)
        if mu in seen:
            continue
        seen.add(mu)
        cand.append({"served": iu, "master": mu, "page": key, "stock_sig": bool(STOCK.search(mu)), "skip_sig": bool(SKIPIMG.search(mu.split("/")[-1]))})
    res["img_candidates"] = len(cand)
    good, served_sizes = [], []
    tries = 0
    for ci in cand:
        if ci["stock_sig"] or ci["skip_sig"]:
            continue
        tries += 1
        if tries > 30:
            break
        d = img_dims(ci["master"], s)
        if d is None and ci["master"] != ci["served"]:
            d = img_dims(ci["served"], s)
            if d:
                ci["master"] = ci["served"]
        if d:
            ci.update(d)
            if d["w"] >= 800:
                good.append(ci)
        if len(good) >= 10:
            break
    res["imgs_800"] = good
    res["imgs_stock"] = [ci["master"] for ci in cand if ci["stock_sig"]][:10]
    # served image byte sizes (G8 defect: gallery images over 1MB)
    for ci in cand[:20]:
        if ci["stock_sig"] or ci["skip_sig"]:
            continue
        try:
            h = s.head(ci["served"], headers=HDRS, timeout=15, allow_redirects=True)
            cl = h.headers.get("Content-Length")
            if cl and cl.isdigit():
                served_sizes.append({"url": ci["served"], "bytes": int(cl), "page": ci["page"]})
        except Exception:
            pass
    res["served_sizes_over_1mb"] = [x for x in served_sizes if x["bytes"] > 1_000_000]

    # ---------- G8 static ----------
    res["viewport_meta"] = bool(re.search(r'<meta[^>]+name=["\']viewport["\']', raw, re.I))
    res["final_scheme"] = urlparse(final).scheme
    https_check = {}
    try:
        hr = s.get("https://" + urlparse(final).netloc + "/", headers=HDRS, timeout=20)
        https_check = {"https_status": hr.status_code}
    except requests.exceptions.SSLError as e:
        https_check = {"https_error": "SSLError: " + str(e)[:200]}
    except Exception as e:
        https_check = {"https_error": f"{type(e).__name__}: {str(e)[:200]}"}
    res["https_check"] = https_check

    # ---------- G9 raw html ----------
    pix = []
    for k, p in PIXELS.items():
        m = re.search(p, allraw, re.I)
        if m:
            pix.append({"signal": k, "snippet": re.sub(r"\s+", " ", allraw[max(0, m.start() - 80): m.end() + 60])[:220]})
    res["paid_signals_raw"] = pix
    res["gtm"] = sorted(set(re.findall(r"GTM-[A-Z0-9]{4,9}", raw)))
    # dated content for G4 (WordPress REST / RSS)
    res["dated_content"] = dated_content(final, raw, plat, s)
    return res


def dated_content(final, raw, plat, s):
    base = f"{urlparse(final).scheme}://{urlparse(final).netloc}"
    out = []
    if "WordPress" in plat:
        for typ in ("posts", "pages", "project", "projects", "portfolio", "gallery"):
            try:
                r = s.get(f"{base}/wp-json/wp/v2/{typ}?per_page=3&orderby=date&_fields=date,link,title,type",
                          headers=HDRS, timeout=15)
                if r.status_code == 200 and r.text.strip().startswith("["):
                    for it in r.json()[:3]:
                        out.append({"src": f"wp-json/{typ}", "date": it.get("date"), "link": it.get("link"),
                                    "title": (it.get("title") or {}).get("rendered", "")[:100]})
            except Exception:
                pass
    feeds = [base + "/blog-feed.xml", base + "/feed/", base + "/blog?format=rss", base + "/rss.xml"]
    for m in re.findall(r'<link[^>]+type=["\']application/rss\+xml["\'][^>]*href=["\']([^"\']+)', raw, re.I):
        feeds.insert(0, urljoin(final, m))
    for f in dict.fromkeys(feeds):
        try:
            r = s.get(f, headers=HDRS, timeout=15)
            if r.status_code == 200 and "<rss" in r.text[:500].lower() or "<feed" in r.text[:500].lower():
                for it in re.findall(r"<item>([\s\S]*?)</item>", r.text)[:3]:
                    d = re.search(r"<pubDate>([^<]+)</pubDate>", it)
                    l = re.search(r"<link>([^<]+)</link>", it)
                    t = re.search(r"<title>(?:<!\[CDATA\[)?([^<\]]+)", it)
                    out.append({"src": "rss:" + f, "date": d.group(1) if d else None, "link": l.group(1) if l else None,
                                "title": t.group(1)[:100] if t else ""})
                if out:
                    break
        except Exception:
            pass
    return out


def run(c):
    try:
        return check_site(c)
    except Exception as e:
        return {"id": c["id"], "name": c["name"], "input_url": c["website"], "g2": "ERROR", "g2_reason": repr(e)[:300]}


def main():
    inp, outp = sys.argv[1], sys.argv[2]
    workers = int(sys.argv[3]) if len(sys.argv) > 3 else 12
    cands = [json.loads(l) for l in open(inp)]
    done = set()
    try:
        done = {json.loads(l)["id"] for l in open(outp)}
    except FileNotFoundError:
        pass
    todo = [c for c in cands if c["id"] not in done]
    print(f"{len(todo)} to check", file=sys.stderr)

    with ProcessPoolExecutor(workers) as ex, open(outp, "a") as fo:
        for i, r in enumerate(ex.map(run, todo)):
            fo.write(json.dumps(r) + "\n")
            fo.flush()
            if i % 25 == 0:
                print(i, r.get("name"), r.get("g2"), file=sys.stderr)


if __name__ == "__main__":
    main()
