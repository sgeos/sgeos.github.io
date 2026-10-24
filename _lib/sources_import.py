#!/usr/bin/env python3
"""Draft source records from registry metadata, for review before they enter the database.

WHAT THIS DOES NOT DECIDE. It proposes a record. It does not decide whether a
journal article is a review, whether a publisher has a stake in its subject, or
whether a venue referees full papers, because no registry answers those. The
caller records those decisions on the record or in `_sources/venues.jsonl`, and
`sources.validate` refuses a record whose recorded section the rules do not
reproduce.

HEADLINE CASE IS A PROPOSAL. Registries mostly store titles in sentence case,
and Chicago wants headline case. `headline_case` capitalises what is lower case
and leaves alone anything already carrying a capital or a digit, so it cannot
damage an acronym or a proper noun, but it cannot know that `km` is a unit or
that `up` is an adverb. Every proposed title is reviewed by a person.
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sources  # noqa: E402

# Chicago lowercases articles, coordinating conjunctions, `to`, `as`, and
# prepositions regardless of length, except as the first or last word of a
# title or subtitle.
MINOR = set("""
a an the and but for or nor as to
about above across after against along amid among around at before behind below beneath beside
between beyond by down during except from in inside into like near of off on onto out outside over
past per since than through throughout till toward towards under underneath until unto up upon via
versus vs with within without
""".split())


def _case_part(part, force):
    """One hyphen-separated part. Existing capitals and digits are never removed."""
    lead = re.match(r"^[^\w]*", part).group(0)
    rest = part[len(lead):]
    bare = re.sub(r"[^\w'\u2019]+$", "", rest)
    # A minor word the registry capitalised, as in "Has A Solid", is lowered.
    # Only the plain capitalised form is touched, so an acronym is never lowered.
    if not force and bare.lower() in MINOR and bare == bare[:1].upper() + bare[1:].lower():
        return lead + rest.lower()
    if not rest or rest[:1].isupper() or re.search(r"[A-Z0-9]", rest):
        return part
    if bare.lower() in MINOR and not force:
        return lead + rest.lower()
    return lead + rest[:1].upper() + rest[1:]


def _case_word(word, force):
    """Chicago 8.161 for compounds. The first part follows the word's position,
    later parts are capitalised unless they are minor words."""
    parts = word.split("-")
    return "-".join(_case_part(p, force if i == 0 else False) for i, p in enumerate(parts))


def normalise_title(title):
    """Registry punctuation repaired before casing. A typed spaced hyphen
    separating a subtitle becomes a colon, and a trailing period is dropped,
    since the entry supplies its own. House rules, see CITATION_STYLE.md."""
    title = re.sub(r"\s+-\s+", ": ", title.strip())
    return re.sub(r"(?<![A-Z])\.$", "", title)


def headline_case(title):
    """A proposed Chicago headline-case title. Review every result."""
    title = normalise_title(title)
    words = title.split(" ")
    if len(words) >= 3 and title.isupper():
        words = title.lower().split(" ")
    out = []
    for i, w in enumerate(words):
        first = i == 0 or words[i - 1].endswith((":", "?", "!", "\u2014"))
        last = i == len(words) - 1 or w.endswith(":")
        out.append(_case_word(w, first or last))
    return " ".join(out)


def _given(g):
    """Given names as printed, with Chicago's spaced initials, as in `A. J.`."""
    g = sources.clean_text(g)
    g = g.title() if g.isupper() and len(g) > 2 and "." not in g else g
    g = re.sub(r"\.(?=[A-Z])", ". ", g)
    return re.sub(r"\b([A-Z])(?=\s|$)", r"\1.", g)


def _family(f):
    """Family names as printed. A generational suffix takes no comma in the 18th edition."""
    f = sources.clean_text(f)
    f = f.title() if f.isupper() and len(f) > 3 else f
    return re.sub(r",\s*(Jr\.|Sr\.|II|III|IV)$", r" \1", f)


def _authors(people):
    out = []
    for p in people or []:
        if p.get("family"):
            a = {"family": _family(p["family"])}
            if p.get("given"):
                a["given"] = _given(p["given"])
            out.append(a)
        elif p.get("name"):
            out.append({"name": sources.clean_text(p["name"])})
    return out


