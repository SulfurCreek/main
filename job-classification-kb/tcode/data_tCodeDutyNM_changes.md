# tCodeDutyNM 新增／改名建議（來源：職類校正討論表 20260420）

> 來源檔：`1ffea538-20260420___________.csv`（807 列，機械工程中類分隔列為 pandas index 268；資料範圍 index 269 起）。
> `ChangeType` 用字依 [01-schema.md](01-schema.md) 既有定義：**新增 = `add`**、**改名 = `edit`**（同 rename）。
> 本檔為**建議清單**，尚未寫入 `tCodeDutyNM`／`TCode_Export.xlsx` 正式代碼表；`add` 的 CodeNo 皆為暫擬，正式代碼以系統指派為準。
>
> **篩選方法（v2，已修正 v1 漏抓）**：v1 只抓 T 欄字面含「新增」「改名」兩詞的列，漏掉了 T 欄直接寫新名稱（無關鍵字）、
> 用「更名」「移到」表述、或單純換中類（不改名）的列——例如 220411~220418 一整組翻譯語系改名。
> v2 改為列出 index 269 後**所有** T 欄非空列，逐列人工核判斷歸類，才收錄本檔。
> 共 **38 筆**收錄（4 筆 `add`、34 筆 `edit`，含 3 筆中類層級 edit、1 筆純換中類不改名）；
> 另有 6 筆 T 欄雖非空但屬「待分析／待人工判斷」而非單純新增/改名，見文末「不列入」章節。

## 代碼結構規則（判斷 add 該掛在哪一層時要用到）

`tCodeDutyNM` 為三層表，CodeNo 規則（詳見 [01-schema.md](01-schema.md)）：

| CodeType | 層級 | CodeNo 特徵 |
|---|---|---|
| 1 | 大類 | 末四碼 `0000`（如 `160000`） |
| 2 | 中類 | 末兩碼 `00`（如 `160100`） |
| 3 | 葉／小類 | 其餘非 `00` 結尾 |

判斷一筆 `edit` 是中類還是小類層級：CSV 中若 `1111小類代碼`／`1111小類名稱` 為空、只有 `1111中類名稱` 有值 → 該筆是**中類層級** edit，`Old_CodeNo`/`New_CodeNo` 末兩碼必為 `00`。

---

## ChangeType = edit（改名，34 筆）

### 中類層級（3 筆）

| Old_CodeNo | New_CodeNo | 現行中類名稱（CodeNameA） | 建議新名稱 | 所屬大類（CodeNameC） |
|---|---|---|---|---|
| 210200 | 210200 | 化工實驗 | 化工／材料研發 | 生物科技／化學製藥 |
| 250500 | 250500 | 教育師資 | 國教師資 | 學術研究／教育師資 |
| 260300 | 260300 | 補習進修 | 補教師資 | 幼教才藝／補習進修 |

### 小類層級 — 純改名（22 筆，Old_CodeNo = New_CodeNo）

