<!--markdownlint-disable MD013-->

# career 路由表（Career Move 與 Resume Writer 共用）

> 目的：不用掃資料夾就知道檔案在哪、該讀什麼。交接與歷史見 [`HANDOFF.md`](HANDOFF.md)；規則見 [`CLAUDE.md`](CLAUDE.md)。
> 維護：Career Move（Claude）維護本檔；新增或搬動重要檔案時同步更新。Resume Writer（Codex）只讀。
> Codex 的檔案只在 `origin/codex/resume-writer` 分支；Career Move 讀取用 `git show origin/codex/resume-writer:career/drafts/codex/<檔>`。
> ⚠️ 個人職涯資料，不外流 HackMD；對外版本須抽象化公司內部名稱與數字。

## 1. 先看：誰能寫哪裡

| 角色 | 可寫 | 唯讀 |
| :-- | :-- | :-- |
| Career Move（Claude，分支 `claude/happy-lamport-ljis8c`） | `career/` 全部（**除** `drafts/codex/`）＋自有 skill | repo 其他 |
| Resume Writer（Codex，分支 `codex/resume-writer`） | 只有 `career/drafts/codex/` | `career/` 其餘全部 |

## 2. 我要做什麼 → 讀哪裡（最小集合）

| 任務 | 必讀（依序） | 視需要 |
| :-- | :-- | :-- |
| **任何對外文字動筆前（強制）** | [`skills/resume-causal-logic-compiler/SKILL.md`](skills/resume-causal-logic-compiler/SKILL.md) §2.3 披露與跨欄位檢查 | — |
| **任何動筆前** | [`library/INDEX.md`](library/INDEX.md) → [`library/decisions.md`](library/decisions.md) §1–§4 | [`library/superseded.md`](library/superseded.md)（改舊稿、審稿） |
| 查「某個事實現在怎麼說」 | [`library/fact-snapshot-2026-10-13.md`](library/fact-snapshot-2026-10-13.md) | [`library/facts-1111.md`](library/facts-1111.md)、[`library/facts-prior.md`](library/facts-prior.md)、[`library/profile.md`](library/profile.md) |
| 寫／潤英文（履歷、推薦信英文條列） | [`style/voice-en.md`](style/voice-en.md) | `style/anti-ai-ats.md` |
| 寫／潤中文履歷 | 現行稿（§3）＋ [`style/resume-voice-zh.md`](style/resume-voice-zh.md) ＋ [`library/decisions.md`](library/decisions.md) | [`style/anti-ai-ats.md`](style/anti-ai-ats.md) |
| 寫自傳、轉職動機 | [`library/about-me.md`](library/about-me.md)（**編輯參考，不可給驗證者**）＋ [`library/profile.md`](library/profile.md) §7 | `.claude/skills/resume-craft/references/autobiography.md` |
| 求職信、故事素材 | [`letters/README.md`](letters/README.md)、[`letters/story-bank.md`](letters/story-bank.md) | [`letters/log.md`](letters/log.md) |
| 104 履歷欄位 | [`104/README.md`](104/README.md) → [`104/fields-spec.md`](104/fields-spec.md) → [`104/content-spec-quill.md`](104/content-spec-quill.md)（Quill HTML 與各欄撰寫規格；範例只取格式） | [`104/resume-104.md`](104/resume-104.md)、[`104/chrome-playbook.md`](104/chrome-playbook.md) |
| 作品集／case study | [`portfolio/`](portfolio/)（內部版）、`portfolio/public/`（對外版） | [`site/`](site/)（網站助手專屬） |
| 投遞紀錄（職缺 × 推薦信 × 履歷版本） | [`applications/INDEX.md`](applications/INDEX.md)，每職缺一檔 `applications/<code>.md` | 推薦信產生流程見 `skills/104coverletter/SKILL.md` §5 |
| 職缺與公司資料 | [`targets/README.md`](targets/README.md)、`targets/jobs.md`、`targets/companies.md` | [`review-panel/jd/routing.tsv`](review-panel/jd/routing.tsv)（每份職缺的分層） |
| 看驗證結果、投遞優先序 | [`review-panel/HISTORY.md`](review-panel/HISTORY.md)、[`review-panel/opus-matrix.md`](review-panel/opus-matrix.md) | `review-panel/runs/<日期>-<版本>-*/`（單次結果） |
| 遇到〔待補〕或想問使用者 | [`library/open-questions.md`](library/open-questions.md)（問前先查） | Codex 的疑問寫 `drafts/codex/QUESTIONS.md` |
| Resume Gen 原 ChatGPT 交接、歷史稿／PDF／對話追溯 | Codex 分類 wiki：`drafts/codex/wiki/README.md` | 逐檔索引：`drafts/codex/FILE_INDEX.md`、雜湊清單 `drafts/codex/FILE_INDEX.csv` |
| 104 個人簡介與頂部個人特色規格 | `104/content-spec-quill.md` §5 | Codex 交接 `drafts/codex/2026-10-21-104-summary-chips-claude-handoff.md`（在 `codex/resume-writer`） |
| Codex 內容編輯協作與交付 | Resume Writer 指令：`drafts/codex/AGENTS.md` | 接手核對 `drafts/codex/2026-10-20-conversation-reconciliation.md`、`drafts/codex/QUESTIONS.md` |
| 產生 104 特化版履歷 md | [`skills/104resume/SKILL.md`](skills/104resume/SKILL.md) | `104/content-spec-quill.md` |
| 寫 104 自我推薦信（指定職缺） | [`skills/104coverletter/SKILL.md`](skills/104coverletter/SKILL.md) | `104/cover-letter-research.md`、`letters/104/` |
| 潤飾 104 特化版草稿（Codex） | [`codex-skills/polish-104/SKILL.md`](codex-skills/polish-104/SKILL.md) | `drafts/v11/104-v11.md` |
| 職能證據（F1–F15） | [`competency-framework.md`](competency-framework.md) → `wiki/F*.md`、`wiki/evidence-*.md` | — |

