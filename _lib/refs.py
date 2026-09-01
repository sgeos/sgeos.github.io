#!/usr/bin/env python3
"""Reference anchors, link text and the categorised definition block.

WHY. Nineteen `gen_refs.py` and seventeen `gen_master.py` copies re-derive this,
and the corpus has paid for several of the fixes more than once.

DEFECTS THIS ENCODES, each of which shipped.

  MID-WORD TRUNCATION. A322 emitted link text cut in the middle of a word.
  `shorten` cuts at a word boundary and never inside a token.

  NINETY-FIVE DUPLICATE SAME-TITLE RECORDS. A322 cited one paper repeatedly
  under different identifiers because publishers register the same work several
  times. `dedupe` keys on normalised title AND year, before anchors are
  assigned, so two identifiers for one paper cannot both be cited.

  UNCATEGORISED REFERENCE BLOCK. A369 shipped 111 definitions under a single
  `### Reference` heading although 109 were `research_` anchors. `emit_blocks`
  groups by anchor prefix and sorts within each group, which is what
  `_verify.py` checks.

  PROSE PUNCTUATION IN LINK TEXT. Titles carry colons, semicolons, brackets and
  dashes that the style rules forbid in prose. `clean` removes them.

TWO LINK-TEXT STYLES EXIST IN THIS CORPUS AND BOTH ARE SUPPORTED. The X-Planes
articles cite as `Author and Author 1958`, built by `display`. A369 cites survey
clusters by shortened title, built by `shorten`. Neither is the house style;
they suit different jobs, since an author-year label is unreadable when four
hundred of them sit in one paragraph.
"""

import os
import html
import re
import sys
import unicodedata

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import post  # noqa: E402

PREFIX_TO_HEADING = {
    "book": "Books",
    "ref": "Reference",
    "related": "Related Post",
    "research": "Research",
}


def fold(s):
    """ASCII-folded, punctuation-free key. Diacritics fold rather than vanish.

    Naive stripping turns `Slavík` into `slavk` through the dotless i and
    `Böhm` into `bhm`, which produced three false author mismatches in an A369
    verification run and read as citation defects until the folding was fixed.
    """
    s = unicodedata.normalize("NFKD", s or "")
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = (s.replace("ı", "i").replace("ø", "o").replace("đ", "d")
           .replace("ł", "l").replace("ß", "ss").replace("æ", "ae").replace("œ", "oe"))
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "", s.lower())


def slug(s):
    s = unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "_", s.lower()).strip("_")


def title_lead(s):
    """Strip leading enumeration artefacts from a title used as a LABEL, not as a title.

    ABSTRACTING SERVICES AND PATENT REGISTRIES PREFIX THEIR OWN ACCESSION NUMBER TO THE
    TITLE FIELD, and Crossref passes it through. Where a record also carries no
    Latin-script author, the label falls back to the first words of the title and the
    accession number becomes the reader-visible link text. A339 harvested 33 of these in
    one pool, producing labels reading "98/02419 Effects of launch 1998", "5451015
    Crashworthy composite aircraft 1996" and "1162. Design of altitude 1968".

    THIS IS DELIBERATELY NOT PART OF `clean`. A title is entitled to begin with a number
    and the full reference text should keep it. Only the shortened LABEL needs the prefix
    removed, so only the label paths call this.

    A number glued to a following capital, as in "85Chapter" and "13Design", is the same
    artefact with the separating space lost, and is split rather than dropped so no word
    is destroyed.
    """
    s = (s or "").strip()
    s = s.lstrip("\"'‘’“”«»")
    # "98/02419 ", "1162. ", "4 " but never "3D printing", which has no space to consume.
    s = re.sub(r"^\d+(?:[/.-]\d+)*\.?\s+", "", s)
    # "85Chapter" -> "Chapter", but "3D printing" keeps its digit. Requiring a LOWERCASE
    # letter after the capital is what separates a glued word from a leading initialism,
    # and the first version of this rule turned "3D printing" into "D printing".
    s = re.sub(r"^\d+(?=[A-Z][a-z])", "", s)
    return s.strip()


# Function words stay lowercase inside a title; anything else that is a short
# all-capitals run is treated as an initialism and preserved.
_TITLE_STOPWORDS = {
    "a", "an", "and", "as", "at", "by", "for", "from", "in", "into", "of", "on",
    "onto", "or", "over", "the", "to", "with", "within", "without", "versus", "vs",
}


