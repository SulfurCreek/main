#!/usr/bin/env python3
"""104 中英並列履歷產生器（2026-11-03）。

規則（本人指定）：
1. 個人簡介（info.bio）：英文先行，再中文（同一欄）。
2. 每一筆工作經歷（experience.description）：英文先行，再中文（同一欄）。
3. 專長、證照、標籤、專案成就等其他欄位維持原設定，原封不動。
4. 自傳（bio.chi）只有中文，原封不動。

來源（本人 2026-11-03 指定：英文只能從現有英文履歷提取，不重工）：
- 中文：career/drafts/v12.19/104-v12.19-public.md（公開版，已通過 verify_polish），逐字不動。
- 英文：career/drafts/line/line-resume.md 已核准的英文句子（簡介、Skills 行、經歷列點），只重排順序與分段、不改字、不新寫、不翻譯。
  中文獨有而英文履歷沒有的細節，英文側不補（見 source-map.md 的「英文未涵蓋」）。
- 專長（skills）6 張卡：英文先行再中文；英文取自簡介句與 Skills 行。專案成就說明：英文先行再中文，英文取自經歷列點。

用法：python3 career/scripts/gen_104_bilingual.py [--out career/drafts/v12.19-bilingual]
"""
import html
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import line_md  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
ZH_MD = ROOT / "drafts/v12.19/104-v12.19-public.md"
LINE_MD = ROOT / "drafts/line/line-resume.md"

SUMMARY_EN = None  # 於 main() 設為 LINE resume 的 Summary 原文

# 英文列點順序（對應中文 104 版結構）：LINE directive index → (LINE bullet 索引依中文順序, 分組標題)
ORDER = {
    0: {"bullets": [0, 4, 5, 2, 6, 1, 3, 8, 7],
        "groups": {}},
    1: {"bullets": [0, 3, 4, 1, 2],
        "groups": {}},
    2: {"bullets": [0, 2, 1], "groups": {}},
    3: {"bullets": [0], "groups": {}},
}
# 視覺重音（依中文版慣例）：G＝金黃底色（成果數字），B＝晴藍底色＋粗體（核心詞）。key＝LINE bullet 索引。
ACCENT = {
    0: {0: {"B": ["Product Owner"], "G": ["about 60,000 active paying employers (2026 Q3)"]},
        1: {"B": ["new-device OTP login verification (MFA)"], "G": ["more than ten employer accounts"]},
        2: {"B": ["unified messaging flow"], "G": ["199 client requests accumulated since 2021"]},
        3: {"B": ["AI-generated job descriptions", "AI talent recommendations"], "G": ["(2024/10)", "(2025/11)"]},
        4: {"B": ["requirements analysis and specification planning"], "G": ["about 70 major features by 2026 Q3"]},
        5: {"B": ["Analyzed and mapped"], "G": ["743 of 840 related client requests (88%)"]},
        6: {"B": ["shared recruitment feature"], "G": ["55 client requests since 2020/12"]},
        7: {"G": ["from 52% to 79%"]},
        8: {"G": ["15 shared category code tables"]}},
    1: {0: {"B": ["JustDating"]},
        1: {"B": ["Malaysia iOS pricing experiment"], "G": ["rose 5%", "fell 18%", "fell 65%"]},
        2: {"G": ["from 24% to over 80%"]},
        3: {"B": ["KOOL"], "G": ["about 16,000 influencer profiles", "over 80,000 campaign applications"]},
        4: {"B": ["Juicy"], "G": ["from about 3,200 to 12,500", "from about 1,500 to 12,000"]}},
    2: {0: {"B": ["SweetRing"]}, 1: {"B": ["CodaPay"], "G": ["8 payment channels"]}, 2: {"G": ["7 markets"]}},
    3: {},
}
# 專案成就英文：取自 LINE resume 經歷列點（原文不改）。key＝專案 index → [(經歷 index, 列點 index)]；第一則放 blockquote，其餘為段落。
PROJECT_SRC = {1: [(1, 4)], 2: [(1, 3)], 3: [(0, 5), (0, 2)], 4: [(0, 6)]}
PROJECT_ACCENT = {
    1: {"B": ["Juicy"], "G": ["from about 3,200 to 12,500", "from about 1,500 to 12,000"]},
    2: {"B": ["KOOL"], "G": ["about 16,000 influencer profiles", "over 80,000 campaign applications"]},
    3: {"B": ["Analyzed and mapped"], "G": ["743 of 840 related client requests (88%)"]},
    4: {"B": ["shared recruitment feature"], "G": ["55 client requests since 2020/12"]},
}
# 專長 6 張卡英文：整句／整行取自 LINE resume（Summary 句、Skills 行、經歷列點的整句）。
SKILL_SRC = [("summary_sentence", 2), ("skills_line", 0), ("bullet_sentence", (0, 5, 1)), ("skills_line", 1), ("summary_sentence", 1), ("skills_line", 2)]
SKILL_ACCENT = {}

