#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
from collections import Counter
import difflib
import html
from html.parser import HTMLParser
import json
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
    "刊案", "RBAC",
    "簡單舊案", "較易處理的舊案", "不再自動覆蓋", "安排代碼交工程更新", "擔任統一窗口", "業務票選",
    "新增、修改", "合併與刪除",
    "非功能上線比例", "不等同功能上線比例", "不予採納", "已有類似功能", "目的是",  # 免責小尾巴（2026-10-26）
    "破局者", "治理者", "先行者", "Credibility", "毛利",
    "共同招募的方式", "安全的驗證機制", "建立網頁付款管道",  # AI 硬湊贅詞（2026-10-26）  # 框架自嗨詞、無紀錄財務詞（2026-10-26）  # 分類治理寫成 CRUD 流水帳（2026-10-26）
    "Account Takeover", "權限模型", "舊系統遷移", "分類治理", "雙邊市場",  # 本人不懂的概念詞（2026-10-25）  # No Detail Dumping（2026-10-25 本人指定）                  # 內部行話，對外讀不懂（2026-10-24 本人）
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
BULLET_LENGTH_CAP = 165  # 工作經歷單一列點「主幹敘事淨字數」上限：剝除括號內統計期間後計算（2026-10-25 本人修訂，原 145 含括號）
BULLET_LENGTH_CAP_JUICY = 190
WORD_FREQ_CAPS = {  # 全篇高頻口癖詞上限（2026-10-26）
    "建立": (5, "[AI 口癖重複違規] 全篇「建立」出現達 {n} 次（上限 5 次）！請勿濫用「建立…的方式／機制」湊字，改用自然動詞（讓…能…、打通、規劃、推動）！"),
    "推進": (8, "[AI 口癖重複違規] 全篇「推進」出現達 {n} 次（上限 8 次）！請按語境改用上線、交付、完成、排定、說服等動詞。"),
    "救回": (1, "[戲劇化詞彙重複違規] 全篇「救回」出現達 {n} 次（上限 1 次，僅限工作經歷危機承接亮點使用，簡介、自傳與專案請用自然的「承接既有用戶與營收」）！"),
}
PAREN_LENGTH_CAP = 35  # 單一括號內中文字上限；產品英文名、日期、數字與符號不計（2026-10-26）
PAREN_CJK = re.compile(r"[\u4e00-\u9fff]")  # 含 Juicy 的兩次下架承接合併點放寬
PAREN_PATTERN = re.compile(r"（[^（）]*）|\([^()]*\)")
WORK_SECTION_PATTERN = re.compile(r"｜.*(?:迄今|\d{4}/\d{2})")

TAG_PATTERN = re.compile(r"<!--\s*\[STATUS:\s*(?P<status>[A-Z_]+)\](?P<attrs>(?:\s*\[[A-Z_]+:[^\]]*\])*)\s*-->")
ATTR_PATTERN = re.compile(r"\[(?P<key>[A-Z_]+):\s*(?P<val>[^\]]*)\]")
VISUAL_KEYS = ("G", "B", "BT")  # G＝金黃底色、B＝晴藍底色＋粗體、BT＝純粗體；值以 | 分隔

BOLD_PREFIX_PATTERN = re.compile(r"^\s*[-*]\s+\*\*[^*]+[：:]\*\*")

# Reviewed 104 metadata: tags have fact support; Scrum refers to 2022–2023 only.
LAYOUT = {
    "target_block": "layout",
    "action": "update_theme",
    "requires_confirmation": True,
    "theme_suggestion": "chronological",
    "skill_display": "SkillThemeCard",
    "accent_color": "#566876",
    "notes": "Senior PM／PO 定位：經歷時序式、專長卡片式、名片主題用沉穩商務色（煙燻冷藍）。版型變更須本人確認後才套用。",
}
LF = ["companyName", "jobName", "duration", "workArea", "management"]
ET = [["製作規格說明書", "Prototype", "Systems Analysis", "專案溝通╱整合管理", "生成式AI", "推薦系統", "工作任務╱業績項目分配", "客訴案件處理"],
      ["市場調查企劃與執行", "產品策略", "產品營運", "數據分析", "專案時間╱進度控管", "Electronic Payment", "iOS", "Android"],
      ["專案溝通╱整合管理", "數據分析", "Electronic Payment", "Android"], []]