| CodeNo | 現行名稱（CodeNameA） | 建議新名稱 | 所屬中類（CodeNameB） | 備註 |
|---|---|---|---|---|
| 160201 | 工廠高階主管 | 工廠主管 | 生產製程 | |
| 160309 | 塑膠射出技術人員 | 塑膠射出／押出／吹出技術人員 | 模具相關 | |
| 170219 | 染印人員 | 染整人員 | 操作技術 | T欄原文「更名為」，v1 漏抓 |
| 170309 | 汽車維修人員 | 汽車／其他車輛維修人員 | 維修／技術服務 | 產業需求穩定 |
| 170310 | 汽車引擎技術人員 | 車輛引擎技術人員 | 維修／技術服務 | 與汽車維修重疊，討論刪除 |
| 170313 | 機械設備組裝測試人員 | 機械設備組裝人員 | 維修／技術服務 | T欄原文「更名」，v1 漏抓；104小類名稱為「機械裝配員」，與T欄建議名不同，以T欄為準 |
| 180204 | 船上作業人員 | 船員 | 運輸物流 | 與船員職類重疊，因難以細分船上工作，故改通用名，去留宜討論 |
| 180318 | 職業安全衛生管理人員 | 職業安全衛生管理員 | 品管品保 | T欄原文「更名」，v1 漏抓 |
| 190109 | 土木技師 | 土木技師／工程師 | 營建規劃 | 法定證照職類 |
| 190114 | 電信／配線繪圖 | 機電配線繪圖 | 營建規劃 | |
| 190201 | 工地主管／主任 | 工地監工／主任 | 營造施作 | |
| 200106 | 臨床／諮商心理師 | 心理師 | 醫事人員 | 法定證照職類 |
| 200114 | 動物醫事助理 | 獸醫助理 | 醫事人員 | 與獸醫助理職類重疊，討論刪除 |
| 220104 | 播報人員 | 播報／主持人 | 新聞媒體 | |
| 220202 | 表演／主持／直播人員 | 表演／直播人員 | 影視演藝 | 新興產業與表演職能整合 |
| 220304 | 執行製作／助理 | 執行助理 | 幕後執行 | |
| 220407 | 英文翻譯／口譯人員 | 英文翻譯 | 出版翻譯 | |
| 220408 | 日文翻譯／口譯人員 | 日文翻譯 | 出版翻譯 | |
| 220409 | 其他語言翻譯／口譯人員 | 其他語言翻譯 | 出版翻譯 | 需提醒廠商修正現有刊登內容 |
| 220419 | 手語翻譯人員 | 手語人員 | 出版翻譯 | |
| 230111 | 美編人員 | 平面設計／美編 | 美編設計 | |
| 260308 | 安親課輔老師 | 安親／課輔老師 | 補習進修 | |
| 270201 | 餐飲主管 | 餐飲主管／領班 | 餐飲烘焙 | |
| 270207 | 中／港式點心廚師 | 麵點／港點師傅 | 餐飲烘焙 | 與「中式麵點人員／師傅」重疊，討論建議保留中式麵點人員／師傅 |
| 270306 | 飯店／旅館服務人員 | 飯店／旅館工作人員 | 觀光旅遊 | |
| 270307 | 休閒娛樂事業從業人員 | 休閒娛樂從業人員 | 觀光旅遊 | 涵蓋電玩場、夜市遊戲、觀光體驗；多數職缺無法精準歸入既有細分類 |
| 280106 | 家事服務／洗衣 | 家事服務／洗衣整燙 | 生活服務 | |
| 290103 | 消防類相關人員 | 消防勤務人員 | 軍警消防 | 與「消防專業人員→消防設備技術人員」區分：前者為公職／勤務（消防員、救災、出勤、救護），後者為技術／工程／民間職（設備檢修、設計、申報） |
| 290203 | 隨扈／安全人員 | 隨扈／特勤 | 保全相關 | 人身安全職能明確 |

### 小類層級 — 出版翻譯語系系列改名（8 筆，本次補抓）

T 欄直接填新名稱、無「改名」關鍵字，v1 因此整組漏抓。與已收錄的 220407/220408/220409/220419 同批（皆為「XX翻譯／口譯人員」→「XX翻譯」簡化）：

| CodeNo | 現行名稱（CodeNameA） | 建議新名稱 | 所屬中類 |
|---|---|---|---|
| 220411 | 印尼翻譯／口譯人員 | 印尼翻譯 | 出版翻譯 |
| 220412 | 越南翻譯／口譯人員 | 越南翻譯 | 出版翻譯 |
| 220413 | 韓文翻譯／口譯人員 | 韓文翻譯 | 出版翻譯 |
| 220414 | 泰文翻譯／口譯人員 | 泰文翻譯 | 出版翻譯 |
| 220415 | 菲律賓翻譯／口譯人員 | 菲律賓翻譯 | 出版翻譯 |
| 220416 | 德文翻譯／口譯人員 | 德文翻譯 | 出版翻譯 |
| 220417 | 西班牙文翻譯／口譯人員 | 西班牙文翻譯 | 出版翻譯 |
| 220418 | 法文翻譯／口譯人員 | 法文翻譯 | 出版翻譯 |

### 小類層級 — 教育師資→補教師資 語言老師搬遷（5 筆，本次補抓 4 筆）

T 欄用「移到 補教師資」表述（非「改名」），v1 漏抓其中 4 筆（僅原收錄 250514）。這批全部**跨中類移動**（教育師資 250500 → 補教師資／原補習進修 260300），部分同時改名：

