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
               "reviewers": "two independent referees chosen by the editor",
               "evidence": [{"url": "https://example.org/policy",
                             "quote": "Every paper goes to two independent referees chosen by the editor.",
                             "read": "2026-10-24", "method": "fetched"}]},
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
    # The entry links through the name the body uses, so the article's own names
    # are the only definitions, and an alias does not drag in the canonical one.
    assert "[research_old_roe]: https://doi.org/10.1/y" in out
    assert "][research_old_roe]" in out.split("\n[")[0] or "][research_old_roe]\n" in out
    assert "[research_roe_2020]:" not in out


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


def t_shared_store_and_index_give_the_same_result_and_stay_unchanged():
    """_verify.py now hands one store and one index to every article check, because
    reloading them per post took the CI verify step from 0.2 to about 50 minutes. That
    is only sound if a check neither changes them nor answers differently with them."""
    recs = _records()
    body = ARTICLE.split("## References\n")[0]
    good = body + S.generate(ARTICLE, recs, VENUES)
    bad = good.replace("[Doe 2020]", "[Doe and Others 2020]")
    before = copy.deepcopy(recs)
    index = S.resolve_index(recs)
    index_before = dict(index)
    for text in (good, bad, good):
        assert S.check_text(text, recs, VENUES, index=index) == S.check_text(text, recs, VENUES)
    assert S.check_text(good, recs, VENUES, index=index) == []
    assert S.check_text(bad, recs, VENUES, index=index), "a wrong label passed with a shared index"
    assert recs == before and index == index_before
    assert S.article_index(recs, None, index) is not index


def t_front_matter_cache_rereads_an_edited_file():
    """Front matter is cached by file version, so a post edited mid-run is read again."""
    import tempfile
    with tempfile.NamedTemporaryFile("w", suffix=".markdown", delete=False, dir=_SCRATCH) as fh:
        fh.write('---\ntitle: "First"\ndate: 2020-01-01 00:00:00 +0000\ncategories: a b\n---\nText.\n')
    try:
        first = S._front_matter(fh.name)
        first["title"] = "changed by a caller"
        assert S._front_matter(fh.name)["title"] == "First"
        with open(fh.name, "w", encoding="utf-8") as g:
            g.write('---\ntitle: "Second title"\ndate: 2020-01-01 00:00:00 +0000\ncategories: a b\n---\nText.\n')
        assert S._front_matter(fh.name)["title"] == "Second title"
    finally:
        os.remove(fh.name)


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
    snip["evidence"] = [dict(snip["evidence"][0], method="snippet")]
    raises(lambda: S.validate_venue(snip), "requires evidence fetched")
    raises(lambda: S.validate_venue(_venue(evidence=[{"url": "x"}])), "exactly url, quote, read and method")
    raises(lambda: S.validate_venue(_venue(evidence={"url": "x"})), "must be a list")


def t_peer_review_must_say_by_whom():
    """The pilot's test of 2026-10-24: reviewed by whom? Without an answer the basis is lacking."""
    v = _venue()
    v.pop("reviewers")
    raises(lambda: S.validate_venue(v), "answer to by whom")
    assert S.classify(journal(), {"Icarus": v})[1] == "Primary Sources, Non-Peer-Reviewed"
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
            assert v["reviewers"] and any(e["method"] == "fetched" for e in v["evidence"]), v["venue"]


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
               "in neither registry cache")
    finally:
        shutil.rmtree(d)


def t_merge_keeps_corrections_of_a_known_source():
    """A382 re-derived Kopp and Lean 2011 from Crossref with placeholder pages A384 had corrected."""
    store = {"a": {"anchor": "a", "doi": "10.1/x", "pages": "L01706"}}
    merged, added, known, conflicts, ext, amap = SI.merge(
        store, {"a": {"anchor": "a", "doi": "10.1/X", "pages": "n/a-n/a"}, "b": {"anchor": "b", "doi": "10.1/y"}})
    assert added == ["b"] and known == ["a"] and not conflicts and merged["a"]["pages"] == "L01706"
    assert amap == {}


def t_merge_renames_a_different_source_under_a_taken_name():
    """research_smith_2020 can be two works in two articles; the store keeps both, the text keeps its name."""
    store = {"research_smith_2020": {"anchor": "research_smith_2020", "doi": "10.1/x"}}
    merged, added, _k, conflicts, _e, amap = SI.merge(
        store, {"research_smith_2020": {"anchor": "research_smith_2020", "doi": "10.1/other"}})
    assert not conflicts and len(added) == 1 and added[0].startswith("research_smith_2020_")
    assert merged["research_smith_2020"]["doi"] == "10.1/x" and merged[added[0]]["doi"] == "10.1/other"
    assert merged[added[0]]["anchor"] == added[0] and amap == {"research_smith_2020": added[0]}
    # The rename is a function of the source, so a second article reaches the same record.
    m2, a2, k2, _c, _e, amap2 = SI.merge(merged, {"research_smith_2020": {"anchor": "research_smith_2020",
                                                                          "doi": "10.1/other"}})
    assert a2 == [] and k2 == [added[0]] and amap2 == amap


def t_merge_maps_a_known_source_under_another_name():
    store = {"research_doe_2020": {"anchor": "research_doe_2020", "doi": "10.1/x"}}
    merged, added, known, _c, _e, amap = SI.merge(store, {"research_doe_jones_2020": {"anchor": "research_doe_jones_2020",
                                                                                     "doi": "10.1/x"}})
    assert added == [] and known == ["research_doe_2020"] and amap == {"research_doe_jones_2020": "research_doe_2020"}


def t_article_map_overlays_the_store():
    import shutil
    import tempfile
    d = tempfile.mkdtemp(dir=_SCRATCH)
    try:
        recs = {"research_x_2020": journal("research_x_2020"), "research_x_2020_ab12cd": journal("research_x_2020_ab12cd", doi="10.1/z")}
        S.save_article_map("2026-01-01-t", {"research_x_2020": "research_x_2020_ab12cd"}, d)
        S.ARTICLES, saved = d, S.ARTICLES
        try:
            idx = S.article_index(recs, "_posts/2026-01-01-t.markdown")
            assert idx["research_x_2020"] == ("research_x_2020_ab12cd", None)
            assert S.resolve_index(recs)["research_x_2020"] == ("research_x_2020", None)
        finally:
            S.ARTICLES = saved
    finally:
        shutil.rmtree(d)


def t_survey_entries_are_not_in_text_labels():
    body = "Prose [Doe 2020][research_doe_2020].\n\n- [Doe and others, 2020, A Title][research_doe_2020]\n"
    assert S.survey_entries(body) == {("Doe and others, 2020, A Title", "research_doe_2020")}


