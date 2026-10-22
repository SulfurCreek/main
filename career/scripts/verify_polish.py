#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
import difflib
import pathlib
import re
import subprocess
import sys

CLAUDE_BRANCH = "origin/claude/happy-lamport-ljis8c"
CODEX_BRANCH = "origin/codex/resume-writer"

DRAFT_REL_PATH = "career/01_claude_stage/causal_draft.md"
FINAL_REL_PATH = "career/02_codex_stage/final_resume.md"

DEFAULT_BANNED_TOKENS = [
    "負責日常", "聽從",
    "賦能", "抓手", "閉環", "攜手", "助力", "全方位", "深耕",
    "致力於", "成功地", "圓滿達成", "極大地", "顯著地", "透過", "藉由",
    "進行一個", "完成了"
]
RESPONSIBILITY_WARN_TOKENS = ["協助", "參與", "配合", "支援", "維護"]
OVERCLAIM_PATTERNS = [
    r"主導", r"架構", r"扛下",
    r"開發(?!中|複雜度|團隊|人員|部門|時程|資源|流程|模式)",
    r"實作", r"重構"
]
LAZY_SIMILARITY_THRESHOLD = 0.99

TAG_PATTERN = re.compile(
    r"<!--\s*\[STATUS:\s*(?P<status>[A-Z_]+)\](?:\s*\[LOCK_ENTITIES:\s*(?P<entities>[^\]]+)\])?\s*-->"
)
BOLD_PREFIX_PATTERN = re.compile(r"^\s*[-*]\s+\*\*[^*]+[：:]\*\*")

def read_from_git(branch_ref: str, rel_path: str):
    clean_branch = branch_ref.replace("origin/", "")
    for ref in [branch_ref, f"origin/{clean_branch}", clean_branch]:
        res = subprocess.run(
            ["git", "show", f"{ref}:{rel_path}"],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding="utf-8"
        )
        if res.returncode == 0:
            return res.stdout
    return None

def load_file_content(rel_path: str, target_branch: str, prefer_local: bool = False) -> str:
    local_path = pathlib.Path(rel_path)
    if prefer_local and local_path.exists():
        return local_path.read_text(encoding="utf-8")
    content = read_from_git(target_branch, rel_path)
    if content is not None:
        return content
    if local_path.exists():
        return local_path.read_text(encoding="utf-8")
    print(f"❌ [FATAL] 無法讀取檔案：{rel_path}")
    sys.exit(2)

def parse_tagged_blocks(md_text: str):
    """以 <!-- [STATUS: ...] --> 為單位解析全篇所有區塊（涵蓋簡介、特色、經歷、專長、自傳、專案）"""
    blocks = []
    current_section = "Header"
    active_block = None

    for idx, line in enumerate(md_text.splitlines(), start=1):
        stripped = line.strip()
        if stripped.startswith("#"):
            if active_block is not None:
                blocks.append(active_block)
                active_block = None
            current_section = stripped.lstrip("#").strip()
            continue

        tag_match = TAG_PATTERN.search(stripped)
        if tag_match:
            if active_block is not None:
                blocks.append(active_block)
            status = tag_match.group("status").strip()
            raw_entities = tag_match.group("entities")
            entities = [e.strip() for e in re.split(r"[,，]", raw_entities) if e.strip()] if raw_entities else []
            active_block = {
                "line_no": idx + 1,
                "status": status,
                "entities": entities,
                "section": current_section,
                "lines": []
            }
            continue

        if active_block is not None and stripped and not stripped.startswith("<!--"):
            active_block["lines"].append(line)

    if active_block is not None:
        blocks.append(active_block)

    for b in blocks:
        b["text"] = "\n".join(l.strip() for l in b["lines"])
    return blocks

