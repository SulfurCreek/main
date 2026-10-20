#!/usr/bin/env python3
"""Calculate deterministic calibration metrics for a hidden answer key and blind scores."""
import argparse, json, math, statistics as st

def ranks(values):
    order=sorted(range(len(values)), key=lambda i: values[i]); out=[0.0]*len(values); i=0
    while i<len(values):
        j=i+1
        while j<len(values) and values[order[j]]==values[order[i]]: j+=1
        rank=(i+j-1)/2+1
        for k in range(i,j): out[order[k]]=rank
        i=j
    return out

def pearson(a,b):
    ma,mb=st.mean(a),st.mean(b)
    num=sum((x-ma)*(y-mb) for x,y in zip(a,b))
    den=math.sqrt(sum((x-ma)**2 for x in a)*sum((y-mb)**2 for y in b))
    return num/den if den else 0.0

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('answer_key'); ap.add_argument('scores'); ap.add_argument('-o','--output')
    args=ap.parse_args()
    key=json.load(open(args.answer_key)); scored=json.load(open(args.scores)); sm={x['id']:x for x in scored}
    if len(key)!=len(scored) or set(sm)!={x['id'] for x in key}: raise SystemExit('ID sets differ')
    rows=[]
    for x in key:
        actual=sm[x['id']]['total']; target=x['target_total']
        if actual!=sum(sm[x['id']]['scores'].values()): raise SystemExit(f"bad total: {x['id']}")
        rows.append({'id':x['id'],'level':x['level'],'target':target,'actual':actual,'error':actual-target})
    target=[x['target'] for x in rows]; actual=[x['actual'] for x in rows]
    eligible=inv=ties=0
    for a in rows:
        for b in rows:
            if b['level']>=a['level']+2:
                eligible+=1
                if a['actual']>b['actual']: inv+=1
                elif a['actual']==b['actual']: ties+=1
    means={str(level):st.mean(x['actual'] for x in rows if x['level']==level) for level in sorted({x['level'] for x in rows})}
    result={'n':len(rows),'spearman':pearson(ranks(target),ranks(actual)),
            'mae':st.mean(abs(x['error']) for x in rows),'bias':st.mean(x['error'] for x in rows),
            'max_abs_error':max(abs(x['error']) for x in rows),'level_means':means,
            'strict_inversions':inv,'eligible_pairs_2plus':eligible,'strict_inversion_rate':inv/eligible if eligible else 0,'ties':ties}
    text=json.dumps(result,ensure_ascii=False,indent=2)
    if args.output: open(args.output,'w').write(text+'\n')
    print(text)

if __name__=='__main__': main()
