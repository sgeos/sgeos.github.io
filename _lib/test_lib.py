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

import diction
import edits
import gate
import lint
import post
import refs
import reflow
import render
import resolve

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


def t_lint_display_math_sharing_a_line_with_prose():
    """A341 shipped one of these into a build and nothing in the toolchain saw it.

    An edit landed `$$...$$` and the next paragraph's opening sentence on one
    source line. Kramdown rendered it as INLINE math inside a paragraph, with
    two unrelated sentences run together. The delimiters balance and the markup
    resolves, so `render.py` reports nothing; the page is merely wrong. It was
    found by comparing the source equation count against the rendered one.
    """
    bad = FM + "prose\n\n$$a = b$$ **Next paragraph opens here.**\n"
    rows = lint.scan(bad)
    assert any(c == "math-display-inlined" and s == lint.DEFECT for s, c, _ in rows), rows

    # A COMPLETE DISPLAY EQUATION ON ITS OWN LINE MUST NOT FIRE.
    good = FM + "prose\n\n$$a = b$$\n\nmore prose\n"
    assert not any(c == "math-display-inlined" for _s, c, _ in lint.scan(good))

    # NEITHER MUST A TWO-LINE EQUATION, which 24 percent of the corpus uses and
    # which kramdown renders correctly. It is a convention, not a defect.
    two = FM + "prose\n\n$$a = b\nc = d$$\n\nmore\n"
    assert not any(c == "math-display-inlined" for _s, c, _ in lint.scan(two))

    # NOR A REFERENCE BULLET whose link text is a paper title containing math.
    ref = FM + "prose\n\n- [$$L_1$$ adaptive control 2026][research_a_2026]\n"
    assert not any(c == "math-display-inlined" for _s, c, _ in lint.scan(ref))

    # NOR SHELL OR MAKEFILE SYNTAX INSIDE CODE, where `$$` is the shell's own.
    code = FM + "prose\n\n```sh\nfor i in 1 2; do echo $$i; done\n```\n"
    assert not any(c == "math-display-inlined" for _s, c, _ in lint.scan(code))


def t_post_strip_code_keeping_lines_preserves_numbering():
    """The line-preserving stripper must not shift the numbers it exists to keep."""
    text = "a\n```\ncode\nmore code\n```\nb\n"
    out = post.strip_code_keeping_lines(text)
    assert len(out.split("\n")) == len(text.split("\n")), (out, text)
    assert out.split("\n")[5] == "b", out.split("\n")
    # a Liquid highlight block is code too, and a tab-indented line is code
    liquid = "a\n{% highlight sh %}\n$$x\n{% endhighlight %}\nb\n"
    assert len(post.strip_code_keeping_lines(liquid).split("\n")) == len(liquid.split("\n"))
    assert "$$x" not in post.strip_code_keeping_lines(liquid)
    assert post.strip_code_keeping_lines("\tmake $$i\n").strip() == ""


def t_gate_normalises_typographic_punctuation():
    """A334 recorded this and told the series to carry it forward. A342 did not.

    A334 refused a nickel-hydrogen battery paper whose depositor wrote the hyphen
    as U+2010. A342 then refused `Validating Human-Robot Interaction Schemes in
    Multitasking Environments`, one of its own foundational sources, because the
    publisher sets `Human-Robot` with an en dash. Twice is a pattern, and a
    per-article fix has already failed once, so the gate normalises.
    """
    g = gate.Gate([r"human[- ]robot interaction"], name="t")
    assert g.admits("Common metrics for human-robot interaction")
    for dash in "\u2010\u2011\u2012\u2013\u2014\u2212":
        title = f"Validating Human{dash}Robot Interaction Schemes"
        assert g.admits(title), f"rejected on U+{ord(dash):04X}: {title!r}"
    # and an off-subject title must still be refused, whatever its punctuation
    assert not g.admits("Validating Human\u2013Machine Trust in Finance")
    # explain() must see the same normalised text
    assert g.explain("Common metrics for human\u2013robot interaction") is None


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


def t_clean_strips_a_bare_pipe_because_kramdown_reads_it_as_a_table():
    """A BARE PIPE IN LINK TEXT IS A TABLE, WHICH IS THE LAST OF THE DELIMITER FAMILY.

    kramdown reads a paragraph whose first line contains a pipe as a table, so a
    pipe that reflow happens to place at a line start shreds the surrounding
    prose into cells. A334 harvested a title deposited as
    "Influence of Small Satellites^|^apos; Post-mission Disposal", where a
    publisher had mangled an apostrophe entity into a sequence carrying a
    literal pipe. The semicolon rule then stripped the terminator and left the
    pipe in the link text, where nothing else would have removed it.

    Same family as the unbalanced `$$` of A327, the bare `\\(` of A328 and the
    stray `>` of A331.
    """
    out = refs.clean("Influence of Small Satellites^|^apos; Post-mission Disposal")
    assert "|" not in out, out
    assert "Post-mission Disposal" in out, out

    # a pipe standing alone between words also goes
    assert "|" not in refs.clean("Throughput | Latency Trade-offs")

    # and an ordinary title is untouched
    assert refs.clean("Ordinary Title With No Pipe") == "Ordinary Title With No Pipe"


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



