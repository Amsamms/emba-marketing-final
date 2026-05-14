"""
Parse exam_qbank.md into structured question objects + render investment-style HTML.

Output structure mirrors the EMBA Investment portal's exam tab:
- Per-question card with chapter pill, q-num, stem, options (MCQ), and toggle answer-box
- Filter pills by chapter with badge counts
- Test mode toggle (hides all answers at once)
"""
import re
from pathlib import Path

CHAPTER_LABELS = {
    'ch1a': 'Ch.1a',
    'ch1b': 'Ch.1b',
    'ch7':  'Ch.7',
    'ch8':  'Ch.8',
    'ch10': 'Ch.10',
    'ch11': 'Ch.11',
    'ch14': 'Ch.14',
}
CHAPTER_FULL_LABELS = {
    'ch1a': 'Ch.1a — Orientations',
    'ch1b': 'Ch.1b — Strategic Mgmt',
    'ch7':  'Ch.7 — STP',
    'ch8':  'Ch.8 — Product',
    'ch10': 'Ch.10 — Pricing',
    'ch11': 'Ch.11 — Promotion',
    'ch14': 'Ch.14 — Place',
}

# Reverse-map h3 chapter strings to slugs
CHAPTER_FROM_HEADING = {
    '1a': 'ch1a', '1b': 'ch1b', '7': 'ch7',
    '8': 'ch8', '10': 'ch10', '11': 'ch11', '14': 'ch14',
}

# Section letter -> question type
SECTION_TYPE = {'A': 'tf', 'B': 'mcq', 'C': 'short', 'D': 'essay'}
TYPE_LABEL = {'tf': 'True/False', 'mcq': 'MCQ', 'short': 'Short answer', 'essay': 'Essay'}


def _extract_citations(text: str) -> list[str]:
    """Extract `[Slide ...]` and `[Lec ...]` citations from a string."""
    cites = re.findall(r'`?\[(?:Slide|Lec)[^\]]+\]`?', text)
    return [c.strip('`') for c in cites]


def _strip_citations(text: str) -> str:
    """Remove citation tokens from rationale prose."""
    return re.sub(r'\s*`?\[(?:Slide|Lec)[^\]]+\]`?\s*', ' ', text).strip()


def _md_inline(text: str) -> str:
    """Minimal inline markdown -> HTML for stems and rationale prose.

    Handles: **bold**, *italic*, `code`, em-dash, line-breaks.
    Does NOT handle: links, lists, tables (those don't appear in stems).
    """
    text = text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    # Bold first (so we don't catch its asterisks as italics)
    text = re.sub(r'\*\*([^*]+?)\*\*', r'<strong>\1</strong>', text)
    # Backtick code (citations were already extracted upstream, so this only catches stray)
    text = re.sub(r'`([^`]+?)`', r'<code>\1</code>', text)
    # Italic
    text = re.sub(r'(?<!\*)\*(?!\*)([^\n*]+?)\*(?!\*)', r'<em>\1</em>', text)
    return text


