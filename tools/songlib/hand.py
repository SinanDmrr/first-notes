# Hand-transcribed melodies with lyrics (syllable per note; "_" = melisma / held note).
# Each tune: meter, lines (bars per display line), bars = [(chords_for_guitar, melody, lyrics)]
# Sources: traditional knowledge for children's songs; Mutopia Project (public domain
# typesetting) for Der Mond ist aufgegangen, Es ist ein Ros entsprungen, Schubert's
# Wiegenlied D498 and Heidenröslein D257, Brahms' Wiegenlied op.49/4, Good King
# Wenceslas, Old Hundredth.
H={}
def tune(k,meter,lines,bars,src=''): H[k]=dict(meter=meter,lines=lines,bars=bars,src=src)

# ---------------- ENGLISH ----------------
tune('mary','4/4',[4,4],[
 ('C','E4 D4 C4 D4','Ma-ry had a'),('C','E4 E4 E4:2','lit-tle lamb,'),('G7','D4 D4 D4:2','lit-tle lamb,'),('C','E4 G4 G4:2','lit-tle lamb,'),
 ('C','E4 D4 C4 D4','Ma-ry had a'),('C','E4 E4 E4 E4','lit-tle lamb, its'),('G7','D4 D4 E4 D4','fleece was white as'),('C','C4:4','snow.')])
tune('buns','4/4',[2,2],[
 ('C','E4 D4 C4:2','Hot cross buns!'),('C','E4 D4 C4:2','Hot cross buns!'),
 ('C','C4:1/2 C4:1/2 C4:1/2 C4:1/2 D4:1/2 D4:1/2 D4:1/2 D4:1/2','One a pen-ny, two a pen-ny,'),('G7 C','E4 D4 C4:2','hot cross buns!')])
tune('twinkle','4/4',[4,4,4],[
 ('C','C4 C4 G4 G4','Twin-kle, twin-kle,'),('Fmaj7 C','A4 A4 G4:2','lit-tle star,'),('Fmaj7 C','F4 F4 E4 E4','how I won-der'),('G7 C','D4 D4 C4:2','what you are!'),
 ('C Fmaj7','G4 G4 F4 F4','Up a-bove the'),('C G7','E4 E4 D4:2','world so high,'),('C Fmaj7','G4 G4 F4 F4','like a dia-mond'),('C G7','E4 E4 D4:2','in the sky.'),
 ('C','C4 C4 G4 G4','Twin-kle, twin-kle,'),('Fmaj7 C','A4 A4 G4:2','lit-tle star,'),('Fmaj7 C','F4 F4 E4 E4','how I won-der'),('G7 C','D4 D4 C4:2','what you are!')])
tune('london','4/4',[4,4],[
 ('C','G4:3/2 A4:1/2 G4 F4','Lon-don Bridge is'),('C','E4 F4 G4:2','fall-ing down,'),('G7','D4 E4 F4:2','fall-ing down,'),('C','E4 F4 G4:2','fall-ing down.'),
 ('C','G4:3/2 A4:1/2 G4 F4','Lon-don Bridge is'),('C','E4 F4 G4:2','fall-ing down,'),('G7','D4:2 G4:2','my fair'),('C','E4 C4:3','la-dy.')])
tune('jingle','4/4',[4,4,4,4],[
 ('C','E4 E4 E4:2','Jin-gle bells,'),('C','E4 E4 E4:2','jin-gle bells,'),('C','E4 G4 C4:3/2 D4:1/2','jin-gle all the'),('C','E4:4','way!'),
 ('Fmaj7','F4 F4 F4:3/2 F4:1/2','Oh, what fun it'),('C','F4 E4 E4 E4:1/2 E4:1/2','is to ride in a'),('D7','E4 D4 D4 E4','one-horse o-pen'),('G7','D4:2 G4:2','sleigh, hey!'),
 ('C','E4 E4 E4:2','Jin-gle bells,'),('C','E4 E4 E4:2','jin-gle bells,'),('C','E4 G4 C4:3/2 D4:1/2','jin-gle all the'),('C','E4:4','way!'),
 ('Fmaj7','F4 F4 F4:3/2 F4:1/2','Oh, what fun it'),('C','F4 E4 E4 E4:1/2 E4:1/2','is to ride in a'),('G7','G4 G4 F4 D4','one-horse o-pen'),('C','C4:4','sleigh!')])
