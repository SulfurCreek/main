/*AI-NOTE @part:hero
標題、lead、meta 與 eyebrow（取自 DATA.title／intro／persona.scope）。
資料：DATA.intro.notes 的「這是什麼」段落當 lead。
維護：先讀 ../ROUTES.md；改完跑 ../build.sh --test
*/
// ---------- Hero ----------
const tm = DATA.title.match(/^(.*?)\s*(User Journey Map)\s*(（.*）)?$/);
$('ttl').innerHTML = tm ? esc(tm[1]) + '<span class="who">' + esc(tm[3] || '') + '</span><span class="en">' + esc(tm[2]) + '</span>' : esc(DATA.title);
const IN = DATA.intro, noteOf = k => IN.notes.find(t => t.startsWith('**' + k));
const what = noteOf('這是什麼');
$('lead').innerHTML = what ? md(what.replace(/^\*\*[^*]+\*\*[：:]\s*/, '')) : '';
const P = DATA.persona;
$('eyebrow').textContent = '1111 求才系統 · ' + (P.scope.split(/[（(]/)[0].trim() || 'User Journey');
const srcDate = (DATA.head_bullets[0] || '').match(/(\d{4}-\d{2}-\d{2})\s*擷取/);
$('meta').innerHTML = (srcDate ? '<span>素材擷取 <b>' + srcDate[1] + '</b></span>' : '') +
  '<span>素材 <code>user-journey/recruiter_journey_map.md</code></span>' +
  '<details><summary>素材說明</summary><ul>' + DATA.head_bullets.map(b => '<li>' + md(b) + '</li>').join('') + '</ul></details>';