def t_clean_text_handles_double_escapes_and_breaks():
    assert S.clean_text("A Conference&amp;lt;BR&amp;gt; 18th Meeting") == "A Conference 18th Meeting"
    assert S.clean_text("Earth &amp;amp; Space") == "Earth & Space"


def t_edited_book_lists_its_editor():
    """With no author the editor leads the entry, the label and the sort."""
    r = {"anchor": "book_conway_2010", "kind": "book", "doi": "10.1017/x", "title": "Spacecraft Trajectory Optimization",
         "editors": [{"family": "Conway", "given": "Bruce A."}], "year": 2010, "publisher": "Cambridge University Press"}
    r["rule"], r["section"] = S.classify(r, {})
    S.validate_record(r, {})
    assert S.entry(r).startswith("Conway, Bruce A., ed. 2010. *Spacecraft Trajectory Optimization*."), S.entry(r)
    assert S.cite_label(r) == "Conway"



FIXTURE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "testdata", "sources")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
A384 = os.path.join(ROOT, "_posts", "2026-08-20-mercury_as_colony_and_launch_site.markdown")
# One of each kind the importer handles: a book, a journal article with a page
# correction, a review, an AIP proceedings paper with corrected authors, an AIAA
# meeting paper, an EGU abstract, a book chapter with a corrected container, a
# pinned Wikipedia article, and a related post with section locators.
FIXTURE_ANCHORS = {
    "book_mcinnes_1999", "research_kopp_lean_2011", "research_killen_et_al_2007",
    "research_benford_benford_2003", "research_lyman_et_al_2001", "research_lammer_et_al_2026",
    "research_solomon_et_al_2007", "ref_mercury", "related_post_mass_drivers",
    "related_post_mass_drivers_curvature", "related_post_mass_drivers_locked",
    "related_post_mass_drivers_parent", "related_post_mass_drivers_positioning",
}


def t_import_reproduces_stored_a384_records():
    """Re-importing representative A384 sources from committed registry data gives the store exactly.

    The Crossref records in `testdata/sources/` are real responses trimmed to
    the fields the importer reads, and the post is A384 itself, cut to the
    fixture's anchors. Every decision kind is exercised: a title, a note, a
    synthesis judgement and field fixes with set and drop.
    """
    import shutil
    import tempfile
    text = open(A384, encoding="utf-8").read()
    lines = [ln for ln in text.splitlines() if re.match(r"^\[([a-z0-9_]+)\]: ", ln)
             and re.match(r"^\[([a-z0-9_]+)\]", ln).group(1) in FIXTURE_ANCHORS]
    assert len(lines) == len(FIXTURE_ANCHORS), len(lines)
    d = tempfile.mkdtemp(dir=_SCRATCH)
    try:
        post_path = os.path.join(d, "post.markdown")
        with open(post_path, "w", encoding="utf-8") as fh:
            fh.write("\n".join(lines) + "\n")
        dec = SI.load_decisions(os.path.join(ROOT, "_sources", "decisions", "A384.toml"))
        dec = {k: ({a: v for a, v in dec[k].items() if a in FIXTURE_ANCHORS} if isinstance(dec[k], dict) else dec[k])
               for k in dec}
        dec["crossref_cache"] = os.path.join(FIXTURE, "crossref")
        dec["wiki_pins"] = os.path.join(FIXTURE, "pins.json")
        drafts, new_venues = SI.import_post(post_path, dec, S.load_venues())
    finally:
        shutil.rmtree(d)
    store = S.load_records()
    base = {a for a in FIXTURE_ANCHORS if a in store}
    assert set(drafts) == base and not new_venues, (sorted(set(drafts) ^ base), new_venues)
    for a in base:
        assert drafts[a] == store[a], (a, {k: (store[a].get(k), drafts[a].get(k))
                                           for k in set(store[a]) | set(drafts[a])
                                           if store[a].get(k) != drafts[a].get(k)})


def t_import_refuses_a_link_that_disagrees_with_its_pin():
    import json
    import shutil
    import tempfile
    d = tempfile.mkdtemp(dir=_SCRATCH)
    try:
        post_path = os.path.join(d, "post.markdown")
        with open(post_path, "w") as fh:
            fh.write("[ref_mercury]: https://en.wikipedia.org/w/index.php?title=Mercury_(planet)&oldid=1\n")
        raises(lambda: SI.import_post(post_path, {"article": "T", "crossref_cache": d,
                                                  "wiki_pins": os.path.join(FIXTURE, "pins.json")}, {}),
               "but is pinned to")
    finally:
        shutil.rmtree(d)


# ------------------------------------------------------- A380 to A383 conversion lessons

def t_embedded_revision_ids_pin_saved_rendered_pages():
    """A380 saved rendered HTML under hashed names; the page's own revision id is the pin."""
    import shutil
    import tempfile
    d = tempfile.mkdtemp(dir=_SCRATCH)
    try:
        open(os.path.join(d, "0b84bf99"), "w").write(
            '<html><script>RLCONF={"wgPageName":"Equity_carve-out","wgRevisionId":1292204263};</script></html>')
        open(os.path.join(d, "missing"), "w").write('{"wgPageName":"Split-off","wgRevisionId":0}')
        got = SI.saved_html_revisions([d])
        assert list(got.values()) == [(os.path.join(d, "0b84bf99"), "Equity_carve-out", 1292204263)], got
    finally:
        shutil.rmtree(d)


def t_legacy_labels_split_at_the_year():
    text = ("- [Research, Abarbanell, Bushee and Smith Raedy 2003, Institutional Investor Preferences][research_a_2003]\n"
            "- [Reference, Corporate Spin-off, Wikipedia][ref_corporate_spin_off]\n")
    got = SI.legacy_labels(text)
    assert got["research_a_2003"] == ("Abarbanell, Bushee and Smith Raedy 2003", "Institutional Investor Preferences")
    assert got["ref_corporate_spin_off"] == ("", "Corporate Spin-off")


def t_headline_case_registry_habits():
    """Each of these was a defect found reviewing A380 to A383."""
    assert SI.headline_case("Photon sails at α Centauri") == "Photon Sails at α Centauri"
    assert SI.headline_case("Solar sail technology\u2014A state of the art review") == \
        "Solar Sail Technology\u2014a State of the Art Review"
    assert SI.headline_case("China is a declining power\u2014and that's the problem") == \
        "China Is a Declining Power\u2014and That's the Problem"
    assert SI.headline_case("Can takeover losses explain Spin-Off gains?") == "Can Takeover Losses Explain Spin-Off Gains?"
    assert SI.headline_case("Polarimeter aboard the demonstrator") == "Polarimeter aboard the Demonstrator"
    assert SI.normalise_title("How many impulses/ques/") == "How many impulses?"
    assert SI.normalise_title("Ground-Based Astrometry\u2217") == "Ground-Based Astrometry"
    # Separately superscripted marks arrive spaced, and a designation in a title
    # set in capitals keeps its capitals. Prsa et al. 2016, found converting A369 on.
    assert SI.normalise_title("Resolution B3 * \u2020") == "Resolution B3"
    assert SI.headline_case("NOMINAL VALUES: RESOLUTION B3 * \u2020") == "Nominal Values: Resolution B3"


