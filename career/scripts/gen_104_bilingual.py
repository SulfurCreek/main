#!/usr/bin/env python3
"""104 中英並列履歷產生器（2026-11-03）。

規則（本人指定）：
1. 個人簡介（info.bio）：英文先行，再中文（同一欄）。
2. 每一筆工作經歷（experience.description）：英文先行，再中文（同一欄）。
3. 專長、證照、標籤、專案成就等其他欄位維持原設定，原封不動。
4. 自傳（bio.chi）只有中文，原封不動。

來源：
- 中文：career/drafts/v12.19/104-v12.19-public.md（公開版，已通過 verify_polish），逐字不動。
- 英文：career/drafts/line/line-resume.md 已核准的英文列點（經 Codex 潤飾、盲審、最新 verify_line_profile），只重排順序、不改字；
  簡介英文為新寫，對應中文簡介，仍須通過 verify_line_profile。
- 英文來源檔 en-source.md 以 LINE resume 格式輸出，供 verify_line_profile --upstream line-resume.md 核對。

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

SUMMARY_EN = (
    "Product Owner with nearly 10 years of product management experience, currently owning an employer-side recruitment system, "
    "managing two product planners as direct reports, and responsible for both ongoing service iterations and the system's full overhaul. "
    "Worked on six products (JustDating, Juicy, Peach, SweetRing, KOOL and the recruitment system), covering subscriptions, pricing experiments, "
    "two-sided matching and enterprise workflows. After the flagship dating app was removed from the App Store, led the launch of a replacement app "
    "and worked with marketing to retain existing users and revenue. Turn complex business rules into product solutions, communicate through flows, "
    "specifications and prototypes, and work with engineering and QA through release. Use AI agents to draft specifications and to organize and analyze data, "
    "then check and correct the output."
)

# 英文列點順序（對應中文 104 版結構）：LINE directive index → (LINE bullet 索引依中文順序, 分組標題)
ORDER = {
    0: {"bullets": [0, 4, 5, 2, 6, 1, 3, 8, 7],
        "groups": {1: "1. Core System Overhaul and Enterprise Needs", 7: "2. AI Features and Operating Processes"}},
    1: {"bullets": [0, 3, 4, 1, 2],
        "groups": {1: "1. Zero-to-One Influencer Platform and Monetization", 3: "2. Product Recovery, Pricing Experiment and Web Payments"}},
    2: {"bullets": [0, 2, 1], "groups": {1: "Market Localization and Third-Party Payments"}},
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
G_STYLE = "background-color: #fbf3db;"
B_STYLE = "background-color: #deebf1;"
H_STYLE = 'class="ql-size-large" style="color: #00afb8;"'


def reduce_fix(b):
    for o, n in EN_FIX.items():
        b = b.replace(o, n)
    return b


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


# 104 英文專屬措辭修正（LINE 原稿不動；本人 2026-11-03 英文信已採同一用字，母語審讀亦指出 opening 用字不自然）
EN_FIX = {"and opening 8 payment channels": "and launching 8 payment channels"}


def english_blocks(line_doc):
    """回傳 {experience index: (bullets_in_zh_order, html)}。"""
    works = [x for x in line_doc["directives"] if x["d"]["target_block"] == "work_experience"]
    res = {}
    for idx, spec in ORDER.items():
        src = [reduce_fix(b) for b in works[idx]["bullets"]]
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


def build_en_source(line_text, line_doc, eng):
    """產出 LINE resume 格式的英文來源檔（供 verify_line_profile --upstream 核對）：Summary 換成 104 簡介、列點依中文順序。"""
    t = line_text
    t = t.replace(line_doc["summary"], SUMMARY_EN, 1)
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


def combine(zh_text, eng):
    """把英文先行併入中文公開版 md：info.bio、四筆 experience.description。其餘逐字不動。"""
    # 簡介
    m = re.search(r"(\"field\": \"bio\", \"mode\": \"plain_text\"\}\n-->\n\n```text\n)(.*?)(```)", zh_text, re.S)
    if not m:
        raise ValueError("找不到 info.bio 區塊")
    zh_bio = m.group(2).rstrip("\n")
    t = zh_text[:m.start(2)] + SUMMARY_EN + "\n\n" + zh_bio + "\n" + zh_text[m.end(2):]
    # 經歷
    pat = re.compile(r"(### 2\.(\d) [^\n]*\n.*?```html\n)(.*?)(```)", re.S)
    seen = 0

    def repl(mm):
        nonlocal seen
        idx = int(mm.group(2)) - 1
        seen += 1
        zh_html = mm.group(3).rstrip("\n")
        return mm.group(1) + eng[idx][1] + "\n<p><br></p>\n" + zh_html + "\n" + mm.group(4)
    t = pat.sub(repl, t)
    if seen != 4:
        raise ValueError(f"工作經歷區塊應為 4 筆，實際 {seen}")
    t = t.replace("# 104 特化版｜v12.19 公開版（2026-10-27）｜**可填表**", "# 104 特化版｜v12.19 公開版 中英並列（2026-11-03）｜**可填表**", 1)
    return t


def plain(s):
    return re.sub(r"\s+", "", re.sub(r"<[^>]*>", "", s))


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    out = Path(argv[argv.index("--out") + 1]) if "--out" in argv else ROOT / "drafts/v12.19-bilingual"
    line_text = LINE_MD.read_text(encoding="utf-8")
    line_doc = line_md.parse(line_text)
    eng = english_blocks(line_doc)
    zh_text = ZH_MD.read_text(encoding="utf-8")
    bilingual = combine(zh_text, eng)
    en_source = build_en_source(line_text, line_doc, eng)
    out.mkdir(parents=True, exist_ok=True)
    # 事實核對基準：LINE resume 但 Summary 換成 104 簡介（104 簡介與 LINE 特化簡介不同，以中文 104 簡介人工對照），並移除 Summary 專屬鎖定詞
    chk = line_text.replace(line_doc["summary"], SUMMARY_EN, 1)
    chk = re.sub(r"(<!-- \[STATUS: POLISHED\]) \[LOCK_ENTITIES:[^\]]*\]( -->\n- " + re.escape(SUMMARY_EN[:30]) + ")", r"\1\2", chk, count=1)
    (out / "upstream-check.md").write_text(chk, encoding="utf-8")
    (out / "en-source.md").write_text(en_source, encoding="utf-8")
    (out / "104-v12.19-bilingual.md").write_text(bilingual, encoding="utf-8")
    print(f"✅ {out}/en-source.md、104-v12.19-bilingual.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
