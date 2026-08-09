---
layout: post
mathjax: false
comments: true
title: "Draft Summary"
date: 2000-01-01 00:00:00 +0000
categories: meta
---

<!-- Axxx -->

This post reviews the status of draft posts in this blog's `_drafts/` directory.
Each draft is assessed for topic, completion status, remaining work, and publication sensibility.
Assessments assume that contemporary tooling will be used if salvaged
and that appropriate ecosystem standard choices will replace any tooling that has fallen out of favor.
Missing sections and prose will need to be drafted.
Stubs and largely incomplete drafts are assessed for topicality and publication merit.


## X-Planes Curtiss-Wright X-19 A316 2025-10-25

`x_planes_curtiss_wright_x19.markdown`, A316, editorial date 2025-10-25, series `x_planes` index 20 of
72.

514 lines, 33 display equations, 79 references, 6,601 words after the draft pass; 688 lines, 78 display
equations, 79 references, 7,239 words after the equation review; 937 lines, 78 display equations, 274
references, 9,408 words after the primary-reference review; **1,200 lines, 78 display equations, 431
references, 11,792 words after the publication review.** All four passes complete. Committed and pushed.
Not published.

**A section was missing from the article entirely.** The genre carries three extras beyond the standard
twelve and this article was drafted with only two, `## The Contemporary Literature` being absent from the
draft pass onward while every automated check passed it, because sections were counted rather than
identified. `check.py` now names the three required extras. Three acronyms were also used before
expansion, which is the A298 defect recurring.

**The survey's organising claim is the opposite of A315's.** That article closed on a keystone dissolved
by distributed electric propulsion. The X-19's keystone was never wrong and never went away. What changed
is the failure mode, and it was abolished rather than improved, because electric propulsion removes the
requirement for an interconnected transmission instead of making gearboxes better. Contemporary coverage
is 157 of 399 research citations, or 39.3 percent.

**The coverage audit found BOTH kinds of gap at once, which has not happened before in this series.** Five
topics were genuinely thin because the draft harvest was never aimed at them, and all five carry relations
the equation pass added, which is the A315 inter-pass dependency arriving on schedule. The rest were deep
and barely used, which no search would have fixed. Research citations are 242, all primary or period, with
zero contemporary left deliberately for the publication review.

**The pass met a false-positive family the series has not seen before.** A propeller in oblique inflow is
a live subject in naval architecture, using this article's exact vocabulary. The first selection returned
eight candidates for the keystone topic and all eight were marine. Filtering on journal name removed them;
two more got through and were caught by reading, being David Taylor Model Basin spindle-torque work and
the open-water characteristics of a propeller for LSD-41, a dock landing ship. **A315 cites both of those
plus two more and has not been corrected**, pending the pilot's decision.

**The first version of the venue filter was worse than the problem it fixed**, rejecting the entire AIAA
Guidance, Navigation and Control series over the token `navigation` and discarding, among others, an
energy-optimal speed profile for a tandem tilt-wing aircraft. Fifteen records were recovered by narrowing
it. Reading the rejected list is what exposed it.

**The equation review caught two errors in the drafted text, which is the twelfth consecutive article in
which writing the relation down has done so.** The pitch-moment relation was displayed as a form
evaluating to twice the value quoted in the prose beside it, so the article contradicted itself while
passing every automated check; the quoted value was right and the algebra had a spurious factor of two.
The yaw inertia was transcribed as 100,565 against a computed 100,690, leaving the acceleration built on
it correct and the stated inertia wrong. **The review also introduced a defect of its own**, an
unterminated display block that would have rendered as broken mathematics and was invisible to every
existing check, since it is not a lone delimiter and the display-equation regex simply fails to match it.
`check.py` now fails on any line opening with a display delimiter that does not close with one.

**The keystone deliberately does not transfer from A315, and the handoff was right to warn against
assuming it would.** A tilt-wing must keep its wing flying at enormous angles of attack, so slipstream
immersion governs it. A tilt-propeller never rotates its wing, so immersion is irrelevant. The X-19's
distinguishing feature is instead a wing loading of 88.4 pounds per square foot in an aircraft required
to land vertically, against a wing that stalls at 136.5 knots.

**The keystone is the propeller normal force**, the force a disc develops normal to its own axis in
oblique flow, which Curtiss-Wright called the radial lift force and sized the wing around. Its primary
literature is Ribner on propellers in yaw, from 1943 to 1945, which is aerodynamic stability work
eighteen years older than the aircraft and would not have appeared in an imported A315 pool.

**Strongest result.** The 400-knot cruise caps tip speed at 644.2 feet per second, and hovering at that
tip speed forces a blade chord of 17.2 inches on a 13-foot propeller without invoking radial lift at all.
The famously wide blade is demanded twice over. Feeding that chord through Ribner's fin analogy fixes the
one free parameter at 0.283 from geometry rather than assumption.

**A result that cuts against the article's own thesis, reported rather than buried.** The propellers
supply 29.8 percent of the cruise lift slope and the equivalent plain wing is 225 square feet at 61
pounds per square foot, computed two independent ways agreeing to 3.5 percent. **But the conversion
corridor is continuous with the radial lift force switched off.** It made the wing smaller rather than
making the aircraft possible.

**Central historical claim.** The X-18's fatal deficiency was uninterconnected engines. The X-19 had the
interconnect, which was necessary because losing one side is 1.67 times full roll control, and the
interconnect is the gearbox that destroyed it. The cure and the cause of death were the same component.

**Two defects found by reading rather than by any check.** The first corridor formulation was circular
and returned 0.6 knots at every nacelle angle below 60 degrees. The isolated build script arrived one
stub short at eighteen predecessors, so the `post_url` to A315 had no target and the entire build failed,
which is the interlock working as designed.

**What the article cannot do.** Fifty flights, four hours, and no transition ever attempted, so there is
no flight data from the regime the aircraft was built for. Comparison With Ground Prediction reports the
absence. The article also names where its own model stops deserving belief, at about 60 degrees of disc
incidence, and reports that five of ten corridor rows sit outside it.

107 independent re-derivations with zero disagreements. Three passes remain.

## X-Planes Hiller X-18 A315 2025-10-24

`x_planes_hiller_x18.markdown`, A315, editorial date 2025-10-24, series `x_planes` index 19 of 72.

386 lines, 21 display equations, 66 references, 3,982 words after the draft pass; **485 lines, 29
display equations, 66 references, 5,240 words after the equation review; **697 lines, 29 display
equations, 248 references, 6,511 words after the primary-reference review; **935 lines, 29 display
equations, 418 references, 8,437 words after the publication review.** All four passes complete.
Committed and pushed. Not published.

**The first article in the series to solve vertical take-off with a wing rather than a jet.** The X-13
and X-14 both pointed a jet downward. A tilt-wing points the wing itself, which is a different problem
with a different failure mode.

**The keystone is slipstream immersion.** A tilted wing points away from the oncoming air, so the
configuration works only where the propeller slipstream keeps the flow attached. Two sixteen-foot
propellers on a 47.92-foot span immerse about 57 percent at a representative contraction, so **about 43
percent of the span is never immersed**, and at a 15-degree stall angle the outer panel is stalled for
**83.3 percent of the conversion**. That is geometric rather than aerodynamic.

**What the slipstream buys is large.** The part-developed slipstream dynamic pressure corresponds to an
equivalent airspeed of **117 knots while the aircraft is stationary**. The immersed wing never stops
flying and the un-immersed wing never starts.

**The engine-out claim was checked and is arithmetic rather than caution.** With the turboprops not
cross-linked, losing one gives a 268 kN m rolling moment while the ailerons supply under one percent of
it in hover. Cross-shafting is the only fix. And **a few percent of thrust asymmetry exhausts the roll
control during conversion**, so the propeller pitch control failure that ended the programme produced a
departure as the expected outcome. Converting at ten thousand feet cost about 26 percent of the
available roll authority.

**A strong internal validation.** Momentum theory gives 7,883 ideal shaft horsepower against an
installed 11,700, implying a figure of merit of 0.674, which is an ordinary propeller value and is the
best available check that the published figures describe one consistent aircraft.

**The equation pass corrected the draft's framing.** The draft asserted the mechanism and never wrote
it down. The relation is the local angle of attack, alpha_local = atan[V sin(i_w) / (V cos(i_w) + v_s)],
and **at zero forward speed it is exactly zero at any tilt**, so the immersed wing is at precisely zero
incidence in hover rather than merely unstalled.

**More importantly, a conversion corridor exists at every speed**, with a margin from 38.1 degrees of
tilt at ten metres per second to a narrowest 12.6 at fifty. The draft's emphasis on what is stalled left
the impression the configuration was marginal. It is not, and the draft's closing claim that the
configuration was sound while the aeroplane was under-equipped is now established rather than asserted.

**Descent is what closes the corridor**, and it was promoted out of Out of Scope. The descent rate that
consumes the whole margin is **284 feet per minute at the slow end**, which is gentle by any normal
standard and explains the restricted descent envelopes tilt-wings carried.

**One finding runs the other way.** Momentum theory with forward speed shows the induced velocity falls
while the freestream rises faster, so slipstream dynamic pressure over the immersed panel climbs from
2,210 to 5,772 pascals through the conversion. The handover is helped by the physics rather than fought
by it.

**The primary-reference pass found a selection problem rather than a supply problem**, which is the
opposite of A314. The harvest had returned every era in quantity and the draft had used almost only
pre-1960 material. Of 218 research references, 184 or 84.4 percent are primary, with era coverage of 54,
53, 39, 38 and 34.

**One topic needed a second harvest, and it exposes a dependency between passes.** Descent stood at three
records because the draft treated it as an aside in Out of Scope, and the equation pass then made it the
quantity that closes the corridor. An equation pass can promote a subject from an aside to a load-bearing
claim, and the reference base has to follow it. That search found the most apposite document in the
article, a measurement of the descent capability of two-propeller tilt-wing configurations.

**Unlike A313 and A314 the configuration has a real primary literature** even though the individual
airframe does not, which is the inverse of those two situations and a milder difficulty.

## X-Planes Lockheed X-17 A314 2025-10-23

`x_planes_lockheed_x17.markdown`, A314, editorial date 2025-10-23, series `x_planes` index 18 of 72.

461 lines, 27 display equations, 71 references, 5,266 words after the draft pass; **607 lines, 47
display equations, 71 references, 6,937 words after the equation review; **835 lines, 47 display
equations, 277 references, 8,301 words after the primary-reference review; **1,066 lines, 47 display
equations, 446 references, 10,417 words after the publication review.** All four passes complete.
Committed and pushed. Not published.

**The second consecutive article whose subject has no archival record of its own.** NTRS returns
astronomy false positives for the vehicle name and nothing technical, and DTIC holds the surrounding
re-entry literature and nothing on this vehicle. Every dimension and performance figure comes from
secondary compilations, and those disagree on the length and, by a factor of two and a half, on the
apogee.

**The keystone is partial simulation.** A re-entry is several simultaneous conditions. Matching
velocity, which sets the chemistry through stagnation enthalpy, matching heating rate, and matching the
degree of chemical nonequilibrium are three requirements, while altitude and model scale are two knobs.
**Two knobs cannot satisfy three conditions**, so the article is an account of which requirement the
X-17 surrendered.

**Firing the stages downward multiplies the heating rate by 13.63** over what free fall from the same
apogee would give, and that conclusion survives every published apogee figure, so the strange
architecture is the experiment rather than an enhancement of it.

**The trade that works and the one that does not.** Density enters the heating correlation under a
square root and velocity cubed, so at 57 percent of intercontinental velocity the vehicle needs 27.74
times the density, which puts it at 13.97 km and reproduces the heating rate exactly. But stagnation
enthalpy contains no density at all, so the X-17 reached **33.0 percent of the energy per unit mass**
and therefore none of the chemistry. The binary scaling parameter is overshot 9.25 times and the total
heat load is short by about 4.17 times.

**The framing is that the programme surrendered the gas physics because nobody could compute it and
kept the heat flux because everybody needed to design against it**, which was correct for 1956 and
would be wrong today.

**The equation pass found a ballistic-coefficient ceiling on the whole technique.** Deriving the
reference condition from the Allen-Eggers solution instead of assuming it shows the draft's assumed
value corresponds to a ballistic coefficient of 1,453 kg/m2, and that above about 2,500 at a practical
altitude floor **no altitude exists at which the X-17 matches the heating rate at all**. The
heating-rate match is therefore conditional on the class of body being simulated. It works for exactly
the blunt first-generation re-entry vehicle the X-17 was built to test and would have failed for a
dense slender one.

**The primary-reference pass found a supply problem rather than a selection problem.** The pool held
only twenty records from before 1960 for a vehicle that flew in 1956, because the first harvest's period
sweep used a 1985 cutoff that let later material crowd out the contemporaneous literature. A second
sweep with a 1960 cutoff took pre-1960 supply from 20 to 157. Of 252 research references, 214 or 84.9
percent are primary and period material.

**Sixteen candidates were rejected after being read rather than matched**, including furnace fillers and
silicon carbide power converters for refractory, a pneumatic air motor for high temperature air, and
microchannel heat sinks for heat flux. A second automated scan flagged seven more that all proved to be
false positives of its own keyword list, which is worth recording as an asymmetry.

**It also showed the vehicle reproduces a point and not a trajectory**, since peak deceleration and the
velocity at peak heating are both independent of ballistic coefficient while the altitude at which they
occur is not, and **that ablation is mandatory rather than convenient**, since a passive surface would
need 4,127 K to reject the matched flux, above tungsten's melting point and graphite's sublimation
point. Radiative heating was added as a fourth thing the vehicle could not reproduce, at one part in
110.7.

## X-Planes Bell X-16 A313 2025-10-22

`x_planes_bell_x16.markdown`, A313, editorial date 2025-10-22, series `x_planes` index 17 of 72.

534 lines, 20 display equations, 85 references, 7,450 words after the draft pass; 758 lines, 72 display
equations, 85 references, 8,731 words after the equation review; **1,016 lines, 72 display equations,
315 references, 10,940 words after the primary-reference review; **1,233 lines, 72 display equations,
468 references, 13,316 words after the publication review.** All four passes complete. Committed and
pushed. Not published.

**This is the first article in the series whose subject has no technical record at all.** NTRS returns
zero records for MX-2147, zero for the aircraft as an aeroplane, and zero for the Bell model number,
and ten false positives for the aircraft name consisting of Bell Laboratories radio surveys and a
galaxy catalogued as MCG-05-23-16. DTIC holds the reconnaissance requirement and several sibling
weapon-system studies but nothing on this aircraft. **Every dimension, weight, and performance figure
in the article comes from a secondary compilation, and the compilations disagree with one another.**

**The article is carried by the A310 rule** that a vehicle with almost no record of its own can still
be dense provided the question it asked was one other people were also asking. The X-16's question is
subsonic cruise at extreme altitude, which is the U-2's question, the RB-57D's question, and the
question the modern high-altitude long-endurance field is asking now.

**The X designation was security cover rather than a research classification**, which makes this the
first entry in the register where the number describes the secrecy rather than the aircraft.

**The keystone is the thrust ceiling and it was chosen against the famous answer.** Minimum drag is
weight over the maximum lift to drag ratio and contains no density at all, so it does not vary with
altitude, while turbojet thrust lapses as the air thins. The ceiling is where they meet, which makes
it a function of instantaneous weight rather than a property of the aeroplane. The coffin corner sits
about fourteen thousand feet above that limit at every weight and never binds.

**The method then failed its own validation, and the failure is the article's best result.** At a
linear thrust lapse the quoted 71,832 foot ceiling requires a weight 955 pounds below the empty
weight, and the same failure lands on the U-2A and the RB-57D in the same direction. Solving for the
lapse exponent instead of assuming it gives 0.9686, 0.9780, and 0.8669 for the three aircraft, with
the two whose wing areas are published agreeing to within one percent. That is a statement about
compressors in thin air rather than about wings, and it corroborates the historical claim that the
programme's lasting contribution was the high-altitude J57 that then powered the U-2.

**The equation pass corrected the article's physics rather than only adding relations.** The draft
attributed the sub-unity thrust lapse exponent to compressor Reynolds number degradation. Degradation
makes a compressor worse in thin air and therefore pushes the exponent above one, so it cannot be the
cause. The mechanism is ram recovery, since sea level static thrust is quoted at Mach zero while the
aeroplane cruises at Mach 0.685. Ram alone predicts 0.8889 against the observed 0.9378, so it
over-explains, and component losses consume 44 percent of the benefit, which is where Reynolds
degradation actually belongs. **The two mechanisms act in opposite directions.**

**A second result reconciles the thrust-limited finding with the U-2's reputation.** In true airspeed
the usable band at the design altitude is 118.1 knots, which is not a corner. In equivalent airspeed,
which is what the pilot's instrument reads, it is 28.8 knots, and 23.1 at the quoted service ceiling.
The instrument band closes 2.15 times faster than the physical one, so the corner does not set the
ceiling and does entirely set the difficulty of flying the cruise.

**The primary-reference pass corrected the article's implicit history.** The draft cited 35 documents
from before 1960 and 22 from 2019 onward and three from the whole of 1960 to 2018, which implied the
X-16's question lapsed for sixty years and then revived. It did not. A second harvest aimed at that era
took the pool from 947 to about 1,400 records and era coverage now runs 69, 61, 56, 47, and 57 across
the five bands. Of 290 research references, 233 or 80.3 percent are primary and period material.

**Three off-topic citations were removed after being read rather than matched**, all having matched on
the word resolution, namely a paper on wireless sensor network localisation, one on unexploded ordnance
detection, and one on spectra of stars in globular clusters. Fifteen more were dropped before insertion.
The Source Base records this.

**The publication review expanded the contemporary survey from 57 references to 217 across twelve
fields**, and two of its findings bear on the article's own conclusions. **The keystone is dissolved
rather than solved by solar-electric propulsion**, since a photovoltaic platform has no compressor and
therefore no lapse exponent, so the term that dominated the X-16's design leaves the equation entirely
and is replaced by energy storage mass. And **the binding constraint on a modern equivalent is
certification rather than performance.**

**Sixteen citations were removed after insertion because they were read rather than merely matched**,
including a railgun bore that matched high aspect ratio, gun tube steel that matched fatigue under
spectrum loading, cable-stayed bridges that matched digital twin, and winter wheat topsoil that matched
airborne hyperspectral imaging. The Source Base records the pattern and the lesson.

**Class question for the pilot.** After all four passes the article sits above the
documentation-poor band of 150 to 400 lines, 0 to 15 equations, and 20 to 60 references on all three
measures. **References at 468 are at or above the full-aircraft band of 250 to 380**, while lines at
1,233 sit 67 below its 1,300 floor and equations at 72 sit 18 below the 90 floor. **A313 is the first
article in the series to finish outside the named classes on two of three measures.** Reported rather
than remedied by padding. Whether `RESEARCH_AIRCRAFT_STRUCTURE.md` should gain a fourth class is left
open. `RESEARCH_AIRCRAFT_STRUCTURE.md` does not currently name an intermediate class. Reported rather
than padded upward or trimmed downward.

## X-Planes North American X-15 A312 2025-10-21

`x_planes_north_american_x15.markdown`, A312, editorial date 2025-10-21, series `x_planes` index 16
of 72.

669 lines, 48 equations, 77 references, 8,057 words after the draft pass; 929 lines, 90 equations, 77
references, 10,729 words after the equation review; 1142 lines, 90 equations, 252 references, 12,993
words after the primary-reference review; **1368 lines, 99 equations, 350 references, 15,267 words after
the publication review.** All three densities inside band. **Nothing trimmed at any point in any pass.**

**The keystone was chosen rather than discovered, and the article says so.** Every previous article in
the series found its keystone by locating the one binding unknown. The X-15's record is large enough
that four candidate keystones are all well supported, so the article names all four, chooses one, and
defends the choice. The rejected candidates are aerodynamic heating, hypersonic stability and control,
flight outside the atmosphere, and structures at temperature. The objection to all four is that they
are consequences of a single quantity, and treating any one as primary makes the other three look like
separate subjects when they are the same subject.

**The keystone is energy disposal.** At its record speed the X-15's kinetic energy per kilogramme was
2.041 MJ, against roughly 0.904 MJ to melt a kilogramme of its own structure from room temperature.
**The aircraft carried 2.26 times the energy needed to melt itself**, and 7.4 times the energy needed
to take the whole structure to the 1,200 degree Fahrenheit limit of its strength. That makes
deceleration a thermal event rather than a nuisance, which is the difference in kind between
hypersonic flight and merely fast flight, and it dimensions the structure, the trajectory, the
propulsion, and the control system in one stroke.

**Central result.** Applying a Sutton and Graves stagnation-point correlation at the record condition
gives 64.8 W/cm2, while a structure at its design temperature radiating at an emissivity of 0.8 can
reject only 3.28 W/cm2. **The record flight asked the structure to reject 19.8 times what its design
temperature could handle**, which is why the X-15A-2 was covered in ablative coating, why that flight
was the fastest ever made, and why nothing like it was attempted again. The correlation is validated
against the reported 2,700 degree leading-edge temperature, which it overshoots by 12.7 percent, and
the conclusion survives doubling the assumed nose radius.

**Results the sources do not state.** The two records are one energy budget spent two ways, at 2.347
and 1.964 MJ/kg, differing by 19.5 percent because the speed flight was flown by the X-15A-2 with
external tanks rather than because it was flown better. **Converting the speed record's kinetic energy
entirely to height gives 239.3 km against an actual altitude record of 108.0**, so a little over half
the available energy never reached apogee. The speed record was 89.9 percent of the ideal rocket
delta-v, which is a remarkably small loss. **The heating rate falls with thinner air and the heat load
rises**, since the rate goes as sqrt(rho) V^3 while the time to shed a fixed energy goes as 1/rho, so
rate and load are optimised by different trajectories and the X-15A-2 moved from a rate-limited to a
load-limited regime when it was coated. A 1.5 mm Inconel skin reaches thermal equilibrium in about
7.5 seconds, which is what makes the hot structure rate-limited. **A 300 kelvin gradient alone yields
the structure**, at 830 MPa, which is why the skin is corrugated and slotted for no load reason.
**99.8 percent of the energy the vehicle holds at its fastest must be disposed of before landing.**

**The series thread arrives from the opposite direction.** The X-13 and X-14 lost aerodynamic control
authority because the vehicle was not moving; the X-15 loses it because there is no air. Same
relation, opposite cause, same reaction-control answer. The dynamic pressure ratio across a single
flight exceeds 4,600.

**An order-of-magnitude error was caught by verifying rather than by reading.** The aerodynamic to
reaction control crossover was written as 6,280 Pa and computes to 628, placing the handover near 55
km rather than between 30 and 50. **Eighth consecutive article in which computing before writing
caught a wrong claim.** The corrected value produced an unplanned result: Flight 91's burnout at 53.6
km sits within 1.4 km of the crossover, so on a high flight the engine stops at roughly the altitude
where the aerodynamic surfaces stop working.

**Two omissions found by surveying the references rather than by reading the draft**, namely the MH-96
adaptive flight control system, which was fitted to the airframe that was lost, and shock interference
heating, which is what nearly destroyed the speed-record flight and which the draft described without
citing. Both were added.

**Equation-density review complete, 2026-08-08. 929 lines, 90 display equations, 77 references,
10,729 body words.** Equations rose from 48 to 90 across 22 edits, landing exactly on the floor.
Nothing was trimmed.

**The pass answered the question the keystone posed and the draft left open.** The article states its
keystone as how much of the shed energy ends up inside the structure rather than in the air behind it,
and never answered it. Working through the Reynolds analogy, the heat entering the wall divided by the
friction work done at it collapses to c_p (T_aw - T_w) / V^2, in which **the velocity cancels from the
numerator entirely**, so the fraction depends only on how far the wall sits below the adiabatic wall
temperature measured against the vehicle's kinetic energy. At the record condition that is 43.0 percent
for a cold wall, 27.7 at the design limit, and 7.2 at the temperature Knight's leading edges reached.
**A hot wall absorbs a smaller fraction than a cold one, so running hot is part of the mechanism by
which a hot structure protects itself** rather than merely something it tolerates. That was not
anticipated by the framing.

**A wrong claim was caught by computing further within the same pass.** The energy fraction reaching
the structure was first written on an assumed friction fraction of 35 percent of drag, giving ten
percent to the structure and a heat load exceeding the structure's absorptive capacity at a ratio of
1.19. Estimating the friction drag directly, from a turbulent flat-plate coefficient at the record
Reynolds number of 3.2e7 over a plausible wetted area, gives 8 to 26 percent and about 15 centrally.
**The corrected figure is four percent to the structure and a ratio of 0.51, so the conclusion
inverts: the total heat load is comfortably within capacity and the binding constraint is the local
rate.** The corrected version is the one consistent with the rest of the article, since a rate-limited
hot structure should have load margin in hand, and the erroneous version contradicted it. **Ninth
consecutive article in which computing before writing caught a wrong claim, and the second in this
article after the crossover order-of-magnitude error.**

**The relation that closes the keystone was added.** Deceleration by drag at constant altitude
integrates to a time to shed the energy, and evaluating it gives 102 minutes at the record altitude,
18 at 20 km, and 8 at 15 km, against a total flight duration of 8 to 12 minutes. **The aircraft cannot
dispose of its energy where it acquires it. It must descend into denser air to do so, and descending is
precisely what raises the heating.** That is the keystone stated as a single trap and every other
result in the sizing section is a term in it.

**Other results added.** The stagnation temperature is 2,271 K, so **the air is 2.46 times hotter than
the metal is permitted to become**, and 89.9 percent of the oncoming stream's total enthalpy is
kinetic, so the heat is the aircraft's own energy arriving back at it. Newtonian impact theory gives
Cp = 2 sin^2(theta), independent of Mach number, which is why a thick wedge fin keeps its effectiveness
and beats a three-degree surface by a factor of 11; the same relation puts the **trim angle of attack
at the record near 13.8 degrees**, so a hypersonic aeroplane does not fly nose-first. The blunt-body
trade eliminates to D_nose ~ q_dot^-4, so **halving the heating costs sixteen times the nose drag**.
The B-52 supplies **under seven percent** of the energy budget. A 1.5 mm skin is through-soaked in half
a second and has no interior. A kilogramme of ablator absorbs nine times what a kilogramme of structure
absorbs reaching its limit.

**Primary-reference review complete, 2026-08-08. 1142 lines, 90 display equations, 252 references,
12,993 body words.** References rose from 77 to 252 across 31 edits, research anchors from 58 to 233.
**Primary sources are 220 of 233 dated, or 94.4 percent**, the highest share the series has carried
after A311's 95.9 at the same stage.

**The pool was too small and was harvested before it was audited**, per the A310 rule. The first sweep
had returned 199 NTRS records and only 17 X-15-specific documents, which is not what a nine-year
programme produces, so a supplementary sweep aimed at the threads the draft and equation passes opened
added 82 NTRS, 100 DTIC, 122 period, and 39 OSTI records and took the master from 673 to 991.

**Two documents found that bear directly on derivations the equation pass produced.** [Keener and Polek
1972] reports measurements of the Reynolds analogy for a hypersonic turbulent boundary layer **on a
nonadiabatic flat plate**, which is precisely the relation the energy-partition result runs on and
precisely the wall condition it runs at; the article derived it without knowing it had been measured.
And [Edney 1968] is the canonical treatment of anomalous heat transfer on blunt bodies in the presence
of an impinging shock, **published the year after the flight that demonstrated the effect on a crewed
aircraft**. A cluster around it now covers the mechanism that destroyed the pylon.

**A second finding worth recording.** The wind-tunnel facility literature establishes that no ground
facility of the period could match Mach number, Reynolds number, and enthalpy at once, which is the
quantitative reason an aircraft was needed at all. And the same flight-versus-tunnel comparison was run
again on the X-24B a decade later, so the calibration problem the X-15 existed to address had not been
solved by its successors.

**Selection discipline.** A loose theme filter surfaced uranium and niobium metallurgy, a Marine Corps
acquisition study, aerial cannon shells, titanium brazing, industrial wind tunnels, and ice crystals in
hypersonic flow, all matching on keywords. **Every one was rejected by title inspection before writing**,
which is what the dump-titles-before-writing rule exists for. Six link-text mismatches were caught by
the invariant and repointed to the master displays.

Citation density 19.32 per thousand body words, comparable to A311's final 20.2. The URL-stability
guard fired no drift when the master was rebuilt on 318 new records.

**Publication review complete, 2026-08-08. All four passes done.** **1368 lines, 99 display equations,
350 references, 15,267 body words.** Contemporary references rose from 13 to **111, or 33.5 percent of
dated**, inside the 101 to 189 absolute range held since A301, closing the largest contemporary gap any
article had carried into a publication review. **All three densities inside band. Nothing trimmed at any
point in any pass.**

**The pass found a limit on the article's own method, which is the most useful thing it did.** Every
relation in the article treats air as a perfect gas at gamma 1.4. Setting the stagnation-temperature
relation equal to the onset of oxygen dissociation near 2,500 K gives Mach 7.06 at the record altitude,
and **the X-15 reached Mach 6.70, or 94.8 percent of it**. The article's arithmetic is therefore very
nearly at the edge of its own validity at the aircraft's fastest condition. That is not a coincidence:
it is close to what the phrase hypersonic aeroplane could mean in 1954, because a vehicle going
meaningfully faster is conducting chemistry rather than managing a thermal load.

**A result changed direction.** The article found that a hot wall absorbs a smaller fraction of the
friction dissipation than a cold one. Extending the same relation shows the fraction tends to the
recovery factor over two, about 44.5 percent, as speed grows, because the adiabatic wall temperature
itself grows as V^2. **A faster vehicle gives a larger share of its friction dissipation to its
structure, not a smaller one**, so the protection the X-15 enjoyed does not scale. Both statements are
in the text and neither supersedes the other.

**The keystone ratio evaluated elsewhere.** The X-15's 2.26 becomes 3.15 for Mach 8 cruise, 13.8 for a
glide vehicle, **33.6 for orbital entry**, and 66.9 for lunar return, so orbital entry is 14.9 times
worse by the measure the article is built on. And the reason the hot metallic structure was abandoned
is a fourth power: **an ultra-high-temperature ceramic leading edge at 2,273 K rejects 39.2 times what
Inconel at its 922 K limit rejects**, and can sustain 198 percent of the heating rate that nearly
destroyed the X-15A-2, against Inconel's 5.1 percent.

**Two defects found.** A URL sweep of all 336 external URLs found **one persistently dead DOI**, a 2026
paper on medical risks in suborbital flight, and **the citation was removed rather than shipped**; a
second 404 proved transient and resolved on recheck. Two link-text mismatches were caught by the
invariant. The URL-stability guard fired no drift on a rebuild over 689 new records.

Citation density 22.73 per thousand body words, above A311's final 20.2, which reflects a survey
section carrying 111 contemporary references. Primary sources 220, or 66.5 percent of dated.

## X-Planes Bell X-14 A311 2025-10-20

`x_planes_bell_x14.markdown`, A311, editorial date 2025-10-20, series `x_planes` index 15 of 72.

854 lines, 51 equations, 95 references, 13,322 words after the draft pass; 1088 lines, 103 equations,
95 references, 15,001 words after the equation review; 1300 lines, 103 equations, 267 references,
17,821 words after the primary-reference review; **1515 lines, 109 equations, 386 references, 19,934
words after the publication review.** Lines and equations inside band, references 6 above the ceiling
and reported rather than trimmed. **Nothing was trimmed at any point in any pass.**

**The first article in the series whose subject is an instrument rather than a vehicle.** The X-14 is
the variable-stability aircraft that produced the attitude control-power criteria A310 borrowed
anachronistically and flagged in its own epistemic state, so the article opens by naming the debt.
The keystone is the criteria themselves rather than any property of the airframe.

**Keystone identified as the measurement of a threshold in human response.** The physics gives a
floor and a ceiling more than an order of magnitude apart and cannot locate the answer between them,
because the quantity is a property of a closed loop containing a person. Locating a threshold requires
crossing it, which requires an aircraft that can be made deliberately deficient while a pilot is
flying it. **The airframe is therefore dimensioned to make the independent variable adjustable rather
than to make the aircraft good**, which inverts the usual relationship between a research aircraft and
its research question.

**Central result.** The reaction-control bleed fraction is inverted rather than estimated. The
tip-turbine fan report states that halving the bleed returned four percent more engine thrust, which
gives beta = 0.08/1.08 = 7.41 percent exactly. At the reported 3,700 pound test weight and 1.1 to 1.2
available thrust-to-weight ratio that cost 397 pounds of thrust and **consumed 34.9 to 51.8 percent of
the entire hover margin**, so between a third and a half of everything the aircraft could lift beyond
its own weight was spent on being controllable.

**Results the sources do not state.** The roll inertia is recovered at 3,333 kg m2 from two numbers in
two different reports, giving a radius of gyration of 13.7 percent of span, mid-band for a
fuselage-heavy layout, which validates the recovery; the replacement fans were specified at exactly
the existing maximum authority and not above it, indicating bleed rather than control power was the
binding constraint. **Control power at fixed bleed fraction falls inversely with span**, so a jet-lift
aircraft with wingtip reaction controls exhausts a twenty percent thrust margin near 28 metres of
span and a Do 31 sized vehicle would need 3,542 pounds of thrust at each wingtip. **The original
Viper-engined X-14 had a thrust-to-weight ratio of 0.843 to 0.946 at the weight the X-14A later
hovered at**, below unity on either reading of the contested engine rating, so the J85 re-engining was
a precondition for the research programme rather than an upgrade. Control power shows **sharply
diminishing returns with an exponent of minus 0.26**. The variable-stability system's synthesised
damping and the pilot's authority draw on one shared budget, which explains the source's otherwise
modest remark that the tested grid covered conditions to the ability of the X-14A. And **gravity was
not adjustable**, so the aircraft reproduced lunar attitude dynamics exactly and lunar translation
2.46 times too fast, which is why the Lunar Landing Research Vehicle had to exist.

**An archive hole, stated in the article.** NASA TN D-1328, the origin of the criteria, carries no
downloadable document and is returned by the NTRS search endpoint for no phrasing of its own title.
It was located through its citation in a later report, and every quantitative claim is taken from the
complete successor TN D-2701. **No pilot ratings are asserted anywhere**, because the figure carrying
them did not survive text extraction.

**Two defects in the numerical spine, both caught by running it rather than reading it.** The
repositioning analysis used a = g theta and searched tilt over a bounded range whose upper bound it
reported as the optimum for every control power above 1.4, so the printed optimum was the edge of the
search interval. And the threshold section had invented plausible Cooper ratings and interpolated a
boundary from them, which would have manufactured the article's headline number from data in no
source. **Seventh article running in which computing before writing caught a claim that reading would
have passed.**

**Three defects caught by reading and counting**, all of which passed every automated check: a phrase
repeated across a paragraph seam, a symbol collision between the disturbance fraction and the
radius-of-gyration fraction, and a sentence promising four subsections where five stood.

**Equation-density review complete, 2026-08-08. 1088 lines, 103 display equations, 95 references,
15,001 body words.** Equations rose from 51 to 103 across 22 edits and are now inside the 90 to 130
band. Nothing was trimmed.

**The pass corrected a claim inherited from A310.** The draft said position is the third integral of
the pilot's control input, following the previous article, which reasoned that attitude is the
integral of what the control does. Writing the transfer function down shows that step is wrong. A
reaction nozzle produces a moment and a moment produces angular acceleration, so attitude is the
double integral of control and **position is the fourth integral**. The reconciliation is that the
earlier description holds below the damping break frequency, since the composed plant is
g CP / (s^3 (s + D/I)), which is third order for omega much less than D/I and fourth order above it.
**Hovering is therefore a third-order problem or a fourth-order one depending on how much damping the
aircraft has**, and the X-14A is the only aircraft in the series that could have shown the difference
because it is the only one whose damping was a dial. The distinction is not cosmetic: a fourth-order
plant demands two derivatives of lead from the pilot rather than one, which is the clearest available
explanation of the 1972 Ames finding that attitude stabilisation gives the best handling qualities for
the least control power. Recorded in the Epistemic State as a correction to the previous article.

**Other results the pass produced.** An optimally flown hover correction **spends exactly half its
time changing attitude and half translating**, whatever the control power and whatever the distance,
which falls out of the stationarity condition theta* = (1/2) sqrt(CP d / g). The wind is confirmed as
a position problem rather than an attitude problem on this aircraft as it was on the X-13, since a ten
metre per second wind is 5.9 percent of the maximum control power as a moment but requires a permanent
1.36 degree tilt and costs 11.7 metres of drift in ten seconds if uncorrected. The compounded overhead
is now stated: control takes 34.9 to 51.8 percent of the hover margin and the disturbance allowance
takes two fifths of what that bought, so **only 21 to 31 percent of the margin reaches the pilot as
manoeuvring authority**. The pitch nozzle must be about forty percent stronger than the roll nozzle
for the same control power, because the aircraft is wider than it is long. The J85-GE-19 installation
bought about 590 pounds more lift than the J85-GE-5, which is what set how much authority the later
experiments could give away. And a lunar vehicle must tilt 27.9 degrees to match the acceleration a
terrestrial one gets from 5 degrees, while a weight-cancelling simulator must support 83.5 percent of
the vehicle.

**Two defects in the new spine, both caught by running it.** The diverter section printed a hardcoded
constant rather than the deflection it claimed to sweep, and **the closed form for the optimum tilt was
simply wrong**, given as (CP d / 4g)^(1/3) and missing the numeric optimum by six degrees; the correct
form is (1/2) sqrt(CP d / g). A pronoun for a generic pilot was also corrected.

**Primary-reference review complete, 2026-08-08. 1300 lines, 103 display equations, 267 references,
17,821 body words.** References rose from 95 to 267 across 26 edits, research anchors from 72 to 244.
**All three densities are now inside band and nothing has been trimmed at any point**, with lines
landing exactly on the 1300 floor.

**Primary sources are 234 of 244 dated research references, or 95.9 percent**, which is the highest
share the series has carried and reflects that the X-14's subject is almost entirely a 1955 to 1985
technical-report literature. Composition is NTRS 105, period 84, DTIC 45, modern 10.

**Two documents found that the article had been missing.** [Hegarty et al 1965] describes a system for
varying the stability and control of a deflected-jet fixed-wing VTOL aircraft, which is the X-14A's
own analogue variable-stability system and is the primary description of the apparatus that produced
every number in the article. It was previously uncited because its title names the configuration
rather than the aircraft. And [Key 1971] is an account of the generation of MIL-F-83300, **which
supplies the primary source for the specification lineage the What the Data Changed section had
previously asserted without one**.

**Corroboration found for two claims the article derived independently.** The scaling argument now
has a second contemporary paper alongside Johnston and Friend, since [Johnston et al 1965] reports a
study of size effects on VTOL handling-qualities criteria in the same year; two papers on size
dependence within three years of the first results is not a coincidence. And the objection this
article raises about two pilots was raised contemporaneously in [Kidd and Bull 1963] on how handling
qualities requirements are influenced by pilot evaluation time and sample size, **published two years
before the lateral control experiments it applies to**.

**The bandwidth successor now has primary sources.** The claim that the field changed the variable
rather than the number is supported by the Pausder and Blanken bandwidth and time-delay experiments
of 1992 to 1994, which are the X-14A's procedure with the independent variables replaced.

Citation density 16.17 per thousand body words, at the top of the 12.82 to 16.58 range A310 held.
Three repeated-phrasing collisions introduced by the insertions were caught by scanning and reading
and were varied.

**Publication review complete, 2026-08-08. All four passes done.** **1515 lines, 109 display
equations, 386 references, 19,934 body words.** Contemporary references rose from 10 to **129, or 35.5
percent of dated**, inside the 101 to 189 absolute range the series has held since A301. References
finish 6 above the 380 ceiling, reported rather than trimmed under the standing no-reference-limit
directive, as A309 did. Nothing was trimmed at any point in any pass.

**The pass ran the article's own relations on a vehicle with no bleed, and the result is the strongest
finding in the article.** Deriving control power for a multirotor from first principles gives
CP = c_g min(r-1,1) g / (2 kappa^2 b), which is **inversely proportional to span, the same law and the
same exponent this article derived for bleed-fed reaction nozzles, by a mechanism that shares no
hardware with it**. The inverse-span dependence is therefore not a property of reaction controls. It
is a property of making moments with forces at the extremities of a vehicle whose thrust scales with
its weight, and it survives complete replacement of the propulsion system.

**The cost changed character rather than magnitude.** The X-14A's bleed was a standing tax of 7.41
percent whether or not the pilot commanded anything. A multirotor's differential is zero-sum, so the
mean cost of attitude control is zero and what the vehicle pays instead is headroom it needs anyway.
**The constraint that dominated the X-14 has been dissolved rather than solved**, which is the same
verdict A310 reached about the X-13 by a different route.

**The constraint moved rather than vanishing.** Setting the multirotor relation equal to the X-14A's
maximum gives 17.3 metres of span at a thrust-to-weight ratio of 1.4, against the 28 metres at which
this article found jet lift exhausting its bleed budget. **Large hovering aircraft are still hard, and
for a reason the X-14A measured.**

**The loop-order result gained a retrospective sting.** A modern attitude loop closes near 10 to 30
radians per second against the X-14A's damping breaks of 0.45 and 0.59, so **the aircraft sat in its
fourth-order regime across the whole of the band its pilots worked in**, which is the sharpest
available explanation of why it was hard to fly.

Representative modern vehicles: a small quadrotor at 173 rad/s2, a cargo multirotor at 54.2, an air
taxi at 4.33, against the X-14A's 2.0, or 87, 27, and 2.2 times.

**Two defects found and fixed.** The URL-stability guard fired on the master rebuild and caught **two
cited anchors that had drifted to different documents**, a biplane tail-sitter paper and a shared
control paper, both repointed. And measuring citation density by section found **The Designation
section at 56.6 citations per thousand words**, the densest in the article, because the primary pass
had attached two paragraphs about the criteria's later application to a section about the designation;
they were moved to What the Data Changed with the citation count asserted unchanged.

**One URL defect found by sweeping all 372.** The Lunar Landing Research Vehicle reference pointed at
a Wikipedia title that returns 404 and was repointed to the page that exists. The sweep returned 185
plain 200s, 121 publisher 403s from bot detection, 51 DTIC DOI redirects to a .mil host that 403s by
policy, 13 202s, and one openlibrary rate limit. **An HTTP 200 does not verify a citation** and this
sweep does not claim to.

Primary sources remain 234, or 64.5 percent of dated, above A310's 52.4 percent.

## X-Planes Ryan X-13 Vertijet A310 2025-10-19

`x_planes_ryan_x13.markdown`, A310, editorial date 2025-10-19, series `x_planes` index 14 of 72.

810 lines, 56 display equations, 143 reference definitions, 11,369 words after the draft pass. All
three densities approach their bands from below, at 810 against a 1300 floor, 56 against 90, and 143
against 250. Reported rather than padded.

**The X-13 ends the run of five.** The X-8 through the X-12 were sounding rockets, missiles, and
ballistic weapon articles. The X-13 is a manufacturer's prototype built in two examples under a
research contract with no operational intent, which is the pattern the X-1 established, and the
article argues that this matters for the closing article because **the run of five was an
interruption rather than a redefinition.**

**Keystone identified as control authority through the transition.** Aerodynamic control moment
scales with the square of speed and vectored thrust does not depend on speed at all, so the two cross
exactly once and the aircraft must be controllable on both sides and at the crossing. The X-11 and
X-12 could not have posed this question because neither was ever at zero airspeed while airborne.

**Central result.** The elevons meet the control-power criterion at 48.2 metres per second against a
stall speed of 52.5, so **the control surfaces become adequate at 91.8 percent of the speed at which
the wing starts flying**, and vectored thrust supplies 3.86 times the criterion everywhere below.
Writing the ratio out shows the wing area and the air density both cancel, so **the ratio is a
property of proportions and not of scale**, which is why a one-fifth-scale model could demonstrate
the same handover.

**Results the sources do not state.** The three axes hand over in sequence rather than together, at
0.62 of stall for yaw, 0.72 for roll, and 0.92 for pitch, so the pilot feels the aircraft become
conventional one axis at a time across a band of about sixteen metres per second. **The entire fuel
load is about eleven minutes of hovering**, and hover endurance depends only on fuel fraction and
specific consumption and therefore not at all on the size of the aircraft. The transition itself
costs 12.6 pounds of fuel and 4.9 seconds at the maximum 47.7 degree tilt, so **the manoeuvre the
programme existed to demonstrate is about one percent of the fuel and the hovering that brackets it
is everything else**. A cautious take-off and landing profile spends 54.6 percent of the fuel without
leaving the airfield. **Holding position to a metre over five seconds requires holding the mean tilt
below half a degree**, because hovering is a third-order position loop with no aerodynamic restoring
moment anywhere in it. A ten metre per second crosswind is only 7.0 percent of the pitch requirement
as a moment and 72 metres of drift in thirty seconds as a position error, so **the wind is a position
problem and not an attitude problem**. The ground observer who talked the pilot down is best
understood as a delayed sensor inside that loop, and a delay of 0.3 seconds consumes the entire hook
tolerance at one metre per second of closure. **Deleting the undercarriage bought roughly a quarter
more fuel.** The exhaust loads the ground about a hundred times more heavily than a rotor of the same
span. And a turboprop tail-sitter hovers with roughly stall-level dynamic pressure already on its
control surfaces while a turbojet tail-sitter hovers with none, **which is the whole design
difference between the X-13 and the XFY-1**.

**An error was made and corrected during the pass.** The first writing said a one-fifth-scale model
imposes a twenty-fifth of the ground pressure. For geometric scaling at fixed thrust to weight the
disc loading goes as the first power of length, so it is one fifth. **Sixth article running in which
writing a relation down caught arithmetic carried as an assertion.**

**A section ordering defect was found and fixed.** The three-axis summary table cited a roll
crossover derived two sections later, and the Roll section was moved ahead of the Yaw section so the
figure is established before it is used.

**Method note.** The master table is built from the A310 harvest alone. The generator inherited from
A309 read both the current and the previous article's directories, which would have imported six
hundred documents about ballistic missiles into an article about a tail-sitting jet.

**Archive note.** Querying NASA's technical archive for `X-13 Vertijet` or `vertijet` returns nothing
at all, and `Ryan X-13` returns the spin-tunnel series and the one-fifth-scale hovering and
transition tests. **The vehicle is indexed under the name its engineers used and not the name the
public learned**, which is the X-10 project-number lesson in a new form.

**Verification**: all 176 worked values re-derived independently with zero corrections beyond the one
described. 45 of 45 fixed identifiers at 200, 82 of 82 DOIs Crossref-resolved on title at the 0.85
threshold with zero flagged, 130 URLs with zero duplicates, no hand-entered identifier anywhere.
`_verify.py` at the 0-error 21-warning corpus baseline. Zero contractions, em-dashes, en-dashes,
prose colons, prose semicolons, prose parentheticals, doubled words, duplicate headings, unbalanced
emphasis markers, lone dollar-delimited lines, or adjacent display-math seams. All twenty insertion
seams read by eye. Isolated build succeeding with 56 rendered display blocks matching the source
count exactly, Part 14 navigation, eleven tables, no unresolved reference links and no surviving
Liquid tags. `aircraft` at 8.83 and `control` at 5.52 per thousand body words are the subject and
keystone nouns and are reported rather than remediated.

**Equation pass complete, 2026-08-07.** 56 to **91 display equations**, inside the 90 to 130 band.
1047 lines, 143 references, 13,590 body words.

**The pass found an imprecision in the article's own framing.** The opening said the two control
systems cross exactly once and then computed a crossing at 48.2 m/s. Those are two different
crossings: the elevons equal the deflected thrust at **94.7 m/s** and meet the criterion at 48.2.
The article now separates them, and tabulating the aerodynamic share shows that **at the adequacy
crossing the elevons supply only a fifth of the available authority**.

**Three results changed what the article says.** The design spiral grows linearly with size, so
**doubling the length doubles the fraction of the engine that attitude control eats**. A tumble is
stopped in 0.52 s with the engine running and not at all without it, since both the nozzle and the
puffers are engine-powered, which is why a spin parachute was tested. And Froude scaling puts the
one-fifth model at 23.5 m/s and 2.19 s with a Reynolds number 11.2 times lower, which is exactly the
division between what the models settled and what they did not.

**The largest exposure is now tabulated.** Halving the assumed elevon effectiveness moves the
crossover ratio to 1.298 and inverts the central claim.

**The contemporary result worth keeping**: a rotor of the X-13's span with a battery at the same
seventeen percent mass fraction hovers 8.2 to 10.9 minutes against the X-13's eleven, because two
roughly forty-fold factors cancel. Flagged as coincidence, not law.

All 268 worked values re-derived with zero disagreements, isolated build clean at 91 rendered display
blocks matching source exactly.

**Primary pass complete, 2026-08-07.** **143 to 250 reference definitions, exactly the floor.**
1184 lines, 91 display equations, 15,521 body words. **Primary sources 167 of 233, or 71.7 percent of
dated, up from 61.1.**

**The pass opened with a harvest rather than a coverage audit**, reversing the usual order per the
draft pass's warning that the 665-entry pool would not support the floor. It would not have. The
harvest returned 684 records and took the pool to **1,305 entries**.

**The source-base finding is that the article is held up almost entirely by documents about other
aircraft.** Almost nothing rests on a document about the X-13. It rests on documents about the
configuration, the flight condition, the test technique, and the pilot's task. An article about a
vehicle with almost no record of its own can still be dense, provided the question it asked was one
other people were also asking, which was true here and not true of the X-10.

**One seam defect caught by reading**, where an insertion left two clauses running together across a
paragraph break with every automated check passing it. **One false alarm recorded**, where
`_verify.py` appeared to jump to 40 warnings because the command had inherited a working directory
inside the scratch build tree.

250 reference definitions, 237 external URLs with zero duplicates, 86 of 86 fixed identifiers at 200,
148 of 148 DOIs Crossref-resolved at 0.85 with zero flagged, all 268 worked values reproducing, and
an isolated build clean at 91 rendered display blocks matching source exactly.

**Publication review complete, 2026-08-07. All four passes done.** **1346 lines, 91 display
equations, 336 references, 17,380 body words. All three densities inside band and nothing trimmed at
any point**, which is the fifth article in the series to finish that way and the first with no band
exceeded in either direction.

**The review ran the article's relations on a modern vehicle and corrected an overstatement.** A
small electric tail-sitter's disc loading and wing loading are the same quantity to within a factor
of two against the X-13's ratio of 84, so the design difference that separated it from the XFY-1 has
been dissolved rather than solved. But holding the energy mass fraction equal gives **12.9 minutes of
hover against 11.0, an improvement of about seventeen percent in seventy years**. As an effective
specific consumption, a battery forty-eight times worse per kilogramme driving a rotor seventeen
times better at converting power into thrust comes out fifteen percent ahead.

**Contemporary coverage closed with a 64-query sweep returning 710 records**, taking contemporary
references from 47 to **133, or 41.7 percent of dated**. Twelve subsections replaced five.

**Two defects found and fixed.** The section replacement silently dropped three equations, caught by
measuring. And an en dash reached the prose inside a citation display string, fixed by an automatic
rule in the normaliser rather than by patching the regenerated markdown.

336 reference definitions, 323 external URLs with zero duplicates, all 268 worked values reproducing,
isolated build clean at 91 rendered display blocks matching source exactly.

**Status**: committed and **pushed**. **Not published.** Fourteen of seventy-two complete.

## X-Planes Convair X-12 A309 2025-10-18

`x_planes_convair_x12.markdown`, A309, editorial date 2025-10-18, series `x_planes` index 13 of 72.

1066 lines, 115 display equations, 165 reference definitions, 13,142 words after the draft pass.
**Equations are inside band at 115 against 90 to 130, which no draft in this series has achieved
before.** Lines sit 234 below the 1300 floor and references 85 below the 250 floor. Both are reported
rather than padded, and the shortfall is deliberately smaller than A308's, which entered its review
passes at 678 lines and needed the largest publication-review expansion the series has performed.

**The X-12 is the Atlas B**, the same airframe as the X-11 with everything the X-11 lacked. An
operational sustainer, a separable booster section on explosive bolts, an airborne guidance computer,
an Azusa transponder, and a detachable nose cone. The structural material is referenced to A308 and
deliberately not re-derived, per the handoff warning that repetition was the trap for this article.

**Keystone identified as terminal velocity control.** A ballistic missile falls for 34.3 minutes and
cannot be steered during any of them, so everything is decided at cutoff. Range responds to burnout
speed with a dimensionless sensitivity of 4.34, or 6.04 kilometres per metre per second, so a two
nautical mile circular error probable allows 0.613 metres per second out of 7193. **One part in
eleven thousand seven hundred.** A308 derived that sensitivity and used it in a single sentence. This
article makes it the spine.

**Central result is the orbital margin.** Grazing circular speed is 7904 metres per second against
7193 for a ten-thousand-kilometre ballistic arc, a deficit of 711 metres per second or 9.9 percent.
Closing it at the sustainer exhaust velocity costs a mass ratio of 1.2645, which is 20.9 percent of
the burnout mass, or 1129 kilogrammes. **The predicted orbital allowance of 4266 kilogrammes
reproduces the reported SCORE on-orbit mass of 3980 to within 7.2 percent**, from nothing but the
range law, a published specific impulse, and a burnout mass taken from a different variant. The
weapon and the satellite launcher are the same machine with the payload changed.

**Results the sources do not state.** The minimum-energy trajectory is stationary in flight path
angle, so angle errors enter at second order while speed errors enter at first, and a tenth of a
degree costs 77 metres of range against the 0.0128 metres per second of speed that would cost the
same. Sustainer tail-off impulse uncertainty is 1.07 metres per second, which is 1.8 times the entire
error budget, so the verniers are a velocity-trim device before they are a roll-control device and
they cut the required timing precision by a factor of 43.4. An accelerometer bias of only 220 micro-g
exhausts the budget over a 280 second powered flight, which is the quantitative case for putting the
guidance on the ground in 1958. Lethal radius scales as the cube root of yield, so **halving the
circular error probable is worth a factor of eight in yield** and a cutoff error of one metre per
second instead of 0.613 must be paid for with a weapon 4.34 times larger. Acceleration falls by a
factor of 4.37 at booster jettison. **The flattening of the Earth is 21.4 kilometres, which is 5.8
times the entire miss budget**, so an intercontinental weapon cannot be aimed on a sphere and the
ballistic missile created a geodetic requirement it could not itself satisfy. The autopilot bandwidth
must live in a window of 31 between a 1.14 second aerodynamic divergence and a 4.32 hertz first
bending mode, and because the shell is pressure-stabilised that bending mode moves during the ascent.
S-band telemetry tolerates 77 times the ionisation that very high frequency does. SCORE was a
store-and-forward relay with a four percent duty cycle. Six of ten against the X-11's four of eight
gives a pooled z of 0.42, so **the Atlas B is not measurably more reliable than the Atlas A** despite
carrying far more.

**The article argues against its own keystone at the end.** Accuracy decided whether the weapon
worked and did not decide whether it was kept. A cryogenic missile needing roughly fifteen minutes to
load consumes 44 percent of the adversary's 34.3 minute flight time, which is not a second-strike
posture, and Minuteman loads nothing.

**A method improvement was made during the pass.** The manual reference-display corrections are now
keyed by URL rather than by anchor. A308 keyed them by anchor, and regenerating the master table for
A309 permuted the disambiguation suffixes on the five Difficulties Review volumes so that every one
of the five manual displays landed on a different volume than it named. A URL is the only stable
identity a harvest record has, and each volume is now named by the subsystem it actually covers.

**Verification**: all 130 worked values re-derived independently with zero corrections to the
article. Two checker disagreements were both the checker, once on a zero-target tolerance and once on
a missing SI-to-cgs conversion in the Sutton and Graves correlation, and the second exposed real
sloppiness in the article's unit labelling, which was repaired. `_verify.py` at the 0-error
21-warning corpus baseline. Zero contractions, em-dashes, en-dashes, prose colons, prose semicolons,
prose parentheticals, doubled words, duplicate headings, lone dollar-delimited lines, or adjacent
display-math seams. 22 of 22 fixed identifiers at 200, 127 of 127 DOIs Crossref-resolved on title at
the 0.85 threshold with zero flagged, zero duplicate URLs, and no hand-entered identifier anywhere.
Isolated build succeeding with 115 rendered display blocks matching the source count exactly, Part 13
navigation, nine tables, and no unresolved reference links or surviving Liquid tags.

**Equation pass complete, 2026-08-07.** 115 to **135 display equations**, five over the 130 ceiling,
reported rather than trimmed because the genre rule that produces the band takes precedence over the
number and every addition answers a claim the draft already made. 1162 lines, 165 references, 13,712
body words.

**The pass found a wrong claim.** The draft asserted all-inertial guidance waited on components
improving "by roughly two orders of magnitude". Deriving the gyroscope drift requirement gives
**0.329 degrees per hour** against period instruments at of order one, so the gap is **a factor of
about three**, and the article's architectural inference is now weaker rather than stronger. Fifth
article running in which writing a relation down caught arithmetic carried as an assertion.

**Three results changed what the article says.** The error budget saturates, and removing the largest
contribution entirely at infinite cost buys only 14.0 percent. The oblate gravity field displaces the
impact point by of order **34 kilometres, nine times the miss budget**, where the draft said only
that the departure "is not small". The angle-versus-speed forgiveness ratio scales as the inverse
square of the angle, so it is 191 at a twentieth of a degree and **1.9 at half a degree, where the
angle stops being free**.

Also added: the identity that the factor by which the vehicle becomes harder to stop is exactly its
sustainer mass ratio of 4.38; the first-order azimuth relation, whose 23 percent shortfall against
the exact value measures where the article's own linear sensitivity stops holding; the requirement
that a range instrument be 3.1 times better than the missile it certifies; the plasma-frequency
inversion and its square-law ratio; the variance-share relation; the speed-budget scaling across one,
two, and five nautical miles; and the boil-off holding time. All 160 worked values re-derived with
zero disagreements, isolated build clean at 135 rendered display blocks matching source exactly.

**Primary pass complete, 2026-08-07.** 165 to **263 reference definitions**, inside the 250 to 380
band. 1286 lines, 135 display equations, 16,482 body words. **Primary sources 220 of 246, or 89.4
percent of dated, up from 83.1 and the highest in the series.** Citation density 14.01 to 18.72 per
thousand body words.

**The pass caught two cited references that had silently become different papers.** Rebuilding the
master on the enlarged harvest moved two already-cited anchors onto unrelated documents. The
generator now compares each cited anchor's new URL against the URL recorded in the existing
reference section and refuses to regenerate on any change.

**The largest addition was unplanned.** The equation pass had established that the flattening of the
Earth is 5.8 times the miss budget, and the harvest contained nothing on geodesy. A sweep returned a
complete discipline, and a new section traces it from surface-gravity geoid determination to a
published world datum sixteen years after the first Atlas B flight. **The source-base finding is that
the weapon literature is classified and fragmentary while the literature the weapon depended on is
openly published**, because the shape of the Earth was not a secret.

All four debt sections closed. 251 external URLs with zero duplicates, 30 of 30 fixed identifiers at
200, 217 of 217 DOIs Crossref-resolved at 0.85 with zero flagged, isolated build clean.

**Publication review complete, 2026-08-07. All four passes done.** **1505 lines, 137 display
equations, 399 references, 18,179 body words. Lines inside band at 1505 against 1300 to 1600.**
Equations seven above the ceiling and references nineteen above, both reported rather than trimmed
under the standing directive of no length limit and no reference limit. **Nothing was trimmed at any
point in any of the four passes.**

**The review ran the article's own arithmetic forward**, recomputing the accuracy chain at a modern
circular error probable. A 120 metre weapon needs its burnout speed correct to one part in 362,029,
with 7.24 micro-g of accelerometer bias and 0.0107 degrees per hour of drift, **thirty-one times
better than the Atlas needed**. The cube-root yield scaling then gives a factor of **2.94 times ten
to the fourth**, so a warhead delivered to 120 metres does the work of one nearly thirty thousand
times larger delivered to two nautical miles. That ratio is why the arsenals grew more accurate
rather than larger.

**Contemporary coverage closed with an 84-query sweep returning 923 records**, taking contemporary
references from 23 to **158, or 41.4 percent of dated**, inside the 101 to 189 range held since A301.
Fourteen subsections replaced seven paragraphs.

**Two further anchor-drift cases, one caught by each guard.** The URL-stability guard fired on the
very next regeneration; the link-text invariant caught two more in citations being added. The two
mechanisms are complementary and neither covers the other's case.

399 reference definitions, 387 external URLs with zero duplicates, 31 of 31 fixed identifiers at 200
after two retries, 352 of 352 DOIs Crossref-resolved at 0.85 with zero flagged, 176 worked values
reproducing, isolated build clean at 137 rendered display blocks matching source exactly.

**Status**: committed and **pushed**. **Not published.** Thirteen of seventy-two complete.

**Superseded, retained for the record**: **contemporary references are 23, or 9.3 percent of
dated.** The absolute count is unchanged since the draft and the percentage fell only because the
primary pass grew the denominator, which is the count-versus-percentage behaviour the series has
seen before. Against the 101 to 189 absolute count held since A301 this is **the largest contemporary
gap any article has carried into a publication review**. Lines are 14 below the 1300 floor, the
closest any article in the series has come before its final pass, so closing the contemporary gap
will carry the article past the floor as a side effect. Equations are five above the ceiling and are
reported rather than trimmed.

## X-Planes Convair X-11 A308 2025-10-17

`x_planes_convair_x11.markdown`, A308, editorial date 2025-10-17, series `x_planes` index 12 of 72.

678 lines, 54 display equations, 160 reference definitions, 9,301 words after the draft pass. All
three densities are under band, at 678 against a 1300 floor, 54 against 90, and 160 against 250.
Reported rather than padded, but **this is further below band than A307's draft was** at 943, 84, and
213, so the three review passes have more to close here than they did there.

**The X-11 is the Atlas A**, the first flying article of the programme whose ballistic timeline the
A307 article computed as the reason the Navaho was cancelled. The two vehicles are separated by one
designation and four weeks, and the X-11 first flew on 11 June 1957 against a cancellation message
dated 12 July.

**Keystone identified as structural mass fraction**, and the vehicle cannot stand up without internal
pressure. Skin is 301 extra-full-hard stainless at 0.014 to 0.037 inches, giving a radius-to-thickness
ratio of 1622 to 4286, which is five to thirteen times thinner in proportion than an aluminium drink
can. The vehicle requires about five pounds per square inch of nitrogen when unfuelled.

**Central result derived and carried through to range.** The Atlas structural mass fraction of 4.58
percent gives a mass ratio of 21.85 and an ideal velocity of 8530 metres per second. Subtracting the
7193 metres per second that A307 established for a ten thousand kilometre ballistic trajectory gives
gravity and drag losses of 1337 metres per second, which is adopted as a calibration. Scaling the
structure and carrying it back through both relations gives ranges of 5676 kilometres at one and a
half times the structural mass, 3941 at twice, and 2346 at three times. **Making the structure half as
efficient costs sixty-one percent of the range**, which turns an intercontinental weapon into an
intermediate-range one.

**The series contribution is a contrast with A307 that neither article could make alone.** The X-10's
keystone was a drift rate, which accumulates, and twenty-eight minutes of flight could not measure it.
The X-11's keystone is a structural load, which is applied in full within the first two minutes, so a
flight reaching only 120 kilometres of apogee and a fifth of the intercontinental burnout speed still
applies every load the mission will ever apply. **A keystone that is exercised early can be validated
cheaply and a keystone that accumulates cannot**, and the difference is a property of the quantity
rather than of the programme.

**Further results the sources do not state**: the critical bending moment of a pressure-stabilised
cylinder is independent of skin thickness at $M = \pi p r^{3} / 2$, so five pounds per square inch
holds the vehicle against an 8.3 kilonewton tip load; the tensile allowable exceeds the knocked-down
compressive allowable by a factor of 67, which is where the mass saving comes from; the light gauge
cannot exist at full pressure, which demonstrates the thickness taper rather than contradicting it;
the common bulkhead saves about 227 kilogrammes or four percent of the empty vehicle; a
constant-acceleration vertical ascent reaches maximum dynamic pressure at exactly one scale height
independent of the acceleration; and the range sensitivity to burnout velocity is 4.34, so an
eight-hundred-metre accuracy requires cutting the engines to 0.13 metres per second out of 7193.

**Source base finding, which is a controlled contrast with A307.** The same Crossref route into the
defence archive that returns nothing for the Navaho project number MX-770 returns Flight Test Working
Group reports for individual Atlas missiles, five volumes of a Difficulties Review of the Atlas booster
and its ground support, propellant loading system design, and engine system-test data. Same archive,
same route, same query form, and the difference is that one programme was cancelled in 1957 and the
other flew for sixty years.

**An error was made and corrected during the pass.** The range-to-velocity sensitivity was first
written as approximately 2.4 with a malformed derivation, because that expansion was written without
computing the value first. The correct value is 4.34, confirmed by closed form and by numerical
differentiation, and the dependent figures changed from 24 to 43 kilometres and from 0.24 to 0.13
metres per second. This is the defect the compute-before-writing rule exists to prevent and it recurred
the moment the rule was skipped.

**Verification**: all 78 worked values re-derived independently with no corrections beyond the one
above. 160 references with zero undefined, zero orphaned, and zero duplicate URLs. `_verify.py` at the
0-error 21-warning corpus baseline. Zero contractions, em-dashes, en-dashes, prose colons, prose
semicolons, prose parentheticals, doubled words, duplicate headings, display-math seam defects, or lone
dollar-delimited lines. Isolated build succeeding with 54 rendered display blocks against 54 in source,
Part 12 navigation, both tables, no unresolved reference links and no surviving Liquid tags.

**A generator defect was fixed before it could ship.** The master-table builder deduplicates by URL from
the outset for this article, carrying forward the A307 repair, and the manual author-display corrections
for the five Difficulties Review volumes live in the normaliser so they survive regeneration.

**Equation-density review performed on request.** Baseline 54 display equations across 8697 body words,
6.2 per thousand. The structural audit found no orphaned or duplicate subsections. 38 equations added
across 18 edits, taking the article from 678 lines and 54 equations to 854 and **92**, which is inside
the 90 to 130 band. References unchanged at 160.

**The pass corrected the draft's own claim.** The draft wrote the staging-gain relation and then
asserted without evaluating it that the gain was modest. Evaluating it gives **1044 metres per second
for a three-tonne jettison, or 12 percent of the whole ideal velocity**. The intuition is wrong because
the benefit of staging depends on the ratio of jettisoned mass to burnout mass rather than to gross
mass, and three tonnes against a burnout mass of 5395 kilogrammes is an enormous fraction. The
one-and-a-half stage arrangement therefore captures most of the value of staging rather than giving it
up, and the article's argument was rewritten accordingly.

**The pass also explained the article's own headline number.** Inverting the buckling relation for the
pressure that produces an equal axial tension gives **2.58 pounds per square inch at the governing
heavy gauge**, so the reported five-pound standing specification carries a margin of 1.94 on the
calculation. A specification at roughly twice the computed requirement is what a designer writes when
the requirement rests on a knockdown factor he does not trust.

Other relations added: Euler column buckling of the whole vehicle at 121 times the empty weight, which
rules out the global mode and establishes that local shell buckling is the failure; the fixed hoop-to-axial
ratio of two, which is why a tank splits lengthwise; tank volume, propellant split, and the finding that
**52.6 kilogrammes of nitrogen holds up 5395 kilogrammes of steel, a ratio of 103 to one**; the acoustic
environment at 153 decibels and 883 pascals at thirty metres; the pogo coupling condition against a
53 hertz solid-bar mode; the Allen and Eggers result that peak reentry deceleration is independent of
ballistic coefficient, giving 64 g against the booster's 3.44; boil-off at 7.5 percent of the oxygen load
per hour; the maximum dynamic pressure of 9736 pascals, which is **two percent of the internal tank
pressure**; the aerodynamic bending moment at three percent of the pressure-stabilised capacity; the
proof and burst factor chain; the tank figure of merit of under seven kilogrammes per tonne of
propellant; the four-to-one experimental scatter in shell buckling with the design factor at the
eleventh percentile; and the orbital comparison showing that **an intercontinental missile is already
92 percent of the way to orbit**, which is why the Atlas became a launcher and the Navaho became nothing.

**Equation-pass verification**: all 42 new worked values re-derived independently, with one correction.
The pressure fluctuation at 153 decibels was first written as roughly six hundred pascals and is 883,
and the relation was rewritten to compute it from intensity directly rather than from the rounded level.
All 78 previously verified values still reproducing. Zero duplicate headings, zero display-math seam
defects, zero lone dollar-delimited lines, zero paragraph-repeated citations. 92 rendered display blocks
confirmed in the built HTML against 92 in the source, Part 12 navigation, `_verify.py` at the 0-error
21-warning corpus baseline.

**No zero-equation subsections over 180 words remain**, against two at baseline.

**State after the equation pass**: 854 lines, 92 display equations, 160 references, 11,180 words.
Equations inside band. Lines remain 446 short of the 1300 floor and references 90 short of the 250
floor, both of which the reference-density and publication review passes must close, and the gap is
larger than it was at the same point in A307.

**Primary-reference review performed on request.** Baseline measured 79 primary of 149 external, or
**53.0 percent**, which is below A307's 61.5 baseline, with only 11 NTRS records cited, implausibly low
for an article whose keystone is shell stability. A citation-coverage audit found **eleven sections over
180 words at or below four citations per thousand**, and every one was a section the equation pass
created or expanded. That is the fourth article running in which the equation pass arrived without its
period sources.

A supplementary harvest of 43 NTRS, 20 DTIC, and 18 period queries returned 158 new NTRS, 171 new DTIC,
and 172 new period records, taking the master index from 845 to 1289 entries with zero duplicate URLs.
74 primary documents were added across 22 edits, taking references from 160 to **234** and primary
sources to **153 of 212 research, or 72.2 percent, and 68.6 percent of external**. Both figures are the
highest in the series, against A307's 69.3 percent peak.

**The best single find is the measurement the article's keystone section describes.** [Miller and Gerus
1966] reports the bending strength of a large thin-walled pressure-stabilised cylinder, which is the
relation derived in the equation pass tested on hardware of the right size. The article had derived the
relation and computed with it without knowing that the period had measured it directly.

**The second-best find explains why the design allowable is a knockdown factor rather than a theory.**
Peterson 1960 correlates measured buckling strength of pressurised cylinders against the pressure
parameter, which is the empirical form the design offices actually used, and Babcock and Sechler 1962
and 1963 measure how much of the classical strength an initial imperfection removes.

Other threads closed: ground-wind induced oscillation on the pad, which is the load case the article had
entirely omitted and which for a pressure-stabilised vehicle is resisted by the standing five pounds
rather than the flight sixty, with a whole period meeting devoted to it; sonic fatigue as a named
discipline with its own test methods and statistical machinery; cryogenic pressurisation, autogenous
systems, and pre-launch conditioning; the period trajectory and staging machinery the range table rests
on; and the reentry deceleration result, which turns out to have been computed by Scherberg and Rubin in
1953, four years before the X-11 flew.

**Coverage after the pass is four thin sections against eleven**, and three of the four are synthesis
sections that correctly carry no citations, namely the Source Base, the Epistemic State, and the
Conclusion.

**A diction defect was introduced and repaired within the pass.** The additions drove the leading
citation construction to 39.1 percent against a house norm of 20 to 27, because the rule to vary while
writing rather than afterwards was not followed. Fifty-four rotations brought it to **18.8 percent**,
with the top actual construction at 3.2 percent.

**Primary-pass verification**: 234 references with zero undefined, zero orphaned, and zero duplicate
URLs. **All 23 fixed identifiers at 200 and all 192 DOIs Crossref-resolved on title at the 0.85 threshold
with zero flagged**, and the article contains no hand-entered identifier anywhere. All 78 worked values
still reproducing. `_verify.py` at the 0-error 21-warning corpus baseline. Zero contractions, em-dashes,
en-dashes, prose colons, prose semicolons, prose parentheticals, doubled words, duplicate headings, or
display-math seam defects. Isolated build succeeding with 92 rendered display blocks, Part 12 navigation,
no unresolved reference links and no surviving Liquid tags.

**State after the primary pass**: 940 lines, 92 display equations, 234 references, 12,447 words.
Equations inside band. **References remain 16 short of the 250 floor and lines 360 short of the 1300
floor.** The reference gap will close in the publication review, which added 96 references to A307, but
**the line gap is larger than any article in this series has carried into a publication review** and the
contemporary work will have to be correspondingly substantial.

**Publication review performed per `_docs/process/PUBLICATION_REVIEW.md`. All checks run.**

**Contemporary coverage closed and the line gap with it.** A 66-query Crossref sweep returned 724 new
records, taking contemporary references from 59 to **189, or 55.3 percent of dated**, above the 101 to
155 range of A301 through A307. The sweep was aimed at the threads the equation and primary passes
opened, so the additions attach to the article's own derivations.

**The review made two findings that qualify the article's central claim, which is the most useful thing
it did.**

The first is that the range table compares the Atlas against a heavier version of itself, which is not
the comparison a designer in 1951 faced. Setting it against a conventional two-stage vehicle instead,
carrying the same propellant through the same loss calibration, puts the crossover near a **nine percent
structural fraction**, and conventional stages of the period achieved between eight and twelve. **The
balloon tank therefore made a single-and-a-half-stage vehicle competitive with a two-stage one rather
than making an intercontinental missile possible at all**, and a new section says so explicitly.

The second is that the sixty-seven-fold tensile-to-compressive asymmetry rests on a knockdown factor
chosen from a band of experimental scatter. Tabulating the sensitivity shows the qualitative claim
survives any reasonable choice, at between 27 and 89, while the specific figure does not. **It also
yields a consistency check the article can use**, since at a knockdown of 0.5 the reported five-pound
standing pressure would be insufficient, so that specification independently brackets the design factor
its engineers must have used to between about 0.15 and 0.4.

Nine subsections were added to the contemporary survey, on shell analysis methods and the probabilistic
turn, inflatable structure as the pressure-stabilised idea's second life, flaws and what a proof test
actually proves, modal survey, launch aerodynamics, materials characterisation, and the fate of a
pressurised tank left in orbit. Further new sections cover the designation question, what the X-11 was
worth as a testbed, what the ground could not reproduce, why the idea was available to Convair, and the
Atlas launcher lineage.

**Two defects found and fixed.** The leading citation construction reached 37.3 percent after the
contemporary rewrite and was rotated to **21.7 percent**. `vehicle` measured 7.98 per thousand body
words and was rotated to 6.86, with `article` brought below threshold; `pressure` at 7.28, `atlas` at
5.83, and `tank` at 5.05 are subject nouns and are left alone. A section placed after the Epistemic State
was moved back into genre order.

**Final verification**: 364 references with zero undefined, zero orphaned, and zero duplicate URLs. All
23 fixed identifiers at 200, one after a transient read timeout that resolved on retry. **All 322 DOIs
Crossref-resolved on title at the 0.85 threshold with zero flagged, and the article contains no
hand-entered identifier anywhere.** All 78 worked values re-derived and reproducing. `_verify.py` at the
0-error 21-warning corpus baseline. Zero contractions, em-dashes, en-dashes, prose colons, prose
semicolons, prose parentheticals, doubled words, duplicate headings, display-math seam defects, or lone
dollar-delimited lines. Isolated build succeeding with 97 rendered display blocks, Part 12 navigation,
four tables, no unresolved reference links and no surviving Liquid tags.

**Final state: 1302 lines, 97 display equations, 364 references, 18,837 words. All three densities are
inside band and nothing was trimmed at any point.** That is the third article in the series to finish
that way, after A306 and A307, and it required the largest single publication-review expansion the series
has performed, since the article entered the pass 360 lines below the floor.

Primary sources are 153 of 353 external, or 43.3 percent, having peaked at 68.6 percent before the
contemporary additions grew the denominator. The absolute count is unchanged.

**Committed and pushed. Not published.** All twelve articles in the series remain in `_drafts/`.

## X-Planes North American X-10 A307 2025-10-16

`x_planes_north_american_x10.markdown`, A307, editorial date 2025-10-16, series `x_planes` index 11 of 72.

943 lines, 84 display equations, 213 reference definitions, 14,346 words after the draft pass.
All three densities sit under band, at 943 against a 1300 floor, 84 against 90, and 213 against 250.
Reported rather than padded, since the equation-density and reference-density passes exist to close
exactly this gap, and the draft was deliberately approached from below per the rule A306 established.

**The keystone is time rather than speed, which is a first for this series.** The Navaho mission is
2.87 hours and the dominant navigation error grows with elapsed time rather than with distance or
speed. Inverting the reported 800 metre accuracy requirement gives a gyroscope drift specification of
0.0025 degrees per hour, and inverting the reported 1.6 kilometre per hour achieved drift gives 0.0144,
a shortfall of 5.74 that reproduces independently by propagating the achieved drift to full range.

**The central result is that the X-10 flew on the wrong side of a threshold nobody computed.** Schuler
tuning makes accelerometer error bounded at 1274 metres and gyroscope error secular, and the two are
equal at 47.8 minutes. The X-10's supersonic leg is 27.6 minutes. Worse than being the smaller term,
the two error signatures are 97.4 percent correlated over that window for a variance inflation of 19.7,
against exact orthogonality over one Schuler period, which is proved here by direct integration. A
window sweep puts the optimum at exactly 84.4 minutes, and flying the same leg subsonically would have
been more than ten times more informative.

**Further results the sources do not state**: the reported ranges cannot be reconciled with the
reported weights on any cruise condition, since the mass ratio of 1.640 gives 275 kilometres at maximum
Mach and the reported figures demand subsonic lift-to-drag ratios of 12.6 to 28.4; the radio horizon of
482 kilometres is less than half the navigation leg; the aluminium recovery-temperature frontier lies at
Mach 2.27 against a demonstrated maximum of 2.05; the vertical channel is unstable with a 6.6 minute
doubling time; deflection of the vertical alone consumes 77 percent of the accuracy requirement; and the
break-even inlet recovery to sustain Mach 2.05 is 0.622, which resolves the free-flight duct anomaly as
a model-scale artefact on the vehicle's own demonstrated performance.

**The error budget does not close and this is reported rather than reconciled.** The quadrature sum
exceeds the reported stellar-inertial accuracy by a factor of 3.3, and the deflection-of-the-vertical
term alone exceeds it. Three readings are offered and none adopted, the most likely being that the
demonstration was flown over surveyed range geometry rather than over the target country.

**Source base finding.** The vehicle is indexed under its project number MX-770 and not under X-10 or
Navaho, and queries on the designation return nothing while queries on the project number return the
primary documents immediately. The DTIC route that reached Bell's own project papers for the X-9
through the project number MX-776 returns nothing whatever for MX-770, which is the same archive, the
same route, and adjacent project numbers, so the negative result is about the record rather than the
method. Three documents in the accessible record concern the actual hardware.

**Verification**: all 102 worked values re-derived independently with no corrections required, which is
the second article running to pass first numeric verification clean. 213 references with zero undefined,
zero orphaned, and zero duplicate URLs. All 132 DOIs Crossref-resolved on title at the 0.85 threshold
with zero flagged and no hand-entered identifiers anywhere. 56 of 66 fixed identifiers at 200, the ten
failures being the unpublished series back-references, which is expected. `_verify.py` at the 0-error
21-warning corpus baseline. Zero contractions, em-dashes, en-dashes, prose colons, prose semicolons, or
prose parentheticals. Zero doubled words, zero display-math seam defects, zero duplicate headings, zero
link texts out of sync with the master table. Isolated build succeeding with 84 rendered display blocks
and Part 11 navigation.

**Correction made during the draft pass.** The article initially claimed the X-10 was the second of
three articles whose designation came from an administrative reorganisation. Checking A305 and A306
showed all three were RTV-A vehicles, the X-8 as RTV-A-1, the X-9 as RTV-A-4, and the X-10 as RTV-A-5.
The corrected claim is stronger, since three exceptions with one common origin are a pattern where three
with distinct origins would not be.

**Equation-density review performed on request.** Baseline 84 display equations across 13,382 body
words. The structural audit found no orphaned or duplicate subsections, unlike A306. 38 equations added
across 17 edits, taking the article from 943 lines and 84 equations to 1111 and 122, which is inside the
90 to 130 band. References rose 213 to 218, which is the equation pass creating reference debt exactly
as it did in A305 and A306, and the primary pass is aimed at it.

**The largest omission was the argument that killed the programme.** The article stated the
cruise-versus-ballistic exposure comparison qualitatively and never derived it. A minimum-energy
ballistic ellipse for the same 10,000 kilometres gives a burnout speed of 7193 metres per second, an
apogee of 1319 kilometres, and a free-flight time of 32.2 minutes against the cruise mission's 172, an
exposure ratio of 5.35. That number is the whole cancellation case and it is now on the page.

Other relations added: the drift specification is inversely proportional to range requirement, so
growing the mission from 500 to 5500 nautical miles tightened the gyroscope specification elevenfold;
two-system availability; static margin and the finding that a seven percent aerodynamic-centre shift
exceeds a three percent static margin outright; the drag decomposition showing base drag at half the
wave drag; the thrust-lapse relation; the skin thermal time constant of 48.6 seconds, which shows the
platform oven faces a step rather than a ramp; the linear drift-temperature model; the quadrature
variance shares, of which two attitude terms carry 94 percent; glide-slope sink rate and the
exponential flare; full-scale Reynolds number of 46.8 million against the free-flight models' 19 to 51
percent of it; dive-angle sensitivity of 48 metres per milliradian; and the modern gyroscope carried
through the article's own relation, which gives 957 metres over the mission and therefore **still does
not meet the 800 metre requirement on drift alone**.

**Equation-pass verification**: all 50 new worked values re-derived independently with no corrections,
and all 102 previously verified values still reproducing. Zero duplicate headings, zero display-math
seam defects, zero lone dollar-delimited lines, zero paragraph-repeated citations. 122 rendered display
blocks confirmed in the built HTML against 122 in the source.

**Two seam defects found by reading and not by any check.** The equation insertion into the
configuration subsection orphaned the canard citation list from the material it belonged to, leaving it
dangling after a base-drag conclusion, and the ballistic insertion left three consecutive
identically-introduced citations. Both repaired. This is the fifth article in which a seam defect
survived every automated check.

**A process error was found and corrected.** The citation-construction rotations performed during the
draft pass were applied to the scratch build copy rather than to the article, because a previous step
had left the shell inside the build directory and the edit script used a relative path. The
verification then read the same scratch copy and reported success, so the draft was committed with the
formulaic drift still present. The rotations have been re-applied to the article and the script now
uses an absolute path. The single-word construction share is 15.1 percent for `in` and 10.1 percent for
`is`, against 21.0 and 30.1 before.

**Primary-reference review performed on request.** Baseline measured 128 primary documents of 208
external, or **61.5 percent**, which was already the highest share in the series, so the deficit was
coverage and count rather than share. A citation-coverage audit by section found **fourteen sections
over 200 words at or below four citations per thousand**, and every one of them was a section the
equation pass had either created or expanded. That is the third article running in which the equation
pass arrived without its period sources, and the harvest was aimed at its topics rather than at the
article's original ones.

A supplementary harvest of 33 NTRS, 22 DTIC, and 16 period queries returned 129 new NTRS records, 181
new DTIC records, and 151 new period records, taking the master index from 1034 to 1448 entries. 53
primary documents were added across 21 edits, taking references from 218 to **271** and primary sources
to **181 of 239 research, or 75.7 percent, and 69.3 percent of external**. Both figures are by a
substantial margin the highest in the series, against A306 at 61.2 percent before its contemporary
additions grew the denominator.

**The strongest finding is that the article's central analytical move had no vocabulary in 1953.**
Identifiability as a property of a system rather than of an estimator was formalised by Aoki in 1966 and
by Staley and Yue in 1970, a decade and more after the programme ended, and the estimation machinery
that would have separated the two error terms is later still. The X-10 was asked to measure a parameter
at a time when the question of whether a parameter is measurable had not been posed as a question. That
is the fairest available account of why nobody noticed the observation window was the wrong length.

Other threads closed: circular error probable as a contested statistic rather than a given, including
what a bias does to it, which matters because a drift rate is a bias; the geodetic literature behind the
deflection-of-the-vertical term, together with the gravity-gradiometer aiding that eventually answered
it two decades too late; inlet and engine airflow matching, whose vocabulary postdates the X-10's inlet
design; radio propagation and range-height-angle charts behind the horizon calculation; what a test
range can actually measure, and the point that nothing in the accessible record states the Atlantic
Missile Range's own tracking error for these flights; the period ballistic-trajectory theory the
cancellation derivation rests on; and the redundancy and availability literature behind the reliability
arithmetic.

**Coverage after the pass is three thin sections against fourteen at baseline**, and all three are
synthesis sections that correctly carry no citations, namely the aircraft-category discussion, the
Epistemic State, and the Conclusion.

**Primary-pass verification**: 271 references with zero undefined, zero orphaned, and zero duplicate
URLs. **All 66 fixed identifiers at 200 and all 180 DOIs Crossref-resolved on title at the 0.85
threshold with zero flagged**, and the article still contains no hand-entered identifier anywhere. All
102 worked values still reproducing. `_verify.py` at the 0-error 21-warning corpus baseline. Zero
contractions, em-dashes, en-dashes, prose colons, prose semicolons, prose parentheticals, doubled words,
duplicate headings, display-math seam defects, or link texts out of sync. Isolated build succeeding with
122 rendered display blocks and Part 11 navigation.

**Two seam defects found by reading, not by any check.** The error-budget citation insertion split the
finding that the budget does not close from the three readings that resolve it, and the cancellation
insertion left a nine-item citation cluster inside the paragraph carrying the argument. Both repaired by
moving rather than rewriting. This is the sixth article in which a seam defect survived every automated
check.

**A durable repair was made to the toolchain.** The manual correction of a Crossref OCR artefact in an
author display had been applied to the master table directly and was silently lost when the table was
regenerated for the supplementary harvest. The correction now lives in the normaliser, so it survives
regeneration. The general form of the rule was already known, namely that reference-text defects belong
in the master table rather than the markdown, and the extension is that a table which is itself
regenerated is not a source of truth either.

**State after the primary pass**: 1181 lines, 122 display equations, 271 references, 16,090 words.
Equations and references are inside band. **Lines remain 119 short of the 1300 floor**, reported rather
than padded, and the contemporary-literature work of the publication review is expected to close it.
Contemporary coverage is 55 references, or 23.0 percent of dated, an absolute count well below the 101
to 155 of A301 through A306, and that is the publication review's principal task.

**Publication review performed per `_docs/process/PUBLICATION_REVIEW.md`. All checks run.**

**Contemporary coverage was the principal task and is closed.** A 64-query Crossref sweep returned 728
new records, taking contemporary references from 55 to **151, or 45.1 percent of dated**, which sits at
the top of the A301 through A306 range of 101 to 155. The sweep was aimed at the threads the equation
and primary passes opened rather than at the article's original topics, so the additions attach to the
article's own derivations.

**The strongest contemporary finding is that the article's central analytical move is now a named
discipline.** The distinction between structural and practical identifiability is exactly the X-10's
difficulty. Its drift rate was structurally identifiable and practically was not, and the window sweep
performed in the equation pass is an optimal-experiment-design calculation with one free variable. None
of that vocabulary existed in 1953, which means the programme is not open to the charge that it ignored
a known method, only to the observation that the method had not been invented.

Five subsections were added. Identifiability. Alignment and calibration. The landing gear, which is
where the fleet was actually lost and which turns out to have a larger current literature than the
guidance problem. Aerothermal analysis, which would have placed the aluminium frontier exactly.
Validation and the model-to-flight gap. Two further subsections were added on the exposure argument,
which has returned in the hypersonic glide vehicle literature, and on command links and latency. The
gravity section carries the pass's best inversion, that the term which defeated the Navaho is now used
as a navigation observation rather than suffered as an error.

**Two defects found and fixed.** NACA appeared in prose with no spell-out anywhere in the article, which
the acronym check caught. The Programme Origin section carried a paragraph merging the German
inheritance, the Snark comparison, and the three flying articles, which was split.

**Diction acted on.** `vehicle` measured 6.04 per thousand body words. Most uses are legitimate, since
the word carries a distinction the aircraft-category argument depends on, but sixteen cases where it
repeated inside a sentence or a short span were rotated across the X-10, the airframe, the article, the
machine, the aeroplane, and the missile, bringing it to **5.00**. `flight` measures 5.23 and is left
alone as the article's subject noun. No other content-independent word reaches 5.0. The apparent
`research` outlier at 21 per thousand is the citation-anchor artefact the handoff documents and is not
prose.

**Acronyms otherwise clean.** CEP appears only in mathematical notation and circular error probable is
spelled out at its first prose use. Every other flagged token is a model designation or programme brand
name, which the convention exempts.

**Structural conformance.** All twelve genre sections present and in order, with the three series-standard
extras and one article-specific section on the aircraft-category question. The Source Base precedes
Epistemic State. Zero duplicate headings.

**Final verification**: 367 references with zero undefined, zero orphaned, and zero duplicate URLs. All
66 fixed identifiers at 200, one of them after a transient read timeout that resolved on retry. **All 276
DOIs Crossref-resolved on title at the 0.85 threshold with zero flagged, and the article contains no
hand-entered identifier anywhere.** All 102 worked values re-derived and reproducing. `_verify.py` at the
0-error 21-warning corpus baseline. Zero contractions, em-dashes, en-dashes, prose colons, prose
semicolons, prose parentheticals, doubled words, display-math seam defects, lone dollar-delimited lines,
or link texts out of sync. Isolated build succeeding with 122 rendered display blocks, Part 11
navigation, both tables, the debug tag, no unresolved reference links and no surviving Liquid tags.

**A generator defect was found and fixed during the pass.** The master table held 105 duplicate URLs,
because a DOI can arrive through more than one harvest file. The DTIC prefix filter and the period date
filter return overlapping records and the two modern sweeps overlap as well. The cited set happened to
be clean, which was luck rather than method. The generator now deduplicates by URL. A consequence worth
recording is that **disambiguation suffixes are not stable across regenerations**, so an anchor must be
verified against its title and not only against its display before it is cited.

**Final state: 1329 lines, 122 display equations, 367 references, 18,323 words. All three densities are
inside band and nothing was trimmed at any point.** 1329 against 1300 to 1600, 122 against 90 to 130,
and 367 against 250 to 380. This is the second article in the series to finish that way, after A306, and
it was again produced by approaching the bands from below and letting the later passes fill.

Primary sources are 181 of 357 external, or 50.7 percent, having peaked at 69.3 percent before the
contemporary additions grew the denominator. The absolute count is unchanged.

**Committed and pushed. Not published.** All eleven articles in the series remain in `_drafts/`.

## X-Planes Bell X-9 Shrike A306 2025-10-15

`x_planes_bell_x9.markdown`, A306, editorial date 2025-10-15, series `x_planes` index 10 of 72.

1556 lines, 115 display equations, 342 reference definitions, 13,654 words after all four passes.
**Every density is inside band and no overage was argued for, which is a first for this series.**
Primary technical documents are 164 of 332 external references, or 49.4 percent, having peaked at 61.2
percent before the contemporary additions grew the denominator. Contemporary coverage is 110
references, or 36.2 percent of dated, an absolute count that sits with A301 through A304.

**The equation audit found a structural defect before it found an equation.** Counting equations per
section exposed four orphaned subsections at the end of The Contemporary Literature, three of them
duplicating headings the draft expansion had already written and one an unfilled stub. Writing the
miss-decay function down then exposed an error in the draft's own reasoning, since the assertion that
eight guidance time constants reduce an error by more than two orders of magnitude describes the bare
exponential and ignores a polynomial factor of 85, so the true residual is three percent.

**The X-9 is the first vehicle in the series whose keystone is a control loop rather than a physical
question, and whose specification is a probability.** The military characteristics of 15 July 1945
asked for a missile that would strike within 500 feet of its target 75 percent of the time, which
converts to an axis standard deviation of 91.5 metres and a circular error probable of 108 metres at
a hundred miles. Every subsystem is then specified in metres of miss distance, contributions add in
quadrature, and the design activity is the allocation of that budget.

The article's central technical claim is that **the two candidate guidance architectures have
opposite error gradients**. A radar resolves an angle, so its cross-range error is proportional to
range. Guiding from the launch aircraft therefore makes the error grow with the standoff distance
that is the entire purpose of the weapon, while guiding from the missile makes it shrink on approach.
Setting the launcher-guided resolution equal to the whole error budget gives a maximum useful range
near 72 kilometres against the X-9's demonstrated 80, which is a close enough correspondence to state
and too loose to press. It is also why the operational weapon was named for its guidance link, since
RASCAL stands for radar scanning link and the link carried a radar picture from the missile back to
an operator in the launch aircraft.

**The founding irony is datable.** The accuracy requirement was published on 15 July 1945, one day
before Trinity. Inverting the damage function shows that a nuclear warhead with a 1,500 metre lethal
radius needs a circular error probable of 823 metres for a 90 percent kill probability, against the
108 metres the specification demanded, so the requirement was about eight times tighter than the
weapon that flew actually needed.

Three further results the sources do not state. The missile's short-period frequency of 7.5 radians
per second against a human operator's maximum crossover of 2.6 means **the operator cannot be given
the control surfaces** and an inner autopilot loop is forced. A guidance time constant of 0.83 seconds
means every error still present within five kilometres of the target arrives at the target, which
reorganises the error budget so that only terminal errors matter. And a beacon on the missile beats
skin tracking by a factor near 10 to the 5, so **a one watt transmitter on the missile is worth more
than a hundred kilowatts on the aircraft**.

The source base is better than the X-8's and the reason is structural. A weapon programme reports to a
service that keeps its reports, and the Defense Technical Information Center holds Bell's own project
documents covering the Shrike and the RASCAL together. Primary technical documents are already **125
of 229 external references, or 54.6 percent**, at the draft stage. Contemporary coverage is 46 of 201
dated references, or 22.9 percent, and is the clearest deficit for the later passes.

Verification: all 62 worked values re-derived independently from their stated inputs with no
corrections required, 239 references with zero undefined, zero orphaned, and zero duplicate URLs, all
70 fixed identifiers at 200, all 124 DOIs Crossref-resolved on title at the 0.85 threshold with zero
flagged, `_verify.py` at the 0-error 21-warning corpus baseline, zero style violations, zero doubled
words, zero display-math seam defects, isolated build succeeding with 88 rendered display blocks and
Part 10 navigation. Reading the seams found two insertions that had split an argument from its
conclusion and orphaned a citation from its subject, both repaired.

No author key was guessed from a document title in this article, because the anchor index was resolved
from metadata before drafting rather than after. That is the first article in the series where the
rule cost nothing to follow.

Equation-density, primary-reference, and publication reviews not yet performed.

## X-Planes Aerojet X-8 Aerobee A305 2025-10-14

`x_planes_aerojet_x8.markdown`, A305, editorial date 2025-10-14, series `x_planes` index 9 of 72.

2226 lines, 200 display equations, 474 reference definitions, 20,352 words after all four passes.
Contemporary references are 155 of 410 dated, or **37.8 percent**, an absolute count above every
earlier article in the series and appropriate to an article half again their length. Primary technical documents are **216 of 420 external
references, or 51.4 percent**, up from 155 and 43.2 percent, and comparable to A298 at 52.1 percent
after its own pass. **The Defense Technical Information Center proved reachable by digital object
identifier under a single Crossref publisher prefix**, which the draft had described as largely not
publicly indexed, and the finding changes the article's conclusion about its own source base rather
than decorating it. The single best result is the research and development report on the Navy
Aerobee-Hi, which is the closest thing in the accessible record to a programme document for this
family. References are inside band. **Equations at 200 are the highest in the series, above
the A297 opener at 147 and well over the 130 ceiling, and lines exceed the 1600 ceiling by 407.** Both
are deliberate. Every equation added in the second pass is a relation the prose names, relies on, or
whose product it quotes, so the rule that produces the number was followed rather than the number
targeted.

**The equation review found arithmetic errors the draft pass had carried as quoted figures.** The
thrust coefficients given as 1.55 in vacuum and 1.36 at sea level compute to 1.624 and 1.409, and the
theoretical characteristic velocity given as 1,570 metres per second computes to 1,505. Writing the
relations down rather than quoting the numbers is what exposed both, which is the entire case for this
pass. The corrected chain carries an independent check the original did not, since the recovered
chamber pressure of 2.16 megapascals reproduces the separately reported vacuum thrust of 4,728 pounds
to within one pound.

The stability analysis was completed so that it predicts what the flight record attributes to it. The
draft appealed to a failure mode the analysis predicted without having written the equation of motion.
Adding it gives a damping ratio of 0.0033 and 33 cycles to halve an oscillation, so **an unguided
finned rocket does not damp its pitch motion aerodynamically in any useful sense**, and a divergence
time constant of 0.86 seconds, so the 24 November 1947 flight that yawed for 35 seconds ran for forty
time constants. Deriving the wind weighting the draft had only named gives **a seven kilometre impact
displacement from a ten metre per second wind**, and the torque-free coning relation gives a **64
degree cone** from a residual transverse rate of a tenth of a radian per second, which is the
strongest support for the claim that the era's science was pointing-limited rather than
altitude-limited.

**This is the first article in the series whose subject is not an aircraft**, and the keystone
follows from that. Every previous X-vehicle was the object of its own measurement. The X-1 was
instrumented to find out what happened to the X-1, and even the expendable X-7 was flying to
characterise the ramjet underneath it. The X-8 is the first X-vehicle whose own performance is not
what is being measured. It is apparatus rather than subject, and the requirement that follows is
transparency, meaning that every way in which the carrier might perturb somebody else's measurement
becomes a design constraint.

The central relation is that observing time above burnout altitude is exactly twice the burnout
velocity divided by gravity, which combined with the rocket equation gives observing time as the
exhaust velocity times the log of the mass ratio divided by half g. With the Aerobee's propellants
the coefficient is 400 seconds per factor of e in mass ratio. **Observing time is logarithmic in the
quantity a programme actually pays for**, which is the quantitative reason a sounding-rocket
programme buys precision by flying often rather than by flying high, and it is the article's answer
to why a five-minute flight was enough to discover Scorpius X-1.

Required altitude is set by optical depth rather than by ambition, and the article computes it for
three cases. Solar Lyman-alpha becomes observable at 80 kilometres, soft X-radiation at 110, and the
ozone layer is opaque by a factor of e to the 92 so its profile is obtained by watching the sun while
climbing through it. The X-8's 116 kilometres is the smallest altitude clearing all three, and the
fact that it barely clears the third is why X-ray astronomy waited for a larger vehicle.

**The published performance figures are not internally self-consistent, and the article says so.** A
staged reconstruction reproduces the reported burnout velocity of 1,347 metres per second to within 2
percent but leaves only 26 metres per second for drag, against an independent drag-loss estimate of 60
to 150. One or more of the booster inert mass, the sustainer burn time, and the specific impulse is
off by a few percent and the record does not say which. The reconstruction's sustainer stage mass of
498 kilogrammes independently matches the separately reported 1,100 pounds, which is what makes the
rest of it credible.

Three results the sources do not state. Roll rate from canted fins and pitch natural frequency are
both linear in velocity, so velocity cancels from their ratio and it varies as the inverse square root
of density, meaning **a vehicle below roll resonance crosses it at a definite altitude regardless of
how fast it is going**. Blowing the fins off to induce tumbling cuts the ballistic coefficient by a
factor of 63 and therefore the parachute opening load by the same factor, which is the whole
justification for a technique that looks like damage. And a single 35 millimetre frame carries three
orders of magnitude more information than the entire telemetry budget of the flight, which is why the
parachute failures on the first five Air Force flights destroyed the science rather than degrading it.

The archival situation is the reverse of the X-6. That article's record lives in the Department of
Energy archive and a standard aerospace search returns nothing. Here a search of that same archive
returns nothing relevant at all, which was verified rather than assumed, and the record lives in the
NASA archive instead. A sweep of 569 records from it returned 41 published in the 1950s against 161 in
the 1960s, so the Aerobee 150 and 350 are far better documented than the X-8 itself.

**Twenty author keys guessed from document titles during drafting were all wrong**, and a further 23
guessed during the citation pass were caught before that pass ran. Reading the reference list rather
than running a check found three mis-citations that every automated check passed, being two
disambiguation-tag pairs assigned to the wrong member of the pair and one citation resolving to an
unrelated paper. A link-text invariant now enforces that every prose citation text equals the
master-table display for its anchor.

Verification: all 89 worked values re-derived independently with two corrections, being a
signal-to-noise ratio inflated 10 percent by a rounding carried through the link budget and a skin
temperature stated 14 kelvin low. One flagged value turned out to be the check rather than the article
being wrong. 370 references with zero undefined, zero orphaned, and zero duplicate URLs, all 147 fixed
identifiers at 200, all 170 DOIs Crossref-resolved on title at a 0.85 threshold with zero flagged,
`_verify.py` at the 0-error 21-warning corpus baseline, zero style violations, zero doubled words,
zero display-math seam defects, isolated build succeeding with 136 rendered display blocks and Part 9
navigation.

Contemporary coverage was raised on the draft pass rather than left for the publication review,
because the draft closed at 11.4 percent of dated references and the directive governs every pass. 87
journal articles were added, taking contemporary references from 25 to 112 and to 36.6 percent, an
absolute count consistent with A301 at 101, A302 at 109, A303 at 105, and A304 at 107.

Equation-density and primary-reference reviews not yet performed.

## X-Planes Lockheed X-7 A304 2025-10-13

`x_planes_lockheed_x7.markdown`, A304, editorial date 2025-10-13, series `x_planes` index 8 of 72.

1395 lines, 94 display equations, 358 reference definitions, 17,330 words after all four passes.
**All three densities are inside band.**

The primary deficit was the largest in the series and was closed by the third pass, taking primary
technical documents from 49 to 109. Dilution by the publication review leaves them at 30.4 percent of
all references, matching A301 at 30.1, with references dated 1965 or earlier at 42.5 percent of dated
references.

The publication review added 45 contemporary journal articles, taking contemporary references from 62
to **107 and from 28.1 to 40.2 percent of dated references**. The absolute count matches A302 at 109
and A303 at 105. The percentage is higher because this article carries fewer dated references overall,
and it is above the 28 to 33 percent range the earlier articles settled at, which is deliberate under
the standing directive. Contemporary references are 38.8 percent of
dated references and references dated 1965 or earlier are 35.6 percent.

**The pass corrected a claim the draft asserted without computing.** The draft said a staged conical
shock system recovers "something like half" the total pressure against a tenth for a normal shock, "a
factor of five." Carrying out the oblique shock arithmetic gives 0.397 for two sixteen-degree turns
followed by a normal shock, against 0.107 for a normal shock alone, which is **a factor of 3.7 rather
than five**. The correction is in the article with the three component recoveries shown.

Three results the draft did not have. Specific impulse at Mach 4.31 works out to 1850 seconds against
250 to 450 for a chemical rocket, so the ramjet delivers four to seven times the specific impulse of
the rocket that starts it, which is the entire reason for the architecture. The subsonic-combustion
ceiling can be located rather than gestured at, since thrust vanishes when stagnation temperature
reaches the combustor limit, giving a limiting Mach number of 6.2. The Damköhler number, the ratio of
residence time to chemical time, is 8.3 for a one millisecond chemistry and 0.83 for ten, so a ramjet
combustor operates within a factor of a few of not working at all.

Two economic and statistical relations were added that the keystone rests on. The Wright learning
curve gives a cumulative average of 0.41 at an eighty-five percent progress ratio, so 130 vehicles
cost about 53 times one vehicle rather than 130 times. The stopping rule that separates a crewed from
an expendable programme was written as an expected-cost balance, in which the vehicle cost term
becomes effectively unbounded when it includes a human life, which is why the X-7's advantage cannot
be recovered by making a crewed aircraft cheaper.

**The keystone is epistemic rather than performance-related, and it is the first in the series that
is.** Every previous article concerns an aircraft that had to come back. A crewed programme approaches
a destructive limit and stops short of it, so its estimate of that limit is an extrapolation whose
prediction variance grows as the square of the margin kept. An expendable programme crosses the limit
and interpolates. For twenty observations, predicting one data span beyond the centroid costs a
factor of 3.6 in standard error against predicting at the centroid.

The physics falls out of the engine. A ramjet's compression ratio is 1 at rest, 7.8 at Mach 2, and
152 at Mach 4, so it is worthless standing still and unmatched at speed, which is why the vehicle
must be thrown. The booster delivers 1.87 million newton seconds and a velocity increment near 575
metres per second, taking the vehicle from a release Mach number of 0.45 to a burnout Mach number of
2.37, which is precisely where the engine becomes worth having, at 13 g rising to 16. A single normal
shock at Mach 4.31 keeps only 10.7 percent of the total pressure, against roughly half for a staged
conical shock system, which is why the nose spike exists. Recovery temperature at Mach 4.31 and 32
kilometres is 985 kelvin, or 712 degrees, which excludes aluminium and specifies steel, and the same
stagnation temperature leaves only 922 kelvin of useful combustion temperature rise against 1600 at
Mach 2, which is the ceiling on the subsonic-combustion ramjet.

**A method failure was caught by verification and is worth recording.** In assembling the contemporary
set I hand-constructed nineteen plausible-looking DOIs rather than taking them from the harvest
records. Crossref resolution showed that most pointed at entirely unrelated papers, including a paper
on dendrite deformation and one on alcohol licensing policy. All were discarded and the contemporary
set was rebuilt from actual harvest records. **Never construct an identifier that can be looked up.**

Verification complete. All 252 references cited with zero undefined, zero orphaned, and zero duplicate
URLs, all 125 meaningful-404 URLs swept at 200, all 58 DOIs Crossref-resolved on author and title, all
70 NTRS records verified individually, `_verify.py` clean at the 0-error 21-warning corpus baseline,
zero contractions, em-dashes, en-dashes, prose colons, prose semicolons, or prose parentheticals, zero
doubled words, zero display-math seam defects, isolated build succeeding with Part 8 navigation and
zero unresolved anchors.

Independent re-derivation of all 28 worked values found two errors, a residence time rounded from 8.3
to 8 milliseconds and an extrapolation figure whose wording described a different calculation from the
one performed. Both corrected.

**Publication order dependency now eight deep.** A304 cites A303, A302, A301, A300, A299, A298, and
A297.

## X-Planes Convair X-6 A303 2025-10-12

`x_planes_convair_x6.markdown`, A303, editorial date 2025-10-12, series `x_planes` index 7 of 72.

1487 lines, 92 display equations, 404 reference definitions, 18,375 words after all four passes.
Lines and equations are inside band. Primary technical documents number 156 at 38.6 percent of all
references, comparable to A302 at 39.1 percent, and references dated 1965 or earlier are 53.9 percent
of dated references, the series high by a wide margin and the expected shape for a programme whose
entire technical life fell inside fifteen years.

The publication review added 46 contemporary journal articles, taking contemporary references from 59
to **105 and from 23.5 to 35.4 percent of dated references**, comparable to A301 at 35.8 percent.

**References at 404 exceed the genre band's ceiling of 380 by 24, and that is deliberate.** The
standing directive states no reference limit and asks that the articles serve as a comprehensive
survey of the contemporary literature. Reported rather than trimmed.

**The equation pass replaced an assumed attenuation factor with a derived one, and the numbers got
worse.** The draft assumed a ten-million-fold attenuation. Deriving the gamma source from the fission
rate gives an unshielded dose rate of 9.8 grays per second at ten metres, when about five grays is a
lethal whole-body dose, so one second of exposure would kill the crew. Holding them to fifty
millisieverts across a hundred-hour flight demands an attenuation of 7.1 times ten to the seventh,
which is 25.7 centimetres of lead rather than 23.2, and a gamma shield of 41 tonnes rather than 37.
That is 22 percent of gross weight and 106 percent of the B-36 maximum bomb load. A separate
lithium hydride neutron layer of 2.2 metres and 24.5 tonnes takes the upper bound to 66 tonnes, or 35
percent of gross and 1.7 times the payload.

**The pass also found a validation the draft did not have.** Applying the same derivation chain to the
one megawatt ASTR in the NB-36H at fifteen metres gives 18.7 centimetres of lead and 12.7 tonnes for
a six square metre bulkhead, and 16.4 centimetres and 11.2 tonnes under the far more permissive
occupational allowance of the 1950s. The reported crew shield was eleven to twelve tonnes. The two
estimates bracket it, so the method used throughout the article reproduces the one aircraft in it
that actually flew.

**The first article in the series about an aircraft that was never built, and the class judgement went
the other way from the obvious one.** The genre document reserves a documentation-poor class at 150
to 400 lines and 20 to 60 references for thin cases. The X-6 is the opposite. The Aircraft Nuclear
Propulsion programme ran fifteen years, spent about a billion dollars, and left a primary record
larger than that of most flown aircraft in this series. It is treated at full length.

**The primary record is not in the NASA archive, and that is a structural finding.** ANP was an
Atomic Energy Commission and Air Force programme, so its reports went to the AEC and are held today
by the Department of Energy, discoverable through the Office of Scientific and Technical Information.
A standard NTRS search for this aircraft returns almost nothing and the standard conclusion, that the
record is thin, is exactly wrong. This article introduces OSTI as a source archive for the series, and
71 of its 287 references are OSTI records against 14 from NTRS.

The keystone is whether the mass of shielding a reactor requires can be carried by an aircraft that
still has a reason to fly. The derivation gives about 100 megawatts of thermal power for a B-36-class
cruise, consuming 0.44 kilograms of uranium-235 in a hundred hours against 837 tonnes of kerosene for
the same energy, a ratio of nearly two million. Against that stands the shield derived above.
Minimizing shield mass plus fuselage structure over the reactor-to-crew separation gives an interior
optimum at 10.1 metres, which a 49 metre B-36 fuselage accommodates easily and which is the geometry
the NB-36H actually used.

Two consequences follow from the exponential and are the article's contribution. Shield thickness
depends on the logarithm of reactor power, so a thousandfold power increase costs under nine
centimetres of lead, which makes the shield a fixed overhead rather than a proportional cost and
excludes small nuclear aircraft entirely rather than merely making them hard. The same logarithm
means accepting ten times the crew dose saves about two percent of the aircraft, so the programme
could not have been rescued by being braver.

The durable output was a reactor rather than an aircraft. The Aircraft Reactor Experiment ran at Oak
Ridge in 1954 as the world's first molten salt reactor, and that concept is under active commercial
development seventy years later while the aircraft remains unbuilt.

Verification complete. All 287 references cited with zero undefined, zero orphaned, and zero
duplicate URLs, all 177 meaningful-404 URLs swept at 200 across three archives, all 74 OSTI records
and 12 NTRS records verified individually, all 51 DOIs Crossref-resolved on author and title,
`_verify.py` clean at the 0-error 21-warning corpus baseline, zero contractions, em-dashes, en-dashes,
prose colons, prose semicolons, or prose parentheticals, zero doubled words, zero display-math seam
defects, isolated build succeeding with Part 7 navigation and zero unresolved anchors.

One arithmetic error was found by independent re-derivation and corrected, a decay-heat energy
integral stated as 58 gigajoules that computes to 73.

**Publication order dependency now seven deep.** A303 cites A302, A301, A300, A299, A298, and A297.

## X-Planes Bell X-5 A302 2025-10-11

`x_planes_bell_x5.markdown`, A302, editorial date 2025-10-11, series `x_planes` index 6 of 72.

1657 lines, 112 display equations, 466 reference definitions, 22,299 words after all four passes. **NTRS-hosted primary documents rose from 94 to 182, or 44.8
percent of all references, which is by a wide margin the highest in the series against 30 to 33
percent for A298 through A301.** References dated 1960 or earlier rose from 70 to 102, or 34.5
percent of dated references, second only to A298 and A301.

The publication review added 60 contemporary journal articles, taking contemporary references from
49 to **109 and from 16.6 to 30.6 percent of dated references**, which is inside the 28 to 33 percent
target range and is the highest absolute contemporary count in the series against A301's 101.

**Two densities sit outside the genre bands and both are deliberate.** References at 466 exceed the
380 ceiling by 86, and lines at 1657 exceed the 1600 ceiling by 57. The standing directive for this
series states no length limit and no reference limit and asks that the articles serve as a
comprehensive survey of the contemporary literature, which is what produced both overages. They are
reported rather than trimmed and the pilot can call for a cut.

The equation pass produced three results the draft did not have. The Korn drag-divergence relation,
evaluated with the streamwise thickness ratios that sweeping produces, returns 0.765 at the low sweep
setting and 0.916 at the middle one against a maximum flight Mach number of about 0.9, which
establishes that the aircraft could not have reached its top speed unswept. Sweeping was the
performance rather than a refinement of it. Induced drag and the spin-recovery inertia parameter were
shown to degrade by the identical factor of 2.61, because both carry the span squared in a
denominator and the sweep lever is a span lever, so one geometric fact produces a performance cost
and a safety cost of exactly the same size. Sweep was given a control derivative in the same form as
an elevator's, returning minus 0.26 per radian against a conventional elevator's minus 0.7, which
makes the gull result quantitative. Sweep is worth roughly a third of an elevator as a pitch
effector, and the obstacle to using it that way is entirely rate, since matching a five degree
elevator input inside one short-period time constant would require 42 degrees per second against the
X-5's 1.33, a factor of thirty-one.

The keystone is whether wing sweep can be a variable rather than a choice. The answer turns on one
line of geometry, since a pivoting panel carries its aerodynamic centre with it and the streamwise
travel is the panel arm times the change in the sine of the sweep angle.

The central results are derived from the X-5's own published dimensions rather than quoted. Solving
the two-span relation recovers a pivot station of 0.953 metres, or 18.7 percent of the semi-span, and
a movable panel length of 4.42 metres. The aerodynamic centre therefore travels 0.93 metres between
the sweep extremes, which is 58 percent of the mean chord and four to eleven times the entire static
margin of a conventional aeroplane. Bell absorbed it with a jackscrew and rails that translated the
wing forward as it swept aft, partially. Langley later found that an outboard pivot with a fixed
inboard glove shrinks the same travel by the product of two factors and needs no mechanism, which is
the finding that put variable sweep into the F-111 and its successors.

The accident result is the article's strongest contribution. The NACA spin-recovery correlating
parameter carries the square of the span in its denominator, and sweeping the X-5's wing shortens the
span from 10.21 to 6.32 metres, so the parameter degrades by a factor of 2.61 with no change in mass
distribution at all. The second aircraft was lost in a spin at the sweep setting where that factor is
worst. The factor is arithmetic and the attribution is labelled as inference in Epistemic State.

One inequality made the aircraft flyable. Sweep took thirty seconds and the short period took two, so
the geometry change was fifteen times slower than the dynamics it perturbed and the pilot met a drift
rather than a step. Much of the contemporary morphing literature concerns the case where that margin
does not exist.

Verification complete. All 318 references cited with zero undefined and zero orphaned and zero
duplicate URLs, all 182 meaningful-404 URLs swept at 200, all 44 DOIs resolved through Crossref and
compared on author and title, all 86 selected NTRS identifiers verified individually, `_verify.py`
clean at the 0-error 21-warning corpus baseline, zero contractions, em-dashes, en-dashes, prose
colons, prose semicolons, or prose parentheticals, zero doubled words, zero malformed links, genre
section order conforming, isolated build succeeding with Part 6 navigation and zero unresolved
anchors.

The reference section is generated from the anchors the body actually uses, so orphaned definitions
are impossible by construction and dangling anchors fail an assertion. This is the direct answer to
the defect A300 and A301 both shipped.

**Publication order dependency now six deep.** A302 cites A301, A300, A299, A298, and A297.

## X-Planes Northrop X-4 Bantam A301 2025-10-10

`x_planes_northrop_x4.markdown`, A301, editorial date 2025-10-10, series `x_planes` index 5 of 72.

1391 lines, 98 display equations, 372 reference definitions, 18,358 words after four passes. All
three densities are inside band. The publication review added 32 contemporary journal articles
harvested from Crossref under a 2019 date filter and verified individually against Crossref on author
and title, taking contemporary references from 69 to 101 and from 27.6 to 35.8 percent of dated
references. That is above the 28 to 33 percent range A297 through A300 settled at, and it is
deliberate under the standing directive that these articles serve as a comprehensive survey of the
contemporary literature. The absolute contemporary count of 101 is the highest in the series. NTRS
primary documents hold at 112, and references dated 1960 or earlier at 38.3 percent of dated
references, so the primary base established by the previous pass was diluted but not displaced.

The keystone is whether a horizontal tail can be dispensed with at transonic speed. A tail does two
jobs and the historical debate was conducted about the wrong one, since the damping contribution
scales as the square of tail length and supplies 94 percent of a conventional aircraft's pitch
damping. The X-4's short-period damping ratio computes to 0.244 against 0.749 for a tailed aircraft,
both stable, so the finding is about margin rather than stability. The tailless aircraft becomes
effectively undamped once its damping falls to 21 percent of nominal where the tailed one tolerates 7
percent. The answer expired rather than being overturned, since a pitch damper restores by feedback
what the missing tail removed.

The primary-reference pass produced three substantive changes beyond citation count. A criterion
contemporaneous with the aircraft was located, so the handling-qualities closure no longer rests only
on criteria postdating the programme by two decades. The Oswald efficiency factor used in the
induced-drag argument is now anchored to the 1932 report that defined it. A second research role the
article had omitted entirely was recovered, in which the split flap speed brakes were opened to spoil
the lift-to-drag ratio deliberately and generate low-ratio approach data for future rocket-powered
aircraft, a thread running through Matranga and Menard 1959 to the same author's analysis of the
first thirty X-15 landings and onward to gliding re-entry practice.

The publication review found and corrected two mathematical defects. The wing pitch damping
expression returned minus 0.007 for the article's own inputs while the same line asserted an order of
minus one and every subsequent number used minus 0.8, an inconsistency of two orders of magnitude.
The passage now separates a parallel-axis term evaluated at minus 0.02 from the wing's own unsteady
chordwise term of order unity, which is where the minus 0.8 comes from, and labels the latter as
adopted rather than derived. A split-drag yaw expression divided by unity, the third instance of that
malformation in the series. The diction check found `aircraft` at 12.37 uses per thousand words
against a sibling range of 5.31 to 8.30, and a rotation across design, layout, configuration, case,
and the designation itself brought it to 9.07.

Verification complete. All 372 references cited with zero undefined and zero orphaned, zero duplicate
URLs, all 182 meaningful-404 URLs swept at 200, all 99 DOIs resolved through Crossref and compared on
author and title, `_verify.py` clean at the 0-error 21-warning corpus baseline, zero contractions,
em-dashes, en-dashes, prose colons, prose semicolons, or prose parentheticals, zero doubled words,
zero malformed links, zero display-math seam defects, genre section order conforming, and the
isolated build succeeding with Part 5 navigation and zero unresolved anchors in the rendered page. A
display-equation seam defect introduced by the equation pass, in which the induced-drag ratio had
prose glued to the same line, was repaired in the primary-reference pass.

**Publication order dependency now five deep.** A301 cites A300, A299, A298, and A297.

## X-Planes Douglas X-3 Stiletto A300 2025-10-09

`x_planes_douglas_x3.markdown`, A300, editorial date 2025-10-09, series `x_planes` index 4 of 72.

1415 lines, 114 display equations, 365 reference definitions, 15,583 words after equation-density,
primary-reference, and publication reviews. All three inside band. Primary 54.3 percent, contemporary
28.9 percent. The first added 28 equations across 12 edits and
closed a substantive omission on inlet spillage drag. The second added 40 NASA and NACA primaries
from sixty the harvests had returned unused, raising primary sources from 44.1 to 50.9 percent.
The publication review then raised contemporary coverage from 21.6 to 28.9 percent with 24 curated
journal articles and rotated 22 formulaic citation constructions, the article having carried the
worst such repetition of the four at 70 percent. **Committed and pushed, not published.**

The article where the keystone framework fails hardest. The sizing does not close, which is the
finding. A thirty percent engine shortfall compounds with a fixed inlet recovering only 0.721 of
total pressure at Mach 2, halving available thrust and predicting Mach 1.42 against a design 2.0. The
aircraft managed 1.21. Separately, a pitch-to-roll inertia ratio of 37.2 against the X-2's 7.5 puts
the critical roll rate at 45 degrees per second, an ordinary control input, and the load factor
increment at 4.3 rather than 11.7, which is why the X-3 survived its departures and the X-2 did not.

Verification complete. All 34 worked examples re-derived, all 301 references cited with zero
undefined and zero orphaned, all 165 meaningful-404 URLs swept at 200, `_verify.py` clean, zero style
violations, isolated build succeeding.

**Publication order dependency now four deep.** A300 cites A299, A298, and A297.

## X-Planes Bell X-2 A299 2025-10-08

`x_planes_bell_x2.markdown`, A299, editorial date 2025-10-08, series `x_planes` index 3 of 72.

1497 lines, 126 display equations, 370 reference definitions, 17,743 words, all three inside band
after equation-density, primary-reference, and publication reviews. The first added 29 equations across 12 edits.
The second added 56 NASA and NACA primaries resolved to fixed NTRS identifiers, raising primary
sources from 42.2 to 52.0 percent of external references and closing four arguments the index did not
support. The publication review then raised contemporary coverage from 25.2 to 33.0 percent with 27
curated journal articles and corrected a section-order drift. Primary sources 55.6 percent and
contemporary coverage 33.0 percent are both the highest of the three articles. **Committed and
pushed, not published.**

The keystone is aerodynamic heating, with the binding constraint being time at temperature rather
than temperature. Two findings carry the article. Dynamic pressure at the fatal condition was 39.2
kilopascals, higher than the X-15 at Mach 6.7, so the accident was not a thin-air failure but a
lift-curve-slope failure. And the divergence is derived rather than asserted, giving a 0.45 second
e-folding time and 1.5 seconds from a one degree disturbance to thirty degrees.

Verification complete. All 41 worked examples re-derived with four corrections. All 287 references
cited with zero undefined and zero orphaned, all 149 meaningful-404 URLs swept at 200, `_verify.py`
clean, zero style violations, zero duplicated seams, isolated build succeeding.

**Publication order dependency is now three deep.** A299 cites A298 and A297, and A298 cites A297.

## X-Planes Bell X-1 A298 2025-10-07

`x_planes_bell_x1.markdown`, A298, editorial date 2025-10-07, series `x_planes` index 2 of 72. The
first per-aircraft article, using the twelve-section research-aircraft order.

1387 lines, 108 display equations, 337 reference definitions, 17,565 words. Drafted at 1095 lines, 80
equations, and 259 references, then taken through equation-density and primary-reference reviews. The
first added 28 equations across 17 edits. The second added 55 NASA and NACA primaries resolved to
fixed NTRS identifiers, raising primary sources from 37.1 to 48.5 percent of external references and
bringing the line count inside the 1300 to 1600 band with content rather than padding. A publication
review then raised contemporary coverage from 18.2 to 26.3 percent with 23 curated journal articles,
rotated 26 formulaic citation constructions, and confirmed structural conformance. Primary sources
are 52.1 percent of external references. **Committed and pushed, not published.**
The review exposed one arithmetic error in the drafted text, an axial acceleration stated as 1.6 that
computes to 1.25. The genre document full-aircraft equation band was raised from 60-to-80 to 90-to-130
to record what the series actually does. The line count remains about 90 below band and has
deliberately not been padded.

Verification complete. All 75 worked examples re-derived independently across both rounds, with two
corrections and four precision tightenings, and zero duplicated clauses at edit seams. All 259 references cited with zero undefined and zero orphaned. All 142
meaningful-404 URLs swept at 200. `_verify.py` clean, zero style violations, acronyms spelled out
before first use, isolated build succeeding with series navigation and the A297 cross-link resolving.

**Publication order dependency.** A298 cites A297 through `post_url`, so publishing A298 while A297
remains a draft fails the entire site build. They publish together or A297 first.

## X-Planes Series Opener A297 2025-10-06

`x_planes_framing.markdown`, A297, editorial date 2025-10-06, series `x_planes` index 1 of 72. The
first article of a seventy-two-article back-dated series running 2025-10-06 through 2025-12-16, one
per day unbroken, ending flush against the 2025-12-17 post. Held for human-pilot review before A298
is drafted.

1765 lines, 147 display equations, 421 reference definitions, 21,933 words, against History of SpaceX
medians of 1345 lines, 72 equations, and 306 references. The article was drafted at 76 equations, at
parity, and then took a requested equation-density pass that found 19 results named or relied upon in
prose but never displayed, adding 71 equations across 44 edits. The genre document gained a
series-opener row to match, since an opener carries the shared derivations the seventy-one
per-aircraft articles reference rather than repeat.

A subsequent primary-reference pass measured the index at 42 primary sources of 327, or 13.5 percent,
against an article that claims the NACA and NASA report series as its backbone. Primary sources are
now 87 of 372, or 24.5 percent. 22 existing NASA citations were upgraded from search endpoints to
fixed NTRS document identifiers resolved through the citations API, all 63 of which were swept at
200, and 11 journal primaries were resolved through Crossref with an author match required. Six
results that the prose named without citing at all were corrected.

The publication review then found three acronym violations, namely NACA spelled out long after first
use, NASA never spelled out at all, and DARPA expanded after its first occurrence, all fixed. It also
found that only 10.2 percent of dated references were 2010 or later with one from the 2020s, against
a directive that these articles survey the contemporary literature. A `## The Contemporary Literature`
section with eight subsections was added, along with 49 contemporary references harvested from
Crossref under a 2015 date filter and from the NTRS API. Contemporary coverage is now 28.8 percent
and primary sources 33.7 percent. **Committed and pushed, not published.** 109 Open Library book
citations still point at search endpoints. The genre is the research-aircraft hybrid
defined in `_docs/writing/RESEARCH_AIRCRAFT_STRUCTURE.md`, and the opener establishes the analytical
model plus the sizing relations that the per-aircraft articles reference rather than repeat.

Verification is complete. All 34 worked numerical examples re-derived independently and agreeing.
All 327 anchors cited in the body with zero undefined and zero orphaned. All 159 Wikipedia citations
swept, with five wrong titles corrected. All 11 digital object identifiers resolved through Crossref
and compared on author and title, of which two were defective and were repaired, one nonexistent and
one resolving to an unrelated paper. `_verify.py` clean, zero style violations, isolated production
build succeeding with every `post_url` resolved.

Two items are outstanding. Categories remain the agent's assumption at `aerospace history
engineering`, which fixes the URL permanently at publication across all seventy-two articles. And
109 Open Library plus 27 NASA Technical Reports Server citations point at search endpoints that
return 200 for any query, so the sweep does not confirm their targets exist. The article states that
limitation in its own Epistemic State rather than letting the reference count imply more rigour than
it has.

## Wire Formats Mini-Series 2026-01-27 and 2026-01-28

Two release-candidate drafts written to fill the only interior gap remaining in the 2026 calendar,
a two-day slot between the WebAssembly-on-Jekyll post at 2026-01-26 and the constant-AMM-mathematics
post at 2026-01-29.

- `wire_formats_what_they_are.markdown`, A295, 2026-01-27, 203 lines, 5 display equations.
  Defines the wire-format class through three membership properties and walks three families that
  are usually treated separately, namely data interchange encodings, protocol framing, and
  instruction encodings.
- `wire_formats_implementation_tradeoffs.markdown`, A296, 2026-01-28, 215 lines, 6 display
  equations. Takes nine tradeoffs that cut across all three families and treats each as a choice
  with no correct answer, closing on the combinations that are mutually contradictory.

Both are analytical essays with the genre's Epistemic State and Out of Scope sections. Every
external URL was checked, and each cited RFC was confirmed by title rather than by response code.
Part two back-references part one, which is legal because 2026-01-27 precedes 2026-01-28; part one
makes no forward reference. Both dates have passed, so batch publication resolves the internal
cross-reference immediately.

## Series-Wide Consistency Pass 2026-08-04

All twelve History of SpaceX articles A281 through A292, published and drafted, were audited together for equation density, reference density, publication suitability, crosslinks, and link validity. Front matter and crosslinks were already fully consistent. Equation density needed no change at 64 to 78 with median 72. A284 was the sole reference-density outlier at 49 primary references and was raised to 68. A285 was the sole structural outlier at 4 H3 subsections and received five Historiographical Gap subsections. Five prose style violations were repaired across A281, A282, and A284.

A citation-integrity audit of all 109 DOI-bearing anchors found twelve fabricated citations and nineteen unregistered DOIs, all repaired, plus five citations removed because the claimed work could not be confirmed to exist. A full sweep of all 853 unique URLs found 84 dead links, all repaired. Final state across all twelve is zero missing, unused, or duplicate anchors, zero duplicate bullets, zero duplicate URLs, all reference blocks alphabetical, and zero style violations.

Outstanding from this pass: 20 of the 43 Open Library replacement URLs are confirmed at 200 and 23 could not be checked because openlibrary.org hard-blocked this address after the 853-URL sweep, with a retest at 30-second spacing failing to recover. The status check is close to meaningless for this host in any case, because an Open Library search URL is a search endpoint that cannot return 404 for a query. The substantive weakness is that a search URL is a weaker citation than an edition page, which applies equally to the 269 such URLs the series already carried, and resolving them to specific work identifiers is worth a dedicated pass. It is not link rot and does not block publication.


## Pathological Word-Usage Pass 2026-08-04

All twelve articles were analyzed for word frequency against a 40-post baseline from the non-SpaceX corpus. The dominant pathology was "specific" at 87.17 per thousand words against a baseline of 1.73, a factor of 44, with 16,230 occurrences of which 12,260 were the bare filler "the specific". It was reduced series-wide to 44 occurrences at 0.20 per thousand, below natural baseline, with technical terms and genuine contrastive uses preserved. Three further tics were toned down: the equation-introduction formula, which accounted for 429 of 488 introductions, was varied across nine alternatives; "supplies" fell from 1.73 to 0.53 per thousand; and "configuration" was retained as domain vocabulary while its 191 within-sentence repeats were varied. All twelve articles verify clean afterward on anchors, LaTeX, equation counts, grammar, and style.

## Draft Status

**Batch published 2026-08-04.** A288 through A292 were published at editorial dates 2026-07-31 through 2026-08-04, all at 09:00 UTC, via the two-commit publication sequence pushed to origin/master. Build verification passed before push with 294 posts in and 294 HTML files out, zero Liquid errors, and every `post_url` in the corpus resolving. **The History of SpaceX series is complete at twelve articles A281 through A292.** No further article in the series is planned. All twelve are now in `_posts/` and none remains in `_drafts/`.

### History of SpaceX Synthesis and Projection article (A292) — Drafted (publication-review parity, series complete)

**Files**:
- `_drafts/spacex_history_synthesis_and_projection.markdown` (A292, twelfth and closing article of the History of SpaceX series, series `spacex_history`, series_index 12 of 12, editorial date 2026-08-04 09:00 UTC)

**Topic**: Closing article of the twelve-article series, with three tasks. The retrospective task restates the seven forcing-function conditions and three capital-formation legs and records what each component article established. The critical task is the article's principal contribution and argues that the framework's independence assumption fails. Across three independent articles written for unrelated purposes the series encountered the same structural surprise: A288 found a portfolio that appears to distribute risk concentrates it on a shared vehicle family, A290 found sub-properties that appear to fail independently fail together under adverse states, and A291 found a leg that appears to remove a constraint substitutes a different one. The article treats this as a property of the framework rather than a coincidence and states the correction, that the conditions are approximately separable in favorable states and correlated in adverse ones. It then shows the assumption biases the assessment in opposite directions. Positive dependence in favorable states means the conjunction is more attainable than the product of marginals implies, so the singular-conjunction thesis overstates rarity and the correct reading is that a smaller number of underlying properties generates most of the ten conditions. Correlation in adverse states means the configuration is more fragile than the product implies, so satisfying nine of ten is not ninety percent of the way to the configuration. Both inequalities hold simultaneously and concern different questions. The article takes up the two cross-condition interactions A288 recorded, finding the key-person dependency perfectly correlated across all lines so the portfolio supplies zero mitigation, and finding conditions six and seven interact adversely because the concentration that protects the mission from capital capture is what makes a key-person event maximally consequential. The projective task extends to 2050 with assumptions enumerated and failure modes ranked rather than listed, concluding structurally that the configuration is not a steady state but a transitional arrangement, so every projection to 2050 is a projection about what replaces it. Treats the Anduril, OpenAI, Palantir, and Blue Origin templates and the Standard Oil, Bell Labs, foundation-ownership, Ford, and early-aircraft precedents. Closes with eight open questions for the series as a whole.

**Article Numbers**: A292
**Completion**: Complete. All four passes done. At publication-review parity with A288 through A291. This is the final article of the series and all twelve are now written. Awaits publication authorization as part of the five-article interlocked batch.
**Publication Sensibility**: High on content. A sequencing constraint applies. The article back-references A288 through A291 by `post_url` and all four are unpublished, so the publication batch is now five articles that publish together or in strict order.
**Status**: Draft 2026-08-04, with equation-density expansion pass the same day adding 57 display equations (14 to 71) to bring the absolute count into the series band. The pass matched the per-section distribution of A290 and A291 at parity and preserved zero-equation status in the six sections that carry none in any sibling. The closer's equations are unusual in the series because they formalize claims about the framework rather than about the case. The factor representation phi_k equals h_k of theta with dim theta below ten is the central device and carries the argument in four sections. The covariance decomposition under a factor structure establishes why conditions sharing a loading cannot be independent. The paired inequalities showing joint attainment above the product of marginals and joint survival below it are stated together so their compatibility is visible. The shared-shock indicator model gives the mechanism producing correlated failure. The reproduction-probability contrast between q to the tenth under independence and q to the fourth under the factor reading is the article's most consequential practical implication. The succession-partition array shows that each available resolution surrenders a different condition and that no row preserves all ten. The failure-mode ranking criterion combining event probability with the fraction of the configuration removed makes the ordering auditable rather than asserted. A primary-reference expansion pass then added 124 primary reference URLs (26 to 150) at the claims a citation audit found uncited. The audit found only four of twenty-six sections carrying any primary source at all, which is the expected shape for a synthesis and is nonetheless a publication defect. The pass added a Primary Source Documentation Across the Series H3 subsection enumerating the four evidentiary layers the whole series rests on, namely the regulatory layer which is complete and authoritative, the government-contracting layer which is substantially complete, the securities and corporate layer which establishes the legal framework and almost nothing about particular transactions, and the reconstruction layer which supplies substantially every quantitative claim and is the weakest. Placements attached the vehicle, award, regulatory, corporate-law, and reconstruction records to each of the ten conditions in the framework restatement, supplied the falsifying data series for each projection so the projections are falsifiable in practice rather than only in principle, attached the foundation-ownership statutes and the listing regime to the succession partition, and attached the grounding precedents and risk-transfer instruments to the failure-mode ranking. The Data Sources section now states the series' central evidentiary asymmetry bluntly: claims about what the government bought on what instrument are checkable by any reader, and claims about what private investors paid on what terms are not supported at all. A publication-review expansion pass then added a new Falsifiability of the Framework H2 developing the article's own identified weak point, a new Cross-Disciplinary Framings Across the Series H2 collecting the traditions the eleven component articles surveyed, eight Historiographical Gap subsections, three analytical framings, and two historical precedent cases. The falsifiability section confronts the degrees-of-freedom objection the closer had raised in a single sentence, namely that a ten-condition scheme constructed from a surviving case and applied retrospectively to failures will locate a fault in any case whatever. It separates the three claims that survive the critique, comprising the independence finding which is falsifiable and was falsified from within the exercise, the capital-formation mechanics whose objects are instruments rather than outcomes and are checkable without reference to any venture's success, and the negative result on ownership form which compares institutional forms against a stated criterion. It concedes that the central conjunctive thesis does not survive in predictive form, states the prospective scoring test that would settle it, and notes that no such test has been performed for this framework or for any alternative the literature offers. The cross-disciplinary section records which traditions earned their place, finding that the transaction-cost, entrepreneurial-finance, and corporate-control traditions supplied the durable findings because their objects are instruments and ownership forms, while the strategy and capability traditions supplied vocabulary and little that could be checked. A DOI verification pass preceded the expansion, checking all 38 DOI-bearing candidates against Crossref with the nineteen previously identified fabricated or unregistered anchors blacklisted from the selection set. 1,508 lines, ~18,092 words, 75 display equations, 29 H2 sections, 18 H3 subsections, 109 book references, 150 primary reference URLs, 91 research references, 20 related-post cross-references, 370 total reference anchors with zero missing, zero unused, and zero duplicate anchors and zero duplicate URLs. Zero em-dashes, en-dashes, prose contractions, prose parentheticals, prose colons, or prose semicolons outside math. All LaTeX balanced and every macro verified against the MathJax `tex-mml-chtml` default package set. Categories `history business aerospace`. Debug tags on lines 13-14. Equation density now in band at 71, comparable to A290 at 77 and A291 at 78. Reference density at 370 total anchors, the highest in the series against A290 at 331 and A291 at 326, with all four categories in the sibling range and primary references at 150 the series high. Every anchor was drawn from the A290 and A291 apparatus, which are the two fully verified and repaired articles in the series, and the nineteen anchors identified as fabricated or unregistered in the citation-integrity audit were excluded from the source pool. All 26 primary URLs rechecked with zero 404 responses. Forward references are absent, since no further article in this series is planned.

### History of SpaceX Category-Dominating Commercial Spinoff article (A291) — Drafted (publication-review parity)

**Files**:
- `_drafts/spacex_history_category_dominating_spinoff.markdown` (A291, eleventh article of the History of SpaceX series, series `spacex_history`, series_index 11 of 12, editorial date 2026-08-03 09:00 UTC)

**Topic**: Eleventh article in the History of SpaceX series and the third and last of the capital-formation legs. Organizing claim is that the category-dominating commercial spinoff is not a diversification into an adjacent market but the internalization of an anchor customer, so that where A283 treats a government customer buying launches this article treats the venture becoming the customer it had previously needed someone else to be. The decisive economic property is that the spinoff consumes the parent's output at marginal cost while every competitor attempting the same business must pay a market price the parent sets, giving a per-launch disadvantage equal to the parent's entire margin and an aggregate disadvantage scaling linearly in campaign size. Article walks the January 2015 Seattle announcement and the surplus-capacity argument the article treats as the stronger of the two stated rationales, the deployment sequence from the May 2019 first operational batch through the 2020 service beta and the 2021 commercial rollout, the vertical integration and the internal transfer price that redistributes profit between segments without changing the total, the launch-cadence coupling in which the constellation raises cumulative flight count and thereby lowers its own launch cost through the learning relationship, the subscriber and revenue trajectory with the segment mix shifting toward higher-value maritime aviation enterprise and government lines, the direct-to-cell extension and its carrier partnerships, the capital intensity and the replenishment treadmill that converts the constellation from a capital asset into a consumable, the regulatory position across the Federal Communications Commission the International Telecommunication Union and national regulators, spectrum priority as the genuinely scarce asset, and the orbital congestion externality. Identifies spectrum priority under the first-filed and bring-into-use regime as the point at which the capital-formation story and the regulatory story become the same story, since captive launch capacity is the mechanism by which a regulatory option is exercised before it expires. Negation and comparison cases are Iridium and Globalstar, which attempted the business without captive launch, OneWeb, and the Amazon programme, which the article treats as the informative comparison because it holds capital scale high and captive input absent. Pattern extraction states five sub-properties and records that the arrangement converts a capital asset into a consumable, so the venture obtains not an annuity but a business that must rebuild itself continuously.

**Article Numbers**: A291
**Completion**: Complete. All four passes done. At publication-review parity with A288, A289, and A290. Awaits publication authorization as part of the four-article interlocked batch.
**Publication Sensibility**: High on content. A sequencing constraint applies. The article back-references A288, A289, and A290 by `post_url` and all three are unpublished, so the publication batch is now four articles that publish together or in strict order.
**Status**: Draft 2026-08-03, with equation-density expansion pass the same day adding 49 display equations (26 to 75) to bring the absolute count into the series band. The pass matched the per-section distribution of A290 at parity rather than applying a uniform ratio, and preserved zero-equation status in the six sections that carry none in any sibling. Additions concentrated in Cross-Disciplinary Framings (0 to 8), the Economic Property section (5 to 7), the Launch-Cadence Coupling (3 to 5), Vertical Integration (1 to 4), and Capital Intensity (2 to 4), and supplied first equations to Alternative Analytical Frameworks (4), Deep Historical Comparative Precedents (3), the Regulatory Position (2), and the Iridium and Globalstar precedents (2). Several additions carry new analytical content rather than restating adjacent prose. The make-or-buy condition is restated as supply unavailability rather than cost comparison, establishing that the integration would have been correct even had it been more expensive than buying, which is not the case the transaction-cost literature ordinarily treats. The average-cost relation shows the spinoff lowers the cost at which the parent serves external customers as a by-product of serving itself, which is the reverse of the resource diversion the diversification literature predicts and is the strongest single piece of evidence that the arrangement is not a diversification. The two-sided-market test shows consumer broadband fails the cross-side externality condition because additional subscribers degrade shared-cell service, so importing platform conclusions into it is an error. The latency ratio shows the low-orbit configuration moves the service across an application threshold rather than improving along an existing dimension, which explains the geostationary incumbents' non-response. The bring-into-use condition is restated as a rate requirement, and the filing option is shown to collapse to zero on failure rather than degrading, which is the formal core of the spectrum-priority finding. The steady-state fleet age result establishes that the treadmill keeps the deployed constellation permanently averaging half a design lifetime, a favorable property rarely stated. A primary-reference expansion pass then added 59 primary reference URLs (68 to 127) at the claims a citation audit found uncited. The audit measured primary-reference density per section and found seven sections carrying none at all, comprising the Mapping Problem, the Economic Property section, Cross-Disciplinary Framings, Capital Intensity and the Replenishment Treadmill, Comparative Cross-Sectional Analysis, Data Sources, and Alternative Analytical Frameworks. Placements put the segment-reporting standard behind the transfer-price argument, the launch-site tenancy and range-licensing record behind the fixed-cost claim, the Commercial Space Launch Act chain and Part 450 licensing rule behind the regulatory and spectrum-priority sections, the orbital-debris mitigation regime behind the short-lifetime design choice, the liability and insurance instruments behind the congestion externality, the mission architecture statements behind the January 2015 rationale, and the corporate-law instruments behind the capacity-allocation conflict. Two placements carry new argument. The debris regime is shown to make the short satellite lifetime partly a compliance cost rather than purely a commercial design choice, so the replenishment burden this article treats as a liability is in part the price of the mitigation practice the same article credits. The liability and insurance instruments are shown not to price the marginal congestion an additional satellite imposes, because each responds to a realized loss rather than to an increment in risk, so the externality survives the existence of an active insurance market. Three dead inherited URLs were dropped rather than replaced by guesswork and two anchors sharing a Starship page were consolidated. A publication-review expansion pass then added a new Constraint the Spinoff Installs H2 section developing the article's own identified weak point, eleven cross-disciplinary traditions, five historical precedent cases, seven Historiographical Gap subsections, five analytical framings, and an expanded contemporary landscape. The new section corrects the mapping-problem claim that the spinoff leg terminates the capital-formation problem, arguing that retained earnings carry no financial claim but do carry an operational one through service obligations, carrier counterparties, and per-jurisdiction regulatory dependencies, none of which holds equity and none of which appears in the capital-formation accounting the series developed. The governance configuration A287 describes is shown to be exact against capital capture and entirely absent against these parties, since their leverage is independent of any equity position. The section also records that this is the third instance of a series-wide pattern in which the framework's decomposition understates coupling between conditions, after the A288 shared-vehicle-family concentration and the A290 adverse-state sub-property correlation, and directs A292 to treat it as a general property rather than three coincidences. A DOI verification pass preceded the survey expansion and excluded one anchor whose registered metadata names a different book. A full sweep of all 179 book and research URLs, the first run on this article, found 20 dead links which were all repaired before commit, twelve by adopting the repaired Open Library versions the sibling drafts already carry, one by a new verified Open Library search URL, six further inherited publisher pages the same way, and two research links repointed at verified DOI targets. One of those repairs corrected a conflated citation in which the Adilov Alexander and Cunningham anchor claimed a 2014 paper's title under a 2018 date; the anchor was renamed and repointed at the verified 2014 DOI, and the same conflation in the published siblings is logged as citation-integrity debt. 1,425 lines, ~18,955 words, 78 display equations, 29 H2 sections, 19 H3 subsections, 101 book references, 127 primary reference URLs, 78 research references, 20 related-post cross-references, 326 total reference anchors with zero missing, zero unused, and zero duplicate anchors and zero duplicate URLs. Zero em-dashes, en-dashes, prose contractions, prose parentheticals, prose colons, or prose semicolons outside math. All LaTeX balanced and every macro verified against the MathJax `tex-mml-chtml` default package set. Categories `history business aerospace`. Debug tags on lines 13-14. Equation density now in band at 75, matching A290 at 77. Reference density at 326 total anchors, at parity with A290 at 331, with all four categories in the sibling range. Every reference anchor was drawn from the verified sibling corpus and rechecked before use, following the citation-integrity audit recorded in TASKLOG. Five dead URLs inherited from the corpus were replaced with verified pages and one anchor with an unregistered DOI was excluded rather than shipped. Forward reference to A292 is plain prose rather than a `post_url` link, per the back-reference-only convention.

### History of SpaceX Anchor Demand article (A283) — Published

**Files**:
- `_posts/2026-07-26-spacex_history_anchor_demand.markdown` (A283, third article of the History of SpaceX series, series `spacex_history`, series_index 3 of 12)

**Topic**: Third article in the History of SpaceX series treating the anchor-demand forcing-function condition. Article walks the SpaceX anchor-demand trajectory through the 2008 near-death moment following three consecutive Falcon 1 launch failures, the December 23 2008 CRS-1 salvation with the 1.6 billion dollar Commercial Resupply Services contract, the Cargo Resupply Services execution across the CRS-1 and CRS-2 rounds, the Commercial Crew Program across the September 16 2014 CCtCap award through the May 30 2020 Demo-2 first commercial crewed flight, the Human Landing System Artemis Program across the April 16 2021 Option A award through the May 19 2023 Blue Origin sustaining second-provider award, the Starshield defense-service line launched in December 2022, and the parallel Space Force National Security Space Launch certification progression through Phase 1A, Phase 2, and Phase 3 Lane 2. Article closes with pattern-extraction section stating the abstract anchor-demand mechanic requires joint satisfaction of five sub-properties: identifiable anchor customer, incentive-compatible payment structure, multi-year sustainment, technical-standard-setting, and anchor-portfolio diversification.

**Article Numbers**: A283 (with A284 currently drafted at initial-draft state and A285 through A292 planned in subsequent sessions)
**Completion**: 100% Published as standalone on 2026-07-25 at editorial date 2026-07-26 with 09:00 UTC publication time via two-commit sequence pushed to origin/master (staging commit `11caa98` followed by publication commit with git mv from `_drafts/` to `_posts/` with date prefix and process file sync)
**Publication Sensibility**: High (comprehensive literature-survey article at publication-review parity with A281 and A282; editorial date 2026-07-26 verified free of collision with published corpus)
**Status**: Published 2026-07-25 after with equation-density expansion pass (8 to 60 display equations), reference-density expansion pass (97 to 190 total anchors), and comprehensive publication-review expansion pass (190 to 232 total anchors, adding two new H2 sections and expanding Cross-Disciplinary Framings, Deep Historical Comparative Precedents, Historiographical Gap, and Alternative Analytical Frameworks sections). 1,100 lines, ~15,332 words, 66 display equations, 21 H2 sections, 82 book references, 49 research references, 90 primary reference URLs, 11 related-post cross-references, 232 total reference anchors with zero missing/unused/duplicated. Zero em-dashes/en-dashes/prose contractions/prose parentheticals outside math notation. Categories `history business aerospace`. Debug tags on lines 13-14. Front matter `series: spacex_history, series_title: History of SpaceX, series_index: 3`. Publication time 09:00 UTC per new series-wide convention. All 11 post_url cross-references to existing published corpus verified including back-references to A281 series opener and A282 Value Gradient article.

### History of SpaceX Patient-Private Capital-Formation Leg article (A290) — Drafted (publication-review parity)

**Files**:
- `_drafts/spacex_history_patient_private_leg.markdown` (A290, tenth article of the History of SpaceX series, series `spacex_history`, series_index 10 of 12, editorial date 2026-08-02 09:00 UTC)

**Topic**: Tenth article in the History of SpaceX series and the second of three capital-formation legs. Organizing claim is that patience is not a temperament investors possess but a structural property instruments manufacture. The binding constraint is the fund-life clock, which obliges a fund to return capital to its limited partners on a schedule unrelated to any portfolio company's development horizon, and which operates through three distinct channels comprising the contractual term, the realization-triggered carried interest, and the distributed-capital metric on which the successor fundraise depends. Article walks the duration mismatch, the August 2008 Founders Fund entry, the 2009 Draper Fisher Jurvetson entry after the CRS-1 award had functioned as a third-party credit enhancement, the January 2015 Google and Fidelity round that shifted the investor base toward vehicles with no fund life, the round and valuation sequence, the semi-annual tender-offer mechanism treated as the decisive structural innovation because it renders realization independent of company exit, investor-base composition and horizon heterogeneity, and dilution management. Negation cases are Iridium, whose debt claim converted a delay into a default, and OneWeb, whose nominally patient equity investor withdrew and where the absence of a secondary market made a single withdrawal terminal. Article treats the contemporary defense-technology venture wave and the Anduril and Palantir comparisons, and finds the secondary-market condition available to few ventures. Pattern extraction states five sub-properties and records that the mechanism supplies patience in good states and none in bad ones, which is the opposite of what the word ordinarily connotes.

**Article Numbers**: A290
**Completion**: Complete. All four passes done. At publication-review parity with A288 and A289. Awaits publication authorization as part of the three-article interlocked batch.
**Publication Sensibility**: High on content. A sequencing constraint applies. The article back-references A288 and A289 by `post_url` and both are unpublished, so A290 must publish with them or after them.
**Status**: Draft 2026-08-02, with equation-density expansion pass the same day adding 41 display equations (30 to 71) to bring the absolute count into the 60-72 series band. The pass matched the per-section equation distribution of A289 rather than applying a uniform ratio, preserving zero-equation status in the six sections that carry none in any sibling, namely Methodological Commitments, Historiographical Gap, Data Sources, Cross-References, Terminological Note, and Load-Bearing Open Questions. Additions concentrated in Cross-Disciplinary Framings (2 to 8), the Fund-Life Constraint (3 to 6), the Economic Property section (5 to 7), and the Tender-Offer Mechanism (2 to 5), and supplied first equations to Deep Historical Comparative Precedents (3), Contemporary Comparative Landscape (2), and Alternative Analytical Frameworks (4). Several additions carry new analytical content rather than restating prose. The binding-clock identification shows the reputational channel binds at three to four years against the ten-year contractual term. The minimum-over-holders form establishes that the earliest remaining vehicle term governs rather than the weighted average, which is what makes the tender mechanism necessary rather than merely convenient. The remaining-life form establishes that the duration condition is evaluated continuously rather than once at entry, so an arrangement adequate at one date requires replacement at another. The carry present-value form shows the constraint is discounting rather than mere deferral. The state-dependence identity states the good-state asymmetry formally and establishes that the mechanism is not a hedge. A subsequent equation-density review audited for unformalized load-bearing claims and added three more (71 to 74), comprising the implied post-money valuation arithmetic for the January 2015 round, the tender recurrence interval as a bound on the realization wait, and an explicit closure matrix in the cross-sectional section marking inapplicable and unestablished cells separately rather than imputing them. A primary-reference expansion pass then added 81 primary reference URLs (53 to 134) at the claims a citation audit found uncited. The audit measured primary-reference density per section and found six sections carrying none at all, comprising the Economic Property section, Cross-Disciplinary Framings, the January 2015 round, Dilution Management, Deep Historical Comparative Precedents, and Alternative Analytical Frameworks. Additions were drawn from the verified sibling corpus rather than invented, with every URL rechecked before use. The pass placed the Delaware and adviser-regulation apparatus behind the fund-structure claims, the listing-standard and index-methodology sources behind the listing-choice discussion, the NBER business-cycle chronology behind the 2008 distress claim, the SpaceX vehicle and programme record behind the milestone sequence against which each round priced, the Seattle constellation announcement behind the January 2015 round that underwrote a business line not yet in existence, the bankruptcy-court and operator records behind both negation cases, the Standard Oil and AT and T primary records behind the historical precedents, the foundation-ownership statutes behind the durable-ownership comparison, and the federal award databases behind the defense-technology wave. Three new passages were added rather than only citations, comprising a legal-apparatus paragraph establishing that every element of the fund-life constraint is locatable in a statute or convention and none is a property of capital, a disclosure-asymmetry paragraph observing that the mechanism manufacturing patience simultaneously withdraws the transactions from public view, and a comparative-institutional paragraph establishing that the finding is jurisdiction-bound because United Kingdom pre-emption, German codetermination, and the European Union Shareholder Rights Directive each alter the control calculus. A new Comparative Contemporary Configurations H3 subsection marks the boundary between the fund-life problem this article treats and the control-allocation problem the commentary conflates with it. Three dead NASA URLs inherited from the corpus were replaced with verified programme pages rather than guessed slugs, and one duplicate-URL anchor was consolidated. A publication-review expansion pass then added a new Adverse-State Financing Regime H2 section developing the article's own identified weak point, seven cross-disciplinary traditions, five historical precedent cases, five Historiographical Gap subsections, five analytical framings, and an expanded contemporary landscape. The new section argues that the adverse-state instrument set moves the supplying claim toward a fixed prioritized position, so the claim-type sub-property is state-contingent rather than a fixed property of equity, and that three of the five sub-properties therefore fail together on a common cause, which means the conjunctive product form overstates joint survival and should be read as a diagnostic checklist rather than a probability model. A citation-integrity audit run during the pass removed six anchors that failed DOI verification before they shipped and surfaced thirteen further fabricated citations across the published siblings, recorded in TASKLOG for human-pilot decision. 1,439 lines, ~23,301 words, 77 display equations, 28 H2 sections, 16 H3 subsections, 106 book references, 134 primary reference URLs, 72 research references, 19 related-post cross-references, 331 total reference anchors with zero missing, zero unused, and zero duplicate anchors and zero duplicate URLs. Zero em-dashes, en-dashes, prose contractions, prose parentheticals, prose colons, or prose semicolons outside math. All LaTeX balanced at 64 matched `\left` and `\right` pairs with balanced braces, and every macro used verified against the MathJax `tex-mml-chtml` default package set. Categories `history business aerospace`. Debug tags on lines 13-14. Equation density now in band at 71. Reference density at 157 against the 190-234 baseline remains outstanding. Forward references to A291 and A292 are plain prose rather than `post_url` links, per the back-reference-only convention. This is the weakest evidentiary position in the series, because the transactions were private placements between private parties and neither side has a disclosure obligation. Prose added by this pass was written at ordinary phrasing density rather than matching the article's elevated "the specific" usage, which is scheduled for a separate series-wide remediation pass.

### History of SpaceX Government-Anchor Capital-Formation Leg article (A289) — Drafted (publication-review parity)

**Files**:
- `_drafts/spacex_history_government_anchor_leg.markdown` (A289, ninth article of the History of SpaceX series, series `spacex_history`, series_index 9 of 12, editorial date 2026-08-01 09:00 UTC)

**Topic**: Ninth article in the History of SpaceX series and the first of the three capital-formation legs. Article's organizing distinction is between anchor demand, which the A283 article treats and which concerns a customer buying an output, and government-anchor capital formation, which concerns the mechanism by which the government relationship supplied capital to build a capability before any output existed and supplied it non-dilutively. Article walks the Space Act Agreement instrument and its consequences from proceeding outside the Federal Acquisition Regulation, the COTS round-one awards of August 2006, the Rocketplane Kistler termination of 2007 in which the failed milestone was a financing milestone rather than a technical one, the milestone mechanics and the non-dilutive property that constitutes the analytical core, the December 2008 Commercial Resupply Services transition at which the channel ceased supplying capital and began supplying revenue, the Commercial Crew progression through the September 2014 CCtCap awards, the Boeing comparison demonstrating the risk transfer a fixed-price instrument accomplishes, the National Security Space Launch certification progression, the litigation that opened the defense channel, and the Starshield reversal in which the firm now invests ahead of the government requirement. Article treats SBIR Phase III sole-source authority as the closest statutory analogue and argues the leg transfers position rather than money. Article contrasts against the cost-plus counterfactual and records the mechanism-design result that optimal incentive power falls with uncertainty, which is in direct tension with the policy lesson usually drawn from the COTS case.

**Article Numbers**: A289
**Completion**: 100% drafted at publication-review parity with the published series articles. Awaits human pilot review and publication authorization.
**Publication Sensibility**: High on content. One sequencing constraint applies. The article back-references A288 by `post_url`, and A288 is unpublished, so A289 must publish with A288 or after it.
**Status**: Draft 2026-08-02, with equation-density and primary-reference expansion passes the same day. Equation pass added 44 display equations (26 to 70). Primary-reference pass added 30 primary reference URLs (91 to 121) at the claims a citation audit found uncited, principally the COTS round-one award amounts, the round-two re-competition, the Dragon and Commercial Crew flight record, the Boeing Starliner programme record, the launch-infrastructure arrangements, and the international liability framework. Publication-review expansion pass then added a new Agency-Side Capability Requirement H2 section arguing the instrument is not a substitute for a capable agency, seven cross-disciplinary traditions, three historical precedent cases, four Historiographical Gap subsections, four analytical framings, and an expanded contemporary landscape, closing the book and research gap the primary-reference pass had identified. 1,392 lines, ~20,136 words, 73 display equations, 28 H2 sections, 15 H3 subsections, 123 book references, 130 primary reference URLs, 69 research references, 19 related-post cross-references, 341 total reference anchors with zero missing, zero unused, and zero duplicate anchors and zero duplicate URLs. Zero em-dashes, en-dashes, prose contractions, prose parentheticals, prose colons, or prose semicolons outside math. All LaTeX balanced. Categories `history business aerospace`. Debug tags on lines 13-14. Equation density at 73 and reference density at 341 anchors, both above the series baselines, with primary references at 130 the highest in the series and the book and research categories brought from the series lows of 50 and 43 to 123 and 69. Repaired 9 broken links inherited from the sibling corpus and consolidated 7 duplicate-URL anchors across the three passes. Repaired 4 dead NASA URLs and dropped one NTRS accession number that could not be confirmed to be the document the title claimed. Forward references to A290 through A292 are plain prose rather than `post_url` links, per the back-reference-only convention. Cross-links to the SBIR series A132, A138, and A140 resolve.

### History of SpaceX Portfolio Patience article (A288) — Drafted (publication-review parity)

**Files**:
- `_drafts/spacex_history_portfolio_patience.markdown` (A288, eighth article of the History of SpaceX series, series `spacex_history`, series_index 8 of 12, editorial date 2026-07-31 09:00 UTC)

**Topic**: Eighth article in the History of SpaceX series treating the portfolio-patience forcing-function condition, the seventh and last of the forcing-function conditions. Article develops the distinction between diversifying return variance, which the finance literature evaluates, and reducing ruin probability, which is what a mission-directed venture actually requires, and it argues the two objectives recommend different portfolios. Article walks the five-line portfolio comprising launch service, spacecraft, constellation, defense services, and the next-generation vehicle, then treats the cross-subsidization structure and the internal capital market that directs it. Article foregrounds the qualification that four of five lines depend on a single launch vehicle family, so the portfolio supplies almost no protection against the most likely catastrophic operational event, and it identifies the surviving Starlink subscription revenue under a grounding scenario as the offsetting feature. Article engages the conglomerate-discount objection in a dedicated section, conceding two of the three standard explanations and answering the third through the generated-versus-assembled portfolio distinction. Negation cases are Iridium, the Superconducting Super Collider, and the contemporary OneWeb and Virgin Orbit failures. Pattern-extraction section states five sub-properties and identifies generation from a shared capability base as the hardest.

**Article Numbers**: A288
**Completion**: 100% drafted at publication-review parity with the published series articles. Awaits human pilot review and publication authorization.
**Publication Sensibility**: High. No publication blocker. All fifteen `post_url` targets resolve because A284 through A287 published on 2026-08-02, so this article can publish standalone.
**Status**: Draft 2026-08-02, with equation-density, primary-reference, and publication-review expansion passes the same day. Equation pass added 36 display equations (33 to 69). Primary-reference pass added 63 primary reference URLs (44 to 107) at the claims a citation audit found uncited, together with a new passage treating launch insurance and the statutory liability regime as complements to rather than substitutes for the portfolio. Publication-review pass added a new Attention-Allocation Constraint H2 section developing the Penrose managerial-services constraint and the bounded-rationality attention limit as the resources that bind before capital does, five cross-disciplinary traditions, four historical precedent cases including the Manhattan Project parallel-track programme as the purest instance of a portfolio held under irreducible technical uncertainty, three Historiographical Gap subsections, four analytical framings, and an expanded contemporary landscape. Final metrics 1,438 lines, ~22,832 words, 75 display equations, 28 H2 sections, 15 H3 subsections, 116 book references, 108 primary reference URLs, 110 research references, 15 related-post cross-references, 349 total reference anchors with zero missing, zero unused, and zero duplicate anchors. Zero em-dashes, en-dashes, prose contractions, prose parentheticals, prose colons, or prose semicolons outside math. All LaTeX balanced. Categories `history business aerospace`. Debug tags on lines 13-14. Equation density at 75 and reference density at 349 anchors, both above the series baselines, with all four categories in or above the sibling range. Repaired 14 broken links inherited from the sibling corpus and consolidated 8 duplicate-URL anchors across the three passes. All fifteen post_url targets resolve, so the article can publish standalone. Forward references to A289 through A292 are plain prose rather than `post_url` links, per the back-reference-only convention.

### History of SpaceX Governance article (A287) — Published

**Files**:
- `_posts/2026-07-30-spacex_history_governance.markdown` (A287, seventh article of the History of SpaceX series, series `spacex_history`, series_index 7 of 12, editorial date 2026-07-30 09:00 UTC)

**Topic**: Seventh article in the History of SpaceX series treating the governance forcing-function condition, which requires that a mission-directed venture absorb the capital its mission demands without transferring to the capital providers the authority to redirect the mission. Article develops the control wedge formalism separating voting rights from cash-flow rights, walks the SpaceX control trajectory through the 2002 self-funded founding, the dual-class share architecture, the thirty-plus financing rounds, the January 2015 Google and Fidelity round that introduced strategic investors at scale, the semi-annual tender-offer liquidity mechanism that substitutes for a public listing, the deferred initial-public-offering decision, and the unresolved Starlink separation question. Article contrasts the configuration against the OpenAI governance failure of November 2023, in which a structure with an unbounded formal wedge was defeated in five days because it lacked any resource-dependence position, and against the Tesla compensation litigation that shows the same individual accepting substantially weaker control where capital was raised publicly. Article treats the Carl Zeiss Stiftung of 1889, the Robert Bosch ownership separation, and the Novo Nordisk Foundation structure as the centurial precedents. Pattern-extraction section states five sub-properties and identifies successor commitment as the one SpaceX does not satisfy.

**Article Numbers**: A287
**Completion**: 100% Published on 2026-08-02 as part of the A284-A287 batch via the two-commit publication sequence pushed to origin/master
**Publication Sensibility**: High (published; editorial date 2026-07-30 verified free of collision, build verified before push)
**Status**: Initial draft 2026-08-02, equation-density expansion pass same day adding 21 display equations (49 to 70) to bring the absolute count into the 60-72 series band. Primary-reference expansion pass added 52 primary reference URLs (25 to 77), placing the securities-law, corporate-law, listing-standard, index-provider, and comparator-disclosure sources at the claims a citation audit found uncited. Publication-review expansion pass then added a new Sunset-Provision and Successor Question H2 section developing the article's identified weakest sub-property, six cross-disciplinary traditions, four historical precedent cases including the Xerox governance failure and the IBM System/360 commitment, three Historiographical Gap subsections, four analytical framings, and expanded contemporary-landscape and foundation-class treatments. 1,302 lines, ~23,648 words, 72 display equations, 26 H2 sections, 15 H3 subsections, 115 book references, 78 primary reference URLs, 78 research references, 16 related-post cross-references, 287 total reference anchors with zero missing, zero unused, and zero duplicate anchors. Zero em-dashes, en-dashes, prose contractions, prose parentheticals, prose colons, or prose semicolons outside math. All LaTeX balanced. All 137 reference URLs verified, drawn from the governance-literature set checked at drafting and from the A286 apparatus repaired earlier in the session. Categories `history business aerospace`. Debug tags on lines 13-14. Equation density in band at 72. Reference density above the 190-234 baseline at 287 anchors, with all four categories in the sibling range. Repaired 20 further broken links inherited from the sibling corpus during the publication-review pass. Forward references to A288 and A290 are deliberately plain prose rather than `post_url` links, per the back-reference-only convention. The article back-references A286 by `post_url`, which resolved on batch publication.

### History of SpaceX Generality-Forcing article (A286) — Published

**Files**:
- `_posts/2026-07-29-spacex_history_generality_forcing.markdown` (A286, sixth article of the History of SpaceX series, series `spacex_history`, series_index 6 of 12, editorial date 2026-07-29 09:00 UTC)

**Topic**: Sixth article in the History of SpaceX series treating the generality-forcing forcing-function condition. Article walks the Mars-mission concept development from the 2001 Mars Oasis concept through the September 27 2016 Interplanetary Transport System announcement, the September 29 2017 Making Life Multi-Planetary revision that states the generality-forcing condition as explicit design intent, and the subsequent Starship architectural convergence. Article develops the Mars-transportation requirement stack across seven requirement categories with the velocity-budget basis for the dominance ordering, then treats the reusable-launch, mass-to-orbit-reduction, in-space-refueling, and life-support-integration generalizations and the Human Landing System, Starlink, National Security Space Launch, and geostationary applications. Article contrasts the SpaceX pattern against three canonical negation cases comprising the Space Shuttle union-construction failure, the Space Launch System constrained-design-space failure, and the Constellation narrow-requirement failure. Article closes with pattern-extraction section stating the abstract generality-forcing mechanic requires joint satisfaction of five sub-properties plus a cost condition the capability condition does not imply, together with a five-question diagnostic procedure.

**Article Numbers**: A286
**Completion**: 100% Published on 2026-08-02 as part of the A284-A287 batch via the two-commit publication sequence pushed to origin/master
**Publication Sensibility**: High (published; comprehensive literature-survey article at structural parity with the series; editorial date 2026-07-29 verified free of collision)
**Status**: Draft completed 2026-07-30 from an interrupted prior drafting session. Prior state was 5,609 words across 18 H2 sections with 56 reference anchors and six template sections absent. Completion pass added the Mars-Mission Concept Development section, the Space Shuttle, Space Launch System, and Constellation negation-case sections promised in the opening paragraph but previously unwritten, and the six template sections at parity with the published articles comprising Deep Historical Comparative Precedents, Historiographical Gap and Recent Scholarship with seven H3 subsections, Contemporary Comparative Landscape, Comparative Cross-Sectional Analysis, Data Sources and Reconstruction Methodology, and Alternative Analytical Frameworks. Existing thin sections expanded with identification-strategy, amortization, factor-substitution, refueling-coupling, life-support-closure, and residual-requirement analysis. Equation-density expansion pass added 33 display equations (39 to 72) across the under-equationed sections, bringing absolute equation count into the series band of 60-72 that A281 through A285 occupy. Primary-reference expansion pass added 33 primary reference URLs (74 to 107) at the uncited factual claims a citation audit identified, concentrated in the three negation-case sections which previously carried almost no primary program documentation. Publication-review expansion pass then added seven cross-disciplinary traditions (military-innovation and dual-use, transaction-cost, organizational-learning, industrial-organization, network-economics and standards, science-and-technology studies, behavioral and managerial cognition), five historical precedent cases including the IBM System/360 architecture-unification precedent treated as the closest structural analogue outside aerospace, five Historiographical Gap subsections covering recent scholarship, critical and skeptical literature, comparative-national and developmental-state literature, single-case-inference methodology, and reliability and organizational-failure literature, four additional analytical framings, and an expanded contemporary landscape. Final metrics 1,586 lines, ~29,811 words, 72 display equations, 28 H2 sections, 16 H3 subsections, 167 book references, 110 primary reference URLs, 99 research references, 14 related-post cross-references, 390 total reference anchors with zero missing, zero unused, and zero duplicate anchors. Zero em-dashes, zero en-dashes, zero prose contractions, zero prose parentheticals, zero prose colons, and zero prose semicolons outside math notation. Categories `history business aerospace`. Debug tags on lines 13-14. All reference URLs verified by HTTP request, with 32 broken links inherited from the sibling-article reference corpus repaired and the remainder either 2xx or non-2xx from documented bot-detection or paywall behavior. Cross-references to A284 and A285 now resolve, both having published in the same batch. Build verified before push with all seven series articles present and every post_url resolving.

### History of SpaceX Decomposability article (A285) — Published

**Files**:
- `_posts/2026-07-28-spacex_history_decomposability.markdown` (A285, fifth article of the History of SpaceX series, series `spacex_history`, series_index 5 of 12, editorial date 2026-07-28 09:00 UTC)

**Topic**: Fifth article in the History of SpaceX series treating the decomposability forcing-function condition. Article walks the vehicle-family ladder from Falcon 1 through Falcon 9, Dragon 1, Falcon Heavy, Dragon 2, and the Starship and Super Heavy architecture as independently valuable rungs, together with the Merlin and Raptor engine-family progressions and the launch-site progression, and contrasts the pattern against single-bet negation cases.

**Article Numbers**: A285
**Completion**: 100% Published on 2026-08-02 as part of the A284-A287 batch via the two-commit publication sequence pushed to origin/master
**Publication Sensibility**: High (published; editorial date 2026-07-28 verified free of collision)
**Status**: Published 2026-08-02. 16,942 words, 69 display equations, 24 H2 sections, 257 total reference anchors with zero missing, unused, or duplicate anchors. Categories `history business aerospace`. Debug tags on lines 13-14. Front matter `series: spacex_history, series_title: History of SpaceX, series_index: 5`. This entry was created at publication; the article was drafted in an earlier session for which the summary entry had not been written.

### History of SpaceX Value Capture article (A284) — Published

**Files**:
- `_posts/2026-07-27-spacex_history_value_capture.markdown` (A284, fourth article of the History of SpaceX series, series `spacex_history`, series_index 4 of 12)

**Topic**: Fourth article in the History of SpaceX series treating the value-capture forcing-function condition. Article walks the launch-service pricing evolution and dollar-per-kilogram trajectory, the Starlink vertical integration into satellite-broadband, and contrasts with the canonical Xerox PARC and Bell Labs value-capture negation cases. Article closes with pattern-extraction section stating the abstract value-capture mechanic requires joint satisfaction of five sub-properties.

**Article Numbers**: A284
**Completion**: Initial draft only. Equation-density, reference-density, and publication-review expansion passes pending.
**Publication Sensibility**: High (initial draft covers all required content; awaits expansion passes to reach publication-review parity with A281, A282, and A283)
**Status**: Initial draft 2026-07-25. 489 lines, ~7,624 words, 12 display equations, 22 H2 sections, 67 total reference anchors with zero missing/unused/duplicated. Zero em-dashes/en-dashes/prose contractions/prose parentheticals outside math notation. Categories `history business aerospace`. Debug tags on lines 13-14. Front matter `series: spacex_history, series_title: History of SpaceX, series_index: 4`. Awaits equation-density expansion pass, reference-density expansion pass, and comprehensive publication-review expansion pass.

### Enhanced and Luxury Facilities miniseries (A293-A294) — Published

**Files**:
- `_posts/2026-01-18-enhanced_luxury_restrooms.markdown` (A293, series `enhanced_luxury_facilities`, series_index 1 of 2, editorial date 2026-01-18)
- `_posts/2026-01-19-enhanced_luxury_bathing.markdown` (A294, series `enhanced_luxury_facilities`, series_index 2 of 2, editorial date 2026-01-19)

**Topic**: Two-part miniseries with shared main title "Enhanced and Luxury Facilities" treating facilities that serve a universal somatic necessity as objects of design elevation. A293 treats the elimination facility (the restroom) and A294 treats the immersion facility (the bath). Both apply a shared six-dimension facility-elevation framework introduced in A293: hygienic sufficiency as a gating base, discretion and privacy, sensory and aesthetic enrichment, throughput and access equity, social and ritual signification, and technological augmentation, aggregated into a gated elevation index. A293 walks the history of the elimination facility from the Roman public latrine through the Victorian sanitary revolution, the public convenience and the gendering of access, the Japanese high-technology washroom and the Tokyo Toilet project, the luxury-fixture and attended-restroom market, and vending and menstrual-equity provisioning, with the queueing and potty-parity apparatus, acoustic masking, ventilation, hygiene and flush hydraulics, and thermal comfort as its quantitative core. A294 walks the history of elevated bathing from the Great Bath of Mohenjo-daro through the Roman thermae, the Islamic hammam, the Finnish sauna and Russian banya, the Japanese onsen sento and furo, the sweat cultures of the Americas and Korea, the European thermal spa and the culture of the cure, the bath as a subject of art, and the modern wellness economy, with heat transfer, immersion physiology, hot-spring geochemistry and geothermometry, disinfection kinetics, and bath-hall acoustics as its quantitative core. A294 closes with the cross-facility generalization that facilities serving a universal necessity are elevated along the same six dimensions with weights set by the nature of the bodily act. Both treat sex-based differences, the asymmetric-provision potty-parity question for A293 and the segregated-bathing question for A294.

**Article Numbers**: A293 and A294 (two articles). Next available after publication: A295. The History of SpaceX series reserves A283-A292 separately.
**Completion**: 100% Published as a two-commit batch on 2026-07-25 at editorial dates 2026-01-18 and 2026-01-19, pushed to origin/master (staging commit `f903826` followed by publication commit with git mv from `_drafts/` to `_posts/` with date prefixes and process file sync). Editorial dates verified free of collision, filling the gap between 2026-01-17 nonblocking-getchar-in-c and 2026-01-20 timezones_for_trading_and_remote_teams.
**Publication Sensibility**: High (comprehensive survey-and-review articles under a shared analytical framework, with primary-source anchoring and contemporary-literature review; standalone miniseries filling a two-day corpus gap; no length or reference limit applied per human-pilot direction).
**Status**: Published 2026-07-25 after initial drafting, equation-density expansion (A293 to 70 and A294 to 68 display equations), reference-density and primary-source expansion (A293 to 203 total anchors with 51 books, 106 reference, 46 research; A294 to 209 total anchors with 66 books, 93 reference, 49 research, 1 related post), and comprehensive publication-review expansion strengthening the contemporary-literature survey. A293: 1,006 lines, ~17,702 words, 70 display equations, 31 H2 sections. A294: 961 lines, ~15,571 words, 68 display equations, 32 H2 sections. Zero em-dashes, en-dashes, prose contractions, or prose parentheticals or colons outside math notation on both. Anchor integrity clean on both (zero missing, unused, duplicate). Categories `culture architecture design`. Debug tags on lines 13-14. A294 back-references A293 via post_url; A293 references the companion in prose only. Primary sources include classical texts (Frontinus, Vitruvius, Celsus, Pliny, Strabo, Pausanias), primary legal and standards documents (10 CFR Part 430, US Access Board, EPA WaterSense, UN resolution 67/291), and primary institutional data (WHO sanitation, WHO and UNICEF JMP). All URLs verified this session via WebFetch.

### History of SpaceX Value Gradient article (A282) — Published

**Files**:
- `_posts/2026-07-25-spacex_history_value_gradient.markdown` (A282, second article of the History of SpaceX series, series `spacex_history`, series_index 2 of 12)

**Topic**: Second article in the History of SpaceX series treating the value-gradient forcing-function condition that the series opener A281 introduced as the first of seven forcing-function conditions in the seven-plus-three analytical framework. Article walks the SpaceX value-gradient trajectory through the Falcon 1 development period from 2002 through 2008 including the four failed launch attempts culminating in the September 28 2008 fourth-flight orbital success and the July 14 2009 RazakSAT first commercial payload, the Falcon 9 development period from 2005 through 2010 including the nine-engine octaweb architecture, the NASA COTS Round 1 278 million dollar award of August 2006, the June 4 2010 first Falcon 9 flight, the Dragon C1 first orbital flight of December 2010, the CRS-1 anchor demand of December 23 2008, the Dragon C2/C3 ISS berthing of May 22 2012, and the SES-8 first geostationary transfer orbit of December 3 2013, and the reusability progression from 2011 through 2026 including the Grasshopper testbed, the F9R Dev1 continuation, the December 21 2015 Orbcomm-2 first successful land landing, the April 8 2016 CRS-8 first drone-ship landing, the March 30 2017 SES-10 first reflight, the Falcon 9 Full Thrust and Block 5 configurations, and the contemporary routine-refly cadence. Article contrasts the SpaceX value-gradient pattern with the Iridium single-bet configuration that concentrated value realization at a distant terminal milestone, with the November 1998 commercial service commencement followed by the August 13 1999 Chapter 11 bankruptcy filing after subscriber acquisition fell to approximately 55000 against a 500000 forecast. Article closes with pattern-extraction section stating the abstract value-gradient mechanic requires joint satisfaction of five sub-properties: architectural decomposability, incentive-structure alignment, process discipline, strategic patience, and demand-configuration absorption.

**Article Numbers**: A282 (with A283-A292 planned in subsequent sessions)
**Completion**: 100% Published as standalone on 2026-07-25 at editorial date 2026-07-25 via two-commit sequence pushed to origin/master (staging commit `c28a6a0` followed by publication commit with git mv from `_drafts/` to `_posts/` with date prefix and process file sync).
**Publication Sensibility**: High (comprehensive literature-survey article covering the value-gradient trajectory across three development periods with pattern-extraction closing; comprehensive coverage of the surrounding scholarly literature including twelve cross-disciplinary framings, sixteen deep historical comparative precedents, six-subsection historiographical-gap treatment, eleven alternative analytical frameworks, and a comparative cross-sectional analysis of adjacent firms; editorial date 2026-07-25 verified free of collision with published corpus; publishing standalone under human-pilot direction rather than waiting for the full twelve-article batch the handoff prompt originally proposed)
**Status**: Published 2026-07-25 after with equation-density expansion pass (16 to 64 display equations), reference-density expansion pass (99 to 198 total anchors), and comprehensive publication-review expansion pass (198 to 236 total anchors, adding two new H2 sections Comparative Cross-Sectional Analysis and Data Sources and Reconstruction Methodology at parity with A281 opener, expanding Cross-Disciplinary Framings with six additional traditions including institutional economics and financial sociology and absorptive capacity and ecosystem strategy and reliability engineering, expanding Deep Historical Comparative Precedents with six additional cases including Tesla Roadster to Model S to Model 3 lineage and Airbus A300 to A380 family and International Space Station assembly and Boeing 787 development and NASA Constellation cancellation and Toyota Production System evolution, and expanding Alternative Analytical Frameworks with four additional framings including political-economy critique and public-choice and rent-seeking and national-champion and actor-network-theory). 1,235 lines, ~24,367 words, 64 display equations, 20 H2 sections, 85 book references, 60 research references, 79 primary reference URLs, 12 related-post cross-references, 236 total reference anchors with zero missing/unused/duplicated. Zero em-dashes/en-dashes/prose contractions/prose parentheticals outside math notation. Descriptive-analytical framing throughout. Categories `history business aerospace`. Debug tags on lines 13-14. Front matter `series: spacex_history, series_title: History of SpaceX, series_index: 2`. All 12 post_url cross-references to existing published corpus verified including back-reference to A281 series opener.

### History of SpaceX series opener (A281) — Published

**Files**:
- `_posts/2026-07-24-spacex_history_framing.markdown` (A281, series opener of planned twelve-article History of SpaceX series, series `spacex_history`, series_index 1 of 12)

**Topic**: Series opener for the planned twelve-article History of SpaceX (A281-A292). Introduces the seven-plus-three analytical framework the subsequent articles will apply, comprising seven forcing-function conditions (value gradient, anchor demand, value capture, decomposability, generality-forcing, governance, portfolio patience) plus three capital-formation legs (government anchor, patient private, category-dominating commercial spinoff). Article establishes the framing that SpaceX is the singular closed-conjunction modern case that satisfies all seven conditions plus all three capital-formation legs, characterizes the mission-primary capital-insatiable government-anchor-dependent venture pattern, provides the SpaceX founding narrative and 2002-2008 pre-COTS prologue including the four Falcon 1 launch attempts culminating in the September 28 2008 fourth-flight success and the December 23 2008 CRS-1 anchor-demand transition, and previews articles A282-A292 that treat each condition and leg in turn. Article treats SpaceX both as comprehensive general history with dates, events, characters, contract mechanics, and technical specifications and as a load-bearing-mechanics case study whose pattern-extraction closing section states the abstract mechanic each article's history embodies.

**Article Numbers**: A281 (with A282-A292 planned in subsequent sessions)
**Completion**: 100% Published as standalone on 2026-07-24 at editorial date 2026-07-24 via two-commit sequence pushed to origin/master (staging commit `9f43278` followed by publication commit with git mv from `_drafts/` to `_posts/` with date prefix and process file sync).
**Publication Sensibility**: High (comprehensive literature-survey framing article that also stands alone as an introduction to the SpaceX case study under the mission-oriented-innovation framework; comprehensive coverage of the surrounding scholarly literature including seven cross-disciplinary framings, ten deep historical comparative precedents, comprehensive historiographical-gap treatment with subsections by literature type, ten alternative analytical frameworks, and a comparative cross-sectional analysis of adjacent firms; editorial date 2026-07-24 verified free of collision with published corpus; publishing standalone under human-pilot direction rather than waiting for the full twelve-article batch the handoff prompt originally proposed)
**Status**: Published 2026-07-24 after equation-density expansion pass (20 to 65 display equations), reference-density expansion pass (102 to 190 total anchors), and comprehensive publication-review expansion pass (190 to 292 total anchors, adding two new H2 sections Comparative Cross-Sectional Analysis and Data Sources and Reconstruction Methodology, expanding Cross-Disciplinary Framings with six additional traditions including science-and-technology studies and institutional economics and developmental state and financial sociology and real options and evolutionary economics, expanding Deep Historical Comparative Precedents with eight additional cases including Manhattan Project and Peenemünde and RAND and Apollo and TVA and Panama Canal and Human Genome Project and Airbus/Ariane and Dutch East India Company, restructuring Historiographical Gap with six H3 subsections by literature type, and expanding Alternative Analytical Frameworks with five additional framings including resource-based-view and dynamic capabilities and real-options and Marxist critique and public choice and complexity-and-evolutionary and actor-network-theory). 1,301 lines, ~24,500 words, 65 display equations, 20 H2 sections, 130 book references, 62 research references, 86 primary reference URLs, 14 related-post cross-references, 292 total reference anchors with zero missing/unused/duplicated. Zero em-dashes/en-dashes/prose contractions/prose parentheticals outside math notation. Descriptive-analytical framing throughout. Categories `history business aerospace`. Debug tags on lines 13-14. Front matter `series: spacex_history, series_title: History of SpaceX, series_index: 1`. All 14 post_url cross-references to existing published corpus verified.

### Virtual Reputation Manipulation miniseries (A277-A280) — Published

**Files**:
- `_posts/2026-01-22-virtual_reputation_manipulation_theory.markdown` (A277, series opener, index 1)
- `_posts/2026-01-23-virtual_reputation_manipulation_self_promotion.markdown` (A278, index 2)
- `_posts/2026-01-24-virtual_reputation_manipulation_competitor_attack.markdown` (A279, index 3)
- `_posts/2026-01-25-virtual_reputation_manipulation_detection_and_organic.markdown` (A280, series closer, index 4)

**Topic**: Four-article miniseries with shared main title "Virtual Reputation Manipulation" and per-article subtitles treating reputation manipulation in the contemporary attention economy as a first-class analytical object. A277 opener establishes reputation as an economic good with information-asymmetry and signaling structure, formalizes the manipulation equilibrium as a prisoner's dilemma over a two-sided platform market, characterizes the organic-establishment minority puzzle via credibility-of-costly-signaling, audience-selection, reputation-portfolio, temporal-arbitrage, and enforcement-shadow accounts, and introduces the six-axis analytical framework (signal, objective, structure, model, interaction, adaptation) that subsequent articles apply. A278 will treat self-promotion oriented manipulation techniques (individual and coordinated review fabrication, follower and engagement purchase, sockpuppet amplification, generative-model produced testimonials, aggressive-end SEO, coordinated cross-platform amplification, credential fabrication, reputation laundering) organized by signal channel and account provenance with FTC enforcement, platform integrity disclosure, and academic detection case anchoring. A279 will treat competitor-attack oriented manipulation techniques (review bombing, brigading, negative SEO, defamation campaigns, reporting-system weaponization, Sybil downvoting, complaint-farm services, adversarial content operations) organized by attack vector and target reputation-system position with parallel case anchoring. A280 series closer will treat the detection landscape (statistical, machine-learning, network, human-review, cross-platform collaboration), the countermeasure landscape (platform integrity operations, identity verification, transaction verification, legal liability, cryptographic attestation), and the organic-establishment minority with forward projection to the 2030-2050 window under alternative assumptions about generative-model capability, platform-integrity investment, regulatory enforcement, and cross-platform coordination.

**Article Numbers**: A277 through A280 (four articles)
**Completion**: 100% Published as batch on 2026-07-24 at editorial dates 2026-01-22 through 2026-01-25 via two-commit sequence pushed to origin/master (staging commit `10ec2a0` followed by publication commit with git mv from `_drafts/` to `_posts/` with date prefixes and process file sync). Pre-NDA state-of-the-art contemporaneous literature review; publication commit establishes the pre-disclosure timestamp.
**Publication Sensibility**: High (analytical descriptive framing rather than operational playbook; treats the manipulation-saturated equilibrium as the empirical default in most contemporary online reputation systems; draws on the economics-of-reputation literature from Akerlof 1970 through Mailath and Samuelson 2006, the sociology-of-reputation literature from Goffman 1959 through Origgi 2018, the digital-reputation-systems literature from Resnick et al 2000 through Cabral 2012, and the manipulation-empirics literature from Luca and Zervas 2016 through He Hollenbeck Proserpio 2022; editorial dates 2026-01-22 through 2026-01-25 planned to fill exactly the four-day gap between 2026-01-21 A71 macOS pbcopy and pbpaste and 2026-01-26 A72 WebAssembly on Jekyll in the current corpus)
**Status**: A277 drafted 2026-07-24 with equation-density pass (60 equations final), reference-density pass (45 primary reference URLs), and comprehensive publication-review expansion pass (234 total anchors final) same day. 1,002 lines, 15,449 words, 60 display equations, 17 H2 sections, 79 book references, 85 research references, 70 primary reference URLs, 234 total reference anchors, zero missing/unused, zero em-dashes/en-dashes/contractions. Comprehensive literature survey covering economics-of-reputation, sociology, behavioral economics, computer-science-and-networks, legal scholarship, critical media studies, decentralized systems, pre-industrial and early-modern historical antecedents, regulatory framework across US federal/state/EU/UK/Australia/Germany/France/India/Singapore/Brazil/China, Section 230 and defamation case law, platform-integrity self-regulation, and generative-model impact.

A280 drafted 2026-07-24 with equation-density expansion pass (29 to 72 equations, matching A278/A279 bar), reference-density expansion pass (31 to 104 primary references, exceeding A278's 92), and comprehensive publication-review expansion pass (159 to 191 total anchors, adding three new H2 sections mirroring A277-A279 treatment). 1,128 lines, 12,922 words, 72 display equations, 19 H2 sections (Cross-Disciplinary Framings, Historiographical Gap and Recent Scholarship, Alternative Analytical Frameworks added in publication-review pass), 34 H3 sections, 31 book references (up from 11), 104 primary reference URLs, 53 research references (up from 41), 3 related-post cross-references (to A277, A278, A279), 191 total reference anchors with zero missing/unused/duplicated, zero em-dashes/en-dashes/contractions. Descriptive-analytical framing throughout. Categories `economics technology sociology`. Debug tags on lines 13-14. Front matter `series: virtual_reputation_manipulation, series_index: 4`. Article serves as series closer with retrospective synthesis, comprehensive detection-methodology-and-countermeasure landscape treatment, organic-establishment-minority case studies, historical inflection points, comparative precedents, counterfactuals, forward projection with falsification framework, contingency analysis, methodology and limitations statement, and consolidated open questions. Detection-methodology section covers statistical anomaly detection (CUSUM, Hawkes, Bonferroni correction), graph-theoretic detection (modularity, GNN via Kipf-Welling and Hamilton-Ying-Leskovec, embedding-based via Dou et al fraud detectors), machine-learning classifier approaches (ensemble accuracy bound, precision-recall AUC under class imbalance via Davis-Goadrich 2006), adversarial ML defenses (adversarial training via Madry et al 2018, certified robustness via Cohen-Rosenfeld-Kolter 2019 randomized smoothing, watermarking), human review integration (optimal triage threshold via Roberts 2019 and Gray-Suri 2019 Ghost Work), cross-platform collaboration (mutual-information gain, GIFCT, Christchurch Call). Countermeasure section covers platform-integrity operations (budget optimization), identity-verification (composite friction cost, W3C VC/DID, FIDO, WebAuthn), content-authentication (C2PA, Content Authenticity Initiative, Kirchenbauer watermarking), legal-liability regimes (FTC 2024 rule, Lanham Act, defamation law), market-based countermeasures (Reputation.com, NetReputation, Fakespot). Organic-establishment section provides six detailed case studies: Wikipedia (consensus editing, sockpuppet investigations, Konieczny 2010, Jemielniak 2014, Halfaker et al 2013), GitHub (commit signing, downstream verification, Vasilescu-Serebrenik-Devanbu-Filkov 2016, Kalliamvakou et al 2016), academic reputation (peer review via Bornmann 2011, Ding et al 2009 PageRank for authors, ORCID, Retraction Watch), Stack Exchange (reputation cascade via Movshovitz-Attias et al 2013), curated high-barrier communities (MetaFilter, LessWrong), cryptographic-attestation Web3 alternatives (Weyl-Ohlhaver-Buterin 2022, Ethereum Attestation Service, Zargham-Nabben 2022 tempering critique). Five common enabling conditions for organic establishment identified with composite survival function. Forward projection develops central scenario and four alternatives (generative-AI acceleration, regulatory response, decentralization, trust collapse) with falsification framework identifying specific empirical predictions and time horizons. Deep historical comparative precedents cover medieval guilds (Epstein-Prak 2008), Consumer Reports 1936 founding, Pure Food and Drug Act 1906, FTC founding 1914, journalism verification-standards evolution (Kovach-Rosenstiel 2001, Silverman 2007). Contingency analysis addresses generative-AI trajectory, regulatory-framework convergence, platform consolidation, cryptographic-identity adoption, and consumer-behavior adaptation contingencies. Methodology-and-limitations section states seven commitments and explicit limitations. Cross-references to A277 theory, A278 self-promotion, and A279 competitor-attack via post_url tags. Editorial date 2026-01-25 planned. Pending equation-density, reference-density, and comprehensive publication-review expansion passes to reach A278/A279 parity.

A279 drafted 2026-07-24 with equation-density expansion pass (34 to 72 equations, matching A278's 72-equation bar), reference-density expansion pass (70 to 99 primary references, exceeding A278's 86), and comprehensive publication-review expansion pass (128 to 190 total anchors, adding four new H2 sections mirroring A277's publication-review treatment). 1,076 lines, 13,638 words, 72 display equations, 22 H2 sections (Cross-Disciplinary Framings, Historical Antecedents, Historiographical Gap and Recent Scholarship, Alternative Analytical Frameworks added), 35 H3 sections, 30 book references (up from 4), 46 research references (up from 23), 112 primary reference URLs (up from 99), 2 related-post cross-references (to A277 and A278), 190 total reference anchors with zero missing/unused/duplicated, zero em-dashes/en-dashes/contractions in prose (Can't instances preserved within cited book and paper titles). Descriptive-analytical framing throughout. Categories `economics technology sociology`. Debug tags on lines 13-14. Front matter `series: virtual_reputation_manipulation, series_index: 3`. Article organizes competitor-attack technique inventory into review-signal attacks (individual negative fabrication with Yelp v Hadeed 2014, coordinated review bombing with Metacritic/Rotten Tomatoes/Goodreads/Amazon cases and Hawkes-process detection, cross-account downvoting, generative-model negative content), brigading and cross-community attack (cross-community brigading with Kumar 2018 Reddit analysis, Chandrasekharan 2017 hate-community ban effects, Hine 2017 4chan analysis, Zannettou 2018 Web-wide coordinated behavior, coordinated dogpiling with Gamergate documentation and Marwick-Caplan 2018, raid organization patterns with 4chan/Discord/Telegram infrastructure), negative SEO (toxic backlink attacks exploiting Google Penguin, duplicate content attacks exploiting Panda, malicious redirect injection, sitemap poisoning, algorithm exploitation with Google spam policies), defamation campaigns (false content publication under NY Times v Sullivan and Gertz frameworks, anonymous defamation with Dendrite and Cahill unmasking tests, coordinated defamation networks, search-engine-amplified defamation with rank-displacement effect), Sybil-attack downvoting (community platform vote manipulation, rating attacks, community-vote weaponization), reporting-system weaponization (false DMCA takedowns with Urban-Karaganis-Schofield 30-50% estimate and Lenz v Universal, trademark abuse with Rescuecom v Google, coordinated abuse reporting, platform-integrity system abuse), complaint-farm services (BBB complaint farms with ABC 20/20 investigation, negative-review farms, consumer-complaint-site abuse with Ripoff Report and ComplaintsBoard, government-complaint weaponization with FTC Consumer Sentinel), adversarial content operations (negative-topic association with Fazio 2019 illusory truth, meme warfare, doxing-adjacent tactics), and cross-platform coordinated negative campaigns. Six-axis framework applied. Detailed legal recourse landscape covers defamation actions (Sullivan/Gertz/Milkovich), Lanham Act §43a false advertising, state unfair-competition (California UCL §17200), intermediary-liability constraints under Section 230 (Zeran, Roommates, Batzel, Barnes, Force, Gonzalez), and international recourse (UK Defamation Act 2013, Germany NetzDG, Australia uniform framework, Canada Grant v Torstar, SPEECH Act 2010). Cross-references to A277 theory and A278 self-promotion via post_url tags; A280 back-references pending completion of that article.

A278 drafted 2026-07-24 with equation-density expansion pass, reference-density expansion pass, and comprehensive publication-review expansion pass (230 total anchors, adding four new H2 sections mirroring the A277/A279 publication-review treatment). 1,116 lines, 15,149 words, 72 display equations, 19 H2 sections (Cross-Disciplinary Framings, Historical Antecedents, Historiographical Gap and Recent Scholarship, Alternative Analytical Frameworks added in publication-review pass), 26 H3 sections, 44 book references (up from 9), 93 research references (up from 74), 92 primary reference URLs (up from 86), 1 related-post cross-reference to A277, 230 total reference anchors, zero missing/unused/duplicated, zero em-dashes/en-dashes/contractions. Descriptive-analytical framing throughout. Categories `economics technology sociology`. Debug tags on lines 13-14. Front matter `series: virtual_reputation_manipulation, series_index: 2`. Article organizes the self-promotion technique inventory into review-signal manipulation (individual fabrication with Ott et al 2011 stylometry, coordinated campaigns and review farming with He-Hollenbeck-Proserpio 2022 marketplace analysis, sockpuppet-driven deposition with Solorio et al Wikipedia framework and Kumar 2017 army-of-me treatment, generative-model-produced content with Sohail 2024 and Sadasivan 2023 detection-limit results), follower-and-engagement manipulation (follower purchase economies with NY AG v Devumi 2019 and De Micheli-Stroppa 2013, engagement purchase and coordinated engagement pods with Weller 2019, view-count and impression inflation with Pearce 2014 and White Ops Methbot), search-ranking manipulation (aggressive SEO with Gyongyi-Garcia-Molina 2005 taxonomy, Google Panda/Penguin algorithmic response, PageRank manipulation formalization, app-store optimization gaming with Ali 2017), network-scale coordinated inauthentic behavior (Sybil networks with Douceur 2002 through Alvisi 2013, cross-platform amplification rings with DiResta 2019 IRA analysis, click farms with Cushing 2013 Bangladesh investigation, state-sponsored operations with Mueller Report), astroturfing (corporate with Oreskes-Conway and Michaels, political with King-Pan-Roberts 50 Cent Army, front-organization structures), credential and identity fabrication (verified-badge acquisition through Musk-era Twitter Blue analysis, professional-credential fabrication, identity impersonation with FTC 2024 rule), reputation laundering (endorsement acquisition with FTC Endorsement Guides history from 2011 through 2024, cross-platform transfer, acquisition-based laundering). Six-axis framework applied to characterize each technique class. Detection methodology and platform countermeasure summaries deferred detailed treatment to A280 closer. Documented case anchoring: FTC v Sunday Riley 2019, FTC v UrthBox 2019, FTC v Devumi 2019, NY AG v Devumi 2019, SEC v Kardashian 2022, FTC v Machinima 2015, FTC v Warner Brothers 2016, Amazon v Fake Review Brokers 2022, Sony PSP 2006 fake blog, Whole Foods Mackey Rahodeb 2007, Beuk Boekhandel 2013 Dutch case, Bing 2004 astroturf blogging. Cross-reference to A277 via post_url tag; awaiting A279 and A280 for back-reference completion within series. Categories `economics technology sociology` (economics first because reputation manipulation is fundamentally an economic phenomenon under information asymmetry and signaling, technology second because it is digitally mediated through platforms, sociology third because reputation is a social construct). Debug tags `<!-- A277 -->` and `<script>console.log("A277");</script>` on lines 13-14. Series roadmap section previews A278-A280. Six-axis framework introduced in the framing section with per-axis operationalization equations. Cross-references within miniseries will use back-reference-only post_url tags once A278-A280 are drafted. Awaiting human pilot review before proceeding to A278. Next available article number after this miniseries publishes: A281.

### Ethnoreligion and American Political Economy series (A266-A276) — Published

**Files**:
- `_posts/2026-01-03-ethnoreligion_and_american_political_economy_framing.markdown` (A266, series opener, index 1)
- `_posts/2026-01-04-ethnoreligion_and_american_political_economy_colonial_folkways.markdown` (A267, index 2)
- `_posts/2026-01-05-ethnoreligion_and_american_political_economy_awakening_and_founding.markdown` (A268, index 3)
- `_posts/2026-01-06-ethnoreligion_and_american_political_economy_second_awakening_and_reform.markdown` (A269, index 4)
- `_posts/2026-01-07-ethnoreligion_and_american_political_economy_civil_war_and_reconstruction.markdown` (A270, index 5)
- `_posts/2026-01-08-ethnoreligion_and_american_political_economy_mass_immigration_and_closure.markdown` (A271, index 6)
- `_posts/2026-01-09-ethnoreligion_and_american_political_economy_depression_war_and_refuge.markdown` (A272, index 7)
- `_posts/2026-01-10-ethnoreligion_and_american_political_economy_postwar_transformation_and_reopening.markdown` (A273, index 8)
- `_posts/2026-01-11-ethnoreligion_and_american_political_economy_diversification_and_consolidation.markdown` (A274, index 9)
- `_posts/2026-01-12-ethnoreligion_and_american_political_economy_contemporary_sorting_and_new_flows.markdown` (A275, index 10)
- `_posts/2026-01-13-ethnoreligion_and_american_political_economy_retrospective_and_projection.markdown` (A276, series closer, index 11)

**Topic**: Eleven-article series with shared main title "Ethnoreligion and American Political Economy" and per-article subtitles walking the four-century American ethnoreligious development from pre-colonial Indigenous, African, and European substrates through contemporary 2024 religious sorting. A266 opener establishes the three-substrate framework, defines the ethnoreligion analytical construct distinct from ethnicity or religion alone, and introduces the six-axis analytical framework (signal, objective, structure, model, interaction, adaptation) subsequent articles apply. A267 covers colonial folkways 1607-1725 across the four established Fischer regional folkways (Puritan New England, Cavalier Chesapeake, Quaker Delaware Valley, Scots-Irish backcountry). A268 covers the First Great Awakening and founding-era religious settlement 1725-1789. A269 covers the Second Great Awakening and antebellum reform 1789-1861. A270 covers Civil War, Reconstruction, and continental consolidation 1861-1900 including Chinese Exclusion 1882 and Native reorganization. A271 covers mass immigration and restrictionist closure 1900-1924 through Johnson-Reed. A272 covers Depression, war, and refuge 1924-1945 including Bracero, Sephardic-Ashkenazi Holocaust refugees, and Japanese internment. A273 covers postwar transformation and reopening 1945-1980 including Displaced Persons Act, McCarran-Walter, Hart-Celler, Cuban, Puerto Rican Great Migration, and Vietnamese refugee waves. A274 covers full post-1965 diversification and religious right consolidation 1980-2000. A275 covers contemporary sorting and new flows 2000-2024 including African migration expansion, Latino diversification, South Asian mainstreaming, post-2001 refugee dynamics, Ukrainian post-2022, and contemporary religious sorting. A276 series closer synthesizes findings via retrospective causal mapping applying the six-axis framework across the four centuries, comparative cases (Canadian, Latin American, Australian, New Zealand, British post-imperial, European post-war, Israeli, East Asian), deep historical comparative precedents (Roman Empire, medieval Christendom, Reformation, Enlightenment), alternative analytical frameworks comparison (Bellah civil religion, Berger secularization, Stark and Bainbridge religious economies, Taylor A Secular Age, Wolfe One Nation After All), alternative American development counterfactuals, and forward projection for the 2024-2050 window.

**Article Numbers**: A266 through A276 (eleven articles)
**Completion**: 100% (all eleven articles have completed four-pass workflow: initial draft, equation density, reference density, publication review)
**Publication Sensibility**: High (comprehensive treatment of the four-century American ethnoreligious development arc at unprecedented depth in the corpus; shared main title with per-article subtitles for reader-facing series identification; back-reference-only cross-references permit both rolling and batch publication; editorial dates 2026-01-03 through 2026-01-13 fill the eleven-day gap between A265 at 2026-01-02 and A94 at 2026-01-14; pre-NDA contemporaneous record of the state of the ethnoreligious historical and analytical literature)
**Status**: Published as batch on 2026-07-24 at editorial dates 2026-01-03 through 2026-01-13 via three-commit sequence pushed to origin/master (staging commit `32a0a9a` followed by publication commit `cb1ce56` with git mv and process file sync, followed by editorial de-bloat commit `51c84e6` removing 894 uses of "substantially" and 229 uses of "successive" as filler across the eleven articles via `tmp/deblat_ethnoreligion.py`). Total 10,806 lines across eleven articles (A266 826, A267 878, A268 978, A269 1,303, A270 1,174, A271 1,184, A272 1,075, A273 1,094, A274 912, A275 842, A276 540). Total 165,625 words. Total 613 display equations. Total 1,539 book references and 613 primary reference URLs across the series. All eleven articles style-clean (zero em-dashes, en-dashes, contractions). Zero forward or self-references (cross-reference monotonicity verified). Zero missing or unused anchors. Six-axis framework naming unified across the series (signal, objective, structure, model, interaction, adaptation, introduced in A266 and applied consistently in A267-A276). Terminological Note sections present across all eleven articles. All eleven articles carry `<!-- Axxx -->` and `<script>console.log("Axxx");</script>` debug tags on lines 13-14. Cross-references within series use back-reference-only post_url tags resolving simultaneously at batch publication. Categories `history economics religion` uniform across all eleven articles (avoiding the Keleusma URL shadow on `keleusma`-first paths). Editorial dates 2026-01-03 through 2026-01-13 verified free of collision with published corpus posts. Cohesiveness pass 2026-07-24 added 148 primary reference URLs to A266-A269 to achieve density parity with A270-A275 and added 12 equations to A266-A268 to improve equation density. Next available article number after publication: A277.

### Las Vegas: Historical Arc, Present Relevance, and Forward Projection (A249) — Published

**Files**:
- `_posts/2026-01-30-las_vegas_history_and_forward_projection.markdown` (A249, standalone one-off)

**Topic**: Standalone one-off case-study article treating Las Vegas across four historical phases (railroad watering stop through mob-era Strip through corporate megaresort transformation to current amenity-priced regime) with point-in-time regional, national, and global relevance assessment as of the mid 2020s and forward projection across 2026 to 2050 under five constraints (water, climate, competition, demographics, pricing power). Core analytical thesis: the historical loss-leader casino model treated non-gaming amenities as subsidies against gambling profit, whereas the contemporary amenity-priced regime treats each amenity as a standalone profit center; the two models optimize different objective functions.

**Article Numbers**: A249
**Completion**: 100%
**Publication Sensibility**: High (comprehensive treatment of the historical arc plus present relevance plus forward projection with primary source anchoring across gambling history, mob-era journalism, Colorado River water history, and primary legal documents; standalone case study filling the single relatively recent one-day publication-date gap between A94 constant_amm_mathematics at 2026-01-29 and A93 claude_code_getting_started at 2026-01-31)
**Status**: Published as standalone on 2026-07-18 at editorial date 2026-01-30. 272 lines. Fourteen display equations covering house-edge expected value, aggregate gaming revenue, per-visitor profit, optimal amenity-subsidy condition, non-gaming revenue share, per-visitor revenue decomposition, price elasticity of volume, southern Nevada water balance, per-capita consumption trajectory, water-constrained population ceiling, Macau-to-Vegas revenue ratio, days-above-105-degrees trajectory, Vegas share of US gaming, and cohort-weighted gambling participation. Forty-two references (eleven books, twenty-eight reference URLs, three research). Primary source anchoring includes Rothman Neon Metropolis 2002, Schwartz Roll the Bones 2006 and Suburban Xanadu 2003, Reid and Demaris Green Felt Jungle 1963, Reisner Cadillac Desert 1986, Fleck Water is for Fighting Over 2016, Findlay People of Chance 1986, Colorado River Compact 1922, Kefauver Third Interim Report 1951, Nevada Revised Statutes 463, Indian Gaming Regulatory Act 1988, Murphy v. National Collegiate Athletic Association 2018, NOAA Las Vegas climate records, IPCC AR6 WGII Chapter 14, US Census Bureau, UNLV Center for Gaming Research, Nevada Gaming Control Board, Bureau of Reclamation Lake Mead operations, Southern Nevada Water Authority, Macau DICJ, LVCVA, and 10-K filings of MGM Resorts, Wynn Resorts, Las Vegas Sands, Sphere Entertainment, and Liberty Media. All anchors resolve (42 defined URLs equal 42 citations). Categories `history economics urban`. Zero em-dashes, en-dashes, contractions, prose colons, prose semicolons, or prose parentheticals outside math notation. Debug tags on lines 10-11. Publication review pass corrected water intake elevations against Southern Nevada Water Authority and Bureau of Reclamation primary data, refined Colorado River Compact history to separate the 1922 Compact's basin apportionment from the Boulder Canyon Project Act of 1928's state-level allocation, added epistemic hedges throughout the forward projection paragraph, spelled out Representative Concentration Pathway and Las Vegas Sands acronyms, updated parking pricing to reflect 2016 launch and 2024 escalation, and hedged the MGM Empire City New York downstate license claim. Editorially back-dated to 2026-01-30 to fill the single relatively recent one-day publication-date gap in the corpus. Next available article number after publication: A250.

### Aerospace, Programming Languages, and Information Technology Co-Development series (A237-A248) — Published

**Files**:
- `_posts/2026-07-12-framing_and_the_co_development_mechanism.markdown` (A237, series opener)
- `_posts/2026-07-13-pre_war_computing_origins_and_ballistics.markdown` (A238, index 2)
- `_posts/2026-07-14-wartime_computing_and_code_breaking.markdown` (A239, index 3)
- `_posts/2026-07-15-early_cold_war_air_defense_and_sage.markdown` (A240, index 4)
- `_posts/2026-07-16-aerospace_simulation_and_real_time_systems.markdown` (A241, index 5)
- `_posts/2026-07-17-apollo_guidance_computer.markdown` (A242, index 6)
- `_posts/2026-07-18-arpanet_and_networking_origins.markdown` (A243, index 7)
- `_posts/2026-07-19-space_shuttle_software_as_engineering_landmark.markdown` (A244, index 8)
- `_posts/2026-07-20-safety_critical_software.markdown` (A245, index 9)
- `_posts/2026-07-21-silicon_valley_from_defense_contracting.markdown` (A246, index 10)
- `_posts/2026-07-22-software_defined_aerospace_and_autonomy.markdown` (A247, index 11)
- `_posts/2026-07-23-contemporary_snapshot_and_extrapolation.markdown` (A248, index 12, series closer)

**Topic**: Twelve-article rolling-publication series with shared main title "Aerospace, Programming Languages, and Information Technology Co-Development" and per-article subtitles walking the co-development arc chronologically from pre-war ballistic computing through contemporary software-defined aerospace and forward extrapolation. A237 opener establishes the co-development mechanism as a coupled first-order dynamical system, characterizes the semiconductor substrate under defense demand, formalizes real-time and reliability constraints distinguishing aerospace computing from commercial computing, and introduces the six-axis analytical framework subsequent articles apply. A238 through A248 walk the historical waves from pre-war computing origins and ballistics, through wartime computing and code-breaking, early Cold War air defense and SAGE, aerospace simulation and real-time systems, the Apollo Guidance Computer, ARPANET and networking origins, Space Shuttle software as engineering landmark, safety-critical software as an engineering discipline, Silicon Valley from defense contracting, software-defined aerospace and autonomy, to contemporary snapshot and extrapolation across the 2026-2050 window.

**Article Numbers**: A237 through A248 (twelve articles all published as of 2026-07-17 batch)
**Completion**: 100%
**Publication Sensibility**: High (comprehensive twelve-article treatment of the aerospace-computing co-development arc across editorial dates 2026-07-12 through 2026-07-23 fitting flush after A216 at 2026-07-11 with no adjacent post following A248; shared main title with per-article subtitles for reader-facing series identification; back-reference-only cross-references within series permit both rolling and batch publication)
**Status**: Twelve-article series published as batch on 2026-07-17. Total 2,418 lines across twelve articles (A237 opener 342, A238 pre-war 212, A239 wartime 202, A240 SAGE 188, A241 simulation 188, A242 Apollo 192, A243 ARPANET 178, A244 Shuttle 182, A245 safety-critical 172, A246 Silicon Valley 166, A247 software-defined aerospace 178, A248 contemporary 218). Total 120 display equations spanning the coupled dynamical system for H and S, Moore's Law doubling, Wright learning-curve unit-cost combined with Moore into per-transistor cost trajectory, exterior ballistics point-mass equation, table operations count, analog error scaling, ENIAC energy per operation and vacuum-tube MTBF, Enigma keyspace and Bombe throughput, Vernam cipher structure, Colossus cross-correlation test, Monte Carlo error scaling, Shannon perfect-secrecy and secrecy bounds, TMR reliability and N-modular generalization, Space Shuttle 4-plus-1 voting reliability, PASS programmer productivity, defect density exponential decay, Fagan inspection defect-capture, static-margin criterion, fly-by-wire pitch transfer function, sensor-to-display latency budget, C2 link margin, A-star and RRT complexity, ML training compute scaling, Chinchilla-form loss law, Herfindahl-Hirschman semiconductor concentration, extrapolation uncertainty growth, and Kondratiev cycle period. Total 286 references across twelve articles. All twelve style-clean (zero em-dashes, en-dashes, contractions, prose colons, prose semicolons, prose parentheticals outside math, or certification vocabulary). Cross-references within series use post_url tags resolving simultaneously at batch publication. Cross-references outside series to A112 fixed-wing UAV, A200 HDL history, A203 HDL state of practice, A206 PL Theory arc opener, A215 PL Theory 2020s. Categories `history technology aerospace` uniform across all twelve. Editorial dates 2026-07-12 through 2026-07-23 fill exactly the twelve-day gap after A216 Keleusma self-hosting at 2026-07-11 with no adjacent post following A248. Next available article number after publication: A249.

### Industrialization Waves and Geopolitical Positioning series (A225-A236) — Published

**Files**:
- `_posts/2026-03-15-framing_and_the_preindustrial_world.markdown` (A225)
- `_posts/2026-03-16-first_mover_britain.markdown` (A226)
- `_posts/2026-03-17-continental_european_followers.markdown` (A227)
- `_posts/2026-03-18-american_ascent.markdown` (A228)
- `_posts/2026-03-19-meiji_japan.markdown` (A229)
- `_posts/2026-03-20-soviet_forced_industrialization.markdown` (A230)
- `_posts/2026-03-21-postwar_japan_and_west_germany.markdown` (A231)
- `_posts/2026-03-22-east_asian_tigers.markdown` (A232)
- `_posts/2026-03-23-china_rise.markdown` (A233)
- `_posts/2026-03-24-india_and_late_arrivals.markdown` (A234)
- `_posts/2026-03-25-non_industrializers_and_edge_cases.markdown` (A235)
- `_posts/2026-03-26-contemporary_snapshot_and_extrapolation.markdown` (A236)

**Topic**: Twelve-article back-dated series with shared main title "Industrialization Waves and Geopolitical Positioning" and per-article subtitles walking industrialization waves chronologically. A225 opener establishes the primary-structural rather than sufficient thesis and the six-axis framework subsequent articles apply. A226 first-mover Britain establishes the reference case. A227 continental European followers as the paradigmatic Gerschenkron catch-up wave. A228 American ascent with continental-scale advantages. A229 Meiji Japan as first non-Western case ending in 1945 catastrophe. A230 Soviet forced industrialization as socialist state-led variant. A231 postwar Japan and West Germany treated jointly under American security guarantee. A232 East Asian tigers as extension of Japanese developmental template under Cold War subsidy. A233 China's rise as continental-scale tiger-template extension. A234 India and other late arrivals under post-Cold-War conditions. A235 non-industrializers and edge cases where supplementary explanation dominates. A236 closer with contemporary snapshot, forward extrapolation, and competing extrapolation strategies from Kotkin, Sachs, Perez, Smil, and Zeihan treated as illustrative rather than exhaustive alternatives.

**Article Numbers**: A225 through A236 (twelve articles)
**Completion**: 100%
**Publication Sensibility**: High (comprehensive back-dated series treating the full arc of industrialization order and its effects on contemporary geopolitical positioning at national and regional scope; shared main title with per-article subtitles for reader-facing series identification; ends flush at 2026-03-26 with A206 Programming Language Theory arc opener at 2026-03-27)
**Status**: Published as batch on 2026-07-16. Total 52 display equations across twelve articles covering Malthusian and organic-economy ceilings, fiscal-state extraction bounds, Gerschenkron catch-up arithmetic, Baumol convergence, forced-savings ratios, wartime destruction ratios, growth-rate premia per case, convergence trajectories per case, dollar and sterling reserve-currency decay, and forward projections for 2026-2050 window. Total 170 references. All twelve articles style-clean (zero em-dashes, en-dashes, contractions, prose colons, prose semicolons, prose parentheticals outside math, or certification vocabulary). Cross-references within series use post_url tags resolving simultaneously at batch publication. Cross-references outside series to A97 Space Force (2026-02-28) and A98 First-Mover Advantage (2026-03-01) predate 2026-03-15. Categories `history economics geopolitics` uniform across all twelve. Editorial dates 2026-03-15 through 2026-03-26 fill exactly the twelve-day gap between A107 Keleusma Getting Started at 2026-03-14 and A206 Programming Language Theory arc opener at 2026-03-27. Next available article number after publication: A237.

### Deficiencies of the HTML Hypermedia Model (A224) — Published

**File**: `_posts/2026-02-17-html_hypermedia_deficiencies.markdown`

**Topic**: Standalone one-off comparative article treating HTML as one hypermedia model among several historical alternatives. Establishes an eight-axis property inventory drawn from the Dexter Hypertext Reference Model (link directionality, link typing, sub-document addressability, transclusion, permanence, versioning, native composition, machine-readable structure) and walks each axis to catalogue where HTML omits or degrades the property relative to systems that had already established the requirement by the late 1980s. Six historical systems anchor the comparison: Bush's Memex as conceptual ancestor, Engelbart's NLS as first working implementation of most Memex properties, Nelson's Xanadu for transclusion and deep permanent addressing, Apple's HyperCard, Sakamura's BTRON hypermedia model as a business-computing subsystem of the TRON project, and Apple's OpenDoc for native document composition. Documents contemporary partial recoveries (wiki-system backlink tables, WebMentions and Pingback, static-site generator conventions, JSON-LD and schema.org for commercial use cases, content-addressable storage systems, Web Components) and treats each as evidence that the historical property was correctly identified as load-bearing. Explains HTML's dominance in terms of implementation simplicity, HTTP-only deployment, permissiveness under central-coordination absence, and community delegation of typing/versioning/composition rather than in terms of model superiority.

**Article Number**: A224
**Completion**: 100%
**Publication Sensibility**: High (foundational analytical article that treats HTML's hypermedia model at the class level and repositions historical hypermedia systems as an already-mature research programme whose properties HTML omitted rather than as historical curiosities superseded by a better model; complements later corpus articles on BTRON and Keleusma-as-hypermedia-substrate at 2026-05-23 and 2026-05-24 by supplying the general critique those later articles refine)
**Status**: Published 2026-02-17 at 09:00 UTC. 201 lines, mathjax true, two display equations ($N_{\text{stale}} \leq \lambda T$ reverse-index staleness bound in the Bidirectional Links section, $f_{\text{broken}}(t) = 1 - 2^{-t / T_{1/2}}$ broken-link decay in the Permanence and Versioning section). Twenty-two References-section entries: four books (Berners-Lee Weaving the Web, Nelson Computer Lib/Dream Machines, Nelson Literary Machines, Nyce and Kahn Memex to Hypertext), six standards and technical reports (Berners-Lee CERN 1989 proposal, Engelbart 1962 conceptual framework, Sakamura TRON, W3C Web Annotation, W3C RDF 1.1, WHATWG HTML), three related posts (A75 bidirectional agentic workflow, A76 markdown as spec, A77 LLM knowledge graphs), nine primary research papers (Berners-Lee Hendler Lassila 2001 Semantic Web Scientific American, Bush 1945 As We May Think Atlantic, Engelbart and English 1968 AFIPS FJCC NLS demo, Halasz 1988 CACM NoteCards, Halasz and Schwartz 1994 CACM Dexter, Klein et al. 2014 PLoS ONE reference rot, Meyrowitz 1989 Hypertext Proceedings Missing Link, Nelson 1965 ACM 20th National Conference File Structure, Nelson 1999 ACM Computing Surveys Xanalogical Structure). Zero em-dashes, en-dashes, contractions, prose semicolons, prose colons in prose, or prose parentheticals outside math notation. TRON expanded as The Real-time Operating system Nucleus and BTRON identified as the Business TRON subsystem on first use per corpus acronym-expansion rule. URL verification: three new primary DOIs verified (Berners-Lee Scientific American 200, Engelbart and English ACM 403 anti-bot matching corpus pattern, Klein PLoS ONE 200). Editorially back-dated to fill the one-day gap between A85 (2026-02-16 AI Apocalypse Will Be Polite) and A86 (2026-02-18 Mission Command Management Style). Categories `hypermedia web history` with no shadowing repository at those first-category paths. Two-commit publication pattern; commits local pending push authorisation.

### Audits and Provenance (A223) — Published

**File**: `_posts/2026-03-09-audits_and_provenance.markdown`

**Topic**: Standalone one-off analytical article treating audits at the class level. Identifies four properties shared across audit categories (scope and procedure, independent review, evidence artifacts, findings with remediation) and walks the three principal audit categories with worked examples: engineering audits (correctness, security, quality), documentation audits (completeness, currency, accuracy), and compliance audits (regulatory, contractual, internal policy). Positions provenance and audit trails as the substrate infrastructure that determines whether any of the three categories can be conducted rather than as a fourth category. Four provenance properties treated: chain of custody, immutability, reconstructibility, retention. Common failure modes catalogued including cargo-cult checklists, adversarial auditee posture, scope creep, retroactive documentation, findings without remediation, single-auditor bias, and audit fatigue. Implications for organizations section covers provenance infrastructure investment ($c N \ll C_R$ observed inequality), documentation as byproduct of work, internal audit independence structure, audit-frequency calibration ($\lambda T \leq K$ coverage bound), and treatment of findings as work.

**Article Number**: A223
**Completion**: 100%
**Publication Sensibility**: High (foundational analytical article that names a common substrate across otherwise-separated audit disciplines and repositions provenance as load-bearing infrastructure rather than record-keeping bureaucracy; complements existing corpus posts on documentation-oriented workflow and engineering discipline; provides explicit anchor for later posts on internal audit function design or provenance-first tooling)
**Status**: Published 2026-03-09 at 09:00 UTC. 193 lines, mathjax true, three display equations ($p = N_R / N_T$ provenance completeness, $c N \ll C_R$ contemporaneous-versus-retrofit cost inequality, $\lambda T \leq K$ audit-coverage bound). Seventeen References-section entries: seven standards documents (PCAOB, IIA, NIST SP 800-53, AICPA Trust Services Criteria, ISO 27001, GDPR, W3C PROV), two MITRE taxonomies (CWE, CVE), three related posts (A75, A76, A93), five primary research papers (Anderson 2001 security economics, Bacchelli and Bird 2013 modern code review, Buneman Khanna Tan 2001 provenance formalism, DeAngelo 1981 audit-quality theory, Simmhan Plale Gannon 2005 provenance survey). Zero em-dashes, en-dashes, contractions, prose semicolons, prose colons in prose, or prose parentheticals outside math notation. Five external URLs return 200 for AICPA, CVE, CWE, GDPR, and W3C PROV. Standards URLs verified via anti-bot patterns. Five primary DOIs verified: Buneman and DeAngelo return 200, Simmhan ACM returns 403 confirmed via SIGMOD Record mirror and Semantic Scholar, Anderson and Bacchelli return 202 IEEE DOI redirects confirmed via Semantic Scholar and archive mirrors. Editorially back-dated to fill the one-day gap between A215 (2026-03-08 steampunk and analog electronics) and A105 (2026-03-10 neuromorphic autonomous probe CPUs). Categories `philosophy management engineering` with no shadowing repository at those first-category paths. Two-commit publication pattern; commits local pending push authorisation.

### Deep-Concentration Knowledge Work (A222) — Published

**File**: `_posts/2026-03-11-deep_concentration_knowledge_work.markdown`

**Topic**: First-principles characterization of the class of knowledge workers whose productivity depends on sustained deep concentration. Standalone one-off article that rolls up one level of abstraction from engineer-specific observation to the class-level property. Identifies three defining cognitive properties: extended ramp-up ($T_r$ of order hours), sustained state across days or weeks including sleep, and external memory prostheses closing the gap $C_{\text{problem}} \gg M_{\text{working}}$. Catalogs cross-profession examples spanning software and hardware engineers, mathematicians, long-form writers, composers, experimental scientists, complex-case attorneys, top-level chess and Go players, cryptographers, and architects. Draws explicit boundary with continuous-shift knowledge work: managers, sales, operations, classroom teaching, and customer support. Formalizes interruption cost with $L(t_i) = (T_s - t_i) + T_r$ and contrasts with the manager loss $L_{\text{manager}} = t_{\text{slot}}$. Argues documentation discipline is a load-bearing consequence of the third property rather than an aesthetic preference. Sections on implications for managers and complementary implications for practitioners. Prior-art section positions the framing relative to Brooks Mythical Man-Month, Graham Maker's Schedule Manager's Schedule, Csikszentmihalyi Flow, and Newport Deep Work. Empirical claims anchored in five peer-reviewed primary references: Cowan 2001 refinement of working memory capacity to approximately four items, Leroy 2009 attention residue phenomenon after task switch, Mark Gudith Klocke 2008 CHI workplace interruption cost, Miller 1956 foundational Magical Number Seven, Rasch and Born 2013 sleep-dependent memory consolidation.

**Article Number**: A222
**Completion**: 100%
**Publication Sensibility**: High (foundational analytical article positioning class-level cognitive requirements above profession-specific manifestations; complements existing corpus posts on management and engineering discipline; provides explicit anchor for later posts on maker productivity, calendar architecture, and documentation practice)
**Status**: Published 2026-03-11 at 09:00 UTC. 199 lines, mathjax true, three display equations. Fourteen References-section entries (three books, one essay, five related posts, five primary research papers). Five cross-references to prior corpus posts (A75, A76, A86, A93, A94). Zero em-dashes, en-dashes, contractions, prose semicolons, prose colons in prose, or prose parentheticals outside math notation. Nine external URLs verified (five 200 responses for Cowan, Leroy, Brooks, Graham, Newport, plus four 403 responses for HarperCollins, Miller APA, Mark ACM, and Rasch Born APS matching the documented publisher anti-bot pattern with all four confirmed indexed via web search). Editorially back-dated to fill the one-day gap between A105 (2026-03-10 neuromorphic autonomous probe CPUs) and A103/A106 (2026-03-12 error correction recursion and delta wing vehicles). Categories `philosophy management engineering` with no shadowing repository at those first-category paths. Two-commit publication pattern; commits local pending push authorisation.

### Rocket Propellant Chemistry series (A217-A221) — Published

**Files**:
- `_posts/2026-02-01-rocket_propellant_chemistry_a_design_tradeoff_space.markdown` (A217)
- `_posts/2026-02-02-rocket_propellant_chemistry_solid_propellants.markdown` (A218)
- `_posts/2026-02-03-rocket_propellant_chemistry_cryogenic_liquid_propellants.markdown` (A219)
- `_posts/2026-02-04-rocket_propellant_chemistry_storable_and_hypergolic_liquid_propellants.markdown` (A220)
- `_posts/2026-02-05-rocket_propellant_chemistry_hybrid_propellants.markdown` (A221)

**Topic**: Five-article back-dated series on rocket propellant chemistry with editorial dates 2026-02-01 through 2026-02-05 filling the open block between `_posts/2026-01-31-claude_code_getting_started.markdown` and `_posts/2026-02-06-bidirectional_agentic_workflow.markdown`. A217 opens the series as a design-tradeoff space article establishing the vocabulary the family articles consume: specific impulse, effective exhaust velocity, thrust equation, ideal specific impulse formula through chamber temperature and average molecular weight, characteristic velocity, thrust coefficient, oxidizer-to-fuel ratio, and density specific impulse. A218 covers solid propellants including composite (ammonium perchlorate with hydroxyl-terminated polybutadiene binder and aluminum fuel, with representative Space Shuttle SRB and Ariane 5 formulations), double-base (nitrocellulose and nitroglycerin), composite modified double-base with HMX, and the research frontier (ammonium dinitramide, hydroxyl-terminated polyether, aluminum hydride). A219 covers cryogenic liquid propellants including hydrolox (RS-25, RL10B-2, Vulcain 2 and 2.1, Vinci, LE-9), methalox (Raptor V2, BE-4), kerolox (F-1, Merlin 1D, RD-180, YF-100, historical Scud reference), and V-2 ethanol-oxygen historical context. Covers ortho-para hydrogen conversion, densified propellants, RP-1 specification (MIL-DTL-25576), coking constraints, five power cycles (gas generator, staged combustion fuel-rich and oxidizer-rich, full-flow staged combustion, expander, expander-bleed), and regenerative cooling. A220 covers storable and hypergolic liquid propellants including nitrogen tetroxide with monomethylhydrazine (R-40, R-4D, OMS), unsymmetrical dimethylhydrazine (YF-20 series, RD-253), and Aerozine 50 (Titan LR87 and LR91, Apollo LM descent and ascent, Apollo SPS, Delta II AJ10-118K); inhibited red fuming nitric acid with kerosene (Scud A AK-20I, Scud B AK-27P, R-12, R-14); hydrazine monopropellant with Shell 405 iridium-alumina catalyst; concentrated hydrogen peroxide monopropellant with silver-plated screens (Me-163, X-15, Black Arrow); green monopropellants LMP-103S (ammonium dinitramide based, PRISMA 2010) and AF-M315E ASCENT (hydroxylammonium nitrate based, Green Propellant Infusion Mission 2019); hypergolic ignition mechanism; toxicity and REACH regulations. A221 covers hybrid propellants including classical HTPB fuels with liquid oxygen, paraffin-based fuels with melt-layer entrainment mechanism (Karabeyoglu Stanford Space Propulsion Group), nitrous oxide storable hybrids (SpaceShipOne, SpaceShipTwo), metallized hybrids (aluminum, alane, boron), alternative oxidizers (hydrogen peroxide, mixed oxides of nitrogen), and combustion instability classes (chuffing and thermoacoustic). Includes the Marxman-Gilbert 1963 regression rate law with pressure-independence property.

**Article Numbers**: A217 through A221 (five articles)
**Completion**: 100%
**Publication Sensibility**: High (comprehensive back-dated block treating the full chemical rocket propellant taxonomy at the level required for engine-level design choices; shared main title "Rocket Propellant Chemistry," across all five articles; ends flush at 2026-02-05 with the dense A75-A151 published block starting 2026-02-06)
**Status**: Published as batch on 2026-07-11. Total 3097 lines across five articles (A217 opener 586, A218 solid 658, A219 cryogenic 670, A220 storable 646, A221 hybrid 537). All articles mathjax true. Thirty-one display equations across the series (A217 opener 7, A218 solid 6, A219 cryogenic 6, A220 storable 6, A221 hybrid 6) covering propulsion analytics (specific impulse, ideal Isp formula, characteristic velocity, thrust coefficient, oxidizer-to-fuel ratio, optimum mixture ratio, density specific impulse, Vieille's law, temperature sensitivity, regression rate correlation) and combustion chemistry (ammonium perchlorate decomposition, aluminum combustion, ammonium dinitramide decomposition, hydrolox and methalox and kerolox and ethanol combustion, nitrogen tetroxide with monomethylhydrazine and unsymmetrical dimethylhydrazine and inhibited red fuming nitric acid with kerosene combustion, hydrazine two-step decomposition, high-test peroxide decomposition, hydroxyl-terminated polybutadiene and paraffin with liquid oxygen and with nitrous oxide combustion, nitrous oxide decomposition). All 31 display equations verified balanced. Zero em-dashes, en-dashes, contractions, prose semicolons, or certification vocabulary series-wide. Twenty post_url cross-references across the series, all resolve at batch publication. Categories `aerospace propulsion chemistry` uniform. Reference URL verification complete: Sutton and Biblarz Wiley 200; AIAA URLs (Chiaverini and Kuo, Huzel and Huang, Kuo and Summerfield, Sutton History, Yang et al.) 403 anti-bot pattern with all confirmed indexed via web search; Kubota Wiley Online Books 403 anti-bot with indexed confirmation; Davenas ScienceDirect 403 anti-bot with indexed confirmation; Karabeyoglu et al. Journal of Propulsion and Power 18 2002 confirmed indexed via Stanford PDF and ResearchGate; Marxman and Gilbert Symposium International on Combustion 9 1963 DOI 200; Clark Ignition Rutgers 200. Next available article number after publication: A222.

### Keleusma's Self-Hosting Strategy (A216) — Published

**File**: `_posts/2026-07-11-keleusma_self_hosting_strategy.markdown`

**Topic**: Public-facing summary of Keleusma's V0.3.0 self-hosting strategy, adapted from two internal documents (`docs/reference/INCREMENTAL_SELF_HOSTING.md` and `docs/roadmap/V0_3_0_SELF_HOSTING.md`). Covers the backward incremental migration method (Fowler strangler pattern run backward with the emit boundary retired first, a single moving adapter at the frontier, adapters as throwaway prototypes, a deferral ledger, the completion gate, decomposing large stages), the three-stage stream-processor pipeline architecture (lexer, parser, codegen each a Keleusma `loop` function matching Brinch Hansen's pipeline-of-processes model), the integrated single-pass Wirth-tradition alternative that the strategy documents but does not recommend, the bootstrap fixed-point procedure (Phase A cross-compile, Phase B self-compile, Phase C fixed point with kelc.0 through kelc.2 artifacts), three surface-language tensions with resolutions (recursion via explicit work-stacks, Hindley-Milner via per-function bounded inference, generics via lazy specialization tables), resolved design questions (R3.1 through R3.5, R5.3), open questions (cross-module monomorphization, diagnostic quality bound, V0.2 surface adequacy audit), prior art lineage (Brinch Hansen 1985, Wirth Compiler Construction 1996 and Project Oberon 1992/2013, Turbo Pascal 1983-1986, CakeML, Thompson Reflections on Trusting Trust 1984 CACM, Wheeler Diverse Double-Compiling 2009), lessons from the contemporary brief-lang partial self-hosting attempt, and nine success criteria for V0.3.0 completion. Explicit note that the C-family multi-pass tradition (GCC, Clang, PCC, lcc) is not relevant prior art. Cross-references A199 streaming compilers series conclusion, A204 self-hosted silicon compiler, A206 PL theory arc opener, A205 Keleusma 0.2.2 getting started.

**Article Number**: A216
**Completion**: 100%
**Publication Sensibility**: High (public-facing summary of the strategy that the Keleusma corpus has been building toward across the compilers series, the HDL series' A204 silicon self-hosting article, and the V0.2.2 getting-started article's mention of the compiler subproject scaffold; establishes the V0.3.0 architectural target in a form readers outside the project can follow)
**Status**: Published 2026-07-11 at 09:00 UTC. 1616 lines, mathjax false, zero display equations. Two ASCII diagrams (moving-seam picture and three-stage pipeline). Approximately fifteen inline code notations covering file paths, artifact names, function categories, host natives, and data-structure names. All numeric quantities in prose spelled out per corpus convention. Zero em-dashes, en-dashes, contractions, prose semicolons, or certification vocabulary. Four post_url cross-references, all resolve. Fifteen external URLs verified with curl (ACM 403 as expected per corpus URL-verification patterns). Internal Keleusma document URLs pinned to the main branch (both files exist there; INCREMENTAL_SELF_HOSTING.md was added post-v0.2.2 tag so v0.2.2 blob URLs would 404). Categories `keleusma compilers self-hosting`. Two-commit publication pattern; commits local pending push authorisation.

### Developments in Programming Language Theory series (A206-A215) — Published

**Files**:
- `_posts/2026-03-27-programming_language_theory_as_a_historical_arc.markdown` (A206)
- `_posts/2026-03-28-foundations_before_1960.markdown` (A207)
- `_posts/2026-03-29-the_1960s.markdown` (A208)
- `_posts/2026-03-30-the_1970s_part_i.markdown` (A209)
- `_posts/2026-03-31-the_1970s_part_ii.markdown` (A210)
- `_posts/2026-04-01-the_1980s.markdown` (A211)
- `_posts/2026-04-02-the_1990s.markdown` (A212)
- `_posts/2026-04-03-the_2000s.markdown` (A213)
- `_posts/2026-04-04-the_2010s.markdown` (A214)
- `_posts/2026-04-05-the_2020s_to_mid_2026.markdown` (A215)

**Topic**: Ten-article historical arc covering developments in programming language theory from Alonzo Church's lambda calculus of the nineteen thirties to the current state of practice in mid two thousand twenty-six. A206 opens the series as a scaffold framing the seventy-year arc and identifying eight recurring threads (type systems, semantics, effect systems, information-flow control, refinement types, dependent types, coroutines and productivity, totality analysis) that the era articles develop. A207 covers pre-nineteen-sixty foundations (Church, Turing, Curry-Schönfinkel, Kleene, von Neumann, FORTRAN, LISP, ALGOL 58, ALGOL 60). A208 covers the nineteen sixties (LISP consolidation, Simula and OOP origins, Landin's SECD/ISWIM, McCarthy's mathematical theory, ALGOL 68, structured programming, Hoare's axiomatic method, Scott-Strachey denotational semantics). A209 covers the pragmatic side of the nineteen seventies (structured programming settled, denotational semantics maturation, Dijkstra's discipline, Pascal, C, Prolog, Concurrent Pascal, Modula, Backus's Turing Award critique of von Neumann style). A210 covers the theoretical side of the nineteen seventies (POPL founding, Hindley principal types, Milner LCF and first ML, Martin-Löf type theory, Curry-Howard correspondence formalization, Denning information-flow lattice). A211 covers the nineteen eighties (Prolog maturation with WAM, Standard ML research program, Miranda and Haskell precursors, category theory as working tool, Lucassen-Gifford effect systems, OOP maturation and OOPSLA founding). A212 covers the nineteen nineties (Standard ML Definition and OCaml, Haskell shipping through Haskell 98, monadic effects reaching practice, Freeman-Pfenning refinement types, Wright-Felleisen type soundness, Coq/PVS/Isabelle/HOL maturation, Andrew Myers JFlow, ICFP founding, industrial dynamic languages Java/JavaScript/Python). A213 covers the two thousands (Pierce Types and Programming Languages consolidation textbook, Coq and Agda maturation with Four Color Theorem and Agda 2, CompCert verified compilation, Rondon-Kawaguchi-Jhala Liquid Types, Siek-Taha gradual typing, HOPL III, new languages Scala/F-sharp/Clojure, dynamic language ascendancy, QuickCheck property-based testing). A214 covers the twenty tens (Rust ownership discipline reaching Rust 1.0 May 2015, F-star and Idris dependent types industrial use, Plotkin-Pretnar effect handlers maturation, Vazou Liquid Haskell as first production refinement-type system, session types entering industrial use, gradual typing reaching mainstream via TypeScript/Python/Ruby, Homotopy Type Theory book, new languages Swift/Kotlin/Elm/Elixir/Julia, WebAssembly). A215 covers the twenty twenties to mid two thousand twenty-six (HOPL IV virtual 2021, Lean 4 and Mathlib, Coq to Rocq rename 2025, OCaml 5.0 effect handlers December 2022, formal verification pipelines reaching production including CompCert Airbus and seL4 Foundation and HACL asterisk in Firefox and Windows, refinement types and information-flow labels in embedded scripting including Keleusma, WCET as first-class language property in Keleusma, new languages Zig/Roc/Verse, LLM-assisted programming language work, transition to periodic current-event surveys). Shared main title "Developments in Programming Language Theory," across all ten articles.

**Article Numbers**: A206 through A215 (ten articles)
**Completion**: 100%
**Publication Sensibility**: High (comprehensive historical arc that closes with the current moment and hands off to periodic current-event surveys; supplies context for reader interpretation of subsequent PL theory developments; every article verified against primary sources with substantial web verification pass per article)
**Status**: Published as batch on 2026-07-10. Total 14,309 lines across ten articles (A206 opener 801, A207 1153, A208 1408, A209 1478, A210 1348, A211 1260, A212 1586, A213 1675, A214 1851, A215 1749). All articles mathjax false, zero display equations, inline code notation used per article where load-bearing. Zero em-dashes, en-dashes, contractions, prose semicolons, or certification vocabulary. Sixty post_url cross-references, zero unresolved. Editorial dates 2026-03-27 through 2026-04-05 forming a consecutive-day back-dated block ending flush at 2026-04-05 one day before A188 compilers series. Categories `programming-languages theory history` uniform. Next available article number: A216.

### Getting Started with Keleusma 0.2.2 (A205) — Published

**File**: `_posts/2026-07-10-keleusma_0_2_2_getting_started.markdown`

**Topic**: Third article in the Keleusma getting-started series with A107 (0.1.1) and A110 (0.2.0). Practical walkthrough of the material additions in the 0.2.x line covering the 0.2.1 language features that 0.2.2 preserves and the 0.2.2 tooling additions. Sections cover: software versions and installation; the boolean/bitwise/shift operator families (`band`/`bor`/`bxor`/`bnot`, `lsl`/`asl`/`lsr`/`asr`, eager `and`/`or`/`xor`/`not` and short-circuit `andalso`/`orelse`); general const generics superseding the earlier `Multiword<N, F>` special case; executable shebang scripts and the script argument vector via `shell::arg` and `shell::arg_count`; debug `assert` statements with strippable debug-record backing; partial-operation handling for checked arithmetic and array indexing and refinement-newtype construction; strippable debug metadata via `keleusma compile --debug` and `keleusma strip`; operator-configured strict-mode deployment policy for signed and encrypted bytecode; an Under the Hood section covering the flat-byte composite runtime representation, the typed operand-stack verifier pass, and trait-method resolution on generic structs; and 0.2.2-specific coverage of the self-hosted-compiler subproject scaffold, the learning guide migration to a bilingual mdbook served at `https://sgeos.github.io/keleusma/`, and the browser-based playground at `https://sgeos.github.io/keleusma/playground/` that compiles and verifies programs through a WebAssembly build of the compiler.

**Article Number**: A205
**Completion**: 100%
**Publication Sensibility**: High (companion to A107 and A110 aligned with the 0.2.2 release, every code listing verified against an installed 0.2.2 CLI producing byte-identical outputs to the 0.2.1 verification pass)
**Status**: Modified 2026-07-10 to cover 0.2.2 in place of 0.2.1 following the 2026-07-09 tag of Keleusma 0.2.2. File renamed via `git mv` from `2026-07-09-keleusma_0_2_1_getting_started.markdown` to `2026-07-10-keleusma_0_2_2_getting_started.markdown`. Editorial date advanced from 2026-07-09 12:00 UTC to 2026-07-10 12:00 UTC to reflect the V0.2.2 test date. 852 lines, mathjax false, zero display equations. All code listings re-executed against an installed `keleusma 0.2.2` and outputs recorded verbatim. Every V0.2.1 example produces identical output under V0.2.2 with byte-identical compiled bytecode confirming V0.2.2 preserves V0.2.1 semantics. Cross-references A107, A110, A109 (verifiable control kernel), A111 (information-flow control deep dive), A199 (streaming compilers conclusion), and A204 (self-hosted silicon compiler). Categories `rust embedded programming`. External URLs updated to the `v0.2.2` tag and the hosted mdbook and playground URLs. A206 and A215 cross-references updated to `related_post_keleusma_022` from `related_post_keleusma_021`.

### The Self-Hosted Silicon Compiler (A204) — Published

**File**: `_posts/2026-07-09-self_hosted_silicon_compiler.markdown`

**Topic**: Fifth article completing the five-article HDL and manufacturing thread with A200 (history), A201 (design space), A202 (meta-factory), and A203 (state of the practice). Addresses the specific integration point between the computational and manufacturing halves of the reproduction loop identified in A201 and A202. Sections cover: definition of self-hosting for silicon compilation (narrow silicon compiler translation, strong vs weak self-hosting forms, dependency reduction and reproduction-loop rationales); software bootstrap precedent citing A199 fixed-point condition, Ken Thompson's 1984 Turing Award lecture Reflections on Trusting Trust published in CACM Vol 27 No 8 August 1984, and David A. Wheeler's 2009 Diverse Double-Compilation countermeasure; Gabriel Somlo's Trustworthy Free Libre Linux-Capable Self-Hosting sixty-four-bit RISC-V Computer at Carnegie Mellon University Software Engineering Institute as strongest existing demonstration with Rocket Chip RISC-V core on LiteX system-on-chip on Lattice ECP5 field-programmable-gate-array with Yosys and Project Trellis and nextpnr toolchain running Fedora Linux; silicon boundary distinguishing what current self-hosting reaches versus what remains below the fabrication boundary; research directions toward compact self-hosting toolchains including Silice minimal grammar by Sylvain Lefebvre at INRIA and Keleusma design-in-progress software-target example and on-fabric compilation acceleration and bootstrap procedure design; applications in trust-adjacent computing citing Wheeler DDC use case and educational contexts and long-term autonomy contexts and reproducible-builds hardware distribution; meta-factory connection tying computational self-hosting to A202's mechanical prior art including brief mention of three additional required system components (materials refinery, kinematic fabricator, meta-cognitive orchestration). Two publication-review hedges applied: Yosys source size softened from specific one-hundred-thousand-lines figure to on-the-order-of-several-hundred-thousand-lines directional claim, and Somlo/DDC connection softened to note Somlo references DDC as related mitigation rather than as integrated bootstrap component.

**Article Number**: A204
**Completion**: 100%
**Publication Sensibility**: High (closes the five-article HDL and manufacturing thread with the specific integration point that ties the computational and manufacturing halves of the reproduction loop, grounded in Somlo's substantial existing work rather than speculation)
**Status**: Published 2026-07-09 (editorial date, tomorrow). 1805 lines, mathjax false, zero display equations. Historical and technical claims verified against primary sources including Thompson CACM 1984, Wheeler arxiv 2010, Somlo CMU SEI project pages, and Wikipedia bootstrapping compilers article. Keleusma named directly with design-in-progress framing. Von Neumann probe named once with explicit decline to develop interstellar case. Categories `hdl hardware self-hosting`.

### Hardware Description Languages, the State of the Practice (A203) — Published

**File**: `_posts/2026-07-08-hardware_description_languages_state_of_the_practice.markdown`

**Topic**: Third article in the HDL thread completing the three-time-frame survey with A200 (history) and A201 (design space). State-of-the-practice framing covering industrial mainstream landscape (Verilog/VHDL split with regional patterns, SystemVerilog absorption for new work, SystemC in system-level modelling, Bluespec in specialised niches), vendor toolchain landscape (AMD Vivado post-2022 Xilinx acquisition, Intel Quartus with 2015 Altera acquisition and 2025 Silver Lake divestiture, Synopsys Synplify, Cadence, Siemens EDA), open-source toolchain landscape (Yosys started 2012 at Vienna University of Technology by Claire Wolf, nextpnr, F4PGA formerly SymbiFlow, Project IceStorm), embedded-DSL revival adoption (Chisel with Rocket Chip generator and SiFive founded 2015 by Asanović/Lee/Waterman from UC Berkeley and FireSim FPGA-accelerated simulation, Amaranth with LiteX system-on-chip generators, SpinalHDL with VexRiscv soft processor, Clash in Haskell research groups, MyHDL in educational contexts), formal verification adoption citing Wilson Research Group 2024 study for growth from approximately thirty percent to sixty percent over a decade and industrial platforms JasperGold VC Formal Questa Formal alongside academic Kami and Koika from Chlipala's MIT PLV group, additional and emerging languages (Silice by Sylvain Lefebvre at INRIA France with Doom-on-ECP5 demonstration, DFHDL Scala-based multi-abstraction dataflow HDL, LiteX Migen family, PyMTL from Cornell), domain-specific adoption patterns for automotive/aerospace safety-critical segments and consumer/mobile and RISC-V processor design and academic computer architecture and hobbyist/open-source contexts, closing adoption trajectory synthesising the persistent Verilog/VHDL mainstream with gradual SystemVerilog absorption plus growing formal verification integration plus maturing open-source toolchain device-family coverage. Wilson Research Group 2024 first-silicon success rate figure (approximately fourteen percent) cited as evidence of design-complexity forcing function. Keleusma not named because state-of-the-practice framing does not include design-in-progress language.

**Article Number**: A203
**Completion**: 100%
**Publication Sensibility**: High (completes the three-time-frame HDL survey started with A200 and A201, brings distinct current-adoption content and Wilson Research Group 2024 verification study data that A200 and A201 did not cover)
**Status**: Published 2026-07-08 at 12:00 UTC to sequence after A202 which was 09:00 UTC on the same date. 1763 lines, mathjax false, zero display equations. Three publication-review corrections applied: Intel-Altera timeline; SiFive founders named; Wolf name updated to current Claire Wolf. Categories `hdl hardware adoption`.

### The Meta-Factory, Prior Art and the Reproduction Loop (A202) — Published

**File**: `_posts/2026-07-08-meta_factory_prior_art_and_the_reproduction_loop.markdown`

**Topic**: Companion article to A201 covering the physical-reproduction side of the reproduction loop that A201's self-hosted synthesis toolchains occupy on the computational side. Historical prior-art survey across four traditions: von Neumann's Universal Constructor from Theory of Self-Reproducing Automata edited by Arthur W. Burks and published posthumously by University of Illinois Press in 1966; the 1980 NASA studies including von Tiesenhausen and Darbro TM-78304 at Marshall Space Flight Center in July 1980 and the NASA-ASEE Summer Study proceedings published as CP-2255 edited by Freitas and Gilbreath in November 1982 with the 150-page self-replicating lunar factory chapter proposing a 20-year development program; Freitas and Merkle's 2004 Kinematic Self-Replicating Machines from Landes Bioscience with its 137-dimensional design-space taxonomy funded by Zyvex; RepRap project by Adrian Bowyer at University of Bath from 23 March 2005 with first self-print 13 September 2006 and Darwin first-generation printer at London Science Museum; industrial digital-twin meta-factories exemplified by Hyundai Motor Group Innovation Center Singapore on NVIDIA Omniverse platform. Closing section synthesises with A201 recording that both computational and mechanical sides of the reproduction loop have established prior art, with remaining engineering work being integration rather than invention. Keleusma named briefly with design-in-progress framing and explicit note that meta-factory prior art does not depend on any specific programming language. Von Neumann probe named once with explicit decline to develop the interstellar case. High-assurance embedded control substituted for scrubbed certification-adjacent framing.

**Article Number**: A202
**Completion**: 100%
**Publication Sensibility**: High (companion to A201 grounded in substantial engineering literature rather than speculation, extends the HDL-and-reproduction thread to the manufacturing side of the loop)
**Status**: Published 2026-07-08 (back-dated by one day for tomorrow's scheduled publication). 1465 lines, mathjax false, zero display equations. Historical attributions verified against Wikipedia, NASA NTRS, molecularassembler.com, RepRap project pages, and NVIDIA press releases. Two hedges applied during publication review. Categories `manufacturing self-replication history`.

### The Design Space for Next-Generation Hardware Description Languages (A201) — Published

**File**: `_posts/2026-07-07-design_space_next_generation_hardware_description_languages.markdown`

**Topic**: Companion to A200 covering the design space for next-generation hardware description languages. Four pain points in current industrial HDL flows (pipeline timing verification, clock-domain crossing, area budget verification, deadlock and livelock verification). Treatment of what the embedded-DSL revival languages (Chisel, SpinalHDL, Amaranth, Clash) address and what they leave open. Four further design levers drawn from adjacent programming-language traditions: static WCET analysis with Keleusma as software-target example, totality and productivity as type-system properties with Kami and Koika at MIT as formal-verification-integrated HDL demonstrations, coroutine primitives for clock-domain crossing, and static memory footprint analysis. Self-hosted synthesis toolchains treatment via Yosys, nextpnr, and F4PGA formerly SymbiFlow as production-adjacent open-source flow. Closer on cross-domain description languages composing hardware description with system-level requirements (SysML v2), multi-domain physical modelling (Modelica), and constructive geometry (OpenSCAD, CadQuery). Keleusma named directly, treated as design-in-progress example implementing software-target analogs of three of the four design levers. Von Neumann probe named once as speculative literature, article declines to develop the case. High-assurance embedded control terminology substituted for scrubbed certification-adjacent framing. Zero display equations because the design-space survey does not have load-bearing quantitative claims.

**Article Number**: A201
**Completion**: 100%
**Publication Sensibility**: High (companion to A200 grounded in the same lineage, extending A200's historical treatment into current-decade design-space analysis)
**Status**: Published 2026-07-07. 1585 lines, mathjax false, 24 references including inline citations to Kami, Koika, F4PGA, Yosys, nextpnr, SysML v2, Modelica, and CDC pragmatic-formal-verification work. Historical and technical claims verified against primary sources including MIT CSAIL PLV project page, PLDI 2020 paper, OMG press release, and open-source project documentation. Categories `hdl hardware design`.

### A History of Hardware Description Languages (A200) — Published

**File**: `_posts/2026-03-13-history_of_hardware_description_languages.markdown`

**Topic**: One-off history of hardware description languages across five decades. Three-era organisation: academic prototypes 1970-1984 (ISPS at Carnegie Mellon under Barbacci, KARL at Kaiserslautern under Hartenstein, ELLA at RSRE UK); commercial standardisation era 1984-2010 (Verilog developed by Goel, Moorby, and Huang at Automated Integrated Design Systems/Gateway 1983-1984 and standardised as IEEE 1364 in 1995; VHDL developed by Intermetrics, Texas Instruments, and IBM under US Air Force VHSIC contract 1983 and standardised as IEEE 1076 in 1987; SystemVerilog by Accellera 2002 as IEEE 1800 in 2005; SystemC originated at Synopsys 1999 and standardised as IEEE 1666 in 2005; Bluespec by Arvind and Hoe at MIT late 1990s, commercialised by Bluespec Inc. co-founded by Arvind Mithal and Joe Stoy in 2003); and embedded-DSL revival 2010-present (Chisel by Asanović's Par Lab team at Berkeley 2012 including Lee and Waterman who also originated RISC-V; SpinalHDL by Papon 2015; Amaranth originally called nMigen by whitequark December 2018, renamed December 2021, succeeding Bourdeauducq's Migen from 2007; MyHDL by Decaluwe 2003; Clash by Baaij at Utrecht and Delft). Verification language track (PSL/IEEE 1850, SVA, UVM/IEEE 1800.2) and high-level synthesis track (behavioural Verilog/VHDL, SystemC HLS via Vivado and Catapult, domain-specific HLS). Closes with observations on formal-methods integration, machine-learning-driven design synthesis, open-source industrial tooling via Yosys, and domain-specific hardware description as the emerging next wave. One display equation formalising Moore's Law $N(t) = N_0 \cdot 2^{t/T}$ as the design-complexity forcing function that repeats at each historical wave.

**Article Number**: A200
**Completion**: 100%
**Publication Sensibility**: High (comprehensive one-article treatment of the HDL space, covering the full lineage from academic prototypes through modern embedded-DSL revival with primary-source-verified attributions)
**Status**: Published 2026-03-13 (back-dated). 1903 lines, one display equation, mathjax enabled. Six substantive attribution corrections applied during publication review after WebSearch verification against Wikipedia and project homepages. Categories `hdl hardware history`.

### Stream-Based Compilers series (A188-A199) — Published

**Files**:
- `_posts/2026-04-06-compilation_as_streaming_discipline.markdown` (A188)
- `_posts/2026-04-07-wirth_single_pass_line.markdown` (A189)
- `_posts/2026-04-08-turbo_pascal_closed_source_demonstration.markdown` (A190)
- `_posts/2026-04-09-brinch_hansen_pipeline_of_processes.markdown` (A191)
- `_posts/2026-04-10-block_structured_single_pass_validation.markdown` (A192)
- `_posts/2026-04-11-coalgebraic_productivity_stream_processor_analogy.markdown` (A193)
- `_posts/2026-04-12-fixup_tables_forward_jump_problem.markdown` (A194)
- `_posts/2026-04-13-declare_before_use_forward_declarations.markdown` (A195)
- `_posts/2026-04-14-symbol_tables_scope_popping_bounded_memory.markdown` (A196)
- `_posts/2026-04-15-integrated_single_pass_versus_decomposed_pipeline.markdown` (A197)
- `_posts/2026-04-16-when_multi_pass_wins.markdown` (A198)
- `_posts/2026-04-17-stream_processor_as_compiler_and_compiler_as_stream_processor.markdown` (A199)

**Topic**: Twelve-article series on the stream-processor compilation discipline. Covers the historical demonstrations (Wirth's PL/0 through Oberon line, Turbo Pascal as the closed-source commercial demonstration, Brinch Hansen's pipeline-of-processes architecture and SuperPascal self-hosting), the mathematical foundation (block-structured control flow with the WebAssembly single-pass validator per Haas et al. PLDI 2017 and Watt's Isabelle mechanisation; coalgebraic productivity per Rutten's universal-coalgebra treatment and stream calculus, with the Endrullis decidability result, the Abel-Pientka copattern framework, and Turner's total functional programming), the engineering techniques (fixup tables with the forward-jump problem, declare-before-use ordering with forward declarations for mutual recursion, scoped symbol tables with the scope-popping discipline), the architectural synthesis (integrated single-pass versus decomposed pipeline compared head-to-head with Keleusma V0.3.0 as modern worked example; when multi-pass wins covering whole-program optimisation, Hindley-Milner unification, type-class resolution, and metaprogramming), and the series closer (the compiler as stream processor and the stream processor as compiler, with the Keleusma five-stage compilation pipeline formalised as function composition and its compositional working-memory bound derived from the WCMU analysis). Historical claims flagged with epistemic markers throughout, especially A190 Turbo Pascal treatment where the compiler internals were never released as open source. Keleusma treatment consistently frames V0.3.0 self-hosting as design-in-progress rather than shipped result. MathJax enabled throughout.

**Article Numbers**: A188 through A199 (twelve articles)
**Completion**: 100%
**Publication Sensibility**: High (comprehensive treatment of the stream-processor compilation discipline as a distinct architectural tradition, with rigorous mathematical foundation from coalgebraic productivity theory, engineering technique specifications, and modern realisation via Keleusma's pipeline)
**Status**: Published 2026-04-06 through 2026-04-17 (back-dated, landing flush with the two-dimensional projection in games series at 2026-04-18). Total ~14,273 lines and ~90 display equations across twelve articles. Historical trio A189-A191, theory pair A192-A193, techniques trio A194-A196, synthesis pair A197-A198, opener A188 and closer A199.

### Two-Dimensional Projection in Games series (A173-A187) — Published

**Files**:
- `_posts/2026-04-18-two_dimensional_projection_as_a_coordinate_mapping_problem.markdown` (A173)
- `_posts/2026-04-19-top_down_projection_without_height.markdown` (A174)
- `_posts/2026-04-20-top_down_with_decoupled_vertical_axis.markdown` (A175)
- `_posts/2026-04-21-side_scrolling_without_depth.markdown` (A176)
- `_posts/2026-04-22-side_scrolling_with_parallax_layers.markdown` (A177)
- `_posts/2026-04-23-belt_scroll_side_scrolling_with_explicit_depth.markdown` (A178)
- `_posts/2026-04-24-oblique_projection_and_quarter_view.markdown` (A179)
- `_posts/2026-04-25-axonometric_projection_isometric_dimetric_trimetric.markdown` (A180)
- `_posts/2026-04-26-mode_7_and_affine_ground_plane.markdown` (A181)
- `_posts/2026-04-27-sprite_scaling_pseudo_three_dimensional.markdown` (A182)
- `_posts/2026-04-28-raycasting_two_dimensional_map_rendered_as_three_dimensions.markdown` (A183)
- `_posts/2026-04-29-stylised_and_hybrid_projections_inconsistent_frame.markdown` (A184)
- `_posts/2026-04-30-draw_order_y_sort_z_sort_and_painters_algorithm.markdown` (A185)
- `_posts/2026-05-01-picking_and_hit_testing_in_pseudo_three_dimensional_projections.markdown` (A186)
- `_posts/2026-05-02-camera_as_linear_operator_affine_and_projective_synthesis.markdown` (A187)

**Topic**: Fifteen-article series on two-dimensional projection in games, covering the math of translating internal world coordinates (2D, pseudo-3D with layer-based depth, and 3D) to screen space, and translating screen-space input back into world space. Organised into six clusters: A173 opener (Two-Dimensional Projection as a Coordinate Mapping Problem framing the forward map and inverse map duality, the math-versus-delivery distinction, and the series roadmap); A174-A178 Cartesian cluster (top-down without height as the floor case, decoupled vertical axis with shadow drop, side-scrolling without depth, side-scrolling with parallax layers, belt-scroll with explicit depth); A179-A180 oblique-and-axonometric cluster (oblique cabinet/cavalier projection with quarter view, axonometric with isometric/dimetric/trimetric variants); A181-A184 affine-and-projective cluster (Mode 7 per-scanline affine ground plane, sprite scaling pseudo-three-dimensional including Battle Clash and Metal Combat, raycasting with fisheye correction, stylised hybrid projections with the Mother lineage and Limbo/Inside stylised post-processing); A185-A186 cross-cutters (draw order with Painter's Algorithm and Y-sort/Z-sort/hybrid sort criteria, picking and hit testing with condition number bounds and the canonical sprite-scale-and-rotate light-gun hit test); A187 synthesis closer (the camera as linear operator showing the PVM pipeline and recovering each previous projection mode as a restricted case of the modern graphics-processing-unit pipeline). Each article carries the standard projection-mode template (Brief History, Forward Map, Inverse Map, Worked Example, Variations Within the Mode, Delivery Mechanisms, Where the Framing Breaks Down, Canon, Out of Scope, Conclusion, References), with appropriate variations for the opener, cross-cutters, and synthesis closer. The y-down depth-into-screen convention is established in A174 and carried throughout the series. MathJax enabled throughout.

**Article Numbers**: A173 through A187 (fifteen articles)
**Completion**: 100%
**Publication Sensibility**: High (a comprehensive series treating every major two-dimensional projection mode in commercial games, with cross-cutting articles on draw order and picking and a synthesis closer that ties the series to the modern projective pipeline)
**Status**: Published 2026-04-18 through 2026-05-02 (back-dated, landing flush with the patent and startup strategy series at 2026-05-03). Total ~14,640 lines, ~343 display equations, ~1,144 inline expressions, ~106 unique references across the fifteen articles. Forward references in prose to be converted to {% post_url %} Liquid tags in a follow-up pass.

### Venus Cloudtop Buoyant Analog — Published

**File**: `_posts/2026-07-06-venus_cloudtop_buoyant_analog.markdown`
**Topic**: Eighth and final per-subsystem deep-dive in the analog-facilities category following A152 through A159, closing the series at the most conspicuous gap A152 identified (the buoyant cloudtop habitat for Venus). Uses the framing that the buoyancy condition is the architectural keystone, with envelope volume, internal atmosphere mass, structural mass, operating altitude band, and subsystem mass budget all dimensioned against the density differential between the internal Earth breathing-mix atmosphere and the external Venus CO2 atmosphere. Derives buoyancy from first principles with worked example at ~6,320 kg total mass for four-crew habitat requiring ~10,500 m^3 envelope at 55 km altitude. References Landis 2003 Colonization of Venus paper and NASA Langley HAVOC 2014-2015 concept. Includes a dedicated synthesis section walking each of the seven prior subsystem articles and explaining how its architectural keystone adapts to the Venus cloudtop context (electricity benefits from 1.92x Earth solar irradiance, water faces sulfuric acid clouds requiring high-closure recovery, communications inherits link budget with cloud attenuation and super-rotation considerations, food benefits from abundant CO2 and high PAR, habitat envelope shifts from pressure containment to acid and UV durability, waste loses several disposition pathways and must rely on incineration and biological processing, transportation gains zero-velocity horizontal travel via super-rotation but loses surface access). Covers terrestrial stratospheric platforms (World View Stratollite, dormant Loon, Sceye, LTA Research Pathfinder, Goodyear Wingfoot) as closest available proxies, no-buoyancy architectures (Venus surface, orbit, flyby), terrestrial-only cheats, keystone-breakdown cases, and a major Series Synthesis section reviewing all eight architectural keystones across the analog-facilities series. MathJax enabled.
**Article Number**: A160
**Completion**: 100%
**Publication Sensibility**: High (closes the analog-facilities series as the planned terminus per the dirigible-last request, addresses the explicit gap from A152)
**Status**: Published 2026-07-06 (20 references; ~1,411 lines; mathjax true with 15 display equations and 28 inline expressions; series terminus)

### Garbage and Transportation for Off-Grid Space Colonization Analogs — Published

**File**: `_posts/2026-07-05-garbage_and_transportation_for_off_grid_space_colonization_analogs.markdown`
**Topic**: Seventh per-subsystem deep-dive in the analog-facilities category following A152 through A158, the penultimate article before the A160 Venus cloudtop closer. Treats transportation as the primary subject with garbage logistics as a specific use case. Uses the framing that the cargo throughput rate is the architectural keystone, with vehicle fleet sizing, route infrastructure, energy budget, and endpoint storage all dimensioned against the throughput. Derives throughput from first principles with worked 50 kg/day example, vehicle fleet sizing with worked utilisation example, rolling resistance and aerodynamic drag equations, gravitational work, energy budget for surface vehicle with 54 kWh worked example, the Tsiolkovsky rocket equation with propellant mass fraction derivation and 0.94 worked example. Walks dependent components covering vehicles (wheeled, tracked, planetary rover including corrected Apollo LRV cruise 13 km/h and 18 km/h record with Apollo 17 traverse 35.9 km, Mars rovers, NASA LTVS Lunar Outpost/Lunar Dawn/Astrolab), routes (paved, graded earth, marked, fixed-rail, no-route), energy supply (chemical, battery, hydrogen, solar), loading and unloading, endpoint storage, crew movement, garbage and bulk solid waste transport with pickup frequency equation. Transportation modes summary with comparative analysis. Covers no-transportation architectures (point-of-use disposition, drop-shipment, self-propelled cargo), terrestrial-only cheats (public road network, commercial freight, refuelling), space-only options (orbital manoeuvre, suborbital hopping, lunar/Mars surface rovers, sample return, electromagnetic launch). Closes on three cases where the keystone framing breaks down (zero-throughput closed colony, surge regime, catastrophic failure). Generalisation section walks residential homestead, remote research station with Antarctic traverse, disaster relief, mining/oilfield camp, maritime vessel under IMO, and forward operating base. MathJax enabled.
**Article Number**: A159
**Completion**: 100%
**Publication Sensibility**: High for the space-themed cluster (seventh per-subsystem article continues the deep-dive cadence under A152's nine-subsystem roadmap, penultimate to the A160 Venus cloudtop closer)
**Status**: Published 2026-07-05 (18 references; ~1,404 lines; mathjax true with 19 display equations and 26 inline expressions)

### Waste and Sewage Management for Off-Grid Space Colonization Analogs — Published

**File**: `_posts/2026-07-04-waste_and_sewage_management_for_off_grid_space_colonization_analogs.markdown`
**Topic**: Sixth per-subsystem deep-dive in the analog-facilities category following A152 through A157. Treats the waste subsystem under the framing that the waste mass balance is the architectural keystone, with stream classification, treatment train selection, storage capacity, regulatory compliance, and disposition pathway all dimensioned against the per-crew per-day waste production rate. Distinguishes itself from A154 by treating the broader waste universe (solid waste, food packaging, hazardous waste, atmospheric trace contaminants, regulated streams) beyond the water-recovery overlap. Derives mass balance from first principles with worked example for a four-crew habitat producing approximately twenty kilograms per day total waste, storage volume of 5.4 cubic metres at fifty percent closure across six-month disposition cadence, and disposition mass flux. Walks dependent components covering stream classification (urine, faeces, food preparation waste, packaging, hazardous, atmospheric), collection subsystem with vacuum-flow toilet, treatment train (vapour compression distillation, composting, anaerobic digestion, incineration with corrected 5 to 10 percent ash residue, plasma pyrolysis, mechanical compactor with compaction ratio equation and Heat Melt Compactor reference), storage, disposition pathways (destructive reentry, return-to-Earth, incineration, regolith burial, vacuum venting under planetary protection, biological processing, recycling), hazardous waste handling under RCRA, and atmospheric waste handling. Treatment technologies section covers carbon dioxide removal through lithium hydroxide canister with stoichiometric mass ratio derivation, regenerable amine swing-bed Carbon Dioxide Removal Assembly, Sabatier reactor with reaction equation, Bosch reactor with reaction equation, trace contaminant control, particulate filtration, and composting/anaerobic digestion. Covers no-treatment architectures (storage-only with linear storage scaling equation, dump-and-forget, vacuum-vent), terrestrial-only cheats (municipal sewer, curbside trash, hazardous waste transporter), and space-only options (destructive reentry, regolith burial citing 96 Apollo lunar waste bags, vacuum venting under COSPAR, in-situ resource recovery). Closes on three cases where the keystone framing breaks down (short-duration mission, upset event surge, heavily regulated waste regime). Generalisation section walks residential homestead, remote research station with Madrid Protocol coverage, disaster relief, maritime vessel with MARPOL coverage, and forward operating base. MathJax enabled.
**Article Number**: A158
**Completion**: 100%
**Publication Sensibility**: High for the space-themed cluster (sixth per-subsystem article continues the deep-dive cadence under A152's nine-subsystem roadmap, while doubling as a general off-grid waste and sewage management guide for terrestrial use cases)
**Status**: Published 2026-07-04 (18 references; ~1,505 lines; mathjax true with 15 display equations and 21 inline expressions)

### Habitat and Physical Operations for Off-Grid Space Colonization Analogs — Published

**File**: `_posts/2026-07-03-habitat_and_physical_operations_for_off_grid_space_colonization_analogs.markdown`
**Topic**: Fifth per-subsystem deep-dive in the analog-facilities category following A152, A153, A154, A155, and A156. Treats the habitat layer under the framing that the habitable pressure envelope is the architectural keystone, with structural mass, airlock cycling, thermal boundary, radiation shielding, micrometeoroid shielding, and interface penetrations all dimensioned against the envelope. Derives habitable volume sizing, differential pressure across the envelope, cylindrical and spherical pressure vessel stress equations, required wall thickness with safety factor and worked example at 8.7 mm for a 4-metre radius aluminium habitat, structural mass equation, thermal heat loss equation with worked 3.2 kW for a Mars surface habitat, airlock gas loss with the corrected ISS Quest 4.2 m^3 crewlock and 0.4 to 1.4 kg per cycle figure, and radiation shielding attenuation. Walks dependent components in order of dependency covering pressure envelope material (rigid aluminium, inflatable BEAM and Sierra Space LIFE, 3D-printed ICON Vulcan and Olympus, subterranean, rammed-earth and regolith), interior layout with NASA HIDH per-crew volume guidance, airlocks and EVA staging including suit-port architecture, thermal control with corrected ISS 70 kW EATCS radiator capacity, radiation shielding with corrected Mars 230 mSv/year unshielded and lunar 380 to 500 mSv/year solar minimum dose figures, micrometeoroid and orbital debris Whipple shield, and interface penetrations. Covers no-pressure-envelope architectures (open-air shelter, underwater habitat, subterranean cave), terrestrial-only cheats (breathable atmosphere, natural radiation shielding, conventional building codes), space-only options (lunar lava tube habitats with Marius Hills and Mare Tranquillitatis pits, regolith burial including Mars Ice Home concept, orbital free-flying habitats including Lunar Gateway and commercial LEO destinations, inflatable surface habitats). Closes on three cases where the keystone framing breaks down (near-zero pressure differential terrestrial, external-pressure-dominated underwater, distributed-village multi-module). Generalisation section walks submarine, Antarctic winter-over, off-grid residential, disaster relief, maritime vessel, and forward operating base. MathJax enabled.
**Article Number**: A157
**Completion**: 100%
**Publication Sensibility**: High for the space-themed cluster (fifth per-subsystem article continues the deep-dive cadence under A152's nine-subsystem roadmap, while doubling as a general off-grid habitat construction and operations guide for terrestrial use cases)
**Status**: Published 2026-07-03 (25 references; ~1,568 lines; mathjax true with 21 display equations and 27 inline expressions)

### Food Production and Closed Ecological Systems for Off-Grid Space Colonization Analogs — Published

**File**: `_posts/2026-07-02-food_production_and_closed_ecological_systems_for_off_grid_space_colonization_analogs.markdown`
**Topic**: Fourth per-subsystem deep-dive in the analog-facilities category following A152, A153, A154, and A155, designed to function as a general off-grid food production guide with space-colonization as contextual flavour. Treats the food production layer under the framing that the caloric yield per square metre per day is the architectural keystone, with the cultivation area following from the daily caloric demand and the achievable yield, and the lighting power, water demand, carbon dioxide flux, nutrient supply, and harvest and storage capacity all dimensioned against the cultivation area. Derives cultivation area sizing from first principles with worked example at 120 m^2 for four crew at 3000 kcal/day on a wheat-and-soybean mix at 150 kcal per square metre per day yield. Walks the dependent components in order of dependency covering cultivation systems (soil, hydroponic, aeroponic, vertical controlled environment), lighting (natural sun, artificial LED, hybrid), climate control with CO2 enrichment, nutrient supply, harvest and storage, and waste recycling through composting, anaerobic digestion, and microbial bioreactor processing. Includes production strategies covering intensive staple horticulture, fresh produce cultivation, aquaculture and aquaponics, single-cell protein from Spirulina and Chlorella, and insect protein with feed conversion ratio comparison. Treats closed ecological system biology through BIOS-3, Biosphere 2 at approximately 80 percent caloric closure across 2000 m^2 cropping area, Yuegong-365 at approximately 80 percent food self-sufficiency, the MELiSSA C1 through C5 compartment architecture with C4a algal and C4b higher-plant split, and the NASA Controlled Ecological Life Support System Biomass Production Chamber at Kennedy Space Center. Includes no-production architectures (ISS-style shelf-stable ration import, hybrid partial production with NASA Veggie and Advanced Plant Habitat, short-duration), terrestrial-only cheats (grocery resupply, local farms, wild harvest), and space-only options (reduced Mars top-of-atmosphere flux further attenuated by atmospheric dust at the surface, lunar peaks of eternal light, lunar equatorial 14-day night, microgravity considerations through Veggie and APH, regolith and in-situ resources). Closes on three cases where the keystone framing breaks down (short-duration mission, crop failure contingency, crew dietary preference). Generalisation section walks residential homestead, remote research station, disaster relief, maritime vessel, and forward operating base. MathJax enabled.
**Article Number**: A156
**Completion**: 100%
**Publication Sensibility**: High for the space-themed cluster (fourth per-subsystem article continues the deep-dive cadence under A152's nine-subsystem roadmap, while doubling as a general off-grid food production guide for terrestrial use cases)
**Status**: Published 2026-07-02 (13 references; ~1,641 lines; mathjax true with 15 display equations and 19 inline expressions)

Fourth per-subsystem deep-dive article following A153, A154, and A155, treating the food production subsystem under the caloric-yield-as-keystone framing.

Sections covered include
opening as fourth subsystem deep-dive citing food as the longest-cycle closed-loop subsystem per A152;
generalisation framing to any off-grid food production system context;
The Caloric Yield Keystone (yield-demand mismatch, closure ratio applied symmetrically from water article);
Sizing From First Principles (cultivation area equation A_crop = N_crew × E_cal × σ / Y with worked example 120 m^2 for four-crew habitat at 3000 kcal/day at 150 kcal per square metre per day yield, daily light integral DLI = PPFD × t_photoperiod, lighting power equation P_light, water demand V_water_food = A_crop × ET_crop with 600 L/day worked example, closure ratio C_food = E_cal,produced / E_cal,consumed, makeup caloric demand equation, photosynthesis stoichiometric reaction 6 CO2 + 6 H2O to glucose plus 6 O2, mass balance equations for CO2 consumption and O2 production at 1.5 kg CO2 and 1 kg O2 per kg dry biomass);
Dependent Components in Order of Dependency (cultivation systems with hydroponic variants, lighting with photosynthetic efficiency η_photo = E_biomass / E_PAR ranging 0.5 to 3 percent field for higher plants with theoretical maxima 4.6 percent C3 and 6 percent C4 and 8 to 10 percent cyanobacteria, climate control with CO2 enrichment, nutrient supply, harvest and storage, waste recycling);
Production Strategies (intensive staple horticulture, fresh produce, aquaculture, single-cell protein, insect protein with feed conversion ratio equation);
Closed Ecological System Biology (BIOS-3 with substantial food closure varying by run, Biosphere 2 with 80 percent caloric closure, Yuegong-365 with 80 percent food self-sufficiency, MELiSSA C1-C5 architecture with C4a algal and C4b higher-plant split, NASA CELSS Biomass Production Chamber);
No-Production Architectures (shelf-stable ration, hybrid partial production, short-duration);
Terrestrial-Only Cheats (grocery resupply, local farm cooperation, wild harvest);
Space-Only Options (Mars top-of-atmosphere 43 percent reduction further attenuated by surface dust, lunar peaks of eternal light, lunar equatorial 14-day night, microgravity considerations, regolith and in-situ resources);
Where the Keystone Framing Breaks Down (short-duration mission, crop failure contingency, crew dietary preference);
Generalisation Beyond the Space Analog Context;
Out of Scope (crop physiology and breeding, soil chemistry and microbiology, aquaculture engineering, pest and pathogen management, food safety and nutrition, spaceflight crew nutrition research);
Conclusion.

Research agent verified
the NASA exploration crew caloric demand of 2000 to 3000 kcal per day with additional 500 kcal on EVA days per JSC-67378,
the wheat, potato, soybean, lettuce, Spirulina, Chlorella, and mealworm caloric densities and protein content,
the photosynthetically active radiation 400 to 700 nanometre wavelength range and the photosynthetic efficiency ranges including 0.5 to 3 percent for higher plants under field conditions with theoretical maxima 4.6 percent C3 and 6 percent C4 and 8 to 10 percent for cyanobacteria,
the daily light integral 12 to 17 mol/m^2/day for leafy greens and 20 to 30 mol/m^2/day for fruiting crops,
the LED grow light efficacy 2.5 to 3.5 micromoles per joule,
the Mars top-of-atmosphere solar flux at approximately 43 percent of Earth further attenuated by atmospheric dust at the surface,
the lunar solar constant at 1361 W/m^2 at 1 AU,
the Biosphere 2 Mission 1 80 percent caloric closure on 2000 m^2 cropping area across the 2-year 8-crew mission,
the BIOS-3 approximately 95 percent atmospheric closure with food closure varying by run,
the Yuegong-365 approximately 98 percent overall system closure with full water and oxygen recycling and approximately 80 percent food self-sufficiency,
the MELiSSA C1 anoxic thermophilic, C2 photoheterotrophic, C3 nitrifying, C4a photoautotrophic algal with Limnospira indica or Spirulina, C4b higher-plant, and C5 crew compartment architecture,
the NASA Veggie deployed April 2014 with crops including red romaine lettuce, zinnia, Mizuna, Russian kale, pak choi, dragoon lettuce, and tomato,
the NASA Advanced Plant Habitat deployed 2017 with Arabidopsis, dwarf wheat, and chile peppers in 2021,
the NASA Controlled Ecological Life Support System Biomass Production Chamber operated 1988 onward for over 1200 days at Kennedy Space Center,
the MELiSSA Pilot Plant inaugurated 4 June 2009 at UAB with the Claude Chipaux Laboratory active in 2025-2026,
the hydroponic, aeroponic, controlled environment agriculture, aquaponic, single-cell protein, and edible insect production strategies,
the USDA Organic 7 CFR Part 205, the FDA Food Code 2022 10th edition, and the FAO/WHO Codex Alimentarius,
and the CO2 enrichment 800 to 1200 ppm versus ambient 425 ppm with C3 yield uplift 40 to 100 percent and C4 yield uplift 10 to 25 percent.

Critical factual corrections applied include
the Biosphere 2 caloric closure corrected from 50 percent to approximately 80 percent across the 2000 square metre cropping area;
the Yuegong-365 food self-sufficiency clarified to 80 percent with the 98 percent figure framed as overall system closure including water and oxygen;
the BIOS-3 food closure softened from a specific 50-60 percent range to substantial food closure varying by run with the 95 percent atmospheric closure cited;
the MELiSSA C4 compartment split into C4a photoautotrophic algal (Limnospira indica or Spirulina) and C4b higher-plant per current ESA definitions;
the Mars solar irradiance qualifier clarified that the 43 percent figure is top-of-atmosphere with further attenuation by atmospheric dust at the surface;
the photosynthetic efficiency refined to 0.5 to 3 percent for higher plants under field conditions with theoretical maxima 4.6 percent C3 and 6 percent C4 and 8 to 10 percent only for cyanobacteria;
the LED efficacy range adjusted to 2.5 to 3.5 micromoles per joule (the upper end was already accurate);
URL replacements for the NASA Advanced Plant Habitat page (relocated to NASA Growing Plants in Space) and the NASA Veggie page (relocated to the Wikipedia Vegetable Production System article).

References:
12 references across Reference (9) and Related Post (4) categories.
All inline-linked per project style.
A152, A153, A154, and A155 cited via post_url as the parent and sibling articles.

### Communications and the Link Budget for Off-Grid Space Colonization Analogs — Published

**File**: `_posts/2026-07-01-communications_and_the_link_budget_for_off_grid_space_colonization_analogs.markdown`
**Topic**: Third per-subsystem deep-dive in the analog-facilities category following A152, A153, and A154, designed to function as a general off-grid communications system guide with space-colonization as contextual flavour. Treats the communications layer of the off-grid analog under the framing that the link budget is the architectural keystone, with antenna aperture, transmit power, modulation, forward error correction strength, and operating frequency all dimensioned against the required signal-to-noise margin. Derives the link budget from first principles with the Friis equation, free-space path loss, Shannon-Hartley capacity bound, parabolic antenna gain, beamwidth, Johnson-Nyquist thermal noise floor, Doppler shift, and link margin equations. Walks the dependent components in order of dependency covering antennas, transmitters and power amplifiers, receivers and low-noise amplifiers, modems and forward error correction, networking layer with IEEE 802.3 and 802.11 references, and power supply and cooling. Includes a latency, bandwidth, and protocol considerations section with delay-tolerant networking and bundle protocol. Includes no-radio-frequency architectures covering free-space optical and physical data transport (sneakernet). Includes terrestrial-only cheats and space-only options covering NASA Deep Space Network, ESA Estrack, Mars Relay Network (updated after MAVEN mission conclusion June 2026), lunar relay constellation through LunaNet and ESA Moonlight, and deep-space optical communications. Closes on three cases where the keystone framing breaks down covering solar conjunction blackout (with January 2026 most recent and early 2028 next), entry-descent-landing plasma sheath, and deep outer solar system extreme-distance regime. Includes generalisation beyond space analog covering residential cabin, remote research station, disaster relief, maritime vessel, and forward operating base use cases. MathJax enabled.
**Article Number**: A155
**Completion**: 100%
**Publication Sensibility**: High for the space-themed cluster (third per-subsystem article continues the deep-dive cadence under A152's nine-subsystem roadmap, while doubling as a general off-grid communications system guide for terrestrial use cases)
**Status**: Published 2026-07-01 (28 references; ~1,544 lines; mathjax true with 16 display equations and 27 inline expressions)

Third per-subsystem deep-dive article following A153 and A154, treating the communications subsystem of the off-grid analog under the link-budget-as-keystone framing.
Sections covered include
opening as third subsystem deep-dive identifying communications as the umbilical that connects the operational island to surrounding institutional context;
generalisation framing to any off-grid communications system context;
The Link Budget Keystone (closure problem analogous to electrical generation-load and water supply-demand mismatch);
Link Budget From First Principles (Friis equation in linear and dB form, free-space path loss with the 32.45 constant for km and MHz, parabolic antenna gain, beamwidth, Johnson-Nyquist thermal noise, Shannon-Hartley capacity bound, link margin definition, worked example for 12 GHz Ku-band geostationary uplink yielding 11 dB margin);
Dependent Components in Order of Dependency (antennas including parabolic, omnidirectional, phased array, horn; transmitters and power amplifiers with 10 to 40 percent solid-state efficiency; receivers and low-noise amplifiers with 0.8 to 1.5 dB noise figure; modems and forward error correction with BPSK at 9 dB through higher-order QAM, LDPC and turbo codes; networking layer under IEEE 802.3 Ethernet and IEEE 802.11 wireless including 802.11s mesh; power supply and cooling);
Latency, Bandwidth, and Protocol Considerations (Mars 3 to 22 minute and lunar 1.3 second light-time delay, TCP degradation under multi-minute delay, Delay-Tolerant Networking and Bundle Protocol substitution, Mars relay UHF data rates, direct-to-Earth X-band, DSOC optical demonstrator);
No-Radio-Frequency Architectures (free-space optical with terrestrial 1 to 10 Gbps over 1 km, NASA LCRD geostationary optical relay, physical data transport sneakernet);
Terrestrial-Only Cheats (broadband Internet, cellular, low Earth orbit constellations including Starlink, OneWeb, and Iridium);
Space-Only Options (NASA Deep Space Network at Goldstone, Madrid, Canberra with 70-metre and 34-metre antennas, ESA Estrack at New Norcia, Cebreros, Malarguee, Mars Relay Network with MRO, Mars Odyssey, Mars Express, ExoMars Trace Gas Orbiter after MAVEN mission conclusion June 2026, lunar relay through LunaNet and ESA Moonlight, deep-space optical communications including DSOC primary mission concluded September 2025);
Where the Keystone Framing Breaks Down (solar conjunction blackout with X-band 5 degree and Ka-band 2 to 3 degree thresholds, most recent January 2026 with next early 2028; entry-descent-landing plasma sheath; deep outer solar system Voyager regime at 160 bps from 24 billion km);
Generalisation Beyond the Space Analog Context (residential off-grid cabin, remote research station with Antarctic Starlink shift since 2022, disaster relief, maritime vessel with antenna gimbal compensation, military forward operating base);
Out of Scope (modulation and coding theory, network protocols and security, antenna engineering and EMC, spectrum allocation and regulatory compliance, quantum communications, software-defined radio architecture);
Conclusion.

Research agent verified
the Friis equation linear and dB forms,
the free-space path loss 32.45 constant for km and MHz,
the Shannon-Hartley capacity bound,
the parabolic antenna gain with aperture efficiency 0.55 to 0.70 for well-designed dishes,
the parabolic 3 dB beamwidth approximately 70 lambda over D in degrees,
the Johnson-Nyquist thermal noise N = k T B with Boltzmann constant 1.380649 times 10 to the minus 23 J/K,
the Doppler shift Delta f over f = v over c non-relativistic limit,
the NASA Deep Space Network three sites at Goldstone, Madrid, and Canberra with one 70-metre and multiple 34-metre antennas each with Madrid adding DSS-53 February 2022,
the ESA Estrack network with three deep-space 35-metre antennas and the upcoming DSA-4 at New Norcia inaugurated October 2025,
the Mars Relay Network active orbiters MRO, Mars Odyssey, Mars Express, and ExoMars Trace Gas Orbiter after MAVEN mission conclusion 3 June 2026,
the NASA Laser Communications Relay Demonstration launch 7 December 2021 with 1.244 Gbps capability and first ILLUMA-T link 5 December 2023,
the Psyche DSOC launch 13 October 2023 with first light 14 November 2023, 267 Mbps from 16 million km in December 2023, distance record from 494 million km on 3 December 2024, primary mission concluded 2 September 2025 with possible 2026 reactivation,
the Starlink 2026 figures of approximately 10,000 active satellites with 25 to 50 ms latency and 100 to 400 Mbps download,
the Iridium 66 active satellites in 6 polar planes with Iridium NEXT completed January 2019,
the Globalstar 25 second-generation satellites with announced 54-satellite expansion and Amazon acquisition agreement April 2026,
the TDRSS three generations with planned phaseout in favour of commercial relay providers,
the HF radio 3 to 30 MHz ionospheric skywave,
the VHF 30 to 300 MHz and UHF 300 MHz to 3 GHz ITU allocations,
the IEEE 802.11s mesh and the Meshtastic-style overlays on LoRa rather than LoRa itself as mesh,
the FCC Part 95 personal radio services covering FRS, GMRS, MURS, and CB,
the CCSDS Space Packet Protocol, CFDP, Proximity-1, and Space Link Extension standards,
the IEEE 802.11ax Wi-Fi 6 published February 2021, 802.11ax 6 GHz extension Wi-Fi 6E, and 802.11be Wi-Fi 7 published September 2024,
the ITU-R Radio Regulations 2024 edition entered force 1 January 2025 after WRC-23,
the CCSDS FEC codes including concatenated convolutional plus Reed-Solomon, turbo, LDPC AR4JA family, and BCH plus LDPC via DVB-S2 with polar codes used in 5G but not in current CCSDS standard suites,
the terrestrial free-space optical 500 m typical year-round availability with multi-kilometre under favourable weather,
and the Mars solar conjunction January 2026 most recent with next opposition February 2027 and next superior conjunction approximately early 2028.

Critical factual corrections applied:
MAVEN removed from active Mars relay list with the mission conclusion announced 3 June 2026 explicitly noted;
the DSOC primary mission framed as concluded September 2025 with the November 2023 first link at 267 Mbps from 16 million km, the December 2024 distance record from 494 million km, and the possible reactivation under consideration following the May 2026 Mars flyby;
the solar conjunction blackout specification expanded with X-band Sun-Earth-Probe angle below approximately five degrees and Ka-band below approximately two to three degrees;
the Mars solar conjunction schedule corrected with the most recent January 2026 and next early 2028 rather than late 2026 to early 2027;
the polar codes removed from CCSDS-standard list with LDPC and concatenated turbo codes substituted;
URL replacements for the NASA Deep Space Network page (relocated to Wikipedia), the LCRD page (Wikipedia), the LunaNet page (Wikipedia), the FCC root (Wikipedia), and the Space Telecommunications Radio System (Software-Defined Radio Wikipedia) along with the IETF RFC 9171 page for the Bundle Protocol.

References:
28 references across Reference (25) and Related Post (3) categories.
All inline-linked per project style.
A152, A153, and A154 cited via post_url as the parent and sibling articles.

### Water Systems and Life Support Recovery for Off-Grid Space Colonization Analogs — Published

**File**: `_posts/2026-06-30-water_systems_and_life_support_recovery_for_off_grid_space_colonization_analogs.markdown`
**Topic**: Second per-subsystem deep-dive in the analog-facilities category following A152 and A153, designed to function as a general off-grid water system guide with space-colonization as contextual flavour. Treats the water layer of the off-grid analog under the dual-keystone framing that the storage tank is the architectural keystone for any off-grid water system and the recovery loop is the closed-system extension that determines long-duration sustainability. Derives storage sizing from first principles with worked examples at 8400 L (terrestrial) and 250 to 420 L (spaceflight regime) scales. Walks the dependent components in order of dependency covering water sources (rainwater harvesting, well extraction, atmospheric water generation, closed-loop recovery), treatment train (sedimentation, filtration, disinfection, polishing), storage materials and geometry, distribution network with hydrostatic pressure and pump power equations, and heating and pressure management. Includes a recovery loop and closure ratio section with worked makeup water demand calculation across mission durations. Includes a treatment technologies in detail section covering reverse osmosis with flux equation, distillation with thermodynamic minimum and multi-stage architectures, ultraviolet disinfection with Chick-Watson kinetics and adenovirus virus caveat, chemical disinfection, activated carbon, and ion exchange. Includes no-recovery architectures section, terrestrial-only cheats section, and space-only options covering lunar polar water ice via LCROSS, Mars subsurface ice via SHARAD, Mars atmospheric water vapor via WAVAR concept, and asteroid and comet volatiles. Closes on three cases where the keystone framing breaks down (sub-day mission duration, trace-water outer solar system, in-situ resource abundance regime). Includes generalisation beyond space analog covering residential cabin, remote research station, disaster relief, maritime vessel, and forward operating base use cases. MathJax enabled.
**Article Number**: A154
**Completion**: 100%
**Publication Sensibility**: High for the space-themed cluster (second per-subsystem article continues the deep-dive cadence under A152's nine-subsystem roadmap, while doubling as a general off-grid water system guide for terrestrial use cases)
**Status**: Published 2026-06-30 (15 references; ~1,690 lines; mathjax true with 11 display equations and 36 inline expressions)

Second per-subsystem deep-dive article following A153, treating the water subsystem of the off-grid analog under the dual-keystone framing where the storage tank is the primary architectural keystone analogous to the battery bank in A153 and the recovery loop is the closed-system extension that determines long-duration sustainability.
Sections covered include
opening as second subsystem deep-dive citing water as the highest-leverage subsystem per A152;
generalisation framing to any off-grid water system context;
The Storage and Recovery Keystone (supply-demand mismatch and closed-system architecture);
Storage Sizing From First Principles (V_storage equation, two worked examples at 8400 L terrestrial and 250 to 420 L spaceflight scales, daily demand decomposition by stream, closure ratio C and makeup water demand equation, makeup water worked example at 95 percent versus zero percent closure);
Dependent Components in Order of Dependency (water sources including rainwater harvesting with the corrected 1.0 L/m2/mm gross conversion and 0.8 to 0.9 effective after runoff coefficient, well extraction with pump power equation, atmospheric water generation, recovery; treatment train through sedimentation, filtration, disinfection with Chick-Watson kinetics, polishing under NSF Standard 61, 53, EPA SDWA, WHO Guidelines; storage materials and geometry; distribution network with hydrostatic pressure equation; heating and pressure management);
The Recovery Loop and Closure Ratio (greywater, blackwater with jurisdiction-dependent kitchen sink classification, atmospheric humidity, urine stream with ISS UPA vapor compression distillation and BPA);
Treatment Technologies in Detail (reverse osmosis with flux equation and corrected energy ranges, distillation with thermodynamic minimum 0.63 kWh/L latent heat and corrected multi-stage values, ultraviolet disinfection with adenovirus caveat, chemical disinfection, activated carbon, ion exchange);
No-Recovery Architectures (single-pass, continuous resupply, hybrid partial recovery);
Terrestrial-Only Cheats (municipal connection, trucked-in delivery, cogeneration);
Space-Only Options (lunar polar water ice via LCROSS October 2009 with Lunar Reconnaissance Orbiter follow-up, Mars subsurface ice via SHARAD with Phoenix lander 2008 confirmation, Mars atmospheric water vapor via WAVAR sorbent regeneration concept from Bruckner at University of Washington, asteroid and comet volatiles);
Where the Keystone Framing Breaks Down (sub-day mission, trace-water outer solar system, in-situ resource abundance);
Generalisation Beyond the Space Analog Context (residential cabin, remote research station, disaster relief, maritime vessel, forward operating base);
Out of Scope (treatment-train engineering, bioregenerative life support biology, pharmaceutical residues, trace organic contaminants, microbial control in distribution, in-situ resource utilisation engineering);
Conclusion.

Research agent verified
the ISS Water Recovery System 98 percent closure after Brine Processor Assembly addition with the 20 June 2023 milestone date,
the ISS Urine Processor Assembly 75 to 87 percent urine water recovery via rotating vapor compression distillation,
the NASA JSC-63414 SWEGs Revision A November 2023 potable water standard,
the Biosphere 2 Mission One water cycle through condensation collection and constructed wetlands,
the BIOS-3 ten crewed closures from 1972 with 180-day longest run and 85 percent water recycling,
the MELiSSA Pilot Plant at the Universitat Autonoma de Barcelona Claude Chipaux Laboratory with five compartments C1 through C5 active in 2025-2026,
the Yuegong-365 mission 10 May 2017 to 15 May 2018 with 98.2 percent overall system closure,
the rainwater harvesting conversion factor 1.0 L per square metre per millimetre gross with 0.8 to 0.9 effective after runoff coefficient,
the atmospheric water generator specific energy 0.25 to 0.5 kWh per litre at moderate humidity,
the kitchen sink jurisdiction-dependent classification with California and Hawaii treating as blackwater versus IPC and UPC excluding from greywater,
the reverse osmosis energy 2.5 to 4 kWh per cubic metre seawater and 0.5 to 1.5 kWh per cubic metre brackish,
the ultraviolet 30 to 40 mJ/cm2 dose for 4-log bacteria and protozoa with adenovirus requiring greater than 100 mJ/cm2,
the ultrafiltration 0.01 to 0.1 micrometre pore size and 0.1 to 0.5 kWh per cubic metre energy,
the distillation thermodynamic minimum 0.63 kWh per litre latent heat with practical small stills at 1 to 2 kWh per litre and multi-stage flash at 18 to 28 kWh per cubic metre,
the NSF/ANSI 61-2025, NSF/ANSI 53-2023, and NSF/ANSI 55-2024 current revisions,
the EPA Safe Drinking Water Act 40 CFR Part 141 National Primary Drinking Water Regulations,
the WHO Guidelines for Drinking-Water Quality fourth edition with third addendum 18 June 2026,
the ASHRAE Standard 188-2021 Legionellosis Risk Management,
the 2024 International Plumbing Code current edition,
the LCROSS impactor mission 9 October 2009 confirming water ice in Cabeus crater,
the Mars Reconnaissance Orbiter SHARAD radar instrument mapping mid-latitude buried ice including Utopia Planitia and Deuteronilus Mensae,
the Phoenix lander 2008 direct observation of subsurface ice,
the WAVAR concept from Adam Bruckner at the University of Washington for Type 3A zeolite molecular sieve cycled adsorption from Martian wind-driven airflow,
and the Mars atmosphere approximately 0.03 percent water vapor average by volume with significant seasonal variation.

Critical factual corrections applied:
the rainwater conversion corrected from 0.9 L/m2/mm to 1.0 L/m2/mm gross with 0.8 to 0.9 effective after runoff coefficient;
the ISS daily water use refined from 4 to 6 L/crew/day to 3 to 5 L/crew/day for drinking and food preparation;
the single-stage distillation energy corrected from 2 to 4 kWh per litre to the thermodynamic minimum 0.63 kWh per litre latent heat with practical small stills at 1 to 2 kWh per litre;
the multi-stage distillation energy refined to 18 to 28 kWh per cubic metre for multi-stage flash and 4 to 7 kWh thermal plus 1.5 to 2 kWh electrical per cubic metre for multi-effect distillation;
the WHO Guidelines for Drinking-Water Quality updated to fourth edition incorporating first, second, and third addenda through June 2026;
the kitchen sink classification softened with jurisdiction-dependent qualifier covering California, Hawaii blackwater treatment versus IPC and UPC exclusion from greywater;
the ultraviolet dose specification expanded with the adenovirus 100 mJ/cm2 caveat for virus inactivation;
the SHARAD acronym spelled out as Shallow Radar on first use.

References:
15 references across Reference (13) and Related Post (2) categories.
All inline-linked per project style.
A152 (Simulating Space Colonization on Earth Using Off-Grid Facilities) and A153 (Electricity and Energy Storage for Off-Grid Space Colonization Analogs) cited via post_url as the parent and sibling articles.

### Electricity and Energy Storage for Off-Grid Space Colonization Analogs — Published

**File**: `_posts/2026-06-29-electricity_and_energy_storage_for_off_grid_space_colonization_analogs.markdown`
**Topic**: First per-subsystem deep-dive in the analog-facilities category following A152, designed to function as a general off-grid electrical-system guide with space-colonization as contextual flavour. Treats the electricity layer of the off-grid analog under the framing that battery storage is the architectural keystone, with every dependent component dimensioned against the battery bank. Derives battery sizing from first principles with worked examples and the round-trip efficiency cascade. Walks the dependent components in order of dependency covering generation capacity with photovoltaic temperature derating, charge controllers, inverters and power conditioning, generator backup with the fuel consumption equation, load shedding strategy, and conductor sizing with the voltage drop equation. Includes a no-battery alternatives section covering continuous baseload fission through Kilopower and Fission Surface Power, geothermal, thermal storage, mechanical storage, and hydrogen production. Includes a terrestrial-only cheats section enumerating grid-tied operation, trucked-in diesel resupply, and cogeneration. Includes a space-only options section covering lunar peaks of eternal light, Mars solar at reduced irradiance, space-based solar power, orbital reflectors and the Znamya experiments, and the statite architecture. Includes a generalisation-beyond-space-analog section covering off-grid cabin, remote research station, disaster relief, maritime vessel, and forward operating base use cases. Closes on three cases where the keystone framing breaks down covering the lunar equatorial fourteen-day night, the Mars dust storm season, and the outer-planet solar weakness. MathJax enabled with ten display equations and twenty inline expressions.
**Article Number**: A153
**Completion**: 100%
**Publication Sensibility**: High for the space-themed cluster (first per-subsystem article opens the deep-dive cadence under A152's nine-subsystem roadmap, while doubling as a general off-grid electrical-system guide for terrestrial use cases)
**Status**: Published 2026-06-29 (16 references; ~1,508 lines; mathjax true with 10 display equations and 20 inline expressions)

First per-subsystem deep-dive article following A152, treating the electricity subsystem of the off-grid analog under the battery-as-keystone framing.
Sections covered include
opening as deep-dive of the highest-leverage subsystem;
The Battery Storage Keystone (decoupling intermittent generation from continuous load, three failure modes for the no-storage architecture);
Battery Sizing From First Principles (E_usable equation, E_nameplate equation with depth of discharge and round-trip efficiency factors, two worked examples at 33 kWh and 1300 kWh scales, chemistry comparison covering LiFePO4, NMC, lead-acid, and vanadium redox flow);
Dependent Components in Order of Dependency (generation capacity with A_PV equation and worked example, charge controllers under NEC 690 and IEC 62548, inverters under UL 1741, generator backup with propane consumption worked example, load shedding strategy with three-tier prioritisation);
No-Battery Architectures (Kilopower KRUSTY with the corrected 28-hour 1 kWe design point demonstration, Fission Surface Power 100 kW class target after August 2025 acceleration, geothermal, thermal storage, mechanical storage, hydrogen production);
Terrestrial-Only Cheats (grid-tied operation, trucked-in fuel resupply, cogeneration with adjacent facility);
Space-Only Options (lunar peaks of eternal light with Shackleton rim Points A and B at 81 and 82 percent illumination and 94 percent maximum, Mars solar at 43 percent of Earth irradiance with InSight dust failure precedent, Space-Based Solar Power with Caltech MAPLE 2023 demonstrator and ESA Solaris programme, orbital reflectors with the Znamya experiments, statite architecture from McInnes 1989 and Forward 1993);
Where the Keystone Framing Breaks Down (lunar equatorial 14-day night, Mars dust storm season, outer-planet solar weakness);
Out of Scope (battery management system engineering, power-electronics circuit design, grid-forming and islanding behaviour, nuclear safety and licensing, space-based solar power economics, energy storage chemistry research);
Conclusion.

Research agent verified
the ISS battery replacement campaign (Ni-H2 to Li-ion, 2017 to 2021, 48 to 24 unit consolidation),
the lithium iron phosphate cycle life and energy density ranges,
the lead-acid and vanadium redox flow battery ranges,
the photovoltaic efficiency ranges across mono- and multi-crystalline silicon, thin film, and triple-junction tandem cells,
the Mars and lunar solar irradiance values,
the McMurdo Ross Island Wind Energy Project specifications,
the Kilopower KRUSTY 28-hour full-power test on 20 March 2018 with 5.5 kW thermal yielding 1 kW electric design point,
the Fission Surface Power programme acceleration to 100 kW class in August 2025,
the MMRTG 125 W beginning of life electrical output from approximately 2 kW thermal,
the Plutonium-238 production restart in 2013 with the 1.5 kg per year target slipped to 2026,
the Peter Glaser 1968 Science paper with the 1973 patent,
the Caltech SSPP MAPLE demonstrator January 2023 launch with June 2023 ground reception below 0.1 microwatt as proof of concept,
the ESA Solaris programme November 2022 Ministerial Council approval with the 2025 full programme decision,
the JAXA mid-2030s commercial SSPS target rather than 2050,
the China space solar power station 2028 LEO demonstrator and 2050 commercial GEO target,
the Znamya 2 February 1993 deployment and Znamya 2.5 February 1999 failure,
the Forward and McInnes statite concept dates (McInnes 1989, Forward 1993),
the Krafft Ehricke Soletta 1978 concept with the Lunetta variant,
the Peaks of Eternal Light at Shackleton crater rim Points A and B with 81 and 82 percent illumination,
the NEC Article 690 and Article 706 photovoltaic and energy storage system coverage,
and the UL 1741 distributed energy resource inverter standard.

Critical factual corrections applied:
the Kilopower KRUSTY description corrected from "1 kW electric output" to "1 kW electric design point demonstrated through 28-hour full-power test producing 5.5 kW thermal";
the Fission Surface Power 40 kW target updated to 100 kW class after the August 2025 NASA acceleration;
the statite attribution corrected from Forward 1991 to McInnes 1989 and Forward 1993;
the Soletta concept date refined from "the 1970s" to "1978" with the Lunetta variant added;
the Caltech MAPLE ground reception detail added that detected power was below one tenth of a microwatt as proof of concept;
the Space-Based Solar Power efficiency caveat expanded to acknowledge theoretical 45 percent ceilings under optimised components;
the IX team description expanded to identify Intuitive Machines and X-energy;
the JAXA acronym spelled out as Japan Aerospace Exploration Agency on first use;
the Peak of Eternal Light section expanded with specific Shackleton Point A and Point B illumination figures and 94 percent maximum;
URL corrections for the NASA Fission Surface Power page (relocated to Wikipedia), the NASA Artemis Base Camp page (replaced with the Peak of Eternal Light Wikipedia article), the Caltech MAPLE landing page (replaced with the Caltech mission-end press release), and the UL 1741 services URL (replaced with the UL Standards Shop product detail page).

References:
14 references across Reference (13) and Related Post (1) categories.
All inline-linked per project style.
A152 (Simulating Space Colonization on Earth Using Off-Grid Facilities) cited via post_url as the parent survey article.

### Simulating Space Colonization on Earth Using Off-Grid Facilities — Published

**File**: `_posts/2026-06-28-simulating_space_colonization_on_earth_using_off_grid_facilities.markdown`
**Topic**: Survey introduction to the off-grid terrestrial analog for space colonization, framed as an iteration engine for the actual space mission. Treats the analog as a problem in its own right rather than a recreational exercise. Establishes a simulation honesty model on four axes (closure, isolation, duration, environmental fidelity), with closure formalised as a quantitative ratio. Surveys the major prior attempts grouped by category (Antarctic stations, closed ecological system experiments, Mars surface analogs, underwater analogs, buoyant and atmospheric platform analogs covering Landis Venus cloudtop and HAVOC), presents a comparison matrix, and walks through site selection criteria with United States and international site catalogues. Defines a nine-subsystem facility stack (electricity and energy storage, electronic operations and computing, communications, food production, potable water, sewage and human waste, physical operations and habitat, garbage and waste disposal, transportation and roads), with light-time delay and Mars synodic period quantified. Introduces the bootstrap and expansion regime distinction with the synodic resupply cadence. Opens the analog-facilities category for subsequent per-subsystem and per-topic articles. Cross-links A82-derived space studies cluster. MathJax enabled.
**Article Number**: A152
**Completion**: 100%
**Publication Sensibility**: High for the space-themed cluster (opens a problem space that subsequent articles can treat in depth)
**Status**: Published 2026-06-28 (57 references; ~2,047 lines; mathjax true)

Survey-style aerospace and engineering article on terrestrial off-grid analog facilities for space colonization simulation.
Sections covered include
opening framing as iteration engine for the real mission;
The Simulation Honesty Problem (closure, isolation, duration, environmental fidelity axes, with closure formalised as C = 1 minus m_ext over m_tot and worked examples for ISS WRS at C ~ 0.98 and Biosphere 2 food at C ~ 0.5);
Survey of Prior Attempts grouped by category covering Antarctic stations (McMurdo, Amundsen-Scott, Concordia), closed ecological system experiments (BIOS-3, Biosphere 2, Yuegong-1, MELiSSA), Mars surface analogs (MDRS, FMARS, HI-SEAS, HERA, CHAPEA, Mars-500), underwater analogs (NEEMO at Aquarius), and buoyant and atmospheric platform analogs (Landis Venus cloudtop and HAVOC framing with density ratio derivation, plus the World View, Loon, and Sceye stratospheric platforms identified as the closest available terrestrial proxies);
Comparison matrix of thirteen prior attempts on site, operator, longest crewed run, closure score, isolation score, and operating year span;
Site Selection (five criteria) with United States catalogue (Mojave, Great Basin, Sonoran, Mauna Loa/Kea, Brooks Range) and international catalogue (Atacama, Devon Island, Pilbara, Iceland and Lanzarote PANGAEA, Antarctic continent, Tibetan Plateau, Pamirs);
The Facility-System Stack (nine subsystems: electricity and energy storage, electronic operations and computing, communications with light-time delay quantified by tau = d/c yielding 3 to 22 minutes for Mars and 1.3 seconds for the Moon, food production, potable water, sewage and human waste, physical operations and habitat, garbage and waste disposal, transportation and roads);
Bootstrap and Expansion (the operational-regime distinction with the Mars synodic period ~780 days fixing the resupply cadence);
Out of Scope (per-subsystem engineering, crew behaviour, closed ecological system biology, pressure suit and EVA, radiation, reduced gravity, programme cost, regulatory and treaty, governance of the simulated colony);
Conclusion.

Research agent verified
the Biosphere 2 mission dates (September 1991 to September 1993, March to September 1994) and the management transfer chain (Columbia 1995 to 2003, University of Arizona 2007 research and 2011 ownership),
the MDRS opening year (2001) and Mars Society operation,
the FMARS inauguration July 2000,
the HI-SEAS operator transfer to International MoonBase Alliance in 2018 with HI-SEAS IV running 366 days in 2015 and 2016,
the HERA 45-day mission length and JSC location,
the CHAPEA Mission 1 dates (June 2023 to July 2024, 378 days) with ICON-printed Mars Dune Alpha habitat,
the Concordia operator as IPEV and PNRA with ESA as scientific participant,
the Mars-500 dates (June 2010 to November 2011) and IBMP Moscow,
the BIOS-3 construction begun 1965 and operational from 1972,
the Yuegong-365 mission (May 2017 to May 2018, 370 days),
the McMurdo establishment date and population variation,
the Amundsen-Scott winter-over population around 40 to 50,
the Aquarius depth (~18 metres), FIU ownership transition (2013 operational, 2014 full), and NEEMO 23 in 2019 as last mission,
the MELiSSA initiation in 1989 with the Pilot Plant at UAB,
the PANGAEA training sites (Lanzarote, Dolomites, Ries Crater),
the Iceland Apollo training dates (1965, 1967) with Artemis II training in 2024,
the ISS Water Recovery System 98 percent recovery via Brine Processor Assembly addition,
and the McMurdo Ross Island Wind Energy Project with three Enercon E33 turbines.

Critical factual corrections applied:
the BIOS-3 dates clarified to construction begun 1965 and operational from 1972;
the Biosphere 2 management chain corrected to Columbia 1995 to 2003, U Arizona research 2007 and full ownership 2011;
the HI-SEAS operator corrected to International MoonBase Alliance since 2018;
the Aquarius depth corrected from approximately 20 metres to approximately 18 metres (60 feet);
the FIU ownership transition split into 2013 operational and 2014 full ownership;
the NEEMO last announced mission corrected to 2019 from 2017;
the ISS Water Recovery System characterised by Brine Processor Assembly addition rather than UPA upgrade;
the PANGAEA training site catalogue expanded to Lanzarote, Dolomites, and Ries Crater with Iceland repositioned as Apollo and Artemis training rather than PANGAEA;
URL replacements for NASA pages reorganised after 2024, the NSF United States Antarctic Program URL migrated to usap.gov, and the Wikipedia URL for Aquarius and Institute of Biophysics articles using current canonical paths.

References:
57 references across Reference (55) and Related Post (2) categories.
All inline-linked per project style.
A90 (introduction to space studies) and A92 (cryptotelemeritocracy for space exploitation) cited via post_url as the prior space-themed cluster articles.
Venus cloudtop subsection cites the Landis 2003 Colonization of Venus paper via NTRS, the NASA Langley High Altitude Venus Operational Concept via Wikipedia, and the World View Stratollite, Loon, and Sceye stratospheric platform programmes as terrestrial proxies.

### Maintenance and Lifecycle Management for SAR Drone Programs — Published

**File**: `_posts/2026-05-21-maintenance_and_lifecycle_management_for_search_and_rescue_drone_programs.markdown`
**Topic**: Seventh and final article in the SAR drone series after A145 (physics), A146 (buyer's framework), A147 (R&D), A148 (geographic setting), A149 (operator training), and A150 (sensor and payload selection with embedded data management). Series terminus. Treats the maintenance and lifecycle management as the second principal cost driver after the operator training programme. Five-layer maintenance stack covering airframe, battery lifecycle, payload calibration, firmware and software, and ground support equipment. Pre-flight and post-flight inspection, scheduled periodic maintenance, mishap repair. Battery cycle counting, state of health monitoring, storage protocols, transport regulations (UN 38.3, IATA DGR, 49 CFR Part 173), disposal and recycling. Payload calibration covering thermal radiometric, lidar boresight, multispectral spectral, gimbal alignment. Firmware and software lifecycle including vendor update cadence and ground station OS lifecycle. Spare parts strategy. Five-year total cost of ownership scorecard table by programme tier with maintenance fraction. End-of-life disposition covering lithium battery recycling, e-waste, and ITAR-controlled sensor disposition. Series synthesis closing the seven-article series.
**Article Number**: A151
**Completion**: 100%
**Publication Sensibility**: High for the buyer audience (closes the series with the operating-cost picture)
**Status**: Published 2026-05-21 (25 references; 3,022 lines)

Standalone aerospace and engineering analytical article on maintenance and lifecycle management for SAR drone programmes.
Sections covered include
opening as series terminus;
Why Maintenance Drives the Multi-Year Cost (consumables, scheduled service, unscheduled service);
The Maintenance Stack Taxonomy (five-layer scorecard table);
Airframe Maintenance (pre-flight and post-flight inspection per Part 107.49, scheduled periodic maintenance with three categories, mishap and field-failure repair with 5 to 10 percent of platform cost per year baseline);
Battery Lifecycle Management (cycle counting against 200 to 500 cycle thresholds, state of health monitoring with 80 percent capacity retirement criterion, storage protocols at 40 to 60 percent state of charge, transport under UN 38.3 and IATA DGR and 49 CFR Part 173, disposal through Call2Recycle and dedicated industrial recyclers);
Payload Maintenance and Calibration (thermal radiometric annual at USD 500 to USD 2000 per cycle, lidar boresight after assembly or major repair, multispectral via reference panels, gimbal mechanical alignment);
Firmware and Software Lifecycle (vendor update cadence with DJI and Skydio security trust centers, ground station OS lifecycle with Windows 10 EOL October 2025);
Spare Parts Strategy (critical spare inventory ratios, vendor parts catalogues, cannibalisation for legacy fleets);
Total Cost of Ownership (five-year scorecard table mapping to A146 tiers with 15 to 25 percent maintenance fraction);
End-of-Life Disposition (lithium battery recycling, airframe and avionics e-waste, ITAR-controlled sensor disposition through DDTC);
A Worked SAR Drone Programme Walk-Through (seven-step walk-through of a constructed Tier 2 mid-sized regional county SAR programme through the buyer's framework, geographic filter, platform selection, sensor selection with data management, operator training, maintenance programme, and integrated operating cycle);
Series Synthesis (seven-domain decision space recapitulation, entry-point matrix mapping reader question to starting article, sequential reading roadmap by reader role covering programme manager, operator pool builder, IT and compliance officer, and R&D lead);
Out of Scope (operator maintenance training, airworthiness certification for non-Part 107 platforms, cybersecurity incident response, maritime SAR specific maintenance, international logistics, plus a Topics Deferred at the Series Terminus subsection enumerating nine deferred topics that the series did not draft including lease versus buy financial analysis, insurance and underwriter requirements, detection algorithm ecosystem, vendor consolidation and supply chain risk, operator labour and human resources strategy, legal and regulatory counsel relationship, inter-agency coordination, multi-platform mixed-fleet management, and metrics and outcomes measurement);
Conclusion (series terminus).

Research agent verified
the DJI Care Enterprise and DJI Maintenance Program tier structures,
the DJI Intelligent Flight Battery cycle definition where one cycle equals 75 percent of rated capacity consumed,
the Skydio Care Enterprise availability for X10 with the explicit exclusion of X10D Blue UAS variant,
the WingtraCARE and Total Maintenance Plan service tiers,
the UN 38.3 Revision 8 with Amendment 1,
the IATA Dangerous Goods Regulations 67th Edition effective 1 January 2026 with the new 30 percent state of charge limit for UN 3480 and UN 3481 shipments,
the 49 CFR 173.185 lithium cells and batteries regulation,
the PHMSA Lithium Battery Guide for Shippers,
the IEC 62133-2 portable sealed secondary lithium cell safety standard,
the ANSI National Accreditation Board and A2LA accreditation pathway,
the FAA Part 107.49 preflight inspection requirement,
the FAA Public Aircraft Operations guidance through AC 00-1.1B,
the FAA AC 107-2A current revision,
the ASTM F2909 Continued Airworthiness specification,
the 14 CFR Part 43 applicability limitation to Category 4 operations,
the Call2Recycle network with the explicit damaged battery limitation,
and
the Microsoft Windows 10 end of standard support on 14 October 2025 with ESU through 13 October 2026.

Critical factual corrections applied:
the "DJI Enterprise Care" naming corrected to "DJI Care Enterprise";
the DJI Intelligent Flight Battery cycle definition clarified to 75 percent of rated capacity consumed rather than full discharge;
the IATA DGR 67th Edition January 2026 30 percent state of charge limit added for lithium battery shipment;
the Call2Recycle limitation clarified that the network does not accept damaged, swollen, leaking, or recalled batteries with the local hazardous waste facility cited as the disposal pathway for the crashed platform battery;
the NIST traceability framed as industry best practice rather than NIST mandate;
the ANSI National Accreditation Board and A2LA cited as the accreditation pathway for ISO IEC 17025 calibration laboratories;
the Microsoft Windows 10 EOL date specified as 14 October 2025 with the ESU programme available through 13 October 2026;
URL corrections for the DJI Battery Maintenance Guide specific support article, the DJI Care service portal, the DJI Care Refresh specific URL, and the 49 CFR 173.185 specific section URL.

References:
25 references across Reference (19) and Related Post (6) categories.
All inline-linked per project style.
A145 (physics), A146 (buyer's framework), A147 (R&D), A148 (geographic setting), A149 (operator training), and A150 (sensors and data) cited via post_url.

**Remaining Work**:
None. Published. Series terminus.

### Sensor and Payload Selection for Search and Rescue Drones — Published

**File**: `_posts/2026-05-20-sensor_and_payload_selection_for_search_and_rescue_drones.markdown`
**Topic**: Sixth article in the SAR drone series after A145 (physics), A146 (buyer's framework), A147 (R&D), A148 (geographic setting), and A149 (operator training). Treats the sensor payload as the principal mission-capability decision the programme manager makes after the airframe and the operator training. Six sensor categories (thermal imaging, electro-optical visible, lidar, multispectral and hyperspectral, audio payloads, specialised). Per-class physics, performance metrics, resolution tiers, vendor landscape. Payload integration covering mass, power, data bandwidth, gimbal mount, and MISB metadata. Sensor data management and chain of custody covering data volume, storage architecture, evidentiary chain of custody, records retention and FOIA, state drone surveillance laws, federal procurement and Blue UAS, cybersecurity controls, vendor data handling policies, and calibration records as evidentiary support. Sensor mix by mission profile scorecard table. Sensor budget by programme tier table mapping to A146 tiers.
**Article Number**: A150
**Completion**: 100%
**Publication Sensibility**: High for the buyer audience (complements A146 as the sensor-and-data investment companion)
**Status**: Published 2026-05-20 (81 references; 4,364 lines)

Standalone aerospace and engineering analytical article on sensor and payload selection for SAR drone programmes.
Sections covered include
opening as sixth in the SAR drone series;
Why the Sensor Frames the Mission (sensor defines detection envelope, airframe defines coverage);
The Sensor Stack Taxonomy (six categories with detection physics, typical range, per-sensor cost tier table);
Thermal Imaging (uncooled LWIR vs cooled MWIR, NETD, four resolution tiers from entry through frontier, radiometric vs non-radiometric, vendor landscape);
Electro-Optical Visible Imaging (sensor format, resolution, stabilisation, low-light and starlight imaging);
Lidar (range, point density, return modes, georegistration via RTK and PPK, vendor landscape);
Multispectral and Hyperspectral Imaging (wildfire SWIR application, water rescue, ground anomaly detection);
Audio Sensors and Acoustic Payloads (loudspeaker payloads, acoustic detection research phase);
Payload Integration (mass and endurance trade, power budget, data bandwidth, gimbal mount standards including DJI Skyport and ASTM F38, MISB KLV and STANAG 4609 metadata);
Sensor Data Management and Chain of Custody (data volume by sensor class with concrete per-hour figures, storage architecture across onboard, ground station, and cloud classes, chain of custody for evidentiary use with KLV metadata, cryptographic hash integrity, calibration record linkage, records retention and FOIA implications including IACP body-worn camera framework adaptation, state drone surveillance laws with NCSL tracker and representative state statutes from Florida, Texas, Illinois, California, and Nevada, federal procurement restrictions with American Security Drone Act and Blue UAS framework, cybersecurity controls covering NIST 800-53, NIST 800-171, CMMC, and FedRAMP, vendor data handling policies for DJI FlightHub 2, Skydio Cloud, Parrot Cloud, Wingtra Cloud, DroneDeploy, Pix4D, Esri Site Scan, and Esri ArcGIS, calibration records and evidentiary support under the Daubert standard with ISO IEC 17025 and NIST traceability);
Sensor Mix by Mission Profile (eight-profile scorecard table from night land search through underwater);
Sensor Budget by Program Tier (five-tier scorecard table mapping to A146 tiers);
Out of Scope (sensor-specific operator training, maintenance and lifecycle management, machine learning detection algorithms, export control regime, specialised sensors, underwater payloads, international regulatory regimes);
Conclusion.

Research agent verified
the FLIR Boson Plus and Boson core distinction (NETD 20 mK vs 50 mK),
the Hadron 640R modular pairing,
the Tau 2 pixel pitch and ITAR classification,
the Workswell WIRIS Pro 640x512 and WIRIS Security 800x600 split,
the Sierra-Olympia naming where Vinden is uncooled LWIR and Ventus is cooled MWIR,
the DJI Zenmuse L2 five-return survey lidar performance,
the DJI Zenmuse V1 thermal-and-loudspeaker payload at 127 dB and 500 metres,
the LightWare microLiDAR altimeter line,
the Ouster-Velodyne merger,
the YellowScan and Riegl survey-grade configurations,
the MicaSense AgEagle ownership and Altum-PT thermal-multispectral configuration,
the Cubert ULTRIS snapshot hyperspectral line,
the MISB ST 0601 KLV and STANAG 4609 motion imagery interoperability framework,
the ASTM F38 subcommittee structure and the ISO 21895 categorisation standard,
the MIL-STD-704 aircraft and MIL-STD-1275 ground vehicle power standards,
and
the DroneAudioset benchmark for distress-signal detection research.

Critical factual corrections applied:
the "Brigade Electronics drone loudspeaker line" claim removed since Brigade has no public drone loudspeaker product, replaced with the DJI Zenmuse V1 integrated payload and the Sky Speaker-I aftermarket payload from Yangda;
the "SkyShout purpose-built drone loudspeaker payloads" claim removed since the SkyShout manufacturer attribution could not be verified, replaced with the Sky Speaker-I from Yangda;
the Carnegie Mellon whistle detection attribution softened to "CMU Robotics Institute AirLab work on SAR-oriented aerial robotics" with the DroneAudioset benchmark cited as the specific distress-signal research anchor;
the "12 volt and 28 volt drone payload power bus standards" claim reframed since the drone industry has not adopted either MIL-STD-704 or MIL-STD-1275 as a universal payload bus, with both standards now cited as relevant aviation power standards rather than drone standards;
the "ASTM Committee F38 universal payload mount standard" claim reframed since F38 has not standardised a universal payload mount, with the DJI SkyPort and X-Port through the DJI Payload SDK cited as the dominant Enterprise mount and fixed-wing platforms noted as vendor-specific custom mounts;
URL corrections for FLIR Boson Plus and Hadron 640R (oem.flir.com pages),
the Workswell WIRIS Pro page,
the Freefly MoVI XL store page,
the YellowScan compare-products page,
the Sierra-Olympia airborne cameras page,
the DJI Payload SDK developer portal,
the Sony Starvis Framos overview page.

Second research agent pass commissioned for the sensor data management section. Verified NIST SP 800-86 publication, ISO IEC 27037 and the 27041, 27042, 27043 family, ASTM E2916, SWGDE Best Practices for Drone Forensics document 21-F-002, CJIS Security Policy version 6.0, 28 CFR Part 23 applicability, American Security Drone Act incorporation in FY 2024 NDAA Sections 1821-1833, NDAA Section 848 of FY 2020 prohibition, Blue UAS framework with the December 2025 list transition from DIU to DCMA, Florida Statute 934.50, California Civil Code Section 1708.8 as amended by AB 856, Texas Government Code Chapter 423, Illinois 725 ILCS 167, FOIA Exemption 7(C), NIST SP 800-53 Release 5.2.0, NIST SP 800-171 Rev 3, CMMC final procurement rule effective 10 November 2025 with DoD-contract scope, FedRAMP, DJI FlightHub 2 data residency, DJI Local Data Mode, Skydio Cloud US AWS regions, Parrot Cloud EU residency, Daubert v. Merrell Dow, ISO IEC 17025 calibration laboratory accreditation, and NIST traceability for radiometric thermal calibration via the Low Background Infrared facility.

Critical factual corrections applied in the second pass:
the thermal radiometric per-hour data volume range extended from "500 megabytes to 2 gigabytes" to "500 megabytes to 5 gigabytes" to capture continuous radiometric video capture;
the lidar per-hour data volume range extended from "5 to 30 gigabytes" to "5 to 50 gigabytes" to capture higher-point-rate frontier survey-grade systems;
the example Tier 2 weekly thermal data volume adjusted to "5 to 50 gigabytes per week" reflecting the wider range;
the CMMC clarification added that the certification applies primarily to Department of Defense contracts rather than the non-Department of Defense federal grants that the SAR programme more commonly operates under;
the Blue UAS attribution clarified as "Defense Innovation Unit Blue UAS framework" with the December 2025 list transition to the Defense Contract Management Agency noted;
the California citation refined to "California Civil Code Section 1708.8 as amended by AB 856";
URL corrections for the American Security Drone Act FAR final rule, the Blue UAS framework page at diu.mil/blue-uas/framework, the SWGDE drone forensics document, the California Civil Code Section 1708.8 specific URL.

References:
81 references across Reference (76) and Related Post (5) categories.
All inline-linked per project style.
A145 (physics), A146 (buyer's framework), A147 (R&D), A148 (geographic setting), and A149 (operator training) cited via post_url.

**Remaining Work**:
None. Published.

### Operator Training and Certification for a Search and Rescue Drone Program — Published

**File**: `_posts/2026-05-19-operator_training_and_certification_for_search_and_rescue_drone_programs.markdown`
**Topic**: Fifth article in the SAR drone series after A145 (physics), A146 (buyer's framework), A147 (R&D), and A148 (geographic setting). Disaggregates the operator training cost that A146 mentioned in passing into a five-layer training stack (FAA Part 107, manufacturer training, SAR operational training, NIMS and ICS, specialised operations). Per-layer cost and timeline. Recurrency requirements. Crew roles and training pathways. Operator pool construction. Training budget by program tier.
**Article Number**: A149
**Completion**: 100%
**Publication Sensibility**: High for the buyer audience (complements A146 as the operator-investment companion)
**Status**: Published 2026-05-19 (56 references; 2,059 lines)

Standalone aerospace and engineering analytical article on operator training and certification for SAR drone programmes.
Sections covered include
opening as fifth in the SAR drone series;
Why Training Dominates the Cost (personnel scaling, currency accumulation, turnover replacement);
The Five Layers of the Training Stack (overview);
Layer 1, the Regulatory Minimum (FAA Part 107 certificate, ALC-451 recurrent course, waivers and exemptions, Public Aircraft Operations pathway);
Layer 2, Manufacturer Training (DJI Enterprise Learning Center, Skydio Academy, Parrot Certified Training Program, AeroVironment training, Quantum Systems, Wingtra);
Layer 3, SAR Operational Training (DRONERESPONDERS UNITE, TEEX UAS programmes, NASAR SARTech series, NDSU/NPUASTS, Sinclair, Embry-Riddle);
Layer 4, NIMS and ICS Integration (IS-100, IS-200, IS-700, IS-800, ICS-300, ICS-400, NWCG alignment);
Layer 5, Specialised Operations (night, OOP with ASTM F3322, BVLOS, wildfire NWCG taskbooks);
Recurrency and Currency Maintenance (per-layer recurrency, flight-hour requirements);
Crew Roles and Training Pathways (Visual Observer, Sensor Operator, Remote Pilot in Command, Search Team Coordinator, UAS Team Leader with role-cost scorecard table);
Building the Operator Pool (selection, volunteer vs paid, retention, multi-platform qualification);
Training Budget by Program Size (scorecard table mapping to A146's five tiers);
Out of Scope (sensor selection training, maintenance technician training, state-by-state variation, international frameworks);
Conclusion.

Research agent verified
the FAA Part 107 and ACS materials,
the FEMA Independent Study and ICS course catalogue,
the NWCG Next Generation Position Task Book pathway,
the SAR-specific training providers,
the manufacturer training portals,
and the NIST Standard Test Methods adoption pathway.
Critical factual corrections applied:
the non-existent "NIMS UAS Group Supervisor" position renamed to "UAS Team Leader" with reference to the actual NWCG UASM position and FEMA NIMS-509 sUAS team typing,
the non-existent NWCG "UASGS" and "RPM" positions replaced with the actual NWCG UASP, UASM, and UASL positions,
the "NIST-licensed evaluator" claim for TEEX corrected to "NIST-aligned evaluator" with reference to ASTM Committee E54.09 and the Airborne Public Safety Association as the credentialing bodies,
and URL corrections for ICS-300/400 (separate catalogue URLs), Embry-Riddle (bachelor's programme), Sinclair (UAS center), AeroVironment (Puma product page since training is contract-bundled), Parrot (certified training programme), NDSU/NPUASTS (test site), TEEX (sUAS-specific programme), and Wingtra (extended services).

References:
56 references across Reference (52) and Related Post (4) categories.
All inline-linked per project style.
A145 (physics), A146 (buyer's framework), A147 (R&D), and A148 (geographic setting) cited via post_url.

**Remaining Work**:
None. Published.

### Search and Rescue Drone Fleets by Geographic Setting — Published

**File**: `_posts/2026-05-18-search_and_rescue_drone_fleets_by_geographic_setting.markdown`
**Topic**: Fourth article in the SAR drone series after A145 (physics and economics), A146 (buyer's framework), and A147 (R&D companion). Treats the urban-to-frontier geographic axis as an independent fleet-selection filter alongside A146's mission-profile filter. Four operational levels (Densely Urban, Suburban or Small Urban, Rural, Frontier and Remote) mapped to federal classifications (RUCC, RUCA, CDC NCHS, FAR). Per-level platform mix, fleet sizing, airspace and regulatory posture, funding map, and crew complement. Parallel-operations patterns (single-aircraft serial, single-class parallel, cross-class parallel, multi-aircraft swarms, manned-unmanned teaming). Reading-order table for the four articles in the series.
**Article Number**: A148
**Completion**: 100%
**Publication Sensibility**: High for the buyer audience (complements A146)
**Status**: Published 2026-05-18 (51 references; 1,694 lines)

Standalone aerospace and engineering analytical article on the geographic-setting filter for SAR drone fleet selection.
Sections covered include
opening as fourth in the SAR drone series;
Why Setting Matters Beyond Mission Profile (six structural axes: airspace classification, operations over people, beyond visual line of sight, range and communications, crew complement, funding landscape);
The Federal Geographic Classifications (USDA RUCC, RUCA, CDC NCHS, USDA FAR);
The Four Operational Levels (with mapping table to the federal classifications);
Level 1, Densely Urban (multicopter-dominated fleet, LAANC routine, OOP routine, UASI funding);
Level 2, Suburban or Small Urban (balanced multicopter and hybrid fleet);
Level 3, Rural (fixed-wing or hybrid essential, Class G airspace, SHSP funding);
Level 4, Frontier and Remote (long-endurance fixed-wing essential, Class G, Section 44807 exemptions, federal frontier-operating agency budgets);
Parallel Operations Patterns (single-aircraft serial, single-class parallel, cross-class parallel, multi-aircraft swarms, manned-unmanned teaming);
Airspace and Regulatory Posture by Level (scorecard table);
Funding by Level (UASI, SHSP, THSGP, AFG, federal frontier agency budgets, USDA Rural Development);
Crew Complement by Level (scorecard table);
The Quartet Reading Order (table mapping audience to entry article);
Out of Scope (international classifications, detailed airspace charting, specific operational tactics, state-by-state regulatory variation);
Conclusion.

Research agent verified
the federal classification system URLs,
the FAA airspace and LAANC URLs,
the Part 107 Operations Over People rule and ASTM F3322 standard,
the UASI and HSGP funding programmes,
the federal frontier-operating agency UAS programmes,
and the parallel-operations multi-drone management platforms.
URL corrections applied for CDC NCHS, B4UFLY, USFS UAS, USFWS UAS, Iridium for UAV markets, Starlink business, NPS aviation search and rescue, USDA Rural Development community facilities, and the UAS Facility Maps canonical ArcGIS-hosted location.

References:
51 references across Reference (48) and Related Post (3) categories.
All inline-linked per project style.
A145 (physics and economics), A146 (buyer's framework), and A147 (R&D companion) cited via post_url as the prior articles in the SAR drone series.

### Research and Development for Search and Rescue Drones — Published

**File**: `_posts/2026-05-17-research_and_development_for_search_and_rescue_drones.markdown`
**Topic**: Third article in the SAR drone series after A145 (physics and economics) and A146 (buyer's framework). Treats the research and development side for the smaller audience of academic SAR research groups, federal labs, public-safety agencies with engineering staff, SBIR awardees, and the supporting contractor base. Build-versus-buy frame, federal R&D funding sources, university and federal lab partnerships, the SDK and simulator landscape, custom payload development, regulatory pathways for experimental aircraft, intellectual property in federally funded research, and the technology transition through the valley of death.
**Article Number**: A147
**Completion**: 100%
**Publication Sensibility**: High for the R&D audience; not for the general SAR buyer audience
**Status**: Published 2026-05-17 (101 references; 2,015 lines)

Standalone aerospace, engineering, and program-management analytical article.
Sections covered include
opening as third in the SAR drone series;
The Build-Versus-Buy Frame (three options: build, modify, buy with operational properties that move the program between tiers);
When to Build, When to Modify, When to Buy (custom flight envelope, custom sensor integration, novel autonomous behaviour, multi-aircraft coordination, custom communications);
Federal R&D Funding for SAR Drones (DHS S&T including LRBAA and SBIR and FRRG, SBIR/STTR, NIST PSCR, NIST Standard Test Methods, NASA UAS-NAS, NSF CPS and SCC, DOE national labs including Sandia ORNL INL PNNL, DARPA OFFSET and SubT);
University and Federal Lab Partnerships (the seven FAA UAS Test Sites with the corrected chronology of six in December 2013 plus UAF in early 2014, Raspet, NREC, MIT Lincoln Lab, JHU/APL, NPS CRUSER);
The SDK and Simulator Landscape (DJI Mobile/Onboard/Payload SDKs, Skydio Extend, Parrot Olympe and Open Flight Control, PX4, ArduPilot, ROS 2, PX4 SITL/HITL, AirSim with the full discontinued-and-continued-by-IAMAI lineage, Gazebo, NVIDIA Isaac Sim, MathWorks UAV Toolbox);
Custom Payload Development (Pixhawk/Holybro/mRo autopilot hardware, FLIR Boson Plus and Workswell and Sierra Olympia thermal payloads, LightWare LiDAR, Raspberry Pi and NVIDIA Jetson companion computers, NDAA-compliant component sourcing);
Regulatory Pathways for Experimental Aircraft (Part 107, Section 44807, COA, Special Airworthiness Certificate, Type Certification, Part 108 NPRM);
Intellectual Property in Federally Funded Research (Bayh-Dole, SBIR uniform 20-year data rights regime under May 2019 SBA Policy Directive and DFARS Final Rule January 2025, Stevenson-Wydler and CRADAs, DFARS 252.227-7013/-7014, STTR pre-award allocation);
Technology Transition from Prototype to Operational Use (valley of death, SBIR Phase III sole-source, DHS T2C and CAP, FAA Type Certification, NIST Standard Test Methods as gates, operator demonstrations through DRONERESPONDERS UNITE);
Out of Scope (detailed engineering of custom platforms covered in A112 through A131, international R&D, counter-UAS, manned aircraft integration, commercial-only development);
Conclusion.

Research agent verified
the underlying SDK and platform URLs,
the federal funding programmes,
the university lab and FAA test site URLs,
the regulatory pathway URLs,
and the intellectual property regime documents.
Critical factual corrections applied:
the SBIR data rights regime corrected to the uniform 20-year window under the May 2019 SBA Policy Directive (the pre-2019 4-years-plus-12 regime no longer applies),
the FAA UAS Test Site chronology corrected to six designated December 2013 plus UAF early 2014,
the Nevada UAS Test Site updated to the UNR Nevada Autonomous programme (March 2022 transition),
the University of Maryland UAS Test Site updated to UROC (October 2022 rebrand),
the Naval Postgraduate School lab corrected from the non-existent CAVR to the actual CRUSER,
the AirSim lineage corrected to acknowledge the July 2022 archive, the December 2023 Project AirSim discontinuation, and the IAMAI Simulations continuation,
and the DHS transition vehicles updated from the older Transition to Practice programme to the current Technology Transfer and Commercialization Program plus the Commercialization Accelerator Program.

References:
101 references across Reference (92) and Related Post (9) categories.
All inline-linked per project style.
A145 (physics and economics) and A146 (buyer's framework) cited via post_url as the prior articles in the SAR drone series.
A112 (prototyping), A132 (SBIR intro), A138 (Phase III), A139 (data rights), A141 (after the award), A142 (strategy), and A144 (worked campaign) cited via post_url as the prior SBIR and fixed-wing UAV series articles.

### A Buyer's Decision Framework for Search and Rescue Drones — Published

**File**: `_posts/2026-05-16-buyers_decision_framework_for_search_and_rescue_drones.markdown`
**Topic**: Practitioner buyer's decision framework for US-based search and rescue drone procurement in 2026, the actionable companion to A145. Three-branch decision tree on funding source, mission profile, and budget tier. Five budget tiers including a Tier 0 proof-of-concept tier for organizations beginning a program. Worked five-year total cost of ownership. Federal funding source map. Crew complement and Incident Command System integration. Insurance and liability. Buying timeline.
**Article Number**: A146
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-05-16 (60 references; 1,755 lines)

Standalone aerospace and engineering analytical article on UAV procurement for SAR.
Sections covered include
opening framing as companion to A145;
Branch One, the Funding Source (FAR 52.240-1 effective 22 December 2025, ADSA 2023, NDAA Section 1709 of FY 2025, FCC Covered List actions on DJI and Autel, DCMA Blue UAS list since 3 December 2025, JAG restriction on drone procurement);
Branch Two, the Mission Profile (wilderness, urban, water rescue, alpine, disaster response, payload essentials);
Branch Three, the Budget Tier:
  Tier 0, Evaluation and Proficiency ($300 to $1,500 acquisition; proof-of-concept-through-production framing universal to any new capability; DJI Mini 4 Pro, Autel Nano Plus, BetaFPV Cetus Pro; SDK and simulator references including DJI Mobile SDK, Parrot Olympe, PX4, ArduPilot, AirSim, Gazebo);
  Tier 1, Volunteer ($3,000 to $15,000);
  Tier 2, Small Professional ($15,000 to $60,000);
  Tier 3, Medium Professional ($60,000 to $250,000);
  Tier 4, Large Program or Federal Agency ($250,000 to $2 million plus);
a Worked Five-Year Total Cost of Ownership (Tier 3 example, approximately $430,000 over five years against $200,000 acquisition);
Funding Sources (HSGP with UASI consolidated into SHSP in FY 2025, AFG admissible for drones, SAFER personnel-only, JAG restricted, Operation Stonegarden);
Crew Complement and Incident Command Integration;
Insurance and Liability (FTCA, sovereign immunity, commercial insurance);
the Buying Timeline (6 to 18 months from decision to operational capability);
Out of Scope;
Conclusion.

Research agent verified
the FAR 52.240-1 effective date and citation,
the ADSA 2023 enactment as part of FY 2024 NDAA,
the corrected attribution of Section 1709 to FY 2025 NDAA,
the DCMA Blue UAS list transfer of 3 December 2025,
the JAG restriction on drone procurement per Bureau of Justice Assistance guidance,
the UASI consolidation into SHSP in FY 2025,
the SAFER personnel-only scope,
current 2026 prices for representative platforms,
and the structural gap that no NDAA-compliant prosumer thermal multicopter sells under $10,000 in the US market.
The article incorporates these findings as factual corrections rather than as commentary.

References:
60 references across Reference (58) and Related Post (2) categories.
All inline-linked per project style.
A145 (physics and economics companion) cited via post_url.
A134 (payload and mission systems) cited via post_url.
Forward reference to a future A147 (drone development companion) is plain prose without a post_url tag, to be upgraded after A147 publishes.

### Fixed-Wing, Multicopter, and Hybrid Drones for Search and Rescue, Physics and Economics — Published

**File**: `_posts/2026-05-15-fixed_wing_multicopter_and_hybrid_drones_for_search_and_rescue.markdown`
**Topic**: Comparative analysis of the three drone platform classes (fixed-wing, multicopter, hybrid VTOL) for search and rescue, covering the underlying physics, capital outlay, upkeep costs, and personnel training. The first of a two-part series, with the buyer's decision framework to follow as A146.
**Article Number**: A145
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-05-15 (57 references; 1,824 lines)

Standalone aerospace and engineering analytical article on UAVs in search and rescue.
Sections covered include
opening problem framing;
the three platform classes (fixed-wing, multicopter, hybrid VTOL with examples);
the physics of fixed-wing flight (lift, drag, lift-to-drag ratio, Reynolds number and the low-Reynolds-number regime, the electric Breguet endurance equation);
the physics of multicopter flight (Rankine and Froude actuator disk theory, hover power, disk loading, figure of merit, forward-flight power minimum, battery endurance);
the physics of hybrid VTOL aircraft (tail-sitter, quad-plane and convertiplane, tilt-rotor and tilt-wing, the cruise efficiency penalty);
performance implications for search and rescue with a scorecard table;
the four-phase SAR use case sequence (wide-area search, target investigation, intervention, sustained coverage);
capital outlay with a price-range table covering multicopter, hybrid VTOL, and fixed-wing classes;
upkeep costs with a per-platform annual cost table covering batteries, propellers, motors, airframe inspection, sensor calibration, ground station, spectrum, insurance, and incident repair;
personnel training (FAA Part 107, manufacturer training, search-and-rescue specific training, recurrency) with a training cost table;
the hybrid compromise with a scorecard table;
Out of Scope (defers detailed regulatory compliance, sensor technology in depth, weather minima and operational envelopes, mission-system architecture, and specific procurement guidance);
conclusion.

MathJax used throughout the physics sections.

Cross-links via post_url to the existing series:
A114 (runway sizing), A116 (launch and recovery), A123 (propulsion and power sizing), A125 (electric energy systems and endurance budget), A134 (payload and mission systems), A135 (regulatory and operations layer), A144 (worked SBIR campaign).

References:
57 references across Reference (50) and Related Post (7) categories.
All inline-linked per project style.
A parallel research agent verified physics references (Wikipedia momentum theory, drag equation, Reynolds number, Breguet, figure of merit, disk loading), platform references (current URLs for ScanEagle, Skylark, Skydio X10, Penguin C as Edge Autonomy), regulatory references (eCFR Part 107 as primary source, FAA public safety page, EASA), training references (DJI Academy, Skydio Academy, AOPA), and SAR-specific references (DRONERESPONDERS, NASAR).
Vendor URLs returning 403 to curl are documented bot-detection patterns, valid for human readers.
No internal research cited.

### A Worked SBIR and STTR Campaign for a Fixed-Wing UAV — Published

**File**: `_posts/2026-06-27-worked_sbir_and_sttr_campaign_for_a_fixed_wing_uav.markdown`
**Topic**: A single constructed company, the running fixed-wing unmanned aircraft firm, followed through a whole SBIR and STTR campaign from feasibility to prototype to market, synthesizing the entire series; the thirteenth and final article of the SBIR/STTR practitioner-playbook series, the worked-campaign capstone.
**Article Number**: A144
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-06-27 (19 references)

Standalone article and the thirteenth and final article of the SBIR/STTR practitioner-playbook series, the worked-campaign capstone that closes it.
Framed on the organizing idea of the whole series, that the programs supply non-dilutive capital in stages against demonstrated risk reduction, a staircase from feasibility to prototype to market, walked once in full by one company that uses each award to buy the next rung.
Sections covered include
the company and the airframe (the dual-use fixed-wing unmanned aircraft of the running case);
deciding to pursue (orientation and the agency choice);
getting ready (eligibility and registration, the STTR route chosen);
finding the topic and winning Phase I (the feasibility proposal);
Phase II and the prototype (the commercialization plan, the research partner performing its share under the STTR split);
the money, the rights, and the compliance (the indirect rate and the cash gap, the Phase-I-to-Phase-II funding gap, data-rights marking and the company-and-partner intellectual-property allocation, reporting and audits);
the valley of death and Phase III (the transition partner and the sole-source follow-on);
the strategy over time (the portfolio, the state match, the private-capital bridge, the international option);
where it could go wrong (the same campaign in reverse as a catalog of the failures the series warned against);
and an Out of Scope section.
The company is explicitly a constructed illustration rather than a real firm.
mathjax false (no equations).
No runnable code, so no Software Versions section.
Cross-links every prior article of the series via post_url (A132 the introduction, A133 the agencies, A134 eligibility, A135 the topic and solicitation, A136 Phase I, A137 Phase II, A138 Phase III, A139 data rights, A140 the money, A141 after the award, A142 strategy, and A143 international analogs) plus A112 (the running-case unmanned aircraft).
19 references across Reference (4), Related Post (13), and Research (2) categories.
With A144 the SBIR/STTR practitioner-playbook series is complete, all thirteen of thirteen articles published.

### International Analogs to SBIR and STTR — Published

**File**: `_posts/2026-06-26-international_analogs_to_sbir_and_sttr.markdown`
**Topic**: A survey of the foreign equivalents to the United States SBIR and STTR programs, organized by the structural axes along which they differ (procurement versus grant versus tax credit versus equity; non-dilutive versus dilutive; challenge-driven versus open; phased versus single-shot); the twelfth article and the single dedicated international article of the SBIR/STTR practitioner-playbook series.
**Article Number**: A143
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-06-26 (20 references)

Standalone article and the twelfth of the SBIR/STTR practitioner-playbook series, the one dedicated international article.
Framed on the idea that every advanced economy faces the same market failure in early-stage high-risk technology and each has built a public instrument to fund the risk reduction private capital will not, so the analogs are different answers to one shared question rather than copies of a single design.
Sections covered include
the common problem (the market failure, the valley of death, industrial policy);
the procurement copies (the United Kingdom Contracts for Innovation, formerly the Small Business Research Initiative; the Netherlands SBIR, now the Innovation Impact Challenge; Australia's Business Research and Innovation Initiative; Canada's Innovative Solutions Canada; Japan's 2021-reformed SBIR under the Cabinet Office);
the European grant programs (Horizon Europe, the European Innovation Council Accelerator, the Eureka network and Eurostars, Germany's Central Innovation Programme for the Mittelstand);
the research-collaboration analog (the STTR dimension, the consortium model as the default abroad, South Korea's move to add an STTR-style program);
the tax-credit instrument (Canada's Scientific Research and Experimental Development credit);
the state as investor (the Israel Innovation Authority's royalty-bearing grants, the European Accelerator's blended grant-plus-equity, South Korea's Tech Incubator Program for Startups);
defense and dual-use (the North Atlantic Treaty Organization's DIANA);
the axes of difference (a 13-program comparison table and where the United States program sits);
scale and the UAV case;
and an Out of Scope section.
mathjax false (no equations).
No runnable code, so no Software Versions section.
All foreign-program facts were verified by web search and flagged current-as-of, with each country's own program authority named as the only reliable source.
Cross-links A132 (the introduction), A134 (eligibility and the STTR distinction), A138 (the valley of death), A140 (the money, non-dilutive), A142 (strategy and the portfolio), and A112 (the running-case company) via post_url; the worked-campaign capstone is referenced in prose pending A144.
20 references across Reference (11), Related Post (6), and Research (3) categories.

### Strategy and the Portfolio of SBIR and STTR Awards — Published

**File**: `_posts/2026-06-25-strategy_and_the_portfolio_of_sbir_and_sttr_awards.markdown`
**Topic**: The strategic view above the single award, the portfolio, transition versus the mill, stacking non-dilutive capital, the private-capital bridge, dual-use markets, and the discipline of choosing what to pursue; the eleventh article of the SBIR/STTR practitioner-playbook series.
**Article Number**: A142
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-06-25 (20 references)

Standalone article and the eleventh of the SBIR/STTR practitioner-playbook series.
Framed on the idea that an award is a means and not an end, and that strategy is the discipline of using a portfolio of non-dilutive awards, staged against the risk reduction the whole series has tracked, to build a company that eventually no longer needs them, with the central choice between transition and the mill.
Sections covered include
the award is a means (the strategic frame);
transition versus the mill (the central choice, the transition partner who pulls a technology across the valley of death, the sole-source Phase III as a positioned-for asset);
the portfolio (diversification across agencies, topics, and customers, sequencing, parallel tracks, the proactive pipeline);
stacking the capital (state matching funds, the assistance programs, layering non-dilutive sources);
the private-capital bridge (venture capital, angels, seed, equity dilution, the majority-investor eligibility wrinkle, de-risking the technology for investors);
the market beyond the government (dual-use, commercialization, the National Science Foundation seed fund);
choosing what to pursue (opportunity cost, the distorting award);
scale and the UAV case;
and an Out of Scope section.
mathjax false (no equations).
No runnable code, so no Software Versions section.
Cross-links A134 (eligibility and the investor exception), A135 (the topic and solicitation), A137 (the commercialization plan), A138 (the valley of death), A140 (the money), and A112 (the running-case company) via post_url; the international-analogs article is referenced in prose pending A143.
20 references across Reference (11), Related Post (6), and Research (3) categories.

### After the Award, Compliance and Reporting for SBIR and STTR — Published

**File**: `_posts/2026-06-24-after_the_award_for_sbir_and_sttr.markdown`
**Topic**: The continuing obligations of holding an award, performing the work, reporting, invoicing, surviving audits, staying in good standing, and closing out, the second half of the campaign where past performance is built or destroyed; the tenth article of the SBIR/STTR practitioner-playbook series.
**Article Number**: A141
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-06-24 (19 references)

Standalone article and the tenth of the SBIR/STTR practitioner-playbook series.
Framed on the idea that an award is a binding agreement with continuing duties and that winning is the start of an obligation rather than the end of an effort.
Sections covered include
winning is the start (the award binds, contract or grant);
performing and who to talk to (milestones and deliverables, the contracting officer versus the technical point of contact, formal modifications, no-cost extensions, termination, subcontractor and partner management);
reporting (technical progress and final reports, the commercialization report that feeds the benchmarks, the late-report consequences);
invoicing and getting paid (the payment systems, the lag);
audits and the settling of rates (the Defense Contract Audit Agency, the incurred-cost true-up, the single audit, the audit trail and records retention);
compliance and integrity (the certifications, the False Claims Act, debarment, the defense cybersecurity obligation);
closing out;
continuing standing (registrations, accounting, benchmarks, past performance);
scale and the UAV case;
and an Out of Scope section.
mathjax false (no equations).
No runnable code, so no Software Versions section.
Cross-links A134 (eligibility), A136 (the Phase I proposal), A139 (data rights), A140 (the money), and A112 (the running-case company) via post_url; the strategy article is referenced in prose pending A142.
19 references across Reference (11), Related Post (5), and Research (3) categories.

### The Money Behind an SBIR or STTR Award — Published

**File**: `_posts/2026-06-23-money_behind_an_sbir_or_sttr_award.markdown`
**Topic**: The cost proposal, direct and indirect costs, the indirect rate, compliant accounting, and the cash flow that decide whether a company that won an award can survive it; the ninth article of the SBIR/STTR practitioner-playbook series, the one with arithmetic.
**Article Number**: A140
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-06-23 (18 references)

Standalone article and the ninth of the SBIR/STTR practitioner-playbook series, the one with arithmetic.
Framed on the idea that the award is a fixed pot and the company must justify it in a compliant budget, account for it in a way the government accepts, and finance the gap between spending it and being paid.
Sections covered include
the cost proposal (justify every dollar, fit the cap, match the work plan, evaluated for reasonableness, the agency budget format);
direct and indirect costs (the fringe, overhead, and general-and-administrative pools, equipment title);
the indirect rate (rate equals the indirect pool over an allocation base, the loaded-cost chain, provisional versus negotiated rates, the true-up risk);
fee and the two contract types (cost-reimbursement with a fee, fixed-price, grants without fee, no cost share);
compliant accounting (segregation, timekeeping, the Defense Contract Audit Agency, proportionate standards);
allowable and unallowable costs (the cost principles);
cash flow, the quiet killer (the lag and the gap, burn rate and runway, outside financing and the line of credit and factoring);
a note on assistance funds;
common money mistakes;
scale and the UAV case;
and an Out of Scope section.
mathjax true, with the indirect-rate and loaded-cost relations, the one article in the series with arithmetic.
No runnable code, so no Software Versions section.
Cross-links A136 (the Phase I proposal), A137 (Phase II), A138 (Phase III), and A112 (the running-case company) via post_url; the compliance and strategy articles are referenced in prose pending A141 and A142.
18 references across Reference (11), Related Post (4), and Research (3) categories.

### Data Rights and Intellectual Property in SBIR and STTR — Published

**File**: `_posts/2026-06-22-data_rights_and_intellectual_property_for_sbir_and_sttr.markdown`
**Topic**: The intellectual property a company keeps under the programs, patents under Bayh-Dole and the special SBIR data rights, the crown jewel that the non-dilutive funding was meant to build and that marking preserves; the eighth article of the SBIR/STTR practitioner-playbook series.
**Article Number**: A139
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-06-22 (16 references)

Standalone article and the eighth of the SBIR/STTR practitioner-playbook series, its crown-jewel article.
Framed on the idea that the government funds the work but the company keeps the inventions and the technical data, so the program is non-dilutive in intellectual property as well as equity, and the retained ownership is the asset the funding was meant to build, kept only by guarding it.
Sections covered include
two bodies of rights (patents versus data rights, and the STTR allocation with the research institution);
patent rights under Bayh-Dole (the company elects title, the election clock, march-in rights, the United-States-manufacturing preference);
SBIR data rights (the protected license, the protection period historically four years and since lengthened, background versus foreground);
marking is the act that preserves the rights (unmarked data risks unlimited rights, markings must conform, assertions can be challenged);
the categories of rights (unlimited, government-purpose, limited and restricted, the special SBIR category);
what the government keeps and what the company keeps;
threats to the crown jewel (subcontracts, omissions, expiry, over-delivery, mixed funding, open-source code);
how the rights create value (the sole-source position, the asset in a sale);
scale and the UAV case;
and an Out of Scope section.
mathjax false (no equations).
No runnable code, so no Software Versions section.
Cross-links A132 (orientation), A134 (eligibility), A136 (the Phase I proposal), A138 (Phase III), and A112 (the running-case company) via post_url; the money, compliance, and strategy articles are referenced in prose pending A140, A141, and A142.
16 references across Reference (9), Related Post (5), and Research (2) categories.

### Phase III and the Valley of Death for SBIR and STTR — Published

**File**: `_posts/2026-06-21-phase_iii_and_the_valley_of_death_for_sbir_and_sttr.markdown`
**Topic**: Phase III, the commercialization step that carries no SBIR funds, and the valley of death between a funded prototype and a self-sustaining product or fielded program, with the sole-source authority and the data rights as the tools for crossing it; the seventh article of the SBIR/STTR practitioner-playbook series.
**Article Number**: A138
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-06-21 (19 references)

Standalone article and the seventh of the SBIR/STTR practitioner-playbook series.
Framed on the idea that Phase III is a destination rather than an award, since it carries no program money, so the company must cross the valley of death from a funded prototype to a self-sustaining product or fielded program on other money.
Sections covered include
what Phase III is (no set-aside money, no dollar or time limit, the high technology-readiness rungs, the concrete funding sources, not strictly sequential);
the sole-source authority (the broad, non-expiring procurement lever, permission to buy and not a commitment);
the valley of death (the gap and why technologies die in it);
crossing by government transition (the program of record, the transition partner, the budget line, the acquisition pull, the prime-contractor path and its risk, the CRADA and the readiness program);
crossing by the market (the product, the customers, the venture capital, the Food and Drug Administration path, SBIR as an investor credential);
why Phase III is the point (the benchmarks measure it, the mill is the failure to reach it);
common ways to fall in;
scale and the UAV case;
and an Out of Scope section.
mathjax false (no equations).
No runnable code, so no Software Versions section.
Cross-links A132 (orientation), A134 (eligibility), A137 (Phase II), and A112 (the running-case company) via post_url; the data-rights, money, and strategy articles are referenced in prose pending A139, A140, and A142.
19 references across Reference (11), Related Post (4), and Research (4) categories.

### Phase II and the Commercialization Plan for SBIR and STTR — Published

**File**: `_posts/2026-06-20-phase_ii_and_the_commercialization_plan_for_sbir_and_sttr.markdown`
**Topic**: The Phase II development award and the commercialization plan that becomes a first-class scored deliverable, the step where a funded research result becomes a business or remains a research result; the sixth article of the SBIR/STTR practitioner-playbook series.
**Article Number**: A137
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-06-20 (20 references)

Standalone article and the sixth of the SBIR/STTR practitioner-playbook series.
Framed on the idea that Phase II is the step where the program stops asking whether the idea can work and starts asking whether it can become a product, so the money grows by an order of magnitude, the work turns from feasibility to development, and the commercialization plan becomes a scored deliverable.
Sections covered include
what Phase II builds (a prototype, the middle technology-readiness rungs, the base-and-option structure, the intellectual property);
the gate from Phase I (the sequence, the funding gap, Direct to Phase II, selection is not award);
the Phase II proposal (the shift of weight to commercialization, the work-split limit);
the commercialization plan as a deliverable (a business plan, the market analysis, the value proposition, the competition, the go-to-market strategy, product-market fit, documented commitments such as a memorandum of understanding, and the reporting that feeds the eligibility benchmarks);
transition versus market commercialization (the two agency cultures);
extending Phase II and bridging toward Phase III (the enhancement, the sequential Phase II, the commercialization readiness program);
the funding gap and cash flow;
common ways to lose Phase II;
scale and the UAV case;
and an Out of Scope section.
mathjax false (no equations).
No runnable code, so no Software Versions section.
Cross-links A132 (orientation), A133 (agency survey), A134 (eligibility), A136 (the Phase I proposal), and A112 (the running-case company) via post_url; Phase III and the money article are referenced in prose pending A138 and A140.
20 references across Reference (11), Related Post (5), and Research (4) categories.

### Writing the Phase I SBIR and STTR Proposal — Published

**File**: `_posts/2026-06-19-writing_the_phase_i_proposal_for_sbir_and_sttr.markdown`
**Topic**: Writing the Phase I proposal as an argument that the company can retire an idea's feasibility risk, written to the evaluation criteria, by a credible team, with a commercial promise; the proposal-craft core of the SBIR/STTR practitioner-playbook series.
**Article Number**: A136
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-06-19 (20 references)

Standalone article and the fifth of the SBIR/STTR practitioner-playbook series, its proposal-craft core.
Framed on the idea that a Phase I proposal is an argument that the company can retire the feasibility risk of an idea, written to the published evaluation criteria, by a believable team, with a commercial promise.
Sections covered include
what Phase I actually asks (feasibility and proof of concept, not a product, the overpromise as the classic failure, the technology-readiness staircase);
the volumes and their shape (the technical and cost volumes telling the same story, the project summary and public abstract, the proprietary markings, the page-limit boundary);
the sections of the technical volume;
the three things a reviewer scores (technical merit, qualifications, commercialization potential);
writing the innovation (the feasibility question, the technical risk to retire, plain technical writing);
the work plan (the work breakdown, milestones, deliverables, risk and mitigation, fitting the envelope, and setting up Phase II with go-or-no-go criteria);
the team and the past performance (the principal investigator and the work-split limits, the STTR partner);
the commercialization story (scored even in Phase I, dual-use, the customer letter);
writing to the reviewer (peer review at science agencies, government technical evaluation at directed agencies, clarity for a busy reader, the internal red-team review);
review, debrief, and resubmission (most proposals lose, the debrief is the prize, resubmit);
common ways to lose;
scale and the UAV case;
and an Out of Scope section.
mathjax false (no equations).
No runnable code, so no Software Versions section.
Cross-links A132 (orientation), A134 (eligibility), A135 (solicitation), and A112 (the running-case company) via post_url; Phase II is referenced in prose pending A137.
20 references across Reference (12), Related Post (4), and Research (4) categories.

### Finding a Topic and Reading an SBIR or STTR Solicitation — Published

**File**: `_posts/2026-06-18-finding_a_topic_and_reading_a_solicitation_for_sbir_and_sttr.markdown`
**Topic**: Finding the topic or funding opportunity that matches a company's capability and reading the solicitation precisely, the bridge between eligibility and the proposal; the fourth article of the SBIR/STTR practitioner-playbook series.
**Article Number**: A135
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-06-18 (16 references)

Standalone article and the fourth of the SBIR/STTR practitioner-playbook series.
Framed on the two tasks of the stage, finding the opportunity (a matching topic at a directed agency, fit within a broad area at an open one) and reading the solicitation as the contract for the competition.
Sections covered include
two kinds of looking;
where the opportunities live (the cross-agency portal, the agency systems, the calendar);
the anatomy of a solicitation, including tracking its amendments;
reading a topic (the objective, deliverables, target technology readiness level, the dual-use expectation, the keywords, and the customer-pull letters to begin lining up);
the pre-release window and talking to the agency (the directed-agency topic-author contact and the blackout versus the open-agency program-officer culture);
is it a fit and is it winnable (past-award intelligence from the searchable awards record, and the teaming and STTR-partner commitment);
reading for compliance (the cheapest loss, with the cost ceiling and period scoping the work);
writing to the evaluation criteria;
the open-agency path (the NSF project pitch, the NIH institute and funding opportunity);
scale and the UAV case;
and an Out of Scope section.
mathjax false (no equations).
No runnable code, so no Software Versions section.
Cross-links A132 (orientation), A133 (agency survey), A134 (eligibility), and A112 (the running-case company) via post_url.
16 references across Reference (8), Related Post (4), and Research (4) categories.

### SBIR and STTR Eligibility and the Registration Stack — Published

**File**: `_posts/2026-06-17-eligibility_and_the_registration_stack_for_sbir_and_sttr.markdown`
**Topic**: The two gates an applicant clears before any SBIR or STTR proposal, eligibility (what the company must be) and registration (getting it into the federal systems), with the registrations' lead time gating the calendar; the third article of the SBIR/STTR practitioner-playbook series.
**Article Number**: A134
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-06-17 (21 references)

Standalone article and the third of the SBIR/STTR practitioner-playbook series.
Framed on the two gates before a proposal, eligibility as a property of the company true or false on the day it applies, and registration as a multi-week sequence of accounts and identifiers whose lead time gates the calendar.
Sections covered include
eligibility, what the company must be (small with affiliation, for-profit, United States, the five-hundred-employee standard versus the industry-code standards, not a socioeconomic set-aside);
the ownership rules and the investor exception (more than half owned by United States individuals or small businesses, the venture, private-equity, and hedge-fund majority-ownership exception that is agency-specific);
the principal investigator and the work (the SBIR primary-employment requirement, the STTR flexibility, the work splits, the United States place of performance);
the performance benchmarks and the duplicate-funding and essentially-equivalent-work rule;
national-security eligibility (the 2026 screening), the export-control neighbor, and the certification-and-fraud framing (False Claims Act exposure);
the registration stack in order (Login.gov, the System for Award Management with the unique entity identifier and CAGE code, the program company registry and its control identifier, the agency portal);
why the stack gates the calendar (validation can take weeks, annual renewal, the registration-is-free warning);
scale and the small-company case;
and an Out of Scope section.
mathjax false (no equations).
No runnable code, so no Software Versions section.
Cross-links A132 (orientation), A133 (agency survey), and A112 (the running-case company) via post_url.
21 references across Reference (13), Related Post (3), and Research (5, the live federal systems) categories.

### A Survey of the SBIR and STTR Agencies — Published

**File**: `_posts/2026-06-16-survey_of_the_sbir_and_sttr_agencies.markdown`
**Topic**: A survey of the eleven SBIR and five STTR agencies for the practitioner choosing where to apply, organized on two axes (grant versus contract, directed versus open topics); the second article of the SBIR/STTR practitioner-playbook series.
**Article Number**: A133
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-06-16 (25 references)

Standalone article and the second of the SBIR/STTR practitioner-playbook series, in the business/funding/sbir category.
Organized on two independent axes, the award vehicle (grant or cooperative agreement versus procurement contract) and the topic (directed versus open), with the agencies populating the corners.
Sections covered include
the two axes and where the agencies sit;
how many agencies and why the sizes differ (eleven SBIR, five STTR, the set-aside making budget proportional to extramural research);
the Department of Defense (contract, directed, the components and the Defense SBIR/STTR Innovation Portal, transition, dual-use, the national-security screening);
the National Institutes of Health (grant, open, standing receipt dates);
the National Science Foundation (grant, broad, America's Seed Fund, the required project pitch);
the Department of Energy (grant but directed, the national-lab STTR fit);
NASA (contract, directed, transition to a NASA mission);
the smaller agencies (Agriculture, Homeland Security, Commerce with NOAA and NIST, Education, Transportation, Environmental Protection);
a comparison table (vehicle, topics, STTR, Direct to Phase II, relative size, character);
choosing where to apply (match by mission and by model, eligibility varying by agency, the cadence as a selection factor, differing post-award support);
and an Out of Scope section.
mathjax false (no equations).
No runnable code, so no Software Versions section.
Balanced across agencies per the series plan, with all time-sensitive specifics flagged as current-as-of.
Cross-links A132 (the orientation), A93 (mission-critical engineering, the Department of Defense culture), and A112 (the UAV as a dual-use example) via post_url.
25 references across Reference (16), Related Post (3), and Research (6, one authoritative portal per major agency) categories.

### An Introduction to the SBIR and STTR Programs — Published

**File**: `_posts/2026-06-15-introduction_to_the_sbir_and_sttr_programs.markdown`
**Topic**: Orientation to the United States SBIR and STTR programs, framed on non-dilutive capital staged against demonstrated risk reduction mapped to the technology readiness level; the first article of the SBIR/STTR practitioner-playbook series.
**Article Number**: A132
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-06-15 (18 references)

Standalone article and the first of a new series, the SBIR/STTR practitioner playbook, in a new category cluster (business/funding/sbir, permalink /business/funding/sbir/).
The master variable is non-dilutive capital staged against demonstrated reduction of risk, the three-phase staircase mapped to the technology readiness level.
Sections covered include
a program that runs on reauthorization (the 2025 lapse and the 2026 reauthorization through fiscal year 2031);
the core idea (non-dilutive, mission-pulled, the set-aside, the scale of over four billion dollars a year across roughly four thousand awards, America's Seed Fund);
the three phases (Phase I feasibility, Phase II development, Phase III commercialization with no SBIR funds and sole-source authority) with the technology-readiness-level mapping and the multi-year timeline;
SBIR versus STTR (the research-institution partner and the work splits);
who can compete (the eligibility gate and the 2026 national-security screening);
why the money is worth the trouble (non-dilutive, data rights, the valley of death);
what the programs are not (the grant-versus-contract distinction, not free money, not a substitute for a customer);
the series ahead;
and an Out of Scope section.
mathjax false (no equations).
No runnable code, so no Software Versions section.
Explicitly United States, with the international analogs deferred to a later article, and all time-sensitive figures flagged as current-as-of with the live solicitation and the SBA policy directive named as authoritative.
Cross-links A93 (mission-critical engineering), A112 (prototyping the UAV, the running case), and A131 (the risk-based regulatory framing) via post_url.
18 references across Reference (12), Related Post (3), and Research (3) categories.

### The Regulatory and Operations Layer for Fixed-Wing UAVs — Published

**File**: `_posts/2026-06-14-regulatory_and_operations_layer_for_fixed_wing_uavs.markdown`
**Topic**: The regulatory and operations layer above the engineering of a fixed-wing UAV, framed jurisdiction-neutrally on the principle that the authorization to operate is granted in proportion to demonstrated risk control, with kinetic energy as the physical proxy for harm; the sixth and final flagged extension.
**Article Number**: A131
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-06-14 (41 references)

Standalone aerospace article and the sixth and final flagged extension beyond the core fixed-wing-UAV arc, the layer above the engineering, with which the series and its extensions are now complete.
The master variable is the authorization to operate, granted in proportion to the risk an operation poses and the control the operator can demonstrate, with the impact kinetic energy E_k = (1/2) m v^2 as the physical proxy for harm tying the regulatory categories to the mass and speed the series worked in.
Explicitly jurisdiction-neutral, framed on the International Civil Aviation Organization and the Chicago Convention with the FAA, the European Union Aviation Safety Agency, the UK Civil Aviation Authority, the Civil Aviation Safety Authority, Transport Canada, and the Civil Aviation Administration of China named as examples, the thresholds presented as patterns that differ by state and change over time.
Sections covered include
regulation is jurisdictional;
authorization proportionate to risk (the open, specific, and certified pattern, ground risk and air risk, the specific operations risk assessment);
kinetic energy as the measure of harm;
the axes of risk (mass, line of sight, over people, altitude, airspace);
registration, identification, and competency with the autonomy-and-responsibility tension;
airworthiness and the certified end;
integrating with other traffic (segregated versus integrated, unmanned traffic management and U-space, detect and avoid, command-and-control reliability);
the operations layer (concept of operations, crew, pre-flight planning, maintenance, training, the safety management system, just culture, independent accident investigation);
contingency and containment (defined procedures, the geofence, flight termination, and command-link security as a regulatory concern);
adjacent regimes (spectrum and the telecommunication union, export control, privacy and data protection, property rights, insurance, and noise);
the boundary with space (the suborbital handoff to space law, the Outer Space Treaty, the Kármán line as a convention);
scale and the UAV case;
and an Out of Scope section.
MathJax for the kinetic-energy relation.
No runnable code, so no Software Versions section.
The pilot's instruction that not everyone is in the USA is honored throughout, the article naming authorities from several continents, framing the specifics as patterns that vary and change, directing the reader to the governing authority, and drawing its three Research sources from the international bodies (the International Civil Aviation Organization, the European Union Aviation Safety Agency, and the Joint Authorities for Rulemaking on Unmanned Systems for the risk assessment).
References A112, A125, A126, A127, and A130 via post_url.
41 references across Reference (33), Related Post (5), and Research (3) categories.

### Payload and Mission Systems for Fixed-Wing UAVs — Published

**File**: `_posts/2026-06-13-payload_and_mission_systems_for_fixed_wing_uavs.markdown`
**Topic**: The payload and mission system of a fixed-wing UAV, framed on the payload fraction and the share of the mass, power, volume, data, and energy budget that reaches the payload, including suborbital spaceplane payload delivery with payload-owned circularization.
**Article Number**: A130
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-06-13 (45 references)

Standalone aerospace article and the fifth extension beyond the core fixed-wing-UAV arc.
The master variable is the payload fraction and, more broadly, the share of the budgets the series tracked that reaches the payload rather than carrying it, the payload being the point and the platform the overhead.
Sections covered include
the payload fraction (size, weight, power, and cost);
a taxonomy of payloads (electro-optical and infrared, synthetic-aperture radar, signals intelligence, lidar, multispectral and hyperspectral, communications relay, delivery and agricultural, the loitering-munition effector, scientific);
integrating the payload with the platform (mass and center of gravity, power as hotel load with the peak-versus-average note, data with onboard storage and compression, heat, volume, vibration and isolation);
pointing and stabilization with the geolocation and target-location-error chain;
the mission system (tasking, edge versus downlink processing, sensor fusion, autonomy);
the payload sizes the aircraft with the aperture-sets-resolution physics (angular resolution and ground sample distance tying SWaP to standoff performance);
releasing and dropping payloads;
suborbital spaceplane payload delivery (the reusable carrier delivers an accurate release state near apogee and the payload owns circularization, Dv = v_circ - v_h);
scale and the UAV case (modular bays and interface standards, the loitering munition as payload-is-the-aircraft);
a worked example (a 20 percent payload fraction on the 25 kg aircraft, and the ~7.8 km/s circular speed at a 200 km apogee with the honest delta-v split);
and an Out of Scope section.
MathJax plug-and-chug formulae throughout.
No runnable code, so no Software Versions section.
The pilot's explicit inclusion, suborbital spaceplane payload delivery where orbital circularization around apogee is the payload's responsibility, is covered in its own section, with the orbital mechanics after release held out of scope except for the handoff delta-v.
References A120, A121, A125, A126, A127, and A128 via post_url.
45 references across Reference (37), Related Post (6), and Research (2) categories.

### An Aerobatic Maneuver Reference Catalog for Fixed-Wing UAVs — Published

**File**: `_posts/2026-06-12-aerobatic_maneuver_reference_catalog_for_fixed_wing_uavs.markdown`
**Topic**: A reference catalog of 79 named aerobatic maneuvers, each classified in the A128 costed-trajectory model, alphabetical with stable family-prefixed IDs; the reference companion to A128.
**Article Number**: A129
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-06-12 (32 references; 79 catalog rows)

Standalone aerospace reference article and the fourth extension beyond the core fixed-wing-UAV arc, the reference companion to the A128 model.
Written for the UAV operator and the autonomy, not the human pilot.
A 79-row alphabetical catalog with a stable family-prefixed identifier per maneuver across twelve families (lines, turns, rolls, loops and eights, partial loops and combinations, stall turns, tailslides, spins, post-stall and supermaneuvers, three-dimensional and prop-hang figures, basic fighter maneuvers, composite or display).
Columns are the identifier, the maneuver, the family, the spatiotemporal path, the energy-height behavior, the peak load class, and the regime ceiling with flags.
Maneuver definitions are cited to the Aresti catalog, the world air sports federation, the International Aerobatic Club, the basic-fighter-maneuver repertoire, and Wikipedia where an article exists.
The cost classification is forward-declared as an original, qualitative synthesis with three stated limitations, since no catalog tabulates the energy-height behavior, the load class, and the regime ceiling per maneuver.
Sections covered include
how to read the table;
why the thermal cost is folded into the regime column;
provenance and limitations;
the catalog;
maneuvers without a closed form (spins, snaps, the cobra, the Kulbit, the Herbst maneuver, the gyroscopic tumbles, and the three-dimensional and prop-hang figures, with what can still be said);
parametric families;
alternate names;
using the catalog;
reading a row in numbers (the break turn read into the corner-speed and load figures of the structures and model articles);
Out of Scope;
and a conclusion.
MathJax enabled for the model symbols.
No runnable code, so no Software Versions section.
The honesty of the catalog rests on a clear division, the maneuver definitions sourced to the established catalogs and the cost classification offered as an original synthesis to be checked rather than as measured data.
References A120, A123, A125, A127, and A128 via post_url.
32 references across Book (1), Reference (26), and Related Post (5) categories.

### Aerobatics as Costed Trajectories for Fixed-Wing UAVs — Published

**File**: `_posts/2026-06-11-aerobatics_as_costed_trajectories_for_fixed_wing_uavs.markdown`
**Topic**: UAV aerobatics treated as commanded spatiotemporal trajectories priced in energetic, structural, and thermal cost across the subsonic, supersonic, and hypersonic regimes, with a hypothetical spaceplane reentry case; the synthesis capstone of the extension set.
**Article Number**: A128
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-06-11 (42 references)

Standalone aerospace article and the third extension beyond the core fixed-wing-UAV arc (after A126 communications and A127 structures), the synthesis capstone of the extension set.
Written for the UAV operator and the autonomy and explicitly not for the human pilot, treating a maneuver as a commanded spatiotemporal trajectory rather than a learned skill.
The master variable is the energy state and the specific excess power Ps = V(T - D)/W = dh_e/dt, with every maneuver a transaction in potential, kinetic, and propulsive energy and three costs (energetic, structural, thermal) whose dominant term migrates with the speed regime.
Sections covered include
a maneuver as a trajectory;
the energy state and specific excess power (energy height h_e = h + V^2/2g, energy-maneuverability theory);
the three costs and the control-authority-and-bandwidth feasibility gate;
the kinematic primitives and the maneuverability (doghouse) diagram with its lift, structural, and sustained bounds;
a scored catalogue table of ten maneuvers (path, peak load, energy-height behavior, highest surviving regime, with the post-stall spin and cobra flagged as no-closed-form);
the footprint in space and time (airspace volume, time, wind drift, deconfliction);
the subsonic regime (figure flying, the no-human-ceiling advantage, negative-g and outside figures);
the transonic and supersonic regimes (wave drag, Ps collapse, Mach tuck, the shrinking catalogue);
the hypersonic regime (stagnation heating dominant, bank-angle modulation and S-turns, boost-glide and HGV referents);
spaceplane maneuvering during reentry (the corridor, bank reversals and angle of attack, the Shuttle's forty-degree alpha and cross-range, control authority migrating from RCS to surfaces per A122);
spaceplane maneuvering after the thermal wall (terminal-area energy management, tying A124 and A125);
scale and the UAV case (favorable structural scaling, the loitering-munition terminal maneuver, the energy and powertrain-thermal bounds);
a worked example on the 25 kg series aircraft (level turn radius and rate, the corner turn, a loop sized by the energy-height trade, a Mach-five thermal note);
and an Out of Scope section.
MathJax plug-and-chug formulae throughout, honest where no closed form exists.
No runnable code, so no Software Versions section.
The term aerobatics is extended to commanded maneuvering, with an explicit lampshade that figure flying does not survive the hypersonic and reentry regimes.
References A120, A122, A123, A124, A125, and A127 via post_url.
42 references across Book (1), Reference (33), Related Post (6), and Research (2) categories.

### Structures and the Flight Envelope for Fixed-Wing UAVs — Published

**File**: `_posts/2026-06-10-structures_and_the_flight_envelope_for_fixed_wing_uavs.markdown`
**Topic**: The airframe structure and the flight envelope of a fixed-wing UAV, framed on the load factor and the load-versus-speed (V-n) diagram, the boundary the whole series operates inside; the second extension beyond the core arc.
**Article Number**: A127
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-06-10 (42 references)

Standalone aerospace article and the second extension beyond the core fixed-wing-UAV arc (after A126 communications).
The master variable is the load factor n = L/W and the load-versus-speed diagram, the flight envelope bounded by the stall parabola, the structural limit-load line, and the maximum-speed line, with the structure sized to its corners.
Sections covered include
the flight envelope;
the corner and the maneuvering speed;
limit load and ultimate load (the 1.5 factor of safety);
categories and the width of the envelope (normal, utility, aerobatic);
the gust envelope (sharp-edged and derived gust, the light-UAV gust sensitivity);
loads beyond the flight envelope (launch, recovery, touchdown through the undercarriage, taxi and handling, tying A116 and A124);
how the structure carries the load (bending, shear, torsion, asymmetric and combined cases, spar/rib/longeron, monocoque and stressed skin, tying A112);
material, stress, buckling, and the margin of safety (specific strength and modulus, the before-yield instability of thin panels, strength versus stiffness);
fatigue and the life of the structure (the stress-life curve, safe-life, fail-safe, damage-tolerant);
aeroelasticity and the flutter boundary (divergence, control reversal, flutter as a dynamic-pressure wall, tying A112 and A123);
the aerobatic envelope (the widest symmetric diagram, negative-g structure, and the UAV no-pilot point tying loitering munitions, with the maneuver art and physiology out of scope);
the envelope is not fixed (density altitude, the A120 thermal wall, composite knockdown, fatigue, autopilot envelope protection tying A123/A125);
proving the structure (the static ultimate-load test, flutter clearance by ground vibration test and stepped envelope expansion, and the fatigue test article);
scale and the UAV case (square-cube structural fraction, composite and printed structures, attritable design);
a worked example on the 25 kg series aircraft (stall speed about 18 m/s, corner speed about 38 m/s, limit and ultimate loads, a gust increment that rivals the maneuver limit);
and an Out of Scope section.
MathJax plug-and-chug formulae throughout.
No runnable code, so no Software Versions section.
The pilot's pre-draft question, whether aerobatics belongs, is answered in the article by covering aerobatics as the envelope's widest symmetric case.
References A112, A116, A120, A123, and A124 via post_url.
42 references across Book (1), Reference (33), Related Post (5), and Research (3) categories.

### Communications and the Command-and-Control Data Link for Fixed-Wing UAVs — Published

**File**: `_posts/2026-06-09-communications_and_the_command_and_control_data_link_for_fixed_wing_uavs.markdown`
**Topic**: The command-and-control data link of a fixed-wing UAV, framed on the link budget (received power versus noise) with latency as the companion constraint; the first extension beyond the core arc.
**Article Number**: A126
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-06-09 (34 references)

Standalone aerospace article and the first extension beyond the core fixed-wing-UAV arc (which closed with the A125 capstone).
The master variable is the link budget, P_rx = P_tx + gains - free-space path loss, with the signal-to-noise margin setting range and the Shannon limit bounding data rate, and latency as the companion constraint that decides what can be controlled over the link.
Sections covered include
the link budget (Friis, free-space path loss, SNR, Shannon, Fresnel, ISM bands, the frequency range-versus-rate trade, near-ground multipath and the two-ray ground reflection, the regulatory cap on effective radiated power);
the radio horizon;
the moving aircraft (airframe shadowing, radiation-pattern nulls and polarization, antenna diversity, a tracking ground antenna);
the three streams (command uplink, telemetry downlink, payload downlink with codec compression latency);
radio control with a handheld transmitter (2.4 GHz FHSS, ExpressLRS, CRSF/SBUS handoff, the control-link packet rate, FPV, failsafe, the manual path);
computer-controlled transmission (MAVLink, SiK/RFD900 telemetry radios, the ground control station, companion computer over cellular, intent versus stick inputs, coexisting with the handheld link);
beyond line of sight (relay, cellular, SATCOM via Iridium);
latency and why the fast loops are aboard (tying A123 and A125);
security and jamming (J/S ratio, spread spectrum, AES encryption, spoofing, directional antenna);
lost link (the preset failsafe, geofence, tying A116 and A125);
scale and the UAV case (the radios as part of the A121 hotel load);
a worked example (a 100 mW 2.4 GHz link closing 10 km with a 12 dB margin, a ~48 km radio horizon, kbps command versus Mbps video, LOS versus SATCOM latency);
and an Out of Scope section.
MathJax plug-and-chug formulae throughout.
No runnable code, so no Software Versions section.
The pilot's explicit requirement, RC control via both a consumer handheld controller and a computer-controlled transmitter, is covered in its own two sections framed as the coexisting manual and autonomous paths.
References A116, A121, and A125 via post_url.
34 references across Reference (28), Related Post (3), and Research (3) categories.

### Guidance, Navigation, and Automatic Landing for Fixed-Wing UAVs — Published

**File**: `_posts/2026-06-08-guidance_navigation_and_automatic_landing_for_fixed_wing_uavs.markdown`
**Topic**: The outer-loop autonomy of a fixed-wing UAV, framed on the feedback loop that drives the error between the navigation estimate and the guidance command to zero; the capstone of the set.
**Article Number**: A125
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-06-08 (29 references; 333 lines)

Standalone aerospace article and the tenth and capstone entry in the fixed-wing-UAV set (A112 airframe, A114 runway, A116 launch and recovery, A118 propulsion, A120 staged and boosted propulsion, A121 electric energy systems, A122 stability and control, A123 dynamic stability and control, A124 landing gear and touchdown, A125 guidance, navigation, and automatic landing).
Takes up the outer loop A123 set up.
The master variable is the feedback loop that drives the error between the commanded state (guidance) and the estimated state (navigation) to zero, nested by bandwidth, with the automatic landing as the tightest loop.
Sections covered include
the nested loops (inner attitude, outer guidance, mission, bandwidth separation, digital sample rates and latency);
navigation (GNSS, INS/IMU, dead reckoning, Kalman fusion, air data, RTK, initialization, GNSS-denied vision);
guidance (waypoints, cross-track error, the look-ahead path-following law);
wind and the ground track (crab, the wind triangle, the small-UAV case);
closing the loop with energy (the total energy control system as the real-time version of the series' energy budget);
the approach and automatic landing (glideslope, flare, RTK/radar-altimeter/vision, touchdown dispersion tied to the runway width) with the automatic-takeoff bookend;
when the loop breaks (GNSS loss, lost link, geofence, return-to-launch, redundancy, flight termination);
scale and the UAV case (Pixhawk-class boards, ArduPilot/PX4, the autonomy spectrum);
a worked example (loop bandwidth separation, the cross-track law, the navigation error budget, the glideslope dispersion);
and an Out of Scope section.
MathJax plug-and-chug formulae throughout.
No runnable code, so no Software Versions section.
References A114, A116, A123, and A124 via post_url, and the conclusion ties the whole ten-article set together.
29 references across Reference, Related Post, and Research categories.
333 lines.

### Landing Gear and the Physics of Touchdown for Fixed-Wing UAVs — Published

**File**: `_posts/2026-06-07-landing_gear_and_the_physics_of_touchdown_for_fixed_wing_uavs.markdown`
**Topic**: Landing gear and the surface interfaces of a fixed-wing UAV, framed on the touchdown energy absorbed over a stroke, complementing the runway and recovery articles.
**Article Number**: A124
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-06-07 (23 references; 320 lines)

Standalone aerospace article and the ninth in the fixed-wing-UAV set (A112 airframe, A114 runway, A116 launch and recovery, A118 propulsion, A120 staged and boosted propulsion, A121 electric energy systems, A122 stability and control, A123 dynamic stability and control, A124 landing gear and touchdown).
The master variable is the touchdown energy absorbed over a stroke, n = v^2/(2 g0 d), the energy-and-stroke idea of the recovery article applied to the final surface interface.
Sections covered include
the touchdown energy and the stroke;
wheels and landing gear (retractable versus fixed, tricycle and conventional layout, the oleo strut as gas spring and oil damper, recoil damping and bounce, frangible and sacrificial gear, spin-up and side gear loads, the gear-up fallback);
skids (sacrificial skids, friction stroke, skis and tundra tires by surface);
water landings (floatplane, flying boat, planing and the step, ditching, porpoising);
drogue and main parachutes (the drogue-before-main staging, with the residual touchdown energy taken by an airbag or crush);
deliberate impact (intentional lithospheric and hydrospheric intersection, crushable crashworthy structure for expendable vehicles);
energy bleeding before touchdown (spoilers, forward slip, S-turns, flare, with the honest distinction that true aerobraking is an orbital maneuver while a boost-glide or ramjet or scramjet vehicle does thermally limited atmospheric deceleration);
scale and the UAV case;
a worked example (sink-rate, parachute, and deliberate-impact loads set by the stroke);
and an Out of Scope section.
MathJax plug-and-chug formulae throughout.
No runnable code, so no Software Versions section.
Complements rather than duplicates the launch-and-recovery article.
References A114, A116, A120, and A122 via post_url.
23 references across Reference, Related Post, and Research categories.
320 lines.

### Dynamic Stability and Control for Fixed-Wing UAVs — Published

**File**: `_posts/2026-06-06-dynamic_stability_and_control_for_fixed_wing_uavs.markdown`
**Topic**: Dynamic stability and control of a fixed-wing UAV, framed on the damping and frequency of the aircraft's natural modes, the dynamic sequel that completes the stability-and-control arc begun by the static-stability article.
**Article Number**: A123
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-06-06 (22 references; 316 lines)

Standalone aerospace article and the eighth in the fixed-wing-UAV set (A112 airframe, A114 runway, A116 launch and recovery, A118 propulsion, A120 staged and boosted propulsion, A121 electric energy systems, A122 stability and control, A123 dynamic stability and control).
Takes up the dynamic question A122 deferred.
The master variable is the damping and frequency of the natural modes, with the aircraft modeled as a damped harmonic oscillator where static stability is the spring, inertia the mass, and aerodynamic rate forces the damping.
Sections covered include
the spring, the mass, and the damping (with a small-disturbance about-trim caveat);
the longitudinal modes (short-period, phugoid);
the lateral-directional modes (roll subsidence, spiral, Dutch roll, with the spiral-versus-Dutch-roll trade tied to A122's dihedral-versus-weathercock balance);
damping, frequency, and handling qualities (settling time, Cooper-Harper, flying-qualities levels);
gusts and ride quality (turbulence excitation and the small-UAV gust sensitivity);
stability augmentation (yaw damper, pitch damper, rate feedback from an IMU, the SAS inner loop, augmentation limits and pilot-induced oscillation, and the SAS-versus-CAS distinction);
fly-by-wire and relaxed static stability;
scale and the UAV case (faster modes, autopilot and actuator bandwidth);
a worked example (Dutch-roll damping from 0.05 to 0.4 with a yaw damper, and a phugoid period);
and an Out of Scope section that defers derivative estimation and the equations of motion, control-law synthesis, sensors and state estimation, structural and aeroelastic dynamics, departure and spin, and the outer-loop guidance, navigation, and automatic landing.
MathJax plug-and-chug formulae throughout.
No runnable code, so no Software Versions section.
References A112, A114, and A122 via post_url.
22 references across Reference, Related Post, and Research categories.
316 lines.

### Stability, Control, and Configuration for Fixed-Wing UAVs — Published

**File**: `_posts/2026-06-05-stability_control_and_configuration_for_fixed_wing_uavs.markdown`
**Topic**: Stability, control, and configuration of a fixed-wing UAV, framed on the balance of moments about the center of gravity with the static margin as the master proxy for the stability-versus-maneuverability trade.
**Article Number**: A122
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-06-05 (46 references; 409 lines)

Standalone aerospace article and the seventh in the fixed-wing-UAV set (A112 airframe, A114 runway, A116 launch and recovery, A118 propulsion, A120 staged and boosted propulsion, A121 electric energy systems, A122 stability and control).
Takes up the full stability-and-control treatment A112 deferred.
The master variable is the moment balance about the center of gravity, with the static margin K_n = (x_np - x_cg)/MAC as the proxy for the stability-versus-maneuverability trade.
Sections covered include
the moment balance and the static margin (with the center-of-gravity range across the loading envelope);
lateral and directional static stability (fin weathercock stability and dihedral);
airfoils, camber, and invertibility;
configuration archetypes (conventional empennage, canard, tandem, tailless flying wing with sweep, washout, and reflex);
control surfaces by placement and name (elevator, aileron, rudder, elevon, ruddervator, stabilator, flaperon) with adverse yaw;
high-lift and spoiler devices;
control authority and dynamic pressure, running from aerodynamic surfaces through differential thrust and thrust vectoring to a reaction control system (spaceplane RCS and cold-gas thrusters, tied to A120's boost-glide arc, with an honest low-altitude caveat);
the wing tradeoff (aspect ratio versus wing loading, speed versus glide, planform);
the trim-drag energy cost;
a worked example (static margin and tail volume coefficient, with a flying-wing reflex contrast);
and an Out of Scope section that defers the dynamic-stability modes, control-law design, RCS detailed design, and the translational orbital problem (orbital mechanics, the orbital maneuver, and stationkeeping, affirmed as legitimate for spacecraft that reach orbit).
MathJax plug-and-chug formulae throughout.
No runnable code, so no Software Versions section.
References A112, A114, and A118 via post_url.
46 references across Reference, Related Post, and Research categories.
409 lines.

### Electric Energy Systems and the Endurance Budget for Fixed-Wing UAVs — Published

**File**: `_posts/2026-06-04-electric_energy_systems_and_endurance_budget_for_fixed_wing_uavs.markdown`
**Topic**: The electric energy economy of a fixed-wing UAV, framed as a state-of-charge energy-flow budget (supply minus demand, buffered by storage), the flow counterpart to A120's stock budget.
**Article Number**: A121
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-06-04 (29 references; 381 lines)

Standalone aerospace article and the sixth in the fixed-wing-UAV set (A112 airframe, A114 runway, A116 launch and recovery, A118 propulsion, A120 staged and boosted propulsion, A121 electric energy systems).
Fills the solar, fuel-cell, hybrid, and battery-management items A118 deferred.
The master variable is the energy-flow budget, the power balance dE/dt = P_in - P_out and its integral over the harvest cycle, contrasted explicitly with A120's one-time energy stock (stock versus flow).
Sections covered include
the energy-flow budget;
the demand side and the hotel load (flight power versus a fixed non-propulsive floor);
storage as the buffer (specific energy, depth of discharge, round-trip efficiency, cold derating, the specific-energy-versus-specific-power tradeoff, the battery wall, supercapacitor for peaks);
harvesting from the sun (output = efficiency times area times irradiance, the daily account, MPPT named);
the scale gate for solar perpetual flight (square-cube, Pathfinder/Helios/Zephyr/Solar Impulse);
harvesting from hydrogen (PEM fuel cell, Ion Tiger, Phantom Eye);
hybrid systems (series and parallel);
harvesting from the air (thermal and dynamic soaring);
the perpetual-flight closure (daily harvest at least daily demand, night energy within usable storage, cycle-life bounding the campaign);
a worked example on the 25 kg series aircraft;
and an Out of Scope section.
MathJax plug-and-chug formulae throughout.
No runnable code, so no Software Versions section.
The thesis is that sustained flight is a balance of powers rather than a quantity of energy, and indefinite flight is the cycle closing on itself, which the large light high-flying solar aircraft achieves and the small one does not.
References A112, A118, and A120 via post_url.
29 references across Reference, Related Post, and Research categories.
381 lines.

### Staged and Boosted Propulsion for Small Fixed-Wing UAVs — Published

**File**: `_posts/2026-06-03-staged_and_boosted_propulsion_for_fixed_wing_uavs.markdown`
**Topic**: Staged and boosted propulsion for a ~2m fixed-wing UAV, framed around the post-boost mission energy budget (potential plus kinetic plus stored propulsive energy).
**Article Number**: A120
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-06-03 (40 references; 472 lines)

Standalone aerospace article and the fifth in the fixed-wing-UAV set (A112 airframe, A114 runway, A116 launch and recovery, A118 propulsion, A120 staged and boosted propulsion).
Reopens the high-speed families A118 ruled out of regime by adding a boost stage, and is framed throughout as the management of the post-boost mission energy budget.
The boost deposits potential and kinetic energy (Tsiolkovsky rocket equation, specific impulse, one versus two stage), to which stored propulsive energy is added, and the kinetic share sets the stagnation temperature and therefore the airframe material.
Sections covered include
the mission energy budget with the energy height h_e = h + V^2/2g;
the boost stage;
the thermal wall (stagnation temperature versus Mach, aerodynamic heating, altitude and duration relief);
airframe materials by regime (LW-PLA subsonic, aluminum/composite transonic, titanium/steel supersonic with the SR-71 anchor, superalloy/refractory/CMC/carbon-carbon/UHTC/active-cooling/ablative hypersonic with the X-43 and X-51 anchors);
airframe archetypes for spending the budget (vertical-fighter banking it as altitude with the Bachem Natter anchor, maneuverable descending spending it on lift with lifting-body/waverider/HGV/MaRV members, and conventional holding it level on propulsion);
boost-glide with range (L/D)(h + V^2/2g);
boost-sustainer (RATO and the cruise-missile boost-turbojet);
boost-ramjet (integral rocket-ramjet, GQM-163 Coyote, Mach 2-4 titanium airframe);
boost-scramjet (X-43, X-51, hypersonic materials, research-grade honesty);
boost-throttleable-rocket;
one stage versus two;
a worked example on a 2 m vehicle (propellant fraction and stagnation temperature to Mach 2 and Mach 5, with the Mach-5 energy height of about 147 km);
and an Out of Scope section.
MathJax plug-and-chug formulae throughout.
No runnable code, so no Software Versions section.
The thesis is that the ~2m scale forbids none of these configurations, since material and budget, not size, set how far up the speed ladder a prototype can be carried.
References A112, A114, A116, and A118 via post_url.
40 references across Reference, Related Post, and Research categories.
472 lines.

### Propulsion and Power Sizing for Small Fixed-Wing UAVs — Published

**File**: `_posts/2026-06-02-propulsion_and_power_sizing_for_fixed_wing_uavs.markdown`
**Topic**: Sizing the propulsion and power system of a small fixed-wing UAV, worked outward from the power-required master variable.
**Article Number**: A118
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-06-02 (36 references; 445 lines)

Standalone aerospace article and the fourth in the fixed-wing-UAV set (A112 airframe, A114 runway, A116 launch and recovery, A118 propulsion).
Establishes the power-required master variable, where power is thrust times speed and thrust in level flight is drag, so the power to fly is the weight times the speed divided by the lift-to-drag ratio, and works through
the drag polar and lift-to-drag ratio;
propellers and efficiency via momentum theory, static thrust, and advance ratio, including the electric ducted fan;
the thrust-to-weight and launch and climb case that usually sizes the powertrain, tying back to A114 and A116;
electric propulsion (battery specific energy, brushless motor, the endurance equation, and the battery wall);
combustion propulsion (two-stroke and Wankel, brake-specific fuel consumption, heavy fuel, range and endurance);
altitude and available power (the density-altitude lapse of engine power and propeller thrust);
endurance and range with reserves (endurance at the minimum-power speed, range at the best lift-to-drag speed for a propeller aircraft);
a brief solar, hybrid, and fuel-cell note;
jets and regimes beyond the propeller (turbojet and turbofan in scope; ramjet, scramjet, throttleable rocket, and rocket boost-glide named and declared out of regime);
a worked example on the 25 kg series aircraft;
and an Out of Scope section.
MathJax plug-and-chug formulae throughout.
No runnable code, so no Software Versions section.
Real-UAV anchors RQ-7 Shadow (Wankel), ScanEagle (heavy-fuel piston), and RQ-20 Puma (electric).
References A112, A114, and A116 via post_url.
36 references across Reference, Related Post, and Research categories.
445 lines.

### Three Audiences for an Operating System — Published

**File**: `_posts/2026-05-22-three_audiences_for_an_operating_system.markdown`
**Topic**: Prequel to the BTRON-hypermedia trilogy. Names the operator-as-end-user category as a distinct third audience for an operating system, alongside the consumer and the developer. Sets up the question that A113, A115, and A117 then answer.
**Article Number**: A119
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-05-22 (61 references; 1,364 lines)

Standalone category-framing article and the prequel to the BTRON-hypermedia trilogy (A113, A115, A117).
Sections covered include
Opening on who an operating system serves;
The Three Audiences (consumer, developer, operator with role definitions and the load-bearing authority concept);
The Consumer Answer (Apple HIG, Windows UX Guidelines, GNOME HIG, KDE HIG, Material Design);
The Developer Answer (Unix philosophy, Emacs, Vim, Visual Studio Code, Git, Cargo, npm, pip);
The Operator (the unfilled category);
A Short History of Operator-Facing Computing (Sketchpad, NLS, MOCR, Alto, Macintosh, BTRON, HyperCard, OpenDoc, GNOME Bonobo, SCADA, PLCs, ARINC 661, ISA-101, NUREG-0700, IEC 62366, ISO 9241, ASM Consortium);
Why the Consumer Answer Fails the Operator (five structural failure modes);
Why the Developer Answer Also Fails (four structural failure modes);
The Operator Population Today (aerospace, medical, industrial, defense and intelligence, legal and regulatory, financial markets);
A Scorecard of Audience Requirements (10-row table across consumer, developer, operator);
The Gap That Remains;
Out of Scope (defers the substantive solution, the language substrate, and the worked vertical to the trilogy);
Conclusion.

References:
61 references across Reference (58) and Related Post (3) categories.
All inline-linked per project style.
A113, A115, and A117 cited via post_url as the deferred follow-ups.
No internal research cited.
A research agent verified the operator-specific references (ISA-101, ASM Consortium, IEC 62366, ISO 9241, NUREG-0700, ARINC 661, glass cockpit, SCADA, HITL, ergonomics, alarm fatigue) and the audience-contrast sources (Apple HIG, Windows UX, GNOME HIG, KDE HIG, Unix philosophy).

### Launch and Recovery Systems for Fixed-Wing UAVs — Published

**File**: `_posts/2026-06-01-launch_and_recovery_systems_for_fixed_wing_uavs.markdown`
**Topic**: Runway-independent launch and recovery for fixed-wing UAVs, worked outward from the energy-and-stroke master variable.
**Article Number**: A116
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-06-01 (26 references; 478 lines)

Standalone aerospace article and the runway-independent companion to A114.
Establishes the energy-and-stroke master variable, where launch must add and recovery must remove a kinetic energy fixed by mass and flying speed and the g-load rises as the stroke shrinks, and works through
launch by catapult (bungee, pneumatic, hydraulic, rail), winch and aerotow, booster, and zero-length launch;
recovery by net and cable (Skyhook), arrested landing, parachute and airbag, belly skid, and high-alpha braking (deep stall, cobra braking as a routine procedure, and perched landing);
wind and environment;
the acceleration limit;
failure and abort modes, with the fail-safe principle and a flight-termination or controlled-ditch option;
matching launch to recovery with real-UAV anchors (ScanEagle, RQ-7 Shadow, RQ-21 Blackjack);
airframe implications;
a worked numeric example;
and a fully declared Out of Scope.
MathJax plug-and-chug formulae throughout.
No runnable code, so no Software Versions section.
References A114 (Runway Sizing for Fixed-Wing UAVs) and A112 (Prototyping Fixed-Wing Aircraft with Lightweight PLA and Fiberglass) via post_url.
26 references across Reference, Related Post, and Research categories.
478 lines.

### Human Spaceflight Ground Systems as an Illustrative Vertical for a Hypermedia Desktop — Published

**File**: `_posts/2026-05-25-human_spaceflight_ground_systems_as_illustrative_vertical.markdown`
**Topic**: Vertical-specific follow-up to A113 and A115. Walks through human spaceflight ground systems in the Apollo lineage, lampshaded as an illustrative example vertical with explicit extrapolation guidance to modern crewed launch and on-orbit operations. Includes a Day-in-the-Launch-Operator's-Workflow walkthrough and six verified Keleusma code samples for the load-bearing claims.
**Article Number**: A117
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-05-25 (40 references; 1,944 lines)

Sections covered include
The Apollo Reference (MOCR, RTCC on IBM System/360 Model 75, LCC and Firing Rooms, MSFN, NASCOM, Flight and Mission Rules, simulators, recovery, the flight directors and Apollo 13);
Extrapolation to Modern Requirements (CCSDS, Commercial Crew Program, ISS Multilateral Coordination, Artemis and Human Landing System, FAA Part 450, NPR 7150.2 and NASA-STD-8719.13 and NPR 8705.2, ITAR);
The Hypermedia Object Model in Launch Operations (six commitments with Apollo-to-hypermedia mapping table);
Engineering Commitments in Launch Operations (five commitments with five Keleusma code samples and a mapping table);
The Ten-Layer Architectural Sketch in Launch Operations (full table inheriting A115 verdicts and clarifying each layer's launch role);
A Day in the Launch Operator's Workflow (eleven scenes from pre-launch shift report through post-flight review);
Trust and Provenance;
Certification and Regulatory Posture;
Why This Vertical Is a Good Illustration (and where it is hard);
Risks and Open Questions;
Out of Scope (link store schema, certification path, contractor selection deferred to future posts);
Conclusion.

Six verified Keleusma code samples in `tmp/a117/`:
01_countdown_sequencer.kel (loop main compiles to 260 bytes);
02_telemetry_alarm.kel (Proprietary -> displayable bucket, returns 1);
03_abort_decision.kel (Sensitive -> typed outcome, returns 2);
04_abort_decision_reject.kel (same without declassify, compile-time reject);
05_mission_rules.kel (const data registry, returns 300);
06_signed_flight_rules.kel (signed entry function compiles to 232 bytes).

References:
40 references across Reference (37), Related Post (2), and Research (1) categories.
All inline-linked per project style.
A113 and A115 cited via post_url.
Apollo-era and contemporary primary sources verified by a parallel research agent.
No internal Keleusma research cited.

### Keleusma as a Substrate for a Real-Time Hypermedia Desktop — Published

**File**: `_posts/2026-05-24-keleusma_as_substrate_for_real_time_hypermedia_desktop.markdown`
**Topic**: Follow-up to A113. Maps Keleusma V0.2.0 capabilities and the public V0.5+ roadmap onto A113's six structural commitments of the hypermedia object model, the five engineering commitments for real-time hypermedia composition, and the ten-layer architectural sketch. Vertical-agnostic by design; the vertical-specific treatment is deferred to a separate follow-up.
**Article Number**: A115
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-05-24 (45 references; 1,701 lines)

Analytical follow-up to A113. Sections covered include
What Keleusma Provides at Version 0.2.0;
The Six Structural Commitments of the Hypermedia Object Model;
The Five Engineering Commitments for Real-Time Hypermedia;
Mapping the Ten-Layer Architectural Sketch (ten verdicts: two strong fits, five partial fits, three mismatches);
What Keleusma Uniquely Provides (verified totality, verified WCET/WCMU, language-level IFC);
What Keleusma Does Not Provide (mature ecosystem, general-purpose breadth, authoring tooling);
The Asymmetry and Its Implication;
The Roadmap Path (V0.3.0 self-hosted compiler through V0.5.x interval-graph refinement);
What Would Need to Be Built;
Risks and Open Questions;
Out of Scope (vertical choice, detailed link store design, certification path all deferred to separate posts);
Conclusion.

Five illustrative Keleusma code samples verified against the installed keleusma 0.2.0 CLI:
01_typed_part.kel (Citation struct, runs and returns 42);
02_handler_loop.kel (loop main with yield, compiles to 228-byte bytecode);
03_ifc_sanitiser.kel (classify/declassify sanitiser pattern, runs and returns 200);
04_ifc_reject.kel (same without declassify, verifier rejects at compile time);
05_preallocated.kel (const data block, runs and returns 20).

All examples in `tmp/a115/`.

References:
45 references across Reference (38), Related Post (5), and Research (1) categories.
Inline citations throughout per project style.
A113, A107, A109, A110, A111 cited via post_url.
No internal Keleusma research material cited; only public Keleusma artefacts (README, crates.io, docs.rs, GitHub).

**Remaining Work**:
Human review of analytical claims and the Keleusma-to-BTRON mapping.
Confirm publication date and assign final timestamp.
Update memory once published.

### Runway Sizing for Fixed-Wing UAVs — Published

**File**: `_posts/2026-05-31-runway_sizing_for_fixed_wing_uavs.markdown`
**Topic**: Sizing runways for small and medium fixed-wing UAVs, worked outward from the master speed variable.
**Article Number**: A114
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-05-31 (28 references; 548 lines)

Standalone aerospace article.
Establishes the squared-speed master variable, where stall and liftoff speed are set by wing loading, air density, and the maximum lift coefficient, and works outward through explicit square-cube size-scaling;
the level ground roll;
paved versus dirt surfaces;
inclined and ski-jump runways;
wind, crosswind, and landing-gear ground handling;
orientation with an Earth-rotation dismissal;
density altitude;
obstacle clearance, margins, and an in-scope abort and stopping-margin note;
the landing roll and ground effect;
width and the lateral dimension (touchdown dispersion and guidance lateral error);
full-runway versus single-phase operation anchored to real UAVs (ScanEagle, RQ-7 Shadow, MQ-9 Reaper);
planform and airframe implications (conventional, delta, flying wing);
a worked numeric example;
and lighting, reflectors, and markings (optional versus required).
MathJax plug-and-chug formulae throughout.
No runnable code, so no Software Versions section.
References A112 (Prototyping Fixed-Wing Aircraft with Lightweight PLA and Fiberglass) via post_url.
28 references across Reference, Related Post, and Research categories.
548 lines.

### BTRON, Hypermedia, and the Real-Time Desktop — Published

**File**: `_posts/2026-05-23-btron_hypermedia_and_real_time_desktop.markdown`
**Topic**: Historical and analytical treatment of the BTRON proposition, the asymmetry between successful real-time operating systems and failed hypermedia desktops, a contemporary diagnosis of the market gap, and a concrete architectural sketch for a 2026 successor.
**Article Number**: A113
**Completion**: 100%
**Publication Sensibility**: High
**Status**: Published 2026-05-23 (149 references; 4,166 lines)

Standalone operating-systems history and philosophy article.
Surveys the BTRON proposition under the TRON Project (Sakamura, 1984),
why BTRON failed (Super 301 trade dispute listed in April 1989 and withdrawn the following month after USTR site visit, hardware program collapse, ecosystem shortfall, conceptual depth tax, vendor entrenchment),
the histories of relevant real-time operating systems (VRTX 1981, pSOS ~1982, VxWorks 1987, QNX 1980 in the Ottawa area of Canada, QNX Photon, Green Hills INTEGRITY, FreeRTOS, Zephyr, RTEMS, NuttX, μITRON, T-Kernel, seL4, Genode, Redox OS),
the histories of hypermedia systems (Memex, NLS in 1968 funded by ARPA/NASA/USAF, Project Xanadu, Smalltalk, NoteCards developed at Xerox PARC starting 1984 by Trigg/Halasz/Moran, HyperCard 1987-2004, OLE 2 in the 1992-1993 window, Cairo, OpenDoc framework 1994 and CyberDog 1996, Bonobo, KParts, Lotus/HCL Notes ~42M peak seats with ~140M cumulative licenses, SharePoint, World Wide Web with the Berners-Lee 1989 CERN proposal, Roam, Logseq, Obsidian, Notion, Coda, Jupyter, Observable, Solid, Beaker last released December 2020, Automerge, Yjs, ActivityPub),
the six structural commitments of the hypermedia object model,
where the model wins on merit and where it is clearly the wrong fit,
the real-time-plus-hypermedia special case,
who is served by the mass-market file-and-application model,
who would benefit from a real-time hypermedia desktop,
the web browser as substrate analysis,
a super-browser as modern realization,
why the gap persists (four-component diagnosis),
and viable entry strategies (vertical-first, internal-program, acquisition-path, sponsored-standards).
References A93 (Fast-Moving Versus Mission-Critical Engineering) and A86 (Mission Command Management Style) via post_url.
76 references across 4 categories (Book, Reference, Related Post, Research).
2,219 lines.

**Research Pass (2026-05-31)**:
Four parallel research agents verified factual claims across TRON Project history,
real-time operating systems history, hypermedia systems history,
and contemporary tools / regulated-industry incumbents / standards.
Corrections applied:
ITRON deployment softened from "several billion per year" to "cumulative billions";
Super 301 chronology refined (listed April 1989, withdrawn May 1989);
Real Object / Virtual Object pairing introduced for BTRON's hypermedia model;
TRON character code Unicode comparison added with concrete dates (Cho Kanji 1999 ~180K characters vs Unicode 4.1 in 2005);
RTOS first-generation date range corrected from "1970s-early 1980s" to "early 1980s";
QNX origin location corrected from "Ottawa" to "Ottawa area of Canada" with University of Waterloo founder attribution;
QNX Photon deprecation since 2014 disclosed;
QNX vehicle deployment updated to "more than 275 million" with BlackBerry press release citation;
FreeRTOS "most widely deployed" softened to "among the most widely deployed";
FreeRTOS AWS 2017 transaction reframed as stewardship transfer with AWS blog citation;
seL4 superlative softened to "most extensive functional-correctness proof of a general-purpose OS kernel";
Redox OS alpha status disclosed;
NLS funding expanded to ARPA/NASA/USAF;
NoteCards authorship attributed (Trigg, Halasz, Moran);
HyperCard "several million users" softened to "millions";
OLE 2 release window clarified (1992-1993);
OpenDoc shipping clarified (framework 1994, CyberDog 1996);
Lotus Notes seat counts corrected from "hundreds of millions" to ~42M active / ~140M cumulative;
SharePoint primitives clarified (files and lists);
Beaker reframed from "dormant" to "discontinued after December 2020";
ARP4754B successor noted.
URL fixes:
ref_cho_kanji (Wikipedia 404, replaced with chokanji.com);
ref_super_301 (replaced with Section 301 stable URL);
ref_vrtx (replaced with Versatile_Real-Time_Executive);
ref_qnx_neutrino (replaced with qnx.software);
ref_qnx_photon (replaced with QNX_Photon Wikipedia entry).
New references added with inline citations:
ARP4754A; TRON character encoding;
IEEE Milestone for TRON RTOS family;
USTR 25 May 1989 statement;
Mars Pathfinder priority inversion engineering note;
BlackBerry QNX 275M vehicles press release;
Amazon FreeRTOS launch blog post;
seL4 SOSP 2009 paper;
Engelbart and English 1968 AFIPS paper;
Halasz 1988 NoteCards retrospective in CACM;
Berners-Lee 1989 CERN proposal;
Kleppmann and colleagues local-first essay (Onward 2019).
URL verification:
all new URLs return HTTP 200 except ACM Digital Library and chokanji.com which return 403 to curl due to bot detection but are valid human-accessible URLs.

**Expansion Pass (2026-05-31)**:
Four additional parallel research agents covered alternative research operating systems (Plan 9, Inferno, Self, Oberon, JX),
the artificial intelligence and large language model angle (retrieval-augmented generation, Model Context Protocol, structured output, Coalition for Content Provenance and Authenticity, agent provenance research),
architectural building blocks for a 2026 hypermedia operating system (Automerge, Yjs, Loro, InterPlanetary File System, Iroh, Hypercore, seL4, Genode, Capsicum, Cap'n Proto, WebAssembly Component Model, Servo, Chromium Embedded Framework, WebKit, ProseMirror, TipTap, Lexical, JetBrains Meta Programming System, CodeMirror, Skia, Cairo Graphics, HarfBuzz, FreeType),
and regulated-industry incumbents (DOORS, Polarion, Windchill, ENOVIA, Vault, Gotham, Foundry, Relativity, iManage).
Seven new sections added:
"Other Radical Unifications" (Plan 9, Inferno, Self/Morphic, Oberon, JX as alternative unification approaches);
"Performance and Latency Engineering for Composed Documents" (bounded handler execution time, deadline propagation, preallocated resources, spatial and temporal isolation, admission control);
"The Artificial Intelligence Synergy" (RAG, MCP, structured output, C2PA, regulatory provenance requirements, PROV-AGENT, HyperAgents workshop);
"How the Incumbents Compare" (comparison table across the nine incumbents on typed parts, typed links, in-place composition, provenance, and local-first persistence);
"Coexistence with the File and Application World" (file system bridges, import handlers, lossy export, gradual adoption);
"A Concrete Architectural Sketch" (ten layers from verified microkernel through user-facing shell, naming production-quality open-source components for each);
"Out of Scope" (explicit declaration of seven topics deferred to follow-up articles).
56 new authoritative sources added with inline citations.
Reference count rose from 76 to 132 across Book (2), Reference (108), Related Post (2), and Research (20) categories.
Line count rose from 2,219 to 3,408.

**Completion Pass (2026-05-31)**:
Three additional parallel research agents covered Lifestreams (Gelernter and Freeman, Yale, mid-1990s),
Sutherland's Sketchpad (1963) and Alan Kay's Dynabook (1968-1972),
and the contemporary Tools for Thought movement (Matuschak, Nielsen, Appleton, Bret Victor, Rheingold, Future of Coding, Hyperlink Academy).
Seven new sections and inline additions added:
Sketchpad paragraph in hypermedia history;
Dynabook paragraph in hypermedia history;
Lifestreams paragraph in hypermedia history;
Tools for Thought paragraph in hypermedia history (with cultural framing);
"A Day in the Workflow, an Aerospace Requirements Example" between Architectural Sketch and Conclusion;
"Epistemic State of the Argument" between Workflow and Conclusion (distinguishing factual, structural, and strategic claims);
"Reader's Next Steps" after Out of Scope (TRON Forum, seL4 community, Genode community, local-first community, Solid working group, HyperAgents workshop, Tools for Thought community);
"Glossary" after Reader's Next Steps (defined-terms section for 12 key concepts including capability-based security, compound document, conflict-free replicated data type, content-addressable storage, handler, hypermedia object model, link store, microkernel, provenance, real-time operating system, separation kernel, transclusion, typed link, typed part).
17 new authoritative sources added with inline citations:
Mirror Worlds (Gelernter 1991 Oxford);
Tools for Thought (Rheingold 1985 MIT Press);
Lifestreams CHI 1996 paper;
Lifestreams SIGMOD 1996 paper;
Lifestreams Yale project page;
Sutherland's Sketchpad Cambridge-hosted thesis;
Sketchpad Wikipedia;
Kay and Goldberg Personal Dynamic Media 1977;
Dynabook Wikipedia;
Matuschak and Nielsen 2019 ttft essay;
Matuschak personal site;
Evergreen Notes;
Maggie Appleton personal site;
Appleton Garden History essay;
Bret Victor Magic Ink essay;
Future of Coding;
Hyperlink Academy.
Reference count rose from 132 to 149.
Line count rose from 3,408 to 4,166.
All anchors verified used and defined; style scan clean.
URL verification: all HTTP 200 except documented OUP 202 (project memory) and ACM DL 403 (bot detection, valid for human readers).

**Remaining Work**:
Human review of the four completion-pass additions (Lifestreams, Sketchpad/Dynabook, Tools for Thought, user journey walkthrough, epistemic state, next steps, glossary).
Confirm publication date and assign final timestamp.
Update Software Versions section if any is desired (currently omitted to match A98-class analytical-article convention).
Update memory once published.

### Solana sBPF Assembly Example — Pre-Release Candidate

**File**: `solana_sbpf_assembly_example.markdown`
**Topic**: Writing Solana programs using sBPF assembly with the sbpf standalone toolchain
**Completion**: ~90%
**Publication Sensibility**: High
**Status**: Pre-Release Candidate

Completely rewritten from a partial draft with x86 assembly and clang build.rs
to use the correct sBPF instruction set and the sbpf standalone toolchain.
Covers the sBPF virtual machine, registers and memory layout, instruction set overview,
toolchain installation, project creation, a Hello World program using `.rodata` section,
`lddw` address loading, and `.equ` named constants for all non-trivial literals.
Building and deploying with sbpf tool,
and the current state of mixed Rust and assembly projects.
Three experimental paths for mixed projects documented (nightly inline asm, sbpf-linker, build.rs).
Includes a theoretical linked Rust and assembly example
using the Solana SDK's Clang and llvm-ar in a `build.rs` script.
The Rust entrypoint passes a string to an sBPF assembly logging subroutine via C FFI.
Both assembly files use `.equ` named constants with inline comments.
Nine limitations documented.
Eleven references across two categories (Reference, Research).
No article number assigned. Not slotted for publication.

**Remaining Work**:
Human verification by building and deploying the Hello World program with the sbpf tool.
Verify the linked Rust and assembly example compiles with cargo build-sbf.
Fill in Software Versions TODO placeholders.
Verify assembly code executes correctly on a local test validator.
Assign article number and publication date when ready.

### Android Development on FreeBSD — Pre-Release Candidate

**File**: `android_development_on_freebsd.markdown`
**Topic**: Android SDK and NDK development on FreeBSD using Kotlin, Rust, and the Linuxulator
**Completion**: ~90%
**Publication Sensibility**: Medium
**Status**: Pre-Release Candidate

Completely rewritten from 2017 content (FreeBSD 11, SDK 25, NDK r13b)
to modern toolchain (FreeBSD 14, SDK 35, NDK r28).
Covers Linuxulator setup with Rocky Linux 9 base,
Android SDK and NDK installation via sdkmanager,
ADB setup with native FreeBSD port,
Kotlin SDK development with standard XML layouts,
Rust NDK development with JNI integration via cargo-ndk,
and emulator feasibility discussion.
Sample app is a native Android port of the CLMM calculator (A91)
with Kotlin UI and Rust math exposed through JNI.
No article number assigned. Not slotted for publication.
Ten references across four categories (Android, FreeBSD, Related Post, Rust).

**Remaining Work**:
Human verification on FreeBSD hardware.
Fill in Software Versions TODO placeholders.
Test build pipeline on FreeBSD 14 with Linuxulator.
Assign article number and publication date when ready.

### Android Unit Testing — Pre-Release Candidate

**File**: `android_unit_testing.markdown`
**Topic**: Android unit testing across Kotlin, Robolectric, instrumented, and NDK layers
**Completion**: ~90%
**Publication Sensibility**: High
**Status**: Pre-Release Candidate

Completely rewritten from 2017 content (SDK 25, Java 1.8, ApplicationTestCase)
to modern toolchain (SDK 35, JDK 17, Kotlin 2.1.0, AGP 8.9.0).
Test subject is the CLMM calculator app with both Kotlin and Rust native implementations.
Covers test dependencies (JUnit 4, AndroidX Test, Robolectric, MockK, Espresso),
local unit tests with pure logic and Robolectric Activity tests,
mocking with MockK object declarations,
instrumented tests with Espresso,
and NDK unit testing with Rust cargo test, JNI boundary testing, and GoogleTest for C++.
Running Tests section provides Gradle task table. Code Coverage section covers JaCoCo, Kover, and cargo-llvm-cov.
Seven limitations documented. MathJax enabled for CLMM reserve formulas.
References Android FreeBSD article and CLMM Mathematics (A91) via post_url.
No article number assigned. Not slotted for publication.
Twelve references across four categories (Android, Reference, Related Post, Rust).

**Remaining Work**:
Human verification of test code against actual Android project.
Fill in Software Versions TODO placeholders.
Verify floating-point test expected values against CLMM calculator.
Verify JNI function name conventions for NativeBridgeTest.
Assign article number and publication date when ready.
Android FreeBSD article and CLMM Mathematics (A91) must be published first.

### Authenticating a Phoenix JSON API with Guardian and Ueberauth — Pre-Release Candidate

**File**: `phoenix_json_api_authentication_with_guardian.markdown`
**Topic**: Phoenix/Elixir JSON API authentication with Guardian JWT and Ueberauth identity strategy
**Completion**: ~90%
**Publication Sensibility**: High
**Status**: Pre-Release Candidate

Completely rewritten from 2016 content (Phoenix 1.1.4, Elixir 1.2.3, Guardian ~0.10.0, Comeonin ~2.1)
to modern toolchain (Phoenix 1.7+, Guardian ~> 2.3, bcrypt_elixir ~> 3.0, Ueberauth ~> 0.10).
MemoApi example application with user registration, JWT-based login, and protected memo CRUD.
Uses context modules, Guardian implementation module pattern, plug pipeline, and error handler.
Ueberauth identity strategy integration with callback pattern example.
Testing the API section with curl commands and expected JSON responses.
Seven limitations documented.
References published article A27 "A Shell Script for Working with Phoenix JSON APIs" via post_url.
No article number assigned. Not slotted for publication.
Eleven references across four categories (Elixir, Phoenix, Reference, Related Post).

**Remaining Work**:
Human verification by building and running the MemoApi project.
Fill in Software Versions TODO placeholders.
Verify Guardian secret key generation command.
Verify Ueberauth identity strategy plug compatibility.
Assign article number and publication date when ready.

### Getting Started with Claude Code on FreeBSD — Pre-Release Candidate

**File**: `claude_code_getting_started_on_freebsd.markdown`
**Topic**: Installing and configuring Claude Code on FreeBSD
**Completion**: ~90%
**Publication Sensibility**: High
**Status**: Pre-Release Candidate

New article covering Claude Code installation on FreeBSD via the misc/claude-code port, binary packages, and npm.
Documents shebang fix, ripgrep configuration, and a Hello World exercise
that generates a curses-based system dashboard using only FreeBSD base system tools.
Limitations section documents unsupported platform status and known issues.
References the companion Getting Started with Claude Code post (A74) via post_url.
Twelve references across four categories (Claude, FreeBSD, GitHub, Related Post).
No article number assigned. Not slotted for publication.

**Remaining Work**:
Human verification on FreeBSD hardware.
Fill in Software Versions output.
Test the Hello World prompt on FreeBSD.
Verify shebang fix and ripgrep configuration.
Assign article number and publication date when ready.

### Getting Started with Claude Code Over SSH — Pre-Release Candidate

**File**: `claude_code_getting_started_over_ssh.markdown`
**Topic**: Using Claude Code locally to work on remote machines over SSH
**Completion**: ~90%
**Publication Sensibility**: High
**Status**: Pre-Release Candidate

New article covering the use of Claude Code on a local workstation
to execute commands on remote machines via SSH.
Introduces SSH fundamentals for readers unfamiliar with the protocol.
Walks through Ed25519 key generation, public key copying, SSH agent setup,
host configuration, and verification.
Documents remote execution patterns using Claude Code's Bash tool
including single commands, multi-command chains, and scp file transfer.
Covers timeout configuration for long-running remote operations.
Detailed agent forwarding section covers mechanism, configuration,
verification, Claude Code usage, security considerations,
and ProxyJump as a safer alternative for untrusted intermediate hosts.
Briefly discusses Claude Code Desktop SSH as an alternative
that requires Claude Code on the remote machine.
Hello World section demonstrates end-to-end remote workflow
with OS detection, C code generation, scp transfer, and remote compilation.
References companion Getting Started posts for macOS (A74), FreeBSD, and OpenBSD via post_url.
Eleven references across three categories (Claude, Reference, Related Post).
No article number assigned. Not slotted for publication.

**Remaining Work**:
Human verification with an actual remote SSH target.
Fill in Software Versions output.
Test the Hello World prompt against a remote machine.
Verify agent forwarding with `ssh -A myserver "ssh-add -l"`.
Verify timeout configuration format.
Assign article number and publication date when ready.

### Getting Started with Claude Code on OpenBSD — Pre-Release Candidate

**File**: `claude_code_getting_started_on_openbsd.markdown`
**Topic**: Installing and configuring Claude Code on OpenBSD
**Completion**: ~90%
**Publication Sensibility**: High
**Status**: Pre-Release Candidate

New article covering Claude Code installation on OpenBSD via npm,
the only viable installation path on the platform.
No port or package exists for Claude Code on OpenBSD.
Documents bash installation and `/bin/bash` symlink requirement,
ripgrep configuration via `USE_BUILTIN_RIPGREP` setting,
and a critical warning against running the native installer or `claude install`
which downloads an incompatible Linux binary and breaks npm installations.
Hello World exercise generates a curses-based system dashboard using only OpenBSD base system tools.
Limitations section is more extensive than the FreeBSD article
due to the absence of a dedicated port and the removal of the Linux compatibility layer.
References the companion Getting Started with Claude Code post (A74)
and the FreeBSD article via post_url.
Twelve references across four categories (Claude, GitHub, OpenBSD, Related Post).
No article number assigned. Not slotted for publication.

**Remaining Work**:
Human verification on OpenBSD hardware.
Fill in Software Versions output.
Test the Hello World prompt on OpenBSD.
Verify bash symlink and ripgrep configuration.
Verify that `doas pkg_add node` installs a supported Node.js version (18-24).
Assign article number and publication date when ready.

### Getting Started with Solana Using Rust and Pinocchio — Pre-Release Candidate

**File**: `solana_with_rust_and_pinocchio_getting_started.markdown`
**Topic**: Building a Solana program with Pinocchio zero-dependency library, mirroring the Anchor companion article (A65)
**Completion**: ~90%
**Publication Sensibility**: High
**Status**: Pre-Release Candidate

New article mirroring A65 "Getting Started with Solana Using Rust and Anchor"
but using the Pinocchio zero-dependency library instead of Anchor.
Same key pegboard toy contract that stores a public key and encrypted private key on-chain.
Covers Pinocchio project setup, manual account validation, raw byte parsing,
PDA creation via CPI to System Program, Mollusk test harness,
building with cargo build-sbf, and deployment to local test validator.
Comparison table with Anchor implementation (A65).
Nine limitations documented.
References published article A65 via post_url.
No article number assigned. Not slotted for publication.
Twelve references across three categories (Reference, Related Post, Research).

**Remaining Work**:
Human verification by building and deploying the program with cargo build-sbf.
Fill in Software Versions TODO placeholders.
Run Mollusk tests against compiled BPF binary.
Verify Pinocchio crate versions are current.
Assign article number and publication date when ready.

### Template

**File**: `template.markdown`
**Topic**: Post template for new articles
**Completion**: N/A
**Publication Sensibility**: N/A

This is a template file, not a draft. It provides the standard structure for new posts.

## Summary

Ten files exist in `_drafts/`. One is a template.
No release candidates remain.
No new drafts remain.
No stubs remain.
A79 through A144 have been published.

**Tier 1: Publishable with moderate effort.**
No drafts remain in Tier 1.
A126 (communications and the command-and-control data link), A127 (structures and the flight envelope), A128 (aerobatics as costed trajectories, the synthesis capstone of the extension set), A129 (an aerobatic maneuver reference catalog, the reference companion to A128), A130 (payload and mission systems), and A131 (the regulatory and operations layer) are the six extensions beyond the core fixed-wing-UAV arc; the series and its extensions are now complete, with no further extensions flagged.
A132 through A144 are the SBIR/STTR practitioner playbook, a complete thirteen-article series in the new business/funding/sbir category covering the United States SBIR and STTR programs from orientation, agency survey, eligibility and registration, finding a topic and reading a solicitation, the Phase I proposal, Phase II and the commercialization plan, Phase III and the valley of death, data rights and intellectual property, the money, after the award, strategy, and international analogs through a worked-campaign capstone that reuses the fixed-wing UAV; the series is now complete, all thirteen of thirteen articles published.

The drafts fall into four tiers when assessed for salvageability with contemporary tooling.

**Pre-Release Candidates.**
Android Development on FreeBSD has been fully rewritten with modern tooling
and is awaiting verification on FreeBSD hardware before publication.
Android Unit Testing has been fully rewritten with contemporary AndroidX Test, Robolectric, MockK,
and NDK testing coverage and is awaiting verification against an actual Android project.
Getting Started with Claude Code on FreeBSD covers installation via ports, packages, and npm
and is awaiting verification on FreeBSD hardware before publication.
Getting Started with Claude Code on OpenBSD covers npm-only installation with bash and ripgrep configuration
and is awaiting verification on OpenBSD hardware before publication.
Getting Started with Claude Code Over SSH covers using Claude Code locally to work on remote machines via SSH
and is awaiting verification with a remote SSH target.
Authenticating a Phoenix JSON API with Guardian and Ueberauth has been fully rewritten
from 2016 Phoenix 1.1/Guardian 0.10 to modern Phoenix 1.7+/Guardian 2.x
and is awaiting verification by building and running the MemoApi project.
Solana sBPF Assembly Example has been fully rewritten from a partial draft with x86 assembly
to use the correct sBPF ISA and the sbpf standalone toolchain,
revised with `.rodata` section usage and a theoretical linked Rust and assembly example,
and is awaiting verification by building and deploying with the sbpf tool.
Getting Started with Solana Using Rust and Pinocchio mirrors the Anchor companion article (A65)
using the Pinocchio zero-dependency library
and is awaiting verification by building and running Mollusk tests.

**No stubs remain.**
All article-numbered drafts have been elevated to release candidate status.

## Candidate Future Post Topics

The following table lists on-brand post ideas organized by thematic cluster.
Topics are selected to align with the blog's established strengths in systems programming, applied mathematics, unconventional toolchains, and AI-assisted development.

| Topic | Categories | Rationale | Builds On |
|-------|------------|-----------|-----------|
| Formal Verification with TLA+ | math development | Formal methods for distributed protocol design. Bridges the mathematical rigor thread with systems engineering. | Writing Proofs (A79), Radioactive Half-Life Demurrage Cryptocurrency Coin (A88) |
| Lean 4 and Automated Theorem Proving | math ai development | Interactive theorem prover with growing LLM integration. Connects proofs, AI, and software verification. | Writing Proofs (A79) |
| Property-Based Testing in Rust | rust development | QuickCheck-style testing as lightweight formal methods. Practical bridge between proofs and everyday engineering. | no_std Rust series, AMM Mathematics (A67) |
| RISC-V Assembly Getting Started | asm embedded development | Emerging instruction set architecture for embedded and open hardware. Natural extension of ARM and x86 assembly posts. | ASM Playdate Development, UNIX ARM Assembler |
| Rust on RISC-V Microcontrollers | rust embedded no_std | no_std Rust on RISC-V hardware. Combines two active threads in the blog. | no_std Rust series, Radioactive Half-Life Demurrage Cryptocurrency Coin (A88) |
| WebAssembly Component Model | rust wasm development | WASI and the component model as the next step beyond basic WASM. | WASM on Jekyll (A73) |
| ~~CLMM Mathematics and Calculator~~ | ~~crypto defi math~~ | ~~Concentrated liquidity mathematics with interactive widget. Direct sequel to AMM article.~~ | ~~Covered by Concentrated Liquidity Market Maker Mathematics (A91)~~ |
| ~~Solana sBPF Assembly~~ | ~~crypto development asm~~ | ~~Writing Solana programs at the assembly level. Unique low-level blockchain content.~~ | ~~Covered by Solana sBPF Assembly Example draft~~ |
| Statistics for A/B Testing | math development | Applied statistics for software engineers. Practical extension of the statistics reference. | Probability and Statistics Reference (A80) |
| ~~Orbital Mechanics Primer~~ | ~~math science~~ | ~~Applied physics with MathJax. Evergreen STEM content.~~ | ~~Covered by Introduction to Space Studies (A90)~~ |
| Context Engineering Patterns Cookbook | ai ai-tools development | Practical patterns distilled from the survey article. Shorter, actionable format. | Context Engineering (A78), A75-A77 series |
| Evaluating AI-Generated Code | ai development | Metrics and methods for assessing agent output quality. Addresses the evaluation gap identified in A78. | A75-A78 series |
| FreeBSD Jails for Development Environments | freebsd development | Container-like isolation using FreeBSD jails. Updates the FreeBSD systems thread with modern practices. | FreeBSD series (A1-A40 era) |
| Shell Scripting with Modern CLI Tools | sh unix development | fd, ripgrep, jq, fzf as modern replacements for traditional UNIX tools. | Shell scripting series |
| Game AI with Minimax and Alpha-Beta Pruning | gamedev math ai | Classical game AI algorithms with proofs of optimality. Bridges game development and mathematical rigor. | Chess/Go game theory series |
| Playdate Game Physics | gamedev playdate math c | Physics simulation on constrained hardware. Applied mathematics on embedded game platform. | Playdate series, Trigonometry (A14) |
| Observable Signatures of Competitive Civilizations | science philosophy | Unselected A101 candidate. What observational evidence would distinguish competitive expansion from natural astrophysical processes. Connects Dyson sphere searches and SETI to the competitive framework. | A98, A99, A100, A101 |
| The Survival Bottleneck Engineering Roadmap | science philosophy | Unselected A101 candidate. Detailed engineering requirements for the Type 0 to Type I transition. Covered adequately in A100 but could be expanded with specific technology roadmaps and quantitative risk reduction strategies. | A100 |
| Self-Replicating Technology Engineering | science philosophy | Unselected A101 candidate. Detailed engineering analysis of self-replicating machines and spacecraft. Von Neumann universal constructor, error correction, gray goo risk quantification. Implementation-focused rather than strategic. | A100, A101 |
| Governance Coherence Deep Dive | science philosophy | Unselected A101 candidate. Full treatment of governance coherence half-life, myth-structure transition, and institutional degradation at cosmic scales. A92 already covers this but the competitive context from A98-A101 would add depth. | A87, A89, A92, A100 |
| Economics of Competitive Expansion | science philosophy | Unselected A101 candidate. Resource allocation, opportunity costs, and economic optimization under competitive expansion imperatives. Interesting but secondary to physical feasibility questions. | A98, A100 |
| First Contact Protocols Under Competitive Assumptions | science philosophy | Unselected A101 candidate. Decision-theoretic analysis of first contact under the competitive framework. Premature without knowing whether force projection is physically feasible, which A101 now addresses. | A98, A99, A101 |
