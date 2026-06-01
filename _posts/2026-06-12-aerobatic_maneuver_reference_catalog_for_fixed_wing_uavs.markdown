---
layout: post
mathjax: true
comments: true
title:  "An Aerobatic Maneuver Reference Catalog for Fixed-Wing UAVs"
date:   2026-06-12 09:00:00 +0000
categories: aerospace engineering uav
---

<!-- A129 -->
<script>console.log("A129");</script>

The previous article built a model that prices an aerobatic maneuver as a
costed trajectory, a path through the energy state carrying an energetic, a
structural, and a thermal cost.
This article is the reference companion to that model, a catalog of the named
and recognized maneuvers with each one classified in the terms the model
defines.
It is written for the people who command unmanned aircraft and the autonomy
that flies them, so a maneuver here is a commanded trajectory to be selected
and budgeted rather than a skill to be learned, and the human-pilot concerns of
technique and physiology are left out as they were in the model article.
The maneuver definitions are drawn from the established catalogs, the
[Aresti system][ref_aresti] codified for competition and the figures recognized
by the [International Aerobatic Club][ref_iac] and the
[world air sports federation][ref_fai], with the basic fighter maneuvers drawn
from the standard [air-combat repertoire][ref_bfm].
The per-maneuver classification in the cost model is, to my knowledge, an
original effort, since no catalog records the energy-height behavior, the load
class, and the regime ceiling of each figure, so that part of the table should
be read as a derived and qualitative synthesis rather than a sourced
measurement, with the limitations stated below.

## How to Read the Table

Each row is one maneuver, sorted alphabetically, and carries a stable
identifier whose letter prefix names its family so the identifier survives the
insertion of new rows.
The families are the lines (LN), the turns (TN), the rolls (RL), the loops and
eights (LP), the partial loops and combinations (PL), the stall turns (ST), the
tailslides (TS), the spins (SP), the post-stall and supermaneuvers (PS), the
three-dimensional and prop-hang figures (TD), the basic fighter maneuvers (BF),
and the composite or display figures (CX).
The path column gives the spatiotemporal character of the figure, the shape it
traces and therefore the volume of airspace it sweeps.
The energy-height column gives the behavior of the energy state in the terms of
the model article, whether the figure conserves the energy height, trades
kinetic for potential energy or the reverse, oscillates it, spends it against
drag, or dumps it.
The peak-load column gives the order of the largest load factor and its sign,
as a qualitative class rather than a measured value.
The last column gives the highest speed regime in which the figure remains
meaningful, together with any flag for a figure that is post-stall, autorotative,
asymmetric, parametric, or without a closed form.

## Why the Thermal Cost Is Folded Into the Regime Column

The model article carried three costs, but a separate thermal column would be
nearly useless in this catalog, because the entire sport and competition
repertoire is flown at subsonic speed where the aerodynamic heating is
negligible.
The thermal cost is therefore folded into the regime ceiling, which already
encodes it, since a figure that survives only to subsonic speed has by
definition no thermal cost worth recording, while the few figures that reach
the transonic and supersonic regimes are exactly the ones where heat begins to
matter.
A reader who needs the thermal cost reads it from the regime ceiling, low when
the ceiling is subsonic and rising only for the figures that climb toward the
thermal wall of the boosted-propulsion article.

## Provenance and Limitations

The honesty of this catalog rests on a clear division.
The existence and the definition of each maneuver are sourced, taken from the
established catalogs cited above, and where a figure has its own published
description it is linked in the table.
The classification of each maneuver in the cost model, the energy-height
behavior, the peak-load class, and the regime ceiling, is my own derivation
from the model of the previous article, and to my knowledge has not been
tabulated this way before, so it is offered as an original and qualitative
synthesis to be checked rather than as measured data.
Three limitations follow.
The values are qualitative classes and orders of magnitude, design guidance
rather than certification figures, and the true numbers depend on the specific
airframe and how aggressively the figure is flown.
The catalog lists the named and recognized base figures and notes the
parametric families separately, rather than enumerating the combinatorial
Aresti space of figures distinguished only by the number of rolls or spins,
which runs to many thousands of mechanical permutations of no reference value.
And the post-stall and unsteady figures have no closed-form pricing, so their
rows carry a flag and are discussed in a dedicated section rather than given a
load number the physics does not support.

## The Catalog

