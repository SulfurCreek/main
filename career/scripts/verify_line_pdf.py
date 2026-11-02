#!/usr/bin/env python3
"""驗收 LINE Resume PDF 成品：頁數 ≤2、無自傳區塊、姓名 Nieh、日期起訖有空格、無 Reverse-engineered、第一人稱 I ≤3、列點有圓點。
用法：python3 career/scripts/verify_line_pdf.py <pdf>"""
import re, subprocess, sys

pdf = sys.argv[1]
info = subprocess.run(["pdfinfo", pdf], capture_output=True, text=True).stdout
pages = int(re.search(r"Pages:\s+(\d+)", info).group(1))
text = subprocess.run(["pdftotext", "-layout", pdf, "-"], capture_output=True, text=True).stdout
errs = []
if pages > 2:
    errs.append(f"頁數 {pages}：英文履歷上限 2 頁")
if re.search(r"personal statement|autobiography", text, re.I):
    errs.append("含 PERSONAL STATEMENT／Autobiography")
if not re.search(r"Kun Huai Nieh\b", text) or re.search(r"Kun Huai Nie\b(?!h)", text):
    errs.append("姓名須為 Kun Huai Nieh")
if re.search(r"reverse-engineer", text, re.I):
    errs.append("含 Reverse-engineered")
for m in re.finditer(r"\b\d{4}-\d{2}[-–]\d{4}-\d{2}\b", text):
    errs.append(f"日期缺空格：{m.group(0)}")
if re.search(r"\b(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{4}\b", text):
    errs.append("內文含英文月份全稱日期")
if len(re.findall(r"\bI\b", text)) > 3:
    errs.append("第一人稱 I 超過 3 次")
if text.count("•") < 10:
    errs.append("列點圓點渲染不足（<10）")
if errs:
    print("❌ LINE PDF 驗收失敗")
    for e in errs:
        print(" -", e)
    sys.exit(1)
print(f"✅ LINE PDF 驗收通過（{pages} 頁）")
