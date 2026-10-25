---
name: resume-review-panel
description: >
  用「20 位虛構審查者（10 人資＋10 用人主管）＋50 份虛構同儕履歷」模擬台灣軟體業 PM 履歷的審查，
  找出使用者履歷的問題並排序。當使用者要「檢查履歷」「模擬 HR／主管怎麼看」「跟其他 PM 比」「這份履歷會不會被刷掉」時使用。
  只產出審查報告，不改履歷；改寫交給 resume-craft 並遵守 career/style/resume-voice-zh.md。
---

# 履歷審查模擬小組

> **在履歷工作流程中的位置**：`resume-craft` 九步流程的步驟 6（人資）與步驟 8（用人主管），中間是步驟 7 ATS 檢測（`resume-craft/references/workflow.md`），前置是步驟 5（去 AI 感）。順序 **人資 → ATS → 主管**；都過了才能進步驟 9 定版（`resume-craft/references/workflow.md`）。單獨使用時流程不變。報告需註明：審查者是同一模型扮演，不是真人意見；分數上升若來自補了清單要求的內容，要明寫。

> 狀態：2026-10-06 由 career session 建立草稿，使用者同日核可、主幹收錄到 `.claude/skills/`。
> **使用限制（先讀）**：
> 1. **素材只在個人線分支 `claude/happy-lamport-ljis8c`**（`career/review-panel/`、`career/wiki/`）。從 main 開的 session 看不到，要用請在該分支工作，或先 `git fetch` 後用 `git show` 唯讀讀取。
> 2. **只產審查報告，不改履歷**；寫入位置只限 `career/`（不是 career session 的 session 要寫報告，請先確認所在分支與目錄所有權，見 `wiki/personal_line_collab.md`）。
> 3. **審查結果是結構化的自我檢查，不是真人意見**（見文末〈可靠度〉）。


## 🗺️ 路由：要做什麼 → 只讀哪個檔（省 token，別整包讀）

| 任務 | 做法／讀什麼 | 不要讀 |
| :-- | :-- | :-- |
| **分流版驗證（2026-10-19 起預設；多職缺）** | ① 職缺分層表 `career/review-panel/jd/routing.tsv`（F 完整／L 輕量批次／X 略過，**一次分好、跨版沿用**；新職缺才加列）→ ② `python3 .claude/skills/resume-review-panel/scripts/build_routed_kit.py --version <版本> --resume career/drafts/<版本>/resume-<版本>.txt` 產生 `career/review-panel/handoff/<版本>/`（每檔＝一次呼叫的完整封包；`00-start-here.md` 有呼叫清單、模型分工、版本路由）→ ③ F 層派 Opus 子代理（每份讀一個 `F-*.md`）；L 層與錨點由使用者在外部模型跑 → ④ L 層回覆用 `scripts/light_report.py <raw.md…> --out …` 整理、F 層用 `schema_v4.py` | 舊單檔套件、`jd/a/`（僅歷史 run 用） |
| **Coach 讀後感（v4.3；定稿後盲審）** | 派 `Agent`（`model: opus`、`effort: low`）讀 `kit/coach-prompt.md`；規格 `rubric-v4.md` §10.1；四段 Markdown（15 秒 OS／ATS 概念對位／3–5 句張力與雜訊體檢／5 個深水區追問），**子代理不讀 `library/`、`causal_draft.md`** | 事實庫、歷史 runs |
| **跑一次驗證（最常用）** | ① `python3 .claude/skills/resume-review-panel/scripts/build_run.py --run career/review-panel/runs/<日期-名稱> --jd career/review-panel/jd/<職缺>.md --resume 標籤=路徑.txt …` 產全部提示＋`RUN.md` → ② 照 `RUN.md` 派子代理（指令一句話，**不要把提示貼進 Agent prompt**）→ ③ `scripts/run_report.py --run …` 自動出表 → ④ 只補結論 3 行 | rubric-v4.md 全文、兩份 registry JSON（程式會讀，不要進 context）、歷史 runs |
| 查某條規則／來源是什麼 | `career/review-panel/INDEX.md` 的對照 → 再 grep 該 ID 於 `rule-registry-v4.2.json`／`research-registry-v4.2.json` | 整份 JSON |
| 改規準 | `career/review-panel/rubric-v4.md` §9（v4.2 增補）＋規格原檔 `career/style/scoring-improvement-v4.2-source.md`（僅查特定節） | 舊 v3 |
| ATS 準備檢查 | `scripts/ats_check.py <pdf> <txt> --jd … --vendor …`；PDF 抽字 `scripts/parse_check.py` | — |
| 確定性迴歸 | `python3 tests/test_v4_rules.py`（20 項）；語義案例清單 `regression-v4.md` | — |
| **查歷史／某版結果／跨版缺口** | `career/review-panel/HISTORY.md`（先讀 §0–§1）；逐職缺矩陣 `opus-matrix.md`（`scripts/history_matrix.py` 產生） | 逐個 runs 資料夾翻 |
| 舊 v3 流程（20 persona、50 同儕、盲審分數） | `references-legacy-v3.md` | 預設不讀 |

