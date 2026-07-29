"""合併規則抽取 + LLM 判定結果，輸出公司資訊文字清單 CSV（供人工檢核）。"""
import json, csv, re, collections

BASE = '/home/user/main/job-classification-kb/'
tok = json.load(open(BASE + 'scripts/_company_tokens.json', encoding='utf-8'))
labels = json.load(open(BASE + 'scripts/_company_brand_labels.json', encoding='utf-8'))

CAT = {
    '外資國別': '1_外資國別',
    '上市櫃': '2_上市櫃',
    '法人型態': '3_法人型態',
    '組織關係': '4_組織關係',
    '規模形容': '5_規模形容',
}

rows = []
for k, cat in CAT.items():
    for w, n in tok['attr'][k].items():
        rows.append((cat, w, n))

# 6_公司品牌名稱：括號候選中被判為「品牌」者 ＋ 法人後綴抽出的專名
brand = collections.Counter()
for w, n in tok['brand_candidates'].items():
    if labels.get(w) == '品牌':
        brand[w] += n
for w, n in tok['corp'].items():
    brand[w] += n
for w, n in brand.most_common():
    rows.append(('6_公司品牌名稱', w, n))

order = {c: i for i, c in enumerate(
    ['1_外資國別', '2_上市櫃', '3_法人型態', '4_組織關係', '5_規模形容', '6_公司品牌名稱'])}
rows.sort(key=lambda r: (order[r[0]], -r[2]))

out = BASE + 'analysis_職缺名稱公司資訊清單.csv'
with open(out, 'w', encoding='utf-8-sig', newline='') as f:
    w = csv.writer(f)
    w.writerow(['類別', '公司相關文字', '出現次數'])
    w.writerows(rows)

c = collections.Counter(r[0] for r in rows)
s = collections.Counter()
for cat, _, n in rows:
    s[cat] += n
for k in sorted(c):
    print(f"{k}: {c[k]:,} 種 / {s[k]:,} 次")
print(f"\n共 {len(rows):,} 列 → {out}")
