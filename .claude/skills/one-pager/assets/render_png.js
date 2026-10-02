// 把 one-pager HTML 渲染成 PNG（交付物）。
// 用法：NODE_PATH=/opt/node22/lib/node_modules node render_png.js <in.html> <out.png>
// 固定 16:9 畫布 2000×1125，deviceScaleFactor:2 → 4000×2250 高解析 PNG，對 .canvas 截圖得乾淨邊界。
const { chromium } = require('playwright');
const path = require('path');

(async () => {
  const inHtml = process.argv[2];
  const outPng = process.argv[3] || inHtml.replace(/\.html$/, '.png');
  if (!inHtml) { console.error('usage: node render_png.js <in.html> <out.png>'); process.exit(1); }

  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  const page = await browser.newPage({
    viewport: { width: 2000, height: 1125 },
    deviceScaleFactor: 2,
  });
  const errors = [];
  page.on('pageerror', e => errors.push('pageerror: ' + e.message));
  page.on('console', m => { if (m.type() === 'error') errors.push('console: ' + m.text()); });

  await page.goto('file://' + path.resolve(inHtml));
  await page.waitForTimeout(250);
  const canvas = page.locator('.canvas');
  await canvas.screenshot({ path: outPng });
  await browser.close();

  if (errors.length) { console.error('JS errors:\n' + errors.join('\n')); process.exit(2); }
  console.log('wrote ' + outPng);
})();
