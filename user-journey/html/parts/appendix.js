/*AI-NOTE @part:appendix
附錄：共用元件、缺口、待辦。
資料：library.shared、appendix.gaps（痛點相關缺口已在 step1 濾掉）、DATA.todo。
維護：先讀 ../ROUTES.md；改完跑 ../build.sh --test
*/
// ---------- 附錄 ----------
$('shared').innerHTML = LIB.shared.map(d => '<a href="' + BASE + d.shortId + '" target="_blank" rel="noopener">' + esc(d.title) + '</a>').join('');
$('gap-h').textContent = A.gap_heading;
$('gap-list').innerHTML = A.gaps.map(g => '<li>' + md(g) + '</li>').join('');
$('todo-h').textContent = DATA.todo.heading;
$('todo-list').innerHTML = DATA.todo.items.map(i => '<li>' + md(i.text) + (i.children.length ? '<ul class="list">' + i.children.map(c => '<li>' + md(c) + '</li>').join('') + '</ul>' : '') + '</li>').join('');
$('foot').innerHTML = '<span>素材由文件助手維護：<code>user-journey/recruiter_journey_map.md</code></span><span>建置：<code>html/step0 → step1 → step2</code></span>';

