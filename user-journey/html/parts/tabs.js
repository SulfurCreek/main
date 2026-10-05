/*AI-NOTE @part:tabs
分頁（Persona／Journey Map）與初始化。最後一個 JS 檔：這裡呼叫所有 render*() 做首次繪製。
Sitemap／文件／流程圖／附錄不在分頁內，兩分頁共用，所以不要把它們搬進 pane。
分頁記憶：localStorage 'uj-tab'；網址 #journey／#persona 可直達。新增分頁：改 tabs.html（tab 按鈕＋pane）、這裡的 setTab()。
維護：先讀 ../ROUTES.md；改完跑 ../build.sh --test
*/
// ---------- 分頁：Persona／Journey Map；下方 Sitemap、文件、流程圖共用 ----------
function setTab(t, scroll) {
  ['persona', 'journey'].forEach(k => { $('pane-' + k).hidden = k !== t; });
  document.querySelectorAll('[data-tab]').forEach(b => b.setAttribute('aria-selected', String(b.dataset.tab === t)));
  try { localStorage.setItem('uj-tab', t); } catch (e) {}
  if (scroll && $('tabs').getBoundingClientRect().top < 0) $('tabs').scrollIntoView({ block: 'start' });
}
document.addEventListener('click', e => { const b = e.target.closest('button[data-tab]'); if (b) setTab(b.dataset.tab, true); });
$('tabs').addEventListener('keydown', e => { if (e.key !== 'ArrowRight' && e.key !== 'ArrowLeft') return; const t = $('tb-persona').getAttribute('aria-selected') === 'true' ? 'journey' : 'persona'; setTab(t); $('tb-' + t).focus(); });
let tab0 = location.hash === '#journey' ? 'journey' : location.hash === '#persona' ? 'persona' : null;
if (!tab0) { try { tab0 = localStorage.getItem('uj-tab'); } catch (e) {} }
setTab(tab0 === 'journey' ? 'journey' : 'persona');

renderPersona(); renderMods(); applyPersona();
setSel(null);
