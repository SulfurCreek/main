#!/usr/bin/env python3
"""履歷機械評分（resume-craft 工作流程步驟 4 與 7 用）。

只算得出來的部分；事實一致、語氣、HR／主管判斷由模型在報告裡人工給分。

用法：
  python3 resume_score.py variants <variants.md> --jd "PRD,UAT,跨部門,..."
      variants.md 格式：每個單位一段「### U01 標題」，下面每行「V01: 文字」…「V20: 文字」。
      輸出每個版本的機械分（0–40）與旗標，供人工再加 0–60 分。
  python3 resume_score.py ats <resume.txt> --jd "必備詞,..." --preferred "加分詞,..."
      依 career/style/ats-2026-source.md 算分表算 B（關鍵字對應）、C（7 秒可讀）、D（量化），
      A（格式）請用 career-ops verify-ats，E（AI 實證）人工。
"""
import argparse, re, sys

BANNED = ['致力於', '深入探討', '扮演關鍵角色', '成功實現', '無縫', '編織', 'Spearheaded', 'Architected',
          '協助', '參與', '負責', '具備良好', '熱情洋溢', '賦能']
NUM = re.compile(r'\d')

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
    head = text[:20]
    if NUM.search(head) or hits(head, jd): s += 8
    else: flags.append('開頭無結果或關鍵詞')
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
    hook = sum(1 for x in bullets if NUM.search(x[:20]) or hits(x[:20], allkw)) / max(len(bullets), 1)
    c = round(20 * hook)
    numr = sum(1 for x in bullets if NUM.search(x)) / max(len(bullets), 1)
    d = 20 if numr >= 0.6 else round(20 * numr / 0.6)
    print(f'B 關鍵字對應 {b}/25（覆蓋 {cov:.0%}；加分詞同時在技能與經歷 {len(pref_both)}/{len(pref)}）')
    print(f'  缺：{"、".join(k for k in allkw if k not in hits(text, allkw)) or "無"}')
    print(f'  加分詞只出現一處：{"、".join(k for k in pref if k not in pref_both) or "無"}')
    print(f'C 7 秒可讀 {c}/20（前 20 字有結果或關鍵詞的條列 {hook:.0%}）')
    print(f'D 量化影響 {d}/20（含數字條列 {numr:.0%}）')
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
