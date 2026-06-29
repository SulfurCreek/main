# 02 — 各表「如何快速分析產生 MD」食譜 (Analysis Recipes)

> 目標：拿到任一 tCode 表，用 token 最省的方式產出可讀 MD。原則：**先看結構（CodeType 分布、列數），再抽葉，再依中類分組**，不要整表 dump。

## 通用三步驟

### Step 1 — 結構偵察（不 dump 全表）
```python
import openpyxl
from collections import Counter
wb = openpyxl.load_workbook(PATH, read_only=True)
ws = wb[SHEET]
rows = list(ws.iter_rows(min_row=1, values_only=True))
hdr = [str(c) if c else '' for c in rows[0]]
idx = {h:i for i,h in enumerate(hdr)}
ct = Counter(str(r[idx['CodeType']]) for r in rows[1:] if r[idx['CodeType']] is not None)
print(hdr); print('CodeType分布:', dict(ct))   # 看出葉層 = max(ct)
```

### Step 2 — 抽葉 + 依中類分組
```python
leaf = max((t for t in ct if t.isdigit()), key=int)
a,b,c = idx['CodeNameA'], idx.get('CodeNameB'), idx.get('CodeNameC')
from collections import defaultdict
tree = defaultdict(lambda: defaultdict(list))   # 大類 > 中類 > [葉]
for r in rows[1:]:
    if str(r[idx['CodeType']]) == leaf:
        big = r[c] if c is not None else ''
        mid = r[b] if b is not None else ''
        tree[big][mid].append(r[a])
```

### Step 3 — 輸出 MD（大類標題 + 中類表）
```python
lines = [f'# {SHEET} 代碼表\n']
for big in sorted(tree):
    lines.append(f'\n## {big}\n')
    for mid in sorted(tree[big]):
        items = "、".join(tree[big][mid])
        lines.append(f'- **{mid}**（{len(tree[big][mid])}）：{items}\n')
open(f'{SHEET}.md','w',encoding='utf-8').writelines(lines)
```

> 一鍵版見 [scripts/tcode_to_md.py](../scripts/tcode_to_md.py)：`python3 tcode_to_md.py tCodeDutyNM`

## 各表客製要點

| 表 | 特殊處理 |
|---|---|
| tCodeDutyNM/HL/PT/ST/TU | 三層；輸出大類>中類>葉。職務表是 plan() 的 MID 來源 |
| tCodeBenefit / tCodeCompSkill | **兩層**（葉=type2），無 CodeNameC，用 CodeNameB 當分組，CodeDescript 可附說明 |
| tCodeCertify | 2,451 葉很大；建議**只輸出中類層級 + 各中類葉數**，需要時再展開特定中類 |
| tCodeWorkAbility | 1,093 葉；同上，先中類概覽 |
| tCodeCity | 葉=鄉鎮區，中類=縣市；輸出可按縣市分組 |
| tCodeMRT | 中類=路線，葉=站名；按路線分組 |
| tCodeTrade | 行業；大類>中類>細項 |

## 大表的 token 節省策略

對 Certify(2451) / WorkAbility(1093) / City(999) 這種大表：
1. **先只產「中類層級摘要」**：每個中類一行 + 葉數，不列出所有葉。
2. 使用者指定某中類時，**再單獨展開**那個中類的葉。
3. 需要全量時才產完整 MD，並考慮分檔（一個大類一個 MD）。

```python
# 中類摘要（大表首選）
for big in sorted(tree):
    for mid in sorted(tree[big]):
        print(f'{big} > {mid}: {len(tree[big][mid])} 葉')
```

## 比對兩版 export（異動分析）

```python
# 載入兩版，比對 CodeNo 集合 + 名稱變化
old = load_leaves('TCode_Export_舊.xlsx', SHEET)   # {CodeNo: CodeNameA}
new = load_leaves('TCode_Export_新.xlsx', SHEET)
added   = new.keys() - old.keys()
removed = old.keys() - new.keys()
renamed = {k for k in old.keys() & new.keys() if old[k] != new[k]}
```
> 完整異動清單/公告流程用 `tcode-excel-ops` skill。
