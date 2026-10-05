// 截圖：node tests/shots.js <輸出資料夾>；每個分頁與 section 各一張（1440 亮／暗、390）
const { chromium } = require('playwright'), path = require('path'), fs = require('fs');
const URL = 'file://' + path.resolve(__dirname, '../../recruiter_journey_report.html'), out = process.argv[2] || 'shots';
fs.mkdirSync(out, { recursive: true });
(async () => {
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium', args: ['--no-sandbox'] });
  for (const [w, th] of [[1440, 'light'], [1440, 'dark'], [390, 'light']]) {
    const pg = await b.newPage({ viewport: { width: w, height: 900 }, colorScheme: th, ignoreHTTPSErrors: true });
    await pg.goto(URL); await pg.waitForTimeout(1200);
    for (const tab of ['persona', 'journey']) { await pg.click('#tb-' + tab); await pg.waitForTimeout(250);
      await pg.screenshot({ path: `${out}/${w}${th}_${tab}.png`, fullPage: true }); }
    await pg.click('#tb-journey'); await pg.click('.stn[data-i="3"]'); await pg.waitForTimeout(250);
    for (const id of ['grid', 'sitemap', 'flows']) await (await pg.$('#' + id)).screenshot({ path: `${out}/${w}${th}_${id}_C.png` });
    await pg.close();
  }
  await b.close();
})();
