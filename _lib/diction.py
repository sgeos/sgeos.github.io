#!/usr/bin/env python3
"""Pathological word and phrase usage, measured against the author's own corpus.

THIS MODULE EXISTS BECAUSE ITS PREDECESSOR WAS LOST. A `diction.py` was written
for A320 and copied into A321, A322 and A323. A369 never received a copy, and
the analysis was redone by hand, rediscovering the same prose-stripping rules
and the same phrase list while missing the acronym check the original had. Four
copies and then silence is the exact pattern this library was built to end.

The original was written because an article reached 46.2 uses of `specific` per
thousand words while passing style review with prose reported clean.

WHY _verify.py CANNOT DO THIS. Its `prose_text` strips math, code and Liquid but
NOT `[text][anchor]` pairs, so reference link text counts as prose. In a survey
article that is fatal: A369 carries 1,650 harvested titles, which inflate the
denominator from 11,830 author words to 27,178 and dilute every rate by well
over half. This module strips citation link text, which is what makes the
measurement about the author rather than about the bibliography.

WHY A FIXED THRESHOLD IS THE WRONG DISCRIMINATOR. The original flagged anything
above 5.0 per thousand, which cannot distinguish a tic from a subject noun:
`instruction` at 5.4 per thousand in a compiler article is what the article is
about. `baseline` compares against peer articles instead, so a construction is
flagged when it is unusual FOR THIS AUTHOR. Domain nouns score near-infinite
ratios against unrelated peers and are therefore reported separately and
ignored, which is a limitation stated rather than hidden.
"""

import collections
import glob as _glob
import os
import re
import statistics
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import post  # noqa: E402

# Constructions worth watching. The first group came from the A320 tool, the
# rest were found in A369 by comparing against peers.
PHRASES = [
    "rather than", "and not", "instead of", "which is the", "which is",
    "it is worth", "worth noting", "worth stating", "worth showing",
    "which is why", "that is why", "in other words", "it is important",
    "the fact that", "is not a", "and it is", "this article",
    "the second is", "in which the", "is the same", "it is the",
]

STOP = set("""the a an and or but of to in on at for with by from as is are was were be been
being it its this that these those which who whom whose what when where how why not no nor
so than then there here their they them he she his her we us our you your i me my if all
any both each few more most other some such only own same too very can will just should now
into over under again further once about above below between through during before after
because while against among within without upon per also may might must shall would could
one two three four five six seven eight nine ten""".split())


def prose(text):
    """Author prose only. Citation link text, math, code and tables removed.

    Order matters. Link pairs go first, because a title containing a dollar sign
    or a pipe would otherwise be partly eaten by the later rules and leave debris.
    """
    body = post.body(text)
    p = post.LINK_PAIR.sub(" ", body)
    p = re.sub(rf"(?m)^\[{post.ANCHOR}\]:.*$", " ", p)
    p = post.strip_code(p)
    p = re.sub(r"(?s)\$\$.*?\$\$", " ", p)
    p = re.sub(r"(?<!\$)\$(?!\$)[^$\n]+\$(?!\$)", " ", p)
    p = re.sub(r"`[^`\n]+`", " ", p)
    p = re.sub(r"<[^>]+>", " ", p)
    p = re.sub(r"(?m)^\|.*$", " ", p)
    return p


def words(text):
    return re.findall(r"[A-Za-z][A-Za-z'-]+", prose(text))


def rates(text, patterns=PHRASES):
    """Occurrences per thousand author words, for each pattern."""
    p = prose(text)
    n = len(re.findall(r"[A-Za-z][A-Za-z'-]+", p)) or 1
    out = {}
    for ph in patterns:
        # A hyphenated technical compound is a domain term, not a style tic.
        # `application-specific` and `target-specific` are not the overuse of
        # `specific` this check hunts, and counting them inflates the signal
        # that matters. Word boundaries alone match inside compounds, because a
        # hyphen IS a boundary, so the neighbours are excluded explicitly.
        k = len(re.findall(r"(?<![\w-])" + re.escape(ph) + r"(?![\w-])", p, re.I))
        out[ph] = (k, 1000.0 * k / n)
    return out, n


def baseline(paths, patterns=PHRASES):
    """Median and maximum rate for each pattern across peer articles.

    A peer set of one is not a baseline. Callers should pass the articles
    written in the same voice, which for this corpus means the same series.
    """
    acc = collections.defaultdict(list)
    used = 0
    for p in paths:
        try:
            t = open(p, encoding="utf-8").read()
        except OSError:
            continue
        used += 1
        r, _ = rates(t, patterns)
        for ph, (_, per_k) in r.items():
            acc[ph].append(per_k)
    return {ph: {"median": statistics.median(v), "max": max(v), "n": len(v)}
            for ph, v in acc.items() if v}, used


