"""重算 4_training_rescue_and_reorder_plan.csv 的「理想推薦」欄。

原始 bug（兩個情境都中招）：舊公式用「現有版本(有問題的模型)的推薦」去填充理想推薦的剩餘欄位，
等於把錯誤推薦當成理想答案的一部分餵給模型訓練：
  - worst_case：現有版本與廠商送出 100% 無交集，填進去的全是無關類別。
  - enhancement：現有版本前5名正是「萬用填充項擠壓」的元凶（調酒師／吧台人員、侍酒師…），
    填進去等於把根因當成正解回饋，模型只會更不準。

修正後（兩情境統一）：理想推薦 = 廠商實際送出的 duty0~4（去重、保留原順序），其餘欄位一律留白。
不臆測、不補值——這份檔案是「逐筆正解標籤」，只主張已知為真的部分。
「現有版本_推薦1~10」欄位保留原樣，作為對照的負面範例。

前置：4_training_rescue_and_reorder_plan.csv 已存在（見 merge_training_feedback_csv.py）。
"""
import pandas as pd

PATH = "/home/user/main/job-classification-kb/training_feedback/4_training_rescue_and_reorder_plan.csv"

duty_cols = ['duty0', 'duty1', 'duty2', 'duty3', 'duty4']
cur_cols = [f'現有版本_推薦{i}' for i in range(1, 11)]
ideal_cols = [f'理想推薦_{i}' for i in range(1, 11)]

COMMENT = (
    "# 訓練回饋合併檔：worst_case_退步案例(14412筆，20260720模型更新後從命中退步成完全沒中) + "
    "enhancement_排序待優化(18737筆，AI有推到正解但沒排進前5)，共33149筆逐筆正解標籤。"
    "訓練回饋用，非全域規則，兩情境互斥不重複。"
    "「理想推薦」= 廠商實際送出的duty0~4(去重、保留原順序)，其餘欄位留白；"
    "刻意不用「現有版本」的推薦填充剩餘欄位——那些正是誤判/擠壓正解的錯誤項，填進去會把錯誤當正解教給模型。"
    "「現有版本_推薦1~10」保留原樣作為對照的負面範例。\n"
)


def build_ideal(row):
    duties = [v for v in (row[c] for c in duty_cols) if pd.notna(v) and v]
    ideal = list(dict.fromkeys(duties))[:10]
    return ideal + [''] * (10 - len(ideal))


def main():
    df = pd.read_csv(PATH, skiprows=1, dtype=str)
    ideals = df.apply(build_ideal, axis=1)
    for i, col in enumerate(ideal_cols):
        df[col] = [x[i] for x in ideals]

    with open(PATH, 'w', encoding='utf-8-sig', newline='') as f:
        f.write(COMMENT)
        cols = ['情境', '問題標記', '職缺名稱'] + duty_cols + cur_cols + ideal_cols
        df[cols].to_csv(f, index=False)

    print(len(df), "列已重新計算並寫回")


if __name__ == '__main__':
    main()
