# 信件即時通整併-搜尋記訊內容（get-by-condition）

UPDATE：2026/07/20（工程端最新版：**取代已棄用的 `get-echat-mail-logs`**，本支同時承擔「列表載入」與「關鍵字／條件搜尋」；回傳改為對話摘要**陣列**、cursor 改 `{organNo}_{RNo}`、新增多個回傳欄位）

> **本 repo 重點備註**
> - **`get-echat-mail-logs` 已棄用**：列表載入改直接打本支 `get-by-condition`（不帶 keyword／篩選即等同原列表）。
> - **回傳結構變更**：新版回傳為**對話摘要陣列**（每筆一個對話），**不再回 `oJsonB`／`tJsonB` 訊息明細**；訊息明細一律走 `get-detail/{infoNo}`。
> - **cursor 格式**：`{organNo}_{RNo}`（舊版記為 `infoNo`，已更正）。此為**列表／搜尋分頁**指標，與聊天室「接收新訊息」用的 `bNo` cursor 是**不同層級**，勿混（見 `notes/uS9` §兩種 cursor 勿混）。
> - `mailType` 為**查詢條件層級**代碼（含 `2:詢問意願`／`9:即時通訊`），與 `get-detail` 回傳 JsonB 內 `type`（原始信件類別，無 `2`）是**兩層不同代碼**，勿混用比對。
> - `sendType` 為**陌生訊息判斷**的後端依據（E.1 §1.1.2 陌生訊息 Tab）。

## API 路徑

`/api/v1/echat/get-by-condition`

### HTTP method

GET

### HTTP Header（未登入呼叫）

- `X-CUSTOM-API-KEY`：（請先向求才端申請 API 金鑰）
- `Referer`：[網域（提交申請）]

### 備註

透過關鍵字／條件搜尋特定廠商的歷史記訊內容；不帶 keyword／篩選時即為列表載入。求職端需固定帶參數 `talentNo`；求職端 `keyword` 查訊息僅針對最後一筆訊息查詢關鍵字。

## Request 請求內容

### 後端預期 Body

```
/api/v1/echat/get-by-condition?keyword=測試&organNo=9565124
```

### 前端預期 Query (網址參數)

| 參數名稱 | 型別 | 必填 | 說明 |
| --- | --- | --- | --- |
| keyword | string? | 否 | 關鍵字（求職：搜廠編、廠名、職編、職名；求才：搜求職編號、求職姓名、職編、職名） |
| organNo | int? | 否 | 廠商編號 |
| empNo | int? | 否 | 職缺編號 |
| startDate | DateTime? | 否 | 開始日期 |
| endDate | DateTime? | 否 | 結束日期 |
| tName | string? | 否 | 求職者名稱 |
| talentNo | int? | 否 | 求職者編號 |
| readStatus | int? | 否 | 是否已讀：0-未讀; 1-已讀 |
| wishStatus | string? | 否 | 求職者意願回覆 (0:未回覆 1:有意願 2:婉拒 3:更改時間) |
| userNos | string? | 否 | 廠商使用者編號（用 , 可多筆） |
| mailType | string? | 否 | 信件類別 (0其他/一般訊息 1面試邀約 2詢問意願(目前無使用) 3邀請加入(目前無使用) 4審核階段(目前無使用) 5遺珠函/感謝函 6到職確認 7面試確認(目前無使用) 8面試異動 9即時通訊) |
| interviewKind | int? | 否 | 面試類別 (0不拘、1實體、2遠距(無用)、3刪除) |
| sendType | int? | 否 | 發送類型（求才端）。0 = 求才發信（含 -1 = 排除陌生訊息）；1 = 求職者先發信（陌生訊息） |
| cursor | string? | 否 | 指標 `{organNo}_{RNo}` |
| limit | int? | 否 | 查詢頁面 size |
| MailCategory | int? | 否 | 求職者過濾通知信分類。0 = 全部信件（含 null = 未處理）；1 = 您可能感興趣的工作 |
| IsStar | bool? | 否 | 星號（true 星號；false 無星號） |
| mailStatus | bool? | 否 | 回覆狀態（true 已回覆／false 未回覆）；信件狀態（1:廠商寄出 0:求職者回覆） |

## Response 回傳訊息

### 後端預期 HTTP 200 Body

回傳為**對話摘要陣列**（每筆一個對話），範例（節錄一筆）：

```json
[
  {
    "rNo": 37549,
    "organNo": 9565124,
    "organName": "1111測試專用公司1(請勿應徵)",
    "talentNo": 50973970,
    "tName": "系統測試王大大",
    "tRole": 1,
    "resumeNo": 3770670,
    "resumeGuid": "273771d0-97a9-4297-8ffd-0a857c9e6955",
    "snapshotGuid": "b673d022-244d-4da7-bf64-299d8afce00e",
    "empNo": 132783421,
    "empName": "行政人員(測試職缺，請勿應徵)#lihoya2026 #6283",
    "eRole": 1,
    "oDelFlag": false,
    "tDelFlag": false,
    "dateIn": "2026-07-13T09:59:23.097",
    "talentImage": "/includes/talentImage.ashx?enc=...",
    "mailStatus": true,
    "tLastReplyWishMsg": 0,
    "oLastViewDate": "2026-07-13T15:57:52.05",
    "tLastViewDate": "2026-07-14T09:33:57.01",
    "lastReplyDate": "2026-07-13T15:57:52.05",
    "lastMailType": 1,
    "lastMsg": "再麻煩查看",
    "nonMsgLastReplyDate": "2026-07-13T00:00:00",
    "lastUpdate": "2026-07-14T11:24:25.363",
    "sendType": 0,
    "totalCount": 224,
    "recommendedCount": 147,
    "filteredCount": 0,
    "lastDisplayType": 0
  }
]
```