def compare(text, peer_paths, patterns=PHRASES):
    """Rows of (pattern, count, rate, median, max, verdict), worst first.

    `over-max` is the finding that matters. It means the construction is used
    more heavily than in ANY article the author has written, which is evidence
    of a tic rather than of subject matter.
    """
    base, npeers = baseline(peer_paths, patterns)
    mine, n = rates(text, patterns)
    rows = []
    for ph, (k, per_k) in mine.items():
        b = base.get(ph)
        if not b:
            rows.append((ph, k, per_k, None, None, "no-baseline"))
            continue
        verdict = ("over-max" if per_k > b["max"] else
                   "over-median" if per_k > b["median"] else "ok")
        rows.append((ph, k, per_k, b["median"], b["max"], verdict))
    order = {"over-max": 0, "over-median": 1, "no-baseline": 2, "ok": 3}
    rows.sort(key=lambda r: (order[r[5]], -(r[2] or 0)))
    return rows, n, npeers


def overused_words(text, limit=5.0, min_count=10):
    """Content-independent words above a rate. The original tool's check.

    Retained because it needs no peer set, which makes it usable on the first
    article of a new series when `compare` has nothing to compare against.
    """
    w = [x.lower() for x in words(text)]
    n = len(w) or 1
    out = []
    for word, k in collections.Counter(w).items():
        if word in STOP or len(word) < 4 or k < min_count:
            continue
        per_k = 1000.0 * k / n
        if per_k >= limit:
            out.append((per_k, k, word))
    return sorted(out, reverse=True)


def repeated_ngrams(text, size=3, min_count=6):
    w = [x.lower() for x in words(text)]
    c = collections.Counter(" ".join(w[i:i + size]) for i in range(len(w) - size + 1))
    return [(k, g) for g, k in c.most_common() if k >= min_count]


def acronyms(text, exempt=()):
    """First use of each acronym, and whether it looks spelled out nearby.

    The check the hand-rolled A369 analysis omitted entirely. Heuristic by
    nature: it looks for the initials appearing as word starts within a window,
    so it reports candidates for reading rather than verdicts.
    """
    p = prose(text)
    ex = {x.upper() for x in exempt}
    seen = {}
    for m in re.finditer(r"\b([A-Z]{2,6})\b", p):
        a = m.group(1)
        if a in ex or a in seen:
            continue
        seen[a] = m.start()
    out = []
    for a, pos in sorted(seen.items(), key=lambda kv: kv[1]):
        window = p[max(0, pos - 260):pos + 260]
        pat = r"\b" + r"[a-z]*\s+".join(list(a)) + r"[a-z]*"
        out.append((a, pos, re.search(pat, window, re.I) is not None))
    return out


def report(path, peer_glob=None, patterns=PHRASES):
    """One-shot human report. Peers default to siblings in the same directory."""
    text = open(path, encoding="utf-8").read()
    peers = [p for p in _glob.glob(peer_glob or os.path.join(os.path.dirname(path) or ".", "*.markdown"))
             if os.path.abspath(p) != os.path.abspath(path)]
    rows, n, npeers = compare(text, peers, patterns)
    print(f"{os.path.basename(path)}: {n} author prose words, {npeers} peers")
    print(f"  {'construction':18s} {'n':>4s} {'rate':>6s} {'median':>7s} {'max':>6s}  verdict")
    for ph, k, per_k, med, mx, verdict in rows:
        if verdict == "ok":
            continue
        ms = f"{med:7.2f}" if med is not None else "      -"
        xs = f"{mx:6.2f}" if mx is not None else "     -"
        print(f"  {ph:18s} {k:4d} {per_k:6.2f} {ms} {xs}  {verdict}")
    flagged = [r for r in rows if r[5] == "over-max"]
    print(f"  {len(flagged)} construction(s) above the corpus maximum")
    return rows


# ===========================================================================================
# Collocation. THE DISCRIMINATOR BETWEEN A TERM OF ART AND A VERBAL TIC.
#
# A rate cannot tell them apart and the corpus has paid for that twice. `specific` reaches
# 15.07 per thousand in the rocket propellant articles and 87 percent of those uses are the
# phrase "specific impulse", which names a quantity and cannot be paraphrased. `substantial`
# reaches 10.6 in the hardware description languages article and names nothing at all. The
# counts look alike. Only the neighbouring words separate them.
#
# THIS REPORTS AND DOES NOT CLASSIFY, and the restraint is deliberate. An automatic verdict
# needs to know that "achieved substantial" is a verb followed by an adjective while
# "capability configuration" is a compound noun, and that is a part-of-speech judgement this
# module has no tagger for. A wrong verdict here would license deleting a term of art from a
# published article, so the tool lays out the evidence and a human writes the reason into
# `_verify_exemptions.yml`.
#
# DIRECTION MATTERS AND IT IS NOT THE SAME FOR EVERY WORD. For a noun such as `configuration`
# the compound is formed by what PRECEDES it. For an adjective such as `specific` it is formed
# by what FOLLOWS. Both directions are therefore returned and neither is privileged.
# ===========================================================================================

_FUNCTION_WORDS = frozenset("""
a an the this that these those its it his her their our my your no any some each every
and or but nor so yet for of to in on at by with from as is are was were be been being
has have had do does did will would can could may might must shall should
more most much many few less least such than then there here when where which who whom
not only also very quite rather one two both either neither
""".split())


