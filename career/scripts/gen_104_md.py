#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""由 Codex 定稿 final_resume.md 產生 104 特化版 md。

視覺重音不再寫死：讀取每個區塊註解中的 [G: ...]（金黃底色）、[B: ...]（晴藍底色＋粗體）、
[BT: ...]（純粗體），值以 | 分隔。未標註的區塊不加任何重音（並在 stderr 提示）。

用法：python3 gen_104_md.py <final_resume.md> <輸出 104.md> <版本> <來源說明>
"""
import json
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import verify_polish as vp  # noqa: E402

GS = '<span style="background-color: #fbf3db;">{}</span>'
BS = '<strong><span style="background-color: #deebf1;">{}</span></strong>'
HEAD = '<p><span class="ql-size-large" style="color: #00afb8;"><strong>{}</strong></span></p>'
CHILD = '<br>　　・'
PLAIN_SECTIONS = {"個人簡介", "專長", "求職條件（工作內容）"}  # 104 純文字欄位，不套重音

# ---- 結構設定（非內文，不經 Codex） ----
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


def bold_first(text, term):
    """在 HTML 標籤外、且不在既有 <strong> 內，粗體 term 的第一次出現。"""
    parts = re.split(r"(<[^>]+>)", text)
    depth = 0
    for k, p in enumerate(parts):
        if p.startswith("<"):
            if p.startswith("<strong"):
                depth += 1
            elif p.startswith("</strong"):
                depth -= 1
            continue
        if depth == 0 and term in p:
            parts[k] = p.replace(term, f"<strong>{term}</strong>", 1)
            return "".join(parts), True
    return text, False


def wrap_first(text, term, tpl):
    parts = re.split(r"(<[^>]+>)", text)
    for k, p in enumerate(parts):
        if not p.startswith("<") and term in p:
            parts[k] = p.replace(term, tpl.format(term), 1)
            return "".join(parts), True
    return text, False


class Decorator:
    """一個區塊的視覺重音：G、B 每個字串只套一次（跨段落），BT 每段落各套一次。"""

    def __init__(self, visual):
        self.g = list(visual.get("G", []))
        self.b = list(visual.get("B", []))
        self.bt = list(visual.get("BT", []))

    def __call__(self, text):
        for lst, tpl in ((self.g, GS), (self.b, BS)):
            for term in list(lst):
                text, ok = wrap_first(text, term, tpl)
                if ok:
                    lst.remove(term)
        for term in self.bt:
            text, _ = bold_first(text, term)
        return text


def body_key(line):
    return re.sub(r"^\s*-\s+", "", line).strip().lstrip("▍")


def build_visual_map(src):
    """正文行 → 所屬區塊的 Decorator（同一區塊的行共用同一個 Decorator）。"""
    m = {}
    missing = []
    for b in vp.parse_tagged_blocks(src):
        dec = Decorator(b.get("visual", {}))
        if not b.get("visual") and b["status"] != "LOCKED" and b["section"] not in PLAIN_SECTIONS:
            missing.append(b["section"])
        for ln in b["lines"]:
            m[body_key(ln)] = dec
    return m, missing


def sec(src, title):
    m = re.search(r"^### " + re.escape(title) + r"\n(.*?)(?=^### |\Z)", src, re.S | re.M)
    return m.group(1)


def clean(t):
    return [l for l in t.splitlines() if l.strip() and not l.strip().startswith("<!--")]


def deco(vmap, line):
    t = body_key(line)
    d = vmap.get(t)
    return d(t) if d else t


def exp_html(lines, vmap):
    out, ul, first = [], False, True
    for l in lines:
        child = l.startswith("    -")
        raw = body_key(l)
        if l.strip().startswith("▍"):
            if ul:
                out.append("</ul>")
                ul = False
            out.append(HEAD.format(raw))
            continue
        t = deco(vmap, l)
        if first:
            out.append(f"<blockquote>{t}</blockquote>")
            first = False
            continue
        if child:
            out[-1] = out[-1][:-5] + f"{CHILD}{t}</li>"
            continue
        if not ul:
            out.append("<ul>")
            ul = True
        out.append(f"<li>{t}</li>")
    if ul:
        out.append("</ul>")
    return "\n".join(out)


def d(o):
    return "<!-- @104-directive\n" + json.dumps(o, ensure_ascii=False) + "\n-->"


def main():
    src_path, out_path, ver, origin = sys.argv[1:5]
    public = "--public" in sys.argv[5:]
    imgs = [IMG[0], IMG[1], None, None] if public else IMG
    src = pathlib.Path(src_path).read_text(encoding="utf-8")
    vmap, missing = build_visual_map(src)
    if missing:
        print("⚠️ 以下區塊沒有視覺重音標註（不加底色／粗體）：" + "、".join(missing), file=sys.stderr)

    exp = sec(src, "工作經歷")
    heads = re.findall(r"^#### (.*)$", exp, re.M)
    parts = re.split(r"^#### .*$", exp, flags=re.M)[1:]
    exps = [exp_html(clean(p), vmap) if i < 3 else "<p>" + body_key(clean(p)[0]) + "</p>" for i, p in enumerate(parts)]
    skills = [body_key(l) for l in clean(sec(src, "專長"))]
    bio = [deco(vmap, p) for p in clean(sec(src, "自傳"))]
    praw = sec(src, "專案成就")
    ph = re.findall(r"^#### (.*)$", praw, re.M)
    pp = re.split(r"^#### .*$", praw, flags=re.M)[1:]
    projs = []
    for p in pp:
        ls = [deco(vmap, x) for x in clean(p)]
        projs.append("<blockquote>" + ls[0] + "</blockquote>\n" + "\n".join(f"<p>{x}</p>" for x in ls[1:]))
    job = "\n".join(clean(sec(src, "求職條件（工作內容）")))

    o = ["<!--markdownlint-disable MD013 MD033-->", "",
         f"# 104 特化版｜{ver}｜**可填表**（verify_polish.py 通過）", "",
         f"> 來源：{origin}。",
         "> 排版依 `career/104/styling-directive-guide.md` v2.2.0：子項併入母項（`<br>　　・`，不用 `ql-indent-1`）、模組大標、"
         "金黃＝成果數字、晴藍＋粗體＝核心產品／系統、粗體＝專案／系統／產品／buzzword。**底色與粗體依 Codex 在定稿註解標的 [G]／[B]／[BT]**；內文逐字取自定稿，只加容器。",
         "> **專案圖片**：本檔與 `images/` 資料夾一起打包；每個專案的 directive 以 `image` 指定相對路徑：5.1→project1_justdating_juicy.png、5.2→project2_kool.png、5.3→project3_1111_recruit.png、5.4→project4_1111_recruit.png。",
         "> 標籤只用 `career/104/tool_categories.md`／`skill_categories.md` 清單內名稱，找不到就略過。", "", "---", "",
         "## 0. 全站版型（需本人確認後才套用）", "", d(LAYOUT), "", "---", "",
         "## 1. 個人簡介", "", d({"target_block": "info", "action": "replace_field", "field": "bio", "mode": "plain_text"}), "",
         "```text", "\n".join(clean(sec(src, "個人簡介"))), "```", "",
         "### 1.1 個人特色（五個分開輸入，依序；LOCKED）", "",
         d({"target_block": "info", "action": "replace_field", "field": "trait", "mode": "plain_text"}), "",
         "```text", "\n".join(clean(sec(src, "個人特色"))), "```", "", "---", "", "## 2. 工作經歷", ""]
    for i, (h, html_) in enumerate(zip(heads, exps)):
        if public and i == 0:
            o += ["▼ 公開版：公司名稱設為 104「公司名暫不公開」（不可出現 1111、全球華人）", ""]
        o += [f"### 2.{i+1} {h}", "", f"▼ management：{MG[i]}", "",
              d({"target_block": "experience", "index": i, "action": "replace_description", "mode": "quill_html", "tags": ET[i], "locked_fields": LF}),
              "", "```html", html_, "```", ""]
    o += ["---", "", "## 3. 專長（6 筆，順序與標題鎖定；desc 純文字）", ""]
    for i, s in enumerate(skills):
        n, desc = s.split("：", 1)
        o += [f"### 3.{i+1} {n}", "", d({"target_block": "skill", "index": i, "action": "replace_all", "mode": "plain_text", "name": n, "tags": ST[i]}),
              "", "```text", desc, "```", ""]
    o += ["---", "", "## 4. 自傳", "", d({"target_block": "bio", "action": "replace_field", "field": "chi", "mode": "quill_html"}), "",
          "```html", "\n<p><br></p>\n".join(f"<p>{p}</p>" for p in bio), "```", "", "---", "", "## 5. 專案成就", ""]
    for i, (h, html_) in enumerate(zip(ph, projs)):
        n = h.split("｜")[0]
        img_line = (f"- 圖片：`{imgs[i]}`（104「專案素材」選「上傳圖片或影片」，把此檔上傳到「素材檔」；每個專案只放這一張）"
                    if imgs[i] else "- 圖片：**無**（公開版刪除此專案的圖片，素材欄留空）")
        pd = {"target_block": "project", "index": i, "action": "replace_all", "mode": "quill_html", "name": n}
        pd.update({"media_type": "上傳圖片或影片", "image": imgs[i], "image_action": "upload_replace"} if imgs[i] else {"image_action": "remove"})
        o += [f"### 5.{i+1} {n}", "", f"- 起訖：{PDATE[i]}｜url：留空", img_line, "", d(pd),
              "", "```html", html_, "```", ""]
    o += ["---", "", "## 6. 求職條件（工作內容，純文字；其餘求職條件欄位不動）", "",
          d({"target_block": "jobCondition", "action": "replace_field", "field": "preferJobContent", "mode": "plain_text",
             "locked_fields": ["preferJobTitle", "salary", "workArea", "onboardDate", "remoteWork"]}),
          "", "```text", job, "```", ""]
    if public:
        o = [x.replace("5.3→project3_1111_recruit.png、5.4→project4_1111_recruit.png", "5.3、5.4 公開版不放圖片") for x in o]
    pathlib.Path(out_path).write_text("\n".join(o) + "\n", encoding="utf-8")

    errs = vp.verify_104_markdown(out_path, src)
    if errs:
        print("❌ 產出驗證失敗：\n" + "\n".join(errs))
        sys.exit(1)
    print(f"✅ 產出 {out_path}；--verify-104 通過")


if __name__ == "__main__":
    main()