def t_clean_decodes_html_entities_before_stripping_punctuation():
    """AN UNDECODED ENTITY IS TURNED INTO VISIBLE JUNK BY THE PUNCTUATION RULE.

    Publishers emit titles wrapped in `&lt;title&gt;` rather than in a literal tag. The
    tag-stripping regex never sees those, and the later rule that removes semicolons then
    converts them into `&lt title&gt`, which renders as exactly that string. THIS SHIPPED
    IN THREE CONSECUTIVE DRAFTS and was found by reading the reference list, not by any
    checker.
    """
    got = refs.clean("&lt;title&gt;Inspection of metallic thermal protection&lt;/title&gt;")
    assert got == "Inspection of metallic thermal protection", got
    assert "&lt" not in got and "&gt" not in got and "<" not in got

    # the literal-tag form must still work, and so must the ampersand entity
    assert refs.clean("<title>Plain tag form</title>") == "Plain tag form"
    assert refs.clean("Science &amp; Enabling Technologies") == \
        "Science and Enabling Technologies"
    # a BARE ampersand is prose punctuation the style rules do not want either
    assert "&" not in refs.clean("Reliability & Robust Design")

    # AND THE MARKUP MUST NOT SURVIVE INTO AN ANCHOR EITHER. The title fallback feeds a
    # two-word window into `slug`, so undecoded markup pushes every meaningful word out of
    # that window and yields `research_lt_title_gt_..._1998`.
    anc = refs.anchor_stem([], "1998", "&lt;title&gt;Metallic panels&lt;/title&gt;")
    assert anc == "research_metallic_panels_1998", anc


def t_verify_doi_declines_an_uncheckable_author_rather_than_failing_it():
    """AN ANCHOR STEM IS ONLY A SURNAME WHEN AN AUTHOR SURVIVED FOLDING.

    Where every registry author is in a non-Latin script, `anchor_stem` falls back to the
    title, so the stem carries no surname. Comparing the two can never succeed, and the old
    code reported a MISMATCH on a citation that was entirely correct. A330's sweep hit this
    on a Chinese-language paper and it read as a citation defect.
    """
    import citations
    # the stem is a title fallback and the registry author folds to nothing
    ok = citations.fold("\u67f3") == ""
    assert ok, "the test premise is that this name folds away"

    # simulate the comparison verify_doi makes, without a network call
    authors = ["\u654f\u9759 \u67f3"]
    surname = "leakage"
    foldable = [a for a in authors if citations.fold(a)]
    checkable = bool(foldable) and bool(surname)
    author_ok = (not checkable) or any(surname in citations.fold(a) for a in foldable)
    assert not checkable, "no foldable author, so the check cannot run"
    assert author_ok, "an uncheckable author must not be reported as a mismatch"

    # AND THE CHECK MUST STILL BITE WHEN IT CAN RUN
    authors2 = ["V. I. Weingarten", "P. Seide"]
    foldable2 = [a for a in authors2 if citations.fold(a)]
    assert any("weingarten" in citations.fold(a) for a in foldable2)
    assert not any("nosuchname" in citations.fold(a) for a in foldable2)


def t_clean_strips_bare_angle_brackets():
    r"""A BARE ANGLE BRACKET IS MARKUP AND SURVIVES THE TAG RULE.

    `clean` removes a MATCHED `<...>` pair, so a published title reading "Precision >>
    Accuracy" keeps both characters. A `>` that reflow places at the start of a line is a
    markdown blockquote, which is the same family as the unbalanced `$$` and the bare `\(`
    this file already guards. A331 found one sitting mid-line by luck.
    """
    got = refs.clean("Precision >> Accuracy in Probabilistic Risk Assessment")
    assert ">" not in got and "<" not in got, got
    assert "Precision" in got and "Accuracy" in got, got
    # the matched-tag case must still work
    assert refs.clean("<title>Plain tag form</title>") == "Plain tag form"
    # and a lone opening bracket must not survive either
    assert "<" not in refs.clean("Comparison of a < b Under Load")


