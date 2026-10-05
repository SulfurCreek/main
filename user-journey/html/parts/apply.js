/*AI-NOTE @part:apply
連動中樞：persona 套用到看板（applyPersona）、setPersona()、persona 選擇器、setSel()（階段篩選）。
setSel() 一次連動：路線圖／迷你列／看板欄／Touchpoints／renderFlow／renderDocs／renderSitemap。新增一個依階段變動的區塊，把它的 render 函式加進 setSel() 最後一行。
setPersona() → renderPersona()＋applyPersona()。
維護：先讀 ../ROUTES.md；改完跑 ../build.sh --test
*/
// ---------- persona 套用到旅程看板 ----------
const colCodes = i => ST[i].code === '6' ? ['6', '7'] : [ST[i].code];
const colReach = i => colCodes(i).some(reach);
function applyPersona() {
  const p = pObj(), ml = modsOn();
  board.querySelectorAll('[data-col]').forEach(el => el.classList.toggle('pdim', !colReach(+el.dataset.col)));
  board.querySelectorAll('.ph').forEach(el => { const i = +el.dataset.col, codes = colCodes(i), sts = codes.map(c => interrupted(c) ? 'blocked' : (p.stages[c] || { state: 'unknown' }).state);
    const uniq = [...new Set(sts)], lim = ml.filter(m => codes.some(c => m.stages[c]));
    el.querySelector('.pstat').innerHTML = (pid === 'P3' && !ml.length ? '' : uniq.map(u => '<span class="pst ' + u + '">' + (codes.length > 1 && uniq.length > 1 ? codes[sts.indexOf(u)] + ' ' : '') + SLAB[u] + '</span>').join('')) +
      (lim.length ? '<span class="pst warn" title="' + esc(lim.map(m => m.name).join('、')) + '">受限 ' + lim.length + '</span>' : ''); });
  document.querySelectorAll('.stn').forEach(b => b.classList.toggle('unreach', !colReach(+b.dataset.i)));
  mini.querySelectorAll('button[data-i]:not([data-i=""])').forEach(b => b.classList.toggle('unreach', !colReach(+b.dataset.i)));
  $('p-matrix').querySelectorAll('tbody tr').forEach(tr => tr.classList.toggle('on', tr.dataset.p === pid));
  $('ppick').querySelectorAll('button').forEach(b => b.setAttribute('aria-pressed', String(b.dataset.p === pid)));
}
function setPersona(id) { pid = id; renderPersona(); applyPersona(); }
$('ppick').innerHTML = '<span class="lb">以哪個 persona 看</span>' + P.personas.map(x => '<button type="button" data-p="' + x.id + '" aria-pressed="false"><span class="st ' + grpOf(x) + '"></span><b>' + x.id + '</b>' + esc(x.name.replace(/^P\d+\s*/, '')) + '</button>').join('');
$('ppick').addEventListener('click', e => { const b = e.target.closest('button[data-p]'); if (b) setPersona(b.dataset.p); });

function setSel(i) {
  sel = (i !== null && sel === i) ? null : i;
  document.querySelectorAll('.stn').forEach(b => b.setAttribute('aria-pressed', String(sel !== null && +b.dataset.i === sel)));
  $('route').classList.toggle('has-sel', sel !== null);
  $('all-btn').setAttribute('aria-pressed', String(sel === null));
  mini.querySelectorAll('button').forEach(b => b.setAttribute('aria-pressed', String(b.dataset.i === '' ? sel === null : +b.dataset.i === sel)));
  board.querySelectorAll('[data-col]').forEach(el => { const on = sel === null || +el.dataset.col === sel;
    el.classList.toggle('dim', !on); el.classList.toggle('sel', sel !== null && on);
    if (el.classList.contains('ph')) { el.setAttribute('aria-disabled', on ? 'false' : 'true'); el.setAttribute('aria-pressed', String(sel !== null && on)); } });
  board.querySelectorAll('[data-tp]').forEach(el => { el.innerHTML = tpHtml(+el.dataset.col); });
  const tag = sel === null ? '' : '目前階段：' + dispCode(ST[sel]) + ' ' + (introRow(ST[sel]) ? introRow(ST[sel])[1] : stageLabel(ST[sel]).name);
  ['sm-sel', 'fl-sel'].forEach(id => { $(id).textContent = tag; $(id).hidden = sel === null; });
  renderFlow(); renderDocs(); renderSitemap();
}

