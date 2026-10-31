#!/usr/bin/env python3
"""L 層（輕量批次）回傳整理：從外部模型的原始回覆抽出 tier=L 的單行 JSON，檢查欄位，產出投遞優先表。

用法：python3 light_report.py <raw1.md> [raw2.md ...] [--out report.md]
原始回覆可以是多段對話直接貼在一起；只抓以 {"rubric":"L1" 開頭的行。
"""
import json, re, sys, csv, collections as C

args = [x for x in sys.argv[1:] if not x.startswith("--")]
out = sys.argv[sys.argv.index("--out") + 1] if "--out" in sys.argv else None
if out in args:
    args.remove(out)
route = {"j-" + r["code"]: r for r in csv.DictReader(open("career/review-panel/jd/routing.tsv"), delimiter="\t")}
need = {"job_id", "batch", "must", "fit", "decision", "top_gap", "doubt", "apply_hook", "escalate"}
rows, bad = {}, []
for f in args:
    for i, line in enumerate(open(f, encoding="utf8"), 1):
        line = line.strip().strip("`")
        if not line.startswith('{"rubric":"L1"'):
            continue
        try:
            d = json.loads(line)
        except json.JSONDecodeError as e:
            bad.append(f"{f}:{i} JSON 解析失敗（{e.msg}）")
            continue
        miss = need - d.keys()
        if miss or d["job_id"] not in route:
            bad.append(f"{f}:{i} {d.get('job_id')} 缺欄位 {sorted(miss)} 或代碼不在 routing.tsv")
            continue
        rows[d["job_id"]] = d
expect = {k for k, r in route.items() if r["tier"] == "L"}
order = {"高": 0, "中": 1, "低": 2}
dec = {"interview": "面", "clarify_first": "先釐清", "not_matched": "不符", "insufficient_info": "資訊不足"}
L = ["<!--markdownlint-disable MD013-->", "", f"# L 層輕量審查整理（{len(rows)}／{len(expect)} 份）", ""]
L += [f"- fit 分布：{dict(C.Counter(d['fit'] for d in rows.values()))}",
      f"- 決定分布：{dict(C.Counter(dec.get(d['decision'], d['decision']) for d in rows.values()))}",
      f"- 缺件：{', '.join(sorted(expect - rows.keys())) or '無'}",
      f"- 格式問題：{len(bad)} 筆" + ("".join(f"\n  - {b}" for b in bad)), "",
      "| 職缺 | 公司 | 批 | fit | 決定 | 必備 S/P/U/C | 升級 | 最大缺口 | 投遞時該被看到的一句 |",
      "| :-- | :-- | :-- | :-: | :-- | :-: | :-: | :-- | :-- |"]
for k, d in sorted(rows.items(), key=lambda kv: (order.get(kv[1]["fit"], 9), kv[1]["decision"] != "interview", kv[0])):
    st = C.Counter(m.get("status") for m in d["must"])
    spuc = "/".join(str(st.get(s, 0)) for s in ("supported", "partial", "unknown", "contradicted"))
    r = route[k]
    L.append(f"| {r['title'][:28]}（{k[2:]}） | {r['company']} | {d['batch']} | {d['fit']} | {dec.get(d['decision'], d['decision'])} | {spuc} | "
             f"{'⬆' if d['escalate'] else ''} | {d['top_gap']} | {d['apply_hook']} |")
L += ["", "## 升級候選（escalate=true）", ""] + [f"- {k}：{d.get('why_escalate', '')}" for k, d in rows.items() if d["escalate"]]
L += ["", "## 審查者質疑（逐份）", ""] + [f"- {k}：{d['doubt']}" for k, d in sorted(rows.items())]
text = "\n".join(L) + "\n"
open(out, "w", encoding="utf8").write(text) if out else print(text)
