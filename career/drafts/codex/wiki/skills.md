# 技能清單與適用範圍

> 2026-10-22：本頁僅供歷史存檔，不是例行讀取清單。操作只依 [AGENTS.md](../AGENTS.md) 的 Strict 3-Step Workflow；下列舊有來源讀取、工具檢查、索引維護等要求全部失效。

> 歷史健診基準：Career Move `dd3d9f14f1acd9e7b887c30f7f1854bb55a917ba`。2026-10-21 本人新管線已讀回 `7839fd42a75c763ff12e4ee23fc1553ed3fa7ec7`；目前下游操作以 [stage 02 語氣指南](../../../02_codex_stage/voice_style_guide.md) 為準。這是技能導航，不是人物或事實庫。操作回 [ROUTER](../ROUTER.md)。

## 已讀內容的完整清單

共用檔從上述提交讀取；Codex 不直接改它們。舊共用待修項須按新角色重核，見 [歷史健診報告與修補](../2026-10-21-skills-healthcheck-and-claude-handoff.md)。

| skill／材料 | 位置 | 狀態、用途與維護者 |
| --- | --- | --- |
| resume-editor | [本區 SKILL](../skills/resume-editor/SKILL.md) | 舊模式參考，已由新管線覆蓋；不能在 stage 02 執行重選材 |
| polish-104 | `career/codex-skills/polish-104/SKILL.md` | 現行、已讀；Career Move 維護。一般潤飾與指定重整，語感及範例入口待修 |
| resume-causal-logic-compiler | `career/skills/resume-causal-logic-compiler/SKILL.md` | 新版已讀；現為 Claude 上游角色，產帶標記 causal_draft；前版 T1–T6 與舊修補不得覆蓋新管線 |
| 104resume | `career/skills/104resume/SKILL.md` | 現行、已讀；104 欄位生成與雙端核對。不得套用其 Career Move 寫入範圍；可填表狀態及舊範例待修 |
| 104coverletter | `career/skills/104coverletter/SKILL.md` | 現行、已讀；指定職缺推薦信。字數優先序、結尾範本與驗證輸入路由待修 |
| resume-gen-editing 快照 | [封存 SKILL](../archive/2026-10-20-resumegen/source/reference/skill_snapshots/resume-gen-editing/SKILL.md) | 歷史，僅健診與追溯；保留選材與語感方法，舊 Library ID／存取方式及權限不執行，不安裝為第二份現行 skill |
| validate-resume-scoring 快照 | [封存 SKILL](../archive/2026-10-20-resumegen/source/archive/historical_validation/skill_snapshot/validate-resume-scoring/SKILL.md) | 歷史，僅健診與追溯；不自行啟動合成履歷、評分、Level 或分代理驗證 |
| 因果技能原始版本說明 | `career/skills/resume-causal-logic-compiler/references/original-user-version.md` | 共用歷史參考，已讀；以其上層現行 skill 為準，不執行強動詞升級、固定演進順序或新建 SSOT |

共讀的規範與入口：`career/ROUTER.md`、`career/CLAUDE.md`、`career/HANDOFF.md`、`career/wiki/skills-index.md`、`career/codex-skills/README.md`、library 的 INDEX／decisions／superseded／About Me、`style/resume-voice-zh.md`、`style/anti-ai-ats.md`、`style/voice-en.md`、`104/content-spec-quill.md` §5，以及本區 AGENTS／INDEX／wiki。它們也可能帶舊規則，不能只健診 SKILL.md 而放過入口。

## 知道存在但未讀內文的技能

共用 `career/wiki/skills-index.md` 列出 Career Move 的 `resume-craft`、`resume-review-panel`、`portfolio-site`，實體在 `career/` 以外。本人原有只讀 career 的邊界仍有效，本輪沒有讀取、修改或宣稱已健診其內文。已檢查其 career 內路由敘述，給 Claude 的指令請該端核對內文並回報；不把外部路徑當 Codex 可執行入口。

本輪也不宣稱盤點平台所有隱藏／未提供的技能或更新 ChatGPT 專案設定。不因新增 skill 自動分類、掃描或更新路由。

## 衝突如何處理

以下舊模式衝突表不能授權下游重新選材或改因果。新管線一律保護 LOCKED／LOCK_ENTITIES；若鎖定與禁詞或幅度衝突，列具體位置回上游，不自行解鎖。

| 衝突 | 本區採用的有效要求 |
| --- | --- |
| 舊九步評分／20 版本與本人禁用分數目標 | 按本人指示做內容編輯，不自行走評分或 Level 流程 |
| 一般潤飾與「外部看不懂」 | 仍需發現句意問題；本人指定重整時只重整指定範圍；鎖定項不動 |
| 每點獨立與名稱反覆堆疊 | 補最短必要情境，整段順讀也要自然；不把整個背景搬入每點 |
| 舊 wiki 事實與 library | library 與本人當次確認優先，過期例句不補成事實 |
| 舊四段自傳與已確認版本結構 | 依本人指定稿及本輪範圍，不強制改段數 |
| 英文技能與中文舊強動詞表 | 依真實責任，不推定工程實作；英文讀共用 voice-en |
| 104 HTML 與 ATS 單欄模板 | 依本輪平台及格式鎖定，不用 ATS 模板移除 104 標籤 |
| 共用技能允許搬螢光與本人要求位置不動 | 本人鎖定優先，標籤、包覆文字與位置都比對 |
| 歷史字數／chip／版本範例與本人鎖定文字 | 查本輪指定稿及現行規格，不回填歷史字數或特色提案 |
| 共用 CLAUDE 可讀全 repo 與 Codex 邊界 | 只讀 career；角色權限不繼承給另一端 |

[返回 wiki](README.md)
