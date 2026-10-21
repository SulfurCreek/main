來源檔：Career Move `dd3d9f14f1acd9e7b887c30f7f1854bb55a917ba` 的 career 內四個現行 skill、原始因果參考、路由／指令／style／library 入口，以及 Codex 本區指令、wiki、兩個封存 skill 和本輪本人要求；逐項見技能清單。
〔待補〕：無履歷資料待補；career 外三個 Claude 技能未讀內文，已交該端健診，不宣稱完成。
事實疑問：無新增；QUESTIONS 只補已同步事項的讀回狀態，未更改 library。

# 技能健診與路由修整（2026-10-21，舊管線紀錄）

> **本人其後已指定新角色與 stage 管線**，新版因果 skill 取代本報告採用的版本。本報告及 14 檔 patch 保留歷史，不能整包套用而回退新規則；須逐項按新指令重核。本區目前入口已指向 `career/02_codex_stage/voice_style_guide.md`。

本區已建立能從固定指令走到實際工作流程的入口，新增人工語意檢查、真實失敗案例與交接狀態；共用技能／style／指令發現的衝突已做成精確修補檔，尚未套用共用來源。健診沒有改履歷正文或 PDF。

## 範圍與根因

本輪完整讀取 career 內 4 份現行 SKILL.md：polish-104、resume-causal-logic-compiler、104resume、104coverletter；另讀 2 份封存技能及 1 份原始因果參考。新建本區 resume-editor 是操作整合，不複製共用技能、有效事實或 About Me。

Career Move 的 resume-craft、resume-review-panel、portfolio-site 實體在 career 以外，受本人邊界限制未讀、未改；僅審查 career 內對它們的路由。平台隱藏／未提供技能不在可核對範圍，這不是全平台技能掃描。完整清單見 [wiki/skills.md](wiki/skills.md)。

反覆漏事有三個具體原因：入口累積歷史而沒有清楚狀態；規則分散且互相覆蓋；T1–T6 與格式檢查被誤當成語意編輯已完成。修正必須同時接入口、提供真實案例，並讓每次交接有讀回依據，不能只增加一段「下次注意」。

## 發現與處理狀態

| 編號 | 問題與原有依據 | 影響 | 本輪處理／尚待誰處理 |
| --- | --- | --- | --- |
| F01 | 本區 AGENTS 累積多輪規則，wiki 只導航封存，沒有單一路徑走到任務 skill | 知道有規則，工作時仍漏載 | **已修本區**：AGENTS → ROUTER → resume-editor；wiki 分有效操作與歷史 |
| F02 | polish-104 自檢偏重 diff、禁用詞、字數，因果技能 T1–T6 沒涵蓋所有語意問題 | 帶人與客戶回饋兩點通過檢查仍生硬 | **已補本區人工檢查**；共用兩份 skill 的補強在 patch，待 Career Move |
| F03 | 獨立可讀被執行成每點重複「KOOL 網紅媒合平台」等完整錨點 | 整段累贅，規則壓過自然閱讀 | **已修本區**：最短情境＋單點及整段兩次實讀；共用 patch 同步補入 |
| F04 | 「追蹤交付」與結案統計並列，「企業使用」未交代客戶，「提案」未定義 | 主詞與指標語意漂移，比例變化容易誤當個人因果 | **已補真實案例** E01–E03／E06；兩點提案維持待採用，不由健診改正文 |
| F05 | decisions §8 舊九步仍寫「20 個版本、評分、盲審、ATS 算分」 | 重新啟動本人已停用的選稿目標 | **本區不執行舊流程**；patch 在 §8 原文前標歷史與覆蓋範圍，待 Career Move |
| F06 | resume-voice-zh 開頭寫事實只能來自 wiki；前段仍示範粗體前綴、強動詞、固定四段自傳 | 舊模板與本人指定版本互相衝突 | **本區明確覆蓋**；patch 修來源並加現行適用順序，不改事實或本人鎖定文案 |
| F07 | anti-ai-ats §2「先停下來問」、§5「空泛就停下來問」，舊動詞規則禁協助／參與／負責 | 重 grill 或升級責任，刪掉有用協作案例 | **本區先查來源與已答**；patch 修 CAR、流程及動詞規則，保留角色界線 |
| F08 | 104resume 步驟 4「全部文字已潤飾過，標可填表」與步驟 7「本人同意後」衝突 | 潤飾被誤當本人採用 | **本區分提案／採用／讀回**；patch 消除可填表自動判定 |
| F09 | polish-104 舊讀稿命令與共用 ROUTER 範例寫死 v11；wiki/versions 也寫死 v11 | 拿錯版本或把最高版號當 current | **已修本區版本頁**；共用 patch 改為本人指定版本及固定來源提交 |
| F10 | 普通 fetch 範例未明確更新追蹤 ref；共用 CLAUDE 叫另一端 checkout Codex 目錄 | 可能讀舊追蹤 ref 或改動對方目錄 | **本區明確 refspec＋git show**；共用 patch 移除 checkout 取稿方式 |
| F11 | polish-104 許可搬螢光，未先判斷本人位置鎖定；ATS 模板要求移除視覺元素 | HTML／螢光被不當更動 | **本區位置鎖定優先**；patch 調整預設與平台適用範圍 |
| F12 | 104coverletter 中文建議 250–350、核對 200–400、中英混合 120–150 words 並列；範本固定結尾 | 為字數亂刪或帶回本人否決的結尾 | **本區依當輪要求與語言計法**；patch 統一優先序，結尾改為可選自然收尾 |
| F13 | 共用 CLAUDE／HANDOFF 有「全 repo 可讀」「可寫自有 skill」；Codex 原本只讀 career | 權限跨角色繼承 | **本區明確不繼承**；patch 在共用入口加角色範圍，未讀 career 外技能 |
| F14 | INDEX／QUESTIONS 有已交接仍待同步的文字，Q010／Q011 已在 library 寫入但歷史狀態未結 | 重問已回答資訊或誤報同步進度 | **已讀回並補最新狀態**，原紀錄保留歷史；不再當待辦 |
| F15 | 原 resume-gen-editing 快照引用舊 Library ID；驗證快照以 Level 為輸出 | 封存指示回流，重新建人物庫或評分 | **已分類為歷史**，不執行／安裝，不複製為第二份現行 skill |
| F16 | 文字採用、共同來源寫入、repo 推送與 PDF 更新常被合併成「完成」 | 誤稱 About Me 或 PDF 已更新 | **已建立交接狀態表**，每項附讀回依據或待同步責任端 |