def t_clean_keeps_a_joining_dash_as_a_hyphen_rather_than_a_space():
    """A COMPOUND JOINER MUST NOT BECOME A WORD SEPARATOR.

    A332 harvested "Applications of jet-jet/film impingement for atomization
    enhancement", written with an EN DASH between the two occurrences of `jet`.
    Collapsing every dash to a space turned it into "jet jet", and the corpus
    doubled-word check then reported a defect against a title that never carried
    one. A hyphen is permitted in prose, so a dash BETWEEN TWO WORD CHARACTERS
    becomes a hyphen and only a parenthetical dash becomes a space.
    """
    got = refs.clean("Applications of jet–jet/film impingement")
    assert "jet jet" not in got, got
    assert "jet-jet" in got, got
    # the em dash joins the same way
    assert "solid-liquid" in refs.clean("A solid—liquid interface study")
    # a PARENTHETICAL dash is still a space, because that is what it separates
    got = refs.clean("Powered lift — a review of the evidence")
    assert "—" not in got and "-" not in got, got
    assert "lift a review" in got, got
    # and neither form leaves a dash behind for the prose rules to trip on
    for s in ("a–b", "a – b", "a—b", "a — b"):
        assert "–" not in refs.clean(s) and "—" not in refs.clean(s)


def t_clean_normalises_typographic_punctuation_to_ascii():
    """A CURLY APOSTROPHE HID A CONTRACTION FROM THE CORPUS CHECKER.

    The corpus contraction pattern matches an ASCII apostrophe, so a harvested
    title reading "What's New" written with U+2019 passed a check that exists to
    catch exactly that word. A332 shipped it until a character survey found it.
    A SOFT HYPHEN is invisible and breaks word matching, and a STANDALONE
    COMBINING MARK attaches itself to whatever precedes it. All three are
    normalised before any other rule runs. DIACRITICS ARE NOT TOUCHED, because
    an author's name is not punctuation.
    """
    assert refs.clean("What’s New in Powered Lift").startswith("What's"), \
        refs.clean("What’s New in Powered Lift")
    assert "‐" not in refs.clean("FAN‐IN‐WING")
    assert refs.clean("FAN‐IN‐WING") == "FAN-IN-WING"
    assert "­" not in refs.clean("Systems Analy­sis")
    assert refs.clean("Coefficient ͞CL") == "Coefficient CL"
    for src in ("“quoted”", "‘single’", "an ellipsis…"):
        got = refs.clean(src)
        for ch in "“”‘’…":
            assert ch not in got, (src, got)
    # a name carrying diacritics must survive untouched
    assert refs.clean("Slavík and Böhm") == "Slavík and Böhm"
    assert refs.clean("Munafò, Lovász and Štrumbelj") == "Munafò, Lovász and Štrumbelj"


def t_clean_unescapes_double_escaped_markup_to_a_fixed_point():
    """DOUBLE-ESCAPED MARKUP BECAME VISIBLE JUNK IN LINK TEXT.

    A publisher emitting `&lt;p&gt;&amp;nbsp;` decodes once to `<p>&nbsp;`. The
    tag rule then removes the paragraph tag, the surviving literal `&nbsp;`
    meets the ampersand rule and becomes `andnbsp;`, and the semicolon rule
    strips the terminator. A332 shipped link text reading `andnbsp andnbsp
    andnbsp` until the corpus doubled-word check caught it. Unescaping to a
    fixed point is the only ordering in which every later rule sees text.
    """
    got = refs.clean("&lt;p&gt;&amp;nbsp;&amp;nbsp;Closed-Loop Valuation&lt;/p&gt;")
    assert "nbsp" not in got, got
    assert "and" not in got.split()[:1], got
    assert "Closed-Loop Valuation" in got, got
    # a singly-escaped ampersand must still become the word `and`
    assert refs.clean("Smith &amp; Jones") == "Smith and Jones"
    assert refs.clean("Smith & Jones") == "Smith and Jones"
    # and the iteration must terminate on text that is not markup at all
    assert refs.clean("A plain title") == "A plain title"



def t_collocations_separates_a_term_of_art_from_a_verbal_tic():
    """A RATE CANNOT TELL THEM APART AND THE CORPUS PAID FOR THAT TWICE.

    `specific` reached 15.07 per thousand in the rocket propellant articles and 86 percent of
    those uses are "specific impulse", which names a quantity and cannot be paraphrased.
    `substantial` reached 10.6 per thousand in the hardware description languages article and
    named nothing. The counts look alike and only the neighbouring words separate them, so
    the collocation share is the discriminator a frequency warning has to carry.
    """
    art = "The specific impulse is high. A vacuum specific impulse of four hundred. " * 4
    _total, _before, after, stats = diction.collocations(art, "specific")
    assert after[0][0] == "impulse", after
    assert stats["top_share"] > 0.9, stats

    tic = ("A substantial adoption followed. There is substantial evidence here. "
           "The substantial gains were real. Substantial concerns remain open. ")
    _t2, _b2, _a2, s2 = diction.collocations(tic, "substantial")
    assert s2["top_share"] < 0.5, s2


