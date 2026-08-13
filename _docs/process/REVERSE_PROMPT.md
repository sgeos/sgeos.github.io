# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-12
**Task**: **A371 primary-reference review**, the pass that was skipped. **Committed AND pushed. LIVE PAGE CHANGED.**

---

## Where It Is

**Published.** `_posts/2026-08-08-do_proven_bounds_survive_compilation.markdown`, live at
`/engineering/compilers/verification/2026/08/08/do_proven_bounds_survive_compilation.html`, series
`keleusma_research_spikes` index 3. 26 display equations, 11,112 reference definitions.

**It went live the moment it was pushed**, because 2026-08-08 is four days in the past and the site sets
`future: false`. The verification build was therefore run **without** `--future`, which is the only
configuration that matches the live site.

**Publication renumbered two live pages**, exactly as flagged beforehand. A369 and A370 now read Part 1 and
Part 2 **of 3**, confirmed as rendered rather than assumed. **The `keleusma_native` series is complete.**

---

## The Skipped Pass, Which Is the Newest Work

**You were right and the TASKLOG shows it.** A372 records a primary-reference review. A371 does not, having
gone standards and retarget, then equation density, then straight to publication review.

**The gap that pass found was created by a later correction**, which is the promoted-subjects rule in its
purest form. Item 5 of the draft corrections narrowed the central claim so that **the arena term of the
memory bound transfers exactly**. That sentence became load-bearing and **cited nobody at all**. The
reference base never followed the correction.

Four references now sit where the claim is made. **Hanson 1990** for the practical allocation-by-lifetime
discipline, **Tofte and Talpin 1997** for the theory making region lifetimes statically inferable,
**Grossman and Morrisett 2002** for regions in a systems language, and **Berger and Zorn 2002** for when a
custom allocator actually pays. The property that matters throughout is that **a region's total is decided
before the program runs**, which is what lets the term cross the boundary, and the article now says so.

**Two of the four were already in the article and never cited**, sitting in the harvested block as records
nobody had read. I promoted them into the hand-selected set instead of adding them again under a second
anchor.

**The counts were reconciled rather than nudged.** Hand-selected 28 to 32, harvested-only 11,068 to 11,066,
total 11,096 to 11,098. **The error-rate paragraph still describes the 27 submitted**, since a later addition
cannot change what was wrong on submission.

Two things I checked rather than assumed. **A double listing is the design**, every harvested anchor
appearing once in its cluster and once in the complete bibliography, measured as 11,068 anchors at two
entries and 30 at one. And **a title check I wrote flagged two of the four while measuring the wrong
direction**, since harvested link text carries surname and year and is a superset of the registry title.
Checked as containment, all four cover it at 1.00.

---

## The Series Rename, From an Earlier Commit

`series_title` goes from **Keleusma Native Code Generation** to **Keleusma Research Spikes**, and the slug
from `keleusma_native` to `keleusma_research_spikes`, across all four live pages.

**I changed the slug as well, which is beyond the literal ask.** The old slug asserts native code generation
for a series no longer defined that way, and the next spike need not concern native code. Say the word if
you want the slug reverted, though nothing outside the four posts referenced it.

**It is URL-neutral, established before anything was touched.** `_layouts/post.html` uses the slug only to
group posts and renders `series_title` with the slug as a fallback, so it reaches no URL and no
reader-visible text. It appears nowhere in `_config.yml`, the layouts, the includes or any plugin. **No
`redirects/` entry is needed.**

**The change had to be atomic or the series would split in two**, since grouping is by exact slug match and a
missed file would form a second series of one with broken navigation. All four were rewritten together and
verified as 4 of 4 with indices 1 through 4 and zero stragglers, then confirmed against a production build.

---

## A372 Is Live, and the Series Is Complete

`_posts/2026-08-09-cost_of_compiling_aggregates.markdown`, at
`/engineering/compilers/verification/2026/08/09/cost_of_compiling_aggregates.html`. **It went live the moment
it was pushed**, because 2026-08-09 is three days in the past, so the verification build was run **without**
`--future`.

**Publication renumbered three live pages.** A369, A370 and A371 now read Part 1, 2 and 3 **of 4**, confirmed
as rendered.

**One imprecision was corrected before the move.** The Epistemic State attributed the 34.5 percent blocking
figure to "the previous article" when it comes from **A369, not the immediately previous A371**. It now links
the first article explicitly, and I applied the fix to `tmp/a372/body.md` as well so a re-run could not
revert it.

**Cross-article consistency was checked against A371 post-erratum.** All five references to the previous
article survive it, the one naming a retracted figure having been neutralised during the standards pass.