| ID | Maneuver | Family | Path | Energy height | Peak load | Regime and flags |
|---|---|---|---|---|---|---|
| RL-01 | [Aileron roll][ref_aileron_roll] | Roll, Aresti 9 | Helical roll about the path | Conserved | Low, near 1g | Subsonic to transonic |
| LP-01 | Avalanche | Loop, Aresti 7 | Inside loop with a snap roll at the apex | Traded, dumped at the apex | High then unsteady | Subsonic, no closed form at the snap |
| RL-02 | [Barrel roll][ref_barrel_roll] | Roll, Aresti 9 | Helix around a line, roll and loop combined | Nearly conserved | Low to moderate, 2 to 3g | Transonic |
| BF-01 | Barrel-roll attack | Fighter | Displacement roll to bleed closure on an overshoot | Spent | Moderate | Subsonic, energy fight |
| BF-02 | Break turn | Fighter | Maximum-rate level turn toward the threat | Spent hard, excess power negative | High, to the corner | Subsonic, energy fight |
| TN-01 | [Chandelle][ref_chandelle] | Turn, training | Climbing 180-degree turn for maximum height | Speed traded for height, net gain | Low to moderate | Subsonic |
| LP-02 | Cloverleaf | Loop, Aresti 7 | Four linked loops each turning ninety degrees | Oscillated | High | Subsonic |
| PS-01 | [Cobra][ref_cobra] | Post-stall | Snap to very high angle of attack and back, little path change | Speed dumped | Unsteady, high transient | Subsonic, post-stall, needs post-stall authority, no closed form |
| SP-01 | Crossover spin | Spin, Aresti 9 | Autorotation that reverses sense | Dumped | Unsteady | Subsonic, post-stall, autorotative, no closed form |
| LP-03 | [Cuban eight][ref_cuban_eight] | Loop, Aresti 7 | Horizontal eight of five-eighths loops joined by half rolls | Oscillated | High | Subsonic |
| BF-03 | Defensive spiral | Fighter | Descending maximum-rate turn | Height traded for turn, spent | High | Subsonic, energy fight |
| RL-03 | Derry turn | Roll and turn, display | Turn entered by rolling under rather than over | Nearly conserved | Low to moderate | Subsonic |
| RL-04 | Eight-point roll | Roll, Aresti 9 | Hesitation roll stopping at eight points | Conserved | Near 1g, mixed sign | Subsonic, parametric in points, high control rate |
| TD-01 | [Elevator][ref_three_d_flying] | Three-dimensional, post-stall | Sustained flat deep-stall descent at very high angle of attack | Spent and slowly dumped | Low, unsteady | Subsonic, post-stall, needs thrust and surface authority, no closed form |
| PS-02 | [Falling leaf][ref_falling_leaf] | Post-stall | Rocking series of incipient stalls | Slowly dumped | Low, unsteady | Subsonic, post-stall, no closed form |
| SP-02 | Flat spin | Spin, Aresti 9 | Flat high-rate autorotation | Dumped | Unsteady | Subsonic, post-stall, may not recover, no closed form |
| LN-01 | Forty-five-degree down line | Line, Aresti 1 | Straight descent at forty-five degrees | Traded to speed | Near 1g | Subsonic, base figure |
| LN-02 | Forty-five-degree up line | Line, Aresti 1 | Straight climb at forty-five degrees | Speed traded for height | Near 1g | Subsonic, base figure |
| RL-05 | Four-point roll | Roll, Aresti 9 | Hesitation roll stopping at four points | Conserved | Near 1g, mixed | Subsonic, parametric in points |
| PL-01 | Goldfish | Combination, Aresti 8 | Forty-five down, partial loop, forty-five up | Traded | High | Subsonic |
| BF-04 | Guns jink | Fighter | Random out-of-plane jinking to spoil tracking | Spent | Moderate to high | Subsonic, energy fight |
| PL-02 | Half Cuban eight | Partial loop, Aresti 7 and 8 | Five-eighths loop then a half roll on the down line | Traded up then down | High | Subsonic |
| PL-03 | Half loop, pull | Partial loop, Aresti 7 | Inside half loop to inverted | Speed traded for height | High | Transonic |
| PL-04 | Half loop, push | Partial loop, Aresti 7 | Outside half loop | Speed traded for height, negative | High negative | Subsonic, negative g |
| RL-06 | Half roll | Roll, Aresti 9 | One-hundred-eighty-degree roll | Conserved | Near 1g | Subsonic |
| ST-01 | [Hammerhead][ref_hammerhead] | Stall turn, Aresti 5 | Vertical climb to near-zero speed, yaw pivot, vertical descent | Spent then regained | Low at the pivot | Subsonic, gyroscopic at the pivot |
| TD-02 | [Harrier][ref_three_d_flying] | Three-dimensional, post-stall | Controlled high-alpha mushing flight along a line | Spent, high drag | Low, unsteady | Subsonic, post-stall, needs thrust and authority, no closed form |
| PS-03 | [Herbst maneuver][ref_herbst] | Post-stall | Post-stall heading reversal at low speed | Dumped and redirected | Unsteady | Subsonic, post-stall, needs thrust vectoring, no closed form |
| RL-07 | Hesitation roll | Roll, Aresti 9 | Roll with stops at set points | Conserved | Near 1g, mixed | Subsonic, parametric in points |
| BF-05 | High yo-yo | Fighter | Out-of-plane climb to reduce closure and keep energy | Speed traded for height | Moderate | Subsonic to transonic, energy fight |
| LP-04 | Horizontal eight | Loop, Aresti 7 | Two loops forming a lying eight | Oscillated | High | Subsonic |
| TD-03 | Hover, prop-hang | Three-dimensional, post-stall | Nose-vertical stationary hang on the propeller | Spent to near zero | Near 0g, thrust carries the weight | Subsonic, post-stall, needs thrust-to-weight above one, no closed form |
| PL-05 | Humpty bump, pull | Combination, Aresti 8 | Vertical up, inside half loop over the top, vertical down | Traded | High | Subsonic |
| PL-06 | Humpty bump, push | Combination, Aresti 8 | Vertical up, outside half loop, vertical down | Traded, negative over the top | High negative | Subsonic, negative g |
| PL-07 | [Immelmann turn][ref_immelmann] | Partial loop, Aresti 7 and 8 | Half loop up then half roll to upright, heading reversed with height gained | Speed traded for height and a reversal | High | Transonic |
| LP-05 | Inside loop | Loop, Aresti 7 | Positive-g vertical circle | Traded up then down | High at the bottom | Transonic at best |
| SP-03 | Inverted flat spin | Spin, Aresti 9 | Flat autorotation from an inverted stall | Dumped | Unsteady, negative | Subsonic, post-stall, no closed form |
| LN-03 | Inverted level flight | Line, Aresti 1 | Sustained negative-g level line | Conserved | Negative, near minus 1g | Subsonic |
| SP-04 | Inverted spin | Spin, Aresti 9 | Autorotation from a negative-g stall | Dumped | Unsteady, negative | Subsonic, post-stall, autorotative, no closed form |
| LN-04 | Knife-edge flight | Line, Aresti 1 | Ninety-degree bank carried on fuselage lift and rudder | Spent, high drag | Low lateral | Subsonic, needs rudder authority |
| LP-06 | Knife-edge loop | Loop, Aresti 7 | Loop flown in the knife-edge attitude | Spent, high drag | Moderate | Subsonic, needs rudder authority |
| PS-04 | [Kulbit][ref_kulbit] | Post-stall | Extremely tight post-stall somersault about the pitch axis | Dumped | Unsteady | Subsonic, post-stall, needs thrust vectoring, no closed form |
| BF-06 | Lag displacement roll | Fighter | Roll to lag pursuit and manage closure | Nearly conserved | Moderate | Subsonic, energy fight |
| TN-02 | Lazy eight | Turn, training | Opposing climbing and descending turns with continuously varying bank | Gently oscillated | Low to moderate | Subsonic |
| CX-01 | [Lomcevak][ref_lomcevak] | Composite, gyroscopic | End-over-end gyroscopic tumble | Dumped | Unsteady, gyroscopic | Subsonic, post-stall, no closed form |
| BF-07 | Low yo-yo | Fighter | Dive to cut a corner and gain closure | Height traded for speed | Moderate to high | Subsonic, energy fight |
| LP-07 | Octagonal loop | Loop, Aresti 7 | Eight-sided loop of lines and partial loops | Oscillated | High at the corners | Subsonic |
| LP-08 | Outside loop | Loop, Aresti 7 | Negative-g vertical circle flown over the top | Traded, negative throughout | High negative | Subsonic, structurally costly |
| RL-08 | Outside snap roll | Roll, Aresti 9 | Negative-g autorotative snap roll | Dumped | Unsteady, negative | Subsonic, post-stall, no closed form |
| BF-08 | Pitchback | Fighter | Climbing high-g turn reversal | Speed traded for height, spent | High | Subsonic, energy fight |
| RL-09 | Point roll | Roll, Aresti 9 | Hesitation roll stopping at evenly spaced points | Conserved | Near 1g, mixed | Subsonic, parametric in points |
| LP-09 | Reverse Cuban eight | Loop, Aresti 7 | Cuban eight flown with forty-five-degree up lines | Oscillated, mixed sign | High | Subsonic |
| RL-10 | Rolling circle | Roll, Aresti 9 | Continuous rolls flown around a level circle | Spent | Moderate | Subsonic, high coordination |
| TD-04 | Rolling harrier | Three-dimensional, post-stall | A harrier flown while rolling | Spent | Low, unsteady | Subsonic, post-stall, no closed form |
| BF-09 | Rolling scissors | Fighter | Overlapping barrel rolls to force an overshoot | Spent | Moderate to high | Subsonic, energy fight |
| RL-11 | Rolling turn | Roll and turn, Aresti 2 | Level turn flown with continuous rolls | Spent | Moderate | Subsonic |
| BF-10 | Scissors, flat | Fighter | Series of turn reversals to bleed relative speed | Spent | Moderate | Subsonic, energy fight |
| BF-11 | Sliceback | Fighter | Descending slice turn reversal | Height traded for turn | High | Subsonic, energy fight |
| RL-12 | Slow roll | Roll, Aresti 9 | Constant-rate roll holding a straight line | Conserved | Near 1g, mixed | Subsonic |
| RL-13 | [Snap roll][ref_snap_roll] | Roll, Aresti 9 | Autorotative rapid roll with one wing stalled | Some energy dumped | Unsteady, high transient | Subsonic, post-stall, autorotative, no closed form |
| SP-05 | [Spin, upright][ref_spin] | Spin, Aresti 9 | Autorotation following a stall | Dumped | Unsteady | Subsonic, post-stall, autorotative, no closed form |
| TN-06 | [Spiral dive][ref_spiral_dive] | Turn | Overbanked accelerating descending turn with the wing unstalled | Height traded for speed, energy gained if unchecked | High and rising | Subsonic, not autorotative, has a closed form, the contrast to the spin |
| PL-08 | [Split S][ref_split_s] | Partial loop, Aresti 7 and 8 | Half roll to inverted then a half loop down, heading reversed | Height traded for speed | High | Transonic |
| LP-10 | Square loop | Loop, Aresti 7 | Four quarter loops joined by straight lines | Oscillated | High at the corners | Subsonic |
| TN-03 | Steep turn | Turn, training | Sustained level turn at forty-five to sixty degrees of bank | Spent | Moderate, about 2g | Transonic |
| TN-04 | [Sustained level turn][ref_banked_turn] | Turn | Level turn held where the excess power is zero | Spent, balanced | Set by thrust | Transonic |
| TS-01 | [Tailslide, canopy down][ref_tailslide] | Tailslide, Aresti 6 | Up to zero speed, slide backward, pitch nose-down over | Spent to zero | Low, reversed flow | Subsonic, no closed form near zero speed |
| TS-02 | Tailslide, canopy up | Tailslide, Aresti 6 | Up to zero speed, slide backward, pitch nose-up over | Spent to zero | Low, reversed flow | Subsonic, no closed form near zero speed |
| TD-05 | Torque roll | Three-dimensional, post-stall | Vertical prop-hang rolling under engine torque | Spent in the hang | Near 0g | Subsonic, post-stall, torque and gyroscopic, no closed form |
| CX-02 | Tumble | Composite | Commanded end-over-end tumble | Dumped | Unsteady, gyroscopic | Subsonic, post-stall, no closed form |
| RL-14 | Two-point roll | Roll, Aresti 9 | Half roll, a pause inverted, a half roll | Conserved | Near 1g | Subsonic, parametric |
| LP-11 | Vertical eight | Loop, Aresti 7 | Two loops stacked in the vertical | Oscillated | High | Subsonic |
| RL-15 | Vertical roll | Roll, Aresti 9 | Roll flown on a vertical up line | Climb spent, roll conserved | Low | Subsonic, parametric in rolls |
| LP-12 | Vertical S | Loop, Aresti 7 | Linked half loops forming an S in the vertical | Traded | Moderate to high | Subsonic |
| TD-06 | Waterfall | Three-dimensional, post-stall | Backward pitching tumble about the wing near zero airspeed | Dumped | Unsteady | Subsonic, post-stall, no closed form |
| PS-05 | Wing rock | Post-stall | Limit-cycle roll oscillation at high angle of attack | Slowly dumped | Unsteady | Subsonic, post-stall, no closed form |
| TN-05 | [Wingover][ref_wingover] | Turn, training | Climbing turn reversal over the top at low speed | Gently traded up then down | Low to moderate | Subsonic |
| LN-05 | Zero-g pushover | Line | Ballistic near-zero-g arc | Conserved, ballistic | Near 0g | Subsonic |
| LN-06 | Zoom climb | Line, energy | Pure trade of speed for height along a constant energy height | Speed traded for height | Low | Transonic to supersonic, energy |

