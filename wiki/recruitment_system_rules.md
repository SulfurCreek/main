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
| `GET /api/v1/external/echat/get-echat-mail-logs`（取得訊息紀錄列表） | `notes/api/echat-get-echat-mail-logs.md` |
| `GET /api/v1/external/echat/get-by-condition`（搜尋記訊內容） | `notes/api/echat-get-by-condition.md` |
| `POST /api/v1/external/echat/update-chatlog`（同步訊息狀態，記訊整併） | `notes/api/echat-update-chatlog.md` |

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

## 6. E.1「信件即時通整併」需求 —— 一律 inference based on 這批素材

**只要任務涉及 E.1 聯絡人才／信件即時通整併（聊天列表、聊天室、邀約卡片、訊息樣式、已讀未讀、陌生訊息、收回、跨系統收發、記訊整併…），一律先讀齊下表這批素材再推導，不要憑記憶或臆測。** 這批素材已彼此交叉驗證，是此功能的唯一事實來源（single source of truth）。

### 6.1 素材清單（權威來源）

| 類別 | 檔案 | 內容 |
| --- | --- | --- |
| 規格書 | `notes/E1-聯絡人才.md`（HackMD `cj-xlto2SdOtVskt3TkhdA`） | E.1 主規格：聊天列表／聊天室／邀約流程／初始化／權限 |
| 規格書 | `notes/H3-訊息樣式.md`（HackMD `_8_6BHe5Qhu4VXJqaYRKOA`） | 各訊息/邀約類型雙視角泡泡樣式＋ SendKind 逐一標註 |
| 後端邏輯 | `notes/uS9-跨系統流程與後端邏輯.md`（HackMD `uS9yE837SYedY9hQFneb6Q`） | 跨系統收發流程、共同發送/回覆行為、完整流程圖＋循序圖、SignalR 連線機制 |
| API 契約 | `notes/api/echat-get-detail-infoNo.md` | 單筆對話明細（`oJsonB`/`tJsonB` 全欄位、前端判斷、已讀未讀欄位） |
| API 契約 | `notes/api/echat-get-echat-mail-logs.md` | 聊天列表（摘要欄位、雙方最後查看時間） |
| API 契約 | `notes/api/echat-get-by-condition.md` | 關鍵字/條件搜尋（`sendType` 陌生訊息判斷、查詢層 `mailType`） |
| API 契約 | `notes/api/echat-update-chatlog.md` | 信件/即時通異動後的整併同步（EventBus） |
| 前端契約 | `notes/api/E1-component-showcase.md` | 前端 component 狀態機：`chatMessageMapper`、`toMailType`／`toInterviewStatus`、卡片矩陣、渲染優先序（實作以此為準） |
| 原始素材 | `notes/api/echat-engineering-sequence-original.md` | 工程端原始循序圖＋整合修正記錄 |
| 渲染快照 | `.claude/assets/E1/E1_component_showcase.html` | 前端展示站原始渲染（可瀏覽） |
| 截圖 | `.claude/assets/E1/*.png` | 各介面/狀態截圖 |

### 6.2 已由這批素材交叉驗證定案的關鍵結論（推導時直接引用，勿再標「待確認」）

- **`詢問意願` 判斷**：API 原始值 `type=1 & interViewKind=0`；前端 mapper `toMailType` 轉為內部 `mailType=2`（`Type:2` 是前端衍生碼，後端無此值）。
- **`Type:8` 分流**：`interViewKind=1` → 面試異動；`interViewKind=3` → 面試取消（`isCancel=true`，同一 mailType=8 的變體）。
- **寄件者/收回**：`sendKind` 0/9→廠商、1/10→求職者、7/8→已收回、3/4/5/6→系統訊息；收回判定改以 `sendKind∈{7,8}`（非 `revokeFlag`）。
- **意願狀態**：`replyWishMsg` 0/4→pending、1/3→accepted、2→rejected；膠囊「已通知無法赴約」與卡內「婉拒」語意刻意不同步。
- **已讀未讀**：訊息層級＝`readflag`＋`oViewDate`/`tViewDate`；列表層級 `unread` 後端尚未提供欄位，暫由 `oLastViewDate` vs `lastUpdate` 推導（聚合規則待定案）。
- **陌生訊息**：搜尋 API `sendType`：0求才發信／1求職者先發信(陌生)／-1排除陌生。

### 6.3 兩層 mailType 代碼（易混淆，務必分清）

- **查詢參數層**（`get-by-condition` 的 `mailType`）：`0一般 1面試邀約 2詢問意願 5感謝函 6到職確認 8面試異動 9即時通訊` —— 整併後語意，含 `2`。
- **jsonB 原始層**（`get-detail` 的 `type`）：原始信件類別，**無 `2`**，詢問意願靠 `type1+interViewKind0` 表達，前端才轉出 `mailType=2`。
- 兩者不可直接比對，`notes/api/echat-get-by-condition.md` 已標註。

### 6.4 尚未定案、遇到時要標記待確認並向 PM/RD 詢問

- 列表未讀紅點的實際聚合來源（後端補欄位 or 前端算）。
- 面試卡 `expired` 的逾期判定邏輯（`wishReplyDate` 計算）。
- 檔案訊息（`type='file'`）的泡泡樣式（訊息樣式文件未涵蓋）。
- 1HR/EHR 整合線的完整業務流程（見 §5）。
- `update-chatlog` 的實際呼叫方（後端自呼 or 獨立 Mail/即時通服務）。
