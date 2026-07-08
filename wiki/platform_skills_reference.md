# 平台內建 Skill 對照表（與本 repo 自製 skill 的分工）

本 repo 的 `.claude/skills/`（`spec-doc-1111`、`pm-toolkit`）只收錄 **1111 求才/求職系統專屬**的撰寫慣例。
除此之外，執行環境本身另外掛載了一批 Anthropic 官方提供、與專案無關的通用 skill（檔案在 `/mnt/skills/`，唯讀、非本 repo 內容），**不需要、也不應該**複製進本 repo——複製只會造成內容漂移與重複維護。本檔案記錄「實際確認存在哪些」與「分工方式」，本身不重複那些 skill 的內容。

## 查核方式與結論

執行環境的 `/mnt/skills/public/` 與 `/mnt/skills/examples/` 各是獨立唯讀掛載點，用 `ls`/`find` 逐一核對檔名後，**實際存在**的官方 skill 如下（未列出的名稱＝查無實體、不存在，不記錄）：

| 官方 skill | 位置 |
| :--- | :--- |
| docx／pdf／pptx／xlsx | ✅ `/mnt/skills/public/` |
| doc-coauthoring／mcp-builder／frontend-design／web-artifacts-builder／canvas-design／algorithmic-art／theme-factory／brand-guidelines／internal-comms／slack-gif-creator／skill-creator | ✅ `/mnt/skills/examples/` |
| `claude-api` | ✅ 以 session 註冊 skill 形式存在（出現在 Skill 工具的可用清單，可直接載入），`/mnt/skills` 下無實體檔——屬 harness 內建，非掛載點檔案 |

（歷史紀錄：曾核對過的 `webapp-testing` 在掛載點與全機檔案系統均查無實體、session 清單也沒有，視為不存在，已自本表移除。）

## 分工決策：哪些值得跟本 repo 的 skill 互相引用

逐一檢視 15 個已確認存在的 skill 後，多數是檔案格式工具（docx/pdf/pptx/xlsx）或視覺/前端產出工具（canvas-design、algorithmic-art、theme-factory、brand-guidelines、frontend-design、web-artifacts-builder、slack-gif-creator），與本 repo「幫 1111 求才/求職系統寫 HackMD 規格書、跨部門溝通」的工作內容沒有重疊，**不需要任何整合動作**——用到時 Claude 會自行判斷觸發，不必在本 repo 額外索引。

真正與本 repo 既有 skill 有主題重疊、值得交叉引用的只有 3 個：

| 官方 skill | 跟本 repo 哪個 skill 重疊 | 分工方式 |
| :--- | :--- | :--- |
| `internal-comms` | `pm-toolkit` 模組 D（跨部門溝通文案） | `pm-toolkit` 模組 D **只保留** 1111 專屬的「依對象調整語氣」「敏感文字優化」兩條慣例；制式內部溝通格式（3P updates、公司 newsletter、FAQ 罐頭回覆、incident report）改用官方 `internal-comms` skill，不在 `pm-toolkit` 重複範本。 |
| `doc-coauthoring` | `spec-doc-1111`（規格文件撰寫） | `spec-doc-1111` 是 1111 規格書的**固定骨架**（章節編號、MECE/操作狀態、版控表等），任何時候撰寫 1111 規格書都必須遵循。若是「從零開始、需要逐節訪談式共寫」的大型新文件，可以**疊加**使用 `doc-coauthoring` 的三階段流程（情境蒐集→逐節共寫→讀者測試）來引導對話，但最終仍要套回 `spec-doc-1111` 的骨架輸出。 |
| `skill-creator` | 維護 `.claude/skills/*` 本身 | 之後若要在本 repo **新增或大幅改寫一個 skill**（非單純補幾行慣例），改用 `skill-creator` 的草稿→測試→迭代流程，而不是手動編輯 SKILL.md 然後憑感覺修改。 |

## 使用原則

- 本檔案**不收錄**上述任何官方 skill 的實際內容/範本——要用時讓 Claude 直接讀 `/mnt/skills/.../SKILL.md`，本 repo 只記錄「分工決策」。
- 之後如果使用者提供新的官方 skill 清單，重複本檔案「查核方式」一節的核對流程（用 `find`/`mount` 實際確認檔案存在，不能只憑使用者描述）再更新上表。
