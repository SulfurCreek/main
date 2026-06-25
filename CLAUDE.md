# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

---

## 🚀 動態檢索（RAG）— 依任務類型讀取對應 wiki 檔案

為了節省 context，平時只保留這份精簡路由表。當任務符合下列任一類型時，**先用 Read 讀取對應檔案**取得完整規則，再動手：

| 任務類型 | 讀取檔案 |
| --- | --- |
| 涉及 HackMD API 呼叫（建立／讀取／更新／刪除 note 或 folder） | `wiki/hackmd_rules.md` |
| 撰寫/修改 1111 規格書、需要求才系統業務代碼（`showfield`／`confirmed`／`oStatus` 等）、需先確認求才 vs 求職專案 | `wiki/recruitment_system_rules.md` |
| 涉及 Figma 畫面規格擷取、Figma → HackMD 轉換 | `wiki/figma_rules.md` |
| 需要用專案縮寫/術語溝通、看不懂某個欄位名稱在講什麼 | `wiki/glossary.md` |
| 產出/修改 Mermaid 圖表（流程圖、循序圖等） | `wiki/mermaid_styling_rules.md` |

規格書撰寫的格式細則（章節編號、MECE 狀態表、🚧 待補區塊模板等）由 `.claude/skills/spec-doc-1111/SKILL.md` 管理，用 `Skill` 工具載入，不在 wiki 裡重複。

涉及**數據分析／競品拆解／商業提案、跨部門溝通文案（公告/客服回覆/敏感溝通）、資料 Mapping Table 與資料庫正規化原則、OTP/MFA 類邊界條件檢查**時，用 `Skill` 工具載入 `.claude/skills/pm-toolkit/SKILL.md`（與 spec-doc-1111、mermaid_styling_rules.md 不重疊，僅收錄它們沒覆蓋的部分）。

---

## 常用速查（不需要查 wiki 就能用）

**HackMD 團隊**：team path `1111-jobdocs`（`https://hackmd.io/team/1111-jobdocs?nav=overview`）

**Auth 快速測試**：
```bash
curl "https://api.hackmd.io/v1/me" -H "Authorization: Bearer $HACKMD_TOKEN"
```
Token 存在環境變數 `HACKMD_TOKEN`，`.env` 已列入 `.gitignore`，絕不寫死在程式碼或文件裡。
