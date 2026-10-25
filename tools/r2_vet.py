#!/usr/bin/env python3
"""Vet round 2 candidates (task 3 results plus the 34 already qualified) before the final pick.
Per candidate: email syntax and domain MX (dns.google), the quote contains the email, the email source is not a
people-search site, how well each social URL and the email match the business name, and whether any website on the
email's own domain or the reported dead site loads (HTTP fetch). Writes data/r2/vetted.json with a status per row:
  pass   email MX ok, quote ok, social matches the name (or Gemini's notes confirm it), no live site
  check  email ok but the social link does not obviously match the business (Gemini's match needs a second look)
  fail   bad email source, made-up email, no MX, or a live website
The email's source page is fetched where possible (not Facebook/Instagram) and must show the email.
Usage: r2_vet.py"""
import csv, json, re, sys, urllib.request, concurrent.futures as cf

D = "/home/user/100homeimprovementsearch/data/r2"
BAD_SRC = re.compile(r"contactout|rocketreach|zoominfo|whitepages|truepeople|fastpeople|peoplesearch|unmask|checkpeople|leadiq|"
                     r"aeroleads|signalhire|apollo\.io|lusha|spokeo|fastbackground|nationalpublicdata|familytreenow|idcrawl|"
                     r"clustrmaps|radaris|beenverified|peoplefinder", re.I)
FREE = {"gmail.com", "yahoo.com", "aol.com", "hotmail.com", "outlook.com", "icloud.com", "comcast.net", "bellsouth.net",
        "att.net", "live.com", "msn.com", "me.com", "verizon.net", "cox.net", "charter.net", "sbcglobal.net", "ymail.com",
        "frontier.com", "windstream.net", "centurylink.net", "earthlink.net", "mail.com", "protonmail.com", "q.com",
        "juno.com", "ptd.net", "xecu.net", "netzero.net", "frontiernet.net", "embarqmail.com", "suddenlink.net",
        "roadrunner.com", "rr.com", "twc.com", "optonline.net", "mchsi.com", "tds.net", "mediacombb.net", "zoominternet.net",
        "wowway.com", "rocketmail.com", "aim.com", "gmx.com", "zoho.com", "bresnan.net", "cableone.net", "sparklight.net"}
# directory and social pages that Gemini sometimes reports as a website
NOT_SITE = re.compile(r"birdeye|yelp|houzz|bbb\.org|angi\.com|homeadvisor|thumbtack|manta|cybo|chamberofcommerce|yellowpages|"
                      r"facebook|instagram|linktr|nextdoor|porch|buildzoom|google\.|mapquest|superpages|nearbyon|wanderboat|"
                      r"showmelocal|brownbook|alignable|bizapedia|opencorporates|dandb|zoominfo|loc8|cylex|maptons|"
                      r"tiktok|youtube|pinterest|x\.com|twitter", re.I)
FAKE = re.compile(r"^(john|jane)\.?doe@|@(company|example|domain|email|yourdomain|website)\.(com|net|org)$", re.I)
STOP = {"llc", "inc", "co", "the", "and", "of", "corp", "company", "services", "service", "home", "construction",
        "remodeling", "kitchen", "kitchens", "bath", "baths", "bathroom", "design", "custom", "tile", "cabinets",
        "cabinet", "granite", "stone", "renovations", "renovation", "improvement", "improvements", "group", "llc."}


def k(v):
    return v if v and v.strip().upper() not in ("UNKNOWN", "NONE", "N/A", "") else ""


def tokens(s):
    return {t for t in re.findall(r"[a-z0-9]+", s.lower()) if len(t) > 2}


def key_tokens(name):
    t = tokens(name)
    return (t - STOP) or t


def match(name, url):
    """share of the business name's distinctive words that appear in the URL slug (letters only, no spaces)"""
    if not url:
        return 0.0
    slug = re.sub(r"[^a-z0-9]", "", url.lower().split(".com/", 1)[-1])
    kt = key_tokens(name)
    return sum(1 for t in kt if t in slug) / max(1, len(kt))


def mx(domain):
    try:
        j = json.load(urllib.request.urlopen(f"https://dns.google/resolve?name={domain}&type=MX", timeout=20))
        return bool(j.get("Answer"))
    except Exception:
        return None


def live(url):
    """True when the page loads with real content that is not a parked, expired or placeholder page"""
    if not url:
        return False
    u = url if url.startswith("http") else "https://" + url
    try:
        req = urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/141.0"})
        r = urllib.request.urlopen(req, timeout=20)
        body = r.read(400000).decode("utf-8", "ignore")
    except Exception:
        return False
    if re.search(r"facebook\.com|instagram\.com", r.geturl()):
        return False
    low = body.lower()
    if len(body) < 3000 or re.search(r"coming soon|launching soon|domain (is )?(for sale|parked)|parked free|"
                                     r"website expired|isn.t connected|reconnect your domain|buy this domain|"
                                     r"suspendedpage|account suspended|lander|hugedomains|sedo|godaddy\.com/forsale", low):
        return False
    return True


