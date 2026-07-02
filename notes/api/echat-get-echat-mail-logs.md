# 信件即時通整併-取得訊息紀錄列表

UPDATE：2026/7/02

## 求才環境

1. 正式機：https://recruit.1111.com.tw/
2. STG測試機：https://recruit-stg.1111.com.tw/

## 取得API資料

### API 路徑

`/api/v1/external/echat/get-echat-mail-logs`

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
GET /api/v1/external/echat/get-echat-mail-logs
Header:
X-CUSTOM-API-KEY: xxxxxxxx
Referer : xxxxxxxx
```

### 備註

取得指定廠商、人才或職缺的相關記訊紀錄。

## Request 請求內容

### 後端預期 Body

```
{
  /api/v1/external/echat/get-echat-mail-logs?organNo=9565124&talentNo=8415561&empNo=132453804
}
```

### 前端預期 Query (網址參數)

| 參數名稱 | 型別 | 必填 | 說明 |
| --- | --- | --- | --- |
| organNo | int? | 否 | 廠商編號 |
| talentNo | int? | 否 | 人才編號 |
| empNo | int? | 否 | 職缺編號 |
| limit | int? | 否 | 查詢size |
| cursor | int? | 否 | 指標 |

## Response 回傳訊息

### 後端預期 HTTP 200 Body

```json
[
  {
    "rNo": 1,
    "organNo": 9565124,
    "organName": "1111測試專用公司1(請勿應徵)",
    "talentNo": 34611960,
    "tName": "吳思賢",
    "tRole": 1,
    "resumeNo": 3737526,
    "resumeGuid": "26699116-5cee-4faa-a754-9c3d49d66541",
    "snapshotGuid": "3f5e4b7c-79fc-4dcf-b355-27ead0d3672a",
    "empNo": 132438815,
    "empName": "手動測試工程師(測試職缺，請勿應徵)#wahoya001 #6283",
    "eRole": 1,
    "uNos": "",
    "oDelFlag": false,
    "tDelFlag": false,
    "dateIn": "2026-03-04T16:37:20.797",
    "mailStatus": false,
    "tLastReplyWishMsg": 0,
    "oLastViewDate": "2026-06-18T09:51:26.503",
    "tLastViewDate": "2026-06-18T09:49:27.113",
    "lastReplyDate": "2026-06-18T09:49:27.12",
    "lastMailType": 1,
    "lastMsg": "7777",
    "nonMsgLastReplyDate": "2026-06-18T09:49:27.12",
    "echatLastReplyDate": "2026-06-18T09:56:51.573",
    "lastUpdate": "2026-06-18T09:56:51.573"
  }
]
```

> 完整範例含多筆對話（不同 `mailStatus`／`lastReplyWishMsg`／EHR 欄位組合），詳見原始 PDF；此處僅保留代表性單筆。

### API 欄位詳細描述

| 名稱 | 型態 | 欄位用意 |
| --- | --- | --- |
| rNo | int | 資料流水號 |
| organNo | int | 公司編號 |
| organName | string | 公司名稱 |
| talentNo | int | 求職者編號 |
| accountNo | string | 求職者帳號 |
| tName | string | 求職者姓名 |
| tRole | byte | 求職者角色別 |
| resumeNo | int? | 履歷編號 oResumeXX.sNo |
| resumeGuid | Guid? | 履歷代碼 oResumeXX.resumeGuid |
| snapshotGuid | Guid? | 快照代碼 oResumeXX.SnapshotGuid |
| empNo | int? | 職缺編號 (employees.employeeNo) |
| empName | string | 職缺名稱 (employees.position0) |
| eRole | byte? | 職缺屬性 (employees.role) |
| uNos | string | 使用者編號清單 |
| oDelFlag | bool | 公司端是否刪除聊天室 |
| tDelFlag | bool | 求職者端是否刪除聊天室 |
| dateIn | DateTime | 建立聊天室時間 |
| talentImage | string | 求職者頭像 |
| mailStatus | bool? | 是否有站內信狀態 |
| tLastReplyWishMsg | int? | 求職者最後回覆許願訊息狀態 |
| oLastViewDate | DateTime? | 公司最後查看聊天室時間 |
| tLastViewDate | DateTime? | 求職者最後查看聊天室時間 |
| lastReplyDate | DateTime? | 最後回覆時間 |
| lastMailType | int? | 最後訊息類型 |
| lastInterViewKind | byte? | 最後面試類型 |
| lastMsg | string | 最後一則訊息內容 |
| nonMsgLastReplyDate | DateTime? | 最後非訊息回覆時間 |
| lastMailTypeEhr | int? | EHR 最後訊息類型 |
| talentNoEhr | long? | EHR 求職者編號 |
| departNoEhr | int? | EHR 部門編號 |
| lastUserEhr | int? | EHR 最後操作使用者 |
| lastSendDateEhr | DateTime? | EHR 最後發送時間 |
| echatLastReplyDate | DateTime? | EChat 最後回覆時間 |
| lastUpdate | DateTime? | 最後更新時間 |
| sendType | int? | 發送類型 |
| totalCount | int | 全部訊息數量 |
| recommendCount | int | 推薦訊息數量 |
| notMatchCount | int | 一般訊息數量 |
| isStar | bool | 是否為釘選訊息 |
| mailCategory | int? | 求職者過濾通知信分類（null_未處理, 0_一般, 1_推薦） |

> **前端備註（本 repo 分析）**：`oLastViewDate`／`tLastViewDate`／`lastUpdate` 三欄可用於推導**列表未讀判斷**（比對「公司最後查看時間」是否早於「最後更新時間」）；目前規格書尚未明確定義聚合規則，待確認。

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
