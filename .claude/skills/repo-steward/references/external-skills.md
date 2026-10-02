# 外部可用的 skill／plugin／內建機制盤點

> 調查日：2026-09-10。**下面分「已實地驗證」與「未驗證線索」兩區，未驗證的不要直接 clone。**
> 評估「該裝外部的還是自己寫」時讀這份；決定要裝什麼之前，先確認該來源當下還活著。

## 一、結論先行：該裝 vs 該自己寫

| 職責 | 建議 | 理由 |
| :--- | :--- | :--- |
| 1. 收斂分支耦合 | **自己寫**（已有 `scripts/repo_healthcheck.py`） | 公開生態**沒有**任何工具在做「長壽分支收斂／跨分支重複資產偵測」，這個缺口是真的 |
| 2. Skill 盤點（內部） | **自己寫**（`.claude_index.md` 已足夠） | 現有做法可行，不需要外部索引器 |
| 2. Skill 盤點（外部） | **直接讀官方 JSON** | `anthropics/skills` 與 `claude-plugins-official` 的 marketplace.json 都是機器可讀，不需要爬蟲 |
| 3. 維護 wiki／路由表 | **裝 `claude-md-management`** ＋ 考慮遷移到 `.claude/rules/` | 官方已有 CLAUDE.md 稽核工具，不用重寫 |
| 4. 定期健檢 | **自己的腳本 ＋ 官方 GitHub Action 排程** | 判斷邏輯自己寫，排程用現成的 |

## 二、已驗證（可直接用）

### 官方 skill 庫 — <https://github.com/anthropics/skills>

2026-09 初仍活躍。收錄：`academy-guide`、`algorithmic-art`、`brand-guidelines`、`canvas-design`、
`claude-api`、`discernment-nudge`、`doc-coauthoring`、`docx`、`frontend-design`、`internal-comms`、
`mcp-builder`、`pdf`、`pptx`、`skill-creator`、`slack-gif-creator`、`theme-factory`、
`web-artifacts-builder`、`webapp-testing`、`xlsx`。

**官方沒有任何 repo 治理類 skill**，不用等。與本 repo 相關的只有 `skill-creator`（寫／改 skill 用，
本 repo 的 `spec-doc-1111` 已註記大改時該用它）與 `doc-coauthoring`。

### Plugin（每一個都已實地開過 marketplace.json）

| Plugin | 來源 | 用途 | 對應職責 |
| :--- | :--- | :--- | :--- |
| `claude-md-management` | `anthropics/claude-plugins-official` | `claude-md-improver` 拿 CLAUDE.md 對照實際 codebase 稽核；`/revise-claude-md` 把 session 心得寫回 | **3、4（最貼近）** |
| `plugin-dev` | 同上 | 寫 plugin／marketplace 的工具與驗證器 | 2 |
| `code-review`／`pr-review-toolkit`／`commit-commands` | `anthropics/claude-code` marketplace | PR 審查 agent、commit/PR 流程 | 1（只到 PR 衛生） |
| `hookify` | 同上 | 從觀察到的壞習慣自動生成 hook | 4 |
| `gitkraken` | `gitkraken/claude-plugin` | 把跨 repo 的 commit／branch／PR／issue 餵給 Claude | 1（只給資料，不做決策） |
| `lumen` | `ory/lumen` | 本地語意程式碼搜尋（Go AST＋embedding） | 2（**本 repo 是 markdown 不是程式碼，效益低**） |

> 官方 marketplace 有 200+ plugin，絕大多數是廠商整合。**查無**分支收斂／重複資產偵測／多 session 協作類 plugin。

### 內建機制（比裝 plugin 更該優先用）

* **`.claude/rules/` ＋ frontmatter `paths:` glob** — 規則只在 Claude 碰到符合的檔案時才載入。
  這是目前 CLAUDE.md 那張路由表的**原生替代品**，可大幅減少每個 session 的固定開銷。
  文件：<https://code.claude.com/docs/en/memory>　**→ 這是這次調查最有價值的一項。**
