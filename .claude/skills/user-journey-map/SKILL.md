---
name: user-journey-map
description: >-
  從既有規格文件反向工程出使用者旅程地圖（User Journey Map），並記錄每個階段對應的
  HackMD 文件。當使用者要「user journey」「旅程地圖」「使用者旅程」「招募流程全貌」
  「從 sitemap 推回使用流程」，或要把一堆功能規格串成一條端到端流程時使用。
  預設角色是求才端招募人員（recruiter），階段骨架取自 `[求才系統] Sitemap` 的 module 順序。
---

# User Journey Map（反向工程版）

## 格式（業界通用骨架，NN/g／Miro／Smaply 共通）

一份地圖固定五區，由上而下：

1. **Persona＋情境**：誰（角色、帳號身分）、要達成什麼、預期。只寫一個 persona；
   主帳號／副帳號、VIP／免費等差異放在「變體」小節，不另開地圖。
2. **階段（Stages）**：由左到右的高階步驟。1111 求才端直接用 Sitemap module 順序
   `登入 → 首頁 → 公司 → 職缺 → 人才 → 聯繫 → 紀錄`；`服務`、`購買`不在主線，
   列為「支援泳道」（任何階段都可能插入）。
3. **每階段五列（泳道）**：目標／行動（actions）／接觸點（頁面 URL）／想法與情緒／
   痛點。
4. **機會點（Opportunities）**：每個痛點對應的改善，已有規格的連文件。
5. **文件關係**：階段 → 功能 → HackMD 文件（含 shortId 連結）的對照表，
   外加跨階段的共用元件（Modal／Lightbox）清單。

## 反向工程規則

- **證據優先**：行動、痛點、機會點都要能指回某份文件（User Story／Use Case／
  需求背景／「本次改善」段落／會議記錄）。每列附 `來源` 連結。
- **沒有證據就標 `NULL`**，不要自己編情緒或痛點（CLAUDE.md 跨文件比對規則）。
  情緒曲線只在有文件記載抱怨／改善動機時才標，其餘寫 `NULL（文件未載）`。
- 行動用 recruiter 第一人稱動詞（「建立公司資料」「開設副帳號」），不寫系統內部邏輯。
- 接觸點用 sitemap 的頁面名稱＋路徑；文件連結用
  `https://hackmd.io/@1111-jobdocs/<shortId>`（不用內部 noteId）。
- 找證據的方法：用 `GET /teams/1111-jobdocs/notes` 取清單＋`folderPaths`，
  逐份抓內容到 scratchpad，grep `User Story|Use Case|身為|As a|需求背景|改善`，
  只保留求才端資料夾（`求才系統/`、`B.`、`C.`、`E.`、`M.`、`信件即時通合併專案/求才`）。
  原文不進 repo（`wiki/hackmd_rules.md` 規則 A）。

## 輸出

- 一份 Markdown（放 `user-journey/`，檔名 `*_journey_map.md`），先放 Mermaid
  `journey` 總覽圖，再放各階段表格與文件關係表；動到 Mermaid 要先渲染驗證。
- 階段 × 泳道適合用表格（短、同形）；單一階段內容很長時改 `####`＋條列
  （見 `spec-doc-1111/references/styling.md`〈表格 vs 標題＋條列〉）。
