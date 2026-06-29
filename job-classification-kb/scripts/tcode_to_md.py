"""
tcode_to_md.py — 把任一 tCode 表轉成可讀 MD（依大類>中類分組）

用法:
  python3 tcode_to_md.py tCodeDutyNM              # 完整輸出
  python3 tcode_to_md.py tCodeCertify --summary   # 只輸出中類層級摘要（大表建議）
  python3 tcode_to_md.py tCodeDutyNM --out NM.md

設計原則: 先偵察結構(CodeType分布)，抽葉，依大類>中類分組，不 dump 全表。
"""
import sys, openpyxl, warnings
from collections import defaultdict, Counter
warnings.filterwarnings('ignore')

TCODE_PATH = 'TCode_Export_20260622.xlsx'   # 移轉時改路徑

def load_sheet(sheet):
    wb = openpyxl.load_workbook(TCODE_PATH, read_only=True)
    ws = wb[sheet]
    rows = list(ws.iter_rows(min_row=1, values_only=True))
    wb.close()
    hdr = [str(c) if c is not None else '' for c in rows[0]]
    idx = {h: i for i, h in enumerate(hdr)}
    return hdr, idx, rows[1:]

def build_tree(idx, data):
    ct = Counter(str(r[idx['CodeType']]) for r in data if r[idx['CodeType']] is not None)
    leaf = max((t for t in ct if t.isdigit()), key=int)
    a = idx.get('CodeNameA'); b = idx.get('CodeNameB'); c = idx.get('CodeNameC')
    has_c = c is not None and any(r[c] for r in data)
    tree = defaultdict(lambda: defaultdict(list))
    for r in data:
        if str(r[idx['CodeType']]) == leaf:
            big = str(r[c]) if has_c and r[c] else '(無大類)'
            mid = str(r[b]) if b is not None and r[b] else '(無中類)'
            tree[big][mid].append(str(r[a]))
    return tree, leaf, dict(ct)

def to_md(sheet, summary=False):
    hdr, idx, data = load_sheet(sheet)
    tree, leaf, ct = build_tree(idx, data)
    n_leaf = sum(len(v) for m in tree.values() for v in m.values())
    lines = [f'# {sheet} 代碼表\n',
             f'\n> 葉 CodeType={leaf} | CodeType分布={ct} | 共 {n_leaf} 葉 / {len(tree)} 大類\n']
    for big in sorted(tree):
        mids = tree[big]
        total = sum(len(v) for v in mids.values())
        lines.append(f'\n## {big}（{total}）\n')
        for mid in sorted(mids):
            items = mids[mid]
            if summary:
                lines.append(f'- **{mid}**：{len(items)} 葉\n')
            else:
                lines.append(f'- **{mid}**（{len(items)}）：{"、".join(items)}\n')
    return ''.join(lines)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(0)
    sheet = sys.argv[1]
    summary = '--summary' in sys.argv
    out = None
    if '--out' in sys.argv:
        out = sys.argv[sys.argv.index('--out') + 1]
    md = to_md(sheet, summary)
    if out:
        open(out, 'w', encoding='utf-8').write(md)
        print(f'Written {out}')
    else:
        print(md)
