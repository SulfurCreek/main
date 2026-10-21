---
name: 104resume
description: 從現行履歷產生 104 特化版履歷 md（Quill HTML、逐欄位路徑，給填表 agent 用），交 Codex 潤飾後由 Career Move 核對採用。觸發：「104 履歷」「104 特化版」「104 md」。
---

<!--markdownlint-disable MD013-->

# 104resume：104 特化版履歷 md

> 維護：Career Move。原 `resume-craft/references/104-quill.md` 的流程獨立成本 skill（2026-10-20 本人要求）；該 reference 改為指向本檔。

## 1. 來源

| 用途 | 檔案 |
| :-- | :-- |
| 正文底稿 | 現行版 `career/drafts/<版本>/resume-<版本>.md`（見 `career/ROUTER.md` §3） |
| 格式 | `career/104/content-spec-quill.md`（Quill HTML 樣式、欄位路徑、撰寫公式；**範例文字只取格式，不取事實**） |
| 字數 | `career/104/fields-spec.md`；取較嚴者：自述 ≤300、經歷每段 ≤1500、專長名 ≤15／desc 100–200、專案名 ≤30／說明 ≤2000、中文自傳 ≤4000 |
| 範圍 | `library/decisions.md` §20：只寫內容欄；不附英文自傳；專案成就 4 個（JustDating／Juicy 兩次承接、KOOL、新版求才系統、群組共同招募） |
| 管理責任 | `library/profile.md`：1111「1~5 人」，尚凡、思維特、新蛋「無」 |
| 範本 | 最新一份 `career/drafts/<版本>/104-<版本>.md` |

## 2. 步驟

1. 依欄位放入：自述（`info.info.bio`）→ 經歷（blockquote 範疇＋`ql-size-large` 主題小標＋條列＋`ql-divider`／`small` 工具列）→ 專長 4 項（name／desc／tag）→ 中文自傳（每段 `<p>`）→ 專案 4 個（name、起訖、isInProgress、introduction）→ 求職條件內容（純文字）。
2. 螢光 `#fbf3db` 只標數字；不新增數字或說法；缺的結構欄（如 KOOL 結束年月）標〔待補〕，填表留空。
3. 字數檢查（去 HTML 計純文字），全部在上限內；禁用詞為 0（Spearheaded、第一大、Jira、案主／業主、3 週上線、千萬、承接率、雙週 Sprint）。
4. 檔頭：若有新寫、未潤飾段落，標「草稿，待 Resume Writer（Codex）潤飾」並列出段落；若全部文字已潤飾過，標「可填表」。
5. 草稿由 Codex 依 `career/codex-skills/polish-104/SKILL.md` 潤飾 → 推 `codex/resume-writer` → 本人轉達。
6. 核對潤飾稿（`git show origin/codex/resume-writer:career/drafts/codex/104-<版本>-polished.md`）：欄位路徑相同、各區塊數字與 HTML 標籤不變、禁用詞 0、限定詞未刪；語意偏移處回報本人。
7. 本人同意後採用，檔頭改「可填表」，更新 `ROUTER.md` 現行版指向，commit 前綴 `career:`。
