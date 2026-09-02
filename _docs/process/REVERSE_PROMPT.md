## Last Updated

**Date**: 2026-09-02
**Task**: **A345 draft pass, the first of four.** Committed and **not pushed**, per the rhythm.
**Not published**, and publication of the series still not authorised.

---

## The Keystone Is the Instrument Rather Than the Vehicle, Which Is a First Here

**The X-48B is an 8.5 percent dynamically scaled free-flight model, and a model cannot match every
dimensionless group at once.** Holding the Froude number and the relative density fixed makes the
model MOVE like the aeroplane. It sends the Reynolds number as $n^{3/2}$, which at this scale is a
factor of **40.35**.

**The geometry closes exactly rather than approximately.** NASA publishes the span as 20.4 ft and the
reference as 240 ft, and separately publishes 8.5 percent. The ratio is 0.085000 to fourteen decimal
places, so the reference vehicle is a real design rather than a round number attached afterwards.

**Time compression is 3.430 and it is a statement about the pilot.** A motion the full-scale aeroplane
would develop over three seconds develops in 0.875 seconds, and the ground pilot's reaction time is
not multiplied by 0.2915 to match.

---

## The Central Finding Is a Contradiction Already Sitting in the Record

**Liebeck's design paper states that separation begins in the kink region, that the outer wing stays
attached and provides lateral control into the stall, and that this is the ideal place for the stall
to begin because the ailerons remain effective.**

**The flight report records uncommanded wing roll-offs at a limiting angle of attack, and that
countering with lateral stick slightly delayed the roll-off and then produced a more abrupt wing
drop.**

**Those two statements are not compatible, and the scaling analysis says the disagreement is exactly
the one a factor of 40 in Reynolds number permits.** Separation onset and its spanwise progression are
Reynolds-governed. The character of the departure as a motion, and whether a pitch-over recovery
works, are Froude-governed.

**The programme's own objective list asks for both**, naming full-scale low-speed characteristics AND
departure onset boundaries as things dynamic scaling would deliver. **The first transfers and the
second does not**, and the article says so and prices it.

---

## The Demonstration Is Tilted and the Direction Is Computed

**Froude scaling makes thrust to weight invariant, so it is directly checkable.** The model carries
**0.3086** against the full-scale **0.2245**, an excess of **1.374**.

**That makes the engine-out test conservative rather than optimistic**, since an engine-out yaw moment
is a thrust asymmetry and the model produces a proportionally larger one. **This is the opposite tilt
from A332**, whose famous sortie was flown in the easiest available ordering.

**The model's own weight describes the vehicle it represents.** Inverting the cube on 525 lb gives
854,875 lb, which is **1.160 times a passenger blended wing body of the same span**. That is
consistent with the stated military freighter interest, and it is recoverable from nothing but the
scale relations.

**Cancelling the 35 ft X-48A cost a factor of 2.247 in Reynolds number** and made the aeroplane 31
percent quicker in its own time. That is the price of the 2002 decision in the only units it has.

**A345 scores A333.** The X-36 at 28 percent was 1.815 times slower in time and 5.979 times closer in
Reynolds than this aeroplane.

---

## A Hyphen Defeated the Gate, and It Is the Second Instrument in This Series It Has Defeated

**A344 fixed AUDIT patterns with `survey.loose` and the rule was never applied to GATES.** A345's gate
then refused **57 records on a separator alone**, among them `Correction of wind-tunnel pressure
coefficients for Reynolds number effect` and `Investigation of a Jet-Noise-Shielding Methodology`,
which are this article's keystone subject and the subject of its second aeroplane.

**The fix went into `_lib/gate.py`**, because a per-article gate fix fixes nothing for anybody else.
Only a hyphen between two LETTERS is flattened and the unflattened title is tested first, so **`X-48B`
survives because the character after its hyphen is a digit**, which matters in a series covering X-1
through X-76.

**The same separator was defeating cluster assignment, a third instrument.** Fixing it moved 195
records out of the residual, and the blended wing body cluster grew **429 to 593**, because the
literature hyphenates the configuration's name far more often than not. **A record in the wrong
cluster is worse than one in no cluster**, since it makes a subject look thin while the evidence sits
under a heading that does not claim it.

**Three passes are reported because a correction changes the instrument.** 6,395 kept, then 6,456,
then 6,428. **The third is smaller because the fix exposed an anchor of my own**, bare `frequency
sweep` being a flight-test excitation and also a mass spectrometer, an ultrasonic inspection and a
magnetospheric chorus emission. **Six homonym families were added by reading the audit**, the most
instructive being a dynamically scaled model that is a marine **foraminifer**.

---

## State

**A345 is committed and NOT pushed. One of four passes complete.** **12,786 lines, 7 display
equations, 6,183 reference definitions, 69,753 words**, of which 6,198 are author prose. Editorial
date 2025-11-23, series index 49, **full-aircraft class**.

`_verify.py` zero errors, `lint.py` **zero defects and zero conventions**, reference integrity **6,183
used, 6,183 defined, zero undefined, zero orphaned, zero duplicate URLs**, every stated value
re-derived by a verifier that does not import the computation and parses the article for what it
claims, **all 17 survey rows agreeing across three independent counts** of stated, cited and
data-derived, the cluster table summing to 6,114, **48 back-references with zero forward references**
and every target present on disk, and zero contractions, colons, semicolons, dashes or caps-emphasis
spans in authored prose. **`_lib` tests are 95 of 95.**

**No production build was run**, which the draft pass does not require. The stub-isolated build and
the rendered audit belong to the publication review.

**Forty-nine of seventy-two drafted, none published, publication never authorised.**

---

## Next

**A345's equation-density review**, the second of four passes. The article carries **7 display
equations**, which is low for this series and expected, since the draft pass spent its argument on
scaling relations that are stated once. **The equation pass should look hardest at the Reynolds
transfer**, which is currently an argument in words about which quantities are governed by which
group, and at the yaw-authority claim for the X-48C, which is presently geometric and directional
rather than computed.
