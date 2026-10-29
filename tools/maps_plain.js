// Plain (undisguised) copy of maps_deep.js: default browser identity, no automation masking.
// Deep Google Maps capture for the round 2 finalists (no-website businesses). Maps serves this server its limited
// view (no photo gallery), so this takes what that view shows: title, category, rating and count, address, phone,
// hours (expanded), the overview text and any "From the business" / About text, the cover photo and the profile
// photos, then the Reviews tab sorted by newest, scrolled until no new reviews load: reviewer, stars, date, text,
// owner reply and every photo attached to a review. Image URLs are stored at original size (=s0).
// Usage: node maps_deep.js <in.jsonl {row, maps_url}> <out.jsonl>
const { chromium } = require('/opt/node22/lib/node_modules/playwright');
const fs = require('fs');
const [inp, out] = process.argv.slice(2);
const done = new Set(fs.existsSync(out) ? fs.readFileSync(out, 'utf8').split('\n').filter(Boolean).map(l => JSON.parse(l).row) : []);
const todo = fs.readFileSync(inp, 'utf8').split('\n').filter(Boolean).map(l => JSON.parse(l)).filter(c => !done.has(c.row));
const full = u => u.replace(/=[swh]\d[^/]*$/, '') + '=s0';

async function newCtx(b) {
  const ctx = await b.newContext({ locale: 'en-US', viewport: { width: 1366, height: 1000 } });
  return [ctx, await ctx.newPage()];
}

const bgUrls = p => p.evaluate(() => [...new Set([...document.querySelectorAll('div[role=main] *')]
  .map(d => (getComputedStyle(d).backgroundImage.match(/url\("([^"]+)"\)/) || [])[1])
  .filter(u => u && /googleusercontent\.com\/(grass-cs|p|gps-cs|geougc)/.test(u)))]);

(async () => {
  const b = await chromium.launch({ proxy: { server: process.env.HTTPS_PROXY } });
  let [ctx, p] = await newCtx(b); let n = 0;
  for (const c of todo) {
    const rec = { row: c.row, maps_url: c.maps_url, retrieved: new Date().toISOString() };
    try {
      await p.goto(c.maps_url, { waitUntil: 'domcontentloaded', timeout: 45000 });
      await p.waitForSelector('h1.DUwDvf', { timeout: 25000 });
      await p.waitForSelector('button[role=tab]', { timeout: 20000 }).catch(() => {});
      await p.waitForTimeout(2000);
      // expand the hours table
      await p.evaluate(() => { const h = document.querySelector('[data-item-id="oh"], div[aria-label*="hours" i] [role=button], span[aria-label*="Show open hours" i]'); h && h.click(); });
      await p.waitForTimeout(800);
      Object.assign(rec, await p.evaluate(() => {
        const q = s => document.querySelector(s); const main = q('div[role=main]') || document.body;
        const hours = [...main.querySelectorAll('table tr')].map(tr => tr.innerText.replace(/\s+/g, ' ').trim()).filter(Boolean);
        return {
          title: (q('h1.DUwDvf') || {}).innerText || null,
          category: (q('button.DkEaL') || {}).innerText || null,
          rating_label: (q('div.F7nice') || {}).innerText || null,
          address: ((q('button[data-item-id="address"]') || {}).innerText || '').replace(/^\W+/, '') || null,
          phone: (q('button[data-item-id^="phone"]') || { getAttribute: () => null }).getAttribute('data-item-id'),
          service_area: (main.innerText.match(/(?:Serves|Service area)[^\n]{0,200}/i) || [null])[0],
          hours,
          overview_text: main.innerText.slice(0, 6000),
          profile_photos: [...main.querySelectorAll('img')].map(i => i.src).filter(s => /googleusercontent\.com\/(grass-cs|p\/|gps-cs|geougc)/.test(s)),
        };
      }));
      rec.overview_photos = await bgUrls(p);
      // About tab, when the limited view offers it
      const about = await p.evaluate(() => { const t = [...document.querySelectorAll('button[role=tab]')].find(b => /About/.test(b.innerText)); if (t) { t.click(); return true; } return false; });
      if (about) { await p.waitForTimeout(1800); rec.about_text = await p.evaluate(() => (document.querySelector('div[role=main]') || document.body).innerText.slice(0, 5000)); }
      // Reviews, newest first, scrolled until nothing new loads
      const rev = await p.evaluate(() => { const t = [...document.querySelectorAll('button[role=tab]')].find(b => /Reviews/.test(b.innerText)); if (t) { t.click(); return true; } return false; });
      if (rev) {
        await p.waitForTimeout(2500);
        await p.evaluate(() => { const s = [...document.querySelectorAll('button')].find(b => /Sort/.test(b.getAttribute('aria-label') || b.innerText)); s && s.click(); });
        await p.waitForTimeout(1000);
        await p.evaluate(() => { const o = [...document.querySelectorAll('[role=menuitemradio], [role=menuitem]')].find(x => /Newest/.test(x.innerText)); o && o.click(); });
        await p.waitForTimeout(2000);
        let last = -1, same = 0;
        for (let i = 0; i < 60 && same < 4; i++) {
          await p.evaluate(() => { const s = document.querySelector('div[role=main] div.m6QErb.DxyBCb') || [...document.querySelectorAll('div[role=main] div')].find(d => d.scrollHeight > d.clientHeight + 200); s && s.scrollBy(0, 5000); });
          await p.waitForTimeout(900);
          const cnt = await p.$$eval('div[data-review-id].jftiEf', d => d.length);
          same = cnt === last ? same + 1 : 0; last = cnt;
        }
        await p.evaluate(() => document.querySelectorAll('button.w8nwRe, button[aria-label="See more"]').forEach(b => b.click()));
        await p.waitForTimeout(800);
        rec.reviews = await p.$$eval('div[data-review-id].jftiEf', ds => ds.map(d => ({
          reviewer: d.getAttribute('aria-label'), when: (d.querySelector('.rsqaWe') || {}).innerText || null,
          stars: d.querySelector('.kvMYJc') ? d.querySelector('.kvMYJc').getAttribute('aria-label') : null,
          text: (d.querySelector('.wiI7pd') || {}).innerText || null,
          owner_reply: (d.querySelector('.CDe7pd') || {}).innerText || null,
          photos: [...d.querySelectorAll('button.Tya61d')].map(x => (getComputedStyle(x).backgroundImage.match(/url\("([^"]+)"\)/) || [])[1]).filter(Boolean) })));
      }
      rec.all_photos = [...new Set([...(rec.profile_photos || []), ...(rec.overview_photos || []), ...(rec.reviews || []).flatMap(r => r.photos)].map(full))];
    } catch (e) { rec.error = e.message.slice(0, 160); }
    fs.appendFileSync(out, JSON.stringify(rec) + '\n');
    n++;
    console.error(n, c.row, rec.title, 'reviews', (rec.reviews || []).length, 'photos', (rec.all_photos || []).length, rec.error || '');
    if (n % 20 === 0) { await ctx.close(); [ctx, p] = await newCtx(b); }
  }
  await b.close();
})();
