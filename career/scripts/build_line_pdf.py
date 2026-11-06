#!/usr/bin/env python3
"""含已停用驗證，勿照歷史命令執行；純格式用途請先確認。
一鍵產出 LINE 英文履歷 PDF：驗收 md（--for pdf）→ fill.json／resume.json → HTML → PDF → verify_line_pdf（內容對帳）。

用法：python3 career/scripts/build_line_pdf.py <line-resume.md> <out.pdf> [--upstream <上游 md>]

2026-11-02 契約：
- HTML 與 PDF 先輸出到暫存檔；verify_line_pdf（--json＋--html）通過後才原子替換正式檔。失敗時刪暫存檔、既有成品不動。
- 超過 2 頁時自動縮字級（最低 9.0pt）只為控制頁數；縮字後的閱讀品質與版面仍需人工視覺驗收，本工具不代替。
"""
import os
import re
import subprocess
import sys
from pathlib import Path
import gen_line_pack as pack


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    if len(argv) < 2:
        print(__doc__)
        return 2
    md, out = Path(argv[0]), Path(argv[1])
    up = argv[argv.index("--upstream") + 1] if "--upstream" in argv else None
    py = sys.executable
    here = Path(__file__).resolve().parent
    if up:
        print("⚠️ --upstream 已停用事實比對，僅保留CLI相容性。")
    try:
        form, resume = pack.prepare(md, purpose="pdf")
        pack.atomic_write([(md.with_name(md.stem + ".fill.json"), form),
                           (md.with_name(md.stem + ".resume.json"), resume)])
    except (OSError, ValueError) as exc:
        print(f"❌ 格式驗收或JSON產生失敗：{exc}（既有PDF不動）")
        return 1
    rj = md.with_name(md.stem + ".resume.json")
    html, final_html = md.with_name(md.stem + ".html.tmp.html"), md.with_name(md.stem + ".html")
    tmp_pdf = out.with_name(out.stem + ".tmp.pdf")
    mkpdf = here.parents[1] / ".claude/skills/resume-craft/scripts/mkpdf.js"
    fs, pages = 9.6, None
    try:
        while True:
            r = subprocess.run([py, str(here / "gen_line_pdf.py"), str(rj), str(html)],
                               env={**os.environ, "LINE_PDF_FONT": f"{fs:.1f}"}, stdout=subprocess.DEVNULL)
            if r.returncode:
                print("❌ HTML 渲染失敗（既有成品不動）")
                return 1
            subprocess.run(["node", str(mkpdf), str(html.resolve()), str(tmp_pdf.resolve())], check=True)
            info = subprocess.run(["pdfinfo", str(tmp_pdf)], capture_output=True, text=True).stdout
            pages = int(re.search(r"Pages:\s+(\d+)", info).group(1))
            if pages <= 2 or fs <= 9.0:
                break
            fs = round(fs - 0.2, 1)
        v = subprocess.run([py, str(here / "verify_line_pdf.py"), str(tmp_pdf), "--json", str(rj), "--html", str(html)])
        if v.returncode:
            print("❌ PDF 驗收失敗：未替換正式成品")
            return 1
        os.replace(html, final_html)
        os.replace(tmp_pdf, out)
        print(f"✅ 已發布 {out}（字級 {fs}pt，{pages} 頁）；" + ("已縮字，" if fs < 9.6 else "") + "請人工視覺驗收版面")
        return 0
    finally:
        for p in (html, tmp_pdf):
            if p.exists():
                p.unlink()


if __name__ == "__main__":
    sys.exit(main())
