# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-11
**Task**: A333, the McDonnell Douglas X-36, drafted as
`_drafts/x_planes_mcdonnell_douglas_x36.markdown`, editorial date 2025-11-11, series index 37 of 72.
**Committed, not pushed.** **Not published.**

**11,068 lines, 13 display equations, 3,467 reference definitions, 59,364 words**, with all 3,352
master records cited and none left over. All thirty-seven articles remain in `_drafts/`.

---

## The Keystone Is the Scale Factor, Not the Missing Tail

Every account of this aeroplane leads with the absent vertical tail. **The interesting number is the
28 percent**, because a free-flight model cannot match Froude, Reynolds and Mach at once in the same
air, and which one it matches decides what the experiment can measure.

**The similarity table settles the design of the experiment in three rows.**

| Matched | Velocity ratio | Froude ratio | Mach ratio | Reynolds ratio |
|---|---|---|---|---|
| **Froude** | **0.5292** | **1.000** | 0.5292 | 0.1482 |
| Mach | 1.000 | 3.571 | 1.000 | 0.2800 |
| Reynolds | 3.571 | **45.55** | 3.571 | 1.000 |

**Matching Reynolds would put the Froude number out by 45.55**, so the model would not fall the way an
aeroplane falls. That row exists only to be dismissed. Matching Mach is a wind tunnel's choice and is
useless for motion. **Froude is the only option and everything else follows from it.**

---

## The Finding I Did Not Expect

**Froude matching makes the model faithful and simultaneously makes it harder to fly.** Time runs at
0.5292 of full scale, so every motion happens **1.8898 times faster in real seconds**.

**A delay in a video and command link does not compress to match.** Neither does a human reaction time.
So both are amplified by 1.8898 when measured against the dynamics they are trying to control. A
hundred milliseconds of link delay is worth 189 at full scale, and a 250 millisecond human reaction
time is worth **472.5**.

**The demonstration was therefore harder than the thing it demonstrated**, by an exact factor, which
makes the result stronger rather than weaker.

**This is the precise inverse of the previous article.** A332 found the X-35's most famous sortie flown
in the easiest available ordering at a weight the production aircraft would never see. **A333 finds one
flown against a handicap the full-scale aircraft would never carry.** Two consecutive demonstrators,
opposite directions, both differences arithmetic rather than opinion. **The pair belongs in the closing
article.**

**The article states the claim in its weaker and honest form**, because no latency figure for this link
has ever been published. The multiplier is exact; what it multiplies is unknown, and the article says
so rather than inventing a number.

---

## The Check That Cost Nothing and Could Have Failed Loudly

**If the aircraft is genuinely a Froude-scaled model then its weight fixes the aeroplane it stands
for.** Inverting the cube law gives a full-scale weight of **57,853 pounds**, a length of 19.82 metres
and a span of 11.34 metres.

**Sixty-five feet, thirty-seven feet of span and fifty-eight thousand pounds is a real class of
aeroplane**, and exactly the class a tailless agility demonstrator of the middle 1990s would stand in
for. The article is careful that this is a check rather than a proof, since the designers chose the
weight, **but it is a check that would have failed loudly had the aircraft not been dynamically scaled
at all.**

---

## The Independent Verifier Caught a Real Distinction

The verifier and the calculation disagreed on the divergence doubling time by a factor of **1.900**,
which the handoff says is a hint that something is wrong. **Neither was wrong. They answered different
questions.**

The flight dynamics convention measures the growing eigen-solution and gives $\ln 2 / \sigma$. **A
disturbance actually released from rest follows a hyperbolic cosine rather than an exponential**,
because it starts with no yaw rate, and needs $\operatorname{arccosh} 2 / \sigma$. The ratio is
arccosh 2 over ln 2, it is **1.900 exactly, and it depends on nothing**.

**Both are now in the article**, verified as a randomised property across growth rates and measured by
integrating the equation of motion under each initial condition separately. **The distinction is more
instructive than either number alone**, and it would have been silently wrong had the verifier used the
same route as the calculation.

---

## The Cleanest Physical Result

**A fin and a vectored nozzle are complementary rather than alternative, and the reason is which terms
carry dynamic pressure.** A fin's yawing moment and the destabilising fuselage moment both go as $q$,
so their ratio never improves with speed. **A nozzle carries no $q$ at all.**

Inverting for the speed at which the nozzle alone can no longer hold ten degrees of sideslip gives
**342.2 knots**, which is above anything the aircraft ever flew. **So the split ailerons were margin
rather than necessity**, and the general lesson is that a tailless aircraft needs an effector whose
authority does not vanish at the low speed and high angle of attack it most fears, where a fin would
have stalled even if it were there.

---

## The Reynolds Penalty, Quantified Rather Than Feared

The factor is 6.749, which sounds fatal until both numbers are on the page. **The model runs at 8.81
million on the mean chord and the full-scale aircraft would run at 59.46 million.** Both are deep in
the fully turbulent regime, so the penalty does not move the model into a different flow regime for
attached flow.

**It still matters where it matters most**, because separation onset and vortex burst are Reynolds
sensitive well past transition, and those are exactly what a high angle of attack experiment studies.
The article says neither that the penalty is fatal nor that it is negligible, but that it is confined
to a list of questions it names.

---

## The Vehicle Cluster Is Thin for a Fourth Distinct Reason

**Six records carry this aircraft's designation.** The three preceding articles found the same shape
and every reason was different. **The X-33 and X-34 were cancelled** and stopped generating literature.
**The X-35 won and never had a trace at all**, because contractor demonstrators flown for a source
selection do not produce reports. **The X-36 was neither**: it ran to completion, met its objectives,
and produced a technique rather than a vehicle, so its contribution is filed under the names of its
methods.

**Four vehicles, four different reasons for one shape**, and that belongs in the closing article.

---

## Verification

- `python3 tmp/a333/verify.py` **59 of 59**, by an independent verifier that does not import the
  calculation, using randomised property tests over twenty thousand scale factors, bisection,
  integration of the yaw equation under two initial conditions, and recomputation of the atmosphere
  from Sutherland's law.
- `python3 _verify.py` **0 errors, 21 warnings**, taken from the repository root.
- `python3 tmp/errata/check_any.py` **0 failures, 0 warnings**, twelve genre sections and three series
  sections in order.
- **Prose style clean.** Zero em dashes, en dashes, contractions, prose colons, curly quotes or
  capitals used for emphasis. **The only semicolon and parentheses are the debug tag.**
- **Reference scan clean across 6,884 visible entries**, zero punctuation defects, zero duplicate,
  undefined or orphaned definitions.
- **Isolated 37-article build exit 0**, page 828 KB, **13 open and 13 close display-math delimiters**,
  zero unexpanded markers, zero nested empty lists, zero blockquotes.

---

## What I Did Not Do

**I did not push.** The draft pass commits only. **Publication has never been authorised** and the
`post_url` interlock is now **thirty-seven deep**.

**The equation count is 13, the lowest in the series so far, and I am reporting it rather than padding
it.** The subject has one relation applied repeatedly rather than several chains. **The
equation-density review is the pass that exists to decide whether more are warranted**, and my own
candidates are the sideslip response, the control-law bandwidth the divergence demands, the drag-rudder
yawing moment, the induced drag of differential drag, and the ground-roll and approach performance that
the published speeds allow.

---

## Next

**A333 pass two**, the equation-density review, on your prompt.
