<!--markdownlint-disable MD013-->

# HR 6 秒篩選參考文件（使用者 2026-10-09 提供）＋研讀筆記

> 原文保留如下，研讀筆記、與既有裁定的衝突處理、落點在後半段。原文引用的是 YouTube 影片的觀點（眼動實驗、Google 招募團隊），**本 session 未逐一查證**，當作方針使用，不寫進履歷。
> 姊妹文件：`ats-2026-source.md`（ATS 怎麼搜、怎麼解析）。本文件管「人怎麼掃」。

## 原文

### The 6-Second Screen: How HR Actually Picks Resumes

When job seekers hit "submit," they often imagine a hiring manager carefully reading their resume from top to bottom, weighing their experiences over a cup of coffee. However, insights from top recruiters and career experts reveal a much more brutal reality. By analyzing five highly viewed videos—including eye-tracking experiments and direct advice from Google's hiring teams—a clear picture emerges of exactly how Human Resources (HR) professionals and recruiters pick winning resumes.

#### The Eye-Tracking Reality: The 6-Second Triage
The most crucial insight into the recruiter's mind comes from how they physically view a document. In his video exposing recruiter habits with a hidden eye tracker (1.25M views), career expert Jerry Lee demonstrates that recruiters do not *read* resumes; they *scan* them. 

On average, a recruiter spends only 6 to 10 seconds on their initial triage. During this time, their eyes follow an "F-pattern" or "E-pattern," heavily favoring the left side of the page. They immediately look for:
1. **Recent Job Title:** To ensure basic qualification alignment.
2. **Current Company:** For industry context.
3. **Dates of Employment:** To check for tenure and career progression.

Because the eye naturally rests on the left margin, putting crucial information (like job titles) on the right side or burying it in the middle of a paragraph guarantees it will be ignored. If the structural layout is confusing, the recruiter simply moves on to the next candidate.

#### The Death of the "Objective Statement"
Both techblueweb's foundational guide (3.4M views) and Thomas Frank's resume masterclass (1.7M views) highlight the necessity of cutting fluff to survive the 6-second scan. The traditional "Objective Statement" (e.g., *“Seeking a challenging role to utilize my skills”*) is universally disliked by modern recruiters because it focuses on what the *candidate* wants, rather than what the *employer* needs. 

If a candidate uses a top section at all, it should be a brief "Professional Summary" that acts as a highlight reel of their most relevant qualifications, immediately answering the recruiter's primary question: *"Can this person do the job?"*

#### The Google Standard: Impact Over Duties
When a candidate survives the initial scan, the recruiter will finally look at the bullet points. Videos from both *Life at Google* (1.5M views) and *Grow with Google* (1.07M views) stress that HR professionals are exhausted by resumes that read like job descriptions. Listing duties (e.g., *"Responsible for managing social media"*) tells the recruiter what you were *supposed* to do, not what you actually *achieved*.

To fix this, Google’s recruiters recommend strictly using their **XYZ Formula**: 
* **Accomplished [X], as measured by [Y], by doing [Z].**

Instead of a vague duty, a bullet point should read: *"Grew social media following by 40% [X], as measured by monthly engagement metrics [Y], by implementing a new video content calendar [Z]."* This provides HR with immediate, quantifiable proof of a candidate's value. 

#### Strategic Tailoring and One-Page Discipline
A common thread across all expert advice is the importance of brevity and relevance. Thomas Frank notes that recruiters are looking for a curated argument for a specific role, not an exhaustive autobiography. 

For early to mid-career professionals, keeping the resume to a single page is heavily preferred by HR. This forces candidates to selectively tailor their work history, omitting irrelevant part-time jobs from years ago to make room for targeted keywords and impactful metrics that directly map to the job description they are applying for. 

#### The Bottom Line
Ultimately, HR professionals are looking for reasons to say "yes" quickly. By optimizing the visual architecture for a left-to-right skim, replacing subjective fluff with quantified XYZ achievements, and mercilessly editing for relevance, candidates can build a resume that survives the 6-second triage and wins the interview.