def t_registry_name_habits():
    assert SI._given("JAMES K.") == "James K." and SI._given("A. J.") == "A. J."
    assert SI._family("O^Neill") == "O'Neill"
    r = journal(authors=[{"family": "Sauer Jr.", "given": "C."}])
    assert S.entry(r).startswith("Sauer, C., Jr. 2020."), S.entry(r)
    assert S.cite_label(r) == "Sauer"


def t_magazine_features_are_general_sources():
    v = {"venue": "Physics Today", "peer_reviewed": False, "checked": True, "magazine": True, "basis": "test"}
    S.validate_venue(v)
    assert S.classify(journal(venue="Physics Today", container="Physics Today"), {"Physics Today": v}) == \
        (7, "General Sources")
    raises(lambda: S.validate_venue(dict(v, peer_reviewed=True, reviewers="x", evidence=[])), "magazine")


def t_a_later_decision_amends_a_stored_record():
    """A382 judged a stored Progress in Aerospace Sciences paper a synthesis; the store must hold it."""
    store = {"a": {"anchor": "a", "doi": "10.1/x", "title": "T"}}
    draft = {"a": {"anchor": "a", "doi": "10.1/x", "title": "T", "synthesis": True, "note": "a review"}}
    decided = SI.decided_fields({"synthesis": {"a": "a review"}})
    merged, _ad, known, _c, ext, _m = SI.merge(store, draft, decided=decided)
    assert ext == ["a"] and merged["a"]["synthesis"] is True and merged["a"]["note"] == "a review"
    merged, _ad, known, _c, ext, _m = SI.merge(store, draft)
    assert known == ["a"] and "synthesis" not in merged["a"], "an undecided difference amended the store"


def t_fix_labels_keeps_heading_and_locator():
    """The first version dropped the References heading, which this guards."""
    recs = {"research_doe_2020": journal(authors=[{"family": "Doe", "given": "J."}, {"family": "Roe", "given": "K."},
                                                    {"family": "Poe", "given": "L."}])}
    text = ("---\n---\nAs shown [Doe, Roe and Poe 2020, p. 4][research_doe_2020].\n\n## References\n\n"
            "[research_doe_2020]: https://doi.org/10.1/x\n")
    new, changes = S.fix_labels(text, recs)
    assert "[Doe et al. 2020, p. 4][research_doe_2020]" in new and "\n## References\n" in new, new
    assert changes == [("Doe, Roe and Poe 2020, p. 4", "Doe et al. 2020, p. 4")], changes


def t_unattributed_work_is_cited_by_short_title():
    r = journal(authors=[], title="Mass-Driver Reaction Engine as Shuttle Upper Stage", short_title="Mass-Driver Reaction Engine")
    assert S.cite_label(r) == "Mass-Driver Reaction Engine"
    text = "---\n---\nSee [Unattributed 2020][research_doe_2020].\n\n## References\n\n[research_doe_2020]: x\n"
    assert S.label_errors(text, {"research_doe_2020": r}) == [
        ("Unattributed 2020", "research_doe_2020", "Mass-Driver Reaction Engine 2020")]

# ------------------------------------------------------- A369 to A379: web sources and scale

def _meta(**kw):
    m = {"url": "https://warontherocks.com/x", "status": "read", "final_url": None, "doc_type": "web-article",
         "title": "Where the wargames weren't", "subtitle": None,
         "authors": [{"family": "Tetreau", "given": "Matthew"}], "publisher": "War on the Rocks",
         "container": "War on the Rocks", "date": "2023-09-22", "modified": None, "number": None, "doi": None,
         "evidence": "Where the Wargames Weren't", "notes": None}
    m.update(kw)
    return m


def t_web_article_in_a_periodical():
    r = SI.record_from_web("commentary_t_2023", "https://warontherocks.com/x", _meta(), "Commentary, Tetreau 2023, X",
                           {"periodical": True}, "2026-10-24")
    r["rule"], r["section"] = S.classify(r, {})
    assert r["section"] == "General Sources" and r["published"] == "2023-09-22"
    assert S.entry(r) == ('Tetreau, Matthew. 2023. "Where the Wargames Weren\'t." *War on the Rocks*, September 22. '
                          '[https://warontherocks.com/x][commentary_t_2023]'), S.entry(r)


def t_unread_page_falls_back_to_its_label_and_says_so():
    r = SI.record_from_web("commentary_m_2021", "https://www.foreignaffairs.com/x", _meta(status="paywalled", title=None),
                           "Commentary, Mastro and Scissors 2022, An Essay", {"stake": True}, "2026-10-24")
    assert r["authors"] == [{"family": "Mastro"}, {"family": "Scissors"}] and r["year"] == 2022
    assert "could not be read" in r["note"] and r["stake"] is True
    undated = SI.record_from_web("data_x", "https://x.org/y", None, "Data, Central Election Commission, Results Database",
                                 {}, "2026-10-24")
    assert "year" not in undated and undated["kind"] == "dataset"
    undated["rule"], undated["section"] = S.classify(undated, {})
    assert "n.d." in S.entry(undated), S.entry(undated)


def t_suffix_in_given_names_moves_to_family():
    r = SI.record_from_web("j", "https://tnsr.org/x", _meta(doc_type="report", authors=[
        {"family": "Ellis", "given": "James O., Jr."}]), "Journal, Ellis 2021, X", {}, "2026-10-24")
    assert r["authors"] == [{"family": "Ellis Jr.", "given": "James O."}], r["authors"]


def t_press_release_is_commercial_and_testimony_primary():
    pr = SI.record_from_web("p", "https://x.gov/p", _meta(doc_type="press-release"), "Government, X 2024, P", {}, "2026-10-24")
    tm = SI.record_from_web("t", "https://x.gov/t", _meta(doc_type="speech-or-testimony"), "Government, X 2024, T", {}, "2026-10-24")
    assert S.classify(pr, {})[1] == "Commercial Sources" and S.classify(tm, {})[1] == "Primary Sources, Non-Peer-Reviewed"


def t_domain_rules_need_reasons_and_match_with_or_without_www():
    import tempfile
    with tempfile.NamedTemporaryFile("w", suffix=".toml", delete=False, dir=_SCRATCH) as fh:
        fh.write('["www.rand.org"]\nstake = true\n')
    try:
        raises(lambda: SI.load_domains(fh.name), "needs `why`")
    finally:
        os.remove(fh.name)
    assert SI.domain_rule("https://rand.org/x", {"www.rand.org": {"stake": True}}) == {"stake": True}
    assert SI.load_domains()["warontherocks.com"] == {"periodical": True}


