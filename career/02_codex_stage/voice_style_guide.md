> 2026-11-03 本人新裁定：自動事實、數字與LOCK內容比對全部停用；下方相關自動gate要求失效。語氣章節只供人工編輯，不重啟fact_lock、固定事實錨點或check_polish_structure。流程唯一依AGENTS及Claude分支career/PIPELINE_POLICY.md。FINAL-LOCKED英文雙語組裝不作自由改寫。main嚴格唯讀。

# Voice & Style Guide：按輸出語言分流

基底：c0c429e1fcff36365054db2b5c7b598a0e6f7d73 的 career/style/README.md。操作、權限、事實鎖定與交付流程依 [AGENTS.md](../drafts/codex/AGENTS.md)。

| 輸出 | 唯一語氣閱讀範圍 | 驗證入口與支援界線 |
| --- | --- | --- |
| 中文履歷／自傳 | 只讀中文潤飾章節 | verify_polish.py，先核對指定工具commit支援的格式與參數。 |
| 中文推薦信 | 只讀中文潤飾章節 | verify_letter.py，只用該版本支援的中文信件入口；職缺名依指定草稿。 |
| 英文LINE Resume／Profile | 只讀英文潤飾章節 | verify_line_profile.py僅限已確認支援的LINE文件格式；不代表生成器相容。 |
| 其他英文Resume／CV／LinkedIn／推薦信／獨立條列 | 只讀英文潤飾章節 | 待Claude指定支援格式與實際入口；不得套用LINE驗證器，也不得宣稱完整驗收。 |
| 中英混合文件 | 各段按輸出語言分流 | 各段與整份文件的語言／類型路由均須明確；入口未支援時逐項標示，不以單段通過代表整份通過。 |
| 轉換／PDF | 依現行分工交Claude | 記錄實際產物、執行者及驗收者；未執行或未驗證就明示。 |

兩章不互相引用，也不把另一語言的口癖、句型、責任動詞白名單或排版套過來。事實與鎖定的共用護欄由 AGENTS 管理。
**唯一語氣橋接**：英文完整保留對應中文的商業目的、系統影響範圍與統計口徑；若翻譯需要資訊而授權草稿不足，交上游補明，不讀受限事實庫、不自行推測。

尚未實作或未收到新工具commit的語氣工具，不當作已存在、已修復或已驗收。Claude維護驗證器及輸入／輸出契約，Codex不修改上游工具。

### 操作與驗收的共通界線

這裡只規定執行證據，不把兩個語言的文體規範混用；具體操作依AGENTS.md。
- 完整閱讀指定SHA上游及完整候選，不只讀diff或鎖定字串。數字相同不等於事實相同，逐項核對數字、對象、單位、百分比／件數、約數、期間、分母、比較組、責任、歸因、限定及開發中／已上線等完成狀態。
- 可改的跨欄重複、語序及不同欄位用途直接處理。刪整個案例、改職缺定位或事實不明交Claude；鎖定阻擋則附上游SHA、區塊、原句、替換句與需調整鎖定詞。
- 不因相似度而任意換詞，不為固定英文錨點、舊格式解析或字串命中塞回不自然句子或重複資訊。合理文字遭誤攔時回報工具／契約問題，不改驗證器、不偽造輸入，也不宣稱通過。
- 交付四項獨立紀錄：腳本名稱／固定版本／實際參數／Exit Code；完整成品表達及跨欄審查；對指定上游的語意事實核對；轉換或PDF是否實際執行及由誰驗收。一項通過不能擴張成其他項通過。
- 已知漏檢風險包括中文數值不變卻更換對象／單位／狀態，英文空文字欄位、非法action或註解錨點被接受，驗證後仍無法輸入生成器，以及僅姓名／占位文字的PDF表面通過。Exit 0不是上述問題已排除的證明。
- 收到Claude指定新工具commit後，先核對支援格式、schema、參數、來源及生成契約，再在獲准範圍回歸。殘餘漏檢／誤攔以最小合成案例交回：版本、入口、合成輸入、預期與實際結果、Exit Code及影響；不把合成數據當本人事實。
- 純規則維護只回報規則差異、路由、工具限制與待Claude事項。未指定新工具commit／成品時，不讀改履歷湊測試，不虛報內容審查、成品盲審或PDF驗收。

