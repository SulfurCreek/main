#!/usr/bin/env python3
"""規準 v4 確定性迴歸測試（答案在執行前固定；不是真人招聘效度證明）。
執行：python3 .claude/skills/resume-review-panel/tests/test_v4_rules.py
語義類案例（需模型）見 ../regression-v4.md，結果寫在各次 runs 報告。
"""
import importlib.util, subprocess, sys, os, tempfile, json
H = os.path.dirname(os.path.abspath(__file__)); R = os.path.dirname(os.path.dirname(H))
def mod(path, name):
    s = importlib.util.spec_from_file_location(name, path); m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
rs = mod(f'{R}/resume-craft/scripts/resume_score.py', 'rs')
sv = mod(f'{H}/../scripts/schema_v4.py', 'sv')
res = []
def case(cid, desc, ok):
    res.append((cid, desc, ok)); print(('✅' if ok else '❌'), cid, desc)

BASE = "姓名\n資深產品經理\nx@y.com\n\n專業摘要\n摘要一句。\n\n工作經歷\n\nPM｜某公司｜2022/08 - 迄今\n- {b}\n\n學歷\n某大學｜2010/09 - 2014/06\n\n專業技能\n- 產品文件：PRD\n"
def stats(b, jd='PRD,驗收'):
    f = tempfile.NamedTemporaryFile('w', suffix='.txt', delete=False, encoding='utf8'); f.write(BASE.format(b=b)); f.close()
    return subprocess.run([sys.executable, f'{R}/resume-craft/scripts/resume_score.py', 'stats', f.name, '--jd', jd], capture_output=True, text=True).stdout

# R01 主責→負責：機械檢查不得因動詞不同出現差異（除貢獻待釐清以外的評價）
a = stats('主責規劃約 50 項大項功能，與工程協作上線'); b = stats('負責規劃約 50 項大項功能，與工程協作上線')
case('R01', '「主責」改「負責」（同事實、有具體動作）→ 機械輸出相同', a.replace('主責', '負責') == b)
# R01b 誠實協作描述不扣分
case('R01b', '「協助／參與」有具體動作或結果 → 不標貢獻待釐清', not rs.contribution_gap('參與定價實驗，降價期 iOS 營收 +5%'))
case('R01c', '只有「協助處理相關事務」→ 標貢獻待釐清（缺口，不是扣分）', rs.contribution_gap('協助處理相關事務'))
# R03 加入無關日期或計數：不產生任何影響力分數
out = stats('主責規劃約 50 項大項功能（2023/12–2026/03），共 3 次會議')
case('R03', '加入無關日期／計數 → 輸出不含任何分數（/25、/20）', '/25' not in out and '/20' not in out)
# R10 英文關鍵字換成中文同義詞：不應判為缺證據
o1 = stats('與 QA 制定驗收案例', jd='UAT'); 
case('R10', 'JD 寫 UAT、履歷寫「驗收」→ 仍找到證據', 'UAT：unknown' not in o1)
# R11 JD 未要求：機械檢查不得把照片／英文版／人員管理列為缺失
case('R11', '機械輸出不出現「照片／英文版／帶人」缺失', not any(w in out for w in ('照片', '英文版', '帶人')))
# 禁用詞分流
s, g = rs.lint('Peach 從 0 到 1 上線；導入東南亞金流；有排定日期的 89 項中 84 項準時')
case('LINT', '「0 到 1」入 style_lint、「東南亞金流／準時」入 factual_guard', '0 到 1' in s and any('東南亞金流' in x for x in g) and any('準時' in x for x in g))
# R12 大項與細項並列：機械檢查不判矛盾
case('R12', '「約 50 項大項」與「111 項細項」並列 → 不觸發 factual_guard', not rs.lint('約 50 項大項功能；另 111 項 Roadmap 細項')[1])
# Schema：只有 contradicted 可阻擋面試；unknown 不可
bad = {'rubric_version': '4.0', 'human_calibrated': False, 'dimensions': [{'id': d, 'rating': '足夠'} for d in sv.DIMS],
       'requirements': [{'id': 'R1', 'status': 'unknown', 'blocks_interview': True}], 'issues': [], 'results': [],
       'decision': {'recommendation': 'interview'}, 'tests': {'pdf_extraction': 'not_tested', 'ats_import': 'not_tested', 'ai_provenance': 'indeterminate_from_text_alone'}}
case('SCHEMA-1', 'requirement 為 unknown 卻阻擋面試 → 驗證失敗', any('只有 contradicted' in e for e in sv.check(bad)))
bad['requirements'][0]['blocks_interview'] = False
case('SCHEMA-2', '合法輸出 → 驗證通過', sv.check(bad) == [])
bad['dimensions'][0]['rating'] = 0
case('SCHEMA-3', '未知用 0 分 → 驗證失敗（未呈現不記零分）', bool(sv.check(bad)))
# R14 同一缺口去重
case('R14', '同一 claim 不同標點 → 去重鍵相同', sv.norm_claim('「約 50 項大項功能上線」') == sv.norm_claim('約 50 項大項功能上線'))
case('KW-1', 'Email「gmail」不可被當成 AI 證據（英數詞需字界）', rs.where('姓名\nx@gmail.com\n\n專業摘要\n摘要\n', 'AI') == [])
fails = [r for r in res if not r[2]]
print(f'\n{len(res) - len(fails)}/{len(res)} 通過')
json.dump([{'id': c, 'desc': d, 'pass': o} for c, d, o in res], open(os.path.join(H, 'last-result.json'), 'w'), ensure_ascii=False, indent=1)
sys.exit(1 if fails else 0)
