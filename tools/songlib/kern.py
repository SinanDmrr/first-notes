import re,sys
from fractions import Fraction as F
K='data/erk/kern/'
PC={'c':0,'d':2,'e':4,'f':5,'g':7,'a':9,'b':11}
def ptok(tok):
    tok=tok.split(' ')[0]
    if 'q' in tok: return None
    m=re.search(r'(\d+)(\.*)',tok)
    if not m: return None
    base=int(m[1]); dots=len(m[2])
    d=F(4,base) if base else F(8)  # quarter units
    add=d
    for _ in range(dots): add/=2; d+=add
    if 'r' in tok: return dict(m=None,d=d,tie='',so=False,sc=False)
    p=re.search(r'([a-gA-G])\1*',tok); s=p.group(0); L=s[0]
    if L.islower(): o=4+len(s)-1
    else: o=3-(len(s)-1)
    acc=tok[p.end():]; a=acc.count('#')-acc.count('-')
    mid=(o+1)*12+PC[L.lower()]+a
    tie='[' if '[' in tok else (']' if ']' in tok else ('_' if '_' in tok else ''))
    return dict(m=mid,d=d,tie=tie,so='(' in tok,sc=')' in tok)
def load(fn):
    L=[l.rstrip('\n') for l in open(K+fn,encoding='utf-8')]
    meta={l[3:6]:l.split(':',1)[1].strip() for l in L if l.startswith('!!!') and ':' in l}
    vox=None; notes=[]; meter=None; key=None; bars=[[]]; texts=[]
    for l in L:
        if l.startswith('!'): continue
        c=l.split('\t')
        if l.startswith('**'): continue
        if vox is None:
            for i,t in enumerate(c):
                if t=='*Ivox': vox=i
            if vox is None: continue
        t=c[-1] if vox==len(c)-1 or True else c[vox]
        # find vox column: last kern col; text spines may follow
        if l.startswith('*'):
            for x in c:
                if re.match(r'^\*M\d+/\d+$',x) and meter is None: meter=x[2:]
                if re.match(r'^\*[A-Ga-g][#-]?:$',x) and key is None: key=x[1:-1]
            continue
        if l.startswith('='): bars.append([]); continue
        tok=c[VOXCOL[0]] if VOXCOL[0]<len(c) else c[-1]
        if tok=='.': continue
        n=ptok(tok)
        if n: bars[-1].append(n)
    return meta,meter,key,[b for b in bars]
VOXCOL=[0]
def find_vox(fn):
    L=[l.rstrip('\n') for l in open(K+fn,encoding='utf-8')]
    for l in L:
        if '*Ivox' in l:
            c=l.split('\t'); return c.index('*Ivox')
def get(fn):
    VOXCOL[0]=find_vox(fn); return load(fn)
if __name__=='__main__':
    for fn in sys.argv[1:]:
        meta,meter,key,bars=get(fn)
        ms=[n['m'] for b in bars for n in b if n['m']]
        print('==',fn,meta.get('OTL'),'|',meter,key,'bars',len(bars),'rng',min(ms),max(ms))
        for i,b in enumerate(bars[:6]):
            print(' ',i,' '.join(f"{n['m'] or 'r'}:{n['d']}{n['tie']}" for n in b))