def parse_qbank(md: str) -> list[dict]:
    """Parse exam_qbank.md into a list of question dicts.

    Each dict: {
        'type': 'tf'|'mcq'|'short'|'essay',
        'chapter': 'ch1a'|...,
        'num': int (visible number, global per-section),
        'stem': str,
        'options': [{'letter': 'A', 'text': str}, ...] (mcq only),
        'correct': 'TRUE'|'FALSE'|'A'|'B'|...|None,
        'rationale_html': str (inline-rendered rationale, may include <p>/<ul>),
        'citations': [str, ...],
    }
    """
    lines = md.split('\n')
    questions = []

    section_re   = re.compile(r'^##\s+([A-D])\.\s+')
    chapter_re   = re.compile(r'^###\s+Ch\.(\w+)')
    qnum_re      = re.compile(r'^\*\*(\d+)\.\*\*\s*(.*)$')
    option_re    = re.compile(r'^([A-E])\)\s*(.*)$')
    answer_start = re.compile(r'^\*Answer:\s*(.*?)(\*?)$')
    model_start  = re.compile(r'^\*Model answer.*?\*?$', re.IGNORECASE)
    section_break = re.compile(r'^---\s*$')

    current_section = None
    current_chapter = None
    current = None
    answer_buf = []  # collects multi-line answer body for short/essay
    in_answer = False

    def flush():
        nonlocal current, answer_buf, in_answer
        if current is not None:
            current['_answer_body'] = '\n'.join(answer_buf).strip()
            questions.append(current)
            current = None
            answer_buf = []
            in_answer = False

    for raw in lines:
        line = raw.rstrip()

        m = section_re.match(line)
        if m:
            flush()
            current_section = SECTION_TYPE.get(m.group(1))
            current_chapter = None  # reset chapter at every section break
            continue

        m = chapter_re.match(line)
        if m:
            flush()
            tag = m.group(1)  # e.g. "1a" or "7" (may have trailing chars)
            tag_norm = tag.split(' ')[0]
            current_chapter = CHAPTER_FROM_HEADING.get(tag_norm)
            continue

        m = qnum_re.match(line)
        if m:
            flush()
            if not current_section or not current_chapter:
                # Skip items in calibration intro before chapter context set
                # (we'll catch them by leaving current_chapter from prior)
                pass
            current = {
                'type': current_section,
                'chapter': current_chapter,  # may be None — post-process sniffer handles it
                'num': int(m.group(1)),
                'stem': m.group(2).strip(),
                'options': [],
            }
            answer_buf = []
            in_answer = False
            continue

        if current is None:
            continue

        if current['type'] == 'mcq':
            m = option_re.match(line)
            if m:
                current['options'].append({
                    'letter': m.group(1),
                    'text': m.group(2).strip()
                })
                continue

        if answer_start.match(line):
            in_answer = True
            m = answer_start.match(line)
            body = m.group(1).rstrip('*').rstrip()
            answer_buf.append(body)
            continue

        if model_start.match(line):
            in_answer = True
            answer_buf.append('**Model answer:**')
            continue

        if in_answer:
            # Stop collecting at section break or blank-then-something? Keep blank-line tolerance.
            if section_break.match(line):
                # don't break — section_break ends the question naturally on next flush
                pass
            answer_buf.append(line)

    flush()

    # Sniff chapter for questions without an explicit chapter heading
    # (e.g. the 2 calibration partial-miss MCQs at the start of section B)
    CHAPTER_SNIFFERS = [
        ('ch1a', ['customer satisfaction', 'managing profitable customer relationships',
                  'societal marketing', 'production concept', 'product concept',
                  'selling concept', 'marketing concept', 'relationship marketing',
                  'one-to-one marketing', 'market offering', 'value proposition']),
        ('ch1b', ['distinctive competency', 'success requirement', 'ansoff', 'swot',
                  'mission', 'marketing audit', 'marketing goals', 'environmental opportunit']),
        ('ch7',  ['segmentation', 'targeting', 'positioning', 'segment', 'target market',
                  'undifferentiated', 'differentiated', 'concentrated', 'micromarketing',
                  'exchange relationship', 'buyers shar']),
        ('ch8',  ['product life cycle', 'plc', 'packaging', 'branding', 'brand equity',
                  'consumer product', 'industrial product', 'service marketing']),
        ('ch10', ['pricing', 'skimming', 'penetration', 'price elasticity', 'cost-based',
                  'value-based']),
        ('ch11', ['promotion mix', 'imc', 'integrated marketing communication',
                  'advertising', 'sales promotion', 'public relations', 'push', 'pull',
                  'aida']),
        ('ch14', ['channel', 'distribution', 'vms', 'wholesal', 'retail', 'logistic',
                  '3pl', 'intensive distribution', 'selective distribution',
                  'exclusive distribution']),
    ]
    for q in questions:
        if q.get('chapter') is None:
            stem_l = q['stem'].lower()
            best_ch = 'ch1a'
            best_hits = 0
            for ch, keywords in CHAPTER_SNIFFERS:
                hits = sum(1 for kw in keywords if kw in stem_l)
                if hits > best_hits:
                    best_hits = hits
                    best_ch = ch
            q['chapter'] = best_ch

    # Post-process: extract correct answer + rationale html
    for q in questions:
        body = q.pop('_answer_body', '').strip()
        cites = _extract_citations(body)
        clean = _strip_citations(body)
        # Strip trailing single asterisk if present
        clean = clean.rstrip('*').strip()

        q['citations'] = cites

        if q['type'] == 'tf':
            m = re.match(r'^(TRUE|FALSE)\.?\s*(.*)$', clean, re.IGNORECASE | re.DOTALL)
            if m:
                q['correct'] = m.group(1).upper()
                rationale = m.group(2).strip()
            else:
                q['correct'] = None
                rationale = clean
            q['rationale_html'] = _md_inline(rationale)

        elif q['type'] == 'mcq':
            # Match "**B — expectations**. rationale..." or "B. rationale..."
            m = re.match(r'^\*?\*?\s*([A-E])\b[^.\n]*\.?\s*(.*)$', clean, re.DOTALL)
            if m:
                q['correct'] = m.group(1)
                rationale = m.group(2).strip()
            else:
                q['correct'] = None
                rationale = clean
            q['rationale_html'] = _md_inline(rationale)

        else:  # short / essay
            q['correct'] = None
            # Treat answer body as block markdown — convert lists + paragraphs minimally
            q['rationale_html'] = _render_block_md(clean)

    return questions


