// QA of the live homepage concepts at phone size (390 px, iPhone): load status and time, tap-to-call numbers vs the
// expected Google number, broken images, horizontal overflow, bottom call bar, H1 count, title, page weight.
// Usage: node concept_qa.js <outreach_base.json> <out.jsonl>
const { chromium, devices } = require('/opt/node22/lib/node_modules/playwright');
const fs = require('fs');
const [base, out] = process.argv.slice(2);
const rows = JSON.parse(fs.readFileSync(base, 'utf8'));
const digits = s => (s || '').replace(/\D/g, '').replace(/^1(?=\d{10}$)/, '');
(async () => {
  const b = await chromium.launch({ proxy: { server: process.env.HTTPS_PROXY } });
  const lanes = 4; let i = 0;
  async function worker() {
    const ctx = await b.newContext({ ...devices['iPhone 13'] });
    while (i < rows.length) {
      const r = rows[i++]; const p = await ctx.newPage(); let bytes = 0;
      p.on('response', async res => { try { const h = res.headers()['content-length']; if (h) bytes += parseInt(h); } catch (e) { } });
      const rec = { n: r.n, id: r.id, url: r.new_concept };
      try {
        const t0 = Date.now(); const resp = await p.goto(r.new_concept, { waitUntil: 'load', timeout: 60000 });
        rec.status = resp.status(); rec.load_ms = Date.now() - t0;
        const H = await p.evaluate(() => document.body.scrollHeight);
        for (let y = 0; y < H; y += 700) { await p.evaluate(v => scrollTo(0, v), y); await p.waitForTimeout(120); }
        await p.evaluate(() => scrollTo(0, 2500)); await p.waitForTimeout(1200);
        Object.assign(rec, await p.evaluate(() => {
          const tels = [...new Set([...document.querySelectorAll('a[href^="tel:"]')].map(a => a.getAttribute('href')))];
          const imgs = [...document.images]; const broken = imgs.filter(im => im.complete && im.naturalWidth === 0 && im.getAttribute('src')).map(im => im.currentSrc || im.src);
          const bar = [...document.querySelectorAll('body *')].some(e => { const cs = getComputedStyle(e); const q = e.getBoundingClientRect();
            return cs.position === 'fixed' && q.bottom >= innerHeight - 4 && q.height > 30 && q.height < 160 && cs.visibility !== 'hidden' && cs.display !== 'none' && parseFloat(cs.opacity) > 0.5 && /call|book|estimate|quote/i.test(e.innerText || ''); });
          return { title: document.title, h1: document.querySelectorAll('h1').length, tels, images: imgs.length, broken: broken.slice(0, 5), broken_count: broken.length,
            overflow_px: Math.max(0, document.documentElement.scrollWidth - innerWidth), bottom_bar: bar,
            women_owned: /women[- ]owned|woman[- ]owned/i.test(document.body.innerText), placeholder: /lorem ipsum|\[your|placeholder|todo/i.test(document.body.innerText) };
        }));
        rec.kb = Math.round(bytes / 1024);
        const want = digits(r.google_phone);
        rec.tel_matches_google = want ? rec.tels.some(t => digits(t) === want) : null;
        rec.other_tels = rec.tels.filter(t => digits(t) !== want);
      } catch (e) { rec.error = String(e).slice(0, 150); }
      fs.appendFileSync(out, JSON.stringify(rec) + '\n'); console.log(rec.n, rec.status, rec.error ? 'ERR' : '');
      await p.close();
    }
    await ctx.close();
  }
  await Promise.all(Array.from({ length: lanes }, worker));
  await b.close();
})();
