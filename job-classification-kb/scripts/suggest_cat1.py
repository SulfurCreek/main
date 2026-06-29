"""
suggest_cat1.py — 只評估「職類1（現有1）是否正確」的高精準度建議器。

設計：依職缺名稱的 function-tail 關鍵字，對照 tCodeDutyNM 合法葉名，
推出該職缺的主職類期望值；若與現有1 不同 → 建議改現有1。
精準優先（寧缺勿濫）：只在關鍵字明確命中時建議，模糊則不動。

用法:
  python3 scripts/suggest_cat1.py            # 印彙整 + 寫 cat1_suggestions.json
  python3 scripts/suggest_cat1.py --md       # 另存 cat1_suggestions.md
依賴: TCode_Export.xlsx, 不合理清單_職類校正.xlsx（皆在 KB 根目錄）
"""
import sys, re, json, warnings; warnings.filterwarnings('ignore')
import openpyxl
from collections import Counter

KB_XLSX = '不合理清單_職類校正.xlsx'
TCODE   = 'TCode_Export.xlsx'

def valid_leaves():
    wb = openpyxl.load_workbook(TCODE, read_only=True); ws = wb['tCodeDutyNM']
    rows = list(ws.iter_rows(min_row=1, values_only=True)); wb.close()
    hdr = [str(c) if c else '' for c in rows[0]]; idx = {h: i for i, h in enumerate(hdr)}
    return {r[idx['CodeNameA']] for r in rows[1:] if str(r[idx['CodeType']]) == '3'}

# function-tail 關鍵字 → 合法葉名（最具體者排前；命中即停）
RULES = [
    (r'主管司機|隨扈|隨身司機',                         '主管駕駛'),
    (r'產品經理|遊戲營運\s*PM|營運\s*PM|產品\s*PM|(?<![A-Za-z])PM(?![A-Za-z])', '產品經理'),
    (r'專案經理|專案副理',                              '專案經理'),
    (r'儲備幹部|管理儲備|儲備主管|儲備店長|儲備',        '儲備幹部'),
    (r'業務助理|業務行政助理|業助',                      '業務助理'),
    (r'國外業務|外銷業務|貿易業務|海外業務',            '國外業務人員'),
    (r'業務主管|業務經理|業務副理|業務襄理',            '國內業務主管'),
    (r'業務專員|業務代表|業務人員|門市業務|電話行銷|電銷', '國內業務人員'),
    (r'客服|客戶服務|客戶關係',                          '客服人員'),
    (r'會計主管|財務主管|財會主管',                      '財務／會計主管'),
    (r'會計|記帳|出納',                                  '會計／出納／記帳人員'),
    (r'總務',                                            '總務人員'),
    (r'採購|資材',                                       '採購人員'),
    (r'倉管|倉儲|物料管理|庫管',                          '倉管／物料管理員'),
    (r'保全|警衛|駐衛',                                  '保全人員／警衛'),
    (r'清潔|環保清潔|環境清潔|清潔隊',                   '清潔／資源回收人員'),
    (r'居家服務|居服|照服|照顧服務|照顧員',              '照顧服務／指導員'),
    (r'護理師|護士',                                     '護理師'),
    (r'教育訓練|教育訓練專員|訓練專員',                  '教育訓練人員'),
]

GENERIC_PARTS = {'人員', '專員', '助理', '主管', '幹部'}

def cur1_matches_title(cur1, title):
    """現有1 是否已對上職缺名稱（擦邊保留：對上就不動）。"""
    t = (title or '').replace('／', '/').replace('台', '檯')
    c = (cur1 or '').replace('／', '/').replace('台', '檯')
    if not c:
        return False
    if c in t:
        return True
    for part in c.split('/'):
        if len(part) >= 2 and part not in GENERIC_PARTS and part in t:
            return True
    return False

def suggest(title, cur1, VALID):
    # 擦邊保留：現有1 已對上職缺名稱 → 不建議改
    if cur1_matches_title(cur1, title):
        return None
    t = (title or '').replace('／', '/')
    for pat, leaf in RULES:
        if re.search(pat, t):
            return leaf if leaf in VALID else None
    return None

def main():
    VALID = valid_leaves()
    wb = openpyxl.load_workbook(KB_XLSX, read_only=True); ws = wb['不合理清單']
    data = list(ws.iter_rows(min_row=2, values_only=True)); wb.close()
    out = []
    for ridx, r in enumerate(data, start=2):  # excel row number
        eno, title, cur1 = r[5], r[6], (r[7] or '')
        s = suggest(title, cur1, VALID)
        if s and s != cur1:
            out.append({'row': ridx, 'eNo': eno, 'title': title, 'cur1': cur1, 'suggest1': s})
    json.dump(out, open('cat1_suggestions.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    # aggregate report only (token-min)
    print(f'評估列數: {len(data)}　|　現有1 建議修改: {len(out)}')
    print('\nTop 現有1 → 建議1 變更類型:')
    for (a, b), n in Counter((o['cur1'], o['suggest1']) for o in out).most_common(20):
        print(f'  {n:>4}  {a}  →  {b}')
    if '--md' in sys.argv:
        with open('cat1_suggestions.md', 'w', encoding='utf-8') as f:
            f.write('# 職類1 建議修改清單\n\n| 職缺編號 | 職缺名稱 | 現有1 | 建議1 |\n|---|---|---|---|\n')
            for o in out:
                f.write(f"| {o['eNo']} | {o['title']} | {o['cur1']} | {o['suggest1']} |\n")
        print('→ cat1_suggestions.md')

if __name__ == '__main__':
    main()
