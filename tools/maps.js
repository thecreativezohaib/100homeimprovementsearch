// Google Business Profile detail via Google Maps (anonymous, US egress).
// Usage: node maps.js <in.jsonl with id,place_id> <out.jsonl>
// Records overview text, rating, review count, and the newest reviews with Google's
// relative timestamps and owner responses, exactly as displayed on the retrieval date.
const { chromium } = require('/opt/node22/lib/node_modules/playwright');
const fs = require('fs');
const [inp, out] = process.argv.slice(2);
const done = new Set(fs.existsSync(out) ? fs.readFileSync(out, 'utf8').split('\n').filter(Boolean).map(l => JSON.parse(l).id) : []);
const todo = fs.readFileSync(inp, 'utf8').split('\n').filter(Boolean).map(l => JSON.parse(l)).filter(c => !done.has(c.id));

async function newCtx(b) {
  const ctx = await b.newContext({ locale: 'en-US', viewport: { width: 1366, height: 900 },
    userAgent: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36' });
  await ctx.addInitScript(() => { Object.defineProperty(navigator, 'webdriver', { get: () => undefined }); });
  const p = await ctx.newPage();
  await p.goto('https://www.google.com/maps?hl=en', { waitUntil: 'domcontentloaded' });
  await p.waitForTimeout(2500);
  return [ctx, p];
}

(async () => {
  const b = await chromium.launch({ proxy: { server: process.env.HTTPS_PROXY }, args: ['--disable-blink-features=AutomationControlled'] });
  let [ctx, p] = await newCtx(b);
  let n = 0;
  for (const c of todo) {
    const url = `https://www.google.com/maps/place/?q=place_id:${c.place_id}&hl=en`;
    const rec = { id: c.id, place_id: c.place_id, gbp_url: url, retrieved: new Date().toISOString() };
    try {
      await p.goto(url, { waitUntil: 'domcontentloaded', timeout: 45000 });
      await p.waitForSelector('h1.DUwDvf', { timeout: 20000, state: 'attached' });
      await p.waitForTimeout(2500);
      rec.overview = await p.evaluate(() => (document.querySelector('div[role=main]') || document.body).innerText.slice(0, 6000));
      rec.title = await p.evaluate(() => (document.querySelector('h1.DUwDvf') || {}).innerText);
      rec.website = await p.evaluate(() => { const a = document.querySelector('a[data-item-id="authority"]'); return a ? a.href : null; });
      rec.phone = await p.evaluate(() => { const a = document.querySelector('button[data-item-id^="phone"]'); return a ? a.getAttribute('data-item-id') : null; });
      rec.address = await p.evaluate(() => { const a = document.querySelector('button[data-item-id="address"]'); return a ? a.innerText : null; });
      rec.rating_label = await p.evaluate(() => { const a = document.querySelector('div.F7nice'); return a ? a.innerText : null; });
      const grab = () => p.$$eval('div[data-review-id].jftiEf', ds => ds.slice(0, 12).map(d => ({
          review_id: d.getAttribute('data-review-id'), reviewer: d.getAttribute('aria-label'),
          when: (d.querySelector('.rsqaWe') || {}).innerText || null,
          stars: d.querySelector('.kvMYJc') ? d.querySelector('.kvMYJc').getAttribute('aria-label') : null,
          text: (d.querySelector('.wiI7pd') || {}).innerText || null,
          owner: (d.querySelector('.CDe7pd') || {}).innerText || null })));
      rec.reviews = await grab();
      rec.limited_view = /limited view of Google Maps/i.test(rec.overview || '');
      if (!rec.reviews.length) {
        const hasTab = await p.evaluate(() => !![...document.querySelectorAll('button[role=tab]')].find(b => /Reviews/.test(b.innerText)));
        if (hasTab) {
          await p.evaluate(() => [...document.querySelectorAll('button[role=tab]')].find(b => /Reviews/.test(b.innerText)).click());
          await p.waitForTimeout(2500);
          rec.reviews = await grab();
        }
      }
      // owner posts ("Updates") if the profile exposes them in the overview
      rec.has_updates_text = /From the owner|Updates from|See all updates|Latest updates/i.test(rec.overview || '');
    } catch (e) {
      rec.error = e.message.slice(0, 200);
    }
    fs.appendFileSync(out, JSON.stringify(rec) + '\n');
    n++;
    if (n % 40 === 0) { await ctx.close(); [ctx, p] = await newCtx(b); }
    if (n % 10 === 0) console.error(n, c.id, rec.title, rec.reviews ? rec.reviews.length : 'x', rec.error || '');
  }
  await b.close();
})();
