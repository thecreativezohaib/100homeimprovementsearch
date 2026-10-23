// Screening of no-website Google Business Profiles (round 2: fresh homepages for businesses without a site).
// Opens each Maps listing and records title, category, phone, address or service area, website (to confirm none, or
// that it only points to Facebook/Instagram/Linktree), social links shown on the profile, rating and review count,
// the "From the business" description, the photo count label, and the newest reviews.
// Usage: node maps_nosite.js <in.jsonl {id, maps_url}> <out.jsonl>
const { chromium } = require('/opt/node22/lib/node_modules/playwright');
const fs = require('fs');
const [inp, out] = process.argv.slice(2);
const done = new Set(fs.existsSync(out) ? fs.readFileSync(out, 'utf8').split('\n').filter(Boolean).map(l => JSON.parse(l).id) : []);
const todo = fs.readFileSync(inp, 'utf8').split('\n').filter(Boolean).map(l => JSON.parse(l)).filter(c => !done.has(c.id));

async function newCtx(b) {
  const ctx = await b.newContext({ locale: 'en-US', viewport: { width: 1366, height: 900 },
    userAgent: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36' });
  await ctx.addInitScript(() => { Object.defineProperty(navigator, 'webdriver', { get: () => undefined }); });
  return [ctx, await ctx.newPage()];
}

(async () => {
  const b = await chromium.launch({ proxy: { server: process.env.HTTPS_PROXY }, args: ['--disable-blink-features=AutomationControlled'] });
  let [ctx, p] = await newCtx(b);
  let n = 0;
  for (const c of todo) {
    // saved search URLs go stale; the place id inside them opens the listing reliably
    const pid = (c.maps_url.match(/!19s(ChIJ[\w-]+)/) || [])[1];
    const url = pid ? `https://www.google.com/maps/place/?q=place_id:${pid}&hl=en` : c.maps_url;
    const rec = { id: c.id, maps_url: url, retrieved: new Date().toISOString() };
    try {
      await p.goto(url, { waitUntil: 'domcontentloaded', timeout: 45000 });
      await p.waitForSelector('h1.DUwDvf', { timeout: 20000, state: 'attached' });
      await p.waitForTimeout(2200);
      Object.assign(rec, await p.evaluate(() => {
        const q = s => document.querySelector(s);
        const main = q('div[role=main]') || document.body;
        const links = [...main.querySelectorAll('a[href]')].map(a => a.href);
        const photoBtn = [...main.querySelectorAll('button')].find(x => /photo/i.test(x.getAttribute('aria-label') || ''));
        return {
          title: (q('h1.DUwDvf') || {}).innerText || null,
          category: (q('button.DkEaL') || {}).innerText || null,
          website: (q('a[data-item-id="authority"]') || {}).href || null,
          phone: (q('button[data-item-id^="phone"]') || { getAttribute: () => null }).getAttribute('data-item-id'),
          address: (q('button[data-item-id="address"]') || {}).innerText || null,
          service_area: /Service area|Serves /i.test(main.innerText) ? (main.innerText.match(/(?:Serves|Service area)[^\n]{0,160}/i) || [null])[0] : null,
          rating_label: (q('div.F7nice') || {}).innerText || null,
          socials: [...new Set(links.filter(h => /facebook\.com|instagram\.com|linktr\.ee|tiktok\.com|youtube\.com|yelp\.com|nextdoor\.com|houzz\.com/i.test(h)))],
          photo_label: photoBtn ? photoBtn.getAttribute('aria-label') : null,
          overview: main.innerText.slice(0, 5000),
          permanently_closed: /Permanently closed|Temporarily closed/i.test(main.innerText),
        };
      }));
      // the About tab holds "From the business" and the attribute list
      const about = await p.evaluate(() => { const t = [...document.querySelectorAll('button[role=tab]')].find(b => /About/.test(b.innerText)); if (t) { t.click(); return true; } return false; });
      if (about) { await p.waitForTimeout(1800); rec.about = await p.evaluate(() => (document.querySelector('div[role=main]') || document.body).innerText.slice(0, 4000)); }
      const rev = await p.evaluate(() => { const t = [...document.querySelectorAll('button[role=tab]')].find(b => /Reviews/.test(b.innerText)); if (t) { t.click(); return true; } return false; });
      if (rev) {
        await p.waitForTimeout(2200);
        rec.reviews = await p.$$eval('div[data-review-id].jftiEf', ds => ds.slice(0, 10).map(d => ({
          reviewer: d.getAttribute('aria-label'), when: (d.querySelector('.rsqaWe') || {}).innerText || null,
          stars: d.querySelector('.kvMYJc') ? d.querySelector('.kvMYJc').getAttribute('aria-label') : null,
          text: (d.querySelector('.wiI7pd') || {}).innerText || null, owner_reply: (d.querySelector('.CDe7pd') || {}).innerText || null })));
      }
    } catch (e) { rec.error = e.message.slice(0, 160); }
    fs.appendFileSync(out, JSON.stringify(rec) + '\n');
    n++;
    if (n % 40 === 0) { await ctx.close(); [ctx, p] = await newCtx(b); }
    if (n % 25 === 0) console.error(n, rec.title, rec.rating_label && rec.rating_label.replace(/\n/g, ' '), rec.error || '');
  }
  await b.close();
})();