Verification: `_verify.py` **0 errors and 0 warnings across 300 posts**, `./_check.sh` clean at 464 pages,
**15 display-math blocks with zero raw `$$` survivors and zero unfilled markers**, present on the home page,
in `feed.xml` and in `sitemap.xml`. Two of 189 internal links are unresolved and that is the **pre-existing
site-wide** `.pdf` and `.epub` pair the post layout emits for every article.

**`tmp/a372/assemble.py` is now guarded** and refuses to run, as A371's is.

---

## The Word Usage Pass, From an Earlier Commit

**`specific` is not a problem here.** It stands at **1 use, 0.18 per thousand**. I checked it first because
you named it.

**The measurement again had to exclude the harvest.** The article carries 183,125 raw body words against
5,595 of author prose, a **thirty-three-fold dilution** that would have made every rate insensitive.

**The phrase instrument found my own boilerplate for the third time in this series.** Six survey leads shared
the stem `contemporary records concern`, differing only in a number. That is exactly the defect A371's pass
found as "The harvest returned N further contemporary records", and **no single-word instrument can see it**.
Six leads now carry a fact about their own cluster, and `is what makes` was reduced from five uses. The
constructions at or above the peer maximum fell **21 to 16**, every survivor being subject vocabulary
measured against a corpus of aircraft articles.

**Twelve single words sit above the peer maximum and eleven are simply the subject**, being `boxed`,
`aggregate`, `layout`, `backend`, `representation`, `form`, `corpus`, `arena` and `anchoring` among them.

**`already` is the twelfth and I left it alone deliberately.** It sits at 3.40 per thousand against a peer
maximum of 2.77, and **17 of its 19 uses are the article's thesis in one word** — the decision was already
made upstream, the backend already implements the residue, the bound already exists. I classified all 19
rather than asserting it. Trading it for a synonym would move the tic, not remove it.

One claim I introduced while editing was checked against the data. "The largest cluster in the survey at 650
records" is verified as the largest modern cluster, against 575 for estimation and 434 for types.

---

## The Publication Review, From an Earlier Commit

**The substantive gap was the survey again.** A369 carries 1,759 research references, A370 1,980 and A371
11,096. A372 arrived with 31.

A harvest of **79 queries across ten clusters in seven rounds** retrieved **45,989** records. The anchor gate
admitted 6,357 and **6,008 reach the reference list**, beside the 31 hand-selected works, which are untouched
and verified as **31 of 31 preserved with none repointed**. **23 of the 31 were independently returned by the
harvest**, which is the coverage corroboration worth having.

**Every lesson A371 paid for was applied from the start, and they held.** All three publication types were
requested in the first pass rather than discovered late, since **Springer deposits Lecture Notes in Computer
Science as `book-chapter`** and the book rounds returned 13,378 records here. Qualifiers order-free, anchors
hyphen-tolerant, proceedings furniture refused by title shape, hand anchors reserved so no harvested record
could displace a cited one.

## This Is the Most Homonym-Hostile Subject the Corpus Has Swept

Its own vocabulary belongs to enormous literatures elsewhere. **`Aggregate` is concrete and economics.
`Layout` is integrated-circuit and facility layout. `Alignment` is bioinformatics. `Offset` is carbon.
`Boxing` is a sport and `arena` is a stadium.** Not one of those is used as an anchor without a computing
qualifier.

**Eight new families recorded**, taking the store from 56 to 64 patterns, being municipal waste collection
against memory reclamation, facility and plant layout, structural and aerospace layout, the linguistic corpus
against a corpus of programs, power-system dispatch against dynamic method dispatch, `unboxed` in archival
cataloguing, the intermediate representation in speech pipelines, and heuristics-and-biases applications
outside estimation.

**The power-dispatch family had been contaminating a cluster**, the dispatch count falling 27 to 18 once it
was removed. That is a claim about the literature, not a stray record.

## Two Defects the Assembler Inherited From A371

**The attrition counts were hardcoded from the previous article.** They are now written out by `gen_master`
and read back, since a transcribed figure goes stale the moment a harvest is re-run. And one statement read
the stats file a line after using it.

**Definition-block separation was verified explicitly**, at 0 issues, because the previous pass lost 64
references to blank lines eaten by a regex while `_verify.py` passed it.

One superlative became a checkable statement, "the largest of the layout clusters" becoming "more than the
representation and dispatch clusters combined", 183 against 108 plus 11.

---

## The Primary-Reference Pass, From an Earlier Commit

**42 to 47 reference definitions, 26 to 31 research identifiers.** Primary count at a 2000 cutoff rose 17 to
20, and the year range extended from 1974-2014 to **1974-2017**. The base previously carried **nothing at all
after 2014**, in a section titled The Contemporary Literature.

