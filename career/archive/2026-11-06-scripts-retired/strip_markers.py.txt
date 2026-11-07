#!/usr/bin/env python3
"""T1 契約：帶標記的編輯來源 ↔ 去標記成品（2026-11-03）。

- 編輯來源：02_codex_stage/final_resume.md（保留 <!-- [STATUS: …] … --> 標記；verify_polish.py 驗）。
- 成品：final_resume.clean.md（去掉所有控制標記註解；Codex check_polish_structure.py 驗）。
- 對帳：clean 必須等於 strip(來源)，且不得殘留任何控制標記；不允許手動刪標記湊通過。

用法：python3 career/scripts/strip_markers.py <來源> <輸出 clean>      # 產生
      python3 career/scripts/strip_markers.py --check <來源> <clean>    # 只對帳
"""
import re
import sys
from pathlib import Path

MARKER = re.compile(r"^[ \t]*<!--\s*\[(?:STATUS|LEAD|LOCK_ENTITIES|LOCK_FACTS|AMPLIFY|KEEP|G|B|BT):[^\n]*?-->[ \t]*\n", re.M)
RESIDUE = re.compile(r"\[(?:STATUS|LOCK_ENTITIES|LOCK_FACTS|LEAD|AMPLIFY):|NEEDS_POLISH")


def strip(text):
    return MARKER.sub("", text)


def check(src, clean):
    errs = []
    if RESIDUE.search(clean):
        errs.append("clean 檔仍有控制標記")
    if strip(src) != clean:
        errs.append("clean 檔與來源去標記後不一致（不得在 clean 檔另行改字）")
    if not MARKER.search(src):
        errs.append("來源沒有任何控制標記（來源應為帶標記版）")
    return errs


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    if len(argv) == 3 and argv[0] == "--check":
        errs = check(Path(argv[1]).read_text(encoding="utf-8"), Path(argv[2]).read_text(encoding="utf-8"))
        print("\n".join("❌ " + e for e in errs) or "✅ 來源與 clean 對帳一致")
        return 1 if errs else 0
    if len(argv) == 2:
        src = Path(argv[0]).read_text(encoding="utf-8")
        Path(argv[1]).write_text(strip(src), encoding="utf-8")
        print(f"✅ 已寫出 {argv[1]}")
        return 0
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main())
