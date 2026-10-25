#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把 Codex 定稿 final_resume.md 轉成 104 公開版來源（去除現職 1111 的可識別資訊）。

規則來源：library/decisions.md §38、104/antigravity-public-redaction-skill.md、
Codex 交接 drafts/codex/2026-10-25-public-wording-handoff.md。替換同時作用於正文與 [G]/[B]/[BT] 註解。

用法：python3 public_redact.py <final_resume.md> <輸出 public.md>
"""
import re
import sys

REPLACE = [
    ("｜1111 全球華人｜", "｜公司名暫不公開｜"),
    ("2026 Q3 服務約 6 萬家活躍付費廠商", "服務數萬家付費企業客戶"),
    ("約 6 萬家活躍付費廠商", "數萬家付費企業客戶"),
    ("現任 1111人力銀行招募系統", "現任人力銀行企業端招募系統"),
    ("1111人力銀行招募系統", "人力銀行企業端招募系統"),
    ("1111 人力銀行", "人力銀行"),
    ("1111人力銀行", "人力銀行"),
    ("我加入 1111，", "我加入目前的公司，"),
    ("1111 新版求才系統重整", "企業端招募系統全面改版"),
    ("1111 企業群組共同招募", "企業群組共同招募"),
    ("新版求才系統", "新版系統"),
    ("招募管理", "招募系統"),
    # Codex 交接：類別代碼表第一句（公開版專用）
    ("職務、證照、技能、福利等 15 張類別代碼表，是全站職缺刊登、履歷填寫、搜尋篩選與配對推薦的共同分類基礎。",
     "職務、證照、技能與福利等分類資料，是全站職缺刊登、履歷填寫、搜尋篩選與配對推薦的共同基礎。"),
    ("[B: 類別代碼表]", "[B: 分類資料]"),
    # 通用：句型改寫後仍能去掉「15 張」（2026-10-25，Codex 03a354f 改寫後原句不再命中）
    ("[G: 15 張 | ", "[G: "),
    ("等 15 張類別代碼表", "等分類資料"),
    ("15 張類別代碼表", "分類資料"),
]
FORBIDDEN = ["1111", "全球華人", "求才", "招募管理", "冒用", "6 萬家", "15 張"]


def main():
    src, out = sys.argv[1:3]
    t = open(src, encoding="utf-8").read()
    # 刪除帳號冒用整條（含其狀態註解）
    t, n = re.subn(r"<!-- \[STATUS:[^\n]*-->\n- [^\n]*冒用[^\n]*\n", "", t)
    assert n == 1, f"冒用條數 {n}"
    for a, b in REPLACE:
        t = t.replace(a, b)
    body = re.sub(r"<!--.*?-->", "", t, flags=re.S)
    left = [k for k in FORBIDDEN if k in body or k in t]
    if left:
        print("❌ 公開版仍含：" + "、".join(left))
        sys.exit(1)
    open(out, "w", encoding="utf-8").write(t)
    print(f"✅ 公開版來源 {out}；{len(REPLACE)} 組替換＋刪除冒用條，禁用字串皆 0 筆")


if __name__ == "__main__":
    main()
