#!/usr/bin/env python3
"""Regression tests. Every case names the defect that actually shipped.

Run with `python3 _lib/test_lib.py`. No test framework, matching the
no-dependency discipline of `_verify.py`, which must run on a bare runner.

THE POINT OF THIS FILE. The survey that motivated the library found five
generator scripts warning about the doubled-backslash trap in their docstrings
and zero checking for it, while the bug shipped in three consecutive articles.
A lesson written as a comment is not a guard. Each test below is the executable
form of a comment that failed to prevent something.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import edits
import lint
import refs
import reflow

FM = ('---\nlayout: post\nmathjax: true\ncomments: true\ntitle: "T"\n'
      "date: 2026-08-06 09:00:00 +0000\ncategories: engineering\n---\n")

RESULTS = []


def check(name, fn):
    try:
        fn()
        RESULTS.append((True, name, ""))
    except AssertionError as e:
        RESULTS.append((False, name, str(e) or "assertion failed"))
    except Exception as e:
        RESULTS.append((False, name, f"{type(e).__name__}: {e}"))


# ---------------------------------------------------------------- refs

def t_shorten_word_boundary():
    """A322 shipped link text truncated in the middle of a word."""
    title = "Automatic generation of peephole superoptimizers for instruction selection"
    s = refs.shorten(title, 40)
    assert s.endswith("..."), s
    body = s[:-3].rstrip()
    assert title.startswith(body), s
    assert title[len(body)] in " ", f"cut mid-word: {s!r}"


def t_shorten_short_titles_untouched():
    assert refs.shorten("Short title", 40) == "Short title"


def t_dedupe_same_title_different_doi():
    """A322 shipped 95 duplicates: one paper registered under several identifiers."""
    recs = [{"title": "Stochastic superoptimization", "year": 2013, "doi": "10.1145/2499368"},
            {"title": "Stochastic Superoptimization", "year": 2013, "doi": "10.1145/2490301"},
            {"title": "Stochastic superoptimization", "year": 2013, "doi": "10.1145/2451116"},
            {"title": "A different paper", "year": 2013, "doi": "10.1/x"}]
    kept, dropped = refs.dedupe(recs)
    assert len(kept) == 2, [r["doi"] for r in kept]
    assert len(dropped) == 2


def t_fold_diacritics():
    """A369 reported three citation defects that were folding bugs, not data bugs."""
    assert refs.fold("Slavík") == "slavik", refs.fold("Slavík")
    assert refs.fold("Böhm") == "bohm", refs.fold("Böhm")
    assert refs.fold("Munafò") == "munafo", refs.fold("Munafò")
    assert refs.fold("Lovász") == "lovasz", refs.fold("Lovász")
    assert refs.fold("Štrumbelj") == "strumbelj", refs.fold("Štrumbelj")


def t_emit_blocks_grouped_and_sorted():
    """A369 shipped 111 definitions under one heading although 109 were research."""
    out = refs.emit_blocks({
        "research_zed_2020": "https://doi.org/10.1/z",
        "research_alpha_1999": "https://doi.org/10.1/a",
        "ref_spec": "https://example.invalid/spec",
        "related_post_x": "{% post_url 2026-01-01-x %}",
    })
    assert "### Reference" in out and "### Research" in out and "### Related Post" in out
    ra = out.index("research_alpha_1999")
    rz = out.index("research_zed_2020")
    assert ra < rz, "definitions not sorted within group"
    assert out.index("### Reference") < out.index("### Related Post") < out.index("### Research")


def t_assign_anchors_no_collision():
    recs = [{"authors": ["Smith"], "year": 2020, "title": "One"},
            {"authors": ["Smith"], "year": 2020, "title": "Two"},
            {"authors": ["Smith"], "year": 2020, "title": "Three"}]
    out = refs.assign_anchors(recs, taken={"research_smith_2020"})
    assert len(out) == 3, out
    assert "research_smith_2020" not in out, "collided with a taken anchor"


def t_clean_strips_prose_punctuation():
    s = refs.clean("Compilers: Principles; Techniques (and Tools) — Second Edition")
    for ch in ":;()[]{}—–":
        assert ch not in s, f"{ch!r} survived in {s!r}"


# ---------------------------------------------------------------- reflow

def t_reflow_bold_atomic():
    body = "**a very emphatic and quite long bold span that would otherwise wrap** and tail text here."
    out = reflow.reflow_body(body * 2, width=40)
    for line in out.split("\n"):
        assert line.count("**") % 2 == 0, f"bold split: {line!r}"


def t_reflow_link_pairs_atomic():
    body = " ".join(f"[Some fairly long reference title {i}][research_author_{i}]" for i in range(8))
    out = reflow.reflow_body(body, width=50)
    for line in out.split("\n"):
        assert line.count("[") == line.count("]"), f"link split: {line!r}"


def t_reflow_never_glues_heading():
    """A369 shipped a heading joined onto the paragraph above it by a reflow."""
    src = "Some prose that is long enough to be rewrapped by the reflow.\n\n### A Heading\n\nMore prose.\n"
    out = reflow.reflow_body(src, width=30)
    assert "\n### A Heading" in out
    assert lint.scan(out) == [] or all(c != "heading-inline" for _, c, _ in lint.scan(out))


def t_reflow_display_math_single_line():
    out = reflow.reflow_body("$$\na = b + c\n$$", width=40)
    assert out.count("\n") == 0, repr(out)


def t_reflow_leaves_tables_and_defs():
    src = "| a | b |\n|---|---|\n| 1 | 2 |\n\n[research_x_2020]: https://doi.org/10.1/x\n"
    assert reflow.reflow_body(src, width=10) == src.rstrip("\n")


# ---------------------------------------------------------------- edits

def t_edits_match_across_line_breaks():
    """The fix that existed in exactly one of 457 scratch files."""
    text = "The quick brown fox\njumps over the lazy dog.\n"
    out = edits.apply_to_text(text, [("quick brown fox jumps over", "slow grey cat sits beside")],
                              guard_invariants=False)
    assert "slow grey cat sits beside" in out


def t_edits_all_or_nothing():
    text = "alpha beta gamma\n"
    try:
        edits.apply_to_text(text, [("alpha", "ALPHA"), ("nonexistent", "X")],
                            guard_invariants=False)
    except edits.EditError as e:
        assert "nothing written" in str(e)
        return
    raise AssertionError("a failing batch was applied anyway")


def t_edits_reports_every_failure():
    try:
        edits.apply_to_text("alpha\n", [("missing one", "a"), ("missing two", "b")],
                            guard_invariants=False)
    except edits.EditError as e:
        assert "2 of 2" in str(e), str(e)
        assert "missing one" in str(e) and "missing two" in str(e)
        return
    raise AssertionError("no error raised")


def t_edits_rejects_ambiguous_anchor():
    try:
        edits.apply_to_text("repeat repeat\n", [("repeat", "X")], guard_invariants=False)
    except edits.EditError as e:
        assert "matched 2 times" in str(e), str(e)
        return
    raise AssertionError("an ambiguous edit was applied")


def t_edits_equation_guard():
    text = "intro\n\n$$a = b$$\n\ntail\n"
    try:
        edits.apply_to_text(text, [("$$a = b$$", "a equals b")], guard_invariants=False)
    except edits.EditError as e:
        assert "equation count dropped" in str(e), str(e)
        return
    raise AssertionError("a dropped equation was allowed")


def t_edits_invariant_guard_blocks_glued_heading():
    text = FM + "Some prose here.\n\n## Heading\n\nMore.\n"
    try:
        edits.apply_to_text(text, [("Some prose here.", "Some prose here. ## Injected")])
    except ValueError as e:
        assert "heading-inline" in str(e), str(e)
        return
    raise AssertionError("a glued heading was written")


def t_substitute_tolerates_wrapped_keys():
    """A369 inserted {c('...')} literally, then failed to match reflow-wrapped keys."""
    import tempfile
    # The reference block is part of the fixture because `substitute` runs the
    # invariant guard, which correctly refuses a citation with no definition.
    text = (FM + "prose {c('a long cluster\nname wrapped by reflow')} tail\n"
            "\n## References\n\n### Research\n\n[research_x_2020]: https://doi.org/10.1/x\n")
    with tempfile.NamedTemporaryFile("w", suffix=".markdown", delete=False) as fh:
        fh.write(text)
        p = fh.name
    try:
        edits.substitute(p, {"a long cluster name wrapped by reflow": "[T][research_x_2020]"})
        out = open(p).read()
        assert "{c(" not in out and "[T][research_x_2020]" in out
    finally:
        os.unlink(p)


def t_substitute_raises_on_unknown_key():
    import tempfile
    with tempfile.NamedTemporaryFile("w", suffix=".markdown", delete=False) as fh:
        fh.write(FM + "prose {c('unknown')} tail\n")
        p = fh.name
    try:
        edits.substitute(p, {"other": "x"})
    except edits.EditError:
        return
    finally:
        os.unlink(p)
    raise AssertionError("an unknown template key was silently left in place")


# ---------------------------------------------------------------- lint

def t_lint_doubled_backslash():
    """Shipped in three consecutive X-Planes articles; warned about, never checked."""
    rows = lint.scan(FM + "text\n\n$$a \\\\, b$$\n")
    assert any(c == "math-doubled-backslash" and s == lint.DEFECT for s, c, _ in rows), rows


def t_lint_glued_heading():
    rows = lint.scan(FM + "Some prose. ## Heading\n\nmore\n")
    assert any(c == "heading-inline" and s == lint.DEFECT for s, c, _ in rows), rows


def t_lint_unfilled_template():
    rows = lint.scan(FM + "prose {c('cluster')} tail\n")
    assert any(c == "unfilled-template" and s == lint.DEFECT for s, c, _ in rows), rows


def t_lint_anchor_integrity():
    text = FM + "prose [X][research_used_2020] tail\n\n## References\n\n[research_orphan_1999]: https://x\n"
    rows = lint.scan(text)
    checks = {c for _, c, _ in rows}
    assert "anchor-undefined" in checks and "anchor-unused" in checks, rows


def t_lint_conventions_are_not_defects():
    """Measured against the corpus: kramdown renders all three of these correctly."""
    text = FM + "a **bold\nspan** b\n\n$$\nx = y\n$$\n"
    rows = lint.scan(text)
    for sev, chk, _ in rows:
        if chk in ("bold-span", "math-multiline", "duplicate-url", "split-link"):
            assert sev == lint.CONVENTION, f"{chk} must not be a defect"


def t_lint_clean_text_passes():
    text = FM + "Some prose.\n\n## Heading\n\n$$a \\, b$$\n\nCite [X][research_x_2020].\n\n## References\n\n[research_x_2020]: https://doi.org/10.1/x\n"
    assert lint.assert_clean(text) is True


# ---------------------------------------------------------------- fetch, offline only

def t_crossref_fields_normalisation():
    import fetch
    msg = {"title": ["A Title"], "author": [{"family": "Smith"}, {"given": "no family"}],
           "issued": {"date-parts": [[1979, 3]]}, "container-title": ["A Journal"]}
    title, authors, year, venue = fetch.crossref_fields(msg)
    assert (title, authors, year, venue) == ("A Title", ["Smith"], 1979, "A Journal")
    assert fetch.crossref_fields(None) == ("", [], None, "")


def t_crossref_fields_missing_pieces():
    import fetch
    assert fetch.crossref_fields({"title": []}) == ("", [], None, "")


# ---------------------------------------------------------------- package hygiene

def t_no_stdlib_shadowing():
    """A module named `numbers` shadowed the standard library and broke `statistics`.

    Article scripts put `_lib` first on sys.path, so any module here named after
    a stdlib module is imported instead of it. `numbers.py` did exactly that and
    broke every caller through the fractions import chain inside `statistics`.
    """
    here = os.path.dirname(os.path.abspath(__file__))
    names = {f[:-3] for f in os.listdir(here) if f.endswith(".py")}
    clash = sorted(names & set(sys.stdlib_module_names))
    assert not clash, f"modules shadow the standard library: {clash}"


def t_statistics_still_importable_with_lib_first():
    import importlib
    importlib.import_module("statistics")
    importlib.import_module("fractions")


# ---------------------------------------------------------------- diction

def t_diction_strips_citation_link_text():
    """The reason _verify.py cannot do this: link text is not prose."""
    import diction
    t = FM + "Real prose here. [A Very Long Harvested Paper Title][research_x_2020]\n"
    p = diction.prose(t)
    assert "Harvested" not in p and "Real prose here." in p


def t_diction_ignores_hyphenated_compounds():
    """`application-specific` is a domain term, not an overuse of `specific`."""
    import diction
    t = FM + "This is application-specific and target-specific, but one specific case matters.\n"
    r, _n = diction.rates(t, ["specific"])
    assert r["specific"][0] == 1, r["specific"]


def t_diction_baseline_flags_over_max():
    import diction, tempfile, os as _os
    peers = []
    for i in range(3):
        fh = tempfile.NamedTemporaryFile("w", suffix=".markdown", delete=False)
        fh.write(FM + ("Plain sentence here. " * 40) + "rather than once.\n")
        fh.close()
        peers.append(fh.name)
    try:
        heavy = FM + ("rather than " * 30) + ("filler word " * 60)
        rows, n, npeers = diction.compare(heavy, peers, ["rather than"])
        assert npeers == 3
        assert rows[0][5] == "over-max", rows[0]
    finally:
        for p_ in peers:
            _os.unlink(p_)


# ---------------------------------------------------------------- audit

def t_audit_citation_gap_detection():
    import audit
    t = FM + "Prose with no source.\n\n$$a = b$$\n\nMore prose.\n"
    assert len(audit.citation_gaps(t)) == 1
    t2 = FM + "Prose citing [X][research_x_2020].\n\n$$a = b$$\n\nMore.\n"
    assert audit.citation_gaps(t2) == []


def t_audit_primary_reports_count_and_fraction():
    import audit
    t = (FM + "body [A][research_a_1960] [B][research_b_2020]\n\n## References\n\n"
         "[research_a_1960]: https://x\n[research_b_2020]: https://y\n")
    pf = audit.primary_fraction(t, 1999)
    assert pf["primary_count"] == 1 and pf["dated"] == 2
    assert abs(pf["primary_fraction"] - 0.5) < 1e-9


def t_anchor_parser_is_single_and_agrees():
    """audit and citations each grew a parser and they disagreed on `1978b`."""
    import audit, citations, refs
    a = "research_nemhauser_wolsey_1978b"
    assert refs.parse_anchor(a) == ("research", "nemhauser", 1978)
    assert audit.year_of(a) == 1978
    assert citations.claimed_from_anchor(a) == ("nemhauser", 1978)
    assert refs.parse_anchor("research_zhao_2023_b")[2] == 2023


# ---------------------------------------------------------------- numcheck

def t_numcheck_catches_wrong_value():
    import numcheck
    c = numcheck.Checker("t")
    c.chk("good", 10.0, 10.05, tol=0.01)
    c.chk("bad", 10.0, 42.0, tol=0.01)
    assert c.ok == 1 and len(c.failures) == 1


def t_numcheck_property_reports_counterexample():
    import numcheck
    c = numcheck.Checker("t")
    c.prop("always positive", lambda x: x > 0, lambda r: r.uniform(-1, 1), trials=500)
    assert len(c.failures) == 1 and "property failed" in c.failures[0]


def t_numcheck_requires_values_in_draft():
    import numcheck, tempfile, os as _os
    fh = tempfile.NamedTemporaryFile("w", suffix=".markdown", delete=False)
    fh.write("The article states 1234 and nothing else.\n")
    fh.close()
    try:
        c = numcheck.Checker("t")
        c.chk("present", 1234, 1234, tol=0)
        c.chk("absent", 9999, 9999, tol=0)
        c.require_in_text(fh.name)
        assert any("absent" in f for f in c.failures), c.failures
    finally:
        _os.unlink(fh.name)


# ---------------------------------------------------------------- citations

def t_citations_flags_search_endpoints():
    import citations
    t = ("body [A][ref_a]\n\n## References\n\n"
         "[ref_a]: https://openlibrary.org/search?q=x\n")
    assert "ref_a" in citations.search_endpoint_citations(t)


def t_citations_fold_handles_diacritics():
    import citations
    for raw, want in [("Slavík", "slavik"), ("Böhm", "bohm"), ("Munafò", "munafo")]:
        assert citations.fold(raw) == want, (raw, citations.fold(raw))


# ---------------------------------------------------------------- anti-duplication

def t_no_duplicate_function_bodies_across_modules():
    """The library reproduced its own defect within a day of being written.

    An audit found `fold` byte-identical in two modules, seven independent
    splits on `## References` across four, and nine hard-codings of the anchor
    character class across six. Extracting shared mechanism does not stop shared
    mechanism reappearing, because re-deriving two lines is always locally
    cheaper than adding an import. So it is checked rather than trusted.
    """
    import hashlib
    import re as _re
    here = os.path.dirname(os.path.abspath(__file__))
    bodies = {}
    for fn in sorted(os.listdir(here)):
        if not fn.endswith(".py") or fn.startswith("test_"):
            continue
        src = open(os.path.join(here, fn), encoding="utf-8").read()
        for m in _re.finditer(r"(?m)^def ([a-z_]+)\(.*?:\n((?:(?:    .*)?\n)*)", src):
            q = chr(34) * 3  # a literal triple quote would end this file's own strings
            body = _re.sub(r"\s+", " ",
                           _re.sub(q + r".*?" + q, "", m.group(2), flags=_re.S)).strip()
            if len(body) < 40:
                continue
            bodies.setdefault(hashlib.sha256(body.encode()).hexdigest(), []).append((fn, m.group(1)))
    dup = [v for v in bodies.values() if len({f for f, _ in v}) > 1]
    assert not dup, f"identical function bodies in different modules: {dup}"


def t_document_structure_lives_in_one_module():
    """Only post.py may know how a post splits or what an anchor looks like."""
    import re as _re
    here = os.path.dirname(os.path.abspath(__file__))
    offenders = []
    for fn in sorted(os.listdir(here)):
        if not fn.endswith(".py") or fn.startswith("test_") or fn == "post.py":
            continue
        src = open(os.path.join(here, fn), encoding="utf-8").read()
        if _re.search(r'split\("## References"', src):
            offenders.append(f"{fn}: splits on '## References' directly")
        if "A-Za-z0-9_-" in src:
            offenders.append(f"{fn}: hard-codes the anchor character class")
    assert not offenders, "; ".join(offenders)


def t_library_imports_are_acyclic():
    """post imports nothing from the library, so the graph cannot cycle."""
    import re as _re
    here = os.path.dirname(os.path.abspath(__file__))
    names = {f[:-3] for f in os.listdir(here) if f.endswith(".py") and not f.startswith("test_")}
    src = open(os.path.join(here, "post.py"), encoding="utf-8").read()
    imported = set(_re.findall(r"(?m)^import ([a-z_]+)", src))
    assert not (imported & names), f"post.py imports from the library: {imported & names}"



def t_reflow_keeps_inline_links_atomic():
    """An inline [text](url) must not be split, exactly as a reference pair must not.

    REGRESSION FOR A REAL DISAGREEMENT BETWEEN TWO SHARED MODULES. `lint.scan` reports a
    split link whenever a line's brackets do not balance, which covers the inline form,
    but `reflow` held only the reference form together. Reflow would split an inline link
    and lint would then report a defect on a file reflow had just declared a fixed point.
    A324 hit it on an in-page section link.
    """
    para = ("word " * 18) + "and the [ground-prediction section](#comparison-with-ground-prediction) says so."
    out = reflow.reflow_paragraph(para)
    assert "\n" in out, "the fixture must be long enough to wrap, or it proves nothing"
    for line in out.split("\n"):
        assert line.count("[") == line.count("]"), f"split link in: {line!r}"
        assert line.count("(") == line.count(")"), f"split link in: {line!r}"


def t_clean_strips_latex_from_titles():
    """A publisher title carrying inline math must not reach link text.

    A327 hit a Springer title reading "Al/MLG/CuO/$${\\text{Bi}}_{2}{\\text{O}}_{3}$$
    Nanothermite". Truncated for link text it left a single unbalanced `$$`, which opens a
    MathJax display block that swallows the rest of the page, and `_verify.py` caught it
    only as an odd delimiter count.
    """
    out = refs.clean("Study of Al/MLG/CuO/$${\\text{Bi}}_{2}{\\text{O}}_{3}$$ Nanothermite")
    assert "$" not in out, out
    assert "\\" not in out, out
    assert "Bi" in out and "Nanothermite" in out, out
    assert refs.clean("plain title") == "plain title"


def t_clean_strips_mathjax_inline_delimiters():
    """A BARE BACKSLASH DELIMITER SURVIVES THE COMMAND RULE AND OPENS A MATH BLOCK.

    `\\(` and `\\[` are MathJax delimiters, and the rule that strips `\\command`
    sequences does not reach them because the character after the backslash is
    punctuation rather than a letter. A328 harvested a title beginning
    `\\({\\mathcal{L}_1}\\)` and the cleaned link text kept bare backslashes, which is
    the A327 dollar-delimiter defect arriving through a different delimiter.
    """
    out = refs.clean(r"\({\mathcal{L}_1}\) Adaptive Loss Fault Tolerance Control")
    assert "\\" not in out, out
    assert out.startswith("L"), out
    assert "Adaptive Loss Fault Tolerance Control" in out, out

    # the dollar form stays fixed
    assert "$" not in refs.clean(r"Al/MLG/CuO/$${\text{Bi}}_{2}$$ Nanothermite")

    # an ordinary title is untouched
    assert refs.clean("Ordinary Title With No Math") == "Ordinary Title With No Math"


def t_anchor_and_display_survive_non_latin_author_names():
    """A NAME IN A NON-LATIN SCRIPT MUST NOT PRODUCE A BROKEN ANCHOR.

    `fold` returns the empty string for Chinese, Cyrillic and similar scripts, so an
    anchor stem built from two such names became a bare underscore, and the `or "anon"`
    guard did not fire because a lone underscore is truthy. A328 harvested thirteen such
    records and shipped anchors reading `research___2023` with link text that was, in one
    case, nothing but a year.

    THE TEST IS INSERTED ABOVE THE DISCOVERY LOOP ON PURPOSE. A327 appended one to the end
    of this file and it was never collected, and the suite reported a healthy count while
    silently omitting the new case.
    """
    # both author forms present: the folding one must win
    assert refs.anchor_stem(["Азамов", "Azamov"], "2020", "A pursuit-evasion game") == \
        "research_azamov_2020"
    assert refs.display(["Азамов", "Azamov"], "2020", "A pursuit-evasion game") == \
        "Azamov 2020"

    # no folding form at all: fall back to the title, never to a bare separator
    stem = refs.anchor_stem(["王", "周"], "2023", "A hierarchical decision making method")
    assert stem.strip("_") == stem.strip("_") and "__" not in stem, stem
    assert stem.startswith("research_a_hierarchical"), stem
    assert refs.display(["王", "周"], "2023", "A hierarchical decision making method") \
        .startswith("A hierarchical")

    # a placeholder author is not an author
    assert refs.anchor_stem(["-"], "2023", "Enhancing limited authority") \
        .startswith("research_enhancing"), refs.anchor_stem(["-"], "2023", "Enhancing limited authority")

    # the ordinary case is untouched
    assert refs.anchor_stem(["Cobleigh"], "1994", "Yawing moment asymmetry") == \
        "research_cobleigh_1994"



for name, fn in sorted(list(globals().items())):
    if name.startswith("t_") and callable(fn):
        check(name[2:], fn)

ok = sum(1 for p, _, _ in RESULTS if p)
for passed, name, detail in RESULTS:
    if not passed:
        print(f"  FAIL  {name}: {detail}")
print(f"{ok}/{len(RESULTS)} passed")
sys.exit(0 if ok == len(RESULTS) else 1)
