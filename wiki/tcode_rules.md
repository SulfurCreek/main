# tCode Taxonomy Reference

## 概述（Overview）

**tCode** 是 1111 獵才平台的職位分類系統（Job Taxonomy），用以將多元職位編目、分類、搜尋與媒合。

### 四大職務類型（Employment Type Categories）

| 代號 | 名稱 | 縮寫 | 說明 |
| --- | --- | --- | --- |
| DutyNM | 全職 | FT | Normal Full-Time Employment |
| DutyPT | 兼職 | PT | Part-Time Employment |
| DutyST | 工讀 | ST | Work-Study / Internship |
| DutyHL | 中高階 | HL | Mid-to-Senior Level Management |

### 層級結構（Hierarchy Levels）

每個職務類型分為**三層**：

| 層級 | 名稱 | 說明 | 範例 |
| --- | --- | --- | --- |
| **Level 1** | 大類（Category） | 最上層職位分類 | 管理幕僚／人資／行政 |
| **Level 2** | 中類（Subcategory） | 大類底下的細項分類 | 人力資源 |
| **Level 3** | 小類（Item） | 具體職位名稱 | 人事／人力資源專員 |

### 統計（Statistics）

Export date: 2026-07-09  
Export file: `TCode_Export_20260707T090934846Z.xlsx`

| 職務類型 | Level 1 | Level 2 | Level 3 | 總計 |
| --- | ---: | ---: | ---: | ---: |
| 全職 (DutyNM) | 20 | 57 | 617 | **694** |
| 兼職 (DutyPT) | 20 | 57 | 528 | **605** |
| 工讀 (DutyST) | 20 | 47 | 219 | **286** |
| 中高階 (DutyHL) | 18 | 40 | 79 | **137** |
| **總計** | **78** | **201** | **1,443** | **1,722** |

> **註**：Level 1 大類數量不完全相同的原因是某些大類在特定職務類型中可能不提供職位選項。

---

## 資料結構（Data Structure）

### Excel 匯出格式

每個職務類型對應一個 Sheet，結構如下：

```
[Sheet: tCodeDutyNM / tCodeDutyPT / tCodeDutyST / tCodeDutyHL]

| ChangeType | Old_CodeNo | New_CodeNo | CodeNo | CodeNameA | CodeNameB | CodeNameC | CodeType | ... |
|---|---|---|---|---|---|---|---|---|
| UnChange | 100000 | 管理幕僚／人資／行政 | 管理幕僚／人資／行政 | 管理幕僚／人資／行政 | 1 | | (description) |
| UnChange | 100100 | 管理幕僚 | 管理幕僚 | 管理幕僚／人資／行政 | 2 | | (description) |
| UnChange | 100101 | 經營管理主管 | 管理幕僚 | 管理幕僚／人資／行政 | 3 | (job desc) | (type info) |
```

### 欄位說明（Column Definitions）

| 欄位 | 說明 | 範例 |
| --- | --- | --- |
| **ChangeType** | 變更類型：`UnChange`, `New`, `Renamed`, `ContentChanged` | `UnChange` |
| **Old_CodeNo** | 舊代碼編號 | `100000`, `100101` |
| **New_CodeNo** | 新代碼或名稱 | `管理幕僚／人資／行政` |
| **CodeNo** | 現用代碼名稱 | `管理幕僚` |
| **CodeNameA** | Level 1 大類名稱 | `管理幕僚／人資／行政` |
| **CodeNameB** | Level 層級編號 (1/2/3) | `1`, `2`, `3` |
| **CodeNameC** | 職位描述（Level 3 時填入） | `1. 執行主管所交代的命令... 2. ...` |
| **CodeType** | 職務類型補充資訊 | `領導管理, 改革創新, ...` |
| **CodeNameA_EN, CodeNameB_EN, ...** | 英文版本 | `Management Staff / Human Resources` |
| **CodeNameA_VI, CodeNameA_TH, CodeNameA_ID** | 越南文、泰文、印尼文版本 | — |

---

## 全職職務分類（Full-Time / DutyNM）

