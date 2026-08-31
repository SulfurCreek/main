"""產出訓練回饋檔（含廠商 duty 供比對驗證）。

定義（依業務端確認）
--------------------
以現行模型（20260720）的實際推薦為準。前提：**推薦前5名完全沒命中廠商送出的任一職類**
（前5名若已有命中，代表使用者看得到正確答案，不列入回饋）。

正向推薦＝**要組成的新 top1~5 推薦組合，結果必須符合廠商選的**
          → 兩種緣由都取「該筆職缺廠商實際送出的職類」（duty0~4 原順序）
負向推薦＝**要壓下去的現行 top1~5**（這些必須被擠出前10名，不是只降到6~10名）

優化緣由（追蹤用，標示問題性質不同）
  ■ 推薦項目命中率改善：廠商送出的職類完全沒出現在推薦1~10 → 模型根本沒想到
  ■ 順序調整：廠商送出的職類已出現在第6~10名 → 模型想到了，只是沒排進使用者看得到的前5名
"""
import pandas as pd
import sys

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

    rows, seen, recs_of = [], set(), {}
    for i in range(n):
        o = old[i]
        title = o.get('職缺名稱', '')
        if not title:
            continue
        duties = list(dict.fromkeys(v for v in (o.get(c, '') for c in DUTY) if v))
        if not duties:
            continue
        r = new.iloc[i]
        recs = [r[c] for c in REC if pd.notna(r[c])]
        if not recs:
            continue

        top5, rank6_10 = recs[:5], recs[5:10]
        if set(top5) & set(duties):        # 前5名已有命中 → 不是問題
            continue

        reason = REORDER if (set(rank6_10) & set(duties)) else MISS
        pos = duties[:5]                   # 新的 top1~5＝廠商選的整組
        assert not (set(top5) & set(pos)), f"負正交集: {title}"

        sig = (title, tuple(duties), reason)
        if sig in seen:
            continue
        seen.add(sig)
        recs_of[sig] = recs

        row = {'職缺名稱': title}
        row.update({DUTY[k]: (duties[k] if k < len(duties) else '') for k in range(5)})
        row.update({NEG[k]: (top5[k] if k < len(top5) else '') for k in range(5)})
        row.update({POS[k]: (pos[k] if k < len(pos) else '') for k in range(5)})
        row['優化緣由'] = reason
        rows.append(row)

    out = pd.DataFrame(rows)[['職缺名稱'] + DUTY + NEG + POS + ['優化緣由']]
    comment = (
        "# 推薦模型訓練回饋。duty0~duty4＝廠商實際送出的職類（供比對驗證）。"
        "負向推薦＝現行模型(20260720)推薦第1~5名，要壓下去且需擠出前10名（不是只降到6~10名）。"
        "正向推薦＝要組成的新 top1~5 推薦組合，取廠商送出的職類（不足5項留白、不補值）。"
        "優化緣由：推薦項目命中率改善＝廠商選的完全沒出現在推薦1~10；順序調整＝已出現在第6~10名、只差沒進前5。\n"
    )
    with open(OUT, 'w', encoding='utf-8-sig', newline='') as f:
        f.write(comment)
        out.to_csv(f, index=False)

    # ---------------- 驗收 ----------------
    chk = pd.read_csv(OUT, skiprows=1, dtype=str)

    def cells(r, cols):
        return [r[x] for x in cols if pd.notna(r.get(x)) and r.get(x)]

    ok = True
    dist = chk['優化緣由'].value_counts().to_dict()
    print(f"[1] 總列數 {len(chk):,}｜{dist}", "✅" if set(dist) == {MISS, REORDER} else "❌")
    ok &= set(dist) == {MISS, REORDER}

    same = sum(1 for _, r in chk.iterrows() if cells(r, POS) != cells(r, DUTY)[:5])
    print(f"[2] 正向推薦 ≠ 廠商送出職類(前5) 的列數 {same}", "✅" if same == 0 else "❌")
    ok &= same == 0

    negf = chk[NEG].notna().all(axis=1).sum()
    ovl = sum(1 for _, r in chk.iterrows() if set(cells(r, NEG)) & set(cells(r, POS)))
    print(f"[3] 負向5項全非空 {negf}/{len(chk)}｜負向與廠商duty交集 {ovl}",
          "✅" if (negf == len(chk) and ovl == 0) else "❌")
    ok &= (negf == len(chk) and ovl == 0)

    bad_r = bad_m = 0
    for _, r in chk.iterrows():
        recs = recs_of[(r['職缺名稱'], tuple(cells(r, DUTY)), r['優化緣由'])]
        pos = set(cells(r, POS))
        if r['優化緣由'] == REORDER:
            if not (pos & set(recs[5:10])):
                bad_r += 1
        elif pos & set(recs):
            bad_m += 1
    print(f"[4] 順序調整-正向卻沒出現在6~10名 {bad_r} 筆｜命中率改善-正向卻出現在推薦中 {bad_m} 筆",
          "✅" if (bad_r == 0 and bad_m == 0) else "❌")
    ok &= (bad_r == 0 and bad_m == 0)

    per_title = chk.groupby('職缺名稱').size()
    print(f"[5] 職缺標題數 {len(per_title):,}｜同標題多列(不同廠商選法) {(per_title > 1).sum():,} 個標題")

    print("\n驗收", "全數通過 ✅" if ok else "未通過 ❌")

    for label in (REORDER, MISS):
        s = chk[chk['優化緣由'] == label].iloc[0]
        sig = (s['職缺名稱'], tuple(cells(s, DUTY)), label)
        print(f"\n--- 範例：{label} ---")
        print(f"  {s['職缺名稱']}")
        print(f"  現行推薦1~5 : {recs_of[sig][:5]}")
        print(f"  現行推薦6~10: {recs_of[sig][5:10]}")
        print(f"  廠商duty0~4 : {cells(s, DUTY)}")
        print(f"  負向(壓下去) : {cells(s, NEG)}")
        print(f"  正向(新top5) : {cells(s, POS)}")

    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