***
**Source Material & Further Viewing:**
* *exposing recruiters w/ hidden eye tracker* - Jerry Lee (1.25M views)
* *Create Your Resume for Google: Tips and Advice* - Life at Google (1.5M views)
* *A recruiter's perspective on resumes* - Grow with Google (1.07M views)
* *8 Tips for Writing a Winning Resume* - Thomas Frank (1.72M views)
* *How to Write a Good Resume* - techblueweb (3.4M views)
## 研讀筆記（session 整理）

### 五個觀念

| # | 原文觀念 | 對我們的意思 |
| :-- | :--- | :--- |
| 1 | 初篩 6–10 秒，**不是讀而是掃**，視線走 F／E 型、集中在左緣 | 每行只有開頭幾個字會被看到；放在行尾或段落中間的資訊等於沒寫 |
| 2 | 先找三樣：**最近職稱、目前公司、起訖日期** | 經歷抬頭要「職稱在左、日期緊跟」，抬頭不能長到日期被擠出視野 |
| 3 | **不要求職目標（Objective）**，摘要要回答「這個人能不能做這份工作」 | 摘要第一句是能力證據，不是「希望」「尋求」「發揮所長」 |
| 4 | **成果勝過職責**，Google XYZ：做到 X、以 Y 衡量、靠 Z 做到 | 「負責／主責／協助」開頭的句子一律改寫；每條拆得出 X、Y、Z |
| 5 | **依職缺取捨、一頁紀律**：刪掉多年前無關的打工，把空間留給關鍵字與成果 | 每次依目標職缺做「相關性刪減」；資深者仍可 2 頁（見下方衝突處理） |

> 結語：HR 在找**快速說 yes 的理由**。所以驗證時要問的是「6 秒內找到幾個 yes 的理由」，不只是「有沒有扣分點」。

### 與既有裁定的衝突與處理

| 衝突 | 處理 | 依據 |
| :--- | :--- | :--- |
| 原文「中階以下一頁」vs 使用者近 10 年資歷、交付鏈必須呈現 | 維持**至多 2 頁**；但第一屏（約前 1,400 字）必須單獨就能通過 6 秒篩選 | `resume-craft` 長度規則；`library/decisions.md` §7 |
| 原文「列職責沒用」vs 交付鏈產出物（User Journey、Use Case、Prototype、PRD…）必須看得到 | 產出物放進 XYZ 的 **Z（靠什麼做到）**，或放技能欄；**每段經歷至多 1 條只有做法的條列**，且不得排在該段第一條 | `decisions.md` §7、`style/postmortem-2026-10-08-deliverables.md` |
| 「職稱在左」vs 正式職稱與對外職稱的寫法 | 抬頭第一段放對外職稱（`decisions.md` §3 允許的寫法），正式職稱放括號或第二行；不改事實 | `decisions.md` §3、`profile.md` §1 |
| 「刪多年前無關打工」vs 104 表單經歷欄 | 只在**依職缺客製的 txt／PDF** 刪；104 表單是否保留由使用者決定（列 open question，不自行刪） | `decisions.md` §6 平台分流 |

### 落點（2026-10-09 寫進 skill）

| 原文觀念 | 寫履歷（resume-craft） | 驗證（resume-review-panel） |
| :--- | :--- | :--- |
| F 型、左緣 | 步驟 4a 新變化軸「左緣 10 字放結果或 JD 詞」；`resume_score.py` 左緣分 | `f_scan.py` 產「F 型視野」，交給另一個模型做 6 秒初篩 |
| 職稱、公司、日期 | 抬頭格式 `職稱｜公司｜起訖`，日期在前 24 字內 | `f_scan.py` 抬頭檢查；初篩題「最近職稱、目前公司、年資」 |
| 不要求職目標 | 摘要第一句是能力證據；求職目標語扣分 | 初篩題「能不能做這份工作？依據哪一句」 |
| XYZ | essay 與每條條列標 X／Y／Z；職責式開頭扣分 | 盲審逐條標 X／Y／Z 與「成果／職責」 |
| 相關性取捨 | 步驟 4c「相關性刪減」 | 盲審列「與這個職缺無關、可刪」的段落 |
| 找 yes 的理由 | — | 初篩列「6 秒內找到的 yes 理由」，對照想傳達的訊息 |