def decap(s, threshold=0.6):
    """Normalise a SHOUTED title, preserving initialisms.

    A PUBLISHER SHOUTING ITS OWN TITLE BECOMES SHOUTED LINK TEXT, and `display`
    already fixed this for AUTHOR names while leaving the no-author branch, which
    falls back to the first words of the title, untouched. The 2026-08-14 audit
    normalised 3,564 citation titles out of all capitals across 26 articles BY
    HAND, and A342 then harvested four more, because a sweep repairs the corpus
    once while the defect is reintroduced by the next harvest. This is the same
    argument that moved the en-dash normalisation into `gate.py`: a per-article or
    per-sweep fix has already failed, so the fix belongs where the text is built.

    ONLY A PREDOMINANTLY UPPERCASE STRING IS TOUCHED. Deciding word by word cannot
    work, because `IFAC` and `ON` are the same length and only one of them is an
    initialism. Deciding on the whole string first means `Volume 5: OGC CDB Radar
    Cross Section (RCS) Models` is left exactly as its publisher set it, since it
    is ordinary title case that happens to contain three initialisms.

    Within a shouted string a run of at most four capitals is kept as an
    initialism unless it is a function word, so `2nd IFAC CONFERENCE ON
    INTELLIGENT AUTONOMOUS VEHICLES` becomes `2nd IFAC Conference on Intelligent
    Autonomous Vehicles`. The threshold is a ratio of cased characters and not a
    count, because a long title needs no more evidence than a short one.
    """
    s = s or ""
    letters = [c for c in s if c.isalpha()]
    if not letters:
        return s
    if sum(1 for c in letters if c.isupper()) / len(letters) < threshold:
        return s
    out, first = [], True
    for tok in re.split(r"(\s+)", s):
        if not tok.strip():
            out.append(tok)
            continue
        core = tok.strip("([{)]}.,;:!?\"'")
        low = core.lower()
        if core.isupper() and len(core) <= 4 and low not in _TITLE_STOPWORDS:
            out.append(tok)                      # NASA, IFAC, RCS, OGC
        elif low in _TITLE_STOPWORDS and not first:
            out.append(tok.lower())
        else:
            out.append(tok.title() if tok.isupper() else tok)
        first = False
    return "".join(out)


