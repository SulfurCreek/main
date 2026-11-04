# 任務路由表（2026-11-04 精簡版）

| 任務類型 | 必讀指南與來源 | 核心原則 |
| :-- | :-- | :-- |
| **新增工作事實／數據** | `career/library/README.md`、`facts-1111.md`、`facts-prior.md` | 直接記錄原始事實與數據，不寫驗證腳本。 |
| **撰寫／改寫中文履歷（v13 雙欄 PDF／104）** | `career/CLAUDE.md`、`career/drafts/v13/00-writing-guide.md` | 全力發揮高階人才行銷張力；改單點必重讀該公司完整經歷。 |
| **撰寫／改寫英文履歷（LINE／外商 CV）** | `career/style/voice-en.md` | 道地美式科技業 Senior PM 語感，2 頁上限，不放自傳，不跑機械鎖定檢查。 |
| **撰寫 104 自我推薦信** | `career/scripts/gen_cover_drafts.py` | 針對目標公司業務痛點精準出牌，標題乾淨、破題吸睛。 |


---

# 附錄｜檔案地圖（2026-11-04 本人指示保留）

## 我要做什麼 → 讀哪裡

| 任務 | 必讀（依序） | 視需要 |
| :-- | :-- | :-- |
| **任何動筆前** | [`library/INDEX.md`](library/INDEX.md) → [`library/decisions.md`](library/decisions.md) §1–§4 | [`library/superseded.md`](library/superseded.md)（改舊稿、審稿） |
| 查「某個事實現在怎麼說」 | [`library/fact-snapshot-2026-10-13.md`](library/fact-snapshot-2026-10-13.md) | [`library/facts-1111.md`](library/facts-1111.md)、[`library/facts-prior.md`](library/facts-prior.md)、[`library/profile.md`](library/profile.md) |
| 寫／潤英文（履歷、推薦信英文條列） | [`style/voice-en.md`](style/voice-en.md) | `style/anti-ai-ats.md` |
| 寫／潤中文履歷 | 現行稿（見下方）＋ [`style/resume-voice-zh.md`](style/resume-voice-zh.md) ＋ [`library/decisions.md`](library/decisions.md) | [`style/anti-ai-ats.md`](style/anti-ai-ats.md) |
| 求職信、故事素材 | [`letters/README.md`](letters/README.md)、[`letters/story-bank.md`](letters/story-bank.md) | [`letters/log.md`](letters/log.md) |
| 104 履歷欄位 | [`104/README.md`](104/README.md) → [`104/fields-spec.md`](104/fields-spec.md) → [`104/content-spec-quill.md`](104/content-spec-quill.md)（Quill HTML 與各欄撰寫規格；範例只取格式） | [`104/resume-104.md`](104/resume-104.md)、[`104/chrome-playbook.md`](104/chrome-playbook.md) |
| 作品集／case study | [`portfolio/`](portfolio/)（內部版）、`portfolio/public/`（對外版） | [`site/`](site/)（網站助手專屬） |
| 投遞紀錄（職缺 × 推薦信 × 履歷版本） | [`applications/INDEX.md`](applications/INDEX.md)，每職缺一檔 `applications/<code>.md` | 推薦信產生流程見 `.claude/skills/104coverletter/SKILL.md` §5 |
| 職缺與公司資料 | [`targets/README.md`](targets/README.md)、`targets/jobs.md`、`targets/companies.md` | [`review-panel/jd/routing.tsv`](review-panel/jd/routing.tsv)（每份職缺的分層） |
| 遇到〔待補〕或想問使用者 | [`library/open-questions.md`](library/open-questions.md)（問前先查） | Codex 的疑問寫 `drafts/codex/QUESTIONS.md` |
| Resume Gen 原 ChatGPT 交接、歷史稿／PDF／對話追溯 | Codex 分類 wiki：`drafts/codex/wiki/README.md` | 逐檔索引：`drafts/codex/FILE_INDEX.md`、雜湊清單 `drafts/codex/FILE_INDEX.csv` |
| 104 個人簡介與頂部個人特色規格 | `104/content-spec-quill.md` §5 | Codex 交接 `drafts/codex/2026-10-21-104-summary-chips-claude-handoff.md`（在 `codex/resume-writer`） |
| Codex 內容編輯協作與交付 | Resume Writer 指令：`drafts/codex/AGENTS.md` | 接手核對 `drafts/codex/2026-10-20-conversation-reconciliation.md`、`drafts/codex/QUESTIONS.md` |
| 產生 104 特化版履歷 md | [`.claude/skills/104resume/SKILL.md`](../.claude/skills/104resume/SKILL.md) | `104/content-spec-quill.md` |
| 寫 104 自我推薦信（指定職缺） | [`.claude/skills/104coverletter/SKILL.md`](../.claude/skills/104coverletter/SKILL.md) | `104/cover-letter-research.md`、`letters/104/` |
| 潤飾 104 特化版草稿（Codex） | [`codex-skills/polish-104/SKILL.md`](codex-skills/polish-104/SKILL.md) | `drafts/v11/104-v11.md` |
| 職能證據（F1–F15） | [`competency-framework.md`](competency-framework.md) → `wiki/F*.md`、`wiki/evidence-*.md` | — |


