#!/usr/bin/env python3
"""驗證 Codex 潤飾結果（階段 03，Claude 執行）。

用法：python3 career/scripts/verify_polish.py <causal_draft.md> <final_resume.md>
檢查：
  1. 漏修／殘留標記：final 中不得殘留 [STATUS: ...]／[LOCK_ENTITIES: ...]。
  2. 鎖定實體：draft 每個 LOCK_ENTITIES 詞都要出現在 final。
  3. LOCKED 段落：draft 中 STATUS: LOCKED 的 bullet 文字須原樣出現在 final。
  4. 未定義專有名詞：draft〈實體字典〉的實體，在 final 首次出現處須在同一行帶有字典中的外部定義關鍵詞（粗略檢查，人工複核）。
  5. 披露：final 不得出現投票名次、預計上線日期、延後、開發中、目標值當成效等字樣。
exit 0＝全過；1＝有問題（逐條列出）。
"""
import re, sys

draft, final = (open(p, encoding="utf8").read() for p in sys.argv[1:3])
bad = []

if re.search(r"\[STATUS:|\[LOCK_ENTITIES:", final):
    bad.append("final 仍有交接標記（漏修或未清除）")

for m in re.finditer(r"<!--\s*\[STATUS:\s*(\w+)\](?:\s*\[LOCK_ENTITIES:\s*([^\]]*)\])?\s*-->\s*\n(- .*)", draft):
    status, ents, bullet = m.group(1), m.group(2) or "", m.group(3)
    for e in [x.strip() for x in ents.split(",") if x.strip()]:
        if e not in final:
            bad.append(f"鎖定實體遺失：「{e}」（{bullet[:30]}…）")
    if status == "LOCKED" and bullet[2:].strip() not in final:
        bad.append(f"LOCKED 段落被改：{bullet[:40]}…")

dic = re.search(r"## 實體字典.*?\n((?:\|.*\n)+)", draft)
if dic:
    for row in dic.group(1).splitlines()[2:]:
        cells = [c.strip() for c in row.strip("|").split("|")]
        if len(cells) < 2 or not cells[0]:
            continue
        ent, definition = cells[0], cells[1]
        line = next((l for l in final.splitlines() if ent in l), None)
        if line is None:
            continue
        keys = [k for k in re.split(r"[，、；（）()\s]+", definition) if len(k) >= 2][:4]
        if keys and not any(k in line for k in keys):
            bad.append(f"可能未定義：「{ent}」首次出現的那行沒有外部定義線索（{'/'.join(keys)}）")

for pat, why in [(r"第一名|票選第|排名第|業務投票", "未公開排序"), (r"預計\s*20\d\d|預計.{0,6}上線", "預計日期"),
                 (r"延後.{0,8}功能", "延後項目"), (r"150%|配對率", "目標當成效")]:
    for hit in re.findall(pat, final):
        bad.append(f"披露：{why}「{hit}」")

print("\n".join(f"✗ {b}" for b in bad) if bad else "✓ 全部通過")
sys.exit(1 if bad else 0)
