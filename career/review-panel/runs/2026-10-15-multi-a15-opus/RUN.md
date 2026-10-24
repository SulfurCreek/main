# 執行單（多職缺）
子代理指令（一句話）：

```
讀 career/review-panel/runs/2026-10-15-multi-a15-opus/raw/prompt_<ID>.md 並照做；用「一次」Bash 指令把單行 JSON 寫到 career/review-panel/runs/2026-10-15-multi-a15-opus/raw/<ID>.json；A 類接著執行 python3 /home/user/main/.claude/skills/resume-review-panel/scripts/schema_v4.py validate career/review-panel/runs/2026-10-15-multi-a15-opus/raw/<ID>.json；不要讀其他檔案；回覆只寫 done＋decision。
```

工作清單（45）：A_jd03_v9.5、A_jd03_v9.6、B_jd03、A_jd09_v9.5、A_jd09_v9.6、B_jd09、A_jd11_v9.5、A_jd11_v9.6、B_jd11、A_jd14_v9.5、A_jd14_v9.6、B_jd14、A_jd20_v9.5、A_jd20_v9.6、B_jd20、A_jd26_v9.5、A_jd26_v9.6、B_jd26、A_jd30_v9.5、A_jd30_v9.6、B_jd30、A_jd31_v9.5、A_jd31_v9.6、B_jd31、A_jd32_v9.5、A_jd32_v9.6、B_jd32、A_jd34_v9.5、A_jd34_v9.6、B_jd34、A_jd36_v9.5、A_jd36_v9.6、B_jd36、A_jd40_v9.5、A_jd40_v9.6、B_jd40、A_jd43_v9.5、A_jd43_v9.6、B_jd43、A_jd44_v9.5、A_jd44_v9.6、B_jd44、A_jd47_v9.5、A_jd47_v9.6、B_jd47

完成後：python3 /home/user/main/.claude/skills/resume-review-panel/scripts/multi_report.py --run career/review-panel/runs/2026-10-15-multi-a15-opus