G_STYLE = "background-color: #fbf3db;"
B_STYLE = "background-color: #deebf1;"
H_STYLE = 'class="ql-size-large" style="color: #00afb8;"'


def accent_html(text, acc):
    """text 先逐段 escape 再套重音；每個片語必須在原文出現，否則報錯（不靜默略過）。"""
    marks = []
    for kind in ("G", "B"):
        for ph in acc.get(kind, []):
            i = text.find(ph)
            if i < 0:
                raise ValueError(f"重音片語不在原文：{ph!r}")
            marks.append((i, i + len(ph), kind))
    marks.sort()
    for (a0, a1, _), (b0, b1, _) in zip(marks, marks[1:]):
        if b0 < a1:
            raise ValueError("重音片語重疊")
    out, pos = [], 0
    for s, e, kind in marks:
        out.append(html.escape(text[pos:s], quote=False))
        inner = html.escape(text[s:e], quote=False)
        out.append(f'<strong><span style="{B_STYLE}">{inner}</span></strong>' if kind == "B"
                   else f'<span style="{G_STYLE}">{inner}</span>')
        pos = e
    out.append(html.escape(text[pos:], quote=False))
    return "".join(out)


def english_blocks(line_doc):
    """回傳 {experience index: (bullets_in_zh_order, html)}。"""
    works = [x for x in line_doc["directives"] if x["d"]["target_block"] == "work_experience"]
    res = {}
    for idx, spec in ORDER.items():
        src = list(works[idx]["bullets"])
        bl = [src[j] for j in spec["bullets"]]
        parts, in_list = [], False
        for pos, j in enumerate(spec["bullets"]):
            text = src[j]
            if pos == 0:
                parts.append("<blockquote>" + accent_html(text, ACCENT[idx].get(j, {})) + "</blockquote>")
                continue
            if pos in spec["groups"]:
                if in_list:
                    parts.append("</ul>")
                parts.append("<p><br></p>")
                parts.append(f'<p><span {H_STYLE}><strong>{html.escape(spec["groups"][pos], quote=False)}</strong></span></p>')
                parts.append("<p><br></p>")
                parts.append("<ul>")
                in_list = True
            elif not in_list:
                parts.append("<p><br></p>")
                parts.append("<ul>")
                in_list = True
            parts.append("<li>" + accent_html(text, ACCENT[idx].get(j, {})) + "</li>")
        if in_list:
            parts.append("</ul>")
        res[idx] = (bl, "\n".join(parts))
    return res