Five references added, each where a step of the argument depends on it.

- **Ohori 1995**, the polymorphic record calculus and a compilation method resolving field access to an index
  computation. **The closest antecedent to what this backend receives already resolved**, and it was absent
  while the surrounding unboxing work was cited.
- **Shepperd and Schofield 1997** and **Walkerden and Jeffery 1999**, for the Threats section's own phrase
  "an argument from similarity". **Estimation by analogy is that argument's literature** and its record is
  mixed, which is the right prior for the article to hold.
- **Bekelman, Li and Gross 2003**, for the threat that the author scoped work he would then perform, since
  the association between an investigator's interest and a favourable result is measured. **It is a
  systematic review and therefore not primary**, which the log states rather than eliding.
- **Haas and others 2017**, the WebAssembly design paper. The format's *proposal* was cited while the paper
  stating *why* was not, and it closes the contemporary window.

## The Rendered Audit Caught What `_verify.py` Passed, Twice

Re-sorting the link-definition blocks with a regex **ate the blank lines** separating them from adjacent
headings and list items. Kramdown then stopped reading them as definitions, and **62 and then 64 references
rendered unresolved** while `_verify.py` reported 0 errors and reference integrity reported 47 used against
47 defined.

**A source checker predicts what kramdown will do. The rendered audit sees what a reader sees.** That is the
standing corpus lesson and it fired twice in one pass. I abandoned the regex for a line-based approach that
sorts each run in place and restores exactly one blank line on each side, verified as 6 runs, 0 separation
issues, every run sorted.

**Three sections remain uncited and correctly so**, being the orientation section, the Measurement and the
Epistemic State, which all report the article's own instrument.

---

## The Equation Pass, From an Earlier Commit

**12 to 15 display equations.** The audit's four candidate gaps were mostly the known false positives, being
two survey subsections whose numbers are publication years and an Epistemic State restating measured values.

**The best addition is the article's own thesis, which was stated in words and never displayed.** The prose
read "These differ by exactly the terms with no instances". That identity now appears as a formula, and
**the whole article is an evaluation of that one sum.**

Also added, the discriminant test as a load and an integer comparison, which was **the only class in the work
enumeration with no displayed relation** while the other three each had one, and which explains in passing
why those 29 operations carry no form tag. And the delivered-coverage ratio of 300 over 302, for the claim
that handling 300 cases and refusing 2 delivers less than the headline.

## A Number in the Lede Was Supported Nowhere

The opening claimed **two thirds of the machinery it was supposed to need is dead code**, and that figure
maps to nothing a reader can check. The instruction set defines 11 aggregate opcodes of which 6 are used, and
the forms number three of which one is empty. **Neither gives two thirds.**

It now reads that two of the three representation forms account for two operations in the entire corpus, and
the Measurement section says where that is checkable. **This is the same defect A371 shipped with its
nine-second figure.**

## The Promoted-Subjects Rule Fired Again, on the Eighth Consecutive Article

`citation_gaps` reported 10. The equation pass had promoted the estimate-versus-actual distinction into a
displayed identity while its supporting literature sat four sections away in the survey. Jørgensen now
appears beside the identity, with the distinction that **the contribution is not that estimates anchor** but
that here the anchor is visible in the index set, so the error is removable by counting instead of by
debiasing.

That took the gaps to **6, and those six are measurements of this corpus or the article's own derivations
about its own compiler**, where citing anyone would be manufacturing.

---

## Where A372 Is

`_drafts/cost_of_compiling_aggregates.markdown`, editorial date **2026-08-09**, series `keleusma_research_spikes`
index 4. **612 lines, 12 display equations, 42 reference definitions, 4,256 words of author prose.**
Titled under the series convention as **Keleusma Research Spike, What It Costs to Compile a Data Structure
Whose Shape Is Already Decided**.

The date slot was free and all three `post_url` targets point at published posts, so the build interlock is
satisfied.

## What the Retarget Needed

**The source claimed no compiler background is required and did not deliver it**, using backend, bytecode,
aggregate, layout, boxed and arena without introducing any of them. That is the same defect A371 shipped. A
`## What You Need to Know to Read This` section now carries the six ideas the argument actually needs.

**I wrote "Five ideas" and gave six.** That is the count-in-my-own-prose defect this series has now shipped
four times. Found by counting, not by any checker.

## Two Fixes Carried In From Earlier Work

**The source reported the series rates as "0 of 31".** A370's published text says **35** in four places and
its pipeline data holds exactly 35, so it now reads 0 of 35 and agrees with the addendum on A369's live page.

**A sentence attributed a frame reduction to A371**, whose frame figures its own erratum has since
retracted. It is neutralised to the quantity rather than the figure.

