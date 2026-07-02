# 信件即時通整併-搜尋記訊內容

UPDATE：2026/07/02

## 求才環境

1. 正式機：https://recruit.1111.com.tw/
2. STG測試機：https://recruit-stg.1111.com.tw/

## 取得API資料

### API 路徑

`/api/v1/external/echat/get-by-condition`

### HTTP method

GET

### HTTP Header

未登入：
- `X-CUSTOM-API-KEY`: (請先向求才端申請API金鑰)
- `Referer`：[網域(提交申請)]

### 如何呼叫

透過 HTTP GET 呼叫此 API。未登入狀態需於 Header 夾帶 `X-CUSTOM-API-KEY`、`Referer`；使用 API KEY (請先向求才申請API金鑰)。

範例（未登入呼叫）：

```
GET /api/v1/external/echat/get-by-condition
Header:
X-CUSTOM-API-KEY: xxxxxxxx
Referer : xxxxxxxx
```

### 備註

透過關鍵字搜尋特定廠商的歷史記訊內容。求職端需固定帶參數 `talentNo`。求職端 `keyword` 查訊息僅針對最後一筆訊息查詢關鍵字。

## Request 請求內容

### 後端預期 Body

```
{
/api/v1/external/echat/get-by-condition?keyword=測試&organNo=9565124
}
```

### 前端預期 Query (網址參數)

| 參數名稱 | 型別 | 必填 | 說明 |
| --- | --- | --- | --- |
| keyword | string | 否 | 搜尋關鍵字 |
| organNo | int | 否 | 廠編 |
| empNo | int | 否 | 職缺編號 |
| startDate | DateTime | 否 | 起始日 |
| endDate | DateTime | 否 | 結束日 |
| tName | String | 否 | 求職者姓名 |
| talentNo | int | 否 | 求職者編號 |
| oReadStatus | int | 否 | 讀取狀態 (1:已讀 0:未讀) |
| wishStatus | int | 否 | 求職者意願回覆 (0:未回覆 1:有意願 2:婉拒 3:更改時間) |
| userNos | string | 否 | 廠商使用者編號，用,分開 |
| mailType | int | 否 | 信件類別 (0其他/一般訊息 1面試邀約 2詢問意願 5遺珠函/感謝函 6到職確認 8面試異動 9即時通訊) |
| interviewKind | int | 否 | 面試類別 (0:不拘 1:實體 2:遠距 3:刪除) |
| sendType | int | 否 | 求才端用 (0 求才發信 1 求職者先發信(陌生訊息) -1 排除陌生訊息) |
| isStar | 否 | | 星號（求職端 是否為過濾訊息） |

> **前端備註（本 repo 分析）**：`sendType` 是**陌生訊息判斷**的後端依據（E.1 §1.1.2 陌生訊息 Tab）。此處 `mailType` 為**查詢條件層級**代碼（含 `2:詢問意願`／`9:即時通訊`），與 `get-detail`／`get-by-condition` 回傳 JsonB 內 `type`（原始信件類別，無 `2`）是**兩層不同代碼**，勿混用比對。

## Response 回傳訊息

### 後端預期 HTTP 200 Body

```json
{
    "rNo": 12,
    "organNo": 9565124,
    "organName": "1111測試專用公司1(請勿應徵)",
    "talentNo": 69228262,
    "tName": "系統測試楊盈秀",
    "tRole": 1,
    "resumeNo": 3738734,
    "resumeGuid": "0df7a6ce-d567-481e-9561-8c33879dab18",
    "snapshotGuid": "d388e4c1-0019-4e20-b228-28c756e6ac80",
    "empNo": 132463011,
    "empName": "wong²20260211主網類別更新_測試職缺請勿應徵_5",
    "eRole": 1,
    "oJsonB": [
        {
            "bNo": 1,
            "msgKind": 1,
            "detailNo": 1161124,
            "mailNo": 9838117,
            "oUserNo": 28129785,
            "oUserName": "育琳",
            "type": 0,
            "sendKind": 0,
            "message": "系統測試",
            "dateSend": "2026-03-02T16:10:46.393",
            "duringTime": 0,
            "oViewDate": "2026-03-02T16:10:46.393",
            "tViewDate": "1911-01-01T00:00:00",
            "readflag": false,
            "tDelFlag": false,
            "oDelFlag": false,
            "displayType": "0",
            "wishReply": 0
        },
        {
            "bNo": 2,
            "msgKind": 1,
            "detailNo": 1240906,
            "mailNo": 10484438,
            "oUserNo": 19766911,
            "oUserName": "主帳號",
            "type": 1,
            "sendKind": 0,
            "message": "您好：本公司透過1111人力銀行招募【2702test】人才，本公司對您的資歷十分感興趣，誠摯邀請您來面試！",
            "interViewKind": 0,
            "dateSend": "2026-05-12T19:35:21.82",
            "duringTime": 0,
            "oViewDate": "2026-05-12T19:35:21.82",
            "tViewDate": "2026-05-12T19:36:58.86",
            "readflag": false,
            "tDelFlag": false,
            "oDelFlag": false,
            "displayType": "0",
            "wishReply": 0,
            "replyWishMsgDateIn": "2026-05-12T19:37:05.057",
            "replyWishMsgDetailNo": 1240908
        }
    ],
    "tJsonB": [
        {
            "bNo": 1,
            "msgKind": 1,
            "detailNo": 1161124,
            "mailNo": 9838117,
            "oUserNo": 28129785,
            "oUserName": "育琳",
            "type": 0,
            "sendKind": 0,
            "message": "系統測試",
            "dateSend": "2026-03-02T16:10:46.393",
            "duringTime": 0,
            "oViewDate": "2026-03-02T16:10:46.393",
            "tViewDate": "1911-01-01T00:00:00",
            "readflag": false,
            "tDelFlag": false,
            "oDelFlag": false,
            "displayType": "0",
            "wishReply": 0
        }
    ],
    "oDelFlag": false,
    "tDelFlag": false,
    "dateIn": "2026-03-04T16:37:26.577"
}
```

