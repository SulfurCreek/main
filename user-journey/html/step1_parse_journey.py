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

intro_h, intro_b = h2("給沒有專案背景的讀者")
paras = [l.strip() for l in intro_b.splitlines() if l.startswith("**")]
tbls = [t for t in re.split(r"\n\s*\n", intro_b) if t.strip().startswith("|")]
intro = {"heading": intro_h, "notes": [l for l in paras if not l.startswith("**階段讀法**")],
         "stage_hdr": table_rows(tbls[0])[0], "stage_rows": table_rows(tbls[0])[1:]}

# ---------- 1. Persona（總覽／P1~P7／受限廠商類型／名詞）----------
ps_h, ps_b = h2("1. Persona")
STAGES9 = ["J", "A", "B", "C", "D", "E", "5", "6", "7"]
STAGE_NM = {"J": "登入", "A": "首頁", "B": "公司", "C": "職缺", "D": "人才", "E": "聯繫", "5": "紀錄", "6": "服務", "7": "購買"}


def bullets2(block):
    """`* **Key：** text` ＋縮排子項 → [{key, text, children}]（Key 可含全形冒號）"""
    out = []
    for ln in block.splitlines():
        m = re.match(r"^\* \*\*(.+?)[：:]\*\*\s*(.*)$", ln)
        if m:
            out.append({"key": m.group(1).strip(), "text": m.group(2).strip(), "children": []}); continue
        m = re.match(r"^\s+[*-]\s+(.*)$", ln)
        if m and out:
            out[-1]["children"].append(m.group(1).strip())
    return out


def stage_states(txt):
    """「可走的旅程」文字 → {stage: ok|partial|conditional|blocked|unknown} ＋備註。只依文字照搬，不補推論。
    列了階段＋「依權限代碼」→ 被列的階段變 conditional；沒列階段只寫「依權限代碼」→ 全部 conditional。"""
    if re.search(r"全部階段", txt):
        return {k: {"state": "ok", "note": ""} for k in STAGES9}
    st = {k: {"state": "unknown", "note": ""} for k in STAGES9}
    listed = False
    for tok in re.split(r"[；;、]", txt):
        m = re.match(r"^(?:〔推論〕)?\s*(?:以\s*)?(J|A|B|C|D|E|5|6／7|6|7)(\.\d+)?\s*(.*)$", tok.strip())
        if not m:
            continue
        listed = True
        code, sub, rest = m.group(1), m.group(2), m.group(3)
        blocked = bool(re.search(r"不可|暫停", rest))
        note = (code + (sub or "") + " " + rest).strip() if (blocked or sub or "（" in rest) else ""
        for k in (["6", "7"] if code == "6／7" else [code]):
            st[k] = {"state": "blocked" if blocked else "partial" if sub else "ok", "note": note}
    if "依權限代碼" in txt:
        for k in STAGES9:
            if not listed or st[k]["state"] in ("ok", "partial"):
                st[k]["state"] = "conditional"
    return st


overview = []
ov = re.search(r"^### Persona 總覽\n(.*?)(?=^### )", ps_b, re.M | re.S)
ov_rows = table_rows(ov.group(1))
ov_hdr, ov_data = ov_rows[0], ov_rows[1:]
ov_notes = [l[2:].strip() for l in ov.group(1).splitlines() if l.startswith("* ")]
personas = []
for m in re.finditer(r"^### (P\d+) (.+?)\n(.*?)(?=^### |\Z)", ps_b, re.M | re.S):
    pid, pname, body = m.groups()
    q = next((l[2:].strip() for l in body.splitlines() if l.startswith("> ")), "")
    items = bullets2(body)
    journey = next((i for i in items if i["key"].startswith("可走的旅程")), None)
    row = next((r for r in ov_data if r[0].startswith(pid + " ")), [])
    personas.append({"id": pid, "name": pname.strip(), "quote": q, "items": [i for i in items if i is not journey],
                     "journey_text": journey["text"] if journey else "", "stages": stage_states(journey["text"]) if journey else {},
                     "overview": row})
mod = re.search(r"^### 受限廠商類型[^\n]*\n(.*?)(?=^### )", ps_b, re.M | re.S)
mod_rows = table_rows(mod.group(1))
mod_intro = next((l.strip() for l in mod.group(1).splitlines() if l.strip() and not l.startswith(("|", "*"))), "")
mod_notes = [l[2:].strip() for l in mod.group(1).splitlines() if l.startswith("* ")]
modifiers = []
for r in mod_rows[1:]:
    toks = [t.strip() for t in r[3].split("、")]
    stg = {}
    for t in toks:
        mm = re.match(r"^(J|A|B|C|D|E|5|6／7|6|7)\s", t)
        if mm:
            for k in (["6", "7"] if mm.group(1) == "6／7" else [mm.group(1)]):
                stg[k] = "中斷" if "中斷" in t else "limit"
    modifiers.append({"name": r[0], "flag": r[1], "limit": r[2], "impact": r[3], "stages": stg})