def collocations(text, word, limit=10, already_prose=False):
    """Words immediately before and after each occurrence, in author prose only.

    Pass `already_prose=True` when the caller has done its own prose extraction. A count and a
    share drawn from two different extractions do not agree, and a warning reading
    "`specific` 59x ... top collocate `specific impulse` 57x = 86%" contradicts its own
    arithmetic, because 57 of 59 is 97 percent. The 86 came from this module counting 66.

    Returns (total, before, after, stats) where before and after are lists of
    (collocate, count) sorted by count, and stats carries the concentration figures a
    reader needs to judge whether the word is participating in a named term.

    Reference link text is excluded, because a bibliography is other people's words and in a
    citation-heavy article it swamps the author's.
    """
    body = text if already_prose else prose(text)
    tokens = [t.lower() for t in re.findall(r"[A-Za-z][A-Za-z'-]*", body)]
    target = word.lower()
    before, after = collections.Counter(), collections.Counter()
    total = 0
    for i, tok in enumerate(tokens):
        if tok != target:
            continue
        total += 1
        if i:
            before[tokens[i - 1]] += 1
        if i + 1 < len(tokens):
            after[tokens[i + 1]] += 1

    def _named(counter):
        return sum(k for w, k in counter.items() if w not in _FUNCTION_WORDS)

    stats = {
        "total": total,
        "before_named": _named(before),
        "after_named": _named(after),
        # Concentration: how much of the usage one collocate accounts for. High
        # concentration in either direction is the signature of a fixed term.
        "top_before": (before.most_common(1)[0] if before else ("", 0)),
        "top_after": (after.most_common(1)[0] if after else ("", 0)),
    }
    stats["top_share"] = (
        max(stats["top_before"][1], stats["top_after"][1]) / total if total else 0.0
    )
    stats["named_share"] = (
        max(stats["before_named"], stats["after_named"]) / total if total else 0.0
    )
    return total, before.most_common(limit), after.most_common(limit), stats


def top_collocate(text, word, already_prose=False):
    """The single most frequent neighbouring word and its share, either direction.

    Intended for a one-line annotation on a frequency warning, so that the warning carries
    the evidence needed to triage it instead of only a count.
    """
    total, _before, _after, _stats = collocations(text, word, already_prose=already_prose)
    if not total:
        return "", 0, 0.0, ""
    # A FUNCTION WORD IS NOT EVIDENCE. "configuration the" is the most frequent pair in one
    # article and says nothing about whether the word names a term, so the strongest CONTENT
    # collocate is reported instead and the function words are passed over.
    def strongest(pairs):
        for w, k in pairs:
            if w not in _FUNCTION_WORDS:
                return w, k
        return "", 0

    bw, bn = strongest(_before)
    aw, an = strongest(_after)
    if an > bn:
        return aw, an, an / total, f"{word} {aw}"
    return bw, bn, bn / total, f"{bw} {word}"


# The tic class. Pathological BY KIND rather than by rate, because every member can be
# deleted from a sentence without changing its meaning. Enumerated rather than discovered,
# since a relative check cannot separate a tic from a subject and usually flags the subject.
TICS = """
specific specifically particular particularly essential essentially fundamental fundamentally
crucial crucially critical key vital important importantly significant significantly
notable notably remarkable remarkably interesting interestingly
indeed actually really truly genuinely certainly clearly obviously evidently plainly
simply merely just only quite very rather somewhat fairly relatively
precisely exactly literally effectively basically generally typically usually
robust seamless leverage utilise utilize holistic comprehensive nuanced
underlying inherent intrinsic straightforward trivial nontrivial obvious
furthermore moreover additionally however nevertheless nonetheless therefore thus hence
overall ultimately arguably presumably
delve realm landscape tapestry testament pivotal
""".split()


# ===========================================================================================
# QUOTED MATERIAL IS NOT THE AUTHOR'S PROSE EITHER.
#
# `prose` strips reference link text on the stated ground that a bibliography is other
# people's words. A block quotation and a long inline quoted fragment are other people's
# words by the identical argument, and `prose` keeps both. In A376, which carries 124 block
# quotations, 7.0 percent of what `prose` attributes to the author is quoted material.
#
# THE BIAS RUNS ONE WAY. Quoted words enlarge the denominator and therefore DILUTE every
# rate, which pushes comparisons toward false negatives, and a false negative is the outcome
# that hides a tic. A quoted word also cannot be edited, so counting it against the author
# would be unactionable even if the arithmetic were right.
#
# WHY THIS IS A SEPARATE FUNCTION RATHER THAN A CHANGE TO `prose`. Every rate `_verify.py`
# reports, and every exemption reason recorded against one, was measured with quotations
# included. Redefining `prose` would silently move every number in the corpus and invalidate
# the recorded reasons. Callers that want the stricter denominator ask for it, and when both
# sides of a comparison use it the dilution cancels.
# ===========================================================================================

_QUOTED_INLINE = re.compile(r'"[^"\n]{8,}"')


