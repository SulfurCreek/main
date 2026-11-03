#!/usr/bin/env python3
"""104 中英雙語履歷驗收（2026-11-03 r2 契約，全程 strict，無人工放行模式）。

用法：python3 career/scripts/verify_104_bilingual.py <雙語 md> --zh <一般版 104 md>
       [--line career/drafts/line/line-resume.md] [--line-sha <sha>] [--limit bio=N] [--limit skill=N]
Exit：0 通過且可填表；3 通過但有欄位上限未量測（不可填表）；1 失敗；2 參數或讀檔錯誤。

檢查：
1. 欄位白名單：把 bio／6 專長／4 專案的 body 換回中文基底後，整份必須與基底逐位元組相同
   （只容許第一個 H1 標題行不同）→ 涵蓋工作經歷、名稱、標籤、圖片、網址、directive、順序、缺欄、重複欄。
2. bio：等於 LINE Summary 原文＋空一行＋CV_SENTENCE，不含中文。
3. 專長：英文＝鎖定映射原文（整句／整行）＋空一行＋中文原文。
4. 專案：英文段落去重音後＝鎖定映射的 LINE 列點原文（逐則、同順序）；只允許兩種重音 span；接 <p><br></p>＋中文原文。
5. 字數：可見字元（md104.visible_len）≤ 上限；上限未知者列為「未可填表」。
"""
import argparse
import html
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import gen_104_bilingual as gb  # noqa: E402
import md104  # noqa: E402

ALLOWED_TAG = re.compile(r'</?blockquote>|</?p>|</?strong>|<span style="background-color: #(?:fbf3db|deebf1);">|</span>')


def parse_limits(items):
    lim = dict(gb.LIMITS_KNOWN)
    for it in items:
        k, v = it.split("=", 1)
        lim[k.strip()] = int(v)
    return lim


def plain(h):
    return html.unescape(re.sub(r"<[^>]*>", "", h))


def _h1(text):
    return re.sub(r"^# .*$", "# H1", text, count=1, flags=re.M)


def verify(out_text, zh_text, line_text, line_sha=None, limits=None):
    limits = dict(gb.LIMITS_KNOWN) if limits is None else limits
    errs, pending = [], set()
    try:
        summ, skills, projects = gb.english_units(line_text, line_sha)
    except ValueError as e:
        return [f"[來源] {e}"], []
    try:
        od, zd = md104.parse(out_text), md104.parse(zh_text)
    except ValueError as e:
        return [f"[解析] {e}"], []
    okeys = [s["key"] for s in od["sections"]]
    if len(okeys) != len(set(okeys)):
        errs.append("[欄位] 有重複欄位")
    if okeys != [s["key"] for s in zd["sections"]]:
        return errs + ["[欄位] 欄位清單或順序與中文基底不同"], []
    restore = {}
    for i, (o, z) in enumerate(zip(od["sections"], zd["sections"])):
        k, body = o["key"], o["body"] or ""
        if k == ("info", "bio"):
            if body != summ + "\n\n" + gb.CV_SENTENCE + "\n":
                errs.append("[簡介] 必須是 LINE Summary 原文＋空一行＋核可的 CV 句，不得改字或加中文")
            if md104.CJK.search(body):
                errs.append("[簡介] 不得含中文")
            field = "bio"
        elif k[0] == "skill":
            want = skills[k[1]] + "\n\n"
            if not body.startswith(want):
                errs.append(f"[專長 {k[1]+1}] 英文不是鎖定映射原文（或缺空行）")
            elif body[len(want):] != z["body"]:
                errs.append(f"[專長 {k[1]+1}] 中文與基底不同")
            field = "skill"
        elif k[0] == "project":
            sep = "<p><br></p>\n"
            if sep + z["body"] not in body or not body.endswith(z["body"]):
                errs.append(f"[專案 {k[1]+1}] 中文與基底不同或缺分隔空段落")
            else:
                en = body[: len(body) - len(z["body"]) - len(sep)]
                bad = [t for t in re.findall(r"<[^>]*>", en) if not ALLOWED_TAG.fullmatch(t)]
                if bad:
                    errs.append(f"[專案 {k[1]+1}] 英文含未允許的標籤：{bad[:3]}")
                paras = [plain(p) for p in re.findall(r"<(?:blockquote|p)>(.*?)</(?:blockquote|p)>", en, re.S)]
                if paras != projects[k[1]]:
                    errs.append(f"[專案 {k[1]+1}] 英文不是鎖定映射的 LINE 列點原文（逐則、同順序）")
            field = "project"
        else:
            continue
        restore[i] = z["body"]
        n = md104.visible_len(body)
        if field in limits:
            if n > limits[field]:
                errs.append(f"[字數超標] {k} 共 {n} 字，上限 {limits[field]}（不得截短，請回報本人）")
        else:
            pending.add(field)
    if _h1(md104.assemble(od, restore)) != _h1(zh_text):
        errs.append("[白名單外異動] 工作經歷、名稱、標籤、圖片、網址、directive 或其他內容與中文基底不同")
    return errs, sorted(pending)


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("file")
    ap.add_argument("--zh", required=True)
    ap.add_argument("--line", default=str(gb.LINE_MD))
    ap.add_argument("--line-sha", default=None)
    ap.add_argument("--limit", action="append", default=[])
    try:
        a = ap.parse_args(argv)
        texts = [Path(p).read_text(encoding="utf-8") for p in (a.file, a.zh, a.line)]
        limits = parse_limits(a.limit)
    except (SystemExit, OSError, ValueError) as e:
        print(f"❌ 參數或讀檔錯誤：{e}")
        return 2
    errs, pending = verify(*texts, a.line_sha, limits)
    if errs:
        print("❌ 雙語驗收失敗")
        for e in errs:
            print(" -", e)
        return 1
    if pending:
        print("⚠️ 內容驗收通過，但下列欄位上限未量測，未可填表：" + "、".join(pending))
        return 3
    print("✅ 雙語驗收通過，可填表")
    return 0


if __name__ == "__main__":
    sys.exit(main())