## 中文潤飾

### 適用與語氣

適用繁體中文履歷、自傳、中文推薦信，以及混合文件的中文段落。授權語氣來源是 career/style/resume-voice-zh.md；不讀英文規範作中文標準。
用台灣用語，平實、具體、結論先行。句子有對象、動作與結果，不堆自誇形容詞。不把產品規劃寫成工程實作；責任、數據、完成狀態依當輪來源。
履歷以本人為預設動作主體，不每點補「由我」。自傳可自然第一人稱，保留本人判斷、語氣與職涯演進，不寫成另一份經歷清單。

### 敘事與跨欄去重

- 前 15～20 字讓讀者辨認產品、核心動作或具體限制，但先定義場景才展開細節；不讓數字失去衡量對象。
- 依上游 LEAD 安排：RESULT 先點明對象與指標；ACTION 以責任與行動串交付；CONTEXT 只留理解行動所需背景。未標 LEAD 時自行判斷，不固定成果永遠最前。
- 背景原則不超過整點 1/3，約 25～45 字；65～85 字是節奏目標，不為壓字數刪事實。一般工作經歷主幹淨字數 ≤165，雙次危機承接 ≤190，依當輪驗證器與本人指示。
- 簡介呈現定位，經歷保留責任與成果，專長呈現通用方法，專案呈現限制與關鍵做法，自傳呈現判斷及人物理解。不要同一案例跨欄完整重講。
- 父子層級與共同背景保留；子項不重複父項，不在父項新增獨立成果。口頭舉例提煉成制度概念，不把分店店長、行政助理等解釋用角色清單塞入正文。

### 詞彙、責任與口癖

- 正文「建立」≤5、「救回」≤1（僅授權的工作經歷危機承接）、「推進」≤8、「統籌」≤3。同一列點／自傳自然段的「規劃、協調、定義、負責」各 ≤2。先整併重複命題，不整批換成另一口癖。
- 主導、推動、拍板只在上游該事項已明寫或有 AMPLIFY 授權時使用，不把授權擴到工程、他人任務或公司決策。公司簡介生成、公司負責人的定價決定等各自歸因。
- 協助、參與、配合、支援、維護若準確反映責任則保留，不為加強詞替換成主導；不用架構、開發、實作、重構、扛下包裝一般規劃。
- 禁文體套詞：賦能、抓手、閉環、攜手、助力、全方位、深耕、致力於、成功地、圓滿達成、極大地、顯著地、透過、藉由、利用、進行一個、完成了。
- 不寫建立…的方式／機制／管道等硬湊句。並列不亂加逗號；不用「再」暗示未確認先後；不堆「推進調整上線」；保留提案後等時間口徑。

### 數據與限定

營收占比不寫成總營收增長；規模與需求件數不當個人成果。保留期間、分母、對照、約數、團隊歸因及開發中狀態。
統計口徑收束在指標旁或句尾括號，單一括號中文字 ≤35；不把核心動作與戰果藏進括號。兩次服務承接的共同限定統攝一次，不貼相同長句兩遍。
不為讀起來更有力新增成效或免責尾句；依當輪已裁定的完成／結案口徑。

### 104／Quill 與視覺樣式

