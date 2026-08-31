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

## A borrowed constant inherits the wrong aircraft

**What happened.** A335 computed a scaling exponent between the X-24A and the X-38 and reported that
mass grew as length to the 4.207. **The X-24A's length had been set equal to the X-38 atmospheric test
vehicle's 24.5 feet, which is a different aircraft**, and its mass was low by three hundred kilograms.
Corrected to 24 feet and 11,447 pounds, the exponent is **3.507** and the geometric-similarity factor
falls from 1.276 to 1.120.

**Why nothing caught it.** Both figures were plausible, both produced a plausible answer, and the
independent verifier had been given the same two constants. **A verifier that shares an input with the
thing it checks does not check that input.**

**The check.** Verify every published figure against a source at the publication review, including ones
that entered as constants months earlier. **Enter them into the verifier by a different route**, which
here meant converting from the imperial figures the sources actually quote rather than copying the
metric values.

**The consolation.** The verifier did catch the correction once the production module changed, because
it held its own copy. **Independence pays even when the shared value was wrong in both places.**

---

## A plausible title is not a URL

**What happened.** Three curated reference links in A334 returned 404, and all three were addresses
constructed from what the page *ought* to be called. Wikipedia has no article titled Space Maneuver
Vehicle, none titled Aerojet AR2-3 and none titled Space Shuttle landing. The subjects are real and
well covered, under Boeing X-40, Rocketdyne AR2 and Space Shuttle orbiter.

**Why nothing caught it earlier.** The identifier sweep covers `doi.org` links, and the rendered audit
covers markup. **Neither looks at a hand-written encyclopaedia link**, so a curated reference is
checked only by the publication review, and only if that review actually requests each one.

**The check.** Issue a request for every curated URL, not only the harvested ones. A 404 is fatal and a
403 is acceptable only on a documented bot-detected host.

**The bonus.** Correcting one of the three corrected a fact. The AR2-3 is a **Rocketdyne** engine and
is widely credited to Aerojet, which is the successor company rather than the developer. **A dead link
is sometimes a symptom of a wrong belief rather than of a moved page.**

---

## A measuring instrument has the same blind spot as the thing it measures

**What happened.** A334 audited its reference pool against the subjects its equations rely on and found
twenty-four of thirty-seven thin. The audit's patterns were written in the ARTICLE's vocabulary while
the harvest had asked in the LITERATURE's, so a well-supplied subject measured zero. **Three of the
largest apparent gaps closed on the instrument and not on the pool**, equilibrium glide going from 3 to
18 and crossrange from 4 to 11, **with no new records found in either case.**

**The check.** Measure coverage with the same vocabulary the search used. **A thin result is a claim
about the question before it is a claim about the field.**

---

## A probe assumes a domain, and the article may not share it

**What happened, 2026-08-14.** A series-wide sweep probed all forty-four X-Planes drafts for harvested
citations that had escaped the gate, using a list of medical, agricultural and social terms. It returned
78 hits across twelve articles and **thirty of them, the largest single block, were in A336**, whose
survey holds archival science, records appraisal, colonial archives and persistent identifier practice.
The obvious reading was that A336 had the worst gate escape in the series.

**The reading was wrong and the article says so in its own prose.** A336 is the X-39, a designation
reserved and never assigned, and its survey section states plainly that **"this article's subject is not
an aircraft. It is what a gap in an official register means"**, then declares eight clusters spanning
archival silence, classification infrastructure and identifier administration. The records are on topic.
**The probe had assumed every article in an aerospace series is about aerospace.**

**The same sweep over-corrected in the other direction.** A second instrument judged each citation
against the modal vocabulary of the cluster it was actually filed under, which needs no domain
assumption at all. It flagged 5,122 of 67,806, or 7.55 percent. Sampling twenty showed most were
correct and flagged only because the link text is truncated, with **`Wind Tunnel Verification of a
Translating Cowl-Lip Method` flagged under a cluster on inlet starting.** A 15 percent precision
instrument produces a defect count that is mostly not defects.

**The check.** Before judging a survey off topic, read what the article says its topic is. Then sample
the instrument in both directions, as `gate.audit` already requires, and quote the precision before
quoting the count. **A flag rate is a claim about the instrument until a sample says otherwise.**

**The habit.** State the article's subject in one sentence, and ask which literature belongs to that
sentence rather than to the series.

---

## A check with high precision and low recall gives false confidence

**What happened, 2026-08-14.** Nine caps-emphasis spans were found by hand across the series, so the
lesson was turned into a check for `_verify.py`. The first version flagged any capitalised token whose
lowercase form led a normal life in the same post: **80 hits across 20 files, of which roughly 85 percent
were legitimate**, including `AT&T`, `ION-DTN`, `AGENTS.md`, `BE-4` and the `AND` and `OR` of logic
gates. Narrowing it to capitals inside a bold span, which is emphasis inside emphasis and never correct,
gave **1 hit corpus-wide and it was real**. That version was nearly committed.

**It would have caught one of the nine defects that motivated it.** Precision was excellent and recall
was 11 percent. A check that green-lights a corpus while missing eight of nine instances is worse than
no check, because it stops the manual search that was working.

