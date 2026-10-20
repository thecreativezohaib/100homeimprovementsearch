// Full crawl for the homepage kit: up to MAX pages per site on the firm's own host, rendered in Chromium.
// Per page: url, title, meta description, headings, visible text, every image (src, largest srcset entry, alt, size),
// CSS background images, outbound social / profile links, tel and mailto links, and raw JSON-LD blocks.
// Usage: node fullcrawl.js <in.jsonl {id,url}> <out.jsonl> [max_pages]
const { chromium } = require('/opt/node22/lib/node_modules/playwright');
const fs = require('fs');
const [inp, out, maxArg] = process.argv.slice(2);
const MAX = parseInt(maxArg || '20');
const done = new Set(fs.existsSync(out) ? fs.readFileSync(out, 'utf8').split('\n').filter(Boolean).map(l => JSON.parse(l).id) : []);
const todo = fs.readFileSync(inp, 'utf8').split('\n').filter(Boolean).map(l => JSON.parse(l)).filter(c => !done.has(c.id));
const SKIP = /\.(pdf|jpe?g|png|gif|webp|svg|zip|mp4|mov|docx?|xlsx?)(\?|$)|\/wp-json|\/feed|\/tag\/|\/author\/|\/cart|\/checkout|\/login|\/wp-admin|privacy|terms|cookie|\/page\/\d+|#|mailto:|tel:/i;
const PRI = /about|service|kitchen|bath|remodel|gallery|portfolio|project|our-work|process|review|testimonial|contact|team|faq|area|location|warranty|financ|showroom|design/i;
(async () => {
  const b = await chromium.launch({ proxy: { server: process.env.HTTPS_PROXY } });
  const ctx = await b.newContext({ viewport: { width: 1366, height: 900 }, userAgent: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36' });
  for (const c of todo) {
    const rec = { id: c.id, start_url: c.url, crawled: new Date().toISOString(), pages: [] };
    const p = await ctx.newPage();
    let host = null; const queue = [c.url]; const seen = new Set();
    try {
      while (queue.length && rec.pages.length < MAX) {
        const u = queue.shift(); const key = u.replace(/\/$/, '');
        if (seen.has(key)) continue; seen.add(key);
        try {
          const r = await p.goto(u, { waitUntil: 'domcontentloaded', timeout: 40000 });
          await p.waitForTimeout(2500);
          await p.evaluate(async () => { for (let y = 0; y < document.body.scrollHeight; y += 900) { window.scrollTo(0, y); await new Promise(z => setTimeout(z, 120)); } });
          const final = p.url(); if (!host) host = new URL(final).host.replace('www.', '');
          if (new URL(final).host.replace('www.', '') !== host) continue;
          const pg = await p.evaluate(() => {
            const abs = s => { try { return new URL(s, location.href).href } catch (e) { return null } };
            const big = el => { const ss = el.getAttribute('srcset') || el.getAttribute('data-srcset') || ''; let best = null, bw = 0; ss.split(',').forEach(x => { const [u, w] = x.trim().split(/\s+/); const n = parseInt(w) || 0; if (u && n >= bw) { bw = n; best = u } }); return best ? abs(best) : null };
            const imgs = [...document.querySelectorAll('img')].map(i => ({ src: abs(i.currentSrc || i.src || i.getAttribute('data-src') || ''), srcset_largest: big(i), alt: i.alt || '', w: i.naturalWidth, h: i.naturalHeight })).filter(x => x.src && !x.src.startsWith('data:'));
            const bgs = [...document.querySelectorAll('*')].map(e => getComputedStyle(e).backgroundImage).filter(x => x && x.startsWith('url(')).map(x => abs(x.slice(4, -1).replace(/["']/g, ''))).filter(Boolean);
            const links = [...document.querySelectorAll('a[href]')].map(a => ({ href: a.href, text: (a.innerText || '').trim().slice(0, 80) }));
            const heads = [...document.querySelectorAll('h1,h2,h3')].map(h => h.tagName + ': ' + h.innerText.replace(/\s+/g, ' ').trim()).filter(x => x.length > 4).slice(0, 80);
            const meta = n => (document.querySelector(`meta[name="${n}"],meta[property="${n}"]`) || {}).content || null;
            const ld = [...document.querySelectorAll('script[type="application/ld+json"]')].map(s => s.textContent.slice(0, 20000));
            return { title: document.title, meta_description: meta('description'), og_title: meta('og:title'), og_image: meta('og:image'),
              headings: heads, text: document.body.innerText.replace(/\n{3,}/g, '\n\n').slice(0, 40000), images: imgs, background_images: [...new Set(bgs)].slice(0, 60), links, jsonld: ld };
          });
          pg.url = final; pg.http = r ? r.status() : null;
          rec.pages.push({ url: final, http: pg.http, title: pg.title, meta_description: pg.meta_description, og_title: pg.og_title, og_image: pg.og_image,
            headings: pg.headings, text: pg.text, images: pg.images, background_images: pg.background_images, jsonld: pg.jsonld,
            outbound: pg.links.filter(l => { try { return new URL(l.href).host.replace('www.', '') !== host } catch (e) { return false } }).map(l => l.href).filter((v, i, a) => a.indexOf(v) === i).slice(0, 80),
            tel: pg.links.filter(l => l.href.startsWith('tel:')).map(l => l.href).filter((v, i, a) => a.indexOf(v) === i),
            mailto: pg.links.filter(l => l.href.startsWith('mailto:')).map(l => l.href).filter((v, i, a) => a.indexOf(v) === i) });
          const inner = pg.links.map(l => l.href.split('#')[0]).filter(h => { try { return new URL(h).host.replace('www.', '') === host && !SKIP.test(h) } catch (e) { return false } });
          const uniq = [...new Set(inner)].filter(h => !seen.has(h.replace(/\/$/, '')));
          uniq.sort((a, b2) => (PRI.test(b2) ? 1 : 0) - (PRI.test(a) ? 1 : 0));
          for (const h of uniq) if (!queue.includes(h)) queue.push(h);
        } catch (e) { rec.pages.push({ url: u, error: e.message.slice(0, 160) }); }
      }
    } catch (e) { rec.error = e.message.slice(0, 160); }
    await p.close();
    fs.appendFileSync(out, JSON.stringify(rec) + '\n');
    console.error(c.id, rec.pages.length);
  }
  await b.close();
})();
