# Project: EMBA Marketing — Final-Exam Study Portal

## Goal
Build a unified single-file HTML study portal covering all 7 chapters (3 from midterm + 4 new) for Ahmed's Strategic Marketing **final exam** (Alexandria Univ EMBA, Dr. Alaa Elgharbawy).

## ✅ SHIPPED 2026-05-14
- **Live**: https://amsamms.github.io/emba-marketing-final/
- **Repo**: https://github.com/Amsamms/emba-marketing-final
- **Companion (midterm)**: https://amsamms.github.io/emba-marketing-midterm/

## Current Status

**Phase 8 — chapter-by-chapter slide-vs-portal review** (opened 2026-05-14, ongoing).

Ahmed is reading each PowerPoint deck slide-by-slide and comparing it against the live portal. Findings are logged in `study_notes/CHAPTER_REVIEW.md` (the single source of truth for what's been reviewed, found, and fixed). Workflow per finding: Ahmed flags → I check source `.md` / `index.html` → propose patch → `Edit` → `git commit` → `git push` → GH Pages redeploys in ~30–60s → mark row 🟢 in CHAPTER_REVIEW with commit hash.

**Phases 0–7 all complete.** Portal is fully shipped: 7 chapters covered, 640 source citations, 95-Q practice bank, 4 mini-cases, mock 80-mark paper, heat-map, mobile-responsive, dark-mode, search, print stylesheet. Total Whisper cost: $3.60 (under $5 cap).

### Phase 8 progress to date (2026-05-15)

**Ch.1b — partial sweep (mission / business-goals area):** 3 findings, 3 fixed. See CHAPTER_REVIEW rows 1–3.
- Row 1 (clarification, no code change): "marketing goals" vs "why studying strategic marketing" — confirmed distinct concepts, both correctly covered on portal.
- Row 2 (commits `da8e2ed` → `5839f54` → `9cd0cfe`): Business Goals reframed from one inline parenthetical to dedicated `<h4>` block + 3-row table mirroring deck's s.13–14 two-slide emphasis. Source-strict: first attempt invented Production-Goals measures, caught by Ahmed and reverted to verbatim deck text only.
- Row 3 (commit `da8e2ed`): Fixed 4 citation pointers for "Sources of environmental opportunities" — was wrongly cited as `[Slide: Basic Concepts s.2]` (the 8 forces slide); corrected to `[Slide: Strategic Marketing Pilot s.16]`.

**Remaining chapters not yet swept**: Ch.1a · Ch.7 · Ch.8 · Ch.10 · Ch.11 · Ch.14 — all ⏳ pending Ahmed's read.

**Remainder of Ch.1b not yet swept**: SWOT / Distinctive Competency / Success Requirements / Ansoff / 4Ps overview / Budgeting / Marketing Audit.

## Completed Work (high level — phase-by-phase)

### Phase 0 — Calibration (DONE)
- Visual-read both pages of actual midterm in `midterm_preparation/actual_exam/`
- Cross-referenced all 23 actual midterm questions against midterm portal's predicted bank
- **Result: 100% topic coverage, 87% verbatim (20/23 hit word-for-word, 3 partial)**
- Full report: `study_notes/CALIBRATION.md`
- **Key insight for the final**: Dr. Alaa recycles Kotler/Kerin publisher test banks almost verbatim. Apply same recipe + heavy 4Ps weighting + adapted cases.

### Phase 1 — Whisper transcription (DONE)
- Script: `transcribe.py` (source A) + `transcribe_b.py` (source B wrapper)
- venv: `portal/venv/` with `openai==2.36.0`
- **Source A** (4 original recordings): Lec_4_1 + Lec_4_2 (same Lec 4, split audio), Lec_5, Lec_6. 299.2 min, ~$1.79.
- **Source B** (`Marketing.zip` re-recordings): Lec_4_B (131 min, 3-track ffmpeg concat), Lec_5_B (88 min), Lec_6_B (82 min). 301 min, ~$1.81.
- **Combined: $3.60 total** (well under $5 cap).
- Transcripts saved to `transcripts/Lec_*.md` with `[mm:ss]` timestamps.

### Phase 2 — Slide extraction (DONE)
- 4 `.ppt` → `.pptx` (via `soffice --headless`) + per-slide PNGs (via `pdftoppm`)
- Slide text extracted via `python-pptx` to `extracted/ch{08,10,11,14}.txt`
- **109 new slides total**: Ch.8 Product 33 · Ch.10 Pricing 27 · Ch.11 Promotion 28 · Ch.14 Place 21

### Phase 3 — Concept mining + slide-by-slide audit (DONE)
- LLM pass over `transcripts/Lec_{4_1,4_2,5,6}.md` → mined concepts, Arabic quotes, `[Lec N @ mm:ss]` anchors
- Lecture-to-chapter mapping confirmed: Lec 4 = Ch.8 + Ch.10 intro · Lec 5 = Ch.10 + Ch.11 · Lec 6 = Ch.11 + Ch.14
- Visual slide-by-slide audit using Opus 4.7 image reading of `extracted/ch{NN}/slide-NN.png`
- Exam signals mined to `study_notes/EXAM_SIGNAL.md`

### Phase 4 — Re-audit existing 3 chapters (DONE)
- Pulled §1–§11 from `midterm_preparation/index.html`
- Audited content captured in `study_notes/existing_3ch_audited.md` (Ch.1a / Ch.1b / Ch.7)

### Phase 5 — Portal scaffold (DONE)
- `index.html` built from `midterm_preparation/portal_template.html` via `build_portal.py`
- Top bar: Home / Chapters ▾ (7 dropdown) / Exam / Cheat-sheet
- URL hash routing (`#ch1a`, `#ch1b`, `#ch7`, `#ch8`, `#ch10`, `#ch11`, `#ch14`)
- Mobile responsive 720px / 420px, dark-mode toggle, search filter, print stylesheet

### Phase 6 — Exam tab + adapted cases (DONE)
- Mock 80-mark final mirroring template image
- Broader practice bank (T/F · MCQ · short · mini-case · essay)
- Adapted cases: Maersk → Ch.11+Ch.14 · Starbucks → Ch.8+Ch.10 · 2 originals (Vodafone churn, El-Cairo footwear)
- Heat-map updated with calibration weights

### Phase 7 — Ship (DONE 2026-05-14)
- Citation grep passed (640 total: 394 Slide + 246 Lec)
- `gh repo create amsamms/emba-marketing-final --public`
- Pushed, Pages enabled, live verified
- Audio + transcripts + raw extracted slides gitignored

### NotebookLM cross-check round (DONE — bonus pass)
- Cross-checked all 4 new chapters against an independent NotebookLM summary
- Filled 30+ gaps in chapter notes + EXAM_SIGNAL.md
- Commit `6aea309` carries this

## Final stats (as of 2026-05-15)
- `index.html`: ~5,800 lines (after Phase 8 patches; was 4,778 at ship time)
- **643 source citations** (394 Slide cites including the 4 newly corrected Pilot s.16 refs + 246 Lec + 3 new in business-goals block)
- ~2,200+ lines of teaching notes across `study_notes/`
- 95 predicted exam questions + 4 full mini-cases + mock 80-mark exam paper
- Mobile-responsive at 720/420px, dark-mode, search filter, print stylesheet
- Total Whisper cost: $3.60 of $5 cap

## Next Steps

1. **Continue Ch.1b sweep** — Ahmed reads remaining slides of Strategic Marketing Pilot deck (SWOT, Distinctive Competency, Success Requirements, Ansoff, 4Ps overview, Budgeting, Marketing Audit). Each finding logged in CHAPTER_REVIEW with row #4+.
2. **Sweep Ch.1a** — Kotler Ch.1 deck (Basic Concepts s.1 + Kotler slides 1–12): definitions, orientations, value, market offering.
3. **Sweep Ch.7** — Kotler Ch.7 deck (STP).
4. **Sweep Ch.8 / 10 / 11 / 14** — the 4 post-midterm chapters with the deepest content. These are where the most undiscovered gaps likely live since they were built from scratch in this project (whereas Ch.1a/1b/7 carried over from the midterm portal where Ahmed already vetted them).
5. **Final-pass calibration check** — after all 7 chapters swept, regenerate citation counts and re-run a Q-bank coverage audit per chapter.

## Key Context

### Critical files
- **Plan**: `/home/amsamms/.claude/plans/the-midterm-actual-exam-kind-manatee.md`
- **Live audit log**: `study_notes/CHAPTER_REVIEW.md` (THE source of truth for Phase 8 — read first when resuming)
- **Calibration brief**: `study_notes/CALIBRATION.md`
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

### Phase-8 workflow gotchas (added 2026-05-15)
- **Edit `index.html` directly** for content already in the live portal — `build_portal.py` is a one-shot scaffolder and re-running it would clobber the in-place edits. Only re-run `build_portal.py` if you're regenerating from scratch.
- **Source-strict rule applies to ALL Phase-8 patches** (per `feedback_source_strict` memory) — when adding a table or block, the verbatim deck wording must be quoted in the cell; do NOT invent measures, labels, or examples. If embellishment is wanted, mark it as "Exam tip" outside the table and don't pretend it's from the slide. (Caught in row #2 of CHAPTER_REVIEW — invented Production-Goals measures.)
- **Heading levels matter** — when adding a sub-section inside an existing §N.M block, use `<h4>` not `<h3>`. Adding `<h3>` creates a duplicate numbered peer in the nav (caught when first version had two `2.2` headings).
- **GH Pages deploy lag** — push triggers Pages build; first build is `queued`, may take 30–90s; sometimes a stale build fails (e.g., commit `da8e2ed` triggered a failed build that emailed Ahmed) but the next successful build supersedes it. Always verify via `gh run list --repo Amsamms/emba-marketing-final` and `curl -s https://amsamms.github.io/emba-marketing-final/ | grep <new-anchor-id>` before declaring done.
- **Citation audit pattern** — when fixing a citation, `grep -n "<wrong-cite>"` in `index.html` first to find ALL occurrences (concept body + exam-signal list + Q-bank q-source + Q-bank answer-cites footer). The Q-bank citations live in 2 places per question: the `<span class="q-source">` tag near the question, AND the `<p class="answer-cites">` block inside the reveal. Both must update.

### Gotchas carried over from earlier phases
- 4 new lecture audio files use `Dr._3alaa` naming (midterm used `Dr._3adel`) — `transcribe.py` handles via `normalize_tag()`
- `.ppt` (not `.pptx`) needs LibreOffice conversion first — already done
- Maersk case is short (247 words), Starbucks (401), Market-driven org (3,890 — theoretical, distill to study reference)
- Final-exam template image dictates 3-question shape; Dr. Alaa's writing pattern (per midterm) is test-bank-recycled definitions

### Cost so far
- Whisper: $3.60 total (Source A + Source B)
- No other paid-API costs

## Open Questions
- None — Phase 8 is open-ended (driven by Ahmed's reads). Each finding closes itself.

## Tasks
Phase tracking moved out of inline list — see `CHAPTER_REVIEW.md` for live row-by-row Phase-8 audit table. Phases 0–7 all completed pre-ship.
