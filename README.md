# First Notes

Free, open-source beginner lessons for **classical guitar** and the **Turkish G clarinet** (Sol klarnet, Boehm system). One HTML file, no build step, no tracking, works on phones and desktops.

Languages: **English** (default), **Deutsch**, **Türkçe**. The chosen language is remembered in the browser.

## What's inside

### Guitar
- **Start here** – an 8-week learning path with checkboxes, a 20-minute practice timer, how to sit, how to read a chord sheet, and a troubleshooter.
- **Chords** – how to read a chord diagram, 13 beginner chords with diagrams, step-by-step finger instructions and sound, plus a one-minute chord-change drill with a personal record.
- **Strumming** – patterns shown as ↓ ↑ on “1 and 2 and…”, played back with a chord progression and click.
- **Picking** – what p i m a means, six patterns shown as tabs and played back.
- **Capo** – what a capo does, a calculator (shape → sounding chord) and the reverse (which capo for a hard chord).
- **Notes** – first-position notes on the staff with string/fret and sound, plus note values.
- **Tuning** – reference tones per string and a microphone tuner.

### Clarinet (G / Sol, written pitch)
- **Start here** – 8-week path, practice timer, air challenge, tonguing, troubleshooter, assembly and care, the Turkish sound (vibrato, sliding, makam).
- **Practice** – five levels; the page shows the fingering and listens through the microphone to check the note.
- **Fingering chart**, **Read music** (staff with registers), **Songs** (simple text notation with playback), **Tuner**, **Embouchure tips**.

## Run it

Open `index.html` in any modern browser. For the microphone features (tuner, note check) the page must be served over HTTPS, for example with GitHub Pages:

1. Push this repository to GitHub (public).
2. **Settings → Pages → Deploy from a branch → `main` / root → Save.**
3. Open `https://<user>.github.io/<repo>/`.

## Song notation (clarinet)

```
Do Re Mi Fa | Sol:2 Sol:2 | La La La La | Sol:4
```

- Solfège (`Do Re Mi…`) or letters (`C D E…`; in German mode `B` = B♭ and `H` = B).
- `:2` = 2 beats, `:1/2` = half a beat.
- `,` or `↓` after a note = low register, `'` or `↑` = high register.
- `P:2` = rest for 2 beats, `|` = bar line.

## Contributing

Everything lives in `index.html`:

- Translations are inline: `X("English", "Deutsch", "Türkçe")`. To add a language, add it to `LANGS`, `NAMES` and `CHORD_ROOT`, then extend `X()` calls (missing entries fall back to English).
- Guitar data: `G.CH` (chords), `G.PATS` (strumming), `G.PPAT` (picking), `G.WEEKS`.
- Clarinet data: `K.N` (fingerings, written MIDI pitch), `K.LEVELS`, `K.WEEKS`, `K.SONGS`.
- Sounds are synthesised in the browser (Web Audio): Karplus-Strong for nylon strings, a simple odd-harmonic tone for the clarinet.

Fingerings are for the Boehm system. Corrections from teachers and players are very welcome.

## License

MIT – see `LICENSE`.
