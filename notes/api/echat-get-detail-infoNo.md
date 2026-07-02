# /api/v1/echat/get-detail/{infoNo}

### API 描述

根據列表回傳的 `rNo` (infoNo) 取得該筆記訊的完整對話內容。

### Request 請求內容

### 前端預期 Path (路徑參數)

| 參數名稱 | 型別 | 必填 | 說明 |
| --- | --- | --- | --- |
| infoNo | int | 是 | 記訊資料的唯一編號 (RNo) |

### Response 回傳訊息

### 後端預期 HTTP 200 Body

```json
{
  "rNo": 10,
  "organNo": 9565124,
  "organName": "1111測試專用公司1(請勿應徵)",
  "talentNo": 52803505,
  "tName": "李晚筠",
  "tRole": 1,
  "resumeNo": 3739692,
  "resumeGuid": "ccb4d0ef-2e53-4ce1-950e-f0916c8fdbde",
  "snapshotGuid": "3a022d03-7dc3-4b61-8953-cbff1ca61fb4",
  "empNo": 132220987,
  "empName": "遛狗人員 請勿應徵1",
  "eRole": 1,
  "oJsonB": [
    {
      "bNo": 1,
      "msgKind": 1,
      "detailNo": 1160165,
      "mailNo": 9810503,
      "oUserNo": 28101870,
      "oUserName": "李晚筠",
      "type": 1,
      "sendKind": 0,
      "message": "您好：<br/><br/>本公司透過1111人力銀行招募【遛狗人員 請勿應徵1】人才，本公司對您的資歷十分感興趣，誠摯邀請您來面試！<br/><br/>如您想進一步了解工作內容，請您回覆是否有意願或婉拒此邀約，謝謝您！<br/><br/>1111測試專用公司1(請勿應徵) 祝福您求職順利！",
      "interViewKind": 0,
      "dateSend": "2026-02-26T14:52:56.32",
      "duringTime": 0,
      "oViewDate": "2026-02-26T14:52:56.32",
      "tViewDate": "2026-02-26T14:53:41.77",
      "readflag": false,
      "tDelFlag": true,
      "oDelFlag": false,
      "wishReply": 0,
      "replyWishMsgDateIn": "2026-02-26T14:54:06.653",
      "replyWishMsgDetailNo": 1160167
    },
    {
      "bNo": 2,
      "msgKind": 1,
      "detailNo": 1160167,
      "mailNo": 9810503,
      "oUserNo": 28101870,
      "type": 1,
      "sendKind": 1,
      "message": "貴主管 您好：\r\n感謝您的來信，很高興能獲得貴公司的青睞，我對本次面試非常有意願，謝謝！",
      "interViewKind": 0,
      "dateSend": "2026-02-26T14:54:06.653",
      "duringTime": 0,
      "oViewDate": "2026-02-26T14:55:16.747",
      "tViewDate": "2026-02-26T14:54:06.65",
      "readflag": false,
      "tDelFlag": true,
      "oDelFlag": false,
      "wishReply": 0
    },
    {
      "bNo": 3,
      "msgKind": 1,
      "detailNo": 1160170,
      "mailNo": 9810503,
      "oUserNo": 28101870,
      "oUserName": "李晚筠",
      "type": 1,
      "sendKind": 0,
      "message": "您好：<br/><br/>本公司透過1111人力銀行招募【遛狗人員 請勿應徵1】人才，本公司對您的資歷十分感興趣，誠摯邀請您來面試！<br/><br/>如您想進一步了解工作內容，請您回覆是否有意願或婉拒此邀約，謝謝您！<br/><br/>1111測試專用公司1(請勿應徵) 祝福您求職順利！<br/><div class='inform' style='margin: 15px 0 0 0; border-left: #e25656 solid 4px; padding: 0 0 0 10px;'>現場面試時間：2026/02/28　01:00。</div><br/><div class='inform' style='border-left: #e25656 solid 4px; padding: 0 0 0 10px;'>聯絡人： CC<br/>面試地點： 台北</div> <br/>",
      "interViewKind": 1,
      "dateSend": "2026-02-26T14:55:40.873",
      "duringTime": 0,
      "oViewDate": "2026-02-26T14:55:40.873",
      "tViewDate": "2026-02-26T14:56:00.8",
      "readflag": false,
      "tDelFlag": true,
      "oDelFlag": false,
      "wishReply": 0,
      "replyWishMsgDateIn": "2026-02-26T14:56:34.44",
      "replyWishMsgDetailNo": 1160172
    },
    {
      "bNo": 4,
      "msgKind": 1,
      "detailNo": 1160172,
      "mailNo": 9810503,
      "oUserNo": 28101870,
      "type": 1,
      "sendKind": 1,
      "message": "貴主管 您好：\r\n感謝您的來信，由於另有求職規劃，將婉拒本次的面試邀請，謝謝您。",
      "interViewKind": 1,
      "dateSend": "2026-02-26T14:56:34.44",
      "duringTime": 0,
      "oViewDate": "2026-02-26T14:56:37.997",
      "tViewDate": "2026-02-26T14:56:34.433",
      "readflag": false,
      "tDelFlag": true,
      "oDelFlag": false,
      "wishReply": 0
    },
    {
      "bNo": 5,
      "msgKind": 1,
      "detailNo": 1160173,
      "mailNo": 9810503,
      "oUserNo": 28101870,
      "oUserName": "李晚筠",
      "type": 1,
      "sendKind": 0,
      "message": "您好：<br/><br/>本公司透過1111人力銀行招募【遛狗人員 請勿應徵1】人才，本公司對您的資歷十分感興趣，誠摯邀請您來面試！<br/><br/>如您想進一步了解工作內容，請您回覆是否有意願或婉拒此邀約，謝謝您！<br/><br/>1111測試專用公司1(請勿應徵) 祝福您求職順利！",
      "interViewKind": 0,
      "dateSend": "2026-02-26T14:56:59.603",
      "duringTime": 0,
      "oViewDate": "2026-02-26T14:56:59.603",
      "tViewDate": "2026-02-26T14:57:55.88",
      "readflag": false,
      "tDelFlag": true,
      "oDelFlag": false,
      "wishReply": 0
    },
    {
      "bNo": 6,
      "msgKind": 1,
      "detailNo": 1161024,
      "mailNo": 9810503,
      "oUserNo": 28101870,
      "oUserName": "李晚筠",
      "type": 1,
      "sendKind": 0,
      "message": "您好：<br/><br/>本公司透過1111人力銀行招募【遛狗人員 請勿應徵1】人才，本公司對您的資歷十分感興趣，誠摯邀請您來面試！<br/><br/>如您想進一步了解工作內容，請您回覆是否有意願或婉拒此邀約，謝謝您！<br/><br/>1111測試專用公司1(請勿應徵) 祝福您求職順利！",
      "interViewKind": 0,
      "dateSend": "2026-03-02T13:47:23.14",
      "duringTime": 0,
      "oViewDate": "2026-03-02T13:47:23.14",
      "tViewDate": "2026-03-02T13:47:31.72",
      "readflag": false,
      "tDelFlag": false,
      "oDelFlag": false,
      "wishReply": 0
    },
    {
      "bNo": 7,
      "msgKind": 1,
      "detailNo": 1161128,
      "mailNo": 9838123,
      "oUserNo": 28129785,
      "oUserName": "育琳",
      "type": 0,
      "sendKind": 0,
      "message": "系統測試",
      "dateSend": "2026-03-02T16:10:53.607",
      "duringTime": 0,
      "oViewDate": "2026-03-02T16:10:53.607",
      "tViewDate": "1911-01-01T00:00:00",
      "readflag": false,
      "tDelFlag": false,
      "oDelFlag": false,
      "wishReply": 0
    }
  ],
  "tJsonB": [
    {
      "bNo": 1,
      "msgKind": 1,
      "detailNo": 1160165,
      "mailNo": 9810503,
      "oUserNo": 28101870,
      "oUserName": "李晚筠",
      "type": 1,
      "sendKind": 0,
      "message": "您好：<br/><br/>本公司透過1111人力銀行招募【遛狗人員 請勿應徵1】人才，本公司對您的資歷十分感興趣，誠摯邀請您來面試！<br/><br/>如您想進一步了解工作內容，請您回覆是否有意願或婉拒此邀約，謝謝您！<br/><br/>1111測試專用公司1(請勿應徵) 祝福您求職順利！",
      "interViewKind": 0,
      "dateSend": "2026-02-26T14:52:56.32",
      "duringTime": 0,
      "oViewDate": "2026-02-26T14:52:56.32",
      "tViewDate": "2026-02-26T14:53:41.77",
      "readflag": false,
      "tDelFlag": true,
      "oDelFlag": false,
      "wishReply": 0,
      "replyWishMsgDateIn": "2026-02-26T14:54:06.653",
      "replyWishMsgDetailNo": 1160167
    },
    {
      "bNo": 2,
      "msgKind": 1,
      "detailNo": 1160167,
      "mailNo": 9810503,
      "oUserNo": 28101870,
      "type": 1,
      "sendKind": 1,
      "message": "貴主管 您好：\r\n感謝您的來信，很高興能獲得貴公司的青睞，我對本次面試非常有意願，謝謝！",
      "interViewKind": 0,
      "dateSend": "2026-02-26T14:54:06.653",
      "duringTime": 0,
      "oViewDate": "2026-02-26T14:55:16.747",
      "tViewDate": "2026-02-26T14:54:06.65",
      "readflag": false,
      "tDelFlag": true,
      "oDelFlag": false,
      "wishReply": 0
    },
    {
      "bNo": 3,
      "msgKind": 1,
      "detailNo": 1160170,
      "mailNo": 9810503,
      "oUserNo": 28101870,
      "oUserName": "李晚筠",
      "type": 1,
      "sendKind": 0,
      "message": "您好：<br/><br/>本公司透過1111人力銀行招募【遛狗人員 請勿應徵1】人才，本公司對您的資歷十分感興趣，誠摯邀請您來面試！<br/><br/>如您想進一步了解工作內容，請您回覆是否有意願或婉拒此邀約，謝謝您！<br/><br/>1111測試專用公司1(請勿應徵) 祝福您求職順利！<br/><div class='inform' style='margin: 15px 0 0 0; border-left: #e25656 solid 4px; padding: 0 0 0 10px;'>現場面試時間：2026/02/28　01:00。</div><br/><div class='inform' style='border-left: #e25656 solid 4px; padding: 0 0 0 10px;'>聯絡人： CC<br/>面試地點： 台北</div> <br/>",
      "interViewKind": 1,
      "dateSend": "2026-02-26T14:55:40.873",
      "duringTime": 0,
      "oViewDate": "2026-02-26T14:55:40.873",
      "tViewDate": "2026-02-26T14:56:00.8",
      "readflag": false,
      "tDelFlag": true,
      "oDelFlag": false,
      "wishReply": 0,
      "replyWishMsgDateIn": "2026-02-26T14:56:34.44",
      "replyWishMsgDetailNo": 1160172
    },
    {
      "bNo": 4,
      "msgKind": 1,
      "detailNo": 1160172,
      "mailNo": 9810503,
      "oUserNo": 28101870,
      "type": 1,
      "sendKind": 1,
      "message": "貴主管 您好：\r\n感謝您的來信，由於另有求職規劃，將婉拒本次的面試邀請，謝謝您。",
      "interViewKind": 1,
      "dateSend": "2026-02-26T14:56:34.44",
      "duringTime": 0,
      "oViewDate": "2026-02-26T14:56:37.997",
      "tViewDate": "2026-02-26T14:56:34.433",
      "readflag": false,
      "tDelFlag": true,
      "oDelFlag": false,
      "wishReply": 0
    },
    {
      "bNo": 5,
      "msgKind": 1,
      "detailNo": 1160173,
      "mailNo": 9810503,
      "oUserNo": 28101870,
      "oUserName": "李晚筠",
      "type": 1,
      "sendKind": 0,
      "message": "您好：<br/><br/>本公司透過1111人力銀行招募【遛狗人員 請勿應徵1】人才，本公司對您的資歷十分感興趣，誠摯邀請您來面試！<br/><br/>如您想進一步了解工作內容，請您回覆是否有意願或婉拒此邀約，謝謝您！<br/><br/>1111測試專用公司1(請勿應徵) 祝福您求職順利！",
      "interViewKind": 0,
      "dateSend": "2026-02-26T14:56:59.603",
      "duringTime": 0,
      "oViewDate": "2026-02-26T14:56:59.603",
      "tViewDate": "2026-02-26T14:57:55.88",
      "readflag": false,
      "tDelFlag": true,
      "oDelFlag": false,
      "wishReply": 0
    },
    {
      "bNo": 6,
      "msgKind": 1,
      "detailNo": 1161024,
      "mailNo": 9810503,
      "oUserNo": 28101870,
      "oUserName": "李晚筠",
      "type": 1,
      "sendKind": 0,
      "message": "您好：<br/><br/>本公司透過1111人力銀行招募【遛狗人員 請勿應徵1】人才，本公司對您的資歷十分感興趣，誠摯邀請您來面試！<br/><br/>如您想進一步了解工作內容，請您回覆是否有意願或婉拒此邀約，謝謝您！<br/><br/>1111測試專用公司1(請勿應徵) 祝福您求職順利！",
      "interViewKind": 0,
      "dateSend": "2026-03-02T13:47:23.14",
      "duringTime": 0,
      "oViewDate": "2026-03-02T13:47:23.14",
      "tViewDate": "2026-03-02T13:47:31.72",
      "readflag": false,
      "tDelFlag": false,
      "oDelFlag": false,
      "wishReply": 0
    },
    {
      "bNo": 7,
      "msgKind": 1,
      "detailNo": 1161128,
      "mailNo": 9838123,
      "oUserNo": 28129785,
      "oUserName": "育琳",
      "type": 0,
      "sendKind": 0,
      "message": "系統測試",
      "dateSend": "2026-03-02T16:10:53.607",
      "duringTime": 0,
      "oViewDate": "2026-03-02T16:10:53.607",
      "tViewDate": "1911-01-01T00:00:00",
      "readflag": false,
      "tDelFlag": false,
      "oDelFlag": false,
      "wishReply": 0
    }
  ],
  "oDelFlag": false,
  "tDelFlag": true,
  "dateIn": "2026-03-04T16:37:26.53"
}
```

