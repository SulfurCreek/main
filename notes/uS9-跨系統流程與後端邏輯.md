<!--markdownlint-disable MD033-->
<!--markdownlint-disable MD013-->

# 跨系統流程與後端邏輯

> 本章描述求才系統與求職系統之間的訊息收發後端／DB 邏輯，依完整系統流程圖整理。
> 主動方＝求才廠商；求職者收到通知後回到「求職主網」回覆。

## 版控紀錄

| 版本 | 日期 | 調整說明（異動區段 + 摘要） |
| :---: | :--- | :--- |
| v6 | 2026-07-03 | [循序圖] 進頁一併載列表＋指定室明細＋建 SignalR；連線時機＝選定聊天室當下；`update-chatlog` 緊接寫主表；驗證失敗以 `break` 擋住不入庫；面試邀約額外寫面試行事曆；寄信收件人明確化；求職端頁面正名「聯絡公司」 |
| v7 | 2026-07-03 | [循序圖／推播段] 依 `echat-realtime-push-flow` 真實鏈路重繪（EventBus→`apiSendMessage.ashx`→`onSignal`＋FCM／APNS）；新增 `senderType` 分流 |
| v8 | 2026-07-03 | [送出／接收] 送出只走 WebAPI（前端不 invoke）；接收僅收 KEY，打 `get-detail` 整包重撈整室渲染 |
| v9 | 2026-07-03 | [接收事件] 統一 `onSignal`（取代 `onTextMessage`），參數只增不改；同步翻修 SignalR 章節、標記廢止事件 |
| v10 | 2026-07-06 | [送出 API] 不跨系統共用（求才 `eChatHandler.ashx`／求職自有）；保留 `setoUser`／`updateMsgReaded`／`settUser`；`onSignal` 內含打取對話 API 的參數 |
| v11 | 2026-07-06 | [接收] `onSignal` 帶 `updateId` 判斷已存在資料；`bNo` 作 cursor 查新資料（唯一取對話 API 仍回整包） |
| v12 | 2026-07-08 | [接收] 求才端接收流程正式確認：`onSignal`→`get-detail` 取全部、`updateId`＋`bNo` cursor |
| v13 | 2026-07-08 | [接收] 結案：求職端取對話共用 `get-detail`（送出仍各端獨立）；`bNo` cursor 為伺服器端機制 |
| v14 | 2026-07-15 | [三支查詢 API／循序圖搜尋段] 依工程端更新的 `get-by-condition` Query 補 `cursor`（＝`infoNo`）＋`limit` 分頁與星號／通知信分類／回覆狀態等篩選；釐清列表 cursor（`infoNo`）與接收 cursor（`bNo`）之別；同步 `notes/api/echat-get-by-condition.md` |

## 進入頁面／搜尋／進聊天室（三支查詢 API）

聊天室相關資料載入，共用三支「信件即時通整併」API（權威文件見 `notes/api/` 對應檔）：

| 場景 | API | 說明 |
| :--- | :--- | :--- |
| 進入聯絡人才頁，載入左側聊天列表 | `GET get-echat-mail-logs`（`notes/api/echat-get-echat-mail-logs.md`） | `cursor`（＝`infoNo`）＋`limit` 分頁；回傳含 `oLastViewDate`／`tLastViewDate`／`lastUpdate`，可推導列表未讀判斷 |
| 搜尋關鍵字／切換一般·陌生訊息 Tab | `GET get-by-condition`（`notes/api/echat-get-by-condition.md`） | `cursor`（＝`infoNo`）＋`limit` 分頁；篩選條件含已讀狀態、意願回覆、信件類別、面試類別、星號、通知信分類、回覆狀態；`sendType` 為陌生訊息判斷依據（0求才發信/1求職者先發信=陌生訊息/-1排除陌生訊息） |
| 進入聊天室，載入單筆對話明細 | `GET get-detail/{infoNo}`（`notes/api/echat-get-detail-infoNo.md`） | `infoNo`＝列表回傳的 `rNo`；回傳 `oJsonB`／`tJsonB` 訊息明細 |

