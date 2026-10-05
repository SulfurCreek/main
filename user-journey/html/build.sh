#!/bin/sh
# 一鍵重建：解析 md → 組裝 HTML →（可選）--test 跑煙霧測試。HackMD Sitemap／流程圖有變時先跑 step0（需 HACKMD_TOKEN）。
set -e
cd "$(dirname "$0")"
python3 step1_parse_journey.py
python3 step2_build_report.py ${FRAGMENT:+--fragment "$FRAGMENT"}
[ "$1" = "--test" ] && NODE_PATH=${NODE_PATH:-/opt/node22/lib/node_modules} node tests/smoke.js
true
