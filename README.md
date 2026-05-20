# EMBA Marketing — Final-Exam Study Portal

A self-contained single-file HTML study portal covering all **7 chapters** of Ahmed's EMBA Strategic Marketing course at Alexandria University (Dr. Alaa Elgharbawy).

🌐 **Live**: https://amsamms.github.io/emba-marketing-final/

📚 **Companion site (midterm)**: https://amsamms.github.io/emba-marketing-midterm/

🧠 **Companion site (mind maps for phone revision)**: https://amsamms.github.io/emba-marketing-mindmaps/

## What's in the portal

- **Home** — coverage map, how to use, exam shape
- **Chapters** (dropdown) — 7 chapter tabs with full plain-English teaching notes:
  - Ch.1a — Marketing Orientations (Kotler Ch.1 first half)
  - Ch.1b — Strategic Marketing Management (Kerin Ch.1)
  - Ch.7 — Segmentation, Targeting, Positioning
  - Ch.8 — Product
  - Ch.10 — Pricing
  - Ch.11 — Promotion / IMC
  - Ch.14 — Place / Channels
- **Exam** — 95 predicted practice questions (40 T/F · 30 MCQ · 15 short-answer · 10 essay) + a template-faithful mock final exam (3 hours, 80 marks) + 4 adapted mini-cases (Cilantro/Starbucks · NileFreight/Maersk · Carrefour-vs-Almarai · NileFresh launch) + 21-row topic heat-map
- **Cheat-sheet** — one-screen reference for 4Ps · SWOT · Ansoff · STP · VMS · Pricing strategies · Promotion mix · Common confusions

## How it was built

This portal applies the same recipe that hit **23 of 23 actual midterm questions** in the companion midterm portal:

1. **Whisper transcription** of 3 post-midterm lectures (Lec 4 / 5 / 6) from two recording sources (original + Marketing.zip)
2. **Slide extraction** — 109 PNGs across the 4 new chapter decks
3. **Visual + LLM concept mining** — every slide visually audited; every concept tagged with Dr. Alaa's in-class examples and Arabic verbatim quotes
4. **Source-strict citations** — every claim cites `[Slide N]` or `[Lec N @ mm:ss]`
5. **Calibration** — predictions tuned against the actual midterm exam paper we sat
6. **Style matching** — exam predictions match Dr. Alaa's wording from his other-cohort International Marketing exam paper

## Stats

- ~4,800 lines of single-file HTML (inline CSS+JS, no external deps)
- 640+ source citations (394 slide + 246 lecture)
- ~2,200 lines of teaching notes across 7 chapters
- Mobile-responsive at 720px and 420px breakpoints
- Dark-mode toggle, print stylesheet, search filter

## Companion materials (gitignored — kept on Ahmed's local disk)

- 7 lecture transcripts (sources A and B) — `transcripts/`
- 109 slide PNGs + text extracts — `extracted/`
- Per-chapter teaching notes in Markdown — `study_notes/`
- Whisper pipeline scripts (`transcribe.py`, `transcribe_b.py`)
- Portal build script (`build_portal.py`)
- Calibration brief, exam-signal mining, full Q-bank, full cases — `study_notes/`

## Licence

Personal study material. No claim of authorship over the textbook content (Kotler, Kerin) or Dr. Alaa's lecture material. The teaching prose, exam predictions, and adapted cases are written by Ahmed (with AI assistance).
