# 01 — plan() 演算法規格 (Algorithm Spec)

> `plan(vals, correct, ctx, title, MID)` 是整個系統的核心。輸入一個職缺的 5 格現有職類 + 正解 + 上下文，輸出「該怎麼改」。本文是它的完整規格；實作見 [scripts/sync_md.py](../scripts/sync_md.py)。

## 輸入

| 參數 | 說明 |
|---|---|
| `vals` | list[5]，現有職類（空格為 `''` 或 `None`） |
| `correct` | str，正解職類（來自 MD 的「正解」欄） |
| `ctx` | str，`"{廠商名稱} {職缺名稱}"`，用於 domain 判斷 |
| `title` | str，職缺名稱 |
| `MID` | dict，職類 → 中類（CodeNameB）對照，來自 tCodeDutyNM |

## 輸出

`(mode, idx)`：
- `mode` ∈ {keep, keep_strike, replace, replace_multi, replace_all, add}
- `idx`：int（replace/add 的目標格）或 list[int]（keep_strike/replace_multi/replace_all 的格集合，其中 list[0] 為主格）或 None（keep）

## 決策流程

```
1. 判斷 title_has_dept：
   - 職稱含部門標籤 (業務部門|財務部|工務部|...) → True
   - 或 function tail 命中 (…人資專員|…會計主管|…工程師結尾) → True
   title_has_dept = True 時抑制「公司 domain 覆蓋」

2. is_office = (correct 的中類 ∈ OFFICE_MID)

3. 對每一格 i 算 prot(i)（是否受保護，不被槓）：
   a. e == correct                          → 保護
   b. 中類(e) == 中類(correct)                → 保護（同中類）
   c. domain_ok(e, title)  ← 職稱明確特例     → 無條件保護（如主管司機→特別助理）
   d. 管理詞保護：e ∈ {基層管理幹部,領班/管理幹部,經營管理主管,儲備幹部}
      且 title 含 (幹部|主管|領班|組長|課長|股長|店長|經理|主任) → 保護
   e. 語言保護：e 是某語言翻譯職類 且 title 含該語言 → 保護
   f. e 出現在 title 字面 → 保護
   g. (非 dept) 公司 domain：
      - is_office 且 domain_ok(e, ctx)                         → 保護
      - 非 office 且 domain_ok(e, ctx) 且 同中類               → 保護
   h. SUPPORT 保護：
      - is_office 且 e ∈ BROAD_SUPPORT                         → 保護
      - is_office 且 e ∈ SUPPORT 且 同中類                     → 保護

4. correct_present = correct 已在某現有格？
   - 是 + 有非保護錯誤格 → ('keep_strike', [錯誤格們])
   - 是 + 無錯誤格       → ('keep', None)

5. cand = 非保護格（或冗餘格）
   - cand 非空：
     - 全部都是 cand（無任何保護格）   → ('replace_all', cand)
     - 否則 primary = cand 排序首位（過資深者優先，再高 seniority，再前位）
       extra_strike = cand 中「非 loosely_related」者（與正解&職缺領域都不相關的雜項）
       - 有 extra_strike → ('replace_multi', [primary]+其餘)
       - 否則             → ('replace', primary)
   - cand 空：
     - 有空格 → ('add', 第一個空格)
     - 全滿無 cand → ('replace', 最資深的非同類格)
```

## loosely_related(i)（取代時是否連帶槓除）

某非保護候選格，若「與職缺沾邊」就只槓主格、保留它；若「完全不相關」就一起槓掉。沾邊判斷：

```
e in title                                       → 沾邊（保留）
domain_ok(e, ctx, title)                          → 沾邊
中類(e) == 中類(correct)                           → 沾邊
is_office 且 中類(e) ∈ {行政後勤／總務, 管理幕僚}    → 沾邊（辦公室類正解保留一般行政）
ctx 含 (機構|醫院|診所|長照|學校|飯店|集團|中心)
   且 中類(e) ∈ {行政後勤／總務, 管理幕僚}          → 沾邊（機構行政共存）
否則                                              → 不相關（連帶槓除）
```

## domain_ok(e, ctx, title='')

```
AGENCY = ctx 含 (人力|人事|仲介|顧問|派遣|萬寶華|才庫|藝珂|企管顧問|管理顧問)
對每條 DOMAIN (pat → cats)：
  若 pat 在 ctx 命中：
    若 AGENCY 且 pat 是「人力|人事|仲介|顧問」那條：
       除非 title 本身含 (人資|人事|人力資源|HR|招募|徵才|教育訓練)，否則跳過
       （派遣公司登的是客戶職缺，公司行業≠職缺）
    對每個 cat：若 cat==e 或 (cat in e 且 len(cat)>3) → True
回傳 False
```
> ⚠️ 方向性：只用 `cat in e`（domain 類別是 e 的子字串），**不可用 `e in cat`**，否則「行政人員」會被「學校行政人員」誤吸。詳見 [03-pitfalls](03-pitfalls.md)。

## 常數集合

```python
OFFICE_MID = {管理幕僚, 人力資源, 行政後勤／總務, 財務會計, 稽核審計, 業務推廣,
              客服開發, 行銷／廣告, 產品／企劃, 國際貿易, 法務專利, 出版翻譯,
              新聞媒體, 顧問諮詢, 專案管理}

SUPPORT = {行政助理, 業務助理, 秘書, 特別助理, 總機／接待／櫃檯人員, 行政人員,
           人事助理, 國貿助理, 採購助理, 行銷企劃助理, 設計助理, 工程助理,
           財務／會計助理, 助教, 內勤業務}

BROAD_SUPPORT = {行政助理, 行政人員, 總機／接待／櫃檯人員, 工讀生, 電腦操作／資料輸入}
```

DOMAIN 規則列表（pat → 允許職類）見 [scripts/sync_md.py](../scripts/sync_md.py) 的 `DOMAIN`。
