#!/usr/bin/env python3
"""104 推薦信驗收：首次提及必定義、禁用詞、職缺名、結構與長度（2026-10-27 起；2026-11-02 P0／P1 契約修訂）。

用法：python3 career/scripts/verify_letter.py <推薦信.md> [--job "<職缺名>"]
檔內每個 ```text 區塊視為一封（方案 A／B），逐封檢查。
全掃：python3 career/scripts/verify_letter.py --all（略過 archive/ 與 INDEX 標「已投遞」的職缺）；--payment 允許 CodaPay 專名（掃 career/letters/ 與 career/applications/ 下所有含 ```text 的 .md）
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
BANNED = ["同仁整理上百筆職務分類", "同仁對照上百筆職務類別", "同仁對照上百筆職務分類", "深感契合", "願景高度契合", "在瀏覽貴公司職缺後", "懇請", "積極進取", "抗壓性強",
          "strategic", "passionate", "detail-oriented", "Spearheaded", "proven track record",
          "I am writing", "excited", "thrilled", "1111", "敬上", "可以直接投入", "可直接投入", "可用於", "完全符合",
          # 單點硬湊兩件事（2026-10-27）
          "Separately", "另外，", "此外，",
          # 自大結尾與囉嗦詞（2026-10-29 七大鐵律）
          "直接解決", "立即解決", "在工程資源有限下", "帳號、登入、公司資料與聯絡人相關",
          # 稱謂與空洞結尾、中式英文倒裝（2026-10-29）
          "貴司", "我司", "敝司", "工作方向相近", "經驗相關",
          "Backed by", ", which leave",
          # 未核准對外的城市／國籍（facts-prior：國籍不放履歷；新加坡團隊本人裁定不對外）
          "Singapore", "新加坡", "Russian", "俄羅斯"]
SENT = re.compile(r"[^。！？.!?\n]*")
BULLET_LABEL = re.compile(r"^[‧•\-]\s*[^，。；：:\n]{2,12}[：:]", re.M)  # 列點冒號小標
BULLET_HEADLESS = re.compile(r"^[‧•\-]\s*(截至 ?20|帳號權限)", re.M)  # 無頭斷句開頭
# 內部產品代號：預設不寫專名，改白話（警告）；CodaPay 在支付／FinTech 職缺可用（--payment）
OBSCURE_NAMES = ["Peach", "JustDating", "Juicy", "KOOL", "SweetRing"]


def check_closing(body):
    """結尾段須謙和：含「期待」（鐵律 7）。"""
    paras = [p.strip() for p in re.split(r"\n\s*\n", body.strip()) if p.strip()]
    if len(paras) < 2:
        return []
    closing = paras[-2] if paras[-1].replace(" ", "") == "聶崑淮" else paras[-1]
    if "期待" not in closing:
        return [f"[結尾不謙和] 結尾段須以「期待能…」收束：{closing[:40]}"]
    if "貴公司團隊" not in closing:
        return [f"[結尾缺貴公司團隊] 結尾須寫「與貴公司團隊進一步交流」：{closing[:40]}"]
    return []


DIRTY_TITLE = re.compile(
    r"應徵貴公司[^。\n]*(?:<[^>]*>|＜[^＞]*＞|★|關係企業[-_—]|【(?:擴編|急徵)】"
    r"|_(?:新店|台北|內湖|林口|桃園|新竹|台中|高雄|JR\w*|[A-Z0-9]{4,})"
    r"|[（(【\[<＜][^）)】\]>＞。]*(?:年以上|經驗|擴編|急徵|面議|台北|新北|林口|內湖|新店|新竹|台中|高雄|助理)[^）)】\]>＞。]*[）)】\]>＞]"
    r"|【[^】]*／[^】]*／[^】]*】|[｜|]\s*[A-Za-z][A-Za-z0-9\s,/&.-]*。|(?:\[\d+-\d+\]|\bNBO\d+)\s*。)")
HARDWARE_JOB = re.compile(r"製造|硬體|韌體|半導體|航太|電源|工業電腦|搜尋推薦|GARMIN|Garmin|研華|Advantech|旭隼|亞果|鎰福")
AI_JOB = re.compile(r"\bAI\b|人工智慧|AI Labs")


def check_domain(body, job, ctx):
    """領域錯配（2026-11-02）：硬體製造或搜尋推薦職缺不得放 C 端交友 App 案例；AI 職缺結尾須呼應 AI。"""
    errs, scope = [], f"{job or ''} {ctx or ''}"
    if HARDWARE_JOB.search(scope) and ("馬來西亞 iOS" in body or "交友 App" in body):
        errs.append("[領域錯配違規] 硬體製造或搜尋推薦職缺禁止塞入 C 端交友 App 案例！")
    if AI_JOB.search(scope):
        paras = [p for p in re.split(r"\n\s*\n", body.strip()) if "期待" in p]
        if paras and "AI" not in paras[-1]:
            errs.append("[結尾脫節違規] AI 相關職缺之結尾必須呼應 AI 課題！")
    return errs


def check_prior(body):
    """跨經歷概念偷跑（2026-11-02）：條列引用前職 C 端產品，首段須先以「曾…」交代背景。"""
    paras = [p.strip() for p in re.split(r"\n\s*\n", body.strip()) if p.strip()]
    head = paras[0] if paras else ""
    rest = "\n".join(paras[1:])
    if any(w in rest for w in ("交友 App", "訂閱制內容 App", "網紅與商家")) and "曾" not in head:
        return ["[跨經歷概念偷跑] 條列引用前職 C 端 App 案例時，首段必須先交代曾負責相關產品之背景！"]
    return []


def check_title(body):
    """職缺名稱淨化（2026-11-02）：首句不得帶招募備註、集團前綴、★ 公告。"""
    m = DIRTY_TITLE.search(body)
    return [f"[職缺名未淨化] 首句含招募備註或集團前綴：{m.group(0)[:50]}"] if m else []


def warn(body, payment=False):
    """預設不寫內部產品專名（鐵律 1）；有出現時提醒改白話。"""
    names = OBSCURE_NAMES + ([] if payment else ["CodaPay"])
    return [f"[預設不寫專名] 「{n}」建議改白話產品型態（有加分理由才保留）" for n in names if n in body]


def is_zh(body):
    """文件類型：中文字數超過英文字母數視為中文信（中文規則只套中文信）。"""
    return len(re.findall(r"[一-鿿]", body)) > len(re.findall(r"[A-Za-z]", body))


def char_count(body):
    """長度契約：正文（```text 區塊內）去除所有空白後的字元數，含標點、英數與署名。"""
    return len(re.sub(r"\s", "", body))


def extract_bodies(text):
    """共用正文抽取器：回傳 (bodies, errors)。缺 fence、未閉合、空正文、只有稱謂／署名一律報錯。"""
    bodies, errs, pos, k = [], [], 0, 0
    while True:
        i = text.find("```text", pos)
        if i < 0:
            break
        k += 1
        start = text.find("\n", i)
        j = text.find("```", start + 1) if start >= 0 else -1
        if start < 0 or j < 0:
            errs.append(f"第 {k} 封：[fence 未閉合] ```text 區塊沒有結束的 ```")
            break
        body = text[start + 1:j]
        core = re.sub(r"您好[：:，,]?|聶崑淮|Kun Huai Nieh|\s", "", body)
        if not core:
            errs.append(f"第 {k} 封：[空正文] text 區塊沒有內容或只有稱謂／署名")
        else:
            bodies.append(body)
        pos = j + 3
    if k == 0:
        errs.append("[缺正文] 找不到 ```text 推薦信區塊")
    return bodies, errs