def author_prose(text):
    """`prose` with block quotations and long inline quoted fragments removed.

    The 8-character floor on an inline fragment keeps short quoted terms of art, which an
    author chooses and is responsible for, while removing quoted sentences, which the author
    did not write. A comparison must apply this to the peers as well as to the article.
    """
    p = prose(text)
    p = "\n".join(ln for ln in p.split("\n") if not ln.lstrip().startswith(">"))
    return _QUOTED_INLINE.sub(" ", p)


def quoted_share(text):
    """(author words, quoted words, quoted fraction) under `author_prose`.

    Reported so that a clean result can state how much dilution it survived, rather than
    leaving a reader to assume the denominator was the author's.
    """
    total = len(words(text))
    own = len(re.findall(r"[A-Za-z][A-Za-z'-]+", author_prose(text)))
    return own, total - own, (total - own) / total if total else 0.0


# TOKENS RATHER THAN DELETIONS. Deleting a citation joined the words either side of
# it into sequences that occur nowhere in the text, and deleting numerals produced
# the phantom `at percent in` from `at 30 percent in` and `at 4 percent in`. Each is
# replaced by a placeholder token instead, so `is CITE` and `at NUM percent` are
# counted as what they are: formulas with a slot.
CITE, NUM, MATH = "<cite>", "<num>", "<math>"
_PLACEHOLDERS = {CITE, NUM, MATH}


def tokens(text, strict=True):
    """Lower-cased author tokens with citations, numbers and inline math as placeholders.

    `strict` also removes quotations, as `author_prose` does. Sentence ends are
    kept as the token `.` so callers can split on them.
    """
    body = post.body(text)
    body = post.LINK_PAIR.sub(f" {CITE} ", body)
    body = re.sub(rf"(?m)^\[{post.ANCHOR}\]:.*$", " ", body)
    body = post.strip_code(body)
    body = re.sub(r"(?s)\$\$.*?\$\$", " ", body)
    body = re.sub(r"(?<!\$)\$(?!\$)[^$\n]+\$(?!\$)", f" {MATH} ", body)
    body = re.sub(r"`[^`\n]+`", " ", body)
    body = re.sub(r"<(?!cite>|num>|math>)[^>]+>", " ", body)
    body = re.sub(r"(?m)^\|.*$", " ", body)
    if strict:
        body = "\n".join(ln for ln in body.split("\n") if not ln.lstrip().startswith(">"))
        body = _QUOTED_INLINE.sub(" ", body)
    body = re.sub(r"\d+(?:[.,]\d+)*", f" {NUM} ", body)
    raw = re.findall(r"<cite>|<num>|<math>|[A-Za-z][A-Za-z'-]*|[.!?]", body)
    return [t if t in _PLACEHOLDERS else ("." if t in ".!?" else t.lower()) for t in raw]


def ngrams(toks, sizes=(2, 3, 4)):
    """Counts of word sequences that do not cross a sentence end or consist only of placeholders.

    The final sequence is counted. An earlier version looped to `len - size` and
    never counted the last one.
    """
    c = collections.Counter()
    sentence = []
    for t in toks + ["."]:
        if t == ".":
            for s in sizes:
                for i in range(len(sentence) - s + 1):
                    g = sentence[i:i + s]
                    if not all(x in _PLACEHOLDERS for x in g):
                        c[" ".join(g)] += 1
            sentence = []
        else:
            sentence.append(t)
    return c


def _word_count(toks):
    return sum(1 for t in toks if t != "." and t not in _PLACEHOLDERS) or 0


def phrase_outliers(text, peer_texts, sizes=(2, 3, 4), min_count=4, strict=True, min_peer_words=400):
    """Repeated word sequences used more heavily than in ANY peer. DISCOVERED, not enumerated.

    `compare` tests the hand-listed constructions in `PHRASES`, so a formula nobody
    thought to enumerate cannot be found by it. Every sequence the article repeats is
    scored against the highest rate any peer reaches, and a peer that never uses it
    contributes a zero.

    BIGRAMS ARE INCLUDED. A369's largest finding was the bigram `and not`, which a
    three-and-four-word scan cannot see. Citations, numbers and inline math are slot
    tokens, so `is <cite>` is countable and `at <num> percent` is not a phantom.

    SUBJECT MATTER DOMINATES THE OUTPUT, exactly as it does for single words. The result
    is a reading list and the caller supplies the judgement.

    Returns rows of (ratio_to_peer_max, phrase, count, rate, peer_max), worst first, with a
    ratio of None where no peer ever used the phrase.
    """
    mine_t = tokens(text, strict)
    n = _word_count(mine_t)
    if not n:
        return [], 0
    mine = ngrams(mine_t, sizes)
    cand = {g: k for g, k in mine.items() if k >= min_count}
    peer_max = collections.defaultdict(float)
    peers = 0
    for pt in peer_texts:
        pt_t = tokens(pt, strict)
        pn = _word_count(pt_t)
        if pn < min_peer_words:
            continue
        peers += 1
        pc = ngrams(pt_t, sizes)
        for g in cand:
            k = pc.get(g, 0)
            if k:
                peer_max[g] = max(peer_max[g], 1000.0 * k / pn)
    rows = []
    for g, k in cand.items():
        rate = 1000.0 * k / n
        mx = peer_max.get(g, 0.0)
        rows.append((rate / mx if mx else None, g, k, rate, mx))
    rows.sort(key=lambda r: (-1e9 if r[0] is None else -r[0]))
    return rows, peers