nm = re.search(r"^### 名詞\n(.*?)(?=^## |\Z)", ps_b, re.M | re.S)
nm_rows = table_rows(nm.group(1))
persona_scope = (re.search(r"\*\*旅程範圍：\*\*\s*(.+)", ps_b) or [None, ""])[1].strip()
persona_intro = next((l.strip() for l in ps_b.splitlines() if l.strip() and not l.startswith(("#", "|", "*", ">", "<", "**")) ), "")
persona = {"heading": ps_h, "intro": persona_intro, "scope": persona_scope,
           "overview": {"hdr": ov_hdr, "notes": ov_notes}, "personas": personas,
           "modifiers": {"intro": mod_intro, "notes": mod_notes, "items": modifiers},
           "terms": {"hdr": nm_rows[0], "rows": nm_rows[1:], "note": next((l[2:].strip() for l in nm.group(1).splitlines() if l.startswith("> ")), "")},
           "stages9": [{"code": k, "name": STAGE_NM[k]} for k in STAGES9]}

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
# 流程圖索引（在〈路由〉節內，AI 索引表）＋ step0 渲染好的 SVG
flows = []
fi = re.search(r"^### 流程圖索引\n(.*?)(?=^#{2,3} |\Z)", text, re.M | re.S)
manifest = {(m["stage"], m["shortId"]): m for m in json.loads((HERE / "flows" / "manifest.json").read_text(encoding="utf-8"))} if (HERE / "flows" / "manifest.json").exists() else {}
for r in table_rows(fi.group(1)) if fi else []:
    if r[0] == "階段" or len(r) < 5:
        continue
    ids = re.findall(r"`([A-Za-z0-9_-]{9,22})`", r[3])
    lm = re.search(r"\((https?://[^)\s]+)\)", r[4])
    code = r[0].split()[0]
    ent = manifest.get((code, ids[1])) if len(ids) > 1 else None
    flows.append({"stage": code, "stage_name": r[0], "name": r[1], "type": r[2],
                  "doc_title": re.sub(r"（.*", "", r[3]).strip(), "link": lm.group(1) if lm else "",
                  "svgs": [(HERE / "flows" / f).read_text(encoding="utf-8") for f in (ent["svgs"] if ent else [])]})
doc_h, doc_b = h3(app_b, "文件關係")
library = json.loads((HERE / "sitemap_docs.json").read_text(encoding="utf-8"))   # 由 step0 依 HackMD Sitemap 產生
gap_h, gap_b = h3(app_b, "缺口")
gaps = [l[2:] for l in gap_b.splitlines() if l.startswith("- ") and HIDE_GAP_KEYWORD not in l]

todo = re.search(r"^### 待辦[^\n]*\n(.*?)(?=^#{2,3} |\Z)", app_b, re.M | re.S)
todo_h = re.search(r"^### (待辦[^\n]*)", app_b, re.M)
todo_items = []
for ln in (todo.group(1).splitlines() if todo else []):
    m = re.match(r"^[*-] (.*)$", ln)
    if m: todo_items.append({"text": m.group(1), "children": []})
    m = re.match(r"^\s+[*-] (.*)$", ln)
    if m and todo_items: todo_items[-1]["children"].append(m.group(1))

data = {"title": title, "intro": intro, "persona": persona, "todo": {"heading": todo_h.group(1) if todo_h else "", "items": todo_items}, "head_bullets": head_bullets,
        "grid": {"heading": grid_h, "intro": grid_intro, "groups": groups,
                 "lanes": [{"en": k, "zh": lane_meta[k]} for k in lane_order], "stages": stages},
        "flows": flows,
        "appendix": {"heading": app_h, "doc_heading": doc_h, "library": library,
                     "gap_heading": gap_h, "gaps": gaps}}
OUT.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")

# 自檢：Grid 每格都有值（空字串代表解析漏抓）
empty = [(s["name"], k) for s in stages for k in lane_order if not s["cells"].get(k)]
print(f"personas={len(personas)} modifiers={len(modifiers)} terms={len(nm_rows)-1} lanes={lane_order} stages={[s['name'] for s in stages]} groups={len(groups)}")
print("flows:", [(f["stage"], f["name"][:12], len(f["svgs"])) for f in flows])
print(f"gaps={len(gaps)} library_modules={len(library['modules'])}")
print("空格（應為 0）:", empty)