## An Arithmetic Gap, and My First Reading of It Was Wrong

The by-form aggregation gives 300 flat, 2 nested and 0 boxed, totalling **302 against a table total of 331**,
and the article did not say where the other 29 went.

**I first thought they were missing from the work enumeration. They are not** — it covers them as
"Discriminant tests, 29 instances", and 239 plus 61 plus 29 plus 2 recovers 331 exactly. The gap is only in
the by-form line, and a sentence now explains that a discriminant test carries no form tag because it is a
comparison and names no layout. **I checked that against `src/vm.rs` in the Keleusma tree** rather than
inferring it from the opcode name.

## Verification

- `_verify.py` **0 errors, 0 warnings**. `./_check.sh --drafts` clean at 508 pages.
- Reference integrity **42 used against 42 defined**, none undefined, orphaned, duplicated or malformed.
- **All 26 research identifiers resolve and all 26 titles match the registry**, which matters because this
  series documents the neighbouring-identifier failure that a working link cannot catch.
- Style clean. 3 em dashes, 15 semicolons and 11 prose colons removed, `rather` brought under the limit with
  each substitution checked for grammaticality.

---

## Read This First

**The LinkedIn announcement I drafted for you states the finding backwards.** It says frames exceed the
proven bound by two to thirteen times in the dangerous direction. **The opposite is true.** If it has been
posted it needs correcting or taking down, and I can supply a corrected draft.

---

## The Erratum, Which Is the Newest Work

**The article's central empirical claim was backwards, and the cause is worth keeping.** Every frame figure
came from invoking `llc` at two optimisation levels over the same intermediate representation. **The pass
that promotes stack slots into registers is a middle-end pass and `llc` is a back end that does not run it**,
so both figures described unpromoted code and their difference was back-end noise. The Keleusma test suite
had written that warning down three days earlier.

Three claims were false and are corrected in place.

- **Promotion eliminates the provisioning** rather than relocating it into spill slots. The same 19 modules
  occupy **5,048 bytes promoted against 275,432 unpromoted, a factor of 54.**
- **The proven bound exceeds the real frame in every module measured**, ratios running **0.12 to 0.88**. The
  dangerous-direction framing was the reverse of what happens.
- **The provisioning change buys nothing for the shipped pipeline**, both regimes measuring 5,048 bytes once
  promotion runs.

**I was careful not to over-correct.** Eight modules agreeing is not a mechanism. The article now says the
bound is **empirically conservative on this corpus under the shipped pipeline**, which is much weaker than
sound, and that deep expression nesting with few live values could plausibly invert it.

**Handling followed the erratum's first ranked option**, an erratum block at the head of the article, with
the original figures retained so the change is visible. It renders as the first heading.

**My item-2 flag last turn was half right.** The tension was real and **A369 was the correct one.** A371 was
wrong, which is the opposite of the direction I suspected. A369 needs no change on that point and its
separate framing fix stands.

**The assembler is now guarded.** `tmp/a371/assemble.py` writes to the `_drafts/` path, so re-running it
would recreate a draft duplicating the published post and **silently discard this erratum**, which never
passed through `body.md`. It refuses to run rather than warning.

---

## The Series Consistency Check, From an Earlier Commit

**In sequence the three are clean.** Dates 2026-08-06, 07 and 08 against series indices 1, 2 and 3, A-numbers
A369, A370 and A371, filenames matching dates, and rendered navigation reading Part 1, 2 and 3 of 3.

**In substance A369 carried the conflation A371's item 5 corrects**, and it is fixed. The sentence read that
the native transfer question is whether a bound proven over the arena survives lowering to code whose stack
frames are chosen by a register allocator. **Those are two different quantities.** It now says that the arena
bound transfers without further argument, because native code allocates from the same arena in the same
bytes, and that the open question is the machine stack frame, which no bytecode-level bound describes.

**No result in A369 changes.** Its subject is coverage ordering and not memory, so this is a fix to how it
frames an open question. The Chaitin 1982 citation is preserved, since dropping it would orphan an anchor.
**I added no link to A371**, because A369 is dated two days earlier and the convention is back-reference
only. The series navigation already connects them.

**A370 needed nothing**, carrying no arena or bound-transfer claim at all.

**The second item is deliberately left alone, as you asked.** A369 says per-function frame size varies by a
factor of roughly thirty depending on whether the middle-end promotion pass has run, against A371's
corpus-wide 7.6 percent across the same boundary. Those are different statistics and not a flat
contradiction, but the claim has the shape of the error the engineering session identified. **It cannot be
settled here**, since A369 attributes it to the project's decision register, which lives in Keleusma.

---

## What Was Checked Before and After the Publication