tune('michael','4/4',[4,4],[
 ('C','C4 E4 G4:3/2 E4:1/2','Mi-chael, row the'),('C','G4 A4 G4:2','boat a-shore,'),('C','E4 G4 A4:2','Hal-le-lu-'),('G7','G4:4','-jah!'),
 ('C','E4 G4 G4:3/2 E4:1/2','Mi-chael, row the'),('Fmaj7 C','F4 E4 D4:2','boat a-shore,'),('C','C4 D4 E4:2','Hal-le-lu-'),('G7 C','D4:2 C4:2','-jah! _')])
tune('camptown','4/4',[4,4],[
 ('C','G4 G4 E4 G4','Camp-town la-dies'),('C','A4 G4 E4:2','sing this song,'),('G7','E4:2 D4:2','doo-dah!'),('C','E4:2 D4:2','doo-dah!'),
 ('C','G4 G4 E4 G4',"Camp-town race-track's"),('C','A4 G4 E4:2','five miles long,'),('G7','D4 D4 E4 D4','oh, de doo-dah'),('C','C4:4','day!')])
tune('susanna','4/4',[5,4],[
 ('','C4:1/2 D4:1/2','I come'),('C','E4 G4 G4:3/2 A4:1/2','from Al-a-ba-'),('C','G4 E4 C4:3/2 D4:1/2','-ma with a ban-'),('C','E4 E4 D4 C4','-jo on my knee,'),('G7','D4:3 C4:1/2 D4:1/2',"_ I'm go-"),
 ('C','E4 G4 G4:3/2 A4:1/2','-ing to Lou-i-'),('C','G4 E4 C4:3/2 D4:1/2','-si-an-a, my'),('C G7','E4 E4 D4 D4','true love for to'),('C','C4:4','see.')])
tune('bday','3/4',[5,4],[
 ('','G3:3/4 G3:1/4','Hap-py'),('C','A3 G3 C4','birth-day to'),('G7','B3:2 G3:3/4 G3:1/4','you, hap-py'),('G7','A3 G3 D4','birth-day to'),('C','C4:2 G3:3/4 G3:1/4','you, hap-py'),
 ('C','G4 E4 C4','birth-day, dear'),('Fmaj7','B3 A3 F4:3/4 F4:1/4','friend, _ hap-py'),('C G7','E4 C4 D4','birth-day to'),('C','C4:3','you!')])
tune('yankee','4/4',[2,2],[
 ('C','C4:1/2 C4:1/2 D4:1/2 E4:1/2 C4:1/2 E4:1/2 D4:1/2 G3:1/2','Yan-kee Doo-dle went to town a-'),('C G7','C4:1/2 C4:1/2 D4:1/2 E4:1/2 C4 B3','-rid-ing on a po-ny,'),
 ('C Fmaj7','C4:1/2 C4:1/2 D4:1/2 E4:1/2 F4:1/2 E4:1/2 D4:1/2 C4:1/2','stuck a fea-ther in his cap and'),('G7 C','B3:1/2 G3:1/2 A3:1/2 B3:1/2 C4 C4','called it ma-ca-ro-ni.')])
tune('clementine','3/4',[5,4],[
 ('','C4:1/2 C4:1/2','Oh my'),('C','C4:3/2 G3:1/2 E4:1/2 E4:1/2','dar-ling, oh my'),('C','E4:3/2 C4:1/2 C4:1/2 E4:1/2','dar-ling, oh my'),('G7','G4:3/2 G4:1/2 F4:1/2 E4:1/2','dar-ling, Cle-men-'),('G7','D4:2 D4:1/2 E4:1/2','-tine! You are'),
 ('G7','F4:3/2 F4:1/2 E4:1/2 D4:1/2','lost and gone for-'),('C','E4:3/2 C4:1/2 C4:1/2 E4:1/2','-ev-er, dread-ful'),('G7','D4:3/2 G3:1/2 B3:1/2 D4:1/2','sor-ry, Cle-men-'),('C','C4:3','-tine.')])
