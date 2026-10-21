---
name: tcode-bulletinboard
description: >-
  產出 job-classification-kb 專案 tCode 代碼表（tCodeDutyNM/PT/ST/HL、tCodeBenefit 等）的
  異動公告／異動清單時使用。當任務是要把新增(add)/改名(edit)/合併(move、move_edit)的項目整理成
  給人看的中文公告格式、發布系統公告、列出本輪異動明細時，觸發本 skill —— 即使使用者只說「發公告」
  「列異動項目」「整理這次的改動」沒有明講 skill 名稱。
  本 skill 服務的是 job-classification-kb/ 專案自己的 tCode 代碼表體系，跟 repo 另一個
  `tcode-excel-ops` skill（服務不同代碼表體系／不同專案）不重疊，不要混用。
---

# tCode 異動公告（tcode-bulletinboard）

本 skill 是指標，不在這裡重複內容。完整規則（輸出格式、按表分節、新增/改名/合併的分類方式、
資料來源鐵則）都在 job-classification-kb 專案內部文件：

**讀取 `job-classification-kb/skills/tcode-bulletinboard.md`，依該檔案的規則執行。**

一句話摘要（細節一律以上述檔案為準）：
- 輸出目的地是聊天訊息本身，不產生檔案，除非使用者另外要求存檔。
- 按 tCode 表分節（Certify／WorkAbility／DutyNM／DutyPT／DutyST／DutyHL／Benefit…），不跨表合併。
- 新增／改名／合併分三種小節格式，新增項目按類別分組用「、」串接。
- 判斷「這次改了什麼」務必拿「修改前／修改後」兩份獨立檔案逐欄比對，不要只信 ChangeType 標記或單一檔案自己的內容。
