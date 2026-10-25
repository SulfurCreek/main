#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
import difflib
import html
import pathlib
import re
import subprocess
import sys

CLAUDE_BRANCH = "origin/claude/happy-lamport-ljis8c"
CODEX_BRANCH = "origin/codex/resume-writer"

DRAFT_REL_PATH = "career/01_claude_stage/causal_draft.md"
FINAL_REL_PATH = "career/02_codex_stage/final_resume.md"

# 1. 文體禁用詞（AI 套話與生硬連接詞）
DEFAULT_BANNED_TOKENS = [
    "負責日常", "聽從",
    "賦能", "抓手", "閉環", "攜手", "助力", "全方位", "深耕",
    "致力於", "成功地", "圓滿達成", "極大地", "顯著地", "透過", "藉由",
    "進行一個", "完成了"
]

# 2. 歷史踩坑之「日常行政流水帳 / 被動聽命 / 已否決幻覺詞」（硬性攔截！）
CHORE_AND_HALLUCINATION_TOKENS = [
    "互相代理",             # 已否決之群組功能幻覺詞
    "依公司政策", "配合公司方向", "依主管政策",  # 被動聽命字眼（若需交代限制請依核准句型，禁止此三詞）
    "每週統一回報", "每週回報", "每月彙整一批",  # 例行行政匯報流水帳
    "並處理翻譯",           # 句尾順帶雜務感
    "送簽流程", "及送簽", "結案確認",           # 內部行政表單流水帳
    "新增、編輯、合併、刪除",                   # CRUD 流水帳羅列
    "報表無付費數據",       # 內部備註誤留正文
    "刊案", "RBAC"                  # 內部行話，對外讀不懂（2026-10-24 本人）
]

# 3. 104 絕對禁止無中生有之假工具標籤（防 Flash / 範本污染）
FORBIDDEN_104_TAGS = [
    "Tableau", "SimilarWeb", "JIRA", "Jira", "Xmind",
    "Google Tag Manager", "Machine Learning", "機器學習", "SQL"
]

RESPONSIBILITY_WARN_TOKENS = ["協助", "參與", "配合", "支援", "維護"]
OVERCLAIM_PATTERNS = [
    r"主導", r"架構", r"扛下",
    r"開發(?!中|複雜度|團隊|人員|部門|時程|資源|流程|模式)",
    r"實作", r"重構", r"確立", r"制定(?!驗收)"
]
UNRESOLVED_BRACKET_PATTERN = re.compile(r"〔[^〕]*(?:待補|待確認|待本人|確認)[^〕]*〕")
LAZY_SIMILARITY_THRESHOLD = 0.99