## Maneuvers Without a Closed Form

A number of rows carry the no-closed-form flag, and they are not a failure of
the catalog but a property of the maneuvers, which live in separated, unsteady,
or autorotative flow that the plug-and-chug relations of the model article do
not describe.
Something can still be said about each of them.
The spins, upright and inverted and flat, are autorotations in which one wing
stays more stalled than the other, so the figure dumps energy height steadily
and is bounded not by a load number but by the departure that begins it and the
recovery that ends it, and the flat and inverted modes are the ones an
autonomous aircraft must be shown to recover from before they are ever
commanded.
The snap and the outside snap are autorotative rolls entered from a stalled
wing, brief and violent, carrying a transient load the structure must tolerate
even though its peak resists a tidy formula.
The post-stall figures, the cobra, the Kulbit, and the Herbst maneuver, are
deliberate excursions far beyond the stall in which the aircraft is flown on its
attitude rather than its lift, dumping speed almost in place, and they are
feasible only where the aircraft keeps control authority past the stall, through
thrust vectoring or a reaction control system or the sheer surface power the
unmanned case can carry without a human limit.
The gyroscopic figures, the Lomcevak and the commanded tumble, draw their
motion from the precession of the spinning mass of the aircraft and its engine,
and are characterized by their entry and their energy dump rather than by a
steady load.
The [three-dimensional and prop-hang figures][ref_three_d_flying], the harrier
and the hover and the torque roll, are sustained flight beyond the stall in which
the propeller thrust rather than the wing carries the aircraft, a regime the
modern [aerobatic][ref_aerobatics] repertoire has opened and one an unmanned
airframe with thrust to spare and no human aboard is unusually free to use,
priced like the others by entry and by control authority rather than by a steady
load.
For all of these the honest statement is the one the structures article made of
flutter, that the figure is real and floatable but that its pricing belongs to a
treatment in unsteady aerodynamics rather than to a closed form, and that for an
unmanned aircraft the binding question is whether the autopilot retains the
authority to enter and leave it safely.