def t_publisher_policy_credits_only_its_scope():
    pubs = [{"name": "ACM", "aliases": ["Association for Computing Machinery (ACM)"], "journals": True,
             "proceedings": False, "reviewers": "experts selected by editors", "basis": "test",
             "evidence": [{"url": "https://x", "quote": "q", "read": "2026-10-24", "method": "fetched"}]}]
    venues = {"J": {"venue": "J", "peer_reviewed": False, "checked": False, "basis": "b", "class": "journal",
                    "publisher": "Association for Computing Machinery (ACM)"},
              "P": {"venue": "P", "peer_reviewed": False, "checked": False, "basis": "b", "class": "proceedings",
                    "publisher": "ACM"},
              "M": {"venue": "M", "peer_reviewed": False, "checked": True, "magazine": True, "basis": "b",
                    "class": "journal", "publisher": "ACM"},
              "Own": {"venue": "Own", "peer_reviewed": False, "checked": False, "basis": "b", "class": "journal",
                      "publisher": "ACM", "evidence": [{"url": "u", "quote": "q", "read": "2026-10-24",
                                                        "method": "fetched"}]}}
    done = SI.credit_venues(venues, pubs)
    assert done == [("J", "ACM")], done
    S.validate_venue(venues["J"])
    assert venues["J"]["via"] == "ACM" and not venues["P"]["peer_reviewed"] and not venues["M"]["peer_reviewed"]


def t_openalex_record_prefers_the_location_carrying_the_doi():
    work = {"title": "On the soundness of coroutines with snapshots", "publication_year": 2018,
            "authorships": [{"raw_author_name": "Prokopec, Aleksandar"}, {"author": {"display_name": "Fengyun Liu"}}],
            "primary_location": {"source": {"type": "repository", "display_name": "arXiv"}},
            "locations": [{"landing_page_url": "https://doi.org/10.4230/LIPIcs.ECOOP.2018.3",
                           "source": {"type": "conference", "display_name": "ECOOP 2018"}}], "biblio": {}}
    r = SI.record_from_openalex("research_p_2018", work, "10.4230/LIPIcs.ECOOP.2018.3")
    assert r["kind"] == "proceedings-paper" and r["container"] == "ECOOP 2018"
    assert r["authors"] == [{"family": "Prokopec", "given": "Aleksandar"}, {"family": "Liu", "given": "Fengyun"}]


def t_crossref_year_is_the_first_publication_year():
    msg = {"DOI": "10.1/x", "type": "journal-article", "title": ["T"], "author": [{"family": "Doe", "given": "J."}],
           "issued": {"date-parts": [[2023, 5]]}, "published-print": {"date-parts": [[2024, 2]]},
           "container-title": ["J"], "publisher": "P"}
    assert SI.record_from_crossref("research_doe_2023", msg)["year"] == 2023


def t_failed_batches_are_halved_until_the_bad_doi_is_isolated():
    import fetch
    import shutil
    import tempfile
    calls = []

    def fake(dois, **kw):
        calls.append(len(dois))
        if "10.1/bad" in dois:
            return None
        return {d: {"DOI": d, "type": "journal-article"} for d in dois}
    d = tempfile.mkdtemp(dir=_SCRATCH)
    post = os.path.join(d, "p.markdown")
    open(post, "w").write("".join(f"[research_x_{i}]: https://doi.org/10.1/{i}\n" for i in range(7))
                          + "[research_bad]: https://doi.org/10.1/bad\n")
    real_b, real_s, real_o = fetch.crossref_works, fetch.crossref_work, fetch.openalex_work
    fetch.crossref_works, fetch.crossref_work, fetch.openalex_work = fake, (lambda d_, **k: None), (lambda d_, **k: None)
    try:
        dois, missing = SI.fetch_crossref(post, os.path.join(d, "crossref"))
    finally:
        fetch.crossref_works, fetch.crossref_work, fetch.openalex_work = real_b, real_s, real_o
        shutil.rmtree(d)
    assert missing == ["10.1/bad"] and len(dois) == 8, (missing, calls)
    assert len(calls) <= 2 * 8, calls

def t_series_policy_matches_by_venue_name():
    """SIGPLAN's policy covers its conferences whatever ACM's pages say; ACM's could not be read."""
    pubs = [p for p in SI.load_publishers() if p["name"] == "ACM SIGPLAN"]
    venues = {"Proceedings of the 41st ACM SIGPLAN Conference on Programming Language Design and Implementation":
              {"venue": "x", "peer_reviewed": False, "checked": False, "basis": "b", "class": "proceedings",
               "publisher": "ACM"},
              "Proceedings of the 2020 ACM Conference on Something": {"venue": "y", "peer_reviewed": False,
                                                                       "checked": False, "basis": "b",
                                                                       "class": "proceedings", "publisher": "ACM"}}
    done = SI.credit_venues(venues, pubs)
    assert [v for v, _p in done] == ["Proceedings of the 41st ACM SIGPLAN Conference on Programming Language Design and Implementation"]


def t_title_in_another_language_keeps_its_casing():
    """A German title gained English headline capitals, `Nur Ein Schlagwort?`. A377."""
    msg = {"DOI": "10.1007/bf1", "type": "journal-article", "language": "de",
           "title": ["Multiple Chemical Sensitivity \u2014 nur ein Schlagwort?"],
           "author": [], "issued": {"date-parts": [[2007]]}, "container-title": ["Allergo Journal"]}
    assert SI.record_from_crossref("research_x_2007", msg)["title"] == \
        "Multiple Chemical Sensitivity \u2014 nur ein Schlagwort?"
    msg["language"] = "en"
    assert SI.record_from_crossref("research_x_2007", msg)["title"] == \
        "Multiple Chemical Sensitivity \u2014 Nur Ein Schlagwort?"


def t_lncs_chapter_is_a_proceedings_paper_in_its_series():
    msg = {"DOI": "10.1007/978-3-030-1_2", "type": "book-chapter", "title": ["A paper"],
           "author": [{"family": "Doe", "given": "J."}], "issued": {"date-parts": [[2020]]},
           "container-title": ["Lecture Notes in Computer Science", "Trends in Functional Programming"],
           "publisher": "Springer International Publishing"}
    r = SI.record_from_crossref("research_doe_2020", msg)
    assert (r["kind"], r["venue"], r["container"]) == ("proceedings-paper", "Lecture Notes in Computer Science",
                                                       "Trends in Functional Programming"), r


def t_publishers_file_is_valid_and_fetched():
    for p in SI.load_publishers():
        assert p["reviewers"] and any(e["method"] == "fetched" for e in p["evidence"]), p["name"]

# ------------------------------------------------------- labels, names and refresh at survey scale