ST = [["Claude", "生成式AI", "AI"], ["製作規格說明書", "Prototype", "功能測試(function test)", "專案規劃執行╱範圍管理"],
      ["Systems Analysis", "UML", "系統整合分析"],
      ["Figma", "Axure RP", "Wireframe", "Prototype", "使用者介面設計", "使用者體驗設計", "iOS", "Android"],
      ["專案溝通╱整合管理", "專案時間╱進度控管", "Scrum", "決策能力"],
      ["產品策略", "產品營運", "數據分析", "Electronic Payment", "iOS", "Android"]]
MG = ['**有管理責任，1~5 人**（直屬 2 名產品企劃）', '**無管理責任**', '**無管理責任**', '**無管理責任**']
IMG = ['images/project1_justdating_juicy.png', 'images/project2_kool.png',
       'images/project3_1111_recruit.png', 'images/project4_1111_recruit.png']
PDATE = ['2020/01 – 2020/06｜isInProgress：否', '2018/05 – 2022/03｜isInProgress：否',
         '2024/12 – ｜isInProgress：**是**', '2025/03 – 2025/09｜isInProgress：否（104 只收年月）']


def read_from_git(branch_ref: str, rel_path: str):
    res = subprocess.run(
        ["git", "show", f"{branch_ref}:{rel_path}"],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding="utf-8"
    )
    if res.returncode:
        raise ValueError(f"無法讀取指定 Git 來源：{branch_ref}:{rel_path}")
    if not res.stdout.strip():
        raise ValueError(f"Git 來源為空：{branch_ref}:{rel_path}")
    return res.stdout

def load_file_content(rel_path: str, target_branch: str, prefer_local: bool = False) -> str:
    local_path = pathlib.Path(rel_path)
    if prefer_local:
        content = local_path.read_text(encoding="utf-8")
        if not content.strip():
            raise ValueError(f"本地來源為空：{rel_path}")
        return content
    return read_from_git(target_branch, rel_path)


def resume_body(text):
    """Only the explicitly marked draft body is handed to Codex, not its appendices."""
    match = re.search(r"^## 草稿\s*\n(.*?)(?=^## |\Z)", text, re.M | re.S)
    return match.group(1) if match else text


def document_checks(text, label, allowed_statuses):
    errors, headings, outside = [], [], []
    active = False
    for no, line in enumerate(resume_body(text).splitlines(), 1):
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("#"):
            headings.append(stripped)
            active = False
        elif re.search(r"\[\s*STATUS\b", stripped):
            match = TAG_PATTERN.fullmatch(stripped)
            if not match or match.group("status") not in allowed_statuses:
                errors.append(f"[非法狀態] {label} 第 {no} 行標記格式或狀態不合法")
            active = bool(match)
        elif stripped.startswith("<!--") and stripped.endswith("-->"):
            continue
        elif not active:
            outside.append(no)
    if outside:
        errors.append(f"[未標記正文] {label} 標記外有正文，行：{outside}")
    return errors, headings


def numeric_values(text):
    return Counter(re.findall(r"\d+(?:[.,]\d+)*", text))


def bullet_shape(block):
    return [(bool(m.group(1)), m.group(2))
            for line in block["lines"]
            if (m := re.match(r"^(\s*)([-*]|\d+[.)])\s+", line))]