> **兩種 cursor 勿混**：列表／搜尋分頁的 cursor＝`infoNo`（指標，見上表 `get-echat-mail-logs`／`get-by-condition`）；聊天室「接收新訊息」的 cursor＝`bNo`（訊息明細流水號，見〈[SignalR 連線機制](#signalr--websocket-即時通連線機制)〉§4）。前者用於翻頁、後者用於抓某對話 `bNo` 之後的新訊息，兩者是不同層級的指標。

## 共同發送行為（求才系統）

廠商送出任一類型（詢問意願／面試邀約／錄取通知／一般訊息／感謝函）後觸發：

| # | 動作 | 端 |
| :--: | :--- | :--- |
| 0 | 驗證廠商點數與職缺權限、計算並檢查履歷瀏覽數 —— **失敗則擋住，不寫入資料庫** | 求才後端 |
| 1 | 寫入信件主表 | 求才後端 |
| 1.5 | 呼叫 `POST update-chatlog`（`notes/api/echat-update-chatlog.md`）同步整併記訊狀態 | 求才後端 |
| 2 | 將「給求職者的通知信」**加入寄信排程**（不即時寄出，處理很快但非馬上送出） | 求才後端 |
| 3 | 將「給廠商副本收件人的信」加入寄信排程 | 求才後端 |
| 4 | 計算履歷瀏覽數（與其他雜項判斷） | 求才後端 |
| 5 | signalR 通知求職主網有新訊息、發送推播給求職 App | 求才後端 |
| 6 | 廠商畫面即時更新 | 求才前端 |

> 第 5 項（signalR／推播）為求職者收到通知、回到求職主網的觸發來源；連線機制見〈[SignalR / WebSocket 即時通連線機制](#signalr--websocket-即時通連線機制)〉。
>
> **第 4 項「計算履歷瀏覽數」細節**（舊版 [4.1 §5.2](/r1ghrPxP-x)）：寄出時寫入發信排程，執行排程時即時檢查廠商當日履歷瀏覽數是否足夠 —— 不足則不執行發信排程；足夠且成功寄出後扣除履歷瀏覽數。
>
> **寄出前檢查**（舊版 [4.1 §2.4／v1.0.4](/r1ghrPxP-x)，既有後端規則，新版沿用待確認）：
> 1. 含指定關鍵字 `留下LINE`（不分大小寫全半形）／`留下賴`：訊息仍寫入資料庫並標 `DELFLAG`、**不寄送 Email**，前台依求職規則顯示或隱藏。
> 2. 含違規字眼（如 `104`）：點「寄出」時不顯示 loading，直接 alert 阻擋送出（`內容含有違規字詞，請調整後再送出。`）。

## 共同回覆行為（求職系統）

求職者於求職主網回覆後，鏡像對應「共同發送行為」，執行端改為求職系統（列於此處供跨系統脈絡參照）：

| # | 動作 | 端 |
| :--: | :--- | :--- |
| 1 | 更新回覆／面試狀態（如「已接受」、`ReplyWishMsg`） | 求職後端 |
| 2 | 寫入信件主表＝自動寫入系統對話紀錄（系統訊息 與 一般訊息） | 求職後端 |
| 2.5 | 呼叫 `POST update-chatlog` 同步整併記訊狀態 | 求職後端 |
| 3 | 判斷回信類別：**一般訊息**→加入廠商帳號（信件收件人）的「**收信區間排程**」（每帳號設定的收信區間不同，依區間彙整寄出）；**其他類別**（意願回覆等）→加入一般寄信排程 | 求職後端 |
| 4 | 將「給廠商副本收件人的信」加入寄信排程 | 求職後端 |
| 5 | 計算回覆狀態（與其他雜項判斷） | 求職後端 |
| 6 | signalR 通知求才系統有新訊息、發送推播給求才 App | 求職後端 |
| 7 | 求職者畫面即時更新 | 求職前端 |

> 回覆完成後另判斷：若回覆為同意面試，求職後端額外寫入面試行事曆（求才與求職雙方）。
> 「回覆有無意願」分支由求職前端帶入系統預設文字（如「我有意願」）寫入一般訊息；自由文字回覆則由求職者自行輸入。

## 類型 → 回覆方式對照

| 發送的邀約類型 | 求職者回覆方式 | 回覆後特殊處理 |
| :--- | :--- | :--- |
| 詢問意願 | 回覆有無意願（有意願 / 婉拒） | — |
| 面試邀約 | 回覆有無意願（接受指定時段 / 婉拒面試 / 更改時間） | 接受 → 寫入面試行事曆；更改時間 → 求職者要求其他時段（後續流程 `待補`） |
| 錄取通知 | 回覆有無意願（同意報到 / 婉拒） | — |
| 一般訊息 | 自由文字回覆 | — |
| 感謝函 | 不可回覆，對話結束 | — |

> 後端 `ReplyWishMsg` 值對照（來源：`get-detail/{infoNo}` schema）：`0`未回覆／`1`有意願／`2`婉拒／`3`更改時間。

## 完整流程圖

```mermaid
flowchart TD
    Start(["廠商發起對話"]):::actor --> HasChat{"廠商與求職者<br/>是否已有對話紀錄"}:::decision

    HasChat -->|無對話紀錄| NewChat["位置：人才名單 或 履歷畫面<br/>於信件主表建立新對話<br/>帶入職缺等必要欄位"]:::cfg
    HasChat -->|已有對話紀錄| InChat["位置：聊天室畫面<br/>延續現有對話"]:::cfg
    NewChat --> SendType
    InChat --> SendType

    SendType{"發送的邀約類型"}:::decision
    SendType -->|詢問意願| C1["設定意願詢問內容"]:::cfg
    SendType -->|面試邀約| C2["設定面試資料"]:::cfg
    SendType -->|錄取通知| C3["設定報到資料"]:::cfg
    SendType -->|一般訊息| C4["輸入文字訊息"]:::cfg
    SendType -->|感謝函| C5["設定婉拒感謝內容"]:::cfg

    subgraph SEND["共同發送行為（求才系統）"]
      direction TB
      SA0["求才後端：驗證點數／職缺權限、檢查履歷瀏覽數<br/>（失敗則擋住，不寫入資料庫）"]:::backend
      SA0 --> SA1["求才後端：寫入信件主表"]:::backend
      SA1 --> SAU["求才後端：呼叫 update-chatlog<br/>同步整併記訊狀態"]:::backend
      SA1 --> SA2["求才後端：通知信加入寄信排程<br/>（給求職者）"]:::backend
      SA1 --> SA3["求才後端：通知信加入寄信排程<br/>（給廠商副本收件人）"]:::backend
      SA1 --> SA4["求才後端：計算履歷瀏覽數（與其他雜項判斷）"]:::backend
      SA1 --> SA5["求才後端：signalR 通知求職主網新訊息<br/>發送推播給求職 App"]:::backend
      SA1 --> SA6["求才前端：廠商畫面即時更新"]:::frontend
    end

    C1 --> SA1
    C2 --> SA1
    C3 --> SA1
    C4 --> SA1
    C5 --> SA1

    SA5 --> Seek(["求職者收到通知<br/>回到求職主網"]):::seeker
    Seek --> Reaction{"該類型的回覆方式"}:::decision
    Reaction -->|詢問意願、面試邀約、錄取通知| RWill["回覆有無意願<br/>有意願 或 婉拒<br/>（前端帶入系統預設文字）"]:::reply
    Reaction -->|一般訊息| RText["自由文字回覆"]:::reply
    Reaction -->|感謝函| EndChat(["不可回覆<br/>對話結束"]):::endnode
    subgraph REPLY["共同回覆行為（求職系統）"]
      direction TB
      RA1["求職後端：寫入信件主表<br/>（系統訊息 與 一般訊息）"]:::backend
      RA1 --> RAU["求職後端：呼叫 update-chatlog<br/>同步整併記訊狀態"]:::backend
      RA1 --> RA2{"回信類別"}:::decision
      RA2 -->|一般訊息| RA2a["加入廠商帳號收信區間排程<br/>（各帳號設定不同區間）"]:::backend
      RA2 -->|其他類別| RA2b["通知信加入寄信排程<br/>（給廠商信件收件人）"]:::backend
      RA1 --> RA3["求職後端：通知信加入寄信排程<br/>（給廠商副本收件人）"]:::backend
      RA1 --> RA4["求職後端：計算回覆狀態（與其他雜項判斷）"]:::backend
      RA1 --> RA5["求職後端：signalR 通知求才系統新訊息<br/>發送推播給求才 App"]:::backend
      RA1 --> RA6["求職前端：求職者畫面即時更新"]:::frontend
    end

    RWill --> RA1
    RText --> RA1
    RA1 --> Cal{"回覆為同意面試"}:::decision
    Cal -->|是| WriteCal["求職後端：額外寫入面試行事曆<br/>（求才與求職雙方）"]:::special
    Cal -->|否| Done(["本輪互動完成"]):::actor
    WriteCal --> Done

    classDef actor fill:#dbeafe,stroke:#3b82f6,stroke-width:2px,color:#1e3a5f;
    classDef decision fill:#fef9c3,stroke:#eab308,stroke-width:2px,color:#713f12;
    classDef cfg fill:#f1f5f9,stroke:#94a3b8,stroke-width:2px,color:#334155;
    classDef seeker fill:#ede9fe,stroke:#8b5cf6,stroke-width:2px,color:#4c1d95;
    classDef reply fill:#ccfbf1,stroke:#14b8a6,stroke-width:2px,color:#115e59;
    classDef special fill:#fce7f3,stroke:#ec4899,stroke-width:2px,color:#831843;
    classDef endnode fill:#fee2e2,stroke:#ef4444,stroke-width:2px,color:#7f1d1d;
    classDef backend fill:#dcfce7,stroke:#16a34a,stroke-width:2px,color:#14532d;
    classDef frontend fill:#bfdbfe,stroke:#2563eb,stroke-width:2px,color:#1e3a5f;
    style SEND fill:#f0fdf4,stroke:#22c55e,stroke-width:2px;
    style REPLY fill:#faf5ff,stroke:#a855f7,stroke-width:2px;
```

## 完整流程圖（循序圖 Sequence Diagram）

> 與上方 `完整流程圖` 同一套邏輯，改以循序圖呈現，並整合工程端提供的前後端技術流程（原始版見 `notes/api/echat-engineering-sequence-original.md`）＋四支 API 的實際呼叫位置。依時間順序排列，並把「使用者／系統端」與「每個 action」分開。

```mermaid
---
config:
  theme: base
  rightAngles: true
  themeVariables:
    fontFamily: "Inter, Helvetica, Arial, sans-serif"
    primaryColor: "#F4F5F7"
    primaryBorderColor: "#C1C7D0"
    primaryTextColor: "#172B4D"
    signalColor: "#42526E"
    signalTextColor: "#333333"
    noteBkgColor: "#FFF0B3"
    noteBorderColor: "#FFC400"
  sequence:
    actorFontSize: 17
    actorFontWeight: bold
    messageFontSize: 16
    noteFontSize: 15
    wrap: true
    wrapPadding: 12
    actorMargin: 70
    boxMargin: 12
    boxTextMargin: 8
    messageMargin: 42
    mirrorActors: false
---
sequenceDiagram
    autonumber

    box rgba(100,150,200,0.1) 求才系統
        actor Emp as 求才廠商
        participant RF as 求才前端
        participant RB as 求才後端
    end

    box rgba(200,200,200,0.1) 共用基礎設施
        participant DB as 資料庫
        participant Bus as 事件匯流排<br>（EventBus）
        participant Push as 推播服務<br>（apiSendMessage.ashx）
        participant Hub as 即時推播<br>（eChatHub SignalR／FCM／APNS）
    end

    box rgba(180,160,200,0.1) 求職系統
        participant SB as 求職後端
        participant SF as 求職前端<br>（求職主網／App）
        actor Seeker as 求職者
    end

    %% ===== 一、進入聯絡人才頁（整併原一＋三：載入列表＋指定聊天室明細＋SignalR） =====
    rect rgb(227, 242, 253)
    Note over Emp,DB: 一、進入「聯絡人才」頁（載入左側列表；正常情況已指定聊天室 → 一併載入該室明細並建立 SignalR）
    Emp->>RF: 進入「聯絡人才」頁
    RF->>RB: GET get-echat-mail-logs<br>（廠商編號／職缺編號，limit＋cursor 分頁）
    RB->>DB: 查詢整併後的記訊列表
    DB-->>RB: 每筆對話摘要
    RB-->>RF: 回傳列表（最後一則訊息、最後訊息類型、<br>雙方最後查看時間、意願回覆狀態、釘選、訊息數量統計）
    Note over RF: 渲染左側聊天列表：<br>信件類型標籤＝最後訊息類型<br>未讀判斷＝比對「公司最後查看時間」與「最後更新時間」
    alt 已指定聊天室（正常情況：由通知／URL 帶入 rNo）
        RF->>RB: GET get-detail/{infoNo}<br>（載入指定聊天室明細，infoNo＝該筆 rNo）
        RB->>DB: 取得該筆對話完整內容
        DB-->>RB: 對話資料＋廠商視角／求職者視角訊息明細
        RB-->>RF: 回傳廠商視角訊息明細
        Note over RF: 依明細渲染右側聊天室：<br>寄件者代碼→泡泡左右與收回樣式<br>信件類別＋面試類別→一般訊息／邀約卡片<br>已讀未讀＝訊息已讀旗標＋雙方已讀日期
        RF->>Hub: 建立 SignalR 連線並加入該聊天室頻道<br>（登入憑證、公司編號、使用者編號，頻道 echathub）
        Note over Hub: 進入指定聊天室即連線；固定間隔心跳偵測、斷線自動重連
    else 未指定聊天室（僅載入列表，待點選）
        Emp->>RF: 點選左側某筆對話（選擇聊天室）
        Note over RF,Hub: 走上方相同流程：GET get-detail 載入該室明細 → 建立 SignalR 連線並加入頻道
    end
    end

    %% ===== 二、搜尋與篩選 =====
    rect rgb(255, 249, 230)
    opt 二、搜尋關鍵字 或 切換篩選 Tab（一般／陌生訊息）
        Emp->>RF: 輸入關鍵字／切換 Tab
        RF->>RB: GET get-by-condition<br>（keyword、已讀未讀、意願回覆、信件類別、面試類別、<br>發送類型、星號、通知信分類、回覆狀態、日期區間、<br>cursor=infoNo＋limit 分頁…）
        Note over RB: 發送類型判斷陌生訊息：<br>0＝求才發信／1＝求職者先發信（陌生訊息）<br>／-1＝排除陌生訊息
        RB->>DB: 依條件搜尋歷史記訊
        DB-->>RB: 符合條件的對話
        RB-->>RF: 回傳搜尋結果（含對話明細）
    end
    end

    %% ===== 三、廠商發送訊息／邀約 ＋ 共同發送行為 =====
    alt 無對話紀錄
        Emp->>RF: 於人才名單／履歷畫面發起新對話<br>（帶職缺等必要欄位）
    else 已有對話紀錄
        Emp->>RF: 於聊天室畫面延續現有對話
    end

    Note over Emp,RF: 選擇邀約類型並設定內容：<br>詢問意願／面試邀約／錄取通知<br>／一般訊息／感謝函
    Emp->>RF: 送出（帶入該類型內容）
    RF->>RB: 提交發送請求（對話編號＋卡片內容）<br>※求才端送出走 eChatHandler.ashx（kind=5）WebAPI，前端不做 SignalR invoke；<br>SignalR 連線只用於「接收」信號
    activate RB

    rect rgb(232, 245, 233)
    Note over RB,DB: 三、共同發送行為（求才系統）

    %% ----- 寫入前檢查：前後端溝通，失敗即擋住、不觸碰資料庫 -----
    RB->>RB: 驗證廠商點數與職缺權限<br>（前後端溝通，尚未觸碰資料庫）
    RB->>RB: 計算並檢查履歷瀏覽數<br>（與其他雜項判斷）
    break 驗證或檢查未通過
        RB-->>RF: 回傳錯誤，擋住送出<br>（此請求根本不會送到資料庫）
    end

    RB->>DB: 寫入信件主表<br>（eChatFunc.SaveMsgLog()，結構化訊息寫入對話紀錄，<br>驗證通過後第一次寫入資料庫；唯一寫入點）

    opt 發送類別為面試邀約
        RB->>DB: 額外寫入一筆面試資料至面試行事曆資料表<br>（求才端；面試欄位隨發送請求帶入）
    end

    %% ----- 信件即時通整併：緊接寫入之後同步 -----
    Note over RB,Bus: 信件／即時通有異動 → 同步記訊狀態
    RB->>Bus: POST update-chatlog<br>（廠商編號、履歷編號、職缺編號、<br>異動類型 0兩表／1信件／2即時通、異動編號）
    activate Bus
    Bus->>DB: 下游服務合併／更新記訊狀態<br>（即時通＋信件整併為單一對話紀錄）
    Bus-->>RB: 成功（true）
    Bus->>Push: 發送訊息事件，觸發 apiSendMessage.ashx
    deactivate Bus

    activate Push
    Push->>Push: 驗證簽章／Token；senderType=1（企業）<br>→ 查詢求職者是否在線 GetTalentUserOnline(tNo)
    alt 求職者在線 且 MsgType=0
        Push->>Hub: hubContext.Clients.User(tNo).onSignal<br>(ContextID="apiSendMessage", tNo, oNo, uNo, eNo, MsgLog)
        Hub-->>SF: 即時推送 onSignal（接收事件名，取代舊版 onTextMessage）<br>（前端忽略 MsgLog；其餘 KEY 參數 tNo／oNo／uNo／eNo 即後續打「取對話 API」的參數；<br>參數原有的都保留、只增不改，新增參數一律附加在後面──擴充中）
    end
    Push->>Hub: DoApiPushMessage（uType=1, Silent=0）
    deactivate Push
    Hub-->>SF: FCM／APNS 手機推播（求職 App）

    Note over SF: 求職前端收到 onSignal 後（SignalR 只傳 KEY 值，正常情況含 updateId）：<br>若為目前開啟中的聊天室 → 用 onSignal 帶的參數打 get-detail（求才／求職共用同一支取對話 API）<br>前端帶上本地已存最大 bNo，讓 SignalR／後端知道要從哪裡開始更新（只回該 bNo 之後的新資料）；<br>以 updateId 判斷已存在／未存在資料，不必每次都整室重新渲染<br>若非目前開啟的聊天室 → 僅更新未讀提示圖示，不打 API

    %% ----- 寄信排程：兩封信最終各自寄到求職者 / 廠商副本收件人 -----
    RB-->>Seeker: 通知信加入寄信排程 → 寄至求職者 email<br>（非即時，由排程送出，處理時間很短）
    RB-->>Emp: 副本通知信加入寄信排程 → 寄至廠商副本收件人 email<br>（可視為求才廠商）
    RB-->>RF: 傳送成功
    deactivate RB
    Note over RF: 聊天泡泡轉為「傳送成功」<br>（廠商畫面即時更新）
    end

    %% ===== 四、求職者收到通知 → 進入「聯絡公司」頁 =====
    SF->>Seeker: 顯示新訊息通知
    Seeker->>SF: 進入「聯絡公司」頁

    rect rgb(232, 234, 246)
    Note over Seeker,Hub: 四、求職者進入「聯絡公司」頁（分辨是否已指定聊天室；有指定則立即建立 SignalR 連線）
    alt 已指定聊天室（如由通知／信件點入該對話）
        SF->>SB: 載入該對話明細（走列表／明細 API，固定帶求職者編號；<br>搜尋僅查最後一筆訊息）
        SB-->>SF: 回傳求職者視角訊息明細
        SF->>Hub: 立即建立 SignalR 連線並加入該聊天室頻道<br>（求職端身分，頻道 echathub）
    else 未指定聊天室（僅載入列表，待點選）
        Seeker->>SF: 點選某筆對話（選擇聊天室）
        SF->>SB: 載入該對話明細
        SB-->>SF: 回傳求職者視角訊息明細
        SF->>Hub: 建立 SignalR 連線並加入該聊天室頻道
    end
    end

    Note over SF,SB: 求職端送出走「求職自己提供的 API」（非 eChatHandler.ashx）；<br>認證用求職端各自的 cookie、參數與求才端不同
    alt 感謝函
        Note over SF,Seeker: 不可回覆，對話結束
    else 詢問意願／面試邀約／錄取通知
        Seeker->>SF: 點擊卡片按鈕回覆有無意願<br>（同意／婉拒，前端帶入系統預設文字）
        SF->>SB: 提交回覆（求職自有送出 API）
    else 一般訊息
        Seeker->>SF: 自由文字回覆
        SF->>SB: 提交回覆（求職自有送出 API）
    end

    rect rgb(243, 229, 245)
    opt 有回覆（非感謝函）
        activate SB
        Note over SB,DB: 五、共同回覆行為（求職系統）
        SB->>DB: 更新回覆／面試狀態<br>（面試狀態「已接受」、意願回覆代碼）
        SB->>DB: 寫入信件主表＝自動寫入系統對話紀錄<br>（系統訊息 與 一般訊息；唯一寫入點）

        %% ----- 信件即時通整併：緊接寫入之後同步 -----
        Note over SB,Bus: 信件／即時通有異動 → 同步記訊狀態
        SB->>Bus: POST update-chatlog<br>（廠商編號、履歷編號、職缺編號、<br>異動類型、異動編號）
        activate Bus
        Bus->>DB: 下游服務合併／更新記訊狀態<br>（即時通＋信件整併）
        Bus-->>SB: 成功（true）
        Bus->>Push: 發送訊息事件，觸發 apiSendMessage.ashx
        deactivate Bus

        activate Push
        Push->>Push: 驗證簽章／Token；senderType=2（求職者）<br>→ 查詢廠商該使用者是否在線 GetOrganUserOnline(oNo, uNo)
        alt 廠商在線 且 MsgType=0
            Push->>Hub: hubContext.Clients.User(oNo_uNo).onSignal<br>(ContextID="apiSendMessage", tNo, oNo, uNo, eNo, MsgLog)
            Hub-->>RF: 即時推送 onSignal（取代舊版 onTextMessage）<br>（前端忽略 MsgLog；其餘 KEY 參數即後續打「取對話 API」的參數）
        end
        Push->>Hub: DoApiPushMessage（uType=2, Silent=1）
        deactivate Push
        Hub-->>RF: FCM／APNS 手機推播（求才 App）

        Note over RF: 求才前端收到 onSignal 後（SignalR 只傳 KEY 值，正常情況含 updateId）：<br>若為目前開啟中的聊天室 → 用 onSignal 帶的參數打 get-detail（求才／求職共用同一支取對話 API）<br>前端帶上本地已存最大 bNo，讓 SignalR／後端知道要從哪裡開始更新（只回該 bNo 之後的新資料）；<br>以 updateId 判斷已存在／未存在資料後更新畫面，卡片狀態更新為「已接受」等（含插入意願狀態標籤）<br>若非目前開啟的聊天室 → 僅更新未讀提示

        %% ----- 依回信類別決定寄信方式（兩種方式終點都是求才廠商） -----
        SB->>SB: 判斷回信類別
        alt 一般訊息
            SB-->>Emp: 加入廠商帳號「收信區間排程」→ 依各帳號設定的區間<br>彙整後寄至求才廠商 email
        else 意願回覆等其他類別
            SB-->>Emp: 即時寄信給求才廠商<br>（信件收件人，不經排程，立即寄出）
        end
        SB-->>Emp: 副本通知信加入寄信排程 → 寄至廠商副本收件人 email

        SB->>SB: 計算回覆狀態（與其他雜項判斷）
        SB-->>SF: 處理成功<br>求職者畫面即時更新

        alt 回覆為同意面試
            SB->>DB: 額外寫入面試行事曆<br>（求才與求職雙方）
        end
        deactivate SB
        RF->>Emp: 廠商畫面即時更新<br>（顯示求職者回覆）
    end
    end
```

## SignalR / WebSocket 即時通連線機制

> 聊天室的即時訊息採 **SignalR**（底層走 WebSocket）推播：本次「信件即時通整併」改版後，SignalR 連線**只負責「接收」信號**，訊息送出一律走 WebAPI（見下方新版流程）。本章只記錄業務邏輯與相關名稱供對照；協定握手、連線升級等技術細節屬 RD 範疇，不在此展開。
> 推播鏈完整技術文件見 `notes/api/echat-realtime-push-flow.md`。

### 連線時機與帶的資訊

- **連線時機**：進入「聯絡人才」（求才）／「聯絡公司」（求職）頁後，**選定／指定特定聊天室當下**才建立連線（非進系統即連線）。
- 建立連線時帶上以下資訊辨識身分與頻道：

| 名稱 | 意義 |
| :--- | :--- |
| `Token` | 登入憑證（確認已登入） |
| `oNo` | 公司編號 |
| `uNo` | 使用者編號 |
| `echathub` | 聊天頻道名稱（全系統統一用這個） |

> 為避免閒置斷線，系統會固定間隔自動偵測連線是否存活（心跳），斷線自動重連。

### 新版業務流程（送出走 WebAPI、SignalR 只收信號）

1. **送出**：前端**不做 SignalR invoke**，改打 WebAPI 存進 DB。
   - **求才端**：打 `eChatHandler.ashx`（`kind=5`）WebAPI（`eChatFunc.SaveMsgLog()`＝唯一寫入點）。
   - **求職端**：打**求職自己提供的送出 API**（**非** `eChatHandler.ashx`）；登入認證用求職端各自的 cookie，API 名稱與參數與求才端**不同、不共用**。
2. DB 寫入成功後，後端呼叫 `POST update-chatlog`（同步整合訊息 API）→ 發事件到 **EventBus** → 觸發 `eChatHub/apiSendMessage.ashx`。
3. `apiSendMessage.ashx` 驗證簽章、查對方線上狀態，對在線接收端呼叫 `onSignal` 做 SignalR 即時推送，並統一分派 FCM／APNS 手機推播。
4. **接收**：前端 `onSignal` 收到的只是「有新訊息」的**通知信號**；`MsgLog` 直接忽略，但**其餘 KEY 參數（`tNo`／`oNo`／`uNo`／`eNo`、正常情況下含 `updateId` 等）即後續打「取對話 API」所需的參數** —— 若為目前開啟中的聊天室，就用這些參數打**「取全部」對話 API**（目前**只有 1 支**取全部 API，**求才／求職共用同一支 `get-detail`**）取得該對話訊息；前端**帶上本地已存最大 `bNo`（訊息明細流水號）作 cursor 指標，讓 SignalR／後端知道要從哪裡開始更新**（後端只回傳該 `bNo` 之後的新資料），並以 `updateId` 判斷哪些資料已存在 DB、哪些還沒，**不必每次都整室重新渲染全部**；非當前聊天室僅更新未讀提示。
5. 接收者讀取後 → 前端回報「已讀」（求才端 `updateMsgReaded`），更新雙方的已讀狀態。

### 常用動作（Action）對照表

> **保留 vs 廢止**（依工程端 Ryder 確認）：原始事件中 `setoUser`、`updateMsgReaded`（求才端）、`settUser`（求職端）**保留、新版仍會使用**；求職端 `setRoomInfo`、`getUserStatus` 未列入保留清單、視為**不再需要**。送出用的 SignalR invoke（`sendMsgPush`）與接收 `onTextMessage` 兩端皆廢止。

| 方向 | 動作名稱 | 端 | 新版狀態 | 說明 |
| :--- | :--- | :--- | :--- | :--- |
| 前端發送 | `setoUser` | 求才 | ✅ **保留**（新版仍使用） | 上線報到（公司名稱, 使用者名稱） |
| 前端發送 | `updateMsgReaded` | 求才 | ✅ **保留**（新版仍使用） | 標記訊息已讀（已讀對象的 ID 陣列） |
| 前端發送 | `settUser` | 求職 | ✅ **保留**（新版仍使用） | 求職端上線報到 |
| 前端發送 | `setRoomInfo` | 求職 | ❌ **廢止**（未列入保留清單，不再需要） | 舊版設定聊天室資訊 |
| 前端發送 | `getUserStatus` | 求職 | ❌ **廢止**（未列入保留清單，不再需要） | 舊版查詢對方線上狀態；新版線上狀態由後端 `apiSendMessage.ashx` 於推播前查（`GetTalentUserOnline`／`GetOrganUserOnline`） |
| 前端發送 | `sendMsgPush` | 求才／求職 | ❌ **廢止** | 舊版送出文字訊息的 SignalR invoke；新版送出改走 WebAPI（求才 `eChatHandler.ashx kind=5`／求職自有送出 API），前端不再 invoke |
| 後端推播 | `onTextMessage` | 求才／求職 | ❌ **廢止（由 `onSignal` 取代）** | 舊版接收文字訊息事件（`signalr?.on('onTextMessage', handleReceive)`） |
| 後端推播 | `onSignal` | 求才／求職 | ✅ **新版接收事件** | 參數 `(ContextID, tNo, oNo, uNo, eNo, MsgLog)`，`ContextID` 固定 `"apiSendMessage"` 供識別推送來源；**原有參數都保留、只增不改，之後若擴充一律附加在後面**（擴充項目確認中）。前端忽略 `MsgLog`，其餘 KEY 參數即後續打「取對話 API」的參數 |
