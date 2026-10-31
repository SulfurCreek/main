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

## 0. Professional Summary & Skills（僅供 PDF／ATS 上傳，不進表單、不屬任何 directive）

<!-- [STATUS: NEEDS_POLISH] [LOCK_ENTITIES: nearly 10 years, Product Owner, B2B recruitment, subscription apps, AI agents, human-in-the-loop, Claude Code, Antigravity] -->
- Product Owner with nearly 10 years of product management experience across a B2B recruitment platform and subscription consumer apps, covering requirements, specifications, pricing and payments, localization and cross-team delivery. Works with AI agents (Claude Code, Antigravity) on specifications and data analysis, with people reviewing and deciding the results.

<!-- [STATUS: NEEDS_POLISH] [LOCK_ENTITIES: PRD, User Story, Use Case, UAT, Axure RP, Figma, Claude Code, Antigravity, Kanban] -->
- Product planning and delivery: PRD, User Story, Use Case, process and sequence diagrams, prototypes, UAT
- Design and AI tools: Axure RP, Figma, Claude Code, Antigravity
- Working methods: Kanban, requirements analysis, stakeholder alignment, pricing experiments, payment integration planning
- Languages: English, Mandarin

---

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

<!-- [STATUS: NEEDS_POLISH] -->
- Product Owner of the employer-side recruitment system serving about 60,000 active paying employers (2026 Q3), covering job posting, applicant management and candidate outreach; manage two direct-report product planners and coordinate engineering, design, sales and customer service.
- With ongoing service iterations and a full system overhaul competing for the same engineering resources, led requirements analysis and specification planning, aligned stakeholders, and secured sales buy-in before delivery, shipping about 70 major features by 2026 Q3.
- Took over the employer-side recruitment system overhaul when account permissions and business rules had no documentation; reconstructed the rules through hands-on testing and internal interviews, then replaced legacy functions in phased releases while keeping the existing back office, database and live service running, resolving 743 of 840 related client requests (88%).
- Because employers and job seekers messaged each other across two overlapping tools that left interview invitations scattered, planned a unified messaging flow, now in development, addressing 199 client requests accumulated since 2021. In response to 55 client requests since 2020/12, planned a group recruitment feature, defining access rules across accounts, job posts and resumes plus legacy data migration, so large employers can recruit by department or branch beyond the original company-wide or individual scope.
- After more than ten employer accounts were hijacked in 2026/03–04, coordinated engineering and customer service to scope the impact, then planned and launched new-device OTP login verification (MFA) and an account-unlock flow, with no similar account-takeover incidents reported through customer service through 2026/10.
- To lower the barrier to job posting and improve candidate matching, led the launch of AI-generated job descriptions (2024/10) and AI talent recommendations (2025/11), and guided direct-report planners to launch company-profile generation (2026/06). Set labor-law compliance acceptance criteria requiring employer confirmation before publishing, and refined recommendation rules based on employers' actual selections and feedback.
- The 15 category code tables for job roles, certifications, skills and benefits are the shared foundation for job posting, resume creation, search filtering and matching across the platform. To resolve category fragmentation as the business expanded, consolidated cross-team category changes starting 2026/04, using an AI Agent to organize mapping and delivery records and guiding colleagues to map hundreds of job categories with AI.
- Raised the 30-day closure rate of enterprise client proposals from 52% to 79% (2024/11–2025/10 vs. 2025/11–2026/09/20, for proposals open at least 30 days). To protect paying employers' satisfaction and renewal base, prioritized client proposals, handled key cases directly and assigned cases to direct-report planners, building the product team's delivery credibility with the sales organization.

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

<!-- [STATUS: NEEDS_POLISH] -->
- Managed the company's flagship, top-grossing subscription dating app JustDating (per public company information, long ranked No. 1 on Taiwan's dating top-grossing chart), the subscription content app Peach and the influencer-matching platform KOOL; planned user flows, subscriptions and payment mechanisms with engineering, design, marketing and overseas payment teams, including English video partnership talks with a European payment provider.
- When the App Store removed JustDating, led the launch of Juicy on the same backend to retain existing users and revenue; after Juicy was removed, led the relaunch of JustDating. Male daily active users (DAU) rose from about 3,200 to 12,500 in 6 weeks (2020/01–02) and from about 1,500 to 12,000 in 12 weeks (2020/04–06), reflecting overall product performance during launch and marketing traffic-routing periods.
- Planned KOOL from zero to one with no direct competitor to benchmark against: interviewed merchants' marketing teams on how they found influencers on Instagram, adapted listing and matching mechanics from Airbnb and dating apps, and mapped invitation, application and messaging flows in Miro. After the project kicked off in 2018/05, coordinated product, design and engineering to launch across iOS, Android and web, accumulating about 16,000 influencer profiles and over 80,000 campaign applications in six months. Led the monetization rollout covering VIP subscriptions, a points paywall and featured exposure.
- Led the design of the Malaysia iOS pricing experiment using unchanged-price Android as the control group across original, discounted and restored-price phases (2021/05–08, 21 days each): the price cut raised iOS non-renewal revenue by 5% (while Android fell 18%), and restoring the original price reduced it by 65% versus the original-price phase. The company owner adopted the lower price based on the experiment results.
- Raised web payments' share of revenue for the subscription content app Peach from 24% to over 80% (2020/11–2021/09) by planning the move from in-app purchases to web payments and completing a Taiwan payment-provider integration.

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

<!-- [STATUS: NEEDS_POLISH] -->
- Maintained and improved SweetRing, a dating app in 7 markets (US, Mexico, Brazil, Indonesia, Malaysia, Japan, Korea), including its question-and-answer feature, and took part in localization and payment planning.
- Coordinated localization across the 7 markets: translated the app's Chinese UI text into English as the base version, then worked with up to about 10 foreign interns, in English-only meetings, to translate it into local languages and run local fan pages.
- Brought in CodaPay, a Southeast Asian payment provider, and opened 8 payment channels (carrier billing, ATM, e-wallets, convenience stores, bank transfer) in Indonesia and Thailand; compared fees and settlement terms, estimated net revenue, proposed 7-, 30- and 90-day subscription plans, and shipped the Android top-up page.

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

<!-- [STATUS: NEEDS_POLISH] -->
- Translated Newegg.com product information from English into Chinese and proofread it.

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