def t_citation_labels_are_names_then_a_year():
    """Links woven into prose end with a year too; only names-then-year is a citation."""
    for t in ("Kopp and Lean 2011", "Malhiac et al 2026", "de Moura and Ierusalimschy 2009", "Lopes and colleagues 2021",
              "National Bureau of Statistics of China 2025", "Sauer 1976, p. 3"):
        assert S.is_citation_label(t), t
    for t in ("Clausius in 1850", "section 5 of the Firearms Act 1968", "statistical communiqué on 2025", "2002",
              "inkwell", "the Low Level Virtual Machine compiler infrastructure"):
        assert not S.is_citation_label(t), t


def t_colliding_short_titles_take_suffixes():
    """Two DOIs of one chapter gave A377 a label naming two entries."""
    a = journal("research_death_by_2022", authors=[], title="Death by Perfume")
    b = journal("research_death_by_2022_b", authors=[], title="8. Death by Perfume")
    c = journal("research_other_2022", authors=[], title="Scented Visions")
    assert S.year_suffixes([a, b, c]) == {"research_death_by_2022_b": "a", "research_death_by_2022": "b"}, \
        S.year_suffixes([a, b, c])


def t_short_title_for_an_unattributed_work():
    assert S.short_title("Officers under Attack\u2014the Thin Blue Line") == "Officers under Attack"
    assert S.short_title("3. Longing for Luxury Perfume: A Nietzschean Interpretation") == "Longing for Luxury Perfume"
    assert S.short_title("Corpus Alienum (Cover the Perfume) in Cervix") == "Corpus Alienum Cover"
    assert S.short_title("Multiple Chemical Sensitivity \u2014 nur ein Schlagwort?") == "Multiple Chemical Sensitivity"
    assert S.short_title("Eau de Cologne \u2013 eklatant") == "Eau de Cologne"
    r = journal(authors=[], title="Environmental Illness: Multiple Chemical Sensitivity")
    assert S.cite_label(r) == "Environmental Illness"


def t_registry_name_habits_are_repaired():
    """Each case is a deposit habit found converting the X-Planes series, A297."""
    A = SI._authors
    assert A([{"family": "Binion", "given": "Jr"}, {"family": "T. W."}]) == [{"family": "Binion Jr.", "given": "T. W."}]
    assert A([{"family": "M. Jaffal", "given": "Hayder"}]) == [{"family": "Jaffal", "given": "Hayder M."}]
    assert A([{"family": "P", "given": "Nishanth"}]) == [{"family": "Nishanth", "given": "P."}]
    assert A([{"family": "CHEN", "given": "ZHIMING"}])[0]["family"] == "Chen"          # capitals are not initials
    assert A([{"family": "HAMILTON, II", "given": "H."}]) == [{"family": "Hamilton II", "given": "H."}]
    assert A([{"family": "Mc Kinney", "given": "R. L."}]) == [{"family": "McKinney", "given": "R. L."}]
    assert A([{"name": "US Naval Academy"}, {"family": "Juhasz", "given": "Ann"}]) == [{"family": "Juhasz", "given": "Ann"}]
    assert A([{"name": "McRuer."}, {"family": "McRuer", "given": "Duane"}]) == [{"family": "McRuer", "given": "Duane"}]
    assert A([{"family": "AIR FORCE FLIGHT TEST CENTER EDWARDS AFB CA"}]) == [
        {"name": "Air Force Flight Test Center Edwards AFB CA"}]                     # DTIC's corporate authors
    assert A([{"family": "Binion", "given": "T. W."}, {"family": "Jr"}]) == [{"family": "Binion Jr.", "given": "T. W."}]
    assert A([{"family": "Huang", "given": "X."}, {"family": "al", "given": "E"}]) == [{"family": "Huang", "given": "X."}]
    assert A([{"family": "II", "given": "J."}]) == []
    P = SI._person
    assert P("WATSON R.") == {"family": "Watson", "given": "R."}
    assert P("Garrison P Layton, Jr.") == {"family": "Layton Jr.", "given": "Garrison P."}
    assert P("John H. Del Frate") == {"family": "Del Frate", "given": "John H."}
    assert P("Kenneth W Mort (NASA retiree)") == {"family": "Mort", "given": "Kenneth W."}
    assert P("Langley Research Center") == {"name": "Langley Research Center"}
    assert P("Kevin Branch") == {"family": "Branch", "given": "Kevin"}               # a surname, not an office
    assert SI._people_from_label("Pisano van der Linden and Winter")[0] == [
        {"family": "Pisano"}, {"family": "van der Linden"}, {"family": "Winter"}]


def t_report_server_builders():
    """NTRS, OSTI and Open Library records, the X-Planes series' report servers."""
    j = {"stiType": "OTHER", "title": "TEST TECHNIQUES USED BY NASA FOR V/STOL MODELS",
         "authorAffiliations": [{"meta": {"author": {"name": "Kirby, R. H."},
                                          "organization": {"name": "NASA Langley Research Center"}}}],
         "publications": [{"publicationDate": "1964-03-01T00:00:00"}], "otherReportNumbers": ["Report Number: NASA-TN-D-2000"]}
    r = SI.record_from_ntrs("x", j, "19640007101")
    assert (r["kind"], r["year"], r["number"], r["publisher"]) == ("report", 1964, "NASA-TN-D-2000", "NASA"), r
    assert r["title"] == "Test Techniques Used by NASA for V/STOL Models", r["title"]
    j2 = {"stiType": "REPRINT", "title": "A paper", "authorAffiliations": [],
          "publications": [{"publicationName": "Journal of Aircraft", "volume": "54", "publicationDate": "2017-09-01"}]}
    assert SI.record_from_ntrs("y", j2, "1")["kind"] == "journal-article"
    o = {"title": "Report", "authors": ["Smith, J. [Lab, City, ST (United States)]"], "publication_date": "1960-01-01",
         "product_type": "Technical Report", "report_number": "ORNL-1; X", "research_orgs":
         ["Oak Ridge National Laboratory (ORNL), Oak Ridge, TN (United States)"]}
    r = SI.record_from_osti("z", o, "1")
    assert (r["number"], r["publisher"], r["authors"]) == ("ORNL-1", "Oak Ridge National Laboratory (ORNL)",
                                                           [{"family": "Smith", "given": "J."}]), r
    w = {"title": "Boundary-Layer Theory", "_author_names": ["Hermann Schlichting (Deceased)"],
         "_editions": [{"key": "/books/OL1M", "publish_date": "2016", "publishers": ["Springer"]},
                       {"key": "/books/OL2M", "publish_date": "1955", "publishers": ["McGraw-Hill"]}]}
    r = SI.record_from_openlibrary("b", w, "works/OL1W", 2017, "Schlichting and Gersten")
    assert r["year"] == 2017 and r["publisher"] == "Springer", r          # no 2017 edition: nearest one's publisher
    assert [a["family"] for a in r["authors"]] == ["Schlichting", "Gersten"], r["authors"]  # the label's authors
    assert SI.record_from_openlibrary("b", w, "works/OL1W", 1955, None)["publisher"] == "McGraw-Hill"


