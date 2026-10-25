<!--markdownlint-disable MD013-->

# review-panel 索引（驗證相關檔案地圖；別整包讀）

| 要找什麼 | 檔案 | 怎麼讀 |
| :-- | :-- | :-- |
| **歷史／比較／某版驗證結果／缺口追蹤（先看這份）** | **`HISTORY.md`**（路由＋版本表＋三模型並列＋缺口追蹤）、`runs/INDEX.tsv`（一列一 run）、`opus-matrix.md`（逐職缺跨版，腳本產生） | 先讀 HISTORY §0–§1，其餘按需 |
| 跑一次驗證 | skill `resume-review-panel` 的〈路由〉 | 照 `build_run.py → RUN.md → run_report.py` |
| 規準全文（原則、六維度、HR、V/A/B 提示、JSON、§9 v4.2 增補） | `rubric-v4.md`（17 KB） | 只改規準時讀；跑驗證不用讀（提示已由 build_run.py 內建精簡版） |
| 規則 ID→問題→來源 | `rule-registry-v4.3.json`（HR01–12、ATS01–14、HM01–14；唯一現行規則庫；v4.2 檔保留供歷史 run） | `grep '"HM05"'` 單條查 |
| 來源 ID→標題→限制 | `research-registry-v4.1.json`（S01–S50）、`research-registry-v4.2.json`（A01–A50、M01–M50） | `grep` 單條查；**不要整份讀（30 KB／58 KB）** |
| 目標職缺 | `jd/gogolook-950oe.md`（800 字，summary 輸入） | build_run.py 的 `--jd` |
| 歷次結果 | `runs/<日期>/report.md`（每次一份結論＋表）；原始 JSON 在 `raw/` | 只讀 report.md；raw 只在查特定輪時用 |
| 規格原檔（使用者提供） | `../style/scoring-improvement-v4{,.1,.2}-source.md` | 只查特定節（`grep -n '^## '`） |
| 舊 v3 材料 | `reviewers/`、`candidates/`（50 份同儕）、`research*.md`、`blind-output-v3.1.md` | 預設不讀；僅舊流程或同儕比較 |

## runs 對照

| 目錄 | 內容 |
| :-- | :-- |
| `2026-10-13-v4` / `-v4.1` | v9.4 vs v8.1c，規準 v4／v4.1（平手，皆建議面試） |
| `2026-10-14-v4.2` | 規準 v4.2：皆建議面試；直接比較 v8.1c 3:1（順序敏感）；`report.md` |
| 更早 | v3.x 舊分數，**跨規準不可比** |

## runs 補充（2026-10-18）

v9.7 起每版有兩個資料夾：`<日期>-<版本>-a15-opus/`（Opus 15 輪）與 `<日期>-<版本>-consolidated/`（三家統整＋外部原始報告）。完整清單與結論見 `HISTORY.md` §4、`runs/INDEX.tsv`。