def t_top_collocate_skips_function_words():
    """"configuration the" IS THE MOST FREQUENT PAIR AND IT IS NOT EVIDENCE.

    The first version of this helper reported the raw most-common neighbour, which for a noun
    in ordinary prose is whatever determiner follows the clause. It answered "configuration
    the" for an article whose real signal was "capability configuration", which would have
    told a reader triaging the warning nothing at all.
    """
    text = ("The capability configuration the first. A capability configuration the second. "
            "The capability configuration the third. A vehicle configuration the fourth. ")
    word, count, share, phrase = diction.top_collocate(text, "configuration")
    assert word == "capability", (word, count, share, phrase)
    assert phrase == "capability configuration", phrase
    assert 0.0 < share <= 1.0, share


def t_collocations_reads_both_directions_because_the_compound_side_differs():
    """A NOUN COMPOUNDS TO ITS LEFT AND AN ADJECTIVE TO ITS RIGHT.

    `configuration` forms "capability configuration", so the evidence precedes it. `specific`
    forms "specific impulse", so the evidence follows it. Testing only one direction misreads
    whichever word compounds the other way, which is the mistake that briefly recommended
    rewriting four published articles.
    """
    noun = "A capability configuration and another capability configuration appear here. "
    _t, before, _a, st = diction.collocations(noun, "configuration")
    assert before[0][0] == "capability", before
    assert st["before_named"] > st["after_named"], st

    adj = "The specific impulse and the specific impulse are quoted throughout. "
    _t2, _b2, after, st2 = diction.collocations(adj, "specific")
    assert after[0][0] == "impulse", after
    assert st2["after_named"] > st2["before_named"], st2


def t_word_outliers_counts_a_silent_peer_as_a_zero():
    """TAKING A MAXIMUM OVER ONLY THE PEERS THAT USE A WORD HIDES EVERY OUTLIER.

    If the peer maximum is computed from the articles that happen to contain a word, an
    article that is the only one using it compares against itself and looks unremarkable. A
    peer that never uses the word has a rate of zero and must be counted as one.
    """
    body = " ".join(["alpha beta gamma delta"] * 150)
    text = body + " widget widget widget widget widget widget widget"
    silent = [body] * 3
    rows, peer_n = diction.word_outliers(text, silent, vocabulary=["widget"], min_count=3)
    assert peer_n == 3, peer_n
    assert rows and rows[0][1] == "widget", rows
    assert rows[0][6] == 0, rows[0]          # peers using the word
    assert rows[0][0] is None, rows[0]       # no peer ever used it, so no ratio exists

    user = body + " widget widget"
    rows2, _ = diction.word_outliers(text, [body, body, user], vocabulary=["widget"], min_count=3)
    assert rows2[0][6] == 1, rows2[0]
    assert rows2[0][5] > 0, rows2[0]         # a peer maximum now exists
    assert rows2[0][0] > 1.0, rows2[0]       # and this article exceeds it




