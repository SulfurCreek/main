#!/usr/bin/env python3
"""PDF 文字還原檢查（規準 v4）：PDF 轉回文字後與原稿比對。

- 去空白相似度 95% 是**本 repo 的內部回歸門檻，不是業界標準**；高相似度仍可能漏掉關鍵數字。
- v4 另查：職稱、Email、每段經歷日期是否還原且落在該段職稱之後（讀序）、章節讀序、重要數字遺漏
  （區分實質遺漏與換行／標點差異）、日期重複次數。
- 只驗 PDF 文字層；**ATS import: not tested**。雙欄是否適用以本檢查結果判定，不由欄數推論。
用法：python3 parse_check.py <resume.pdf> <source.txt> [--layout raw|layout]
"""
import subprocess, sys, re, difflib

pdf, src = sys.argv[1], sys.argv[2]
mode = '-layout' if '--layout' in sys.argv and sys.argv[sys.argv.index('--layout') + 1] == 'layout' else '-raw'
out = subprocess.run(['pdftotext', mode, pdf, '-'], capture_output=True, text=True).stdout
s = open(src, encoding='utf8').read()
norm = lambda t: re.sub(r'\s+', '', t)
N, O = norm(s), norm(out)
ratio = difflib.SequenceMatcher(None, N, O, autojunk=False).ratio()
print(f'文字還原相似度 {ratio:.1%}（{"≥" if ratio >= .95 else "<"} 95% 內部回歸門檻；抽字模式 {mode}）')

heads = ['專業摘要', '工作經歷', '學歷', '專業技能', '求職條件', '自傳']
present = [h for h in heads if h in s]
pos = [O.find(h) for h in present]
print('章節可讀：', '、'.join(h + ('✅' if p >= 0 else '❌') for h, p in zip(present, pos)))
print('章節讀序：', '✅ 與原稿一致' if all(p >= 0 for p in pos) and pos == sorted(pos) else '⚠️ 與原稿不同（可能左右欄交錯）')

DATE = re.compile(r'\d{4}/\d{1,2}\s*[-–~至]\s*(?:\d{4}/\d{1,2}|迄今|至今|Present)')
jobs = [l.strip() for l in s.split('\n') if '｜' in l and DATE.search(l)]
bad = []
for j in jobs:
    title = j.split('｜')[0]
    d = norm(DATE.search(j).group(0))
    ti, di = O.find(norm(title)), O.find(d)
    if ti < 0 or di < 0 or di < ti: bad.append(f'{title[:14]}（職稱{"✅" if ti >= 0 else "❌"} 日期{"✅" if di >= 0 else "❌"}{" 讀序反" if 0 <= di < ti else ""}）')
print(f'經歷抬頭（職稱→日期）{len(jobs) - len(bad)}/{len(jobs)}', ('；問題：' + '；'.join(bad)) if bad else '')

dates = re.findall(r'\d{4}/\d{1,2}', s)
lost_d = [d for d in set(dates) if s.count(d) > out.count(d)]
print(f'日期 YYYY/MM：原稿 {len(dates)} 次，次數短少 {"、".join(sorted(lost_d)) or "無"}')

nums = set(re.findall(r'\d[\d,.]*\d%?|\d+%', s))
lost = sorted(n for n in nums if norm(n) not in O)
print(f'重要數字遺漏（{len(nums)} 個不同數字）：{"、".join(lost) or "無"}')
print('亂碼字元（U+FFFD）：', out.count('�'))
em = re.search(r'[\w.+-]+@[\w-]+\.[\w.]+', s)
print('Email：', ('✅' if em and em.group(0) in out else '❌') if em else '原稿無 Email')
print('ATS import: not tested')
