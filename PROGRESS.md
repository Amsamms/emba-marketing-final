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

### Phase 8 progress to date (2026-05-15 — session 3)

**Ch.1b — ✅ COMPLETE** (rows 1–22, last commit `79dc10e`). All 37 slides visually audited and fixed. 22 findings total — key patterns: missing Process labels/anchors, paraphrased Ansoff definitions, invented budget component labels, missing Plan of Action phrasing, SWOT verbatim definitions absent.

**Ch.7 — ✅ COMPLETE** (rows 23–36, last commit `6c23be4`). All 33 slides visually confirmed this session. 14 findings total:
- §3.0 new: 4 verbatim STP definitions (s.3–4) + Figure 7.1 desc (s.5)
- §3.1 table: all 4 base defs now verbatim (s.8–12); removed invented "Climate, density" from Geographic def
- §3.3 B2B: "four" → "ten" variables with full s.14 verbatim list; "Purchasing factors" → "Purchasing Approaches"
- §3.4 International: "three" → "four" factors; added "Geographic location" as first factor (s.15)
- §3.5b new: Requirements for Effective Segmentation gets own sub-section with s.17 "To be useful..." framing
- §3.8 Targeting: Figure 7.2 desc (s.20); verbatim defs for all 4 strategies (s.21–24); Local/Individual marketing defs (s.25–26)
- §3.9: "Depends on:" verbatim intro + 5-factor list (s.27)
- §3.10: verbatim deck text quoted for vulnerable segments (s.28)
- §3.11: Product position def (s.29); Competitive advantage def (s.31); 3-step heading (s.30); bases renamed "X differentiation" per s.32; wrong citations s.41-43/s.50 → s.30/s.32/s.33 fixed

**Ch.10 — ✅ COMPLETE** (rows 37–45, last commit `9d584e5`). All 27 slides visually audited and fixed. 9 findings.

**Ch.11 — ✅ COMPLETE** (rows 46–54, last commit `7902ceb`). All 28 slides visually audited + Part-B invention grep run. 9 findings.

