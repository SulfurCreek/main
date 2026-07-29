"""產出單一訓練回饋檔：一個職缺標題一列、一個優化緣由。

設計要點
--------
1. **一律以現行模型（20260720）的實際推薦為準**，不混用舊模型基準——避免同一筆職缺
   因被不同模型版本評估而產生兩列、兩種緣由。
2. **以職缺標題為合併單位**。已驗證模型輸出 100% 由標題決定（154,860 個標題中，
   同標題推薦不一致者 0 個），因此同標題的多筆職缺對模型而言是同一個輸入；
   若給出兩種不同答案即為矛盾訊號。同標題的各廠商送出職類取聯集，
   依「幾家廠商送過」由多到少排序（共識優先）。
3. **沿用原本「前5名完全沒命中」的問題定義**：若該標題的推薦前5名已含任何一個廠商送過的職類，
   代表模型在使用者看得到的範圍內已給出正確答案，不列入回饋。

欄位
----
負面推薦1~5 = 現行模型推薦1~5（定義上保證不含任何正向項）
正向推薦1~5 = 該標題下廠商送出的職類（共識排序，不足留白、不補值）
優化緣由    = 順序調整（正向項有出現在第6~10名）／推薦項目命中率改善（完全沒出現在推薦1~10）
"""
import pandas as pd
import sys
from collections import defaultdict, Counter

OLD_MD = "/home/user/main/job-classification-kb/tcode/data_職缺名稱_dutyMapping.md"
NEW_XLSX = "/root/.claude/uploads/6d643d58-f39d-53f8-a740-df69060d043b/a61c2155-________20260720.xlsx"
OUT = "/home/user/main/job-classification-kb/training_feedback/推薦模型訓練回饋.csv"

DUTY = [f"duty{i}" for i in range(5)]
REC = [f"職類推薦{i}" for i in range(1, 11)]
NEG = [f'負面推薦{i}' for i in range(1, 6)]
POS = [f'正向推薦{i}' for i in range(1, 6)]
MISS, REORDER = '推薦項目命中率改善', '順序調整'


def parse_md(path):
    lines = open(path, encoding='utf-8').read().splitlines()
    start = header = None
    for i, l in enumerate(lines):
        if l.startswith("| 職缺名稱"):
            header = [c.strip() for c in l.strip().strip("|").split("|")]
            start = i + 2
            break
    out = []
    for l in lines[start:]:
        if not l.startswith("|"):
            continue
        c = [x.strip() for x in l.strip("|").split("|")]
        if len(c) == len(header):
            out.append(dict(zip(header, c)))
    return out


def main():
    old = parse_md(OLD_MD)
    new = pd.read_excel(NEW_XLSX, sheet_name="Sheet1", dtype=str)
    n = min(len(old), len(new))

    recs_of = {}
    duty_votes = defaultdict(Counter)
    for i in range(n):
        title = old[i].get('職缺名稱', '')
        duties = list(dict.fromkeys(v for v in (old[i].get(c, '') for c in DUTY) if v))
        if not duties:
            continue
        r = new.iloc[i]
        recs = [r[c] for c in REC if pd.notna(r[c])]
        if not recs:
            continue
        recs_of[title] = recs
        for d in duties:
            duty_votes[title][d] += 1

    rows = []
    for title, votes in duty_votes.items():
        if not title:
            continue
        recs = recs_of[title]
        top5, rest = recs[:5], recs[5:10]

        # 前5名已含任何廠商送過的職類 → 使用者看得到正確答案，不是問題
        if set(top5) & set(votes):
            continue
        pos = [d for d, _ in votes.most_common()][:5]
        reason = REORDER if any(p in rest for p in pos) else MISS

        assert not (set(top5) & set(pos)), f"負正交集: {title}"

        row = {'職缺名稱': title}
        row.update({NEG[k]: (top5[k] if k < len(top5) else '') for k in range(5)})
        row.update({POS[k]: (pos[k] if k < len(pos) else '') for k in range(5)})
        row['優化緣由'] = reason
        rows.append(row)

    out = pd.DataFrame(rows)[['職缺名稱'] + NEG + POS + ['優化緣由']]
    comment = ("# 推薦模型訓練回饋：每個職缺標題一列。負面推薦＝現行模型(20260720)推錯的前5項；"
               "正向推薦＝該標題下廠商實際送出的職類（多家廠商時依共識排序，不足5項留白、不補值）。"
               "優化緣由二擇一：順序調整＝正向項目前落在第6~10名；推薦項目命中率改善＝正向項完全沒出現在推薦1~10。\n")
    with open(OUT, 'w', encoding='utf-8-sig', newline='') as f:
        f.write(comment)
        out.to_csv(f, index=False)

    # ---------------- 驗收 ----------------
    chk = pd.read_csv(OUT, skiprows=1, dtype=str)

    def cells(r, cols):
        return [r[x] for x in cols if pd.notna(r.get(x)) and r.get(x)]

    ok = True
    dup_title = chk['職缺名稱'].duplicated().sum()
    print(f"[1] 重複職缺標題 {dup_title} 筆（每個標題只能一列、一種緣由）",
          "✅" if dup_title == 0 else "❌")
    ok &= dup_title == 0

    dist = chk['優化緣由'].value_counts().to_dict()
    print(f"[2] 總列數 {len(chk):,}｜緣由分布 {dist}",
          "✅" if set(dist) == {MISS, REORDER} else "❌")
    ok &= set(dist) == {MISS, REORDER}

    neg_full = chk[NEG].notna().all(axis=1).sum()
    overlap = sum(1 for _, r in chk.iterrows() if set(cells(r, NEG)) & set(cells(r, POS)))
    pos1 = chk['正向推薦1'].isna().sum()
    print(f"[3] 負面5項全非空 {neg_full}/{len(chk)}｜正負交集 {overlap}｜正向1為空 {pos1}",
          "✅" if (neg_full == len(chk) and overlap == 0 and pos1 == 0) else "❌")
    ok &= (neg_full == len(chk) and overlap == 0 and pos1 == 0)

    bad = 0
    for _, r in chk.iterrows():
        recs = recs_of[r['職缺名稱']]
        pos = cells(r, POS)
        hit = any(p in recs[5:10] for p in pos)
        if (REORDER if hit else MISS) != r['優化緣由']:
            bad += 1
    print(f"[4] 緣由與現行模型實際狀態不符 {bad} 筆", "✅" if bad == 0 else "❌")
    ok &= bad == 0

    k = chk[chk['職缺名稱'].str.contains('卡比音樂', na=False)]
    print(f"[5] 抽查卡比音樂工作室 {len(k)} 個標題，緣由 {sorted(set(k['優化緣由']))}")
    if len(k):
        r = k.iloc[0]
        print(f"    {r['職缺名稱']}")
        print(f"    負面={cells(r, NEG)}")
        print(f"    正向={cells(r, POS)}")

    print("\n驗收", "全數通過 ✅" if ok else "未通過 ❌")
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
