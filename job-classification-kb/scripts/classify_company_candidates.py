"""把括號品牌候選詞交給 LLM 判定是否為「公司／品牌名稱」。

輸出 _company_brand_labels.json： 候選詞 -> 標籤
標籤：品牌 / 產業 / 職務 / 其他
"""
import json, subprocess, concurrent.futures as cf, re

IN = '/home/user/main/job-classification-kb/scripts/_company_tokens.json'
OUT = '/home/user/main/job-classification-kb/scripts/_company_brand_labels.json'
BATCH = 40
WORKERS = 24

cands = list(json.load(open(IN, encoding='utf-8'))['brand_candidates'].keys())
print(f"候選 {len(cands):,} 個")

PROMPT = """判斷每個詞是不是「公司名稱或商業品牌名稱」（含店名、連鎖品牌、集團名）。
分類標籤只能是下列四種之一：
品牌 = 公司名或商業品牌/店名（例：DHL、寶雅、CoCo都可、大樹藥局）
產業 = 產業或業務領域名稱（例：半導體、物流、餐飲）
職務 = 職務、工作內容、工作條件（例：儲備幹部、早班、無經驗可）
其他 = 地名、數字、其他無法歸類

每行輸出「詞|標籤」，不要有其他文字。共 {n} 個詞：
{items}"""


def run(batch):
    p = PROMPT.format(n=len(batch), items='\n'.join(batch))
    try:
        r = subprocess.run(['claude', '-p', '--model', 'haiku'], input=p,
                           capture_output=True, text=True, timeout=300)
        out = {}
        for line in r.stdout.splitlines():
            if '|' in line:
                w, _, lab = line.rpartition('|')
                w, lab = w.strip(), lab.strip()
                if w in batch and lab in ('品牌', '產業', '職務', '其他'):
                    out[w] = lab
        return out
    except Exception as e:
        print('err', e)
        return {}


batches = [cands[i:i + BATCH] for i in range(0, len(cands), BATCH)]
labels = {}
with cf.ThreadPoolExecutor(WORKERS) as ex:
    for i, res in enumerate(ex.map(run, batches), 1):
        labels.update(res)
        if i % 20 == 0:
            print(f"{i}/{len(batches)} 批，已標 {len(labels):,}")

json.dump(labels, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
import collections
print(collections.Counter(labels.values()))
print(f"未標到 {len(cands) - len(labels)} 個")
print(f"已存 {OUT}")