def _render_block_md(md: str) -> str:
    """Render a block of markdown (possibly with lists, multiple paragraphs)
    into safe inline HTML. No tables / no code-blocks (not used in answer bodies)."""
    if not md.strip():
        return ''
    blocks = re.split(r'\n\n+', md.strip())
    out = []
    for blk in blocks:
        lines = blk.split('\n')
        # Check if it's a bulleted list
        if all(re.match(r'^\s*[-*]\s+', l) or not l.strip() for l in lines if l.strip()):
            items = [_md_inline(re.sub(r'^\s*[-*]\s+', '', l)) for l in lines if l.strip()]
            out.append('<ul>' + ''.join(f'<li>{i}</li>' for i in items) + '</ul>')
        elif all(re.match(r'^\s*\d+\.\s+', l) or not l.strip() for l in lines if l.strip()):
            items = [_md_inline(re.sub(r'^\s*\d+\.\s+', '', l)) for l in lines if l.strip()]
            out.append('<ol>' + ''.join(f'<li>{i}</li>' for i in items) + '</ol>')
        else:
            out.append(f'<p>{_md_inline(blk.replace(chr(10), " "))}</p>')
    return '\n'.join(out)


def render_question(q: dict, global_num: int) -> str:
    """Render one question card as investment-style HTML."""
    ch = q['chapter']
    chap_label = CHAPTER_LABELS.get(ch, ch.upper())
    q_type = q['type']
    type_label = TYPE_LABEL.get(q_type, q_type.upper())

    # Source — concatenate the first 1-2 citations
    src = ''
    if q['citations']:
        src = ' · '.join(q['citations'][:2])

    # Stem
    stem_html = _md_inline(q['stem'])

    # Options block (MCQ only)
    options_html = ''
    if q_type == 'mcq' and q['options']:
        items = []
        for opt in q['options']:
            cls = 'correct' if opt['letter'] == q['correct'] else ''
            letter_lower = opt['letter'].lower()
            opt_text = _md_inline(opt['text'])
            items.append(
                f'    <li class="{cls}" data-letter="{letter_lower})">{opt_text}</li>'
            )
        options_html = f'  <ul class="q-options">\n' + '\n'.join(items) + '\n  </ul>\n'

    # Correct-answer badge text
    correct_badge = ''
    if q['correct']:
        correct_badge = f'<span class="answer-letter">{q["correct"]}</span><span class="answer-tag">ANSWER</span>'

    # Citation list inside answer-body
    cite_html = ''
    if q['citations']:
        cite_html = '<p class="answer-cites">' + ' '.join(
            f'<span class="citation">{c}</span>' for c in q['citations']
        ) + '</p>'

    rationale = q.get('rationale_html', '')
    if rationale and not rationale.startswith('<'):
        rationale = f'<p>{rationale}</p>'

    why_block = ''
    if rationale:
        why_block = f'''  <div class="answer-why">
    <strong class="label">Why:</strong>
    <div class="why-body">{rationale}</div>
  </div>'''

    return f'''<div class="exam-q" data-chapter="{ch}" data-type="{q_type}">
  <div class="exam-q-head">
    <span class="chapter-tag {ch}">{chap_label}</span>
    <span class="q-type-tag">{type_label}</span>
    <span class="q-num">Q{global_num}</span>
    {f'<span class="q-source">{src}</span>' if src else ''}
  </div>
  <div class="q-text">{stem_html}</div>
{options_html}  <div class="answer-box">
    <button class="answer-toggle" aria-expanded="false">Show answer</button>
    <div class="answer-body">
      <div class="answer-head">{correct_badge}</div>
{why_block}
      {cite_html}
    </div>
  </div>
</div>'''


