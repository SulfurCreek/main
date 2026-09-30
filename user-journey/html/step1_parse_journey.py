"""解析 ../recruiter_journey_map.md → report_data.json。

素材格式＝user-journey-map skill 三段式（1. Context／2. The Journey Grid／3. Key Takeaways）＋附錄。
只搬運，不改寫、不補齊、不自編編號；〈路由〉是給 AI 的索引，不進 HTML。
"""
import re, json, pathlib

HERE = pathlib.Path(__file__).parent
# 使用者指示：痛點相關資訊先不呈現（素材不改，只在 HTML 端略過）
HIDE_LANES = {"Pain Points"}
HIDE_CONTEXT_PREFIX = ("核心痛點",)
HIDE_GAP_KEYWORD = "痛點"
SRC = HERE.parent / "recruiter_journey_map.md"
OUT = HERE / "report_data.json"
text = SRC.read_text(encoding="utf-8")


def h2(prefix):
    m = re.search(rf"^## ({re.escape(prefix)}[^\n]*)\n(.*?)(?=^## |\Z)", text, re.M | re.S)
    if not m:
        raise SystemExit(f"找不到章節：{prefix}")
    return m.group(1).strip(), m.group(2)


def h3(block, prefix):
    m = re.search(rf"^### ({re.escape(prefix)}[^\n]*)\n(.*?)(?=^### |\Z)", block, re.M | re.S)
    if not m:
        raise SystemExit(f"找不到小節：{prefix}")
    return m.group(1).strip(), m.group(2)


def table_rows(block):
    rows = []
    for ln in block.splitlines():
        ln = ln.strip()
        if not ln.startswith("|") or re.match(r"^\|\s*:?-{2,}", ln):
            continue
        rows.append([c.strip() for c in re.split(r"(?<!\\)\|", ln.strip("|"))])
    return rows


def bullets(block):
    """`* **Label (Sub):** text` 與縮排子項 → [{label, sub, text, children}]"""
    items = []
    for ln in block.splitlines():
        m = re.match(r"^[*-] \*\*(.+?)(?:\s*\(([^)]*)\))?:\*\*\s*(.*)$", ln)
        if m:
            items.append({"label": m.group(1).strip(), "sub": (m.group(2) or "").strip(), "text": m.group(3).strip(), "children": []})
            continue
        m = re.match(r"^\s+(?:[*-]|\d+\.)\s+(.*)$", ln)
        if m and items:
            items[-1]["children"].append(m.group(1).strip())
    return items


head = text.split("\n---", 1)[0]
title = re.search(r"^# (.+)$", head, re.M).group(1)
head_bullets = [l[2:] for l in head.splitlines() if l.startswith("- ")]

ctx_h, ctx_b = h2("1. Context")
context = bullets(ctx_b)
for it in context:
    it["children"] = [c for c in it["children"] if not c.startswith(HIDE_CONTEXT_PREFIX)]
marker_note = next((l[2:].strip() for l in ctx_b.splitlines() if l.startswith("> ")), "")

grid_h, grid_b = h2("2. The Journey Grid")
grid_intro = next((l.strip() for l in grid_b.splitlines() if l.strip() and not l.startswith(("#", "|"))), "")
lane_order, lane_meta, stages, groups = [], {}, [], []
for m in re.finditer(r"^### (.+?)$(.*?)(?=^### |\Z)", grid_b, re.M | re.S):
    gtitle, body = m.group(1).strip(), m.group(2)
    rows = table_rows(body)
    phases = rows[0][1:]
    groups.append({"title": gtitle, "start": len(stages), "count": len(phases)})
    cols = [{"name": p, "code": p.split()[0], "cells": {}} for p in phases]
    for r in rows[1:]:
        if re.match(r"\*\*(.+?)\*\*", r[0]).group(1).strip() in HIDE_LANES:
            continue
        lm = re.match(r"\*\*(.+?)\*\*(?:<br>\((.+?)\))?", r[0])
        en, zh = lm.group(1).strip(), (lm.group(2) or "").strip()
        if en not in lane_meta:
            lane_order.append(en); lane_meta[en] = zh
        for i, c in enumerate(cols):
            c["cells"][en] = r[i + 1] if i + 1 < len(r) else ""
    stages.extend(cols)

app_h, app_b = h2("附錄")
doc_h, doc_b = h3(app_b, "文件關係")
library = json.loads((HERE / "sitemap_docs.json").read_text(encoding="utf-8"))   # 由 step0 依 HackMD Sitemap 產生
gap_h, gap_b = h3(app_b, "缺口")
gaps = [l[2:] for l in gap_b.splitlines() if l.startswith("- ") and HIDE_GAP_KEYWORD not in l]

data = {"title": title, "head_bullets": head_bullets,
        "context": {"heading": ctx_h, "items": context, "marker_note": marker_note},
        "grid": {"heading": grid_h, "intro": grid_intro, "groups": groups,
                 "lanes": [{"en": k, "zh": lane_meta[k]} for k in lane_order], "stages": stages},
        "appendix": {"heading": app_h, "doc_heading": doc_h, "library": library,
                     "gap_heading": gap_h, "gaps": gaps}}
OUT.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")

# 自檢：Grid 每格都有值（空字串代表解析漏抓）
empty = [(s["name"], k) for s in stages for k in lane_order if not s["cells"].get(k)]
print(f"context={len(context)} lanes={lane_order} stages={[s['name'] for s in stages]} groups={len(groups)}")
print(f"gaps={len(gaps)} library_modules={len(library['modules'])}")
print("空格（應為 0）:", empty)
