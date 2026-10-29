<!--markdownlint-disable MD013 MD033-->
<!--
LINE Career Profile 上游草稿 r3（2026-10-29）｜來源：104 v12.19 + library｜Career Move
給潤飾者（Codex）：
1. 只潤飾每個區塊下方的英文 Bullet Points 語感（依 career/style/voice-en.md）；<!-- @line-directive --> JSON 一個字都不要動。
2. 不改公司名、職稱、日期、數字、限定詞、Enum 代碼；不新增事實；責任詞不升級（led 僅限 decisions §51 白名單：70 項功能規劃、職缺工作說明生成與 AI 推薦人才、Juicy 推出與 JustDating 重新上架、馬來西亞定價實驗設計、KOOL 多元變現）。
3. 純英文；每個 Bullet 痛點／場景先行，不用 Backed by、句尾 , which leave…；禁用 strategic、passionate、detail-oriented、leverage、robust、seamlessly。
4. 日期一律 YYYY-MM；在職 end_date 為空字串。
5. 回傳整份 line-profile.md；修改紀錄寫於對話回覆，勿寫入本檔（不得有 Editing Notes／Self-Review 章節）。
6. 英文履歷列點省略主詞 I（全篇 ≤3）；同區塊不連續同字開頭；`For ` 開頭 ≤2 點；不抄規則備註括號（voice-en §8）。
驗收：python3 career/scripts/verify_line_profile.py <檔>
-->

# LINE Career Profile 特化版｜可填表

## 1. Basic & Contact Information

<!-- @line-directive
{
  "target_block": "basic",
  "action": "replace_all",
  "fields": {
    "email": "kunhuainie@gmail.com",
    "mobile_phone": "886-978-802-871",
    "current_position_title": "Product Owner",
    "current_employer": "1111 Job Bank (Global Chinese Co., Ltd.)",
    "country": "215",
    "address": "3F, No. 14, Lane 98, Huaide St., Beitou District",
    "city": "Taipei"
  }
}
-->

---

## 2. Work Experience (Dataset 155)

### 2.1 Product Owner｜1111 Job Bank (Global Chinese Co., Ltd.)｜2022-08 – Present

<!-- @line-directive
{
  "target_block": "work_experience",
  "index": 0,
  "action": "replace_row",
  "fields": {
    "company": "1111 Job Bank (Global Chinese Co., Ltd.)",
    "position_title": "Product Owner",
    "employment_type": "1194",
    "location": "Taipei City",
    "start_date": "2022-08",
    "end_date": ""
  }
}
-->

<!-- [STATUS: POLISHED] -->
- Product Owner of an employer-side recruitment system serving about 60,000 active paying employers (2026 Q3), covering job posting, applicant management and candidate outreach. Manage two direct-report product planners and coordinate engineering, design, sales and customer service.
- With ongoing service iterations and a full system overhaul competing for the same engineering resources, led requirements analysis and specification planning. Aligned stakeholders and secured sales buy-in before delivery, shipping about 70 major features by 2026 Q3.
- The employer-side recruitment system overhaul had to proceed without documentation of account permissions or business rules. Recovered the rules through hands-on testing and internal interviews, then coordinated phased replacement of legacy functions while keeping the existing back office, database and live service running. Of 840 related client requests, 743 (88%) were resolved.
- Because employers and job seekers used two overlapping messaging tools, interview invitations were scattered. To address 199 client requests accumulated since 2021, planned a unified messaging flow (in development). The system also limited data access to company-wide or individual scope. In response to 55 client requests since 2020/12, planned a group recruitment feature so large employers could recruit by department or branch, defining access rules across accounts, job posts and resumes, along with legacy data migration.
- After more than ten employer accounts were hijacked in 2026/03–04, coordinated engineering and customer service to determine the impact. Planned and launched new-device OTP login verification (MFA) and an account-unlock flow. No similar account-takeover incidents were reported through customer service through 2026/10.
- To lower the barrier to job posting and improve candidate matching, led the launch of AI-generated job descriptions (2024/10) and AI talent recommendations (2025/11). Guided direct-report product planners in launching company-profile generation (2026/06). Set labor-law compliance acceptance criteria requiring employer confirmation before publishing, and refined recommendation rules using employers' actual selections and feedback.
- The 15 category code tables for job roles, certifications, skills and benefits form the shared foundation for job posting, resume creation, search filtering and matching across the platform. As business growth fragmented these categories, consolidated cross-team category changes starting 2026/04. Used an AI Agent to organize mapping and delivery records, and guided colleagues in mapping hundreds of job categories with AI.
- Raised the 30-day closure rate for enterprise client proposals from 52% to 79% (2024/11–2025/10 vs. 2025/11–2026/09/20, for proposals submitted at least 30 days earlier). To protect paying employers' satisfaction and renewal base, prioritized client proposals, handled key cases directly and assigned cases to direct-report product planners. This built the product team's delivery credibility with the sales organization.

### 2.2 Product Manager｜Sunfun Info Co., Ltd.｜2018-01 – 2022-03

<!-- @line-directive
{
  "target_block": "work_experience",
  "index": 1,
  "action": "replace_row",
  "fields": {
    "company": "Sunfun Info Co., Ltd.",
    "position_title": "Product Manager",
    "employment_type": "1194",
    "location": "Taipei City",
    "start_date": "2018-01",
    "end_date": "2022-03"
  }
}
-->