def bullet_tree(blocks):
    """Compare parent relationships; two/four-space child styles may be equivalent."""
    stack, tree, section = [], [], None
    for block in blocks:
        if section != block["section"]:
            stack, section = [], block["section"]
        for line in block["lines"]:
            match = re.match(r"^(\s*)([-*]|\d+[.)])\s+", line)
            if not match:
                continue
            indent = len(match.group(1).expandtabs(4))
            while stack and indent <= stack[-1][0]:
                stack.pop()
            tree.append((stack[-1][1] if stack else None, match.group(2)))
            stack.append((indent, len(tree) - 1))
    return tree

def parse_tagged_blocks(md_text: str):
    blocks = []
    current_section = "Header"
    active_block = None

    for idx, line in enumerate(resume_body(md_text).splitlines(), start=1):
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
            amplify = [v.strip() for v in re.split(r"[,，|]", attrs.get("AMPLIFY", "")) if v.strip()]  # 上游授權的強勢責任詞（2026-10-26）
            visual = {k: [v.strip() for v in attrs[k].split("|") if v.strip()] for k in VISUAL_KEYS if k in attrs}
            active_block = {
                "line_no": idx + 1,
                "status": status,
                "entities": entities,
                "amplify": amplify,
                "visual": visual,
                "section": current_section,
                "lines": [],
                "raw_lines": []
            }
            continue

        if active_block is not None:
            active_block["raw_lines"].append(line)
        if active_block is not None and stripped and not stripped.startswith("<!--"):
            active_block["lines"].append(line)

    if active_block is not None:
        blocks.append(active_block)

    for b in blocks:
        b["text"] = "\n".join(l.strip() for l in b["lines"])
    return blocks

def bullet_length_violations(blocks, label):
    """工作經歷中非母項、非子項的單一列點，剝除括號後的淨字數超過上限即違規。"""
    out = []
    for i, b in enumerate(blocks):
        if not WORK_SECTION_PATTERN.search(b["section"]) or not b["lines"]:
            continue
        first = b["lines"][0]
        if not first.lstrip().startswith("- ") or first.startswith((" ", "\t")):
            continue  # 非列點或子項
        nxt = blocks[i + 1] if i + 1 < len(blocks) else None
        if nxt and nxt["lines"] and nxt["lines"][0].startswith((" ", "\t")) and nxt["section"] == b["section"]:
            continue  # 母項
        net = PAREN_PATTERN.sub("", b["text"].lstrip("- "))
        n = len(re.sub(r"\s", "", net))
        cap = BULLET_LENGTH_CAP_JUICY if "Juicy" in b["text"] else BULLET_LENGTH_CAP
        if n > cap:
            out.append((i, n, label, cap))
    return out