- 保留欄位路徑、HTML、螢光位置、管理責任、本人已定特色與 LOCKED 模組標題，除非本輪明確授權。
- G 金黃 #fbf3db：工作經歷及專案成就每區選1～2處成果／規模短語；不標純日期、不突出負向對照、不整句塗滿。
- B 晴藍 #deebf1 加粗：工作經歷每點至多1處核心產品或模組；不為湊色另造贅句。
- BT 純粗體：經歷、自傳、專案首次必要專名；不與 B 重複。
- 參數值是本區正文精確連續子字串；較長詞優先，避免巢狀套色；未命中回報。簡介、個人特色、專長、新蛋及求職條件純文字。
- 不用粗體分類前綴。104轉換與PDF由Claude處理；Markdown通過不等於Quill或PDF已驗收。

### 中文自我推薦信

純文字，一封一職缺，指定三點或來源指定點數，使用「‧」；全中文350字內，除非本人另訂。
前5秒呈現已確認的限制、交付與反差成果，不把履歷剪成電報。每點有獨立產品場景，不以日期或無對象的「帳號權限」起頭；不加「能力小標：」。
上游已白話化的產品名不加回；必要專名首次定義。不塞報表分母分類清單，不用另外／此外硬接無關事件。
稱謂一律貴公司；不寫貴司、我司、敝司、敬上。不新增公司觀察或未授權地名。
結尾總結前三點的核心課題，期待交流與分享經驗；不寫經驗相關、方向相近、可以直接投入或立即解決。
本人2026-11-02更新的批次推薦信：有AI工作流程案例時，「可重複使用的 AI 作業流程」「指導同仁」「收斂至個位數筆」須逐字保留，不改回「可重用 Skill」，也不得改成以同仁為主詞。由本人定義規則、驗證要求、整理流程及指導同仁；Agent標示信心程度後仍須人工覆核。結尾保留「貴公司團隊」。這是本批的明文裁定，不據此在其他未提供該案例的信件新增事實。

### 中文自審與隔離盲審提示

乾淨、不繼承歷史的只讀子代理，只收完整對外中文候選正文及獲准JD；不收上游、內部規則、事實庫、鎖定清單或另一側意見。非對外註解在派發Prompt時移除，不在repo新增盲審暫存檔；提示與回覆用中文。實際派發可用：

> 以台灣科技業資深PM／B2B PO招聘閱讀視角，閱讀下列完整中文成品。檢查責任與職級是否可信、陌生人能否理解場景、商業目的與成果是否清楚、中文自然度及跨欄重複。指出具體原句、理解風險與可改措辭，不新增事實、不評分、不為湊數捏造問題。不使用工具讀取其他檔案；只依提供的成品與JD。請以中文回覆並說明實際讀取範圍。

主代理逐項依三分類閉合：已修正附Before → After及跨欄結果；不採納附來源或本人明文裁定；鎖定阻擋附精確上游替換指令。Claude主代理依現行規則終審，避免A↔B反覆修改。盲審不能替代事實核對；未讀JD就不宣稱JD匹配審查。完整中文履歷按實際欄位回報；推薦信不硬套不存在的七大模組，不用英文I次數等規則審中文。
中文履歷及推薦信先確認指定版本的支援格式及實際入口。可預檢、隔離盲審、改稿重讀及最終驗證，但不能以Exit 0代表文字、事實、轉換或PDF同時合格。工具誤攔交Claude，不為過關改事實或硬湊文字；未通過如實標示，是否先交候選依本人明文指示。規則維護不將這些成品步驟冒稱已完成。

## 英文潤飾

### Scope and register

Applies to English resumes, LINE Resume/Profile, LinkedIn/CV, English cover letters and the English passages of mixed documents. The voice source is career/style/voice-en.md, especially §§8–13. Use natural American business English, concrete verbs and readable sentences; do not apply Chinese word-frequency limits, a mandatory first-20-words impact test, a Chinese responsibility-verb whitelist, Quill styling or autobiography conventions.

### Genre and syntax

