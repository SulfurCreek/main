"""步驟1：抽出需補齊的不重複標題清單 + 準備 duty_data prompt 素材。"""
import pandas as pd, json

SCRATCH = "/tmp/claude-0/-home-user-main/6d643d58-f39d-53f8-a740-df69060d043b/scratchpad/llmfill"
df = pd.read_csv('training_feedback/推薦模型訓練回饋.csv', skiprows=1, dtype=str)
POS = [f'正向推薦{i}' for i in range(1,6)]
need = df[df[POS].notna().sum(axis=1) < 5]
titles = sorted(need['職缺名稱'].unique())
json.dump(titles, open(f'{SCRATCH}/titles.json','w',encoding='utf-8'), ensure_ascii=False)
leaves = json.load(open('scripts/_dutynm_leaves.json',encoding='utf-8'))
open(f'{SCRATCH}/duty_data.txt','w',encoding='utf-8').write('、'.join(leaves))
print('標題數:', len(titles), '| 葉數:', len(leaves))