def run_verification(draft_text: str, final_text: str):
    errors = []
    warnings = []
    if re.search(r"^## 草稿\s*$", final_text, re.M):
        errors.append("[成品結構] 成品不得使用上游草稿包裝隱藏章節外文字")
    for label, text, states in (("上游草稿", draft_text, {"NEEDS_POLISH", "LOCKED"}),
                                 ("下游成品", final_text, {"POLISHED", "LOCKED"})):
        if not text.strip():
            errors.append(f"[空輸入] {label} 不得為空")
        structural, headings = document_checks(text, label, states)
        errors.extend(structural)
        if label == "上游草稿":
            draft_headings = headings
        elif headings != draft_headings:
            errors.append("[章節異動] 章節或公司標題、層級、順序與上游不同")
    for idx, line in enumerate(final_text.splitlines(), start=1):
        if "NEEDS_POLISH" in line:
            errors.append(f"[殘留標記錯誤] final_resume.md 第 {idx} 行仍殘留 NEEDS_POLISH 標記。")

    draft_blocks = parse_tagged_blocks(draft_text)
    final_blocks = parse_tagged_blocks(final_text)
    if not draft_blocks or not final_blocks:
        errors.append("[零區塊] 上游與成品皆須有非零標記區塊")
    if bullet_tree(draft_blocks) != bullet_tree(final_blocks):
        errors.append("[父子結構] 全文列點順序或父子關係改變")
    for label, blocks in (("上游草稿", draft_blocks), ("下游成品", final_blocks)):
        if any(not b["lines"] for b in blocks):
            errors.append(f"[空區塊] {label} 有標記但沒有正文")

    if len(draft_blocks) != len(final_blocks):
        errors.append(
            f"[結構不對稱] 上游草稿有 {len(draft_blocks)} 個標記區塊，下游成品有 {len(final_blocks)} 個。"
            "請確認每個區塊上方皆保留 <!-- [STATUS: POLISHED/LOCKED] --> 標記！"
        )

    for label, blocks in (("上游草稿", draft_blocks), ("下游成品", final_blocks)):
        body = "\n".join(b["text"] for b in blocks)
        for word, (cap, msg) in WORD_FREQ_CAPS.items():
            n = body.count(word)
            if n > cap:
                errors.append(f"{label}：" + msg.format(n=n))

    for label, blocks in (("上游草稿", draft_blocks), ("下游成品", final_blocks)):
        for bi, b in enumerate(blocks):
            for m in PAREN_PATTERN.finditer(b["text"]):
                n = len(PAREN_CJK.findall(m.group(0)[1:-1]))
                if n > PAREN_LENGTH_CAP:
                    errors.append(f"[括號塞爆/免責違規] 區塊 #{bi+1} ({b['section']}) {label}單一括號內達 {n} 字（只計中文字；上限 {PAREN_LENGTH_CAP} 字），嚴禁在括號內塞入內部報表定義或免責備註！")

    for bi, n, label, cap in bullet_length_violations(draft_blocks, "上游草稿") + bullet_length_violations(final_blocks, "下游成品"):
        src = draft_blocks if label == "上游草稿" else final_blocks
        errors.append(f"[篇幅膨脹違規] 區塊 #{bi+1} ({src[bi]['section']}) {label}單點主幹敘事淨字數達 {n} 字（不含括號；上限 {cap} 字），請刪除內部作業細節與規格瑣事，僅保留核心產品判斷與功績！")

    for i in range(min(len(draft_blocks), len(final_blocks))):
        d_item, f_item = draft_blocks[i], final_blocks[i]
        loc = f"區塊 #{i+1} ({d_item['section']} | 成品第 {f_item['line_no']} 行)"
        expected_status = "LOCKED" if d_item["status"] == "LOCKED" else "POLISHED"
        if f_item["status"] != expected_status:
            errors.append(f"[狀態轉換] {loc} 應為 {expected_status}")
        if d_item["section"] != f_item["section"]:
            errors.append(f"[區塊位置] {loc} 所屬章節不同")
        if bullet_shape(d_item) != bullet_shape(f_item):
            errors.append(f"[父子結構] {loc} 列點數量、符號或縮排改變")
        if numeric_values(d_item["text"]) != numeric_values(f_item["text"]):
            errors.append(f"[數字異動] {loc} 數字或出現次數與上游不同")

        # 檢查上游或下游是否殘留未解決的〔待確認/待補〕括號
        for label, txt in [("上游草稿", d_item["text"]), ("下游成品", f_item["text"])]:
            m_br = UNRESOLVED_BRACKET_PATTERN.search(txt)
            if m_br:
                errors.append(f"[未清內部括號] {loc} {label}殘留未確認標記：`{m_br.group(0)}`")

        if d_item["status"] == "LOCKED" and (
            "\n".join(d_item["raw_lines"]).strip("\n") !=
            "\n".join(f_item["raw_lines"]).strip("\n")
        ):
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
                if fm and not re.search(pat, d_item["text"]) and fm.group(0) not in d_item.get("amplify", []):
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

