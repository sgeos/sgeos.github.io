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


for name, fn in sorted(list(globals().items())):
    if name.startswith("t_") and callable(fn):
        check(name[2:], fn)

ok = sum(1 for p, _, _ in RESULTS if p)
for passed, name, detail in RESULTS:
    if not passed:
        print(f"  FAIL  {name}: {detail}")
print(f"{ok}/{len(RESULTS)} passed")
sys.exit(0 if ok == len(RESULTS) else 1)