## Parametric Families

Many of the figures above are base cases of a parametric family, and the catalog
lists the base case and notes the parameter rather than spending a row on every
value of it.
A roll on any line may be flown as a continuous roll, or as a hesitation roll
that stops at two, four, or eight points, or as any number of consecutive rolls,
so the point rolls and the multi-roll lines are one family indexed by the number
of points and the number of rotations.
A loop or a vertical line may carry a roll or a snap or a spin on the up line or
the down line, which is how the Aresti system generates its thousands of
figures, each a base figure decorated with a count of rolls and spins.
A turn may be flown level or rolling, through any angle, at any bank.
The cost model treats a parametric family by its trend, since adding rolls to a
line spends a little more energy and demands a little more control bandwidth
without changing the character of the figure, while adding a snap or a spin
changes the character entirely and pushes the figure into the post-stall rows.
The catalog is therefore extensible by parameter rather than by enumeration, and
it is deliberately not the full combinatorial Aresti space, which is a generator
of permutations rather than a reference of distinct maneuvers.

## Alternate Names

Several figures carry more than one name, and a reference is more useful for
recording them.
The hammerhead is also the stall turn or the hammer stall, the snap roll is the
flick roll, the tailslide is sometimes the whip stall, the Split S is the
half-roll-and-pull or the descending half loop, the Immelmann is the roll off
the top, and the inside loop is simply the loop, while the chandelle and the
wingover shade into each other in casual use.
The basic fighter maneuvers carry their own vocabulary, the high and low yo-yo,
the pitchback and the sliceback, and the flat and the rolling scissors, names
from air-combat doctrine rather than from the competition catalog.
Where an alternate name is in common use the reader should expect to find the
same costed trajectory under it, since the physics of the figure does not change
with the label.

