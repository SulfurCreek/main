import re, json, sys
src=open('final.md',encoding='utf-8').read()
GS='<span style="background-color: #fbf3db;">{}</span>'
BS='<strong><span style="background-color: #deebf1;">{}</span></strong>'
HEAD='<p><span class="ql-size-large" style="color: #00afb8;"><strong>{}</strong></span></p>'
def sec(t):
    m=re.search(r'^### '+re.escape(t)+r'\n(.*?)(?=^### |\Z)',src,re.S|re.M); return m.group(1)
def clean(t): return [l for l in t.splitlines() if l.strip() and not l.strip().startswith('<!--')]
def bold(text,terms):
    # bold first occurrence of each term outside tags
    for t in terms:
        parts=re.split(r'(<[^>]+>)',text); done=False; depth=0
        for k,p in enumerate(parts):
            if p.startswith('<'):
                if p.startswith('<strong'): depth+=1
                elif p.startswith('</strong'): depth-=1
                continue
            if not done and depth==0 and t in p:
                parts[k]=p.replace(t,f'<strong>{t}</strong>',1); done=True
        text=''.join(parts)
    return text
def deco(t,g=(),b=None,bt=()):
    for x in g:
        assert x in t,(x,t[:40]); t=t.replace(x,GS.format(x),1)
    if b:
        assert b in t,b; t=t.replace(b,BS.format(b),1)
    return bold(t,bt)
exp=sec('工作經歷')
heads=re.findall(r'^#### (.*)$',exp,re.M); parts=re.split(r'^#### .*$',exp,flags=re.M)[1:]
# per-experience: list of (pattern-in-line -> decoration)
D=[
 [('2026 Q3',dict(g=['約 6 萬家'],bt=['Product Owner','企業端招募系統'])),
  ('約 70 項',dict(g=['約 70 項主要功能已上線'],bt=['QA'])),
  ('新版求才系統',dict(g=['743 件已完成（88%）'],b='新版求才系統')),
  ('兩套功能重複',dict(g=['199 件'])),
  ('分店店長',dict(g=['55 件'],b='群組功能')),
  ('冒用',dict(g=['十多家'])),
  ('職缺工作說明生成',dict(b='AI 推薦人才',bt=['職缺工作說明生成','公司簡介生成'])),
  ('15 張',dict(g=['15 張'],b='類別代碼表',bt=['AI Agent'])),
  ('52%',dict(g=['由 52% 升至 79%']))],
 [('暢銷榜',dict(b='JustDating',bt=['Peach','KOOL'])),
  ('KOOL 是網紅',dict(bt=['KOOL'])),
  ('Instagram',dict(bt=['Instagram','Airbnb','Miro'])),
  ('1.6 萬',dict(g=['約 1.6 萬份','8 萬多次'])),
  ('VIP 訂閱',dict(b='KOOL',bt=['VIP 訂閱','點數付費牆','精選曝光'])),
  ('Juicy；',dict(g=['約 3,200 增至 1.25 萬','約 1,500 增至 1.2 萬'],b='Juicy',bt=['App Store','DAU'])),
  ('馬來西亞',dict(g=['增加 5%','減少 18%'],bt=['iOS 定價實驗'])),
  ('Peach',dict(g=['從 24% 升至 80% 以上'],bt=['Peach','App 內購','智冠'])) ],
 [('7 個市場。',dict(g=['7 個市場'],bt=['SweetRing'])),
  ('外籍實習生',dict(g=['約 10 位'])),
  ('CodaPay',dict(g=['2 國','8 種付款管道'],b='CodaPay',bt=['SweetRing Android 加值頁']))],
 []]
def exp_html(lines,rules):
    out=[]; ul=False; first=True
    def close():
        nonlocal ul
        if ul: out.append('</ul>'); ul=False
    for l in lines:
        child=l.startswith('    -'); t=re.sub(r'^\s*-\s+','',l).strip()
        if t.startswith('▍'):
            close(); out.append(HEAD.format(t[1:])); continue
        for key,kw in rules:
            if key in t: t=deco(t,**kw); break
        if first: out.append(f'<blockquote>{t}</blockquote>'); first=False; continue
        if child:
            out[-1]=out[-1][:-5]+f'<br>　　・{t}</li>'; continue
        if not ul: out.append('<ul>'); ul=True
        out.append(f'<li>{t}</li>')
    close(); return '\n'.join(out)
exps=[exp_html(clean(p),D[i]) if i<3 else '<p>'+re.sub(r'^\s*-\s+','',clean(p)[0])+'</p>' for i,p in enumerate(parts)]
skills=[re.sub(r'^\s*-\s+','',l) for l in clean(sec('專長'))]
BIO_B=['KOOL','Instagram','Airbnb','Miro','JustDating','Juicy','App Store','新版求才系統','群組功能','AI Agent','Antigravity','Claude Code']
bio=[bold(p,BIO_B) for p in clean(sec('自傳'))]
praw=sec('專案成就'); ph=re.findall(r'^#### (.*)$',praw,re.M); pp=re.split(r'^#### .*$',praw,flags=re.M)[1:]
PD=[dict(g=['約 3,200 增至 1.25 萬','約 1,500 回升至 1.2 萬'],bt=['JustDating','Juicy','App Store','CodaPay','DAU']),
    dict(g=[],bt=['KOOL','Instagram','Airbnb','Miro','VIP 訂閱','點數付費牆','精選曝光']),
    dict(g=[],bt=['新版求才系統','企業端招募系統']),
    dict(g=['2025/Q3'],bt=['群組功能'])]
