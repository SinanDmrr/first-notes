import json, re
from fractions import Fraction as F
from core import ptoken, align_bar
from hand import H
from tr_import import verse
from kern2 import get as kget
from de_lyrics import DE as DEL

NAMES='C C# D Eb E F F# G G# A Bb B'.split()
def tok(m): return 'R' if m is None else NAMES[m%12]+str(m//12-1)
def fmt(d): d=F(d); return '' if d==1 else ':'+str(d)
def notes_of(m): return [ptoken(t) for t in m.split()]
def mstr(ns): return ' '.join(tok(p)+fmt(d) for p,d in ns)

GCH={'Em':(4,'m'),'Am':(9,'m'),'E':(4,''),'Dm':(2,'m'),'D':(2,''),'A':(9,''),'G':(7,''),'C':(0,''),'E7':(4,'7'),'A7':(9,'7'),'D7':(2,'7'),'G7':(7,'7'),'Fmaj7':(5,'maj7')}
def chord_pcs(name):
    r,q=GCH[name]
    iv={'':[0,4,7],'m':[0,3,7],'7':[0,4,7,10],'maj7':[0,4,7,11]}[q]
    return [(r+i)%12 for i in iv]
SETS={'minor':['Am','Dm','E7','G','C','Fmaj7'],'major_C':['C','Fmaj7','G7','Am','Dm','Em'],'major_G':['G','C','D7','Em','Am'],
      'hicaz':['A','Dm','G','C']}
TONIC={'minor':'Am','major_C':'C','major_G':'G','hicaz':'A'}
SETS['major_D']=['D','G','A7','Em']; TONIC['major_D']='D'

# ------------------------------------------------------------------ tunes
def tune_from_hand(k,ln):
    t=H[k]; bars=[]
    for c,m,w in t['bars']:
        l,ok=align_bar(m,w); assert ok,(k,m,w)
        bars.append(dict(c=c,ns=notes_of(m),l=l))
    return dict(meter=t['meter'],lines=t['lines'],bars=bars,chords=True)

def syl_list(txt):
    out=[]
    for w in txt.split():
        parts=w.split('-')
        for i,p in enumerate(parts): out.append(p+(' ' if i==len(parts)-1 else ''))
    return out
ERK_FIX={'erk061.krn':dict(mel=[(3,3),(6,1)],upto=8),'erk042.krn':dict(upto=8)}
def tune_from_erk(fn):
    meta,meter,key,bars=kget(fn)
    fix=ERK_FIX.get(fn,{})
    num,den=map(int,meter.split('/')); mul=2 if den==8 else 1
    bars=[b for b in bars]
    if 'upto' in fix: bars=bars[:fix['upto']+1]
    for bi,ni in fix.get('mel',[]): bars[bi][ni]['mel']=True
    txt=DEL[fn][1].replace('Ännchen','Änn-chen')
    if fn=='erk061.krn': txt="Ich weiß nicht, was soll es be-deu-ten, dass ich so trau-rig bin; ein Mär-chen aus ur-al-ten Zei-ten, das kommt mir nicht aus dem Sinn."
    if fn=='erk042.krn': pass
    S=syl_list(txt); k=0; out=[]
    for b in bars:
        if not b: continue
        ns=[];l=[]
        for n in b:
            ns.append((n['m'],n['d']*mul))
            slot=n['m'] and n['tie'] not in (']','_') and not n.get('mel')
            if slot:
                l.append(S[k] if k<len(S) else ''); k+=1
            else: l.append('')
        out.append(dict(c='',ns=ns,l=l))
    assert k==len(S),(fn,k,len(S))
    # drop trailing empty/rest-only bars
    while out and all(p is None for p,_ in out[-1]['ns']): out.pop()
    return dict(meter=f'{num}/{den}',lines=auto_lines(out),bars=out,chords=False)

def auto_lines(bars):
    L=[];cnt=0
    for i,b in enumerate(bars):
        cnt+=1
        end=any(s.strip() and s.strip()[-1] in '.,;!?:' for s in b['l'])
        if (end and cnt>=2) or cnt>=4: L.append(cnt); cnt=0
    if cnt: L.append(cnt)
    return L

def tune_from_symbtr(key,koma=False,**kw):
    v=verse(key,koma=koma,**kw)
    # make short verses longer (more lines) so every song has some substance
    ml=kw.get('max_lines',4)
    while len(v['bars'])<8 and ml<8:
        ml+=2; kw2=dict(kw); kw2['max_lines']=ml; v=verse(key,koma=koma,**kw2)
    bars=[dict(c='',ns=notes_of(b['m']),l=list(b['l'])) for b in v['bars']]
    # liaison marks: proper noun + short suffix -> apostrophe (Üsküdar'a), otherwise a normal word gap
    flat=[(bi,i) for bi,b in enumerate(bars) for i,s in enumerate(b['l']) if s]
    word=''
    for n,(bi,i) in enumerate(flat):
        s=bars[bi]['l'][i]
        if '‿' in s:
            pre,_,post=s.partition('‿')
            whole=word+pre
            # suffix = rest of this token + following tokens until word end
            suf=post.strip(); k=n
            while not bars[flat[k][0]]['l'][flat[k][1]].endswith(' ') and k+1<len(flat):
                k+=1; suf+=bars[flat[k][0]]['l'][flat[k][1]].strip()
            apo=whole[:1].isupper() and len(whole)>=5 and 0<len(suf)<=3 and suf[:1] in 'aeıioöuü'
            if apo: s=pre+'’'+post
            else: s=pre+' '+post if post.strip() else pre+' '
            bars[bi]['l'][i]=s
        word='' if bars[bi]['l'][i].endswith(' ') else word+bars[bi]['l'][i].split(' ')[-1]
    return dict(meter=v['meter'],lines=v['lines'],bars=bars,chords=False)

# ------------------------------------------------------------------ instruments
PLAY={'k':set([52,53,55,57,59,60,62,64,65,67,68,69,70,71,72,74,76]),
      'n':set([55,57,58,59,60,61,62,64,65,67,69,70,71,72,73,74,76,77]),
      's':set([69,70,71,72,73,74,75,76,77,78,79,81])}
CENTER={'k':65,'n':69,'s':75,'g':62}
def pitches(t): return [p for b in t['bars'] for p,_ in b['ns'] if p is not None]
def choose_tr(t,inst,prefer=None):
    ps=pitches(t); c=(min(ps)+max(ps))/2
    if inst=='g':
        return None
    cands=[x for x in range(-26,27) if all(p+x in PLAY[inst] for p in ps)]
    if inst=='s': cands=[x for x in cands if all(p+x!=70 for p in ps) or prefer==0]   # avoid the koma fret unless original Turkish tuning
    if not cands: return 'NOFIT'
    if prefer is not None and prefer in cands: return prefer
    tonic=[p for bb in t['bars'] for p,_ in bb['ns'] if p is not None][-1]
    PREF={'s':{9:0,2:0,4:1,7:1,0:1},'n':{7:0,9:0,0:1,2:1},'k':{0:0,9:0,5:1,2:1,7:1,4:1}}[inst]
    return min(cands,key=lambda x:(PREF.get((tonic+x)%12,3),abs(c+x-CENTER[inst])//6,abs(x)))

# ------------------------------------------------------------------ harmonizer (guitar)
def key_of(t):
    ps=[(p,d) for b in t['bars'] for p,d in b['ns'] if p is not None]
    tonic=ps[-1][0]%12
    dur={}
    for p,d in ps: dur[p%12]=dur.get(p%12,0)+d
    g=lambda i:dur.get((tonic+i)%12,0)
    if g(1)>0.3 and g(4)>g(3): return tonic,'hicaz'
    return tonic,('minor' if g(3)>=g(4) else 'major')
def harmonize(t,mode):
    S=SETS[mode]; ton=TONIC[mode]; prev=None; num=int(t['meter'].split('/')[0])
    nb=len(t['bars'])
    for bi,b in enumerate(t['bars']):
        ns=b['ns']; L=sum(d for _,d in ns)
        halves=2 if L>=3 and len(ns)>2 else 1
        seg=[[] for _ in range(halves)]; tt=F(0)
        for p,d in ns:
            # distribute duration over halves
            s0=tt; s1=tt+d
            for h in range(halves):
                a=L*h/halves; e=L*(h+1)/halves
                ov=max(F(0),min(s1,e)-max(s0,a))
                if ov>0 and p is not None: seg[h].append((p,ov))
            tt=s1
        ch=[]
        for h in range(halves):
            if not seg[h]: ch.append(prev or ton); continue
            best=None
            for c in S:
                pcs=chord_pcs(c); sc=0
                for p,d in seg[h]:
                    pc=p%12
                    if pc==pcs[0]: sc+=1.5*d
                    elif pc in pcs[1:3]: sc+=1.1*d
                    elif pc in pcs: sc+=0.5*d
                    else: sc-=1.0*d
                tot=sum(d for _,d in seg[h])
                if c==ton: sc+=0.35*tot
                if c==prev: sc+=0.25*tot
                if (bi==nb-1 and h==halves-1) or (bi==0 and h==0 and c==ton): sc+= 2*tot if c==ton else 0
                if best is None or sc>best[0]: best=(sc,c)
            ch.append(best[1]); prev=best[1]
        b['c']=' '.join(ch) if not (len(ch)==2 and ch[0]==ch[1]) else ch[0]

def guitar_prepare(t):
    """transpose to a guitar-friendly key and add chords if missing"""
    if t['chords'] and all(c in GCH for b in t['bars'] for c in b['c'].split()):
        ps=pitches(t); c=(min(ps)+max(ps))/2
        tr=min([-24,-12,0,12],key=lambda x:abs(c+x-62)); return tr
    tonic,mode=key_of(t)
    if mode in('minor','hicaz'): target=9
    else:
        # choose C, G or D by smallest shift
        target=min([0,7,2],key=lambda x:min((x-tonic)%12,(tonic-x)%12))
        mode={0:'major_C',7:'major_G',2:'major_D'}[target]
    sh=(target-tonic)%12
    if sh>6: sh-=12
    ps=pitches(t); c=(min(ps)+max(ps))/2+sh
    oc=min([-24,-12,0,12],key=lambda x:abs(c+x-62)); tr=sh+oc
    for b in t['bars']: b['ns']=[(None if p is None else p+tr,d) for p,d in b['ns']]
    harmonize(t,mode)
    return 0

# ------------------------------------------------------------------ difficulty
def difficulty(t):
    ns=[(p,d) for b in t['bars'] for p,d in b['ns'] if p is not None]
    num,den=t['meter'].split('/'); unit=F(4,int(den))  # beats -> quarters
    short=sum(1 for p,d in ns if d*unit<F(1,2))
    ps=[p for p,_ in ns]
    jumps=sum(1 for a,b in zip(ps,ps[1:]) if abs(a-b)>4)
    return len(ns)*0.6 + short*1.6 + (max(ps)-min(ps))*0.8 + jumps*1.2 + len(set(p%12 for p in ps))*1.5 + (6 if den=='8' and num not in('6','3') else 0)
