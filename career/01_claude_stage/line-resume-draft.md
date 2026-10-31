<!--markdownlint-disable MD013 MD033-->
<!--
LINE Resume 上游草稿 r1（2026-10-31）｜針對 LINE Taiwan Product Manager (Messenger & OA Products)（官網 /jobs/3106/）與 LINE Pay Product Planner（官網 /jobs/2782/）｜Career Move
本檔是「LINE Resume」特化版，不是通用版（通用版＝line-profile.md）。
給潤飾者（Codex）：
1. 事實基準＝本檔指定 SHA 的完整內容與各段 LOCK_ENTITIES／LOCKED；不讀 library、applications、SKILL.md。
2. 本輪改動只有「排序與強調」：1111、Sunfun、Sweet Tech 的列點順序依兩個職缺重排（帳號安全、訊息、AI 與合規、定價實驗、支付優先）；§0 摘要加入 account security、messaging。
3. 只潤飾標 NEEDS_POLISH 的區塊：語感、節奏、跨欄去重。重排後請確認每點開頭仍有獨立場景主詞、不依賴前一點的定義。
4. 不改公司名、職稱、日期、數字、限定詞、Enum；不新增事實；責任詞不升級（led 僅限 decisions §51 白名單：70 項功能規劃、職缺工作說明生成與 AI 推薦人才、Juicy 推出與 JustDating 重新上架、馬來西亞定價實驗設計、KOOL 多元變現）。
5. directive JSON 一個字都不要動；directive 註解不要複製進檔頭。
6. 英文履歷列點省略主詞 I（全篇 ≤3）；同區塊不連續同字開頭；For 開頭 ≤2 點；不抄規則備註括號（voice-en §8）。
7. 回傳整份檔；修改紀錄與盲審摘要寫在對話回覆，勿寫入本檔。
驗收：python3 career/scripts/verify_line_profile.py <檔>
-->

# LINE Resume｜Messenger & OA／Payments Product Planning 特化版｜可填表

## 0. Professional Summary & Skills（僅供 PDF／ATS 上傳，不進表單、不屬任何 directive）

<!-- [STATUS: NEEDS_POLISH] [LOCK_ENTITIES: account security, messaging, nearly 10 years, Product Owner, B2B recruitment, subscription apps, AI agents, human-in-the-loop, Claude Code, Antigravity] -->
- Product Owner with nearly 10 years of product management experience spanning B2B recruitment and consumer subscription apps, with work in account security, messaging, pricing experiments, payments and localization. Translate business requirements into specifications and coordinate cross-team delivery. Apply AI agents (Claude Code, Antigravity) to specification writing and data analysis within a human-in-the-loop workflow, with human review and final decisions.

