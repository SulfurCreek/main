#!/usr/bin/env python3
"""履歷機械檢查（規準 v4，2026-10-13；依 career/style/scoring-improvement-v4-source.md）。

v4 只報「檢查結果與描述性統計」，**不產生任何能力分數**：
- 舊 B（關鍵字 70–90% 甜蜜區間、≥95% 扣分、經歷＋技能重複加分）→ 刪除。改為逐項能力證據對應（含同義詞），
  列出每個詞在哪一段有證據；無關重複另列可讀性提醒。
- 舊 C（左緣 10 字、抬頭 24 字換成分數）→ 只當版面提醒（可讀性以實際排版另驗）。
- 舊 D（含數字條列 ≥60% 得滿分、職責式開頭每處 −2）→ 數字比例只作描述；「負責／協助／參與」不扣分，
  只有該條列看不出具體貢獻時才標「貢獻待釐清」。
- 禁用詞拆成 style_lint（使用者語氣偏好，editorial）與 factual_guard（事實禁寫）；兩者都不影響 Level。

用法：
  python3 resume_score.py stats <resume.txt> --jd "PRD,UAT,跨部門,..."     # ats 為舊名，仍可用
  python3 resume_score.py variants <variants.md> --jd "..."               # 只輸出 lint，不排分數
"""
import argparse, re

NUM = re.compile(r'\d')
EDGE, HEADER_CHARS = 10, 24
DATE = re.compile(r'\d{4}/\d{1,2}\s*[-–~至]\s*(?:\d{4}/\d{1,2}|迄今|至今|Present)')
DUTY_START = re.compile(r'^(主責|負責|職責|協助|參與|處理|管理|Responsible|Managed|Worked|Assisted|Helped)')
RESULT_VERB = ['主導', '上線', '降到', '降至', '提升', '成長', '→', '縮短', '增加', '減少', '導入', '推進', '規劃', '選擇', '改用', '完成']
TITLE_WORDS = ['經理', 'Manager', 'PM', 'Owner', '主任', '企劃', '工程師', '專員', '工讀生', 'Intern',
               'Lead', 'Director', '總監', '主管', '顧問', 'Analyst', '分析師', '設計師']
OBJECTIVE = ['希望', '尋求', '期望', '追求', '挑戰性', '發揮所長', '貢獻所學', '學習成長', 'Seeking', 'Objective']

# 使用者語氣偏好與去 AI 腔（editorial；不影響能力判斷）
STYLE_LINT = ['致力於', '深入探討', '扮演關鍵角色', '成功實現', '無縫', '編織', 'Spearheaded', 'Architected',
              '具備良好', '熱情洋溢', '賦能', '至關重要', '不可或缺', '值得注意的是', '總而言之', '展現了',
              '充滿熱情', '積極進取', '期許自己', '挑戰自我', '團隊合作能力', '抗壓性極佳',
              '0 到 1', '從 0 到 1', '0→1', '每個功能', '都由我', '一路帶', '全部由我', '所有功能']
# 事實禁寫（事實快照 career/library/fact-snapshot-2026-10-13.md；命中＝需事實核對，不是語氣問題）
FACTUAL_GUARD = {'準時': '準時率已刪（定義不明，superseded）', '職缺匯入': '尚未開發，不得列為已上線',
                 '4 項 AI': '已上線 AI 功能為 3 項', '東南亞金流': '使用者改口徑：IAP 與 Web 金流',
                 'JD2': '一律寫 JustDating', 'SQL': '使用者未確認具備', 'Jira': '使用者未確認具備',
                 'Scrum': '開發方式是瀑布＋Kanban', '零停機': '實際停機約 1.5 小時',
                 '前任主管未': '組織負面敘事', '停擺': '組織負面敘事'}
# 同義詞：英文關鍵字換成意思清楚的中文，不應被判為缺證據（迴歸案例 10）
SYN = {'prd': ['prd', '規格', '需求文件'], 'uat': ['uat', '驗收'], 'roadmap': ['roadmap', '路線圖', '優先級', '排優先'],
       '跨部門': ['跨部門', '對接', '協調', '需求單位'], 'ai': ['ai', 'claude', '資料科學'], 'api': ['api', '串接'],
       '金流': ['金流', '付款', 'iap', 'codapay', '內購'], '數據': ['數據', 'ga4', '世代分析', '分析'],
       'figma': ['figma', 'wireframe', 'prototype', '原型'], 'b2b': ['b2b', '企業端', '廠商', 'saas'],
       '使用者訪談': ['使用者訪談', '訪談', '問卷'], 'agile': ['agile', 'kanban', '敏捷'], '英文': ['英文', 'toeic', 'toefl', 'english']}


def vw(t):
    return sum(0.5 if ord(c) < 0x2E80 else 1 for c in t)


def cut(t, w):
    out, n = '', 0
    for c in t:
        n += vw(c)
        if n > w: break
        out += c
    return out


def kw_list(s):
    return [k.strip() for k in (s or '').split(',') if k.strip()]


