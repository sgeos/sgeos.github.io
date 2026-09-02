#!/usr/bin/env python3
"""Subject-anchor gating for a harvested reference corpus, and the sampling that audits it.

THIS MODULE EXISTS BECAUSE THE SAME DEFECT SHIPPED TWICE IN TWO ARTICLES, IN OPPOSITE
DIRECTIONS, BECAUSE THE GATE WAS COPIED BETWEEN ARTICLES RATHER THAN WRITTEN FOR EACH.

  A333. The gate was inherited from an aeronautics article and tested for aircraft
  vocabulary. Applied to a compiler-science pool it rejected 2,174 titles for containing no
  aircraft, and it rejected the article's oldest primary source because that source's title
  used the vocabulary of the underlying mathematics rather than of the application.

  A370. The gate was rewritten for the new subject and OVERCORRECTED. It admitted generic
  stems, being analysis, implementation, generation, evaluation, system, model, performance
  and interface, each of which occurs in every discipline that publishes. It admitted 4,305
  records including rabies control, seismic depth imaging, veterinary breeding soundness
  examination, photonic supercontinuum generation, transport appraisal and fibre art.

THE TWO FAILURES LOOK COMPLETELY DIFFERENT IN EVERY SUMMARY STATISTIC AND IDENTICAL IN NONE.
A narrow gate reports a small corpus, which reads as a thin literature rather than a bug. A
permissive gate reports a large corpus, which reads as thoroughness. Cluster distributions
look plausible in both cases and the drop-reason table looks plausible in both cases.

  ONLY READING A RANDOM SAMPLE OF WHAT WAS KEPT DETECTS THE PERMISSIVE FORM.
  ONLY READING A RANDOM SAMPLE OF WHAT WAS DROPPED DETECTS THE NARROW FORM.

So `select` refuses to return a corpus until both samples have been drawn, and `audit`
prints them. The sampling is not a recommendation in a comment that the next article's copy
will lose. It is the return protocol.
"""
import random
import re

# A gate is a pair of patterns. STRONG terms are specific to the subject on their own and
# admit a record by themselves. AMBIGUOUS terms are shared with every discipline and admit
# nothing, however many of them a title carries, because a pile of ambiguity is still
# ambiguous. The ambiguous list is not used for admission. It exists so `explain` can say
# WHY a record was dropped, which is what makes a narrow gate visible.
AMBIGUOUS = frozenset("""
analysis analyses analytical approach application applications assessment
comparison components computation design development evaluation experiment
framework generation implementation improvement integration interface
investigation measurement method methodology model modeling modelling
optimisation optimization performance process research review simulation
study system systems technique technology theory validation
""".split())


# THE SHARED PHYSICAL SUBSTRATE, WHICH IS NOT A SUBJECT AND IS NEEDED BY EVERY
# SUBJECT THAT COMPUTES ANYTHING AT ALTITUDE.
#
# This is deliberately NOT a reusable gate. The header above records what copying
# gates between articles costs, and nothing here relaxes that. It names one small
# vocabulary that is common to every article in an aeronautical series because it
# describes the medium rather than the aeroplane, and a subject gate that omits it
# reports zero records for a relation the article displays.
#
# THE INCIDENT CHAIN IS THREE ARTICLES LONG. A341's gate refused `U.S. Standard
# Atmosphere, 1976`, one of its own foundational sources, because `atmosphere` was
# not an anchor, and the article readmitted it BY NAME and recorded the defect.
# The fix was made for that article only. A342 then used the standard atmosphere
# for its corrected-parameter engine model and its ceiling analysis and harvested
# ZERO records about it. A343 displayed the atmosphere relation itself and also
# harvested zero. Neither noticed, because a subject nobody searched for returns
# no records and an absent cluster looks like an absent literature.
#
# A per-article fix has now failed twice, so the vocabulary lives here.
# NARROWED AFTER MEASUREMENT, and the first version is the lesson. Written with a
# bare `speed of sound` and a bare `stratospher`, it admitted the speed of sound in
# seawater, in mammalian tissue, in ionic liquids, in molten potassium halides and
# in PVC pipes, together with GNSS tropospheric delay and a tropical cyclone study.
# FORTY-SEVEN OF ONE HUNDRED AND FORTY-THREE RECORDS IN THE CLUSTER WERE WRONG.
# `speed of sound` is a homonym across acoustics, physical chemistry, biology and
# oceanography, which is the same shape as A341's designation harvest returning tax
# valuations. The term now requires an atmospheric context on one side or the other.
# Bare `stratospher` is dropped entirely, because genuinely aeronautical
# stratospheric work carries aircraft vocabulary and is admitted by a subject gate.
ATMOSPHERE = [
    r"standard atmosphere|atmospheric (?:model|propert|structur|tabl)|\bICAO atmosphere\b",
    r"atmosphere.{0,25}(?:propert|model|tabl|altitude)|properties of the atmosphere",
    r"tropopause|geopotential|pressure altitude|density altitude",
    r"(?:speed of sound|acoustic velocity).{0,40}(?:air|atmospher|altitude)",
    r"(?:air|atmospher\w*|altitude).{0,40}(?:speed of sound|acoustic velocity)",
    r"air (?:densit|temperature|pressure|viscosit).{0,20}altitude|altitude.{0,20}air (?:densit|propert)",
]


