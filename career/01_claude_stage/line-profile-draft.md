<!--markdownlint-disable MD013 MD033-->
<!--
LINE Career Profile 上游草稿 r1（2026-10-29）｜來源：104 v12.19 + library｜Career Move
給潤飾者（Codex）：
1. 只潤飾每個區塊下方的英文 Bullet Points 語感（依 career/style/voice-en.md）；<!-- @line-directive --> JSON 一個字都不要動。
2. 不改公司名、職稱、日期、數字、限定詞、Enum 代碼；不新增事實；責任詞不升級（led 僅限 decisions §51 白名單：70 項功能規劃、職缺工作說明生成與 AI 推薦人才、Juicy 推出與 JustDating 重新上架、馬來西亞定價實驗設計、KOOL 多元變現）。
3. 純英文；每個 Bullet 痛點／場景先行，不用 Backed by、句尾 , which leave…；禁用 strategic、passionate、detail-oriented、leverage、robust、seamlessly。
4. 日期一律 YYYY-MM；在職 end_date 為空字串。
5. 回傳整份 line-profile.md；修改紀錄寫檔末。
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
    "address": "3F, No. 14, Lane 98, Huaide St. Beitou District.",
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
- Product Owner of the employer-side recruitment system, which serves about 60,000 active paying employers (2026 Q3); manage two direct-report product planners and coordinate engineering, design, sales and customer service.
- Overhaul and day-to-day iterations competed for the same development resources. I led requirements analysis and specification planning, aligned stakeholders, and got sales buy-in before delivery; about 70 major features were live by 2026 Q3.
- Took over an overhaul with no documentation of account permissions or business rules. Recovered the rules through hands-on testing and internal interviews, then replaced legacy functions in phased releases on top of the existing back office and database; 743 of 840 related client requests (88%) are resolved.
- To address 199 merge requests accumulated since 2021, planned a unified messaging flow so employers and job seekers no longer split interview invitations across two overlapping tools (in development). Planned a group function for large employers, answering 55 client requests since 2020/12.
- After more than ten employer accounts were hijacked in 2026/03–04, worked with engineering and customer service to scope the impact, then planned new-device OTP login verification (MFA) and an unlock flow; no similar customer reports through 2026/10.
- Led the launch of AI-generated job descriptions (2024/10) and AI talent recommendations (2025/11), and guided my planners through company-profile generation (2026/06). Set labor-law acceptance criteria; employers confirm generated content before publishing.
- Consolidated cross-team changes to 15 job, certification, skill and benefit category tables, and guided colleagues in using an AI Agent to map hundreds of job categories.
- Raised the share of client proposals closed within 30 days from 52% to 79% (2024/11–2025/10 vs. 2025/11–2026/09/20).

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
- Managed the company's top-grossing subscription dating app JustDating (per public company information, long ranked No. 1 in Taiwan's dating category), the subscription content app Peach and the influencer-matching platform KOOL; planned user flows and subscription and payment mechanisms with engineering, design, marketing and overseas payment teams.
- When the App Store removed JustDating, led the launch of Juicy on the same backend; after Juicy was removed, led the relaunch of JustDating. Male daily active users rose from about 3,200 to 12,500 in 6 weeks (2020/01–02) and from about 1,500 to 12,000 in 12 weeks (2020/04–06), measured over launch and promotion periods.
- Planned KOOL from zero with no direct competitor to reference: interviewed merchants' marketing teams about finding influencers on Instagram, then mapped listing, invitation, sign-up and messaging flows; launched in 2018/05 with about 16,000 influencer profiles and over 80,000 campaign sign-ups in six months. Led the monetization design (VIP subscription, points paywall, featured exposure).
- Designed the Malaysia iOS pricing experiment with unchanged-price Android as the control (2021/05–08, 21 days per phase): the price cut raised iOS non-renewal revenue 5% (Android fell 18%), and restoring the original price cut it 65% versus the original-price phase. The company owner chose the lower price based on the results.
- Raised Peach's web-payment share of revenue from 24% to over 80% (2020/11–2021/09) by planning the move from in-app purchases to web payments and completing a Taiwan payment-provider integration. Held partnership discussions in English with a European payment provider.

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