## Using the Catalog

An autonomy designer uses the catalog by reading it in the direction opposite to
the way it was built.
The mission states a required spatiotemporal effect, a heading reversal in a
small box, a rapid loss of speed, a gain of height from speed, or a turn of a
given rate, and the path column names the figures that produce it.
The energy-height and peak-load columns then say what each candidate costs in
the budget the energy and structures articles tracked, and the regime column
says whether the figure is even available at the speed of interest, since most
of the catalog is subsonic and only a few rows survive into the transonic and
above.
The flags warn where a figure demands control authority the aircraft may not
have, the post-stall rows needing authority past the stall and the
rudder-dependent rows needing a fin that can carry the load, the same
feasibility gate the model article placed beside the three costs.
What the catalog does for the unmanned case in particular is make the figure a
selectable object with a known cost and a known footprint, so that the autopilot
of the guidance article can choose a maneuver the way it chooses a waypoint,
against a budget rather than against the nerve of a pilot.

## Reading a Row in Numbers

The catalog gives classes rather than values, but a row reads into numbers as
soon as a particular aircraft is named.
Take the break turn, BF-02, on the twenty-five-kilogram aircraft of the model
article, whose corner speed is about thirty-eight meters per second at a
structural limit near four and four tenths gravities.
The path column says a maximum-rate level turn and the peak-load column says high
and to the corner, and reading those against the structures article gives a turn
radius of about thirty-four meters and a rate near sixty-three degrees per
second, the tightest the airframe allows.
The energy-height column says the excess power is spent hard, which the model
article quantified as a deeply negative specific excess power, so the figure is
an instantaneous one that bleeds energy and cannot be held.
The regime column says subsonic, so none of the high-speed cautions apply.
That is the intended use, the qualitative row narrowing to a quantitative answer
once the airframe supplies the wing loading, the corner speed, and the limit
load.

