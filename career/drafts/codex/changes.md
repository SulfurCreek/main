# 104 v12.19 中英並列潤飾紀錄

基底：db850563768156d8cd907e227a232501c758e26b（claude/happy-lamport-ljis8c，唯讀）。
成品：104-v12.19-bilingual.codex.md。
英文唯一來源：同SHA的career/drafts/line/line-resume.md（FINAL-LOCKED）。
中文基準：同SHA的career/drafts/v12.19/104-v12.19-public.md。未改來源或工具。

## 改動句子紀錄：共1筆

### 1｜1. 個人簡介｜英文首句

**原句**

> Product Owner with nearly 10 years of product management experience spanning B2B recruitment and consumer subscription apps, with experience in account security, messaging, pricing, payments and localization.

**改後**

> Product Owner with nearly 10 years of product management experience spanning B2B recruitment and consumer subscription apps, including account security, messaging, pricing, payments and localization.

**理由**：同句重複 experience … with experience；僅將第二個連接片語 with experience in 改為 including，保留年資、範圍與能力清單。 屬本人允許的極小連接詞修補，不是新寫英文、翻譯中文、增減事實或改責任。其他句子與順序保留。

## 完全未動的14個並列欄位

- 經歷2.1 Product Owner／PM、2.2 尚凡、2.3 思維特、2.4 台灣新蛋：完整英中內容與HTML逐字不動。
- 專長3.1 AI Agent協作、3.2 產品規劃與交付、3.3 系統分析、3.4 UI/UX規劃、3.5 跨部門協作與時程、3.6 App產品與變現：逐字不動，名稱與標籤不動。
- 專案5.1 JustDating／Juicy兩次承接、5.2 KOOL、5.3 企業端招募系統全面改版、5.4 企業群組共同招募：逐字不動，名稱與標籤不動。

中文、自傳、個人特色、求職條件、所有directive與欄位名稱也完全未動。全檔核對：成品恰等於輸入只替換上述連接片語一次，連末尾空行也一致。HTML tag序列、span style、strong與段落／清單結構完全相同。

## 單輪隔離盲審及處置

代理：bilingual_native_review（全新、不繼承歷史）。母語美式英文招聘閱讀者，提示與回覆皆為英文。

只讀成品公開全文及JD概念：Senior PM／PO、產品規劃、複雜業務規則、企業流程、訂閱／支付、跨部門交付。沒有特定公司JD，不宣稱特定職缺匹配驗收。

實際讀完18個公開欄位組：15個英中並列欄位、個人特色5項、自傳全文、工作內容條件。所有英中正文完整、未截斷；工具抽取時剔除HTML註解、directive JSON、來源／排版說明等非公開中繼資料。未讀library、上游、規則或前輪意見，未新增盲審暫存檔，未派第二輪。

原始結論摘要：“The English is understandable throughout and has no major grammar errors.” 未見同欄意外重複或明顯重複句首；跨經歷／專案、簡介／專長的重用不屬同欄語病。

| 原始挑刺或建議 | 處置與依據 |
| --- | --- |
| 經歷2.1／專案5.4：extending the original company-wide or individual-account data access，建議改為adding department- or branch-level access alongside ... | ⛔ 來源限制保留。建議不是來源現有句，且alongside明說額外的並存關係，超出微修範圍，不自行判定／新增。 |
| 經歷2.2定價：建議將original-price phase寫成initial original-price phase，釐清第一次原價期 | ⛔ 來源限制保留。initial是額外限定，不是冠詞／標點修補，本輪不重寫來源句或自行調比較組。 |
| 經歷2.2／專案5.1：縮短Across both launches and their accompanying marketing campaigns directing users to the apps | 🔒 不採納。會刪去導流限定，且與既有統攝兩次上線／導流的方向相反；完整保留原句與產品整體表現歸因。 |
| 經歷2.2：將a three-phase Malaysia iOS pricing experiment改為a three-phase iOS pricing experiment in Malaysia | 🔒 不採納。可選名詞排列偏好，非新句接合硬傷；本輪不因偏好改鎖定句。 |
| 經歷2.2／專案5.2：from zero to one改成from initial concept through launch | 🔒 不採納。來源外措辭，不以盲審重新創作。 |
| 經歷2.1：15 shared category code tables改成15 shared classification tables | 🔒 不採納。換了專有對象名稱，不是連接修補；資料層詞彙依來源保留。 |
| 經歷2.1：ongoing service iterations改成ongoing product improvements | 🔒 不採納。來源外同義替換，本輪預設不改。 |

