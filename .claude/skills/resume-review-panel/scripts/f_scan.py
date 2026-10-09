#!/usr/bin/env python3
"""6 秒 F 型掃描模擬（resume-review-panel 驗證機制 v3.1，項目 3）。

依 career/style/hr-6-second-source.md：招募者初篩 6–10 秒，視線走 F／E 型、集中在左緣，
先找「最近職稱、目前公司、起訖日期」。本腳本做兩件事：

1. 產生「F 型視野」：第一屏上方幾行看全句，之後每行只看左緣幾個字。
   這份視野交給另一個模型做 6 秒初篩（只看得到招募者眼睛真的掃到的字）。
2. 結構檢查：抬頭是否職稱在左、日期是否落在視野內、摘要是否寫成求職目標、
   條列左緣有沒有結果或關鍵詞、職責式開頭、與職缺無關的舊經歷。

用法：
  python3 f_scan.py <resume.txt> [--jd "PRD,UAT,..."] [--view-only]
      [--top 3] [--header-chars 24] [--edge 10] [--page-chars 1400] [--stale-years 10]
"""
import argparse, re, datetime

DATE = re.compile(r'(\d{4})/(\d{1,2})\s*[-–~至]\s*(?:(\d{4})/(\d{1,2})|迄今|至今|Present)')
NUM = re.compile(r'\d')
TITLE_WORDS = ['經理', 'Manager', 'PM', 'Owner', '主任', '企劃', '工程師', '專員', '工讀生', 'Intern',
               'Lead', 'Director', '總監', '主管', '顧問', 'Analyst', '分析師', '設計師', 'Designer']
OBJECTIVE = ['希望', '尋求', '期望', '追求', '挑戰性', '發揮所長', '貢獻所學', '學習成長', 'Seeking', 'Objective',
             'objective', 'looking for']
DUTY_START = re.compile(r'^(主責|負責|職責|協助|參與|處理|管理|Responsible|Managed|Worked|Assisted|Helped)')
RESULT_VERB = ['主導', '上線', '降到', '提升', '成長', '從 0 到 1', '0 到 1', '→', '縮短', '增加', '減少']


def kw_list(s):
    return [k.strip() for k in (s or '').split(',') if k.strip()]


def has_any(text, words):
    t = text.lower()
    return [w for w in words if w.lower() in t]


def sections(lines):
    """回傳 (工作經歷起訖 index, 摘要行)；找不到標題就用全文。"""
    start, end = 0, len(lines)
    summ = []
    for i, l in enumerate(lines):
        s = l.strip()
        if s in ('工作經歷', 'Professional Experience', 'Experience'):
            start = i
        if s in ('學歷', 'Education') and i > start:
            end = i
            break
    for i, l in enumerate(lines):
        if l.strip() in ('專業摘要', 'Summary', 'Professional Summary'):
            j = i + 1
            while j < len(lines) and lines[j].strip() and lines[j].strip() not in ('工作經歷',):
                summ.append(lines[j].strip()); j += 1
            break
    return start, end, summ


def f_view(lines, top, header_chars, edge, page_chars):
    out, used, shown = [], 0, 0
    for l in lines:
        s = l.rstrip()
        if not s.strip():
            continue
        if used >= page_chars:
            out.append('〔第一屏結束〕')
            break
        if shown < top:
            v = s[:80]
        elif DATE.search(s) and '｜' in s:
            v = s[:header_chars]
        else:
            v = s[:edge]
        out.append(v + ('…' if len(v) < len(s) else ''))
        used += len(s)
        shown += 1
    return out


def years(lines, start, end):
    now = datetime.date.today()
    total, spans = 0.0, []
    for l in lines[start:end]:
        m = DATE.search(l)
        if not m or '｜' not in l:
            continue
        y1, m1 = int(m.group(1)), int(m.group(2))
        y2, m2 = (int(m.group(3)), int(m.group(4))) if m.group(3) else (now.year, now.month)
        spans.append((l.strip(), y1, m1, y2, m2))
        total += (y2 - y1) + (m2 - m1) / 12
    return total, spans


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('path')
    ap.add_argument('--jd', default='')
    ap.add_argument('--view-only', action='store_true')
    ap.add_argument('--top', type=int, default=3)
    ap.add_argument('--header-chars', type=int, default=24)
    ap.add_argument('--edge', type=int, default=10)
    ap.add_argument('--page-chars', type=int, default=1400)
    ap.add_argument('--stale-years', type=int, default=10)
    a = ap.parse_args()
    jd = kw_list(a.jd)
    lines = open(a.path, encoding='utf8').read().split('\n')
    view = f_view(lines, a.top, a.header_chars, a.edge, a.page_chars)
    if a.view_only:
        print('\n'.join(view))
        return

    start, end, summ = sections(lines)
    total, spans = years(lines, start, end)
    bullets = [l.strip()[2:] for l in lines[start:end] if l.strip().startswith('- ')]
    first = [l.strip() for l in lines if l.strip()][:a.top]

    print('## F 型視野（交給初篩模型的版本）\n')
    print('```text\n' + '\n'.join(view) + '\n```\n')
    print('## 結構檢查\n')
    print('| 項目 | 結果 | 說明 |')
    print('| :--- | :-: | :--- |')
    t_top = has_any(' '.join(first), TITLE_WORDS)
    print(f'| 前 {a.top} 行看得到職稱 | {"✅" if t_top else "❌"} | {"、".join(t_top) or "無"} |')
    obj = has_any(' '.join(summ), OBJECTIVE)
    print(f'| 摘要不是求職目標 | {"✅" if not obj else "❌"} | {("命中：" + "、".join(obj)) if obj else "摘要 " + str(len(summ)) + " 段"} |')
    now = datetime.date.today().year
    for h, y1, m1, y2, m2 in spans:
        head = h.split('｜')[0]
        title_first = bool(has_any(head, TITLE_WORDS))
        m = DATE.search(h)
        date_vis = m.start() < a.header_chars
        stale = y2 < now - a.stale_years and not has_any(h, jd) and not has_any(h, ['PM', 'Product', '產品'])
        notes = []
        if not title_first: notes.append('左緣是公司不是職稱')
        if not date_vis: notes.append(f'起訖在第 {m.start()} 字，超出 {a.header_chars} 字視野')
        if stale: notes.append(f'{y2} 年結束、與職缺無關：可刪候選')
        ok = title_first and date_vis and not stale
        print(f'| 抬頭：{h[:30]} | {"✅" if ok else "⚠️"} | {"；".join(notes) or "職稱在左、日期可見"} |')
    if bullets:
        edge_ok = [b for b in bullets if NUM.search(b[:a.edge]) or has_any(b[:a.edge], jd + RESULT_VERB)]
        duty = [b for b in bullets if DUTY_START.match(b)]
        print(f'| 條列左緣 {a.edge} 字有結果或關鍵詞 | {len(edge_ok)}/{len(bullets)} | 目標 ≥ 60% |')
        print(f'| 職責式開頭 | {len(duty)}/{len(bullets)} | {"；".join(d[:16] for d in duty) or "無"} |')
    scope = [l.strip() for l in lines[start:end] if DUTY_START.match(l.strip())]
    if scope:
        print(f'| 範圍行以職責開頭 | ⚠️ | {"；".join(s[:20] for s in scope)} |')
    print(f'| 可推算年資 | {total:.1f} 年 | 由 {len(spans)} 段抬頭日期加總（含工讀） |')


if __name__ == '__main__':
    main()