def t_label_forms_and_inferred_attributions():
    assert SI.split_label("Anderson 2002 Modern Compressible Flow") == ("Anderson", 2002, "Modern Compressible Flow")
    assert SI.split_label("National Museum of the United States Air Force, Martin RB-57D fact sheet, 2009") == (
        "National Museum of the United States Air Force", 2009, "Martin RB-57D fact sheet")
    assert SI.split_label("Civil Aircraft Sonic Boom, Final Rule, 38 FR 8051")[1] is None   # a page, not a year
    assert not SI._label_names_people("Aircraft Stability and Control", "Aircraft Stability & Control")
    m = SI._drop_inferred({"publisher": "Faircount Media Group", "authors": [{"family": "O'Rourke"}],
                           "notes": "Publisher Faircount Media Group inferred, not seen in fetch. Author likely O'Rourke, unverified."})
    assert m["publisher"] is None and m["authors"] == []
    r = SI.record_from_web("x", "https://a.example/b.pdf", {"status": "blocked"}, "Falcon HTV-2 fact sheet 2010", {}, "2026-10-24")
    assert (r["title"], r["authors"], r["year"]) == ("Falcon HTV-2 fact sheet", [], 2010)


def t_anchor_with_empty_name_part_has_a_shard():
    """The X-Planes harvest named works by non-Latin authors `research__2026`."""
    assert S.shard_of("research__2026") == "2" and S.shard_of("research_smith_2020") == "s"


def t_title_opening_label_is_a_citation():
    """The X-Planes surveys cited author-less harvest records by their title's opening words."""
    r = journal(title="Earth Oblateness in Terms of Satellite Orbits")
    assert S._title_label("Earth oblateness in terms 1959", r)
    assert not S._title_label("Clausius in 1850", r)
    assert not S._title_label("Earth 1959", r)         # too short to identify the work


def t_registry_placeholders_are_not_authors():
    """Wolters Kluwer deposits `&NA;` as a family name, which an entry printed as `&Na`."""
    assert SI._authors([{"family": "&NA;"}, {"family": "&NA;"}]) == []
    assert SI._authors([{"family": "Na", "given": "Li"}]) == [{"family": "Na", "given": "Li"}]


def t_affiliations_and_bylines_are_not_authors():
    got = SI._authors([{"name": "Department of Environmental Engineering, Daejeon University"},
                       {"name": "Formulaction, Inc."}, {"family": "KIM", "given": "J."}, {"name": "A Correspondent"}])
    assert got == [{"family": "Kim", "given": "J."}], got
    assert SI._authors([{"name": "Inter American Development Bank"}]) == [{"name": "Inter American Development Bank"}]
    assert SI._family("Tisserand,") == "Tisserand" and SI._family("Azuma*") == "Azuma"


def t_reprint_is_cited_by_its_original_year():
    r = journal(original_year=1972, year=1998)
    assert S.entry(r).startswith("Doe, Jane. (1972) 1998."), S.entry(r)
    text = "---\n---\nAs [Doe 1998][research_doe_2020] showed.\n\n## References\n\n[research_doe_2020]: x\n"
    assert S.label_errors(text, {"research_doe_2020": r}) == [("Doe 1998", "research_doe_2020", "Doe 1972")]


def t_refresh_rebuilds_only_unannotated_registry_records():
    store = {"a": {"anchor": "a", "doi": "10.1/x", "authors": [{"family": "KIM"}]},
             "b": {"anchor": "b", "doi": "10.1/y", "authors": [{"family": "Lang"}], "note": "fixed by hand"},
             "p": {"anchor": "p", "kind": "related-post", "post": "2026-01-01-x", "locators": {"p_a": "one"}}}
    drafts = {"a": {"anchor": "a", "doi": "10.1/x", "authors": [{"family": "Kim"}]},
              "b": {"anchor": "b", "doi": "10.1/y", "authors": []},
              "p": {"anchor": "p", "kind": "related-post", "post": "2026-01-01-x"}}
    merged, *_ = SI.merge(store, drafts, refresh=True)
    assert merged["a"]["authors"] == [{"family": "Kim"}]
    assert merged["b"]["authors"] == [{"family": "Lang"}], "a hand correction was refreshed away"
    assert merged["p"]["locators"] == {"p_a": "one"}, "a related post lost locators to refresh"


def t_prose_links_are_exempt_per_article():
    import shutil
    import tempfile
    d = tempfile.mkdtemp(dir=_SCRATCH)
    try:
        json_path = os.path.join(d, "2026-01-01-t.links.json")
        open(json_path, "w").write('["government_act_1948"]')
        S.ARTICLES, saved = d, S.ARTICLES
        try:
            assert S.load_prose_links("_posts/2026-01-01-t.markdown") == {"government_act_1948"}
        finally:
            S.ARTICLES = saved
    finally:
        shutil.rmtree(d)


def t_diff_labels_reports_substance_and_other_text():
    pre = "---\n---\nAs [Hanley and Lippman-Hand 1983][research_h] and [Doe and others 2020][research_d] said.\nX\n\n## References\n"
    post = "---\n---\nAs [Hanley 1983][research_h] and [Doe et al. 2020][research_d] said.\nY\n\n## References\n"
    changes, other = S.label_changes(pre, post)
    assert changes == [("research_h", "Hanley and Lippman-Hand 1983", "Hanley 1983")], changes
    assert [o[0] for o in other] == [4], other


def t_url_identifiers_are_read_from_links():
    import sources_resolve as SR
    cases = {
        "https://dl.acm.org/doi/abs/10.1145/3110268": ("doi", "10.1145/3110268"),
        "https://psycnet.apa.org/doiLanding?doi=10.1037%2Fh0054346": ("doi", "10.1037/h0054346"),
        "https://www.tandfonline.com/doi/full/10.1080/1/abstract": ("doi", "10.1080/1"),
        "https://www.jstor.org/stable/1968337": ("doi", "10.2307/1968337"),
        "https://www.nature.com/articles/nature14236": ("doi", "10.1038/nature14236"),
        "https://www.sciencedirect.com/science/article/abs/pii/0304405X77900150": ("doi", "10.1016/0304-405x(77)90015-0"),
        "https://www.sciencedirect.com/science/article/pii/S0890540184710935": ("pii", "S0890540184710935"),
        "https://www.cell.com/x/fulltext/S1364-6613(16)30126-7": ("pii", "S1364661316301267"),
        "https://arxiv.org/abs/2301.04104v2": ("arxiv", "2301.04104"),
        "https://global.oup.com/academic/product/x-9780195320442": ("isbn", "9780195320442"),
    }
    for url, want in cases.items():
        assert SR.url_identifier(url) == want, (url, SR.url_identifier(url))
    # A NUMBER THAT FAILS THE ISBN CHECK DIGIT is not an ISBN, so an article id is not read as one.
    assert SR.url_identifier("https://ieeexplore.ieee.org/document/6119585") is None
    assert SR.url_identifier("https://example.org/story/9780195320443") is None


