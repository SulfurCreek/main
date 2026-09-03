---
name: hackmd-api
description: >
  已停用，內容併入 `wiki/hackmd_rules.md`。以程式呼叫 HackMD API（讀取／建立／更新／刪除 note、
  列出團隊文件、操作資料夾與排序、重建文件樹）時，改讀 `wiki/hackmd_rules.md`
  （端點細節見 `wiki/references/hackmd-api-endpoints.md`），不要用本檔或另開新的 hackmd-api skill。
---

# hackmd-api（已停用，內容併入 `wiki/hackmd_rules.md`）

**這個 skill 名稱保留這個空殼是為了避免其他分支/session 重新造一份。實際規則不在這裡。**

本檔原本內容（`claude/happy-lamport-ljis8c` 分支的獨立版本）已與 `wiki/hackmd_rules.md`
逐節比對過（2026-08-31）：Auth、端點總表、權限欄位規則、標題推導優先序、note/folder 欄位表、
folder-order PUT 覆蓋語意、把 note 移進資料夾的 UUID 陷阱——**全部內容相同**，僅有一處原本沒有的
新資訊（`GET /<noteId>/download` 免 token 唯讀捷徑），已補進 `wiki/hackmd_rules.md`〈Gotchas〉
與 `wiki/references/hackmd-api-endpoints.md`〈無 token 時的替代讀法〉。

**請改讀：**

- `wiki/hackmd_rules.md` — 認證、team path、本地快取＋安全回寫規則（規則 A–D）、端點總表、欄位參考、Gotchas
- `wiki/references/hackmd-api-endpoints.md` — 各端點完整 request/response、Folder API 全套、Node.js／Python／cURL 範例

**不要**：
- 在這個目錄下恢復完整內容，或另開一個新的 hackmd-api skill——會重新製造兩個真相來源
- 修改 `wiki/hackmd_rules.md` 時漏掉同步（本檔已無實質內容，不需要跟著改）

若之後發現 `wiki/hackmd_rules.md` 有遺漏、或有更適合走「skill 觸發」而非「wiki 動態檢索」的理由，
在這裡的討論串或 commit message 說明原因，而不是直接把內容搬回來。
