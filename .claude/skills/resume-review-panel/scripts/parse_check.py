#!/usr/bin/env python3
"""ATS 解析測試：PDF 轉回文字後與原稿比對（中文是否亂碼、順序、標題、日期、Email）。
用法：python3 parse_check.py <resume.pdf> <source.txt>
"""
import subprocess, sys, re, difflib
pdf, src = sys.argv[1], sys.argv[2]
out = subprocess.run(['pdftotext', '-layout', pdf, '-'], capture_output=True, text=True).stdout
s = open(src, encoding='utf8').read()
norm = lambda t: re.sub(r'\s+', '', t)
ratio = difflib.SequenceMatcher(None, norm(s), norm(out)).ratio()
heads = ['專業摘要', '工作經歷', '學歷', '專業技能', '自傳']
dates = re.findall(r'\d{4}/\d{2}', s)
print(f'文字還原相似度 {ratio:.1%}（≥ 95% 視為可解析）')
print('標題可讀：', '、'.join(h + ('✅' if h in out else '❌') for h in heads))
print(f'日期 YYYY/MM 還原 {sum(d in out for d in dates)}/{len(dates)}')
print('亂碼字元（U+FFFD）：', out.count('�'))
print('Email：', '✅' if re.search(r'[\w.+-]+@[\w-]+\.[\w.]+', out) else '❌ 本文無 Email')
