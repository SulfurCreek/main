---
name: session-router
description: >
  跨 session／分支「這是誰的工作」判斷手冊。當使用者的請求可能不屬於目前這個分支／session
  的職責範圍時（例如在 Repo Steward session 被要求分析 CSV、在文件 session 被要求改 API 測試腳本、
  在職務分類 session 被要求設計前端 modal），或使用者直接問「這個誰負責」「要換去哪個 session」
  「這件事誰在處理」「幫我 cue 一下」「該去哪個分支做」時，必須先讀 `wiki/session_directory.md`
  查清楚職責歸屬，再決定是自己做還是告知使用者該去哪個 session——不確定是不是自己的工作時，
  先查表，不要憑感覺接手（造成重工／耦合）也不要憑感覺回絕。
---

# Session Router — 職責邊界判斷

## 目的

本 repo 有多支 Claude Code Remote session 各自認養不同任務網域（見 `wiki/session_directory.md`）。
沒有邊界機制時，一個 session 收到「順手就能做」的跨網域請求容易直接接手，結果是同一件事被
兩支分支重複做、或該 session 用著自己那套（可能較舊的）規則去做另一個網域的事。這個 skill
就是「先查清楚再動手」的判斷流程。

## 跨 session 傳訊息：雲端 session 之間實際送不到（2026-09-29 實測）

環境裡有 `SendMessage`／`ListAgents`，但**雲端 session 之間實際送不到**。2026-09-29 從 Repo Housekeeping
對「規格文件html示意圖助手」（RUNNING＋connected）與「文件助手」（connected）分別用側欄名稱、
session ID 定址，全部回 `No agent named '…' is reachable`；`ListAgents` 也列不出任何 session。
`list_sessions` 查得到、狀態是 RUNNING，都**不代表**送得到。

**所以「cue」＝盡力把歸屬講清楚，不是代為轉發**：
- 仍先跑一次 `ListAgents`（工具之後可能開放）。真的列出目標才用 `SendMessage`，並提醒對方無法回覆。
- 列不出來（目前一律如此）→ 回報歸屬（側欄名稱＋分支＋現況）＋一段使用者可直接貼過去的指令。
- ❌ 不要說「我已經 cue 過去了」。不能請別的 session 代做自己被擋的動作。

## 使用流程

1. **確認自己是誰**：`git branch --show-current`。
2. **讀 `wiki/session_directory.md`**，用使用者需求的關鍵字比對「網域對照表」。
3. **判斷結果分三種**：

   **(a) 網域對應到自己所在的分支** → 這就是自己的工作，正常做，不用特別聲明歸屬。

   **(b) 網域對應到別的分支** → **不要動手**。跟使用者說清楚三件事：
      - 側欄名稱（快照）
      - 分支名稱
      - 一句話現況（IDLE/RUNNING/ARCHIVED/blocked 等，快照時間點）

      有 `mcp__Claude_Code_Remote__list_sessions`（`mine: true`）工具可用時，**優先即時查一次**，
      用回傳的 `outcomes[].git_repository.git_info.branches` 比對目標分支，抓最新的
      session id／title／`session_status`／`post_turn_summary` 回報給使用者，並註明
      「以下是即時查詢結果，不是 wiki 快照」；查不到對應分支的活躍 session 時，老實說
      「這個分支目前查不到活躍 session，你可能要自己開一個新的」，不要瞎猜。

      沒有該工具可用時，直接用 wiki 快照回報，並提醒使用者「這是 2026-09-10 的快照，
      側欄名稱／狀態可能已經變了，分支名稱本身應該還準」。

   **(c) 網域不在表上（全新需求）** → 不要用「最接近」硬套一個網域。直接問使用者：
      這算既有哪個分支的延伸，還是該開一支新分支／新 session；開新分支一律從最新 `main` 開始
      （治理規則 #1）。

4. **邊界鐵律**：不是自己網域的事，不要因為「反正我也能做」就順手接手——這正是本 repo
   耦合與重複造輪的根因（`report-generator`／`frontend-slicing-1111` 都各自被造過兩次）。
   先講清楚歸屬，讓使用者自己決定要不要現在就跨界處理；使用者明確說「沒差，你直接做」時，
   才在當前 session 動手，且完工後提醒一句「這個結果建議之後同步給 `<owning session>`，
   不然那邊之後可能不知道」。

## 維護

`wiki/session_directory.md` 是共用資產，只有主幹管理（Repo Steward）session 能改。其他 session
發現分類過期、有新網域、或表上的 session 已經不在了，提醒使用者或在自己的 PR 描述寫一段
「請主幹更新 session_directory」，不要自己動手改。
