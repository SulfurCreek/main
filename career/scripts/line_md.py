#!/usr/bin/env python3
"""LINE 英文履歷／Profile Markdown 解析契約（驗證器與產生器共用，2026-11-02）。

支援格式（以內容判定，不靠章節編號）：
- resume：含「Professional Summary」二級標題（Summary 第一點＋Skills 其餘點），加上 directive 區塊。
  可產生 fill.json＋resume.json＋PDF。
- profile：沒有 Summary 區塊，只有 directive 區塊與工作列點（例：Codex line-profile-polished.md）。
  只能驗證，不能產生 PDF／填表包（缺 summary_text），前置驗證即明確拒絕。

所有正文檢查只看「對外正文」：HTML 註解（含 directive 與 STATUS 標記）一律剔除。
"""
import json
import re

DIRECTIVE = re.compile(r"<!--\s*@line-directive\s*(\{.*?\})\s*-->", re.S)
COMMENT = re.compile(r"<!--.*?-->", re.S)
FIELDS = {
    "basic": ["email", "mobile_phone", "current_position_title", "current_employer", "country", "address", "city"],
    "work_experience": ["company", "position_title", "employment_type", "location", "start_date", "end_date"],
    "education": ["degree_name", "type_of_degree", "degree_status", "university", "start_date", "end_date"],
    "languages": ["language", "written", "spoken", "reading", "listening"],
}
OPTIONAL_EMPTY = {("work_experience", "end_date"), ("education", "end_date")}
ACTIONS = {"basic": {"replace_all"}, "work_experience": {"replace_row"}, "education": {"replace_row"}, "languages": {"replace_row"}}
COUNT = {"basic": (1, 1), "work_experience": (1, 20), "education": (1, 10), "languages": (1, 10)}
PURPOSES = {"verify": {"resume", "profile"}, "pack": {"resume"}, "pdf": {"resume"}}


class DupKey(ValueError):
    pass


def _no_dup(pairs):
    seen = {}
    for k, v in pairs:
        if k in seen:
            raise DupKey(f"重複鍵：{k}")
        seen[k] = v
    return seen


def visible(text):
    """對外正文：剔除所有 HTML 註解。"""
    return COMMENT.sub("", text)


def bullets_of(chunk):
    return [l[2:].strip() for l in visible(chunk).splitlines() if l.startswith("- ")]


def parse(text):
    """回傳 doc：format、summary、skills、statement、directives（含 bullets）、errors（結構錯誤）。"""
    doc = {"format": None, "summary": None, "skills": [], "statement": [], "directives": [], "errors": []}
    heads = list(re.finditer(r"^(#{2,3}) (.+)$", text, re.M))
    summ = next((h for h in heads if h.group(1) == "##" and re.search(r"Professional Summary", h.group(2), re.I)), None)
    if summ:
        nxt = next((h.start() for h in heads if h.start() > summ.start() and h.group(1) == "##"), len(text))
        sec = text[summ.end():nxt]
        stmt = re.search(r"^#{2,3} .*Personal Statement.*$", sec, re.M | re.I)
        if stmt:
            st = sec[stmt.end():].split("\n---")[0]
            doc["statement"] = [p.strip() for p in visible(st).split("\n\n") if p.strip()]
            sec = sec[:stmt.start()]
        bl = bullets_of(sec.split("\n---")[0])
        if not bl:
            doc["errors"].append("Professional Summary 區塊沒有任何列點")
        else:
            doc["summary"], doc["skills"] = bl[0], bl[1:]
        doc["format"] = "resume"
    else:
        doc["format"] = "profile"
    ms = list(DIRECTIVE.finditer(text))
    for i, m in enumerate(ms):
        line = text.count("\n", 0, m.start()) + 1
        try:
            d = json.loads(m.group(1), object_pairs_hook=_no_dup)
        except (ValueError, DupKey) as e:
            doc["errors"].append(f"第 {line} 行 directive JSON 錯誤：{e}")
            continue
        end = ms[i + 1].start() if i + 1 < len(ms) else len(text)
        chunk = text[m.end():end]
        cut = re.search(r"^#{2,3} ", chunk, re.M)
        chunk = chunk[:cut.start()] if cut else chunk
        doc["directives"].append({"line": line, "d": d, "bullets": bullets_of(chunk)})
    return doc


def validate(doc, purpose="verify"):
    """格式契約：區塊、欄位、型別、非空、action、index、數量；用途不支援時明確拒絕。"""
    errs = list(doc["errors"])
    if doc["format"] not in PURPOSES.get(purpose, set()):
        errs.append(f"[不支援的格式] 用途「{purpose}」只接受 {sorted(PURPOSES.get(purpose, set()))}，本檔判定為「{doc['format']}」"
                    "（缺 Professional Summary 區塊）；請先補 Summary 或改用 verify 用途，不在轉換時才失敗")
    seen = {b: [] for b in FIELDS}
    for item in doc["directives"]:
        d, ln = item["d"], item["line"]
        if not isinstance(d, dict):
            errs.append(f"第 {ln} 行 directive 不是物件"); continue
        b = d.get("target_block")
        if b not in FIELDS:
            errs.append(f"第 {ln} 行 未知 target_block：{b!r}"); continue
        if d.get("action") not in ACTIONS[b]:
            errs.append(f"第 {ln} 行 {b} 的 action={d.get('action')!r} 不允許（只接受 {sorted(ACTIONS[b])}）")
        extra = set(d) - {"target_block", "action", "index", "fields"}
        if extra:
            errs.append(f"第 {ln} 行 directive 有未知鍵：{sorted(extra)}")
        f = d.get("fields")
        if not isinstance(f, dict):
            errs.append(f"第 {ln} 行 {b}.fields 必須是物件"); continue
        if set(f) != set(FIELDS[b]):
            errs.append(f"第 {ln} 行 {b} 欄位不符：多 {sorted(set(f) - set(FIELDS[b]))} 缺 {sorted(set(FIELDS[b]) - set(f))}")
        for k, v in f.items():
            if not isinstance(v, str):
                errs.append(f"第 {ln} 行 {b}.{k} 必須為字串")
            elif not v.strip() and (b, k) not in OPTIONAL_EMPTY:
                errs.append(f"第 {ln} 行 {b}.{k} 為必要欄位，不得留空")
        if b == "basic":
            if "index" in d:
                errs.append(f"第 {ln} 行 basic 不得有 index")
            seen[b].append(0)
        else:
            idx = d.get("index")
            if not isinstance(idx, int) or isinstance(idx, bool):
                errs.append(f"第 {ln} 行 {b}.index 必須是整數")
            seen[b].append(idx)
    for b, (lo, hi) in COUNT.items():
        n = len(seen[b])
        if not lo <= n <= hi:
            errs.append(f"[區塊數量] {b} 有 {n} 個（須 {lo}–{hi} 個）")
        if b != "basic" and seen[b] and seen[b] != list(range(n)):
            errs.append(f"[index] {b} index 須為 0..{n - 1} 連號，目前 {seen[b]}")
    return errs


def payload(doc):
    """產生器用的單一資料來源：同一份 doc 轉成 resume.json 的 steps。"""
    steps = []
    for i, item in enumerate(doc["directives"], 1):
        d = item["d"]
        st = {"step": i, "target_block": d["target_block"], "action": d["action"], "index": d.get("index"), "fields": d["fields"]}
        if item["bullets"]:
            st["description_bullets"] = item["bullets"]
            st["description_text"] = "\n".join("• " + b for b in item["bullets"])
        steps.append(st)
    return steps
