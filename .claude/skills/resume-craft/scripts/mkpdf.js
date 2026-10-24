// 用法：node mkpdf.js <html 絕對路徑> <out.pdf>；Playwright 從 career-ops 或全域找，Chromium 用 /opt/pw-browsers/chromium
let pw; try { pw = require('playwright'); } catch { pw = require('/home/user/career-ops/node_modules/playwright'); }
(async () => {
  const b = await pw.chromium.launch({ executablePath: '/opt/pw-browsers/chromium', args: ['--no-sandbox'] });
  const p = await b.newPage(); await p.goto('file://' + process.argv[2]);
  await p.pdf({ path: process.argv[3], format: 'A4', printBackground: true, preferCSSPageSize: true }); await b.close();
})();
