# 計畫：104 最新中文履歷 → 中英雙語履歷（2026-11-03，待本人核可）

> 個資檔，不外流。基準：本分支 `8e9b99a`、Codex 分支 `e73c007`。**本人說 OK 前，不跑任何上下游與盲測。**
> 已取消：先前「104 經歷只放英文」任務（commit 8e9b99a）。新規格的雙語產生器會重寫，該 commit 的 ORDER／斷路器將被取代。

## 一、要產出什麼

| # | 產出 | 位置（預計） |
| :-- | :-- | :-- |
| 1 | 最新中文 104 履歷（v12.20） | `career/drafts/v12.20/104-v12.20.md`、公開版 `104-v12.20-public.md` |
| 2 | 中英雙語 104 履歷 | `career/drafts/v12.20-bilingual/104-v12.20-bilingual.md` |
| 3 | 盲測報告＋處置表 | `career/review-panel/runs/2026-11-0x-*/` |

## 二、雙語欄位規格（本人 2026-11-03 指定）

| 欄位 | 內容 |
| :-- | :-- |
| 個人簡介 `info.bio` | **英文**（LINE 履歷 Summary 原句）＋一句說明附有英文 CV（見 Q2） |
| 工作經歷 4 筆 | **只放中文**（v12.20 中文原文，逐字） |
| 專案成就 4 筆說明 | **英文先行＋中文**；專案名稱、起訖、圖片、網址維持原設定 |
| 專長 6 筆說明 `desc` | **英文先行＋中文**；名稱、標籤維持原設定 |
| 其他（個人特色、經歷技能標籤、各欄位可自選的技能／工具、證照、語文、求職條件、自傳） | **全部維持原設定**，不動 |

英文規則：只從 `career/drafts/line/line-resume.md`（FINAL-LOCKED）擷取現成句子，Claude 與 Codex 都不得新寫或翻譯。

## 三、流程

### Step 1｜最新中文履歷（v12.20）
1. Stage 1–2（Claude）：讀 `library/`（含 10-27 之後新增的 decisions），比對 `01_claude_stage/causal_draft.md`，把新事實／裁定編入；標 `NEEDS_POLISH`／`LOCKED`、`LOCK_ENTITIES`。跑 `verify_polish.py` 上游 0 違規。
2. Claude 端盲測（credibility-blind-prompt，不讀 library）→ A/B/C 分流。
3. Stage 3（Codex）：依 `voice_style_guide.md` 潤飾 → `02_codex_stage/final_resume.md`，Codex 自跑 `check_polish_structure.py` 與 `verify_polish.py`。
4. Stage 4（Claude）：唯讀拉取 → `verify_polish.py` → `gen_104_md.py` 產 104 md → `verify_polish.py --verify-104` → `public_redact.py` 產公開版。
5. 定稿盲審（coach-prompt）→ 終審，收斂停機（不跑第 3 輪）。

### Step 2｜雙語組合
1. 改寫 `gen_104_bilingual.py`：簡介英文＋CV 說明；經歷只放中文；專案／專長英文先行；其餘逐字不動。
2. 改寫 `verify_104_bilingual.py`：欄位規格、中文零加工、英文句子必須來自 LINE（strict）、簡介 / 專案說明 ≤2000 字、專長字數。
3. Codex 潤飾（只能擷取／重排 LINE 原句、最小接合；「英文 CV」一句可潤）→ Claude 核對「已修改」清單 → 盲審一輪 → 定稿。
4. 新舊比對：Codex 舊版（e73c007）與新版逐欄 diff 報告，Claude 核對後採用。
5. 更新 Antigravity 填表指令檔（新欄位規格）。

## 四、本人答覆（2026-11-03）與據此調整

| # | 答覆 | 計畫調整 |
| :-- | :-- | :-- |
| Q1 | 好，今天自薦信改的句子也進履歷 | 已寫入 `library/decisions.md`（2026-11-03 九句）；編譯 v12.20 時視為現行事實，措辭仍依履歷語氣規則 |
| Q2 | Claude 先寫、Codex 潤 | 起草句：`An English version of this résumé is available on request.`（簡介最後一句；唯一新寫文字；Codex 潤飾後 Claude 核對）。若你嫌不夠「附近有」可改成 `English CV attached.` |
| Q3 | 簡介只留英文 | 簡介欄＝LINE Summary 原句 ＋ 上述一句；不放中文 |
| Q4 | 舊版 e73c007 不沿用，但要互相比較 | Step 2 新增比對：Codex 舊版（`origin/codex/resume-writer@e73c007` 的 `104-v12.19-bilingual.codex.md`）vs 新產生版，逐欄列差異（句子層級），由 Claude 核對，採用以新規格為準 |

## 五、工具清單
見同資料夾 `TOOLS.md`；檔案副本在 `claude/` 與 `codex/`（Codex 檔取自 `origin/codex/resume-writer@e73c007`，唯讀複本）。