<!-- [STATUS: POLISHED] -->
- Managed JustDating, the company's flagship, top-grossing subscription dating app (per public company information, long ranked No. 1 on Taiwan's dating top-grossing chart). My scope also covered Peach, a subscription content app, and KOOL, an influencer-matching platform. Planned user flows, subscriptions and payment mechanisms with engineering, design, marketing and overseas payment teams, including partnership talks with a European payment provider over video in English.
- When the App Store removed JustDating, led the launch of Juicy on the same backend to retain existing users and revenue. After Juicy was removed, led the relaunch of JustDating. Male daily active users (DAU) rose from about 3,200 to 12,500 in 6 weeks (2020/01–02) and from about 1,500 to 12,000 in 12 weeks (2020/04–06). These figures reflect overall product performance during launch and marketing traffic-routing periods.
- With no direct competitor to benchmark against, planned KOOL from zero to one by interviewing merchants' marketing teams about finding influencers on Instagram. Adapted listing and matching mechanics from Airbnb and dating apps, and mapped invitation, application and messaging flows in Miro. After the project kicked off in 2018/05, coordinated product, design and engineering to launch across iOS, Android and web. The platform accumulated about 16,000 influencer profiles and over 80,000 campaign applications in six months. Led the monetization rollout covering VIP subscriptions, a points paywall and featured exposure.
- Led the design of the Malaysia iOS pricing experiment across original, discounted and restored-price phases (2021/05–08, 21 days each), using unchanged-price Android as the control group. The price cut raised iOS non-renewal revenue by 5% (while Android fell 18%). Restoring the original price reduced iOS non-renewal revenue by 65% versus the original-price phase. The company owner adopted the lower price based on the experiment results.
- Raised web payments' share of revenue for Peach, a subscription content app, from 24% to over 80% (2020/11–2021/09) by planning the shift from in-app purchases to web payments and coordinating integration with a payment provider in Taiwan.

### 2.3 Associate Product Manager｜Sweet Tech Ltd.｜2016-06 – 2018-01

<!-- @line-directive
{
  "target_block": "work_experience",
  "index": 2,
  "action": "replace_row",
  "fields": {
    "company": "Sweet Tech Ltd.",
    "position_title": "Associate Product Manager",
    "employment_type": "1194",
    "location": "Taipei City",
    "start_date": "2016-06",
    "end_date": "2018-01"
  }
}
-->

<!-- [STATUS: POLISHED] -->
- Maintained and improved SweetRing, a dating app operating across 7 markets (US, Mexico, Brazil, Indonesia, Malaysia, Japan, Korea), including its question-and-answer feature. Also took part in localization and payment planning.
- Coordinated localization across the 7 markets, translating the app's Chinese UI text into English as the shared baseline. Then worked with up to about 10 foreign interns in English-only meetings to translate it into local languages and run local fan pages.
- Expanded payment options in Indonesia and Thailand by bringing in CodaPay, a Southeast Asian payment provider, and opening 8 payment channels (carrier billing, ATM, e-wallets, convenience stores, bank transfer). Compared fees and settlement terms, estimated net revenue, proposed 7-, 30- and 90-day subscription plans, and coordinated delivery of the Android top-up page.

### 2.4 Translation Intern (Part-time)｜Newegg Taiwan｜2014-08 – 2015-01

<!-- @line-directive
{
  "target_block": "work_experience",
  "index": 3,
  "action": "replace_row",
  "fields": {
    "company": "Newegg Taiwan",
    "position_title": "Translation Intern",
    "employment_type": "1195",
    "location": "Taipei City",
    "start_date": "2014-08",
    "end_date": "2015-01"
  }
}
-->

<!-- [STATUS: POLISHED] -->
- Translated and proofread English-to-Chinese product listings for Newegg.com.

---

## 3. Education History (Dataset 157)

### 3.1 Tamkang University｜International Business｜2010-09 – 2014-06

<!-- @line-directive
{
  "target_block": "education",
  "index": 0,
  "action": "replace_row",
  "fields": {
    "degree_name": "International Business",
    "type_of_degree": "21",
    "degree_status": "1172",
    "university": "Tamkang University",
    "start_date": "2010-09",
    "end_date": "2014-06"
  }
}
-->

### 3.2 California State University, Sacramento｜Business (Exchange Program)｜2011-01 – 2012-06

<!-- @line-directive
{
  "target_block": "education",
  "index": 1,
  "action": "replace_row",
  "fields": {
    "degree_name": "Business (Exchange Program)",
    "type_of_degree": "21",
    "degree_status": "2559",
    "university": "California State University, Sacramento",
    "start_date": "2011-01",
    "end_date": "2012-06"
  }
}
-->

---

## 4. Languages (Dataset 257)

### 4.1 English

<!-- @line-directive
{
  "target_block": "languages",
  "index": 0,
  "action": "replace_row",
  "fields": {
    "language": "10",
    "written": "1174",
    "spoken": "1174",
    "reading": "1174",
    "listening": "1174"
  }
}
-->

### 4.2 Mandarin

<!-- @line-directive
{
  "target_block": "languages",
  "index": 1,
  "action": "replace_row",
  "fields": {
    "language": "14",
    "written": "33",
    "spoken": "33",
    "reading": "33",
    "listening": "33"
  }
}
-->
