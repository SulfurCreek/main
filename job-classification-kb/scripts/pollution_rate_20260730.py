"""20260720→20260730 退步案例的污染率分析（rawdata skill Step 3）。

污染率 = 退步進來的筆數 / (救回進來的筆數 + 退步進來的筆數)，
以「新模型推薦第1名」分組。
"""
import pandas as pd

sub = pd.read_pickle('/tmp/paired_20260720_to_20260730.pkl')
new_rec_cols = [c for c in sub.columns if c.endswith('_new')]
new_rec1_col = [c for c in new_rec_cols if '職類推薦1_' in c][0]

rescued = sub[(sub['old_scenario'] == 'worst') & (sub['new_scenario'] != 'worst')].copy()
regressed = sub[(sub['old_scenario'] != 'worst') & (sub['new_scenario'] == 'worst')].copy()

rescued['bucket'] = rescued[new_rec1_col]
regressed['bucket'] = regressed[new_rec_cols[0]]  # regressed→worst時第1名必為duty沒命中的桶

r_cnt = rescued['bucket'].value_counts()
g_cnt = regressed['bucket'].value_counts()

buckets = set(r_cnt.index) | set(g_cnt.index)
rows = []
for b in buckets:
    r, g = r_cnt.get(b, 0), g_cnt.get(b, 0)
    if r + g < 20:
        continue
    rows.append((b, r, g, g / (r + g)))

rows.sort(key=lambda x: -x[3])
print(f"{'桶（新推薦第1名）':<20}{'救回':>8}{'退步':>8}{'污染率':>8}")
for b, r, g, p in rows[:40]:
    flag = ' ⚠️' if p > 0.3 else ''
    print(f"{b:<20}{r:>8,}{g:>8,}{p:>7.1%}{flag}")

print(f"\n>30% 污染率的桶數: {sum(1 for *_, p in rows if p > 0.3)} / {len(rows)}")

import json
json.dump([{'bucket': b, 'rescued': r, 'regressed': g, 'pollution_rate': p} for b, r, g, p in rows],
          open('/tmp/pollution_20260730.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
