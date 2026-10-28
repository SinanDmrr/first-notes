import re,sys
from fractions import Fraction as F
from kern import ptok,K
SL=[False]
def get(fn):
    SL[0]=False
    L=[l.rstrip('\n') for l in open(K+fn,encoding='utf-8')]
    meta={l[3:6]:l.split(':',1)[1].strip() for l in L if l.startswith('!!!') and ':' in l}
    labels=None; vox=None; txt=None; meter=None; key=None; bars=[[]]
    for l in L:
        if l.startswith('!') or not l.strip(): continue
        c=l.split('\t')
        if l.startswith('**'):
            labels=[str(i) for i in range(len(c))]; kinds=c; continue
        if l.startswith('*'):
            if vox is None and '*Ivox' in c: vox=labels[c.index('*Ivox')]
            for x in c:
                if re.match(r'^\*M\d+/\d+$',x) and meter is None: meter=x[2:]
                if re.match(r'^\*[A-Ga-g][#-]?:$',x) and key is None: key=x[1:-1]
            new=[];i=0
            while i<len(c):
                x=c[i]
                if x=='*^': new+= [labels[i]+'a',labels[i]+'b']; i+=1
                elif x=='*v':
                    j=i
                    while j<len(c) and c[j]=='*v': j+=1
                    new.append(labels[i][:-1] if labels[i][-1] in 'ab' and j-i>1 else labels[i]); i=j
                elif x=='*-': i+=1
                else: new.append(labels[i]); i+=1
            labels=new; continue
        if l.startswith('='): bars.append([]); continue
        if vox is None: continue
        idx=[k for k,lab in enumerate(labels) if lab==vox or lab.startswith(vox+'a') or lab==vox+'a']
        if not idx: idx=[k for k,lab in enumerate(labels) if lab.startswith(vox)]
        tok=c[idx[0]]
        # text spine: column right after vox whose kind is **text
        tx=None
        if txtcol(kinds,labels,vox) is not None:
            k=txtcol(kinds,labels,vox); tx=c[k] if k<len(c) else None
        if tok=='.' or tok.startswith('*'): continue
        n=ptok(tok)
        if n:
            n['mel']=SL[0] and not n['so']
            if n['so']: SL[0]=True
            if n['sc']: SL[0]=False
            n['t']= tx if tx not in (None,'.') else ''
            bars[-1].append(n)
    return meta,meter,key,bars
def txtcol(kinds,labels,vox):
    for k,lab in enumerate(labels):
        base=lab.rstrip('ab')
        if base.isdigit() and int(base)<len(kinds) and kinds[int(base)]=='**text': return k
    return None
if __name__=='__main__':
    for fn in sys.argv[1:]:
        meta,meter,key,bars=get(fn)
        ms=[n['m'] for b in bars for n in b if n['m']]
        print('==',fn,meta.get('OTL'),'|',meter,key,'bars',len(bars),'rng',min(ms),max(ms))
        for i,b in enumerate(bars):
            print(' ',i,' '.join(f"{n['m'] or 'r'}:{n['d']}{n['tie']}{'['+n['t']+']' if n['t'] else ''}" for n in b))
