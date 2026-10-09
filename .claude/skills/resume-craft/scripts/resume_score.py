#!/usr/bin/env python3
"""履歷機械評分（resume-craft 工作流程步驟 4 與 7 用）。

只算得出來的部分；事實一致、語氣、HR／主管判斷由模型在報告裡人工給分。

用法：
  python3 resume_score.py variants <variants.md> --jd "PRD,UAT,跨部門,..."
      variants.md 格式：每個單位一段「### U01 標題」，下面每行「V01: 文字」…「V20: 文字」。
      輸出每個版本的機械分（0–40）與旗標，供人工再加 0–60 分。
  python3 resume_score.py ats <resume.txt> --jd "必備詞,..." --preferred "加分詞,..."
      依 career/style/ats-2026-source.md 算分表算 B（關鍵字對應）、C（6 秒 F 型可讀，v2）、D（量化），
      A（格式）請用 career-ops verify-ats，E（AI 實證）人工。

2026-10-09 起依 career/style/hr-6-second-source.md 加：左緣 10 字訊號、職責式開頭、求職目標語、
經歷抬頭「職稱在左、日期在 24 字內」。C 分算法改為 v2，與先前版本的 C 分不可直接比較。
"""
import argparse, re, sys

BANNED = ['致力於', '深入探討', '扮演關鍵角色', '成功實現', '無縫', '編織', 'Spearheaded', 'Architected',
          '協助', '參與', '負責', '具備良好', '熱情洋溢', '賦能']
NUM = re.compile(r'\d')
# 6 秒 F 型掃描（career/style/hr-6-second-source.md）
EDGE = 10            # 招募者視線只停在每行左緣幾個字（視覺寬度：中文 1、英數 0.5）
HEADER_CHARS = 24    # 經歷抬頭的可見寬度
DUTY_START = re.compile(r'^(主責|負責|職責|協助|參與|處理|管理|Responsible|Managed|Worked|Assisted|Helped)')
OBJECTIVE = ['希望', '尋求', '期望', '追求', '挑戰性', '發揮所長', '貢獻所學', '學習成長', 'Seeking', 'Objective']
RESULT_VERB = ['主導', '上線', '降到', '提升', '成長', '0 到 1', '→', '縮短', '增加', '減少']
TITLE_WORDS = ['經理', 'Manager', 'PM', 'Owner', '主任', '企劃', '工程師', '專員', '工讀生', 'Intern',
               'Lead', 'Director', '總監', '主管', '顧問', 'Analyst', '分析師', '設計師']
DATE = re.compile(r'\d{4}/\d{1,2}\s*[-–~至]\s*(?:\d{4}/\d{1,2}|迄今|至今|Present)')

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

def hits(text, kws):
    t = text.lower()
    return [k for k in kws if k.lower() in t]

def score_line(text, jd):
    flags = []
    s = 0
    n = len(text)
    # 長度：條列 25–90 字最佳
    if 25 <= n <= 90: s += 10
    elif n <= 120: s += 6
    else: flags.append('過長')
    if NUM.search(text): s += 10
    else: flags.append('無數字')
    edge, head = cut(text, EDGE), text[:20]
    if NUM.search(edge) or hits(edge, jd + RESULT_VERB): s += 8
    elif NUM.search(head) or hits(head, jd): s += 4; flags.append('左緣 10 字無結果')
    else: flags.append('開頭無結果或關鍵詞')
    if DUTY_START.match(text): s -= 8; flags.append('職責式開頭')
    obj = [o for o in OBJECTIVE if o in text]
    if obj: s -= 6; flags.append('求職目標語:' + '/'.join(obj))
    h = hits(text, jd)
    s += min(len(h), 3) * 2 + (0 if len(h) <= 4 else -4)
    if len(h) > 4: flags.append('疑似塞詞')
    bad = [b for b in BANNED if b in text]
    if bad: s -= 10; flags.append('禁用詞:' + '/'.join(bad))
    if '—' in text or '**' in text: s -= 10; flags.append('破折號或粗體')
    return max(s, 0), h, flags

