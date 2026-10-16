#!/usr/bin/env python3
"""履歷 txt → 雙欄 PDF 版面 HTML（2026-10-13 使用者指定版型，參考 Enhancv「Brad Jensen」範例）。

版型：
- 抬頭：姓名大字粗黑；職稱行藍字（｜分隔）；聯絡資訊一列，前置小圖示（inline SVG，不進文字層）。
- 左欄（約 63%）：專業摘要、關鍵成果之外的工作經歷——職稱黑字、公司藍字、日期列附日曆圖示、條列。
- 右欄（約 37%）：關鍵成果（txt 有〈關鍵成果〉才出現，格式「- 標題：內文」）、專業技能（「類別：內容」類別加粗）、
  學歷（學校粗體、科系藍字、日期圖示）、求職條件。
- 自傳：雙欄之後整寬，接在左欄結尾之後（不強制換頁，避免空白頁）。
- 區塊標題：粗體、字距、下方 3px 黑線。
DOM 順序 = 閱讀順序（左欄全部 → 右欄 → 自傳），PDF 抽文字時不會左右交錯；產出後仍要跑 parse_check.py。

用法：python3 render_twocol.py <resume.txt> <out.html> [--location 台北市]
接著：node mkpdf.js <out.html 絕對路徑> <out.pdf>
"""
import html, re, sys

LEFT = ['專業摘要', '工作經歷']
RIGHT = ['關鍵成果', '專業技能', '學歷', '求職條件']
FULL = ['自傳']
HEADS = set(LEFT + RIGHT + FULL)
DATE = re.compile(r'(\d{4}/\d{1,2}\s*[-–~至]\s*(?:\d{4}/\d{1,2}|迄今|至今|Present))')

I = {  # 14px 線條圖示
    'cal': '<svg viewBox="0 0 24 24"><rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/></svg>',
    'mail': '<svg viewBox="0 0 24 24"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/></svg>',
    'phone': '<svg viewBox="0 0 24 24"><path d="M5 4h4l2 5-3 2a11 11 0 0 0 5 5l2-3 5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2z"/></svg>',
    'pin': '<svg viewBox="0 0 24 24"><path d="M12 22s7-7 7-12a7 7 0 0 0-14 0c0 5 7 12 7 12z"/><circle cx="12" cy="10" r="2.5"/></svg>',
}
e = html.escape


def ico(k):
    return f'<span class="ic">{I[k]}</span>'


def split_sections(lines):
    head, secs, cur = [], {}, None
    for l in lines:
        s = l.rstrip()
        if s in HEADS:
            cur = s; secs[cur] = []; continue
        if cur is None:
            if s: head.append(s)
        else:
            secs[cur].append(s)
    return head, secs


def bullets(items):
    return '<ul>' + ''.join(f'<li>{e(x)}</li>' for x in items) + '</ul>' if items else ''


def r_summary(ls):
    return '<p class="summary">' + ''.join(e(l) for l in ls if l.strip()) + '</p>'


def r_jobs(ls):
    out, buf = [], []
    def flush():
        if buf: out.append(bullets(buf)); buf.clear()
    for l in ls:
        if not l.strip(): flush(); continue
        if l.startswith('- '): buf.append(l[2:]); continue
        flush()
        m = DATE.search(l)
        if '｜' in l and m:
            parts = [p.strip() for p in l[:m.start()].strip('｜ ').split('｜')]
            title, comp = parts[0], '｜'.join(parts[1:])
            out.append(f'<div class="job"><div class="jt">{e(title)}</div><div class="co">{e(comp)}</div>'
                       f'<div class="meta">{ico("cal")}{e(m.group(1))}</div></div>')
        elif m and l.strip().startswith(m.group(1)):
            out.append(f'<p class="note">{e(l)}</p>')
        else:
            out.append(f'<p class="scope">{e(l)}</p>')
    flush()
    return ''.join(out)


def r_kv(ls, cls):
    out = []
    for l in ls:
        l = l.strip()
        if not l: continue
        l = l[2:] if l.startswith('- ') else l
        k, sep, v = l.partition('：')
        out.append(f'<div class="{cls}"><b>{e(k)}</b>{"<span>" + e(v) + "</span>" if sep else ""}</div>')
    return ''.join(out)


