#!/usr/bin/env python3
"""由 line-profile.fill.json（定稿唯一內文來源）產生單欄英文履歷 HTML；再用 resume-craft/scripts/mkpdf.js 轉 PDF。
不新增、不改寫任何內文；不含街道地址。用法：python3 career/scripts/gen_line_pdf.py [fill.json] [out.html]"""
import html, json, sys
from pathlib import Path

src = Path(sys.argv[1] if len(sys.argv) > 1 else "career/drafts/line/line-profile.fill.json")
out = Path(sys.argv[2] if len(sys.argv) > 2 else "career/drafts/line/line-profile.html")
steps = json.loads(src.read_text(encoding="utf-8"))["steps"]
e = html.escape
basic = next(s for s in steps if s["target_block"] == "basic")["fields"]
work = [s for s in steps if s["target_block"] == "work_experience"]
edu = [s for s in steps if s["target_block"] == "education"]
DEG = {"21": "Bachelor's"}
STAT = {"2559": "Exchange Program"}

def span(f):
    return f"{f['start_date']} – {f['end_date'] or 'Present'}"

h = [f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Kun Huai Nie – Resume</title><style>
@page{{size:A4;margin:12mm 14mm}}
body{{font:9.6pt/1.33 Arial,Helvetica,sans-serif;color:#111;margin:0}}
h1{{font-size:22pt;margin:0}} .t{{color:#1d4f91;font-weight:bold;margin:2px 0}} .c{{color:#444;font-size:9.5pt}}
h2{{font-size:11pt;letter-spacing:.08em;text-transform:uppercase;border-bottom:2px solid #111;padding-bottom:2px;margin:12px 0 6px}}
.j{{margin:0 0 10px;break-inside:avoid-page}} .jh{{font-weight:bold}} .co{{color:#1d4f91}} .d{{color:#555;font-size:9.5pt}}
ul{{margin:4px 0 0;padding-left:18px}} li{{margin:0 0 2px}}
</style></head><body>
<h1>Kun Huai Nie</h1><div class="t">{e(basic['current_position_title'])}</div>
<div class="c">{e(basic['email'])} · {e(basic['mobile_phone'])} · {e(basic['city'])}, Taiwan</div>
<h2>Work Experience</h2>"""]
for s in work:
    f = s["fields"]
    h.append(f'<div class="j"><div class="jh">{e(f["position_title"])} · <span class="co">{e(f["company"])}</span></div>'
             f'<div class="d">{span(f)} · {e(f["location"])}</div><ul>')
    h += [f"<li>{e(b)}</li>" for b in s.get("description_bullets", [])]
    h.append("</ul></div>")
h.append("<h2>Education</h2>")
for s in edu:
    f = s["fields"]
    note = f" ({STAT[f['degree_status']]})" if f["degree_status"] in STAT and "Exchange" not in f["degree_name"] else ""
    h.append(f'<div class="j"><div class="jh">{e(f["university"])}</div><div>{e(f["degree_name"])}{note}</div><div class="d">{span(f)}</div></div>')
h.append("<h2>Languages</h2><div>English · Mandarin</div></body></html>")
out.write_text("\n".join(h), encoding="utf-8")
print("✅", out)
