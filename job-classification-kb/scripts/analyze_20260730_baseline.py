"""20260730 新母體樣本：基準指標計算（rawdata skill Step 1）。

真命中率＝前5名以內；三情境（best/enhancement/worst）互斥判定。
"""
import pandas as pd, numpy as np

df = pd.read_pickle('/tmp/new_20260730.pkl')
n_total = len(df)

duty_cols = [f'duty{i}' for i in range(5)]
rec_cols = [f'職類推薦{i}' for i in range(1, 11)]

df['duties'] = df[duty_cols].apply(lambda r: [d for d in r if pd.notna(d)], axis=1)
df['recs'] = df[rec_cols].apply(lambda r: [d for d in r if pd.notna(d)], axis=1)

def classify(row):
    duties, recs = row['duties'], row['recs']
    if not duties:
        return None
    top5, rank6_10 = recs[:5], recs[5:10]
    hit5 = set(top5) & set(duties)
    hit10_extra = set(rank6_10) & set(duties)
    n_duty = len(duties)
    if recs and recs[0] in duties and len(hit5) == n_duty:
        return 'best'
    if not hit5 and hit10_extra:
        return 'enhancement'
    if not hit5 and not hit10_extra:
        return 'worst'
    return 'other'

df['scenario'] = df.apply(classify, axis=1)
valid = df[df['scenario'].notna()]
n_valid = len(valid)
print(f"總筆數 {n_total:,}（duty 全空排除 {n_total - n_valid:,}，有效 {n_valid:,}）")

dist = valid['scenario'].value_counts()
for k in ['best', 'enhancement', 'worst', 'other']:
    v = dist.get(k, 0)
    print(f"  {k:<12}{v:>10,}  {v/n_valid:>7.1%}")

# 真命中率＝前5名內任一 duty 命中（含 best + other 的部分命中 + enhancement 不算，worst 不算）
def hit5(row):
    return bool(set(row['recs'][:5]) & set(row['duties']))

valid = valid.copy()
valid['hit5'] = valid.apply(hit5, axis=1)
print(f"\n真命中率（前5名內）: {valid['hit5'].mean():.1%}")

# 第1名就命中
def first_hit(row):
    return bool(row['recs']) and row['recs'][0] in row['duties']
valid['first_hit'] = valid.apply(first_hit, axis=1)
print(f"第1名就命中: {valid['first_hit'].mean():.1%}")

# 前5名平均覆蓋率
def coverage(row):
    if not row['duties']:
        return np.nan
    return len(set(row['recs'][:5]) & set(row['duties'])) / len(row['duties'])
valid['coverage'] = valid.apply(coverage, axis=1)
print(f"前5名平均覆蓋廠商選擇: {valid['coverage'].mean():.1%}")

# 唯一標題數與多列標題
n_titles = valid['職缺名稱'].nunique()
multi = valid.groupby('職缺名稱').size()
print(f"\n不重複標題數: {n_titles:,}（多列標題: {(multi > 1).sum():,}）")

valid.to_pickle('/tmp/new_20260730_classified.pkl')
print("\n已存 /tmp/new_20260730_classified.pkl")
