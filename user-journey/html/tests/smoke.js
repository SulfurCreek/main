// 互動煙霧測試：node tests/smoke.js（需 NODE_PATH=/opt/node22/lib/node_modules）。失敗會 exit 1。
// 覆蓋：進頁流程圖空狀態／階段篩選連動／Sitemap 錨點／迷你路線列／persona 反灰／受限卡疊加／分頁共用／手機無橫捲／無 console 錯誤
const { chromium } = require('playwright'), path = require('path');
const URL = 'file://' + path.resolve(__dirname, '../../recruiter_journey_report.html');
const fails = []; const ok = (c, m) => { if (!c) fails.push(m); console.log(c ? 'ok  ' : 'FAIL', m); };
(async () => {
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium', args: ['--no-sandbox'] });
  for (const [w, th] of [[1440, 'light'], [1440, 'dark'], [390, 'light']]) {
    const pg = await b.newPage({ viewport: { width: w, height: 900 }, colorScheme: th, ignoreHTTPSErrors: true });
    const er = []; pg.on('pageerror', e => er.push(e.message));
    await pg.goto(URL); await pg.waitForTimeout(1000);
    const ev = f => pg.evaluate(f), tag = `${w}${th}`;
    ok(await ev(() => document.querySelectorAll('#flow-body svg').length === 0), `${tag} 進頁流程圖為空狀態`);
    ok(await ev(() => document.querySelectorAll('.sm-mod').length === 9), `${tag} Sitemap 顯示全部 9 個模組`);
    ok(await ev(() => document.documentElement.scrollWidth <= innerWidth), `${tag} 無橫向捲動`);
    await pg.click('#ptabs button[data-p="P7"]'); await pg.click('#mods button[data-k="12"]');
    await pg.click('#tb-journey'); await pg.waitForTimeout(200);
    ok(await ev(() => [...document.querySelectorAll('.board .ph')].map(e => +e.classList.contains('pdim')).join('') === '01111111'), `${tag} P7＋不可登入 → 只剩 J 欄不反灰`);
    await pg.click('#mods button[data-k="12"]', { force: true }).catch(() => {});
    await pg.click('.stn[data-i="3"]');
    ok(await ev(() => document.querySelectorAll('#flow-body svg').length === 1 && document.querySelectorAll('.sm-mod.lit').length === 1), `${tag} 選 C → 載入 1 張流程圖、亮 1 個模組`);
    if (w === 1440 && th === 'light') {
      await pg.click('[data-tp].sel a >> nth=1'); await pg.waitForTimeout(900);
      ok(await ev(() => !!document.querySelector('.sm-node.flash')), `${tag} Touchpoints 錨點 → Sitemap 節點標亮`);
      await pg.click('#tb-persona');
      ok(await ev(() => document.querySelectorAll('#flow-body svg').length === 1 && document.querySelector('#pane-journey').hidden), `${tag} 切到 Persona 分頁，共用區塊保持篩選`);
      await pg.click('#pcard .all-btn[data-tab="journey"]');
      ok(await ev(() => !document.querySelector('#pane-journey').hidden), `${tag} persona 卡 → 跳到 Journey Map`);
    }
    ok(er.length === 0, `${tag} 無 JS 錯誤 ${er.join('|')}`);
    await pg.close();
  }
  await b.close();
  if (fails.length) { console.log('\n失敗 ' + fails.length + ' 項'); process.exit(1); }
  console.log('\n全部通過');
})();
