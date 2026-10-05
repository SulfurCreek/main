/*AI-NOTE @part:route
Hero 路線圖（站點＝階段篩選）與捲動後的迷你路線列。
站點按鈕只呼叫 setSel()（定義在 apply.js）；不要在這裡直接改看板／Sitemap。
資料：stat() 的頁面／文件／流程圖數量來自 data.js。
維護：先讀 ../ROUTES.md；改完跑 ../build.sh --test
*/
// ---------- 路線圖（階段篩選） ----------
const mains = ST.map((st, i) => i).filter(i => !isSupport(ST[i])), spurs = ST.map((st, i) => i).filter(i => isSupport(ST[i]));
const stnHtml = i => { const st = ST[i], r = introRow(st), L = stageLabel(st), s = stat(st);
  return '<button type="button" class="stn" data-i="' + i + '" aria-pressed="false"><span class="dot">' + esc(dispCode(st)) + '</span><span class="txt">' +
    '<span class="nm">' + esc(r ? r[1] : L.name) + '</span>' + (r ? '<span class="ver">' + esc(r[2]) + '</span><span class="does">' + md(r[3]) + '</span>' : '') +
    '<span class="nums"><span>頁面 <b>' + s.pages + '</b></span><span>文件 <b>' + s.docs + '</b></span><span>流程圖 <b>' + (s.flows || '—') + '</b></span></span></span></button>'; };
$('main-line').style.setProperty('--m', mains.length);
$('main-line').innerHTML = mains.map(stnHtml).join('');
$('spur').innerHTML = '<span class="spur-tag">支線 · 任何階段可轉乘</span>' + spurs.map(stnHtml).join('');
$('route').addEventListener('click', e => { const b = e.target.closest('.stn'); if (b) setSel(+b.dataset.i); });
$('all-btn').onclick = () => setSel(null);
const mini = $('minirail');
mini.innerHTML = '<span class="tabsw" role="tablist" aria-label="切換檢視"><button type="button" role="tab" data-tab="persona">Persona</button><button type="button" role="tab" data-tab="journey">Journey Map</button></span><span class="lb">STAGE</span><button type="button" class="all" data-i="">全部</button>' +
  ST.map((st, i) => '<button type="button" data-i="' + i + '" class="' + (isSupport(st) ? 'sp' : '') + '"><i>' + esc(st.code) + '</i>' + esc(introRow(st) ? introRow(st)[1].replace(/（.*）/, '') : stageLabel(st).name) + '</button>').join('');
mini.addEventListener('click', e => { const b = e.target.closest('button[data-i]'); if (b) setSel(b.dataset.i === '' ? null : +b.dataset.i); });
if ('IntersectionObserver' in window) new IntersectionObserver(([en]) => mini.classList.toggle('show', !en.isIntersecting && en.boundingClientRect.top < 0)).observe($('tabs'));

