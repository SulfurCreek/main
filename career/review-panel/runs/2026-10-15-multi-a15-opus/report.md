# 多職缺驗證：v9.5 vs v9.6 × A 級 15 職缺（2026-10-15）

條件：主模型 Sonnet 5.5，審查模型 Opus 5.5（45 個新 context 子代理：A 30、B 15）；每格 1 輪。換審查模型即換測試條件，**不與 Sonnet 審查的 v9.4／v9.5 結果直接比較**。

**結論**：兩版 15/15 都建議面試；Level 中位數都是 7（v9.5：8 級 5 份；v9.6：8 級 7 份）；B 直接比較 v9.6 勝 14、無明確偏好 1（jd36），換順序偏好不變。

- Level 升降：v9.6 升 jd03、jd31、jd43（7→8）；降 jd30（8→7）。每格 1 輪，±1 在誤差內，個別升降不宜解讀。
- 維度：兩版 decision_depth 皆強 15/15、outcome_quality 與 readability 皆足夠 15/15；role_evidence 強 3→4、ownership 足夠 14→15（v9.5 有 1 份強，屬單輪波動）。
- **B 偏好有混淆**：v9.5 寫「對接 16 個需求單位」、v9.6 寫「10 個」，審查者在 jd20、jd32、jd43 都標出兩版互相矛盾。這是已知的事實更正，不是寫法優劣；Opus 偏好 v9.6 的理由中，單位數更正與 KOOL 0→1、Scrum 補充混在一起，無法拆開。
- 仍重複的缺口（兩版）：SQL／API 深度（partial）、法遵確認適法性（partial）、B2B 5–8 年與近母語英文（partial）。v9.5 的「Jira／Confluence unknown」在 v9.6 不再是缺口（已寫內部專案系統與 Scrum）。
- 方法限制：每格 1 輪、單一審查模型、JD 為摘要、無 ATS 實測與真人校準；子代理有數次 schema 補寫（HR12／HM13 缺 resume_evidence），內容未改。原始資料 `raw/`，草稿 `report-draft.md`。
