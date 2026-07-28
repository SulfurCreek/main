"""修正 4_training_rescue_and_reorder_plan.csv 的「理想推薦」計算邏輯（原始bug：worst_case情境下，
現有版本推薦跟廠商送出100%無關，卻被原封不動塞進理想推薦2~10欄，等於教模型學錯誤的關聯）。

修正後：
- worst_case_退步案例：理想推薦 = 廠商送出的 duty0~4（去重、保留原順序），其餘留白，不用現有版本(無關)推薦填充。
- enhancement_排序待優化：理想推薦 = duty0~4 優先排列，剩餘欄位才用「現有推薦中不在 duty0~4 裡」的項目補滿。

前置：4_training_rescue_and_reorder_plan.csv 已存在（見 merge_training_feedback_csv.py）。
"""
import pandas as pd

PATH = "/home/user/main/job-classification-kb/training_feedback/4_training_rescue_and_reorder_plan.csv"

duty_cols = ['duty0', 'duty1', 'duty2', 'duty3', 'duty4']
cur_cols = [f'現有版本_推薦{i}' for i in range(1, 11)]
ideal_cols = [f'理想推薦_{i}' for i in range(1, 11)]


def build_ideal(row):
    duties = [v for v in (row[c] for c in duty_cols) if pd.notna(v) and v]
    duties_dedup = list(dict.fromkeys(duties))
    current = [v for v in (row[c] for c in cur_cols) if pd.notna(v) and v]

    if row['情境'] == 'worst_case_退步案例':
        ideal = duties_dedup[:10]
    else:
        remaining = 10 - len(duties_dedup)
        filler = [c for c in current if c not in duties_dedup]
        ideal = duties_dedup + (filler[:remaining] if remaining > 0 else [])

    ideal = ideal[:10]
    ideal += [''] * (10 - len(ideal))
    return ideal


def main():
    df = pd.read_csv(PATH, skiprows=1, dtype=str)
    ideals = df.apply(build_ideal, axis=1)
    for i, col in enumerate(ideal_cols):
        df[col] = [x[i] for x in ideals]

    comment = ("# 訓練回饋合併檔：worst_case_退步案例(14412筆，20260720模型更新後從命中退步成完全沒中) + "
               "enhancement_排序待優化(18737筆，AI有推到正解但沒排進前5，含556筆新模型仍未解決的殘餘案例)，"
               "共33149筆逐筆理想推薦/理想重排標籤。訓練回饋用，非全域規則，兩者互斥不重複。"
               "「理想推薦」邏輯：worst_case優先只放vendor自己送出的duty0~4(其餘留白，不用現有版本的無關推薦填充避免誤導模型)；"
               "enhancement則用vendor duty0~4優先排列、再用現有推薦中未重複的項目安全填滿剩餘欄位。\n")

    with open(PATH, 'w', encoding='utf-8-sig', newline='') as f:
        f.write(comment)
        cols = ['情境', '問題標記', '職缺名稱'] + duty_cols + cur_cols + ideal_cols
        df[cols].to_csv(f, index=False)

    print(len(df), "列已重新計算並寫回")


if __name__ == '__main__':
    main()