def word_rates(text, vocabulary=None):
    """Occurrences per thousand author prose words, for each word in a vocabulary.

    CASE IS FOLDED. Counting without it missed every sentence-initial use, 51 of
    the corpus's 116 uses of `however`, so a tic that opens sentences was
    invisible to exactly the check meant to find it.
    """
    ws = [w.lower() for w in words(text)]
    n = len(ws)
    if not n:
        return {}, 0
    counts = collections.Counter(ws)
    vocab = vocabulary if vocabulary is not None else counts.keys()
    return {w: 1000.0 * counts.get(w, 0) / n for w in vocab}, n


def word_outliers(text, peer_texts, vocabulary=None, min_count=6):
    """Words this article uses more than ANY peer article ever has.

    A fixed per-thousand limit asks whether a word is frequent, which for a technical article
    is often just what the subject requires. This asks whether the article exceeds the
    author's own established practice, which is a better proxy for a tic.

    A PEER THAT NEVER USES THE WORD CONTRIBUTES A ZERO. Taking the maximum over only the peers
    that happen to use a word makes every rate look unremarkable.

    Returns rows of (ratio_to_peer_max, word, count, rate, median, peer_max, peers_using),
    worst first. A ratio of None means no peer ever used the word.
    """
    ws = [w.lower() for w in words(text)]
    n = len(ws)
    counts = collections.Counter(ws)
    peer_rates = collections.defaultdict(list)
    peer_n = 0
    for pt in peer_texts:
        prates, pn = word_rates(pt)
        if pn < 400:
            continue
        peer_n += 1
        for w, r in prates.items():
            peer_rates[w].append(r)

    rows = []
    vocab = vocabulary if vocabulary is not None else counts.keys()
    for w in vocab:
        k = counts.get(w, 0)
        if k < min_count or not w.isalpha() or len(w) < 3:
            continue
        rate = 1000.0 * k / n if n else 0.0
        rs = sorted(peer_rates.get(w, []) + [0.0] * (peer_n - len(peer_rates.get(w, []))))
        if not rs:
            rows.append((None, w, k, rate, 0.0, 0.0, 0))
            continue
        mx, med = rs[-1], rs[len(rs) // 2]
        used = sum(1 for r in rs if r > 0)
        rows.append((rate / mx if mx else None, w, k, rate, med, mx, used))
    rows.sort(key=lambda r: (-1e9 if r[0] is None else -r[0]))
    return rows, peer_n


def collocation_report(path, word, limit=10):
    """Print the evidence needed to decide whether `word` names a term or is a tic.

    Prints both directions, because the compound side differs by part of speech, and prints
    the concentration figures. IT OFFERS NO VERDICT. The reader writes the verdict into
    `_verify_exemptions.yml` as a reason, which is what makes that file auditable.
    """
    text = open(path, encoding="utf-8").read()
    total, before, after, stats = collocations(text, word, limit)
    n = len(words(text))
    rate = 1000.0 * total / n if n else 0.0
    print(f"{os.path.basename(path)}: `{word}` {total}x in {n:,} author prose words "
          f"= {rate:.2f}/1k")
    print(f"  top collocate share {stats['top_share'] * 100:.0f} percent, "
          f"content-word share {stats['named_share'] * 100:.0f} percent")
    print(f"  {'preceding':>24s} | following")
    for i in range(max(len(before), len(after))):
        b = f"{before[i][0]} {word} ({before[i][1]})" if i < len(before) else ""
        a = f"{word} {after[i][0]} ({after[i][1]})" if i < len(after) else ""
        print(f"  {b:>24s} | {a}")
    return total, before, after, stats


# ================================================================ further instruments
#
# Each of these was a scratch script in a pass that then lost it. The survey of
# 24 October 2026 found them under tmp/cite/, tmp/a370/ and tmp/a372/.

def _sentences(toks):
    out, cur = [], []
    for t in toks + ["."]:
        if t == ".":
            if cur:
                out.append(cur)
            cur = []
        else:
            cur.append(t)
    return out


def openers(text, peer_texts, size=2, min_count=4, min_peer_sentences=40):
    """Sentence openings used more often than in any peer, per hundred sentences.

    A framework article opened 106 of 273 sentences with `The framework provides`,
    and A377 opened 18 with `and found`. No word or phrase rate sees this, because
    the words are common and the repetition is in the position.
    """
    def count(t):
        sents = [x for x in _sentences(tokens(t)) if len(x) >= size]
        return collections.Counter(" ".join(x[:size]) for x in sents), len(sents)
    mine, n = count(text)
    if not n:
        return [], 0
    peer_max, peers = collections.defaultdict(float), 0
    cand = {g for g, k in mine.items() if k >= min_count}
    for pt in peer_texts:
        pc, pn = count(pt)
        if pn < min_peer_sentences:
            continue
        peers += 1
        for g in cand:
            if pc.get(g):
                peer_max[g] = max(peer_max[g], 100.0 * pc[g] / pn)
    rows = []
    for g in cand:
        rate = 100.0 * mine[g] / n
        mx = peer_max.get(g, 0.0)
        rows.append((rate / mx if mx else None, g, mine[g], rate, mx))
    rows.sort(key=lambda r: (-1e9 if r[0] is None else -r[0]))
    return rows, peers


# Constructions found by reading in the X-Planes word pass and A364, which no rate
# discovers because each is a SHAPE with a variable slot. Each is (name, pattern,
# where), where `where` is `body` for the article body or `headings`.
SHAPES = [
    ("citation as the predicate of is", r"\b(?:is|are)\s+\\?\[?\[[A-Z][^\]\n]*\]\[", "body"),
    ("attribution formula", r"\bas\s+(?:[A-Z]\w+\s+){1,4}(?:records|reports|notes|states|shows|finds)\b", "body"),
    ("according to", r"\baccording to\b", "body"),
    ("not X, it is Y", r"\bis not [^.\n]{1,80}\.\s+(?:It|This|That) is\b", "body"),
    ("the section headed", r"\bthe section headed\b", "body"),
    ("bold paragraph opener", r"(?m)^\*\*(?:So|And|But|Thus|Hence)\b", "body"),
    ("let X be", r"(?m)^Let \$[^$]+\$ be\b", "body"),
    ("heading formula", r"(?m)^#{2,4} .*, (?:Which|Where|What|Because|and Why)\b", "headings"),
]


def shapes(text, peer_texts):
    """Rows of (name, count, rate, peer_max) for each construction shape, per thousand words."""
    def measure(t):
        body = post.strip_code(post.body(t))
        n = len(words(t)) or 1
        return {name: len(re.findall(pat, body)) for name, pat, _w in SHAPES}, n
    mine, n = measure(text)
    peer_max = collections.defaultdict(float)
    for pt in peer_texts:
        pc, pn = measure(pt)
        if pn < 400:
            continue
        for name, k in pc.items():
            peer_max[name] = max(peer_max[name], 1000.0 * k / pn)
    return [(name, k, 1000.0 * k / n, peer_max[name]) for name, k in mine.items()], n


def display_lead_ins(text, min_count=3, size=3):
    """The last words before a display equation, when one phrasing introduces many.

    One article introduced 429 of 488 displays with `admits the compact form`. The
    phrasing is fine once and a formula at scale.
    """
    body = post.strip_code(post.body(text))
    leads = collections.Counter()
    lines = body.split("\n")
    for i, line in enumerate(lines):
        if line.strip().startswith("$$") and i:
            prev = next((lines[j] for j in range(i - 1, -1, -1) if lines[j].strip()), "")
            ws = re.findall(r"[A-Za-z][A-Za-z'-]*", prev.lower())
            if len(ws) >= size:
                leads[" ".join(ws[-size:])] += 1
    total = sum(leads.values())
    return [(g, k, total) for g, k in leads.most_common() if k >= min_count]


def sentence_repeats(text, min_repeats=3):
    """Sentences in which one content word appears `min_repeats` times or more.

    A pass once reduced sentences with three uses of one word from 37 to 2 by
    reading. This finds them without reading.
    """
    out = []
    for sent in _sentences(tokens(text)):
        c = collections.Counter(t for t in sent if t not in STOP and t not in _PLACEHOLDERS and len(t) > 3)
        hits = [(w, k) for w, k in c.items() if k >= min_repeats]
        if hits:
            out.append((hits, " ".join(sent)[:160]))
    return out


# Counters for substitution creep. A fix for one tic installs another: `rather than`
# became `and not` and pushed it past the corpus maximum in A369 and A374, and cuts
# of `find` raised `their` in A378. These are counted with punctuation, which the
# word tokeniser drops, so `, not` is visible.
CREEP = [", not", "and not", "rather than", "instead of", "according to", "which is", "that is"]


def creep(before_text, after_text, sizes=(2, 3, 4), min_after=2):
    """Sequences that rose across an edit pass, and the substitution counters.

    Returns (rows, counters). Rows are (phrase, before, after) for every sequence
    whose count rose to at least `min_after`. A threshold below the peer test is
    deliberate, because creep starts small and the formulas report only phrases
    already over every peer.
    """
    b, a = ngrams(tokens(before_text), sizes), ngrams(tokens(after_text), sizes)
    rows = sorted(((g, b.get(g, 0), k) for g, k in a.items() if k >= min_after and k > b.get(g, 0)),
                  key=lambda r: (r[1] - r[2], r[0]))
    pb, pa = prose(before_text).lower(), prose(after_text).lower()
    counters = [(c, pb.count(c), pa.count(c)) for c in CREEP]
    return rows, counters


def carriers(word, paths, rate=5.0, min_count=8):
    """Which articles use `word` above `rate` per thousand, the inverted corpus scan.

    A high peer maximum means the pathology sits in another article, and the
    per-article test then excuses everyone. This names the carriers.
    """
    w = word.lower()
    out = []
    for p in paths:
        t = open(p, encoding="utf-8").read()
        ws = [x.lower() for x in words(t)]
        k = ws.count(w)
        if ws and k >= min_count and 1000.0 * k / len(ws) >= rate:
            out.append((1000.0 * k / len(ws), k, p))
    return sorted(out, reverse=True)


def series(paths, corpus_paths, min_articles=25, min_ratio=2.0, vocabulary=None):
    """Words the series as a whole overuses against the rest of the corpus.

    A tic shared by every sibling is invisible to a per-article peer maximum when
    the siblings are among the peers. The series is pooled and compared with the
    corpus outside it. The corpus count is smoothed by one half, so a word the
    corpus never uses does not divide by zero, and a word must appear in at least
    `min_articles` series articles, so one article's subject cannot dominate.
    """
    def pool(ps):
        c, n, df = collections.Counter(), 0, collections.Counter()
        for p in ps:
            ws = [x.lower() for x in words(open(p, encoding="utf-8").read())]
            c.update(ws)
            n += len(ws)
            df.update(set(ws))
        return c, n, df
    inside = set(map(os.path.abspath, paths))
    sc, sn, sdf = pool(paths)
    cc, cn, _ = pool([p for p in corpus_paths if os.path.abspath(p) not in inside])
    if not sn or not cn:
        return []
    rows = []
    for w, k in sc.items():
        if vocabulary is not None and w not in vocabulary:
            continue
        if sdf[w] < min_articles or w in STOP:
            continue
        ratio = (k / sn) / ((cc.get(w, 0) + 0.5) / cn)
        if ratio >= min_ratio:
            rows.append((ratio, w, k, 1000.0 * k / sn, 1000.0 * cc.get(w, 0) / cn, sdf[w]))
    return sorted(rows, reverse=True)


def kwic(text, pattern, width=60):
    """(line number, context) for every case-insensitive match in the file."""
    out = []
    for i, line in enumerate(text.split("\n"), 1):
        for m in re.finditer(pattern, line, re.I):
            out.append((i, line[max(0, m.start() - width):m.end() + width]))
    return out


def section(text, heading):
    """The text of the `## heading` section, for scoping a measurement to part of an article."""
    m = re.search(rf"(?ms)^##+ {re.escape(heading)}\s*$\n(.*?)(?=^## |\Z)", post.body(text))
    if not m:
        raise ValueError(f"no section headed {heading!r}")
    return m.group(1)


def _peers(path, peer_glob):
    """Peer texts. THE DEFAULT IS THE PUBLISHED CORPUS, not the article's directory.

    The old default took the article's own directory, which for a draft is
    `_drafts/` and compared it with other unfinished drafts (A377).
    """
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    pat = peer_glob or os.path.join(root, "_posts", "*.markdown")
    return [open(q, encoding="utf-8").read() for q in sorted(_glob.glob(pat))
            if os.path.abspath(q) != os.path.abspath(path)]


def _ratio(r):
    return "never" if r is None else f"{r:.2f}"


def _main(argv):
    import argparse
    ap = argparse.ArgumentParser(prog="diction.py", description="Word and phrase usage against the author's corpus.")
    sub = ap.add_subparsers(dest="cmd", required=True)

    def add(name, help_, peers=True, path=True):
        p = sub.add_parser(name, help=help_)
        if path:
            p.add_argument("path")
        if peers:
            p.add_argument("--peers", help="peer glob, default _posts/*.markdown")
        p.add_argument("--section", help="measure only the section with this heading")
        return p
    add("all", "every instrument below, in one report")
    add("report", "the enumerated constructions against peers")
    add("outliers", "words above the peer maximum")
    add("tics", "the enumerated tic class against peers")
    add("formulas", "discovered 2 to 4 word sequences above the peer maximum")
    add("openers", "sentence openings above the peer maximum")
    add("shapes", "construction shapes with a variable slot")
    add("leads", "phrasings that introduce many display equations", peers=False)
    add("repeats", "sentences repeating one content word", peers=False)
    add("acronyms", "first use of each acronym and whether it is spelled out nearby", peers=False)
    p = add("collocate", "evidence for whether a word names a term or is a tic", peers=False)
    p.add_argument("word")
    p = sub.add_parser("creep", help="sequences that rose across an edit pass")
    p.add_argument("before")
    p.add_argument("after")
    p = sub.add_parser("carriers", help="articles carrying a word above a rate")
    p.add_argument("word")
    p.add_argument("--glob", default="_posts/*.markdown")
    p.add_argument("--rate", type=float, default=5.0)
    p = sub.add_parser("series", help="words a set of articles overuses against the rest of the corpus")
    p.add_argument("glob")
    p.add_argument("--corpus", default="_posts/*.markdown")
    p.add_argument("--min-articles", type=int, default=25)
    p = sub.add_parser("kwic", help="every match with its line number")
    p.add_argument("path")
    p.add_argument("pattern")
    a = ap.parse_args(argv[1:])

    if a.cmd == "creep":
        rows, counters = creep(open(a.before, encoding="utf-8").read(), open(a.after, encoding="utf-8").read())
        print(f"  {'sequence':40s}{'before':>8}{'after':>7}")
        for g, b, k in rows[:60]:
            print(f"  {g:40s}{b:8d}{k:7d}")
        print("  substitution counters")
        for c, b, k in counters:
            print(f"  {c!r:40s}{b:8d}{k:7d}{'  <== ROSE' if k > b else ''}")
        return 0
    if a.cmd == "carriers":
        for r, k, p in carriers(a.word, sorted(_glob.glob(a.glob)), a.rate):
            print(f"  {r:6.2f}/1k {k:4d}  {p}")
        return 0
    if a.cmd == "series":
        rows = series(sorted(_glob.glob(a.glob)), sorted(_glob.glob(a.corpus)), a.min_articles)
        print(f"  {'word':20s}{'ratio':>7}{'n':>6}{'series':>8}{'corpus':>8}{'articles':>9}")
        for ratio, w, k, sr, cr, df in rows[:60]:
            print(f"  {w:20s}{ratio:7.2f}{k:6d}{sr:8.2f}{cr:8.2f}{df:9d}")
        return 0
    if a.cmd == "kwic":
        for ln, ctx in kwic(open(a.path, encoding="utf-8").read(), a.pattern):
            print(f"  {ln:5d}: {ctx}")
        return 0

    full = open(a.path, encoding="utf-8").read()
    text = full if not a.section else "---\n---\n" + section(full, a.section)
    if a.cmd == "collocate":
        collocation_report(a.path, a.word)
        return 0
    peers = _peers(a.path, getattr(a, "peers", None)) if hasattr(a, "peers") else []
    cmds = ["report", "outliers", "tics", "formulas", "openers", "shapes", "leads", "repeats",
            "acronyms"] if a.cmd == "all" else [a.cmd]
    print(f"{os.path.basename(a.path)}: {len(words(text)):,} author prose words"
          + (f", section {a.section!r}" if a.section else "") + (f", {len(peers)} peers" if peers else ""))
    for cmd in cmds:
        print(f"\n== {cmd} ==")
        if cmd == "report":
            rows, _n, _np = compare(text, [], PHRASES) if not peers else _compare_texts(text, peers)
            for ph, k, per_k, med, mx, verdict in rows:
                if verdict != "ok":
                    print(f"  {ph:18s} {k:4d} {per_k:6.2f}  {verdict}")
        elif cmd in ("outliers", "tics"):
            rows, _pn = word_outliers(text, peers, vocabulary=TICS if cmd == "tics" else None,
                                      min_count=1 if cmd == "tics" else 6)
            for ratio, w, k, rate, med, mx, used in rows:
                if ratio is not None and ratio <= 1.0:
                    continue
                print(f"  {w:22s}{k:5d}{rate:8.2f}{med:9.2f}{mx:9.2f}{_ratio(ratio):>8}  {used:3d}")
        elif cmd == "formulas":
            rows, _pn = phrase_outliers(text, peers)
            for ratio, g, k, rate, mx in rows:
                if ratio is None or ratio > 1.0:
                    print(f"  {g:44s}{k:4d}{rate:7.2f}{mx:9.2f}{_ratio(ratio):>8}")
        elif cmd == "openers":
            rows, _pn = openers(text, peers)
            for ratio, g, k, rate, mx in rows:
                if ratio is None or ratio > 1.0:
                    print(f"  {g:30s}{k:4d}{rate:7.2f}/100 sentences  peer max {mx:6.2f}  {_ratio(ratio)}")
        elif cmd == "shapes":
            rows, _n = shapes(text, peers)
            for name, k, rate, mx in rows:
                if k:
                    flag = "  <== OVER PEER MAX" if rate > mx else ""
                    print(f"  {name:34s}{k:4d}{rate:7.2f}{mx:9.2f}{flag}")
        elif cmd == "leads":
            for g, k, total in display_lead_ins(text):
                print(f"  {g:40s}{k:4d} of {total} display lead-ins")
        elif cmd == "repeats":
            for hits, sent in sentence_repeats(text):
                print(f"  {hits}  {sent}")
        elif cmd == "acronyms":
            for acro, _pos, spelled in acronyms(text):
                if not spelled:
                    print(f"  {acro:8s} not spelled out near its first use")
    print("\nA FINDING IS A READING LIST, NOT A VERDICT. Subject matter dominates every relative "
          "measure; check `collocate` and `kwic` before editing, and `creep` after.")
    return 0


def _compare_texts(text, peer_texts, patterns=PHRASES):
    """`compare` for texts already read, which the command line uses with `--section`."""
    acc = collections.defaultdict(list)
    for t in peer_texts:
        r, _ = rates(t, patterns)
        for ph, (_, per_k) in r.items():
            acc[ph].append(per_k)
    base = {ph: {"median": statistics.median(v), "max": max(v)} for ph, v in acc.items() if v}
    mine, n = rates(text, patterns)
    rows = []
    for ph, (k, per_k) in mine.items():
        b = base.get(ph)
        verdict = ("no-baseline" if not b else "over-max" if per_k > b["max"]
                   else "over-median" if per_k > b["median"] else "ok")
        rows.append((ph, k, per_k, b and b["median"], b and b["max"], verdict))
    return rows, n, len(peer_texts)


if __name__ == "__main__":
    sys.exit(_main(sys.argv))
