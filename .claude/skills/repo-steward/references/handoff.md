# 交接文件：Repo Steward session

> 交接日：2026-09-10　來源：HackMD 文件 session
> 最後更新：2026-09-10（第一批收斂已完成，見下方第二節）
> 這份是**當下狀態快照＋已知的坑**，會過期。開工先跑 `python3 scripts/repo_healthcheck.py` 拿即時事實，
> 兩者衝突時信健檢報告，然後回來更新這份與 CLAUDE.md 分支索引。

## 一、現況快照（2026-09-10 收斂後）

| 項目 | 狀態 |
| :--- | :--- |
| 主幹 | `main`（唯一主幹，2026-08-31 由 PR #15 升格） |
| 遠端分支 | 13 支（含 main）；`claude/claude-md-docs-BmaVo` 已停用、🚧 待手動刪除 |
| Skill 總數 | 22 個，全在 `.claude/skills/`，全部已進 CLAUDE.md 路由表與 `.claude_index.md` |
| Open PR | #9（email-layout）／#10（csv-retrieval）／#12（vm-api）／#13（part-time-modal），base 均已改指 `main` |
| 索引健康度 | ✅ 受管檔案都有進索引、所有 skill 都有路由列、無 >1MB 版控檔 |

## 二、第一批收斂（2026-09-10，已完成）

三支「2026-08-31 稽核後又動過」的分支已處理完，結論已沉澱進 CLAUDE.md 分支索引：

1. **`gifted-meitner-6eSoK` → 全數吸收**：`photo/SKILL.md` 併入，含使用者裁定採用的
   **「圖片一律遷移 R2」政策異動**（不再沿用既有 `hackmd.io/_uploads` 網址），
   連帶修正 `spec-doc-1111/references/styling.md` 的圖床與限寬寫法。
2. **`google-sheet-url-allowlist-GKFEU` → 收版型庫、砍 PDF**：`references/設計描述五層面.md`
   與 `references/html-templates/`（77 版型，Apache-2.0）併入 `report-generator`；
   1.8MB 來源 PDF 不收（超過 1MB 門檻，內容已萃取）。
3. **`email-layout-handoff-gjq5zu` → 一律不吸收**：3 處共用檔改動逐段複查，
   其中〈規格書 UI 截圖標號慣例〉是**已棄用規則**（Pillow 燒 badge＋GitHub raw 圖床），
   與主幹現行的 `photo` skill（HTML overlay＋R2）直接衝突，吸收會讓主幹倒退。

**下一批可做的**：`vm-api-testing-setup-wpf6y8`（落後 59、動到 4 類共用檔）與
`happy-lamport-ljis8c`／`csv-retrieval-retry-do5a9o`／`eloquent-maxwell-j31ot5` 都只是血緣落後，
健檢已判定「分支較舊」，**不需要逐支去合**；只有健檢標 `🔺分支較新` 的才要人工比對。

## 三、已知的坑（別踩）

* **`hackmd-api` skill 是「刻意的空殼重導向」**，不是壞掉。內容已併入 `wiki/hackmd_rules.md`，
  留一個 SKILL.md 只為了擋其他 session 重建重複的參考來源。**不要把 `happy-lamport-ljis8c` 的完整版還原回來。**
* **`mermaid-sequence-diagram` skill 已裁定不收錄**。它的冷灰／莫蘭迪配色與本 repo 的柔色系衝突，
  使用者 2026-08-31 明確裁定採柔色系；非配色的機制（`box` 分組、`autonumber`、字級間距）
  已改寫成柔色系 token 併入 `wiki/mermaid_styling_rules.md` §4。**不要重新評估配色，那件事結案了。**
* **重複造輪已發生兩次**：`report-generator`（csv-retrieval 與 extract-job-duty 各做一份，逐位元組相同）、
  `frontend-slicing-1111`（eloquent-maxwell 舊版 vs email-layout 新版）。新增前一定先查索引。
* **`job-classification-kb` 那一串 skill 是不同專案**（職務分類／不合理清單），與本 repo 主線
  （1111 求才系統規格書）無關，只是借放當共用 skill 庫。不要試圖把它整合進主線敘事，
  也不要把該專案的資料目錄搬進主幹。
* **`spec-doc-1111` 在 7 支分支上都是舊版**——那是正常的血緣落後，不是分歧，別逐支去合。
* **舊分支的共用檔改動可能是「已棄用規則」，不是「主幹漏收的新東西」**：`email-layout-handoff-gjq5zu`
  往 CLAUDE.md 加的〈規格書 UI 截圖標號慣例〉要求 Pillow 燒 badge＋GitHub raw 圖床，兩者主幹都已棄用。
  **判斷方法：先看該分支的分岔點日期，再看它改的規則在主幹是不是已經被更新過**——分支較舊卻動到共用檔，
  預設是倒退而不是補充。
* **本環境不能刪遠端分支**：`git push origin --delete` 會被 proxy 擋（HTTP 403），
  GitHub MCP 也沒有 delete branch 工具。要刪分支只能請使用者在 GitHub 網頁操作。
* **不要 force-push**，不要整支 `git merge` 老分支（分岔規模動輒 100+ commit，衝突成本遠大於選擇性搬運）。
* `career/` 是使用者的個人職能框架，2026-08-31 經明確同意才併入（`resume-craft` skill 依賴它）。
  已做過 secret 掃描。不要再對它做結構性改動。

## 四、兩個 session 的交界

* **你（Repo Steward）**：`CLAUDE.md`／`.claude/skills/`／`.claude/settings.json`／`.claude_index.md`／`wiki/`／`scripts/`
* **HackMD session**：HackMD team `1111-jobdocs` 的文件內容、`notes/` 快取

交界規則：

* HackMD session 覺得某個做法該沉澱成 skill → 描述需求給你，**由你決定寫不寫、怎麼寫**。
* 你發現 skill 內容與 HackMD 規格衝突 → **以 HackMD 為準**，回頭修 skill。
* 兩邊都不要動對方的主場檔案。真的需要，開 PR 並在描述註明請對方吸收。

## 五、怎麼啟動（兩種都可以）

### A. subagent（建議，有跨 session 記憶）

`.claude/agents/repo-steward.md` 已經建好，帶 `memory: project`。直接叫它即可，
它會把「上次收斂到哪、哪些議題已裁示」寫進 `.claude/agent-memory/repo-steward/`，下次接得上。

### B. 獨立 session — kickoff prompt

開新 session 時貼這段：

```text
你是這個 repo（sulfurcreek/main）的主幹管理 session（Repo Steward）。

開工第一件事：
  git fetch origin --prune
  python3 scripts/repo_healthcheck.py

然後用 Skill 工具載入 `repo-steward`，那是你的工作手冊；
`.claude/skills/repo-steward/references/handoff.md` 是前一個 session 的交接文件，
裡面有現況快照、第一批任務、已知的坑，開工前讀完。

你的職權範圍是共用資產（CLAUDE.md／.claude/skills/／.claude/settings.json／
.claude_index.md／wiki/／scripts/），四項職責：收斂分支耦合、盤點納管 skill、
維護 wiki 與路由表、定期健檢。

不要碰 HackMD 上的任何文件內容，也不要改 notes/ —— 那條線由另一個 session 負責。
在 main 上直接工作，push 前先確認 git status 乾淨。
```