tune('deck','4/4',[4,4,4],[
 ('C','G4:3/2 F4:1/2 E4 D4','Deck the halls with'),('C','C4 D4 E4 C4','boughs of hol-ly,'),('G7 C','D4:1/2 E4:1/2 F4:1/2 D4:1/2 E4:3/2 D4:1/2','fa la la la la, la'),('G7 C','C4 B3 C4:2','la la la!'),
 ('C','G4:3/2 F4:1/2 E4 D4',"'Tis the sea-son"),('C','C4 D4 E4 C4','to be jol-ly,'),('G7 C','D4:1/2 E4:1/2 F4:1/2 D4:1/2 E4:3/2 D4:1/2','fa la la la la, la'),('G7 C','C4 B3 C4:2','la la la!'),
 ('C','G4:3/2 F4:1/2 E4 D4','Troll the an-cient'),('C','C4 D4 E4 C4','Yule-tide car-ol,'),('G7 C','D4:1/2 E4:1/2 F4:1/2 D4:1/2 E4:3/2 D4:1/2','fa la la la la, la'),('G7 C','C4 B3 C4:2','la la la!')])
tune('largo','4/4',[4,4],[
 ('C','E4:3/2 G4:1/2 G4:2',"Go-in' home,"),('C','E4:3/2 D4:1/2 C4:2',"go-in' home,"),('G7','D4 E4 G4 E4',"I'm a-go-in'"),('G7','D4:4','home;'),
 ('C','E4:3/2 G4:1/2 G4:2','qui-et-like,'),('C','E4:3/2 D4:1/2 C4:2','some still day,'),('G7','D4 E4 D4:3/2 C4:1/2',"I'm jes' go-in'"),('C','C4:4','home.')])
tune('saints','4/4',[4,4,4,3],[
 ('C','R C4 E4 F4','Oh, when the'),('C','G4:4','saints'),('C','R C4 E4 F4','go march-ing'),('G7','G4:4','in,'),
 ('C','R C4 E4 F4','oh, when the'),('C','G4:2 E4:2','saints go'),('C','C4:2 E4:2','march-ing'),('G7','D4:4','in,'),
 ('C','R E4 E4 D4','oh, Lord, I'),('C','C4:3 C4','want to'),('Fmaj7','E4:2 G4 G4','be in that'),('Fmaj7','F4:2 F4:2','num-ber,'),
 ('C','R E4 F4 G4','when the saints'),('C G7','E4:2 C4:2','go march-'),('G7 C','D4:2 C4:2','-ing in!')])
tune('grace','3/4',[4,4,4,4],[
 ('','R:2 G3','A-'),('C','C4:2 E4:1/2 C4:1/2','-maz-ing _'),('C','E4:2 D4','grace, how'),('Fmaj7','C4:2 A3','sweet the'),
 ('C','G3:2 G3','sound that'),('C','C4:2 E4:1/2 C4:1/2','saved a _'),('C','E4:2 D4','wretch like'),('G7','G4:3','me!'),
 ('G7','G4:2 E4','_ I'),('C','G4:2 E4:1/2 G4:1/2','once was _'),('C','E4:2 C4','lost, but'),('Fmaj7','G3:2 A3','now am'),
 ('C','C4:2 C4','found, was'),('Am','A3:2 G3','blind, but'),('C G7','C4:2 E4:1/2 C4:1/2','now I _'),('C','E4:2 D4 C4:3','see. _ _')])
tune('auld','4/4',[5,4],[
 ('','G3','Should'),('C','C4:3/2 C4:1/2 C4 E4','auld ac-quaint-ance'),('G7','D4:3/2 C4:1/2 D4 E4','be for-got, and'),('C','C4:3/2 C4:1/2 E4 G4','nev-er brought to'),('Fmaj7','A4:3 A4','mind? Should'),
 ('C','G4:3/2 E4:1/2 E4 C4','auld ac-quaint-ance'),('G7','D4:3/2 C4:1/2 D4 E4','be for-got, and'),('Am Fmaj7','C4:3/2 A3:1/2 A3 G3','days of auld lang'),('C','C4:3 R','syne?')])