**Before.** The date slot 2026-08-08 was free, posts running 08-01 through 08-07. Both `post_url` tags point
at A369 and A370, which are published, and **nothing anywhere forward-references A371**, so the build
interlock was satisfied in both directions.

**After.** `_verify.py` **0 errors and 0 warnings across 299 posts**, `./_check.sh` clean end to end at 463
pages with no rendered findings, production build in 10.1 seconds. The article carries **zero raw `$$`
survivors and zero unfilled markers**, 22,192 resolved research anchors, and appears on the home page, in
`feed.xml` and in `sitemap.xml`.

**Two of its 189 internal links are unresolved and that is pre-existing.** They are the `.pdf` and `.epub`
download links the post layout emits for every article. I checked rather than assumed: both published
siblings show the identical pair, and the built tree holds two PDF files and zero EPUB files across the
entire corpus.

`_drafts/draft_summary.md` lost its A371 section, since it tracks `_drafts/` only, leaving 45.

---

## The Corrections That Went Live With It

---

## The Contradiction Is Resolved, and I Had Guessed Its Cause Wrong

**The two totals are not two targets.** That was my inference from your "different measurements" ruling and
the engineering session has given the real answer. They are **two orthogonal axes**.

| | O0 | O2 |
|---|---|---|
| fixed provisioning, which is A371's world | 298,192 | 275,432 |
| on-demand provisioning, landed after A371 | 43,240 | 23,976 |

The optimisation-level axis is 298,192 to 275,432, **7.6 percent**, and that is A371's story. The code-change
axis is 275,432 to 23,976 at O2, **91.3 percent**, and that is a later fix which is not.

**So I removed the paragraph I had written claiming the frame total is a property of the target.** It was
unsupported by the evidence it cited, and the 8 percent is corrected to 7.6 throughout.

---

## Item 4 Is Withdrawn, and I Reversed What I Had Applied

Composite bodies belong in the arena, not on the machine stack, so the frame-growth concern does not arise.
The Threats to Validity paragraph I added about aggregate lowering reintroducing allocations is **deleted**.

---

## Item 5 Narrows the Article's Central Claim, and the Article's Own Equation Already Knew

**The memory bound is a pair and the article had been reading it as one number**, although its own displayed
equation writes it as a sum. Separating the terms is the whole of item 5.

- **The arena term transfers exactly.** Native code allocates from the same fixed-size arena in the same
  bytes, and the memory-bound pass already sums every allocation. No argument is required beyond noticing
  that the arena is the same object.
- **The operand-slot term has no native counterpart.** It counts slots on the interpreter's operand stack.
  Native code has no operand stack, so comparing that term to a machine frame **compares two different
  things**, which is why it came out as badly as it did.
- **The machine frame is a third quantity** that the bytecode never described and that needs its own bound.

Result 1's heading is now **One Term of the Memory Bound Transfers Exactly and the Other Describes Nothing
Native**. The lede, the summary, the conclusion, the strongest-claim paragraph and the central-promise
passage were all narrowed to match, and the no-constant equation was rescoped from a generic memory
superscript to the frame against the operand slots, **since a claim about the whole memory bound is exactly
the overreach item 5 removes.**

**Every measurement is unchanged.** What changed is which of the three quantities each one is about.

**And the recommendation is now concrete instead of despairing.** Allocate dynamic data from the arena, where
the bound already transfers, and bound the machine frame separately from the artefact. The article says
plainly that neither of those is research.

---

## The Earlier Corrections, Which Still Stand

**Items 1 and 2 are applied and they strengthen Result 1.** The optimiser promotes the allocations into
*virtual* registers, of which the compiler may invent any number, and a target with roughly fourteen usable
registers spills most of the 64 operand slots straight back. **The provisioning is relocated, not removed**,
and the article now says the count going to zero is a fact about the intermediate representation and not
about memory.

The deferral is gone. Its stated reason, that the stack-size section is ELF-only while the host produces
Mach-O, **confused the host with the target**, since a compiler cross-targets by construction. A new
subsection reports that **every module's frame exceeds the bound proven of its bytecode by two to thirteen
times**, which is the dangerous direction, and that **no constant rescues it**, four modules sharing a proven
bound of 64 bytes against frames of 520, 600, 632 and 824.

**Item 3 needed no action, and I checked rather than assumed.** The retrospective claim about A369's rate
**appears in neither the blog draft nor the Keleusma source draft.** The only sibling comparison A371 makes
is to A370 at 35 of 35.

---

## The Contradiction, As I First Reported It

