#!/usr/bin/env python3
"""事實保存比對（中英文共用，2026-11-02）。

用途：下游成品與「指定上游版本」逐區塊比對，程式能確定的改動直接拒絕，
不能機械判定的部分列入「主代理人工查核」，不宣稱完成語意驗證。

可機械判定（拒絕）：
1. 數字＋單位：88% 改 88 件、10 件改 10 家（multiset 比對，不只比數字）。
2. 上游鎖定事實 [LOCK_FACTS: 對象=數值; …]：對象與數值須在同一句、對象在數值之前且相距 ≤ 20 字，
   可攔截「甲產品 10 件／乙產品 20 件」對調。純字串項目須原樣存在。
3. 完成狀態：上游為開發中／規劃中／預計（in development / planned），下游不得改寫成已上線（launched / live）。
4. 限定詞：約、近、逾、超過、以上、至少、團隊、協助、參與（about、nearly、more than、at least、team …）
   在同一區塊的出現次數不得減少。

只能人工查核（回報，不判失敗）：責任歸屬與因果是否被改寫、比較組語意、限定詞換位置後的語意。
"""
import re
from collections import Counter

ZH_UNITS = r"%|％|件|家|名|筆|天|項|次|倍|萬|億|年|個月|月|週|位|人|張|國|種|成|元"
EN_UNITS = r"%|percent|requests?|clients?|employers?|features?|cases?|accounts?|days?|weeks?|months?|years?|times|tables?|members?|countries|markets?|channels?"
NUM = r"\d+(?:[.,]\d+)*"

# 限定詞以「語境 regex」計數，避免「邀約」「限制」「團隊合作」等一般詞誤判
ZH_LIMITERS = {"約": r"約\s*\d", "近": r"近\s*\d", "逾": r"逾\s*\d", "超過": r"超過\s*\d", "至少": r"至少\s*\d",
               "以上": r"\d[^。，；\n]{0,6}以上", "左右": r"\d[^。，；\n]{0,6}左右", "團隊歸因": r"團隊(?:已)?(?:完成|上線|推出|處理)",
               "協助": r"協助", "參與": r"參與", "限定口徑": r"[（(]限|限[^制定度時期]{0,8}者"}
EN_LIMITERS = {w: r"\b%s\b" % w for w in ("about", "nearly", "approximately", "more than", "at least", "helped", "contributed", "supported")}
EN_LIMITERS["over"] = r"\bover\s+\d"
EN_LIMITERS["team"] = r"\bthe team\b|\bteam (?:resolved|completed|shipped|delivered)"
ZH_PENDING = r"開發中|規劃中|預計|試行|尚未上線"
ZH_DONE = r"已上線|正式上線|已推出|全面上線"
EN_PENDING = r"in development|planned|under development|upcoming|pilot"
EN_DONE = r"\blaunched\b|\bshipped\b|\bwent live\b|\bis live\b|\breleased\b"


def is_en(text):
    return len(re.findall(r"[A-Za-z]", text)) > len(re.findall(r"[一-鿿]", text))


def number_units(text):
    """數字＋單位的 multiset；沒有單位的數字以空字串記單位。"""
    units = EN_UNITS if is_en(text) else ZH_UNITS
    out = Counter()
    for m in re.finditer(r"(%s)\s*(%s)?" % (NUM, units), text, re.I):
        out[(m.group(1).replace(",", ""), (m.group(2) or "").lower().rstrip("s"))] += 1
    return out


def limiter_counts(text):
    words = EN_LIMITERS if is_en(text) else ZH_LIMITERS
    flags = re.I if is_en(text) else 0
    return {w: len(re.findall(rx, text, flags)) for w, rx in words.items()}


def parse_lock_facts(raw):
    """[LOCK_FACTS: 甲產品=10 件; 乙產品=20 件; 開發中] → [("甲產品","10 件"), (None,"開發中")]。"""
    items = []
    for part in re.split(r"[;；]", raw or ""):
        part = part.strip()
        if not part:
            continue
        if "=" in part:
            k, v = part.split("=", 1)
            items.append((k.strip(), v.strip()))
        else:
            items.append((None, part))
    return items


def _norm(s):
    return re.sub(r"\s+", "", s)


def lock_fact_errors(lock_items, text):
    errs = []
    flat = _norm(text)
    sentences = [_norm(s) for s in re.split(r"[。！？；\n]|(?<=[a-z0-9])\.\s", text)]
    for obj, val in lock_items:
        v = _norm(val)
        if obj is None:
            if v not in flat:
                errs.append(f"鎖定事實「{val}」不見了")
            continue
        o = _norm(obj)
        ok = False
        for s in sentences:
            for m in re.finditer(re.escape(v), s):
                head = s[:m.start()]
                i = head.rfind(o)
                if i >= 0 and m.start() - (i + len(o)) <= 20:
                    # 對象與數值之間不得夾著另一個鎖定對象（防對調）
                    between = head[i + len(o):]
                    if not any(_norm(o2) in between for o2, _ in lock_items if o2 and _norm(o2) != o):
                        ok = True
        if not ok:
            errs.append(f"鎖定事實「{obj}={val}」的對象與數值不在同一句或已被調換")
    return errs


def compare_block(up, down, lock_items=()):
    """回傳 (errors, manual)。errors：程式可確定的事實改動；manual：需主代理人工查核的項目。"""
    errs, manual = [], []
    nu, nd = number_units(up), number_units(down)
    if nu != nd:
        miss = list((nu - nd).elements())
        extra = list((nd - nu).elements())
        errs.append(f"[數字單位異動] 少了 {miss} 多了 {extra}")
    errs += [f"[鎖定事實] {e}" for e in lock_fact_errors(lock_items, down)]
    en = is_en(up)
    pend, done = (EN_PENDING, EN_DONE) if en else (ZH_PENDING, ZH_DONE)
    flags = re.I if en else 0
    if re.search(pend, up, flags) and not re.search(pend, down, flags):
        errs.append("[完成狀態升級] 上游為開發中／規劃中，成品刪除了未完成狀態")
    if re.search(done, down, flags) and not re.search(done, up, flags) and not re.search(r"上線|推出" if not en else r"live|launch", up, flags):
        errs.append("[完成狀態升級] 成品出現上游沒有的已上線說法")
    lu, ld = limiter_counts(up), limiter_counts(down)
    dropped = [w for w in lu if ld.get(w, 0) < lu[w]]
    if dropped:
        errs.append(f"[限定詞刪除] 減少了：{'、'.join(dropped)}")
    if _norm(up) != _norm(down):
        manual.append("責任歸屬、因果與比較組語意：程式無法判定，需主代理人工查核")
    return errs, manual
