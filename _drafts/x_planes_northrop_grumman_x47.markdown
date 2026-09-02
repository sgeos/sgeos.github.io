---
layout: post
mathjax: true
comments: true
title: "X-Planes: Northrop Grumman X-47"
date: 2025-11-22 09:00:00 +0000
categories: aerospace history engineering
series: x_planes
series_title: X-Planes
series_index: 48
---
<!-- A344 -->
<script>console.log("A344");</script>

**On 10 July 2013 an aeroplane with nobody aboard caught the three-wire on a carrier at sea, and then on its next approach caught the two-wire.** Choosing between those two wires is a question of about two feet of height at the ramp. **That number is the whole subject of this article**, because everything the X-47B is famous for follows from being able to control a position relative to a moving ship to a precision the deck sets rather than the aeroplane.
This is the forty-eighth article in the [X-Planes series][related_post_a297_framing], following the [X-1][related_post_a298_bell_x1], the [X-2][related_post_a299_bell_x2], the [X-3][related_post_a300_douglas_x3], the [X-4][related_post_a301_northrop_x4], the [X-5][related_post_a302_bell_x5], the [X-6][related_post_a303_convair_x6], the [X-7][related_post_a304_lockheed_x7], the [X-8][related_post_a305_aerojet_x8], the [X-9][related_post_a306_bell_x9], the [X-10][related_post_a307_north_american_x10], the [X-11][related_post_a308_convair_x11], the [X-12][related_post_a309_convair_x12], the [X-13][related_post_a310_ryan_x13], the [X-14][related_post_a311_bell_x14], the [X-15][related_post_a312_north_american_x15], the [X-16][related_post_a313_bell_x16], the [X-17][related_post_a314_lockheed_x17], the [X-18][related_post_a315_hiller_x18], the [X-19][related_post_a316_curtiss_wright_x19], the [X-20][related_post_a317_boeing_x20], the [X-21][related_post_a318_northrop_x21], the [X-22][related_post_a319_bell_x22], the [X-23][related_post_a320_martin_marietta_x23], the [X-24][related_post_a321_martin_marietta_x24], the [X-25][related_post_a322_bensen_x25], the [X-26][related_post_a323_schweizer_x26], the [X-27][related_post_a324_lockheed_x27], the [X-28][related_post_a325_osprey_x28], the [X-29][related_post_a326_grumman_x29], the [X-30][related_post_a327_rockwell_x30], the [X-31][related_post_a328_rockwell_mbb_x31], the [X-32][related_post_a329_boeing_x32], the [X-33][related_post_a330_lockheed_martin_x33], the [X-34][related_post_a331_orbital_sciences_x34], the [X-35][related_post_a332_lockheed_martin_x35], the [X-36][related_post_a333_mcdonnell_douglas_x36], the [X-37][related_post_a334_boeing_x37], the [X-38][related_post_a335_scaled_composites_x38], the [X-39][related_post_a336_x39_reserved_never_assigned], the [X-40][related_post_a337_boeing_x40], the [X-41][related_post_a338_x41_common_aero_vehicle], the [X-42][related_post_a339_orbital_sciences_x42], the [X-43][related_post_a340_micro_craft_x43], the [X-44][related_post_a341_x44_two_aircraft], the [X-45][related_post_a342_boeing_x45], and the [X-46][related_post_a343_boeing_x46].

**This is a full-length article and the record supports the length.** Two airframes flew from February 2011, launched from a catapult at sea, landed under arrest at sea, flew at night, operated in the deck cycle alongside manned aircraft, and refuelled from a tanker without a human in the loop [[Parsch, Northrop Grumman X-47, Directory of U.S. Military Rockets and Missiles][ref_parsch_x47]]. **After three articles about unmanned combat aircraft that did not do these things, this is the one that did.**

**It is also the aeroplane that beat the two this series has just described.** The [X-45][related_post_a342_boeing_x45] demonstrated that one operator could hold two vehicles, and the [X-46][related_post_a343_boeing_x46] was cancelled before an airframe was built. **The previous article sized a requirement without an aeroplane to measure**, and named the assumption it was least sure of. **This article has the aeroplane, so that prediction can be checked**, and the section on what the data changed does exactly that.

## The Research Question

**The binding unknown was whether an unmanned aircraft could be told where it was, relative to a moving deck, accurately enough to land on it.**

**That is a narrower question than it sounds and a harder one.** Autonomous landing on a runway had been done for decades. A runway does not move, its position is surveyed once, and an error of several feet costs nothing. **A carrier deck moves in six degrees of freedom, is making way at twenty to thirty knots, and its usable landing area is a few hundred feet long.**

**The problem is one of relative rather than absolute position.** Knowing the aeroplane's latitude and longitude to a foot is useless if the ship's position is known only to ten. **What matters is the vector between them**, and that is a different measurement with different error sources.

**The X-47A, which flew once, was flying to test exactly this.** Its single flight on 23 February 2003 carried a shipboard relative Global Positioning System and ended with a landing on a pre-designated spot on a runway [[Parsch, Northrop Grumman X-47, Directory of U.S. Military Rockets and Missiles][ref_parsch_x47]]. **Ten years separate that flight from the carrier landing and the subject is the same one.**

## Programme Origin

**The programme began as the losing half of a competition this series has already described.** In June 2000 the Defense Advanced Research Projects Agency awarded study contracts for a carrier-based unmanned combat aircraft to Northrop Grumman and to Boeing, of two million dollars each [[Northrop Grumman X-47B][ref_x47b_wikipedia]] [[previous article][related_post_a343_boeing_x46]]. Boeing's answer was the X-46A and Northrop Grumman's the X-47A.

**Northrop Grumman built hardware at its own expense and Boeing did not.** The X-47A Pegasus was completed in July 2001, received its designation in June 2001, and flew on 23 February 2003 [[Parsch, Northrop Grumman X-47, Directory of U.S. Military Rockets and Missiles][ref_parsch_x47]] [[Northrop Grumman X-47A Pegasus][ref_x47a_wikipedia]]. **That was its only flight.** In April 2003 the naval effort was merged into the joint programme, and in January 2006 the joint programme was cancelled.

**The competition was then re-run and Northrop Grumman won it.** In August 2007 the X-47B was selected for the Unmanned Combat Air System Demonstration, under a contract of 635.8 million dollars [[Northrop Grumman X-47B][ref_x47b_wikipedia]]. **The aeroplane was unveiled in December 2008 and first flew on 4 February 2011 at Edwards Air Force Base**, with the second airframe following on 22 November 2011.

**The programme was a demonstration and it was not a procurement.** Its stated purpose was to show carrier suitability, and the Navy declared the primary test programme complete in May 2015. **Neither airframe entered service and neither was intended to.**

## Sizing From First Principles

**The deck sets the requirement and the geometry of the deck is public even where the aeroplane's performance is not.**

### What Choosing a Wire Costs in Height

**A carrier's landing area carries four arresting pendants and a pilot aims for the third.** Published accounts of the Nimitz class give the spacing between pendants as forty feet in some sources and fifty in others, and both are carried here rather than one being chosen.

**A glide slope converts height into distance along the deck, and the conversion is unfavourable.** For a glide slope $\gamma$, a height error $\Delta h$ at the ramp displaces the touchdown point by

$$\Delta x = \frac{\Delta h}{\tan \gamma}$$

**At the three degrees a carrier approach uses, one foot of height becomes 19.08 feet along the deck.** The same relation read the other way says what a wire is worth in height,

$$\Delta h = \Delta x \tan \gamma$$

| pendant spacing, ft | glide slope, degrees | height per wire, ft | height per wire, cm |
|---|---|---|---|
| 40 | 3.0 | 2.10 | 64 |
| 40 | 3.5 | 2.45 | 75 |
| 40 | 4.0 | 2.80 | 85 |
| 50 | 3.0 | 2.62 | 80 |
| 50 | 3.5 | 3.06 | 93 |
| 50 | 4.0 | 3.50 | 107 |

**Choosing between adjacent wires is therefore a question of two to three and a half feet of height**, or roughly two-thirds of a metre to one metre. **That is the precision the deck demands** and it is demanded of a measurement taken with respect to something that is itself moving.

### Why the Measurement Has to Be Relative

**The ship does not wait.** A carrier making twenty-five knots covers 12.9 metres every second, and an aeroplane closing at 145 knots against that deck closes at 61.7 metres per second.

$$v_{\text{closure}} = v_{\text{aircraft}} - v_{\text{ship}} = (145 - 25) \times 0.5144 = 61.7 \ \text{m/s}$$

**At a hundred updates a second the deck moves 12.9 centimetres between one fix and the next**, and the aeroplane closes 61.7 centimetres. **A navigation solution referenced to the earth would have to carry the ship's own position error into the aeroplane's**, and those errors do not cancel because they come from different receivers at different times.

**A differential measurement between the two removes most of what they share.** The satellite clock and ephemeris errors and the bulk of the atmospheric delay are common to two receivers a few miles apart, so a solution computed on the difference is far more accurate than either absolute position [[Misra and Enge, Global Positioning System, signals, measurements and performance][book_misra_enge]]. **The same principle underlies the joint precision approach and landing system the services later fielded** [[Joint Precision Approach and Landing System, Collins Aerospace][ref_jpals_collins]]. **The programme used a precision relative scheme of this kind**, described as allowing the aeroplane to know where it was with respect to the ship [[Parsch, Northrop Grumman X-47, Directory of U.S. Military Rockets and Missiles][ref_parsch_x47]].

**What the open record does not give is the accuracy achieved.** Figures circulate and none of them is traceable to a programme document, so this article computes what the deck requires and does not assert what the aeroplane delivered.

### The Arrestment

**The landing is over in about three seconds and it is the most violent thing the airframe does.** A reported engagement brought the aeroplane from about 145 knots to rest in less than 350 feet [[X-47B makes first arrested landing aboard an aircraft carrier][ref_first_trap]]. Taking constant deceleration,

$$a = \frac{v^{2}}{2s}$$

| reading of the speed | deceleration, m/s² | in g | time to stop, s |
|---|---|---|---|
| 145 kn as airspeed | 26.08 | 2.66 | 2.86 |
| about 120 kn over the deck, allowing 25 kn of wind | 17.86 | 1.82 | 3.46 |

**The two readings differ by a factor of one and a half and the record does not say which is meant.** An arresting engagement is rated on speed relative to the deck, while a quoted airspeed is relative to the air, and the difference is the wind over the deck. **Both are given because choosing silently would be inventing a figure.**

The energy the gear absorbs follows directly,

$$E = \tfrac{1}{2} m v^{2} = \tfrac{1}{2} \times 20{,}185 \times 74.6^{2} = 56.2 \ \text{MJ}$$

**Fifty-six megajoules is the kinetic energy of a small car at two hundred miles an hour**, taken out of the aeroplane in under three seconds by a hook and a wire.

## The Two Aircraft

**The X-47A and the X-47B share a designation, a manufacturer and a subject, and almost nothing else.**

| | X-47A Pegasus | X-47B |
|---|---|---|
| span | 8.47 m | 18.9 m |
| length | 8.50 m | 11.6 m |
| gross mass | 2,500 kg | 19,000 kg |
| engine | Pratt and Whitney JT15D-5C | Pratt and Whitney F100-PW-220U |
| thrust | 14.2 kN | 71.2 kN |
| payload | none | 2,040 kg |
| flights | one | many |

**The X-47A is a proof of concept and the X-47B is an aeroplane.** The gross mass ratio is 7.6 and the thrust ratio 5.0, and the second aircraft carries a payload while the first carries none [[Parsch, Northrop Grumman X-47, Directory of U.S. Military Rockets and Missiles][ref_parsch_x47]].

**The X-47B's wing is the part worth measuring.** Its span is 62.1 feet, folding to 30.9, over a wing area of 953.6 square feet [[Northrop Grumman X-47B][ref_x47b_wikipedia]], which makes the aspect ratio

$$A\!R = \frac{b^{2}}{S} = \frac{62.1^{2}}{953.6} = 4.04$$

**A folding wing is a structural penalty accepted for a deck-space reason**, and halving the span is what lets the aeroplane fit the spots and the lifts a carrier is built around. **The tailless planform is a signature decision before it is an aerodynamic one** [[Knott, Shaeffer and Tuley, Radar cross section][book_knott]], with a history far older than the jet age [[Wooldridge, Winged wonders, the story of the flying wings][book_wooldridge]], and the stability a fin would supply is replaced by feedback [[Etkin and Reid, Dynamics of flight][book_etkin_reid]]. **The vehicle class itself has a longer history than this programme** [[Unmanned combat aerial vehicle][ref_ucav_wikipedia]].

## Dependent Systems

### Navigation, Which Is the Keystone

**Everything above depends on a position known with respect to the ship**, and the programme's relative scheme is the reason the rest of the aeroplane could be built to ordinary tolerances. **A landing system accurate to a metre would have made the wire a matter of luck**, since a metre of height is half a wire spacing.

### The Structure That Takes the Arrestment

**The hook, the keel and the gear are sized by the numbers in the arrestment table rather than by flight loads.** A deceleration of two to two and a half g applied through a hook at the tail puts the whole airframe in tension [[Tailhook][ref_tailhook_wikipedia]], and a carrier landing gear is sized for a descent rate several times what a runway aeroplane sees [[Raymer, Aircraft design, a conceptual approach][book_raymer]] [[Torenbeek, Synthesis of subsonic airplane design][book_torenbeek]].

### Propulsion

**One Pratt and Whitney F100-PW-220U of 71.2 kilonewtons** [[Parsch, Northrop Grumman X-47, Directory of U.S. Military Rockets and Missiles][ref_parsch_x47]], which is the engine family of the F-15 and F-16 without afterburning [[Pratt and Whitney F100][ref_f100_wikipedia]]. Against the gross mass this gives

$$\frac{T}{W} = \frac{71.2}{19{,}000 \times 9.80665 \times 10^{-3}} = 0.382$$

**The previous article estimated that an aeroplane of this class would need a thrust to weight ratio between 0.30 and 0.40** and computed the thrust that implied. **The measured value falls inside that band**, which is one of the few quantitative predictions in that article the record can confirm.

### Autonomy and the Operator

**The fan-out relation this series established two articles ago governs here too** [[previous article on the X-45][related_post_a342_boeing_x45]],

$$FO = \frac{NT + IT}{IT} = 1 + \frac{NT}{IT}$$

**The X-47B's demonstrations were single-vehicle**, so no fan-out above one is claimed for it, and the article does not compute one. **What it demonstrated instead was that the neglect time can include the recovery**, which is the phase a manned aeroplane cannot delegate at all.

## The Flight Test Record

**This is the first article in four with a flight test record worth tabulating.**

| date | milestone |
|---|---|
| 23 February 2003 | X-47A first and only flight, testing relative navigation |
| 4 February 2011 | X-47B first flight, Edwards Air Force Base |
| 22 November 2011 | second airframe first flight |
| 29 November 2012 | first land-based catapult launch |
| 26 November 2012 | carrier deck evaluation aboard USS Harry S. Truman |
| 14 May 2013 | first catapult launch from a carrier at sea |
| 17 May 2013 | first touch and go aboard a carrier [[Navy's unmanned carrier aircraft performs first touch and go][ref_first_cat]] |
| 10 July 2013 | first arrested landing aboard a carrier at sea |
| 10 April 2014 | first night flight |
| 17 August 2014 | operations in the deck cycle alongside manned aircraft |
| April 2015 | first fully autonomous aerial refuelling |
| May 2015 | primary test programme declared complete |

**The third approach on 10 July 2013 is the most informative entry and it is not in the table.** After two arrested landings the aeroplane was launched again, and an onboard subsystem failure caused it to abort the approach automatically [[X-47B makes first arrested landing aboard an aircraft carrier][ref_first_trap]]. **An automatic wave-off on a detected fault is the behaviour a deck requires**, and a demonstration that produced two traps and one correct refusal is a better result than three traps would have been.

## What the Data Changed

**The previous article sized this requirement without an aeroplane, so its predictions can now be scored.**

**It predicted the wrong gross mass and it named the reason in advance.** That article inherited a payload fraction of 0.12293, measured across two Boeing aircraft, and computed a gross mass of 32,539 pounds for a four thousand pound payload. **The X-47B carries 2,040 kilograms, which is the same payload as the X-45C, at a gross mass of 19,000 kilograms**, so

$$\frac{m_{\text{payload}}}{m_{\text{gross}}} = \frac{2{,}040}{19{,}000} = 0.10737$$

**against the 0.12293 that was assumed**, and the aeroplane is 1.287 times the predicted mass.

**The previous article said this would happen and said why.** It recorded that the inherited payload fraction was its weakest load-bearing assumption, and that a naval variant might not hold it because carrier equipment is charged to empty weight and a designer under that pressure may trade payload fraction rather than accept a larger aeroplane. **The X-47B did both.** It has a lower payload fraction and it is a larger aeroplane, which is the predicted failure in the predicted direction and larger than predicted in magnitude.

**A second prediction failed differently and more interestingly.** That article argued that the carrier approach speed limit caps wing loading and therefore sizes the wing, and it computed wing loadings between 68.7 and 142.4 pounds per square foot. **The X-47B's wing loading is 43.9 pounds per square foot at the directory's gross mass**, below every row in that table.

$$\frac{W}{S} = \frac{41{,}888}{953.6} = 43.9 \ \text{lb/ft}^{2}$$

**So the approach constraint is real and it did not size this wing.** Something else did, and the candidates are fuel volume for a 2,100 nautical mile range and low-speed handling margin on the deck. **A constraint that is satisfied with a wide margin is not the constraint that set the design**, which is a correction to how the previous article used it.

**A third prediction held.** The thrust to weight ratio of 0.382 falls inside the 0.30 to 0.40 band that article assumed.

**What the programme changed outside this series is that carrier aviation stopped being a thing only people could do.** The demonstrations of 2013 to 2015 established launch, recovery, deck operations alongside manned aircraft and autonomous refuelling, which together are the whole cycle.

## Where the Framing Breaks Down

**Five places.**

**The precision this article computes is the deck's requirement and not the aeroplane's performance.** The geometry says a wire is worth two to three and a half feet of height. **It does not say what the X-47B achieved**, and the figures that circulate for that are not traceable to a programme document, so no claim about achieved accuracy is made here.

**The arrestment table cannot resolve its own speed.** A quoted 145 knots may be airspeed or speed over the deck, the two differ by the wind over the deck, and the deceleration differs by a factor of one and a half between them. **The article gives both and the record does not choose.**

**Scoring the previous article's predictions is comparing a requirement to one aeroplane.** The X-47B is a single design by a single manufacturer that won a competition, and a payload fraction measured from it is one observation. **The previous article's constant came from two aircraft and this adds a third from a different company**, which is better evidence and still not a population.

**The gross mass figures disagree between sources by six percent.** The specialist directory gives 19,000 kilograms and other compilations give 44,501 pounds, which is 20,185 kilograms, and the directory warns that its own figures may be inaccurate. **Every mass fraction in this article moves by about six percent between those readings**, and the conclusions do not turn on which is right because the differences being argued about are larger than that.

**Treating the X-47A as a proof of concept understates what its single flight was for.** It carried the relative navigation system that the whole subject turns on, and it is described as landing on a designated spot. **One flight is one flight**, and an article that made more of it would be building on a sentence.

## The Contemporary Literature

| Cluster | Records |
|---|---|
| Other aeronautical and autonomy literature | 1,724 |
| Relative navigation, precision approach and the automatic landing | 840 |
| Automatic takeoff, landing and carrier recovery | 395 |
| Autonomy, mission management and onboard decision making | 241 |
| Aircraft sizing, mission analysis and the weight estimate | 191 |
| Tailless configurations and their control effectors | 147 |
| Aerodynamics of the configuration | 134 |
| Flight control law design and handling qualities | 120 |
| Programme, acquisition and the cost of a demonstrator | 86 |
| Unmanned combat aircraft and the strike mission | 84 |
| Multi-vehicle coordination and cooperative control | 59 |
| Propulsion, inlet integration and installed performance | 54 |
| Human supervisory control and the span of control | 36 |
| Internal weapons carriage and store separation | 26 |
| Airframe structure, composites and affordability | 24 |
| Datalink, latency and beyond-line-of-sight command | 12 |
| Verification, validation and the certification of autonomous software | 11 |
| Low observable design and signature | 10 |
| Suppression of enemy air defences and time-critical targeting | 9 |
| The atmosphere and the flight condition | 2 |
| **Total** | **4,205** |

### Other aeronautical and autonomy literature

**The residual, reported and not hidden.** On-subject work belonging to no cluster above, including aircraft systems, navigation, sensors, simulation and a long tail of single-topic papers. **A residual of roughly a third is a property of a subject that spans two disciplines**, and no attempt was made to force it down by inventing categories.

**1,724 records.** [[A psychological evaluation of 1972][research_a_psychological_1972]] [[Aamir et al 2026][research_aamir_benhamida_2026]] [[Abdelrahman et al 2009][research_abdelrahman_elnomrossy_2009]] [[Abouheaf et al 2019][research_abouheaf_mailhot_2019]] [[Abouzahr and Jacob 2023][research_abouzahr_jacob_2023]] [[Abwanzo 2016][research_abwanzo_2016]] [[Acosta et al 2016][research_acosta_decos_2016]] [[Adams 2000][research_adams_2000]] [[Adams and Moen 1967][research_adams_moen_1967]] [[Adelgren et al 2004][research_adelgren_minor_2004]] [[Advanced Aircraft Control 2026][research_advanced_aircraft_2026]] [[Aerospace Quality Management 2004][research_aerospace_quality_2004]] [[Aerospace series. Unmanned Aircraft][research_aerospace_series]] [[Agrawal 1984][research_agrawal_1984]] [[Ahmad and Narmeen 2026][research_ahmad_narmeen_2026]] [[Ahn et al 2022][research_ahn_kim_2022]] [[Air cargo equipment. Base-restrained][research_air_cargo_c]] [[Air cargo equipment. Wide][research_air_cargo]] [[Air cargo equipment. Wide][research_air_cargo_b]] [[Air Combat Command 2011][research_aircombatcommand_2011]] [[Air Combat Command Langley Afb Va 2000][research_aircombatcommandlangleyafbva_2000]] [[Air Combat Command Langley Afb Va 2013][research_aircombatcommandlangleyafbva_2013]] [[Air Proving Ground Center Eglin Afb Fl 1944][research_airprovinggroundcentereglinafbfl_1944]] [[Air Proving Ground Center Eglin Afb Fl 1949][research_airprovinggroundcentereglinafbfl_1949]] [[Air Proving Ground Center Eglin Afb Fl 1954][research_airprovinggroundcentereglinafbfl_1954]] [[Air Proving Ground Center Eglin Afb Fl 1954][research_airprovinggroundcentereglinafbfl_1954_b]] [[Air Proving Ground Center Eglin Afb Fl 1955][research_airprovinggroundcentereglinafbfl_1955]] [[Air Proving Ground Center Eglin Afb Fl 1955][research_airprovinggroundcentereglinafbfl_1955_b]] [[Air Univ Maxwell Afb Al 1978][research_airunivmaxwellafbal_1978]] [[Airborne Landing Guidance System][research_airborne_landing]] [[Airborne Windshear Systems][research_airborne_windshear]] [[Aircraft Carrier 2005][research_aircraft_carrier_2005]] [[Aircraft carrier base 1987][research_aircraft_carrier_1987]] [[Aircraft Case Studies 2026][research_aircraft_case_2026]] [[Aircraft Characteristics 2022][research_aircraft_characteristics_2022]] [[Aircraft Circuit Breaker and][research_aircraft_circuit]] [[Aircraft Control 2011][research_aircraft_control_2011]] [[Aircraft Cost Considerations 2010][research_aircraft_cost_2010]] [[Aircraft Design A Conceptual 2024][research_aircraft_design_2024]] [[Aircraft design at the 1993][research_aircraft_design_1993]] [[Aircraft Design Fundamentals 2012][research_aircraft_design_2012]] [[Aircraft Design Optimization 2013][research_aircraft_design_2013]] [[Aircraft Dynamics and Classical 2015][research_aircraft_dynamics_2015]] [[Aircraft Flight Control 2014][research_aircraft_flight_2014]] [[Aircraft Flotation Analysis][research_aircraft_flotation]] [[Aircraft Flotation Analysis Methods][research_aircraft_flotation_b]] [[Aircraft ground equipment. Lower][research_aircraft_ground_c]] [[Aircraft ground equipment. Main][research_aircraft_ground_f]] [[Aircraft ground equipment. Upper][research_aircraft_ground_d]] [[Aircraft ground equipment. Upper][research_aircraft_ground_e]] [[Aircraft Ground Flotation Analysis][research_aircraft_ground]] [[Aircraft Landing Measurement System 1971][research_aircraft_landing_1971]] [[Aircraft Load 2010][research_aircraft_load_2010]] [[Aircraft Mechanics 2026][research_aircraft_mechanics_2026]] [[Aircraft Non-Linear Dynamics Equations 2014][research_aircraft_non_linear_2014]] [[Aircraft Operating Envelope 2010][research_aircraft_operating_2010]] [[Aircraft Oxygen Replenishment Coupling][research_aircraft_oxygen]] [[Aircraft Payload Limits for 1970][research_aircraft_payload_1970]] [[Aircraft Performance 2010][research_aircraft_performance_2010_b]] [[Aircraft Performance 2026][research_aircraft_performance_2026]] [[Aircraft Performance Methods 2010][research_aircraft_performance_2010]] [[Aircraft Response Transfer Functions 1997][research_aircraft_response_1997]] [[Aircraft Response Transfer Functions 2013][research_aircraft_response_2013]] [[Aircraft Seat Design Guidance][research_aircraft_seat]] [[Aircraft Simulation Model 2022][research_aircraft_simulation_2022]] [[Aircraft Stability and Control 2026][research_aircraft_stability_2026]] [[Aircraft Stability Derivatives 1998][research_aircraft_stability_1998]] [[Aircraft TIRE Condition Monitoring][research_aircraft_tire_b]] [[Aircraft Tire Pressure Monitoring][research_aircraft_tire]] [[Aircraft Weight and Center 2010][research_aircraft_weight_2010]] [[Aircraft Weight Distribution 2012][research_aircraft_weight_2012]] [[Aircraft Weights Data 2010][research_aircraft_weights_2010]] [[Aircraft with annular wing 2001][research_aircraft_with_2001]] [[Aircraft. Declaration of design][research_aircraft_declaration]] [[Aircraft. Passenger doors interface][research_aircraft_passenger]] [[Airframe Avionics and Systems 2017][research_airframe_avionics_2017]] [[Al-Hiddabi and McClamroch 2002][research_alhiddabi_mcclamroch_2002]] [[Alam et al 2011][research_alam_nguyen_2011]] [[Aldrich and Krabill 1972][research_aldrich_krabill_1972]] [[ALE-a carrier aircraft availability 1977][research_ale_a_carrier_1977]] [[Alexandrov et al 1980][research_alexandrov_kazakov_1980]] [[Alexopoulos et al 2017][research_alexopoulos_kirsch_2017]] [[Alford 1999][research_alford_1999]] [[Ali et al 2024][research_ali_abbas_2024]] [[Allen][research_allen]] [[Allen 2009][research_allen_2009]] [[Altynova et al 2011][research_altynova_wasser_2011]] [[Aluc and Komurgoz 2023][research_aluc_komurgoz_2023]] [[Alvarez and Wissa 2021][research_alvarez_wissa_2021]] [[Aly et al 2002][research_aly_ogot_2002]] [[Ambler and Smith 1974][research_ambler_smith_1974]] [[Analysis and Design of 2020][research_analysis_and_2020]] [[Analytical Methods for Aircraft][research_analytical_methods]] [[Anderson 1973][research_anderson_1973]] [[Anderson 1996][research_anderson_1996]] [[Angell 2009][research_angell_2009]] [[Anggoro 2021][research_anggoro_2021]] [[Anton et al 2012][research_anton_erturk_2012]] [[Antony et al 2024][research_antony_kumar_2024]] [[Appleman 1957][research_appleman_1957]] [[Approach to Landing Guidance][research_approach_to]] [[Argrow 2016][research_argrow_2016]] [[Argrow et al 2008][research_argrow_weatherhead_2008]] [[Armed Forces Health Surveillance Center 2014][research_armedforceshealthsurveillancecenter_2014]] [[Armed Forces Health Surveillance Center 2015][research_armedforceshealthsurveillancecenter_2015]] [[Armed Forces Health Surveillance Center 2015][research_armedforceshealthsurveillancecenter_2015_b]] [[Armstrong 2018][research_armstrong_2018]] [[Army Aviation Center And Fort Rucker Al 1992][research_armyaviationcenterandfortruckeral_1992]] [[Army Aviation Materiel Labs Fort Eustis Va 1963][research_armyaviationmateriellabsforteustisva_1963]] [[Army Safety Center Fort Rucker Al 1991][research_armysafetycenterfortruckeral_1991]] [[Army Safety Center Fort Rucker Al 1991][research_armysafetycenterfortruckeral_1991_b]] [[Army Safety Center Fort Rucker Al 1999][research_armysafetycenterfortruckeral_1999]] [[Army Safety Center Fort Rucker Al 1999][research_armysafetycenterfortruckeral_1999_b]] [[Army Service Forces Washington Dc 1940][research_armyserviceforceswashingtondc_1940]] [[Army War Coll Carlisle Barracks Pa 2006][research_armywarcollcarlislebarrackspa_2006]] [[Asher et al 1975][research_asher_mitchell_1975]] [[Assessment of the state-of-the-art 1979][research_assessment_of_1979]] [[Ateş 2022][research_ates_2022]] [[Atkins and Di Donato 2016][research_atkins_didonato_2016]] [[Atkinson 1990][research_atkinson_1990]] [[Autopilot, Flight Director, and][research_autopilot_flight]] [[Avery and Jacob 2017][research_avery_jacob_2017]] [[Avery et al 2019][research_avery_bunting_2019]] [[Aviation And Troop Command Army St Louis Mo 1995][research_aviationandtroopcommandarmystlouismo_1995]] [[Aviation History and UAS][research_aviation_history]] [[Ayar and Karakoc 2023][research_ayar_karakoc_2023]] [[Aygün et al 2014][research_aygun_tascioglu_2014]] [[Azer et al 2024][research_azer_colpan_2024]] [[Azimov and Bishop 2025][research_azimov_bishop_2025]] [[B and Gupta 2026][research_b_gupta_2026]] [[Bachman 1988][research_bachman_1988]] [[Baek and York 2020][research_baek_york_2020]] [[Bahamonde Jacome and Elham 2017][research_bahamondejacome_elham_2017]] [[Bahrami and Jafarnejadsani 2022][research_bahrami_jafarnejadsani_2022]] [[Bai and Zhang 2011][research_bai_zhang_2011]] [[Baily and Gilbertson 1980][research_baily_gilbertson_1980]] [[Bainum and Diarra 1988][research_bainum_diarra_1988]] [[Bainum et al 2005][research_bainum_tan_2005]] [[Baisden et al 1977][research_baisden_ambler_1977]] [[Baker 1955][research_baker_1955]] [[Baker et al 2000][research_baker_brennan_2000]] [[Balabanov and Haftka 1996][research_balabanov_haftka_1996]] [[Bald 1957][research_bald_1957]] [[Ballou 1963][research_ballou_1963]] [[Banerjee and Taneja 2026][research_banerjee_taneja_2026]] [[Banks 2000][research_banks_2000]] [[Baralli et al 2002][research_baralli_pollini_2002]] [[Baranov and Chernov 2019][research_baranov_chernov_2019]] [[Barnes 1968][research_barnes_1968]] [[Barnett 1961][research_barnett_1961]] [[Bartsch 2018][research_bartsch_2018]] [[Basic Aircraft Oxygen Systems][research_basic_aircraft]] [[Basic Principles for the 2012][research_basic_principles_for_2012]] [[Bason et al 1976][research_bason_macintyre_1976]] [[Bass 2006][research_bass_2006]] [[Bass 2013][research_bass_2013]] [[Bastiaens et al 2021][research_bastiaens_mommerency_2021]] [[Bateman et al 2007][research_bateman_nelson_2007]] [[Baum 2021][research_baum_2021]] [[Baum 2021][research_baum_2021_b]] [[Baxter 2013][research_baxter_2013]] [[Bean 2015][research_bean_2015]] [[Bejan 2010][research_bejan_2010]] [[Belart 1938][research_belart_1938]] [[Bell 1997][research_bell_1997]] [[Bell Aerospace Co Buffalo Ny 1956][research_bellaerospacecobuffalony_1956]] [[Belta 2012][research_belta_2012]] [[Belta 2012][research_belta_2012_b]] [[Benders 2018][research_benders_2018]] [[Benders and Koch 2019][research_benders_koch_2019]] [[Benders et al 2018][research_benders_wenz_2018]] [[Bendix Corp York Pa 1963][research_bendixcorpyorkpa_1963]] [[Bennett][research_bennett]] [[Berberi et al 2020][research_berberi_segre_2020]] [[Berkshire 1967][research_berkshire_1967]] [[Bernardin 1961][research_bernardin_1961]] [[Beyer and Mansir 1987][research_beyer_mansir_1987]] [[Bezandry et al 2016][research_bezandry_raglin_2016]] [[Bibin et al 2012][research_bibin_selvaraj_2012]] [[Biggerstaff 1998][research_biggerstaff_1998]] [[Bil 1989][research_bil_1989]] [[Birkeland 2013][research_birkeland_2013]] [[Bishop and Antoulas 1991][research_bishop_antoulas_1991]] [[Bishop and Antoulas 1994][research_bishop_antoulas_1994]] [[Blask 2002][research_blask_2002]] [[Blodgett and Lagor 2022][research_blodgett_lagor_2022]] [[Blumer 1963][research_blumer_1963]] [[Board technology lowers mil/aerospace 2005][research_board_technology_2005]] [[Bogdan 2015][research_bogdan_2015]] [[Bolds 1961][research_bolds_1961]] [[Bolds 1962][research_bolds_1962]] [[Bolzak 1989][research_bolzak_1989]] [[Bonetti et al 2013][research_bonetti_dezaiacomo_2013]] [[Booz-Allen And Hamilton Inc Mclean Va 2000][research_boozallenandhamiltonincmcleanva_2000]] [[Borrelli et al 2006][research_borrelli_subramanian_2006]] [[Bortner 2009][research_bortner_2009]] [[Boskovic and Jackson 2016][research_boskovic_jackson_2016]] [[Boskovic et al 2021][research_boskovic_diel_2021]] [[Bostian and Young 2011][research_bostian_young_2011]] [[Bouadi and Mora-Camino 2012][research_bouadi_moracamino_2012]] [[Boudreault 1983][research_boudreault_1983]] [[Boutros 2015][research_boutros_2015]] [[Bowman, James S. 1965][research_bowmanjamess_1965]] [[Boyd and Scharf 2022][research_boyd_scharf_2022]] [[Boyuk et al 2020][research_boyuk_duvar_2020]] [[Bradshaw and Brunter 1975][research_bradshaw_brunter_1975]] [[Brand and Dresksler 1995][research_brand_dresksler_1995]] [[Breitkopf 1989][research_breitkopf_1989]] [[Breitmaier 1988][research_breitmaier_1988]] [[Brenckmann 1964][research_brenckmann_1964]] [[Breunig and Sayed 2018][research_breunig_sayed_2018]] [[Briere 2007][research_briere_2007]] [[Briere and Warkander 2007][research_briere_warkander_2007]] [[Briggs 2002][research_briggs_2002]] [[Brodersen and Sauer 1992][research_brodersen_sauer_1992]] [[Brodzinsky 1959][research_brodzinsky_1959]] [[Broglio 1961][research_broglio_1961]] [[Broglio 1962][research_broglio_1962]] [[Brown 1950][research_brown_1950]] [[Brown et al 2014][research_brown_mchenry_2014]] [[Bruening et al 2000][research_bruening_snyder_2000]] [[Bruening et al 2001][research_bruening_snyder_2001]] [[Brungardt 2011][research_brungardt_2011]] [[Bryce L Horvath and Gregory A Wrenn][research_brycelhorvath_gregoryawrenn]] [[Buchanan 2010][research_buchanan_2010]] [[Bucholtz et al 2008][research_bucholtz_nichols_2008]] [[Bucklew 2009][research_bucklew_2009]] [[Buckner 2000][research_buckner_2000]] [[Budd 2002][research_budd_2002]] [[Bulka and Nahon 2019][research_bulka_nahon_2019]] [[Burcham 1998][research_burcham_1998]] [[Burke 2015][research_burke_2015]] [[Burken et al 2011][research_burken_frost_2011]] [[Burns 2000][research_burns_2000]] [[Burnside 1974][research_burnside_1974]] [[Bushey][research_bushey]] [[Bye 1993][research_bye_1993]] [[Callens and Pugmire 1969][research_callens_pugmire_1969]] [[Callicoatt 2009][research_callicoatt_2009]] [[Calvano and Harney 1998][research_calvano_harney_1998]] [[Camatti et al 1998][research_camatti_chiesa_1998]] [[Cameron et al 2022][research_cameron_fredin_2022]] [[Campbell 1959][research_campbell_1959]] [[Canpolat et al 2009][research_canpolat_yayla_2009]] [[Cao and Morse 2008][research_cao_morse_2008]] [[Cao et al 2026][research_cao_gao_2026]] [[Carico 1995][research_carico_1995]] [[Caron][research_caron]] [[Carpenter and Jenny 1964][research_carpenter_jenny_1964]] [[Carr et al 2003][research_carr_lambrecht_2003]] [[Carretta and Ree 1999][research_carretta_ree_1999]] [[Carrier et al 2022][research_carrier_arnoult_2022]] [[Carrillo Córcoles et al 2023][research_carrillocorcoles_mertens_2023]] [[Carrio Fernández][research_carriofernandez]] [[Carter and Mueller 1991][research_carter_mueller_1991]] [[Casarosa et al 2004][research_casarosa_galatolo_2004]] [[Case 1965][research_case_1965]] [[Casey-Maslen 2018][research_caseymaslen_2018]] [[Casey-Maslen 2018][research_caseymaslen_2018_b]] [[Casey-Maslen 2018][research_caseymaslen_2018_c]] [[Castagno et al 2018][research_castagno_ochoa_2018]] [[Castanon and Cassandras 2010][research_castanon_cassandras_2010]] [[Castrichini et al 2016][research_castrichini_hodigeresiddaramaiah_2016]] [[Catchpole 1990][research_catchpole_1990]] [[Categorization and classification of][research_categorization_and]] [[Caurin et al 2024][research_caurin_daudfilho_2024]] [[Cazaurang et al 2003][research_cazaurang_bergeon_2003]] [[Cecrdle 2019][research_cecrdle_2019]] [[Celko et al 1995][research_celko_dubois_1995]] [[Ceren and Altuğ 2011][research_ceren_altug_2011]] [[Chai and Wilhite 2012][research_chai_wilhite_2012]] [[Chana and Sullivan 1992][research_chana_sullivan_1992]] [[Chandler 1989][research_chandler_1989]] [[Chang 2006][research_chang_2006]] [[Changes in top management 2002][research_changes_in_2002]] [[Chapa 2013][research_chapa_2013]] [[Chapter 3. Dynamics of 2005][research_chapter_3_2005]] [[Chapter 3U.S. Aviation Regulatory 2016][research_chapter_3u_s_2016]] [[Characteristics of Aircraft Types 2010][research_characteristics_of_2010]] [[Chattot 2005][research_chattot_2005]] [[Chattot 2006][research_chattot_2006]] [[Chaudhry et al 2016][research_chaudhry_smith_2016]] [[Chaussee and Dervault 2013][research_chaussee_dervault_2013]] [[Chen 1964][research_chen_1964]] [[Chen 1995][research_chen_1995]] [[Chen 2025][research_chen_2025]] [[Chen and Ho 2017][research_chen_ho_2017]] [[Chen and Hubner 2021][research_chen_hubner_2021]] [[Chen et al 2020][research_chen_zhou_2020]] [[Chen et al 2020][research_chen_zhou_2020_b]] [[Chen et al 2020][research_chen_zhou_2020_c]] [[Chen et al 2021][research_chen_zhou_2021]] [[Chen et al 2024][research_chen_yang_2024]] [[Chesser et al 1999][research_chesser_draper_1999]] [[Chessman 2022][research_chessman_2022]] [[Chester 2002][research_chester_2002]] [[Chester 2002][research_chester_2002_b]] [[Cheung et al 2020][research_cheung_rezgui_2020]] [[Chiang and Youssef 1995][research_chiang_youssef_1995]] [[Childers and Condon 2004][research_childers_condon_2004]] [[Chisman 1991][research_chisman_1991]] [[Chitrakaran et al 2005][research_chitrakaran_dawson_2005]] [[Chiu Hung Luk et al][research_chiuhungluk_gao]] [[Chorley 1981][research_chorley_1981]] [[Cifaldi 2017][research_cifaldi_2017]] [[Cihak and Anton W. 2005][research_cihak_antonw_2005]] [[Civil Nuclear Systems Corp Albuquerque Nm 1977][research_civilnuclearsystemscorpalbuquerquenm_1977]] [[Civil small and light][research_civil_small]] [[Civil small and light][research_civil_small_b]] [[Clark 2006][research_clark_2006]] [[Clark 2013][research_clark_2013]] [[Cleveland 1970][research_cleveland_1970]] [[Clothier and Walker 2014][research_clothier_walker_2014]] [[Cockpit Visibility for Commercial][research_cockpit_visibility]] [[Coiro and Nicolosi 2001][research_coiro_nicolosi_2001]] [[Cole 1989][research_cole_1989]] [[Computer vision-based approach for 2025][research_computer_vision_based_2025]] [[Conducting Unmanned Aircraft Flight 2015][research_conducting_unmanned_2015]] [[Configuring Aircraft 2010][research_configuring_aircraft_2010]] [[Connolly 1981][research_connolly_1981]] [[Connolly et al 2023][research_connolly_ogorman_2023]] [[Construction vehicles with an 2025][research_construction_vehicles_2025]] [[Control of cooperative unmanned][research_control_of_cooperative]] [[Cook 1964][research_cook_1964]] [[Cook et al 2005][research_cook_kokolios_2005]] [[Cooke and Speck 1971][research_cooke_speck_1971]] [[Cookerly 1988][research_cookerly_1988]] [[Cooper 2023][research_cooper_2023]] [[Cooper and Stroud 1972][research_cooper_stroud_1972]] [[Coopmans et al 2013][research_coopmans_jensen_2013]] [[Coordinating Research Council Inc Atlanta Ga 1988][research_coordinatingresearchcouncilincatlantaga_1988]] [[Coppock and Gerke 1977][research_coppock_gerke_1977]] [[Corley et al 2008][research_corley_kehler_2008]] [[Corn et al 2005][research_corn_mclaurine_2005]] [[Corridor-Wide Surveillance Using Unmanned 2021][research_corridor_wide_surveillance_2021]] [[Corridor-Wide Surveillance Using Unmanned 2023][research_corridor_wide_surveillance_2023]] [[Corridor-Wide Surveillance Using Unmanned 2023][research_corridor_wide_surveillance_2023_b]] [[Corridor-Wide Surveillance Using Unmanned 2024][research_corridor_wide_surveillance_2024]] [[Corridor-Wide Surveillance Using Unmanned 2025][research_corridor_wide_surveillance_2025]] [[Cote 2015][research_cote_2015]] [[Cour-Harbo 2018][research_courharbo_2018]] [[Cour-Harbo 2020][research_courharbo_2020]] [[Courtaulds Aerospace launch quick 1998][research_courtaulds_aerospace_1998]] [[Courtois and Aouf 2017][research_courtois_aouf_2017]] [[Coutard and Chaumette 2011][research_coutard_chaumette_2011_b]] [[Cox and Roy 1988][research_cox_roy_1988]] [[Coyle 1992][research_coyle_1992]] [[Coyle and Herr 2026][research_coyle_herr_2026]] [[Craig et al 1991][research_craig_zwernemann_1991]] [[Crandall 1999][research_crandall_1999]] [[Cranfield helps launch the 2008][research_cranfield_helps_2008]] [[Crew Safety Provision for][research_crew_safety_b]] [[Crew Safety Provisions for][research_crew_safety]] [[Cristofaro et al 2015][research_cristofaro_johansen_2015]] [[Cronk 2007][research_cronk_2007]] [[Crossley 2004][research_crossley_2004]] [[Cruz and Encarnação 2011][research_cruz_encarnacao_2011]] [[Cruz and Fierro 2015][research_cruz_fierro_2015]] [[Cui et al 2020][research_cui_han_2020]] [[Cummins 1999][research_cummins_1999]] [[Cunningham][research_cunningham]] [[Cunningham 1976][research_cunningham_1976]] [[Curlett 2002][research_curlett_2002]] [[Current Manned Aviation Regulation][research_current_manned]] [[Cutler et al 2010][research_cutler_mclain_2010]] [[Cygańczuk and Roguski 2023][research_cyganczuk_roguski_2023]] [[Dahleh and Tsitsiklis 2002][research_dahleh_tsitsiklis_2002]] [[Dai and Cochran 2009][research_dai_cochran_2009]] [[Dal'Carobo and Fensterseifer 2010][research_dalcarobo_fensterseifer_2010]] [[Dalamagkidis 2014][research_dalamagkidis_2014]] [[Dalamagkidis 2014][research_dalamagkidis_2014_b]] [[Dalamagkidis et al 2012][research_dalamagkidis_valavanis_2012]] [[Danko and Oh 2013][research_danko_oh_2013]] [[Dantsker et al 2019][research_dantsker_yu_2019]] [[Darrah and Conrad 1971][research_darrah_conrad_1971]] [[Darvish et al 2015][research_darvish_pourtakdoust_2015]] [[Daud Filho][research_daudfilho]] [[David 2025][research_david_2025]] [[Davidson and Little 1977][research_davidson_little_1977]] [[Dawson 2015][research_dawson_2015]] [[de Poix 1964][research_depoix_1964]] [[Defense Science Board Washington Dc 2002][research_defensescienceboardwashingtondc_2002]] [[DeJarnette-Crumsey et al 2022][research_dejarnettecrumsey_savage_2022]] [[Del Vecchio and Costa 1999][research_delvecchio_costa_1999]] [[Delgado Regis et al 2004][research_delgadoregis_mattos_2004]] [[Demir et al 2021][research_demir_gorguluarslan_2021]] [[Demircali and Uvet 2018][research_demircali_uvet_2018]] [[Denegri et al 2021][research_denegri_sharma_2021]] [[Denham and Paines 2008][research_denham_paines_2008]] [[Department Of Defense Washington Dc 1994][research_departmentofdefensewashingtondc_1994]] [[Department Of Defense Washington Dc 2009][research_departmentofdefensewashingtondc_2009]] [[Department Of The Air Force Washington Dc 1986][research_departmentoftheairforcewashingtondc_1986]] [[Department Of The Air Force Washington Dc 1997][research_departmentoftheairforcewashingtondc_1997]] [[Department Of The Air Force Washington Dc 2004][research_departmentoftheairforcewashingtondc_2004]] [[Department Of The Air Force Washington Dc 2005][research_departmentoftheairforcewashingtondc_2005]] [[Deresh 1982][research_deresh_1982]] [[Design and Development of 2014][research_design_and_2014]] [[Design and Fluid Flow 2015][research_design_and_2015]] [[Design and Implementation of 2014][research_design_and_2014_b]] [[Design constraints in the 1993][research_design_constraints_1993]] [[Design of Locking Mechanism 2024][research_design_of_2024_b]] [[Design of the Well-Tempered 2013][research_design_of_2013]] [[Design of Unique Aircraft 2024][research_design_of_2024]] [[Desjardins and Laananen 1980][research_desjardins_laananen_1980]] [[Deverill 2000][research_deverill_2000]] [[Deyoung 1971][research_deyoung_1971]] [[Diana 2015][research_diana_2015]] [[Dickey and Marek 1963][research_dickey_marek_1963]] [[Dickinson and Goggin 2000][research_dickinson_goggin_2000]] [[Diget et al 2022][research_diget_hasan_2022]] [[Digges 1971][research_digges_1971]] [[Digman 2009][research_digman_2009]] [[Ding and Tomlin 2009][research_ding_tomlin_2009]] [[Dixon et al 2005][research_dixon_wickens_2005]] [[Doan][research_doan]] [[Doblhoff 1956][research_doblhoff_1956]] [[DoD Office of Inspector General 2015][research_dodofficeofinspectorgeneral_2015]] [[Dodge 2015][research_dodge_2015]] [[Doggett and Soistmann 1992][research_doggett_soistmann_1992]] [[Doherty and Butzel 1979][research_doherty_butzel_1979]] [[Doherty and Butzel 1979][research_doherty_butzel_1979_b]] [[Doherty et al 2013][research_doherty_heintz_2013]] [[Donmez et al 2008][research_donmez_brzezinski_2008]] [[Dorobantu et al 2013][research_dorobantu_murch_2013]] [[Douglas Aircraft Co Long Beach Ca 1983][research_douglasaircraftcolongbeachca_1983]] [[Douma et al 2021][research_douma_wang_2021]] [[Dowling and Costello 2017][research_dowling_costello_2017]] [[Downs 2009][research_downs_2009]] [[Drinkwater, Iii and Rolls 1965][research_drinkwateriii_rolls_1965]] [[Drummond 1971][research_drummond_1971]] [[Dubicki and Gorospe 2026][research_dubicki_gorospe_2026]] [[Dudek and Schulte 2022][research_dudek_schulte_2022]] [[Dukes 1970][research_dukes_1970]] [[Duong Nguyen et al 2022][research_duongnguyen_kashitani_2022]] [[Durmuş and Duymaz 2023][research_durmus_duymaz_2023]] [[Dwi Setiawan and Aldino 2026][research_dwisetiawan_aldino_2026]] [[Dynamics of Aircraft Motion 2015][research_dynamics_of_2015]] [[Dynamics of Flexible Aircraft 2023][research_dynamics_of_2023_c]] [[Dynamics of Flexible Aircraft 2023][research_dynamics_of_2023_d]] [[Dynamics of Rigid Aircraft 2023][research_dynamics_of_2023_b]] [[Dynamics of Very Flexible 2023][research_dynamics_of_2023]] [[Eaton and Chen 2015][research_eaton_chen_2015]] [[Eckels 1983][research_eckels_1983]] [[Edge et al 2010][research_edge_collins_2010]] [[Edge et al 2011][research_edge_brown_2011]] [[Edwards and Lennie O. 1990][research_edwards_lennieo_1990]] [[Effect of High Mach 2010][research_effect_of_2010]] [[Effing et al 2023][research_effing_schueltke_2023]] [[Eichorn 1989][research_eichorn_1989]] [[Eisenreich 2009][research_eisenreich_2009]] [[Eisler][research_eisler]] [[Ekici et al 2023][research_ekici_dalkiran_2023]] [[El Tin et al 2022][research_eltin_sharf_2022]] [[El-Ferik 2020][research_elferik_2020]] [[El-Sayed and ElHelw 2012][research_elsayed_elhelw_2012]] [[Electric Aircraft 2024][research_electric_aircraft_2024]] [[Electricity in the aircraft 1954][research_electricity_in_1954]] [[Elham and Bahamonde Jacome 2016][research_elham_bahamondejacome_2016]] [[Eller and Cavanagh 2000][research_eller_cavanagh_2000]] [[Elliott 2009][research_elliott_2009]] [[Energy Approach To Performance 2003][research_energy_approach_2003]] [[Engdahl 2004][research_engdahl_2004]] [[Engineering institutions launch aerospace 1998][research_engineering_institutions_1998]] [[Englebry 1980][research_englebry_1980]] [[Englebry 1981][research_englebry_1981]] [[Englezou et al 2022][research_englezou_timotheou_2022]] [[Environmental Control Systems ECS][research_environmental_control]] [[Epperson 2010][research_epperson_2010]] [[Eppley 2012][research_eppley_2012]] [[Er-El 1988][research_erel_1988]] [[Erdman and Mitchum 2013][research_erdman_mitchum_2013]] [[Ericsson 1997][research_ericsson_1997]] [[Ericsson 1998][research_ericsson_1998]] [[Estimating the Takeoff Wing 2010][research_estimating_the_2010]] [[Fahimi 2005][research_fahimi_2005]] [[Fahimi and Thakur 2013][research_fahimi_thakur_2013]] [[Faiz and Agarwal 1998][research_faiz_agarwal_1998]] [[Falcone et al 1974][research_falcone_clark_1974]] [[Fan et al 2021][research_fan_jiang_2021]] [[Fant 2001][research_fant_2001]] [[Farajollahi and Markazi 2010][research_farajollahi_markazi_2010]] [[Farid and Mouhoub 2023][research_farid_mouhoub_2023]] [[Farmani et al 2015][research_farmani_sun_2015]] [[Fenwick 1966][research_fenwick_1966]] [[Ferrier and Duncan 2012][research_ferrier_duncan_2012]] [[Ferrier et al 2024][research_ferrier_christmas_2024]] [[Ferrier et al 2025][research_ferrier_watson_2025]] [[Fibre ropes for offshore][research_fibre_ropes]] [[Fidan and Mostafa 2024][research_fidan_mostafa_2024]] [[Fierro et al][research_fierro_branca]] [[Figge 1973][research_figge_1973]] [[Figge and Bernhardt 1975][research_figge_bernhardt_1975]] [[Fisch et al 2012][research_fisch_lenz_2012]] [[Fischer 2006][research_fischer_2006]] [[Fisher et al 2010][research_fisher_vanzwieten_2010]] [[Flansburg 2015][research_flansburg_2015]] [[Flansburg 2016][research_flansburg_2016]] [[Fleming et al 2004][research_fleming_ng_2004]] [[Flexible wing coating reduces 2007][research_flexible_wing_2007]] [[Flight Control Compartment Nomenclature][research_flight_control]] [[Flight Deck Controls and][research_flight_deck_g]] [[Flight Deck Escape Provisions][research_flight_deck]] [[Flight Deck Instrumentation, Display][research_flight_deck_c]] [[Flight Deck Interior Doors][research_flight_deck_b]] [[Flight Deck Lighting for][research_flight_deck_e]] [[Flight Deck Lighting for][research_flight_deck_f]] [[Flight DECK Seats for][research_flight_deck_d]] [[Flight Dynamics of Elastic 2014][research_flight_dynamics_2014]] [[Flight Envelope Awareness/Protection][research_flight_envelope]] [[Floyd 2000][research_floyd_2000]] [[Foch 1992][research_foch_1992]] [[Foch and Toot 1989][research_foch_toot_1989]] [[Fong 1982][research_fong_1982]] [[Foreign Technology Div Wright-Pattersonafb Oh 1973][research_foreigntechnologydivwrightpattersonafboh_1973]] [[Forrester][research_forrester]] [[Forsmo et al 2013][research_forsmo_grotli_2013]] [[Foss 2026][research_foss_2026]] [[Fradenburgh 1991][research_fradenburgh_1991]] [[Franco et al 2019][research_franco_correia_2019]] [[Frederick et al 2001][research_frederick_jr_2001]] [[Frederick et al 2001][research_frederick_jr_2001_b]] [[Frederick et al 2001][research_frederick_jr_2001_c]] [[Frederick et al 2001][research_frederick_roberta_2001]] [[Frederick et al 2002][research_frederick_jr_2002]] [[Freeway Incident Detection and 2024][research_freeway_incident_2024]] [[Frew and Brown][research_frew_brown]] [[Frey 2011][research_frey_2011]] [[Frontera Sánchez][research_fronterasanchez]] [[Frost 1968][research_frost_1968]] [[Fu 1972][research_fu_1972]] [[Fuchser 1984][research_fuchser_1984]] [[Fukushima and Tsubone 2019][research_fukushima_tsubone_2019]] [[Fuselages and Tails Empennage 2017][research_fuselages_and_2017]] [[Félix et al 2019][research_felix_gomes_2019]] [[Gacy 2011][research_gacy_2011]] [[Gage 1994][research_gage_1994]] [[Gall and Caverly 2025][research_gall_caverly_2025]] [[Galloway 1989][research_galloway_1989]] [[Galloway and Dey 2015][research_galloway_dey_2015]] [[Gao et al 2016][research_gao_kang_2016]] [[Gao et al 2021][research_gao_hu_2021]] [[Gardi et al 2016][research_gardi_ramasamy_2016]] [[Gardi et al 2016][research_gardi_sabatini_2016]] [[Garmendia et al 2016][research_garmendia_chakraborty_2016]] [[Garrard and Zhang 2025][research_garrard_zhang_2025]] [[Gary 1983][research_gary_1983]] [[Gasaway 1969][research_gasaway_1969]] [[Gates 1992][research_gates_1992]] [[Geisler et al 2014][research_geisler_rosikon_2014]] [[Geister and Geister 2013][research_geister_geister_2013]] [[General requirements for tethered][research_general_requirements]] [[General requirements for the][research_general_requirements_b]] [[Generic Aircraft Design Flowchart 2017][research_generic_aircraft_2017]] [[George and Ghose 2009][research_george_ghose_2009]] [[Germond 2025][research_germond_2025]] [[Ghaemi et al 2019][research_ghaemi_lax_2019]] [[Gillett 1994][research_gillett_1994]] [[Girish et al 2014][research_girish_emilio_2014]] [[Giunta 1999][research_giunta_1999]] [[GKN Westland aerospace management 1999][research_gkn_westland_1999]] [[Go and Ramnath 2001][research_go_ramnath_2001]] [[Goddard and Eastgate 2010][research_goddard_eastgate_2010]] [[Goerttler and Schnepf 2024][research_goerttler_schnepf_2024]] [[Gomez and la Cour-Harbo 2021][research_gomez_lacourharbo_2021]] [[Goncharenko et al 2019][research_goncharenko_lebedev_2019]] [[Gonzalez 2013][research_gonzalez_2013]] [[Goodner and Rao 1988][research_goodner_rao_1988]] [[Gopinath and Bakshi 2020][research_gopinath_bakshi_2020]] [[Gorgulu et al 2023][research_gorgulu_yazar_2023]] [[Gorin et al 2024][research_gorin_gubankov_2024]] [[Goth][research_goth]] [[Gou et al 2021][research_gou_dahl_2021]] [[Goudarzi and Richards 2020][research_goudarzi_richards_2020]] [[Gould 2001][research_gould_2001]] [[Gould 2004][research_gould_2004]] [[Govan et al 2018][research_govan_griffith_2018]] [[Grace 1992][research_grace_1992]] [[Graham et al 2023][research_graham_gonzalez_2023]] [[Grant and Lind 2010][research_grant_lind_2010]] [[Grappel et al 2008][research_grappel_harris_2008]] [[Gray 2005][research_gray_2005]] [[Greaney 2010][research_greaney_2010]] [[Green 1998][research_green_1998]] [[Greenhaw 2008][research_greenhaw_2008]] [[Gregory and Tierno 1996][research_gregory_tierno_1996]] [[Grepper and Huguenin 1979][research_grepper_huguenin_1979]] [[Grigsby 2008][research_grigsby_2008]] [[Grimm 1986][research_grimm_1986]] [[Grisworld 2008][research_grisworld_2008]] [[Grotte and Brooks 1982][research_grotte_brooks_1982]] [[Grunch 2000][research_grunch_2000]] [[Gudmundsson 2014][research_gudmundsson_2014_b]] [[Gudmundsson 2014][research_gudmundsson_2014_c]] [[Gudmundsson 2014][research_gudmundsson_2014_d]] [[Gudmundsson 2022][research_gudmundsson_2022_b]] [[Gudmundsson 2022][research_gudmundsson_2022_c]] [[Guidance on aircraft turnaround 2001][research_guidance_on_2001]] [[Guide for Wing Interface][research_guide_for_c]] [[Guillen et al][research_guillen_bell]] [[Guo 2007][research_guo_2007]] [[Guo et al 2025][research_guo_li_2025]] [[Guo et al 2026][research_guo_han_2026]] [[Guo et al 2026][research_guo_liu_2026]] [[Guoqing et al 2016][research_guoqing_tiantian_2016]] [[Gwin 1976][research_gwin_1976]] [[H.M. Aircraft-Carrier Ark Royal 1939][research_h_m_aircraft_carrier_1939]] [[Ha 1995][research_ha_1995]] [[Haas et al 2000][research_haas_gorb_2000]] [[Hafer 2009][research_hafer_2009]] [[Haider et al 2023][research_haider_mansor_2023]] [[Haitao and Yan 2021][research_haitao_yan_2021]] [[Haiyang Chao and YangQuan Chen 2010][research_haiyangchao_yangquanchen_2010]] [[Haley 1990][research_haley_1990]] [[Hamlin 1990][research_hamlin_1990]] [[Hammack and Mullen 1995][research_hammack_mullen_1995]] [[Hammond 1986][research_hammond_1986]] [[Hamnanaka 2018][research_hamnanaka_2018]] [[Han 2022][research_han_2022]] [[Han et al 2019][research_han_xiao_2019]] [[Han et al 2026][research_han_wu_2026]] [[Hann-Shing Ju et al][research_hannshingju_chingchihtsai]] [[Hao and Yongqi 2024][research_hao_yongqi_2024]] [[Harford 1989][research_harford_1989]] [[Haritos and Barnhart 2021][research_haritos_barnhart_2021]] [[Harned and Head 1965][research_harned_head_1965]] [[Hart and Williams 2008][research_hart_williams_2008]] [[Hartmann et al 2017][research_hartmann_schutt_2017]] [[Hartmann et al 2024][research_hartmann_scott_2024]] [[Hartmann et al 2024][research_hartmann_scott_2024_b]] [[Hartney][research_hartney]] [[Hatch et al 2007][research_hatch_williamd_2007]] [[Haugen 1966][research_haugen_1966]] [[Hawkins 1982][research_hawkins_1982]] [[Hawkins 2017][research_hawkins_2017]] [[Hayes 2006][research_hayes_2006]] [[Hays 1989][research_hays_1989]] [[Helliwell 1952][research_helliwell_1952]] [[Henderson 2023][research_henderson_2023]] [[Henne 1989][research_henne_1989]] [[Henrickson et al 2016][research_henrickson_rogers_2016]] [[Hept 2002][research_hept_2002]] [[Herdiana et al 2023][research_herdiana_arifin_2023]] [[Herrera 2014][research_herrera_2014]] [[Herrera Rubio and Parra Prada 2019][research_herrerarubio_parraprada_2019]] [[Heyns and Borden 2017][research_heyns_borden_2017]] [[Hicks 1968][research_hicks_1968]] [[Hicks and Durbin 2014][research_hicks_durbin_2014]] [[Hicks et al 2002][research_hicks_petrov_2002]] [[High altitude reconnaissance aircraft 1989][research_high_altitude_1989]] [[Hightower 1985][research_hightower_1985]] [[Hildebrand 1945][research_hildebrand_1945]] [[Hill 1987][research_hill_1987]] [[Hinsz 2006][research_hinsz_2006]] [[Hirsh 1965][research_hirsh_1965]] [[History of Supersonic Transport 2020][research_history_of_2020]] [[Hobbs 2010][research_hobbs_2010]] [[Hobbs, Alan et al 2016][research_hobbsalan_cardozacolleen_2016]] [[Hobe et al 2026][research_hobe_heile_2026]] [[Hochstetler et al 2016][research_hochstetler_bosma_2016]] [[Hodgkinson and Johnston 2018][research_hodgkinson_johnston_2018]] [[Hodgkinson and Johnston 2018][research_hodgkinson_johnston_2018_b]] [[Hodgkinson and Johnston 2018][research_hodgkinson_johnston_2018_c]] [[Hodgkinson and Johnston 2018][research_hodgkinson_johnston_2018_d]] [[Hodgkinson and Johnston 2018][research_hodgkinson_johnston_2018_e]] [[Hodgkinson and Johnston 2018][research_hodgkinson_johnston_2018_f]] [[Hoffer et al 2013][research_hoffer_coopmans_2013]] [[Holcroft, Christopher Mark, born 2014][research_holcroft_christopher_2014]] [[Holland et al 2009][research_holland_lalejini_2009]] [[Holloway et al 1972][research_holloway_thompson_1972]] [[Holmes 2000][research_holmes_2000]] [[Hone et al 2011][research_hone_friedman_2011]] [[Hoogreef 2026][research_hoogreef_2026]] [[Hopkins et al 2010][research_hopkins_nix_2010]] [[Hossny et al 2020][research_hossny_elbadawy_2020]] [[Hou et al 2020][research_hou_fang_2020]] [[Housel 1952][research_housel_1952]] [[Houtsma 2003][research_houtsma_2003]] [[How et al 2014][research_how_frazzoli_2014]] [[Howard 1995][research_howard_1995]] [[Howard 1996][research_howard_1996]] [[Howard 2002][research_howard_2002]] [[Howard 2023][research_howard_2023]] [[Howe 2000][research_howe_2000]] [[Hoy 1963][research_hoy_1963]] [[Hu et al 2019][research_hu_bent_2019]] [[Hu et al 2026][research_hu_liu_2026]] [[Huang 2013][research_huang_2013]] [[Huang and Tomlin 2009][research_huang_tomlin_2009]] [[Huang and Zhang 2020][research_huang_zhang_2020]] [[Huang et al 2026][research_huang_chen_2026]] [[Huber and Reynolds 1976][research_huber_reynolds_1976]] [[Hughes 1982][research_hughes_1982]] [[Hughes aircraft nominates payload 1984][research_hughes_aircraft_1984]] [[Human Factors in Unmanned 2016][research_human_factors_2016]] [[Hunter et al 2018][research_hunter_schaal_2018]] [[Huttunen and Scott 2023][research_huttunen_scott_2023]] [[Hwang and Pi 1978][research_hwang_pi_1978]] [[Hwang and Pi 1979][research_hwang_pi_1979]] [[Hwang et al 2007][research_hwang_balakrishnan_2007]] [[Hůlek 2015][research_hulek_2015]] [[I. Scott and T. Huttunen 2023][research_iscott_thuttunen_2023]] [[Ikonen and Sobester 2016][research_ikonen_sobester_2016]] [[Illustrations and Comments on 2016][research_illustrations_and_2016]] [[Imado and Kuroda 2011][research_imado_kuroda_2011]] [[In-flight control and guidance 2006][research_in_flight_control_2006]] [[In-Flight Refuelling 1961][research_in_flight_refuelling_1961]] [[Incremona and Ferrara 2023][research_incremona_ferrara_2023]] [[Initial evaluation of video 2012][research_initial_evaluation_2012]] [[Initiative for aircraft launch 2007][research_initiative_for_2007]] [[Instrument Panel Arrangement for][research_instrument_panel]] [[International Conference on Unmanned 2013][research_international_conference_2013]] [[International Conference on Unmanned 2014][research_international_conference_2014]] [[International Conference on Unmanned 2015][research_international_conference_2015]] [[International Conference on Unmanned 2016][research_international_conference_2016]] [[International Conference on Unmanned 2017][research_international_conference_2017]] [[International Conference on Unmanned 2018][research_international_conference_2018]] [[International Conference on Unmanned 2019][research_international_conference_2019]] [[International Conference on Unmanned 2020][research_international_conference_2020]] [[International Conference on Unmanned 2021][research_international_conference_2021]] [[International Conference on Unmanned 2021][research_international_conference_2021_b]] [[International Conference on Unmanned 2022][research_international_conference_2022]] [[International Conference on Unmanned 2023][research_international_conference_2023]] [[International Conference on Unmanned 2024][research_international_conference_2024]] [[International Conference on Unmanned 2025][research_international_conference_2025]] [[International Conference on Unmanned 2026][research_international_conference_2026]] [[International Symposium on Unmanned 2024][research_international_symposium_2024]] [[Introduction to Aircraft Flight 1998][research_introduction_to_1998]] [[Introduction to Unmanned Aircraft 2010][research_introduction_to_2010]] [[Iran will destroy a 2020][research_iran_will_2020]] [[Irvin and Swan 1956][research_irvin_swan_1956]] [[Itt Systems Rome Ny 1987][research_ittsystemsromeny_1987]] [[Işilak and Oktal 2025][research_isilak_oktal_2025]] [[İşci and Günel 2021][research_isci_gunel_2021]] [[Jackson 2001][research_jackson_2001]] [[Jackson et al 1996][research_jackson_jr_1996]] [[Jacobson and Tsubaki 1986][research_jacobson_tsubaki_1986]] [[James 1972][research_james_1972]] [[Jameson 2009][research_jameson_2009]] [[Jamison 2010][research_jamison_2010]] [[Janousek and Marcon 2018][research_janousek_marcon_2018]] [[Janousek et al 2010][research_janousek_bjorn_2010]] [[Japan's aircraft carrier plan 2018][research_japan_s_aircraft_2018]] [[Jauron 1993][research_jauron_1993]] [[Jazzar and Kale 2023][research_jazzar_kale_2023]] [[Jenkins et al 2005][research_jenkins_snodgrass_2005]] [[Jensen 2016][research_jensen_2016]] [[Jensen 2021][research_jensen_2021]] [[Jian and Ke-Qin 2004][research_jian_keqin_2004]] [[Jiang et al 2017][research_jiang_su_2017]] [[Jiang et al 2022][research_jiang_liu_2022]] [[Jiang et al 2022][research_jiang_nan_2022]] [[Jin 2024][research_jin_2024]] [[John 2014][research_john_2014]] [[Johnson 1966][research_johnson_1966]] [[Johnson 1972][research_johnson_1972]] [[Johnson 1993][research_johnson_1993]] [[Johnson 1995][research_johnson_1995]] [[Johnson 1997][research_johnson_1997]] [[Johnson and Robertson 1980][research_johnson_robertson_1980]] [[Johnson, Jr. and White 1983][research_johnsonjr_white_1983]] [[Johnston and Swenson 2009][research_johnston_swenson_2009]] [[Johnston and Swenson 2010][research_johnston_swenson_2010]] [[Jones 1973][research_jones_1973]] [[Jones 1992][research_jones_1992]] [[Jones 2009][research_jones_2009]] [[Jones and Marsh 2003][research_jones_marsh_2003]] [[Joslin 2015][research_joslin_2015]] [[Journal of Aerospace Technology][research_journal_of]] [[Julke and Kawa 2000][research_julke_kawa_2000]] [[Jurges 1977][research_jurges_1977]] [[Kahya and Konar 2026][research_kahya_konar_2026]] [[Kaliardos and Lyall 2014][research_kaliardos_lyall_2014]] [[Kaliszuk et al 2025][research_kaliszuk_kierzkowski_2025]] [[Kallinen][research_kallinen]] [[Kallinen et al 2020][research_kallinen_martin_2020]] [[Kambampati and Smith 2017][research_kambampati_smith_2017]] [[Kaminski 1997][research_kaminski_1997]] [[Kaminski and Ralston 1996][research_kaminski_ralston_1996]] [[kanahara 2022][research_kanahara_2022]] [[Kane 2014][research_kane_2014]] [[Kansas Univ Lawrence 1952][research_kansasunivlawrence_1952]] [[Kaplan 1965][research_kaplan_1965]] [[Kaplan 1965][research_kaplan_1965_b]] [[Kaplan 1969][research_kaplan_1969]] [[Kaplan and sargent 1965][research_kaplan_sargent_1965]] [[Karimidoona and Schön 2022][research_karimidoona_schon_2022]] [[Kasim 2018][research_kasim_2018]] [[Katrňák and Juračka 2017][research_katrnak_juracka_2017]] [[Katz 1967][research_katz_1967]] [[Katz 1979][research_katz_1979]] [[Kaul 2019][research_kaul_2019]] [[Kaul 2020][research_kaul_2020]] [[Kaye and Freeman 1989][research_kaye_freeman_1989]] [[Kaymal 2016][research_kaymal_2016]] [[Keane et al 2017][research_keane_sobester_2017]] [[Keeping cool at flight 1996][research_keeping_cool_1996]] [[Kelly 2001][research_kelly_2001]] [[Kelly and Skudrna 1981][research_kelly_skudrna_1981]] [[Kemper 2004][research_kemper_2004]] [[Kennedy 1999][research_kennedy_1999]] [[Kern et al 2020][research_kern_bobbe_2020]] [[Kessler et al 2000][research_kessler_spearing_2000]] [[Khalid et al 2026][research_khalid_ahmed_2026]] [[Khan 2021][research_khan_2021]] [[Khan and Khorasani 2010][research_khan_khorasani_2010]] [[Khan and Nahon 2014][research_khan_nahon_2014]] [[Kharchenko et al 2015][research_kharchenko_bogoslavets_2015]] [[Khazetdinov et al 2021][research_khazetdinov_zakiev_2021]] [[Kiflu and Lopez 2015][research_kiflu_lopez_2015]] [[Kilkis 2024][research_kilkis_2024]] [[Kim 2019][research_kim_2019]] [[Kim and Bang 2016][research_kim_bang_2016]] [[Kim and Oh 2017][research_kim_oh_2017]] [[Kim et al 2015][research_kim_jung_2015]] [[Kim et al 2024][research_kim_kang_2024]] [[Kindley 2015][research_kindley_2015]] [[King][research_king]] [[Kirk et al 2022][research_kirk_wang_2022]] [[Kistyarev and Wang 2025][research_kistyarev_wang_2025]] [[Kladis et al 2008][research_kladis_economou_2008]] [[Klemin 1940][research_klemin_1940]] [[Kline 2012][research_kline_2012]] [[Klipp et al 2021][research_klipp_kirk_2021]] [[Klishin and Kolesnikova 2022][research_klishin_kolesnikova_2022]] [[Knutzon][research_knutzon]] [[Ko and Kumar 2019][research_ko_kumar_2019]] [[Kochenderfer et al 2008][research_kochenderfer_kuchar_2008]] [[Korpela et al 2011][research_korpela_danko_2011]] [[Korzatkowski et al 2015][research_korzatkowski_kolsch_2015]] [[Kovtun and Tkachenko 2018][research_kovtun_tkachenko_2018]] [[Kovtun and Tkachenko 2019][research_kovtun_tkachenko_2019]] [[Kozol and Tankins 1993][research_kozol_tankins_1993]] [[Krawczyk et al 2019][research_krawczyk_szczepanski_2019]] [[Kreerenko 2025][research_kreerenko_2025]] [[Krings et al 2013][research_krings_annighofer_2013]] [[Krispin and Portnoy 1988][research_krispin_portnoy_1988]] [[Krozel 2002][research_krozel_2002]] [[Kube et al 2018][research_kube_bischof_2018]] [[Kucherov et al 2019][research_kucherov_sushchenko_2019]] [[Kumar 1997][research_kumar_1997]] [[Kumar and Kumar 2022][research_kumar_kumar_2022]] [[Kumar et al 2007][research_kumar_shanmugam_2007]] [[Kumuk and Ilbas 2023][research_kumuk_ilbas_2023]] [[Kuppusamy and Yoon 2016][research_kuppusamy_yoon_2016]] [[Kurdel et al 2024][research_kurdel_gecejova_2024]] [[Kurdyla 1963][research_kurdyla_1963]] [[Kurkcu et al 2011][research_kurkcu_erhan_2011]] [[Kushneruk 2026][research_kushneruk_2026]] [[L.P and Ghosh 2020][research_lp_ghosh_2020]] [[La Porte et al 1988][research_laporte_roberts_1988]] [[Laananen 1980][research_laananen_1980]] [[Lachaona Jr 2023][research_lachaonajr_2023]] [[Lahoti et al 2022][research_lahoti_gogulapati_2022]] [[Lange 1983][research_lange_1983]] [[Lange 1984][research_lange_1984]] [[Lanteigne et al 2020][research_lanteigne_mcleod_2020]] [[Larm 2004][research_larm_2004]] [[Larson 1958][research_larson_1958]] [[Lateral-Directional Dynamics 1998][research_lateral_directional_dynamics_1998]] [[Lattimore 1991][research_lattimore_1991]] [[Laufer et al 1997][research_laufer_krauss_1997]] [[Lawrence 2000][research_lawrence_2000]] [[Lawrence 2003][research_lawrence_2003]] [[Lawson 2001][research_lawson_2001]] [[Le et al 2019][research_le_vesely_2019]] [[Lebacqz and Chen 1977][research_lebacqz_chen_1977]] [[Lee 2012][research_lee_2012]] [[Lehman and Kaplan 1965][research_lehman_kaplan_1965]] [[Lemmon 2013][research_lemmon_2013]] [[Lemmon 2015][research_lemmon_2015]] [[Leuchter 2013][research_leuchter_2013]] [[Level Flight Performance Jet 2003][research_level_flight_2003]] [[Lewis and Pickering 2014][research_lewis_pickering_2014]] [[Li 2008][research_li_2008]] [[Li 2019][research_li_2019]] [[Li 2021][research_li_2021]] [[Li and Fan 2018][research_li_fan_2018]] [[Li and Qin 2020][research_li_qin_2020]] [[Li and Zhang 2025][research_li_zhang_2025_b]] [[Li et al 2013][research_li_li_2013]] [[Li et al 2013][research_li_su_2013]] [[Li et al 2013][research_li_zhu_2013]] [[Li et al 2018][research_li_zhang_2018_b]] [[Li et al 2020][research_li_liu_2020]] [[Li et al 2022][research_li_fan_2022]] [[Li et al 2022][research_li_xu_2022]] [[Li et al 2023][research_li_feng_2023]] [[Li et al 2024][research_li_zhou_2024]] [[Li et al 2025][research_li_zhang_2025]] [[Li et al 2025][research_li_zheng_2025]] [[Li et al 2026][research_li_han_2026]] [[Li et al 2026][research_li_liu_2026]] [[Liang et al 2014][research_liang_jia_2014]] [[Liang et al 2020][research_liang_chen_2020]] [[Liggin et al 2001][research_liggin_crawford_2001]] [[Lijesen et al 2005][research_lijesen_nijkamp_2005]] [[Lin and Saripalli 2014][research_lin_saripalli_2014]] [[Lindsay and Sun 2020][research_lindsay_sun_2020]] [[Ling 1970][research_ling_1970]] [[Linnell 1963][research_linnell_1963]] [[Liseitsev 2025][research_liseitsev_2025]] [[Liu 2018][research_liu_2018]] [[Liu and Bush 2004][research_liu_bush_2004]] [[Liu and Wang 2025][research_liu_wang_2025]] [[Liu and Wang 2025][research_liu_wang_2025_b]] [[Liu et al 2017][research_liu_sengupta_2017]] [[Liu et al 2020][research_liu_han_2020]] [[Liu et al 2020][research_liu_zheng_2020]] [[Liu et al 2022][research_liu_han_2022]] [[Liu et al 2024][research_liu_zheng_2024]] [[Liu et al 2025][research_liu_yuan_2025]] [[Locatelli et al 2011][research_locatelli_mulani_2011]] [[Location and Actuation of][research_location_and]] [[Location and Actuation of][research_location_and_b]] [[Loegering and Harris 2002][research_loegering_harris_2002]] [[Londner 2016][research_londner_2016]] [[Longino 1994][research_longino_1994]] [[Lorenz 2015][research_lorenz_2015]] [[Love and Argrow 2021][research_love_argrow_2021]] [[Lovett 1984][research_lovett_1984]] [[Lu and Pierson 1995][research_lu_pierson_1995]] [[Lu and Xu 2024][research_lu_xu_2024]] [[Lu et al 2011][research_lu_jiang_2011]] [[Lu et al 2024][research_lu_liu_2024]] [[Luan and Sun 2020][research_luan_sun_2020]] [[Lungu 2017][research_lungu_2017]] [[Luu 2025][research_luu_2025]] [[Lv et al 2026][research_lv_wang_2026]] [[Lynn 1978][research_lynn_1978]] [[Lyu et al 2021][research_lyu_su_2021]] [[MacGarvey 2014][research_macgarvey_2014]] [[Macnae 1995][research_macnae_1995]] [[Macone 1996][research_macone_1996]] [[Majoros 1989][research_majoros_1989]] [[Makarenko and Tokarev 2023][research_makarenko_tokarev_2023]] [[Maksimova 2025][research_maksimova_2025]] [[Malaek and Soltan-Mohammed 2001][research_malaek_soltanmohammed_2001]] [[Malone and Mason 1992][research_malone_mason_1992]] [[Mann 1963][research_mann_1963]] [[Manned General Aviation Helicopters 2026][research_manned_general_2026]] [[Manon 1981][research_manon_1981]] [[Maraman 1987][research_maraman_1987]] [[Marchese 1963][research_marchese_1963]] [[Mare 2006][research_mare_2006]] [[Marie Vianney et al 2018][research_marievianney_li_2018]] [[Marino 2001][research_marino_2001]] [[Marinov and Penev 2025][research_marinov_penev_2025]] [[Marker 2009][research_marker_2009]] [[Marretta et al 1999][research_marretta_davi_1999]] [[Marshall 2011][research_marshall_2011]] [[Marshall 2016][research_marshall_2016]] [[Martin and McMahon 2017][research_martin_mcmahon_2017]] [[Martinez-Val et al 1994][research_martinezval_perez_1994]] [[Martone 1983][research_martone_1983]] [[Martone and Hawkins 1983][research_martone_hawkins_1983]] [[Mason 1990][research_mason_1990]] [[Mason and Iglesias 2001][research_mason_iglesias_2001]] [[Masud and Khan 2015][research_masud_khan_2015]] [[Mathias et al 1995][research_mathias_ross_1995]] [[Matson et al 2011][research_matson_licht_2011]] [[Matsuno and Andreeva-Mori 2023][research_matsuno_andreevamori_2023]] [[Matsushita et al][research_matsushita_miyata]] [[Maurer 1982][research_maurer_1982]] [[Maurer 1987][research_maurer_1987]] [[Maute and Reich 2006][research_maute_reich_2006]] [[Mazzitelli 1966][research_mazzitelli_1966]] [[Mazzitelli 1967][research_mazzitelli_1967]] [[McCarthy and Chattopadhyay 1996][research_mccarthy_chattopadhyay_1996]] [[McCullough and Dieckmann 1981][research_mccullough_dieckmann_1981]] [[McDermott 2004][research_mcdermott_2004]] [[Mcdonnell Aircraft Corp St Louis Mo 1950][research_mcdonnellaircraftcorpstlouismo_1950]] [[Mcdonnell Aircraft Corp St Louis Mo 1963][research_mcdonnellaircraftcorpstlouismo_1963]] [[McElreath 1972][research_mcelreath_1972]] [[McFadyen and Martin 2016][research_mcfadyen_martin_2016]] [[McFadyen and Martin 2016][research_mcfadyen_martin_2016_b]] [[McFadyen et al 2018][research_mcfadyen_martin_2018]] [[McGahern 2000][research_mcgahern_2000]] [[Mcgee 1977][research_mcgee_1977]] [[McGrath 2000][research_mcgrath_2000]] [[Mcingvale and Dudley 1990][research_mcingvale_dudley_1990]] [[McKinnis et al 2021][research_mckinnis_hauptman_2021]] [[McLaughlin and Perhinschi 2023][research_mclaughlin_perhinschi_2023]] [[Mehta et al 2006][research_mehta_kaiser_2006]] [[Mei 2025][research_mei_2025]] [[Mejdrich 1977][research_mejdrich_1977]] [[Mengali and Pieracci 2000][research_mengali_pieracci_2000]] [[Mengying et al 2017][research_mengying_hua_2017]] [[Merkel and Whitmoyer 1976][research_merkel_whitmoyer_1976]] [[Meyer 2013][research_meyer_2013]] [[Meyer 2015][research_meyer_2015]] [[Microwave Landing System MLS][research_microwave_landing]] [[Middleton 1979][research_middleton_1979]] [[Middleton 1980][research_middleton_1980]] [[Middleton and Thalmann 1981][research_middleton_thalmann_1981]] [[Milano et al 2022][research_milano_primatesta_2022]] [[Miles 1990][research_miles_1990]] [[Miller and Burkhalter 1987][research_miller_burkhalter_1987]] [[Miller and Eagan 1997][research_miller_eagan_1997]] [[Mingfeng Zhang and Liu 2012][research_mingfengzhang_liu_2012]] [[Miniature Unmanned Air Vehicle][research_miniature_unmanned]] [[Miniature Unmanned Air Vehicle 2008][research_miniature_unmanned_2008]] [[Miquel et al 2006][research_miquel_moracamino_2006]] [[Mirosavljević 2023][research_mirosavljevic_2023]] [[Mirot 2013][research_mirot_2013]] [[Mirzaei et al 2008][research_mirzaei_abdollahi_2008]] [[Mirzayev et al 2025][research_mirzayev_ahmadova_2025]] [[Misovec et al][research_misovec_inanc]] [[Mistree 1987][research_mistree_1987]] [[Modeling the Aircraft 2015][research_modeling_the_2015]] [[Moen and Williams 1966][research_moen_williams_1966]] [[Mohamed et al 2013][research_mohamed_aljaroodi_2013]] [[Montalvo and Costello 2015][research_montalvo_costello_2015]] [[Mook and Shyu 1990][research_mook_shyu_1990]] [[Mook and Shyu 1992][research_mook_shyu_1992]] [[Moore 2000][research_moore_2000]] [[Moorhouse 1991][research_moorhouse_1991]] [[Morley 1961][research_morley_1961]] [[Morley 2013][research_morley_2013]] [[Morote and Liaño 2012][research_morote_liano_2012]] [[Morozov 2015][research_morozov_2015]] [[Morris, C. E. K., Jr. 1983][research_morriscekjr_1983]] [[Morris, C. E. K., Jr. 1984][research_morriscekjr_1984]] [[Moser 2011][research_moser_2011]] [[Mostafa and Schnell 2016][research_mostafa_schnell_2016]] [[Moum 2010][research_moum_2010]] [[Mueller 2018][research_mueller_2018]] [[Mueller and Krozel 2000][research_mueller_krozel_2000]] [[Mujica 1987][research_mujica_1987]] [[Mukherjee 2015][research_mukherjee_2015]] [[Mulero-Pázmány et al 2014][research_muleropazmany_negro_2014]] [[Muller 2001][research_muller_2001]] [[Multi-finger Dynamic Position Tracking 2025][research_multi_finger_dynamic_2025]] [[Muniraj and Farhood 2017][research_muniraj_farhood_2017]] [[Munroe 1978][research_munroe_1978]] [[Murray et al 2022][research_murray_richardson_2022]] [[Musolino et al 2012][research_musolino_rizzo_2012]] [[Nadler 2015][research_nadler_2015]] [[Naghash and Enns 1998][research_naghash_enns_1998]] [[Naik and Ostowari 1990][research_naik_ostowari_1990]] [[Nan et al 2024][research_nan_yang_2024]] [[Nangia and Palmer 2007][research_nangia_palmer_2007]] [[Nangia and Palmer 2007][research_nangia_palmer_2007_b]] [[Natesan et al 2008][research_natesan_gu_2008]] [[Nath 2025][research_nath_2025]] [[National Research Council Washington Dc 2001][research_nationalresearchcouncilwashingtondc_2001]] [[Naundrup][research_naundrup]] [[Naval Air Development Center Warminsterpa 1975][research_navalairdevelopmentcenterwarminsterpa_1975]] [[Naval Air Systems Command Patuxent River Md 2013][research_navalairsystemscommandpatuxentrivermd_2013]] [[Naval Aviation Enterprise Patuxent River Md 2012][research_navalaviationenterprisepatuxentrivermd_2012]] [[Naval Postgraduate School Monterey Ca 1981][research_navalpostgraduateschoolmontereyca_1981]] [[Neal 2010][research_neal_2010]] [[Nebiker 1981][research_nebiker_1981]] [[Nedresky 1996][research_nedresky_1996]] [[Neff 2019][research_neff_2019]] [[Negaard 1980][research_negaard_1980]] [[Nelson 1974][research_nelson_1974]] [[Nelson and Dix 2003][research_nelson_dix_2003]] [[Neto et al 2024][research_neto_douradovilla_2024]] [[Neuenswander 2013][research_neuenswander_2013]] [[New Achievements in Unmanned 2023][research_new_achievements_2023]] [[New aircraft carrier expands 2019][research_new_aircraft_2019]] [[New Method for Station 2005][research_new_method_2005]] [[Newcome 2004][research_newcome_2004]] [[Newcome 2009][research_newcome_2009]] [[Newman and Stanzione 1991][research_newman_stanzione_1991]] [[Nguyen et al 2024][research_nguyen_crismer_2024]] [[Ni and Zhang 2026][research_ni_zhang_2026]] [[Ni et al 2018][research_ni_hu_2018]] [[Ni et al 2018][research_ni_hu_2018_b]] [[Nichols 1998][research_nichols_1998]] [[Nichols 2021][research_nichols_2021]] [[Nida and O'Connor 2006][research_nida_oconnor_2006]] [[Niewoehner and Filbey 2005][research_niewoehner_filbey_2005]] [[Nigam and Kroo 2008][research_nigam_kroo_2008]] [[Niles 1964][research_niles_1964]] [[Noise measurements for UAS][research_noise_measurements]] [[Nominal aircraft dynamics][research_nominal_aircraft]] [[Norris 1998][research_norris_1998]] [[Northrop Aircraft Inc Hawthorne Ca 1953][research_northropaircraftinchawthorneca_1953]] [[Norton and Dyme 1952][research_norton_dyme_1952]] [[Norwood and Chichester 2015][research_norwood_chichester_2015]] [[Nugent and Girard 2003][research_nugent_girard_2003]] [[null][research_null]] [[Nygard 1995][research_nygard_1995]] [[O'Keefe 2008][research_okeefe_2008]] [[O.V. Milenin 2019][research_ovmilenin_2019]] [[Oblique Wing Aircraft 2020][research_oblique_wing_2020]] [[Obradovic and Subbarao 2010][research_obradovic_subbarao_2010]] [[Obradovic and Subbarao 2011][research_obradovic_subbarao_2011]] [[Oh et al 2017][research_oh_kim_2017]] [[Ohio State Univ Columbus Electroscience Lab 1968][research_ohiostateunivcolumbuselectrosciencelab_1968]] [[Okcu 2016][research_okcu_2016]] [[Olivares Méndez][research_olivaresmendez]] [[Oliver 1962][research_oliver_1962]] [[Olson 2005][research_olson_2005]] [[Olson and Henricks 2018][research_olson_henricks_2018]] [[Oncu and Yildiz 2014][research_oncu_yildiz_2014]] [[Ono 2024][research_ono_2024]] [[Optimal Control System of 2018][research_optimal_control_2018]] [[Oren and Kocyigit 2016][research_oren_kocyigit_2016]] [[Ortiz 2008][research_ortiz_2008]] [[Osadchiy et al 2013][research_osadchiy_kalich_2013]] [[Osiecki et al 2023][research_osiecki_fortonska_2023]] [[Overholt 2007][research_overholt_2007]] [[Overview of Unmanned Aircraft 2012][research_overview_of_2012]] [[Overview of Unmanned Aircraft 2014][research_overview_of_2014]] [[Owashi et al 2017][research_owashi_tanaka_2017]] [[Oyama 2021][research_oyama_2021]] [[Ozartan et al 2013][research_ozartan_akgul_2013]] [[Ozcan and Alemdaroglu 2015][research_ozcan_alemdaroglu_2015]] [[Ozoroski et al 2003][research_ozoroski_mas_2003]] [[Oztekin et al 2011][research_oztekin_flass_2011]] [[Pack and York 2008][research_pack_york_2008]] [[Pack et al][research_pack_york_b]] [[Paget et al 2004][research_paget_atherton_2004]] [[Palmer 1970][research_palmer_1970]] [[Palmisano and Gillam 2005][research_palmisano_gillam_2005]] [[Palomino and Epp 2012][research_palomino_epp_2012]] [[Pandey et al 2024][research_pandey_kumari_2024]] [[Pant and Fielding 1999][research_pant_fielding_1999]] [[Papageorgiou et al 2019][research_papageorgiou_dalkilic_2019]] [[Parasuraman and Miller 2006][research_parasuraman_miller_2006]] [[Parker 1980][research_parker_1980]] [[Parsons 1989][research_parsons_1989]] [[Parsons Engineering Sciences Inc Pasadena Ca 1991][research_parsonsengineeringsciencesincpasadenaca_1991]] [[Parts 1979][research_parts_1979]] [[Passenger SEAT Design Commercial][research_passenger_seat]] [[Passner et al 2012][research_passner_kirby_2012]] [[Pathak 1976][research_pathak_1976]] [[Paul][research_paul]] [[Paul et al 2013][research_paul_fendley_2013]] [[Pauls 2012][research_pauls_2012]] [[Paulsen 1998][research_paulsen_1998]] [[Payton 2011][research_payton_2011]] [[Pehlivan et al 2023][research_pehlivan_ozen_2023]] [[Pei et al 2025][research_pei_huang_2025]] [[Peixoto 2024][research_peixoto_2024]] [[Peng and Mohseni 2014][research_peng_mohseni_2014]] [[Pentz and Tang 2019][research_pentz_tang_2019]] [[Perkins 1991][research_perkins_1991]] [[Perry 2000][research_perry_2000]] [[Perry 2011][research_perry_2011]] [[Pervan and Parkinson 1997][research_pervan_parkinson_1997]] [[Peterson and Finkenstadt 2011][research_peterson_finkenstadt_2011]] [[Peterson and Staley 2011][research_peterson_staley_2011]] [[Petnga and Xu 2016][research_petnga_xu_2016]] [[Petrock and Huizenga 2006][research_petrock_huizenga_2006]] [[Pettigrew 2003][research_pettigrew_2003]] [[Pettit and Grandhi 2003][research_pettit_grandhi_2003]] [[Pham][research_pham_b]] [[Pham][research_pham_c]] [[Pham and Sim 2002][research_pham_sim_2002]] [[Phillips and Herr 2020][research_phillips_herr_2020]] [[Piersol 1977][research_piersol_1977]] [[Pierson 1985][research_pierson_1985]] [[Pilot Training Recommendations for][research_pilot_training]] [[Pilot Versatility From the][research_pilot_versatility]] [[Pilot Visibility from the][research_pilot_visibility]] [[Pilot Visibility from the][research_pilot_visibility_b]] [[Pisani 1977][research_pisani_1977]] [[Pittsburgh Univ Washington Dc Research Staff 1966][research_pittsburghunivwashingtondcresearchstaff_1966]] [[Pomranky 2006][research_pomranky_2006]] [[Pond 1973][research_pond_1973]] [[Poock 1976][research_poock_1976]] [[Portage Inc Idaho Falls Id 2013][research_portageincidahofallsid_2013]] [[Porter 1979][research_porter_1979]] [[Potes et al 2026][research_potes_retamal_2026]] [[Pottinger et al 2017][research_pottinger_cross_2017]] [[Pozzi et al 2012][research_pozzi_guo_2012]] [[Practice for Application of][research_practice_for_d]] [[Practice for Independent Audit][research_practice_for_b]] [[Practice for Production Approval][research_practice_for_c]] [[Pradeep 1998][research_pradeep_1998]] [[Pradeep and Wei 2018][research_pradeep_wei_2018]] [[Precision Approach Radar to 1979][research_precision_approach_1979]] [[Precision Landing of Aircraft 1996][research_precision_landing_1996]] [[Pressure Die Cast Aircraft][research_pressure_die]] [[Price and Forrest 2016][research_price_forrest_2016]] [[Primatesta et al 2018][research_primatesta_guglieri_2018]] [[Primatesta et al 2021][research_primatesta_pagliano_2021]] [[Pritpal 2005][research_pritpal_2005]] [[Prudhomme 1995][research_prudhomme_1995]] [[Purshouse 2003][research_purshouse_2003]] [[Purvis 2003][research_purvis_2003]] [[Putra et al 2018][research_putra_wiyagi_2018]] [[Putscher 1967][research_putscher_1967]] [[Pyzynski 2020][research_pyzynski_2020]] [[Qi and Wang 2016][research_qi_wang_2016]] [[Qiao et al 2008][research_qiao_bai_2008]] [[Qiwei et al 2014][research_qiwei_shumei_2014]] [[Quan et al 2021][research_quan_edmond_2021]] [[Ragi and Chong 2013][research_ragi_chong_2013]] [[Ragon et al 2003][research_ragon_gurdal_2003]] [[Ralles 1966][research_ralles_1966]] [[Ramasamy 2015][research_ramasamy_2015]] [[Ramasamy and Ghose 2016][research_ramasamy_ghose_2016]] [[Ramasamy et al 2015][research_ramasamy_gardi_2015]] [[Randolph 1997][research_randolph_1997]] [[Rasmussen 1992][research_rasmussen_1992]] [[Ravenstein 1984][research_ravenstein_1984]] [[Raychem gel material improves 1998][research_raychem_gel_1998]] [[Rayman 1979][research_rayman_1979]] [[Raymer 2012][research_raymer_2012]] [[Raymer 2012][research_raymer_2012_b]] [[Raymer 2018][research_raymer_2018]] [[Raymer 2024][research_raymer_2024]] [[Razzak and Damodaran 2022][research_razzak_damodaran_2022]] [[Read and Iii 1991][research_read_iii_1991]] [[Reardon et al 1999][research_reardon_katz_1999]] [[Recommended Practice for Measurement][research_recommended_practice]] [[Reed 2010][research_reed_2010]] [[Regan 1986][research_regan_1986]] [[Reid 1969][research_reid_1969]] [[Reinbold 1954][research_reinbold_1954]] [[Reinhardt and Johansen 2021][research_reinhardt_johansen_2021]] [[Reinhart 1975][research_reinhart_1975]] [[Reitan and Saib 1976][research_reitan_saib_1976]] [[Ren and Stephens 2006][research_ren_stephens_2006]] [[Ren et al 2025][research_ren_wang_2025]] [[Reorganization for the Era 2008][research_reorganization_for_2008]] [[Requirements Analysis, Partitioning, Implementation 2013][research_requirements_analysis_2013]] [[Resulkulyeva and Serebryansky 2022][research_resulkulyeva_serebryansky_2022]] [[Rhudy et al 2019][research_rhudy_gross_2019]] [[Ribarich 1967][research_ribarich_1967]] [[Riboldi 2019][research_riboldi_2019]] [[Riedel 1979][research_riedel_1979]] [[Rife 1993][research_rife_1993]] [[Rios Quesada and Charpentier][research_riosquesada_charpentier]] [[Ritchey 2008][research_ritchey_2008]] [[Ritter][research_ritter]] [[RlDHA 1969][research_rldha_1969]] [[Roadman et al 2012][research_roadman_elston_2012]] [[Roberts and Sutton 2006][research_roberts_sutton_2006]] [[Rocha et al 2006][research_rocha_li_2006]] [[Rodden 1972][research_rodden_1972]] [[Rogers 2009][research_rogers_2009]] [[Rohl and Schrage 1992][research_rohl_schrage_1992]] [[Rollo et al 2024][research_rollo_volf_2024]] [[Rolls-Royce and British Aerospace 1999][research_rolls_royce_and_1999]] [[Romero 2015][research_romero_2015]] [[Rose et al 2022][research_rose_ghoreyshi_2022]] [[Rosenman and Hoekstra 1964][research_rosenman_hoekstra_1964]] [[Rosenthal 1970][research_rosenthal_1970]] [[Rosenthal and Walsh 1996][research_rosenthal_walsh_1996]] [[Roskam 1986][research_roskam_1986]] [[Roskam 1988][research_roskam_1988]] [[Rothwell 2001][research_rothwell_2001]] [[Rotorcraft Application of Existing][research_rotorcraft_application]] [[Rovig et al 2004][research_rovig_bohnker_2004]] [[Roy et al 2006][research_roy_levy_2006]] [[Rudy 2013][research_rudy_2013]] [[Ryan 1990][research_ryan_1990]] [[Ryan and Cummings 2016][research_ryan_cummings_2016]] [[Răducanu and Cîrciu 2017][research_raducanu_circiu_2017]] [[Sabatini et al 2015][research_sabatini_cappello_2015]] [[Sacharny and Henderson 2022][research_sacharny_henderson_2022]] [[Sacharny and Henderson 2022][research_sacharny_henderson_2022_b]] [[Sachse 1998][research_sachse_1998]] [[Sadasivan et al 2001][research_sadasivan_gurubasavaraj_2001]] [[Sadraey 2010][research_sadraey_2010]] [[Saeedipour and Neil Stevenson 1998][research_saeedipour_neilstevenson_1998]] [[Saelman 1964][research_saelman_1964]] [[Safety Considerations - Flight][research_safety_considerations]] [[Safi 2023][research_safi_2023]] [[Saif et al 2014][research_saif_fantoni_2014]] [[Sakamaki et al 2017][research_sakamaki_beard_2017]] [[Samuels 1982][research_samuels_1982]] [[Sancho 2002][research_sancho_2002]] [[Sanders 1957][research_sanders_1957]] [[Sanghi et al 2024][research_sanghi_cesnik_2024]] [[Santamaría Barnadas][research_santamariabarnadas]] [[Sarigul-Klijn et al 2008][research_sarigulklijn_sarigulklijn_2008]] [[Sastry 2001][research_sastry_2001]] [[Savić 2024][research_savic_2024]] [[Savuran and Karakaya 2015][research_savuran_karakaya_2015]] [[Savuran and Karakaya 2015][research_savuran_karakaya_2015_b]] [[Scafetta 1983][research_scafetta_1983]] [[Scarpa 2001][research_scarpa_2001]] [[Schairer 1946][research_schairer_1946]] [[Schalk 2017][research_schalk_2017]] [[Schleicher 1966][research_schleicher_1966]] [[Schmidt 1983][research_schmidt_1983]] [[Schmidt 1984][research_schmidt_1984]] [[Schmidt 1985][research_schmidt_1985]] [[Schmidt et al 2006][research_schmidt_stevens_2006]] [[Schoenbeck and Schultz 1999][research_schoenbeck_schultz_1999]] [[Schoenbein 2009][research_schoenbein_2009]] [[Schopferer and Pfeifer 2015][research_schopferer_pfeifer_2015]] [[Schrage and McKeithan 1989][research_schrage_mckeithan_1989]] [[Schutz and Kutrzyba 2000][research_schutz_kutrzyba_2000]] [[Schwartz 1988][research_schwartz_1988]] [[Scott and Hartmann 2024][research_scott_hartmann_2024]] [[Scott and Trimarchi 2024][research_scott_trimarchi_2024]] [[Scribner 1998][research_scribner_1998]] [[Seah and Hwang 2006][research_seah_hwang_2006]] [[Seah and Hwang 2007][research_seah_hwang_2007]] [[Seah and Hwang 2009][research_seah_hwang_2009]] [[Sease et al 2023][research_sease_warwick_2023]] [[Seaton 1989][research_seaton_1989]] [[Seats for Flight DECK][research_seats_for]] [[Seats for Flight Deck][research_seats_for_b]] [[Section 7 International Civil 2016][research_section_7_2016]] [[Seiferth et al 2017][research_seiferth_kuchar_2017]] [[Semakov and Semakov 2020][research_semakov_semakov_2020]] [[Semke 2016][research_semke_2016]] [[Semke 2021][research_semke_2021]] [[Seraj and Martins 2022][research_seraj_martins_2022]] [[Sevcik and Oh][research_sevcik_oh]] [[Sgarioto et al 2006][research_sgarioto_williams_2006]] [[Shao et al 2024][research_shao_guo_2024]] [[Sharma et al 2009][research_sharma_saunders_2009]] [[Shay et al 2012][research_shay_swieringa_2012]] [[Shen and Rahman 2011][research_shen_rahman_2011]] [[Shen et al 2026][research_shen_zhang_2026]] [[Sher 1981][research_sher_1981]] [[Sherstjuk 2015][research_sherstjuk_2015]] [[Shi 2023][research_shi_2023]] [[Shi and Ng 2018][research_shi_ng_2018]] [[Shiyan et al 2016][research_shiyan_huimin_2016]] [[Shock mounts for aircraft 1993][research_shock_mounts_1993]] [[Shujun et al 2014][research_shujun_jianyun_2014]] [[Shustrov 1998][research_shustrov_1998]] [[Si et al 2024][research_si_song_2024]] [[Sibruk et al 2015][research_sibruk_bondarenko_2015]] [[Siddarth and Valasek 2011][research_siddarth_valasek_2011]] [[Siegel 1995][research_siegel_1995]] [[Siegel and Lanterman 1963][research_siegel_lanterman_1963]] [[Sim et al 1994][research_sim_murray_1994]] [[Simmons 1993][research_simmons_1993]] [[Simms 2023][research_simms_2023]] [[Simoncic 2013][research_simoncic_2013]] [[Singer 2011][research_singer_2011]] [[Singh et al 2016][research_singh_toropov_2016]] [[Sivakumar et al 2021][research_sivakumar_man_2021]] [[Sivakumar et al 2022][research_sivakumar_hasrizamcheman_2022]] [[Slapnicar][research_slapnicar]] [[Smith 2000][research_smith_2000]] [[Smith and Meyer 1981][research_smith_meyer_1981]] [[Snyder 1950][research_snyder_1950]] [[Snyder 2000][research_snyder_2000]] [[Snyder et al 2009][research_snyder_sanders_2009]] [[Soban 1993][research_soban_1993]] [[Solvey 1951][research_solvey_1951]] [[Song 2008][research_song_2008]] [[Soop 1994][research_soop_1994]] [[Soop 1994][research_soop_1994_b]] [[Sosa 1997][research_sosa_1997]] [[Souanef 2024][research_souanef_2024]] [[Soumekh][research_soumekh]] [[Speakman et al 1978][research_speakman_powell_1978]] [[Special Topics in Unmanned 2014][research_special_topics_2014]] [[Specification for Aircraft Flight][research_specification_for_c]] [[Specification for aircraft pressure][research_specification_for_e]] [[Specification for Design and][research_specification_for]] [[Specification for Design of][research_specification_for_f]] [[Specification for Small Unmanned][research_specification_for_d]] [[Specification for Unmanned Aircraft][research_specification_for_b]] [[Spiridon and Fuiorea 2025][research_spiridon_fuiorea_2025]] [[Spreen 2019][research_spreen_2019]] [[Spreen 2019][research_spreen_2019_b]] [[Spreen 2019][research_spreen_2019_c]] [[Spreen 2019][research_spreen_2019_d]] [[Spreen 2019][research_spreen_2019_f]] [[Spreen 2019][research_spreen_2019_g]] [[Spreen 2019][research_spreen_2019_h]] [[Spreen 2019][research_spreen_2019_i]] [[Spreen 2019][research_spreen_2019_j]] [[Spreen 2019][research_spreen_2019_k]] [[Spreen 2019][research_spreen_2019_l]] [[Spreen 2019][research_spreen_2019_m]] [[Spreen 2019][research_spreen_2019_n]] [[Spreen 2023][research_spreen_2023]] [[Spry et al][research_spry_girard]] [[Squire et al 2006][research_squire_trafton_2006]] [[Standard Guide for Wing][research_standard_guide]] [[Standard Specification for Small][research_standard_specification_c]] [[Standard Terminology for Unmanned][research_standard_terminology]] [[Stanford et al 2012][research_stanford_kurdi_2012]] [[Stark and Chen 2014][research_stark_chen_2014]] [[Stastny and Stoica 2021][research_stastny_stoica_2021]] [[Station Keeping 2008][research_station_keeping_2008]] [[Station Keeping Of Satellites 1962][research_station_keeping_1962]] [[Station Keeping System 2022][research_station_keeping_2022]] [[Stedman 1992][research_stedman_1992]] [[Steeb et al 1979][research_steeb_chu_1979]] [[Stephan et al 2020][research_stephan_pfeifle_2020]] [[Stewart et al 2012][research_stewart_roberts_2012]] [[Stieger 1929][research_stieger_1929]] [[Stone][research_stone]] [[Storage, Handling, and Shipping][research_storage_handling]] [[Strawser 2013][research_strawser_2013]] [[Strganac 2007][research_strganac_2007]] [[Striebich 1986][research_striebich_1986]] [[Strock 1983][research_strock_1983]] [[Structural dynamics centre for 1999][research_structural_dynamics_1999]] [[Strukov_ 2025][research_strukov_2025]] [[Su et al 2018][research_su_han_2018]] [[Su et al 2018][research_su_han_2018_b]] [[Su et al 2018][research_su_li_2018]] [[Su et al 2018][research_su_wu_2018]] [[Su et al 2019][research_su_li_2019]] [[Subbarao et al 2001][research_subbarao_steinberg_2001]] [[Subramani et al 2021][research_subramani_m_2021]] [[Subramaniam et al 2012][research_subramaniam_joseph_2012]] [[Sui 2022][research_sui_2022]] [[Suima 2025][research_suima_2025]] [[Sullivan 1991][research_sullivan_1991]] [[Sullivan 1991][research_sullivan_1991_b]] [[Sullivan 1991][research_sullivan_1991_c]] [[Sullivan 1997][research_sullivan_1997]] [[Summey et al 2001][research_summey_rodriguez_2001]] [[Sun 2023][research_sun_2023]] [[Sun and Gebre-Egziabher 2021][research_sun_gebreegziabher_2021]] [[Sun and Pack 2016][research_sun_pack_2016]] [[Sun et al 2025][research_sun_guo_2025]] [[Sun et al 2025][research_sun_liu_2025]] [[Supplementary Bibliography for Aircraft 1990][research_supplementary_bibliography_1990]] [[Suresh et al 2019][research_suresh_sura_2019]] [[Surgeoner 1999][research_surgeoner_1999]] [[Suzuki and Yonezawa 1993][research_suzuki_yonezawa_1993]] [[Svoboda 1999][research_svoboda_1999]] [[Swaim 1969][research_swaim_1969]] [[Swett and Blanche][research_swett_blanche]] [[Swisdak and Michael M. 1992][research_swisdak_michaelm_1992]] [[Sychev 2017][research_sychev_2017]] [[Synthetic vision and precision 1994][research_synthetic_vision_1994]] [[Szabolcsi 2018][research_szabolcsi_2018]] [[Szabolcsi 2018][research_szabolcsi_2018_b]] [[Szabolcsi 2018][research_szabolcsi_2018_c]] [[Tactical Air Command Langley Afb Va 1989][research_tacticalaircommandlangleyafbva_1989]] [[Tafanidis et al 2025][research_tafanidis_banerjee_2025]] [[Takita and Kashitani 2016][research_takita_kashitani_2016]] [[Takita and Kashitani 2017][research_takita_kashitani_2017]] [[Tam 2015][research_tam_2015]] [[Tang][research_tang]] [[Tang and Dowell 2008][research_tang_dowell_2008]] [[Tang et al 2024][research_tang_zeng_2024]] [[Tang, Adrian J. 2013][research_tangadrianj_2013]] [[Tate 2001][research_tate_2001]] [[Taylor 1999][research_taylor_1999]] [[Taylor et al 2021][research_taylor_boubin_2021]] [[Technical requirements for small][research_technical_requirements]] [[Tekinalp and Prach 2013][research_tekinalp_prach_2013]] [[Tekinalp and Prach 2014][research_tekinalp_prach_2014]] [[Templalexis et al 2016][research_templalexis_lekas_2016]] [[Terminology for Unmanned Aircraft][research_terminology_for]] [[Terry 1965][research_terry_1965]] [[Test methods for civil][research_test_methods]] [[Thakur and Kumar 2021][research_thakur_kumar_2021]] [[The Control of Multiple 2026][research_the_control_2026]] [[The Design of Classical 2012][research_the_design_2012]] [[The Future of Unmanned 2016][research_the_future_2016]] [[The Kinematics and Dynamics 2015][research_the_kinematics_2015]] [[The Process of Lubricating][research_the_process]] [[The Red Wing Church][research_the_red]] [[The Wing Structure and 2013][research_the_wing_2013]] [[Theiss 2007][research_theiss_2007]] [[Thelander 1965][research_thelander_1965]] [[Thomas 1961][research_thomas_1961]] [[Thome and Jr. 2003][research_thome_jr_2003]] [[Thompson 1965][research_thompson_1965]] [[Thompson and Robertson 1990][research_thompson_robertson_1990]] [[Thorne and Yim 2011][research_thorne_yim_2011]] [[Thys et al 2025][research_thys_macabiau_2025]] [[Tian and Zhao 2012][research_tian_zhao_2012]] [[Tianjian et al 2014][research_tianjian_xin_2014]] [[Tielking 1989][research_tielking_1989]] [[Tiimus et al 2015][research_tiimus_murumae_2015]] [[Tire Pressure Monitoring Systems][research_tire_pressure]] [[Tokarick 2005][research_tokarick_2005]] [[Tolfa and Edward 1971][research_tolfa_edward_1971]] [[Tomczyk and Rogalski 2005][research_tomczyk_rogalski_2005]] [[Tonhauser and Hecker 2016][research_tonhauser_hecker_2016]] [[Torenbeek 1972][research_torenbeek_1972]] [[Torenbeek 2000][research_torenbeek_2000]] [[Torenbeek 2013][research_torenbeek_2013]] [[Torvold 2000][research_torvold_2000]] [[Tosun 2023][research_tosun_2023]] [[Tran][research_tran]] [[Tran et al 2020][research_tran_thiriet_2020]] [[Trimarchi 2023][research_trimarchi_2023]] [[Trinen and Pieri 2026][research_trinen_pieri_2026]] [[Troop Carrier Aviation in][research_troop_carrier]] [[Troop Carrier Aviation in][research_troop_carrier_b]] [[Truxal and Scott 2024][research_truxal_scott_2024]] [[Tsybriy and Guskov 2025][research_tsybriy_guskov_2025]] [[Tucker and Iii 1993][research_tucker_iii_1993]] [[Tuzlukov 2026][research_tuzlukov_2026]] [[Tvaryanas 2006][research_tvaryanas_2006]] [[Tvaryanas 2006][research_tvaryanas_2006_b]] [[Tvaryanas et al 2012][research_tvaryanas_singer_2012]] [[Tweddale et al 2011][research_tweddale_fichtl_2011]] [[UAV control with active 2023][research_uav_control_2023]] [[UK aircraft carrier projecting 2014][research_uk_aircraft_2014]] [[Ulybyshev 2015][research_ulybyshev_2015]] [[Universal Balancing supports up 2007][research_universal_balancing_2007]] [[Unmanned Aerial Vehicle Design 2024][research_unmanned_aerial_2024]] [[Unmanned Aerial Vehicles 2013][research_unmanned_aerial_2013]] [[Unmanned Aerial Vehicles 2016][research_unmanned_aerial_2016]] [[Unmanned Aerial Vehicles 2020][research_unmanned_aerial_2020]] [[Unmanned Air Vehicles 2017][research_unmanned_air_2017]] [[Unmanned Aircraft Categories 2012][research_unmanned_aircraft_2012]] [[Unmanned Aircraft Categories 2014][research_unmanned_aircraft_2014]] [[Unmanned Aircraft Geometry and 2014][research_unmanned_aircraft_2014_b]] [[Unmanned Aircraft System Elements 2016][research_unmanned_aircraft_2016]] [[Unmanned Aircraft System Operations 2016][research_unmanned_aircraft_2016_b]] [[Unmanned aircraft systems][research_unmanned_aircraft]] [[Unmanned Aircraft Systems 2009][research_unmanned_aircraft_2009]] [[Unmanned Aircraft Systems for 2016][research_unmanned_aircraft_2016_c]] [[Unmanned Aircraft Systems Regulation][research_unmanned_aircraft_b]] [[Unmanned aircraft systems UAS][research_unmanned_aircraft_c]] [[Unmanned aircraft systems. Training][research_unmanned_aircraft_d]] [[Unmanned-Aircraft Geometry and Configurations 2012][research_unmanned_aircraft_geometry_2012]] [[ur Rehman 2018][research_urrehman_2018]] [[Useful Aircraft Design Data][research_useful_aircraft]] [[Useful aircraft design data 1999][research_useful_aircraft_1999]] [[Utsch and Rockwell 1990][research_utsch_rockwell_1990]] [[Uzzell 1997][research_uzzell_1997]] [[Vachtsevanos and Valavanis 2014][research_vachtsevanos_valavanis_2014]] [[Vahidi and Saberinia 2016][research_vahidi_saberinia_2016]] [[Valavanis and Vachtsevanos 2014][research_valavanis_vachtsevanos_2014]] [[Valavanis et al][research_valavanis_oh]] [[Vale and Albuquerque 2025][research_vale_albuquerque_2025]] [[Vali 2004][research_vali_2004]] [[Validation and Verification Process][research_validation_and]] [[Vance 1984][research_vance_1984]] [[Variable sweep wing design 1980][research_variable_sweep_1980]] [[Vashishth et al 2024][research_vashishth_sharma_2024]] [[Venkatesh 2023][research_venkatesh_2023]] [[Vepa 2016][research_vepa_2016]] [[Vepa 2020][research_vepa_2020]] [[Vepa 2023][research_vepa_2023]] [[Vepa 2023][research_vepa_2023_b]] [[Vick and Carter 1963][research_vick_carter_1963]] [[Vicory 1968][research_vicory_1968]] [[Video Communications in Unmanned 2013][research_video_communications_2013]] [[Vidimlic et al 2021][research_vidimlic_levin_2021]] [[Vishniak 1993][research_vishniak_1993]] [[Vlasov 1969][research_vlasov_1969]] [[Vos et al 2010][research_vos_gurdal_2010]] [[Vulnerability of Quick-Reacting Sheltered 1959][research_vulnerability_of_1959]] [[Wade 2002][research_wade_2002]] [[Wadley et al 2003][research_wadley_tallant_2003]] [[Wagdi 1984][research_wagdi_1984]] [[Walker 1960][research_walker_1960]] [[Walker 1961][research_walker_1961]] [[Walker 2015][research_walker_2015]] [[Walker 2024][research_walker_2024]] [[Wallace 2000][research_wallace_2000]] [[Walton 1992][research_walton_1992]] [[Wang 2026][research_wang_2026_b]] [[Wang and Hubbard 2022][research_wang_hubbard_2022]] [[Wang and McDonald 2019][research_wang_mcdonald_2019]] [[Wang and Zhao 2022][research_wang_zhao_2022]] [[Wang et al 2009][research_wang_song_2009]] [[Wang et al 2011][research_wang_sun_2011]] [[Wang et al 2016][research_wang_feng_2016]] [[Wang et al 2016][research_wang_liu_2016]] [[Wang et al 2016][research_wang_zhu_2016]] [[Wang et al 2020][research_wang_liu_2020]] [[Wang et al 2020][research_wang_xuan_2020]] [[Wang et al 2021][research_wang_chen_2021]] [[Wang et al 2022][research_wang_mkhoyan_2022]] [[Wang et al 2024][research_wang_li_2024]] [[Ward 1983][research_ward_1983]] [[Warner 1970][research_warner_1970]] [[Warren and Richards 2009][research_warren_richards_2009]] [[Wasser et al 2011][research_wasser_boddhu_2011]] [[Wasserman and Mitchell 1973][research_wasserman_mitchell_1973]] [[Watanabe 2020][research_watanabe_2020]] [[Waterman and Miller 2000][research_waterman_miller_2000]] [[Watson et al 2020][research_watson_owen_2020]] [[Watson et al 2025][research_watson_owen_2025]] [[Wauters 2022][research_wauters_2022]] [[Weaponised Unmanned Air Systems 2013][research_weaponised_unmanned_2013]] [[Web site urges students 2008][research_web_site_2008]] [[Webb 2022][research_webb_2022]] [[Webster 1971][research_webster_1971]] [[Weeks 2000][research_weeks_2000]] [[Wei 2013][research_wei_2013]] [[Wei et al 2026][research_wei_tong_2026]] [[Wei et al 2026][research_wei_zhai_2026]] [[Weinberg 1966][research_weinberg_1966]] [[Weinert et al 1991][research_weinert_richardp_1991]] [[Weingarten 1977][research_weingarten_1977]] [[Weisshaar 1990][research_weisshaar_1990]] [[Weisshaar 1994][research_weisshaar_1994]] [[Welbourn and Lachance 1961][research_welbourn_lachance_1961]] [[Wells 1993][research_wells_1993]] [[West 2009][research_west_2009]] [[Westat Inc Rockville Md 2001][research_westatincrockvillemd_2001]] [[White][research_white]] [[White 1992][research_white_1992]] [[White 2005][research_white_2005]] [[White 2012][research_white_2012]] [[Whitford 1990][research_whitford_1990]] [[Whitford 1992][research_whitford_1992]] [[Whitford 1993][research_whitford_1993]] [[Whitford 1994][research_whitford_1994]] [[Why Should We Design][research_why_should]] [[Why should we design 1999][research_why_should_1999]] [[Wick][research_wick]] [[Wide-Body and Standard-Body Aircraft][research_wide_body_and]] [[Wieland et al 2013][research_wieland_sharma_2013]] [[Wilcox et al 2010][research_wilcox_mackunis_2010]] [[Wilhem 1970][research_wilhem_1970]] [[Williams and Trivailo 2006][research_williams_trivailo_2006]] [[Williams and Trivailo 2006][research_williams_trivailo_2006_b]] [[Williamson 1966][research_williamson_1966]] [[Willis][research_willis]] [[Wilsbach 1998][research_wilsbach_1998]] [[Wilson, S. B., III 1992][research_wilsonsbiii_1992]] [[Wing Design 2012][research_wing_design_2012]] [[Wings 2017][research_wings_2017]] [[Wise 1990][research_wise_1990]] [[Wise 2004][research_wise_2004]] [[Wiser 2009][research_wiser_2009]] [[Wittenberg 2001][research_wittenberg_2001]] [[Woelk 1989][research_woelk_1989]] [[Wolf et al 2016][research_wolf_shelley_2016]] [[Wolff 2022][research_wolff_2022]] [[Wolff et al 1988][research_wolff_lohr_1988]] [[Woods 1994][research_woods_1994]] [[Worked Manned Aircraft Detail 2017][research_worked_manned_2017]] [[Wortman 1981][research_wortman_1981]] [[Wortmann et al 2015][research_wortmann_hoogreef_2015]] [[Wright and Barry 2014][research_wright_barry_2014]] [[Wright and Burton 1991][research_wright_burton_1991]] [[Wu and Lin 2026][research_wu_lin_2026]] [[Wu and Mora-Camino 2012][research_wu_moracamino_2012]] [[Wu and Mueller 2018][research_wu_mueller_2018]] [[Wu et al 2023][research_wu_lv_2023]] [[Wu et al 2024][research_wu_wang_2024]] [[Wu et al 2026][research_wu_wang_2026]] [[Wynnyk et al 2017][research_wynnyk_lunsford_2017]] [[Xi and Liu 2020][research_xi_liu_2020]] [[Xia et al 2016][research_xia_dong_2016]] [[Xiao 2008][research_xiao_2008]] [[Xie and Haberland 1999][research_xie_haberland_1999]] [[Xie et al 2026][research_xie_jia_2026]] [[Xie et al 2026][research_xie_jia_2026_b]] [[Xie et al 2026][research_xie_jia_2026_c]] [[Xie et al 2026][research_xie_jia_2026_d]] [[Xie et al 2026][research_xie_jia_2026_e]] [[Xie et al 2026][research_xie_jia_2026_f]] [[Xie et al 2026][research_xie_jia_2026_g]] [[Xu and Carrillo 2015][research_xu_carrillo_2015]] [[Xu et al 2018][research_xu_zhang_2018]] [[Xu et al 2019][research_xu_han_2019]] [[Xu et al 2020][research_xu_huang_2020]] [[Xu et al 2021][research_xu_liu_2021]] [[Xue and Atkins 2003][research_xue_atkins_2003]] [[Xue and Do 2019][research_xue_do_2019]] [[Xue et al 2011][research_xue_zhao_2011]] [[Yacef et al 2014][research_yacef_bouhali_2014]] [[Yadav and Shukla 2012][research_yadav_shukla_2012]] [[Yan et al 2025][research_yan_zhang_2025]] [[Yang 2013][research_yang_2013]] [[Yang et al 2026][research_yang_shou_2026]] [[Yang et al 2026][research_yang_song_2026]] [[Yanushevsky 2026][research_yanushevsky_2026]] [[Yanushevsky 2026][research_yanushevsky_2026_b]] [[Yanushevsky 2026][research_yanushevsky_2026_c]] [[Yao et al 2018][research_yao_wang_2018]] [[Yardley et al 2008][research_yardley_kallimani_2008]] [[Yarygina and Popov 2012][research_yarygina_popov_2012]] [[Yasuda 2025][research_yasuda_2025]] [[Yerger 2006][research_yerger_2006]] [[Yilmaz et al 2019][research_yilmaz_warren_2019]] [[Yoakum and Cerreta 2020][research_yoakum_cerreta_2020]] [[Yogeshwaran][research_yogeshwaran]] [[Yong Jiang et al 2006][research_yongjiang_jiecao_2006]] [[York and Pack 2011][research_york_pack_2011]] [[Young 1997][research_young_1997]] [[Young 2000][research_young_2000]] [[Yu and Chen 2011][research_yu_chen_2011]] [[Yu and Du 2006][research_yu_du_2006]] [[Yu and Liu 2019][research_yu_liu_2019]] [[Yu et al 2017][research_yu_hua_2017]] [[Yu et al 2018][research_yu_qu_2018]] [[Yuan et al 2014][research_yuan_xing_2014]] [[Yuma Proving Ground Az 2013][research_yumaprovinggroundaz_2013]] [[Yuma Test Center Yuma Proving Ground Az 2008][research_yumatestcenteryumaprovinggroundaz_2008]] [[Zadniprovsky and Konotop 2025][research_zadniprovsky_konotop_2025]] [[Zappa and Gordon 2011][research_zappa_gordon_2011]] [[Załęski 2018][research_zaeski_2018]] [[Zehner 2001][research_zehner_2001]] [[Zelenkov and Golik 2014][research_zelenkov_golik_2014]] [[Zhai et al 2025][research_zhai_li_2025]] [[Zhang and Qin 2026][research_zhang_qin_2026]] [[Zhang and Wang 2023][research_zhang_wang_2023_c]] [[Zhang and Zhang 2020][research_zhang_zhang_2020]] [[Zhang and Zhang 2022][research_zhang_zhang_2022]] [[Zhang and Zhu 2025][research_zhang_zhu_2025]] [[Zhang et al 2016][research_zhang_zhao_2016]] [[Zhang et al 2020][research_zhang_li_2020]] [[Zhang et al 2020][research_zhang_zhang_2020_b]] [[Zhang et al 2021][research_zhang_su_2021]] [[Zhang et al 2021][research_zhang_wang_2021]] [[Zhang et al 2022][research_zhang_zhang_2022_b]] [[Zhang et al 2023][research_zhang_chen_2023]] [[zhang et al 2023][research_zhang_lin_2023]] [[Zhao et al 2023][research_zhao_liu_2023]] [[Zheng et al 2014][research_zheng_qiaoqiao_2014]] [[Zheng et al 2026][research_zheng_qu_2026]] [[Zhiqiang and Wu 2017][research_zhiqiang_wu_2017]] [[Zhou 2016][research_zhou_2016]] [[Zhou et al 2017][research_zhou_jiang_2017]] [[Zhou et al 2018][research_zhou_zeng_2018]] [[Zhou et al 2019][research_zhou_huang_2019]] [[Zhou et al 2022][research_zhou_wang_2022]] [[Zhou et al 2022][research_zhou_zhang_2022]] [[Zhu et al 2020][research_zhu_lung_2020]] [[Zhu et al 2023][research_zhu_shi_2023]] [[Zhu et al 2026][research_zhu_zhu_2026]] [[Zink][research_zink]] [[Zou and Devasia 2000][research_zou_devasia_2000]] [[Zou and Devasia 2006][research_zou_devasia_2006]] [[Zou et al 2017][research_zou_yin_2017]] [[Zou et al 2020][research_zou_song_2020]] [[Zvyagina and Mordovin 2026][research_zvyagina_mordovin_2026]] [[Çakıcı and Leblebicioğlu 2016][research_cakici_leblebicioglu_2016]] [[Çoban and Oktay 2018][research_coban_oktay_2018]] [[Çoban and Oktay 2018][research_coban_oktay_2018_b]]

### Relative navigation, precision approach and the automatic landing

**This is the cluster this article's keystone lives in and it is a satellite-navigation subject before it is an aeronautical one.** The deck moves, so the aeroplane's position must be known with respect to the ship rather than to the earth. Differential and carrier-phase positioning, integer ambiguity resolution, ship-relative GPS, the joint precision approach and landing system, inertial navigation and sensor fusion, the automatic carrier landing system, glide slope tracking and touchdown dispersion.

**840 records.** [[Abbasi and Haeri 2019][research_abbasi_haeri_2019]] [[Abdel-Hafez et al 2003][research_abdelhafez_lee_2003]] [[Abdel-Hafez et al 2004][research_abdelhafez_speyer_2004]] [[Acuna et al 2018][research_acuna_zhang_2018]] [[Aftatah and Zebbara 2024][research_aftatah_zebbara_2024]] [[Aftatah et al 2026][research_aftatah_khalil_2026]] [[Agarwal et al 2008][research_agarwal_arya_2008]] [[Agrawal et al 2025][research_agrawal_rai_2025]] [[Aircraft Automatic Approach and 1996][research_aircraft_automatic_1996]] [[Akagi and McLain 2025][research_akagi_mclain_2025]] [[Akagi et al 2020][research_akagi_christensen_2020]] [[Akca and Demirekler 2012][research_akca_demirekler_2012]] [[Alaeiyan and Mosavi 2026][research_alaeiyan_mosavi_2026]] [[Alarcon et al 2015][research_alarcon_santamaria_2015]] [[Alhosban 2019][research_alhosban_2019]] [[Ali and Jiancheng 2005][research_ali_jiancheng_2005]] [[Allende-Alba et al 2018][research_allendealba_montenbruck_2018]] [[Almagbile et al 2010][research_almagbile_wang_2010]] [[Amiri-Simkooei et al 2015][research_amirisimkooei_jazaeri_2015]] [[Amzajerdian et al 2026][research_amzajerdian_gragossian_2026]] [[An et al 2019][research_an_meng_2019]] [[Andersen et al 1993][research_andersen_hauge_1993]] [[Antonini 1993][research_antonini_1993]] [[Anwendungsbeispiel GPS/INS-Integration 2007][research_anwendungsbeispiel_gps_ins_integration_2007]] [[Anwendungsbeispiel GPS/INS-Integration 2011][research_anwendungsbeispiel_gps_ins_integration_2011]] [[Anđić 2021][research_andic_2021]] [[Appendix D Comparison of 2004][research_appendix_d_2004]] [[Application of quasi-object control 2008][research_application_of_quasi_object_2008]] [[Arai 2000][research_arai_2000]] [[Ardaens et al 2013][research_ardaens_damico_2013]] [[Ascher et al 2011][research_ascher_zwirello_2011]] [[Ashraf et al 2019][research_ashraf_naqvi_2019]] [[Azimi-Sadjadi and Krishnaprasad 2001][research_azimisadjadi_krishnaprasad_2001]] [[Bai and Taylor 2020][research_bai_taylor_2020]] [[Balard et al 2005][research_balard_santerre_2005]] [[Bao et al 2017][research_bao_lai_2017]] [[Baselga et al 2009][research_baselga_garciaasenjo_2009]] [[Basil et al 2004][research_basil_anathasayanam_2004]] [[Bautista et al 2023][research_bautista_gutierrez_2023]] [[Belabbas][research_belabbas]] [[Belfadel et al 2023][research_belfadel_haessig_2023]] [[Belfadel et al 2024][research_belfadel_haessig_2024]] [[Ben-Ishai et al 2001][research_benishai_reiner_2001]] [[Benitez et al 2023][research_benitez_rutherford_2023]] [[Benzerrouk et al 2020][research_benzerrouk_landry_2020]] [[Berger et al 2026][research_berger_bonzatto_2026]] [[Bergeron et al 2011][research_bergeron_tavan_2011]] [[Beser 1978][research_beser_1978]] [[Beser 1979][research_beser_1979]] [[Bever et al 2002][research_bever_urschel_2002]] [[Bhamidipati and Gao 2020][research_bhamidipati_gao_2020]] [[Bhandari and O'Keefe 2017][research_bhandari_okeefe_2017]] [[Bhattacharyya 2016][research_bhattacharyya_2016]] [[Bhattacharyya 2023][research_bhattacharyya_2023]] [[Bhattacharyya 2025][research_bhattacharyya_2025]] [[Bhattacharyya and Mute 2020][research_bhattacharyya_mute_2020]] [[Bhattacharyya et al 2019][research_bhattacharyya_mute_2019]] [[Bian et al 2022][research_bian_nener_2022]] [[Binjammaz et al 2013][research_binjammaz_albayatti_2013]] [[Bletsos 1986][research_bletsos_1986]] [[Blewitt 2008][research_blewitt_2008]] [[Bloch 1989][research_bloch_1989]] [[Bolla and Won 2018][research_bolla_won_2018]] [[Bona 2000][research_bona_2000]] [[Braasch 2006][research_braasch_2006]] [[Brack 2014][research_brack_2014]] [[Brack 2016][research_brack_2016]] [[Brack 2017][research_brack_2017]] [[Brack 2020][research_brack_2020]] [[Braff 2008][research_braff_2008]] [[Braff and Loh 1992][research_braff_loh_1992]] [[Braff et al 2012][research_braff_bian_2012]] [[Brown and Hwang 1983][research_brown_hwang_1983]] [[Brown and Lu 2006][research_brown_lu_2006]] [[Brown et al 2000][research_brown_silva_2000]] [[Bruckner et al 2010][research_bruckner_vangraas_2010]] [[Bruton et al 1999][research_bruton_glennie_1999]] [[Cacopardi et al 1990][research_cacopardi_caporicci_1990]] [[Cai et al 2009][research_cai_grafarend_2009]] [[Calhoun and Raquet 2016][research_calhoun_raquet_2016]] [[Candan et al 2024][research_candan_sanci_2024]] [[Capderou 2012][research_capderou_2012]] [[Caporicci and Soddu][research_caporicci_soddu]] [[Carrier phase differential GPS/INS 1999][research_carrier_phase_1999]] [[Carroll][research_carroll]] [[Casey][research_casey]] [[Castaldo et al 2014][research_castaldo_angrisano_2014]] [[Catalán et al 2025][research_catalan_iglesias_2025]] [[Causa and Fasano 2025][research_causa_fasano_2025]] [[Cellmer et al 2010][research_cellmer_wielgosz_2010]] [[Chakravarty and Chichka 2006][research_chakravarty_chichka_2006]] [[Chang 2013][research_chang_2013]] [[Chang et al 2021][research_chang_wang_2021]] [[Chansarkar 2000][research_chansarkar_2000]] [[Chansik Park and Ilsun Kim][research_chansikpark_ilsunkim]] [[Chansik Park and Ilsun Kim 2000][research_chansikpark_ilsunkim_2000]] [[Chapteer 8. GPS Modernization 2008][research_chapteer_8_2008]] [[Chelnokov and Perelyaev 2022][research_chelnokov_perelyaev_2022]] [[Chen][research_chen]] [[Chen and Zhao 2024][research_chen_zhao_2024]] [[Chen et al 2011][research_chen_zheng_2011]] [[Chen et al 2011][research_chen_zheng_2011_b]] [[Chen et al 2014][research_chen_zhao_2014]] [[Chen et al 2016][research_chen_zhao_2016]] [[Chen et al 2021][research_chen_li_2021]] [[Chen et al 2023][research_chen_han_2023]] [[Chen et al 2023][research_chen_li_2023]] [[Chen et al 2024][research_chen_wei_2024]] [[Chihabi and Ulrich 2024][research_chihabi_ulrich_2024]] [[Chihabi and Ulrich 2024][research_chihabi_ulrich_2024_b]] [[Childers and Gelderloos][research_childers_gelderloos]] [[Chin 1985][research_chin_1985]] [[China Satellite Navigation Conference 2013][research_china_satellite_2013]] [[Cho and Lee 2025][research_cho_lee_2025]] [[Cho et al 2019][research_cho_kang_2019]] [[Choi 2016][research_choi_2016]] [[Chun et al 2005][research_chun_kwon_2005]] [[Clark][research_clark]] [[Cobb et al][research_cobb_cohen]] [[Cohen et al 1994][research_cohen_pervan_1994]] [[Corazzini et al 1998][research_corazzini_robertson_1998]] [[Cossaboom et al 2012][research_cossaboom_georgy_2012]] [[Cove and Santos 2004][research_cove_santos_2004]] [[Cox 1978][research_cox_1978]] [[Crain et al 2016][research_crain_bishop_2016]] [[Crassidis and Mook 1991][research_crassidis_mook_1991]] [[Crassidis and Mook 1992][research_crassidis_mook_1992]] [[Crassidis et al 1993][research_crassidis_mook_1993]] [[D'Amico et al 2008][research_damico_montenbruck_2008]] [[Dahmane et al 2022][research_dahmane_lejdel_2022]] [[Dang et al 2022][research_dang_chen_2022]] [[Daquan Tang et al 2016][research_daquantang_yongkangjiao_2016]] [[Davis 2010][research_davis_2010]] [[de Cunto][research_decunto]] [[Decoust and Udrea 2008][research_decoust_udrea_2008]] [[Delporte et al 2007][research_delporte_mercier_2007]] [[Delporte et al 2008][research_delporte_mercier_2008]] [[Deng and Duan 2016][research_deng_duan_2016]] [[Deprez and Warnant 2018][research_deprez_warnant_2018]] [[Di Li and Jinling Wang][research_dili_jinlingwang]] [[Dieffenbach 1995][research_dieffenbach_1995]] [[Diesel 1987][research_diesel_1987]] [[Differential carrier phase GPS-aided 1999][research_differential_carrier_1999]] [[Dill and Uijt de Haag 2016][research_dill_uijtdehaag_2016]] [[Dill et al 2017][research_dill_young_2017]] [[Ding 2015][research_ding_2015]] [[Ding et al 2007][research_ding_wang_2007]] [[Ding et al 2010][research_ding_wang_2010]] [[Ding et al 2015][research_ding_li_2015]] [[Doer et al 2020][research_doer_koenig_2020]] [[Dong et al 2020][research_dong_wang_2020]] [[Dong et al 2020][research_dong_zhang_2020]] [[Dou and Duan 2017][research_dou_duan_2017]] [[Duan et al 2015][research_duan_zhao_2015]] [[Duan et al 2016][research_duan_zhao_2016]] [[Duan et al 2022][research_duan_yuan_2022]] [[Durand and Wasicko 1967][research_durand_wasicko_1967]] [[Edwan et al 2012][research_edwan_zhou_2012]] [[Effective GPS Positioning Algorithm 2012][research_effective_gps_positioning_2012]] [[El-Diasty and Pagiatakis 2010][research_eldiasty_pagiatakis_2010]] [[El-Mowafy 2005][research_elmowafy_2005]] [[El-Mowafy 2008][research_elmowafy_2008]] [[El-Mowafy and Imparato 2018][research_elmowafy_imparato_2018]] [[Elchynski et al][research_elchynski_kirkland]] [[Elias 1985][research_elias_1985]] [[Ellingson et al 2018][research_ellingson_brink_2018]] [[Ellingson et al 2020][research_ellingson_brink_2020]] [[Enbo Shi 2012][research_enboshi_2012]] [[Enge 1999][research_enge_1999]] [[Enkhtur 2013][research_enkhtur_2013]] [[Erkeç and Hajiyev 2020][research_erkec_hajiyev_2020]] [[Ertler][research_ertler]] [[Falkenberg et al][research_falkenberg_hartt]] [[Fang et al 2018][research_fang_kim_2018]] [[Farrell et al 2001][research_farrell_vangraas_2001]] [[Fei-Bin Hsiao et al 2003][research_feibinhsiao_shihhsienhuang_2003]] [[Felter and Wu 1997][research_felter_wu_1997]] [[Felux et al 2013][research_felux_dautermann_2013]] [[Feng 2001][research_feng_2001]] [[Feng and Jokinen 2015][research_feng_jokinen_2015]] [[Feng et al 2011][research_feng_ochieng_2011]] [[Feng et al 2018][research_feng_li_2018]] [[Ferrando et al 1999][research_ferrando_perez_1999]] [[Fikes 1996][research_fikes_1996]] [[Firing][research_firing]] [[Firuzabadì and King 2011][research_firuzabadi_king_2011]] [[Fortenbaugh 1972][research_fortenbaugh_1972]] [[Frost 1995][research_frost_1995]] [[Frye 1984][research_frye_1984]] [[Fu et al 2015][research_fu_zhang_2015]] [[Fu et al 2023][research_fu_sun_2023]] [[Fusion of Multi-Antenna Carrier 2012][research_fusion_of_2012]] [[G et al 2016][research_g_mnvss_2016]] [[Galdos et al][research_galdos_upadhyay]] [[Gandolfi et al 2016][research_gandolfi_tavasci_2016]] [[Gannan Yuan and Tao Zhang 2009][research_gannanyuan_taozhang_2009]] [[Gao et al 2019][research_gao_li_2019]] [[Gavrilovski et al 2011][research_gavrilovski_ward_2011]] [[Gaylor and Lightsey 2003][research_gaylor_lightsey_2003]] [[Gazzino and Lelarge 2024][research_gazzino_lelarge_2024]] [[Ge et al 2005][research_ge_gendt_2005]] [[Gebre-Egziabher 2011][research_gebreegziabher_2011]] [[Geng and Wang 2007][research_geng_wang_2007]] [[Geng et al 2006][research_geng_li_2006]] [[Geng et al 2010][research_geng_deurloo_2010]] [[Geng et al 2017][research_geng_xie_2017]] [[Genrich and Minster 1991][research_genrich_minster_1991]] [[Georgy et al 2009][research_georgy_iqbal_2009]] [[Giorgi and G. Teunisse 2012][research_giorgi_gteunisse_2012]] [[Glaner and Weber 2021][research_glaner_weber_2021]] [[Glaner and Weber 2021][research_glaner_weber_2021_b]] [[Goad][research_goad]] [[Godha and Cannon 2007][research_godha_cannon_2007]] [[Goodall et al 2006][research_goodall_syed_2006]] [[GPS][research_gps]] [[GPS receiver selected for 2005][research_gps_receiver_2005]] [[GPS segments 2013][research_gps_segments_2013]] [[GPS signals 2013][research_gps_signals_2013]] [[Grafarend 2000][research_grafarend_2000]] [[Grafarend 2003][research_grafarend_2003]] [[Gray and Maybeck][research_gray_maybeck]] [[Grejner-Brzezinska and Wang 1998][research_grejnerbrzezinska_wang_1998]] [[Gross et al 2010][research_gross_gu_2010]] [[Gross et al 2010][research_gross_gu_2010_b]] [[Grzegorzewski and Śliwak 2016][research_grzegorzewski_sliwak_2016]] [[Guangcai et al 2021][research_guangcai_xu_2021]] [[Guo 2013][research_guo_2013]] [[Guo et al 2024][research_guo_geng_2024]] [[Guorong Zhao et al 2006][research_guorongzhao_jixinli_2006]] [[Ha 2008][research_ha_2008]] [[Haak 1994][research_haak_1994]] [[Hajiyev and Aykut Tutucu 2001][research_hajiyev_aykuttutucu_2001]] [[Hajiyev and Tutucu 2003][research_hajiyev_tutucu_2003]] [[Han and Wang 2011][research_han_wang_2011]] [[Han et al 2012][research_han_lee_2012]] [[Han et al 2016][research_han_xu_2016]] [[Han et al 2025][research_han_xu_2025]] [[Hao and Huang 2009][research_hao_huang_2009]] [[Hao et al 2018][research_hao_xu_2018]] [[Hardy et al 2016][research_hardy_strader_2016]] [[Hartana][research_hartana]] [[Hartman and Johnson 1998][research_hartman_johnson_1998]] [[Hawker 1991][research_hawker_1991]] [[Hawker 1992][research_hawker_1992]] [[Haxhi and Gikas 2023][research_haxhi_gikas_2023]] [[Hazlett et al 2011][research_hazlett_crassidis_2011]] [[He et al 2013][research_he_le_2013]] [[He et al 2026][research_he_wang_2026]] [[Henkel and Günther 2012][research_henkel_gunther_2012]] [[Henkel and Zhu 2011][research_henkel_zhu_2011]] [[Heo et al 2004][research_heo_pervan_2004]] [[Hermann et al 1995][research_hermann_evans_1995]] [[Hess and Judd 1976][research_hess_judd_1976]] [[Hewitson and Wang 2007][research_hewitson_wang_2007]] [[Hewitson et al 2004][research_hewitson_kyulee_2004]] [[Hide et al][research_hide_moore]] [[Hide et al 2003][research_hide_moore_2003]] [[High-Precision GPS Systems 2011][research_high_precision_gps_2011]] [[Hodgart and Purivigraipong][research_hodgart_purivigraipong]] [[Hongwei et al 2006][research_hongwei_zhihua_2006]] [[Hornbuckle 2015][research_hornbuckle_2015]] [[Hosseini and Jalili 2025][research_hosseini_jalili_2025]] [[hosseini et al 2024][research_hosseini_jalili_2024]] [[Hou et al 2024][research_hou_zhang_2024]] [[Hou et al 2025][research_hou_shi_2025]] [[Hou et al 2025][research_hou_wang_2025]] [[Hough et al 2024][research_hough_mohammadi_2024]] [[Hu et al 2020][research_hu_gao_2020]] [[Hu et al 2020][research_hu_ni_2020]] [[Huan-Jung Lin][research_huanjunglin]] [[Huang et al 2011][research_huang_yu_2011]] [[Huang et al 2019][research_huang_zhao_2019]] [[Hui et al 2014][research_hui_liu_2014]] [[Hundley et al 1993][research_hundley_rowson_1993]] [[Hvezda 2021][research_hvezda_2021]] [[Hwang and Brown 1990][research_hwang_brown_1990]] [[Hwang and Speyer 2009][research_hwang_speyer_2009]] [[Ibrahim 2008][research_ibrahim_2008]] [[Idris et al 2014][research_idris_sathyamoorthy_2014]] [[Integration of GPS and 1991][research_integration_of_1991]] [[Ioannidis et al][research_ioannidis_walton]] [[Irigireddy and Moncayo 2020][research_irigireddy_moncayo_2020]] [[Isaacs et al 2016][research_isaacs_ezal_2016]] [[Islam and Saha 2017][research_islam_saha_2017]] [[Iwamoto et al 2016][research_iwamoto_takewa_2016]] [[J. et al 2013][research_j_golubkov_2013]] [[J.M. Urnes et al 1981][research_jmurnes_moomaw_1981]] [[Jacob 1989][research_jacob_1989]] [[Jeong et al 2023][research_jeong_kee_2023]] [[Jeong et al 2025][research_jeong_kee_2025]] [[Jeong Won Kim et al][research_jeongwonkim_donghwanhwang]] [[Ji et al 2013][research_ji_xu_2013]] [[Jia et al 2016][research_jia_chen_2016]] [[Jian-jun et al 2003][research_jianjun_xiaoli_2003]] [[Jiancheng Fang and Xiaolin Gong 2010][research_jianchengfang_xiaolingong_2010]] [[Jiang and Muluneh Mekonnen 2013][research_jiang_mulunehmekonnen_2013]] [[Jiang et al 2016][research_jiang_zhang_2016]] [[Jiang et al 2024][research_jiang_yan_2024]] [[Jianping Yuan et al 1998][research_jianpingyuan_jianjunluo_1998]] [[Jiao et al 2018][research_jiao_rino_2018]] [[Jiayao et al 2020][research_jiayao_dalong_2020]] [[Jing et al 2015][research_jing_xu_2015]] [[Joerger and Pervan 2012][research_joerger_pervan_2012]] [[Johnson and Ivanov 2011][research_johnson_ivanov_2011]] [[Johnson et al 2007][research_johnson_ansar_2007]] [[Junli Chen et al 2010][research_junlichen_xiaoliangwang_2010]] [[Jwo 2004][research_jwo_2004]] [[Jwo and Chang 2009][research_jwo_chang_2009]] [[Jwo and Chung 2010][research_jwo_chung_2010]] [[Jwo and Huang 2007][research_jwo_huang_2007]] [[Jwo and Lai 2007][research_jwo_lai_2007]] [[Jwo et al 2009][research_jwo_chen_2009]] [[Jwo et al 2013][research_jwo_yang_2013]] [[Kalman Filter Basics 2000][research_kalman_filter_2000]] [[Kalman Filter Engineering 2000][research_kalman_filter_2000_b]] [[Kang et al 2018][research_kang_park_2018]] [[Kang et al 2018][research_kang_park_2018_b]] [[Kasuda 2011][research_kasuda_2011]] [[Kawamura et al 2022][research_kawamura_kannan_2022]] [[Kawano et al 2001][research_kawano_mokuno_2001]] [[Kee et al 2004][research_kee_park_2004]] [[Keke et al 2014][research_keke_nong_2014]] [[Kelley et al][research_kelley_katz]] [[Kelly and Davis 1994][research_kelly_davis_1994]] [[Ketterle et al 2008][research_ketterle_vuletic_2008]] [[Khanafseh and Pervan 2008][research_khanafseh_pervan_2008]] [[Khodabandeh and Teunissen 2022][research_khodabandeh_teunissen_2022]] [[Kim and Park 2007][research_kim_park_2007]] [[Kim and Sung 2025][research_kim_sung_2025]] [[Kim and Sung 2025][research_kim_sung_2025_b]] [[Kim et al][research_kim_jee]] [[Kim et al 2012][research_kim_won_2012]] [[Kim et al 2013][research_kim_choi_2013]] [[Kim et al 2024][research_kim_kim_2024]] [[Kim et al 2025][research_kim_kim_2025]] [[Kis and Lantos 2011][research_kis_lantos_2011]] [[Kishi and Pfeffer 1971][research_kishi_pfeffer_1971]] [[Kleusberg 1989][research_kleusberg_1989]] [[Koenke et al][research_koenke_hill]] [[Kometani 2005][research_kometani_2005]] [[Kondo and Yasuda 2006][research_kondo_yasuda_2006]] [[Koremura][research_koremura]] [[Kovach and Conley 1991][research_kovach_conley_1991]] [[Kozel and Cardoza][research_kozel_cardoza]] [[Krasuski and Wierzbicki 2018][research_krasuski_wierzbicki_2018]] [[Krempasky 1996][research_krempasky_1996]] [[Krempasky 1999][research_krempasky_1999]] [[Krempasky and Krempasky 1997][research_krempasky_krempasky_1997]] [[Krzykowska-Piotrowska 2020][research_krzykowskapiotrowska_2020]] [[Kubo et al][research_kubo_ito]] [[Kubo et al 2004][research_kubo_muto_2004]] [[Kubo et al 2007][research_kubo_fujita_2007]] [[Kukla 2026][research_kukla_2026]] [[Kumar][research_kumar]] [[Kumar et al 2019][research_kumar_yokeshraj_2019]] [[Kumar Rath et al 2020][research_kumarrath_ramirezserrano_2020]] [[Kwon et al 2012][research_kwon_jang_2012]] [[Lachapelle et al 1992][research_lachapelle_cannon_1992]] [[Ladd and Xinhua Qin][research_ladd_xinhuaqin]] [[Lai 2007][research_lai_2007]] [[Lai et al 2022][research_lai_tong_2022]] [[Lambregts and Creedon 1980][research_lambregts_creedon_1980]] [[Landrum and Tournes 2001][research_landrum_tournes_2001]] [[Lannes 2001][research_lannes_2001]] [[Lau 2016][research_lau_2016]] [[Laurichesse et al 2009][research_laurichesse_mercier_2009]] [[Le et al 2014][research_le_he_2014]] [[Lee][research_lee]] [[Lee 1988][research_lee_1988]] [[Lee 2014][research_lee_2014]] [[Lee and O'Laughlin 2000][research_lee_olaughlin_2000]] [[Lee and O'Laughlin 2001][research_lee_olaughlin_2001]] [[Lee et al 2005][research_lee_wang_2005]] [[Lee et al 2008][research_lee_soon_2008]] [[Lee et al 2012][research_lee_park_2012]] [[Lee et al 2015][research_lee_kim_2015]] [[Leishman et al 2013][research_leishman_mclain_2013]] [[Lejeune et al 2011][research_lejeune_wautelet_2011]] [[Leonidov 2021][research_leonidov_2021]] [[Leva][research_leva]] [[Lewantowicz][research_lewantowicz]] [[Li and Duan 2015][research_li_duan_2015]] [[Li and Leung 2007][research_li_leung_2007]] [[Li and Sun 2013][research_li_sun_2013]] [[Li and Wang 2013][research_li_wang_2013_b]] [[Li et al 2008][research_li_rizos_2008]] [[Li et al 2009][research_li_feng_2009]] [[Li et al 2012][research_li_glennon_2012]] [[Li et al 2012][research_li_zhang_2012]] [[Li et al 2013][research_li_cao_2013]] [[Li et al 2013][research_li_chen_2013]] [[Li et al 2013][research_li_verhagen_2013]] [[Li et al 2013][research_li_wang_2013]] [[Li et al 2013][research_li_yang_2013]] [[Li et al 2013][research_li_yuan_2013]] [[Li et al 2014][research_li_li_2014]] [[Li et al 2015][research_li_li_2015]] [[Li et al 2016][research_li_gao_2016]] [[Li et al 2016][research_li_wang_2016]] [[Li et al 2018][research_li_yuan_2018]] [[Li et al 2020][research_li_jiang_2020]] [[Li et al 2020][research_li_weng_2020]] [[Li et al 2022][research_li_li_2022]] [[Li et al 2022][research_li_li_2022_b]] [[Li et al 2024][research_li_tang_2024]] [[Li et al 2024][research_li_zhai_2024]] [[Li et al 2024][research_li_zhai_2024_b]] [[Li et al 2025][research_li_wang_2025]] [[Li et al 2025][research_li_yan_2025]] [[Li et al 2026][research_li_zhang_2026]] [[Liang et al 2022][research_liang_li_2022]] [[Lightsey and Crassidis 2004][research_lightsey_crassidis_2004]] [[Lightsey et al 1999][research_lightsey_crassidis_1999]] [[Lin 2015][research_lin_2015]] [[Lin 2023][research_lin_2023]] [[Lin and Da 1994][research_lin_da_1994]] [[Lin et al 2020][research_lin_meghdadhasheminasab_2020]] [[Liu 2024][research_liu_2024]] [[Liu and Cai 2019][research_liu_cai_2019]] [[Liu and Chen 2011][research_liu_chen_2011]] [[Liu and Yan 2025][research_liu_yan_2025]] [[Liu et al 2007][research_liu_wang_2007]] [[Liu et al 2014][research_liu_chen_2014]] [[Liu et al 2017][research_liu_fu_2017]] [[Liu et al 2017][research_liu_lou_2017]] [[Liu et al 2018][research_liu_fan_2018]] [[Liu et al 2018][research_liu_yang_2018]] [[Liu et al 2021][research_liu_zheng_2021]] [[Liu et al 2022][research_liu_tan_2022]] [[Liu et al 2024][research_liu_zhang_2024]] [[Liu et al 2024][research_liu_zhang_2024_b]] [[Liu et al 2025][research_liu_bogu_2025]] [[Liu et al 2025][research_liu_zhang_2025]] [[Loh and Fernow][research_loh_fernow]] [[Lopez 2010][research_lopez_2010]] [[Lopez et al 2021][research_lopez_garcia_2021]] [[Low and D'Amico 2024][research_low_damico_2024]] [[Lu 2021][research_lu_2021]] [[Lu Keke et al 2016][research_lukeke_yujinyong_2016]] [[Lungu et al 2022][research_lungu_chen_2022]] [[Luo et al 2012][research_luo_babu_2012]] [[Luzica and Bloudicek 2016][research_luzica_bloudicek_2016]] [[Ma et al 2018][research_ma_guan_2018]] [[Ma et al 2022][research_ma_lou_2022]] [[MacDORAN et al 1984][research_macdoran_miller_1984]] [[Macias-Valadez et al 2011][research_maciasvaladez_santerre_2011]] [[Mader 2001][research_mader_2001]] [[Madonna et al 2010][research_madonna_viola_2010]] [[Madyastha et al 2011][research_madyastha_ravindra_2011]] [[Maeda et al 1998][research_maeda_itsukaichi_1998]] [[Mah and O'Keefe 2025][research_mah_okeefe_2025]] [[Mahmud et al 2016][research_mahmud_qaisar_2016]] [[Maier et al 2011][research_maier_kiesel_2011]] [[Malleswaran et al 2011][research_malleswaran_vaidehi_2011]] [[Marques Filho et al 2016][research_marquesfilho_riosneto_2016]] [[Marquis 2003][research_marquis_2003]] [[Martin et al 2010][research_martin_travis_2010]] [[Maskell][research_maskell]] [[Massarweh and Teunissen 2025][research_massarweh_teunissen_2025]] [[Mathematical model of the 2023][research_mathematical_model_2023]] [[Maybourn 1983][research_maybourn_1983]] [[McBurney][research_mcburney]] [[McFarland][research_mcfarland]] [[McFARLAND 1991][research_mcfarland_1991]] [[Mcnally et al 1992][research_mcnally_warner_1992]] [[Meng 2013][research_meng_2013]] [[Meng and Li 2014][research_meng_li_2014]] [[Meng et al 2019][research_meng_wang_2019]] [[Meng et al 2023][research_meng_sun_2023]] [[Mi et al 2022][research_mi_zhang_2022]] [[Michalson 1995][research_michalson_1995]] [[Michaud and Santerre 2001][research_michaud_santerre_2001]] [[Mikhailov and Mikhailov 2010][research_mikhailov_mikhailov_2010]] [[Milbert 2005][research_milbert_2005]] [[Milbert 2005][research_milbert_2005_b]] [[Milner et al 2011][research_milner_ochieng_2011]] [[Misra and Bai 2019][research_misra_bai_2019]] [[Misra et al 1993][research_misra_bayliss_1993]] [[Moafipoor et al 2012][research_moafipoor_grejnerbrzezinska_2012]] [[Moafipoor et al 2018][research_moafipoor_bock_2018]] [[Mohiuddin and Psiaki 2005][research_mohiuddin_psiaki_2005]] [[Mohiuddin and Psiaki 2006][research_mohiuddin_psiaki_2006]] [[Montenbruck and D'Amico 2012][research_montenbruck_damico_2012]] [[Montenbruck et al 2002][research_montenbruck_ebinuma_2002]] [[Montenbruck et al 2011][research_montenbruck_wermuth_2011]] [[Montenbruck et al 2012][research_montenbruck_swatschina_2012]] [[Montenbruck et al 2017][research_montenbruck_hackel_2017]] [[Mook et al 1990][research_mook_swanson_1990]] [[Moon-Beom Heo and Pervan 2006][research_moonbeomheo_pervan_2006]] [[Moore 2013][research_moore_2013]] [[Morujão and Mendes 2008][research_morujao_mendes_2008]] [[Mosavi and Shafiee 2015][research_mosavi_shafiee_2015]] [[Murakami and Peck 2011][research_murakami_peck_2011]] [[Muralikrishna et al 2022][research_muralikrishna_mallesham_2022]] [[Nam][research_nam]] [[Nam et al 2026][research_nam_min_2026]] [[Napier 1989][research_napier_1989]] [[Nayerabadi and Mohammadi 2022][research_nayerabadi_mohammadi_2022]] [[Nebula 2018][research_nebula_2018]] [[Negast and Paschall][research_negast_paschall]] [[Neusypin et al 2023][research_neusypin_kupriyanov_2023]] [[Nicosia et al][research_nicosia_loss]] [[Nielsen 1997][research_nielsen_1997]] [[Nikiforov 1995][research_nikiforov_1995]] [[Ning Luo and Lachapelle 2003][research_ningluo_lachapelle_2003]] [[Noe and Zabaneh][research_noe_zabaneh]] [[Noureldin et al 2012][research_noureldin_karamat_2012]] [[Nowel et al 2018][research_nowel_cellmer_2018]] [[O'Keefe et al 2006][research_okeefe_julien_2006]] [[Odijk and Teunissen 2002][research_odijk_teunissen_2002]] [[Odijk and Teunissen 2011][research_odijk_teunissen_2011]] [[Odijk et al 2012][research_odijk_teunissen_2012]] [[Odolinski and Teunissen 2017][research_odolinski_teunissen_2017]] [[Oh and Johnson 2007][research_oh_johnson_2007]] [[Oh et al 2016][research_oh_park_2016]] [[Ojha et al 2009][research_ojha_chow_2009]] [[Olds 1998][research_olds_1998]] [[Olsen et al 1999][research_olsen_park_1999]] [[Olson et al 2020][research_olson_toombs_2020]] [[Omar et al 2016][research_omar_yanzhong_2016]] [[Owens et al 2021][research_owens_macdonald_2021]] [[Parkinson and Axelrad 1988][research_parkinson_axelrad_1988]] [[Parkinson et al 1970][research_parkinson_bauman_1970]] [[Particle Filter Performance for 2008][research_particle_filter_2008]] [[Pei and Xia 2018][research_pei_xia_2018]] [[Peng et al 2007][research_peng_li_2007]] [[Peng et al 2025][research_peng_li_2025]] [[Pereira and Sanguino 2016][research_pereira_sanguino_2016]] [[Performance Evaluation of the 2023][research_performance_evaluation_of_2023]] [[Performance Investigation of GPS/INS 2006][research_performance_investigation_2006]] [[Performance Investigation of the 2007][research_performance_investigation_2007]] [[Pervan et al 1994][research_pervan_cohen_1994]] [[Pervan et al 1998][research_pervan_pullen_1998]] [[Pervan et al 2003][research_pervan_chan_2003]] [[Petit et al 2015][research_petit_kanj_2015]] [[Poritzky 1970][research_poritzky_1970]] [[Poritzky 1971][research_poritzky_1971]] [[Priambodo et al 2022][research_priambodo_arifin_2022]] [[Prickett and Parkes][research_prickett_parkes]] [[Progri and Michalson][research_progri_michalson]] [[Psiaki and Mohiuddin 2005][research_psiaki_mohiuddin_2005]] [[Psiaki and Mohiuddin 2007][research_psiaki_mohiuddin_2007]] [[Pullen and Joerger 2020][research_pullen_joerger_2020]] [[Pullen et al][research_pullen_enge]] [[Pullen et al][research_pullen_pervan]] [[Purivigraipong et al 2005][research_purivigraipong_unwin_2005]] [[Purivigraipong et al 2010][research_purivigraipong_hodgart_2010]] [[Qian et al 2010][research_qian_chengquan_2010]] [[Qin et al 2017][research_qin_ang_2017]] [[Qin et al 2019][research_qin_yue_2019]] [[Qin et al 2024][research_qin_yang_2024]] [[Rabbou and El-Rabbany 2021][research_rabbou_elrabbany_2021]] [[Racette et al 2023][research_racette_dunaway_2023]] [[Radar Altimeter Aiding of 2019][research_radar_altimeter_2019]] [[Rao and Narayana 1995][research_rao_narayana_1995]] [[Rao et al 2001][research_rao_sarma_2001]] [[Rapinski et al 2012][research_rapinski_cellmer_2012]] [[Ratcliffe 1983][research_ratcliffe_1983]] [[Ray et al 1999][research_ray_salychev_1999]] [[Real-Time Kinematics Relative Positioning 2015][research_real_time_kinematics_2015]] [[Reid 1978][research_reid_1978]] [[Relative Navigation 1972][research_relative_navigation_1972]] [[Ren et al 2023][research_ren_lyu_2023]] [[Renga et al 2009][research_renga_tancredi_2009]] [[Renga et al 2013][research_renga_grassi_2013]] [[Renga et al 2015][research_renga_tancredi_2015]] [[Rezaifard and Abbasi 2017][research_rezaifard_abbasi_2017]] [[Rhudy et al 2014][research_rhudy_gu_2014]] [[Riaz 2011][research_riaz_2011]] [[Rife 2009][research_rife_2009]] [[Rife et al 2008][research_rife_khanafseh_2008]] [[Rosamond 1961][research_rosamond_1961]] [[Rothmaier and Del Peral Rosado 2023][research_rothmaier_delperalrosado_2023]] [[Ruan and Wei 2019][research_ruan_wei_2019]] [[Rui 2016][research_rui_2016]] [[Rui Li et al 2013][research_ruili_dazhizeng_2013]] [[Sabatini et al 2013][research_sabatini_moore_2013]] [[Sachs and Moeller 1995][research_sachs_moeller_1995]] [[Safvat and Keighobadi 2025][research_safvat_keighobadi_2025]] [[Sai et al 2025][research_sai_athreyam_2025]] [[Salt 1995][research_salt_1995]] [[Santerre and Geiger 2018][research_santerre_geiger_2018]] [[Santerre et al 2017][research_santerre_geiger_2017]] [[Santhosh Kumar S A and Suganthi J 2015][research_santhoshkumarsa_suganthij_2015]] [[Sasiadek and Wang 1999][research_sasiadek_wang_1999]] [[Sasiadek et al 2000][research_sasiadek_wang_2000]] [[Satkunanathan and Murphy 1998][research_satkunanathan_murphy_1998]] [[Sayim 2018][research_sayim_2018]] [[Scherzinger and Blake Reid 1989][research_scherzinger_blakereid_1989]] [[Schmidt and Setterlund 1994][research_schmidt_setterlund_1994]] [[Schneider and Maida][research_schneider_maida]] [[Serrano and Serrano 2010][research_serrano_serrano_2010]] [[Shaghaghian and Karimaghaee 2018][research_shaghaghian_karimaghaee_2018]] [[Shaiju and Sreeja 2022][research_shaiju_sreeja_2022]] [[Shaikh 2025][research_shaikh_2025]] [[Sharma and Hablani 2014][research_sharma_hablani_2014]] [[Shen et al 2016][research_shen_hao_2016]] [[Shen et al 2019][research_shen_lifey_2019]] [[Shi and Gao 2013][research_shi_gao_2013]] [[Shoop et al 2023][research_shoop_munoz_2023]] [[Shoop et al 2024][research_shoop_munoz_2024]] [[Shu et al 2013][research_shu_sun_2013]] [[Simonetti and Crespillo 2024][research_simonetti_crespillo_2024]] [[Sjöberg 1998][research_sjoberg_1998]] [[Slegers et al 2008][research_slegers_beyer_2008]] [[Snyder et al][research_snyder_schipper]] [[Snyder et al 1992][research_snyder_schipper_1992]] [[So 2016][research_so_2016]] [[Soloviev and Venable 2010][research_soloviev_venable_2010]] [[Song et al 2019][research_song_zhang_2019]] [[Song et al 2020][research_song_chen_2020]] [[Soni and Hablani 2015][research_soni_hablani_2015]] [[Souza and Monico 2004][research_souza_monico_2004]] [[Speth et al 2016][research_speth_kamann_2016]] [[Srinuandee][research_srinuandee]] [[Steinberg][research_steinberg]] [[Steinberg 1992][research_steinberg_1992]] [[Stoltz 1995][research_stoltz_1995]] [[Stolz and Hein 1989][research_stolz_hein_1989]] [[Stratton 1995][research_stratton_1995]] [[Sturza 1983][research_sturza_1983]] [[Su and Schön 2021][research_su_schon_2021]] [[Su et al 2013][research_su_xu_2013]] [[Su et al 2023][research_su_schon_2023]] [[Subrahmanyam 1994][research_subrahmanyam_1994]] [[Subrahmanyam 1995][research_subrahmanyam_1995]] [[Subrata 2017][research_subrata_2017]] [[Sugimoto 2006][research_sugimoto_2006]] [[Sun and Fu 2018][research_sun_fu_2018]] [[Sun and Tang 2011][research_sun_tang_2011]] [[Sun et al 2022][research_sun_zhang_2022_b]] [[Sun et al 2025][research_sun_duan_2025]] [[Sun et al 2026][research_sun_zhang_2026]] [[Suozhong Yuan and Yidong Yang][research_suozhongyuan_yidongyang]] [[Supriyono and Akhara 2021][research_supriyono_akhara_2021]] [[Svendsen et al 2013][research_svendsen_obrien_2013]] [[Swanson][research_swanson]] [[T. Davies 1974][research_tdavies_1974]] [[T. Ruxton-davies and Powell 1970][research_truxtondavies_powell_1970]] [[Taghizadeh and Safabakhsh 2023][research_taghizadeh_safabakhsh_2023]] [[Talbot 1991][research_talbot_1991]] [[Tan et al 2015][research_tan_wang_2015]] [[Tancredi et al 2010][research_tancredi_renga_2010]] [[Tancredi et al 2012][research_tancredi_renga_2012]] [[Tancredi et al 2013][research_tancredi_renga_2013]] [[Tancredi et al 2014][research_tancredi_renga_2014]] [[Tang et al 2018][research_tang_shen_2018]] [[Tangthong and Aktimagool 2021][research_tangthong_aktimagool_2021]] [[Tanil et al 2016][research_tanil_khanafseh_2016]] [[Tao et al 2022][research_tao_chen_2022]] [[Tatiyaworanun and Purivigraipong 2013][research_tatiyaworanun_purivigraipong_2013]] [[Terheyden and Zickwolff 1986][research_terheyden_zickwolff_1986]] [[Terrain Relative Navigation 2025][research_terrain_relative_2025]] [[Teunissen][research_teunissen]] [[Teunissen][research_teunissen_b]] [[Teunissen 1995][research_teunissen_1995]] [[Teunissen 1998][research_teunissen_1998]] [[Teunissen 2000][research_teunissen_2000]] [[Teunissen 2003][research_teunissen_2003]] [[Teunissen 2003][research_teunissen_2003_b]] [[Teunissen 2017][research_teunissen_2017]] [[Teunissen 2026][research_teunissen_2026]] [[Teunissen and Odijk 2003][research_teunissen_odijk_2003]] [[Teunissen and Verhagen][research_teunissen_verhagen]] [[Teunissen et al 1999][research_teunissen_joosten_1999]] [[The Block Decorrelation Method 2002][research_the_block_2002]] [[The Origins of Satellite 2018][research_the_origins_2018]] [[The Resampled Kernel-Diffeomorphism Filter 2011][research_the_resampled_2011]] [[The Use of Digital 2006][research_the_use_2006]] [[Tian et al 2016][research_tian_ge_2016]] [[Tian et al 2025][research_tian_gong_2025]] [[Tian et al 2026][research_tian_sun_2026]] [[Tiberius et al 2002][research_tiberius_pany_2002]] [[Toth et al 2017][research_toth_jozkow_2017]] [[Tranfield][research_tranfield]] [[Travis et al 2005][research_travis_simmons_2005]] [[Tsai et al 2004][research_tsai_chang_2004]] [[Tseng et al 2016][research_tseng_lin_2016]] [[Turner and Faruqi][research_turner_faruqi]] [[Urnes and Hess 1983][research_urnes_hess_1983]] [[Urnes and Hess 1985][research_urnes_hess_1985]] [[Urnes et al 1979][research_urnes_hess_1979]] [[Utterstrom and Kestek 1965][research_utterstrom_kestek_1965]] [[Vallot et al 1991][research_vallot_snyder_1991]] [[Van Dierendonck et al 1992][research_vandierendonck_hatch_1992]] [[Van Dyke 1992][research_vandyke_1992]] [[Van et al 2015][research_van_van_2015]] [[van Graas 1988][research_vangraas_1988]] [[van Kampen et al 2009][research_vankampen_deweerdt_2009]] [[Vana and Bisnath 2024][research_vana_bisnath_2024]] [[Vehicle Navigation using Carrier 2002][research_vehicle_navigation_2002]] [[Verhagen 2004][research_verhagen_2004]] [[Verhagen 2005][research_verhagen_2005]] [[Verma et al 2021][research_verma_shrinivasan_2021]] [[Videmsek and de Haag 2020][research_videmsek_dehaag_2020]] [[Videmsek et al 2019][research_videmsek_dehaag_2019]] [[Vieweg][research_vieweg]] [[Visual glide slope indicator 1961][research_visual_glide_1961]] [[Vorobуev et al 2020][research_vorobev_beliatskaya_2020]] [[WAAS GPS Landing System 2009][research_waas_gps_2009]] [[Wagner 2005][research_wagner_2005]] [[Wall 1962][research_wall_1962]] [[Wang 2000][research_wang_2000]] [[Wang 2010][research_wang_2010]] [[Wang and Jan 2023][research_wang_jan_2023]] [[Wang and Ober 2009][research_wang_ober_2009]] [[Wang and Wang 2013][research_wang_wang_2013]] [[Wang et al 1996][research_wang_morikawa_1996]] [[Wang et al 2001][research_wang_rizos_2001]] [[Wang et al 2002][research_wang_iz_2002]] [[Wang et al 2006][research_wang_liu_2006]] [[Wang et al 2009][research_wang_miao_2009]] [[Wang et al 2010][research_wang_deng_2010]] [[Wang et al 2010][research_wang_gong_2010]] [[Wang et al 2012][research_wang_yang_2012]] [[Wang et al 2013][research_wang_cui_2013]] [[Wang et al 2013][research_wang_huang_2013]] [[Wang et al 2016][research_wang_chen_2016]] [[Wang et al 2018][research_wang_rathinam_2018]] [[Wang et al 2018][research_wang_wu_2018]] [[Wang et al 2018][research_wang_wu_2018_b]] [[Wang et al 2019][research_wang_yao_2019]] [[Wang et al 2020][research_wang_zhan_2020]] [[Wang et al 2021][research_wang_li_2021]] [[Wang et al 2021][research_wang_lv_2021]] [[Wang et al 2021][research_wang_toth_2021]] [[Wang et al 2021][research_wang_you_2021]] [[Wang et al 2021][research_wang_zhan_2021]] [[Wang et al 2022][research_wang_hou_2022]] [[Wang et al 2023][research_wang_zhan_2023]] [[Wanli Xu et al 2012][research_wanlixu_zhunliu_2012]] [[Ward 1994][research_ward_1994]] [[Ward and Costello 2012][research_ward_costello_2012]] [[Ward and Costello 2013][research_ward_costello_2013]] [[Ward et al 2013][research_ward_gavrilovski_2013]] [[Wareyka-Glaner and Möller 2025][research_wareykaglaner_moller_2025]] [[Wei and Du 2018][research_wei_du_2018]] [[Wei and Schwarz][research_wei_schwarz]] [[Wei et al 2025][research_wei_kang_2025]] [[Weiss and Shields][research_weiss_shields]] [[Wen et al 2021][research_wen_pfeifer_2021]] [[Wendel et al 2005][research_wendel_maier_2005]] [[Wenhu You et al][research_wenhuyou_fuxingjiang]] [[Wheeler et al 2016][research_wheeler_nyholm_2016]] [[Wheeler et al 2018][research_wheeler_koch_2018]] [[Widnall et al 1982][research_widnall_gobbini_1982]] [[Wiederholt and Klein 1984][research_wiederholt_klein_1984]] [[Williams et al 2000][research_williams_davis_2000]] [[Wilson et al 2014][research_wilson_goktogan_2014]] [[Wolfe 1976][research_wolfe_1976]] [[Wolfe and Speyer 2004][research_wolfe_speyer_2004]] [[Wolfe et al 2003][research_wolfe_williamson_2003]] [[wu 2017][research_wu_2017]] [[Wu et al 2008][research_wu_peck_2008]] [[Wu et al 2017][research_wu_gu_2017]] [[Wu et al 2018][research_wu_zhang_2018]] [[Wu et al 2026][research_wu_zhu_2026]] [[Xia 2004][research_xia_2004]] [[Xiang Jin and de Jong 1996][research_xiangjin_dejong_1996]] [[Xiaofeng et al 2020][research_xiaofeng_daqian_2020]] [[Xie et al 2023][research_xie_huang_2023]] [[Xu 2002][research_xu_2002]] [[Xu 2013][research_xu_2013]] [[Xu 2025][research_xu_2025]] [[Xu and Morton 2018][research_xu_morton_2018]] [[Xu et al 2010][research_xu_li_2010]] [[Xu et al 2012][research_xu_shi_2012]] [[Xu et al 2013][research_xu_liu_2013]] [[Xu et al 2017][research_xu_zhao_2017]] [[Xu et al 2022][research_xu_shen_2022]] [[Xuan Zhao et al 2016][research_xuanzhao_zhong_2016]] [[Xue et al 2023][research_xue_zhen_2023]] [[Yadav et al 2017][research_yadav_shanmukha_2017]] [[Yan and Zhao 2014][research_yan_zhao_2014]] [[Yang and Mischel 1995][research_yang_mischel_1995]] [[Yang et al 2001][research_yang_chang_2001]] [[Yang et al 2013][research_yang_li_2013]] [[Yang et al 2013][research_yang_zheng_2013]] [[Yang et al 2016][research_yang_jiang_2016]] [[Yang et al 2018][research_yang_duan_2018]] [[Yang et al 2018][research_yang_shi_2018]] [[Yang et al 2023][research_yang_zhang_2023]] [[Yang et al 2023][research_yang_zhang_2023_b]] [[Yang et al 2023][research_yang_zheng_2023]] [[Yang et al 2024][research_yang_zhu_2024]] [[Yao et al 2024][research_yao_kan_2024]] [[Yao et al 2025][research_yao_li_2025]] [[Yao et al 2025][research_yao_li_2025_b]] [[Ye et al 2022][research_ye_zhang_2022]] [[Ye et al 2023][research_ye_gu_2023]] [[Yin et al 2025][research_yin_teunissen_2025]] [[Yoon and Lundberg 2002][research_yoon_lundberg_2002]] [[Yoon et al 2004][research_yoon_nerem_2004]] [[Yu and Chen 2010][research_yu_chen_2010]] [[Yu et al 2019][research_yu_he_2019]] [[Yuan and Bao 2012][research_yuan_bao_2012]] [[Yuan et al 2011][research_yuan_yuan_2011]] [[Yue et al 2016][research_yue_liu_2016]] [[Yue et al 2017][research_yue_lian_2017]] [[Yukihiro et al 2000][research_yukihiro_akihiko_2000]] [[Zandbergen and Barbeau 2011][research_zandbergen_barbeau_2011]] [[Zhai et al 2012][research_zhai_qi_2012]] [[Zhang 2018][research_zhang_2018]] [[Zhang 2021][research_zhang_2021]] [[Zhang 2025][research_zhang_2025]] [[Zhang and Morton 2013][research_zhang_morton_2013]] [[Zhang and Wang 2023][research_zhang_wang_2023_b]] [[Zhang and Yang 2013][research_zhang_yang_2013]] [[Zhang et al 2012][research_zhang_niu_2012]] [[Zhang et al 2012][research_zhang_zhang_2012]] [[Zhang et al 2016][research_zhang_liu_2016]] [[Zhang et al 2017][research_zhang_li_2017]] [[Zhang et al 2019][research_zhang_zhai_2019]] [[Zhang et al 2019][research_zhang_zhai_2019_b]] [[Zhang et al 2022][research_zhang_chai_2022]] [[Zhang et al 2023][research_zhang_zhang_2023]] [[Zhang et al 2024][research_zhang_li_2024]] [[Zhang et al 2026][research_zhang_fang_2026]] [[Zhao et al 2016][research_zhao_qiu_2016]] [[Zhao et al 2017][research_zhao_li_2017]] [[Zhao et al 2023][research_zhao_khanafseh_2023]] [[Zhen et al 2019][research_zhen_peng_2019]] [[Zhen et al 2020][research_zhen_yu_2020]] [[Zhijin Zhao et al 2006][research_zhijinzhao_qigao_2006]] [[Zhilan Xiong et al][research_zhilanxiong_yanlinghao]] [[Zhimin and Guanxin 2008][research_zhimin_guanxin_2008]] [[Zhimin and Guanxin 2013][research_zhimin_guanxin_2013_b]] [[ZhiWen et al 2013][research_zhiwen_xiaoping_2013]] [[Zhong et al 2018][research_zhong_xu_2018]] [[Zhong et al 2018][research_zhong_xu_2018_b]] [[Zhou et al 2010][research_zhou_knedlik_2010]] [[Zhou et al 2011][research_zhou_yang_2011]] [[Zhou et al 2017][research_zhou_wan_2017]] [[Zhou et al 2024][research_zhou_liu_2024]] [[Zhu and Yang 2020][research_zhu_yang_2020]] [[Zhu et al 2006][research_zhu_lai_2006]] [[Zhu et al 2017][research_zhu_zhang_2017]] [[Zhu Qi-dan et al 2009][research_zhuqidan_wangtong_2009]] [[Zhu Qi-dan et al 2009][research_zhuqidan_wangtong_2009_b]] [[Zou et al 2026][research_zou_zhen_2026]]

### Automatic takeoff, landing and carrier recovery

**Where an unmanned aeroplane earns or loses its case.** Automatic takeoff and landing, carrier approach and recovery, arresting gear, catapults and autonomous aerial refuelling. **The X-45A taxied, took off and landed without a pilot in any loop**, which was novel in 2002 and is the least remarked of its achievements.

**395 records.** [[A testing platform which 1950][research_a_testing_1950]] [[Abu-Akeel 1968][research_abuakeel_1968]] [[Abu-Akeel 1969][research_abuakeel_1969]] [[Aerospace Landing GEAR Systems][research_aerospace_landing]] [[Ahlrich 1991][research_ahlrich_1991]] [[Air Force District Of Washington 2015][research_airforcedistrictofwashington_2015]] [[Aircraft ground equipment. Design][research_aircraft_ground_b]] [[Aircraft Landing GEAR][research_aircraft_landing]] [[Aircraft Tires Key Principles 2022][research_aircraft_tires_2022]] [[Aircraft Wheels, Brakes, and 2022][research_aircraft_wheels_2022]] [[Allen and Breitsamter 2008][research_allen_breitsamter_2008]] [[Altmann 2013][research_altmann_2013]] [[Apeng et al 2018][research_apeng_shu_2018]] [[ASTM International Standard helps 2007][research_astm_international_2007]] [[Aubert et al 2016][research_aubert_ross_2016]] [[Bardera et al 2019][research_bardera_barcalamontejano_2019]] [[Batill and Bacarro 1988][research_batill_bacarro_1988]] [[Beklemishchev and Tikhonov 2021][research_beklemishchev_tikhonov_2021]] [[Berbaum et al 1991][research_berbaum_kennedy_1991]] [[Berry 2000][research_berry_2000]] [[Best 1986][research_best_1986]] [[Bhandari et al 2013][research_bhandari_thomas_2013]] [[Bian et al 2018][research_bian_nener_2018]] [[Bihrle, Jr. 1969][research_bihrlejr_1969]] [[Billec 1967][research_billec_1967]] [[Binder et al 2001][research_binder_holcomb_2001]] [[Bittrick 1984][research_bittrick_1984]] [[Black 1968][research_black_1968]] [[Bodson and Athans 1985][research_bodson_athans_1985]] [[Bohao et al 2026][research_bohao_daochun_2026]] [[Bolonkin 2005][research_bolonkin_2005]] [[bolter 0 2023][research_bolter_0_2023]] [[bolter boulter, n.¹ 2023][research_bolter_boulter_2023]] [[Bolter, Albert Ernest, 29 2007][research_bolter_albert_2007]] [[bolter, n.² 2023][research_bolter_n_2_2023]] [[Boullianne 1997][research_boullianne_1997]] [[Bourgeois][research_bourgeois]] [[Brictson et al 1969][research_brictson_ciavarelli_1969]] [[Brown 2009][research_brown_2009]] [[Brukarczyk et al 2021][research_brukarczyk_nowak_2021]] [[Buell, Jr. 1970][research_buelljr_1970]] [[Bunnell 2001][research_bunnell_2001]] [[Butler 1970][research_butler_1970]] [[C-Scan¿A Milestone for Carrier 1969][research_c_scana_milestone_1969]] [[Cai et al 2018][research_cai_cui_2018]] [[Carrier Recovery Applications and 2012][research_carrier_recovery_2012]] [[Chai and Mason 1996][research_chai_mason_1996]] [[Chaloff et al 1974][research_chaloff_hiyama_1974]] [[Chang and Ai 2026][research_chang_ai_2026]] [[Chapter 1. "Under the 2017][research_chapter_1_2017]] [[Chen et al 2015][research_chen_han_2015]] [[Chen et al 2021][research_chen_fang_2021]] [[Chen et al 2024][research_chen_xu_2024]] [[Chen et al 2026][research_chen_zhang_2026]] [[Cheng et al 2021][research_cheng_cao_2021]] [[Chernenko and Burnashev 2022][research_chernenko_burnashev_2022]] [[Chester 1995][research_chester_1995]] [[Citurs and Caton 1985][research_citurs_caton_1985]] [[Clark 1965][research_clark_1965]] [[Clarkson 1991][research_clarkson_1991]] [[Cochrane and Whitman 1987][research_cochrane_whitman_1987]] [[Cockburn 1965][research_cockburn_1965]] [[Collins et al 2025][research_collins_kochersberger_2025]] [[Collyer et al 1980][research_collyer_ricard_1980]] [[Colwell 1966][research_colwell_1966]] [[Comandur et al 2019][research_comandur_walters_2019]] [[Connelly 1982][research_connelly_1982]] [[Connelly 1983][research_connelly_1983]] [[Coutard et al 2011][research_coutard_chaumette_2011]] [[Crashworthy landing gear for 1998][research_crashworthy_landing_1998]] [[Currey 1988][research_currey_1988]] [[Dai et al 2016][research_dai_wei_2016]] [[Daly 1994][research_daly_1994]] [[Daughetee 1974][research_daughetee_1974]] [[De Lellis et al 2013][research_delellis_divito_2013]] [[Deja et al 2022][research_deja_dayyani_2022]] [[Denny 2003][research_denny_2003]] [[Development of algorithmic support 2022][research_development_of_2022]] [[Dewispelare and Stager 1981][research_dewispelare_stager_1981]] [[DeWispelare and Stager 1983][research_dewispelare_stager_1983]] [[Di̇nç 2021][research_dinc_2021]] [[Dong et al 2021][research_dong_shao_2021]] [[Donley 1980][research_donley_1980]] [[Douglas Aircraft Co Long Beach Ca 1963][research_douglasaircraftcolongbeachca_1963]] [[Du and Yang 2004][research_du_yang_2004]] [[Duan et al 2022][research_duan_chen_2022]] [[Durand and Teper 1964][research_durand_teper_1964]] [[Durand and Wasicko 1965][research_durand_wasicko_1965]] [[Durmuşoğlu 2026][research_durmusoglu_2026]] [[Dynnikov 2020][research_dynnikov_2020]] [[Eigenmann et al 1984][research_eigenmann_kitzmiller_1984]] [[Elliott and Dogan 2009][research_elliott_dogan_2009]] [[Epp 2024][research_epp_2024]] [[Evaluation of the navigation 1979][research_evaluation_of_1979]] [[Ferrier et al 2000][research_ferrier_baitis_2000]] [[Ferrier et al 2006][research_ferrier_duncan_2006]] [[Ferrier et al 2015][research_ferrier_ernst_2015]] [[Fezans and Jann 2017][research_fezans_jann_2017]] [[Field and Rossitto 1999][research_field_rossitto_1999]] [[Fong and Self][research_fong_self]] [[Fracture of an Aluminum 2019][research_fracture_of_2019]] [[Frost et al 2002][research_frost_franklin_2002]] [[Frost et al 2021][research_frost_walters_2021]] [[Frounfelker and Belencan 1984][research_frounfelker_belencan_1984]] [[Furnish and Anders 1971][research_furnish_anders_1971]] [[Gan et al 2021][research_gan_fang_2021]] [[Gao et al 2024][research_gao_luo_2024]] [[Georghiou et al 1986][research_georghiou_metcalfe_1986]] [[Ghiringhelli 2000][research_ghiringhelli_2000]] [[Ghosh Dastidar and Frazzoli 2011][research_ghoshdastidar_frazzoli_2011]] [[Gibson et al 1968][research_gibson_alexander_1968]] [[Gillman 2015][research_gillman_2015]] [[Gold 1973][research_gold_1973]] [[Gold 1974][research_gold_1974]] [[Gold and Walchli 1974][research_gold_walchli_1974]] [[Grantham and Williams 1987][research_grantham_williams_1987]] [[Grasso 1994][research_grasso_1994]] [[Green and Findlay 2016][research_green_findlay_2016]] [[Guide for Installation of][research_guide_for]] [[Guo et al 2006][research_guo_yamamoto_2006]] [[Guo et al 2013][research_guo_cain_2013]] [[Guo et al 2023][research_guo_han_2023]] [[Guth 2015][research_guth_2015]] [[Gutt et al 2004][research_gutt_fischer_2004]] [[Han et al 2019][research_han_kang_2019]] [[Han et al 2026][research_han_zou_2026]] [[Harper 1936][research_harper_1936]] [[Harris 1961][research_harris_1961]] [[Harting 1981][research_harting_1981]] [[He et al 2004][research_he_xin_2004]] [[Heffley 1986][research_heffley_1986]] [[Heller and Dobrzynski 1976][research_heller_dobrzynski_1976]] [[Hess 2019][research_hess_2019]] [[Historical Design Information of][research_historical_design]] [[Horn 1973][research_horn_1973]] [[Howie and Frizzell][research_howie_frizzell]] [[Hsin 1973][research_hsin_1973]] [[Hsin 1974][research_hsin_1974]] [[Hui 2016][research_hui_2016]] [[Human Catapult Managing Relationships 2014][research_human_catapult_2014]] [[Human factors review of 1982][research_human_factors_1982]] [[Humphreys et al 1988][research_humphreys_paulsonjr_1988]] [[Huntington and Lyrintzis 1996][research_huntington_lyrintzis_1996]] [[Huntington and Lyrintzis 1998][research_huntington_lyrintzis_1998]] [[Jia et al 2011][research_jia_han_2011]] [[Jiang et al 2013][research_jiang_zhu_2013]] [[Jiang et al 2018][research_jiang_zhen_2018]] [[Jie et al 2017][research_jie_wenhai_2017]] [[Jing and Zheng-Chun 2015][research_jing_zhengchun_2015]] [[Johnstone 1968][research_johnstone_1968]] [[Juang * and Chio 2005][research_juang_chio_2005]] [[Kansas Univ Lawrence 1952][research_kansasunivlawrence_1952_b]] [[Kaplan and Sargent 1970][research_kaplan_sargent_1970]] [[Katz 2017][research_katz_2017]] [[Katz 2025][research_katz_2025]] [[Katzenstein and Bjornstad 1987][research_katzenstein_bjornstad_1987]] [[Kaur][research_kaur]] [[Ke et al 2014][research_ke_zhengzhong_2014]] [[Kennedy and Floyd D. 1985][research_kennedy_floydd_1985]] [[Kewley et al 2016][research_kewley_lowenberg_2016]] [[Kim and Costello 2016][research_kim_costello_2016]] [[Kirnon et al 2019][research_kirnon_majar_2019]] [[Kitts and Lucas 1963][research_kitts_lucas_1963]] [[Knowles et al 2012][research_knowles_krauskopf_2012]] [[Koo et al 2015][research_koo_kim_2015]] [[Kowal][research_kowal]] [[Kozłowski and Bołoz 2024][research_kozlowski_boloz_2024]] [[Krabacher 1993][research_krabacher_1993]] [[Krammer et al 2021][research_krammer_scherer_2021]] [[Krüger et al 1997][research_kruger_besselink_1997]] [[Lampton et al 2018][research_lampton_gray_2018]] [[Landing GEAR - Aircraft][research_landing_gear]] [[Landing Gear Fatigue Spectrum][research_landing_gear_c]] [[Landing Gear Shock Absorption][research_landing_gear_b]] [[Lee and Chiou 1994][research_lee_chiou_1994]] [[Lee et al 1998][research_lee_shim_1998]] [[Lehman 1964][research_lehman_1964]] [[Lehman 1965][research_lehman_1965]] [[Lehman 1966][research_lehman_1966]] [[Li 2020][research_li_2020]] [[Li and Maiorova 2022][research_li_maiorova_2022]] [[Li et al 2012][research_li_zhu_2012]] [[Li et al 2014][research_li_li_2014_b]] [[Li et al 2021][research_li_gao_2021]] [[Li et al 2024][research_li_yang_2024]] [[Lighthill 1963][research_lighthill_1963]] [[Lin et al 2015][research_lin_garratt_2015]] [[Lin et al 2017][research_lin_wang_2017]] [[Linn and Langlois 2006][research_linn_langlois_2006]] [[Lintern 1984][research_lintern_1984]] [[Lion 1966][research_lion_1966]] [[Lisauskas et al 2015][research_lisauskas_poska_2015]] [[Liu and Fan 2025][research_liu_fan_2025]] [[Liu et al 2023][research_liu_liu_2023]] [[Liu et al 2023][research_liu_wang_2023]] [[Liu et al 2026][research_liu_zhu_2026]] [[Lorenzetti et al 2020][research_lorenzetti_mcclellan_2020]] [[Lu et al 2014][research_lu_tan_2014]] [[Lu et al 2014][research_lu_zhang_2014]] [[Lu et al 2020][research_lu_wang_2020]] [[Lu et al 2022][research_lu_zhu_2022]] [[Lu et al 2025][research_lu_yan_2025]] [[Luo and Duan 2014][research_luo_duan_2014]] [[Luong et al 2025][research_luong_le_2025]] [[Lv et al 2011][research_lv_zhu_2011]] [[Lykken and Shah 1972][research_lykken_shah_1972]] [[Makarenko et al 2017][research_makarenko_makarov_2017]] [[Martin and Irani 2022][research_martin_irani_2022]] [[Martorella et al 1981][research_martorella_kelly_1981]] [[Mayer 2000][research_mayer_2000]] [[Mcdonald 1980][research_mcdonald_1980]] [[McDonald et al 2020][research_mcdonald_richards_2020]] [[McMuldroch et al 1979][research_mcmuldroch_stein_1979]] [[McRoberts et al 2015][research_mcroberts_early_2015]] [[Menon and Walker 1984][research_menon_walker_1984]] [[Menon and Walker 1985][research_menon_walker_1985]] [[Michini and How 2011][research_michini_how_2011]] [[Micklos 1991][research_micklos_1991]] [[Miles and Lepping 1962][research_miles_lepping_1962]] [[Miller 1969][research_miller_1969]] [[Miller 1970][research_miller_1970]] [[Mine roof bolting machine 2010][research_mine_roof_2010]] [[Mirabile][research_mirabile]] [[Misra and Bai 2018][research_misra_bai_2018]] [[Mitchell and Hoh 1983][research_mitchell_hoh_1983]] [[Morrison et al][research_morrison_zahraee]] [[Murray-Smith 1995][research_murraysmith_1995]] [[Nastasi et al 1983][research_nastasi_martorella_1983]] [[Naval Air Systems Command Washington Dc 1978][research_navalairsystemscommandwashingtondc_1978]] [[Naval Air Systems Command Washington Dc 1980][research_navalairsystemscommandwashingtondc_1980]] [[Nave 1973][research_nave_1973]] [[Negre 1975][research_negre_1975]] [[Nengjian Wang et al 2016][research_nengjianwang_xiangleimeng_2016]] [[New steam catapult for 1952][research_new_steam_1952]] [[Ngo and Sultan 2024][research_ngo_sultan_2024]] [[Novakovic et al 2016][research_novakovic_vasic_2016]] [[Nowak et al 2022][research_nowak_kopecki_2022]] [[Obye and Hakim 1984][research_obye_hakim_1984]] [[Overview of Aircraft Landing][research_overview_of]] [[Pan and Pi 2024][research_pan_pi_2024]] [[Peer 2000][research_peer_2000]] [[Peng et al 2020][research_peng_xie_2020]] [[Perry and Schneider 1984][research_perry_schneider_1984]] [[Peterson et al 1963][research_peterson_gipe_1963]] [[Photometric characteristics of U.S 1968][research_photometric_characteristics_1968]] [[Pollack 2013][research_pollack_2013]] [[Pomarolli 1965][research_pomarolli_1965]] [[Powers et al 2015][research_powers_mclaughlin_2015]] [[Powers et al 2018][research_powers_mclaughlin_2018]] [[Prabha and Raghavendra 2021][research_prabha_raghavendra_2021]] [[Prasad et al 2018][research_prasad_comandur_2018]] [[Purdy 2010][research_purdy_2010]] [[Qi et al 2018][research_qi_zhao_2018]] [[Ramsey and Dixon 1967][research_ramsey_dixon_1967]] [[Raychaudhuri][research_raychaudhuri]] [[Rebel 2000][research_rebel_2000]] [[Redesigned aircraft landing gear 1987][research_redesigned_aircraft_1987]] [[Redesigning landing gear for 2001][research_redesigning_landing_2001]] [[Ren et al 2024][research_ren_man_2024]] [[Richards and Tate 2023][research_richards_tate_2023]] [[Ridha 1968][research_ridha_1968]] [[Rinkinen 1959][research_rinkinen_1959]] [[Robinson 1992][research_robinson_1992]] [[roof bolter 2014][research_roof_bolter_2014]] [[Roof bolting machine operators 2006][research_roof_bolting_2006]] [[Rudowsky et al 2002][research_rudowsky_hynes_2002]] [[Ruiyang et al 2020][research_ruiyang_konstantin_2020]] [[Rupert 2008][research_rupert_2008]] [[Ryan et al 2011][research_ryan_cummings_2011]] [[Ryan et al 2014][research_ryan_banerjee_2014]] [[Sankar 2012][research_sankar_2012]] [[Sasoh et al 2015][research_sasoh_imaizumi_2015]] [[Schallhorn 2020][research_schallhorn_2020]] [[Schmidt 2015][research_schmidt_2015]] [[Schmidt 2021][research_schmidt_2021]] [[Schoenman and Doniger 1965][research_schoenman_doniger_1965]] [[Scholz et al 2026][research_scholz_theuser_2026]] [[Schultz et al 2009][research_schultz_mcgrath_2009]] [[Schwartz 1975][research_schwartz_1975]] [[Shao et al 2023][research_shao_li_2023]] [[Shao et al 2026][research_shao_li_2026]] [[Sharma et al 2021][research_sharma_padthe_2021]] [[Shaw 1960][research_shaw_1960]] [[Shayler 1961][research_shayler_1961]] [[Sheppard and Foster 2008][research_sheppard_foster_2008]] [[Shimski et al 2013][research_shimski_schmidt_2013]] [[Siegel and Crain 1960][research_siegel_crain_1960]] [[Sivaramakrishnan 1981][research_sivaramakrishnan_1981]] [[Smith and Chow 1998][research_smith_chow_1998]] [[Stachiw][research_stachiw]] [[Stachiw et al 2020][research_stachiw_khouli_2020]] [[Stachiw et al 2021][research_stachiw_khouli_2021]] [[Standard Specification for Light][research_standard_specification]] [[Standard Specification for Light][research_standard_specification_b]] [[Steinberg and Page 2001][research_steinberg_page_2001]] [[Streamline development of aircraft 2009][research_streamline_development_2009]] [[Strietzel and Shefler 1963][research_strietzel_shefler_1963]] [[Structure with carrier suitability 1974][research_structure_with_1974]] [[Suggett 1960][research_suggett_1960]] [[Sullings and Waller 1967][research_sullings_waller_1967]] [[Sun 2026][research_sun_2026]] [[Sun et al 2022][research_sun_zhang_2022]] [[Syd S. Peng 2001][research_sydspeng_2001]] [[Syd S. Peng 2002][research_sydspeng_2002]] [[Syd S. Peng 2002][research_sydspeng_2002_b]] [[Syd S. Peng 2003][research_sydspeng_2003]] [[Syd S. Peng 2004][research_sydspeng_2004]] [[Syd S. Peng 2005][research_sydspeng_2005]] [[Tang and Lai 2020][research_tang_lai_2020]] [[Technology News 523 2007][research_technology_news_2007]] [[Technology News 559 2017][research_technology_news_2017]] [[Technology News 560 2017][research_technology_news_2017_b]] [[Teledyne Ryan Aeronautical San Diego Ca 1974][research_teledyneryanaeronauticalsandiegoca_1974]] [[Templeman and Parker 1968][research_templeman_parker_1968]] [[Tests, Impact, Shock Absorber][research_tests_impact]] [[The Catapult][research_the_catapult]] [[The Culture Catapult][research_the_culture]] [[The WAVE OFF][research_the_wave]] [[Thiele 1965][research_thiele_1965]] [[Thota et al 2008][research_thota_krauskopf_2008]] [[Torres et al 2023][research_torres_harris_2023]] [[Tugolukov 2020][research_tugolukov_2020]] [[van Slagmaat 1992][research_vanslagmaat_1992]] [[van Slagmaat 2004][research_vanslagmaat_2004]] [[van Slagmaat 2026][research_vanslagmaat_2026]] [[Wang 2016][research_wang_2016]] [[Wang 2022][research_wang_2022]] [[Wang and Carl 1999][research_wang_carl_1999]] [[Wang et al 2019][research_wang_yin_2019]] [[Wang et al 2021][research_wang_lu_2021]] [[Wang et al 2023][research_wang_liu_2023]] [[Wang et al 2024][research_wang_yuan_2024]] [[Ward et al 1999][research_ward_monaco_1999]] [[Webb and Nolan 1954][research_webb_nolan_1954]] [[Weingarten and Chalk 1982][research_weingarten_chalk_1982]] [[Wen et al 2009][research_wen_zhi_2009]] [[Westra et al 1981][research_westra_simon_1981]] [[Westra et al 1986][research_westra_lintern_1986]] [[Whitehead 1960][research_whitehead_1960]] [[Wilson 2018][research_wilson_2018]] [[Witherell 1992][research_witherell_1992]] [[Wu and Zhu 2024][research_wu_zhu_2024]] [[Wu et al 2018][research_wu_song_2018]] [[Xiao et al 2024][research_xiao_zhen_2024]] [[Xu et al 2025][research_xu_hong_2025]] [[Yakimenko et al 2002][research_yakimenko_kaminer_2002]] [[Yanagihara et al 1999][research_yanagihara_shigemi_1999]] [[Yang 1970][research_yang_1970]] [[Yang 1971][research_yang_1971]] [[Yang et al 2010][research_yang_garratt_2010]] [[Yang et al 2026][research_yang_jiang_2026]] [[Yawei Liang][research_yaweiliang]] [[Yilmaz and alaiwi 2024][research_yilmaz_alaiwi_2024]] [[Yin et al 2025][research_yin_ni_2025]] [[Yoo et al 2013][research_yoo_cho_2013]] [[Yoo et al 2014][research_yoo_chihoonlee_2014]] [[Yoo et al 2015][research_yoo_park_2015]] [[Young Jr 2002][research_youngjr_2002]] [[Yu et al 2022][research_yu_hu_2022]] [[Yuan et al 2011][research_yuan_xi_2011]] [[Yuan et al 2017][research_yuan_zhao_2017]] [[Yuan et al 2025][research_yuan_wang_2025]] [[Zakrajsek et al 2017][research_zakrajsek_vogel_2017]] [[Zeng et al 2025][research_zeng_li_2025]] [[Zhang and Guo 2024][research_zhang_guo_2024]] [[Zhang et al 2014][research_zhang_zou_2014]] [[Zhang et al 2015][research_zhang_lin_2015]] [[Zhang et al 2022][research_zhang_peng_2022]] [[Zhang et al 2022][research_zhang_peng_2022_b]] [[Zhang et al 2023][research_zhang_wang_2023]] [[Zhang et al 2023][research_zhang_wang_2023_d]] [[Zhang et al 2025][research_zhang_ma_2025]] [[Zhang et al 2025][research_zhang_song_2025]] [[Zhang et al 2025][research_zhang_wang_2025]] [[Zhang et al 2025][research_zhang_wang_2025_b]] [[Zhang et al 2026][research_zhang_chen_2026]] [[Zhang et al 2026][research_zhang_chen_2026_b]] [[Zhao et al 2012][research_zhao_li_2012]] [[Zhao et al 2018][research_zhao_krishnamurthi_2018]] [[Zhao et al 2018][research_zhao_krishnamurthi_2018_b]] [[Zhao et al 2019][research_zhao_mishra_2019]] [[Zhen et al 2018][research_zhen_tao_2018]] [[Zheng et al 2013][research_zheng_gong_2013]] [[Zhicong and Voronko 2023][research_zhicong_voronko_2023]] [[Zhimin and Guanxin 2013][research_zhimin_guanxin_2013]] [[Zhimin and Guanxin 2014][research_zhimin_guanxin_2014]] [[Zhou and Huang 2020][research_zhou_huang_2020]] [[Zhou et al 2024][research_zhou_zhang_2024]] [[Zhu 2024][research_zhu_2024]] [[Zhu and Qiu 2013][research_zhu_qiu_2013]] [[Zhu Bin et al 2018][research_zhubin_kepeng_2018]] [[Zhu et al 2012][research_zhu_zhao_2012]] [[Zhu et al 2018][research_zhu_lu_2018]] [[Zhu et al 2019][research_zhu_lu_2019]] [[Zhu et al 2022][research_zhu_zhang_2022]]

### Autonomy, mission management and onboard decision making

**What the X-45A's software blocks were actually delivering.** Mission management architectures, onboard replanning, contingency handling, deliberative and reactive planning, and the long argument about what autonomy means when the word is used as a selling point. **The programme's milestones were all software milestones after the first year**, and this is the field those milestones were drawn from.

**241 records.** [[Aburime][research_aburime]] [[Adhikari 2021][research_adhikari_2021]] [[Adhikari 2021][research_adhikari_2021_b]] [[Aguiar and Pascoal 2012][research_aguiar_pascoal_2012]] [[Ahmed et al 2026][research_ahmed_stanziano_2026]] [[Alijani and Osman 2021][research_alijani_osman_2021]] [[Alonso da Silva 2019][research_alonsodasilva_2019]] [[Alsayed et al 2022][research_alsayed_nabawy_2022]] [[An et al 2023][research_an_krzysiak_2023]] [[Arora et al 2022][research_arora_carlson_2022]] [[Ashokkumar 2023][research_ashokkumar_2023]] [[Attitude control system of 1994][research_attitude_control_1994]] [[Automation and Autonomy in 2016][research_automation_and_2016]] [[Autonomous Control of Unmanned 2012][research_autonomous_control_2012]] [[Autonomous Control of Unmanned 2019][research_autonomous_control_2019]] [[Autonomous unmanned aircraft RandD 1994][research_autonomous_unmanned_1994]] [[Barbier and Chanthery 2004][research_barbier_chanthery_2004]] [[Bardhan et al 2017][research_bardhan_bera_2017]] [[Barlow 2004][research_barlow_2004]] [[Barnhart 2012][research_barnhart_2012]] [[Bestaoui and Lakhlef 2013][research_bestaoui_lakhlef_2013]] [[Bhatia et al 2021][research_bhatia_jiang_2021]] [[Bil et al 2015][research_bil_zegers_2015]] [[Boskovic and Redding 2009][research_boskovic_redding_2009]] [[Brinker 2004][research_brinker_2004]] [[Brockett et al 2002][research_brockett_laux_2002]] [[Bryant et al 2015][research_bryant_gradwell_2015]] [[Bulka and Nahon 2017][research_bulka_nahon_2017]] [[Cappuzzo et al 2022][research_cappuzzo_bianchi_2022]] [[Castillo-Effen and Visnevski 2009][research_castilloeffen_visnevski_2009]] [[Cetin and Yilmaz 2013][research_cetin_yilmaz_2013]] [[Cetin et al 2010][research_cetin_kurnaz_2010]] [[Chakrabarty et al 2016][research_chakrabarty_morris_2016]] [[Chalenski et al 2018][research_chalenski_hatchell_2018]] [[Chapter 3 Autonomous UAVs 2021][research_chapter_3_2021]] [[Chen and Duan 2016][research_chen_duan_2016]] [[Chen et al 2025][research_chen_fang_2025]] [[Civil Regulation Of Autonomous 2024][research_civil_regulation_2024]] [[Clare et al 2012][research_clare_macbeth_2012]] [[Clough 2003][research_clough_2003]] [[Cooper and Ravela 2024][research_cooper_ravela_2024]] [[Dai et al 2018][research_dai_quan_2018]] [[Dai et al 2020][research_dai_wei_2020]] [[de Paula et al 2025][research_depaula_dwivedi_2025]] [[Design, control, and autonomous][research_design_control_and]] [[Di et al 2022][research_di_mishra_2022]] [[Doherty et al 2023][research_doherty_costello_2023]] [[Drusinsky et al 2022][research_drusinsky_michael_2022]] [[Duan et al 2021][research_duan_sun_2021]] [[Duncan et al 2006][research_duncan_ferrier_2006]] [[Duraklar 2024][research_duraklar_2024]] [[Eubank and Atkins 2011][research_eubank_atkins_2011]] [[Frau 2022][research_frau_2022]] [[Frew and Lawrence 2005][research_frew_lawrence_2005]] [[Fu et al 2014][research_fu_carrio_2014]] [[Fukuda and Takimoto 2014][research_fukuda_takimoto_2014]] [[Further development and flight 1994][research_further_development_1994]] [[Galway 2008][research_galway_2008]] [[Galway 2008][research_galway_2008_b]] [[Garcia et al 2017][research_garcia_keshmiri_2017]] [[Garcia et al 2020][research_garcia_caballero_2020]] [[Gardi et al 2015][research_gardi_ramasamy_2015]] [[Gautam et al 2014][research_gautam_sujit_2014]] [[Getir Yaman et al 2025][research_getiryaman_ribeiro_2025]] [[Gu and Enoiu 2023][research_gu_enoiu_2023]] [[Guelman 2014][research_guelman_2014]] [[Guide for Unmanned Undersea][research_guide_for_b]] [[Gunawardana and Alonso 2013][research_gunawardana_alonso_2013]] [[Gunetti et al 2013][research_gunetti_thompson_2013]] [[Gürsoylu et al 2025][research_gursoylu_sziroczak_2025]] [[Hagele and Soffker 2017][research_hagele_soffker_2017]] [[Hauschildt et al 1981][research_hauschildt_gripp_1981]] [[Herbst and Klöckner 2014][research_herbst_klockner_2014]] [[Hewgley et al 2011][research_hewgley_yakimenko_2011]] [[Hewgley et al 2014][research_hewgley_cristi_2014]] [[Hinchey et al][research_hinchey_rash]] [[Hirsch and Schroeder 2014][research_hirsch_schroeder_2014]] [[Hopchak et al 2022][research_hopchak_davis_2022]] [[Horn et al 2014][research_horn_tritschler_2014]] [[Horn et al 2015][research_horn_tritschler_2015]] [[Horowitz et al 2014][research_horowitz_beling_2014]] [[Hu et al 2018][research_hu_wu_2018]] [[Huang et al 2019][research_huang_zhu_2019]] [[Huang et al 2019][research_huang_zhu_2019_b]] [[Huang et al 2019][research_huang_zhu_2019_c]] [[Jabbal 2015][research_jabbal_2015]] [[Jahangirova et al 2021][research_jahangirova_stocco_2021]] [[Jiang et al 2016][research_jiang_stol_2016]] [[Johansen and Perez 2016][research_johansen_perez_2016]] [[Jones and Dye 2016][research_jones_dye_2016]] [[K. Senthil Kumar and J. Shanmugam 2023][research_ksenthilkumar_jshanmugam_2023]] [[Kaidan 2026][research_kaidan_2026]] [[Kannan and Min 2022][research_kannan_min_2022]] [[Kartal and Yüksek 2025][research_kartal_yuksek_2025]] [[Karásek et al 2026][research_karasek_kallies_2026]] [[Ke et al 2009][research_ke_tsourdos_2009]] [[Keke et al 2014][research_keke_qing_2014]] [[Keong et al 2019][research_keong_shin_2019]] [[Khanafseh and Pervan 2007][research_khanafseh_pervan_2007]] [[Kim et al 2022][research_kim_gregory_2022]] [[Koh and Paranjape 2020][research_koh_paranjape_2020]] [[Konert and Balcerzak 2021][research_konert_balcerzak_2021]] [[Koo and Sastry 2003][research_koo_sastry_2003]] [[Kopeikin et al 2013][research_kopeikin_ponda_2013]] [[Kotsinis et al 2026][research_kotsinis_karras_2026]] [[Krishna Kamath et al 2020][research_krishnakamath_kumartripathi_2020]] [[Krozel and Andrisani 1990][research_krozel_andrisani_1990]] [[Kurnaz et al][research_kurnaz_cetin]] [[Kwon et al 2013][research_kwon_yoder_2013]] [[Lee et al 2018][research_lee_shim_2018]] [[Lee et al 2026][research_lee_lowe_2026]] [[Leira et al 2017][research_leira_johansen_2017]] [[Li 2017][research_li_2017]] [[Li and Chen 2003][research_li_chen_2003]] [[Lin et al 2019][research_lin_yang_2019]] [[Linne 2022][research_linne_2022]] [[Liu and Valavanis 2026][research_liu_valavanis_2026]] [[Liu et al 2019][research_liu_he_2019]] [[Liu et al 2023][research_liu_li_2023]] [[Liu et al 2025][research_liu_huang_2025]] [[Liu et al 2026][research_liu_huang_2026]] [[Lowe et al 2026][research_lowe_torshizi_2026]] [[Lugo and Zell 2013][research_lugo_zell_2013]] [[Lungu et al 2022][research_lungu_flores_2022]] [[Mammadov and Gueaieb 2014][research_mammadov_gueaieb_2014]] [[Martinez et al 2013][research_martinez_richardson_2013]] [[Marwaha et al 2009][research_marwaha_valasek_2009]] [[McGarey and Saripalli 2013][research_mcgarey_saripalli_2013]] [[McManus and Walker 2006][research_mcmanus_walker_2006]] [[Mejias 2014][research_mejias_2014]] [[Miller et al 2023][research_miller_mwaffo_2023]] [[Morris et al 2005][research_morris_frew_2005]] [[Murillo et al 2025][research_murillo_montes_2025]] [[Müller and Bauer 2024][research_muller_bauer_2024]] [[Niendorf et al 2012][research_niendorf_adolf_2012]] [[Nieuwenhuisen et al 2014][research_nieuwenhuisen_droeschel_2014]] [[Nijveldt and Ijtsma 2022][research_nijveldt_ijtsma_2022]] [[Nikolaidis et al 2025][research_nikolaidis_laoudias_2025]] [[Ogorzalek et al 2019][research_ogorzalek_doyle_2019]] [[Oktay and Eraslan 2024][research_oktay_eraslan_2024]] [[Opening up civil airspace 2007][research_opening_up_2007]] [[Ordoukhanian and Madni 2019][research_ordoukhanian_madni_2019]] [[Owais et al 2022][research_owais_midtiby_2022]] [[Papa 2023][research_papa_2023]] [[Papa et al 2026][research_papa_ariante_2026]] [[Park and Bang 2022][research_park_bang_2022]] [[Patel et al 2011][research_patel_brinton_2011]] [[Patel et al 2021][research_patel_krishnamurthy_2021]] [[Pedrozo 2022][research_pedrozo_2022]] [[Peng 2021][research_peng_2021]] [[Peng et al 2016][research_peng_lin_2016]] [[Pieniążek 2003][research_pieniazek_2003]] [[Practice for Commercial Unmanned][research_practice_for]] [[Primatesta 2025][research_primatesta_2025]] [[Qu et al 2011][research_qu_li_2011]] [[Qu et al 2013][research_qu_li_2013]] [[Ramesh and Subbarao 2016][research_ramesh_subbarao_2016]] [[Rao et al 2020][research_rao_ma_2020]] [[Ren and Quan 2024][research_ren_quan_2024]] [[Ren et al 2026][research_ren_du_2026]] [[Richez and Costello 2024][research_richez_costello_2024]] [[Roberto Mati 2006][research_robertomati_2006]] [[Rodriguez-Ramos et al 2017][research_rodriguezramos_sampedro_2017]] [[Rosales et al 2021][research_rosales_reyes_2021]] [[Rumba and Nikitenko 2020][research_rumba_nikitenko_2020]] [[Sadraey 2016][research_sadraey_2016]] [[Safeer and Costello 2026][research_safeer_costello_2026]] [[Saghafi and Esmailifar 2009][research_saghafi_esmailifar_2009]] [[Saha et al 2023][research_saha_kumar_2023]] [[Saska et al 2014][research_saska_chudoba_2014]] [[Scheidt 2014][research_scheidt_2014]] [[Scherer et al 2015][research_scherer_yang_2015]] [[Schopferer and Benders 2020][research_schopferer_benders_2020]] [[Scognamiglio et al 2024][research_scognamiglio_caccavale_2024]] [[Sebestyén and Szénási 2026][research_sebestyen_szenasi_2026]] [[See et al 2017][research_see_ghosh_2017]] [[Seitzer 2003][research_seitzer_2003]] [[Sevostyanov and Devitt 2021][research_sevostyanov_devitt_2021]] [[Sevostyanov et al 2022][research_sevostyanov_devitt_2022]] [[Shanshan et al 2020][research_shanshan_ao_2020]] [[Shin et al 2013][research_shin_you_2013]] [[Shin et al 2013][research_shin_you_2013_b]] [[Silva][research_silva]] [[Skjong et al 2015][research_skjong_nundal_2015]] [[Smith][research_smith]] [[Smith et al 2026][research_smith_andersen_2026]] [[Sorensen and Johansen 2017][research_sorensen_johansen_2017]] [[Sun et al 2019][research_sun_deng_2019]] [[Sun et al 2026][research_sun_wang_2026]] [[Surono et al 2021][research_surono_ashar_2021]] [[Survivability of Unmanned Autonomous 2016][research_survivability_of_2016]] [[Sánchez López][research_sanchezlopez]] [[Tan et al 2019][research_tan_wang_2019]] [[Tanaka and Matsumoto 2019][research_tanaka_matsumoto_2019]] [[Tandale et al 2005][research_tandale_bowers_2005]] [[Tandale et al 2006][research_tandale_bowers_2006]] [[ten Have 1993][research_tenhave_1993]] [[The algorithm of the 2020][research_the_algorithm_2020]] [[The Ethics of Autonomous 2016][research_the_ethics_2016]] [[Tin et al 2020][research_tin_borowczyk_2020]] [[Tinoco][research_tinoco]] [[Tiwari et al 2020][research_tiwari_stacey_2020]] [[Torno et al 2014][research_torno_hintz_2014]] [[Tsoukalas et al 2026][research_tsoukalas_unlu_2026]] [[Tsourveloudis and Doitsidis 2025][research_tsourveloudis_doitsidis_2025]] [[Tzes et al 2023][research_tzes_tsoukalas_2023]] [[Unmanned Autonomous Vehicle 2016][research_unmanned_autonomous_2016]] [[Usach Molina][research_usachmolina]] [[Uzun 2024][research_uzun_2024]] [[Vanualailai et al 2013][research_vanualailai_sharan_2013]] [[Venugopalan et al 2012][research_venugopalan_taher_2012]] [[Vinokurov et al 1992][research_vinokurov_glinkin_1992]] [[Vinokurov et al 1993][research_vinokurov_glinkin_1993]] [[Visnevski and Castillo-Effen 2010][research_visnevski_castilloeffen_2010]] [[Wang and Wang 2018][research_wang_wang_2018]] [[Wang and Wang 2020][research_wang_wang_2020_b]] [[Wang et al 2005][research_wang_zhang_2005]] [[Wang et al 2017][research_wang_li_2017]] [[Wang et al 2022][research_wang_lin_2022]] [[Wang et al 2026][research_wang_yang_2026]] [[Webster et al 2012][research_webster_cameron_2012]] [[Wilson et al 2015][research_wilson_goktogan_2015]] [[Wu et al 2023][research_wu_luo_2023]] [[Wynn and McLain 2019][research_wynn_mclain_2019]] [[Xie et al 2019][research_xie_dong_2019]] [[Xin et al 2018][research_xin_luo_2018]] [[Xiong et al 2022][research_xiong_zhou_2022]] [[Xu 2018][research_xu_2018]] [[Yan et al 2018][research_yan_xunhua_2018]] [[Yavnai 2003][research_yavnai_2003]] [[Yomchinda 2015][research_yomchinda_2015]] [[You and Shim 2010][research_you_shim_2010]] [[Yu et al 2020][research_yu_yang_2020]] [[Yuan][research_yuan]] [[Yuan et al 2024][research_yuan_duan_2024]] [[Zhang and Li 2023][research_zhang_li_2023]] [[Zhao and Zhu 2016][research_zhao_zhu_2016]] [[Zhao et al 2018][research_zhao_currier_2018]] [[Zhao et al 2021][research_zhao_duan_2021]] [[Zhu et al 2016][research_zhu_jin_2016]] [[Çoban 2020][research_coban_2020]]

### Aircraft sizing, mission analysis and the weight estimate

**This is the cluster this article argues from, which is unusual and follows from the record.** No specification for the X-46A was published, so the analysis sizes the requirement instead of describing a vehicle, and the literature it leans on is conceptual design rather than flight test. Weight fraction estimation, the Breguet range and endurance relations, mission profile and combat radius analysis, loiter optimisation, design space exploration and multidisciplinary optimisation. **The largest cluster in this survey, because the article's keystone lives in it.**

**191 records.** [[Acerra Gil and Guimaraes 2019][research_acerragil_guimaraes_2019]] [[Acharya et al 2021][research_acharya_sinha_2021]] [[Aircraft Conceptual Design 2012][research_aircraft_conceptual_2012]] [[Aircraft Sizing, Engine Matching 2010][research_aircraft_sizing_2010]] [[Ajaj et al 2013][research_ajaj_friswell_2013]] [[Ali and Al-Shamma 2026][research_ali_alshamma_2026]] [[Altman 2015][research_altman_2015]] [[Altman 2019][research_altman_2019]] [[Amadori et al 2019][research_amadori_jouannet_2019]] [[Andrews, L. Cullen et al 1988][research_andrewslcullen_augsburgerbill_1988]] [[Ascani 1974][research_ascani_1974]] [[Autry and Victorazzo 2019][research_autry_victorazzo_2019]] [[Babetto and Stumpf 2021][research_babetto_stumpf_2021]] [[Bagdatli et al 2019][research_bagdatli_karagoz_2019]] [[Bai et al 2014][research_bai_mingqiang_2014]] [[Barton][research_barton]] [[Batill et al 1999][research_batill_stelmack_1999]] [[Bendarkar et al 2013][research_bendarkar_pant_2013]] [[Berman 1997][research_berman_1997]] [[Bindolino et al 2010][research_bindolino_ghiringhelli_2010]] [[Biswal M 2023][research_biswalm_2023]] [[Brooks and Mavris 2021][research_brooks_mavris_2021]] [[Brown And Root Development Inc Houston Tx 1983][research_brownandrootdevelopmentinchoustontx_1983]] [[Butler et al 1999][research_butler_lillico_1999]] [[Cai et al 2022][research_cai_rajaram_2022]] [[Caldwell 1963][research_caldwell_1963]] [[Carreyette 1950][research_carreyette_1950]] [[Cavagna et al 2009][research_cavagna_ricci_2009]] [[Cavagna et al 2010][research_cavagna_ricci_2010]] [[Cavagna et al 2011][research_cavagna_ricci_2011]] [[Centracchio et al 2018][research_centracchio_rossetti_2018]] [[Cestino 2006][research_cestino_2006]] [[Chai et al 1995][research_chai_crisafulli_1995]] [[Chakraborty et al 2014][research_chakraborty_trawick_2014]] [[Chaput 1987][research_chaput_1987]] [[Chen et al 2023][research_chen_han_2023_b]] [[Chiesa et al 1999][research_chiesa_disciuva_1999]] [[Colozza, Anthony and Dolce, James 2003][research_colozzaanthony_dolcejames_2003]] [[Commercial Aircraft Hydraulic System][research_commercial_aircraft]] [[Conceptual Design Examples 2024][research_conceptual_design_2024]] [[Control authority assessment in 1993][research_control_authority_1993]] [[Crossley et al 2011][research_crossley_skillen_2011]] [[Dannenhoffer 1981][research_dannenhoffer_1981]] [[de Carvalho Bertoli et al 2016][research_decarvalhobertoli_adabo_2016]] [[DeBilzan 1975][research_debilzan_1975]] [[Demarchi and Haning 1978][research_demarchi_haning_1978]] [[Doguet and Rancourt 2023][research_doguet_rancourt_2023]] [[Early Conceptual Design 2013][research_early_conceptual_2013]] [[Ender and McClure 2002][research_ender_mcclure_2002]] [[Esdras and Liscouet-Hanke 2013][research_esdras_liscouethanke_2013]] [[Essari 2018][research_essari_2018]] [[Essari 2018][research_essari_2018_b]] [[Essari and Ghatus 2023][research_essari_ghatus_2023]] [[Fielding and Vaziry-Z 1995][research_fielding_vaziryz_1995]] [[Fladeland, Matt et al 2019][research_fladelandmatt_schoenungsusan_2019]] [[Foss, W. E., Jr. 1981][research_fosswejr_1981]] [[Foss, W. E.., Jr. 1984][research_fosswejr_1984]] [[Frulla 2021][research_frulla_2021]] [[G et al 2024][research_g_gowda_2024]] [[Gabriele 1991][research_gabriele_1991]] [[Gardner and Poehlman 1999][research_gardner_poehlman_1999]] [[Gates 1949][research_gates_1949]] [[Giles 1995][research_giles_1995]] [[Gilhool 2005][research_gilhool_2005]] [[Golombek et al 2025][research_golombek_bustamante_2025]] [[Golombek et al 2026][research_golombek_bustamante_2026]] [[Goyal 2026][research_goyal_2026]] [[Green and Zanine 1984][research_green_zanine_1984]] [[Gregory, T. J. and Wilcox, D. E. 1970][research_gregorytj_wilcoxde_1970]] [[Gudmundsson 2014][research_gudmundsson_2014]] [[Gudmundsson 2022][research_gudmundsson_2022]] [[Hayase 1974][research_hayase_1974]] [[Hayase 1974][research_hayase_1974_b]] [[Heit and Liscouet-Hanke 2023][research_heit_liscouethanke_2023]] [[Heller 1961][research_heller_1961]] [[High-Altitude Long-Endurance HALE Sensor 2026][research_high_altitude_long_endurance_2026]] [[Hiyama 1974][research_hiyama_1974]] [[Hiyama 1974][research_hiyama_1974_b]] [[Hon et al 2022][research_hon_karpuk_2022]] [[Horvath and Wells 2018][research_horvath_wells_2018]] [[Howe 2000][research_howe_2000_b]] [[Ibrahim 2011][research_ibrahim_2011]] [[Ingram et al 2015][research_ingram_dendinger_2015]] [[Initial Sizing 2024][research_initial_sizing_2024]] [[Initial Tail Sizing 2013][research_initial_tail_2013]] [[Initial Unmanned Aircraft Sizing 2014][research_initial_unmanned_2014]] [[Initial Unmanned-Aircraft Sizing 2012][research_initial_unmanned_aircraft_2012]] [[James Joseph et al][research_jamesjoseph_davidjkinney]] [[James Joseph et al][research_jamesjoseph_davidjkinney_b]] [[Johnson 1985][research_johnson_1985]] [[Jun et al 2003][research_jun_tischler_2003]] [[Kai et al 2026][research_kai_binghong_2026]] [[Kao et al 2018][research_kao_white_2018]] [[Karagoz et al 2019][research_karagoz_reilley_2019]] [[Karpuk 2026][research_karpuk_2026]] [[Kei̇yi̇nci̇ and Aydin 2021][research_keiyinci_aydin_2021]] [[Kottapalli, Anjaney P. and Harris, Franklin D. 2012][research_kottapallianjaneyp_harrisfranklind_2012]] [[Krengel et al 2019][research_krengel_hepperle_2019]] [[Kroo 1983][research_kroo_1983]] [[Lehovec 1979][research_lehovec_1979]] [[Lehovec 1980][research_lehovec_1980]] [[Liscouet-Hanke and Huynh 2013][research_liscouethanke_huynh_2013]] [[Liu and Wu 2003][research_liu_wu_2003]] [[Liu, G. C. et al 1983][research_liugc_morriscekjr_1983]] [[Logan 1989][research_logan_1989]] [[Ma et al 2022][research_ma_yan_2022]] [[Martindale et al 1974][research_martindale_rockwell_1974]] [[Min Tint 2018][research_mintint_2018]] [[Mokotoff et al 2025][research_mokotoff_arnson_2025]] [[Mokotoff et al 2026][research_mokotoff_arnson_2026]] [[Myers 1973][research_myers_1973]] [[Myers 1974][research_myers_1974]] [[Myklebust and Gelhausen 1993][research_myklebust_gelhausen_1993]] [[Nam and Mavris 2018][research_nam_mavris_2018]] [[Naval Applied Science Lab Brooklyn Ny 1963][research_navalappliedsciencelabbrooklynny_1963]] [[Neufeld 2021][research_neufeld_2021]] [[Newberry 1998][research_newberry_1998]] [[Nickol, Craig L. et al 2007][research_nickolcraigl_guynnmarkd_2007]] [[Nigam et al 2015][research_nigam_ayyalasomayajula_2015]] [[Onat and Tolle 1979][research_onat_tolle_1979]] [[Oole 1993][research_oole_1993]] [[Palaia et al 2025][research_palaia_salem_2025]] [[Park 2025][research_park_2025]] [[Park et al 2025][research_park_jeong_2025]] [[Parker 1986][research_parker_1986]] [[Patterson 1989][research_patterson_1989]] [[Peterson and Taboada 2012][research_peterson_taboada_2012]] [[Preliminary Estimate of Takeoff 2010][research_preliminary_estimate_2010]] [[Preliminary Fuselage Sizing and 2010][research_preliminary_fuselage_2010]] [[Preliminary Sizing of the 2010][research_preliminary_sizing_2010]] [[Probst 2010][research_probst_2010]] [[R H et al 2020][research_rh_vp_2020]] [[Raczkowski et al 2026][research_raczkowski_boyd_2026]] [[Rajpal and Pant 2011][research_rajpal_pant_2011]] [[Raymer 1992][research_raymer_1992]] [[Raymer 1998][research_raymer_1998]] [[Rodriguez and Liscouët-Hanke 2025][research_rodriguez_liscouethanke_2025]] [[Rosenstein 1989][research_rosenstein_1989]] [[Roskam 1985][research_roskam_1985]] [[Sadraey 2014][research_sadraey_2014]] [[Sadraey 2016][research_sadraey_2016_b]] [[Sagdeo 1990][research_sagdeo_1990]] [[Samareh, Jamshid A. et al 2006][research_samarehjamshida_sensmeiermarkd_2006]] [[Sanchez-Carmona and Cuerno-Rejado 2018][research_sanchezcarmona_cuernorejado_2018]] [[Sandy 1981][research_sandy_1981]] [[Sanghi 2003][research_sanghi_2003]] [[Sensmeier, Mark D. and Samareh, Jamshid A. 2005][research_sensmeiermarkd_samarehjamshida_2005]] [[Silva][research_silva_b]] [[Simon and Chudoba 2021][research_simon_chudoba_2021]] [[Simos and Jenkinson 1986][research_simos_jenkinson_1986]] [[Singh 1974][research_singh_1974]] [[Sirigireddy and Ahner 2026][research_sirigireddy_ahner_2026]] [[Sizing from a Conceptual 2024][research_sizing_from_2024]] [[Sizing, Trade Studies, and 2024][research_sizing_trade_2024]] [[Skillen and Crossley 2005][research_skillen_crossley_2005]] [[Skillen and Crossley 2008][research_skillen_crossley_2008]] [[Smith 1967][research_smith_1967]] [[Staack][research_staack]] [[Staats et al 2025][research_staats_troeltsch_2025]] [[Stamm and Woods 2024][research_stamm_woods_2024]] [[Stemler and Craig 1976][research_stemler_craig_1976]] [[Stringer et al][research_stringer_bunner]] [[Stroub 1989][research_stroub_1989]] [[Takahashi 2022][research_takahashi_2022]] [[Toffol and Ricci 2023][research_toffol_ricci_2023]] [[Torenbeek 1971][research_torenbeek_1971]] [[Torenbeek 2020][research_torenbeek_2020]] [[Trade Studies and Sizing 2010][research_trade_studies_2010]] [[Traub 2016][research_traub_2016]] [[Trw Inc Cleveland Oh Trw Accessories Div 1965][research_trwincclevelandohtrwaccessoriesdiv_1965]] [[Turriziani, R. V. et al 1979][research_turrizianirv_lovellwa_1979]] [[Ugwueze et al 2023][research_ugwueze_statheros_2023]] [[Vos 2019][research_vos_2019]] [[Vos 2019][research_vos_2019_b]] [[Waggoner 1999][research_waggoner_1999]] [[Wampler et al 1988][research_wampler_myklebust_1988]] [[Wang and Shi 2023][research_wang_shi_2023]] [[Weight Prediction, Optimization, and 2020][research_weight_prediction_2020]] [[Werner-Westphal et al 2008][research_wernerwestphal_heinze_2008]] [[Whitford 1991][research_whitford_1991]] [[Wildermuth et al 1974][research_wildermuth_rothammer_1974]] [[Wildermuth et al 1974][research_wildermuth_rothammer_1974_b]] [[Winter et al 2021][research_winter_robinson_2021]] [[Wrenn and Dovi 1988][research_wrenn_dovi_1988]] [[Xie et al 2019][research_xie_cai_2019]] [[Yang et al 2021][research_yang_nita_2021]] [[Yang et al 2025][research_yang_wan_2025]] [[Zafi and Chakraborty 2023][research_zafi_chakraborty_2023]] [[Zaimis et al 2024][research_zaimis_carpentari_2024]] [[Zandberg 2001][research_zandberg_2001]] [[Ünal et al 2023][research_unal_oz_2023]]

### Tailless configurations and their control effectors

**The configuration, and the thread this article inherits from its predecessor.** Tailless and flying wing aerodynamics, elevons, split drag rudders, control allocation among redundant effectors, and yaw by thrust vectoring. **The X-45A flew the configuration the previous article in this series analysed and found wanting for an operational fighter**, and it flew it sixty-four times.

**147 records.** [[Agenbag et al 2009][research_agenbag_theron_2009]] [[Agte et al 1997][research_agte_hadley_1997]] [[Alipour et al 2022][research_alipour_shahiashtiani_2022]] [[Alyanak and Pendleton 2014][research_alyanak_pendleton_2014]] [[Ashkenas, Irving L. and Klyde, David H. 1989][research_ashkenasirvingl_klydedavidh_1989]] [[Atay et al 2021][research_atay_bryant_2021]] [[Atmaca et al 2026][research_atmaca_stroosma_2026]] [[Berger et al 2011][research_berger_carmona_2011]] [[Bergman 1979][research_bergman_1979]] [[Boskovic and Mehra 1999][research_boskovic_mehra_1999]] [[Boskovic and Mehra 2000][research_boskovic_mehra_2000]] [[Boskovic et al][research_boskovic_saimingli]] [[Bourdin et al 2007][research_bourdin_gatto_2007]] [[Bradley et al 2012][research_bradley_gardhagen_2012]] [[Bramsiepe et al 2020][research_bramsiepe_voss_2020]] [[Buffington 1997][research_buffington_1997]] [[Buffington 1999][research_buffington_1999]] [[Buffington 1999][research_buffington_1999_b]] [[Chudoba and Cook 2003][research_chudoba_cook_2003]] [[Control Surface Sizing Criteria 2010][research_control_surface_2010]] [[Cook and Hauser 2018][research_cook_hauser_2018]] [[Dakka and Johnson 2019][research_dakka_johnson_2019]] [[DeLaurier 2022][research_delaurier_2022]] [[Deslich et al 2021][research_deslich_flick_2021]] [[Ebrahimi Fakhari et al 2024][research_ebrahimifakhari_moshtaghzadeh_2024]] [[Experimental investigation of synthetic 2023][research_experimental_investigation_2023]] [[Gillard 1998][research_gillard_1998]] [[Gillard et al 1997][research_gillard_dorsett_1997]] [[Gopejenko et al 2026][research_gopejenko_sidenko_2026]] [[Guiler][research_guiler]] [[Guiler and Huebsch 2005][research_guiler_huebsch_2005]] [[Guiler and Huebsch 2005][research_guiler_huebsch_2005_b]] [[Guo et al][research_guo_sun]] [[Harley et al 2009][research_harley_wilde_2009]] [[Hassairi and Abid 2021][research_hassairi_abid_2021]] [[Hauser 1999][research_hauser_1999]] [[Hoffler et al 1986][research_hoffler_rao_1986]] [[Hou et al 2022][research_hou_lv_2022]] [[Huang and Wei 2025][research_huang_wei_2025]] [[Huber 2022][research_huber_2022]] [[Huber et al 2012][research_huber_schutte_2012]] [[Islam et al 2024][research_islam_mohona_2024]] [[Jiang et al 2019][research_jiang_zhang_2019]] [[Jiguang Li et al 2016][research_jiguangli_xinchen_2016]] [[Jo et al 2016][research_jo_park_2016]] [[Johnson, Joseph L. 1949][research_johnsonjosephl_1949]] [[Jun 2023][research_jun_2023]] [[Karimi Kelayeh and Djavareshkian 2024][research_karimikelayeh_djavareshkian_2024]] [[Keidel et al 2019][research_keidel_fasel_2019]] [[Kumar et al 2020][research_kumar_mandal_2020]] [[Kumar et al 2020][research_kumar_mandal_2020_b]] [[Kwiek and Figat 2016][research_kwiek_figat_2016]] [[Li and Guo 2013][research_li_guo_2013]] [[Li et al 2017][research_li_yong_2017]] [[Li et al 2018][research_li_zhang_2018]] [[Lin et al 2026][research_lin_zong_2026]] [[Lingyu et al 2006][research_lingyu_youwu_2006]] [[Liu and Zhang 2022][research_liu_zhang_2022]] [[Liu et al 2026][research_liu_ai_2026]] [[Loechert et al 2018][research_loechert_huber_2018]] [[Love and Kapania 2020][research_love_kapania_2020]] [[Löchert et al 2019][research_lochert_huber_2019]] [[Ma and Wang 2009][research_ma_wang_2009]] [[Mader and Martins 2010][research_mader_martins_2010]] [[Mahantesh Katagi et al 2015][research_mahanteshkatagi_manishkumarsingh_2015]] [[Maimako et al 2026][research_maimako_mintah_2026]] [[Mansor et al 2019][research_mansor_sahwee_2019]] [[Mardanpour and Hodges 2013][research_mardanpour_hodges_2013]] [[Mardanpour and Hodges 2014][research_mardanpour_hodges_2014]] [[Matamoros and de Visser 2018][research_matamoros_devisser_2018]] [[McBreen et al 2023][research_mcbreen_boling_2023]] [[Mertzlufft et al 2022][research_mertzlufft_carvajal_2022]] [[Metin et al 2023][research_metin_uzuner_2023]] [[Mitcham, Grady L et al 1956][research_mitchamgradyl_stevensjosephe_1956]] [[Morris and Tigner 1995][research_morris_tigner_1995]] [[Mullins, Jr. et al 1996][research_mullinsjr_tipton_1996]] [[Murray 1949][research_murray_1949]] [[Orhan and Subbarao 2021][research_orhan_subbarao_2021]] [[Oshin Mittal et al 2024][research_oshinmittal_alokkumarsahu_2024]] [[Pan and Huang 2019][research_pan_huang_2019]] [[Pan et al 2025][research_pan_ma_2025]] [[Paranjape and Chung 2010][research_paranjape_chung_2010]] [[Peng et al 2014][research_peng_wang_2014]] [[Phan and Park 2018][research_phan_park_2018]] [[Qi et al 2017][research_qi_wang_2017]] [[Qi et al 2018][research_qi_zhao_2018_b]] [[Rajamurugu et al 2026][research_rajamurugu_dheerajkumar_2026]] [[Rajput et al 2014][research_rajput_zhang_2014]] [[Rajput et al 2015][research_rajput_zhangweiguo_2015]] [[Rojas Carvajal and Amitay 2023][research_rojascarvajal_amitay_2023]] [[Rojas Carvajal and Amitay 2025][research_rojascarvajal_amitay_2025]] [[Rojas Carvajal et al 2022][research_rojascarvajal_guha_2022]] [[Roy 2009][research_roy_2009]] [[Roy and Ghosh 2010][research_roy_ghosh_2010]] [[Rui et al 2007][research_rui_zhou_2007]] [[Saheby et al 2026][research_saheby_jialu_2026]] [[Sanghi et al 2022][research_sanghi_riso_2022]] [[Saucez][research_saucez]] [[Saucez and Boiffier 2012][research_saucez_boiffier_2012]] [[Schuette et al 2018][research_schuette_vormweg_2018]] [[Shayan and Van Kampen 2021][research_shayan_vankampen_2021]] [[Shi and Wu 2022][research_shi_wu_2022]] [[Shuang et al 2016][research_shuang_zhang_2016]] [[Shuang et al 2017][research_shuang_zhang_2017]] [[Song et al 2014][research_song_yang_2014]] [[Staelens et al 2007][research_staelens_blackwelder_2007]] [[Stenfelt and Ringertz 2009][research_stenfelt_ringertz_2009]] [[Stenfelt and Ringertz 2010][research_stenfelt_ringertz_2010]] [[Sun et al 2005][research_sun_zhang_2005]] [[Sun et al 2024][research_sun_zhou_2024]] [[Suresh et al 2013][research_suresh_radhakrishnan_2013]] [[Tal and Karaman 2021][research_tal_karaman_2021]] [[Tan et al 2014][research_tan_zhou_2014]] [[Teel 1999][research_teel_1999]] [[Teel 1999][research_teel_1999_b]] [[Tingting and Aijun 2014][research_tingting_aijun_2014]] [[Tomac and Stenfelt 2014][research_tomac_stenfelt_2014]] [[Traas et al 2026][research_traas_atmaca_2026]] [[Voss 2018][research_voss_2018]] [[Voß 2019][research_voss_2019]] [[Wang and Wang 2012][research_wang_wang_2012]] [[Wang and Zhou 2022][research_wang_zhou_2022]] [[Wang et al 2020][research_wang_tang_2020]] [[Wang et al 2024][research_wang_zhao_2024]] [[Wang et al 2025][research_wang_ai_2025]] [[Wang et al 2026][research_wang_liu_2026]] [[Weyl 1944][research_weyl_1944]] [[Weyl 1945][research_weyl_1945]] [[Weyl 1945][research_weyl_1945_b]] [[White, Maurice D. and Innis, Robert C. 1959][research_whitemauriced_innisrobertc_1959]] [[Williams et al 2025][research_williams_niestroy_2025]] [[Xi and Zhao 2017][research_xi_zhao_2017]] [[Xie et al 2011][research_xie_yang_2011]] [[Yu et al 2023][research_yu_li_2023]] [[Yu et al 2024][research_yu_li_2024]] [[Yue et al 2009][research_yue_wang_2009]] [[Yue et al 2013][research_yue_wang_2013]] [[Yue et al 2013][research_yue_wang_2013_b]] [[Zhang and He 2026][research_zhang_he_2026]] [[Zhang and He 2026][research_zhang_he_2026_b]] [[Zhang and Zhao 2023][research_zhang_zhao_2023]] [[Zhang et al 2017][research_zhang_shan_2017]] [[Zhang et al 2018][research_zhang_shuang_2018]] [[Zhang et al 2023][research_zhang_huang_2023]] [[Zhang et al 2025][research_zhang_zhao_2025]] [[Zhou et al 2022][research_zhou_dong_2022]] [[Zhou et al 2023][research_zhou_dong_2023]]

### Aerodynamics of the configuration

**The flow the vehicle lives in.** Lift, drag, vortex behaviour, boundary layers, wind tunnel technique and computation. **The X-45's aerodynamic record is thin because the aerodynamics were not the point**, the configuration having been chosen for signature and the programme's risk having sat in the software.

**134 records.** [[Aerodynamic Data of Real 2010][research_aerodynamic_data_2010]] [[Aerodynamics 2024][research_aerodynamics_2024]] [[Aircraft Drag 2010][research_aircraft_drag_2010]] [[Airfoil and Wing/Tail Geometry 2024][research_airfoil_and_2024]] [[Aoyama et al 1995][research_aoyama_kawachi_1995]] [[Appendix G Aerodynamic Data 2010][research_appendix_g_2010]] [[Ashenberg and Weihs 1984][research_ashenberg_weihs_1984]] [[Attinello 1956][research_attinello_1956]] [[Awadalla Ali Haj Ahmed 2024][research_awadallaalihajahmed_2024]] [[Bardera-Mora et al 2018][research_barderamora_garciamagarino_2018]] [[Bardera-Mora et al 2019][research_barderamora_garciamagarino_2019]] [[Barthelemy et al 1994][research_barthelemy_coen_1994]] [[Belloni et al 2024][research_belloni_silvestrini_2024]] [[Berens 2003][research_berens_2003]] [[Biber 2023][research_biber_2023]] [[Biber et al 2004][research_biber_ol_2004]] [[Boo et al 2015][research_boo_mansor_2015]] [[Borgen and Mott 2024][research_borgen_mott_2024]] [[Brauckmann, Gregory J. 1998][research_brauckmanngregoryj_1998]] [[Breitsamter and Laschka 2001][research_breitsamter_laschka_2001]] [[Bryant et al 1998][research_bryant_tigges_1998]] [[Butler 1976][research_butler_1976]] [[Cass and Ball 1988][research_cass_ball_1988]] [[Chang et al 2022][research_chang_zheng_2022]] [[Chen and Qin 2013][research_chen_qin_2013]] [[Chen et al 2020][research_chen_zhou_2020_d]] [[Chen et al 2020][research_chen_zhou_2020_e]] [[Chen et al 2026][research_chen_zhai_2026]] [[Chiba et al 2006][research_chiba_obayashi_2006]] [[Chinag and Youssef 1994][research_chinag_youssef_1994]] [[Crimi and Johnson 1973][research_crimi_johnson_1973]] [[Cunningham and den Boer 1990][research_cunningham_denboer_1990]] [[Dresser et al 1990][research_dresser_newberry_1990]] [[Ebne-Abbasi et al 2024][research_ebneabbasi_makarov_2024]] [[Elisov et al 2018][research_elisov_ishkov_2018]] [[Elkhoury 2016][research_elkhoury_2016]] [[Elkhoury and Nakad 2009][research_elkhoury_nakad_2009]] [[Figliola 2004][research_figliola_2004]] [[Figliola 2005][research_figliola_2005]] [[Fofonov 2021][research_fofonov_2021]] [[Geva et al 2019][research_geva_abramovich_2019]] [[Giles 1986][research_giles_1986]] [[Gordnier and Visbal 1994][research_gordnier_visbal_1994]] [[Govindarajan and Sridharan 2020][research_govindarajan_sridharan_2020]] [[Grosser 1965][research_grosser_1965]] [[Head and Hohenemser 1951][research_head_hohenemser_1951]] [[Hermanutz and Hornung 2020][research_hermanutz_hornung_2020]] [[Herrmann 2004][research_herrmann_2004]] [[High-Lift Devices 2010][research_high_lift_devices_2010]] [[Hill and Waters 1974][research_hill_waters_1974]] [[Hubbell][research_hubbell]] [[Hummel and Oelker 1994][research_hummel_oelker_1994]] [[Hutchison et al 1994][research_hutchison_unger_1994]] [[Huyer et al 1992][research_huyer_robinson_1992]] [[Hynes et al 1989][research_hynes_franklin_1989]] [[Introduction to Aircraft Aerodynamic 2021][research_introduction_to_2021]] [[Jones, Thomas, W. and Hoppe, John C. 2001][research_jonesthomasw_hoppejohnc_2001]] [[Kamman and Hall 1978][research_kamman_hall_1978]] [[Kasim Biber and Trenton White 2019][research_kasimbiber_trentonwhite_2019]] [[Kasuga et al 2017][research_kasuga_yoshida_2017]] [[Knuth et al 2012][research_knuth_cassano_2012]] [[Kogiso et al 2000][research_kogiso_tsushima_2000]] [[Kolpitcke and Smith 2025][research_kolpitcke_smith_2025]] [[Kroo 1986][research_kroo_1986]] [[Kryvokhatko 2023][research_kryvokhatko_2023]] [[Kryvokhatko 2023][research_kryvokhatko_2023_b]] [[Kryvokhatko 2024][research_kryvokhatko_2024]] [[Kryvokhatko 2024][research_kryvokhatko_2024_b]] [[Kuo and Hsu 1997][research_kuo_hsu_1997]] [[Lam and Maull 1993][research_lam_maull_1993]] [[Lawson and Barakos 2010][research_lawson_barakos_2010]] [[Lee and Batina 1991][research_lee_batina_1991]] [[Lee and Kim 2024][research_lee_kim_2024]] [[Li et al 2014][research_li_huang_2014]] [[Liu 2006][research_liu_2006]] [[Livne and Mineau 1997][research_livne_mineau_1997]] [[Ma 1989][research_ma_1989]] [[Manokaran et al 2009][research_manokaran_vidya_2009]] [[Marchman, Iii et al 1983][research_marchmaniii_donatelli_1983]] [[Mark and Dehart 1976][research_mark_dehart_1976]] [[McMillin and Wood 1987][research_mcmillin_wood_1987]] [[Menner and Lavretsky 2026][research_menner_lavretsky_2026]] [[Meyn, Larry A. et al 1993][research_meynlarrya_zellpetert_1993]] [[Moeller and Rediniotis 2002][research_moeller_rediniotis_2002]] [[Natalie and Jacob 2019][research_natalie_jacob_2019]] [[Nikolic 2007][research_nikolic_2007]] [[Nikolic et al 1996][research_nikolic_jumper_1996]] [[Nugroho 2026][research_nugroho_2026]] [[Obayashi et al 1997][research_obayashi_yamaguchi_1997]] [[Parenteau et al 2018][research_parenteau_laurendeau_2018]] [[Pham][research_pham]] [[Phillips and Hunsaker 2019][research_phillips_hunsaker_2019]] [[Phillips et al 2019][research_phillips_hunsaker_2019_b]] [[Planform Parameterization 2014][research_planform_parameterization_2014]] [[Preliminary Aerodynamic and Stability 2017][research_preliminary_aerodynamic_2017]] [[Pátek and Smrcek 1999][research_patek_smrcek_1999]] [[Recktenwald and Ahmed 2008][research_recktenwald_ahmed_2008]] [[Recktenwald et al 2010][research_recktenwald_crouse_2010]] [[Reubush 1979][research_reubush_1979]] [[Rieken et al 2004][research_rieken_yasumuro_2004]] [[Rizzetta and Visbal 2016][research_rizzetta_visbal_2016]] [[Rogers and Cook 1952][research_rogers_cook_1952]] [[Rosin et al 2004][research_rosin_mattos_2004]] [[Ross and Matarazzo 1982][research_ross_matarazzo_1982]] [[Rozov et al 2019][research_rozov_volmering_2019]] [[Selecting the Planform and 2010][research_selecting_the_2010]] [[Shipman et al 2008][research_shipman_arunajatesan_2008]] [[Shirley et al 2014][research_shirley_schetz_2014]] [[Silva et al 2024][research_silva_lundbladh_2024]] [[Skorobogatov and Buturov 2026][research_skorobogatov_buturov_2026]] [[Snyder 1990][research_snyder_1990]] [[Soemaryanto and Rosid 2018][research_soemaryanto_rosid_2018]] [[Song et al 2020][research_song_ma_2020]] [[Stalford 1979][research_stalford_1979]] [[Suarez et al 1992][research_suarez_kramer_1992]] [[Swanson and Isaac 2010][research_swanson_isaac_2010]] [[Traub 1994][research_traub_1994]] [[Traub 1995][research_traub_1995]] [[Traub 1995][research_traub_1995_b]] [[Tu et al 1998][research_tu_munir_1998]] [[Tu et al 2000][research_tu_munir_2000]] [[Venkata and Jones 2013][research_venkata_jones_2013]] [[Vrchota 2017][research_vrchota_2017]] [[Wakayama and Kroo 1995][research_wakayama_kroo_1995]] [[Wang and Zhan 2005][research_wang_zhan_2005]] [[Wiart and Carrier 2010][research_wiart_carrier_2010]] [[Woods and Daines 2003][research_woods_daines_2003]] [[Yen 1982][research_yen_1982]] [[Yukish and Valenti 2020][research_yukish_valenti_2020]] [[Zhao et al 2023][research_zhao_zeng_2023]] [[Zhou and Wang 2023][research_zhou_wang_2023]] [[Zuo et al 2023][research_zuo_xu_2023]] [[Čápek 1995][research_capek_1995]] [[Şugar Gabor et al 2016][research_sugargabor_koreanschi_2016]]

### Flight control law design and handling qualities

**What replaces the pilot's hands.** Control law design, stability augmentation, gain scheduling, adaptive and robust control, and the handling qualities framework that an unmanned aeroplane inherits without inheriting the pilot who defined it. **A handling quality is a statement about a human being**, and this cluster is where the field works out what the term means when there is nobody aboard.

**120 records.** [[Adams and Hatch, Jr. 1970][research_adams_hatchjr_1970]] [[Adamski 2021][research_adamski_2021]] [[Agarwal et al 2021][research_agarwal_ng_2021]] [[Aircraft lateral-directional handling qualities 2011][research_aircraft_lateral_directional_2011]] [[Aircraft longitudinal handling qualities 2011][research_aircraft_longitudinal_2011]] [[Alexander 2025][research_alexander_2025]] [[Alexander 2025][research_alexander_2025_b]] [[Ashkenas 1965][research_ashkenas_1965]] [[Ashkenas 1965][research_ashkenas_1965_b]] [[Ashkenas 1965][research_ashkenas_1965_c]] [[Ashkenas 1982][research_ashkenas_1982]] [[Bachelder and Aponso 2020][research_bachelder_aponso_2020]] [[Bachelder and Aponso 2020][research_bachelder_aponso_2020_b]] [[Bachelder et al 2023][research_bachelder_aponso_2023]] [[Bahr et al 2021][research_bahr_mckay_2021]] [[Baughman and Longeauay 2015][research_baughman_longeauay_2015]] [[Bechelder et al 2025][research_bechelder_bjorkman_2025]] [[Berger et al 2019][research_berger_horn_2019]] [[Berger et al 2022][research_berger_blanken_2022]] [[Berger et al 2025][research_berger_christensen_2025]] [[Berry 1986][research_berry_1986]] [[Berry and Powers 1970][research_berry_powers_1970]] [[Booz 1988][research_booz_1988]] [[Bray 1963][research_bray_1963]] [[Breul 1963][research_breul_1963]] [[Burnashev and Zbrutsky 2019][research_burnashev_zbrutsky_2019]] [[Callaghan and Kunz 2019][research_callaghan_kunz_2019]] [[Chaikalis et al 2020][research_chaikalis_khorrami_2020]] [[Chalk 1963][research_chalk_1963]] [[Chalk 1964][research_chalk_1964]] [[Cheatham and Hackler 1966][research_cheatham_hackler_1966]] [[Chevalier and Burke 1972][research_chevalier_burke_1972]] [[Clark 1964][research_clark_1964]] [[Cook 1997][research_cook_1997]] [[Cook 2007][research_cook_2007]] [[Cook 2013][research_cook_2013]] [[Cooke 2010][research_cooke_2010]] [[Crespo et al 2010][research_crespo_matsutani_2010]] [[Design Objectives for Flying][research_design_objectives_b]] [[Design Objectives For Handling][research_design_objectives]] [[Didomenico and Biezad 1985][research_didomenico_biezad_1985]] [[Drewiacki et al 2025][research_drewiacki_moreira_2025]] [[Duggan and Bhandari 2021][research_duggan_bhandari_2021]] [[Evangelou 1998][research_evangelou_1998]] [[Fegely et al 2017][research_fegely_xin_2017]] [[Gerken 1979][research_gerken_1979]] [[Goldstein 1982][research_goldstein_1982]] [[Hall 1971][research_hall_1971]] [[Handling qualities 2000][research_handling_qualities_2000]] [[Handling Qualities Analysis 2008][research_handling_qualities_2008]] [[Handling Qualities and Control 2017][research_handling_qualities_2017]] [[Harper and Sardanowsky 1969][research_harper_sardanowsky_1969]] [[Harris et al 2000][research_harris_gautrey_2000]] [[Hart 1956][research_hart_1956]] [[Hess 1981][research_hess_1981]] [[Hess 1984][research_hess_1984]] [[Hess 2010][research_hess_2010]] [[Hoh 1988][research_hoh_1988]] [[Hoh and Mitchell 1983][research_hoh_mitchell_1983]] [[Horn et al 2017][research_horn_thorsen_2017]] [[Ito et al 2016][research_ito_endo_2016]] [[Johnston and Friend 1965][research_johnston_friend_1965]] [[Jones et al 2023][research_jones_klyde_2023]] [[Junfeng et al 2020][research_junfeng_wuzhou_2020]] [[Klein et al 2017][research_klein_krainski_2017]] [[Klyde et al 1999][research_klyde_mitchell_1999]] [[Klyde et al 2021][research_klyde_lampton_2021]] [[Kozhanov et al 2022][research_kozhanov_suvorova_2022]] [[Kramer et al 2023][research_kramer_bailey_2023]] [[Lampton et al 2024][research_lampton_klyde_2024]] [[Levison and Rickard 1981][research_levison_rickard_1981]] [[Li et al 2024][research_li_zhang_2024]] [[Li et al 2026][research_li_zhang_2026_b]] [[Liang et al 2024][research_liang_dong_2024]] [[Lusardi 2023][research_lusardi_2023]] [[Ma][research_ma]] [[MacKunis et al 2008][research_mackunis_kaiser_2008]] [[Martin 1963][research_martin_1963]] [[McCormick 1969][research_mccormick_1969]] [[Mcgregor and Smith 1965][research_mcgregor_smith_1965]] [[Miller 1968][research_miller_1968]] [[Mooij 1985][research_mooij_1985]] [[Mooij 1985][research_mooij_1985_b]] [[Mooij 1985][research_mooij_1985_c]] [[Mooij 1985][research_mooij_1985_d]] [[Natesan and Bhat 2005][research_natesan_bhat_2005]] [[Nettleton 1965][research_nettleton_1965]] [[Noble and Bhandari 2017][research_noble_bhandari_2017]] [[Northrop Aircraft Inc Hawthorne Ca 1952][research_northropaircraftinchawthorneca_1952]] [[Oosterom and Babuska 2001][research_oosterom_babuska_2001]] [[Ossmann et al 2019][research_ossmann_luspay_2019]] [[Peng et al 2025][research_peng_kaiqi_2025]] [[Peters et al 1997][research_peters_andrisaniii_1997]] [[Qian Shen et al 2016][research_qianshen_suozhongyuan_2016]] [[Rhoads 1967][research_rhoads_1967]] [[Riccardi et al 2025][research_riccardi_mamino_2025]] [[Rotorcraft handling qualities design 2011][research_rotorcraft_handling_2011]] [[Rylko et al 2025][research_rylko_favaro_2025]] [[Rzucidło 2006][research_rzucidlo_2006]] [[Saetti and Rogers 2020][research_saetti_rogers_2020]] [[Sarrafian and Powers 1988][research_sarrafian_powers_1988]] [[Schmidt 2016][research_schmidt_2016]] [[Shubert and Jones 2025][research_shubert_jones_2025]] [[Shweyk and Hyde 2013][research_shweyk_hyde_2013]] [[Simplício et al 2018][research_simplicio_navarrotapia_2018]] [[Smith 2023][research_smith_2023]] [[Solies 1995][research_solies_1995]] [[Srinathkumar 2011][research_srinathkumar_2011]] [[Stability, Control, and Handling 2024][research_stability_control_2024]] [[Teofilatto 2001][research_teofilatto_2001]] [[Teper and Stapleford 1965][research_teper_stapleford_1965]] [[Teper and Stapleford 1966][research_teper_stapleford_1966]] [[Thukral and Innocenti 1992][research_thukral_innocenti_1992]] [[Torelli et al 2023][research_torelli_stroosma_2023]] [[Van Gool and Mooij 1979][research_vangool_mooij_1979]] [[Van Gool and Weingarten 1981][research_vangool_weingarten_1981]] [[Weltz and Barajas 2025][research_weltz_barajas_2025]] [[Westbrook 1964][research_westbrook_1964]] [[Wilhelm and Schafranek 1986][research_wilhelm_schafranek_1986]] [[Willebeek-LeMair and Rhinehart 2023][research_willebeeklemair_rhinehart_2023]]

### Programme, acquisition and the cost of a demonstrator

**Why the programme ended, which is the part of this story that is documented.** Acquisition, cost estimation, technology readiness and the transition from demonstrator to programme of record. **J-UCAS was cancelled in January 2006 with both vehicles flying or nearly so**, and the reasons were institutional rather than technical.

**86 records.** [[A340-600 wing completes UK 2002][research_a340_600_wing_2002]] [[Aerospace ID Technologies Research 2006][research_aerospace_id_2006]] [[Aerospace series - Programme][research_aerospace_series_e]] [[Aerospace series - Programme][research_aerospace_series_h]] [[Aerospace series - Programme][research_aerospace_series_k]] [[Aerospace series. Programme Management][research_aerospace_series_b]] [[Aerospace series. Programme Management][research_aerospace_series_d]] [[Aerospace series. Programme management][research_aerospace_series_f]] [[Aerospace series. Programme Management][research_aerospace_series_g]] [[Aerospace series. Programme management][research_aerospace_series_i]] [[Aerospace series�� Programme management��][research_aerospace_series_c]] [[Aerospace series�� Programme management��][research_aerospace_series_j]] [[Aerospace supplier programme 2004][research_aerospace_supplier_2004]] [[Aircraft improvement programme at 2002][research_aircraft_improvement_2002]] [[Aircraft Prototype and Technology 1983][research_aircraft_prototype_1983]] [[Alley et al 2010][research_alley_steele_2010]] [[Backing for Aviation Centenary 2009][research_backing_for_2009]] [[Bajurko 2019][research_bajurko_2019]] [[Barbatei et al 2015][research_barbatei_skavhaug_2015]] [[Beech Announces Wing Structure 1982][research_beech_announces_1982]] [[Belai 2025][research_belai_2025]] [[Bell 1993][research_bell_1993]] [[Catelani et al 2015][research_catelani_ciani_2015]] [[Chiba et al 2009][research_chiba_makino_2009]] [[Constantin et al 2023][research_constantin_decourcy_2023]] [[Cox 1989][research_cox_1989]] [[Crafton 1965][research_crafton_1965]] [[DeCAMP and Hardy 1981][research_decamp_hardy_1981]] [[DeLancey et al 2011][research_delancey_harris_2011]] [[Design of the circulation 1979][research_design_of_1979]] [[Dietrich 2020][research_dietrich_2020]] [[Draper et al 1983][research_draper_buck_1983]] [[Dress et al 1992][research_dress_boyden_1992]] [[Délery and Meauzé 2003][research_delery_meauze_2003]] [[EADS and A* STAR 2007][research_eads_and_2007]] [[ECO Demonstrator Begins Flight 2018][research_eco_demonstrator_2018]] [[Elena 2026][research_elena_2026]] [[Ellis 1976][research_ellis_1976]] [[Flight Test Programme 1970][research_flight_test_1970]] [[Fuel cell demonstrator aeroplane 2007][research_fuel_cell_2007]] [[Fuhrmann et al][research_fuhrmann_koch]] [[Gilge 2010][research_gilge_2010]] [[Graves et al 2023][research_graves_snow_2023]] [[Greer and Campbell 1980][research_greer_campbell_1980]] [[Gregory and Kim 2022][research_gregory_kim_2022]] [[Hintzke and Haggard 1991][research_hintzke_haggard_1991]] [[Hirschel 1993][research_hirschel_1993]] [[Holubik 1988][research_holubik_1988]] [[IEC in-flight system chosen 1999][research_iec_in_flight_1999]] [[Inoyama et al 2008][research_inoyama_sanders_2008]] [[Integrated wing research programme 2006][research_integrated_wing_2006]] [[Jategaonkar et al 2006][research_jategaonkar_behr_2006]] [[Jurges 1999][research_jurges_1999]] [[Konar et al 2024][research_konar_ozdemir_2024]] [[Krüger et al 2022][research_kruger_meddaikar_2022]] [[Kuczera and Hauck 1992][research_kuczera_hauck_1992]] [[Kuczera et al 1993][research_kuczera_hauck_1993]] [[Larsson 2025][research_larsson_2025]] [[Leasure 2002][research_leasure_2002]] [[Marx et al 1995][research_marx_mavris_1995]] [[Mathy Franz-Josef 2012][research_mathyfranzjosef_2012]] [[McDevitt 2005][research_mcdevitt_2005]] [[Montes et al 2022][research_montes_mitchell_2022]] [[Morton 1956][research_morton_1956]] [[Nickol 2011][research_nickol_2011]] [[Olejnik et al 2019][research_olejnik_rogolski_2019]] [[Options for Reducing Costs 2005][research_options_for_2005]] [[OU-validated Foundation Degree Programme 2008][research_ou_validated_foundation_2008]] [[Rapstine et al 2017][research_rapstine_sava_2017]] [[Robinson 2004][research_robinson_2004]] [[Ruiqian et al 2020][research_ruiqian_juan_2020]] [[Shane 1992][research_shane_1992]] [[Simpson et al 2005][research_simpson_rawashdeh_2005]] [[Standard Practice for Development][research_standard_practice]] [[Sylvester 1980][research_sylvester_1980]] [[The U.S. Aircraft Carrier 1998][research_the_u_s_1998]] [[Theorem's CADverter software converts 2003][research_theorem_s_cadverter_2003]] [[Tsukamoto et al 2003][research_tsukamoto_deturris_2003]] [[UAV demonstrator opens up 2006][research_uav_demonstrator_2006]] [[UAV demonstrator opens up 2007][research_uav_demonstrator_2007]] [[Walker 2011][research_walker_2011]] [[Wang 2026][research_wang_2026]] [[Wright 2005][research_wright_2005]] [[Yakovlev et al 2020][research_yakovlev_bakulin_2020]] [[Zhang et al 2013][research_zhang_cui_2013]] [[Zhongfei and Lijun 2025][research_zhongfei_lijun_2025]]

### Unmanned combat aircraft and the strike mission

**The vehicle class, as distinct from the far larger literature on unmanned aircraft in general.** Armed unmanned aircraft, strike mission analysis and the operational arguments for and against them. **This cluster is deliberately narrow**, because the civil small aircraft literature now dwarfs the combat one and would otherwise swamp the survey.

**84 records.** [[A.V. Ananyev 2019][research_avananyev_2019]] [[Aleisa et al 2023][research_aleisa_kontis_2023]] [[Aleisa et al 2023][research_aleisa_kontis_2023_b]] [[Aslan and Oktay 2023][research_aslan_oktay_2023]] [[Bookstaber 2000][research_bookstaber_2000]] [[Booz 1998][research_booz_1998]] [[Brown 1989][research_brown_1989]] [[Brown 1998][research_brown_1998]] [[Chang et al 2022][research_chang_zhang_2022]] [[Choi et al 2010][research_choi_nguyen_2010]] [[Cox 2009][research_cox_2009]] [[Cummings and Schütte 2012][research_cummings_schutte_2012]] [[Cummings et al 2003][research_cummings_morton_2003]] [[Cummings et al 2008][research_cummings_morton_2008]] [[Cummings et al 2018][research_cummings_liersch_2018]] [[Davidson 2004][research_davidson_2004]] [[Dickes et al 2002][research_dickes_gingras_2002]] [[Dong et al 2017][research_dong_huang_2017]] [[Dong Kangsheng et al 2016][research_dongkangsheng_huangchangqiang_2016]] [[Elkhoury 2008][research_elkhoury_2008]] [[Elkhoury and Rockwell 2004][research_elkhoury_rockwell_2004]] [[Elkhoury et al 2005][research_elkhoury_yavuz_2005]] [[Ernest and Carroll 2016][research_ernest_carroll_2016]] [[Ernest and Cohen 2016][research_ernest_cohen_2016]] [[Flow Control and High-Lift 2016][research_flow_control_2016]] [[Fu Li et al 2008][research_fuli_yumeixiang_2008]] [[Gordnier et al][research_gordnier_visbal]] [[Gordnier et al 2006][research_gordnier_visbal_2006]] [[Gordnier et al 2007][research_gordnier_sherer_2007]] [[Grzesik and Sobolewski 2014][research_grzesik_sobolewski_2014]] [[Khalid 2023][research_khalid_2023]] [[Khreish et al 2005][research_khreish_sinha_2005]] [[Klein 2002][research_klein_2002]] [[Kumar 2020][research_kumar_2020]] [[Kumar et al 2026][research_kumar_mittal_2026]] [[Lee and Tahk 2019][research_lee_tahk_2019]] [[Lei 2020][research_lei_2020]] [[Lewis 2002][research_lewis_2002]] [[Li et al 2024][research_li_zhu_2024]] [[Liersch and Bishop 2018][research_liersch_bishop_2018]] [[Lima Filho et al 2021][research_limafilho_medeiros_2021]] [[Liu et al 2023][research_liu_sun_2023]] [[Liu et al 2025][research_liu_ding_2025]] [[Matsushima 2001][research_matsushima_2001]] [[Minglang et al 2018][research_minglang_haiwen_2018]] [[Mishra et al 2022][research_mishra_ullah_2022]] [[Nguyen et al 2009][research_nguyen_choi_2009]] [[Nguyen et al 2013][research_nguyen_choi_2013]] [[Ordaz et al 2004][research_ordaz_lee_2004]] [[Pedro et al 2013][research_pedro_panday_2013]] [[Prakash 2020][research_prakash_2020]] [[Pratt and Whitney 2009][research_pratt_and_2009]] [[Qinkun Xiao et al 2006][research_qinkunxiao_xiaoguanggao_2006]] [[Ramin et al 2022][research_ramin_heriana_2022]] [[Reichenbach 2003][research_reichenbach_2003]] [[Renehan 1997][research_renehan_1997]] [[Ruetten 2018][research_ruetten_2018]] [[S. et al 2025][research_s_c_2025]] [[Sathe and Pant 2010][research_sathe_pant_2010]] [[Schneider 1989][research_schneider_1989]] [[Sepulveda Palacios and Smith 2019][research_sepulvedapalacios_smith_2019]] [[Tekinalp and Cavus 2012][research_tekinalp_cavus_2012]] [[Tianyuan and Xiongqing 2009][research_tianyuan_xiongqing_2009]] [[Tomac et al 2012][research_tomac_rizzi_2012]] [[Twesme and Corzine 2003][research_twesme_corzine_2003]] [[Vallespin et al 2011][research_vallespin_ronch_2011]] [[van Rooij and Cummings 2018][research_vanrooij_cummings_2018]] [[van Rooij et al 2018][research_vanrooij_frink_2018]] [[van Rooij et al 2019][research_vanrooij_frink_2019]] [[Venetsky et al 2003][research_venetsky_husni_2003]] [[Vicroy et al 2012][research_vicroy_loeser_2012]] [[Vicroy, Dan D. et al 2014][research_vicroydand_huberkerstinc_2014]] [[Voss et al 2011][research_voss_cumnuantip_2011]] [[Wang et al 2020][research_wang_wang_2020]] [[Wills 2015][research_wills_2015]] [[Wills 2015][research_wills_2015_b]] [[Wilt et al 2022][research_wilt_hicks_2022]] [[Wise 2003][research_wise_2003]] [[Woo et al 2022][research_woo_choi_2022]] [[Wyatt 2003][research_wyatt_2003]] [[Yang 2024][research_yang_2024]] [[Yin et al 2020][research_yin_fan_2020]] [[Zhang et al 2023][research_zhang_yang_2023]] [[Zhou et al 2015][research_zhou_bao_2015]]

### Multi-vehicle coordination and cooperative control

**The other half of the fan-out problem, approached from the machine's side.** Cooperative control, task allocation, consensus, distributed decision making, formation flight and swarm coordination. **Autonomy raises the fan-out by raising neglect time**, and this cluster is where the algorithms that do so live.

**59 records.** [[A Prediction Method for 2017][research_a_prediction_2017]] [[Abas et al 2013][research_abas_pebrianti_2013]] [[Ali Dehghani and Bagher Menhaj 2016][research_alidehghani_baghermenhaj_2016]] [[An and Kim 2025][research_an_kim_2025]] [[Anum et al 2022][research_anum_liaquat_2022]] [[Azizi and Khorasani 2011][research_azizi_khorasani_2011]] [[Bayraktar et al 2004][research_bayraktar_fainekos_2004]] [[Birkenhead 2024][research_birkenhead_2024]] [[Cai et al 2018][research_cai_zhou_2018]] [[Calnoor Rajashekar et al 2020][research_calnoorrajashekar_tourani_2020]] [[Cetin and Yilmaz 2014][research_cetin_yilmaz_2014]] [[Chao et al 2017][research_chao_brink_2017]] [[Chen et al 2026][research_chen_wang_2026]] [[Coleman and Hamilton 2026][research_coleman_hamilton_2026]] [[Cui et al 2022][research_cui_zhou_2022]] [[D'Andrea 2008][research_dandrea_2008]] [[Dehghani and Menhaj 2016][research_dehghani_menhaj_2016]] [[Duan 2013][research_duan_2013]] [[Gong et al 2022][research_gong_xu_2022]] [[Guerrero 2012][research_guerrero_2012]] [[Hemati et al 2012][research_hemati_eldredge_2012]] [[Jenkinson et al 2000][research_jenkinson_page_2000]] [[Jianan Wang and Ming Xin 2013][research_jiananwang_mingxin_2013]] [[Krizek et al 2022][research_krizek_horyna_2022]] [[Larrabee][research_larrabee]] [[Leonard et al 2013][research_leonard_savvaris_2013]] [[Li et al 2017][research_li_qin_2017]] [[Lin 2002][research_lin_2002]] [[Liu and Bucknall 2018][research_liu_bucknall_2018]] [[Liu et al 2022][research_liu_liu_2022]] [[Miller 2006][research_miller_2006]] [[Mingfeng Zhang and Liu 2013][research_mingfengzhang_liu_2013]] [[Nguyen 2019][research_nguyen_2019]] [[Noro and Inamori 2020][research_noro_inamori_2020]] [[Orozco et al 2026][research_orozco_walsh_2026]] [[Pack et al][research_pack_york]] [[Panday and Pedro 2018][research_panday_pedro_2018]] [[Ransquin et al 2021][research_ransquin_caprace_2021]] [[Ruggiero et al 2025][research_ruggiero_ito_2025]] [[Saska 2015][research_saska_2015]] [[Sauter et al 2005][research_sauter_matthews_2005]] [[Sperling et al 2008][research_sperling_kewley_2008]] [[Teague et al 2008][research_teague_kewley_2008]] [[Tierney and Rodenbeck 2019][research_tierney_rodenbeck_2019]] [[Uybarreta et al 2025][research_uybarreta_grant_2025]] [[Wang and Wang 2017][research_wang_wang_2017]] [[Wang and Xin 2012][research_wang_xin_2012]] [[Wang et al 2020][research_wang_fei_2020]] [[Weijun et al 2008][research_weijun_xiangju_2008]] [[Wen et al 2023][research_wen_du_2023]] [[Xu and Shi 2013][research_xu_shi_2013]] [[Xue et al 2024][research_xue_huang_2024]] [[Yang et al 2024][research_yang_yang_2024]] [[Ye and Zheng 2025][research_ye_zheng_2025]] [[Yin et al 2023][research_yin_gu_2023]] [[Yoo et al 2021][research_yoo_park_2021]] [[Zhang and Mehrjerdi 2013][research_zhang_mehrjerdi_2013]] [[Zhou et al 2020][research_zhou_kuang_2020]] [[Zhu et al 2025][research_zhu_bordner_2025]]

### Propulsion, inlet integration and installed performance

**The engine and what the airframe does to it.** Turbofan cycle and installed performance, embedded inlet integration, pressure recovery and specific fuel consumption. **The article uses this literature for one purpose**, being to test whether a published thrust figure can hold a published ceiling.

**54 records.** [[Allard 1982][research_allard_1982]] [[Bolonkin 2005][research_bolonkin_2005_b]] [[Brown and Sun 2017][research_brown_sun_2017]] [[Che Man et al 2020][research_cheman_liu_2020]] [[Conners 1995][research_conners_1995]] [[Dantsker et al 2018][research_dantsker_theile_2018]] [[Design and Development of 1989][research_design_and_1989]] [[DLR and MTU Aero 2020][research_dlr_and_2020]] [[Duhamel 1989][research_duhamel_1989]] [[Edelbaum 1963][research_edelbaum_1963]] [[Farokhi 1998][research_farokhi_1998]] [[German Hypersonics Technology Programme 1993][research_german_hypersonics_1993]] [[Ghadge and S. 2021][research_ghadge_s_2021]] [[Hartmann et al 2021][research_hartmann_noland_2021]] [[Havey and Kline 1989][research_havey_kline_1989]] [[Heitmeir et al 1992][research_heitmeir_lederer_1992]] [[Hirschel 1991][research_hirschel_1991]] [[Hunziker 1968][research_hunziker_1968]] [[Jagtap 2025][research_jagtap_2025]] [[Licheva and Liscouet-Hanke 2023][research_licheva_liscouethanke_2023]] [[Lu 2026][research_lu_2026]] [[Martinez 2022][research_martinez_2022]] [[McAllister and Parish 2009][research_mcallister_parish_2009]] [[Medina et al 2021][research_medina_patel_2021]] [[Mutz et al 1964][research_mutz_pierce_1964]] [[Norris and Bauer 1993][research_norris_bauer_1993]] [[Numerical Methods and Experimental 2026][research_numerical_methods_2026]] [[Office Of Naval Research Arlington Va 1993][research_officeofnavalresearcharlingtonva_1993]] [[Patterson et al 1991][research_patterson_champion_1991]] [[Pavkovic et al 2020][research_pavkovic_krznar_2020]] [[Podhradsky et al 2013][research_podhradsky_bone_2013]] [[Pritulo et al 1995][research_pritulo_gubanov_1995]] [[Propulsion 2017][research_propulsion_2017]] [[Propulsion 2024][research_propulsion_2024]] [[Propulsion Data 2010][research_propulsion_data_2010]] [[Propulsion System Thrust Sizing 2010][research_propulsion_system_2010]] [[Quan et al 2018][research_quan_xiao_2018]] [[Reichbach et al 2001][research_reichbach_sedwick_2001]] [[Remiger et al 2024][research_remiger_grois_2024]] [[Ridley 1982][research_ridley_1982]] [[Silva and Guimarães 2020][research_silva_guimaraes_2020]] [[Sizing the Engine Installed 2002][research_sizing_the_2002]] [[Sizing the Engine Installed 2018][research_sizing_the_2018]] [[Stechman 1984][research_stechman_1984]] [[Svoboda 2000][research_svoboda_2000]] [[Taflan et al 2026][research_taflan_smith_2026]] [[Thrust-to-Weight Ratio and Wing 2024][research_thrust_to_weight_ratio_2024]] [[Turan 2012][research_turan_2012]] [[Turbine Engine Inlet Design 2010][research_turbine_engine_2010]] [[Vos 2019][research_vos_2019_c]] [[Warner and Lee 2026][research_warner_lee_2026]] [[Warsch et al 2026][research_warsch_carbone_2026]] [[Xia et al 2025][research_xia_wu_2025]] [[Zhao et al 2024][research_zhao_zhou_2024]]

### Human supervisory control and the span of control

**This is the cluster the article's keystone comes from and it is not an aeronautical literature at all.** It holds human-robot interaction, the fan-out relation and its successors, neglect time and interaction time, operator workload and situation awareness, levels of automation, trust in automation and the out-of-the-loop problem. **A gate written only in the vocabulary of aircraft would have returned none of it**, which is why this article's gate carries a second anchor family declared before the harvest rather than patched in afterwards.

**36 records.** [[Alexander et al 2000][research_alexander_nygren_2000]] [[Brooks 1989][research_brooks_1989]] [[Buerger and Cannon 2016][research_buerger_cannon_2016]] [[Calhoun et al 2017][research_calhoun_draper_2017]] [[Clare et al 2012][research_clare_ryan_2012]] [[Cuevas and Aguiar 2017][research_cuevas_aguiar_2017]] [[Cummings et al 2013][research_cummings_mastracchio_2013]] [[Doane 2003][research_doane_2003]] [[Donmez and Cummings 2010][research_donmez_cummings_2010]] [[Donmez et al 2009][research_donmez_cummings_2009]] [[Draper 2008][research_draper_2008]] [[Fontaine][research_fontaine]] [[Friedrich and Vollrath 2022][research_friedrich_vollrath_2022]] [[Fuchs et al 2013][research_fuchs_ferreira_2013]] [[Kidwell et al 2012][research_kidwell_calhoun_2012]] [[Kilgore et al 2009][research_kilgore_nehme_2009]] [[Lin et al 2015][research_lin_wohleber_2015]] [[McKendrick et al 2013][research_mckendrick_shaw_2013]] [[McLeod 2025][research_mcleod_2025]] [[McLeod 2025][research_mcleod_2025_b]] [[McLeod 2025][research_mcleod_2025_c]] [[McLeod 2025][research_mcleod_2025_d]] [[Mekdeci and Cummings 2009][research_mekdeci_cummings_2009]] [[Mercado-Ravell][research_mercadoravell]] [[Miller 2013][research_miller_2013]] [[Nelson and Bolia 2006][research_nelson_bolia_2006]] [[Nelson et al 2006][research_nelson_calhoun_2006]] [[Oliver 2012][research_oliver_2012]] [[Parasuraman et al 2013][research_parasuraman_kidwell_2013]] [[Roltgen and Gilbert 2010][research_roltgen_gilbert_2010]] [[Ruff et al 2002][research_ruff_narayanan_2002]] [[Scukins et al 2023][research_scukins_klein_2023]] [[Terwilliger and Ison 2014][research_terwilliger_ison_2014]] [[Theunissen et al 2005][research_theunissen_koeners_2005]] [[Zhang et al 2008][research_zhang_yang_2008]] [[Zheng et al 2019][research_zheng_wang_2019]]

### Internal weapons carriage and store separation

**A bay is a hole in a low observable aeroplane and opening it is the moment it stops being one.** Internal carriage, store separation, cavity flow and acoustics, and guided weapon delivery accuracy. **The X-45A released a weapon from an internal bay autonomously in 2004**, which required the separation problem to have been solved on the ground first.

**26 records.** [[Air-to-Air/Air-to-Ground Weapons Integration 2010][research_air_to_air_air_to_ground_weapons_2010]] [[American Airpower in World 2008][research_american_airpower_2008]] [[Anderson and Teope 2017][research_anderson_teope_2017]] [[Ben-Gida 2022][research_bengida_2022]] [[Cenko et al 1981][research_cenko_tinoco_1981]] [[Clark 1975][research_clark_1975]] [[Gong and Wang 2019][research_gong_wang_2019]] [[Gough, Jr. and Carlson 1979][research_goughjr_carlson_1979]] [[Hirlinger 2001][research_hirlinger_2001]] [[Klingelhoefer 2005][research_klingelhoefer_2005]] [[Lee 2010][research_lee_2010]] [[Loupy et al 2018][research_loupy_barakos_2018]] [[Nichols and Westmoreland 2007][research_nichols_westmoreland_2007]] [[Panickar et al 2013][research_panickar_murray_2013]] [[Shaw and Smith 1977][research_shaw_smith_1977]] [[Shaw et al 1988][research_shaw_clark_1988]] [[Sinha et al 2001][research_sinha_arunajatesan_2001]] [[Song and Ai 2021][research_song_ai_2021]] [[Stanek 2002][research_stanek_2002]] [[Stanek 2003][research_stanek_2003]] [[Stanek 2007][research_stanek_2007]] [[Tait et al 2009][research_tait_hatfield_2009]] [[Teng and Yu 2023][research_teng_yu_2023]] [[TRW to provide weapons 2002][research_trw_to_2002]] [[Weapons Carriage and Guidance 2006][research_weapons_carriage_2006]] [[Welterlen 2000][research_welterlen_2000]]

### Airframe structure, composites and affordability

**Affordability was a stated programme objective and not a consequence.** Composite structure, sandwich construction, producibility, tooling and cost. **The X-45A used a foam matrix core with a composite skin**, and the argument for an unmanned strike aircraft has always been partly that it can be built cheaply enough to lose.

**24 records.** [[Aircraft Manufacturing Considerations 2010][research_aircraft_manufacturing_2010]] [[Blair and Takahashi 2022][research_blair_takahashi_2022]] [[Brown and Timmerman 1991][research_brown_timmerman_1991]] [[Brunson and Rais-Rohani 1996][research_brunson_raisrohani_1996]] [[Dewa et al 2024][research_dewa_atami_2024]] [[Fisher 1950][research_fisher_1950]] [[Grover 1966][research_grover_1966]] [[Heimbs et al 2012][research_heimbs_lang_2012]] [[Herpers 1965][research_herpers_1965]] [[Hewitt et al 2005][research_hewitt_weiss_2005]] [[Jin et al 2011][research_jin_song_2011]] [[Kapidžić et al 2014][research_kapidzic_nilsson_2014]] [[Kundu and Raghunathan 2000][research_kundu_raghunathan_2000]] [[Lawrence and Mosnier 2009][research_lawrence_mosnier_2009]] [[Lindsey 1977][research_lindsey_1977]] [[Mayfield et al 2001][research_mayfield_baker_2001]] [[Pugazhenthi et al 2018][research_pugazhenthi_gopalakannan_2018]] [[Rarthlomeusz et al 1993][research_rarthlomeusz_paul_1993]] [[Saltzgaber and Miller 2003][research_saltzgaber_miller_2003]] [[Santoso and Hariyanto 2022][research_santoso_hariyanto_2022]] [[Smith 1968][research_smith_1968]] [[Stepanova 2025][research_stepanova_2025]] [[Wasmi and Rahim 2016][research_wasmi_rahim_2016]] [[Zhao and Kapania 2019][research_zhao_kapania_2019]]

### Datalink, latency and beyond-line-of-sight command

**The link is what makes supervision possible and what makes it fragile.** Datalinks, latency, beyond-line-of-sight satellite command, bandwidth, lost-link procedures and network-centric command and control. **A small cluster for a large subject**, because much of the operational literature on military links is not published where a bibliographic sweep can reach it.

**12 records.** [[Beffert and Zell 2026][research_beffert_zell_2026]] [[Carney 2008][research_carney_2008]] [[Cetin and Zagli 2011][research_cetin_zagli_2011]] [[Gray 2015][research_gray_2015]] [[Hess 2018][research_hess_2018]] [[Hunn 2005][research_hunn_2005]] [[Hutmacher 2011][research_hutmacher_2011]] [[Osterman 2010][research_osterman_2010]] [[Reichstein et al 2022][research_reichstein_schopferer_2022]] [[Yuan et al 2026][research_yuan_xue_2026]] [[Zhang et al 2024][research_zhang_dou_2024]] [[Zolanvari et al 2018][research_zolanvari_teixeira_2018]]

### Verification, validation and the certification of autonomous software

**The reason an autonomous combat aircraft is hard to field rather than hard to fly.** Verification and validation, certification, run-time assurance, safety cases, formal methods and redundancy management. **A demonstrator may fly on a waiver and a fielded aeroplane may not**, and the gap between those two states is where the J-UCAS programme spent its later years.

**11 records.** [[Butt and Markmiller 2023][research_butt_markmiller_2023]] [[Classification for Unmanned Aircraft][research_classification_for]] [[Cook 2024][research_cook_2024]] [[Gao et al 2021][research_gao_an_2021]] [[Habashi 2023][research_habashi_2023]] [[Klyde et al 2020][research_klyde_schulze_2020]] [[Methodology to Aircraft Design 2010][research_methodology_to_2010]] [[Panchal et al 2024][research_panchal_hein_2024]] [[Practices for Unmanned Aircraft][research_practices_for]] [[Shriwastav and Song 2020][research_shriwastav_song_2020]] [[Spreen 2019][research_spreen_2019_e]]

### Low observable design and signature

**Why the aeroplane has that shape and no fin.** Radar cross section, low observable planforms, serpentine inlet ducts, absorbing materials and infrared signature suppression. **The premise is taken from this literature and nothing in it is computed here.**

**10 records.** [[Altman 2008][research_altman_2008]] [[Fry 2008][research_fry_2008]] [[Gaitanakis et al 2020][research_gaitanakis_limnaios_2020]] [[Orhan 2020][research_orhan_2020]] [[Papageorgiou et al 2018][research_papageorgiou_tarkian_2018]] [[Paterson 1999][research_paterson_1999]] [[Paterson and Paterson 1997][research_paterson_paterson_1997]] [[Strattan 1978][research_strattan_1978]] [[Sutrakar et al 2025][research_sutrakar_kumari_2025]] [[Zhang et al 2026][research_zhang_yang_2026]]

### Suppression of enemy air defences and time-critical targeting

**The mission the vehicle was built for and the one that sets its clock.** Suppression of enemy air defences, emitter location, time-critical targeting, the kill chain, threat evaluation and jamming. **A mobile emitter that shuts down sets a deadline**, and whether the loop closes inside it is the question the mission poses to the autonomy.

**9 records.** [[Army War Coll Carlisle Barracks Pa 1982][research_armywarcollcarlislebarrackspa_1982]] [[Gaver and Jacobs 1998][research_gaver_jacobs_1998]] [[Heilenday 2000][research_heilenday_2000]] [[Horrigan 1990][research_horrigan_1990]] [[Mustopa 2022][research_mustopa_2022]] [[Stegall 2001][research_stegall_2001]] [[Suminsby 2002][research_suminsby_2002]] [[Sutton 2005][research_sutton_2005]] [[Sutton 2006][research_sutton_2006]]

### The atmosphere and the flight condition

**This cluster measured zero before the primary-reference pass and the article displays a relation that uses it.** The standard atmosphere, atmospheric property tables, the tropopause and the speed of sound. **A341's gate refused the U.S. Standard Atmosphere because `atmosphere` was not an anchor**, readmitted it by name for itself alone, and both following articles then harvested nothing. **A subject nobody searched for returns no records, and an absent cluster looks exactly like an absent literature.**

**2 records.** [[Du et al 2019][research_du_li_2019]] [[Wang et al 2021][research_wang_meng_2021]]


## The Source Base

**The argument rests on four documents and none of them is a Northrop Grumman engineering report.**

**One carries both aircraft.** The specialist designation directory gives the contract history, the designations, the dimensions, the engines, the payload and the X-47A's single flight and its purpose [[Parsch, Northrop Grumman X-47, Directory of U.S. Military Rockets and Missiles][ref_parsch_x47]]. **It is a secondary source, it is the best one available, and it warns that its own figures may be inaccurate.**

**One carries the chronology and the second set of dimensions.** The encyclopaedia entry supplies the wing area, the folded span, the weights and the full sequence of carrier firsts [[Northrop Grumman X-47B][ref_x47b_wikipedia]], and it disagrees with the directory about gross mass by six percent.

**One carries the landing.** The contemporary account of 10 July 2013 gives the wire caught, the speed, the stopping distance and the aborted third approach [[X-47B makes first arrested landing aboard an aircraft carrier][ref_first_trap]].

**One carries the deck.** The geometry of the arresting gear and the landing area is the basis of the precision calculation and comes from published descriptions of the Nimitz class [[Nimitz-class aircraft carrier][ref_nimitz_wikipedia]] [[Arresting gear][ref_arresting_gear_wikipedia]].

**No primary programme document was located.** No test report, no navigation performance analysis and no weight statement for either aircraft has been found in the open literature.

## Epistemic State

### Historical Fact

**In June 2000 the Defense Advanced Research Projects Agency awarded study contracts of two million dollars each to Northrop Grumman and Boeing** for a carrier-based unmanned combat aircraft.

**The X-47A Pegasus was completed in July 2001 and flew once, on 23 February 2003**, carrying a shipboard relative navigation system.

**In August 2007 the X-47B won the Unmanned Combat Air System Demonstration under a contract of 635.8 million dollars.** It first flew on 4 February 2011.

**On 14 May 2013 an X-47B was catapulted from USS George H.W. Bush and on 10 July 2013 one made an arrested landing aboard her**, catching the three-wire and then on a second approach the two-wire, with a third approach automatically aborted after a subsystem failure.

**In April 2015 an X-47B refuelled from a tanker autonomously**, and in May 2015 the primary test programme was declared complete.

### Verified by Independent Derivation

**A height error divides by the tangent of the glide slope to give a displacement along the deck**, which is 19.08 feet per foot at three degrees, 16.35 at three and a half and 14.30 at four.

**A pendant spacing of 40 to 50 feet corresponds to 2.10 to 3.50 feet of height** across glide slopes from three to four degrees.

**An arrestment from 145 knots in 350 feet is 26.08 metres per second squared, or 2.66 g, in 2.86 seconds**, and from 120 knots is 17.86 metres per second squared, or 1.82 g, in 3.46 seconds. **The energy is 56.2 megajoules at 20,185 kilograms and 145 knots.**

**The X-47B's aspect ratio is 4.04, its wing loading 43.9 pounds per square foot at 19,000 kilograms, its thrust to weight ratio 0.382, and its payload fraction 0.10737.**

### Analysis

**The deck sets a precision requirement of one metre or better in height** if a particular wire is to be chosen rather than accepted, and that requirement is on a measurement relative to a moving ship.

**The previous article's inherited payload fraction did not hold for this aeroplane**, and the direction of the failure is the one that article predicted.

**The approach speed constraint did not size this wing**, since the achieved wing loading is below every value that constraint implies.

### Inference

**The relative navigation system is what made the rest of the aeroplane ordinary**, inferred from the geometry rather than from any statement of achieved accuracy.

**The wing was sized by fuel volume or by low-speed handling margin rather than by approach speed**, inferred from the margin between the achieved wing loading and the constraint.

### What the Record Does Not Settle

**What accuracy the navigation system achieved.** No traceable figure has been found.

**Which speed the arrestment account means.** Airspeed and speed over the deck differ by the wind over the deck and the difference matters by a factor of one and a half.

**What the X-47B weighs empty.** Published figures conflate empty and zero-fuel weight and the two differ by the payload.

**Whether the aeroplane could have met the endurance the original naval requirement asked for.** Its range is published and its loiter is not.

## Out of Scope

**The X-45 and the X-46**, which are the previous two articles and are cited here only where this aeroplane's record bears on theirs.

**The operational programmes that followed**, which are outside this series because they carry no X designation.

**The arresting gear as a machine**, meaning the hydraulic engine, the purchase cable and the sheave dampers, which the survey covers and which this article treats only through the deceleration it produces.

**Satellite navigation as a subject**, including integer ambiguity resolution and integrity monitoring, which the survey covers and which this article uses only as far as the relative measurement.

## Conclusion

**The Northrop Grumman X-47B is the aeroplane that made a carrier deck a place an unmanned aircraft can use.**

**The binding unknown was never the aerodynamics and never the autonomy in the sense the word usually carries.** It was whether a position could be known with respect to a moving ship to the precision the deck demands. **The deck's geometry sets that precision and it is unforgiving**, because a glide slope converts height into distance at nineteen feet per foot, and the forty to fifty feet between arresting pendants is only two to three and a half feet of height.

**A metre of height error is half a wire.** That is why the programme's navigation was relative rather than absolute, and it is why an aeroplane that could do this could also be built to ordinary tolerances everywhere else.

**The record it left is the whole deck cycle.** Catapult launch in May 2013, arrested landing in July, night flying in 2014, operations alongside manned aircraft in the same pattern, and autonomous refuelling in 2015. **The third approach of 10 July 2013 was automatically abandoned after a subsystem failure**, and a demonstration that produced two traps and one correct refusal is worth more than three traps.

**This article also scores the previous one, which sized this requirement with no aeroplane to measure.** That article predicted a gross mass of 32,539 pounds from an inherited payload fraction of 0.12293, and named that fraction as its weakest assumption because a designer under carrier weight pressure might trade it rather than accept a larger aeroplane. **The X-47B carries the same payload as the X-45C at a fraction of 0.10737 and a mass 1.287 times the prediction.** It did both of the things that were predicted, and more of each than was predicted.

**One prediction held and one failed in a way worth keeping.** The thrust to weight ratio of 0.382 fell inside the assumed band. **The approach speed constraint, which that article used to size a wing, is satisfied by this aeroplane with a wide margin and therefore did not size its wing.** A constraint that binds in an argument and not in the hardware is a true constraint used in the wrong role, and that is the most useful thing this aeroplane says about the one before it.

## References

### Books

- [Etkin and Reid, Dynamics of flight][book_etkin_reid]
- [Knott, Shaeffer and Tuley, Radar cross section][book_knott]
- [Misra and Enge, Global Positioning System, signals, measurements and performance][book_misra_enge]
- [Raymer, Aircraft design, a conceptual approach][book_raymer]
- [Torenbeek, Synthesis of subsonic airplane design][book_torenbeek]
- [Wooldridge, Winged wonders, the story of the flying wings][book_wooldridge]

[book_etkin_reid]: https://openlibrary.org/works/OL19844466W
[book_knott]: https://openlibrary.org/works/OL18817543W
[book_misra_enge]: https://openlibrary.org/works/OL8016599W
[book_raymer]: https://openlibrary.org/works/OL17855977W
[book_torenbeek]: https://openlibrary.org/works/OL17631348W
[book_wooldridge]: https://openlibrary.org/works/OL5220705W

### Reference

- [Arresting gear][ref_arresting_gear_wikipedia]
- [Joint Precision Approach and Landing System, Collins Aerospace][ref_jpals_collins]
- [Navy's unmanned carrier aircraft performs first touch and go][ref_first_cat]
- [Nimitz-class aircraft carrier][ref_nimitz_wikipedia]
- [Northrop Grumman X-47A Pegasus][ref_x47a_wikipedia]
- [Northrop Grumman X-47B][ref_x47b_wikipedia]
- [Parsch, Northrop Grumman X-47, Directory of U.S. Military Rockets and Missiles][ref_parsch_x47]
- [Pratt and Whitney F100][ref_f100_wikipedia]
- [Tailhook][ref_tailhook_wikipedia]
- [Unmanned combat aerial vehicle][ref_ucav_wikipedia]
- [X-47B makes first arrested landing aboard an aircraft carrier][ref_first_trap]

[ref_arresting_gear_wikipedia]: https://en.wikipedia.org/wiki/Arresting_gear
[ref_f100_wikipedia]: https://en.wikipedia.org/wiki/Pratt_%26_Whitney_F100
[ref_first_cat]: https://news.usni.org/2013/05/20/navys-unmanned-carrier-aircraft-preforms-first-touch-and-go
[ref_first_trap]: https://news.usni.org/2013/07/10/new-carrier-age-in-carrier-aviation-takes-off-with-x-47b-landing
[ref_jpals_collins]: https://www.rtx.com/collinsaerospace/what-we-do/industries/military-and-defense/navigation/airborne-products/navigation-and-landing-systems/jpals
[ref_nimitz_wikipedia]: https://en.wikipedia.org/wiki/Nimitz-class_aircraft_carrier
[ref_parsch_x47]: https://www.designation-systems.net/dusrm/app4/x-47.html
[ref_tailhook_wikipedia]: https://en.wikipedia.org/wiki/Tailhook
[ref_ucav_wikipedia]: https://en.wikipedia.org/wiki/Unmanned_combat_aerial_vehicle
[ref_x47a_wikipedia]: https://en.wikipedia.org/wiki/Northrop_Grumman_X-47A_Pegasus
[ref_x47b_wikipedia]: https://en.wikipedia.org/wiki/Northrop_Grumman_X-47B

### Related Post

- [X-Planes: Aerojet X-8 Aerobee][related_post_a305_aerojet_x8]
- [X-Planes: Bell X-1][related_post_a298_bell_x1]
- [X-Planes: Bell X-14][related_post_a311_bell_x14]
- [X-Planes: Bell X-16][related_post_a313_bell_x16]
- [X-Planes: Bell X-2][related_post_a299_bell_x2]
- [X-Planes: Bell X-22][related_post_a319_bell_x22]
- [X-Planes: Bell X-5][related_post_a302_bell_x5]
- [X-Planes: Bell X-9 Shrike][related_post_a306_bell_x9]
- [X-Planes: Bensen X-25][related_post_a322_bensen_x25]
- [X-Planes: Boeing X-20 Dyna-Soar][related_post_a317_boeing_x20]
- [X-Planes: Boeing X-32][related_post_a329_boeing_x32]
- [X-Planes: Boeing X-37][related_post_a334_boeing_x37]
- [X-Planes: Boeing X-40][related_post_a337_boeing_x40]
- [X-Planes: Boeing X-45][related_post_a342_boeing_x45]
- [X-Planes: Boeing X-46][related_post_a343_boeing_x46]
- [X-Planes: Convair X-11][related_post_a308_convair_x11]
- [X-Planes: Convair X-12][related_post_a309_convair_x12]
- [X-Planes: Convair X-6][related_post_a303_convair_x6]
- [X-Planes: Curtiss-Wright X-19][related_post_a316_curtiss_wright_x19]
- [X-Planes: Douglas X-3 Stiletto][related_post_a300_douglas_x3]
- [X-Planes: Framing and the Research Aircraft Model][related_post_a297_framing]
- [X-Planes: Grumman X-29][related_post_a326_grumman_x29]
- [X-Planes: Hiller X-18][related_post_a315_hiller_x18]
- [X-Planes: Lockheed Martin X-33][related_post_a330_lockheed_martin_x33]
- [X-Planes: Lockheed Martin X-35][related_post_a332_lockheed_martin_x35]
- [X-Planes: Lockheed X-17][related_post_a314_lockheed_x17]
- [X-Planes: Lockheed X-27][related_post_a324_lockheed_x27]
- [X-Planes: Lockheed X-7][related_post_a304_lockheed_x7]
- [X-Planes: Martin Marietta X-23 PRIME and a Contested Assignment][related_post_a320_martin_marietta_x23]
- [X-Planes: Martin Marietta X-24][related_post_a321_martin_marietta_x24]
- [X-Planes: McDonnell Douglas X-36][related_post_a333_mcdonnell_douglas_x36]
- [X-Planes: Micro-Craft X-43 Hyper-X][related_post_a340_micro_craft_x43]
- [X-Planes: North American X-10][related_post_a307_north_american_x10]
- [X-Planes: North American X-15][related_post_a312_north_american_x15]
- [X-Planes: Northrop X-21][related_post_a318_northrop_x21]
- [X-Planes: Northrop X-4 Bantam][related_post_a301_northrop_x4]
- [X-Planes: Orbital Sciences X-34][related_post_a331_orbital_sciences_x34]
- [X-Planes: Orbital Sciences X-42][related_post_a339_orbital_sciences_x42]
- [X-Planes: Osprey X-28 Sea Skimmer][related_post_a325_osprey_x28]
- [X-Planes: Rockwell X-30 and the National Aero-Space Plane][related_post_a327_rockwell_x30]
- [X-Planes: Rockwell-MBB X-31][related_post_a328_rockwell_mbb_x31]
- [X-Planes: Ryan X-13 Vertijet][related_post_a310_ryan_x13]
- [X-Planes: Scaled Composites X-38][related_post_a335_scaled_composites_x38]
- [X-Planes: Schweizer X-26 Frigate][related_post_a323_schweizer_x26]
- [X-Planes: X-39, Reserved but Never Assigned][related_post_a336_x39_reserved_never_assigned]
- [X-Planes: X-41 Common Aero Vehicle][related_post_a338_x41_common_aero_vehicle]
- [X-Planes: X-44, One Designation and Two Aircraft][related_post_a341_x44_two_aircraft]

[related_post_a297_framing]: {% post_url 2025-10-06-x_planes_framing %}
[related_post_a298_bell_x1]: {% post_url 2025-10-07-x_planes_bell_x1 %}
[related_post_a299_bell_x2]: {% post_url 2025-10-08-x_planes_bell_x2 %}
[related_post_a300_douglas_x3]: {% post_url 2025-10-09-x_planes_douglas_x3 %}
[related_post_a301_northrop_x4]: {% post_url 2025-10-10-x_planes_northrop_x4 %}
[related_post_a302_bell_x5]: {% post_url 2025-10-11-x_planes_bell_x5 %}
[related_post_a303_convair_x6]: {% post_url 2025-10-12-x_planes_convair_x6 %}
[related_post_a304_lockheed_x7]: {% post_url 2025-10-13-x_planes_lockheed_x7 %}
[related_post_a305_aerojet_x8]: {% post_url 2025-10-14-x_planes_aerojet_x8 %}
[related_post_a306_bell_x9]: {% post_url 2025-10-15-x_planes_bell_x9 %}
[related_post_a307_north_american_x10]: {% post_url 2025-10-16-x_planes_north_american_x10 %}
[related_post_a308_convair_x11]: {% post_url 2025-10-17-x_planes_convair_x11 %}
[related_post_a309_convair_x12]: {% post_url 2025-10-18-x_planes_convair_x12 %}
[related_post_a310_ryan_x13]: {% post_url 2025-10-19-x_planes_ryan_x13 %}
[related_post_a311_bell_x14]: {% post_url 2025-10-20-x_planes_bell_x14 %}
[related_post_a312_north_american_x15]: {% post_url 2025-10-21-x_planes_north_american_x15 %}
[related_post_a313_bell_x16]: {% post_url 2025-10-22-x_planes_bell_x16 %}
[related_post_a314_lockheed_x17]: {% post_url 2025-10-23-x_planes_lockheed_x17 %}
[related_post_a315_hiller_x18]: {% post_url 2025-10-24-x_planes_hiller_x18 %}
[related_post_a316_curtiss_wright_x19]: {% post_url 2025-10-25-x_planes_curtiss_wright_x19 %}
[related_post_a317_boeing_x20]: {% post_url 2025-10-26-x_planes_boeing_x20 %}
[related_post_a318_northrop_x21]: {% post_url 2025-10-27-x_planes_northrop_x21 %}
[related_post_a319_bell_x22]: {% post_url 2025-10-28-x_planes_bell_x22 %}
[related_post_a320_martin_marietta_x23]: {% post_url 2025-10-29-x_planes_martin_marietta_x23 %}
[related_post_a321_martin_marietta_x24]: {% post_url 2025-10-30-x_planes_martin_marietta_x24 %}
[related_post_a322_bensen_x25]: {% post_url 2025-10-31-x_planes_bensen_x25 %}
[related_post_a323_schweizer_x26]: {% post_url 2025-11-01-x_planes_schweizer_x26 %}
[related_post_a324_lockheed_x27]: {% post_url 2025-11-02-x_planes_lockheed_x27 %}
[related_post_a325_osprey_x28]: {% post_url 2025-11-03-x_planes_osprey_x28 %}
[related_post_a326_grumman_x29]: {% post_url 2025-11-04-x_planes_grumman_x29 %}
[related_post_a327_rockwell_x30]: {% post_url 2025-11-05-x_planes_rockwell_x30 %}
[related_post_a328_rockwell_mbb_x31]: {% post_url 2025-11-06-x_planes_rockwell_mbb_x31 %}
[related_post_a329_boeing_x32]: {% post_url 2025-11-07-x_planes_boeing_x32 %}
[related_post_a330_lockheed_martin_x33]: {% post_url 2025-11-08-x_planes_lockheed_martin_x33 %}
[related_post_a331_orbital_sciences_x34]: {% post_url 2025-11-09-x_planes_orbital_sciences_x34 %}
[related_post_a332_lockheed_martin_x35]: {% post_url 2025-11-10-x_planes_lockheed_martin_x35 %}
[related_post_a333_mcdonnell_douglas_x36]: {% post_url 2025-11-11-x_planes_mcdonnell_douglas_x36 %}
[related_post_a334_boeing_x37]: {% post_url 2025-11-12-x_planes_boeing_x37 %}
[related_post_a335_scaled_composites_x38]: {% post_url 2025-11-13-x_planes_scaled_composites_x38 %}
[related_post_a336_x39_reserved_never_assigned]: {% post_url 2025-11-14-x_planes_x39_reserved_never_assigned %}
[related_post_a337_boeing_x40]: {% post_url 2025-11-15-x_planes_boeing_x40 %}
[related_post_a338_x41_common_aero_vehicle]: {% post_url 2025-11-16-x_planes_x41_common_aero_vehicle %}
[related_post_a339_orbital_sciences_x42]: {% post_url 2025-11-17-x_planes_orbital_sciences_x42 %}
[related_post_a340_micro_craft_x43]: {% post_url 2025-11-18-x_planes_micro_craft_x43_hyper_x %}
[related_post_a341_x44_two_aircraft]: {% post_url 2025-11-19-x_planes_x44_one_designation_two_aircraft %}
[related_post_a342_boeing_x45]: {% post_url 2025-11-20-x_planes_boeing_x45 %}
[related_post_a343_boeing_x46]: {% post_url 2025-11-21-x_planes_boeing_x46 %}

### Research

- [A Prediction Method for 2017][research_a_prediction_2017]
- [A psychological evaluation of 1972][research_a_psychological_1972]
- [A testing platform which 1950][research_a_testing_1950]
- [A.V. Ananyev 2019][research_avananyev_2019]
- [A340-600 wing completes UK 2002][research_a340_600_wing_2002]
- [Aamir et al 2026][research_aamir_benhamida_2026]
- [Abas et al 2013][research_abas_pebrianti_2013]
- [Abbasi and Haeri 2019][research_abbasi_haeri_2019]
- [Abdel-Hafez et al 2003][research_abdelhafez_lee_2003]
- [Abdel-Hafez et al 2004][research_abdelhafez_speyer_2004]
- [Abdelrahman et al 2009][research_abdelrahman_elnomrossy_2009]
- [Abouheaf et al 2019][research_abouheaf_mailhot_2019]
- [Abouzahr and Jacob 2023][research_abouzahr_jacob_2023]
- [Abu-Akeel 1968][research_abuakeel_1968]
- [Abu-Akeel 1969][research_abuakeel_1969]
- [Aburime][research_aburime]
- [Abwanzo 2016][research_abwanzo_2016]
- [Acerra Gil and Guimaraes 2019][research_acerragil_guimaraes_2019]
- [Acharya et al 2021][research_acharya_sinha_2021]
- [Acosta et al 2016][research_acosta_decos_2016]
- [Acuna et al 2018][research_acuna_zhang_2018]
- [Adams 2000][research_adams_2000]
- [Adams and Hatch, Jr. 1970][research_adams_hatchjr_1970]
- [Adams and Moen 1967][research_adams_moen_1967]
- [Adamski 2021][research_adamski_2021]
- [Adelgren et al 2004][research_adelgren_minor_2004]
- [Adhikari 2021][research_adhikari_2021]
- [Adhikari 2021][research_adhikari_2021_b]
- [Advanced Aircraft Control 2026][research_advanced_aircraft_2026]
- [Aerodynamic Data of Real 2010][research_aerodynamic_data_2010]
- [Aerodynamics 2024][research_aerodynamics_2024]
- [Aerospace ID Technologies Research 2006][research_aerospace_id_2006]
- [Aerospace Landing GEAR Systems][research_aerospace_landing]
- [Aerospace Quality Management 2004][research_aerospace_quality_2004]
- [Aerospace series - Programme][research_aerospace_series_e]
- [Aerospace series - Programme][research_aerospace_series_h]
- [Aerospace series - Programme][research_aerospace_series_k]
- [Aerospace series. Programme Management][research_aerospace_series_b]
- [Aerospace series. Programme Management][research_aerospace_series_d]
- [Aerospace series. Programme management][research_aerospace_series_f]
- [Aerospace series. Programme Management][research_aerospace_series_g]
- [Aerospace series. Programme management][research_aerospace_series_i]
- [Aerospace series. Unmanned Aircraft][research_aerospace_series]
- [Aerospace series�� Programme management��][research_aerospace_series_c]
- [Aerospace series�� Programme management��][research_aerospace_series_j]
- [Aerospace supplier programme 2004][research_aerospace_supplier_2004]
- [Aftatah and Zebbara 2024][research_aftatah_zebbara_2024]
- [Aftatah et al 2026][research_aftatah_khalil_2026]
- [Agarwal et al 2008][research_agarwal_arya_2008]
- [Agarwal et al 2021][research_agarwal_ng_2021]
- [Agenbag et al 2009][research_agenbag_theron_2009]
- [Agrawal 1984][research_agrawal_1984]
- [Agrawal et al 2025][research_agrawal_rai_2025]
- [Agte et al 1997][research_agte_hadley_1997]
- [Aguiar and Pascoal 2012][research_aguiar_pascoal_2012]
- [Ahlrich 1991][research_ahlrich_1991]
- [Ahmad and Narmeen 2026][research_ahmad_narmeen_2026]
- [Ahmed et al 2026][research_ahmed_stanziano_2026]
- [Ahn et al 2022][research_ahn_kim_2022]
- [Air cargo equipment. Base-restrained][research_air_cargo_c]
- [Air cargo equipment. Wide][research_air_cargo]
- [Air cargo equipment. Wide][research_air_cargo_b]
- [Air Combat Command 2011][research_aircombatcommand_2011]
- [Air Combat Command Langley Afb Va 2000][research_aircombatcommandlangleyafbva_2000]
- [Air Combat Command Langley Afb Va 2013][research_aircombatcommandlangleyafbva_2013]
- [Air Force District Of Washington 2015][research_airforcedistrictofwashington_2015]
- [Air Proving Ground Center Eglin Afb Fl 1944][research_airprovinggroundcentereglinafbfl_1944]
- [Air Proving Ground Center Eglin Afb Fl 1949][research_airprovinggroundcentereglinafbfl_1949]
- [Air Proving Ground Center Eglin Afb Fl 1954][research_airprovinggroundcentereglinafbfl_1954]
- [Air Proving Ground Center Eglin Afb Fl 1954][research_airprovinggroundcentereglinafbfl_1954_b]
- [Air Proving Ground Center Eglin Afb Fl 1955][research_airprovinggroundcentereglinafbfl_1955]
- [Air Proving Ground Center Eglin Afb Fl 1955][research_airprovinggroundcentereglinafbfl_1955_b]
- [Air Univ Maxwell Afb Al 1978][research_airunivmaxwellafbal_1978]
- [Air-to-Air/Air-to-Ground Weapons Integration 2010][research_air_to_air_air_to_ground_weapons_2010]
- [Airborne Landing Guidance System][research_airborne_landing]
- [Airborne Windshear Systems][research_airborne_windshear]
- [Aircraft Automatic Approach and 1996][research_aircraft_automatic_1996]
- [Aircraft Carrier 2005][research_aircraft_carrier_2005]
- [Aircraft carrier base 1987][research_aircraft_carrier_1987]
- [Aircraft Case Studies 2026][research_aircraft_case_2026]
- [Aircraft Characteristics 2022][research_aircraft_characteristics_2022]
- [Aircraft Circuit Breaker and][research_aircraft_circuit]
- [Aircraft Conceptual Design 2012][research_aircraft_conceptual_2012]
- [Aircraft Control 2011][research_aircraft_control_2011]
- [Aircraft Cost Considerations 2010][research_aircraft_cost_2010]
- [Aircraft Design A Conceptual 2024][research_aircraft_design_2024]
- [Aircraft design at the 1993][research_aircraft_design_1993]
- [Aircraft Design Fundamentals 2012][research_aircraft_design_2012]
- [Aircraft Design Optimization 2013][research_aircraft_design_2013]
- [Aircraft Drag 2010][research_aircraft_drag_2010]
- [Aircraft Dynamics and Classical 2015][research_aircraft_dynamics_2015]
- [Aircraft Flight Control 2014][research_aircraft_flight_2014]
- [Aircraft Flotation Analysis][research_aircraft_flotation]
- [Aircraft Flotation Analysis Methods][research_aircraft_flotation_b]
- [Aircraft ground equipment. Design][research_aircraft_ground_b]
- [Aircraft ground equipment. Lower][research_aircraft_ground_c]
- [Aircraft ground equipment. Main][research_aircraft_ground_f]
- [Aircraft ground equipment. Upper][research_aircraft_ground_d]
- [Aircraft ground equipment. Upper][research_aircraft_ground_e]
- [Aircraft Ground Flotation Analysis][research_aircraft_ground]
- [Aircraft improvement programme at 2002][research_aircraft_improvement_2002]
- [Aircraft Landing GEAR][research_aircraft_landing]
- [Aircraft Landing Measurement System 1971][research_aircraft_landing_1971]
- [Aircraft lateral-directional handling qualities 2011][research_aircraft_lateral_directional_2011]
- [Aircraft Load 2010][research_aircraft_load_2010]
- [Aircraft longitudinal handling qualities 2011][research_aircraft_longitudinal_2011]
- [Aircraft Manufacturing Considerations 2010][research_aircraft_manufacturing_2010]
- [Aircraft Mechanics 2026][research_aircraft_mechanics_2026]
- [Aircraft Non-Linear Dynamics Equations 2014][research_aircraft_non_linear_2014]
- [Aircraft Operating Envelope 2010][research_aircraft_operating_2010]
- [Aircraft Oxygen Replenishment Coupling][research_aircraft_oxygen]
- [Aircraft Payload Limits for 1970][research_aircraft_payload_1970]
- [Aircraft Performance 2010][research_aircraft_performance_2010_b]
- [Aircraft Performance 2026][research_aircraft_performance_2026]
- [Aircraft Performance Methods 2010][research_aircraft_performance_2010]
- [Aircraft Prototype and Technology 1983][research_aircraft_prototype_1983]
- [Aircraft Response Transfer Functions 1997][research_aircraft_response_1997]
- [Aircraft Response Transfer Functions 2013][research_aircraft_response_2013]
- [Aircraft Seat Design Guidance][research_aircraft_seat]
- [Aircraft Simulation Model 2022][research_aircraft_simulation_2022]
- [Aircraft Sizing, Engine Matching 2010][research_aircraft_sizing_2010]
- [Aircraft Stability and Control 2026][research_aircraft_stability_2026]
- [Aircraft Stability Derivatives 1998][research_aircraft_stability_1998]
- [Aircraft TIRE Condition Monitoring][research_aircraft_tire_b]
- [Aircraft Tire Pressure Monitoring][research_aircraft_tire]
- [Aircraft Tires Key Principles 2022][research_aircraft_tires_2022]
- [Aircraft Weight and Center 2010][research_aircraft_weight_2010]
- [Aircraft Weight Distribution 2012][research_aircraft_weight_2012]
- [Aircraft Weights Data 2010][research_aircraft_weights_2010]
- [Aircraft Wheels, Brakes, and 2022][research_aircraft_wheels_2022]
- [Aircraft with annular wing 2001][research_aircraft_with_2001]
- [Aircraft. Declaration of design][research_aircraft_declaration]
- [Aircraft. Passenger doors interface][research_aircraft_passenger]
- [Airfoil and Wing/Tail Geometry 2024][research_airfoil_and_2024]
- [Airframe Avionics and Systems 2017][research_airframe_avionics_2017]
- [Ajaj et al 2013][research_ajaj_friswell_2013]
- [Akagi and McLain 2025][research_akagi_mclain_2025]
- [Akagi et al 2020][research_akagi_christensen_2020]
- [Akca and Demirekler 2012][research_akca_demirekler_2012]
- [Al-Hiddabi and McClamroch 2002][research_alhiddabi_mcclamroch_2002]
- [Alaeiyan and Mosavi 2026][research_alaeiyan_mosavi_2026]
- [Alam et al 2011][research_alam_nguyen_2011]
- [Alarcon et al 2015][research_alarcon_santamaria_2015]
- [Aldrich and Krabill 1972][research_aldrich_krabill_1972]
- [ALE-a carrier aircraft availability 1977][research_ale_a_carrier_1977]
- [Aleisa et al 2023][research_aleisa_kontis_2023]
- [Aleisa et al 2023][research_aleisa_kontis_2023_b]
- [Alexander 2025][research_alexander_2025]
- [Alexander 2025][research_alexander_2025_b]
- [Alexander et al 2000][research_alexander_nygren_2000]
- [Alexandrov et al 1980][research_alexandrov_kazakov_1980]
- [Alexopoulos et al 2017][research_alexopoulos_kirsch_2017]
- [Alford 1999][research_alford_1999]
- [Alhosban 2019][research_alhosban_2019]
- [Ali and Al-Shamma 2026][research_ali_alshamma_2026]
- [Ali and Jiancheng 2005][research_ali_jiancheng_2005]
- [Ali Dehghani and Bagher Menhaj 2016][research_alidehghani_baghermenhaj_2016]
- [Ali et al 2024][research_ali_abbas_2024]
- [Alijani and Osman 2021][research_alijani_osman_2021]
- [Alipour et al 2022][research_alipour_shahiashtiani_2022]
- [Allard 1982][research_allard_1982]
- [Allen][research_allen]
- [Allen 2009][research_allen_2009]
- [Allen and Breitsamter 2008][research_allen_breitsamter_2008]
- [Allende-Alba et al 2018][research_allendealba_montenbruck_2018]
- [Alley et al 2010][research_alley_steele_2010]
- [Almagbile et al 2010][research_almagbile_wang_2010]
- [Alonso da Silva 2019][research_alonsodasilva_2019]
- [Alsayed et al 2022][research_alsayed_nabawy_2022]
- [Altman 2008][research_altman_2008]
- [Altman 2015][research_altman_2015]
- [Altman 2019][research_altman_2019]
- [Altmann 2013][research_altmann_2013]
- [Altynova et al 2011][research_altynova_wasser_2011]
- [Aluc and Komurgoz 2023][research_aluc_komurgoz_2023]
- [Alvarez and Wissa 2021][research_alvarez_wissa_2021]
- [Aly et al 2002][research_aly_ogot_2002]
- [Alyanak and Pendleton 2014][research_alyanak_pendleton_2014]
- [Amadori et al 2019][research_amadori_jouannet_2019]
- [Ambler and Smith 1974][research_ambler_smith_1974]
- [American Airpower in World 2008][research_american_airpower_2008]
- [Amiri-Simkooei et al 2015][research_amirisimkooei_jazaeri_2015]
- [Amzajerdian et al 2026][research_amzajerdian_gragossian_2026]
- [An and Kim 2025][research_an_kim_2025]
- [An et al 2019][research_an_meng_2019]
- [An et al 2023][research_an_krzysiak_2023]
- [Analysis and Design of 2020][research_analysis_and_2020]
- [Analytical Methods for Aircraft][research_analytical_methods]
- [Andersen et al 1993][research_andersen_hauge_1993]
- [Anderson 1973][research_anderson_1973]
- [Anderson 1996][research_anderson_1996]
- [Anderson and Teope 2017][research_anderson_teope_2017]
- [Andrews, L. Cullen et al 1988][research_andrewslcullen_augsburgerbill_1988]
- [Angell 2009][research_angell_2009]
- [Anggoro 2021][research_anggoro_2021]
- [Anton et al 2012][research_anton_erturk_2012]
- [Antonini 1993][research_antonini_1993]
- [Antony et al 2024][research_antony_kumar_2024]
- [Anum et al 2022][research_anum_liaquat_2022]
- [Anwendungsbeispiel GPS/INS-Integration 2007][research_anwendungsbeispiel_gps_ins_integration_2007]
- [Anwendungsbeispiel GPS/INS-Integration 2011][research_anwendungsbeispiel_gps_ins_integration_2011]
- [Anđić 2021][research_andic_2021]
- [Aoyama et al 1995][research_aoyama_kawachi_1995]
- [Apeng et al 2018][research_apeng_shu_2018]
- [Appendix D Comparison of 2004][research_appendix_d_2004]
- [Appendix G Aerodynamic Data 2010][research_appendix_g_2010]
- [Appleman 1957][research_appleman_1957]
- [Application of quasi-object control 2008][research_application_of_quasi_object_2008]
- [Approach to Landing Guidance][research_approach_to]
- [Arai 2000][research_arai_2000]
- [Ardaens et al 2013][research_ardaens_damico_2013]
- [Argrow 2016][research_argrow_2016]
- [Argrow et al 2008][research_argrow_weatherhead_2008]
- [Armed Forces Health Surveillance Center 2014][research_armedforceshealthsurveillancecenter_2014]
- [Armed Forces Health Surveillance Center 2015][research_armedforceshealthsurveillancecenter_2015]
- [Armed Forces Health Surveillance Center 2015][research_armedforceshealthsurveillancecenter_2015_b]
- [Armstrong 2018][research_armstrong_2018]
- [Army Aviation Center And Fort Rucker Al 1992][research_armyaviationcenterandfortruckeral_1992]
- [Army Aviation Materiel Labs Fort Eustis Va 1963][research_armyaviationmateriellabsforteustisva_1963]
- [Army Safety Center Fort Rucker Al 1991][research_armysafetycenterfortruckeral_1991]
- [Army Safety Center Fort Rucker Al 1991][research_armysafetycenterfortruckeral_1991_b]
- [Army Safety Center Fort Rucker Al 1999][research_armysafetycenterfortruckeral_1999]
- [Army Safety Center Fort Rucker Al 1999][research_armysafetycenterfortruckeral_1999_b]
- [Army Service Forces Washington Dc 1940][research_armyserviceforceswashingtondc_1940]
- [Army War Coll Carlisle Barracks Pa 1982][research_armywarcollcarlislebarrackspa_1982]
- [Army War Coll Carlisle Barracks Pa 2006][research_armywarcollcarlislebarrackspa_2006]
- [Arora et al 2022][research_arora_carlson_2022]
- [Ascani 1974][research_ascani_1974]
- [Ascher et al 2011][research_ascher_zwirello_2011]
- [Ashenberg and Weihs 1984][research_ashenberg_weihs_1984]
- [Asher et al 1975][research_asher_mitchell_1975]
- [Ashkenas 1965][research_ashkenas_1965]
- [Ashkenas 1965][research_ashkenas_1965_b]
- [Ashkenas 1965][research_ashkenas_1965_c]
- [Ashkenas 1982][research_ashkenas_1982]
- [Ashkenas, Irving L. and Klyde, David H. 1989][research_ashkenasirvingl_klydedavidh_1989]
- [Ashokkumar 2023][research_ashokkumar_2023]
- [Ashraf et al 2019][research_ashraf_naqvi_2019]
- [Aslan and Oktay 2023][research_aslan_oktay_2023]
- [Assessment of the state-of-the-art 1979][research_assessment_of_1979]
- [ASTM International Standard helps 2007][research_astm_international_2007]
- [Atay et al 2021][research_atay_bryant_2021]
- [Ateş 2022][research_ates_2022]
- [Atkins and Di Donato 2016][research_atkins_didonato_2016]
- [Atkinson 1990][research_atkinson_1990]
- [Atmaca et al 2026][research_atmaca_stroosma_2026]
- [Attinello 1956][research_attinello_1956]
- [Attitude control system of 1994][research_attitude_control_1994]
- [Aubert et al 2016][research_aubert_ross_2016]
- [Automation and Autonomy in 2016][research_automation_and_2016]
- [Autonomous Control of Unmanned 2012][research_autonomous_control_2012]
- [Autonomous Control of Unmanned 2019][research_autonomous_control_2019]
- [Autonomous unmanned aircraft RandD 1994][research_autonomous_unmanned_1994]
- [Autopilot, Flight Director, and][research_autopilot_flight]
- [Autry and Victorazzo 2019][research_autry_victorazzo_2019]
- [Avery and Jacob 2017][research_avery_jacob_2017]
- [Avery et al 2019][research_avery_bunting_2019]
- [Aviation And Troop Command Army St Louis Mo 1995][research_aviationandtroopcommandarmystlouismo_1995]
- [Aviation History and UAS][research_aviation_history]
- [Awadalla Ali Haj Ahmed 2024][research_awadallaalihajahmed_2024]
- [Ayar and Karakoc 2023][research_ayar_karakoc_2023]
- [Aygün et al 2014][research_aygun_tascioglu_2014]
- [Azer et al 2024][research_azer_colpan_2024]
- [Azimi-Sadjadi and Krishnaprasad 2001][research_azimisadjadi_krishnaprasad_2001]
- [Azimov and Bishop 2025][research_azimov_bishop_2025]
- [Azizi and Khorasani 2011][research_azizi_khorasani_2011]
- [B and Gupta 2026][research_b_gupta_2026]
- [Babetto and Stumpf 2021][research_babetto_stumpf_2021]
- [Bachelder and Aponso 2020][research_bachelder_aponso_2020]
- [Bachelder and Aponso 2020][research_bachelder_aponso_2020_b]
- [Bachelder et al 2023][research_bachelder_aponso_2023]
- [Bachman 1988][research_bachman_1988]
- [Backing for Aviation Centenary 2009][research_backing_for_2009]
- [Baek and York 2020][research_baek_york_2020]
- [Bagdatli et al 2019][research_bagdatli_karagoz_2019]
- [Bahamonde Jacome and Elham 2017][research_bahamondejacome_elham_2017]
- [Bahr et al 2021][research_bahr_mckay_2021]
- [Bahrami and Jafarnejadsani 2022][research_bahrami_jafarnejadsani_2022]
- [Bai and Taylor 2020][research_bai_taylor_2020]
- [Bai and Zhang 2011][research_bai_zhang_2011]
- [Bai et al 2014][research_bai_mingqiang_2014]
- [Baily and Gilbertson 1980][research_baily_gilbertson_1980]
- [Bainum and Diarra 1988][research_bainum_diarra_1988]
- [Bainum et al 2005][research_bainum_tan_2005]
- [Baisden et al 1977][research_baisden_ambler_1977]
- [Bajurko 2019][research_bajurko_2019]
- [Baker 1955][research_baker_1955]
- [Baker et al 2000][research_baker_brennan_2000]
- [Balabanov and Haftka 1996][research_balabanov_haftka_1996]
- [Balard et al 2005][research_balard_santerre_2005]
- [Bald 1957][research_bald_1957]
- [Ballou 1963][research_ballou_1963]
- [Banerjee and Taneja 2026][research_banerjee_taneja_2026]
- [Banks 2000][research_banks_2000]
- [Bao et al 2017][research_bao_lai_2017]
- [Baralli et al 2002][research_baralli_pollini_2002]
- [Baranov and Chernov 2019][research_baranov_chernov_2019]
- [Barbatei et al 2015][research_barbatei_skavhaug_2015]
- [Barbier and Chanthery 2004][research_barbier_chanthery_2004]
- [Bardera et al 2019][research_bardera_barcalamontejano_2019]
- [Bardera-Mora et al 2018][research_barderamora_garciamagarino_2018]
- [Bardera-Mora et al 2019][research_barderamora_garciamagarino_2019]
- [Bardhan et al 2017][research_bardhan_bera_2017]
- [Barlow 2004][research_barlow_2004]
- [Barnes 1968][research_barnes_1968]
- [Barnett 1961][research_barnett_1961]
- [Barnhart 2012][research_barnhart_2012]
- [Barthelemy et al 1994][research_barthelemy_coen_1994]
- [Barton][research_barton]
- [Bartsch 2018][research_bartsch_2018]
- [Baselga et al 2009][research_baselga_garciaasenjo_2009]
- [Basic Aircraft Oxygen Systems][research_basic_aircraft]
- [Basic Principles for the 2012][research_basic_principles_for_2012]
- [Basil et al 2004][research_basil_anathasayanam_2004]
- [Bason et al 1976][research_bason_macintyre_1976]
- [Bass 2006][research_bass_2006]
- [Bass 2013][research_bass_2013]
- [Bastiaens et al 2021][research_bastiaens_mommerency_2021]
- [Bateman et al 2007][research_bateman_nelson_2007]
- [Batill and Bacarro 1988][research_batill_bacarro_1988]
- [Batill et al 1999][research_batill_stelmack_1999]
- [Baughman and Longeauay 2015][research_baughman_longeauay_2015]
- [Baum 2021][research_baum_2021]
- [Baum 2021][research_baum_2021_b]
- [Bautista et al 2023][research_bautista_gutierrez_2023]
- [Baxter 2013][research_baxter_2013]
- [Bayraktar et al 2004][research_bayraktar_fainekos_2004]
- [Bean 2015][research_bean_2015]
- [Bechelder et al 2025][research_bechelder_bjorkman_2025]
- [Beech Announces Wing Structure 1982][research_beech_announces_1982]
- [Beffert and Zell 2026][research_beffert_zell_2026]
- [Bejan 2010][research_bejan_2010]
- [Beklemishchev and Tikhonov 2021][research_beklemishchev_tikhonov_2021]
- [Belabbas][research_belabbas]
- [Belai 2025][research_belai_2025]
- [Belart 1938][research_belart_1938]
- [Belfadel et al 2023][research_belfadel_haessig_2023]
- [Belfadel et al 2024][research_belfadel_haessig_2024]
- [Bell 1993][research_bell_1993]
- [Bell 1997][research_bell_1997]
- [Bell Aerospace Co Buffalo Ny 1956][research_bellaerospacecobuffalony_1956]
- [Belloni et al 2024][research_belloni_silvestrini_2024]
- [Belta 2012][research_belta_2012]
- [Belta 2012][research_belta_2012_b]
- [Ben-Gida 2022][research_bengida_2022]
- [Ben-Ishai et al 2001][research_benishai_reiner_2001]
- [Bendarkar et al 2013][research_bendarkar_pant_2013]
- [Benders 2018][research_benders_2018]
- [Benders and Koch 2019][research_benders_koch_2019]
- [Benders et al 2018][research_benders_wenz_2018]
- [Bendix Corp York Pa 1963][research_bendixcorpyorkpa_1963]
- [Benitez et al 2023][research_benitez_rutherford_2023]
- [Bennett][research_bennett]
- [Benzerrouk et al 2020][research_benzerrouk_landry_2020]
- [Berbaum et al 1991][research_berbaum_kennedy_1991]
- [Berberi et al 2020][research_berberi_segre_2020]
- [Berens 2003][research_berens_2003]
- [Berger et al 2011][research_berger_carmona_2011]
- [Berger et al 2019][research_berger_horn_2019]
- [Berger et al 2022][research_berger_blanken_2022]
- [Berger et al 2025][research_berger_christensen_2025]
- [Berger et al 2026][research_berger_bonzatto_2026]
- [Bergeron et al 2011][research_bergeron_tavan_2011]
- [Bergman 1979][research_bergman_1979]
- [Berkshire 1967][research_berkshire_1967]
- [Berman 1997][research_berman_1997]
- [Bernardin 1961][research_bernardin_1961]
- [Berry 1986][research_berry_1986]
- [Berry 2000][research_berry_2000]
- [Berry and Powers 1970][research_berry_powers_1970]
- [Beser 1978][research_beser_1978]
- [Beser 1979][research_beser_1979]
- [Best 1986][research_best_1986]
- [Bestaoui and Lakhlef 2013][research_bestaoui_lakhlef_2013]
- [Bever et al 2002][research_bever_urschel_2002]
- [Beyer and Mansir 1987][research_beyer_mansir_1987]
- [Bezandry et al 2016][research_bezandry_raglin_2016]
- [Bhamidipati and Gao 2020][research_bhamidipati_gao_2020]
- [Bhandari and O'Keefe 2017][research_bhandari_okeefe_2017]
- [Bhandari et al 2013][research_bhandari_thomas_2013]
- [Bhatia et al 2021][research_bhatia_jiang_2021]
- [Bhattacharyya 2016][research_bhattacharyya_2016]
- [Bhattacharyya 2023][research_bhattacharyya_2023]
- [Bhattacharyya 2025][research_bhattacharyya_2025]
- [Bhattacharyya and Mute 2020][research_bhattacharyya_mute_2020]
- [Bhattacharyya et al 2019][research_bhattacharyya_mute_2019]
- [Bian et al 2018][research_bian_nener_2018]
- [Bian et al 2022][research_bian_nener_2022]
- [Biber 2023][research_biber_2023]
- [Biber et al 2004][research_biber_ol_2004]
- [Bibin et al 2012][research_bibin_selvaraj_2012]
- [Biggerstaff 1998][research_biggerstaff_1998]
- [Bihrle, Jr. 1969][research_bihrlejr_1969]
- [Bil 1989][research_bil_1989]
- [Bil et al 2015][research_bil_zegers_2015]
- [Billec 1967][research_billec_1967]
- [Binder et al 2001][research_binder_holcomb_2001]
- [Bindolino et al 2010][research_bindolino_ghiringhelli_2010]
- [Binjammaz et al 2013][research_binjammaz_albayatti_2013]
- [Birkeland 2013][research_birkeland_2013]
- [Birkenhead 2024][research_birkenhead_2024]
- [Bishop and Antoulas 1991][research_bishop_antoulas_1991]
- [Bishop and Antoulas 1994][research_bishop_antoulas_1994]
- [Biswal M 2023][research_biswalm_2023]
- [Bittrick 1984][research_bittrick_1984]
- [Black 1968][research_black_1968]
- [Blair and Takahashi 2022][research_blair_takahashi_2022]
- [Blask 2002][research_blask_2002]
- [Bletsos 1986][research_bletsos_1986]
- [Blewitt 2008][research_blewitt_2008]
- [Bloch 1989][research_bloch_1989]
- [Blodgett and Lagor 2022][research_blodgett_lagor_2022]
- [Blumer 1963][research_blumer_1963]
- [Board technology lowers mil/aerospace 2005][research_board_technology_2005]
- [Bodson and Athans 1985][research_bodson_athans_1985]
- [Bogdan 2015][research_bogdan_2015]
- [Bohao et al 2026][research_bohao_daochun_2026]
- [Bolds 1961][research_bolds_1961]
- [Bolds 1962][research_bolds_1962]
- [Bolla and Won 2018][research_bolla_won_2018]
- [Bolonkin 2005][research_bolonkin_2005]
- [Bolonkin 2005][research_bolonkin_2005_b]
- [bolter 0 2023][research_bolter_0_2023]
- [bolter boulter, n.¹ 2023][research_bolter_boulter_2023]
- [Bolter, Albert Ernest, 29 2007][research_bolter_albert_2007]
- [bolter, n.² 2023][research_bolter_n_2_2023]
- [Bolzak 1989][research_bolzak_1989]
- [Bona 2000][research_bona_2000]
- [Bonetti et al 2013][research_bonetti_dezaiacomo_2013]
- [Boo et al 2015][research_boo_mansor_2015]
- [Bookstaber 2000][research_bookstaber_2000]
- [Booz 1988][research_booz_1988]
- [Booz 1998][research_booz_1998]
- [Booz-Allen And Hamilton Inc Mclean Va 2000][research_boozallenandhamiltonincmcleanva_2000]
- [Borgen and Mott 2024][research_borgen_mott_2024]
- [Borrelli et al 2006][research_borrelli_subramanian_2006]
- [Bortner 2009][research_bortner_2009]
- [Boskovic and Jackson 2016][research_boskovic_jackson_2016]
- [Boskovic and Mehra 1999][research_boskovic_mehra_1999]
- [Boskovic and Mehra 2000][research_boskovic_mehra_2000]
- [Boskovic and Redding 2009][research_boskovic_redding_2009]
- [Boskovic et al][research_boskovic_saimingli]
- [Boskovic et al 2021][research_boskovic_diel_2021]
- [Bostian and Young 2011][research_bostian_young_2011]
- [Bouadi and Mora-Camino 2012][research_bouadi_moracamino_2012]
- [Boudreault 1983][research_boudreault_1983]
- [Boullianne 1997][research_boullianne_1997]
- [Bourdin et al 2007][research_bourdin_gatto_2007]
- [Bourgeois][research_bourgeois]
- [Boutros 2015][research_boutros_2015]
- [Bowman, James S. 1965][research_bowmanjamess_1965]
- [Boyd and Scharf 2022][research_boyd_scharf_2022]
- [Boyuk et al 2020][research_boyuk_duvar_2020]
- [Braasch 2006][research_braasch_2006]
- [Brack 2014][research_brack_2014]
- [Brack 2016][research_brack_2016]
- [Brack 2017][research_brack_2017]
- [Brack 2020][research_brack_2020]
- [Bradley et al 2012][research_bradley_gardhagen_2012]
- [Bradshaw and Brunter 1975][research_bradshaw_brunter_1975]
- [Braff 2008][research_braff_2008]
- [Braff and Loh 1992][research_braff_loh_1992]
- [Braff et al 2012][research_braff_bian_2012]
- [Bramsiepe et al 2020][research_bramsiepe_voss_2020]
- [Brand and Dresksler 1995][research_brand_dresksler_1995]
- [Brauckmann, Gregory J. 1998][research_brauckmanngregoryj_1998]
- [Bray 1963][research_bray_1963]
- [Breitkopf 1989][research_breitkopf_1989]
- [Breitmaier 1988][research_breitmaier_1988]
- [Breitsamter and Laschka 2001][research_breitsamter_laschka_2001]
- [Brenckmann 1964][research_brenckmann_1964]
- [Breul 1963][research_breul_1963]
- [Breunig and Sayed 2018][research_breunig_sayed_2018]
- [Brictson et al 1969][research_brictson_ciavarelli_1969]
- [Briere 2007][research_briere_2007]
- [Briere and Warkander 2007][research_briere_warkander_2007]
- [Briggs 2002][research_briggs_2002]
- [Brinker 2004][research_brinker_2004]
- [Brockett et al 2002][research_brockett_laux_2002]
- [Brodersen and Sauer 1992][research_brodersen_sauer_1992]
- [Brodzinsky 1959][research_brodzinsky_1959]
- [Broglio 1961][research_broglio_1961]
- [Broglio 1962][research_broglio_1962]
- [Brooks 1989][research_brooks_1989]
- [Brooks and Mavris 2021][research_brooks_mavris_2021]
- [Brown 1950][research_brown_1950]
- [Brown 1989][research_brown_1989]
- [Brown 1998][research_brown_1998]
- [Brown 2009][research_brown_2009]
- [Brown and Hwang 1983][research_brown_hwang_1983]
- [Brown and Lu 2006][research_brown_lu_2006]
- [Brown And Root Development Inc Houston Tx 1983][research_brownandrootdevelopmentinchoustontx_1983]
- [Brown and Sun 2017][research_brown_sun_2017]
- [Brown and Timmerman 1991][research_brown_timmerman_1991]
- [Brown et al 2000][research_brown_silva_2000]
- [Brown et al 2014][research_brown_mchenry_2014]
- [Bruckner et al 2010][research_bruckner_vangraas_2010]
- [Bruening et al 2000][research_bruening_snyder_2000]
- [Bruening et al 2001][research_bruening_snyder_2001]
- [Brukarczyk et al 2021][research_brukarczyk_nowak_2021]
- [Brungardt 2011][research_brungardt_2011]
- [Brunson and Rais-Rohani 1996][research_brunson_raisrohani_1996]
- [Bruton et al 1999][research_bruton_glennie_1999]
- [Bryant et al 1998][research_bryant_tigges_1998]
- [Bryant et al 2015][research_bryant_gradwell_2015]
- [Bryce L Horvath and Gregory A Wrenn][research_brycelhorvath_gregoryawrenn]
- [Buchanan 2010][research_buchanan_2010]
- [Bucholtz et al 2008][research_bucholtz_nichols_2008]
- [Bucklew 2009][research_bucklew_2009]
- [Buckner 2000][research_buckner_2000]
- [Budd 2002][research_budd_2002]
- [Buell, Jr. 1970][research_buelljr_1970]
- [Buerger and Cannon 2016][research_buerger_cannon_2016]
- [Buffington 1997][research_buffington_1997]
- [Buffington 1999][research_buffington_1999]
- [Buffington 1999][research_buffington_1999_b]
- [Bulka and Nahon 2017][research_bulka_nahon_2017]
- [Bulka and Nahon 2019][research_bulka_nahon_2019]
- [Bunnell 2001][research_bunnell_2001]
- [Burcham 1998][research_burcham_1998]
- [Burke 2015][research_burke_2015]
- [Burken et al 2011][research_burken_frost_2011]
- [Burnashev and Zbrutsky 2019][research_burnashev_zbrutsky_2019]
- [Burns 2000][research_burns_2000]
- [Burnside 1974][research_burnside_1974]
- [Bushey][research_bushey]
- [Butler 1970][research_butler_1970]
- [Butler 1976][research_butler_1976]
- [Butler et al 1999][research_butler_lillico_1999]
- [Butt and Markmiller 2023][research_butt_markmiller_2023]
- [Bye 1993][research_bye_1993]
- [C-Scan¿A Milestone for Carrier 1969][research_c_scana_milestone_1969]
- [Cacopardi et al 1990][research_cacopardi_caporicci_1990]
- [Cai et al 2009][research_cai_grafarend_2009]
- [Cai et al 2018][research_cai_cui_2018]
- [Cai et al 2018][research_cai_zhou_2018]
- [Cai et al 2022][research_cai_rajaram_2022]
- [Caldwell 1963][research_caldwell_1963]
- [Calhoun and Raquet 2016][research_calhoun_raquet_2016]
- [Calhoun et al 2017][research_calhoun_draper_2017]
- [Callaghan and Kunz 2019][research_callaghan_kunz_2019]
- [Callens and Pugmire 1969][research_callens_pugmire_1969]
- [Callicoatt 2009][research_callicoatt_2009]
- [Calnoor Rajashekar et al 2020][research_calnoorrajashekar_tourani_2020]
- [Calvano and Harney 1998][research_calvano_harney_1998]
- [Camatti et al 1998][research_camatti_chiesa_1998]
- [Cameron et al 2022][research_cameron_fredin_2022]
- [Campbell 1959][research_campbell_1959]
- [Candan et al 2024][research_candan_sanci_2024]
- [Canpolat et al 2009][research_canpolat_yayla_2009]
- [Cao and Morse 2008][research_cao_morse_2008]
- [Cao et al 2026][research_cao_gao_2026]
- [Capderou 2012][research_capderou_2012]
- [Caporicci and Soddu][research_caporicci_soddu]
- [Cappuzzo et al 2022][research_cappuzzo_bianchi_2022]
- [Carico 1995][research_carico_1995]
- [Carney 2008][research_carney_2008]
- [Caron][research_caron]
- [Carpenter and Jenny 1964][research_carpenter_jenny_1964]
- [Carr et al 2003][research_carr_lambrecht_2003]
- [Carretta and Ree 1999][research_carretta_ree_1999]
- [Carreyette 1950][research_carreyette_1950]
- [Carrier et al 2022][research_carrier_arnoult_2022]
- [Carrier phase differential GPS/INS 1999][research_carrier_phase_1999]
- [Carrier Recovery Applications and 2012][research_carrier_recovery_2012]
- [Carrillo Córcoles et al 2023][research_carrillocorcoles_mertens_2023]
- [Carrio Fernández][research_carriofernandez]
- [Carroll][research_carroll]
- [Carter and Mueller 1991][research_carter_mueller_1991]
- [Casarosa et al 2004][research_casarosa_galatolo_2004]
- [Case 1965][research_case_1965]
- [Casey][research_casey]
- [Casey-Maslen 2018][research_caseymaslen_2018]
- [Casey-Maslen 2018][research_caseymaslen_2018_b]
- [Casey-Maslen 2018][research_caseymaslen_2018_c]
- [Cass and Ball 1988][research_cass_ball_1988]
- [Castagno et al 2018][research_castagno_ochoa_2018]
- [Castaldo et al 2014][research_castaldo_angrisano_2014]
- [Castanon and Cassandras 2010][research_castanon_cassandras_2010]
- [Castillo-Effen and Visnevski 2009][research_castilloeffen_visnevski_2009]
- [Castrichini et al 2016][research_castrichini_hodigeresiddaramaiah_2016]
- [Catalán et al 2025][research_catalan_iglesias_2025]
- [Catchpole 1990][research_catchpole_1990]
- [Categorization and classification of][research_categorization_and]
- [Catelani et al 2015][research_catelani_ciani_2015]
- [Caurin et al 2024][research_caurin_daudfilho_2024]
- [Causa and Fasano 2025][research_causa_fasano_2025]
- [Cavagna et al 2009][research_cavagna_ricci_2009]
- [Cavagna et al 2010][research_cavagna_ricci_2010]
- [Cavagna et al 2011][research_cavagna_ricci_2011]
- [Cazaurang et al 2003][research_cazaurang_bergeon_2003]
- [Cecrdle 2019][research_cecrdle_2019]
- [Celko et al 1995][research_celko_dubois_1995]
- [Cellmer et al 2010][research_cellmer_wielgosz_2010]
- [Cenko et al 1981][research_cenko_tinoco_1981]
- [Centracchio et al 2018][research_centracchio_rossetti_2018]
- [Ceren and Altuğ 2011][research_ceren_altug_2011]
- [Cestino 2006][research_cestino_2006]
- [Cetin and Yilmaz 2013][research_cetin_yilmaz_2013]
- [Cetin and Yilmaz 2014][research_cetin_yilmaz_2014]
- [Cetin and Zagli 2011][research_cetin_zagli_2011]
- [Cetin et al 2010][research_cetin_kurnaz_2010]
- [Chai and Mason 1996][research_chai_mason_1996]
- [Chai and Wilhite 2012][research_chai_wilhite_2012]
- [Chai et al 1995][research_chai_crisafulli_1995]
- [Chaikalis et al 2020][research_chaikalis_khorrami_2020]
- [Chakrabarty et al 2016][research_chakrabarty_morris_2016]
- [Chakraborty et al 2014][research_chakraborty_trawick_2014]
- [Chakravarty and Chichka 2006][research_chakravarty_chichka_2006]
- [Chalenski et al 2018][research_chalenski_hatchell_2018]
- [Chalk 1963][research_chalk_1963]
- [Chalk 1964][research_chalk_1964]
- [Chaloff et al 1974][research_chaloff_hiyama_1974]
- [Chana and Sullivan 1992][research_chana_sullivan_1992]
- [Chandler 1989][research_chandler_1989]
- [Chang 2006][research_chang_2006]
- [Chang 2013][research_chang_2013]
- [Chang and Ai 2026][research_chang_ai_2026]
- [Chang et al 2021][research_chang_wang_2021]
- [Chang et al 2022][research_chang_zhang_2022]
- [Chang et al 2022][research_chang_zheng_2022]
- [Changes in top management 2002][research_changes_in_2002]
- [Chansarkar 2000][research_chansarkar_2000]
- [Chansik Park and Ilsun Kim][research_chansikpark_ilsunkim]
- [Chansik Park and Ilsun Kim 2000][research_chansikpark_ilsunkim_2000]
- [Chao et al 2017][research_chao_brink_2017]
- [Chapa 2013][research_chapa_2013]
- [Chapteer 8. GPS Modernization 2008][research_chapteer_8_2008]
- [Chapter 1. "Under the 2017][research_chapter_1_2017]
- [Chapter 3 Autonomous UAVs 2021][research_chapter_3_2021]
- [Chapter 3. Dynamics of 2005][research_chapter_3_2005]
- [Chapter 3U.S. Aviation Regulatory 2016][research_chapter_3u_s_2016]
- [Chaput 1987][research_chaput_1987]
- [Characteristics of Aircraft Types 2010][research_characteristics_of_2010]
- [Chattot 2005][research_chattot_2005]
- [Chattot 2006][research_chattot_2006]
- [Chaudhry et al 2016][research_chaudhry_smith_2016]
- [Chaussee and Dervault 2013][research_chaussee_dervault_2013]
- [Che Man et al 2020][research_cheman_liu_2020]
- [Cheatham and Hackler 1966][research_cheatham_hackler_1966]
- [Chelnokov and Perelyaev 2022][research_chelnokov_perelyaev_2022]
- [Chen][research_chen]
- [Chen 1964][research_chen_1964]
- [Chen 1995][research_chen_1995]
- [Chen 2025][research_chen_2025]
- [Chen and Duan 2016][research_chen_duan_2016]
- [Chen and Ho 2017][research_chen_ho_2017]
- [Chen and Hubner 2021][research_chen_hubner_2021]
- [Chen and Qin 2013][research_chen_qin_2013]
- [Chen and Zhao 2024][research_chen_zhao_2024]
- [Chen et al 2011][research_chen_zheng_2011]
- [Chen et al 2011][research_chen_zheng_2011_b]
- [Chen et al 2014][research_chen_zhao_2014]
- [Chen et al 2015][research_chen_han_2015]
- [Chen et al 2016][research_chen_zhao_2016]
- [Chen et al 2020][research_chen_zhou_2020]
- [Chen et al 2020][research_chen_zhou_2020_b]
- [Chen et al 2020][research_chen_zhou_2020_c]
- [Chen et al 2020][research_chen_zhou_2020_d]
- [Chen et al 2020][research_chen_zhou_2020_e]
- [Chen et al 2021][research_chen_fang_2021]
- [Chen et al 2021][research_chen_li_2021]
- [Chen et al 2021][research_chen_zhou_2021]
- [Chen et al 2023][research_chen_han_2023]
- [Chen et al 2023][research_chen_han_2023_b]
- [Chen et al 2023][research_chen_li_2023]
- [Chen et al 2024][research_chen_wei_2024]
- [Chen et al 2024][research_chen_xu_2024]
- [Chen et al 2024][research_chen_yang_2024]
- [Chen et al 2025][research_chen_fang_2025]
- [Chen et al 2026][research_chen_wang_2026]
- [Chen et al 2026][research_chen_zhai_2026]
- [Chen et al 2026][research_chen_zhang_2026]
- [Cheng et al 2021][research_cheng_cao_2021]
- [Chernenko and Burnashev 2022][research_chernenko_burnashev_2022]
- [Chesser et al 1999][research_chesser_draper_1999]
- [Chessman 2022][research_chessman_2022]
- [Chester 1995][research_chester_1995]
- [Chester 2002][research_chester_2002]
- [Chester 2002][research_chester_2002_b]
- [Cheung et al 2020][research_cheung_rezgui_2020]
- [Chevalier and Burke 1972][research_chevalier_burke_1972]
- [Chiang and Youssef 1995][research_chiang_youssef_1995]
- [Chiba et al 2006][research_chiba_obayashi_2006]
- [Chiba et al 2009][research_chiba_makino_2009]
- [Chiesa et al 1999][research_chiesa_disciuva_1999]
- [Chihabi and Ulrich 2024][research_chihabi_ulrich_2024]
- [Chihabi and Ulrich 2024][research_chihabi_ulrich_2024_b]
- [Childers and Condon 2004][research_childers_condon_2004]
- [Childers and Gelderloos][research_childers_gelderloos]
- [Chin 1985][research_chin_1985]
- [China Satellite Navigation Conference 2013][research_china_satellite_2013]
- [Chinag and Youssef 1994][research_chinag_youssef_1994]
- [Chisman 1991][research_chisman_1991]
- [Chitrakaran et al 2005][research_chitrakaran_dawson_2005]
- [Chiu Hung Luk et al][research_chiuhungluk_gao]
- [Cho and Lee 2025][research_cho_lee_2025]
- [Cho et al 2019][research_cho_kang_2019]
- [Choi 2016][research_choi_2016]
- [Choi et al 2010][research_choi_nguyen_2010]
- [Chorley 1981][research_chorley_1981]
- [Chudoba and Cook 2003][research_chudoba_cook_2003]
- [Chun et al 2005][research_chun_kwon_2005]
- [Cifaldi 2017][research_cifaldi_2017]
- [Cihak and Anton W. 2005][research_cihak_antonw_2005]
- [Citurs and Caton 1985][research_citurs_caton_1985]
- [Civil Nuclear Systems Corp Albuquerque Nm 1977][research_civilnuclearsystemscorpalbuquerquenm_1977]
- [Civil Regulation Of Autonomous 2024][research_civil_regulation_2024]
- [Civil small and light][research_civil_small]
- [Civil small and light][research_civil_small_b]
- [Clare et al 2012][research_clare_macbeth_2012]
- [Clare et al 2012][research_clare_ryan_2012]
- [Clark][research_clark]
- [Clark 1964][research_clark_1964]
- [Clark 1965][research_clark_1965]
- [Clark 1975][research_clark_1975]
- [Clark 2006][research_clark_2006]
- [Clark 2013][research_clark_2013]
- [Clarkson 1991][research_clarkson_1991]
- [Classification for Unmanned Aircraft][research_classification_for]
- [Cleveland 1970][research_cleveland_1970]
- [Clothier and Walker 2014][research_clothier_walker_2014]
- [Clough 2003][research_clough_2003]
- [Cobb et al][research_cobb_cohen]
- [Cochrane and Whitman 1987][research_cochrane_whitman_1987]
- [Cockburn 1965][research_cockburn_1965]
- [Cockpit Visibility for Commercial][research_cockpit_visibility]
- [Cohen et al 1994][research_cohen_pervan_1994]
- [Coiro and Nicolosi 2001][research_coiro_nicolosi_2001]
- [Cole 1989][research_cole_1989]
- [Coleman and Hamilton 2026][research_coleman_hamilton_2026]
- [Collins et al 2025][research_collins_kochersberger_2025]
- [Collyer et al 1980][research_collyer_ricard_1980]
- [Colozza, Anthony and Dolce, James 2003][research_colozzaanthony_dolcejames_2003]
- [Colwell 1966][research_colwell_1966]
- [Comandur et al 2019][research_comandur_walters_2019]
- [Commercial Aircraft Hydraulic System][research_commercial_aircraft]
- [Computer vision-based approach for 2025][research_computer_vision_based_2025]
- [Conceptual Design Examples 2024][research_conceptual_design_2024]
- [Conducting Unmanned Aircraft Flight 2015][research_conducting_unmanned_2015]
- [Configuring Aircraft 2010][research_configuring_aircraft_2010]
- [Connelly 1982][research_connelly_1982]
- [Connelly 1983][research_connelly_1983]
- [Conners 1995][research_conners_1995]
- [Connolly 1981][research_connolly_1981]
- [Connolly et al 2023][research_connolly_ogorman_2023]
- [Constantin et al 2023][research_constantin_decourcy_2023]
- [Construction vehicles with an 2025][research_construction_vehicles_2025]
- [Control authority assessment in 1993][research_control_authority_1993]
- [Control of cooperative unmanned][research_control_of_cooperative]
- [Control Surface Sizing Criteria 2010][research_control_surface_2010]
- [Cook 1964][research_cook_1964]
- [Cook 1997][research_cook_1997]
- [Cook 2007][research_cook_2007]
- [Cook 2013][research_cook_2013]
- [Cook 2024][research_cook_2024]
- [Cook and Hauser 2018][research_cook_hauser_2018]
- [Cook et al 2005][research_cook_kokolios_2005]
- [Cooke 2010][research_cooke_2010]
- [Cooke and Speck 1971][research_cooke_speck_1971]
- [Cookerly 1988][research_cookerly_1988]
- [Cooper 2023][research_cooper_2023]
- [Cooper and Ravela 2024][research_cooper_ravela_2024]
- [Cooper and Stroud 1972][research_cooper_stroud_1972]
- [Coopmans et al 2013][research_coopmans_jensen_2013]
- [Coordinating Research Council Inc Atlanta Ga 1988][research_coordinatingresearchcouncilincatlantaga_1988]
- [Coppock and Gerke 1977][research_coppock_gerke_1977]
- [Corazzini et al 1998][research_corazzini_robertson_1998]
- [Corley et al 2008][research_corley_kehler_2008]
- [Corn et al 2005][research_corn_mclaurine_2005]
- [Corridor-Wide Surveillance Using Unmanned 2021][research_corridor_wide_surveillance_2021]
- [Corridor-Wide Surveillance Using Unmanned 2023][research_corridor_wide_surveillance_2023]
- [Corridor-Wide Surveillance Using Unmanned 2023][research_corridor_wide_surveillance_2023_b]
- [Corridor-Wide Surveillance Using Unmanned 2024][research_corridor_wide_surveillance_2024]
- [Corridor-Wide Surveillance Using Unmanned 2025][research_corridor_wide_surveillance_2025]
- [Cossaboom et al 2012][research_cossaboom_georgy_2012]
- [Cote 2015][research_cote_2015]
- [Cour-Harbo 2018][research_courharbo_2018]
- [Cour-Harbo 2020][research_courharbo_2020]
- [Courtaulds Aerospace launch quick 1998][research_courtaulds_aerospace_1998]
- [Courtois and Aouf 2017][research_courtois_aouf_2017]
- [Coutard and Chaumette 2011][research_coutard_chaumette_2011_b]
- [Coutard et al 2011][research_coutard_chaumette_2011]
- [Cove and Santos 2004][research_cove_santos_2004]
- [Cox 1978][research_cox_1978]
- [Cox 1989][research_cox_1989]
- [Cox 2009][research_cox_2009]
- [Cox and Roy 1988][research_cox_roy_1988]
- [Coyle 1992][research_coyle_1992]
- [Coyle and Herr 2026][research_coyle_herr_2026]
- [Crafton 1965][research_crafton_1965]
- [Craig et al 1991][research_craig_zwernemann_1991]
- [Crain et al 2016][research_crain_bishop_2016]
- [Crandall 1999][research_crandall_1999]
- [Cranfield helps launch the 2008][research_cranfield_helps_2008]
- [Crashworthy landing gear for 1998][research_crashworthy_landing_1998]
- [Crassidis and Mook 1991][research_crassidis_mook_1991]
- [Crassidis and Mook 1992][research_crassidis_mook_1992]
- [Crassidis et al 1993][research_crassidis_mook_1993]
- [Crespo et al 2010][research_crespo_matsutani_2010]
- [Crew Safety Provision for][research_crew_safety_b]
- [Crew Safety Provisions for][research_crew_safety]
- [Crimi and Johnson 1973][research_crimi_johnson_1973]
- [Cristofaro et al 2015][research_cristofaro_johansen_2015]
- [Cronk 2007][research_cronk_2007]
- [Crossley 2004][research_crossley_2004]
- [Crossley et al 2011][research_crossley_skillen_2011]
- [Cruz and Encarnação 2011][research_cruz_encarnacao_2011]
- [Cruz and Fierro 2015][research_cruz_fierro_2015]
- [Cuevas and Aguiar 2017][research_cuevas_aguiar_2017]
- [Cui et al 2020][research_cui_han_2020]
- [Cui et al 2022][research_cui_zhou_2022]
- [Cummings and Schütte 2012][research_cummings_schutte_2012]
- [Cummings et al 2003][research_cummings_morton_2003]
- [Cummings et al 2008][research_cummings_morton_2008]
- [Cummings et al 2013][research_cummings_mastracchio_2013]
- [Cummings et al 2018][research_cummings_liersch_2018]
- [Cummins 1999][research_cummins_1999]
- [Cunningham][research_cunningham]
- [Cunningham 1976][research_cunningham_1976]
- [Cunningham and den Boer 1990][research_cunningham_denboer_1990]
- [Curlett 2002][research_curlett_2002]
- [Current Manned Aviation Regulation][research_current_manned]
- [Currey 1988][research_currey_1988]
- [Cutler et al 2010][research_cutler_mclain_2010]
- [Cygańczuk and Roguski 2023][research_cyganczuk_roguski_2023]
- [D'Amico et al 2008][research_damico_montenbruck_2008]
- [D'Andrea 2008][research_dandrea_2008]
- [Dahleh and Tsitsiklis 2002][research_dahleh_tsitsiklis_2002]
- [Dahmane et al 2022][research_dahmane_lejdel_2022]
- [Dai and Cochran 2009][research_dai_cochran_2009]
- [Dai et al 2016][research_dai_wei_2016]
- [Dai et al 2018][research_dai_quan_2018]
- [Dai et al 2020][research_dai_wei_2020]
- [Dakka and Johnson 2019][research_dakka_johnson_2019]
- [Dal'Carobo and Fensterseifer 2010][research_dalcarobo_fensterseifer_2010]
- [Dalamagkidis 2014][research_dalamagkidis_2014]
- [Dalamagkidis 2014][research_dalamagkidis_2014_b]
- [Dalamagkidis et al 2012][research_dalamagkidis_valavanis_2012]
- [Daly 1994][research_daly_1994]
- [Dang et al 2022][research_dang_chen_2022]
- [Danko and Oh 2013][research_danko_oh_2013]
- [Dannenhoffer 1981][research_dannenhoffer_1981]
- [Dantsker et al 2018][research_dantsker_theile_2018]
- [Dantsker et al 2019][research_dantsker_yu_2019]
- [Daquan Tang et al 2016][research_daquantang_yongkangjiao_2016]
- [Darrah and Conrad 1971][research_darrah_conrad_1971]
- [Darvish et al 2015][research_darvish_pourtakdoust_2015]
- [Daud Filho][research_daudfilho]
- [Daughetee 1974][research_daughetee_1974]
- [David 2025][research_david_2025]
- [Davidson 2004][research_davidson_2004]
- [Davidson and Little 1977][research_davidson_little_1977]
- [Davis 2010][research_davis_2010]
- [Dawson 2015][research_dawson_2015]
- [de Carvalho Bertoli et al 2016][research_decarvalhobertoli_adabo_2016]
- [de Cunto][research_decunto]
- [De Lellis et al 2013][research_delellis_divito_2013]
- [de Paula et al 2025][research_depaula_dwivedi_2025]
- [de Poix 1964][research_depoix_1964]
- [DeBilzan 1975][research_debilzan_1975]
- [DeCAMP and Hardy 1981][research_decamp_hardy_1981]
- [Decoust and Udrea 2008][research_decoust_udrea_2008]
- [Defense Science Board Washington Dc 2002][research_defensescienceboardwashingtondc_2002]
- [Dehghani and Menhaj 2016][research_dehghani_menhaj_2016]
- [Deja et al 2022][research_deja_dayyani_2022]
- [DeJarnette-Crumsey et al 2022][research_dejarnettecrumsey_savage_2022]
- [Del Vecchio and Costa 1999][research_delvecchio_costa_1999]
- [DeLancey et al 2011][research_delancey_harris_2011]
- [DeLaurier 2022][research_delaurier_2022]
- [Delgado Regis et al 2004][research_delgadoregis_mattos_2004]
- [Delporte et al 2007][research_delporte_mercier_2007]
- [Delporte et al 2008][research_delporte_mercier_2008]
- [Demarchi and Haning 1978][research_demarchi_haning_1978]
- [Demir et al 2021][research_demir_gorguluarslan_2021]
- [Demircali and Uvet 2018][research_demircali_uvet_2018]
- [Denegri et al 2021][research_denegri_sharma_2021]
- [Deng and Duan 2016][research_deng_duan_2016]
- [Denham and Paines 2008][research_denham_paines_2008]
- [Denny 2003][research_denny_2003]
- [Department Of Defense Washington Dc 1994][research_departmentofdefensewashingtondc_1994]
- [Department Of Defense Washington Dc 2009][research_departmentofdefensewashingtondc_2009]
- [Department Of The Air Force Washington Dc 1986][research_departmentoftheairforcewashingtondc_1986]
- [Department Of The Air Force Washington Dc 1997][research_departmentoftheairforcewashingtondc_1997]
- [Department Of The Air Force Washington Dc 2004][research_departmentoftheairforcewashingtondc_2004]
- [Department Of The Air Force Washington Dc 2005][research_departmentoftheairforcewashingtondc_2005]
- [Deprez and Warnant 2018][research_deprez_warnant_2018]
- [Deresh 1982][research_deresh_1982]
- [Design and Development of 1989][research_design_and_1989]
- [Design and Development of 2014][research_design_and_2014]
- [Design and Fluid Flow 2015][research_design_and_2015]
- [Design and Implementation of 2014][research_design_and_2014_b]
- [Design constraints in the 1993][research_design_constraints_1993]
- [Design Objectives for Flying][research_design_objectives_b]
- [Design Objectives For Handling][research_design_objectives]
- [Design of Locking Mechanism 2024][research_design_of_2024_b]
- [Design of the circulation 1979][research_design_of_1979]
- [Design of the Well-Tempered 2013][research_design_of_2013]
- [Design of Unique Aircraft 2024][research_design_of_2024]
- [Design, control, and autonomous][research_design_control_and]
- [Desjardins and Laananen 1980][research_desjardins_laananen_1980]
- [Deslich et al 2021][research_deslich_flick_2021]
- [Development of algorithmic support 2022][research_development_of_2022]
- [Deverill 2000][research_deverill_2000]
- [Dewa et al 2024][research_dewa_atami_2024]
- [Dewispelare and Stager 1981][research_dewispelare_stager_1981]
- [DeWispelare and Stager 1983][research_dewispelare_stager_1983]
- [Deyoung 1971][research_deyoung_1971]
- [Di et al 2022][research_di_mishra_2022]
- [Di Li and Jinling Wang][research_dili_jinlingwang]
- [Diana 2015][research_diana_2015]
- [Dickes et al 2002][research_dickes_gingras_2002]
- [Dickey and Marek 1963][research_dickey_marek_1963]
- [Dickinson and Goggin 2000][research_dickinson_goggin_2000]
- [Didomenico and Biezad 1985][research_didomenico_biezad_1985]
- [Dieffenbach 1995][research_dieffenbach_1995]
- [Diesel 1987][research_diesel_1987]
- [Dietrich 2020][research_dietrich_2020]
- [Differential carrier phase GPS-aided 1999][research_differential_carrier_1999]
- [Diget et al 2022][research_diget_hasan_2022]
- [Digges 1971][research_digges_1971]
- [Digman 2009][research_digman_2009]
- [Dill and Uijt de Haag 2016][research_dill_uijtdehaag_2016]
- [Dill et al 2017][research_dill_young_2017]
- [Ding 2015][research_ding_2015]
- [Ding and Tomlin 2009][research_ding_tomlin_2009]
- [Ding et al 2007][research_ding_wang_2007]
- [Ding et al 2010][research_ding_wang_2010]
- [Ding et al 2015][research_ding_li_2015]
- [Dixon et al 2005][research_dixon_wickens_2005]
- [Di̇nç 2021][research_dinc_2021]
- [DLR and MTU Aero 2020][research_dlr_and_2020]
- [Doan][research_doan]
- [Doane 2003][research_doane_2003]
- [Doblhoff 1956][research_doblhoff_1956]
- [DoD Office of Inspector General 2015][research_dodofficeofinspectorgeneral_2015]
- [Dodge 2015][research_dodge_2015]
- [Doer et al 2020][research_doer_koenig_2020]
- [Doggett and Soistmann 1992][research_doggett_soistmann_1992]
- [Doguet and Rancourt 2023][research_doguet_rancourt_2023]
- [Doherty and Butzel 1979][research_doherty_butzel_1979]
- [Doherty and Butzel 1979][research_doherty_butzel_1979_b]
- [Doherty et al 2013][research_doherty_heintz_2013]
- [Doherty et al 2023][research_doherty_costello_2023]
- [Dong et al 2017][research_dong_huang_2017]
- [Dong et al 2020][research_dong_wang_2020]
- [Dong et al 2020][research_dong_zhang_2020]
- [Dong et al 2021][research_dong_shao_2021]
- [Dong Kangsheng et al 2016][research_dongkangsheng_huangchangqiang_2016]
- [Donley 1980][research_donley_1980]
- [Donmez and Cummings 2010][research_donmez_cummings_2010]
- [Donmez et al 2008][research_donmez_brzezinski_2008]
- [Donmez et al 2009][research_donmez_cummings_2009]
- [Dorobantu et al 2013][research_dorobantu_murch_2013]
- [Dou and Duan 2017][research_dou_duan_2017]
- [Douglas Aircraft Co Long Beach Ca 1963][research_douglasaircraftcolongbeachca_1963]
- [Douglas Aircraft Co Long Beach Ca 1983][research_douglasaircraftcolongbeachca_1983]
- [Douma et al 2021][research_douma_wang_2021]
- [Dowling and Costello 2017][research_dowling_costello_2017]
- [Downs 2009][research_downs_2009]
- [Draper 2008][research_draper_2008]
- [Draper et al 1983][research_draper_buck_1983]
- [Dress et al 1992][research_dress_boyden_1992]
- [Dresser et al 1990][research_dresser_newberry_1990]
- [Drewiacki et al 2025][research_drewiacki_moreira_2025]
- [Drinkwater, Iii and Rolls 1965][research_drinkwateriii_rolls_1965]
- [Drummond 1971][research_drummond_1971]
- [Drusinsky et al 2022][research_drusinsky_michael_2022]
- [Du and Yang 2004][research_du_yang_2004]
- [Du et al 2019][research_du_li_2019]
- [Duan 2013][research_duan_2013]
- [Duan et al 2015][research_duan_zhao_2015]
- [Duan et al 2016][research_duan_zhao_2016]
- [Duan et al 2021][research_duan_sun_2021]
- [Duan et al 2022][research_duan_chen_2022]
- [Duan et al 2022][research_duan_yuan_2022]
- [Dubicki and Gorospe 2026][research_dubicki_gorospe_2026]
- [Dudek and Schulte 2022][research_dudek_schulte_2022]
- [Duggan and Bhandari 2021][research_duggan_bhandari_2021]
- [Duhamel 1989][research_duhamel_1989]
- [Dukes 1970][research_dukes_1970]
- [Duncan et al 2006][research_duncan_ferrier_2006]
- [Duong Nguyen et al 2022][research_duongnguyen_kashitani_2022]
- [Duraklar 2024][research_duraklar_2024]
- [Durand and Teper 1964][research_durand_teper_1964]
- [Durand and Wasicko 1965][research_durand_wasicko_1965]
- [Durand and Wasicko 1967][research_durand_wasicko_1967]
- [Durmuş and Duymaz 2023][research_durmus_duymaz_2023]
- [Durmuşoğlu 2026][research_durmusoglu_2026]
- [Dwi Setiawan and Aldino 2026][research_dwisetiawan_aldino_2026]
- [Dynamics of Aircraft Motion 2015][research_dynamics_of_2015]
- [Dynamics of Flexible Aircraft 2023][research_dynamics_of_2023_c]
- [Dynamics of Flexible Aircraft 2023][research_dynamics_of_2023_d]
- [Dynamics of Rigid Aircraft 2023][research_dynamics_of_2023_b]
- [Dynamics of Very Flexible 2023][research_dynamics_of_2023]
- [Dynnikov 2020][research_dynnikov_2020]
- [Délery and Meauzé 2003][research_delery_meauze_2003]
- [EADS and A* STAR 2007][research_eads_and_2007]
- [Early Conceptual Design 2013][research_early_conceptual_2013]
- [Eaton and Chen 2015][research_eaton_chen_2015]
- [Ebne-Abbasi et al 2024][research_ebneabbasi_makarov_2024]
- [Ebrahimi Fakhari et al 2024][research_ebrahimifakhari_moshtaghzadeh_2024]
- [Eckels 1983][research_eckels_1983]
- [ECO Demonstrator Begins Flight 2018][research_eco_demonstrator_2018]
- [Edelbaum 1963][research_edelbaum_1963]
- [Edge et al 2010][research_edge_collins_2010]
- [Edge et al 2011][research_edge_brown_2011]
- [Edwan et al 2012][research_edwan_zhou_2012]
- [Edwards and Lennie O. 1990][research_edwards_lennieo_1990]
- [Effect of High Mach 2010][research_effect_of_2010]
- [Effective GPS Positioning Algorithm 2012][research_effective_gps_positioning_2012]
- [Effing et al 2023][research_effing_schueltke_2023]
- [Eichorn 1989][research_eichorn_1989]
- [Eigenmann et al 1984][research_eigenmann_kitzmiller_1984]
- [Eisenreich 2009][research_eisenreich_2009]
- [Eisler][research_eisler]
- [Ekici et al 2023][research_ekici_dalkiran_2023]
- [El Tin et al 2022][research_eltin_sharf_2022]
- [El-Diasty and Pagiatakis 2010][research_eldiasty_pagiatakis_2010]
- [El-Ferik 2020][research_elferik_2020]
- [El-Mowafy 2005][research_elmowafy_2005]
- [El-Mowafy 2008][research_elmowafy_2008]
- [El-Mowafy and Imparato 2018][research_elmowafy_imparato_2018]
- [El-Sayed and ElHelw 2012][research_elsayed_elhelw_2012]
- [Elchynski et al][research_elchynski_kirkland]
- [Electric Aircraft 2024][research_electric_aircraft_2024]
- [Electricity in the aircraft 1954][research_electricity_in_1954]
- [Elena 2026][research_elena_2026]
- [Elham and Bahamonde Jacome 2016][research_elham_bahamondejacome_2016]
- [Elias 1985][research_elias_1985]
- [Elisov et al 2018][research_elisov_ishkov_2018]
- [Elkhoury 2008][research_elkhoury_2008]
- [Elkhoury 2016][research_elkhoury_2016]
- [Elkhoury and Nakad 2009][research_elkhoury_nakad_2009]
- [Elkhoury and Rockwell 2004][research_elkhoury_rockwell_2004]
- [Elkhoury et al 2005][research_elkhoury_yavuz_2005]
- [Eller and Cavanagh 2000][research_eller_cavanagh_2000]
- [Ellingson et al 2018][research_ellingson_brink_2018]
- [Ellingson et al 2020][research_ellingson_brink_2020]
- [Elliott 2009][research_elliott_2009]
- [Elliott and Dogan 2009][research_elliott_dogan_2009]
- [Ellis 1976][research_ellis_1976]
- [Enbo Shi 2012][research_enboshi_2012]
- [Ender and McClure 2002][research_ender_mcclure_2002]
- [Energy Approach To Performance 2003][research_energy_approach_2003]
- [Engdahl 2004][research_engdahl_2004]
- [Enge 1999][research_enge_1999]
- [Engineering institutions launch aerospace 1998][research_engineering_institutions_1998]
- [Englebry 1980][research_englebry_1980]
- [Englebry 1981][research_englebry_1981]
- [Englezou et al 2022][research_englezou_timotheou_2022]
- [Enkhtur 2013][research_enkhtur_2013]
- [Environmental Control Systems ECS][research_environmental_control]
- [Epp 2024][research_epp_2024]
- [Epperson 2010][research_epperson_2010]
- [Eppley 2012][research_eppley_2012]
- [Er-El 1988][research_erel_1988]
- [Erdman and Mitchum 2013][research_erdman_mitchum_2013]
- [Ericsson 1997][research_ericsson_1997]
- [Ericsson 1998][research_ericsson_1998]
- [Erkeç and Hajiyev 2020][research_erkec_hajiyev_2020]
- [Ernest and Carroll 2016][research_ernest_carroll_2016]
- [Ernest and Cohen 2016][research_ernest_cohen_2016]
- [Ertler][research_ertler]
- [Esdras and Liscouet-Hanke 2013][research_esdras_liscouethanke_2013]
- [Essari 2018][research_essari_2018]
- [Essari 2018][research_essari_2018_b]
- [Essari and Ghatus 2023][research_essari_ghatus_2023]
- [Estimating the Takeoff Wing 2010][research_estimating_the_2010]
- [Eubank and Atkins 2011][research_eubank_atkins_2011]
- [Evaluation of the navigation 1979][research_evaluation_of_1979]
- [Evangelou 1998][research_evangelou_1998]
- [Experimental investigation of synthetic 2023][research_experimental_investigation_2023]
- [Fahimi 2005][research_fahimi_2005]
- [Fahimi and Thakur 2013][research_fahimi_thakur_2013]
- [Faiz and Agarwal 1998][research_faiz_agarwal_1998]
- [Falcone et al 1974][research_falcone_clark_1974]
- [Falkenberg et al][research_falkenberg_hartt]
- [Fan et al 2021][research_fan_jiang_2021]
- [Fang et al 2018][research_fang_kim_2018]
- [Fant 2001][research_fant_2001]
- [Farajollahi and Markazi 2010][research_farajollahi_markazi_2010]
- [Farid and Mouhoub 2023][research_farid_mouhoub_2023]
- [Farmani et al 2015][research_farmani_sun_2015]
- [Farokhi 1998][research_farokhi_1998]
- [Farrell et al 2001][research_farrell_vangraas_2001]
- [Fegely et al 2017][research_fegely_xin_2017]
- [Fei-Bin Hsiao et al 2003][research_feibinhsiao_shihhsienhuang_2003]
- [Felter and Wu 1997][research_felter_wu_1997]
- [Felux et al 2013][research_felux_dautermann_2013]
- [Feng 2001][research_feng_2001]
- [Feng and Jokinen 2015][research_feng_jokinen_2015]
- [Feng et al 2011][research_feng_ochieng_2011]
- [Feng et al 2018][research_feng_li_2018]
- [Fenwick 1966][research_fenwick_1966]
- [Ferrando et al 1999][research_ferrando_perez_1999]
- [Ferrier and Duncan 2012][research_ferrier_duncan_2012]
- [Ferrier et al 2000][research_ferrier_baitis_2000]
- [Ferrier et al 2006][research_ferrier_duncan_2006]
- [Ferrier et al 2015][research_ferrier_ernst_2015]
- [Ferrier et al 2024][research_ferrier_christmas_2024]
- [Ferrier et al 2025][research_ferrier_watson_2025]
- [Fezans and Jann 2017][research_fezans_jann_2017]
- [Fibre ropes for offshore][research_fibre_ropes]
- [Fidan and Mostafa 2024][research_fidan_mostafa_2024]
- [Field and Rossitto 1999][research_field_rossitto_1999]
- [Fielding and Vaziry-Z 1995][research_fielding_vaziryz_1995]
- [Fierro et al][research_fierro_branca]
- [Figge 1973][research_figge_1973]
- [Figge and Bernhardt 1975][research_figge_bernhardt_1975]
- [Figliola 2004][research_figliola_2004]
- [Figliola 2005][research_figliola_2005]
- [Fikes 1996][research_fikes_1996]
- [Firing][research_firing]
- [Firuzabadì and King 2011][research_firuzabadi_king_2011]
- [Fisch et al 2012][research_fisch_lenz_2012]
- [Fischer 2006][research_fischer_2006]
- [Fisher 1950][research_fisher_1950]
- [Fisher et al 2010][research_fisher_vanzwieten_2010]
- [Fladeland, Matt et al 2019][research_fladelandmatt_schoenungsusan_2019]
- [Flansburg 2015][research_flansburg_2015]
- [Flansburg 2016][research_flansburg_2016]
- [Fleming et al 2004][research_fleming_ng_2004]
- [Flexible wing coating reduces 2007][research_flexible_wing_2007]
- [Flight Control Compartment Nomenclature][research_flight_control]
- [Flight Deck Controls and][research_flight_deck_g]
- [Flight Deck Escape Provisions][research_flight_deck]
- [Flight Deck Instrumentation, Display][research_flight_deck_c]
- [Flight Deck Interior Doors][research_flight_deck_b]
- [Flight Deck Lighting for][research_flight_deck_e]
- [Flight Deck Lighting for][research_flight_deck_f]
- [Flight DECK Seats for][research_flight_deck_d]
- [Flight Dynamics of Elastic 2014][research_flight_dynamics_2014]
- [Flight Envelope Awareness/Protection][research_flight_envelope]
- [Flight Test Programme 1970][research_flight_test_1970]
- [Flow Control and High-Lift 2016][research_flow_control_2016]
- [Floyd 2000][research_floyd_2000]
- [Foch 1992][research_foch_1992]
- [Foch and Toot 1989][research_foch_toot_1989]
- [Fofonov 2021][research_fofonov_2021]
- [Fong 1982][research_fong_1982]
- [Fong and Self][research_fong_self]
- [Fontaine][research_fontaine]
- [Foreign Technology Div Wright-Pattersonafb Oh 1973][research_foreigntechnologydivwrightpattersonafboh_1973]
- [Forrester][research_forrester]
- [Forsmo et al 2013][research_forsmo_grotli_2013]
- [Fortenbaugh 1972][research_fortenbaugh_1972]
- [Foss 2026][research_foss_2026]
- [Foss, W. E., Jr. 1981][research_fosswejr_1981]
- [Foss, W. E.., Jr. 1984][research_fosswejr_1984]
- [Fracture of an Aluminum 2019][research_fracture_of_2019]
- [Fradenburgh 1991][research_fradenburgh_1991]
- [Franco et al 2019][research_franco_correia_2019]
- [Frau 2022][research_frau_2022]
- [Frederick et al 2001][research_frederick_jr_2001]
- [Frederick et al 2001][research_frederick_jr_2001_b]
- [Frederick et al 2001][research_frederick_jr_2001_c]
- [Frederick et al 2001][research_frederick_roberta_2001]
- [Frederick et al 2002][research_frederick_jr_2002]
- [Freeway Incident Detection and 2024][research_freeway_incident_2024]
- [Frew and Brown][research_frew_brown]
- [Frew and Lawrence 2005][research_frew_lawrence_2005]
- [Frey 2011][research_frey_2011]
- [Friedrich and Vollrath 2022][research_friedrich_vollrath_2022]
- [Frontera Sánchez][research_fronterasanchez]
- [Frost 1968][research_frost_1968]
- [Frost 1995][research_frost_1995]
- [Frost et al 2002][research_frost_franklin_2002]
- [Frost et al 2021][research_frost_walters_2021]
- [Frounfelker and Belencan 1984][research_frounfelker_belencan_1984]
- [Frulla 2021][research_frulla_2021]
- [Fry 2008][research_fry_2008]
- [Frye 1984][research_frye_1984]
- [Fu 1972][research_fu_1972]
- [Fu et al 2014][research_fu_carrio_2014]
- [Fu et al 2015][research_fu_zhang_2015]
- [Fu et al 2023][research_fu_sun_2023]
- [Fu Li et al 2008][research_fuli_yumeixiang_2008]
- [Fuchs et al 2013][research_fuchs_ferreira_2013]
- [Fuchser 1984][research_fuchser_1984]
- [Fuel cell demonstrator aeroplane 2007][research_fuel_cell_2007]
- [Fuhrmann et al][research_fuhrmann_koch]
- [Fukuda and Takimoto 2014][research_fukuda_takimoto_2014]
- [Fukushima and Tsubone 2019][research_fukushima_tsubone_2019]
- [Furnish and Anders 1971][research_furnish_anders_1971]
- [Further development and flight 1994][research_further_development_1994]
- [Fuselages and Tails Empennage 2017][research_fuselages_and_2017]
- [Fusion of Multi-Antenna Carrier 2012][research_fusion_of_2012]
- [Félix et al 2019][research_felix_gomes_2019]
- [G et al 2016][research_g_mnvss_2016]
- [G et al 2024][research_g_gowda_2024]
- [Gabriele 1991][research_gabriele_1991]
- [Gacy 2011][research_gacy_2011]
- [Gage 1994][research_gage_1994]
- [Gaitanakis et al 2020][research_gaitanakis_limnaios_2020]
- [Galdos et al][research_galdos_upadhyay]
- [Gall and Caverly 2025][research_gall_caverly_2025]
- [Galloway 1989][research_galloway_1989]
- [Galloway and Dey 2015][research_galloway_dey_2015]
- [Galway 2008][research_galway_2008]
- [Galway 2008][research_galway_2008_b]
- [Gan et al 2021][research_gan_fang_2021]
- [Gandolfi et al 2016][research_gandolfi_tavasci_2016]
- [Gannan Yuan and Tao Zhang 2009][research_gannanyuan_taozhang_2009]
- [Gao et al 2016][research_gao_kang_2016]
- [Gao et al 2019][research_gao_li_2019]
- [Gao et al 2021][research_gao_an_2021]
- [Gao et al 2021][research_gao_hu_2021]
- [Gao et al 2024][research_gao_luo_2024]
- [Garcia et al 2017][research_garcia_keshmiri_2017]
- [Garcia et al 2020][research_garcia_caballero_2020]
- [Gardi et al 2015][research_gardi_ramasamy_2015]
- [Gardi et al 2016][research_gardi_ramasamy_2016]
- [Gardi et al 2016][research_gardi_sabatini_2016]
- [Gardner and Poehlman 1999][research_gardner_poehlman_1999]
- [Garmendia et al 2016][research_garmendia_chakraborty_2016]
- [Garrard and Zhang 2025][research_garrard_zhang_2025]
- [Gary 1983][research_gary_1983]
- [Gasaway 1969][research_gasaway_1969]
- [Gates 1949][research_gates_1949]
- [Gates 1992][research_gates_1992]
- [Gautam et al 2014][research_gautam_sujit_2014]
- [Gaver and Jacobs 1998][research_gaver_jacobs_1998]
- [Gavrilovski et al 2011][research_gavrilovski_ward_2011]
- [Gaylor and Lightsey 2003][research_gaylor_lightsey_2003]
- [Gazzino and Lelarge 2024][research_gazzino_lelarge_2024]
- [Ge et al 2005][research_ge_gendt_2005]
- [Gebre-Egziabher 2011][research_gebreegziabher_2011]
- [Geisler et al 2014][research_geisler_rosikon_2014]
- [Geister and Geister 2013][research_geister_geister_2013]
- [General requirements for tethered][research_general_requirements]
- [General requirements for the][research_general_requirements_b]
- [Generic Aircraft Design Flowchart 2017][research_generic_aircraft_2017]
- [Geng and Wang 2007][research_geng_wang_2007]
- [Geng et al 2006][research_geng_li_2006]
- [Geng et al 2010][research_geng_deurloo_2010]
- [Geng et al 2017][research_geng_xie_2017]
- [Genrich and Minster 1991][research_genrich_minster_1991]
- [George and Ghose 2009][research_george_ghose_2009]
- [Georghiou et al 1986][research_georghiou_metcalfe_1986]
- [Georgy et al 2009][research_georgy_iqbal_2009]
- [Gerken 1979][research_gerken_1979]
- [German Hypersonics Technology Programme 1993][research_german_hypersonics_1993]
- [Germond 2025][research_germond_2025]
- [Getir Yaman et al 2025][research_getiryaman_ribeiro_2025]
- [Geva et al 2019][research_geva_abramovich_2019]
- [Ghadge and S. 2021][research_ghadge_s_2021]
- [Ghaemi et al 2019][research_ghaemi_lax_2019]
- [Ghiringhelli 2000][research_ghiringhelli_2000]
- [Ghosh Dastidar and Frazzoli 2011][research_ghoshdastidar_frazzoli_2011]
- [Gibson et al 1968][research_gibson_alexander_1968]
- [Giles 1986][research_giles_1986]
- [Giles 1995][research_giles_1995]
- [Gilge 2010][research_gilge_2010]
- [Gilhool 2005][research_gilhool_2005]
- [Gillard 1998][research_gillard_1998]
- [Gillard et al 1997][research_gillard_dorsett_1997]
- [Gillett 1994][research_gillett_1994]
- [Gillman 2015][research_gillman_2015]
- [Giorgi and G. Teunisse 2012][research_giorgi_gteunisse_2012]
- [Girish et al 2014][research_girish_emilio_2014]
- [Giunta 1999][research_giunta_1999]
- [GKN Westland aerospace management 1999][research_gkn_westland_1999]
- [Glaner and Weber 2021][research_glaner_weber_2021]
- [Glaner and Weber 2021][research_glaner_weber_2021_b]
- [Go and Ramnath 2001][research_go_ramnath_2001]
- [Goad][research_goad]
- [Goddard and Eastgate 2010][research_goddard_eastgate_2010]
- [Godha and Cannon 2007][research_godha_cannon_2007]
- [Goerttler and Schnepf 2024][research_goerttler_schnepf_2024]
- [Gold 1973][research_gold_1973]
- [Gold 1974][research_gold_1974]
- [Gold and Walchli 1974][research_gold_walchli_1974]
- [Goldstein 1982][research_goldstein_1982]
- [Golombek et al 2025][research_golombek_bustamante_2025]
- [Golombek et al 2026][research_golombek_bustamante_2026]
- [Gomez and la Cour-Harbo 2021][research_gomez_lacourharbo_2021]
- [Goncharenko et al 2019][research_goncharenko_lebedev_2019]
- [Gong and Wang 2019][research_gong_wang_2019]
- [Gong et al 2022][research_gong_xu_2022]
- [Gonzalez 2013][research_gonzalez_2013]
- [Goodall et al 2006][research_goodall_syed_2006]
- [Goodner and Rao 1988][research_goodner_rao_1988]
- [Gopejenko et al 2026][research_gopejenko_sidenko_2026]
- [Gopinath and Bakshi 2020][research_gopinath_bakshi_2020]
- [Gordnier and Visbal 1994][research_gordnier_visbal_1994]
- [Gordnier et al][research_gordnier_visbal]
- [Gordnier et al 2006][research_gordnier_visbal_2006]
- [Gordnier et al 2007][research_gordnier_sherer_2007]
- [Gorgulu et al 2023][research_gorgulu_yazar_2023]
- [Gorin et al 2024][research_gorin_gubankov_2024]
- [Goth][research_goth]
- [Gou et al 2021][research_gou_dahl_2021]
- [Goudarzi and Richards 2020][research_goudarzi_richards_2020]
- [Gough, Jr. and Carlson 1979][research_goughjr_carlson_1979]
- [Gould 2001][research_gould_2001]
- [Gould 2004][research_gould_2004]
- [Govan et al 2018][research_govan_griffith_2018]
- [Govindarajan and Sridharan 2020][research_govindarajan_sridharan_2020]
- [Goyal 2026][research_goyal_2026]
- [GPS][research_gps]
- [GPS receiver selected for 2005][research_gps_receiver_2005]
- [GPS segments 2013][research_gps_segments_2013]
- [GPS signals 2013][research_gps_signals_2013]
- [Grace 1992][research_grace_1992]
- [Grafarend 2000][research_grafarend_2000]
- [Grafarend 2003][research_grafarend_2003]
- [Graham et al 2023][research_graham_gonzalez_2023]
- [Grant and Lind 2010][research_grant_lind_2010]
- [Grantham and Williams 1987][research_grantham_williams_1987]
- [Grappel et al 2008][research_grappel_harris_2008]
- [Grasso 1994][research_grasso_1994]
- [Graves et al 2023][research_graves_snow_2023]
- [Gray 2005][research_gray_2005]
- [Gray 2015][research_gray_2015]
- [Gray and Maybeck][research_gray_maybeck]
- [Greaney 2010][research_greaney_2010]
- [Green 1998][research_green_1998]
- [Green and Findlay 2016][research_green_findlay_2016]
- [Green and Zanine 1984][research_green_zanine_1984]
- [Greenhaw 2008][research_greenhaw_2008]
- [Greer and Campbell 1980][research_greer_campbell_1980]
- [Gregory and Kim 2022][research_gregory_kim_2022]
- [Gregory and Tierno 1996][research_gregory_tierno_1996]
- [Gregory, T. J. and Wilcox, D. E. 1970][research_gregorytj_wilcoxde_1970]
- [Grejner-Brzezinska and Wang 1998][research_grejnerbrzezinska_wang_1998]
- [Grepper and Huguenin 1979][research_grepper_huguenin_1979]
- [Grigsby 2008][research_grigsby_2008]
- [Grimm 1986][research_grimm_1986]
- [Grisworld 2008][research_grisworld_2008]
- [Gross et al 2010][research_gross_gu_2010]
- [Gross et al 2010][research_gross_gu_2010_b]
- [Grosser 1965][research_grosser_1965]
- [Grotte and Brooks 1982][research_grotte_brooks_1982]
- [Grover 1966][research_grover_1966]
- [Grunch 2000][research_grunch_2000]
- [Grzegorzewski and Śliwak 2016][research_grzegorzewski_sliwak_2016]
- [Grzesik and Sobolewski 2014][research_grzesik_sobolewski_2014]
- [Gu and Enoiu 2023][research_gu_enoiu_2023]
- [Guangcai et al 2021][research_guangcai_xu_2021]
- [Gudmundsson 2014][research_gudmundsson_2014]
- [Gudmundsson 2014][research_gudmundsson_2014_b]
- [Gudmundsson 2014][research_gudmundsson_2014_c]
- [Gudmundsson 2014][research_gudmundsson_2014_d]
- [Gudmundsson 2022][research_gudmundsson_2022]
- [Gudmundsson 2022][research_gudmundsson_2022_b]
- [Gudmundsson 2022][research_gudmundsson_2022_c]
- [Guelman 2014][research_guelman_2014]
- [Guerrero 2012][research_guerrero_2012]
- [Guidance on aircraft turnaround 2001][research_guidance_on_2001]
- [Guide for Installation of][research_guide_for]
- [Guide for Unmanned Undersea][research_guide_for_b]
- [Guide for Wing Interface][research_guide_for_c]
- [Guiler][research_guiler]
- [Guiler and Huebsch 2005][research_guiler_huebsch_2005]
- [Guiler and Huebsch 2005][research_guiler_huebsch_2005_b]
- [Guillen et al][research_guillen_bell]
- [Gunawardana and Alonso 2013][research_gunawardana_alonso_2013]
- [Gunetti et al 2013][research_gunetti_thompson_2013]
- [Guo 2007][research_guo_2007]
- [Guo 2013][research_guo_2013]
- [Guo et al][research_guo_sun]
- [Guo et al 2006][research_guo_yamamoto_2006]
- [Guo et al 2013][research_guo_cain_2013]
- [Guo et al 2023][research_guo_han_2023]
- [Guo et al 2024][research_guo_geng_2024]
- [Guo et al 2025][research_guo_li_2025]
- [Guo et al 2026][research_guo_han_2026]
- [Guo et al 2026][research_guo_liu_2026]
- [Guoqing et al 2016][research_guoqing_tiantian_2016]
- [Guorong Zhao et al 2006][research_guorongzhao_jixinli_2006]
- [Guth 2015][research_guth_2015]
- [Gutt et al 2004][research_gutt_fischer_2004]
- [Gwin 1976][research_gwin_1976]
- [Gürsoylu et al 2025][research_gursoylu_sziroczak_2025]
- [H.M. Aircraft-Carrier Ark Royal 1939][research_h_m_aircraft_carrier_1939]
- [Ha 1995][research_ha_1995]
- [Ha 2008][research_ha_2008]
- [Haak 1994][research_haak_1994]
- [Haas et al 2000][research_haas_gorb_2000]
- [Habashi 2023][research_habashi_2023]
- [Hafer 2009][research_hafer_2009]
- [Hagele and Soffker 2017][research_hagele_soffker_2017]
- [Haider et al 2023][research_haider_mansor_2023]
- [Haitao and Yan 2021][research_haitao_yan_2021]
- [Haiyang Chao and YangQuan Chen 2010][research_haiyangchao_yangquanchen_2010]
- [Hajiyev and Aykut Tutucu 2001][research_hajiyev_aykuttutucu_2001]
- [Hajiyev and Tutucu 2003][research_hajiyev_tutucu_2003]
- [Haley 1990][research_haley_1990]
- [Hall 1971][research_hall_1971]
- [Hamlin 1990][research_hamlin_1990]
- [Hammack and Mullen 1995][research_hammack_mullen_1995]
- [Hammond 1986][research_hammond_1986]
- [Hamnanaka 2018][research_hamnanaka_2018]
- [Han 2022][research_han_2022]
- [Han and Wang 2011][research_han_wang_2011]
- [Han et al 2012][research_han_lee_2012]
- [Han et al 2016][research_han_xu_2016]
- [Han et al 2019][research_han_kang_2019]
- [Han et al 2019][research_han_xiao_2019]
- [Han et al 2025][research_han_xu_2025]
- [Han et al 2026][research_han_wu_2026]
- [Han et al 2026][research_han_zou_2026]
- [Handling qualities 2000][research_handling_qualities_2000]
- [Handling Qualities Analysis 2008][research_handling_qualities_2008]
- [Handling Qualities and Control 2017][research_handling_qualities_2017]
- [Hann-Shing Ju et al][research_hannshingju_chingchihtsai]
- [Hao and Huang 2009][research_hao_huang_2009]
- [Hao and Yongqi 2024][research_hao_yongqi_2024]
- [Hao et al 2018][research_hao_xu_2018]
- [Hardy et al 2016][research_hardy_strader_2016]
- [Harford 1989][research_harford_1989]
- [Haritos and Barnhart 2021][research_haritos_barnhart_2021]
- [Harley et al 2009][research_harley_wilde_2009]
- [Harned and Head 1965][research_harned_head_1965]
- [Harper 1936][research_harper_1936]
- [Harper and Sardanowsky 1969][research_harper_sardanowsky_1969]
- [Harris 1961][research_harris_1961]
- [Harris et al 2000][research_harris_gautrey_2000]
- [Hart 1956][research_hart_1956]
- [Hart and Williams 2008][research_hart_williams_2008]
- [Hartana][research_hartana]
- [Harting 1981][research_harting_1981]
- [Hartman and Johnson 1998][research_hartman_johnson_1998]
- [Hartmann et al 2017][research_hartmann_schutt_2017]
- [Hartmann et al 2021][research_hartmann_noland_2021]
- [Hartmann et al 2024][research_hartmann_scott_2024]
- [Hartmann et al 2024][research_hartmann_scott_2024_b]
- [Hartney][research_hartney]
- [Hassairi and Abid 2021][research_hassairi_abid_2021]
- [Hatch et al 2007][research_hatch_williamd_2007]
- [Haugen 1966][research_haugen_1966]
- [Hauschildt et al 1981][research_hauschildt_gripp_1981]
- [Hauser 1999][research_hauser_1999]
- [Havey and Kline 1989][research_havey_kline_1989]
- [Hawker 1991][research_hawker_1991]
- [Hawker 1992][research_hawker_1992]
- [Hawkins 1982][research_hawkins_1982]
- [Hawkins 2017][research_hawkins_2017]
- [Haxhi and Gikas 2023][research_haxhi_gikas_2023]
- [Hayase 1974][research_hayase_1974]
- [Hayase 1974][research_hayase_1974_b]
- [Hayes 2006][research_hayes_2006]
- [Hays 1989][research_hays_1989]
- [Hazlett et al 2011][research_hazlett_crassidis_2011]
- [He et al 2004][research_he_xin_2004]
- [He et al 2013][research_he_le_2013]
- [He et al 2026][research_he_wang_2026]
- [Head and Hohenemser 1951][research_head_hohenemser_1951]
- [Heffley 1986][research_heffley_1986]
- [Heilenday 2000][research_heilenday_2000]
- [Heimbs et al 2012][research_heimbs_lang_2012]
- [Heit and Liscouet-Hanke 2023][research_heit_liscouethanke_2023]
- [Heitmeir et al 1992][research_heitmeir_lederer_1992]
- [Heller 1961][research_heller_1961]
- [Heller and Dobrzynski 1976][research_heller_dobrzynski_1976]
- [Helliwell 1952][research_helliwell_1952]
- [Hemati et al 2012][research_hemati_eldredge_2012]
- [Henderson 2023][research_henderson_2023]
- [Henkel and Günther 2012][research_henkel_gunther_2012]
- [Henkel and Zhu 2011][research_henkel_zhu_2011]
- [Henne 1989][research_henne_1989]
- [Henrickson et al 2016][research_henrickson_rogers_2016]
- [Heo et al 2004][research_heo_pervan_2004]
- [Hept 2002][research_hept_2002]
- [Herbst and Klöckner 2014][research_herbst_klockner_2014]
- [Herdiana et al 2023][research_herdiana_arifin_2023]
- [Hermann et al 1995][research_hermann_evans_1995]
- [Hermanutz and Hornung 2020][research_hermanutz_hornung_2020]
- [Herpers 1965][research_herpers_1965]
- [Herrera 2014][research_herrera_2014]
- [Herrera Rubio and Parra Prada 2019][research_herrerarubio_parraprada_2019]
- [Herrmann 2004][research_herrmann_2004]
- [Hess 1981][research_hess_1981]
- [Hess 1984][research_hess_1984]
- [Hess 2010][research_hess_2010]
- [Hess 2018][research_hess_2018]
- [Hess 2019][research_hess_2019]
- [Hess and Judd 1976][research_hess_judd_1976]
- [Hewgley et al 2011][research_hewgley_yakimenko_2011]
- [Hewgley et al 2014][research_hewgley_cristi_2014]
- [Hewitson and Wang 2007][research_hewitson_wang_2007]
- [Hewitson et al 2004][research_hewitson_kyulee_2004]
- [Hewitt et al 2005][research_hewitt_weiss_2005]
- [Heyns and Borden 2017][research_heyns_borden_2017]
- [Hicks 1968][research_hicks_1968]
- [Hicks and Durbin 2014][research_hicks_durbin_2014]
- [Hicks et al 2002][research_hicks_petrov_2002]
- [Hide et al][research_hide_moore]
- [Hide et al 2003][research_hide_moore_2003]
- [High altitude reconnaissance aircraft 1989][research_high_altitude_1989]
- [High-Altitude Long-Endurance HALE Sensor 2026][research_high_altitude_long_endurance_2026]
- [High-Lift Devices 2010][research_high_lift_devices_2010]
- [High-Precision GPS Systems 2011][research_high_precision_gps_2011]
- [Hightower 1985][research_hightower_1985]
- [Hildebrand 1945][research_hildebrand_1945]
- [Hill 1987][research_hill_1987]
- [Hill and Waters 1974][research_hill_waters_1974]
- [Hinchey et al][research_hinchey_rash]
- [Hinsz 2006][research_hinsz_2006]
- [Hintzke and Haggard 1991][research_hintzke_haggard_1991]
- [Hirlinger 2001][research_hirlinger_2001]
- [Hirsch and Schroeder 2014][research_hirsch_schroeder_2014]
- [Hirschel 1991][research_hirschel_1991]
- [Hirschel 1993][research_hirschel_1993]
- [Hirsh 1965][research_hirsh_1965]
- [Historical Design Information of][research_historical_design]
- [History of Supersonic Transport 2020][research_history_of_2020]
- [Hiyama 1974][research_hiyama_1974]
- [Hiyama 1974][research_hiyama_1974_b]
- [Hobbs 2010][research_hobbs_2010]
- [Hobbs, Alan et al 2016][research_hobbsalan_cardozacolleen_2016]
- [Hobe et al 2026][research_hobe_heile_2026]
- [Hochstetler et al 2016][research_hochstetler_bosma_2016]
- [Hodgart and Purivigraipong][research_hodgart_purivigraipong]
- [Hodgkinson and Johnston 2018][research_hodgkinson_johnston_2018]
- [Hodgkinson and Johnston 2018][research_hodgkinson_johnston_2018_b]
- [Hodgkinson and Johnston 2018][research_hodgkinson_johnston_2018_c]
- [Hodgkinson and Johnston 2018][research_hodgkinson_johnston_2018_d]
- [Hodgkinson and Johnston 2018][research_hodgkinson_johnston_2018_e]
- [Hodgkinson and Johnston 2018][research_hodgkinson_johnston_2018_f]
- [Hoffer et al 2013][research_hoffer_coopmans_2013]
- [Hoffler et al 1986][research_hoffler_rao_1986]
- [Hoh 1988][research_hoh_1988]
- [Hoh and Mitchell 1983][research_hoh_mitchell_1983]
- [Holcroft, Christopher Mark, born 2014][research_holcroft_christopher_2014]
- [Holland et al 2009][research_holland_lalejini_2009]
- [Holloway et al 1972][research_holloway_thompson_1972]
- [Holmes 2000][research_holmes_2000]
- [Holubik 1988][research_holubik_1988]
- [Hon et al 2022][research_hon_karpuk_2022]
- [Hone et al 2011][research_hone_friedman_2011]
- [Hongwei et al 2006][research_hongwei_zhihua_2006]
- [Hoogreef 2026][research_hoogreef_2026]
- [Hopchak et al 2022][research_hopchak_davis_2022]
- [Hopkins et al 2010][research_hopkins_nix_2010]
- [Horn 1973][research_horn_1973]
- [Horn et al 2014][research_horn_tritschler_2014]
- [Horn et al 2015][research_horn_tritschler_2015]
- [Horn et al 2017][research_horn_thorsen_2017]
- [Hornbuckle 2015][research_hornbuckle_2015]
- [Horowitz et al 2014][research_horowitz_beling_2014]
- [Horrigan 1990][research_horrigan_1990]
- [Horvath and Wells 2018][research_horvath_wells_2018]
- [Hosseini and Jalili 2025][research_hosseini_jalili_2025]
- [hosseini et al 2024][research_hosseini_jalili_2024]
- [Hossny et al 2020][research_hossny_elbadawy_2020]
- [Hou et al 2020][research_hou_fang_2020]
- [Hou et al 2022][research_hou_lv_2022]
- [Hou et al 2024][research_hou_zhang_2024]
- [Hou et al 2025][research_hou_shi_2025]
- [Hou et al 2025][research_hou_wang_2025]
- [Hough et al 2024][research_hough_mohammadi_2024]
- [Housel 1952][research_housel_1952]
- [Houtsma 2003][research_houtsma_2003]
- [How et al 2014][research_how_frazzoli_2014]
- [Howard 1995][research_howard_1995]
- [Howard 1996][research_howard_1996]
- [Howard 2002][research_howard_2002]
- [Howard 2023][research_howard_2023]
- [Howe 2000][research_howe_2000]
- [Howe 2000][research_howe_2000_b]
- [Howie and Frizzell][research_howie_frizzell]
- [Hoy 1963][research_hoy_1963]
- [Hsin 1973][research_hsin_1973]
- [Hsin 1974][research_hsin_1974]
- [Hu et al 2018][research_hu_wu_2018]
- [Hu et al 2019][research_hu_bent_2019]
- [Hu et al 2020][research_hu_gao_2020]
- [Hu et al 2020][research_hu_ni_2020]
- [Hu et al 2026][research_hu_liu_2026]
- [Huan-Jung Lin][research_huanjunglin]
- [Huang 2013][research_huang_2013]
- [Huang and Tomlin 2009][research_huang_tomlin_2009]
- [Huang and Wei 2025][research_huang_wei_2025]
- [Huang and Zhang 2020][research_huang_zhang_2020]
- [Huang et al 2011][research_huang_yu_2011]
- [Huang et al 2019][research_huang_zhao_2019]
- [Huang et al 2019][research_huang_zhu_2019]
- [Huang et al 2019][research_huang_zhu_2019_b]
- [Huang et al 2019][research_huang_zhu_2019_c]
- [Huang et al 2026][research_huang_chen_2026]
- [Hubbell][research_hubbell]
- [Huber 2022][research_huber_2022]
- [Huber and Reynolds 1976][research_huber_reynolds_1976]
- [Huber et al 2012][research_huber_schutte_2012]
- [Hughes 1982][research_hughes_1982]
- [Hughes aircraft nominates payload 1984][research_hughes_aircraft_1984]
- [Hui 2016][research_hui_2016]
- [Hui et al 2014][research_hui_liu_2014]
- [Human Catapult Managing Relationships 2014][research_human_catapult_2014]
- [Human Factors in Unmanned 2016][research_human_factors_2016]
- [Human factors review of 1982][research_human_factors_1982]
- [Hummel and Oelker 1994][research_hummel_oelker_1994]
- [Humphreys et al 1988][research_humphreys_paulsonjr_1988]
- [Hundley et al 1993][research_hundley_rowson_1993]
- [Hunn 2005][research_hunn_2005]
- [Hunter et al 2018][research_hunter_schaal_2018]
- [Huntington and Lyrintzis 1996][research_huntington_lyrintzis_1996]
- [Huntington and Lyrintzis 1998][research_huntington_lyrintzis_1998]
- [Hunziker 1968][research_hunziker_1968]
- [Hutchison et al 1994][research_hutchison_unger_1994]
- [Hutmacher 2011][research_hutmacher_2011]
- [Huttunen and Scott 2023][research_huttunen_scott_2023]
- [Huyer et al 1992][research_huyer_robinson_1992]
- [Hvezda 2021][research_hvezda_2021]
- [Hwang and Brown 1990][research_hwang_brown_1990]
- [Hwang and Pi 1978][research_hwang_pi_1978]
- [Hwang and Pi 1979][research_hwang_pi_1979]
- [Hwang and Speyer 2009][research_hwang_speyer_2009]
- [Hwang et al 2007][research_hwang_balakrishnan_2007]
- [Hynes et al 1989][research_hynes_franklin_1989]
- [Hůlek 2015][research_hulek_2015]
- [I. Scott and T. Huttunen 2023][research_iscott_thuttunen_2023]
- [Ibrahim 2008][research_ibrahim_2008]
- [Ibrahim 2011][research_ibrahim_2011]
- [Idris et al 2014][research_idris_sathyamoorthy_2014]
- [IEC in-flight system chosen 1999][research_iec_in_flight_1999]
- [Ikonen and Sobester 2016][research_ikonen_sobester_2016]
- [Illustrations and Comments on 2016][research_illustrations_and_2016]
- [Imado and Kuroda 2011][research_imado_kuroda_2011]
- [In-flight control and guidance 2006][research_in_flight_control_2006]
- [In-Flight Refuelling 1961][research_in_flight_refuelling_1961]
- [Incremona and Ferrara 2023][research_incremona_ferrara_2023]
- [Ingram et al 2015][research_ingram_dendinger_2015]
- [Initial evaluation of video 2012][research_initial_evaluation_2012]
- [Initial Sizing 2024][research_initial_sizing_2024]
- [Initial Tail Sizing 2013][research_initial_tail_2013]
- [Initial Unmanned Aircraft Sizing 2014][research_initial_unmanned_2014]
- [Initial Unmanned-Aircraft Sizing 2012][research_initial_unmanned_aircraft_2012]
- [Initiative for aircraft launch 2007][research_initiative_for_2007]
- [Inoyama et al 2008][research_inoyama_sanders_2008]
- [Instrument Panel Arrangement for][research_instrument_panel]
- [Integrated wing research programme 2006][research_integrated_wing_2006]
- [Integration of GPS and 1991][research_integration_of_1991]
- [International Conference on Unmanned 2013][research_international_conference_2013]
- [International Conference on Unmanned 2014][research_international_conference_2014]
- [International Conference on Unmanned 2015][research_international_conference_2015]
- [International Conference on Unmanned 2016][research_international_conference_2016]
- [International Conference on Unmanned 2017][research_international_conference_2017]
- [International Conference on Unmanned 2018][research_international_conference_2018]
- [International Conference on Unmanned 2019][research_international_conference_2019]
- [International Conference on Unmanned 2020][research_international_conference_2020]
- [International Conference on Unmanned 2021][research_international_conference_2021]
- [International Conference on Unmanned 2021][research_international_conference_2021_b]
- [International Conference on Unmanned 2022][research_international_conference_2022]
- [International Conference on Unmanned 2023][research_international_conference_2023]
- [International Conference on Unmanned 2024][research_international_conference_2024]
- [International Conference on Unmanned 2025][research_international_conference_2025]
- [International Conference on Unmanned 2026][research_international_conference_2026]
- [International Symposium on Unmanned 2024][research_international_symposium_2024]
- [Introduction to Aircraft Aerodynamic 2021][research_introduction_to_2021]
- [Introduction to Aircraft Flight 1998][research_introduction_to_1998]
- [Introduction to Unmanned Aircraft 2010][research_introduction_to_2010]
- [Ioannidis et al][research_ioannidis_walton]
- [Iran will destroy a 2020][research_iran_will_2020]
- [Irigireddy and Moncayo 2020][research_irigireddy_moncayo_2020]
- [Irvin and Swan 1956][research_irvin_swan_1956]
- [Isaacs et al 2016][research_isaacs_ezal_2016]
- [Islam and Saha 2017][research_islam_saha_2017]
- [Islam et al 2024][research_islam_mohona_2024]
- [Ito et al 2016][research_ito_endo_2016]
- [Itt Systems Rome Ny 1987][research_ittsystemsromeny_1987]
- [Iwamoto et al 2016][research_iwamoto_takewa_2016]
- [Işilak and Oktal 2025][research_isilak_oktal_2025]
- [İşci and Günel 2021][research_isci_gunel_2021]
- [J. et al 2013][research_j_golubkov_2013]
- [J.M. Urnes et al 1981][research_jmurnes_moomaw_1981]
- [Jabbal 2015][research_jabbal_2015]
- [Jackson 2001][research_jackson_2001]
- [Jackson et al 1996][research_jackson_jr_1996]
- [Jacob 1989][research_jacob_1989]
- [Jacobson and Tsubaki 1986][research_jacobson_tsubaki_1986]
- [Jagtap 2025][research_jagtap_2025]
- [Jahangirova et al 2021][research_jahangirova_stocco_2021]
- [James 1972][research_james_1972]
- [James Joseph et al][research_jamesjoseph_davidjkinney]
- [James Joseph et al][research_jamesjoseph_davidjkinney_b]
- [Jameson 2009][research_jameson_2009]
- [Jamison 2010][research_jamison_2010]
- [Janousek and Marcon 2018][research_janousek_marcon_2018]
- [Janousek et al 2010][research_janousek_bjorn_2010]
- [Japan's aircraft carrier plan 2018][research_japan_s_aircraft_2018]
- [Jategaonkar et al 2006][research_jategaonkar_behr_2006]
- [Jauron 1993][research_jauron_1993]
- [Jazzar and Kale 2023][research_jazzar_kale_2023]
- [Jenkins et al 2005][research_jenkins_snodgrass_2005]
- [Jenkinson et al 2000][research_jenkinson_page_2000]
- [Jensen 2016][research_jensen_2016]
- [Jensen 2021][research_jensen_2021]
- [Jeong et al 2023][research_jeong_kee_2023]
- [Jeong et al 2025][research_jeong_kee_2025]
- [Jeong Won Kim et al][research_jeongwonkim_donghwanhwang]
- [Ji et al 2013][research_ji_xu_2013]
- [Jia et al 2011][research_jia_han_2011]
- [Jia et al 2016][research_jia_chen_2016]
- [Jian and Ke-Qin 2004][research_jian_keqin_2004]
- [Jian-jun et al 2003][research_jianjun_xiaoli_2003]
- [Jianan Wang and Ming Xin 2013][research_jiananwang_mingxin_2013]
- [Jiancheng Fang and Xiaolin Gong 2010][research_jianchengfang_xiaolingong_2010]
- [Jiang and Muluneh Mekonnen 2013][research_jiang_mulunehmekonnen_2013]
- [Jiang et al 2013][research_jiang_zhu_2013]
- [Jiang et al 2016][research_jiang_stol_2016]
- [Jiang et al 2016][research_jiang_zhang_2016]
- [Jiang et al 2017][research_jiang_su_2017]
- [Jiang et al 2018][research_jiang_zhen_2018]
- [Jiang et al 2019][research_jiang_zhang_2019]
- [Jiang et al 2022][research_jiang_liu_2022]
- [Jiang et al 2022][research_jiang_nan_2022]
- [Jiang et al 2024][research_jiang_yan_2024]
- [Jianping Yuan et al 1998][research_jianpingyuan_jianjunluo_1998]
- [Jiao et al 2018][research_jiao_rino_2018]
- [Jiayao et al 2020][research_jiayao_dalong_2020]
- [Jie et al 2017][research_jie_wenhai_2017]
- [Jiguang Li et al 2016][research_jiguangli_xinchen_2016]
- [Jin 2024][research_jin_2024]
- [Jin et al 2011][research_jin_song_2011]
- [Jing and Zheng-Chun 2015][research_jing_zhengchun_2015]
- [Jing et al 2015][research_jing_xu_2015]
- [Jo et al 2016][research_jo_park_2016]
- [Joerger and Pervan 2012][research_joerger_pervan_2012]
- [Johansen and Perez 2016][research_johansen_perez_2016]
- [John 2014][research_john_2014]
- [Johnson 1966][research_johnson_1966]
- [Johnson 1972][research_johnson_1972]
- [Johnson 1985][research_johnson_1985]
- [Johnson 1993][research_johnson_1993]
- [Johnson 1995][research_johnson_1995]
- [Johnson 1997][research_johnson_1997]
- [Johnson and Ivanov 2011][research_johnson_ivanov_2011]
- [Johnson and Robertson 1980][research_johnson_robertson_1980]
- [Johnson et al 2007][research_johnson_ansar_2007]
- [Johnson, Joseph L. 1949][research_johnsonjosephl_1949]
- [Johnson, Jr. and White 1983][research_johnsonjr_white_1983]
- [Johnston and Friend 1965][research_johnston_friend_1965]
- [Johnston and Swenson 2009][research_johnston_swenson_2009]
- [Johnston and Swenson 2010][research_johnston_swenson_2010]
- [Johnstone 1968][research_johnstone_1968]
- [Jones 1973][research_jones_1973]
- [Jones 1992][research_jones_1992]
- [Jones 2009][research_jones_2009]
- [Jones and Dye 2016][research_jones_dye_2016]
- [Jones and Marsh 2003][research_jones_marsh_2003]
- [Jones et al 2023][research_jones_klyde_2023]
- [Jones, Thomas, W. and Hoppe, John C. 2001][research_jonesthomasw_hoppejohnc_2001]
- [Joslin 2015][research_joslin_2015]
- [Journal of Aerospace Technology][research_journal_of]
- [Juang * and Chio 2005][research_juang_chio_2005]
- [Julke and Kawa 2000][research_julke_kawa_2000]
- [Jun 2023][research_jun_2023]
- [Jun et al 2003][research_jun_tischler_2003]
- [Junfeng et al 2020][research_junfeng_wuzhou_2020]
- [Junli Chen et al 2010][research_junlichen_xiaoliangwang_2010]
- [Jurges 1977][research_jurges_1977]
- [Jurges 1999][research_jurges_1999]
- [Jwo 2004][research_jwo_2004]
- [Jwo and Chang 2009][research_jwo_chang_2009]
- [Jwo and Chung 2010][research_jwo_chung_2010]
- [Jwo and Huang 2007][research_jwo_huang_2007]
- [Jwo and Lai 2007][research_jwo_lai_2007]
- [Jwo et al 2009][research_jwo_chen_2009]
- [Jwo et al 2013][research_jwo_yang_2013]
- [K. Senthil Kumar and J. Shanmugam 2023][research_ksenthilkumar_jshanmugam_2023]
- [Kahya and Konar 2026][research_kahya_konar_2026]
- [Kai et al 2026][research_kai_binghong_2026]
- [Kaidan 2026][research_kaidan_2026]
- [Kaliardos and Lyall 2014][research_kaliardos_lyall_2014]
- [Kaliszuk et al 2025][research_kaliszuk_kierzkowski_2025]
- [Kallinen][research_kallinen]
- [Kallinen et al 2020][research_kallinen_martin_2020]
- [Kalman Filter Basics 2000][research_kalman_filter_2000]
- [Kalman Filter Engineering 2000][research_kalman_filter_2000_b]
- [Kambampati and Smith 2017][research_kambampati_smith_2017]
- [Kaminski 1997][research_kaminski_1997]
- [Kaminski and Ralston 1996][research_kaminski_ralston_1996]
- [Kamman and Hall 1978][research_kamman_hall_1978]
- [kanahara 2022][research_kanahara_2022]
- [Kane 2014][research_kane_2014]
- [Kang et al 2018][research_kang_park_2018]
- [Kang et al 2018][research_kang_park_2018_b]
- [Kannan and Min 2022][research_kannan_min_2022]
- [Kansas Univ Lawrence 1952][research_kansasunivlawrence_1952]
- [Kansas Univ Lawrence 1952][research_kansasunivlawrence_1952_b]
- [Kao et al 2018][research_kao_white_2018]
- [Kapidžić et al 2014][research_kapidzic_nilsson_2014]
- [Kaplan 1965][research_kaplan_1965]
- [Kaplan 1965][research_kaplan_1965_b]
- [Kaplan 1969][research_kaplan_1969]
- [Kaplan and sargent 1965][research_kaplan_sargent_1965]
- [Kaplan and Sargent 1970][research_kaplan_sargent_1970]
- [Karagoz et al 2019][research_karagoz_reilley_2019]
- [Karimi Kelayeh and Djavareshkian 2024][research_karimikelayeh_djavareshkian_2024]
- [Karimidoona and Schön 2022][research_karimidoona_schon_2022]
- [Karpuk 2026][research_karpuk_2026]
- [Kartal and Yüksek 2025][research_kartal_yuksek_2025]
- [Karásek et al 2026][research_karasek_kallies_2026]
- [Kasim 2018][research_kasim_2018]
- [Kasim Biber and Trenton White 2019][research_kasimbiber_trentonwhite_2019]
- [Kasuda 2011][research_kasuda_2011]
- [Kasuga et al 2017][research_kasuga_yoshida_2017]
- [Katrňák and Juračka 2017][research_katrnak_juracka_2017]
- [Katz 1967][research_katz_1967]
- [Katz 1979][research_katz_1979]
- [Katz 2017][research_katz_2017]
- [Katz 2025][research_katz_2025]
- [Katzenstein and Bjornstad 1987][research_katzenstein_bjornstad_1987]
- [Kaul 2019][research_kaul_2019]
- [Kaul 2020][research_kaul_2020]
- [Kaur][research_kaur]
- [Kawamura et al 2022][research_kawamura_kannan_2022]
- [Kawano et al 2001][research_kawano_mokuno_2001]
- [Kaye and Freeman 1989][research_kaye_freeman_1989]
- [Kaymal 2016][research_kaymal_2016]
- [Ke et al 2009][research_ke_tsourdos_2009]
- [Ke et al 2014][research_ke_zhengzhong_2014]
- [Keane et al 2017][research_keane_sobester_2017]
- [Kee et al 2004][research_kee_park_2004]
- [Keeping cool at flight 1996][research_keeping_cool_1996]
- [Keidel et al 2019][research_keidel_fasel_2019]
- [Kei̇yi̇nci̇ and Aydin 2021][research_keiyinci_aydin_2021]
- [Keke et al 2014][research_keke_nong_2014]
- [Keke et al 2014][research_keke_qing_2014]
- [Kelley et al][research_kelley_katz]
- [Kelly 2001][research_kelly_2001]
- [Kelly and Davis 1994][research_kelly_davis_1994]
- [Kelly and Skudrna 1981][research_kelly_skudrna_1981]
- [Kemper 2004][research_kemper_2004]
- [Kennedy 1999][research_kennedy_1999]
- [Kennedy and Floyd D. 1985][research_kennedy_floydd_1985]
- [Keong et al 2019][research_keong_shin_2019]
- [Kern et al 2020][research_kern_bobbe_2020]
- [Kessler et al 2000][research_kessler_spearing_2000]
- [Ketterle et al 2008][research_ketterle_vuletic_2008]
- [Kewley et al 2016][research_kewley_lowenberg_2016]
- [Khalid 2023][research_khalid_2023]
- [Khalid et al 2026][research_khalid_ahmed_2026]
- [Khan 2021][research_khan_2021]
- [Khan and Khorasani 2010][research_khan_khorasani_2010]
- [Khan and Nahon 2014][research_khan_nahon_2014]
- [Khanafseh and Pervan 2007][research_khanafseh_pervan_2007]
- [Khanafseh and Pervan 2008][research_khanafseh_pervan_2008]
- [Kharchenko et al 2015][research_kharchenko_bogoslavets_2015]
- [Khazetdinov et al 2021][research_khazetdinov_zakiev_2021]
- [Khodabandeh and Teunissen 2022][research_khodabandeh_teunissen_2022]
- [Khreish et al 2005][research_khreish_sinha_2005]
- [Kidwell et al 2012][research_kidwell_calhoun_2012]
- [Kiflu and Lopez 2015][research_kiflu_lopez_2015]
- [Kilgore et al 2009][research_kilgore_nehme_2009]
- [Kilkis 2024][research_kilkis_2024]
- [Kim 2019][research_kim_2019]
- [Kim and Bang 2016][research_kim_bang_2016]
- [Kim and Costello 2016][research_kim_costello_2016]
- [Kim and Oh 2017][research_kim_oh_2017]
- [Kim and Park 2007][research_kim_park_2007]
- [Kim and Sung 2025][research_kim_sung_2025]
- [Kim and Sung 2025][research_kim_sung_2025_b]
- [Kim et al][research_kim_jee]
- [Kim et al 2012][research_kim_won_2012]
- [Kim et al 2013][research_kim_choi_2013]
- [Kim et al 2015][research_kim_jung_2015]
- [Kim et al 2022][research_kim_gregory_2022]
- [Kim et al 2024][research_kim_kang_2024]
- [Kim et al 2024][research_kim_kim_2024]
- [Kim et al 2025][research_kim_kim_2025]
- [Kindley 2015][research_kindley_2015]
- [King][research_king]
- [Kirk et al 2022][research_kirk_wang_2022]
- [Kirnon et al 2019][research_kirnon_majar_2019]
- [Kis and Lantos 2011][research_kis_lantos_2011]
- [Kishi and Pfeffer 1971][research_kishi_pfeffer_1971]
- [Kistyarev and Wang 2025][research_kistyarev_wang_2025]
- [Kitts and Lucas 1963][research_kitts_lucas_1963]
- [Kladis et al 2008][research_kladis_economou_2008]
- [Klein 2002][research_klein_2002]
- [Klein et al 2017][research_klein_krainski_2017]
- [Klemin 1940][research_klemin_1940]
- [Kleusberg 1989][research_kleusberg_1989]
- [Kline 2012][research_kline_2012]
- [Klingelhoefer 2005][research_klingelhoefer_2005]
- [Klipp et al 2021][research_klipp_kirk_2021]
- [Klishin and Kolesnikova 2022][research_klishin_kolesnikova_2022]
- [Klyde et al 1999][research_klyde_mitchell_1999]
- [Klyde et al 2020][research_klyde_schulze_2020]
- [Klyde et al 2021][research_klyde_lampton_2021]
- [Knowles et al 2012][research_knowles_krauskopf_2012]
- [Knuth et al 2012][research_knuth_cassano_2012]
- [Knutzon][research_knutzon]
- [Ko and Kumar 2019][research_ko_kumar_2019]
- [Kochenderfer et al 2008][research_kochenderfer_kuchar_2008]
- [Koenke et al][research_koenke_hill]
- [Kogiso et al 2000][research_kogiso_tsushima_2000]
- [Koh and Paranjape 2020][research_koh_paranjape_2020]
- [Kolpitcke and Smith 2025][research_kolpitcke_smith_2025]
- [Kometani 2005][research_kometani_2005]
- [Konar et al 2024][research_konar_ozdemir_2024]
- [Kondo and Yasuda 2006][research_kondo_yasuda_2006]
- [Konert and Balcerzak 2021][research_konert_balcerzak_2021]
- [Koo and Sastry 2003][research_koo_sastry_2003]
- [Koo et al 2015][research_koo_kim_2015]
- [Kopeikin et al 2013][research_kopeikin_ponda_2013]
- [Koremura][research_koremura]
- [Korpela et al 2011][research_korpela_danko_2011]
- [Korzatkowski et al 2015][research_korzatkowski_kolsch_2015]
- [Kotsinis et al 2026][research_kotsinis_karras_2026]
- [Kottapalli, Anjaney P. and Harris, Franklin D. 2012][research_kottapallianjaneyp_harrisfranklind_2012]
- [Kovach and Conley 1991][research_kovach_conley_1991]
- [Kovtun and Tkachenko 2018][research_kovtun_tkachenko_2018]
- [Kovtun and Tkachenko 2019][research_kovtun_tkachenko_2019]
- [Kowal][research_kowal]
- [Kozel and Cardoza][research_kozel_cardoza]
- [Kozhanov et al 2022][research_kozhanov_suvorova_2022]
- [Kozol and Tankins 1993][research_kozol_tankins_1993]
- [Kozłowski and Bołoz 2024][research_kozlowski_boloz_2024]
- [Krabacher 1993][research_krabacher_1993]
- [Kramer et al 2023][research_kramer_bailey_2023]
- [Krammer et al 2021][research_krammer_scherer_2021]
- [Krasuski and Wierzbicki 2018][research_krasuski_wierzbicki_2018]
- [Krawczyk et al 2019][research_krawczyk_szczepanski_2019]
- [Kreerenko 2025][research_kreerenko_2025]
- [Krempasky 1996][research_krempasky_1996]
- [Krempasky 1999][research_krempasky_1999]
- [Krempasky and Krempasky 1997][research_krempasky_krempasky_1997]
- [Krengel et al 2019][research_krengel_hepperle_2019]
- [Krings et al 2013][research_krings_annighofer_2013]
- [Krishna Kamath et al 2020][research_krishnakamath_kumartripathi_2020]
- [Krispin and Portnoy 1988][research_krispin_portnoy_1988]
- [Krizek et al 2022][research_krizek_horyna_2022]
- [Kroo 1983][research_kroo_1983]
- [Kroo 1986][research_kroo_1986]
- [Krozel 2002][research_krozel_2002]
- [Krozel and Andrisani 1990][research_krozel_andrisani_1990]
- [Kryvokhatko 2023][research_kryvokhatko_2023]
- [Kryvokhatko 2023][research_kryvokhatko_2023_b]
- [Kryvokhatko 2024][research_kryvokhatko_2024]
- [Kryvokhatko 2024][research_kryvokhatko_2024_b]
- [Krzykowska-Piotrowska 2020][research_krzykowskapiotrowska_2020]
- [Krüger et al 1997][research_kruger_besselink_1997]
- [Krüger et al 2022][research_kruger_meddaikar_2022]
- [Kube et al 2018][research_kube_bischof_2018]
- [Kubo et al][research_kubo_ito]
- [Kubo et al 2004][research_kubo_muto_2004]
- [Kubo et al 2007][research_kubo_fujita_2007]
- [Kucherov et al 2019][research_kucherov_sushchenko_2019]
- [Kuczera and Hauck 1992][research_kuczera_hauck_1992]
- [Kuczera et al 1993][research_kuczera_hauck_1993]
- [Kukla 2026][research_kukla_2026]
- [Kumar][research_kumar]
- [Kumar 1997][research_kumar_1997]
- [Kumar 2020][research_kumar_2020]
- [Kumar and Kumar 2022][research_kumar_kumar_2022]
- [Kumar et al 2007][research_kumar_shanmugam_2007]
- [Kumar et al 2019][research_kumar_yokeshraj_2019]
- [Kumar et al 2020][research_kumar_mandal_2020]
- [Kumar et al 2020][research_kumar_mandal_2020_b]
- [Kumar et al 2026][research_kumar_mittal_2026]
- [Kumar Rath et al 2020][research_kumarrath_ramirezserrano_2020]
- [Kumuk and Ilbas 2023][research_kumuk_ilbas_2023]
- [Kundu and Raghunathan 2000][research_kundu_raghunathan_2000]
- [Kuo and Hsu 1997][research_kuo_hsu_1997]
- [Kuppusamy and Yoon 2016][research_kuppusamy_yoon_2016]
- [Kurdel et al 2024][research_kurdel_gecejova_2024]
- [Kurdyla 1963][research_kurdyla_1963]
- [Kurkcu et al 2011][research_kurkcu_erhan_2011]
- [Kurnaz et al][research_kurnaz_cetin]
- [Kushneruk 2026][research_kushneruk_2026]
- [Kwiek and Figat 2016][research_kwiek_figat_2016]
- [Kwon et al 2012][research_kwon_jang_2012]
- [Kwon et al 2013][research_kwon_yoder_2013]
- [L.P and Ghosh 2020][research_lp_ghosh_2020]
- [La Porte et al 1988][research_laporte_roberts_1988]
- [Laananen 1980][research_laananen_1980]
- [Lachaona Jr 2023][research_lachaonajr_2023]
- [Lachapelle et al 1992][research_lachapelle_cannon_1992]
- [Ladd and Xinhua Qin][research_ladd_xinhuaqin]
- [Lahoti et al 2022][research_lahoti_gogulapati_2022]
- [Lai 2007][research_lai_2007]
- [Lai et al 2022][research_lai_tong_2022]
- [Lam and Maull 1993][research_lam_maull_1993]
- [Lambregts and Creedon 1980][research_lambregts_creedon_1980]
- [Lampton et al 2018][research_lampton_gray_2018]
- [Lampton et al 2024][research_lampton_klyde_2024]
- [Landing GEAR - Aircraft][research_landing_gear]
- [Landing Gear Fatigue Spectrum][research_landing_gear_c]
- [Landing Gear Shock Absorption][research_landing_gear_b]
- [Landrum and Tournes 2001][research_landrum_tournes_2001]
- [Lange 1983][research_lange_1983]
- [Lange 1984][research_lange_1984]
- [Lannes 2001][research_lannes_2001]
- [Lanteigne et al 2020][research_lanteigne_mcleod_2020]
- [Larm 2004][research_larm_2004]
- [Larrabee][research_larrabee]
- [Larson 1958][research_larson_1958]
- [Larsson 2025][research_larsson_2025]
- [Lateral-Directional Dynamics 1998][research_lateral_directional_dynamics_1998]
- [Lattimore 1991][research_lattimore_1991]
- [Lau 2016][research_lau_2016]
- [Laufer et al 1997][research_laufer_krauss_1997]
- [Laurichesse et al 2009][research_laurichesse_mercier_2009]
- [Lawrence 2000][research_lawrence_2000]
- [Lawrence 2003][research_lawrence_2003]
- [Lawrence and Mosnier 2009][research_lawrence_mosnier_2009]
- [Lawson 2001][research_lawson_2001]
- [Lawson and Barakos 2010][research_lawson_barakos_2010]
- [Le et al 2014][research_le_he_2014]
- [Le et al 2019][research_le_vesely_2019]
- [Leasure 2002][research_leasure_2002]
- [Lebacqz and Chen 1977][research_lebacqz_chen_1977]
- [Lee][research_lee]
- [Lee 1988][research_lee_1988]
- [Lee 2010][research_lee_2010]
- [Lee 2012][research_lee_2012]
- [Lee 2014][research_lee_2014]
- [Lee and Batina 1991][research_lee_batina_1991]
- [Lee and Chiou 1994][research_lee_chiou_1994]
- [Lee and Kim 2024][research_lee_kim_2024]
- [Lee and O'Laughlin 2000][research_lee_olaughlin_2000]
- [Lee and O'Laughlin 2001][research_lee_olaughlin_2001]
- [Lee and Tahk 2019][research_lee_tahk_2019]
- [Lee et al 1998][research_lee_shim_1998]
- [Lee et al 2005][research_lee_wang_2005]
- [Lee et al 2008][research_lee_soon_2008]
- [Lee et al 2012][research_lee_park_2012]
- [Lee et al 2015][research_lee_kim_2015]
- [Lee et al 2018][research_lee_shim_2018]
- [Lee et al 2026][research_lee_lowe_2026]
- [Lehman 1964][research_lehman_1964]
- [Lehman 1965][research_lehman_1965]
- [Lehman 1966][research_lehman_1966]
- [Lehman and Kaplan 1965][research_lehman_kaplan_1965]
- [Lehovec 1979][research_lehovec_1979]
- [Lehovec 1980][research_lehovec_1980]
- [Lei 2020][research_lei_2020]
- [Leira et al 2017][research_leira_johansen_2017]
- [Leishman et al 2013][research_leishman_mclain_2013]
- [Lejeune et al 2011][research_lejeune_wautelet_2011]
- [Lemmon 2013][research_lemmon_2013]
- [Lemmon 2015][research_lemmon_2015]
- [Leonard et al 2013][research_leonard_savvaris_2013]
- [Leonidov 2021][research_leonidov_2021]
- [Leuchter 2013][research_leuchter_2013]
- [Leva][research_leva]
- [Level Flight Performance Jet 2003][research_level_flight_2003]
- [Levison and Rickard 1981][research_levison_rickard_1981]
- [Lewantowicz][research_lewantowicz]
- [Lewis 2002][research_lewis_2002]
- [Lewis and Pickering 2014][research_lewis_pickering_2014]
- [Li 2008][research_li_2008]
- [Li 2017][research_li_2017]
- [Li 2019][research_li_2019]
- [Li 2020][research_li_2020]
- [Li 2021][research_li_2021]
- [Li and Chen 2003][research_li_chen_2003]
- [Li and Duan 2015][research_li_duan_2015]
- [Li and Fan 2018][research_li_fan_2018]
- [Li and Guo 2013][research_li_guo_2013]
- [Li and Leung 2007][research_li_leung_2007]
- [Li and Maiorova 2022][research_li_maiorova_2022]
- [Li and Qin 2020][research_li_qin_2020]
- [Li and Sun 2013][research_li_sun_2013]
- [Li and Wang 2013][research_li_wang_2013_b]
- [Li and Zhang 2025][research_li_zhang_2025_b]
- [Li et al 2008][research_li_rizos_2008]
- [Li et al 2009][research_li_feng_2009]
- [Li et al 2012][research_li_glennon_2012]
- [Li et al 2012][research_li_zhang_2012]
- [Li et al 2012][research_li_zhu_2012]
- [Li et al 2013][research_li_cao_2013]
- [Li et al 2013][research_li_chen_2013]
- [Li et al 2013][research_li_li_2013]
- [Li et al 2013][research_li_su_2013]
- [Li et al 2013][research_li_verhagen_2013]
- [Li et al 2013][research_li_wang_2013]
- [Li et al 2013][research_li_yang_2013]
- [Li et al 2013][research_li_yuan_2013]
- [Li et al 2013][research_li_zhu_2013]
- [Li et al 2014][research_li_huang_2014]
- [Li et al 2014][research_li_li_2014]
- [Li et al 2014][research_li_li_2014_b]
- [Li et al 2015][research_li_li_2015]
- [Li et al 2016][research_li_gao_2016]
- [Li et al 2016][research_li_wang_2016]
- [Li et al 2017][research_li_qin_2017]
- [Li et al 2017][research_li_yong_2017]
- [Li et al 2018][research_li_yuan_2018]
- [Li et al 2018][research_li_zhang_2018]
- [Li et al 2018][research_li_zhang_2018_b]
- [Li et al 2020][research_li_jiang_2020]
- [Li et al 2020][research_li_liu_2020]
- [Li et al 2020][research_li_weng_2020]
- [Li et al 2021][research_li_gao_2021]
- [Li et al 2022][research_li_fan_2022]
- [Li et al 2022][research_li_li_2022]
- [Li et al 2022][research_li_li_2022_b]
- [Li et al 2022][research_li_xu_2022]
- [Li et al 2023][research_li_feng_2023]
- [Li et al 2024][research_li_tang_2024]
- [Li et al 2024][research_li_yang_2024]
- [Li et al 2024][research_li_zhai_2024]
- [Li et al 2024][research_li_zhai_2024_b]
- [Li et al 2024][research_li_zhang_2024]
- [Li et al 2024][research_li_zhou_2024]
- [Li et al 2024][research_li_zhu_2024]
- [Li et al 2025][research_li_wang_2025]
- [Li et al 2025][research_li_yan_2025]
- [Li et al 2025][research_li_zhang_2025]
- [Li et al 2025][research_li_zheng_2025]
- [Li et al 2026][research_li_han_2026]
- [Li et al 2026][research_li_liu_2026]
- [Li et al 2026][research_li_zhang_2026]
- [Li et al 2026][research_li_zhang_2026_b]
- [Liang et al 2014][research_liang_jia_2014]
- [Liang et al 2020][research_liang_chen_2020]
- [Liang et al 2022][research_liang_li_2022]
- [Liang et al 2024][research_liang_dong_2024]
- [Licheva and Liscouet-Hanke 2023][research_licheva_liscouethanke_2023]
- [Liersch and Bishop 2018][research_liersch_bishop_2018]
- [Liggin et al 2001][research_liggin_crawford_2001]
- [Lighthill 1963][research_lighthill_1963]
- [Lightsey and Crassidis 2004][research_lightsey_crassidis_2004]
- [Lightsey et al 1999][research_lightsey_crassidis_1999]
- [Lijesen et al 2005][research_lijesen_nijkamp_2005]
- [Lima Filho et al 2021][research_limafilho_medeiros_2021]
- [Lin 2002][research_lin_2002]
- [Lin 2015][research_lin_2015]
- [Lin 2023][research_lin_2023]
- [Lin and Da 1994][research_lin_da_1994]
- [Lin and Saripalli 2014][research_lin_saripalli_2014]
- [Lin et al 2015][research_lin_garratt_2015]
- [Lin et al 2015][research_lin_wohleber_2015]
- [Lin et al 2017][research_lin_wang_2017]
- [Lin et al 2019][research_lin_yang_2019]
- [Lin et al 2020][research_lin_meghdadhasheminasab_2020]
- [Lin et al 2026][research_lin_zong_2026]
- [Lindsay and Sun 2020][research_lindsay_sun_2020]
- [Lindsey 1977][research_lindsey_1977]
- [Ling 1970][research_ling_1970]
- [Lingyu et al 2006][research_lingyu_youwu_2006]
- [Linn and Langlois 2006][research_linn_langlois_2006]
- [Linne 2022][research_linne_2022]
- [Linnell 1963][research_linnell_1963]
- [Lintern 1984][research_lintern_1984]
- [Lion 1966][research_lion_1966]
- [Lisauskas et al 2015][research_lisauskas_poska_2015]
- [Liscouet-Hanke and Huynh 2013][research_liscouethanke_huynh_2013]
- [Liseitsev 2025][research_liseitsev_2025]
- [Liu 2006][research_liu_2006]
- [Liu 2018][research_liu_2018]
- [Liu 2024][research_liu_2024]
- [Liu and Bucknall 2018][research_liu_bucknall_2018]
- [Liu and Bush 2004][research_liu_bush_2004]
- [Liu and Cai 2019][research_liu_cai_2019]
- [Liu and Chen 2011][research_liu_chen_2011]
- [Liu and Fan 2025][research_liu_fan_2025]
- [Liu and Valavanis 2026][research_liu_valavanis_2026]
- [Liu and Wang 2025][research_liu_wang_2025]
- [Liu and Wang 2025][research_liu_wang_2025_b]
- [Liu and Wu 2003][research_liu_wu_2003]
- [Liu and Yan 2025][research_liu_yan_2025]
- [Liu and Zhang 2022][research_liu_zhang_2022]
- [Liu et al 2007][research_liu_wang_2007]
- [Liu et al 2014][research_liu_chen_2014]
- [Liu et al 2017][research_liu_fu_2017]
- [Liu et al 2017][research_liu_lou_2017]
- [Liu et al 2017][research_liu_sengupta_2017]
- [Liu et al 2018][research_liu_fan_2018]
- [Liu et al 2018][research_liu_yang_2018]
- [Liu et al 2019][research_liu_he_2019]
- [Liu et al 2020][research_liu_han_2020]
- [Liu et al 2020][research_liu_zheng_2020]
- [Liu et al 2021][research_liu_zheng_2021]
- [Liu et al 2022][research_liu_han_2022]
- [Liu et al 2022][research_liu_liu_2022]
- [Liu et al 2022][research_liu_tan_2022]
- [Liu et al 2023][research_liu_li_2023]
- [Liu et al 2023][research_liu_liu_2023]
- [Liu et al 2023][research_liu_sun_2023]
- [Liu et al 2023][research_liu_wang_2023]
- [Liu et al 2024][research_liu_zhang_2024]
- [Liu et al 2024][research_liu_zhang_2024_b]
- [Liu et al 2024][research_liu_zheng_2024]
- [Liu et al 2025][research_liu_bogu_2025]
- [Liu et al 2025][research_liu_ding_2025]
- [Liu et al 2025][research_liu_huang_2025]
- [Liu et al 2025][research_liu_yuan_2025]
- [Liu et al 2025][research_liu_zhang_2025]
- [Liu et al 2026][research_liu_ai_2026]
- [Liu et al 2026][research_liu_huang_2026]
- [Liu et al 2026][research_liu_zhu_2026]
- [Liu, G. C. et al 1983][research_liugc_morriscekjr_1983]
- [Livne and Mineau 1997][research_livne_mineau_1997]
- [Locatelli et al 2011][research_locatelli_mulani_2011]
- [Location and Actuation of][research_location_and]
- [Location and Actuation of][research_location_and_b]
- [Loechert et al 2018][research_loechert_huber_2018]
- [Loegering and Harris 2002][research_loegering_harris_2002]
- [Logan 1989][research_logan_1989]
- [Loh and Fernow][research_loh_fernow]
- [Londner 2016][research_londner_2016]
- [Longino 1994][research_longino_1994]
- [Lopez 2010][research_lopez_2010]
- [Lopez et al 2021][research_lopez_garcia_2021]
- [Lorenz 2015][research_lorenz_2015]
- [Lorenzetti et al 2020][research_lorenzetti_mcclellan_2020]
- [Loupy et al 2018][research_loupy_barakos_2018]
- [Love and Argrow 2021][research_love_argrow_2021]
- [Love and Kapania 2020][research_love_kapania_2020]
- [Lovett 1984][research_lovett_1984]
- [Low and D'Amico 2024][research_low_damico_2024]
- [Lowe et al 2026][research_lowe_torshizi_2026]
- [Lu 2021][research_lu_2021]
- [Lu 2026][research_lu_2026]
- [Lu and Pierson 1995][research_lu_pierson_1995]
- [Lu and Xu 2024][research_lu_xu_2024]
- [Lu et al 2011][research_lu_jiang_2011]
- [Lu et al 2014][research_lu_tan_2014]
- [Lu et al 2014][research_lu_zhang_2014]
- [Lu et al 2020][research_lu_wang_2020]
- [Lu et al 2022][research_lu_zhu_2022]
- [Lu et al 2024][research_lu_liu_2024]
- [Lu et al 2025][research_lu_yan_2025]
- [Lu Keke et al 2016][research_lukeke_yujinyong_2016]
- [Luan and Sun 2020][research_luan_sun_2020]
- [Lugo and Zell 2013][research_lugo_zell_2013]
- [Lungu 2017][research_lungu_2017]
- [Lungu et al 2022][research_lungu_chen_2022]
- [Lungu et al 2022][research_lungu_flores_2022]
- [Luo and Duan 2014][research_luo_duan_2014]
- [Luo et al 2012][research_luo_babu_2012]
- [Luong et al 2025][research_luong_le_2025]
- [Lusardi 2023][research_lusardi_2023]
- [Luu 2025][research_luu_2025]
- [Luzica and Bloudicek 2016][research_luzica_bloudicek_2016]
- [Lv et al 2011][research_lv_zhu_2011]
- [Lv et al 2026][research_lv_wang_2026]
- [Lykken and Shah 1972][research_lykken_shah_1972]
- [Lynn 1978][research_lynn_1978]
- [Lyu et al 2021][research_lyu_su_2021]
- [Löchert et al 2019][research_lochert_huber_2019]
- [Ma][research_ma]
- [Ma 1989][research_ma_1989]
- [Ma and Wang 2009][research_ma_wang_2009]
- [Ma et al 2018][research_ma_guan_2018]
- [Ma et al 2022][research_ma_lou_2022]
- [Ma et al 2022][research_ma_yan_2022]
- [MacDORAN et al 1984][research_macdoran_miller_1984]
- [MacGarvey 2014][research_macgarvey_2014]
- [Macias-Valadez et al 2011][research_maciasvaladez_santerre_2011]
- [MacKunis et al 2008][research_mackunis_kaiser_2008]
- [Macnae 1995][research_macnae_1995]
- [Macone 1996][research_macone_1996]
- [Mader 2001][research_mader_2001]
- [Mader and Martins 2010][research_mader_martins_2010]
- [Madonna et al 2010][research_madonna_viola_2010]
- [Madyastha et al 2011][research_madyastha_ravindra_2011]
- [Maeda et al 1998][research_maeda_itsukaichi_1998]
- [Mah and O'Keefe 2025][research_mah_okeefe_2025]
- [Mahantesh Katagi et al 2015][research_mahanteshkatagi_manishkumarsingh_2015]
- [Mahmud et al 2016][research_mahmud_qaisar_2016]
- [Maier et al 2011][research_maier_kiesel_2011]
- [Maimako et al 2026][research_maimako_mintah_2026]
- [Majoros 1989][research_majoros_1989]
- [Makarenko and Tokarev 2023][research_makarenko_tokarev_2023]
- [Makarenko et al 2017][research_makarenko_makarov_2017]
- [Maksimova 2025][research_maksimova_2025]
- [Malaek and Soltan-Mohammed 2001][research_malaek_soltanmohammed_2001]
- [Malleswaran et al 2011][research_malleswaran_vaidehi_2011]
- [Malone and Mason 1992][research_malone_mason_1992]
- [Mammadov and Gueaieb 2014][research_mammadov_gueaieb_2014]
- [Mann 1963][research_mann_1963]
- [Manned General Aviation Helicopters 2026][research_manned_general_2026]
- [Manokaran et al 2009][research_manokaran_vidya_2009]
- [Manon 1981][research_manon_1981]
- [Mansor et al 2019][research_mansor_sahwee_2019]
- [Maraman 1987][research_maraman_1987]
- [Marchese 1963][research_marchese_1963]
- [Marchman, Iii et al 1983][research_marchmaniii_donatelli_1983]
- [Mardanpour and Hodges 2013][research_mardanpour_hodges_2013]
- [Mardanpour and Hodges 2014][research_mardanpour_hodges_2014]
- [Mare 2006][research_mare_2006]
- [Marie Vianney et al 2018][research_marievianney_li_2018]
- [Marino 2001][research_marino_2001]
- [Marinov and Penev 2025][research_marinov_penev_2025]
- [Mark and Dehart 1976][research_mark_dehart_1976]
- [Marker 2009][research_marker_2009]
- [Marques Filho et al 2016][research_marquesfilho_riosneto_2016]
- [Marquis 2003][research_marquis_2003]
- [Marretta et al 1999][research_marretta_davi_1999]
- [Marshall 2011][research_marshall_2011]
- [Marshall 2016][research_marshall_2016]
- [Martin 1963][research_martin_1963]
- [Martin and Irani 2022][research_martin_irani_2022]
- [Martin and McMahon 2017][research_martin_mcmahon_2017]
- [Martin et al 2010][research_martin_travis_2010]
- [Martindale et al 1974][research_martindale_rockwell_1974]
- [Martinez 2022][research_martinez_2022]
- [Martinez et al 2013][research_martinez_richardson_2013]
- [Martinez-Val et al 1994][research_martinezval_perez_1994]
- [Martone 1983][research_martone_1983]
- [Martone and Hawkins 1983][research_martone_hawkins_1983]
- [Martorella et al 1981][research_martorella_kelly_1981]
- [Marwaha et al 2009][research_marwaha_valasek_2009]
- [Marx et al 1995][research_marx_mavris_1995]
- [Maskell][research_maskell]
- [Mason 1990][research_mason_1990]
- [Mason and Iglesias 2001][research_mason_iglesias_2001]
- [Massarweh and Teunissen 2025][research_massarweh_teunissen_2025]
- [Masud and Khan 2015][research_masud_khan_2015]
- [Matamoros and de Visser 2018][research_matamoros_devisser_2018]
- [Mathematical model of the 2023][research_mathematical_model_2023]
- [Mathias et al 1995][research_mathias_ross_1995]
- [Mathy Franz-Josef 2012][research_mathyfranzjosef_2012]
- [Matson et al 2011][research_matson_licht_2011]
- [Matsuno and Andreeva-Mori 2023][research_matsuno_andreevamori_2023]
- [Matsushima 2001][research_matsushima_2001]
- [Matsushita et al][research_matsushita_miyata]
- [Maurer 1982][research_maurer_1982]
- [Maurer 1987][research_maurer_1987]
- [Maute and Reich 2006][research_maute_reich_2006]
- [Maybourn 1983][research_maybourn_1983]
- [Mayer 2000][research_mayer_2000]
- [Mayfield et al 2001][research_mayfield_baker_2001]
- [Mazzitelli 1966][research_mazzitelli_1966]
- [Mazzitelli 1967][research_mazzitelli_1967]
- [McAllister and Parish 2009][research_mcallister_parish_2009]
- [McBreen et al 2023][research_mcbreen_boling_2023]
- [McBurney][research_mcburney]
- [McCarthy and Chattopadhyay 1996][research_mccarthy_chattopadhyay_1996]
- [McCormick 1969][research_mccormick_1969]
- [McCullough and Dieckmann 1981][research_mccullough_dieckmann_1981]
- [McDermott 2004][research_mcdermott_2004]
- [McDevitt 2005][research_mcdevitt_2005]
- [Mcdonald 1980][research_mcdonald_1980]
- [McDonald et al 2020][research_mcdonald_richards_2020]
- [Mcdonnell Aircraft Corp St Louis Mo 1950][research_mcdonnellaircraftcorpstlouismo_1950]
- [Mcdonnell Aircraft Corp St Louis Mo 1963][research_mcdonnellaircraftcorpstlouismo_1963]
- [McElreath 1972][research_mcelreath_1972]
- [McFadyen and Martin 2016][research_mcfadyen_martin_2016]
- [McFadyen and Martin 2016][research_mcfadyen_martin_2016_b]
- [McFadyen et al 2018][research_mcfadyen_martin_2018]
- [McFarland][research_mcfarland]
- [McFARLAND 1991][research_mcfarland_1991]
- [McGahern 2000][research_mcgahern_2000]
- [McGarey and Saripalli 2013][research_mcgarey_saripalli_2013]
- [Mcgee 1977][research_mcgee_1977]
- [McGrath 2000][research_mcgrath_2000]
- [Mcgregor and Smith 1965][research_mcgregor_smith_1965]
- [Mcingvale and Dudley 1990][research_mcingvale_dudley_1990]
- [McKendrick et al 2013][research_mckendrick_shaw_2013]
- [McKinnis et al 2021][research_mckinnis_hauptman_2021]
- [McLaughlin and Perhinschi 2023][research_mclaughlin_perhinschi_2023]
- [McLeod 2025][research_mcleod_2025]
- [McLeod 2025][research_mcleod_2025_b]
- [McLeod 2025][research_mcleod_2025_c]
- [McLeod 2025][research_mcleod_2025_d]
- [McManus and Walker 2006][research_mcmanus_walker_2006]
- [McMillin and Wood 1987][research_mcmillin_wood_1987]
- [McMuldroch et al 1979][research_mcmuldroch_stein_1979]
- [Mcnally et al 1992][research_mcnally_warner_1992]
- [McRoberts et al 2015][research_mcroberts_early_2015]
- [Medina et al 2021][research_medina_patel_2021]
- [Mehta et al 2006][research_mehta_kaiser_2006]
- [Mei 2025][research_mei_2025]
- [Mejdrich 1977][research_mejdrich_1977]
- [Mejias 2014][research_mejias_2014]
- [Mekdeci and Cummings 2009][research_mekdeci_cummings_2009]
- [Meng 2013][research_meng_2013]
- [Meng and Li 2014][research_meng_li_2014]
- [Meng et al 2019][research_meng_wang_2019]
- [Meng et al 2023][research_meng_sun_2023]
- [Mengali and Pieracci 2000][research_mengali_pieracci_2000]
- [Mengying et al 2017][research_mengying_hua_2017]
- [Menner and Lavretsky 2026][research_menner_lavretsky_2026]
- [Menon and Walker 1984][research_menon_walker_1984]
- [Menon and Walker 1985][research_menon_walker_1985]
- [Mercado-Ravell][research_mercadoravell]
- [Merkel and Whitmoyer 1976][research_merkel_whitmoyer_1976]
- [Mertzlufft et al 2022][research_mertzlufft_carvajal_2022]
- [Methodology to Aircraft Design 2010][research_methodology_to_2010]
- [Metin et al 2023][research_metin_uzuner_2023]
- [Meyer 2013][research_meyer_2013]
- [Meyer 2015][research_meyer_2015]
- [Meyn, Larry A. et al 1993][research_meynlarrya_zellpetert_1993]
- [Mi et al 2022][research_mi_zhang_2022]
- [Michalson 1995][research_michalson_1995]
- [Michaud and Santerre 2001][research_michaud_santerre_2001]
- [Michini and How 2011][research_michini_how_2011]
- [Micklos 1991][research_micklos_1991]
- [Microwave Landing System MLS][research_microwave_landing]
- [Middleton 1979][research_middleton_1979]
- [Middleton 1980][research_middleton_1980]
- [Middleton and Thalmann 1981][research_middleton_thalmann_1981]
- [Mikhailov and Mikhailov 2010][research_mikhailov_mikhailov_2010]
- [Milano et al 2022][research_milano_primatesta_2022]
- [Milbert 2005][research_milbert_2005]
- [Milbert 2005][research_milbert_2005_b]
- [Miles 1990][research_miles_1990]
- [Miles and Lepping 1962][research_miles_lepping_1962]
- [Miller 1968][research_miller_1968]
- [Miller 1969][research_miller_1969]
- [Miller 1970][research_miller_1970]
- [Miller 2006][research_miller_2006]
- [Miller 2013][research_miller_2013]
- [Miller and Burkhalter 1987][research_miller_burkhalter_1987]
- [Miller and Eagan 1997][research_miller_eagan_1997]
- [Miller et al 2023][research_miller_mwaffo_2023]
- [Milner et al 2011][research_milner_ochieng_2011]
- [Min Tint 2018][research_mintint_2018]
- [Mine roof bolting machine 2010][research_mine_roof_2010]
- [Mingfeng Zhang and Liu 2012][research_mingfengzhang_liu_2012]
- [Mingfeng Zhang and Liu 2013][research_mingfengzhang_liu_2013]
- [Minglang et al 2018][research_minglang_haiwen_2018]
- [Miniature Unmanned Air Vehicle][research_miniature_unmanned]
- [Miniature Unmanned Air Vehicle 2008][research_miniature_unmanned_2008]
- [Miquel et al 2006][research_miquel_moracamino_2006]
- [Mirabile][research_mirabile]
- [Mirosavljević 2023][research_mirosavljevic_2023]
- [Mirot 2013][research_mirot_2013]
- [Mirzaei et al 2008][research_mirzaei_abdollahi_2008]
- [Mirzayev et al 2025][research_mirzayev_ahmadova_2025]
- [Mishra et al 2022][research_mishra_ullah_2022]
- [Misovec et al][research_misovec_inanc]
- [Misra and Bai 2018][research_misra_bai_2018]
- [Misra and Bai 2019][research_misra_bai_2019]
- [Misra et al 1993][research_misra_bayliss_1993]
- [Mistree 1987][research_mistree_1987]
- [Mitcham, Grady L et al 1956][research_mitchamgradyl_stevensjosephe_1956]
- [Mitchell and Hoh 1983][research_mitchell_hoh_1983]
- [Moafipoor et al 2012][research_moafipoor_grejnerbrzezinska_2012]
- [Moafipoor et al 2018][research_moafipoor_bock_2018]
- [Modeling the Aircraft 2015][research_modeling_the_2015]
- [Moeller and Rediniotis 2002][research_moeller_rediniotis_2002]
- [Moen and Williams 1966][research_moen_williams_1966]
- [Mohamed et al 2013][research_mohamed_aljaroodi_2013]
- [Mohiuddin and Psiaki 2005][research_mohiuddin_psiaki_2005]
- [Mohiuddin and Psiaki 2006][research_mohiuddin_psiaki_2006]
- [Mokotoff et al 2025][research_mokotoff_arnson_2025]
- [Mokotoff et al 2026][research_mokotoff_arnson_2026]
- [Montalvo and Costello 2015][research_montalvo_costello_2015]
- [Montenbruck and D'Amico 2012][research_montenbruck_damico_2012]
- [Montenbruck et al 2002][research_montenbruck_ebinuma_2002]
- [Montenbruck et al 2011][research_montenbruck_wermuth_2011]
- [Montenbruck et al 2012][research_montenbruck_swatschina_2012]
- [Montenbruck et al 2017][research_montenbruck_hackel_2017]
- [Montes et al 2022][research_montes_mitchell_2022]
- [Mooij 1985][research_mooij_1985]
- [Mooij 1985][research_mooij_1985_b]
- [Mooij 1985][research_mooij_1985_c]
- [Mooij 1985][research_mooij_1985_d]
- [Mook and Shyu 1990][research_mook_shyu_1990]
- [Mook and Shyu 1992][research_mook_shyu_1992]
- [Mook et al 1990][research_mook_swanson_1990]
- [Moon-Beom Heo and Pervan 2006][research_moonbeomheo_pervan_2006]
- [Moore 2000][research_moore_2000]
- [Moore 2013][research_moore_2013]
- [Moorhouse 1991][research_moorhouse_1991]
- [Morley 1961][research_morley_1961]
- [Morley 2013][research_morley_2013]
- [Morote and Liaño 2012][research_morote_liano_2012]
- [Morozov 2015][research_morozov_2015]
- [Morris and Tigner 1995][research_morris_tigner_1995]
- [Morris et al 2005][research_morris_frew_2005]
- [Morris, C. E. K., Jr. 1983][research_morriscekjr_1983]
- [Morris, C. E. K., Jr. 1984][research_morriscekjr_1984]
- [Morrison et al][research_morrison_zahraee]
- [Morton 1956][research_morton_1956]
- [Morujão and Mendes 2008][research_morujao_mendes_2008]
- [Mosavi and Shafiee 2015][research_mosavi_shafiee_2015]
- [Moser 2011][research_moser_2011]
- [Mostafa and Schnell 2016][research_mostafa_schnell_2016]
- [Moum 2010][research_moum_2010]
- [Mueller 2018][research_mueller_2018]
- [Mueller and Krozel 2000][research_mueller_krozel_2000]
- [Mujica 1987][research_mujica_1987]
- [Mukherjee 2015][research_mukherjee_2015]
- [Mulero-Pázmány et al 2014][research_muleropazmany_negro_2014]
- [Muller 2001][research_muller_2001]
- [Mullins, Jr. et al 1996][research_mullinsjr_tipton_1996]
- [Multi-finger Dynamic Position Tracking 2025][research_multi_finger_dynamic_2025]
- [Muniraj and Farhood 2017][research_muniraj_farhood_2017]
- [Munroe 1978][research_munroe_1978]
- [Murakami and Peck 2011][research_murakami_peck_2011]
- [Muralikrishna et al 2022][research_muralikrishna_mallesham_2022]
- [Murillo et al 2025][research_murillo_montes_2025]
- [Murray 1949][research_murray_1949]
- [Murray et al 2022][research_murray_richardson_2022]
- [Murray-Smith 1995][research_murraysmith_1995]
- [Musolino et al 2012][research_musolino_rizzo_2012]
- [Mustopa 2022][research_mustopa_2022]
- [Mutz et al 1964][research_mutz_pierce_1964]
- [Myers 1973][research_myers_1973]
- [Myers 1974][research_myers_1974]
- [Myklebust and Gelhausen 1993][research_myklebust_gelhausen_1993]
- [Müller and Bauer 2024][research_muller_bauer_2024]
- [Nadler 2015][research_nadler_2015]
- [Naghash and Enns 1998][research_naghash_enns_1998]
- [Naik and Ostowari 1990][research_naik_ostowari_1990]
- [Nam][research_nam]
- [Nam and Mavris 2018][research_nam_mavris_2018]
- [Nam et al 2026][research_nam_min_2026]
- [Nan et al 2024][research_nan_yang_2024]
- [Nangia and Palmer 2007][research_nangia_palmer_2007]
- [Nangia and Palmer 2007][research_nangia_palmer_2007_b]
- [Napier 1989][research_napier_1989]
- [Nastasi et al 1983][research_nastasi_martorella_1983]
- [Natalie and Jacob 2019][research_natalie_jacob_2019]
- [Natesan and Bhat 2005][research_natesan_bhat_2005]
- [Natesan et al 2008][research_natesan_gu_2008]
- [Nath 2025][research_nath_2025]
- [National Research Council Washington Dc 2001][research_nationalresearchcouncilwashingtondc_2001]
- [Naundrup][research_naundrup]
- [Naval Air Development Center Warminsterpa 1975][research_navalairdevelopmentcenterwarminsterpa_1975]
- [Naval Air Systems Command Patuxent River Md 2013][research_navalairsystemscommandpatuxentrivermd_2013]
- [Naval Air Systems Command Washington Dc 1978][research_navalairsystemscommandwashingtondc_1978]
- [Naval Air Systems Command Washington Dc 1980][research_navalairsystemscommandwashingtondc_1980]
- [Naval Applied Science Lab Brooklyn Ny 1963][research_navalappliedsciencelabbrooklynny_1963]
- [Naval Aviation Enterprise Patuxent River Md 2012][research_navalaviationenterprisepatuxentrivermd_2012]
- [Naval Postgraduate School Monterey Ca 1981][research_navalpostgraduateschoolmontereyca_1981]
- [Nave 1973][research_nave_1973]
- [Nayerabadi and Mohammadi 2022][research_nayerabadi_mohammadi_2022]
- [Neal 2010][research_neal_2010]
- [Nebiker 1981][research_nebiker_1981]
- [Nebula 2018][research_nebula_2018]
- [Nedresky 1996][research_nedresky_1996]
- [Neff 2019][research_neff_2019]
- [Negaard 1980][research_negaard_1980]
- [Negast and Paschall][research_negast_paschall]
- [Negre 1975][research_negre_1975]
- [Nelson 1974][research_nelson_1974]
- [Nelson and Bolia 2006][research_nelson_bolia_2006]
- [Nelson and Dix 2003][research_nelson_dix_2003]
- [Nelson et al 2006][research_nelson_calhoun_2006]
- [Nengjian Wang et al 2016][research_nengjianwang_xiangleimeng_2016]
- [Neto et al 2024][research_neto_douradovilla_2024]
- [Nettleton 1965][research_nettleton_1965]
- [Neuenswander 2013][research_neuenswander_2013]
- [Neufeld 2021][research_neufeld_2021]
- [Neusypin et al 2023][research_neusypin_kupriyanov_2023]
- [New Achievements in Unmanned 2023][research_new_achievements_2023]
- [New aircraft carrier expands 2019][research_new_aircraft_2019]
- [New Method for Station 2005][research_new_method_2005]
- [New steam catapult for 1952][research_new_steam_1952]
- [Newberry 1998][research_newberry_1998]
- [Newcome 2004][research_newcome_2004]
- [Newcome 2009][research_newcome_2009]
- [Newman and Stanzione 1991][research_newman_stanzione_1991]
- [Ngo and Sultan 2024][research_ngo_sultan_2024]
- [Nguyen 2019][research_nguyen_2019]
- [Nguyen et al 2009][research_nguyen_choi_2009]
- [Nguyen et al 2013][research_nguyen_choi_2013]
- [Nguyen et al 2024][research_nguyen_crismer_2024]
- [Ni and Zhang 2026][research_ni_zhang_2026]
- [Ni et al 2018][research_ni_hu_2018]
- [Ni et al 2018][research_ni_hu_2018_b]
- [Nichols 1998][research_nichols_1998]
- [Nichols 2021][research_nichols_2021]
- [Nichols and Westmoreland 2007][research_nichols_westmoreland_2007]
- [Nickol 2011][research_nickol_2011]
- [Nickol, Craig L. et al 2007][research_nickolcraigl_guynnmarkd_2007]
- [Nicosia et al][research_nicosia_loss]
- [Nida and O'Connor 2006][research_nida_oconnor_2006]
- [Nielsen 1997][research_nielsen_1997]
- [Niendorf et al 2012][research_niendorf_adolf_2012]
- [Nieuwenhuisen et al 2014][research_nieuwenhuisen_droeschel_2014]
- [Niewoehner and Filbey 2005][research_niewoehner_filbey_2005]
- [Nigam and Kroo 2008][research_nigam_kroo_2008]
- [Nigam et al 2015][research_nigam_ayyalasomayajula_2015]
- [Nijveldt and Ijtsma 2022][research_nijveldt_ijtsma_2022]
- [Nikiforov 1995][research_nikiforov_1995]
- [Nikolaidis et al 2025][research_nikolaidis_laoudias_2025]
- [Nikolic 2007][research_nikolic_2007]
- [Nikolic et al 1996][research_nikolic_jumper_1996]
- [Niles 1964][research_niles_1964]
- [Ning Luo and Lachapelle 2003][research_ningluo_lachapelle_2003]
- [Noble and Bhandari 2017][research_noble_bhandari_2017]
- [Noe and Zabaneh][research_noe_zabaneh]
- [Noise measurements for UAS][research_noise_measurements]
- [Nominal aircraft dynamics][research_nominal_aircraft]
- [Noro and Inamori 2020][research_noro_inamori_2020]
- [Norris 1998][research_norris_1998]
- [Norris and Bauer 1993][research_norris_bauer_1993]
- [Northrop Aircraft Inc Hawthorne Ca 1952][research_northropaircraftinchawthorneca_1952]
- [Northrop Aircraft Inc Hawthorne Ca 1953][research_northropaircraftinchawthorneca_1953]
- [Norton and Dyme 1952][research_norton_dyme_1952]
- [Norwood and Chichester 2015][research_norwood_chichester_2015]
- [Noureldin et al 2012][research_noureldin_karamat_2012]
- [Novakovic et al 2016][research_novakovic_vasic_2016]
- [Nowak et al 2022][research_nowak_kopecki_2022]
- [Nowel et al 2018][research_nowel_cellmer_2018]
- [Nugent and Girard 2003][research_nugent_girard_2003]
- [Nugroho 2026][research_nugroho_2026]
- [null][research_null]
- [Numerical Methods and Experimental 2026][research_numerical_methods_2026]
- [Nygard 1995][research_nygard_1995]
- [O'Keefe 2008][research_okeefe_2008]
- [O'Keefe et al 2006][research_okeefe_julien_2006]
- [O.V. Milenin 2019][research_ovmilenin_2019]
- [Obayashi et al 1997][research_obayashi_yamaguchi_1997]
- [Oblique Wing Aircraft 2020][research_oblique_wing_2020]
- [Obradovic and Subbarao 2010][research_obradovic_subbarao_2010]
- [Obradovic and Subbarao 2011][research_obradovic_subbarao_2011]
- [Obye and Hakim 1984][research_obye_hakim_1984]
- [Odijk and Teunissen 2002][research_odijk_teunissen_2002]
- [Odijk and Teunissen 2011][research_odijk_teunissen_2011]
- [Odijk et al 2012][research_odijk_teunissen_2012]
- [Odolinski and Teunissen 2017][research_odolinski_teunissen_2017]
- [Office Of Naval Research Arlington Va 1993][research_officeofnavalresearcharlingtonva_1993]
- [Ogorzalek et al 2019][research_ogorzalek_doyle_2019]
- [Oh and Johnson 2007][research_oh_johnson_2007]
- [Oh et al 2016][research_oh_park_2016]
- [Oh et al 2017][research_oh_kim_2017]
- [Ohio State Univ Columbus Electroscience Lab 1968][research_ohiostateunivcolumbuselectrosciencelab_1968]
- [Ojha et al 2009][research_ojha_chow_2009]
- [Okcu 2016][research_okcu_2016]
- [Oktay and Eraslan 2024][research_oktay_eraslan_2024]
- [Olds 1998][research_olds_1998]
- [Olejnik et al 2019][research_olejnik_rogolski_2019]
- [Olivares Méndez][research_olivaresmendez]
- [Oliver 1962][research_oliver_1962]
- [Oliver 2012][research_oliver_2012]
- [Olsen et al 1999][research_olsen_park_1999]
- [Olson 2005][research_olson_2005]
- [Olson and Henricks 2018][research_olson_henricks_2018]
- [Olson et al 2020][research_olson_toombs_2020]
- [Omar et al 2016][research_omar_yanzhong_2016]
- [Onat and Tolle 1979][research_onat_tolle_1979]
- [Oncu and Yildiz 2014][research_oncu_yildiz_2014]
- [Ono 2024][research_ono_2024]
- [Oole 1993][research_oole_1993]
- [Oosterom and Babuska 2001][research_oosterom_babuska_2001]
- [Opening up civil airspace 2007][research_opening_up_2007]
- [Optimal Control System of 2018][research_optimal_control_2018]
- [Options for Reducing Costs 2005][research_options_for_2005]
- [Ordaz et al 2004][research_ordaz_lee_2004]
- [Ordoukhanian and Madni 2019][research_ordoukhanian_madni_2019]
- [Oren and Kocyigit 2016][research_oren_kocyigit_2016]
- [Orhan 2020][research_orhan_2020]
- [Orhan and Subbarao 2021][research_orhan_subbarao_2021]
- [Orozco et al 2026][research_orozco_walsh_2026]
- [Ortiz 2008][research_ortiz_2008]
- [Osadchiy et al 2013][research_osadchiy_kalich_2013]
- [Oshin Mittal et al 2024][research_oshinmittal_alokkumarsahu_2024]
- [Osiecki et al 2023][research_osiecki_fortonska_2023]
- [Ossmann et al 2019][research_ossmann_luspay_2019]
- [Osterman 2010][research_osterman_2010]
- [OU-validated Foundation Degree Programme 2008][research_ou_validated_foundation_2008]
- [Overholt 2007][research_overholt_2007]
- [Overview of Aircraft Landing][research_overview_of]
- [Overview of Unmanned Aircraft 2012][research_overview_of_2012]
- [Overview of Unmanned Aircraft 2014][research_overview_of_2014]
- [Owais et al 2022][research_owais_midtiby_2022]
- [Owashi et al 2017][research_owashi_tanaka_2017]
- [Owens et al 2021][research_owens_macdonald_2021]
- [Oyama 2021][research_oyama_2021]
- [Ozartan et al 2013][research_ozartan_akgul_2013]
- [Ozcan and Alemdaroglu 2015][research_ozcan_alemdaroglu_2015]
- [Ozoroski et al 2003][research_ozoroski_mas_2003]
- [Oztekin et al 2011][research_oztekin_flass_2011]
- [Pack and York 2008][research_pack_york_2008]
- [Pack et al][research_pack_york]
- [Pack et al][research_pack_york_b]
- [Paget et al 2004][research_paget_atherton_2004]
- [Palaia et al 2025][research_palaia_salem_2025]
- [Palmer 1970][research_palmer_1970]
- [Palmisano and Gillam 2005][research_palmisano_gillam_2005]
- [Palomino and Epp 2012][research_palomino_epp_2012]
- [Pan and Huang 2019][research_pan_huang_2019]
- [Pan and Pi 2024][research_pan_pi_2024]
- [Pan et al 2025][research_pan_ma_2025]
- [Panchal et al 2024][research_panchal_hein_2024]
- [Panday and Pedro 2018][research_panday_pedro_2018]
- [Pandey et al 2024][research_pandey_kumari_2024]
- [Panickar et al 2013][research_panickar_murray_2013]
- [Pant and Fielding 1999][research_pant_fielding_1999]
- [Papa 2023][research_papa_2023]
- [Papa et al 2026][research_papa_ariante_2026]
- [Papageorgiou et al 2018][research_papageorgiou_tarkian_2018]
- [Papageorgiou et al 2019][research_papageorgiou_dalkilic_2019]
- [Paranjape and Chung 2010][research_paranjape_chung_2010]
- [Parasuraman and Miller 2006][research_parasuraman_miller_2006]
- [Parasuraman et al 2013][research_parasuraman_kidwell_2013]
- [Parenteau et al 2018][research_parenteau_laurendeau_2018]
- [Park 2025][research_park_2025]
- [Park and Bang 2022][research_park_bang_2022]
- [Park et al 2025][research_park_jeong_2025]
- [Parker 1980][research_parker_1980]
- [Parker 1986][research_parker_1986]
- [Parkinson and Axelrad 1988][research_parkinson_axelrad_1988]
- [Parkinson et al 1970][research_parkinson_bauman_1970]
- [Parsons 1989][research_parsons_1989]
- [Parsons Engineering Sciences Inc Pasadena Ca 1991][research_parsonsengineeringsciencesincpasadenaca_1991]
- [Particle Filter Performance for 2008][research_particle_filter_2008]
- [Parts 1979][research_parts_1979]
- [Passenger SEAT Design Commercial][research_passenger_seat]
- [Passner et al 2012][research_passner_kirby_2012]
- [Patel et al 2011][research_patel_brinton_2011]
- [Patel et al 2021][research_patel_krishnamurthy_2021]
- [Paterson 1999][research_paterson_1999]
- [Paterson and Paterson 1997][research_paterson_paterson_1997]
- [Pathak 1976][research_pathak_1976]
- [Patterson 1989][research_patterson_1989]
- [Patterson et al 1991][research_patterson_champion_1991]
- [Paul][research_paul]
- [Paul et al 2013][research_paul_fendley_2013]
- [Pauls 2012][research_pauls_2012]
- [Paulsen 1998][research_paulsen_1998]
- [Pavkovic et al 2020][research_pavkovic_krznar_2020]
- [Payton 2011][research_payton_2011]
- [Pedro et al 2013][research_pedro_panday_2013]
- [Pedrozo 2022][research_pedrozo_2022]
- [Peer 2000][research_peer_2000]
- [Pehlivan et al 2023][research_pehlivan_ozen_2023]
- [Pei and Xia 2018][research_pei_xia_2018]
- [Pei et al 2025][research_pei_huang_2025]
- [Peixoto 2024][research_peixoto_2024]
- [Peng 2021][research_peng_2021]
- [Peng and Mohseni 2014][research_peng_mohseni_2014]
- [Peng et al 2007][research_peng_li_2007]
- [Peng et al 2014][research_peng_wang_2014]
- [Peng et al 2016][research_peng_lin_2016]
- [Peng et al 2020][research_peng_xie_2020]
- [Peng et al 2025][research_peng_kaiqi_2025]
- [Peng et al 2025][research_peng_li_2025]
- [Pentz and Tang 2019][research_pentz_tang_2019]
- [Pereira and Sanguino 2016][research_pereira_sanguino_2016]
- [Performance Evaluation of the 2023][research_performance_evaluation_of_2023]
- [Performance Investigation of GPS/INS 2006][research_performance_investigation_2006]
- [Performance Investigation of the 2007][research_performance_investigation_2007]
- [Perkins 1991][research_perkins_1991]
- [Perry 2000][research_perry_2000]
- [Perry 2011][research_perry_2011]
- [Perry and Schneider 1984][research_perry_schneider_1984]
- [Pervan and Parkinson 1997][research_pervan_parkinson_1997]
- [Pervan et al 1994][research_pervan_cohen_1994]
- [Pervan et al 1998][research_pervan_pullen_1998]
- [Pervan et al 2003][research_pervan_chan_2003]
- [Peters et al 1997][research_peters_andrisaniii_1997]
- [Peterson and Finkenstadt 2011][research_peterson_finkenstadt_2011]
- [Peterson and Staley 2011][research_peterson_staley_2011]
- [Peterson and Taboada 2012][research_peterson_taboada_2012]
- [Peterson et al 1963][research_peterson_gipe_1963]
- [Petit et al 2015][research_petit_kanj_2015]
- [Petnga and Xu 2016][research_petnga_xu_2016]
- [Petrock and Huizenga 2006][research_petrock_huizenga_2006]
- [Pettigrew 2003][research_pettigrew_2003]
- [Pettit and Grandhi 2003][research_pettit_grandhi_2003]
- [Pham][research_pham]
- [Pham][research_pham_b]
- [Pham][research_pham_c]
- [Pham and Sim 2002][research_pham_sim_2002]
- [Phan and Park 2018][research_phan_park_2018]
- [Phillips and Herr 2020][research_phillips_herr_2020]
- [Phillips and Hunsaker 2019][research_phillips_hunsaker_2019]
- [Phillips et al 2019][research_phillips_hunsaker_2019_b]
- [Photometric characteristics of U.S 1968][research_photometric_characteristics_1968]
- [Pieniążek 2003][research_pieniazek_2003]
- [Piersol 1977][research_piersol_1977]
- [Pierson 1985][research_pierson_1985]
- [Pilot Training Recommendations for][research_pilot_training]
- [Pilot Versatility From the][research_pilot_versatility]
- [Pilot Visibility from the][research_pilot_visibility]
- [Pilot Visibility from the][research_pilot_visibility_b]
- [Pisani 1977][research_pisani_1977]
- [Pittsburgh Univ Washington Dc Research Staff 1966][research_pittsburghunivwashingtondcresearchstaff_1966]
- [Planform Parameterization 2014][research_planform_parameterization_2014]
- [Podhradsky et al 2013][research_podhradsky_bone_2013]
- [Pollack 2013][research_pollack_2013]
- [Pomarolli 1965][research_pomarolli_1965]
- [Pomranky 2006][research_pomranky_2006]
- [Pond 1973][research_pond_1973]
- [Poock 1976][research_poock_1976]
- [Poritzky 1970][research_poritzky_1970]
- [Poritzky 1971][research_poritzky_1971]
- [Portage Inc Idaho Falls Id 2013][research_portageincidahofallsid_2013]
- [Porter 1979][research_porter_1979]
- [Potes et al 2026][research_potes_retamal_2026]
- [Pottinger et al 2017][research_pottinger_cross_2017]
- [Powers et al 2015][research_powers_mclaughlin_2015]
- [Powers et al 2018][research_powers_mclaughlin_2018]
- [Pozzi et al 2012][research_pozzi_guo_2012]
- [Prabha and Raghavendra 2021][research_prabha_raghavendra_2021]
- [Practice for Application of][research_practice_for_d]
- [Practice for Commercial Unmanned][research_practice_for]
- [Practice for Independent Audit][research_practice_for_b]
- [Practice for Production Approval][research_practice_for_c]
- [Practices for Unmanned Aircraft][research_practices_for]
- [Pradeep 1998][research_pradeep_1998]
- [Pradeep and Wei 2018][research_pradeep_wei_2018]
- [Prakash 2020][research_prakash_2020]
- [Prasad et al 2018][research_prasad_comandur_2018]
- [Pratt and Whitney 2009][research_pratt_and_2009]
- [Precision Approach Radar to 1979][research_precision_approach_1979]
- [Precision Landing of Aircraft 1996][research_precision_landing_1996]
- [Preliminary Aerodynamic and Stability 2017][research_preliminary_aerodynamic_2017]
- [Preliminary Estimate of Takeoff 2010][research_preliminary_estimate_2010]
- [Preliminary Fuselage Sizing and 2010][research_preliminary_fuselage_2010]
- [Preliminary Sizing of the 2010][research_preliminary_sizing_2010]
- [Pressure Die Cast Aircraft][research_pressure_die]
- [Priambodo et al 2022][research_priambodo_arifin_2022]
- [Price and Forrest 2016][research_price_forrest_2016]
- [Prickett and Parkes][research_prickett_parkes]
- [Primatesta 2025][research_primatesta_2025]
- [Primatesta et al 2018][research_primatesta_guglieri_2018]
- [Primatesta et al 2021][research_primatesta_pagliano_2021]
- [Pritpal 2005][research_pritpal_2005]
- [Pritulo et al 1995][research_pritulo_gubanov_1995]
- [Probst 2010][research_probst_2010]
- [Progri and Michalson][research_progri_michalson]
- [Propulsion 2017][research_propulsion_2017]
- [Propulsion 2024][research_propulsion_2024]
- [Propulsion Data 2010][research_propulsion_data_2010]
- [Propulsion System Thrust Sizing 2010][research_propulsion_system_2010]
- [Prudhomme 1995][research_prudhomme_1995]
- [Psiaki and Mohiuddin 2005][research_psiaki_mohiuddin_2005]
- [Psiaki and Mohiuddin 2007][research_psiaki_mohiuddin_2007]
- [Pugazhenthi et al 2018][research_pugazhenthi_gopalakannan_2018]
- [Pullen and Joerger 2020][research_pullen_joerger_2020]
- [Pullen et al][research_pullen_enge]
- [Pullen et al][research_pullen_pervan]
- [Purdy 2010][research_purdy_2010]
- [Purivigraipong et al 2005][research_purivigraipong_unwin_2005]
- [Purivigraipong et al 2010][research_purivigraipong_hodgart_2010]
- [Purshouse 2003][research_purshouse_2003]
- [Purvis 2003][research_purvis_2003]
- [Putra et al 2018][research_putra_wiyagi_2018]
- [Putscher 1967][research_putscher_1967]
- [Pyzynski 2020][research_pyzynski_2020]
- [Pátek and Smrcek 1999][research_patek_smrcek_1999]
- [Qi and Wang 2016][research_qi_wang_2016]
- [Qi et al 2017][research_qi_wang_2017]
- [Qi et al 2018][research_qi_zhao_2018]
- [Qi et al 2018][research_qi_zhao_2018_b]
- [Qian et al 2010][research_qian_chengquan_2010]
- [Qian Shen et al 2016][research_qianshen_suozhongyuan_2016]
- [Qiao et al 2008][research_qiao_bai_2008]
- [Qin et al 2017][research_qin_ang_2017]
- [Qin et al 2019][research_qin_yue_2019]
- [Qin et al 2024][research_qin_yang_2024]
- [Qinkun Xiao et al 2006][research_qinkunxiao_xiaoguanggao_2006]
- [Qiwei et al 2014][research_qiwei_shumei_2014]
- [Qu et al 2011][research_qu_li_2011]
- [Qu et al 2013][research_qu_li_2013]
- [Quan et al 2018][research_quan_xiao_2018]
- [Quan et al 2021][research_quan_edmond_2021]
- [R H et al 2020][research_rh_vp_2020]
- [Rabbou and El-Rabbany 2021][research_rabbou_elrabbany_2021]
- [Racette et al 2023][research_racette_dunaway_2023]
- [Raczkowski et al 2026][research_raczkowski_boyd_2026]
- [Radar Altimeter Aiding of 2019][research_radar_altimeter_2019]
- [Ragi and Chong 2013][research_ragi_chong_2013]
- [Ragon et al 2003][research_ragon_gurdal_2003]
- [Rajamurugu et al 2026][research_rajamurugu_dheerajkumar_2026]
- [Rajpal and Pant 2011][research_rajpal_pant_2011]
- [Rajput et al 2014][research_rajput_zhang_2014]
- [Rajput et al 2015][research_rajput_zhangweiguo_2015]
- [Ralles 1966][research_ralles_1966]
- [Ramasamy 2015][research_ramasamy_2015]
- [Ramasamy and Ghose 2016][research_ramasamy_ghose_2016]
- [Ramasamy et al 2015][research_ramasamy_gardi_2015]
- [Ramesh and Subbarao 2016][research_ramesh_subbarao_2016]
- [Ramin et al 2022][research_ramin_heriana_2022]
- [Ramsey and Dixon 1967][research_ramsey_dixon_1967]
- [Randolph 1997][research_randolph_1997]
- [Ransquin et al 2021][research_ransquin_caprace_2021]
- [Rao and Narayana 1995][research_rao_narayana_1995]
- [Rao et al 2001][research_rao_sarma_2001]
- [Rao et al 2020][research_rao_ma_2020]
- [Rapinski et al 2012][research_rapinski_cellmer_2012]
- [Rapstine et al 2017][research_rapstine_sava_2017]
- [Rarthlomeusz et al 1993][research_rarthlomeusz_paul_1993]
- [Rasmussen 1992][research_rasmussen_1992]
- [Ratcliffe 1983][research_ratcliffe_1983]
- [Ravenstein 1984][research_ravenstein_1984]
- [Ray et al 1999][research_ray_salychev_1999]
- [Raychaudhuri][research_raychaudhuri]
- [Raychem gel material improves 1998][research_raychem_gel_1998]
- [Rayman 1979][research_rayman_1979]
- [Raymer 1992][research_raymer_1992]
- [Raymer 1998][research_raymer_1998]
- [Raymer 2012][research_raymer_2012]
- [Raymer 2012][research_raymer_2012_b]
- [Raymer 2018][research_raymer_2018]
- [Raymer 2024][research_raymer_2024]
- [Razzak and Damodaran 2022][research_razzak_damodaran_2022]
- [Read and Iii 1991][research_read_iii_1991]
- [Real-Time Kinematics Relative Positioning 2015][research_real_time_kinematics_2015]
- [Reardon et al 1999][research_reardon_katz_1999]
- [Rebel 2000][research_rebel_2000]
- [Recktenwald and Ahmed 2008][research_recktenwald_ahmed_2008]
- [Recktenwald et al 2010][research_recktenwald_crouse_2010]
- [Recommended Practice for Measurement][research_recommended_practice]
- [Redesigned aircraft landing gear 1987][research_redesigned_aircraft_1987]
- [Redesigning landing gear for 2001][research_redesigning_landing_2001]
- [Reed 2010][research_reed_2010]
- [Regan 1986][research_regan_1986]
- [Reichbach et al 2001][research_reichbach_sedwick_2001]
- [Reichenbach 2003][research_reichenbach_2003]
- [Reichstein et al 2022][research_reichstein_schopferer_2022]
- [Reid 1969][research_reid_1969]
- [Reid 1978][research_reid_1978]
- [Reinbold 1954][research_reinbold_1954]
- [Reinhardt and Johansen 2021][research_reinhardt_johansen_2021]
- [Reinhart 1975][research_reinhart_1975]
- [Reitan and Saib 1976][research_reitan_saib_1976]
- [Relative Navigation 1972][research_relative_navigation_1972]
- [Remiger et al 2024][research_remiger_grois_2024]
- [Ren and Quan 2024][research_ren_quan_2024]
- [Ren and Stephens 2006][research_ren_stephens_2006]
- [Ren et al 2023][research_ren_lyu_2023]
- [Ren et al 2024][research_ren_man_2024]
- [Ren et al 2025][research_ren_wang_2025]
- [Ren et al 2026][research_ren_du_2026]
- [Renehan 1997][research_renehan_1997]
- [Renga et al 2009][research_renga_tancredi_2009]
- [Renga et al 2013][research_renga_grassi_2013]
- [Renga et al 2015][research_renga_tancredi_2015]
- [Reorganization for the Era 2008][research_reorganization_for_2008]
- [Requirements Analysis, Partitioning, Implementation 2013][research_requirements_analysis_2013]
- [Resulkulyeva and Serebryansky 2022][research_resulkulyeva_serebryansky_2022]
- [Reubush 1979][research_reubush_1979]
- [Rezaifard and Abbasi 2017][research_rezaifard_abbasi_2017]
- [Rhoads 1967][research_rhoads_1967]
- [Rhudy et al 2014][research_rhudy_gu_2014]
- [Rhudy et al 2019][research_rhudy_gross_2019]
- [Riaz 2011][research_riaz_2011]
- [Ribarich 1967][research_ribarich_1967]
- [Riboldi 2019][research_riboldi_2019]
- [Riccardi et al 2025][research_riccardi_mamino_2025]
- [Richards and Tate 2023][research_richards_tate_2023]
- [Richez and Costello 2024][research_richez_costello_2024]
- [Ridha 1968][research_ridha_1968]
- [Ridley 1982][research_ridley_1982]
- [Riedel 1979][research_riedel_1979]
- [Rieken et al 2004][research_rieken_yasumuro_2004]
- [Rife 1993][research_rife_1993]
- [Rife 2009][research_rife_2009]
- [Rife et al 2008][research_rife_khanafseh_2008]
- [Rinkinen 1959][research_rinkinen_1959]
- [Rios Quesada and Charpentier][research_riosquesada_charpentier]
- [Ritchey 2008][research_ritchey_2008]
- [Ritter][research_ritter]
- [Rizzetta and Visbal 2016][research_rizzetta_visbal_2016]
- [RlDHA 1969][research_rldha_1969]
- [Roadman et al 2012][research_roadman_elston_2012]
- [Roberto Mati 2006][research_robertomati_2006]
- [Roberts and Sutton 2006][research_roberts_sutton_2006]
- [Robinson 1992][research_robinson_1992]
- [Robinson 2004][research_robinson_2004]
- [Rocha et al 2006][research_rocha_li_2006]
- [Rodden 1972][research_rodden_1972]
- [Rodriguez and Liscouët-Hanke 2025][research_rodriguez_liscouethanke_2025]
- [Rodriguez-Ramos et al 2017][research_rodriguezramos_sampedro_2017]
- [Rogers 2009][research_rogers_2009]
- [Rogers and Cook 1952][research_rogers_cook_1952]
- [Rohl and Schrage 1992][research_rohl_schrage_1992]
- [Rojas Carvajal and Amitay 2023][research_rojascarvajal_amitay_2023]
- [Rojas Carvajal and Amitay 2025][research_rojascarvajal_amitay_2025]
- [Rojas Carvajal et al 2022][research_rojascarvajal_guha_2022]
- [Rollo et al 2024][research_rollo_volf_2024]
- [Rolls-Royce and British Aerospace 1999][research_rolls_royce_and_1999]
- [Roltgen and Gilbert 2010][research_roltgen_gilbert_2010]
- [Romero 2015][research_romero_2015]
- [roof bolter 2014][research_roof_bolter_2014]
- [Roof bolting machine operators 2006][research_roof_bolting_2006]
- [Rosales et al 2021][research_rosales_reyes_2021]
- [Rosamond 1961][research_rosamond_1961]
- [Rose et al 2022][research_rose_ghoreyshi_2022]
- [Rosenman and Hoekstra 1964][research_rosenman_hoekstra_1964]
- [Rosenstein 1989][research_rosenstein_1989]
- [Rosenthal 1970][research_rosenthal_1970]
- [Rosenthal and Walsh 1996][research_rosenthal_walsh_1996]
- [Rosin et al 2004][research_rosin_mattos_2004]
- [Roskam 1985][research_roskam_1985]
- [Roskam 1986][research_roskam_1986]
- [Roskam 1988][research_roskam_1988]
- [Ross and Matarazzo 1982][research_ross_matarazzo_1982]
- [Rothmaier and Del Peral Rosado 2023][research_rothmaier_delperalrosado_2023]
- [Rothwell 2001][research_rothwell_2001]
- [Rotorcraft Application of Existing][research_rotorcraft_application]
- [Rotorcraft handling qualities design 2011][research_rotorcraft_handling_2011]
- [Rovig et al 2004][research_rovig_bohnker_2004]
- [Roy 2009][research_roy_2009]
- [Roy and Ghosh 2010][research_roy_ghosh_2010]
- [Roy et al 2006][research_roy_levy_2006]
- [Rozov et al 2019][research_rozov_volmering_2019]
- [Ruan and Wei 2019][research_ruan_wei_2019]
- [Rudowsky et al 2002][research_rudowsky_hynes_2002]
- [Rudy 2013][research_rudy_2013]
- [Ruetten 2018][research_ruetten_2018]
- [Ruff et al 2002][research_ruff_narayanan_2002]
- [Ruggiero et al 2025][research_ruggiero_ito_2025]
- [Rui 2016][research_rui_2016]
- [Rui et al 2007][research_rui_zhou_2007]
- [Rui Li et al 2013][research_ruili_dazhizeng_2013]
- [Ruiqian et al 2020][research_ruiqian_juan_2020]
- [Ruiyang et al 2020][research_ruiyang_konstantin_2020]
- [Rumba and Nikitenko 2020][research_rumba_nikitenko_2020]
- [Rupert 2008][research_rupert_2008]
- [Ryan 1990][research_ryan_1990]
- [Ryan and Cummings 2016][research_ryan_cummings_2016]
- [Ryan et al 2011][research_ryan_cummings_2011]
- [Ryan et al 2014][research_ryan_banerjee_2014]
- [Rylko et al 2025][research_rylko_favaro_2025]
- [Rzucidło 2006][research_rzucidlo_2006]
- [Răducanu and Cîrciu 2017][research_raducanu_circiu_2017]
- [S. et al 2025][research_s_c_2025]
- [Sabatini et al 2013][research_sabatini_moore_2013]
- [Sabatini et al 2015][research_sabatini_cappello_2015]
- [Sacharny and Henderson 2022][research_sacharny_henderson_2022]
- [Sacharny and Henderson 2022][research_sacharny_henderson_2022_b]
- [Sachs and Moeller 1995][research_sachs_moeller_1995]
- [Sachse 1998][research_sachse_1998]
- [Sadasivan et al 2001][research_sadasivan_gurubasavaraj_2001]
- [Sadraey 2010][research_sadraey_2010]
- [Sadraey 2014][research_sadraey_2014]
- [Sadraey 2016][research_sadraey_2016]
- [Sadraey 2016][research_sadraey_2016_b]
- [Saeedipour and Neil Stevenson 1998][research_saeedipour_neilstevenson_1998]
- [Saelman 1964][research_saelman_1964]
- [Saetti and Rogers 2020][research_saetti_rogers_2020]
- [Safeer and Costello 2026][research_safeer_costello_2026]
- [Safety Considerations - Flight][research_safety_considerations]
- [Safi 2023][research_safi_2023]
- [Safvat and Keighobadi 2025][research_safvat_keighobadi_2025]
- [Sagdeo 1990][research_sagdeo_1990]
- [Saghafi and Esmailifar 2009][research_saghafi_esmailifar_2009]
- [Saha et al 2023][research_saha_kumar_2023]
- [Saheby et al 2026][research_saheby_jialu_2026]
- [Sai et al 2025][research_sai_athreyam_2025]
- [Saif et al 2014][research_saif_fantoni_2014]
- [Sakamaki et al 2017][research_sakamaki_beard_2017]
- [Salt 1995][research_salt_1995]
- [Saltzgaber and Miller 2003][research_saltzgaber_miller_2003]
- [Samareh, Jamshid A. et al 2006][research_samarehjamshida_sensmeiermarkd_2006]
- [Samuels 1982][research_samuels_1982]
- [Sanchez-Carmona and Cuerno-Rejado 2018][research_sanchezcarmona_cuernorejado_2018]
- [Sancho 2002][research_sancho_2002]
- [Sanders 1957][research_sanders_1957]
- [Sandy 1981][research_sandy_1981]
- [Sanghi 2003][research_sanghi_2003]
- [Sanghi et al 2022][research_sanghi_riso_2022]
- [Sanghi et al 2024][research_sanghi_cesnik_2024]
- [Sankar 2012][research_sankar_2012]
- [Santamaría Barnadas][research_santamariabarnadas]
- [Santerre and Geiger 2018][research_santerre_geiger_2018]
- [Santerre et al 2017][research_santerre_geiger_2017]
- [Santhosh Kumar S A and Suganthi J 2015][research_santhoshkumarsa_suganthij_2015]
- [Santoso and Hariyanto 2022][research_santoso_hariyanto_2022]
- [Sarigul-Klijn et al 2008][research_sarigulklijn_sarigulklijn_2008]
- [Sarrafian and Powers 1988][research_sarrafian_powers_1988]
- [Sasiadek and Wang 1999][research_sasiadek_wang_1999]
- [Sasiadek et al 2000][research_sasiadek_wang_2000]
- [Saska 2015][research_saska_2015]
- [Saska et al 2014][research_saska_chudoba_2014]
- [Sasoh et al 2015][research_sasoh_imaizumi_2015]
- [Sastry 2001][research_sastry_2001]
- [Sathe and Pant 2010][research_sathe_pant_2010]
- [Satkunanathan and Murphy 1998][research_satkunanathan_murphy_1998]
- [Saucez][research_saucez]
- [Saucez and Boiffier 2012][research_saucez_boiffier_2012]
- [Sauter et al 2005][research_sauter_matthews_2005]
- [Savić 2024][research_savic_2024]
- [Savuran and Karakaya 2015][research_savuran_karakaya_2015]
- [Savuran and Karakaya 2015][research_savuran_karakaya_2015_b]
- [Sayim 2018][research_sayim_2018]
- [Scafetta 1983][research_scafetta_1983]
- [Scarpa 2001][research_scarpa_2001]
- [Schairer 1946][research_schairer_1946]
- [Schalk 2017][research_schalk_2017]
- [Schallhorn 2020][research_schallhorn_2020]
- [Scheidt 2014][research_scheidt_2014]
- [Scherer et al 2015][research_scherer_yang_2015]
- [Scherzinger and Blake Reid 1989][research_scherzinger_blakereid_1989]
- [Schleicher 1966][research_schleicher_1966]
- [Schmidt 1983][research_schmidt_1983]
- [Schmidt 1984][research_schmidt_1984]
- [Schmidt 1985][research_schmidt_1985]
- [Schmidt 2015][research_schmidt_2015]
- [Schmidt 2016][research_schmidt_2016]
- [Schmidt 2021][research_schmidt_2021]
- [Schmidt and Setterlund 1994][research_schmidt_setterlund_1994]
- [Schmidt et al 2006][research_schmidt_stevens_2006]
- [Schneider 1989][research_schneider_1989]
- [Schneider and Maida][research_schneider_maida]
- [Schoenbeck and Schultz 1999][research_schoenbeck_schultz_1999]
- [Schoenbein 2009][research_schoenbein_2009]
- [Schoenman and Doniger 1965][research_schoenman_doniger_1965]
- [Scholz et al 2026][research_scholz_theuser_2026]
- [Schopferer and Benders 2020][research_schopferer_benders_2020]
- [Schopferer and Pfeifer 2015][research_schopferer_pfeifer_2015]
- [Schrage and McKeithan 1989][research_schrage_mckeithan_1989]
- [Schuette et al 2018][research_schuette_vormweg_2018]
- [Schultz et al 2009][research_schultz_mcgrath_2009]
- [Schutz and Kutrzyba 2000][research_schutz_kutrzyba_2000]
- [Schwartz 1975][research_schwartz_1975]
- [Schwartz 1988][research_schwartz_1988]
- [Scognamiglio et al 2024][research_scognamiglio_caccavale_2024]
- [Scott and Hartmann 2024][research_scott_hartmann_2024]
- [Scott and Trimarchi 2024][research_scott_trimarchi_2024]
- [Scribner 1998][research_scribner_1998]
- [Scukins et al 2023][research_scukins_klein_2023]
- [Seah and Hwang 2006][research_seah_hwang_2006]
- [Seah and Hwang 2007][research_seah_hwang_2007]
- [Seah and Hwang 2009][research_seah_hwang_2009]
- [Sease et al 2023][research_sease_warwick_2023]
- [Seaton 1989][research_seaton_1989]
- [Seats for Flight DECK][research_seats_for]
- [Seats for Flight Deck][research_seats_for_b]
- [Sebestyén and Szénási 2026][research_sebestyen_szenasi_2026]
- [Section 7 International Civil 2016][research_section_7_2016]
- [See et al 2017][research_see_ghosh_2017]
- [Seiferth et al 2017][research_seiferth_kuchar_2017]
- [Seitzer 2003][research_seitzer_2003]
- [Selecting the Planform and 2010][research_selecting_the_2010]
- [Semakov and Semakov 2020][research_semakov_semakov_2020]
- [Semke 2016][research_semke_2016]
- [Semke 2021][research_semke_2021]
- [Sensmeier, Mark D. and Samareh, Jamshid A. 2005][research_sensmeiermarkd_samarehjamshida_2005]
- [Sepulveda Palacios and Smith 2019][research_sepulvedapalacios_smith_2019]
- [Seraj and Martins 2022][research_seraj_martins_2022]
- [Serrano and Serrano 2010][research_serrano_serrano_2010]
- [Sevcik and Oh][research_sevcik_oh]
- [Sevostyanov and Devitt 2021][research_sevostyanov_devitt_2021]
- [Sevostyanov et al 2022][research_sevostyanov_devitt_2022]
- [Sgarioto et al 2006][research_sgarioto_williams_2006]
- [Shaghaghian and Karimaghaee 2018][research_shaghaghian_karimaghaee_2018]
- [Shaiju and Sreeja 2022][research_shaiju_sreeja_2022]
- [Shaikh 2025][research_shaikh_2025]
- [Shane 1992][research_shane_1992]
- [Shanshan et al 2020][research_shanshan_ao_2020]
- [Shao et al 2023][research_shao_li_2023]
- [Shao et al 2024][research_shao_guo_2024]
- [Shao et al 2026][research_shao_li_2026]
- [Sharma and Hablani 2014][research_sharma_hablani_2014]
- [Sharma et al 2009][research_sharma_saunders_2009]
- [Sharma et al 2021][research_sharma_padthe_2021]
- [Shaw 1960][research_shaw_1960]
- [Shaw and Smith 1977][research_shaw_smith_1977]
- [Shaw et al 1988][research_shaw_clark_1988]
- [Shay et al 2012][research_shay_swieringa_2012]
- [Shayan and Van Kampen 2021][research_shayan_vankampen_2021]
- [Shayler 1961][research_shayler_1961]
- [Shen and Rahman 2011][research_shen_rahman_2011]
- [Shen et al 2016][research_shen_hao_2016]
- [Shen et al 2019][research_shen_lifey_2019]
- [Shen et al 2026][research_shen_zhang_2026]
- [Sheppard and Foster 2008][research_sheppard_foster_2008]
- [Sher 1981][research_sher_1981]
- [Sherstjuk 2015][research_sherstjuk_2015]
- [Shi 2023][research_shi_2023]
- [Shi and Gao 2013][research_shi_gao_2013]
- [Shi and Ng 2018][research_shi_ng_2018]
- [Shi and Wu 2022][research_shi_wu_2022]
- [Shimski et al 2013][research_shimski_schmidt_2013]
- [Shin et al 2013][research_shin_you_2013]
- [Shin et al 2013][research_shin_you_2013_b]
- [Shipman et al 2008][research_shipman_arunajatesan_2008]
- [Shirley et al 2014][research_shirley_schetz_2014]
- [Shiyan et al 2016][research_shiyan_huimin_2016]
- [Shock mounts for aircraft 1993][research_shock_mounts_1993]
- [Shoop et al 2023][research_shoop_munoz_2023]
- [Shoop et al 2024][research_shoop_munoz_2024]
- [Shriwastav and Song 2020][research_shriwastav_song_2020]
- [Shu et al 2013][research_shu_sun_2013]
- [Shuang et al 2016][research_shuang_zhang_2016]
- [Shuang et al 2017][research_shuang_zhang_2017]
- [Shubert and Jones 2025][research_shubert_jones_2025]
- [Shujun et al 2014][research_shujun_jianyun_2014]
- [Shustrov 1998][research_shustrov_1998]
- [Shweyk and Hyde 2013][research_shweyk_hyde_2013]
- [Si et al 2024][research_si_song_2024]
- [Sibruk et al 2015][research_sibruk_bondarenko_2015]
- [Siddarth and Valasek 2011][research_siddarth_valasek_2011]
- [Siegel 1995][research_siegel_1995]
- [Siegel and Crain 1960][research_siegel_crain_1960]
- [Siegel and Lanterman 1963][research_siegel_lanterman_1963]
- [Silva][research_silva]
- [Silva][research_silva_b]
- [Silva and Guimarães 2020][research_silva_guimaraes_2020]
- [Silva et al 2024][research_silva_lundbladh_2024]
- [Sim et al 1994][research_sim_murray_1994]
- [Simmons 1993][research_simmons_1993]
- [Simms 2023][research_simms_2023]
- [Simon and Chudoba 2021][research_simon_chudoba_2021]
- [Simoncic 2013][research_simoncic_2013]
- [Simonetti and Crespillo 2024][research_simonetti_crespillo_2024]
- [Simos and Jenkinson 1986][research_simos_jenkinson_1986]
- [Simplício et al 2018][research_simplicio_navarrotapia_2018]
- [Simpson et al 2005][research_simpson_rawashdeh_2005]
- [Singer 2011][research_singer_2011]
- [Singh 1974][research_singh_1974]
- [Singh et al 2016][research_singh_toropov_2016]
- [Sinha et al 2001][research_sinha_arunajatesan_2001]
- [Sirigireddy and Ahner 2026][research_sirigireddy_ahner_2026]
- [Sivakumar et al 2021][research_sivakumar_man_2021]
- [Sivakumar et al 2022][research_sivakumar_hasrizamcheman_2022]
- [Sivaramakrishnan 1981][research_sivaramakrishnan_1981]
- [Sizing from a Conceptual 2024][research_sizing_from_2024]
- [Sizing the Engine Installed 2002][research_sizing_the_2002]
- [Sizing the Engine Installed 2018][research_sizing_the_2018]
- [Sizing, Trade Studies, and 2024][research_sizing_trade_2024]
- [Sjöberg 1998][research_sjoberg_1998]
- [Skillen and Crossley 2005][research_skillen_crossley_2005]
- [Skillen and Crossley 2008][research_skillen_crossley_2008]
- [Skjong et al 2015][research_skjong_nundal_2015]
- [Skorobogatov and Buturov 2026][research_skorobogatov_buturov_2026]
- [Slapnicar][research_slapnicar]
- [Slegers et al 2008][research_slegers_beyer_2008]
- [Smith][research_smith]
- [Smith 1967][research_smith_1967]
- [Smith 1968][research_smith_1968]
- [Smith 2000][research_smith_2000]
- [Smith 2023][research_smith_2023]
- [Smith and Chow 1998][research_smith_chow_1998]
- [Smith and Meyer 1981][research_smith_meyer_1981]
- [Smith et al 2026][research_smith_andersen_2026]
- [Snyder 1950][research_snyder_1950]
- [Snyder 1990][research_snyder_1990]
- [Snyder 2000][research_snyder_2000]
- [Snyder et al][research_snyder_schipper]
- [Snyder et al 1992][research_snyder_schipper_1992]
- [Snyder et al 2009][research_snyder_sanders_2009]
- [So 2016][research_so_2016]
- [Soban 1993][research_soban_1993]
- [Soemaryanto and Rosid 2018][research_soemaryanto_rosid_2018]
- [Solies 1995][research_solies_1995]
- [Soloviev and Venable 2010][research_soloviev_venable_2010]
- [Solvey 1951][research_solvey_1951]
- [Song 2008][research_song_2008]
- [Song and Ai 2021][research_song_ai_2021]
- [Song et al 2014][research_song_yang_2014]
- [Song et al 2019][research_song_zhang_2019]
- [Song et al 2020][research_song_chen_2020]
- [Song et al 2020][research_song_ma_2020]
- [Soni and Hablani 2015][research_soni_hablani_2015]
- [Soop 1994][research_soop_1994]
- [Soop 1994][research_soop_1994_b]
- [Sorensen and Johansen 2017][research_sorensen_johansen_2017]
- [Sosa 1997][research_sosa_1997]
- [Souanef 2024][research_souanef_2024]
- [Soumekh][research_soumekh]
- [Souza and Monico 2004][research_souza_monico_2004]
- [Speakman et al 1978][research_speakman_powell_1978]
- [Special Topics in Unmanned 2014][research_special_topics_2014]
- [Specification for Aircraft Flight][research_specification_for_c]
- [Specification for aircraft pressure][research_specification_for_e]
- [Specification for Design and][research_specification_for]
- [Specification for Design of][research_specification_for_f]
- [Specification for Small Unmanned][research_specification_for_d]
- [Specification for Unmanned Aircraft][research_specification_for_b]
- [Sperling et al 2008][research_sperling_kewley_2008]
- [Speth et al 2016][research_speth_kamann_2016]
- [Spiridon and Fuiorea 2025][research_spiridon_fuiorea_2025]
- [Spreen 2019][research_spreen_2019]
- [Spreen 2019][research_spreen_2019_b]
- [Spreen 2019][research_spreen_2019_c]
- [Spreen 2019][research_spreen_2019_d]
- [Spreen 2019][research_spreen_2019_e]
- [Spreen 2019][research_spreen_2019_f]
- [Spreen 2019][research_spreen_2019_g]
- [Spreen 2019][research_spreen_2019_h]
- [Spreen 2019][research_spreen_2019_i]
- [Spreen 2019][research_spreen_2019_j]
- [Spreen 2019][research_spreen_2019_k]
- [Spreen 2019][research_spreen_2019_l]
- [Spreen 2019][research_spreen_2019_m]
- [Spreen 2019][research_spreen_2019_n]
- [Spreen 2023][research_spreen_2023]
- [Spry et al][research_spry_girard]
- [Squire et al 2006][research_squire_trafton_2006]
- [Srinathkumar 2011][research_srinathkumar_2011]
- [Srinuandee][research_srinuandee]
- [Staack][research_staack]
- [Staats et al 2025][research_staats_troeltsch_2025]
- [Stability, Control, and Handling 2024][research_stability_control_2024]
- [Stachiw][research_stachiw]
- [Stachiw et al 2020][research_stachiw_khouli_2020]
- [Stachiw et al 2021][research_stachiw_khouli_2021]
- [Staelens et al 2007][research_staelens_blackwelder_2007]
- [Stalford 1979][research_stalford_1979]
- [Stamm and Woods 2024][research_stamm_woods_2024]
- [Standard Guide for Wing][research_standard_guide]
- [Standard Practice for Development][research_standard_practice]
- [Standard Specification for Light][research_standard_specification]
- [Standard Specification for Light][research_standard_specification_b]
- [Standard Specification for Small][research_standard_specification_c]
- [Standard Terminology for Unmanned][research_standard_terminology]
- [Stanek 2002][research_stanek_2002]
- [Stanek 2003][research_stanek_2003]
- [Stanek 2007][research_stanek_2007]
- [Stanford et al 2012][research_stanford_kurdi_2012]
- [Stark and Chen 2014][research_stark_chen_2014]
- [Stastny and Stoica 2021][research_stastny_stoica_2021]
- [Station Keeping 2008][research_station_keeping_2008]
- [Station Keeping Of Satellites 1962][research_station_keeping_1962]
- [Station Keeping System 2022][research_station_keeping_2022]
- [Stechman 1984][research_stechman_1984]
- [Stedman 1992][research_stedman_1992]
- [Steeb et al 1979][research_steeb_chu_1979]
- [Stegall 2001][research_stegall_2001]
- [Steinberg][research_steinberg]
- [Steinberg 1992][research_steinberg_1992]
- [Steinberg and Page 2001][research_steinberg_page_2001]
- [Stemler and Craig 1976][research_stemler_craig_1976]
- [Stenfelt and Ringertz 2009][research_stenfelt_ringertz_2009]
- [Stenfelt and Ringertz 2010][research_stenfelt_ringertz_2010]
- [Stepanova 2025][research_stepanova_2025]
- [Stephan et al 2020][research_stephan_pfeifle_2020]
- [Stewart et al 2012][research_stewart_roberts_2012]
- [Stieger 1929][research_stieger_1929]
- [Stoltz 1995][research_stoltz_1995]
- [Stolz and Hein 1989][research_stolz_hein_1989]
- [Stone][research_stone]
- [Storage, Handling, and Shipping][research_storage_handling]
- [Strattan 1978][research_strattan_1978]
- [Stratton 1995][research_stratton_1995]
- [Strawser 2013][research_strawser_2013]
- [Streamline development of aircraft 2009][research_streamline_development_2009]
- [Strganac 2007][research_strganac_2007]
- [Striebich 1986][research_striebich_1986]
- [Strietzel and Shefler 1963][research_strietzel_shefler_1963]
- [Stringer et al][research_stringer_bunner]
- [Strock 1983][research_strock_1983]
- [Stroub 1989][research_stroub_1989]
- [Structural dynamics centre for 1999][research_structural_dynamics_1999]
- [Structure with carrier suitability 1974][research_structure_with_1974]
- [Strukov_ 2025][research_strukov_2025]
- [Sturza 1983][research_sturza_1983]
- [Su and Schön 2021][research_su_schon_2021]
- [Su et al 2013][research_su_xu_2013]
- [Su et al 2018][research_su_han_2018]
- [Su et al 2018][research_su_han_2018_b]
- [Su et al 2018][research_su_li_2018]
- [Su et al 2018][research_su_wu_2018]
- [Su et al 2019][research_su_li_2019]
- [Su et al 2023][research_su_schon_2023]
- [Suarez et al 1992][research_suarez_kramer_1992]
- [Subbarao et al 2001][research_subbarao_steinberg_2001]
- [Subrahmanyam 1994][research_subrahmanyam_1994]
- [Subrahmanyam 1995][research_subrahmanyam_1995]
- [Subramani et al 2021][research_subramani_m_2021]
- [Subramaniam et al 2012][research_subramaniam_joseph_2012]
- [Subrata 2017][research_subrata_2017]
- [Suggett 1960][research_suggett_1960]
- [Sugimoto 2006][research_sugimoto_2006]
- [Sui 2022][research_sui_2022]
- [Suima 2025][research_suima_2025]
- [Sullings and Waller 1967][research_sullings_waller_1967]
- [Sullivan 1991][research_sullivan_1991]
- [Sullivan 1991][research_sullivan_1991_b]
- [Sullivan 1991][research_sullivan_1991_c]
- [Sullivan 1997][research_sullivan_1997]
- [Suminsby 2002][research_suminsby_2002]
- [Summey et al 2001][research_summey_rodriguez_2001]
- [Sun 2023][research_sun_2023]
- [Sun 2026][research_sun_2026]
- [Sun and Fu 2018][research_sun_fu_2018]
- [Sun and Gebre-Egziabher 2021][research_sun_gebreegziabher_2021]
- [Sun and Pack 2016][research_sun_pack_2016]
- [Sun and Tang 2011][research_sun_tang_2011]
- [Sun et al 2005][research_sun_zhang_2005]
- [Sun et al 2019][research_sun_deng_2019]
- [Sun et al 2022][research_sun_zhang_2022]
- [Sun et al 2022][research_sun_zhang_2022_b]
- [Sun et al 2024][research_sun_zhou_2024]
- [Sun et al 2025][research_sun_duan_2025]
- [Sun et al 2025][research_sun_guo_2025]
- [Sun et al 2025][research_sun_liu_2025]
- [Sun et al 2026][research_sun_wang_2026]
- [Sun et al 2026][research_sun_zhang_2026]
- [Suozhong Yuan and Yidong Yang][research_suozhongyuan_yidongyang]
- [Supplementary Bibliography for Aircraft 1990][research_supplementary_bibliography_1990]
- [Supriyono and Akhara 2021][research_supriyono_akhara_2021]
- [Suresh et al 2013][research_suresh_radhakrishnan_2013]
- [Suresh et al 2019][research_suresh_sura_2019]
- [Surgeoner 1999][research_surgeoner_1999]
- [Surono et al 2021][research_surono_ashar_2021]
- [Survivability of Unmanned Autonomous 2016][research_survivability_of_2016]
- [Sutrakar et al 2025][research_sutrakar_kumari_2025]
- [Sutton 2005][research_sutton_2005]
- [Sutton 2006][research_sutton_2006]
- [Suzuki and Yonezawa 1993][research_suzuki_yonezawa_1993]
- [Svendsen et al 2013][research_svendsen_obrien_2013]
- [Svoboda 1999][research_svoboda_1999]
- [Svoboda 2000][research_svoboda_2000]
- [Swaim 1969][research_swaim_1969]
- [Swanson][research_swanson]
- [Swanson and Isaac 2010][research_swanson_isaac_2010]
- [Swett and Blanche][research_swett_blanche]
- [Swisdak and Michael M. 1992][research_swisdak_michaelm_1992]
- [Sychev 2017][research_sychev_2017]
- [Syd S. Peng 2001][research_sydspeng_2001]
- [Syd S. Peng 2002][research_sydspeng_2002]
- [Syd S. Peng 2002][research_sydspeng_2002_b]
- [Syd S. Peng 2003][research_sydspeng_2003]
- [Syd S. Peng 2004][research_sydspeng_2004]
- [Syd S. Peng 2005][research_sydspeng_2005]
- [Sylvester 1980][research_sylvester_1980]
- [Synthetic vision and precision 1994][research_synthetic_vision_1994]
- [Szabolcsi 2018][research_szabolcsi_2018]
- [Szabolcsi 2018][research_szabolcsi_2018_b]
- [Szabolcsi 2018][research_szabolcsi_2018_c]
- [Sánchez López][research_sanchezlopez]
- [T. Davies 1974][research_tdavies_1974]
- [T. Ruxton-davies and Powell 1970][research_truxtondavies_powell_1970]
- [Tactical Air Command Langley Afb Va 1989][research_tacticalaircommandlangleyafbva_1989]
- [Tafanidis et al 2025][research_tafanidis_banerjee_2025]
- [Taflan et al 2026][research_taflan_smith_2026]
- [Taghizadeh and Safabakhsh 2023][research_taghizadeh_safabakhsh_2023]
- [Tait et al 2009][research_tait_hatfield_2009]
- [Takahashi 2022][research_takahashi_2022]
- [Takita and Kashitani 2016][research_takita_kashitani_2016]
- [Takita and Kashitani 2017][research_takita_kashitani_2017]
- [Tal and Karaman 2021][research_tal_karaman_2021]
- [Talbot 1991][research_talbot_1991]
- [Tam 2015][research_tam_2015]
- [Tan et al 2014][research_tan_zhou_2014]
- [Tan et al 2015][research_tan_wang_2015]
- [Tan et al 2019][research_tan_wang_2019]
- [Tanaka and Matsumoto 2019][research_tanaka_matsumoto_2019]
- [Tancredi et al 2010][research_tancredi_renga_2010]
- [Tancredi et al 2012][research_tancredi_renga_2012]
- [Tancredi et al 2013][research_tancredi_renga_2013]
- [Tancredi et al 2014][research_tancredi_renga_2014]
- [Tandale et al 2005][research_tandale_bowers_2005]
- [Tandale et al 2006][research_tandale_bowers_2006]
- [Tang][research_tang]
- [Tang and Dowell 2008][research_tang_dowell_2008]
- [Tang and Lai 2020][research_tang_lai_2020]
- [Tang et al 2018][research_tang_shen_2018]
- [Tang et al 2024][research_tang_zeng_2024]
- [Tang, Adrian J. 2013][research_tangadrianj_2013]
- [Tangthong and Aktimagool 2021][research_tangthong_aktimagool_2021]
- [Tanil et al 2016][research_tanil_khanafseh_2016]
- [Tao et al 2022][research_tao_chen_2022]
- [Tate 2001][research_tate_2001]
- [Tatiyaworanun and Purivigraipong 2013][research_tatiyaworanun_purivigraipong_2013]
- [Taylor 1999][research_taylor_1999]
- [Taylor et al 2021][research_taylor_boubin_2021]
- [Teague et al 2008][research_teague_kewley_2008]
- [Technical requirements for small][research_technical_requirements]
- [Technology News 523 2007][research_technology_news_2007]
- [Technology News 559 2017][research_technology_news_2017]
- [Technology News 560 2017][research_technology_news_2017_b]
- [Teel 1999][research_teel_1999]
- [Teel 1999][research_teel_1999_b]
- [Tekinalp and Cavus 2012][research_tekinalp_cavus_2012]
- [Tekinalp and Prach 2013][research_tekinalp_prach_2013]
- [Tekinalp and Prach 2014][research_tekinalp_prach_2014]
- [Teledyne Ryan Aeronautical San Diego Ca 1974][research_teledyneryanaeronauticalsandiegoca_1974]
- [Templalexis et al 2016][research_templalexis_lekas_2016]
- [Templeman and Parker 1968][research_templeman_parker_1968]
- [ten Have 1993][research_tenhave_1993]
- [Teng and Yu 2023][research_teng_yu_2023]
- [Teofilatto 2001][research_teofilatto_2001]
- [Teper and Stapleford 1965][research_teper_stapleford_1965]
- [Teper and Stapleford 1966][research_teper_stapleford_1966]
- [Terheyden and Zickwolff 1986][research_terheyden_zickwolff_1986]
- [Terminology for Unmanned Aircraft][research_terminology_for]
- [Terrain Relative Navigation 2025][research_terrain_relative_2025]
- [Terry 1965][research_terry_1965]
- [Terwilliger and Ison 2014][research_terwilliger_ison_2014]
- [Test methods for civil][research_test_methods]
- [Tests, Impact, Shock Absorber][research_tests_impact]
- [Teunissen][research_teunissen]
- [Teunissen][research_teunissen_b]
- [Teunissen 1995][research_teunissen_1995]
- [Teunissen 1998][research_teunissen_1998]
- [Teunissen 2000][research_teunissen_2000]
- [Teunissen 2003][research_teunissen_2003]
- [Teunissen 2003][research_teunissen_2003_b]
- [Teunissen 2017][research_teunissen_2017]
- [Teunissen 2026][research_teunissen_2026]
- [Teunissen and Odijk 2003][research_teunissen_odijk_2003]
- [Teunissen and Verhagen][research_teunissen_verhagen]
- [Teunissen et al 1999][research_teunissen_joosten_1999]
- [Thakur and Kumar 2021][research_thakur_kumar_2021]
- [The algorithm of the 2020][research_the_algorithm_2020]
- [The Block Decorrelation Method 2002][research_the_block_2002]
- [The Catapult][research_the_catapult]
- [The Control of Multiple 2026][research_the_control_2026]
- [The Culture Catapult][research_the_culture]
- [The Design of Classical 2012][research_the_design_2012]
- [The Ethics of Autonomous 2016][research_the_ethics_2016]
- [The Future of Unmanned 2016][research_the_future_2016]
- [The Kinematics and Dynamics 2015][research_the_kinematics_2015]
- [The Origins of Satellite 2018][research_the_origins_2018]
- [The Process of Lubricating][research_the_process]
- [The Red Wing Church][research_the_red]
- [The Resampled Kernel-Diffeomorphism Filter 2011][research_the_resampled_2011]
- [The U.S. Aircraft Carrier 1998][research_the_u_s_1998]
- [The Use of Digital 2006][research_the_use_2006]
- [The WAVE OFF][research_the_wave]
- [The Wing Structure and 2013][research_the_wing_2013]
- [Theiss 2007][research_theiss_2007]
- [Thelander 1965][research_thelander_1965]
- [Theorem's CADverter software converts 2003][research_theorem_s_cadverter_2003]
- [Theunissen et al 2005][research_theunissen_koeners_2005]
- [Thiele 1965][research_thiele_1965]
- [Thomas 1961][research_thomas_1961]
- [Thome and Jr. 2003][research_thome_jr_2003]
- [Thompson 1965][research_thompson_1965]
- [Thompson and Robertson 1990][research_thompson_robertson_1990]
- [Thorne and Yim 2011][research_thorne_yim_2011]
- [Thota et al 2008][research_thota_krauskopf_2008]
- [Thrust-to-Weight Ratio and Wing 2024][research_thrust_to_weight_ratio_2024]
- [Thukral and Innocenti 1992][research_thukral_innocenti_1992]
- [Thys et al 2025][research_thys_macabiau_2025]
- [Tian and Zhao 2012][research_tian_zhao_2012]
- [Tian et al 2016][research_tian_ge_2016]
- [Tian et al 2025][research_tian_gong_2025]
- [Tian et al 2026][research_tian_sun_2026]
- [Tianjian et al 2014][research_tianjian_xin_2014]
- [Tianyuan and Xiongqing 2009][research_tianyuan_xiongqing_2009]
- [Tiberius et al 2002][research_tiberius_pany_2002]
- [Tielking 1989][research_tielking_1989]
- [Tierney and Rodenbeck 2019][research_tierney_rodenbeck_2019]
- [Tiimus et al 2015][research_tiimus_murumae_2015]
- [Tin et al 2020][research_tin_borowczyk_2020]
- [Tingting and Aijun 2014][research_tingting_aijun_2014]
- [Tinoco][research_tinoco]
- [Tire Pressure Monitoring Systems][research_tire_pressure]
- [Tiwari et al 2020][research_tiwari_stacey_2020]
- [Toffol and Ricci 2023][research_toffol_ricci_2023]
- [Tokarick 2005][research_tokarick_2005]
- [Tolfa and Edward 1971][research_tolfa_edward_1971]
- [Tomac and Stenfelt 2014][research_tomac_stenfelt_2014]
- [Tomac et al 2012][research_tomac_rizzi_2012]
- [Tomczyk and Rogalski 2005][research_tomczyk_rogalski_2005]
- [Tonhauser and Hecker 2016][research_tonhauser_hecker_2016]
- [Torelli et al 2023][research_torelli_stroosma_2023]
- [Torenbeek 1971][research_torenbeek_1971]
- [Torenbeek 1972][research_torenbeek_1972]
- [Torenbeek 2000][research_torenbeek_2000]
- [Torenbeek 2013][research_torenbeek_2013]
- [Torenbeek 2020][research_torenbeek_2020]
- [Torno et al 2014][research_torno_hintz_2014]
- [Torres et al 2023][research_torres_harris_2023]
- [Torvold 2000][research_torvold_2000]
- [Tosun 2023][research_tosun_2023]
- [Toth et al 2017][research_toth_jozkow_2017]
- [Traas et al 2026][research_traas_atmaca_2026]
- [Trade Studies and Sizing 2010][research_trade_studies_2010]
- [Tran][research_tran]
- [Tran et al 2020][research_tran_thiriet_2020]
- [Tranfield][research_tranfield]
- [Traub 1994][research_traub_1994]
- [Traub 1995][research_traub_1995]
- [Traub 1995][research_traub_1995_b]
- [Traub 2016][research_traub_2016]
- [Travis et al 2005][research_travis_simmons_2005]
- [Trimarchi 2023][research_trimarchi_2023]
- [Trinen and Pieri 2026][research_trinen_pieri_2026]
- [Troop Carrier Aviation in][research_troop_carrier]
- [Troop Carrier Aviation in][research_troop_carrier_b]
- [Truxal and Scott 2024][research_truxal_scott_2024]
- [Trw Inc Cleveland Oh Trw Accessories Div 1965][research_trwincclevelandohtrwaccessoriesdiv_1965]
- [TRW to provide weapons 2002][research_trw_to_2002]
- [Tsai et al 2004][research_tsai_chang_2004]
- [Tseng et al 2016][research_tseng_lin_2016]
- [Tsoukalas et al 2026][research_tsoukalas_unlu_2026]
- [Tsourveloudis and Doitsidis 2025][research_tsourveloudis_doitsidis_2025]
- [Tsukamoto et al 2003][research_tsukamoto_deturris_2003]
- [Tsybriy and Guskov 2025][research_tsybriy_guskov_2025]
- [Tu et al 1998][research_tu_munir_1998]
- [Tu et al 2000][research_tu_munir_2000]
- [Tucker and Iii 1993][research_tucker_iii_1993]
- [Tugolukov 2020][research_tugolukov_2020]
- [Turan 2012][research_turan_2012]
- [Turbine Engine Inlet Design 2010][research_turbine_engine_2010]
- [Turner and Faruqi][research_turner_faruqi]
- [Turriziani, R. V. et al 1979][research_turrizianirv_lovellwa_1979]
- [Tuzlukov 2026][research_tuzlukov_2026]
- [Tvaryanas 2006][research_tvaryanas_2006]
- [Tvaryanas 2006][research_tvaryanas_2006_b]
- [Tvaryanas et al 2012][research_tvaryanas_singer_2012]
- [Tweddale et al 2011][research_tweddale_fichtl_2011]
- [Twesme and Corzine 2003][research_twesme_corzine_2003]
- [Tzes et al 2023][research_tzes_tsoukalas_2023]
- [UAV control with active 2023][research_uav_control_2023]
- [UAV demonstrator opens up 2006][research_uav_demonstrator_2006]
- [UAV demonstrator opens up 2007][research_uav_demonstrator_2007]
- [Ugwueze et al 2023][research_ugwueze_statheros_2023]
- [UK aircraft carrier projecting 2014][research_uk_aircraft_2014]
- [Ulybyshev 2015][research_ulybyshev_2015]
- [Universal Balancing supports up 2007][research_universal_balancing_2007]
- [Unmanned Aerial Vehicle Design 2024][research_unmanned_aerial_2024]
- [Unmanned Aerial Vehicles 2013][research_unmanned_aerial_2013]
- [Unmanned Aerial Vehicles 2016][research_unmanned_aerial_2016]
- [Unmanned Aerial Vehicles 2020][research_unmanned_aerial_2020]
- [Unmanned Air Vehicles 2017][research_unmanned_air_2017]
- [Unmanned Aircraft Categories 2012][research_unmanned_aircraft_2012]
- [Unmanned Aircraft Categories 2014][research_unmanned_aircraft_2014]
- [Unmanned Aircraft Geometry and 2014][research_unmanned_aircraft_2014_b]
- [Unmanned Aircraft System Elements 2016][research_unmanned_aircraft_2016]
- [Unmanned Aircraft System Operations 2016][research_unmanned_aircraft_2016_b]
- [Unmanned aircraft systems][research_unmanned_aircraft]
- [Unmanned Aircraft Systems 2009][research_unmanned_aircraft_2009]
- [Unmanned Aircraft Systems for 2016][research_unmanned_aircraft_2016_c]
- [Unmanned Aircraft Systems Regulation][research_unmanned_aircraft_b]
- [Unmanned aircraft systems UAS][research_unmanned_aircraft_c]
- [Unmanned aircraft systems. Training][research_unmanned_aircraft_d]
- [Unmanned Autonomous Vehicle 2016][research_unmanned_autonomous_2016]
- [Unmanned-Aircraft Geometry and Configurations 2012][research_unmanned_aircraft_geometry_2012]
- [ur Rehman 2018][research_urrehman_2018]
- [Urnes and Hess 1983][research_urnes_hess_1983]
- [Urnes and Hess 1985][research_urnes_hess_1985]
- [Urnes et al 1979][research_urnes_hess_1979]
- [Usach Molina][research_usachmolina]
- [Useful Aircraft Design Data][research_useful_aircraft]
- [Useful aircraft design data 1999][research_useful_aircraft_1999]
- [Utsch and Rockwell 1990][research_utsch_rockwell_1990]
- [Utterstrom and Kestek 1965][research_utterstrom_kestek_1965]
- [Uybarreta et al 2025][research_uybarreta_grant_2025]
- [Uzun 2024][research_uzun_2024]
- [Uzzell 1997][research_uzzell_1997]
- [Vachtsevanos and Valavanis 2014][research_vachtsevanos_valavanis_2014]
- [Vahidi and Saberinia 2016][research_vahidi_saberinia_2016]
- [Valavanis and Vachtsevanos 2014][research_valavanis_vachtsevanos_2014]
- [Valavanis et al][research_valavanis_oh]
- [Vale and Albuquerque 2025][research_vale_albuquerque_2025]
- [Vali 2004][research_vali_2004]
- [Validation and Verification Process][research_validation_and]
- [Vallespin et al 2011][research_vallespin_ronch_2011]
- [Vallot et al 1991][research_vallot_snyder_1991]
- [Van Dierendonck et al 1992][research_vandierendonck_hatch_1992]
- [Van Dyke 1992][research_vandyke_1992]
- [Van et al 2015][research_van_van_2015]
- [Van Gool and Mooij 1979][research_vangool_mooij_1979]
- [Van Gool and Weingarten 1981][research_vangool_weingarten_1981]
- [van Graas 1988][research_vangraas_1988]
- [van Kampen et al 2009][research_vankampen_deweerdt_2009]
- [van Rooij and Cummings 2018][research_vanrooij_cummings_2018]
- [van Rooij et al 2018][research_vanrooij_frink_2018]
- [van Rooij et al 2019][research_vanrooij_frink_2019]
- [van Slagmaat 1992][research_vanslagmaat_1992]
- [van Slagmaat 2004][research_vanslagmaat_2004]
- [van Slagmaat 2026][research_vanslagmaat_2026]
- [Vana and Bisnath 2024][research_vana_bisnath_2024]
- [Vance 1984][research_vance_1984]
- [Vanualailai et al 2013][research_vanualailai_sharan_2013]
- [Variable sweep wing design 1980][research_variable_sweep_1980]
- [Vashishth et al 2024][research_vashishth_sharma_2024]
- [Vehicle Navigation using Carrier 2002][research_vehicle_navigation_2002]
- [Venetsky et al 2003][research_venetsky_husni_2003]
- [Venkata and Jones 2013][research_venkata_jones_2013]
- [Venkatesh 2023][research_venkatesh_2023]
- [Venugopalan et al 2012][research_venugopalan_taher_2012]
- [Vepa 2016][research_vepa_2016]
- [Vepa 2020][research_vepa_2020]
- [Vepa 2023][research_vepa_2023]
- [Vepa 2023][research_vepa_2023_b]
- [Verhagen 2004][research_verhagen_2004]
- [Verhagen 2005][research_verhagen_2005]
- [Verma et al 2021][research_verma_shrinivasan_2021]
- [Vick and Carter 1963][research_vick_carter_1963]
- [Vicory 1968][research_vicory_1968]
- [Vicroy et al 2012][research_vicroy_loeser_2012]
- [Vicroy, Dan D. et al 2014][research_vicroydand_huberkerstinc_2014]
- [Videmsek and de Haag 2020][research_videmsek_dehaag_2020]
- [Videmsek et al 2019][research_videmsek_dehaag_2019]
- [Video Communications in Unmanned 2013][research_video_communications_2013]
- [Vidimlic et al 2021][research_vidimlic_levin_2021]
- [Vieweg][research_vieweg]
- [Vinokurov et al 1992][research_vinokurov_glinkin_1992]
- [Vinokurov et al 1993][research_vinokurov_glinkin_1993]
- [Vishniak 1993][research_vishniak_1993]
- [Visnevski and Castillo-Effen 2010][research_visnevski_castilloeffen_2010]
- [Visual glide slope indicator 1961][research_visual_glide_1961]
- [Vlasov 1969][research_vlasov_1969]
- [Vorobуev et al 2020][research_vorobev_beliatskaya_2020]
- [Vos 2019][research_vos_2019]
- [Vos 2019][research_vos_2019_b]
- [Vos 2019][research_vos_2019_c]
- [Vos et al 2010][research_vos_gurdal_2010]
- [Voss 2018][research_voss_2018]
- [Voss et al 2011][research_voss_cumnuantip_2011]
- [Voß 2019][research_voss_2019]
- [Vrchota 2017][research_vrchota_2017]
- [Vulnerability of Quick-Reacting Sheltered 1959][research_vulnerability_of_1959]
- [WAAS GPS Landing System 2009][research_waas_gps_2009]
- [Wade 2002][research_wade_2002]
- [Wadley et al 2003][research_wadley_tallant_2003]
- [Wagdi 1984][research_wagdi_1984]
- [Waggoner 1999][research_waggoner_1999]
- [Wagner 2005][research_wagner_2005]
- [Wakayama and Kroo 1995][research_wakayama_kroo_1995]
- [Walker 1960][research_walker_1960]
- [Walker 1961][research_walker_1961]
- [Walker 2011][research_walker_2011]
- [Walker 2015][research_walker_2015]
- [Walker 2024][research_walker_2024]
- [Wall 1962][research_wall_1962]
- [Wallace 2000][research_wallace_2000]
- [Walton 1992][research_walton_1992]
- [Wampler et al 1988][research_wampler_myklebust_1988]
- [Wang 2000][research_wang_2000]
- [Wang 2010][research_wang_2010]
- [Wang 2016][research_wang_2016]
- [Wang 2022][research_wang_2022]
- [Wang 2026][research_wang_2026]
- [Wang 2026][research_wang_2026_b]
- [Wang and Carl 1999][research_wang_carl_1999]
- [Wang and Hubbard 2022][research_wang_hubbard_2022]
- [Wang and Jan 2023][research_wang_jan_2023]
- [Wang and McDonald 2019][research_wang_mcdonald_2019]
- [Wang and Ober 2009][research_wang_ober_2009]
- [Wang and Shi 2023][research_wang_shi_2023]
- [Wang and Wang 2012][research_wang_wang_2012]
- [Wang and Wang 2013][research_wang_wang_2013]
- [Wang and Wang 2017][research_wang_wang_2017]
- [Wang and Wang 2018][research_wang_wang_2018]
- [Wang and Wang 2020][research_wang_wang_2020_b]
- [Wang and Xin 2012][research_wang_xin_2012]
- [Wang and Zhan 2005][research_wang_zhan_2005]
- [Wang and Zhao 2022][research_wang_zhao_2022]
- [Wang and Zhou 2022][research_wang_zhou_2022]
- [Wang et al 1996][research_wang_morikawa_1996]
- [Wang et al 2001][research_wang_rizos_2001]
- [Wang et al 2002][research_wang_iz_2002]
- [Wang et al 2005][research_wang_zhang_2005]
- [Wang et al 2006][research_wang_liu_2006]
- [Wang et al 2009][research_wang_miao_2009]
- [Wang et al 2009][research_wang_song_2009]
- [Wang et al 2010][research_wang_deng_2010]
- [Wang et al 2010][research_wang_gong_2010]
- [Wang et al 2011][research_wang_sun_2011]
- [Wang et al 2012][research_wang_yang_2012]
- [Wang et al 2013][research_wang_cui_2013]
- [Wang et al 2013][research_wang_huang_2013]
- [Wang et al 2016][research_wang_chen_2016]
- [Wang et al 2016][research_wang_feng_2016]
- [Wang et al 2016][research_wang_liu_2016]
- [Wang et al 2016][research_wang_zhu_2016]
- [Wang et al 2017][research_wang_li_2017]
- [Wang et al 2018][research_wang_rathinam_2018]
- [Wang et al 2018][research_wang_wu_2018]
- [Wang et al 2018][research_wang_wu_2018_b]
- [Wang et al 2019][research_wang_yao_2019]
- [Wang et al 2019][research_wang_yin_2019]
- [Wang et al 2020][research_wang_fei_2020]
- [Wang et al 2020][research_wang_liu_2020]
- [Wang et al 2020][research_wang_tang_2020]
- [Wang et al 2020][research_wang_wang_2020]
- [Wang et al 2020][research_wang_xuan_2020]
- [Wang et al 2020][research_wang_zhan_2020]
- [Wang et al 2021][research_wang_chen_2021]
- [Wang et al 2021][research_wang_li_2021]
- [Wang et al 2021][research_wang_lu_2021]
- [Wang et al 2021][research_wang_lv_2021]
- [Wang et al 2021][research_wang_meng_2021]
- [Wang et al 2021][research_wang_toth_2021]
- [Wang et al 2021][research_wang_you_2021]
- [Wang et al 2021][research_wang_zhan_2021]
- [Wang et al 2022][research_wang_hou_2022]
- [Wang et al 2022][research_wang_lin_2022]
- [Wang et al 2022][research_wang_mkhoyan_2022]
- [Wang et al 2023][research_wang_liu_2023]
- [Wang et al 2023][research_wang_zhan_2023]
- [Wang et al 2024][research_wang_li_2024]
- [Wang et al 2024][research_wang_yuan_2024]
- [Wang et al 2024][research_wang_zhao_2024]
- [Wang et al 2025][research_wang_ai_2025]
- [Wang et al 2026][research_wang_liu_2026]
- [Wang et al 2026][research_wang_yang_2026]
- [Wanli Xu et al 2012][research_wanlixu_zhunliu_2012]
- [Ward 1983][research_ward_1983]
- [Ward 1994][research_ward_1994]
- [Ward and Costello 2012][research_ward_costello_2012]
- [Ward and Costello 2013][research_ward_costello_2013]
- [Ward et al 1999][research_ward_monaco_1999]
- [Ward et al 2013][research_ward_gavrilovski_2013]
- [Wareyka-Glaner and Möller 2025][research_wareykaglaner_moller_2025]
- [Warner 1970][research_warner_1970]
- [Warner and Lee 2026][research_warner_lee_2026]
- [Warren and Richards 2009][research_warren_richards_2009]
- [Warsch et al 2026][research_warsch_carbone_2026]
- [Wasmi and Rahim 2016][research_wasmi_rahim_2016]
- [Wasser et al 2011][research_wasser_boddhu_2011]
- [Wasserman and Mitchell 1973][research_wasserman_mitchell_1973]
- [Watanabe 2020][research_watanabe_2020]
- [Waterman and Miller 2000][research_waterman_miller_2000]
- [Watson et al 2020][research_watson_owen_2020]
- [Watson et al 2025][research_watson_owen_2025]
- [Wauters 2022][research_wauters_2022]
- [Weaponised Unmanned Air Systems 2013][research_weaponised_unmanned_2013]
- [Weapons Carriage and Guidance 2006][research_weapons_carriage_2006]
- [Web site urges students 2008][research_web_site_2008]
- [Webb 2022][research_webb_2022]
- [Webb and Nolan 1954][research_webb_nolan_1954]
- [Webster 1971][research_webster_1971]
- [Webster et al 2012][research_webster_cameron_2012]
- [Weeks 2000][research_weeks_2000]
- [Wei 2013][research_wei_2013]
- [Wei and Du 2018][research_wei_du_2018]
- [Wei and Schwarz][research_wei_schwarz]
- [Wei et al 2025][research_wei_kang_2025]
- [Wei et al 2026][research_wei_tong_2026]
- [Wei et al 2026][research_wei_zhai_2026]
- [Weight Prediction, Optimization, and 2020][research_weight_prediction_2020]
- [Weijun et al 2008][research_weijun_xiangju_2008]
- [Weinberg 1966][research_weinberg_1966]
- [Weinert et al 1991][research_weinert_richardp_1991]
- [Weingarten 1977][research_weingarten_1977]
- [Weingarten and Chalk 1982][research_weingarten_chalk_1982]
- [Weiss and Shields][research_weiss_shields]
- [Weisshaar 1990][research_weisshaar_1990]
- [Weisshaar 1994][research_weisshaar_1994]
- [Welbourn and Lachance 1961][research_welbourn_lachance_1961]
- [Wells 1993][research_wells_1993]
- [Welterlen 2000][research_welterlen_2000]
- [Weltz and Barajas 2025][research_weltz_barajas_2025]
- [Wen et al 2009][research_wen_zhi_2009]
- [Wen et al 2021][research_wen_pfeifer_2021]
- [Wen et al 2023][research_wen_du_2023]
- [Wendel et al 2005][research_wendel_maier_2005]
- [Wenhu You et al][research_wenhuyou_fuxingjiang]
- [Werner-Westphal et al 2008][research_wernerwestphal_heinze_2008]
- [West 2009][research_west_2009]
- [Westat Inc Rockville Md 2001][research_westatincrockvillemd_2001]
- [Westbrook 1964][research_westbrook_1964]
- [Westra et al 1981][research_westra_simon_1981]
- [Westra et al 1986][research_westra_lintern_1986]
- [Weyl 1944][research_weyl_1944]
- [Weyl 1945][research_weyl_1945]
- [Weyl 1945][research_weyl_1945_b]
- [Wheeler et al 2016][research_wheeler_nyholm_2016]
- [Wheeler et al 2018][research_wheeler_koch_2018]
- [White][research_white]
- [White 1992][research_white_1992]
- [White 2005][research_white_2005]
- [White 2012][research_white_2012]
- [White, Maurice D. and Innis, Robert C. 1959][research_whitemauriced_innisrobertc_1959]
- [Whitehead 1960][research_whitehead_1960]
- [Whitford 1990][research_whitford_1990]
- [Whitford 1991][research_whitford_1991]
- [Whitford 1992][research_whitford_1992]
- [Whitford 1993][research_whitford_1993]
- [Whitford 1994][research_whitford_1994]
- [Why Should We Design][research_why_should]
- [Why should we design 1999][research_why_should_1999]
- [Wiart and Carrier 2010][research_wiart_carrier_2010]
- [Wick][research_wick]
- [Wide-Body and Standard-Body Aircraft][research_wide_body_and]
- [Widnall et al 1982][research_widnall_gobbini_1982]
- [Wiederholt and Klein 1984][research_wiederholt_klein_1984]
- [Wieland et al 2013][research_wieland_sharma_2013]
- [Wilcox et al 2010][research_wilcox_mackunis_2010]
- [Wildermuth et al 1974][research_wildermuth_rothammer_1974]
- [Wildermuth et al 1974][research_wildermuth_rothammer_1974_b]
- [Wilhelm and Schafranek 1986][research_wilhelm_schafranek_1986]
- [Wilhem 1970][research_wilhem_1970]
- [Willebeek-LeMair and Rhinehart 2023][research_willebeeklemair_rhinehart_2023]
- [Williams and Trivailo 2006][research_williams_trivailo_2006]
- [Williams and Trivailo 2006][research_williams_trivailo_2006_b]
- [Williams et al 2000][research_williams_davis_2000]
- [Williams et al 2025][research_williams_niestroy_2025]
- [Williamson 1966][research_williamson_1966]
- [Willis][research_willis]
- [Wills 2015][research_wills_2015]
- [Wills 2015][research_wills_2015_b]
- [Wilsbach 1998][research_wilsbach_1998]
- [Wilson 2018][research_wilson_2018]
- [Wilson et al 2014][research_wilson_goktogan_2014]
- [Wilson et al 2015][research_wilson_goktogan_2015]
- [Wilson, S. B., III 1992][research_wilsonsbiii_1992]
- [Wilt et al 2022][research_wilt_hicks_2022]
- [Wing Design 2012][research_wing_design_2012]
- [Wings 2017][research_wings_2017]
- [Winter et al 2021][research_winter_robinson_2021]
- [Wise 1990][research_wise_1990]
- [Wise 2003][research_wise_2003]
- [Wise 2004][research_wise_2004]
- [Wiser 2009][research_wiser_2009]
- [Witherell 1992][research_witherell_1992]
- [Wittenberg 2001][research_wittenberg_2001]
- [Woelk 1989][research_woelk_1989]
- [Wolf et al 2016][research_wolf_shelley_2016]
- [Wolfe 1976][research_wolfe_1976]
- [Wolfe and Speyer 2004][research_wolfe_speyer_2004]
- [Wolfe et al 2003][research_wolfe_williamson_2003]
- [Wolff 2022][research_wolff_2022]
- [Wolff et al 1988][research_wolff_lohr_1988]
- [Woo et al 2022][research_woo_choi_2022]
- [Woods 1994][research_woods_1994]
- [Woods and Daines 2003][research_woods_daines_2003]
- [Worked Manned Aircraft Detail 2017][research_worked_manned_2017]
- [Wortman 1981][research_wortman_1981]
- [Wortmann et al 2015][research_wortmann_hoogreef_2015]
- [Wrenn and Dovi 1988][research_wrenn_dovi_1988]
- [Wright 2005][research_wright_2005]
- [Wright and Barry 2014][research_wright_barry_2014]
- [Wright and Burton 1991][research_wright_burton_1991]
- [wu 2017][research_wu_2017]
- [Wu and Lin 2026][research_wu_lin_2026]
- [Wu and Mora-Camino 2012][research_wu_moracamino_2012]
- [Wu and Mueller 2018][research_wu_mueller_2018]
- [Wu and Zhu 2024][research_wu_zhu_2024]
- [Wu et al 2008][research_wu_peck_2008]
- [Wu et al 2017][research_wu_gu_2017]
- [Wu et al 2018][research_wu_song_2018]
- [Wu et al 2018][research_wu_zhang_2018]
- [Wu et al 2023][research_wu_luo_2023]
- [Wu et al 2023][research_wu_lv_2023]
- [Wu et al 2024][research_wu_wang_2024]
- [Wu et al 2026][research_wu_wang_2026]
- [Wu et al 2026][research_wu_zhu_2026]
- [Wyatt 2003][research_wyatt_2003]
- [Wynn and McLain 2019][research_wynn_mclain_2019]
- [Wynnyk et al 2017][research_wynnyk_lunsford_2017]
- [Xi and Liu 2020][research_xi_liu_2020]
- [Xi and Zhao 2017][research_xi_zhao_2017]
- [Xia 2004][research_xia_2004]
- [Xia et al 2016][research_xia_dong_2016]
- [Xia et al 2025][research_xia_wu_2025]
- [Xiang Jin and de Jong 1996][research_xiangjin_dejong_1996]
- [Xiao 2008][research_xiao_2008]
- [Xiao et al 2024][research_xiao_zhen_2024]
- [Xiaofeng et al 2020][research_xiaofeng_daqian_2020]
- [Xie and Haberland 1999][research_xie_haberland_1999]
- [Xie et al 2011][research_xie_yang_2011]
- [Xie et al 2019][research_xie_cai_2019]
- [Xie et al 2019][research_xie_dong_2019]
- [Xie et al 2023][research_xie_huang_2023]
- [Xie et al 2026][research_xie_jia_2026]
- [Xie et al 2026][research_xie_jia_2026_b]
- [Xie et al 2026][research_xie_jia_2026_c]
- [Xie et al 2026][research_xie_jia_2026_d]
- [Xie et al 2026][research_xie_jia_2026_e]
- [Xie et al 2026][research_xie_jia_2026_f]
- [Xie et al 2026][research_xie_jia_2026_g]
- [Xin et al 2018][research_xin_luo_2018]
- [Xiong et al 2022][research_xiong_zhou_2022]
- [Xu 2002][research_xu_2002]
- [Xu 2013][research_xu_2013]
- [Xu 2018][research_xu_2018]
- [Xu 2025][research_xu_2025]
- [Xu and Carrillo 2015][research_xu_carrillo_2015]
- [Xu and Morton 2018][research_xu_morton_2018]
- [Xu and Shi 2013][research_xu_shi_2013]
- [Xu et al 2010][research_xu_li_2010]
- [Xu et al 2012][research_xu_shi_2012]
- [Xu et al 2013][research_xu_liu_2013]
- [Xu et al 2017][research_xu_zhao_2017]
- [Xu et al 2018][research_xu_zhang_2018]
- [Xu et al 2019][research_xu_han_2019]
- [Xu et al 2020][research_xu_huang_2020]
- [Xu et al 2021][research_xu_liu_2021]
- [Xu et al 2022][research_xu_shen_2022]
- [Xu et al 2025][research_xu_hong_2025]
- [Xuan Zhao et al 2016][research_xuanzhao_zhong_2016]
- [Xue and Atkins 2003][research_xue_atkins_2003]
- [Xue and Do 2019][research_xue_do_2019]
- [Xue et al 2011][research_xue_zhao_2011]
- [Xue et al 2023][research_xue_zhen_2023]
- [Xue et al 2024][research_xue_huang_2024]
- [Yacef et al 2014][research_yacef_bouhali_2014]
- [Yadav and Shukla 2012][research_yadav_shukla_2012]
- [Yadav et al 2017][research_yadav_shanmukha_2017]
- [Yakimenko et al 2002][research_yakimenko_kaminer_2002]
- [Yakovlev et al 2020][research_yakovlev_bakulin_2020]
- [Yan and Zhao 2014][research_yan_zhao_2014]
- [Yan et al 2018][research_yan_xunhua_2018]
- [Yan et al 2025][research_yan_zhang_2025]
- [Yanagihara et al 1999][research_yanagihara_shigemi_1999]
- [Yang 1970][research_yang_1970]
- [Yang 1971][research_yang_1971]
- [Yang 2013][research_yang_2013]
- [Yang 2024][research_yang_2024]
- [Yang and Mischel 1995][research_yang_mischel_1995]
- [Yang et al 2001][research_yang_chang_2001]
- [Yang et al 2010][research_yang_garratt_2010]
- [Yang et al 2013][research_yang_li_2013]
- [Yang et al 2013][research_yang_zheng_2013]
- [Yang et al 2016][research_yang_jiang_2016]
- [Yang et al 2018][research_yang_duan_2018]
- [Yang et al 2018][research_yang_shi_2018]
- [Yang et al 2021][research_yang_nita_2021]
- [Yang et al 2023][research_yang_zhang_2023]
- [Yang et al 2023][research_yang_zhang_2023_b]
- [Yang et al 2023][research_yang_zheng_2023]
- [Yang et al 2024][research_yang_yang_2024]
- [Yang et al 2024][research_yang_zhu_2024]
- [Yang et al 2025][research_yang_wan_2025]
- [Yang et al 2026][research_yang_jiang_2026]
- [Yang et al 2026][research_yang_shou_2026]
- [Yang et al 2026][research_yang_song_2026]
- [Yanushevsky 2026][research_yanushevsky_2026]
- [Yanushevsky 2026][research_yanushevsky_2026_b]
- [Yanushevsky 2026][research_yanushevsky_2026_c]
- [Yao et al 2018][research_yao_wang_2018]
- [Yao et al 2024][research_yao_kan_2024]
- [Yao et al 2025][research_yao_li_2025]
- [Yao et al 2025][research_yao_li_2025_b]
- [Yardley et al 2008][research_yardley_kallimani_2008]
- [Yarygina and Popov 2012][research_yarygina_popov_2012]
- [Yasuda 2025][research_yasuda_2025]
- [Yavnai 2003][research_yavnai_2003]
- [Yawei Liang][research_yaweiliang]
- [Ye and Zheng 2025][research_ye_zheng_2025]
- [Ye et al 2022][research_ye_zhang_2022]
- [Ye et al 2023][research_ye_gu_2023]
- [Yen 1982][research_yen_1982]
- [Yerger 2006][research_yerger_2006]
- [Yilmaz and alaiwi 2024][research_yilmaz_alaiwi_2024]
- [Yilmaz et al 2019][research_yilmaz_warren_2019]
- [Yin et al 2020][research_yin_fan_2020]
- [Yin et al 2023][research_yin_gu_2023]
- [Yin et al 2025][research_yin_ni_2025]
- [Yin et al 2025][research_yin_teunissen_2025]
- [Yoakum and Cerreta 2020][research_yoakum_cerreta_2020]
- [Yogeshwaran][research_yogeshwaran]
- [Yomchinda 2015][research_yomchinda_2015]
- [Yong Jiang et al 2006][research_yongjiang_jiecao_2006]
- [Yoo et al 2013][research_yoo_cho_2013]
- [Yoo et al 2014][research_yoo_chihoonlee_2014]
- [Yoo et al 2015][research_yoo_park_2015]
- [Yoo et al 2021][research_yoo_park_2021]
- [Yoon and Lundberg 2002][research_yoon_lundberg_2002]
- [Yoon et al 2004][research_yoon_nerem_2004]
- [York and Pack 2011][research_york_pack_2011]
- [You and Shim 2010][research_you_shim_2010]
- [Young 1997][research_young_1997]
- [Young 2000][research_young_2000]
- [Young Jr 2002][research_youngjr_2002]
- [Yu and Chen 2010][research_yu_chen_2010]
- [Yu and Chen 2011][research_yu_chen_2011]
- [Yu and Du 2006][research_yu_du_2006]
- [Yu and Liu 2019][research_yu_liu_2019]
- [Yu et al 2017][research_yu_hua_2017]
- [Yu et al 2018][research_yu_qu_2018]
- [Yu et al 2019][research_yu_he_2019]
- [Yu et al 2020][research_yu_yang_2020]
- [Yu et al 2022][research_yu_hu_2022]
- [Yu et al 2023][research_yu_li_2023]
- [Yu et al 2024][research_yu_li_2024]
- [Yuan][research_yuan]
- [Yuan and Bao 2012][research_yuan_bao_2012]
- [Yuan et al 2011][research_yuan_xi_2011]
- [Yuan et al 2011][research_yuan_yuan_2011]
- [Yuan et al 2014][research_yuan_xing_2014]
- [Yuan et al 2017][research_yuan_zhao_2017]
- [Yuan et al 2024][research_yuan_duan_2024]
- [Yuan et al 2025][research_yuan_wang_2025]
- [Yuan et al 2026][research_yuan_xue_2026]
- [Yue et al 2009][research_yue_wang_2009]
- [Yue et al 2013][research_yue_wang_2013]
- [Yue et al 2013][research_yue_wang_2013_b]
- [Yue et al 2016][research_yue_liu_2016]
- [Yue et al 2017][research_yue_lian_2017]
- [Yukihiro et al 2000][research_yukihiro_akihiko_2000]
- [Yukish and Valenti 2020][research_yukish_valenti_2020]
- [Yuma Proving Ground Az 2013][research_yumaprovinggroundaz_2013]
- [Yuma Test Center Yuma Proving Ground Az 2008][research_yumatestcenteryumaprovinggroundaz_2008]
- [Zadniprovsky and Konotop 2025][research_zadniprovsky_konotop_2025]
- [Zafi and Chakraborty 2023][research_zafi_chakraborty_2023]
- [Zaimis et al 2024][research_zaimis_carpentari_2024]
- [Zakrajsek et al 2017][research_zakrajsek_vogel_2017]
- [Zandberg 2001][research_zandberg_2001]
- [Zandbergen and Barbeau 2011][research_zandbergen_barbeau_2011]
- [Zappa and Gordon 2011][research_zappa_gordon_2011]
- [Załęski 2018][research_zaeski_2018]
- [Zehner 2001][research_zehner_2001]
- [Zelenkov and Golik 2014][research_zelenkov_golik_2014]
- [Zeng et al 2025][research_zeng_li_2025]
- [Zhai et al 2012][research_zhai_qi_2012]
- [Zhai et al 2025][research_zhai_li_2025]
- [Zhang 2018][research_zhang_2018]
- [Zhang 2021][research_zhang_2021]
- [Zhang 2025][research_zhang_2025]
- [Zhang and Guo 2024][research_zhang_guo_2024]
- [Zhang and He 2026][research_zhang_he_2026]
- [Zhang and He 2026][research_zhang_he_2026_b]
- [Zhang and Li 2023][research_zhang_li_2023]
- [Zhang and Mehrjerdi 2013][research_zhang_mehrjerdi_2013]
- [Zhang and Morton 2013][research_zhang_morton_2013]
- [Zhang and Qin 2026][research_zhang_qin_2026]
- [Zhang and Wang 2023][research_zhang_wang_2023_b]
- [Zhang and Wang 2023][research_zhang_wang_2023_c]
- [Zhang and Yang 2013][research_zhang_yang_2013]
- [Zhang and Zhang 2020][research_zhang_zhang_2020]
- [Zhang and Zhang 2022][research_zhang_zhang_2022]
- [Zhang and Zhao 2023][research_zhang_zhao_2023]
- [Zhang and Zhu 2025][research_zhang_zhu_2025]
- [Zhang et al 2008][research_zhang_yang_2008]
- [Zhang et al 2012][research_zhang_niu_2012]
- [Zhang et al 2012][research_zhang_zhang_2012]
- [Zhang et al 2013][research_zhang_cui_2013]
- [Zhang et al 2014][research_zhang_zou_2014]
- [Zhang et al 2015][research_zhang_lin_2015]
- [Zhang et al 2016][research_zhang_liu_2016]
- [Zhang et al 2016][research_zhang_zhao_2016]
- [Zhang et al 2017][research_zhang_li_2017]
- [Zhang et al 2017][research_zhang_shan_2017]
- [Zhang et al 2018][research_zhang_shuang_2018]
- [Zhang et al 2019][research_zhang_zhai_2019]
- [Zhang et al 2019][research_zhang_zhai_2019_b]
- [Zhang et al 2020][research_zhang_li_2020]
- [Zhang et al 2020][research_zhang_zhang_2020_b]
- [Zhang et al 2021][research_zhang_su_2021]
- [Zhang et al 2021][research_zhang_wang_2021]
- [Zhang et al 2022][research_zhang_chai_2022]
- [Zhang et al 2022][research_zhang_peng_2022]
- [Zhang et al 2022][research_zhang_peng_2022_b]
- [Zhang et al 2022][research_zhang_zhang_2022_b]
- [Zhang et al 2023][research_zhang_chen_2023]
- [Zhang et al 2023][research_zhang_huang_2023]
- [zhang et al 2023][research_zhang_lin_2023]
- [Zhang et al 2023][research_zhang_wang_2023]
- [Zhang et al 2023][research_zhang_wang_2023_d]
- [Zhang et al 2023][research_zhang_yang_2023]
- [Zhang et al 2023][research_zhang_zhang_2023]
- [Zhang et al 2024][research_zhang_dou_2024]
- [Zhang et al 2024][research_zhang_li_2024]
- [Zhang et al 2025][research_zhang_ma_2025]
- [Zhang et al 2025][research_zhang_song_2025]
- [Zhang et al 2025][research_zhang_wang_2025]
- [Zhang et al 2025][research_zhang_wang_2025_b]
- [Zhang et al 2025][research_zhang_zhao_2025]
- [Zhang et al 2026][research_zhang_chen_2026]
- [Zhang et al 2026][research_zhang_chen_2026_b]
- [Zhang et al 2026][research_zhang_fang_2026]
- [Zhang et al 2026][research_zhang_yang_2026]
- [Zhao and Kapania 2019][research_zhao_kapania_2019]
- [Zhao and Zhu 2016][research_zhao_zhu_2016]
- [Zhao et al 2012][research_zhao_li_2012]
- [Zhao et al 2016][research_zhao_qiu_2016]
- [Zhao et al 2017][research_zhao_li_2017]
- [Zhao et al 2018][research_zhao_currier_2018]
- [Zhao et al 2018][research_zhao_krishnamurthi_2018]
- [Zhao et al 2018][research_zhao_krishnamurthi_2018_b]
- [Zhao et al 2019][research_zhao_mishra_2019]
- [Zhao et al 2021][research_zhao_duan_2021]
- [Zhao et al 2023][research_zhao_khanafseh_2023]
- [Zhao et al 2023][research_zhao_liu_2023]
- [Zhao et al 2023][research_zhao_zeng_2023]
- [Zhao et al 2024][research_zhao_zhou_2024]
- [Zhen et al 2018][research_zhen_tao_2018]
- [Zhen et al 2019][research_zhen_peng_2019]
- [Zhen et al 2020][research_zhen_yu_2020]
- [Zheng et al 2013][research_zheng_gong_2013]
- [Zheng et al 2014][research_zheng_qiaoqiao_2014]
- [Zheng et al 2019][research_zheng_wang_2019]
- [Zheng et al 2026][research_zheng_qu_2026]
- [Zhicong and Voronko 2023][research_zhicong_voronko_2023]
- [Zhijin Zhao et al 2006][research_zhijinzhao_qigao_2006]
- [Zhilan Xiong et al][research_zhilanxiong_yanlinghao]
- [Zhimin and Guanxin 2008][research_zhimin_guanxin_2008]
- [Zhimin and Guanxin 2013][research_zhimin_guanxin_2013]
- [Zhimin and Guanxin 2013][research_zhimin_guanxin_2013_b]
- [Zhimin and Guanxin 2014][research_zhimin_guanxin_2014]
- [Zhiqiang and Wu 2017][research_zhiqiang_wu_2017]
- [ZhiWen et al 2013][research_zhiwen_xiaoping_2013]
- [Zhong et al 2018][research_zhong_xu_2018]
- [Zhong et al 2018][research_zhong_xu_2018_b]
- [Zhongfei and Lijun 2025][research_zhongfei_lijun_2025]
- [Zhou 2016][research_zhou_2016]
- [Zhou and Huang 2020][research_zhou_huang_2020]
- [Zhou and Wang 2023][research_zhou_wang_2023]
- [Zhou et al 2010][research_zhou_knedlik_2010]
- [Zhou et al 2011][research_zhou_yang_2011]
- [Zhou et al 2015][research_zhou_bao_2015]
- [Zhou et al 2017][research_zhou_jiang_2017]
- [Zhou et al 2017][research_zhou_wan_2017]
- [Zhou et al 2018][research_zhou_zeng_2018]
- [Zhou et al 2019][research_zhou_huang_2019]
- [Zhou et al 2020][research_zhou_kuang_2020]
- [Zhou et al 2022][research_zhou_dong_2022]
- [Zhou et al 2022][research_zhou_wang_2022]
- [Zhou et al 2022][research_zhou_zhang_2022]
- [Zhou et al 2023][research_zhou_dong_2023]
- [Zhou et al 2024][research_zhou_liu_2024]
- [Zhou et al 2024][research_zhou_zhang_2024]
- [Zhu 2024][research_zhu_2024]
- [Zhu and Qiu 2013][research_zhu_qiu_2013]
- [Zhu and Yang 2020][research_zhu_yang_2020]
- [Zhu Bin et al 2018][research_zhubin_kepeng_2018]
- [Zhu et al 2006][research_zhu_lai_2006]
- [Zhu et al 2012][research_zhu_zhao_2012]
- [Zhu et al 2016][research_zhu_jin_2016]
- [Zhu et al 2017][research_zhu_zhang_2017]
- [Zhu et al 2018][research_zhu_lu_2018]
- [Zhu et al 2019][research_zhu_lu_2019]
- [Zhu et al 2020][research_zhu_lung_2020]
- [Zhu et al 2022][research_zhu_zhang_2022]
- [Zhu et al 2023][research_zhu_shi_2023]
- [Zhu et al 2025][research_zhu_bordner_2025]
- [Zhu et al 2026][research_zhu_zhu_2026]
- [Zhu Qi-dan et al 2009][research_zhuqidan_wangtong_2009]
- [Zhu Qi-dan et al 2009][research_zhuqidan_wangtong_2009_b]
- [Zink][research_zink]
- [Zolanvari et al 2018][research_zolanvari_teixeira_2018]
- [Zou and Devasia 2000][research_zou_devasia_2000]
- [Zou and Devasia 2006][research_zou_devasia_2006]
- [Zou et al 2017][research_zou_yin_2017]
- [Zou et al 2020][research_zou_song_2020]
- [Zou et al 2026][research_zou_zhen_2026]
- [Zuo et al 2023][research_zuo_xu_2023]
- [Zvyagina and Mordovin 2026][research_zvyagina_mordovin_2026]
- [Çakıcı and Leblebicioğlu 2016][research_cakici_leblebicioglu_2016]
- [Çoban 2020][research_coban_2020]
- [Çoban and Oktay 2018][research_coban_oktay_2018]
- [Çoban and Oktay 2018][research_coban_oktay_2018_b]
- [Ünal et al 2023][research_unal_oz_2023]
- [Čápek 1995][research_capek_1995]
- [Şugar Gabor et al 2016][research_sugargabor_koreanschi_2016]

[research_a340_600_wing_2002]: https://doi.org/10.1108/aeat.2002.12774eaf.003
[research_a_prediction_2017]: https://doi.org/10.18494/sam.2017.1588
[research_a_psychological_1972]: https://doi.org/10.1016/s0003-6870(72)80032-2
[research_a_testing_1950]: https://doi.org/10.1016/0016-0032(50)90496-0
[research_aamir_benhamida_2026]: https://doi.org/10.2514/1.c038961
[research_abas_pebrianti_2013]: https://doi.org/10.1007/978-4-431-54276-6_8
[research_abbasi_haeri_2019]: https://doi.org/10.1109/iccia49288.2019.9030830
[research_abdelhafez_lee_2003]: https://doi.org/10.1002/j.2161-4296.2003.tb00336.x
[research_abdelhafez_speyer_2004]: https://doi.org/10.1002/j.2161-4296.2004.tb00354.x
[research_abdelrahman_elnomrossy_2009]: https://doi.org/10.2514/6.2009-1970
[research_abouheaf_mailhot_2019]: https://doi.org/10.1109/rose.2019.8790425
[research_abouzahr_jacob_2023]: https://doi.org/10.2514/6.2023-4459
[research_abuakeel_1968]: https://doi.org/10.2514/6.1968-312
[research_abuakeel_1969]: https://doi.org/10.2514/3.43996
[research_aburime]: https://doi.org/10.22215/etd/2018-13444
[research_abwanzo_2016]: https://doi.org/10.2139/ssrn.2861230
[research_acerragil_guimaraes_2019]: https://doi.org/10.26678/abcm.cobem2019.cob2019-0694
[research_acharya_sinha_2021]: https://doi.org/10.1109/iria53009.2021.9588696
[research_acosta_decos_2016]: https://doi.org/10.1109/icuas.2016.7502675
[research_acuna_zhang_2018]: https://doi.org/10.1109/lars/sbr/wre.2018.00096
[research_adams_2000]: https://doi.org/10.21236/ada378302
[research_adams_hatchjr_1970]: https://doi.org/10.2514/6.1970-568
[research_adams_moen_1967]: https://doi.org/10.2514/6.1967-617
[research_adamski_2021]: https://doi.org/10.3846/aviation.2021.13391
[research_adelgren_minor_2004]: https://doi.org/10.21236/ada428090
[research_adhikari_2021]: https://doi.org/10.32920/16636006.v1
[research_adhikari_2021_b]: https://doi.org/10.32920/ryerson.14668500
[research_advanced_aircraft_2026]: https://doi.org/10.1017/9781009399913.014
[research_aerodynamic_data_2010]: https://doi.org/10.2514/5.9781600867538.0733.0744
[research_aerodynamics_2024]: https://doi.org/10.2514/5.9781624107290.0403.0486
[research_aerospace_id_2006]: https://doi.org/10.1108/aeat.2006.12778aab.021
[research_aerospace_landing]: https://doi.org/10.4271/air1489
[research_aerospace_quality_2004]: https://doi.org/10.1108/aeat.2004.12776aae.002
[research_aerospace_series]: https://doi.org/10.3403/bsen4709
[research_aerospace_series_b]: https://doi.org/10.3403/30286292
[research_aerospace_series_c]: https://doi.org/10.3403/30505104u
[research_aerospace_series_d]: https://doi.org/10.3403/30293259
[research_aerospace_series_e]: https://doi.org/10.3403/30487417u
[research_aerospace_series_f]: https://doi.org/10.3403/30293259u
[research_aerospace_series_g]: https://doi.org/10.3403/30304490
[research_aerospace_series_h]: https://doi.org/10.3403/30487414u
[research_aerospace_series_i]: https://doi.org/10.3403/30498294u
[research_aerospace_series_j]: https://doi.org/10.3403/30487411u
[research_aerospace_series_k]: https://doi.org/10.3403/30396190u
[research_aerospace_supplier_2004]: https://doi.org/10.1108/aeat.2004.12776baf.002
[research_aftatah_khalil_2026]: https://doi.org/10.1109/access.2026.3659348
[research_aftatah_zebbara_2024]: https://doi.org/10.56294/dm2024.405
[research_agarwal_arya_2008]: https://doi.org/10.1504/ijidss.2008.020271
[research_agarwal_ng_2021]: https://doi.org/10.1109/icuas51884.2021.9476830
[research_agenbag_theron_2009]: https://doi.org/10.2514/1.39755
[research_agrawal_1984]: https://doi.org/10.1115/84-gt-163
[research_agrawal_rai_2025]: https://doi.org/10.52202/080560-0028
[research_agte_hadley_1997]: https://doi.org/10.4271/975636
[research_aguiar_pascoal_2012]: https://doi.org/10.1049/pbce077e_ch12
[research_ahlrich_1991]: https://doi.org/10.21236/ada238954
[research_ahmad_narmeen_2026]: https://doi.org/10.1007/978-981-96-9662-8_1
[research_ahmed_stanziano_2026]: https://doi.org/10.2514/6.2026-4752
[research_ahn_kim_2022]: https://doi.org/10.32956/kopoms.2022.33.3.611
[research_air_cargo]: https://doi.org/10.3403/00416635
[research_air_cargo_b]: https://doi.org/10.3403/00477960
[research_air_cargo_c]: https://doi.org/10.3403/00309415
[research_air_to_air_air_to_ground_weapons_2010]: https://doi.org/10.1049/sbra033e_ch10
[research_airborne_landing]: https://doi.org/10.4271/arp4102/12a
[research_airborne_windshear]: https://doi.org/10.4271/arp4102/11b
[research_aircombatcommand_2011]: https://doi.org/10.21236/ada640064
[research_aircombatcommandlangleyafbva_2000]: https://doi.org/10.21236/ada451627
[research_aircombatcommandlangleyafbva_2013]: https://doi.org/10.21236/ada607877
[research_aircraft_automatic_1996]: https://doi.org/10.2514/5.9781600866395.0397.0425
[research_aircraft_carrier_1987]: https://doi.org/10.1016/0025-326x(87)90231-1
[research_aircraft_carrier_2005]: https://doi.org/10.4135/9781412952446.n10
[research_aircraft_case_2026]: https://doi.org/10.1017/9781009399913.020
[research_aircraft_characteristics_2022]: https://doi.org/10.1002/9781119988281.ch6
[research_aircraft_circuit]: https://doi.org/10.4271/arp4101/5a
[research_aircraft_conceptual_2012]: https://doi.org/10.1002/9781118352700.ch3
[research_aircraft_control_2011]: https://doi.org/10.1201/9781315252988-14
[research_aircraft_cost_2010]: https://doi.org/10.1017/cbo9780511844652.018
[research_aircraft_declaration]: https://doi.org/10.3403/01376393
[research_aircraft_design_1993]: https://doi.org/10.2514/6.1993-4007
[research_aircraft_design_2012]: https://doi.org/10.1002/9781118352700.ch1
[research_aircraft_design_2013]: https://doi.org/10.1002/9781118568101.ch7
[research_aircraft_design_2024]: https://doi.org/10.2514/5.9781624107290.0000.0000
[research_aircraft_drag_2010]: https://doi.org/10.1017/cbo9780511844652.011
[research_aircraft_dynamics_2015]: https://doi.org/10.1002/9781119174882.ch4
[research_aircraft_flight_2014]: https://doi.org/10.1201/b17346-12
[research_aircraft_flotation]: https://doi.org/10.4271/air1780
[research_aircraft_flotation_b]: https://doi.org/10.4271/arp1821
[research_aircraft_ground]: https://doi.org/10.4271/arp1821a
[research_aircraft_ground_b]: https://doi.org/10.3403/30082925
[research_aircraft_ground_c]: https://doi.org/10.3403/30083343
[research_aircraft_ground_d]: https://doi.org/10.3403/30149695
[research_aircraft_ground_e]: https://doi.org/10.3403/30153939u
[research_aircraft_ground_f]: https://doi.org/10.3403/30083339
[research_aircraft_improvement_2002]: https://doi.org/10.1108/aeat.2002.12774daf.005
[research_aircraft_landing]: https://doi.org/10.4271/arp1311a
[research_aircraft_landing_1971]: https://doi.org/10.1108/eb034716
[research_aircraft_lateral_directional_2011]: https://doi.org/10.1049/pbce074e_ch9
[research_aircraft_load_2010]: https://doi.org/10.1017/cbo9780511844652.007
[research_aircraft_longitudinal_2011]: https://doi.org/10.1049/pbce074e_ch10
[research_aircraft_manufacturing_2010]: https://doi.org/10.1017/cbo9780511844652.019
[research_aircraft_mechanics_2026]: https://doi.org/10.1017/9781009399913.002
[research_aircraft_non_linear_2014]: https://doi.org/10.1201/b17346-8
[research_aircraft_operating_2010]: https://doi.org/10.2514/5.9781600867538.0101.0122
[research_aircraft_oxygen]: https://doi.org/10.4271/as1219a
[research_aircraft_passenger]: https://doi.org/10.3403/30192426
[research_aircraft_payload_1970]: https://doi.org/10.7249/d20322
[research_aircraft_performance_2010]: https://doi.org/10.2514/5.9781600867538.0071.0100
[research_aircraft_performance_2010_b]: https://doi.org/10.1017/cbo9780511844652.015
[research_aircraft_performance_2026]: https://doi.org/10.1017/9781009399913.006
[research_aircraft_prototype_1983]: https://doi.org/10.2514/maptds83
[research_aircraft_response_1997]: https://doi.org/10.1016/b978-0-340-63200-0.50020-4
[research_aircraft_response_2013]: https://doi.org/10.1016/b978-0-08-098242-7.00026-2
[research_aircraft_seat]: https://doi.org/10.4271/arp5526e
[research_aircraft_simulation_2022]: https://doi.org/10.1002/9781119988281.ch7
[research_aircraft_sizing_2010]: https://doi.org/10.1017/cbo9780511844652.013
[research_aircraft_stability_1998]: https://doi.org/10.2514/5.9781600862052.0333.0354
[research_aircraft_stability_2026]: https://doi.org/10.1017/9781009399913.010
[research_aircraft_tire]: https://doi.org/10.4271/air4830a
[research_aircraft_tire_b]: https://doi.org/10.4271/air4830
[research_aircraft_tires_2022]: https://doi.org/10.4271/9781468604641
[research_aircraft_weight_2010]: https://doi.org/10.1017/cbo9780511844652.010
[research_aircraft_weight_2012]: https://doi.org/10.1002/9781118352700.ch11
[research_aircraft_weights_2010]: https://doi.org/10.2514/5.9781600867538.0759.0784
[research_aircraft_wheels_2022]: https://doi.org/10.4271/9781468604702
[research_aircraft_with_2001]: https://doi.org/10.1108/aeat.2001.12773dad.007
[research_airfoil_and_2024]: https://doi.org/10.2514/5.9781624107290.0055.0118
[research_airforcedistrictofwashington_2015]: https://doi.org/10.21236/ada628457
[research_airframe_avionics_2017]: https://doi.org/10.1002/9781119406303.ch6
[research_airprovinggroundcentereglinafbfl_1944]: https://doi.org/10.21236/adb972097
[research_airprovinggroundcentereglinafbfl_1949]: https://doi.org/10.21236/adb971411
[research_airprovinggroundcentereglinafbfl_1954]: https://doi.org/10.21236/adb193040
[research_airprovinggroundcentereglinafbfl_1954_b]: https://doi.org/10.21236/ad0031528
[research_airprovinggroundcentereglinafbfl_1955]: https://doi.org/10.21236/adb191132
[research_airprovinggroundcentereglinafbfl_1955_b]: https://doi.org/10.21236/ad0068388
[research_airunivmaxwellafbal_1978]: https://doi.org/10.21236/ada542272
[research_ajaj_friswell_2013]: https://doi.org/10.1017/s0001924000008174
[research_akagi_christensen_2020]: https://doi.org/10.1109/plans46316.2020.9110194
[research_akagi_mclain_2025]: https://doi.org/10.2514/6.2025-1539
[research_akca_demirekler_2012]: https://doi.org/10.1109/plans.2012.6236907
[research_alaeiyan_mosavi_2026]: https://doi.org/10.1016/j.rineng.2026.109856
[research_alam_nguyen_2011]: https://doi.org/10.2514/1.c031241
[research_alarcon_santamaria_2015]: https://doi.org/10.1016/j.ifacol.2015.08.056
[research_aldrich_krabill_1972]: https://doi.org/10.2514/6.1972-838
[research_ale_a_carrier_1977]: https://doi.org/10.1016/0026-2714(77)90045-2
[research_aleisa_kontis_2023]: https://doi.org/10.2514/1.c037257
[research_aleisa_kontis_2023_b]: https://doi.org/10.2514/1.c037258
[research_alexander_2025]: https://doi.org/10.4050/sm_handling_2025-5295
[research_alexander_2025_b]: https://doi.org/10.4050/sm_handling_2025-5289
[research_alexander_nygren_2000]: https://doi.org/10.21236/ada387207
[research_alexandrov_kazakov_1980]: https://doi.org/10.1016/b978-0-08-024449-5.50044-8
[research_alexopoulos_kirsch_2017]: https://doi.org/10.1109/icuas.2017.7991416
[research_alford_1999]: https://doi.org/10.21236/ada372248
[research_alhiddabi_mcclamroch_2002]: https://doi.org/10.2514/2.4871
[research_alhosban_2019]: https://doi.org/10.32567/hm.2019.4.10
[research_ali_abbas_2024]: https://doi.org/10.31026/j.eng.2024.09.09
[research_ali_alshamma_2026]: https://doi.org/10.1017/aer.2026.10184
[research_ali_jiancheng_2005]: https://doi.org/10.2514/6.2005-6452
[research_alidehghani_baghermenhaj_2016]: https://doi.org/10.1108/aa-09-2015-074
[research_alijani_osman_2021]: https://doi.org/10.1109/icuas51884.2021.9476875
[research_alipour_shahiashtiani_2022]: https://doi.org/10.1108/aeat-07-2020-0130
[research_allard_1982]: https://doi.org/10.21236/ada119455
[research_allen]: https://doi.org/10.33915/etd.559
[research_allen_2009]: https://doi.org/10.21236/ada509844
[research_allen_breitsamter_2008]: https://doi.org/10.2514/1.34995
[research_allendealba_montenbruck_2018]: https://doi.org/10.1007/s10291-018-0734-x
[research_alley_steele_2010]: https://doi.org/10.2514/6.2010-3450
[research_almagbile_wang_2010]: https://doi.org/10.5081/jgps.9.1.33
[research_alonsodasilva_2019]: https://doi.org/10.4271/epr2019012
[research_alsayed_nabawy_2022]: https://doi.org/10.2514/6.2022-4062
[research_altman_2008]: https://doi.org/10.21236/ada494088
[research_altman_2015]: https://doi.org/10.2514/6.2015-1012
[research_altman_2019]: https://doi.org/10.2514/6.2019-0068
[research_altmann_2013]: https://doi.org/10.2514/6.2013-1345
[research_altynova_wasser_2011]: https://doi.org/10.21236/ada567803
[research_aluc_komurgoz_2023]: https://doi.org/10.1007/978-3-031-29933-9_3
[research_alvarez_wissa_2021]: https://doi.org/10.1115/smasis2021-68299
[research_aly_ogot_2002]: https://doi.org/10.2514/2.3035
[research_alyanak_pendleton_2014]: https://doi.org/10.2514/6.2014-3158
[research_amadori_jouannet_2019]: https://doi.org/10.2514/6.2019-0257
[research_ambler_smith_1974]: https://doi.org/10.21236/ada003033
[research_american_airpower_2008]: https://doi.org/10.5040/9798400608872.ch-005
[research_amirisimkooei_jazaeri_2015]: https://doi.org/10.1007/s10291-015-0445-5
[research_amzajerdian_gragossian_2026]: https://doi.org/10.2514/6.2026-0327
[research_an_kim_2025]: https://doi.org/10.1007/s12555-023-0884-7
[research_an_krzysiak_2023]: https://doi.org/10.1109/icuas57906.2023.10156138
[research_an_meng_2019]: https://doi.org/10.1007/s10291-019-0830-6
[research_analysis_and_2020]: https://doi.org/10.25236/ictmic.2020.066
[research_analytical_methods]: https://doi.org/10.4271/arp5765b
[research_andersen_hauge_1993]: https://doi.org/10.1007/bf01371373
[research_anderson_1973]: https://doi.org/10.21236/ad0770300
[research_anderson_1996]: https://doi.org/10.2514/6.1996-3877
[research_anderson_teope_2017]: https://doi.org/10.2514/6.2017-1859
[research_andic_2021]: https://doi.org/10.3846/gac.2021.12303
[research_andrewslcullen_augsburgerbill_1988]: https://ntrs.nasa.gov/citations/19890009040
[research_angell_2009]: https://doi.org/10.21236/ada513762
[research_anggoro_2021]: https://doi.org/10.28989/vortex.v2i1.933
[research_anton_erturk_2012]: https://doi.org/10.2514/1.c031542
[research_antonini_1993]: https://doi.org/10.2514/6.1993-3702
[research_antony_kumar_2024]: https://doi.org/10.1109/icc64753.2024.10883710
[research_anum_liaquat_2022]: https://doi.org/10.1109/anzcc56036.2022.9966862
[research_anwendungsbeispiel_gps_ins_integration_2007]: https://doi.org/10.1524/9783486595154.191
[research_anwendungsbeispiel_gps_ins_integration_2011]: https://doi.org/10.1524/9783486705720.189
[research_aoyama_kawachi_1995]: https://doi.org/10.2514/3.46823
[research_apeng_shu_2018]: https://doi.org/10.1177/1464419318785978
[research_appendix_d_2004]: https://doi.org/10.1049/pbra017e_appendixd
[research_appendix_g_2010]: https://doi.org/10.2514/5.9781600867538.0733.0743
[research_appleman_1957]: https://doi.org/10.21236/ad0125760
[research_application_of_quasi_object_2008]: https://doi.org/10.18372/1990-5548.18.642
[research_approach_to]: https://doi.org/10.4271/arp4102/12b
[research_arai_2000]: https://doi.org/10.9749/jin.102.319
[research_ardaens_damico_2013]: https://doi.org/10.1016/j.actaastro.2013.06.025
[research_argrow_2016]: https://doi.org/10.1201/9781315372044-9
[research_argrow_weatherhead_2008]: https://doi.org/10.1007/978-1-4020-9137-7_7
[research_armedforceshealthsurveillancecenter_2014]: https://doi.org/10.21236/ada614179
[research_armedforceshealthsurveillancecenter_2015]: https://doi.org/10.21236/ada622922
[research_armedforceshealthsurveillancecenter_2015_b]: https://doi.org/10.21236/ada615586
[research_armstrong_2018]: https://doi.org/10.64628/aam.nnm3d95he
[research_armyaviationcenterandfortruckeral_1992]: https://doi.org/10.21236/ada383063
[research_armyaviationmateriellabsforteustisva_1963]: https://doi.org/10.21236/ad0635695
[research_armysafetycenterfortruckeral_1991]: https://doi.org/10.21236/ada382363
[research_armysafetycenterfortruckeral_1991_b]: https://doi.org/10.21236/ada382344
[research_armysafetycenterfortruckeral_1999]: https://doi.org/10.21236/ada364618
[research_armysafetycenterfortruckeral_1999_b]: https://doi.org/10.21236/ada372187
[research_armyserviceforceswashingtondc_1940]: https://doi.org/10.21236/ada377432
[research_armywarcollcarlislebarrackspa_1982]: https://doi.org/10.21236/ada390492
[research_armywarcollcarlislebarrackspa_2006]: https://doi.org/10.21236/ada481301
[research_arora_carlson_2022]: https://doi.org/10.1109/icuas54217.2022.9836120
[research_ascani_1974]: https://doi.org/10.21236/ada002850
[research_ascher_zwirello_2011]: https://doi.org/10.1109/ipin.2011.6071948
[research_ashenberg_weihs_1984]: https://doi.org/10.2514/3.56733
[research_asher_mitchell_1975]: https://doi.org/10.21236/ada019696
[research_ashkenas_1965]: https://doi.org/10.21236/ad0627659
[research_ashkenas_1965_b]: https://doi.org/10.21236/ad0627989
[research_ashkenas_1965_c]: https://doi.org/10.2514/6.1965-314
[research_ashkenas_1982]: https://doi.org/10.2514/6.1982-1353
[research_ashkenasirvingl_klydedavidh_1989]: https://ntrs.nasa.gov/citations/19890011628
[research_ashokkumar_2023]: https://doi.org/10.2514/6.2023-2537
[research_ashraf_naqvi_2019]: https://doi.org/10.1109/icase48783.2019.9059154
[research_aslan_oktay_2023]: https://doi.org/10.3390/aerospace10050487
[research_assessment_of_1979]: https://doi.org/10.2172/5094238
[research_astm_international_2007]: https://doi.org/10.1108/aeat.2007.12779dab.028
[research_atay_bryant_2021]: https://doi.org/10.1115/1.4050998
[research_ates_2022]: https://doi.org/10.30518/jav.1083114
[research_atkins_didonato_2016]: https://doi.org/10.1002/9780470686652.eae1139
[research_atkinson_1990]: https://doi.org/10.21236/ada230644
[research_atmaca_stroosma_2026]: https://doi.org/10.2514/6.2026-0550
[research_attinello_1956]: https://doi.org/10.4271/560012
[research_attitude_control_1994]: https://doi.org/10.1016/0967-0661(94)91008-1
[research_aubert_ross_2016]: https://doi.org/10.1109/aero.2016.7500894
[research_automation_and_2016]: https://doi.org/10.1201/b11202-12
[research_autonomous_control_2012]: https://doi.org/10.1109/mcs.2012.2205532
[research_autonomous_control_2019]: https://doi.org/10.3390/books978-3-03921-031-2
[research_autonomous_unmanned_1994]: https://doi.org/10.1016/0967-0661(94)90590-8
[research_autopilot_flight]: https://doi.org/10.4271/arp5366
[research_autry_victorazzo_2019]: https://doi.org/10.2514/6.2019-0550
[research_avananyev_2019]: https://doi.org/10.21557/mth.57847390
[research_avery_bunting_2019]: https://doi.org/10.2514/6.2019-3305
[research_avery_jacob_2017]: https://doi.org/10.2514/6.2017-3929
[research_aviation_history]: https://doi.org/10.1007/978-1-4020-8672-4_2
[research_aviationandtroopcommandarmystlouismo_1995]: https://doi.org/10.21236/ada302233
[research_awadallaalihajahmed_2024]: https://doi.org/10.47191/etj/v9i10.09
[research_ayar_karakoc_2023]: https://doi.org/10.1007/978-3-031-29933-9_32
[research_aygun_tascioglu_2014]: https://doi.org/10.1115/esda2014-20495
[research_azer_colpan_2024]: https://doi.org/10.1007/978-3-031-70694-3_17
[research_azimisadjadi_krishnaprasad_2001]: https://doi.org/10.1109/acc.2001.946221
[research_azimov_bishop_2025]: https://doi.org/10.1007/978-3-031-91088-3_16
[research_azizi_khorasani_2011]: https://doi.org/10.1080/00207179.2011.582157
[research_b_gupta_2026]: https://doi.org/10.2139/ssrn.6741293
[research_babetto_stumpf_2021]: https://doi.org/10.2514/6.2021-3219
[research_bachelder_aponso_2020]: https://doi.org/10.4050/sm_2020_hq-915
[research_bachelder_aponso_2020_b]: https://doi.org/10.4050/sm_2020_hq-914
[research_bachelder_aponso_2023]: https://doi.org/10.4050/sm_2023_hq-1194
[research_bachman_1988]: https://doi.org/10.21236/ada198918
[research_backing_for_2009]: https://doi.org/10.1108/aeat.2009.12781aab.024
[research_baek_york_2020]: https://doi.org/10.1109/icuas48674.2020.9213917
[research_bagdatli_karagoz_2019]: https://doi.org/10.2514/6.2019-0497
[research_bahamondejacome_elham_2017]: https://doi.org/10.2514/1.c034050
[research_bahr_mckay_2021]: https://doi.org/10.1017/aer.2021.114
[research_bahrami_jafarnejadsani_2022]: https://doi.org/10.1109/icuas54217.2022.9836208
[research_bai_mingqiang_2014]: https://doi.org/10.5139/ijass.2014.15.4.383
[research_bai_taylor_2020]: https://doi.org/10.1109/taes.2020.2974052
[research_bai_zhang_2011]: https://doi.org/10.1109/iccis.2011.65
[research_baily_gilbertson_1980]: https://doi.org/10.21236/ada096458
[research_bainum_diarra_1988]: https://doi.org/10.2514/6.1988-4252
[research_bainum_tan_2005]: https://doi.org/10.1016/j.ijsolstr.2005.03.017
[research_baisden_ambler_1977]: https://doi.org/10.21236/ada049139
[research_bajurko_2019]: https://doi.org/10.2478/tar-2019-0004
[research_baker_1955]: https://doi.org/10.21236/ad0061751
[research_baker_brennan_2000]: https://doi.org/10.1111/j.1559-3584.2000.tb03305.x
[research_balabanov_haftka_1996]: https://doi.org/10.2514/3.46926
[research_balard_santerre_2005]: https://doi.org/10.1007/s10291-005-0008-2
[research_bald_1957]: https://doi.org/10.21236/ada530629
[research_ballou_1963]: https://doi.org/10.21236/ad0414492
[research_banerjee_taneja_2026]: https://doi.org/10.1007/s42452-026-08727-6
[research_banks_2000]: https://doi.org/10.21236/ada381841
[research_bao_lai_2017]: https://doi.org/10.1109/cac.2017.8242934
[research_baralli_pollini_2002]: https://doi.org/10.2514/6.2002-4993
[research_baranov_chernov_2019]: https://doi.org/10.22363/2312-8143-2019-20-3-220-228
[research_barbatei_skavhaug_2015]: https://doi.org/10.1109/icuas.2015.7152350
[research_barbier_chanthery_2004]: https://doi.org/10.1016/j.ast.2004.01.003
[research_bardera_barcalamontejano_2019]: https://doi.org/10.1016/j.oceaneng.2019.03.020
[research_barderamora_garciamagarino_2018]: https://doi.org/10.2514/6.2018-3006
[research_barderamora_garciamagarino_2019]: https://doi.org/10.2514/1.c035188
[research_bardhan_bera_2017]: https://doi.org/10.1109/icuas.2017.7991504
[research_barlow_2004]: https://doi.org/10.21236/ada460111
[research_barnes_1968]: https://doi.org/10.21236/ad0664750
[research_barnett_1961]: https://doi.org/10.21236/ad0407011
[research_barnhart_2012]: https://doi.org/10.21236/ada582460
[research_barthelemy_coen_1994]: https://doi.org/10.2514/3.46491
[research_barton]: https://doi.org/10.15368/theses.2019.144
[research_bartsch_2018]: https://doi.org/10.4324/9780203712986-18
[research_baselga_garciaasenjo_2009]: https://doi.org/10.1017/s0373463309990117
[research_basic_aircraft]: https://doi.org/10.4271/air825/14
[research_basic_principles_for_2012]: https://doi.org/10.18372/2306-1472.53.3477
[research_basil_anathasayanam_2004]: https://doi.org/10.2514/6.2004-5122
[research_bason_macintyre_1976]: https://doi.org/10.21236/ada029138
[research_bass_2006]: https://doi.org/10.21236/ada453983
[research_bass_2013]: https://doi.org/10.21236/ada588625
[research_bastiaens_mommerency_2021]: https://doi.org/10.1109/ipin51156.2021.9662584
[research_bateman_nelson_2007]: https://doi.org/10.2514/6.2007-2703
[research_batill_bacarro_1988]: https://doi.org/10.2514/6.1988-2315
[research_batill_stelmack_1999]: https://doi.org/10.1016/s1369-8869(99)00002-6
[research_baughman_longeauay_2015]: https://doi.org/10.21236/ada616887
[research_baum_2021]: https://doi.org/10.1201/9780429347498-19
[research_baum_2021_b]: https://doi.org/10.1201/9781003124689
[research_bautista_gutierrez_2023]: https://doi.org/10.3390/s23041934
[research_baxter_2013]: https://doi.org/10.21236/ada613350
[research_bayraktar_fainekos_2004]: https://doi.org/10.21236/ada436407
[research_bean_2015]: https://doi.org/10.21236/ad1009080
[research_bechelder_bjorkman_2025]: https://doi.org/10.4050/sm_handling_2025-5299
[research_beech_announces_1982]: https://doi.org/10.1108/eb035831
[research_beffert_zell_2026]: https://doi.org/10.1109/icuas69441.2026.11598598
[research_bejan_2010]: https://doi.org/10.21236/ada593178
[research_beklemishchev_tikhonov_2021]: https://doi.org/10.1088/1742-6596/1958/1/012004
[research_belabbas]: https://doi.org/10.70675/ec924d0ezfd43z40dczae21z3d2cd1e54679
[research_belai_2025]: https://doi.org/10.4337/9781035315987.00025
[research_belart_1938]: https://doi.org/10.1108/eb030322
[research_belfadel_haessig_2023]: https://doi.org/10.1117/12.2664917
[research_belfadel_haessig_2024]: https://doi.org/10.1109/access.2024.3481409
[research_bell_1993]: https://doi.org/10.2514/6.1993-3964
[research_bell_1997]: https://doi.org/10.21236/ada328241
[research_bellaerospacecobuffalony_1956]: https://doi.org/10.21236/ad0102194
[research_belloni_silvestrini_2024]: https://doi.org/10.1016/j.asr.2023.07.051
[research_belta_2012]: https://doi.org/10.21236/ada577491
[research_belta_2012_b]: https://doi.org/10.21236/ada567708
[research_bendarkar_pant_2013]: https://doi.org/10.2514/6.2013-4303
[research_benders_2018]: https://doi.org/10.1109/icuas.2018.8453437
[research_benders_koch_2019]: https://doi.org/10.1109/icuas.2019.8798170
[research_benders_wenz_2018]: https://doi.org/10.1109/icuas.2018.8453341
[research_bendixcorpyorkpa_1963]: https://doi.org/10.21236/ad0427770
[research_bengida_2022]: https://doi.org/10.2514/6.2022-3448
[research_benishai_reiner_2001]: https://doi.org/10.2514/6.2001-4402
[research_benitez_rutherford_2023]: https://doi.org/10.1109/dasc58513.2023.10311329
[research_bennett]: https://doi.org/10.1109/milcom.1992.244107
[research_benzerrouk_landry_2020]: https://doi.org/10.23919/icins43215.2020.9133871
[research_berbaum_kennedy_1991]: https://doi.org/10.1016/0003-6870(91)90226-8
[research_berberi_segre_2020]: https://doi.org/10.1101/2020.08.11.246926
[research_berens_2003]: https://doi.org/10.2514/6.2003-3419
[research_berger_blanken_2022]: https://doi.org/10.4050/jahs.67.032009
[research_berger_bonzatto_2026]: https://doi.org/10.1109/iccc71363.2026.11593300
[research_berger_carmona_2011]: https://doi.org/10.2514/6.2011-3663
[research_berger_christensen_2025]: https://doi.org/10.4050/sm_handling_2025-5294
[research_berger_horn_2019]: https://doi.org/10.4050/f-0075-2019-14595
[research_bergeron_tavan_2011]: https://doi.org/10.2514/6.2011-2530
[research_bergman_1979]: https://doi.org/10.2514/6.1979-1812
[research_berkshire_1967]: https://doi.org/10.21236/ad0653441
[research_berman_1997]: https://doi.org/10.21236/ada354166
[research_bernardin_1961]: https://doi.org/10.21236/ad0258002
[research_berry_1986]: https://doi.org/10.2514/6.1986-334
[research_berry_2000]: https://doi.org/10.2514/6.2000-5601
[research_berry_powers_1970]: https://doi.org/10.2514/6.1970-566
[research_beser_1978]: https://doi.org/10.2514/6.1978-1295
[research_beser_1979]: https://doi.org/10.2514/3.55920
[research_best_1986]: https://doi.org/10.1108/eb036313
[research_bestaoui_lakhlef_2013]: https://doi.org/10.1002/9781118599938.ch14
[research_bever_urschel_2002]: https://doi.org/10.2514/6.2002-3440
[research_beyer_mansir_1987]: https://doi.org/10.21236/ada210724
[research_bezandry_raglin_2016]: https://doi.org/10.21236/ad1006022
[research_bhamidipati_gao_2020]: https://doi.org/10.1002/navi.381
[research_bhandari_okeefe_2017]: https://doi.org/10.1007/s10291-017-0648-z
[research_bhandari_thomas_2013]: https://doi.org/10.2514/6.2013-4695
[research_bhatia_jiang_2021]: https://doi.org/10.1002/acs.3228
[research_bhattacharyya_2016]: https://doi.org/10.33012/2016.14683
[research_bhattacharyya_2023]: https://doi.org/10.1088/1361-6501/acec8e
[research_bhattacharyya_2025]: https://doi.org/10.1088/1361-6501/adba04
[research_bhattacharyya_mute_2019]: https://doi.org/10.2514/6.2019-0363
[research_bhattacharyya_mute_2020]: https://doi.org/10.3390/s20226606
[research_bian_nener_2018]: https://doi.org/10.1080/00207179.2018.1473643
[research_bian_nener_2022]: https://doi.org/10.1016/j.ast.2022.107392
[research_biber_2023]: https://doi.org/10.1007/978-3-031-29933-9_13
[research_biber_ol_2004]: https://doi.org/10.2514/6.2004-1050
[research_bibin_selvaraj_2012]: https://doi.org/10.1016/j.proeng.2012.06.238
[research_biggerstaff_1998]: https://doi.org/10.21236/ada362220
[research_bihrlejr_1969]: https://doi.org/10.2514/6.1969-894
[research_bil_1989]: https://doi.org/10.2514/6.1989-2131
[research_bil_zegers_2015]: https://doi.org/10.1007/978-3-319-19830-9_27
[research_billec_1967]: https://doi.org/10.21236/ad0813761
[research_binder_holcomb_2001]: https://doi.org/10.21236/ada389917
[research_bindolino_ghiringhelli_2010]: https://doi.org/10.2514/1.41552
[research_binjammaz_albayatti_2013]: https://doi.org/10.1109/wpnc.2013.6533268
[research_birkeland_2013]: https://doi.org/10.21236/ada603131
[research_birkenhead_2024]: https://doi.org/10.32920/25613355.v1
[research_bishop_antoulas_1991]: https://doi.org/10.2514/6.1991-2639
[research_bishop_antoulas_1994]: https://doi.org/10.2514/3.21319
[research_biswalm_2023]: https://doi.org/10.31224/3042
[research_bittrick_1984]: https://doi.org/10.2514/6.1984-1214
[research_black_1968]: https://doi.org/10.2514/6.1968-311
[research_blair_takahashi_2022]: https://doi.org/10.2514/6.2022-4009
[research_blask_2002]: https://doi.org/10.21236/ada402884
[research_bletsos_1986]: https://doi.org/10.2514/6.1986-2107
[research_blewitt_2008]: https://doi.org/10.1029/2008jb005736
[research_bloch_1989]: https://doi.org/10.1007/978-3-642-74585-0_9
[research_blodgett_lagor_2022]: https://doi.org/10.2514/6.2022-2036
[research_blumer_1963]: https://doi.org/10.21236/ad0410173
[research_board_technology_2005]: https://doi.org/10.1108/aeat.2005.12777bab.020
[research_bodson_athans_1985]: https://doi.org/10.2514/6.1985-1928
[research_bogdan_2015]: https://doi.org/10.21236/ad1019428
[research_bohao_daochun_2026]: https://doi.org/10.1007/978-3-032-11165-4_39
[research_bolds_1961]: https://doi.org/10.21236/ad0269208
[research_bolds_1962]: https://doi.org/10.21236/ad0277128
[research_bolla_won_2018]: https://doi.org/10.1049/iet-rsn.2018.5036
[research_bolonkin_2005]: https://doi.org/10.1016/b978-008044731-5/50052-4
[research_bolonkin_2005_b]: https://doi.org/10.1016/b978-008044731-5/50056-1
[research_bolter_0_2023]: https://doi.org/10.5040/9781350601529.1646
[research_bolter_albert_2007]: https://doi.org/10.1093/ww/9780199540884.013.u206328
[research_bolter_boulter_2023]: https://doi.org/10.1093/oed/9086486155
[research_bolter_n_2_2023]: https://doi.org/10.1093/oed/5882058739
[research_bolzak_1989]: https://doi.org/10.21236/ada234396
[research_bona_2000]: https://doi.org/10.1007/pl00012839
[research_bonetti_dezaiacomo_2013]: https://doi.org/10.2514/6.2013-5021
[research_boo_mansor_2015]: https://doi.org/10.2514/6.2015-2250
[research_bookstaber_2000]: https://doi.org/10.21236/ada520346
[research_booz_1988]: https://doi.org/10.2514/6.1988-4363
[research_booz_1998]: https://doi.org/10.21236/ada350673
[research_boozallenandhamiltonincmcleanva_2000]: https://doi.org/10.21236/ada405392
[research_borgen_mott_2024]: https://doi.org/10.7771/2159-6670.1307
[research_borrelli_subramanian_2006]: https://doi.org/10.1109/acc.2006.1657644
[research_bortner_2009]: https://doi.org/10.2514/6.2009-7000
[research_boskovic_diel_2021]: https://doi.org/10.2514/6.2021-1759
[research_boskovic_jackson_2016]: https://doi.org/10.2514/6.2016-0375
[research_boskovic_mehra_1999]: https://doi.org/10.2514/6.1999-4041
[research_boskovic_mehra_2000]: https://doi.org/10.2514/2.4617
[research_boskovic_redding_2009]: https://doi.org/10.2514/6.2009-6264
[research_boskovic_saimingli]: https://doi.org/10.1109/plans.2000.838323
[research_bostian_young_2011]: https://doi.org/10.21236/ada546145
[research_bouadi_moracamino_2012]: https://doi.org/10.2514/6.2012-4613
[research_boudreault_1983]: https://doi.org/10.2514/6.1983-2446
[research_boullianne_1997]: https://doi.org/10.21236/ada328154
[research_bourdin_gatto_2007]: https://doi.org/10.2514/6.2007-4443
[research_bourgeois]: https://doi.org/10.22215/etd/2016-11324
[research_boutros_2015]: https://doi.org/10.21236/ada621067
[research_bowmanjamess_1965]: https://ntrs.nasa.gov/citations/19980228384
[research_boyd_scharf_2022]: https://doi.org/10.7771/2159-6670.1249
[research_boyuk_duvar_2020]: https://doi.org/10.1109/asyu50717.2020.9259868
[research_braasch_2006]: https://doi.org/10.21236/ada456221
[research_brack_2014]: https://doi.org/10.1007/s10291-014-0401-9
[research_brack_2016]: https://doi.org/10.1007/s10291-016-0594-1
[research_brack_2017]: https://doi.org/10.1007/s10291-017-0600-2
[research_brack_2020]: https://doi.org/10.31237/osf.io/bv6pj
[research_bradley_gardhagen_2012]: https://doi.org/10.2514/6.2012-248
[research_bradshaw_brunter_1975]: https://doi.org/10.21236/adb005062
[research_braff_2008]: https://doi.org/10.1002/j.2161-4296.2008.tb00436.x
[research_braff_bian_2012]: https://doi.org/10.1002/navi.1
[research_braff_loh_1992]: https://doi.org/10.1017/s0373463300010717
[research_bramsiepe_voss_2020]: https://doi.org/10.1007/s13272-020-00446-x
[research_brand_dresksler_1995]: https://doi.org/10.21236/ada292873
[research_brauckmanngregoryj_1998]: https://ntrs.nasa.gov/citations/20040087392
[research_bray_1963]: https://doi.org/10.2514/6.1963-1003
[research_breitkopf_1989]: https://doi.org/10.1520/stp10349s
[research_breitmaier_1988]: https://doi.org/10.21236/ada206786
[research_breitsamter_laschka_2001]: https://doi.org/10.2514/2.2758
[research_brenckmann_1964]: https://doi.org/10.2514/6.1964-804
[research_breul_1963]: https://doi.org/10.21236/ad0402774
[research_breunig_sayed_2018]: https://doi.org/10.2514/6.2018-3349
[research_brictson_ciavarelli_1969]: https://doi.org/10.1177/001872086901100310
[research_briere_2007]: https://doi.org/10.21236/ada480162
[research_briere_warkander_2007]: https://doi.org/10.21236/ada480163
[research_briggs_2002]: https://doi.org/10.21236/ada404192
[research_brinker_2004]: https://doi.org/10.2514/6.2004-6575
[research_brockett_laux_2002]: https://doi.org/10.2514/6.2002-3454
[research_brodersen_sauer_1992]: https://doi.org/10.2514/3.46146
[research_brodzinsky_1959]: https://doi.org/10.1109/tane3.1959.4201675
[research_broglio_1961]: https://doi.org/10.21236/ad0294976
[research_broglio_1962]: https://doi.org/10.1007/978-3-7091-5470-0_15
[research_brooks_1989]: https://doi.org/10.1117/12.949102
[research_brooks_mavris_2021]: https://doi.org/10.2514/6.2021-3711
[research_brown_1950]: https://doi.org/10.21236/ad0109768
[research_brown_1989]: https://doi.org/10.2514/6.1989-2112
[research_brown_1998]: https://doi.org/10.21236/ada387958
[research_brown_2009]: https://doi.org/10.21236/ada508608
[research_brown_hwang_1983]: https://doi.org/10.1002/j.2161-4296.1983.tb00852.x
[research_brown_lu_2006]: https://doi.org/10.21236/ada458227
[research_brown_mchenry_2014]: https://doi.org/10.1007/978-90-481-9707-1_31
[research_brown_silva_2000]: https://doi.org/10.21236/ada475831
[research_brown_sun_2017]: https://doi.org/10.1109/icuas.2017.7991466
[research_brown_timmerman_1991]: https://doi.org/10.2514/6.1991-3167
[research_brownandrootdevelopmentinchoustontx_1983]: https://doi.org/10.21236/ada131463
[research_bruckner_vangraas_2010]: https://doi.org/10.1007/s10291-010-0193-5
[research_bruening_snyder_2000]: https://doi.org/10.1115/2000-gt-0014
[research_bruening_snyder_2001]: https://doi.org/10.1115/1.1362666
[research_brukarczyk_nowak_2021]: https://doi.org/10.3390/aerospace8060167
[research_brungardt_2011]: https://doi.org/10.1201/b11202-3
[research_brunson_raisrohani_1996]: https://doi.org/10.2514/6.1996-1378
[research_bruton_glennie_1999]: https://doi.org/10.1007/pl00012771
[research_bryant_gradwell_2015]: https://doi.org/10.1109/icuas.2015.7152322
[research_bryant_tigges_1998]: https://doi.org/10.2514/6.1998-4572
[research_brycelhorvath_gregoryawrenn]: https://ntrs.nasa.gov/citations/20210017483
[research_buchanan_2010]: https://doi.org/10.21236/ada525266
[research_bucholtz_nichols_2008]: https://doi.org/10.21236/ada488142
[research_bucklew_2009]: https://doi.org/10.21236/ada517761
[research_buckner_2000]: https://doi.org/10.21236/ada575487
[research_budd_2002]: https://doi.org/10.21236/ada420662
[research_buelljr_1970]: https://doi.org/10.2514/6.1970-1000
[research_buerger_cannon_2016]: https://doi.org/10.1109/ecc.2016.7810276
[research_buffington_1997]: https://doi.org/10.21236/ada327799
[research_buffington_1999]: https://doi.org/10.21236/ada375713
[research_buffington_1999_b]: https://doi.org/10.21236/ada374954
[research_bulka_nahon_2017]: https://doi.org/10.1109/icuas.2017.7991437
[research_bulka_nahon_2019]: https://doi.org/10.1109/icuas.2019.8797720
[research_bunnell_2001]: https://doi.org/10.2514/6.2001-4065
[research_burcham_1998]: https://doi.org/10.21236/ada351574
[research_burke_2015]: https://doi.org/10.21236/ad1019501
[research_burken_frost_2011]: https://doi.org/10.2514/6.2011-6304
[research_burnashev_zbrutsky_2019]: https://doi.org/10.3846/aviation.2019.10300
[research_burns_2000]: https://doi.org/10.21236/ada493254
[research_burnside_1974]: https://doi.org/10.21236/ada112369
[research_bushey]: https://doi.org/10.1007/978-1-4020-9137-7_6
[research_butler_1970]: https://doi.org/10.1007/bf02319998
[research_butler_1976]: https://doi.org/10.21236/ada023690
[research_butler_lillico_1999]: https://doi.org/10.1017/s0001924000064617
[research_butt_markmiller_2023]: https://doi.org/10.20944/preprints202306.2101.v1
[research_bye_1993]: https://doi.org/10.2514/6.1993-3996
[research_c_scana_milestone_1969]: https://doi.org/10.1109/mspec.1969.5213661
[research_cacopardi_caporicci_1990]: https://doi.org/10.1049/el:19901050
[research_cai_cui_2018]: https://doi.org/10.23919/chicc.2018.8482646
[research_cai_grafarend_2009]: https://doi.org/10.1007/s10291-008-0115-y
[research_cai_rajaram_2022]: https://doi.org/10.31224/2410
[research_cai_zhou_2018]: https://doi.org/10.1109/access.2018.2872529
[research_cakici_leblebicioglu_2016]: https://doi.org/10.1177/1756829316678876
[research_caldwell_1963]: https://doi.org/10.21236/ad0406938
[research_calhoun_draper_2017]: https://doi.org/10.1201/9781315576138-10
[research_calhoun_raquet_2016]: https://doi.org/10.1109/plans.2016.7479713
[research_callaghan_kunz_2019]: https://doi.org/10.2514/6.2019-3548
[research_callens_pugmire_1969]: https://doi.org/10.2514/6.1969-296
[research_callicoatt_2009]: https://doi.org/10.21236/ada517767
[research_calnoorrajashekar_tourani_2020]: https://doi.org/10.2514/6.2020-2926
[research_calvano_harney_1998]: https://doi.org/10.21236/ada345638
[research_camatti_chiesa_1998]: https://doi.org/10.1016/s1369-8869(98)00002-0
[research_cameron_fredin_2022]: https://doi.org/10.1109/icuas54217.2022.9836082
[research_campbell_1959]: https://doi.org/10.1108/eb033068
[research_candan_sanci_2024]: https://doi.org/10.13031/aim.202401277
[research_canpolat_yayla_2009]: https://doi.org/10.2514/1.45274
[research_cao_gao_2026]: https://doi.org/10.2514/1.c038744
[research_cao_morse_2008]: https://doi.org/10.1109/acc.2008.4586586
[research_capderou_2012]: https://doi.org/10.1007/978-2-287-99050-2_14
[research_capek_1995]: https://doi.org/10.1002/pssb.2221880219
[research_caporicci_soddu]: https://doi.org/10.1109/plans.1992.185908
[research_cappuzzo_bianchi_2022]: https://doi.org/10.4050/f-0078-2022-17638
[research_carico_1995]: https://doi.org/10.21236/ada300966
[research_carney_2008]: https://doi.org/10.21236/ada482272
[research_caron]: https://doi.org/10.22215/etd/2011-07219
[research_carpenter_jenny_1964]: https://doi.org/10.2514/6.1964-286
[research_carr_lambrecht_2003]: https://doi.org/10.21236/ada424895
[research_carretta_ree_1999]: https://doi.org/10.21236/ada372383
[research_carreyette_1950]: https://doi.org/10.1108/eb031848
[research_carrier_arnoult_2022]: https://doi.org/10.2514/6.2022-0726
[research_carrier_phase_1999]: https://doi.org/10.1109/acc.1999.782450
[research_carrier_recovery_2012]: https://doi.org/10.1002/9781118383285.ch11
[research_carrillocorcoles_mertens_2023]: https://doi.org/10.2514/1.c037108
[research_carriofernandez]: https://doi.org/10.20868/upm.thesis.65523
[research_carroll]: https://doi.org/10.1109/plans.1994.303298
[research_carter_mueller_1991]: https://doi.org/10.21236/ada529766
[research_casarosa_galatolo_2004]: https://doi.org/10.1108/00022660410565526
[research_case_1965]: https://doi.org/10.2514/6.1965-710
[research_casey]: https://doi.org/10.14264/311857
[research_caseymaslen_2018]: https://doi.org/10.1163/9789004363267_005
[research_caseymaslen_2018_b]: https://doi.org/10.1163/9789004363267_003
[research_caseymaslen_2018_c]: https://doi.org/10.1163/9789004363267_008
[research_cass_ball_1988]: https://doi.org/10.2514/6.1988-4487
[research_castagno_ochoa_2018]: https://doi.org/10.1109/icuas.2018.8453483
[research_castaldo_angrisano_2014]: https://doi.org/10.1155/2014/173818
[research_castanon_cassandras_2010]: https://doi.org/10.21236/ada567152
[research_castilloeffen_visnevski_2009]: https://doi.org/10.1109/aero.2009.4839599
[research_castrichini_hodigeresiddaramaiah_2016]: https://doi.org/10.2514/1.c033474
[research_catalan_iglesias_2025]: https://doi.org/10.3390/engproc2025088062
[research_catchpole_1990]: https://doi.org/10.21236/ada232041
[research_categorization_and]: https://doi.org/10.3403/30350792u
[research_catelani_ciani_2015]: https://doi.org/10.1109/metroaerospace.2015.7180648
[research_caurin_daudfilho_2024]: https://doi.org/10.1007/978-3-031-62094-2_6
[research_causa_fasano_2025]: https://doi.org/10.1109/plans61210.2025.11028417
[research_cavagna_ricci_2009]: https://doi.org/10.2514/6.2009-2571
[research_cavagna_ricci_2010]: https://doi.org/10.2514/6.2010-9076
[research_cavagna_ricci_2011]: https://doi.org/10.2514/1.c031072
[research_cazaurang_bergeon_2003]: https://doi.org/10.2514/6.2003-5478
[research_cecrdle_2019]: https://doi.org/10.2514/6.2019-1529
[research_celko_dubois_1995]: https://doi.org/10.21236/ada327772
[research_cellmer_wielgosz_2010]: https://doi.org/10.1007/s00190-009-0364-8
[research_cenko_tinoco_1981]: https://doi.org/10.2514/3.57473
[research_centracchio_rossetti_2018]: https://doi.org/10.1155/2018/6320197
[research_ceren_altug_2011]: https://doi.org/10.1007/978-94-007-3033-5_23
[research_cestino_2006]: https://doi.org/10.1016/j.ast.2006.06.001
[research_cetin_kurnaz_2010]: https://doi.org/10.1007/978-94-007-1110-5_16
[research_cetin_yilmaz_2013]: https://doi.org/10.1109/icuas.2013.6564699
[research_cetin_yilmaz_2014]: https://doi.org/10.1109/icuas.2014.6842245
[research_cetin_zagli_2011]: https://doi.org/10.1007/978-94-007-3033-5_38
[research_chai_crisafulli_1995]: https://doi.org/10.2514/6.1995-3882
[research_chai_mason_1996]: https://doi.org/10.2514/6.1996-4038
[research_chai_wilhite_2012]: https://doi.org/10.2514/6.2012-5112
[research_chaikalis_khorrami_2020]: https://doi.org/10.1109/icuas48674.2020.9213920
[research_chakrabarty_morris_2016]: https://doi.org/10.1109/icuas.2016.7502612
[research_chakraborty_trawick_2014]: https://doi.org/10.2514/6.2014-3012
[research_chakravarty_chichka_2006]: https://doi.org/10.2514/6.2006-6543
[research_chalenski_hatchell_2018]: https://doi.org/10.3997/2214-4609.201801942
[research_chalk_1963]: https://doi.org/10.2514/6.1963-1001
[research_chalk_1964]: https://doi.org/10.2514/3.43604
[research_chaloff_hiyama_1974]: https://doi.org/10.21236/ada002858
[research_chana_sullivan_1992]: https://doi.org/10.4271/921911
[research_chandler_1989]: https://doi.org/10.21236/ada211469
[research_chang_2006]: https://doi.org/10.21236/ada466498
[research_chang_2013]: https://doi.org/10.1017/s0373463313000775
[research_chang_ai_2026]: https://doi.org/10.3390/aerospace13060516
[research_chang_wang_2021]: https://doi.org/10.1007/s10291-021-01148-5
[research_chang_zhang_2022]: https://doi.org/10.1109/icus55513.2022.9986552
[research_chang_zheng_2022]: https://doi.org/10.3390/en15228616
[research_changes_in_2002]: https://doi.org/10.1108/aeat.2002.12774cab.043
[research_chansarkar_2000]: https://doi.org/10.1007/pl00012837
[research_chansikpark_ilsunkim]: https://doi.org/10.1109/sice.1998.742988
[research_chansikpark_ilsunkim_2000]: https://doi.org/10.1109/7.826336
[research_chao_brink_2017]: https://doi.org/10.33012/2017.15021
[research_chapa_2013]: https://doi.org/10.21236/ada580972
[research_chapteer_8_2008]: https://doi.org/10.4324/9780203305225-11
[research_chapter_1_2017]: https://doi.org/10.1515/9780824853952-004
[research_chapter_3_2005]: https://doi.org/10.1515/9781400866816-004
[research_chapter_3_2021]: https://doi.org/10.1515/9781683927082-004
[research_chapter_3u_s_2016]: https://doi.org/10.1201/b11202-8
[research_chaput_1987]: https://doi.org/10.2514/6.1987-2954
[research_characteristics_of_2010]: https://doi.org/10.1002/9780470664797.ch4
[research_chattot_2005]: https://doi.org/10.2514/1.14377
[research_chattot_2006]: https://doi.org/10.2514/1.15349
[research_chaudhry_smith_2016]: https://doi.org/10.2514/6.2016-1253
[research_chaussee_dervault_2013]: https://doi.org/10.2514/6.2013-1678
[research_cheatham_hackler_1966]: https://doi.org/10.2514/3.28506
[research_chelnokov_perelyaev_2022]: https://doi.org/10.23919/icins51784.2022.9815405
[research_cheman_liu_2020]: https://doi.org/10.1109/icuas48674.2020.9214048
[research_chen]: https://doi.org/10.5353/th_991026390699703414
[research_chen_1964]: https://doi.org/10.2514/6.1964-477
[research_chen_1995]: https://doi.org/10.21236/ada302749
[research_chen_2025]: https://doi.org/10.1109/csis-iac65538.2025.11161417
[research_chen_duan_2016]: https://doi.org/10.1109/aus.2016.7748123
[research_chen_fang_2021]: https://doi.org/10.3390/app11199037
[research_chen_fang_2025]: https://doi.org/10.2478/amns-2025-0772
[research_chen_han_2015]: https://doi.org/10.1109/iscid.2015.257
[research_chen_han_2023]: https://doi.org/10.1007/978-981-19-6613-2_212
[research_chen_han_2023_b]: https://doi.org/10.1109/icuas57906.2023.10156435
[research_chen_ho_2017]: https://doi.org/10.1139/juvs-2016-0011
[research_chen_hubner_2021]: https://doi.org/10.2514/1.c035763
[research_chen_li_2021]: https://doi.org/10.1007/s10291-021-01203-1
[research_chen_li_2023]: https://doi.org/10.1016/j.measurement.2023.113666
[research_chen_qin_2013]: https://doi.org/10.2514/1.c032102
[research_chen_wang_2026]: https://doi.org/10.1109/ddcls71227.2026.11610077
[research_chen_wei_2024]: https://doi.org/10.1016/j.asr.2024.03.076
[research_chen_xu_2024]: https://doi.org/10.3390/aerospace11080656
[research_chen_yang_2024]: https://doi.org/10.1109/ddcls61622.2024.10606864
[research_chen_zhai_2026]: https://doi.org/10.1038/s41598-026-56269-z
[research_chen_zhang_2026]: https://doi.org/10.2139/ssrn.7028426
[research_chen_zhao_2014]: https://doi.org/10.1109/cdc.2014.7040426
[research_chen_zhao_2016]: https://doi.org/10.1109/tcst.2015.2501352
[research_chen_zhao_2024]: https://doi.org/10.1109/jsen.2023.3341155
[research_chen_zheng_2011]: https://doi.org/10.1109/cca.2011.6044364
[research_chen_zheng_2011_b]: https://doi.org/10.1109/cdc.2011.6161439
[research_chen_zhou_2020]: https://doi.org/10.1007/978-981-15-8901-0_11
[research_chen_zhou_2020_b]: https://doi.org/10.1007/978-981-15-8901-0_3
[research_chen_zhou_2020_c]: https://doi.org/10.1007/978-981-15-8901-0_9
[research_chen_zhou_2020_d]: https://doi.org/10.1007/978-981-15-8901-0_14
[research_chen_zhou_2020_e]: https://doi.org/10.1007/978-981-15-8901-0_10
[research_chen_zhou_2021]: https://doi.org/10.1007/978-981-15-8901-0
[research_cheng_cao_2021]: https://doi.org/10.1007/s11071-020-06129-w
[research_chernenko_burnashev_2022]: https://doi.org/10.20535/0203-3771422021268461
[research_chesser_draper_1999]: https://doi.org/10.2172/6077
[research_chessman_2022]: https://doi.org/10.22454/fammed.2022.610853
[research_chester_1995]: https://doi.org/10.2514/3.46816
[research_chester_2002]: https://doi.org/10.2514/2.2964
[research_chester_2002_b]: https://doi.org/10.1016/b978-008042699-0/50031-0
[research_cheung_rezgui_2020]: https://doi.org/10.2514/1.c035732
[research_chevalier_burke_1972]: https://doi.org/10.2514/6.1972-125
[research_chiang_youssef_1995]: https://doi.org/10.2514/6.1995-3179
[research_chiba_makino_2009]: https://doi.org/10.2514/6.2009-968
[research_chiba_obayashi_2006]: https://doi.org/10.2514/1.12782
[research_chiesa_disciuva_1999]: https://doi.org/10.1016/s1369-8869(99)00011-7
[research_chihabi_ulrich_2024]: https://doi.org/10.2514/6.2024-0627
[research_chihabi_ulrich_2024_b]: https://doi.org/10.2514/6.2024-0627.c1
[research_childers_condon_2004]: https://doi.org/10.21236/ada426621
[research_childers_gelderloos]: https://doi.org/10.1109/dasc.2001.964227
[research_chin_1985]: https://doi.org/10.2514/6.1985-1878
[research_china_satellite_2013]: https://doi.org/10.1007/978-3-642-37404-3
[research_chinag_youssef_1994]: https://doi.org/10.2514/6.1994-3599
[research_chisman_1991]: https://doi.org/10.2514/6.1991-3168
[research_chitrakaran_dawson_2005]: https://doi.org/10.21236/ada465706
[research_chiuhungluk_gao]: https://doi.org/10.1109/ijcnn.2004.1380871
[research_cho_kang_2019]: https://doi.org/10.5220/0007832602370242
[research_cho_lee_2025]: https://doi.org/10.1109/access.2025.3585495
[research_choi_2016]: https://doi.org/10.12673/jant.2016.20.3.218
[research_choi_nguyen_2010]: https://doi.org/10.2514/6.2010-482
[research_chorley_1981]: https://doi.org/10.2514/6.1981-2264
[research_chudoba_cook_2003]: https://doi.org/10.2514/6.2003-5386
[research_chun_kwon_2005]: https://doi.org/10.5081/jgps.4.1.201
[research_cifaldi_2017]: https://doi.org/10.1007/978-3-319-32193-6_158-1
[research_cihak_antonw_2005]: https://doi.org/10.21236/ada477051
[research_citurs_caton_1985]: https://doi.org/10.2514/6.1985-1807
[research_civil_regulation_2024]: https://doi.org/10.4337/9781035312344
[research_civil_small]: https://doi.org/10.3403/30426813u
[research_civil_small_b]: https://doi.org/10.3403/30426807u
[research_civilnuclearsystemscorpalbuquerquenm_1977]: https://doi.org/10.21236/adb017277
[research_clare_macbeth_2012]: https://doi.org/10.1109/acc.2012.6314752
[research_clare_ryan_2012]: https://doi.org/10.1177/1071181312561110
[research_clark]: https://doi.org/10.1109/plans.1996.509103
[research_clark_1964]: https://doi.org/10.2514/6.1964-618
[research_clark_1965]: https://doi.org/10.2514/6.1965-792
[research_clark_1975]: https://doi.org/10.21236/ada334771
[research_clark_2006]: https://doi.org/10.21236/ada463370
[research_clark_2013]: https://doi.org/10.21236/ada589119
[research_clarkson_1991]: https://doi.org/10.21236/ada240824
[research_classification_for]: https://doi.org/10.1520/f2635-07
[research_cleveland_1970]: https://doi.org/10.2514/6.1970-940
[research_clothier_walker_2014]: https://doi.org/10.1007/978-90-481-9707-1_39
[research_clough_2003]: https://doi.org/10.2514/6.2003-6504
[research_coban_2020]: https://doi.org/10.1108/aeat-08-2019-0171
[research_coban_oktay_2018]: https://doi.org/10.30518/jav.461116
[research_coban_oktay_2018_b]: https://doi.org/10.30518/jav.421644
[research_cobb_cohen]: https://doi.org/10.1109/ntc.1994.316683
[research_cochrane_whitman_1987]: https://doi.org/10.1109/oceans.1987.1160864
[research_cockburn_1965]: https://doi.org/10.1049/sqj.1965.0062
[research_cockpit_visibility]: https://doi.org/10.4271/air32a
[research_cohen_pervan_1994]: https://doi.org/10.1002/j.2161-4296.1994.tb02568.x
[research_coiro_nicolosi_2001]: https://doi.org/10.1016/s1369-8869(00)00020-3
[research_cole_1989]: https://doi.org/10.21236/ada217370
[research_coleman_hamilton_2026]: https://doi.org/10.2514/6.2026-4223
[research_collins_kochersberger_2025]: https://doi.org/10.1007/978-1-4419-9834-7-28
[research_collyer_ricard_1980]: https://doi.org/10.21236/ada087012
[research_colozzaanthony_dolcejames_2003]: https://ntrs.nasa.gov/citations/20040021326
[research_colwell_1966]: https://doi.org/10.1108/eb034185
[research_comandur_walters_2019]: https://doi.org/10.4050/f-0075-2019-14591
[research_commercial_aircraft]: https://doi.org/10.4271/arp6277
[research_computer_vision_based_2025]: https://doi.org/10.31673/2412-4338.2025.038701
[research_conceptual_design_2024]: https://doi.org/10.2514/5.9781624107290.0911.1002
[research_conducting_unmanned_2015]: https://doi.org/10.13031/aim.20152147654
[research_configuring_aircraft_2010]: https://doi.org/10.1017/cbo9780511844652.008
[research_connelly_1982]: https://doi.org/10.21236/ada120473
[research_connelly_1983]: https://doi.org/10.1177/154193128302701108
[research_conners_1995]: https://doi.org/10.1115/95-gt-116
[research_connolly_1981]: https://doi.org/10.21236/ada107456
[research_connolly_ogorman_2023]: https://doi.org/10.1109/icuas57906.2023.10155987
[research_constantin_decourcy_2023]: https://doi.org/10.1016/j.ast.2023.108450
[research_construction_vehicles_2025]: https://doi.org/10.36652/1684-1298-2025-5-43-46
[research_control_authority_1993]: https://doi.org/10.2514/6.1993-3968
[research_control_of_cooperative]: https://doi.org/10.12681/eadd/25712
[research_control_surface_2010]: https://doi.org/10.2514/5.9781600867538.0613.0624
[research_cook_1964]: https://doi.org/10.21236/ada953004
[research_cook_1997]: https://doi.org/10.1016/b978-0-340-63200-0.50015-0
[research_cook_2007]: https://doi.org/10.1016/b978-075066927-6/50013-1
[research_cook_2013]: https://doi.org/10.1016/b978-0-08-098242-7.00010-9
[research_cook_2024]: https://doi.org/10.1109/icuas60882.2024.10557026
[research_cook_hauser_2018]: https://doi.org/10.23919/acc.2018.8431242
[research_cook_kokolios_2005]: https://doi.org/10.2514/1.2834
[research_cooke_2010]: https://doi.org/10.1002/9780470686652.eae259
[research_cooke_speck_1971]: https://doi.org/10.1117/12.953460
[research_cookerly_1988]: https://doi.org/10.21236/ada202092
[research_cooper_2023]: https://doi.org/10.52843/cassyni.czz9tq
[research_cooper_ravela_2024]: https://doi.org/10.1109/icuas60882.2024.10556902
[research_cooper_stroud_1972]: https://doi.org/10.2514/3.44341
[research_coopmans_jensen_2013]: https://doi.org/10.1109/icuas.2013.6564757
[research_coordinatingresearchcouncilincatlantaga_1988]: https://doi.org/10.21236/ada198197
[research_coppock_gerke_1977]: https://doi.org/10.21236/ada039834
[research_corazzini_robertson_1998]: https://doi.org/10.1002/j.2161-4296.1998.tb02382.x
[research_corley_kehler_2008]: https://doi.org/10.21236/ada518405
[research_corn_mclaurine_2005]: https://doi.org/10.21236/ada444713
[research_corridor_wide_surveillance_2021]: https://doi.org/10.5038/cutr-nicr-y1-4.3
[research_corridor_wide_surveillance_2023]: https://doi.org/10.5038/cutr-nicr-y2-4-4.1
[research_corridor_wide_surveillance_2023_b]: https://doi.org/10.5038/cutr-nicr-y2-4-4.2
[research_corridor_wide_surveillance_2024]: https://doi.org/10.5038/cutr-nicr-y3-4-7.1
[research_corridor_wide_surveillance_2025]: https://doi.org/10.5038/cutr-nicr-y3-4-7.2
[research_cossaboom_georgy_2012]: https://doi.org/10.1155/2012/576807
[research_cote_2015]: https://doi.org/10.21236/ad1019500
[research_courharbo_2018]: https://doi.org/10.1109/icuas.2018.8453411
[research_courharbo_2020]: https://doi.org/10.1109/icuas48674.2020.9213990
[research_courtaulds_aerospace_1998]: https://doi.org/10.1108/aeat.1998.12770cab.017
[research_courtois_aouf_2017]: https://doi.org/10.1109/icuas.2017.7991328
[research_coutard_chaumette_2011]: https://doi.org/10.1109/iros.2011.6048527
[research_coutard_chaumette_2011_b]: https://doi.org/10.1109/icra.2011.5979771
[research_cove_santos_2004]: https://doi.org/10.1007/s10291-004-0105-7
[research_cox_1978]: https://doi.org/10.1002/j.2161-4296.1978.tb01335.x
[research_cox_1989]: https://doi.org/10.1108/eb036783
[research_cox_2009]: https://doi.org/10.4271/2009-01-3098
[research_cox_roy_1988]: https://doi.org/10.21236/ada202871
[research_coyle_1992]: https://doi.org/10.1002/sdr.4260080302
[research_coyle_herr_2026]: https://doi.org/10.2514/6.2026-4382
[research_crafton_1965]: https://doi.org/10.21236/ad0620135
[research_craig_zwernemann_1991]: https://doi.org/10.2514/6.1991-3120
[research_crain_bishop_2016]: https://doi.org/10.2514/6.2016-0099
[research_crandall_1999]: https://doi.org/10.21236/ada368478
[research_cranfield_helps_2008]: https://doi.org/10.1108/aeat.2008.12780eab.028
[research_crashworthy_landing_1998]: https://doi.org/10.1108/aeat.1998.12770ead.004
[research_crassidis_mook_1991]: https://doi.org/10.2514/6.1991-2666
[research_crassidis_mook_1992]: https://doi.org/10.2514/6.1992-4619
[research_crassidis_mook_1993]: https://doi.org/10.2514/3.21101
[research_crespo_matsutani_2010]: https://doi.org/10.2514/6.2010-8049
[research_crew_safety]: https://doi.org/10.4271/arp4101/9
[research_crew_safety_b]: https://doi.org/10.4271/arp1139
[research_crimi_johnson_1973]: https://doi.org/10.2514/3.60231
[research_cristofaro_johansen_2015]: https://doi.org/10.1109/ecc.2015.7330774
[research_cronk_2007]: https://doi.org/10.21236/ada636422
[research_crossley_2004]: https://doi.org/10.21236/ada430430
[research_crossley_skillen_2011]: https://doi.org/10.2514/1.c031180
[research_cruz_encarnacao_2011]: https://doi.org/10.1007/978-94-007-3033-5_15
[research_cruz_fierro_2015]: https://doi.org/10.1109/icuas.2015.7152349
[research_cuevas_aguiar_2017]: https://doi.org/10.15394/ijaaa.2017.1176
[research_cui_han_2020]: https://doi.org/10.1016/j.ast.2020.106346
[research_cui_zhou_2022]: https://doi.org/10.1002/asjc.2828
[research_cummings_liersch_2018]: https://doi.org/10.2514/1.c033808
[research_cummings_mastracchio_2013]: https://doi.org/10.1093/iwc/iws011
[research_cummings_morton_2003]: https://doi.org/10.2514/6.2003-417
[research_cummings_morton_2008]: https://doi.org/10.1016/j.ast.2007.08.007
[research_cummings_schutte_2012]: https://doi.org/10.2514/1.c031430
[research_cummins_1999]: https://doi.org/10.21236/ada363211
[research_cunningham]: https://doi.org/10.22215/etd/2016-11270
[research_cunningham_1976]: https://doi.org/10.2514/6.1976-1954
[research_cunningham_denboer_1990]: https://doi.org/10.2514/3.45893
[research_curlett_2002]: https://doi.org/10.21236/ada402153
[research_current_manned]: https://doi.org/10.1007/978-1-4020-8672-4_3
[research_currey_1988]: https://doi.org/10.2514/4.861468
[research_cutler_mclain_2010]: https://doi.org/10.2514/6.2010-8037
[research_cyganczuk_roguski_2023]: https://doi.org/10.5604/01.3001.0053.7159
[research_dahleh_tsitsiklis_2002]: https://doi.org/10.21236/ada417306
[research_dahmane_lejdel_2022]: https://doi.org/10.11591/eei.v11i2.3695
[research_dai_cochran_2009]: https://doi.org/10.1109/acc.2009.5159914
[research_dai_quan_2018]: https://doi.org/10.1016/j.ast.2018.09.034
[research_dai_wei_2016]: https://doi.org/10.1016/j.cja.2016.02.001
[research_dai_wei_2020]: https://doi.org/10.1109/taes.2019.2953413
[research_dakka_johnson_2019]: https://doi.org/10.15394/ijaaa.2019.1411
[research_dalamagkidis_2014]: https://doi.org/10.1007/978-90-481-9707-1_93
[research_dalamagkidis_2014_b]: https://doi.org/10.1007/978-90-481-9707-1_109
[research_dalamagkidis_valavanis_2012]: https://doi.org/10.1007/978-94-007-2479-2_2
[research_dalcarobo_fensterseifer_2010]: https://doi.org/10.4271/2010-36-0513
[research_daly_1994]: https://doi.org/10.21236/ada279592
[research_damico_montenbruck_2008]: https://doi.org/10.2514/6.2008-6661
[research_dandrea_2008]: https://doi.org/10.21236/ada530333
[research_dang_chen_2022]: https://doi.org/10.1109/jas.2021.1004350
[research_danko_oh_2013]: https://doi.org/10.1109/icuas.2013.6564784
[research_dannenhoffer_1981]: https://doi.org/10.2514/6.1981-1368
[research_dantsker_theile_2018]: https://doi.org/10.2514/6.2018-5009
[research_dantsker_yu_2019]: https://doi.org/10.2514/6.2019-3230
[research_daquantang_yongkangjiao_2016]: https://doi.org/10.1109/cgncc.2016.7829144
[research_darrah_conrad_1971]: https://doi.org/10.21236/ada373246
[research_darvish_pourtakdoust_2015]: https://doi.org/10.1016/j.ast.2014.12.030
[research_daudfilho]: https://doi.org/10.11606/t.18.2023.tde-27032023-153150
[research_daughetee_1974]: https://doi.org/10.2514/6.1974-343
[research_david_2025]: https://doi.org/10.2139/ssrn.5274107
[research_davidson_2004]: https://doi.org/10.2514/6.2004-6557
[research_davidson_little_1977]: https://doi.org/10.2172/6868208
[research_davis_2010]: https://doi.org/10.1109/plans.2010.5507196
[research_dawson_2015]: https://doi.org/10.21236/ad1019430
[research_debilzan_1975]: https://doi.org/10.21236/ada019111
[research_decamp_hardy_1981]: https://doi.org/10.1108/eb035691
[research_decarvalhobertoli_adabo_2016]: https://doi.org/10.4271/2016-36-0437
[research_decoust_udrea_2008]: https://doi.org/10.2514/6.2008-7492
[research_decunto]: https://doi.org/10.22215/etd/2020-14127
[research_defensescienceboardwashingtondc_2002]: https://doi.org/10.21236/ada429489
[research_dehghani_menhaj_2016]: https://doi.org/10.1016/j.robot.2016.03.008
[research_deja_dayyani_2022]: https://doi.org/10.2139/ssrn.4046787
[research_dejarnettecrumsey_savage_2022]: https://doi.org/10.21236/ad1172530
[research_delancey_harris_2011]: https://doi.org/10.21236/ada555666
[research_delaurier_2022]: https://doi.org/10.1201/9781315228167-4
[research_delellis_divito_2013]: https://doi.org/10.2514/6.2013-4585
[research_delery_meauze_2003]: https://doi.org/10.1016/s1270-9638(02)00008-1
[research_delgadoregis_mattos_2004]: https://doi.org/10.2514/6.2004-5192
[research_delporte_mercier_2007]: https://doi.org/10.1109/freq.2007.4319215
[research_delporte_mercier_2008]: https://doi.org/10.1155/2008/273785
[research_delvecchio_costa_1999]: https://doi.org/10.4043/10778-ms
[research_demarchi_haning_1978]: https://doi.org/10.21236/ada062749
[research_demir_gorguluarslan_2021]: https://doi.org/10.2514/6.2021-3045
[research_demircali_uvet_2018]: https://doi.org/10.3390/app8091541
[research_denegri_sharma_2021]: https://doi.org/10.2514/1.c035850
[research_deng_duan_2016]: https://doi.org/10.1007/s11071-016-2670-z
[research_denham_paines_2008]: https://doi.org/10.2514/6.2008-6331
[research_denny_2003]: https://doi.org/10.1088/0143-0807/24/4/355
[research_departmentofdefensewashingtondc_1994]: https://doi.org/10.21236/ada286190
[research_departmentofdefensewashingtondc_2009]: https://doi.org/10.21236/ada522247
[research_departmentoftheairforcewashingtondc_1986]: https://doi.org/10.21236/ada268421
[research_departmentoftheairforcewashingtondc_1997]: https://doi.org/10.21236/ada339102
[research_departmentoftheairforcewashingtondc_2004]: https://doi.org/10.21236/ada460562
[research_departmentoftheairforcewashingtondc_2005]: https://doi.org/10.21236/ada495209
[research_depaula_dwivedi_2025]: https://doi.org/10.2514/6.2025-3547
[research_depoix_1964]: https://doi.org/10.1111/j.1559-3584.1964.tb04751.x
[research_deprez_warnant_2018]: https://doi.org/10.33012/2018.16078
[research_deresh_1982]: https://doi.org/10.21236/ada118194
[research_design_and_1989]: https://doi.org/10.2514/5.9781600861499.0001.0101
[research_design_and_2014]: https://doi.org/10.21535/5z0qts63
[research_design_and_2014_b]: https://doi.org/10.21535/hw14d376
[research_design_and_2015]: https://doi.org/10.21275/v4i11.nov151216
[research_design_constraints_1993]: https://doi.org/10.2514/6.1993-3951
[research_design_control_and]: https://doi.org/10.12681/eadd/43358
[research_design_objectives]: https://doi.org/10.4271/arp842c
[research_design_objectives_b]: https://doi.org/10.4271/arp842a
[research_design_of_1979]: https://doi.org/10.2514/6.1979-1842
[research_design_of_2013]: https://doi.org/10.1002/9781118568101.ch1
[research_design_of_2024]: https://doi.org/10.2514/5.9781624107290.0875.0910
[research_design_of_2024_b]: https://doi.org/10.25236/ajets.2024.070513
[research_desjardins_laananen_1980]: https://doi.org/10.21236/ada088441
[research_deslich_flick_2021]: https://doi.org/10.2514/6.2021-0607
[research_development_of_2022]: https://doi.org/10.36652/0869-4931-2022-76-12-545-550
[research_deverill_2000]: https://doi.org/10.21236/ada377958
[research_dewa_atami_2024]: https://doi.org/10.2478/fas-2024-0006
[research_dewispelare_stager_1981]: https://doi.org/10.2514/6.1981-1639
[research_dewispelare_stager_1983]: https://doi.org/10.2514/3.44870
[research_deyoung_1971]: https://doi.org/10.2514/3.59178
[research_di_mishra_2022]: https://doi.org/10.1109/tmech.2021.3085696
[research_diana_2015]: https://doi.org/10.1016/j.cstp.2015.04.007
[research_dickes_gingras_2002]: https://doi.org/10.21236/ada459237
[research_dickey_marek_1963]: https://doi.org/10.21236/ad0401718
[research_dickinson_goggin_2000]: https://doi.org/10.2514/6.2000-1743
[research_didomenico_biezad_1985]: https://doi.org/10.2514/6.1985-1788
[research_dieffenbach_1995]: https://doi.org/10.1117/12.211487
[research_diesel_1987]: https://doi.org/10.1002/j.2161-4296.1987.tb01500.x
[research_dietrich_2020]: https://doi.org/10.4324/9781003075080-10
[research_differential_carrier_1999]: https://doi.org/10.1109/acc.1999.782449
[research_diget_hasan_2022]: https://doi.org/10.1109/icuas54217.2022.9836179
[research_digges_1971]: https://doi.org/10.21236/ad0728647
[research_digman_2009]: https://doi.org/10.21236/ada539662
[research_dili_jinlingwang]: https://doi.org/10.1109/plans.2006.1650615
[research_dill_uijtdehaag_2016]: https://doi.org/10.1002/navi.134
[research_dill_young_2017]: https://doi.org/10.33012/2017.15023
[research_dinc_2021]: https://doi.org/10.20290/estubtdb.900786
[research_ding_2015]: https://doi.org/10.2991/icmmcce-15.2015.441
[research_ding_li_2015]: https://doi.org/10.5772/60142
[research_ding_tomlin_2009]: https://doi.org/10.2514/6.2009-5742
[research_ding_wang_2007]: https://doi.org/10.1017/s0373463307004316
[research_ding_wang_2010]: https://doi.org/10.1109/icece.2010.1117
[research_dixon_wickens_2005]: https://doi.org/10.1518/001872005774860005
[research_dlr_and_2020]: https://doi.org/10.12968/s1478-2774(22)50337-3
[research_doan]: https://doi.org/10.32657/10356/47560
[research_doane_2003]: https://doi.org/10.21236/ada417024
[research_doblhoff_1956]: https://doi.org/10.21236/ad0109767
[research_dodge_2015]: https://doi.org/10.21236/ad1019503
[research_dodofficeofinspectorgeneral_2015]: https://doi.org/10.21236/ad1004894
[research_doer_koenig_2020]: https://doi.org/10.1109/icuas48674.2020.9213925
[research_doggett_soistmann_1992]: https://doi.org/10.2514/3.46155
[research_doguet_rancourt_2023]: https://doi.org/10.17118/11143/21180
[research_doherty_butzel_1979]: https://doi.org/10.21236/adb049493
[research_doherty_butzel_1979_b]: https://doi.org/10.21236/adb049608
[research_doherty_costello_2023]: https://doi.org/10.1109/icuas57906.2023.10156598
[research_doherty_heintz_2013]: https://doi.org/10.1142/s2301385013500052
[research_dong_huang_2017]: https://doi.org/10.21629/jsee.2017.05.14
[research_dong_shao_2021]: https://doi.org/10.2514/1.c036404
[research_dong_wang_2020]: https://doi.org/10.3390/s20020561
[research_dong_zhang_2020]: https://doi.org/10.1007/s10291-020-0969-1
[research_dongkangsheng_huangchangqiang_2016]: https://doi.org/10.1109/cgncc.2016.7828848
[research_donley_1980]: https://doi.org/10.4271/801205
[research_donmez_brzezinski_2008]: https://doi.org/10.21236/ada531512
[research_donmez_cummings_2009]: https://doi.org/10.1177/0018720809347106
[research_donmez_cummings_2010]: https://doi.org/10.1145/2377576.2377580
[research_dorobantu_murch_2013]: https://doi.org/10.2514/1.c032065
[research_dou_duan_2017]: https://doi.org/10.1016/j.ast.2016.11.012
[research_douglasaircraftcolongbeachca_1963]: https://doi.org/10.21236/ad0406168
[research_douglasaircraftcolongbeachca_1983]: https://doi.org/10.21236/ada133628
[research_douma_wang_2021]: https://doi.org/10.2514/6.2021-2378
[research_dowling_costello_2017]: https://doi.org/10.2514/6.2017-3882
[research_downs_2009]: https://doi.org/10.3940/rina.ws.2009.02
[research_draper_2008]: https://doi.org/10.1177/154193120805200114
[research_draper_buck_1983]: https://doi.org/10.2514/6.1983-1054
[research_dress_boyden_1992]: https://doi.org/10.2514/6.1992-5009
[research_dresser_newberry_1990]: https://doi.org/10.2514/6.1990-3213
[research_drewiacki_moreira_2025]: https://doi.org/10.2514/6.2025-1440
[research_drinkwateriii_rolls_1965]: https://doi.org/10.2514/6.1965-782
[research_drummond_1971]: https://doi.org/10.21236/ad0729870
[research_drusinsky_michael_2022]: https://doi.org/10.1109/issrew55968.2022.00089
[research_du_li_2019]: https://doi.org/10.1016/j.ast.2019.01.001
[research_du_yang_2004]: https://doi.org/10.1201/9780203022528-149
[research_duan_2013]: https://doi.org/10.1007/978-3-642-41196-0_5
[research_duan_chen_2022]: https://doi.org/10.1109/taes.2022.3168247
[research_duan_sun_2021]: https://doi.org/10.1109/taes.2020.3034026
[research_duan_yuan_2022]: https://doi.org/10.1109/taes.2022.3156070
[research_duan_zhao_2015]: https://doi.org/10.1590/s1982-21702015000400049
[research_duan_zhao_2016]: https://doi.org/10.17706/jcp.11.1.52-61
[research_dubicki_gorospe_2026]: https://doi.org/10.1109/syscon66367.2026.11503579
[research_dudek_schulte_2022]: https://doi.org/10.5220/0011946500003622
[research_duggan_bhandari_2021]: https://doi.org/10.1109/icuas51884.2021.9476857
[research_duhamel_1989]: https://doi.org/10.2514/6.1989-2274
[research_dukes_1970]: https://doi.org/10.21236/ad0871424
[research_duncan_ferrier_2006]: https://doi.org/10.4050/vfs-f62-097
[research_duongnguyen_kashitani_2022]: https://doi.org/10.2514/1.c036154
[research_duraklar_2024]: https://doi.org/10.2139/ssrn.5002520
[research_durand_teper_1964]: https://doi.org/10.21236/ad0606040
[research_durand_wasicko_1965]: https://doi.org/10.2514/6.1965-791
[research_durand_wasicko_1967]: https://doi.org/10.2514/3.43812
[research_durmus_duymaz_2023]: https://doi.org/10.1007/978-3-031-32639-4_26
[research_durmusoglu_2026]: https://doi.org/10.3390/math14122195
[research_dwisetiawan_aldino_2026]: https://doi.org/10.54317/oto.v5i2.542
[research_dynamics_of_2015]: https://doi.org/10.2307/j.ctt1287kgx.6
[research_dynamics_of_2023]: https://doi.org/10.1017/9781108354868.010
[research_dynamics_of_2023_b]: https://doi.org/10.1017/9781108354868.005
[research_dynamics_of_2023_c]: https://doi.org/10.1017/9781108354868.006
[research_dynamics_of_2023_d]: https://doi.org/10.1017/9781108354868.007
[research_dynnikov_2020]: https://doi.org/10.1201/9780429070372-59
[research_eads_and_2007]: https://doi.org/10.1108/aeat.2007.12779cab.035
[research_early_conceptual_2013]: https://doi.org/10.1002/9781118568101.ch2
[research_eaton_chen_2015]: https://doi.org/10.1109/icuas.2015.7152268
[research_ebneabbasi_makarov_2024]: https://doi.org/10.1016/j.ijhydene.2023.12.056
[research_ebrahimifakhari_moshtaghzadeh_2024]: https://doi.org/10.2514/6.2024-2461
[research_eckels_1983]: https://doi.org/10.2514/6.1983-2463
[research_eco_demonstrator_2018]: https://doi.org/10.12968/s1478-2774(23)50032-6
[research_edelbaum_1963]: https://doi.org/10.2514/6.1963-154
[research_edge_brown_2011]: https://doi.org/10.1007/978-94-007-3033-5_41
[research_edge_collins_2010]: https://doi.org/10.21236/ada513823
[research_edwan_zhou_2012]: https://doi.org/10.1002/navi.7
[research_edwards_lennieo_1990]: https://doi.org/10.21236/ada225454
[research_effect_of_2010]: https://doi.org/10.2514/5.9781600867552.0375.0442
[research_effective_gps_positioning_2012]: https://doi.org/10.4156/jcit.vol7.issue9.31
[research_effing_schueltke_2023]: https://doi.org/10.2514/6.2023-1356
[research_eichorn_1989]: https://doi.org/10.21236/ada207015
[research_eigenmann_kitzmiller_1984]: https://doi.org/10.2514/6.1984-1215
[research_eisenreich_2009]: https://doi.org/10.21236/ada539694
[research_eisler]: https://doi.org/10.22215/etd/2004-05725
[research_ekici_dalkiran_2023]: https://doi.org/10.1007/978-3-031-29933-9_1
[research_elchynski_kirkland]: https://doi.org/10.1109/plans.1998.670203
[research_eldiasty_pagiatakis_2010]: https://doi.org/10.1017/s0373463310000226
[research_electric_aircraft_2024]: https://doi.org/10.2514/5.9781624107290.0771.0796
[research_electricity_in_1954]: https://doi.org/10.1049/sqj.1954.0089
[research_elena_2026]: https://doi.org/10.1007/s42401-026-00535-5
[research_elferik_2020]: https://doi.org/10.1109/access.2020.3000774
[research_elham_bahamondejacome_2016]: https://doi.org/10.2514/6.2016-1660
[research_elias_1985]: https://doi.org/10.1002/j.2161-4296.1985.tb00887.x
[research_elisov_ishkov_2018]: https://doi.org/10.1063/1.5081547
[research_elkhoury_2008]: https://doi.org/10.2514/1.32609
[research_elkhoury_2016]: https://doi.org/10.2514/1.c033576
[research_elkhoury_nakad_2009]: https://doi.org/10.2514/1.42154
[research_elkhoury_rockwell_2004]: https://doi.org/10.2514/1.6290
[research_elkhoury_yavuz_2005]: https://doi.org/10.2514/1.9777
[research_eller_cavanagh_2000]: https://doi.org/10.21236/ada389009
[research_ellingson_brink_2018]: https://doi.org/10.1109/plans.2018.8373454
[research_ellingson_brink_2020]: https://doi.org/10.1002/navi.364
[research_elliott_2009]: https://doi.org/10.21236/ada517779
[research_elliott_dogan_2009]: https://doi.org/10.2514/6.2009-5602
[research_ellis_1976]: https://doi.org/10.2514/6.1976-908
[research_elmowafy_2005]: https://doi.org/10.5081/jgps.4.1.2
[research_elmowafy_2008]: https://doi.org/10.1109/plans.2008.4570105
[research_elmowafy_imparato_2018]: https://doi.org/10.33012/2018.16028
[research_elsayed_elhelw_2012]: https://doi.org/10.1109/icinfa.2012.6246780
[research_eltin_sharf_2022]: https://doi.org/10.1109/icuas54217.2022.9836074
[research_enboshi_2012]: https://doi.org/10.1109/mic.2012.6273443
[research_ender_mcclure_2002]: https://doi.org/10.2514/6.2002-5856
[research_energy_approach_2003]: https://doi.org/10.2514/5.9781600861840.0143.0151
[research_engdahl_2004]: https://doi.org/10.21236/ada422807
[research_enge_1999]: https://doi.org/10.1109/5.736345
[research_engineering_institutions_1998]: https://doi.org/10.1108/aeat.1998.12770aab.021
[research_englebry_1980]: https://doi.org/10.2514/6.1980-1878
[research_englebry_1981]: https://doi.org/10.2514/3.57593
[research_englezou_timotheou_2022]: https://doi.org/10.1109/icuas54217.2022.9836098
[research_enkhtur_2013]: https://doi.org/10.4218/etrij.13.0212.0540
[research_environmental_control]: https://doi.org/10.4271/air7063
[research_epp_2024]: https://doi.org/10.32920/25336336.v1
[research_epperson_2010]: https://doi.org/10.21236/ad1019093
[research_eppley_2012]: https://doi.org/10.21236/ada566064
[research_erdman_mitchum_2013]: https://doi.org/10.21236/ada612970
[research_erel_1988]: https://doi.org/10.2514/3.45535
[research_ericsson_1997]: https://doi.org/10.2514/2.2192
[research_ericsson_1998]: https://doi.org/10.2514/2.2399
[research_erkec_hajiyev_2020]: https://doi.org/10.1504/ijsa.2020.112637
[research_ernest_carroll_2016]: https://doi.org/10.4172/2167-0374.1000144
[research_ernest_cohen_2016]: https://doi.org/10.4172/2167-0374.1000139
[research_ertler]: https://doi.org/10.31274/rtd-20201118-152
[research_esdras_liscouethanke_2013]: https://doi.org/10.4271/2013-01-2206
[research_essari_2018]: https://doi.org/10.21467/proceedings.4.35
[research_essari_2018_b]: https://doi.org/10.59743/aujas.v3i1.1613
[research_essari_ghatus_2023]: https://doi.org/10.59992/ijsr.2023.v2n12p12
[research_estimating_the_2010]: https://doi.org/10.2514/5.9781600867538.0151.0169
[research_eubank_atkins_2011]: https://doi.org/10.2514/6.2011-1614
[research_evaluation_of_1979]: https://doi.org/10.2514/6.1979-1708
[research_evangelou_1998]: https://doi.org/10.1049/cp:19980616
[research_experimental_investigation_2023]: https://doi.org/10.1063/5.0147213
[research_fahimi_2005]: https://doi.org/10.21236/ada437212
[research_fahimi_thakur_2013]: https://doi.org/10.1109/icuas.2013.6564708
[research_faiz_agarwal_1998]: https://doi.org/10.2514/6.1998-4500
[research_falcone_clark_1974]: https://doi.org/10.21236/ad0784595
[research_falkenberg_hartt]: https://doi.org/10.1109/plans.1994.303324
[research_fan_jiang_2021]: https://doi.org/10.1007/978-981-15-8155-7_129
[research_fang_kim_2018]: https://doi.org/10.5302/j.icros.2018.0079
[research_fant_2001]: https://doi.org/10.21236/ada393597
[research_farajollahi_markazi_2010]: https://doi.org/10.1109/iccet.2010.5486075
[research_farid_mouhoub_2023]: https://doi.org/10.1109/icuas57906.2023.10155896
[research_farmani_sun_2015]: https://doi.org/10.1109/icuas.2015.7152315
[research_farokhi_1998]: https://doi.org/10.1016/s1369-8869(98)00012-3
[research_farrell_vangraas_2001]: https://doi.org/10.1002/j.2161-4296.2001.tb00235.x
[research_fegely_xin_2017]: https://doi.org/10.4050/sm_2017_hq-2372
[research_feibinhsiao_shihhsienhuang_2003]: https://doi.org/10.1109/rast.2003.1303946
[research_felix_gomes_2019]: https://doi.org/10.1080/0305215x.2019.1639691
[research_felter_wu_1997]: https://doi.org/10.1109/7.599319
[research_felux_dautermann_2013]: https://doi.org/10.1108/aeat-07-2012-0115
[research_feng_2001]: https://doi.org/10.1007/pl00012882
[research_feng_jokinen_2015]: https://doi.org/10.1007/s10291-015-0506-9
[research_feng_li_2018]: https://doi.org/10.3390/s18061919
[research_feng_ochieng_2011]: https://doi.org/10.1017/s037346331100052x
[research_fenwick_1966]: https://doi.org/10.21236/ad0737274
[research_ferrando_perez_1999]: https://doi.org/10.1109/7.805440
[research_ferrier_baitis_2000]: https://doi.org/10.1111/j.1559-3584.2000.tb03338.x
[research_ferrier_christmas_2024]: https://doi.org/10.4050/f-0080-2024-1058
[research_ferrier_duncan_2006]: https://doi.org/10.4050/vfs-f62-014
[research_ferrier_duncan_2012]: https://doi.org/10.21236/ada557352
[research_ferrier_ernst_2015]: https://doi.org/10.4050/f-0071-2015-10296
[research_ferrier_watson_2025]: https://doi.org/10.4050/sm_avtol_2025-5315
[research_fezans_jann_2017]: https://doi.org/10.2514/6.2017-4008
[research_fibre_ropes]: https://doi.org/10.3403/30292362u
[research_fidan_mostafa_2024]: https://doi.org/10.23919/ecc64448.2024.10590912
[research_field_rossitto_1999]: https://doi.org/10.2514/6.1999-4095
[research_fielding_vaziryz_1995]: https://doi.org/10.2514/6.1995-3906
[research_fierro_branca]: https://doi.org/10.1109/icnsc.2005.1461278
[research_figge_1973]: https://doi.org/10.21236/ad0781810
[research_figge_bernhardt_1975]: https://doi.org/10.2514/3.59854
[research_figliola_2004]: https://doi.org/10.21236/ada431388
[research_figliola_2005]: https://doi.org/10.21236/ada435403
[research_fikes_1996]: https://doi.org/10.1002/j.2161-4296.1996.tb01919.x
[research_firing]: https://doi.org/10.1109/oceans.1991.627945
[research_firuzabadi_king_2011]: https://doi.org/10.1007/s10291-011-0218-8
[research_fisch_lenz_2012]: https://doi.org/10.2514/6.2012-4598
[research_fischer_2006]: https://doi.org/10.21236/ada449436
[research_fisher_1950]: https://doi.org/10.1108/eb031908
[research_fisher_vanzwieten_2010]: https://doi.org/10.1109/oceanssyd.2010.5603649
[research_fladelandmatt_schoenungsusan_2019]: https://ntrs.nasa.gov/citations/20190032041
[research_flansburg_2015]: https://doi.org/10.2514/6.2015-0457
[research_flansburg_2016]: https://doi.org/10.2514/6.2016-0232
[research_fleming_ng_2004]: https://doi.org/10.2514/1.11486
[research_flexible_wing_2007]: https://doi.org/10.1108/aeat.2007.12779bad.016
[research_flight_control]: https://doi.org/10.4271/as425a
[research_flight_deck]: https://doi.org/10.4271/arp4101/7
[research_flight_deck_b]: https://doi.org/10.4271/arp4101/8
[research_flight_deck_c]: https://doi.org/10.4271/arp1068b
[research_flight_deck_d]: https://doi.org/10.4271/as290
[research_flight_deck_e]: https://doi.org/10.4271/arp4103b
[research_flight_deck_f]: https://doi.org/10.4271/arp4103a
[research_flight_deck_g]: https://doi.org/10.4271/arp571c
[research_flight_dynamics_2014]: https://doi.org/10.1201/b17346-14
[research_flight_envelope]: https://doi.org/10.4271/arp4104/1
[research_flight_test_1970]: https://doi.org/10.1108/eb034622
[research_flow_control_2016]: https://doi.org/10.21152/1750-9548.10.2.117
[research_floyd_2000]: https://doi.org/10.21236/ada388189
[research_foch_1992]: https://doi.org/10.2514/6.1992-4078
[research_foch_toot_1989]: https://doi.org/10.1007/978-3-642-84010-4_30
[research_fofonov_2021]: https://doi.org/10.33257/phchgd.22.6.965
[research_fong_1982]: https://doi.org/10.21236/ada123291
[research_fong_self]: https://doi.org/10.18260/1-2-1153-52380
[research_fontaine]: https://doi.org/10.70675/b40dd64cz1454z45b1z8213z795a90beef23
[research_foreigntechnologydivwrightpattersonafboh_1973]: https://doi.org/10.21236/ada032206
[research_forrester]: https://doi.org/10.22215/etd/2011-07308
[research_forsmo_grotli_2013]: https://doi.org/10.1109/icuas.2013.6564697
[research_fortenbaugh_1972]: https://doi.org/10.2514/6.1972-873
[research_foss_2026]: https://doi.org/10.2139/ssrn.6196618
[research_fosswejr_1981]: https://ntrs.nasa.gov/citations/19810011498
[research_fosswejr_1984]: https://ntrs.nasa.gov/citations/19830000631
[research_fracture_of_2019]: https://doi.org/10.31399/asm.fach.aero.c0046022
[research_fradenburgh_1991]: https://doi.org/10.4271/911974
[research_franco_correia_2019]: https://doi.org/10.1109/icuas.2019.8798217
[research_frau_2022]: https://doi.org/10.4337/9781788111904.00041
[research_frederick_jr_2001]: https://doi.org/10.21236/ada397957
[research_frederick_jr_2001_b]: https://doi.org/10.21236/ada397955
[research_frederick_jr_2001_c]: https://doi.org/10.21236/ada397956
[research_frederick_jr_2002]: https://doi.org/10.21236/ada407956
[research_frederick_roberta_2001]: https://doi.org/10.21236/ada397958
[research_freeway_incident_2024]: https://doi.org/10.5038/cutr-nicr-y3-4-7
[research_frew_brown]: https://doi.org/10.1007/978-1-4020-9137-7_3
[research_frew_lawrence_2005]: https://doi.org/10.2514/6.2005-6363
[research_frey_2011]: https://doi.org/10.21236/ada547454
[research_friedrich_vollrath_2022]: https://doi.org/10.1016/j.displa.2022.102185
[research_fronterasanchez]: https://doi.org/10.20868/upm.thesis.40622
[research_frost_1968]: https://doi.org/10.21236/ada020223
[research_frost_1995]: https://doi.org/10.7249/rb29
[research_frost_franklin_2002]: https://doi.org/10.2514/6.2002-6016
[research_frost_walters_2021]: https://doi.org/10.2514/6.2021-2769
[research_frounfelker_belencan_1984]: https://doi.org/10.21236/ada147415
[research_frulla_2021]: https://doi.org/10.37394/232010.2021.18.7
[research_fry_2008]: https://doi.org/10.21236/ada494062
[research_frye_1984]: https://doi.org/10.1002/j.2161-4296.1984.tb00882.x
[research_fu_1972]: https://doi.org/10.21236/ada014224
[research_fu_carrio_2014]: https://doi.org/10.1109/icuas.2014.6842309
[research_fu_sun_2023]: https://doi.org/10.1007/978-981-19-6613-2_130
[research_fu_zhang_2015]: https://doi.org/10.3390/s150922854
[research_fuchs_ferreira_2013]: https://doi.org/10.1007/978-3-642-39330-3_73
[research_fuchser_1984]: https://doi.org/10.21236/ada145135
[research_fuel_cell_2007]: https://doi.org/10.1108/aeat.2007.12779daf.013
[research_fuhrmann_koch]: https://doi.org/10.1109/itsc.2005.1520015
[research_fukuda_takimoto_2014]: https://doi.org/10.1109/iccas.2014.6987817
[research_fukushima_tsubone_2019]: https://doi.org/10.1109/isocc47750.2019.9027701
[research_fuli_yumeixiang_2008]: https://doi.org/10.1109/ccdc.2008.4598037
[research_furnish_anders_1971]: https://doi.org/10.4271/710401
[research_further_development_1994]: https://doi.org/10.2514/6.1994-2141
[research_fuselages_and_2017]: https://doi.org/10.1002/9781119406303.ch4
[research_fusion_of_2012]: https://doi.org/10.2514/6.2012-2480
[research_g_gowda_2024]: https://doi.org/10.4271/2024-26-0442
[research_g_mnvss_2016]: https://doi.org/10.21817/ijet/2016/v8i6/160806229
[research_gabriele_1991]: https://doi.org/10.2514/6.1991-3099
[research_gacy_2011]: https://doi.org/10.21236/ada550675
[research_gage_1994]: https://doi.org/10.21236/ada422537
[research_gaitanakis_limnaios_2020]: https://doi.org/10.1108/aeat-01-2020-0011
[research_galdos_upadhyay]: https://doi.org/10.1109/ntc.1993.292992
[research_gall_caverly_2025]: https://doi.org/10.2514/6.2025-99106
[research_galloway_1989]: https://doi.org/10.4050/sm_rotary_1989-1589
[research_galloway_dey_2015]: https://doi.org/10.1109/acc.2015.7172080
[research_galway_2008]: https://doi.org/10.21236/ada530597
[research_galway_2008_b]: https://doi.org/10.21236/ada530598
[research_gan_fang_2021]: https://doi.org/10.3390/app11125445
[research_gandolfi_tavasci_2016]: https://doi.org/10.1007/s10291-016-0575-4
[research_gannanyuan_taozhang_2009]: https://doi.org/10.1109/icma.2009.5244821
[research_gao_an_2021]: https://doi.org/10.1016/b978-0-12-822990-3.00003-6
[research_gao_hu_2021]: https://doi.org/10.3390/act10050099
[research_gao_kang_2016]: https://doi.org/10.1007/978-981-10-2875-5_66
[research_gao_li_2019]: https://doi.org/10.3390/s19020417
[research_gao_luo_2024]: https://doi.org/10.2139/ssrn.4923748
[research_garcia_caballero_2020]: https://doi.org/10.1109/icuas48674.2020.9213883
[research_garcia_keshmiri_2017]: https://doi.org/10.1109/icuas.2017.7991395
[research_gardi_ramasamy_2015]: https://doi.org/10.1109/icuas.2015.7152314
[research_gardi_ramasamy_2016]: https://doi.org/10.1109/icuas.2016.7502670
[research_gardi_sabatini_2016]: https://doi.org/10.1109/icuas.2016.7502677
[research_gardner_poehlman_1999]: https://doi.org/10.21236/ada378683
[research_garmendia_chakraborty_2016]: https://doi.org/10.2514/1.c033390
[research_garrard_zhang_2025]: https://doi.org/10.1109/icuas65942.2025.11007921
[research_gary_1983]: https://doi.org/10.21236/ada137910
[research_gasaway_1969]: https://doi.org/10.21236/ad0702422
[research_gates_1949]: https://doi.org/10.1108/eb031750
[research_gates_1992]: https://doi.org/10.21236/ada264502
[research_gautam_sujit_2014]: https://doi.org/10.1109/icuas.2014.6842377
[research_gaver_jacobs_1998]: https://doi.org/10.21236/ada354015
[research_gavrilovski_ward_2011]: https://doi.org/10.2514/6.2011-2517
[research_gaylor_lightsey_2003]: https://doi.org/10.2514/6.2003-5445
[research_gazzino_lelarge_2024]: https://doi.org/10.33012/2024.19722
[research_ge_gendt_2005]: https://doi.org/10.1007/s00190-005-0447-0
[research_gebreegziabher_2011]: https://doi.org/10.21236/ada578999
[research_geisler_rosikon_2014]: https://doi.org/10.2478/ama-2014-0023
[research_geister_geister_2013]: https://doi.org/10.1002/navi.40
[research_general_requirements]: https://doi.org/10.3403/30408094u
[research_general_requirements_b]: https://doi.org/10.3403/30408088u
[research_generic_aircraft_2017]: https://doi.org/10.1002/9781119406303.app1
[research_geng_deurloo_2010]: https://doi.org/10.1007/s10291-010-0190-8
[research_geng_li_2006]: https://doi.org/10.1117/12.712665
[research_geng_wang_2007]: https://doi.org/10.1007/s10291-007-0084-6
[research_geng_xie_2017]: https://doi.org/10.1007/s10291-017-0602-0
[research_genrich_minster_1991]: https://doi.org/10.1190/1.1443008
[research_george_ghose_2009]: https://doi.org/10.1109/acc.2009.5160241
[research_georghiou_metcalfe_1986]: https://doi.org/10.1007/978-1-349-07455-6_35
[research_georgy_iqbal_2009]: https://doi.org/10.1109/isma.2009.5164810
[research_gerken_1979]: https://doi.org/10.21236/ada132587
[research_german_hypersonics_1993]: https://doi.org/10.2514/6.1993-5094
[research_germond_2025]: https://doi.org/10.64628/ab.an7hfe3gw
[research_getiryaman_ribeiro_2025]: https://doi.org/10.1016/j.jss.2024.112229
[research_geva_abramovich_2019]: https://doi.org/10.3390/aerospace6080085
[research_ghadge_s_2021]: https://doi.org/10.1108/aeat-12-2020-0305
[research_ghaemi_lax_2019]: https://doi.org/10.2514/6.2019-3617
[research_ghiringhelli_2000]: https://doi.org/10.2514/2.2672
[research_ghoshdastidar_frazzoli_2011]: https://doi.org/10.2514/6.2011-1514
[research_gibson_alexander_1968]: https://doi.org/10.21236/ad0665328
[research_giles_1986]: https://doi.org/10.2514/3.45393
[research_giles_1995]: https://doi.org/10.2514/6.1995-3945
[research_gilge_2010]: https://doi.org/10.21236/ada536682
[research_gilhool_2005]: https://doi.org/10.21236/ada437595
[research_gillard_1998]: https://doi.org/10.21236/ada362903
[research_gillard_dorsett_1997]: https://doi.org/10.2514/6.1997-3487
[research_gillett_1994]: https://doi.org/10.21236/ada288289
[research_gillman_2015]: https://doi.org/10.1353/ect.2015.0019
[research_giorgi_gteunisse_2012]: https://doi.org/10.5772/38381
[research_girish_emilio_2014]: https://doi.org/10.1007/978-90-481-9707-1_87
[research_giunta_1999]: https://doi.org/10.1016/s1369-8869(99)00016-6
[research_gkn_westland_1999]: https://doi.org/10.1108/aeat.1999.12771aab.064
[research_glaner_weber_2021]: https://doi.org/10.1007/s10291-021-01140-z
[research_glaner_weber_2021_b]: https://doi.org/10.1007/s10291-021-01159-2
[research_go_ramnath_2001]: https://doi.org/10.2514/6.2001-4426
[research_goad]: https://doi.org/10.1109/plans.1990.66187
[research_goddard_eastgate_2010]: https://doi.org/10.21236/ada554344
[research_godha_cannon_2007]: https://doi.org/10.1007/s10291-006-0050-8
[research_goerttler_schnepf_2024]: https://doi.org/10.2514/1.c037360
[research_gold_1973]: https://doi.org/10.2514/6.1973-917
[research_gold_1974]: https://doi.org/10.2514/3.60407
[research_gold_walchli_1974]: https://doi.org/10.2514/6.1974-952
[research_goldstein_1982]: https://doi.org/10.4050/sm_handling_1982-4947
[research_golombek_bustamante_2025]: https://doi.org/10.21203/rs.3.rs-6227073/v1
[research_golombek_bustamante_2026]: https://doi.org/10.1007/s13272-026-00996-6
[research_gomez_lacourharbo_2021]: https://doi.org/10.1109/icuas51884.2021.9476792
[research_goncharenko_lebedev_2019]: https://doi.org/10.1109/mlsd.2019.8911094
[research_gong_wang_2019]: https://doi.org/10.1088/1742-6596/1215/1/012001
[research_gong_xu_2022]: https://doi.org/10.1142/s2301385023410029
[research_gonzalez_2013]: https://doi.org/10.21236/ada583878
[research_goodall_syed_2006]: https://doi.org/10.1109/vtcf.2006.578
[research_goodner_rao_1988]: https://doi.org/10.2514/6.1988-4502
[research_gopejenko_sidenko_2026]: https://doi.org/10.2478/lpts-2026-0027
[research_gopinath_bakshi_2020]: https://doi.org/10.4135/9781529792720
[research_gordnier_sherer_2007]: https://doi.org/10.1109/hpcmp-ugc.2007.23
[research_gordnier_visbal]: https://doi.org/10.1109/dodugc.2005.34
[research_gordnier_visbal_1994]: https://doi.org/10.2514/3.46480
[research_gordnier_visbal_2006]: https://doi.org/10.1109/hpcmp-ugc.2006.33
[research_gorgulu_yazar_2023]: https://doi.org/10.1007/978-3-031-29933-9_9
[research_gorin_gubankov_2024]: https://doi.org/10.1109/rusautocon61949.2024.10694649
[research_goth]: https://doi.org/10.22215/etd/2010-11329
[research_gou_dahl_2021]: https://doi.org/10.5220/0010655500003061
[research_goudarzi_richards_2020]: https://doi.org/10.1109/icuas48674.2020.9213870
[research_goughjr_carlson_1979]: https://doi.org/10.2514/6.1979-92
[research_gould_2001]: https://doi.org/10.2514/6.2001-369
[research_gould_2004]: https://doi.org/10.21236/ada508661
[research_govan_griffith_2018]: https://doi.org/10.1007/978-3-319-32193-6_154-1
[research_govindarajan_sridharan_2020]: https://doi.org/10.2514/1.c035805
[research_goyal_2026]: https://doi.org/10.4271/2026-26-0773
[research_gps]: https://doi.org/10.1007/978-3-211-73017-1_9
[research_gps_receiver_2005]: https://doi.org/10.1108/aeat.2005.12777dad.006
[research_gps_segments_2013]: https://doi.org/10.4324/9780080941523-111
[research_gps_signals_2013]: https://doi.org/10.4324/9780080941523-112
[research_grace_1992]: https://doi.org/10.21236/ada263357
[research_grafarend_2000]: https://doi.org/10.1007/pl00012840
[research_grafarend_2003]: https://doi.org/10.1007/978-3-662-05296-9_32
[research_graham_gonzalez_2023]: https://doi.org/10.1109/icuas57906.2023.10156493
[research_grant_lind_2010]: https://doi.org/10.2514/6.2010-8203
[research_grantham_williams_1987]: https://doi.org/10.2514/6.1987-2290
[research_grappel_harris_2008]: https://doi.org/10.21236/ada489387
[research_grasso_1994]: https://doi.org/10.2514/6.1994-1619
[research_graves_snow_2023]: https://doi.org/10.2514/6.2023-4323
[research_gray_2005]: https://doi.org/10.21236/ada435692
[research_gray_2015]: https://doi.org/10.21236/ad1003560
[research_gray_maybeck]: https://doi.org/10.1109/naecon.1995.521930
[research_greaney_2010]: https://doi.org/10.21236/ada522950
[research_green_1998]: https://doi.org/10.21236/ada388031
[research_green_findlay_2016]: https://doi.org/10.2514/6.2016-1768
[research_green_zanine_1984]: https://doi.org/10.4271/841555
[research_greenhaw_2008]: https://doi.org/10.2514/6.2008-7102
[research_greer_campbell_1980]: https://doi.org/10.21236/ada092458
[research_gregory_kim_2022]: https://doi.org/10.21236/ad1171274
[research_gregory_tierno_1996]: https://doi.org/10.2514/6.1996-3860
[research_gregorytj_wilcoxde_1970]: https://ntrs.nasa.gov/citations/19700064255
[research_grejnerbrzezinska_wang_1998]: https://doi.org/10.1002/j.2161-4296.1998.tb02383.x
[research_grepper_huguenin_1979]: https://doi.org/10.2514/6.1979-1776
[research_grigsby_2008]: https://doi.org/10.21236/ada493705
[research_grimm_1986]: https://doi.org/10.1109/cdc.1986.267420
[research_grisworld_2008]: https://doi.org/10.21236/ada490208
[research_gross_gu_2010]: https://doi.org/10.2514/6.2010-8332
[research_gross_gu_2010_b]: https://doi.org/10.2514/6.2010-7759
[research_grosser_1965]: https://doi.org/10.2514/6.1965-789
[research_grotte_brooks_1982]: https://doi.org/10.21236/ada121599
[research_grover_1966]: https://doi.org/10.21236/ad0660529
[research_grunch_2000]: https://doi.org/10.21236/ada388366
[research_grzegorzewski_sliwak_2016]: https://doi.org/10.1515/aon-2016-0018
[research_grzesik_sobolewski_2014]: https://doi.org/10.3846/16487788.2014.865947
[research_gu_enoiu_2023]: https://doi.org/10.1109/icstw58534.2023.00017
[research_guangcai_xu_2021]: https://doi.org/10.1109/tim.2020.3021224
[research_gudmundsson_2014]: https://doi.org/10.1016/b978-0-12-397308-5.00003-9
[research_gudmundsson_2014_b]: https://doi.org/10.1016/b978-0-12-397308-5.00004-0
[research_gudmundsson_2014_c]: https://doi.org/10.1016/b978-0-12-397308-5.00006-4
[research_gudmundsson_2014_d]: https://doi.org/10.1016/b978-0-12-397308-5.00001-5
[research_gudmundsson_2022]: https://doi.org/10.1016/b978-0-12-818465-3.00027-6
[research_gudmundsson_2022_b]: https://doi.org/10.1016/b978-0-12-818465-3.00006-9
[research_gudmundsson_2022_c]: https://doi.org/10.1016/b978-0-12-818465-3.00001-x
[research_guelman_2014]: https://doi.org/10.1016/j.actaastro.2013.12.009
[research_guerrero_2012]: https://doi.org/10.1002/9781118387191.ch7
[research_guidance_on_2001]: https://doi.org/10.1108/aeat.2001.12773baf.006
[research_guide_for]: https://doi.org/10.4271/air4004a
[research_guide_for_b]: https://doi.org/10.1520/f2541
[research_guide_for_c]: https://doi.org/10.1520/f3199-16a
[research_guiler]: https://doi.org/10.33915/etd.2779
[research_guiler_huebsch_2005]: https://doi.org/10.4271/2005-01-3391
[research_guiler_huebsch_2005_b]: https://doi.org/10.2514/6.2005-4981
[research_guillen_bell]: https://doi.org/10.18260/1-2-110.1147-46351
[research_gunawardana_alonso_2013]: https://doi.org/10.2514/6.2013-1035
[research_gunetti_thompson_2013]: https://doi.org/10.2514/1.53282
[research_guo_2007]: https://doi.org/10.1016/j.ast.2007.01.003
[research_guo_2013]: https://doi.org/10.11591/telkomnika.v11i3.2189
[research_guo_cain_2013]: https://doi.org/10.2316/journal.201.2013.4.201-2436
[research_guo_geng_2024]: https://doi.org/10.1007/s10291-023-01610-6
[research_guo_han_2023]: https://doi.org/10.1016/j.dt.2021.12.006
[research_guo_han_2026]: https://doi.org/10.23919/jsee.2026.000043
[research_guo_li_2025]: https://doi.org/10.1016/j.cja.2024.09.032
[research_guo_liu_2026]: https://doi.org/10.1007/s11704-025-50967-z
[research_guo_sun]: https://doi.org/10.1115/1.859810.paper38
[research_guo_yamamoto_2006]: https://doi.org/10.2514/1.11085
[research_guoqing_tiantian_2016]: https://doi.org/10.14257/ijca.2016.9.11.22
[research_guorongzhao_jixinli_2006]: https://doi.org/10.1109/wcica.2006.1712768
[research_gursoylu_sziroczak_2025]: https://doi.org/10.1007/978-3-032-00618-9_7
[research_guth_2015]: https://doi.org/10.21313/hawaii/9780824839598.003.0001
[research_gutt_fischer_2004]: https://doi.org/10.2514/6.2004-5027
[research_gwin_1976]: https://doi.org/10.2514/3.58668
[research_h_m_aircraft_carrier_1939]: https://doi.org/10.1038/143592c0
[research_ha_1995]: https://doi.org/10.2514/3.21454
[research_ha_2008]: https://doi.org/10.1109/atc.2008.4760625
[research_haak_1994]: https://doi.org/10.21236/ada288609
[research_haas_gorb_2000]: https://doi.org/10.1016/s1467-8039(00)00025-6
[research_habashi_2023]: https://doi.org/10.1007/978-3-030-64725-4_46-1
[research_hafer_2009]: https://doi.org/10.21236/ada539963
[research_hagele_soffker_2017]: https://doi.org/10.1109/icuas.2017.7991415
[research_haider_mansor_2023]: https://doi.org/10.1108/aeat-03-2022-0092
[research_haitao_yan_2021]: https://doi.org/10.1109/icrae53653.2021.9657814
[research_haiyangchao_yangquanchen_2010]: https://doi.org/10.1109/acc.2010.5530609
[research_hajiyev_aykuttutucu_2001]: https://doi.org/10.1016/s1474-6670(17)40778-6
[research_hajiyev_tutucu_2003]: https://doi.org/10.1109/rast.2003.1303978
[research_haley_1990]: https://doi.org/10.21236/ada222249
[research_hall_1971]: https://doi.org/10.4271/710374
[research_hamlin_1990]: https://doi.org/10.21236/ada241089
[research_hammack_mullen_1995]: https://doi.org/10.21236/ada300174
[research_hammond_1986]: https://doi.org/10.2514/6.1986-2733
[research_hamnanaka_2018]: https://doi.org/10.1109/icuas.2018.8453463
[research_han_2022]: https://doi.org/10.1088/1742-6596/2166/1/012005
[research_han_kang_2019]: https://doi.org/10.2514/1.c035298
[research_han_lee_2012]: https://doi.org/10.12673/jkoni.2012.16.6.927
[research_han_wang_2011]: https://doi.org/10.1007/s10291-011-0240-x
[research_han_wu_2026]: https://doi.org/10.1016/j.dt.2026.02.002
[research_han_xiao_2019]: https://doi.org/10.1108/ijicc-04-2018-0050
[research_han_xu_2016]: https://doi.org/10.3390/s16071057
[research_han_xu_2025]: https://doi.org/10.1088/1361-6501/adda6f
[research_han_zou_2026]: https://doi.org/10.1155/ijae/7696495
[research_handling_qualities_2000]: https://doi.org/10.2514/5.9781600866555.0119.0169
[research_handling_qualities_2008]: https://doi.org/10.1201/b15919-14
[research_handling_qualities_2017]: https://doi.org/10.4324/9781315255217-11
[research_hannshingju_chingchihtsai]: https://doi.org/10.1109/icmech.2005.1529379
[research_hao_huang_2009]: https://doi.org/10.1109/iwisa.2009.5072799
[research_hao_xu_2018]: https://doi.org/10.3390/s18113809
[research_hao_yongqi_2024]: https://doi.org/10.23919/ccc63176.2024.10662106
[research_hardy_strader_2016]: https://doi.org/10.1109/plans.2016.7479719
[research_harford_1989]: https://doi.org/10.21236/ada207401
[research_haritos_barnhart_2021]: https://doi.org/10.1201/9780429347498-20
[research_harley_wilde_2009]: https://doi.org/10.2514/6.2009-146
[research_harned_head_1965]: https://doi.org/10.4050/sm_vstol_1965-3034
[research_harper_1936]: https://doi.org/10.1080/03071843609422740
[research_harper_sardanowsky_1969]: https://doi.org/10.21236/ad0858184
[research_harris_1961]: https://doi.org/10.1049/jbire.1961.0005
[research_harris_gautrey_2000]: https://doi.org/10.1017/s0001924000028098
[research_hart_1956]: https://doi.org/10.21236/ad0108104
[research_hart_williams_2008]: https://doi.org/10.21236/ada477535
[research_hartana]: https://doi.org/10.22215/etd/2000-04613
[research_harting_1981]: https://doi.org/10.1111/j.1747-1567.1981.tb01597.x
[research_hartman_johnson_1998]: https://doi.org/10.1002/j.2161-4296.1998.tb02370.x
[research_hartmann_noland_2021]: https://doi.org/10.36227/techrxiv.17102792
[research_hartmann_schutt_2017]: https://doi.org/10.2514/6.2017-1914
[research_hartmann_scott_2024]: https://doi.org/10.4337/9781035312344.00005
[research_hartmann_scott_2024_b]: https://doi.org/10.4337/9781035312344.00021
[research_hartney]: https://doi.org/10.31979/etd.2nzx-arxy
[research_hassairi_abid_2021]: https://doi.org/10.5220/0010436900002994
[research_hatch_williamd_2007]: https://doi.org/10.21236/ada496678
[research_haugen_1966]: https://doi.org/10.2514/6.1966-1866
[research_hauschildt_gripp_1981]: https://doi.org/10.1115/81-gt-112
[research_hauser_1999]: https://doi.org/10.21236/ada387263
[research_havey_kline_1989]: https://doi.org/10.2514/6.1989-2020
[research_hawker_1991]: https://doi.org/10.21236/ada254257
[research_hawker_1992]: https://doi.org/10.21236/ada255374
[research_hawkins_1982]: https://doi.org/10.2514/6.1982-814
[research_hawkins_2017]: https://doi.org/10.4324/9781351218580-13
[research_haxhi_gikas_2023]: https://doi.org/10.3390/enc2023-15431
[research_hayase_1974]: https://doi.org/10.21236/ada002866
[research_hayase_1974_b]: https://doi.org/10.21236/ada002862
[research_hayes_2006]: https://doi.org/10.21236/ada463638
[research_hays_1989]: https://doi.org/10.2514/6.1989-2059
[research_hazlett_crassidis_2011]: https://doi.org/10.2514/6.2011-6577
[research_he_le_2013]: https://doi.org/10.1109/maes.2013.6642828
[research_he_wang_2026]: https://doi.org/10.2514/1.g009488
[research_he_xin_2004]: https://doi.org/10.4050/vfs-f60-000020
[research_head_hohenemser_1951]: https://doi.org/10.21236/ad0109764
[research_heffley_1986]: https://doi.org/10.2514/6.1986-2251
[research_heilenday_2000]: https://doi.org/10.21236/ada375233
[research_heimbs_lang_2012]: https://doi.org/10.2478/s13531-012-0002-8
[research_heit_liscouethanke_2023]: https://doi.org/10.2514/6.2023-1362
[research_heitmeir_lederer_1992]: https://doi.org/10.2514/6.1992-5057
[research_heller_1961]: https://doi.org/10.21236/ad0258024
[research_heller_dobrzynski_1976]: https://doi.org/10.2514/6.1976-552
[research_helliwell_1952]: https://doi.org/10.1017/s0001925900000688
[research_hemati_eldredge_2012]: https://doi.org/10.2514/6.2012-4768
[research_henderson_2023]: https://doi.org/10.3390/drones7010063
[research_henkel_gunther_2012]: https://doi.org/10.1002/navi.6
[research_henkel_zhu_2011]: https://doi.org/10.1109/ssp.2011.5967717
[research_henne_1989]: https://doi.org/10.2514/6.1989-2023
[research_henrickson_rogers_2016]: https://doi.org/10.1109/icuas.2016.7502652
[research_heo_pervan_2004]: https://doi.org/10.1002/j.2161-4296.2004.tb00350.x
[research_hept_2002]: https://doi.org/10.21236/ada420757
[research_herbst_klockner_2014]: https://doi.org/10.14323/ijuseng.2014.11
[research_herdiana_arifin_2023]: https://doi.org/10.1063/5.0115922
[research_hermann_evans_1995]: https://doi.org/10.1002/j.2161-4296.1995.tb01902.x
[research_hermanutz_hornung_2020]: https://doi.org/10.3390/aerospace7040045
[research_herpers_1965]: https://doi.org/10.1016/b978-1-4831-9818-7.50024-7
[research_herrera_2014]: https://doi.org/10.21236/ad1019180
[research_herrerarubio_parraprada_2019]: https://doi.org/10.22463/0122820x.1795
[research_herrmann_2004]: https://doi.org/10.2514/6.2004-4539
[research_hess_1981]: https://doi.org/10.2514/6.1981-1771
[research_hess_1984]: https://doi.org/10.2514/6.1984-236
[research_hess_2010]: https://doi.org/10.1002/9780470686652.eae258
[research_hess_2018]: https://doi.org/10.2514/1.c034596
[research_hess_2019]: https://doi.org/10.1016/j.ifacol.2019.01.017
[research_hess_judd_1976]: https://doi.org/10.2514/3.44514
[research_hewgley_cristi_2014]: https://doi.org/10.1109/plans.2014.6851505
[research_hewgley_yakimenko_2011]: https://doi.org/10.2514/6.2011-2573
[research_hewitson_kyulee_2004]: https://doi.org/10.1017/s0373463304002693
[research_hewitson_wang_2007]: https://doi.org/10.1017/s0373463307004134
[research_hewitt_weiss_2005]: https://doi.org/10.1520/stp11301s
[research_heyns_borden_2017]: https://doi.org/10.1093/oxfordhb/9780199300983.013.30
[research_hicks_1968]: https://doi.org/10.1111/j.1559-3584.1968.tb04546.x
[research_hicks_durbin_2014]: https://doi.org/10.21236/ada616169
[research_hicks_petrov_2002]: https://doi.org/10.21236/ada467481
[research_hide_moore]: https://doi.org/10.1109/plans.2004.1308998
[research_hide_moore_2003]: https://doi.org/10.1017/s0373463302002151
[research_high_altitude_1989]: https://doi.org/10.2514/6.1989-2109
[research_high_altitude_long_endurance_2026]: https://doi.org/10.2514/5.9781624107719.0007.0050
[research_high_lift_devices_2010]: https://doi.org/10.2514/5.9781600867538.0221.0253
[research_high_precision_gps_2011]: https://doi.org/10.1061/9780784411506.ch05
[research_hightower_1985]: https://doi.org/10.21236/ada163129
[research_hildebrand_1945]: https://doi.org/10.1093/milmed/96.6.485
[research_hill_1987]: https://doi.org/10.21236/ada186949
[research_hill_waters_1974]: https://doi.org/10.2514/6.1974-969
[research_hinchey_rash]: https://doi.org/10.1109/sew.2001.992667
[research_hinsz_2006]: https://doi.org/10.21236/ada460842
[research_hintzke_haggard_1991]: https://doi.org/10.2514/6.1991-836
[research_hirlinger_2001]: https://doi.org/10.21236/ada386073
[research_hirsch_schroeder_2014]: https://doi.org/10.1007/978-90-481-9707-1_112
[research_hirschel_1991]: https://doi.org/10.2514/6.1991-5041
[research_hirschel_1993]: https://doi.org/10.2514/6.1993-5072
[research_hirsh_1965]: https://doi.org/10.21236/ad0621684
[research_historical_design]: https://doi.org/10.4271/air5565
[research_history_of_2020]: https://doi.org/10.1002/9781119667063.ch1
[research_hiyama_1974]: https://doi.org/10.21236/ada002867
[research_hiyama_1974_b]: https://doi.org/10.21236/ada002868
[research_hobbs_2010]: https://doi.org/10.1016/b978-0-12-374518-7.00016-x
[research_hobbsalan_cardozacolleen_2016]: https://ntrs.nasa.gov/citations/20160011549
[research_hobe_heile_2026]: https://doi.org/10.5771/9783748941811-110
[research_hochstetler_bosma_2016]: https://doi.org/10.2514/6.2016-4223
[research_hodgart_purivigraipong]: https://doi.org/10.1109/plans.2000.838294
[research_hodgkinson_johnston_2018]: https://doi.org/10.4324/9781351332323
[research_hodgkinson_johnston_2018_b]: https://doi.org/10.4324/9781351332323-3
[research_hodgkinson_johnston_2018_c]: https://doi.org/10.4324/9781351332323-4
[research_hodgkinson_johnston_2018_d]: https://doi.org/10.4324/9781351332323-6
[research_hodgkinson_johnston_2018_e]: https://doi.org/10.4324/9781351332323-2
[research_hodgkinson_johnston_2018_f]: https://doi.org/10.4324/9781351332323-1
[research_hoffer_coopmans_2013]: https://doi.org/10.1109/icuas.2013.6564775
[research_hoffler_rao_1986]: https://doi.org/10.2514/6.1986-1838
[research_hoh_1988]: https://doi.org/10.2514/6.1988-4328
[research_hoh_mitchell_1983]: https://doi.org/10.21236/ada132857
[research_holcroft_christopher_2014]: https://doi.org/10.1093/ww/9780199540884.013.276528
[research_holland_lalejini_2009]: https://doi.org/10.21236/ada525035
[research_holloway_thompson_1972]: https://doi.org/10.2514/3.59030
[research_holmes_2000]: https://doi.org/10.21236/ada375025
[research_holubik_1988]: https://doi.org/10.21236/ada194398
[research_hon_karpuk_2022]: https://doi.org/10.2478/tar-2022-0009
[research_hone_friedman_2011]: https://doi.org/10.21236/ada557665
[research_hongwei_zhihua_2006]: https://doi.org/10.1016/s1004-4132(06)60086-8
[research_hoogreef_2026]: https://doi.org/10.21741/9781644904251-108
[research_hopchak_davis_2022]: https://doi.org/10.1109/icuas54217.2022.9836182
[research_hopkins_nix_2010]: https://doi.org/10.21236/ada539681
[research_horn_1973]: https://doi.org/10.21236/ad0759709
[research_horn_thorsen_2017]: https://doi.org/10.4050/f-0073-2017-12066
[research_horn_tritschler_2014]: https://doi.org/10.21236/ada613620
[research_horn_tritschler_2015]: https://doi.org/10.21236/ada617860
[research_hornbuckle_2015]: https://doi.org/10.21236/ad1019476
[research_horowitz_beling_2014]: https://doi.org/10.21236/ada608340
[research_horrigan_1990]: https://doi.org/10.21236/ada301576
[research_horvath_wells_2018]: https://doi.org/10.2514/6.2018-2032
[research_hosseini_jalili_2024]: https://doi.org/10.61186/masm.3.4.537
[research_hosseini_jalili_2025]: https://doi.org/10.1007/s10291-025-01900-1
[research_hossny_elbadawy_2020]: https://doi.org/10.1109/icuas48674.2020.9213902
[research_hou_fang_2020]: https://doi.org/10.33012/2020.17156
[research_hou_lv_2022]: https://doi.org/10.1016/j.ast.2022.107950
[research_hou_shi_2025]: https://doi.org/10.1007/s10291-025-01904-x
[research_hou_wang_2025]: https://doi.org/10.1016/j.measurement.2024.115471
[research_hou_zhang_2024]: https://doi.org/10.1007/s10291-023-01600-8
[research_hough_mohammadi_2024]: https://doi.org/10.2514/6.2024-0311
[research_housel_1952]: https://doi.org/10.21236/ada076059
[research_houtsma_2003]: https://doi.org/10.21236/ada419911
[research_how_frazzoli_2014]: https://doi.org/10.1007/978-90-481-9707-1_49
[research_howard_1995]: https://doi.org/10.21236/ada387625
[research_howard_1996]: https://doi.org/10.21236/ada305682
[research_howard_2002]: https://doi.org/10.21236/ada408129
[research_howard_2023]: https://doi.org/10.2514/6.2023-4099
[research_howe_2000]: https://doi.org/10.1002/9781118903094.ch2
[research_howe_2000_b]: https://doi.org/10.1002/9781118903094
[research_howie_frizzell]: https://doi.org/10.1109/ias.1989.96850
[research_hoy_1963]: https://doi.org/10.21236/ad0409438
[research_hsin_1973]: https://doi.org/10.2514/6.1973-51
[research_hsin_1974]: https://doi.org/10.2514/3.60342
[research_hu_bent_2019]: https://doi.org/10.1109/icuas.2019.8797793
[research_hu_gao_2020]: https://doi.org/10.1016/j.inffus.2020.08.005
[research_hu_liu_2026]: https://doi.org/10.3233/atde260114
[research_hu_ni_2020]: https://doi.org/10.1109/access.2019.2962832
[research_hu_wu_2018]: https://doi.org/10.3390/math6100178
[research_huang_2013]: https://doi.org/10.21236/ada584646
[research_huang_chen_2026]: https://doi.org/10.1016/j.compeleceng.2026.111073
[research_huang_tomlin_2009]: https://doi.org/10.2514/6.2009-6169
[research_huang_wei_2025]: https://doi.org/10.1088/1742-6596/3004/1/012045
[research_huang_yu_2011]: https://doi.org/10.1109/cso.2011.165
[research_huang_zhang_2020]: https://doi.org/10.1109/icuas48674.2020.9213966
[research_huang_zhao_2019]: https://doi.org/10.1017/s0373463319000225
[research_huang_zhu_2019]: https://doi.org/10.2514/6.2019-1422
[research_huang_zhu_2019_b]: https://doi.org/10.2514/6.2019-1422.c1
[research_huang_zhu_2019_c]: https://doi.org/10.1016/j.ast.2018.07.032
[research_huanjunglin]: https://doi.org/10.1109/plans.2004.1308989
[research_hubbell]: https://doi.org/10.33915/etd.4869
[research_huber_2022]: https://doi.org/10.2514/6.2022-3438
[research_huber_reynolds_1976]: https://doi.org/10.2514/6.1976-1717
[research_huber_schutte_2012]: https://doi.org/10.2514/6.2012-3325
[research_hughes_1982]: https://doi.org/10.1080/07266472.1982.11878550
[research_hughes_aircraft_1984]: https://doi.org/10.1016/0045-8732(84)90149-9
[research_hui_2016]: https://doi.org/10.14257/ijmue.2016.11.4.25
[research_hui_liu_2014]: https://doi.org/10.1109/dasc.2014.70
[research_hulek_2015]: https://doi.org/10.14311/mad.2015.16.02
[research_human_catapult_2014]: https://doi.org/10.5040/9798400683886.ch-012
[research_human_factors_1982]: https://doi.org/10.1016/0003-6870(82)90169-7
[research_human_factors_2016]: https://doi.org/10.1201/b11202-16
[research_hummel_oelker_1994]: https://doi.org/10.2514/3.46573
[research_humphreys_paulsonjr_1988]: https://doi.org/10.2514/6.1988-3222
[research_hundley_rowson_1993]: https://doi.org/10.1002/j.2161-4296.1993.tb02302.x
[research_hunn_2005]: https://doi.org/10.1177/154193120504900106
[research_hunter_schaal_2018]: https://doi.org/10.7490/f1000research.1115476.1
[research_huntington_lyrintzis_1996]: https://doi.org/10.2514/6.1996-1360
[research_huntington_lyrintzis_1998]: https://doi.org/10.2514/2.2272
[research_hunziker_1968]: https://doi.org/10.2514/6.1968-849
[research_hutchison_unger_1994]: https://doi.org/10.2514/3.46462
[research_hutmacher_2011]: https://doi.org/10.21236/ada543399
[research_huttunen_scott_2023]: https://doi.org/10.4337/9781803923659.00154
[research_huyer_robinson_1992]: https://doi.org/10.2514/3.46171
[research_hvezda_2021]: https://doi.org/10.3846/aviation.2021.14554
[research_hwang_balakrishnan_2007]: https://doi.org/10.2514/1.27366
[research_hwang_brown_1990]: https://doi.org/10.1002/j.2161-4296.1990.tb01546.x
[research_hwang_pi_1978]: https://doi.org/10.2514/6.1978-1456
[research_hwang_pi_1979]: https://doi.org/10.2514/3.58533
[research_hwang_speyer_2009]: https://doi.org/10.2514/6.2009-5743
[research_hynes_franklin_1989]: https://doi.org/10.2514/3.20440
[research_ibrahim_2008]: https://doi.org/10.1109/plans.2008.4570004
[research_ibrahim_2011]: https://doi.org/10.2514/6.2011-166
[research_idris_sathyamoorthy_2014]: https://doi.org/10.1088/1755-1315/18/1/012035
[research_iec_in_flight_1999]: https://doi.org/10.1108/aeat.1999.12771dab.035
[research_ikonen_sobester_2016]: https://doi.org/10.2514/6.2016-3286
[research_illustrations_and_2016]: https://doi.org/10.1201/b10815-9
[research_imado_kuroda_2011]: https://doi.org/10.2514/1.49079
[research_in_flight_control_2006]: https://doi.org/10.1108/aeat.2006.12778aaf.009
[research_in_flight_refuelling_1961]: https://doi.org/10.1108/eb033495
[research_incremona_ferrara_2023]: https://doi.org/10.23919/acc55779.2023.10156354
[research_ingram_dendinger_2015]: https://doi.org/10.2514/6.2015-1682
[research_initial_evaluation_2012]: https://doi.org/10.1201/b12321-68
[research_initial_sizing_2024]: https://doi.org/10.2514/5.9781624107290.0151.0172
[research_initial_tail_2013]: https://doi.org/10.2514/5.9781600868986.0211.0218
[research_initial_unmanned_2014]: https://doi.org/10.2514/5.9781624102615.0057.0084
[research_initial_unmanned_aircraft_2012]: https://doi.org/10.2514/5.9781600868443.0057.0084
[research_initiative_for_2007]: https://doi.org/10.1108/aeat.2007.12779dab.032
[research_inoyama_sanders_2008]: https://doi.org/10.2514/1.29988
[research_instrument_panel]: https://doi.org/10.4271/arp1166
[research_integrated_wing_2006]: https://doi.org/10.1108/aeat.2006.12778faf.014
[research_integration_of_1991]: https://doi.org/10.1109/vnis.1991.205808
[research_international_conference_2013]: https://doi.org/10.1109/icuas32183.2013
[research_international_conference_2014]: https://doi.org/10.1109/icuas32188.2014
[research_international_conference_2015]: https://doi.org/10.1109/icuas34863.2015
[research_international_conference_2016]: https://doi.org/10.1109/icuas37425.2016
[research_international_conference_2017]: https://doi.org/10.1109/icuas40370.2017
[research_international_conference_2018]: https://doi.org/10.1109/icuas43076.2018
[research_international_conference_2019]: https://doi.org/10.1109/icuas46274.2019
[research_international_conference_2020]: https://doi.org/10.1109/icuas48674.2020
[research_international_conference_2021]: https://doi.org/10.1109/icuas51884.2021.9476682
[research_international_conference_2021_b]: https://doi.org/10.1109/icuas51884.2021
[research_international_conference_2022]: https://doi.org/10.1109/icuas54217.2022
[research_international_conference_2023]: https://doi.org/10.1109/icuas57906.2023
[research_international_conference_2024]: https://doi.org/10.1109/icuas60882.2024
[research_international_conference_2025]: https://doi.org/10.1109/icuas65942.2025
[research_international_conference_2026]: https://doi.org/10.1109/icuas69441.2026
[research_international_symposium_2024]: https://doi.org/10.30546/2224.978-9952-582-04-8
[research_introduction_to_1998]: https://doi.org/10.1108/aeat.1998.12770eae.009
[research_introduction_to_2010]: https://doi.org/10.1002/9780470664797.ch1
[research_introduction_to_2021]: https://doi.org/10.1017/9781139094672.003
[research_ioannidis_walton]: https://doi.org/10.1109/plans.1994.303307
[research_iran_will_2020]: https://doi.org/10.1108/oxan-es254164
[research_irigireddy_moncayo_2020]: https://doi.org/10.2514/6.2020-0989
[research_irvin_swan_1956]: https://doi.org/10.21236/ad0147927
[research_isaacs_ezal_2016]: https://doi.org/10.1109/cdc.2016.7799236
[research_isci_gunel_2021]: https://doi.org/10.1007/s40435-021-00803-6
[research_iscott_thuttunen_2023]: https://doi.org/10.4337/9781803923659.00153
[research_isilak_oktal_2025]: https://doi.org/10.1017/aer.2025.10081
[research_islam_mohona_2024]: https://doi.org/10.2514/6.2024-88782
[research_islam_saha_2017]: https://doi.org/10.1109/ceee.2017.8412926
[research_ito_endo_2016]: https://doi.org/10.1299/jsmermd.2016.1a2-18a4
[research_ittsystemsromeny_1987]: https://doi.org/10.21236/ada396019
[research_iwamoto_takewa_2016]: https://doi.org/10.1109/plans.2016.7479700
[research_j_golubkov_2013]: https://doi.org/10.5772/55792
[research_jabbal_2015]: https://doi.org/10.14323/ijuseng.2015.9
[research_jackson_2001]: https://doi.org/10.21236/ada407162
[research_jackson_jr_1996]: https://doi.org/10.21236/ada387961
[research_jacob_1989]: https://doi.org/10.1007/978-3-642-74585-0_11
[research_jacobson_tsubaki_1986]: https://doi.org/10.2514/6.1986-2667
[research_jagtap_2025]: https://doi.org/10.31224/4316
[research_jahangirova_stocco_2021]: https://doi.org/10.1109/icst49551.2021.00030
[research_james_1972]: https://doi.org/10.2514/3.58999
[research_jamesjoseph_davidjkinney]: https://ntrs.nasa.gov/citations/20240006450
[research_jamesjoseph_davidjkinney_b]: https://ntrs.nasa.gov/citations/20240014871
[research_jameson_2009]: https://doi.org/10.21236/ada500380
[research_jamison_2010]: https://doi.org/10.21236/ada518060
[research_janousek_bjorn_2010]: https://doi.org/10.1121/1.3384554
[research_janousek_marcon_2018]: https://doi.org/10.1109/iiphdw.2018.8388325
[research_japan_s_aircraft_2018]: https://doi.org/10.1108/oxan-es240187
[research_jategaonkar_behr_2006]: https://doi.org/10.2514/1.19602
[research_jauron_1993]: https://doi.org/10.21236/ada262710
[research_jazzar_kale_2023]: https://doi.org/10.1007/978-3-031-29933-9_2
[research_jenkins_snodgrass_2005]: https://doi.org/10.21236/ada496652
[research_jenkinson_page_2000]: https://doi.org/10.1016/s1369-8869(00)00021-5
[research_jensen_2016]: https://doi.org/10.1201/9781315372044-6
[research_jensen_2021]: https://doi.org/10.1201/9780429347498-6
[research_jeong_kee_2023]: https://doi.org/10.33012/2023.18602
[research_jeong_kee_2025]: https://doi.org/10.33012/2025.19977
[research_jeongwonkim_donghwanhwang]: https://doi.org/10.1109/plans.2006.1650616
[research_ji_xu_2013]: https://doi.org/10.1017/s0373463313000477
[research_jia_chen_2016]: https://doi.org/10.1134/s2075108716030068
[research_jia_han_2011]: https://doi.org/10.4028/www.scientific.net/amm.105-107.470
[research_jian_keqin_2004]: https://doi.org/10.2514/1.5467
[research_jiananwang_mingxin_2013]: https://doi.org/10.1109/tcst.2012.2218815
[research_jianchengfang_xiaolingong_2010]: https://doi.org/10.1109/tim.2009.2026614
[research_jiang_liu_2022]: https://doi.org/10.1007/s10291-022-01325-0
[research_jiang_mulunehmekonnen_2013]: https://doi.org/10.4028/www.scientific.net/amr.718-720.1207
[research_jiang_nan_2022]: https://doi.org/10.3390/aerospace9080424
[research_jiang_stol_2016]: https://doi.org/10.1109/icuas.2016.7502613
[research_jiang_su_2017]: https://doi.org/10.1109/ccsse.2017.8087910
[research_jiang_yan_2024]: https://doi.org/10.1007/s10291-024-01623-9
[research_jiang_zhang_2016]: https://doi.org/10.1155/2016/3727241
[research_jiang_zhang_2019]: https://doi.org/10.23919/chicc.2019.8866455
[research_jiang_zhen_2018]: https://doi.org/10.23919/chicc.2018.8483965
[research_jiang_zhu_2013]: https://doi.org/10.4028/www.scientific.net/amm.300-301.1610
[research_jianjun_xiaoli_2003]: https://doi.org/10.1007/bf02899811
[research_jianpingyuan_jianjunluo_1998]: https://doi.org/10.1109/62.735952
[research_jiao_rino_2018]: https://doi.org/10.1002/navi.231
[research_jiayao_dalong_2020]: https://doi.org/10.1109/iccc51575.2020.9345280
[research_jie_wenhai_2017]: https://doi.org/10.1109/yac.2017.7967480
[research_jiguangli_xinchen_2016]: https://doi.org/10.1109/cgncc.2016.7828811
[research_jin_2024]: https://doi.org/10.54097/xv395z51
[research_jin_song_2011]: https://doi.org/10.2514/1.c031493
[research_jing_xu_2015]: https://doi.org/10.1007/s10291-015-0499-4
[research_jing_zhengchun_2015]: https://doi.org/10.2514/6.2015-1136
[research_jmurnes_moomaw_1981]: https://doi.org/10.2514/3.56069
[research_jo_park_2016]: https://doi.org/10.2514/6.2016-0163
[research_joerger_pervan_2012]: https://doi.org/10.2514/6.2012-4450
[research_johansen_perez_2016]: https://doi.org/10.1109/icuas.2016.7502542
[research_john_2014]: https://doi.org/10.21236/ada612259
[research_johnson_1966]: https://doi.org/10.21236/ad0393383
[research_johnson_1972]: https://doi.org/10.21236/ad0754909
[research_johnson_1985]: https://doi.org/10.2514/6.1985-4027
[research_johnson_1993]: https://doi.org/10.21236/ada275701
[research_johnson_1995]: https://doi.org/10.21236/ada380292
[research_johnson_1997]: https://doi.org/10.21236/ada360614
[research_johnson_ansar_2007]: https://doi.org/10.2514/6.2007-2854
[research_johnson_ivanov_2011]: https://doi.org/10.2514/6.2011-6578
[research_johnson_robertson_1980]: https://doi.org/10.21236/ada082513
[research_johnsonjosephl_1949]: https://ntrs.nasa.gov/citations/20090026465
[research_johnsonjr_white_1983]: https://doi.org/10.2514/6.1983-2531
[research_johnston_friend_1965]: https://doi.org/10.4050/sm_vstol_1965-2533
[research_johnston_swenson_2009]: https://doi.org/10.2514/6.2009-5647
[research_johnston_swenson_2010]: https://doi.org/10.2514/1.c000220
[research_johnstone_1968]: https://doi.org/10.2514/6.1968-846
[research_jones_1973]: https://doi.org/10.21236/ada002569
[research_jones_1992]: https://doi.org/10.21236/ada263325
[research_jones_2009]: https://doi.org/10.21236/ada510336
[research_jones_dye_2016]: https://doi.org/10.21236/ad1020042
[research_jones_klyde_2023]: https://doi.org/10.4050/sm_2023_hq-1189
[research_jones_marsh_2003]: https://doi.org/10.21236/ada422017
[research_jonesthomasw_hoppejohnc_2001]: https://ntrs.nasa.gov/citations/20010007228
[research_joslin_2015]: https://doi.org/10.7771/2159-6670.1117
[research_journal_of]: https://doi.org/10.5028/jatm
[research_juang_chio_2005]: https://doi.org/10.1080/0020772042000325961
[research_julke_kawa_2000]: https://doi.org/10.21236/ada387686
[research_jun_2023]: https://doi.org/10.1109/csat61646.2023.00170
[research_jun_tischler_2003]: https://doi.org/10.2514/2.7219
[research_junfeng_wuzhou_2020]: https://doi.org/10.1109/icus50048.2020.9274833
[research_junlichen_xiaoliangwang_2010]: https://doi.org/10.1109/isscaa.2010.5633067
[research_jurges_1977]: https://doi.org/10.1111/j.1559-3584.1977.tb05538.x
[research_jurges_1999]: https://doi.org/10.1111/j.1559-3584.1999.tb01216.x
[research_jwo_2004]: https://doi.org/10.1007/s10291-004-0101-y
[research_jwo_chang_2009]: https://doi.org/10.1108/00022660910967336
[research_jwo_chen_2009]: https://doi.org/10.5772/6812
[research_jwo_chung_2010]: https://doi.org/10.1109/iscid.2010.148
[research_jwo_huang_2007]: https://doi.org/10.1109/iecon.2007.4460302
[research_jwo_lai_2007]: https://doi.org/10.1007/s10291-007-0081-9
[research_jwo_yang_2013]: https://doi.org/10.1007/s11071-013-0793-z
[research_kahya_konar_2026]: https://doi.org/10.30518/jav.1902446
[research_kai_binghong_2026]: https://doi.org/10.1007/978-981-95-6988-5_6
[research_kaidan_2026]: https://doi.org/10.62717/3083-7057-2026-1-108
[research_kaliardos_lyall_2014]: https://doi.org/10.1007/978-90-481-9707-1_36
[research_kaliszuk_kierzkowski_2025]: https://doi.org/10.3390/electronics14132726
[research_kallinen]: https://doi.org/10.5204/thesis.eprints.232516
[research_kallinen_martin_2020]: https://doi.org/10.1109/icuas48674.2020.9213980
[research_kalman_filter_2000]: https://doi.org/10.1002/0471200719.ch7
[research_kalman_filter_2000_b]: https://doi.org/10.1002/0471200719.ch8
[research_kambampati_smith_2017]: https://doi.org/10.2514/1.c034195
[research_kaminski_1997]: https://doi.org/10.21236/ada339157
[research_kaminski_ralston_1996]: https://doi.org/10.21236/ada339253
[research_kamman_hall_1978]: https://doi.org/10.21236/ada060206
[research_kanahara_2022]: https://doi.org/10.2139/ssrn.4158440
[research_kane_2014]: https://doi.org/10.21236/ada614170
[research_kang_park_2018]: https://doi.org/10.1007/s42405-018-0081-8
[research_kang_park_2018_b]: https://doi.org/10.5140/jass.2018.35.4.287
[research_kannan_min_2022]: https://doi.org/10.1109/icuas54217.2022.9836219
[research_kansasunivlawrence_1952]: https://doi.org/10.21236/ad0021570
[research_kansasunivlawrence_1952_b]: https://doi.org/10.21236/ad0009895
[research_kao_white_2018]: https://doi.org/10.2514/6.2018-3877
[research_kapidzic_nilsson_2014]: https://doi.org/10.1016/j.ast.2013.11.002
[research_kaplan_1965]: https://doi.org/10.21236/ad0624155
[research_kaplan_1965_b]: https://doi.org/10.21236/ad0623046
[research_kaplan_1969]: https://doi.org/10.2514/3.48101
[research_kaplan_sargent_1965]: https://doi.org/10.21236/ad0620869
[research_kaplan_sargent_1970]: https://doi.org/10.21236/ad0714242
[research_karagoz_reilley_2019]: https://doi.org/10.2514/6.2019-0498
[research_karasek_kallies_2026]: https://doi.org/10.1109/icuas69441.2026.11598680
[research_karimidoona_schon_2022]: https://doi.org/10.33012/2022.18201
[research_karimikelayeh_djavareshkian_2024]: https://doi.org/10.1061/jaeeez.aseng-5073
[research_karpuk_2026]: https://doi.org/10.1016/j.rineng.2026.111314
[research_kartal_yuksek_2025]: https://doi.org/10.1007/978-3-032-00618-9_9
[research_kasim_2018]: https://doi.org/10.7771/2159-6670.1161
[research_kasimbiber_trentonwhite_2019]: https://doi.org/10.17265/2159-5275/2019.06.004
[research_kasuda_2011]: https://doi.org/10.21236/ad1018752
[research_kasuga_yoshida_2017]: https://doi.org/10.2514/6.2017-0039
[research_katrnak_juracka_2017]: https://doi.org/10.3846/16487788.2016.1266819
[research_katz_1967]: https://doi.org/10.21236/ad0649619
[research_katz_1979]: https://doi.org/10.2514/3.44637
[research_katz_2017]: https://doi.org/10.2514/1.c034373
[research_katz_2025]: https://doi.org/10.2139/ssrn.5652791
[research_katzenstein_bjornstad_1987]: https://doi.org/10.21236/ada199416
[research_kaul_2019]: https://doi.org/10.1007/978-3-030-20707-6_96-1
[research_kaul_2020]: https://doi.org/10.1007/978-3-030-36308-6_96
[research_kaur]: https://doi.org/10.22215/etd/2013-06982
[research_kawamura_kannan_2022]: https://doi.org/10.2514/6.2022-0497
[research_kawano_mokuno_2001]: https://doi.org/10.1002/j.2161-4296.2001.tb00227.x
[research_kaye_freeman_1989]: https://doi.org/10.2514/6.1989-3304
[research_kaymal_2016]: https://doi.org/10.1109/icuas.2016.7502634
[research_ke_tsourdos_2009]: https://doi.org/10.2514/6.2009-6216
[research_ke_zhengzhong_2014]: https://doi.org/10.1109/cgncc.2014.7007248
[research_keane_sobester_2017]: https://doi.org/10.1002/9781119406303
[research_kee_park_2004]: https://doi.org/10.2322/tjsass.46.224
[research_keeping_cool_1996]: https://doi.org/10.1016/s0262-1762(99)81196-1
[research_keidel_fasel_2019]: https://doi.org/10.2514/6.2019-0854
[research_keiyinci_aydin_2021]: https://doi.org/10.26701/ems.770407
[research_keke_nong_2014]: https://doi.org/10.1109/cgncc.2014.7007391
[research_keke_qing_2014]: https://doi.org/10.1109/cgncc.2014.7007393
[research_kelley_katz]: https://doi.org/10.1109/naecon.1990.112801
[research_kelly_2001]: https://doi.org/10.21236/ada401195
[research_kelly_davis_1994]: https://doi.org/10.1002/j.2161-4296.1994.tb02320.x
[research_kelly_skudrna_1981]: https://doi.org/10.2514/6.1981-2247
[research_kemper_2004]: https://doi.org/10.21236/ada428980
[research_kennedy_1999]: https://doi.org/10.21236/ada377912
[research_kennedy_floydd_1985]: https://doi.org/10.21236/ada168062
[research_keong_shin_2019]: https://doi.org/10.1109/reduas47371.2019.8999689
[research_kern_bobbe_2020]: https://doi.org/10.1109/icuas48674.2020.9213960
[research_kessler_spearing_2000]: https://doi.org/10.2514/6.2000-5538
[research_ketterle_vuletic_2008]: https://doi.org/10.21236/ada499671
[research_kewley_lowenberg_2016]: https://doi.org/10.2514/1.c033320
[research_khalid_2023]: https://doi.org/10.4197/eng.33-1.5
[research_khalid_ahmed_2026]: https://doi.org/10.2514/6.2026-4753
[research_khan_2021]: https://doi.org/10.1201/9780429347498-13
[research_khan_khorasani_2010]: https://doi.org/10.2316/p.2010.702-051
[research_khan_nahon_2014]: https://doi.org/10.1109/icuas.2014.6842326
[research_khanafseh_pervan_2007]: https://doi.org/10.2514/1.28195
[research_khanafseh_pervan_2008]: https://doi.org/10.1109/plans.2008.4570101
[research_kharchenko_bogoslavets_2015]: https://doi.org/10.1109/apuavd.2015.7346545
[research_khazetdinov_zakiev_2021]: https://doi.org/10.1109/sibcon50419.2021.9438855
[research_khodabandeh_teunissen_2022]: https://doi.org/10.33012/2022.18437
[research_khreish_sinha_2005]: https://doi.org/10.4050/vfs-f61-000104
[research_kidwell_calhoun_2012]: https://doi.org/10.1177/1071181312561096
[research_kiflu_lopez_2015]: https://doi.org/10.21236/ada626751
[research_kilgore_nehme_2009]: https://doi.org/10.2514/6.2009-1808
[research_kilkis_2024]: https://doi.org/10.1007/978-3-031-62094-2_4
[research_kim_2019]: https://doi.org/10.2514/6.2019-3052
[research_kim_bang_2016]: https://doi.org/10.1109/icuas.2016.7502547
[research_kim_choi_2013]: https://doi.org/10.11003/jkgs.2013.2.1.019
[research_kim_costello_2016]: https://doi.org/10.2514/6.2016-1863
[research_kim_gregory_2022]: https://doi.org/10.1109/icuas54217.2022.9836041
[research_kim_jee]: https://doi.org/10.1109/plans.1998.670208
[research_kim_jung_2015]: https://doi.org/10.1109/icuas.2015.7152335
[research_kim_kang_2024]: https://doi.org/10.2139/ssrn.4783504
[research_kim_kim_2024]: https://doi.org/10.33012/2024.19484
[research_kim_kim_2025]: https://doi.org/10.3390/aerospace12100928
[research_kim_oh_2017]: https://doi.org/10.1109/icuas.2017.7991455
[research_kim_park_2007]: https://doi.org/10.3182/20070625-5-fr-2916.00093
[research_kim_sung_2025]: https://doi.org/10.1109/plans61210.2025.11028325
[research_kim_sung_2025_b]: https://doi.org/10.23919/iccas66577.2025.11301129
[research_kim_won_2012]: https://doi.org/10.5394/kinpr.2012.36.10.825
[research_kindley_2015]: https://doi.org/10.21236/ad1019143
[research_king]: https://doi.org/10.31390/gradschool_theses.4773
[research_kirk_wang_2022]: https://doi.org/10.21236/ad1170051
[research_kirnon_majar_2019]: https://doi.org/10.7490/f1000research.1116429.1
[research_kis_lantos_2011]: https://doi.org/10.1109/aim.2011.6027009
[research_kishi_pfeffer_1971]: https://doi.org/10.2514/3.44234
[research_kistyarev_wang_2025]: https://doi.org/10.1007/s42496-025-00249-5
[research_kitts_lucas_1963]: https://doi.org/10.21236/ad0624930
[research_kladis_economou_2008]: https://doi.org/10.1109/med.2008.4602182
[research_klein_2002]: https://doi.org/10.21236/ada406509
[research_klein_krainski_2017]: https://doi.org/10.4050/sm_2017_hq-1572
[research_klemin_1940]: https://doi.org/10.1108/eb030620
[research_kleusberg_1989]: https://doi.org/10.1007/978-3-642-74585-0_8
[research_kline_2012]: https://doi.org/10.21236/ada573898
[research_klingelhoefer_2005]: https://doi.org/10.21236/ada431848
[research_klipp_kirk_2021]: https://doi.org/10.21236/ad1152543
[research_klishin_kolesnikova_2022]: https://doi.org/10.18698/0236-3941-2022-4-60-76
[research_klyde_lampton_2021]: https://doi.org/10.2514/6.2021-0178
[research_klyde_mitchell_1999]: https://doi.org/10.2514/2.4429
[research_klyde_schulze_2020]: https://doi.org/10.2514/6.2020-3285
[research_knowles_krauskopf_2012]: https://doi.org/10.1007/s11071-012-0664-z
[research_knuth_cassano_2012]: https://doi.org/10.5194/essdd-5-1035-2012
[research_knutzon]: https://doi.org/10.31274/rtd-180815-695
[research_ko_kumar_2019]: https://doi.org/10.1109/icuas.2019.8798090
[research_kochenderfer_kuchar_2008]: https://doi.org/10.2514/6.2008-6629
[research_koenke_hill]: https://doi.org/10.1109/ntc.1994.316663
[research_kogiso_tsushima_2000]: https://doi.org/10.2514/6.2000-4739
[research_koh_paranjape_2020]: https://doi.org/10.2514/6.2020-1086
[research_kolpitcke_smith_2025]: https://doi.org/10.2514/1.c037859
[research_kometani_2005]: https://doi.org/10.2493/jjspe.71.1339
[research_konar_ozdemir_2024]: https://doi.org/10.30518/jav.1523967
[research_kondo_yasuda_2006]: https://doi.org/10.9749/jin.115.163
[research_konert_balcerzak_2021]: https://doi.org/10.1109/icuas51884.2021.9476822
[research_koo_kim_2015]: https://doi.org/10.1016/j.ifacol.2015.06.464
[research_koo_sastry_2003]: https://doi.org/10.2514/6.2003-6541
[research_kopeikin_ponda_2013]: https://doi.org/10.1142/s2301385013500039
[research_koremura]: https://doi.org/10.1109/plans.1992.185846
[research_korpela_danko_2011]: https://doi.org/10.1007/978-94-007-3033-5_7
[research_korzatkowski_kolsch_2015]: https://doi.org/10.1177/1541931215591398
[research_kotsinis_karras_2026]: https://doi.org/10.1109/icuas69441.2026.11598720
[research_kottapallianjaneyp_harrisfranklind_2012]: https://ntrs.nasa.gov/citations/20130011015
[research_kovach_conley_1991]: https://doi.org/10.1002/j.2161-4296.1991.tb01722.x
[research_kovtun_tkachenko_2018]: https://doi.org/10.1615/tsagiscij.2018029399
[research_kovtun_tkachenko_2019]: https://doi.org/10.24937/2542-2324-2019-4-390-125-136
[research_kowal]: https://doi.org/10.1109/naecon.2000.894909
[research_kozel_cardoza]: https://doi.org/10.1109/plans.1996.509061
[research_kozhanov_suvorova_2022]: https://doi.org/10.52348/2712-8873_mmtt_2022_5_45
[research_kozlowski_boloz_2024]: https://doi.org/10.3390/en17123033
[research_kozol_tankins_1993]: https://doi.org/10.21236/ada268260
[research_krabacher_1993]: https://doi.org/10.4271/931400
[research_kramer_bailey_2023]: https://doi.org/10.1109/aero55745.2023.10115921
[research_krammer_scherer_2021]: https://doi.org/10.2514/6.2021-3217
[research_krasuski_wierzbicki_2018]: https://doi.org/10.5604/01.3001.0012.2504
[research_krawczyk_szczepanski_2019]: https://doi.org/10.7225/toms.v08.n02.002
[research_kreerenko_2025]: https://doi.org/10.1109/smartindustrycon65166.2025.10986169
[research_krempasky_1996]: https://doi.org/10.2514/6.1996-3816
[research_krempasky_1999]: https://doi.org/10.1002/j.2161-4296.1999.tb02402.x
[research_krempasky_krempasky_1997]: https://doi.org/10.2514/6.1997-3562
[research_krengel_hepperle_2019]: https://doi.org/10.2514/6.2019-3368
[research_krings_annighofer_2013]: https://doi.org/10.1109/acc.2013.6580044
[research_krishnakamath_kumartripathi_2020]: https://doi.org/10.5772/intechopen.86057
[research_krispin_portnoy_1988]: https://doi.org/10.2514/3.45537
[research_krizek_horyna_2022]: https://doi.org/10.1109/icuas54217.2022.9836073
[research_kroo_1983]: https://doi.org/10.2514/6.1983-2476
[research_kroo_1986]: https://doi.org/10.2514/6.1986-2624
[research_krozel_2002]: https://doi.org/10.2514/6.2002-4995
[research_krozel_andrisani_1990]: https://doi.org/10.2514/3.20592
[research_kruger_besselink_1997]: https://doi.org/10.1080/00423119708969352
[research_kruger_meddaikar_2022]: https://doi.org/10.3390/aerospace9100535
[research_kryvokhatko_2023]: https://doi.org/10.1007/978-3-031-23777-5_2
[research_kryvokhatko_2023_b]: https://doi.org/10.1007/978-3-031-23777-5_4
[research_kryvokhatko_2024]: https://doi.org/10.1007/978-3-031-74809-7_2
[research_kryvokhatko_2024_b]: https://doi.org/10.1007/978-3-031-74809-7_4
[research_krzykowskapiotrowska_2020]: https://doi.org/10.3390/ecas2020-08135
[research_ksenthilkumar_jshanmugam_2023]: https://doi.org/10.61653/joast.v60i4.2008.798
[research_kube_bischof_2018]: https://doi.org/10.1007/s10291-018-0709-y
[research_kubo_fujita_2007]: https://doi.org/10.5687/sss.2007.180
[research_kubo_ito]: https://doi.org/10.1109/roman.2000.892467
[research_kubo_muto_2004]: https://doi.org/10.1109/tencon.2004.1414507
[research_kucherov_sushchenko_2019]: https://doi.org/10.1109/apuavd47061.2019.8943918
[research_kuczera_hauck_1992]: https://doi.org/10.2514/6.1992-5002
[research_kuczera_hauck_1993]: https://doi.org/10.2514/6.1993-5159
[research_kukla_2026]: https://doi.org/10.37701/ts.11.2026.11
[research_kumar]: https://doi.org/10.1109/pq.1998.710389
[research_kumar_1997]: https://doi.org/10.21236/ada398405
[research_kumar_2020]: https://doi.org/10.2139/ssrn.3593220
[research_kumar_kumar_2022]: https://doi.org/10.1109/icuas54217.2022.9836191
[research_kumar_mandal_2020]: https://doi.org/10.2514/6.2020-3064
[research_kumar_mandal_2020_b]: https://doi.org/10.1615/jflowvisimageproc.2020031042
[research_kumar_mittal_2026]: https://doi.org/10.2514/6.2026-4389
[research_kumar_shanmugam_2007]: https://doi.org/10.2514/6.2007-2736
[research_kumar_yokeshraj_2019]: https://doi.org/10.1109/iccmc.2019.8819646
[research_kumarrath_ramirezserrano_2020]: https://doi.org/10.1002/eng2.12275
[research_kumuk_ilbas_2023]: https://doi.org/10.1007/978-3-031-29933-9_15
[research_kundu_raghunathan_2000]: https://doi.org/10.1016/s1369-8869(00)00015-x
[research_kuo_hsu_1997]: https://doi.org/10.2514/2.2222
[research_kuppusamy_yoon_2016]: https://doi.org/10.1109/icmae.2016.7549577
[research_kurdel_gecejova_2024]: https://doi.org/10.3390/aerospace11010082
[research_kurdyla_1963]: https://doi.org/10.21236/ad0434421
[research_kurkcu_erhan_2011]: https://doi.org/10.1007/978-94-007-3033-5_5
[research_kurnaz_cetin]: https://doi.org/10.1007/978-1-4020-9137-7_13
[research_kushneruk_2026]: https://doi.org/10.2139/ssrn.6450239
[research_kwiek_figat_2016]: https://doi.org/10.1017/aer.2015.16
[research_kwon_jang_2012]: https://doi.org/10.12673/jkoni.2012.16.4.627
[research_kwon_yoder_2013]: https://doi.org/10.1109/icuas.2013.6564669
[research_laananen_1980]: https://doi.org/10.21236/ada082512
[research_lachaonajr_2023]: https://doi.org/10.2139/ssrn.4445309
[research_lachapelle_cannon_1992]: https://doi.org/10.1080/01490419209388062
[research_ladd_xinhuaqin]: https://doi.org/10.1109/ntc.1993.292993
[research_lahoti_gogulapati_2022]: https://doi.org/10.1016/j.ifacol.2023.03.067
[research_lai_2007]: https://doi.org/10.21236/ada476563
[research_lai_tong_2022]: https://doi.org/10.1016/j.measurement.2022.111641
[research_lam_maull_1993]: https://doi.org/10.2514/3.46387
[research_lambregts_creedon_1980]: https://doi.org/10.2514/6.1980-1757
[research_lampton_gray_2018]: https://doi.org/10.2514/6.2018-0075
[research_lampton_klyde_2024]: https://doi.org/10.2514/6.2024-2479
[research_landing_gear]: https://doi.org/10.4271/arp1311
[research_landing_gear_b]: https://doi.org/10.4271/arp5644a
[research_landing_gear_c]: https://doi.org/10.4271/air5914
[research_landrum_tournes_2001]: https://doi.org/10.2514/6.2001-4204
[research_lange_1983]: https://doi.org/10.2514/6.1983-2440
[research_lange_1984]: https://doi.org/10.2514/6.1984-2416
[research_lannes_2001]: https://doi.org/10.1364/josaa.18.001046
[research_lanteigne_mcleod_2020]: https://doi.org/10.1139/juvs-2019-0012
[research_laporte_roberts_1988]: https://doi.org/10.21236/ada198692
[research_larm_2004]: https://doi.org/10.21236/ada424221
[research_larrabee]: https://doi.org/10.33915/etd.678
[research_larson_1958]: https://doi.org/10.21236/ad0142268
[research_larsson_2025]: https://doi.org/10.3384/ecp215.1202
[research_lateral_directional_dynamics_1998]: https://doi.org/10.2514/5.9781600862052.0207.0256
[research_lattimore_1991]: https://doi.org/10.21236/ada233199
[research_lau_2016]: https://doi.org/10.1007/s10291-016-0533-1
[research_laufer_krauss_1997]: https://doi.org/10.2514/6.1997-1421
[research_laurichesse_mercier_2009]: https://doi.org/10.1002/j.2161-4296.2009.tb01750.x
[research_lawrence_2000]: https://doi.org/10.21236/ada377470
[research_lawrence_2003]: https://doi.org/10.2514/6.2003-5543
[research_lawrence_mosnier_2009]: https://doi.org/10.3940/rina.ws.2009.01
[research_lawson_2001]: https://doi.org/10.21236/ada389603
[research_lawson_barakos_2010]: https://doi.org/10.2514/1.c000218
[research_le_he_2014]: https://doi.org/10.4028/www.scientific.net/amm.568-570.970
[research_le_vesely_2019]: https://doi.org/10.23919/irs.2019.8768091
[research_leasure_2002]: https://doi.org/10.58940/2329-258x.1305
[research_lebacqz_chen_1977]: https://doi.org/10.2514/6.1977-1143
[research_lee]: https://doi.org/10.1109/plans.1992.185887
[research_lee_1988]: https://doi.org/10.1002/j.2161-4296.1988.tb00954.x
[research_lee_2010]: https://doi.org/10.2514/1.46684
[research_lee_2012]: https://doi.org/10.21236/ada561596
[research_lee_2014]: https://doi.org/10.12652/ksce.2014.34.1.0341
[research_lee_batina_1991]: https://doi.org/10.2514/3.45996
[research_lee_chiou_1994]: https://doi.org/10.2514/3.46508
[research_lee_kim_2015]: https://doi.org/10.1007/s10291-015-0446-4
[research_lee_kim_2024]: https://doi.org/10.2514/1.c037495
[research_lee_lowe_2026]: https://doi.org/10.1109/icuas69441.2026.11598585
[research_lee_olaughlin_2000]: https://doi.org/10.1002/j.2161-4296.2000.tb00212.x
[research_lee_olaughlin_2001]: https://doi.org/10.1002/j.2161-4296.2001.tb00236.x
[research_lee_park_2012]: https://doi.org/10.5394/kinpr.2012.36.6.429
[research_lee_shim_1998]: https://doi.org/10.1016/s1474-6670(17)41111-6
[research_lee_shim_2018]: https://doi.org/10.1109/icuas.2018.8453315
[research_lee_soon_2008]: https://doi.org/10.1017/s037346330700464x
[research_lee_tahk_2019]: https://doi.org/10.1109/ssci44817.2019.9002789
[research_lee_wang_2005]: https://doi.org/10.1007/s00190-005-0466-x
[research_lehman_1964]: https://doi.org/10.21236/ad0606886
[research_lehman_1965]: https://doi.org/10.2514/6.1965-332
[research_lehman_1966]: https://doi.org/10.2514/3.43726
[research_lehman_kaplan_1965]: https://doi.org/10.21236/ad0614672
[research_lehovec_1979]: https://doi.org/10.21236/ada071841
[research_lehovec_1980]: https://doi.org/10.21236/ada087432
[research_lei_2020]: https://doi.org/10.1109/icmra51221.2020.9398346
[research_leira_johansen_2017]: https://doi.org/10.1109/icuas.2017.7991435
[research_leishman_mclain_2013]: https://doi.org/10.1109/icuas.2013.6564707
[research_lejeune_wautelet_2011]: https://doi.org/10.1007/s10291-011-0212-1
[research_lemmon_2013]: https://doi.org/10.21236/ada613398
[research_lemmon_2015]: https://doi.org/10.21236/ad1019142
[research_leonard_savvaris_2013]: https://doi.org/10.1109/icuas.2013.6564681
[research_leonidov_2021]: https://doi.org/10.26732/j.st.2021.1.05
[research_leuchter_2013]: https://doi.org/10.2514/6.2013-4213
[research_leva]: https://doi.org/10.1109/plans.1994.303373
[research_level_flight_2003]: https://doi.org/10.2514/5.9781600861840.0097.0104
[research_levison_rickard_1981]: https://doi.org/10.2514/6.1981-1773
[research_lewantowicz]: https://doi.org/10.1109/plans.1992.185856
[research_lewis_2002]: https://doi.org/10.21236/ada420631
[research_lewis_pickering_2014]: https://doi.org/10.21236/ada612283
[research_li_2008]: https://doi.org/10.2514/6.2008-6464
[research_li_2017]: https://doi.org/10.26226/morressier.59c106e9d462b80292389d4a
[research_li_2019]: https://doi.org/10.1139/juvs-2018-0022
[research_li_2020]: https://doi.org/10.23940/ijpe.20.11.p5.17321740
[research_li_2021]: https://doi.org/10.36227/techrxiv.14751966
[research_li_cao_2013]: https://doi.org/10.1007/978-3-642-37398-5_18
[research_li_chen_2003]: https://doi.org/10.1117/12.522111
[research_li_chen_2013]: https://doi.org/10.1007/978-3-642-37404-3_4
[research_li_duan_2015]: https://doi.org/10.1016/j.ast.2015.01.017
[research_li_fan_2018]: https://doi.org/10.2991/ncce-18.2018.32
[research_li_fan_2022]: https://doi.org/10.3390/aerospace9040221
[research_li_feng_2009]: https://doi.org/10.1007/s10291-009-0131-6
[research_li_feng_2023]: https://doi.org/10.1017/flo.2023.30
[research_li_gao_2016]: https://doi.org/10.1007/s10291-015-0511-z
[research_li_gao_2021]: https://doi.org/10.1155/2021/5597878
[research_li_glennon_2012]: https://doi.org/10.1007/978-3-642-29193-7_44
[research_li_guo_2013]: https://doi.org/10.2514/6.2013-1934
[research_li_han_2026]: https://doi.org/10.1016/j.neunet.2026.108776
[research_li_huang_2014]: https://doi.org/10.4028/www.scientific.net/amm.540.138
[research_li_jiang_2020]: https://doi.org/10.1007/s10291-020-00992-1
[research_li_leung_2007]: https://doi.org/10.1109/icmech.2007.4280015
[research_li_li_2013]: https://doi.org/10.4028/www.scientific.net/amm.373-375.1196
[research_li_li_2014]: https://doi.org/10.1007/s10291-013-0362-4
[research_li_li_2014_b]: https://doi.org/10.1109/eml.2014.6920169
[research_li_li_2015]: https://doi.org/10.1007/s10291-015-0468-y
[research_li_li_2022]: https://doi.org/10.1007/s10291-022-01327-y
[research_li_li_2022_b]: https://doi.org/10.1007/s10291-022-01269-5
[research_li_liu_2020]: https://doi.org/10.1088/1742-6596/1626/1/012146
[research_li_liu_2026]: https://doi.org/10.1007/s10291-026-02128-3
[research_li_maiorova_2022]: https://doi.org/10.36074/grail-of-science.17.06.2022.039
[research_li_qin_2017]: https://doi.org/10.1109/ccdc.2017.7978762
[research_li_qin_2020]: https://doi.org/10.2514/1.c035696
[research_li_rizos_2008]: https://doi.org/10.1002/j.2161-4296.2008.tb00427.x
[research_li_su_2013]: https://doi.org/10.1109/mec.2013.6885503
[research_li_sun_2013]: https://doi.org/10.1109/icma.2013.6618070
[research_li_tang_2024]: https://doi.org/10.1080/10095020.2024.2336595
[research_li_verhagen_2013]: https://doi.org/10.1007/s10291-013-0329-5
[research_li_wang_2013]: https://doi.org/10.1007/s10291-013-0342-8
[research_li_wang_2013_b]: https://doi.org/10.1007/s10291-013-0312-1
[research_li_wang_2016]: https://doi.org/10.1017/s0373463315001083
[research_li_wang_2025]: https://doi.org/10.1007/s10291-025-01823-x
[research_li_weng_2020]: https://doi.org/10.1109/icecce49384.2020.9179243
[research_li_xu_2022]: https://doi.org/10.1007/s10291-022-01279-3
[research_li_yan_2025]: https://doi.org/10.1016/j.ifacol.2025.11.250
[research_li_yang_2013]: https://doi.org/10.1007/s10291-013-0360-6
[research_li_yang_2024]: https://doi.org/10.1109/tasc.2024.3370122
[research_li_yong_2017]: https://doi.org/10.23919/chicc.2017.8027800
[research_li_yuan_2013]: https://doi.org/10.1007/978-3-642-37404-3_16
[research_li_yuan_2018]: https://doi.org/10.1007/s10291-018-0721-2
[research_li_zhai_2024]: https://doi.org/10.1007/978-981-97-5300-0_12
[research_li_zhai_2024_b]: https://doi.org/10.1007/978-981-97-5300-0_10
[research_li_zhang_2012]: https://doi.org/10.4028/www.scientific.net/amr.466-467.1070
[research_li_zhang_2018]: https://doi.org/10.1109/gncc42960.2018.9019083
[research_li_zhang_2018_b]: https://doi.org/10.1109/icuas.2018.8453297
[research_li_zhang_2024]: https://doi.org/10.20944/preprints202409.2177.v1
[research_li_zhang_2025]: https://doi.org/10.2514/1.g008074
[research_li_zhang_2025_b]: https://doi.org/10.1007/978-981-96-7352-0_15
[research_li_zhang_2026]: https://doi.org/10.1016/j.measurement.2026.121391
[research_li_zhang_2026_b]: https://doi.org/10.2139/ssrn.6438823
[research_li_zheng_2025]: https://doi.org/10.1088/1748-3190/adb2cb
[research_li_zhou_2024]: https://doi.org/10.1117/12.3025721
[research_li_zhu_2012]: https://doi.org/10.1109/eml.2012.6325100
[research_li_zhu_2013]: https://doi.org/10.4028/www.scientific.net/amr.664.1122
[research_li_zhu_2024]: https://doi.org/10.1007/978-981-97-7004-5_3
[research_liang_chen_2020]: https://doi.org/10.1109/ccdc49329.2020.9164274
[research_liang_dong_2024]: https://doi.org/10.1109/ccdc62350.2024.10587983
[research_liang_jia_2014]: https://doi.org/10.1109/cdc.2014.7039509
[research_liang_li_2022]: https://doi.org/10.1016/j.measurement.2022.110962
[research_licheva_liscouethanke_2023]: https://doi.org/10.2514/6.2023-0213
[research_liersch_bishop_2018]: https://doi.org/10.2514/6.2018-2839
[research_liggin_crawford_2001]: https://doi.org/10.2514/6.2001-5108
[research_lighthill_1963]: https://doi.org/10.1088/0031-9112/14/3/001
[research_lightsey_crassidis_1999]: https://doi.org/10.2514/6.1999-3967
[research_lightsey_crassidis_2004]: https://doi.org/10.1007/bf03546432
[research_lijesen_nijkamp_2005]: https://doi.org/10.2139/ssrn.652983
[research_limafilho_medeiros_2021]: https://doi.org/10.1590/jatm.v13.1228
[research_lin_2002]: https://doi.org/10.21236/ada403633
[research_lin_2015]: https://doi.org/10.2991/iccet-15.2015.353
[research_lin_2023]: https://doi.org/10.26855/acc.2023.08.008
[research_lin_da_1994]: https://doi.org/10.2514/6.1994-3678
[research_lin_garratt_2015]: https://doi.org/10.1109/icma.2015.7237532
[research_lin_meghdadhasheminasab_2020]: https://doi.org/10.1109/icuas48674.2020.9214049
[research_lin_saripalli_2014]: https://doi.org/10.1109/icuas.2014.6842268
[research_lin_wang_2017]: https://doi.org/10.23919/chicc.2017.8028365
[research_lin_wohleber_2015]: https://doi.org/10.1177/1541931215591175
[research_lin_yang_2019]: https://doi.org/10.3390/s19153410
[research_lin_zong_2026]: https://doi.org/10.1063/5.0334699
[research_lindsay_sun_2020]: https://doi.org/10.1109/icuas48674.2020.9213838
[research_lindsey_1977]: https://doi.org/10.21236/ada522361
[research_ling_1970]: https://doi.org/10.2514/3.44119
[research_lingyu_youwu_2006]: https://doi.org/10.1109/chicc.2006.4347425
[research_linn_langlois_2006]: https://doi.org/10.2514/1.13865
[research_linne_2022]: https://doi.org/10.21236/ad1181447
[research_linnell_1963]: https://doi.org/10.21236/ad0408661
[research_lintern_1984]: https://doi.org/10.2466/pms.58.1.167-172
[research_lion_1966]: https://doi.org/10.21236/ad0635753
[research_lisauskas_poska_2015]: https://doi.org/10.4028/www.scientific.net/ssp.220-221.67
[research_liscouethanke_huynh_2013]: https://doi.org/10.4271/2013-01-2235
[research_liseitsev_2025]: https://doi.org/10.1007/978-981-96-4599-2_6
[research_liu_2006]: https://doi.org/10.2514/1.13234
[research_liu_2018]: https://doi.org/10.3997/2214-4609.201801897
[research_liu_2024]: https://doi.org/10.1109/cac63892.2024.10864935
[research_liu_ai_2026]: https://doi.org/10.1016/j.ast.2025.111042
[research_liu_bogu_2025]: https://doi.org/10.1088/1742-6596/2977/1/012111
[research_liu_bucknall_2018]: https://doi.org/10.1017/s0263574718000218
[research_liu_bush_2004]: https://doi.org/10.21236/ada457106
[research_liu_cai_2019]: https://doi.org/10.1201/9780429507229-21
[research_liu_chen_2011]: https://doi.org/10.1109/imccc.2011.240
[research_liu_chen_2014]: https://doi.org/10.1016/j.asr.2014.01.030
[research_liu_ding_2025]: https://doi.org/10.3390/aerospace12030193
[research_liu_fan_2018]: https://doi.org/10.1016/j.ymssp.2017.07.051
[research_liu_fan_2025]: https://doi.org/10.1049/icp.2024.2978
[research_liu_fu_2017]: https://doi.org/10.33012/2017.14953
[research_liu_han_2020]: https://doi.org/10.1109/jsyst.2019.2932783
[research_liu_han_2022]: https://doi.org/10.3390/drones6120375
[research_liu_he_2019]: https://doi.org/10.1109/icuas.2019.8798329
[research_liu_huang_2025]: https://doi.org/10.2139/ssrn.5316865
[research_liu_huang_2026]: https://doi.org/10.1016/j.ast.2026.112007
[research_liu_li_2023]: https://doi.org/10.1109/icuas57906.2023.10156472
[research_liu_liu_2022]: https://doi.org/10.1201/9781003242147
[research_liu_liu_2023]: https://doi.org/10.1088/1742-6596/2658/1/012055
[research_liu_lou_2017]: https://doi.org/10.1007/s10291-017-0641-6
[research_liu_sengupta_2017]: https://doi.org/10.1109/icuas.2017.7991310
[research_liu_sun_2023]: https://doi.org/10.1007/978-981-99-0479-2_211
[research_liu_tan_2022]: https://doi.org/10.1109/icus55513.2022.9986820
[research_liu_valavanis_2026]: https://doi.org/10.1109/icuas69441.2026.11598642
[research_liu_wang_2007]: https://doi.org/10.11728/cjss2007.02.162
[research_liu_wang_2023]: https://doi.org/10.3390/aerospace10110953
[research_liu_wang_2025]: https://doi.org/10.3390/e27070662
[research_liu_wang_2025_b]: https://doi.org/10.1108/aeat-07-2024-0197
[research_liu_wu_2003]: https://doi.org/10.1016/s1000-9361(11)60165-9
[research_liu_yan_2025]: https://doi.org/10.3934/mfc.2024022
[research_liu_yang_2018]: https://doi.org/10.1007/s10291-018-0771-5
[research_liu_yuan_2025]: https://doi.org/10.1108/aeat-01-2025-0030
[research_liu_zhang_2022]: https://doi.org/10.3390/aerospace9020079
[research_liu_zhang_2024]: https://doi.org/10.1016/j.jfranklin.2024.107218
[research_liu_zhang_2024_b]: https://doi.org/10.23919/ccc63176.2024.10662356
[research_liu_zhang_2025]: https://doi.org/10.3390/s25020321
[research_liu_zheng_2020]: https://doi.org/10.1109/icus50048.2020.9274945
[research_liu_zheng_2021]: https://doi.org/10.23919/ccc52363.2021.9550644
[research_liu_zheng_2024]: https://doi.org/10.1016/j.ast.2024.109545
[research_liu_zhu_2026]: https://doi.org/10.1016/j.isatra.2026.07.013
[research_liugc_morriscekjr_1983]: https://ntrs.nasa.gov/citations/19830009259
[research_livne_mineau_1997]: https://doi.org/10.2514/2.2209
[research_locatelli_mulani_2011]: https://doi.org/10.2514/1.c031336
[research_location_and]: https://doi.org/10.4271/arp268g
[research_location_and_b]: https://doi.org/10.4271/arp268e
[research_lochert_huber_2019]: https://doi.org/10.1016/j.ast.2019.105319
[research_loechert_huber_2018]: https://doi.org/10.2514/6.2018-3329
[research_loegering_harris_2002]: https://doi.org/10.2514/6.2002-3457
[research_logan_1989]: https://doi.org/10.4050/sm_rotary_1989-3454
[research_loh_fernow]: https://doi.org/10.1109/plans.1994.303369
[research_londner_2016]: https://doi.org/10.2514/6.2016-1987
[research_longino_1994]: https://doi.org/10.21236/ada289777
[research_lopez_2010]: https://doi.org/10.1109/map.2010.5466404
[research_lopez_garcia_2021]: https://doi.org/10.1109/rpic53795.2021.9648419
[research_lorenz_2015]: https://doi.org/10.1016/j.pss.2015.01.003
[research_lorenzetti_mcclellan_2020]: https://doi.org/10.2514/6.2020-1721
[research_loupy_barakos_2018]: https://doi.org/10.2514/1.c034344
[research_love_argrow_2021]: https://doi.org/10.1201/9780429347498-9
[research_love_kapania_2020]: https://doi.org/10.2514/6.2020-0166
[research_lovett_1984]: https://doi.org/10.21236/ada270017
[research_low_damico_2024]: https://doi.org/10.1109/aero58975.2024.10521084
[research_lowe_torshizi_2026]: https://doi.org/10.1109/icuas69441.2026.11598715
[research_lp_ghosh_2020]: https://doi.org/10.1109/icuas48674.2020.9213866
[research_lu_2021]: https://doi.org/10.1007/978-981-16-1075-2_2
[research_lu_2026]: https://doi.org/10.1109/eei70303.2026.11640594
[research_lu_jiang_2011]: https://doi.org/10.1109/ccdc.2011.5968270
[research_lu_liu_2024]: https://doi.org/10.3390/a17110488
[research_lu_pierson_1995]: https://doi.org/10.2514/6.1995-3342
[research_lu_tan_2014]: https://doi.org/10.1109/eml.2014.6920679
[research_lu_wang_2020]: https://doi.org/10.1109/icmae50897.2020.9178904
[research_lu_xu_2024]: https://doi.org/10.1007/978-981-97-7139-4_42
[research_lu_yan_2025]: https://doi.org/10.23919/ccc64809.2025.11178352
[research_lu_zhang_2014]: https://doi.org/10.1109/eml.2014.6920681
[research_lu_zhu_2022]: https://doi.org/10.1109/cac57257.2022.10055231
[research_luan_sun_2020]: https://doi.org/10.2316/j.2020.206-0222
[research_lugo_zell_2013]: https://doi.org/10.1109/icuas.2013.6564735
[research_lukeke_yujinyong_2016]: https://doi.org/10.1109/cgncc.2016.7829047
[research_lungu_2017]: https://doi.org/10.2316/p.2017.848-004
[research_lungu_chen_2022]: https://doi.org/10.3390/aerospace9110644
[research_lungu_flores_2022]: https://doi.org/10.1109/codit55151.2022.9803999
[research_luo_babu_2012]: https://doi.org/10.1007/s10291-011-0246-4
[research_luo_duan_2014]: https://doi.org/10.3182/20140824-6-za-1003.00330
[research_luong_le_2025]: https://doi.org/10.3390/mi16030355
[research_lusardi_2023]: https://doi.org/10.4050/sm_2023_hq-1186
[research_luu_2025]: https://doi.org/10.32920/29170238
[research_luzica_bloudicek_2016]: https://doi.org/10.1109/icate.2016.7754685
[research_lv_wang_2026]: https://doi.org/10.1016/b978-0-443-14081-5.00051-9
[research_lv_zhu_2011]: https://doi.org/10.1109/icma.2011.5986275
[research_lykken_shah_1972]: https://doi.org/10.2514/3.58988
[research_lynn_1978]: https://doi.org/10.21236/ada068619
[research_lyu_su_2021]: https://doi.org/10.1109/icus52573.2021.9641437
[research_ma]: https://doi.org/10.5353/th_991044058293703414
[research_ma_1989]: https://doi.org/10.2514/3.45778
[research_ma_guan_2018]: https://doi.org/10.23919/chicc.2018.8482717
[research_ma_lou_2022]: https://doi.org/10.1007/s10291-022-01285-5
[research_ma_wang_2009]: https://doi.org/10.2514/6.2009-55
[research_ma_yan_2022]: https://doi.org/10.1177/09544100221095370
[research_macdoran_miller_1984]: https://doi.org/10.1002/j.2161-4296.1984.tb00862.x
[research_macgarvey_2014]: https://doi.org/10.21236/ada605342
[research_maciasvaladez_santerre_2011]: https://doi.org/10.1007/s10291-011-0244-6
[research_mackunis_kaiser_2008]: https://doi.org/10.2514/6.2008-6792
[research_macnae_1995]: https://doi.org/10.1190/1.1887449
[research_macone_1996]: https://doi.org/10.21236/ada309765
[research_mader_2001]: https://doi.org/10.1007/pl00012864
[research_mader_martins_2010]: https://doi.org/10.2514/6.2010-9199
[research_madonna_viola_2010]: https://doi.org/10.1109/plans.2010.5507342
[research_madyastha_ravindra_2011]: https://doi.org/10.2514/6.2011-6615
[research_maeda_itsukaichi_1998]: https://doi.org/10.2514/6.1998-1333
[research_mah_okeefe_2025]: https://doi.org/10.1109/plans61210.2025.11028327
[research_mahanteshkatagi_manishkumarsingh_2015]: https://doi.org/10.17577/ijertv4is051050
[research_mahmud_qaisar_2016]: https://doi.org/10.1109/plans.2016.7479803
[research_maier_kiesel_2011]: https://doi.org/10.1134/s2075108711040110
[research_maimako_mintah_2026]: https://doi.org/10.2139/ssrn.7115964
[research_majoros_1989]: https://doi.org/10.2514/6.1989-2101
[research_makarenko_makarov_2017]: https://doi.org/10.21778/2413-9599-2017-1-96-103
[research_makarenko_tokarev_2023]: https://doi.org/10.1007/978-3-031-32639-4_10
[research_maksimova_2025]: https://doi.org/10.26467/2079-0619-2025-28-1-39-52
[research_malaek_soltanmohammed_2001]: https://doi.org/10.1016/s1369-8869(00)00024-0
[research_malleswaran_vaidehi_2011]: https://doi.org/10.1109/icoac.2011.6165205
[research_malone_mason_1992]: https://doi.org/10.2514/6.1992-4221
[research_mammadov_gueaieb_2014]: https://doi.org/10.1109/icuas.2014.6842279
[research_mann_1963]: https://doi.org/10.4271/630220
[research_manned_general_2026]: https://doi.org/10.1142/9789819823468_0010
[research_manokaran_vidya_2009]: https://doi.org/10.2514/1.39732
[research_manon_1981]: https://doi.org/10.2514/3.44726
[research_mansor_sahwee_2019]: https://doi.org/10.1109/iconda47345.2019.9034911
[research_maraman_1987]: https://doi.org/10.21236/ada268599
[research_marchese_1963]: https://doi.org/10.21236/ad0442887
[research_marchmaniii_donatelli_1983]: https://doi.org/10.2514/6.1983-2555
[research_mardanpour_hodges_2013]: https://doi.org/10.2514/6.2013-1570
[research_mardanpour_hodges_2014]: https://doi.org/10.1016/j.jfluidstructs.2013.09.020
[research_mare_2006]: https://doi.org/10.1108/17488840610675546
[research_marievianney_li_2018]: https://doi.org/10.1109/iaeac.2018.8577825
[research_marino_2001]: https://doi.org/10.21236/ada404020
[research_marinov_penev_2025]: https://doi.org/10.2478/kbo-2025-0083
[research_mark_dehart_1976]: https://doi.org/10.2514/6.1976-910
[research_marker_2009]: https://doi.org/10.21236/ada540177
[research_marquesfilho_riosneto_2016]: https://doi.org/10.21528/cbic2011-14.1
[research_marquis_2003]: https://doi.org/10.1002/j.2161-4296.2003.tb00331.x
[research_marretta_davi_1999]: https://doi.org/10.2514/2.2455
[research_marshall_2011]: https://doi.org/10.1201/b11202-4
[research_marshall_2016]: https://doi.org/10.1201/9781315372044-5
[research_martin_1963]: https://doi.org/10.2514/6.1963-484
[research_martin_irani_2022]: https://doi.org/10.1016/j.oceaneng.2022.110957
[research_martin_mcmahon_2017]: https://doi.org/10.7249/rr2006
[research_martin_travis_2010]: https://doi.org/10.1109/plans.2010.5507307
[research_martindale_rockwell_1974]: https://doi.org/10.21236/ada002869
[research_martinez_2022]: https://doi.org/10.1386/eme_00121_7
[research_martinez_richardson_2013]: https://doi.org/10.1109/icra.2013.6631404
[research_martinezval_perez_1994]: https://doi.org/10.2514/3.46646
[research_martone_1983]: https://doi.org/10.21236/ada138501
[research_martone_hawkins_1983]: https://doi.org/10.21236/ada138364
[research_martorella_kelly_1981]: https://doi.org/10.2514/6.1981-1710
[research_marwaha_valasek_2009]: https://doi.org/10.2514/6.2009-1887
[research_marx_mavris_1995]: https://doi.org/10.2514/6.1995-3861
[research_maskell]: https://doi.org/10.22215/etd/1982-00664
[research_mason_1990]: https://doi.org/10.2514/6.1990-3262
[research_mason_iglesias_2001]: https://doi.org/10.2514/6.2001-5234
[research_massarweh_teunissen_2025]: https://doi.org/10.5194/egusphere-egu24-19367
[research_masud_khan_2015]: https://doi.org/10.2514/6.2015-0773
[research_matamoros_devisser_2018]: https://doi.org/10.2514/6.2018-1116
[research_mathematical_model_2023]: https://doi.org/10.36652/0869-4931-2023-77-1-20-26
[research_mathias_ross_1995]: https://doi.org/10.2514/3.46858
[research_mathyfranzjosef_2012]: https://doi.org/10.3233/978-1-61499-063-5-418
[research_matson_licht_2011]: https://doi.org/10.21236/ada535726
[research_matsuno_andreevamori_2023]: https://doi.org/10.2514/6.2023-4408
[research_matsushima_2001]: https://doi.org/10.21236/ada526557
[research_matsushita_miyata]: https://doi.org/10.1109/sice.2002.1195240
[research_maurer_1982]: https://doi.org/10.21236/ada128026
[research_maurer_1987]: https://doi.org/10.21236/ada195714
[research_maute_reich_2006]: https://doi.org/10.2514/1.12802
[research_maybourn_1983]: https://doi.org/10.1017/s0373463300039710
[research_mayer_2000]: https://doi.org/10.4271/2000-01-1699
[research_mayfield_baker_2001]: https://doi.org/10.21236/ada397631
[research_mazzitelli_1966]: https://doi.org/10.2514/6.1966-790
[research_mazzitelli_1967]: https://doi.org/10.2514/3.43839
[research_mcallister_parish_2009]: https://doi.org/10.2514/6.2009-5264
[research_mcbreen_boling_2023]: https://doi.org/10.2514/6.2023-4282
[research_mcburney]: https://doi.org/10.31274/rtd-180813-8076
[research_mccarthy_chattopadhyay_1996]: https://doi.org/10.4050/jahs.41.360
[research_mccormick_1969]: https://doi.org/10.21236/ad0863818
[research_mccullough_dieckmann_1981]: https://doi.org/10.21236/ada109128
[research_mcdermott_2004]: https://doi.org/10.21236/ada523744
[research_mcdevitt_2005]: https://doi.org/10.21236/ada436605
[research_mcdonald_1980]: https://doi.org/10.1002/j.2161-4296.1980.tb01396.x
[research_mcdonald_richards_2020]: https://doi.org/10.2514/6.2020-1138
[research_mcdonnellaircraftcorpstlouismo_1950]: https://doi.org/10.21236/ad0109763
[research_mcdonnellaircraftcorpstlouismo_1963]: https://doi.org/10.21236/ad0417219
[research_mcelreath_1972]: https://doi.org/10.21236/ad0755374
[research_mcfadyen_martin_2016]: https://doi.org/10.1109/icuas.2016.7502622
[research_mcfadyen_martin_2016_b]: https://doi.org/10.1109/dasc.2016.7778006
[research_mcfadyen_martin_2018]: https://doi.org/10.1109/aero.2018.8396463
[research_mcfarland]: https://doi.org/10.1109/plans.1994.303379
[research_mcfarland_1991]: https://doi.org/10.1002/j.2161-4296.1991.tb01857.x
[research_mcgahern_2000]: https://doi.org/10.21236/ada389255
[research_mcgarey_saripalli_2013]: https://doi.org/10.1109/icuas.2013.6564692
[research_mcgee_1977]: https://doi.org/10.2514/6.1977-603
[research_mcgrath_2000]: https://doi.org/10.21236/ada531665
[research_mcgregor_smith_1965]: https://doi.org/10.2514/6.1965-705
[research_mcingvale_dudley_1990]: https://doi.org/10.2514/6.1990-3280
[research_mckendrick_shaw_2013]: https://doi.org/10.1177/0018720813496269
[research_mckinnis_hauptman_2021]: https://doi.org/10.1109/icuas51884.2021.9476780
[research_mclaughlin_perhinschi_2023]: https://doi.org/10.1007/978-3-031-29933-9_11
[research_mcleod_2025]: https://doi.org/10.1201/9781003679479-9
[research_mcleod_2025_b]: https://doi.org/10.1201/9781003679479-13
[research_mcleod_2025_c]: https://doi.org/10.1201/9781003679479-11
[research_mcleod_2025_d]: https://doi.org/10.1201/9781003679479-10
[research_mcmanus_walker_2006]: https://doi.org/10.2514/1.15204
[research_mcmillin_wood_1987]: https://doi.org/10.2514/3.45529
[research_mcmuldroch_stein_1979]: https://doi.org/10.1109/cdc.1979.270259
[research_mcnally_warner_1992]: https://doi.org/10.1002/j.2161-4296.1992.tb01872.x
[research_mcroberts_early_2015]: https://doi.org/10.2514/1.c032726
[research_medina_patel_2021]: https://doi.org/10.2514/6.2021-4096
[research_mehta_kaiser_2006]: https://doi.org/10.2514/6.2006-6718
[research_mei_2025]: https://doi.org/10.4337/9781035315987.00047
[research_mejdrich_1977]: https://doi.org/10.21236/ada052652
[research_mejias_2014]: https://doi.org/10.1109/icuas.2014.6842380
[research_mekdeci_cummings_2009]: https://doi.org/10.1145/1865909.1865911
[research_meng_2013]: https://doi.org/10.4028/www.scientific.net/amm.397-400.1598
[research_meng_li_2014]: https://doi.org/10.1109/chicc.2014.6895687
[research_meng_sun_2023]: https://doi.org/10.33012/2023.18609
[research_meng_wang_2019]: https://doi.org/10.1109/tie.2019.2891465
[research_mengali_pieracci_2000]: https://doi.org/10.2514/2.4579
[research_mengying_hua_2017]: https://doi.org/10.1109/icus.2017.8278326
[research_menner_lavretsky_2026]: https://doi.org/10.2514/6.2026-1171
[research_menon_walker_1984]: https://doi.org/10.2514/6.1984-1895
[research_menon_walker_1985]: https://doi.org/10.2514/3.20036
[research_mercadoravell]: https://doi.org/10.70675/458fa1dbz4811z44c3zaa6az8c415b592611
[research_merkel_whitmoyer_1976]: https://doi.org/10.2514/6.1976-1950
[research_mertzlufft_carvajal_2022]: https://doi.org/10.1103/aps.dfd.2022.gfm.v0102
[research_methodology_to_2010]: https://doi.org/10.1017/cbo9780511844652.004
[research_metin_uzuner_2023]: https://doi.org/10.2514/6.2023-1572
[research_meyer_2013]: https://doi.org/10.21236/ada613351
[research_meyer_2015]: https://doi.org/10.21236/ad1019138
[research_meynlarrya_zellpetert_1993]: https://ntrs.nasa.gov/citations/19930046932
[research_mi_zhang_2022]: https://doi.org/10.1007/s10291-022-01363-8
[research_michalson_1995]: https://doi.org/10.1109/62.469796
[research_michaud_santerre_2001]: https://doi.org/10.1007/pl00012888
[research_michini_how_2011]: https://doi.org/10.2514/6.2011-1515
[research_micklos_1991]: https://doi.org/10.21236/ada239511
[research_microwave_landing]: https://doi.org/10.4271/arp4102/12
[research_middleton_1979]: https://doi.org/10.21236/ada088303
[research_middleton_1980]: https://doi.org/10.21236/ada091221
[research_middleton_thalmann_1981]: https://doi.org/10.21236/ada105609
[research_mikhailov_mikhailov_2010]: https://doi.org/10.1134/s2075108710010025
[research_milano_primatesta_2022]: https://doi.org/10.1109/icuas54217.2022.9836146
[research_milbert_2005]: https://doi.org/10.1002/j.2161-4296.2005.tb01729.x
[research_milbert_2005_b]: https://doi.org/10.1002/j.2161-4296.2005.tb01738.x
[research_miles_1990]: https://doi.org/10.21236/ada223204
[research_miles_lepping_1962]: https://doi.org/10.21236/ad0294968
[research_miller_1968]: https://doi.org/10.2514/6.1968-816
[research_miller_1969]: https://doi.org/10.2514/6.1969-897
[research_miller_1970]: https://doi.org/10.2514/3.44206
[research_miller_2006]: https://doi.org/10.21236/ada521374
[research_miller_2013]: https://doi.org/10.5898/jhri.1.2.miller
[research_miller_burkhalter_1987]: https://doi.org/10.2514/3.45418
[research_miller_eagan_1997]: https://doi.org/10.21236/ada334209
[research_miller_mwaffo_2023]: https://doi.org/10.1109/icuas57906.2023.10156120
[research_milner_ochieng_2011]: https://doi.org/10.1017/s0373463311000269
[research_mine_roof_2010]: https://doi.org/10.26616/nioshpub2010126
[research_mingfengzhang_liu_2012]: https://doi.org/10.1109/acc.2012.6315132
[research_mingfengzhang_liu_2013]: https://doi.org/10.1109/acc.2013.6580066
[research_minglang_haiwen_2018]: https://doi.org/10.1109/ccdc.2018.8407416
[research_miniature_unmanned]: https://doi.org/10.1007/springerreference_67265
[research_miniature_unmanned_2008]: https://doi.org/10.1007/978-0-387-48998-8_1031
[research_mintint_2018]: https://doi.org/10.47119/ijrp10020112019484
[research_miquel_moracamino_2006]: https://doi.org/10.2514/6.2006-6064
[research_mirabile]: https://doi.org/10.33915/etd.1389
[research_mirosavljevic_2023]: https://doi.org/10.1007/978-3-031-42041-2_33
[research_mirot_2013]: https://doi.org/10.15394/jaaer.2013.1317
[research_mirzaei_abdollahi_2008]: https://doi.org/10.1109/elt.2008.28
[research_mirzayev_ahmadova_2025]: https://doi.org/10.1007/978-3-032-07678-6_6
[research_mishra_ullah_2022]: https://doi.org/10.1109/mapcon56011.2022.10046748
[research_misovec_inanc]: https://doi.org/10.1109/cdc.2003.1273100
[research_misra_bai_2018]: https://doi.org/10.23919/acc.2018.8431815
[research_misra_bai_2019]: https://doi.org/10.2514/1.g004160
[research_misra_bayliss_1993]: https://doi.org/10.1002/j.2161-4296.1993.tb02296.x
[research_mistree_1987]: https://doi.org/10.2514/6.1987-2965
[research_mitchamgradyl_stevensjosephe_1956]: https://ntrs.nasa.gov/citations/19930084649
[research_mitchell_hoh_1983]: https://doi.org/10.2514/6.1983-2106
[research_moafipoor_bock_2018]: https://doi.org/10.33012/2018.15896
[research_moafipoor_grejnerbrzezinska_2012]: https://doi.org/10.1017/s0373463312000240
[research_modeling_the_2015]: https://doi.org/10.1002/9781119174882.ch2
[research_moeller_rediniotis_2002]: https://doi.org/10.2514/2.3032
[research_moen_williams_1966]: https://doi.org/10.2514/6.1966-1828
[research_mohamed_aljaroodi_2013]: https://doi.org/10.1109/icuas.2013.6564794
[research_mohiuddin_psiaki_2005]: https://doi.org/10.2514/6.2005-6054
[research_mohiuddin_psiaki_2006]: https://doi.org/10.2514/6.2006-6797
[research_mokotoff_arnson_2025]: https://doi.org/10.2514/6.2025-2374
[research_mokotoff_arnson_2026]: https://doi.org/10.2514/1.c038452
[research_montalvo_costello_2015]: https://doi.org/10.2514/1.c032634
[research_montenbruck_damico_2012]: https://doi.org/10.1007/978-1-4614-4541-8_5
[research_montenbruck_ebinuma_2002]: https://doi.org/10.1016/s1270-9638(02)01185-9
[research_montenbruck_hackel_2017]: https://doi.org/10.1007/s00190-017-1090-2
[research_montenbruck_swatschina_2012]: https://doi.org/10.1007/s10291-011-0252-6
[research_montenbruck_wermuth_2011]: https://doi.org/10.1002/j.2161-4296.2011.tb02587.x
[research_montes_mitchell_2022]: https://doi.org/10.2514/6.2022-3230
[research_mooij_1985]: https://doi.org/10.1007/978-94-017-1193-7_5
[research_mooij_1985_b]: https://doi.org/10.1007/978-94-017-1193-7
[research_mooij_1985_c]: https://doi.org/10.1007/978-94-017-1193-7_6
[research_mooij_1985_d]: https://doi.org/10.1007/978-94-017-1193-7_3
[research_mook_shyu_1990]: https://doi.org/10.2514/6.1990-3402
[research_mook_shyu_1992]: https://doi.org/10.2514/3.20823
[research_mook_swanson_1990]: https://doi.org/10.2514/6.1990-3374
[research_moonbeomheo_pervan_2006]: https://doi.org/10.1109/taes.2006.1642581
[research_moore_2000]: https://doi.org/10.21236/ada389246
[research_moore_2013]: https://doi.org/10.2514/6.2013-1380
[research_moorhouse_1991]: https://doi.org/10.2514/6.1991-2641
[research_morley_1961]: https://doi.org/10.4271/610197
[research_morley_2013]: https://doi.org/10.21236/ada613348
[research_morote_liano_2012]: https://doi.org/10.2514/1.c031802
[research_morozov_2015]: https://doi.org/10.3103/s106879981501016x
[research_morris_frew_2005]: https://doi.org/10.21236/ada437347
[research_morris_tigner_1995]: https://doi.org/10.2514/6.1995-3327
[research_morriscekjr_1983]: https://ntrs.nasa.gov/citations/19830057439
[research_morriscekjr_1984]: https://ntrs.nasa.gov/citations/19840007077
[research_morrison_zahraee]: https://doi.org/10.18260/1-2--6415
[research_morton_1956]: https://doi.org/10.1108/eb032772
[research_morujao_mendes_2008]: https://doi.org/10.5081/jgps.7.1.35
[research_mosavi_shafiee_2015]: https://doi.org/10.1007/s10291-015-0442-8
[research_moser_2011]: https://doi.org/10.21236/ada553342
[research_mostafa_schnell_2016]: https://doi.org/10.1109/icnsurv.2016.7486379
[research_moum_2010]: https://doi.org/10.21236/ada542580
[research_mueller_2018]: https://doi.org/10.1115/dscc2018-9079
[research_mueller_krozel_2000]: https://doi.org/10.2514/6.2000-4067
[research_mujica_1987]: https://doi.org/10.2514/6.1987-2869
[research_mukherjee_2015]: https://doi.org/10.4324/9781315668512-5
[research_muleropazmany_negro_2014]: https://doi.org/10.1139/juvs-2013-0012
[research_muller_2001]: https://doi.org/10.21236/ada399037
[research_muller_bauer_2024]: https://doi.org/10.5220/0012951500003822
[research_mullinsjr_tipton_1996]: https://doi.org/10.2514/6.1996-894
[research_multi_finger_dynamic_2025]: https://doi.org/10.3901/jme.2025.15.441
[research_muniraj_farhood_2017]: https://doi.org/10.1109/icuas.2017.7991465
[research_munroe_1978]: https://doi.org/10.21236/ada053862
[research_murakami_peck_2011]: https://doi.org/10.2514/6.2011-1629
[research_muralikrishna_mallesham_2022]: https://doi.org/10.1109/iceca55336.2022.10009084
[research_murillo_montes_2025]: https://doi.org/10.1109/icuas65942.2025.11007803
[research_murray_1949]: https://doi.org/10.1108/eb031761
[research_murray_richardson_2022]: https://doi.org/10.2514/6.2022-3417
[research_murraysmith_1995]: https://doi.org/10.1007/978-1-4615-2504-2_11
[research_musolino_rizzo_2012]: https://doi.org/10.1109/eml.2012.6325162
[research_mustopa_2022]: https://doi.org/10.37868/dss.v3.id203
[research_mutz_pierce_1964]: https://doi.org/10.2514/6.1964-601
[research_myers_1973]: https://doi.org/10.21236/ad0758463
[research_myers_1974]: https://doi.org/10.21236/ad0784140
[research_myklebust_gelhausen_1993]: https://doi.org/10.2514/6.1993-3970
[research_nadler_2015]: https://doi.org/10.21236/ad1001745
[research_naghash_enns_1998]: https://doi.org/10.2514/6.1998-4207
[research_naik_ostowari_1990]: https://doi.org/10.2514/3.45906
[research_nam]: https://doi.org/10.17918/00008556
[research_nam_mavris_2018]: https://doi.org/10.2514/1.c032099
[research_nam_min_2026]: https://doi.org/10.33012/navi.769
[research_nan_yang_2024]: https://doi.org/10.3390/aerospace11110885
[research_nangia_palmer_2007]: https://doi.org/10.2514/6.2007-4569
[research_nangia_palmer_2007_b]: https://doi.org/10.2514/6.2007-250
[research_napier_1989]: https://doi.org/10.1007/978-3-642-74585-0_41
[research_nastasi_martorella_1983]: https://doi.org/10.2514/6.1983-2072
[research_natalie_jacob_2019]: https://doi.org/10.2514/6.2019-3404
[research_natesan_bhat_2005]: https://doi.org/10.2514/6.2005-6406
[research_natesan_gu_2008]: https://doi.org/10.3182/20080706-5-kr-1001.02067
[research_nath_2025]: https://doi.org/10.59551/ijhmp/25832069/2025.6.2.108
[research_nationalresearchcouncilwashingtondc_2001]: https://doi.org/10.21236/ada397119
[research_naundrup]: https://doi.org/10.54337/aau763800320
[research_navalairdevelopmentcenterwarminsterpa_1975]: https://doi.org/10.21236/ada358666
[research_navalairsystemscommandpatuxentrivermd_2013]: https://doi.org/10.21236/ada614838
[research_navalairsystemscommandwashingtondc_1978]: https://doi.org/10.21236/ada060081
[research_navalairsystemscommandwashingtondc_1980]: https://doi.org/10.21236/ada085450
[research_navalappliedsciencelabbrooklynny_1963]: https://doi.org/10.21236/ad0419055
[research_navalaviationenterprisepatuxentrivermd_2012]: https://doi.org/10.21236/ada585703
[research_navalpostgraduateschoolmontereyca_1981]: https://doi.org/10.21236/ada484210
[research_nave_1973]: https://doi.org/10.21236/ad0764516
[research_nayerabadi_mohammadi_2022]: https://doi.org/10.1109/iccia54998.2022.9737174
[research_neal_2010]: https://doi.org/10.21236/ada525097
[research_nebiker_1981]: https://doi.org/10.2514/3.44722
[research_nebula_2018]: https://doi.org/10.1109/aero.2018.8396387
[research_nedresky_1996]: https://doi.org/10.21236/ada309766
[research_neff_2019]: https://doi.org/10.58940/2374-6793.1303
[research_negaard_1980]: https://doi.org/10.21236/ada361289
[research_negast_paschall]: https://doi.org/10.1109/naecon.1992.220595
[research_negre_1975]: https://doi.org/10.2514/6.1975-1023
[research_nelson_1974]: https://doi.org/10.21236/ad0787193
[research_nelson_bolia_2006]: https://doi.org/10.1016/s1479-3601(05)07004-9
[research_nelson_calhoun_2006]: https://doi.org/10.21236/ada444586
[research_nelson_dix_2003]: https://doi.org/10.21236/ada412680
[research_nengjianwang_xiangleimeng_2016]: https://doi.org/10.1109/imcec.2016.7867313
[research_neto_douradovilla_2024]: https://doi.org/10.1109/icuas60882.2024.10557080
[research_nettleton_1965]: https://doi.org/10.2514/6.1965-713
[research_neuenswander_2013]: https://doi.org/10.21236/ada583239
[research_neufeld_2021]: https://doi.org/10.32920/ryerson.14648304.v1
[research_neusypin_kupriyanov_2023]: https://doi.org/10.1007/s10291-023-01433-5
[research_new_achievements_2023]: https://doi.org/10.1007/978-3-031-29933-9
[research_new_aircraft_2019]: https://doi.org/10.1108/oxan-es249495
[research_new_method_2005]: https://doi.org/10.5139/jksas.2005.33.1.039
[research_new_steam_1952]: https://doi.org/10.1016/0016-0032(52)90994-0
[research_newberry_1998]: https://doi.org/10.1016/s1369-8869(98)00015-9
[research_newcome_2004]: https://doi.org/10.2514/4.868894
[research_newcome_2009]: https://doi.org/10.1017/s0001924000003122
[research_newman_stanzione_1991]: https://doi.org/10.2514/6.1991-3097
[research_ngo_sultan_2024]: https://doi.org/10.2514/6.2024-2398
[research_nguyen_2019]: https://doi.org/10.1109/vppc46532.2019.8952226
[research_nguyen_choi_2009]: https://doi.org/10.2514/6.2009-7093
[research_nguyen_choi_2013]: https://doi.org/10.1016/j.ast.2012.04.004
[research_nguyen_crismer_2024]: https://doi.org/10.1109/sii58957.2024.10417303
[research_ni_hu_2018]: https://doi.org/10.1007/978-3-031-01496-3_4
[research_ni_hu_2018_b]: https://doi.org/10.1007/978-3-031-01496-3_3
[research_ni_zhang_2026]: https://doi.org/10.20944/preprints202601.1019.v1
[research_nichols_1998]: https://doi.org/10.21236/ada397134
[research_nichols_2021]: https://doi.org/10.1201/9780429347498-18
[research_nichols_westmoreland_2007]: https://doi.org/10.2514/1.23067
[research_nickol_2011]: https://doi.org/10.2514/6.2011-6951
[research_nickolcraigl_guynnmarkd_2007]: https://ntrs.nasa.gov/citations/20070004936
[research_nicosia_loss]: https://doi.org/10.1109/ntc.1993.293001
[research_nida_oconnor_2006]: https://doi.org/10.21236/ada515555
[research_nielsen_1997]: https://doi.org/10.1109/7.570809
[research_niendorf_adolf_2012]: https://doi.org/10.2514/6.2012-2567
[research_nieuwenhuisen_droeschel_2014]: https://doi.org/10.1109/icuas.2014.6842355
[research_niewoehner_filbey_2005]: https://doi.org/10.2514/1.12406
[research_nigam_ayyalasomayajula_2015]: https://doi.org/10.2514/6.2015-3360
[research_nigam_kroo_2008]: https://doi.org/10.2514/6.2008-5913
[research_nijveldt_ijtsma_2022]: https://doi.org/10.2514/6.2022-3620
[research_nikiforov_1995]: https://doi.org/10.2514/6.1995-3192
[research_nikolaidis_laoudias_2025]: https://doi.org/10.1109/icuas65942.2025.11007842
[research_nikolic_2007]: https://doi.org/10.2514/1.23490
[research_nikolic_jumper_1996]: https://doi.org/10.2514/3.46916
[research_niles_1964]: https://doi.org/10.21236/ad0607953
[research_ningluo_lachapelle_2003]: https://doi.org/10.1109/taes.2003.1238747
[research_noble_bhandari_2017]: https://doi.org/10.1109/icuas.2017.7991337
[research_noe_zabaneh]: https://doi.org/10.1109/plans.1994.303364
[research_noise_measurements]: https://doi.org/10.3403/30426804
[research_nominal_aircraft]: https://doi.org/10.1007/bfb0043102
[research_noro_inamori_2020]: https://doi.org/10.1299/jsmemecj.2020.j19127
[research_norris_1998]: https://doi.org/10.1016/s1369-8869(98)00007-x
[research_norris_bauer_1993]: https://doi.org/10.2514/3.46372
[research_northropaircraftinchawthorneca_1952]: https://doi.org/10.21236/ad0024361
[research_northropaircraftinchawthorneca_1953]: https://doi.org/10.21236/ad0022941
[research_norton_dyme_1952]: https://doi.org/10.21236/ad0018119
[research_norwood_chichester_2015]: https://doi.org/10.2514/6.2015-0459
[research_noureldin_karamat_2012]: https://doi.org/10.1007/978-3-642-30466-8_8
[research_novakovic_vasic_2016]: https://doi.org/10.5937/str1604022n
[research_nowak_kopecki_2022]: https://doi.org/10.3390/aerospace9060285
[research_nowel_cellmer_2018]: https://doi.org/10.1007/s10291-017-0694-6
[research_nugent_girard_2003]: https://doi.org/10.2514/6.2003-6513
[research_nugroho_2026]: https://doi.org/10.14203/widyariset.14.3.2011.633-642
[research_null]: https://doi.org/10.4271/air8776
[research_numerical_methods_2026]: https://doi.org/10.1007/978-3-031-97725-1
[research_nygard_1995]: https://doi.org/10.21236/ada300064
[research_obayashi_yamaguchi_1997]: https://doi.org/10.2514/2.2231
[research_oblique_wing_2020]: https://doi.org/10.1002/9781119667063.ch10
[research_obradovic_subbarao_2010]: https://doi.org/10.2514/6.2010-8236
[research_obradovic_subbarao_2011]: https://doi.org/10.2514/1.c000313
[research_obye_hakim_1984]: https://doi.org/10.2514/6.1984-1176
[research_odijk_teunissen_2002]: https://doi.org/10.1007/978-3-662-04709-5_65
[research_odijk_teunissen_2011]: https://doi.org/10.2478/v10156-010-0017-0
[research_odijk_teunissen_2012]: https://doi.org/10.1061/(asce)su.1943-5428.0000085
[research_odolinski_teunissen_2017]: https://doi.org/10.1007/s10291-017-0613-x
[research_officeofnavalresearcharlingtonva_1993]: https://doi.org/10.21236/ada268966
[research_ogorzalek_doyle_2019]: https://doi.org/10.2514/6.2019-3050
[research_oh_johnson_2007]: https://doi.org/10.2514/6.2007-6866
[research_oh_kim_2017]: https://doi.org/10.2514/1.c032984
[research_oh_park_2016]: https://doi.org/10.5140/jass.2016.33.1.45
[research_ohiostateunivcolumbuselectrosciencelab_1968]: https://doi.org/10.21236/ada951904
[research_ojha_chow_2009]: https://doi.org/10.1109/iecon.2009.5415281
[research_okcu_2016]: https://doi.org/10.1109/icuas.2016.7502593
[research_okeefe_2008]: https://doi.org/10.2514/6.2008-7614
[research_okeefe_julien_2006]: https://doi.org/10.1016/j.actaastro.2005.12.008
[research_oktay_eraslan_2024]: https://doi.org/10.1108/aeat-09-2022-0262
[research_olds_1998]: https://doi.org/10.21236/ada389224
[research_olejnik_rogolski_2019]: https://doi.org/10.1109/metroaerospace.2019.8869609
[research_olivaresmendez]: https://doi.org/10.20868/upm.thesis.15082
[research_oliver_1962]: https://doi.org/10.2307/3007570
[research_oliver_2012]: https://doi.org/10.21236/ada561658
[research_olsen_park_1999]: https://doi.org/10.1002/j.2161-4296.1999.tb02394.x
[research_olson_2005]: https://doi.org/10.21236/ada435967
[research_olson_henricks_2018]: https://doi.org/10.2514/6.2018-4143
[research_olson_toombs_2020]: https://doi.org/10.1109/icuas48674.2020.9213860
[research_omar_yanzhong_2016]: https://doi.org/10.1109/itnec.2016.7560421
[research_onat_tolle_1979]: https://doi.org/10.21236/ada074454
[research_oncu_yildiz_2014]: https://doi.org/10.21236/ada620843
[research_ono_2024]: https://doi.org/10.2514/6.2024-1061
[research_oole_1993]: https://doi.org/10.21236/ada277206
[research_oosterom_babuska_2001]: https://doi.org/10.2514/6.2001-4358
[research_opening_up_2007]: https://doi.org/10.1108/aeat.2007.12779bab.023
[research_optimal_control_2018]: https://doi.org/10.23977/icamcs.2018.061
[research_options_for_2005]: https://doi.org/10.7249/mg240
[research_ordaz_lee_2004]: https://doi.org/10.2514/6.2004-6336
[research_ordoukhanian_madni_2019]: https://doi.org/10.2514/6.2019-0222
[research_oren_kocyigit_2016]: https://doi.org/10.1109/icuas.2016.7502556
[research_orhan_2020]: https://doi.org/10.1109/icuas48674.2020.9213945
[research_orhan_subbarao_2021]: https://doi.org/10.2514/6.2021-0108
[research_orozco_walsh_2026]: https://doi.org/10.1109/icuas69441.2026.11598640
[research_ortiz_2008]: https://doi.org/10.21236/ada500198
[research_osadchiy_kalich_2013]: https://doi.org/10.1109/apuavd.2013.6705294
[research_oshinmittal_alokkumarsahu_2024]: https://doi.org/10.61359/11.2106-2447
[research_osiecki_fortonska_2023]: https://doi.org/10.1109/icuas57906.2023.10156331
[research_ossmann_luspay_2019]: https://doi.org/10.1109/aero.2019.8741853
[research_osterman_2010]: https://doi.org/10.21236/ada525089
[research_ou_validated_foundation_2008]: https://doi.org/10.1108/aeat.2008.12780aab.021
[research_overholt_2007]: https://doi.org/10.21236/ada478576
[research_overview_of]: https://doi.org/10.4271/air6280
[research_overview_of_2012]: https://doi.org/10.2514/5.9781600868443.0001.0023
[research_overview_of_2014]: https://doi.org/10.2514/5.9781624102615.0001.0024
[research_ovmilenin_2019]: https://doi.org/10.21557/mth.57847377
[research_owais_midtiby_2022]: https://doi.org/10.1109/icuas54217.2022.9836092
[research_owashi_tanaka_2017]: https://doi.org/10.1299/jsmermd.2017.1p2-e04
[research_owens_macdonald_2021]: https://doi.org/10.2514/6.2021-0376
[research_oyama_2021]: https://doi.org/10.32920/ryerson.14635701
[research_ozartan_akgul_2013]: https://doi.org/10.1109/icuas.2013.6564686
[research_ozcan_alemdaroglu_2015]: https://doi.org/10.1109/icuas.2015.7152280
[research_ozoroski_mas_2003]: https://doi.org/10.2514/6.2003-6566
[research_oztekin_flass_2011]: https://doi.org/10.1007/978-94-007-3033-5_2
[research_pack_york]: https://doi.org/10.1109/icnsc.2006.1673187
[research_pack_york_2008]: https://doi.org/10.4337/9781035305520.00019
[research_pack_york_b]: https://doi.org/10.1109/icnsc.2005.1461264
[research_paget_atherton_2004]: https://doi.org/10.1016/b978-1-85573-831-7.50161-9
[research_palaia_salem_2025]: https://doi.org/10.2514/1.c038131
[research_palmer_1970]: https://doi.org/10.21236/ad0711349
[research_palmisano_gillam_2005]: https://doi.org/10.1037/1076-898x.11.1.19
[research_palomino_epp_2012]: https://doi.org/10.21236/ada576313
[research_pan_huang_2019]: https://doi.org/10.5028/jatm.v11.1074
[research_pan_ma_2025]: https://doi.org/10.1109/comea66280.2025.11241272
[research_pan_pi_2024]: https://doi.org/10.2139/ssrn.5047766
[research_panchal_hein_2024]: https://doi.org/10.2514/6.2024-1465
[research_panday_pedro_2018]: https://doi.org/10.1109/cec.2018.8477720
[research_pandey_kumari_2024]: https://doi.org/10.1002/9781394230648.ch7
[research_panickar_murray_2013]: https://doi.org/10.2514/1.c031747
[research_pant_fielding_1999]: https://doi.org/10.1016/s1369-8869(99)00020-8
[research_papa_2023]: https://doi.org/10.3390/electronics12071591
[research_papa_ariante_2026]: https://doi.org/10.3390/electronics15091779
[research_papageorgiou_dalkilic_2019]: https://doi.org/10.1109/icaset.2019.8714274
[research_papageorgiou_tarkian_2018]: https://doi.org/10.2514/1.c034314
[research_paranjape_chung_2010]: https://doi.org/10.2514/6.2010-7633
[research_parasuraman_kidwell_2013]: https://doi.org/10.1177/0018720813510736
[research_parasuraman_miller_2006]: https://doi.org/10.1016/s1479-3601(05)07018-9
[research_parenteau_laurendeau_2018]: https://doi.org/10.1016/j.ast.2018.02.023
[research_park_2025]: https://doi.org/10.1016/j.energy.2025.139192
[research_park_bang_2022]: https://doi.org/10.31818/jknst.2022.03.5.1.38
[research_park_jeong_2025]: https://doi.org/10.1016/j.apenergy.2024.124567
[research_parker_1980]: https://doi.org/10.21236/ada087427
[research_parker_1986]: https://doi.org/10.2514/6.1986-2622
[research_parkinson_axelrad_1988]: https://doi.org/10.1002/j.2161-4296.1988.tb00955.x
[research_parkinson_bauman_1970]: https://doi.org/10.21236/ad0722412
[research_parsons_1989]: https://doi.org/10.21236/ada599462
[research_parsonsengineeringsciencesincpasadenaca_1991]: https://doi.org/10.21236/ada413142
[research_particle_filter_2008]: https://doi.org/10.5302/j.icros.2008.14.8.785
[research_parts_1979]: https://doi.org/10.21236/ada076512
[research_passenger_seat]: https://doi.org/10.4271/arp750a
[research_passner_kirby_2012]: https://doi.org/10.21236/ada561959
[research_patek_smrcek_1999]: https://doi.org/10.1016/s1369-8869(99)00015-4
[research_patel_brinton_2011]: https://doi.org/10.2514/6.2011-1457
[research_patel_krishnamurthy_2021]: https://doi.org/10.1109/icuas51884.2021.9476881
[research_paterson_1999]: https://doi.org/10.2514/2.2468
[research_paterson_paterson_1997]: https://doi.org/10.2514/6.1997-5544
[research_pathak_1976]: https://doi.org/10.21236/ada088940
[research_patterson_1989]: https://doi.org/10.2514/6.1989-2011
[research_patterson_champion_1991]: https://doi.org/10.2514/6.1991-3169
[research_paul]: https://doi.org/10.15581/10171/65007
[research_paul_fendley_2013]: https://doi.org/10.21236/ada595397
[research_pauls_2012]: https://doi.org/10.21236/ada606087
[research_paulsen_1998]: https://doi.org/10.21236/ada398707
[research_pavkovic_krznar_2020]: https://doi.org/10.1109/icuas48674.2020.9214002
[research_payton_2011]: https://doi.org/10.21236/ada555678
[research_pedro_panday_2013]: https://doi.org/10.2478/amcs-2013-0007
[research_pedrozo_2022]: https://doi.org/10.1017/9781009042178.011
[research_peer_2000]: https://doi.org/10.3940/rina.ws.2000.07
[research_pehlivan_ozen_2023]: https://doi.org/10.1007/978-3-031-37160-8_5
[research_pei_huang_2025]: https://doi.org/10.1109/raiic65850.2025.11170302
[research_pei_xia_2018]: https://doi.org/10.1007/s11768-018-8064-7
[research_peixoto_2024]: https://doi.org/10.5040/9781350411708.ch-9
[research_peng_2021]: https://doi.org/10.1142/s2737480721500096
[research_peng_kaiqi_2025]: https://doi.org/10.23919/ccc64809.2025.11178793
[research_peng_li_2007]: https://doi.org/10.2514/6.2007-6764
[research_peng_li_2025]: https://doi.org/10.1016/j.isatra.2025.10.052
[research_peng_lin_2016]: https://doi.org/10.5220/0005949603850392
[research_peng_mohseni_2014]: https://doi.org/10.1109/icuas.2014.6842298
[research_peng_wang_2014]: https://doi.org/10.4028/www.scientific.net/amr.1049-1050.953
[research_peng_xie_2020]: https://doi.org/10.3390/app10249033
[research_pentz_tang_2019]: https://doi.org/10.4018/978-1-5225-8365-3.ch024
[research_pereira_sanguino_2016]: https://doi.org/10.1109/icl-gnss.2016.7533840
[research_performance_evaluation_of_2023]: https://doi.org/10.12677/gst.2023.112017
[research_performance_investigation_2006]: https://doi.org/10.5302/j.icros.2006.12.8.773
[research_performance_investigation_2007]: https://doi.org/10.5302/j.icros.2007.13.8.817
[research_perkins_1991]: https://doi.org/10.2514/6.1991-3115
[research_perry_2000]: https://doi.org/10.21236/ada381737
[research_perry_2011]: https://doi.org/10.2514/6.2011-6948
[research_perry_schneider_1984]: https://doi.org/10.2514/6.1984-2449
[research_pervan_chan_2003]: https://doi.org/10.1002/j.2161-4296.2003.tb00328.x
[research_pervan_cohen_1994]: https://doi.org/10.1002/j.2161-4296.1994.tb02569.x
[research_pervan_parkinson_1997]: https://doi.org/10.2514/2.4131
[research_pervan_pullen_1998]: https://doi.org/10.1002/j.2161-4296.1998.tb02372.x
[research_peters_andrisaniii_1997]: https://doi.org/10.2514/6.1997-3701
[research_peterson_finkenstadt_2011]: https://doi.org/10.21236/ada555656
[research_peterson_gipe_1963]: https://doi.org/10.21236/ad0296475
[research_peterson_staley_2011]: https://doi.org/10.21236/ada555650
[research_peterson_taboada_2012]: https://doi.org/10.21236/ada610335
[research_petit_kanj_2015]: https://doi.org/10.1088/0026-1394/52/2/301
[research_petnga_xu_2016]: https://doi.org/10.1109/icuas.2016.7502663
[research_petrock_huizenga_2006]: https://doi.org/10.21236/ada463921
[research_pettigrew_2003]: https://doi.org/10.21236/ada414712
[research_pettit_grandhi_2003]: https://doi.org/10.2514/2.7208
[research_pham]: https://doi.org/10.15368/theses.2012.87
[research_pham_b]: https://doi.org/10.70675/58914cc6z5676z4b06zaa2czc838f27f6996
[research_pham_c]: https://doi.org/10.31979/etd.pskw-x92d
[research_pham_sim_2002]: https://doi.org/10.21236/ada410088
[research_phan_park_2018]: https://doi.org/10.1088/1748-3190/aab313
[research_phillips_herr_2020]: https://doi.org/10.58940/2374-6793.1484
[research_phillips_hunsaker_2019]: https://doi.org/10.2514/1.c035206
[research_phillips_hunsaker_2019_b]: https://doi.org/10.2514/6.2019-3349
[research_photometric_characteristics_1968]: https://doi.org/10.6028/nbs.rpt.9350sup
[research_pieniazek_2003]: https://doi.org/10.1016/s1474-6670(17)33411-0
[research_piersol_1977]: https://doi.org/10.21236/ada037067
[research_pierson_1985]: https://doi.org/10.1016/0066-4138(85)90475-6
[research_pilot_training]: https://doi.org/10.4271/arp5707
[research_pilot_versatility]: https://doi.org/10.4271/as580b
[research_pilot_visibility]: https://doi.org/10.4271/as580
[research_pilot_visibility_b]: https://doi.org/10.4271/as580a
[research_pisani_1977]: https://doi.org/10.21236/ada047858
[research_pittsburghunivwashingtondcresearchstaff_1966]: https://doi.org/10.21236/ad0482131
[research_planform_parameterization_2014]: https://doi.org/10.1002/9781118534748.ch8
[research_podhradsky_bone_2013]: https://doi.org/10.1109/icuas.2013.6564679
[research_pollack_2013]: https://doi.org/10.31399/asm.hb.v05a.a0005739
[research_pomarolli_1965]: https://doi.org/10.21236/ad0627218
[research_pomranky_2006]: https://doi.org/10.21236/ada476904
[research_pond_1973]: https://doi.org/10.21236/ad0779728
[research_poock_1976]: https://doi.org/10.21236/ada027256
[research_poritzky_1970]: https://doi.org/10.2514/6.1970-937
[research_poritzky_1971]: https://doi.org/10.2514/3.59134
[research_portageincidahofallsid_2013]: https://doi.org/10.21236/ada596203
[research_porter_1979]: https://doi.org/10.21236/ada078422
[research_potes_retamal_2026]: https://doi.org/10.1109/icuas69441.2026.11598664
[research_pottinger_cross_2017]: https://doi.org/10.2139/ssrn.2973982
[research_powers_mclaughlin_2015]: https://doi.org/10.2514/6.2015-2374
[research_powers_mclaughlin_2018]: https://doi.org/10.2514/1.c034213
[research_pozzi_guo_2012]: https://doi.org/10.1117/12.917039
[research_prabha_raghavendra_2021]: https://doi.org/10.1016/j.matpr.2020.10.830
[research_practice_for]: https://doi.org/10.1520/f2636-08
[research_practice_for_b]: https://doi.org/10.1520/f3364-23
[research_practice_for_c]: https://doi.org/10.1520/f3686-24a
[research_practice_for_d]: https://doi.org/10.1520/f2505
[research_practices_for]: https://doi.org/10.1520/f2501-06
[research_pradeep_1998]: https://doi.org/10.1016/s1369-8869(98)00017-2
[research_pradeep_wei_2018]: https://doi.org/10.1109/gncc42960.2018.9018748
[research_prakash_2020]: https://doi.org/10.2514/6.2020-2849
[research_prasad_comandur_2018]: https://doi.org/10.4050/f-0074-2018-12780
[research_pratt_and_2009]: https://doi.org/10.1108/aeat.2009.12781cab.032
[research_precision_approach_1979]: https://doi.org/10.1108/eb035583
[research_precision_landing_1996]: https://doi.org/10.2514/5.9781600866395.0427.0459
[research_preliminary_aerodynamic_2017]: https://doi.org/10.1002/9781119406303.ch13
[research_preliminary_estimate_2010]: https://doi.org/10.2514/5.9781600867538.0123.0149
[research_preliminary_fuselage_2010]: https://doi.org/10.2514/5.9781600867538.0195.0220
[research_preliminary_sizing_2010]: https://doi.org/10.2514/5.9781600867538.0283.0292
[research_pressure_die]: https://doi.org/10.4271/air20
[research_priambodo_arifin_2022]: https://doi.org/10.1088/1742-6596/2406/1/012004
[research_price_forrest_2016]: https://doi.org/10.1016/b978-0-12-804293-9.00009-6
[research_prickett_parkes]: https://doi.org/10.1109/aero.2001.931220
[research_primatesta_2025]: https://doi.org/10.1109/icuas65942.2025.11007812
[research_primatesta_guglieri_2018]: https://doi.org/10.1109/icuas.2018.8453354
[research_primatesta_pagliano_2021]: https://doi.org/10.1109/icuas51884.2021.9476836
[research_pritpal_2005]: https://doi.org/10.21236/ada442011
[research_pritulo_gubanov_1995]: https://doi.org/10.2514/6.1995-3946
[research_probst_2010]: https://doi.org/10.21236/ada518449
[research_progri_michalson]: https://doi.org/10.1109/plans.2002.998910
[research_propulsion_2017]: https://doi.org/10.1002/9781119406303.ch5
[research_propulsion_2024]: https://doi.org/10.2514/5.9781624107290.0487.0518
[research_propulsion_data_2010]: https://doi.org/10.2514/5.9781600867538.0785.0822
[research_propulsion_system_2010]: https://doi.org/10.2514/5.9781600867538.0467.0490
[research_prudhomme_1995]: https://doi.org/10.2514/6.1995-3308
[research_psiaki_mohiuddin_2005]: https://doi.org/10.2514/6.2005-6053
[research_psiaki_mohiuddin_2007]: https://doi.org/10.2514/1.29534
[research_pugazhenthi_gopalakannan_2018]: https://doi.org/10.1109/icscan.2018.8541192
[research_pullen_enge]: https://doi.org/10.1109/cdc.1996.572689
[research_pullen_joerger_2020]: https://doi.org/10.1002/9781119458449.ch23
[research_pullen_pervan]: https://doi.org/10.1109/plans.1994.303384
[research_purdy_2010]: https://doi.org/10.1002/9780470686652.eae580
[research_purivigraipong_hodgart_2010]: https://doi.org/10.1109/taes.2010.5461660
[research_purivigraipong_unwin_2005]: https://doi.org/10.1109/tencon.2005.301345
[research_purshouse_2003]: https://doi.org/10.3940/rina.ws.2003.03
[research_purvis_2003]: https://doi.org/10.21236/ada419206
[research_putra_wiyagi_2018]: https://doi.org/10.1109/icalip.2018.8455553
[research_putscher_1967]: https://doi.org/10.21236/ad0654743
[research_pyzynski_2020]: https://doi.org/10.1109/icuas48674.2020.9213922
[research_qi_wang_2016]: https://doi.org/10.1016/j.ifacol.2016.07.810
[research_qi_wang_2017]: https://doi.org/10.23919/acc.2017.7963645
[research_qi_zhao_2018]: https://doi.org/10.23919/acc.2018.8431539
[research_qi_zhao_2018_b]: https://doi.org/10.1109/cdc.2018.8618742
[research_qian_chengquan_2010]: https://doi.org/10.1109/icoip.2010.137
[research_qianshen_suozhongyuan_2016]: https://doi.org/10.1109/cgncc.2016.7829014
[research_qiao_bai_2008]: https://doi.org/10.1109/paciia.2008.57
[research_qin_ang_2017]: https://doi.org/10.33012/2017.15095
[research_qin_yang_2024]: https://doi.org/10.1088/1402-4896/ad19bb
[research_qin_yue_2019]: https://doi.org/10.1007/s10291-019-0844-0
[research_qinkunxiao_xiaoguanggao_2006]: https://doi.org/10.1109/wcica.2006.1713131
[research_qiwei_shumei_2014]: https://doi.org/10.1109/eml.2014.6920652
[research_qu_li_2011]: https://doi.org/10.1109/icciautom.2011.6183979
[research_qu_li_2013]: https://doi.org/10.12696/gsam.2013.0935
[research_quan_edmond_2021]: https://doi.org/10.1109/icuas51884.2021.9476825
[research_quan_xiao_2018]: https://doi.org/10.1109/gncc42960.2018.9019062
[research_rabbou_elrabbany_2021]: https://doi.org/10.32920/ryerson.14669094.v1
[research_racette_dunaway_2023]: https://doi.org/10.2514/6.2023-3625
[research_raczkowski_boyd_2026]: https://doi.org/10.2514/6.2026-0915
[research_radar_altimeter_2019]: https://doi.org/10.1109/icnsurv.2019.8735127
[research_raducanu_circiu_2017]: https://doi.org/10.19062/1842-9238.2017.15.3.12
[research_ragi_chong_2013]: https://doi.org/10.1109/icuas.2013.6564698
[research_ragon_gurdal_2003]: https://doi.org/10.2514/2.6884
[research_rajamurugu_dheerajkumar_2026]: https://doi.org/10.47176/jafm.19.4.3598
[research_rajpal_pant_2011]: https://doi.org/10.2514/6.2011-547
[research_rajput_zhang_2014]: https://doi.org/10.4028/www.scientific.net/amm.643.54
[research_rajput_zhangweiguo_2015]: https://doi.org/10.1109/ascc.2015.7244649
[research_ralles_1966]: https://doi.org/10.21236/ad0645885
[research_ramasamy_2015]: https://doi.org/10.2514/6.2015-0085
[research_ramasamy_gardi_2015]: https://doi.org/10.1109/icuas.2015.7152332
[research_ramasamy_ghose_2016]: https://doi.org/10.1109/icuas.2016.7502678
[research_ramesh_subbarao_2016]: https://doi.org/10.1016/j.ifacol.2016.03.068
[research_ramin_heriana_2022]: https://doi.org/10.53866/jimi.v2i4.126
[research_ramsey_dixon_1967]: https://doi.org/10.21236/ada382399
[research_randolph_1997]: https://doi.org/10.21236/ada327417
[research_ransquin_caprace_2021]: https://doi.org/10.2514/1.g006028
[research_rao_ma_2020]: https://doi.org/10.1109/cac51589.2020.9326776
[research_rao_narayana_1995]: https://doi.org/10.1002/j.2161-4296.1995.tb01910.x
[research_rao_sarma_2001]: https://doi.org/10.1017/s0373463301001333
[research_rapinski_cellmer_2012]: https://doi.org/10.1017/s0373463312000124
[research_rapstine_sava_2017]: https://doi.org/10.1139/juvs-2017-0019
[research_rarthlomeusz_paul_1993]: https://doi.org/10.1108/eb037363
[research_rasmussen_1992]: https://doi.org/10.21236/ada263304
[research_ratcliffe_1983]: https://doi.org/10.1017/s0373463300039709
[research_ravenstein_1984]: https://doi.org/10.21236/ada154181
[research_ray_salychev_1999]: https://doi.org/10.1007/s001900050267
[research_raychaudhuri]: https://doi.org/10.17918/00004908
[research_raychem_gel_1998]: https://doi.org/10.1108/aeat.1998.12770ead.023
[research_rayman_1979]: https://doi.org/10.21236/ada067833
[research_raymer_1992]: https://doi.org/10.2514/6.1992-4226
[research_raymer_1998]: https://doi.org/10.1016/s1369-8869(98)00005-6
[research_raymer_2012]: https://doi.org/10.2514/4.869112
[research_raymer_2012_b]: https://doi.org/10.2514/4.869211
[research_raymer_2018]: https://doi.org/10.2514/4.104909
[research_raymer_2024]: https://doi.org/10.2514/4.107290
[research_razzak_damodaran_2022]: https://doi.org/10.2514/6.2022-4018
[research_read_iii_1991]: https://doi.org/10.21236/ada236366
[research_real_time_kinematics_2015]: https://doi.org/10.1002/9781119018612.ch7
[research_reardon_katz_1999]: https://doi.org/10.21236/ada361526
[research_rebel_2000]: https://doi.org/10.21236/ada375712
[research_recktenwald_ahmed_2008]: https://doi.org/10.2514/6.2008-371
[research_recktenwald_crouse_2010]: https://doi.org/10.2514/1.46149
[research_recommended_practice]: https://doi.org/10.4271/air1380a
[research_redesigned_aircraft_1987]: https://doi.org/10.1016/0308-9126(87)90458-5
[research_redesigning_landing_2001]: https://doi.org/10.1108/aeat.2001.12773dab.008
[research_reed_2010]: https://doi.org/10.21236/ada525316
[research_regan_1986]: https://doi.org/10.21236/ada170418
[research_reichbach_sedwick_2001]: https://doi.org/10.2514/6.2001-3646
[research_reichenbach_2003]: https://doi.org/10.2514/6.2003-1883
[research_reichstein_schopferer_2022]: https://doi.org/10.1109/icuas54217.2022.9836194
[research_reid_1969]: https://doi.org/10.21236/ad0506146
[research_reid_1978]: https://doi.org/10.2514/3.58307
[research_reinbold_1954]: https://doi.org/10.21236/ad0045694
[research_reinhardt_johansen_2021]: https://doi.org/10.1109/icuas51884.2021.9476855
[research_reinhart_1975]: https://doi.org/10.21236/ada011588
[research_reitan_saib_1976]: https://doi.org/10.1145/1499799.1499894
[research_relative_navigation_1972]: https://doi.org/10.1017/s0373463300026710
[research_remiger_grois_2024]: https://doi.org/10.1115/gt2024-122647
[research_ren_du_2026]: https://doi.org/10.1016/j.ast.2025.111086
[research_ren_lyu_2023]: https://doi.org/10.1007/s10291-023-01420-w
[research_ren_man_2024]: https://doi.org/10.1109/yac63405.2024.10598702
[research_ren_quan_2024]: https://doi.org/10.1016/j.cja.2023.11.011
[research_ren_stephens_2006]: https://doi.org/10.2514/1.19028
[research_ren_wang_2025]: https://doi.org/10.1007/s11071-025-11899-2
[research_renehan_1997]: https://doi.org/10.21236/ada329050
[research_renga_grassi_2013]: https://doi.org/10.1155/2013/627509
[research_renga_tancredi_2009]: https://doi.org/10.1007/978-3-642-03501-2_44
[research_renga_tancredi_2015]: https://doi.org/10.1155/2015/570382
[research_reorganization_for_2008]: https://doi.org/10.5040/9798400608872.ch-009
[research_requirements_analysis_2013]: https://doi.org/10.1002/9781118519165.ch3
[research_resulkulyeva_serebryansky_2022]: https://doi.org/10.1109/mlsd55143.2022.9934439
[research_reubush_1979]: https://doi.org/10.2514/3.58532
[research_rezaifard_abbasi_2017]: https://doi.org/10.1109/iraniancee.2017.7985144
[research_rh_vp_2020]: https://doi.org/10.33564/ijeast.2020.v05i01.105
[research_rhoads_1967]: https://doi.org/10.21236/ad0820790
[research_rhudy_gross_2019]: https://doi.org/10.2514/6.2019-3111
[research_rhudy_gu_2014]: https://doi.org/10.2514/6.2014-0446
[research_riaz_2011]: https://doi.org/10.1260/1756-8293.3.1.25
[research_ribarich_1967]: https://doi.org/10.2514/6.1967-544
[research_riboldi_2019]: https://doi.org/10.1016/j.ast.2019.105507
[research_riccardi_mamino_2025]: https://doi.org/10.4050/sm_handling_2025-5298
[research_richards_tate_2023]: https://doi.org/10.2514/6.2023-3521
[research_richez_costello_2024]: https://doi.org/10.2514/6.2024-0056
[research_ridha_1968]: https://doi.org/10.2514/6.1968-328
[research_ridley_1982]: https://doi.org/10.1115/82-gt-254
[research_riedel_1979]: https://doi.org/10.21236/ada071395
[research_rieken_yasumuro_2004]: https://doi.org/10.2514/6.2004-6489
[research_rife_1993]: https://doi.org/10.21236/ada289069
[research_rife_2009]: https://doi.org/10.1002/j.2161-4296.2009.tb01761.x
[research_rife_khanafseh_2008]: https://doi.org/10.1109/jproc.2008.2006107
[research_rinkinen_1959]: https://doi.org/10.6028/nbs.rpt.6518
[research_riosquesada_charpentier]: https://doi.org/10.1109/elt.2004.1398127
[research_ritchey_2008]: https://doi.org/10.21236/ada484206
[research_ritter]: https://doi.org/10.17918/00006169
[research_rizzetta_visbal_2016]: https://doi.org/10.2514/6.2016-0322
[research_rldha_1969]: https://doi.org/10.2514/3.44045
[research_roadman_elston_2012]: https://doi.org/10.2514/1.c031655
[research_robertomati_2006]: https://doi.org/10.1109/med.2006.235988
[research_roberts_sutton_2006]: https://doi.org/10.1049/pbce069e_ch1
[research_robinson_1992]: https://doi.org/10.5670/oceanog.1992.31
[research_robinson_2004]: https://doi.org/10.21236/ada425641
[research_rocha_li_2006]: https://doi.org/10.2514/1.21934
[research_rodden_1972]: https://doi.org/10.2514/3.59062
[research_rodriguez_liscouethanke_2025]: https://doi.org/10.2514/1.c037723
[research_rodriguezramos_sampedro_2017]: https://doi.org/10.1109/icuas.2017.7991438
[research_rogers_2009]: https://doi.org/10.21236/ada540173
[research_rogers_cook_1952]: https://doi.org/10.21236/ad0013026
[research_rohl_schrage_1992]: https://doi.org/10.2514/6.1992-4721
[research_rojascarvajal_amitay_2023]: https://doi.org/10.2514/6.2023-0456
[research_rojascarvajal_amitay_2025]: https://doi.org/10.2514/1.j064152
[research_rojascarvajal_guha_2022]: https://doi.org/10.2514/6.2022-0470
[research_rollo_volf_2024]: https://doi.org/10.1007/978-3-031-62094-2_7
[research_rolls_royce_and_1999]: https://doi.org/10.1108/aeat.1999.12771aaf.006
[research_roltgen_gilbert_2010]: https://doi.org/10.1115/winvr2010-3753
[research_romero_2015]: https://doi.org/10.21236/ad1019455
[research_roof_bolter_2014]: https://doi.org/10.1007/978-3-642-41714-6_183347
[research_roof_bolting_2006]: https://doi.org/10.26616/nioshpub2006135
[research_rosales_reyes_2021]: https://doi.org/10.1109/icuas51884.2021.9476798
[research_rosamond_1961]: https://doi.org/10.2514/8.8932
[research_rose_ghoreyshi_2022]: https://doi.org/10.2514/6.2022-2755
[research_rosenman_hoekstra_1964]: https://doi.org/10.21236/ad0452444
[research_rosenstein_1989]: https://doi.org/10.4050/sm_rotary_1989-2147
[research_rosenthal_1970]: https://doi.org/10.21236/ad0705170
[research_rosenthal_walsh_1996]: https://doi.org/10.1287/opre.44.2.305
[research_rosin_mattos_2004]: https://doi.org/10.2514/6.2004-5191
[research_roskam_1985]: https://doi.org/10.2514/6.1985-4031
[research_roskam_1986]: https://doi.org/10.2514/6.1986-2636
[research_roskam_1988]: https://doi.org/10.2514/6.1988-4485
[research_ross_matarazzo_1982]: https://doi.org/10.4271/821467
[research_rothmaier_delperalrosado_2023]: https://doi.org/10.1109/plans53410.2023.10139988
[research_rothwell_2001]: https://doi.org/10.1016/s1369-8869(01)00004-0
[research_rotorcraft_application]: https://doi.org/10.4271/arp5632
[research_rotorcraft_handling_2011]: https://doi.org/10.1049/pbce074e_ch11
[research_rovig_bohnker_2004]: https://doi.org/10.7205/milmed.169.6.429
[research_roy_2009]: https://doi.org/10.21236/ada511003
[research_roy_ghosh_2010]: https://doi.org/10.21236/ada532004
[research_roy_levy_2006]: https://doi.org/10.2514/6.2006-6324
[research_rozov_volmering_2019]: https://doi.org/10.3390/aerospace6030030
[research_ruan_wei_2019]: https://doi.org/10.1007/s00190-019-01251-z
[research_rudowsky_hynes_2002]: https://doi.org/10.21236/ada411068
[research_rudy_2013]: https://doi.org/10.21236/ada590671
[research_ruetten_2018]: https://doi.org/10.2514/6.2018-3340
[research_ruff_narayanan_2002]: https://doi.org/10.1162/105474602760204264
[research_ruggiero_ito_2025]: https://doi.org/10.1016/j.actaastro.2025.04.026
[research_rui_2016]: https://doi.org/10.1109/icite.2016.7581325
[research_rui_zhou_2007]: https://doi.org/10.1109/chicc.2006.4346934
[research_ruili_dazhizeng_2013]: https://doi.org/10.1049/cp.2013.0521
[research_ruiqian_juan_2020]: https://doi.org/10.1109/iccasit50869.2020.9368540
[research_ruiyang_konstantin_2020]: https://doi.org/10.23919/icins43215.2020.9134026
[research_rumba_nikitenko_2020]: https://doi.org/10.1109/icuas48674.2020.9214031
[research_rupert_2008]: https://doi.org/10.2514/6.2008-7495
[research_ryan_1990]: https://doi.org/10.21236/ada228351
[research_ryan_banerjee_2014]: https://doi.org/10.1109/tcyb.2013.2271694
[research_ryan_cummings_2011]: https://doi.org/10.2514/6.2011-1516
[research_ryan_cummings_2016]: https://doi.org/10.1109/thms.2014.2376355
[research_rylko_favaro_2025]: https://doi.org/10.4050/sm_avtol_2025-5322
[research_rzucidlo_2006]: https://doi.org/10.3846/16487788.2006.9635935
[research_s_c_2025]: https://doi.org/10.1108/aeat-08-2024-0241
[research_sabatini_cappello_2015]: https://doi.org/10.1108/aeat-06-2014-0081
[research_sabatini_moore_2013]: https://doi.org/10.1017/s0373463313000143
[research_sacharny_henderson_2022]: https://doi.org/10.1007/978-3-030-98574-5
[research_sacharny_henderson_2022_b]: https://doi.org/10.1007/978-3-030-98574-5_2
[research_sachs_moeller_1995]: https://doi.org/10.2514/6.1995-3331
[research_sachse_1998]: https://doi.org/10.21236/ada344202
[research_sadasivan_gurubasavaraj_2001]: https://doi.org/10.14429/dsj.51.2238
[research_sadraey_2010]: https://doi.org/10.2514/6.2010-9302
[research_sadraey_2014]: https://doi.org/10.2514/6.2014-2718
[research_sadraey_2016]: https://doi.org/10.2514/6.2016-3710
[research_sadraey_2016_b]: https://doi.org/10.2514/6.2016-3448
[research_saeedipour_neilstevenson_1998]: https://doi.org/10.1016/s1369-8869(98)00004-4
[research_saelman_1964]: https://doi.org/10.2514/3.43599
[research_saetti_rogers_2020]: https://doi.org/10.4050/sm_2020_hq-916
[research_safeer_costello_2026]: https://doi.org/10.1109/icuas69441.2026.11598721
[research_safety_considerations]: https://doi.org/10.4271/arp1150
[research_safi_2023]: https://doi.org/10.32920/23581176.v1
[research_safvat_keighobadi_2025]: https://doi.org/10.1007/s10291-025-01880-2
[research_sagdeo_1990]: https://doi.org/10.2514/6.1990-3220
[research_saghafi_esmailifar_2009]: https://doi.org/10.1109/icas.2009.46
[research_saha_kumar_2023]: https://doi.org/10.1109/aero55745.2023.10115655
[research_saheby_jialu_2026]: https://doi.org/10.1016/j.ast.2025.111026
[research_sai_athreyam_2025]: https://doi.org/10.1109/etaav66793.2025.11213379
[research_saif_fantoni_2014]: https://doi.org/10.1109/icuas.2014.6842259
[research_sakamaki_beard_2017]: https://doi.org/10.1007/978-3-319-55372-6_12
[research_salt_1995]: https://doi.org/10.1117/12.212734
[research_saltzgaber_miller_2003]: https://doi.org/10.21236/ada415449
[research_samarehjamshida_sensmeiermarkd_2006]: https://ntrs.nasa.gov/citations/20060013435
[research_samuels_1982]: https://doi.org/10.2514/3.57418
[research_sanchezcarmona_cuernorejado_2018]: https://doi.org/10.1108/aeat-05-2017-0129
[research_sanchezlopez]: https://doi.org/10.20868/upm.thesis.46302
[research_sancho_2002]: https://doi.org/10.21236/ada400776
[research_sanders_1957]: https://doi.org/10.1108/eb032813
[research_sandy_1981]: https://doi.org/10.21236/ada104732
[research_sanghi_2003]: https://doi.org/10.1515/tjj.2003.20.1.83
[research_sanghi_cesnik_2024]: https://doi.org/10.2514/1.c037470
[research_sanghi_riso_2022]: https://doi.org/10.2514/6.2022-4093
[research_sankar_2012]: https://doi.org/10.2514/6.2012-4953
[research_santamariabarnadas]: https://doi.org/10.5821/dissertation-2117-93334
[research_santerre_geiger_2017]: https://doi.org/10.1007/s10291-017-0649-y
[research_santerre_geiger_2018]: https://doi.org/10.1007/s10291-018-0713-2
[research_santhoshkumarsa_suganthij_2015]: https://doi.org/10.17577/ijertv4is050739
[research_santoso_hariyanto_2022]: https://doi.org/10.28989/vortex.v3i2.1236
[research_sarigulklijn_sarigulklijn_2008]: https://doi.org/10.2514/6.2008-7835
[research_sarrafian_powers_1988]: https://doi.org/10.2514/3.20309
[research_sasiadek_wang_1999]: https://doi.org/10.2514/6.1999-4307
[research_sasiadek_wang_2000]: https://doi.org/10.1016/s1474-6670(17)37966-1
[research_saska_2015]: https://doi.org/10.1109/icuas.2015.7152376
[research_saska_chudoba_2014]: https://doi.org/10.1109/icuas.2014.6842301
[research_sasoh_imaizumi_2015]: https://doi.org/10.2514/1.j053540
[research_sastry_2001]: https://doi.org/10.21236/ada394091
[research_sathe_pant_2010]: https://doi.org/10.2514/6.2010-9306
[research_satkunanathan_murphy_1998]: https://doi.org/10.1007/pl00000023
[research_saucez]: https://doi.org/10.70675/f03a0681z9efcz414ez8944zcc71830d8acb
[research_saucez_boiffier_2012]: https://doi.org/10.2514/6.2012-4501
[research_sauter_matthews_2005]: https://doi.org/10.2514/6.2005-7046
[research_savic_2024]: https://doi.org/10.1109/icuas60882.2024.10556905
[research_savuran_karakaya_2015]: https://doi.org/10.7763/lnse.2015.v3.204
[research_savuran_karakaya_2015_b]: https://doi.org/10.1007/s00500-015-1970-4
[research_sayim_2018]: https://doi.org/10.5578/fmbd.66811
[research_scafetta_1983]: https://doi.org/10.2514/6.1983-1075
[research_scarpa_2001]: https://doi.org/10.1108/aeat.2001.12773dag.001
[research_schairer_1946]: https://doi.org/10.4271/460027
[research_schalk_2017]: https://doi.org/10.1109/icnsurv.2017.8012018
[research_schallhorn_2020]: https://doi.org/10.3357/amhp.5532.2020
[research_scheidt_2014]: https://doi.org/10.1007/978-90-481-9707-1_110
[research_scherer_yang_2015]: https://doi.org/10.1109/icuas.2015.7152401
[research_scherzinger_blakereid_1989]: https://doi.org/10.1007/978-3-642-74585-0_42
[research_schleicher_1966]: https://doi.org/10.21236/ad0629765
[research_schmidt_1983]: https://doi.org/10.2514/6.1983-2231
[research_schmidt_1984]: https://doi.org/10.21236/ada139132
[research_schmidt_1985]: https://doi.org/10.2514/3.19935
[research_schmidt_2015]: https://doi.org/10.4271/pt-169
[research_schmidt_2016]: https://doi.org/10.2514/6.2016-2099
[research_schmidt_2021]: https://doi.org/10.4271/9780768099430
[research_schmidt_setterlund_1994]: https://doi.org/10.1002/j.2161-4296.1994.tb02324.x
[research_schmidt_stevens_2006]: https://doi.org/10.2514/6.2006-6510
[research_schneider_1989]: https://doi.org/10.2514/6.1989-2116
[research_schneider_maida]: https://doi.org/10.1109/plans.1988.195513
[research_schoenbeck_schultz_1999]: https://doi.org/10.21236/ada375738
[research_schoenbein_2009]: https://doi.org/10.21236/ada539461
[research_schoenman_doniger_1965]: https://doi.org/10.4271/650571
[research_scholz_theuser_2026]: https://doi.org/10.1007/s13272-026-00958-y
[research_schopferer_benders_2020]: https://doi.org/10.2514/6.2020-0137
[research_schopferer_pfeifer_2015]: https://doi.org/10.1109/icuas.2015.7152406
[research_schrage_mckeithan_1989]: https://doi.org/10.4050/sm_rotary_1989-4104
[research_schuette_vormweg_2018]: https://doi.org/10.2514/6.2018-2841
[research_schultz_mcgrath_2009]: https://doi.org/10.2514/6.2009-6122
[research_schutz_kutrzyba_2000]: https://doi.org/10.21236/ada389329
[research_schwartz_1975]: https://doi.org/10.21236/adb008194
[research_schwartz_1988]: https://doi.org/10.21236/ada200453
[research_scognamiglio_caccavale_2024]: https://doi.org/10.1109/icuas60882.2024.10556996
[research_scott_hartmann_2024]: https://doi.org/10.4337/9781035312344.00007
[research_scott_trimarchi_2024]: https://doi.org/10.4324/9781003435501-13
[research_scribner_1998]: https://doi.org/10.21236/ada341712
[research_scukins_klein_2023]: https://doi.org/10.1109/icuas57906.2023.10156497
[research_seah_hwang_2006]: https://doi.org/10.2514/6.2006-6245
[research_seah_hwang_2007]: https://doi.org/10.2514/6.2007-6691
[research_seah_hwang_2009]: https://doi.org/10.2514/1.40127
[research_sease_warwick_2023]: https://doi.org/10.1007/978-3-031-45321-2_4
[research_seaton_1989]: https://doi.org/10.21236/ada218489
[research_seats_for]: https://doi.org/10.4271/as290a
[research_seats_for_b]: https://doi.org/10.4271/as290b
[research_sebestyen_szenasi_2026]: https://doi.org/10.1109/iccc68994.2026.11511574
[research_section_7_2016]: https://doi.org/10.4324/9781315514338-21
[research_see_ghosh_2017]: https://doi.org/10.1109/icuas.2017.7991478
[research_seiferth_kuchar_2017]: https://doi.org/10.1109/cdc.2017.8264238
[research_seitzer_2003]: https://doi.org/10.21236/ada421313
[research_selecting_the_2010]: https://doi.org/10.2514/5.9781600867538.0171.0194
[research_semakov_semakov_2020]: https://doi.org/10.1109/iccar49639.2020.9108026
[research_semke_2016]: https://doi.org/10.1201/9781315372044-14
[research_semke_2021]: https://doi.org/10.1201/9780429347498-15
[research_sensmeiermarkd_samarehjamshida_2005]: https://ntrs.nasa.gov/citations/20050175694
[research_sepulvedapalacios_smith_2019]: https://doi.org/10.1108/aeat-09-2018-0249
[research_seraj_martins_2022]: https://doi.org/10.2514/1.c036618
[research_serrano_serrano_2010]: https://doi.org/10.1109/plans.2010.5507310
[research_sevcik_oh]: https://doi.org/10.1007/978-1-4020-9137-7_17
[research_sevostyanov_devitt_2021]: https://doi.org/10.52348/2712-8873_mmtt_2021_7_83
[research_sevostyanov_devitt_2022]: https://doi.org/10.52261/02346206_2022_2_124
[research_sgarioto_williams_2006]: https://doi.org/10.21914/anziamj.v47i0.1041
[research_shaghaghian_karimaghaee_2018]: https://doi.org/10.1002/asjc.1931
[research_shaiju_sreeja_2022]: https://doi.org/10.1016/j.ifacol.2023.03.035
[research_shaikh_2025]: https://doi.org/10.2139/ssrn.5395070
[research_shane_1992]: https://doi.org/10.2514/6.1992-1038
[research_shanshan_ao_2020]: https://doi.org/10.1109/icus50048.2020.9274957
[research_shao_guo_2024]: https://doi.org/10.2139/ssrn.5041226
[research_shao_li_2023]: https://doi.org/10.3390/aerospace10121005
[research_shao_li_2026]: https://doi.org/10.2514/1.c038254
[research_sharma_hablani_2014]: https://doi.org/10.3182/20140313-3-in-3024.00224
[research_sharma_padthe_2021]: https://doi.org/10.2514/1.c035973
[research_sharma_saunders_2009]: https://doi.org/10.2514/6.2009-6180
[research_shaw_1960]: https://doi.org/10.1017/s0368393100072655
[research_shaw_clark_1988]: https://doi.org/10.2514/3.45555
[research_shaw_smith_1977]: https://doi.org/10.21236/ada041263
[research_shay_swieringa_2012]: https://doi.org/10.2514/6.2012-5615
[research_shayan_vankampen_2021]: https://doi.org/10.2514/6.2021-0884
[research_shayler_1961]: https://doi.org/10.1049/jbire.1961.0004
[research_shen_hao_2016]: https://doi.org/10.1109/chicc.2016.7554220
[research_shen_lifey_2019]: https://doi.org/10.36652/0869-4931-2019-73-4
[research_shen_rahman_2011]: https://doi.org/10.2514/6.2011-1465
[research_shen_zhang_2026]: https://doi.org/10.1016/j.oceaneng.2026.125162
[research_sheppard_foster_2008]: https://doi.org/10.1002/pfi.193
[research_sher_1981]: https://doi.org/10.21236/ada101951
[research_sherstjuk_2015]: https://doi.org/10.1109/apuavd.2015.7346620
[research_shi_2023]: https://doi.org/10.1109/icuas57906.2023.10156460
[research_shi_gao_2013]: https://doi.org/10.1007/s10291-013-0348-2
[research_shi_ng_2018]: https://doi.org/10.1109/icuas.2018.8453346
[research_shi_wu_2022]: https://doi.org/10.1016/j.procs.2022.10.049
[research_shimski_schmidt_2013]: https://doi.org/10.21236/ada618781
[research_shin_you_2013]: https://doi.org/10.1109/icuas.2013.6564759
[research_shin_you_2013_b]: https://doi.org/10.1007/s10846-013-9927-2
[research_shipman_arunajatesan_2008]: https://doi.org/10.2514/6.2008-6227
[research_shirley_schetz_2014]: https://doi.org/10.2514/1.c032605
[research_shiyan_huimin_2016]: https://doi.org/10.1109/ccdc.2016.7532141
[research_shock_mounts_1993]: https://doi.org/10.1016/0261-3069(93)90094-c
[research_shoop_munoz_2023]: https://doi.org/10.1007/s40295-023-00369-9
[research_shoop_munoz_2024]: https://doi.org/10.1007/978-3-031-51928-4_1
[research_shriwastav_song_2020]: https://doi.org/10.1109/icuas48674.2020.9213833
[research_shu_sun_2013]: https://doi.org/10.2514/6.2013-5158
[research_shuang_zhang_2016]: https://doi.org/10.1109/cgncc.2016.7828825
[research_shuang_zhang_2017]: https://doi.org/10.2514/6.2017-1253
[research_shubert_jones_2025]: https://doi.org/10.4050/sm_handling_2025-5291
[research_shujun_jianyun_2014]: https://doi.org/10.1109/eml.2014.6920638
[research_shustrov_1998]: https://doi.org/10.1016/s1369-8869(98)00016-0
[research_shweyk_hyde_2013]: https://doi.org/10.2514/6.2013-1101
[research_si_song_2024]: https://doi.org/10.21203/rs.3.rs-3893642/v1
[research_sibruk_bondarenko_2015]: https://doi.org/10.1109/apuavd.2015.7346602
[research_siddarth_valasek_2011]: https://doi.org/10.1007/978-3-642-19817-5_19
[research_siegel_1995]: https://doi.org/10.21236/ada593358
[research_siegel_crain_1960]: https://doi.org/10.21236/ad0245849
[research_siegel_lanterman_1963]: https://doi.org/10.21236/ad0298331
[research_silva]: https://doi.org/10.11606/t.55.2018.tde-16102018-100220
[research_silva_b]: https://doi.org/10.14393/ufu.di.2019.26
[research_silva_guimaraes_2020]: https://doi.org/10.2514/6.2020-1503
[research_silva_lundbladh_2024]: https://doi.org/10.2514/1.c037653
[research_sim_murray_1994]: https://doi.org/10.2514/3.46617
[research_simmons_1993]: https://doi.org/10.21236/ada289000
[research_simms_2023]: https://doi.org/10.32920/ryerson.14662974.v1
[research_simon_chudoba_2021]: https://doi.org/10.2514/6.2021-4121
[research_simoncic_2013]: https://doi.org/10.21236/ada580613
[research_simonetti_crespillo_2024]: https://doi.org/10.33012/navi.637
[research_simos_jenkinson_1986]: https://doi.org/10.2514/6.1986-2696
[research_simplicio_navarrotapia_2018]: https://doi.org/10.1016/j.ifacol.2018.11.095
[research_simpson_rawashdeh_2005]: https://doi.org/10.1109/aero.2005.1559753
[research_singer_2011]: https://doi.org/10.21236/ada546157
[research_singh_1974]: https://doi.org/10.21236/ad0782965
[research_singh_toropov_2016]: https://doi.org/10.2514/6.2016-3364
[research_sinha_arunajatesan_2001]: https://doi.org/10.2514/6.2001-2125
[research_sirigireddy_ahner_2026]: https://doi.org/10.2139/ssrn.6662520
[research_sivakumar_hasrizamcheman_2022]: https://doi.org/10.1109/icuas54217.2022.9836157
[research_sivakumar_man_2021]: https://doi.org/10.1109/icuas51884.2021.9476872
[research_sivaramakrishnan_1981]: https://doi.org/10.2514/3.57591
[research_sizing_from_2024]: https://doi.org/10.2514/5.9781624107290.0029.0054
[research_sizing_the_2002]: https://doi.org/10.2514/5.9781600861444.0189.0230
[research_sizing_the_2018]: https://doi.org/10.2514/5.9781624105173.0221.0272
[research_sizing_trade_2024]: https://doi.org/10.2514/5.9781624107290.0745.0770
[research_sjoberg_1998]: https://doi.org/10.1179/003962698791484301
[research_skillen_crossley_2005]: https://doi.org/10.2514/6.2005-1960
[research_skillen_crossley_2008]: https://doi.org/10.2514/6.2008-166
[research_skjong_nundal_2015]: https://doi.org/10.1109/icuas.2015.7152377
[research_skorobogatov_buturov_2026]: https://doi.org/10.26467/2079-0619-2026-29-3-48-58
[research_slapnicar]: https://doi.org/10.14264/69b8f75
[research_slegers_beyer_2008]: https://doi.org/10.2514/1.32099
[research_smith]: https://doi.org/10.5204/thesis.eprints.246280
[research_smith_1967]: https://doi.org/10.21236/ad0816142
[research_smith_1968]: https://doi.org/10.21236/ad0684315
[research_smith_2000]: https://doi.org/10.2514/6.2000-4174
[research_smith_2023]: https://doi.org/10.4050/sm_2023_hq-1192
[research_smith_andersen_2026]: https://doi.org/10.1109/icuas69441.2026.11598658
[research_smith_chow_1998]: https://doi.org/10.2514/6.1998-2228
[research_smith_meyer_1981]: https://doi.org/10.2514/6.1981-2238
[research_snyder_1950]: https://doi.org/10.21236/ad0109766
[research_snyder_1990]: https://doi.org/10.2514/6.1990-3209
[research_snyder_2000]: https://doi.org/10.21236/ada388710
[research_snyder_sanders_2009]: https://doi.org/10.2514/1.34685
[research_snyder_schipper]: https://doi.org/10.1109/plans.1992.185863
[research_snyder_schipper_1992]: https://doi.org/10.1109/62.257086
[research_so_2016]: https://doi.org/10.11003/jpnt.2016.5.4.165
[research_soban_1993]: https://doi.org/10.2514/6.1993-3993
[research_soemaryanto_rosid_2018]: https://doi.org/10.30536/j.jtd.2017.v15.a2747
[research_solies_1995]: https://doi.org/10.2514/6.1995-3912
[research_soloviev_venable_2010]: https://doi.org/10.1109/plans.2010.5507322
[research_solvey_1951]: https://doi.org/10.1108/eb032033
[research_song_2008]: https://doi.org/10.21236/ada477568
[research_song_ai_2021]: https://doi.org/10.1016/j.ast.2021.106528
[research_song_chen_2020]: https://doi.org/10.1016/j.isatra.2020.05.049
[research_song_ma_2020]: https://doi.org/10.1109/cacre50138.2020.9230178
[research_song_yang_2014]: https://doi.org/10.1016/j.cja.2014.08.003
[research_song_zhang_2019]: https://doi.org/10.1109/dasc43569.2019.9081785
[research_soni_hablani_2015]: https://doi.org/10.1109/rdcape.2015.7281368
[research_soop_1994]: https://doi.org/10.1007/978-94-015-8352-7_7
[research_soop_1994_b]: https://doi.org/10.1007/978-94-015-8352-7_6
[research_sorensen_johansen_2017]: https://doi.org/10.1109/icuas.2017.7991301
[research_sosa_1997]: https://doi.org/10.21236/ada326936
[research_souanef_2024]: https://doi.org/10.1061/jaeeez.aseng-4427
[research_soumekh]: https://doi.org/10.1109/icip.1995.529056
[research_souza_monico_2004]: https://doi.org/10.1007/s10291-004-0100-z
[research_speakman_powell_1978]: https://doi.org/10.21236/ada053701
[research_special_topics_2014]: https://doi.org/10.2514/5.9781624102615.0799.0814
[research_specification_for]: https://doi.org/10.1520/f2585-06
[research_specification_for_b]: https://doi.org/10.1520/f2908-23
[research_specification_for_c]: https://doi.org/10.1520/f2908-14
[research_specification_for_d]: https://doi.org/10.1520/f3322-24
[research_specification_for_e]: https://doi.org/10.3403/00248001u
[research_specification_for_f]: https://doi.org/10.1520/f2317_f2317m
[research_sperling_kewley_2008]: https://doi.org/10.21236/ada488967
[research_speth_kamann_2016]: https://doi.org/10.1109/wpnc.2016.7822852
[research_spiridon_fuiorea_2025]: https://doi.org/10.13111/2066-8201.2025.17.4.18
[research_spreen_2019]: https://doi.org/10.4324/9780429299452-8
[research_spreen_2019_b]: https://doi.org/10.4324/9780429299452-10
[research_spreen_2019_c]: https://doi.org/10.4324/9780429299452-9
[research_spreen_2019_d]: https://doi.org/10.4324/9780429299452-7
[research_spreen_2019_e]: https://doi.org/10.4324/9780429299452-11
[research_spreen_2019_f]: https://doi.org/10.4324/9780429299452-12
[research_spreen_2019_g]: https://doi.org/10.4324/9780429299452-13
[research_spreen_2019_h]: https://doi.org/10.4324/9780429299452-2
[research_spreen_2019_i]: https://doi.org/10.4324/9780429299452-14
[research_spreen_2019_j]: https://doi.org/10.4324/9780429299452
[research_spreen_2019_k]: https://doi.org/10.4324/9780429299452-15
[research_spreen_2019_l]: https://doi.org/10.4324/9780429299452-3
[research_spreen_2019_m]: https://doi.org/10.4324/9780429299452-5
[research_spreen_2019_n]: https://doi.org/10.4324/9780429299452-4
[research_spreen_2023]: https://doi.org/10.4324/9781003457633-5
[research_spry_girard]: https://doi.org/10.1109/acc.2005.1470519
[research_squire_trafton_2006]: https://doi.org/10.1145/1121241.1121248
[research_srinathkumar_2011]: https://doi.org/10.1049/pbce074e
[research_srinuandee]: https://doi.org/10.58837/chula.the.2015.1401
[research_staack]: https://doi.org/10.3384/diss.diva-132614
[research_staats_troeltsch_2025]: https://doi.org/10.3390/aerospace12121085
[research_stability_control_2024]: https://doi.org/10.2514/5.9781624107290.0619.0672
[research_stachiw]: https://doi.org/10.22215/etd/2020-14047
[research_stachiw_khouli_2020]: https://doi.org/10.2514/6.2020-1681
[research_stachiw_khouli_2021]: https://doi.org/10.2514/1.c035921
[research_staelens_blackwelder_2007]: https://doi.org/10.2514/6.2007-68
[research_stalford_1979]: https://doi.org/10.21236/ada080025
[research_stamm_woods_2024]: https://doi.org/10.2514/6.2024-2641
[research_standard_guide]: https://doi.org/10.1520/f3199-16
[research_standard_practice]: https://doi.org/10.1520/f3478
[research_standard_specification]: https://doi.org/10.1520/f3835
[research_standard_specification_b]: https://doi.org/10.1520/f3838
[research_standard_specification_c]: https://doi.org/10.1520/f3322
[research_standard_terminology]: https://doi.org/10.1520/f3341_f3341m
[research_stanek_2002]: https://doi.org/10.1121/1.1492934
[research_stanek_2003]: https://doi.org/10.1121/1.1572348
[research_stanek_2007]: https://doi.org/10.1121/1.2822955
[research_stanford_kurdi_2012]: https://doi.org/10.2514/1.c031094
[research_stark_chen_2014]: https://doi.org/10.1109/icuas.2014.6842243
[research_stastny_stoica_2021]: https://doi.org/10.13111/2066-8201.2021.13.4.18
[research_station_keeping_1962]: https://doi.org/10.2514/5.9781600864827.0057.0087
[research_station_keeping_2008]: https://doi.org/10.1515/9781846156373-009
[research_station_keeping_2022]: https://doi.org/10.1007/978-981-10-6946-8_300764
[research_stechman_1984]: https://doi.org/10.2514/6.1984-1231
[research_stedman_1992]: https://doi.org/10.21236/ada526309
[research_steeb_chu_1979]: https://doi.org/10.21236/ada077917
[research_stegall_2001]: https://doi.org/10.21236/ada390246
[research_steinberg]: https://doi.org/10.1109/fuzzy.1993.327544
[research_steinberg_1992]: https://doi.org/10.2514/6.1992-4392
[research_steinberg_page_2001]: https://doi.org/10.21236/ada390355
[research_stemler_craig_1976]: https://doi.org/10.21236/ada028290
[research_stenfelt_ringertz_2009]: https://doi.org/10.2514/1.41092
[research_stenfelt_ringertz_2010]: https://doi.org/10.2514/1.c031017
[research_stepanova_2025]: https://doi.org/10.7868/s3034498025050034
[research_stephan_pfeifle_2020]: https://doi.org/10.2514/1.g005240
[research_stewart_roberts_2012]: https://doi.org/10.21236/ada563620
[research_stieger_1929]: https://doi.org/10.1108/eb029158
[research_stoltz_1995]: https://doi.org/10.1007/pl00022497
[research_stolz_hein_1989]: https://doi.org/10.1080/00050326.1989.10438601
[research_stone]: https://doi.org/10.1007/1-84628-179-2_7
[research_storage_handling]: https://doi.org/10.4271/arp6951
[research_strattan_1978]: https://doi.org/10.21236/ada052447
[research_stratton_1995]: https://doi.org/10.2514/6.1995-3194
[research_strawser_2013]: https://doi.org/10.1093/acprof:oso/9780199926121.003.0001
[research_streamline_development_2009]: https://doi.org/10.1108/aeat.2009.12781fad.012
[research_strganac_2007]: https://doi.org/10.21236/ada475354
[research_striebich_1986]: https://doi.org/10.21236/adb100948
[research_strietzel_shefler_1963]: https://doi.org/10.21236/ad0426766
[research_stringer_bunner]: https://doi.org/10.18260/1-2--29760
[research_strock_1983]: https://doi.org/10.2514/6.1983-2759
[research_stroub_1989]: https://doi.org/10.4050/sm_rotary_1989-4099
[research_structural_dynamics_1999]: https://doi.org/10.1108/aeat.1999.12771aab.011
[research_structure_with_1974]: https://doi.org/10.1108/eb035126
[research_strukov_2025]: https://doi.org/10.62717/2221-4550-2025-1-036
[research_sturza_1983]: https://doi.org/10.1002/j.2161-4296.1983.tb00831.x
[research_su_han_2018]: https://doi.org/10.1155/2018/6932985
[research_su_han_2018_b]: https://doi.org/10.1109/access.2018.2879503
[research_su_li_2018]: https://doi.org/10.1088/1757-899x/381/1/012194
[research_su_li_2019]: https://doi.org/10.1109/ccdc.2019.8832824
[research_su_schon_2021]: https://doi.org/10.33012/2021.18078
[research_su_schon_2023]: https://doi.org/10.1109/plans53410.2023.10139987
[research_su_wu_2018]: https://doi.org/10.20944/preprints201804.0201.v1
[research_su_xu_2013]: https://doi.org/10.1007/978-3-642-37404-3_23
[research_suarez_kramer_1992]: https://doi.org/10.2514/6.1992-2716
[research_subbarao_steinberg_2001]: https://doi.org/10.2514/6.2001-4019
[research_subrahmanyam_1994]: https://doi.org/10.2514/3.21177
[research_subrahmanyam_1995]: https://doi.org/10.1007/978-1-4612-4272-7_6
[research_subramani_m_2021]: https://doi.org/10.1108/aeat-04-2021-0115
[research_subramaniam_joseph_2012]: https://doi.org/10.2514/6.2012-1039
[research_subrata_2017]: https://doi.org/10.26555/jiteki.v2i2.4896
[research_sugargabor_koreanschi_2016]: https://doi.org/10.1016/j.ast.2016.03.014
[research_suggett_1960]: https://doi.org/10.1017/s0368393100073910
[research_sugimoto_2006]: https://doi.org/10.2493/jjspe.72.285
[research_sui_2022]: https://doi.org/10.22541/au.165416416.64807284/v1
[research_suima_2025]: https://doi.org/10.62717/2221-4550-2025-1-100
[research_sullings_waller_1967]: https://doi.org/10.2514/6.1967-757
[research_sullivan_1991]: https://doi.org/10.21236/ada243486
[research_sullivan_1991_b]: https://doi.org/10.21236/ada242085
[research_sullivan_1991_c]: https://doi.org/10.21236/ada242554
[research_sullivan_1997]: https://doi.org/10.21236/ada350630
[research_suminsby_2002]: https://doi.org/10.21236/ada420687
[research_summey_rodriguez_2001]: https://doi.org/10.21236/ada390575
[research_sun_2023]: https://doi.org/10.54254/2755-2721/9/20230080
[research_sun_2026]: https://doi.org/10.1088/1742-6596/3207/1/012035
[research_sun_deng_2019]: https://doi.org/10.1016/j.ast.2019.05.005
[research_sun_duan_2025]: https://doi.org/10.1016/j.ast.2025.110067
[research_sun_fu_2018]: https://doi.org/10.33012/2018.15846
[research_sun_gebreegziabher_2021]: https://doi.org/10.1002/navi.440
[research_sun_guo_2025]: https://doi.org/10.1049/icp.2025.3445
[research_sun_liu_2025]: https://doi.org/10.23919/ccc64809.2025.11178625
[research_sun_pack_2016]: https://doi.org/10.1109/icuas.2016.7502611
[research_sun_tang_2011]: https://doi.org/10.1109/icma.2011.5986361
[research_sun_wang_2026]: https://doi.org/10.1109/icst69053.2026.00019
[research_sun_zhang_2005]: https://doi.org/10.2514/6.2005-4602
[research_sun_zhang_2022]: https://doi.org/10.1109/icus55513.2022.9986607
[research_sun_zhang_2022_b]: https://doi.org/10.3390/su141811230
[research_sun_zhang_2026]: https://doi.org/10.1007/s42401-026-00459-0
[research_sun_zhou_2024]: https://doi.org/10.1016/j.isatra.2023.10.024
[research_suozhongyuan_yidongyang]: https://doi.org/10.1109/wcica.2000.863180
[research_supplementary_bibliography_1990]: https://doi.org/10.1515/9781400855988.769
[research_supriyono_akhara_2021]: https://doi.org/10.1088/1742-6596/1858/1/012074
[research_suresh_radhakrishnan_2013]: https://doi.org/10.1016/j.ast.2011.10.012
[research_suresh_sura_2019]: https://doi.org/10.4271/01-12-01-0001
[research_surgeoner_1999]: https://doi.org/10.21236/ada398896
[research_surono_ashar_2021]: https://doi.org/10.54317/kom.v2ioktober.181
[research_survivability_of_2016]: https://doi.org/10.1201/9781315371191-13
[research_sutrakar_kumari_2025]: https://doi.org/10.21203/rs.3.rs-8289189/v1
[research_sutton_2005]: https://doi.org/10.21236/ada432367
[research_sutton_2006]: https://doi.org/10.21236/ada449249
[research_suzuki_yonezawa_1993]: https://doi.org/10.2514/3.48276
[research_svendsen_obrien_2013]: https://doi.org/10.1002/navi.26
[research_svoboda_1999]: https://doi.org/10.1016/s1369-8869(99)00019-1
[research_svoboda_2000]: https://doi.org/10.1016/s1369-8869(99)00021-x
[research_swaim_1969]: https://doi.org/10.2514/3.44031
[research_swanson]: https://doi.org/10.1109/plans.1998.670210
[research_swanson_isaac_2010]: https://doi.org/10.2514/1.45921
[research_swett_blanche]: https://doi.org/10.1109/elt.2004.1398142
[research_swisdak_michaelm_1992]: https://doi.org/10.21236/ada517651
[research_sychev_2017]: https://doi.org/10.3103/s1068799817020052
[research_sydspeng_2001]: https://doi.org/10.2172/819897
[research_sydspeng_2002]: https://doi.org/10.2172/819906
[research_sydspeng_2002_b]: https://doi.org/10.2172/819908
[research_sydspeng_2003]: https://doi.org/10.2172/825234
[research_sydspeng_2004]: https://doi.org/10.2172/893088
[research_sydspeng_2005]: https://doi.org/10.2172/837258
[research_sylvester_1980]: https://doi.org/10.2514/6.1980-1827
[research_synthetic_vision_1994]: https://doi.org/10.2514/6.1994-3674
[research_szabolcsi_2018]: https://doi.org/10.19062/1842-9238.2018.16.3.6
[research_szabolcsi_2018_b]: https://doi.org/10.19062/1842-9238.2018.16.1.5
[research_szabolcsi_2018_c]: https://doi.org/10.19062/1842-9238.2018.16.1.7
[research_tacticalaircommandlangleyafbva_1989]: https://doi.org/10.21236/ada271137
[research_tafanidis_banerjee_2025]: https://doi.org/10.1016/j.asr.2025.04.082
[research_taflan_smith_2026]: https://doi.org/10.2514/1.c038402
[research_taghizadeh_safabakhsh_2023]: https://doi.org/10.1017/s0373463322000583
[research_tait_hatfield_2009]: https://doi.org/10.1109/isemc.2009.5284712
[research_takahashi_2022]: https://doi.org/10.2514/6.2022-3655
[research_takita_kashitani_2016]: https://doi.org/10.1299/jsmedmc.2016.431
[research_takita_kashitani_2017]: https://doi.org/10.1299/jsmemovic.2017.15.a13
[research_tal_karaman_2021]: https://doi.org/10.2514/6.2021-3214
[research_talbot_1991]: https://doi.org/10.1007/bf03655416
[research_tam_2015]: https://doi.org/10.21236/ada625485
[research_tan_wang_2015]: https://doi.org/10.1017/s037346331500003x
[research_tan_wang_2019]: https://doi.org/10.1109/icuas.2019.8798078
[research_tan_zhou_2014]: https://doi.org/10.4028/www.scientific.net/amr.940.419
[research_tanaka_matsumoto_2019]: https://doi.org/10.1109/gcce46687.2019.9015373
[research_tancredi_renga_2010]: https://doi.org/10.2514/6.2010-8189
[research_tancredi_renga_2012]: https://doi.org/10.2514/6.2012-4707
[research_tancredi_renga_2013]: https://doi.org/10.1016/j.actaastro.2013.01.005
[research_tancredi_renga_2014]: https://doi.org/10.1016/j.actaastro.2013.07.029
[research_tandale_bowers_2005]: https://doi.org/10.2514/6.2005-5868
[research_tandale_bowers_2006]: https://doi.org/10.2514/1.19694
[research_tang]: https://doi.org/10.70675/f90d5cf8z75e6z4b6fzbc4bz8589cda08298
[research_tang_dowell_2008]: https://doi.org/10.2514/1.32754
[research_tang_lai_2020]: https://doi.org/10.1109/icuas48674.2020.9213987
[research_tang_shen_2018]: https://doi.org/10.1007/s10291-018-0737-7
[research_tang_zeng_2024]: https://doi.org/10.1145/3675417.3675504
[research_tangadrianj_2013]: https://ntrs.nasa.gov/citations/20140002265
[research_tangthong_aktimagool_2021]: https://doi.org/10.1109/ieecon51072.2021.9440230
[research_tanil_khanafseh_2016]: https://doi.org/10.1109/plans.2016.7479805
[research_tao_chen_2022]: https://doi.org/10.1007/s10291-022-01287-3
[research_tate_2001]: https://doi.org/10.21236/ada395716
[research_tatiyaworanun_purivigraipong_2013]: https://doi.org/10.1109/ecticon.2013.6559507
[research_taylor_1999]: https://doi.org/10.21236/ada374953
[research_taylor_boubin_2021]: https://doi.org/10.1109/icuas51884.2021.9476844
[research_tdavies_1974]: https://doi.org/10.1109/cdc.1974.270418
[research_teague_kewley_2008]: https://doi.org/10.21236/ada488664
[research_technical_requirements]: https://doi.org/10.3403/30408085u
[research_technology_news_2007]: https://doi.org/10.26616/nioshpub2007119
[research_technology_news_2017]: https://doi.org/10.26616/nioshpub2017208
[research_technology_news_2017_b]: https://doi.org/10.26616/nioshpub2018100
[research_teel_1999]: https://doi.org/10.21236/ada367415
[research_teel_1999_b]: https://doi.org/10.21236/ada367012
[research_tekinalp_cavus_2012]: https://doi.org/10.2514/6.2012-5532
[research_tekinalp_prach_2013]: https://doi.org/10.2514/6.2013-5167
[research_tekinalp_prach_2014]: https://doi.org/10.2514/6.2014-1302
[research_teledyneryanaeronauticalsandiegoca_1974]: https://doi.org/10.21236/ad0783935
[research_templalexis_lekas_2016]: https://doi.org/10.1115/gt2016-56225
[research_templeman_parker_1968]: https://doi.org/10.2514/3.43940
[research_teng_yu_2023]: https://doi.org/10.2514/6.2023-4547
[research_tenhave_1993]: https://doi.org/10.1017/s0373463300011863
[research_teofilatto_2001]: https://doi.org/10.1016/s1369-8869(00)00025-2
[research_teper_stapleford_1965]: https://doi.org/10.2514/6.1965-1237
[research_teper_stapleford_1966]: https://doi.org/10.2514/3.43725
[research_terheyden_zickwolff_1986]: https://doi.org/10.1007/978-3-662-21924-9_4
[research_terminology_for]: https://doi.org/10.1520/f2395-05
[research_terrain_relative_2025]: https://doi.org/10.1002/9781394267743.ch10
[research_terry_1965]: https://doi.org/10.21236/ad0478321
[research_terwilliger_ison_2014]: https://doi.org/10.1139/juvs-2013-0020
[research_test_methods]: https://doi.org/10.3403/30412888u
[research_tests_impact]: https://doi.org/10.4271/as6053a
[research_teunissen]: https://doi.org/10.1007/bfb0117685
[research_teunissen_1995]: https://doi.org/10.1007/bf00863419
[research_teunissen_1998]: https://doi.org/10.1007/978-3-642-72011-6_8
[research_teunissen_2000]: https://doi.org/10.2514/6.2000-1223
[research_teunissen_2003]: https://doi.org/10.5081/jgps.2.1.1
[research_teunissen_2003_b]: https://doi.org/10.1007/bf02899809
[research_teunissen_2017]: https://doi.org/10.1007/978-3-319-42928-1_23
[research_teunissen_2026]: https://doi.org/10.3390/app16094089
[research_teunissen_b]: https://doi.org/10.1109/ssp.2001.955208
[research_teunissen_joosten_1999]: https://doi.org/10.1007/pl00012758
[research_teunissen_odijk_2003]: https://doi.org/10.1007/s00190-002-0285-2
[research_teunissen_verhagen]: https://doi.org/10.1007/978-3-540-85426-5_90
[research_thakur_kumar_2021]: https://doi.org/10.14429/dsj.71.15648
[research_the_algorithm_2020]: https://doi.org/10.36652/0869-4931-2020-74-2-78-84
[research_the_block_2002]: https://doi.org/10.5139/jksas.2002.30.8.078
[research_the_catapult]: https://doi.org/10.1007/978-1-4302-0258-5_4
[research_the_control_2026]: https://doi.org/10.1016/c2024-0-02916-5
[research_the_culture]: https://doi.org/10.1057/9781137321350.0010
[research_the_design_2012]: https://doi.org/10.2514/5.9781600869228.0221.0337
[research_the_ethics_2016]: https://doi.org/10.4324/9781315613246-25
[research_the_future_2016]: https://doi.org/10.1201/b11202-17
[research_the_kinematics_2015]: https://doi.org/10.1002/9781119174882.ch1
[research_the_origins_2018]: https://doi.org/10.7551/mitpress/11012.003.0004
[research_the_process]: https://doi.org/10.4271/arp698
[research_the_red]: https://doi.org/10.2307/j.ctt6wr9wj.73
[research_the_resampled_2011]: https://doi.org/10.1115/1.859902.paper116
[research_the_u_s_1998]: https://doi.org/10.7249/mr948
[research_the_use_2006]: https://doi.org/10.1002/0470035668.ch7
[research_the_wave]: https://doi.org/10.2307/j.ctt207g7kz.13
[research_the_wing_2013]: https://doi.org/10.1002/9781118568101.ch11
[research_theiss_2007]: https://doi.org/10.22488/okstate.18.100498
[research_thelander_1965]: https://doi.org/10.21236/ad0617354
[research_theorem_s_cadverter_2003]: https://doi.org/10.1108/aeat.2003.12775dab.007
[research_theunissen_koeners_2005]: https://doi.org/10.2514/6.2005-6441
[research_thiele_1965]: https://doi.org/10.21236/ad0467888
[research_thomas_1961]: https://doi.org/10.21236/ad0400231
[research_thome_jr_2003]: https://doi.org/10.21236/ada414557
[research_thompson_1965]: https://doi.org/10.2514/6.1965-1209
[research_thompson_robertson_1990]: https://doi.org/10.2514/6.1990-3245
[research_thorne_yim_2011]: https://doi.org/10.1007/978-94-007-3033-5_29
[research_thota_krauskopf_2008]: https://doi.org/10.1007/s11071-008-9455-y
[research_thrust_to_weight_ratio_2024]: https://doi.org/10.2514/5.9781624107290.0119.0150
[research_thukral_innocenti_1992]: https://doi.org/10.2514/3.20987
[research_thys_macabiau_2025]: https://doi.org/10.33012/2025.20380
[research_tian_ge_2016]: https://doi.org/10.1007/s10291-016-0584-3
[research_tian_gong_2025]: https://doi.org/10.1007/s10291-025-01974-x
[research_tian_sun_2026]: https://doi.org/10.3390/a19020158
[research_tian_zhao_2012]: https://doi.org/10.1109/rams.2012.6175503
[research_tianjian_xin_2014]: https://doi.org/10.1109/ccdc.2014.6852801
[research_tianyuan_xiongqing_2009]: https://doi.org/10.1016/s1000-9361(08)60114-4
[research_tiberius_pany_2002]: https://doi.org/10.1007/s10291-002-0022-6
[research_tielking_1989]: https://doi.org/10.21236/ada279100
[research_tierney_rodenbeck_2019]: https://doi.org/10.1109/rws.2019.8714287
[research_tiimus_murumae_2015]: https://doi.org/10.4028/www.scientific.net/ssp.220-221.928
[research_tin_borowczyk_2020]: https://doi.org/10.1109/icuas48674.2020.9213839
[research_tingting_aijun_2014]: https://doi.org/10.1109/icarcv.2014.7064295
[research_tinoco]: https://doi.org/10.14393/ufu.te.2024.575
[research_tire_pressure]: https://doi.org/10.4271/arp6137
[research_tiwari_stacey_2020]: https://doi.org/10.33012/2020.17209
[research_toffol_ricci_2023]: https://doi.org/10.1016/j.compstruct.2022.116557
[research_tokarick_2005]: https://doi.org/10.21236/ada463720
[research_tolfa_edward_1971]: https://doi.org/10.21236/ad0529249
[research_tomac_rizzi_2012]: https://doi.org/10.2514/1.c031384
[research_tomac_stenfelt_2014]: https://doi.org/10.1016/j.ast.2014.09.007
[research_tomczyk_rogalski_2005]: https://doi.org/10.2514/6.2005-6965
[research_tonhauser_hecker_2016]: https://doi.org/10.1109/inertialsensors.2016.7745677
[research_torelli_stroosma_2023]: https://doi.org/10.2514/6.2023-0907
[research_torenbeek_1971]: https://doi.org/10.1108/eb034787
[research_torenbeek_1972]: https://doi.org/10.1108/eb034867
[research_torenbeek_2000]: https://doi.org/10.1016/s1369-8869(00)00022-7
[research_torenbeek_2013]: https://doi.org/10.1002/9781118568101
[research_torenbeek_2020]: https://doi.org/10.1002/9781119667063
[research_torno_hintz_2014]: https://doi.org/10.1109/icuas.2014.6842353
[research_torres_harris_2023]: https://doi.org/10.1007/978-3-031-21893-4_12
[research_torvold_2000]: https://doi.org/10.21236/ada379321
[research_tosun_2023]: https://doi.org/10.1007/978-3-031-29933-9_20
[research_toth_jozkow_2017]: https://doi.org/10.1061/(asce)su.1943-5428.0000231
[research_traas_atmaca_2026]: https://doi.org/10.2514/6.2026-0549
[research_trade_studies_2010]: https://doi.org/10.2514/5.9781600867538.0651.0668
[research_tran]: https://doi.org/10.70675/525a043az1807z4a8ez858cza3a7c4e2729e
[research_tran_thiriet_2020]: https://doi.org/10.1109/icuas48674.2020.9213903
[research_tranfield]: https://doi.org/10.1109/plans.1996.509105
[research_traub_1994]: https://doi.org/10.2514/3.46626
[research_traub_1995]: https://doi.org/10.2514/3.46739
[research_traub_1995_b]: https://doi.org/10.2514/3.46856
[research_traub_2016]: https://doi.org/10.2514/1.c033416
[research_travis_simmons_2005]: https://doi.org/10.1109/ivs.2005.1505126
[research_trimarchi_2023]: https://doi.org/10.1109/icuas57906.2023.10156156
[research_trinen_pieri_2026]: https://doi.org/10.2514/6.2026-114919
[research_troop_carrier]: https://doi.org/10.2307/j.ctt1ddr8gr.16
[research_troop_carrier_b]: https://doi.org/10.2307/j.ctt1ddr8gr.12
[research_truxal_scott_2024]: https://doi.org/10.4337/9781035312344.00008
[research_truxtondavies_powell_1970]: https://doi.org/10.1109/sap.1970.269969
[research_trw_to_2002]: https://doi.org/10.1108/aeat.2002.12774bab.035
[research_trwincclevelandohtrwaccessoriesdiv_1965]: https://doi.org/10.21236/ad0471437
[research_tsai_chang_2004]: https://doi.org/10.1049/ip-rsn:20040728
[research_tseng_lin_2016]: https://doi.org/10.1017/s0373463316000692
[research_tsoukalas_unlu_2026]: https://doi.org/10.1109/icuas69441.2026.11598570
[research_tsourveloudis_doitsidis_2025]: https://doi.org/10.1109/icuas65942.2025.11007903
[research_tsukamoto_deturris_2003]: https://doi.org/10.2514/6.2003-911
[research_tsybriy_guskov_2025]: https://doi.org/10.52467/2949-401x-2025-3-2-350-361
[research_tu_munir_1998]: https://doi.org/10.2514/6.1998-4573
[research_tu_munir_2000]: https://doi.org/10.2514/2.4607
[research_tucker_iii_1993]: https://doi.org/10.21236/ada290948
[research_tugolukov_2020]: https://doi.org/10.34759/trd-2020-111-17
[research_turan_2012]: https://doi.org/10.1016/j.energy.2012.03.030
[research_turbine_engine_2010]: https://doi.org/10.2514/5.9781600867538.0383.0412
[research_turner_faruqi]: https://doi.org/10.1109/icassp.1997.604846
[research_turrizianirv_lovellwa_1979]: https://ntrs.nasa.gov/citations/19790009681
[research_tuzlukov_2026]: https://doi.org/10.1201/9781003408802-6
[research_tvaryanas_2006]: https://doi.org/10.21236/ada444925
[research_tvaryanas_2006_b]: https://doi.org/10.21236/ada456387
[research_tvaryanas_singer_2012]: https://doi.org/10.21236/ada593691
[research_tweddale_fichtl_2011]: https://doi.org/10.21236/ada545736
[research_twesme_corzine_2003]: https://doi.org/10.2514/6.2003-6612
[research_tzes_tsoukalas_2023]: https://doi.org/10.2139/ssrn.4578669
[research_uav_control_2023]: https://doi.org/10.36652/0869-4931-2023-77-4-155-161
[research_uav_demonstrator_2006]: https://doi.org/10.1108/aeat.2006.12778eaf.005
[research_uav_demonstrator_2007]: https://doi.org/10.1108/aeat.2007.12779aaf.009
[research_ugwueze_statheros_2023]: https://doi.org/10.3390/aerospace10030311
[research_uk_aircraft_2014]: https://doi.org/10.1080/13567888.2014.955292
[research_ulybyshev_2015]: https://doi.org/10.2514/1.g000242
[research_unal_oz_2023]: https://doi.org/10.1108/aeat-02-2022-0056
[research_universal_balancing_2007]: https://doi.org/10.1108/aeat.2007.12779cad.003
[research_unmanned_aerial_2013]: https://doi.org/10.1002/9781118599938
[research_unmanned_aerial_2016]: https://doi.org/10.1201/b10401-24
[research_unmanned_aerial_2020]: https://doi.org/10.3390/books978-3-03936-709-2
[research_unmanned_aerial_2024]: https://doi.org/10.1007/978-3-031-45321-2
[research_unmanned_air_2017]: https://doi.org/10.1002/9781119406303.ch2
[research_unmanned_aircraft]: https://doi.org/10.3403/30421990
[research_unmanned_aircraft_2009]: https://doi.org/10.1007/978-1-4020-9137-7
[research_unmanned_aircraft_2012]: https://doi.org/10.2514/5.9781600868443.0025.0056
[research_unmanned_aircraft_2014]: https://doi.org/10.2514/5.9781624102615.0025.0056
[research_unmanned_aircraft_2014_b]: https://doi.org/10.2514/5.9781624102615.0085.0148
[research_unmanned_aircraft_2016]: https://doi.org/10.1201/b11202-7
[research_unmanned_aircraft_2016_b]: https://doi.org/10.1201/b11202-10
[research_unmanned_aircraft_2016_c]: https://doi.org/10.1201/b11202-11
[research_unmanned_aircraft_b]: https://doi.org/10.1007/978-1-4020-8672-4_4
[research_unmanned_aircraft_c]: https://doi.org/10.3403/30379528
[research_unmanned_aircraft_d]: https://doi.org/10.3403/30439524
[research_unmanned_aircraft_geometry_2012]: https://doi.org/10.2514/5.9781600868443.0085.0150
[research_unmanned_autonomous_2016]: https://doi.org/10.1201/9781315371191-12
[research_urnes_hess_1979]: https://doi.org/10.2514/6.1979-1772
[research_urnes_hess_1983]: https://doi.org/10.2514/6.1983-2162
[research_urnes_hess_1985]: https://doi.org/10.2514/3.19978
[research_urrehman_2018]: https://doi.org/10.2139/ssrn.3243546
[research_usachmolina]: https://doi.org/10.4995/thesis/10251/130202
[research_useful_aircraft]: https://doi.org/10.1017/9781139542418.013
[research_useful_aircraft_1999]: https://doi.org/10.1017/cbo9780511808906.013
[research_utsch_rockwell_1990]: https://doi.org/10.2514/3.25324
[research_utterstrom_kestek_1965]: https://doi.org/10.2514/6.1965-1234
[research_uybarreta_grant_2025]: https://doi.org/10.2514/6.2025-3610
[research_uzun_2024]: https://doi.org/10.1108/aeat-11-2023-0302
[research_uzzell_1997]: https://doi.org/10.21236/ada388266
[research_vachtsevanos_valavanis_2014]: https://doi.org/10.1007/978-90-481-9707-1_96
[research_vahidi_saberinia_2016]: https://doi.org/10.1109/icuas.2016.7502656
[research_valavanis_oh]: https://doi.org/10.1007/978-1-4020-9137-7_1
[research_valavanis_vachtsevanos_2014]: https://doi.org/10.1007/978-90-481-9707-1_95
[research_vale_albuquerque_2025]: https://doi.org/10.7862/tiam.2025.4.2
[research_vali_2004]: https://doi.org/10.21236/ada426298
[research_validation_and]: https://doi.org/10.4271/arp6539
[research_vallespin_ronch_2011]: https://doi.org/10.2514/1.c031385
[research_vallot_snyder_1991]: https://doi.org/10.1002/j.2161-4296.1991.tb01719.x
[research_van_van_2015]: https://doi.org/10.12720/joace.3.2.109-114
[research_vana_bisnath_2024]: https://doi.org/10.1007/s10291-023-01606-2
[research_vance_1984]: https://doi.org/10.21236/ada166209
[research_vandierendonck_hatch_1992]: https://doi.org/10.21236/ada255276
[research_vandyke_1992]: https://doi.org/10.1002/j.2161-4296.1992.tb02286.x
[research_vangool_mooij_1979]: https://doi.org/10.2514/6.1979-1679
[research_vangool_weingarten_1981]: https://doi.org/10.2514/6.1981-2478
[research_vangraas_1988]: https://doi.org/10.1002/j.2161-4296.1988.tb00948.x
[research_vankampen_deweerdt_2009]: https://doi.org/10.2514/6.2009-5973
[research_vanrooij_cummings_2018]: https://doi.org/10.2514/6.2018-2840
[research_vanrooij_frink_2018]: https://doi.org/10.2514/6.2018-2998
[research_vanrooij_frink_2019]: https://doi.org/10.1016/j.ast.2019.105510
[research_vanslagmaat_1992]: https://doi.org/10.1080/00423119208970002
[research_vanslagmaat_2004]: https://doi.org/10.1080/00423110408970002
[research_vanslagmaat_2026]: https://doi.org/10.1201/9781003760634-9
[research_vanualailai_sharan_2013]: https://doi.org/10.1109/isic.2013.6658618
[research_variable_sweep_1980]: https://doi.org/10.2514/6.1980-3043
[research_vashishth_sharma_2024]: https://doi.org/10.1002/9781394230648.ch1
[research_vehicle_navigation_2002]: https://doi.org/10.5394/kinpr.2002.26.3.303
[research_venetsky_husni_2003]: https://doi.org/10.21236/ada422629
[research_venkata_jones_2013]: https://doi.org/10.2514/1.c032128
[research_venkatesh_2023]: https://doi.org/10.32920/23579814
[research_venugopalan_taher_2012]: https://doi.org/10.1109/oceans.2012.6404893
[research_vepa_2016]: https://doi.org/10.1201/9781315367378
[research_vepa_2020]: https://doi.org/10.1201/9780429202315-6
[research_vepa_2023]: https://doi.org/10.1201/9781003266310-4
[research_vepa_2023_b]: https://doi.org/10.1201/9781003266310-10
[research_verhagen_2004]: https://doi.org/10.1007/s10291-004-0087-5
[research_verhagen_2005]: https://doi.org/10.1002/j.2161-4296.2005.tb01736.x
[research_verma_shrinivasan_2021]: https://doi.org/10.37394/23203.2021.16.25
[research_vick_carter_1963]: https://doi.org/10.21236/ad0607920
[research_vicory_1968]: https://doi.org/10.21236/ad0676791
[research_vicroy_loeser_2012]: https://doi.org/10.2514/1.c031501
[research_vicroydand_huberkerstinc_2014]: https://ntrs.nasa.gov/citations/20140011407
[research_videmsek_dehaag_2019]: https://doi.org/10.1109/dasc43569.2019.9081778
[research_videmsek_dehaag_2020]: https://doi.org/10.23919/enc48637.2020.9317481
[research_video_communications_2013]: https://doi.org/10.1201/b15552-22
[research_vidimlic_levin_2021]: https://doi.org/10.5220/0010248801230135
[research_vieweg]: https://doi.org/10.1109/plans.1994.303386
[research_vinokurov_glinkin_1992]: https://doi.org/10.1016/s1474-6670(17)49645-5
[research_vinokurov_glinkin_1993]: https://doi.org/10.1016/b978-0-08-041715-8.50023-7
[research_vishniak_1993]: https://doi.org/10.2514/6.1993-1250
[research_visnevski_castilloeffen_2010]: https://doi.org/10.1109/aero.2010.5446782
[research_visual_glide_1961]: https://doi.org/10.1109/ee.1961.6433403
[research_vlasov_1969]: https://doi.org/10.21236/ad0697985
[research_vorobev_beliatskaya_2020]: https://doi.org/10.26467/2079-0619-2020-23-4-33-44
[research_vos_2019]: https://doi.org/10.35294/ls201902.vos3
[research_vos_2019_b]: https://doi.org/10.35294/ls201902.vos1
[research_vos_2019_c]: https://doi.org/10.35294/ls201902.vos2
[research_vos_gurdal_2010]: https://doi.org/10.2514/1.39328
[research_voss_2018]: https://doi.org/10.2514/6.2018-3326
[research_voss_2019]: https://doi.org/10.1016/j.ast.2019.03.049
[research_voss_cumnuantip_2011]: https://doi.org/10.2514/6.2011-3020
[research_vrchota_2017]: https://doi.org/10.2514/6.2017-0491
[research_vulnerability_of_1959]: https://doi.org/10.7249/d6625
[research_waas_gps_2009]: https://doi.org/10.1108/aeat.2009.12781cab.008
[research_wade_2002]: https://doi.org/10.21236/ada408061
[research_wadley_tallant_2003]: https://doi.org/10.2514/6.2003-5596
[research_wagdi_1984]: https://doi.org/10.2514/6.1984-239
[research_waggoner_1999]: https://doi.org/10.21236/ada363882
[research_wagner_2005]: https://doi.org/10.1007/s10291-004-0122-6
[research_wakayama_kroo_1995]: https://doi.org/10.2514/3.46786
[research_walker_1960]: https://doi.org/10.1049/sqj.1960.0043
[research_walker_1961]: https://doi.org/10.1049/jiee-3.1961.0061
[research_walker_2011]: https://doi.org/10.21236/ada545592
[research_walker_2015]: https://doi.org/10.31356/avi-fac0003
[research_walker_2024]: https://doi.org/10.58940/2374-6793.1884
[research_wall_1962]: https://doi.org/10.6028/nbs.rpt.7419
[research_wallace_2000]: https://doi.org/10.21236/ada382563
[research_walton_1992]: https://doi.org/10.21236/ada263324
[research_wampler_myklebust_1988]: https://doi.org/10.2514/6.1988-4481
[research_wang_2000]: https://doi.org/10.15760/etd.6517
[research_wang_2010]: https://doi.org/10.1007/s10291-010-0175-7
[research_wang_2016]: https://doi.org/10.1051/matecconf/20167701038
[research_wang_2022]: https://doi.org/10.1049/icp.2022.1550
[research_wang_2026]: https://doi.org/10.1007/978-981-95-7840-5_53
[research_wang_2026_b]: https://doi.org/10.1590/jatm.v18.1450
[research_wang_ai_2025]: https://doi.org/10.3390/aerospace12080688
[research_wang_carl_1999]: https://doi.org/10.2514/6.1999-265
[research_wang_chen_2016]: https://doi.org/10.1155/2016/7345056
[research_wang_chen_2021]: https://doi.org/10.1109/iceemt52412.2021.9601650
[research_wang_cui_2013]: https://doi.org/10.1016/j.ast.2012.11.004
[research_wang_deng_2010]: https://doi.org/10.1088/0957-0233/21/6/065102
[research_wang_fei_2020]: https://doi.org/10.1109/ccdc49329.2020.9164781
[research_wang_feng_2016]: https://doi.org/10.1007/s10291-016-0550-0
[research_wang_gong_2010]: https://doi.org/10.1109/navitec.2010.5708079
[research_wang_hou_2022]: https://doi.org/10.1007/s10291-022-01367-4
[research_wang_huang_2013]: https://doi.org/10.1007/978-3-642-37404-3_17
[research_wang_hubbard_2022]: https://doi.org/10.7771/2159-6670.1238
[research_wang_iz_2002]: https://doi.org/10.1007/s10291-002-0021-7
[research_wang_jan_2023]: https://doi.org/10.1109/plans53410.2023.10140022
[research_wang_li_2017]: https://doi.org/10.1155/2017/6427209
[research_wang_li_2021]: https://doi.org/10.1049/rsn2.12199
[research_wang_li_2024]: https://doi.org/10.1007/978-981-97-3340-8_50
[research_wang_lin_2022]: https://doi.org/10.1177/01423312221104424
[research_wang_liu_2006]: https://doi.org/10.1016/j.ast.2006.03.003
[research_wang_liu_2016]: https://doi.org/10.2514/6.2016-3528
[research_wang_liu_2020]: https://doi.org/10.1016/j.cja.2020.06.020
[research_wang_liu_2023]: https://doi.org/10.1109/isas59543.2023.10164287
[research_wang_liu_2026]: https://doi.org/10.1007/978-981-95-3013-7_4
[research_wang_lu_2021]: https://doi.org/10.1007/s11431-021-1915-6
[research_wang_lv_2021]: https://doi.org/10.23919/ccc52363.2021.9550472
[research_wang_mcdonald_2019]: https://doi.org/10.2514/6.2019-3619
[research_wang_meng_2021]: https://doi.org/10.1016/j.asr.2021.01.048
[research_wang_miao_2009]: https://doi.org/10.1088/0957-0233/20/7/075108
[research_wang_mkhoyan_2022]: https://doi.org/10.2514/1.g005921
[research_wang_morikawa_1996]: https://doi.org/10.1002/ecja.4410790808
[research_wang_ober_2009]: https://doi.org/10.1017/s0373463308005158
[research_wang_rathinam_2018]: https://doi.org/10.1115/dscc2018-8949
[research_wang_rizos_2001]: https://doi.org/10.1007/pl00012877
[research_wang_shi_2023]: https://doi.org/10.1088/1742-6596/2472/1/012017
[research_wang_song_2009]: https://doi.org/10.2514/1.38057
[research_wang_sun_2011]: https://doi.org/10.4028/www.scientific.net/kem.467-469.579
[research_wang_tang_2020]: https://doi.org/10.1088/1742-6596/1509/1/012022
[research_wang_toth_2021]: https://doi.org/10.33012/2021.17989
[research_wang_wang_2012]: https://doi.org/10.1016/s1000-9361(11)60412-3
[research_wang_wang_2013]: https://doi.org/10.4028/www.scientific.net/amr.748.747
[research_wang_wang_2017]: https://doi.org/10.1007/s11432-016-9092-y
[research_wang_wang_2018]: https://doi.org/10.26438/ijcse/v6i6.16
[research_wang_wang_2020]: https://doi.org/10.1016/j.ast.2019.105534
[research_wang_wang_2020_b]: https://doi.org/10.1109/icus50048.2020.9274858
[research_wang_wu_2018]: https://doi.org/10.1109/plans.2018.8373460
[research_wang_wu_2018_b]: https://doi.org/10.1007/s10291-018-0773-3
[research_wang_xin_2012]: https://doi.org/10.2514/6.2012-4459
[research_wang_xuan_2020]: https://doi.org/10.1002/adc2.27
[research_wang_yang_2012]: https://doi.org/10.1109/iccect.2012.178
[research_wang_yang_2026]: https://doi.org/10.1016/j.jfranklin.2025.108381
[research_wang_yao_2019]: https://doi.org/10.1007/s10291-019-0825-3
[research_wang_yin_2019]: https://doi.org/10.1016/j.ast.2019.07.026
[research_wang_you_2021]: https://doi.org/10.3390/s22010165
[research_wang_yuan_2024]: https://doi.org/10.1016/j.ast.2023.108772
[research_wang_zhan_2005]: https://doi.org/10.2514/1.9929
[research_wang_zhan_2020]: https://doi.org/10.1007/s42401-020-00057-8
[research_wang_zhan_2021]: https://doi.org/10.1016/j.cja.2020.05.022
[research_wang_zhan_2023]: https://doi.org/10.33012/2023.18607
[research_wang_zhang_2005]: https://doi.org/10.1117/12.658348
[research_wang_zhao_2022]: https://doi.org/10.1007/978-3-030-99018-3_3
[research_wang_zhao_2024]: https://doi.org/10.2139/ssrn.5001796
[research_wang_zhou_2022]: https://doi.org/10.1016/j.ast.2022.107804
[research_wang_zhu_2016]: https://doi.org/10.2514/1.c033721
[research_wanlixu_zhunliu_2012]: https://doi.org/10.1109/nces.2012.6544145
[research_ward_1983]: https://doi.org/10.2514/6.1983-2459
[research_ward_1994]: https://doi.org/10.1017/s0373463300012108
[research_ward_costello_2012]: https://doi.org/10.1109/acc.2012.6315600
[research_ward_costello_2013]: https://doi.org/10.2514/1.59260
[research_ward_gavrilovski_2013]: https://doi.org/10.2514/1.c032029
[research_ward_monaco_1999]: https://doi.org/10.2514/6.1999-4045
[research_wareykaglaner_moller_2025]: https://doi.org/10.5194/egusphere-egu25-15232
[research_warner_1970]: https://doi.org/10.2514/6.1970-938
[research_warner_lee_2026]: https://doi.org/10.2514/6.2026-3040
[research_warren_richards_2009]: https://doi.org/10.2514/6.2009-6070
[research_warsch_carbone_2026]: https://doi.org/10.3390/aerospace13070623
[research_wasmi_rahim_2016]: https://doi.org/10.31026/j.eng.2016.10.05
[research_wasser_boddhu_2011]: https://doi.org/10.21236/ada567802
[research_wasserman_mitchell_1973]: https://doi.org/10.21236/ad0761120
[research_watanabe_2020]: https://doi.org/10.1016/j.ifacol.2020.12.1842
[research_waterman_miller_2000]: https://doi.org/10.21236/ada381795
[research_watson_owen_2020]: https://doi.org/10.2514/1.c035733
[research_watson_owen_2025]: https://doi.org/10.1017/aer.2025.10072
[research_wauters_2022]: https://doi.org/10.1177/17568293221092139
[research_weaponised_unmanned_2013]: https://doi.org/10.1002/9781118519165.ch14
[research_weapons_carriage_2006]: https://doi.org/10.1002/0470035463.ch9
[research_web_site_2008]: https://doi.org/10.1108/aeat.2008.12780dab.025
[research_webb_2022]: https://doi.org/10.21236/ad1183624
[research_webb_nolan_1954]: https://doi.org/10.21236/ad0037814
[research_webster_1971]: https://doi.org/10.21236/ad0729067
[research_webster_cameron_2012]: https://doi.org/10.2514/6.2012-2573
[research_weeks_2000]: https://doi.org/10.21236/ada379424
[research_wei_2013]: https://doi.org/10.2514/6.2013-4268
[research_wei_du_2018]: https://doi.org/10.1109/gncc42960.2018.9019216
[research_wei_kang_2025]: https://doi.org/10.1007/978-981-96-2248-1_16
[research_wei_schwarz]: https://doi.org/10.1109/plans.1990.66210
[research_wei_tong_2026]: https://doi.org/10.4271/2026-99-1860
[research_wei_zhai_2026]: https://doi.org/10.2139/ssrn.6944778
[research_weight_prediction_2020]: https://doi.org/10.1002/9781119667063.ch3
[research_weijun_xiangju_2008]: https://doi.org/10.1016/s1000-9361(08)60029-1
[research_weinberg_1966]: https://doi.org/10.21236/ad0632457
[research_weinert_richardp_1991]: https://doi.org/10.21236/ada236573
[research_weingarten_1977]: https://doi.org/10.21236/ada055343
[research_weingarten_chalk_1982]: https://doi.org/10.2514/6.1982-1296
[research_weiss_shields]: https://doi.org/10.1109/plans.1998.670196
[research_weisshaar_1990]: https://doi.org/10.2514/3.25276
[research_weisshaar_1994]: https://doi.org/10.2514/3.46463
[research_welbourn_lachance_1961]: https://doi.org/10.21236/ad0268302
[research_wells_1993]: https://doi.org/10.21236/ada265083
[research_welterlen_2000]: https://doi.org/10.2514/6.2000-3926
[research_weltz_barajas_2025]: https://doi.org/10.2514/6.2025-3538
[research_wen_du_2023]: https://doi.org/10.1109/icus58632.2023.10318480
[research_wen_pfeifer_2021]: https://doi.org/10.1002/navi.421
[research_wen_zhi_2009]: https://doi.org/10.1016/s1000-9361(08)60113-2
[research_wendel_maier_2005]: https://doi.org/10.2514/6.2005-6055
[research_wenhuyou_fuxingjiang]: https://doi.org/10.1109/wcica.2004.1340924
[research_wernerwestphal_heinze_2008]: https://doi.org/10.1016/j.ast.2007.05.006
[research_west_2009]: https://doi.org/10.21236/ada540176
[research_westatincrockvillemd_2001]: https://doi.org/10.21236/ada385238
[research_westbrook_1964]: https://doi.org/10.2514/6.1964-777
[research_westra_lintern_1986]: https://doi.org/10.21236/ada169962
[research_westra_simon_1981]: https://doi.org/10.21236/ada122064
[research_weyl_1944]: https://doi.org/10.1108/eb031199
[research_weyl_1945]: https://doi.org/10.1108/eb031288
[research_weyl_1945_b]: https://doi.org/10.1108/eb031217
[research_wheeler_koch_2018]: https://doi.org/10.1109/mcs.2018.2830079
[research_wheeler_nyholm_2016]: https://doi.org/10.1002/9780470686652.eae1154
[research_white]: https://doi.org/10.18130/v3kt0v
[research_white_1992]: https://doi.org/10.21236/ada249834
[research_white_2005]: https://doi.org/10.21236/ada471992
[research_white_2012]: https://doi.org/10.21236/ada566304
[research_whitehead_1960]: https://doi.org/10.1017/s036839310007245x
[research_whitemauriced_innisrobertc_1959]: https://ntrs.nasa.gov/citations/19980232080
[research_whitford_1990]: https://doi.org/10.2514/6.1990-3241
[research_whitford_1991]: https://doi.org/10.2514/6.1991-3114
[research_whitford_1992]: https://doi.org/10.2514/6.1992-1092
[research_whitford_1993]: https://doi.org/10.2514/6.1993-3953
[research_whitford_1994]: https://doi.org/10.21236/ada338919
[research_why_should]: https://doi.org/10.1017/9781139542418.003
[research_why_should_1999]: https://doi.org/10.1017/cbo9780511808906.003
[research_wiart_carrier_2010]: https://doi.org/10.2514/6.2010-9135
[research_wick]: https://doi.org/10.31274/rtd-180813-14316
[research_wide_body_and]: https://doi.org/10.4271/air1869c
[research_widnall_gobbini_1982]: https://doi.org/10.21236/ada116417
[research_wiederholt_klein_1984]: https://doi.org/10.1002/j.2161-4296.1984.tb00867.x
[research_wieland_sharma_2013]: https://doi.org/10.2514/6.2013-4364
[research_wilcox_mackunis_2010]: https://doi.org/10.2514/1.46785
[research_wildermuth_rothammer_1974]: https://doi.org/10.21236/ada002854
[research_wildermuth_rothammer_1974_b]: https://doi.org/10.21236/ada002873
[research_wilhelm_schafranek_1986]: https://doi.org/10.2514/3.45377
[research_wilhem_1970]: https://doi.org/10.21236/ad0702528
[research_willebeeklemair_rhinehart_2023]: https://doi.org/10.4050/sm_2023_hq-1196
[research_williams_davis_2000]: https://doi.org/10.21236/ada459739
[research_williams_niestroy_2025]: https://doi.org/10.2514/6.2025-1451
[research_williams_trivailo_2006]: https://doi.org/10.2514/1.21132
[research_williams_trivailo_2006_b]: https://doi.org/10.2514/6.2006-6375
[research_williamson_1966]: https://doi.org/10.21236/ad0648585
[research_willis]: https://doi.org/10.1017/upo9781846156373.007
[research_wills_2015]: https://doi.org/10.1057/9781137498496_4
[research_wills_2015_b]: https://doi.org/10.1057/9781137498496
[research_wilsbach_1998]: https://doi.org/10.21236/ada348345
[research_wilson_2018]: https://doi.org/10.2514/6.2018-3678
[research_wilson_goktogan_2014]: https://doi.org/10.1109/icra.2014.6907590
[research_wilson_goktogan_2015]: https://doi.org/10.1109/icra.2015.7139941
[research_wilsonsbiii_1992]: https://ntrs.nasa.gov/citations/19930029330
[research_wilt_hicks_2022]: https://doi.org/10.2514/6.2022-3202
[research_wing_design_2012]: https://doi.org/10.1002/9781118352700.ch5
[research_wings_2017]: https://doi.org/10.1002/9781119406303.ch3
[research_winter_robinson_2021]: https://doi.org/10.2514/6.2021-2437
[research_wise_1990]: https://doi.org/10.21236/ada237349
[research_wise_2003]: https://doi.org/10.2514/6.2003-5320
[research_wise_2004]: https://doi.org/10.23919/acc.2004.1383562
[research_wiser_2009]: https://doi.org/10.21236/ada510744
[research_witherell_1992]: https://doi.org/10.31399/asm.fach.v01.c9001020
[research_wittenberg_2001]: https://doi.org/10.1016/s1369-8869(00)00026-4
[research_woelk_1989]: https://doi.org/10.2514/6.1989-2123
[research_wolf_shelley_2016]: https://doi.org/10.2514/6.2016-0406
[research_wolfe_1976]: https://doi.org/10.21236/ada034873
[research_wolfe_speyer_2004]: https://doi.org/10.2514/6.2004-4777
[research_wolfe_williamson_2003]: https://doi.org/10.1002/j.2161-4296.2003.tb00317.x
[research_wolff_2022]: https://doi.org/10.64628/ab.33yrjfrqj
[research_wolff_lohr_1988]: https://doi.org/10.4043/5624-ms
[research_woo_choi_2022]: https://doi.org/10.3390/drones6010020
[research_woods_1994]: https://doi.org/10.21236/ada280625
[research_woods_daines_2003]: https://doi.org/10.2514/6.2003-982
[research_worked_manned_2017]: https://doi.org/10.1002/9781119406303.app3
[research_wortman_1981]: https://doi.org/10.21236/adb058960
[research_wortmann_hoogreef_2015]: https://doi.org/10.2514/6.2015-2385
[research_wrenn_dovi_1988]: https://doi.org/10.2514/3.45634
[research_wright_2005]: https://doi.org/10.1108/aeat.2005.12777eaf.001
[research_wright_barry_2014]: https://doi.org/10.1109/milcom.2014.206
[research_wright_burton_1991]: https://doi.org/10.21236/ada269764
[research_wu_2017]: https://doi.org/10.1117/12.2281937
[research_wu_gu_2017]: https://doi.org/10.23919/icins.2017.7995603
[research_wu_lin_2026]: https://doi.org/10.1109/iccad69956.2026.11643021
[research_wu_luo_2023]: https://doi.org/10.1007/978-981-99-0479-2_128
[research_wu_lv_2023]: https://doi.org/10.1145/3638584.3638598
[research_wu_moracamino_2012]: https://doi.org/10.2514/6.2012-4442
[research_wu_mueller_2018]: https://doi.org/10.1109/icuas.2018.8453347
[research_wu_peck_2008]: https://doi.org/10.1109/plans.2008.4570100
[research_wu_song_2018]: https://doi.org/10.1109/gncc42960.2018.9019138
[research_wu_wang_2024]: https://doi.org/10.3390/drones9010003
[research_wu_wang_2026]: https://doi.org/10.2139/ssrn.7292623
[research_wu_zhang_2018]: https://doi.org/10.1017/s0373463318001017
[research_wu_zhu_2024]: https://doi.org/10.1155/2024/2054883
[research_wu_zhu_2026]: https://doi.org/10.1108/aeat-08-2025-0295
[research_wyatt_2003]: https://doi.org/10.2514/6.2003-2616
[research_wynn_mclain_2019]: https://doi.org/10.23919/acc.2019.8814694
[research_wynnyk_lunsford_2017]: https://doi.org/10.2514/1.c033708
[research_xi_liu_2020]: https://doi.org/10.1109/icuas48674.2020.9213983
[research_xi_zhao_2017]: https://doi.org/10.1109/ascc.2017.8287228
[research_xia_2004]: https://doi.org/10.1007/s10291-004-0085-7
[research_xia_dong_2016]: https://doi.org/10.2514/1.c033175
[research_xia_wu_2025]: https://doi.org/10.1109/ifeea66847.2025.11388784
[research_xiangjin_dejong_1996]: https://doi.org/10.1017/s0373463300013357
[research_xiao_2008]: https://doi.org/10.2514/6.2008-7022
[research_xiao_zhen_2024]: https://doi.org/10.1108/aeat-07-2023-0193
[research_xiaofeng_daqian_2020]: https://doi.org/10.5194/egusphere-egu2020-4508
[research_xie_cai_2019]: https://doi.org/10.2514/6.2019-2885
[research_xie_dong_2019]: https://doi.org/10.1109/icusai47366.2019.9124851
[research_xie_haberland_1999]: https://doi.org/10.1016/s1369-8869(99)00012-9
[research_xie_huang_2023]: https://doi.org/10.1007/s10291-022-01393-2
[research_xie_jia_2026]: https://doi.org/10.1016/b978-0-44-340433-7.00008-2
[research_xie_jia_2026_b]: https://doi.org/10.1016/b978-0-44-340433-7.00011-2
[research_xie_jia_2026_c]: https://doi.org/10.1016/b978-0-44-340433-7.00010-0
[research_xie_jia_2026_d]: https://doi.org/10.1016/b978-0-44-340433-7.00012-4
[research_xie_jia_2026_e]: https://doi.org/10.1016/b978-0-44-340433-7.00013-6
[research_xie_jia_2026_f]: https://doi.org/10.1016/b978-0-44-340433-7.00014-8
[research_xie_jia_2026_g]: https://doi.org/10.1016/b978-0-44-340433-7.00015-x
[research_xie_yang_2011]: https://doi.org/10.4028/www.scientific.net/amr.213.334
[research_xin_luo_2018]: https://doi.org/10.1108/ijicc-06-2017-0067
[research_xiong_zhou_2022]: https://doi.org/10.3390/s22186992
[research_xu_2002]: https://doi.org/10.5081/jgps.1.2.122
[research_xu_2013]: https://doi.org/10.4028/www.scientific.net/amm.336-338.332
[research_xu_2018]: https://doi.org/10.1117/12.2304718
[research_xu_2025]: https://doi.org/10.1109/aipip66876.2025.11299229
[research_xu_carrillo_2015]: https://doi.org/10.1109/icuas.2015.7152374
[research_xu_han_2019]: https://doi.org/10.1155/2019/9362629
[research_xu_hong_2025]: https://doi.org/10.5220/0013432600003970
[research_xu_huang_2020]: https://doi.org/10.1155/2020/8881233
[research_xu_li_2010]: https://doi.org/10.1017/s0373463309990361
[research_xu_liu_2013]: https://doi.org/10.4028/www.scientific.net/amm.380-384.3429
[research_xu_liu_2021]: https://doi.org/10.1049/sbra545e_ch1
[research_xu_morton_2018]: https://doi.org/10.1007/s10291-018-0775-1
[research_xu_shen_2022]: https://doi.org/10.1007/s10291-022-01242-2
[research_xu_shi_2012]: https://doi.org/10.1179/1752270611y.0000000004
[research_xu_shi_2013]: https://doi.org/10.4028/www.scientific.net/amm.367.411
[research_xu_zhang_2018]: https://doi.org/10.12783/dtcse/mmsta2017/19666
[research_xu_zhao_2017]: https://doi.org/10.23919/chicc.2017.8028367
[research_xuanzhao_zhong_2016]: https://doi.org/10.1109/cgncc.2016.7828804
[research_xue_atkins_2003]: https://doi.org/10.2514/6.2003-5515
[research_xue_do_2019]: https://doi.org/10.2514/6.2019-3513
[research_xue_huang_2024]: https://doi.org/10.1142/s2301385025500694
[research_xue_zhao_2011]: https://doi.org/10.2514/1.c031240
[research_xue_zhen_2023]: https://doi.org/10.1108/aeat-02-2023-0047
[research_yacef_bouhali_2014]: https://doi.org/10.1109/icuas.2014.6842341
[research_yadav_shanmukha_2017]: https://doi.org/10.1109/icammaet.2017.8186715
[research_yadav_shukla_2012]: https://doi.org/10.1061/(asce)gm.1943-5622.0000118
[research_yakimenko_kaminer_2002]: https://doi.org/10.1109/taes.2002.1145742
[research_yakovlev_bakulin_2020]: https://doi.org/10.3997/2214-4609.202034014
[research_yan_xunhua_2018]: https://doi.org/10.1109/gncc42960.2018.9019112
[research_yan_zhang_2025]: https://doi.org/10.2514/1.c038223
[research_yan_zhao_2014]: https://doi.org/10.1109/cgncc.2014.7007245
[research_yanagihara_shigemi_1999]: https://doi.org/10.2514/2.2553
[research_yang_1970]: https://doi.org/10.2514/6.1970-914
[research_yang_1971]: https://doi.org/10.2514/3.59188
[research_yang_2013]: https://doi.org/10.1007/s12555-011-0157-8
[research_yang_2024]: https://doi.org/10.1002/adc2.194
[research_yang_chang_2001]: https://doi.org/10.1016/s1474-6670(17)40730-0
[research_yang_duan_2018]: https://doi.org/10.1016/j.ast.2018.06.013
[research_yang_garratt_2010]: https://doi.org/10.1007/978-94-007-1110-5_18
[research_yang_jiang_2016]: https://doi.org/10.2991/mmme-16.2016.34
[research_yang_jiang_2026]: https://doi.org/10.3390/aerospace13080669
[research_yang_li_2013]: https://doi.org/10.1017/s0373463313000763
[research_yang_mischel_1995]: https://doi.org/10.2514/6.1995-3245
[research_yang_nita_2021]: https://doi.org/10.31224/osf.io/5hfv4
[research_yang_shi_2018]: https://doi.org/10.1007/s10291-018-0766-2
[research_yang_shou_2026]: https://doi.org/10.1109/taes.2026.3729189
[research_yang_song_2026]: https://doi.org/10.2514/1.j066663
[research_yang_wan_2025]: https://doi.org/10.3390/drones9100690
[research_yang_yang_2024]: https://doi.org/10.3390/drones8080382
[research_yang_zhang_2023]: https://doi.org/10.1049/rsn2.12488
[research_yang_zhang_2023_b]: https://doi.org/10.1007/978-981-19-6613-2_339
[research_yang_zheng_2013]: https://doi.org/10.1007/978-3-642-37404-3_12
[research_yang_zheng_2023]: https://doi.org/10.1109/cac59555.2023.10452111
[research_yang_zhu_2024]: https://doi.org/10.1007/978-981-97-6199-9_3
[research_yanushevsky_2026]: https://doi.org/10.1201/9781003675921-8
[research_yanushevsky_2026_b]: https://doi.org/10.1201/9781003675921
[research_yanushevsky_2026_c]: https://doi.org/10.1201/9781003675921-12
[research_yao_kan_2024]: https://doi.org/10.1108/aeat-10-2023-0273
[research_yao_li_2025]: https://doi.org/10.1142/s2737480725500062
[research_yao_li_2025_b]: https://doi.org/10.1016/j.cja.2024.08.033
[research_yao_wang_2018]: https://doi.org/10.23919/chicc.2018.8484250
[research_yardley_kallimani_2008]: https://doi.org/10.7249/rb9316
[research_yarygina_popov_2012]: https://doi.org/10.3103/s106879981202002x
[research_yasuda_2025]: https://doi.org/10.1007/978-981-96-8437-3_9
[research_yavnai_2003]: https://doi.org/10.2514/6.2003-6639
[research_yaweiliang]: https://doi.org/10.1109/icnnb.2005.1614598
[research_ye_gu_2023]: https://doi.org/10.1007/978-981-99-6944-9_46
[research_ye_zhang_2022]: https://doi.org/10.1007/978-981-19-2580-1_14
[research_ye_zheng_2025]: https://doi.org/10.1109/cac67268.2025.11487888
[research_yen_1982]: https://doi.org/10.2514/3.61549
[research_yerger_2006]: https://doi.org/10.21236/ada460061
[research_yilmaz_alaiwi_2024]: https://doi.org/10.2139/ssrn.4848586
[research_yilmaz_warren_2019]: https://doi.org/10.2514/6.2019-3122
[research_yin_fan_2020]: https://doi.org/10.1109/icus50048.2020.9274892
[research_yin_gu_2023]: https://doi.org/10.1016/j.isatra.2023.01.018
[research_yin_ni_2025]: https://doi.org/10.2514/1.c038271
[research_yin_teunissen_2025]: https://doi.org/10.1007/s10291-024-01806-4
[research_yoakum_cerreta_2020]: https://doi.org/10.15394/ijaaa.2020.1524
[research_yogeshwaran]: https://doi.org/10.32657/10356/61444
[research_yomchinda_2015]: https://doi.org/10.1109/acdt.2015.7111613
[research_yongjiang_jiecao_2006]: https://doi.org/10.1109/wcica.2006.1714021
[research_yoo_chihoonlee_2014]: https://doi.org/10.1109/iccas.2014.6987820
[research_yoo_cho_2013]: https://doi.org/10.1109/iccas.2013.6704243
[research_yoo_park_2015]: https://doi.org/10.1109/iccas.2015.7364647
[research_yoo_park_2021]: https://doi.org/10.11627/jkise.2021.44.3.064
[research_yoon_lundberg_2002]: https://doi.org/10.1016/s0096-3003(01)00029-7
[research_yoon_nerem_2004]: https://doi.org/10.1080/01490410490889058
[research_york_pack_2011]: https://doi.org/10.1007/978-94-007-3033-5_32
[research_you_shim_2010]: https://doi.org/10.1007/978-94-007-1110-5_21
[research_young_1997]: https://doi.org/10.1063/1.51932
[research_young_2000]: https://doi.org/10.1016/s1369-8869(00)00014-8
[research_youngjr_2002]: https://doi.org/10.21236/ada454056
[research_yu_chen_2010]: https://doi.org/10.1109/icgcs.2010.5543092
[research_yu_chen_2011]: https://doi.org/10.2514/6.2011-6714
[research_yu_du_2006]: https://doi.org/10.1080/15732470600590333
[research_yu_he_2019]: https://doi.org/10.1016/j.actaastro.2019.03.011
[research_yu_hu_2022]: https://doi.org/10.3390/aerospace9050261
[research_yu_hua_2017]: https://doi.org/10.23919/chicc.2017.8027858
[research_yu_li_2023]: https://doi.org/10.1002/rnc.6570
[research_yu_li_2024]: https://doi.org/10.1109/tvt.2023.3329470
[research_yu_liu_2019]: https://doi.org/10.2514/6.2019-2940
[research_yu_qu_2018]: https://doi.org/10.1109/ccta.2018.8511405
[research_yu_yang_2020]: https://doi.org/10.1007/s11071-020-05915-w
[research_yuan]: https://doi.org/10.32657/10356/85185
[research_yuan_bao_2012]: https://doi.org/10.1007/978-3-642-29193-7_42
[research_yuan_duan_2024]: https://doi.org/10.1109/jas.2024.124254
[research_yuan_wang_2025]: https://doi.org/10.1007/978-981-96-3240-4_57
[research_yuan_xi_2011]: https://doi.org/10.4028/www.scientific.net/amm.63-64.569
[research_yuan_xing_2014]: https://doi.org/10.1109/chicc.2014.6896009
[research_yuan_xue_2026]: https://doi.org/10.1002/asjc.70051
[research_yuan_yuan_2011]: https://doi.org/10.1109/cso.2011.63
[research_yuan_zhao_2017]: https://doi.org/10.1109/ascc.2017.8287584
[research_yue_lian_2017]: https://doi.org/10.1007/978-981-10-4591-2_32
[research_yue_liu_2016]: https://doi.org/10.2514/6.2016-3527
[research_yue_wang_2009]: https://doi.org/10.2514/6.2009-6155
[research_yue_wang_2013]: https://doi.org/10.2514/6.2013-624
[research_yue_wang_2013_b]: https://doi.org/10.2514/6.2013-623
[research_yukihiro_akihiko_2000]: https://doi.org/10.1541/ieejeiss1987.120.11_1644
[research_yukish_valenti_2020]: https://doi.org/10.2514/1.c035586
[research_yumaprovinggroundaz_2013]: https://doi.org/10.21236/ada568947
[research_yumatestcenteryumaprovinggroundaz_2008]: https://doi.org/10.21236/ada503063
[research_zadniprovsky_konotop_2025]: https://doi.org/10.20535/0203-3771502025347458
[research_zaeski_2018]: https://doi.org/10.7862/rz.2018.mmr.20
[research_zafi_chakraborty_2023]: https://doi.org/10.2514/6.2023-3663
[research_zaimis_carpentari_2024]: https://doi.org/10.1115/gt2024-126351
[research_zakrajsek_vogel_2017]: https://doi.org/10.2514/6.2017-0352
[research_zandberg_2001]: https://doi.org/10.21236/ada385919
[research_zandbergen_barbeau_2011]: https://doi.org/10.1017/s0373463311000051
[research_zappa_gordon_2011]: https://doi.org/10.21236/ada553770
[research_zehner_2001]: https://doi.org/10.21236/ada399750
[research_zelenkov_golik_2014]: https://doi.org/10.18372/1990-5548.39.7336
[research_zeng_li_2025]: https://doi.org/10.1007/978-981-96-2240-5_37
[research_zhai_li_2025]: https://doi.org/10.23919/ccc64809.2025.11179589
[research_zhai_qi_2012]: https://doi.org/10.1109/sopo.2012.6270470
[research_zhang_2018]: https://doi.org/10.1109/icnsurv.2018.8384984
[research_zhang_2021]: https://doi.org/10.1007/s10291-021-01179-y
[research_zhang_2025]: https://doi.org/10.1109/iccnse66404.2025.11144354
[research_zhang_chai_2022]: https://doi.org/10.21203/rs.3.rs-2248799/v1
[research_zhang_chen_2023]: https://doi.org/10.1007/978-981-19-6613-2_436
[research_zhang_chen_2026]: https://doi.org/10.2139/ssrn.6582445
[research_zhang_chen_2026_b]: https://doi.org/10.1016/j.ast.2026.112946
[research_zhang_cui_2013]: https://doi.org/10.4028/www.scientific.net/amm.473.46
[research_zhang_dou_2024]: https://doi.org/10.1109/icrca60878.2024.10649174
[research_zhang_fang_2026]: https://doi.org/10.3390/electronics15061333
[research_zhang_guo_2024]: https://doi.org/10.1109/isstc63573.2024.10824167
[research_zhang_he_2026]: https://doi.org/10.1016/j.cja.2025.103811
[research_zhang_he_2026_b]: https://doi.org/10.1016/j.cja.2025.103582
[research_zhang_huang_2023]: https://doi.org/10.1016/j.cja.2023.03.017
[research_zhang_li_2017]: https://doi.org/10.1109/nana.2017.36
[research_zhang_li_2020]: https://doi.org/10.23919/ccc50068.2020.9188393
[research_zhang_li_2023]: https://doi.org/10.1016/b978-0-443-13283-4.00003-2
[research_zhang_li_2024]: https://doi.org/10.1108/aeat-08-2023-0217
[research_zhang_lin_2015]: https://doi.org/10.2514/6.2015-1111
[research_zhang_lin_2023]: https://doi.org/10.2139/ssrn.4673118
[research_zhang_liu_2016]: https://doi.org/10.1155/2016/4892376
[research_zhang_ma_2025]: https://doi.org/10.3390/act14030114
[research_zhang_mehrjerdi_2013]: https://doi.org/10.1109/icuas.2013.6564798
[research_zhang_morton_2013]: https://doi.org/10.1002/navi.33
[research_zhang_niu_2012]: https://doi.org/10.1109/plans.2012.6236908
[research_zhang_peng_2022]: https://doi.org/10.1017/aer.2022.1
[research_zhang_peng_2022_b]: https://doi.org/10.1016/j.ast.2022.107864
[research_zhang_qin_2026]: https://doi.org/10.54097/f31pre98
[research_zhang_shan_2017]: https://doi.org/10.1360/n092016-00329
[research_zhang_shuang_2018]: https://doi.org/10.1007/s12555-017-0454-y
[research_zhang_song_2025]: https://doi.org/10.1016/j.cja.2025.103463
[research_zhang_su_2021]: https://doi.org/10.1109/ccdc52312.2021.9601405
[research_zhang_wang_2021]: https://doi.org/10.1109/ifeea54171.2021.00164
[research_zhang_wang_2023]: https://doi.org/10.1016/j.cja.2023.01.006
[research_zhang_wang_2023_b]: https://doi.org/10.1186/s43020-023-00099-1
[research_zhang_wang_2023_c]: https://doi.org/10.2139/ssrn.4598457
[research_zhang_wang_2023_d]: https://doi.org/10.1007/978-981-19-6613-2_516
[research_zhang_wang_2025]: https://doi.org/10.1109/safeprocess67117.2025.11267806
[research_zhang_wang_2025_b]: https://doi.org/10.1360/sst-2024-0133
[research_zhang_yang_2008]: https://doi.org/10.1109/ivs.2008.4621224
[research_zhang_yang_2013]: https://doi.org/10.4028/www.scientific.net/amr.760-762.457
[research_zhang_yang_2023]: https://doi.org/10.1109/iscer58777.2023.00059
[research_zhang_yang_2026]: https://doi.org/10.1016/j.applthermaleng.2025.129428
[research_zhang_zhai_2019]: https://doi.org/10.3390/s19020408
[research_zhang_zhai_2019_b]: https://doi.org/10.1109/access.2019.2893062
[research_zhang_zhang_2012]: https://doi.org/10.1109/bcgin.2012.159
[research_zhang_zhang_2020]: https://doi.org/10.1016/j.actaastro.2019.11.012
[research_zhang_zhang_2020_b]: https://doi.org/10.1109/icuas48674.2020.9213901
[research_zhang_zhang_2022]: https://doi.org/10.23919/ccc55666.2022.9902473
[research_zhang_zhang_2022_b]: https://doi.org/10.23919/ccc55666.2022.9901754
[research_zhang_zhang_2023]: https://doi.org/10.1007/s10291-023-01485-7
[research_zhang_zhao_2016]: https://doi.org/10.1109/chicc.2016.7554234
[research_zhang_zhao_2023]: https://doi.org/10.3390/aerospace10120981
[research_zhang_zhao_2025]: https://doi.org/10.1109/tase.2024.3363838
[research_zhang_zhu_2025]: https://doi.org/10.23919/ccc64809.2025.11179339
[research_zhang_zou_2014]: https://doi.org/10.1109/chicc.2014.6896001
[research_zhao_currier_2018]: https://doi.org/10.1109/icuas.2018.8453381
[research_zhao_duan_2021]: https://doi.org/10.1109/icuas51884.2021.9476886
[research_zhao_kapania_2019]: https://doi.org/10.2514/1.j057892
[research_zhao_khanafseh_2023]: https://doi.org/10.1109/plans53410.2023.10140122
[research_zhao_krishnamurthi_2018]: https://doi.org/10.23919/acc.2018.8430942
[research_zhao_krishnamurthi_2018_b]: https://doi.org/10.4050/f-0074-2018-12907
[research_zhao_li_2012]: https://doi.org/10.1109/eml.2012.6325115
[research_zhao_li_2017]: https://doi.org/10.18280/ama_c.720104
[research_zhao_liu_2023]: https://doi.org/10.1088/1742-6596/2513/1/012009
[research_zhao_mishra_2019]: https://doi.org/10.4050/f-0075-2019-14750
[research_zhao_qiu_2016]: https://doi.org/10.1016/j.measurement.2015.11.008
[research_zhao_zeng_2023]: https://doi.org/10.1016/j.ast.2023.108287
[research_zhao_zhou_2024]: https://doi.org/10.2139/ssrn.4862138
[research_zhao_zhu_2016]: https://doi.org/10.1109/icuas.2016.7502671
[research_zhen_peng_2019]: https://doi.org/10.1109/access.2019.2957740
[research_zhen_tao_2018]: https://doi.org/10.23919/chicc.2018.8483143
[research_zhen_yu_2020]: https://doi.org/10.1109/taes.2019.2924134
[research_zheng_gong_2013]: https://doi.org/10.1007/978-3-642-45037-2_57
[research_zheng_qiaoqiao_2014]: https://doi.org/10.1109/cgncc.2014.7007289
[research_zheng_qu_2026]: https://doi.org/10.2514/1.c038372
[research_zheng_wang_2019]: https://doi.org/10.1109/icus48101.2019.8995983
[research_zhicong_voronko_2023]: https://doi.org/10.36074/grail-of-science.17.02.2023.070
[research_zhijinzhao_qigao_2006]: https://doi.org/10.1049/cp:20061541
[research_zhilanxiong_yanlinghao]: https://doi.org/10.1109/icma.2005.1626643
[research_zhimin_guanxin_2008]: https://doi.org/10.2514/6.2008-6335
[research_zhimin_guanxin_2013]: https://doi.org/10.19026/rjaset.5.4818
[research_zhimin_guanxin_2013_b]: https://doi.org/10.19026/rjaset.5.4544
[research_zhimin_guanxin_2014]: https://doi.org/10.19026/rjaset.7.613
[research_zhiqiang_wu_2017]: https://doi.org/10.23919/chicc.2017.8027812
[research_zhiwen_xiaoping_2013]: https://doi.org/10.1109/cac.2013.6775762
[research_zhong_xu_2018]: https://doi.org/10.1109/icnsurv.2018.8384892
[research_zhong_xu_2018_b]: https://doi.org/10.1109/icnsurv.2018.8384985
[research_zhongfei_lijun_2025]: https://doi.org/10.1109/iccasit66611.2025.11348723
[research_zhou_2016]: https://doi.org/10.1515/freq-2015-0279
[research_zhou_bao_2015]: https://doi.org/10.3390/app5041457
[research_zhou_dong_2022]: https://doi.org/10.1109/cac57257.2022.10055837
[research_zhou_dong_2023]: https://doi.org/10.1002/rnc.6571
[research_zhou_huang_2019]: https://doi.org/10.1177/0954410019877715
[research_zhou_huang_2020]: https://doi.org/10.1016/j.cja.2019.08.004
[research_zhou_jiang_2017]: https://doi.org/10.23919/chicc.2017.8027779
[research_zhou_knedlik_2010]: https://doi.org/10.1017/s0373463310000068
[research_zhou_kuang_2020]: https://doi.org/10.1360/ssi-2019-0196
[research_zhou_liu_2024]: https://doi.org/10.1007/978-981-97-6199-9_2
[research_zhou_wan_2017]: https://doi.org/10.1109/robio.2017.8324798
[research_zhou_wang_2022]: https://doi.org/10.3390/drones6070182
[research_zhou_wang_2023]: https://doi.org/10.3390/drones7070431
[research_zhou_yang_2011]: https://doi.org/10.2514/6.2011-6488
[research_zhou_zeng_2018]: https://doi.org/10.1155/2018/2105682
[research_zhou_zhang_2022]: https://doi.org/10.1117/12.2631651
[research_zhou_zhang_2024]: https://doi.org/10.1109/aaac63570.2024.11027352
[research_zhu_2024]: https://doi.org/10.1117/12.3039854
[research_zhu_bordner_2025]: https://doi.org/10.2514/6.2025-1460
[research_zhu_jin_2016]: https://doi.org/10.1109/ccdc.2016.7532153
[research_zhu_lai_2006]: https://doi.org/10.1007/s00190-006-0096-y
[research_zhu_lu_2018]: https://doi.org/10.23919/chicc.2018.8483411
[research_zhu_lu_2019]: https://doi.org/10.3390/app9153079
[research_zhu_lung_2020]: https://doi.org/10.1145/3403746.3403911
[research_zhu_qiu_2013]: https://doi.org/10.1109/imccc.2013.324
[research_zhu_shi_2023]: https://doi.org/10.1007/978-981-19-6613-2_27
[research_zhu_yang_2020]: https://doi.org/10.1016/j.compeleceng.2020.106637
[research_zhu_zhang_2017]: https://doi.org/10.1108/aeat-10-2015-0224
[research_zhu_zhang_2022]: https://doi.org/10.3390/app12020785
[research_zhu_zhao_2012]: https://doi.org/10.1109/imccc.2012.162
[research_zhu_zhu_2026]: https://doi.org/10.2514/1.c038900
[research_zhubin_kepeng_2018]: https://doi.org/10.1049/cp.2018.0220
[research_zhuqidan_wangtong_2009]: https://doi.org/10.1109/ccdc.2009.5191918
[research_zhuqidan_wangtong_2009_b]: https://doi.org/10.1109/ccdc.2009.5194878
[research_zink]: https://doi.org/10.31274/rtd-180813-16429
[research_zolanvari_teixeira_2018]: https://doi.org/10.1109/icuas.2018.8453394
[research_zou_devasia_2000]: https://doi.org/10.2514/6.2000-4051
[research_zou_devasia_2006]: https://doi.org/10.2514/6.2006-6241
[research_zou_song_2020]: https://doi.org/10.1109/ccdc49329.2020.9164526
[research_zou_yin_2017]: https://doi.org/10.1109/ccsse.2017.8087893
[research_zou_zhen_2026]: https://doi.org/10.2139/ssrn.6802811
[research_zuo_xu_2023]: https://doi.org/10.1016/j.asr.2023.04.019
[research_zvyagina_mordovin_2026]: https://doi.org/10.18572/1812-3791-2026-9-46-50
