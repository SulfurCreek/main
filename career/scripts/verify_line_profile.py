#!/usr/bin/env python3
"""驗收 LINE Career Profile（line-profile.md）：directive JSON、Enum 白名單、日期、英文、Bullet 禁用詞。
用法：python3 career/scripts/verify_line_profile.py <檔>"""
import json, re, sys

ENUM = {
    "employment_type": {"1194", "1195"},
    "type_of_degree": {"20", "21", "22", "23"},
    "degree_status": {"1172", "1173", "2559"},
    "language": {"10", "14", "273", "18", "272", "15", "16"},
    "country": {"215", "110", "117", "233"},
    **{k: {"33", "1174", "34", "35", "36"} for k in ("written", "spoken", "reading", "listening")},
}
FIELDS = {
    "basic": ["email", "mobile_phone", "current_position_title", "current_employer", "country", "address", "city"],
    "work_experience": ["company", "position_title", "employment_type", "location", "start_date", "end_date"],
    "education": ["degree_name", "type_of_degree", "degree_status", "university", "start_date", "end_date"],
    "languages": ["language", "written", "spoken", "reading", "listening"],
}
BANNED = ["strategic", "passionate", "detail-oriented", "leverage", "robust", "seamlessly", "delve", "Spearheaded",
          "Backed by", ", which leave", "merge request", "my planners", "guided my planners", "guided direct-report planners through",
          "launched in 2018/05", "launched in 2018-05", "planned a group function for large employers", "proven track record", "cutting-edge", "(to consolidate", "Present", "Singapore", "Russia", "1111 Job Bank"]
BANNED_BULLET_ONLY = BANNED[:-1]

ANCHORS = {
    "2.1": ["sales buy-in", "department or branch", "lower the barrier", "candidate matching", "compliance",
            "actual selections", "shared foundation", "renewal", "credibility", "at least 30 days"],
    "2.2": ["Airbnb", "Miro", "kicked off in 2018", "Led the design"],
}
DATE = re.compile(r"^\d{4}-(0[1-9]|1[0-2])$")
D = re.compile(r"<!-- @line-directive\s*(\{.*?\})\s*-->", re.S)


def main(path):
    t = open(path, encoding="utf-8").read()
    errs = []
    seen = {}
    for m in D.finditer(t):
        try:
            d = json.loads(m.group(1))
        except Exception as e:
            errs.append(f"JSON 解析失敗：{e}")
            continue
        b, f = d.get("target_block"), d.get("fields", {})
        if b not in FIELDS:
            errs.append(f"未知 target_block：{b}")
            continue
        if set(f) != set(FIELDS[b]):
            errs.append(f"{b} 欄位不符：多 {sorted(set(f)-set(FIELDS[b]))} 缺 {sorted(set(FIELDS[b])-set(f))}")
        if b != "basic":
            seen.setdefault(b, []).append(d.get("index"))
        for k, v in f.items():
            if not isinstance(v, str):
                errs.append(f"{b}.{k} 必須為字串")
                continue
            if k in ENUM and v not in ENUM[k]:
                errs.append(f"{b}.{k}={v!r} 不在 Enum 白名單")
            if k.endswith("date"):
                if k == "end_date" and v == "":
                    pass
                elif not DATE.match(v):
                    errs.append(f"{b}.{k}={v!r} 非 YYYY-MM")
            if re.search(r"[^\x00-\x7f]", v):
                errs.append(f"{b}.{k} 含非英文字元：{v!r}")
        if b == "work_experience" and f.get("end_date") not in ("",) and f.get("end_date", "") < f.get("start_date", ""):
            errs.append(f"work_experience index {d.get('index')} 結束早於開始")
    for b, idx in seen.items():
        if idx != list(range(len(idx))):
            errs.append(f"{b} index 非 0..N 連號：{idx}")
    # 在職者 end_date 必為空：標題含 Present 的區塊
    for h in re.finditer(r"^### [^\n]*Present[^\n]*\n+<!-- @line-directive\s*(\{.*?\})\s*-->", t, re.M | re.S):
        if json.loads(h.group(1))["fields"].get("end_date") != "":
            errs.append("在職（Present）區塊 end_date 必須為空字串")
    # Bullet 禁用詞（只查 - 開頭行）
    for i, line in enumerate(t.splitlines(), 1):
        if line.startswith("- "):
            for w in BANNED_BULLET_ONLY:
                if w.lower() in line.lower():
                    errs.append(f"第 {i} 行含禁用詞「{w}」")
            if re.search(r"[一-鿿]", line):
                errs.append(f"第 {i} 行 Bullet 含中文")
    # 體裁與句型（voice-en §8）
    heads = [l for l in t.splitlines() if re.match(r"^## (Editing Notes|English Self-Review)", l)]
    if heads:
        errs.append("[成品污染] 不得含 " + "、".join(h[3:] for h in heads) + "：修改紀錄寫於對話回覆，勿寫入本檔")
    bullets = [l for l in t.splitlines() if l.startswith("- ")]
    i_cnt = sum(len(re.findall(r"\bI\b", l)) for l in bullets)
    if i_cnt > 3:
        errs.append(f'[英文履歷體裁違規] 全篇 Bullet 出現高達 {i_cnt} 次第一人稱 "I"（上限 3 次）！英文履歷列點請採用外商標準 Implied First-Person（省略主詞 I，直接以動詞或場景子句接過去式動詞）！')
    for_cnt = sum(1 for l in bullets if l.startswith("- For "))
    prev_blk, prev_w = None, None
    repeat = False
    blk = None
    for l in t.splitlines():
        if l.startswith("### "):
            blk, prev_w = l, None
        elif l.startswith("- "):
            w = l[2:].split(" ", 1)[0].strip(",:").lower()
            if prev_w is not None and w == prev_w:
                repeat = True
            prev_w = w
    if for_cnt > 2 or repeat:
        errs.append(f"[AI 句首模板違規] 偵測到過多或連續重複的句首詞（For 開頭 {for_cnt} 點，上限 2；同區塊連續同字開頭={repeat}），請打散句首結構！")
    if sum(1 for l in bullets if l.count("(") >= 2 and re.search(r"\((?:to|in) [a-z]", l)) :
        errs.append("[規則備註括號] Bullet 內有解釋性括號堆疊，請改寫成正文")
    # 商業價值錨點：避免中翻英降維（voice-en §7）
    for num, words in ANCHORS.items():
        m = re.search(r"^### %s\b.*?(?=^### |^---|\Z)" % re.escape(num), t, re.M | re.S)
        body = m.group(0).lower() if m else ""
        for w in words:
            if w.lower() not in body:
                errs.append(f"區塊 {num} 缺少必備錨點「{w}」（Credibility Stripping）")
    for m in D.finditer(t):
        a = json.loads(m.group(1)).get("fields", {}).get("address")
        if a and (a.endswith(".") or "St. Beitou" in a):
            errs.append(f"address 標點錯誤：{a!r}")
    for blk in ("basic", "work_experience", "education", "languages"):
        if blk not in {json.loads(m.group(1)).get("target_block") for m in D.finditer(t)}:
            errs.append(f"缺少區塊 {blk}")
    if errs:
        print("❌ LINE profile 驗收失敗")
        for e in errs:
            print(" -", e)
        return 1
    print("✅ LINE profile 驗收通過")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
