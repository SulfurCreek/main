#!/usr/bin/env python3
"""104 推薦信驗收：首次提及必定義、禁用詞、職缺名（2026-10-27 起；本人抓到 Peach／JustDating 未定義）。

用法：python3 career/scripts/verify_letter.py <推薦信.md> [--job "<職缺名>"]
檔內每個 ```text 區塊視為一封（方案 A／B），逐封檢查。
"""
import re
import sys

# 產品名 → 首次出現的那一句必須含其中一個定義詞（中英皆可）
ENTITY_DEFS = {
    "JustDating": ["dating app", "交友 App", "交友App", "交友"],
    "Juicy": ["dating app", "follow-up app", "接續產品", "交友"],
    "Peach": ["subscription content app", "content app", "訂閱制內容 App", "內容 App"],
    "KOOL": ["influencer marketplace", "網紅媒合平台", "網紅媒合"],
    "SweetRing": ["dating app", "交友 App", "交友"],
    "CodaPay": ["payment provider", "payment service", "第三方支付", "支付服務", "金流"],
}
BANNED = ["深感契合", "願景高度契合", "在瀏覽貴公司職缺後", "懇請", "積極進取", "抗壓性強",
          "strategic", "passionate", "detail-oriented", "Spearheaded", "proven track record",
          "I am writing", "excited", "thrilled", "1111", "敬上", "可以直接投入", "完全符合"]
SENT = re.compile(r"[^。！？.!?\n]*")


def check(body, job=None):
    errs = []
    for name, defs in ENTITY_DEFS.items():
        i = body.find(name)
        if i < 0:
            continue
        # 首次出現所在的句子
        start = max(body.rfind(c, 0, i) for c in "。！？.!?\n") + 1
        ends = [body.find(c, i) for c in "。！？.!?\n"]
        end = min([e for e in ends if e >= 0] or [len(body)])
        sent = body[start:end]
        if not any(d.lower() in sent.lower() for d in defs):
            errs.append(f"[首次提及未定義] 「{name}」第一次出現的句子沒有交代它是什麼（需含：{'／'.join(defs[:3])}）：{sent.strip()[:60]}")
    for w in BANNED:
        if w in body:
            errs.append(f"[禁用詞] {w}")
    if job and job not in body:
        errs.append(f"[職缺名不符] 找不到「{job}」")
    return errs


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        sys.exit(2)
    job = None
    if "--job" in args:
        job = args[args.index("--job") + 1]
    text = open(args[0], encoding="utf-8").read()
    bodies = [b.split("```")[0] for b in text.split("```text")[1:]]
    if not bodies:
        print("❌ 找不到 ```text 推薦信區塊")
        sys.exit(1)
    bad = 0
    for k, b in enumerate(bodies, 1):
        errs = check(b, job)
        for e in errs:
            print(f"❌ 第 {k} 封：{e}")
        bad += len(errs)
    print("✅ 推薦信驗收通過" if not bad else f"❌ 共 {bad} 項違規")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
