<!--markdownlint-disable MD013-->

# 使用者裁定（寫法、保密、定位）

> 這些是使用者明說的決定，不是 session 的建議。要推翻只能由使用者本人裁示，裁示後把舊條移到 [superseded](superseded.md)。

## 1. 角色定位（最高優先，2026-10-06）

- 寫成**規劃者、協作者、驗收者、時程掌控者**；不寫工程實作（不寫「開發」「實作」「架構」「Architected」）。
- 技術專案寫「全盤掌握」：影響評估、上線範圍與時程、驗收、對客服說明、回饋收斂。
- 跨國團隊寫「協作」：SweetRing 實習生不是下屬。
- 來源：`style/resume-voice-zh.md` §7、`wiki/soft-skills.md`〈角色定位〉

## 2. 語氣（2026-10-06 回饋、2026-10-08 anti-AI 規範）

- 技術詞太多 → 一般 PM 職缺用白話；HMAC、MECE、SSOT 等只在投技術型 PM 時保留。
- 軟實力寫成句子裡的動作，不寫「具備溝通能力」。
- 去 AI 感＋ATS：見 `style/anti-ai-ats.md`（與本頁 §1 衝突時以 §1 為準）。
- 來源：`style/resume-voice-zh.md` §6、`style/anti-ai-ats.md`

## 3. 命名與對外抽象化

| 項目 | 裁定 | 日期 |
| :--- | :--- | :--- |
| JD2 | **禁用**，寫「JustDating 重新上架版」 | 2026-10-06 |
| JC | 正式名稱 **Juicy** | 2026-10-05 |
| JD 生成 | 對外寫「職缺工作說明生成」 | `style/resume-voice-zh.md` |
| E.1 | 對外寫「信件與即時通整合」「開發中」 | 同上 |
| 職稱 | 「1111人力銀行招募系統 Product Owner」或「Product Owner／PM（職稱：產品企劃主任）」 | 同上、v5.1 |
| 作品集對外版 | 保守預設：不寫公司名（「某大型求職平台」）、不寫 HackMD／內部 wiki／RAG、時間線只寫年資級距；使用者放寬才記入 `portfolio/public/STATUS.md`〈使用者決定〉 | 2026-10-05 |

## 4. 保密與誠實

- **career/ 內容絕不寫進 HackMD**（`../CLAUDE.md` 硬規則二）。
- 營收、分潤金額不寫；KOOL DAU 不寫；創作者個資不寫。
- 原始資料檔（Numbers、Excel、截圖、簡報原檔）不進 repo。
- 不捏造數字：本 library 沒有的數字一律標〔待補〕。
- 規模脈絡（全站廠商數、暢銷榜）≠ 個人貢獻，不能寫成個人成果。
- 「零停機」禁用（見 [facts-1111](facts-1111.md) §3）。

## 5. 0→1 代表作與排序（2026-10-06）

- 0→1 代表作＝JustDating（重新上架版）與 KOOL；Peach 次要。
- Peach 付款管道轉移可寫，但不是首推代表作。

## 6. 平台分流

- 104 與 Cake Resume 分開；104 規格（欄位、字數）不得套到 Cake。路由見 `../CLAUDE.md`〈履歷平台路由〉。

## 7. PM 交付鏈與產出文件必須呈現（2026-10-08，最高優先之一）

- 「少用技術詞」≠「不提產出文件」。履歷與作品集**必須**看得到使用者的完整交付鏈與產出物。
- 交付鏈（使用者口述順序）：User Journey Map → User Story → Use Case → SA（系統分析、流程與資料盤點）→ Flowchart／Sequence Diagram → Wireframe → 與 UI/UX 協作 → 製作 Prototype → 向 Stakeholder 匯報 → Spec 文件 → 與工程師跑專案流程、追時程 → 開發完成後與 QA 協作 → 安排上線計畫 → 完整交付。
- 這些是**產出物名稱**，不是工程術語，一般 PM 職缺也要寫；工程實作詞（開發、實作、架構）仍依 §1 禁用。
- 寫法：至少一條條列呈現「定義」段（Journey → Spec），一條呈現「交付」段（追時程 → QA → 上線）；技能欄列出產出物。
- 來源：2026-10-08 使用者對話（「之前說不要有太多技術用語，但不代表不要提到我產出的文件」）

## 8. 履歷標準工作流程（2026-10-08 使用者裁定，取代先前「改稿＝刪修上一版」的做法）

八步，依序、不跳步：

1. **調用職能**：讀 library、`competency-framework.md`、F01–F15，列出本次要涵蓋的職能與交付鏈。
2. **蒐集證據**：每個職能配事實、數字、口徑、出處；缺的先問使用者，答覆先寫 library。
3. **每個項目寫成小 essay**：先寫完整，不管長短，保留情境、決定、做法、結果、自己負責與不負責的部分。
4. **精簡**：用 resume-craft 把 essay 轉成履歷文字；被拿掉的細節移到自傳或面試備忘，不丟。
5. **檢測讀者的 AI 感受、去 AI 化**：用讀者角度看 AI 腔，改到像本人寫的。
6. **HR 檢測**（resume-review-panel：人資 H1–H10＋HR 清單）。
7. **用人主管檢測**（HM 清單，含交付鏈覆蓋）。
8. **定版產出**：通過閘門、使用者核可措辭後，才產 txt／PDF、歸檔舊版、更新指標。

- 順序：HR 先、用人主管後（2026-10-08 使用者指定）。
- 不得只拿上一版刪修；不得為了審查分數犧牲職能覆蓋（見 `style/postmortem-2026-10-08-deliverables.md`）。
- 來源：2026-10-08 使用者對話

## 9. 使用者提供過的外部 skill 與採用狀態（2026-10-08 稽核補記）

| 外部 skill | 提供日 | 採用 | 不採用（理由） | 落點 |
| :--- | :--- | :--- | :--- | :--- |
| `cv-resume-optimizer`（雙語履歷＋自傳、問診模式） | 2026-10-02 | 自傳每段 ≤ 4 行／空行／不寫家庭背景、前 90 天（須從 JD 推出）、繁中 bullet 結果前置、英文版畢業年份提醒、缺資料一次問一題；另補「轉換動機」 | 技能分 Languages／Frameworks（PM 用職能叢集）、工程式範例 bullet（越權宣稱）、bullet 禁粗體與句號、只輸出不講話 | `resume-craft/assets/template-tw-zh.md`、`references/tw-voice.md` |
| `pm-portfolio-creator` | 2026-10-03 | 台灣執行導向案例範本、TL;DR／假設／優先級、NDA 去識別（用級距不用假資料）、Mermaid 照柔色系 | 開場問卷、「可用於 HackMD」（違反硬規則二）、工程式範例 | `resume-craft/assets/portfolio-case-study-tw.md`、`references/portfolio.md` |
| `anti-ai-ats-resume-crafter`（V3、V4 Toxic HR Defense） | 2026-10-08 兩次 | 禁用詞與破折號、CAR 盤問、RACR 結果先行、職稱包裝、量級錨定、產業洗白、ATS 單欄 | 剔除 AWS／交換／遠端意願（使用者調整後保留）、反日常勞力字面解讀（decisions §7 取代）、動詞升級為「架構」「Spearheaded」（decisions §1 禁用） | `style/anti-ai-ats.md`、`resume-craft/references/anti-ai-ats.md` |

- 若使用者所說「AI resume builder」另有所指，請告知名稱；目前紀錄中只有以上三個。
- 來源：2026-10-02、10-03、10-08 使用者對話
