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


class Gate:
    """A compiled subject gate. Build one per article and do not copy one between articles."""

    def __init__(self, strong, name="gate"):
        if isinstance(strong, str):
            strong = [strong]
        self.name = name
        self.source = list(strong)
        self.pattern = re.compile("|".join(f"(?:{p})" for p in strong), re.I)

    def admits(self, title):
        return bool(self.pattern.search(title or ""))

    def explain(self, title):
        """Why a title was dropped, distinguishing 'off subject' from 'only ambiguous words'.

        A record dropped while carrying several ambiguous terms is the signature of a gate
        written for a different subject, which is the A333 failure. Saying so at drop time is
        cheaper than discovering it in the published reference list.
        """
        if self.admits(title):
            return None
        hits = [w for w in re.findall(r"[A-Za-z][A-Za-z-]+", (title or "").lower())
                if w in AMBIGUOUS]
        if len(hits) >= 2:
            return f"no subject anchor, but {len(hits)} ambiguous terms: {sorted(set(hits))}"
        return "no subject anchor"


def select(records, gate, key=lambda r: r.get("title", "")):
    """Partition records into kept and dropped. Returns (kept, dropped_with_reasons)."""
    kept, dropped = [], []
    for r in records:
        title = key(r)
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
