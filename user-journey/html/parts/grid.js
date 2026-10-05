/*AI-NOTE @part:grid
Journey 看板：欄＝階段、列＝泳道（User Actions／Touchpoints／Thoughts／Emotions／Opportunities／Metrics）。cellHtml() 負責把一格 md 轉成 HTML。
資料：DATA.grid（step1 parse_grid）。痛點列已在 step1 隱藏（HIDE_LANES，使用者指示），前端不用處理。
Touchpoints 列不用 md 原文，改成 Sitemap 頁面名稱（tpHtml）；選了階段才變成錨點。Email 觸點取自原文 Email 行。
看板反灰分兩種 class：.dim（階段篩選，不可點）與 .pdim（persona 走不到，仍可點）。
維護：先讀 ../ROUTES.md；改完跑 ../build.sh --test
*/
// ---------- Journey Grid ----------
[$('grid-en').textContent, $('grid-h').textContent] = splitH(G.heading);
$('grid-intro').innerHTML = md(G.intro);
const board = $('board');
board.style.setProperty('--n', n);
function tpHtml(i) {
  const st = ST[i], link = sel === i, out = [];
  modsOf(st.code).forEach(m => m.tree.forEach((nd, k) => { if (nd.group) return;
    out.push(link ? '<a href="#sm-' + m.no + '-' + k + '" data-sm="sm-' + m.no + '-' + k + '">' + esc(nd.name) + '</a>' : esc(nd.name)); }));
  const mail = (st.cells['Touchpoints'] || '').split(/<br\s*\/?>/i).filter(x => /^Email[：:]/.test(x.trim()));
  return (out.length ? (link ? '<div class="tp">' + out.join('') + '</div>' : '<p class="tp-plain">' + out.join('<i>・</i>') + '</p>') : '<span class="none">Sitemap 無對應頁面</span>') + mail.map(x => '<div class="tp-mail">' + md(x) + '</div>').join('');
}
function cellHtml(raw, lane) {
  const t = raw.trim();
  if (/^NULL$/.test(t)) return '<span class="mk null">NULL</span>';
  const parts = t.split(/<br\s*\/?>/i);
  let main = parts.shift(), extra = [], cites = [];
  parts.forEach(p => (isLinkLine(p) ? cites : extra).push(p));
  const bm = main.match(/^(.*?)[；;]?\s*(依據[：:同].*)$/);
  if (bm && bm[1].trim()) { main = bm[1]; cites.unshift(bm[2]); }
  let body;
  if (lane === 'User Actions') body = '<ol class="steps">' + main.split(/\s*→\s*/).map(s => '<li>' + md(s) + '</li>').join('') + '</ol>';
  else if (lane === 'Emotions') { const em = main.match(/^(\p{Extended_Pictographic}️?)\s*(.*)$/u);
    body = em ? '<span class="emo" aria-hidden="true">' + em[1] + '</span><span class="emo-w">' + md(em[2]) + '</span>' : md(main); }
  else if (lane === 'Thoughts') body = md(main).replace(/「([^」]+)」/g, '<span class="q">「$1」</span>');
  else body = md(main);
  body += extra.map(p => '<div style="margin-top:6px">' + md(p) + '</div>').join('');
  return body + (cites.length ? '<div class="cite">' + cites.map(md).join('<br>') + '</div>' : '');
}
const cells = [];
const label = (en, zh, cls) => '<div class="rl ' + (cls || '') + '"><span class="en">' + esc(en) + '</span>' + (zh ? '<small>' + esc(zh) + '</small>' : '') + '</div>';
cells.push('<div class="rl grp">素材分表</div>');
G.groups.forEach(g => cells.push('<div class="grp" style="grid-column:span ' + g.count + '">' + esc(g.title) + '</div>'));
cells.push(label('Phases', '階段'));
ST.forEach((st, i) => { const L = stageLabel(st), note = st.name.match(/（(.*)）$/), r = introRow(st); if (r) L.name = r[1].replace(/（.*）/, '');
  cells.push('<div class="ph' + (isSupport(st) ? ' support' : '') + '" data-col="' + i + '" tabindex="0" role="button" aria-pressed="false"><span class="code">' + esc(dispCode(st)) + '</span><span class="nm">' +
    esc(L.name) + (note ? '<small>' + esc(note[1]) + '</small>' : '') + '</span><span class="pstat" aria-live="polite"></span></div>'); });
const CLS = { 'Opportunities': 'r-opp' };
G.lanes.forEach((ln, li) => {
  const last = li === G.lanes.length - 1 ? ' last' : '';
  cells.push(label(ln.en, ln.zh, (CLS[ln.en] || '') + last));
  ST.forEach((st, i) => cells.push('<div class="' + (CLS[ln.en] || '') + last + '" data-col="' + i + '"' + (ln.en === 'Touchpoints' ? ' data-tp="1"' : '') + '>' +
    (ln.en === 'Touchpoints' ? tpHtml(i) : cellHtml(st.cells[ln.en] || '', ln.en)) + '</div>'));
});
board.innerHTML = cells.join('');
board.addEventListener('mouseover', e => { const c = e.target.closest('[data-col]'); board.querySelectorAll('.col-hover').forEach(x => x.classList.remove('col-hover'));
  if (c && !c.classList.contains('dim')) board.querySelectorAll('[data-col="' + c.dataset.col + '"]').forEach(x => x.classList.add('col-hover')); });
board.addEventListener('mouseleave', () => board.querySelectorAll('.col-hover').forEach(x => x.classList.remove('col-hover')));
board.addEventListener('click', e => {
  const a = e.target.closest('a[data-sm]');
  if (a) { e.preventDefault(); const t = $(a.dataset.sm); if (!t) return;
    $('sitemap').scrollIntoView({ block: 'start' });
    const box = $('sm-scroll'); box.scrollTo({ top: t.offsetTop - 60, behavior: 'smooth' });
    t.classList.add('flash'); setTimeout(() => t.classList.remove('flash'), 1800); return; }
  const p = e.target.closest('.ph'); if (p && !p.classList.contains('dim')) setSel(+p.dataset.col); });
board.addEventListener('keydown', e => { const p = e.target.closest('.ph'); if (p && (e.key === 'Enter' || e.key === ' ') && !p.classList.contains('dim')) { e.preventDefault(); setSel(+p.dataset.col); } });