tune('sailor','4/4',[4,4,4,4],[
 ('Dm','A4 A4:1/2 A4:1/2 A4 A4:1/2 A4:1/2','What shall we do with a'),('Dm','A4 D4 F4 A4','drunk-en sai-lor,'),('C','G4 G4:1/2 G4:1/2 G4 G4:1/2 G4:1/2','what shall we do with a'),('C','G4 C4 E4 G4','drunk-en sai-lor,'),
 ('Dm','A4 A4:1/2 A4:1/2 A4 A4:1/2 A4:1/2','what shall we do with a'),('Dm','A4 B4 C5 D5','drunk-en sai-lor'),('C','C5 A4 G4 E4','ear-ly in the'),('Dm','D4:2 D4:2','mor-ning?'),
 ('Dm','A4:2 A4 A4','Way, hey, and'),('Dm','A4 D4 F4 A4','up she ri-ses,'),('C','G4:2 G4 G4','way, hey, and'),('C','G4 C4 E4 G4','up she ri-ses,'),
 ('Dm','A4:2 A4 A4','way, hey, and'),('Dm','A4 B4 C5 D5','up she ri-ses'),('C','C5 A4 G4 E4','ear-ly in the'),('Dm','D4:2 D4:2','mor-ning!')])
tune('row','6/8',[4,4],[
 ('G','G3:3 G3:3','Row, row,'),('G','G3:2 A3 B3:3','row your boat'),('G','B3:2 A3 B3:2 C4','gent-ly down the'),('G','D4:6','stream.'),
 ('G','G4 G4 G4 D4 D4 D4','Mer-ri-ly, mer-ri-ly,'),('G','B3 B3 B3 G3 G3 G3','mer-ri-ly, mer-ri-ly,'),('D7','D4:2 C4 B3:2 A3','life is but a'),('G','G3:6','dream.')])
tune('mac','4/4',[4,4],[
 ('C','C4 C4 C4 G3','Old Mac-Don-ald'),('Fmaj7 C','A3 A3 G3:2','had a farm,'),('G7','E4 E4 D4 D4','E-I-E-I-'),('C','C4:3 G3','O! And'),
 ('C','C4 C4 C4 G3','on his farm he'),('Fmaj7 C','A3 A3 G3:2','had a cow,'),('G7','E4 E4 D4 D4','E-I-E-I-'),('C','C4:4','O!')])
tune('wish','3/4',[5,4],[
 ('','D3','We'),('G','G3 G3:1/2 A3:1/2 G3:1/2 F#3:1/2','wish you a mer-ry'),('C','E3 E3 E3','Christ-mas, we'),('A7','A3 A3:1/2 B3:1/2 A3:1/2 G3:1/2','wish you a mer-ry'),('D7','F#3 D3 D3','Christ-mas, we'),
 ('Em','B3 B3:1/2 C4:1/2 B3:1/2 A3:1/2','wish you a mer-ry'),('C','G3 E3 D3:1/2 D3:1/2','Christ-mas and a'),('C D7','E3 A3 F#3','hap-py New'),('G','G3:3','Year!')])
tune('green','3/4',[5,4,4,3],[
 ('','A3','A-'),('Am','C4:2 D4','-las, my'),('C','E4:3/2 F4:1/2 E4','love, _ you'),('G','D4:2 B3','do me'),('Em','G3:3/2 A3:1/2 B3','wrong, _ to'),
 ('Am','C4:2 A3','cast me'),('E','A3:3/2 G#3:1/2 A3','off _ dis-'),('E','B3:2 G#3','-cour-teous-'),('Am','E3:2 A3','-ly. For'),
 ('Am','C4:2 D4','I have'),('C','E4:3/2 F4:1/2 E4','lov- _ -ed'),('G','D4:2 B3','you well'),('Em','G3:3/2 A3:1/2 B3','and long, de-'),
 ('Am','C4:3/2 B3:1/2 A3','-light-ing in'),('E','G#3:3/2 F#3:1/2 G#3','your com-pa-'),('Am','A3:3','-ny.')])
