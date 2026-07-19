# 前端修改工程單 撰寫規則

產出「前端修改工程單」（給切版師/QA 驗收用的視覺調整需求文件本體）時，**格式強制**套用 `.claude/skills/frontend-change-ticket-1111/SKILL.md`，用 `Skill` 工具載入該檔取得完整 Output Guidelines 與 Output Template。

## 何時用這份 vs 其他規則

| 情境 | 用哪個 |
| --- | --- |
| 決定「需求文件內文怎麼寫」（選擇器精準度、要不要 HTML 範例、備註區塊） | `.claude/skills/frontend-change-ticket-1111/SKILL.md`（本檔只是路由指標，內容以該 skill 為準） |
| 切版工作流程本身（稽核 mock↔正式、抓 Figma token、產自包含預覽、commit 節奏） | `.claude/skills/frontend-slicing-1111/SKILL.md` |
| HackMD 文件外層版面（版控表、`[TOC]`、章節編號、紅字慣例） | `.claude/skills/spec-doc-1111/SKILL.md` |

三者同時套用時的分工：`frontend-slicing-1111` 管流程、`spec-doc-1111` 管 HackMD 外層版面、`frontend-change-ticket-1111` 管**每一段需求內文**怎麼寫——三者衝突時，內文寫法以 `frontend-change-ticket-1111` 為準，取代 `frontend-slicing-1111/reference/requirement-doc-style.md` 的白話敘述風格。

## 核心差異（一句話記住）

工程單要**精準、少廢話**：選擇器/屬性直接寫出來，不寫視覺形容詞；有結構變更就給 HTML 範例；沒有的不硬湊背景說明。