# TYPOGRAPHIC PUNCTUATION IS NORMALISED BEFORE ANY PATTERN SEES A TITLE, AND THAT
# IS NOT OPTIONAL. A334 refused `Thermal Characteristics of a Nickel-Hydrogen
# Battery` because the depositor wrote the hyphen as U+2010, and recorded that its
# selection script carried a normalise step which should be copied forward. It was
# not copied forward. A342 then refused `Validating Human-Robot Interaction Schemes
# in Multitasking Environments`, one of its own foundational sources, because the
# publisher sets `Human-Robot` with an en dash.
#
# Twice is a pattern and a per-article fix has now failed once, so the
# normalisation lives here where every gate inherits it. There is no case in which
# a subject gate should fail on the shape of a dash.
_DASHES = dict.fromkeys(map(ord, "\u2010\u2011\u2012\u2013\u2014\u2212"), "-")
_QUOTES = dict.fromkeys(map(ord, "\u2018\u2019\u201c\u201d"), "'")


def normalise(title):
    """Fold typographic dashes and quotes to their ASCII forms."""
    return (title or "").translate(_DASHES).translate(_QUOTES)


# A HYPHEN MUST NOT DEFEAT A MULTI-WORD ANCHOR, AND THIS IS THE SECOND INSTRUMENT
# IT HAS DEFEATED. A344's audit asked for `arresting gear` with a space while the
# literature writes `ARRESTING-GEAR CABLE`, and `_lib/survey.py` gained `loose` so
# that an audit pattern could not be beaten that way. The rule was recorded for
# AUDIT patterns and nobody applied it to GATES.
#
# A345's gate then refused 57 records on a separator alone, among them `Correction
# of wind-tunnel pressure coefficients for Reynolds number effect` and
# `Investigation of a Jet-Noise-Shielding Methodology`, which are that article's
# keystone subject and the subject of its second vehicle. The anchors said `wind
# tunnel` and `jet noise` with spaces.
#
# THE FIX IS HERE RATHER THAN IN AN ARTICLE'S GATE, because a per-article gate fix
# fixes nothing for anybody else, which the atmosphere family established across
# three articles. Only a hyphen BETWEEN TWO LETTERS is flattened, and the original
# title is tested first, so no existing pattern changes meaning. A single-word
# anchor is unaffected either way: `\blift\b` already matches inside `non-lift`,
# because a hyphen is not a word character.
_INTRAWORD_HYPHEN = re.compile(r"(?<=[A-Za-z])-(?=[A-Za-z])")


def flatten_separators(title):
    """`Boundary-Layer Methods` as `Boundary Layer Methods`, for anchor matching only."""
    return _INTRAWORD_HYPHEN.sub(" ", normalise(title))