tune('silent','6/8',[4,4,4],[
 ('C','G4:3/2 A4:1/2 G4 E4:3','Si-lent night, _'),('C','G4:3/2 A4:1/2 G4 E4:3','ho-ly night, _'),('G7','D5:2 D5 B4:3','all is calm,'),('C','C5:2 C5 G4:3','all is bright,'),
 ('Fmaj7','A4:2 A4 C5:3/2 B4:1/2 A4','round yon Vir-gin Moth-'),('C','G4:3/2 A4:1/2 G4 E4:3','-er and Child, _'),('Fmaj7','A4:2 A4 C5:3/2 B4:1/2 A4','Ho-ly In-fant so'),('C','G4:3/2 A4:1/2 G4 E4:3','ten-der and mild,'),
 ('G7','D5:2 D5 F5:3/2 D5:1/2 B4','sleep in heav-en-ly'),('C','C5:3 E5:3','peace, _'),('C G7','C5 G4 E4 G4:3/2 F4:1/2 D4','sleep in heav-en _ -ly'),('C','C4:6','peace.')])
tune('wenceslas','4/4',[4,4,4,5],[
 ('A','A4 A4 A4 B4','Good King Wen-ces-'),('A E7','A4 A4 E4:2','-las looked out'),('D A','F#4 E4 F#4 G#4','on the Feast of'),('A','A4:2 A4:2','Ste-phen,'),
 ('A','A4 A4 A4 B4','when the snow lay'),('A E7','A4 A4 E4:2','round a-bout,'),('D A','F#4 E4 F#4 G#4','deep and crisp and'),('A','A4:2 A4:2','e-ven:'),
 ('A','E5 D5 C#5 B4','Bright-ly shone the'),('A E7','C#5 B4 A4:2','moon that night,'),('D A','F#4 E4 F#4 G#4','though the frost was'),('A','A4:2 A4:2','cru-el,'),
 ('A','E4 E4 F#4 G#4','when a poor man'),('A E7','A4 A4 B4:2','came in sight,'),('A','E5 D5 C#5 B4',"gath'-ring win-ter"),('A D','A4:2 D5:2','fu- _'),('A','A4:4','-el.')])
tune('old100','4/2',[4,4,4,4],[
 ('','G4:4','Praise'),('G D','G4:2 F#4:2 E4:2 D4:2','God, from whom all'),('G D','G4:4 A4:4','bless-ings'),('G','B4:4','flow;'),
 ('','B4:4','praise'),('G D','B4:2 B4:2 A4:2 G4:2','him, all crea-tures'),('C G','C5:4 B4:4','here be-'),('D','A4:4','-low;'),
 ('','G4:4','praise'),('D G','A4:2 B4:2 A4:2 G4:2','him a-bove, ye'),('C D','E4:4 F#4:4','heav’n-ly'),('G','G4:4','host;'),
 ('','D5:4','praise'),('G D','B4:2 G4:2 A4:2 C5:2','Fa-ther, Son, and'),('G D','B4:4 A4:4','Ho-ly'),('G','G4:4','Ghost.')])

# ---------------- DEUTSCH ----------------
tune('entchen','4/4',[4,2,4],[
 ('C','C4 D4 E4 F4','Al-le mei-ne'),('C','G4:2 G4:2','Ent-chen'),('Fmaj7','A4 A4 A4 A4','schwim-men auf dem'),('C','G4:4','See,'),
 ('Fmaj7','A4 A4 A4 A4','schwim-men auf dem'),('C','G4:4','See.'),
 ('G7','F4 F4 F4 F4','Köpf-chen in das'),('C','E4:2 E4:2','Was-ser,'),('G7','D4 D4 D4 D4','Schwänz-chen in die'),('C','C4:4','Höh’.')])
