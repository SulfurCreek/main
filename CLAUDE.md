# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

---

## 🚀 動態檢索（RAG）— 依任務類型讀取對應 wiki 檔案

為了節省 context，平時只保留這份精簡路由表。當任務符合下列任一類型時，**先用 Read 讀取對應檔案**取得完整規則，再動手：

| 任務類型 | 讀取檔案 |
| --- | --- |
| 涉及 HackMD API 呼叫（建立／讀取／更新／刪除 note 或 folder） | `wiki/hackmd_rules.md` |
| 撰寫/修改 1111 規格書、需要求才系統業務代碼（`showfield`／`confirmed`／`oStatus` 等）、需先確認求才 vs 求職專案、**引用後端 API 契約（欄位／前端判斷／已讀未讀等）**、**任何 E.1 聯絡人才／信件即時通整併相關需求** | `wiki/recruitment_system_rules.md`（API 契約見 §3；**E.1／信件即時通整併素材與 inference 規則見 §6**，實體檔在 `notes/`、`notes/api/`） |
| 截圖存檔＋標註（Figma MCP 截圖、使用者上傳圖、badge／紅框／編號、存進 repo 供 HackMD 引用） | 用 `Skill` 載入 `photo`（`wiki/figma_rules.md` 已收斂為指標） |
| TCode 代碼表 Excel（`TCode_Export`、證照／工作技能／職務／福利代碼表的比對、異動清單、公告） | 用 `Skill` 載入 `tcode-excel-ops` |
| 需要**覆蓋改寫截圖裡既有文字**、維護舊版「截圖標號＝章節編號」規格書、或把整段說明輸出成單一 PNG | 用 `Skill` 載入 `png`（`photo` 的舊版備用流程，一般標註任務仍優先用 `photo`） |
| 需要產生 Figma 元件的完整文件（anatomy／design tokens／variants／a11y，非 1111 專屬） | 用 `Skill` 載入 `generate-component-doc-figma` |
| 手繪風 lo-fi wireframe／線框圖草稿 | 用 `Skill` 載入 `lofi-wireframer` |
| 1111 切版改版（mock↔正式偏離稽核、CSS 對照表）或前端修改工程單 | 用 `Skill` 載入 `frontend-slicing-1111`（改版稽核）／`frontend-change-ticket-1111`（工程單內文強制格式，兩者衝突時後者優先） |
| 分析 API 文件產測試矩陣、或依矩陣產生並執行 pytest | 用 `Skill` 載入 `api`（文件→矩陣）／`auto-test`（矩陣→腳本→報告，需先跑過 `api`） |
| 撰寫/修改個人履歷、CV、作品集 | 用 `Skill` 載入 `resume-craft`（依賴的 `career/` 職能框架 wiki 已於 2026-08-31 併入本 repo，開箱即用） |
| 數據分析報告寫作（MD 或靜態 HTML）、或濃縮成單張 PNG 摘要圖 | 用 `Skill` 載入 `report-generator`（報告本體）／`one-pager`（單張決策圖，出圖前需先給文字大綱確認） |
| 1111 職務分類／不合理清單專案（`plan()` 規則、`sync_md.py`、廠商身分 Google Sheet、AI 職類推薦模型分析） | 用 `Skill` 載入 `job-classification-kb`（知識庫入口）／`gsheet-vendor-identity`／`md-datalayer`／`safe-excel-editor`／`tabular-token-min`／`rawdata`——**與本 repo 主線（1111 聊天室文件）是不同專案**，僅供其他 session 共用 skill 庫 |
| 需要用專案縮寫/術語溝通、看不懂某個欄位名稱在講什麼 | `wiki/glossary.md` |
| 產出/修改 Mermaid 圖表（流程圖、循序圖等） | `wiki/mermaid_styling_rules.md`（§4 為循序圖專屬 frontmatter config，柔色系已裁定為準） |
| 需判斷該用本 repo 自製 skill 還是執行環境內建的官方 Anthropic skill（docx/pdf/internal-comms/doc-coauthoring 等） | `wiki/platform_skills_reference.md` |

