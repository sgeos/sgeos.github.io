# Research Agent Pattern

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

The pattern for using a background research agent to verify factual claims, dates, numbers, and URLs in an article before publication.

## When to Use

Any article with substantial factual content benefits from a research agent pass. The pattern proved out across the analog-facilities series, where the agent caught dozens of date drifts, numerical errors, URL relocations, and acronym misattributions before publication.

## Procedure

1. Compose a focused research-agent prompt listing the specific claims, dates, numbers, and URLs the article will use. Number each claim for the agent to address. Avoid open-ended research; the agent works best with a punch list.
2. Launch the agent in background while drafting the structure and prose. The two activities are independent.
3. When the agent returns, apply corrections immediately to the draft. Common correction categories:
   - Date refinements, for example a mission conclusion that the article had as ongoing.
   - Numerical refinements, for example a closure ratio or efficiency that the article had at the wrong magnitude.
   - Acronym expansions where the spell-out was missed.
   - URL replacements where a referenced page has moved.
   - Caveat additions where claims oversimplify, for example a theoretical maximum versus a practical achievable value.
4. Anchor any "current" or "as of" claims to the actual drafting date by including "today is YYYY-MM-DD" in the prompt.

## Prompt Template

```
Verify and gather authoritative public-source facts for an academic blog article on "<title>".
<one-paragraph article summary including framing and keystone>
Today is YYYY-MM-DD.

Verify or correct the following claims and provide canonical URLs
(prefer Wikipedia, NASA, ESA, .gov, .edu, peer-reviewed; flag any that require manual web-search):

CATEGORY ONE:

1. <Specific claim with the article's stated value>. Verify or correct.

2. <Specific claim with the article's stated value>. Verify or correct.

CATEGORY TWO:

3. <Specific claim with the article's stated value>. Verify or correct.

...

For each verified item, provide:
- The claim as currently stated
- Correction if needed
- A canonical URL that responds to curl
- Note any URL that requires manual web-search verification

Flag any uncertain, contested, or contradicted claims. Report under 1800 words.
```

The numbered claims make the agent's response easy to apply mechanically. The word budget keeps the response focused.

## After the Agent Returns

Apply corrections in order of impact. Critical corrections come first:

- Factual errors that misstate dates, numbers, or causation.
- URL replacements for 404 destinations.
- Acronym spell-outs that were missed.

Stylistic refinements come after the corrections. The reviewer's energy is on correctness, not polish.

Update the draft summary or the REVERSE_PROMPT to record the corrections applied. The publication-side artifacts should reflect what the published article actually says, not what the draft originally claimed.

## Related Sections

- [Publication Review](./PUBLICATION_REVIEW.md) for the broader review pass
- [URL Verification](./URL_VERIFICATION.md) for the URL-check step
- [Common Errors](../reference/COMMON_ERRORS.md) for recurring factual traps


## The Harvest Anchor Gate

A harvested reference corpus is admitted by a subject-anchor gate. **Build the gate for the article's
subject and never copy one from a previous article.** `_lib/gate.py` carries the shared machinery and
the failure history.

```python
import gate
g = gate.Gate([r"compiler|bytecode|coroutine|calling convention"], name="a370")
kept, dropped = gate.select(records, g)
gate.audit(kept, dropped, seed=20260811)     # READ THE OUTPUT. This is not optional.
```

**The same defect has shipped twice, in opposite directions, and neither was visible in any summary
statistic.**

- **A333** inherited an aeronautics gate and applied it to a compiler-science pool, rejecting 2,174
  titles for containing no aircraft and rejecting the article's oldest primary source. A narrow gate
  reports a small corpus, which reads as a thin literature rather than a bug.
- **A370** rewrote the gate and overcorrected, admitting generic stems such as analysis,
  implementation, generation and performance. It took in rabies control, seismic depth imaging,
  veterinary breeding soundness examination and fibre art. A permissive gate reports a large corpus,
  which reads as thoroughness.

**Only reading a random sample detects either one.** Cluster distributions and drop-reason tables look
plausible in both cases. `gate.audit` samples the kept side, which catches a permissive gate, and the
dropped side, which catches a narrow one. Its `seed` argument is required so a reviewer can reproduce
exactly what was read.

**Re-run the metadata pass after any gate change.** Widening a gate after the detail pass leaves newly
admitted records without metadata, so they never reach the master set and nothing reports an error.
