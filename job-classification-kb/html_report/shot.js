const { chromium } = require('playwright');
const path = require('path');

(async () => {
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  const file = 'file://' + path.resolve('../analysis_推薦精準度_報告.html');
  for (const scheme of ['light', 'dark']) {
    const page = await browser.newPage({ colorScheme: scheme, viewport: { width: 1000, height: 800 } });
    page.on('console', msg => console.log(`[console:${scheme}]`, msg.type(), msg.text()));
    page.on('pageerror', err => console.log(`[pageerror:${scheme}]`, err.message));
    await page.goto(file);
    await page.waitForTimeout(300);
    await page.screenshot({ path: `shot-${scheme}.png`, fullPage: true });
    await page.close();
  }
  await browser.close();
  console.log('done');
})();