規格書撰寫的格式細則（章節編號、MECE 狀態表、🚧 待補區塊模板等）由 `.claude/skills/spec-doc-1111/SKILL.md` 管理，用 `Skill` 工具載入，不在 wiki 裡重複。

> **本專案專屬的 skill 一律放在 `.claude/skills/`（進版控）**，完整清單見 `.claude_index.md`〈skills〉一節（2026-08-31 起本 repo 已成為跨分支的 skill 集散地，不只 1111 聊天室文件這條主線的 skill）。不要放在帳號層的雲端同步區（`~/.claude/skills/synced/`）——那裡只該有與專案無關的通用／官方 skill，兩邊同名會造成載到舊版。

涉及**數據分析／競品拆解／商業提案、跨部門溝通文案（公告/客服回覆/敏感溝通）、資料 Mapping Table 與資料庫正規化原則、OTP/MFA 類邊界條件檢查**時，用 `Skill` 工具載入 `.claude/skills/pm-toolkit/SKILL.md`（與 spec-doc-1111、mermaid_styling_rules.md 不重疊，僅收錄它們沒覆蓋的部分）。

---

## 🌿 分支索引（Branch Index）

**本 repo 有多支 Claude session 各自獨立開的分支，經常各自長出專屬 skill、彼此不知道對方存在。** 開始任何「新增 skill」「找有沒有人做過類似的事」類任務前，先掃一眼下表；找不到才動手，避免重工或跟其他分支撞名。

> 查最新狀態：`git fetch origin --prune && git branch -r`。下表為 2026-08-31 稽核快照（同日 PR 全面清理：#15 升格 main；#1/#2/#4/#7/#8/#14 已關閉；#11 已併入職務分類主線；#9/#10/#12/#13 留 open 屬各專案 deliverable）。之後有新分支或分支被合併/刪除，比對後更新本表。