- Resume bullets use implied first person: omit I, default zero, at most three occurrences across bullets. Use an authorized action verb or a concise contextual clause; current-role scope may use present tense.
- Cover letters use natural first-person I and complete sentences. Do not apply the resume I limit to letters.
- Within a company, consecutive bullets must not start with the same word. At most two bullets start with For. Vary syntax for meaning, not merely to replace the opening word.
- Define a product, experiment or system before referring to its acceptance criteria, discounted phase or other details. Keep subjects and references clear.
- Client requests are problems to address, not backing: use To address / In response to, never Backed by. Do not hide the core business problem in a trailing “, which leave…” clause.
- Use client requests for tool-consolidation suggestions, not merge requests. Do not copy editorial explanations such as “(to consolidate the tools)” into final prose.

### Responsibility, management and data literacy

Keep the precise responsibility authorized in the English source; do not infer engineering implementation, architectural ownership, model development or a pricing decision made by someone else.
Use led only for the explicitly authorized task. Do not turn planned/worked with engineering into rebuilt, engineered the model or led the architecture.
Use the approved management wording “Manage two product planners as direct reports.” Follow with guided direct reports or delegated … to direct reports when the recipients are direct reports; retain colleagues for other collaborators. Never imply a larger team or use subordinates.
For the approved category-table example, define the object first: “Audited and consolidated 15 shared category code tables (job roles, certifications, skills and benefits)”. Use reviewing the underlying data fields and structuring field-level mappings; do not substitute govern, or claim software implementation. These expressions apply only to the confirmed work, not as generic claims for other cases.
For undocumented system rules, use the approved “Analyzed and mapped undocumented account permissions and business rules”. Never use Reverse-engineer/Reverse-engineered or revive Recovered the logic behind. Keep the approved 743-of-840 result and its temporal attribution; do not turn it into a direct causal claim.

### AI, skills and word choice

Within a human-in-the-loop workflow, retain ownership of final product decisions; do not repeat with human review. Keep the actual human decision-maker clear when describing colleagues.
Introduce unfamiliar tools with AI agents (Claude Code, Antigravity) or Design & Agentic AI Tools.
Skills items and category headings use Title Case, preserving acronym and brand spelling: Requirements Analysis, PRD, User Story, Use Case, Process & Sequence Diagrams, Prototyping, UAT. Use & in skill category labels.
Avoid strategic, passionate, detail-oriented, leverage, robust, seamlessly, delve, tapestry, synergy, cutting-edge, proven track record, I am writing to express, I am excited/thrilled to and other inflated claims. Do not add Jira, SQL, billing/finance experience or development skills not present in the authorized source.
Do not use arrows in bullets; express a sequence with then or a natural clause.

### Dates, names, structure and rendering handoff

- Name: Kun Huai Nieh. Do not infer spelling from the email address.
- Role/education ranges: YYYY-MM – YYYY-MM, with spaces around the en dash; retain Present for an ongoing role and the original directive end_date empty string.
- Narrative dates: YYYY/MM or YYYY/MM–MM. Do not mix full English month names or start a bullet with a date. Preserve exact statistical cutoff days and source-authorized quarters.
- Resume content: Summary, Skills, Work Experience, Education and Languages only; no Personal Statement/Autobiography. Preserve source directive JSON/Enum as machine metadata; do not invent missing fields.
- No Editing Notes, English Self-Review, internal instructions or editorial commentary in the candidate.
- The exported resume must fit within two pages and have visible, aligned • bullets without an orphan third page. Claude owns PDF generation, template metadata filtering, page-count/visual checks and verify_line_pdf.py/build_line_pdf.py. Codex delivers validated Markdown and does not report an unexamined PDF as passed.

### Cross-section editing and qualifiers

Summary states positioning and approach; Skills lists capabilities and tools; Experience supplies evidence and metrics. Do not repeat the same scope/result number in Summary and Experience; career tenure is an allowed summary fact.
Keep periods, denominators, comparison groups, approximations, development status, reporting channel and team attribution. Do not redefine a case-closure metric as shipped features or sales conversions. A payment-channel share is not total revenue growth.
For two app launches in one bullet, use one shared launch/marketing/overall-product-performance qualifier, with each metric clearly tied to its product and period. Avoid repeated long disclaimers, but do not remove required attribution.
Pure rewording is allowed without changing a qualifier's meaning. A source lock is not a reason to ignore every fluency problem: fix the surrounding sentence and send a concrete upstream proposal only for the locked conflict.