## Out of Scope

Several things are deliberately excluded.
The full combinatorial enumeration of the Aresti space is left to a generator,
since it is permutations rather than distinct maneuvers and could not be
verified row by row in any case.
The judging and scoring formalism of competition aerobatics, the difficulty
coefficients and the figure symbols, is a human-sport concern beside the point
of a costed trajectory.
The human technique and physiology of flying these figures are out of scope by
the same choice the model article made.
The control-law synthesis that would actually fly each figure belongs to the
dynamics and guidance articles, and the unsteady aerodynamics that would price
the post-stall figures belongs to a treatment of its own.
And the precise load and energy numbers for a given airframe are a matter for
simulation and flight test, since the catalog gives the class and the sign, not
the certified value.

## Conclusion

This catalog turns the model of the previous article into a reference, a list of
the recognized maneuvers each classified by what it does to the energy state,
what load it demands, and how high in the speed range it survives.
The definitions are borrowed from the established catalogs and the
classification is an original and qualitative synthesis, offered to be checked
rather than trusted, and honest about the post-stall figures that admit no
closed form.
Its purpose is the one that has run through the whole extension set, to let an
unmanned aircraft and its autonomy treat a maneuver as a selectable object with
a known cost and footprint, chosen against the budget of energy and structure
and heat rather than against the limits of a person who is no longer aboard.

## References