def proj(lines,kw):
    body=lines[1:]; out=[]
    gold=list(kw['g']); bt=list(kw['bt'])
    for x in body:
        for g in list(gold):
            if g in x: x=x.replace(g,GS.format(g),1); gold.remove(g)
        out.append(x)
    assert not gold,gold
    html='<blockquote>'+bold(lines[0],bt)+'</blockquote>\n'+'\n'.join(f'<p>{bold(x,bt)}</p>' for x in out)
    return html
projs=[proj(clean(p),PD[i]) for i,p in enumerate(pp)]
job='\n'.join(clean(sec('求職條件（工作內容）')))
def d(o): return '<!-- @104-directive\n'+json.dumps(o,ensure_ascii=False)+'\n-->'
LF=["companyName","jobName","duration","workArea","management"]
ET=[["製作規格說明書","Prototype","Systems Analysis","專案溝通╱整合管理","生成式AI","推薦系統","工作任務╱業績項目分配","客訴案件處理"],
    ["市場調查企劃與執行","產品策略","產品營運","數據分析","專案時間╱進度控管","Electronic Payment","iOS","Android"],
    ["專案溝通╱整合管理","數據分析","Electronic Payment","Android"],[]]
ST=[["Claude","生成式AI","AI"],["製作規格說明書","Prototype","功能測試(function test)","專案規劃執行╱範圍管理"],["Systems Analysis","UML","系統整合分析"],
    ["Figma","Axure RP","Wireframe","Prototype","使用者介面設計","使用者體驗設計","iOS","Android"],["專案溝通╱整合管理","專案時間╱進度控管","Scrum","決策能力"],
    ["產品策略","產品營運","數據分析","Electronic Payment","iOS","Android"]]
MG=['**有管理責任，1~5 人**（直屬 2 名產品企劃）','**無管理責任**','**無管理責任**','**無管理責任**']
PDATE=['2020/01 – 2020/06｜isInProgress：否','2018/05 – 2022/03｜isInProgress：否','2024/12 – ｜isInProgress：**是**','2025/03 – 2025/09｜isInProgress：否（104 只收年月）']
o=['<!--markdownlint-disable MD013 MD033-->','','# 104 特化版｜v12.1（2026-10-24）｜**可填表**（verify_polish.py 41 區塊通過）','',
'> 來源：`causal_draft.md` r3.16 → Codex `final_resume.md`（`codex/resume-writer` 8c52b17）→ verify_polish 通過。',
'> 排版依 Antigravity 指南 v2.2.0：子項併入母項（`<br>　　・`）、模組大標、金黃＝成果數字、晴藍＋粗體＝核心產品／系統（每點最多 1 處）、粗體＝專案／系統／產品／buzzword（decisions §33）。**內文逐字取自定稿**，只加容器。',
'> 經歷底部不放「核心工具與技能」；標籤只用 `career/104/tool_categories.md`／`skill_categories.md` 清單內名稱，找不到就略過。','','---','',
'## 1. 個人簡介','',d({"target_block":"info","action":"replace_field","field":"bio","mode":"plain_text"}),'','```text','\n'.join(clean(sec('個人簡介'))),'```','',
'### 1.1 個人特色（五個分開輸入，依序；LOCKED）','',d({"target_block":"info","action":"replace_field","field":"trait","mode":"plain_text"}),'','```text','\n'.join(clean(sec('個人特色'))),'```','','---','','## 2. 工作經歷','']
for i,(h,html) in enumerate(zip(heads,exps)):
    o+=[f'### 2.{i+1} {h}','',f'▼ management：{MG[i]}','',d({"target_block":"experience","index":i,"action":"replace_description","mode":"quill_html","tags":ET[i],"locked_fields":LF}),'','```html',html,'```','']
o+=['---','','## 3. 專長（6 筆，順序與標題鎖定；desc 純文字）','']
for i,s in enumerate(skills):
    n,desc=s.split('：',1)
    o+=[f'### 3.{i+1} {n}','',d({"target_block":"skill","index":i,"action":"replace_all","mode":"plain_text","name":n,"tags":ST[i]}),'','```text',desc,'```','']
o+=['---','','## 4. 自傳','',d({"target_block":"bio","action":"replace_field","field":"chi","mode":"quill_html"}),'','```html','\n<p><br></p>\n'.join(f'<p>{p}</p>' for p in bio),'```','','---','','## 5. 專案成就','']
for i,(h,html) in enumerate(zip(ph,projs)):
    n=h.split('｜')[0]
    o+=[f'### 5.{i+1} {n}','',f'- 起訖：{PDATE[i]}｜url：留空','',d({"target_block":"project","index":i,"action":"replace_all","mode":"quill_html","name":n}),'','```html',html,'```','']
o+=['---','','## 6. 求職條件（工作內容，純文字；其餘求職條件欄位不動）','',d({"target_block":"jobCondition","action":"replace_field","field":"preferJobContent","mode":"plain_text","locked_fields":["preferJobTitle","salary","workArea","onboardDate","remoteWork"]}),'','```text',job,'```','']
out='\n'.join(o)+'\n'; open(sys.argv[1],'w',encoding='utf-8').write(out)
# zero mutation: every source text line must appear in output (tags stripped, ▍ stripped)
plain=re.sub(r'<[^>]+>','',''.join(re.findall(r'```(?:html|text)\n(.*?)```',out,re.S))).replace('\n','').replace('　　・','')
names=[s.split('：')[0] for s in skills]
bad=0
for line in re.sub(r'<!--.*?-->','',src).splitlines():
    t=re.sub(r'^\s*-\s+','',line).strip().lstrip('▍')
    if not t or t.startswith('#'): continue
    if '：' in t and t.split('：')[0] in names: t=t.split('：',1)[1]
    if t not in plain: print('MISMATCH',t[:60]); bad+=1
assert '<li></li>' not in out and 'ql-indent' not in out
print('checked',bad)
