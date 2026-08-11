# Verification Traps

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

Every entry here is a mistake that actually happened, together with the check that caught it. The
repository already applies this rule to `_verify.py`, where every check exists because the defect
shipped. This file applies it to the working method rather than to the corpus.

**The common root is asserting a property instead of measuring it.** In every case below the wrong
belief was reasonable, the work looked finished, and only an independent observation exposed it. The
lesson is not to be more careful. It is to run the observation.

---

## The working directory is sticky and a later edit will land in the wrong tree

**What happened.** A `cd` into a throwaway build copy persisted across commands. Eight draft date
changes and a category rename were written into that copy, verified there, reported as complete, and
then deleted with the copy. The reported "0 errors, 0 warnings" was measured against a directory that
no longer exists.

**The check.** `git status` before claiming a file changed. A repository edit that does not appear
there did not happen.

**The habit.** Use absolute paths for edits. Treat a `cd` into `tmp/` as scoped to one command.

---

## A checker's first version is usually wrong, and its second version can hide the first

**What happened.** A rendered display-math check was written three times.

1. Counting `\[` and `\]` naively. `\\[2mm]` is a LaTeX line break with a spacing argument, legal
   inside `cases`, and it counted as an opening delimiter. One correct page reported broken.
2. Excluding any bracket preceded by a backslash. A display block whose last line ends in a line break
   closes as `\\\]`, so the legitimate closing delimiter was discarded. Two more correct pages
   reported broken, **and this version masked the first error**.
3. Backslash-run parity, which is right. A bracket is a delimiter exactly when the run before it has
   odd length.

**The check.** Validate a new checker against known-good AND known-bad input before trusting a clean
result. **A clean report from an unvalidated checker is not evidence.** Prove it can fail: inject the
defect it claims to catch and confirm a non-zero exit.

**The habit.** When a checker reports a defect in old, stable, published material, suspect the checker
first.

---

## Two instruments measuring the same thing will disagree, so never mix their numbers

**What happened.** A frequency warning printed a count from one prose extraction and a percentage from
another, reading `` `specific` 59x ... top collocate `specific impulse` 57x = 86% ``. Fifty-seven of
fifty-nine is ninety-seven percent. The 86 came from the second instrument counting 66.

**The check.** Any two figures in one sentence must come from one measurement. If a function needs a
caller's data, pass it in rather than recomputing.

---

## A rate cannot tell a term of art from a tic

**What happened.** `specific` reaches 15.07 uses per thousand words in the rocket propellant articles
and 86 percent of them are the phrase "specific impulse", which names a quantity and cannot be
paraphrased. `substantial` reaches 10.6 in another article and names nothing.

**The check.** `python3 _lib/diction.py collocate <word> <path>`. **Direction depends on part of
speech.** A noun compounds with the word before it and an adjective with the word after. Reading one
direction only once produced a recommendation to rewrite four correct published articles.

---

## A style substitution is an edit to the argument

**What happened.** Twice, a change made to satisfy a prose rule changed a claim.

- Rewriting a colon-led label, `Remaining, and genuinely open:`, into a sentence, `Two options
  remain`, invented a count. The list beneath it had three. It reached a published article.
- Replacing `substantial` with `sustained` swapped a magnitude claim for a duration claim in a
  sentence that already made the duration claim.

**The check.** Read the whole diff of a style pass as prose, asking of each change whether it asserts
anything the original did not. See the substitution rules in
[STYLE_GUIDE](../writing/STYLE_GUIDE.md).

---

## Renaming a category moves every URL of every post that carries it

**What happened.** `c` and `c++` both slugify to `c`, so one archive silently overwrote the other and
`/categories/cpp/` returned 404. Renaming the category fixed the archive and **broke two live 2022
URLs**, on the belief that only the first category appears in a URL. Jekyll's default permalink joins
the whole list.

**The check.** Build the previous revision and list the generated paths. That is what established the
old addresses after the fact, and it would have established them beforehand.

**The remedy.** `_verify.py` now fails on `category-slug-collision`, and `redirects/` holds a page for
each retired address.

---

## The repository may already know

**What happened.** A finding was reported as a discovery when `_verify_exemptions.yml` had recorded it
six days earlier, with a measurement.

**The check.** Search the process files and the exemption records before writing up a finding as new.

---

## A source check cannot answer a rendering question

**What happened.** `_verify.py` and `_lib/lint.py` both read markdown source. Run across the corpus,
lint reported 1,596 defect-severity findings and the rendered pages carried none of them.

**The check.** `./_check.sh`, which builds and runs `_lib/render.py` over the output, is the only
instrument that sees what a reader sees.

---

## An HTTP failure is usually not a citation failure

**What happened.** On a 250-record sample, 22 identifiers failed by HTTP and every one was registered
and correct. Publishers run bot mitigation, and a Defense Technical Information Center deposit refuses
the connection outright.

**The check.** `_lib/resolve.py` falls back to the issuing registry, which is a different route rather
than a retry of the same failing request. **An HTTP 200 still does not verify a citation**; use
`_verify_citations.py` for whether an identifier resolves to the work it is cited as.
