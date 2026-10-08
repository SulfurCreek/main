<!--markdownlint-disable MD013-->

# career/library — 使用者提供資料庫（現行事實的唯一入口）

> 建立：2026-10-08（Repo Steward 健檢後重建）。⚠️ 個人職涯資料，不外流 HackMD（見 [`../CLAUDE.md`](../CLAUDE.md) 硬規則二）。

**為什麼有這一層**：使用者在不同日期口述、確認、更正過的事實，原本散在 F 頁、evidence 頁、104 檔與 commit message 裡，而且是「逐次疊加」——舊說法沒刪、新說法附在後面。session 讀到前段就停，於是一再寫回已被更正的內容（主導 Peach／JD2、零停機、Spearheaded…）。library 把**目前有效**的版本收成一處。

## 讀取順序（衝突時上面優先）

1. **library/**（本目錄）——使用者確認過的現行事實與裁定
2. `style/resume-voice-zh.md` §7 角色定位鐵則（寫法層面的最高規則，library 的 [decisions](decisions.md) 已摘錄）
3. `wiki/` F 頁與 evidence 頁——細節與證據原文（可能含舊層，與 library 衝突以 library 為準）
4. 104／信件／作品集等產出檔——都是下游，**不得當事實來源**

## 檔案

| 檔案 | 內容 | 何時讀 |
| :--- | :--- | :--- |
| [`profile.md`](profile.md) | 個人基本資料、時間軸、職稱、匯報線、年資、學歷、證照、語言、求職條件 | 任何履歷／信件／作品集開工前 |
| [`facts-1111.md`](facts-1111.md) | 1111 期間可用的事實與數字（含口徑與使用限制） | 寫 1111 段 |
| [`facts-prior.md`](facts-prior.md) | 尚凡／思維特期間的產品、角色、數字（已整合 10/04–10/08 的所有更正） | 寫前段職涯 |
| [`decisions.md`](decisions.md) | 使用者裁定：角色定位、禁用詞、保密範圍、對外抽象化、語氣 | 每次動筆前 |
| [`superseded.md`](superseded.md) | 已被推翻的舊說法 → 正確說法（防倒退清單） | 審稿、改舊稿時 |
| [`open-questions.md`](open-questions.md) | 尚未確認、不可自行補齊的項目 | 遇到〔待補〕時；問使用者前先查 |

## 維護規則

- **新事實先寫 library，再改下游**。使用者口述、確認、更正任何事，當下寫進對應檔，每條附 `日期｜來源`（來源＝對話日期、wiki 檔或 commit SHA）。
- **被推翻的條目不刪**：移到 [`superseded.md`](superseded.md)，寫明取代它的新說法與日期。
- **不推測**：缺資料就留在 [`open-questions.md`](open-questions.md)，產出裡標〔待補〕。
- **只收使用者提供／確認的事**。session 自己的推論、建議寫法不進 library（放 `style/` 或 review 檔）。
- 原始資料檔（Numbers、Excel、截圖、簡報）**不進 repo**，只記萃取後的數字與出處描述。

## 稽核紀錄

- **2026-10-08 第一次稽核**（使用者指出交付鏈與技術素養「早就提供過」）：重建時只收了 10/04 之後對話中的更正，**漏收** `competency-framework.md`、F01、F02、F05、F06、F07、F15、`resume-extract.md`、`prior-roles.md`（舊履歷）、`104/resume-104.md` §6 裡的既有能力與方法。已補進 `facts-1111.md` §4、`facts-prior.md`〈方法與能力〉、`profile.md` §4。
- **之後規則**：library 不只收「更正」，也要收「使用者提供過的能力、方法、產出物」；每次重建或大改後，對照 `competency-framework.md` 與 F01–F15 檢查一次覆蓋。
