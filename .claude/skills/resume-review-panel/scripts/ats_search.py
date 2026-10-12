#!/usr/bin/env python3
"""ATS 模擬招募者搜尋排名（驗證機制 v3 第 2 項）。

ATS 多半是讓招募者「搜尋」的資料庫（career/style/ats-2026-source.md）。本工具把使用者各版履歷
與 50 份同儕履歷放進同一個索引，用 A 級職缺推導的招募者查詢詞搜尋，看使用者排第幾。

用法：
  python3 ats_search.py --peers career/review-panel/candidates --queries queries.tsv \
      --doc v7.1=career/104/archive/resume-104-v7.1.txt --doc v7.2=career/104/resume-104-v7.2.txt
queries.tsv：每行「職缺名<TAB>查詢詞（空白分隔）」。
評分：BM25，中文以字元 bigram 切詞、英數以單字切詞；各版本**分別**和 50 份同儕競爭（不互相競爭）。
輸出：每條查詢的名次、各版本 Top-10 命中率與平均名次。
"""
import argparse, glob, math, re, collections

def toks(t):
    t = t.lower()
    out = re.findall(r'[a-z0-9][a-z0-9+./#-]*', t)
    for seg in re.findall(r'[一-鿿]+', t):
        out += [seg[i:i+2] for i in range(len(seg) - 1)] or [seg]
    return out

def qtoks(q):
    return [x for w in q.split() for x in toks(w)]

def bm25_rank(docs, q, k1=1.5, b=0.75):
    N = len(docs); avg = sum(len(d) for d in docs.values()) / N
    df = collections.Counter(w for d in docs.values() for w in set(d))
    sc = {}
    for name, d in docs.items():
        tf = collections.Counter(d); s = 0
        for w in q:
            if w not in tf: continue
            idf = math.log(1 + (N - df[w] + .5) / (df[w] + .5))
            s += idf * tf[w] * (k1 + 1) / (tf[w] + k1 * (1 - b + b * len(d) / avg))
        sc[name] = s
    return sorted(sc, key=lambda n: -sc[n])

def load_peers(path):
    peers = {}
    for f in sorted(glob.glob(path + '/resumes-*.md')):
        for blk in re.split(r'\n(?=## \d+ )', open(f, encoding='utf8').read()):
            m = re.match(r'## (\d+) ', blk)
            if m: peers['peer' + m.group(1)] = toks(blk)
    return peers

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--peers', required=True); ap.add_argument('--queries', required=True)
    ap.add_argument('--doc', action='append', required=True)
    a = ap.parse_args()
    peers = load_peers(a.peers)
    mine = {k: toks(open(v, encoding='utf8').read()) for k, v in (x.split('=', 1) for x in a.doc)}
    qs = [l.rstrip('\n').split('\t') for l in open(a.queries, encoding='utf8') if '\t' in l]
    res = {k: [] for k in mine}
    print('| 職缺 | 查詢 | ' + ' | '.join(mine) + ' |'); print('| :-- | :-- |' + ' :-: |' * len(mine))
    for job, q in qs:
        row = []
        for k, d in mine.items():
            rank = bm25_rank({**peers, k: d}, qtoks(q)).index(k) + 1
            res[k].append(rank); row.append(str(rank))
        print(f'| {job} | {q} | ' + ' | '.join(row) + ' |')
    print(f'\n同儕數：{len(peers)}；查詢數：{len(qs)}')
    for k, r in res.items():
        print(f'{k}: Top-10 命中 {sum(x <= 10 for x in r)}/{len(r)}（{sum(x <= 10 for x in r)/len(r):.0%}），Top-3 {sum(x <= 3 for x in r)}/{len(r)}，平均名次 {sum(r)/len(r):.1f}')
