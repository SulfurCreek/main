#!/usr/bin/env python3
"""退役入口，保留以免舊指令被誤認為現行工具；不執行任何檢查。"""
import json
import sys

if __name__ == "__main__":
    print(json.dumps({
        "status": "retired",
        "checks_executed": False,
        "message": "舊履歷結構與機械比對檢查已停用。依 WRITER_GOVERNANCE.md 與當輪指定來源作業；本入口不判定品質或是否可交付。"
    }, ensure_ascii=False))
    sys.exit(2)