def t_label_forms_are_parsed():
    import sources_resolve as SR
    lab = SR.parse_label("Curry, Haskell B. and Feys, Robert, Combinatory Logic, North-Holland, 1958")
    assert [p["family"] for p in lab["people"]] == ["Curry", "Feys"] and lab["title"] == "Combinatory Logic", lab
    assert lab["venue"] == "North-Holland" and lab["year"] == 1958 and lab["form"] == "full"
    lab = SR.parse_label("Yang, Vigor, Habiballah, Mohammed, Popp, Michael, and Hulka, James (editors), "
                         "Liquid Rocket Thrust Chambers, Aspects of Modeling, AIAA, 2004")
    assert len(lab["people"]) == 4 and lab["editors"] and lab["title"].startswith("Liquid"), lab
    lab = SR.parse_label("Brooks, Frederick P., Jr., The Mythical Man-Month, anniversary edition, Addison-Wesley, 1995")
    assert lab["people"] == [{"family": "Brooks Jr.", "given": "Frederick P."}] and lab["title"] == "The Mythical Man-Month"
    # TITLE, SURNAMES, YEAR, the A100 to A199 form, with a bracketed venue.
    lab = SR.parse_label("Are Self-Replicating Machines Feasible? (JBIS), Ellery, 2017", "future_x")
    assert lab["people"] == [{"family": "Ellery"}] and lab["venue"] == "JBIS" and lab["year"] == 2017, lab
    assert SR.parse_label("Curry, Haskell B. and Feys, Robert, Combinatory Logic, North-Holland, 1958")["form"] == "full"
    # A TITLE'S OWN `and` IS NO SECOND AUTHOR.
    lab = SR.parse_label("Baumol, William J., Productivity Growth, Convergence, and Welfare, What the Long-run "
                         "Data Show, American Economic Review 76, 1986")
    assert [p["family"] for p in lab["people"]] == ["Baumol"] and lab["title"].startswith("Productivity"), lab
    assert SR.parse_label("Boehm 1981")["people"] == [{"family": "Boehm"}]
    # A SECTION NUMBER IS NO YEAR.
    assert SI.split_label("NDAA Section 1709 of FY 2024")[1] == 2024
    assert [p["family"] for p in SR.parse_label("Bruner Goodnow Austin 1956 Study of Thinking")["people"]] == \
        ["Bruner", "Goodnow", "Austin"]
    # A `ref_` LABEL DESCRIBES, so its words are a title, never five surnames.
    lab = SR.parse_label("Commercial Space Launch Amendments Act 2004", "ref_csla_amendments_2004")
    assert lab["people"] == [] and lab["title"] == "Commercial Space Launch Amendments Act", lab
    assert len(SR.parse_label("Hopkins Alonso Adcock 1965", "research_hopkins_alonso_adcock_1965")["people"]) == 3
    # A DESCRIPTION names no people and no year.
    lab = SR.parse_label("Computer History Museum")
    assert lab["people"] == [] and lab["year"] is None and lab["form"] == "none"


def t_registry_records_must_agree_with_the_label():
    import sources_resolve as SR
    lab = SR.parse_label("Ahlstrom 1972 A Religious History of the American People")
    assert SR.agrees(lab, "A Religious History of the American People", ["Ahlstrom"], 1972, False)[0]
    # A SEARCH HIT by another author, or decades off, is not the work.
    assert not SR.agrees(lab, "A Religious History of the American People", ["Smith"], 1972, False)[0]
    assert not SR.agrees(lab, "A Religious History of the American People", ["Ahlstrom"], 1990, False)[0]
    # A LINK'S OWN IDENTIFIER may stand on author and year when the label has no title.
    lab = SR.parse_label("Boehm 1981")
    assert SR.agrees(lab, "Software Engineering Economics", ["Boehm"], 1981, True)[0]
    assert not SR.agrees(lab, "Software Engineering Economics", ["Boehm"], 1981, False)[0]
    assert not SR.agrees(lab, "Something Else", ["Jones"], 1981, True)[0]
    # AN ORGANISATION'S LABEL, `OpenAI 2019`, rests on the link's identifier and the exact year.
    lab = SR.parse_label("OpenAI 2019")
    assert SR.agrees(lab, "Solving Rubik's Cube with a Robot Hand", ["Akkaya", "Andrychowicz"], 2019, True)[0]
    assert not SR.agrees(lab, "Solving Rubik's Cube with a Robot Hand", ["Akkaya"], 2020, True)[0]
    assert not SR.agrees(lab, "Solving Rubik's Cube with a Robot Hand", ["Akkaya"], 2019, False)[0]
    # A SHORT TITLE agrees with the full title it opens; a colon written as a comma is no difference.
    assert SR.title_agrees("Study of Thinking", "A Study of Thinking")
    assert SR.title_agrees("Varieties of Capitalism, The Institutional Foundations",
                           "Varieties of Capitalism: The Institutional Foundations")
    assert SR.title_agrees("Why Nations Fail", "Why Nations Fail: The Origins of Power, Prosperity, and Poverty")
    assert not SR.title_agrees("The Reformation", "The Counter-Reformation in Europe")


def t_a_full_label_builds_a_full_entry():
    import sources_resolve as SR
    r = SR.record_from_label("book_church_calculi", "https://example.org/b",
                             "Church, Alonzo, The Calculi of Lambda-Conversion, Princeton University Press, 1941",
                             {}, "2026-10-25", "The page could not be read (no metadata)")
    assert r["kind"] == "book" and r["publisher"] == "Princeton University Press", r
    assert r["authors"] == [{"family": "Church", "given": "Alonzo"}] and r["year"] == 1941
    r = SR.record_from_label("paper_church_postulates", "https://example.org/p",
                             "Church, Alonzo, A Set of Postulates for the Foundation of Logic, Annals of Mathematics 33, 1932",
                             {}, "2026-10-25", "x")
    assert r["kind"] == "journal-article" and r["container"] == "Annals of Mathematics" and r["volume"] == "33", r
    r = SR.record_from_label("book_x", "https://example.org/e", "Edinburgh LCF, A Mechanised Logic, Springer, 1979",
                             {}, "2026-10-25", "x")
    assert r is None, "a label that names no people is not a full form"


