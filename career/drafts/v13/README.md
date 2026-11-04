# v13 交付說明（內部，不對外）

## PM 線 雙欄 PDF（2026-11-03）
- 來源：Codex `aa6117ac1bafe2670736cea6f5ba33eddd4fe3ee` `career/02_codex_stage/final_resume_v13_pm.md`（副本 `final_resume_v13_pm.source.md`）
- 產生：`python3 career/scripts/build_zh_pdf.py <source> 聶崑淮_資深產品經理_v13-PM.pdf '男性 DAU +48%=>iOS 男性 DAU 較原價期 +48%'`
- Claude 終審唯一修改：DAU +48% 補比較基準（Codex 回報第 3 段指出；facts-prior 第 34 行為 iOS 3,054→4,505，對原價期，不是對照組）。上游草稿已同步。
- 人工事實核對：逐點對過上游 r8，數字、日期、責任詞、限定詞一致（自動事實驗證依 PIPELINE_POLICY 停用）。
- 版面：A4 兩頁；第 1 頁簡介＋1111 六點＋專長／學歷；第 2 頁尚凡、思維特、新蛋。
- 人工邀約檢查：6 秒能讀出「訂閱／支付 PM＋能接手複雜系統」✅｜第一頁 3 個邀約理由（翻新、帳號事件、AI 上線）✅｜決策可見（不推倒重來、查根因、定價對照）✅｜數字不易誤讀 ✅｜最近經歷撐 Senior ✅

## PM 線 r9 定稿（2026-11-04）
- 來源：Codex `b2da461ce198f85003eba6ab04707fda3a057885`（上游 r9 `8f64688`）；副本覆蓋 `final_resume_v13_pm.source.md`
- 人工核對：與上游逐句 diff，只有斷句與語序差異；數字、責任詞、限定、公司改價主體皆一致。Claude 終審無修改（不再需要 --sub）
- 版面：A4 兩頁；新蛋依本人 11/03 裁定不放
- 狀態：**FINAL LOCKED**（Convergence Stop Gate；本人另行要求才重開）
