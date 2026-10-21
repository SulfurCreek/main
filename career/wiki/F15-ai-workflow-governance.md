<!--markdownlint-disable MD033-->
<!--markdownlint-disable MD013-->

> 🧭 [← 職能框架首頁 / Home](../competency-framework.md)

# F15. AI 協作系統設計與治理 / AI Workflow Architecture & Multi-Agent Governance

> **履歷叢集 / Résumé cluster**：AI Product ＋ Process & Tooling
> **與 [F4](F04-ai-product.md) 的分野**：F4 是**把 AI 做成產品交付給客戶**（對外）；
> 本項是**用 AI 重構自己的工作系統並治理它**（對內）——兩者都是 AI 職能，但考的是不同肌肉。

**定義 / Definition**：把單一 AI 對話無法承載的工作量，拆解成**多條長駐、分領域、各自帶記憶與規則的 AI 工作分身**，
並設計一套治理機制讓它們不互相污染、不重複造輪、衝突可被偵測與回復。
*Decompose a workload that no single AI session can hold into multiple long-running, domain-scoped agent branches —
each with its own skills and memory — and design the governance that keeps them from colliding, duplicating work,
or corrupting shared assets.*

## 實際展現 / In practice

### 架構：一個領域一條分身

- 規模：**12 條分支（主幹＋11）、14 個常駐 session、23 個共用 skill、1 份共用規則書**。
- **拆分理由是 context 工程**：規格書查代碼、切版對 Figma、API 寫測試矩陣、履歷換人設——
  混在同一個對話裡會**規則互相污染、context 迅速塞爆**。故以**領域**為切分軸，
  每條分身各自帶自己的 skill 與 wiki 運作。
- **彼此不需知道對方在做什麼，但查得到「這件事該找誰」**——以同一份 `CLAUDE.md` 作為互相認得的路由層。

### 共用技能庫：23 個 skill，7 個工種

| 工種 | 數量 | 代表 skill |
| :--- | :--: | :--- |
| 規格文件與治理 | 4 | `spec-doc-1111`、`pm-toolkit`、`repo-steward`、`session-router` |
| 截圖與視覺標註 | 4 | `photo`、`png`、`lofi-wireframer`、`generate-component-doc-figma` |
| 前端切版與工程單 | 2 | `frontend-slicing-1111`、`frontend-change-ticket-1111` |
| API 文件與測試 | 2 | `api`、`auto-test`（OpenAPI → MECE 測試矩陣 → pytest）|
| 數據分析與報告 | 4 | `report-generator`、`one-pager`、`tabular-token-min`、`rawdata` |
| 職務分類專案套件 | 5 | `job-classification-kb`、`safe-excel-editor`、`tcode-excel-ops` 等 |
| 履歷與個人品牌 | 1 | `resume-craft` |

**技能是共用資產**：寫一次、全部分身可用；**新增前必須先查索引**確認沒人做過。

### 治理機制（這才是真正的職能所在）

- **單一事實來源（SSOT）**：共用資產（規則書、skill、wiki、健檢腳本）**只有一條分身能改**；
  其他分身要改就在 PR 描述寫「請主幹吸收」——直接改必然撞衝突且會被蓋掉。
- **重複造輪偵測，已實際攔截 2 次**：`report-generator` 與 `frontend-slicing-1111` 各被兩條分支重複產出，
  逐位元組比對後合併為一份，並把「先查索引」寫成鐵律。
- **刻意保留空殼擋重複**：`hackmd-api` 內容併入 wiki 後仍留一個空檔案，
  **目的是擋住其他分身重新造一份一樣的東西**——用結構本身預防問題，而非靠紀律。
- **職責邊界與誠實原則**：任何分身收到不屬於自己領域的請求，先查跨 session 職責對照表、
  講清楚該找誰，而不是「反正我也能做」順手接。並明文寫下能力邊界：
  > 「自動 cue」的意思是「**盡力把歸屬講清楚**」，不是「幫你轉過去」——**做不到的事不講得像做到了**。

### 事故處理：自己捅的簍子、自己抓、改機制（2026-09-11）

| 階段 | 內容 |
| :--- | :--- |
| **現象** | 三個長駐 PR（未讀提醒、CSV 統計、API 測試框架）與主幹產生真實文字衝突 |
| **根因** | 治理分身連續數次修改共用規則檔，**未回頭檢查是否撞到他人 PR** |
| **處置** | 三支分支各自 merge 主幹、共用檔一律採主幹版本、各自產出完整保留，於 PR 留言說明後結案 |
| **機制修復** | 健檢腳本從「有沒有動到共用資產路徑」升級為 **`git merge-tree` 乾跑，直接偵測現在合不合併得起來** |
| **制度化** | 寫進治理手冊：**每次改共用檔都要主動跑一次檢查**，不等使用者發現才處理 |

> 這正是 [F11](F11-problem-solving-ops.md) 的同一套閉環——**根因定位 → 機制調整 → 制度化**——
> 只是對象從產品維運換成自己的 AI 工作系統。

## 工作證據 / Evidence

本人撰寫的現場筆記《分身工作制》（Claude Code artifact，2026-09-14，Repo Steward session 產出），
含分支關係圖、13 個分身的狀態與最近產出、23 個 skill 的分類、治理規則與事故報告。
另有本 repo 可直接檢視的同一套方法：`career/wiki/` 的入口＋路由表＋分頁、
skill 的 `SKILL.md` ＋ `references/` 漸進揭露拆分。

## 資深度訊號 / Seniority signal

**這是 2026 年最稀缺的 PM 訊號之一**——不是「會用 AI 工具」，而是**設計並治理一套多代理 AI 工作系統**：
定義領域邊界、管理共用資產的單一事實來源、偵測重複建置、處理衝突事故並把修復寫回機制。

用你自己的話總結最準：

> 系統設計、任務分工、品質稽核、衝突排解、留下決策記錄——**這些本來就是 PM 的活，
> 只是這次帶的團隊是十幾條 Claude Code 分身。**

面試時這句話的殺傷力在於：它證明的不是工具熟練度，而是**把 PM 的核心職能套用到新介質上的遷移能力**。

## ⚠️ 誠實邊界 / Honest boundaries

- 這是**內部生產力系統**，不是對外交付的產品。可說「設計並治理 AI 工作流」，
  **不可**說「交付了一個 multi-agent 產品」。
- 你**沒有自建 agent 框架**——用的是 Claude Code 既有能力，你建的是**其上的治理層**（規則書、
  技能庫、路由表、健檢腳本）。這個區分要講清楚，反而更可信。
- 效益目前是**定性**的（不再重複造輪、衝突可偵測）。〔待補數據：省下的工時／重工次數下降〕——
  若能量化，這條會從「做了很酷的事」升級為「帶來可衡量的效益」。

---

**相關分頁 / Related**：[F4 AI 產品企劃（對外）](F04-ai-product.md) ・ [F7 流程標準化與工具化](F07-process-tooling.md) ・ [F11 問題解決與維運交付](F11-problem-solving-ops.md) ・ [PM 語彙對照表](pm-vocabulary-map.md)
