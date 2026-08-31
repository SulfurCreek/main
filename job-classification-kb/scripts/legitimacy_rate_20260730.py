"""20260730 新模型：可疑桶的合法率計算（rawdata skill Step 4）。

合法率 = 該桶真的出現在廠商 duty0~4 的次數 / 該桶被推為新模型第1名的次數
"""
import pandas as pd

new = pd.read_pickle('/tmp/new_20260730.pkl')
duty_cols = [f'duty{i}' for i in range(5)]
new['duties'] = new[duty_cols].apply(lambda r: set(d for d in r if pd.notna(d)), axis=1)

TARGETS = ['飯店／旅館工作人員', '休閒娛樂從業人員', '售票／收銀人員', '餐廚助手',
           '資材人員', '國外業務人員', '冷熱飲調製人員', '管理員', '技術人員',
           '房務人員', '調酒師／吧台人員', '咖啡師', '不動產經紀人／營業員']

rows = []
for t in TARGETS:
    is_rank1 = new['職類推薦1'] == t
    n_rank1 = is_rank1.sum()
    if n_rank1 == 0:
        continue
    n_legit = new.loc[is_rank1, 'duties'].apply(lambda s: t in s).sum()
    rows.append((t, n_rank1, n_legit, n_legit / n_rank1))

rows.sort(key=lambda x: x[3])
print(f"{'類別':<20}{'排第1名次數':>12}{'真命中次數':>12}{'合法率':>8}")
for t, n1, nl, rate in rows:
    judge = '純誤判產物' if rate < 0.05 else ('偏誤判' if rate < 0.25 else '混合/需窄範圍' if rate < 0.6 else '合法類別')
    print(f"{t:<20}{n1:>12,}{nl:>12,}{rate:>7.1%}  {judge}")
