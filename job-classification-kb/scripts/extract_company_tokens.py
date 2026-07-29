"""從職缺名稱中萃取「透露公司名稱／公司屬性」的文字（供人工檢核）。

與 extract_noise_tokens.py 的差別：那支抓地區/編號/電話等雜訊，
這支專抓「公司身分」相關文字——公司屬性（德商、上市、集團…）與公司/品牌名稱。

註：產業相關文字（半導體、物流、餐飲…）不列入，依需求排除。

階段一（本檔）：規則可枚舉的公司屬性 + 品牌名候選抽取（結構線索）。
階段二：候選交由 LLM 分類（見 classify_company_candidates.py）。
"""
import re, json, collections

MD = '/home/user/main/job-classification-kb/tcode/data_職缺名稱_dutyMapping.md'
CITY_JSON = '/home/user/main/job-classification-kb/scripts/_city_district_names.json'
OUT = '/home/user/main/job-classification-kb/scripts/_company_tokens.json'

names = set()
for l in open(MD, encoding='utf-8'):
    if l.startswith('| '):
        n = l.split('|')[1].strip()
        if n and n != '職缺名稱':
            names.add(n)
names = sorted(names)
print(f"不重複職缺名稱：{len(names):,}")

# ── 1. 公司屬性（規則可枚舉，高信心）────────────────────────────
ATTR = [
    ('外資國別', r'(?:[美日德法英韓港星荷瑞義澳加台陸新泰馬印越西丹挪芬俄以土巴墨阿中]商)'),
    ('上市櫃',   r'(?:股票上市|上市公司|上市櫃|上市|上櫃|興櫃)'),
    ('法人型態', r'(?:股份有限公司|有限公司|企業社|商行|工作室|事務所|控股|集團)'),
    ('組織關係', r'(?:總公司|分公司|子公司|關係企業|旗下|直營|加盟店|加盟|連鎖|總部|本社)'),
    ('規模形容', r'(?:世界500大|五百大|千大企業|國際級|跨國|知名|老字號|百年企業|百年老店|龍頭|大廠|原廠|績優|優良企業|新創|獨角獸|外商)'),
]

# ── 2. 公司／品牌名稱候選（結構線索）────────────────────────────
# 2a 法人後綴前的專名：「XX股份有限公司」「XX集團」
CORP_NAME = re.compile(r'([一-鿿A-Za-z0-9]{2,10})(?:股份有限公司|有限公司|企業社|集團|控股|事務所)')
# 2b 括號類前綴內容（【】〔〕[]（）等）
BRACKET = re.compile(r'[【\[［〖〔]([^】\]］〗〕]{1,20})[】\]］〗〕]')

city = json.load(open(CITY_JSON, encoding='utf-8'))
zh_city = set(city['zh']); en_city = set(n.lower() for n in city['en'])

# 括號內容若命中以下性質，就不是公司名，濾掉
DROP_RX = re.compile(
    r'^(?:\d+|[A-Za-z]?\d+[A-Za-z]?)$'                       # 純編號
    r'|急徵|誠徵|徵才|招募|徵人|應徵|招聘|徵$|電洽|面洽|洽詢|來電|面議|可議'
    r'|兼職|正職|全職|工讀|時薪|月薪|年薪|獎金|薪|待遇|福利|保障'
    r'|早班|晚班|夜班|中班|大夜|小夜|班$|週休|做四休|彈性|時段|排班|工時'
    r'|經驗|無經驗|新鮮人|可|歡迎|培訓|長期|短期|急|限|需|意者'
    r'|人員$|助理$|專員$|工程師$|主任$|經理$|店長$|幹部$|司機$|技師$|業務$'
)
INDUSTRY = re.compile(r'半導體|電子|光電|生技|製藥|化工|機械|紡織|營建|建築|物流|倉儲|餐飲|飲料|零售|百貨|金融|保險|銀行|證券|房仲|房屋|補教|教育|醫療|診所|長照|美容|美髮|旅遊|飯店|旅館|科技業|傳產|製造業|服務業|電商|遊戲|軟體|資訊')

attr_counter = {k: collections.Counter() for k, _ in ATTR}
attr_rx = [(k, re.compile(p)) for k, p in ATTR]
corp_counter = collections.Counter()
brand_cand = collections.Counter()

for n in names:
    for k, rx in attr_rx:
        for m in rx.findall(n):
            attr_counter[k][m] += 1
    for m in CORP_NAME.findall(n):
        corp_counter[m] += 1
    for m in BRACKET.findall(n):
        t = m.strip()
        if not t or len(t) > 20:
            continue
        if t in zh_city or t.lower() in en_city:
            continue
        if DROP_RX.search(t) or INDUSTRY.search(t):
            continue
        brand_cand[t] += 1

for k, c in attr_counter.items():
    print(f"公司屬性/{k}: {len(c)} 種，{sum(c.values()):,} 次")
print(f"法人全名專名: {len(corp_counter):,} 種，{sum(corp_counter.values()):,} 次")
print(f"括號品牌候選: {len(brand_cand):,} 種，{sum(brand_cand.values()):,} 次（待 LLM 判定）")

json.dump({
    'attr': {k: dict(v.most_common()) for k, v in attr_counter.items()},
    'corp': dict(corp_counter.most_common()),
    'brand_candidates': dict(brand_cand.most_common()),
}, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(f"\n已存 {OUT}")