### Level 1 大類清單（20 categories）

1. 管理幕僚／人資／行政
2. 金融保險／財會／稽核
3. 業務／貿易／客服／門市
4. 資訊系統
5. 設計／創意
6. 工程／機械／製造
7. 生產製造／組裝
8. 物流／運輸／倉儲
9. 採購／供應鏈
10. 教育師資
11. 醫療健康
12. 餐飲旅遊
13. 美容美髮
14. 房地產
15. 出版翻譯
16. 影視演藝
17. 運動健身
18. 法律會計
19. 社會福利
20. 其他

> 詳細子分類見 `notes/tcode_dutyNM_full_structure.md`

---

## 兼職職務分類（Part-Time / DutyPT）

### Level 1 大類清單（20 categories）

與全職相同，共 20 大類，但細項職位數量較少（605 vs 694）。

> 詳細子分類見 `notes/tcode_dutyPT_full_structure.md`

---

## 工讀職務分類（Work-Study / DutyST）

### Level 1 大類清單（20 categories）

與全職相同，共 20 大類，細項職位最少（286 items）。  
適用於學生工讀、短期臨時職位。

> 詳細子分類見 `notes/tcode_dutyST_full_structure.md`

---

## 中高階職務分類（Mid-to-Senior / DutyHL）

### Level 1 大類清單（18 categories）

與上述三種有所不同，主要涵蓋經營管理層級的職位（18 大類，140 items）。

| 代號 | 大類名稱 |
| --- | --- |
| 1 | 管理幕僚／人資／行政 |
| 2 | 金融保險／財會／稽核 |
| 3 | 業務／貿易／客服／門市 |
| — | 其他 |

> 詳細子分類見 `notes/tcode_dutyHL_full_structure.md`

---

## API 整合（API Integration）

### 前端篩選選項源

當求職者或企業選擇職位時，系統通常會展示分層級的選項清單：

```
1️⃣ 選擇大類（Level 1） → 
2️⃣ 選擇中類（Level 2） → 
3️⃣ 選擇具體職位（Level 3）
```

### 後端儲存格式

職位代碼通常以 `Old_CodeNo` （如 `100101`, `100202`）儲存在資料庫，配合 `CodeNameA`, `CodeNameB`, `CodeNameC` 進行多語言顯示。

---

## 變更紀錄（Change Log）

### 2026-07-09

- **Export Date**: 2026-07-09 09:09:34.846Z
- **Status**: All items marked as `UnChange` in this export (snapshot of current state)
- **Previous changes**: Refer to prior conversation context for historical renames and additions

---

## 使用指南（Usage Guide）

### 何時參考本文件

- 需要理解職位分類層級結構
- 進行職位搜尋、篩選相關前端開發
- 撰寫/修改職位相關規格書
- 分析職位統計數據

### 相關檔案

| 檔案 | 用途 |
| --- | --- |
| `notes/tcode_dutyNM_full_structure.md` | 全職職位完整列表 |
| `notes/tcode_dutyPT_full_structure.md` | 兼職職位完整列表 |
| `notes/tcode_dutyST_full_structure.md` | 工讀職位完整列表 |
| `notes/tcode_dutyHL_full_structure.md` | 中高階職位完整列表 |
| `wiki/recruitment_system_rules.md §3` | 後端 API 約定與欄位定義 |

---

## 常見問題（FAQ）

### Q: tCode 有幾層？
**A**: 三層 (Level 1 / Level 2 / Level 3)。

### Q: 為何四種職務類型的大類數不同？
**A**: 因為某些大類在特定職務類型中未提供選項，例如「運動健身」可能僅在全職提供。

### Q: 職位代碼格式？
**A**: `Old_CodeNo` 為六位數字代碼（如 `100101`），`CodeNo` 為中文職位名稱。

### Q: 支援多語言嗎？
**A**: 是，提供中文（繁體）、英文、越南文、泰文、印尼文五種版本。

---

**維護者**: Platform Team  
**最後更新**: 2026-07-09  
**版本**: v1.0.0 (First Release)
