#!/usr/bin/env python3
"""Find kitchen and bath businesses on Google Maps that have no website, and keep only the ones worth building a
homepage for. Runs on your own laptop in a normal, visible Chrome window, at a human pace.

What it does
  1. For every "category in town" search (categories.txt x towns.txt) it opens Google Maps, scrolls the results list
     and collects each business.
  2. Opens each business once and reads: name, category, rating, number of reviews, address, phone, website, hours,
     open or closed, "From the business" text.
  3. Quick filter (no extra clicks): no website of its own (a Facebook/Instagram/Linktree link is fine), open,
     rating >= MIN_RATING, reviews >= MIN_REVIEWS, a kitchen / bath / remodeling category.
  4. For businesses that pass: reads the newest reviews (name, stars, date, text) and requires a review within
     MAX_NEWEST_REVIEW_MONTHS; then collects the photos and requires at least MIN_PHOTOS; downloads them full size.
  5. Writes everything as it goes, so you can stop (Ctrl+C) and start again; finished searches and businesses are skipped.

Output (folder "maps_out" next to this script)
  leads_all.csv          every business seen, with PASS / FAIL and the reason
  qualified/<slug>/      place.json, reviews.json, images/ for every business that passed
  progress.log           what happened, line by line

If Google shows a "unusual traffic" / CAPTCHA page, the script stops: with you at the laptop it waits for you to solve
it and press Enter; overnight (--unattended) it waits 20, 40, then 60 minutes and tries again. It never tries to hide
or get around the check. Overnight it also restarts Chrome if it crashes, and with --drive-folder it zips the results
into your Google Drive for desktop folder every --upload-every businesses (same file name, so the shared link always
opens the newest results).

Setup (once)
  pip install playwright
  python -m playwright install chromium
Run
  python maps_leads.py                     (uses categories.txt and towns.txt)
  python maps_leads.py --max-per-search 40 --limit-searches 10   (a small test run first)
  python maps_leads.py --unattended --drive-folder "G:/My Drive/maps_leads"   (overnight)
"""
import argparse, csv, json, os, random, re, sys, time, urllib.request
from pathlib import Path
from urllib.parse import quote_plus, urlparse

from playwright.sync_api import sync_playwright, TimeoutError as PWTimeout

# ---- criteria (edit here) -------------------------------------------------------------------------------------
MIN_RATING = 4.5
MIN_REVIEWS = 15
MAX_NEWEST_REVIEW_MONTHS = 6
MIN_PHOTOS = 10
MAX_PHOTOS = 30
MAX_REVIEWS = 10
KB_WORDS = re.compile(r"kitchen|bath|remodel|renovat|tile|cabinet|countertop|granite|marble|quartz|stone|"
                      r"shower|flooring|contractor|home improvement|handyman|carpent", re.I)
# a listing whose website is one of these still counts as "no website"
SOCIAL = re.compile(r"facebook\.com|fb\.com|instagram\.com|linktr\.ee|linktree|yelp\.|houzz\.|nextdoor\.|"
                    r"thumbtack\.|angi\.com|homeadvisor\.|bbb\.org|google\.|business\.site|tiktok\.com", re.I)

HERE = Path(__file__).resolve().parent
OUT = HERE / "maps_out"
QUAL = OUT / "qualified"
ALL_CSV = OUT / "leads_all.csv"
DONE_SEARCHES = OUT / "done_searches.txt"
LOG = OUT / "progress.log"
COLS = ["place_key", "verdict", "reason", "name", "category", "rating", "reviews", "phone", "address", "website",
        "newest_review_months", "photos", "email_on_google", "facebook", "instagram", "maps_url", "search"]
EMAIL_TODO = OUT / "email_todo.csv"
# businesses researched in earlier rounds: skipped by phone (file next to this script)
SKIP_FILE = HERE / "already_researched_homeliving.csv"
SKIP_PHONES = set()
if SKIP_FILE.exists():
    with open(SKIP_FILE, newline="", encoding="utf-8") as f:
        SKIP_PHONES = {re.sub(r"\D", "", r.get("phone") or "")[-10:] for r in csv.DictReader(f)} - {""}
