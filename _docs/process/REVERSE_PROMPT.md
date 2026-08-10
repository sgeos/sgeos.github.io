# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-09
**Task**: A323 equation-density review, the second of four passes. Committed. **Not pushed.** **Not
published.** All twenty-seven articles in the series remain in `_drafts/`.

**17 display equations to 35**, across twelve edits each asserted to match its anchor exactly once,
taking the article from 3,613 to 3,785 lines and 12,061 to 13,226 words.

---

## The Largest Omission Was the Relation Everything Rests On

**The drag polar was never displayed.**

    C_D = C_D0 + C_L^2 / (pi e A)

**That second term is the common root of both halves of the article.** It is what makes the
lift-to-drag ratio high, because it falls as aspect ratio rises. **And it is what makes a rolling wing
drag asymmetrically**, which is the adverse yaw the whole first half is about. The article derived
from this polar twice and displayed only its consequences.

Two further assertions had no derivation behind them. **Where the elliptic result comes from** is one
line, since rolling changes local incidence by `p y / V` and therefore local induced drag. **And the
helix angle was called a property of the configuration without proof**, when writing the steady roll
balance down is exactly what shows the speed dropping out.

---

## Best Glide Is Not Minimum Power, and the Quiet Aircraft Wanted the Second

**The draft did not distinguish these and they are different speeds.** Minimising power puts the
parasite term at three times the induced one, where maximising lift-to-drag puts them equal.

    C_L,mp = sqrt(3) C_L*      V_mp = V_bg / 3^(1/4) = 0.760 V_bg      (L/D)mp = 0.866 (L/D)max

**A 12.3 percent power saving for flying 24 percent slower.** For the QT-2PC that puts best glide at
81.5 miles per hour and minimum power at 62.0, and **the quoted quiet cruise of 70 to 80 falls between
them**, which is what an aircraft needing both endurance and a speed margin does.

**The noise value of that choice is 0.57 decibels.** Saying so keeps two motives from being confused:
**the loiter speed was chosen for endurance, not for quiet.**

---

## And It Supplied a Second Independent Check

**Minimum sink is the minimum-power condition, and minimum sink is a quoted number.** Predicted **129
feet per minute at 42 miles per hour against a quoted 124 at 46**, which is 4 percent in sink and 10
in speed, **from the same two assumed parameters that produced the glide ratio and with no further
fitting**.

**One polar now reproduces two independent quoted figures.** That is worth considerably more than
reproducing either alone, and it was available in the draft without being taken.

---

## The One Logarithm Behind the Sharpest Acoustic Claim

**The article asserted that the limit moved to the exhaust and airframe once the propeller was slowed,
and never showed why it must.** Incoherent sources add in power,

    L_total = 10 log10( sum of 10^(Li/10) )

so **quieting one source has a ceiling set by the others**. With the propeller starting ten decibels
above everything else, a **seventeen decibel propeller reduction buys ten**, and removing the
propeller entirely buys 10.4 and no more.

**A related pair of numbers turned out to be one statement.** A detection range is a slant range, so
above 750 feet the detection sphere cannot reach the ground at all. **The 750 foot detection distance
and the 800 foot minimum mission altitude are the same fact with fifty feet of margin**, which is a
cleaner reading of the record than treating them as unrelated.

---

## The Verifier Caught a Wrong Number in the New Material

**A stall prediction of 45.9 miles per hour from an assumed maximum lift coefficient of 1.4 is wrong
by five miles an hour.** The true value at that coefficient is 40.9.

**The claim was replaced by inverting the relation rather than by adjusting the assumption.** The
stall cannot be predicted without knowing the maximum lift coefficient, but the quoted 46 miles per
hour can be asked what coefficient it implies, which is **1.11 at the light weight and 1.47 at gross**.

**That turned an error into a better finding.** A coefficient of 1.11 is entirely ordinary for an
unflapped sailplane section and 1.47 is high for one, so this is a **third independent piece of
evidence that the quoted performance figures belong to the lighter aircraft**, agreeing with what the
glide-speed reconciliation already showed.

---

## Two Defects Found by Reading

**A doubled backslash survived an rf-string once more**, in a file whose own docstring warns against
exactly that. It is now the third occurrence across three articles and it passes every automated check
every time.

**Two adjacent equations stated the same sink relation with different symbols** and were merged.

**Five sentences referring to what the draft had said were removed**, applying the A322 lesson at the
first opportunity rather than waiting for the publication pass to find them.

---

## Verification

**Numerical.** Extended from 40 to **74 independent checks**, none importing the calculation. Minimum
power is found by **scanning the power curve** rather than by the analytic factors, and the searched
ratio is then required to equal three to the minus one quarter. The incoherent-addition ceiling is
verified **as a limit rather than at a point**, by confirming that no reduction however large can
exceed it. The inverted maximum lift coefficient is required to reproduce the quoted stall on a
forward pass. **All pass, and every value was required to appear in the draft text.**

**Build.** Twenty-seven article isolated build, all 35 equations rendering as display math, zero
mangled escapes, zero duplicates, Part 27 of 72.

**Corpus.** `_verify.py` at 0 errors and 21 warnings. Style and integrity clean across all
twenty-seven articles.

---

## State

**A323 has two of four passes complete. Committed, not pushed, not published.**

**Expected next is the primary-reference review.** The coverage audit will need rewriting for this
subject, since the topic list it currently carries is A322's rotor vocabulary.

**Still open and unchanged.** The fourth genre class, now **fifteen** consecutive articles. The A305
length offer.
