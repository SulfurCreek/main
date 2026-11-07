#!/usr/bin/env python3
"""多職缺彙整：JD × 版本決定矩陣、Level、B 偏好、各版最常見的缺口與 requirement 狀態。不加總、不平均維度。
  python3 multi_report.py --run <run>   → <run>/report-draft.md
"""
import argparse, collections, glob, json, os, re

ap = argparse.ArgumentParser(); ap.add_argument('--run', required=True); a = ap.parse_args()
raw = f'{a.run}/raw'; man = json.load(open(f'{raw}/manifest.json'))
ks = list(man['resumes']); A = {}
for f in glob.glob(f'{raw}/A_*.json'):
    m = re.match(r'A_(jd\d+)_(.+)\.json', os.path.basename(f))
    try: A[m.groups()] = json.load(open(f))
    except Exception: A[m.groups()] = None
title = {}
for jid in man['jds']:
    p = f'career/review-panel/jd/a/{jid}.md'
    title[jid] = open(p).readline().strip('# \n')[:28] if os.path.exists(p) else jid
L = [f'# 多職缺驗證草稿（{os.path.basename(a.run)}）', '', '## 1. JD × 版本', '',
     '| JD | ' + ' | '.join(f'{k} 決定／Level' for k in ks) + ' | B 偏好（順序） |', '|' + ' --- |' * (len(ks) + 2)]
dec = collections.defaultdict(collections.Counter); bt = collections.Counter(); gaps = collections.defaultdict(collections.Counter)
for jid in man['jds']:
    row = [f'{jid} {title[jid]}']
    for k in ks:
        j = A.get((jid, k))
        if not j: row.append('缺'); continue
        r = j['decision']['recommendation']; dec[k][r] += 1
        row.append(f"{r}／{j['spectrum']['level']}")
        for g in j.get('key_gaps', []): gaps[k][g[:30]] += 1
    bp = f'{raw}/B_{jid}.json'; order = man.get(f'B_{jid}_order', '')
    if os.path.exists(bp):
        try:
            p = json.load(open(bp))['preference']; o = dict(x.split('=') for x in order.split('/'))
            v = o.get(p, p); bt[v] += 1; row.append(f'{v}（{order}）')
        except Exception: row.append('解析失敗')
    else: row.append('—')
    L.append('| ' + ' | '.join(row) + ' |')
L += ['', '## 2. 決定分布', ''] + [f'- {k}：' + '、'.join(f'{x} {n}' for x, n in dec[k].most_common()) for k in ks]
L += ['', '## 3. B 偏好合計', '', '、'.join(f'{x} {n}' for x, n in bt.most_common()) or '—']
for k in ks:
    L += ['', f'## 4. {k} 最常出現的關鍵缺口（前 8，前 30 字聚合，需人工合併同義）', '']
    L += [f'- {n}× {g}' for g, n in gaps[k].most_common(8)]
open(f'{a.run}/report-draft.md', 'w').write('\n'.join(L) + '\n'); print('\n'.join(L[:25]))
