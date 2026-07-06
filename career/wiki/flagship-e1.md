<!--markdownlint-disable MD033-->
<!--markdownlint-disable MD013-->

> 🧭 [← 職能框架首頁 / Home](../competency-framework.md) ｜ `career/` 個人職涯 wiki 分頁，非 1111 規格文件（規則見 [`career/CLAUDE.md`](../CLAUDE.md)）

# 旗艦專案 / Flagship Project — 跨系統聯絡人才（求才 ↔ 求職即時訊息）

> 至今**最具野心**的專案：打通**求才（廠商 B 端）↔ 求職主網（求職者 C 端）**兩套系統的即時訊息，是 F1／F2／F3／F6／F10 的**綜合輸出**。
> *Most ambitious project to date: a cross-system messaging feature bridging the employer (B-side) and jobseeker
> (C-side) platforms — a composite output evidencing F1/F2/F3/F6/F10.*
>
> 📖 **完整敘事版（問題→研究→方法→結果＋循序圖）見作品集案例：[`portfolio/e1-cross-system-messaging.md`](../portfolio/e1-cross-system-messaging.md)**。本頁為職能證據索引版。

- **跨系統即時推送 / Cross-system real-time push**：在求才端建單一聊天室介面，與求職主網**雙向同步**；以 **SignalR（底層 WebSocket）** 即時推播——統一頻道 `echathub`、連線帶 `Token`／`oNo`／`uNo`、訊息封包以 `H`(Hub)／`M`(Method，如 `sendMsgPush`／`onTextMessage`／`updateMsgReaded`)／`A`(Arguments) 描述、每則訊息產生 UUID、心跳維持連線、已讀狀態雙向同步。（協定握手等底層細節由 RD 負責，規格定義的是**業務層連線契約**。）
- **整合兩條 legacy 通道 / Unifying two legacy channels**：把原本分離的**即時通**與**信件**兩套來源（`MsgKind` 0/1）合併為單一對話流，建立廠商／求職者**雙視角訊息明細**（`oJsonB`／`tJsonB`），並以 `SendKind` 建模**跨系統寄件者路由**（含「即時通轉入」與「求才↔求職系統信」）。
- **跨系統收發管線 ＋ 計價／防呆 / Send-reply pipeline, pricing & guardrails**：定義求才→求職的 **6 步共同發送行為**（寫信件主表 → 寄 E-mail 給雙方 → 計算履歷瀏覽數 → `signalR` 通知求職主網＋推播 App → 前端即時更新），求職端回覆**鏡像同 6 步**；第 5 步即跨系統觸發點，同意面試則**雙寫面試行事曆**。內含**計價機制**（寄送前檢查並扣除廠商「履歷瀏覽數」配額，不足則不寄）與**送出防呆**（含 `留下LINE`／違規字 → 標 `DELFLAG` 不寄或直接阻擋）。
- **狀態機與業務邏輯 / State machine & business logic**：邀約狀態（詢問意願／面試邀約／錄取通知／感謝函／面試異動）、求職者意願回覆（`ReplyWishMsg`：0未回覆／1有意願／2婉拒／3更改時間）、**跨系統面試行事曆寫入**（求職者同意 → 求職後端寫雙方行事曆 → 聊天室即時顯示面試確認區塊）。
- **欄位級規格與相容遷移 / Field-level spec & compatible migration**：定義 `get-echat-mail-logs`／`get-detail/{infoNo}` 兩支 API 的 query／header／回傳欄位（含 30+ 欄位明細對照表）；以**現版↔新版命名對照**與 **iframe 串接現版 lightbox**（信件通知／封鎖／紀錄管理）做**漸進遷移、向後相容**；MECE 四狀態（載入／有資料／無資料／錯誤）全覆蓋。
- **規格治理量化亮點 / Quantified spec-governance highlights**：統整 **8+ 份異質來源**（3 份 HackMD 規格＋4 份後端 API 契約 PDF＋前端 component 展示站＋工程循序圖＋介面截圖）為單一事實來源；文件化 **4 支後端 API ＋ 1 套前端狀態機契約**；仲裁並定案 **3 處**長期標記「待確認」的業務代碼衝突（`詢問意願`＝`type1&interViewKind0`／`Type:8` 依 `interViewKind` 分流面試異動·取消／收回改以 `sendKind∈{7,8}` 判定）；建構含 **5 大階段**、涵蓋前端／後端／DB／即時推播／排程的完整跨系統流程模型。
- **工作證據 / Evidence**：HackMD `E.1 聯絡人才` 規格及其嵌入子文件 `跨系統流程與後端邏輯`（User Story／Use Case／權限判斷／API 欄位對照表／`oJsonB`／`tJsonB` 訊息明細／SignalR 動作對照表／**本人繪製的跨系統流程圖與循序圖（sequence diagram）**），本人為文件作者。
- **資深度訊號 / Seniority signal**：以**單一 PM** 之力定義橫跨**兩個系統、兩個後端、即時通訊＋既有信件**的整合架構——平台級系統思維與跨團隊（含 SignalR 工程協作）協調的綜合展現，是本框架技術深度最高的單一證據。

> ⚠️ **對外引用務必抽象化**：履歷／面試可述「跨系統即時訊息、整合兩條 legacy 通道」，但**勿外露**內部 API 名、欄位名、權限代碼（1111 機密）。

---

**相關分頁 / Related**：[作品集案例（完整敘事＋循序圖）](../portfolio/e1-cross-system-messaging.md) ・ [F2 功能規格與系統思維](F02-spec-systems-thinking.md) ・ [F10 業務邏輯梳理](F10-business-logic.md) ・ [履歷可用摘要](resume-extract.md)
