<!--markdownlint-disable MD033-->
<!--markdownlint-disable MD013-->

# 給主幹（Repo Steward）的變更請求 / Requests to main

本檔由 `claude/happy-lamport-ljis8c`（career session）依硬規則一寫入，**不自行修改** `career/` 以外的檔案。
請主幹判斷後統一施作，施作後可清空對應條目。

---

（目前沒有待處理請求。先前請求已由主幹於 `7269939`／`69f383c`／作品集雙軌 commit 施作並清空。）

## 2026-10-04：新增求職信能力（中文自我推薦信＋英文 cover letter）

**現況**：英文的部分 career-ops 已經有完整的 `modes/cover.md`（JD gate、公司研究、語氣校準），不需要重做。
中文自我推薦信目前**沒有任何 skill 涵蓋**。資料層已建在 `career/letters/`（story-bank、log、archive），由 career session 維護。

**建議做法**：不另開 skill，併入 `resume-craft`，避免跟 career-ops 重複造輪。

1. 新增 `.claude/skills/resume-craft/references/cover-letters.md`，內容：
   - **路由**：英文 cover letter → 用 career-ops `cover` 模式，story-bank 優先於 cv.md；中文自我推薦信 → 用本檔。
   - **中文自我推薦信規格**：A4 一頁、350–500 字、4 段、每段 ≤ 4 行（手機可讀）。
     ① 稱謂＋應徵職缺＋一句定位；② 1–2 個成果證據，對應 JD 前三項要求；
     ③ 為什麼是這間公司（必須是真實的連結，例如產品使用者或同領域）；④ 前 90 天能做什麼＋面談邀請。
   - **跟自傳的分工**：自傳寫「我是誰」，放在 104 自傳欄，通用；推薦信寫「為什麼是這個職缺」，每封客製。兩者不可整段複用。
   - **台灣語氣**：用「您好」「敬請」等有禮但不卑微的語氣；不寫「懇請給予機會」這類乞求句；不寫家庭背景。
   - **硬規則**：數字只能取自 `career/letters/story-bank.md`，沒有就標 `〔待補數據〕`；
     寫完存 `career/letters/archive/`，並在 `log.md` 加一列；career 內容不上 HackMD。
2. 新增 `assets/cover-letter-tw-zh.md`（中文範本，對應上面 4 段的佔位符）。
3. `SKILL.md` 的 description 觸發詞加入「求職信、自我推薦信、推薦函、cover letter、應徵信」；任務路由表加一列指向 `references/cover-letters.md`。

**為什麼**：使用者要求針對中文推薦信與英文 cover letter 建立專責能力。英文已由 career-ops 涵蓋，缺的只有中文；併進 resume-craft，就能沿用同一套證據與誠實規則。
