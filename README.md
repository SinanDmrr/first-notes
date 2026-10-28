# First Notes

Free, open-source beginner lessons for **classical guitar**, the **saz** (kısa sap bağlama), the **Turkish G clarinet** (Sol klarnet, Boehm system) and the **Turkish ney**. One HTML file, no build step, no tracking, works on phones and desktops.

**▶ Use it now: https://sinandmrr.github.io/first-notes/**

Privacy: the page loads nothing from third parties (no external fonts, scripts, cookies or analytics). Progress is stored only in your own browser, and the microphone is analysed locally.

Languages: **English** (default), **Deutsch**, **Türkçe**. The chosen language is remembered in the browser.

## What's inside

Every instrument has the same structure, so nothing is left out:

- **Start here** – an 8-week learning path; weeks open and close like an accordion and the **step coach** sits inside the open week: each step has its own instructions, a diagram where useful, ← → arrows, a “done, next step” button and a shortcut that opens the matching tool with the right settings. Plus a 20-minute practice timer and a troubleshooter.
- **Instrument tools** – see below.
- **Read music** – notes on the staff, tap to see where to play them and to hear them; note values.
- **Tuner / Note finder** – guitar and saz get a tuner with their own reference tones per string/course; clarinet and ney, which aren't tuned note by note, get a note finder that names the note you play and shows how close it is (microphone, needs HTTPS hosting, e.g. GitHub Pages).
- **Songs** – a song library per language and instrument: every instrument gets 2 easy, 2 medium and 2 hard songs in English, German and Turkish (folk songs, classics like Für Elise, Bach, Mozart, Grieg's Mountain King, and rock-friendly pieces like Drunken Sailor and the Toccata). Each song only uses notes that instrument can play; chords for guitar, melody in learned notes for saz, clarinet and ney, with playback and highlighting. All lyrics are public domain; pieces without lyrics are instrumental.
- **My chord sheets (guitar)** – paste a song the way chord websites show it (chord line above the lyric line, or ChordPro `[Am]inline`). The page converts the capo on the sheet, suggests the easiest capo up to fret 7, transposes for your voice and shows each chord as a diagram. Sheets stay in your browser only; nothing is uploaded.
- **Tips** – technique basics.

### Guitar
Chords (how to read diagrams, 13 beginner chords, one-minute change drill) · Strumming (↓ ↑ patterns with playback) · Picking (p i m a, tabs) · Capo (calculator both ways) · reference tones for tuning.

### Saz (kısa sap bağlama, bağlama düzeni La – Re – Mi)
Frets (all 17 frets per octave on all three courses, koma frets marked, tap to hear) · Mızrap (down/up, folk rhythm, aksak 9/8, tremolo with playback) · Practice (5 levels on the alt course, incl. Si♭²) · Note chart · Songs · tuning reference tones for the three courses.

### Clarinet (G / Sol, written pitch)
Practice (5 levels, the page listens and checks the note) · Fingering chart · Songs (simple text notation with playback) · air challenge, tonguing, assembly and care, the Turkish sound.

### Ney (Mansur ney, Rast = G)
Practice (5 levels incl. low register and octave jumps) · Fingering chart for Rast, Dügah, Kürdi, Segah, Çargah, Nim Hicaz, Neva, Hüseyni and Acem in two registers · Songs with perde names · holding, embouchure, care, angle and makam. The tuner expects Segah and Kürdi slightly below the piano note.

## Run it

Open `index.html` in any modern browser. For the microphone features (tuner, note check) the page must be served over HTTPS, for example with GitHub Pages:

1. Push this repository to GitHub (public).
2. **Settings → Pages → Deploy from a branch → `main` / root → Save.**
3. Open `https://<user>.github.io/<repo>/`.

## Song notation (saz, clarinet and ney)

```
Do Re Mi Fa | Sol:2 Sol:2 | La La La La | Sol:4
```

- Solfège (`Do Re Mi…`) or letters (`C D E…`; in German mode `B` = B♭ and `H` = B).
- `:2` = 2 beats, `:1/2` = half a beat.
- `,` or `↓` after a note = low register, `'` or `↑` = high register.
- `P:2` = rest for 2 beats, `|` = bar line.
- Ney: perde names work too (`Rast Dügah Kürdi Segah Çargah Neva`), `Rast,` = low register.

## Contributing

Everything lives in `index.html`:

- Translations are inline: `X("English", "Deutsch", "Türkçe")`. To add a language, add it to `LANGS`, `NAMES` and `CHORD_ROOT`, then extend `X()` calls (missing entries fall back to English).
- Guitar data: `G.CH` (chords), `G.PATS` (strumming), `G.PPAT` (picking), `G.WEEKS`.
- Clarinet data: `K.N` (fingerings, written MIDI pitch), `K.LEVELS`, `K.WEEKS`, `K.SONGS`.
- Saz data: `S.RATIOS` (fret ratios), `S.COURSES`, `S.N`, `S.PATS` (mızrap), `S.WEEKS`, `S.SONGS`.
- Ney data: `N.N` / `NF` (fingerings), `N.LEVELS`, `N.WEEKS`, `N.SONGS`.
- Saz, clarinet and ney share one UI (`windUI(M)`); instrument text comes from hooks such as `M.care()`, `M.tips()`, `M.readLead()`.
- Sounds are synthesised in the browser (Web Audio): Karplus-Strong for nylon strings, a simple odd-harmonic tone for the clarinet.

Clarinet fingerings are for the Boehm system; ney fingerings follow the common Mansur chart (first register). Corrections from teachers and players are very welcome.

## Credits

Created by **Sinan** ([@SinanDmrr](https://github.com/SinanDmrr)) with the help of **Claude** (Anthropic).

## License

MIT – see `LICENSE`.