TAG_PATTERN = re.compile(r"<!--\s*\[STATUS:\s*(?P<status>[A-Z_]+)\](?P<attrs>(?:\s*\[[A-Z_]+:[^\]]*\])*)\s*-->")
ATTR_PATTERN = re.compile(r"\[(?P<key>[A-Z_]+):\s*(?P<val>[^\]]*)\]")
VISUAL_KEYS = ("G", "B", "BT")  # G＝金黃底色、B＝晴藍底色＋粗體、BT＝純粗體；值以 | 分隔

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
            attrs = {m.group("key"): m.group("val").strip() for m in ATTR_PATTERN.finditer(tag_match.group("attrs") or "")}
            raw_entities = attrs.get("LOCK_ENTITIES")
            entities = [e.strip() for e in re.split(r"[,，]", raw_entities) if e.strip()] if raw_entities else []
            visual = {k: [v.strip() for v in attrs[k].split("|") if v.strip()] for k in VISUAL_KEYS if k in attrs}
            active_block = {
                "line_no": idx + 1,
                "status": status,
                "entities": entities,
                "visual": visual,
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

def run_verification(draft_text: str, final_text: str):
    errors = []
    warnings = []
    for idx, line in enumerate(final_text.splitlines(), start=1):
        if "NEEDS_POLISH" in line:
            errors.append(f"[殘留標記錯誤] final_resume.md 第 {idx} 行仍殘留 NEEDS_POLISH 標記。")

    draft_blocks = parse_tagged_blocks(draft_text)
    final_blocks = parse_tagged_blocks(final_text)

    if len(draft_blocks) != len(final_blocks):
        errors.append(
            f"[結構不對稱] 上游草稿有 {len(draft_blocks)} 個標記區塊，下游成品有 {len(final_blocks)} 個。"
            "請確認每個區塊上方皆保留 <!-- [STATUS: POLISHED/LOCKED] --> 標記！"
        )

    for i in range(min(len(draft_blocks), len(final_blocks))):
        d_item, f_item = draft_blocks[i], final_blocks[i]
        loc = f"區塊 #{i+1} ({d_item['section']} | 成品第 {f_item['line_no']} 行)"

        # 檢查上游或下游是否殘留未解決的〔待確認/待補〕括號
        for label, txt in [("上游草稿", d_item["text"]), ("下游成品", f_item["text"])]:
            m_br = UNRESOLVED_BRACKET_PATTERN.search(txt)
            if m_br:
                errors.append(f"[未清內部括號] {loc} {label}殘留未確認標記：`{m_br.group(0)}`")

        if d_item["status"] == "LOCKED" and d_item["text"] != f_item["text"]:
            errors.append(f"[越權修改] {loc} 標記為 LOCKED，但文字被更動！")
            continue

        if d_item["status"] == "NEEDS_POLISH":
            sim = difflib.SequenceMatcher(None, d_item["text"], f_item["text"]).ratio()
            if sim >= LAZY_SIMILARITY_THRESHOLD:
                errors.append(f"[漏修/偷懶攔截] {loc} 標記為 NEEDS_POLISH，但原句照抄 (相似度 {sim:.0%})！")

        for key, vals in f_item.get("visual", {}).items():
            for v in vals:
                if v not in f_item["text"]:
                    errors.append(f"[視覺重音不存在] {loc} 註解 [{key}] 指定的「{v}」不在該區塊正文中")

        for ent in d_item["entities"]:
            if ent not in f_item["text"]:
                errors.append(f"[事實遺失] {loc} 遺失了鎖定實體或數據：`{ent}`")

        for raw_l in f_item["lines"]:
            if BOLD_PREFIX_PATTERN.match(raw_l):
                errors.append(f"[AI 排版違規] {loc} 使用了禁止的粗體摘要開頭 (**...：**)。")

        if d_item["status"] != "LOCKED":
            hit_banned = [t for t in DEFAULT_BANNED_TOKENS if t in f_item["text"]]
            if hit_banned:
                errors.append(f"[禁用詞違規] {loc} 觸犯文體黑名單：{', '.join(hit_banned)}")

            for label, txt in [("上游草稿", d_item["text"]), ("下游成品", f_item["text"])]:
                hit_chore = [t for t in CHORE_AND_HALLUCINATION_TOKENS if t in txt]
                if hit_chore:
                    errors.append(f"[流水帳/幻覺詞攔截] {loc} {label}出現已禁用之日常雜務或幻覺詞：{', '.join(hit_chore)}")

            for pat in OVERCLAIM_PATTERNS:
                fm = re.search(pat, f_item["text"])
                if fm and not re.search(pat, d_item["text"]):
                    errors.append(f"[責任升級] {loc} 成品出現「{fm.group(0)}」，上游草稿同一區塊沒有。")

            hit_resp = [t for t in RESPONSIBILITY_WARN_TOKENS if t in f_item["text"]]
            if hit_resp:
                warnings.append(f"[責任詞提示] {loc} 含「{'、'.join(hit_resp)}」（不影響通過）。")

            # 檢查是否有超過 32 字未切分的超長逗號子句（提示語感）
            clauses = re.split(r"[，,；;。｜|：:\n]", re.sub(r"（[^）]*）|\([^)]*\)", "", f_item["text"]))
            long_clauses = [c.strip() for c in clauses if len(c.strip()) > 32]
            if long_clauses:
                warnings.append(f"[長子句語感提示] {loc} 含超過 32 字未切分子句：「{long_clauses[0][:18]}...」（建議檢視節奏）。")

    return errors, warnings

def verify_104_markdown(md_104_path: str, final_text: str):
    """驗證 Stage 3 產出的 104.md 是否違反 v2.1.0 指南（假標籤、粗體前綴、巢狀 ul、空 li）"""
    p = pathlib.Path(md_104_path)
    if not p.exists():
        return [f"[104 驗證失敗] 找不到檔案：{md_104_path}"]
    text = p.read_text(encoding="utf-8")
    errs = []
    for bad_tag in FORBIDDEN_104_TAGS:
        if re.search(r"[^\x00-\x7F]", bad_tag):
            hit = bad_tag in text  # 含中文：\b 在中文相鄰時失靈，改用子字串
        else:
            hit = re.search(rf"(?<![A-Za-z0-9_]){re.escape(bad_tag)}(?![A-Za-z0-9_])", text) is not None
        if hit:
            errs.append(f"[104 假標籤違規] 104 檔案中出現禁止捏造之工具標籤：`{bad_tag}`")

    # 內文一致性：定稿每一句都必須原樣出現在 104.md 的 code block（剝除 HTML 後）
    blocks = re.findall(r"```(?:html|text)\n(.*?)```", text, re.S)
    plain = html.unescape(re.sub(r"<[^>]+>", "", "".join(blocks))).replace("\n", "").replace("　　・", "")
    section = ""
    for raw in re.sub(r"<!--.*?-->", "", final_text, flags=re.S).splitlines():
        s = raw.strip()
        if not s:
            continue
        if s.startswith("#"):
            section = s.lstrip("#").strip()
            continue
        t = re.sub(r"^-\s+", "", s).lstrip("▍").strip()
        if section == "專長" and "：" in t:
            t = t.split("：", 1)[1]  # 專長名稱進 name 欄，desc 只放冒號後內文
        if t and t not in plain:
            errs.append(f"[104 內文竄改] 定稿句子未原樣出現在 104 檔案（{section}）：「{t[:30]}…」")
    if re.search(r"<li>\s*<strong>[^<]+[：:]\s*</strong>", text):
        errs.append("[104 格式違規] <li> 開頭使用了禁止的 <strong>標題：</strong> 分類前綴！")
    if re.search(r"<li>\s*</?ul>", text) or re.search(r"<li[^>]*>[^<]*<ul>", text):
        errs.append("[104 Quill 縮排違規] 偵測到巢狀 <ul>，請改用扁平 <li class=\"ql-indent-1\">！")
    if "ql-indent" in "".join(re.findall(r"```html\n(.*?)```", text, re.S)):
        errs.append("[104 縮排違規] 104 不支援 ql-indent，子項請併入母項 <li> 並以 <br>　　・ 呈現！")
    if re.search(r"<li[^>]*>\s*</li>", text):
        errs.append("[104 空圓點違規] 偵測到空白的 <li></li>！")
    return errs

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--local-codex", action="store_true")
    parser.add_argument("--verify-104", type=str, default=None, help="額外驗證 104.md 檔案路徑")
    args = parser.parse_args()

    if args.local_codex:
        draft_text = load_file_content(DRAFT_REL_PATH, CLAUDE_BRANCH, prefer_local=False)
        final_text = load_file_content(FINAL_REL_PATH, CODEX_BRANCH, prefer_local=True)
    else:
        draft_text = load_file_content(DRAFT_REL_PATH, CLAUDE_BRANCH, prefer_local=True)
        final_text = load_file_content(FINAL_REL_PATH, CODEX_BRANCH, prefer_local=False)

    errors, warnings = run_verification(draft_text, final_text)
    if args.verify_104:
        errors.extend(verify_104_markdown(args.verify_104, final_text))

    if warnings:
        print(f"⚠️ 語感與責任詞提示 {len(warnings)} 項（不影響通過）：\n" + "\n".join(f"  - {w}" for w in warnings))
    if errors:
        print(f"❌ 驗收失敗！共發現 {len(errors)} 項違規：\n" + "\n".join(f"{i+1}. {e}" for i, e in enumerate(errors)))
        sys.exit(1)
    print(f"✅ GATEKEEPER PASSED: 全篇 {len(parse_tagged_blocks(final_text))} 個標記區塊（含反流水帳、未清括號與結構檢查）全數通過！")
    sys.exit(0)

if __name__ == "__main__":
    main()