def check_structure(body):
    """中文信結構與長度：三個條列、250–350 字（>350 只警告，由 Codex 壓縮）。回傳 (errors, warnings)。"""
    if not is_zh(body):
        return [], []
    errs, warns = [], []
    n_bullets = len(re.findall(r"^‧", body, re.M))
    if n_bullets != 3:
        errs.append(f"[條列數] 中文推薦信須 3 個條列，目前 {n_bullets} 個")
    n = char_count(body)
    if n < 250:
        errs.append(f"[字數不足] {n} 字，中文推薦信須 250–350 字（不含空白）")
    elif n > 350:
        warns.append(f"[字數超標] {n} 字，超過 350 字上限，交 Codex 壓縮")
    return errs, warns


def banned_hits(body):
    """禁用詞：英文詞不分大小寫並加字母邊界，中文詞照字面比對。"""
    hits = []
    for w in BANNED:
        if re.search(r"[A-Za-z]", w):
            pre = r"(?<![A-Za-z])" if w[0].isalpha() else ""
            post = r"(?![A-Za-z])" if w[-1].isalpha() else ""
            if re.search(pre + re.escape(w) + post, body, re.I):
                hits.append(w)
        elif w in body:
            hits.append(w)
    return hits


def check(body, job=None, ctx=""):
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
    for w in banned_hits(body):
        errs.append(f"[禁用詞] {w}")
    for m in BULLET_LABEL.finditer(body):
        errs.append(f"[列點冒號小標] 列點開頭不得加「能力標籤：」：{m.group(0).strip()}")
    for m in BULLET_HEADLESS.finditer(body):
        errs.append(f"[無頭斷句開頭] 每點開頭要自帶場景主詞，不可以「{m.group(1)}」裸奔")
    if not is_zh(body):
        for bad in ("at your company", "requirements contact", "opened 8 payment channels", "Ai "):
            if bad.lower() in body.lower() and (bad != "Ai " or "Ai " in body):
                errs.append(f"[英文直譯腔] 不得出現「{bad.strip()}」（中文「貴公司／需求窗口／開通」的死譯）")
    if not is_zh(body) and re.search(r"[【】]", body):
        errs.append("[英文信含中文全形括號] 英文信不得出現【】：代碼改成 (CODE)，公司名或口號直接移除")
    if is_zh(body):  # 中文專屬規則不套英文信
        errs += check_closing(body)
        errs += check_title(body)
        errs += check_prior(body)
    errs += check_domain(body, job, ctx)
    if job and job not in body:
        errs.append(f"[職缺名不符] 找不到「{job}」")
    return errs


