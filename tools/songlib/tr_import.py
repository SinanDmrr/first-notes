import re
from symb import load,F
NAMES='C C# D Eb E F F# G G# A Bb B'.split()
def tok(m): return 'R' if m is None else NAMES[m%12]+str(m//12-1)
def fmt(d):
    d=F(d); return '' if d==1 else ':'+str(d)
def verse(key,max_lines=4,max_bars=18,start_bar=None,koma=False):
    name,usul,notes=load(key)
    num,den=usul[0],usul[1]; unit=F(den)          # beat unit = 1/den of whole
    barlen=F(num,den)
    # assign bar index by cumulative time
    t=F(0); rows=[]
    for n in notes:
        rows.append(dict(n,bar=int(t/barlen),t=t)); t+=n['d']
    def mark(s): x=s.strip(); return len(x)>=3 and x.isupper()
    def lyr(s): return s not in ('.','') and s.strip()!='' and not mark(s)
    first=next(i for i,r in enumerate(rows) if lyr(r['s']) and (start_bar is None or r['bar']>=start_bar))
    b0=rows[first]['bar']
    lines=0; end=None
    for i in range(first,len(rows)):
        s=rows[i]['s']
        if mark(s):
            # instrumental fill: continue if singing resumes within two bars
            nb=rows[i]['bar']
            if any(lyr(r['s']) for r in rows[i+1:] if r['bar']<=nb+2): continue
            end=i; break
        if lyr(s) and s.endswith('  '):
            lines+=1
            if lines>=max_lines: end=i+1; break
        if rows[i]['bar']-b0>=max_bars: end=i; break
    if end is None: end=len(rows)
    # extend to end of the bar of the last sung note (keep melody), but cut instrumental markers
    lastbar=rows[end-1]['bar']
    j=end
    while j<len(rows) and rows[j]['bar']==lastbar and not mark(rows[j]['s']): j+=1
    sel=[r for r in rows if r['bar']>=b0 and r['bar']<=lastbar][: (j - next(k for k,r in enumerate(rows) if r['bar']>=b0))]
    bars={}; lineends=set()
    for k,r in enumerate(sel):
        idx=rows.index(r)
        before_first= (idx<first) or (idx>=end)
        m=None if before_first else r['m']
        if koma and m is not None and re.match(r'^B\d+b[1-3]$',r['raw']): m-=1
        s=r['s']
        if before_first or not lyr(s): syl=''
        else:
            syl=s.rstrip(' ').replace('_','‿')
            if s.endswith(' '): syl+=' '
            if s.endswith('  '): lineends.add(r['bar'])
        bars.setdefault(r['bar'],[]).append((m,r['d']*den,syl))
    out=[]; L=[]; cnt=0
    for b in sorted(bars):
        ns=bars[b]
        # merge adjacent rests
        mm=[];ll=[]
        for m,d,s in ns:
            if m is None and mm and mm[-1][0] is None: mm[-1]=(None,mm[-1][1]+d)
            else: mm.append((m,d)); ll.append(s)
        out.append(dict(m=' '.join(tok(m)+fmt(d) for m,d in mm),l=ll))
        cnt+=1
        if b in lineends or cnt>=4: L.append(cnt); cnt=0
    if cnt: L.append(cnt)
    return dict(meter=f'{num}/{den}',lines=L,bars=out,usul=usul[2])
if __name__=='__main__':
    import sys
    v=verse(sys.argv[1]); print(v['meter'],v['usul'],v['lines'])
    for b in v['bars']: print(' ',b['m'],'|',''.join(b['l']))