### API 欄位詳細描述

| 參數名稱 | 型別 | 說明 |
| --- | --- | --- |
| rNo | int | 流水號 (PK) |
| organNo | int | 廠商編號 |
| organName | string | 廠商名稱 |
| talentNo | int | 人才編號 |
| tName | string | 人才姓名 |
| tRole | int | 人才角色 |
| resumeNo | int | 履歷編號 |
| resumeGuid | string | 履歷 GUID |
| snapshotGuid | string | 快照 GUID |
| empNo | int | 職缺編號 |
| empName | string | 職缺名稱 |
| eRole | int | 職缺角色 |
| uNos | string | 使用者編號集合 |
| oJsonB | json | 廠商視角對話紀錄 (JSON 物件) |
| tJsonB | json | 求職者視角對話紀錄 (JSON 物件) |
| oDelFlag | bool | 廠商刪除標記 |
| tDelFlag | bool | 求職者刪除標記 |
| dateSend | datetime | 建立/更新時間 |

# JsonB欄位

| **參數名稱** | **型別** | **說明** | 前端備註 | 前端判斷 |
| --- | --- | --- | --- | --- |
| **BNo** | int | 序號 (自動編號) |  |  |
| **MsgKind** | byte | 合併來源類別：0:即時通 1:信件 |  |  |
| **DetailNo** | int | mailDetailNo / eChatLog.aNo |  |  |
| **MailNo** | int | mailNotice.MailNo |  |  |
| **OUserNo** | int? | 廠商使用者編號 |  |  |
| **OUserName** | string | 廠商使用者名稱 |  |  |
| **Type** | int | 信件類別 / 訊息類型：0-文字; 1-通話; 2-視訊; 3-圖片; 4-檔案; 5-通知 | mailType
0: '一般訊息',
1: '面試邀約',
5: '感謝函',
6: '錄取通知',
8: '面試異動', | ◆type 1 && interViewKind 1 → 面試邀約
◆type 1 && interViewKind 0 → 詢問意願 
◆type5 → 感謝函 (資料有的有傳 interViewKind 0 有的沒傳)
◆type6 → 錄取通知  (資料有的有傳 interViewKind 0 有的沒傳)
◆ type8 && interViewKind 1 →面試異動
◆ type8 && interViewKind 3 →面試取消 |
| **SendKind** | byte | 寄件者 (0:廠商 1:求職者 3:廠商系統訊息 4:求職者系統訊息 5:求才發給求職系統信 6:求職給求才系統信)

    寄件者(0:廠商 1:求職者 3:廠商系統訊息(廠商動作的訊息) 4:求職者系統訊息(求職動作的訊息)
  5求才發給求職系統信(3動作產生信件)  6求職給求才系統信(4的動作產生信件)) 7:求才回收 8:求職回收  9:求才即時通  10:求職即時通

  廠商端顯示：0,1,3,6,9,10
  求職端顯示：0,1,4,5,9,10
  廠商寄出信件：0,5
  求職者寄出信件：1,6
  求才回收訊息：7
  求職者回收訊息：8
  即時通廠商轉入：9
  即時通求職者轉入：10 | 9(視為0)即時通廠商轉入  , 10(視為1)即時通求職者轉入 |  |
