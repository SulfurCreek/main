#!/usr/bin/env python3
"""由 <stem>.resume.json（唯一內文來源）產生單欄英文履歷 HTML；再用 resume-craft/scripts/mkpdf.js 轉 PDF。
不新增、不改寫任何內文；不含街道地址。用法：python3 career/scripts/gen_line_pdf.py <resume.json> <out.html>

2026-11-02 契約：渲染前重算 payload_sha256、並以 source 路徑重算 source_sha256，任一不符即拒絕（防 JSON 被竄改或來源不符）。
HTML 以 <meta> 帶兩個雜湊，供 verify_line_pdf 串接 Markdown → JSON → HTML → PDF。Languages：Skills 已列出者不重複，未列出者補區塊；未知代碼直接報錯。"""
import hashlib, html, json, os, sys
from pathlib import Path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_line_pack import payload_hash  # noqa: E402

LANG = {"10": "English", "14": "Mandarin"}
LEVEL = {"33": "Native"}


def check_source(d):
    errs = []
    if d.get("payload_sha256") != payload_hash(d):
        errs.append("payload_sha256 與內容不符（JSON 被修改或非 gen_line_pack 產出）")
    src = Path(d.get("source", ""))
    if not src.is_file():
        errs.append(f"找不到來源 Markdown：{src}")
    elif hashlib.sha256(src.read_text(encoding="utf-8").encode()).hexdigest() != d.get("source_sha256"):
        errs.append("source_sha256 與來源 Markdown 不符（來源已變更，請重跑 gen_line_pack）")
    return errs

FS = os.environ.get('LINE_PDF_FONT', '9.6')
def render(_d, FS=FS):
    """resume.json → HTML 字串（不寫檔）。"""
    steps, summary, skills = _d["steps"], _d["summary"], _d["skills"]
    pstat = _d.get("personal_statement", [])
    e = html.escape
    basic = next(s for s in steps if s["target_block"] == "basic")["fields"]
    work = [s for s in steps if s["target_block"] == "work_experience"]
    edu = [s for s in steps if s["target_block"] == "education"]
    DEG = {"21": "Bachelor's"}
    STAT = {"2559": "Exchange Program"}

    def span(f):
        return f"{f['start_date']} – {f['end_date'] or 'Present'}"

    h = [f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Kun Huai Nieh – Resume</title><style>
    @page{{size:A4;margin:12mm 14mm}}
    body{{font:{FS}pt/1.33 Arial,Helvetica,sans-serif;color:#111;margin:0}}
    h1{{font-size:22pt;margin:0}} .t{{color:#1d4f91;font-weight:bold;margin:2px 0}} .c{{color:#444;font-size:9.5pt}}
    h2{{font-size:11pt;letter-spacing:.08em;text-transform:uppercase;border-bottom:2px solid #111;padding-bottom:2px;margin:12px 0 6px}}
    .j{{margin:0 0 10px;break-inside:avoid-page}} .jh{{font-weight:bold}} .co{{color:#1d4f91}} .d{{color:#555;font-size:9.5pt}}
    ul{{margin:4px 0 0;padding-left:0;list-style:none}} li{{margin:0 0 2px;display:flex;gap:6px}} li .b{{flex:0 0 10px;text-align:center}} li .bt{{flex:1}}
    </style></head><body>
    <meta name="source-sha256" content="{_d['source_sha256']}"><meta name="payload-sha256" content="{_d['payload_sha256']}">
    <h1>Kun Huai Nieh</h1><div class="t">{e(basic['current_position_title'])}</div>
    <div class="c">{e(basic['email'])} · {e(basic['mobile_phone'])} · {e(basic['city'])}, Taiwan</div>
    <h2>Professional Summary</h2><p style="margin:0">{e(summary)}</p>
    <h2>Skills</h2><ul>"""
        + "".join(f'<li><span class="b">•</span><span class="bt">{e(x)}</span></li>' for x in skills) + """</ul><h2>Work Experience</h2>"""]
    for s in work:
        f = s["fields"]
        h.append(f'<div class="j"><div class="jh">{e(f["position_title"])} · <span class="co">{e(f["company"])}</span></div>'
                 f'<div class="d">{span(f)} · {e(f["location"])}</div><ul>')
        h += [f'<li><span class="b">•</span><span class="bt">{e(b)}</span></li>' for b in s.get("description_bullets", [])]
        h.append("</ul></div>")
    h.append("<h2>Education</h2>")
    for s in edu:
        f = s["fields"]
        note = f" ({STAT[f['degree_status']]})" if f["degree_status"] in STAT and "Exchange" not in f["degree_name"] else ""
        h.append(f'<div class="j"><div class="jh">{e(f["university"])}</div><div>{e(f["degree_name"])}{note}</div><div class="d">{span(f)}</div></div>')
    langs = [s for s in steps if s["target_block"] == "languages"]
    if langs:
        items = []
        for s in langs:
            f = s["fields"]
            if f["language"] not in LANG:
                raise ValueError(f"❌ 未知語言代碼 {f['language']}：請在 gen_line_pdf.LANG 補對照，不得略過")
            lv = {LEVEL.get(f[k]) for k in ("written", "spoken", "reading", "listening")} - {None}
            items.append(LANG[f["language"]] + (f" ({lv.pop()})" if len(lv) == 1 else ""))
        shown = " ".join(skills)
        missing = [x.split(" (")[0] for x in items if x.split(" (")[0] not in shown]
        if missing:  # 語言已在 Skills 的 Languages 行呈現；沒呈現的才補區塊，不得無聲遺漏
            h.append("<h2>Languages</h2><p style=\"margin:0\">" + e(" · ".join(items)) + "</p>")
    if pstat:
        h.append("<h2>Personal Statement</h2>" + "".join(f"<p style=\"margin:0 0 6px\">{e(x)}</p>" for x in pstat))
    h.append("</body></html>")
    return "\n".join(h)


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    if len(argv) != 2:
        print(__doc__)
        return 2
    src, out = Path(argv[0]), Path(argv[1])
    d = json.loads(src.read_text(encoding="utf-8"))
    bad = check_source(d)
    if bad:
        print("❌ 拒絕渲染：" + "；".join(bad))
        return 1
    try:
        out.write_text(render(d), encoding="utf-8")
    except ValueError as e:
        print(e)
        return 1
    print("✅", out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
