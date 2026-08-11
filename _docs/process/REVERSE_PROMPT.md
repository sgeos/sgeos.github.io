# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-11
**Task**: A370 equation-density review. **Committed, not pushed.** **Not published.**

**21 display equations to 31.** The article moved from 8,937 to 9,812 words, with references unchanged
at 53 definitions.

---

## The Pass Nearly Broke a Sound Argument, and That Is the Main Report

**The article's central claim is that a terminating coroutine must convey two events from one call, and my
first reading concluded it was wrong.** The obvious objection is that the completion can simply arrive on a
second call, which would make the deficit one bit of discrimination rather than one word of capacity.

**Re-reading the convention showed the objection fails, and the reason was in the article all along without
being connected to this argument.** The return convention has no resumption point. The host calls a plain
function again with the resume value as the argument, so a second call **re-runs the body from the top**,
suspends again, and never reaches the completion. For a divergent chunk that is exactly right, because the
reset instruction rewinds to the same place and clears every local. **For a terminating chunk it means the
first call is the entire budget.**

**I have displayed the re-entry so the one-call budget is derived rather than asserted**, because a reader
will raise the same objection I did and the article did not answer it.

---

## The Deficit Is One Bit, Not One Word

**Two designs were being run together and they cost very different amounts.**

| Design | States needed | Bits | Shortfall |
|---|---|---|---|
| Cram both events into one call | $\lvert W \times W \rvert = 2^{128}$ | 128 | **a whole word** |
| Re-enter with a discriminator | $\lvert \{\mathsf{Y},\mathsf{F}\} \times W \rvert = 2^{65}$ | 65 | **one bit** |

That single bit is what forces a second register, since $\lceil 65/64 \rceil = 2$, **and it is the whole
reason the register-pair rules in the two application binary interfaces matter to the decision.** The
option the article calls expensive costs one bit of information and one register of encoding.

---

## A Confidence Bound Turns a Slogan Into a Number

The article says no quantity of confirming instances establishes a universal claim. **True, and the
measurement is weak even on its own terms.** Reading nine successes from nine trials as a sampling exercise,

$$p_{\min} = \alpha^{1/n} = 0.05^{1/9} = 0.7169,$$

so **the observation is consistent with 28.31 percent of cases failing**, falling to 0.5995 at 99 percent
confidence. Licensing a claim of 0.99 would need **299** consecutive successes.

**The article is careful that this is the weaker objection.** The counting argument does not need the sample
to be small and would refute the unification from a sample of a million.

---

## Three Smaller Additions

**The deficit does not grow with suspension count.** At $n$ suspensions the collapse factor is
$\lvert W \rvert^{n}$, catastrophic at every $n$ and no worse in kind at nine than at one, **so the
smallest instance really was the right one to check.**

**The over-strict rule now has its coverage stated**, at 58.33 percent admitted against 100 percent
licensed, losing 41.67 percent.

**The sentinel's cost is exact**, at 18,446,744,073,709,551,615 usable values and a loss near
$5.421 \times 10^{-20}$. **Negligible in measure and total in reachability, and only the second matters.**

---

## Something I Wrote and Deleted

**I first costed the two surviving options with a table of nanoseconds per call and a one-off cost in
equivalent nanoseconds, and then removed it.** Inventing both constants produces a crossover that is a fact
about the invented numbers.

What replaced it is the structure, which needs no measurement. One widened convention pays a discriminator
on every call and two conventions pay a constant, so the totals are $c_{\mathrm{tag}} N$ against
$c_{\mathrm{meta}}$ and the crossover is $N^{*} = c_{\mathrm{meta}} / c_{\mathrm{tag}}$. **A per-call term
always loses to a constant eventually**, and the article says both constants are unpublished rather than
guessing them.

---

## Verification

- `python3 tmp/a370/verify.py` **34 of 34**, by a verifier that does not import the calculation. The
  confidence bound is checked by **Monte Carlo over 200,000 trials** rather than by evaluating the closed
  form, the pigeonhole by **exhaustive enumeration at one to four bit words** rather than by cardinality,
  and both tail segments by **simulating a stack machine** rather than by summing a table of deltas.
- `python3 _verify.py` **0 errors, 21 warnings**, the unchanged baseline, from the repository root.
- `lint.scan` **clean**, after a reflow verified a fixed point and content-preserving.
- **Prose scan clean** of em dashes, en dashes, contractions, prose colons, prose semicolons and italics.
  The only parentheses are mathematical notation, which the style guide permits.
- **Isolated build exit 0**, with **31 open and 31 close display-math delimiters**.
- **The comma-spacing trap fired**, on a sentinel figure present only inside a display where LaTeX comma
  spacing flattens it. Stated in prose as well.

---

## Next

Your call. Two of the four passes have now been applied to A370, being the standards brush-up and this one.
**A primary-reference review and a publication review have not**, and the article currently cites only
primary documents by design, so a reference pass would be a larger change of character than it was for the
X-Planes articles.

The X-Planes series is unchanged at **thirty-seven of seventy-two**, none published, with **A334, the Boeing
X-37, next** whenever you want it.