| 分支 | 最後更新 | 主題 | 帶有的獨有 skill | 狀態 |
| :--- | :--- | :--- | :--- | :--- |
| `main`＝`claude/claude-md-docs-BmaVo`（主幹） | — | 1111 求才系統 HackMD 規格書主線＋全部 21 個 skill 的集散地 | 全部（見 `.claude_index.md`〈skills〉） | 2026-08-31 起 main 為唯一主幹（PR #15），兩者同步演進 |
| `claude/gifted-meitner-6eSoK` | 2026-08-26 | photo/png skill 改進（Figma 座標來源、跨區塊視覺比對） | （`photo`／`png` 已選擇性併入本分支，見下方） | 已部分吸收（PR #1 已關閉留言），其餘核心文件版本較舊不採用；`mermaid-sequence-diagram` 已裁定採柔色系，機制併入 `wiki/mermaid_styling_rules.md` §4，skill 本身不獨立收錄 |
| `claude/lofi-wireframer-skill-0u25rk` | 2026-08-21 | Balsamiq 風格 HTML 手繪線框圖 skill；**分岔點是本分支自己的近期 commit**（`0fc94c3`），血緣最近 | `lofi-wireframer` | ✅ 已併入；PR #14 已關閉留言 |
| `claude/google-sheet-url-allowlist-GKFEU` | 2026-08-27 | 職務分類資料工作流；最後一筆是 TCode 福利代碼顯示順序對照表 | `gsheet-vendor-identity`／`job-classification-kb`／`md-datalayer`／`safe-excel-editor`／`tabular-token-min` | ✅ 2026-08-31 skill 已併入（與 `tcode-excel-ops` 無重疊，各管不同代碼表體系）；同日複查：`pm-toolkit`／`spec-doc-1111` 均與本分支相同或較舊，`.claude/settings.json` 的 Google Sheets/Docs WebFetch allowlist 已一併搬入（否則併入的兩個 skill 會因權限擋住無法用）；`job-classification-kb/` 資料目錄本體（scripts／tcode／wiki 等大量專案資料）維持不搬。PR #2 已關閉留言；**#11 已併入本分支**，職務分類專案自此收斂為這一支主線 |
| `claude/extract-job-duty-markdown-4avmd6` | 2026-08-03 | 職務分類資料工作流（大量資料檔，200萬行級 diff） | `report-generator`／`rawdata`／`one-pager`／同上 job-classification 系列 | 整支分支 ❌ 不合併（規模/資料檔跟本 repo 無關）；2026-08-31 已抽出 `report-generator`／`rawdata`／`one-pager` 三個 skill 併入；同日複查：`job-classification-kb/skills/tcode-excel-ops.md` 是該專案內部文件（非 `.claude/skills/`），跟本 repo 的 `tcode-excel-ops` skill 同名但服務不同代碼表體系，維持不搬，避免混淆。其 PR #11（對 google-sheet 分支）已合併，該專案後續以 google-sheet 分支為主線 |
| `claude/vm-api-testing-setup-wpf6y8` | 2026-08-03 | API 測試/VM 環境設置，含呼叫紀錄 | `api`／`auto-test` | ✅ 2026-08-31 已併入；同日複查：`pm-toolkit`／`spec-doc-1111` 逐位元組與本分支相同，`wiki/apis/` 下的 API 測試working data（talent-search-api／talent-sourcing-gateway-api 的 spec/報告/pytest）維持不搬，屬該分支專屬工作產出。PR #12 留 open（專案 deliverable 不進主幹），已留言說明政策 |
| `claude/part-time-modal-design-tmtt7n` | 2026-07-28 | 兼職相關 modal 設計調整 | 無獨有 skill | 功能分支非 skill 分支；PR #13 留 open（專案 deliverable 不進主幹），已留言說明政策 |
| `claude/happy-lamport-ljis8c` | 2026-07-26 | Context/token 精簡；含履歷撰寫、HackMD API skill 化 | `hackmd-api`／`resume-craft` | 部分評估：`resume-craft` 2026-08-31 已併入；`hackmd-api` 逐節比對後與 `wiki/hackmd_rules.md` 幾乎全同，唯一新資訊已補進 wiki，原檔改放空殼重導向；`career/` 職能框架（resume-craft 依賴）已於 2026-08-31 經使用者核准併入。此分支的 `spec-doc-1111` 是**精簡改寫版**（176 行 vs 本分支 387 行，不同檔名結構），未採用但值得之後參考其瘦身思路。PR #7 已關閉留言（career/ 已併入） |
| `claude/email-layout-handoff-gjq5zu` | 2026-07-03 | 信件訊息頁前端修改工程單 | `frontend-change-ticket-1111`／`frontend-slicing-1111` | ✅ 2026-08-31 已併入（`frontend-slicing-1111` 取本分支版本，比 `eloquent-maxwell-j31ot5` 的舊版新）；同日複查：`spec-doc-1111` headers 逐項比對後與本分支完全相同（只是本分支拆進 `references/` 子目錄）；`wiki/frontend_change_ticket_rules.md` 只是指向 `frontend-change-ticket-1111` skill 的路由指標，內容已被 CLAUDE.md 路由表涵蓋，不重複搬入；`handoff/` 下的切版 before/after 資產維持不搬。PR #9 留 open（專案 deliverable 不進主幹）、PR #8（舊版 mockup）已關閉留言 |
| `claude/csv-retrieval-retry-do5a9o` | 2026-07-13 | CSV 資料重試邏輯；`report-generator` skill 的另一個獨立來源 | `report-generator` | 內容與 `extract-job-duty-markdown-4avmd6` 版本逐位元組相同，已從該分支併入。PR #10 留 open（專案 deliverable 不進主幹），已留言說明政策 |
| `claude/eloquent-maxwell-j31ot5` | 2026-06-29 | 前端切版交接；session 交接 INDEX.md 慣例 | `frontend-slicing-1111` | 舊版（06/29），已被 `email-layout-handoff-gjq5zu` 的新版取代並併入，這支不用再看 |
| `claude/static-html-github-deploy-1h0w1c` | 2026-06-15 | GitHub Pages 靜態部署設定，僅 18 檔 | 無 | EPK 頁面在 main 已 merge 過又 revert（#5→#6）；PR #4 已關閉留言，此分支結案 |