## 現行稿

| 項目 | 位置 |
| :-- | :-- |
| **現行 PM 線（訂閱／支付）** | `drafts/v13/聶崑淮_資深產品經理_v13-PM.pdf`（文字 `drafts/v13/final_resume_v13_pm.source.md`；上游 `01_claude_stage/v13-pm-draft.md`） |
| 現行 104 線上版 | `drafts/v12.20/104-v12.20.md`（v13 PO 線待做） |
| 歷史稿 | `drafts/v7` … `drafts/v12.20` |
| Codex 產出 | `codex/resume-writer` 分支 `career/02_codex_stage/`、`career/drafts/codex/` |

## 目錄速查

| 目錄／檔 | 內容 | 誰寫 |
| :-- | :-- | :-- |
| `library/`（＝00_library） | 使用者確認過的現行事實與裁定（**事實唯一來源**） | Career Move |
| `02_codex_stage/` | Codex 潤飾稿與語氣參數（在 `codex/resume-writer`） | Resume Writer（Codex）；Claude 只讀 |
| `style/` | 語氣、去 AI 感、ATS 規則與來源 | Career Move |
| `wiki/` | 職能 F1–F15 與證據細節（可能含舊層，與 library 衝突以 library 為準） | Career Move |
| `drafts/` | 各版履歷與中間產物 | Career Move（`codex/` 除外） |
| `letters/` | 求職信、故事庫 | Career Move |
| `104/` | 104 欄位規格與逐欄內容 | Career Move |
| `portfolio/` | 作品集內部版＋對外版 | Career Move |
| `site/` | 作品集網站 | 作品集網站助手 |
| `targets/` | 職缺與公司資料 | Career Move |
| `review-panel/` | 驗證規則、職缺分流、各次驗證結果 | Career Move |
| `career-ops/` | 求職流程工具與 pipeline | Career Move |
| `_requests-to-main.md` | 需要主幹施作的請求 | Career Move |

| `01_claude_stage/` | Claude 上游行銷草稿（例：`v13-pm-draft.md`） | Claude |

## 快速搜尋

| 想找 | 指令（在 repo 根目錄） |
| :-- | :-- |
| 某個數字或說法出現在哪 | `grep -rn "關鍵字" career/library career/wiki` |
| 某個說法是否已被推翻 | `grep -n "關鍵字" career/library/superseded.md` |
| 某職缺的分層與公司 | `grep "代碼" career/review-panel/jd/routing.tsv` |
| 現行稿某段文字 | `grep -n "關鍵字" career/drafts/v11/resume-v11.md` |
