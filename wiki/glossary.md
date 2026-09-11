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
- **「錄取通知」vs「到職確認」**（`mailType=6`，同一件事的兩個名稱）：**目標名稱是「錄取通知」**——E.1 聯絡人才完成上線後，所有文件統一改用「錄取通知」。在那之前，既有文件與後端文件沿用的「到職確認」**現階段可接受**，不需要為此回頭改舊文件；新寫的文件優先用「錄取通知」。遇到兩者並存時視為同義，不要標成 🚧 待確認。
- **`Type`(`MailType`)**：信件／訊息類別（一般訊息／面試邀約／感謝函／錄取通知／面試異動…）。**代碼枚舉見 `uS9yE837SYedY9hQFneb6Q` §5.1，本檔不複製。**
- **`interViewKind`**（即訊息 schema 內的 `InterViewKind`）：與 `Type`(`MailType`) **搭配**判斷邀約子類型——單看 `Type` 不足以決定卡片樣式，這是本欄位存在的意義。**代碼枚舉見 `uS9yE837SYedY9hQFneb6Q` §5.3**（該處另標明「訊息明細的 `InterViewKind`」與「篩選參數 `interviewKind`」代碼不同，勿混用）。組合判斷規則見 `wiki/recruitment_system_rules.md §6.2`。
- **`SendKind`**：寄件者代碼（廠商／求職者／系統訊息／已收回／即時通轉入）。**代碼枚舉與雙視角顯示規則見 `uS9yE837SYedY9hQFneb6Q` §5.2，本檔不複製。**
- **`ReplyWishMsg`**：求職者意願回覆狀態。**代碼枚舉見 `uS9yE837SYedY9hQFneb6Q` §5.4。**

> **代碼枚舉一律不落在本 repo。** 兩個權威來源：
>
> - 信件即時通整併相關（`Type`／`SendKind`／`InterViewKind`／`ReplyWishMsg`／`notifyType` 等）→ `[REF] 信件即時通整併－API 與代碼對照庫`（`uS9yE837SYedY9hQFneb6Q`）
> - 求才系統權限／狀態／開關（`showfield`／`confirmed`／`oStatus` 等）→ `[REF] 求才系統代碼表`（`B1j3sN-bzx`）
>
> 本檔只解釋「這個詞在講什麼、為什麼存在」，不列數值；規則見 `wiki/recruitment_system_rules.md §2`。

## 規格書撰寫慣例術語

- **MECE 四狀態表**：載入中／有資料／無資料／錯誤，規格書中非同步資料載入區塊（資料載入、列表、搜尋）的標準呈現方式。
- **🚧 待補規則區塊**：`:::warning` 包住、標題帶 🚧、內文紅字，固定結構為「現況 → 缺口 → 待確認（checkbox 清單）→ 來源」，用於標記規格**未定案、需要 PM 裁示**的部分。
- **判斷條件欄位（新舊代碼共存）**：當同一業務類型橫跨新舊代碼（如新版單一 `Type`、舊資料是 `Type`+`InterViewKind` 組合）時，表格欄名用 `判斷條件`，欄內以 `<ul><li>` 列舉現行代碼＋各組「舊資料：」相容代碼。這是**已確認**的相容規則，不要誤標成 🚧 待補規則（後者只用於尚待 PM 確認的衝突）。
- **`{%hackmd <noteId> %}`**：HackMD 原生全文嵌入語法，把另一份 note 的內容就地渲染（通常包在 `:::spoiler` 內）。
- **相對 note 連結**：`[標題](/noteId)`，同一 team workspace 下規格書互連的標準寫法，不用完整 URL。
- **階段拆分**：把第二階段功能拆成獨立 HackMD 文件，第二階段文件每節記 `> 來源：原 §x`，第一階段文件保留入口並連結過去。

## 訊息／邀約卡片規格術語

- **邀約訊息 / Interview Card**：聊天室內以卡片呈現的訊息類型，含 `詢問意願`／`面試邀約`／`面試異動`／`錄取通知`／`婉拒（感謝函）`，依 `Type`(`MailType`) + `InterViewKind` **共同**判斷對應泡泡（現行＋舊資料相容代碼已於 `_8_6BHe5Qhu4VXJqaYRKOA` 確認）。**組合對照表見 `uS9yE837SYedY9hQFneb6Q` §5.1／§5.3 與 `wiki/recruitment_system_rules.md §6.2`，本檔不複製。**
- **雙視角（發出↔收到）**：同一則跨系統訊息在收發兩端各有不同呈現，規格拆成 `#### 廠商發出：X` / `#### 求職者收到：X` 兩個視角（動作與類型間用冒號分隔）；泡泡靠邊（廠商靠右／求職者靠左）與角落資訊欄名（右下角／左下角）隨視角相反。寫法見 `spec-doc-1111` skill。
- **操作狀態（互動狀態）**：互動元件（邀約卡片按鈕、可回覆訊息）的狀態軸，逐一列舉如 `未選擇`／`已選擇`／`已婉拒`／`已過期`（多半標 `disabled`），有別於資料載入的 MECE 四狀態（載入中／有資料／無資料／錯誤）。
- **意願狀態標籤**：求職者回覆後系統自動寫入、雙方都看得到的提示文字（如「施小君已回覆有意願面試」）。雙視角文案差異：廠商側用第三人稱主詞、求職者側用第二人稱（「你已…」）；有意願／同意＝綠色、無意願／婉拒＝灰色。後端對應欄位 `ReplyWishMsg`（代碼見 `uS9yE837SYedY9hQFneb6Q` §5.4）；其中「更改時間」（面試邀約「選擇其他時間」按鈕）的標籤文案與樣式待補。
- **跨系統流程與後端邏輯（獨立文件）**：寫信件主表／寄 E-mail／signalR／推播／面試行事曆等後端步驟集中於一份獨立 note，各訊息類型在「點擊後狀態」末尾用相對連結 `[跨系統流程與後端邏輯](/noteId)` 指過去，不在每處重複展開。

## 即時通（聊天室）名稱對照

聊天室即時訊息採 SignalR（底層 WebSocket）雙向推播。規格書只記錄業務名稱與邏輯，技術機制屬 RD 範疇不展開（見 `spec-doc-1111` 核心原則「讀者是 PM」）。權威紀錄在 HackMD note `跨系統流程與後端邏輯`（`uS9yE837SYedY9hQFneb6Q`）。

- **`echathub`**：聊天頻道名稱（Hub），全系統統一用這個。
- **`H` / `M` / `A`**：即時訊息的三個欄位 —— `H`(Hub) 頻道名、`M`(Method) 觸發的動作、`A`(Arguments) 動作所需資料陣列。
- **連線帶入參數**：`Token`（登入憑證）／`oNo`（公司編號）／`uNo`（使用者編號）。
- **常用動作（M）**（依 `uS9yE837SYedY9hQFneb6Q` v11 定案，分「保留／廢止」）：
  - 保留：`setoUser`（求才上線報到）／`settUser`（求職上線報到）／`updateMsgReaded`（標記已讀）／`onSignal`（後端推播的統一接收事件，**只用於接收**，取代舊 `onTextMessage`）。
  - 廢止：`onTextMessage`（舊接收事件，由 `onSignal` 取代）／`sendMsgPush`（SignalR invoke 送出——送出一律改走 WebAPI：求才 `eChatHandler.ashx?kind=5`、求職自有送出 API，皆為原有 API 而非新增）／`setRoomInfo`、`getUserStatus`（求職端，不再使用）。