**已知重複造輪**：`report-generator` 至少有兩支分支各自產出一份（`csv-retrieval-retry-do5a9o`、`extract-job-duty-markdown-4avmd6`）；`frontend-slicing-1111` 也出現在兩支（`eloquent-maxwell-j31ot5`、`email-layout-handoff-gjq5zu`）。挑選要不要併入時，同名 skill 要先比對哪一份較新/較完整，不要兩份都拿。

**併入既有先例**：`png`／`generate-component-doc-figma`／`wiki/master_prompt.md`（選擇性從 `gifted-meitner-6eSoK` 併入）；2026-08-31 批次再從 6 支分支選擇性抽出 `lofi-wireframer`／`frontend-slicing-1111`／`frontend-change-ticket-1111`／`api`／`auto-test`／`resume-craft`／`report-generator`／`one-pager`／`rawdata`／`gsheet-vendor-identity`／`job-classification-kb`／`md-datalayer`／`safe-excel-editor`／`tabular-token-min`（完整清單與各自取捨理由見 `.claude_index.md`〈2026-08-31 分支整併批次〉）。決策與取捨記錄在該次的 commit message 裡，之後選擇性併入其他分支時比照辦理——只搬跟本 repo 主題相關、且不會覆蓋掉本分支已驗證內容的部分，整支 `git merge` 一律先評估分岔規模再決定，不要預設用。

> **`main` 已於 2026-08-31 升格為唯一主幹（PR #15）**：文件主線＋全部 skill 的集散地，`claude/claude-md-docs-BmaVo` 與 main 同步演進。其他 session 需要用哪個 skill，直接從最新 `main` 拿，不要各自維護一份。已知未併入、待裁示的項目：`.claude/skills/hackmd-api/`（已逐節比對，內容併入 `wiki/hackmd_rules.md`，原路徑改放空殼重導向 SKILL.md，不要恢復完整版本）、`.claude/skills/mermaid-sequence-diagram/`（配色系統跟現有 `wiki/mermaid_styling_rules.md` 衝突，**已裁定採柔色系**：配色不採用，非配色機制併入 `wiki/mermaid_styling_rules.md` §4，該 skill 不獨立收錄）。

---

## 🧭 多 session 治理規則（2026-08-31 起生效）

多支 session 平行工作造成品質漂移的根因是「從古老 commit 分岔、帶著舊規則與舊 skill 繼續產出」（實例：`gifted-meitner` 分岔後仍用已棄用的 GitHub-raw 圖床）。自 `main` 升格為唯一主幹起，一律遵守：

1. **新 session 一律從最新 `main` 開分支**。開工第一件事 `git fetch origin main` 確認基準點，繼承最新路由表＋全部 skill。
2. **共用資產唯一變更入口＝主幹管理 session**：`CLAUDE.md`／`.claude/skills/`／`wiki/`／`scripts/`／`.claude_index.md`／`.claude/settings.json` 只由主幹管理 session 修改。其他 session 需要改共用檔時，在自己的 PR 描述註明「請主幹對照吸收」，**不要直接改**——直接改必然跟主幹撞衝突，且會被主幹版本覆蓋。
3. **各專案工作產出放各自目錄**（`job-classification-kb/`、`wiki/apis/`、`handoff/`、`notes/`…），不碰共用檔，PR 就不會互撞。專案 deliverable **不進主幹**，留在各自分支（位置記錄於分支索引）；主幹只收文件主線＋skill。
4. **新增 skill 前先查分支索引＋`.claude_index.md`**——重複造輪已發生兩例（`report-generator`×2、`frontend-slicing-1111`×2）。真的要新增，通知主幹 session 統一納管。
5. **PR 送出前先 rebase 最新 `main`**；一個 PR 一個主題。

