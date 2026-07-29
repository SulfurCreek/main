"""從三份情境檔的職缺名稱中，萃取與職位無關的雜訊文字（供人工檢核）。

類別（1與2已合併為「地區」，用 tCodeCity 官方縣市/鄉鎮區全名比對，
不使用鬆散正則，避免把「店/廠/館/處」等泛用字尾或非地名片語誤判為地區）：
  1. 地區（縣市＋鄉鎮區，含中英文，含常見短稱如「板橋」而非只有「板橋區」）
  2. 職缺編號
  3. 招募文字
  4. 招募窗口姓名
  5. 電話
  6. 廠商自己內部的職缺編號
"""
import pandas as pd, re, json
from collections import Counter

FILES = ['1_best_practice.csv', '2_enhancement.csv', '3_worst_practice.csv']
BASE = '/home/user/main/job-classification-kb/training_feedback/'
CITY_JSON = '/home/user/main/job-classification-kb/scripts/_city_district_names.json'

titles = []
for f in FILES:
    df = pd.read_csv(BASE + f, skiprows=1, dtype=str)
    titles += df['職缺名稱'].dropna().tolist()
titles = list(dict.fromkeys(titles))
print(f"不重複職缺名稱：{len(titles):,}")

city = json.load(open(CITY_JSON, encoding='utf-8'))
zh_names = sorted(set(city['zh']), key=len, reverse=True)
en_names = sorted(set(city['en']), key=len, reverse=True)
zh_rx = re.compile('|'.join(re.escape(n) for n in zh_names))
en_rx = re.compile(r'\b(?:' + '|'.join(re.escape(n) for n in en_names) + r')\b', re.IGNORECASE)

NAME_SUR = ('陳|林|黃|張|李|王|吳|劉|蔡|楊|許|鄭|謝|郭|洪|曾|邱|廖|賴|周|徐|蘇|葉|莊|呂|江|何|蕭|羅|'
            '高|潘|簡|朱|鍾|游|彭|詹|胡|施|沈|余|盧|梁|趙|顏|柯|翁|魏|孫|戴|范|方|宋|鄧|杜|傅|侯|曹|溫')

PATTERNS = [
    ('2_職缺編號', [
        r'(?:No|NO|no)[.．:：\s]*\d+', r'#\d+', r'編號[:：]?\s*\w+',
        r'\b[A-Z]{1,4}[-_]?\d{3,8}\b',
    ]),
    ('3_招募文字', [
        r'急徵|急征|誠徵|誠征|招募|徵才|徵求|求才|熱徵|大徵|快徵|速徵|徵人|應徵|招聘|補人',
        r'電洽|面洽|洽詢|洽談|來電|請洽|意洽|電話洽|預約|可議|面議',
        r'意者|意者請',
        r'立即上工|馬上上班|隨到隨上|今日面試|快速面試',
    ]),
    ('4_招募窗口姓名', [
        rf'(?:{NAME_SUR})(?:先生|小姐|經理|主任|課長|襄理|專員|姐|哥|老師|店長|副理|協理)',
        rf'洽\s*(?:{NAME_SUR})[^\s，,。]{{0,3}}',
        rf'聯絡人[:：]?\s*(?:{NAME_SUR})[^\s，,。]{{0,3}}',
    ]),
    ('5_電話', [
        r'0\d{1,3}[-\s]?\d{3,4}[-\s]?\d{3,4}',
        r'09\d{2}[-\s]?\d{3}[-\s]?\d{3}',
        r'\(0\d{1,2}\)\s?\d{3,4}[-\s]?\d{3,4}',
        r'分機\s?\d+',
    ]),
    ('6_廠商內部編號', [
        r'[（(]\s*[A-Za-z]{2,6}\s*[)）]',
        r'\b[A-Za-z]{1,4}\d{2,8}[A-Za-z]?\b',
    ]),
]

results = {}

# 地區：用官方名稱清單直接掃描（不是鬆散正則猜測）
c = Counter()
for t in titles:
    for m in zh_rx.findall(t):
        c[m] += 1
    for m in en_rx.findall(t):
        c[m] += 1
results['1_地區'] = c
print(f"1_地區: {len(c):,} 種不重複片語，總出現 {sum(c.values()):,} 次")

for cat, pats in PATTERNS:
    c = Counter()
    rx = [re.compile(p) for p in pats]
    for t in titles:
        for r in rx:
            for m in r.findall(t):
                m = m.strip() if isinstance(m, str) else m
                if m and len(m) <= 20:
                    c[m] += 1
    results[cat] = c
    print(f"{cat}: {len(c):,} 種不重複片語，總出現 {sum(c.values()):,} 次")

json.dump({k: dict(v.most_common()) for k, v in results.items()},
          open('/home/user/main/job-classification-kb/scripts/_noise_tokens.json', 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)
print("\n已存 scripts/_noise_tokens.json")