EMAIL_RE = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")


def log(msg):
    line = time.strftime("%H:%M:%S ") + msg
    print(line, flush=True)
    with open(LOG, "a", encoding="utf-8") as f:
        f.write(line + "\n")


def pause(a=1.5, b=3.5):
    time.sleep(random.uniform(a, b))


def slug(s):
    return re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", s.lower())).strip("-")[:60] or "business"


def place_key(url):
    m = re.search(r"!1s(0x[0-9a-f]+:0x[0-9a-f]+)", url) or re.search(r"[?&]cid=(\d+)", url)
    return m.group(1) if m else url.split("?")[0]


def months_ago(text):
    m = re.search(r"(\d+|a|an)\s+(minute|hour|day|week|month|year)", text or "")
    if not m:
        return None
    n = 1 if m.group(1) in ("a", "an") else int(m.group(1))
    return {"minute": 0, "hour": 0, "day": n / 30, "week": n / 4.3, "month": n, "year": n * 12}[m.group(2)]


UNATTENDED = False
BLOCKS = [0]


def blocked(page):
    return "/sorry/" in page.url or "unusual traffic" in (page.content()[:20000]).lower()


def wait_if_blocked(page):
    """Google sometimes asks for a human check. Attended: you solve it and press Enter. Unattended (overnight):
    the script stops working and waits (20 min, then 40, then 60) before trying again. It never tries to get
    around the check."""
    while blocked(page):
        if not UNATTENDED:
            log("Google is asking for a check. Solve it in the browser window, then press Enter here.")
            input()
        else:
            BLOCKS[0] += 1
            wait = min(60, 20 * BLOCKS[0])
            log(f"Google is asking for a check: waiting {wait} minutes before trying again (you can also solve it in the window)")
            for _ in range(wait * 6):
                time.sleep(10)
                try:
                    if not blocked(page):
                        break
                except Exception:
                    break
            try:
                page.reload(wait_until="domcontentloaded")
            except Exception:
                pass
        pause()
    BLOCKS[0] = 0


def accept_consent(page):
    if "consent.google" in page.url:
        for label in ("Accept all", "Reject all", "I agree"):
            b = page.get_by_role("button", name=label)
            if b.count():
                b.first.click()
                pause()
                return


def load_seen():
    seen = {}
    if ALL_CSV.exists():
        with open(ALL_CSV, newline="", encoding="utf-8") as f:
            for r in csv.DictReader(f):
                seen[r["place_key"]] = r["verdict"]
    return seen


def write_row(row):
    new = not ALL_CSV.exists()
    with open(ALL_CSV, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=COLS)
        if new:
            w.writeheader()
        w.writerow({k: row.get(k, "") for k in COLS})


# ---- Google Maps pages ------------------------------------------------------------------------------------------
def search_results(page, query, max_results):
    page.goto(f"https://www.google.com/maps/search/{quote_plus(query)}?hl=en&gl=us", wait_until="domcontentloaded")
    accept_consent(page)
    wait_if_blocked(page)
    try:
        page.wait_for_selector('div[role="feed"], h1.DUwDvf', timeout=20000)
    except PWTimeout:
        log(f"  no results list for: {query}")
        return []
    if not page.query_selector('div[role="feed"]'):  # the search went straight to one business
        return [page.url]
    links, stale = {}, 0
    while len(links) < max_results and stale < 4:
        before = len(links)
        for a in page.query_selector_all('div[role="feed"] a.hfpxzc'):
            href = a.get_attribute("href")
            if href:
                links.setdefault(place_key(href), href)
        page.eval_on_selector('div[role="feed"]', "f => f.scrollBy(0, 2500)")
        pause(1.2, 2.2)
        end = page.query_selector("text=You've reached the end of the list")
        stale = stale + 1 if len(links) == before else 0
        if end:
            break
    return list(links.values())[:max_results]


