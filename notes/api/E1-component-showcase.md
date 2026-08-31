# 求才端對話 UI 狀態設計文件（SDD）— 前端 component showcase

> 來源：前端 component 展示站 `components-dev.1111.com.tw/notify-message-recruit/dist-spa/index-showcase.html`（內網 -dev，遠端環境無法直連，由使用者提供 .mhtml 存檔轉存）。
> 原始渲染快照（含 CSS、可瀏覽）：`.claude/assets/E1/E1_component_showcase.html`。
> 本檔為該站「資料流／狀態判定規則」的結構化文字版，供 E.1（信件即時通整併）需求推導時參照。
> **此文件是前端實作契約**：欄位轉換、卡片判定、狀態機邏輯以此為準；與規格書衝突時，前端實作優先，並回頭修規格書。

---

## 0. 資料流總覽

### 兩條資料路徑

| 路徑 | 後端 API | 回傳型別 | 前端使用型別 | 用途 |
| --- | --- | --- | --- | --- |
| 聊天列表 | 聊天列表 API（`get-echat-mail-logs`） | `ChatResponseItem[]` | 直接使用（**不經 mapper**） | 左側 `ChatItem` 列表 |
| 聊天訊息 | 聊天詳情 API（`get-detail`）→ `oJsonB` + `tJsonB` | `ChatMessageItem[]` | 經 `chatMessageMapper` → `ChatMessage[]` | 右側 `CompanyMessage` / `TalentMessage` / `InterviewCard` |

### 後端原始型別：ChatMessageItem（oJsonB / tJsonB 陣列元素）→ 前端轉換

| 後端欄位 | 型別 | 說明 | 前端轉換後欄位 |
| --- | --- | --- | --- |
| `detailNo` | number | 訊息唯一 ID（去重用） | `id` |
| `sendKind` | 0~10 | 發送者種類（見 §5） | `sender` + `isRevoked` |
| `msgKind` | 0/1 | 0=即時通、1=信件 | `type`（卡片判定依據之一） |
| `type` | 0~8 | msgKind=0 時為訊息格式；=1 時對應 MailType | `card.mailType`（經 `toMailType` 轉換） |
| `interViewKind` | 0/1/3 | 0=詢問意願、1=實體面試、3=取消面試 | `card.mailType` + `card.isCancel` |
| `replyWishMsg` | 0~4 | 求職者意願回覆 | `card.status` + `replyWishMsg`（膠囊） |
| `message` | string | 訊息內容（EHR 來源為 URL 編碼） | `text` / `card.bodyHtml` + `informItems` |
| `dateSend` | string | 發送時間 | `time` + `date` |
| `oUserName` | string? | 廠商操作者姓名 | `oUserName` |
| `accountName` | string? | 廠商操作者帳號 | `accountName`（**後端尚未提供**） |
| `readflag` | boolean | 已讀旗標 | `isRead`（mapper 未對應，**待補**） |
| `revokeFlag` | number? | 1=已回收 | **不使用**（改以 `sendKind` 7/8 判定） |
| `talentNoEhr` | number? | 有值=來源為 EHR 系統 | 決定 parser 分支 |
| `fileName`/`filePath` | string? | 附件檔名/路徑 | `file.name`/`file.url` |

### 後端原始型別：ChatResponseItem（聊天列表）— 後端提供狀態

| 後端欄位 | 說明 | 後端提供狀態 |
| --- | --- | --- |
| `rNo`/`organNo`/`talentNo`/`empNo` | 關聯 ID | 已提供 |
| `organName`/`tName`/`empName` | 顯示名稱 | 已提供 |
| `lastMsg`/`dateIn`/`talentImage` | 最後訊息/時間/頭像 | 已提供 |
| `isBlocked` | 是否封鎖 | 型別未定義（前端預留使用中） |
| `unread` | 是否有未讀訊息 | **後端尚未提供** |
| `mailType` | 信件類別標籤 | **後端尚未提供** |
| `isPinned` | 是否釘選 | **後端尚未提供**（功能未實作） |

> ⚠️ 列表層級 `unread`／`mailType`／`isPinned` 前端預留、後端尚未提供欄位。列表 API（`get-echat-mail-logs`）實際有回 `oLastViewDate`／`tLastViewDate`／`lastUpdate`／`lastMailType`，未讀與標籤可由這些推導，待後端/前端定案聚合規則。

---

## 1. 對話列表卡片（ChatItem）

### 狀態維度

| 維度 | 前端欄位 | 可能值 | 後端 API 狀態 |
| --- | --- | --- | --- |
| 封鎖 | `isBlocked` | true/false/undefined | 型別未定義，前端預留使用中 |
| 未讀 | `unread` | true/false/undefined | 後端尚未提供此欄位 |
| 信件類別 | `mailType` | 1/2/5/6/8/undefined | 後端尚未提供此欄位 |
| 選中 | `rNo === selectedChat.rNo` | true/false | 純前端狀態 |
| 批次模式 | `listSelectedOption` | 有值/null | 純前端狀態 |

