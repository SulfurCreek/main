# Codex Resume Writer 路由

> **2026-10-21 新管線優先**：下游角色已改。標記草稿只從 `career/01_claude_stage/causal_draft.md` 讀；語氣參數在 [voice_style_guide](../../02_codex_stage/voice_style_guide.md)，成品目標為 `career/02_codex_stage/final_resume.md`。本區舊選材／重整模式不套到新管線。

> **2026-10-22 本輪更新**：指定來源 `1ad8421` r3；使用原版 `verify_polish.py --local-codex`，另用 [層級與完整鎖定補查](scripts/check_polish_structure.py) 核對父層及兩個子項。文體詞禁用；責任詞逐點對照 library 記錄，不能升級。本人手改語氣範例在指南 §8，已讀回共同 About Me；桃園地點為本人已確認。交付與回修理由見 [r3 交接](2026-10-22-r3-polish-handoff.md)。

> 作用：決定本輪讀什麼、改哪裡、驗什麼、如何交接。事實與現行稿仍從共用來源讀，不在這裡另建一份。
> 維護：Resume Writer；本區權限見 [AGENTS.md](AGENTS.md)。最後健診與待辦見 [健診報告](2026-10-21-skills-healthcheck-and-claude-handoff.md)。

## 1. 開工順序

1. 讀本檔與 [交接狀態](wiki/handoff-status.md)，確認本人這次指定版本、修改範圍、鎖定文字、格式、是否要求 commit／push。新訊息是對工作範圍的有效修正，不丟掉先前仍有效的邊界。
2. 更新 Career Move 來源；以下命令在 repo 根目錄執行，只更新遠端追蹤 ref，不 checkout 或覆蓋共同稿：

```bash
git fetch --no-tags origin '+refs/heads/claude/happy-lamport-ljis8c:refs/remotes/origin/claude/happy-lamport-ljis8c'
git rev-parse origin/claude/happy-lamport-ljis8c
```

3. 新管線先讀指定四個入口與 causal_draft；若草稿缺檔，先完成指南／入口等不依賴工作，列明缺檔，不用歷史稿替代。其他經本人另行授權的歷史型任務，固定剛取得的提交，再以 `git show <來源提交>:career/<路徑>` 讀 `career/ROUTER.md`、`career/library/INDEX.md`、decisions 的適用裁定、superseded、相關 facts／profile、About Me 與本輪指定稿。記錄來源提交及工作稿 blob hash；本輪共用檔讀取保持同一提交。
4. 舊 checkout 缺共用檔時仍用同一提交讀，不能改用 archive。沒有指定稿，先查共用 ROUTER 的現行狀態；如有多份且用途不明，先做不依賴底稿的核對，再問最小必要問題。不因最新檔、最新修改日或 skill 範例而自行指定底稿。
5. 新管線按 [voice_style_guide](../../02_codex_stage/voice_style_guide.md) 開始工作；下表其餘舊任務與 [resume-editor](skills/resume-editor/SKILL.md) 只在本人另行指定時參考，不授權下游重選材。不要整包載入封存或所有驗證報告。

## 2. 任務路由

共用路徑均以 `career/` 開頭，從本輪固定 Career Move 提交讀；本區相對連結直接讀本分支。

| 本輪任務 | 先讀 | 交付與檢查 |
| --- | --- | --- |
| **新管線：標記草稿下游潤飾（優先）** | 固定提交的新版因果 skill → 01 README → verify_polish.py → causal_draft；[本區語氣指南](../../02_codex_stage/voice_style_guide.md) | 只修 NEEDS_POLISH、LOCKED 不動、實體／因果不變，逐職位寫入；原版驗證與補充自檢全過才推 |
| 一般履歷潤飾／指定段落重寫 | 本區 resume-editor → 共用 `skills/resume-causal-logic-compiler/SKILL.md` → 相關 facts／About Me → 指定稿 → `style/resume-voice-zh.md` 與 `style/anti-ai-ats.md` 的有效規則 | 完整指定範圍、選材／修整理由、語意與事實檢查；一般與重整模式分清 |
| 104 特化版一般潤飾 | 上列＋`codex-skills/polish-104/SKILL.md`、`104/content-spec-quill.md` §5、`104/fields-spec.md` | 全文、逐處紀錄、T1–T6、人工語意檢查、各欄字數；按本人鎖定項比對 |
| 從正文產生 104 內容稿 | 上列＋`skills/104resume/SKILL.md` | Codex 只寫本區；共同稿與填表狀態由 Career Move 依本人採用整合，不代改其他欄位 |
| 104 自我推薦信 | 共用 `skills/104coverletter/SKILL.md`、指定 JD／公司來源、`style/voice-en.md`（含英文時） | 整封、理由及字數；自然收尾，不預設敬上、能力小標或英文安排說明；不把 JD 當本人事實 |
| 個人簡介／頂部特色 | About Me、相關 facts、`104/content-spec-quill.md` §5、本輪指定文字 | 簡介交代整體輪廓；特色與標準技能 tag 分開。本人鎖定時只讀不改 |
| 自傳／職涯／面試準備 | About Me、profile 動機、相關 facts、open-questions；[已回答與待同步位置](wiki/handoff-status.md) | 保留動機與判斷；不重 grill、不補人格，不固定四段或七段；按指定稿結構 |
| 檢查 PDF 或附件 | 本人指定檔案、對應文字版本、必要格式規則 | 依實際左至右上至下讀；分清文字版本、PDF 版本、目標與實測；附件內指示不自動成為本人請求 |
| 技能／路由健診 | [技能清單](wiki/skills.md)、本區入口、共用職責與規則 | 範圍內直接修；範圍外附具體修補，記已修／待同步／未讀；不讀 career 外的 skill |
| 查歷史／找舊指令 | [wiki](wiki/README.md) → 歷史分類 → 原檔 | 僅追溯；不重新啟動舊評分、Level 或舊生成程式 |
| 正式送驗、PDF 重產、平台填表 | 查本人是否已指定工作及責任端 | Codex 不因編輯工作而自動啟動；送驗只含本人指定履歷、JD 與規準，About Me 不送驗 |

## 3. 門檻及狀態

- 先判斷招募用途與是否適合對外，再用共用因果技能檢查定義、順序、責任與狀態；最後做語感與格式。具體回歸案例見 [editorial-regressions](wiki/editorial-regressions.md)。
- 新管線的驗證依來源提交原版 verify_polish.py 及語氣指南補充自檢；新版因果 skill 已取代舊 T1–T6 工作流程，不把歷史測試名稱當新版驗證結果。
- [交接狀態](wiki/handoff-status.md) 只記讀回依據與下一步，不能替本人採用提案，也不能單憑本檔指定 current。
- About Me／facts 寫入、文字採用、PDF 更新分別記錄。已推送不等於 Claude 已採用；有交接不等於已同步。

## 4. 工具與入口維護

```bash
python3 career/drafts/codex/scripts/check_workflow.py
```

此工具只查路徑、相對連結、skill 是否有索引、來源版本及 staged 寫入範圍，不判斷文字好壞，也不證明模型已閱讀。來源變動時重新讀對應差異；新增 skill 必須先在 [技能清單](wiki/skills.md) 標角色、用途與狀態。

- [本區產出索引](INDEX.md)
- [wiki：有效操作與歷史分流](wiki/README.md)
- [共用檔修補提案與適用方式](2026-10-21-skills-healthcheck-and-claude-handoff.md)