def render_qbank(md_text: str) -> tuple[str, dict]:
    """Render the full Q-bank as HTML. Returns (html, stats_dict)."""
    questions = parse_qbank(md_text)

    # Count per chapter
    counts = {ch: 0 for ch in CHAPTER_LABELS}
    counts['all'] = len(questions)
    for q in questions:
        counts[q['chapter']] = counts.get(q['chapter'], 0) + 1

    # Render each question
    cards = []
    for i, q in enumerate(questions, 1):
        cards.append(render_question(q, i))

    # Build filter bar
    filter_buttons = ['<button class="filter-btn active" data-filter="all">All <span class="badge">' + str(counts['all']) + '</span></button>']
    for ch in ['ch1a', 'ch1b', 'ch7', 'ch8', 'ch10', 'ch11', 'ch14']:
        n = counts.get(ch, 0)
        if n > 0:
            filter_buttons.append(
                f'<button class="filter-btn" data-filter="{ch}">{CHAPTER_FULL_LABELS[ch]} '
                f'<span class="badge">{n}</span></button>'
            )

    # Type filter — only if multiple types present
    type_counts = {}
    for q in questions:
        type_counts[q['type']] = type_counts.get(q['type'], 0) + 1
    type_buttons = []
    if len(type_counts) > 1:
        type_buttons.append(
            '<button class="type-btn active" data-type="all">All types '
            f'<span class="badge">{counts["all"]}</span></button>'
        )
        for t in ['tf', 'mcq', 'short', 'essay']:
            if type_counts.get(t):
                type_buttons.append(
                    f'<button class="type-btn" data-type="{t}">{TYPE_LABEL[t]} '
                    f'<span class="badge">{type_counts[t]}</span></button>'
                )

    type_bar = ''
    if type_buttons:
        type_bar = '<div class="filter-row type-row">' + ''.join(type_buttons) + '</div>'

    controls = f'''<div class="exam-controls">
  <div class="filter-row chapter-row">{''.join(filter_buttons)}</div>
  {type_bar}
  <div class="exam-controls-right">
    <button id="testModeBtn" class="test-mode-toggle">🎯 Test mode</button>
    <button id="revealAllBtn" class="test-mode-toggle">👁 Reveal all</button>
    <button id="hideAllBtn" class="test-mode-toggle">🙈 Hide all</button>
  </div>
</div>
<div class="exam-empty" id="examEmpty" hidden>No questions match the current filter.</div>'''

    html = controls + '\n\n<div id="examQuestions">\n' + '\n'.join(cards) + '\n</div>'

    stats = {'total': counts['all'], 'per_chapter': counts, 'per_type': type_counts}
    return html, stats