def _load_verify():
    """Load `_verify.py` by path. It sits at the repository root and is not importable."""
    import importlib.util
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    spec = importlib.util.spec_from_file_location("_verify_under_test",
                                                  os.path.join(root, "_verify.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def t_category_slug_collision_is_detectable():
    """TWO CATEGORIES THAT SLUGIFY TO ONE PATH SILENTLY DESTROY A PAGE.

    `c` and `c++` both slugify to `c`, so jekyll-archives wrote /categories/c/index.html
    twice, one archive overwrote the other, and /categories/cpp/ returned 404 on the live site
    for as long as both categories existed. The build said only "Conflict" among a screen of
    Sass deprecations. The remedy is not free either, because the default permalink joins
    every category, so renaming one moves the post and needs a redirect.
    """
    v = _load_verify()
    assert v.category_slug("c++") == "c", v.category_slug("c++")
    assert v.category_slug("c") == "c"
    assert v.category_slug("c#") == "c"
    assert v.category_slug("node.js") == "node-js"
    assert v.category_slug("no_std") == "no-std"
    # the collision is exactly an equality of slugs across distinct names
    assert v.category_slug("c++") == v.category_slug("c")
    assert v.category_slug("rust") != v.category_slug("c")


def t_post_categories_reads_both_front_matter_forms():
    """A NAIVE SPLIT ON WHITESPACE MISREADS THE YAML LIST FORM.

    Splitting `categories: [ai, crypto, philosophy]` on spaces yields `[ai,` and `philosophy]`,
    which slugify to `ai` and `philosophy` and look exactly like a collision with the plain
    forms. That artefact briefly appeared as sixteen collisions where the corpus had one.
    """
    v = _load_verify()
    assert v.post_categories("categories: gamedev playdate c cpp lua") == [
        "gamedev", "playdate", "c", "cpp", "lua"]
    assert v.post_categories("categories: [ai, crypto, philosophy]") == [
        "ai", "crypto", "philosophy"]
    assert v.post_categories("title: no categories here\n") == []
    # a quoted list entry keeps neither quote
    assert v.post_categories('categories: ["ai-tools", \'rust\']') == ["ai-tools", "rust"]




def t_gate_admits_on_a_strong_term_and_never_on_ambiguous_ones():
    """A PILE OF AMBIGUOUS WORDS IS STILL AMBIGUOUS.

    A370's second gate admitted generic stems, being analysis, implementation, generation,
    evaluation, system, model, performance and interface. Every discipline that publishes uses
    those, so the harvest took in rabies control, seismic depth imaging, veterinary breeding
    soundness examination and fibre art, and the larger count read as thoroughness.
    """
    g = gate.Gate([r"compiler|bytecode|coroutine"], name="test")
    assert g.admits("A verified compiler backend")
    assert not g.admits("Rabies control in urban settings")
    # four ambiguous terms and no subject term must still be refused
    noise = "A systematic analysis and evaluation of implementation performance"
    assert not g.admits(noise), noise


def t_gate_explains_a_drop_that_carries_ambiguous_terms():
    """A GATE WRITTEN FOR THE WRONG SUBJECT IS INVISIBLE IN EVERY SUMMARY STATISTIC.

    A333 inherited an aeronautics gate and rejected 2,174 compiler-science titles for
    containing no aircraft. That reports a small corpus, which reads as a thin literature
    rather than a bug. Naming the ambiguous terms at drop time is what makes it visible.
    """
    g = gate.Gate([r"aerofoil|fuselage"], name="wrong-subject")
    why = g.explain("A systematic analysis and evaluation of implementation performance")
    assert why is not None and "ambiguous" in why, why
    assert g.explain("Fuselage loads in transonic flight") is None
    # a genuinely off-subject title carrying no ambiguous vocabulary reports the plain reason
    assert g.explain("Rabies control") == "no subject anchor"


def t_gate_audit_samples_both_sides_reproducibly():
    """ONE SIDE OF THE SAMPLE CANNOT DETECT BOTH FAILURES.

    Reading kept records detects a permissive gate. Reading dropped records detects a narrow
    one. The seed is required so a reviewer can reproduce exactly what was read.
    """
    import contextlib
    import io

    kept = [{"title": f"compiler paper {i}"} for i in range(50)]
    dropped = [({"title": f"other paper {i}"}, "no subject anchor") for i in range(50)]

    # `audit` always prints, because printing is the point of it. Stdout is captured HERE
    # rather than given a quiet flag, since a quiet flag is exactly the thing a future caller
    # would reach for to skip the reading the function exists to force.
    def quiet(*a, **kw):
        with contextlib.redirect_stdout(io.StringIO()):
            return gate.audit(*a, **kw)

    ks1, ds1 = quiet(kept, dropped, seed=7, n=5)
    ks2, ds2 = quiet(kept, dropped, seed=7, n=5)
    assert [r["title"] for r in ks1] == [r["title"] for r in ks2], "sample is not reproducible"
    assert [r["title"] for r, _ in ds1] == [r["title"] for r, _ in ds2]
    assert len(ks1) == 5 and len(ds1) == 5
    # a different seed must actually draw a different sample
    ks3, _ = quiet(kept, dropped, seed=8, n=5)
    assert [r["title"] for r in ks3] != [r["title"] for r in ks1]




def t_lint_resolves_anchors_under_a_non_standard_reference_heading():
    """`references()` SPLITS ON A LITERAL `## References` AND NOT EVERY POST USES IT.

    Two 2016 posts head their link block `## Links:`. The block therefore landed in the body,
    the reference block came back empty, and all 16 of their anchors were reported undefined
    against pages whose links all resolve and which carry no literal `[text][anchor]` anywhere
    in the rendered HTML.
    """
    text = (FM + "See [Parametric Curves][parametric] for detail.\n\n"
            "## Links:\n\n- [Parametric Curves][parametric]\n\n"
            "[parametric]: http://example.org/parcur/\n")
    rows = [r for r in lint.scan(text) if r[1].startswith("anchor")]
    assert rows == [], rows


def t_lint_counts_a_visible_reference_entry_as_a_use():
    """THE CORPUS PUTS THE VISIBLE ENTRY INSIDE THE REFERENCES SECTION.

    Counting uses in the body alone cannot see `- [text][anchor]` lines that sit beside the
    definitions, so every reference in a convention-following article read as defined but
    never used. That was 1,579 false defects, the largest single class in the corpus.
    """
    text = (FM + "Prose with no citation in it at all.\n\n"
            "## References\n\n### Research\n\n"
            "- [Some Paper][research_a_2020]\n\n"
            "[research_a_2020]: https://doi.org/10.0000/x\n")
    rows = [r for r in lint.scan(text) if r[1] == "anchor-unused"]
    assert rows == [], rows
    # a definition nothing points at anywhere is still reported
    orphan = text + "[research_b_2021]: https://doi.org/10.0000/y\n"
    rows2 = [r for r in lint.scan(orphan) if r[1] == "anchor-unused"]
    assert len(rows2) == 1 and "research_b_2021" in rows2[0][2], rows2


def t_unfilled_template_ignores_latex_and_still_catches_a_placeholder():
    """`\\frac{W}{c(t)}` CONTAINS THE LITERAL BYTES THE CHECK LOOKS FOR.

    Scanning raw text reported a surviving generator placeholder against a published article
    whose only offence was dividing by a function of time. Math is stripped first, and the
    real placeholder must still be caught or the fix would be a regression.
    """
    latex = FM + "The ceiling is\n\n$$P_{max}(t) = \\frac{W_{avail}}{c(t)}$$\n\nso that.\n"
    assert [r for r in lint.scan(latex) if r[1] == "unfilled-template"] == []
    real = FM + "prose {c('cluster')} tail\n"
    assert [r for r in lint.scan(real) if r[1] == "unfilled-template"], "placeholder missed"




def t_render_math_parity_survives_a_latex_line_break():
    """TWO WRONG VERSIONS OF THIS CHECK CAME FIRST AND ONE MASKED THE OTHER.

    `\\\\[2mm]` is a LaTeX line break with a spacing argument, legal inside `cases`, and a
    naive counter reads it as an opening display delimiter. Excluding any bracket preceded by
    a backslash then discards the legitimate `\\\\\\]` that closes a block whose last line ends
    in a line break. Only backslash-run parity is right: a bracket is a delimiter when the run
    before it has ODD length.
    """
    # a plain balanced block
    assert render.delimiter_counts(r"\[x = 1\]")[:2] == (1, 1)
    # a line break with a spacing argument is not a delimiter
    assert render.delimiter_counts(r"\[\begin{cases}a \\\\[2mm] b\end{cases}\]")[:2] == (1, 1)
    # a block closing straight after a line break still closes
    assert render.delimiter_counts(r"\[a \\\\ \]")[:2] == (1, 1)
    # inline delimiters are counted separately
    assert render.delimiter_counts(r"\(y\)")[2:] == (1, 1)


def t_render_flags_only_what_a_reader_would_see():
    """A CONVENTION VIOLATION IS NOT A RENDERING DEFECT.

    An unresolved reference shows its own source text in the prose and is a defect. The same
    markup inside a code block is the subject matter of the Jekyll and MathJax tutorial posts
    and must not be flagged.
    """
    assert render.audit_html("<p>ordinary prose</p>") == []
    hit = render.audit_html("<p>see [Some Title][ref_a] here</p>")
    assert hit and hit[0][0] == "unresolved-reference", hit
    # the same text inside a code block is legitimate
    assert render.audit_html("<pre><code>[Some Title][ref_a]</code></pre>") == []
    assert render.audit_html("<pre><code>{% if page.comments %}</code></pre>") == []
    # the doubled-list-marker defect that shipped in A332 and A333
    nested = render.audit_html("<ul><li><ul><li>text</li></ul></li></ul>")
    assert any(n == "nested-empty-list" for n, _c, _e in nested), nested


def t_render_reports_unbalanced_display_math():
    """AN UNCLOSED DISPLAY BLOCK LEAVES RAW LATEX ON THE PAGE."""
    rows = render.audit_html(r"<p>text</p> \[x = 1")
    assert any(n == "math-display-unbalanced" for n, _c, _e in rows), rows
    assert render.audit_html(r"<p>text</p> \[x = 1\]") == []




def t_resolve_treats_bot_mitigation_as_resolution():
    """AN HTTP FAILURE IS USUALLY NOT A CITATION FAILURE.

    Publishers run bot mitigation. IEEE answers 202, several others answer 403, and a Defense
    Technical Information Center deposit refuses the connection outright. On a 250-record
    sample of A370, 22 identifiers, being 8.8 percent, failed by HTTP and every one was
    registered and correct. Treating those as broken would condemn one reference in eleven.
    """
    for code in (200, 202, 301, 302, 303, 307, 308, 401, 403, 418):
        assert code in resolve.ACCEPTED, code
    for code in (404, 410, 500):
        assert code not in resolve.ACCEPTED, code


def t_resolve_extracts_only_identifier_bearing_definitions():
    """A reference block mixes specifications and documentation with registered identifiers."""
    text = ("[research_a_2020]: https://doi.org/10.1000/abc\n"
            "[ref_spec]: https://example.org/spec.html\n"
            "[research_b_2021]: https://dx.doi.org/10.1000/xyz\n")
    got = resolve.identifiers(text)
    assert set(got) == {"research_a_2020", "research_b_2021"}, got


def t_resolve_sampling_requires_a_seed_and_is_reproducible():
    """AN UNSEEDED SAMPLE IS NOT A REPRODUCIBLE MEASUREMENT.

    A reviewer has to be able to check exactly which records were read. The seed is therefore
    required rather than defaulted, the same rule `gate.audit` follows.
    """
    text = "".join(f"[research_x{i}_2020]: https://doi.org/10.1000/{i}\n" for i in range(40))
    try:
        resolve.sweep(text, sample=5)
    except ValueError as e:
        assert "seed" in str(e), e
    else:
        raise AssertionError("sampling without a seed must raise")

    # No network in tests, so the SELECTION path is exercised rather than the sweep itself.
    import random
    anchors = sorted(resolve.identifiers(text))
    a = random.Random(11).sample(anchors, 3)
    b = random.Random(11).sample(anchors, 3)
    assert a == b, (a, b)


def t_resolve_summarise_reports_the_registry_only_fraction():
    """THE FIGURE A READER NEEDS IS HOW OFTEN CLICKING FAILS ON A CORRECT CITATION."""
    rows = [{"anchor": "a", "url": "u", "resolved": True, "route": "http", "status": 200},
            {"anchor": "b", "url": "u", "resolved": True, "route": "registry", "status": 404},
            {"anchor": "c", "url": "u", "resolved": False, "route": "", "status": 404}]
    s = resolve.summarise(rows)
    assert s["total"] == 3 and s["resolved"] == 2, s
    assert s["via_registry"] == 1 and abs(s["registry_only_fraction"] - 1 / 3) < 1e-9, s
    assert len(s["failed"]) == 1 and s["failed"][0]["anchor"] == "c", s




def t_clean_collapses_a_repeated_comma_from_a_registry_title():
    """`, ,` IS A REGISTRY ARTEFACT AND NO TITLE LEGITIMATELY CARRIES ONE.

    A harvested title reached a draft reading "Col, Demler of A, E, C, , Washington", where an
    abbreviation full stop had already become a comma and the empty field between two of them
    rendered as a bare `, ,` in the visible reference entry.
    """
    got = refs.clean("Col, Demler of A, E, C, , Washington, Col,")
    assert ", ," not in got, got
    assert ",," not in got, got
    # an ordinary comma list must survive untouched
    assert refs.clean("Smith, Jones and Brown") == "Smith, Jones and Brown"




def t_gate_refuses_a_dictionary_headword_but_keeps_a_short_real_title():
    """A SUBJECT TEST IS NOT A SUBSTANCE TEST.

    An Oxford English Dictionary entry titled `compiler, n.` passes every
    computing anchor perfectly, because the title IS the anchor. Six such
    records reached two published articles. The rule must stay narrow, since
    `Garbage Collection` and `Abstract Interpretation` are real paper titles.
    """
    assert gate.substance_reason("compiler, n.")
    assert gate.substance_reason("sandboxing, n")
    assert gate.substance_reason("Unboxed", "Unboxed")
    assert gate.substance_reason("") 
    assert gate.substance_reason("Garbage Collection") is None
    assert gate.substance_reason("Abstract Interpretation") is None
    assert gate.substance_reason("Region-Based Memory Management",
                                 "Information and Computation") is None


def t_gate_select_refuses_no_substance_before_testing_the_subject():
    """A record that is not a work should be refused for that reason."""
    g = gate.Gate([r"\bcompiler"], name="t")
    recs = [{"title": "compiler, n.", "venue": "Oxford English Dictionary"},
            {"title": "A verified compiler back-end", "venue": "JAR"}]
    kept, dropped = gate.select(recs, g)
    assert len(kept) == 1 and kept[0]["title"].startswith("A verified"), kept
    assert len(dropped) == 1 and "no substance" in dropped[0][1], dropped


def t_homonym_store_reaches_anchor_keyed_rejections_at_harvest_time():
    """THREE QUARTERS OF THE STORE WAS INERT BEFORE THIS.

    550 of 728 rejections are keyed by anchor, but `filter_records` runs at
    harvest time where a record has a digital object identifier and no anchor,
    so those entries could never match. The prospective stem is now derived.
    """
    sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(
        os.path.abspath(__file__))), "_research"))
    import homonyms
    homonyms._self_test()


