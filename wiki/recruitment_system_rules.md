# 1111 規格書撰寫 — 專案判斷與業務代碼來源

本文件不重複規格書的格式細則（章節編號、MECE 狀態表、🚧 待補區塊、跨文件引用方式等——這些由 `.claude/skills/spec-doc-1111/SKILL.md` 統一管理，使用 `Skill` 工具載入）。
這裡只記錄「動筆前要先確認什麼、代碼表去哪裡找」這類跨文件的判斷依據。

## 1. 動筆前必須先確認專案

1111 人力銀行有兩套使用者方/系統，規格書範本與業務邏輯不同，**寫文件前必須先確認屬於哪一邊**：

| 專案 | 對象 | 範本 |
| --- | --- | --- |
| 求才系統（recruit） | 廠商端 | `spec-doc-1111` skill 預設範本 |
| 求職系統（求職主網） | 求職者端 | `.claude/skills/spec-doc-1111/assets/template-jobseeker.md` |

如果使用者沒有明講是哪個專案，且從上下文（HackMD 資料夾、URL、截圖來源）無法判斷，要主動詢問，不要用錯範本硬寫。

## 2. 業務代碼表的權威來源

求才系統的權限／狀態／功能開關代碼（例如 `organs.showfield`、`organs.confirmed`、`oStatus`、`organsMore`、`interViewType`、`interViewKind` 等 bit-flag／enum 家族）**不在本 repo 內維護**，權威來源是 HackMD team note：

> `[REF] 求才系統代碼表`（note id `B1j3sN-bzx`）

規則：
- 規格書內任何提到上述代碼的地方，一律用相對連結 `[REF] 求才系統代碼表](/B1j3sN-bzx)` 指過去，**不要在別的文件裡複製代碼表**（複製會導致兩處不同步）。
- 如果使用者提供新的代碼（截圖、口頭說明），應該更新到 `B1j3sN-bzx` 本身，再讓其他文件連結過去，而不是就地寫死在當下正在編輯的規格書裡。
- 代碼表目前尚有未補完的項目（例如部分 `interViewKind` 代碼），遇到時依規格書慣例標記 `待補`，不要臆造數值。

## 3. API 契約文件的權威來源（同一支 API 一律參照）

後端提供的 API 文件（Request/Response、欄位定義、前端判斷）存放在本 repo：

| API | 權威文件 |
| --- | --- |
| `GET /api/v1/echat/get-detail/{infoNo}`（取得單筆對話完整內容，含 `oJsonB`／`tJsonB` 訊息明細） | `notes/api/echat-get-detail-infoNo.md` |

規則（**鐵律**）：
- 只要任務涉及**同一支 API**，一律先 Read 上表對應文件取用欄位定義／前端判斷，**不要**憑記憶、對話歷史或其他文件的轉抄版本作答（轉抄版可能過期）。
- 規格書／wiki／glossary 內提到該 API 的欄位或判斷邏輯時，以此文件為準；發現不一致時，以 `notes/api/` 的文件為權威，回頭修正其他文件。
- **未讀／已讀判斷**即定義於此：`Readflag`（0 未讀／1 已讀）、`OViewDate`（廠商已讀日期）、`TViewDate`（求職者已讀日期）——見 `notes/api/echat-get-detail-infoNo.md` 的 JsonB 欄位表。
- 後端釋出新版 API 文件時，**覆蓋更新** `notes/api/` 對應檔（保留同一檔名當作穩定引用點），不要另存新檔造成多份並存。
- 此文件是唯讀契約鏡像，內容以後端為準；不在此處自行改寫欄位語意。

## 4. 規格書格式慣例的索引

實際撰寫格式（章節編號階層、User Story/Use Case 寫法、MECE 四狀態表的適用範圍、🚧 待補規則區塊模板、跨文件引用三層方式、階段拆分慣例、交付前檢查清單）全部在 `spec-doc-1111` skill 裡，寫規格書時務必先用 `Skill` 工具載入該 skill，不要憑記憶套用舊格式。

## 5. 第三方系統整合（1HR）—— 新發現，尚待確認

從 `get-detail/{infoNo}`（見 §3 權威文件）的 API schema 發現一組標註「1HR用」／「求職端用」的欄位，目前**沒有任何規格書記錄這條整合線**，先在此存證，遇到相關規格再展開：

| 欄位 | 推測用途 |
| --- | --- |
| `WishReply` | 意願回覆內容（與 `ReplyWishMsg` 狀態碼搭配，待確認兩者關係） |
| `ReplyMailResult` | 回覆信件結果 |
| `MailTypeEhr` | 1HR 對應的信件類型代碼（與本系統 `Type`／`MailType` 的對照關係待確認） |
| `TalentNoEhr` | 1HR 端獨立的求職者（人才）編號，**不等於本系統的 `talentNo`** |
| `DepartNoEhr` | 1HR 端部門編號 |
| `ReplyWishMsgDateIn` | 意願回覆寫入時間 |
| `ReplyWishMsgDetailNo` | 意願回覆對應的訊息明細編號 |

**待確認**：1HR 是否為獨立第三方系統（與求才/求職系統並列的第三方對接），還是求才系統內部模組的別稱；上述欄位的實際業務流程目前無對應規格書記錄，遇到相關需求時要先向 PM 確認再動筆，不要憑欄位名稱臆測流程。