**指令全表（2026-10-14 逐一實測過）**：`scripts/build_run.py`、`scripts/schema_v4.py validate|aggregate`、`scripts/run_report.py`、`scripts/ats_check.py`、`scripts/parse_check.py <pdf> <txt>`、`scripts/f_scan.py --view-only`（V 階段遮罩）、`scripts/ats_search.py`（搜尋實驗）、`scan.py <履歷.md>`（v3 舊工具，v4 起不再印分數）、`tests/test_v4_rules.py`。`render`／`mkpdf.js` 屬 resume-craft。

**子代理省 token 規則**：提示只放固定前綴＋一份履歷（前綴逐位元組相同才吃快取）；輸出單行 JSON 並有欄位上限；子代理只做「讀一個檔→一次 Bash 寫入並驗證」；換審查模型＝換條件，須記在 manifest／報告，不能跨條件比較。

## ⭐ 規準 v4.3（2026-10-25 起；v4.2 原則全數保留）

**v4.3 追加**（`rubric-v4.md` §10；規則 `rule-registry-v4.3.json`）：新增 HM14 AI 產品判斷與人機協作邊界；HM03 改為主動掃描策略張力；HM10／HR08 改為版面投資報酬率與訊號雜訊比；新增 coach 模式（深度讀後感，禁止只輸出 JSON 缺口表）。`build_run.py` 已改讀 v4.3 registry。

## 規準 v4.2（2026-10-14 起，取代下方 v3／v3.1／v3.2 的評分與彙整）

**v4.2 追加**（規格 `career/style/scoring-improvement-v4.2-source.md` §16–22；規準 `rubric-v4.md` §9）：ATS01–ATS14 用 `scripts/ats_check.py <pdf> <txt> --jd … [--vendor …]` 產五塊報告（不加總、不產生通用 ATS 分數、test_level=local_extraction）；用人主管十三問 HM01–HM13 進 A 審查的 `content_questions`，主管報告只列 ≤3 約談理由、≤3 關鍵缺口，語句微調放 editorial_appendix；不給 AI 作者機率；blocking 需 block_target。來源 A01–A50／M01–M50（`research-registry-v4.2.json`）、規則 `rule-registry-v4.2.json`。同模型新 context 不稱「另一模型」。


**v4.1 追加**：人資十二問 HR01–HR12（`career/review-panel/rule-registry-v4.2.json`，對應六維度、不另加總分）；50 筆來源登錄（`research-registry-v4.1.json`，S01–S30 沿用筆記未重開、S31–S50 本次查閱）；issue 需帶 rule_id／source_ids／application_note／context_limit，`hr_questions` 分開記 resume_evidence；來源不構成淘汰門檻。原檔 `career/style/scoring-improvement-v4.1-source.md`。

依使用者提供的修訂規格（`career/style/scoring-improvement-v4-source.md`）。完整規準：`career/review-panel/rubric-v4.md`；迴歸：`regression-v4.md`＋`tests/test_v4_rules.py`。

| 舊（v3.x） | 新（v4） |
| :-- | :-- |
| 20 persona 各 1–5 分取平均、6 份匿名混排、只審最長 3 份 | 每份**獨立**審查（新 context、同一 JD、同一深度）＋兩兩比較（甲乙順序交換）；HR／主管兩視角；20 persona 改為選用情境 |
| 15 筆職缺高頻詞＋20 種公司情境混成總分 | **一份目標 JD**（記錄擷取日期與 full／summary）；requirement matrix：supported／partial／unknown／contradicted／not_applicable |
| 1–5 分、Level 為主 | 六維度：強／足夠／待補／未呈現／不適用（不記零分、不加權）；招聘決定 interview／clarify_first／not_matched／insufficient_info；Level 次要 |
| 6 秒 F 型初篩、答錯一項＝不過 | **截斷文字可見性壓力測試**（內部代理規則），獨立請求、先存檔；unknown 不等於不合格 |
| 事實庫不給審查者，但事實核對與審查混在一起 | 事實核對獨立（可讀事實庫）；比較前用同一事實快照清理版本，原版保留 |
| B 關鍵字甜蜜區間、C／D 分數、禁用詞命中扣 Level | `resume_score.py stats`：只報證據對應與描述統計；style_lint（偏好）與 factual_guard（事實禁寫）分開 |
| 「差距小於波動不算進步」、對照組沒排預期就作廢 | 先列每輪決定、再列中位數與範圍；允許平手；對照組異常保留並做方法診斷；工具失敗標 technical_failure |
| ATS 搜尋排名 | 「指定語料與查詢下的搜尋實驗」，不代表商用 ATS；ATS import: not tested |

執行：產提示（見 `runs/2026-10-13-v4/raw/prompt-example-A.md`）→ 子代理各寫 JSON → `scripts/schema_v4.py validate`／`aggregate`。所有報告標 human_calibration: not_performed，不得寫「已證明優於同級」「真人會更喜歡」。

> 舊 v3 流程（驗證機制 v3、素材表、1–5 步流程、禁止、可靠度）已移到 `references-legacy-v3.md`。禁止事項不變：不改使用者履歷、不編造數字或經歷、不把 persona 說成真人、不拿同儕內容填補。
