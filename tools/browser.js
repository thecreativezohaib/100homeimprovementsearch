// Real-browser checks (Chromium, US egress).
// Usage: node browser.js <in.jsonl with id,url> <out.jsonl> [saveHtmlDir]
// Measures: final URL/status (G2 retry route), horizontal overflow at a 375px viewport (G8),
// ad / tracking / review-platform network requests fired on load (G9), served image bytes (G8).
const { chromium } = require('/opt/node22/lib/node_modules/playwright');
const fs = require('fs');
const [inp, out, htmlDir] = process.argv.slice(2);
const done = new Set(fs.existsSync(out) ? fs.readFileSync(out, 'utf8').split('\n').filter(Boolean).map(l => JSON.parse(l).id) : []);
const todo = fs.readFileSync(inp, 'utf8').split('\n').filter(Boolean).map(l => JSON.parse(l)).filter(c => !done.has(c.id));
const NET = {
  'Google Ads (googleadservices / AW- conversion)': /googleadservices\.com|googleads\.g\.doubleclick\.net|google\.com\/pagead|[?&]id=AW-|\/AW-\d+/,
  'Meta Pixel fbevents.js': /connect\.facebook\.net\/[^ ]*fbevents\.js|facebook\.com\/tr[?\/]/,
  'Microsoft Ads UET bat.bing.com': /bat\.bing\.com/,
  'CallRail': /callrail\.com/, 'CallTrackingMetrics': /tctm\.co|calltrackingmetrics/, 'WhatConverts': /whatconverts/,
  'Podium': /podium\.com|podiumwebchat/, 'Birdeye': /birdeye\.com/, 'NiceJob': /nicejob/, 'GuildQuality': /guildquality/,
  'Houzz Pro': /houzz\.com\/pro|houzz\.com\/widget/, 'Angi/HomeAdvisor': /angi\.com|homeadvisor/, 'Thumbtack': /thumbtack/,
  'ServiceTitan': /servicetitan/, 'Housecall Pro': /housecallpro/, 'Jobber': /getjobber|jobber\.com/, 'JobNimbus': /jobnimbus/,
  'Buildertrend': /buildertrend/, 'CompanyCam': /companycam/, 'Hatch': /usehatchapp|hatchapp/, 'ReviewBuzz': /reviewbuzz/,
};
(async () => {
  const b = await chromium.launch({ proxy: { server: process.env.HTTPS_PROXY }, args: ['--disable-blink-features=AutomationControlled'] });
  for (const c of todo) {
    const rec = { id: c.id, url: c.url, tested: new Date().toISOString(), method: 'Chromium (Playwright 1.56) viewport 375x812, isMobile, DPR 3, US egress' };
    const ctx = await b.newContext({ viewport: { width: 375, height: 812 }, deviceScaleFactor: 3, isMobile: true, hasTouch: true, locale: 'en-US',
      userAgent: 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Mobile/15E148 Safari/604.1' });
    await ctx.addInitScript(() => { Object.defineProperty(navigator, 'webdriver', { get: () => undefined }); });
    const p = await ctx.newPage();
    const net = {}; const imgs = [];
    p.on('request', r => { const u = r.url(); for (const [k, re] of Object.entries(NET)) if (re.test(u) && !net[k]) net[k] = u.slice(0, 300); });
    p.on('response', async r => {
      try {
        if (r.request().resourceType() === 'image') {
          let len = +(r.headers()['content-length'] || 0);
          if (!len) { try { len = (await r.body()).length; } catch (e) {} }
          if (len > 1000000) imgs.push({ url: r.url().slice(0, 300), bytes: len, page: p.url() });
        }
      } catch (e) {}
    });
    try {
      const resp = await p.goto(c.url, { waitUntil: 'domcontentloaded', timeout: 45000 });
      rec.status = resp ? resp.status() : null;
      await p.waitForTimeout(6000);
      rec.final_url = p.url();
      rec.title = await p.title();
      for (let y = 0; y < 6; y++) { await p.evaluate(() => window.scrollBy(0, 1200)); await p.waitForTimeout(500); }
      await p.waitForTimeout(1500);
      const m = await p.evaluate(() => {
        const vw = window.innerWidth; const de = document.documentElement;
        const sw = Math.max(de.scrollWidth, document.body ? document.body.scrollWidth : 0);
        const offenders = [];
        for (const el of document.querySelectorAll('body *')) {
          const r = el.getBoundingClientRect();
          if (r.width > 0 && r.right > vw + 2 && getComputedStyle(el).position !== 'fixed') {
            offenders.push((el.tagName + (el.id ? '#' + el.id : '') + (el.className && typeof el.className === 'string' ? '.' + el.className.split(' ').slice(0, 2).join('.') : '')).slice(0, 80) + ` right=${Math.round(r.right)}`);
            if (offenders.length > 5) break;
          }
        }
        const ox = getComputedStyle(de).overflowX + '/' + (document.body ? getComputedStyle(document.body).overflowX : '');
        const vp = document.querySelector('meta[name=viewport]');
        return { innerWidth: vw, scrollWidth: sw, offenders, overflowX: ox, viewport: vp ? vp.content : null };
      });
      Object.assign(rec, m);
      rec.horizontal_overflow_px = Math.max(0, m.scrollWidth - m.innerWidth);
      rec.overflow_vs_device_px = Math.max(0, Math.max(m.scrollWidth, m.innerWidth) - 375);
      if (c.gallery) {
        try {
          await p.goto(c.gallery, { waitUntil: 'domcontentloaded', timeout: 45000 });
          await p.waitForTimeout(4000);
          for (let y = 0; y < 8; y++) { await p.evaluate(() => window.scrollBy(0, 1200)); await p.waitForTimeout(500); }
          await p.waitForTimeout(1500);
          rec.gallery_tested = c.gallery;
        } catch (e) { rec.gallery_error = e.message.slice(0, 120); }
      }
      rec.net_signals = net;
      rec.served_images_over_1mb = imgs;
      if (htmlDir) fs.writeFileSync(`${htmlDir}/${c.id.replace(/[^a-z0-9.\-]/gi, '_')}.html`, await p.content());
    } catch (e) { rec.error = e.message.slice(0, 200); rec.net_signals = net; }
    fs.appendFileSync(out, JSON.stringify(rec) + '\n');
    await ctx.close();
  }
  await b.close();
})();