def t_listed_works_the_prose_does_not_cite_are_kept():
    # A207 AND NINE X-PLANES ARTICLES lost every work their lists named and their prose
    # did not cite, 156 of them, because the generator kept only cited anchors.
    pre = ("---\n---\nSee [Smith 2001][research_smith_2001].\n\n## References\n\n"
           "- [Smith 2001 A Title][research_smith_2001]\n- [Jones 1999 Another][book_jones_1999]\n"
           "- [*Kinematic Machines*][book_freitas_ksrm], Robert A. Freitas Jr., Landes Bioscience, 2004\n\n"
           "[research_smith_2001]: https://example.org/a\n[book_jones_1999]: https://example.org/b\n"
           "[book_freitas_ksrm]: https://example.org/c\n")
    assert SI.listed_anchors(pre) == ["book_freitas_ksrm", "book_jones_1999"], SI.listed_anchors(pre)


def t_undated_entry_has_one_full_stop():
    # 77 POSTS PRINTED `n.d..`, the abbreviation's full stop doubled by the element's.
    r = {"anchor": "research_x", "kind": "report", "title": "A Report", "authors": [{"family": "Doe", "given": "J."}],
         "url": "https://example.org/r", "publisher": "X"}
    e = S.entry(r)
    assert "n.d.." not in e and "n.d. *A Report*" in e, e


def t_open_library_quirks_are_repaired():
    # A267 TO A276 BOOKS: a work listing its author twice, a title running into its
    # subtitle, and an imprint statement in the publisher's place.
    w = {"title": "From Puritan to Yankee Character and the Social Order",
         "subtitle": "Character and the Social Order in Connecticut, 1690-1765",
         "_author_names": ["Richard L. Bushman", "Richard L. Bushman"],
         "_editions": [{"key": "/books/OL1M", "publish_date": "1967", "publishers": [
             "Published for the Institute of Early American History and Culture by the University of North Carolina Press"]}]}
    r = SI.record_from_openlibrary("book_bushman_1967", w, "works/OL1W", 1967)
    assert r["title_published"] == "From Puritan to Yankee: Character and the Social Order in Connecticut, 1690-1765", r
    assert len(r["authors"]) == 1 and r["publisher"] == "University of North Carolina Press", r


def t_given_names_filed_as_family_are_swapped():
    # ELSEVIER DEPOSITED Huttenlocher 1979 as `{family: Peter R., given: Huttenlocher}`.
    assert SI._repair_people([{"family": "Peter R.", "given": "Huttenlocher"}]) == \
        [{"family": "Huttenlocher", "given": "Peter R."}]
    assert SI._repair_people([{"family": "Smith", "given": "John R."}]) == [{"family": "Smith", "given": "John R."}]


def t_works_sharing_a_link_stay_two_sources():
    # A262 LINKED Werbos 1987 and Barto et al. 1983 to one IEEE page; merged by URL
    # alone, relabelling rewrote `Werbos 1987` in the prose as the other paper.
    a = {"anchor": "a", "kind": "report", "url": "https://x.org/p", "year": 1987, "authors": [{"family": "Werbos"}]}
    b = {"anchor": "b", "kind": "report", "url": "https://x.org/p", "year": 1983, "authors": [{"family": "Barto"}]}
    assert SI.identity(a) != SI.identity(b)
    assert SI.identity(a) == SI.identity(dict(a, anchor="c", title="Another Spelling"))


def t_two_surnames_take_no_comma():
    assert S.author_list([{"family": "Astrahan"}, {"family": "Jacobs"}]) == "Astrahan and Jacobs"
    assert S.author_list([{"family": "Ward", "given": "Geoffrey C."}, {"family": "Burns", "given": "Ken"}]) == \
        "Ward, Geoffrey C., and Ken Burns"


def t_legacy_posts_are_normalised():
    import sources_resolve as SR
    text = ("---\n---\nSee [the guide][Android-Guide] and [it][ANDROID-GUIDE].\n\n## References:\n"
            "- [GitHub Pages](https://pages.github.com)\n- [Guide][Android-Guide]\n\n"
            "[Android-Guide]:    https://example.org/g\n[own]: https://sgeos.github.io/a/2016/01/08/x.html\n")
    out, notes = SR.normalise_legacy(text, {"/a/2016/01/08/x.html": "2016-01-08-x"}, {})
    assert "## References\n" in out and "## References:" not in out
    assert "[the guide][android_guide]" in out and "[it][android_guide]" in out, out
    assert "[android_guide]: https://example.org/g" in out
    assert "- [GitHub Pages][ref_github_pages]" in out and "[ref_github_pages]: https://pages.github.com" in out
    assert "[own]: {% post_url 2016-01-08-x %}" in out, out


def t_refresh_never_steps_down_in_source():
    page = {"anchor": "ref_p", "kind": "web-page", "url": "https://x.org/p", "title": "14 CFR Part 450",
            "authors": [], "accessed": "2026-10-25", "note": "Read from the Internet Archive capture."}
    label = dict(page, title="FAA Part 450 Licensing",
                 note="The page could not be read (no metadata), so this entry is built from the article's label; x.")
    merged, *_ = SI.merge({"ref_p": page}, {"ref_p": label}, refresh=True)
    assert merged["ref_p"]["title"] == "14 CFR Part 450", "a label replaced a page"
    merged, *_ = SI.merge({"ref_p": label}, {"ref_p": dict(label, title="Another Label")}, refresh=True)
    assert merged["ref_p"]["title"] == "FAA Part 450 Licensing", "one label replaced another"
    merged, *_ = SI.merge({"ref_p": label}, {"ref_p": page}, refresh=True)
    assert merged["ref_p"]["title"] == "14 CFR Part 450", "a page did not replace a label"
    # A SAME-RANK PAGE DRAFT carries another article's judgements and is not taken.
    merged, *_ = SI.merge({"ref_p": page}, {"ref_p": dict(page, kind="book")}, refresh=True)
    assert merged["ref_p"]["kind"] == "web-page"
    # A REGISTRY REBUILD keeps the stored year.
    reg = {"anchor": "r", "kind": "report", "doi": "10.1/x", "title": "T", "authors": [], "year": 1987}
    merged, *_ = SI.merge({"r": reg}, {"r": dict(reg, year=1971, title="T2")}, refresh=True)
    assert merged["r"]["year"] == 1987 and merged["r"]["title"] == "T2", merged["r"]

for name, fn in sorted(list(globals().items())):
    if name.startswith("t_") and callable(fn):
        check(name[2:], fn)

ok = sum(1 for p, _, _ in RESULTS if p)
for passed, name, detail in RESULTS:
    if not passed:
        print(f"  FAIL  {name}: {detail}")
print(f"{ok}/{len(RESULTS)} passed")
sys.exit(0 if ok == len(RESULTS) else 1)
