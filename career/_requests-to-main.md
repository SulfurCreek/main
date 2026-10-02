<!--markdownlint-disable MD033-->
<!--markdownlint-disable MD013-->

# 給主幹（Repo Steward）的變更請求 / Requests to main

本檔由 `claude/happy-lamport-ljis8c`（career session）依硬規則一寫入，**不自行修改** `career/` 以外的檔案。
請主幹判斷後統一施作，施作後可清空對應條目。

---

（先前兩條已施作：2026-09-16 `resume-craft` F1–F15、2026-09-29 `session_directory` session ID 兩條已由主幹於 `7a0dbee` 施作。）

## 2026-09-29：本分支殘留兩個 main 已不存在的 `spec-doc-1111` references 檔

**想改什麼**：`claude/happy-lamport-ljis8c` 上有 `.claude/skills/spec-doc-1111/references/cross-doc-and-gaps.md`、
`references/mermaid.md` 兩檔（來自舊 commit `f84d35e`），main 上已無（現行為 `cross-doc-refs.md` 等）。
merge main 不會刪掉它們。請主幹決定：直接在本分支刪除（career session 依硬規則一不能自己刪），或確認無害保留。

**為什麼**：若日後本分支任何內容被整支合回 main，這兩檔會被重新帶回，造成 skill 新舊版並存。

## 2026-09-29：`wiki/session_directory.md` career 列 session ID 換成 v3

**想改什麼**：career 列的 session ID 由 `session_01PKC4scvp58BuQxq5JKMHPw` 改為 `session_017u5Po6SGpjD3iLBZ2VL2HH`，
側欄名稱改為「Career move function definition (v3)」。分支不變（`claude/happy-lamport-ljis8c`）。

**為什麼**：v2 為載入 `CAREER_OPS_ROOT` 環境變數換手，已停止寫入；不改的話 session-router 會把 career 工作導到已停用的 session。

## 2026-10-02：`resume-craft` 吸收外部 skill `cv-resume-optimizer` 的四項規則

**來源**：使用者提供的外部 skill `cv-resume-optimizer`。我用兩種 HR 視角審過（台灣本土企業 HR、在台外商 HR），
結論是只部分採用：自傳規則與兩條市場差異規則有增益，其餘跟 resume-craft 重複，或跟它的誠實與 PM 定位衝突，不採用。

**想改什麼**（只動 `.claude/skills/resume-craft/`）：

1. **`assets/template-tw-zh.md`〈自傳〉整段換成下面這版**（原本是 4 段，段落長度沒有限制）：
   ```markdown
   ## 自傳

   <!-- 104／Cake 的 HR 多半用手機看：每段 ≤ 4 行（約 100–150 字），段落之間空一行，總長 500–800 字。
   不寫家庭背景；求學經歷只在跟職缺高度相關時寫。所有數字與上方經歷一致，沒有就標 〔待補數據〕。英文 ATS 版不放這段。 -->

   [① 破題：一句話講年資與核心定位，一句話講為什麼適合這個職缺（鏡射 JD 用語）。]

   [② 核心戰績：挑 1–2 個最難的專案，寫 問題 → 作法 → 量化結果，並交代跨部門怎麼推動。]

   [③ 轉換動機（選）：有空窗期或轉換跑道時，用一句話正面交代，不迴避。]

   [④ 落地貢獻：入職前 90 天能做的 2–3 件具體事，必須從 JD 推出來，不承諾做不到的成果數字。]
   ```
2. **`SKILL.md`〈Bullet 公式〉後面加一段「繁中在地版可用結果前置」**：
   ```markdown
   **繁中在地版可改用結果前置（Result-First）**：104／Cake 的 HR 是用掃描的，第一眼要看到成果。
   公式：`[成效] ｜ [主導的專案] ＋ [規模／方法]`。
   例：`半年 111 項上線、94% 準時 ｜ 主導 227 項求才產品 roadmap，以 P0–P3 分級與時間盒交付`。
   英文 ATS 版維持「動詞開頭」，因為 LLM 抽取 impact 靠句內因果，見 references/ats-and-ai-screening.md。
   ```
3. **`assets/template-ats-en.md` 的 Education 註解加一句**：學位取得超過 5 年，英文版不寫畢業年份（避免年齡偏見）；
   但背景調查要的正確年份仍記在 `career/wiki/education-certifications.md`，面試被問到要答得出來。
4. **`SKILL.md`〈從職能框架產出〉第 4 步改成**：遇到 `〔待補數據〕` 先問使用者，**一次只問一題**，
   優先順序是商業影響 → 規模 → 方法／工具；拿不到就保留標記，不要編。

**不採用的部分與原因**：

| 外部規則 | 不採用原因 |
| :--- | :--- |
| 技能分成 Languages／Frameworks／Tools | 這是工程師的分法；PM 用職能叢集＋證據點比較強（現行規則） |
| 範例 bullet「Architected… decoupling SignalR… latency –40%」 | PM 寫成工程架構成果屬於越權宣稱，外商 HR 面試一追問就破功，違反誠實契約 |
| bullet 內禁止粗體、結尾不加句號 | 現代 ATS 不受影響，屬於風格偏好；現行「單欄純文字」已經涵蓋 |
| 「只輸出履歷、不講任何話」 | 跟〔待補數據〕回報和交付前檢查清單衝突 |
| Intake 四題問卷 | 證據已經在 `career/` wiki 裡，只保留「缺資料時一次問一題」 |

**為什麼**：現行自傳範本沒有限制段落長度，也沒有排除無效資訊，在手機上可讀性差；台灣 HR 看自傳最在意轉換動機和即戰力，
現行範本沒有明確欄位。履歷 bullet 的結果前置能讓 104 掃描時更快看到成果。