def clean(s):
    """Strip what the prose rules forbid from anything that becomes link text."""
    # AN UNDECODED HTML ENTITY IS TURNED INTO VISIBLE JUNK BY THE PUNCTUATION RULE BELOW,
    # AND THIS SHIPPED IN THREE CONSECUTIVE DRAFTS BEFORE ANYONE READ THE REFERENCE LIST.
    # Publishers emit titles wrapped in `&lt;title&gt;` rather than in a literal tag, so the
    # tag-stripping regex on the next line never sees them. The later rule that removes
    # semicolons then converts `&lt;title&gt;` into `&lt title&gt`, which renders as exactly
    # that. Decoding entities FIRST turns them back into real tags, which the next line
    # removes, and is the only ordering in which both rules are correct.
    # DOUBLE-ESCAPED MARKUP SURVIVES A SINGLE UNESCAPE PASS AND THE LATER RULES THEN MANGLE
    # IT INTO VISIBLE JUNK. A publisher emitting `&lt;p&gt;&amp;nbsp;` decodes once to
    # `<p>&nbsp;`, so the tag rule removes the paragraph tag and the surviving literal
    # `&nbsp;` meets the ampersand rule, which turns it into `andnbsp;`, and the semicolon
    # rule then strips the terminator. A332 shipped link text reading `andnbsp andnbsp
    # andnbsp`. Unescaping to a FIXED POINT is the only ordering in which every later rule
    # sees text rather than markup, and the iteration is bounded because a hostile title
    # could otherwise be made to expand.
    s = s or ""
    for _ in range(4):
        once = html.unescape(s)
        if once == s:
            break
        s = once
    # TYPOGRAPHIC PUNCTUATION MUST BECOME ITS ASCII EQUIVALENT BEFORE ANY OTHER RULE RUNS,
    # AND THE REASON IS A HOLE RATHER THAN AN UNTIDINESS. The corpus contraction check
    # matches an ASCII apostrophe, so a harvested title reading "What's" with a RIGHT
    # SINGLE QUOTATION MARK sails straight past it. A332 shipped exactly that until a
    # character survey found it. Normalising here means one rule catches both spellings.
    # The SOFT HYPHEN is invisible and breaks word matching wherever it lands, and a
    # STANDALONE COMBINING MARK is harvest residue that attaches itself to whatever
    # character happens to precede it.
    s = unicodedata.normalize("NFC", s)
    for src, dst in (("‘", "'"), ("’", "'"), ("‚", "'"), ("‛", "'"),
                     ("“", '"'), ("”", '"'), ("„", '"'), ("′", "'"),
                     ("‐", "-"), ("‑", "-"), ("‒", "-"), ("⁃", "-"),
                     ("…", "..."), (" ", " "), (" ", " "), (" ", " ")):
        s = s.replace(src, dst)
    s = s.replace("­", "")
    s = re.sub(r"(?<![^\W\d_])[̀-ͯ᪰-᫿⃐-⃰]", "", s)
    s = re.sub(r"<[^>]+>", " ", s).replace("&amp;", "and").replace("&", "and")
    # LATEX IN A TITLE BREAKS THE PAGE, NOT JUST THE PROSE. Publishers emit titles
    # containing inline math, and a stray `$$` in link text opens a MathJax display block
    # that swallows everything after it. A327 hit this with a Springer title reading
    # "Al/MLG/CuO/$${\text{Bi}}_{2}{\text{O}}_{3}$$ Nanothermite", whose truncated form
    # left a single unbalanced `$$` and tripped the math-delimiter check. Strip the command
    # sequences first, then the dollars, and let the existing brace rule take the rest.
    s = re.sub(r"\\[a-zA-Z]+", " ", s)
    s = s.replace("$", " ")
    # A BARE ANGLE BRACKET IS MARKUP AND NOT PROSE. The tag rule above only removes a
    # MATCHED pair, so a title reading "Precision >> Accuracy" keeps both characters, and a
    # `>` that reflow happens to place at the start of a line is a blockquote. A331 found
    # one sitting mid-line by luck rather than by design.
    s = re.sub(r"[():;\[\]{}<>]", " ", s)
    # `\(` AND `\[` ARE MATHJAX DELIMITERS TOO AND THE COMMAND RULE DOES NOT REACH THEM,
    # because the character after the backslash is punctuation rather than a letter. A328
    # harvested a title reading "\({\mathcal{L}_1}\) Adaptive Loss Fault Tolerance
    # Control", and stripping `\mathcal` and the braces left BARE BACKSLASHES in the link
    # text. An unbalanced `\(` opens an inline math block exactly as an unbalanced `$$`
    # opens a display one, which is the A327 defect arriving through a different delimiter.
    # Any backslash surviving this far is residue and is removed.
    s = s.replace("\\", " ")
    # A BARE PIPE IN LINK TEXT IS A KRAMDOWN TABLE. This is the same family as the
    # unbalanced `$$`, the bare `\(` and the stray `>`, and it is the one delimiter the
    # rules above did not reach. kramdown reads a paragraph whose first line contains a
    # pipe as a table, so a pipe that reflow happens to place at the start of a line
    # shreds the surrounding text into cells. A334 harvested a title deposited as
    # "Influence of Small Satellites^|^apos; Post-mission Disposal", in which a publisher
    # had mangled an apostrophe entity into a sequence carrying a literal pipe, and the
    # semicolon rule then stripped the terminator and left the pipe sitting in link text.
    # `_verify.py` already warns on this as `math-pipe-table` when it reaches inline math.
    s = s.replace("|", " ")
    # AN EM OR EN DASH IS TWO DIFFERENT PUNCTUATION MARKS AND COLLAPSING BOTH TO A SPACE
    # CORRUPTS ONE OF THEM. Used with spaces around it, a dash is parenthetical and a space
    # is the right replacement. Used directly between two word characters it is a COMPOUND
    # JOINER, and a space there both destroys the term and can MANUFACTURE A DOUBLED WORD.
    # A332 harvested "Applications of jet-jet/film impingement", written with an en dash,
    # and the old rule turned it into "jet jet", which the corpus doubled-word check then
    # reported against a title that never contained one. A hyphen is permitted in prose,
    # so the joining case becomes a hyphen and only the parenthetical case becomes a space.
    s = re.sub(r"(?<=\w)[—–](?=\w)", "-", s)
    s = s.replace("—", " ").replace("–", " ").replace("−", "-")
    # A REPEATED COMMA IS A REGISTRY ARTEFACT, NOT PUNCTUATION THE TITLE CARRIES. One harvested
    # title reached a draft reading "Col, Demler of A, E, C, , Washington", where an abbreviation
    # full stop had already become a comma and the empty field between two of them rendered as
    # `, ,`. Collapsing the run is safe because no title legitimately carries one.
    s = re.sub(r",\s*(?:,\s*)+", ", ", s)
    s = re.sub(r"\s+,", ",", s)
    return re.sub(r"\s+", " ", s).strip(" ,.-")

