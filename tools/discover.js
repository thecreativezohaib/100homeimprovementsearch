// Google Maps list discovery. Usage: node discover.js <region> <out.jsonl> "<query>|<location>" ...
const { chromium } = require('/opt/node22/lib/node_modules/playwright');
const fs = require('fs');
const [region, out, ...jobs] = process.argv.slice(2);
(async () => {
  const b = await chromium.launch({ proxy: { server: process.env.HTTPS_PROXY } });
  const ctx = await b.newContext({ locale: 'en-US', viewport: { width: 1280, height: 1000 } });
  const p = await ctx.newPage();
  for (const job of jobs) {
    const [q, loc] = job.split('|');
    const url = 'https://www.google.com/maps/search/' + encodeURIComponent(q + ' near ' + loc) + '?hl=en&gl=us';
    try {
      await p.goto(url, { waitUntil: 'domcontentloaded', timeout: 60000 });
      await p.waitForSelector('div[role=feed]', { timeout: 20000 });
      await p.waitForTimeout(2500);
      for (let i = 0; i < 15; i++) {
        await p.mouse.move(200, 600); await p.mouse.wheel(0, 8000);
        await p.evaluate(() => { const f = document.querySelector('div[role=feed]'); f.scrollTop = f.scrollHeight; });
        await p.waitForTimeout(2200);
        const end = await p.evaluate(() => /reached the end of the list/i.test(document.querySelector('div[role=feed]').innerText));
        if (end) break;
      }
      await p.waitForTimeout(2500);
      const rows = await p.evaluate(() => [...document.querySelectorAll('div[role=feed] > div > div.Nv2PK, div.Nv2PK')].map(c => {
        const a = c.querySelector('a.hfpxzc');
        const w = c.querySelector('a[data-value="Website"]');
        const r = c.querySelector('span.MW4etd'); const n = c.querySelector('span.UY7F9');
        return { name: a ? a.getAttribute('aria-label') : null, maps_url: a ? a.href : null, website: w ? w.href : null,
          rating: r ? r.textContent : null, reviews: n ? n.textContent.replace(/[(),]/g, '') : null, text: c.innerText };
      }));
      const seen = new Set();
      for (const r of rows) {
        if (!r.maps_url || seen.has(r.maps_url)) continue; seen.add(r.maps_url);
        const ph = (r.text.match(/\+1 \d{3}-\d{3}-\d{4}|\(\d{3}\) \d{3}-\d{4}/) || [null])[0];
        const lines = r.text.split('\n').map(s => s.trim()).filter(Boolean);
        const cat = (lines.find(l => /·/.test(l) && !/Open|Closed|Opens|Closes/.test(l)) || '').split('·')[0].trim();
        fs.appendFileSync(out, JSON.stringify({ region, query: q, location: loc, name: r.name, maps_url: r.maps_url, website: r.website,
          rating: r.rating, reviews: r.reviews, phone: ph, category: cat, card_text: r.text, discovered: new Date().toISOString() }) + '\n');
      }
      console.error(region, job, rows.length);
    } catch (e) { console.error('ERR', job, e.message); }
  }
  await b.close();
})();