### 封鎖 × 各維度交叉影響

| 子元素 | isBlocked=false | isBlocked=true |
| --- | --- | --- |
| 姓名 `tName` | 預設文字色 | text-disabled-neutral |
| 職稱 `empName` | 預設文字色 | text-disabled-neutral |
| 最後訊息 | `item.lastMsg`（truncate） | 固定文字「已封鎖」 |
| 未讀紅點 | 依 `unread` 顯示 | 隱藏（封鎖覆蓋） |
| `mailType` 標籤 | 依 `mailType` 顯示 | 隱藏 |
| 右側圖示 | 不顯示 | icon-unavailable（灰色鎖） |

### mailType 標籤色票（僅在 isBlocked=false 且 mailType 有值時渲染）

| mailType | 文字 | CSS class | 文字色 | 背景色 |
| --- | --- | --- | --- | --- |
| 1 | 面試邀約 | tag--blue | #1a66ff | #e3ecfc |
| 2 | 詢問意願 | tag--blue | #1a66ff | #e3ecfc |
| 5 | 感謝函 | tag--gray | #495057 | #e9ecef |
| 6 | 錄取通知 | tag--green | #4b8b1a | #f0f9e9 |
| 8 | 面試異動 | tag--orange | #b2410f | #ffede5 |

### 批次操作模式

| listSelectedOption | 左側 Checkbox | 點擊行為 |
| --- | --- | --- |
| null | 隱藏 | setSelectedChat(item) |
| 有值 | 顯示 | 僅操作 Checkbox |

---

## 2. 求才方訊息（CompanyMessage）

### 渲染優先序

| 優先 | 前端條件 | 後端原始條件（ChatMessageItem） | 渲染結果 |
| --- | --- | --- | --- |
| 1 | isRevoked=true | sendKind ∈ {7, 8} | 收回文字框 |
| 2 | type='card' + card 有值 | msgKind=1 且 type ∈ [1, 5, 6, 8] | InterviewCard |
| 3 | type='file' + file 有值 | fileName + filePath 有值 | 檔案卡 |
| 4 | fallback | 其餘所有情況 | 文字氣泡 |

### 收回按鈕顯示條件

| 前端 isRead | 前端 isRevoked | type | 後端原始欄位 | 收回按鈕 |
| --- | --- | --- | --- | --- |
| false | false | 非 card/file | readflag=false 且 sendKind ∉ {7,8} | 顯示（hover 觸發） |
| true | — | — | readflag=true | 隱藏 |
| — | true | — | sendKind ∈ {7, 8} | 不適用（整則為收回框） |
| — | — | card/file | — | 無收回按鈕 |

### Meta 資訊

| 訊息類型 | isRevoked | 顯示內容 | 後端來源 |
| --- | --- | --- | --- |
| card | — | meta slot：oUserName + accountName + [已讀・] + time | oUserName + accountName（待補）+ dateSend |
| 非 card | false | 氣泡下方：oUserName + accountName + [已讀・] + time | 同上 |
| 非 card | true | 僅 [已讀・] + time | dateSend |

---

## 3. 求職者訊息（TalentMessage）

### 系統膠囊狀態

| 後端 replyWishMsg | 前端 replyWishMsg | 膠囊文字 | 樣式 | 背景色 | 文字色 |
| --- | --- | --- | --- | --- | --- |
| 1（有意願） | 1 | {tName}已同意面試邀約 | accepted | #f0f9e9 | #4b8b1a |
| 2（婉拒） | 2 | {tName}已通知無法赴約 | declined | #e9ecef | #495057 |
| 0/3/4/undefined | — | 不渲染膠囊 | | | |

> ⚠️ 膠囊文字「已通知無法赴約」與卡片內「婉拒」**語意刻意不同步**：後端不區分「邀約前婉拒」與「答應後無法赴約」。

### Company vs Talent 差異

| 差異 | CompanyMessage | TalentMessage | 後端判定依據 |
| --- | --- | --- | --- |
| 對齊 | 靠右 | 靠左 | sender 由 sendKind：0/7/9→company、1/8/10→talent |
| 氣泡背景 | candidate-blue-050（藍） | surface-neutral-tertiary（灰） | |
| 文字渲染 | v-html | 純文字 | |
| 收回按鈕 | 有（isRead=false hover） | 無 | |
| 卡片 | InterviewCard | 不渲染卡片 | |
| 頭像 | 不顯示 | 顯示（可點擊） | |
| 系統膠囊 | 無 | 有 | |
| meta | oUserName + accountName + 已讀 + time | 僅 time | |

---

## 4. 面試卡片狀態矩陣（InterviewCard，viewer='recruit'）