<!-- [STATUS: LOCKED] [LOCK_ENTITIES: PRD, User Story, Use Case, UAT, Axure RP, Figma, Claude Code, Antigravity, Kanban] -->
- Requirements and validation: requirements analysis, PRD, User Story, Use Case, process and sequence diagrams, prototypes, UAT
- Design and AI tools: Axure RP, Figma, Claude Code, Antigravity
- Delivery and commercial methods: Kanban, stakeholder alignment, pricing experiments, payment integration planning
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
- Product Owner of an employer-side recruitment system serving about 60,000 active paying employers (2026 Q3), covering job posting, applicant management and candidate outreach. Manage two direct-report product planners and coordinate engineering, design, sales and customer service.
- Coordinated engineering and customer service to determine the impact of more than ten employer accounts hijacked in 2026/03–04. Designed and launched new-device OTP login verification (MFA) and an account-unlock flow. No similar account-takeover incidents were reported to customer service through 2026/10.
- Planned a unified messaging flow to address 199 client requests accumulated since 2021 (in development), consolidating two overlapping tools that scattered interview invitations between employers and job seekers.
- To lower the barrier to job posting and improve candidate matching, led the launch of AI-generated job descriptions (2024/10) and AI talent recommendations (2025/11), and guided the product planners in launching company-profile generation (2026/06). Set labor-law compliance acceptance criteria requiring employer confirmation before publishing, and refined recommendation rules using employers' actual selections and feedback.
- Led requirements analysis and specification planning to ship about 70 major features by 2026 Q3 while ongoing service iterations and a full system overhaul competed for the same engineering resources; aligned stakeholders and secured sales buy-in before delivery.
- Recovered undocumented account permissions and business rules for the employer-side recruitment system overhaul; 743 of 840 related client requests (88%) were resolved during the overhaul. Used hands-on testing and internal interviews, then coordinated phased replacement of legacy functions while keeping the existing back office, database and live service running.
- In response to 55 client requests since 2020/12, planned group recruitment by department or branch. Defined access rules across accounts, job posts and resumes and defined legacy data migration rules, extending the original company-wide or individual-account data access.
- Raised the 30-day case closure rate for enterprise clients' product issues and suggestions from 52% to 79% (2024/11–2025/10 vs. 2025/11–2026/09/20, for cases submitted at least 30 days earlier). To support paying employers' satisfaction and renewals, prioritized client cases, handled key cases directly and assigned others to the planners, building the product team's delivery credibility with sales.
- Consolidated cross-team changes to 15 category code tables starting 2026/04 to keep categories consistent across job posting, resume creation, search filtering and matching. These tables cover job roles, certifications, skills and benefits and form the platform's shared foundation; consolidation addressed fragmentation as the business expanded. Used an AI Agent to organize mappings and handoff records, and guided colleagues in using AI to map hundreds of job categories.

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
- Managed JustDating, the company's flagship and highest-grossing subscription dating app. According to public company information, it had long ranked No. 1 on Taiwan's dating app revenue chart. Also managed Peach, a subscription content app, and KOOL, an influencer-matching platform. Planned user flows, subscriptions and payment mechanisms with engineering, design, marketing and overseas payment teams. Held partnership discussions with a European payment provider in English over video calls.
- Led the design of the Malaysia iOS pricing experiment across original, discounted and restored-price phases (2021/05–08, 21 days each), using Android as the control group, with its price unchanged. The price cut raised iOS revenue excluding renewals by 5% (while Android fell 18%). Restoring the original price reduced iOS revenue excluding renewals by 65% versus the original-price phase. The company owner adopted the lower price based on the experiment results.
- Raised web payments' share of revenue for Peach, a subscription content app, from 24% to over 80% (2020/11–2021/09) by planning the shift from in-app purchases to web payments and coordinating integration with a payment provider in Taiwan.
- With no direct competitor to benchmark against, planned KOOL from zero to one by interviewing merchants' marketing teams about finding influencers on Instagram. Adapted listing and matching mechanics from Airbnb and dating apps, and mapped invitation, application and messaging flows in Miro. After the project kicked off in 2018/05, coordinated product, design and engineering to launch across iOS, Android and web. The platform accumulated about 16,000 influencer profiles and over 80,000 campaign applications in six months. Led the monetization rollout covering VIP subscriptions, a points paywall and featured exposure.
- When the App Store removed JustDating, led the launch of Juicy, a replacement app on the same backend, to retain existing users and revenue; after Juicy was removed, led JustDating's relaunch. Across both launch and marketing campaigns directing users to the app, male daily active users (DAU) rose from about 3,200 to 12,500 in 6 weeks (2020/01–02) and from about 1,500 to 12,000 in 12 weeks (2020/04–06), reflecting overall product performance.

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
- Maintained and improved SweetRing, a dating app operating across 7 markets (US, Mexico, Brazil, Indonesia, Malaysia, Japan, Korea), including its question-and-answer feature. Also took part in localization and payment planning.
- Expanded payment options in Indonesia and Thailand by bringing in CodaPay, a Southeast Asian payment provider, and opening 8 payment channels (carrier billing, ATM, e-wallets, convenience stores, bank transfer). Compared fees and settlement terms, estimated net revenue, proposed 7-, 30- and 90-day subscription plans, and coordinated delivery of the Android top-up page.
- Coordinated localization across the 7 markets, translating the app's Chinese UI text into English as the shared baseline. Then worked with up to about 10 foreign interns in English-only meetings to translate it into local languages and run local fan pages.

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
