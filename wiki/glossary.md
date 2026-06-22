# 專案術語與縮寫字典

本專案實際會用到的縮寫/術語，方便溝通時不用每次展開解釋。

## 平台與團隊

- **`1111-jobdocs`**：HackMD 團隊 path，所有 team note/folder 端點的 `:teamPath` 都用這個值。
- **求才系統（recruit）**：廠商端系統，HackMD 規格書用 `spec-doc-1111` skill 預設範本。
- **求職系統（求職主網）**：求職者端系統，HackMD 規格書用 `assets/template-jobseeker.md` 範本。動筆前必須先確認文件屬於哪一邊（見 `wiki/recruitment_system_rules.md`）。

## 資料欄位

- **`organNo`**：廠商編號。
- **`talentNo`**：求職者（人才）編號。
- **`empNo`**：職缺編號（對應 `employees.employeeNo`）。
- **`rNo`**：某張記訊/對話資料的流水號 (PK)，常作為跨 API 傳遞的識別碼（如 `get-echat-mail-logs` 回傳的 `rNo` 即 `get-detail/{infoNo}` 要帶的 `infoNo`）。

## 業務代碼家族（權威來源見 `B1j3sN-bzx`）

- **`organs.showfield`**：廠商功能開關（bit-flag）。
- **`organs.confirmed`**：審核/確認狀態代碼。
- **`oStatus`**：通用狀態代碼。
- **`organsMore`**：廠商擴充欄位代碼。
- **`interViewType`**：邀約類型（詢問意願／面試邀約／錄取通知／感謝函…）。
- **`interViewKind`**：面試類別/方式。

> 這些代碼的完整對照表不放在本 repo，一律連結到 HackMD note `[REF] 求才系統代碼表`（`B1j3sN-bzx`），詳見 `wiki/recruitment_system_rules.md`。

## 規格書撰寫慣例術語

- **MECE 四狀態表**：載入中／有資料／無資料／錯誤，規格書中非同步資料載入區塊（資料載入、列表、搜尋）的標準呈現方式。
- **🚧 待補規則區塊**：`:::warning` 包住、標題帶 🚧、內文紅字，固定結構為「現況 → 缺口 → 待確認（checkbox 清單）→ 來源」，用於標記規格未定案的部分。
- **`{%hackmd <noteId> %}`**：HackMD 原生全文嵌入語法，把另一份 note 的內容就地渲染（通常包在 `:::spoiler` 內）。
- **相對 note 連結**：`[標題](/noteId)`，同一 team workspace 下規格書互連的標準寫法，不用完整 URL。
- **階段拆分**：把第二階段功能拆成獨立 HackMD 文件，第二階段文件每節記 `> 來源：原 §x`，第一階段文件保留入口並連結過去。
