"""依 training_feedback/SPEC_正負推薦簡化格式.md 產出單一訓練回饋檔。

輸出欄位：職缺名稱 + 負面推薦1~5 + 正向推薦1~5 + 優化緣由
- 負面推薦1~5 = 現有版本_推薦1~5（兩情境定義上皆保證不含廠商送出職類）
- 正向推薦1~5 = 廠商實際送出的 duty0~4（去重、保留原順序，不足留白，嚴禁補值）
- 優化緣由    = worst_case_退步案例→推薦項目命中率改善 / enhancement_排序待優化→順序調整
"""
import pandas as pd
import sys

SRC = "/home/user/main/job-classification-kb/training_feedback/4_training_rescue_and_reorder_plan.csv"
OUT = "/home/user/main/job-classification-kb/training_feedback/推薦模型訓練回饋.csv"

duty_cols = ['duty0', 'duty1', 'duty2', 'duty3', 'duty4']
cur5_cols = [f'現有版本_推薦{i}' for i in range(1, 6)]
NEG = [f'負面推薦{i}' for i in range(1, 6)]
POS = [f'正向推薦{i}' for i in range(1, 6)]

REASON = {
    'worst_case_退步案例': '推薦項目命中率改善',
    'enhancement_排序待優化': '順序調整',
}


def cells(row, cols):
    return [row[c] for c in cols if pd.notna(row.get(c)) and row.get(c)]


def main():
    src = pd.read_csv(SRC, skiprows=1, dtype=str)
    rows = []
    for _, r in src.iterrows():
        neg = cells(r, cur5_cols)
        pos = list(dict.fromkeys(cells(r, duty_cols)))[:5]

        # 紅線 assert：負面項不得含任何廠商送出職類
        assert not (set(neg) & set(cells(r, duty_cols))), f"負正交集: {r['職缺名稱']}"
        assert r['情境'] in REASON, f"未知情境: {r['情境']}"

        row = {'職缺名稱': r['職缺名稱']}
        row.update({NEG[i]: (neg[i] if i < len(neg) else '') for i in range(5)})
        row.update({POS[i]: (pos[i] if i < len(pos) else '') for i in range(5)})
        row['優化緣由'] = REASON[r['情境']]
        rows.append(row)

    out = pd.DataFrame(rows)[['職缺名稱'] + NEG + POS + ['優化緣由']]

    comment = ("# 推薦模型訓練回饋：每筆案例的負面推薦（模型目前推錯的前5項）與正向推薦（應推薦的正確職類與順序）。"
               "優化緣由：推薦項目命中率改善＝原本完全沒命中需救回；順序調整＝有推到但排在第6~10名需調進前5。"
               "正向推薦來源為廠商實際送出職類，不足5項即留白（不補值）。\n")
    with open(OUT, 'w', encoding='utf-8-sig', newline='') as f:
        f.write(comment)
        out.to_csv(f, index=False)

    # ---- 規格驗收 ----
    chk = pd.read_csv(OUT, skiprows=1, dtype=str)
    ok = True

    n_hit = (chk['優化緣由'] == '推薦項目命中率改善').sum()
    n_ord = (chk['優化緣由'] == '順序調整').sum()
    print(f"[1] 總列數 {len(chk)}（命中率改善 {n_hit} / 順序調整 {n_ord}）",
          "✅" if (len(chk) == 33149 and n_hit == 14412 and n_ord == 18737) else "❌")
    ok &= (len(chk) == 33149 and n_hit == 14412 and n_ord == 18737)

    neg_full = chk[NEG].notna().all(axis=1).sum()
    overlap = sum(1 for _, r in chk.iterrows()
                  if set(cells(r, NEG)) & set(cells(r, POS)))
    print(f"[2] 負面5項全非空 {neg_full}/{len(chk)}｜正負交集 {overlap} 筆",
          "✅" if (neg_full == len(chk) and overlap == 0) else "❌")
    ok &= (neg_full == len(chk) and overlap == 0)

    pos1_empty = chk['正向推薦1'].isna().sum()
    src_map = {}
    for _, r in src.iterrows():
        src_map.setdefault(r['職缺名稱'], []).append(set(cells(r, duty_cols)))
    illegal = 0
    for _, r in chk.iterrows():
        p = set(cells(r, POS))
        if not any(p <= d for d in src_map.get(r['職缺名稱'], [])):
            illegal += 1
    print(f"[3] 正向推薦1為空 {pos1_empty} 筆｜正向含非廠商送出職類 {illegal} 筆",
          "✅" if (pos1_empty == 0 and illegal == 0) else "❌")
    ok &= (pos1_empty == 0 and illegal == 0)

    k = chk[chk['職缺名稱'].str.contains('卡比音樂', na=False)]
    print(f"[4] 抽查卡比音樂工作室 {len(k)} 筆：")
    for _, r in k.drop_duplicates(subset=['優化緣由']).iterrows():
        print(f"    [{r['優化緣由']}] 負面={cells(r, NEG)}")
        print(f"    {' ' * len(r['優化緣由'])}   正向={cells(r, POS)}")

    print("\n驗收", "全數通過 ✅" if ok else "未通過 ❌")
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
