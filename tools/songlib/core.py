import re
from fractions import Fraction as F
PCN={'C':0,'D':2,'E':4,'F':5,'G':7,'A':9,'B':11}
def ptoken(t):
    n,_,d=t.partition(':')
    b=F(d) if d else F(1)
    if n=='R': return None,b
    m=re.match(r'^([A-G])([#b]?)(\d)$',n)
    return (int(m[3])+1)*12+PCN[m[1]]+(1 if m[2]=='#' else -1 if m[2]=='b' else 0), b
def wtokens(w):
    """'Ma-ry had a' -> ['Ma','ry ','had ','a '] ; '-maz-ing' continues previous word; trailing '-' keeps word open; '_' = melisma"""
    out=[]
    for word in w.split():
        if word=='_': out.append('_'); continue
        cont_end=word.endswith('-') and len(word)>1
        parts=[p for p in word.strip('-').split('-')]
        for i,p in enumerate(parts):
            last=(i==len(parts)-1)
            out.append(p+('' if (not last or cont_end) else ' '))
    return out
def align_bar(m,w):
    notes=[ptoken(t) for t in m.split()]
    toks=wtokens(w) if w else []
    slots=[i for i,(p,_) in enumerate(notes) if p is not None]
    l=['']*len(notes)
    if not toks: return l,True
    if len(toks)!=len(slots): return l,False
    for i,t in zip(slots,toks): l[i]='' if t=='_' else t
    return l,True