def sentences(text):
    """英文句子切分（供來源核對）：句點／問號／驚嘆號後接空白與大寫或括號。"""
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+(?=[A-Z(])", text.strip()) if s.strip()]


def english_projects(line_doc):
    """專案成就英文 HTML：blockquote＝第一則，其餘為段落；全部取自經歷列點原文。"""
    works = [x for x in line_doc["directives"] if x["d"]["target_block"] == "work_experience"]
    res = {}
    for pi, srcs in PROJECT_SRC.items():
        parts = []
        for k, (wi, bi) in enumerate(srcs):
            text = works[wi]["bullets"][bi]
            acc = PROJECT_ACCENT[pi] if k == 0 else {}
            inner = accent_html(text, acc)
            parts.append(f"<blockquote>{inner}</blockquote>" if k == 0 else f"<p>{inner}</p>")
        res[pi] = ("\n".join(parts), [works[wi]["bullets"][bi] for wi, bi in srcs])
    return res


def english_skills(line_doc):
    """專長 6 張卡英文（純文字）：整句或整行取自 LINE resume。"""
    works = [x for x in line_doc["directives"] if x["d"]["target_block"] == "work_experience"]
    summ = sentences(line_doc["summary"])
    out = []
    for kind, ref in SKILL_SRC:
        if kind == "summary_sentence":
            out.append(summ[ref])
        elif kind == "skills_line":
            out.append(line_doc["skills"][ref])
        else:
            wi, bi, si = ref
            out.append(sentences(works[wi]["bullets"][bi])[si])
    return out


def build_en_source(line_text, line_doc, eng):
    """英文來源檔（LINE resume 格式；經歷列點依中文順序重排），供 verify_line_profile 檢查。"""
    t = line_text
    chunks = list(line_md.DIRECTIVE.finditer(t))
    out, last, widx = [], 0, 0
    for m in chunks:
        d = line_md.json.loads(m.group(1))
        end = m.end()
        nxt = t.find("\n## ", end)
        nxt2 = t.find("\n### ", end)
        stop = min(x for x in (nxt, nxt2, len(t)) if x != -1) if d["target_block"] == "work_experience" else end
        out.append(t[last:end])
        if d["target_block"] == "work_experience":
            chunk = t[end:stop]
            keep = [l for l in chunk.splitlines() if not l.startswith("- ")]
            head = "\n".join(keep).rstrip("\n")
            bullets = "\n".join("- " + b for b in eng[widx][0])
            out.append(head + "\n" + bullets + "\n")
            last = stop
            widx += 1
        else:
            last = end
    out.append(t[last:])
    return "".join(out)


def combine(zh_text, summary_en, eng, skills_en, projects_en):
    """把英文先行併入中文公開版 md：info.bio、4 筆經歷、6 張專長、4 筆專案說明。自傳與其餘逐字不動。"""
    m = re.search(r"(\"field\": \"bio\", \"mode\": \"plain_text\"\}\n-->\n\n```text\n)(.*?)(```)", zh_text, re.S)
    if not m:
        raise ValueError("找不到 info.bio 區塊")
    t = zh_text[:m.start(2)] + summary_en + "\n\n" + m.group(2).rstrip("\n") + "\n" + zh_text[m.end(2):]

    def sub_all(text, pat, fn, expect, label):
        seen = [0]

        def r(mm):
            seen[0] += 1
            return fn(mm)
        out = pat.sub(r, text)
        if seen[0] != expect:
            raise ValueError(f"{label}應為 {expect} 筆，實際 {seen[0]}")
        return out

    t = sub_all(t, re.compile(r"(### 2\.(\d) [^\n]*\n.*?```html\n)(.*?)(```)", re.S),
                lambda mm: mm.group(1) + eng[int(mm.group(2)) - 1][1] + "\n<p><br></p>\n" + mm.group(3).rstrip("\n") + "\n" + mm.group(4), 4, "工作經歷")
    t = sub_all(t, re.compile(r"(### 3\.(\d) [^\n]*\n.*?```text\n)(.*?)(```)", re.S),
                lambda mm: mm.group(1) + skills_en[int(mm.group(2)) - 1] + "\n\n" + mm.group(3).rstrip("\n") + "\n" + mm.group(4), 6, "專長")
    t = sub_all(t, re.compile(r"(### 5\.(\d) [^\n]*\n.*?```html\n)(.*?)(```)", re.S),
                lambda mm: mm.group(1) + projects_en[int(mm.group(2))][0] + "\n<p><br></p>\n" + mm.group(3).rstrip("\n") + "\n" + mm.group(4), 4, "專案成就")
    t = t.replace("# 104 特化版｜v12.19 公開版（2026-10-27）｜**可填表**", "# 104 特化版｜v12.19 公開版 中英並列（2026-11-03）｜**可填表**", 1)
    return t


def numbers_en(s):
    s = re.sub(r"<[^>]*>", "", s)
    return {round(float(m.group(0).replace(",", "")), 3) for m in re.finditer(r"\d[\d,]*(?:\.\d+)?", s)}


def numbers_zh(s):
    s = re.sub(r"<[^>]*>", "", s)
    out = set()
    for m in re.finditer(r"(\d[\d,]*(?:\.\d+)?)\s*(萬)?", s):
        out.add(round(float(m.group(1).replace(",", "")) * (10000 if m.group(2) else 1), 3))
    return out


def project_checks(zh_text, projects_en):
    """英文專案不得出現中文專案說明沒有的數字（防新增事實）。中文有而英文沒有的細節列為「英文未涵蓋」，不算錯。"""
    errs = []
    zh_blocks = {int(m.group(1)): m.group(2) for m in re.finditer(r"### 5\.(\d) [^\n]*\n.*?```html\n(.*?)```", zh_text, re.S)}
    zh_all = numbers_zh(zh_text)  # 英文取自同一份履歷的經歷列點，數字只需出現在中文履歷某處
    for i, (h, _) in projects_en.items():
        extra = numbers_en(h) - zh_all
        if extra:
            errs.append(f"5.{i} 英文有、中文專案說明沒有的數字：{sorted(extra)}")
    return errs


def source_map(skills_en):
    L = ["<!--markdownlint-disable MD013-->", "", "# 104 中英並列：英文來源對照（2026-11-03）", "",
         "> 規則：英文只能取自 `career/drafts/line/line-resume.md` 現有英文，不新寫、不翻譯、不補中文獨有細節。", "",
         "| 欄位 | 英文來源 |", "| :-- | :-- |", "| 個人簡介 | line-resume.md Summary（全文） |"]
    works = ["2.1", "2.2", "2.3", "2.4"]
    for idx, spec in ORDER.items():
        L.append(f"| 經歷 {works[idx]} | line-resume.md §{works[idx]} 列點索引 {spec['bullets']}（依中文順序重排，原文不改） |")
    for i, s in enumerate(SKILL_SRC, 1):
        L.append(f"| 專長 3.{i} | {s[0]} {s[1]}：{skills_en[i-1][:60]}… |")
    for pi, srcs in PROJECT_SRC.items():
        L.append(f"| 專案 5.{pi} | line-resume.md §2.{srcs[0][0]+1} 列點 {[b for _, b in srcs]} |")
    L += ["", "## 英文未涵蓋（中文獨有、英文履歷沒有的細節；不補）", "",
          "- 專案 5.1：CodaPay 在台灣以外市場的收款規劃（網頁加值頁、商務洽談、定價、工程窗口）；",
          "- 專案 5.2：KOOL「網紅人力銀行」構想、評價／地圖／手機認證／作品集功能；",
          "- 專案 5.3：全國客服上線前封測、2025/10 與 2026/01 分階段上線日期；",
          "- 專案 5.4：2025/Q3 上線時間；",
          "- 專長 3.1–3.6 中文描述中的工具與做法細節（Trello、甘特圖、IAP 抽成比較等）；",
          "- 簡介中文的「6 款產品」清單。", ""]
    return "\n".join(L)


def main(argv=None):
    global SUMMARY_EN
    argv = sys.argv[1:] if argv is None else argv
    out = Path(argv[argv.index("--out") + 1]) if "--out" in argv else ROOT / "drafts/v12.19-bilingual"
    line_text = LINE_MD.read_text(encoding="utf-8")
    line_doc = line_md.parse(line_text)
    SUMMARY_EN = line_doc["summary"]
    eng = english_blocks(line_doc)
    skills_en = english_skills(line_doc)
    projects_en = english_projects(line_doc)
    zh_text = ZH_MD.read_text(encoding="utf-8")
    perr = project_checks(zh_text, projects_en)
    if perr:
        print("❌ 專案英文檢查失敗：\n - " + "\n - ".join(perr))
        return 1
    bilingual = combine(zh_text, SUMMARY_EN, eng, skills_en, projects_en)
    out.mkdir(parents=True, exist_ok=True)
    (out / "upstream-check.md").write_text(line_text, encoding="utf-8")
    (out / "en-source.md").write_text(build_en_source(line_text, line_doc, eng), encoding="utf-8")
    (out / "104-v12.19-bilingual.md").write_text(bilingual, encoding="utf-8")
    (out / "source-map.md").write_text(source_map(skills_en), encoding="utf-8")
    print(f"✅ {out}/104-v12.19-bilingual.md、en-source.md、source-map.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