def shorten(title, limit=58):
    """Word-boundary truncation. THE A322 DEFECT WAS CUTTING MID-WORD."""
    t = clean(title)
    if len(t) <= limit:
        return t
    cut = t[:limit]
    sp = cut.rfind(" ")
    if sp < 20:
        return cut.rstrip() + "..."
    return cut[:sp].rstrip(" ,.-") + "..."


def display(authors, year, title, disambiguate=False):
    """Author-year link text, the X-Planes convention."""
    a = latin_authors(authors)
    if not a:
        # DECAP ON THE WHOLE TITLE AND NOT ON THE FRAGMENT. The uppercase ratio is
        # the evidence, and four words carry less of it than the full title does.
        base = clean(" ".join(title_lead(decap(title)).split()[:4]))
    elif len(a) == 1:
        base = a[0].title() if a[0].isupper() else a[0]
    elif len(a) == 2:
        x = a[0].title() if a[0].isupper() else a[0]
        y = a[1].title() if a[1].isupper() else a[1]
        base = f"{x} and {y}"
    else:
        x = a[0].title() if a[0].isupper() else a[0]
        base = f"{x} et al"
    # A TITLE THAT ALREADY ENDS IN ITS OWN YEAR MUST NOT HAVE IT APPENDED AGAIN.
    # Standards and reference documents are titled that way as a matter of course,
    # so the no-author branch produced `U.S. Standard Atmosphere, 1976 1976`. A341
    # carried the same source and did not show this only because it was readmitted
    # and labelled by hand, which is a repair that does not survive to the next
    # article.
    if year and re.search(rf"\b{re.escape(str(year))}$", base.strip()):
        out = base
    else:
        out = f"{base} {year}" if year else base
    if disambiguate:
        out += ", " + clean(decap(title))[:33]
    return clean(out)


def latin_authors(authors):
    """Authors whose names survive ASCII folding, in order.

    A NAME IN A NON-LATIN SCRIPT FOLDS TO THE EMPTY STRING AND THAT PRODUCED BROKEN
    ANCHORS AND USELESS LINK TEXT. A328 harvested thirteen records with Chinese, Russian
    and Ukrainian author names and got anchors reading `research___2023`, because the
    stem was built as `fold(a) + "_" + fold(b)` and both folded away, leaving a bare
    separator that the `or "anon"` guard did not catch because a lone underscore is
    truthy. The link text was worse, rendering as a bare surname in a script the rest of
    the page does not use, and in one case as nothing but a year.

    Crossref frequently supplies BOTH forms of the same name, so preferring the folding
    ones recovers the record rather than discarding it."""
    return [x for x in (authors or []) if x and fold(x)]


def anchor_stem(authors, year, title, kind="research"):
    a = latin_authors(authors) or [x for x in (authors or []) if x]
    # THE TITLE FALLBACK MUST GO THROUGH `clean` AND NOT STRAIGHT INTO `slug`. A publisher
    # title wrapped in `&lt;title&gt;` otherwise produces an anchor reading
    # `research_lt_title_gt_..._1998`, in which every meaningful word has been pushed past
    # the two-word window by markup. `clean` removes the markup first, so the window lands
    # on the title.
    title = clean(title)
    if not a:
        stem = slug(" ".join(title_lead(title).split()[:2])) or "anon"
    elif len(a) >= 2:
        stem = f"{fold(a[0])}_{fold(a[1])}"
    else:
        stem = fold(a[0])
    # A STEM OF NOTHING BUT SEPARATORS IS EMPTY AND THE OLD GUARD MISSED IT.
    if not stem.strip("_"):
        stem = slug(" ".join(title_lead(title).split()[:3])) or "anon"
    return f"{kind}_{stem}_{year}" if year else f"{kind}_{stem}"