**A hypothesis about the cause was also wrong, and measuring it took two minutes.** The low recall was
attributed to `prose_text` stripping only single-line `[text][anchor]` pairs while citation text wraps.
Comparing it against a multiline strip across the series showed **0.0 percent inflation on every
article, including the 26,249-line A340**. The helper is correct and the hypothesis was not.

**The check.** Measure recall against the known defects before shipping a checker, not just precision
against the corpus. **Both numbers, or neither.**

---

## A summary that lists only exceptions cannot distinguish clean from unexamined

**What happened.** A corpus citation run reported findings per article and listed only articles that
had them. A334 had no row and was very nearly reported clean. It had been examined at **34.5 percent
coverage**, because the run was capped at 600 new lookups against 64,462 distinct identifiers.

**The check.** Measure coverage explicitly. An absent row means nothing until the denominator is known.

---

## An HTTP failure is usually not a citation failure

**What happened.** On a 250-record sample, 22 identifiers failed by HTTP and every one was registered
and correct. Publishers run bot mitigation, and a Defense Technical Information Center deposit refuses
the connection outright.

**The check.** `_lib/resolve.py` falls back to the issuing registry, which is a different route rather
than a retry of the same failing request. **An HTTP 200 still does not verify a citation**; use
`_verify_citations.py` for whether an identifier resolves to the work it is cited as.

## Describing a checker's correct findings as noise

**A371 and A372, 2026-08-13.** A citation sweep reported hard findings on two published
articles. The first reading called most of them artefacts of a trailing full stop, on the
reasoning that the visible link text strips one while the registry keeps it, so `compiler, n`
against `compiler, n.` must be a false positive.

**The comparison never sees punctuation.** `tokens` matches alphabetic runs of three or more
characters, so a trailing stop cannot produce a mismatch. The rule that fires is that the
registry supplies **no authors** and the label is **too short to read as a title**, which is
exactly the signature of a dictionary headword. An author-less record with a real multi-word
title passes cleanly.

**The checker was right and the first reading called it noise.** That is worse than missing a
finding, because a diagnosis of noise licenses dismissing every similar finding without
reading it, and forty-five more were waiting in the unpublished drafts.

**Read the rule that fired before deciding a finding is spurious.** The mechanism was
recoverable in one minute from the source, and asserting a mechanism without checking it is
the same defect the corpus documents everywhere else, arriving in the diagnosis rather than in
the article.

## A rendered-output audit cannot see a display equation demoted to inline math

**What happened.** In A341 an edit landed a `$$...$$` display equation and the next paragraph's
opening sentence on the same source line, because the article's prose is written one paragraph per
line and two consecutive edits both anchored on that line. Kramdown rendered the equation as inline
math inside a paragraph and ran two unrelated sentences together.

**Why nothing caught it.** `render.py` is the only instrument that sees what a reader sees, and it
looks for unbalanced delimiters, unresolved markup and unexpanded Liquid. **Here the delimiters
balance and the markup resolves.** The page is not malformed, it is merely wrong, and no property of
the HTML distinguishes an equation the author wanted inline from one the author wanted displayed.
`_verify.py` and `lint.py` both read source and had no rule about it either.

**The check.** Count display equations in the source and count `\[` in the rendered HTML, and require
them to agree. The discrepancy was one, which is what pointed at the line. **A count comparison
between two representations finds what neither representation can report on its own.**

**The guard.** `lint.py` now carries `math-display-inlined` as a DEFECT, firing when a line contains
`$$` and is neither a complete one-line display equation, nor one half of a two-line one, nor a
reference bullet whose link text is a title containing math. **It was measured across the whole corpus
before being made a defect** and reports zero findings there, so it gates without flagging anything
that already ships. Code is excluded through `post.strip_code_keeping_lines`, which blanks fenced,
Liquid-highlight and indented code while preserving line numbers so the report points at the right
line. Two regression tests cover it.

**The habit.** When an edit batch inserts an equation next to prose in an unwrapped file, the
separating blank line is the thing to check, and the cheapest way to check it is to compare counts
across the source and the render rather than to read.

---

## A wait loop that matches its own command line can never exit

**2026-08-13, twenty-two leaked shells across three sessions.** Waiting for a background job was
written as

    until ! pgrep -f "harvest3.py" > /dev/null; do sleep 60; done

**`pgrep -f` matches the full command line of every process, including the waiting shell's own**,
and that command line contains the literal string `harvest3.py`. So the loop finds itself, concludes
the job is still running, and sleeps forever. It is not slow. **It is structurally unable to
terminate**, and it survives the session that created it.

Twenty-two of these accumulated, aged up to a day and a half, every one waiting on a script that had
finished long before. They cost almost no processor time, which is why nothing ever surfaced them.

**Key the wait on the job's OUTPUT, not on its process name.**

    until [ -f tmp/a372/cr_dtic.json ]; do sleep 45; done
    until grep -q "clean of hard" tmp/audit.txt; do sleep 45; done

A sentinel in a file cannot match the waiting shell. **The same defect appears in verification**, and
it did here: a follow-up check written as `ps -eo command | grep -c "until .*sleep"` reported three
survivors by counting its own pipeline. Snapshot `ps` to a file and read the file, or the instrument
becomes one of the things it is measuring.
