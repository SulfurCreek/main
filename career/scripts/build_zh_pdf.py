#!/usr/bin/env python3
"""中文雙欄履歷 PDF：讀 Codex 定稿 md（含註解），去標記後渲染 HTML → Playwright PDF。
用法：python3 career/scripts/build_zh_pdf.py <final.md> <out.pdf> [--sub '舊=>新' ...]
--sub 只用於 Claude 終審的事實限定修正，必須在交付說明逐條列出。"""
import re, sys, html, subprocess, json, os
src, out = sys.argv[1], sys.argv[2]
subs = [a.split('=>', 1) for a in sys.argv[3:] if '=>' in a]
t = open(src, encoding='utf-8').read()
t = re.sub(r'<!--.*?-->', '', t, flags=re.S)
for a, b in subs:
    assert a in t, f'找不到：{a}'
    t = t.replace(a, b)
sec, cur = {}, None
for line in t.splitlines():
    if line.startswith('## '):
        cur = line[3:].strip(); sec[cur] = []
    elif cur and not line.lstrip().startswith('> '):
        sec[cur].append(line)
e = html.escape
def inline(s):
    s = e(s)
    return re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', s)
def block(lines):
    o, jobs = [], []
    for l in lines:
        l = l.rstrip()
        if not l: continue
        if l.startswith('### '):
            title, co, dur = (l[4:].split('｜') + ['', ''])[:3]
            o.append(f'<div class="job"><div class="jh"><span class="jt">{e(title)}</span><span class="jd">{e(dur)}</span></div><div class="jc">{e(co)}</div>')
            o.append('</div>'); 
        elif l.startswith('- '):
            o.insert(len(o)-1, f'<li>{inline(l[2:])}</li>')
        else:
            o.insert(len(o)-1 if o and o[-1]=='</div>' else len(o), f'<p>{inline(l)}</p>')
    h = ''.join(o)
    return re.sub(r'((?:<li>.*?</li>)+)', r'<ul>\1</ul>', h)
head = [l for l in sec.get('抬頭', []) if l.strip()]
name, title = (head[0].split('｜') + [''])[:2]
skills = ''.join(f'<li>{e(x.strip())}</li>' for x in ' '.join(sec.get('專長', [])).split('｜') if x.strip())
edu = ''.join(f'<li>{e(x.strip())}</li>' for l in sec.get('學歷與證照', []) for x in l.split('｜') if x.strip())
summary = ''.join(f'<p>{inline(x.strip())}</p>' for x in '\n'.join(sec.get('簡介', [])).split('\n\n') if x.strip())
doc = f'''<!doctype html><html><head><meta charset="utf-8"><style>
@page {{ size: A4; margin: 12mm 12mm; }}
body {{ font-family: "Noto Sans CJK TC","WenQuanYi Zen Hei",sans-serif; font-size: 9.3pt; line-height: 1.5; color:#222; margin:0 }}
.top {{ border-bottom: 2px solid #566876; padding-bottom: 6px; margin-bottom: 8px; display:flex; justify-content:space-between; align-items:flex-end }}
.top h1 {{ font-size: 20pt; margin:0; color:#2c3a45 }} .top .t {{ font-size: 11pt; color:#566876; margin-left:8px }}
.top .c {{ font-size: 8.8pt; color:#444 }}
.sum {{ background:#f2f5f7; padding:7px 9px; border-radius:4px; margin-bottom:8px }}
.grid {{ display:grid; grid-template-columns: 1fr 52mm; gap: 12px }}
h2 {{ font-size: 10.5pt; color:#566876; border-bottom:1px solid #c9d2d8; margin:6px 0 4px; padding-bottom:2px }}
.job {{ margin-bottom:7px }} .sum p {{ margin:0 0 4px }} .jh {{ display:flex; justify-content:space-between }}
.jt {{ font-weight:700; font-size:10pt }} .jd {{ color:#566876; font-size:8.8pt }} .jc {{ color:#444; font-size:9pt; margin-bottom:2px }}
p {{ margin: 2px 0 3px }} ul {{ margin: 2px 0; padding-left: 14px }} li {{ margin-bottom: 3px; break-inside: avoid }}
.side ul {{ padding-left: 12px }} .side li {{ font-size: 8.8pt }}
b {{ color:#0b5d7a; -webkit-text-stroke: 0.35px #0b5d7a }} .jt {{ -webkit-text-stroke: 0.4px #222 }} .top h1 {{ -webkit-text-stroke: 0.6px #2c3a45 }}
</style></head><body>
<div class="top"><div><h1>{e(name)}<span class="t">{e(title)}</span></h1></div><div class="c">{e(head[1] if len(head)>1 else "")}</div></div>
<div class="sum">{summary}</div>
<div class="grid"><div class="main"><h2>工作經歷</h2>{block(sec.get("工作經歷", []))}</div>
<div class="side"><h2>專長</h2><ul>{skills}</ul><h2>學歷與證照</h2><ul>{edu}</ul></div></div>
</body></html>'''
hp = out[:-4] + '.html'
open(hp, 'w', encoding='utf-8').write(doc)
js = f"""const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();const p=await b.newPage();
await p.goto('file://{os.path.abspath(hp)}');await p.pdf({{path:'{os.path.abspath(out)}',format:'A4',printBackground:true,preferCSSPageSize:true}});await b.close();}})();"""
subprocess.run(['node', '-e', js], check=True)
print('OK', out)