def title_key(title, year):
    return (fold(title)[:70], str(year or ""))


def dedupe(records, key=title_key):
    """Drop repeat registrations of one work. Returns (kept, dropped).

    Publishers register the same paper under several identifiers, so a naive
    harvest cites one work many times. A322 shipped 95 such duplicates.
    """
    seen, kept, dropped = {}, [], []
    for r in records:
        k = key(r.get("title", ""), r.get("year"))
        if k in seen:
            dropped.append(r)
            continue
        seen[k] = True
        kept.append(r)
    return kept, dropped


def assign_anchors(records, taken=(), kind="research"):
    """Unique anchor per record. Returns {anchor: record}, never colliding."""
    used = set(taken)
    out = {}
    for r in records:
        base = anchor_stem(r.get("authors"), r.get("year"), r.get("title", ""), kind)
        anc, n = base, 1
        while anc in used:
            n += 1
            anc = f"{base}_{chr(96 + n)}" if n <= 26 else f"{base}_{n}"
        used.add(anc)
        out[anc] = r
    return out


def emit_blocks(definitions, texts=None):
    """Categorised `## References` block from {anchor: url}.

    A LINK DEFINITION IS INVISIBLE. `[anchor]: url` renders as nothing at all,
    so a block containing only definitions produces a heading with empty
    subheadings and no references. That shipped in the published A369, which
    served 1,765 definitions under four empty headings, and it is latent in
    seventeen of the twenty-seven X-Planes drafts.

    The corpus convention is a VISIBLE bulleted list of `- [text][anchor]`
    followed by the definitions, and `texts` supplies the display text. Passing
    no `texts` still emits definitions alone, which is what the defect looked
    like, so callers that want a rendered section must supply it.

    Definitions stay sorted by anchor within each group, which is what the
    `anchor-order` check in `_verify.py` enforces. Bullets sort by display text,
    since that is the order a reader scans.
    """
    groups = {}
    for anc, url in definitions.items():
        head = PREFIX_TO_HEADING.get(anc.split("_")[0], anc.split("_")[0].title())
        groups.setdefault(head, []).append((anc, url))
    out = ["## References", ""]
    for head in sorted(groups):
        out.append(f"### {head}")
        out.append("")
        if texts:
            for anc, _url in sorted(groups[head], key=lambda p: (texts.get(p[0], p[0]).lower(), p[0])):
                out.append(f"- [{texts.get(anc, anc)}][{anc}]")
            out.append("")
        for anc, url in sorted(groups[head]):
            out.append(f"[{anc}]: {url}")
        out.append("")
    return "\n".join(out).rstrip("\n") + "\n"


def replace_block(text, definitions):
    """Swap a post's reference block for a freshly emitted one."""
    front, body_text, _refs = post.split(text)
    return front + body_text + emit_blocks(definitions)


def integrity(text):
    """Used, defined, undefined and orphaned anchors, plus duplicate URLs."""
    _front, body_text, refs_block = post.split(text)
    used = set(post.USE.findall(body_text))
    defs = post.DEF_LINE.findall(refs_block)
    defined = {a for a, _ in defs}
    urls = {}
    for a, u in defs:
        urls.setdefault(u.strip(), []).append(a)
    return {"used": len(used), "defined": len(defined),
            "undefined": sorted(used - defined), "orphaned": sorted(defined - used),
            "duplicate_urls": {u: a for u, a in urls.items() if len(a) > 1}}

def parse_anchor(anchor):
    """Read (kind, surname, year) back out of an anchor. Inverse of anchor_stem.

    ONE PARSER, DELIBERATELY. `audit` and `citations` each grew their own and
    they disagreed: a year written as `1978b`, with no separator before the
    disambiguator, parsed in one and silently returned None in the other, so a
    year check was skipped without any signal. Both now call this.

    Handles `_1997`, `_1978b` and `_2023_b`.
    """
    m = re.match(r"([a-z]+)_(.+)$", anchor or "")
    if not m:
        return None, None, None
    kind, rest = m.group(1), m.group(2)
    ym = re.search(r"_(\d{4})[a-z]?(?:_[a-z0-9]+)?$", "_" + rest)
    year = int(ym.group(1)) if ym else None
    sm = re.match(r"([a-z]+)", rest)
    return kind, (sm.group(1) if sm else None), year
