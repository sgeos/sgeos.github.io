#!/usr/bin/env python3
"""Regression tests for the source database and its generated References sections.

Run with `python3 _lib/test_sources.py`. No framework and no files written,
matching `test_lib.py`. Each case names the defect or the rule it guards.
"""

import copy
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sources as S  # noqa: E402
import sources_import as SI  # noqa: E402

RESULTS = []
SKIPPED = []
# Temporary files go under the project's tmp/, never the system temporary directory.
_SCRATCH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "tmp")
os.makedirs(_SCRATCH, exist_ok=True)


def check(name, fn):
    try:
        fn()
        RESULTS.append((True, name, ""))
    except Exception as e:  # noqa: BLE001  a test harness reports every failure
        RESULTS.append((False, name, f"{type(e).__name__}: {e}"))


def raises(fn, fragment):
    try:
        fn()
    except S.SourceError as e:
        assert fragment in str(e), f"wrong error: {e}"
        return
    raise AssertionError(f"expected SourceError containing {fragment!r}")


VENUES = {
    "Icarus": {"venue": "Icarus", "peer_reviewed": True, "checked": True, "basis": "test",
               "evidence": {"url": "https://example.org/policy", "quote": "Every paper is refereed.",
                            "read": "2026-10-24", "method": "fetched"}},
    "Meeting": {"venue": "Meeting", "peer_reviewed": False, "checked": False, "basis": "test"},
}


def journal(anchor="research_doe_2020", **kw):
    r = {"anchor": anchor, "kind": "journal-article", "doi": "10.1/x", "title": "A Title",
         "authors": [{"family": "Doe", "given": "Jane"}], "year": 2020, "container": "Icarus",
         "venue": "Icarus", "volume": "141", "issue": "2", "pages": "179-193"}
    r.update(kw)
    r["rule"], r["section"] = S.classify(r, VENUES)
    return r


# ----------------------------------------------------------- formatting rules

def t_page_range_published_examples():
    """Chicago's abbreviation, including the cases that keep every digit."""
    for x, w in [("471-485", "471–85"), ("101-108", "101–8"), ("321-328", "321–28"), ("498-532", "498–532"),
                 ("1496-1504", "1496–1504"), ("100-104", "100–104"), ("39-54", "39–54"), ("1103-1104", "1103–4")]:
        assert S.page_range(x) == w, (x, S.page_range(x), w)


def t_page_range_article_number_passes_through():
    assert S.page_range("L01706") == "L01706"


def t_authors_up_to_six_named_more_take_three():
    """13.23 and 13.78 in the 18th edition."""
    people = [{"family": f"F{i}", "given": f"G{i}"} for i in range(7)]
    assert S.author_list(people[:6]) == "F0, G0, G1 F1, G2 F2, G3 F3, G4 F4, and G5 F5"
    assert S.author_list(people) == "F0, G0, G1 F1, G2 F2, et al."
    assert S.author_list(people[:2]) == "F0, G0, and G1 F1"


def t_cite_label_names_two_then_et_al():
    """In the text, two authors are named and three or more take et al."""
    two = journal(authors=[{"family": "Kopp"}, {"family": "Lean"}])
    three = journal(authors=[{"family": "Kulkarni"}, {"family": "Lubin"}, {"family": "Zhang"}])
    assert S.cite_label(two) == "Kopp and Lean"
    assert S.cite_label(three) == "Kulkarni et al."


def t_organisation_author_carries_its_expansion():
    org = [{"name": "National Aeronautics and Space Administration", "short": "NASA"}]
    assert S.author_list(org) == "NASA (National Aeronautics and Space Administration)"


def t_initial_does_not_double_the_period():
    """`Ercol, C.` must not become `Ercol, C.. 2007`."""
    r = journal(authors=[{"family": "Ercol", "given": "C."}])
    assert ".." not in S.entry(r)


def t_title_question_mark_takes_no_period():
    r = journal(title="Is Mercury Hot?")
    assert '"Is Mercury Hot?"' in S.entry(r) and '?."' not in S.entry(r)


def t_issue_range_takes_en_dash():
    assert "(1–2)" in S.entry(journal(issue="1-2"))


def t_wikipedia_entry_pins_revision_and_omits_repeated_year():
    r = SI.record_from_wikipedia("ref_mercury", "Mercury (planet)", 1381089194, "2026-10-19T23:34:46Z")
    r["rule"], r["section"] = S.classify(r, VENUES)
    S.validate_record(r, VENUES)
    e = S.entry(r)
    assert e.startswith('"Mercury (Planet)." 2026. Wikipedia. Last modified October 19, at 23:34 (UTC).'), e
    assert "oldid=1381089194" in e