### mailType 軸：後端 → 前端對照

| 前端 mailType | 前端文字 | 後端 type | 後端 interViewKind | 轉換 |
| --- | --- | --- | --- | --- |
| 1 | 面試邀約 | 1 | 1 或 3 | toMailType() |
| 2 | 詢問意願 | 1 | 0 | toMailType()（**前端自行新增的值，後端無 2**） |
| 5 | 感謝函 | 5 | — | 直通 |
| 6 | 錄取通知 | 6 | — | 直通 |
| 8 | 面試異動 | 8 | ≠3 | 直通 |
| 8 + isCancel | 面試取消 | 8 | 3 | type=8 且 interViewKind=3 → isCancel=true |

### status 軸：後端 → 前端對照

| 前端 status | 後端 replyWishMsg | 備註 |
| --- | --- | --- |
| pending | 0 / 4 / undefined | 未回覆 |
| accepted | 1 / 3 | 有意願 / 更改時間（皆視為已接受） |
| rejected | 2 | 婉拒 |
| expired | — | 由 wishReplyDate 逾期判定（待確認邏輯） |

### mailType × status 渲染矩陣

| mailType | pending | accepted | rejected | expired |
| --- | --- | --- | --- | --- |
| 1 面試邀約 | 可選時段按鈕 | 已選定時段 | 已婉拒 | 按鈕全 disabled |
| 2 詢問意願 | 婉拒/同意按鈕 | 已同意 | 已婉拒 | 按鈕全 disabled |
| 5 感謝函 | 僅 bodyHtml | — | — | — |
| 6 錄取通知 | 婉拒/同意按鈕 | 已同意 | 已婉拒 | 按鈕全 disabled |
| 8 面試異動 | bodyHtml + informItems | 已選定時段 | 已婉拒 | 按鈕全 disabled |
| 8 + isCancel | 標題改「面試取消」，僅 bodyHtml，隱藏 informItems/分隔線/按鈕 | | | |

### 面試取消特殊狀態（type=8 且 interViewKind=3 → isCancel=true）

| 正常 mailType=8 | isCancel=true |
| --- | --- |
| 標題「面試異動」 | 標題「面試取消」 |
| 顯示 informItems | 隱藏 |
| 顯示分隔線 | 隱藏 |
| 顯示按鈕區 | 隱藏 |

---

## 5. 資料轉換狀態機（chatMessageMapper）

### sendKind → sender + isRevoked

| 後端 sendKind | 前端 sender | 前端 isRevoked | 備註 |
| --- | --- | --- | --- |
| 0 | company | false | 廠商 |
| 9 | company | false | 即時通廠商轉入 |
| 7 | company | true | 求才回收 |
| 1 | talent | false | 求職者 |
| 10 | talent | false | 即時通求職者轉入 |
| 8 | talent | true | 求職回收 |
| 3/4/5/6/其他 | system | false | 系統訊息 |

### 卡片判定

- `msgKind=0` → 即時通，`type=undefined`（走文字氣泡）
- `msgKind=1` 且 `type ∈ [1,5,6,8]` → `type='card'`，執行 `toMailType(msg)` 與 `toInterviewStatus(replyWishMsg)`
- `msgKind=1` 且 `type ∉ [1,5,6,8]` → `type=undefined`（走文字氣泡）

### toMailType 決策表

| 後端 type | 後端 interViewKind | 前端 mailType | 備註 |
| --- | --- | --- | --- |
| 1 | 0 | 2（詢問意願） | mailType=2 為前端新增值，後端無此數字 |
| 1 | 1 | 1（面試邀約） | 實體面試 |
| 1 | 3 | 1（面試邀約） | 取消面試（另由 isCancel 處理） |
| 5 | — | 5（感謝函） | 直通 |
| 6 | — | 6（錄取通知） | 直通 |
| 8 | — | 8（面試異動） | 直通 |

### toInterviewStatus 決策表

| 後端 replyWishMsg | 前端 InterviewStatus | 備註 |
| --- | --- | --- |
| 0 | pending | 未回覆 |
| 1 | accepted | 有意願 |
| 2 | rejected | 婉拒 |
| 3 | accepted | 更改時間（視為已接受） |
| 4 / undefined | pending | — |

### EHR 來源分歧

| 後端 talentNoEhr | message 處理 | 面試卡片 parser |
| --- | --- | --- |
| 有值（EHR 來源） | decodeURIComponent() | parseEhrInterviewText()：整段 HTML → bodyHtml，informItems=[] |
| 無值（求才後端） | 直接使用 | parseInterviewText()：拆出 bodyHtml + informItems[] |

### 合併去重流程

- `oJsonB` + `tJsonB` 各自 mapper 後合併；以 `detailNo` 為 key 去重（Map），再依 `dateSend` 排序輸出 `ChatMessage[]`。