def cmd_variants(path, jd):
    unit = None
    print('| 單位 | 版本 | 機械分/40 | 關鍵詞 | 旗標 |')
    print('| :-- | :-- | :-: | :--- | :--- |')
    for line in open(path, encoding='utf8'):
        m = re.match(r'###\s+(\S+)', line)
        if m: unit = m.group(1); continue
        m = re.match(r'(V\d+)\s*[:：]\s*(.+)', line.strip())
        if m and unit:
            sc, h, fl = score_line(m.group(2), jd)
            print(f'| {unit} | {m.group(1)} | {sc} | {"、".join(h)} | {"；".join(fl)} |')

def cmd_ats(path, jd, pref):
    text = open(path, encoding='utf8').read()
    bullets = [l[2:] for l in text.split('\n') if l.startswith('- ')]
    exp = text.split('專業技能')[0]
    skills = text.split('專業技能')[1].split('求職條件')[0] if '專業技能' in text else ''
    allkw = list(dict.fromkeys(jd + pref))
    cov = len(hits(text, allkw)) / len(allkw) if allkw else 0
    if 0.70 <= cov <= 0.90: b = 25
    elif 0.90 < cov < 0.95: b = 22
    elif cov >= 0.95: b = 18   # 疑似塞詞
    elif cov >= 0.50: b = 15
    else: b = 8
    pref_both = [k for k in pref if k.lower() in exp.lower() and k.lower() in skills.lower()]
    pref_ratio = len(pref_both) / len(pref) if pref else 1
    b = round(b * (0.6 + 0.4 * pref_ratio))
    nb = max(len(bullets), 1)
    hook = sum(1 for x in bullets if NUM.search(x[:20]) or hits(x[:20], allkw)) / nb
    edge = sum(1 for x in bullets if NUM.search(cut(x, EDGE)) or hits(cut(x, EDGE), allkw + RESULT_VERB)) / nb
    lines = [l.strip() for l in exp.split('\n學歷')[0].split('\n')]   # 抬頭只看工作經歷，不含學歷
    heads = [l for l in lines if '｜' in l and DATE.search(l)]
    head_ok = [h for h in heads if any(w in h.split('｜')[0] for w in TITLE_WORDS) and vw(h[:DATE.search(h).start()]) < HEADER_CHARS]
    head_r = len(head_ok) / len(heads) if heads else 0
    first = ' '.join([l for l in lines if l][:3])
    summ = text.split('專業摘要')[1].split('工作經歷')[0] if '專業摘要' in text else ''
    obj = [o for o in OBJECTIVE if o in summ]
    c = round(8 * edge + 4 * hook + 4 * head_r + (2 if not obj else 0) + (2 if any(w in first for w in TITLE_WORDS) else 0))
    numr = sum(1 for x in bullets if NUM.search(x)) / nb
    duty = [x for x in bullets + lines if DUTY_START.match(x)]
    d = max((20 if numr >= 0.6 else round(20 * numr / 0.6)) - 2 * len(duty), 0)
    print(f'B 關鍵字對應 {b}/25（覆蓋 {cov:.0%}；加分詞同時在技能與經歷 {len(pref_both)}/{len(pref)}）')
    print(f'  缺：{"、".join(k for k in allkw if k not in hits(text, allkw)) or "無"}')
    print(f'  加分詞只出現一處：{"、".join(k for k in pref if k not in pref_both) or "無"}')
    print(f'C 6 秒可讀 v2 {c}/20（左緣 {EDGE} 字有訊號 {edge:.0%}；前 20 字 {hook:.0%}；'
          f'抬頭職稱在左且日期在 {HEADER_CHARS} 字內 {len(head_ok)}/{len(heads)}；'
          f'摘要求職目標語 {"、".join(obj) or "無"}）')
    print(f'D 量化影響 {d}/20（含數字條列 {numr:.0%}；職責式開頭 {len(duty)} 處，每處 -2）')
    for x in duty: print(f'  職責式：{x[:24]}')
    print('A 格式請用 career-ops verify-ats；E AI 實證人工給分。')

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('mode', choices=['variants', 'ats'])
    ap.add_argument('path')
    ap.add_argument('--jd', default='')
    ap.add_argument('--preferred', default='')
    a = ap.parse_args()
    if a.mode == 'variants': cmd_variants(a.path, kw_list(a.jd))
    else: cmd_ats(a.path, kw_list(a.jd), kw_list(a.preferred))
