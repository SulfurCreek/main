<!--markdownlint-disable MD013-->

# 104 特化版產生流程（Claude／Career Move）

> 2026-10-20 起，每次產生履歷只交兩樣：雙欄 PDF＋104 特化版 md（`career/library/decisions.md` §20）。本檔是 104 特化版的產生步驟。

## 來源

| 用途 | 檔案 |
| :-- | :-- |
| 正文底稿 | 現行版 `career/drafts/<版本>/resume-<版本>.md`（見 `career/ROUTER.md` §3） |
| 格式 | `career/104/content-spec-quill.md`：Quill HTML 樣式、欄位路徑、撰寫公式。**範例文字只取格式，不取事實** |
| 字數 | `career/104/fields-spec.md`（取較嚴者：自述 ≤300、經歷 ≤1500、專長名 ≤15／desc 100–200、專案名 ≤30／說明 ≤2000、中文自傳 ≤4000） |
| 範圍裁定 | `decisions.md` §20：只寫內容欄、不附英文自傳、專案成就 4 個（JustDating／Juicy、KOOL、新版求才系統、群組共同招募） |
| 管理責任 | `library/profile.md`：1111「1~5 人」，其餘「無」 |
| 範本 | 上一版 `career/drafts/v11/104-v11.md` |

## 步驟

1. 從底稿取文字，依欄位放入：自述 → 經歷（blockquote＋主題小標＋條列＋工具列）→ 專長 4 項（name／desc／tag）→ 中文自傳（每段 `<p>`）→ 專案 4 個 → 求職條件內容。
2. 螢光 `#fbf3db` 只標數字；不新增數字或說法。缺的結構欄（如 KOOL 結束年月）標〔待補〕，填表時留空。
3. 跑字數檢查（去 HTML 計純文字），全部在上限內。
4. 檔頭標「草稿，待 Resume Writer（Codex）潤飾」，並列出**本版新寫、未潤飾的段落**。
5. Codex 依 `career/codex-skills/polish-104/SKILL.md` 潤飾 → 推 `codex/resume-writer` → 使用者轉達。
6. Career Move 讀取潤飾稿（`git show origin/codex/resume-writer:career/drafts/codex/104-<版本>-polished.md`），核對：欄位路徑相同、各區塊數字與 HTML 標籤不變、禁用詞為 0、限定詞未刪；只回報語意偏移處給使用者決定。
7. 使用者同意後採用，檔頭改「已潤飾，可填表」，commit 前綴 `career:`。