| **Message** | string | 訊息內容 / 內文 |  |  |
| **InterViewKind** | byte? | 面試類別 (面試邀約種類代碼表) | 0: '詢問意願',
1:'實體面試'
3:'取消面試' |  |
| **DateSend** | DateTime | 寄送日期 |  |  |
| **StartTalk** | DateTime? | 開始(視訊)通話時間 |  |  |
| **EndTalk** | DateTime? | 結束(視訊)通話時間 |  |  |
| **DuringTime** | int | (視訊)通話經過時間(秒) |  |  |
| **FileName** | string | 檔案名稱 |  |  |
| **FilePath** | string | 檔案路徑：125/eChatFile/ |  |  |
| **ReplyWishMsg** | byte? | 求職者意願回覆 (0:未回覆 1:有意願 2:婉拒 3:更改時間) |  |  |
| **OViewDate** | DateTime? | 廠商已讀日期 |  |  |
| **TViewDate** | DateTime? | 求職者已讀日期 |  |  |
| **Readflag** | bool | 是否已讀：0-未讀; 1-已讀 |  |  |
| **TDelFlag** | bool | 求職者刪除標記 |  |  |
| **ODelFlag** | bool | 廠商刪除標記 |  |  |
| **OIgnore** | int? | 求職寫罐頭語會是1 (暫無用處) |  |  |
| **RevokeFlag** | byte? | 訊息回收 (1:已回收) |  |  |
| **RevokeUNo** | int? | 回收訊息的帳號編號 |  |  |
| **OIgnoreType** | int? | 面試用代碼: 400301 |  |  |
| **DisplayType** | string | 顯示類型 (0:一般字串 1:JSON格式字串) |  |  |
| **WishReply** | int | 是否能回覆(1HR) 0:未回覆 |  |  |
| **ReplyMailResult** | bool? | 回覆信件結果 (1HR, 求職端查用) |  |  |
| **MailTypeEhr** | int? | 信件類別 (1hr用) |  |  |
| **TalentNoEhr** | long? | 履歷編號 (1hr第三方履歷) |  |  |
| **ReplyWishMsgDateIn** | DateTime? | 求職者意願回覆時間 (求職端用) |  |  |
| **ReplyWishMsgDetailNo** | int? | 求職者意願回覆的 mailDetailNo (求職端用) |  |  |
| **DepartNoEhr** | int? | 部門 (1hr用) |  |  |

```bash
curl -X'GET' \'https://recruit.1111.com.tw/api/v1/echat/get-detail/1' \  -H'accept: */*'
```