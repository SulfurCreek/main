#!/usr/bin/env python3
"""由 gen_cover_drafts.py 的草稿產生批次總表。用法：python3 career/scripts/gen_cover_index.py <jobs.json> <codes.txt> <輸出.md> <標題日期>"""
import glob, json, re, sys
J = json.load(open(sys.argv[1]))["jobs"]
codes = open(sys.argv[2]).read().split()
names = {"R": "無文件重建", "W": "需求窗口與交付", "A": "AI Agent 協作", "F": "AI 功能上線", "S": "帳號安全 OTP", "M": "訊息整併", "P": "定價實驗", "Y": "網頁付款", "C": "海外支付", "K": "網紅平台 0→1", "J": "下架危機承接", "G": "群組招募", "Q": "結案率", "L": "在地化", "T": "代碼表整合"}
rows, missing, noisy, eng = [], [], [], []
for c in codes:
    g = glob.glob(f"career/letters/104/{c}-*-draft.md")
    if not g:
        missing.append(c); continue
    t = open(g[0]).read()
    stories = re.findall(r"^\| \d \| ([A-Z]) \|", t, re.M)
    n = re.search(r"字數（純文字不含空白）：(\d+)", t).group(1)
    title = J[c]["title"].strip()
    comp = re.search(r"j-%s ([^｜]*)｜" % c, t).group(1)
    en = "英文JD" if "JD 以英文為主" in t else ""
    gaps = re.search(r"不暗示 ([^；\n]*)", t)
    if re.search(r"[★<>]", title): noisy.append(c)
    if en: eng.append(c)
    rows.append(f"| [{c}](https://www.104.com.tw/job/{c}) | {comp[:22]} | {title[:34]} | {'、'.join(names[s] for s in stories)} | {n} | {en} |")
out = f"""<!--markdownlint-disable MD013-->

# {sys.argv[4]} 批次推薦信（共 {len(rows)} 封上游草稿）

> 上游：`career/letters/104/<code>-<公司>-draft.md`（`gen_cover_drafts.py` 依 JD 主題從核准事實句庫選三點；全中文；`verify_letter.py` 逐封 Exit 0）。下游：Codex 逐封潤飾到 `career/drafts/codex/letters/`。
> 事實全來自已核准定稿句（decisions §34、§51、R09、R20），沒有新增事實；缺口關鍵字列在各檔〈刻意不寫〉。

| 代碼 | 公司 | 職缺 | 選用事實 | 字數 | 備註 |
| :-- | :-- | :-- | :-- | :-: | :-- |
""" + "\n".join(rows) + f"""

## 需要你決定或補資料

- **JD 缺漏，未產出**：{'、'.join(missing) or '無'}。
- **JD 以英文為主（目前先出全中文）**：{'、'.join(eng) or '無'}。要不要改中英混合版？
- **職缺名含雜訊字元（逐字保留，投遞時請確認要不要照貼）**：{'、'.join(noisy) or '無'}。
- **同公司多封**：請避免三點完全相同，Codex 潤飾時各自調整角度，不改事實。
- 自動選材的限制：依 JD 主題關鍵字配對，不是逐封精讀；適配度低的職缺針對性有限，建議依優先序挑重點職缺。
"""
open(sys.argv[3], "w").write(out)
print(len(rows), missing)
