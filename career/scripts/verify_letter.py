#!/usr/bin/env python3
"""104 推薦信驗收：首次提及必定義、禁用詞、職缺名（2026-10-27 起；本人抓到 Peach／JustDating 未定義）。

用法：python3 career/scripts/verify_letter.py <推薦信.md> [--job "<職缺名>"]
檔內每個 ```text 區塊視為一封（方案 A／B），逐封檢查。
全掃：python3 career/scripts/verify_letter.py --all（掃 career/letters/ 與 career/applications/ 下所有含 ```text 的 .md）
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
          "I am writing", "excited", "thrilled", "1111", "敬上", "可以直接投入", "可直接投入", "可用於", "完全符合",
          # 單點硬湊兩件事（2026-10-27）
          "Separately,", "Separately ", "另外，", "此外，",
          # 未核准對外的城市／國籍（facts-prior：國籍不放履歷；新加坡團隊本人裁定不對外）
          "Singapore", "新加坡", "Russian", "俄羅斯"]
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
    if args[0] == "--all":
        import pathlib
        root = pathlib.Path(__file__).resolve().parents[1]
        files = sorted(p for d in ("letters", "applications") for p in (root / d).rglob("*.md") if "```text" in p.read_text(encoding="utf-8"))
        total = 0
        for f in files:
            bodies = [b.split("```")[0] for b in f.read_text(encoding="utf-8").split("```text")[1:]]
            for k, b in enumerate(bodies, 1):
                for e in check(b):
                    print(f"❌ {f.relative_to(root)} 第 {k} 封：{e}")
                    total += 1
        print(f"掃描 {len(files)} 檔；" + ("✅ 0 違規" if not total else f"❌ 共 {total} 項違規"))
        sys.exit(1 if total else 0)
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
