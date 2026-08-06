# Reverse Prompt

> **Navigation**: [Process](./README.md) | [Documentation Root](../README.md)

This file is the AI-to-human communication channel. It is overwritten after each completed task.

---

## Last Updated

**Date**: 2026-08-05
**Task**: A303 equation-density review. Committed and **not pushed**. **No article in this series is
published.**

**37 to 92 display equations, 995 to 1235 lines.** Equations and references are inside band.

---

## The Pass Replaced an Assumption With a Derivation, and the Numbers Got Worse

The draft assumed a ten-million-fold attenuation because that is a plausible round number. Deriving
it instead changes the article.

Working forward from the fission rate gives a gamma source of $2.5 \times 10^{19}$ photons per second,
and at ten metres unshielded that is **9.8 grays per second, when about five grays is a lethal
whole-body dose**. One second of exposure at ten metres from an unshielded hundred megawatt core kills
the crew. Holding them to fifty millisieverts across a hundred-hour flight then demands an attenuation
of $7.1 \times 10^{7}$, which is **25.7 centimetres of lead rather than 23.2**, and a gamma shield of
**41 tonnes rather than 37**. That is 22 percent of gross weight and **106 percent of the B-36 maximum
bomb load**, where the draft said 95 percent.

The draft also treated only gammas. Neutrons need a hydrogenous layer attenuated by a removal
cross-section rather than a photon coefficient, and lithium hydride requires **2.2 metres and 24.5
tonnes**. Stated as an upper bound rather than an addition, because a layered design attenuates both
radiations in both materials and beats the sum, so the true figure lies between 41 and 66 tonnes.

Either way the conclusion sharpens rather than softens. **The shield weighs at least the payload.**

---

## A Validation the Draft Did Not Have

This is the addition I would least want lost, because it is the only place in the article where the
derivation can be checked against hardware.

Apply the same chain to the one megawatt ASTR in the NB-36H at fifteen metres rather than to a
propulsion reactor. Scaling the source and the distance gives 157 grays per hour unshielded, and
holding the crew to fifty millisieverts across the 89 hours the reactor actually ran demands 18.7
centimetres of lead, which for a six square metre bulkhead is **12.7 tonnes**. Repeating with the far
more permissive occupational allowance of the 1950s gives 16.4 centimetres and **11.2 tonnes**.

**The reported crew shield was eleven to twelve tonnes.** The two estimates bracket it.

The method used throughout this article reproduces the one aircraft in it that actually flew, which
is the closest thing to validation available for a programme that never built its aeroplane, and it
is why the propulsion-reactor figures are worth taking seriously rather than treating as arithmetic
exercises.

---

## What Else Went In

The compact-core argument now has its criticality relation, so the article can say why every aircraft
reactor in the programme used highly enriched fuel rather than merely noting that it did. The
air-scattered term now carries the exponential atmosphere, giving a factor of four reduction between
sea level and twelve kilometres, which is why the shield cannot be sized without first choosing the
cruise altitude.

The direct cycle gained the Dittus-Boelter film relation that sets how much hotter a fuel element must
run than the air it heats, a core power density of a hundred megawatts per cubic metre, and the core
pressure drop as a thrust penalty, since a reactor is a heat exchanger where a combustor is an open
volume. The decay heat section gained the adiabatic heat-up, giving **23 minutes from a cooling
failure to a melted core an hour after the aircraft has landed**.

The molten salt argument is now quantitative. Vessel mass scales with pressure through the thin-shell
relation, and a fluoride salt at 1000 kelvin against a pressurized water reactor at 600 is a pressure
ratio of $1.5 \times 10^{4}$, so **the vessel is four orders of magnitude lighter**. That is why the
concept survived in a place it was not invented for.

The cancellation now has a relation beside it. Refuelled range is a sum over segments with no bound
the aircraft imposes, so **unlimited range was achieved by a logistics arrangement at zero cost in
payload**. The nuclear aircraft was competing against a solution that had already won on its own
metric.

---

## Verification

**All 34 worked values re-derived independently, none disagreeing beyond 3.5 percent.**

287 references with zero undefined and zero orphaned. `_verify.py` at the 0-error 21-warning corpus
baseline. Zero style violations, zero doubled words, zero consecutive-display runs. Isolated build
succeeding with 92 rendered display blocks matching 92 source equations and Part 7 navigation.

One seam defect was found and repaired, a neutron source equation with prose glued to the same line.
The unbalanced-delimiter check caught it, which is the check that exists because of A297.

---

## What Remains

**Lines at 1235 are 65 short of the 1300 floor and have not been padded.** Contemporary references are
already 32.8 percent of dated, inside the target range, so A303 does not have A302's deficit going
into the later passes.

**Publication order dependency is seven deep.** Two commits unpushed. Categories remain
`aerospace history engineering`, seven articles deep.