def header_context(text):
    """草稿檔頭契約：｜j-<code> <公司>｜<對外職稱>｜分級。回傳 (code, company, job) 或 None。"""
    m = re.search(r"｜j-(\w+) ([^｜]*)｜([^｜]*)｜分級", text)
    return (m.group(1), m.group(2).strip(), m.group(3).strip()) if m else None


def submitted_codes(root):
    """applications/INDEX.md 中「應徵狀態」含「已投遞／已應徵／不投遞／已面試」的職缺代碼（不再掃描）。"""
    idx = root / "applications" / "INDEX.md"
    out = set()
    if idx.exists():
        for line in idx.read_text(encoding="utf-8").splitlines():
            m = re.match(r"\|\s*\[([0-9a-z]+)\]", line)
            if m and any(w in line for w in ("已投遞", "已應徵", "不投遞", "已面試")):
                out.add(m.group(1))
    return out


def verify_text(text, job=None, ctx="", payment=False, label=""):
    """單封與批次共用：抽取→結構→內容。回傳 (n_bodies, errors, warnings)。"""
    bodies, errs = extract_bodies(text)
    errs = [f"{label}{e}" for e in errs]
    warns = []
    for k, b in enumerate(bodies, 1):
        e2, w2 = check_structure(b)
        e2 += check(b, job, ctx)
        w2 += warn(b, payment)
        errs += [f"{label}第 {k} 封：{e}" for e in e2]
        warns += [f"{label}第 {k} 封：{w}" for w in w2]
    return len(bodies), errs, warns


