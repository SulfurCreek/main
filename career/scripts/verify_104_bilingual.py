#!/usr/bin/env python3
"""104 中英並列履歷驗收（2026-11-03）。

用法：python3 career/scripts/verify_104_bilingual.py <並列 md> [--zh <中文公開版 md>] [--line <英文履歷 md>] [--strict]

檢查（程式可確定者）：
1. 中文零加工：中文公開版的簡介、4 筆經歷、6 張專長、自傳、4 筆專案說明，原文逐字出現在並列檔。
2. 英文先行：簡介、4 筆經歷、6 張專長、4 筆專案說明，英文都在中文之前；自傳區塊沒有英文。
3. 來源：每個英文句子都必須是 LINE 英文履歷中現有的句子（規範化空白後為子字串）。
   --strict：任何不在來源的句子即失敗（上游產生器輸出用）。
   預設：不在來源的句子列為「已修改，需主代理人工查核」，不判失敗（Codex 潤飾後用）。
4. 英文語氣硬規則：沿用 verify_line_profile 的禁用詞、中文字夾雜、第一人稱上限。
不能機械判定：改寫後的語意是否仍等同原句、母語語感；由主代理與盲審處理。
"""
import argparse
import html
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import gen_104_bilingual as gb  # noqa: E402
import verify_line_profile as vlp  # noqa: E402

CJK = re.compile(r"[一-鿿]")


def norm(s):
    s = re.sub(r"</?(?:span|strong|b|em|i|u)\b[^>]*>", "", s)
    s = html.unescape(re.sub(r"<[^>]*>", " ", s))
    return re.sub(r"\s+", " ", re.sub(r"\s+([,.;:)])", r"\1", s)).strip()


def fields(text):
    """依序取出並列檔欄位：[(key, 區塊文字)]。"""
    out = []
    m = re.search(r'"field": "bio", "mode": "plain_text"\}\n-->\n\n```text\n(.*?)```', text, re.S)
    out.append(("summary", m.group(1)))
    for pat, key, fence in ((r"### 2\.(\d) [^\n]*\n.*?```html\n(.*?)```", "exp", "html"),
                            (r"### 3\.(\d) [^\n]*\n.*?```text\n(.*?)```", "skill", "text"),
                            (r"### 5\.(\d) [^\n]*\n.*?```html\n(.*?)```", "project", "html")):
        for mm in re.finditer(pat, text, re.S):
            out.append((f"{key}{mm.group(1)}", mm.group(2)))
    return out


def split_lang(block):
    """英文在前、中文在後：回傳 (英文部分, 中文部分)；中文由第一個含中文字的段落起算。"""
    paras = re.split(r"\n\s*\n|(?<=</p>)\n|(?<=</blockquote>)\n|(?<=</ul>)\n", block)
    en, zh, seen_zh = [], [], False
    for p in paras:
        if not seen_zh and not CJK.search(p):
            en.append(p)
        else:
            seen_zh = True
            zh.append(p)
    return "\n".join(en), "\n".join(zh)


def verify(bi_text, zh_text, line_text, strict=False):
    errs, manual = [], []
    src = norm(line_text)
    bf, zf = dict(fields(bi_text)), dict(fields(zh_text))
    for key, block in bf.items():
        en, zh = split_lang(block)
        if not en.strip() or CJK.search(en):
            errs.append(f"[英文先行] {key} 欄位沒有在中文之前的英文段")
            continue
        # 中文零加工
        zh_orig = zf[key].strip()
        if zh_orig not in block:
            errs.append(f"[中文被改動] {key} 的中文原文沒有逐字保留")
        # 英文來源與語氣
        text = norm(en)
        for s in gb.sentences(text):
            if norm(s) not in src:
                (errs if strict else manual).append(f"[英文不在來源] {key}：{s[:80]}…" if strict else f"{key}：{s[:80]}…（已修改或新增，需人工查核）")
        for w in vlp.BANNED_BULLET_ONLY:
            if w.lower() in text.lower():
                errs.append(f"[禁用詞] {key}：{w}")
        if len(re.findall(r"\bI\b", text)) > 3:
            errs.append(f"[第一人稱] {key}：I 超過 3 次")
    # 自傳只有中文
    m = re.search(r'"field": "chi", "mode": "quill_html"\}\n-->\n\n```html\n(.*?)```', bi_text, re.S)
    z = re.search(r'"field": "chi", "mode": "quill_html"\}\n-->\n\n```html\n(.*?)```', zh_text, re.S)
    if not m or not z or m.group(1) != z.group(1):
        errs.append("[自傳] 自傳必須與中文公開版逐字相同（只有中文）")
    elif re.search(r"[A-Za-z]{6,} [A-Za-z]{3,} [A-Za-z]{3,}", re.sub(r"<[^>]*>", "", m.group(1))) and not CJK.search(m.group(1)):
        errs.append("[自傳] 自傳出現整段英文")
    keys = set(bf)
    if len(keys) != 15:
        errs.append(f"[欄位數] 並列欄位應為 15 個（簡介 1＋經歷 4＋專長 6＋專案 4），實際 {len(keys)}")
    return errs, manual


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("file")
    ap.add_argument("--zh", default=str(gb.ZH_MD))
    ap.add_argument("--line", default=str(gb.LINE_MD))
    ap.add_argument("--strict", action="store_true")
    try:
        a = ap.parse_args(argv)
    except SystemExit:
        return 2
    try:
        errs, manual = verify(Path(a.file).read_text(encoding="utf-8"), Path(a.zh).read_text(encoding="utf-8"),
                              Path(a.line).read_text(encoding="utf-8"), a.strict)
    except (OSError, AttributeError) as e:
        print(f"❌ 無法讀取或解析：{e}")
        return 2
    if errs:
        print("❌ 中英並列驗收失敗")
        for e in errs:
            print(" -", e)
        return 1
    print("✅ 中文零加工、英文先行、欄位數、禁用詞通過" + ("；英文句子全部取自現有英文履歷（strict）" if a.strict else ""))
    if manual:
        print(f"⚠️ 英文句子與來源不同 {len(manual)} 處（Codex 潤飾後的差異，需主代理人工查核，不判失敗）：")
        for m in manual:
            print("  -", m)
    return 0


if __name__ == "__main__":
    sys.exit(main())