Item 1 gives a corpus frame of 298,192 at O0 against **275,432** at O2, an 8 percent reduction. Item 4 and
the A372 source draft give a corpus frame total of **23,976** and describe a **91 percent** frame reduction.
Against a common O0 those are 7.6 percent and 92.0 percent, and they cannot both hold. **Item 1's reduction
of 22,760 is also close to A372's total of 23,976**, which reads like a frame and a saving swapped.

You ruled they are different measurements, so **the article now names the target beside the figure** and
reports 298,192 against 275,432 for `x86_64-unknown-linux-gnu`. I added the consequence rather than just the
caveat: **a total that moves when the target moves was not determined by the bytecode**, which is the
article's own thesis arriving from a second direction.

**Item 4 was applied without naming A372.** A371 is dated 2026-08-08 and A372 does not exist in this
repository, so a `post_url` would fail the entire site build and even a prose forward reference breaks the
back-reference-only convention. Threats to Validity now records that planned aggregate lowering would
reintroduce allocations into the same frame, so the 8 percent is a measurement of one commit.

---

## The A369 Addendum, With One Row Corrected Before It Shipped

Added as you asked, framed as later data, withdrawing nothing.

**The note's own table was wrong about A370.** It reports 31 identifiers checked. **A370's published text
says 35 in four separate places, and its pipeline's `hand_research.json` holds exactly 35 entries, all
DOI-based.** The row now reads 35.

Two things to be aware of. **Two of the four rows describe articles that are not yet published**, so a reader
cannot currently check them. And **neither set of frame measurements was independently reproduced here**,
because the LLVM 22 toolchain the Keleusma test expects is absent from this host, which carries 14 and 19
only. They are recorded as the engineering session reports them.

---

## The Shared Title, From an Earlier Commit

The three articles now read **Keleusma Research Spike** followed by their own subtitle.

- A369, `Blocking Frequency as the Ordering Principle for Instruction-Set Coverage`
- A370, `When an Apparent Design Wart Is a Semantic Boundary`
- A371, `What a Verified Bound Says About the Code That Actually Runs`

**I checked the URL risk before touching anything and it is nil.** `_config.yml` carries no top-level
`permalink:`, the `permalinks:` key belonging to `jekyll-archives`, and none of the three files carries a
`slug:` override. Jekyll's default permalink therefore takes `:title` from the **filename**, so a
front-matter title is URL-neutral and **no `redirects/` entry is needed**. Confirmed afterwards against a
production build, with both live URLs resolving unchanged.

**The comment threads were the risk that mattered more, and they survive.** `_includes/comments.html` sets
`data-mapping="pathname"`, so Giscus keys its GitHub Discussions to the URL path. **Had it been set to
`title`, this change would have orphaned every existing comment thread on two published articles.**

**The link-text convention had to change with the titles.** Related-post entries carried the main title
alone, which under a shared main title would make three different links read identically. They now carry
the subtitle. Three were updated, one in A370 and two in A371.

Two consequences worth your eye. The series navigation now lists two entries both beginning
**Keleusma Research Spike**, distinguished by their Part 1 and Part 2 labels, which reads acceptably but is
repetitive by construction. And **historical TASKLOG entries still name the old titles**, which I left
alone deliberately, since they record what was true when written.

---

## The Word Usage Pass, From the Previous Commit

**`specific` is not a problem here.** It stands at **6 uses for 0.82 per thousand**, well under the limit
and under the corpus median. I checked it first because you named it.

**The measurement had to exclude the harvest or it could not fire at all.** The article carries 331,800 raw
body words against **7,403 words of author prose**, so measuring the raw body would divide every rate by
about forty-five and guarantee silence. `diction.prose` strips link pairs, which is the fix made after A369
found that defect, and it is the only reason this article is measurable.

**Every existing instrument looks at single words, and A369's largest finding was a phrase.** `_verify.py`
watches a fixed forty-seven word class. A369's `and not` reached 2.19 per thousand against a peer maximum
of 1.73 **because an earlier pass had mechanically rewritten `rather than` to clear a single-word limit**,
which is a trade no single-word instrument can see. I added `tmp/a371/phrases.py`, which ranks two- to
four-word constructions against 254 published peers, counting a peer that never uses a phrase as a zero.

**It found 37 constructions at or above the peer maximum, and the real ones were my own boilerplate from
the previous pass.** Six survey subsections opened with `The harvest returned N further contemporary
records in this cluster`, identical but for the number, and four more used `N contemporary records concern
X`. **Ten template sentences now carry a fact about their own cluster instead of restating a count the
reader can already see.** The count fell to 26, and every survivor is subject vocabulary measured against a
corpus of aircraft articles.

**A sense collision on a defined term.** `artefact` is this article's name for $A$, the thing a property was
established about. The Epistemic State also used it in the ordinary measurement sense, saying none of the
four errors "was an artefact of the checking method". It now says false positive.

