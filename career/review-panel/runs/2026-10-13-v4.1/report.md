<!--markdownlint-disable MD013-->

# 規準 v4.1：v9.4 與 v8.1（事實修正版 v8.1c）驗證　2026-10-13

> **本次是評分器改進與模型內部檢查，不能證明招聘成功率提升。** human_calibration: not_performed；ATS import: not tested；PDF 只驗文字層（見 v4 報告 §5，本次未改）。
> 規準：`career/review-panel/rubric-v4.md`（rubric_version 4.1）＋`rule-registry-v4.1.json`（HR01–HR12）＋`research-registry-v4.1.json`（50 筆來源）。審查模型 Opus 子代理（無法鎖版）；原始輸出、提示雜湊：`raw/`。第一次啟動 16 輪全數因用量上限失敗（technical_failure，無輸出），額度重設後全部重跑。
> 職缺：Gogolook Senior PM（Anti-Scam BU／2B），**job_input: summary**；本次沒有平台欄位、求職信或附件。可見性壓力測試未重跑（規準修訂不影響遮罩請求），沿用 `runs/2026-10-13-v4/`。

## 1. 結論：平手（兩版都建議面試）

| | v9.4 | v8.1c |
| :-- | :-- | :-- |
| 招聘決定（5 輪） | **interview 5** | interview 4、clarify_first 1 |
| Level | 7 × 5 | 7 × 4、8 × 1 |
| 維度 | 決策 強×5；ownership 強 1／足夠 4；其餘足夠 | 決策 強×5；readability 強 1／足夠 4；其餘足夠 |
| 資深能力 | 交付強、PO 協調強、方向與資源 **足夠×5** | 同左 |
| 兩兩比較（甲乙交換 4 輪） | **無明確偏好 4／4**，未順序敏感 | 同左 |

v4.1 加入人資十二問後，兩版的差異更小：v4.0 時「方向與資源」v8.1c 是待補×5，這次兩版都是足夠×5。比較審查者 4 輪一致：**v9.4 的長處在衡量與歸因的校準，v8.1c 的長處在決策案例的可見性；都不構成能力差異。**

## 2. 人資十二問（各 5 輪狀態）

| 題 | 問題 | v9.4 | v8.1c |
| :-- | :-- | :-- | :-- |
| HR01 | 與這份工作的直接關聯 | partial×5 | partial×5 |
| HR02 | 最近在做什麼、環境異同 | supported×5 | supported×5 |
| HR03 | 本人做了哪部分 | **supported 4**、partial 1 | supported 2、**partial 3** |
| HR04 | 留下什麼可確認的改變 | supported×5 | supported×5 |
| HR05 | 面對限制如何判斷 | supported×5 | supported×5 |
| HR06 | 責任與方向如何演變 | supported×5 | supported×5 |
| HR07 | 技能是否用過 | partial×5 | partial×5 |
| HR08 | 能否容易找到重點 | supported×5 | supported×5 |
| HR09 | 哪些聲明需面試核對 | partial×5 | partial×5 |
| HR10 | 下一步方向與職位相容 | partial×5 | partial×5 |
| HR11 | 工作條件衝突 | supported 3、partial 1、unknown 1 | supported 2、partial 2、unknown 1 |
| HR12 | 足以支持面試？ | supported×5 | supported 4、partial 1 |

唯一有方向性的差異是 **HR03 本人角色**：v9.4 寫出帳號冒用事件中自己統籌的範圍、Juicy 的歸因說明，審查者較能分辨個人貢獻。

## 3. 兩版共同缺口（決定面試信心的不是版本差異）

HR01／HR07 都是 partial 的原因相同（≥3 輪）：
1. **英語**：只有 TOEIC／TOEFL 分數，沒有工作中使用英文的例子（JD 明文必要條件 → partial／unknown，不阻擋面試）。
2. **SQL／BI 自行查詢**：只有 GA4、Excel、世代分析等名稱，沒有「自己查什麼、得出什麼」。
3. **B2B／B2G 年資**：招募系統是 B2B，2022/08 起約 3 年多；無政府或海外企業客戶。
4. **防詐動機**：未寫（unknown；不推論沒有意願）。
5. **50 項大項的個人／團隊邊界**、**之後未再出現的監測來源**、**Peach 付款占比＝渠道組成**：面試追問，不是扣分。

**blocking 0 筆**；每個 issue 都帶了 rule_id 與 source_ids（96/96）。

## 4. 迴歸結果（v4.1 新增部分）

| # | 案例 | 結果 |
| :-- | :-- | :-- |
| 17 | 換掉姓名與所有雇主名（v9.4anon ×2） | ✅ interview×2、Level 7／8、HR03 supported×2；沒有因名氣下降 |
| 21 | 新鮮人規範 vs 資深 PM | ✅ 12 輪 0 筆把頁數、學歷、學校、空窗、任職長度列為缺失 |
| 9 | 交換甲乙順序 | ✅ 4 輪皆無明確偏好，未翻轉 |
| 6 | 未上線案例 | ✅ 比較審查者明說「只能支持決策品質，不能算成果」 |
| 16、18（語義）、19、20 | 空窗變體、移除頻率數字、平台欄位、104 未讀 | ⏸ 未跑或僅規則層通過（見 `regression-v4.md`） |

確定性測試 13/13 通過。

## 5. 下一步

1. **版本選擇**：模型審查下兩版同檔，選哪版是編輯決定。v9.4 衡量較穩、v8.1c 決策案例較多，合併是最直接的改善。
2. **真正會改變面試信心的是共同缺口**（英語使用場景、自己做的數據分析、B2B 客戶對接）——需要你提供事實，不能為了得分補寫。
3. **真人校準**仍未做：找 1–2 位 HR／用人主管用同一 JD 獨立判讀，才能知道模型和真人的落差。
