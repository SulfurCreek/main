/*AI-NOTE @part:sitemap
Sitemap 樹（renderSitemap）與對應文件表／文件關係表（renderDocs）。
資料：DATA.appendix.library（step0 產生的 sitemap_docs.json：modules[].tree／docs、relations）。
節點 id 規則 sm-{模組no}-{節點序}，Touchpoints 錨點依它跳轉。
維護：先讀 ../ROUTES.md；改完跑 ../build.sh --test
*/
// ---------- Sitemap ＋ 文件 ----------
const A = DATA.appendix;
$('ap-h').textContent = '對應文件';
$('lib-note').textContent = '依 HackMD Sitemap 對齊，只列文件名稱，點了開 HackMD。';
$('sm-note').textContent = '來源：HackMD Sitemap。預設顯示全部模組；選了階段，對應模組亮起。';
function renderSitemap() {
  const on = new Set(sel === null ? [] : modsOf(ST[sel].code).map(m => m.no));
  $('sm-tree').innerHTML = LIB.modules.map(m => {
    const cls = sel === null ? '' : on.has(m.no) ? ' lit' : ' dim';
    return '<div class="sm-mod' + cls + '"><h4><span class="n">' + esc(m.no) + '</span>' + esc(m.name) + '</h4>' + (m.tree.length ? '<div class="sm-list">' + m.tree.map((nd, k) =>
      '<div class="sm-node' + (nd.group ? ' grp' : '') + '" id="sm-' + m.no + '-' + k + '" style="margin-left:' + Math.max(0, nd.depth - 1) * 14 + 'px">' + esc(nd.name) +
      (nd.tag ? '<span class="mk usx">' + esc(nd.tag) + '</span>' : '') + '</div>').join('') + '</div>' : '<span class="none">Sitemap 無頁面</span>') + '</div>'; }).join('');
  if (sel !== null) { const first = document.querySelector('.sm-mod.lit'); if (first) $('sm-scroll').scrollTo({ top: first.offsetTop - 12 }); }
}
const stageName = code => { const st = ST.find(x => x.code === code || (code === '6／7' && x.code === '6')); return st ? dispCode(st) + ' ' + (introRow(st) ? introRow(st)[1] : stageLabel(st).name) : code; };
function renderDocs() {
  const mods = LIB.modules.filter(m => sel === null || modsOf(ST[sel].code).includes(m));
  $('doc-table').innerHTML = '<thead><tr><th>階段</th><th>Sitemap 模組</th><th>文件</th></tr></thead><tbody>' +
    mods.map(m => '<tr><td class="k">' + esc(stageName(m.stage)) + '</td><td class="k">' + esc(m.no + ' ' + m.name.replace(/（.*）/, '')) + '</td><td>' +
      (m.docs.length ? '<ul class="libdocs">' + m.docs.map(d => '<li><a href="' + BASE + d.shortId + '" target="_blank" rel="noopener">' + esc(d.title) + '</a></li>').join('') + '</ul>' : '<span class="none">Sitemap 未掛文件</span>') +
      '</td></tr>').join('') + '</tbody>';
  const rels = (LIB.relations || []).filter(r => sel === null || relCode(r) === null || relCode(r) === ST[sel].code);
  $('rel-table').innerHTML = '<thead><tr><th>階段</th><th>功能</th><th>文件</th></tr></thead><tbody>' + rels.map(r => '<tr><td class="k">' + esc(r.stage) + '</td><td class="k">' + esc(r.func) + '</td><td>' +
    '<ul class="libdocs">' + r.docs.map(d => '<li><a href="' + BASE + d.shortId + '" target="_blank" rel="noopener">' + esc(d.title) + '</a>' + (d.note ? '<span class="none">　' + esc(d.note) + '</span>' : '') + '</li>').join('') + '</ul></td></tr>').join('') + '</tbody>';
  $('rel-n').textContent = rels.length ? '（' + rels.length + ' 列）' : '';
}