class FieldHTML(HTMLParser):
    """Recover ordered paragraphs/items, preserving repeated text and inline spacing."""
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.chunks = []
        self.current = []

    def flush(self):
        value = "".join(self.current).strip()
        if value:
            self.chunks.append(value)
        self.current = []

    def handle_starttag(self, tag, attrs):
        if tag not in {"p", "li", "ul", "blockquote", "br", "span", "strong"}:
            raise ValueError("104 不允許的 HTML 標籤：" + tag)
        if any(name not in {"style", "class"} for name, _ in attrs):
            raise ValueError("104 不允許的 HTML 屬性")
        if tag in {"p", "li", "blockquote", "br"}:
            self.flush()

    def handle_endtag(self, tag):
        if tag in {"p", "li", "blockquote"}:
            self.flush()

    def handle_data(self, data):
        if self.current or data.strip():
            self.current.append(data)


def visible_lines(payload, mode):
    if mode == "quill_html":
        parser = FieldHTML()
        parser.feed(payload)
        parser.close()
        parser.flush()
        return parser.chunks
    return [line.strip() for line in payload.splitlines() if line.strip()]


def source_sections(text):
    """Read source headings independently of the renderer, rejecting unknown structure."""
    clean = re.sub(r"<!--.*?-->", "", resume_body(text), flags=re.S)
    sections, section, subsection = {}, None, None
    for raw in clean.splitlines():
        line = raw.strip()
        if not line:
            continue
        if line.startswith("### "):
            section = line[4:]
            if section in sections:
                raise ValueError("重複來源章節：" + section)
            sections[section] = {"lines": [], "parts": []}
            subsection = None
        elif line.startswith("#### ") and section:
            subsection = {"name": line[5:], "lines": []}
            sections[section]["parts"].append(subsection)
        elif line.startswith("#") or section is None:
            raise ValueError("104 來源含未知標題或章節外正文")
        else:
            value = re.sub(r"^[-*]\s+", "", line).lstrip("▍")
            (subsection["lines"] if subsection is not None else sections[section]["lines"]).append(value)
    required = ["個人簡介", "個人特色", "工作經歷", "專長", "自傳", "專案成就", "求職條件（工作內容）"]
    if list(sections) != required:
        raise ValueError("104 來源章節缺漏、順序錯誤或出現未知章節")
    if len(sections["工作經歷"]["parts"]) != len(ET) or len(sections["專案成就"]["parts"]) != len(IMG):
        raise ValueError("104 來源經歷或專案數量與核可結構不同")
    if len(sections["專長"]["lines"]) != len(ST):
        raise ValueError("104 來源專長數量與核可結構不同")
    return sections


def expected_104_fields(final_text, public=False):
    sections = source_sections(final_text)
    fields = [(LAYOUT.copy(), [])]
    fields.append(({"target_block": "info", "action": "replace_field", "field": "bio", "mode": "plain_text"}, sections["個人簡介"]["lines"]))
    fields.append(({"target_block": "info", "action": "replace_field", "field": "trait", "mode": "plain_text"}, sections["個人特色"]["lines"]))
    for i, part in enumerate(sections["工作經歷"]["parts"]):
        fields.append(({"target_block": "experience", "index": i, "action": "replace_description", "mode": "quill_html", "tags": ET[i], "locked_fields": LF}, part["lines"]))
    for i, line in enumerate(sections["專長"]["lines"]):
        if "：" not in line:
            raise ValueError("專長缺名稱分隔符號")
        name, desc = line.split("：", 1)
        fields.append(({"target_block": "skill", "index": i, "action": "replace_all", "mode": "plain_text", "name": name, "tags": skill_tags(i, desc)}, [desc]))
    fields.append(({"target_block": "bio", "action": "replace_field", "field": "chi", "mode": "quill_html"}, sections["自傳"]["lines"]))
    for i, part in enumerate(sections["專案成就"]["parts"]):
        name = part["name"].split("｜")[0]
        directive = {"target_block": "project", "index": i, "action": "replace_all", "mode": "quill_html", "name": name}
        if public and i >= 2:
            directive.update(image_action="remove")
        else:
            directive.update(media_type="上傳圖片或影片", image=IMG[i], image_action="upload_replace")
        fields.append((directive, part["lines"]))
    fields.append(({"target_block": "jobCondition", "action": "replace_field", "field": "preferJobContent", "mode": "plain_text", "locked_fields": ["preferJobTitle", "salary", "workArea", "onboardDate", "remoteWork"]}, sections["求職條件（工作內容）"]["lines"]))
    return fields


