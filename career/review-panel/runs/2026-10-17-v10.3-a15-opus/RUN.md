# 執行單（多職缺）
子代理指令（一句話）：

```
讀 career/review-panel/runs/2026-10-17-v10.3-a15-opus/raw/prompt_<ID>.md 並照做；用「一次」Bash 指令把單行 JSON 寫到 career/review-panel/runs/2026-10-17-v10.3-a15-opus/raw/<ID>.json；A 類接著執行 python3 /home/user/main/.claude/skills/resume-review-panel/scripts/schema_v4.py validate career/review-panel/runs/2026-10-17-v10.3-a15-opus/raw/<ID>.json；不要讀其他檔案；回覆只寫 done＋decision。
```

工作清單（15）：A_jd03_v10.3、A_jd09_v10.3、A_jd11_v10.3、A_jd14_v10.3、A_jd20_v10.3、A_jd26_v10.3、A_jd30_v10.3、A_jd31_v10.3、A_jd32_v10.3、A_jd34_v10.3、A_jd36_v10.3、A_jd40_v10.3、A_jd43_v10.3、A_jd44_v10.3、A_jd47_v10.3

完成後：python3 /home/user/main/.claude/skills/resume-review-panel/scripts/multi_report.py --run career/review-panel/runs/2026-10-17-v10.3-a15-opus
