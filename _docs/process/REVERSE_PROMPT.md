# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

## Last Updated

**Date**: 2026-09-07
**Task**: **A351, X-Planes: Gulfstream X-54, equation-density review. The second of four.**
Committed and **not pushed**, which is what this pass asks for. **Not published**, and publication of
the series still not authorised. **Fifty-five of seventy-two drafted.**

**Eleven display equations to thirty-one.**

---

## The Pass Changed a Conclusion Twice, Which Is What It Is For

**Adding the equations was not the point. Working them was.** Two of the article's own claims did not
survive being computed properly, and both errors ran in the direction that flattered the argument.

### The Draft Divided by the Wrong Distance

**A boom does not travel straight down.** The ray leaves normal to the Mach cone, so it makes the Mach
angle with the vertical and the path from 45,000 feet at Mach 1.4 is

    r = h / cos(mu) = h / sqrt(1 - 1/M^2)

which is **19,598 metres and not 13,716**. Every percentage in the draft's coalescence table was too
large by 42.9 percent. **The correction makes the finding stronger, which is exactly why it was easy
to miss.**

### And the Conclusion Is Conditional, Which the Plane-Wave Form Hid

**The draft said the coalescence result did not depend on the assumed shock strength.** It looked that
way because dividing a fixed closing rate into a fixed separation scales the same at every strength.
**Adding geometric spreading breaks that.** Both shocks weaken as roughly the inverse square root of
distance, so integrating

    ds/dr = -((gamma+1)/(4 gamma)) delta_0 sqrt(r_0/r)

to zero separation gives `sqrt(r_c) = sqrt(r_0) + L/(2 sqrt(r_0))`, where `L` is the plane-wave answer
and `r_0` is one aeroplane length.

| Strength difference | Plane wave | With spreading | Share of the ray path |
|---|---|---|---|
| 0.01 | 1,729 m | 40,177 m | **never completes** |
| 0.02 | 864 m | 10,491 m | 53.5 percent |
| 0.05 | 346 m | 1,902 m | 9.7 percent |
| 0.10 | 173 m | 577 m | 2.9 percent |

**At the weakest strength in the range the shocks would still be separate when they arrived.** The
finding holds at 0.02 and above, which is where an aeroplane the size of an F-15 sits. **So the
programme's stated reason is right about its own aeroplane and is not a general truth about spikes**,
and the article now says the smaller thing.

---

## Symbols Collided Four Times and a Table Now Prevents It

**`T` was the temperature, the N-wave duration and the sound-exposure reference time.** **`L` was the
atmospheric lapse rate, the coalescence distance and the sound pressure level.** **`R` was the gas
constant and the ground reflection coefficient.** **`\ell` was the lift per unit length and the shock
separation.** A349 shipped the same class of defect using `m` and `n` for two things each.

**`verify_numbers.py` now carries a declared symbol table and refuses anything undeclared.** A regex
cannot know what a symbol means, so the instrument is the table plus the refusal, and maintaining it is
what catches a collision because a second meaning has nowhere to go. **It was proved non-vacuous by
injecting an undeclared symbol and watching it fail.**

**The check itself was wrong on its first run** and reported LaTeX operators as undeclared symbols,
because `\int_{0}` is `\int` followed by an underscore and a trailing word boundary never matches one.
**A broken diagnostic reports the data as broken**, which is the direction that wastes work.

---

## A Pipe Masked a Failed Assembly and the Verifier Validated Stale Bytes

**`python3 assemble.py | tail -3 && python3 verify_numbers.py` reports the exit status of `tail`**, so
a failed assembly let the verifier run against the previous draft and report all checks passing.
**A checker that silently validates stale output is worse than no checker.** `verify_numbers.py` now
refuses to run when `body.md` or any input JSON is newer than the draft, which is cheaper than
remembering to set `pipefail`.

---

## What Was Added

**Twenty new display equations.** The speed of sound; the ray path from altitude; the N-wave waveform
and its positive-phase impulse; the total lift term in the equivalent area and the resulting
square-root weight scaling; the von Karman wave-drag integral; the two standard-atmosphere layers; the
dynamic pressure in its pressure-and-Mach form; the aging length; the spreading-corrected coalescence;
the Taylor shock profile; the ray invariant for a stratified medium; the sound pressure level; the
ground reflection factor; the threshold as a pressure ratio; the effective sound speed with wind; the
lateral cutoff azimuth; and the turning altitude.

**Three of them produce numbers the article had no way to state before.**

- **The dynamic pressure relation is a check on the record and the record passes it.** The Quiet Spike
  report gives 685 pounds per square foot at Mach 1.8 and 45,000 feet, and inverting the relation at
  that altitude gives **Mach 1.782**.
- **The turning altitude collapses fast.** At Mach 1.10 the ray turns at 4,001 metres and at Mach 1.15
  at 251 metres, so five hundredths of Mach take the shadow zone from 13,125 feet to 823. **The
  technique that actually changed the rule is a forecast rather than a chart.**
- **The threshold in acoustic units.** 0.11 pounds per square foot is 5.27 pascals, **108.4 decibels
  peak** against roughly 133.6 for a Concorde at cruise, and one part in 19,000 of ambient.

**And one is an engineering tension the article had stated only in words.** Wave drag is a functional
of the same second derivative that sets the F-function, so **the boom and the drag are two functionals
of one function** and the distribution minimising one does not minimise the other.

---

## Two Passages Narrated the Article's Own Drafting History and Were Rewritten

**A reader has no access to a superseded draft.** The corrected position is now stated directly in the
argument and the correction itself lives in What the Data Changed, which is the A345 rule and the
section that exists for it.

---

## Counts

| Quantity | Draft pass | After this pass |
|---|---|---|
| Lines | 6,745 | 6,891 |
| Words | 39,473 | 41,392 |
| Display equations | 11 | **31** |
| Reference definitions | 3,159 | 3,159 |
| Prose citation labels checked | 41 | 48 |

**References were not touched by this pass**, which is the next one's job.

---

## Open Questions for the Pilot

**A324's `book_jenkins` label remains the one live repair**, unchanged.

**The OpenLibrary work pages returning Internal Error to a reader** is also unchanged.

**Nothing is pushed.** The next prompt in the rhythm is the primary-reference review.
