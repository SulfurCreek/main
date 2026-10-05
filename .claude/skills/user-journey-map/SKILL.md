---
name: user-journey-map
description: >-
  從既有規格文件反向工程出使用者旅程地圖（User Journey Map），並記錄每個階段對應的
  HackMD 文件。當使用者要「user journey」「旅程地圖」「使用者旅程」「招募流程全貌」
  「從 sitemap 推回使用流程」，或要把一堆功能規格串成一條端到端流程時使用。
  輸出格式固定為三段式（Persona／Journey Grid／Key Takeaways & PM Action Items），
  範本見 `references/template.md`。預設角色是求才端招募人員（recruiter），
  階段骨架取自 `[求才系統] Sitemap` 的 module 順序。
---

# User Journey Map（反向工程版）

**格式以 `references/template.md` 為準（使用者 2026-09-30 指定）**，先讀它再動筆。舊版「五區＋每階段一張泳道表」已廢止。

## 三段式結構

1. **Persona**（2026-10-05 起取代原 Context，Roman Pichler Agile Persona Canvas）：
   **多 persona、不取人名**，以「公司會員狀態 `oStatus` × 帳號角色（主帳號／副帳號＋權限）」定義，persona 清單由使用者決定
   （目前 7 個：普通廠商／過期廠商／VIP 主帳號（人資窗口）／VIP 副帳號（人資）／VIP 副帳號（用人主管、分店店長）／VIP 人事助理／關權廠商）。
   順序：給下游 HTML agent 的 `<!-- [SYSTEM: UI/UX RENDERING INSTRUCTIONS ...] -->` 註解 → 說明與旅程範圍（Journey Type）
   → Persona 總覽表（廠商狀態、帳號類型、可走的旅程、主要限制）→ 各 persona 卡（引言、Details、Goals、Pain Points、可走的旅程）
   → 受限廠商類型（`organs.confirmed` 會改變旅程功能的旗標，作為疊加在任一 persona 上的修飾條件）→ 名詞。
   Journey Grid 以 VIP 主帳號為主線，其他 persona 的差異只寫在各自卡片。代碼定義一律引自 HackMD [REF] 系統代碼表（`B1j3sN-bzx`）；
   文件沒有的角色描述（如人事助理）寫 `NULL`，不自行編造。
2. **Journey Grid**：**階段在欄、泳道在列**，列固定七列、順序不可增減：
   User Actions／Touchpoints／Thoughts／Emotions／Pain Points／Opportunities／Metrics。
   - 階段沿用 Sitemap module 順序 `登入 → 首頁 → 公司 → 職缺 → 人才 → 聯繫 → 紀錄`；
     `服務`、`購買`不在主線，另開一個「支援」格組（任何階段都可能插入）。
   - **每張表最多 4 個階段欄**，超過就拆成多張同列序的表（例：表 A 登入～公司、表 B 職缺～聯繫、表 C 紀錄＋支援），
     表格上方標「階段 1–4」等範圍。
   - Emotions 列用 emoji＋一個詞（🤔 困惑／😤 挫折／😐 平靜／🙂 順利），不寫長句。
3. **Key Takeaways & PM Action Items**：Aha Moment、Biggest Drop-off Risk、Next Steps（≥2 條）。
   Aha 與 Drop-off 各**只選一個**，並說明選它的證據；Next Steps 要能直接丟給開發／設計，
   並標明對應哪個階段的哪個痛點。

**附錄（本 repo 專屬，放在三段式之後）**：階段 → 功能 → HackMD 文件對照表（shortId 連結）＋跨階段共用元件清單。
這是後續 HTML 與文件維護的索引，模板沒有這一段但不可省。

## 證據標記（三級，寫在儲存格內）

| 標記 | 意思 | 適用列 |
| :--- | :--- | :--- |
| 無標記＋來源連結 | 文件明文記載（User Story／Use Case／需求背景／會議記錄） | 全部 |
| `〔推論〕` | 依某個**已引用的**文件事實推出，必須在同格寫出依據 | Thoughts、Emotions、Metrics 建議、Opportunities 中「文件沒寫但合理」者 |
| `NULL` | 文件未載，也沒有可推論的依據 | 全部 |

規則：
- **Pain Points 與 User Actions 不准用 `〔推論〕`**——只能有文件依據或 `NULL`。痛點是事實，不是想像。
- **Thoughts／Emotions**：文件有抱怨、客服反映、改善動機才可寫，寫成 `〔推論〕「…？」`＋依據；
  沒有就 `NULL`。不可為了填滿表格而編。
- **Metrics**：只寫**指標名稱與定義**（例：「發出詢問意願後 7 日內回覆率」），標 `〔推論〕`；
  **不寫任何數字或目標值**，除非文件本身載有。
- **Opportunities**：文件已有規格的連文件（無標記）；文件沒有、由你提出的標 `〔推論〕`。
- 沿用 `US`／`US*` 標記於 Persona 與目標描述：`US`＝真實 User Story，`US*`＝套版句「以便提高求才效率」
  （只證明功能存在，不證明動機）。

## 反向工程規則

- 行動用 recruiter 第一人稱動詞（「建立公司資料」「開設副帳號」），不寫系統內部邏輯。
- 接觸點用 sitemap 的頁面名稱＋路徑；文件連結用 `https://hackmd.io/@1111-jobdocs/<shortId>`（不用內部 noteId）。
- 找證據的方法：用 `GET /teams/1111-jobdocs/notes` 取清單＋`folderPaths`，
  逐份抓內容到 scratchpad，grep `User Story|Use Case|身為|As a|需求背景|改善`，
  只保留求才端資料夾（`求才系統/`、`B.`、`C.`、`E.`、`M.`、`信件即時通合併專案/求才`）。
  原文不進 repo（`wiki/hackmd_rules.md` 規則 A）。
- 表格儲存格內換行用 `<br>`；儲存格內容過長（>3 行）就把來源連結收成 `[1][2]` 式短標，完整連結放附錄。

## 輸出

- 一份 Markdown（放 `user-journey/`，檔名 `*_journey_map.md`），順序：三段式 → 附錄。
- 動到 Mermaid 要先渲染驗證。**Mermaid `journey` 總覽圖改為選用**（放在 Grid 之前），
  分數必須註明「依文件記載的痛點多寡相對標示，非用戶研究數據」；Emotions 列已取代它的主要用途。
- 內容太長時遵守 `spec-doc-1111/references/styling.md`〈表格 vs 標題＋條列〉，
  但 Journey Grid 本身**一律用表格**（這是模板的核心）。

## 下游

- 此檔的編輯權在 HackMD 文件 session（見 `user-journey/README.md`）；HTML 化由「產生HTML報告」session 接手。
- **格式異動後兩邊要同步**：文件 session 重產 md，HTML session 再依新格式重建（舊的解析腳本吃舊格式會壞）。
