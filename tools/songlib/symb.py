import sys,glob,re,os
from fractions import Fraction as F
D='data/SymbTr/txt/'
PC={'C':0,'D':2,'E':4,'F':5,'G':7,'A':9,'B':11}
def midi(n):
    if n in ('Es',''): return None
    m=re.match(r'([A-G])(\d)([#b]\d+)?$',n)
    if not m: raise ValueError(n)
    v=(int(m[2])+1)*12+PC[m[1]]
    c=0
    if m[3]: k=int(m[3][1:])*22.64; c=k if m[3][0]=='#' else -k
    return v+round(c/100)
def load(pat):
    f=[x for x in glob.glob(D+'*') if pat in os.path.basename(x)]
    assert len(f)==1, (pat,f)
    rows=[l.rstrip('\n').split('\t') for l in open(f[0],encoding='utf-8')][1:]
    usul=None; notes=[]
    for r in rows:
        kod=r[1]
        if kod=='51': usul=(int(r[6]),int(r[7]),r[11]); continue
        if kod not in ('9','10','11','12'): continue
        d=F(int(r[6]),int(r[7]))
        if d==0: continue
        notes.append(dict(m=midi(r[3]),d=d,s=r[11],off=float(r[12]),raw=r[3]))
    return os.path.basename(f[0]),usul,notes
if __name__=='__main__':
    name,usul,notes=load(sys.argv[1]); print(name,usul,len(notes))
    t=F(0); bar=None
    for n in notes:
        b=int(float(t*F(usul[1],usul[0])) + 1e-9) if usul else 0
        if b!=bar: print(f'\n|{b:3d}|',end=' '); bar=b
        print(f"{n['raw']}:{n['d']}{'['+n['s']+']' if n['s'] not in ('.','') else ''}",end=' ')
        t+=n['d']
    print()
