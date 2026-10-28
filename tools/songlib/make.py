import json,sys
from build import *
from trfit import SEL

PD={'en':'public domain','de':'gemeinfrei','tr':'kamu malı'}
SYM='nota: TRT / SymbTr (CC BY-NC-SA 4.0)'
A=[
 # lang, inst, source, key, title, info
 ('en','g','h','row','Row, Row, Row Your Boat','Traditional, 19th century'),
 ('en','g','h','mac','Old MacDonald Had a Farm','Traditional, early 20th century'),
 ('en','g','h','susanna','Oh! Susanna','Stephen Foster, 1848'),
 ('en','g','h','deck','Deck the Halls','Welsh melody, 16th century; words 1862'),
 ('en','g','h','green','Greensleeves','English folk song, 16th century'),
 ('en','g','h','sailor','Drunken Sailor','Sea shanty, 19th century – a rock-band favourite'),
 ('en','k','h','twinkle','Twinkle, Twinkle, Little Star','Words Jane Taylor 1806, French melody'),
 ('en','k','h','yankee','Yankee Doodle','Traditional American, 18th century'),
 ('en','k','h','michael','Michael, Row the Boat Ashore','Traditional spiritual, 19th century'),
 ('en','k','h','bday','Happy Birthday to You','Mildred J. Hill & Patty Hill, 1893'),
 ('en','k','h','auld','Auld Lang Syne','Robert Burns 1788, Scottish melody'),
 ('en','k','h','wenceslas','Good King Wenceslas','Words J. M. Neale 1853, melody 1582 (Mutopia)'),
 ('en','s','h','london','London Bridge Is Falling Down','Traditional English'),
 ('en','s','h','buns','Hot Cross Buns','Traditional, 18th century'),
 ('en','s','h','camptown','Camptown Races','Stephen Foster, 1850'),
 ('en','s','h','wish','We Wish You a Merry Christmas','Traditional English carol'),
 ('en','s','h','grace','Amazing Grace','Words John Newton 1779, melody “New Britain” 1835'),
 ('en','s','h','saints','When the Saints Go Marching In','Traditional spiritual'),
 ('en','n','h','mary','Mary Had a Little Lamb','Sarah Josepha Hale, 1830'),
 ('en','n','h','largo','Goin’ Home','Dvořák, New World Symphony 1893; words W. A. Fisher 1922'),
 ('en','n','h','jingle','Jingle Bells','James Lord Pierpont, 1857 (chorus)'),
 ('en','n','h','clementine','Oh My Darling, Clementine','Traditional American, 1884'),
 ('en','n','h','silent','Silent Night','Franz X. Gruber 1818, English words J. F. Young 1859'),
 ('en','n','h','old100','Praise God, from Whom All Blessings Flow','“Old Hundredth”, Genevan Psalter 1551; words Thomas Ken 1674 (Mutopia)'),
 # ---------------- DE
 ('de','g','h','jakob','Bruder Jakob','Volkslied, Melodie 18. Jh.'),
 ('de','g','h','heidenroeslein','Heidenröslein','Franz Schubert 1815 (D 257), Text Goethe · Mutopia'),
 ('de','g','e','erk084.krn','O Tannenbaum','Volksweise, Text Ernst Anschütz 1824 · Melodie nach Erk, Deutscher Liederschatz'),
 ('de','g','e','erk199.krn','Wir hatten gebauet','Volksweise, Text August von Binzer 1819 · nach Erk'),
 ('de','g','e','erk061.krn','Die Loreley','Friedrich Silcher 1837, Text Heinrich Heine · erste Strophenhälfte'),
 ('de','g','e','erk017.krn','Ein Jäger aus Kurpfalz','Volkslied, 18. Jh. · nach Erk, Deutscher Liederschatz'),
 ('de','k','h','geburtstag','Zum Geburtstag viel Glück','Melodie Mildred J. & Patty Hill 1893, Text überliefert'),
 ('de','k','h','morgenkommt','Morgen kommt der Weihnachtsmann','Text Hoffmann von Fallersleben 1835, französische Melodie'),
 ('de','k','e','erkanh06.krn','Ihr Kinderlein, kommet','J. A. P. Schulz 1794, Text Christoph von Schmid'),
 ('de','k','e','erk030.krn','Du, du liegst mir im Herzen','Volkslied um 1820 · nach Erk, Deutscher Liederschatz'),
 ('de','k','e','erk003.krn','Ach, wie ist’s möglich dann','Friedrich Kücken 1827, Volkslied · nach Erk'),
 ('de','k','h','ros','Es ist ein Ros entsprungen','Melodie 1599, Satz Michael Praetorius 1609 · Mutopia'),
 ('de','s','h','haensel','Hänschen klein','Volkslied, Text Franz Wiedemann 1860'),
 ('de','s','h','mond','Der Mond ist aufgegangen','J. A. P. Schulz 1790, Text Matthias Claudius · Mutopia'),
 ('de','s','h','entchen','Alle meine Entchen','Volkslied, 19. Jh.'),
 ('de','s','e','erk004.krn','Ännchen von Tharau','Friedrich Silcher 1827, Text Simon Dach · nach Erk'),
 ('de','s','e','erk118.krn','Wenn ich ein Vöglein wär','Volkslied, Des Knaben Wunderhorn · nach Erk'),
 ('de','s','e','erk184.krn','Ich bin der Doktor Eisenbart','Volkslied, 18. Jh. · nach Erk, Deutscher Liederschatz'),
 ('de','n','h','ode','Ode an die Freude','Beethoven 1824, Text Friedrich Schiller'),
 ('de','n','h','brahms','Guten Abend, gut’ Nacht','Johannes Brahms 1868, Text Des Knaben Wunderhorn · Mutopia'),
 ('de','n','h','stille','Stille Nacht, heilige Nacht','Franz Xaver Gruber 1818, Text Joseph Mohr'),
 ('de','n','h','schubertwiegen','Schlafe, schlafe, holder süßer Knabe','Franz Schubert 1816 (D 498) · Mutopia'),
 ('de','n','e','erk089.krn','Schlaf, Herzenssöhnchen','Carl Maria von Weber 1810, Text Franz Carl Hiemer · nach Erk'),
 ('de','n','e','erk042.krn','Es war ein König in Thule','Carl Friedrich Zelter, Text Goethe · nach Erk'),
 # ---------------- TR
 ('tr','g','s','uskudara_gider','Üsküdar’a Gider İken','Anonim (İstanbul)'),
 ('tr','g','s','canakkale_icinde','Çanakkale İçinde','Anonim, 1915'),
 ('tr','g','s','havada_bulut','Yemen Türküsü (Havada Bulut Yok)','Anonim'),
 ('tr','g','s','hey_onbesli','Hey Onbeşli','Anonim (Tokat)'),
 ('tr','g','s','ceddin_deden','Ceddin Deden (Mehter Marşı)','Kaptanzade Ali Rıza Bey (1881–1934)'),
 ('tr','g','s','cirpinirdi_karadeniz','Çırpınırdı Karadeniz','Üzeyir Hacıbeyli (1885–1948), söz Ahmet Cevat (1892–1937)'),
 ('tr','k','s','hekimoglu','Hekimoğlu','Anonim'),
 ('tr','k','s','zeytinyagli_yiyemem','Zeytinyağlı Yiyemem','Anonim'),
 ('tr','k','s','drama_koprusu','Drama Köprüsü','Anonim (Rumeli)'),
 ('tr','k','s','binnaz','Binnaz','Anonim (Uşak)'),
 ('tr','k','s','cemberim_de','Çemberimde Gül Oya','Anonim (Biga)'),
 ('tr','k','s','istanbuldan_uskudara','İstanbul’dan Üsküdar’a','Anonim'),
 ('tr','s','s','dere_geliyor','Dere Geliyor Dere','Anonim'),
 ('tr','s','s','cilveloy','Cilveloy','Anonim (Artvin)'),
 ('tr','s','s','kizilciklar_oldu','Kızılcıklar Oldu mu','Anonim (Edirne)'),
 ('tr','s','s','ankaranin_tasina','Ankara’nın Taşına Bak','Anonim (Ankara)'),
 ('tr','s','s','sari_gelin','Sarı Gelin','Anonim (Erzurum)'),
 ('tr','s','s','bulbulum_altin','Bülbülüm Altın Kafeste','Anonim'),
 ('tr','n','s','entarisi_ala','Entarisi Ala Benziyor','Anonim (İstanbul)'),
 ('tr','n','s','bir_of_ceksem','Bir Of Çeksem','Anonim (Kayseri)'),
 ('tr','n','s','sigaramin_dumani','Sigaramın Dumanı','Anonim'),
 ('tr','n','s','mektebin_bacalari','Mektebin Bacaları','Anonim (Muş)'),
 ('tr','n','s','gesi_baglarinda','Gesi Bağları','Anonim (Kayseri)'),
 ('tr','n','s','yuksek_yuksek','Yüksek Yüksek Tepelere','Anonim'),
]
out=[]; report=[]
for ln,inst,src,key,title,info in A:
    if src=='h': t=tune_from_hand(key,ln)
    elif src=='e': t=tune_from_erk(key)
    else: t=tune_from_symbtr(key,koma=(inst=='s'),**SEL.get(key,{}))
    if inst=='g':
        tr=guitar_prepare(t)
    else:
        tr=choose_tr(t,inst,prefer=0 if (src=='s' and inst in 's') else None)
        if tr=='NOFIT':
            report.append(f'NOFIT {ln} {inst} {key}'); continue
        if inst!='g':
            for b in t['bars']: b['c']=''
    if src=='s': info=info+' · '+SYM
    info=info+' · '+PD[ln]
    out.append(dict(id=f'{ln}-{inst}-{key.replace(".krn","")}',ln=ln,**{'for':[inst]},title=title,meter=t['meter'],
        info=info,tr={inst:tr},lines=t['lines'],diff=difficulty(t),
        bars=[dict(c=b['c'],m=mstr(b['ns']),l=b['l']) for b in t['bars']]))
# levels: 2 easy / 2 medium / 2 hard per language × instrument, by difficulty
from collections import defaultdict
G=defaultdict(list)
for s in out: G[(s['ln'],s['for'][0])].append(s)
for k,lst in G.items():
    lst.sort(key=lambda s:s['diff'])
    for i,s in enumerate(lst): s['lvl']=['easy','easy','medium','medium','hard','hard'][i] if len(lst)==6 else ['easy','medium','hard'][min(2,i*3//len(lst))]
    report.append(f"{k}: "+' | '.join(f"{s['title']} ({s['lvl'][0]},{s['diff']:.0f},tr{s['tr'][s['for'][0]]})" for s in lst))
for s in out: del s['diff']
js="const SONGLIB="+json.dumps(out,ensure_ascii=False,separators=(',',':'))+".map(s=>{ const i=s.info; s.info=()=>i; return s; });\n"
open('songlib3.js','w',encoding='utf-8').write(js)
print('\n'.join(report)); print(len(out),'songs',len(js)//1024,'KB')
