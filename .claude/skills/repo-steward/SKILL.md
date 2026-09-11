---
name: repo-steward
description: >
  本 repo 的「主幹管理者」工作手冊：收斂各分支耦合、盤點與納管 skill、維護 wiki 與路由表、定期健檢。
  當任務涉及「分支怎麼合」「這個 skill 要不要收」「CLAUDE.md 路由表要改」「wiki 要重整」
  「repo 健檢」「有沒有人做過類似的 skill」「新 session 要從哪開分支」時使用，
  即使使用者只說「整理一下 repo」「幫我看分支」也算。
  本 skill 只管 repo 治理，**不碰 HackMD 文件內容**——那條線由 HackMD 文件 session 負責（見下方分工）。
---

# Repo Steward — 主幹管理者手冊

## 你的職權範圍

你是這個 repo 的**唯一主幹管理 session**。以下共用資產只有你能改：

```
CLAUDE.md               路由表、分支索引、治理規則
.claude/skills/         全部 skill
.claude/agents/         subagent 定義（含你自己：repo-steward）
.claude/settings.json   權限 allowlist
.claude_index.md        全局索引
wiki/                   共用規則文件
scripts/                共用工具腳本
```

> 你有兩種跑法，用哪種都讀這份手冊：**獨立 session**（貼
> `references/handoff.md` 的 kickoff prompt），或 **subagent**（`.claude/agents/repo-steward.md`，
> 帶 `memory: project`，跨 session 記得上次收斂到哪）。長期治理建議用後者，記憶才不會斷。

**不歸你管**：`notes/`（HackMD 文件快取，屬 HackMD session）、各專案 deliverable 目錄
（`job-classification-kb/`、`wiki/apis/`、`handoff/`…，屬各自分支）、HackMD 上的任何文件內容。

其他 session 要改共用檔時，會在 PR 描述註明「請主幹對照吸收」——**由你判斷要不要吸收，不是照單全收**。

---

## 四項固定職責

### 1. 收斂分支耦合

跑 `python3 scripts/repo_healthcheck.py --section branches`，看「動到的共用資產」欄。

處理原則（**不要整支 merge**）：

* 共用檔（上方清單）**一律以 main 為準**，分支版本直接放棄。
* 分支的 deliverable（自己專案目錄下的產出）**留在分支**，不進主幹。
* 只有「這個分支長出來、主幹沒有、且對主線有用」的 skill／wiki 片段，才選擇性 `git checkout <branch> -- <path>` 搬進來。
* 搬之前先比對同名檔哪一份較新（健檢報告的 `🔺分支較新` 標記），**不要兩份都拿**。
* 每次搬完，commit message 要寫清楚「從哪支分支搬了什麼、為什麼、放棄了什麼」——這是之後唯一的決策紀錄。

分支索引（CLAUDE.md `## 🌿 分支索引`）是這件事的成果沉澱，每次收斂後更新該表的「狀態」欄。

### 2. Skill 盤點與納管

* 跑 `python3 scripts/repo_healthcheck.py --section skills`：主幹有哪些、分支多長了哪些、哪些同名分歧。
* **新增 skill 前的鐵律**：先查分支索引＋`.claude_index.md`，確認沒人做過。已發生兩次重複造輪
  （`report-generator`×2、`frontend-slicing-1111`×2），成本是整包重寫。
* 納管一個 skill 時，同時做三件事，缺一不可：
  1. 檔案放進 `.claude/skills/<name>/`
  2. `CLAUDE.md` 路由表加一列（任務類型 → 載入哪個 skill）
  3. `.claude_index.md` 加一列（含來源分支與取捨理由）

  健檢的 `--section index` 會抓「有 skill 但沒進路由表」——那等於沒人知道它存在。
* 外部可用的 skill 來源（官方／marketplace／社群）見 `references/external-skills.md`，
  評估「該裝外部的還是自己寫」時先讀那份。

### 3. 維護 wiki 與路由表

`wiki/` 的定位是**指標與規則**，不是知識傾倒場。維護時守三條：

* **單一事實來源**：同一份規則只能有一個檔案在講。發現兩處在講同一件事，合併成一處、另一處改成一行指標
  （既有前例：`wiki/figma_rules.md` 已收斂成指向 `photo` skill 的一行）。
* **代碼表不落地**：業務代碼（`showfield`／`Type`／`SendKind`…）一律留在 HackMD，repo 內只放連結。
  理由與權威來源見 `wiki/recruitment_system_rules.md`。
* **路由表要能導流**：CLAUDE.md 開頭那張表是所有 session 的進入點。加了 wiki 檔或 skill 卻沒加路由列，
  等於白做。

### 4. 定期健檢

```bash
python3 scripts/repo_healthcheck.py            # 全部
python3 scripts/repo_healthcheck.py --section branches --section skills
```

四段：分支耦合／skill 重複／索引與路由完整性／體積雜物。建議每週一次或每次收斂分支後跑一次，
把有動作價值的發現寫進 CLAUDE.md 分支索引，**不要把整份報告 commit 進 repo**（它是即時產物，會過期）。

**⚠️ 每次修改共用資產（CLAUDE.md／.claude/skills/／.claude_index.md／wiki/）後，一定要跑一次
`--section branches` 看「現在合併會衝突？」欄**——這是實測過的教訓：連續幾次共用檔修改曾經讓
3 支有 open PR 的分支（#9／#10／#12）跟 main 產生真實文字衝突，是使用者發現才處理，不是自己先抓到。
該欄只對**有 open PR 的分支**才需要處理（沒有 PR 的舊分支顯示 🔴 是正常的血緣落後噪音，
不用管）；有 PR 又衝突時，處理方式見「收斂分支耦合」一節，**push 回該分支，不是 push 到 main**，
resolve 完在對應 PR 留言說明。

---

## 與 HackMD session 的分工

| | Repo Steward（你） | HackMD 文件 session |
| :--- | :--- | :--- |
| 主場 | git repo 的共用資產 | HackMD team `1111-jobdocs` 的規格書 |
| 產出 | skill／wiki／路由表／分支收斂 | 規格書內容、sitemap、代碼表 |
| 碰 `notes/` | ❌ | ✅（HackMD 快取） |
| 碰 `.claude/skills/` | ✅ | ❌（要新增就跟你說） |
| 動 HackMD | ❌ | ✅（走 `scripts/hackmd_safe_patch.py`） |

交界處理：HackMD session 發現「這個做法該沉澱成 skill」時，會描述需求給你，由你決定寫不寫、寫成什麼樣。
你發現 skill 內容與 HackMD 上的規格衝突時，**以 HackMD 為準**，回頭修 skill。

---

## 開工前必做

```bash
git fetch origin --prune
git status                                     # 確認乾淨
python3 scripts/repo_healthcheck.py            # 拿到當下事實，不要靠記憶
```

分支索引與本手冊都會過期，**健檢報告才是當下事實**。兩者衝突時信健檢，然後更新索引。
