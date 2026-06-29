<!--markdownlint-disable MD033-->
<!--markdownlint-disable MD013-->

# 📚 交接包索引（WIKI）— 信件訊息頁切版

> **新 session 從這裡開始。** 這份是整包的目錄與導覽；路徑皆相對 repo 根目錄（zip 解開後同此結構）。
> 任務：1111 求才企業端「信件訊息」頁（`ResumePoolNoticeMail`）前端視覺改版。分支 `claude/eloquent-maxwell-j31ot5`（PR #8）。

---

## 🚀 三步上手

1. 先讀 **[`handoff/_migration/README-session-handoff.md`](README-session-handoff.md)** —— 全局背景、四檔關係、待辦、環境限制。
2. 再讀兩份修改紀錄：**[`01_HTML…`](01_HTML結構調整對照.md)**（結構/偏離）、**[`02_CSS…`](02_CSS樣式調整對照.md)**（逐條樣式）。
3. 要動手時，行為法則看 skill：**`.claude/skills/frontend-slicing-1111/SKILL.md`**（觸發「切版/改版/需求文件」會自動帶出）。

---

## 🗂️ 全部檔案地圖

### A. 交接主文件
| 檔 | 是什麼 |
| :-- | :-- |
| `handoff/_migration/INDEX.md` | **本檔**，整包索引（WIKI 入口） |
| `handoff/_migration/README-session-handoff.md` | 交接主文件：背景、四檔關係（P/B/A 三狀態）、時間軸、待辦、環境限制、接手步驟 |

### B. 四個程式檔（before/after × HTML/CSS）
| 檔 | 狀態 | 說明 |
| :-- | :-- | :-- |
| `handoff/_migration/before/ResumePoolNoticeMail.html` | B（改前） | PM 給的 mock HTML，我動手前 |
| `handoff/_migration/before/resumePoolNoticeMail.css` | B（改前） | mock CSS 原始 bundle（1629 行） |
| `handoff/_migration/after/ResumePoolNoticeMail.html` | A（改後） | 現在的 mock HTML |
| `handoff/_migration/after/resumePoolNoticeMail.css` | A（改後） | mock CSS＋我加的 override（1706 行） |

> before↔after 的 diff＝**我這輪的改動（B↔A）**。「mock 與正式環境的偏離（P↔B）」另記在 `01_…§2.5`。三狀態 P/B/A 定義見 README §1。

### C. 兩份修改紀錄
| 檔 | 是什麼 |
| :-- | :-- |
| `handoff/_migration/01_HTML結構調整對照.md` | HTML 面：差異點＋§2.5 與正式環境的結構偏離清單 |
| `handoff/_migration/02_CSS樣式調整對照.md` | CSS 面：逐條 `selector｜原值→新值｜行數`（A/B/C/D 區） |

### D. 交付給工程師的需求文件 + 預覽
| 檔 | 是什麼 |
| :-- | :-- |
| `handoff/需求文件-ResumePoolNoticeMail.md` | **最終需求文件**（求才 template、白話、逐標籤、CSS 標檔名行號）。v0.2.2，HackMD：`@1111-jobdocs/S1cYFSFfzx` |
| `handoff/preview-tab-underline.html` | 自包含預覽（after CSS 內嵌進 after HTML），瀏覽器單檔可開 |

### E. 可複用 skill（切版/前端經驗）
| 檔 | 是什麼 |
| :-- | :-- |
| `.claude/skills/frontend-slicing-1111/SKILL.md` | 主：鐵則、標準流程、三狀態 |
| `…/reference/css-conventions.md` | CSS override 策略、字體規則、離線替身排除、行號擷取、常見改法 |
| `…/reference/mock-vs-production-audit.md` | tag/class skeleton diff（Python）、偏離分類、何時修 mock |
| `…/reference/requirement-doc-style.md` | 需求文件白話寫法、標記符號、章節範本 |
| `…/reference/preview-and-figma.md` | 自包含預覽產生、Figma token 擷取、環境限制 |

---

## 🔎 我想做 X → 看哪裡

| 我想… | 去 |
| :-- | :-- |
| 了解整件事的來龍去脈 | `README-session-handoff.md` |
| 知道某區塊最終長怎樣 / CSS 在第幾行 | `README §3` 或 `需求文件` 對應章節 |
| 知道「我改了什麼」 | before↔after 四檔 diff + `02_CSS…` |
| 知道「mock 跟正式差在哪」 | `01_…§2.5` |
| 繼續改樣式 | 改 `handoff/_files/resumePoolNoticeMail.css`（repo 內的 after 本體）→ 重生預覽 → 更新 `02_`/需求文件 |
| 知道規矩（只改 CSS、字體、預覽…） | `SKILL.md` 鐵則 + README §5 |
| 接手卡住的待辦 | `README §4`（HackMD 區塊對應、before/after 截圖編號） |

---

## ⚠️ 一定要知道的鐵則（細節見 SKILL.md）

1. **只改 CSS 值**達成視覺，**不動 HTML 結構/class/tag**；HTML typo 不自行修。
2. **字體一律微軟正黑體**；FontAwesome 圖示字型不動。
3. **動到畫面就重生自包含預覽**並交付。
4. **mock 偏離據實記錄**；會誤導工程師的偏離優先「修 mock 對齊正式」。

## 🧱 卡住/環境限制

* HackMD（`hackmd.io`/`api.hackmd.io`）**egress 被擋**＋**無 token** → 讀寫 HackMD 要靠使用者貼/上傳，或開放 egress。
* **無頭瀏覽器不可用** → 截不了圖，改交付自包含預覽 HTML。
* 待辦詳見 `README §4`。
