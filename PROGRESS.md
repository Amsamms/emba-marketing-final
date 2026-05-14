# Project: EMBA Marketing — Final-Exam Study Portal

## Goal
Build a unified single-file HTML study portal covering all 7 chapters (3 from midterm + 4 new) for Ahmed's Strategic Marketing **final exam** (Alexandria Univ EMBA, Dr. Alaa Elgharbawy). Ship to `https://amsamms.github.io/emba-marketing-final/`.

## Current Status
**Paused mid-session 2026-05-14 ~18:05 UTC** at user's request. Whisper still running in background. Resume from Phase 3 next session.

## Completed Work

### Phase 0 — Calibration (DONE)
- Visual-read both pages of actual midterm in `midterm_preparation/actual_exam/`
- Cross-referenced all 23 actual questions against midterm portal's predicted bank
- **Result: 100% topic coverage, 87% verbatim (20/23 hit word-for-word, 3 partial)**
- Full report: `study_notes/CALIBRATION.md`
- **Key insight for the final**: Dr. Alaa recycles Kotler/Kerin publisher test banks almost verbatim. Apply same recipe + heavy 4Ps weighting + adapted cases.

### Phase 1 — Whisper transcription (PARTIAL — two passes running in background)
- Script: `transcribe.py` (source A) + `transcribe_b.py` (source B wrapper, monkey-patches VOICES dir)
- venv: `portal/venv/` with `openai==2.36.0` installed

**Source A** — original recordings:
- 4 audio files in `Final preparation/Lecture voice of dr alaa/Lec.*.m4a` (Lec 4 split into part-1 + part-2 audio files of same lecture; Lec 5; Lec 6), 299.2 min total, est $1.79
- Status: Lec_4_1, Lec_4_2, Lec_5 saved; Lec_6 on chunk 3/9 at pause time
- PID 9023, log `whisper.log`

