// Free social and email discovery through Google search in a real browser (round 2). For each business, three
// searches: its Facebook page, its Instagram profile, and any published email. Records every result's URL, title and
// snippet, plus the emails that appear in snippets. Paced, with a fresh browser context every 25 businesses and a long
// pause when Google shows its "unusual traffic" page.
// Usage: node google_social.js <in.jsonl {id, name, city, phone}> <out.jsonl>
const { chromium } = require('/opt/node22/lib/node_modules/playwright');
const fs = require('fs');
const [inp, out] = process.argv.slice(2);
const done = new Set(fs.existsSync(out) ? fs.readFileSync(out, 'utf8').split('\n').filter(Boolean).map(l => JSON.parse(l).id) : []);
const todo = fs.readFileSync(inp, 'utf8').split('\n').filter(Boolean).map(l => JSON.parse(l)).filter(c => !done.has(c.id));
const EMAIL = /[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}/g;
const sleep = ms => new Promise(r => setTimeout(r, ms));

async function newCtx(b) {
  const ctx = await b.newContext({ locale: 'en-US', viewport: { width: 1280, height: 1000 },
    userAgent: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36' });
  await ctx.addInitScript(() => { Object.defineProperty(navigator, 'webdriver', { get: () => undefined }); });
  return [ctx, await ctx.newPage()];
}

async function search(p, q) {
  await p.goto('https://www.google.com/search?q=' + encodeURIComponent(q) + '&hl=en&gl=us&num=10', { waitUntil: 'domcontentloaded', timeout: 45000 });
  await p.waitForTimeout(2200 + Math.random() * 1500);
  const blocked = await p.evaluate(() => /unusual traffic|not a robot|recaptcha/i.test(document.body.innerText));
  if (blocked) return { blocked: true, results: [] };
  const results = await p.evaluate(() => [...document.querySelectorAll('div#search a h3')].map(h => {
    const a = h.closest('a'); let box = a; for (let i = 0; i < 6 && box && !/MjjYud|g /.test(box.className || ''); i++) box = box.parentElement;
    return { url: a.href, title: h.innerText, snippet: (box || a).innerText.slice(0, 600) };
  }).slice(0, 10));
  return { blocked: false, results };
}

(async () => {
  const b = await chromium.launch({ proxy: { server: process.env.HTTPS_PROXY }, args: ['--disable-blink-features=AutomationControlled'] });
  let [ctx, p] = await newCtx(b); let n = 0;
  for (const c of todo) {
    const rec = { id: c.id, name: c.name, searched: new Date().toISOString(), queries: {} };
    // MODE=one: a single name + city search (usually returns Facebook, Instagram, Yelp and BBB together); slower pacing
    const qs = process.env.MODE === 'one' ? { all: `"${c.name}" ${c.city || ''}` } : {
      facebook: `"${c.name}" ${c.city || ''} facebook`,
      instagram: `"${c.name}" ${c.city || ''} instagram`,
      email: `"${c.name}" ${c.city || ''} email OR "@gmail.com" OR contact`,
    };
    for (const [k, q] of Object.entries(qs)) {
      let r;
      for (let attempt = 0; attempt < 3; attempt++) {
        try { r = await search(p, q); } catch (e) { r = { blocked: false, results: [], error: String(e).slice(0, 100) }; }
        if (!r.blocked) break;
        console.error('blocked; pausing', c.id); await ctx.close(); await sleep(600000 * (attempt + 1)); [ctx, p] = await newCtx(b);
      }
      rec.queries[k] = { q, ...r };
      await sleep((parseInt(process.env.DELAY || '4000')) + Math.random() * 6000);
    }
    const all = Object.values(rec.queries).flatMap(x => x.results || []);
    rec.facebook = [...new Set(all.map(x => x.url).filter(u => /facebook\.com\/(?!sharer|groups|events|watch|share)/i.test(u)))];
    rec.instagram = [...new Set(all.map(x => x.url).filter(u => /instagram\.com\/(?!p\/|reel\/|explore)/i.test(u)))];
    rec.emails = [...new Set(all.flatMap(x => (x.snippet.match(EMAIL) || []).map(e => e.toLowerCase().replace(/[.]+$/, ''))))]
      .filter(e => !/example\.|sentry|wix|\.png|\.jpg/.test(e));
    fs.appendFileSync(out, JSON.stringify(rec) + '\n');
    n++;
    if (n % 25 === 0) { await ctx.close(); [ctx, p] = await newCtx(b); }
    console.error(n, c.name, 'fb', rec.facebook.length, 'ig', rec.instagram.length, 'emails', rec.emails.join(','));
  }
  await b.close();
})();