def t_title_lead_strips_accession_prefixes():
    """A339: an abstracting service's accession number became reader-visible link text.

    Crossref passes through the prefix that abstracting services and patent registries put
    on the title field. Where the same record carries no Latin-script author, the label
    falls back to the opening words of the title and the accession number leads it. A339
    harvested 33 in one pool, giving labels such as "98/02419 Effects of launch 1998" and
    "5451015 Crashworthy composite aircraft 1996".

    THE FIRST FIX BROKE A LEGITIMATE TITLE. Stripping digits before any capital turned
    "3D printing" into "D printing", so the rule requires a lowercase letter after the
    capital, which is what distinguishes a glued word from a leading initialism.
    """
    assert refs.title_lead("98/02419 Effects of launch") == "Effects of launch"
    assert refs.title_lead("5451015 Crashworthy composite") == "Crashworthy composite"
    assert refs.title_lead("1162. Design of altitude") == "Design of altitude"
    assert refs.title_lead("4 Launch Vehicles") == "Launch Vehicles"
    assert refs.title_lead("85Chapter 6 Tutorial") == "Chapter 6 Tutorial"
    assert refs.title_lead("13Design and evaluation") == "Design and evaluation"

    # A LEADING NUMBER THAT BELONGS TO THE TITLE SURVIVES.
    assert refs.title_lead("3D printing of nozzles") == "3D printing of nozzles"
    assert refs.title_lead("2D flow past a cylinder") == "2D flow past a cylinder"
    assert refs.title_lead("Ordinary title") == "Ordinary title"

    # Both label paths use it, and neither may reintroduce the prefix.
    assert refs.display([], "1998", "98/02419 Effects of launch vehicle emissions") == \
        "Effects of launch vehicle 1998"
    assert refs.anchor_stem([], "1998", "98/02419 Effects of launch") == \
        "research_effects_of_1998"

    # `clean` MUST NOT ACQUIRE THIS BEHAVIOUR. A full title keeps its leading number,
    # because only the shortened label needs the prefix gone.
    assert refs.clean("1162. Design of altitude").startswith("1162"), \
        "title_lead leaked into clean, which would rewrite full reference text"