PLACE_JS = r"""() => {
  const q = s => document.querySelector(s);
  const t = s => (q(s) || {}).innerText || '';
  const main = q('div[role=main]') || document.body;
  const ratingBox = t('div.F7nice');
  const web = q('a[data-item-id="authority"]');
  const phone = q('button[data-item-id^="phone:tel:"]');
  const hours = [...main.querySelectorAll('table tr')].map(tr => tr.innerText.replace(/\s+/g, ' ').trim()).filter(Boolean);
  return {
    name: t('h1.DUwDvf'),
    category: t('button.DkEaL'),
    rating_box: ratingBox,
    address: t('button[data-item-id="address"]').replace(/^\W+/, ''),
    phone: phone ? phone.getAttribute('data-item-id').replace('phone:tel:', '') : '',
    website: web ? web.href : '',
    closed: /Permanently closed|Temporarily closed/i.test(main.innerText.slice(0, 3000)),
    socials: [...new Set([...main.querySelectorAll('a[href]')].map(a => a.href).filter(h => /facebook\.com|instagram\.com/.test(h)))],
    hours,
    overview: main.innerText.slice(0, 4000),
  };
}"""


def read_place(page, url):
    page.goto(url if "hl=en" in url else url + ("&" if "?" in url else "?") + "hl=en", wait_until="domcontentloaded")
    wait_if_blocked(page)
    page.wait_for_selector("h1.DUwDvf", timeout=20000)
    pause(1.0, 2.0)
    d = page.evaluate(PLACE_JS)
    m = re.search(r"([\d.]+)\s*\(([\d,]+)\)", d["rating_box"].replace("\n", " "))
    d["rating"] = float(m.group(1)) if m else None
    d["reviews"] = int(m.group(2).replace(",", "")) if m else 0
    d["maps_url"] = page.url
    return d


def open_tab(page, name):
    tab = page.query_selector(f'button[role="tab"]:has-text("{name}")')
    if not tab:
        return False
    tab.click()
    pause(1.5, 2.5)
    return True


def read_reviews(page, n):
    if not open_tab(page, "Reviews"):
        return []
    try:  # newest first
        page.click('button[aria-label*="Sort"]', timeout=5000)
        pause(0.8, 1.5)
        page.click('div[role="menuitemradio"]:has-text("Newest")', timeout=5000)
        pause(1.5, 2.5)
    except PWTimeout:
        pass
    for _ in range(6):
        page.evaluate("""() => { const s = [...document.querySelectorAll('div.m6QErb')].find(e => e.scrollHeight > e.clientHeight + 50);
                                 if (s) s.scrollBy(0, 3000); }""")
        pause(1.0, 1.8)
        if len(page.query_selector_all("div.jftiEf")) >= n:
            break
    for b in page.query_selector_all("button.w8nwRe"):  # "More" on long reviews
        try:
            b.click()
        except Exception:
            pass
    return page.evaluate(r"""(n) => [...document.querySelectorAll('div.jftiEf')].slice(0, n).map(r => ({
        reviewer: (r.querySelector('.d4r55') || {}).innerText || '',
        stars: ((r.querySelector('span.kvMYJc') || {getAttribute: () => ''}).getAttribute('aria-label') || ''),
        when: (r.querySelector('span.rsqaWe') || {}).innerText || '',
        text: (r.querySelector('span.wiI7pd') || {}).innerText || '',
        owner_reply: ((r.querySelector('div.CDe7pd') || {}).innerText || '').slice(0, 1500),
    }))""", n)


def read_photos(page, n):
    btn = page.query_selector('button[aria-label^="Photo of"], button[jsaction*="heroHeaderImage"]')
    if not btn:
        return []
    btn.click()
    pause(2.0, 3.0)
    urls = []
    for _ in range(8):
        found = page.evaluate(r"""() => {
            const out = new Set();
            document.querySelectorAll('[style*="googleusercontent"], img[src*="googleusercontent"]').forEach(e => {
              const m = (e.getAttribute('style') || '').match(/url\(["']?(https:[^"')]+)/);
              const u = m ? m[1] : e.getAttribute('src');
              if (u && /googleusercontent\.com\/(p|gps-cs|geougc|gps-proxy)/.test(u)) out.add(u);
            });
            return [...out];
        }""")
        for u in found:
            full = re.sub(r"=[swh]\d+[^/]*$", "", u) + "=s1600"
            if full not in urls:
                urls.append(full)
        if len(urls) >= n:
            break
        page.mouse.wheel(0, 2500)
        pause(1.0, 1.8)
    page.keyboard.press("Escape")
    return urls[:n]