**Two content redundancies that the word count found and reading had not.** The coverage claim was stated
almost verbatim in both the Source Base and the Epistemic State. And a harvested-list lead I wrote in the
previous pass repeated the hand prose three lines above it, that the theorems are about observable
behaviour.

**`about` remains above the peer maximum and I did not reduce it mechanically.** It sits at 6.08 per
thousand against a peer maximum of 5.28. **42 of its 45 uses are the aboutness sense the thesis is written
in**, being a property established about one artefact and claimed about another, and 3 are the
approximation sense. I classified all 45 rather than asserting the reason. A369's standing lesson is that a
mechanical substitution is not an edit, and trading `about` for a synonym here would move the tic rather
than remove it.

`rather` stands at 28 for 3.78 per thousand. The `three distinct magnitudes` refrain was varied in three of
seven places, in each case where the wording and not the claim was the repetition.

---

## The Corpus-Wide Outliers Are Mostly Not Tics, and One Is

Since you gave `specific` as a recurring example, I ran the corpus-wide check and triaged by collocate,
which is the only thing that separates a topic from a tic.

- **`specific` at 15.07 per thousand is `specific impulse`**, 86 to 99 percent of uses across the rocket
  propellant chemistry articles. It is the term Isp and must not be touched. `_verify.py`'s own comment
  already records this.
- **`key` at 18.26 per thousand is the cryptographic key** in the Solana and SSH articles, `key pair` and
  `key file`. A subject noun.
- **`typically` at 6.88 per thousand in the published search and rescue drone article is a genuine hedge.**
  Its collocates are all verbs, being `typically completes`, `typically budgets` and `typically holds`, so
  it modifies claims rather than naming a thing. **I flagged it and did not touch it**, because it is a
  live published page and outside what you asked for. Say the word if you want it fixed.

---

## The Substantive Gap Was the Survey, and the Numbers Say So Plainly

A369 carries 1,759 research references. A370 carries 1,980. **A371 arrived with 28**, which is a factor of
about sixty-five against your standing instruction that every article in this series serve as a
comprehensive survey of the contemporary literature.

A harvest of **119 queries across fifteen clusters in seven rounds** retrieved 60,091 records. The anchor
gate admitted 11,604 and **11,068 reach the reference list**, beside the 28 hand-selected works, which are
untouched and remain the only ones read. The article says so in its own Source Base and Epistemic State.

**27 of the 28 hand-chosen works were independently returned by the harvest.** That is the best
corroboration of coverage available, because those 28 were chosen before any query ran.

---

## The Largest Defect Was a Venue Filter, and It Took Two Corrections to Find the Bottom

The first rounds requested **journal articles only**, which is the right choice for the aerospace articles
this machinery was built for and the wrong one for computer science. Those rounds returned 19,169 records
and **not one paper from the CerCo project**, which is the research programme the article itself names as
the closest existing work to its own problem.

**Adding conference proceedings more than doubled the corpus and still returned no CerCo paper.** The
reason is that **Springer deposits its Lecture Notes in Computer Science volumes as `book-chapter` rather
than `proceedings-article`**, so an LNCS proceedings paper is typed as a chapter of a book. A third pair of
rounds recovered both papers the article cites by hand.

**No count could have found this.** Each of the first two attempts produced a corpus that was large,
plausible and missing the same thing. It was found only by probing for a named project the survey was known
in advance to require, which is now the method I would use first rather than last.

---

## A Silent Structural Defect in My Own Gate

Every qualified anchor was written as `X(?=.*Q)`, which requires the qualifier to appear **after** the
anchor. `Crafting a Java virtual machine in silicon` was therefore refused, because Java precedes the
phrase. Rewriting every qualifier as a pair of lookaheads evaluated from the start of the title
**recovered 303 records**.

**The cost family was admitted unqualified**, so a Handbook of Army Cost Analysis Terms, a
refuse-derived-fuel cost model and a cost-effectiveness compilation for heart conditions reached the kept
set. The harvest's own notes warned that `resource` cannot be filtered and then **failed to apply the same
reasoning to `cost`, which is worse**, because `cost analysis` and `cost model` are complete phrases in
accounting rather than words merely shared with it.

Tightening it then **collapsed the cost cluster from 52 to 3**, which is the signal that a tightening has
gone too far. Reading the 144 rejects found **four genuine losses**, including `Cost Relation Systems` and
`Closed-Form Upper Bounds in Static Cost Analysis`, each refused by a qualifier that was correct and too
literal, wanting `type system` against `type-theory`.

**A literal space in a multi-word anchor refuses the hyphenated spelling.** That is the **seventh** time in
this corpus that a spelling variant has returned a smaller corpus rather than a wrong one.

