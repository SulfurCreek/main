# Mermaid 圖表美化與排版守則 (Mermaid Styling Guidelines)

本守則定義產出 Mermaid 圖表（包含循序圖、流程圖等）時的視覺樣式與語法標準，確保所有圖表具備高可讀性、視覺舒適，並能安全渲染。

## 1. 視覺與顏色規範 (Aesthetics & Colors)
* **柔和色系 (Pastel Colors)**：絕對避免使用高飽和度、刺眼或強烈的純色（如純紅、純綠、亮黃）。必須使用低飽和度、平易近人的柔和色調作為節點與區塊背景（例如：淺藍 `#E3F2FD`、淺灰 `#F5F5F5`、薄荷綠 `#E8F5E9`、淡米色 `#FFF8E1`）。
* **明確邊框 (Distinct Borders)**：每個參與者 (Participant)、節點 (Node) 與執行區間 (Activation box) 都必須具備清晰且對比適中的邊框。請透過樣式定義邊框的顏色與粗細（例如：`stroke:#90A4AE, stroke-width:2px`），讓圖形輪廓立體分明。
* **高對比文字**：文字顏色必須與柔和背景形成高對比，統一使用深灰或黑藍色（如 `#333333`），以達到最佳易讀性。

## 2. 語法與相容性限制 (Compatibility)
* **主流引擎相容**：為確保在多數 Markdown 平台（如 HackMD, Notion, GitHub）皆可順利渲染，請僅使用標準穩定的 `classDef` 與 `class` 語法來定義樣式。
* **禁用進階特效**：避免使用過度複雜的 HTML 標籤（如內嵌 `<div>` 或特殊 CSS 陰影），以免在支援度較低的渲染引擎中引發錯誤或解析失敗。

## 3. 防跑版排版與自我檢核 (Layout & Self-Correction)
* **控制文字長度**：若節點內的文字過長（例如複雜的 API 欄位說明），必須主動插入 `<br>` 進行手動換行，嚴禁讓單一節點被無限拉長而導致整體畫面失衡。
* **產出後自我檢核機制**：在生成 Mermaid 語法前，必須進行以下邏輯審查：
  1. **防重疊**：線條與箭頭是否有過度交錯？若有，請重新排列節點宣告的順序，或調整方向（如 `direction TB` 改為 `LR`）。
  2. **防跑版**：檢視長字串是否已妥善換行，確保圖表維持在合理的寬高比例內。
  3. **樣式確認**：確認是否已套用定義好的 `classDef` 柔和色系與邊框。

## 4. 循序圖（sequenceDiagram）專屬設定

`classDef`／`class` 語法只套用在 `flowchart`；`sequenceDiagram` 沒有 `classDef`，樣式改由 frontmatter `config.themeVariables` 注入。**配色仍是本檔第 1 節的柔和色系**，不使用冷灰／莫蘭迪色調（如 `#F4F5F7`／`#C1C7D0`／`#172B4D`／`#42526E`）——曾有分支提案採用該冷灰配色，已裁定不採用，一律沿用下方柔色系 token，維持全 repo 圖表色調一致。

於循序圖頂端強制寫入：

```
---
config:
  theme: base
  rightAngles: true
  themeVariables:
    fontFamily: "Inter, Helvetica, Arial, sans-serif"
    primaryColor: "#E3F2FD"
    primaryBorderColor: "#90A4AE"
    primaryTextColor: "#333333"
    signalColor: "#90A4AE"
    signalTextColor: "#333333"
    noteBkgColor: "#FFF8E1"
    noteBorderColor: "#FFD54F"
  sequence:
    actorFontSize: 17
    actorFontWeight: bold
    messageFontSize: 16
    noteFontSize: 15
    wrap: true
    wrapPadding: 12
    actorMargin: 70
    boxMargin: 12
    boxTextMargin: 8
    messageMargin: 42
    mirrorActors: false
---
```

* `theme: base` ＋ `rightAngles: true` 是啟用自訂 `themeVariables`／訊息線畫直角的必要開關，不是配色選擇，兩者都要保留。
* `sequence` 區塊的字級／間距是可讀性微調，不是配色：mermaid 預設字級（`actorFontSize:14`／`messageFontSize:16`）中文常態下偏小易擠，上表數值統一放大並加寬 `actorMargin`／`messageMargin` 避免文字疊行；`mirrorActors:false` 讓底部不重複畫一次參與者，減少視覺雜訊。
* **`box` 語法**：需要區分系統網域（如求才／求職／共用基礎設施）時使用，底色用低透明度 `rgba` 呼應柔色系（不要用高飽和純色）：

  ```
  box rgba(227,242,253,0.5) 求才系統 Recruit
      actor Emp as 求才廠商
      participant RF as 求才前端
  end
  box rgba(245,245,245,0.5) 共用基礎設施 Shared
      participant DB as 資料庫 (DB)
  end
  ```

  ⚠️ **box 標題不可含半形括號**——`box rgba(...) 標題` 的標題若含半形括號（如 `求才系統 (Recruit)`），mermaid 會解析失敗：整串 `rgba` 被當成標題文字、底色變 transparent（實測 mermaid v10.9）。標題一律不加半形括號，寫 `求才系統 Recruit` 即可；`participant ... as` 的別名不受此限，可正常使用括號。
* **`Note over` 標示邊界條件**：前置檢查、逾時、防呆規則、狀態轉換等關鍵條件用 `Note over` 明示，不要藏在訊息文字內；需要表達處理生命週期時可搭配 `activate`／`deactivate`。
* `autonumber` 一律開啟。

此設定與第 1–3 節的 `flowchart` `classDef` 規範互補、不衝突：`flowchart` 用 `classDef`，`sequenceDiagram` 用本節的 frontmatter config，兩者統一走柔色系。
