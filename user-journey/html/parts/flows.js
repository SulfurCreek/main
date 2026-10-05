/*AI-NOTE @part:flows
流程圖區塊：進頁空狀態，選了階段才把 SVG 放進 DOM。
資料：DATA.flows（step1 讀〈流程圖索引〉＋step0 用 mermaid-cli 產的 SVG，存在 flows/）。
維護：先讀 ../ROUTES.md；改完跑 ../build.sh --test
*/
// ---------- 流程圖：進頁空狀態，選了階段才載入 SVG ----------
function renderFlow() {
  const body = $('flow-body');
  if (sel === null) { body.innerHTML = '<div class="blank"><div><b>先選一個階段</b>在上方路線圖點站點，這裡會載入該階段的所有流程圖。</div></div>'; return; }
  const code = ST[sel].code, items = (DATA.flows || []).filter(f => f.stage === code);
  if (!items.length) { body.innerHTML = '<div class="blank"><div><b>' + esc(dispCode(ST[sel]) + ' ' + stageLabel(ST[sel]).name) + ' 還沒有流程圖</b>留白，內容待補。</div></div>'; return; }
  body.innerHTML = items.map(f =>
    '<article class="flow-item"><h3>' + esc(f.name) + '</h3><div class="meta">' + esc(f.type) + '　·　來源文件 ' +
    (f.link ? '<a href="' + esc(f.link) + '" target="_blank" rel="noopener">' + esc(f.doc_title) + '</a>' : esc(f.doc_title)) + '</div>' +
    (f.svgs.length ? f.svgs.map(v => '<div class="flow-canvas" role="img" aria-label="' + esc(f.name) + '">' + v + '</div>').join('') : '<div class="blank" style="min-height:120px"><div>留白，內容待補</div></div>') + '</article>').join('');
  document.querySelectorAll('.flow-canvas').forEach(c => c.setAttribute('tabindex', '0'));
}

