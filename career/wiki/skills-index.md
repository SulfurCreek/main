<!--markdownlint-disable MD013-->

# 個人線 skill 索引與路由（Career Move 專用）

> 三個自有 skill（commit 前綴 `career(skill):`，擁有權在本分支）。**不要整包載入**：先看這張表，只讀「讀什麼」欄的檔案。
> 其他分支的 skill（1111 規格書、HackMD、線框圖…）與本線無關，見根目錄 `.claude_index.md`。

## 一、什麼任務用哪個 skill

| 任務 | skill | 入口 | 備註 |
| :-- | :-- | :-- | :-- |
| 寫／改履歷、自傳、求職信、作品集 case study、JD 客製 | `resume-craft` | SKILL.md 的〈任務路由〉表 | 先讀 `career/library/INDEX.md` 取事實 |
| 把 txt 履歷轉 PDF | `resume-craft` | `references/pdf-layout.md`；雙欄 `scripts/render_twocol.py`＋`scripts/mkpdf.js`；單欄見下方指令 | 雙欄只給人看，單欄給 ATS |
| 驗證履歷（模擬人資／主管、ATS 準備檢查、版本比較） | `resume-review-panel` | SKILL.md 的〈路由〉表 | 一鍵 `scripts/build_run.py` |
| 作品集渲染成靜態網站 | `portfolio-site` | SKILL.md §0 分層與邊界 | 只渲染不寫內容 |
| **寫任何對外履歷文字之前**（外部讀者看不懂、像工作報告、因果怪、披露檢查） | `resume-causal-logic-compiler` | `career/skills/resume-causal-logic-compiler/SKILL.md` | 強制門檻；驗收 T1–T6 |
| 104 特化版履歷 md／104 自我推薦信 | `104resume`／`104coverletter` | `career/skills/` | 先過上一列門檻 |
| 找事實、查使用者裁定 | （非 skill）`career/library/INDEX.md` | — | library 最優先 |
| 找驗證相關檔案／規則／來源 | （非 skill）`career/review-panel/INDEX.md` | — | — |
| **查驗證歷史、某版結果、跨版缺口、模型傾向** | （非 skill）`career/review-panel/HISTORY.md` | 先讀 §0–§1 | 每輪驗證後依 §9 更新 |

## 二、skill 檔案與大小（讀之前先看值不值得）

| skill | 檔案（KB） | 常讀 | 少讀 |
| :-- | :-- | :-- | :-- |
| resume-craft（116 KB） | SKILL.md 24、references/workflow 20、autobiography 9、reverse-xyz 7、portfolio 5、anti-ai-ats 5、ats-and-ai-screening 5、tw-voice 4、cover-letters 2、pdf-layout 2；assets 範本 5 份；scripts 3 支 | SKILL.md（核心＋路由）、tw-voice、anti-ai-ats | workflow（要走九步時才讀）、portfolio、reverse-xyz |
| resume-review-panel（~75 KB） | SKILL.md 7、references-legacy-v3 10、regression-v4 5；scripts 7 支；tests 1 支 | SKILL.md | references-legacy-v3（預設不讀） |
| portfolio-site（7 KB） | SKILL.md 7 | 全讀 | — |

## 三、驗證用指令一覽（皆在 repo 根目錄執行；2026-10-14 實測）

| 目的 | 指令 |
| :-- | :-- |
| 產提示＋執行單 | `python3 .claude/skills/resume-review-panel/scripts/build_run.py --run career/review-panel/runs/<日期-名稱> --jd career/review-panel/jd/gogolook-950oe.md --resume v9.4=career/drafts/v9.4/resume-v9.4.txt --resume v8.1c=career/drafts/v8.1c/resume-v8.1c.txt [--anon 標籤=路徑] --rounds 5 --anon-rounds 2 --b-rounds 4` |
| 子代理驗證輸出 | `python3 .claude/skills/resume-review-panel/scripts/schema_v4.py validate <raw/X.json>` |
| 彙整出報告草稿 | `python3 .claude/skills/resume-review-panel/scripts/run_report.py --run <runs/…>` |
| 更新逐職缺跨版矩陣 | `python3 .claude/skills/resume-review-panel/scripts/history_matrix.py` |
| ATS 準備檢查 | `python3 .claude/skills/resume-review-panel/scripts/ats_check.py <pdf> <txt> --jd "詞,詞" --vendor Greenhouse` |
| PDF 抽字還原 | `python3 .claude/skills/resume-review-panel/scripts/parse_check.py <pdf> <txt>` |
| 機械檢查（只報結果） | `python3 .claude/skills/resume-craft/scripts/resume_score.py stats <txt> --jd "…"` |
| 確定性迴歸 | `python3 .claude/skills/resume-review-panel/tests/test_v4_rules.py` |
| 雙欄 PDF | `python3 .claude/skills/resume-craft/scripts/render_twocol.py <txt> <html> [--location 台北市]` → `node .claude/skills/resume-craft/scripts/mkpdf.js <html 絕對路徑> <pdf>` |
| 單欄 PDF | `python3 .claude/skills/resume-craft/scripts/render_onecol.py <txt> <html>` → `node .claude/skills/resume-craft/scripts/mkpdf.js <html 絕對路徑> <pdf>` |

## 四、驗證省 token 的做法（2026-10-14）

1. 提示由腳本產生，**主代理不再手貼提示**；前綴固定（可吃快取），履歷放最後。
2. 前綴從約 18,000 字縮到約 5,900 字：規則只放「ID＋一句話＋source_ids」，來源不放標題。
3. 輸出有上限（requirements≤12、issues≤6、quote≤40 字、單行 JSON）。
4. 子代理只做兩步（讀檔→一次 Bash 寫入並驗證），指令一句話。
5. 報告表格由 `run_report.py` 算，主代理只寫 3 行結論。
6. 想再省：把審查子代理改用較小模型——**這是換條件**，要記在 manifest／報告，且不能與舊結果比較。

## 五、待辦／已知缺口

- 舊工具 `scan.py`（v3）仍在 skill 根目錄，v4 起不輸出分數；`--pool` 同儕模式仍有舊分數，僅供歷史比對。
