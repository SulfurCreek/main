# 交接文件：Repo Steward session

> 交接日：2026-09-10　來源：HackMD 文件 session（`claude/claude-md-docs-BmaVo`）
> 這份是**當下狀態快照＋已知的坑**，會過期。開工先跑 `python3 scripts/repo_healthcheck.py` 拿即時事實，
> 兩者衝突時信健檢報告，然後回來更新這份與 CLAUDE.md 分支索引。

## 一、現況快照（2026-09-10）

| 項目 | 狀態 |
| :--- | :--- |
| 主幹 | `main` == `claude/claude-md-docs-BmaVo` == `2faeb26`（2026-08-31 由 PR #15 升格） |
| 遠端分支 | 13 支（含 main），其中 11 支是各 Claude session 的獨立產出 |
| Skill 總數 | 21 個，全在 `.claude/skills/`，全部已進 CLAUDE.md 路由表與 `.claude_index.md` |
| Open PR | #9（email-layout）／#10（csv-retrieval）／#12（vm-api）／#13（part-time-modal） |
| 索引健康度 | ✅ 受管檔案都有進索引、所有 skill 都有路由列、無 >1MB 版控檔 |

⚠️ **注意：4 個 open PR 的 base 都指向 `claude/claude-md-docs-BmaVo`，不是 `main`。**
兩者目前同 commit 所以看起來沒差，但之後只要主幹往前走就會分岔。要嘛把 base 改成 `main`，
要嘛維持「這 4 支是專案 deliverable、本來就不進主幹」的既有裁示（2026-08-31 已留言說明政策）。

## 二、開工第一批任務（照順序做）

1. **`photo` skill 有分支版比主幹新** — `claude/gifted-meitner-6eSoK` 的 `photo` 是 2026-09-01，
   主幹版是 2026-08-31。該分支的主題正是 photo/png skill 改進，很可能有主幹沒吸收的東西。
   逐段比對後決定吸收哪些，**不要整包覆蓋**（主幹版已有其他 session 驗證過的內容）。
2. **3 支分支在 2026-08-31 稽核後又動過**，分支索引的「最後更新」欄已過期：
   `google-sheet-url-allowlist-GKFEU`（09-08，超前 108 commit）、`email-layout-handoff-gjq5zu`（09-03）、
   `gifted-meitner-6eSoK`（09-01）。先看它們新增了什麼，再更新索引表。
3. **`email-layout-handoff-gjq5zu` 動到 `CLAUDE.md` 與 `wiki/`** — 這是治理規則 #2 明文禁止的
   （共用檔只有主幹能改）。處理方式：共用檔取 main 版本、只保留該分支自己的 `handoff/` deliverable，
   並在 PR #9 留言提醒。
4. 跑一次完整健檢，把有動作價值的發現沉澱進 CLAUDE.md 分支索引。

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