> `oJsonB`／`tJsonB` NULL 欄位不會吐出。原始 PDF 另附一筆含完整未省略欄位（`BNo`/`MsgKind`/... 大寫開頭）的範例，供對照 `get-detail` 欄位命名（大小寫慣例不完全一致，見備註）。

### API 欄位詳細描述

| 名稱 | 型態 | 欄位用意 |
| --- | --- | --- |
| rNo | int | 流水號 (PK)，記訊資料的唯一編號 (RNo) |
| organNo | int | 廠商編號 |
| organName | string? | 廠商名稱 |
| talentNo | int | 求職者編號 |
| tName | string? | 求職者名稱 |
| tRole | int | 求職者履歷屬性 |
| resumeNo | int? | oResumeXX.sNo |
| resumeGuid | string? | 履歷代碼 oResumeXX.resumeGuid |
| snapshotGuid | string? | 快照代碼 oResumeXX.SnapshotGuid |
| empNo | int? | 職缺編號 (employees.employeeNo) |
| empName | string? | 職缺名稱 (employees.position0) |
| eRole | byte? | 職缺屬性 (employees.role) |
| oDelFlag | bool | 廠商是否刪除 (1:刪除 0:未刪除) |
| tDelFlag | bool | 求職者是否刪除 (1:刪除 0:未刪除) |
| dateIn | string | 建立/更新時間 |
| oJsonB | json | 廠商對話明細 |
| tJsonB | json | 求職者對話明細 |

### JsonB 欄位描述

| 名稱 | 型態 | 欄位用意 |
| --- | --- | --- |
| bNo | int | 流水號 (PK) |
| msgKind | int | 合併來源類別：0:即時通 1:信件 |
| detailNo | int | 原資料表編號 mailNoticeDetailXX.mailDetailNo / eChatLog.aNo |
| mailNo | int | 信件主表編號 mailNotice.MailNo |
| oUserNo | int? | 廠商使用者編號 |
| oUserName | string? | 廠商使用者名稱 |
| type | int | 信件類別 mailType（0其他/一般訊息 1面試邀約 2詢問意願 5遺珠函/感謝函 6到職確認 8面試異動 9即時通訊） |
| sendKind | int? | 寄件者：mail→ 0廠商/1求職者/3廠商系統訊息/4求職者系統訊息/5求才發給求職系統信/6求職給求才系統信/7求才回收/8求職回收/9求才即時通/10求職即時通；echat→ WhoTalk 0廠商/1求職者。廠商端顯示：0,1,3,6,9,10；求職端顯示：0,1,4,5,9,10；廠商寄出信件：0,5；求職者寄出信件：1,6；求才回收訊息：7；求職者回收訊息：8；即時通廠商轉入：9；即時通求職者轉入：10 |
| message | string | 內文 |
| interViewKind | int | 面試類別 |
| dateSend | DateTime | 寄送日期 |
| StartTalk | DateTime? | 開始(視訊)通話時間 |
| EndTalk | DateTime? | 結束(視訊)通話時間 |
| duringTime | int | (視訊)通話經過時間(秒) |
| FileName | string | 檔案名稱 |
| FilePath | string | 檔案路徑：125/eChatFile/ |
| oViewDate | DateTime? | 廠商已讀日期 |
| tViewDate | DateTime? | 求職者已讀日期 |
| readflag | bool | 是否已讀：0-未讀; 1-已讀 |
| tDelFlag | bool | 求職者刪除標記 |
| oDelFlag | bool | 廠商刪除標記 |
| oIgnore | int? | 求職寫罐頭語會是1（暫無用處） |
| RevokeuNo | int? | 回收訊息的帳號編號 |
| displayType | int | 顯示類型（0:一般字串(NULL) 1:JSON格式字串(action) 2:語音JSON(msgType:6)）。MsgType 訊息類型：0-文字; 1-通話; 2-視訊; 3-圖片; 4-檔案; 5-通知 6:撥出電話(取消) |
| wishReply | int | 是否能回覆(1HR) 0:未回覆 |
| replyMailResult | bool? | 回覆信件結果 (1HR,求職端查用) |
| mailTypeEhr | int? | 信件類別 (1hr用) |
| talentNoEhr | long? | 履歷編號 (1hr第三方履歷) |
| replyWishMsgDateIn | datetime? | 求職者意願回覆時間 (求職端用) |
| replyWishMsgDetailNo | int? | 求職者意願回覆的 mailDetailNo (求職端用) |
| departNoEhr | int? | 部門(1hr用) |

### HTTP Status Code

Status Code 400
```json
{
  "code": "InputError",
  "message": "OrganNo is required for simulated authentication on this path.",
  "errorUserNo": 0,
  "details": []
}
```

Status Code 401
```json
{
  "code": "VipUserNotFound",
  "message": "Invalid or missing API key.",
  "errorUserNo": 0,
  "details": []
}
```