## 本區已直接更動

- [AGENTS](AGENTS.md)：縮為固定啟動及角色邊界，移除會過期的範例指向。
- [ROUTER](ROUTER.md)：按任務列讀取、技能、修改範圍與交付檢查。
- [resume-editor](skills/resume-editor/SKILL.md)：把招募用途、主詞動作、指標語意、自然度及原意核對接入工作流程；與共用 T1–T6 分開記結果。
- [wiki](wiki/README.md)：有效操作與封存分流；[技能表](wiki/skills.md)、[錯誤案例](wiki/editorial-regressions.md)、[交接狀態](wiki/handoff-status.md) 各只做一件事。
- INDEX、原 ROUTER-INTEGRATION、wiki/versions 及 QUESTIONS：修過期路由或同步狀態，舊提案與來源原檔保留。
- [check_workflow.py](scripts/check_workflow.py)：只讀檢查必需檔案、相對連結、現行 skill 是否漏索引、來源版本提醒與 staged 寫入範圍。它不判斷語意、讀取完成、本人採用或平台設定，沒有 hook／自動推送。

## 共用來源修補（尚未套用）

[2026-10-21-shared-skill-fixes.patch](2026-10-21-shared-skill-fixes.patch) 精確針對上述固定提交的 14 個 career 內檔案：4 個現行 skill、2 個中文 style、decisions、ROUTER、CLAUDE、HANDOFF、共用 skills-index、codex-skills README、library INDEX 及 About Me。

Codex 只把修補文字寫在本區，沒有更改 library／共用技能。patch 的政策修正依本人先前有效要求與本輪健診授權；不更動任何履歷事實、數字、日期或工作稿。

About Me 修補只在〈九〉替換舊技能讀取說明，記本人這輪明確要求「技能健診＋router／wiki」，不新增人格推論；目前仍是**待同步**。

## 可直接交給 Claude Code 的指令

```text
請接手 Resume Writer 技能健診的共用修補。

1. 明確 fetch origin 的 codex/resume-writer，固定取得的提交；以 git show 讀
   career/drafts/codex/2026-10-21-skills-healthcheck-and-claude-handoff.md
   career/drafts/codex/2026-10-21-shared-skill-fixes.patch
   不 checkout、修改或整支合併對方 drafts/codex 目錄。
2. patch 基準是 dd3d9f14f1acd9e7b887c30f7f1854bb55a917ba。
   先逐檔核對後續改動，再 git apply --check；若已有後續改動，逐處整合，不覆蓋新資料。
   只在 Career Move 的可寫範圍套用並保留歷史紀錄；不改本輪履歷或 PDF，不把提案當本人定版。
3. 四個 career 內現行 skill 均需保持共同規則單一版本；Codex 流程入口只連到其分支，不 @ 匯入 Codex AGENTS 到 Claude 指令。
   完成語意門檻、狀態判定、歷史流程標記、版本路由、角色權限、字數計法及 About Me 協作偏好的修補。
4. 另請在你可讀／可寫的範圍健診 resume-craft、resume-review-panel、portfolio-site：
   核對有無強制評分／Level、20 版本、重複 grill、強動詞升級、舊四段模板、wiki 當事實 SSOT、
   104／PDF 路由或寫入範圍錯置。Codex 因只讀 career 邊界未讀它們的內文，不是已通過。
   回報每個入口、發現、實際修正與未完成項；不啟動驗證或網站發布。
5. 跑相對連結、角色與 staged 範圍檢查；commit 前綴 career:，只推自己的工作分支，不 force。
   回報實際提交、改哪些共用檔、三個技能健診結果。Codex 下一輪讀回後才將「待同步」結案。
```

上面是交接指令，未使用工具向另一端發訊息，不宣稱 Claude 已收到或執行。共用讀回與 patch 套用狀態見 [handoff-status](wiki/handoff-status.md)。

## 驗收紀錄

- `python3 career/drafts/codex/scripts/check_workflow.py`：14 份工作流程文件、148 個相對連結、4 個共用現行 skill 與 1 個本區現行 skill 均通過；沒有漏索引或跨 career 的操作連結。
- patch 語法由 `git apply --numstat` 解析，共 14 個共用檔。
- 以 `.scratch/skill-audit-2026-10-21/shared-baseline.index` 獨立暫存索引讀入固定來源，執行 `git apply --cached --check` 通過；沒有在共用工作區或正式暫存索引套用 patch。
- 本輪人工檢查：舊技能只作歷史、有效流程接入固定指令、語意與機械檢查分開、角色／事實來源不越界、未採用與待同步如實標示、路由不寫死現行版本。共用來源尚未完成的修補仍標待 Career Move。
- staged 範圍與 whitespace 於提交前再檢查。沒有刪除／改名來源檔，也未改 library、共用技能、履歷正文或 PDF。

結構檢查與 patch 可套用性不代表內容已採用；沒有對履歷重跑評分或正式送驗。