* **`@path` import**：相對／絕對路徑都支援，最多 4 層，反引號內不生效。
  注意：import 仍會在啟動時全部載入，**只整理結構、不省 context**。
* **Hooks**（35 種事件）：`SessionStart`、`InstructionsLoaded`（記錄實際載入了哪些指令檔——
  這是「哪些 wiki 檔其實沒人在用」的實證答案）、`Stop`（官方文件本身就建議用它提議 CLAUDE.md 更新）。
* **Subagent**（`.claude/agents/*.md`）：支援 `model:`／`tools:` 限制與 **`memory: project`**
  （寫進 `.claude/agent-memory/<name>/`）。**skill 不會跨 session 保留狀態，subagent memory 會**——
  若之後想讓 steward 記住「上次收斂到哪」，這是唯一原生解。
* **`/doctor`**：CLAUDE.md 過大時會提議精簡（v2.1.206+）。
* **`claudeMdExcludes`**、`Read` deny 規則、`worktree.sparsePaths`：<https://code.claude.com/docs/en/large-codebases>
* **GitHub Action `anthropics/claude-code-action@v1`**：automation 模式可用 `prompt` 輸入在 **cron** 上跑，
  可指定 `plugin_marketplaces`／`plugins`，也可直接叫一個 skill。**這就是定期健檢的排程器，不用自己寫。**
  代價：需要 `ANTHROPIC_API_KEY` 或 `CLAUDE_CODE_OAUTH_TOKEN`（Pro/Max/Team/Enterprise）；
  排程若被歸屬到 bot 帳號會被擋（要列進 `allowed_bots`）；public repo 閒置 60 天會自動停用排程。
* ⚠️ **`/cost` 已不存在，現在是 `/usage`**——不要圍繞 `/cost` 做工具。
* ⚠️ Agent teams 需要 `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`，token 成本約 7 倍。

### 社群清單

* **`hesreallyhim/awesome-claude-code`**（5.3 萬星、活躍）— 這領域的權威清單。已驗證其中符合需求的項目：
  `anthropics/claude-code-action`（職責 4）、`Barnett-Studios/cxpak`（職責 2）、
  `costajohnt/oss-autopilot`（跨 repo PR 追蹤，職責 1）、`disler/fusion-harness`（多 agent，職責 1）。
* **`Barnett-Studios/cxpak`** — Rust＋tree-sitter 支援 43 種語言、型別依賴圖、死碼偵測、MCP/LSP/HTTP server。
  **只有 27 星**，單一組織的小專案，**要用先評估**；且本 repo 是 markdown，AST 索引效益不大。

## 三、未驗證線索（**不要照這份 clone**）

下列只出現在搜尋結果或他人清單中，**沒有實地開啟確認過**，要用之前必須自己先驗：

* `composio-community/awesome-claude-plugins`（repo 本身存在已確認，但其中列的
  `audit-project`、`documentation-generator`、`changelog-generator`、`codebase-graph`、`maestro-orchestrate`
  **未逐一驗證**）
* `ComposioHQ/awesome-claude-skills`、`travisvn/awesome-claude-skills`、
  `subinium/awesome-claude-code`、`quemsah/awesome-claude-plugins`

## 四、建議的導入順序

1. 先跑 `/doctor` 看官方怎麼建議精簡現有 CLAUDE.md。
2. 裝 `claude-md-management`，用它稽核一次 CLAUDE.md 與實際狀態的落差。
3. 評估把路由表遷到 `.claude/rules/`（**改動最大、收益也最大**，但會改變所有 session 的載入行為，
   要先跟 HackMD session 對齊再動）。
4. 加 `InstructionsLoaded` hook，蒐集「哪些 wiki 檔實際上從沒被載入」的實證，再據此裁掉孤兒檔。
5. 最後才考慮把定期健檢掛上 GitHub Action cron。