| CodeNo | 現行名稱（CodeNameA） | 建議新名稱 | 中類異動 | 備註 |
|---|---|---|---|---|
| 250510 | 英語教師 | 英文老師 | 教育師資（250500）→ 補教師資（260300） | v1 漏抓 |
| 250511 | 日語教師 | 日文老師 | 教育師資（250500）→ 補教師資（260300） | v1 漏抓 |
| 250512 | 韓語教師 | 韓文老師 | 教育師資（250500）→ 補教師資（260300） | v1 漏抓 |
| 250513 | 其他語系教師 | （名稱不變） | 教育師資（250500）→ 補教師資（260300） | v1 漏抓；純換中類，不改名 |
| 250514 | 華語教師 | 中文老師 | 教育師資（250500）→ 補教師資（260300） | 原已收錄 |

> 這 5 筆的 `New_CodeNo` 皆待系統重新編號（原 2505xx 前綴，移入 260300 系列後應改 2603xx），非純改名，不可套用「Old=New」假設。

### 小類層級 — 純換中類，不改名（1 筆，本次補抓）

| CodeNo | 現行名稱（CodeNameA） | 中類異動 | 備註 |
|---|---|---|---|
| 210206 | 食品研發人員 | 化工實驗（210200）→ 醫藥生技（210100） | 名稱不變，僅搬移中類；`New_CodeNo` 待系統重新編號 |

---

## ChangeType = add（新增，4 筆）

中類層級無新增。以下皆為小類／葉層級新增，`Old_CodeNo`/`New_CodeNo` 為 `NULL`（全新代碼）。

| 暫擬 CodeNo | 建議名稱（CodeNameA） | 所屬中類（CodeNameB） | 命名依據 | 說明 |
|---|---|---|---|---|
| 160117 | 電力工程師 | 機械工程（160100） | 104 小類名稱（104對應碼 2008001030） | 1111 無專指電力相關職類，多用電機代替，較不精準；相關職缺已逾千筆 |
| 160118 | 能源工程師 | 機械工程（160100） | 104 小類名稱（104對應碼 2008001031） | 綠能產業需求明確 |
| 290206 | 徵信／調查人員 | 保全相關（290200） | CSV 原詞「調查員」，討論後建議定名 | 涵蓋保險理賠、徵信、企業內部調查、背景查核；與金融業授權／授信／徵信人員（金融風控）本質不同，屬民間調查服務；與法務／客服／業務職能區隔明確 |
| — | 監控／門禁／停車／監視器／保全工程技術人員／網路及電信（關鍵字擴充，非新葉） | 弱電工程師（170223） | CSV 建議 | 非新增小類，是既有「弱電工程師」小類的關鍵字補充，不佔用新 CodeNo |

> 暫擬 CodeNo 取各所屬中類現有最大葉代碼 +1（機械工程現有葉最大 160116；保全相關現有葉最大 290205）。實際入庫代碼仍須由系統/負責人指派，不保證無衝突。

### add 項目完整欄位草稿（I~T、Z~AQ，供複製貼上；CodeNo 為 row）

> 依 [01-schema.md](01-schema.md) 的 I~T／Z~AQ 欄位定義草擬。**B/C 系列翻譯（CodeNameB/C_EN/VI/TH/ID）直接沿用同中類既有葉節點的值**（機械工程沿用 160104 電機技師／工程師；保全相關沿用 290203/290204）；A 系列（葉名本身）、chs 系列、Descript_EN/VI/TH/ID 系列為本次新寫內容，屬**草稿**，需人工審閱、必要時補上實際統計數據（本草稿未捏造薪資／人數等具體數字）。`CodeDescript_EN/VI/TH/ID` 依 I 欄內容逐點翻譯補齊（多數既有葉節點此欄留空，但本次依要求補上）。

#### I ~ T

