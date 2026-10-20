// Design reference capture: full-page screenshots of a site's homepage at desktop (1440 wide) and mobile (390 wide,
// iPhone user agent, 2x), after dismissing cookie banners and scrolling to load lazy images.
// Usage: node design_shots.js <in.jsonl {id,url}> <outdir>
const { chromium, devices } = require('/opt/node22/lib/node_modules/playwright');
const fs = require('fs');

const ACCEPT = /^(accept( all)?( cookies)?|i accept|agree|i agree|got it|ok|okay|allow all|close|no thanks|dismiss|×|x)$/i;

async function prep(page) {
  await page.waitForTimeout(3500);
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
  for (let y = 0; y < Math.min(h, 16000); y += 500) {
    await page.evaluate(v => window.scrollTo(0, v), y);
    await page.waitForTimeout(180);
  }
  await page.evaluate(() => window.scrollTo(0, 0));
  await page.waitForTimeout(1500);
}

async function shot(browser, opts, url, file) {
  const ctx = await browser.newContext({ ...opts, ignoreHTTPSErrors: true });
  const page = await ctx.newPage();
  try {
    await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 60000 });
    await prep(page);
    const title = await page.title();
    await page.screenshot({ path: file, fullPage: true, type: 'jpeg', quality: 75, timeout: 90000 });
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
    const d = await shot(browser, { viewport: { width: 1440, height: 900 } }, url, `${out}/${id}__desktop_full.jpg`);
    const m = await shot(browser, { ...iphone, viewport: { width: 390, height: 844 }, deviceScaleFactor: 2 }, url, `${out}/${id}__mobile_full.jpg`);
    const rec = { id, url, desktop: d, mobile: m, captured: new Date().toISOString() };
    fs.appendFileSync(`${out}/_log.jsonl`, JSON.stringify(rec) + '\n');
    console.log(id, d.ok, m.ok);
  }
  await browser.close();
})();