def where(text, kw):
    """回傳證據所在段落（摘要／經歷／技能／自傳），含同義詞。"""
    alts = SYN.get(kw.lower(), [kw.lower()])
    secs = re.split(r'\n(專業摘要|工作經歷|學歷|專業技能|求職條件|自傳)\n', '\n' + text)
    out, name = [], '抬頭'
    for i, part in enumerate(secs):
        if part in ('專業摘要', '工作經歷', '學歷', '專業技能', '求職條件', '自傳'):
            name = part; continue
        low = part.lower()
        if any((re.search(r'(?<![a-z])' + re.escape(a) + r'(?![a-z])', low) if a.isascii() else a in low) for a in alts): out.append(name)
    return sorted(set(out))


def lint(text):
    style = [w for w in STYLE_LINT if w in text]
    if '—' in text or '**' in text: style.append('破折號或粗體')
    guard = [f'{k}（{v}）' for k, v in FACTUAL_GUARD.items() if k in text]
    return style, guard


def contribution_gap(b):
    """誠實協作描述不扣分；只有看不出具體動作或結果時才標待釐清。"""
    return bool(DUTY_START.match(b)) and not NUM.search(b) and not any(v in b for v in RESULT_VERB)


def cmd_stats(path, jd):
    text = open(path, encoding='utf8').read()
    lines = [l.strip() for l in text.split('\n')]
    exp = text.split('\n學歷')[0]
    bullets = [l[2:] for l in exp.split('\n') if l.startswith('- ')]
    nb = max(len(bullets), 1)
    print('## 機械檢查 v4（只報結果，不轉能力分；human_calibration: not_performed）\n')
    if jd:
        print('### 能力證據對應（含同義詞；不設覆蓋率甜蜜區間）')
        for k in jd:
            w = where(text, k)
            only_skill = w == ['專業技能']
            print(f'- {k}：{"、".join(w) or "unknown（未寫，不推論不會）"}{"（只在技能索引，經歷無證據）" if only_skill else ""}')
    numr = sum(1 for b in bullets if NUM.search(b)) / nb
    edge = sum(1 for b in bullets if NUM.search(cut(b, EDGE)) or any(v in cut(b, EDGE) for v in RESULT_VERB + jd)) / nb
    heads = [l for l in exp.split('\n') if '｜' in l and DATE.search(l)]
    late = [h[:20] for h in heads if vw(h[:DATE.search(h).start()]) >= HEADER_CHARS]
    print('\n### 描述性統計（不換算影響力）')
    print(f'- 工作經歷條列 {len(bullets)} 條；含數字 {numr:.0%}（有數字≠有影響，數字性質由內容審查分類）')
    print(f'- 條列左緣 10 字寬有數字或動作詞 {edge:.0%}（版面提醒）')
    print(f'- 經歷抬頭 {len(heads)} 段；日期超過 24 字寬：{"、".join(late) or "無"}（版面提醒，以實際排版另驗）')
    summ = text.split('專業摘要')[1].split('工作經歷')[0] if '專業摘要' in text else ''
    obj = [o for o in OBJECTIVE if o in summ]
    print(f'- 摘要求職目標語：{"、".join(obj) or "無"}')
    gaps = [b[:24] for b in bullets if contribution_gap(b)]
    print(f'- 貢獻待釐清（協作動詞開頭且無具體動作或結果）：{"；".join(gaps) or "無"}')
    style, guard = lint(text)
    print('\n### style_lint（使用者偏好，editorial）：' + ('、'.join(style) or '無'))
    print('### factual_guard（事實禁寫，需事實核對）：' + ('、'.join(guard) or '無'))
    print('\nA 格式：career-ops verify-ats；PDF：parse_check.py；ATS import: not tested。')


def cmd_variants(path, jd):
    unit = None
    print('| 單位 | 版本 | 字數 | 含數字 | style_lint | factual_guard | 貢獻待釐清 |')
    print('| :-- | :-- | :-: | :-: | :-- | :-- | :-: |')
    for line in open(path, encoding='utf8'):
        m = re.match(r'###\s+(\S+)', line)
        if m: unit = m.group(1); continue
        m = re.match(r'(V\d+)\s*[:：]\s*(.+)', line.strip())
        if m and unit:
            t = m.group(2); s, g = lint(t)
            print(f'| {unit} | {m.group(1)} | {len(t)} | {"有" if NUM.search(t) else "無"} | {"、".join(s)} | {"、".join(g)} | {"是" if contribution_gap(t) else ""} |')


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('mode', choices=['stats', 'ats', 'variants'])
    ap.add_argument('path')
    ap.add_argument('--jd', default='')
    ap.add_argument('--preferred', default='')  # 舊參數，v4 併入 --jd 對應
    a = ap.parse_args()
    if a.mode == 'variants': cmd_variants(a.path, kw_list(a.jd))
    else: cmd_stats(a.path, kw_list(a.jd) + kw_list(a.preferred))
