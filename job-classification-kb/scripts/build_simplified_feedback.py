"""產出訓練回饋檔：一個職缺標題一列、一種優化緣由。

定義（依業務端確認）
--------------------
以現行模型（20260720）的實際推薦為準，每個標題歸入唯一一種緣由：

■ 推薦項目命中率改善（worst case：推薦1~10 完全沒命中廠商送出的任一職類）
    負向推薦 = 模型推薦第1~5名（與廠商選擇有落差、沒命中的部分）
    正向推薦 = 廠商實際送出的職類（讓模型學習與廠商選擇行為對齊）

■ 順序調整（enhancement：前5名沒命中，但第6~10名有命中）
    負向推薦 = 模型推薦第1~5名（要壓下去的）
    正向推薦 = 第6~10名中命中廠商送出職類的項目（要推上來的），依原名次排序

合併單位
--------
以「職缺標題」為單位。已驗證模型輸出 100% 由標題決定（154,860 個標題中，
同標題推薦不一致者 0 個），故同標題的多筆職缺對模型是同一個輸入，只能給一種答案。
同標題有多家廠商時，送出職類取聯集，依「幾家廠商送過」由多到少排序（共識優先）。
"""
import pandas as pd
import sys
from collections import defaultdict, Counter

OLD_MD = "/home/user/main/job-classification-kb/tcode/data_職缺名稱_dutyMapping.md"
NEW_XLSX = "/root/.claude/uploads/6d643d58-f39d-53f8-a740-df69060d043b/a61c2155-________20260720.xlsx"
OUT = "/home/user/main/job-classification-kb/training_feedback/推薦模型訓練回饋.csv"

DUTY = [f"duty{i}" for i in range(5)]
REC = [f"職類推薦{i}" for i in range(1, 11)]
NEG = [f'負向推薦{i}' for i in range(1, 6)]
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
        if not title:
            continue
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
        recs = recs_of[title]
        top5, rank6_10 = recs[:5], recs[5:10]

        # 前5名已含廠商送過的職類 → 使用者看得到正確答案，不是問題
        if set(top5) & set(votes):
            continue

        promote = [x for x in rank6_10 if x in votes]      # 第6~10名中命中的
        if promote:
            reason, pos = REORDER, promote[:5]
        else:
            reason, pos = MISS, [d for d, _ in votes.most_common()][:5]

        assert not (set(top5) & set(pos)), f"負正交集: {title}"

        row = {'職缺名稱': title}
        row.update({NEG[k]: (top5[k] if k < len(top5) else '') for k in range(5)})
        row.update({POS[k]: (pos[k] if k < len(pos) else '') for k in range(5)})
        row['優化緣由'] = reason
        rows.append(row)

    out = pd.DataFrame(rows)[['職缺名稱'] + NEG + POS + ['優化緣由']]
    comment = (
        "# 推薦模型訓練回饋（每個職缺標題一列）。"
        "負向推薦＝現行模型(20260720)推薦第1~5名，是要壓下去/修正的部分；"
        "正向推薦＝應該推薦的職類與順序。"
        "優化緣由二擇一：推薦項目命中率改善＝推薦1~10完全沒命中，正向推薦取廠商實際送出的職類；"
        "順序調整＝命中落在第6~10名，正向推薦取那些要推上前5名的項目。不足5項即留白。\n"
    )
    with open(OUT, 'w', encoding='utf-8-sig', newline='') as f:
        f.write(comment)
        out.to_csv(f, index=False)

    # ---------------- 驗收 ----------------
    chk = pd.read_csv(OUT, skiprows=1, dtype=str)

    def cells(r, cols):
        return [r[x] for x in cols if pd.notna(r.get(x)) and r.get(x)]

    ok = True
    dup = chk['職缺名稱'].duplicated().sum()
    print(f"[1] 重複標題 {dup} 筆（每標題一列一緣由）", "✅" if dup == 0 else "❌")
    ok &= dup == 0

    dist = chk['優化緣由'].value_counts().to_dict()
    print(f"[2] 總列數 {len(chk):,}｜{dist}", "✅" if set(dist) == {MISS, REORDER} else "❌")
    ok &= set(dist) == {MISS, REORDER}

    negf = chk[NEG].notna().all(axis=1).sum()
    ovl = sum(1 for _, r in chk.iterrows() if set(cells(r, NEG)) & set(cells(r, POS)))
    pos1 = chk['正向推薦1'].isna().sum()
    print(f"[3] 負向5項全非空 {negf}/{len(chk)}｜正負交集 {ovl}｜正向1為空 {pos1}",
          "✅" if (negf == len(chk) and ovl == 0 and pos1 == 0) else "❌")
    ok &= (negf == len(chk) and ovl == 0 and pos1 == 0)

    bad_r = bad_m = 0
    for _, r in chk.iterrows():
        recs = recs_of[r['職缺名稱']]
        pos = cells(r, POS)
        if r['優化緣由'] == REORDER:
            # 正向項必須全部來自第6~10名，且順序與原名次一致
            expect = [x for x in recs[5:10] if x in set(pos)]
            if pos != expect:
                bad_r += 1
        else:
            # 正向項必須全部是廠商送出職類，且完全沒出現在推薦1~10
            if any(p in recs for p in pos):
                bad_m += 1
    print(f"[4] 順序調整-正向非來自6~10名或順序錯 {bad_r} 筆｜命中率改善-正向卻出現在推薦中 {bad_m} 筆",
          "✅" if (bad_r == 0 and bad_m == 0) else "❌")
    ok &= (bad_r == 0 and bad_m == 0)

    print("\n驗收", "全數通過 ✅" if ok else "未通過 ❌")

    print("\n--- 範例：順序調整 ---")
    s = chk[chk['優化緣由'] == REORDER].iloc[0]
    print(f"  {s['職缺名稱']}")
    print(f"  現行推薦1~10: {recs_of[s['職缺名稱']]}")
    print(f"  負向(壓下去)={cells(s, NEG)}")
    print(f"  正向(推上來)={cells(s, POS)}")
    print("--- 範例：推薦項目命中率改善 ---")
    s = chk[chk['優化緣由'] == MISS].iloc[0]
    print(f"  {s['職缺名稱']}")
    print(f"  現行推薦1~10: {recs_of[s['職缺名稱']]}")
    print(f"  負向(沒命中)={cells(s, NEG)}")
    print(f"  正向(廠商選的)={cells(s, POS)}")

    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