**Ch.14 — ✅ COMPLETE** (rows 55–66, last commit `3225604`). All 21 slides visually read fresh this session (Part A + Part B). 12 findings total — key patterns:
- Wrong deck filename in coverage note (`product_PPT_C14` → `place_PPT_C14.ppt`); missing 12.8 Retailer Marketing Decisions from section list.
- Slide-1 title page incorrectly cited as content.
- Supply/demand chain definitions replaced Claude paraphrase ("producer/customer in the centre") with Slide-5 verbatim.
- Value delivery network clause "not just their own profit" was Claude invention; replaced with Slide-6 verbatim.
- Administered VMS: silent "a few" → "one" quantifier change + invented "brand pull/volume" restored to slide verbatim.
- H/V conflict textbook definitions flagged as not-on-slide.
- Contractual VMS franchise sub-form examples (Ford/Coca-Cola/McDonald's) flagged as textbook-standard not on Slide 17.
- Channel-1/3 diagram examples flagged as not-on-slide.
- "Direct sales force" → "sales force" per Slide 21 label.
- F10 Whisper anchors: contact-reduction (Lec_6 @ 29:37), Almarai Saudi setting (59:11), brand-power (1:00:30), Diina Farms (1:06:10) all replaced with real timestamps + verbatim Arabic.

**🚨 NEW AUDIT RULE (confirmed by Ahmed 2026-05-15)**: Every chapter must begin with fresh visual read of ALL slide PNGs in that session — never rely on summaries or extracted text. See `memory/feedback_visual_slide_audit.md`.

**Ch.8 — ✅ COMPLETE** (rows 67–78). All 33 slides visually audited fresh. 12 findings — patterns: invented BlackBerry Actual/Augmented breakdown on Slide 4; invented industrial-product examples (Steel coils, machinery, lubricants) under [Slide 12]; missing Slide-17 umbrella "Product quality includes level and consistency" + "a" vs "the" targeted level; brand-equity citation [Slides 20, 25] lumping two slightly different wordings; "Packaging involves" prefix dropped on Slide 21; invented stretching definitions (Slide 23) and mix-dimension definitions (Slide 24); invented examples + silent "easy → easily" correction on Slide-27 desirable qualities; Slide-29 callout answer key invented (Camry/Prius/Scion); Slide-32 service-industry examples invented; Slide-33 Figure 8.5 callout truncated to first sentence; multiple NotebookLM citations replaced with real Whisper anchors (Hotel-shampoo Lec_4_1 @ 08:54-09:36; Abu Shaka Lec_4_B @ 1:50:50; Netflix Lec_4_2 @ 10:33; Defacto Lec_4_2 @ 13:36; MBA Business-Language flagged as NotebookLM-only paraphrase with no verbatim Whisper hit).

**Remaining chapters not yet swept**: Ch.1a — ⏳ pending.

## Next Step
**Ch.1a Marketing Orientations** — next session. ~12 slides (Basic Concepts s.1 + Kotler Ch.1 s.1–12). Read ALL slide PNGs visually before making any fixes.

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

### 🚨 CRITICAL — top priority for next session (locked by Ahmed 2026-05-15)

**Full visual slide-by-slide audit of ALL 7 chapters: Ch.1a, Ch.1b, Ch.7, Ch.8, Ch.10, Ch.11, Ch.14.** Ahmed's 2026-05-15 partial review of Ch.1b's mission/business-goals area surfaced 5 violations in just one sub-section (rows #1–5 in CHAPTER_REVIEW) — including the canonical example added 2026-05-15 evening: deck slide 7 lists "**Processes in Strategic Marketing Management**" with 5 gerund-form items, Process 4 = "**Budgeting marketing, financial, and production resources**", but the portal had compressed it to imperative paraphrases and dropped the 3 resource categories. That kind of finding — Part-A (heading/list deviation from deck wording) + Part-B (silently-dropped key terms like the Production/Financial/Marketing trio) — is exactly what the systematic audit must catch on every slide.

**⚠️ WORKFLOW — chapter by chapter, not all 7 at once** (locked by Ahmed 2026-05-15): Do ONE chapter per session. Within that chapter, audit every slide of every relevant deck, log findings as rows in CHAPTER_REVIEW.md, propose fixes, get Ahmed's sign-off per finding, apply, commit + push, mark 🟢. Only when that chapter is fully closed (all rows 🟢 or ⚪) do we move to the next chapter. Do NOT batch multiple chapters into a single audit pass — Ahmed wants to review and approve findings chapter-at-a-time before scope expands.

**Two-part audit per chapter — both parts mandatory for every slide of every deck:**

**Part A — Emphasis-match audit (visual):**
- Open each slide PNG in `portal/extracted/ch{NN}/slide-NN.png` (Ch.7 PNGs live in midterm-portal extracted dir; Ch.8/10/11/14 are in this portal's `extracted/`).
- For each slide measure visually: what does the slide emphasise (a single headline concept, a numbered list, a 2×2 grid, a labelled diagram, a bold/coloured term)?
- Compare against the **live portal page** for that chapter: is the same concept given equivalent weight (dedicated heading + framed block) or is it compressed to inline parenthetical / dropped entirely?
- Flag mismatches: "Slide N emphasises X (full-slide / bold / numbered) — portal mentions X inline only" or "Slide N gives 30% of pixel area to X — portal has no anchor for X."
- This is the same pattern that caught the **Business Goals umbrella** (Ch.1b row #2): deck dedicated 2 slides → portal had 1 inline parenthetical. Visual measurement is the only way to catch this — text-only LLM mining doesn't see slide layout / emphasis.

**Part B — Source-strict claude-invention audit:**
- For every category label, umbrella term, and definition in the portal's coverage of that chapter, verify it exists in the deck text (`extracted/{NN}.txt`) OR in lecture transcripts (`transcripts/Lec_{N}.md`).
- Use the **double-grep technique** that caught "environmental forces": `grep -i "<term>" extracted/*.txt transcripts/*.md` — zero hits means I invented it.
- Flag every invented term, even if pedagogically convenient. Per the source-strict feedback memory: Dr. Alaa recycles deck wording near-verbatim, so a Claude-invented label can be the exact word that costs Ahmed points.
- Known invention patterns to watch for: collective umbrella nouns ("the 8 X forces" / "the 5 X strategies" / "the 3 X levers"), category labels in tables, performance-type framings ("firm performance vs market performance"), "Typical measures" / "Typical examples" columns enriched beyond the slide.

**Output**: For each chapter, populate CHAPTER_REVIEW.md with one row per finding. Both audits feed the same row table (use the "Slide / location" column to identify Part-A vs Part-B findings — Part A = "Slide N (visual emphasis)", Part B = "Invented label: '<term>'").

**Chapters in priority order — one per session** (worst-risk first; Ch.8/10/11/14 were built from scratch in this project so they have highest invention risk; Ch.1a/1b/7 carried over from the midterm portal but the 2026-05-15 partial review of Ch.1b alone surfaced 5 violations, so carried-over chapters are NOT safe to skip):

1. **Session N+1 = Ch.8 Product** — 33 slides (largest deck, biggest invention risk)
2. **Session N+2 = Ch.10 Pricing** — 27 slides
3. **Session N+3 = Ch.11 Promotion** — 28 slides
4. **Session N+4 = Ch.14 Place** — 21 slides
5. **Session N+5 = Ch.1b Strategic Marketing Mgmt remainder** — Strategic Pilot s.5–37 minus what's already done (s.7 5-processes, s.8–14 mission/business-goals span are 🟢). Remainder = s.15–22 SWOT / Distinctive Competency / Success Requirements / Sources of env-opp deep-dive, s.23–32 Ansoff + 4Ps overview, s.33–34 Budgeting, s.35–37 Reformulation + Marketing Audit + drafting the marketing plan.
6. **Session N+6 = Ch.1a Marketing Orientations** — ~12 slides (Basic Concepts s.1 + Kotler Ch.1 s.1–12)
7. **Session N+7 = Ch.7 STP** — 22 slides (midterm-vetted but still audit)

**Each session's deliverable**: that one chapter's CHAPTER_REVIEW rows all marked 🟢 or ⚪, with commit hashes. Do not start session N+2 until session N+1's chapter is fully closed.

**Estimated workload**: ~178 slide visual reads (33+27+28+21+35+12+22) spread across **7 sessions** (one chapter per session). Each session ≈ 30–90 min depending on chapter size + finding density.

**Why this is critical**: this session found 5 source-strict violations in just the mission/business-goals area of Ch.1b alone (rows #1–5 in CHAPTER_REVIEW). The other 6 chapters likely contain similar-density issues. Pre-exam audit is the last line of defense before Ahmed sits the paper.

**Canonical example of what each chapter's audit should catch** (row #5, this session's evening discovery):
- **Part-A finding (visual emphasis)**: Deck slide 7 dedicates a whole slide to "**Processes in Strategic Marketing Management**" with 5 numbered gerund-form items, then slides 8 / 15 / 23 / 33 / 35 each give a dedicated "Process One / Two / Three / Four / Five" anchor slide. Portal had only a single inline "5 processes themselves" list with imperative paraphrases — losing both the deck's verbatim phrasing AND the per-process anchored emphasis.
- **Part-B finding (silently dropped terms)**: Deck Process 4 says "**Budgeting marketing, financial, and production resources**" — names 3 specific resource categories that mirror the Business Goals slide's Production/Financial/Marketing trio. Portal compressed to "Budget the resources" — those 3 critical category names dropped.
- **Fix pattern**: add a deck-verbatim list labelled `[Slide: Strategic Marketing Pilot s.7]` ABOVE the plain-language list. Both versions coexist, deck wording clearly marked as exam-safe. Per-process slide-citation badges (`[Slide s.8 — Process One]` etc.) restored.
- Each chapter audit should look for: (a) deck-section headings the portal renamed; (b) numbered/bulleted lists the portal compressed or re-ordered; (c) specific terms / category names / verb forms the portal silently changed.

### Remaining lower-priority steps

1. **Final-pass calibration check** — after all 7 chapters swept, regenerate citation counts and re-run a Q-bank coverage audit per chapter.

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