tune('haensel','4/4',[4,4,4,4],[
 ('C','G4 E4 E4:2','Häns-chen klein'),('G7','F4 D4 D4:2','ging al-lein'),('C','C4 D4 E4 F4','in die wei-te'),('C','G4 G4 G4:2','Welt hin-ein.'),
 ('C','G4 E4 E4:2','Stock und Hut'),('G7','F4 D4 D4:2','steht ihm gut,'),('C','C4 E4 G4 G4','ist gar wohl-ge-'),('C','C4:4','-mut.'),
 ('G7','D4 D4 D4 D4','A-ber Mut-ter'),('G7','D4 E4 F4:2','wei-net sehr,'),('C','E4 E4 E4 E4','hat ja nun kein'),('C','E4 F4 G4:2','Häns-chen mehr.'),
 ('C','G4 E4 E4:2','Da be-sinnt'),('G7','F4 D4 D4:2','sich das Kind,'),('C','C4 E4 G4 G4','kehrt nach Haus ge-'),('C','C4:4','-schwind.')])
tune('jakob','4/4',[4,4],[
 ('C','C4 D4 E4 C4','Bru-der Ja-kob,'),('C','C4 D4 E4 C4','Bru-der Ja-kob,'),('C','E4 F4 G4:2','schläfst du noch?'),('C','E4 F4 G4:2','Schläfst du noch?'),
 ('C','G4:1/2 A4:1/2 G4:1/2 F4:1/2 E4 C4','Hörst du nicht die Glo-cken?'),('C','G4:1/2 A4:1/2 G4:1/2 F4:1/2 E4 C4','Hörst du nicht die Glo-cken?'),('G7 C','C4 G3 C4:2','Ding, dang, dong!'),('G7 C','C4 G3 C4:2','Ding, dang, dong!')])
tune('geburtstag','3/4',[5,4],[
 ('','G3:3/4 G3:1/4','Zum Ge-'),('C','A3 G3 C4','-burts-tag viel'),('G7','B3:2 G3:3/4 G3:1/4','Glück, zum Ge-'),('G7','A3 G3 D4','-burts-tag viel'),('C','C4:2 G3:3/4 G3:1/4','Glück, zum Ge-'),
 ('C','G4 E4 C4','-burts-tag, lie-'),('Fmaj7','B3 A3 F4:3/4 F4:1/4','-ber Freund, zum Ge-'),('C G7','E4 C4 D4','-burts-tag viel'),('C','C4:3','Glück!')])
tune('ode','4/4',[4,4,4,4],[
 ('C','E4 E4 F4 G4','Freu-de, schö-ner'),('G7','G4 F4 E4 D4','Göt-ter-fun-ken,'),('C','C4 C4 D4 E4','Toch-ter aus E-'),('G7','E4:3/2 D4:1/2 D4:2','-ly-si-um!'),
 ('C','E4 E4 F4 G4','Wir be-tre-ten'),('G7','G4 F4 E4 D4','feu-er-trun-ken,'),('C','C4 C4 D4 E4','Himm-li-sche, dein'),('G7 C','D4:3/2 C4:1/2 C4:2','Hei-lig-tum!'),
 ('G7','D4 D4 E4 C4','Dei-ne Zau-ber'),('G7 C','D4 E4:1/2 F4:1/2 E4 C4','bin-den _ wie-der,'),('G7 C','D4 E4:1/2 F4:1/2 E4 D4','was die _ Mo-de'),('C G7','C4 D4 G3:2','streng ge-teilt;'),
 ('C','E4 E4 F4 G4','al-le Men-schen'),('G7','G4 F4 E4 D4','wer-den Brü-der,'),('C','C4 C4 D4 E4','wo dein sanf-ter'),('G7 C','D4:3/2 C4:1/2 C4:2','Flü-gel weilt.')])
tune('stille','6/8',[4,4,4],[
 ('C','G4:3/2 A4:1/2 G4 E4:3','Stil-le Nacht, _'),('C','G4:3/2 A4:1/2 G4 E4:3','hei-li-ge Nacht!'),('G7','D5:2 D5 B4:3','Al-les schläft,'),('C','C5:2 C5 G4:3','ein-sam wacht'),
 ('Fmaj7','A4:2 A4 C5:3/2 B4:1/2 A4','nur das trau-te hoch-'),('C','G4:3/2 A4:1/2 G4 E4:3','-hei-li-ge Paar.'),('Fmaj7','A4:2 A4 C5:3/2 B4:1/2 A4','Hol-der Kna-be im'),('C','G4:3/2 A4:1/2 G4 E4:3','lo-cki-gen Haar,'),
 ('G7','D5:2 D5 F5:3/2 D5:1/2 B4','schlaf in himm-li-scher'),('C','C5:3 E5:3','Ruh’! _'),('C G7','C5 G4 E4 G4:3/2 F4:1/2 D4','Schlaf in himm-li _ -scher'),('C','C4:6','Ruh’!')])
