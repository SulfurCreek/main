# 02 — 工作流程 (Workflow)

## 核心理念

**不要每次都從 Excel 讀資料。** 建立一個 MD 檔當中間資料層，從那裡讀取；改完再更新回 Excel，但**更新前一定先對照 (diff)**。

```
Excel/CSV  ──export──▶  MD (資料層)  ──apply──▶  對照版 Excel (交付)
                          ▲                ▲
                       手動編輯          先 diff 再寫
                       (改正解)
```

## 三個指令

| 指令 | 用途 | 會寫檔？ |
|---|---|---|
| `python3 sync_md.py export` | Excel/CSV → MD（初始化或重建） | 寫 MD |
| `python3 sync_md.py diff` | 顯示 MD 會對 Excel 造成的差異 | 否 |
| `python3 sync_md.py apply --confirm` | 先顯示 diff，確認後寫入對照版 Excel | 寫 Excel |

> `apply` 不帶 `--confirm` 時只顯示前 30 筆差異、不寫入；帶 `--confirm` 才真正寫。

## 標準修正流程（個案微調）

當使用者回報「某個 eNo 判錯了」：

1. **看資料**：在 MD 找到該 eNo 那列，確認現有 5 格與目前正解。
2. **判斷類型**：
   - 純粹正解設錯 → 只改 MD 的「正解」欄。
   - 規則性錯誤（會影響同型案例）→ 改 `plan()` 規則 + 改 MD 正解。
3. **回歸測試**：跑 [logic/02](../logic/02-verified-logic.md) 的校準案例，確認沒有退化。
4. **diff**：`python3 sync_md.py diff`，確認只動到預期的列。
5. **apply**：`python3 sync_md.py apply --confirm`。
6. **重建北三區 sheet**（apply 只重建主表，北三區要另跑，見下）。
7. 重大變動 → 做三輪自我審查再回報。

## 重建北三區 sheet

`sync_md.py apply` 產生的是單一「不合理清單」工作表。北三區需另外拆出（程式碼見 [scripts/sync_md.py](../scripts/sync_md.py) 的 `split_region` 函式，或手動）：

```python
# 從對照版主表複製「分區含台北三區」的列到新 sheet「北三區」
# 保留所有格式（刪除線、配色、欄寬、凍結窗格 H2）
```

## 注意事項（血淚教訓）

- **build 的 mode 分支要齊全**：`plan()` 回傳的每一種 mode（keep / keep_strike / replace / replace_multi / replace_all / add）在 `build_excel` 都要有對應寫入邏輯。曾經改 `replace_multi` 時誤刪 `replace` 分支，導致 226 筆判斷正確卻沒寫進 Excel。詳見 [logic/03](../logic/03-pitfalls.md)。
- **檔案系統會重置**：容器環境下 `/home/claude/*.pkl` 可能消失，需從 `TCode_Export` 重新載入 duty 資料。
- **MD 不再給使用者**：MD 是 Claude 自己維護的資料層，使用者只看對照版 Excel。規則學習持久化在記憶/本知識庫。