---

## Seventeen Homonym Families, Found by Reading Four Samples and Not by Anticipation

`_research/homonyms.py` goes from 41 to 56 noise patterns. **Four independent samples of thirty were read,
each found families the previous had missed, and the last one still found one.** A survey reporting a clean
sample would be reporting that it stopped looking, and the article says that in its Epistemic State.

The families include Stack Overflow the website against the stack overflow condition, circuit timing
signoff against software timing analysis, **three separate senses of just-in-time** being manufacturing,
instructional delivery and commit-time defect prediction, formal semantics in linguistics, the peephole in
critical theory, semantic preservation in natural language generation, the calendar timing anomaly in
finance, Java the island together with pre-stack seismic imaging, static analysis in geotechnical
engineering, the cloud virtual machine, web cache replacement, and software cost estimation.

---

## Two Load-Bearing Citations Were Silently Repointed, and an Off-By-Two Found It

`refs.assign_anchors` builds an anchor stem from first author and year, so **`Necula 2000` names two
different papers**, being the hand-cited translation validation work and a harvested proof-carrying code
abstract. The harvested record took the stem and the merge then replaced the hand entry, so **the prose
citations of Necula 2000 and Pnueli 1998 resolved to the wrong works**.

**This is the exact defect class the article reports having committed four times**, reproduced by my own
tooling in the same sitting. It was found by an off-by-two in the reference count and by no checker. The
hand anchors are now reserved, and the assembler **raises on any collision** instead of merging over it.

Separately, `hand_selected_keys` read the draft, **which is this pipeline's output**. Once a harvest was
assembled it reported 11,094 hand-selected references, treated the whole harvest as already cited, and
emitted a master set of one record.

---

## The Count in My Own Prose Was Wrong by Eight

I wrote that **nine** homonym families were recorded. The store held **seventeen**. That is the same
count-in-my-own-prose defect this article family has now shipped three times, so the count is now derived
from the store, and the assembler **raises if the prose list length disagrees with it**.

Three superlative claims were checked against the numbers that actually landed and corrected. Worst-case
execution time is fourth largest and not second. Real-time certification is largest only among the named
clusters, since the adjacent bucket is larger. And the cost cluster is more than two orders of magnitude
smaller, not roughly two.

---

## The Two Defects Carried Over From the Equation Pass

**The stale identifier count is fixed.** The Epistemic State now says the bibliography was submitted with
27 identifiers of which four were wrong, and that a twenty-eighth was added during editing and resolves,
which describes what happened instead of renumbering the error rate.

**The claim about A370 was wrong and is corrected.** A371 said A370 "resolved 31 of 31". A370's own text
states 35 hand-selected references and 35 resolved. It now reads 35 of 35.

---

## Style and Verification

- `python3 _verify.py` **0 errors, 0 warnings**.
- `python3 _lib/test_lib.py` **75 of 75**.
- `./_check.sh --drafts` **passes end to end**, 506 pages, no findings.
- Reference integrity **11,112 used against 11,112 defined**, zero undefined, zero orphaned, zero duplicate
  definitions, zero malformed list entries.
- **All 28 hand-selected identifiers resolve.** The 403 responses are ACM and the 202 responses are IEEE,
  both documented publisher behaviour, and the single failure was a transient name-resolution error
  confirmed afterwards against the registry, which returned the exact cited title.
- A sample of 12 harvested identifiers resolves.
- Prose clean with zero em dashes, zero en dashes, zero prose parentheticals and zero prose semicolons
  outside mathematics. Two prose colons removed.
- `rather` brought back under the corpus maximum with eight rewrites, **each checked for grammaticality
  rather than substituted mechanically**, which is the lesson A369 paid for.

---

## Outstanding, and One Thing I Did Not Decide for You

**It is committed and pushed, and it is not published**, which is what you asked for.

**Publishing it would put it live immediately**, because 2026-08-08 is in the past. It sits behind A370 in
the series, so publishing would also renumber the two published articles' navigation from "Part 1 of 2" and
"Part 2 of 2" to "of 3". **That is a change to two live pages and I have not made it.**

**The X-Planes work is untouched by this.** A335 remains the last of thirty-nine drafts, all four passes
done, **none published and none authorised**, and **A336 is X-39, Reserved but Never Assigned**, a
designation anomaly taking the reduced section order. The handoff at `_docs/process/HANDOFF.md` describes it
and should be re-validated against `git rev-parse HEAD~1` before it is trusted, since this commit moves the
head.

**One item is outstanding elsewhere.** The engineering session reported that **A372 carries the same
stack-allocation error** corrected here and needs its own correction file. That is their next action and no
part of this repository.
