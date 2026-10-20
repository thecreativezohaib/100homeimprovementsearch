// Render home + about/team/contact pages in Chromium and save visible text + mailto links (for dm_scan on JS-built sites).
// Usage: node render_text.js <in.jsonl {id,url}> <out.jsonl>
const { chromium } = require('/opt/node22/lib/node_modules/playwright');
const fs = require('fs');
const [inp, out] = process.argv.slice(2);
const todo = fs.readFileSync(inp, 'utf8').split('\n').filter(Boolean).map(l => JSON.parse(l));
const RX = /about|team|story|who-we-are|meet|owner|founder|contact|staff|people|history/i;
(async () => {
  const b = await chromium.launch({ proxy: { server: process.env.HTTPS_PROXY } });
  const ctx = await b.newContext({ userAgent: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36' });
  for (const c of todo) {
    const rec = { id: c.id, pages: [] };
    const p = await ctx.newPage();
    try {
      await p.goto(c.url, { waitUntil: 'domcontentloaded', timeout: 40000 }); await p.waitForTimeout(3500);
      const host = new URL(p.url()).host.replace('www.', '');
      const links = await p.evaluate(() => [...document.querySelectorAll('a[href]')].map(a => [a.href, a.innerText.trim()]));
      const urls = [p.url()];
      for (const [h, t] of links) { try { if (new URL(h).host.replace('www.', '') === host && !urls.includes(h.split('#')[0]) && (RX.test(h) || RX.test(t))) urls.push(h.split('#')[0]); } catch (e) {} }
      for (const u of urls.slice(0, 6)) {
        try {
          if (u !== urls[0]) { await p.goto(u, { waitUntil: 'domcontentloaded', timeout: 40000 }); await p.waitForTimeout(2500); }
          rec.pages.push({ url: u, text: (await p.evaluate(() => document.body.innerText)).slice(0, 60000),
            mailto: await p.evaluate(() => [...document.querySelectorAll('a[href^="mailto:"]')].map(a => a.getAttribute('href'))) });
        } catch (e) {}
      }
    } catch (e) { rec.error = e.message.slice(0, 120); }
    await p.close();
    fs.appendFileSync(out, JSON.stringify(rec) + '\n');
  }
  await b.close();
})();
