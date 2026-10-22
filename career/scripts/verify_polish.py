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
STYLE_REL_PATH = "career/02_codex_stage/voice_style_guide.md"

# 2026-10-22 本人裁定：禁用詞分兩類。
# 1) 文體詞：純 AI 腔／空洞詞，命中即失敗。
DEFAULT_BANNED_TOKENS = [
    "負責日常", "聽從",
    "賦能", "抓手", "閉環", "攜手", "助力", "全方位", "深耕",
    "致力於", "成功地", "圓滿達成", "極大地", "顯著地", "透過", "藉由",
    "進行一個", "完成了"
]
# 2) 責任詞：真實責任界線可能正需要這些詞（例：協助製作銷售簡報），只警示、不失敗；
#    LOCKED 段落內不檢查。Codex 須逐點對照 library 確認該詞是真實責任。
RESPONSIBILITY_WARN_TOKENS = ["協助", "參與", "配合", "支援", "維護"]
# 3) 責任升級詞：成品出現而上游草稿同一點沒有 → 失敗（防止下游悄悄放大責任）。
#    「主導」只有 library 確認的兩件事（Juicy、JustDating 重新上架）可用，須由上游草稿先寫出。
OVERCLAIM_PATTERNS = [r"主導", r"架構", r"扛下", r"開發(?!中|複雜度)", r"實作", r"重構"]
LAZY_SIMILARITY_THRESHOLD = 0.99  # 2026-10-22 本人：不強求改寫比例，只攔原句照抄

TAG_PATTERN = re.compile(
    r"<!--\s*\[STATUS:\s*(?P<status>[A-Z_]+)\](?:\s*\[LOCK_ENTITIES:\s*(?P<entities>[^\]]+)\])?\s*-->"
)
BULLET_PATTERN = re.compile(r"^\s*[-*]\s+(?P<text>.+)$")
BOLD_PREFIX_PATTERN = re.compile(r"^\s*[-*]\s+\*\*[^*]+[：:]\*\*")

def read_from_git(branch_ref: str, rel_path: str):
    # 嘗試先 fetch 確保雲端環境拿到最新分支
    clean_branch = branch_ref.replace("origin/", "")
    subprocess.run(["git", "fetch", "origin", clean_branch], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    for ref in [branch_ref, clean_branch]:
        res = subprocess.run(["git", "show", f"{ref}:{rel_path}"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding="utf-8")
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
    print(f"❌ [FATAL] 無法讀取檔案：{rel_path} (分支: {target_branch})")
    sys.exit(2)

def parse_markdown_bullets(md_text: str):
    bullets = []
    current_status = "UNMARKED"
    current_entities = []
    current_section = "Header"
    for idx, line in enumerate(md_text.splitlines(), start=1):
        stripped = line.strip()
        if stripped.startswith("#"):
            current_section = stripped.lstrip("#").strip()
            continue
        tag_match = TAG_PATTERN.search(stripped)
        if tag_match:
            current_status = tag_match.group("status").strip()
            raw_entities = tag_match.group("entities")
            current_entities = [e.strip() for e in re.split(r"[,，、]", raw_entities) if e.strip()] if raw_entities else []
            continue
        bullet_match = BULLET_PATTERN.match(line)
        if bullet_match:
            bullets.append({
                "line_no": idx,
                "raw_line": line,
                "text": bullet_match.group("text").strip(),
                "status": current_status,
                "entities": current_entities,
                "section": current_section
            })
            current_status = "UNMARKED"
            current_entities = []
    return bullets

def run_verification(draft_text: str, final_text: str, banned_tokens):
    errors = []
    warnings = []
    for idx, line in enumerate(final_text.splitlines(), start=1):
        if "NEEDS_POLISH" in line:
            errors.append(f"[殘留標記錯誤] final_resume.md 第 {idx} 行仍殘留 NEEDS_POLISH 標記。")

    draft_bullets = parse_markdown_bullets(draft_text)
    final_bullets = parse_markdown_bullets(final_text)

    if len(draft_bullets) != len(final_bullets):
        errors.append(f"[結構不對稱] 上游草稿有 {len(draft_bullets)} 點，下游成品有 {len(final_bullets)} 點。嚴禁合併或增刪列點！")

    for i in range(min(len(draft_bullets), len(final_bullets))):
        d_item, f_item = draft_bullets[i], final_bullets[i]
        loc = f"第 {i+1} 點 ({d_item['section']} | 成品第 {f_item['line_no']} 行)"

        if d_item["status"] == "LOCKED" and d_item["text"] != f_item["text"]:
            errors.append(f"[越權修改] {loc} 標記為 LOCKED，但文字被更動！")
            continue

        if d_item["status"] == "NEEDS_POLISH":
            sim = difflib.SequenceMatcher(None, d_item["text"], f_item["text"]).ratio()
            if sim >= LAZY_SIMILARITY_THRESHOLD:
                errors.append(f"[漏修/偷懶攔截] {loc} 標記為 NEEDS_POLISH，但與原句相似度高達 {sim:.0%}！")

        for ent in d_item["entities"]:
            if ent not in f_item["text"]:
                errors.append(f"[事實遺失] {loc} 遺失了鎖定實體或數據：`{ent}`")

        if BOLD_PREFIX_PATTERN.match(f_item["raw_line"]):
            errors.append(f"[AI 排版違規] {loc} 使用了禁止的粗體摘要開頭 (**...：**)。")

        hit_banned = [t for t in banned_tokens if t in f_item["text"]]
        if hit_banned:
            errors.append(f"[禁用詞違規] {loc} 觸犯黑名單詞彙：{', '.join(hit_banned)}")

        for pat in OVERCLAIM_PATTERNS:
            fm = re.search(pat, f_item["text"])
            if fm and not re.search(pat, d_item["text"]):
                errors.append(f"[責任升級] {loc} 成品出現「{fm.group(0)}」，上游草稿同一點沒有；責任動詞須先由上游依 library 確認。")

        if d_item["status"] != "LOCKED":
            hit_resp = [t for t in RESPONSIBILITY_WARN_TOKENS if t in f_item["text"]]
            if hit_resp:
                warnings.append(f"[責任詞確認] {loc} 含「{'、'.join(hit_resp)}」：請對照 library 確認是真實責任，並在修改紀錄說明。")

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
        print(f"⚠️ 責任詞警示 {len(warnings)} 項（不影響通過，須在修改紀錄逐點說明）：\n" + "\n".join(f"  - {w}" for w in warnings))
    if errors:
        print(f"❌ 驗收失敗！共發現 {len(errors)} 項違規：\n" + "\n".join(f"{i+1}. {e}" for i, e in enumerate(errors)))
        sys.exit(1)
    print("✅ GATEKEEPER PASSED: 無漏修段落、LOCKED 完好、核心數據完整、零禁用詞！")
    sys.exit(0)

if __name__ == "__main__":
    main()
