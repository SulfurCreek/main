"""合併 worst_case 拯救方案與 enhancement 重排方案為單一訓練回饋 CSV（欄位結構相同，情境互斥不重疊）。
前置：需先跑 build_rescue_csv.py 產出 4_worst_case_rescue_plan.csv，
     build_enhancement_csv.py + build_enhancement_residual.py 產出 5_enhancement_reorder_plan.csv，
     這兩個中繼檔本身已不留在 repo（併入本檔後即刪除），僅為重跑時的暫存輸入。"""
import pandas as pd

DIR = "/home/user/main/job-classification-kb/training_feedback"

worst = pd.read_csv(f"{DIR}/4_worst_case_rescue_plan.csv", skiprows=1, dtype=str)
enh = pd.read_csv(f"{DIR}/5_enhancement_reorder_plan.csv", skiprows=1, dtype=str)

worst = worst.rename(columns={'已驗證安全套用規則': '問題標記'})
worst.insert(0, '情境', 'worst_case_退步案例')

enh = enh.rename(columns={'排序問題樣態': '問題標記'})
enh.insert(0, '情境', 'enhancement_排序待優化')

cols = ['情境', '問題標記', '職缺名稱', 'duty0', 'duty1', 'duty2', 'duty3', 'duty4'] + \
       [f'現有版本_推薦{i}' for i in range(1, 11)] + [f'理想推薦_{i}' for i in range(1, 11)]

merged = pd.concat([worst[cols], enh[cols]], ignore_index=True)

comment = ("# 訓練回饋合併檔：worst_case_退步案例(14412筆，20260720模型更新後從命中退步成完全沒中) + "
           "enhancement_排序待優化(18737筆，AI有推到正解但沒排進前5，含556筆新模型仍未解決的殘餘案例)，"
           "共33149筆逐筆理想推薦/理想重排標籤。訓練回饋用，非全域規則，兩者互斥不重複。\n")

with open(f"{DIR}/4_training_rescue_and_reorder_plan.csv", 'w', encoding='utf-8-sig', newline='') as f:
    f.write(comment)
    merged.to_csv(f, index=False)

print(len(merged), "rows written")