def run_all(root, payment=False):
    submitted = submitted_codes(root)
    files, skipped = [], []
    for d in ("letters", "applications"):
        for p in sorted((root / d).rglob("*.md")):
            if "archive" in p.parts or "```text" not in p.read_text(encoding="utf-8"):
                continue
            code = re.match(r"([0-9a-z]{5})(?:-|\.md$)", p.name)
            if code and code.group(1) in submitted:
                skipped.append((p, "已投遞／不投遞／已面試"))
                continue
            files.append(p)
    total_err, verified, no_ctx = 0, 0, []
    for f in files:
        text = f.read_text(encoding="utf-8")
        ctxh = header_context(text)
        if not ctxh:  # 成品沒有檔頭：找同代碼草稿的檔頭
            m = re.match(r"([0-9a-z]{5})(?:-|\.md$)", f.name)
            drafts = sorted(f.parent.glob(f"{m.group(1)}-*-draft.md")) if m else []
            ctxh = header_context(drafts[0].read_text(encoding="utf-8")) if drafts else None
        job, ctx = (ctxh[2], ctxh[1]) if ctxh else (None, "")
        if not ctxh:
            no_ctx.append(f.relative_to(root))
        n, errs, warns = verify_text(text, job, ctx, payment, f"{f.relative_to(root)} ")
        verified += n
        for w in warns:
            print(f"⚠️ {w}")
        for e in errs:
            print(f"❌ {e}")
        total_err += len(errs)
    for p, why in skipped:
        print(f"略過（{why}）：{p.relative_to(root)}")
    for p in no_ctx:
        print(f"⚠️ 未完成對位驗證（缺職缺／公司上下文，只做通用檢查）：{p}")
    print(f"掃描 {len(files)} 檔、驗證 {verified} 封、略過 {len(skipped)} 檔、缺上下文 {len(no_ctx)} 檔")
    if verified == 0:
        print("❌ 未驗證任何信件，不得視為通過")
        return 1
    print("✅ 0 違規" if not total_err else f"❌ 共 {total_err} 項違規")
    return 1 if total_err else 0


def main(argv=None):
    import argparse
    import pathlib
    ap = argparse.ArgumentParser(description="104 推薦信驗收")
    ap.add_argument("file", nargs="?", help="推薦信 md 檔")
    ap.add_argument("--all", action="store_true", help="掃描 career/letters 與 applications")
    ap.add_argument("--job", help="職缺對外名稱（淨化後）；未給時讀草稿檔頭")
    ap.add_argument("--company", default="", help="公司名稱或產業，用於領域錯配與 AI 結尾檢查")
    ap.add_argument("--payment", action="store_true", help="允許 CodaPay 專名")
    try:
        a = ap.parse_args(argv)
    except SystemExit:
        return 2
    if a.all:
        return run_all(pathlib.Path(__file__).resolve().parents[1], a.payment)
    if not a.file:
        ap.print_usage()
        return 2
    try:
        text = open(a.file, encoding="utf-8").read()
    except OSError as e:
        print(f"❌ 無法讀取檔案：{e}")
        return 2
    ctxh = header_context(text)
    job = a.job or (ctxh[2] if ctxh else None)
    ctx = f"{a.company} {ctxh[1] if ctxh else ''}".strip()
    if not job and not ctx:
        print("⚠️ 未完成對位驗證：缺職缺名與公司（請給 --job、--company，或使用含檔頭的草稿）")
    n, errs, warns = verify_text(text, job, ctx, a.payment)
    for w in warns:
        print(f"⚠️ {w}")
    for e in errs:
        print(f"❌ {e}")
    if n == 0 and not errs:
        print("❌ 未驗證任何信件")
        return 1
    print("✅ 推薦信驗收通過" if not errs else f"❌ 共 {len(errs)} 項違規")
    return 1 if errs else 0


if __name__ == "__main__":
    sys.exit(main())