| CodeNo | CodeNameA | I CodeDescript | J CodeCore | K CodeAlike | L CodeCert | M CodeFuture | N CodeMajor | O CodeDefinition | P chsNameA | Q chsDescription | R chsJobContent | S chsJobSkills | T chsAlike |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 160117 | 電力工程師 | 1.電力系統之規劃、設計與配電網路架構<br>2.發電、輸電、配電設備之運轉維護與故障排除<br>3.配合再生能源專案，執行併網與電力品質評估<br>4.用電設備安全檢測與電力容量計算<br>5.電力相關法規與台電併聯規範之遵循與申請作業 | 1.分析思考<br>2.問題解決<br>3.精確嚴謹<br>4.溝通協調 | 電力系統工程師<br>配電工程師<br>輸電工程師<br>電網工程師<br>用電設備工程師<br>電力調度員 | 1.高考電機工程技師<br>2.用電設備檢驗技術士<br>3.變電設備裝修技術士<br>4.變壓器裝修技術士 | 資深電力工程師<br>電力系統主管<br>工程部經理 | 大學 以上，電機工程學類相關科系 | 從事發電、輸電、配電系統之規劃設計、運轉維護與電力品質管理之工程人員 | 供電工程師 | φ指從事電力系統規劃、輸配電設備運轉維護的專業技術人員 | φ負責電力系統設計與配電網路規劃 φ進行輸變電設備運轉監控與故障排除 φ執行用電設備安全檢測與容量計算 | φ電機工程相關科系畢業，具電力系統設計與維護經驗 φ熟悉相關法規與台電併聯申請流程 | φ電力系統工程師φ配電工程師φ輸電工程師 |
| 160118 | 能源工程師 | 1.再生能源（太陽能、風能、儲能系統等）之規劃、設計與導入評估<br>2.能源效率提升方案之研擬與能源稽核<br>3.能源系統之運轉監控、維護與績效分析<br>4.協助企業ESG／碳盤查與節能減碳專案執行<br>5.政府能源相關法規、補助案與併網申請作業 | 1.分析思考<br>2.學習態度<br>3.跨部門溝通<br>4.問題解決 | 綠能工程師<br>再生能源工程師<br>太陽能工程師<br>儲能系統工程師<br>節能工程師<br>ESG專案工程師<br>碳權管理師 | 1.能源管理技術士<br>2.高考電機工程技師<br>3.太陽光電設置技術士 | 資深能源工程師<br>能源專案經理<br>永續發展主管 | 大學 以上，電機工程／能源工程／環境工程學類相關科系 | 從事再生能源、節能與能源效率相關系統之規劃設計、導入評估與稽核管理之工程人員 | 新能源工程師 | φ指從事太陽能、風能等再生能源系統規劃、導入與能源效率管理的專業技術人員 | φ規劃太陽能、風能、儲能等再生能源導入方案 φ執行能源稽核與節能改善建議 φ協助企業碳盤查與ESG專案執行 | φ電機／能源／環境工程相關科系畢業，具再生能源專案經驗 φ熟悉能源法規與補助申請流程 | φ綠能工程師φ再生能源工程師φ太陽能工程師 |
| 290206 | 徵信／調查人員 | 1.受託進行徵信調查、背景查核、個人資料查證等蒐證工作<br>2.外勤跟監、行蹤調查與證據蒐集<br>3.企業內部調查（如舞弊、洩密、內控違規）之訪查與資料分析<br>4.調查報告撰寫與委託人溝通說明<br>5.遵循個資法及相關法規，確保調查手法合法 | 1.觀察力<br>2.隨機應變<br>3.保密原則<br>4.溝通協調 | 徵信人員<br>調查員<br>徵信社人員<br>企業內部調查人員<br>背景查核人員<br>蒐證人員 | 1.保全人員護照<br>2.個人資料保護管理師 | 資深調查員<br>徵信社主管<br>風控稽核主管 | 專科 以上，法律／刑事司法／社會學類相關科系 | 受託對特定對象進行蒐證、跟監、背景查核與資料分析，提供徵信或調查報告之人員；與金融業徵信（授信風控）性質不同，屬民間調查服務 | 私家偵探 | φ受託對特定對象進行蒐證、跟監、背景與資信查核，提供調查報告的專業人員 | φ受理徵信、背景查核委託案件 φ執行外勤跟監、行蹤調查與蒐證 φ撰寫調查報告並與委託人說明 | φ具法律或刑事調查相關背景佳 φ熟悉個資法規範，具良好觀察與溝通能力 | φ調查員φ私家偵探φ徵信人員 |

