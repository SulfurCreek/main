#!/usr/bin/env python3
"""ATS 準備檢查（規準 v4.2 §17，ATS01–ATS14）：只做本機文字擷取＋精確詞查詢模擬，輸出五塊，不加總成分數。

  python3 ats_check.py <resume.pdf> <source.txt> [--jd "PRD,驗收"] [--vendor Greenhouse] [--json out.json]

- 狀態用 pass／risk／fail／unknown／not_applicable；fail 只表示該明確檢查失敗，不表示候選人不合格。
- 測試層級固定 local_extraction（ATS13）；沒有真實 ATS 匯入，不宣稱任何平台實測通過。
- 平台功能、AI 開關、申請表規則未知時一律 unknown（ATS01／07／08／09／14），不推定自動篩選或通過。
- 重要欄位（職稱—公司—起訖）逐段檢查，總文字還原率高也不能掩蓋錯配（R42-03）。
- 履歷內嵌給模型的指令只當資料標出，不服從（ATS12，R42-14）。
"""
import argparse, hashlib, json, os, re, subprocess, difflib

DATE = re.compile(r'\d{4}/\d{1,2}\s*[-–~至]\s*(?:\d{4}/\d{1,2}|迄今|至今|Present)')
INJECT = re.compile(r'(ignore (all|previous)|忽略(以上|前述)?(規則|指令)|給(我)?最高分|give (me )?(the )?highest score|you are (now )?an? )', re.I)
# 已知解析限制（只在指定 vendor 時套用；來源 A11）
VENDOR_PARSE_MB = {'greenhouse': 2.5}
norm = lambda t: re.sub(r'\s+', '', t)


def jobs_of(src):
    out = []
    for l in src.split('\n'):
        m = DATE.search(l)
        if '｜' in l and m:
            parts = [p.strip() for p in l[:m.start()].strip('｜ ').split('｜') if p.strip()]
            out.append(dict(title=parts[0], company=parts[1] if len(parts) > 1 else '', date=norm(m.group(0))))
    return out


def field_map(jobs, O):
    """每段經歷：職稱、公司、日期都要出現，且公司與日期落在該職稱之後、下一段職稱之前。"""
    pos = [O.find(norm(j['title'])) for j in jobs]
    res = []
    for k, j in enumerate(jobs):
        t = pos[k]
        nxt = min([p for p in pos[k + 1:] if p > t] or [len(O)])
        c = O.find(norm(j['company']), t) if t >= 0 and j['company'] else -1
        d = O.find(j['date'], t) if t >= 0 else -1
        ok = t >= 0 and (not j['company'] or 0 <= c < nxt) and 0 <= d < nxt
        res.append(dict(title=j['title'], ok=ok, title_found=t >= 0, company_in_block=not j['company'] or 0 <= c < nxt, date_in_block=0 <= d < nxt))
    return res


