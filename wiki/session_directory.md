# 跨 Session／分支職責對照表

> 用途：任何 session 收到「感覺不是自己主線」的請求時，查這份表決定「這是誰的工作」，
> 而不是憑感覺接手（造成重工／耦合）或憑感覺拒絕。搭配 `.claude/skills/session-router/SKILL.md` 使用。
>
> ⚠️ **本表是快照，只有下方「分支」欄穩定**（git 分支不會自己改名）。「側欄名稱」「session_id」
> 「現況」是 2026-09-10 用 `mcp__Claude_Code_Remote__list_sessions`（mine:true）即時查到的結果，
> **使用者隨時可能改名、封存、開新分支**，過期的機率比 git 分支本身高很多。要精準最新狀態，
> 有該工具時務必重查一次，用「分支」欄位對照，不要只信這份表的「側欄名稱／現況」。
> 只有主幹管理（Repo Steward）session 能更新本表；其他 session 發現分類過期或有新網域，
> 提醒使用者或在 PR 描述請主幹更新，不要自己改。

## 職責對照表（2026-09-10 快照）

| 網域關鍵字 | 側欄名稱（快照） | 分支 | session_id（快照） | 現況（快照） |
| :--- | :--- | :--- | :--- | :--- |
| HackMD 規格書內容撰寫、1111 求才/求職系統文件、E.1 聯絡人才整併、履歷文件編修 | 文件助手 | `main`（outcome 歷史上寫 `claude/claude-md-docs-BmaVo`，⚠️見下方特別注意） | `session_01Cd8ro9qHrxAgVDh98ePdZf` | **RUNNING** |
| Repo 治理：分支收斂、skill 納管、wiki／路由表維護、健檢 | Repo Housekeeping | `main` | `session_01KDak6qp7Eim1Zt3inztq7v` | RUNNING（本 session） |
| 職務分類／不合理清單／AI 職類推薦模型／TCode 代碼表比對／廠商身分 Google Sheet | tCode幫手 | `claude/google-sheet-url-allowlist-GKFEU` | `session_01UHEjnAEkd1cRB7C9gHkUcj` | IDLE，completed |
| 數據分析報告寫作／HTML 報告產出 | 產生HTML報告 | `claude/extract-job-duty-markdown-4avmd6` | `session_01QXs4QyHUx32r5AxVpJtYoj` | IDLE，review_ready |
| Lo-fi wireframe 線框圖草稿 | Lo-fi wireframer skill | `claude/lofi-wireframer-skill-0u25rk` | `session_019WwXEooe1HuTjpLbhHueEQ` | IDLE，review_ready |
| API 測試（Talent Sourcing Gateway API 等）、pytest 測試矩陣 | 虛擬機器 API 測試環境 | `claude/vm-api-testing-setup-wpf6y8` | `session_01THk1wnhhqk5NheyvzBqncj` | IDLE，blocked（等待回覆是否記錄回歸結果） |
| 信件訊息頁前端修改工程單／未讀履歷提醒統計／切版 | 未讀提醒 **或** 網頁分析工具（⚠️見下方特別注意） | `claude/email-layout-handoff-gjq5zu` | 未讀提醒＝`session_01ERFbn8cEWMfmDPEdMxJs4T`；網頁分析工具＝`session_0155Dp5oiYKgfH9BRhStd5T6` | 未讀提醒＝review_ready；網頁分析工具＝blocked（push 403，卡在確認 PR base 該不該改 main） |
| 兼職職缺（工讀生停用說明）modal 設計 | （已封存，不在側欄） | `claude/part-time-modal-design-tmtt7n` | `session_01UCest88UyhV6wBo2myhk1A` | ARCHIVED——有新需求要另開 session |
| 履歷／個人職能框架撰寫（resume-craft 相關舊分支） | Career move function definition | `claude/happy-lamport-ljis8c` | `session_018VJFZiuZYfnPhMppvaGFcR` | IDLE，review_ready——但 `resume-craft` skill 本體已併入 main，**新的履歷需求直接找「文件助手」（main）即可**，不必回這支舊分支 |
| Figma 截圖標註／規格書示意圖 | 規格文件html示意圖助手 | `claude/gifted-meitner-6eSoK` | `session_01HouvBCKKpMkZARx7CKhh6X` | IDLE，completed——`photo` skill 已全數併入 main，**新需求直接找「文件助手」（main）即可** |
| CSV／Excel／Google Sheet 資料分析（新需求、尚無指定分支） | CSV/Excel data analysis | `csv-excel-gsheet-analysis-9kQmZ2`（⚠️不在 CLAUDE.md 既有分支索引，2026-09-10 才新建） | `session_01Fug6iscZrsqXo3Msi4yAbW` | IDLE，等待提供資料或任務——**目前是空的，適合接手任何新的 CSV/Excel/GSheet 分析需求** |

## 已停用／不要去的分支

| 分支 | 側欄名稱（快照） | 狀態 | 新需求怎麼辦 |
| :--- | :--- | :--- | :--- |
| `claude/eloquent-maxwell-j31ot5` | UI切版需求助手(archived) | ARCHIVED，已被 `email-layout-handoff-gjq5zu` 取代 | 前端切版需求找上表「未讀提醒／網頁分析工具」 |
| `claude/csv-retrieval-retry-do5a9o` | （查無對應活躍 session） | skill 已併入 main | CSV 相關新需求找「CSV/Excel data analysis」 |
| `claude/static-html-github-deploy-1h0w1c` | （查無對應活躍 session） | 已結案（PR #4 已關閉） | — |

## 不同 repo，本索引不管

| repo | 側欄名稱（快照） | session_id | 說明 |
| :--- | :--- | :--- | :--- |
| `SulfurCreek/sulfurcreek.github.io` | EPK | `session_01KnZZpEqNjB5VWW5wvnxnMR` | 個人網站，跟本 repo（`SulfurCreek/main`）無關，只是避免使用者側欄搞混才列出來 |

## ⚠️ 特別注意（2026-09-10 發現，待處理）

1. **「文件助手」目前仍把 `claude/claude-md-docs-BmaVo` 當 outcome 分支，這支分支還在被實際使用**。
   Repo Steward 先前（同日稍早）誤判該分支「內容已完全含於 main、可安全刪除」——**這個判斷需要收回**，
   刪之前要先確認「文件助手」不會再往那支推東西，否則會讓它下次推送失敗。
2. **「未讀提醒」與「網頁分析工具」是兩個獨立 session，卻共用同一條分支** `claude/email-layout-handoff-gjq5zu`——
   兩邊如果各自 commit／push，會互相蓋掉對方或衝突。建議之後只留一個在用，另一個封存。
3. `csv-excel-gsheet-analysis-9kQmZ2` 是全新分支，不在 CLAUDE.md 分支索引裡；等它有實際產出後，
   由 Repo Steward 補進 CLAUDE.md 分支索引。

## 沒有找到對應網域時怎麼辦

上表沒有匹配的關鍵字，不要用「最接近」硬套，直接跟使用者確認：這算既有哪個分支的延伸、
還是該開一支新分支／新 session。開新分支一律照治理規則從最新 `main` 開始。
