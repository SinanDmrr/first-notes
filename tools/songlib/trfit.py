from tr_import import verse
from core import ptoken
NEY=set([55,57,58,59,60,61,62,64,65,67,69,70,71,72,73,74,76,77])
CLA=set([52,53,55,57,59,60,62,64,65,67,68,69,70,71,72,74,76])
SAZ=set([69,70,71,72,73,74,75,76,77,78,79,81])
SEL={'uskudara_gider':{},'canakkale_icinde':{'start_bar':40},'sari_gelin':{},'ankaranin_tasina':{},'bulbulum_altin':{},'havada_bulut':{},'dere_geliyor':{},'hey_onbesli':{},'entarisi_ala':{},'mektebin_bacalari':{},'gesi_baglarinda':{},'yuksek_yuksek':{},'kizilciklar_oldu':{},'cilveloy':{},'hekimoglu':{},'zeytinyagli_yiyemem':{},'drama_koprusu':{},'ceddin_deden':{},'cirpinirdi_karadeniz':{},'sigaramin_dumani':{},'bir_of_ceksem':{},'mevlam_bircok':{},'binnaz':{},'cemberim_de':{},'silifkenin_yogurdu':{},'yarim_istanbulu':{},'istanbuldan_uskudara':{},'kahve_yemenden':{},'dagda_tavsanlar':{},'tuna_nehri':{},'oklavayim':{},'seni_sevdim':{},'kalenin_burcu':{}}
if __name__=='__main__':
  for k,kw in SEL.items():
    v=verse(k,**kw); ms=sorted(set(p for b in v['bars'] for t in b['m'].split() for p in [ptoken(t)[0]] if p))
    f=lambda S,R:[t for t in R if all(m+t in S for m in ms)]
    nb=len(v['bars']); nn=sum(len(b['m'].split()) for b in v['bars'])
    print(f"{k:22s} {v['meter']:5s} bars{nb:3d} notes{nn:4d} rng{min(ms)}-{max(ms)} ney{f(NEY,range(-14,15))} kla{f(CLA,range(-24,13))} saz{f(SAZ,range(-14,15))}")