def skill_tags(index, description):
    # Scrum is supported as historical experience in library, but a tag must also
    # have evidence in this final skill card. Do not silently add it to a card
    # that only describes the current Kanban/coordination workflow.
    return [tag for tag in ST[index] if tag != "Scrum" or "Scrum" in description]


def unique_json(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("重複 directive key：" + key)
        result[key] = value
    return result


def verify_104_fields(text, final_text, public=False):
    errors = []
    try:
        expected = expected_104_fields(final_text, public)
        sections = source_sections(final_text)
        headings = ["## 0. 全站版型（需本人確認後才套用）", "## 1. 個人簡介",
                    "### 1.1 個人特色（五個分開輸入，依序；LOCKED）", "## 2. 工作經歷"]
        headings += [f"### 2.{i+1} {part['name']}" for i, part in enumerate(sections["工作經歷"]["parts"])]
        headings += ["## 3. 專長（6 筆，順序與標題鎖定；desc 純文字）"]
        headings += [f"### 3.{i+1} {line.split('：', 1)[0]}" for i, line in enumerate(sections["專長"]["lines"])]
        headings += ["## 4. 自傳", "## 5. 專案成就"]
        headings += [f"### 5.{i+1} {part['name'].split('｜')[0]}" for i, part in enumerate(sections["專案成就"]["parts"])]
        headings += ["## 6. 求職條件（工作內容，純文字；其餘求職條件欄位不動）"]
        outside_fences = re.sub(r"```.*?```", "", text, flags=re.S)
        if re.findall(r"^#{2,3} .+$", outside_fences, re.M) != headings:
            errors.append("[104 欄位標題] 欄位標題、公司名稱或順序與來源不同")
        matches = list(re.finditer(r"<!--\s*@104-directive\s*\n(.*?)-->", text, re.S))
        if len(matches) != len(expected):
            errors.append("[104 欄位結構] directive 數量與來源不符")
        prefix = text[:matches[0].start()] if matches else text
        if "```" in prefix:
            errors.append("[104 未歸屬內容] directive 前有未歸屬的 code block")
        for i, match in enumerate(matches):
            directive = json.loads(match.group(1), object_pairs_hook=unique_json)
            end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
            segment = text[match.end():end]
            fences = list(re.finditer(r"```(html|text)\n(.*?)```", segment, re.S))
            if i >= len(expected):
                continue
            policy, source_lines = expected[i]
            if json.dumps(directive, sort_keys=True, ensure_ascii=False) != json.dumps(policy, sort_keys=True, ensure_ascii=False):
                errors.append(f"[104 directive 異動] 欄位 #{i+1} 的名稱、標籤、順序或指令內容不符")
            expected_count = 0 if policy["target_block"] == "layout" else 1
            if len(fences) != expected_count or segment.count("```") != 2 * expected_count:
                errors.append(f"[104 欄位結構] 欄位 #{i+1} 的 code block 數量不符")
                continue
            if not fences:
                continue
            mode = policy["mode"]
            if fences[0].group(1) != ("html" if mode == "quill_html" else "text"):
                errors.append(f"[104 欄位格式] 欄位 #{i+1} 的 code block 類型不符")
            if visible_lines(fences[0].group(2), mode) != source_lines:
                errors.append(f"[104 欄位內文] 欄位 #{i+1} 內容、順序或重複次數與來源不同")
    except (ValueError, TypeError, KeyError) as exc:
        errors.append("[104 結構錯誤] " + str(exc))
    return errors


def verify_104_markdown(md_104_path: str, final_text: str, public=False):
    """驗證 Stage 3 產出的 104.md 是否違反 v2.1.0 指南（假標籤、粗體前綴、巢狀 ul、空 li）"""
    p = pathlib.Path(md_104_path)
    if not p.exists():
        return [f"[104 驗證失敗] 找不到檔案：{md_104_path}"]
    text = p.read_text(encoding="utf-8")
    errs = verify_104_fields(text, final_text, public)
    for bad_tag in FORBIDDEN_104_TAGS:
        if re.search(r"[^\x00-\x7F]", bad_tag):
            hit = bad_tag in text  # 含中文：\b 在中文相鄰時失靈，改用子字串
        else:
            hit = re.search(rf"(?<![A-Za-z0-9_]){re.escape(bad_tag)}(?![A-Za-z0-9_])", text) is not None
        if hit:
            errs.append(f"[104 假標籤違規] 104 檔案中出現禁止捏造之工具標籤：`{bad_tag}`")

    # 內文一致性：定稿每一句都必須原樣出現在 104.md 的 code block（剝除 HTML 後）
    blocks = re.findall(r"```(?:html|text)\n(.*?)```", text, re.S)
    plain = html.unescape(re.sub(r"<[^>]+>", "", "".join(blocks))).replace("\n", "")
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
        errs.append("[104 Quill 縮排違規] 偵測到巢狀 <ul>，請改用扁平 <li style=\"margin-left: 1em;\">！")
    if "ql-indent" in "".join(re.findall(r"```html\n(.*?)```", text, re.S)):
        errs.append("[104 縮排違規] 104 不支援 ql-indent，子項請用 <li style=\"margin-left: 1em;\">（v2.3.0）！")
    if re.search(r"<li[^>]*>\s*</li>", text):
        errs.append("[104 空圓點違規] 偵測到空白的 <li></li>！")
    return errs

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--local-codex", action="store_true")
    parser.add_argument("--verify-104", type=str, default=None, help="額外驗證 104.md 檔案路徑")
    parser.add_argument("--public", action="store_true", help="驗證已去識別的公開版 104（先驗收原始定稿）")
    args = parser.parse_args()

    if args.local_codex:
        draft_text = load_file_content(DRAFT_REL_PATH, CLAUDE_BRANCH, prefer_local=False)
        final_text = load_file_content(FINAL_REL_PATH, CODEX_BRANCH, prefer_local=True)
    else:
        draft_text = load_file_content(DRAFT_REL_PATH, CLAUDE_BRANCH, prefer_local=True)
        final_text = load_file_content(FINAL_REL_PATH, CODEX_BRANCH, prefer_local=False)

    errors, warnings = run_verification(draft_text, final_text)
    if args.verify_104:
        if args.public:
            from public_redact import redact
            public_source = redact(final_text)
        else:
            public_source = final_text
        errors.extend(verify_104_markdown(args.verify_104, public_source, args.public))

    if warnings:
        print(f"⚠️ 語感與責任詞提示 {len(warnings)} 項（不影響通過）：\n" + "\n".join(f"  - {w}" for w in warnings))
    if errors:
        print(f"❌ 驗收失敗！共發現 {len(errors)} 項違規：\n" + "\n".join(f"{i+1}. {e}" for i, e in enumerate(errors)))
        sys.exit(1)
    print(f"✅ GATEKEEPER PASSED: 全篇 {len(parse_tagged_blocks(final_text))} 個標記區塊（含反流水帳、未清括號與結構檢查）全數通過！")
    sys.exit(0)

if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError) as exc:
        print(f"❌ [FATAL] {exc}", file=sys.stderr)
        sys.exit(2)