tune('morgenkommt','4/4',[4,4,4],[
 ('C','C4 C4 G4 G4','Mor-gen kommt der'),('Fmaj7 C','A4 A4 G4:2','Weih-nachts-mann,'),('Fmaj7 C','F4 F4 E4 E4','kommt mit sei-nen'),('G7 C','D4 D4 C4:2','Ga- _ -ben.'),
 ('C Fmaj7','G4 G4 F4 F4','Trom-mel, Pfei-fe'),('C G7','E4 E4 D4:2','und Ge-wehr,'),('C Fmaj7','G4 G4 F4 F4','Fahn und Sä-bel'),('C G7','E4 E4 D4:2','und noch mehr,'),
 ('C','C4 C4 G4 G4','ja ein gan-zes'),('Fmaj7 C','A4 A4 G4:2','Krie-ges-heer'),('Fmaj7 C','F4 F4 E4 E4',"möcht ich ger-ne"),('G7 C','D4 D4 C4:2','ha- _ -ben.')])
tune('brahms','3/4',[4,4,4,5],[
 ('','G4:1/2 G4:1/2','Gu-ten'),('Eb','Bb4:3/2 G4:1/2 G4','A-bend, gut’'),('Eb','Bb4 R G4:1/2 Bb4:1/2','Nacht, mit _'),('Ab','Eb5 D5:3/2 C5:1/2','Ro-sen be-'),
 ('Eb','C5 Bb4 F4:1/2 G4:1/2','-dacht, _ mit _'),('Bb7','Ab4 F4 F4:1/2 G4:1/2','Näg-lein be- _'),('Bb7','Ab4 R F4:1/2 Ab4:1/2','-steckt, schlupf _'),('Bb7','D5:1/2 C5:1/2 Bb4 D5','un- _ -ter die'),
 ('Eb','Eb5 R Eb4:1/2 Eb4:1/2','Deck’. Mor-gen'),('Ab','Eb5:2 C5:1/2 Ab4:1/2','früh, wenn Gott'),('Eb','Bb4:2 G4:1/2 Eb4:1/2','will, wirst du'),('Bb7','Ab4 Bb4 C5','wie-der ge-'),
 ('Eb','Bb4:2 Eb4:1/2 Eb4:1/2','weckt. Mor-gen'),('Ab','Eb5:2 C5:1/2 Ab4:1/2','früh, wenn Gott'),('Eb','Bb4:2 G4:1/2 Eb4:1/2','will, wirst du'),('Bb7','Ab4 G4 F4','wie-der ge-'),('Eb','Eb4:3','weckt.')],src='Mutopia')
tune('mond','4/4',[4,3,3,3],[
 ('','F4','Der'),('F C','G4 F4 Bb4 A4','Mond ist auf-ge-'),('C F','G4:2 F4 A4','-gan-gen, die'),('Dm A','A4 A4 D5 C5','gold-nen Stern-lein'),
 ('Bb F','Bb4:2 A4 A4','pran-gen am'),('F Bb','A4 A4 Bb4 A4','Him-mel hell und'),('C F','G4:3 F4','klar; der'),
 ('C F','G4 F4 Bb4 A4','Wald steht schwarz und'),('C F','G4:2 F4 A4','schwei-get, und'),('Dm A','A4 A4 D5 C5','aus den Wie-sen'),
 ('Bb F','Bb4:2 A4 A4','stei-get der'),('F Bb','A4 A4 Bb4 A4','wei-ße Ne-bel'),('C F','G4 G4 F4','wun-der-bar.')],src='Mutopia')
