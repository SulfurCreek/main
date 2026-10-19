#!/usr/bin/env python3
"""履歷 txt → 單欄 ATS 版 HTML。用法：python3 render_onecol.py <resume.txt> <out.html>；接著 node mkpdf.js <out.html 絕對路徑> <out.pdf>"""
import html,sys
src,dst=sys.argv[1],sys.argv[2]  # 選項 --bio-newpage：自傳另起一頁
t=open(src,encoding='utf8').read().split('\n')
heads={'專業摘要','工作經歷','學歷','專業技能','求職條件','自傳'}
out=[];ul=False;sec=''
for i,l in enumerate(t):
    l=l.rstrip()
    if i==0: out.append(f'<h1>{html.escape(l)}</h1>');continue
    if not l.startswith('- ') and ul: out.append('</ul>');ul=False
    if not l: continue
    if l in heads: sec=l
    if l in heads: out.append(f'<h2 style="break-before:page">{l}</h2>' if l=='自傳' and '--bio-newpage' in sys.argv else f'<h2>{l}</h2>');continue
    if l.startswith('- '):
        if not ul: out.append('<ul>');ul=True
        out.append(f'<li>{html.escape(l[2:])}</li>');continue
    pb=not t[i-1].strip()
    if sec=='學歷': out.append(f'<p class="edu">{html.escape(l)}</p>');continue
    if sec=='自傳': out.append(f'<p class="bio">{html.escape(l)}</p>');continue
    if pb and (('｜' in l and not l.startswith(('資深','2015'))) or (len(l)<18 and '。' not in l)): out.append(f'<h3>{html.escape(l)}</h3>')
    else: out.append(f'<p>{html.escape(l)}</p>')
if ul: out.append('</ul>')
css="""@page{size:A4;margin:12mm 14mm}body{font-family:Arial,'Noto Sans TC','WenQuanYi Zen Hei',sans-serif;font-size:10.2pt;line-height:1.5;color:#111}
h1{font-size:18pt;margin:0 0 6px}h2{break-after:avoid;page-break-after:avoid;font-size:12pt;border-bottom:1px solid #444;margin:10px 0 4px;padding-bottom:2px}h3{break-after:avoid;page-break-after:avoid;font-size:10.5pt;margin:8px 0 2px}
p{margin:2px 0}ul{margin:2px 0 4px 18px;padding:0}li{margin:2px 0;break-inside:avoid}.edu{margin:1px 0}.bio{margin:0 0 7px;line-height:1.65}h3+p{break-after:avoid;page-break-after:avoid}h3+p+ul>li:first-child{break-before:avoid}"""
open(dst,'w',encoding='utf8').write(f'<!doctype html><html lang="zh-Hant"><meta charset=utf-8><title>Resume</title><style>{css}</style><body>'+'\n'.join(out)+'</body></html>')