def r_edu(ls):
    out = []
    for l in ls:
        if not l.strip(): continue
        m = DATE.search(l)
        parts = [p.strip() for p in (l[:m.start()] if m else l).strip('｜ ').split('｜')]
        out.append(f'<div class="edu"><b>{e(parts[0])}</b><div class="co">{e("｜".join(parts[1:]))}</div>'
                   + (f'<div class="meta">{ico("cal")}{e(m.group(1))}</div>' if m else '') + '</div>')
    return ''.join(out)


def r_para(ls):
    return ''.join(f'<p>{e(l)}</p>' for l in ls if l.strip())


R = {'專業摘要': r_summary, '工作經歷': r_jobs, '關鍵成果': lambda ls: r_kv(ls, 'ach'),
     '專業技能': lambda ls: r_kv(ls, 'sk'), '學歷': r_edu, '求職條件': r_para, '自傳': r_para}

CSS = """@page{size:A4;margin:11mm 12mm}
:root{--blue:#2f7fd8;--ink:#141414;--mute:#555}
body{font-family:Arial,'Noto Sans TC','WenQuanYi Zen Hei',sans-serif;font-size:9.6pt;line-height:1.45;color:var(--ink);margin:0}
h1{font-size:24pt;font-weight:700;letter-spacing:.5px;margin:0}
.tagline{color:var(--blue);font-size:12.5pt;font-weight:700;margin:3px 0 5px}
.contact{display:flex;gap:16px;font-size:9.2pt;font-weight:700;margin-bottom:10px}
.ic svg{width:11px;height:11px;fill:none;stroke:var(--blue);stroke-width:2;vertical-align:-1px;margin-right:4px}
.grid{display:grid;grid-template-columns:63fr 37fr;gap:22px}
h2{font-size:12pt;font-weight:700;letter-spacing:1px;border-bottom:3px solid var(--ink);padding-bottom:2px;margin:10px 0 6px;break-after:avoid}
.job{margin-top:8px;break-after:avoid}.jt{font-size:11pt;font-weight:700}.co{color:var(--blue);font-weight:700}
.meta{font-size:8.8pt;color:var(--mute);margin:1px 0 2px}.meta .ic svg{stroke:var(--mute)}
.scope{color:var(--mute);font-size:9pt;margin:2px 0}.note{font-size:9pt;color:var(--mute);margin:6px 0 0}
ul{margin:3px 0 4px 15px;padding:0}li{margin:2px 0}
.summary{margin:0}
.ach{padding:5px 0;border-bottom:1px dotted #bbb}.ach b{display:block;font-size:9.8pt}.ach span{font-size:9pt}
.sk{margin:3px 0}.sk b{display:block}.sk span{font-size:9pt}
.edu{margin:4px 0 8px}.edu b{font-size:10pt}
.full{margin-top:6px}.full p{margin:0 0 7px}"""


def main():
    src, dst = sys.argv[1], sys.argv[2]
    loc = sys.argv[sys.argv.index('--location') + 1] if '--location' in sys.argv else ''
    head, secs = split_sections(open(src, encoding='utf8').read().split('\n'))
    name, tag = head[0], head[1] if len(head) > 1 else ''
    contact = head[2].split('｜') if len(head) > 2 else []
    cs = ''.join(f'<span>{ico("mail" if "@" in c else "phone")}{e(c.strip())}</span>' for c in contact)
    if loc: cs += f'<span>{ico("pin")}{e(loc)}</span>'
    col = lambda names: ''.join(f'<section><h2>{n}</h2>{R[n](secs[n])}</section>' for n in names if n in secs)
    body = (f'<header><h1>{e(name)}</h1><div class="tagline">{e(tag)}</div><div class="contact">{cs}</div></header>'
            f'<div class="grid"><div>{col(LEFT)}</div><div>{col(RIGHT)}</div></div>')
    if '自傳' in secs:
        body += f'<div class="full">{col(FULL)}</div>'
    open(dst, 'w', encoding='utf8').write(
        f'<!doctype html><html lang="zh-Hant"><meta charset=utf-8><title>{e(name)}</title><style>{CSS}</style><body>{body}</body></html>')


if __name__ == '__main__':
    main()
