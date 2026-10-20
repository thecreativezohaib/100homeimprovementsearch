// Design reference capture: full-page screenshots of a site's homepage at desktop (1440 wide) and mobile (390 wide,
// iPhone user agent, 2x), after dismissing cookie banners and scrolling to load lazy images.
// Usage: node design_shots.js <in.jsonl {id,url}> <outdir>
const { chromium, devices } = require('/opt/node22/lib/node_modules/playwright');
const fs = require('fs');

const ACCEPT = /^(accept( all)?( cookies)?|i accept|agree|i agree|got it|ok|okay|allow all|close|no thanks|dismiss|×|x)$/i;

const CLEAN = `*,*::before,*::after{animation-delay:0s!important;animation-duration:0s!important;transition:none!important}
[data-aos],.wow,[data-animate],.aos-init,.reveal,.fade-in,.fadeIn{opacity:1!important;transform:none!important;visibility:visible!important}`;

// hide fixed or sticky overlays that are not part of the design: cookie and consent banners, newsletter and chat
// pop-ups, full-screen dimmers and bot-check notices; sticky headers and call bars stay
function cleanOverlays() {
  const vw = innerWidth, vh = innerHeight;
  for (const el of document.querySelectorAll('body *')) {
    const cs = getComputedStyle(el);
    if (cs.position !== 'fixed' && cs.position !== 'sticky') continue;
    const t = (el.innerText || '').toLowerCase();
    const r = el.getBoundingClientRect();
    const big = r.width * r.height > vw * vh * 0.2;
    const z = parseInt(cs.zIndex) || 0;
    if (/cookie|consent|privacy information|we use .{0,30}(cookies|technologies)/.test(t) && t.length < 1500
        || big && /subscribe|newsletter|sign up for|book instantly|text me|verify the security/.test(t)
        || big && z >= 999 && t.trim().length < 3) el.style.setProperty('display', 'none', 'important');
  }
  for (const el of document.querySelectorAll('body *')) {
    if (el.children.length < 3 && /verify the security of your connection/i.test(el.textContent || '')) el.style.setProperty('display', 'none', 'important');
  }
  document.documentElement.style.setProperty('overflow', 'auto', 'important');
  document.body.style.setProperty('overflow', 'auto', 'important');
}

async function prep(page) {
  await page.waitForTimeout(3500);
  await page.addStyleTag({ content: CLEAN }).catch(() => { });
  for (let round = 0; round < 2; round++) {
    for (const el of await page.$$('button, a[role=button], [aria-label*="close" i], [aria-label*="dismiss" i]')) {
      try {
        const t = ((await el.innerText()) || (await el.getAttribute('aria-label')) || '').trim();
        if (ACCEPT.test(t) && await el.isVisible()) { await el.click({ timeout: 1500 }); await page.waitForTimeout(400); }
      } catch (e) { }
    }
    await page.keyboard.press('Escape').catch(() => { });
  }
  const h = await page.evaluate(() => document.body.scrollHeight);
  // SLOW=1: smaller steps and longer pauses for sites whose lazy images or bot checks need more time
  const step = process.env.SLOW ? 300 : 500, pause = process.env.SLOW ? 450 : 180;
  if (process.env.SLOW) await page.waitForTimeout(6000);
  for (let y = 0; y < Math.min(h, 16000); y += step) {
    await page.evaluate(v => window.scrollTo(0, v), y);
    await page.waitForTimeout(pause);
  }
  await page.evaluate(() => window.scrollTo(0, 0));
  await page.waitForTimeout(1500);
  await page.evaluate(cleanOverlays).catch(() => { });
}

async function shot(browser, opts, url, file) {
  const { viewShots, ...ctxOpts } = opts;
  const ctx = await browser.newContext({ ...ctxOpts, ignoreHTTPSErrors: true });
  const page = await ctx.newPage();
  try {
    await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 60000 });
    await prep(page);
    const title = await page.title();
    await page.screenshot({ path: file, fullPage: true, type: 'jpeg', quality: 75, timeout: 90000 });
    if (opts.viewShots) {
      // what a visitor sees on screen: first screen, then after scrolling (shows sticky headers and call bars)
      await page.screenshot({ path: file.replace('_full.jpg', '_screen1.jpg'), type: 'jpeg', quality: 80 });
      await page.evaluate(() => window.scrollTo(0, 1600)); await page.waitForTimeout(1200);
      await page.screenshot({ path: file.replace('_full.jpg', '_screen2_scrolled.jpg'), type: 'jpeg', quality: 80 });
    }
    return { ok: true, title, final_url: page.url() };
  } catch (e) {
    return { ok: false, error: String(e).slice(0, 200) };
  } finally { await ctx.close(); }
}

(async () => {
  const [inp, out] = process.argv.slice(2);
  fs.mkdirSync(out, { recursive: true });
  const browser = await chromium.launch({ proxy: { server: process.env.HTTPS_PROXY } });
  const iphone = devices['iPhone 13'];
  for (const line of fs.readFileSync(inp, 'utf8').split('\n').filter(Boolean)) {
    const { id, url } = JSON.parse(line);
    const d = await shot(browser, { viewport: { width: 1440, height: 900 }, viewShots: true }, url, `${out}/${id}__desktop_full.jpg`);
    const m = await shot(browser, { ...iphone, viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, viewShots: true }, url, `${out}/${id}__mobile_full.jpg`);
    const t = process.env.TABLET ? await shot(browser, { viewport: { width: 820, height: 1180 } }, url, `${out}/${id}__tablet_full.jpg`) : null;
    const rec = { id, url, desktop: d, mobile: m, tablet: t, captured: new Date().toISOString() };
    fs.appendFileSync(`${out}/_log.jsonl`, JSON.stringify(rec) + '\n');
    console.log(id, d.ok, m.ok);
  }
  await browser.close();
})();
