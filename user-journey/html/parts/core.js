/*AI-NOTE @part:core
DATA 注入點（__DATA__ 由 step2 替換）、$()/esc()/md() 工具、深淺色切換。
md() 是全站唯一的 mini-markdown：處理 `code`、**粗體**、[連結](url)、證據標記 US／US*／〔推論〕／NULL。改標記樣式只改這裡的 MK/marks。
不要在別處自己拼標記徽章；連結正則支援一層巢狀方括號（[[REF] 系統代碼表](url)）。
維護：先讀 ../ROUTES.md；改完跑 ../build.sh --test
*/
const DATA = __DATA__;
const $ = id => document.getElementById(id);
$('theme-toggle').onclick = () => {
  const r = document.documentElement, cur = r.getAttribute('data-theme');
  const dark = cur ? cur === 'dark' : matchMedia('(prefers-color-scheme: dark)').matches;
  r.setAttribute('data-theme', dark ? 'light' : 'dark');
};
const esc = s => String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');
const BASE = 'https://hackmd.io/@1111-jobdocs/';
const MK = /〔推論〕|(?<![A-Za-z])(?:US\*|US(?![A-Za-z])|NULL)/g;
const marks = t => t.replace(MK, m => m === '〔推論〕' ? '<span class="mk inf">推論</span>' : m === 'US*' ? '<span class="mk usx">US*</span>' : m === 'US' ? '<span class="mk us">US</span>' : '<span class="mk null">NULL</span>');
function md(raw) {
  const s = esc(String(raw).replace(/\\\*/g, '*')), out = []; let last = 0, m; const rx = /\[((?:[^\[\]]|\[[^\]]*\])+)\]\((https?:\/\/[^)\s]+)\)/g;
  const seg = t => marks(t.replace(/`(【[^】`]+】)`/g, '<span class="mk tag">$1</span>').replace(/`([^`]+)`/g, '<code>$1</code>').replace(/\*\*([^*]+)\*\*/g, '<b>$1</b>'));
  while ((m = rx.exec(s))) { out.push(seg(s.slice(last, m.index))); out.push('<a href="' + m[2] + '" target="_blank" rel="noopener">' + m[1] + '</a>'); last = rx.lastIndex; }
  out.push(seg(s.slice(last))); return out.join('');
}
const isLinkLine = p => /^(US\s*)?\[/.test(p.trim());

