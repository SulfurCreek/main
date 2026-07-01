# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

---

## 🚀 動態檢索（RAG）— 依任務類型讀取對應 wiki 檔案

為了節省 context，平時只保留這份精簡路由表。當任務符合下列任一類型時，**先用 Read 讀取對應檔案**取得完整規則，再動手：

| 任務類型 | 讀取檔案 |
| --- | --- |
| 涉及 HackMD API 呼叫（建立／讀取／更新／刪除 note 或 folder） | `wiki/hackmd_rules.md` |
| 撰寫/修改 1111 規格書、需要求才系統業務代碼（`showfield`／`confirmed`／`oStatus` 等）、需先確認求才 vs 求職專案 | `wiki/recruitment_system_rules.md` |
| 涉及 Figma 畫面規格擷取、Figma → HackMD 轉換 | `wiki/figma_rules.md` |
| 需要用專案縮寫/術語溝通、看不懂某個欄位名稱在講什麼 | `wiki/glossary.md` |
| 產出/修改 Mermaid 圖表（流程圖、循序圖等） | `wiki/mermaid_styling_rules.md` |
| 需判斷該用本 repo 自製 skill 還是執行環境內建的官方 Anthropic skill（docx/pdf/internal-comms/doc-coauthoring 等） | `wiki/platform_skills_reference.md` |

規格書撰寫的格式細則（章節編號、MECE 狀態表、🚧 待補區塊模板等）由 `.claude/skills/spec-doc-1111/SKILL.md` 管理，用 `Skill` 工具載入，不在 wiki 裡重複。

涉及**數據分析／競品拆解／商業提案、跨部門溝通文案（公告/客服回覆/敏感溝通）、資料 Mapping Table 與資料庫正規化原則、OTP/MFA 類邊界條件檢查**時，用 `Skill` 工具載入 `.claude/skills/pm-toolkit/SKILL.md`（與 spec-doc-1111、mermaid_styling_rules.md 不重疊，僅收錄它們沒覆蓋的部分）。

涉及**前端切版／視覺改版（拿到被調整過的頁面 mock HTML/CSS、逐一盤點樣式更動、依 Figma 設計稿微調樣式、把改動整理成給人類前端工程師的需求文件、比對 mock 與正式環境 HTML 結構差異、產自包含預覽）**時，用 `Skill` 工具載入 `.claude/skills/frontend-slicing-1111/SKILL.md`（封裝「只改 CSS 不動結構、mock↔正式偏離稽核、自包含預覽、微軟正黑體字體規則、求才白話需求文件」這套做法；需求文件的 HackMD 排版格式仍搭 spec-doc-1111）。「信件訊息」頁（`ResumePoolNoticeMail`）的實際交接包見 `handoff/INDEX.md`。

---

## 規格書 UI 截圖標號慣例

規格書／需求文件的畫面截圖，要在圖上標「區塊編號」badge，編號與文件章節一致，方便 RD/QA 對照畫面。**一律以 Pillow 在截圖上程式化標注／覆蓋文字**，不要手動修圖：

- **badge 樣式（固定）**：紅底 `#FF5F57`、白字 `Inter`／`700`／`20px`、圓角；打在截圖**上緣加出的白色留白**上，**不壓到畫面內容**。
- **流程**：取圖（Figma `get_screenshot` 或現成截圖）→（URL 來源用 `curl` 下載）→ Pillow 加白邊＋打 badge → 裁切 → commit 到 `.claude/assets/` → 文件用 `https://raw.githubusercontent.com/<owner>/<repo>/<SHA>/.claude/assets/<file>`（URL 帶 commit SHA）引用，`<img>` 加 `alt`。
- 完整步驟與 Pillow 範例碼見 `.claude/skills/spec-doc-1111/SKILL.md` 的「截圖標注／覆蓋」一節。

---

## 🧠 Token 最佳化與全局索引

處理大量規格書／長文／代碼時，嚴守以下「上下文壓縮」規範：

- **全局索引**：根目錄 `.claude_index.md` 是輕量索引（檔名＋一句話摘要）。要找檔案先查它，不要靠記憶或全文掃描整個 repo；新增/搬移重要檔案時順手更新它。
- **靜態參照（拒絕重複生成）**：套用核心規則／業務代碼／設計變數時，直接讀對應指標檔，**禁止**在對話中重複貼出已知規則全文或大段原始碼——改用「檔名＋指標」引用。需要時才動態加載子文件，處理完即從工作記憶釋放，保持 context 乾淨。
- **輸出極簡**：理解指令後回「ACK」或簡短進度即可，不寫冗長客套；規劃流程／邏輯優先用 Markdown 表格或 Mermaid，避免長段散文。截圖標註一律用「HTML 絕對定位覆蓋」或「Markdown 標號對照表」＋預覽網址掛圖，**禁止使用或提及任何外部 AI 圖像生成模型**渲染畫面。
- **記憶垃圾回收**：單次任務完成後，總結 1–3 條核心變更寫入版控表／專案日誌，並提示使用者可開新對話視窗（New Chat）重置 Token 累積量。
- **範本警語**：此能力範本中的範例（`oTag` 狀態表、`rNo` 無後綴鐵律、`figma_tokens.json`／`bg-primary` 等）只是格式示範，**非本專案實況**；索引與文件一律記真實檔案與規則，不杜撰。

---

## 常用速查（不需要查 wiki 就能用）

**HackMD 團隊**：team path `1111-jobdocs`（`https://hackmd.io/team/1111-jobdocs?nav=overview`）

**Auth 快速測試**：
```bash
curl "https://api.hackmd.io/v1/me" -H "Authorization: Bearer $HACKMD_TOKEN"
```
Token 存在環境變數 `HACKMD_TOKEN`，`.env` 已列入 `.gitignore`，絕不寫死在程式碼或文件裡。
