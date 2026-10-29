<!--markdownlint-disable MD013-->

# 英文寫作語氣規範（履歷、104 推薦信英文條列、cover letter）

> 2026-10-21 建立（本人同意）。Claude 與 Codex 共用。事實與責任範圍仍以 `library/` 為準；本檔只管英文怎麼寫。

## 1. 語域

- 平實商務英文；句子約 25 words 內。**第一人稱依體裁分流，見 §8**：推薦信／cover letter 用 `I`、短句；英文履歷列點省略主詞 `I`。
- 美式拼字（organization、prioritize）。
- 直接寫做了什麼、為什麼、結果；不先鋪陳、不自我評價。

## 2. 責任範圍 → 動詞對照（不得升級）

| 實際角色（library） | 可用 | 不可用 |
| :-- | :-- | :-- |
| 定義 AI 功能的情境與驗收標準 | defined the use cases and acceptance criteria; worked with the data science team | built, developed, engineered the model |
| 規劃新版系統、與工程分階段上線 | planned, worked with engineering on phased releases | rebuilt, led the architecture, architected |
| 還原沒有文件的規則 | worked out / recovered undocumented rules through hands-on testing and internal interviews | reverse-engineered the codebase |
| 導入 AI Agent 給同仁使用、同仁做最後判斷 | introduced an AI Agent; my colleagues made the final decisions | automated the whole process, eliminated manual work |
| 帶 2 名直屬企劃 | managed two product planners | led a large team |
| 主導職缺工作說明生成與 AI 推薦人才上線（decisions §51 白名單）；制定合規驗收標準 | led the launch of; set acceptance criteria | built the AI model, developed the algorithm |
| 主導 Juicy 推出（上線與導流期間 DAU） | led the launch of; during launch and promotion | single-handedly grew, drove X% revenue |

## 3. 固定譯法

| 中文 | 英文 |
| :-- | :-- |
| 產品企劃主任（履歷抬頭） | Product Owner (title: Product Planning Supervisor) |
| 企業端招募系統 | employer-side recruitment system |
| 職務類別代碼 | job-category codes |
| 驗收標準 | acceptance criteria |
| 分階段上線 | phased releases |
| 權限與計費規則 | permission and billing rules |
| 信心程度 | confidence levels |
| 人工判斷／覆核 | human review; final decisions |
| 近 10 年 | nearly 10 years |

## 4. 禁用

- AI 感詞：delve, tapestry, navigated, seamlessly, testament to, transformative, leverage, synergy, robust, cutting-edge。
- 套話：I am writing to express…, I am excited / thrilled to…, I believe I would be a great fit…, proven track record。
- 自誇形容詞：strategic, passionate, visionary, detail-oriented, results-driven。
- Spearheaded（全份最多 1 次，推薦信不用）。
- 不寫未具備的：Jira, SQL, frontend/backend development, A/B testing at this company。

## 5. 自檢

1. 每句主詞動詞清楚；被動句只在主詞不重要時用。
2. 數字、數量、日期與中文版一致。
3. 動詞沒有超出 §2 的範圍。
4. 大聲念一遍：像本人在面試裡會說的話。

## 6. 痛點破題、禁尾巴子句（本人 2026-10-29，推薦信與履歷共用）

- **不用 `Backed by N client requests` 開頭**：客戶的需求、建議或抱怨是「待解決的問題」，不是贊助或背書。用 `To address N client requests accumulated since 2021, …` 或 `In response to …`。
- **核心商業痛點不得塞在句尾關係子句**（No Trailing Pain Clauses）：
  - ❌ `Backed by 199 client requests since 2021, I am planning to merge the two overlapping tools employers and job seekers use to message each other, which leave interview invitations scattered; the work is now in development.`（最重要的痛點「面試邀約散落」被丟在 `, which leave…`，結構鬆散、力道全失）
  - ✅ **真實痛點破題 → 需求規模與核心方案**：`Because employers and job seekers currently message each other across two overlapping tools, interview invitations often get scattered. To address 199 client requests accumulated since 2021, I planned a unified messaging flow that is now in development.`
