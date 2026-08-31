<!--markdownlint-disable MD033-->
<!--markdownlint-disable MD013-->

# 逆向模式：日常產出 → XYZ 影響力 bullet（含 NVIDIA-tier 深技術版）

> 回 [`../SKILL.md`](../SKILL.md)。

「正向」是框架 → 履歷；「逆向」是把一段**日常產出**（規格書、週報、Figma、工單紀錄、流程圖）反推成履歷 bullet。
扮演角色：**精通矽谷科技業標準的資深獵頭／履歷教練**。

## 三步驟

1. **職能萃取**：從產出中用到的**工具與思維**（Mermaid／循序圖、Markdown 規格、權限代碼建模、Kanban 工單治理、
   資料結構重構…）反推對應 PM 職能，並**對映回 F1–F11**——不要發明新職能，先連回框架。
2. **XYZ 句型重構**：`達成／主導 [X 影響力或產品模組]，透過 [Z 技術／管理方法]，解決了 [Y 複雜度或痛點]`。
   等價於 Google XYZ：*Accomplished [X] by doing [Z], solving [Y]*。**X＝結果、Z＝方法、Y＝痛點／複雜度**。
3. **技術 × 商業雙語轉譯**：同一條 bullet 同時帶**商業價值**（營收保護、續約、降低溝通成本、定價策略）與
   **技術含金量**（API 串接邏輯、防呆機制、資料結構重構、狀態建模），並產出**中英兩版**。

### 輸出格式

- **【原產出概述】**：一句話描述輸入素材。
- **【展現的核心職能】**：2–3 個 PM 關鍵能力（標註對映 `F#`）。
- **【履歷黃金亮點】**：**3 種動詞強度**的選項（穩健 → 進取 → 主導），讓使用者挑語氣。

> ⚠️ **誠實護欄**：XYZ 的 X／Y 若無真實數字，用**代理指標**（規模／速度／廣度／流程改善）或保留 `〔待補數據〕`，
> **絕不為了句型漂亮而編造**。技術詞也須屬實——手繪 vs AI 輔助、`contributed` vs `led`、結案率有來源才寫。

### 範例（取自 F11 維運工單）

- **【原產出概述】**：每週求才系統週報——工單量統計＋已上線／待上線清單；工單幾乎全來自付費中廠商。
- **【展現的核心職能】**：問題解決與維運交付（F11）、利害關係人溝通（F9）、根因分析（F11／F2）。
- **【履歷黃金亮點】**
  1. （穩健）*Resolved 1,279 paying-customer support tickets at ~88% close rate via a ticket→Kanban→launch loop, protecting account experience and renewals.*
  2. （進取）*Drove a ~88% close rate across 1,279 paying-account tickets by standing up a ticket→Kanban→launch ops loop with root-cause fixes — safeguarding the sales team's revenue retention.*
  3. （主導）*Owned recruit-system operations end-to-end as single intake, clearing 1,279 paying-customer tickets (~88% closed) through root-cause remediation (matching engine, AI recommendations, code-table overhaul) to defend renewal revenue.*
  - 中文（主導版）：**主導**求才維運單一窗口，以「工單→Kanban→上線」閉環與根因修復清理 **1,279 張付費廠商工單（~88% 結案）**，守住續約營收。

---

## NVIDIA-tier 深技術逆向優化 / Deep-tech zero-fluff escalation

應徵**硬技術公司／技術型 PM**（NVIDIA、平台／基礎設施、infra）時把 XYZ 再升一級。
扮演：深諳 NVIDIA 價值觀（**Intellectual Honesty、Deep Tech Competence、Speed & Agility**）的首席技術獵頭。
四個模組依序跑：

**① NVIDIA-Tier XYZ（含技術轉譯）**：過濾所有空泛修辭，盤點真實技術細節（API 協議與端點、系統代碼對照、
欄位規則、驗證邊界），再套 XYZ——**X**＝具體系統優化／商業規模、**Y**＝克服的歷史包袱或架構限制、
**Z**＝制定的核心系統規範或技術路徑。

> 技術轉譯範例：「管理資料庫追蹤狀態」→「**主導資料追蹤邏輯重構，確立主識別碼純粹化（無後綴）規範，
> 並將追蹤狀態隔離至獨立資料表，提升底層正規化與擴充性。**」

**② SOAR 專案故事框架**（跨系統整合／代碼整併／跨部門協調用；比 STAR 多「阻礙」、凸顯張力）：
**S** 系統痛點／業務目標 → **O** 技術或溝通阻礙（舊代碼與新需求不相容）→ **A** 具體解法（用 Mermaid 梳理
API 序列邏輯、產出 Markdown 規格與新舊代碼對照表）→ **R** 量化或質化成果。

**③ 技術 × ATS 最佳化**：純文字 bullet、無雙欄／複雜表格／圖示；**強制保留高含金量技術關鍵字**
（API 整合協定、Mermaid 流程視覺化、狀態機、向後相容遷移、多因素驗證之邊界條件與冷卻防呆機制）。

> ⚠️ 對外抽象化：可寫「整合兩條 legacy 通道為單一即時對話流」，但**勿外露** 1111 內部 API 名、欄位名、權限代碼。
> Intellectual Honesty ≠ 揭露機密。

**④ 矽谷級 PM 嚴格自審（出稿前必過）**：

1. **動詞強度**：開頭為強主動語態（Architected／Orchestrated／Spearheaded／Formulated）？
2. **商業 × 技術平衡**：同時展現前端介面／後端串接理解 ＋ 對定價模型／商業化策略的敏銳？
3. **Zero-Fluff**：剔除「成功地／大幅地／successfully／significantly」，全以系統機制或商業事實取代？

### 輸出工作流（依序）

1. **【技術深度與職能盤點】**：2–3 項核心 PM 職能（標 `F#`）。
2. **【SOAR 專案故事摘要】**：≤50 字重建挑戰與解法。
3. **【Nvidia-Tier 履歷亮點】**：3–5 句 ATS 相容 bullet，提供不同動詞強度供選；
   每句含**具體資料流向／系統機制／計價模型**。

### 範例（旗艦專案：跨系統聯絡人才，已抽象化）

- **【技術深度與職能盤點】**：跨系統即時訊息架構（B↔C，F3）、雙來源訊息流合併與路由建模（F10）、
  欄位級 API 規格與向後相容遷移（F2）。
- **【SOAR 摘要】**：即時通與信件兩條 legacy 通道分裂、跨兩系統兩後端不相容（S／O）；以即時推送統一對話流、
  定義訊息封包與 6 步收發鏡像、iframe 漸進遷移（A）；零中斷上線、消除跨系統同步斷點（R）。
- **【Nvidia-Tier 履歷亮點】**
  1. *Architected a cross-system real-time messaging layer unifying two legacy channels (instant messaging + mail) into one conversation stream over WebSocket, with a hub/method/argument message envelope and read-receipt sync across both platforms.*
  2. *Formulated end-to-end API and field-level contracts plus an invitation state machine and a mirrored six-step send/reply pipeline, enabling engineers to deliver cross-system push without ambiguity.*
  3. *Orchestrated backward-compatible cutover — bridging legacy lightboxes via embedded iframes — so no existing recruiter workflow broke during migration.*
