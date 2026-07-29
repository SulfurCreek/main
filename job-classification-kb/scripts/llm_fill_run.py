"""步驟2：批次呼叫 LLM 取得候選職類，結果落地快取（可中斷續跑）。"""
import json, os, re, subprocess, sys
from concurrent.futures import ThreadPoolExecutor, as_completed

SCRATCH = "/tmp/claude-0/-home-user-main/6d643d58-f39d-53f8-a740-df69060d043b/scratchpad/llmfill"
CACHE = f"{SCRATCH}/cache"
BATCH, WORKERS, TIMEOUT, RETRY = 30, 24, 240, 3

os.makedirs(CACHE, exist_ok=True)
titles = json.load(open(f"{SCRATCH}/titles.json", encoding='utf-8'))
duty = open(f"{SCRATCH}/duty_data.txt", encoding='utf-8').read()

TPL = """你是職務類別推薦系統。從清單中為每個關鍵字推薦最相關職類。

# 職務類別清單
{duty}

# 關鍵字（編號<TAB>關鍵字）
{kw}

# 輸出
純JSON物件不要markdown。key=編號字串，value=字串陣列，每項格式「類別名稱|分數」，最多8項，分數0-100由高到低。類別名稱必須完全出自上述清單。
範例：{{"1":["秘書|95","行政人員|88"],"2":["廚師|90"]}}
每個編號都要有。"""


def parse(out, chunk):
    m = re.search(r'\{.*\}', out, re.S)
    if not m:
        return None
    data = json.loads(m.group(0))
    res = {}
    for k, v in data.items():
        try:
            t = chunk[int(k) - 1]
        except (ValueError, IndexError):
            continue
        cands = []
        for item in v if isinstance(v, list) else []:
            if not isinstance(item, str) or '|' not in item:
                continue
            name, _, sc = item.rpartition('|')
            try:
                cands.append([name.strip(), int(re.sub(r'\D', '', sc) or 0)])
            except ValueError:
                pass
        if cands:
            res[t] = cands
    return res or None


def work(bi):
    path = f"{CACHE}/b{bi:05d}.json"
    if os.path.exists(path):
        return bi, 'skip'
    chunk = titles[bi * BATCH:(bi + 1) * BATCH]
    kw = '\n'.join(f'{i+1}\t{t}' for i, t in enumerate(chunk))
    prompt = TPL.format(duty=duty, kw=kw)
    for _ in range(RETRY):
        try:
            p = subprocess.run(['claude', '-p', '--model', 'haiku'],
                               input=prompt, capture_output=True, text=True, timeout=TIMEOUT)
            res = parse(p.stdout, chunk)
            if res:
                json.dump(res, open(path, 'w', encoding='utf-8'), ensure_ascii=False)
                return bi, 'ok'
        except Exception:
            pass
    return bi, 'fail'


def main():
    nb = (len(titles) + BATCH - 1) // BATCH
    todo = [i for i in range(nb) if not os.path.exists(f"{CACHE}/b{i:05d}.json")]
    print(f"總批次 {nb}，待處理 {len(todo)}", flush=True)
    done = fail = 0
    with ThreadPoolExecutor(max_workers=WORKERS) as ex:
        futs = [ex.submit(work, i) for i in todo]
        for f in as_completed(futs):
            _, st = f.result()
            done += 1
            fail += st == 'fail'
            if done % 25 == 0:
                print(f"  進度 {done}/{len(todo)}  失敗 {fail}", flush=True)
    print(f"完成 {done}，失敗 {fail}", flush=True)
    return 1 if fail else 0


if __name__ == '__main__':
    sys.exit(main())
