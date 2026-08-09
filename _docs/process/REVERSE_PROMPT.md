# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-09
**Task**: A318 equation-density review, the second of four passes. **Committed, not pushed. Not
published.**

**16 display equations to 45**, across 16 edits, each asserted to match its anchor exactly once. 827
lines to 949, 6,664 words to 7,831.

---

## The Pass Found a Defect, and It Favoured the Wrong Side

The draft assumed a whole-aircraft zero-lift drag coefficient of 0.0180 and then computed the friction
saving as $\Delta C_f$ times the laminarised wetted area, with no form factor.

**Those two are inconsistent.** A coefficient of 0.0180 is only reachable if the friction contribution
carries a form factor, so **the aeroplane was being charged form-factored drag and credited flat-plate
drag**.

Building the coefficient from its parts removes the possibility and reproduces the assumed value,

$$C_{D_0} = 1.20 \times 0.002713 \times 4.0 + 0.0050 = 0.01802$$

which is the check that the decomposition is the right one. **The corrected benefit is larger, not
smaller.** Drag reduction 0.087 becomes 0.108 and the range gain 9.5 percent becomes 12.1 percent.

This is the thirteenth article in which writing the relation down caught a wrong claim.

---

## A Cross-Check the Draft Did Not Make

The article opens by asserting, from the literature, that about half a transport's fuel goes to
overcoming skin friction. The drag build-up gives the friction share independently,

$$\frac{k \, C_{f,\text{turb}} S_{\text{wet}} / S}{C_D} = \frac{0.01302}{0.02857} = 0.456$$

**One number came from the literature and the other from geometry and a flat-plate correlation. They
agree to about nine percent.** Nothing prompted that check except looking for one.

---

## A Question the Draft Posed and Did Not Answer

The draft observed that the 1963 case for laminar flow control promised a lift-to-drag ratio above thirty
and that the table of laminarisation fractions did not reach it. It did not ask why.

**It is not reachable on this planform at any level of laminarisation.** Laminarise the entire aeroplane,
fuselage included, which is impossible but bounds the argument, and the answer is 23.1. The reason is
visible in the budget. A ratio of thirty allows a total drag coefficient of 0.01435, and induced drag
alone is 0.01055, or **73 percent of the whole allowance**. Induced drag is set by the planform and is
untouched by anything done to the boundary layer. Inverting for the aspect ratio that would leave room
gives **11.8, against the X-21's 6.99**.

**So laminar flow control does not merely clean a wing. It moves the optimum planform.** Once friction is
removed, induced drag dominates, and the aircraft that collects the benefit wants a much longer, thinner
wing than a converted bomber has. That is a second and stronger reason the testbed could not demonstrate
the case, because unlike the wetted-area argument it does not depend on how much of the aeroplane is
laminarised.

---

## Three Sections That Carried No Algebra Now Do

**Surface tolerance.** A three-dimensional roughness element trips a laminar boundary layer at a
roughness Reynolds number near 600, which gives an admissible height of **0.0123 inches** one foot behind
the leading edge, scaling as the fourth root of distance. It is therefore tighter further forward, which
is exactly where the wing splices and the fairing putty were. For scale, the slots are 0.0035 inches wide.

**The suction surface.** With slots 0.0035 inches wide on a 0.75 inch pitch the open-area ratio is
0.00467, so **the surface is 99.5 percent solid** and the air enters the slots at 31 feet per second
against 200 miles per hour in the ducts below. That is a useful corrective to the sieve impression the
literature's slot-count error creates.

**Atmospheric particles, which is the one that pays.** A turbulent wedge from a single leading-edge
disturbance covers 31.5 square feet on a 13.4 foot chord, so about forty blanket the wing. Cirrus at ten
thousand crystals per cubic metre delivers 294,000 encounters per second into a boundary layer 0.18
inches thick. **The wing is blanketed in 140 microseconds and clears in the 18 millisecond convection
time.** Both halves of the reported behaviour follow, with five orders of magnitude to spare, and the
difference from an insect is that nothing is left on the surface.

---

## An Independent Check on the Weakest Assumption

The suction coefficient is the least well constrained input in the article. The duct sizing checks it
from outside the model. The computed mass flow and the contemporary report of 200 mile per hour duct
speeds give 185 square inches of total duct area, about seven inches square in each of four ducts, which
fits inside a 13.4 foot chord without difficulty. **Had the assumed coefficient been an order of
magnitude wrong, the duct would not have fitted in the wing.**

---

## Verification

- **142 independent re-derivations across two verifiers, zero disagreements.** The verifiers use a
  tabulated atmosphere where the model uses a formula, bisection where the model uses closed forms, and
  numerical integration where the model uses a triangle area
- **A forward substitution confirms the inverted aspect ratio**, putting 11.8 back into the polar and
  recovering a lift-to-drag ratio of 30.0. Inverting a polar that already contains three assumptions is
  worth checking in the other direction
- **The wedge-area integration caught a factor-of-two defect in the VERIFIER, not the article.** I
  integrated the half-width where the wedge spreads at a half-angle on each side. The article was right
- All 22 articles pass `check_any.py`, `_verify.py` at the 0-error 21-warning baseline, and the
  22-article isolated build succeeds with **45 of 45 equations rendering as display math**

---

## Two Draft-Pass Defects Also Fixed

**The series chain listed the X-1 twice**, because the generator began the chain at the article the
sentence had already named.

**The OSTI archive contributed almost nothing usable and six wrong citations.** Of 49 records, one was
relevant. The rest were coal gasification, breeder reactors, magnetohydrodynamic generators, road-vehicle
aerodynamics and coastal oceanography, and one cited record was a **laminar flow cyclone**, which is a
coal-cleaning device. The Department of Energy corpus uses these words for other things. Forty-eight
records were dropped and the source is now effectively excluded for this subject.

---

## State

**A318 has had two of four passes.** The reference-density review and the publication review are yours to
prompt.

At 949 lines and 45 equations it is still short of the series bands and long on references at 531. The
reference pass has less to do here than usual and the publication review will carry the contemporary
survey.

Nothing in the series is published. The publication-order dependency is twenty-two deep.

**Still open and unchanged.** The fourth genre class, now seven consecutive articles outside all four
named classes. The A305 length offer.
