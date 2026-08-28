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
| 需要用專案縮寫/術語溝通、看不懂某個欄位名稱在講什麼 | `wiki/glossary.md` |
| 產出/修改 Mermaid 圖表（流程圖、循序圖等） | `wiki/mermaid_styling_rules.md` |
| 需判斷該用本 repo 自製 skill 還是執行環境內建的官方 Anthropic skill（docx/pdf/internal-comms/doc-coauthoring 等） | `wiki/platform_skills_reference.md` |

規格書撰寫的格式細則（章節編號、MECE 狀態表、🚧 待補區塊模板等）由 `.claude/skills/spec-doc-1111/SKILL.md` 管理，用 `Skill` 工具載入，不在 wiki 裡重複。

> **本專案專屬的 skill 一律放在 `.claude/skills/`（進版控）**：`spec-doc-1111`、`pm-toolkit`、`photo`、`tcode-excel-ops`。不要放在帳號層的雲端同步區（`~/.claude/skills/synced/`）——那裡只該有與專案無關的通用／官方 skill，兩邊同名會造成載到舊版。

涉及**數據分析／競品拆解／商業提案、跨部門溝通文案（公告/客服回覆/敏感溝通）、資料 Mapping Table 與資料庫正規化原則、OTP/MFA 類邊界條件檢查**時，用 `Skill` 工具載入 `.claude/skills/pm-toolkit/SKILL.md`（與 spec-doc-1111、mermaid_styling_rules.md 不重疊，僅收錄它們沒覆蓋的部分）。

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
