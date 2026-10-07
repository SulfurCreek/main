#!/usr/bin/env python3
"""履歷機械掃描：可重複、不靠 LLM 判斷的指標。
用法：python3 scan.py <履歷.md>            # 單份
      python3 scan.py --pool <candidates 目錄>  # 對 50 份同儕池算分並檢查與品質分級的相關
"""
import re, sys, glob, os

BUZZ = ['賦能','驅動','顯著','無縫','指數級','戰略性','卓越','締造','擘劃','結果導向','充滿熱情','熱情積極',
        '高效','端到端','全生命週期','創新解決方案','數據驅動','跨職能','生態系','高可用','低延遲','成功交付']
JARGON = ['API','HMAC','SSOT','MECE','狀態機','契約','Timebox','Kanban','Waterfall','Cohort','p=','重放','限流',
          'PR/FAQ','UAT','RBAC','OAuth','Webhook','冪等','Kafka','MQTT','Kubernetes','gRPC','WebSocket','RAG','微服務','DevOps','CI/CD']
SOFT = ['訪談','傾聽','說服','對齊','投票','致歉','道歉','帶','一對一','實習生','陪','回饋','客服','法務','稽核',
        '夥伴','窗口','跨國','共識','教','問答','不做','吵','談']
DUTY = re.compile(r'^- *負責')

def metrics(text):
    lines=[l for l in text.splitlines() if l.strip().startswith('-')]
    n=max(len(lines),1)
    num_lines=sum(1 for l in lines if re.search(r'\d',l))
    baseline=sum(1 for l in lines if re.search(r'\d+(\.\d+)?\s*[%％萬千天倍人家項個]?\s*(→|到|降至|提升至|提升到|從)',l) or re.search(r'從.*\d.*(到|→)',l))
    m=dict(
        bullets=len(lines),
        num_ratio=round(num_lines/n,2),
        baseline_ratio=round(baseline/n,2),
        duty_ratio=round(sum(1 for l in lines if DUTY.match(l.strip()))/n,2),
        buzz=sum(text.count(w) for w in BUZZ),
        jargon=sum(text.count(w) for w in JARGON),
        soft=sum(text.count(w) for w in SOFT),
        chars=len(text),
    )
    m['jargon_per_1k']=round(m['jargon']*1000/max(m['chars'],1),1)
    # 綜合分（0–100），權重見 SKILL.md；設計時未看 50 份的分級結果
    s=50
    s+=20*m['num_ratio']+15*m['baseline_ratio']
    s+=min(m['soft'],8)*2.5
    s-=30*m['duty_ratio']
    s-=min(m['buzz'],8)*4
    s-=max(m['jargon_per_1k']-8,0)*1.5
    m['score']=round(max(0,min(100,s)),1)
    return m

def pool(d):
    idx=open(os.path.join(d,'index.md')).read()
    tier={int(r[0]):r[1] for r in re.findall(r'^\| (\d\d) \|.*\| ([ABC]) \|',idx,re.M)}
    res={}
    for f in sorted(glob.glob(os.path.join(d,'resumes-*.md'))):
        for block in re.split(r'\n---\n',open(f).read()):
            mm=re.search(r'^## (\d\d) ',block,re.M)
            if mm: res[int(mm.group(1))]=metrics(block)
    by={t:[res[i]['score'] for i in res if tier.get(i)==t] for t in 'ABC'}
    for t in 'ABC':
        v=sorted(by[t]); print(t,len(v),'平均',round(sum(v)/len(v),1),'最低',v[0],'最高',v[-1])
    # 成對排序正確率：A>B、B>C、A>C 的比例
    def pair(x,y):
        tot=ok=0
        for a in by[x]:
            for b in by[y]:
                tot+=1; ok+= a>b; ok+= 0.5*(a==b)
        return round(ok/tot,2)
    print('A>B',pair('A','B'),'B>C',pair('B','C'),'A>C',pair('A','C'))
    return res,tier

if __name__=='__main__':
    if sys.argv[1]=='--pool': pool(sys.argv[2])
    else:
        for k,v in metrics(open(sys.argv[1]).read()).items(): print(f'{k}: {v}')
