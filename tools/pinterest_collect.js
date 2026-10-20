// Pinterest search collector for design references. Opens the logged-out search page for each query, scrolls, and
// records every pin from Pinterest's own search API responses (BaseSearchResource): pin id, title, description,
// link, board, pinner, and the original-size image URL.
// Usage: node pinterest_collect.js <queries.txt one per line> <out.jsonl> [scrolls]
const { chromium } = require('/opt/node22/lib/node_modules/playwright');
const fs = require('fs');
const [qfile, out, scrollArg] = process.argv.slice(2);
const SCROLLS = parseInt(scrollArg || '8');
const queries = fs.readFileSync(qfile, 'utf8').split('\n').map(s => s.trim()).filter(Boolean);

function pinsFrom(json, q) {
  const res = [];
  const walk = o => {
    if (!o || typeof o !== 'object') return;
    if (o.type === 'pin' && o.id && o.images) {
      const im = o.images.orig || o.images['736x'] || Object.values(o.images).pop();
      res.push({ q, id: o.id, url: `https://www.pinterest.com/pin/${o.id}/`, image: im && im.url, w: im && im.width, h: im && im.height,
        title: o.title || o.grid_title || '', description: (o.description || '').slice(0, 300), link: o.link || null,
        domain: o.domain || null, board: o.board && o.board.name, pinner: o.pinner && o.pinner.username,
        saves: o.aggregated_pin_data && o.aggregated_pin_data.aggregated_stats && o.aggregated_pin_data.aggregated_stats.saves });
      return;
    }
    for (const v of Array.isArray(o) ? o : Object.values(o)) walk(v);
  };
  walk(json);
  return res;
}

(async () => {
  const b = await chromium.launch({ proxy: { server: process.env.HTTPS_PROXY } });
  const ctx = await b.newContext({ viewport: { width: 1400, height: 1000 }, userAgent: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36' });
  const seen = new Set(fs.existsSync(out) ? fs.readFileSync(out, 'utf8').split('\n').filter(Boolean).map(l => JSON.parse(l).id) : []);
  for (const q of queries) {
    const p = await ctx.newPage();
    let n = 0;
    p.on('response', async r => {
      if (!/BaseSearchResource|SearchResource|__PWS_DATA__/.test(r.url())) return;
      try {
        for (const pin of pinsFrom(await r.json(), q)) {
          if (seen.has(pin.id)) continue; seen.add(pin.id); n++;
          fs.appendFileSync(out, JSON.stringify(pin) + '\n');
        }
      } catch (e) { }
    });
    try {
      await p.goto(`https://www.pinterest.com/search/pins/?q=${encodeURIComponent(q)}&rs=typed`, { waitUntil: 'domcontentloaded', timeout: 60000 });
      await p.waitForTimeout(5000);
      // first page of results is embedded in the HTML
      const embedded = await p.evaluate(() => { const s = document.getElementById('__PWS_INITIAL_PROPS__') || document.getElementById('__PWS_DATA__'); return s ? s.textContent : null; });
      if (embedded) {
        try {
          for (const pin of pinsFrom(JSON.parse(embedded), q)) { if (!seen.has(pin.id)) { seen.add(pin.id); n++; fs.appendFileSync(out, JSON.stringify(pin) + '\n'); } }
        } catch (e) { }
      }
      await p.evaluate(() => document.querySelectorAll('[role=dialog], [data-test-id*="modal" i]').forEach(e => e.remove()));
      for (let i = 0; i < SCROLLS; i++) { await p.mouse.wheel(0, 3000); await p.waitForTimeout(1800); }
    } catch (e) { console.log('error', q, String(e).slice(0, 120)); }
    console.log(q, n);
    await p.close();
  }
  await b.close();
})();
