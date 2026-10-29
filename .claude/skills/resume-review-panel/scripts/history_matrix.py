#!/usr/bin/env python3
"""掃描 career/review-panel/runs/*/raw/A_*.json，產出 Opus 逐職缺跨版矩陣 career/review-panel/opus-matrix.md。
只整理「每份職缺的決定／Level」與維度分布，不平均、不排名；跨規準與跨審查者不可比（見 HISTORY.md §可比性）。
用法：python3 history_matrix.py   （在 repo 根目錄執行）"""
import json, glob, re, csv, collections as C, os

RUNS = "career/review-panel/runs"
OUT = "career/review-panel/opus-matrix.md"
# 舊 run 的 jdNN 代號依 routing.tsv 對到 104 職缺代碼，新舊 run 同一職缺排在同一列
OLD = {r["old_id"]: "j-" + r["code"] for r in csv.DictReader(open("career/review-panel/jd/routing.tsv"), delimiter="\t") if r["old_id"]}
rows = C.OrderedDict()   # (run, ver) -> {jd: (decision, level)}
dims = {}
for f in sorted(glob.glob(f"{RUNS}/*/raw/A_*.json")):
    m = re.search(r"/([^/]+)/raw/A_(jd\d+|j-\w+?)[^/]*?_(v[\d.]+)\.json$", f)
    if not m:
        continue
    run, jd, ver = m.groups()
    jd = OLD.get(jd, jd)
    try:
        d = json.load(open(f))
    except Exception:
        continue
    dec = d["decision"]["recommendation"] if isinstance(d["decision"], dict) else d["decision"]
    lv = d.get("spectrum", {}).get("level")
    rows.setdefault((run, ver), {})[jd] = (dec, lv)
    for x in d.get("dimensions", []):
        dims.setdefault((run, ver), C.defaultdict(C.Counter))[x["id"]][x["rating"]] += 1

jds = sorted({j for v in rows.values() for j in v})
short = {"interview": "面", "clarify_first": "先釐清", "not_matched": "不符", "insufficient_info": "資訊不足"}
vkey = lambda v: tuple(int(x) for x in v[1:].split('.'))
keys = sorted(rows, key=lambda k: (vkey(k[1]), k[0]))
L = ["<!--markdownlint-disable MD013-->", "", "# Opus 逐職缺跨版矩陣（自動產生，勿手改）", "",
     "> 由 `.claude/skills/resume-review-panel/scripts/history_matrix.py` 掃描 `runs/*/raw/A_*.json` 產生。",
     "> 格式：`面/7` ＝ 建議面試／Level 7。**每格 1 輪、±1 屬單輪波動；規準與審查者條件不同的 run 不可直接比。**",
     "> 欄位的 run 名稱即 `runs/` 下的資料夾。", ""]
head = "| 職缺 | " + " | ".join(f"{v}<br>`{r[5:]}`" for r, v in keys) + " |"
L += [head, "| :-- |" + " :-: |" * len(keys)]
for jd in jds:
    cells = []
    for k in keys:
        dc = rows[k].get(jd)
        cells.append(f"{short.get(dc[0], dc[0])}/{dc[1]}" if dc else "—")
    L.append(f"| {jd} | " + " | ".join(cells) + " |")
L += ["", "## 分布與維度", "",
      "| run | 版本 | 份數 | 決定 | Level 分布 | 決策深度 | 角色證據 | 責任 |", "| :-- | :-- | --: | :-- | :-- | :-- | :-- | :-- |"]
for k in keys:
    ds = rows[k]
    dec = C.Counter(short.get(v[0], v[0]) for v in ds.values())
    lvc = C.Counter(v[1] for v in ds.values())
    dm = dims.get(k, {})
    fmt = lambda c: "／".join(f"{a}{n}" for a, n in sorted(c.items())) if c else "—"
    L.append(f"| `{k[0]}` | {k[1]} | {len(ds)} | {fmt(dec)} | " + "、".join(f"L{a}×{n}" for a, n in sorted(lvc.items()))
             + f" | {fmt(dm.get('decision_depth', {}))} | {fmt(dm.get('role_evidence', {}))} | {fmt(dm.get('ownership', {}))} |")
open(OUT, "w").write("\n".join(L) + "\n")
print("wrote", OUT, len(keys), "groups")
