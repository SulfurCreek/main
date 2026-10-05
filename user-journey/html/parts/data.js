/*AI-NOTE @part:data
全站共用的資料對照與衍生值：ST（階段欄）、LIB（Sitemap／文件庫）、modsOf()、introRow()、stat()、relsOf()。
階段代碼對照的唯一入口：旅程看板最後一欄 code 是 '6'，Sitemap 模組 stage 是 '6／7'，由 modsOf() 處理。新增階段或改編碼，先改這裡。
全域狀態變數 sel（階段篩選）宣告在這個檔案；persona 狀態 pid 宣告在 persona.js。
維護：先讀 ../ROUTES.md；改完跑 ../build.sh --test
*/
// ---------- 資料對照 ----------
const G = DATA.grid, ST = G.stages, n = ST.length, LIB = DATA.appendix.library;
const isSupport = st => /支援/.test(st.name);
const stageLabel = st => { const m = st.name.match(/^(\S+)\s+(.*)$/) || [null, st.code, st.name]; return { code: m[1], name: m[2].replace(/（.*）$/, '') }; };
const modsOf = code => LIB.modules.filter(m => m.stage === code || (code === '6' && m.stage === '6／7'));
const introRow = st => IN.stage_rows.find(r => r[0] === st.code || r[0].split('／')[0] === st.code) || null;
const relCode = r => { const c = r.stage.split(/\s/)[0]; return c === '各階段' ? null : c === '6／7' ? '6' : c; };
const relsOf = code => (LIB.relations || []).filter(r => relCode(r) === code);
const stat = st => { const ms = modsOf(st.code);
  const ids = new Set([...ms.flatMap(m => m.docs.map(d => d.shortId)), ...relsOf(st.code).flatMap(r => r.docs.map(d => d.shortId))]);
  return { pages: ms.reduce((a, m) => a + m.tree.filter(x => !x.group).length, 0), docs: ids.size,
           flows: (DATA.flows || []).filter(f => f.stage === st.code).length }; };
const dispCode = st => { const r = introRow(st); return r ? r[0] : st.code; };

let sel = null;