### API 欄位詳細描述

| 名稱 | 型態 | 欄位用意 |
| --- | --- | --- |
| rNo | int | 流水號 (PK)，記訊資料的唯一編號 (RNo) |
| organNo | int | 廠商編號 |
| organName | string? | 廠商名稱 |
| talentNo | int | 求職者編號 |
| tName | string? | 求職者姓名 |
| tRole | int | 求職者履歷屬性 |
| resumeNo | int? | 履歷編號 oResumeXX.sNo |
| resumeGuid | string? | 履歷代碼 oResumeXX.resumeGuid |
| snapshotGuid | string? | 快照代碼 oResumeXX.SnapshotGuid |
| empNo | int? | 職缺編號 (employees.employeeNo) |
| empName | string? | 職缺名稱 (employees.position0) |
| eRole | byte? | 職缺屬性 (employees.role) |
| uNos | string? | 需回覆的廠商使用者（逗號分隔字串）。→ 原本即時通用；整併後不使用 |
| oDelFlag | bool | 廠商是否刪除 (1:刪除 0:未刪除) |
| tDelFlag | bool | 求職者是否刪除 (1:刪除 0:未刪除) |
| dateIn | string | 建立/更新時間 |
| talentImage | string | 求職者頭像 |
| mailStatus | bool? | 信件狀態 (1:廠商寄出 0:求職者回覆) |
| tLastReplyWishMsg | int? | 求職者最後一次的意願回覆值（最後一筆訊息的 ReplyWishMsg，無則為 0） |
| oLastViewDate | DateTime? | 廠商端最後檢視時間（掃描 JSON 內 OViewDate 的最大有效值） |
| tLastViewDate | DateTime? | 求職者端最後檢視時間（掃描 JSON 內 TViewDate 的最大有效值） |
| lastReplyDate | DateTime? | 最後一封符合條件信件的發送時間（MsgKind=1 且 Type ∈ {1,5,6,8}） |
| lastMailType | int? | 最後一封符合條件信件的類型；只會是 1、5、6、8 或 null，其他值不會被寫入 |
| lastInterViewKind | byte? | 最後面試類型 |
| lastMsg | string? | 最後一筆訊息內容（已 HtmlDecode、將 `<br>` 轉為換行、其他標籤剝除並 Trim） |
| nonMsgLastReplyDate | DateTime? | 非聊天訊息（即信件）的最後回覆時間；與 LastReplyDate 條件相同 |
| lastMailTypeEhr | int? | EHR 最後訊息類型 |
| talentNoEhr | long? | EHR 求職者編號 |
| departNoEhr | int? | EHR 部門編號 |
| lastUserEhr | int? | EHR 最後信件類型（取自最後一筆訊息的 MailTypeEhr） |
| lastSendDateEhr | long? | EHR 最後發言廠商使用者編號；僅當最後一筆為 SendKind=0（廠商）時填入，否則為 null |
| echatLastReplyDate | DateTime? | EChat 最後回覆時間 |
| lastUpdate | int? | 最後更新時間；優先使用 EChatMailMergeLastMsg.LastUpdate，若無則退回 EChatMailMergeInfo.LastUpdate |
| sendType | int? | 發送類型（求才端）。0 = 求才發信；1 = 求職者先發信（陌生訊息）；-1 = 排除陌生訊息 |
| totalCount | int | 全部訊息數量 |
| recommendCount | int | 推薦訊息數量 |
| notMatchCount | int | 一般訊息數量 |
| StarMarkNo | int? | 星號編號 |
| mailCategory | int? | （求職端）求職者過濾通知信分類（null 未處理, 0 一般, 1 推薦） |
| lastDisplayType | int? | 最後顯示類型 (0:一般字串 1:JSON格式字串 2:語音JSON (echat.msgType:6))；最後訊息為 echat 匯入才會有值，無則清空 |
| lastReplyDetailNo | int? | 需回覆意願的 mailDetailNo（mailType = 1、6、8） |

> ⚠️ 回傳範例欄位名 `recommendedCount`／`filteredCount` 與欄位描述表的 `recommendCount`／`notMatchCount` 命名略有出入（工程端原文即如此），前端串接以實際 API 回傳為準。

## HTTP Status Code

### Status Code 400

```json
{ "code": "InputError", "message": "OrganNo is required for simulated authentication on this path.", "errorUserNo": 0, "details": [] }
```

### Status Code 401

```json
{ "code": "VipUserNotFound", "message": "Invalid or missing API key.", "errorUserNo": 0, "details": [] }
```