## 3. 現行稿與歷史稿

| 項目 | 位置 |
| :-- | :-- |
| **現行投遞版** | `drafts/v11.1/聶崑淮_資深產品經理_履歷_雙欄.pdf`（文字來源 `resume-v11.1.md`）＋104 特化版**現行 `drafts/v11.3/104-v11.3.md`**（階段 03 通過；v11.2 為前版、v11.1 待重整）；前版 `drafts/v11/`：`resume-v11.md`（文字來源）、`resume-v11.txt`、`聶崑淮_資深產品經理_履歷.pdf`（單欄，投遞用）、`…_雙欄.pdf`（僅寄信）、`104-v11.md`（104 特化版，給填表 agent） |
| 歷史稿 | `drafts/v7` … `drafts/v10.9`（v10.8 已被使用者否決，僅供查閱；不做版本間逐項比較） |
| Codex 產出 | `drafts/codex/`（只有 Resume Writer 寫；Career Move 只讀取） |
| Resume Gen 歷史封存 | `drafts/codex/archive/2026-10-20-resumegen/`（歷史 ZIP 全部原檔與後補對話；**僅供追溯，不是現行 facts、About Me 或投遞版**）；分類索引 `drafts/codex/wiki/`、`FILE_INDEX` 由 Codex 維護 |
| 草稿慣例 | [`drafts/README.md`](drafts/README.md) |

> **產出格式（2026-10-20 起）**：每次產生履歷只交雙欄 PDF＋104 特化版 md（見 `library/decisions.md` §20）。

> **每輪人物來源同步（2026-10-20 起）**：每輪檢查 `library/about-me.md` 是否需同步新確認內容；發現新補充與稿件落差，回報本人並附具體處理指令。規則見 `library/about-me.md`〈九〉。

> **管線（2026-10-21 起）**：`library/`（＝`00_library`，見 `library/README.md`）→ Claude `01_claude_stage/causal_draft.md` → Codex `02_codex_stage/`（Codex 分支；含 `voice_style_guide.md`、`final_resume.md`）→ Claude `scripts/verify_polish.py` 核對 → `drafts/<版本>/` 成品。

### 現行結構（2026-10-22）

```text
SulfurCreek/main
├── career/                                   # 分支 claude/happy-lamport-ljis8c（Claude 寫）
│   ├── library/                              # ＝00_library（不改名；優先級見 library/README.md）
│   │   ├── INDEX.md                          # 入口
│   │   ├── facts-1111.md、facts-prior.md、profile.md   # 事實庫（＝entities_source_of_truth）
│   │   ├── decisions.md、superseded.md、open-questions.md
│   │   └── about-me.md                       # 職涯思維與選材（＝about_me_mindset）
│   ├── 01_claude_stage/causal_draft.md       # Claude 產出：因果草稿＋STATUS／LOCK_ENTITIES 標記
│   ├── scripts/verify_polish.py              # Claude 執行：漏修、鎖定實體、未定義名詞、披露
│   ├── skills/resume-causal-logic-compiler/  # Claude 角色與編譯規則
│   ├── drafts/<版本>/                        # 成品：104 md、雙欄 PDF（Claude 核對後產出）
│   └── style/、104/、letters/ …              # 既有語氣、104 規格、推薦信
│
└── career/                                   # 分支 codex/resume-writer（Codex 寫；Claude 只讀）
    ├── 02_codex_stage/
    │   ├── voice_style_guide.md              # 語氣參數與禁用詞
    │   └── final_resume.md                   # Codex 潤飾、清除標記的成品
    └── drafts/codex/                         # Codex 交接與修改紀錄
```

## 4. 目錄速查

| 目錄／檔 | 內容 | 誰寫 |
| :-- | :-- | :-- |
| `library/`（＝00_library） | 使用者確認過的現行事實與裁定（**事實唯一來源**） | Career Move |
| `01_claude_stage/` | Claude 因果草稿 `causal_draft.md` | Career Move |
| `02_codex_stage/` | Codex 潤飾稿與語氣參數（在 `codex/resume-writer`） | Resume Writer（Codex）；Claude 只讀 |
| `scripts/verify_polish.py` | 潤飾後驗證：殘留標記、鎖定實體、LOCKED 段、未定義名詞、披露 | Career Move |
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

## 5. 讀取優先序（衝突時上面優先）

`library/` ＞ `style/resume-voice-zh.md` §7 ＞ `wiki/` ＞ 104／信件／作品集等下游產出（**下游不得當事實來源**）。

## 6. 快速搜尋

| 想找 | 指令（在 repo 根目錄） |
| :-- | :-- |
| 某個數字或說法出現在哪 | `grep -rn "關鍵字" career/library career/wiki` |
| 某個說法是否已被推翻 | `grep -n "關鍵字" career/library/superseded.md` |
| 某職缺的分層與公司 | `grep "代碼" career/review-panel/jd/routing.tsv` |
| 現行稿某段文字 | `grep -n "關鍵字" career/drafts/v11/resume-v11.md` |
