"""產出「撤回清單」：列出所有曾經被錯誤標記為『理想推薦』、但實際上並非廠商送出職類的配對。

背景：4/5 號訓練回饋檔的多個歷史版本，「理想推薦」欄用『現有版本(有問題的模型)的推薦』填充剩餘欄位，
等於把錯誤類別當成正解餵給模型。本腳本掃描所有受污染的歷史版本(從 git 取出)，計算去重後的
(職缺, 錯誤類別) 配對，供模型團隊做負向回饋 / 反向修正。

用法：先用 git show 把歷史版本匯出到 HIST 目錄，再執行本腳本。
"""
import pandas as pd
import glob
import os
from collections import defaultdict

HIST = "/tmp/claude-0/-home-user-main/6d643d58-f39d-53f8-a740-df69060d043b/scratchpad/hist"
OUT = "/home/user/main/job-classification-kb/training_feedback/5_retraction_wrong_ideal_labels.csv"
MAX_WRONG = 19

duty_cols = ['duty0', 'duty1', 'duty2', 'duty3', 'duty4']
ideal_cols = [f'理想推薦_{i}' for i in range(1, 11)]

# 歷史版本 → 對外說法（哪個 commit / 哪份檔案）
VERSION_LABEL = {
    '6c0c809_4_worst_case_rescue_plan.csv': 'v1-worst(615筆版)',
    'df5f787_4_worst_case_rescue_plan.csv': 'v2-worst(14412筆版)',
    '3924c8c_5_enhancement_reorder_plan.csv': 'v3-enh(18181筆版)',
    '42ac763_5_enhancement_reorder_plan.csv': 'v4-enh(19131筆版)',
    '13b1e5c_5_enhancement_reorder_plan.csv': 'v5-enh(18737筆版)',
    '3b1b641_4_training_rescue_and_reorder_plan.csv': 'v6-合併版',
    'fe3fa9c_4_training_rescue_and_reorder_plan.csv': 'v7-合併版(worst已修/enh仍污染)',
}


def main():
    pollution = defaultdict(lambda: defaultdict(set))
    meta = {}

    for path in sorted(glob.glob(f"{HIST}/*.csv")):
        name = os.path.basename(path)
        label = VERSION_LABEL.get(name, name)
        df = pd.read_csv(path, skiprows=1, dtype=str)
        for _, r in df.iterrows():
            duties = [r[c] for c in duty_cols if pd.notna(r.get(c)) and r.get(c)]
            dutyset = set(duties)
            ideal = [r[c] for c in ideal_cols if pd.notna(r.get(c)) and r.get(c)]
            wrong = [x for x in ideal if x not in dutyset]
            if not wrong:
                continue
            key = (r['職缺名稱'], tuple(duties))
            meta[key] = r.get('情境', '') or ('worst_case_退步案例' if 'worst' in name else 'enhancement_排序待優化')
            for w in wrong:
                pollution[key][w].add(label)

    rows = []
    for (title, duties), cats in pollution.items():
        ordered = sorted(cats.keys())
        versions = sorted({v for s in cats.values() for v in s})
        row = {
            '情境': meta[(title, duties)],
            '職缺名稱': title,
            '錯誤類別數': len(ordered),
            '曾出現版本': '｜'.join(versions),
        }
        for i, c in enumerate(duty_cols):
            row[c] = duties[i] if i < len(duties) else ''
        for i in range(MAX_WRONG):
            row[f'應撤回_錯誤類別_{i+1}'] = ordered[i] if i < len(ordered) else ''
        rows.append(row)

    cols = (['情境', '職缺名稱'] + duty_cols + ['錯誤類別數']
            + [f'應撤回_錯誤類別_{i+1}' for i in range(MAX_WRONG)] + ['曾出現版本'])
    out = pd.DataFrame(rows)[cols]

    comment = (
        "# ⚠️ 撤回清單（負向回饋用）：以下職缺曾在 4/5 號訓練回饋檔的歷史版本中，被錯誤標記為『理想推薦』的類別。\n"
    )
    with open(OUT, 'w', encoding='utf-8-sig', newline='') as f:
        f.write(comment)
        out.to_csv(f, index=False)

    print(f"{len(out)} 筆職缺、{sum(out['錯誤類別數'])} 個錯誤配對已寫入 {OUT}")


if __name__ == '__main__':
    main()