#### Z ~ AQ

| CodeNo | Z CodeNameEN | AA CodeNameCHS | AB CodeNameA_EN | AC CodeNameB_EN | AD CodeNameC_EN | AE CodeDescript_EN | AF CodeNameA_VI | AG CodeNameB_VI | AH CodeNameC_VI | AI CodeDescript_VI | AJ CodeNameA_TH | AK CodeNameB_TH | AL CodeNameC_TH | AM CodeDescript_TH | AN CodeNameA_ID | AO CodeNameB_ID | AP CodeNameC_ID | AQ CodeDescript_ID |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 160117 | Electrical Power Engineer | 电力工程师 | Electrical Power Engineer | Mechanical Engineering | Mechanical Mold / Production Process | 1. Plan and design electrical power systems and distribution network architecture.<br>2. Operate, maintain, and troubleshoot power generation, transmission, and distribution equipment.<br>3. Support renewable energy projects by performing grid interconnection and power quality assessments.<br>4. Conduct electrical safety inspections and calculate power capacity for electrical equipment.<br>5. Comply with electricity-related regulations and Taipower grid-interconnection requirements, and handle related applications. | Kỹ sư điện lực | kỹ sư cơ khí | Khuôn cơ khí / quy trình sản xuất | 1. Lập kế hoạch và thiết kế hệ thống điện lực và mạng lưới phân phối điện.<br>2. Vận hành, bảo trì và khắc phục sự cố các thiết bị phát điện, truyền tải và phân phối điện.<br>3. Hỗ trợ các dự án năng lượng tái tạo bằng cách thực hiện đấu nối lưới điện và đánh giá chất lượng điện năng.<br>4. Kiểm tra an toàn thiết bị dùng điện và tính toán công suất điện.<br>5. Tuân thủ các quy định về điện và quy định đấu nối của Taipower, đồng thời xử lý các thủ tục xin phép liên quan. | วิศวกรไฟฟ้ากำลัง | วิศวกรรมเครื่องกล | แม่พิมพ์ทางกล / กระบวนการผลิต | 1. วางแผนและออกแบบระบบไฟฟ้ากำลังและโครงสร้างเครือข่ายจำหน่ายไฟฟ้า<br>2. ควบคุมการเดินเครื่อง บำรุงรักษา และแก้ไขปัญหาอุปกรณ์ผลิต ส่ง และจำหน่ายไฟฟ้า<br>3. สนับสนุนโครงการพลังงานหมุนเวียนโดยดำเนินการเชื่อมต่อระบบไฟฟ้าและประเมินคุณภาพไฟฟ้า<br>4. ตรวจสอบความปลอดภัยของอุปกรณ์ไฟฟ้าและคำนวณความจุไฟฟ้า<br>5. ปฏิบัติตามกฎระเบียบด้านไฟฟ้าและข้อกำหนดการเชื่อมต่อของการไฟฟ้า (Taipower) รวมถึงดำเนินการยื่นขออนุญาตที่เกี่ยวข้อง | Insinyur Tenaga Listrik | teknik Mesin | Cetakan mekanis / proses produksi | 1. Merencanakan dan merancang sistem tenaga listrik dan arsitektur jaringan distribusi.<br>2. Mengoperasikan, memelihara, dan mengatasi gangguan pada peralatan pembangkit, transmisi, dan distribusi listrik.<br>3. Mendukung proyek energi terbarukan dengan melakukan interkoneksi jaringan dan evaluasi kualitas daya.<br>4. Melakukan pemeriksaan keselamatan peralatan listrik dan menghitung kapasitas daya.<br>5. Mematuhi peraturan kelistrikan dan ketentuan interkoneksi jaringan Taipower, serta mengurus perizinan terkait. |
| 160118 | Energy Engineer | 能源工程师 | Energy Engineer | Mechanical Engineering | Mechanical Mold / Production Process | 1. Plan, design, and evaluate the adoption of renewable energy systems (solar, wind, energy storage, etc.).<br>2. Develop energy efficiency improvement proposals and conduct energy audits.<br>3. Monitor, maintain, and analyze the performance of energy systems.<br>4. Assist companies with ESG/carbon inventory and energy-saving/carbon-reduction projects.<br>5. Handle government energy-related regulations, subsidy applications, and grid interconnection applications. | Kỹ sư năng lượng | kỹ sư cơ khí | Khuôn cơ khí / quy trình sản xuất | 1. Lập kế hoạch, thiết kế và đánh giá việc áp dụng các hệ thống năng lượng tái tạo (năng lượng mặt trời, gió, hệ thống lưu trữ năng lượng, v.v.).<br>2. Xây dựng các phương án nâng cao hiệu quả năng lượng và thực hiện kiểm toán năng lượng.<br>3. Giám sát vận hành, bảo trì và phân tích hiệu suất của hệ thống năng lượng.<br>4. Hỗ trợ doanh nghiệp trong việc kiểm kê ESG/carbon và thực hiện các dự án tiết kiệm năng lượng, giảm phát thải carbon.<br>5. Xử lý các quy định về năng lượng của chính phủ, hồ sơ xin trợ cấp và đấu nối lưới điện. | วิศวกรพลังงาน | วิศวกรรมเครื่องกล | แม่พิมพ์ทางกล / กระบวนการผลิต | 1. วางแผน ออกแบบ และประเมินการนำระบบพลังงานหมุนเวียน (พลังงานแสงอาทิตย์ ลม ระบบกักเก็บพลังงาน ฯลฯ) มาใช้<br>2. จัดทำแผนเพิ่มประสิทธิภาพพลังงานและดำเนินการตรวจสอบพลังงาน (Energy Audit)<br>3. ติดตามการเดินระบบ บำรุงรักษา และวิเคราะห์ประสิทธิภาพของระบบพลังงาน<br>4. ช่วยเหลือองค์กรในการจัดทำบัญชี ESG/คาร์บอน และดำเนินโครงการประหยัดพลังงานและลดคาร์บอน<br>5. ดำเนินการตามกฎระเบียบด้านพลังงานของภาครัฐ การยื่นขอเงินอุดหนุน และการเชื่อมต่อระบบไฟฟ้า | Insinyur Energi | teknik Mesin | Cetakan mekanis / proses produksi | 1. Merencanakan, merancang, dan mengevaluasi penerapan sistem energi terbarukan (surya, angin, sistem penyimpanan energi, dll).<br>2. Menyusun proposal peningkatan efisiensi energi dan melakukan audit energi.<br>3. Memantau operasional, memelihara, dan menganalisis kinerja sistem energi.<br>4. Membantu perusahaan dalam inventarisasi ESG/karbon serta pelaksanaan proyek hemat energi dan pengurangan karbon.<br>5. Menangani peraturan energi pemerintah, permohonan subsidi, dan aplikasi interkoneksi jaringan. |
| 290206 | Investigator | 征信／调查人员 | Investigator | Security-Related | Military / Police / Fire / Security | 1. Conduct entrusted investigations such as credit/background checks, background verification, and personal information verification.<br>2. Perform field surveillance, whereabouts investigation, and evidence gathering.<br>3. Conduct interviews and data analysis for internal corporate investigations (e.g., fraud, information leaks, internal control violations).<br>4. Prepare investigation reports and communicate findings to clients.<br>5. Comply with the Personal Data Protection Act and related regulations to ensure investigation methods are lawful. | Nhân viên điều tra | liên quan đến bảo mật | Quân đội và cảnh sát phòng cháy chữa cháy/an ninh liên quan | 1. Thực hiện các cuộc điều tra tín nhiệm, xác minh lý lịch và kiểm tra thông tin cá nhân theo yêu cầu ủy thác.<br>2. Thực hiện giám sát hiện trường, điều tra tung tích và thu thập chứng cứ.<br>3. Phỏng vấn và phân tích dữ liệu phục vụ điều tra nội bộ doanh nghiệp (như gian lận, rò rỉ thông tin, vi phạm kiểm soát nội bộ).<br>4. Soạn thảo báo cáo điều tra và trao đổi kết quả với khách hàng ủy thác.<br>5. Tuân thủ Luật Bảo vệ Dữ liệu Cá nhân và các quy định liên quan để đảm bảo phương pháp điều tra hợp pháp. | เจ้าหน้าที่สืบสวน | เกี่ยวข้องกับความปลอดภัย | การดับเพลิงของทหารและตำรวจ / การรักษาความปลอดภัยที่เกี่ยวข้อง | 1. ดำเนินการสืบสวนด้านความน่าเชื่อถือ ตรวจสอบประวัติ และยืนยันข้อมูลส่วนบุคคลตามที่ได้รับมอบหมาย<br>2. ปฏิบัติงานสืบสวนภาคสนาม ติดตามความเคลื่อนไหว และรวบรวมหลักฐาน<br>3. สัมภาษณ์และวิเคราะห์ข้อมูลสำหรับการสืบสวนภายในองค์กร (เช่น การทุจริต การรั่วไหลของข้อมูล การละเมิดการควบคุมภายใน)<br>4. จัดทำรายงานการสืบสวนและสื่อสารผลการสืบสวนกับผู้ว่าจ้าง<br>5. ปฏิบัติตามกฎหมายคุ้มครองข้อมูลส่วนบุคคลและกฎระเบียบที่เกี่ยวข้อง เพื่อให้แน่ใจว่าวิธีการสืบสวนถูกต้องตามกฎหมาย | Petugas Investigasi | Terkait keamanan | Terkait pemadam kebakaran/keamanan militer dan polisi | 1. Melakukan investigasi kepercayaan, verifikasi latar belakang, dan pemeriksaan data pribadi berdasarkan penugasan.<br>2. Melakukan pengawasan lapangan, penyelidikan keberadaan seseorang, dan pengumpulan bukti.<br>3. Melakukan wawancara dan analisis data untuk investigasi internal perusahaan (seperti kecurangan, kebocoran informasi, pelanggaran kontrol internal).<br>4. Menyusun laporan investigasi dan mengomunikasikan hasilnya kepada klien.<br>5. Mematuhi Undang-Undang Perlindungan Data Pribadi dan peraturan terkait untuk memastikan metode investigasi dilakukan secara sah. |