tune('ros','4/4',[5,4,2,5],[
 ('','C5:2','Es'),('F','C5 C5 D5 C5','ist ein Ros ent-'),('F Dm','C5:2 A4:2','-sprun-gen'),('Bb F','Bb4:2 A4 G4:2 F4:2 E4','aus ei-ner Wur-zel'),('F','F4:2 C5:2','zart, wie'),
 ('F','C5 C5 D5 C5','uns die Al-ten'),('F Dm','C5:2 A4:2','sun-gen,'),('Bb F','Bb4:2 A4 G4:2 F4:2 E4','von Jes-se kam die'),('F','F4:2 R A4','Art. Und'),
 ('C F','G4 E4 F4 D4','hat ein Blüm-lein'),('C','C4:2 R C5','bracht mit-'),('F','C5 C5 D5 C5','-ten im kal-ten'),('F Dm','C5:2 A4:2','Win-ter,'),('Bb F','Bb4:2 A4 G4:2','wohl zu der'),('C','F4:2 E4','hal-ben'),('F','F4:4','Nacht.')],src='Mutopia')
tune('schubertwiegen','4/4',[2,2,2,2],[
 ('Ab Eb7','C5 Eb5 Bb4:3/4 C5:1/4 Db5','Schla-fe, schla- _ -fe,'),('Ab Eb7','C5:1/2 C5:1/2 Bb4:1/4 Ab4:1/4 G4:1/4 Ab4:1/4 Bb4 Eb4','hol-der, sü- _ -ßer _ Kna-be,'),
 ('Ab Eb7','C5 Eb5 Bb4:3/4 C5:1/4 Db5','lei-se wiegt _ dich'),('Ab Eb7 Ab','C5:1/2 C5:1/2 Bb4:1/4 C5:1/4 Db5:1/4 Bb4:1/4 Ab4 R','dei-ner Mut- _ -ter _ Hand;'),
 ('Eb7 Ab','Bb4:3/2 Bb4:1/2 C5:3/4 Bb4:1/4 Ab4','sanf-te Ru- _ -he,'),('Ab Eb7','Eb5 Db5:1/2 C5:1/2 Bb4 Eb4','mil- _ -de La-be'),
 ('Ab Eb7','C5 Eb5 Bb4:3/4 C5:1/4 Db5','bringt dir schwe- _ -bend'),('Ab Eb7 Ab','C5:1/2 C5:1/2 Bb4:1/4 C5:1/4 Db5:1/4 Bb4:1/4 Ab4 R','die-ses Wie- _ -gen- _ band.')],src='Mutopia')
tune('heidenroeslein','2/4',[4,4,3,3],[
 ('G','B4:1/2 B4:1/2 B4:1/2 B4:1/2','Sah ein Knab ein'),('D7','D5:1/4 C5:1/4 C5:1/4 B4:1/4 A4','Rös- _ -lein _ stehn,'),('D7','A4:1/2 A4:1/2 B4:1/2 C5:1/2','Rös-lein auf der'),('G','D5 G5:1/2 R:1/2','Hei-den,'),
 ('G','B4:1/2 B4:1/2 B4:1/2 B4:1/2','war so jung und'),('A7','D5:1/4 C#5:1/4 C#5:1/4 B4:1/4 A4','mor- _ -gen- _ schön,'),('D','D5:1/2 D5:1/2 E5:3/4 D5:1/4','lief er schnell, es'),('A7 D','C#5:1/4 D5:1/4 E5:1/4 F#5:1/4 D5','nah _ zu _ sehn,'),
 ('D A7','D5:1/4 F#5:1/4 E5:1/4 D5:1/4 C#5:1/4 B4:1/4 A#4:1/4 B4:1/4',"sah's _ mit _ vie- _ -len _"),('A7 D','G5:3/4 C#5:1/4 D5','Freu- _ -den.'),('D7','A4:1/2 A4:1/2 B4:1/2 C5:1/2','Rös-lein, Rös-lein,'),
 ('G','D5:1/2 E5:1/4 F#5:1/4 G5','Rös-lein _ rot,'),('C G','E5:1/2 G5:1/2 C5:1/2 E5:1/2','Rös-lein auf der'),('D7 G','G4:1/2 B4:1/4 A4:1/4 G4','Hei- _ _ -den.')],src='Mutopia')
