# Housekeeper交接｜jobs.json新增resume_review

## 可直接交給housekeeper的指令

請保留並支援 SulfurCreek/main 的 automation/104-data 分支 career/targets/104/jobs.json 中新欄位 `jobs.<job_id>.resume_review`。
新增commit：5d2136327304887a99172550f97c5893382d6b9e；分類基底JD版本：09a7c2358f1190c6a4921f7f86e5c86d83c0d8fd。137筆均已分類，職缺代碼是關聯鍵。
這是Codex按JD人工判讀的衍生註記，不是104回傳欄位，不是本人應徵狀態，也不是能力評分。
更新同步器時，請按job_id保留此物件，不要在全量覆寫時丟掉，也不要將它反向送進104。
若新JD的description實質改變，保留舊註記但標stale、排入重審；不要自動重新判定PM或改寫reason。首次沒有分類的新職缺保持未分類，不以職稱自動補yes。
如專案政策要求把衍生註記拆到sidecar，請以job_id等值遷移，保留全部來源與分類欄位，同步更新JOB_TRACKS/HR索引，不能直接刪除。
請只在既有工作分支按權限修改；main分支不動。完成後回報是否確保下一次同步不會覆蓋分類。本次Codex沒有修改同步器，故「跨同步保留」仍待housekeeper實作。

## Schema v1

```json
{
  "resume_review": {
    "schema_version": 1,
    "track": "PM",
    "specialty": "第三方支付變現",
    "pm_line": "yes",
    "v13_fit": "primary",
    "reason": "支付策略、roadmap、夥伴收益與市場變現。",
    "jd_anchor": "推動產品變現",
    "jd_source_sha": "09a7c2358f1190c6a4921f7f86e5c86d83c0d8fd",
    "jd_fetched_at": "來源該筆fetched_at原值",
    "classified_at": "2026-11-03",
    "reviewer": "agent_proposed_primary_reviewed"
  }
}
```

track枚舉：PM、PM_PO、PO、PROJECT、SOLUTION、HARDWARE、OPERATIONS、DATA_ANALYST、REVIEW。
pm_line：yes、conditional、no。v13_fit：primary、partial、not_target。
reviewer記來源：agent_proposed_primary_reviewed或primary_assistant，不代表真人公司背書。
原欄位與description全部保留；本輪未改投遞狀態/地點/職稱/擷取時間。

## 索引

- [JOB_TRACKS.md](JOB_TRACKS.md)：137筆人讀清單及33筆未投PM線。
- [INDEX.md](INDEX.md)：現行HR入口，表格跳脫錯誤已修。
- [REPORT.md](runs/2026-11-03-585ee01/REPORT.md)：固定草稿招聘診斷；沒有PDF/正式gate通過宣稱。