✅ 實際修正僅簡介第1筆；盲審沒有要求撤回。上述未採納與來源限制建議不計入改動筆數。

如將來本人另授權上游修句，可轉給Claude；本輪不執行：

> 基底db850563768156d8cd907e227a232501c758e26b，請先核對line-resume.md群組句“extending the original company-wide or individual-account data access”是否需明示部門／分店層級，以及定價句“versus the original-price phase”是否需加initial釐清首次原價期。盲審候選分別是“adding department- or branch-level access alongside the existing company-wide and individual-account access”及“was 65% lower than in the initial original-price phase”。只有本人確認語意且另授權修改FINAL-LOCKED來源後才採用；不得新增存取並存狀態、改數字／比較組或升級責任。本輪Codex保留原句，不把建議當成事實裁定。

## 自驗：兩支均Exit 0

工具與依賴verify_line_profile、verify_104_bilingual、line_md、fact_lock、gen_104_bilingual全部固定上述SHA，唯讀複製至/tmp/resume-db850563/career/scripts/執行；中文、英文與upstream-check基準亦取同SHA。未讀較新的工作區來源、未改上游工具。

### 1｜實際成品抽出的英文

    python3 /tmp/resume-db850563/career/scripts/verify_line_profile.py /tmp/resume-db850563/candidate-en.md --for pdf --upstream /tmp/resume-db850563/career/drafts/v12.19-bilingual/upstream-check.md

Exit 0。resume格式、pdf用途及語氣檢查通過；與上游核對數字＋單位、限定詞、狀態與LOCK_ENTITIES通過。

抽出稿由實際成品的1簡介、6專長、4經歷及4專案產生，去中文與HTML樣式，經歷列點數為9／5／3／1。為滿足驗證器的LINE格式，使用固定LINE來源metadata作驗證封套；正文全部來自成品，不以原英文稿代替候選，封套不寫回104成品。

腳本列Summary及3個經歷的人工查核：Summary僅第1筆微修；經歷是輸入雙語稿原有104排序與LINE排序不同。已逐點比對，四個經歷的英文列點集合都與來源逐字一致，沒有本輪新增句子。第一支的上游語意機械核對主要針對Summary及經歷，不能擴張成全部欄位的獨立事實驗證。

### 2｜完整雙語稿

    python3 /tmp/resume-db850563/career/scripts/verify_104_bilingual.py career/drafts/codex/104-v12.19-bilingual.codex.md --zh /tmp/resume-db850563/career/drafts/v12.19/104-v12.19-public.md --line /tmp/resume-db850563/career/drafts/line/line-resume.md

Exit 0、errors 0。中文零加工、英文先行、15欄、自傳及禁詞檢查通過。僅summary首句1處列為“已修改／需人工查核”，對應改句紀錄第1筆，不是錯誤。其餘英文仍取自原履歷。

另核對：全檔除該連接片語外逐字相同；中文與非英文區域、所有Quill span及HTML結構均不動；took part in、in development及about／nearly／more than等限定未刪。

## 未執行範圍

未產生PDF、未執行104填表或投遞。--for pdf只是驗證用途，不是PDF匯出／視覺驗收。中文自傳依104規格保留，不以LINE Resume的英文自傳限制刪除。