def t_refs_display_normalises_a_shouted_title():
    """The 2026-08-14 audit fixed 3,564 shouted titles BY HAND and A342 harvested more.

    `display` already lowered all-capitals AUTHOR names. Its no-author branch,
    which falls back to the first words of the title, did not, so a publisher
    shouting its own title produced shouted link text. A sweep repairs the corpus
    once; the next harvest reintroduces the defect. Hence the library.

    THE HARD PART IS NOT SHOUTING, IT IS TELLING AN INITIALISM FROM A WORD.
    `IFAC` and `ON` are the same length, so the decision is taken on the whole
    string first and only then word by word.
    """
    assert refs.decap("2nd IFAC CONFERENCE ON INTELLIGENT AUTONOMOUS VEHICLES") == \
        "2nd IFAC Conference on Intelligent Autonomous Vehicles"
    assert refs.display([], "1995", "2nd IFAC CONFERENCE ON INTELLIGENT AUTONOMOUS") == \
        "2nd IFAC Conference on 1995"

    # ORDINARY TITLE CASE CARRYING INITIALISMS MUST BE LEFT EXACTLY AS SET.
    ordinary = "Volume 5: OGC CDB Radar Cross Section (RCS) Models"
    assert refs.decap(ordinary) == ordinary
    assert refs.decap("A NASA study of the X-15 airframe") == \
        "A NASA study of the X-15 airframe"
    assert refs.decap("Fan-out: measuring human control of multiple robots") == \
        "Fan-out: measuring human control of multiple robots"

    # An all-capitals author name was already handled and must stay handled.
    assert refs.display(["SMITH"], "2004", "anything") == "Smith 2004"

    # A title with no letters at all must not raise.
    assert refs.decap("1962") == "1962"
    assert refs.decap("") == ""


for name, fn in sorted(list(globals().items())):
    if name.startswith("t_") and callable(fn):
        check(name[2:], fn)

ok = sum(1 for p, _, _ in RESULTS if p)
for passed, name, detail in RESULTS:
    if not passed:
        print(f"  FAIL  {name}: {detail}")
print(f"{ok}/{len(RESULTS)} passed")
sys.exit(0 if ok == len(RESULTS) else 1)
