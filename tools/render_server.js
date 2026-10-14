// Local render service: GET http://127.0.0.1:8765/?url=<u> -> rendered HTML (Chromium, US egress).
// Response headers: X-Status (HTTP status of navigation), X-Final-Url.
const { chromium } = require('/opt/node22/lib/node_modules/playwright');
const http = require('http');
const MAX = +(process.env.RENDER_CONC || 6);
(async () => {
  const b = await chromium.launch({ proxy: { server: process.env.HTTPS_PROXY }, args: ['--disable-blink-features=AutomationControlled'] });
  let active = 0; const queue = [];
  const run = async (u, res) => {
    active++;
    const ctx = await b.newContext({ locale: 'en-US', viewport: { width: 1366, height: 900 },
      userAgent: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36' });
    await ctx.addInitScript(() => { Object.defineProperty(navigator, 'webdriver', { get: () => undefined }); });
    const p = await ctx.newPage();
    try {
      const r = await p.goto(u, { waitUntil: 'domcontentloaded', timeout: 40000 });
      await p.waitForTimeout(4500);
      try { await p.evaluate(() => window.scrollBy(0, 3000)); await p.waitForTimeout(800); } catch (e) {}
      let html = await p.content();
      if (/just a moment|challenge-platform/i.test(html.slice(0, 5000))) { await p.waitForTimeout(8000); html = await p.content(); }
      res.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8', 'X-Status': String(r ? r.status() : 0), 'X-Final-Url': encodeURI(p.url()) });
      res.end(html);
    } catch (e) {
      res.writeHead(502, { 'X-Error': e.message.slice(0, 150).replace(/[^\x20-\x7e]/g, ' ') }); res.end('');
    } finally {
      await ctx.close(); active--;
      if (queue.length) { const [u2, r2] = queue.shift(); run(u2, r2); }
    }
  };
  http.createServer((req, res) => {
    const u = new URL(req.url, 'http://x').searchParams.get('url');
    if (!u) { res.writeHead(400); return res.end(); }
    if (active < MAX) run(u, res); else queue.push([u, res]);
  }).listen(8765, '127.0.0.1');
  console.error('render server up');
})();
