# Song library generator

Builds `SONGLIB` (the song list inside `index.html`) – 6 songs (2 easy, 2 medium, 2 hard)
per language × instrument, with one syllable per note.

```bash
cd tools/songlib
git clone --depth 1 https://github.com/MTG/SymbTr.git data/SymbTr              # Turkish songs (CC BY-NC-SA 4.0)
git clone --depth 1 https://github.com/craigsapp/erk-liederschatz.git data/erk # Erk, Deutscher Liederschatz
python3 make.py        # writes songlib3.js – paste it over `const SONGLIB=…` in index.html
```

- `hand.py` – hand-transcribed melodies + lyrics (EN/DE, some from the Mutopia Project). Lyrics use `-` between syllables and `_` for a held note.
- `de_lyrics.py` – German lyrics for the Erk melodies; a song is only used if notes and syllables match exactly.
- `tr_import.py` – first verse of a SymbTr türkü (notes, rhythm, syllables, line ends).
- `build.py` – transposition per instrument, simple automatic guitar chords, difficulty score.
- `make.py` – which song goes to which language/instrument, titles and source lines.
