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
    c = collections.Counter(" ".join(w[i:i + size]) for i in range(len(w) - size))
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


def word_rates(text, vocabulary=None):
    """Occurrences per thousand author prose words, for each word in a vocabulary."""
    ws = words(prose(text))
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
    ws = words(prose(text))
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
    n = len(words(prose(text)))
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


def _main(argv):
    if len(argv) >= 3 and argv[1] == "collocate":
        word = argv[2]
        paths = argv[3:]
        if not paths:
            print("usage: python3 _lib/diction.py collocate <word> <path>...")
            return 2
        for path in paths:
            collocation_report(path, word)
            print()
        return 0
    if len(argv) >= 3 and argv[1] == "report":
        report(argv[2], argv[3] if len(argv) > 3 else None)
        return 0
    if len(argv) >= 3 and argv[1] in ("outliers", "tics"):
        path = argv[2]
        peer_glob = argv[3] if len(argv) > 3 else os.path.join(
            os.path.dirname(os.path.abspath(path)) or ".", "*.markdown")
        peers = [open(q, encoding="utf-8").read()
                 for q in _glob.glob(peer_glob)
                 if os.path.abspath(q) != os.path.abspath(path)]
        text = open(path, encoding="utf-8").read()
        vocab = TICS if argv[1] == "tics" else None
        rows, peer_n = word_outliers(text, peers, vocabulary=vocab,
                                     min_count=1 if argv[1] == "tics" else 6)
        n = len(words(prose(text)))
        print(f"{os.path.basename(path)}: {n:,} author prose words against {peer_n} peers")
        if argv[1] == "tics":
            print("  the tic class is enumerated, not discovered, because a relative check "
                  "cannot separate a tic from a subject")
        print(f"  {'word':22s}{'n':>5}{'rate':>8}{'median':>9}{'peermax':>9}{'x max':>8}  peers")
        shown = 0
        for ratio, w, k, rate, med, mx, used in rows:
            over = ratio is None or ratio > 1.0
            if not over and shown >= 25:
                break
            shown += 1
            rr = "never" if ratio is None else f"{ratio:.2f}"
            flag = "  <== OVER PEER MAX" if over else ""
            print(f"  {w:22s}{k:5d}{rate:8.2f}{med:9.2f}{mx:9.2f}{rr:>8}  {used:3d}{flag}")
        over_n = sum(1 for r in rows if r[0] is None or r[0] > 1.0)
        print(f"  {over_n} word(s) at or above the peer maximum")
        print("  A WORD ABOVE THE PEER MAXIMUM IS USUALLY THE SUBJECT, NOT A TIC. Check the "
              "collocations before acting:")
        print("    python3 _lib/diction.py collocate <word> <path>")
        return 0
    print("usage:\n"
          "  python3 _lib/diction.py collocate <word> <path>...     evidence for one word\n"
          "  python3 _lib/diction.py report <path> [peer-glob]      constructions vs peers\n"
          "  python3 _lib/diction.py outliers <path> [peer-glob]    words above the peer max\n"
          "  python3 _lib/diction.py tics <path> [peer-glob]        the enumerated tic class")
    return 2


if __name__ == "__main__":
    sys.exit(_main(sys.argv))
