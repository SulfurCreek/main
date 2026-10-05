/*AI-NOTE @part:persona
Persona 分頁：總覽矩陣、P1~P7 卡、受限廠商卡、名詞表。狀態 pid（目前 persona）、modSel（疊加的受限類型）、mFilter。
資料：DATA.persona（step1 parse_persona）。stages[code].state ∈ ok／partial／conditional／blocked／unknown，由 step1 stage_states() 從「可走的旅程」文字轉出；顯示只讀這個狀態，不要在前端重新解析文字。
改完 persona 狀態要呼叫 renderPersona()＋applyPersona()（後者在 apply.js，負責旅程看板反灰）。
不要做：省略 NULL、替空欄補推論、改素材 md。
維護：先讀 ../ROUTES.md；改完跑 ../build.sh --test
*/
// ---------- Persona ----------
const splitH = h => { const m = h.replace(/^\d+\.\s*/, '').match(/^(.*?)\s*\((.*)\)$/); return m ? [m[1].replace(/^The\s+/, ''), m[2]] : ['', h]; };
$('ctx-h').textContent = P.heading.replace(/^\d+\.\s*/, '');
$('p-intro').innerHTML = md(P.intro);
$('p-scope').innerHTML = '<b>旅程範圍</b>　' + md(P.scope.replace(/^\*\*[^*]+\*\*\s*/, ''));
const ver = noteOf('新版'), opp = noteOf('Opportunities');
$('guide').innerHTML = '<span class="eyebrow">證據標記</span>' +
  '<div class="legend"><div><span class="mk us">US</span><span>真實 User Story</span></div><div><span class="mk usx">US*</span><span>套版句，只證明功能存在</span></div>' +
  '<div><span class="mk inf">推論</span><span>依同格文件事實推出</span></div><div><span class="mk null">NULL</span><span>文件未載，也無可推論</span></div><div><span style="font-size:0.72rem;color:var(--ink-3)">無標記</span><span>文件明載（附連結）</span></div></div>' +
  (ver ? '<p>' + md(ver) + '</p>' : '') + (opp ? '<p>' + md(opp) + '</p>' : '');

const SLAB = { ok: '可走', partial: '部分', conditional: '依權限', blocked: '不可', unknown: 'NULL' };
const grpOf = p => { const m = (p.overview[1] || '').match(/oStatus:(\d)/); const n = m ? +m[1] : -1; return n === 1 || n === 4 ? 'vip' : n === 3 ? 'warn' : 'neutral'; };
let pid = 'P3';   // 預設 P3＝全部階段（旅程看板主線）
const modSel = new Set(); let mFilter = null;
const pObj = () => P.personas.find(x => x.id === pid);
const modsOn = () => P.modifiers.items.filter((m, k) => modSel.has(k));
const interrupted = code => code !== 'J' && modsOn().some(m => m.stages.J === '中斷');
const reach = code => { const s = pObj().stages[code]; return !!s && ['ok', 'partial', 'conditional'].includes(s.state) && !interrupted(code); };

$('p-matrix').innerHTML = '<thead><tr>' + P.overview.hdr.map(h => '<th>' + esc(h) + '</th>').join('') + '</tr></thead><tbody>' +
  P.personas.map(p => { const r = p.overview, g = grpOf(p);
    return '<tr data-p="' + p.id + '"><td><button type="button" class="pn" data-p="' + p.id + '"><span class="pid">' + p.id + '</span>' + esc(p.name.replace(/^P\d+\s*/, '')) + '</button></td>' +
      '<td><span class="chip ' + g + '">' + md(r[1] || 'NULL') + '</span></td><td>' + (/^NULL/.test(r[2] || 'NULL') ? md(r[2] || 'NULL') : '<span class="chip neutral">' + md(r[2]) + '</span>') + '</td>' +
      '<td>' + md(r[3] || 'NULL') + '</td><td>' + md(r[4] || 'NULL') + '</td></tr>'; }).join('') + '</tbody>';
$('p-notes').innerHTML = P.overview.notes.map(n => '<li>' + md(n) + '</li>').join('');
$('p-matrix').addEventListener('click', e => { const b = e.target.closest('button[data-p]'); if (!b) return; setPersona(b.dataset.p); $('pcard-top').scrollIntoView({ block: 'start' }); });

