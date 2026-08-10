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


def clean(s):
    """Strip what the prose rules forbid from anything that becomes link text."""
    s = re.sub(r"<[^>]+>", " ", s or "").replace("&amp;", "and")
    s = re.sub(r"[():;\[\]{}]", " ", s)
    s = s.replace("—", " ").replace("–", " ").replace("−", "-")
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
    a = [x for x in (authors or []) if x]
    if not a:
        base = clean(" ".join((title or "").split()[:4]))
    elif len(a) == 1:
        base = a[0].title() if a[0].isupper() else a[0]
    elif len(a) == 2:
        x = a[0].title() if a[0].isupper() else a[0]
        y = a[1].title() if a[1].isupper() else a[1]
        base = f"{x} and {y}"
    else:
        x = a[0].title() if a[0].isupper() else a[0]
        base = f"{x} et al"
    out = f"{base} {year}" if year else base
    if disambiguate:
        out += ", " + clean(title)[:33]
    return clean(out)


def anchor_stem(authors, year, title, kind="research"):
    a = [x for x in (authors or []) if x]
    if not a:
        stem = slug(" ".join((title or "").split()[:2])) or "anon"
    elif len(a) >= 2:
        stem = f"{fold(a[0])}_{fold(a[1])}"
    else:
        stem = fold(a[0])
    stem = stem or "anon"
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
