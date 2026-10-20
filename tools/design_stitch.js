// Scroll-and-stitch capture for sites whose content only renders while it is on screen (scroll-triggered reveals,
// lazy images that a one-shot full-page screenshot misses). Scrolls one screen at a time, waits, and saves each
// screen as a tile; fixed and sticky elements (header, call bars) are hidden after the first tile so they do not
// repeat. tools/design_slices.py stitch joins the tiles into <id>__<device>_full.jpg.
// Usage: node design_stitch.js <in.jsonl {id,url}> <outdir>
const { chromium, devices } = require('/opt/node22/lib/node_modules/playwright');
const fs = require('fs');

async function tiles(browser, ctxOpts, url, prefix) {
  const ctx = await browser.newContext({ ...ctxOpts, ignoreHTTPSErrors: true });
  const page = await ctx.newPage();
  try {
    await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 60000 });
    await page.waitForTimeout(6000);
    for (const el of await page.$$('button, a[role=button]')) {
      try {
        const t = ((await el.innerText()) || '').trim();
        if (/^(accept( all)?( cookies)?|i accept|agree|i agree|got it|ok|allow all|close|no thanks|dismiss)$/i.test(t) && await el.isVisible()) await el.click({ timeout: 1500 });
      } catch (e) { }
    }
    const vh = ctxOpts.viewport.height;
    // first pass: walk the page so lazy content starts loading
    let H = await page.evaluate(() => document.documentElement.scrollHeight);
    for (let y = 0; y < Math.min(H, 16000); y += 400) { await page.evaluate(v => window.scrollTo(0, v), y); await page.waitForTimeout(250); }
    await page.evaluate(() => window.scrollTo(0, 0)); await page.waitForTimeout(2000);
    H = Math.min(await page.evaluate(() => document.documentElement.scrollHeight), 16000);
    const meta = [];
    for (let y = 0, n = 0; y < H; y += vh, n++) {
      const top = Math.min(y, Math.max(0, H - vh));
      await page.evaluate(v => window.scrollTo(0, v), top);
      await page.waitForTimeout(1300);
      const actual = await page.evaluate(() => window.scrollY);
      const f = `${prefix}_tile${String(n).padStart(2, '0')}.png`;
      await page.screenshot({ path: f });
      meta.push({ file: f, y: actual });
      if (n === 0) {
        await page.evaluate(() => {
          for (const el of document.querySelectorAll('body *')) {
            const p = getComputedStyle(el).position;
            if (p === 'fixed' || p === 'sticky') el.style.setProperty('visibility', 'hidden', 'important');
          }
        });
      }
    }
    fs.writeFileSync(`${prefix}_tiles.json`, JSON.stringify({ url, height: H, viewport: ctxOpts.viewport, scale: ctxOpts.deviceScaleFactor || 1, tiles: meta }));
    return { ok: true, tiles: meta.length };
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
    const d = await tiles(browser, { viewport: { width: 1440, height: 900 } }, url, `${out}/${id}__desktop`);
    const m = await tiles(browser, { ...iphone, viewport: { width: 390, height: 844 }, deviceScaleFactor: 2 }, url, `${out}/${id}__mobile`);
    const t = await tiles(browser, { viewport: { width: 820, height: 1180 } }, url, `${out}/${id}__tablet`);
    fs.appendFileSync(`${out}/_log.jsonl`, JSON.stringify({ id, url, desktop: d, mobile: m, tablet: t, captured: new Date().toISOString() }) + '\n');
    console.log(id, d.ok, m.ok, t.ok);
  }
  await browser.close();
})();