const ICON_OK = '<svg viewBox="0 0 16 16" aria-hidden="true"><circle cx="8" cy="8" r="7" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M4.6 8.3l2.2 2.2 4.6-4.9" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>';
const ICON_WARN = '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M8 1.8l6.6 11.6H1.4z" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/><path d="M8 6.2v3.4M8 11.4v.2" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>';
const list = it => {
  const hasKids = it.children.length;
  if (!it.text && hasKids) return '<ul>' + it.children.map(c => '<li>' + md(c) + '</li>').join('') + '</ul>';
  return '<ul><li>' + md(it.text) + (hasKids ? '<ul>' + it.children.map(c => '<li>' + md(c) + '</li>').join('') + '</ul>' : '') + '</li></ul>';
};
const splitQuote = q => { const m = q.replace(/^>\s*/, '').match(/^(.*?)(〔推論〕.*)$/); return m ? [m[1], m[2]] : [q, '']; };
function renderPersona() {
  const p = pObj(), by = k => p.items.find(i => i.key.startsWith(k)), g = grpOf(p), r = p.overview;
  $('ptabs').innerHTML = P.personas.map(x => '<button type="button" role="tab" id="tab-' + x.id + '" data-p="' + x.id + '" aria-selected="' + (x.id === pid) + '"><span class="st ' + grpOf(x) + '"></span><b>' + x.id + '</b>' + esc(x.name.replace(/^P\d+\s*/, '')) + '</button>').join('');
  $('pcard').setAttribute('aria-labelledby', 'tab-' + pid);
  const [qt, qwhy] = splitQuote(p.quote);
  const det = by('Details'), goal = by('Goals'), pain = by('Pain'), ml = modsOn();
  $('pcard').innerHTML =
    '<blockquote class="pq"><div class="head"><span class="pid">' + p.id + '</span><h3>' + esc(p.name.replace(/^P\d+\s*/, '')) + '</h3><span class="chip ' + g + '">' + md(r[1] || 'NULL') + '</span>' +
    (r[2] ? '<span class="chip neutral">' + md(r[2]) + '</span>' : '') + '</div><div class="qt">' + md(qt) + '</div>' + (qwhy ? '<div class="why">' + md(qwhy) + '</div>' : '') + '</blockquote>' +
    '<div class="pgrid"><div class="pcol">' + (det ? '<div class="box profile"><h4>Details</h4>' + list(det) + '</div>' : '') + '</div>' +
    '<div class="pcol">' + (goal ? '<div class="box goals"><h4>' + ICON_OK + 'Goals</h4>' + list(goal) + '</div>' : '') +
    (pain ? '<div class="box pains"><h4>' + ICON_WARN + 'Pain Points</h4>' + list(pain) + '</div>' : '') + '</div></div>' +
    '<div class="journey"><div style="display:flex;justify-content:space-between;gap:8px;flex-wrap:wrap;align-items:center"><h4>可走的旅程</h4><button type="button" class="all-btn" data-tab="journey">在 Journey Map 看 ' + p.id + ' →</button></div><p class="jtxt">' + md(p.journey_text) + '</p><div class="jrow">' +
    P.stages9.map(s => { const st = p.stages[s.code] || { state: 'unknown', note: '' }, lim = ml.filter(m => m.stages[s.code]), off = interrupted(s.code);
      return '<div class="sc ' + (off ? 'blocked' : st.state) + (lim.length ? ' mod' : '') + '" title="' + esc(lim.map(m => m.name).join('、')) + '"><b>' + s.code + '</b><span>' + s.name + '</span><em>' + (off ? '不可登入中斷' : SLAB[st.state]) + (st.note && st.state !== 'ok' ? '｜' + esc(st.note) : '') + (lim.length ? '｜受限 ' + lim.length : '') + '</em></div>'; }).join('') + '</div>' +
    (ml.length ? '<div class="ovl">疊加中：' + ml.map(m => esc(m.name)).join('、') + '　（黃底線＝該階段受影響）</div>' : '') + '</div>';
}
$('ptabs').addEventListener('click', e => { const b = e.target.closest('button[data-p]'); if (b) setPersona(b.dataset.p); });
$('ptabs').addEventListener('keydown', e => { if (e.key !== 'ArrowRight' && e.key !== 'ArrowLeft') return; const i = P.personas.findIndex(x => x.id === pid), n2 = (i + (e.key === 'ArrowRight' ? 1 : -1) + P.personas.length) % P.personas.length;
  setPersona(P.personas[n2].id); $('tab-' + P.personas[n2].id).focus(); });

// 受限廠商類型
const mPill = (c) => c === 'ALL' ? '全部' : c;
$('m-intro').innerHTML = md(P.modifiers.intro);
$('mfilter').innerHTML = '<span class="lb">受影響階段</span>' + ['ALL', ...P.stages9.map(s => s.code)].map(c => '<button type="button" data-f="' + c + '" aria-pressed="' + (c === 'ALL') + '">' + (c === 'ALL' ? '全部' : c + ' ' + P.stages9.find(s => s.code === c).name) + '</button>').join('');
function renderMods() {
  $('mods').innerHTML = P.modifiers.items.map((m, k) => (mFilter && !m.stages[mFilter]) ? '' :
    '<button type="button" class="mod" data-k="' + k + '" aria-pressed="' + modSel.has(k) + '"><span class="top"><h4>' + esc(m.name) + '</h4><span class="tick">' + (modSel.has(k) ? '已疊加' : '疊加') + '</span></span>' +
    '<span class="code">' + esc(m.flag.replace(/`/g, '')) + '</span><p>' + md(m.limit) + '</p><span class="imp">' + Object.entries(m.stages).map(([c, v]) => '<span>' + c + (v === '中斷' ? ' 中斷' : '') + '</span>').join('') + '</span></button>').join('');
  $('mfilter').querySelectorAll('button').forEach(b => b.setAttribute('aria-pressed', String((b.dataset.f === 'ALL' ? null : b.dataset.f) === mFilter)));
}
$('mfilter').addEventListener('click', e => { const b = e.target.closest('button[data-f]'); if (!b) return; mFilter = b.dataset.f === 'ALL' ? null : b.dataset.f; renderMods(); });
$('mods').addEventListener('click', e => { const b = e.target.closest('button[data-k]'); if (!b) return; const k = +b.dataset.k; modSel.has(k) ? modSel.delete(k) : modSel.add(k); renderMods(); renderPersona(); applyPersona(); });
$('m-notes').innerHTML = P.modifiers.notes.map(n => '<li>' + md(n) + '</li>').join('');

// 名詞
$('g-n').textContent = '（' + P.terms.rows.length + ' 條）';
$('terms').innerHTML = P.terms.rows.map(r => '<div><dt>' + md(r[0]) + '</dt><dd>' + md(r[1]) + (r[2] && r[2] !== '—' ? '<span class="src">' + md(r[2]) + '</span>' : '') + '</dd></div>').join('');
$('g-note').innerHTML = md(P.terms.note.replace(/^標記：/, '標記：'));