def download(url, path):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        data = urllib.request.urlopen(req, timeout=40).read()
        if len(data) > 8000:
            path.write_bytes(data)
            return True
    except Exception:
        pass
    return False


def check_business(page, url, search):
    """Open one listing, apply the criteria, and save everything for a business that passes."""
    d = read_place(page, url)
    row = {"search": search, **{k: d.get(k, "") for k in ("name", "category", "rating", "reviews", "phone", "address", "website", "maps_url")}}
    socials = d.get("socials") or []
    if d.get("website") and re.search(r"facebook\.com|instagram\.com", d["website"]):
        socials.append(d["website"])
    row["facebook"] = next((u for u in socials if "facebook.com" in u), "")
    row["instagram"] = next((u for u in socials if "instagram.com" in u), "")
    row["email_on_google"] = ", ".join(sorted(set(EMAIL_RE.findall(d.get("overview", "")))))
    site = d["website"]
    reason = ""
    if re.sub(r"\D", "", d.get("phone") or "")[-10:] in SKIP_PHONES:
        reason = "already researched in an earlier round"
    elif site and not SOCIAL.search(urlparse(site).netloc + urlparse(site).path):
        reason = f"has a website ({urlparse(site).netloc})"
    elif d["closed"]:
        reason = "closed"
    elif not d["rating"] or d["rating"] < MIN_RATING:
        reason = f"rating {d['rating']}"
    elif d["reviews"] < MIN_REVIEWS:
        reason = f"{d['reviews']} reviews"
    elif not KB_WORDS.search(d["category"] + " " + d["name"]):
        reason = f"category {d['category']}"
    reviews, photos = [], []
    if not reason:
        reviews = read_reviews(page, MAX_REVIEWS)
        ages = [m for m in (months_ago(r["when"]) for r in reviews) if m is not None]
        row["newest_review_months"] = round(min(ages), 1) if ages else ""
        if not ages or min(ages) > MAX_NEWEST_REVIEW_MONTHS:
            reason = "no review in the last %d months" % MAX_NEWEST_REVIEW_MONTHS
    if not reason:
        page.goto(d["maps_url"], wait_until="domcontentloaded")
        wait_if_blocked(page)
        page.wait_for_selector("h1.DUwDvf", timeout=20000)
        pause()
        photos = read_photos(page, MAX_PHOTOS)
        row["photos"] = len(photos)
        if len(photos) < MIN_PHOTOS:
            reason = f"only {len(photos)} photos"
    row["verdict"] = "FAIL" if reason else "PASS"
    row["reason"] = reason
    if not reason:
        folder = QUAL / f"{slug(d['name'])}-{re.sub(r'[^0-9]', '', d['phone'])[-4:]}"
        (folder / "images").mkdir(parents=True, exist_ok=True)
        row["photos"] = sum(download(u, folder / "images" / f"maps_{i:02d}.jpg") for i, u in enumerate(photos, 1))
        d.pop("overview", None)
        json.dump({**d, "search": search, "photo_urls": photos}, open(folder / "place.json", "w", encoding="utf-8"), indent=1, ensure_ascii=False)
        json.dump(reviews, open(folder / "reviews.json", "w", encoding="utf-8"), indent=1, ensure_ascii=False)
        # the short list of businesses whose email still has to be found on their own Facebook / Instagram
        new = not EMAIL_TODO.exists()
        with open(EMAIL_TODO, "a", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            if new:
                w.writerow(["name", "phone", "address", "maps_url", "email_on_google", "facebook", "instagram", "folder"])
            w.writerow([d["name"], d["phone"], d["address"], d["maps_url"], row["email_on_google"], row["facebook"], row["instagram"], folder.name])
    return row


def publish(drive_folder):
    """Zip maps_out into the Google Drive for desktop folder. The file keeps the same name, so Drive updates the
    same file and its shared link always opens the newest results."""
    if not drive_folder:
        return
    import shutil, zipfile
    dst = Path(drive_folder)
    dst.mkdir(parents=True, exist_ok=True)
    tmp = HERE / "maps_out_latest.zip"
    with zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as z:
        for f in OUT.rglob("*"):
            if f.is_file():
                z.write(f, f.relative_to(HERE))
    shutil.copyfile(tmp, dst / "maps_out_latest.zip")
    log(f"results zipped to {dst / 'maps_out_latest.zip'} (Google Drive uploads it)")


# ---- main ---------------------------------------------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--categories", default=str(HERE / "categories.txt"))
    ap.add_argument("--towns", default=str(HERE / "towns.txt"))
    ap.add_argument("--max-per-search", type=int, default=60)
    ap.add_argument("--limit-searches", type=int, default=0, help="stop after this many searches (0 = all)")
    ap.add_argument("--unattended", action="store_true", help="overnight: wait out Google checks instead of asking you")
    ap.add_argument("--drive-folder", default="", help="a folder inside Google Drive for desktop, e.g. \"G:/My Drive/maps_leads\"")
    ap.add_argument("--upload-every", type=int, default=1000, help="zip results to the Drive folder after this many businesses")
    args = ap.parse_args()
    global UNATTENDED
    UNATTENDED = args.unattended
    OUT.mkdir(exist_ok=True)
    QUAL.mkdir(exist_ok=True)
    cats = [l.strip() for l in open(args.categories, encoding="utf-8") if l.strip() and not l.startswith("#")]
    towns = [l.strip() for l in open(args.towns, encoding="utf-8") if l.strip() and not l.startswith("#")]
    searches = [f"{c} in {t}" for t in towns for c in cats]
    done = set(DONE_SEARCHES.read_text(encoding="utf-8").splitlines()) if DONE_SEARCHES.exists() else set()
    seen = load_seen()
    passed = sum(1 for v in seen.values() if v == "PASS")
    log(f"{len(searches)} searches planned, {len(done)} already done, {len(seen)} businesses seen, {passed} passed")

    with sync_playwright() as pw:
        def start():
            try:
                b = pw.chromium.launch(channel="chrome", headless=False)
            except Exception:
                b = pw.chromium.launch(headless=False)
            return b, b.new_page(locale="en-US", viewport={"width": 1400, "height": 950})
        browser, page = start()
        count, since_upload, failures = 0, 0, 0
        for s in searches:
            if s in done:
                continue
            if args.limit_searches and count >= args.limit_searches:
                break
            count += 1
            log(f"SEARCH {s}")
            try:
                links = search_results(page, s, args.max_per_search)
            except Exception as e:
                log(f"  search failed: {str(e)[:80]}; restarting the browser")
                try:
                    browser.close()
                except Exception:
                    pass
                browser, page = start()
                continue
            log(f"  {len(links)} businesses in the list")
            for url in links:
                key = place_key(url)
                if key in seen:
                    continue
                try:
                    row = check_business(page, url, s)
                    failures = 0
                except Exception as e:
                    log(f"  could not read a listing: {str(e)[:80]}")
                    failures += 1
                    if failures >= 5:  # the browser is probably stuck or closed: start a fresh one
                        log("  restarting the browser")
                        try:
                            browser.close()
                        except Exception:
                            pass
                        browser, page = start()
                        failures = 0
                    continue
                row["place_key"] = key
                passed += row["verdict"] == "PASS"
                if row["verdict"] == "PASS":
                    log(f"  PASS  {row['name']} | {row['rating']} ({row['reviews']}) | {row['photos']} photos | total passed {passed}")
                else:
                    log(f"  fail  {row['name'][:40]} | {row['reason']}")
                write_row(row)
                seen[key] = row["verdict"]
                since_upload += 1
                if since_upload >= args.upload_every:
                    publish(args.drive_folder)
                    since_upload = 0
                pause()
            with open(DONE_SEARCHES, "a", encoding="utf-8") as f:
                f.write(s + "\n")
            pause(3, 6)
        browser.close()
    publish(args.drive_folder)
    log(f"done: {passed} passed. Zip the maps_out folder and share it.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        log("stopped; run again to continue where it left off")