---

## 🧠 Token 最佳化與全局索引

處理大量規格書／長文／代碼時，嚴守以下「上下文壓縮」規範：

- **全局索引**：根目錄 `.claude_index.md` 是輕量索引（檔名＋一句話摘要）。要找檔案先查它，不要靠記憶或全文掃描整個 repo；新增/搬移重要檔案時順手更新它。
- **靜態參照（拒絕重複生成）**：套用核心規則／業務代碼／設計變數時，直接讀對應指標檔，**禁止**在對話中重複貼出已知規則全文或大段原始碼——改用「檔名＋指標」引用。需要時才動態加載子文件，處理完即從工作記憶釋放，保持 context 乾淨。
- **輸出極簡**：預設極短。
  - **結論先行**：第一句就是答案／結果，不要鋪陳。
  - **砍掉包裝**：不寫開場白（「以下是…」「我來幫你…」）、不寫結尾總結、不寫客套話；理解指令後回「ACK」或一行進度即可。
  - **不覆述**：不複述題目、不逐步敘述自己的思考過程或工具操作流水帳；**除非使用者明確要求詳細說明**。
  - **格式看價值**：預設用白話短句；**只有在 Markdown（標題／表格／清單）真的能承載結構時才用**——流程、狀態、欄位對照、多項比對用表格或 Mermaid，其餘不要為了排版而排版。
- **截圖標註**：一律用「HTML 絕對定位覆蓋」或「Markdown 標號對照表」＋預覽網址掛圖，**禁止使用或提及任何外部 AI 圖像生成模型**渲染畫面。
- **記憶垃圾回收**：單次任務完成後，總結 1–3 條核心變更寫入版控表／專案日誌，並提示使用者可開新對話視窗（New Chat）重置 Token 累積量。
- **跨文件比對**：比對多份文件（新舊代碼表、API 規格差異）時，欄位定義與狀態描述要逐一對齊；**資料缺失就標 `NULL`，不要自行推測補齊**。
- **Excel/CSV 走 pandas 漸進式分析**：不要把原始資料整份讀進 context。先用 Python 讀結構（`df.info()`）與極簡預覽 → 在 Python 環境內完成 JOIN／翻譯／交叉比對 → 對話裡只輸出最終統計表格或洞察結論，不印 raw data。

---

## 常用速查（不需要查 wiki 就能用）

**HackMD 團隊**：team path `1111-jobdocs`（`https://hackmd.io/team/1111-jobdocs?nav=overview`）

**Auth 快速測試**：
```bash
curl "https://api.hackmd.io/v1/me" -H "Authorization: Bearer $HACKMD_TOKEN"
```
Token 存在環境變數 `HACKMD_TOKEN`，`.env` 已列入 `.gitignore`，絕不寫死在程式碼或文件裡。

**改既有 HackMD note 一律走安全回寫**（防蓋掉小聶的手動編輯）：先落地 baseline → 本地改 working → 用腳本回寫，遠端在期間被改過會 exit 1 中止、不盲蓋。
```bash
python3 scripts/hackmd_safe_patch.py --note-id <內部 noteId> \
  --baseline "$SCRATCHPAD/<noteId>.md" --working "$SCRATCHPAD/<noteId>.working.md" \
  --team-path 1111-jobdocs   # exit: 0 已更新／1 衝突／2 錯誤
```

**動到 Mermaid 就要渲染驗證**再 push（HackMD 上壞圖不會報錯，只會渲染失敗）：
```bash
npx -y @mermaid-js/mermaid-cli -p <puppeteer-cfg> -i x.mmd -o x.png
# puppeteer cfg: {"executablePath":"/opt/pw-browsers/chromium","args":["--no-sandbox"]}
```
