來源：上游 41cba67 對應推薦信 r1、職缺全文；voice_style_guide.md §2 七準則。
〔待補〕：無；Yahoo A／B 尚待本人選用。
事實疑問：無新增。

# 91fp9-Yahoo

## 方案 A

```text
您好：
應徵貴司 [R78] (Sr.)Product Manager 產品經理。我有近 10 年產品經理經驗，現任人力銀行企業端招募系統 Product Owner，以 AI Agent 協作規格撰寫與資料分析。以下是三項相關經驗：

‧ For specs and data analysis, I use AI agents including Antigravity and Claude Code. I define the problem, rules and verification requirements; the agent checks data and flags confidence, while a person makes the final decision. I documented the method as a reusable skill and taught a colleague to apply it to large datasets.
‧ In our recruitment system, I led the launch of AI-generated job descriptions and AI talent recommendations. With the data science team, I defined use cases and acceptance criteria. Employers confirm content before publication; recommendation rules reflect clients' actual selections.
‧ Employers and job seekers use two overlapping messaging tools. I am planning an integrated flow in response to 199 client requests accumulated since 2021. The work is still in development.

期待與團隊交流 AI Agent 與訊息平台，分享規劃及帶同仁使用 AI 的實務經驗。謝謝您的閱讀。
聶崑淮
```

## 方案 B

```text
您好：
應徵貴司 [R78] (Sr.)Product Manager 產品經理。近10年產品經理經驗，現任人力銀行企業端招募系統Product Owner。

‧ 撰寫規格與分析資料時，使用 Antigravity、Claude Code 等 AI Agent。我定義問題、規則與驗證要求，讓 AI 檢查資料並標示把握程度，由人判斷；將做法整理成 skill，教同仁用這套方法處理大量資料。
‧ 主導招募系統的職缺工作說明生成與AI推薦人才上線，與資料科學團隊定義使用情境與驗收標準。內容經企業確認才刊登，推薦規則依客戶實際選用調整。
‧ 企業與求職者使用兩套功能重複的訊息工具，我正規劃整合流程，回應2021年起累積的199件客戶建議，目前開發中。

期待與團隊交流AI Agent與訊息平台，分享規劃及帶同仁使用AI的經驗。謝謝。
聶崑淮
```

## 修改紀錄

- 先交代支付、系統改版或 AI 使用場景，再接動作及成果；保留數字與上游責任。
- 結尾改期待交流；不新增公司觀察。三個條列各保留一條主線。
- 保留人為最終判斷、企業刊登確認與訊息整合開發中，未暗示工程實作或職缺要求但未具備的工具經驗。

## 驗證與盲審

A 英文三點 123 words，整封 832 字元；B 全文 347 字元（含標點、英數，不含空白）。兩案各三點；上游 verify_letter.py 以指定職缺名驗收，0 違規。近 10 年、2021 年起、199 件及開發中均保留。

獨立子代理 two_letters_blind 僅讀正文。已修 B 的省略：明寫 AI「檢查資料」，以及教同仁「用這套方法」處理大量資料。A 的主詞與方法對應清楚，未發現待修問題。無上游鎖定阻擋；未宣稱獨立事實查證。