def source_check(url, email):
    """verified: the source page shows the email; missing: the page loads but the email is not on it;
    unfetchable: login wall (Facebook, Instagram), PDF or blocked"""
    if not url or re.search(r"facebook\.com|instagram\.com|google\.com/maps", url):
        return "unfetchable"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/141.0"})
        r = urllib.request.urlopen(req, timeout=25)
        if "pdf" in (r.headers.get("Content-Type") or ""):
            return "unfetchable"
        body = r.read(3000000).decode("utf-8", "ignore")
    except Exception:
        return "unfetchable"
    if len(body) < 2000:
        return "unfetchable"
    low = re.sub(r"\s+", "", body.lower()).replace("[at]", "@").replace("(at)", "@").replace("&#64;", "@")
    return "verified" if email.lower() in low else "missing"


rows = []
for r in csv.DictReader(open(f"{D}/gemini_in/task3_all.csv", encoding="utf-8-sig")):
    if k(r["email"]) and (k(r["facebook_url"]) or k(r["instagram_url"])) and r["website_status"].strip().lower() != "live":
        rows.append({**r, "origin": "task3"})
for q in json.load(open(f"{D}/qualified.json")):
    rows.append({"row": q["row"], "business_name": q["business_name"], "email": q["email"], "email_source_url": q["email_source_url"],
                 "email_source_quote": q.get("email_source_quote", q["email"]), "facebook_url": q["facebook_url"],
                 "instagram_url": q["instagram_url"], "website_found": q.get("website", ""), "website_status": "", "notes": q.get("note", ""),
                 "origin": "qualified34"})
seen = {}
for r in rows:  # task 3 is newer; the 34 keep their earlier verified values unless task 3 re-found them
    seen.setdefault(r["row"], r)
rows = list(seen.values())


def vet(r):
    e = r["email"].strip().strip(".").replace(" ", "")
    dom = e.split("@")[-1].lower()
    out = {"row": r["row"], "business_name": r["business_name"], "email": e, "origin": r["origin"],
           "facebook_url": k(r["facebook_url"]), "instagram_url": k(r["instagram_url"]),
           "email_source_url": r["email_source_url"], "email_source_quote": r["email_source_quote"],
           "website_found": k(r["website_found"]), "notes": r.get("notes", "")}
    out["email_ok"] = bool(re.fullmatch(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", e))
    out["mx"] = mx(dom) if out["email_ok"] else False
    out["quote_has_email"] = e.lower() in re.sub(r"\s+", "", (r["email_source_quote"] or "").lower()) or r["origin"] == "qualified34"
    out["bad_source"] = bool(BAD_SRC.search(r["email_source_url"] or ""))
    out["fb_match"] = round(match(r["business_name"], out["facebook_url"]), 2)
    out["ig_match"] = round(match(r["business_name"], out["instagram_url"]), 2)
    out["email_match"] = round(match(r["business_name"], e.split("@")[0] + " " + (dom if dom not in FREE else "")), 2)
    # a live site on the email's own domain or at the reported website means the business has a website
    sites = {out["website_found"]} if out["website_found"] and not NOT_SITE.search(out["website_found"]) else set()
    if dom not in FREE:
        sites.add(dom)
    out["fake_email"] = bool(FAKE.search(e))
    out["source_check"] = source_check(r["email_source_url"], e)
    out["live_site"] = next((s for s in sites if live(s)), "")
    social_ok = max(out["fb_match"], out["ig_match"]) >= 0.5 or r["origin"] == "qualified34"
    if out["bad_source"] or not out["mx"] or not out["email_ok"] or out["live_site"] or out["fake_email"]:
        out["status"] = "fail"
    elif out["source_check"] == "missing":
        out["status"] = "check"  # the source page loads but does not show the email
    elif social_ok and (out["source_check"] == "verified" or out["quote_has_email"]):
        out["status"] = "pass"
    else:
        out["status"] = "check"
    return out


with cf.ThreadPoolExecutor(12) as ex:
    res = list(ex.map(vet, rows))
json.dump(res, open(f"{D}/vetted.json", "w"), indent=1)
from collections import Counter
print(len(res), Counter(x["status"] for x in res), "live site", sum(1 for x in res if x["live_site"]),
      "no mx", sum(1 for x in res if not x["mx"]), "bad src", sum(1 for x in res if x["bad_source"]))