def _strip_the(container):
    """Chicago drops an initial `The` from a periodical's name, as in *American Naturalist*."""
    return re.sub(r"^The\s+", "", container)


CROSSREF_KIND = {
    "journal-article": "journal-article",
    "proceedings-article": "proceedings-paper",
    "book-chapter": "chapter",
    "book": "book",
    "monograph": "book",
    "report": "report",
}


def record_from_crossref(anchor, msg):
    """A draft record from a Crossref `message`. Raises on a type with no mapping."""
    doi = msg["DOI"].lower()
    ctype = msg.get("type")
    kind = CROSSREF_KIND.get(ctype)
    number = None
    container = sources.clean_text(((msg.get("container-title") or [""]) or [""])[0])
    # EGU General Assembly abstracts are `posted-content` with no meeting name;
    # the DOI carries both the year and the abstract number.
    m = re.match(r"^10\.5194/egusphere-egu(\d\d)-(\d+)$", doi)
    if ctype == "posted-content" and m:
        kind = "abstract"
        number = f"EGU{m.group(1)}-{m.group(2)}"
        container = f"EGU General Assembly 20{m.group(1)}"
    elif ctype == "posted-content":
        kind = "preprint"
        container = sources.clean_text((msg.get("institution") or [{}])[0].get("name", "")) or container
    if not kind:
        raise sources.SourceError(f"{anchor}: Crossref type {ctype!r} has no mapping")
    m = re.match(r"^10\.2514/6\.(\d{4}-\d+)$", doi)
    if m:
        number = f"AIAA {m.group(1)}"
    issued = (msg.get("issued", {}) or {}).get("date-parts") or [[None]]
    rec = {
        "anchor": anchor,
        "kind": kind,
        "doi": doi,
        "title_published": sources.clean_text((msg.get("title") or [""])[0]),
        "authors": _authors(msg.get("author")),
        "year": (issued[0] or [None])[0],
        "publisher": sources.clean_text(msg.get("publisher", "")),
    }
    subtitle = sources.clean_text((msg.get("subtitle") or [""])[0])
    if subtitle and subtitle.lower() not in rec["title_published"].lower():
        rec["title_published"] += ": " + subtitle
    rec["title"] = headline_case(rec["title_published"])
    if kind == "journal-article":
        rec["container"] = _strip_the(container)
        rec["venue"] = rec["container"]
        for k_src, k_dst in (("volume", "volume"), ("issue", "issue")):
            if msg.get(k_src):
                rec[k_dst] = sources.clean_text(msg[k_src])
        if msg.get("page"):
            rec["pages"] = sources.clean_text(msg["page"])
        elif msg.get("article-number"):
            rec["pages"] = sources.clean_text(msg["article-number"])
        rec.pop("publisher")
    elif kind in ("proceedings-paper", "chapter", "abstract", "preprint"):
        rec["container"] = container
        if kind == "proceedings-paper":
            rec["venue"] = container
            if msg.get("volume"):
                rec["volume"] = sources.clean_text(msg["volume"])
        if msg.get("editor"):
            rec["editors"] = _authors(msg["editor"])
    if number:
        rec["number"] = number
    return rec


def record_from_wikipedia(anchor, page_title, oldid, timestamp):
    """A pinned Wikipedia record. `page_title` is the canonical title the API returned."""
    import urllib.parse
    q = urllib.parse.quote(page_title.replace(" ", "_"), safe="()_,'-")
    return {
        "anchor": anchor,
        "kind": "wikipedia",
        "title_published": page_title,
        "title": headline_case(page_title),
        "year": int(timestamp[:4]),
        "revision": {"oldid": oldid, "timestamp": timestamp},
        "url": f"https://en.wikipedia.org/w/index.php?title={q}&oldid={oldid}",
    }


def record_from_related_post(anchor, post_stem, locators=None):
    rec = {"anchor": anchor, "kind": "related-post", "post": post_stem}
    if locators:
        rec["locators"] = dict(sorted(locators.items()))
    return rec