> AC/AD、AG/AH、AK/AL、AO/AP（B/C 系列）沿用同中類既有葉節點原值，未重新翻譯。

---

## 不列入 add/edit——需人工進一步判斷（6 筆，T欄非空但非單純新增/改名）

以下列 T 欄有內容，但性質是「待分析」「待刪除評估」「待拆分」等流程性任務，不是可直接套用的新增/改名指示，本檔不代為判斷：

| CodeNo | 現行名稱 | 所屬中類 | T欄原文 |
|---|---|---|---|
| 160102 | 汽車研發人員 | 機械工程 | 分析現有履歷資料，是否只選一個值 |
| 160302 | 模具技術人員 | 模具相關 | 撈職缺資料 |
| 170302 | 技術支援主管 | 維修／技術服務 | 分析職缺資訊後移除（刪除候選，非改名） |
| 190125 | 地質師／地質工程師 | 營建規劃 | 職缺拆分到「地質與地球科學研究員」「水土保持技師」兩類；求職者統一分配到「地質與地球科學研究員」（拆分個案，非單一新名） |
| 250509 | 校長 | 教育師資 | 通知客服與高階獵頭處理（流程指示，非分類異動） |
| 260302 | 語文補習班老師 | 補習進修 | 依語種分析職缺資料並修改分類，分不出語種者放到「其他語系老師」（規則性拆分，非單一新名） |

---

## 待進一步討論／已排除（非本次 add/edit 範圍）

- **節目製作人員**：CSV 中重複出現兩次，判定互相矛盾 —— row 561（新聞媒體中類下）T 欄明確標「**不新增**」，理由「與執行製作／助理重疊」；row 579（幕後執行中類下，緊接在 220304 執行製作／助理→執行助理 改名列之後）T 欄卻標「新增」且無附理由。以有明確理由的「不新增」（row 561）為準，判定**不需新增**，排除，不列入 add 清單。
- 社區秘書、其他保安服務工作（皆「1111無此代碼」，保全相關中類下）：CSV 原文標「不新增」但附完整背景說明，顯示廠商端仍有討論空間；本檔不予採用，僅記錄於原始 CSV，若日後重啟討論可回頭查對。