# --------------------------------------------------------------- escaping

def t_registry_text_cannot_inject_markup():
    """Titles come from untrusted registries. Nothing in one may open markup."""
    evil = "[x](javascript:alert(1)) *b* _i_ `c` <script> {% raw %} $$x$$ | #"
    out = S.md_escape(evil)
    for ch in "[]*_`<{}$|#":
        assert not re.search(r"(?<!\\)" + re.escape(ch), out), (ch, out)


# ------------------------------------------------------------ headline case

def t_headline_case_keeps_acronyms_and_lowers_minor_words():
    for t, w in [("TRAPPIST-1", "TRAPPIST-1"), ("MESSENGER", "MESSENGER"),
                 ("Geodetic evidence that Mercury has A solid inner core",
                  "Geodetic Evidence That Mercury Has a Solid Inner Core"),
                 ("The first naked-eye superflare", "The First Naked-Eye Superflare"),
                 ("BepiColombo - Mission overview", "BepiColombo: Mission Overview"),
                 ("Where to go: up or down?", "Where to Go: Up or Down?")]:
        assert SI.headline_case(t) == w, (t, SI.headline_case(t), w)


def t_given_names_spaced_initials_and_suffix():
    assert SI._given("A.J.") == "A. J."
    assert SI._given("H") == "H."
    assert SI._family("McNutt, Jr.") == "McNutt Jr."


# --------------------------------------------------------- classification

def t_unestablished_venue_is_not_peer_reviewed():
    """Default deny. A proceedings whose full-paper review is unknown is not credited with it."""
    r = journal(kind="proceedings-paper", venue="Meeting", container="Meeting")
    assert S.classify(r, VENUES) == (4, "Primary Sources, Non-Peer-Reviewed")
    unknown = journal(venue="Nowhere")
    assert S.classify(unknown, VENUES)[1] == "Primary Sources, Non-Peer-Reviewed"


def t_review_in_refereed_journal_is_secondary():
    assert S.classify(journal(synthesis=True), VENUES) == (3, "Secondary Sources")


def t_web_page_with_stake_is_commercial():
    page = {"kind": "web-page", "stake": True}
    assert S.classify(page, VENUES) == (6, "Commercial Sources")
    assert S.classify({"kind": "web-page"}, VENUES) == (7, "General Sources")


# -------------------------------------------------------------- validation

def t_validation_rejects_unknown_field():
    r = journal(colour="blue")
    raises(lambda: S.validate_record(r, VENUES), "unknown field")


def t_validation_rejects_section_the_rules_do_not_give():
    r = journal()
    r["section"] = "Secondary Sources"
    raises(lambda: S.validate_record(r, VENUES), "the rules give")


def t_validation_rejects_unpinned_wikipedia():
    r = SI.record_from_wikipedia("ref_moon", "Moon", 5, "2026-10-20T15:52:43Z")
    r["rule"], r["section"] = S.classify(r, VENUES)
    r["url"] = "https://en.wikipedia.org/wiki/Moon"
    raises(lambda: S.validate_record(r, VENUES), "must pin oldid")


def t_validation_rejects_placeholder_pages():
    """Kopp and Lean 2011 arrived from Crossref with pages `n/a-n/a`."""
    raises(lambda: S.validate_record(journal(pages="n/a-n/a"), VENUES), "placeholder")


def t_alias_claimed_twice_is_rejected():
    a = journal("research_a_2020", aliases=["research_old"])
    b = journal("research_b_2020", aliases=["research_old"])
    raises(lambda: S.resolve_index({"research_a_2020": a, "research_b_2020": b}), "resolves to both")


# -------------------------------------------------------------- generation

ARTICLE = """---
title: "T"
---

Body cites [Doe 2020][research_doe_2020] and [Roe 2020][research_old_roe].

## References

- legacy
"""


def _records():
    doe = journal()
    roe = journal("research_roe_2020", authors=[{"family": "Roe"}], aliases=["research_old_roe"],
                  doi="10.1/y")
    return {"research_doe_2020": doe, "research_roe_2020": roe}