- [Book, Flight Mechanics of High-Performance Aircraft, Vinh][book_vinh]
- [Reference, Aerobatic Maneuver][ref_aerobatic_maneuver]
- [Reference, Aerobatics][ref_aerobatics]
- [Reference, Aileron Roll][ref_aileron_roll]
- [Reference, Aresti Catalog][ref_aresti]
- [Reference, Banked Turn][ref_banked_turn]
- [Reference, Barrel Roll][ref_barrel_roll]
- [Reference, Basic Fighter Maneuvers][ref_bfm]
- [Reference, Chandelle][ref_chandelle]
- [Reference, Cuban Eight][ref_cuban_eight]
- [Reference, Energy-Maneuverability Theory][ref_em_theory]
- [Reference, Falling Leaf][ref_falling_leaf]
- [Reference, Fédération Aéronautique Internationale][ref_fai]
- [Reference, Hammerhead Turn][ref_hammerhead]
- [Reference, Herbst Maneuver][ref_herbst]
- [Reference, Immelmann Turn][ref_immelmann]
- [Reference, International Aerobatic Club][ref_iac]
- [Reference, Kulbit][ref_kulbit]
- [Reference, Lomcevak][ref_lomcevak]
- [Reference, Pugachev's Cobra][ref_cobra]
- [Reference, Snap Roll][ref_snap_roll]
- [Reference, Spin in Aerodynamics][ref_spin]
- [Reference, Spiral Dive][ref_spiral_dive]
- [Reference, Split S][ref_split_s]
- [Reference, Tailslide][ref_tailslide]
- [Reference, Three-Dimensional Flying][ref_three_d_flying]
- [Reference, Wingover][ref_wingover]
- [Related Post, Aerobatics as Costed Trajectories for Fixed-Wing UAVs][related_post_aerobatics]
- [Related Post, Dynamic Stability and Control for Fixed-Wing UAVs][related_post_dynamic]
- [Related Post, Guidance, Navigation, and Automatic Landing for Fixed-Wing UAVs][related_post_gnc]
- [Related Post, Staged and Boosted Propulsion for Small Fixed-Wing UAVs][related_post_staged]
- [Related Post, Structures and the Flight Envelope for Fixed-Wing UAVs][related_post_structures]

[book_vinh]: https://books.google.com/books/about/Flight_Mechanics_of_High_Performance_Air.html?id=ND9dDeOARkMC
[ref_aerobatic_maneuver]: https://en.wikipedia.org/wiki/Aerobatic_maneuver
[ref_aerobatics]: https://en.wikipedia.org/wiki/Aerobatics
[ref_aileron_roll]: https://en.wikipedia.org/wiki/Aileron_roll
[ref_aresti]: https://en.wikipedia.org/wiki/Aresti_Catalog
[ref_banked_turn]: https://en.wikipedia.org/wiki/Banked_turn
[ref_barrel_roll]: https://en.wikipedia.org/wiki/Barrel_roll
[ref_bfm]: https://en.wikipedia.org/wiki/Basic_fighter_maneuvers
[ref_chandelle]: https://en.wikipedia.org/wiki/Chandelle
[ref_cuban_eight]: https://en.wikipedia.org/wiki/Cuban_Eight
[ref_em_theory]: https://en.wikipedia.org/wiki/Energy%E2%80%93maneuverability_theory
[ref_falling_leaf]: https://en.wikipedia.org/wiki/Falling_leaf
[ref_fai]: https://en.wikipedia.org/wiki/F%C3%A9d%C3%A9ration_A%C3%A9ronautique_Internationale
[ref_hammerhead]: https://en.wikipedia.org/wiki/Hammerhead_turn
[ref_herbst]: https://en.wikipedia.org/wiki/Herbst_maneuver
[ref_immelmann]: https://en.wikipedia.org/wiki/Immelmann_turn
[ref_iac]: https://en.wikipedia.org/wiki/International_Aerobatic_Club
[ref_kulbit]: https://en.wikipedia.org/wiki/Kulbit
[ref_lomcevak]: https://en.wikipedia.org/wiki/Lomcevak
[ref_cobra]: https://en.wikipedia.org/wiki/Pugachev%27s_Cobra
[ref_snap_roll]: https://en.wikipedia.org/wiki/Snap_roll
[ref_spin]: https://en.wikipedia.org/wiki/Spin_(aerodynamics)
[ref_spiral_dive]: https://en.wikipedia.org/wiki/Spiral_dive
[ref_split_s]: https://en.wikipedia.org/wiki/Split_S
[ref_tailslide]: https://en.wikipedia.org/wiki/Tailslide
[ref_three_d_flying]: https://en.wikipedia.org/wiki/3D_flying
[ref_wingover]: https://en.wikipedia.org/wiki/Wingover
[related_post_aerobatics]: {% post_url 2026-06-11-aerobatics_as_costed_trajectories_for_fixed_wing_uavs %}
[related_post_dynamic]: {% post_url 2026-06-06-dynamic_stability_and_control_for_fixed_wing_uavs %}
[related_post_gnc]: {% post_url 2026-06-08-guidance_navigation_and_automatic_landing_for_fixed_wing_uavs %}
[related_post_staged]: {% post_url 2026-06-03-staged_and_boosted_propulsion_for_fixed_wing_uavs %}
[related_post_structures]: {% post_url 2026-06-10-structures_and_the_flight_envelope_for_fixed_wing_uavs %}
