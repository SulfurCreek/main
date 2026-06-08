---
name: gsheet-vendor-identity
description: >
  查詢「廠商身分」Google Sheet 資料表中特定功能項目（頁面區塊）的完整廠商身分狀態資料。
  當使用者提到要查某個功能編號（如 A.1.7）或功能名稱（如「全站異常狀態顯示文案」）對應的各廠商身分文案或行為時，使用本 skill。
---

# 廠商身分 Google Sheet 查詢（gsheet-vendor-identity）

本 skill 從專案的 Google Sheet「廠商身分」工作表抓取特定功能列的完整資料。

## 資料來源

- **試算表 ID**：`1cLqoBpmjkMkWa_ZJ9pDQNektQsnPlcehNcnA1wwuSmY`
- **工作表名稱**：`廠商身分`
- **CSV 匯出 URL**：
  ```
  https://docs.google.com/spreadsheets/d/1cLqoBpmjkMkWa_ZJ9pDQNektQsnPlcehNcnA1wwuSmY/gviz/tq?tqx=out:csv&sheet=廠商身分
  ```

## 欄位結構

| 欄位名稱 | 說明 |
|----------|------|
| Module | 模組代號（A、B、C…） |
| 頁面名稱 | 模組全名（如 A. 首頁） |
| 頁面區塊／身分 | 功能編號＋名稱（如 A.1.7 全站異常狀態 顯示文案） |
| 普通會員(oStatus: 0) | 普通會員的行為或文案 |
| VIP(oStatus: 1) | VIP 的行為或文案 |
| VIP有下一單合約(oStatus: 1) | VIP 且有下一單合約的行為或文案 |
| 到期(oStatus: 2) | 到期狀態的行為或文案 |
| 關權(oStatus: 3) | 關權狀態的行為或文案 |
| 關權超過30天(oStatus: 3) | 關權超過 30 天的行為或文案 |
| 免費VIP(oStatus: 4) | 免費 VIP 的行為或文案 |
| 免費曝光(oStatus: 5) | 免費曝光的行為或文案 |
| 免費曝光非VIP或已到期(oStatus: 5) | 免費曝光且非 VIP 或已到期的行為或文案 |
| 準VIP有下一單合約(oStatus: 6) | 準 VIP 且有下一單合約的行為或文案 |
| 準VIP無下一單合約(oStatus: 6) | 準 VIP 且無下一單合約的行為或文案 |

## 使用步驟

1. 用 `WebFetch` 抓取 CSV（URL 如上），redirect 時接著抓 redirect URL。
2. 在 prompt 中指定：「找出『頁面區塊／身分』欄位包含 `{使用者指定的編號或關鍵字}` 的那一整列，完整回傳所有欄位的值，不要省略任何欄位」。
3. 將回傳結果整理成 Markdown 表格呈現給使用者。

## 輸出格式

以 Markdown 表格呈現，欄位為各廠商身分狀態（oStatus），列值為對應文案或行為。範例：

| 身分狀態 | 值 |
|---|---|
| 普通會員 (oStatus:0) | 尚未成為VIP會員 |
| VIP (oStatus:1) | 不顯示 |
| ... | ... |
