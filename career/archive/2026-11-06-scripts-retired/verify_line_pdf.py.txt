#!/usr/bin/env python3
"""驗收 LINE Resume PDF 成品。

用法：python3 career/scripts/verify_line_pdf.py <pdf> --json <resume.json> [--html <html>]
      python3 career/scripts/verify_line_pdf.py <pdf> --format-only   # 只做格式檢查，明確標示「內容完整性未驗收」並 Exit 1

格式檢查：頁數 ≤2、無自傳區塊、姓名 Nieh、日期起訖有空格、無 Reverse-engineered、第一人稱 I ≤3。
內容對帳（2026-11-02）：以 resume.json 為唯一來源，逐項核對 Summary、Skills、每段職稱／公司／列點、學歷，
須全部出現、順序一致、次數相同，圓點數＝Skills＋列點數；--html 時再核對 HTML <meta> 的雜湊與 JSON 一致。
頁數、姓名、圓點數本身不足以證明內容完整；版面閱讀品質仍需人工視覺驗收（本工具不代替）。
"""
import argparse
import json
import re
import subprocess
import sys


def pdf_text(pdf):
    info = subprocess.run(["pdfinfo", pdf], capture_output=True, text=True)
    if info.returncode:
        raise ValueError(f"pdfinfo 失敗：{info.stderr.strip()}")
    pages = int(re.search(r"Pages:\s+(\d+)", info.stdout).group(1))
    text = subprocess.run(["pdftotext", "-layout", pdf, "-"], capture_output=True, text=True).stdout
    return pages, text


def squash(s):
    return re.sub(r"\s+", "", s).replace("‐", "-")


def format_errors(pages, text):
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
    return errs


def expected_items(d):
    """依渲染順序列出必須出現的內容。"""
    items = [("Summary", d["summary"])] + [("Skill", x) for x in d["skills"]]
    for s in d["steps"]:
        f = s["fields"]
        if s["target_block"] == "work_experience":
            items += [("Title", f["position_title"]), ("Company", f["company"])]
            items += [("Bullet", b) for b in s.get("description_bullets", [])]
    for s in d["steps"]:
        if s["target_block"] == "education":
            items += [("University", s["fields"]["university"]), ("Degree", s["fields"]["degree_name"])]
    return items


def content_errors(text, d):
    errs = []
    flat = squash(text)
    pos = 0
    for kind, val in expected_items(d):
        v = squash(val)
        if not v:
            continue
        i = flat.find(v, pos)
        if i < 0:
            errs.append(f"[內容遺失或換序] {kind}：{val[:60]}" + ("（存在但順序不對）" if v in flat else ""))
            continue
        pos = i + len(v)
    for kind in ("Bullet", "Skill"):
        for val in {v for k, v in expected_items(d) if k == kind}:
            want = sum(1 for k, v in expected_items(d) if k == kind and v == val)
            got = flat.count(squash(val))
            if got != want:
                errs.append(f"[重複次數] {kind} 出現 {got} 次，來源 {want} 次：{val[:50]}")
    bullets = len(d["skills"]) + sum(len(s.get("description_bullets", [])) for s in d["steps"])
    if text.count("•") != bullets:
        errs.append(f"[圓點數] PDF 有 {text.count('•')} 個圓點，來源應為 {bullets} 個（Skills＋列點）")
    return errs


def html_errors(html_path, d):
    h = open(html_path, encoding="utf-8").read()
    errs = []
    for key in ("source-sha256", "payload-sha256"):
        m = re.search(r'<meta name="%s" content="([0-9a-f]+)">' % key, h)
        want = d.get(key.replace("-", "_"))
        if not m or m.group(1) != want:
            errs.append(f"[來源串接] HTML 的 {key} 與 resume.json 不符")
    return errs


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("pdf")
    ap.add_argument("--json")
    ap.add_argument("--html")
    ap.add_argument("--format-only", action="store_true")
    try:
        a = ap.parse_args(argv)
    except SystemExit:
        return 2
    try:
        pages, text = pdf_text(a.pdf)
    except (OSError, ValueError) as e:
        print(f"❌ 無法讀取 PDF：{e}")
        return 2
    errs = format_errors(pages, text)
    if a.json:
        d = json.loads(open(a.json, encoding="utf-8").read())
        errs += content_errors(text, d)
        if a.html:
            errs += html_errors(a.html, d)
    if errs:
        print("❌ LINE PDF 驗收失敗")
        for e in errs:
            print(" -", e)
        return 1
    if not a.json:
        print(f"⚠️ 格式檢查通過（{pages} 頁），但未提供 --json：內容完整性未驗收，不得視為完整履歷")
        return 1
    print(f"✅ LINE PDF 格式與內容對帳通過（{pages} 頁）；版面閱讀品質仍需人工視覺驗收")
    return 0


if __name__ == "__main__":
    sys.exit(main())