**Source B** — `Marketing.zip` (second recording of same 3 lectures, often longer/more complete):
- Unzipped to `Final preparation/Lecture voice of dr alaa/audio_src_b/`
- Lec 4's 3 tracks (Track-109/108/107) ffmpeg-concatenated chronologically into `Lec_4_B.m4a` (131 min)
- `Lec_5_B.m4a` = Track-110 (88 min), `Lec_6_B.m4a` = Track-111 (82 min)
- Total 301 min, est $1.81
- PID 19660 — wrapper that polls PID 9023, then runs `transcribe_b.py` after source A finishes
- Log `whisper_b.log` (won't have content until source A done)

**Combined est cost: ~$3.60** (still under $5 cap).

Resume check:
```bash
tail whisper.log whisper_b.log
ls transcripts/    # expect 6 files when both done: Lec_4_1, Lec_4_2, Lec_5, Lec_6, Lec_4_B, Lec_5_B, Lec_6_B
```

### Phase 2 — Slide extraction (DONE)
- 4 .ppt → .pptx (via `soffice --headless`) + per-slide PNG (via `pdftoppm`)
- Slide text extracted via `python-pptx` to `extracted/ch{08,10,11,14}.txt`
- **109 new slides total**:
  - Ch8 Product: 33 slides
  - Ch10 Pricing: 27 slides
  - Ch11 Promotion: 28 slides
  - Ch14 Place: 21 slides

## In-Progress Work
(none — Phases 0-6 complete; Phase 7 ships next)

## Final stats (after Phase 6)
- `index.html`: 4,778 lines, 254KB → 395KB
- **640 source citations** (394 Slide + 246 Lec)
- ~2,200 lines of teaching notes in `study_notes/`
- 95 predicted exam questions + 4 full mini-cases + mock 80-mark exam paper
- Mobile-responsive at 720/420px, dark-mode toggle, search filter, print-stylesheet
- Total Whisper cost: $3.60 of $5 cap

## Next Steps (in order)

### When resuming the session:
1. **Verify both Whisper passes finished** — `transcripts/` should have 7 files: Lec_4_1.md, Lec_4_2.md, Lec_5.md, Lec_6.md (source A) + Lec_4_B.md, Lec_5_B.md, Lec_6_B.md (source B). If incomplete, re-run the relevant script — both skip already-done lectures.
2. **Merge step (Phase 1c)** — write a small Python tool that interleaves source A + source B per lecture into `Lec_N_final.md`. Strategy: parse both `[mm:ss] text` blocks, sort by timestamp, drop near-duplicates (>80% Jaccard on consecutive entries). Source B will typically have ~40-50 extra min for Lec 4 since 3-track recorder caught more.

2. **Phase 3 — Concept mining + slide-by-slide audit** (`TaskList` shows #4)
   - For each of Ch8/10/11/14: LLM pass through `transcripts/Lec_{4_1,4_2,5,6}.md` extracting concepts + Arabic quotes + `[Lec N @ mm:ss]` anchors → write `study_notes/TEACHING_NOTES.md`
   - **Lecture-to-chapter mapping** (3 lectures cover 4 chapters; Lec_4_1 + Lec_4_2 = same Lec 4, just split audio):
     - Lec 4 (parts 1+2): probably Ch8 Product (largest deck) + maybe start of Ch10
     - Lec 5: probably Ch10 Pricing and/or Ch11 Promotion
     - Lec 6: probably Ch11 Promotion remainder + Ch14 Place
     - Verify by sampling first 5 minutes of each transcript (look for slide titles / "today we'll cover" cues).
   - Visual slide-by-slide audit using Opus 4.7's image reading — read `extracted/ch{NN}/slide-NN.png` and gap-fill `TEACHING_NOTES.md`
   - Mine exam signals into `study_notes/EXAM_SIGNAL.md` (look for "this is on the exam", "هذا مهم", "هذا هيجي", etc.)

3. **Phase 4 — Re-audit existing 3 chapters** (`TaskList` #5)
   - Pull §1–§11 content from `midterm_preparation/index.html` (lines 250–847)
   - Cross-check vs `CALIBRATION.md`; expand under-covered, mark over-covered

4. **Phase 5 — Portal scaffold** (`TaskList` #6)
   - Build `index.html` from `midterm_preparation/portal_template.html`
   - Top bar: Home / Chapters ▾ (dropdown of 7) / Exam / Cheat-sheet
   - URL hash routing (#ch8, #ch10, etc.)
   - Mobile responsive 720/420
   - **Chunked authoring** — placeholder markers + progressive Edits, NEVER mega-Write

5. **Phase 6 — Exam tab + adapted cases** (`TaskList` #7)
   - 6.1 Mock final mirroring template image (3 Qs)
   - 6.2 Broader Q bank (T/F 40, MCQ 30, short 15, mini-case 5, essay 10)
   - 6.3 Adapt Maersk → Ch11+Ch14, Starbucks → Ch8+Ch10, 2 originals
   - 6.4 21-row heat-map updated with calibration weights

6. **Phase 7 — Ship** (`TaskList` #8)
   - Citation grep ≥150 lec + ≥120 slide cites
   - `gh repo create amsamms/emba-marketing-final --public`
   - Push, enable Pages, verify live URL
   - Audio + transcripts + extracted slides gitignored

## Key Context

### Critical files
- **Plan**: `/home/amsamms/.claude/plans/the-midterm-actual-exam-kind-manatee.md`
- **Calibration brief**: `study_notes/CALIBRATION.md` (read this BEFORE any predicted exam authoring)
- **Source assets** (gitignored on publish):
  - Audio: `Final preparation/Lecture voice of dr alaa/Lec.*.m4a`
  - Slides: `Final preparation/chapters taken after midterm/*.ppt` + `portal/extracted/`
  - Style refs: `Final preparation/Exam template the the dr sai he will get.jpeg`, `Final preparation/International market exam/*.jpeg`
  - Cases: `Final preparation/Some case studies (from other sillubus )/*.docx`
  - Midterm feedback: `midterm_preparation/actual_exam/*.jpeg`
- **Reference (do not modify)**: `midterm_preparation/index.html`, `midterm_preparation/portal_template.html`, `midterm_preparation/transcribe.py`, `midterm_preparation/study_notes/*.md`

### Architecture notes
- Single-file HTML, inline CSS+JS, no deps (midterm pattern proven)
- Source-strict citations: every claim cites `[Slide N]` or `[Lec N @ mm:ss]`
- Mobile breakpoints at 720px and 420px

### Gotchas
- 4 new lecture audio files use `Dr._3alaa` naming (midterm used `Dr._3adel`) — `transcribe.py` handles via `normalize_tag()`
- `.ppt` (not `.pptx`) needs LibreOffice conversion first — already done
- Maersk case is short (247 words), Starbucks (401), Market-driven org (3,890 — theoretical, distill to study reference)
- Final-exam template image dictates 3-question shape; Dr. Alaa's writing pattern (per midterm) is test-bank-recycled definitions

### Cost so far
- Whisper estimated $1.79 (running)
- Nothing else

## Open Questions
- None — plan is approved end-to-end (see plan file).

## Tasks
Use `TaskList` to see status. Currently:
- #1 Phase 0 Calibration — completed
- #2 Phase 1 Whisper — in_progress (running in background)
- #3 Phase 2 Slide extraction — completed
- #4-#8 — pending