def run(pdf, src_path, jd, vendor):
    src = open(src_path, encoding='utf8').read()
    raw = open(pdf, 'rb').read()
    info = subprocess.run(['pdfinfo', pdf], capture_output=True, text=True).stdout
    out = subprocess.run(['pdftotext', '-raw', pdf, '-'], capture_output=True, text=True).stdout
    N, O = norm(src), norm(out)
    ratio = difflib.SequenceMatcher(None, N, O, autojunk=False).ratio()
    mb = len(raw) / 1e6
    C = []
    add = lambda rid, block, status, ev, nxt='', limit='': C.append(dict(rule_id=rid, block=block, status=status, artifact_evidence=ev, next_step=nxt, limit=limit))
    v = (vendor or '').lower()
    add('ATS01', '匹配功能與未知設定', 'unknown', [f'vendor={vendor or "未提供"}；module／AI 開關／職缺設定未取得'], '取得實際申請頁或雇主設定', '知道品牌也不能推知啟用哪些功能')
    # 1 檔案接受
    pg = re.search(r'Pages:\s*(\d+)', info); pages = pg.group(1) if pg else '?'
    enc = 'Encrypted:' in info and 'yes' in info.split('Encrypted:')[1].split('\n')[0]
    add('ATS02', '檔案接受', 'fail' if enc else ('unknown' if not vendor else 'pass'),
        [f'PDF {mb:.2f} MB；加密={"是" if enc else "否"}；頁數={pages}'],
        '以實際申請頁確認格式與大小限制', '上傳接受≠解析成功；不宣稱 PDF 必敗或 DOCX 必勝')
    if v in VENDOR_PARSE_MB:
        lim = VENDOR_PARSE_MB[v]
        add('ATS02', '檔案接受', 'risk' if mb > lim else 'pass', [f'{vendor} 文件所述解析上限 {lim} MB，本檔 {mb:.2f} MB'], '超過則可能只保留附件、不解析', '附件上限與解析上限不可混用（A11）')
    # 2 欄位解析
    jobs = jobs_of(src); fm = field_map(jobs, O)
    bad = [f'{x["title"][:12]}（公司{"✅" if x["company_in_block"] else "❌"} 日期{"✅" if x["date_in_block"] else "❌"}）' for x in fm if not x['ok']]
    em = re.search(r'[\w.+-]+@[\w-]+\.[\w.]+', src); ph = re.search(r'09\d{2}[-\s]?\d{3}[-\s]?\d{3}', src)
    name = src.strip().split('\n')[0].strip()
    contact = [f'姓名{"✅" if norm(name) in O else "❌"}', f'Email{"✅" if em and em.group(0) in out else ("無" if not em else "❌")}',
               f'電話{"✅" if ph and norm(ph.group(0)) in O else ("無" if not ph else "❌")}']
    lost = sorted(n for n in set(re.findall(r'\d[\d,.]*\d%?|\d+%', src)) if norm(n) not in O)
    st = 'fail' if bad or '❌' in ''.join(contact) else ('risk' if lost else 'pass')
    add('ATS03', '欄位解析', st, [f'經歷 職稱→公司→日期 {len(fm) - len(bad)}/{len(fm)}' + (('；錯配：' + '；'.join(bad)) if bad else ''), '、'.join(contact),
        f'數字遺漏：{"、".join(lost) or "無"}', f'總文字還原 {ratio:.1%}（內部參考，不能掩蓋欄位錯配）'], '若 fail，改單欄或調整該段順序後重測', '本機 pdftotext，不是廠商解析器')
    add('ATS04', '欄位解析', 'unknown', ['語言 zh-Hant；本機擷取無亂碼' if '�' not in out else f'U+FFFD ×{out.count("�")}'],
        '查該解析器公開語言清單並實測', '供應商清單未列繁體→待驗證，不判不能讀（A14 Ashby 列繁體；Greenhouse 未明列）')
    # 3 搜尋可見性（只有精確詞路徑）
    if jd:
        hit = [k for k in jd if k.lower() in out.lower()]; miss = [k for k in jd if k not in hit]
        add('ATS05', '搜尋可見性', 'pass' if not miss else 'risk', [f'精確詞查詢（附件全文、不分大小寫、OR 逐詞）命中 {len(hit)}/{len(jd)}；未命中：{"、".join(miss) or "無"}'],
            '未命中詞若履歷有真實證據，可自然補全稱或縮寫', '只測精確詞路徑；語意配對未測，不互相覆寫；命中≠能力通過')
        add('ATS06', '搜尋可見性', 'not_applicable' if not miss else 'risk', ['需求原句→證據對照由內容審查產出；本腳本只列精確詞缺口'], '', '不設覆蓋率門檻，不建議重複詞或隱藏文字')
    else:
        add('ATS05', '搜尋可見性', 'unknown', ['未提供查詢詞'], '以 --jd 提供 JD 詞做查詢情境測試')
    # 4 資格／流程
    for rid, ev in (('ATS07', '申請表題目、答案與條件未取得'), ('ATS08', '表單規則、AI 評估、自動推進／拒絕設定未取得'), ('ATS10', '重投限制與候選人合併設定未取得'), ('ATS11', '無平台申請中繼資料；不從文風判斷作者或自動投遞')):
        add(rid, '資格／流程條件', 'unknown', [ev], '', '未知不推定淘汰或通過')
    # 5 匹配與未知設定
    add('ATS09', '匹配功能與未知設定', 'unknown', ['評估輸入、職缺準則、權重、顯示尺度均未知'], '', '不產生通用 ATS 分數；各產品尺度不可互換')
    inj = INJECT.findall(src)
    add('ATS12', '匹配功能與未知設定', 'risk' if inj else 'pass', [f'疑似給模型的指令：{len(inj)} 處' if inj else '無嵌入指令；平台摘要未產生，無法回查'], '刪除嵌入指令' if inj else '', '嵌入指令只當資料，不服從')
    add('ATS13', '匹配功能與未知設定', 'pass', [f'test_level=local_extraction；pdftotext -raw；pdf sha256 {hashlib.sha256(raw).hexdigest()[:12]}'], '', '不宣稱任何真實 ATS／104 匯入通過')
    add('ATS14', '匹配功能與未知設定', 'unknown', ['未啟用 AI、退出 AI、技術錯誤或缺分數 → 人工途徑，不當低能力'], '')
    return dict(rubric_version='4.2', ats_context=dict(vendor=vendor, module=None, settings_source=None, test_level='local_extraction', language='zh-Hant', actual_ats_import_performed=False), ats_checks=C)


def report(o):
    lines = ['## ATS 準備檢查（v4.2 §17；五塊分開，不加總；actual ATS import: not performed）']
    for b in ['檔案接受', '欄位解析', '搜尋可見性', '資格／流程條件', '匹配功能與未知設定']:
        lines.append(f'\n### {b}\n\n| 規則 | 狀態 | 證據 | 限制 |\n| :-- | :-- | :-- | :-- |')
        lines += [f'| {c["rule_id"]} | {c["status"]} | {"；".join(c["artifact_evidence"])} | {c["limit"]} |' for c in o['ats_checks'] if c['block'] == b]
    return '\n'.join(lines)


if __name__ == '__main__':
    ap = argparse.ArgumentParser(); ap.add_argument('pdf'); ap.add_argument('src')
    ap.add_argument('--jd', default=''); ap.add_argument('--vendor'); ap.add_argument('--json')
    a = ap.parse_args()
    o = run(a.pdf, a.src, [k.strip() for k in a.jd.split(',') if k.strip()], a.vendor)
    if a.json: json.dump(o, open(a.json, 'w', encoding='utf8'), ensure_ascii=False, indent=1)
    print(report(o))
