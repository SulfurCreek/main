#!/usr/bin/env python3
"""一鍵產出 LINE 英文履歷 PDF：驗收 md → 產 fill.json／resume.json → HTML → PDF（超過 2 頁自動縮字級至 9.0pt）→ verify_line_pdf。
用法：python3 career/scripts/build_line_pdf.py career/drafts/line/line-resume.md <out.pdf>"""
import os, re, subprocess, sys
from pathlib import Path

md, out = Path(sys.argv[1]), Path(sys.argv[2])
run = lambda *a, **k: subprocess.run(a, **k)
if run(sys.executable, "career/scripts/verify_line_profile.py", str(md)).returncode:
    sys.exit("md 驗收未通過，不產出 PDF")
run(sys.executable, "career/scripts/gen_line_pack.py", str(md), check=True)
resume_json = md.with_name(md.stem + ".resume.json")
html = md.with_name(md.stem + ".html")
fs = 9.6
while True:
    run(sys.executable, "career/scripts/gen_line_pdf.py", str(resume_json), str(html), env={**os.environ, "LINE_PDF_FONT": f"{fs:.1f}"}, check=True, stdout=subprocess.DEVNULL)
    run("node", ".claude/skills/resume-craft/scripts/mkpdf.js", str(html.resolve()), str(out.resolve()), check=True)
    pages = int(re.search(r"Pages:\s+(\d+)", subprocess.run(["pdfinfo", str(out)], capture_output=True, text=True).stdout).group(1))
    if pages <= 2 or fs <= 9.0:
        break
    fs = round(fs - 0.2, 1)
print(f"字級 {fs}pt，{pages} 頁")
sys.exit(run(sys.executable, "career/scripts/verify_line_pdf.py", str(out)).returncode)