def run_verification(draft_text: str, final_text: str, banned_tokens):
    errors = []
    warnings = []
    for idx, line in enumerate(final_text.splitlines(), start=1):
        if "NEEDS_POLISH" in line:
            errors.append(f"[殘留標記錯誤] final_resume.md 第 {idx} 行仍殘留 NEEDS_POLISH 標記。")

    draft_blocks = parse_tagged_blocks(draft_text)
    final_blocks = parse_tagged_blocks(final_text)

    if len(draft_blocks) != len(final_blocks):
        errors.append(f"[結構不對稱] 上游草稿有 {len(draft_blocks)} 個標記區塊，下游成品有 {len(final_blocks)} 個。請確認每個區塊上方皆保留 <!-- [STATUS: POLISHED/LOCKED] --> 標記！")

    for i in range(min(len(draft_blocks), len(final_blocks))):
        d_item, f_item = draft_blocks[i], final_blocks[i]
        loc = f"區塊 #{i+1} ({d_item['section']} | 成品第 {f_item['line_no']} 行)"

        if d_item["status"] == "LOCKED" and d_item["text"] != f_item["text"]:
            errors.append(f"[越權修改] {loc} 標記為 LOCKED，但文字被更動！")
            continue

        if d_item["status"] == "NEEDS_POLISH":
            sim = difflib.SequenceMatcher(None, d_item["text"], f_item["text"]).ratio()
            if sim >= LAZY_SIMILARITY_THRESHOLD:
                errors.append(f"[漏修/偷懶攔截] {loc} 標記為 NEEDS_POLISH，但完全原句照抄 (相似度 {sim:.0%})！")

        for ent in d_item["entities"]:
            if ent not in f_item["text"]:
                errors.append(f"[事實遺失] {loc} 遺失了鎖定實體或數據：`{ent}`")

        for raw_l in f_item["lines"]:
            if BOLD_PREFIX_PATTERN.match(raw_l):
                errors.append(f"[AI 排版違規] {loc} 使用了禁止的粗體摘要開頭 (**...：**)。")

        if d_item["status"] != "LOCKED":
            hit_banned = [t for t in banned_tokens if t in f_item["text"]]
            if hit_banned:
                errors.append(f"[禁用詞違規] {loc} 觸犯黑名單詞彙：{', '.join(hit_banned)}")

            for pat in OVERCLAIM_PATTERNS:
                fm = re.search(pat, f_item["text"])
                if fm and not re.search(pat, d_item["text"]):
                    errors.append(f"[責任升級] {loc} 成品出現「{fm.group(0)}」，上游草稿同一區塊沒有。")

            hit_resp = [t for t in RESPONSIBILITY_WARN_TOKENS if t in f_item["text"]]
            if hit_resp:
                warnings.append(f"[責任詞提示] {loc} 含「{'、'.join(hit_resp)}」（不影響通過）。")

    return errors, warnings

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--local-codex", action="store_true")
    args = parser.parse_args()

    if args.local_codex:
        draft_text = load_file_content(DRAFT_REL_PATH, CLAUDE_BRANCH, prefer_local=False)
        final_text = load_file_content(FINAL_REL_PATH, CODEX_BRANCH, prefer_local=True)
    else:
        draft_text = load_file_content(DRAFT_REL_PATH, CLAUDE_BRANCH, prefer_local=True)
        final_text = load_file_content(FINAL_REL_PATH, CODEX_BRANCH, prefer_local=False)

    errors, warnings = run_verification(draft_text, final_text, DEFAULT_BANNED_TOKENS)
    if warnings:
        print(f"⚠️ 責任詞提示 {len(warnings)} 項（不影響通過）：\n" + "\n".join(f"  - {w}" for w in warnings))
    if errors:
        print(f"❌ 驗收失敗！共發現 {len(errors)} 項違規：\n" + "\n".join(f"{i+1}. {e}" for i, e in enumerate(errors)))
        sys.exit(1)
    print(f"✅ GATEKEEPER PASSED: 全篇 {len(parse_tagged_blocks(final_text))} 個標記區塊（簡介、特色、經歷、專長、自傳、專案）全數檢查通過！")
    sys.exit(0)

if __name__ == "__main__":
    main()