### English cover letters

Use one product/work context and one main line per bullet. Define unfamiliar names when retained; do not restore product names that the authorized English draft replaced with plain product types.
English bullet sections of a mixed letter target 120–150 words unless otherwise requested. Do not invent a link to the company or guarantee immediate suitability. Close with a natural invitation to discuss the relevant experience; a fully English letter must not be forced to contain the Chinese word “期待”.
Do not enforce a Chinese character limit on English paragraphs. Run a letter Gatekeeper only with the explicit language/document-type routing supported by that version; an incompatible Chinese-only check is an upstream tool conflict, not a reason to distort English.

### Isolated English review prompt and acceptance

Use a clean reviewer with no inherited history, an English-only prompt, a native-English hiring-reader role, and an English response. Provide only the complete outward-facing candidate and authorized JD. Strip non-public comments and machine directives while assembling the prompt; do not create a blind-review file in the repo. Do not provide the upstream draft, internal rules, fact library, lock lists, revision history or the other side's opinions. Record what the reviewer actually read; without a JD review, do not claim JD-fit acceptance.

> Act as a native-English-speaking hiring reader reviewing the complete candidate below. Assess clear scope and responsibility, business relevance, first-read comprehension, natural English, sentence structure and unnecessary repetition. Identify concrete wording issues and suggest concise alternatives without inventing facts, metrics, authority or outcomes. Do not read files or use external sources. Reply in English, state exactly what material you received, and distinguish genuine comprehension problems from optional stylistic preferences.

For a separate JD-fit review, keep the prompt and response in English and use only the candidate and authorized JD; do not treat lack of evidence as proof of a missing career fact. Native-language fluency review is not factual validation.
The main editor closes each finding using the disposition matrix: corrected wording with Before → After and cross-section results; rejection tied to a source fact or explicit user ruling; or an upstream lock/contract issue with exact replacement instructions. Claude is the final arbiter under the current rules, preventing preference-driven A↔B reversals. Blind review does not replace a full comparison with the designated upstream SHA. Preserve metrics and their objects, units, denominators, periods, comparison groups, responsibility, attribution, qualifiers and completion status. No Chinese impact, verb-count or formatting rubric is supplied to the English reviewer.

Run verify_line_profile.py only for the English LINE input format explicitly supported by the designated tool commit. For other English CVs, LinkedIn documents, letters and standalone bullets, wait for Claude's supported format and actual entry point. An unknown route is unsupported or unverified, not fully accepted. Never impose LINE JSON/Enum requirements on unrelated English documents.

Verify required text fields contain actual candidate content, actions/Enums match the declared contract, and anchors occur in the intended body rather than comments. A checker may miss these errors; Exit 0 does not prove that a candidate is complete, semantically faithful, compatible with a generator or acceptable as a PDF. Record source and tool commits separately, along with the actual command and Exit Code.

Do not rewrite natural English merely to meet a similarity threshold or fixed anchor, reinsert redundant facts, or restore an obsolete parser format. Keep a reasonable candidate and send false positives or missed errors to Claude using minimal synthetic input, expected and actual behavior, tool commit, arguments and Exit Code. Do not modify the validator or fake input. An unpassed tool remains unpassed; any early candidate handoff requires the user's explicit direction.

Report four separate results: script execution; complete-candidate expression and cross-section review; semantic comparison with the designated upstream; and actual conversion/PDF execution and acceptance. Claude owns conversion and PDF review. Without an actual run and inspected artifact, mark those results unverified; a name-only or placeholder PDF is not evidence of acceptance. For rule-only maintenance, review rules and routing only, without altering resumes or claiming any candidate review, blind review or PDF check.