def t_generated_section_orders_and_defines_aliases():
    recs = _records()
    out = S.generate(ARTICLE, recs, VENUES)
    assert out.startswith("## References\n\n" + S.MARKER), out[:120]
    assert out.index("- Doe") < out.index("- Roe")
    # The alias the body uses and the canonical anchor the entry uses are both defined.
    assert "[research_old_roe]: https://doi.org/10.1/y" in out
    assert "[research_roe_2020]: https://doi.org/10.1/y" in out


def t_hand_edit_to_generated_section_is_caught():
    recs = _records()
    body = ARTICLE.split("## References\n")[0]
    good = body + S.generate(ARTICLE, recs, VENUES)
    assert S.check_text(good, recs, VENUES) == [], S.check_text(good, recs, VENUES)
    tampered = good.replace("A Title", "A Different Title", 1)
    assert any("differs from the database" in e for e in S.check_text(tampered, recs, VENUES))


def t_wrong_in_text_label_is_caught():
    recs = _records()
    text = ARTICLE.replace("[Doe 2020]", "[Doe and Others 2020]")
    body = text.split("## References\n")[0]
    full = body + S.generate(text, recs, VENUES)
    assert any("should read [Doe 2020]" in e for e in S.check_text(full, recs, VENUES))


def t_uncited_database_anchor_is_an_error():
    text = ARTICLE.replace("[research_doe_2020]", "[research_missing_2020]")
    raises(lambda: S.generate(text, _records(), VENUES), "not in the database")


def t_same_label_same_year_takes_suffixes():
    """13.114. Two Doe 2020 works become 2020a and 2020b, ordered by title."""
    a = journal("research_doe_2020", title="Beta")
    b = journal("research_doe_2020b", title="Alpha", doi="10.1/z")
    suf = S.year_suffixes([a, b])
    assert suf == {"research_doe_2020b": "a", "research_doe_2020": "b"}, suf


def t_unconverted_article_is_not_checked():
    assert S.check_text(ARTICLE, _records(), VENUES) == []



# ------------------------------------------------- peer review must be verified

def _venue(**kw):
    v = copy.deepcopy(VENUES["Icarus"])
    v.update(kw)
    return v


def t_peer_review_without_fetched_evidence_is_refused():
    """The pilot's rule of 2026-10-24: peer review is credited only when verified."""
    raises(lambda: S.validate_venue(_venue(checked=False)), "requires checked")
    no_ev = _venue()
    no_ev.pop("evidence")
    raises(lambda: S.validate_venue(no_ev), "requires evidence")
    snip = _venue()
    snip["evidence"] = dict(snip["evidence"], method="snippet")
    raises(lambda: S.validate_venue(snip), "requires evidence fetched")
    raises(lambda: S.validate_venue(_venue(evidence={"url": "x"})), "exactly url, quote, read and method")
    raises(lambda: S.validate_venue(_venue(colour="red")), "unknown venue field")


def t_unverified_journal_falls_to_non_peer_reviewed():
    """A venue marked peer-reviewed but unchecked is not credited, even if a hand edit skips validation."""
    venues = {"Icarus": _venue(checked=False)}
    r = journal()
    assert S.classify(r, venues) == (4, "Primary Sources, Non-Peer-Reviewed")


def t_evidence_start_year_is_enforced():
    """Nature mandated review only from 1973, so a 1972 paper is not credited."""
    venues = {"Icarus": _venue(since=1973)}
    assert S.classify(journal(year=1972), venues)[1] == "Primary Sources, Non-Peer-Reviewed"
    assert S.classify(journal(year=1973), venues)[1] == "Primary Sources, Peer-Reviewed"
    raises(lambda: S.validate_venue(_venue(since="1973")), "since must be a year")


def t_review_in_unverified_venue_stays_secondary():
    """Secondary is about synthesis, so an unverified venue moves a review to rule 5, not rule 4."""
    venues = {"Icarus": _venue(peer_reviewed=False, checked=False)}
    assert S.classify(journal(synthesis=True), venues) == (5, "Secondary Sources")


def t_store_credits_no_venue_without_fetched_evidence():
    """The stored venue table itself obeys the rule."""
    for v in S.load_venues().values():
        S.validate_venue(v)
        if v["peer_reviewed"]:
            assert v["evidence"]["method"] == "fetched", v["venue"]


# ------------------------------------------------------------- import

