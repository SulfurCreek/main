"""合併規則抽取 + LLM 判定結果，輸出公司資訊文字清單 CSV（供人工檢核）。"""
import json, csv, re, collections

BASE = '/home/user/main/job-classification-kb/'
tok = json.load(open(BASE + 'scripts/_company_tokens.json', encoding='utf-8'))
labels = json.load(open(BASE + 'scripts/_company_brand_labels.json', encoding='utf-8'))
city = json.load(open(BASE + 'scripts/_city_district_names.json', encoding='utf-8'))
zh_city = set(city['zh']); en_city = {n.lower() for n in city['en']}

# 品牌清單的排除規則：地區、產業、公司屬性（已歸在 1~5 類）、通用詞
INDUSTRY = re.compile(r'半導體|電子|光電|生技|製藥|化工|機械|紡織|營建|營造|建築|土木|物流|倉儲|'
                      r'餐飲|飲料|火鍋|燒肉|咖啡|茶飲|烘焙|零售|百貨|超商|超市|金融|保險|銀行|'
                      r'證券|投信|房仲|房屋|不動產|補教|教育|補習|醫療|醫美|長照|護理|美容|美髮|'
                      r'旅遊|飯店|旅館|民宿|科技|傳產|製造|服務業|電商|遊戲|軟體|資訊|網路|汽車|'
                      r'機車|運輸|貨運|水電|工程|設計|廣告|行銷|會計|法律|人力|清潔|保全')
ATTR_WORDS = {w for k in tok['attr'] for w in tok['attr'][k]}
ATTR_RX = re.compile('|'.join(sorted((re.escape(w) for w in ATTR_WORDS), key=len, reverse=True)))
GENERIC = re.compile(r'^(?:公司|企業|本公司|該公司|集團|總部|門市|門店|分店|店舖|店|廠|部|處|課|組|中心|'
                     r'菁英|精英|團隊|事業處|事業部|金控|股份|實業|國際|開發|控股|旗艦|台灣|全台)$')
# 「高雄分公司」被切成「高雄分」這類殘片
FRAGMENT = re.compile(r'^.{1,3}分$|^.{0,2}(?:著名|知名)')


def is_brand(w):
    """排除地區/產業/公司屬性/通用詞後才算品牌名。"""
    if len(w) < 2:
        return False
    if w in zh_city or w.lower() in en_city:
        return False
    if INDUSTRY.search(w) or ATTR_RX.search(w) or GENERIC.match(w) or FRAGMENT.match(w):
        return False
    return True

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
    if labels.get(w) == '品牌' and is_brand(w):
        brand[w] += n
for w, n in tok['corp'].items():
    if is_brand(w):
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
