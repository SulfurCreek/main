#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""由 Codex 定稿 final_resume.md 產生 104 特化版 md。

視覺重音不再寫死：讀取每個區塊註解中的 [G: ...]（金黃底色）、[B: ...]（晴藍底色＋粗體）、
[BT: ...]（純粗體），值以 | 分隔。未標註的區塊不加任何重音（並在 stderr 提示）。

用法：python3 gen_104_md.py <final_resume.md> <輸出 104.md> <版本> <來源說明>
"""
import argparse
import html
import json
import os
import pathlib
import re
import sys
import tempfile

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import verify_polish as vp  # noqa: E402

GS = '<span style="background-color: #fbf3db;">{}</span>'
BS = '<strong><span style="background-color: #deebf1;">{}</span></strong>'
HEAD = '<p><span class="ql-size-large" style="color: #00afb8;"><strong>{}</strong></span></p>'
CHILD = '<li style="margin-left: 1em;">{}</li>'  # 子項＝獨立 li＋左縮排（v2.3.0，104 實測可渲染）
GAP = '<p><br></p>'  # 模組大標上下留白（Quill 空行）
PLAIN_SECTIONS = {"個人簡介", "專長", "求職條件（工作內容）"}  # 104 純文字欄位，不套重音

# ---- 結構設定（非內文，不經 Codex） ----
# Metadata is reviewed once in the verifier and used by the renderer unchanged.
LAYOUT, LF, ET, ST, MG, IMG, PDATE = (vp.LAYOUT, vp.LF, vp.ET, vp.ST, vp.MG, vp.IMG, vp.PDATE)


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
        self.g = [html.escape(t, quote=False) for t in visual.get("G", [])]
        self.b = [html.escape(t, quote=False) for t in visual.get("B", [])]
        self.bt = [html.escape(t, quote=False) for t in visual.get("BT", [])]

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
    if not m:
        raise ValueError("找不到符合管線格式的來源章節：" + title)
    return m.group(1)


def clean(t):
    return [l for l in t.splitlines() if l.strip() and not l.strip().startswith("<!--")]


def deco(vmap, line):
    t = body_key(line)
    d = vmap.get(t)
    escaped = html.escape(t, quote=False)
    return d(escaped) if d else escaped


def exp_html(lines, vmap):
    out, ul, first = [], False, True
    for l in lines:
        child = l.startswith("    -")
        raw = body_key(l)
        if l.strip().startswith("▍"):
            if ul:
                out.append("</ul>")
                ul = False
            if out and out[-1] != GAP:
                out.append(GAP)
            out.append(HEAD.format(html.escape(raw, quote=False)))
            out.append(GAP)
            continue
        t = deco(vmap, l)
        if first:
            out.append(f"<blockquote>{t}</blockquote>")
            first = False
            continue
        if child:
            out.append(CHILD.format(t))
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
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source")
    parser.add_argument("output")
    parser.add_argument("version")
    parser.add_argument("origin")
    parser.add_argument("--public", action="store_true", help="驗收原始定稿後去識別並產生公開版")
    parser.add_argument("--draft", help="明確指定上游草稿快照；未指定則讀本地管線草稿")
    args = parser.parse_args()
    src_path, out_path, ver, origin = args.source, args.output, args.version, args.origin
    public = args.public
    if pathlib.Path(src_path).resolve() == pathlib.Path(out_path).resolve():
        raise ValueError("輸出不可覆蓋來源定稿")
    imgs = [IMG[0], IMG[1], None, None] if public else IMG
    src = pathlib.Path(src_path).read_text(encoding="utf-8")
    draft = (pathlib.Path(args.draft).read_text(encoding="utf-8") if args.draft else
             vp.load_file_content(vp.DRAFT_REL_PATH, vp.CLAUDE_BRANCH, prefer_local=True))
    if public:
        from public_redact import redact
        # Accept the established pre-redacted input only if it exactly matches the
        # current remote final; never validate a public derivative against itself.
        if "公司名暫不公開" in src:
            original = vp.load_file_content(vp.FINAL_REL_PATH, vp.CODEX_BRANCH)
            if redact(original) != src:
                raise ValueError("公開版來源與指定遠端定稿的去識別結果不同")
        else:
            original = src
    else:
        original = src
    errors, warnings = vp.run_verification(draft, original)
    if errors:
        raise ValueError("潤飾驗證失敗：\n" + "\n".join(errors))
    for warning in warnings:
        print("⚠️ " + warning, file=sys.stderr)
    if public:
        src = redact(original)
    vp.expected_104_fields(src, public)  # Reject unsupported source structure before rendering.
    vmap, missing = build_visual_map(src)
    if missing:
        print("⚠️ 以下區塊沒有視覺重音標註（不加底色／粗體）：" + "、".join(missing), file=sys.stderr)

    exp = sec(src, "工作經歷")
    heads = re.findall(r"^#### (.*)$", exp, re.M)
    parts = re.split(r"^#### .*$", exp, flags=re.M)[1:]
    exps = [exp_html(clean(p), vmap) if i < 3 else "<p>" + html.escape(body_key(clean(p)[0]), quote=False) + "</p>" for i, p in enumerate(parts)]
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
         f"# 104 特化版｜{ver}｜草稿（驗證中）", "",
         f"> 來源：{origin}。",
         "> 排版依 `career/104/styling-directive-guide.md` v2.3.0：子項為獨立 `<li style=\"margin-left: 1em;\">`、模組大標上下 `<p><br></p>` 留白（產出即定版，下游零加工原樣貼入）、"
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
        o += [f"### 3.{i+1} {n}", "", d({"target_block": "skill", "index": i, "action": "replace_all", "mode": "plain_text", "name": n, "tags": vp.skill_tags(i, desc)}),
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
    # Validate a same-directory temporary candidate; publish atomically only after
    # both source/final and field-level checks succeed. A previous good output is
    # preserved on failure; this run never writes a false success marker.
    destination = pathlib.Path(out_path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=destination.parent,
                                         prefix=".104-", suffix=".md", delete=False) as handle:
            temporary = pathlib.Path(handle.name)
            handle.write("\n".join(o) + "\n")
        errs = vp.verify_104_markdown(str(temporary), src, public)
        if errs:
            raise ValueError("產出驗證失敗：\n" + "\n".join(errs))
        candidate = temporary.read_text(encoding="utf-8").replace(
            f"# 104 特化版｜{ver}｜草稿（驗證中）",
            f"# 104 特化版｜{ver}｜**可填表**（verify_polish.py 與 104 欄位驗證通過）", 1)
        temporary.write_text(candidate, encoding="utf-8")
        os.replace(temporary, destination)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)
    print(f"✅ 產出 {out_path}；--verify-104 通過")


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError, IndexError) as exc:
        print(f"❌ {exc}", file=sys.stderr)
        sys.exit(1)