def t_decisions_refuse_two_notes_for_one_record():
    import tempfile
    with tempfile.NamedTemporaryFile("w", suffix=".toml", delete=False, dir=_SCRATCH) as fh:
        fh.write('article = "A1"\ncrossref_cache = "c"\nwiki_pins = "p"\n'
                 '[note]\nresearch_x = "one"\n[synthesis]\nresearch_x = "two"\n')
    try:
        raises(lambda: SI.load_decisions(fh.name), "write one note")
    finally:
        os.remove(fh.name)


def t_decisions_refuse_unknown_fields():
    import tempfile
    with tempfile.NamedTemporaryFile("w", suffix=".toml", delete=False, dir=_SCRATCH) as fh:
        fh.write('article = "A1"\ncrossref_cache = "c"\nwiki_pins = "p"\n'
                 '[fix.research_x]\nnote = "n"\nset = { colour = "red" }\n')
    try:
        raises(lambda: SI.load_decisions(fh.name), "unknown fields")
    finally:
        os.remove(fh.name)


def t_import_never_credits_a_new_venue():
    """A venue first met at import is added as not established, so its paper falls to rule 4."""
    import json
    import shutil
    import tempfile
    d = tempfile.mkdtemp(dir=_SCRATCH)
    try:
        post_path = os.path.join(d, "post.markdown")
        with open(post_path, "w") as fh:
            fh.write("[research_doe_2020]: https://doi.org/10.1/x\n")
        cache = os.path.join(d, "cr")
        os.makedirs(cache)
        msg = {"DOI": "10.1/x", "type": "journal-article", "title": ["A test"],
               "author": [{"family": "Doe", "given": "Jane"}], "issued": {"date-parts": [[2020]]},
               "container-title": ["Brand New Journal"], "publisher": "P"}
        with open(SI.crossref_cache_path(cache, "10.1/x"), "w") as fh:
            json.dump(msg, fh)
        pins = os.path.join(d, "pins.json")
        with open(pins, "w") as fh:
            fh.write("{}")
        recs, new = SI.import_post(post_path, {"article": "T", "crossref_cache": cache, "wiki_pins": pins}, {})
        assert set(new) == {"Brand New Journal"} and new["Brand New Journal"]["peer_reviewed"] is False
        assert recs["research_doe_2020"]["section"] == "Primary Sources, Non-Peer-Reviewed"
        raises(lambda: SI.import_post(post_path, {"article": "T", "crossref_cache": d, "wiki_pins": pins}, {}),
               "not in the Crossref cache")
    finally:
        shutil.rmtree(d)


def t_merge_reports_conflicts_and_keeps_store():
    store = {"a": {"anchor": "a", "title": "Old"}}
    merged, added, same, conflicts = SI.merge(store, {"a": {"anchor": "a", "title": "New"},
                                                       "b": {"anchor": "b"}})
    assert added == ["b"] and conflicts == ["a"] and merged["a"]["title"] == "Old", (added, conflicts)
    merged, *_ = SI.merge(store, {"a": {"anchor": "a", "title": "New"}}, replace=True)
    assert merged["a"]["title"] == "New"


def t_a384_import_reproduces_the_store():
    """GOLDEN, LOCAL ONLY. Rebuilding A384 from its decision file gives its stored records exactly.

    The registry caches it reads are gitignored scratch, so on a checkout without
    them this test is reported as skipped rather than passed.
    """
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    dec = os.path.join(root, "_sources", "decisions", "A384.toml")
    d = SI.load_decisions(dec)
    if not os.path.isdir(os.path.join(root, d["crossref_cache"])):
        SKIPPED.append("a384_import_reproduces_the_store")
        return
    cwd = os.getcwd()
    os.chdir(root)
    try:
        drafts, new_venues = SI.import_post("_posts/2026-08-20-mercury_as_colony_and_launch_site.markdown",
                                            d, S.load_venues())
    finally:
        os.chdir(cwd)
    store = S.load_records()
    _, added, same, conflicts = SI.merge(store, drafts)
    assert not added and not conflicts and not new_venues and len(same) == 99, (added, conflicts)


for name, fn in sorted(list(globals().items())):
    if name.startswith("t_") and callable(fn):
        check(name[2:], fn)

ok = sum(1 for p, _, _ in RESULTS if p)
for passed, name, detail in RESULTS:
    if not passed:
        print(f"  FAIL  {name}: {detail}")
print(f"{ok}/{len(RESULTS)} passed" + (f", of which {len(SKIPPED)} skipped for missing local data: "
                                         f"{', '.join(SKIPPED)}" if SKIPPED else ""))
sys.exit(0 if ok == len(RESULTS) else 1)