- 英文條列仍受 §2 責任動詞對照與「一點一事」約束；`planned`（規劃）不得升級成 `led`（除 decisions §51 白名單）。


## 7. 中翻英反降維與反直譯鐵律（Anti-Chinglish & No Credibility Stripping；本人 2026-10-29，LINE profile 抓出）

1. **不撞工程保留字**：中文「合併建議」（客戶要求整併兩套工具）一律譯 `N client requests`（前文已交代兩套工具，不另加括號解釋；括號是給編輯看的語意備註，不是正文，見 §8.4），禁用 `merge request(s)`（GitLab 程式碼合併請求，面試官會誤解）。同類先問：此英文詞在軟體業是否另有專有意義。
2. **專業帶人與法規用語**：直屬企劃＝`direct-report product planners`（禁 `my planners`、`guided … through`）；`labor-law compliance acceptance criteria` 不可漏 `compliance`；同句不混用名詞 `price cut` 與動詞 `cut it 65%`，改 `reduced it by 65%`。
3. **時序不得為省字改寫**：KOOL 2018/05 是專案啟動，英文寫 `After the project kicked off in 2018/05, … launch`，不寫 `launched in 2018/05`；借鏡 Airbnb、以 Miro 繪製流程不可刪。
4. **英文同享「首次提及必定義」**：不寫空泛的 `a group function`；必須交代解決的限制（原僅有全公司與個人兩種資料範圍）與用途（定義帳號、職缺、履歷存取規則與舊資料轉換，讓大型企業按部門或分店共同招募）。
5. **中文版 Stage 2 的商業目的、系統影響範圍、統計分母口徑，英文版 100% 保留**，不得因壓縮字數刪除（verify_line_profile.py 以必備錨點檢查）。

## 8. 體裁分流、句首多樣性、禁抄備註括號、成品檔純淨（本人 2026-10-29，LINE profile 第二輪抓出 4 病灶；verify_line_profile.py 自動攔截）

1. **體裁分流（Cover Letter ≠ Resume Bullets）**：
   - Cover Letter：自然第一人稱 `I`，每點 2～3 句完整短句。
   - **英文履歷列點（LINE、LinkedIn、英文 CV）**：外商標準 Implied First-Person，**省略主詞 `I`**。直接以高張力動詞（`Led`、`Planned`、`Raised`、`Coordinated`、`Consolidated`）或「精煉背景／目的子句 + 過去式動詞」開頭（`To lower…, led…`、`With ongoing iterations…, led…`、`After 10+ accounts were hijacked…, coordinated…`）。全篇列點 `I` ≤ 3 次，預設 0。成因：把推薦信的 `I` 短句規則套到履歷，一點連發 `I led… I guided… I set…` 像日記。
2. **句首多樣性（Anti-Anaphora）**：同一公司區塊內不得連續兩點以同一個首字開頭；全篇 `- For ` 開頭的列點 ≤ 2 點。成因：為湊「場景先行」無腦套 `For X, …` 模板。場景先行可改用 `With…`、`After…`、`When…`、`Because…`、`To…`、`In response to…` 或直接動詞開頭。
3. **規則備註不入正文**：本檔或 skill 裡括號內的譯法說明（如舊版 §7.1 的 `(to consolidate the tools)`）是給編輯看的語意提示，**不得連括號照抄**。前文已交代背景，後句直接寫 `199 client requests`；同一句不堆兩個說明性括號。**寫規則時，範例譯文只寫可直接入文的最終文字，語意說明放括號外的中文敘述。**
4. **成品檔純淨**：可填表的 `line-profile.md` 只含標題、directive、Bullet；不得出現 `## Editing Notes`、`## English Self-Review` 等非履歷章節。修改紀錄與自審寫在對話回覆（或 Codex 的交接檔 `drafts/codex/` 內），不寫進成品。