class Gate:
    """A compiled subject gate. Build one per article and do not copy one between articles."""

    def __init__(self, strong, name="gate"):
        if isinstance(strong, str):
            strong = [strong]
        self.name = name
        self.source = list(strong)
        self.pattern = re.compile("|".join(f"(?:{p})" for p in strong), re.I)

    def admits(self, title):
        """True when the title carries an anchor, hyphenated or not.

        The normalised title is tested first, so a pattern written with a literal
        hyphen keeps its meaning. The flattened form is tried only on a miss.
        """
        t = normalise(title)
        if self.pattern.search(t):
            return True
        flat = _INTRAWORD_HYPHEN.sub(" ", t)
        return flat != t and bool(self.pattern.search(flat))

    def explain(self, title):
        """Why a title was dropped, distinguishing 'off subject' from 'only ambiguous words'.

        A record dropped while carrying several ambiguous terms is the signature of a gate
        written for a different subject, which is the A333 failure. Saying so at drop time is
        cheaper than discovering it in the published reference list.
        """
        if self.admits(title):
            return None
        hits = [w for w in re.findall(r"[A-Za-z][A-Za-z-]+", normalise(title).lower())
                if w in AMBIGUOUS]
        if len(hits) >= 2:
            return f"no subject anchor, but {len(hits)} ambiguous terms: {sorted(set(hits))}"
        return "no subject anchor"


# A SUBJECT TEST IS NOT A SUBSTANCE TEST, AND THE CORPUS LEARNED THAT THE HARD WAY.
# An Oxford English Dictionary entry titled `compiler, n.` passes every computing
# anchor perfectly, BECAUSE THE TITLE IS THE ANCHOR. Six such records reached two
# published articles before an audit caught them, along with book chapters titled
# `Compiler`, `CompCert` and `Unboxed`. No amount of qualifying the anchors helps,
# since the defect is that the title carries no claim at all.
#
# The rule is deliberately narrow. A title of one or two words is refused ONLY when
# it is a bare subject term or a dictionary headword, because `Garbage Collection`
# and `Abstract Interpretation` are legitimate paper titles and must survive. What
# is refused is the dictionary part-of-speech form, and a title identical to its own
# container, which is book front or back matter rather than a work.
_HEADWORD = re.compile(r"^\s*[\w][\w\s'-]{0,40},\s*(?:n|v|adj|adv|prep|conj)\.?\s*$",
                       re.I)


def substance_reason(title, container=""):
    """Why this title is not a work, or None if it is one.

    Reports rather than judges silently, so a caller can log what it refused.
    """
    t = (title or "").strip()
    if not t:
        return "no title"
    if _HEADWORD.match(t):
        return "dictionary headword, a part-of-speech entry rather than a work"
    c = (container or "").strip()
    if c and t.casefold() == c.casefold():
        return "title identical to its container, so book front or back matter"
    return None


def select(records, gate, key=lambda r: r.get("title", ""),
           container=lambda r: r.get("container", "") or r.get("venue", "")):
    """Partition records into kept and dropped. Returns (kept, dropped_with_reasons).

    THE SUBSTANCE TEST RUNS FIRST, because a record that is not a work should be
    refused for that reason and not for whichever anchor it happened to miss.
    """
    kept, dropped = [], []
    for r in records:
        title = key(r)
        lacks = substance_reason(title, container(r))
        if lacks:
            dropped.append((r, f"[no substance] {lacks}"))
            continue
        why = gate.explain(title)
        if why is None:
            kept.append(r)
        else:
            dropped.append((r, why))
    return kept, dropped


def audit(kept, dropped, seed, n=25, key=lambda r: r.get("title", "")):
    """Print a random sample of BOTH sides. Call this and read it before using the corpus.

    Returns (kept_sample, dropped_sample) so a caller can assert on them, but the value of
    this function is the printed output and the fact that a human looked at it.

    `seed` is required and has no default, because an unseeded sample is not reproducible and
    a reviewer cannot check what was actually read.
    """
    rng = random.Random(seed)
    ks = rng.sample(list(kept), min(n, len(kept)))
    ds = rng.sample(list(dropped), min(n, len(dropped)))
    print(f"AUDIT seed={seed}  kept {len(kept)}  dropped {len(dropped)}")
    print(f"\n-- {len(ks)} RANDOM KEPT RECORDS. Anything off-subject here means the gate is "
          f"too permissive. --")
    for r in ks:
        print(f"   {key(r)[:100]}")
    print(f"\n-- {len(ds)} RANDOM DROPPED RECORDS. Anything on-subject here means the gate is "
          f"too narrow. --")
    for r, why in ds:
        print(f"   [{why[:38]}] {key(r)[:80]}")
    return ks, ds
