#!/usr/bin/env python3
"""含已停用驗證，勿照歷史命令執行；純格式用途請先確認。
104 中英雙語履歷：組裝器（2026-11-03 r2 契約，本人 D1–D4 裁定）。

欄位規格（只有這三類可變，其餘逐位元組與中文基底相同）：
- info.bio：英文 only＝LINE Summary 原文 ＋ 空一行 ＋ 本人核可的 CV 句（CV_SENTENCE，逐字鎖定）。
- skill[0..5] desc：英文（LINE 整句／整行）＋ 空一行 ＋ 原中文。
- project[0..3] 說明：英文（LINE 整個列點，第一則 blockquote、其餘段落）＋ <p><br></p> ＋ 原中文。
- 工作經歷、個人特色、自傳、求職條件、名稱、標籤、圖片、網址、directive、順序：不得變。

英文零改寫：只擷取 LINE 對外正文（line_md.parse 已剔除註解與標記）的完整句／行／列點；不改字、不接合、不翻譯。
來源鎖定：LINE 檔 SHA-256 必須等於 LINE_SHA；每個映射附預期原文雜湊，不符即失敗。
中文基底（D1）：一般版（不公開公司名的版本不用）。
流程：組裝 → verify_104_bilingual.verify()（strict）→ 通過才原子寫入；失敗不留任何成品。

用法：python3 career/scripts/gen_104_bilingual.py --zh <一般版 104 md> --out <輸出 md>
       [--line career/drafts/line/line-resume.md] [--line-sha <sha256>] [--limit bio=N] [--limit skill=N]
"""
import argparse
import hashlib
import html
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import line_md  # noqa: E402
import md104  # noqa: E402

from bilingual_contract import (LINE_MD, LINE_SHA, CV_SENTENCE, SUMMARY_SHA,
                                SKILL_SRC, PROJECT_SRC, LIMITS_KNOWN,
                                sha16, sentences, english_units)
PROJECT_ACCENT = {
    0: {"B": ["Juicy"], "G": ["from about 3,200 to 12,500", "from about 1,500 to 12,000"]},
    1: {"B": ["KOOL"], "G": ["about 16,000 influencer profiles", "over 80,000 campaign applications"]},
    2: {"B": ["employer-side recruitment system overhaul"], "G": ["743 of 840 related client requests (88%)"]},  # 晴藍只標名詞，不標動詞
    3: {"B": ["shared recruitment feature"], "G": ["55 client requests since 2020/12"]},
}
G_STYLE = "background-color: #fbf3db;"
B_STYLE = "background-color: #deebf1;"
def accent_html(text, acc):
    marks = []
    for kind in ("G", "B"):
        for ph in acc.get(kind, []):
            i = text.find(ph)
            if i < 0:
                raise ValueError(f"重音片語不在原文：{ph!r}")
            marks.append((i, i + len(ph), kind))
    marks.sort()
    for (a0, a1, _), (b0, b1, _) in zip(marks, marks[1:]):
        if b0 < a1:
            raise ValueError("重音片語重疊")
    out, pos = [], 0
    for s, e, kind in marks:
        out.append(html.escape(text[pos:s], quote=False))
        inner = html.escape(text[s:e], quote=False)
        out.append(f'<strong><span style="{B_STYLE}">{inner}</span></strong>' if kind == "B"
                   else f'<span style="{G_STYLE}">{inner}</span>')
        pos = e
    out.append(html.escape(text[pos:], quote=False))
    return "".join(out)


def project_html(pi, items):
    parts = []
    for k, text in enumerate(items):
        inner = accent_html(text, PROJECT_ACCENT.get(pi, {}) if k == 0 else {})
        parts.append(f"<blockquote>{inner}</blockquote>" if k == 0 else f"<p>{inner}</p>")
    return "\n".join(parts) + "\n"


def build(zh_text, line_text, line_sha=None):
    summ, skills, projects = english_units(line_text, line_sha)
    doc = md104.parse(zh_text)
    bodies, seen = {}, set()
    for i, s in enumerate(doc["sections"]):
        k = s["key"]
        if k == ("info", "bio"):
            bodies[i] = summ + "\n\n" + CV_SENTENCE + "\n"
        elif k[0] == "skill":
            bodies[i] = skills[k[1]] + "\n\n" + s["body"]
        elif k[0] == "project":
            bodies[i] = project_html(k[1], projects[k[1]]) + "<p><br></p>\n" + s["body"]
        else:
            continue
        seen.add(k)
    want = {("info", "bio")} | {("skill", i) for i in range(6)} | {("project", i) for i in range(4)}
    if seen != want:
        raise ValueError(f"中文基底欄位不符：缺 {sorted(want - seen)}")
    return md104.assemble(doc, bodies)


def atomic_write(path, text):
    path = Path(path)
    tmp = path.with_name(path.name + ".tmp")
    tmp.write_text(text, encoding="utf-8")
    os.replace(tmp, path)


def main(argv=None):
    import verify_104_bilingual as vb
    ap = argparse.ArgumentParser()
    ap.add_argument("--zh", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--line", default=str(LINE_MD))
    ap.add_argument("--line-sha", default=None)
    ap.add_argument("--limit", action="append", default=[], help="欄位上限，例如 bio=2000、skill=500")
    try:
        a = ap.parse_args(argv)
    except SystemExit:
        return 2
    try:
        zh, line = Path(a.zh).read_text(encoding="utf-8"), Path(a.line).read_text(encoding="utf-8")
        out = build(zh, line, a.line_sha)
    except (OSError, ValueError, KeyError, IndexError) as e:
        print(f"❌ 無法組裝（未寫出任何檔案）：{e}")
        return 1
    limits = vb.parse_limits(a.limit)
    errs, pending = vb.verify(out, zh, line, a.line_sha, limits)
    if errs:
        print("❌ 驗收失敗（未寫出任何檔案）")
        for e in errs:
            print(" -", e)
        return 1
    if pending:
        print("⚠️ 未可填表，未寫入正式輸出（上限未量測）：" + "、".join(pending))
        return 3
    atomic_write(a.out, out)
    print(f"✅ 已寫出 {a.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
