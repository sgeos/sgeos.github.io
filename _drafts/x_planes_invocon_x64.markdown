---
layout: post
mathjax: true
comments: true
title:  "X-Planes: Invocon X-64"
date:   2025-12-09 09:00:00 +0000
categories: aerospace history engineering
series: x_planes
series_title: X-Planes
series_index: 65
---
<!-- A361 -->
<script>console.log("A361");</script>

This is the sixty-fifth article in the [X-Planes series][related_post_a297_framing], following the [X-1][related_post_a298_bell_x1], the [X-2][related_post_a299_bell_x2], the [X-3][related_post_a300_douglas_x3], the [X-4][related_post_a301_northrop_x4], the [X-5][related_post_a302_bell_x5], the [X-6][related_post_a303_convair_x6], the [X-7][related_post_a304_lockheed_x7], the [X-8][related_post_a305_aerojet_x8], the [X-9][related_post_a306_bell_x9], the [X-10][related_post_a307_north_american_x10], the [X-11][related_post_a308_convair_x11], the [X-12][related_post_a309_convair_x12], the [X-13][related_post_a310_ryan_x13], the [X-14][related_post_a311_bell_x14], the [X-15][related_post_a312_north_american_x15], the [X-16][related_post_a313_bell_x16], the [X-17][related_post_a314_lockheed_x17], the [X-18][related_post_a315_hiller_x18], the [X-19][related_post_a316_curtiss_wright_x19], the [X-20][related_post_a317_boeing_x20], the [X-21][related_post_a318_northrop_x21], the [X-22][related_post_a319_bell_x22], the [X-23][related_post_a320_martin_marietta_x23], the [X-24][related_post_a321_martin_marietta_x24], the [X-25][related_post_a322_bensen_x25], the [X-26][related_post_a323_schweizer_x26], the [X-27][related_post_a324_lockheed_x27], the [X-28][related_post_a325_osprey_x28], the [X-29][related_post_a326_grumman_x29], the [X-30][related_post_a327_rockwell_x30], the [X-31][related_post_a328_rockwell_mbb_x31], the [X-32][related_post_a329_boeing_x32], the [X-33][related_post_a330_lockheed_martin_x33], the [X-34][related_post_a331_orbital_sciences_x34], the [X-35][related_post_a332_lockheed_martin_x35], the [X-36][related_post_a333_mcdonnell_douglas_x36], the [X-37][related_post_a334_boeing_x37], the [X-38][related_post_a335_scaled_composites_x38], the [X-39][related_post_a336_x39_reserved_never_assigned], the [X-40][related_post_a337_boeing_x40], the [X-41][related_post_a338_x41_common_aero_vehicle], the [X-42][related_post_a339_orbital_sciences_x42], the [X-43][related_post_a340_micro_craft_x43], the [X-44][related_post_a341_x44_two_aircraft], the [X-45][related_post_a342_boeing_x45], the [X-46][related_post_a343_boeing_x46], the [X-47][related_post_a344_northrop_grumman_x47], the [X-48][related_post_a345_boeing_x48], the [X-49][related_post_a346_piasecki_x49], the [X-50][related_post_a347_boeing_x50], the [X-51][related_post_a348_boeing_x51], the [X-52][related_post_a349_x52_designation_refused], the [X-53][related_post_a350_boeing_x53], the [X-54][related_post_a351_gulfstream_x54], the [X-55][related_post_a352_lockheed_martin_x55], the [X-56][related_post_a353_lockheed_martin_x56], the [X-57][related_post_a354_esaero_x57_maxwell], the [X-58][related_post_a355_x58_slot_taken_by_xq58], the [X-59][related_post_a356_x59_quesst], the [X-60][related_post_a357_generation_orbit_x60], the [X-61][related_post_a358_dynetics_x61_gremlins], the [X-62][related_post_a359_lockheed_martin_x62_vista], and the [X-63][related_post_a360_abl_space_systems_x63].

**The register describes this vehicle in one hundred and one characters that it also uses for a different vehicle, and the laboratory that paid for both says they are not alike.**

The X-64A was allocated on 20 April 2022 to a team of three companies led by Invocon Incorporated, with KT Engineering and Troy7 Incorporated \[[Invocon X-64][ref_ds_x64]\] \[[ABL Space Systems X-63][ref_ds_x63]\]. [The previous article][related_post_a360_abl_space_systems_x63] took the other half of the same allocation, the X-63A of ABL Space Systems, and established that the two rows share their date, their sponsor cell, their engines cell and every character of their description \[[DOD 4120.15-L Addendum][ref_mds_addendum]\].

> Demonstrator rocket for AFRL's *ARISE* (Aerospike Rocket Integration and Suborbital Experiment) program

That is the whole of what the register says about either machine. **This article is about what the register conceals**, which is a vehicle of a different shape, built by a team of a different trade, to answer the half of the question its sibling cannot answer alone.

## The Research Question

**An aerospike nozzle is worth between five and eight percent of first-stage impulse, and the question this vehicle exists to settle is whether five to eight percent can be seen from the ground.**

[The previous article][related_post_a360_abl_space_systems_x63] computed the prize. On the published reference trajectory of the parent vehicle, an ideal altitude-compensating nozzle delivers between 5.3 and 8.5 percent more first-stage impulse than the best fixed nozzle that trajectory admits. **That is a number about thermodynamics and it says nothing about instruments.**

A flight test does not measure impulse. It measures whatever its transducers measure, and then somebody reconstructs impulse from that. So the questions here are these. **What does an instrument on a rocket actually observe, and what has to be assumed to turn that observation into thrust?** How accurate must each assumption be before a five percent effect is distinguishable from the error in the measurement of it? What does a finite ring of sensors on an annular nozzle fail to see? And what does it mean that this vehicle, unlike its sibling, is designed to come back?

**The answers are sharper than the programme's own language suggests, and one of them is reassuring.** The observable is not thrust but thrust minus drag, so recovering thrust requires a drag model and the accuracy of that model sets the accuracy of the whole experiment. **The drag term is the only one nothing on board measures.** But the signal is collected early and the drag confounder peaks late, so by the time drag is at its worst the measurement is largely already banked. And the vehicle's own published dimensions, of which there are exactly two, say that it was shaped for recovery rather than for ascent.

## Programme Origin

**The programme reached the register as a finished arrangement, and its origin lies in an award made well before the designation.** The award was a three-year other transaction agreement made in December 2019 with a team led by Invocon Incorporated \[[AFRL awards agreements under ARISE][ref_arise_award]\]. The designation was allocated on 20 April 2022, on the same day as the X-63A \[[DOD 4120.15-L Addendum][ref_mds_addendum]\]. The Air Force Research Laboratory's background document, cleared in September 2022, places the vehicle in a portfolio whose stated goals are development time and development cost rather than performance \[[AFRL's Rocket Lab Past, Present and Future][ref_rocketlab]\]. **The origin is therefore read from four records, being the register, the laboratory's background document, the award announcement and the federal award record of the three companies** \[[USAspending][ref_usaspending]\], and the subsections that make up this section read them in turn.

### The Register Row, Read From the Other Side

The addendum to the joint designation handbook gives the X-64A a row identical to the X-63A's in every cell that describes the machine, differing only in the contractor \[[DOD 4120.15-L Addendum][ref_mds_addendum]\].

| Designation | Allocated | Contractor | Engines cell | Sponsor | Description marked as a reconstruction |
|---|---|---|---|---|---|
| X-63A | 20-Apr-22 | ABL Space Systems | `1 rocket engine` | USAF/USSF | yes |
| X-64A | 20-Apr-22 | Invocon, KT Engineering, Troy7 | `1 rocket engine` | USAF/USSF | yes |

[The previous article][related_post_a360_abl_space_systems_x63] established the three facts that row carries. **Eleven descriptions repeat somewhere in the 539 rows of that register and this pair is the only repeat among the thirty-one rows whose designation begins with the letter X.** The sponsor cell reads `USAF/USSF`, which **only these two rows in the whole register do**. And the engines cell reads `1 rocket engine`, naming a class where the register almost always names a model, which **again only these two rows do**.

**Both rows are also marked as reconstructions.** The compiler notes that for allocations after October 2018 the official description is not releasable and prints its own reading in blue. So the hundred and one characters this article opened with are a careful reader's summary of open sources and not a government statement, and the three-state officiality classification [the X-63A article][related_post_a360_abl_space_systems_x63] recomputed puts both rows in the wholly unofficial category.

**What is primary in that row is the date, the contractor names and the fact that two numbers were issued at once.** Everything describing the vehicle is secondary, and the vehicle-describing sentence is the one that is identical between the two.

### What the Laboratory Says That the Register Does Not

The Air Force Research Laboratory published a background document on its rocket propulsion organisation, cleared in September 2022, and one paragraph of it contradicts the impression the register leaves. **It names the portfolio ARISE belongs to by its initials alone, being the Affordable Responsive Modular Rocket**, and the expansion is supplied here because the passage quoted below does not carry it \[[AFRL's Rocket Lab Past, Present and Future][ref_rocketlab]\].

> Under the Aerospike Rocket Integration and Suborbital Experiment (ARISE) AFRL, working in Public Private Partnerships with Invocon and ABL Space Systems, will fly the first ever modular aerospike engine. Each company has their own launch vehicle and chosen approach to implementing the ARMR architecture. ABL's vehicle has been designated X-63 while Invocon's is designated X-64.

**The laboratory's public fact sheet for the programme says none of that**, describing the aerospike, the three wake regimes and the modular architecture without naming either designation \[[ARISE and Fly][ref_afrl_arise]\]. [The X-63A article][related_post_a360_abl_space_systems_x63] read that sheet in full and found it names its two flight-test vehicles only as `abl` and `Invocon` in a figure caption. **So the designations and the companies are tied together in the background paper and nowhere else the laboratory publishes.**

**Each company has its own launch vehicle and its own chosen approach.** That sentence is the reason this article exists as a separate piece of work rather than as a paragraph appended to its predecessor. The register assigns one description to two vehicles, and the laboratory that commissioned them says the vehicles differ in design and in approach. **A designation register is a naming instrument and not a technical one**, and this is what that distinction costs a reader who has only the register.

Two further things fall out of the same paragraph. **The document ties each designation to its company in a government publication**, which the register does only through the contractor cell. And **it calls the instrument a Public Private Partnership**, where the award announcement calls it an other transaction agreement executed through the Space Enterprise Consortium \[[AFRL awards agreements under ARISE][ref_arise_award]\]. Those are not in conflict. A public private partnership is a description of the relationship and an other transaction agreement is the legal vehicle for it, and [the article on the sibling designation][related_post_a360_abl_space_systems_x63] established that the second is why neither award appears in the federal procurement record.

### The Team, and What the Award Record Says Each Member Does

The award announcement describes the lead contractor in one sentence \[[AFRL awards agreements under ARISE][ref_arise_award]\].

> Invocon is a veteran-owned small business that provides turnkey instrumentation and control solutions for demanding applications in extreme environments and has teamed with KT Engineering and Troy7 for their unique capabilities.

**The prime contractor for a rocket is an instrumentation house.** That is the single most informative fact about this vehicle, and the award record confirms it at length rather than leaving it as a self-description.

Searching the federal award reporting system by recipient name across five families of award type returns **81 rows for Invocon**, and their descriptions are the descriptions of a measurement company \[[USAspending][ref_usaspending]\]. An internal and external wireless instrumentation system. Hypervelocity impact detection, location and assessment. A radiation environment monitor, twice, under the small business research programme. A micro-wireless instrumentation system design and development. A blanket agreement for miscellaneous data acquisition equipment and networking. **The largest single row is mission support for the Navy at 3,053,408 dollars and 20 cents**, and the company founded in 1985 describes itself as four decades of precision instrumentation from Conroe, Texas \[[Invocon, About Us][ref_invocon_about]\].

**KT Engineering's record is not instrumentation. It is this programme's own architecture, a decade early.**

| Company | Role named in the announcement | Award rows | Largest row | What the largest row is for |
|---|---|---|---|---|
| Invocon | lead, turnkey instrumentation and control | 81 | 3,053,408.20 dollars | mission support for the Navy |
| KT Engineering | unique capabilities | 15 | 6,571,144.00 dollars | segmented launch vehicle manufacturing development and demonstration |
| Troy7, as `Troy 7` | unique capabilities | 15 | 2,889,435.00 dollars | a hypersonic control system |
| Troy7, as `Troy7` | unique capabilities | 0 | none | the spelling returns nothing |

Fifteen rows return for KT Engineering and the largest of them is a **segmented launch vehicle manufacturing development and demonstration programme** at 6,571,144 dollars, followed by **crew exploration vehicle propulsion advanced development** of a 7,500 pound force vacuum engine at 4,186,522 dollars. Two further rows are third-phase small business awards for a **radially segmented launch vehicle** \[[USAspending][ref_usaspending]\]. **Asking the award record for `segmented launch vehicle` returns seven rows and every one of them is this company's.** The modular architecture ARISE exists to fly has been a funded line of work under one of the X-64A's own subcontractors since at least 2004.

**Troy7's record is control, and finding it at all depends on a space.**

The announcement writes the company `Troy7` and the award record writes it `TROY 7, INC.` \[[AFRL awards agreements under ARISE][ref_arise_award]\] \[[USAspending][ref_usaspending]\]. **The keyword `Troy7` returns nothing in any of the five award families. The keyword `Troy 7` returns fifteen rows.** The largest is a research and development contract for a **hypersonic control system** at 2,889,435 dollars. So the team divides into instrumentation, propulsion and control, and one third of it is invisible to a search that spells its name the way its own customer spells it.

**That is the same class of defect [the previous article][related_post_a360_abl_space_systems_x63] found in a fetcher.** There a page parameter passed as an encoded object returned ten records where the server held 242, and the repair was a spelling. **Here a company name passed without a space returns nothing where the record holds fifteen.** A name is a query, and a query is only as good as its spelling.

**The spaced spelling also imports the collision the unspaced one avoided.** Among those fifteen rows are a router backup belonging to a different company and a seven-inch drop-in rail belonging to a third, both matched because `Troy 7` occurs inside `TROY 7" DROP-IN RAIL` and inside a product name. **A more findable query is a less precise one**, and both halves of that trade have to be stated for the count to mean anything.

### The Programme's Own Numbers, Which Are About Cost Rather Than Thrust

[The previous article][related_post_a360_abl_space_systems_x63] observed that the modularity half of ARISE is a claim about cost and schedule rather than about performance, and said the fact sheet did not quantify it. **The background document does quantify it** \[[AFRL's Rocket Lab Past, Present and Future][ref_rocketlab]\].

> The goal of the ARMR portfolio is to radically change the current space access engine design paradigm. We seek to reduce the development time for a new engine by 70% and reduce the development cost by 50%.

**Seventy percent off the schedule and fifty percent off the cost.** Those are the numbers the modular architecture is accountable to, and neither is a thrust or an impulse. An engine assembled from many copies of one small module is an argument about how many distinct components have to be designed, qualified and tolerated, and the portfolio states its target as a factor of about three and a third in time and two in money.

The same document places ARISE at the end of a lineage that the laboratory names and dates.

| Programme | Years the document gives | What it aimed at | How far it got |
|---|---|---|---|
| Integrated Powerhead Demonstrator | 1994 to 2006 | 200 mission life, 100 mean time between overhaul, twenty times the Space Shuttle | the world's first full-flow staged combustion engine, demonstrated |
| Upper Stage Engine Technology | from 2004 | a modernised upper-stage industrial base and better analysis tools | technologies now in several commercial engines, over 150 tool transitions |
| Hydrocarbon Boost Demonstrator | from 2007 | to beat the RD-180 on performance and reusability, 200 mission life | a preburner rather than a full engine |
| Third Generation Reusable Booster | named, not dated | a reusable booster | leveraged into the portfolio that follows |
| Affordable Responsive Modular Rocket | present at the 2022 clearance | 70 percent less development time, 50 percent less development cost | ARISE, being the two vehicles of this article and the last |

**Two of those predecessors carried quantified reusability goals and neither reached a flying engine.** The integrated powerhead demonstrator ran from 1994 to 2006, demonstrated what the document calls the world's first full-flow staged combustion engine, and aimed at 200 mission life and 100 mean time between overhaul. The hydrocarbon boost programme began in 2007 with the same 200 mission life target and **progressed only far enough to demonstrate a preburner rather than a full engine**, which the document states plainly while also calling the programme an outstanding success on the strength of requests for information about its technologies.

**One phrase in that document is worth recording because it recurs.** It says twice that a programme sought to bring a part of the industry `into the 22nd century`, once of the modelling tools and once of the upper-stage industrial base. A document cleared in 2022 describing work of 2004 and 2007 almost certainly means the twenty-first. **It is a slip rather than an ambiguity**, and it is noted here because this series quotes primaries verbatim and a reader meeting the phrase in the original should know it was not corrected in transit.

**A second slip in the same document is a matter of chemistry.** Describing the move from the Atlas to the Titan it says the laboratory experimented with switching to nitrogen tetroxide and Aerozine 50, and then in the next sentence discusses the storability of nitrogen tetroxide and monomethylhydrazine. **Aerozine 50 and monomethylhydrazine are not the same fuel**, the first being a half-and-half blend of hydrazine and unsymmetrical dimethylhydrazine, and the Titan II burned the blend. The storability argument the paragraph makes holds for either, which is presumably why the substitution passed.

## Sizing From First Principles

**Sizing this vehicle from first principles means sizing two things, and the record supports arithmetic for one and a requirement for the other.** The first is the vehicle itself, of which two approximate dimensions are published and nothing else, so its geometry can be computed while its mass, thrust and drag coefficient cannot \[[Invocon X-64][ref_ds_x64]\]. The second is the experiment the vehicle was to carry, which can be sized even where the vehicle cannot, because the accuracy a drag model must have follows from the drag fraction, the size of the effect and the instrument errors alone. **What is computed is therefore the geometry the two numbers fix and the accuracy the measurement demands**, with the drag fraction left as a variable because no published figure fixes it.

### The Shape, Which Is the Whole of What Was Published

**Two numbers describe this vehicle and they are enough to say what it was for.**

The encyclopedia entry reports, from the contractor's own release about the contract award, that the vehicle is apparently recoverable, that it lands on a gear of four legs which function as stabilising fins during flight and presumably rotate downward before landing, and that it stands about 12 metres tall with a diameter of about 2.4 metres \[[Invocon X-64][ref_ds_x64]\]. **The entry states in its own voice that only little public information about the X-64A is available and that detailed physical characteristics are not yet available.** That is the whole specification.

**The contractor's release has not been read by this article.** The live company site no longer carries it and the archive returned no capture, so the physical description above is taken at second hand from an entry that names the release as its source, and that is stated here rather than smoothed over. **What follows is arithmetic on two numbers whose provenance is one remove away.**

Set those two numbers beside the parent vehicle of the sibling designation, whose payload user's guide gives 88 feet integrated length and 6 feet diameter \[[ABL Payload User's Guide][ref_abl_pug]\].

**Three elementary relations carry everything this section says**, and they are written down because every number below is one of them evaluated twice. Let $L$ be the length in metre, $D_b$ the body diameter in metre, $f$ the fineness ratio \[[fineness ratio][ref_fineness]\], dimensionless, $A$ the reference frontal area in square metre, $S$ the wetted side area of the equivalent cylinder in square metre, and $V_c$ its enclosed volume in cubic metre.

$$ f \equiv \frac{L}{D_b}, \qquad A = \frac{\pi D_b^2}{4}, \qquad S = \pi D_b L, \qquad V_c = A L $$

**Two of the comparisons below are therefore not independent measurements but consequences**, and saying which is which keeps the argument honest. Read as scaling laws at fixed shape,

$$ A \propto D_b^{2}, \qquad S \propto D_b L, \qquad V_c \propto D_b^{2} L $$

**The frontal-area ratio is the square of the diameter ratio and nothing else.** So the figure of 1.72 quoted below is 1.3123 squared, and the volume ratio of 0.7705 is that same 1.72 multiplied by the length ratio of 0.4474. **Neither is a separate fact about the vehicles**, and a reader who checked them against each other would find them consistent by construction rather than by agreement.

| Quantity | X-64A | RS1, the sibling's parent | Ratio |
|---|---|---|---|
| Length | 12.0 metre | 26.8224 metre | 0.4474 |
| Diameter | 2.4 metre | 1.8288 metre | 1.3123 |
| Fineness ratio | 5.00 | 14.6667 | 2.9333 |
| Frontal area | 4.5239 square metre | 2.6268 square metre | 1.7222 |
| Cylinder volume | 54.29 cubic metre | 70.46 cubic metre | 0.7705 |
| Wetted side area | 90.48 square metre | 154.10 square metre | 0.5871 |
| One calibre of static margin, as a share of length | 20.0 percent | 6.8 percent | 2.9333 |

**The X-64A is 44.7 percent of the RS1's length and 131.2 percent of its diameter.** Its fineness ratio, being length divided by diameter, is **5.0** against the RS1's **14.67**, so the parent vehicle is **2.93 times as slender**. Both published figures for the X-64A are approximate and both are round in both unit systems, forty feet by eight and twelve metres by two point four, so **the exactness of 5.0 is an artefact of the rounding and the honest statement is a fineness ratio of about five**.

A fineness ratio of five is not a launch-vehicle proportion. It is nearer to that of a lander or an early sounding rocket, and its consequences are arithmetic.

**The frontal area is 4.524 square metres against 2.627, which is 1.72 times as much.** Pressure drag and base drag both scale with that area, so at equal mass and equal drag coefficient **this vehicle's drag force is 1.72 times its sibling's**, and that factor comes from published dimensions with no aerodynamic model in it at all.

**The drag coefficients are probably not equal either, and the asymmetry is worth stating carefully because it is a judgement rather than a derivation.** Base area is the same for a given diameter however long the body is, so the difference is not one of area. **What fineness changes is the boundary layer arriving at the base and the bluntness of the nose.** A longer body presents a thicker boundary layer at its base, which raises the base pressure and lowers base drag, so the shorter vehicle pays more of it. And a body of fineness five carries a nose of proportionally lower fineness for the same overall proportions, which raises forebody wave drag through the transonic and low supersonic range where this vehicle spends its dynamic pressure.

**Running the other way is skin friction, and it favours the short vehicle.** A cylinder of these proportions has 90.5 square metres of side area against the RS1's 154.1, so friction drag is lower by a factor of 1.70 on area alone.

**Which of those wins is not settled here.** At the Mach numbers computed below, wave and base drag are the larger contributions and friction the smaller, so the expectation is that the shorter vehicle's drag coefficient is the higher of the two. **That expectation is an inference from the ordering of drag contributions and not a computation**, so the only claim this article makes about drag without qualification is the geometric one. **The frontal-area factor of 1.72 holds at equal mass and equal drag coefficient**, and putting a number above it would need a drag model for a configuration whose contours are not public.

**And the enclosed volume says the shortness is not a matter of being a smaller vehicle.** The X-64A's cylinder holds 54.29 cubic metres against the RS1's 70.46, which is **77.1 percent of the volume in 44.7 percent of the length**. It is not a scaled-down launch vehicle. It is a differently proportioned one.

**The proportion is what a recoverable vehicle wants.** Four legs deployed from a 2.4 metre body give a footprint whose radius is a larger fraction of the vehicle's height than the same legs on a 26.8 metre body could, the centre of mass of a returning stage sits lower on a short body, and the aerodynamic surfaces that steer a descent have a shorter moment arm to work against. **Every one of those favours the short vehicle, and every one of them costs drag on the way up.** The section on the measurement shows where that cost is paid.

### The Claim, Stated Exactly

Everything that follows rests on what an instrument bolted to a rocket actually senses, and the answer is not what a reader might assume.

Let $F$ be the thrust in newton, $D$ the aerodynamic drag in newton, $m$ the instantaneous mass in kilogram, $g$ the local gravitational acceleration in metre per second squared, $\gamma$ the flight-path angle in radian and $v$ the speed in metre per second. Newton's second law along the flight path reads

$$ m \frac{\mathrm{d} v}{\mathrm{d} t} = F - D - m g \sin \gamma $$

which contains four quantities of which one is wanted and three are not. **A body-mounted accelerometer does not measure $\mathrm{d}v / \mathrm{d}t$.** It measures specific force, being the non-gravitational force per unit mass \[[proper acceleration][ref_specific_force]\], because a freely falling accelerometer reads zero. Write $a_s$ for the sensed specific force in metre per second squared. Then

$$ a_s = \frac{F - D}{m}, \qquad F = m \, a_s + D $$

**The gravitational term has vanished and it has vanished exactly.** An accelerometer's blindness to gravity, which is an inconvenience for navigation, is the property that makes it the right instrument for measuring thrust, because the largest term in the equation of motion is the one it declines to see. **That is the first thing this article wants on the page**, and it is why a thrust measurement in flight is possible at all without knowing where the vehicle is.

**One assumption is buried in that identity and it is worth digging out rather than leaving implicit.** Thrust and drag are written as though both act along the flight path, which is true at zero angle of attack and not otherwise. An accelerometer aligned with the body axis measures the body-axial component of the total non-gravitational force, and the aerodynamic force resolves onto that axis through the angle of attack. Let $\alpha$ be the angle of attack in radian, $N_a$ the aerodynamic normal force in newton, and $X_a$ the axial aerodynamic force in newton.

$$ a_s = \frac{F - X_a}{m}, \qquad X_a = D \cos \alpha - N_a \sin \alpha $$

**At zero angle of attack $X_a$ is the drag and the identity above is exact.** Away from it the normal force contributes a forward axial component, so a vehicle at angle of attack has a smaller retarding axial force than its drag, and an analysis that substituted $D$ for $X_a$ would understate the thrust it recovered.

**A gravity-turning launch vehicle flies at a small angle of attack by design**, because the pitch program exists to keep the airframe aligned with the relative wind through the dense atmosphere, so the approximation is a good one where this article uses it. **It is an approximation nonetheless**, and correcting it needs $\alpha$, which needs either an air-data measurement or a reconstruction, and this article has neither.

**What remains is a sum of three quantities and only one of them is measured directly.** The specific force is measured. **The mass is inferred rather than measured**, from an initial value and an integrated propellant flow. Let $m_0$ be the initial mass in kilogram and $\dot{m}$ the propellant mass flow in kilogram per second.

$$ m(t) = m_0 - \int_{0}^{t} \dot{m}(s) \, \mathrm{d}s $$

**That integral is why the mass error grows through the burn rather than staying where the loading scales left it.** A constant relative error in the flow measurement accumulates into an absolute mass error proportional to the propellant already spent, so the mass term in the budget below is at its worst late in the flight, which is the opposite end from where the altitude-compensation signal lives.

**The drag is neither measured nor inferred. It is modelled.**

#### This Problem Has a Literature and the Drafting Pass Engaged None of It

**Determining thrust in flight is a settled discipline with its own methodology, and it says the same thing this article has just derived.** The review of measurement error in the practice puts it plainly \[[Uncertainty of in-flight thrust determination][ref_thrust_uncertainty]\].

> While the term 'in-flight thrust determination' is used synonymously with 'in-flight thrust measurement', in-flight thrust is not directly measured but is determined or calculated using mathematical modeling relationships between in-flight thrust and various direct measurements of physical quantities.

**That is the premise of this article stated by the field twenty-five years before the programme**, and it is worth having on the page because it converts the argument above from a derivation into a confirmation. The companion review of the processes themselves surveys the analytical and ground-test routes and works three turbofan examples \[[In-flight thrust determination][ref_thrust_determination]\] \[[on a real-time basis][ref_thrust_realtime]\], and a separate study traces how measurement error propagates into a computed thrust for one engine in detail \[[Measurement effects for an F404 turbofan][ref_f404_measurement]\].

**And that literature is about air-breathing engines, which is why its method is not this one.** A turbofan's thrust cannot be reached through an accelerometer, because the inlet captures a momentum flux that depends on the flight condition, so the net propulsive force is not separable from the airframe's drag by any body-mounted instrument. **The practice therefore computes thrust from gas-path pressures and temperatures against a calibrated engine model.** A rocket carries its oxidiser and captures nothing, so the accelerometer route is open to it, and **the simplification is real rather than an oversight of the earlier work.**

**The inverse problem was solved in flight once and the way it was solved shows how entangled the two forces are.** The drag of the XB-70 was measured in flight from Mach 0.75 to 2.5, and the paper describing it is explicit that what made that possible was determining engine net thrust independently and then charging the remainder to the propulsion system \[[Techniques for determining propulsion system forces][ref_propulsion_forces]\]. **Thrust minus drag is one observable and splitting it needs a model of one or the other.** This article models the drag and recovers the thrust, where that programme modelled the thrust and recovered the drag. **Neither can have both for free.**

#### And the Established Methodology Carries a Term This Article's Budget Does Not

The methodology the field settled on is independent of how thrust is calculated and traceable to a national standards laboratory, and it enumerates what an uncertainty statement has to contain \[[Uncertainty methodology for in-flight thrust determination][ref_thrust_methodology]\] \[[its application][ref_thrust_uncertainty_app]\]. Its categories are measurement error, precision, bias, uncertainty, error estimation and classification, error propagation, ground testing, **and the related problems of model bias error, model precision error and the uncertainty limit**.

**Three of those this article does not have, and naming them is more useful than pretending otherwise.** It does not separate bias from precision, treating every term as a random contribution combined in quadrature, when a calibration offset is a bias that does not average down over a flight. **It has no model bias term at all**, which is precisely where a drag model's systematic error belongs, and a drag model's error is far more likely to be systematic than random because it comes from a wrong shape assumption rather than from noise. And it states no uncertainty limit in the methodology's sense.

**So the budget here is a sensitivity analysis rather than an uncertainty statement**, and the difference matters for how its conclusions should be read. **It says correctly how the answer's sensitivity to each input scales.** It does not say, and cannot say, what the uncertainty of a real measurement would have been.

**One further point of contact is exact rather than approximate.** A single demonstrator flight is a single-sample experiment in the technical sense, meaning one that cannot be repeated enough to estimate its own scatter, and single-sample uncertainty analysis is a developed subject with its own conventions \[[Moffat 1982][ref_moffat_1982]\]. **A programme that buys one flight has bought a single sample**, and the whole apparatus of precision estimated from repetition is unavailable to it by construction.

#### The Symbols This Article Uses

| Symbol | Meaning | Unit |
|---|---|---|
| $ \alpha $ | angle of attack | radian |
| $ \Delta $ | size of the effect being measured, as a fraction | dimensionless |
| $ \delta $ | uncertainty in the quantity that follows it | that quantity's own unit |
| $ \dot{m} $ | propellant mass flow | kilogram per second |
| $ \ell $ | lever arm from the tilt axis to the footprint boundary | metre |
| $ \ell_{\max} $ | longest lever arm, straight over a leg | metre |
| $ \ell_{\min} $ | shortest lever arm, across the gap between two legs | metre |
| $ \eta_\ell $ | ratio of aggregate data rate to downlink capacity | dimensionless |
| $ \gamma $ | flight-path angle above the horizontal | radian |
| $ \hat{A}_\mu $ | estimate of the cosine coefficient from a finite ring of sensors | the measurand's own unit |
| $ \hat{B}_\mu $ | estimate of the sine coefficient from a finite ring of sensors | the measurand's own unit |
| $ \kappa $ | ratio of specific heats of air, written gamma by A360 | dimensionless |
| $ \lambda $ | temperature lapse rate of an atmospheric layer | kelvin per metre |
| $ \mathcal{R} $ | aggregate data rate | bit per second |
| $ \mathcal{R}_\ell $ | downlink capacity | bit per second |
| $ \mu $ | azimuthal harmonic index | dimensionless |
| $ \mu_{\max} $ | highest azimuthal harmonic resolvable in both phases | dimensionless |
| $ \phi $ | direction in which the vehicle tilts | radian |
| $ \Psi $ | the measurand distributed around the annulus | its own unit |
| $ \psi $ | initial thrust-to-weight ratio | dimensionless |
| $ \rho $ | atmospheric mass density | kilogram per cubic metre |
| $ \theta $ | tilt angle from the vertical | radian |
| $ \theta_k $ | angular position of leg k on the ring | radian |
| $ \theta_{\mathrm{tip}} $ | tilt angle at which the vehicle tips over | radian |
| $ \varphi $ | phase of an azimuthal harmonic | radian |
| $ \vartheta $ | azimuthal angle around the annulus | radian |
| $ A $ | reference frontal area | square metre |
| $ a $ | angle from the nearest leg | radian |
| $ A_0 $ | mean of the measurand around the annulus | the measurand's own unit |
| $ A_\mu $ | cosine coefficient of azimuthal harmonic mu | the measurand's own unit |
| $ a_s $ | specific force sensed by a body-mounted accelerometer | metre per second squared |
| $ b $ | bits per sample | dimensionless |
| $ B $ | ballistic coefficient, being initial mass over drag area | kilogram per square metre |
| $ B_\mu $ | sine coefficient of azimuthal harmonic mu | the measurand's own unit |
| $ c $ | speed of sound in the atmosphere | metre per second |
| $ C_D $ | drag coefficient | dimensionless |
| $ C_{N\alpha,\,\mathrm{body}} $ | that slope for the cylindrical body alone | per radian |
| $ C_{N\alpha,\,\mathrm{nose}} $ | that slope for the nose alone | per radian |
| $ C_{N\alpha} $ | normal-force coefficient slope, referenced to the frontal area | per radian |
| $ D $ | aerodynamic drag | newton |
| $ d $ | drag fraction, being drag divided by thrust | dimensionless |
| $ D_b $ | body diameter | metre |
| $ d_{\mathrm{crit}} $ | drag fraction at which the total error equals the effect | dimensionless |
| $ F $ | thrust | newton |
| $ f $ | fineness ratio, being length divided by diameter | dimensionless |
| $ f_s $ | per-channel sample rate | hertz |
| $ g $ | local gravitational acceleration | metre per second squared |
| $ g_0 $ | standard gravity | metre per second squared |
| $ h $ | geometric altitude | metre |
| $ h_0 $ | altitude at the base of an atmospheric layer | metre |
| $ H_\rho $ | density scale height of the atmosphere | metre |
| $ h_b $ | altitude at main engine cut-off | metre |
| $ H_p $ | pressure scale height of the atmosphere | metre |
| $ h_s $ | support function of the footprint hull | metre |
| $ h_{cm} $ | height of the centre of mass above the ground | metre |
| $ J $ | time integral of ambient pressure over the burn | pascal second |
| $ j $ | index over the sensors on a ring | dimensionless |
| $ k $ | pitch-program exponent | dimensionless |
| $ L $ | vehicle length | metre |
| $ m $ | instantaneous vehicle mass | kilogram |
| $ M $ | Mach number | dimensionless |
| $ m_0 $ | initial vehicle mass | kilogram |
| $ m_c $ | number of sides of A360's control polygon | dimensionless |
| $ m_h $ | number of sides of the footprint hull | dimensionless |
| $ N $ | number of legs, and elsewhere the number of sensors on a ring | dimensionless |
| $ n $ | altitude-profile exponent of the model this article discards, carried over from A360 | dimensionless |
| $ N_a $ | aerodynamic normal force | newton |
| $ n_c $ | number of instrumentation channels | dimensionless |
| $ p $ | speed-profile exponent | dimensionless |
| $ p_0 $ | pressure at the base of an atmospheric layer | pascal |
| $ p_a $ | ambient atmospheric pressure | pascal |
| $ q $ | dynamic pressure | pascal |
| $ R $ | specific gas constant of air | joule per kilogram kelvin |
| $ r $ | radius of the circle of legs | metre |
| $ s $ | dummy variable of integration over time | second |
| $ S $ | wetted side area of the equivalent cylinder | square metre |
| $ S_m $ | static margin | calibre |
| $ T $ | atmospheric temperature | kelvin |
| $ t $ | time from liftoff | second |
| $ T_0 $ | temperature at the base of an atmospheric layer | kelvin |
| $ t_1 $ | an earlier instant in the burn | second |
| $ t_2 $ | a later instant in the burn | second |
| $ t_b $ | burn duration of the first stage | second |
| $ V $ | data volume written over a burn | byte |
| $ v $ | speed along the flight path | metre per second |
| $ v_b $ | speed at main engine cut-off | metre per second |
| $ V_c $ | enclosed volume of the equivalent cylinder | cubic metre |
| $ X_a $ | axial component of the aerodynamic force | newton |
| $ x_{cm} $ | axial position of the centre of mass | metre |
| $ x_{cp} $ | axial position of the centre of pressure | metre |

**Every symbol above appears in the mathematics and every symbol in the mathematics appears above**, checked by a scanner that strips the operators and the prose inside `\text` and then requires the remainder to be empty.

### The Error Budget, and the Term Nothing Measures

Treat the three errors as independent and propagate them through $F = m a_s + D$. Let $\delta$ denote the uncertainty in whatever follows it. Then

$$ \left( \delta F \right)^2 = \left( a_s \, \delta m \right)^2 + \left( m \, \delta a_s \right)^2 + \left( \delta D \right)^2 $$

Divide by $F^2$ and introduce the drag fraction $d \equiv D / F$, dimensionless. Because $m a_s = F - D = (1 - d) F$, the mass and accelerometer terms both carry that factor while the drag term carries $d$.

$$ \left( \frac{\delta F}{F} \right)^2 = \left( 1 - d \right)^2 \left[ \left( \frac{\delta m}{m} \right)^2 + \left( \frac{\delta a_s}{a_s} \right)^2 \right] + d^2 \left( \frac{\delta D}{D} \right)^2 $$

**That is the whole budget and its structure is the finding.** The two terms a designer can improve by buying better instruments are attenuated by $1 - d$, which is close to one. **The term that cannot be improved by any instrument on the vehicle is amplified by $d$**, which is small, so the drag model's accuracy is multiplied by a small number before it reaches the answer. Whether that is enough is an arithmetic question rather than a matter of opinion.

**Two limits are worth reading off before any numbers.** At $d = 0$, which is flight in vacuum, the drag model drops out entirely and the measurement is as good as the mass bookkeeping and the accelerometer. At $d = 1$, which is a vehicle whose drag equals its thrust and therefore is not accelerating, the instruments drop out entirely and the answer is whatever the drag model says. **A launch vehicle spends its first minute somewhere between those, closer to the first, and the whole question is how much closer.**

#### The Floor, Which Exists Even in Vacuum

Set the drag error to zero and the budget collapses to the instrument terms alone.

$$ \frac{\delta F}{F}\Big\rvert_{d = 0} = \sqrt{ \left( \frac{\delta m}{m} \right)^2 + \left( \frac{\delta a_s}{a_s} \right)^2 } $$

| Mass bookkeeping | Accelerometer | Thrust error at zero drag | As a share of a 5.3 percent effect |
|---|---|---|---|
| 1.0 percent | 0.5 percent | 1.118 percent | 21.1 percent |
| 0.5 percent | 0.2 percent | 0.539 percent | 10.2 percent |
| 2.0 percent | 1.0 percent | 2.236 percent | 42.2 percent |

**Against a five point three percent effect, the instrument floor alone consumes between a tenth and two fifths of the budget.** A mass bookkeeping good to one percent and an accelerometer good to half a percent give 1.12 percent, which is 21.1 percent of the smaller of A360's two gain figures. **Tightening the instruments to half a percent and two tenths of a percent gives 0.54 percent, which is 10.2 percent of it.** Loosening them to two percent and one percent gives 2.24 percent, or 42.2 percent of the effect. **So even a vehicle flying in vacuum with a perfect drag model would spend a tenth of its error budget before the atmosphere was mentioned**, and mass bookkeeping is the larger of the two contributions in every case.

### Where the Atmosphere Pushes Hardest, Which Is an Exact Condition

The drag fraction $d$ follows the dynamic pressure, so the shape of the dynamic-pressure history is what decides when the measurement is hardest.

Let $\rho$ be the atmospheric mass density in kilogram per cubic metre and $q$ the dynamic pressure \[[dynamic pressure][ref_dynamic_pressure]\] in pascal, with $C_D$ the drag coefficient, dimensionless, and $A$ the reference frontal area in square metre.

$$ q = \tfrac{1}{2} \rho v^2, \qquad D = q \, C_D A $$

The density comes from the 1976 United States Standard Atmosphere, whose defining constants give pressure and temperature by layer and from which density follows by the perfect-gas law rather than by tabulation, which is what the standard itself does \[[U.S. Standard Atmosphere 1976][ref_usatm1976]\]. Let $R$ be the specific gas constant of air in joule per kilogram kelvin and $T$ the temperature in kelvin.

$$ \rho(h) = \frac{p_a(h)}{R \, T(h)} $$

**Both of those come from the layer structure and neither is tabulated here** \[[defining constants and abbreviated tables][ref_atm_constants]\]. Let $T_0$, $p_0$ and $h_0$ be the temperature, pressure and altitude at the base of a layer, in kelvin, pascal and metre, and $\lambda$ its lapse rate in kelvin per metre.

$$ T(h) = T_0 + \lambda \left( h - h_0 \right) $$

$$ p_a(h) = p_0 \left( 1 + \frac{\lambda \left( h - h_0 \right)}{T_0} \right)^{-\frac{g_0}{R \lambda}}, \qquad p_a(h) = p_0 \exp\left( -\frac{g_0 \left( h - h_0 \right)}{R T_0} \right) $$

**The second form is the limit of the first as the lapse rate goes to zero** and is the one an isothermal layer needs, which is the single place in this article where a relation and its own degenerate case both have to be implemented.

**The speed of sound and the Mach number follow, and the ratio of specific heats needs a new letter.** [The X-63A article][related_post_a360_abl_space_systems_x63] wrote that ratio $\gamma$, which this article has already spent on the flight-path angle, so it is written $\kappa$ here. Let $c$ be the speed of sound in metre per second and $M$ the Mach number, dimensionless.

$$ c = \sqrt{\kappa R T}, \qquad M = \frac{v}{c} $$

**The implementation returns 1.225000 kilogram per cubic metre at sea level and 0.363918 at 11 kilometres, against the standard's published 1.2250 and 0.36391, and a sound speed of 340.294 metres per second against the standard's own 340.294.**

#### The Density Scale Height Is Not the Pressure Scale Height

The natural length for a density profile is its own scale height \[[scale height][ref_scale_height]\], and in a layer with a lapse rate it differs from the pressure scale height that [the X-63A article][related_post_a360_abl_space_systems_x63] used. Let $\lambda$ be the lapse rate in kelvin per metre and $H_\rho$ the density scale height in metre.

$$ H_\rho \equiv -\frac{\rho}{\mathrm{d}\rho / \mathrm{d}h} = \frac{R \, T}{g_0 + R \lambda} $$

**The lapse rate enters added to the gravitational term, and in the troposphere it is negative and therefore makes the denominator smaller.** So $H_\rho$ exceeds $H_p$ there, which is to say **density falls more slowly with altitude than pressure does**, and the reason is that cooling air is denser at a given pressure, so the temperature drop partly offsets the pressure drop rather than compounding it. At sea level the two are 10,416 metres and 8,435. **In an isothermal layer the lapse rate vanishes and the two coincide exactly**, which the implementation reproduces at 15 kilometres to nine decimal places and which is the cheapest available check that the closed form is the right one. Across the layers where a trajectory spends its dynamic pressure the closed form agrees with a numerical difference of the density profile to better than two parts in a thousand million.

#### The Condition for Peak Dynamic Pressure

Differentiate the logarithm of the dynamic pressure along the trajectory and set it to zero. Using $\mathrm{d}h / \mathrm{d}t = v \sin \gamma$ and the definition of the density scale height,

$$ \frac{\mathrm{d}}{\mathrm{d}t} \ln q = -\frac{v \sin \gamma}{H_\rho} + \frac{2}{v}\frac{\mathrm{d}v}{\mathrm{d}t} = 0 \qquad \Longrightarrow \qquad v^2 \sin \gamma = 2 H_\rho \frac{\mathrm{d}v}{\mathrm{d}t} $$

**Maximum dynamic pressure occurs where the vertical speed divided by the density scale height equals twice the relative rate of acceleration.** The relation is exact, it holds for any atmosphere and any trajectory, and it contains nothing about the vehicle. It was checked at the computed peak of five ascent profiles and **the worst disagreement between its two sides is 4.5 parts in a million**, which is the resolution of the golden-section search rather than an error in the relation.

Written as a statement about competition it is easier to read. **Dynamic pressure rises while the vehicle is accelerating and falls while the air is thinning, and it peaks at the moment those two rates balance.** Climbing faster moves the peak earlier and lower, and accelerating harder moves it later and higher.

### The Trajectory, and Why Two Power Laws Are Not One

[The previous article][related_post_a360_abl_space_systems_x63] fitted the altitude alone, as $h_b (t / t_b)^n$ with the exponent swept between 1.5 and 3.0, and used it inside a pressure integral where only the altitude enters. **Dynamic pressure needs the altitude and the speed together, and choosing each independently does not produce a trajectory.**

**Taking that altitude law with an exponent of 2 alongside a speed law linear in time puts this vehicle at Mach 2.85 at 8.4 kilometres and returns a peak dynamic pressure of 190 kilopascal.** That is about five times what a launch vehicle experiences, and it makes the drag fraction exceed one at every plausible ballistic coefficient. **A drag fraction above one describes a vehicle that is decelerating, and this one was climbing.** The model refuted itself on a quantity it was not asked about, which is the cheapest way for a model to fail.

The repair is to stop choosing the altitude. A rocket flying a gravity turn \[[gravity turn][ref_gravity_turn]\] has its altitude fixed by the integral of the vertical component of its own speed, so a speed law and a pitch program determine it, and **the published cut-off altitude then fixes the remaining parameter instead of being assumed alongside it**. Let $k$ be a pitch exponent, dimensionless.

$$ \gamma(t) = \frac{\pi}{2}\left( 1 - \frac{t}{t_b} \right)^{k}, \qquad v(t) = v_b \left( \frac{t}{t_b} \right)^{p}, \qquad h(t) = \int_{0}^{t} v(s) \sin \gamma(s) \, \mathrm{d}s $$

The published reference mission gives liftoff at zero and main engine cut-off at 160 seconds, 75 kilometres and 2.6 kilometres per second \[[ABL Payload User's Guide][ref_abl_pug]\]. **Requiring $h(t_b) = 75$ kilometres determines $k$ for each speed exponent**, by bisection on a monotone function, and what is left is one swept assumption rather than two.

| Speed exponent | Pitch exponent solved | Peak dynamic pressure | Time of peak | Altitude of peak | Mach at peak | Flight-path angle at peak |
|---|---|---|---|---|---|---|
| 0.8 | 1.6444 | 92.23 kilopascal | 25.04 second | 7.912 kilometre | 1.912 | 68.0 degree |
| 1.0 | 1.3438 | 71.60 kilopascal | 33.61 second | 8.761 kilometre | 1.792 | 65.6 degree |
| 1.2 | 1.1242 | 60.36 kilopascal | 41.98 second | 9.424 kilometre | 1.729 | 63.9 degree |
| 1.5 | 0.8866 | 51.54 kilopascal | 53.67 second | 10.172 kilometre | 1.691 | 62.6 degree |
| 2.0 | 0.6264 | 45.86 kilopascal | 70.30 second | 10.995 kilometre | 1.701 | 62.6 degree |

**Peak dynamic pressure is now 45.9 to 92.2 kilopascal, reached at 25.0 to 70.3 seconds, at 7.9 to 11.0 kilometres, at Mach 1.69 to 1.91.** Those are launch-vehicle numbers. The spread is the cost of not knowing how the vehicle builds speed, and it is reported rather than hidden behind the central case.

**One numerical coincidence is worth defusing before a reader finds it.** For the central profile the peak sits at 8,753 metres and the density scale height there is 8,360 metres, so the ratio is 1.047. [The previous article][related_post_a360_abl_space_systems_x63] reported a sea-level pressure scale height of 8,434.9 metres, and the first version of this calculation produced a peak altitude of 8,434.5 metres, which looked like a theorem. **It is not one.** The two quantities are different functions of different variables evaluated at different altitudes, and the agreement was a consequence of the inconsistent trajectory that has since been discarded. **Across the consistent family the ratio of peak altitude to local density scale height runs from 0.92 to 1.40 and is not a constant.**

### The Signal Is Collected Before the Confounder Arrives

Now the two histories can be laid against each other, and the answer is the opposite of what the framing invites.

The altitude-compensation effect is driven by the pressure-time integral, because [the previous article][related_post_a360_abl_space_systems_x63] showed that a fixed nozzle's whole atmospheric penalty is its exit area multiplied by that integral. Let $J$ be it, in pascal second.

$$ J = \int_{0}^{t_b} p_a\left( t \right) \, \mathrm{d}t $$

**The measurement difficulty is driven by the dynamic pressure instead.** Both quantities are largest early, so the natural expectation is that they peak together and that the confounder is worst exactly where the signal lives.

**They do not peak together.** On the consistent profiles, half the pressure-time integral is collected by **11.9 to 28.3 seconds**, while dynamic pressure peaks at **25.0 to 70.3 seconds**, which is **2.10 to 2.48 times later** in every case.

| Speed exponent | Half the signal collected by | Dynamic pressure peaks at | Peak later by a factor of | Dynamic pressure at the half-signal time | Share of the signal already collected when it peaks |
|---|---|---|---|---|---|
| 0.8 | 11.95 second | 25.04 second | 2.096 | 57.2 percent of its peak | 83.6 percent |
| 1.0 | 14.89 second | 33.61 second | 2.258 | 42.0 percent of its peak | 87.7 percent |
| 1.2 | 17.79 second | 41.98 second | 2.360 | 30.5 percent of its peak | 90.4 percent |
| 1.5 | 21.97 second | 53.67 second | 2.443 | 18.6 percent of its peak | 93.0 percent |
| 2.0 | 28.29 second | 70.30 second | 2.485 | 8.2 percent of its peak | 95.3 percent |

**By the time dynamic pressure peaks, between 83.6 and 95.3 percent of the whole pressure-time integral has already been collected.** And at the moment half the integral is in hand, dynamic pressure stands at only **8.2 to 57.2 percent** of the value it will reach.

**So the experiment is better posed than the arithmetic of the error budget alone suggests.** The seconds that carry the altitude-compensation signal are seconds in which the atmosphere is dense enough to matter thermodynamically and the vehicle is still slow enough that the drag force is a modest fraction of thrust. **Pressure matters at low altitude and drag matters at high speed, and a rocket is at low altitude before it is at high speed.** That separation is not an accident of this trajectory. It follows from the fact that ambient pressure depends on position while drag depends on position and on the square of speed, so the drag term is the later of the two to develop.

**The separation weakens as the profile lingers.** The slowest-accelerating profile collects half its integral at 28.3 seconds and peaks its dynamic pressure at 70.3, a factor of 2.48; the fastest collects half at 11.9 and peaks at 25.0, a factor of 2.10. **The ordering never reverses across the family tried**, and no profile in it puts the dynamic-pressure peak inside the window that carries half the signal.

### What the Drag Fraction Depends On

**The drag fraction has carried the whole argument and it has not yet been written down in terms of anything a designer chooses.** That is worth repairing before the budget is read as a requirement, because it says which unknowns matter and which cancel.

$$ d \equiv \frac{D}{F} = \frac{q \, C_D A}{F} $$

Two groups turn that into a statement about the vehicle rather than about its absolute size. Let $m_0$ be the initial mass in kilogram, $\psi$ the initial thrust-to-weight ratio, dimensionless, and $B$ the ballistic coefficient in kilogram per square metre.

$$ \psi \equiv \frac{F}{m_0 g_0}, \qquad B \equiv \frac{m_0}{C_D A} $$

$$ d = \frac{q}{\psi \, g_0 B} $$

**The flight appears once, as the dynamic pressure, and the vehicle appears twice, as a thrust-to-weight ratio and a ballistic coefficient.** Neither the mass nor the reference area survives on its own. **That is the useful form because a designer knows a thrust-to-weight ratio and a ballistic coefficient without being able to quote either of the quantities inside them**, and because it separates what the trajectory does from what the vehicle is.

**It does not let this article compute a number, and saying why is the point.** The X-64A's mass is not published, its drag coefficient is not published and its thrust is not published, so none of $\psi$, $B$ or $d$ can be evaluated. **The budget below is therefore stated as a function of $d$ rather than at a value of it**, and the comparison that matters is against the range of $d$ a vehicle of these proportions could plausibly occupy rather than against a point.

**One thing the form does give without any of those numbers.** Since $\psi$, $g_0$ and $B$ are constant through the burn to the accuracy that matters here, the drag fraction is proportional to the dynamic pressure, so its shape in time is the dynamic-pressure history and its ratio between two instants is theirs.

$$ \frac{d\left( t_1 \right)}{d\left( t_2 \right)} = \frac{q\left( t_1 \right)}{q\left( t_2 \right)} $$

**That is what licenses the comparison made below** between the drag fraction during the seconds that carry the signal and its value at the peak, because the ratio of the two is a ratio of dynamic pressures and both of those are computed.

### What Accuracy the Drag Model Has to Have

With the timing established, the budget can be read as a requirement rather than as an algebraic identity.

| Drag fraction | Drag-model accuracy | Total thrust error | Drag term alone | Drag share of the variance | Total error over a 5.3 percent effect |
|---|---|---|---|---|---|
| 5 percent | 5 percent | 1.091 percent | 0.250 percent | 5.2 percent | 0.206 |
| 5 percent | 10 percent | 1.174 percent | 0.500 percent | 18.1 percent | 0.222 |
| 5 percent | 25 percent | 1.640 percent | 1.250 percent | 58.1 percent | 0.309 |
| 10 percent | 5 percent | 1.124 percent | 0.500 percent | 19.8 percent | 0.212 |
| 10 percent | 10 percent | 1.419 percent | 1.000 percent | 49.7 percent | 0.268 |
| 10 percent | 25 percent | 2.695 percent | 2.500 percent | 86.1 percent | 0.508 |
| 20 percent | 5 percent | 1.342 percent | 1.000 percent | 55.6 percent | 0.253 |
| 20 percent | 10 percent | 2.191 percent | 2.000 percent | 83.3 percent | 0.413 |
| 20 percent | 25 percent | 5.079 percent | 5.000 percent | 96.9 percent | 0.958 |
| 30 percent | 5 percent | 1.692 percent | 1.500 percent | 78.6 percent | 0.319 |
| 30 percent | 10 percent | 3.100 percent | 3.000 percent | 93.6 percent | 0.585 |
| 30 percent | 25 percent | 7.541 percent | 7.500 percent | 98.9 percent | 1.423 |

**Read down the drag-share column and the character of the experiment changes as the drag fraction rises.** At a drag fraction of one twentieth and a drag model good to five percent, the drag term contributes 5.3 percent of the variance and the measurement is an instrument problem. At a drag fraction of one fifth and a drag model good to a quarter, **the drag term is 96.9 percent of the variance and the measurement is a drag problem with instruments attached.**

Inverting the budget gives the requirement directly. For the drag term alone to be a fraction $f$ of an effect of size $\Delta$,

$$ d \, \frac{\delta D}{D} \le f \Delta \qquad \Longrightarrow \qquad \frac{\delta D}{D} \le \frac{f \Delta}{d} $$

| Drag fraction | For a tenth of the effect | For a quarter | For a half | For all of it |
|---|---|---|---|---|
| 5 percent | 10.60 percent | 26.50 percent | 53.00 percent | 106.00 percent |
| 10 percent | 5.30 percent | 13.25 percent | 26.50 percent | 53.00 percent |
| 20 percent | 2.65 percent | 6.62 percent | 13.25 percent | 26.50 percent |
| 30 percent | 1.77 percent | 4.42 percent | 8.83 percent | 17.67 percent |

**The requirement is hyperbolic in the drag fraction and that is the whole difficulty.** At a drag fraction of one twentieth, holding the drag term to a tenth of the effect needs a drag model good to 10.6 percent, which is achievable for a configuration that has been wind-tunnel tested. At a drag fraction of one fifth it needs **2.65 percent**, and at three tenths it needs **1.77 percent**. **No drag model of a novel configuration is good to two percent before the vehicle flies.** Predicting the drag of a body of revolution to a few percent through the transonic region is not what pre-flight aerodynamics does.

#### The Drag Fraction at Which the Experiment Stops Working

The useful single number is the drag fraction at which the total error equals the effect being measured. Write $d_{\mathrm{crit}}$ for it, dimensionless, and $\Delta$ for the size of the effect as a fraction, dimensionless. The condition is the budget set equal to the effect.

$$ \left( 1 - d_{\mathrm{crit}} \right)^{2} \left[ \left( \frac{\delta m}{m} \right)^{2} + \left( \frac{\delta a_s}{a_s} \right)^{2} \right] + d_{\mathrm{crit}}^{2} \left( \frac{\delta D}{D} \right)^{2} = \Delta^{2} $$

**That is a quadratic in $d_{\mathrm{crit}}$ and it is solved by bisection rather than by formula**, because the left side is monotone in $d_{\mathrm{crit}}$ wherever the drag-model error exceeds the instrument terms, which is the only regime in which the question is interesting. Solving it at fixed drag-model accuracy gives the following.

| Drag-model accuracy | Drag fraction at which the error equals 5.3 percent | Drag fraction at which it equals 8.5 percent |
|---|---|---|
| 5 percent | above unity | above unity |
| 10 percent | 0.5274 | 0.8498 |
| 25 percent | 0.2090 | 0.3387 |
| 50 percent | 0.1041 | 0.1690 |

**A drag model good to five percent never breaks the experiment at any drag fraction below unity.** A model good to ten percent breaks it at a drag fraction of **0.527**. A model good to a quarter breaks it at **0.209**, and a model good only to a half breaks it at **0.104**.

**The comparison that matters is against the drag fraction during the seconds that carry the signal, not against its peak.** Dynamic pressure at the half-signal time is 8.2 to 57.2 percent of its peak value, so the drag fraction there is the same fraction of its own peak. **Even a peak drag fraction of three tenths, which would be high for a launch vehicle, gives between 0.025 and 0.17 during the window that carries half the effect.** Against a critical value of 0.209 for a quarter-accurate drag model, that is inside the feasible region across most of the family and marginal at its slow end.

**So the honest verdict on the measurement is that it works, and that it works because of when the signal arrives rather than because of how good the instruments are.** An accelerometer twice as good buys a factor of two on a term that is already small. **Flying a profile that reaches altitude before it reaches speed buys a factor of seven on the term that dominates.** The trajectory is the instrument.

**And the vehicle's shape works against exactly that.** The drag fraction is proportional to $C_D A / m$, and this vehicle's frontal area is 1.72 times its sibling's at equal mass and equal drag coefficient, with a fineness ratio that probably makes its drag coefficient the higher of the two as well. **The shape chosen to make the vehicle recoverable raises the one term in the error budget that no instrument on board can reduce.** That is not a contradiction in the design. It is a trade, and naming it is the point of computing the budget.

### Two Vehicles Cannot Be Differenced

One consequence of the laboratory's own sentence deserves stating because it bears on what the programme could have learned.

**The cleanest way to measure a five percent nozzle effect is not to measure thrust twice. It is to measure the difference.** Fly the same vehicle on the same trajectory with two nozzles, and the drag model, the mass bookkeeping and the accelerometer calibration are common to both flights and cancel to first order in the difference. **What survives is the quantity of interest**, and a differential experiment can resolve an effect far smaller than either of its absolute measurements.

**ARISE is not built that way.** The laboratory put two teams on two vehicles of two designs \[[AFRL's Rocket Lab Past, Present and Future][ref_rocketlab]\], and they differ in the dimension that matters most for the cancellation. The X-63A was to be a single-stage aerospike variant of a vehicle of fineness ratio 14.67; the X-64A is a vehicle of fineness ratio about 5. **Their drag models are not common terms and their difference does not cancel anything.**

**This is an inference about experiment design and it is marked as one.** Neither document says the two vehicles were intended to be compared against one another, and there are good reasons to fund two independent attempts at a first flight that have nothing to do with differencing, chief among them that one of them might not fly. **What can be said without inference is narrower.** Two vehicles of different proportions, flown by different teams, produce two absolute measurements each limited by its own drag model, and **the register's identical descriptions give a reader no warning that the two results are not interchangeable.**

## Dependent Systems

**The record names one subsystem of this vehicle and one property of its engine, and the systems that depend on them are reconstructed from those two facts.** The subsystem is a set of four legs that serve as stabilising fins in flight and as landing gear on return \[[Invocon X-64][ref_ds_x64]\]. The property is that the engine is to be highly instrumented \[[AFRL awards agreements under ARISE][ref_arise_award]\]. From the legs follow the static-margin requirement and the tip-over footprint, and from the instrumentation follow the sensor ring on the annulus and the data rate it produces. **The recoverability that the legs make possible is where those two lines meet.** No subsystem design, sensor count or telemetry capacity for this vehicle is published, so every quantity in this section is a requirement or a sweep rather than a specification.

### The Legs, Which Are Also Fins

**The one design feature the record describes is a set of four legs that are stabilising fins on the way up and landing gear on the way down** \[[Invocon X-64][ref_ds_x64]\]. That is two jobs with different optima on one set of hardware, and both jobs are governed by the same count.

#### What a Short Vehicle Costs in Static Margin

A fin-stabilised vehicle is statically stable when its centre of pressure lies aft of its centre of mass, and the convention states the separation in calibres, being multiples of the body diameter. Let $x_{cp}$ and $x_{cm}$ be the axial positions of the centre of pressure and the centre of mass in metre, $D_b$ the body diameter in metre, and $S_m$ the static margin in calibre, dimensionless.

$$ S_m = \frac{x_{cp} - x_{cm}}{D_b} $$

**The rule of thumb asks for at least one calibre, and what one calibre costs depends entirely on how slender the vehicle is.** Expressed as a fraction of the vehicle's own length, with $L$ the length in metre and $f = L / D_b$ the fineness ratio,

$$ \frac{x_{cp} - x_{cm}}{L} = \frac{S_m}{f} $$

**One calibre of margin on this vehicle is 20 percent of its length. One calibre on its sibling's parent is 6.8 percent.** The ratio is 2.93, which is the fineness ratio again, and it follows from published dimensions with no aerodynamics in it. A short vehicle has to move its centre of pressure four times as far, measured against the only length it has, to buy the same conventional margin.

**That is why the legs have to be fins rather than merely being stowed alongside.** A body of revolution generates little of its own restoring moment, and slender-body theory says how little. Let $C_{N\alpha}$ be the normal-force coefficient slope per radian, referenced to the frontal area, dimensionless.

$$ C_{N\alpha,\,\mathrm{nose}} = 2, \qquad C_{N\alpha,\,\mathrm{body}} = 0 $$

**The nose contributes a slope of two per radian and the cylindrical body contributes nothing at all**, in inviscid slender-body theory and at small angle of attack. **Both halves of that come from the 1967 report that made the method a convention** \[[Barrowman 1967][ref_barrowman]\], which was read in full for this article. Its equation 3-66 gives the body normal-force coefficient derivative in subsonic flow as twice the ratio of the nose base area to the reference area, so a nose whose base is the reference area contributes two. **And its derivation requires the body components to be slender and free of discontinuities in cross-sectional area or its derivative**, which is exactly why a constant-diameter cylinder contributes nothing. The nose contribution also acts near the front of the vehicle, forward of any plausible centre of mass, **so the bare airframe is statically unstable and every scrap of restoring moment has to come from the aft surfaces.**

**That report is also the answer to something this article's own source base records as a puzzle.** The bibliographic index returns nothing relevant for the author's name, offering context-aware random numbers and gastrointestinal lymphatics instead. **The reports server holds the document under its title.** A method that circulated as a report and then as a handbook convention has no presence in an index of journal papers, **and the two registries hold different literatures rather than the same literature to different depths.**

**The inviscid result is a floor and the viscous correction runs upward.** The classical study of viscosity on slender inclined bodies shows the measured normal force exceeding the potential-flow value, the excess growing with angle of attack as crossflow separation develops \[[Allen and Perkins 1951][ref_allen_perkins]\]. **So a real body contributes more restoring moment than two per radian implies, and the fin requirement computed from the inviscid figure is the conservative one**, which is the direction a designer would want an error to run and the opposite of the direction that would invalidate the argument. **A vehicle whose landing gear is also its empennage has not bolted two functions onto one part for elegance. It has put the aerodynamic surface where a short vehicle needs it and then noticed it was also where the ground is.**

**This article does not compute the fin area required**, because that needs the nose contour, the fin planform and a centre-of-mass history, none of which is public. **What is computed is the requirement those unknowns have to satisfy**, and the requirement is 2.93 times more demanding than it would be for the parent vehicle of the other designation.

### The Footprint Is a Polygon, and It Is Simpler Than the One A360 Needed

On the ground the same four surfaces become a support polygon, and the mathematics is the same family as [the companion article's][related_post_a360_abl_space_systems_x63] but a different member of it.

Let $N$ be the number of legs, dimensionless, equally spaced on a circle of radius $r$ in metre, and let $h_{cm}$ be the height of the centre of mass above the ground in metre. Tipping occurs when the centre of mass passes outside the convex hull of the contact points \[[convex hull][ref_convex_hull]\]. If the vehicle tilts by $\theta$ in the direction $\phi$, the ground projection of the centre of mass moves $h_{cm} \tan \theta$, so the critical tilt is set by the distance from the axis to the hull boundary in that direction. Write $\ell(\phi)$ for that distance in metre, calling it the lever arm, **because $\rho$ is already the atmospheric density above**.

$$ \tan \theta_{\mathrm{tip}}\left( \phi \right) = \frac{\ell\left( \phi \right)}{h_{cm}} $$

For a regular polygon with vertices at the legs, $\ell$ has a closed form. Let $a$ be the angle from the nearest leg, so that $\lvert a \rvert \le \pi / N$.

$$ \ell\left( \phi \right) = \frac{r \cos\left( \pi / N \right)}{\cos\left( \pi / N - \lvert a \rvert \right)}, \qquad \ell_{\max} = r, \qquad \ell_{\min} = r \cos\left( \frac{\pi}{N} \right) $$

**The lever arm is not the support function of the hull, and the difference is worth writing down because the two are easy to conflate.** The support function \[[support function of a convex set][ref_support_function]\] gives the distance from the axis to a supporting line perpendicular to a direction, where the lever arm gives the distance along a ray to the hull boundary. Let $h_s$ be the support function in metre, with the legs at angles $\theta_k = 2 \pi k / N$ in radian.

$$ h_s\left( \phi \right) = \max_{k} \, r \cos\left( \theta_k - \phi \right) = r \cos a $$

**The two agree only at the extremes.** Both run from $r \cos(\pi / N)$ to $r$, which is why the anisotropy below is the same for either, and between those directions the lever arm is the smaller of the two because a ray reaches the boundary before the supporting line does. **Tipping is a question about the boundary along a ray, so the lever arm is the right object**, and a footprint that was not a regular polygon would separate them in range as well as in shape.

**The lever arm is longest straight over a leg and shortest across the gap between two**, because the legs are the vertices of the hull and the gaps are spanned by its edges.

**The tempting construction gets this backwards and it is worth saying which one.** Measuring the angle to the nearest leg and dividing the inradius by its cosine produces a function with the right range and the wrong orientation, placing the short lever arm at a leg and the long one in the gap, **which inverts the physical conclusion and makes a four-legged vehicle look most stable in the direction it is least stable in.** **A footprint is a hull and not a rosette.** Evaluating the closed form at the two special directions and asking which gives the smaller number settles it in one line, and is worth doing because both orientations look plausible written down.

#### The Anisotropy Is the Same Closed Form A360 Derived

$$ \frac{\ell_{\max}}{\ell_{\min}} = \frac{1}{\cos\left( \pi / N \right)} $$

**That is, character for character, the ratio of best-direction to guaranteed control authority that [the previous article][related_post_a360_abl_space_systems_x63] derived for differential throttling of a ring of thrusters.** The same regular polygon governs how evenly a ring of engines can steer and how evenly a ring of legs can stand.

| Legs | Sides of the footprint polygon | Sides of A360's control polygon at the same count | Inradius over circumradius | Tip-over anisotropy | Best over worst |
|---|---|---|---|---|---|
| 3 | 3 | 6 | 0.500000 | 2.000000 | 100.00 percent |
| 4 | 4 | 4 | 0.707107 | 1.414214 | 41.42 percent |
| 5 | 5 | 10 | 0.809017 | 1.236068 | 23.61 percent |
| 6 | 6 | 6 | 0.866025 | 1.154701 | 15.47 percent |
| 8 | 8 | 8 | 0.923880 | 1.082392 | 8.24 percent |
| 12 | 12 | 12 | 0.965926 | 1.035276 | 3.53 percent |

**For four legs the anisotropy is exactly the square root of two.** A four-legged vehicle tolerates 41.4 percent more tilt falling across a leg than falling between two, and **a three-legged one tolerates exactly twice as much**, which is the arithmetic behind the reputation of tripod landers. **Eight legs bring it to 8.2 percent and twelve to 3.5 percent**, and the returns diminish as the cosine flattens.

#### Why This Polygon Has N Sides and A360's Had N or 2N

**[The previous article][related_post_a360_abl_space_systems_x63] found that its control polygon has $N$ sides for an even ring and $2N$ for an odd one, and that result has no counterpart here.** The footprint polygon has exactly $N$ sides for every $N$.

Write $m_h$ for the number of sides of the footprint hull and $m_c$ for the number of sides of A360's control polygon, both dimensionless.

$$ m_h = N \quad \text{for every } N, \qquad m_c = \begin{cases} N, & N \text{ even} \\ 2N, & N \text{ odd} \end{cases} $$

**The difference is the construction and not the geometry.** A360's object was a maximum over throttle patterns of a sum of $\max\left( \cos, 0 \right)$ terms, and that truncation puts a breakpoint wherever a module crosses the boundary of the forward half plane. For an odd ring those crossings interleave into two families and the count doubles. **Here the object is the convex hull of the contact points, whose support function is piecewise linear with one piece per vertex, and there is no half-plane to cross.** No truncation, no parity.

**That contrast has a second layer which A360 records.** Which direction is extremal relative to the modules turns, for the control polygon, on the module count modulo four rather than on its parity. **The footprint polygon has no such subtlety**, and the extremal directions are the legs and the gaps between them for every count. **The truncated object is the complicated one and the hull is the simple one**, which is worth stating because the two share a closed form and a reader who met the anisotropy first might expect them to share everything.

#### The Numbers, With the Vehicle's Own Dimensions

The leg reach and the centre-of-mass height of a returning X-64A are not published, so both are swept. A body radius of 1.2 metres sets the lower bound on the footprint radius, since legs cannot retract inside the hull, and a 12 metre vehicle returning nearly empty puts its centre of mass low.

| Footprint radius | Centre-of-mass height | Worst direction, across a gap | Best direction, over a leg | Shortest lever arm | Longest lever arm |
|---|---|---|---|---|---|
| 1.2 metre | 3.0 metre | 15.79 degree | 21.80 degree | 0.8485 metre | 1.2000 metre |
| 1.2 metre | 4.0 metre | 11.98 degree | 16.70 degree | 0.8485 metre | 1.2000 metre |
| 1.2 metre | 5.0 metre | 9.63 degree | 13.50 degree | 0.8485 metre | 1.2000 metre |
| 1.2 metre | 6.0 metre | 8.05 degree | 11.31 degree | 0.8485 metre | 1.2000 metre |
| 1.8 metre | 3.0 metre | 22.99 degree | 30.96 degree | 1.2728 metre | 1.8000 metre |
| 1.8 metre | 4.0 metre | 17.65 degree | 24.23 degree | 1.2728 metre | 1.8000 metre |
| 1.8 metre | 5.0 metre | 14.28 degree | 19.80 degree | 1.2728 metre | 1.8000 metre |
| 1.8 metre | 6.0 metre | 11.98 degree | 16.70 degree | 1.2728 metre | 1.8000 metre |
| 2.4 metre | 3.0 metre | 29.50 degree | 38.66 degree | 1.6971 metre | 2.4000 metre |
| 2.4 metre | 4.0 metre | 22.99 degree | 30.96 degree | 1.6971 metre | 2.4000 metre |
| 2.4 metre | 5.0 metre | 18.75 degree | 25.64 degree | 1.6971 metre | 2.4000 metre |
| 2.4 metre | 6.0 metre | 15.79 degree | 21.80 degree | 1.6971 metre | 2.4000 metre |
| 3.0 metre | 3.0 metre | 35.26 degree | 45.00 degree | 2.1213 metre | 3.0000 metre |
| 3.0 metre | 4.0 metre | 27.94 degree | 36.87 degree | 2.1213 metre | 3.0000 metre |
| 3.0 metre | 5.0 metre | 22.99 degree | 30.96 degree | 2.1213 metre | 3.0000 metre |
| 3.0 metre | 6.0 metre | 19.47 degree | 26.57 degree | 2.1213 metre | 3.0000 metre |

**Across that sweep the worst-direction tilt tolerance runs from 8.05 to 35.26 degrees.** The favourable corner, being legs reaching 3 metres on a vehicle whose centre of mass is 3 metres up, tolerates 35.26 degrees across a gap and 45.00 degrees over a leg. **The unfavourable corner, legs no wider than the body on a vehicle whose mass sits at half its height, tolerates 8.05 degrees.** A landing gear that reaches only to the body radius is not a landing gear, which is the arithmetic reason the legs in the description are said to rotate downward and outward rather than merely down.

### What a Ring of Sensors Can See, and What It Cannot

The award requires a highly instrumented engine \[[AFRL awards agreements under ARISE][ref_arise_award]\], and an annular aerospike presents its measurands on a circle. **A finite number of sensors on a circle is a sampling problem and sampling problems have exact answers.**

[The previous article][related_post_a360_abl_space_systems_x63] established what the flight was meant to observe. The fact sheet names open wake, wake transition and closed wake as three regimes to be visited, the base pressure of a truncated plug decides how much of the truncation loss is recovered, and the transition between two flow topologies is the kind of thing that can be unsteady or hysteretic. **An ideal axisymmetric nozzle puts all of that in the zeroth azimuthal harmonic. A real one does not, and the departures are what a ring of sensors is for.**

Expand the quantity measured around the annulus as a Fourier series in the azimuthal angle. Let $\vartheta$ be that angle in radian, $\mu$ the azimuthal harmonic index, dimensionless, and $A_\mu$ and $B_\mu$ the coefficients in whatever unit the measurand carries.

$$ \Psi\left( \vartheta \right) = A_0 + \sum_{\mu = 1}^{\infty} \left[ A_\mu \cos \mu \vartheta + B_\mu \sin \mu \vartheta \right] $$

**The harmonics are not interchangeable and each means something physical.** The zeroth is the mean, which is the thrust-bearing quantity. The first is a net lateral resultant, which is a side load. The second is an ovalisation. **Harmonics at the leg count and its multiples are whatever the legs themselves impose on the flow.**

Sample at $N$ sensors equally spaced at $\vartheta_j = 2 \pi j / N$. **The estimator for each coefficient is a sum over the sensors and it is what makes the counting argument concrete.**

$$ \hat{A}_\mu = \frac{2}{N}\sum_{j=0}^{N-1} \Psi\left( \vartheta_j \right) \cos \mu \vartheta_j, \qquad \hat{B}_\mu = \frac{2}{N}\sum_{j=0}^{N-1} \Psi\left( \vartheta_j \right) \sin \mu \vartheta_j $$

**The counting is the sampling theorem applied to a circle rather than to a line**, and the theorem's own statements are worth citing rather than an encyclopaedia's summary of them \[[Shannon 1949][ref_shannon_1949]\] \[[Nyquist 1928][ref_nyquist_1928]\]. **Neither was read for this article and both are cited at second hand**, which is stated here because the result is used and not merely mentioned. **What makes the circular case finite rather than a limit is that the domain is compact**, so the harmonics are indexed by integers and the count is exact where the line's version is a bandwidth condition.

**Each sensor contributes one number, so $N$ sensors deliver $N$ numbers and no more.** Recovering the mean costs one of them and recovering each harmonic costs two, being a cosine coefficient and a sine coefficient, so the harmonics resolvable in both phases are bounded by a count rather than by anything physical.

$$ 1 + 2 \mu_{\max} \le N \qquad \Longrightarrow \qquad \mu_{\max} = \left\lfloor \frac{N - 1}{2} \right\rfloor $$

And the harmonics above that limit are not lost but misread \[[aliasing][ref_aliasing]\] \[[discrete Fourier transform][ref_dft]\]. **The discrete transform sees harmonic $\mu$ as harmonic $\mu \bmod N$, folded into the resolvable range.**

$$ \mu \; \longmapsto \; \min\left( \mu \bmod N, \; N - \left( \mu \bmod N \right) \right) $$

| Sensors on the ring | Harmonics resolved in both phases | Harmonic resolved in one phase only | Harmonic that aliases onto the mean | Sensors needed for a four-lobed pattern |
|---|---|---|---|---|
| 3 | 0 to 1 | none | 3 | 9 |
| 4 | 0 to 1 | 2 | 4 | 9 |
| 5 | 0 to 2 | none | 5 | 9 |
| 6 | 0 to 2 | 3 | 6 | 9 |
| 8 | 0 to 3 | 4 | 8 | 9 |
| 12 | 0 to 5 | 6 | 12 | 9 |

**Recovering both phases of harmonic $\mu$ needs $2\mu + 1$ sensors.** A side load needs three. An ovalisation needs five. **A four-lobed pattern needs nine.** An even sensor count resolves the harmonic at half that count in one phase only, so four sensors see an ovalisation aligned with them and are blind to the same ovalisation rotated by forty-five degrees.

### Four Sensors Cannot See Four Legs

The sharp case is the one this vehicle's own geometry produces.

$$ \frac{1}{N}\sum_{j=0}^{N-1} \cos\left( N \, \vartheta_j + \varphi \right) = \cos \varphi \qquad \text{for every } N \text{ and every } \varphi $$

**Harmonic $N$ sampled at $N$ points has exactly the same discrete mean as harmonic zero.** Not approximately, and not for particular phases. The sum above was evaluated at five sensor counts and returns 1 at zero phase and one half at a phase of sixty degrees, which is the cosine of the phase in both cases, matching harmonic zero term for term.

| Sensors | Discrete mean of harmonic zero | Discrete mean of harmonic equal to the sensor count | The same at a phase of sixty degrees | Cosine of sixty degrees |
|---|---|---|---|---|
| 3 | 1.000000 | 1.000000 | 0.500000 | 0.500000 |
| 4 | 1.000000 | 1.000000 | 0.500000 | 0.500000 |
| 5 | 1.000000 | 1.000000 | 0.500000 | 0.500000 |
| 6 | 1.000000 | 1.000000 | 0.500000 | 0.500000 |
| 8 | 1.000000 | 1.000000 | 0.500000 | 0.500000 |

**This vehicle has four legs, and four legs impose a disturbance whose leading azimuthal content is harmonic four.** Four wakes, four sets of shed vorticity, four interference regions where a surface meets the body. **If such a vehicle carried four pressure taps on its annulus, aligned with its legs as the natural symmetry invites, that four-lobed pattern would be read as a uniform shift in base pressure.** The instrument would report a change in the mean, which is the thrust-bearing quantity, when what had changed was a four-lobed asymmetry contributing nothing to axial thrust.

**The failure mode is worse than blindness because it is not silent.** A sensor set that cannot see a harmonic returns zero for it and a careful analyst notices the gap. **A sensor set that aliases a harmonic onto the mean returns a plausible number in the channel that matters most**, and nothing in the data says it came from the wrong place.

**The sensor count of the ARISE engine is not public and this is therefore a statement about sensor rings rather than about this hardware.** What can be said without inference is that the count must not equal the leg count, nor any divisor of it, and that **nine sensors are needed to resolve a four-lobed pattern in both phases while five suffice to distinguish it from the mean**. The second number is the cheap one and the one a designer would want to know.

**One reassurance falls out of the same arithmetic.** The regimes the flight exists to measure are changes in the mean, and the mean is the one harmonic every sensor count recovers. **An undersampled ring measures the wake transition correctly and misattributes the asymmetry**, which is the right way round for this programme's primary objective and the wrong way round for anybody hoping to learn about side loads from the same data.

### Highly Instrumented, in Bits Per Second

The word the award uses is `highly instrumented` \[[AFRL awards agreements under ARISE][ref_arise_award]\]. That is a qualitative phrase attached to a quantitative constraint, and the constraint is worth writing down because it explains the vehicle's most distinctive feature.

Let $n_c$ be the number of channels, dimensionless, $f_s$ the per-channel sample rate in hertz, $b$ the bits per sample, dimensionless, and $\mathcal{R}$ the aggregate rate in bit per second.

$$ \mathcal{R} = n_c f_s b, \qquad V = \frac{\mathcal{R} \, t_b}{8} $$

where $V$ is the volume written over a burn in byte. **Both are elementary and neither is usually stated, which is why the trade they describe is usually invisible.**

| Channels | Sample rate | Bits | Aggregate rate | Written over a 160 second burn | Written over a 600 second flight |
|---|---|---|---|---|---|
| 100 | 1,000 hertz | 12 | 1.2 megabit per second | 0.024 gigabyte | 0.090 gigabyte |
| 200 | 5,000 hertz | 16 | 16.0 megabit per second | 0.320 gigabyte | 1.200 gigabyte |
| 500 | 10,000 hertz | 16 | 80.0 megabit per second | 1.600 gigabyte | 6.000 gigabyte |
| 1000 | 20,000 hertz | 16 | 320.0 megabit per second | 6.400 gigabyte | 24.000 gigabyte |
| 2000 | 50,000 hertz | 16 | 1600.0 megabit per second | 32.000 gigabyte | 120.000 gigabyte |

**Five hundred channels at ten kilohertz and sixteen bits is eighty megabits per second and 1.6 gigabytes over a 160 second burn.** That is the middle row of the table and it is the modest case.

**The sample rate is not free to choose, because the engine sets it.** [The X-63A article][related_post_a360_abl_space_systems_x63] recovered a combustion instability at 4.5 kilohertz from the manufacturer's own incident report, and the first tangential mode of a thrust chamber is exactly the kind of thing a highly instrumented engine exists to observe. **Sampling theory puts the floor at nine kilohertz and practice puts it several times higher**, because a mode at the Nyquist limit is detectable and not characterisable. **So the ten kilohertz row is below what this engine's own published instability requires**, and the twenty kilohertz row, at 320 megabits per second and 6.4 gigabytes, is nearer the honest figure for the channels that matter.

**The deficit is a ratio and it is worth writing down.** Let $\mathcal{R}_\ell$ be the downlink capacity in bit per second and $\eta_\ell$ the deficit, dimensionless.

$$ \eta_\ell = \frac{\mathcal{R}}{\mathcal{R}_\ell} = \frac{n_c f_s b}{\mathcal{R}_\ell} $$

**The volume is trivial and the rate is not.** **No telemetry capacity for either ARISE vehicle is published**, so the comparison below is against a range rather than a number, and the range is an assumption of this article. Sounding-rocket and small-launcher links of this era are commonly of order one to twenty megabits per second, and the table gives the deficit across that whole span rather than resting on one value.

| Downlink capacity | 200 channels at 5 kilohertz | 500 channels at 10 kilohertz | 1000 channels at 20 kilohertz |
|---|---|---|---|
| 0.5 megabit per second | 32.0 | 160.0 | 640.0 |
| 1.0 megabit per second | 16.0 | 80.0 | 320.0 |
| 5.0 megabit per second | 3.2 | 16.0 | 64.0 |
| 10.0 megabit per second | 1.6 | 8.0 | 32.0 |
| 20.0 megabit per second | 0.8 | 4.0 | 16.0 |

**1.6 gigabytes is a component that costs nothing and weighs nothing. Eighty megabits per second through the atmosphere from a moving vehicle is a programme.** So an expendable vehicle that wants this much data must either throw most of it away before transmission, which means deciding in advance what matters, or accept losing it with the vehicle.

### Why the Vehicle Comes Back

**The recoverability is the answer to the bandwidth arithmetic, and that is the thesis this article has been assembling.**

The lead contractor is an instrumentation house whose award record is wireless data acquisition, impact detection and radiation monitoring \[[USAspending][ref_usaspending]\]. The award scope is a highly instrumented engine \[[AFRL awards agreements under ARISE][ref_arise_award]\]. The vehicle is described as recoverable, landing on four legs \[[Invocon X-64][ref_ds_x64]\]. **Those three facts are usually read as three features. They are one decision.**

**Recovery converts a telemetry problem into a memory problem.** A vehicle that comes back can record at full rate onboard and be read out on the ground, so the link carries only what is needed to fly the mission and to reconstruct it if the vehicle is lost. **The constraint moves from bits per second, where it is expensive, to bytes, where in this decade it is free.** An instrumentation company asked to gather large amounts of data through an entire trajectory, and free to choose the vehicle, has an obvious reason to choose one that returns.

**The inference is marked as an inference and its weakness is that nothing in the record says so.** No document consulted states that recoverability was chosen for data return. The contractor's release, as reported, describes the legs and the dimensions and does not give a rationale \[[Invocon X-64][ref_ds_x64]\]. **Other reasons for recovery are at least as plausible and some are stated elsewhere in the programme's own literature**, chief among them that the portfolio's goals are cost and schedule and that a reusable article amortises both, which the president of the lead company named directly in saying the technology has potential for a reusable capability \[[AFRL awards agreements under ARISE][ref_arise_award]\].

**What the arithmetic establishes is not the motive but the magnitude.** Whatever recovery was chosen for, it removes a factor of sixteen to eighty between what this class of instrumentation produces and what a link of this class carries. **A programme that wanted the data and not the vehicle would have had to make that factor disappear some other way**, and the usual other way is to record less.

**And the same shape that makes recovery possible is the shape that raised the drag term in the error budget.** The vehicle is short and fat because it must stand on legs and fly on fins, its frontal area is 1.72 times its sibling's, and the drag fraction that follows is the one term no instrument on board can reduce. **The design buys its data back at the cost of the measurement's hardest term**, and whether that trade is favourable depends on the timing result above rather than on any property of the vehicle.

## The Flight Test Record, and What Happened to It

**No source consulted announces the cancellation of the X-64A, and no source announces a flight either.**

The encyclopedia entry, last revised on 11 August 2024, states in its own voice that the status and progress of the programme at the time of writing is unknown \[[Invocon X-64][ref_ds_x64]\]. The award was a three-year agreement made in December 2019, so its term expired at the end of 2022 \[[AFRL awards agreements under ARISE][ref_arise_award]\]. The designations were allocated on 20 April 2022, **eight months before that expiry and with no vehicle flown** \[[DOD 4120.15-L Addendum][ref_mds_addendum]\]. The laboratory's background document of September 2022 still describes ARISE in the future tense, saying the partnership `will fly` the first modular aerospike engine \[[AFRL's Rocket Lab Past, Present and Future][ref_rocketlab]\].

**The asymmetry with the sibling designation is the interesting part.**

[The previous article][related_post_a360_abl_space_systems_x63] followed the X-63A's contractor to its end as a launch company. The RS1 failed 10.87 seconds into its first orbital attempt in January 2023, the second vehicle burned on its pad in July 2024, and in February 2025 the company renamed itself and left the commercial launch market for missile defence. **ABL Space Systems stopped being what it was.**

**Invocon did not, and the record gives no sign that it had ever been a launch company to stop being.** Its own current description of itself is wireless sensing, distributed processing and high-precision instrumentation for extreme environments, with product families in power systems, telemetry and signal conversion, and detection and initiation \[[Invocon][ref_invocon_home]\] \[[Invocon, About Us][ref_invocon_about]\]. It says its instrumentation **flies on** launch vehicles. **It does not say it builds them, and it lists no launch vehicle among its products.** Nothing on the pages consulted mentions ARISE, the aerospike, or the X-64.

**So the two halves of one allocation ended in two different ways and neither is a flight.** One contractor attempted the vehicle, lost two of them and left the business. **The other appears to have returned to the business it was always in.** The register carries both numbers still, with the same hundred and one characters against each.

**That this programme asked an instrumentation supplier to become a launch-vehicle prime is not a criticism and the record does not support one.** The other transaction instrument exists precisely to bring in companies that would not otherwise bid, the announcement says so in as many words, and a small business leading a rocket programme with a propulsion subcontractor of KT Engineering's record is a defensible structure \[[AFRL awards agreements under ARISE][ref_arise_award]\] \[[USAspending][ref_usaspending]\]. **What the record shows is the arrangement, not its wisdom.**

## Comparison With Ground Prediction

**Nothing flew, so flight returned nothing to set beside any prediction made on the ground.** The section headed The Flight Test Record, and What Happened to It records that no source consulted announces a flight, that the agreement's three-year term expired at the end of 2022, and that the laboratory still described the flight in the future tense in September 2022 \[[AFRL's Rocket Lab Past, Present and Future][ref_rocketlab]\]. **What can be stated is what was predicted or claimed before flight**, and every such item has nothing from flight to stand against it.

**The laboratory claimed a first.** Its background document says the partnership will fly the first ever modular aerospike engine \[[AFRL's Rocket Lab Past, Present and Future][ref_rocketlab]\]. No flight of the X-64A is recorded in any source this article consulted, so this vehicle neither confirmed nor refuted the claim.

**The portfolio stated its targets in time and money rather than in thrust.** The modular architecture was to cut development time by seventy percent and development cost by fifty percent \[[AFRL's Rocket Lab Past, Present and Future][ref_rocketlab]\]. Those are predictions about a programme rather than about a flight, and the record holds no development time or cost for this vehicle to compare them with, the dollar value of the agreement itself being unknown.

**The performance prediction is analytical and belongs to the sibling article.** [The X-63A article][related_post_a360_abl_space_systems_x63] computed that an ideal altitude-compensating nozzle delivers between 5.3 and 8.5 percent more first-stage impulse than the best fixed nozzle on the parent vehicle's reference trajectory. That is the effect this vehicle was to measure, and it was never measured.

**This article's own predictions concern the measurement, and they too stand unchecked.** The section headed Sizing From First Principles predicts that the instrument floor alone consumes between a tenth and two fifths of a 5.3 percent effect, that dynamic pressure peaks 2.10 to 2.48 times later than the moment half the pressure-time integral is collected, and that even a peak drag fraction of three tenths leaves a drag model good to a quarter inside the feasible region across most of the trajectory family. The section headed Dependent Systems predicts that four equally spaced taps on the annulus would read the four-lobed disturbance of four legs as a change in the mean. **Each of those could have been tested by one instrumented flight, and none was.**

**No wind-tunnel result, contractor analysis or simulation of this vehicle is cited anywhere in this article**, and its contours, mass, thrust and drag coefficient are not public. So the comparison this section exists to make has neither of its two columns filled from the vehicle's own programme. What the record supports is a list of claims and derived requirements beside a flight record that is empty.

## What the Data Changed

Four things in this article came out differently from the way they went in.

**The trajectory model refuted itself on a quantity it was not asked about.** Two power laws chosen independently, one for altitude and one for speed, returned a peak dynamic pressure of 190 kilopascal and a drag fraction above one. **A drag fraction above one describes a decelerating vehicle and this one was climbing.** The repair was to stop choosing the altitude and let it be the integral of the vertical speed, which turns the published cut-off altitude from a second assumption into a constraint. **A model with one assumption too many will usually tell you so somewhere, and the place it tells you is rarely the quantity you were computing.**

**The timing result reversed the expected answer.** The error budget says the drag fraction sets the difficulty, the drag fraction follows dynamic pressure, and both the signal and the dynamic pressure are largest early, so the expectation was that the confounder peaks where the signal lives. **It does not.** Dynamic pressure peaks 2.10 to 2.48 times later than the half-signal time, and by the time it peaks 83.6 to 95.3 percent of the pressure-time integral is already collected. **Ambient pressure depends on position and drag depends on position and the square of speed, and a rocket reaches altitude before it reaches speed.** The measurement is feasible, and it is feasible because of when the signal arrives rather than because of how good the instruments are.

**The support polygon was computed inside out.** The first version measured the angle to the nearest leg and divided by its cosine, which places the short lever arm at a leg and the long one in the gap, and therefore said a four-legged vehicle is most stable falling between two legs. **The footprint is the convex hull of the contact points, so the legs are its vertices and the gaps are spanned by its edges**, and the truth is the reverse. It was caught by evaluating the closed form at the two special directions and asking which gave the smaller number, which is a check that costs one line.

**And the aliasing result was looked for and found in the wrong place.** The search was for a sensor count that cannot resolve a side load, which is a first harmonic and needs only three sensors, so almost any ring suffices. **The sharp case is not the smallest harmonic but the one equal to the sensor count**, because harmonic $N$ sampled at $N$ points has exactly the discrete mean of harmonic zero. **Four legs impose a four-lobed disturbance and four sensors are precisely the count that reports it as a change in the thrust-bearing mean.**

## The Contemporary Literature

The survey behind this article holds **3,837 records** after gating and deduplication, drawn from 1 sweeps that retrieved 23,960 records of which 23,824 were distinct. **1,726 of them, 45.0 percent, are report primaries**, meaning items served by the National Aeronautics and Space Administration's technical reports server or registered under the Defense Technical Information Center's prefix. 3,638 records carry a usable year, running from 1928 to 2026 with a median of 2003. **3,192 of those, 87.7 percent, predate or share the year in which both designations were allocated.**

**Every record the gate admitted is cited below.** The clusters are ordered with the specific before the general ones they are special cases of, because a matcher that returns the first match gives a broad cluster the records a narrow one was written for.

### Measuring a rocket in flight, which is the entire claim

**181 records.** \[[Fleming, William A and Gabriel, David S 1955][research_flemingwilliama_gabrieldavids_1955]\] \[[Useller, James W and Pappas, George E 1956][research_usellerjamesw_pappasgeorgee_1956]\] \[[Bloomer, Harry E 1958][research_bloomerharrye_1958]\] \[[Carta, D. G. 1963][research_cartadg_1963]\] \[[Goldin, D. S. and Norgren, C. T. 1963][research_goldinds_norgrenct_1963]\] \[[Heine, J. C. 1964][research_heinejc_1964]\] \[[Davis and Spicer 1965][research_davis_spicer_1965]\] \[[Williams 1965][research_williams_1965]\] \[[Lovell, R. R. and Nieberding, W. C. 1966][research_lovellrr_nieberdingwc_1966]\] \[[Otto, E. W. 1966][research_ottoew_1966]\] \[[Postflight Evaluation of Atlas-Centaur 1966][research_postflight_evaluation_1966]\] \[[Smith, J. D. 1966][research_smithjd_1966]\] \[[Crosswy and Kalb 1967][research_crosswy_kalb_1967]\] \[[Strome 1969][research_strome_1969]\] \[[Apollo mission 11, trajectory 1970][research_apollo_mission_1970]\] \[[Berkopec 1970][research_berkopec_1970]\] \[[Dennis, T. et al 1970][research_dennist_mchughd_1970]\] \[[Huberman et al 1970][research_huberman_kidd_1970]\] \[[Lane and Redman 1970][research_lane_redman_1970]\] \[[Poland and Schwanebeck 1970][research_poland_schwanebeck_1970]\] \[[Woodfield 1970][research_woodfield_1970]\] \[[Adams, G. L. et al 1971][research_adamsgl_bradtaj_1971]\] \[[Stark, K. W. 1972][research_starkkw_1972]\] \[[Apollo/Saturn 5 Postflight Trajectory 1973][research_apollo_saturn_5_1973]\] \[[Patterson, R. E. 1973][research_pattersonre_1973]\] \[[Lilley, R. W. 1974][research_lilleyrw_1974]\] \[[Solid rocket booster performance 1974][research_solid_rocket_1974]\] \[[Banks, B. et al 1975][research_banksb_rawlinv_1975]\] \[[Biesiadny, T. J. et al 1978][research_biesiadnytj_leed_1978]\] \[[Bohse, J. R. et al 1979][research_bohsejr_bewtram_1979]\] \[[Compton, H. R. et al 1979][research_comptonhr_blanchardrc_1979]\] \[[Compton, H. R. et al 1981][research_comptonhr_findlayjt_1981]\] \[[Hillje, E. R. and Nelson, R. L. 1981][research_hilljeer_nelsonrl_1981]\] \[[McKenna 1981][research_mckenna_1981]\] \[[Schoelen 1981][research_schoelen_1981]\] \[[Wadia and Wilson 1981][research_wadia_wilson_1981]\] \[[Lacarna, R. J. and Wissinger, D. B. 1982][research_lacarnarj_wissingerdb_1982]\] \[[Myers, L. P. et al 1982][research_myerslp_mackallkg_1982]\] \[[Adams et al 1983][research_adams_thompson_1983]\] \[[Adams et al 1983][research_adams_thompson_1983_b]\] \[[Kelly, G. M. et al 1985][research_kellygm_mcconnelljg_1985]\] \[[Roberts et al 1985][research_roberts_lewis_1985]\] \[[Rooney and Wilt 1985][research_rooney_wilt_1985]\] \[[Sovey, J. S. et al 1985][research_soveyjs_penkopf_1985]\] \[[Sovey, J. S. et al 1985][research_soveyjs_penkopf_1985_b]\] \[[Sovey, J. S. et al 1986][research_soveyjs_penkopf_1986]\] \[[Fruboese, Joachim 1987][research_fruboesejoachim_1987]\] \[[Haag, Thomas W. 1989][research_haagthomasw_1989]\] \[[Bursey and Dickinson 1990][research_bursey_dickinson_1990]\] \[[Soldi et al 1995][research_soldi_jr_1995]\] \[[Tuttle, S. L. et al 1995][research_tuttlesl_meedj_1995]\] \[[Conners and Sims 1998][research_conners_sims_1998]\] \[[Negrão et al 1998][research_negrao_fanton_1998]\] \[[Bruegge, C. and Chafin, B. 1999][research_brueggec_chafinb_1999]\] \[[Eckert and Oechslein 1999][research_eckert_oechslein_1999]\] \[[Kutschera and Render 1999][research_kutschera_render_1999]\] \[[Di Fiore dos Santos et al 2000][research_difioredossantos_lewis_2000]\] \[[Bull, Barton et al 2001][research_bullbarton_diehljames_2001]\] \[[Carpenter, J. Russell and Bauer, Frank H. 2001][research_carpenterjrussell_bauerfrankh_2001]\] \[[Thomas, Scott R. et al 2001][research_thomasscottr_palacdonaldt_2001]\] \[[Ziemer, J. K. 2001][research_ziemerjk_2001]\] \[[Bull, Barton et al 2002][research_bullbarton_diehljames_2002]\] \[[Willis, William D., III et al 2002][research_williswilliamdiii_zakrzwskicharlesm_2002]\] \[[Cook and Gruet 2003][research_cook_gruet_2003]\] \[[Desai, Prasun et al 2003][research_desaiprasun_schofieldjohnt_2003]\] \[[Hiers et al 2003][research_hiers_mackinnon_2003]\] \[[Jet Thrust Measurement In 2003][research_jet_thrust_2003]\] \[[Kerzhanovich, Viktor and Pichkhadze, Konstantin 2003][research_kerzhanovichviktor_pichkhadzekonstantin_2003]\] \[[Mart L. Cook et al 2003][research_martlcook_laurentgruet_2003]\] \[[Snellgrove et al 2003][research_snellgrove_griffin_2003]\] \[[Karlgaard, Christopher D. et al 2004][research_karlgaardchristopherd_tartabinipaulv_2004]\] \[[Lisano, Michael E. and Jah, Moriba 2004][research_lisanomichaele_jahmoriba_2004]\] \[[Lisano, Michael E. and Jah, Moriba 2004][research_lisanomichaele_jahmoriba_2004_b]\] \[[Markusic, T. E. et al 2004][research_markusicte_jonesje_2004]\] \[[Parent 2004][research_parent_2004]\] \[[Bordi, John J. et al 2005][research_bordijohnj_antreasianpete_2005]\] \[[Desai, Prasun N. et al 2005][research_desaiprasunn_quallsgarryd_2005]\] \[[Karlgaard, Christopher D. et al 2005][research_karlgaardchristopherd_martinjohng_2005]\] \[[Kazeminejad, B. et al 2005][research_kazeminejadb_atkinsondh_2005]\] \[[Kim 2005][research_kim_2005]\] \[[Sabzehparvar 2005][research_sabzehparvar_2005]\] \[[Santoro, Robert J. et al 2005][research_santororobertj_paksibtosh_2005]\] \[[Peters et al 2006][research_peters_brost_2006]\] \[[Polzin, Kurt A. et al 2006][research_polzinkurta_markusicthomase_2006]\] \[[Hoff 2007][research_hoff_2007]\] \[[Striepe, Scott A. et al 2007][research_striepescotta_blanchardrobertc_2007]\] \[[Tartabini, Paul V. 2007][research_tartabinipaulv_2007]\] \[[Imlach, Joseph et al 2008][research_imlachjoseph_kasardamary_2008]\] \[[Park, Ryan S. et al 2009][research_parkryans_bhaskaranshyam_2009]\] \[[Diamant, Kevin D. et al 2010][research_diamantkevind_pollardjamese_2010]\] \[[Moeller, Trevor and Polzin, Kurt A. 2010][research_moellertrevor_polzinkurta_2010]\] \[[Niehus and Mracek 2010][research_niehus_mracek_2010]\] \[[O'Keefe, Stephen A. and Bose, David M. 2010][research_okeefestephena_bosedavidm_2010]\] \[[Smith, Andrew and Harrison, Phil 2010][research_smithandrew_harrisonphil_2010]\] \[[Santos, Jose A. et al 2011][research_santosjosea_oishitomo_2011]\] \[[Tsuboi et al 2011][research_tsuboi_kawakami_2011]\] \[[Wong, Andrea R. et al 2011][research_wongandrear_polzinkurta_2011]\] \[[Wong, Andrea R. et al 2011][research_wongandrear_toftulalexandra_2011]\] \[[Hu and Wang 2012][research_hu_wang_2012]\] \[[Abilleira, Fernando 2013][research_abilleirafernando_2013]\] \[[Cassady, Leonard D. et al 2013][research_cassadyleonardd_rayerics_2013]\] \[[Karlgaard, Christopher D. et al 2013][research_karlgaardchristopherd_kuttyprasad_2013]\] \[[Lugo, Rafael A. et al 2013][research_lugorafaela_tolsonroberth_2013]\] \[[Olds, Aaron D. et al 2013][research_oldsaarond_beckroger_2013]\] \[[Polk, James E. et al 2013][research_polkjamese_pancottianthony_2013]\] \[[Stackpoole, M. et al 2013][research_stackpoolem_kaod_2013]\] \[[Feng et al 2014][research_feng_sun_2014]\] \[[Wagner, Sean 2014][research_wagnersean_2014]\] \[[Barth, Andrew et al 2015][research_barthandrew_mamichharvey_2015]\] \[[Dankanich, John et al 2015][research_dankanichjohn_aaneslandane_2015]\] \[[Takahashi et al 2015][research_takahashi_tomita_2015]\] \[[Ajith et al 2016][research_ajith_s_2016]\] \[[Bazin et al 2016][research_bazin_fields_2016]\] \[[Flight Test Data Analysis 2016][research_flight_test_2016]\] \[[Renitha P and Sivaramapandian J 2016][research_renithap_sivaramapandianj_2016]\] \[[Takahashi 2016][research_takahashi_2016]\] \[[Bronz et al 2017][research_bronz_garciademarina_2017]\] \[[Gong et al 2017][research_gong_maunder_2017]\] \[[Mahzari, Milad and White, Todd 2017][research_mahzarimilad_whitetodd_2017]\] \[[Alghamdi et al 2018][research_alghamdi_nadeem_2018]\] \[[Anzalone, Evan J. et al 2018][research_anzaloneevanj_johnstonhunter_2018]\] \[[Bullinger et al 2018][research_bullinger_bodensteiner_2018]\] \[[Del Mônaco Monteiro et al 2018][research_delmonacomonteiro_machiaverni_2018]\] \[[Lugo, Rafael A. et al 2018][research_lugorafaela_karlgaardchristopherd_2018]\] \[[Thiele et al 2018][research_thiele_gulhan_2018]\] \[[Williams, R. Anthony and Green, Justin S. 2018][research_williamsranthony_greenjustins_2018]\] \[[Xu and Lan 2018][research_xu_lan_2018]\] \[[Yu et al 2018][research_yu_yang_2018]\] \[[Abilleira, Fernando et al 2019][research_abilleirafernando_halsellallen_2019]\] \[[Chomputawat and Chatwiriya 2019][research_chomputawat_chatwiriya_2019]\] \[[Dutta, Soumyo and Green, Justin S. 2019][research_duttasoumyo_greenjustins_2019]\] \[[Soumyo Dutta 2020][research_soumyodutta_2020]\] \[[Soumyo Dutta et al 2020][research_soumyodutta_christopherdkarlgaard_2020]\] \[[Abilleira, Fernando et al 2021][research_abilleirafernando_kruizingagerard_2021]\] \[[Li et al 2021][research_li_qiao_2021]\] \[[Wang et al 2021][research_wang_an_2021]\] \[[Way, David W. and Brugarolas, Paul 2021][research_waydavidw_brugarolaspaul_2021]\] \[[Wei and Shao 2021][research_wei_shao_2021]\] \[[Tortora et al 2022][research_tortora_cordelli_2022]\] \[[Wang et al 2022][research_wang_an_2022]\] \[[Yamada et al 2022][research_yamada_nagata_2022]\] \[[Zhang et al 2022][research_zhang_zhang_2022]\] \[[Di Monaco et al 2023][research_dimonaco_dantuono_2023]\] \[[Siva et al 2023][research_siva_vikramasuriyan_2023]\] \[[Chen et al 2024][research_chen_chen_2024]\] \[[Sophia Vedvik and Christopher D Karlgaard 2024][research_sophiavedvik_christopherdkarlgaard_2024]\] \[[Wang et al 2024][research_wang_liang_2024]\] \[[Zhao et al 2024][research_zhao_he_2024]\] \[[Zhou et al 2024][research_zhou_xu_2024]\] \[[Choi and Kim 2025][research_choi_kim_2025]\] \[[Chris D Karlgaard et al 2025][research_chrisdkarlgaard_rafaelalugo_2025]\] \[[Elan M Graupe et al 2025][research_elanmgraupe_chrisdkarlgaard_2025]\] \[[Minaz and Meram 2025][research_minaz_meram_2025]\] \[[Wang et al 2025][research_wang_lian_2025]\] \[[Ahmed et al 2026][research_ahmed_mishra_2026]\] \[[Darby Vicker 2026][research_darbyvicker_2026]\] \[[Dobrodomov et al 2026][research_dobrodomov_proroka_2026]\] \[[Robbennolt and Munira 2026][research_robbennolt_munira_2026]\] \[[Toson et al 2026][research_toson_porcarelli_2026]\] \[[Advanced Ducted Propulsor In-Flight][research_advanced_ducted]\] \[[Christopher D Karlgaard et al][research_christopherdkarlgaard_rafaelalugo]\] \[[Christopher D Karlgaard et al][research_christopherdkarlgaard_rafaellugo]\] \[[Christopher D Karlgaard et al][research_christopherdkarlgaard_rohangdeshmukh]\] \[[Evan Anzalone et al][research_evananzalone_mikefritzinger]\] \[[Evan John Anzalone et al][research_evanjohnanzalone_gregdukeman]\] \[[Fernandes von Huelsen][research_fernandesvonhuelsen]\] \[[In-Flight Thrust Determination][research_in_flight_thrust_b]\] \[[In-Flight Thrust Determination for][research_in_flight_thrust]\] \[[Kent Frankovich et al][research_kentfrankovich_mahadevankrishnan]\] \[[Kent Frankovich et al][research_kentfrankovich_mahadevankrishnan_b]\] \[[Manish Mehta and Thomas B Steva][research_manishmehta_thomasbsteva]\] \[[Manish Mehta and Thomas Steva][research_manishmehta_thomassteva]\] \[[Manish Mehta et al][research_manishmehta_sheldondsmith]\] \[[Matthew P Fritz et al][research_matthewpfritz_javieradoll]\] \[[Ozelsel][research_ozelsel]\] \[[Propeller/Propfan In-Flight Thrust Determination][research_propeller_propfan_in_flight]\] \[[R. A. Miller et al][research_ramiller_hsalpert]\] \[[Richard Winski and Alejandro Pensado][research_richardwinski_alejandropensado]\] \[[Stephen et al][research_stephen_rajanna]\] \[[Time-Dependent In-Flight Thrust Determination][research_time_dependent_in_flight]\] \[[Uncertainty of In-Flight Thrust][research_uncertainty_of]\]

### The transducers, and what they are bonded to

**238 records.** \[[Gallagher, James J. 1948][research_gallagherjamesj_1948]\] \[[Jackson, H Herbert et al 1950][research_jacksonhherbert_rumseycharlesb_1950]\] \[[Purser, Paul E et al 1950][research_purserpaule_thibodauxjosephg_1950]\] \[[Jackson, H Herbert et al 1954][research_jacksonhherbert_rumseycharlesb_1954]\] \[[Sabin 1955][research_sabin_1955]\] \[[Sabin 1956][research_sabin_1956]\] \[[White 1957][research_white_1957]\] \[[Mull, Harold R. and Algranti, Joseph S. 1960][research_mullharoldr_algrantijosephs_1960]\] \[[Roshon 1960][research_roshon_1960]\] \[[Trott 1961][research_trott_1961]\] \[[Trott 1962][research_trott_1962]\] \[[Ziemer and Lambert 1962][research_ziemer_lambert_1962]\] \[[Baker et al 1965][research_baker_stockton_1965]\] \[[Miller, E. E. 1965][research_milleree_1965]\] \[[Hickam, W. M. and Sternbergh, S. A. 1966][research_hickamwm_sternberghsa_1966]\] \[[Pernet, D. F. 1966][research_pernetdf_1966]\] \[[Vacuum transducer calibration 1966][research_vacuum_transducer_1966]\] \[[Canfil, L. W. and Nieberding, W. C. 1967][research_canfillw_nieberdingwc_1967]\] \[[Carter, R. R. and Massey, G. A. 1967][research_carterrr_masseyga_1967]\] \[[Chalmers 1967][research_chalmers_1967]\] \[[Cullen, R. E. and Ragland, K. W. 1967][research_cullenre_raglandkw_1967]\] \[[Delmonte, J. 1967][research_delmontej_1967]\] \[[Ferris, D. J. 1967][research_ferrisdj_1967]\] \[[Loyd, J. R. and Pickard, R. F. 1967][research_loydjr_pickardrf_1967]\] \[[Schuler, A. E. 1967][research_schulerae_1967]\] \[[V E Horn 1967][research_vehorn_1967]\] \[[Hennen, H. A. and Lambert, R. F. 1968][research_hennenha_lambertrf_1968]\] \[[Miller, E. F. et al 1968][research_milleref_nieberdingwc_1968]\] \[[Schuler, A. E. 1968][research_schulerae_1968]\] \[[Hendrix, J. M. 1969][research_hendrixjm_1969]\] \[[Sita, E. R. 1969][research_sitaer_1969]\] \[[Hilten 1970][research_hilten_1970]\] \[[Martin and Brazzel 1970][research_martin_brazzel_1970]\] \[[Reinel 1970][research_reinel_1970]\] \[[Sabatini, R. R. and Rabchevsky, G. 1970][research_sabatinirr_rabchevskyg_1970]\] \[[Devries, L. L. 1971][research_devriesll_1971]\] \[[Price, E. A. et al 1971][research_priceea_hulljj_1971]\] \[[Strain gauge installation in 1971][research_strain_gauge_1971]\] \[[Clarke et al 1972][research_clarke_khayat_1972]\] \[[Johnson 1972][research_johnson_1972]\] \[[Lewis, T. L. and Dods, J. B., Jr. 1972][research_lewistl_dodsjbjr_1972]\] \[[Rogero, S. 1972][research_rogeros_1972]\] \[[Sule, W. P. and Mueller, T. J. 1973][research_sulewp_muellertj_1973]\] \[[Taylor et al 1973][research_taylor_simmons_1973]\] \[[Watters 1973][research_watters_1973]\] \[[Wilson, E. J. 1973][research_wilsonej_1973]\] \[[Livingstone 1974][research_livingstone_1974]\] \[[Prokopec 1974][research_prokopec_1974]\] \[[Kraft 1975][research_kraft_1975]\] \[[Tooth 1975][research_tooth_1975]\] \[[Pearson 1976][research_pearson_1976]\] \[[Jones and Bergquist 1977][research_jones_bergquist_1977]\] \[[Seifert and Shea 1977][research_seifert_shea_1977]\] \[[Vrolyk, John J. 1977][research_vrolykjohnj_1977]\] \[[Molland 1978][research_molland_1978]\] \[[Tang, M. H. et al 1978][research_tangmh_seficwj_1978]\] \[[Cook 1979][research_cook_1979]\] \[[Walter and Shaw 1979][research_walter_shaw_1979]\] \[[Bentzen 1980][research_bentzen_1980]\] \[[Galway 1980][research_galway_1980]\] \[[Transducer calibration 1980][research_transducer_calibration_1980]\] \[[Antonazzi 1981][research_antonazzi_1981]\] \[[Kidd 1981][research_kidd_1981]\] \[[Bradley, P. F. et al 1983][research_bradleypf_siemerspmiii_1983]\] \[[Transducer calibration tool 1983][research_transducer_calibration_1983]\] \[[Blanchard and Rutherford 1984][research_blanchard_rutherford_1984]\] \[[Electroacoustic Transducer Calibration Method 1984][research_electroacoustic_transducer_1984]\] \[[Electroacoustic transducer calibration method 1984][research_electroacoustic_transducer_1984_b]\] \[[James, K. and Quick, B. 1984][research_jamesk_quickb_1984]\] \[[Blanchard and Rutherford 1985][research_blanchard_rutherford_1985]\] \[[Schäfer et al 1985][research_schafer_krull_1985]\] \[[Berthold, III, John W. 1986][research_bertholdiiijohnw_1986]\] \[[Perry 1987][research_perry_1987]\] \[[Thompson et al 1987][research_thompson_russell_1987]\] \[[Ainsleigh et al 1988][research_ainsleigh_george_1988]\] \[[Irons, James R. and Irish, Richard R. 1988][research_ironsjamesr_irishrichardr_1988]\] \[[Keltner et al 1988][research_keltner_bainbridge_1988]\] \[[Bennink and Pate 1989][research_bennink_pate_1989]\] \[[Farokhi, S. and Vertzberger, M. 1989][research_farokhis_vertzbergerm_1989]\] \[[Williams, M. Susan 1989][research_williamsmsusan_1989]\] \[[Bayer, Janice I. et al 1991][research_bayerjanicei_varadanvv_1991]\] \[[Flanagan, Patrick M. 1991][research_flanaganpatrickm_1991]\] \[[Gellman, David I. et al 1991][research_gellmandavidi_biggarstuartf_1991]\] \[[George, William K. et al 1991][research_georgewilliamk_raewilliamj_1991]\] \[[Parzych, D. et al 1991][research_parzychd_boydl_1991]\] \[[Segal, Corin et al 1991][research_segalcorin_mcdanieljamesc_1991]\] \[[Whitmore, Stephen A. and Leondes, Cornelius T. 1991][research_whitmorestephena_leondescorneliust_1991]\] \[[Bennink and Pate 1992][research_bennink_pate_1992]\] \[[Bethea, Mark D. and Rosenthal, Bruce N. 1992][research_betheamarkd_rosenthalbrucen_1992]\] \[[Ficker 1992][research_ficker_1992]\] \[[Little 1992][research_little_1992]\] \[[Mallon, Joseph R., Jr. 1992][research_mallonjosephrjr_1992]\] \[[Mclachlan, B. G. et al 1992][research_mclachlanbg_belljh_1992]\] \[[Smith, William C. et al 1992][research_smithwilliamc_leiwekerobertj_1992]\] \[[Davis, W. S. et al 1993][research_davisws_eudellah_1993]\] \[[Egerev et al 1993][research_egerev_ovchinnikov_1993]\] \[[Gibson, Lorelei S. and Sealey, Bradley S. 1993][research_gibsonloreleis_sealeybradleys_1993]\] \[[Fichtel, Edward J. and Mcdaniel, Amos D. 1994][research_fichteledwardj_mcdanielamosd_1994]\] \[[Iaconis and D'Emilia 1994][research_iaconis_demilia_1994]\] \[[Semenov 1994][research_semenov_1994]\] \[[Reinersman, P. et al 1995][research_reinersmanp_carderkl_1995]\] \[[Lucht and Charest 1996][research_lucht_charest_1996]\] \[[Mcnichol, Randal S. 1996][research_mcnicholrandals_1996]\] \[[Wnuk, S. P., Jr. and Wnuk, V. P. 1997][research_wnukspjr_wnukvp_1997]\] \[[Lei, Jih-Fen et al 1998][research_leijihfen_willherberta_1998]\] \[[Peterson, Chariya et al 1998][research_petersonchariya_rowejohn_1998]\] \[[Applications of neural networks 1999][research_applications_of_1999]\] \[[Grosshandler 1999][research_grosshandler_1999]\] \[[John S Tripp 1999][research_johnstripp_1999]\] \[[Peterson, Chariya et al 1999][research_petersonchariya_rowejohn_1999]\] \[[Rai et al 1999][research_rai_brunt_1999]\] \[[Rhew, Ray D. 1999][research_rhewrayd_1999]\] \[[Tripp, John S. and Tcheng, Ping 1999][research_trippjohns_tchengping_1999]\] \[[Guimpilevich and Vertegel 2000][research_guimpilevich_vertegel_2000]\] \[[Hudson et al 2000][research_hudson_zoladz_2000]\] \[[Green, Robert O. et al 2001][research_greenroberto_pavribetina_2001]\] \[[Martin, Lisa C. et al 2001][research_martinlisac_wrbanekjohnd_2001]\] \[[Smith and Scott 2001][research_smith_scott_2001]\] \[[Hudson, Susan T. et al 2002][research_hudsonsusant_zoladzthomasf_2002]\] \[[Lerch, B. A. et al 2002][research_lerchba_nathalmv_2002]\] \[[Milos, Frank S. et al 2002][research_milosfranks_karunaratnek_2002]\] \[[Zhao 2002][research_zhao_2002]\] \[[Figueroa, Jorge et al 2003][research_figueroajorge_saintcyrwilliam_2003]\] \[[Sedlak, Joseph et al 2003][research_sedlakjoseph_weltergary_2003]\] \[[Wentz, Frank J. and Lawrence, Richard J. 2003][research_wentzfrankj_lawrencerichardj_2003]\] \[[Figueroa, Jorge et al 2004][research_figueroajorge_stcyrwilliam_2004]\] \[[Goodenow, Debra 2004][research_goodenowdebra_2004]\] \[[Iliopoulou et al 2004][research_iliopoulou_denos_2004]\] \[[Moore, Thomas C., Sr. 2004][research_moorethomascsr_2004]\] \[[Sedlak, Joseph and Hashmall, Joseph 2004][research_sedlakjoseph_hashmalljoseph_2004]\] \[[Zdenek and Anthenien 2004][research_zdenek_anthenien_2004]\] \[[Zuckerwar, Allan J. and Scott, Michael A. 2004][research_zuckerwarallanj_scottmichaela_2004]\] \[[Farr et al 2005][research_farr_wiley_2005]\] \[[Wang et al 2005][research_wang_ding_2005]\] \[[Chung 2006][research_chung_2006]\] \[[Jenne 2006][research_jenne_2006]\] \[[Knipp et al 2006][research_knipp_street_2006]\] \[[Champaigne and Sumners 2007][research_champaigne_sumners_2007]\] \[[Griffin and Sykes 2007][research_griffin_sykes_2007]\] \[[Wrbanek, John D. and Fralick, Gustave C. 2007][research_wrbanekjohnd_fralickgustavec_2007]\] \[[Guo et al 2008][research_guo_eriksen_2008]\] \[[Slane et al 2008][research_slane_morris_2008]\] \[[Wiley, John et al 2008][research_wileyjohn_kormanvalentin_2008]\] \[[Andrie 2009][research_andrie_2009]\] \[[Brown, Andrew et al 2009][research_brownandrew_rufjosephh_2009]\] \[[Carter 2009][research_carter_2009]\] \[[Mackey et al 2009][research_mackey_krasowski_2009]\] \[[Ripper et al 2009][research_ripper_dias_2009]\] \[[Arning et al 2010][research_arning_wu_2010]\] \[[Finley, Tom and Parker, Peter 2010][research_finleytom_parkerpeter_2010]\] \[[Oota et al 2010][research_oota_usuda_2010]\] \[[Xie 2010][research_xie_2010]\] \[[Ajovalasit 2011][research_ajovalasit_2011]\] \[[Baars, Woutijn J. et al 2011][research_baarswoutijnj_tinneycharlese_2011]\] \[[Dave et al 2011][research_dave_murty_2011]\] \[[Sheng and Hua 2011][research_sheng_hua_2011]\] \[[Zaman, Afroz et al 2011][research_zamanafroz_bauchmatthew_2011]\] \[[Cao 2012][research_cao_2012]\] \[[Hall 2012][research_hall_2012]\] \[[Lv et al 2012][research_lv_yu_2012]\] \[[Xiong, Xiaoxiong et al 2012][research_xiongxiaoxiong_wuaisheng_2012]\] \[[Ma et al 2013][research_ma_tang_2013]\] \[[Adamovsky, Grigory et al 2014][research_adamovskygrigory_mackeyjeffreyr_2014]\] \[[Niu et al 2014][research_niu_zhao_2014]\] \[[Zhou et al 2014][research_zhou_zhao_2014]\] \[[Zhou et al 2014][research_zhou_lin_2014]\] \[[Diaz, Carlos E., Jr. 2015][research_diazcarlosejr_2015]\] \[[Furuichi and Terao 2015][research_furuichi_terao_2015]\] \[[Irimpan et al 2015][research_irimpan_mannil_2015]\] \[[McCorkel, J. et al 2015][research_mccorkelj_czaplamyersj_2015]\] \[[Bąkowski et al 2016][research_bakowski_radziszewski_2016]\] \[[Gao et al 2016][research_gao_dai_2016]\] \[[King, Michael C. et al 2016][research_kingmichaelc_bognarjohn_2016]\] \[[Sarma et al 2016][research_sarma_sahoo_2016]\] \[[Wilson, Truman and Xiong, Xiaoxiong 2016][research_wilsontruman_xiongxiaoxiong_2016]\] \[[Yao et al 2016][research_yao_liang_2016]\] \[[Garg and Schiefer 2017][research_garg_schiefer_2017]\] \[[Gerlach et al 2017][research_gerlach_sanli_2017]\] \[[Lazarev et al 2017][research_lazarev_tarabrin_2017]\] \[[Platte et al 2017][research_platte_iwanczik_2017]\] \[[Tan 2017][research_tan_2017]\] \[[Alam and Kumar 2018][research_alam_kumar_2018]\] \[[Alam and Kumar 2018][research_alam_kumar_2018_b]\] \[[High-Load Strain Gauge Balance 2018][research_high_load_strain_2018]\] \[[Ksica et al 2018][research_ksica_hadas_2018]\] \[[Li et al 2018][research_li_sun_2018]\] \[[Nakabeppu and Dejima 2018][research_nakabeppu_dejima_2018]\] \[[Sarma et al 2018][research_sarma_sahoo_2018]\] \[[Bal et al 2019][research_bal_consoliverzack_2019]\] \[[Swanson, G. T. et al 2019][research_swansongt_millerra_2019]\] \[[Zheng et al 2019][research_zheng_zhao_2019]\] \[[Alam and Kumar 2020][research_alam_kumar_2020]\] \[[Jadhav et al 2020][research_jadhav_kulkarni_2020]\] \[[Nguyen et al 2020][research_nguyen_kostiukov_2020]\] \[[Raab and Rohde-Brandenburger 2020][research_raab_rohdebrandenburger_2020]\] \[[Usandizaga et al 2020][research_usandizaga_beard_2020]\] \[[Alam and Kumar 2021][research_alam_kumar_2021]\] \[[H S Alpert et al 2021][research_hsalpert_ramiller_2021]\] \[[Rajendran et al 2021][research_rajendran_ramalingame_2021]\] \[[Siroka et al 2021][research_siroka_foley_2021]\] \[[Sriharsha Madhavan et al 2021][research_sriharshamadhavan_junqiangsun_2021]\] \[[The Invention Relates to 2021][research_the_invention_2021]\] \[[Wejrzanowski et al 2021][research_wejrzanowski_tymicki_2021]\] \[[Hanapur et al 2022][research_hanapur_hiremath_2022]\] \[[Jin et al 2022][research_jin_tian_2022]\] \[[Kokuyama et al 2022][research_kokuyama_shimoda_2022]\] \[[Yang 2022][research_yang_2022]\] \[[Dongare et al 2023][research_dongare_peetala_2023]\] \[[Noroozinejad Farsangi and Karimi Pour 2023][research_noroozinejadfarsangi_karimipour_2023]\] \[[Veldman 2023][research_veldman_2023]\] \[[Xu et al 2023][research_xu_huang_2023]\] \[[Zhao et al 2023][research_zhao_zhao_2023]\] \[[Chivers and Filmore 2024][research_chivers_filmore_2024]\] \[[Dongare et al 2024][research_dongare_peetala_2024]\] \[[Dongare et al 2024][research_dongare_agrawal_2024]\] \[[Feng et al 2024][research_feng_shi_2024]\] \[[Wang et al 2024][research_wang_yao_2024]\] \[[Behera et al 2025][research_behera_panda_2025]\] \[[De Filippis et al 2025][research_defilippis_cappuccio_2025]\] \[[Dongare et al 2025][research_dongare_peetala_2025]\] \[[Frankel et al 2025][research_frankel_vergeer_2025]\] \[[Frankel et al 2025][research_frankel_vergeer_2025_b]\] \[[Gao et al 2025][research_gao_zhang_2025]\] \[[Schoenekess et al 2025][research_schoenekess_volkers_2025]\] \[[Hedrick et al 2026][research_hedrick_friman_2026]\] \[[Mireles Jr. et al 2026][research_mirelesjr_jimenez_2026]\] \[[Olivas et al 2026][research_olivas_vergeer_2026]\] \[[Qi et al 2026][research_qi_meng_2026]\] \[[Stoica et al 2026][research_stoica_dimarco_2026]\] \[[Zhang et al 2026][research_zhang_sheng_2026]\] \[[Zhang et al 2026][research_zhang_hu_2026]\] \[[David Doelling et al][research_daviddoelling_conorhaney]\] \[[Davis et al][research_davis_denison]\] \[[Galbraith et al][research_galbraith_hayward]\] \[[Guimpilevich and Vertegel][research_guimpilevich_vertegel]\] \[[Ibell][research_ibell]\] \[[Philip C Calhoun et al][research_philipccalhoun_jonathanglickman]\] \[[Robert Okojie et al][research_robertokojie_christianpetrov]\]

### Telemetry, recording, and what a link will actually carry

**742 records.** \[[Urban 1959][research_urban_1959]\] \[[Ratz 1960][research_ratz_1960]\] \[[Reeves, E. H., Jr. et al 1960][research_reevesehjr_stovalljr_1960]\] \[[Ludwig, George H. 1961][research_ludwiggeorgeh_1961]\] \[[Marko et al 1961][research_marko_mclennan_1961]\] \[[Viterbi, Andrew 1961][research_viterbiandrew_1961]\] \[[Adkins, F. L. and Griffin, C. E. 1962][research_adkinsfl_griffince_1962]\] \[[Baghdady, E. J. 1962][research_baghdadyej_1962]\] \[[Brummer, E. A. and Harrington, R. F. 1962][research_brummerea_harringtonrf_1962]\] \[[Choate, R. L. 1962][research_choaterl_1962]\] \[[Eichelberger, R. P. 1962][research_eichelbergerrp_1962]\] \[[Eichelberger, R. P. and Ratner, V. A. 1962][research_eichelbergerrp_ratnerva_1962]\] \[[Frost, W. O. 1962][research_frostwo_1962]\] \[[Harris, B. 1962][research_harrisb_1962]\] \[[Muehlner 1962][research_muehlner_1962]\] \[[Brummer, E. A. et al 1963][research_brummerea_harringtonrf_1963]\] \[[Feinberg, P. M. et al 1963][research_feinbergpm_leskojgjr_1963]\] \[[Fisher and Jr 1963][research_fisher_jr_1963]\] \[[Hauptschein, A. and Sommer, R. C. 1963][research_hauptscheina_sommerrc_1963]\] \[[Hill 1963][research_hill_1963]\] \[[Moore, W. M. 1963][research_moorewm_1963]\] \[[Ng 1963][research_ng_1963]\] \[[R. C. Chapman, Jr. et al 1963][research_rcchapmanjr_gfcritchlow_1963]\] \[[Reeves, E. H., Jr. and Threlkeld, W. B., Jr. 1963][research_reevesehjr_threlkeldwbjr_1963]\] \[[Singer et al 1963][research_singer_reinhardt_1963]\] \[[Titsworth, R. C. 1963][research_titsworthrc_1963]\] \[[Urban 1963][research_urban_1963]\] \[[Wye et al 1963][research_wye_teicher_1963]\] \[[Adolphsen, J. W. and Malinowski, A. B. 1964][research_adolphsenjw_malinowskiab_1964]\] \[[Averkin, E. G. et al 1964][research_averkineg_fryertb_1964]\] \[[Bailey, J. S. et al 1964][research_baileyjs_johnsondr_1964]\] \[[Barnes, W. P. et al 1964][research_barneswp_billingsleyjb_1964]\] \[[Creveling, C. J. 1964][research_crevelingcj_1964]\] \[[Feinberg, P. M. et al 1964][research_feinbergpm_leskojgjr_1964]\] \[[Grant, M. M. et al 1964][research_grantmm_stephanidescc_1964]\] \[[Higgins et al 1964][research_higgins_jacobson_1964]\] \[[Holmes, R. G. and Stagner, H. R. 1964][research_holmesrg_stagnerhr_1964]\] \[[Horiuchi, H. S. 1964][research_horiuchihs_1964]\] \[[Lechter, S. S. 1964][research_lechterss_1964]\] \[[Mahoney, M. and Quann, J. J. 1964][research_mahoneym_quannjj_1964]\] \[[Manders, A. M. and Sussman, S. M. 1964][research_mandersam_sussmansm_1964]\] \[[Mermagen 1964][research_mermagen_1964]\] \[[Mermagen 1964][research_mermagen_1964_b]\] \[[Stine 1964][research_stine_1964]\] \[[The design and performance 1964][research_the_design_1964]\] \[[Walt C Long 1964][research_waltclong_1964]\] \[[White, H. D., Jr. 1964][research_whitehdjr_1964]\] \[[Allen, K. J. and Wrigley, W. R. 1965][research_allenkj_wrigleywr_1965]\] \[[An examination of the 1965][research_an_examination_1965]\] \[[Bechtold, W. R. et al 1965][research_bechtoldwr_medlinje_1965]\] \[[Bloomquist, C. E. and Graham, W. C. 1965][research_bloomquistce_grahamwc_1965]\] \[[Buige, A. and Goode, W. 1965][research_buigea_goodew_1965]\] \[[Campbell, R. L. 1965][research_campbellrl_1965]\] \[[Creveling, C. J. 1965][research_crevelingcj_1965]\] \[[Czarcinski, E. A. et al 1965][research_czarcinskiea_maxwellms_1965]\] \[[Deboo, G. J. and Fryer, T. B. 1965][research_deboogj_fryertb_1965]\] \[[Des Jardins, R. and Wentz, L. H., Jr. 1965][research_desjardinsr_wentzlhjr_1965]\] \[[E Mozzi and S Roth 1965][research_emozzi_sroth_1965]\] \[[Eisenberger and Posner 1965][research_eisenberger_posner_1965]\] \[[Eliassen 1965][research_eliassen_1965]\] \[[Elms, C. P. 1965][research_elmscp_1965]\] \[[Furstenau 1965][research_furstenau_1965]\] \[[Griffin, M. A. et al 1965][research_griffinma_hassellhpjr_1965]\] \[[Hoff, H. L. 1965][research_hoffhl_1965]\] \[[Holmes, R. G. and Stagner, H. R. 1965][research_holmesrg_stagnerhr_1965]\] \[[Horiuchi, H. S. and Martin, N. L. 1965][research_horiuchihs_martinnl_1965]\] \[[Integral sensor telemetry final 1965][research_integral_sensor_1965]\] \[[Jamison, D. E. 1965][research_jamisonde_1965]\] \[[Mathison, R. P. 1965][research_mathisonrp_1965]\] \[[Medlin 1965][research_medlin_1965]\] \[[Mukhey, A. 1965][research_mukheya_1965]\] \[[Space vehicle sa-6 telemetry 1965][research_space_vehicle_1965]\] \[[Springett 1965][research_springett_1965]\] \[[Thin-film personal communications and 1965][research_thin_film_personal_1965]\] \[[Wang, C. C. 1965][research_wangcc_1965]\] \[[Weiner, B. J. 1965][research_weinerbj_1965]\] \[[Weiner, B. J. 1965][research_weinerbj_1965_b]\] \[[Adaptive compressive telemetry techniques 1966][research_adaptive_compressive_1966]\] \[[An analytical investigation of 1966][research_an_analytical_1966]\] \[[Anderson, J. D. 1966][research_andersonjd_1966]\] \[[Baer, J. A. and Heckler, C. H., Jr. 1966][research_baerja_hecklerchjr_1966]\] \[[Baer, J. A. and Heckler, C. H., Jr. 1966][research_baerja_hecklerchjr_1966_b]\] \[[Bassen and Jantz 1966][research_bassen_jantz_1966]\] \[[Bathker, D. A. and Clauss, R. C. 1966][research_bathkerda_claussrc_1966]\] \[[Bechtold, W. R. et al 1966][research_bechtoldwr_bjorntjr_1966]\] \[[Bowser and Busch 1966][research_bowser_busch_1966]\] \[[Brown, M. K. et al 1966][research_brownmk_griffinma_1966]\] \[[Burst transmission of PCM 1966][research_burst_transmission_1966]\] \[[Cote, C. E. 1966][research_cotece_1966]\] \[[Creveling, C. J. 1966][research_crevelingcj_1966]\] \[[Donaldson, H. M. et al 1966][research_donaldsonhm_griffinma_1966]\] \[[Emens, F. H. et al 1966][research_emensfh_frostwo_1966]\] \[[Frost, W. O. and Norvell, D. E. 1966][research_frostwo_norvellde_1966]\] \[[Fryer, T. B. 1966][research_fryertb_1966]\] \[[Griffin, M. A. et al 1966][research_griffinma_hassellhpjr_1966]\] \[[Holgersen, L. et al 1966][research_holgersenl_knutsone_1966]\] \[[Horton, J. A. et al 1966][research_hortonja_masseyhn_1966]\] \[[Husick and Ritenour 1966][research_husick_ritenour_1966]\] \[[Jamison, D. E. 1966][research_jamisonde_1966]\] \[[Kann, M. N. 1966][research_kannmn_1966]\] \[[Lokerson, D. C. 1966][research_lokersondc_1966]\] \[[M. J. Quinn 1966][research_mjquinn_1966]\] \[[Massey, H. N. 1966][research_masseyhn_1966]\] \[[Minderman, P. A. 1966][research_mindermanpa_1966]\] \[[Pasternack, M. 1966][research_pasternackm_1966]\] \[[Postal, R. B. and Potts, C. M. 1966][research_postalrb_pottscm_1966]\] \[[Research on microminiature passive 1966][research_research_on_1966]\] \[[Reynolds, L. W. and Tye, F. C. 1966][research_reynoldslw_tyefc_1966]\] \[[Sos, J. Y. 1966][research_sosjy_1966]\] \[[Thin-Film Personal Communications and 1966][research_thin_film_personal_1966]\] \[[Thin-Film Personal Communications and 1966][research_thin_film_personal_1966_b]\] \[[Trigg, H. W. 1966][research_trigghw_1966]\] \[[Zrubek, W. E. 1966][research_zrubekwe_1966]\] \[[Adair, B. M. and Polge, R. J. 1967][research_adairbm_polgerj_1967]\] \[[Anderson, T. O. and Gallo, A. J. 1967][research_andersonto_galloaj_1967]\] \[[Bassen 1967][research_bassen_1967]\] \[[Carl, C. 1967][research_carlc_1967]\] \[[Charles, F. J. and Larson, F. L. 1967][research_charlesfj_larsonfl_1967]\] \[[Conference on Adaptive Telemetry 1967][research_conference_on_1967]\] \[[Cote, C. E. and Cressey, J. R. 1967][research_cotece_cresseyjr_1967]\] \[[Creveling, C. J. 1967][research_crevelingcj_1967]\] \[[Eisenberger and Posner 1967][research_eisenberger_posner_1967]\] \[[George, W. V. 1967][research_georgewv_1967]\] \[[Graeve, E. and Massey, H. N. 1967][research_graevee_masseyhn_1967]\] \[[Husick and Ritenour 1967][research_husick_ritenour_1967]\] \[[Hynes, R. T. 1967][research_hynesrt_1967]\] \[[Kurtenbach, A. J. and Wintz, P. A. 1967][research_kurtenbachaj_wintzpa_1967]\] \[[Lynch, T. J. 1967][research_lynchtj_1967]\] \[[Lynch, T. J. 1967][research_lynchtj_1967_b]\] \[[Miller, W. et al 1967][research_millerw_mullerr_1967]\] \[[Pasternack, M. 1967][research_pasternackm_1967]\] \[[Research and advanced development 1967][research_research_and_1967]\] \[[Saliga, T. V. 1967][research_saligatv_1967]\] \[[Stein, M. 1967][research_steinm_1967]\] \[[Thin-Film Personal Communications and 1967][research_thin_film_personal_1967]\] \[[Thin-film Personal Communications and 1967][research_thin_film_personal_1967_b]\] \[[Adaptive telemetry systems Final 1968][research_adaptive_telemetry_1968]\] \[[Cox, F. B. et al 1968][research_coxfb_keipertfa_1968]\] \[[Easterling, M. F. et al 1968][research_easterlingmf_spearaj_1968]\] \[[Feinberg, P. M. and Townsend, M. R. 1968][research_feinbergpm_townsendmr_1968]\] \[[Fryer, T. B. 1968][research_fryertb_1968]\] \[[Harney, P. F. and Richardson, R. B. 1968][research_harneypf_richardsonrb_1968]\] \[[Houts, R. C. et al 1968][research_houtsrc_parsonsfd_1968]\] \[[Hynes, R. T. 1968][research_hynesrt_1968]\] \[[King, E. L. and Shaffer, H. W. 1968][research_kingel_shafferhw_1968]\] \[[Kurtenbach, A. J. and Wintz, P. A. 1968][research_kurtenbachaj_wintzpa_1968]\] \[[Miller, W. et al 1968][research_millerw_mullerr_1968]\] \[[Research, development, design, integration 1968][research_research_development_1968]\] \[[Simpson, R. S. and Tranter, W. H. 1968][research_simpsonrs_tranterwh_1968]\] \[[Sixteen channel microminiature FM 1968][research_sixteen_channel_1968]\] \[[Spacecraft telemetry and command 1968][research_spacecraft_telemetry_1968]\] \[[Telemetry modulation system MSC-TS-8A 1968][research_telemetry_modulation_1968]\] \[[Thin-Film Personal Communications and 1968][research_thin_film_personal_1968]\] \[[Antinone, R. et al 1969][research_antinoner_kowh_1969]\] \[[Bell, G. U. et al 1969][research_bellgu_hindspl_1969]\] \[[Borek, R. W. and Richardson, R. B. 1969][research_borekrw_richardsonrb_1969]\] \[[Crawford, W. L. and Reynolds, D. R. 1969][research_crawfordwl_reynoldsdr_1969]\] \[[Dannenberg, R. E. and Katzman, H. 1969][research_dannenbergre_katzmanh_1969]\] \[[Datnow, B. et al 1969][research_datnowb_fryertb_1969]\] \[[Easterling, M. F. et al 1969][research_easterlingmf_spearaj_1969]\] \[[Feinberg, P. et al 1969][research_feinbergp_maxwellm_1969]\] \[[Frost, W. O. et al 1969][research_frostwo_simpsonrs_1969]\] \[[Golden 1969][research_golden_1969]\] \[[Harrison and Lockman 1969][research_harrison_lockman_1969]\] \[[Hudgins, J. I. and Lease, J. R. 1969][research_hudginsji_leasejr_1969]\] \[[Karras, T. J. 1969][research_karrastj_1969]\] \[[Meigs and Stine 1969][research_meigs_stine_1969]\] \[[Panneton, R. J. and Warren, W. B. 1969][research_pannetonrj_warrenwb_1969]\] \[[Polge, R. J. and Wallace, G. R. 1969][research_polgerj_wallacegr_1969]\] \[[Posner, E. C. et al 1969][research_posnerec_rodemicher_1969]\] \[[Starner, D. L. 1969][research_starnerdl_1969]\] \[[Starner, D. L. 1969][research_starnerdl_1969_b]\] \[[Tranter, W. H. 1969][research_tranterwh_1969]\] \[[Velde et al 1969][research_velde_bentley_1969]\] \[[Visscher, J. 1969][research_visscherj_1969]\] \[[Arndt, G. D. et al 1970][research_arndtgd_novosadsw_1970]\] \[[Christensen, C. S. 1970][research_christensencs_1970]\] \[[Czarcinski, E. A. et al 1970][research_czarcinskiea_feinbergpm_1970]\] \[[Feinberg, P. and Maxwell, M. S. 1970][research_feinbergp_maxwellms_1970]\] \[[Frost, W. O. 1970][research_frostwo_1970]\] \[[Gilchriest, C. et al 1970][research_gilchriestc_goldsteinr_1970]\] \[[Gilder, J. R. et al 1970][research_gilderjr_gillmorewfjr_1970]\] \[[Glines, A. and Lazzaro, J. A. 1970][research_glinesa_lazzaroja_1970]\] \[[Homquest, D. L. 1970][research_homquestdl_1970]\] \[[Kulick, J. H. 1970][research_kulickjh_1970]\] \[[Lorio, L. A. 1970][research_loriola_1970]\] \[[Meigs and Stine 1970][research_meigs_stine_1970]\] \[[Underwood, T. C., Jr. 1970][research_underwoodtcjr_1970]\] \[[Brockman, M. H. 1971][research_brockmanmh_1971]\] \[[Burke, E. S. and Harris, C. W. 1971][research_burkees_harriscw_1971]\] \[[Butman, S. and Timor, U. 1971][research_butmans_timoru_1971]\] \[[Butman, S. and Timor, U. 1971][research_butmans_timoru_1971_b]\] \[[Butman, S. et al 1971][research_butmans_savageje_1971]\] \[[Clubb, J. J. 1971][research_clubbjj_1971]\] \[[Cramer, R. L. and Grant, T. L. 1971][research_cramerrl_granttl_1971]\] \[[Dawson, C. T. and Schmitt, N. M. 1971][research_dawsonct_schmittnm_1971]\] \[[Frost, W. O. and Ellis, D. H. 1971][research_frostwo_ellisdh_1971]\] \[[Hill, K. H. et al 1971][research_hillkh_leighouro_1971]\] \[[Jackson, W. H. and Eaton, J. P. 1971][research_jacksonwh_eatonjp_1971]\] \[[Lumb, D. R. 1971][research_lumbdr_1971]\] \[[Lumb, D. R. and Viterbi, A. J. 1971][research_lumbdr_viterbiaj_1971]\] \[[Miller, W. et al 1971][research_millerw_mullerr_1971]\] \[[Scaffidi, C. A. et al 1971][research_scaffidica_stocklinfj_1971]\] \[[Wintz, P. A. 1971][research_wintzpa_1971]\] \[[Burt, R. W. et al 1972][research_burtrw_hamnc_1972]\] \[[Fryer, T. B. et al 1972][research_fryertb_sandlerh_1972]\] \[[Hopkins, P. M. 1972][research_hopkinspm_1972]\] \[[Silverman, J. R. 1972][research_silvermanjr_1972]\] \[[Baldwin, H. A. and Freyman, R. W. 1973][research_baldwinha_freymanrw_1973]\] \[[Borek, R. W. 1973][research_borekrw_1973]\] \[[Broglio, C. J. 1973][research_brogliocj_1973]\] \[[Butman, S. and Timor, U. 1973][research_butmans_timoru_1973]\] \[[Crosswy, F. L. and Hornkohl, J. O. 1973][research_crosswyfl_hornkohljo_1973]\] \[[Easton, R. A. and Hilbert, E. E. 1973][research_eastonra_hilbertee_1973]\] \[[Peterson, M. R. 1973][research_petersonmr_1973]\] \[[Pickett, R. B. and Matthews, F. L. 1973][research_pickettrb_matthewsfl_1973]\] \[[Smith, R. and Carr, T. 1973][research_smithr_carrt_1973]\] \[[Task four report Telemetry 1973][research_task_four_1973]\] \[[Chen, T. T. et al 1974][research_chentt_bohningod_1974]\] \[[Evanchuk, V. L. 1974][research_evanchukvl_1974]\] \[[Fain, L. T. and Cribb, H. E. 1974][research_fainlt_cribbhe_1974]\] \[[Finger, H. J. and Cambra, J. M. 1974][research_fingerhj_cambrajm_1974]\] \[[Fryer, T. B. 1974][research_fryertb_1974]\] \[[Kantor, A. V. et al 1974][research_kantorav_perevertkinsm_1974]\] \[[Pitts, K. J. 1974][research_pittskj_1974]\] \[[Snider, W. J. 1974][research_sniderwj_1974]\] \[[Tolmadzheva, T. A. et al 1974][research_tolmadzhevata_kantorav_1974]\] \[[Wood, G. E. and Risa, T. 1974][research_woodge_risat_1974]\] \[[Evans, S. A. et al 1975][research_evanssa_grosskw_1975]\] \[[Fryer, T. B. et al 1975][research_fryertb_sandlerh_1975]\] \[[Gilley, G. C. 1975][research_gilleygc_1975]\] \[[Griffin, D. C., Jr. 1975][research_griffindcjr_1975]\] \[[Mulhall, B. D. L. et al 1975][research_mulhallbdl_benjauthritb_1975]\] \[[Peterson, M. R. 1975][research_petersonmr_1975]\] \[[Real time telemetry and 1975][research_real_time_1975]\] \[[Weathers, G. 1975][research_weathersg_1975]\] \[[Benjauthrit, B. 1976][research_benjauthritb_1976]\] \[[Benjauthrit, B. et al 1976][research_benjauthritb_mulhallb_1976]\] \[[Gatz, E. C. 1976][research_gatzec_1976]\] \[[Greene, E. P. 1976][research_greeneep_1976]\] \[[Greenhall, C. A. 1976][research_greenhallca_1976]\] \[[King 1976][research_king_1976]\] \[[Konigsberg, E. 1976][research_konigsberge_1976]\] \[[Wilcher, J. H. 1976][research_wilcherjh_1976]\] \[[Anson, K. W. 1977][research_ansonkw_1977]\] \[[Benjauthrit, B. and Kemp, R. P. 1977][research_benjauthritb_kemprp_1977]\] \[[Fryer, T. B. et al 1977][research_fryertb_mccutcheonep_1977]\] \[[Gatz, E. C. 1977][research_gatzec_1977]\] \[[Low, P. W. 1977][research_lowpw_1977]\] \[[Marks 1977][research_marks_1977]\] \[[Mccutcheon, E. P. et al 1977][research_mccutcheonep_mirandar_1977]\] \[[Salter, W. E. 1977][research_salterwe_1977]\] \[[Young, D. R. et al 1977][research_youngdr_howardwh_1977]\] \[[Brockman, M. H. 1978][research_brockmanmh_1978]\] \[[Fryer, T. B. et al 1978][research_fryertb_corbinsd_1978]\] \[[Fryer, T. B. et al 1978][research_fryertb_lundgf_1978]\] \[[Greene and Desjardins 1978][research_greene_desjardins_1978]\] \[[Greene, E. P. 1978][research_greeneep_1978]\] \[[Greene, E. P. 1978][research_greeneep_1978_b]\] \[[Lord 1978][research_lord_1978]\] \[[Medical Telemetry 1978][research_medical_telemetry_1978]\] \[[Rey, R. D. and Nipper, E. J. 1978][research_reyrd_nipperej_1978]\] \[[Smith 1978][research_smith_1978]\] \[[Stermer, R. L., Jr. 1978][research_stermerrljr_1978]\] \[[Gatz, E. C. 1979][research_gatzec_1979]\] \[[Holmes, J. K. 1979][research_holmesjk_1979]\] \[[Hooke 1979][research_hooke_1979]\] \[[Ko, W. H. et al 1979][research_kowh_hynecekj_1979]\] \[[Rosatino, S. A. and Westbrook, R. M. 1979][research_rosatinosa_westbrookrm_1979]\] \[[Schneider, W. C. and Garman, A. A. 1979][research_schneiderwc_garmanaa_1979]\] \[[Bell, H. and Strock, J. 1980][research_bellh_strockj_1980]\] \[[Christensen, C. S. et al 1980][research_christensencs_moultrieb_1980]\] \[[Cipolle, D. J. 1980][research_cipolledj_1980]\] \[[Erickson et al 1980][research_erickson_craddock_1980]\] \[[Giles and Whitford 1980][research_giles_whitford_1980]\] \[[Renz, R. R. L. et al 1980][research_renzrrl_clarker_1980]\] \[[Stevens, G. L. 1980][research_stevensgl_1980]\] \[[Brockman, M. H. and Easterling, M. F. 1981][research_brockmanmh_easterlingmf_1981]\] \[[Burt, R. 1981][research_burtr_1981]\] \[[Glenn A Bever 1981][research_glennabever_1981]\] \[[Harney, P. F. 1981][research_harneypf_1981]\] \[[Meredith et al 1981][research_meredith_kelly_1981]\] \[[Renz, R. R. L. 1981][research_renzrrl_1981]\] \[[Schneider and Garman 1981][research_schneider_garman_1981]\] \[[Stephison, D. B. 1981][research_stephisondb_1981]\] \[[Sue, M. K. 1981][research_suemk_1981]\] \[[Wechsler, E. R. 1981][research_wechslerer_1981]\] \[[Burt, R. 1982][research_burtr_1982]\] \[[Carreno, V. A. 1982][research_carrenova_1982]\] \[[Clarke, R. et al 1982][research_clarker_shaned_1982]\] \[[Deutsch, L. J. 1982][research_deutschlj_1982]\] \[[Implantable telemetry for small 1982][research_implantable_telemetry_1982]\] \[[Rummer, D. I. et al 1982][research_rummerdi_mosserma_1982]\] \[[Spahn, C. J. and Pena, C. D. 1982][research_spahncj_penacd_1982]\] \[[Sue, M. K. 1982][research_suemk_1982]\] \[[Yuen, J. H. et al 1982][research_yuenjh_divsalard_1982]\] \[[Deutsch, L. J. 1983][research_deutschlj_1983]\] \[[Kinman, P. W. 1983][research_kinmanpw_1983]\] \[[Space Telemetry for the 1983][research_space_telemetry_1983]\] \[[Srijayantha, M. 1983][research_srijayantham_1983]\] \[[Cruickshank 1984][research_cruickshank_1984]\] \[[Glenn A Bever 1984][research_glennabever_1984]\] \[[Koerner, M. A. 1984][research_koernerma_1984]\] \[[Stevens, R. 1984][research_stevensr_1984]\] \[[Boykin, F. M. 1985][research_boykinfm_1985]\] \[[Carreno, V. A. 1985][research_carrenova_1985]\] \[[Hooke, A. J. and Greenberg, E. 1985][research_hookeaj_greenberge_1985]\] \[[Macmedan, M. L. 1985][research_macmedanml_1985]\] \[[Ross, D. L. 1985][research_rossdl_1985]\] \[[Stokes, J. H. and Ward, S. M. 1985][research_stokesjh_wardsm_1985]\] \[[Barthelme, N. et al 1986][research_barthelmen_leej_1986]\] \[[Briscoe 1986][research_briscoe_1986]\] \[[Carreno, Victor A. 1986][research_carrenovictora_1986]\] \[[Glenn A Bever 1986][research_glennabever_1986]\] \[[Jenkins, George 1986][research_jenkinsgeorge_1986]\] \[[Massey, D. E. 1986][research_masseyde_1986]\] \[[Urech, J. M. et al 1986][research_urechjm_chamarroa_1986]\] \[[Watters, D. M. 1986][research_wattersdm_1986]\] \[[Bryant, Thomas et al 1987][research_bryantthomas_crusebryant_1987]\] \[[Connell, Edward B. et al 1987][research_connelledwardb_howelldavidr_1987]\] \[[Flagg, Howard S. and Kalil, Lou F. 1987][research_flagghowards_kalillouf_1987]\] \[[Graham, Olin L. 1987][research_grahamolinl_1987]\] \[[Kao, Simon A. et al 1987][research_kaosimona_laffeythomasj_1987]\] \[[Lewallen, Pat 1987][research_lewallenpat_1987]\] \[[Madsen, Boyd D. 1987][research_madsenboydd_1987]\] \[[Muratore, John F. 1987][research_muratorejohnf_1987]\] \[[Thomas, Mitchel E. and Diamond, John K. 1987][research_thomasmitchele_diamondjohnk_1987]\] \[[Whitelaw, Virginia A. 1987][research_whitelawvirginiaa_1987]\] \[[Bechtel, R. D. et al 1988][research_bechtelrd_mateosma_1988]\] \[[Carper, Richard D. 1988][research_carperrichardd_1988]\] \[[Carraway, Preston I., III 1988][research_carrawayprestoniiii_1988]\] \[[Hurd, W. J. et al 1988][research_hurdwj_browndh_1988]\] \[[Leng, Christopher and Peet, Arthur 1988][research_lengchristopher_peetarthur_1988]\] \[[Mouneimne, Samih A. 1988][research_mouneimnesamiha_1988]\] \[[Nguyen, T. M. 1988][research_nguyentm_1988]\] \[[Pettit, Richard L., Jr. 1988][research_pettitrichardljr_1988]\] \[[Sabia, Steve and Hand, Sarah 1988][research_sabiasteve_handsarah_1988]\] \[[Tcheng, Ping et al 1988][research_tchengping_schotttimothyd_1988]\] \[[Collins, Aaron S. 1989][research_collinsaarons_1989]\] \[[Collins, Aaron et al 1989][research_collinsaaron_dominycarol_1989]\] \[[Dalton, John T. 1989][research_daltonjohnt_1989]\] \[[Diamond, John K. 1989][research_diamondjohnk_1989]\] \[[Horner, Ward and Sabia, Steve 1989][research_hornerward_sabiasteve_1989]\] \[[Ingels, Frank et al 1989][research_ingelsfrank_parkerglenn_1989]\] \[[Koerner, M. A. 1989][research_koernerma_1989]\] \[[Lawson, Denise L. and James, Mark L. 1989][research_lawsondenisel_jamesmarkl_1989]\] \[[Lawson, Denise L. and James, Mark L. 1989][research_lawsondenisel_jamesmarkl_1989_b]\] \[[Pritchard, James A. 1989][research_pritchardjamesa_1989]\] \[[Sayood, Khalid and Rost, Martin C. 1989][research_sayoodkhalid_rostmartinc_1989]\] \[[Sinderson, R. L. et al 1989][research_sindersonrl_salazarga_1989]\] \[[Wike, Jeffrey and Griffith, Paul 1989][research_wikejeffrey_griffithpaul_1989]\] \[[Advanced telemetry systems for 1990][research_advanced_telemetry_1990]\] \[[Carper, Richard D. and Stallings, William H., III 1990][research_carperrichardd_stallingswilliamhiii_1990]\] \[[Hooke, Adrian J. et al 1990][research_hookeadrianj_macmedanmervynl_1990]\] \[[Massey, David and Corbin, Brian 1990][research_masseydavid_corbinbrian_1990]\] \[[Miller, Warner H. et al 1990][research_millerwarnerh_morakisjamesc_1990]\] \[[Nguyen, T. M. 1990][research_nguyentm_1990]\] \[[Nguyen, Tien M. 1990][research_nguyentienm_1990]\] \[[Ross, D. L. 1990][research_rossdl_1990]\] \[[Dominy, Carol T. et al 1991][research_dominycarolt_chesneyjamesr_1991]\] \[[Glenn A Bever 1991][research_glennabever_1991]\] \[[Glenn A Bever 1991][research_glennabever_1991_b]\] \[[Hinedi, S. et al 1991][research_hinedis_bevanr_1991]\] \[[Massey, D. E. and Corbin, B. 1991][research_masseyde_corbinb_1991]\] \[[Morris, R. A. et al 1991][research_morrisra_powellwr_1991]\] \[[Nguyen, Tien M. 1991][research_nguyentienm_1991]\] \[[Nguyen, Tien M. 1991][research_nguyentienm_1991_b]\] \[[Berman, A. L. and Au, P. A. 1992][research_bermanal_aupa_1992]\] \[[Bessant and Knight 1992][research_bessant_knight_1992]\] \[[Kirkham, Harold 1992][research_kirkhamharold_1992]\] \[[Nguyen, Tien M. 1992][research_nguyentienm_1992]\] \[[Nguyen, Tien Manh 1992][research_nguyentienmanh_1992]\] \[[Ruth et al 1992][research_ruth_colburn_1992]\] \[[Schneider, John R. 1992][research_schneiderjohnr_1992]\] \[[Valdes 1992][research_valdes_1992]\] \[[Anderson, Karl F. 1993][research_andersonkarlf_1993]\] \[[Arcangeli, J.-P. et al 1993][research_arcangelijp_crochemorem_1993]\] \[[Girouard, Forrest R. and Hopkins, Allen 1993][research_girouardforrestr_hopkinsallen_1993]\] \[[Hinedi, Sami M. et al 1993][research_hinedisamim_bevanrolandp_1993]\] \[[Hyde, Charles R. and Massie, Jeffrey J. 1993][research_hydecharlesr_massiejeffreyj_1993]\] \[[Jones and Jr 1993][research_jones_jr_1993]\] \[[Lesho, Jeffery C. and Eaton, Harry A. C. 1993][research_leshojefferyc_eatonharryac_1993]\] \[[Nguyen, Tien M. et al 1993][research_nguyentienm_hinedisamim_1993]\] \[[Thorn, Karen E. 1993][research_thornkarene_1993]\] \[[Tsou, H. et al 1993][research_tsouh_shahb_1993]\] \[[Wells, George and Baroth, Edmund C. 1993][research_wellsgeorge_barothedmundc_1993]\] \[[Douard, Stephane 1994][research_douardstephane_1994]\] \[[El-Ghazawi, Tarek A. et al 1994][research_elghazawitareka_pritchardjim_1994]\] \[[Fogel, Alvin J. 1994][research_fogelalvinj_1994]\] \[[Kan, E. 1994][research_kane_1994]\] \[[Kan, Edwin P. 1994][research_kanedwinp_1994]\] \[[Koeberlein, Ernest, III and Pender, Shaw Exum 1994][research_koeberleinernestiii_pendershawexum_1994]\] \[[Loubeyre, Jean Philippe 1994][research_loubeyrejeanphilippe_1994]\] \[[Medelius, Pedro J. et al 1994][research_medeliuspedroj_hallbergcarl_1994]\] \[[Quinto, P. Frank and Orie, Nettie M. 1994][research_quintopfrank_orienettiem_1994]\] \[[Shihabi, Mazen M. et al 1994][research_shihabimazenm_nguyentienmanh_1994]\] \[[Simmons, Charles 1994][research_simmonscharles_1994]\] \[[Sorensen, Erik Mose and Ferri, Paolo 1994][research_sorensenerikmose_ferripaolo_1994]\] \[[Srinivasan, Jefferey M. and Lichten, Stephen M. 1994][research_srinivasanjeffereym_lichtenstephenm_1994]\] \[[Wells, G. and Baroth, E. 1994][research_wellsg_barothe_1994]\] \[[Anderson, Karl F. 1995][research_andersonkarlf_1995]\] \[[Andrew Roberts and Claude Hashem 1995][research_andrewroberts_claudehashem_1995]\] \[[Bloise, Anthony 1995][research_bloiseanthony_1995]\] \[[Bufalino 1995][research_bufalino_1995]\] \[[Day, John C. 1995][research_dayjohnc_1995]\] \[[Hines, John W. et al 1995][research_hinesjohnw_sompschris_1995]\] \[[Hummel 1995][research_hummel_1995]\] \[[Maurer 1995][research_maurer_1995]\] \[[Sidorovich 1995][research_sidorovich_1995]\] \[[Tsou, Haiping et al 1995][research_tsouhaiping_hinedisamim_1995]\] \[[Miller, Geoffrey et al 1996][research_millergeoffrey_richwinedavidm_1996]\] \[[Patel, P. 1996][research_patelp_1996]\] \[[Sazani et al 1996][research_sazani_mau_1996]\] \[[Telemetry Systems 1996][research_telemetry_systems_1996]\] \[[Blue, Lisa and Crawford, Kevin 1997][research_bluelisa_crawfordkevin_1997]\] \[[Kinney, Frank 1997][research_kinneyfrank_1997]\] \[[Telemetry Technology 1997][research_telemetry_technology_1997]\] \[[Boyadzhyan, V. V. 1998][research_boyadzhyanvv_1998]\] \[[Burkes, Darryl A. 1998][research_burkesdarryla_1998]\] \[[Crawford, Kevin and Pinkleton, David 1998][research_crawfordkevin_pinkletondavid_1998]\] \[[Data Acquisition System DAS 1998][research_data_acquisition_1998]\] \[[Development of an onboard 1998][research_development_of_1998]\] \[[Drews, Michael E. et al 1998][research_drewsmichaele_formandouglasa_1998]\] \[[Fantini, Jay A. 1998][research_fantinijaya_1998]\] \[[Haddock, Paul C. and Horan, Stephen 1998][research_haddockpaulc_horanstephen_1998]\] \[[Huegel, Fred 1998][research_huegelfred_1998]\] \[[Medelius, Pedro J. et al 1998][research_medeliuspedroj_hallbergcarlg_1998]\] \[[Normyle 1998][research_normyle_1998]\] \[[Sea Technology Arlington Va 1998][research_seatechnologyarlingtonva_1998]\] \[[Wang 1998][research_wang_1998]\] \[[Baggeroer 1999][research_baggeroer_1999]\] \[[Betancourt-Zamora, Rafael J. 1999][research_betancourtzamorarafaelj_1999]\] \[[Crawford, Kevin and Pinkleton, David 1999][research_crawfordkevin_pinkletondavid_1999]\] \[[Crawford, Kevin et al 1999][research_crawfordkevin_huberharold_1999]\] \[[Gonsalves et al 1999][research_gonsalves_ivanov_1999]\] \[[Rice 1999][research_rice_1999]\] \[[Calderon, M. 2000][research_calderonm_2000]\] \[[D'Amico 2000][research_damico_2000]\] \[[Integrated Advanced Microwave Sounding 2000][research_integrated_advanced_2000]\] \[[Jiang, Hui and Horan, Stephen 2000][research_jianghui_horanstephen_2000]\] \[[Kennedy, Paul and Sims, Herb 2000][research_kennedypaul_simsherb_2000]\] \[[Kohtake et al 2000][research_kohtake_kawabata_2000]\] \[[Norris, J. S. et al 2000][research_norrisjs_backesp_2000]\] \[[Paschke 2000][research_paschke_2000]\] \[[Ryan 2000][research_ryan_2000]\] \[[Yamada 2000][research_yamada_2000]\] \[[Zahzah, Mohamad et al 2000][research_zahzahmohamad_korkoszgregoryj_2000]\] \[[Alhorn, Dean C. et al 2001][research_alhorndeanc_howarddavide_2001]\] \[[Grace 2001][research_grace_2001]\] \[[Jensen 2001][research_jensen_2001_b]\] \[[Morgan, Dwayne R. et al 2001][research_morgandwayner_streichrong_2001]\] \[[Streich, Ronald C. et al 2001][research_streichronaldc_morgandwayner_2001]\] \[[Wilson, E. 2001][research_wilsone_2001]\] \[[Fincannon, H. James 2002][research_fincannonhjames_2002]\] \[[Jannette, Anthony G. et al 2002][research_jannetteanthonyg_hojnickijeffreys_2002]\] \[[Jensen 2002][research_jensen_2002]\] \[[Shell, Michael T. and McElyea, Richard M. 2002][research_shellmichaelt_mcelyearichardm_2002]\] \[[Fincannon, H. James 2003][research_fincannonhjames_2003]\] \[[Fort, David et al 2003][research_fortdavid_rogstaddavid_2003]\] \[[Horan 2003][research_horan_2003]\] \[[Jensen 2003][research_jensen_2003]\] \[[Kirby, Randy L. et al 2003][research_kirbyrandyl_manndavid_2003]\] \[[Prasad and Pal 2003][research_prasad_pal_2003]\] \[[Rainee N Simons and Felix A Miranda 2003][research_raineensimons_felixamiranda_2003]\] \[[Speer, Dave 2003][research_speerdave_2003]\] \[[Demspm. Erol et al 2004][research_demspmerol_valencialisam_2004]\] \[[Hase 2004][research_hase_2004]\] \[[Hogie, Keith et al 2004][research_hogiekeith_crisuoloed_2004]\] \[[Martinez, Elmain et al 2004][research_martinezelmain_mcauleymyche_2004]\] \[[McLeod, Christopher 2004][research_mcleodchristopher_2004]\] \[[Pedro J Medelius et al 2004][research_pedrojmedelius_carlostmata_2004]\] \[[Simons, Rainee N. et al 2004][research_simonsraineen_halldavidg_2004]\] \[[Washburn 2004][research_washburn_2004]\] \[[Wilson 2004][research_wilson_2004]\] \[[Yairi et al 2004][research_yairi_ogasawara_2004]\] \[[Dimmock, John O. 2005][research_dimmockjohno_2005]\] \[[Moore 2005][research_moore_2005]\] \[[Semmel, Glenn S. et al 2005][research_semmelglenns_davisstevenr_2005]\] \[[Whiteman, Donald E. et al 2005][research_whitemandonalde_valencialisam_2005]\] \[[Whiteman, Donald E. et al 2005][research_whitemandonalde_valencialisam_2005_b]\] \[[Faulstich and Law 2006][research_faulstich_law_2006]\] \[[Franz, Russ et al 2006][research_franzruss_pestanamark_2006]\] \[[OBrien, Robin A. 2006][research_obrienrobina_2006]\] \[[Okino, Clayton et al 2006][research_okinoclayton_gaojay_2006]\] \[[Rodriguez et al 2006][research_rodriguez_ready_2006]\] \[[Simons, Rainee N. et al 2006][research_simonsraineen_mirandafelixa_2006]\] \[[Specht, Ted and Noble, David 2006][research_spechtted_nobledavid_2006]\] \[[Sturdevant et al 2006][research_sturdevant_wright_2006]\] \[[Knopf, William P. 2007][research_knopfwilliamp_2007]\] \[[Lin, Chujen et al 2007][research_linchujen_lonskeben_2007]\] \[[Snowden and Levinson 2007][research_snowden_levinson_2007]\] \[[Ardalan, S.M. et al 2008][research_ardalansm_antreasianpg_2008]\] \[[Kim et al 2008][research_kim_keidar_2008]\] \[[Losik 2008][research_losik_2008]\] \[[Next-Generation Telemetry Workstation 2008][research_next_generation_telemetry_2008]\] \[[Powell, Mark et al 2008][research_powellmark_mittmandavid_2008]\] \[[Simons, Rainee N. et al 2008][research_simonsraineen_mirandafelixa_2008]\] \[[Bagri and Majid 2009][research_bagri_majid_2009]\] \[[Davydov and Sazonov 2009][research_davydov_sazonov_2009]\] \[[Determining Aliasing in Isolated 2009][research_determining_aliasing_2009]\] \[[Inui et al 2009][research_inui_kawahara_2009]\] \[[LaBelle, Remi et al 2009][research_labelleremi_bernardoabner_2009]\] \[[Oxer and Blemings 2009][research_oxer_blemings_2009]\] \[[Stoneking, Eric T. and Tsai, Dean 2009][research_stonekingerict_tsaidean_2009]\] \[[Telemetry Boards Interpret Rocket 2009][research_telemetry_boards_2009]\] \[[Apollo 11 Telemetry Data 2010][research_apollo_11_2010]\] \[[Beyon, J. Y. et al 2010][research_beyonjy_kochgj_2010]\] \[[Breed, Kelly S. et al 2010][research_breedkellys_powellmarkw_2010]\] \[[Bryant 2010][research_bryant_2010]\] \[[Leachman, Jonathan 2010][research_leachmanjonathan_2010]\] \[[Losik 2010][research_losik_2010]\] \[[Losik 2010][research_losik_2010_b]\] \[[Losik 2010][research_losik_2010_c]\] \[[Luan et al 2010][research_luan_tang_2010]\] \[[Mackey and Kulikov 2010][research_mackey_kulikov_2010]\] \[[Moore, Charlotte 2010][research_moorecharlotte_2010]\] \[[Mukai, Ryan and Vilnrotter, Victor 2010][research_mukairyan_vilnrottervictor_2010]\] \[[Parkes and Armbruster 2010][research_parkes_armbruster_2010]\] \[[Rice, Kevin et al 2010][research_ricekevin_kizzortbrad_2010]\] \[[Sepan and Lawrence 2010][research_sepan_lawrence_2010]\] \[[Sherman, Aaron 2010][research_shermanaaron_2010]\] \[[Stoneking et al 2010][research_stoneking_shah_2010]\] \[[Ahmad, Mohammad et al 2011][research_ahmadmohammad_tranthanh_2011]\] \[[Bates, Lakesha and Hong, Liang 2011][research_bateslakesha_hongliang_2011]\] \[[Fang et al 2011][research_fang_zou_2011]\] \[[Fielhauer, K. B. and Boone, B. G. 2011][research_fielhauerkb_boonebg_2011]\] \[[Fillery and Stanton 2011][research_fillery_stanton_2011]\] \[[Fresconi and Harkins 2011][research_fresconi_harkins_2011]\] \[[Fukushima 2011][research_fukushima_2011]\] \[[Griebeler, Elmer et al 2011][research_griebelerelmer_nawashnuha_2011]\] \[[Hamkins, Jon et al 2011][research_hamkinsjon_vilnrottervictora_2011]\] \[[OFarrell, Zachary L. 2011][research_ofarrellzacharyl_2011]\] \[[Silva-Opps and B. 2011][research_silvaopps_b_2011]\] \[[Yang et al 2011][research_yang_zhang_2011]\] \[[Beyon, Jeffrey Y. et al 2012][research_beyonjeffreyy_kochgradyj_2012]\] \[[Burnside, Jathan J. 2012][research_burnsidejathanj_2012]\] \[[Fang et al 2012][research_fang_yixing_2012]\] \[[Fang et al 2012][research_fang_ma_2012]\] \[[Fitch, Jeffery T. et al 2012][research_fitchjefferyt_simonalanl_2012]\] \[[Hunter, Gary W. and Behbahani, Alireza 2012][research_huntergaryw_behbahanialireza_2012]\] \[[Jiang et al 2012][research_jiang_dong_2012]\] \[[Lee, Hyun H. 2012][research_leehyunh_2012]\] \[[Losik 2012][research_losik_2012]\] \[[Losik 2012][research_losik_2012_b]\] \[[Losik 2012][research_losik_2012_c]\] \[[Perrins 2012][research_perrins_2012]\] \[[Pomerantz, M. I. et al 2012][research_pomerantzmi_limc_2012]\] \[[R. et al 2012][research_r_mi_2012]\] \[[Swanson, Gregory T. et al 2012][research_swansongregoryt_empeydanielm_2012]\] \[[Vorontsov and Samoilov 2012][research_vorontsov_samoilov_2012]\] \[[Ayoung-Chee et al 2013][research_ayoungchee_mack_2013]\] \[[Cheyne et al 2013][research_cheyne_key_2013]\] \[[Gao et al 2013][research_gao_zhang_2013]\] \[[Li Guojun et al 2013][research_liguojun_shijian_2013]\] \[[Marquez 2013][research_marquez_2013]\] \[[Nye 2013][research_nye_2013]\] \[[Rice 2013][research_rice_2013]\] \[[Stanboli, Alice 2013][research_stanbolialice_2013]\] \[[Stanboli, Alice et al 2013][research_stanbolialice_martinezelmainm_2013]\] \[[Takacs 2013][research_takacs_2013]\] \[[Varnavas, Kosta A. and Sims, William Herbert, III 2013][research_varnavaskostaa_simswilliamherbertiii_2013]\] \[[Vidya et al 2013][research_vidya_vivekananad_2013]\] \[[Bohlouri et al 2014][research_bohlouri_kosari_2014]\] \[[Chandiramani et al 2014][research_chandiramani_bhandari_2014]\] \[[Havelund, Klaus and Joshi, Rajeev 2014][research_havelundklaus_joshirajeev_2014]\] \[[Kargin 2014][research_kargin_2014]\] \[[Manusubramanian et al 2014][research_manusubramanian_sumitra_2014]\] \[[Parkes et al 2014][research_parkes_mcclements_2014]\] \[[Savitha et al 2014][research_savitha_ravindra_2014]\] \[[Simms, William Herbert, III et al 2014][research_simmswilliamherbertiii_varnavaskosta_2014]\] \[[Sims, William Herbert, III and Varnavas, Kosta A. 2014][research_simswilliamherbertiii_varnavaskostaa_2014]\] \[[Varnavas, Kosta A. and Sims, William Herbert, III 2014][research_varnavaskostaa_simswilliamherbertiii_2014]\] \[[Brosnan, Ian G. et al 2015][research_brosnaniang_mcgarrylouisep_2015]\] \[[Herbert, Phillip W., Sr. et al 2015][research_herbertphillipwsr_elliotalexc_2015]\] \[[Jackson, Markus Deon 2015][research_jacksonmarkusdeon_2015]\] \[[Lee and Pomerantz 2015][research_lee_pomerantz_2015]\] \[[Morgan 2015][research_morgan_2015]\] \[[Mudford et al 2015][research_mudford_obyrne_2015]\] \[[Nishanth. N. R et al 2015][research_nishanthnr_rekhaks_2015]\] \[[Pace et al 2015][research_pace_eastburg_2015]\] \[[Parkes et al 2015][research_parkes_mcclements_2015]\] \[[Pomerantz, Marc et al 2015][research_pomerantzmarc_nguyenviet_2015]\] \[[Scheidt, Douglas et al 2015][research_scheidtdouglas_aulterick_2015]\] \[[Starkey 2015][research_starkey_2015]\] \[[Vijayan and Suresh Babu 2015][research_vijayan_sureshbabu_2015]\] \[[Biswas et al 2016][research_biswas_khorasgani_2016]\] \[[Blanco et al 2016][research_blanco_rahimov_2016]\] \[[DeForrest, Lloyd et al 2016][research_deforrestlloyd_saadatfarzad_2016]\] \[[Evans and Chattlain 2016][research_evans_chattlain_2016]\] \[[Evans et al 2016][research_evans_martinez_2016]\] \[[Evans et al 2016][research_evans_martinez_2016_b]\] \[[Maharaja, Rishabh 2016][research_maharajarishabh_2016]\] \[[Singh, Garima et al 2016][research_singhgarima_lozijulien_2016]\] \[[Tieshan et al 2016][research_tieshan_daquan_2016]\] \[[Bin et al 2017][research_bin_hua_2017]\] \[[Du et al 2017][research_du_wang_2017]\] \[[Evans et al 2017][research_evans_martinez_2017]\] \[[Hang, Richard 2017][research_hangrichard_2017]\] \[[Herbert, Phillip W., Sr. et al 2017][research_herbertphillipwsr_elliottalexc_2017]\] \[[Jones, Ron et al 2017][research_jonesron_smithdan_2017]\] \[[Levenets et al 2017][research_levenets_bogachev_2017]\] \[[Pires, Craig and Knudson, Matthew D. 2017][research_pirescraig_knudsonmatthewd_2017]\] \[[Ren et al 2017][research_ren_he_2017]\] \[[Shan et al 2017][research_shan_ren_2017]\] \[[Shaolin 2017][research_shaolin_2017]\] \[[Tkachenko et al 2017][research_tkachenko_salmin_2017]\] \[[Vasudevan et al 2017][research_vasudevan_das_2017]\] \[[Waldersen, Matt and Schnarr, Otto, III 2017][research_waldersenmatt_schnarrottoiii_2017]\] \[[Weber, Romann et al 2017][research_weberromann_yueyisong_2017]\] \[[Chang, Chen J. et al 2018][research_changchenj_liaghatijramirl_2018]\] \[[Elshafey 2018][research_elshafey_2018]\] \[[Evans and Donati 2018][research_evans_donati_2018]\] \[[Farnham 2018][research_farnham_2018]\] \[[Fuertes et al 2018][research_fuertes_pilastre_2018]\] \[[Konkin et al 2018][research_konkin_kolesenkov_2018]\] \[[Levenets 2018][research_levenets_2018]\] \[[Negron-Martinez, Antonio Jose and Thomas, Taylor Walter 2018][research_negronmartinezantoniojose_thomastaylorwalter_2018]\] \[[Saglam and Yilmaz 2018][research_saglam_yilmaz_2018]\] \[[Shi et al 2018][research_shi_shen_2018]\] \[[Zhe et al 2018][research_zhe_meizhen_2018]\] \[[Doudkin et al 2019][research_doudkin_marushko_2019]\] \[[Hamkins, Jon and Vilnrotter, Victor 2019][research_hamkinsjon_vilnrottervictor_2019]\] \[[Li et al 2019][research_li_zhang_2019]\] \[[Luo et al 2019][research_luo_tan_2019]\] \[[Pandey and Arora 2019][research_pandey_arora_2019]\] \[[Sakagami et al 2019][research_sakagami_takeishi_2019]\] \[[Thomas, Taylor Walter 2019][research_thomastaylorwalter_2019]\] \[[Volkov et al 2019][research_volkov_kolokutin_2019]\] \[[Beegum et al 2020][research_beegum_chacko_2020]\] \[[Biswas et al 2020][research_biswas_khorasgani_2020]\] \[[Flávio 2020][research_flavio_2020]\] \[[Johan Klun et al 2020][research_johanklun_brucelipe_2020]\] \[[Li et al 2020][research_li_yang_2020]\] \[[Naik et al 2020][research_naik_holmgren_2020]\] \[[Pan et al 2020][research_pan_guo_2020]\] \[[Review for "Inferring individual 2020][research_review_for_2020]\] \[[Rojdev, Kristina et al 2020][research_rojdevkristina_hagenjeff_2020]\] \[[S. et al 2020][research_s_chauhan_2020]\] \[[Skobtsov and Novoselova 2020][research_skobtsov_novoselova_2020]\] \[[Song et al 2020][research_song_yu_2020]\] \[[Tabakov and Zinina 2020][research_tabakov_zinina_2020]\] \[[Tabakov et al 2020][research_tabakov_zinina_2020_b]\] \[[Tamami 2020][research_tamami_2020]\] \[[Bennett et al 2021][research_bennett_schaub_2021]\] \[[Fenglei 2021][research_fenglei_2021]\] \[[Grigoryev and Burlutskiy 2021][research_grigoryev_burlutskiy_2021]\] \[[Ramalingam et al 2021][research_ramalingam_thanuja_2021]\] \[[Sazonov 2021][research_sazonov_2021]\] \[[Wang et al 2021][research_wang_wu_2021]\] \[[Wenzel, Sean et al 2021][research_wenzelsean_huangcalvin_2021]\] \[[Yang 2021][research_yang_2021]\] \[[Yang et al 2021][research_yang_ma_2021]\] \[[Yu et al 2021][research_yu_song_2021]\] \[[Zdravković et al 2021][research_zdravkovic_ilic_2021]\] \[[Anjana et al 2022][research_anjana_renjith_2022]\] \[[He et al 2022][research_he_shi_2022]\] \[[Kegenbekov and Saparova 2022][research_kegenbekov_saparova_2022]\] \[[Kothapalli 2022][research_kothapalli_2022]\] \[[Li et al 2022][research_li_chen_2022]\] \[[Nebiolo and Castro-Santos 2022][research_nebiolo_castrosantos_2022]\] \[[Othman et al 2022][research_othman_kashevnik_2022]\] \[[Othman et al 2022][research_othman_kashevnik_2022_b]\] \[[Salgovic et al 2022][research_salgovic_galinski_2022]\] \[[Schmidhuber and Lopez-Delgado 2022][research_schmidhuber_lopezdelgado_2022]\] \[[Song et al 2022][research_song_yu_2022]\] \[[Yan et al 2022][research_yan_wei_2022]\] \[[Zhang et al 2022][research_zhang_xu_2022]\] \[[Bao et al 2023][research_bao_dong_2023]\] \[[Huang 2023][research_huang_2023]\] \[[Instrumentation for Telemetry, Testing 2023][research_instrumentation_for_2023]\] \[[Intelligence and Neuroscience 2023][research_intelligenceandneuroscience_2023]\] \[[Ivanova and Khoroshilov 2023][research_ivanova_khoroshilov_2023]\] \[[Jiang et al 2023][research_jiang_jiang_2023]\] \[[Miniature Onboard Data Acquisition 2023][research_miniature_onboard_2023]\] \[[Ren et al 2023][research_ren_yang_2023]\] \[[Yesmagambetov et al 2023][research_yesmagambetov_mussabekov_2023]\] \[[Zhu et al 2023][research_zhu_yan_2023]\] \[[Cervantes et al 2024][research_cervantes_moore_2024]\] \[[Cianci et al 2024][research_cianci_corallo_2024]\] \[[Lakey and Schlippe 2024][research_lakey_schlippe_2024]\] \[[Liu et al 2024][research_liu_lu_2024]\] \[[Luan et al 2024][research_luan_xue_2024]\] \[[Mo et al 2024][research_mo_wang_2024]\] \[[Shaw et al 2024][research_shaw_thakur_2024]\] \[[Skobtsov 2024][research_skobtsov_2024]\] \[[Tian et al 2024][research_tian_wang_2024]\] \[[Yu et al 2024][research_yu_yu_2024]\] \[[Aji et al 2025][research_aji_agusdian_2025]\] \[[Akl and Elattar 2025][research_akl_elattar_2025]\] \[[Chen et al 2025][research_chen_wang_2025]\] \[[Chua et al 2025][research_chua_kumar_2025]\] \[[Debnath and Naresh Reddy 2025][research_debnath_nareshreddy_2025]\] \[[Fejjari et al 2025][research_fejjari_delavault_2025]\] \[[Goetze et al 2025][research_goetze_schlippe_2025]\] \[[Gouri et al 2025][research_gouri_krishnama_2025]\] \[[K A et al 2025][research_ka_parikh_2025]\] \[[Laporte et al 2025][research_laporte_perlin_2025]\] \[[Mokhtar et al 2025][research_mokhtar_ibrahim_2025]\] \[[Ruixue and Zexu 2025][research_ruixue_zexu_2025]\] \[[S et al 2025][research_s_s_2025]\] \[[Sequence Mining of Spacecraft 2025][research_sequence_mining_of_2025]\] \[[Yang et al 2025][research_yang_peng_2025]\] \[[Agarwal 2026][research_agarwal_2026]\] \[[Anima D Sabale and Erika E Gallegos 2026][research_animadsabale_erikaegallegos_2026]\] \[[Anima Sabale and Erika E Gallegos 2026][research_animasabale_erikaegallegos_2026]\] \[[Barros et al 2026][research_barros_correia_2026]\] \[[Bolhov and Klyatchenko 2026][research_bolhov_klyatchenko_2026]\] \[[Dai et al 2026][research_dai_xiao_2026]\] \[[Güler 2026][research_guler_2026]\] \[[Hong et al 2026][research_hong_wang_2026]\] \[[Issitt et al 2026][research_issitt_mahendrakar_2026]\] \[[Kochetova and Levenets 2026][research_kochetova_levenets_2026]\] \[[Mahmood et al 2026][research_mahmood_zulfiqar_2026]\] \[[Rusconi et al 2026][research_rusconi_borelli_2026]\] \[[Sachikonye 2026][research_sachikonye_2026]\] \[[Zhang et al 2026][research_zhang_pan_2026]\] \[[Boldissar and Alfredson][research_boldissar_alfredson]\] \[[Brian Saulman and Robert Wagner][research_briansaulman_robertwagner]\] \[[Elaine Yi Jia Zheng et al][research_elaineyijiazheng_danielcellucci]\] \[[Epperly and Walls][research_epperly_walls]\] \[[File S1 2016 The][research_file_s1]\] \[[File S2 2018 The][research_file_s2]\] \[[File S4 2017 The][research_file_s4]\] \[[Hammond][research_hammond]\] \[[Jeff Hagen et al][research_jeffhagen_michaelburlone]\] \[[Kristina Rojdev et al][research_kristinarojdev_antonywilliams]\] \[[Kristina Rojdev et al][research_kristinarojdev_jennydevolites]\] \[[Maluf et al][research_maluf_hsu]\] \[[Optimizing the Performance of][research_optimizing_the]\] \[[Portell i de Mora][research_portellidemora]\] \[[Space data and information][research_space_data]\] \[[Space data and information][research_space_data_b]\] \[[Space data and information][research_space_data_c]\] \[[Space data and information][research_space_data_d]\] \[[Space data and information][research_space_data_e]\] \[[Space engineering. Space data][research_space_engineering]\] \[[Space engineering. Space data][research_space_engineering_b]\] \[[Space systems. Launch-vehicle-to-spacecraft flight][research_space_systems_b]\] \[[Spencer][research_spencer]\] \[[Staudinger et al][research_staudinger_hershey]\] \[[Tom Young][research_tomyoung]\] \[[Yairi et al][research_yairi_nakatsugaawa]\]

### What a finite number of sensors on a circle can see

**143 records.** \[[Lobdell 1968][research_lobdell_1968]\] \[[Morse 1968][research_morse_1968]\] \[[Lobdell 1969][research_lobdell_1969]\] \[[Yellott 1982][research_yellott_1982]\] \[[Salikuddin, M. 1983][research_salikuddinm_1983]\] \[[Liu, G. 1985][research_liug_1985]\] \[[Udwadia, F. E. and Garba, J. 1985][research_udwadiafe_garbaj_1985]\] \[[Brooks, T. F. et al 1987][research_brookstf_marcolinima_1987]\] \[[Ligrani, P. M. et al 1989][research_ligranipm_baunlr_1989]\] \[[Bergmann, Martin et al 1990][research_bergmannmartin_longmanrichardw_1990]\] \[[Lim, Tae W. 1991][research_limtaew_1991]\] \[[Manalo, Natividad D. and Smith, G. L. 1991][research_manalonatividadd_smithgl_1991]\] \[[Raman, Ganesh et al 1991][research_ramanganesh_riceedwardj_1991]\] \[[Thomson et al 1991][research_thomson_ebbeson_1991]\] \[[Bogart and Yang 1992][research_bogart_yang_1992]\] \[[Lim, Tae W. 1992][research_limtaew_1992]\] \[[Ehrlichmann et al 1993][research_ehrlichmann_habich_1993]\] \[[Glassburn, Robin S. and Smith, Suzanne Weaver 1994][research_glassburnrobins_smithsuzanneweaver_1994]\] \[[Lester, Daniel 1994][research_lesterdaniel_1994]\] \[[Tsai 1995][research_tsai_1995]\] \[[Levitan and Buchsbaum 1996][research_levitan_buchsbaum_1996]\] \[[Citriniti and Citriniti 1997][research_citriniti_citriniti_1997]\] \[[Kinzie and McLaughlin 1997][research_kinzie_mclaughlin_1997]\] \[[Abhayapala et al 1999][research_abhayapala_kennedy_1999]\] \[[Newman 2000][research_newman_2000]\] \[[Rappin and De Bazelaire 2000][research_rappin_debazelaire_2000]\] \[[Williams, Glenn L. 2000][research_williamsglennl_2000]\] \[[Al-Masoud and Singh 2001][research_almasoud_singh_2001]\] \[[Kim et al 2001][research_kim_yoo_2001]\] \[[Al-Shehabi and Newman 2002][research_alshehabi_newman_2002]\] \[[Jiao et al 2002][research_jiao_leger_2002]\] \[[Li et al 2002][research_li_schemel_2002]\] \[[Larsen, M. F. 2003][research_larsenmf_2003]\] \[[Meo and Zumpano 2004][research_meo_zumpano_2004]\] \[[Liu et al 2005][research_liu_maurer_2005]\] \[[Meo and Zumpano 2005][research_meo_zumpano_2005]\] \[[Mooney, James T. and Stahl, H. Phil 2005][research_mooneyjamest_stahlhphil_2005]\] \[[Mooney, James T. and Stahl, H. Philip 2005][research_mooneyjamest_stahlhphilip_2005]\] \[[Mach, D. M. and Koshak, W. J. 2006][research_machdm_koshakwj_2006]\] \[[Wei Jiang et al 2006][research_weijiang_yixinyang_2006]\] \[[Mach, D. M. and Koshak, W. J. 2007][research_machdm_koshakwj_2007]\] \[[Rafaely et al 2007][research_rafaely_weiss_2007]\] \[[Liu et al 2008][research_liu_gao_2008]\] \[[Meyer and Elko 2008][research_meyer_elko_2008]\] \[[Reibman and Suthaharan 2008][research_reibman_suthaharan_2008]\] \[[Akhtar et al 2009][research_akhtar_borggaard_2009]\] \[[Paturzo et al 2009][research_paturzo_ferraro_2009]\] \[[Wiegmann et al 2009][research_wiegmann_schulz_2009]\] \[[Gaitonde and Samimy 2010][research_gaitonde_samimy_2010]\] \[[Chang 2011][research_chang_2011]\] \[[Even and Hagita 2011][research_even_hagita_2011]\] \[[Ma Xiaoli et al 2011][research_maxiaoli_wanglibin_2011]\] \[[Chik and Cheng 2012][research_chik_cheng_2012]\] \[[Eckart, M. E. et al 2012][research_eckartme_adamsjs_2012]\] \[[Kirsch and Schuhmann 2012][research_kirsch_schuhmann_2012]\] \[[Litvin et al 2012][research_litvin_dudley_2012]\] \[[Faranosov et al 2013][research_faranosov_karabasov_2013]\] \[[Khatun et al 2013][research_khatun_laitinen_2013]\] \[[Kijima et al 2013][research_kijima_mitsukura_2013]\] \[[Vergallo et al 2013][research_vergallo_layekuakille_2013]\] \[[Wu 2013][research_wu_2013]\] \[[Alon and Rafaely 2014][research_alon_rafaely_2014]\] \[[Castro-Triguero et al 2014][research_castrotriguero_saavedraflores_2014]\] \[[Chao-Shan et al 2014][research_chaoshan_hua_2014]\] \[[Sekikawa and Hamada 2014][research_sekikawa_hamada_2014]\] \[[Ye and Law 2014][research_ye_law_2014]\] \[[Ishida et al 2015][research_ishida_sekikawa_2015]\] \[[Laera 2015][research_laera_2015]\] \[[Sekikawa and Hamada 2015][research_sekikawa_hamada_2015]\] \[[Ali et al 2016][research_ali_pandey_2016]\] \[[Behn et al 2016][research_behn_kisler_2016]\] \[[Xu and Zhao 2016][research_xu_zhao_2016]\] \[[Mainini 2017][research_mainini_2017]\] \[[Normal Mode Decomposition Based 2017][research_normal_mode_decomposition_2017]\] \[[Sijtsma and Brouwer 2017][research_sijtsma_brouwer_2017]\] \[[Zhao et al 2017][research_zhao_wu_2017]\] \[[Bodrucki et al 2018][research_bodrucki_broilo_2018]\] \[[He et al 2018][research_he_xu_2018]\] \[[Rajasegar et al 2018][research_rajasegar_choi_2018]\] \[[Sijtsma and Brouwer 2018][research_sijtsma_brouwer_2018]\] \[[Viúdez 2018][research_viudez_2018]\] \[[Brown et al 2019][research_brown_sethu_2019]\] \[[Deng et al 2019][research_deng_wang_2019]\] \[[Shima Azimi et al 2019][research_shimaazimi_alirezabdariane_2019]\] \[[Suroso et al 2019][research_suroso_gautam_2019]\] \[[Wang et al 2019][research_wang_wang_2019]\] \[[Xu et al 2019][research_xu_zhou_2019]\] \[[Yang et al 2019][research_yang_zheng_2019]\] \[[Haldorsen 2020][research_haldorsen_2020]\] \[[Li and Yang 2020][research_li_yang_2020_b]\] \[[Lin et al 2020][research_lin_wu_2020]\] \[[Chai et al 2021][research_chai_yang_2021]\] \[[Fan 2021][research_fan_2021]\] \[[Luo and Kareem 2021][research_luo_kareem_2021]\] \[[Gonzales et al 2022][research_gonzales_sakaue_2022]\] \[[Gonzales et al 2022][research_gonzales_sakaue_2022_b]\] \[[Li et al 2022][research_li_an_2022]\] \[[Ohmichi et al 2022][research_ohmichi_sugioka_2022]\] \[[Wu et al 2022][research_wu_yu_2022]\] \[[Wu et al 2022][research_wu_yu_2022_b]\] \[[Zhao 2022][research_zhao_2022]\] \[[A hydro-acoustic mode decomposition 2023][research_a_hydro_acoustic_2023]\] \[[Chanteur 2023][research_chanteur_2023]\] \[[Herrera 2023][research_herrera_2023]\] \[[Juhlin and Jakobsson 2023][research_juhlin_jakobsson_2023]\] \[[Mudge 2023][research_mudge_2023]\] \[[Sha et al 2023][research_sha_wang_2023]\] \[[Zhong et al 2023][research_zhong_jiang_2023]\] \[[Berthomieu et al 2024][research_berthomieu_salmon_2024]\] \[[Cao et al 2024][research_cao_zhang_2024]\] \[[Nicoletti et al 2024][research_nicoletti_quarchioni_2024]\] \[[Snaiki and Mirfakhar 2024][research_snaiki_mirfakhar_2024]\] \[[Zhang et al 2024][research_zhang_zhang_2024]\] \[[Al Maraashli et al 2025][research_almaraashli_youseffi_2025]\] \[[Behn and Tapken 2025][research_behn_tapken_2025]\] \[[Bejani et al 2025][research_bejani_mauri_2025]\] \[[Fu et al 2025][research_fu_lam_2025]\] \[[Goto et al 2025][research_goto_tsujimura_2025]\] \[[Guzik et al 2025][research_guzik_cengarle_2025]\] \[[Mudge 2025][research_mudge_2025]\] \[[Sun et al 2025][research_sun_mahmoodian_2025]\] \[[Vincent et al 2025][research_vincent_pereira_2025]\] \[[Chen et al 2026][research_chen_du_2026]\] \[[Chen et al 2026][research_chen_yuan_2026]\] \[[Lian et al 2026][research_lian_wang_2026]\] \[[Lian et al 2026][research_lian_liangji_2026]\] \[[Monnoyer et al 2026][research_monnoyer_louveaux_2026]\] \[[Monnoyer et al 2026][research_monnoyer_louveaux_2026_b]\] \[[Moussa and Guedria 2026][research_moussa_guedria_2026]\] \[[Nikiforov et al 2026][research_nikiforov_tsymbalov_2026]\] \[[Shen et al 2026][research_shen_sun_2026]\] \[[Wang et al 2026][research_wang_pei_2026]\] \[[Yang et al 2026][research_yang_wang_2026]\] \[[Barani][research_barani]\] \[[Daly][research_daly]\] \[[DeFord et al][research_deford_craig]\] \[[Jie Li et al][research_jieli_nettiehroozeboom]\] \[[Jie Li et al][research_jieli_nettiehroozeboom_b]\] \[[Jie Li et al][research_jieli_elaralash]\] \[[Mohammad Barani et al][research_mohammadbarani_weichaotu]\] \[[Movva][research_movva]\] \[[Ryan Connelly et al][research_ryanconnelly_thomassteva]\] \[[Sawada et al][research_sawada_araki]\]

### Error budgets, and the discipline of propagating them

**210 records.** \[[Abdelwahab, Mahmood et al 1987][research_abdelwahabmahmood_biesiadnythomasj_1987]\] \[[Davidian, Kenneth J. 1987][research_davidiankennethj_1987]\] \[[Ferguson, C. R. et al 1987][research_fergusoncr_treedr_1987]\] \[[Kenneth J. Davidian et al 1987][research_kennethjdavidian_ronaldhdieck_1987]\] \[[Arueti 1988][research_arueti_1988]\] \[[Rusek 1989][research_rusek_1989]\] \[[Gowing 1990][research_gowing_1990]\] \[[Batill, Stephen M. 1994][research_batillstephenm_1994]\] \[[Whitmore, Stephen A. and Moes, Timothy R. 1994][research_whitmorestephena_moestimothyr_1994]\] \[[Blumenthal, Philip Z. 1995][research_blumenthalphilipz_1995]\] \[[Naughton, Jonathan W. et al 1996][research_naughtonjonathanw_brownjamesl_1996]\] \[[Rossi 1996][research_rossi_1996]\] \[[Cohn 1997][research_cohn_1997]\] \[[Sims, Joseph D. and Coleman, Hugh W. 1998][research_simsjosephd_colemanhughw_1998]\] \[[Tripp, John S. and Tcheng, Ping 1999][research_trippjohns_tchengping_1999_b]\] \[[Betta et al 2000][research_betta_liguori_2000]\] \[[Chunovkina 2000][research_chunovkina_2000]\] \[[Krystek 2000][research_krystek_2000]\] \[[Meyn 2000][research_meyn_2000]\] \[[Tarapčík et al 2001][research_tarapcik_labuda_2001]\] \[[Measurement Uncertainty 2002][research_measurement_uncertainty_2002]\] \[[Chin, T. M. et al 2003][research_chintm_grossrs_2003]\] \[[Cox et al 2003][research_cox_harris_2003]\] \[[Ellison and Williams 2003][research_ellison_williams_2003]\] \[[Gertsbakh 2003][research_gertsbakh_2003]\] \[[Selvan 2003][research_selvan_2003]\] \[[Amer, Tahani et al 2004][research_amertahani_trippjohn_2004]\] \[[D'Antona 2004][research_dantona_2004]\] \[[Driscoll, E. A. and Landrum, D. B. 2004][research_driscollea_landrumdb_2004]\] \[[Lineberry et al 2004][research_lineberry_coleman_2004]\] \[[Denguir-Rekik et al 2005][research_denguirrekik_mauris_2005]\] \[[Hall 2005][research_hall_2005]\] \[[Locke, Justin M. and Landrum, D. Brian 2005][research_lockejustinm_landrumdbrian_2005]\] \[[Peretto et al 2005][research_peretto_sasdelli_2005]\] \[[Case studies in measurement 2006][research_case_studies_2006]\] \[[Hinrichs 2006][research_hinrichs_2006]\] \[[Uncertainty Propagation for Systems 2006][research_uncertainty_propagation_2006]\] \[[Bich et al 2007][research_bich_dagostino_2007]\] \[[Cristaldi et al 2007][research_cristaldi_faifer_2007]\] \[[Mana and Pennecchi 2007][research_mana_pennecchi_2007]\] \[[Mencattini et al 2007][research_mencattini_salmeri_2007]\] \[[Roberts et al 2007][research_roberts_stevens_2007]\] \[[White and Saunders 2007][research_white_saunders_2007]\] \[[Golubev 2008][research_golubev_2008]\] \[[Hemsch, Michael J. et al 2008][research_hemschmichaelj_hankejeremyl_2008]\] \[[Meija and Mester 2008][research_meija_mester_2008]\] \[[Mekid and Vaja 2008][research_mekid_vaja_2008]\] \[[Ponci and Johnson 2008][research_ponci_johnson_2008]\] \[[Torres et al 2008][research_torres_olea_2008]\] \[[Uncertainty Propagation Methods 2008][research_uncertainty_propagation_2008]\] \[[Hale and Wang 2009][research_hale_wang_2009]\] \[[Mari 2009][research_mari_2009]\] \[[Mencattini et al 2009][research_mencattini_rabottino_2009]\] \[[Murray-Krezan 2009][research_murraykrezan_2009]\] \[[Stenarson and Yhland 2009][research_stenarson_yhland_2009]\] \[[Di Leo et al 2010][research_dileo_liguori_2010]\] \[[Mellodge and Kachroo 2010][research_mellodge_kachroo_2010]\] \[[Okuyama 2010][research_okuyama_2010]\] \[[Chiang, Vincent et al 2011][research_chiangvincent_sunjunqiang_2011]\] \[[Dietrich and Schulze 2011][research_dietrich_schulze_2011]\] \[[Dietrich and Schulze 2011][research_dietrich_schulze_2011_b]\] \[[Gupta 2011][research_gupta_2011]\] \[[Hanke, Jeremy L. 2011][research_hankejeremyl_2011]\] \[[Hessling 2011][research_hessling_2011]\] \[[Konda et al 2011][research_konda_singla_2011]\] \[[Wang and Wang 2011][research_wang_wang_2011]\] \[[Xiong, Xiaoxiong et al 2011][research_xiongxiaoxiong_sunjunqiang_2011]\] \[[Molleda et al 2012][research_molleda_usamentiaga_2012]\] \[[Taylor 2012][research_taylor_2012]\] \[[Taylor 2012][research_taylor_2012_b]\] \[[Chapter 9 Uncertainty Propagation 2013][research_chapter_9_2013]\] \[[Mai et al 2013][research_mai_vogt_2013]\] \[[Taylor 2013][research_taylor_2013]\] \[[Zappa et al 2013][research_zappa_malavasi_2013]\] \[[Azpurua et al 2014][research_azpurua_paez_2014]\] \[[Mackey, Jon et al 2014][research_mackeyjon_sehirlioglualp_2014]\] \[[Mackey, Jon et al 2014][research_mackeyjon_sehirlioglualp_2014_b]\] \[[Methods of uncertainty propagation 2014][research_methods_of_2014]\] \[[Operative procedures for the 2014][research_operative_procedures_2014]\] \[[Ratcliffe and Ratcliffe 2014][research_ratcliffe_ratcliffe_2014]\] \[[Ratcliffe and Ratcliffe 2014][research_ratcliffe_ratcliffe_2014_b]\] \[[Turpie, Kevin R. et al 2014][research_turpiekevinr_epleerobertejr_2014]\] \[[Brochot 2015][research_brochot_2015]\] \[[Ferrero et al 2015][research_ferrero_prioli_2015]\] \[[Liu, X. 2015][research_liux_2015]\] \[[Propagation of measurement uncertainty 2015][research_propagation_of_2015]\] \[[Sargsyan 2015][research_sargsyan_2015]\] \[[Stephens, Julia et al 2015][research_stephensjulia_hubbarderin_2015]\] \[[Zhu et al 2015][research_zhu_tian_2015]\] \[[Aronstein, David L. and Smith, J. Scott 2016][research_aronsteindavidl_smithjscott_2016]\] \[[Blalock and Fordham 2016][research_blalock_fordham_2016]\] \[[Davison, Craig R. et al 2016][research_davisoncraigr_strappjwalter_2016]\] \[[Fotowicz 2016][research_fotowicz_2016]\] \[[Haas, Evan and DeLuccia, Frank 2016][research_haasevan_delucciafrank_2016]\] \[[Idźkowski et al 2016][research_idzkowski_walendziuk_2016]\] \[[Mohammadikaji et al 2016][research_mohammadikaji_bergmann_2016]\] \[[Morris and Crowley 2016][research_morris_crowley_2016]\] \[[Qin et al 2016][research_qin_zhang_2016]\] \[[Sciacchitano and Wieneke 2016][research_sciacchitano_wieneke_2016]\] \[[Stephens, Julia E. et al 2016][research_stephensjuliae_hubbarderinp_2016]\] \[[Stephens, Julia et al 2016][research_stephensjulia_hubbarderin_2016]\] \[[Tutmez 2016][research_tutmez_2016]\] \[[Uncertainty Estimation, Propagation, and 2016][research_uncertainty_estimation_2016]\] \[[Zhou et al 2016][research_zhou_zhangduizhong_2016]\] \[[Chiang, Kwofu V. et al 2017][research_chiangkwofuv_mcintirejeff_2017]\] \[[Determining Measurement Uncertainty Example 2017][research_determining_measurement_2017]\] \[[Eguia et al 2017][research_eguia_lamikiz_2017]\] \[[Heidenreich et al 2017][research_heidenreich_gross_2017]\] \[[Krejci et al 2017][research_krejci_petri_2017]\] \[[Measurement Uncertainty 2017][research_measurement_uncertainty_2017]\] \[[Nikbay, Melike and Heeg, Jennifer 2017][research_nikbaymelike_heegjennifer_2017]\] \[[None 2017][research_none_2017]\] \[[Chalyy 2018][research_chalyy_2018]\] \[[Cristaldi et al 2018][research_cristaldi_ferrero_2018]\] \[[Dalle, Derek J. et al 2018][research_dallederekj_rogersstuarte_2018]\] \[[David M Driver et al 2018][research_davidmdriver_danielphilippidis_2018]\] \[[Gorbunov and Kirchengast 2018][research_gorbunov_kirchengast_2018]\] \[[Schalken and Chantler 2018][research_schalken_chantler_2018]\] \[[Silva et al 2018][research_silva_amado_2018]\] \[[Xiong, Xiaoxiong et al 2018][research_xiongxiaoxiong_angalamit_2018]\] \[[Elizabeth et al 2019][research_elizabeth_kumar_2019]\] \[[Hubbard, Erin P. 2019][research_hubbarderinp_2019]\] \[[Kajita 2019][research_kajita_2019]\] \[[Matsukawa et al 2019][research_matsukawa_watanabe_2019]\] \[[Tolić et al 2019][research_tolic_primorac_2019]\] \[[Turmon, Michael and Braverman, Amy 2019][research_turmonmichael_bravermanamy_2019]\] \[[Aaron Pearlman et al 2020][research_aaronpearlman_matthewmontanaro_2020]\] \[[Campbell 2020][research_campbell_2020]\] \[[Lee and Lee 2020][research_lee_lee_2020]\] \[[Matharu and Devi 2020][research_matharu_devi_2020]\] \[[Perez et al 2020][research_perez_gietler_2020]\] \[[Shi et al 2020][research_shi_kuschmierz_2020]\] \[[Zhao et al 2020][research_zhao_li_2020]\] \[[Gu et al 2021][research_gu_cho_2021]\] \[[Nate Kelsey 2021][research_natekelsey_2021]\] \[[Sakai et al 2021][research_sakai_yoshii_2021]\] \[[Sarkar 2021][research_sarkar_2021]\] \[[Dexter Johnson et al 2022][research_dexterjohnson_joelwsills_2022]\] \[[Doyoro et al 2022][research_doyoro_chang_2022]\] \[[Du et al 2022][research_du_meng_2022]\] \[[Kanso et al 2022][research_kanso_jha_2022]\] \[[Zhang et al 2022][research_zhang_liu_2022]\] \[[Cavalieri et al 2023][research_cavalieri_liberatori_2023]\] \[[David J. Friedlander et al 2023][research_davidjfriedlander_michaeldbozeman_2023]\] \[[Demerdziev and Cundeva-Blajer 2023][research_demerdziev_cundevablajer_2023]\] \[[Demerdziev and Dimchev 2023][research_demerdziev_dimchev_2023]\] \[[Guidelines on measurement uncertainty 2023][research_guidelines_on_2023]\] \[[Mandal and Mukhopadhyay 2023][research_mandal_mukhopadhyay_2023]\] \[[Ooi et al 2023][research_ooi_rajan_2023]\] \[[Pamela Poljak 2023][research_pamelapoljak_2023]\] \[[Rizza et al 2023][research_rizza_machado_2023]\] \[[Ezebili and Schreve 2024][research_ezebili_schreve_2024]\] \[[Fossum et al 2024][research_fossum_bhowmik_2024]\] \[[Huang et al 2024][research_huang_xie_2024]\] \[[Lagouanelle and Gall 2024][research_lagouanelle_gall_2024]\] \[[Measurement Uncertainty 2024][research_measurement_uncertainty_2024_b]\] \[[Measurement uncertainty concepts 2024][research_measurement_uncertainty_2024]\] \[[Ou et al 2024][research_ou_xiao_2024]\] \[[Rishi 2024][research_rishi_2024]\] \[[Skinner et al 2024][research_skinner_gruber_2024]\] \[[Thompson 2024][research_thompson_2024]\] \[[Zakharov et al 2024][research_zakharov_botsiura_2024]\] \[[Zhipeng Wang et al 2024][research_zhipengwang_juliabarsi_2024]\] \[[Carratù et al 2025][research_carratu_gallo_2025]\] \[[Dirix and Enayati 2025][research_dirix_enayati_2025]\] \[[Ferrero 2025][research_ferrero_2025]\] \[[Francisco Pena and Erick Rossi De La Fuente 2025][research_franciscopena_erickrossidelafuente_2025]\] \[[Gorla et al 2025][research_gorla_brewer_2025]\] \[[Joachim Balis et al 2025][research_joachimbalis_hervelamy_2025]\] \[[Ludwig et al 2025][research_ludwig_gruber_2025]\] \[[Manop et al 2025][research_manop_tanghengjareon_2025]\] \[[McDowell et al 2025][research_mcdowell_raghu_2025]\] \[[Witkovský 2025][research_witkovsky_2025]\] \[[Zangl and Pérez 2025][research_zangl_perez_2025]\] \[[Zhou et al 2025][research_zhou_wang_2025]\] \[[Agourakis and Agourakis 2026][research_agourakis_agourakis_2026]\] \[[Andrieu 2026][research_andrieu_2026]\] \[[Appendix H Alternate Measurement 2026][research_appendix_h_2026]\] \[[Appendix K Condensed Measurement 2026][research_appendix_k_2026]\] \[[Arronde Pérez and Zangl 2026][research_arrondeperez_zangl_2026]\] \[[Cabrera et al 2026][research_cabrera_zouhri_2026]\] \[[Ekici and Savun 2026][research_ekici_savun_2026]\] \[[Fundamentals of Measurement Uncertainty 2026][research_fundamentals_of_2026]\] \[[Gozuoglu and Gerçekcioğlu 2026][research_gozuoglu_gercekcioglu_2026]\] \[[Li et al 2026][research_li_ren_2026]\] \[[Nasution et al 2026][research_nasution_gianto_2026]\] \[[Otsuka 2026][research_otsuka_2026]\] \[[Otsuka 2026][research_otsuka_2026_b]\] \[[Petitjean and Musset 2026][research_petitjean_musset_2026]\] \[[The Measurement Uncertainty Model 2026][research_the_measurement_2026]\] \[[Vasilevskyi and Cullinan 2026][research_vasilevskyi_cullinan_2026]\] \[[Wang et al 2026][research_wang_dai_2026]\] \[[Bhatia][research_bhatia]\] \[[Daniel C. Kammer et al][research_danielckammer_paulblelloch]\] \[[David Friedlander et al][research_davidfriedlander_michaelbozeman]\] \[[Eleni Mowery et al][research_elenimowery_jacobstonehill]\] \[[Erin Hubbard and Frank Semmelmayer][research_erinhubbard_franksemmelmayer]\] \[[Estimation of Measurement Uncertainty][research_estimation_of]\] \[[Example Uncertainty Propagation][research_example_uncertainty]\] \[[Fuzzy Variables and Measurement][research_fuzzy_variables]\] \[[Goyal][research_goyal]\] \[[Heather P Houlden and Erin Hubbard][research_heatherphoulden_erinhubbard]\] \[[Kenneth McAfee et al][research_kennethmcafee_hannahalpert]\] \[[Mario Santos et al][research_mariosantos_serhathosder]\] \[[Measurement Uncertainty Applied to][research_measurement_uncertainty]\] \[[Measurement of neutron capture][research_measurement_of]\] \[[Moon][research_moon]\] \[[Pamela Poljak et al][research_pamelapoljak_aaronjohnson]\] \[[Quincy Mckown et al][research_quincymckown_markschoenenberger]\] \[[Vathsal][research_vathsal]\]

### Coming back, which is what the legs are for

**518 records.** \[[Barraza 1962][research_barraza_1962]\] \[[Barraza, R. M. 1962][research_barrazarm_1962]\] \[[Mcnair, L. L. 1962][research_mcnairll_1962]\] \[[Bono, P. 1963][research_bonop_1963]\] \[[Milliken 1963][research_milliken_1963]\] \[[Armstrong 1964][research_armstrong_1964]\] \[[Benson, H. E. et al 1964][research_bensonhe_mcculloughje_1964]\] \[[Eberhart 1964][research_eberhart_1964]\] \[[Flynn, R. Y. and Groves, J. R. 1964][research_flynnry_grovesjr_1964]\] \[[Suit et al 1964][research_suit_kiker_1964]\] \[[Spieth 1965][research_spieth_1965]\] \[[Vaglio-Laurin and Finke 1965][research_vagliolaurin_finke_1965]\] \[[Dunavant, J. C. et al 1966][research_dunavantjc_schersh_1966]\] \[[Knaur 1966][research_knaur_1966]\] \[[Parachute recovery system for 1966][research_parachute_recovery_1966]\] \[[Scher and Dunavant 1966][research_scher_dunavant_1966]\] \[[Hull 1967][research_hull_1967]\] \[[Karel 1967][research_karel_1967]\] \[[Knaur 1967][research_knaur_1967]\] \[[Cassanto, J. M. et al 1968][research_cassantojm_eichelda_1968]\] \[[Hinchey 1968][research_hinchey_1968]\] \[[Knaur 1968][research_knaur_1968]\] \[[Jones, R. H. 1970][research_jonesrh_1970]\] \[[Kah 1970][research_kah_1970]\] \[[Bejczy 1971][research_bejczy_1971]\] \[[Expendable Second Stage Reusable 1971][research_expendable_second_1971]\] \[[Space shuttle program. Expendable 1971][research_space_shuttle_1971]\] \[[Beck, P. E. 1972][research_beckpe_1972]\] \[[Hurley, M. J. 1972][research_hurleymj_1972]\] \[[Roth, C. E. et al 1972][research_rothce_wattsll_1972]\] \[[Beck, P. E. 1973][research_beckpe_1973]\] \[[Godfrey 1973][research_godfrey_1973]\] \[[Lacroix, W. P. 1973][research_lacroixwp_1973]\] \[[Mansfield, D. L. 1973][research_mansfielddl_1973]\] \[[Space shuttle solid rocket 1973][research_space_shuttle_1973]\] \[[Space shuttle solid rocket 1973][research_space_shuttle_1973_b]\] \[[Space shuttle solid rocket 1973][research_space_shuttle_1973_c]\] \[[Bendot, J. G. 1974][research_bendotjg_1974]\] \[[Nevins, C. D. 1975][research_nevinscd_1975]\] \[[Tharratt, C. E. 1975][research_tharrattce_1975]\] \[[Hannum et al 1976][research_hannum_kasper_1976]\] \[[Rehder, J. J. 1977][research_rehderjj_1977]\] \[[Chase 1979][research_chase_1979]\] \[[Moog et al 1979][research_moog_bacchus_1979]\] \[[Runkle, R. E. 1981][research_runklere_1981]\] \[[Macgregor, C. A. 1982][research_macgregorca_1982]\] \[[Hampson 1984][research_hampson_1984]\] \[[Tewell 1984][research_tewell_1984]\] \[[Hampson, M. E. and Barkhoudarian, S. 1985][research_hampsonme_barkhoudarians_1985]\] \[[Knacke 1985][research_knacke_1985]\] \[[Cikanek 1986][research_cikanek_1986]\] \[[Cikanek, H. A., III 1986][research_cikanekhaiii_1986]\] \[[Marsik, S. J. and Gawrylowicz, H. T. 1986][research_marsiksj_gawrylowiczht_1986]\] \[[Maram, J. and Barkhoudarian, S. 1987][research_maramj_barkhoudarians_1987]\] \[[Wyett, L. et al 1987][research_wyettl_maramj_1987]\] \[[Barkhoudarian et al 1988][research_barkhoudarian_szemenyei_1988]\] \[[Cannon et al 1988][research_cannon_norman_1988]\] \[[Merrill and Lorenzo 1988][research_merrill_lorenzo_1988]\] \[[Merrill, Walter C. and Lorenzo, Carl F. 1988][research_merrillwalterc_lorenzocarlf_1988]\] \[[Norman et al 1988][research_norman_weiss_1988]\] \[[Macbeth 1989][research_macbeth_1989]\] \[[Macconochie, Ian O. and Breiner, Charles A. 1989][research_macconochieiano_breinercharlesa_1989]\] \[[Macconochie, Ian O. et al 1989][research_macconochieiano_martinjamesa_1989]\] \[[Perry, John G. 1989][research_perryjohng_1989]\] \[[Grosdemange and Schaeffer 1990][research_grosdemange_schaeffer_1990]\] \[[Guo, T.-H. et al 1990][research_guoth_merrillw_1990]\] \[[Schindler, Carla M. and Lansaw, John 1990][research_schindlercarlam_lansawjohn_1990]\] \[[Sedillo 1990][research_sedillo_1990]\] \[[Steinmeyer et al 1990][research_steinmeyer_howard_1990]\] \[[Anex et al 1991][research_anex_russell_1991]\] \[[Just 1991][research_just_1991]\] \[[MacConochie, Ian O. and Briener, Charles A. 1991][research_macconochieiano_brienercharlesa_1991]\] \[[Musgrave 1991][research_musgrave_1991]\] \[[Nemeth, ED et al 1991][research_nemethed_andersonron_1991]\] \[[Burkardt, Leo A. 1992][research_burkardtleoa_1992]\] \[[Ezell et al 1992][research_ezell_barkhoudarian_1992]\] \[[Guo, T. H. et al 1992][research_guoth_merrillw_1992]\] \[[Musgrave, Jeffrey L. 1992][research_musgravejeffreyl_1992]\] \[[Musgrave, Jeffrey L. et al 1992][research_musgravejeffreyl_paxsondaniele_1992]\] \[[Stanley et al 1992][research_stanley_engelund_1992]\] \[[Hannigan et al 1993][research_hannigan_sved_1993]\] \[[Hardy et al 1993][research_hardy_eldrenkamp_1993]\] \[[Martin, James A. 1993][research_martinjamesa_1993]\] \[[Meiboom 1993][research_meiboom_1993]\] \[[Allen et al 1994][research_allen_sauvageau_1994]\] \[[Dumbacher and Klevatt 1994][research_dumbacher_klevatt_1994]\] \[[Litt, Jonathan S. et al 1994][research_littjonathans_musgravejeffreyl_1994]\] \[[Manski and Fina 1994][research_manski_fina_1994]\] \[[Peng et al 1994][research_peng_zhang_1994]\] \[[Surko, Pamela 1994][research_surkopamela_1994]\] \[[Astorg and Barreau, luiver, C 1995][research_astorg_barreauluiverc_1995]\] \[[Bos et al 1995][research_bos_nienkemper_1995]\] \[[Cook 1995][research_cook_1995]\] \[[Goncharov et al 1995][research_goncharov_orlov_1995]\] \[[Keith 1995][research_keith_1995]\] \[[Meiboom and Geerdes 1995][research_meiboom_geerdes_1995]\] \[[Nielsen and Stratton 1995][research_nielsen_stratton_1995]\] \[[Ray, Asok and Dai, Xiaowen 1995][research_rayasok_daixiaowen_1995]\] \[[Reusable Launch Vehicle 1995][research_reusable_launch_1995]\] \[[Rogerson 1995][research_rogerson_1995]\] \[[Rysev and Andronov 1995][research_rysev_andronov_1995]\] \[[Schorr and Speas 1995][research_schorr_speas_1995]\] \[[Vishnyak 1995][research_vishnyak_1995]\] \[[Cook 1996][research_cook_1996]\] \[[Davis 1996][research_davis_1996]\] \[[Elvin 1996][research_elvin_1996]\] \[[Fitzsimmons 1996][research_fitzsimmons_1996]\] \[[Freeman et al 1996][research_freeman_talay_1996]\] \[[Freeman, Delma C., Jr. et al 1996][research_freemandelmacjr_talaytheodorea_1996]\] \[[Froning, Jr. 1996][research_froningjr_1996]\] \[[Immich and Caporicci 1996][research_immich_caporicci_1996]\] \[[Inokuchi 1996][research_inokuchi_1996]\] \[[Komar and Christenson 1996][research_komar_christenson_1996]\] \[[MacLean and Rodriguez 1996][research_maclean_rodriguez_1996]\] \[[Peery and Parsley 1996][research_peery_parsley_1996]\] \[[Pelaccio 1996][research_pelaccio_1996]\] \[[Rogers and Dragone 1996][research_rogers_dragone_1996]\] \[[Schmidt and Mann 1996][research_schmidt_mann_1996]\] \[[Springer 1996][research_springer_1996]\] \[[Stewart, Eric et al 1996][research_stewarteric_mcconnaugheyp_1996]\] \[[Zubrin and Clapp 1996][research_zubrin_clapp_1996]\] \[[Baumgartner 1997][research_baumgartner_1997]\] \[[Blosser 1997][research_blosser_1997]\] \[[Cook et al 1997][research_cook_walters_1997]\] \[[Cordes and Hertzfeld 1997][research_cordes_hertzfeld_1997]\] \[[Ferrandon 1997][research_ferrandon_1997]\] \[[Freeman et al 1997][research_freeman_talay_1997]\] \[[Logsdon and Williamson 1997][research_logsdon_williamson_1997]\] \[[Lu 1997][research_lu_1997]\] \[[Sahu et al 1997][research_sahu_cooper_1997]\] \[[Shtessel and Krupp 1997][research_shtessel_krupp_1997]\] \[[Shtessel et al 1997][research_shtessel_tournes_1997]\] \[[Takahashi et al 1997][research_takahashi_mizobata_1997]\] \[[Tatry et al 1997][research_tatry_deneu_1997]\] \[[Andrews 1998][research_andrews_1998]\] \[[Christenson, R. L. and Komar, D. R. 1998][research_christensonrl_komardr_1998]\] \[[Ferrandon 1998][research_ferrandon_1998]\] \[[Herzog et al 1998][research_herzog_yue_1998]\] \[[Keith, E. L. and Rothschild, W. J. 1998][research_keithel_rothschildwj_1998]\] \[[Koester et al 1998][research_koester_meltzer_1998]\] \[[Konno et al 1998][research_konno_kishimoto_1998]\] \[[Lorenzo, Carl F. et al 1998][research_lorenzocarlf_holmesmichaels_1998]\] \[[McClure 1998][research_mcclure_1998]\] \[[Meyerson 1998][research_meyerson_1998]\] \[[Olds and Bellini 1998][research_olds_bellini_1998]\] \[[Ratekin, Gary 1998][research_ratekingary_1998]\] \[[Sawyer and Bush 1998][research_sawyer_bush_1998]\] \[[Stadler 1998][research_stadler_1998]\] \[[Tanck and Steadman 1998][research_tanck_steadman_1998]\] \[[Tournes and Johnson 1998][research_tournes_johnson_1998]\] \[[Tuohy 1998][research_tuohy_1998]\] \[[Wangu and Mouyos 1998][research_wangu_mouyos_1998]\] \[[Balepin, Vladimir et al 1999][research_balepinvladimir_pricejohn_1999]\] \[[Birkeland and Meuser 1999][research_birkeland_meuser_1999]\] \[[Bos and Offerman 1999][research_bos_offerman_1999]\] \[[Clayton 1999][research_clayton_1999]\] \[[Dorsey et al 1999][research_dorsey_wu_1999]\] \[[Fallon, II et al 1999][research_fallonii_taylor_1999]\] \[[Gardinier and Taylor 1999][research_gardinier_taylor_1999]\] \[[Griner, Carolyn and Lyles, Garry 1999][research_grinercarolyn_lylesgarry_1999]\] \[[Hamilton, Tom and Healy, Tom 1999][research_hamiltontom_healytom_1999]\] \[[Inatani et al 1999][research_inatani_naruo_1999]\] \[[Keith, E. L. and Rothschild, W. J. 1999][research_keithel_rothschildwj_1999]\] \[[Knapp 1999][research_knapp_1999]\] \[[Mease et al 1999][research_mease_teufel_1999]\] \[[Pamadi, Bandu N. and Brauckmann, Gregory J. 1999][research_pamadibandun_brauckmanngregoryj_1999]\] \[[Pettit et al 1999][research_pettit_barkhoudarian_1999]\] \[[Rothschild and Schuster 1999][research_rothschild_schuster_1999]\] \[[Sawyer et al 1999][research_sawyer_hodge_1999]\] \[[Shepperd and Staugler 1999][research_shepperd_staugler_1999]\] \[[Spencer 1999][research_spencer_1999]\] \[[Staniszewski 1999][research_staniszewski_1999]\] \[[Zimpfer 1999][research_zimpfer_1999]\] \[[Blades and Redgrave 2000][research_blades_redgrave_2000]\] \[[Calhoun 2000][research_calhoun_2000]\] \[[Clancy 2000][research_clancy_2000]\] \[[Dorsey et al 2000][research_dorsey_myers_2000]\] \[[Dragone 2000][research_dragone_2000]\] \[[Hertzfeld 2000][research_hertzfeld_2000]\] \[[Hueter, Uwe 2000][research_hueteruwe_2000]\] \[[Larsen 2000][research_larsen_2000]\] \[[Letchworth and Letchworth 2000][research_letchworth_letchworth_2000]\] \[[Rey 2000][research_rey_2000]\] \[[Shtessel et al 2000][research_shtessel_hall_2000]\] \[[Tetlow et al 2000][research_tetlow_schoettle_2000]\] \[[Wiesenberg 2000][research_wiesenberg_2000]\] \[[Wolf 2000][research_wolf_2000]\] \[[Balepin 2001][research_balepin_2001]\] \[[Balepin et al 2001][research_balepin_czysz_2001]\] \[[Balepin et al 2001][research_balepin_czysz_2001_b]\] \[[Clayton, J. Louie 2001][research_claytonjlouie_2001]\] \[[Corban et al 2001][research_corban_johnson_2001]\] \[[Der Kiureghian 2001][research_derkiureghian_2001]\] \[[Kostromin et al 2001][research_kostromin_sokolov_2001]\] \[[McWhorter and Ewing 2001][research_mcwhorter_ewing_2001]\] \[[Milos, Frank S. et al 2001][research_milosfranks_wattersdg_2001]\] \[[Nonaka et al 2001][research_nonaka_ogawa_2001]\] \[[Schierman et al 2001][research_schierman_ward_2001]\] \[[Schierman et al 2001][research_schierman_ward_2001_b]\] \[[Staniszewski 2001][research_staniszewski_2001]\] \[[Yamakawa et al 2001][research_yamakawa_higuchi_2001]\] \[[Ahmad, Rashid A. and Cash, Stephen F. 2002][research_ahmadrashida_cashstephenf_2002]\] \[[Dumbacher 2002][research_dumbacher_2002]\] \[[Fisher, J. E. et al 2002][research_fisherje_lawrenceda_2002]\] \[[Hagopian 2002][research_hagopian_2002]\] \[[Hodel, A. S. et al 2002][research_hodelas_callahanronnie_2002]\] \[[Kaplan 2002][research_kaplan_2002]\] \[[Ngo and Doman 2002][research_ngo_doman_2002]\] \[[Noneman 2002][research_noneman_2002]\] \[[Okayasu et al 2002][research_okayasu_ohta_2002]\] \[[Sholtis 2002][research_sholtis_2002]\] \[[Arora and Ananthasayanam 2003][research_arora_ananthasayanam_2003]\] \[[Arora et al 2003][research_arora_george_2003]\] \[[Ballard, Richard O. 2003][research_ballardrichardo_2003]\] \[[Fujimoto and Fujii 2003][research_fujimoto_fujii_2003]\] \[[Gage and Vander Kam 2003][research_gage_vanderkam_2003]\] \[[Larsen 2003][research_larsen_2003]\] \[[Marlow 2003][research_marlow_2003]\] \[[McWhorter 2003][research_mcwhorter_2003]\] \[[Miotto and LePome 2003][research_miotto_lepome_2003]\] \[[Ngo and Blake 2003][research_ngo_blake_2003]\] \[[Rooney 2003][research_rooney_2003]\] \[[Sarigul-Klijn and Sarigul-Klijn 2003][research_sarigulklijn_sarigulklijn_2003]\] \[[Urschel and Cox 2003][research_urschel_cox_2003]\] \[[Wallace et al 2003][research_wallace_olds_2003]\] \[[Brock and Franke 2004][research_brock_franke_2004]\] \[[Daniel et al 2004][research_daniel_tumino_2004]\] \[[Eklund 2004][research_eklund_2004]\] \[[Horneman and Kluever 2004][research_horneman_kluever_2004]\] \[[Jones 2004][research_jones_2004]\] \[[Ogawa et al 2004][research_ogawa_nonaka_2004]\] \[[Raj, Sai V. and Ghosn, Louis J. 2004][research_rajsaiv_ghosnlouisj_2004]\] \[[Schmitt and Burchett 2004][research_schmitt_burchett_2004]\] \[[Tripropellant Engine Technology for 2004][research_tripropellant_engine_2004]\] \[[Brinda et al 2005][research_brinda_arora_2005]\] \[[Brown and Olds 2005][research_brown_olds_2005]\] \[[Chase and McKinney 2005][research_chase_mckinney_2005]\] \[[Chiesa et al 2005][research_chiesa_grassi_2005]\] \[[Daniel and Ramusat 2005][research_daniel_ramusat_2005]\] \[[Dissel et al 2005][research_dissel_kothari_2005]\] \[[Hall and Shtessel 2005][research_hall_shtessel_2005]\] \[[Ishimoto et al 2005][research_ishimoto_fujii_2005]\] \[[Kachler and Beaurain 2005][research_kachler_beaurain_2005]\] \[[Kluever and Horneman 2005][research_kluever_horneman_2005]\] \[[Larsen 2005][research_larsen_2005]\] \[[Raj, Sai V. et al 2005][research_rajsaiv_robinsonraymondc_2005]\] \[[Shaffer et al 2005][research_shaffer_ross_2005]\] \[[Xu 2005][research_xu_2005]\] \[[Bollino et al 2006][research_bollino_oppenheimer_2006]\] \[[Jategaonkar et al 2006][research_jategaonkar_behr_2006]\] \[[Johnson et al 2006][research_johnson_jacobs_2006]\] \[[Martin 2006][research_martin_2006]\] \[[Martindale 2006][research_martindale_2006]\] \[[Michael A. Bolender 2006][research_michaelabolender_2006]\] \[[Nonaka et al 2006][research_nonaka_watanabe_2006]\] \[[Rasky et al 2006][research_rasky_pittman_2006]\] \[[Suzuki et al 2006][research_suzuki_nonaka_2006]\] \[[Yang et al 2006][research_yang_hu_2006]\] \[[Burton et al 2007][research_burton_loth_2007]\] \[[Kalden 2007][research_kalden_2007]\] \[[Michalski and Johnson 2007][research_michalski_johnson_2007]\] \[[Suzuki et al 2007][research_suzuki_nonaka_2007]\] \[[Vaughn et al 2007][research_vaughn_singh_2007]\] \[[Caogen et al 2008][research_caogen_hongjun_2008]\] \[[Donahue et al 2008][research_donahue_weldon_2008]\] \[[Hellman and Tejtel 2008][research_hellman_tejtel_2008]\] \[[Jiang and Ordonez 2008][research_jiang_ordonez_2008]\] \[[Johnson and Servidio 2008][research_johnson_servidio_2008]\] \[[Liaoni Wu et al 2008][research_liaoniwu_yiminhuang_2008]\] \[[Garg and Dodiyal 2009][research_garg_dodiyal_2009]\] \[[Jiang and Ordóñez 2009][research_jiang_ordonez_2009]\] \[[Jurist 2009][research_jurist_2009]\] \[[Kelly et al 2009][research_kelly_charania_2009]\] \[[Kluever et al 2009][research_kluever_horneman_2009]\] \[[Kuzin et al 2009][research_kuzin_lozin_2009]\] \[[Lemieux 2009][research_lemieux_2009]\] \[[Lin, C. F. et al 2009][research_lincf_figueroaf_2009]\] \[[Molina et al 2009][research_molina_johnson_2009]\] \[[Xu 2009][research_xu_2009]\] \[[Bradford and St. Germain 2010][research_bradford_stgermain_2010]\] \[[Fischbach, Sean R. and Kenny, R. Jeremy 2010][research_fischbachseanr_kennyrjeremy_2010]\] \[[Kothari and Webber 2010][research_kothari_webber_2010]\] \[[Lin et al 2010][research_lin_figueroa_2010]\] \[[Namera et al 2010][research_namera_takaki_2010]\] \[[Rippere, Troy B. and Wiens, Gloria J. 2010][research_ripperetroyb_wiensgloriaj_2010]\] \[[Xu and Tang 2010][research_xu_tang_2010]\] \[[Cowling 2011][research_cowling_2011]\] \[[Hellman et al 2011][research_hellman_remillard_2011]\] \[[Hellman et al 2011][research_hellman_wallace_2011]\] \[[Hutchison 2011][research_hutchison_2011]\] \[[Kuzuu et al 2011][research_kuzuu_kitamura_2011]\] \[[Letchworth 2011][research_letchworth_2011]\] \[[Mains 2011][research_mains_2011]\] \[[Moore, D. R. and Phelps, W. J. 2011][research_mooredr_phelpswj_2011]\] \[[Moore, Dennis R. and Phelps, Willie J. 2011][research_mooredennisr_phelpswilliej_2011]\] \[[Smith 2011][research_smith_2011]\] \[[Song et al 2011][research_song_song_2011]\] \[[SpaceX to cut launch 2011][research_spacex_to_2011]\] \[[Spaceport America attracts reusable 2011][research_spaceport_america_2011]\] \[[Clayton, J. Louie 2012][research_claytonjlouie_2012]\] \[[Dissel et al 2012][research_dissel_huseman_2012]\] \[[Lemieux and Murray 2012][research_lemieux_murray_2012]\] \[[Losik, Ph.D. 2012][research_losikphd_2012]\] \[[Nonaka et al 2012][research_nonaka_nishida_2012]\] \[[Paschall and Brady 2012][research_paschall_brady_2012]\] \[[Chen et al 2013][research_chen_yang_2013]\] \[[Hellman et al 2013][research_hellman_pleiman_2013]\] \[[Reusable rocket lander continues 2013][research_reusable_rocket_2013]\] \[[SpaceX gets a rival 2013][research_spacex_gets_2013]\] \[[Stansbury et al 2013][research_stansbury_towhidnejead_2013]\] \[[Stewart, Christine E. 2013][research_stewartchristinee_2013]\] \[[Zhou et al 2013][research_zhou_zhou_2013]\] \[[Baran et al 2014][research_baran_blanchard_2014]\] \[[Gong et al 2014][research_gong_chen_2014]\] \[[Launch of SpaceX reusable 2014][research_launch_of_2014]\] \[[Mu and Zhang 2014][research_mu_zhang_2014]\] \[[Najam 2014][research_najam_2014]\] \[[Skariya et al 2014][research_skariya_sebastian_2014]\] \[[SpaceX tests legs that 2014][research_spacex_tests_2014]\] \[[SpaceX to test rocket 2014][research_spacex_to_2014]\] \[[Webb et al 2014][research_webb_williams_2014]\] \[[Wuilbercq et al 2014][research_wuilbercq_pescetelli_2014]\] \[[Yu et al 2014][research_yu_sun_2014]\] \[[European company is developing 2015][research_european_company_2015]\] \[[Gong et al 2015][research_gong_bing_2015]\] \[[Huang et al 2015][research_huang_zhang_2015]\] \[[India to launch prototype 2015][research_india_to_2015]\] \[[Junaid R and Beebi M 2015][research_junaidr_beebim_2015]\] \[[Ragab and Cheatwood 2015][research_ragab_cheatwood_2015]\] \[[Smart 2015][research_smart_2015]\] \[[Su and Wang 2015][research_su_wang_2015]\] \[[Tartabini, Paul V. et al 2015][research_tartabinipaulv_beatyjamesr_2015]\] \[[United Launch Alliance announces 2015][research_united_launch_2015]\] \[[Zhi et al 2015][research_zhi_ran_2015]\] \[[Childress-Thompson, Rhonda et al 2016][research_childressthompsonrhonda_thomasdale_2016]\] \[[Devanath and Beebi 2016][research_devanath_beebi_2016]\] \[[Jianguo et al 2016][research_jianguo_guoqing_2016]\] \[[Mueller et al 2016][research_mueller_trigwell_2016]\] \[[Nizin et al 2016][research_nizin_antony_2016]\] \[[Numerical Optimization on Approach 2016][research_numerical_optimization_2016]\] \[[Reed, John G. et al 2016][research_reedjohng_ragabmohamedm_2016]\] \[[Williamson 2016][research_williamson_2016]\] \[[Yang et al 2016][research_yang_qiu_2016]\] \[[Yoshida et al 2016][research_yoshida_kimura_2016]\] \[[AL-Bakri and Kluever 2017][research_albakri_kluever_2017]\] \[[Aogaki et al 2017][research_aogaki_kitamura_2017]\] \[[Childress-Thompson, Rhonda et al 2017][research_childressthompsonrhonda_dalethomasl_2017]\] \[[Dai et al 2017][research_dai_liu_2017]\] \[[Demidovich 2017][research_demidovich_2017]\] \[[Hao et al 2017][research_hao_peng_2017]\] \[[Lei et al 2017][research_lei_yan_2017]\] \[[Liu et al 2017][research_liu_dai_2017]\] \[[Sippel et al 2017][research_sippel_bussler_2017]\] \[[Sivan and Murmu 2017][research_sivan_murmu_2017]\] \[[Success for SpaceX reusable 2017][research_success_for_2017]\] \[[Umadevi et al 2017][research_umadevi_navas_2017]\] \[[Zhang et al 2017][research_zhang_zong_2017]\] \[[Zhang et al 2017][research_zhang_li_2017]\] \[[Zhang et al 2017][research_zhang_guo_2017]\] \[[Abrahamm and Valsa 2018][research_abrahamm_valsa_2018]\] \[[Chen et al 2018][research_chen_mu_2018]\] \[[Choo et al 2018][research_choo_mun_2018]\] \[[Fuchs et al 2018][research_fuchs_haskell_2018]\] \[[Gupta et al 2018][research_gupta_anilkumar_2018]\] \[[ISRO Releases the Special 2018][research_isro_releases_the_2018]\] \[[Ma et al 2018][research_ma_wang_2018]\] \[[Masilamani et al 2018][research_masilamani_kumar_2018]\] \[[Sivan and Pandian 2018][research_sivan_pandian_2018]\] \[[Szmuk and Acikmese 2018][research_szmuk_acikmese_2018]\] \[[Wang and Song 2018][research_wang_song_2018]\] \[[Wang and Song 2018][research_wang_song_2018_b]\] \[[Zhang et al 2018][research_zhang_xu_2018]\] \[[Aogaki et al 2019][research_aogaki_kitamura_2019]\] \[[Aprovitola et al 2019][research_aprovitola_iuspa_2019]\] \[[Aprovitola et al 2019][research_aprovitola_iuspa_2019_b]\] \[[Chen and Ma 2019][research_chen_ma_2019_b]\] \[[Chen et al 2019][research_chen_ma_2019]\] \[[Cusick and Kontis 2019][research_cusick_kontis_2019]\] \[[Inatomi et al 2019][research_inatomi_kitamura_2019]\] \[[Lei et al 2019][research_lei_hongbo_2019]\] \[[Ma et al 2019][research_ma_wang_2019]\] \[[Nardozzo et al 2019][research_nardozzo_popkin_2019]\] \[[Wang and Song 2019][research_wang_song_2019]\] \[[Antonelli et al 2020][research_antonelli_pepe_2020]\] \[[Brevault et al 2020][research_brevault_balesdent_2020]\] \[[Buzuluk et al 2020][research_buzuluk_plokhikh_2020]\] \[[Jiandong et al 2020][research_jiandong_qiang_2020]\] \[[Kawatsu et al 2020][research_kawatsu_tsutsumi_2020]\] \[[Li et al 2020][research_li_xing_2020]\] \[[Shukla et al 2020][research_shukla_singh_2020]\] \[[Timofeev 2020][research_timofeev_2020]\] \[[Usmonov and Kretov 2020][research_usmonov_kretov_2020]\] \[[Wang et al 2020][research_wang_chen_2020]\] \[[Wu et al 2020][research_wu_tian_2020]\] \[[Xie et al 2020][research_xie_zhang_2020]\] \[[Chen et al 2021][research_chen_xing_2021]\] \[[Cheng et al 2021][research_cheng_jing_2021]\] \[[Lukin et al 2021][research_lukin_prisiazhnyi_2021]\] \[[Pidvysotskyi 2021][research_pidvysotskyi_2021]\] \[[Su et al 2021][research_su_dai_2021]\] \[[Su et al 2021][research_su_dai_2021_b]\] \[[Wang et al 2021][research_wang_song_2021]\] \[[Yuan et al 2021][research_yuan_zhao_2021]\] \[[Botelho et al 2022][research_botelho_martinez_2022]\] \[[Brooks 2022][research_brooks_2022]\] \[[Lei et al 2022][research_lei_zhang_2022]\] \[[Li et al 2022][research_li_long_2022]\] \[[Mo et al 2022][research_mo_li_2022]\] \[[Mukundan et al 2022][research_mukundan_maity_2022]\] \[[Prasad 2022][research_prasad_2022]\] \[[Qi et al 2022][research_qi_cheng_2022]\] \[[Sithara and Shenil 2022][research_sithara_shenil_2022]\] \[[Thies 2022][research_thies_2022]\] \[[Wang et al 2022][research_wang_wei_2022]\] \[[Yue et al 2022][research_yue_lin_2022]\] \[[Agarwal 2023][research_agarwal_2023]\] \[[Brociek et al 2023][research_brociek_hetmaniok_2023]\] \[[Dong et al 2023][research_dong_wu_2023]\] \[[Guadagnini et al 2023][research_guadagnini_dezaiacomo_2023]\] \[[Guo et al 2023][research_guo_zhao_2023]\] \[[Liu 2023][research_liu_2023]\] \[[Radhakrishnan et al 2023][research_radhakrishnan_hari_2023]\] \[[Wang et al 2023][research_wang_li_2023]\] \[[Wu and Zhang 2023][research_wu_zhang_2023]\] \[[Allard 2024][research_allard_2024]\] \[[Alvord et al 2024][research_alvord_arias_2024]\] \[[C et al 2024][research_c_vinaykumar_2024]\] \[[Cheng et al 2024][research_cheng_jing_2024]\] \[[Costa et al 2024][research_costa_parente_2024]\] \[[Gibart et al 2024][research_gibart_pietlahanier_2024]\] \[[Hara et al 2024][research_hara_mamashita_2024]\] \[[Hetmaniok et al 2024][research_hetmaniok_brociek_2024]\] \[[Imhuelse et al 2024][research_imhuelse_zydel_2024]\] \[[Islam 2024][research_islam_2024]\] \[[Kim et al 2024][research_kim_woldeyohannis_2024]\] \[[Liu 2024][research_liu_2024]\] \[[Martin et al 2024][research_martin_stay_2024]\] \[[Mirzabayova and Rustamov 2024][research_mirzabayova_rustamov_2024]\] \[[Ren et al 2024][research_ren_ma_2024]\] \[[Scarlatella et al 2024][research_scarlatella_guadagnini_2024]\] \[[Serçeoglu 2024][research_serceoglu_2024]\] \[[Shoyama and Hirakawa 2024][research_shoyama_hirakawa_2024]\] \[[Singh et al 2024][research_singh_luyten_2024]\] \[[Wang et al 2024][research_wang_xu_2024]\] \[[Wang et al 2024][research_wang_wang_2024]\] \[[Xing et al 2024][research_xing_feng_2024]\] \[[Xinguo et al 2024][research_xinguo_ting_2024]\] \[[Yang et al 2024][research_yang_gan_2024]\] \[[Zhao et al 2024][research_zhao_han_2024]\] \[[Zhou et al 2024][research_zhou_wang_2024]\] \[[Zhou et al 2024][research_zhou_hu_2024]\] \[[Çelik and Demirezen 2024][research_celik_demirezen_2024]\] \[[Agarwalla 2025][research_agarwalla_2025]\] \[[Chen et al 2025][research_chen_yang_2025]\] \[[Colicci et al 2025][research_colicci_noonan_2025]\] \[[Fox 2025][research_fox_2025]\] \[[Fox 2025][research_fox_2025_b]\] \[[Iafrate et al 2025][research_iafrate_brandonisio_2025]\] \[[Iwabuchi and Hashimoto 2025][research_iwabuchi_hashimoto_2025]\] \[[Li et al 2025][research_li_zhao_2025]\] \[[Nair and Kukreja 2025][research_nair_kukreja_2025]\] \[[Purcell et al 2025][research_purcell_wicklund_2025]\] \[[Roma Rubi et al 2025][research_romarubi_kuo_2025]\] \[[Ryu et al 2025][research_ryu_kim_2025]\] \[[Satriani et al 2025][research_satriani_abdiani_2025]\] \[[Su and Liu 2025][research_su_liu_2025]\] \[[Su and Liu 2025][research_su_liu_2025_b]\] \[[Swiss Students Achieve Europe's 2025][research_swiss_students_2025]\] \[[Tong et al 2025][research_tong_shi_2025]\] \[[Trajectory Shaping Guidance for 2025][research_trajectory_shaping_2025]\] \[[Wang et al 2025][research_wang_gan_2025]\] \[[Xu et al 2025][research_xu_guo_2025]\] \[[Zaragoza Prous et al 2025][research_zaragozaprous_grustangutierrez_2025]\] \[[Zhou et al 2025][research_zhou_minzhao_2025]\] \[[Zimmerli et al 2025][research_zimmerli_arkwright_2025]\] \[[China achieves first reusable 2026][research_china_achieves_2026]\] \[[Chowdhury et al 2026][research_chowdhury_joshi_2026]\] \[[Depardon 2026][research_depardon_2026]\] \[[Fan et al 2026][research_fan_yao_2026]\] \[[Huang 2026][research_huang_2026]\] \[[Huang and Zhang 2026][research_huang_zhang_2026]\] \[[Khamlak 2026][research_khamlak_2026]\] \[[Kim et al 2026][research_kim_ko_2026]\] \[[Lee et al 2026][research_lee_jo_2026]\] \[[Li et al 2026][research_li_paik_2026]\] \[[Long et al 2026][research_long_li_2026]\] \[[Maru et al 2026][research_maru_kobayashi_2026]\] \[[Mastromatteo et al 2026][research_mastromatteo_gaverina_2026]\] \[[Oktaviana et al 2026][research_oktaviana_alwan_2026]\] \[[Ren 2026][research_ren_2026]\] \[[Response Analysis of Landing 2026][research_response_analysis_2026]\] \[[Reusable Launch Vehicle Landing 2026][research_reusable_launch_2026]\] \[[Romano et al 2026][research_romano_pisano_2026]\] \[[Wang and Miao 2026][research_wang_miao_2026]\] \[[Wang et al 2026][research_wang_xu_2026]\] \[[Wang et al 2026][research_wang_zhang_2026]\] \[[Wang et al 2026][research_wang_song_2026]\] \[[Xiao et al 2026][research_xiao_chang_2026]\] \[[Yamashita et al 2026][research_yamashita_nutzel_2026]\] \[[liu et al 2026][research_liu_cheng_2026]\] \[[Al Bakri][research_albakri]\] \[[Burchett][research_burchett]\] \[[Caplin][research_caplin]\] \[[Coakley][research_coakley]\] \[[Dan Dorney][research_dandorney]\] \[[Deming Zhang et al][research_demingzhang_guiqingchen]\] \[[Galli][research_galli]\] \[[Guo and Musgrave][research_guo_musgrave]\] \[[Guodong Ning et al][research_guodongning_shuguangzhang]\] \[[Julian S. Hamilton][research_julianshamilton]\] \[[Kitsios and Lygeros][research_kitsios_lygeros]\] \[[Lorenzo et al][research_lorenzo_merrill]\] \[[Ménou][research_menou]\] \[[Pérez Roca][research_perezroca]\] \[[Shtessel and Krupp][research_shtessel_krupp]\] \[[Sun][research_sun]\] \[[Wetzel][research_wetzel]\] \[[Xiaowen Dai et al][research_xiaowendai_ray]\]

### Stability from surfaces, including surfaces that are also legs

**144 records.** \[[Hart, Roger G. and Katz, Ellis R. 1949][research_hartrogerg_katzellisr_1949]\] \[[Cole, Henry, A, jr and Abramovitz, Marvin 1952][research_colehenryajr_abramovitzmarvin_1952]\] \[[James, Carlton S and Carros, Robert J 1953][research_jamescarltons_carrosrobertj_1953]\] \[[Johnson, Harold S and Hayes, William C 1953][research_johnsonharolds_hayeswilliamc_1953]\] \[[Burrows, Dale L and Newman, Ernest E 1954][research_burrowsdalel_newmanerneste_1954]\] \[[Kurbjun, Max C 1954][research_kurbjunmaxc_1954]\] \[[Howell, Robert R. and Braslow, Albert L. 1955][research_howellrobertr_braslowalbertl_1955]\] \[[Schmidt 1955][research_schmidt_1955]\] \[[Gillespie, W., Jr. 1956][research_gillespiewjr_1956]\] \[[Simon 1956][research_simon_1956]\] \[[Appich, W. H., Jr. and Turner, K. L. 1958][research_appichwhjr_turnerkl_1958]\] \[[Foss, Willard E, Jr et al 1958][research_fosswillardejr_runckeljackf_1958]\] \[[J J Donegan 1958][research_jjdonegan_1958]\] \[[James, Carlton S. 1960][research_jamescarltons_1960]\] \[[Sung and Park 1960][research_sung_park_1960]\] \[[Medukhovskii 1961][research_medukhovskii_1961]\] \[[Leland H Jorgensen et al 1962][research_lelandhjorgensen_jrichardspahr_1962]\] \[[Ziegler 1963][research_ziegler_1963]\] \[[Burt and Hillsamer 1964][research_burt_hillsamer_1964]\] \[[Duncan and Ensey 1964][research_duncan_ensey_1964]\] \[[Lieske and Kochenderfer 1966][research_lieske_kochenderfer_1966]\] \[[Arrington et al 1967][research_arrington_molloy_1967]\] \[[Babb, C. D. and Fuller, D. E. 1967][research_babbcd_fullerde_1967]\] \[[Ferris, J. C. 1967][research_ferrisjc_1967]\] \[[Lewak 1967][research_lewak_1967]\] \[[Fuller, D. E. 1968][research_fullerde_1968]\] \[[Washington et al 1968][research_washington_pettis_1968]\] \[[De Angelis, V. M. and Tang, M. H. 1969][research_deangelisvm_tangmh_1969]\] \[[Huerta 1969][research_huerta_1969]\] \[[Dahlke and Pettis 1970][research_dahlke_pettis_1970]\] \[[Daniels 1970][research_daniels_1970]\] \[[Tang, M. H. 1971][research_tangmh_1971]\] \[[Tang, M. H. and Pearson, G. P. E. 1971][research_tangmh_pearsongpe_1971]\] \[[Ellis, R. R. and Gamble, M. 1972][research_ellisrr_gamblem_1972]\] \[[Luckert 1973][research_luckert_1973]\] \[[Spencer, B., Jr. and Fournier, R. H. 1973][research_spencerbjr_fournierrh_1973]\] \[[Trescot, C. D., Jr. et al 1973][research_trescotcdjr_fostergv_1973]\] \[[Lindsay and Jordan 1975][research_lindsay_jordan_1975]\] \[[Fansler and Schmidt 1976][research_fansler_schmidt_1976]\] \[[Jenke 1976][research_jenke_1976]\] \[[Kassner, D. L. and Wettlaufer, B. 1977][research_kassnerdl_wettlauferb_1977]\] \[[Jernell, L. S. and Croom, D. R. 1979][research_jernellls_croomdr_1979]\] \[[Rollstin 1979][research_rollstin_1979]\] \[[Blair, A. B., Jr. 1980][research_blairabjr_1980]\] \[[Schmidt 1980][research_schmidt_1980]\] \[[Sawyer, W. C. et al 1981][research_sawyerwc_montawj_1981]\] \[[Blair, A. B., Jr. et al 1983][research_blairabjr_allenjm_1983]\] \[[Smeltzer, D. B. et al 1983][research_smeltzerdb_durstonda_1983]\] \[[Weinacht et al 1984][research_weinacht_guidos_1984]\] \[[Fancher 1985][research_fancher_1985]\] \[[Whyte et al 1985][research_whyte_hathaway_1985]\] \[[Celmins 1987][research_celmins_1987]\] \[[Brooks and Burkhalter 1988][research_brooks_burkhalter_1988]\] \[[Jenn and Nelson 1988][research_jenn_nelson_1988]\] \[[Nelson 1988][research_nelson_1988]\] \[[Pagendarm et al 1988][research_pagendarm_laurien_1988]\] \[[Bornstein et al 1989][research_bornstein_celmins_1989]\] \[[Plostins et al 1990][research_plostins_celmins_1990]\] \[[Est and Nelson 1991][research_est_nelson_1991]\] \[[Blair, A. B., Jr. et al 1992][research_blairabjr_dillonjamesl_1992]\] \[[Bossi and Nelson 1992][research_bossi_nelson_1992]\] \[[Washington et al 1993][research_washington_booth_1993]\] \[[Lesieutre et al 1994][research_lesieutre_lesieutre_1994]\] \[[Miller and Washington 1994][research_miller_washington_1994]\] \[[Yang 1994][research_yang_1994]\] \[[Burkhalter and Frank 1995][research_burkhalter_frank_1995]\] \[[Moran and Beran 1995][research_moran_beran_1995]\] \[[Burkhalter and Frank 1996][research_burkhalter_frank_1996]\] \[[Dillon, Jr. 1996][research_dillonjr_1996]\] \[[Eugene, L. Tu 1996][research_eugeneltu_1996]\] \[[Huffman, Jr. et al 1996][research_huffmanjr_tilmann_1996]\] \[[Bosworth, John T. and Burken, John J. 1997][research_bosworthjohnt_burkenjohnj_1997]\] \[[Costello and Costello 1997][research_costello_costello_1997]\] \[[Schmidt et al 1997][research_schmidt_donovan_1997]\] \[[Gnoffo, Peter A. et al 1998][research_gnoffopetera_braunrobertd_1998]\] \[[Sun and Khalid 1998][research_sun_khalid_1998]\] \[[Erline and Hathaway 1999][research_erline_hathaway_1999]\] \[[Costello and Agarwalla 2000][research_costello_agarwalla_2000]\] \[[Costello and Agarwalla 2001][research_costello_agarwalla_2001]\] \[[DeSpirito and Sahu 2001][research_despirito_sahu_2001]\] \[[Dillo 2001][research_dillo_2001]\] \[[Fournier 2001][research_fournier_2001]\] \[[Landers et al 2003][research_landers_hall_2003]\] \[[Lin et al 2003][research_lin_huang_2003]\] \[[He et al 2004][research_he_he_2004]\] \[[Ma et al 2005][research_ma_deng_2005]\] \[[Theerthamalai et al 2005][research_theerthamalai_manisekaran_2005]\] \[[Blake and Cunningham 2006][research_blake_cunningham_2006]\] \[[Wilks 2006][research_wilks_2006]\] \[[Erickson, Gary E. 2007][research_ericksongarye_2007]\] \[[Ghosh et al 2008][research_ghosh_singhal_2008]\] \[[Khalil et al 2009][research_khalil_abdalla_2009]\] \[[Debiasi et al 2010][research_debiasi_yan_2010]\] \[[Aftosmis, Michael J. 2011][research_aftosmismichaelj_2011]\] \[[Fresconi 2011][research_fresconi_2011]\] \[[Kless and Aftosmis 2011][research_kless_aftosmis_2011]\] \[[Kumar et al 2011][research_kumar_misra_2011]\] \[[Pruzan et al 2011][research_pruzan_mendenhall_2011]\] \[[Terhune et al 2011][research_terhune_hollis_2011]\] \[[DeSpirito 2012][research_despirito_2012]\] \[[Debiasi 2012][research_debiasi_2012]\] \[[Ji et al 2012][research_ji_wang_2012]\] \[[Kumar et al 2012][research_kumar_mishra_2012]\] \[[Larin 2012][research_larin_2012]\] \[[Silton and Bhagwandin 2012][research_silton_bhagwandin_2012]\] \[[DeSpirito 2013][research_despirito_2013]\] \[[Krishnamurthy et al 2013][research_krishnamurthy_shende_2013]\] \[[Coirier et al 2014][research_coirier_stutts_2014]\] \[[Despeyroux et al 2014][research_despeyroux_desaulnier_2014]\] \[[Elsaadany and Wen-Jun 2014][research_elsaadany_wenjun_2014]\] \[[Enciu and Rosen 2015][research_enciu_rosen_2015]\] \[[Garcia and Silveira 2015][research_garcia_silveira_2015]\] \[[Silton and Coyle 2015][research_silton_coyle_2015]\] \[[Silton and Fresconi 2015][research_silton_fresconi_2015]\] \[[Silton and Coyle 2016][research_silton_coyle_2016]\] \[[Xu and Pei 2016][research_xu_pei_2016]\] \[[Zhang et al 2016][research_zhang_yu_2016]\] \[[Zhaoqing and Hailong 2016][research_zhaoqing_hailong_2016]\] \[[Koomphati 2017][research_koomphati_2017]\] \[[Muralidhar and Bhandari 2017][research_muralidhar_bhandari_2017]\] \[[Tripathi et al 2018][research_tripathi_misra_2018]\] \[[Anandaraj et al 2019][research_anandaraj_sarkar_2019]\] \[[Tripathi et al 2019][research_tripathi_sucheendran_2019]\] \[[Tripathi et al 2019][research_tripathi_sucheendran_2019_b]\] \[[Ding et al 2020][research_ding_yang_2020]\] \[[Meda 2020][research_meda_2020]\] \[[Dol 2021][research_dol_2021]\] \[[Salahudden and Ghosh 2021][research_salahudden_ghosh_2021]\] \[[Dinçer and Sezer Uzol 2022][research_dincer_sezeruzol_2022]\] \[[Bordachev et al 2023][research_bordachev_kolga_2023]\] \[[Ren et al 2023][research_ren_wang_2023]\] \[[Storey 2023][research_storey_2023]\] \[[Wang and Hsu 2023][research_wang_hsu_2023]\] \[[Żurawka et al 2023][research_zurawka_sahbon_2023]\] \[[Liu and Tan 2024][research_liu_tan_2024]\] \[[Dixit et al 2025][research_dixit_goplani_2025]\] \[[Liu et al 2025][research_liu_zhu_2025]\] \[[Pribadi 2025][research_pribadi_2025]\] \[[Tripathi et al 2025][research_tripathi_sucheendran_2025]\] \[[Anuskiewicz et al 2026][research_anuskiewicz_cave_2026]\] \[[Montesinos et al 2026][research_montesinos_davis_2026]\] \[[Woodyard 2026][research_woodyard_2026]\] \[[Wu et al 2026][research_wu_li_2026]\] \[[Yadav et al 2026][research_yadav_tripathi_2026]\]

### Drag, fineness, and the price of being short

**190 records.** \[[R. 1928][research_r_1928]\] \[[Zahm, A F et al 1929][research_zahmaf_smithrh_1929]\] \[[Abbott, Ira H 1937][research_abbottirah_1937]\] \[[Thomas 1942][research_thomas_1942]\] \[[Brown, Clinton E and Parker, Hermon M 1945][research_brownclintone_parkerhermonm_1945]\] \[[Jones, Robert T and Margolis, Kenneth 1946][research_jonesrobertt_margoliskenneth_1946]\] \[[Katz, Ellis R 1947][research_katzellisr_1947]\] \[[Mastrocola, N 1947][research_mastrocolan_1947]\] \[[Mathews, Charles W and Thompson, Jim Rogers 1947][research_mathewscharlesw_thompsonjimrogers_1947]\] \[[Nielsen, Jack N 1947][research_nielsenjackn_1947]\] \[[Thompson, Jim Rogers and Mathews, Charles W 1947][research_thompsonjimrogers_mathewscharlesw_1947]\] \[[Thompson, Jim Rogers and Kurbjun, Max C 1948][research_thompsonjimrogers_kurbjunmaxc_1948]\] \[[Katz, Ellis R 1949][research_katzellisr_1949]\] \[[Thompson, Jim Rogers 1950][research_thompsonjimrogers_1950]\] \[[Adams, Mac C. 1951][research_adamsmacc_1951]\] \[[Cohen, Robert J 1951][research_cohenrobertj_1951]\] \[[Cortright, Edgar M, Jr and Schroeder, Albert H 1951][research_cortrightedgarmjr_schroederalberth_1951]\] \[[Friedman, Morris D 1951][research_friedmanmorrisd_1951]\] \[[Lopatoff, Mitchell 1951][research_lopatoffmitchell_1951]\] \[[Spahr, J Richard and Dickey, Robert R 1951][research_spahrjrichard_dickeyrobertr_1951]\] \[[Welsh, Clement J and Demoraes, Carlos A 1951][research_welshclementj_demoraescarlosa_1951]\] \[[Chapman, Dean R 1952][research_chapmandeanr_1952]\] \[[Kawamura 1952][research_kawamura_1952]\] \[[Kurbjun, Max C and Thompson, Jim Rogers 1952][research_kurbjunmaxc_thompsonjimrogers_1952]\] \[[Love, Eugene S et al 1952][research_loveeugenes_colettidonalde_1952]\] \[[Sommer, Simon C and Stark, James A 1952][research_sommersimonc_starkjamesa_1952]\] \[[Benedikt 1953][research_benedikt_1953]\] \[[Bromm, August F, Jr and Goodwin, Julia M 1953][research_brommaugustfjr_goodwinjuliam_1953]\] \[[Jack, John R 1953][research_jackjohnr_1953]\] \[[Loposer, J Dan and Mottard, Elmo J 1953][research_loposerjdan_mottardelmoj_1953]\] \[[Hopko, Russell N 1954][research_hopkorusselln_1954]\] \[[Mottard, Elmo J and Loposer, J Dan 1954][research_mottardelmoj_loposerjdan_1954]\] \[[Nelson, W. J. and Henry, B. Z., Jr. 1955][research_nelsonwj_henrybzjr_1955]\] \[[Parker, Hermon M 1955][research_parkerhermonm_1955]\] \[[Bromm, August, F, jr and Goodwin, Julia M 1956][research_brommaugustfjr_goodwinjuliam_1956]\] \[[Falanga, Ralph A 1956][research_falangaralpha_1956]\] \[[Falanga, Ralph A and Leiss, Abraham 1956][research_falangaralpha_leissabraham_1956]\] \[[Harder, Keith C and Rennemann, Conrad, Jr 1956][research_harderkeithc_rennemannconradjr_1956]\] \[[Parker, Hermon M 1956][research_parkerhermonm_1956]\] \[[Eggers, A J, Jr et al 1957][research_eggersajjr_resnikoffmeyerm_1957]\] \[[Gillespie, Warren JR 1957][research_gillespiewarrenjr_1957]\] \[[Kawamura and Karashima 1957][research_kawamura_karashima_1957]\] \[[Lomax, Harvard 1957][research_lomaxharvard_1957]\] \[[Nelson, William J and Scott, William R 1958][research_nelsonwilliamj_scottwilliamr_1958]\] \[[Perkins, Edward W et al 1958][research_perkinsedwardw_jorgensenlelandh_1958]\] \[[Effect of uniformly distributed 1959][research_effect_of_1959]\] \[[Henning, Allen B. 1959][research_henningallenb_1959]\] \[[Gillespie, Warren, Jr. 1960][research_gillespiewarrenjr_1960]\] \[[McKinney, Linwood W. 1960][research_mckinneylinwoodw_1960]\] \[[Morris 1961][research_morris_1961]\] \[[Brazzel 1963][research_brazzel_1963]\] \[[Macagno and Hsieh 1963][research_macagno_hsieh_1963]\] \[[Miele and Hull 1963][research_miele_hull_1963]\] \[[Tetervin 1963][research_tetervin_1963]\] \[[Sims and Hahn 1964][research_sims_hahn_1964]\] \[[Connolly 1965][research_connolly_1965]\] \[[Eggers, A. J., Jr. 1965][research_eggersajjr_1965]\] \[[Vasil'ev 1966][research_vasilev_1966]\] \[[Crowe 1967][research_crowe_1967]\] \[[Grodzovskii 1968][research_grodzovskii_1968]\] \[[Trimmer 1968][research_trimmer_1968]\] \[[Jackson, C. M., Jr. and Smith, R. S. 1969][research_jacksoncmjr_smithrs_1969]\] \[[Tkalenko 1969][research_tkalenko_1969]\] \[[Addy 1970][research_addy_1970]\] \[[Street 1970][research_street_1970]\] \[[Rubin 1971][research_rubin_1971]\] \[[Usry, J. W. and Wallace, J. W. 1971][research_usryjw_wallacejw_1971]\] \[[Berrier, B. L. 1972][research_berrierbl_1972]\] \[[Tanner 1972][research_tanner_1972]\] \[[Reubush, D. E. 1973][research_reubushde_1973]\] \[[Reubush, D. E. and Runckel, J. F. 1973][research_reubushde_runckeljf_1973]\] \[[Head, V. L. 1974][research_headvl_1974]\] \[[Hess and James 1975][research_hess_james_1975]\] \[[Micci 1975][research_micci_1975]\] \[[Jones, R. T. and Margolis, K. 1976][research_jonesrt_margolisk_1976]\] \[[Korkegi and Freeman 1976][research_korkegi_freeman_1976]\] \[[Mikhail 1979][research_mikhail_1979]\] \[[Putnam, L. E. 1979][research_putnamle_1979]\] \[[Bauer 1980][research_bauer_1980]\] \[[Lijewski 1980][research_lijewski_1980]\] \[[Payne 1980][research_payne_1980]\] \[[Payne et al 1980][research_payne_hartley_1980]\] \[[Plant, T. J. et al 1980][research_planttj_nugentj_1980]\] \[[Gai and Sharma 1981][research_gai_sharma_1981]\] \[[Lijewski 1981][research_lijewski_1981]\] \[[Peters 1981][research_peters_1981]\] \[[Peterson, R. L. 1981][research_petersonrl_1981]\] \[[Quass, B. et al 1981][research_quassb_howardf_1981]\] \[[Schiff and Sturek 1981][research_schiff_sturek_1981]\] \[[Vasil'chenko 1981][research_vasilchenko_1981]\] \[[Kapoor 1982][research_kapoor_1982]\] \[[Lijewski 1982][research_lijewski_1982]\] \[[Miller, C. G., III 1982][research_millercgiii_1982]\] \[[Gloss, B. B. and Sewall, W. G. 1983][research_glossbb_sewallwg_1983]\] \[[Howard, F. G. et al 1983][research_howardfg_goodmanwl_1983]\] \[[Howard, F. G. and Goodman, W. L. 1984][research_howardfg_goodmanwl_1984]\] \[[Howard, F. G. and Goodman, W. L. 1985][research_howardfg_goodmanwl_1985]\] \[[Larina 1985][research_larina_1985]\] \[[Nielsen 1985][research_nielsen_1985]\] \[[Mcmillin and Wood 1986][research_mcmillin_wood_1986]\] \[[Osawa and Hewitt 1986][research_osawa_hewitt_1986]\] \[[McMillin and Wood 1987][research_mcmillin_wood_1987]\] \[[Newcomb, A. W. 1988][research_newcombaw_1988]\] \[[Goradia, S. H. et al 1989][research_goradiash_bobbittpj_1989]\] \[[Moore, F. G. et al 1993][research_moorefg_hymert_1993]\] \[[Roshko 1993][research_roshko_1993]\] \[[Carlson, John R. 1996][research_carlsonjohnr_1996]\] \[[ESDU Data Item estimates 1998][research_esdu_data_1998]\] \[[Riggins et al 1998][research_riggins_nelson_1998]\] \[[Candler and Kelley 1999][research_candler_kelley_1999]\] \[[Malone, Michael B. and Peavey, Charles C. 1999][research_malonemichaelb_peaveycharlesc_1999]\] \[[Riggins et al 1999][research_riggins_nelson_1999]\] \[[Glagolev et al 2000][research_glagolev_zubkov_2000]\] \[[Jones et al 2000][research_jones_townsend_2000]\] \[[Guy et al 2001][research_guy_mclaughlin_2001]\] \[[Whitmore et al 2001][research_whitmore_sprague_2001]\] \[[Garanin et al 2002][research_garanin_glagolev_2002]\] \[[Shang 2002][research_shang_2002]\] \[[Eremenko et al 2003][research_eremenko_mouton_2003]\] \[[Rallabhandi and Mavris 2003][research_rallabhandi_mavris_2003]\] \[[Durgesh et al 2004][research_durgesh_naughton_2004]\] \[[Myrabo et al 2004][research_myrabo_raizer_2004]\] \[[Nikolic and Jumper 2004][research_nikolic_jumper_2004]\] \[[Palaniappan and Jameson 2004][research_palaniappan_jameson_2004]\] \[[Sawada et al 2004][research_sawada_kunimasu_2004]\] \[[Knight and Tso 2005][research_knight_tso_2005]\] \[[Aul'chenko 2006][research_aulchenko_2006]\] \[[Cummings et al 2006][research_cummings_divine_2006]\] \[[Florendo et al 2006][research_florendo_yechout_2006]\] \[[Maruyama et al 2006][research_maruyama_matsushima_2006]\] \[[Venukumar et al 2006][research_venukumar_jagadeesh_2006]\] \[[Florendo et al 2007][research_florendo_yechout_2007]\] \[[Goto et al 2007][research_goto_obayashi_2007]\] \[[Satheesh and Jagadeesh 2007][research_satheesh_jagadeesh_2007]\] \[[Mahapatra et al 2008][research_mahapatra_sriram_2008]\] \[[Schuelein 2008][research_schuelein_2008]\] \[[Ahlborn et al 2009][research_ahlborn_blake_2009]\] \[[Sasoh et al 2009][research_sasoh_sekiya_2009]\] \[[Satheesh and Jagadeesh 2009][research_satheesh_jagadeesh_2009]\] \[[Schülein 2009][research_schulein_2009]\] \[[Srinath and Reddy 2010][research_srinath_reddy_2010]\] \[[Nesteruk and Cartwright 2011][research_nesteruk_cartwright_2011]\] \[[Aruna and Devi 2012][research_aruna_devi_2012]\] \[[Dahan et al 2012][research_dahan_morgans_2012]\] \[[Mironov and Serdyuk 2012][research_mironov_serdyuk_2012]\] \[[Sahai et al 2014][research_sahai_john_2014]\] \[[Choi et al 2015][research_choi_lee_2015]\] \[[Schuelein 2015][research_schuelein_2015]\] \[[Wilder, Michael C. et al 2015][research_wildermichaelc_redadanielc_2015]\] \[[Zishka and Agarwal 2015][research_zishka_agarwal_2015]\] \[[Ageev and Pavlenko 2016][research_ageev_pavlenko_2016]\] \[[Huang et al 2016][research_huang_gardner_2016]\] \[[Huang et al 2017][research_huang_zhao_2017]\] \[[Magier and Merda 2017][research_magier_merda_2017]\] \[[Seager and Agarwal 2017][research_seager_agarwal_2017]\] \[[Yadav et al 2018][research_yadav_bodavula_2018]\] \[[Zhang et al 2018][research_zhang_huang_2018]\] \[[Alam and Pant 2019][research_alam_pant_2019]\] \[[Gardner and Agarwal 2019][research_gardner_agarwal_2019]\] \[[Han et al 2019][research_han_wang_2019]\] \[[Zhang et al 2019][research_zhang_huang_2019]\] \[[Huang and Yao 2020][research_huang_yao_2020]\] \[[Vozhdaev and Teperin 2020][research_vozhdaev_teperin_2020]\] \[[Goto et al 2021][research_goto_nakayama_2021]\] \[[Tekure et al 2021][research_tekure_pophali_2021]\] \[[Wang et al 2021][research_wang_yang_2021]\] \[[Mazurov and Takovitskii 2022][research_mazurov_takovitskii_2022]\] \[[Mokin et al 2022][research_mokin_kalashnikov_2022]\] \[[Stack 2022][research_stack_2022]\] \[[Easwer et al 2023][research_easwer_manideep_2023]\] \[[Pokela et al 2023][research_pokela_gustavsson_2023]\] \[[Rao et al 2023][research_rao_abhinav_2023]\] \[[Sahbon et al 2023][research_sahbon_michalow_2023]\] \[[Wang et al 2023][research_wang_fang_2023]\] \[[Balusamy et al 2024][research_balusamy_a_2024]\] \[[Kanwar 2024][research_kanwar_2024]\] \[[Ni and Fang 2024][research_ni_fang_2024_b]\] \[[Ni et al 2024][research_ni_fang_2024]\] \[[Popkov and Kornilov 2024][research_popkov_kornilov_2024]\] \[[Sanchez-Muñoz et al 2024][research_sanchezmunoz_lagarzacortes_2024]\] \[[Sarwar et al 2024][research_sarwar_rao_2024]\] \[[Camacho-Sánchez et al 2025][research_camachosanchez_loritediez_2025]\] \[[He et al 2025][research_he_pan_2025]\] \[[Sarwar et al 2025][research_sarwar_nizami_2025]\] \[[Camacho-Sánchez et al 2026][research_camachosanchez_loritediez_2026]\] \[[Du Plessis 2026][research_duplessis_2026]\] \[[He et al 2026][research_he_pan_2026]\] \[[Kim 2026][research_kim_2026]\] \[[Yavuz and Cihan 2026][research_yavuz_cihan_2026]\] \[[Zeidan][research_zeidan]\]

### The ascent, and where the dynamic pressure goes

**165 records.** \[[Eujen, E 1942][research_eujene_1942]\] \[[Air Force Test Pilot School Edwards Afb Ca 1962][research_airforcetestpilotschooledwardsafbca_1962]\] \[[Stancil 1963][research_stancil_1963]\] \[[Dembrow, D. W. and Jamieson, L. B. 1964][research_dembrowdw_jamiesonlb_1964]\] \[[Hillsley and Robbins 1964][research_hillsley_robbins_1964]\] \[[Stancil 1964][research_stancil_1964]\] \[[J A Sterhardt 1965][research_jasterhardt_1965]\] \[[Giacconi, R. et al 1967][research_giacconir_gorensteinp_1967]\] \[[Nicolaides et al 1967][research_nicolaides_eikenberry_1967]\] \[[Reis and Sundberg 1967][research_reis_sundberg_1967]\] \[[Sounding rocket flight of 1967][research_sounding_rocket_1967]\] \[[Crutcher, H. L. and Guttman, N. B. 1969][research_crutcherhl_guttmannb_1969]\] \[[Pierman, B. C. 1969][research_piermanbc_1969]\] \[[de Mendonça et al 1969][research_demendonca_sobral_1969]\] \[[Gabris, E. A. et al 1970][research_gabrisea_hansenqm_1970]\] \[[Belleville, R. E. and Lange, K. O. 1971][research_bellevillere_langeko_1971]\] \[[Demas, L. J. and Kinsley, R. L. 1971][research_demaslj_kinsleyrl_1971]\] \[[Grassl, H. J. 1971][research_grasslhj_1971]\] \[[Pincus, B. R. et al 1971][research_pincusbr_stephensonjs_1971]\] \[[Mcintosh et al 1972][research_mcintosh_knowles_1972]\] \[[Wolff, J. J., Jr. and Fitz, J. F. 1972][research_wolffjjjr_fitzjf_1972]\] \[[Bensimon 1973][research_bensimon_1973]\] \[[Loesch and Pawlowski 1973][research_loesch_pawlowski_1973]\] \[[Mcgarvey 1973][research_mcgarvey_1973]\] \[[Needleman and Tackett 1973][research_needleman_tackett_1973]\] \[[Timothy, J. G. 1973][research_timothyjg_1973]\] \[[Edge and Powers 1974][research_edge_powers_1974]\] \[[Code, A. D. 1975][research_codead_1975]\] \[[Handbook for space processing 1975][research_handbook_for_1975]\] \[[Lange, K. O. et al 1975][research_langeko_bellevillere_1975]\] \[[Spradley, L. W. 1975][research_spradleylw_1975]\] \[[Edge and Powers 1976][research_edge_powers_1976]\] \[[Matsumoto, T. et al 1976][research_matsumotot_chiseldm_1976]\] \[[Rochefort and Yorra 1976][research_rochefort_yorra_1976]\] \[[Charron et al 1978][research_charron_campbell_1978]\] \[[Morin 1978][research_morin_1978]\] \[[Ahlborn and Loehberg 1979][research_ahlborn_loehberg_1979]\] \[[Andersson and Forsell 1979][research_andersson_forsell_1979]\] \[[Chinn et al 1979][research_chinn_dekany_1979]\] \[[Cohen, H. A. et al 1979][research_cohenha_shermanc_1979]\] \[[Euler, E. A. et al 1979][research_eulerea_adamsgl_1979]\] \[[Mcanally and Engel 1979][research_mcanally_engel_1979]\] \[[Mcgarvey 1979][research_mcgarvey_1979]\] \[[Stouffer 1979][research_stouffer_1979]\] \[[Windsor 1979][research_windsor_1979]\] \[[Delvaille, J. P. 1981][research_delvaillejp_1981]\] \[[Fabrication of X-ray telescopes 1981][research_fabrication_of_1981]\] \[[Bartoe 1982][research_bartoe_1982]\] \[[Chun 1983][research_chun_1983]\] \[[Glaab, J. A. 1985][research_glaabja_1985]\] \[[Golub, L. 1985][research_golubl_1985]\] \[[Hills 1985][research_hills_1985]\] \[[Beyma 1986][research_beyma_1986]\] \[[Buchanan, R. P. 1986][research_buchananrp_1986]\] \[[Flores, Jr. 1986][research_floresjr_1986]\] \[[Ward, P. R. 1986][research_wardpr_1986]\] \[[Williams 1986][research_williams_1986]\] \[[Golub, Leon 1987][research_golubleon_1987]\] \[[Bruner, Marilyn E. et al 1989][research_brunermarilyne_brownwilliama_1989]\] \[[Golub, Leon 1989][research_golubleon_1989]\] \[[Well 1989][research_well_1989]\] \[[Wessling, Francis C. and Maybee, George W. 1989][research_wesslingfrancisc_maybeegeorgew_1989]\] \[[Herrick, W. D. et al 1990][research_herrickwd_penegorgt_1990]\] \[[McKenna 1990][research_mckenna_1990]\] \[[Smith et al 1990][research_smith_adelfang_1990]\] \[[Woods, Thomas N. and Rottman, Gary J. 1990][research_woodsthomasn_rottmangaryj_1990]\] \[[Nemzek, R. J. and Winckler, J. R. 1991][research_nemzekrj_wincklerjr_1991]\] \[[Nemzek, R. J. and Winckler, J. R. 1991][research_nemzekrj_wincklerjr_1991_b]\] \[[Rochefort et al 1991][research_rochefort_oconnor_1991]\] \[[Monti et al 1992][research_monti_fortezza_1992]\] \[[Lyons, J. T. 1993][research_lyonsjt_1993]\] \[[Balach, Dean 1995][research_balachdean_1995]\] \[[Lydon and Va 1995][research_lydon_va_1995]\] \[[Slater, David C. et al 1995][research_slaterdavidc_sternsalan_1995]\] \[[Golub, Leon 1996][research_golubleon_1996]\] \[[Sachs et al 1996][research_sachs_mehlhorn_1996]\] \[[Stern, Alan S. 1996][research_sternalans_1996]\] \[[Golub, Leon 1997][research_golubleon_1997]\] \[[Kintner, P. M. et al 1997][research_kintnerpm_arnoldyr_1997]\] \[[Basciano 1998][research_basciano_1998]\] \[[Golub, Leon 1998][research_golubleon_1998]\] \[[Olds and Budianto 1998][research_olds_budianto_1998]\] \[[Blum et al 1999][research_blum_wurm_1999]\] \[[CODAG sounding rocket experiment 1999][research_codag_sounding_1999]\] \[[Calise et al 2000][research_calise_tandon_2000]\] \[[Gath et al 2000][research_gath_well_2000]\] \[[Kim, Jungho et al 2000][research_kimjungho_bentonjohn_2000]\] \[[Thomas, Roger J. et al 2001][research_thomasrogerj_kankelborgcharlesc_2001]\] \[[Brinton, John and Golub, Leon 2004][research_brintonjohn_golubleon_2004]\] \[[Krause and Blum 2004][research_krause_blum_2004]\] \[[Gowan 2005][research_gowan_2005]\] \[[Nakasuka et al 2006][research_nakasuka_funase_2006]\] \[[Starnone and Biesbroek 2006][research_starnone_biesbroek_2006]\] \[[Summerer et al 2006][research_summerer_putz_2006]\] \[[Fuhrmann and Dreyer 2008][research_fuhrmann_dreyer_2008]\] \[[Berman, Joshua et al 2009][research_bermanjoshua_dudamichael_2009]\] \[[Stillwater, Ryan A. 2009][research_stillwaterryana_2009]\] \[[Zeeshan et al 2009][research_zeeshan_waheed_2009]\] \[[Kannengieser et al 2010][research_kannengieser_colin_2010]\] \[[Murillo and Lu 2010][research_murillo_lu_2010]\] \[[Galeazzi, M. et al 2012][research_galeazzim_colliermr_2012]\] \[[Guo et al 2012][research_guo_zhu_2012]\] \[[Lazzarin et al 2012][research_lazzarin_bellomo_2012]\] \[[Pescetelli et al 2012][research_pescetelli_minisci_2012]\] \[[Guo and Zhu 2013][research_guo_zhu_2013]\] \[[Lu and Wang 2013][research_lu_wang_2013]\] \[[M E Eckart et al 2013][research_meeckart_jsadams_2013]\] \[[Shi et al 2013][research_shi_jing_2013]\] \[[Shi et al 2013][research_shi_jing_2013_b]\] \[[Iguchi and Matsuoka 2014][research_iguchi_matsuoka_2014]\] \[[Kubo, M. et al 2014][research_kubom_kanor_2014]\] \[[Qiuhong et al 2014][research_qiuhong_zhaoying_2014]\] \[[Holt, James B. et al 2015][research_holtjamesb_deespatrickd_2015]\] \[[Narukage, Noriyuki et al 2015][research_narukagenoriyuki_kanoryohei_2015]\] \[[Song and Su 2015][research_song_su_2015]\] \[[Wang 2015][research_wang_2015]\] \[[Wu et al 2015][research_wu_liu_2015]\] \[[Barbosa et al 2016][research_barbosa_silva_2016]\] \[[Mao et al 2016][research_mao_sinn_2016]\] \[[Mao et al 2016][research_mao_sinn_2016_b]\] \[[Cheng et al 2017][research_cheng_li_2017]\] \[[Hergert et al 2017][research_hergert_brock_2017]\] \[[Hergert, Jakob D. et al 2017][research_hergertjakobd_brockjosephm_2017]\] \[[Li et al 2017][research_li_wu_2017]\] \[[Smith, B. P. and Dutta, S. 2017][research_smithbp_duttas_2017]\] \[[Wercinski, Paul et al 2017][research_wercinskipaul_smithb_2017]\] \[[He et al 2018][research_he_li_2018]\] \[[Ishikawa, R. et al 2018][research_ishikawar_kanor_2018]\] \[[Karlgaard et al 2018][research_karlgaard_tynis_2018]\] \[[Zhengxiang et al 2018][research_zhengxiang_tao_2018]\] \[[Cassell et al 2019][research_cassell_wercinski_2019]\] \[[Cassell, Alan et al 2019][research_cassellalan_wercinskipaul_2019]\] \[[Fu et al 2019][research_fu_wang_2019]\] \[[Ishikawa, Ryohko et al 2019][research_ishikawaryohko_mckenziedavid_2019]\] \[[Karlgaard et al 2019][research_karlgaard_tynis_2019]\] \[[Mukundan et al 2019][research_mukundan_maity_2019]\] \[[Rodi et al 2019][research_rodi_stoldt_2019]\] \[[Tynis et al 2019][research_tynis_karlgaard_2019]\] \[[Akbari and Pfaff 2020][research_akbari_pfaff_2020]\] \[[Dąbrowski et al 2020][research_dabrowski_pelzner_2020]\] \[[He et al 2020][research_he_liu_2020]\] \[[J. S. Adams et al 2020][research_jsadams_ajanderson_2020]\] \[[Zheng et al 2020][research_zheng_fu_2020]\] \[[Hu et al 2021][research_hu_bai_2021]\] \[[Marchetti et al 2021][research_marchetti_minisci_2021]\] \[[Ascent Trajectory Analysis and 2022][research_ascent_trajectory_2022]\] \[[Deng et al 2022][research_deng_xu_2022]\] \[[Lan and Li 2022][research_lan_li_2022]\] \[[Ma et al 2022][research_ma_pan_2022]\] \[[Nair and Vaidyanathan 2022][research_nair_vaidyanathan_2022]\] \[[Gilson et al 2023][research_gilson_a_2023]\] \[[Zhang et al 2023][research_zhang_yang_2023]\] \[[Siewert et al 2024][research_siewert_borgzinner_2024]\] \[[Benedikter et al 2025][research_benedikter_dambrosio_2025]\] \[[Michael Zemcov et al 2025][research_michaelzemcov_jamesjbock_2025]\] \[[Xue et al 2025][research_xue_xie_2025]\] \[[Zhao et al 2025][research_zhao_pan_2025]\] \[[Lei et al 2026][research_lei_chen_2026]\] \[[Taki et al 2026][research_taki_sergienko_2026]\] \[[Murillo][research_murillo]\] \[[P S Athiray et al][research_psathiray_amywinebarger]\] \[[P. S. Athiray et al][research_psathiray_amywinebarger_b]\] \[[Patrick Champey][research_patrickchampey]\] \[[R Ishikawa et al][research_rishikawa_tokamoto]\] \[[Ryohko Ishikawa et al][research_ryohkoishikawa_songdonguk]\]

### The nozzle this vehicle carries, which the previous article took

**294 records.** \[[Salmi, R J and Cortright, E M, Jr 1956][research_salmirj_cortrightemjr_1956]\] \[[Salmi, Reino J 1956][research_salmireinoj_1956]\] \[[Mercer, C. E. and Salters, L. B., Jr. 1963][research_mercerce_salterslbjr_1963]\] \[[Lee, C. C. 1966][research_leecc_1966]\] \[[Berrier, B. L. and Mercer, C. E. 1967][research_berrierbl_mercerce_1967]\] \[[Bresnahan, D. L. 1968][research_bresnahandl_1968]\] \[[Bresnahan, D. L. and Johns, A. L. 1968][research_bresnahandl_johnsal_1968]\] \[[Harrington, D. E. and Wasko, R. A. 1968][research_harringtonde_waskora_1968]\] \[[Berrier, B. L. 1969][research_berrierbl_1969]\] \[[Bresnahan, D. L. 1969][research_bresnahandl_1969]\] \[[Cikanek, H. A., Jr. et al 1969][research_cikanekhajr_mcgowenjjiii_1969]\] \[[Huntley, S. C. and Samanich, N. E. 1969][research_huntleysc_samanichne_1969]\] \[[Johns, A. L. 1969][research_johnsal_1969]\] \[[Berrier, B. L. and Mercer, C. E. 1970][research_berrierbl_mercerce_1970]\] \[[Burley, R. R. and Samanich, N. E. 1970][research_burleyrr_samanichne_1970]\] \[[Chenoweth, F. C. and Jeracki, R. J. 1970][research_chenowethfc_jerackirj_1970]\] \[[Clark, J. S. et al 1970][research_clarkjs_graberej_1970]\] \[[Harrington, D. E. 1970][research_harringtonde_1970]\] \[[Harrington, D. E. 1970][research_harringtonde_1970_b]\] \[[Steffen, F. W. 1970][research_steffenfw_1970]\] \[[Chambellan, R. E. and Stepka, F. S. 1971][research_chambellanre_stepkafs_1971]\] \[[Chamberlin, R. and Samanich, N. E. 1971][research_chamberlinr_samanichne_1971]\] \[[Chenoweth, F. C. and Lieberman, A. 1971][research_chenowethfc_liebermana_1971]\] \[[Hall, C. R., Jr. and Mueller, T. J. 1971][research_hallcrjr_muellertj_1971]\] \[[Brausch, J. F. 1972][research_brauschjf_1972]\] \[[Bresnahan, D. L. 1972][research_bresnahandl_1972]\] \[[Clark, J. S. and Lieberman, A. 1972][research_clarkjs_liebermana_1972]\] \[[Graber, E. J., Jr. and Clark, J. S. 1972][research_graberejjr_clarkjs_1972]\] \[[Mueller, T. J. and Sule, W. P. 1972][research_muellertj_sulewp_1972]\] \[[Muller, T. J. et al 1972][research_mullertj_sulewp_1972]\] \[[Samanich, N. E. 1972][research_samanichne_1972]\] \[[Berrier, B. L. 1973][research_berrierbl_1973]\] \[[Chamberlin, R. 1973][research_chamberlinr_1973]\] \[[Mueller and Sule 1973][research_mueller_sule_1973]\] \[[Straight, D. M. and Harrington, D. E. 1973][research_straightdm_harringtonde_1973]\] \[[Burley, R. R. and Head, V. L. 1974][research_burleyrr_headvl_1974]\] \[[Burley, R. R. and Johns, A. L. 1974][research_burleyrr_johnsal_1974]\] \[[Harrington, D. E. and Schloemer, J. J. 1974][research_harringtonde_schloemerjj_1974]\] \[[Harrington, D. E. et al 1974][research_harringtonde_noseksm_1974]\] \[[Huang 1974][research_huang_1974]\] \[[Giel, T. V., Jr. and Mueller, T. J. 1975][research_gieltvjr_muellertj_1975]\] \[[Harrington, D. E. et al 1975][research_harringtonde_schloemerjj_1975]\] \[[Galanga, F. L. and Mueller, T. J. 1976][research_galangafl_muellertj_1976]\] \[[Harrington, D. E. et al 1976][research_harringtonde_schloemerjj_1976]\] \[[Lee, R. 1976][research_leer_1976]\] \[[Nosek, S. M. and Straight, D. M. 1976][research_noseksm_straightdm_1976]\] \[[Diem, H. G. and Kirby, F. M. 1977][research_diemhg_kirbyfm_1977]\] \[[Kirby and Martinez 1977][research_kirby_martinez_1977]\] \[[Maestrello, L. 1978][research_maestrellol_1978]\] \[[Staid, P. S. 1978][research_staidps_1978]\] \[[Bhutiani, P. K. 1980][research_bhutianipk_1980]\] \[[Knott, P. R. et al 1980][research_knottpr_brauschjf_1980]\] \[[Bauer, A. B. 1981][research_bauerab_1981]\] \[[Knott, P. R. et al 1981][research_knottpr_blozyjt_1981]\] \[[Knott, P. R. et al 1981][research_knottpr_janardanba_1981]\] \[[Vdoviak, J. W. et al 1981][research_vdoviakjw_knottpr_1981]\] \[[Bauer, A. B. et al 1982][research_bauerab_kibensv_1982]\] \[[Dosanjh, D. S. et al 1983][research_dosanjhds_dasi_1983]\] \[[Knott, P. R. et al 1984][research_knottpr_janardanba_1984]\] \[[Dosanjh, D. S. and Das, I. S. 1985][research_dosanjhds_dasis_1985]\] \[[Janardan, B. A. et al 1985][research_janardanba_majjigirk_1985]\] \[[Mercer, C. E. and Burley, J. R., II 1985][research_mercerce_burleyjrii_1985]\] \[[Dosanjh, D. S. and Das, I. S. 1986][research_dosanjhds_dasis_1986]\] \[[Dosanjh, Darshan S. and Das, Indu S. 1987][research_dosanjhdarshans_dasindus_1987]\] \[[Dosanjh, Darshan S. and Das, Indu S. 1988][research_dosanjhdarshans_dasindus_1988]\] \[[Murthy, S. N. B. and Sheu, W. H. 1988][research_murthysnb_sheuwh_1988]\] \[[Aukerman, Carl A. 1991][research_aukermancarla_1991]\] \[[Das, I. S. and Dosanjh, D. S. 1991][research_dasis_dosanjhds_1991]\] \[[Cler, Daniel L. et al 1993][research_clerdaniell_masonmaryl_1993]\] \[[Quentmeyer, Richard J. and Roncace, Elizabeth A. 1993][research_quentmeyerrichardj_roncaceelizabetha_1993]\] \[[Das, Indu S. et al 1996][research_dasindus_khavaranabbas_1996]\] \[[Dunn, Stuart S. and Coats, Douglas E. 1996][research_dunnstuarts_coatsdouglase_1996]\] \[[Khavaran, A. et al 1996][research_khavarana_dasap_1996]\] \[[Moes et al 1996][research_moes_cobleigh_1996]\] \[[Fick et al 1997][research_fick_schmucker_1997]\] \[[Korte et al 1997][research_korte_salas_1997]\] \[[Korte, J. J. et al 1997][research_kortejj_salasao_1997]\] \[[Ruf et al 1997][research_ruf_mcconaughey_1997]\] \[[Bouslog, S. et al 1998][research_bouslogs_mammanoj_1998]\] \[[Cobleigh, Brent R. 1998][research_cobleighbrentr_1998]\] \[[Dale A Mackall et al 1998][research_daleamackall_robertsakahara_1998]\] \[[Dukeman, Gregory A. and Gallaher, Michael W. 1998][research_dukemangregorya_gallahermichaelw_1998]\] \[[Hall, Charles E. et al 1998][research_hallcharlese_gallahermichaelw_1998]\] \[[Jackson, Jerry E. et al 1998][research_jacksonjerrye_espenschiederich_1998]\] \[[Kumakawa et al 1998][research_kumakawa_onodera_1998]\] \[[Mackall, D. et al 1998][research_mackalld_sakaharar_1998]\] \[[Mizukami, Masashi et al 1998][research_mizukamimasashi_corpeninggriffinp_1998]\] \[[Moes et al 1998][research_moes_cobleigh_1998]\] \[[Simpson, Timothy W. 1998][research_simpsontimothyw_1998]\] \[[Stephen Corda et al 1998][research_stephencorda_bradfordaneal_1998]\] \[[Vinson, John 1998][research_vinsonjohn_1998]\] \[[Wang, Ten-See 1998][research_wangtensee_1998]\] \[[Wang, Ten-See 1998][research_wangtensee_1998_b]\] \[[Aguilar, Robert 1999][research_aguilarrobert_1999]\] \[[Austin, Robert E. and Rising, Jerry J. 1999][research_austinroberte_risingjerryj_1999]\] \[[Barret, Chris 1999][research_barretchris_1999]\] \[[Crowley, Tim 1999][research_crowleytim_1999]\] \[[Ennix, Kimberly A. et al 1999][research_ennixkimberlya_corpeninggriffinp_1999]\] \[[Hall, Charles E. and Panossian, Hagop V. 1999][research_hallcharlese_panossianhagopv_1999]\] \[[Hass, Neal et al 1999][research_hassneal_mizukamimasashi_1999]\] \[[Holmes, Richard et al 1999][research_holmesrichard_ellisdavid_1999]\] \[[Larson, Richard R. 1999][research_larsonrichardr_1999]\] \[[Liou, Larry C. 1999][research_lioularryc_1999]\] \[[Littlefield, Alan C. and Melton, Gregory S. 1999][research_littlefieldalanc_meltongregorys_1999]\] \[[Murphy, Kelly J. et al 1999][research_murphykellyj_nowakrobertj_1999]\] \[[Murphy, Terry 1999][research_murphyterry_1999]\] \[[Prabhu, Ramadas K. 1999][research_prabhuramadask_1999]\] \[[Reichenfeld, Curtis J. and Jones, Paul G. 1999][research_reichenfeldcurtisj_jonespaulg_1999]\] \[[Sakamoto et al 1999][research_sakamoto_takahashi_1999]\] \[[Tomita et al 1999][research_tomita_takahashi_1999]\] \[[Whitmore, Stephen A. and Moes, Timothy R. 1999][research_whitmorestephena_moestimothyr_1999]\] \[[X-33/RLV Program Aerospike Engines 1999][research_x_33_rlv_program_1999]\] \[[Austin, Robert E. and Rising, Jerry J. 2000][research_austinroberte_risingjerryj_2000]\] \[[Elam, S. K. 2000][research_elamsk_2000]\] \[[Korte 2000][research_korte_2000]\] \[[Littlefield, Alan C. and Melton, Gregory S. 2000][research_littlefieldalanc_meltongregorys_2000]\] \[[Meyer, Claudia M. 2000][research_meyerclaudiam_2000]\] \[[Miller, C. G. 2000][research_millercg_2000]\] \[[Shtessel, Yuri B. and Hall, Charles E. 2000][research_shtesselyurib_hallcharlese_2000]\] \[[Soni, Bharat 2000][research_sonibharat_2000]\] \[[Zhao et al 2000][research_zhao_mo_2000]\] \[[Zhu et al 2000][research_zhu_banker_2000]\] \[[DAgostino, Mark et al 2001][research_dagostinomark_leeyoungc_2001]\] \[[Ito and Fujii 2001][research_ito_fujii_2001]\] \[[Korte et al 2001][research_korte_salas_2001]\] \[[Liu et al 2001][research_liu_zhang_2001]\] \[[Rieckhoff, T. J. et al 2001][research_rieckhofftj_covanma_2001]\] \[[Schweikhard, Keith A. et al 2001][research_schweikhardkeitha_richardswlance_2001]\] \[[Tomita et al 2001][research_tomita_takahashi_2001]\] \[[Wang, Ten-See et al 2001][research_wangtensee_williamsrobert_2001]\] \[[Wuye et al 2001][research_wuye_yu_2001]\] \[[Ito and Fujii 2002][research_ito_fujii_2002]\] \[[Ruf, J. H. and McDaniels, D. M. 2002][research_rufjh_mcdanielsdm_2002]\] \[[Ito and Fujii 2003][research_ito_fujii_2003]\] \[[Ito and Fujii 2003][research_ito_fujii_2003_b]\] \[[Ruf, J. H. et al 2003][research_rufjh_hagemanng_2003]\] \[[Ruf, Joseph H. and McDaniels, David M. 2003][research_rufjosephh_mcdanielsdavidm_2003]\] \[[Wang, Tee-See et al 2003][research_wangteesee_droegealan_2003]\] \[[Wang, Ten-See et al 2003][research_wangtensee_droegealan_2003]\] \[[Rogers, Rayna C. 2004][research_rogersraynac_2004]\] \[[Wang, Ten-See et al 2004][research_wangtensee_droegealan_2004]\] \[[Aso and Sugimoto 2005][research_aso_sugimoto_2005]\] \[[Bui et al 2005][research_bui_murray_2005]\] \[[Ruf, Joseph H. and McDaniels, David M. 2005][research_rufjosephh_mcdanielsdavidm_2005]\] \[[Tsukada et al 2005][research_tsukada_fujimoto_2005]\] \[[Tsutsumi et al 2005][research_tsutsumi_teramoto_2005]\] \[[Taniguchi et al 2006][research_taniguchi_mori_2006]\] \[[Wang et al 2006][research_wang_liu_2006]\] \[[Tsutsumi et al 2007][research_tsutsumi_yamaguchi_2007]\] \[[Wang et al 2007][research_wang_qin_2007]\] \[[Zilic et al 2007][research_zilic_hitt_2007]\] \[[Tomita et al 2008][research_tomita_moriya_2008]\] \[[Verma 2008][research_verma_2008]\] \[[Karthikeyan et al 2009][research_karthikeyan_verma_2009]\] \[[Verma 2009][research_verma_2009]\] \[[Wang et al 2009][research_wang_liu_2009]\] \[[Wilson et al 2009][research_wilson_clark_2009]\] \[[Dennis et al 2010][research_dennis_hernandez_2010]\] \[[Eilers et al 2010][research_eilers_matthew_2010]\] \[[Ladeinde and Chen 2010][research_ladeinde_chen_2010]\] \[[Shark et al 2010][research_shark_dennis_2010]\] \[[Eilers et al 2011][research_eilers_wilson_2011]\] \[[Grieb et al 2011][research_grieb_lemieux_2011]\] \[[Hall et al 2011][research_hall_hartsfield_2011]\] \[[Noori and Shahrokhi 2011][research_noori_shahrokhi_2011]\] \[[Simmons and Branam 2011][research_simmons_branam_2011]\] \[[Eilers et al 2012][research_eilers_wilson_2012]\] \[[Narimiya et al 2012][research_narimiya_tsuboi_2012]\] \[[Rajesh et al 2012][research_rajesh_kumar_2012]\] \[[Design and FLOW Simulation 2014][research_design_and_flow_2014]\] \[[Donbosco and Kumar 2014][research_donbosco_kumar_2014]\] \[[Peugeot, John et al 2014][research_peugeotjohn_garciachance_2014]\] \[[Shibao et al 2014][research_shibao_tsuboi_2014]\] \[[Bogoi et al 2015][research_bogoi_rugescu_2015]\] \[[He et al 2015][research_he_qin_2015]\] \[[Heath, Christopher M. et al 2015][research_heathchristopherm_grayjustins_2015]\] \[[Lash and Moeller 2015][research_lash_moeller_2015]\] \[[Karthikeyan et al 2016][research_karthikeyan_aravindhkumar_2016]\] \[[Menon 2016][research_menon_2016]\] \[[Bach 2017][research_bach_2017]\] \[[Chaudhari 2017][research_chaudhari_2017]\] \[[Kumar et al 2017][research_kumar_gopalsamy_2017]\] \[[Mason-Smith 2017][research_masonsmith_2017]\] \[[Nair et al 2017][research_nair_suryan_2017]\] \[[Performance Optimization of Aerospike 2017][research_performance_optimization_2017]\] \[[Purohit and Mathpal 2017][research_purohit_mathpal_2017]\] \[[Reza and Arora 2017][research_reza_arora_2017]\] \[[T and Cm 2017][research_t_cm_2017]\] \[[Lai et al 2018][research_lai_wei_2018]\] \[[Masdari et al 2018][research_masdari_tahani_2018]\] \[[Schnabel and Brophy 2018][research_schnabel_brophy_2018]\] \[[Schwer et al 2018][research_schwer_brophy_2018]\] \[[Tsuboi et al 2018][research_tsuboi_jourdaine_2018]\] \[[Fotia et al 2019][research_fotia_kaemming_2019]\] \[[Ha et al 2019][research_ha_kim_2019]\] \[[Harroun et al 2019][research_harroun_heister_2019]\] \[[Jourdaine et al 2019][research_jourdaine_tsuboi_2019]\] \[[Sieder et al 2019][research_sieder_propst_2019]\] \[[Ferlauto et al 2020][research_ferlauto_ferrero_2020]\] \[[Ferlauto et al 2020][research_ferlauto_ferrero_2020_b]\] \[[Heath and Bell 2020][research_heath_bell_2020]\] \[[Kurita et al 2020][research_kurita_jourdaine_2020]\] \[[Shenoy et al 2020][research_shenoy_sreekumar_2020]\] \[[Stephen A 2020][research_stephena_2020]\] \[[Stewart et al 2020][research_stewart_papadopoulos_2020]\] \[[Tian et al 2020][research_tian_guo_2020]\] \[[Udaiyakumar et al 2020][research_udaiyakumar_iyer_2020]\] \[[B et al 2021][research_b_kasher_2021]\] \[[Balaji et al 2021][research_balaji_navinkumar_2021]\] \[[Dakka and Dennison 2021][research_dakka_dennison_2021]\] \[[Et. al. 2021][research_etal_2021]\] \[[Ghosh and Gunasekaran 2021][research_ghosh_gunasekaran_2021]\] \[[Huang et al 2021][research_huang_xia_2021]\] \[[Kumar Mishra et al 2021][research_kumarmishra_goswami_2021]\] \[[Lengade 2021][research_lengade_2021]\] \[[Naseh and Alipoor 2021][research_naseh_alipoor_2021]\] \[[Sankari Ashok Alshiya et al 2021][research_sankariashokalshiya_santhosh_2021]\] \[[Senthilkumar et al 2021][research_senthilkumar_mudholkar_2021]\] \[[Sequeira and Sanjay 2021][research_sequeira_sanjay_2021]\] \[[Ha and Kim 2022][research_ha_kim_2022]\] \[[Jain and Kumar 2022][research_jain_kumar_2022]\] \[[Liu et al 2022][research_liu_cheng_2022]\] \[[Sriganapathy et al 2022][research_sriganapathy_arjunkumara_2022]\] \[[Aithani et al 2023][research_aithani_shahid_2023]\] \[[Di Cicca et al 2023][research_dicicca_hassan_2023]\] \[[Khairul BMQ Zaman and Amy F Fagan 2023][research_khairulbmqzaman_amyffagan_2023]\] \[[Ma et al 2023][research_ma_bao_2023]\] \[[Nagaral et al 2023][research_nagaral_r_2023]\] \[[Pyle et al 2023][research_pyle_jacobs_2023]\] \[[Sundaria et al 2023][research_sundaria_bhagat_2023]\] \[[Sundaria et al 2023][research_sundaria_bhagat_2023_b]\] \[[A et al 2024][research_a_sampathkumar_2024]\] \[[Amy F Fagan et al 2024][research_amyffagan_khairulbmqzaman_2024]\] \[[Bayir and Akbıyık 2024][research_bayir_akbiyik_2024]\] \[[Bindal et al 2024][research_bindal_joshi_2024]\] \[[Bindal et al 2024][research_bindal_kattyayan_2024]\] \[[Di Cicca et al 2024][research_dicicca_marsilio_2024]\] \[[Golliard and Mihaescu 2024][research_golliard_mihaescu_2024]\] \[[Golliard and Mihaescu 2024][research_golliard_mihaescu_2024_b]\] \[[Golliard and Mihaescu 2024][research_golliard_mihaescu_2024_c]\] \[[Khairul B M Q Zaman et al 2024][research_khairulbmqzaman_amyffagan_2024]\] \[[Langner et al 2024][research_langner_gupta_2024]\] \[[Marsilio et al 2024][research_marsilio_resta_2024]\] \[[Paramo and Arizpe 2024][research_paramo_arizpe_2024]\] \[[Peshkov and Tret'yakov 2024][research_peshkov_tretyakov_2024]\] \[[Resta et al 2024][research_resta_dicicca_2024]\] \[[Reza et al 2024][research_reza_agarwal_2024]\] \[[Scwartz et al 2024][research_scwartz_krishnan_2024]\] \[[Silva and Brójo 2024][research_silva_brojo_2024]\] \[[Strobel and Macneil 2024][research_strobel_macneil_2024]\] \[[Swathish and Rakesh 2024][research_swathish_rakesh_2024]\] \[[Bodra and Khairnar 2025][research_bodra_khairnar_2025]\] \[[Golliard and Mihaescu 2025][research_golliard_mihaescu_2025]\] \[[Golliard and Mihaescu 2025][research_golliard_mihaescu_2025_b]\] \[[Hu 2025][research_hu_2025]\] \[[Inturi et al 2025][research_inturi_lovaraju_2025]\] \[[John Henry Korth et al 2025][research_johnhenrykorth_jonathanmburt_2025]\] \[[Khairul B M Q Zaman et al 2025][research_khairulbmqzaman_johnhkorth_2025]\] \[[Liu et al 2025][research_liu_zhang_2025]\] \[[Liu et al 2025][research_liu_liu_2025]\] \[[M et al 2025][research_m_ka_2025]\] \[[Mukesh Reddy Dhanagari 2025][research_mukeshreddydhanagari_2025]\] \[[Rafi and Al-Faruk 2025][research_rafi_alfaruk_2025]\] \[[Wang et al 2025][research_wang_niu_2025]\] \[[Alam et al 2026][research_alam_karim_2026]\] \[[Aslan et al 2026][research_aslan_kara_2026]\] \[[Bakker et al 2026][research_bakker_madhumitha_2026]\] \[[Golliard and Mihaescu 2026][research_golliard_mihaescu_2026]\] \[[Karim et al 2026][research_karim_some_2026]\] \[[Liu et al 2026][research_liu_guo_2026]\] \[[Liu et al 2026][research_liu_guo_2026_b]\] \[[Lizcano et al 2026][research_lizcano_martinez_2026]\] \[[Magnani et al 2026][research_magnani_sozio_2026]\] \[[Pyle and Jacobs 2026][research_pyle_jacobs_2026]\] \[[Pyle and Jacobs 2026][research_pyle_jacobs_2026_b]\] \[[Sen Ayush et al 2026][research_senayush_kaur_2026]\] \[[Steiner and Bauer 2026][research_steiner_bauer_2026]\] \[[Sun et al 2026][research_sun_sun_2026]\] \[[Wißmann et al 2026][research_wissmann_kahler_2026]\] \[[Aerospike engine][research_aerospike_engine]\] \[[Amy F Fagan and Khairul BMQ Zaman][research_amyffagan_khairulbmqzaman]\] \[[Amy F Fagan et al][research_amyffagan_khairulbmqzaman_b]\] \[[Beebe][research_beebe]\] \[[Brennen][research_brennen]\] \[[Brock][research_brock]\] \[[Case][research_case]\] \[[Grieb][research_grieb]\] \[[Imbaratto][research_imbaratto]\] \[[John Henry Korth][research_johnhenrykorth]\] \[[John Henry Korth et al][research_johnhenrykorth_jonathanmburt]\] \[[Khairul BMQ Zaman et al][research_khairulbmqzaman_johnhkorth]\] \[[Khairul Zaman et al][research_khairulzaman_amyfagan]\] \[[Shahrokhi and Noori][research_shahrokhi_noori]\] \[[Stewart][research_stewart]\]

### Segmented and modular vehicles, which is a subcontractor's trade

**9 records.** \[[Carpenter and Jeffus 1962][research_carpenter_jeffus_1962]\] \[[Carpenter and Jeffus 1963][research_carpenter_jeffus_1963]\] \[[Rice, W. J. and Birchenough, A. G. 1982][research_ricewj_birchenoughag_1982]\] \[[Binder, Michael and Felder, James L. 1993][research_bindermichael_felderjamesl_1993]\] \[[Tarrant and Crook 1996][research_tarrant_crook_1996]\] \[[Tarrant, Charlie and Crook, Jerry 1997][research_tarrantcharlie_crookjerry_1997]\] \[[Crook and Tarrant 1998][research_crook_tarrant_1998]\] \[[Szalkowski et al 2024][research_szalkowski_chrostowski_2024]\] \[[Tarrant and Crook][research_tarrant_crook]\]

### This vehicle, this team, and this programme's lineage

**1 records.** \[[Steele, W. G. et al 2005][research_steelewg_molderkj_2005]\]

### Monitoring a structure and detecting what hits it, the lead's own trade

**167 records.** \[[Teng 1970][research_teng_1970]\] \[[Weller 1982][research_weller_1982]\] \[[Lamb 1987][research_lamb_1987]\] \[[Rogowski, Robert S. 1990][research_rogowskiroberts_1990]\] \[[Ricles, James M. 1991][research_riclesjamesm_1991]\] \[[Chang 1998][research_chang_1998]\] \[[Chang 2000][research_chang_2000]\] \[[Masri 2000][research_masri_2000]\] \[[Balageas 2002][research_balageas_2002]\] \[[Chang 2002][research_chang_2002]\] \[[Mufti 2002][research_mufti_2002]\] \[[Giurgiutiu 2003][research_giurgiutiu_2003]\] \[[Prosser, William and Percy, Daniel 2003][research_prosserwilliam_percydaniel_2003]\] \[[Chang 2004][research_chang_2004]\] \[[Decker, Arthur J. 2004][research_deckerarthurj_2004]\] \[[Engberg, Robert and Ooi, Teng K. 2004][research_engbergrobert_ooitengk_2004]\] \[[Giurgiutiu and Lin 2004][research_giurgiutiu_lin_2004]\] \[[Prosser, William H. et al 2004][research_prosserwilliamh_gormanmichaelr_2004]\] \[[The Structural Health Monitoring 2004][research_the_structural_2004]\] \[[Blackshire et al 2005][research_blackshire_giurgiutiu_2005]\] \[[Coppotelli et al 2005][research_coppotelli_marzocca_2005]\] \[[Engberg, Robert C. 2005][research_engbergrobertc_2005]\] \[[Giurgiutiu and Zagrai 2005][research_giurgiutiu_zagrai_2005]\] \[[Lopes and Silva 2005][research_lopes_silva_2005]\] \[[Park and Inman 2005][research_park_inman_2005]\] \[[Raghavan and Cesnik 2005][research_raghavan_cesnik_2005]\] \[[The Structural Health Monitoring 2005][research_the_structural_2005]\] \[[Chattopadhyay 2006][research_chattopadhyay_2006]\] \[[Chronister and Palazotto 2006][research_chronister_palazotto_2006]\] \[[Udd 2006][research_udd_2006]\] \[[Allison, Sidney G. et al 2007][research_allisonsidneyg_prosserwilliamh_2007]\] \[[Dissanayake and Karunananda 2008][research_dissanayake_karunananda_2008]\] \[[Kulkarni and Achenbach 2008][research_kulkarni_achenbach_2008]\] \[[Spurný et al 2008][research_spurny_ploc_2008]\] \[[Structural Health Monitoring Person 2008][research_structural_health_2008]\] \[[Underwood et al 2008][research_underwood_swenson_2008]\] \[[Cesnik 2009][research_cesnik_2009]\] \[[Choi and Sweetman 2009][research_choi_sweetman_2009]\] \[[Kochergin et al 2009][research_kochergin_shi_2009]\] \[[Kral et al 2009][research_kral_horn_2009]\] \[[Liu 2009][research_liu_2009]\] \[[de Leeuw and Brennan 2009][research_deleeuw_brennan_2009]\] \[[Chiu 2010][research_chiu_2010]\] \[[Chiu et al 2010][research_chiu_chang_2010]\] \[[Diamanti and Soutis 2010][research_diamanti_soutis_2010]\] \[[Dragan 2010][research_dragan_2010]\] \[[Esterline et al 2010][research_esterline_wright_2010]\] \[[Giurgiutiu and Soutis 2010][research_giurgiutiu_soutis_2010]\] \[[Grandhi and Tobe 2010][research_grandhi_tobe_2010]\] \[[Haftka et al 2010][research_haftka_yuan_2010]\] \[[Park et al 2010][research_park_farrar_2010]\] \[[Staszewski and Sohn 2010][research_staszewski_sohn_2010]\] \[[Whitlow et al 2010][research_whitlow_sundaresan_2010]\] \[[Worden and Inman 2010][research_worden_inman_2010]\] \[[Yap, Keng C. 2010][research_yapkengc_2010]\] \[[Chang et al 2011][research_chang_markmiller_2011]\] \[[Lindgren et al 2011][research_lindgren_buynak_2011]\] \[[Russell, Richard et al 2011][research_russellrichard_washabaughandy_2011]\] \[[Sankararaman et al 2011][research_sankararaman_ling_2011]\] \[[Structural Health Monitoring OrientedModelling 2011][research_structural_health_2011]\] \[[Yap, Keng C. et al 2011][research_yapkengc_maciasjesus_2011]\] \[[Zagrai et al 2011][research_zagrai_barnes_2011]\] \[[Bentham Science Publisher 2012][research_benthamsciencepublisher_2012]\] \[[Chattopadhyay et al 2012][research_chattopadhyay_seaver_2012]\] \[[Ghoshal et al 2012][research_ghoshal_ayers_2012]\] \[[Han et al 2012][research_han_mateescu_2012]\] \[[Michaels et al 2012][research_michaels_michaels_2012]\] \[[Neerrukatti et al 2012][research_neerrukatti_liu_2012]\] \[[Nondestructive inspection and structural 2012][research_nondestructive_inspection_2012]\] \[[Seaver et al 2012][research_seaver_chattopadhyay_2012]\] \[[Zein-Sabatto et al 2012][research_zeinsabatto_mikhail_2012]\] \[[Foote 2013][research_foote_2013]\] \[[Giglio et al 2013][research_giglio_manes_2013]\] \[[Richards, W Lance et al 2013][research_richardswlance_madaraserici_2013]\] \[[Smart Technical Textiles for 2013][research_smart_technical_2013]\] \[[Sohn 2013][research_sohn_2013]\] \[[Veidt and Liew 2013][research_veidt_liew_2013]\] \[[Williams, Martha et al 2013][research_williamsmartha_lewismark_2013]\] \[[Richards, Lance et al 2014][research_richardslance_parkerallen_2014]\] \[[The Person of the 2014][research_the_person_2014]\] \[[Trends on research in 2014][research_trends_on_2014]\] \[[Borkowski 2015][research_borkowski_2015]\] \[[Giurgiutiu 2015][research_giurgiutiu_2015]\] \[[Golato et al 2015][research_golato_santhanam_2015]\] \[[Iglesias et al 2015][research_iglesias_haynes_2015]\] \[[Le and Yu 2015][research_le_yu_2015]\] \[[Ravi et al 2015][research_ravi_rathod_2015]\] \[[Ryu et al 2015][research_ryu_castano_2015]\] \[[Swindell 2015][research_swindell_2015]\] \[[Cramer, K. Elliott 2016][research_cramerkelliott_2016]\] \[[Derriso et al 2016][research_derriso_mccurry_2016]\] \[[Giurgiutiu 2016][research_giurgiutiu_2016]\] \[[Giurgiutiu 2016][research_giurgiutiu_2016_b]\] \[[Henderson et al 2016][research_henderson_mathews_2016]\] \[[Jha et al 2016][research_jha_sullivan_2016]\] \[[Kranz et al 2016][research_kranz_english_2016]\] \[[Okabe and Wu 2016][research_okabe_wu_2016]\] \[[Sihver et al 2016][research_sihver_kodaira_2016]\] \[[Structural Health Monitoring SHM 2016][research_structural_health_2016_b]\] \[[Structural Health Monitoring of 2016][research_structural_health_2016]\] \[[Yu and Tian 2016][research_yu_tian_2016]\] \[[De Simone et al 2017][research_desimone_ciampa_2017]\] \[[Moix-Bonet et al 2017][research_moixbonet_schmidt_2017]\] \[[Rébillat et al 2017][research_rebillat_hmad_2017]\] \[[Towler and Ryu 2017][research_towler_ryu_2017]\] \[[Cawley 2018][research_cawley_2018]\] \[[Dong and Kim 2018][research_dong_kim_2018]\] \[[Harris et al 2018][research_harris_dizaji_2018]\] \[[Schubert Kabban et al 2018][research_schubertkabban_uber_2018]\] \[[Hadjria and D'Almeida 2019][research_hadjria_dalmeida_2019]\] \[[Lewis, Mark E. et al 2019][research_lewismarke_gibsontracyl_2019]\] \[[Rahul et al 2019][research_rahul_alokita_2019]\] \[[Structural health monitoring SHM 2019][research_structural_health_2019]\] \[[Wan and Ni 2019][research_wan_ni_2019]\] \[[Bao and Li 2020][research_bao_li_2020]\] \[[Barthorpe and Worden 2020][research_barthorpe_worden_2020]\] \[[Giurgiutiu 2020][research_giurgiutiu_2020]\] \[[Lee 2020][research_lee_2020]\] \[[Structural Health Monitoring Damage 2021][research_structural_health_2021]\] \[[Broer et al 2022][research_broer_benedictus_2022]\] \[[Gardner et al 2022][research_gardner_bull_2022]\] \[[Giurgiutiu 2022][research_giurgiutiu_2022]\] \[[Sause and Jasiūnienė 2022][research_sause_jasiuniene_2022]\] \[[Yu et al 2022][research_yu_fan_2022]\] \[[Data-Centric Structural Health Monitoring 2023][research_data_centric_structural_2023]\] \[[Franz and Hassan 2023][research_franz_hassan_2023]\] \[[Gordan et al 2023][research_gordan_mccrum_2023]\] \[[Hassani and Dackermann 2023][research_hassani_dackermann_2023]\] \[[Sharif Khodaei and Aliabadi 2023][research_sharifkhodaei_aliabadi_2023]\] \[[Structural health monitoring SHM 2023][research_structural_health_2023]\] \[[Tiachacht et al 2023][research_tiachacht_kahouadji_2023]\] \[[He and Yuan 2024][research_he_yuan_2024]\] \[[Kawai and Hasegawa 2024][research_kawai_hasegawa_2024]\] \[[Next Generation Structural Health 2024][research_next_generation_2024]\] \[[Structural Health Monitoring/management SHM 2024][research_structural_health_2024]\] \[[Xu et al 2024][research_xu_zhang_2024]\] \[[Batista et al 2025][research_batista_trujilho_2025]\] \[[Chabukswar et al 2025][research_chabukswar_mullen_2025]\] \[[Demis Thomas et al 2025][research_demisthomas_caitrinduffydeno_2025]\] \[[Deng et al 2025][research_deng_ompusunggu_2025]\] \[[Khalid et al 2025][research_khalid_qureshi_2025]\] \[[Krishnamoorthy and Marius 2025][research_krishnamoorthy_marius_2025]\] \[[Monaco et al 2025][research_monaco_viscardi_2025]\] \[[Pan and Bao 2025][research_pan_bao_2025]\] \[[Park et al 2025][research_park_kim_2025]\] \[[Sao and Garain 2025][research_sao_garain_2025]\] \[[Scarselli and Nicassio 2025][research_scarselli_nicassio_2025]\] \[[Structural Health Monitoring 2025][research_structural_health_2025_b]\] \[[Structural health monitoring SHM 2025][research_structural_health_2025]\] \[[Viscardi et al 2025][research_viscardi_monaco_2025]\] \[[Chehrzad and Khoramishad 2026][research_chehrzad_khoramishad_2026]\] \[[Yang et al 2026][research_yang_zhang_2026]\] \[[Bill Prosser][research_billprosser]\] \[[Bishop][research_bishop]\] \[[DeSimio et al][research_desimio_miller]\] \[[Demis Thomas et al][research_demisthomas_caitrinduffydeno]\] \[[Guidance for Assessing the][research_guidance_for]\] \[[Guidelines for Implementation of][research_guidelines_for]\] \[[Landing Gear Structural Health][research_landing_gear]\] \[[Nerlikar][research_nerlikar]\] \[[Pant][research_pant]\] \[[Perspectives on Integrating Structural][research_perspectives_on]\] \[[Prognostic methodologies for remaining][research_prognostic_methodologies_for]\] \[[Ranganatha][research_ranganatha]\] \[[Sharma][research_sharma]\] \[[Structural Health Monitoring Considerations][research_structural_health]\] \[[Zhang and Pang][research_zhang_pang]\]

### Steering it, which is the third partner's trade

**75 records.** \[[Robbins, H. J. and Zebrowski, Z. E. 1966][research_robbinshj_zebrowskize_1966]\] \[[Alston, D. W. et al 1967][research_alstondw_barberjb_1967]\] \[[Hansen et al 1967][research_hansen_gabris_1967]\] \[[Rasmussen et al 1967][research_rasmussen_lanzaro_1967]\] \[[Hanford 1969][research_hanford_1969]\] \[[Moore, J. W. and Tcheng, P. 1969][research_moorejw_tchengp_1969]\] \[[Penchuk and Schlundt 1969][research_penchuk_schlundt_1969]\] \[[Abbott and Walker 1970][research_abbott_walker_1970]\] \[[Jenkins 1970][research_jenkins_1970]\] \[[Garmire, G. P. 1974][research_garmiregp_1974]\] \[[Ellis and Kearney 1982][research_ellis_kearney_1982]\] \[[Olney and Shiftlett 1982][research_olney_shiftlett_1982]\] \[[Carroll and Cox 1983][research_carroll_cox_1983]\] \[[Leitner 1986][research_leitner_1986]\] \[[Maughmer, Mark D. et al 1990][research_maughmermarkd_ozoroskil_1990]\] \[[Hattis, Philip D. and Malchow, Harvey L. 1991][research_hattisphilipd_malchowharveyl_1991]\] \[[Maughmer, M. et al 1991][research_maughmerm_straussfogeld_1991]\] \[[Gregory, Irene M. et al 1992][research_gregoryirenem_chowdhryrajivs_1992]\] \[[Hattis, Philip D. and Malchow, Harvey L. 1992][research_hattisphilipd_malchowharveyl_1992]\] \[[Murray, Jonathan 1992][research_murrayjonathan_1992]\] \[[Gregory, Irene M. et al 1993][research_gregoryirenem_mcminnjohnd_1993]\] \[[Maughmer, M. et al 1993][research_maughmerm_ozoroskil_1993]\] \[[Schmidt 1993][research_schmidt_1993]\] \[[Problems in control system 1994][research_problems_in_1994]\] \[[Ishimoto et al 1996][research_ishimoto_takizawa_1996]\] \[[Lazur et al 1999][research_lazur_sawyer_1999]\] \[[David O. Sigthorsson 2006][research_davidosigthorsson_2006]\] \[[Dyakonov, Artem A. et al 2009][research_dyakonovartema_buckgregorym_2009]\] \[[Falkiewicz et al 2009][research_falkiewicz_cesnik_2009]\] \[[Rehman et al 2009][research_rehman_fidan_2009]\] \[[Vogel et al 2009][research_vogel_kelkar_2009]\] \[[Falkiewicz et al 2010][research_falkiewicz_cesnik_2010]\] \[[Lee, Allan Y. et al 2010][research_leeallany_strahanalan_2010]\] \[[Liu et al 2010][research_liu_hou_2010]\] \[[Shuping Tan and Zhibin Li 2010][research_shupingtan_zhibinli_2010]\] \[[Jang, Jiann-Woei et al 2011][research_jangjiannwoei_alanizabran_2011]\] \[[Shi-guo et al 2011][research_shiguo_yangwang_2011]\] \[[Wan et al 2012][research_wan_wang_2012]\] \[[Wang et al 2012][research_wang_liu_2012]\] \[[Jha et al 2013][research_jha_m_2013]\] \[[Lian et al 2013][research_lian_bai_2013]\] \[[Qian et al 2013][research_qian_sun_2013]\] \[[Hong et al 2014][research_hong_xiong_2014]\] \[[Rubio Hervas and Reyhanoglu 2014][research_rubiohervas_reyhanoglu_2014]\] \[[Fan et al 2015][research_fan_yu_2015]\] \[[Hu et al 2015][research_hu_deng_2015]\] \[[Wei and Chen 2015][research_wei_chen_2015]\] \[[Feng Li et al 2016][research_fengli_chaowang_2016]\] \[[Lu and Zhou 2017][research_lu_zhou_2017]\] \[[Qi and Jianliang 2017][research_qi_jianliang_2017]\] \[[Song et al 2018][research_song_cai_2018]\] \[[Ying et al 2018][research_ying_fang_2018]\] \[[Zhao et al 2018][research_zhao_cai_2018]\] \[[Zhao et al 2018][research_zhao_he_2018]\] \[[Bao et al 2019][research_bao_wang_2019]\] \[[Buddhavarapu et al 2019][research_buddhavarapu_charlson_2019]\] \[[Song and Bian 2019][research_song_bian_2019]\] \[[Wang et al 2019][research_wang_zhang_2019]\] \[[Zhang et al 2019][research_zhang_teng_2019]\] \[[Fenfen et al 2020][research_fenfen_xubo_2020]\] \[[Averyanov et al 2021][research_averyanov_kazantsev_2021]\] \[[Stokes and Lombaerts 2023][research_stokes_lombaerts_2023]\] \[[Zhuo et al 2023][research_zhuo_zhang_2023]\] \[[Nathaniel A Stepp 2024][research_nathanielastepp_2024]\] \[[Santos and Oliveira 2024][research_santos_oliveira_2024]\] \[[Wang et al 2024][research_wang_ren_2024]\] \[[Wang et al 2024][research_wang_zhou_2024]\] \[[Djanal-Mann and Murugan 2025][research_djanalmann_murugan_2025]\] \[[Ferreira de Moura and Borges Ribeiro 2025][research_ferreirademoura_borgesribeiro_2025]\] \[[Raharema et al 2026][research_raharema_sasongko_2026]\] \[[Reynolds et al 2026][research_reynolds_caillet_2026]\] \[[Blake Stuart and Jesse McEnulty][research_blakestuart_jessemcenulty]\] \[[Du][research_du]\] \[[Jeb S. Orr et al][research_jebsorr_timothymbarrows]\] \[[John H. Wall et al][research_johnhwall_colterwrussell]\]

### Rocket propulsion as a subject in general

**760 records.** \[[Burdett 1946][research_burdett_1946]\] \[[Berggren et al 1948][research_berggren_ross_1948]\] \[[Singelmann and Mueller 1948][research_singelmann_mueller_1948]\] \[[Bernstein et al 1949][research_bernstein_linzer_1949]\] \[[Gompertz 1950][research_gompertz_1950]\] \[[Princeton Univ Nj 1952][research_princetonunivnj_1952]\] \[[Grey 1953][research_grey_1953]\] \[[Philipchuk 1953][research_philipchuk_1953]\] \[[Grey 1954][research_grey_1954]\] \[[Kamperman 1957][research_kamperman_1957]\] \[[Matthews 1957][research_matthews_1957]\] \[[Rose 1958][research_rose_1958]\] \[[Harrje 1959][research_harrje_1959]\] \[[Krebs, Richard P. and Hart, Clint E. 1959][research_krebsrichardp_hartclinte_1959]\] \[[Keast 1960][research_keast_1960]\] \[[Levine, Jack et al 1960][research_levinejack_martzcwilliam_1960]\] \[[Summerfield 1960][research_summerfield_1960]\] \[[Dethloff 1961][research_dethloff_1961]\] \[[Glatt 1961][research_glatt_1961]\] \[[Hermance 1961][research_hermance_1961]\] \[[Hoertel 1961][research_hoertel_1961]\] \[[Keast 1961][research_keast_1961]\] \[[Slocumb, Travis H. and Andrews, Earl H., Jr. 1961][research_slocumbtravish_andrewsearlhjr_1961]\] \[[Viventi 1961][research_viventi_1961]\] \[[Bujes 1962][research_bujes_1962]\] \[[Campbell 1962][research_campbell_1962]\] \[[Crabtree 1962][research_crabtree_1962]\] \[[Gale and Moedt 1962][research_gale_moedt_1962]\] \[[Jensen et al 1962][research_jensen_goshgarian_1962]\] \[[Martin 1962][research_martin_1962]\] \[[Spherical rocket motor static-test 1962][research_spherical_rocket_1962]\] \[[Aerojet-General Corp Sacramento Ca 1963][research_aerojetgeneralcorpsacramentoca_1963]\] \[[Elston 1963][research_elston_1963]\] \[[Excelco Developments Inc Silver Creek Ny 1963][research_excelcodevelopmentsincsilvercreekny_1963]\] \[[Gordon and Brown 1963][research_gordon_brown_1963]\] \[[Harris 1963][research_harris_1963]\] \[[Hauer et al 1963][research_hauer_tabata_1963]\] \[[Hauser and Helfrich 1963][research_hauser_helfrich_1963]\] \[[Kammer et al 1963][research_kammer_smith_1963]\] \[[Launch Vehicle Performance 1963][research_launch_vehicle_1963]\] \[[Lee 1963][research_lee_1963]\] \[[Luton 1963][research_luton_1963]\] \[[Lyon Inc Detroit Mi 1963][research_lyonincdetroitmi_1963]\] \[[Michigan Univ Ann Arbor 1963][research_michiganunivannarbor_1963]\] \[[Naval Weapons Center China Lake Ca 1963][research_navalweaponscenterchinalakeca_1963]\] \[[Nuclear rocket engine cycle 1963][research_nuclear_rocket_1963]\] \[[Plane 1963][research_plane_1963]\] \[[Scott 1963][research_scott_1963]\] \[[Fio Rito 1964][research_fiorito_1964]\] \[[Hurt, G. J. and Lina, L. J. 1964][research_hurtgj_linalj_1964]\] \[[Lee 1964][research_lee_1964]\] \[[Martinez and Jortner 1964][research_martinez_jortner_1964]\] \[[Mueller 1964][research_mueller_1964]\] \[[Naval Weapons Center China Lake Ca 1964][research_navalweaponscenterchinalakeca_1964]\] \[[Plane 1964][research_plane_1964]\] \[[Plane 1964][research_plane_1964_b]\] \[[Plane 1964][research_plane_1964_c]\] \[[Sale 1964][research_sale_1964]\] \[[Strauss 1964][research_strauss_1964]\] \[[Tedrick, R. N. 1964][research_tedrickrn_1964]\] \[[Tellier 1964][research_tellier_1964]\] \[[Becker, H. and Hamilton, H. 1965][research_beckerh_hamiltonh_1965]\] \[[Brinich, P. F. et al 1965][research_brinichpf_jackjr_1965]\] \[[Darwell and Leeming 1965][research_darwell_leeming_1965]\] \[[Friedland 1965][research_friedland_1965]\] \[[Holdhusen and Perusse 1965][research_holdhusen_perusse_1965]\] \[[Hornstein 1965][research_hornstein_1965]\] \[[Jones, H. B., Jr. et al 1965][research_joneshbjr_knauerrc_1965]\] \[[Langill, Jr. 1965][research_langilljr_1965]\] \[[Mohler 1965][research_mohler_1965]\] \[[Nagy, J. A. 1965][research_nagyja_1965]\] \[[Nelius and Harris 1965][research_nelius_harris_1965]\] \[[Perlmutter and DePierre 1965][research_perlmutter_depierre_1965]\] \[[Raper, J. L. 1965][research_raperjl_1965]\] \[[Seidel 1965][research_seidel_1965]\] \[[Techniques for rocket engine 1965][research_techniques_for_1965]\] \[[Wong and Brown 1965][research_wong_brown_1965]\] \[[Becker, H. and Tang, C. N. 1966][research_beckerh_tangcn_1966]\] \[[Breshears et al 1966][research_breshears_mccafferty_1966]\] \[[Brunner, J. J. 1966][research_brunnerjj_1966]\] \[[Craig, K. A. 1966][research_craigka_1966]\] \[[Crocker, M. J. and Potter, R. C. 1966][research_crockermj_potterrc_1966]\] \[[Duke and Houghton 1966][research_duke_houghton_1966]\] \[[Hendershot, K. C. 1966][research_hendershotkc_1966]\] \[[Hopson, George D. and McAnelly, William B. 1966][research_hopsongeorged_mcanellywilliamb_1966]\] \[[Kirschbaum and Sheridan 1966][research_kirschbaum_sheridan_1966]\] \[[Leese 1966][research_leese_1966]\] \[[Mcgee, R. S. and Say, M. B. 1966][research_mcgeers_saymb_1966]\] \[[Mueller 1966][research_mueller_1966]\] \[[Smallwood 1966][research_smallwood_1966]\] \[[Tobey and Bastress 1966][research_tobey_bastress_1966]\] \[[Carey 1967][research_carey_1967]\] \[[Clark, D. H. and Tenenbaum, D. M. 1967][research_clarkdh_tenenbaumdm_1967]\] \[[Clayton, R. M. et al 1967][research_claytonrm_gerbrachtfg_1967]\] \[[Fairall 1967][research_fairall_1967]\] \[[Friedman et al 1967][research_friedman_hines_1967]\] \[[Heuston et al 1967][research_heuston_fish_1967]\] \[[Kunz 1967][research_kunz_1967]\] \[[Milleman 1967][research_milleman_1967]\] \[[Neiland, V. R. 1967][research_neilandvr_1967]\] \[[Smallwood 1967][research_smallwood_1967]\] \[[Sprattling, Jr. 1967][research_sprattlingjr_1967]\] \[[Crowe et al 1968][research_crowe_babcock_1968]\] \[[Herrick 1968][research_herrick_1968]\] \[[Porter 1968][research_porter_1968]\] \[[Rafferty 1968][research_rafferty_1968]\] \[[Williams 1968][research_williams_1968]\] \[[Wong and Brown 1968][research_wong_brown_1968]\] \[[Baker 1969][research_baker_1969]\] \[[Hosack 1969][research_hosack_1969]\] \[[Hosack and Stromsta 1969][research_hosack_stromsta_1969]\] \[[Hydrostatic bearings for cryogenic 1969][research_hydrostatic_bearings_1969]\] \[[Maynard 1969][research_maynard_1969]\] \[[Rogero, S. 1969][research_rogeros_1969]\] \[[Campbell 1970][research_campbell_1970]\] \[[Carroll 1970][research_carroll_1970]\] \[[Franklin and Tinsley 1970][research_franklin_tinsley_1970]\] \[[Gabriel and Helms 1970][research_gabriel_helms_1970]\] \[[Hardesty 1970][research_hardesty_1970]\] \[[Mclafferty 1970][research_mclafferty_1970]\] \[[Ward, Jr. 1970][research_wardjr_1970]\] \[[Babcock and Coe 1971][research_babcock_coe_1971]\] \[[Balcomb 1972][research_balcomb_1972]\] \[[Experimental investigation of combustor 1972][research_experimental_investigation_1972]\] \[[Marchese, V. P. et al 1972][research_marchesevp_rakowskyel_1972]\] \[[Odom, J. B. 1972][research_odomjb_1972]\] \[[Smith, G. W. and Sforzini, R. H. 1972][research_smithgw_sforzinirh_1972]\] \[[Study of solid rocket 1972][research_study_of_1972]\] \[[Study of solid rocket 1972][research_study_of_1972_b]\] \[[Study of solid rocket 1972][research_study_of_1972_c]\] \[[Study of solid rocket 1972][research_study_of_1972_d]\] \[[Study of solid rocket 1972][research_study_of_1972_e]\] \[[Study of solid rocket 1972][research_study_of_1972_f]\] \[[Study of solid rocket 1972][research_study_of_1972_g]\] \[[Study of solid rocket 1972][research_study_of_1972_h]\] \[[Technical report analysis and 1972][research_technical_report_1972]\] \[[Vonderesch, A. H. 1972][research_vondereschah_1972]\] \[[Calhoon et al 1973][research_calhoon_kors_1973]\] \[[Fries, J. 1973][research_friesj_1973]\] \[[Fuller 1973][research_fuller_1973]\] \[[Larson 1973][research_larson_1973]\] \[[Nurick, W. H. and Hines, W. S. 1973][research_nurickwh_hinesws_1973]\] \[[Salinas and Ball 1973][research_salinas_ball_1973]\] \[[Sanchini, D. J. and Kirby, F. M. 1973][research_sanchinidj_kirbyfm_1973]\] \[[Toelle, R. G. et al 1973][research_toellerg_blackwelldl_1973]\] \[[Wagner, W. R. and Waldman, B. J. 1973][research_wagnerwr_waldmanbj_1973]\] \[[Baetz 1974][research_baetz_1974]\] \[[Marchese, V. P. 1974][research_marchesevp_1974]\] \[[Markowsky and McManus 1974][research_markowsky_mcmanus_1974]\] \[[Merryman, H. L. and Smith, L. R. 1974][research_merrymanhl_smithlr_1974]\] \[[Rakowsky, E. L. and Marchese, V. P. 1974][research_rakowskyel_marchesevp_1974]\] \[[Baetz 1975][research_baetz_1975]\] \[[Lucci and Hodson 1975][research_lucci_hodson_1975]\] \[[Pergament, H. S. et al 1975][research_pergamenths_thorperd_1975]\] \[[Eldred, C. H. and Gordon, S. V. 1976][research_eldredch_gordonsv_1976]\] \[[Liquid rocket engine nozzles 1976][research_liquid_rocket_1976]\] \[[Sforzini, R. H. and Foster, W. A., Jr. 1976][research_sforzinirh_fosterwajr_1976]\] \[[Vetter 1977][research_vetter_1977]\] \[[Kosmann et al 1978][research_kosmann_dionne_1978]\] \[[Pouliquen 1978][research_pouliquen_1978]\] \[[Advisory Group for Aerospace Research and Development 1979][research_advisorygroupforaerospaceresearchanddevelopment_1979]\] \[[Bjorklund et al 1979][research_bjorklund_rogero_1979]\] \[[Caveny, L. H. et al 1980][research_cavenylh_kuokk_1980]\] \[[Francis and Thompson 1980][research_francis_thompson_1980]\] \[[Mathes, H. B. 1980][research_matheshb_1980]\] \[[Mullen, C. R. and Kearnes, J. H. 1980][research_mullencr_kearnesjh_1980]\] \[[Allen 1981][research_allen_1981]\] \[[Bergman et al 1981][research_bergman_boyd_1981]\] \[[Etters and Flurchick 1981][research_etters_flurchick_1981]\] \[[Foster, W. A., Jr. et al 1981][research_fosterwajr_sforzinirh_1981]\] \[[Gunter, E. J. and Flack, R. D. 1981][research_gunterej_flackrd_1981]\] \[[Hudson et al 1981][research_hudson_brosz_1981]\] \[[Koelle 1981][research_koelle_1981]\] \[[Millard et al 1982][research_millard_barton_1982]\] \[[Nakanishi et al 1982][research_nakanishi_sogame_1982]\] \[[Smith, S. D. 1982][research_smithsd_1982]\] \[[Yerushalmi and Glick 1982][research_yerushalmi_glick_1982]\] \[[Allen 1983][research_allen_1983]\] \[[Lemaster, R. A. and Runyan, R. B. 1983][research_lemasterra_runyanrb_1983]\] \[[Martin, C. L. 1983][research_martincl_1983]\] \[[Pollet 1983][research_pollet_1983]\] \[[Smith 1983][research_smith_1983]\] \[[Hardgrove and Krieg, Jr. 1984][research_hardgrove_kriegjr_1984]\] \[[Koelle 1984][research_koelle_1984]\] \[[Gibson 1985][research_gibson_1985]\] \[[Korting and Reitsma 1985][research_korting_reitsma_1985]\] \[[Marsik, S. J. and Morea, S. F. 1985][research_marsiksj_moreasf_1985]\] \[[Marsik, S. J. and Morea, S. F. 1985][research_marsiksj_moreasf_1985_b]\] \[[Mccoy, K. E. and Hester, J. 1985][research_mccoyke_hesterj_1985]\] \[[Welsh 1985][research_welsh_1985]\] \[[Block 2 Solid Rocket 1986][research_block_2_1986]\] \[[External autoignition test for 1986][research_external_autoignition_1986]\] \[[Forester and Strom 1986][research_forester_strom_1986]\] \[[Foster, W. A., Jr. et al 1986][research_fosterwajr_shuph_1986]\] \[[Meisl 1986][research_meisl_1986]\] \[[Pavli, A. J. et al 1986][research_pavliaj_kacynskikj_1986]\] \[[Praharaj, Sarat C. and Palko, Richard L. 1986][research_praharajsaratc_palkorichardl_1986]\] \[[Chiu 1987][research_chiu_1987]\] \[[Cox, Jr. 1987][research_coxjr_1987]\] \[[Davidian 1987][research_davidian_1987]\] \[[French 1987][research_french_1987]\] \[[Pavli, Albert J. et al 1987][research_pavlialbertj_kacynskikennethj_1987]\] \[[Ali and Crawford 1988][research_ali_crawford_1988]\] \[[Cosens and Newton 1988][research_cosens_newton_1988]\] \[[Cox, Jr. 1988][research_coxjr_1988]\] \[[Davis, Jr. 1988][research_davisjr_1988]\] \[[Manski, Detlef and Martin, James A. 1988][research_manskidetlef_martinjamesa_1988]\] \[[Meisl 1988][research_meisl_1988]\] \[[Moore, Carleton J. 1988][research_moorecarletonj_1988]\] \[[Naraghi, M. H. N. and Armstrong, E. S. 1988][research_naraghimhn_armstronges_1988]\] \[[Petrasek, Donald W. and Stephens, Joseph R. 1988][research_petrasekdonaldw_stephensjosephr_1988]\] \[[Powers, William T. et al 1988][research_powerswilliamt_sherrellfg_1988]\] \[[Rubin, S. et al 1988][research_rubins_searlega_1988]\] \[[Russell, D. L. et al 1988][research_russelldl_blacklockk_1988]\] \[[Siddiqui and Smith 1988][research_siddiqui_smith_1988]\] \[[Vibbart 1988][research_vibbart_1988]\] \[[Bryant 1989][research_bryant_1989]\] \[[Collamore, Frank N. 1989][research_collamorefrankn_1989]\] \[[Difrancesco et al 1989][research_difrancesco_boorady_1989]\] \[[Dunn, Michael G. 1989][research_dunnmichaelg_1989]\] \[[Dynamic real-time radiography of 1989][research_dynamic_real_time_1989]\] \[[Estler, W. Tyler 1989][research_estlerwtyler_1989]\] \[[Gunn 1989][research_gunn_1989]\] \[[Hagar and Alcock 1989][research_hagar_alcock_1989]\] \[[Jones, Kenneth W. and Zoller, Lowell K. 1989][research_joneskennethw_zollerlowellk_1989]\] \[[Jones, Kenneth W. and Zoller, Lowell K. 1989][research_joneskennethw_zollerlowellk_1989_b]\] \[[Lin 1989][research_lin_1989]\] \[[Martin, James A. and Manski, Detlef 1989][research_martinjamesa_manskidetlef_1989]\] \[[Meisl 1989][research_meisl_1989]\] \[[Petrasek, Donald W. and Stephens, Joseph R. 1989][research_petrasekdonaldw_stephensjosephr_1989]\] \[[Pieper, Jerry L. and Muss, Jeff 1989][research_pieperjerryl_mussjeff_1989]\] \[[Salita, Mark 1989][research_salitamark_1989]\] \[[Tulpule 1989][research_tulpule_1989]\] \[[Ahmed, Rafiq 1990][research_ahmedrafiq_1990]\] \[[Bentsman, Joseph et al 1990][research_bentsmanjoseph_pearlsteinarnej_1990]\] \[[Bickford, R. L. and Madzsar, G. 1990][research_bickfordrl_madzsarg_1990]\] \[[Bickford, R. L. et al 1990][research_bickfordrl_duncandb_1990]\] \[[Chiu et al 1990][research_chiu_kross_1990]\] \[[Dunn, Michael G. 1990][research_dunnmichaelg_1990]\] \[[Glozman, Vladimir and Brillhart, Ralph D. 1990][research_glozmanvladimir_brillhartralphd_1990]\] \[[Hamed, Awatef 1990][research_hamedawatef_1990]\] \[[Han, Samuel S. 1990][research_hansamuels_1990]\] \[[Martin, James A. and Kramer, Richard D. 1990][research_martinjamesa_kramerrichardd_1990]\] \[[Martinez et al 1990][research_martinez_reinert_1990]\] \[[Melchior 1990][research_melchior_1990]\] \[[Puening 1990][research_puening_1990]\] \[[Sepcenko, Valentin et al 1990][research_sepcenkovalentin_margasahayamravi_1990]\] \[[Wang, T.-S. 1990][research_wangts_1990]\] \[[Wang, Ten-See and Chen, Yen-Sen 1990][research_wangtensee_chenyensen_1990]\] \[[Benjamin, Theodore G. and Mcconnaughey, Paul K. 1991][research_benjamintheodoreg_mcconnaugheypaulk_1991]\] \[[Borowski, Stanley K. 1991][research_borowskistanleyk_1991]\] \[[Dougherty, N. Sam and Liu, Baw-Lin 1991][research_doughertynsam_liubawlin_1991]\] \[[Gage, Mark and Dehoff, Ronald 1991][research_gagemark_dehoffronald_1991]\] \[[Han, Samuel S. 1991][research_hansamuels_1991]\] \[[Herbell, Thomas P. and Eckel, Andrew J. 1991][research_herbellthomasp_eckelandrewj_1991]\] \[[Hybrid Rocket Propulsion for 1991][research_hybrid_rocket_1991]\] \[[Lemberger et al 1991][research_lemberger_patanchon_1991]\] \[[Lorenzo, Carl F. and Musgrave, Jeffrey L. 1991][research_lorenzocarlf_musgravejeffreyl_1991]\] \[[Lui, C. Y. and Mason, D. R. 1991][research_luicy_masondr_1991]\] \[[Raines, N. G. et al 1991][research_rainesng_bircherfe_1991]\] \[[Roncace 1991][research_roncace_1991]\] \[[Toten et al 1991][research_toten_fong_1991]\] \[[Zakrajsek, June F. 1991][research_zakrajsekjunef_1991]\] \[[Zubrin and Decher 1991][research_zubrin_decher_1991]\] \[[Anderson, P. G. et al 1992][research_andersonpg_chenys_1992]\] \[[Appendix C Rocket Engine 1992][research_appendix_c_1992]\] \[[Babbitt, Norman E., III 1992][research_babbittnormaneiii_1992]\] \[[Ballard 1992][research_ballard_1992]\] \[[Chaouat and Vuillot 1992][research_chaouat_vuillot_1992]\] \[[Design of Rocket-Engine Control 1992][research_design_of_1992]\] \[[Gaddis, Stephen W. et al 1992][research_gaddisstephenw_hudsonsusant_1992]\] \[[Ghaffarian, Benny et al 1992][research_ghaffarianbenny_majumdaralokk_1992]\] \[[Giridharan, M. G. et al 1992][research_giridharanmg_leejg_1992]\] \[[Koelle 1992][research_koelle_1992]\] \[[Luke, Gary D. and Dwyer, Harry A. 1992][research_lukegaryd_dwyerharrya_1992]\] \[[Madzsar, G. C. et al 1992][research_madzsargc_bickfordrl_1992]\] \[[Meisl 1992][research_meisl_1992]\] \[[Merrill, W. C. et al 1992][research_merrillwc_musgravejl_1992]\] \[[Petrosky 1992][research_petrosky_1992]\] \[[Rocket engine propulsion 'system 1992][research_rocket_engine_1992]\] \[[Sakala, G. G. and Raines, N. G. 1992][research_sakalagg_rainesng_1992]\] \[[Tran, Ken et al 1992][research_tranken_chandanielc_1992]\] \[[Anderson, P. G. et al 1993][research_andersonpg_chenggc_1993]\] \[[Arnett 1993][research_arnett_1993]\] \[[Benjamin, Theodore G. et al 1993][research_benjamintheodoreg_garciaroberto_1993]\] \[[Binder 1993][research_binder_1993]\] \[[Browning 1993][research_browning_1993]\] \[[Culver and Rochow 1993][research_culver_rochow_1993]\] \[[Davidian, Kenneth O. and Kacynski, Kenneth J. 1993][research_davidiankennetho_kacynskikennethj_1993]\] \[[Degelsmith et al 1993][research_degelsmith_freaner_1993]\] \[[Delcher et al 1993][research_delcher_nemeth_1993]\] \[[Gould, Reginald J. 1993][research_gouldreginaldj_1993]\] \[[Grubelich et al 1993][research_grubelich_rowland_1993]\] \[[Gulati, S. et al 1993][research_gulatis_tawelr_1993]\] \[[Huzel 1993][research_huzel_1993]\] \[[Jenkins, Rhonald M. and Foster, Winfred A., Jr. 1993][research_jenkinsrhonaldm_fosterwinfredajr_1993]\] \[[Keyhani, M. 1993][research_keyhanim_1993]\] \[[Kuo et al 1993][research_kuo_kokal_1993]\] \[[Maram 1993][research_maram_1993]\] \[[Niiya, Karen E. et al 1993][research_niiyakarene_walkerricharde_1993]\] \[[Obrien, Charles J. 1993][research_obriencharlesj_1993]\] \[[Ratcliff, Mark L. et al 1993][research_ratcliffmarkl_athavalemaheshm_1993]\] \[[Rutledge 1993][research_rutledge_1993]\] \[[Ryan and Verderaime 1993][research_ryan_verderaime_1993]\] \[[Sander, E. J. and Leahy, J. C. 1993][research_sanderej_leahyjc_1993]\] \[[Small nuclear thermal rocket 1993][research_small_nuclear_1993]\] \[[Tierney 1993][research_tierney_1993]\] \[[Tucker, P. K. and Warsi, S. A. 1993][research_tuckerpk_warsisa_1993]\] \[[Williams, Robert W. 1993][research_williamsrobertw_1993]\] \[[Borowski, Stanley K. 1994][research_borowskistanleyk_1994]\] \[[Fanciullo and Lacefield 1994][research_fanciullo_lacefield_1994]\] \[[Green 1994][research_green_1994]\] \[[Hardy, Terry L. and Rapp, Douglas C. 1994][research_hardyterryl_rappdouglasc_1994]\] \[[Heat transfer measurements and 1994][research_heat_transfer_1994]\] \[[Hydrogen peroxide hybrid rocket 1994][research_hydrogen_peroxide_1994]\] \[[Jones, Kenneth M. 1994][research_joneskennethm_1994]\] \[[Kuo, Kenneth K. et al 1994][research_kuokennethk_luyc_1994]\] \[[Lacefield and Sprow 1994][research_lacefield_sprow_1994]\] \[[Liu, Chung-Chiun 1994][research_liuchungchiun_1994]\] \[[Madzsar et al 1994][research_madzsar_bickford_1994]\] \[[Pande 1994][research_pande_1994]\] \[[Schley 1994][research_schley_1994]\] \[[Trevino, Luis C. 1994][research_trevinoluisc_1994]\] \[[Binder, Michael P. 1995][research_bindermichaelp_1995]\] \[[Brown et al 1995][research_brown_coleman_1995]\] \[[Campbell and Riccio 1995][research_campbell_riccio_1995]\] \[[Casey 1995][research_casey_1995]\] \[[Combustion Instability Analysis Numerical 1995][research_combustion_instability_1995]\] \[[Goertz 1995][research_goertz_1995]\] \[[Gu and Liu 1995][research_gu_liu_1995]\] \[[Instability Phenomenology and Case 1995][research_instability_phenomenology_1995]\] \[[Instability Phenomenology and Case 1995][research_instability_phenomenology_1995_b]\] \[[Instability Phenomenology and Case 1995][research_instability_phenomenology_1995_c]\] \[[Instability Phenomenology and Case 1995][research_instability_phenomenology_1995_d]\] \[[Liquid Rocket Engine Combustion 1995][research_liquid_rocket_1995]\] \[[Lorenzo 1995][research_lorenzo_1995]\] \[[McAmis 1995][research_mcamis_1995]\] \[[Performance of Fusion-Fission Hybrid 1995][research_performance_of_1995]\] \[[Sambamurthi 1995][research_sambamurthi_1995]\] \[[Anderson et al 1996][research_anderson_mcamis_1996]\] \[[Blomshield, Fred S. and Bicker, C. J. 1996][research_blomshieldfreds_bickercj_1996]\] \[[Follett, W. 1996][research_follettw_1996]\] \[[Follett, W. et al 1996][research_follettw_ketchuma_1996]\] \[[McGrath 1996][research_mcgrath_1996]\] \[[Micklow, Gerald J. 1996][research_micklowgeraldj_1996]\] \[[Voinov and Mel'nikov 1996][research_voinov_melnikov_1996]\] \[[Williams, R. W. 1996][research_williamsrw_1996]\] \[[Binder, Michael et al 1997][research_bindermichael_tomsikthomas_1997]\] \[[Goracke et al 1997][research_goracke_levack_1997]\] \[[Haidinger et al 1997][research_haidinger_weiland_1997]\] \[[Jenkins, Rhonald M. 1997][research_jenkinsrhonaldm_1997]\] \[[Kassoy 1997][research_kassoy_1997]\] \[[Lee et al 1997][research_lee_olds_1997]\] \[[Palaszewski, Bryan 1997][research_palaszewskibryan_1997]\] \[[Jetevator for rocket engine 1998][research_jetevator_for_1998]\] \[[Koelle 1998][research_koelle_1998]\] \[[Koschel 1998][research_koschel_1998]\] \[[Mitra, D. et al 1998][research_mitrad_bhallapn_1998]\] \[[Palaszewski, Bryan A. 1998][research_palaszewskibryana_1998]\] \[[Palaszewski, Bryan et al 1998][research_palaszewskibryan_olearyrobert_1998]\] \[[Rice et al 1998][research_rice_bangsund_1998]\] \[[Rocket engine seals project 1998][research_rocket_engine_1998]\] \[[Shen, Ji Y. and Sharpe, Lonnie, Jr. 1998][research_shenjiy_sharpelonniejr_1998]\] \[[Effinger, Michael et al 1999][research_effingermichael_clintonrgjr_1999]\] \[[Farmer, Richard C. et al 1999][research_farmerrichardc_chenggary_1999]\] \[[Genge, Gary G. and Marsh, Matthew W. 1999][research_gengegaryg_marshmattheww_1999]\] \[[Knuth et al 1999][research_knuth_gramer_1999]\] \[[Mueller et al 1999][research_mueller_bratkovich_1999]\] \[[Nix, Michael B. and Escher, William J. d. 1999][research_nixmichaelb_escherwilliamjd_1999]\] \[[Pytanowski 1999][research_pytanowski_1999]\] \[[Santoro, Robert J. and Pal, Sibtosh 1999][research_santororobertj_palsibtosh_1999]\] \[[Umholtz 1999][research_umholtz_1999]\] \[[Wu et al 1999][research_wu_fuller_1999]\] \[[Blair and DeGeorge 2000][research_blair_degeorge_2000]\] \[[Brown, Andrew M. 2000][research_brownandrewm_2000]\] \[[Kiris, Cetin and Williams, Robert 2000][research_kiriscetin_williamsrobert_2000]\] \[[Laubacher, Brian A. 2000][research_laubacherbriana_2000]\] \[[London et al 2000][research_london_epstein_2000]\] \[[Majumdar, Alok et al 2000][research_majumdaralok_polsgroverobert_2000]\] \[[McDonald, Kathleen R. and Wooten, John R. 2000][research_mcdonaldkathleenr_wootenjohnr_2000]\] \[[Rahaim et al 2000][research_rahaim_grage_2000]\] \[[Rocket Engine One Super-Profit 2000][research_rocket_engine_2000_b]\] \[[Rocket Engine Two Hard 2000][research_rocket_engine_2000]\] \[[Ryan, H. M. et al 2000][research_ryanhm_rahmans_2000]\] \[[Schoneman et al 2000][research_schoneman_buckley_2000]\] \[[Stechman et al 2000][research_stechman_woll_2000]\] \[[Vaidyanathan, Rajkumar et al 2000][research_vaidyanathanrajkumar_papitanilay_2000]\] \[[Wehrmeyer, Joseph et al 2000][research_wehrmeyerjoseph_hartfieldroyjjr_2000]\] \[[Whitehead 2000][research_whitehead_2000]\] \[[A Global Optimization Methodology 2001][research_a_global_2001]\] \[[Brown, Andrew M. and Brunty, Joseph A. 2001][research_brownandrewm_bruntyjosepha_2001]\] \[[Candler 2001][research_candler_2001]\] \[[Farmer, Richard et al 2001][research_farmerrichard_chenggary_2001]\] \[[Jensen 2001][research_jensen_2001]\] \[[Kiris, Cetin et al 2001][research_kiriscetin_chanwilliam_2001]\] \[[Kris, Cetin C. and Kwak, Dochan 2001][research_kriscetinc_kwakdochan_2001]\] \[[Lee, Jonathan A. et al 2001][research_leejonathana_elamsandy_2001]\] \[[Morris, Christopher I. 2001][research_morrischristopheri_2001]\] \[[Mossman and Perkins 2001][research_mossman_perkins_2001]\] \[[Nguyen, Dalton and Turner, Larry D. 2001][research_nguyendalton_turnerlarryd_2001]\] \[[Osborne, Robin et al 2001][research_osbornerobin_wehrmeyerjoseph_2001]\] \[[Santi, L. Michael 2001][research_santilmichael_2001]\] \[[Shelley et al 2001][research_shelley_leclaire_2001]\] \[[Shyy et al 2001][research_shyy_papila_2001]\] \[[Ventura and WErnimont 2001][research_ventura_wernimont_2001]\] \[[Wehrmeyer, Joseph A. et al 2001][research_wehrmeyerjosepha_osbornerobinj_2001]\] \[[Chelner 2002][research_chelner_2002]\] \[[Hyde 2002][research_hyde_2002]\] \[[Joseph A Wehrmeyer 2002][research_josephawehrmeyer_2002]\] \[[Kiris, Cetin et al 2002][research_kiriscetin_chanwilliam_2002]\] \[[Morris 2002][research_morris_2002]\] \[[Nesman, Tom and Turner, James E. 2002][research_nesmantom_turnerjamese_2002]\] \[[Nguyen, Dalton 2002][research_nguyendalton_2002]\] \[[Ogbuji, Linus U. J. et al 2002][research_ogbujilinusuj_humphreydonaldh_2002]\] \[[Ogbuji, Linus U. Thomas and Humphrey, Donald L. 2002][research_ogbujilinusuthomas_humphreydonaldl_2002]\] \[[Talley 2002][research_talley_2002]\] \[[Thornburg 2002][research_thornburg_2002]\] \[[Trinh, Huu P. et al 2002][research_trinhhuup_bullardbrad_2002]\] \[[Vorozhtsov and Matvienko 2002][research_vorozhtsov_matvienko_2002]\] \[[Weidner, Thomas J. et al 2002][research_weidnerthomasj_larsendavidv_2002]\] \[[Beck and Beach 2003][research_beck_beach_2003]\] \[[Chelner 2003][research_chelner_2003]\] \[[Cheng, Gary 2003][research_chenggary_2003]\] \[[Christenson, Rick L. et al 2003][research_christensonrickl_nelsonmichaela_2003]\] \[[Conley et al 2003][research_conley_lee_2003]\] \[[Gregory and Han 2003][research_gregory_han_2003]\] \[[Huppi, Hal et al 2003][research_huppihal_tobiasmark_2003]\] \[[Majumdar, Alok and Flachbart, Robin 2003][research_majumdaralok_flachbartrobin_2003]\] \[[Meyers et al 2003][research_meyers_lu_2003]\] \[[Onodera et al 2003][research_onodera_sakamoto_2003]\] \[[Pempie 2003][research_pempie_2003]\] \[[Tejwani, Gopal D. et al 2003][research_tejwanigopald_langfordlestera_2003]\] \[[Trefny, Charles J. 2003][research_trefnycharlesj_2003]\] \[[Bradford et al 2004][research_bradford_charania_2004]\] \[[Cho et al 2004][research_cho_kim_2004]\] \[[Morris 2004][research_morris_2004]\] \[[Nix, Michael and Staton, Eric J. 2004][research_nixmichael_statonericj_2004]\] \[[Portz 2004][research_portz_2004]\] \[[Rocket Engine Nozzle Concepts 2004][research_rocket_engine_2004]\] \[[Sims, J. D. et al 2004][research_simsjd_flandrogarya_2004]\] \[[Wang 2004][research_wang_2004]\] \[[Williams 2004][research_williams_2004]\] \[[Yamanishi et al 2004][research_yamanishi_kimura_2004]\] \[[Yang 2004][research_yang_2004]\] \[[Hill, A. and Acosta, E. 2005][research_hilla_acostae_2005]\] \[[Jensen 2005][research_jensen_2005]\] \[[Lawrence 2005][research_lawrence_2005]\] \[[Liquid-Propellant Rocket Engine 2005][research_liquid_propellant_rocket_2005]\] \[[Rocket Engine 2005][research_rocket_engine_2005]\] \[[Shelton, Joey D. et al 2005][research_sheltonjoeyd_frederickroberta_2005]\] \[[Stewart et al 2005][research_stewart_tang_2005]\] \[[Tiwari et al 2005][research_tiwari_kalluru_2005]\] \[[Barkhoudarian, Sarkis and Kittinger, Scott 2006][research_barkhoudariansarkis_kittingerscott_2006]\] \[[Chung, J. N. et al 2006][research_chungjn_tullylandon_2006]\] \[[France's Liquid Propellant Rocket-Engine 2006][research_france_s_liquid_2006]\] \[[Hellman 2006][research_hellman_2006]\] \[[Japan's Liquid Propellant Rocket-Engine 2006][research_japan_s_liquid_2006]\] \[[Kutter 2006][research_kutter_2006]\] \[[Liquid Propellant Rocket-Engine Organizations 2006][research_liquid_propellant_2006]\] \[[Rothmund 2006][research_rothmund_2006]\] \[[Snoddy et al 2006][research_snoddy_dumbacher_2006]\] \[[Hughes, Mark S. et al 2007][research_hughesmarks_davisdawnm_2007]\] \[[Longenecker and Clark 2007][research_longenecker_clark_2007]\] \[[Modular Program for Conceptual 2007][research_modular_program_2007]\] \[[Moore et al 2007][research_moore_kuo_2007]\] \[[Rusick 2007][research_rusick_2007]\] \[[Smalley, Kurt B. et al 2007][research_smalleykurtb_brownandrew_2007]\] \[[Smith et al 2007][research_smith_schneider_2007]\] \[[Alexander, Leslie et al 2008][research_alexanderleslie_chapmanjack_2008]\] \[[Burrows 2008][research_burrows_2008]\] \[[Dombrovsky 2008][research_dombrovsky_2008]\] \[[Haberstroh et al 2008][research_haberstroh_besnard_2008]\] \[[Heister 2008][research_heister_2008]\] \[[Hulka 2008][research_hulka_2008]\] \[[Hunley 2008][research_hunley_2008]\] \[[Hunley 2008][research_hunley_2008_b]\] \[[Hunley 2008][research_hunley_2008_c]\] \[[Jacob 2008][research_jacob_2008]\] \[[Rhee et al 2008][research_rhee_lee_2008]\] \[[Shimizu et al 2008][research_shimizu_mizobuchi_2008]\] \[[Gao and Sun 2009][research_gao_sun_2009]\] \[[Kenny, Jeremy et al 2009][research_kennyjeremy_hobbschris_2009]\] \[[Rocket Engine Pump Feed 2009][research_rocket_engine_2009]\] \[[Suresh et al 2009][research_suresh_rong_2009]\] \[[Butt, Adam et al 2010][research_buttadam_poppchristopherg_2010]\] \[[Creech, Dennis M. et al 2010][research_creechdennism_threetgradyejr_2010]\] \[[El-Aini, Yehia et al 2010][research_elainiyehia_parkjohn_2010]\] \[[French 2010][research_french_2010]\] \[[Graham 2010][research_graham_2010]\] \[[Kitsche 2010][research_kitsche_2010]\] \[[Maynard, Bryon T. and Raines, Nickey G. 2010][research_maynardbryont_rainesnickeyg_2010]\] \[[Nallasamy, R. et al 2010][research_nallasamyr_kandulam_2010]\] \[[Vargas, Magda B. and Kenny, R. Jeremy 2010][research_vargasmagdab_kennyrjeremy_2010]\] \[[Watanabe and Mikami 2010][research_watanabe_mikami_2010]\] \[[Bandyopadhyay, Alak et al 2011][research_bandyopadhyayalak_hamillbrian_2011]\] \[[Johnson, Martin L. and Crawford, Kevin 2011][research_johnsonmartinl_crawfordkevin_2011]\] \[[Kenny, R. Jeremy et al 2011][research_kennyrjeremy_leeerik_2011]\] \[[Li et al 2011][research_li_fan_2011]\] \[[Mehta, Manish et al 2011][research_mehtamanish_canabalfrancisco_2011]\] \[[Pinier 2011][research_pinier_2011]\] \[[Plasma propulsion for rocket 2011][research_plasma_propulsion_2011]\] \[[Quing, Xinlin et al 2011][research_quingxinlin_beardshawn_2011]\] \[[Albanese et al 2012][research_albanese_meyers_2012]\] \[[Anderson et al 2012][research_anderson_son_2012]\] \[[Baars, Woutijn J. et al 2012][research_baarswoutijnj_tinneycharlese_2012]\] \[[Cortopassi, A. C. et al 2012][research_cortopassiac_martinht_2012]\] \[[Lancelle et al 2012][research_lancelle_bozic_2012]\] \[[Lanin 2012][research_lanin_2012]\] \[[Lanin 2012][research_lanin_2012_b]\] \[[May, Todd A. and Creech, Stephen D. 2012][research_maytodda_creechstephend_2012]\] \[[Progress made on experimental 2012][research_progress_made_2012]\] \[[Rocket Engine Innovations Advance 2012][research_rocket_engine_2012]\] \[[Threet, Grady E. et al 2012][research_threetgradye_watersericd_2012]\] \[[Ali, Aliyah N. and Borrer, Jerry L. 2013][research_alialiyahn_borrerjerryl_2013]\] \[[Ali, Aliyah N. and Borrer, Jerry L. 2013][research_alialiyahn_borrerjerryl_2013_b]\] \[[Anderson et al 2013][research_anderson_heister_2013]\] \[[Bennewitz et al 2013][research_bennewitz_lineberry_2013]\] \[[Chiba et al 2013][research_chiba_kanazaki_2013]\] \[[Ellis, David L. 2013][research_ellisdavidl_2013]\] \[[Long et al 2013][research_long_joyner_2013]\] \[[Wan et al 2013][research_wan_shu_2013]\] \[[Waters, Eric D. et al 2013][research_watersericd_beersbenjamin_2013]\] \[[Bai and Weng 2014][research_bai_weng_2014]\] \[[Brown, Andrew M. 2014][research_brownandrewm_2014]\] \[[Chiba et al 2014][research_chiba_watanabe_2014]\] \[[Chiba et al 2014][research_chiba_kanazaki_2014]\] \[[Dorosh and Leontiev 2014][research_dorosh_leontiev_2014]\] \[[Fischbach, Sean 2014][research_fischbachsean_2014]\] \[[Foster, Winfred A., Jr. et al 2014][research_fosterwinfredajr_crowderwinston_2014]\] \[[Harvazinski et al 2014][research_harvazinski_sankaran_2014]\] \[[Jones, Daniel S. et al 2014][research_jonesdaniels_rufjosephh_2014]\] \[[Jones, Jonathan et al 2014][research_jonesjonathan_kibbeytim_2014]\] \[[Mehta et al 2014][research_mehta_dufrene_2014]\] \[[Pritchett, Victor E. et al 2014][research_pritchettvictore_maylemelodyn_2014]\] \[[Spurlock and Williams 2014][research_spurlock_williams_2014]\] \[[Starkey et al 2014][research_starkey_cannella_2014]\] \[[Takagi et al 2014][research_takagi_morozumi_2014]\] \[[Wall, John H. et al 2014][research_walljohnh_orrjebs_2014]\] \[[Watson et al 2014][research_watson_neeley_2014]\] \[[Westra, Douglas G. and West, Jeffrey S. 2014][research_westradouglasg_westjeffreys_2014]\] \[[Alter, Stephen J. et al 2015][research_alterstephenj_brauckmanngregoryj_2015]\] \[[Alter, Stephen J. et al 2015][research_alterstephenj_brauckmanngregoryj_2015_b]\] \[[Anderson et al 2015][research_anderson_heister_2015]\] \[[Coogan 2015][research_coogan_2015]\] \[[Dalle, Derek J. and Rogers, Stuart E. 2015][research_dallederekj_rogersstuarte_2015]\] \[[Eberhart, C. J. et al 2015][research_eberhartcj_snellgrovelm_2015]\] \[[Piatak, David J. et al 2015][research_piatakdavidj_sekulamartink_2015]\] \[[Pinier, Jeremy T. et al 2015][research_pinierjeremyt_ericksongarye_2015]\] \[[Qu and Yang 2015][research_qu_yang_2015]\] \[[Rogers, Stuart E. et al 2015][research_rogersstuarte_dallederekj_2015]\] \[[Sekula, Martin K. et al 2015][research_sekulamartink_piatakdavidj_2015]\] \[[Son and Sohn 2015][research_son_sohn_2015]\] \[[Stefanski, Philip L. 2015][research_stefanskiphilipl_2015]\] \[[VanZwieten, Tannen S. et al 2015][research_vanzwietentannens_gilliganerict_2015]\] \[[Wall, John H. et al 2015][research_walljohnh_vanzwietentannens_2015]\] \[[Wang et al 2015][research_wang_fan_2015]\] \[[Yoda et al 2015][research_yoda_ito_2015]\] \[[Chiba et al 2016][research_chiba_kanazaki_2016]\] \[[Dalle, Derek J. et al 2016][research_dallederekj_rogersstuarte_2016]\] \[[Emrich 2016][research_emrich_2016]\] \[[Emrich 2016][research_emrich_2016_b]\] \[[Emrich 2016][research_emrich_2016_c]\] \[[Favaregh, Amber L. et al 2016][research_favareghamberl_houldenheatherp_2016]\] \[[Gradl, Paul 2016][research_gradlpaul_2016]\] \[[Gradl, Paul R. 2016][research_gradlpaulr_2016]\] \[[Gradl, Paul R. 2016][research_gradlpaulr_2016_b]\] \[[Gradl, Paul R. and Schmidt, Tim 2016][research_gradlpaulr_schmidttim_2016]\] \[[Hemsch, Michael J. 2016][research_hemschmichaelj_2016]\] \[[Herron, Andrew J. et al 2016][research_herronandrewj_crosbywilliama_2016]\] \[[Honeycutt, John and Lyles, Garry 2016][research_honeycuttjohn_lylesgarry_2016]\] \[[Johnson, Katie 2016][research_johnsonkatie_2016]\] \[[Kanazaki et al 2016][research_kanazaki_ito_2016]\] \[[Lohrer, J. D. and Wright, R. D. 2016][research_lohrerjd_wrightrd_2016]\] \[[Mehta, Manish et al 2016][research_mehtamanish_knoxkyle_2016]\] \[[Numerical Method and Simulations 2016][research_numerical_method_2016]\] \[[Piatak, David J. et al 2016][research_piatakdavidj_sekulamartink_2016]\] \[[Priskos, Alex 2016][research_priskosalex_2016]\] \[[Stahl, H. Philip et al 2016][research_stahlhphilip_hopkinsrandallc_2016]\] \[[Zhang 2016][research_zhang_2016]\] \[[Askins, Bruce and Robinson, Kimberly F. 2017][research_askinsbruce_robinsonkimberlyf_2017]\] \[[Civek and Özgören 2017][research_civek_ozgoren_2017]\] \[[Clayton, J. Louie 2017][research_claytonjlouie_2017]\] \[[Clayton, J. Louie 2017][research_claytonjlouie_2017_b]\] \[[Cook, Jerry and Lyles, Garry 2017][research_cookjerry_lylesgarry_2017]\] \[[Du 2017][research_du_2017]\] \[[McCutcheon, David Matthew 2017][research_mccutcheondavidmatthew_2017]\] \[[Statham, Tamara and Thompson, Seth 2017][research_stathamtamara_thompsonseth_2017]\] \[[Tannen S Vanzwieten et al 2017][research_tannensvanzwieten_michaelrhannan_2017]\] \[[Wernet, Mark P. and Stiegemeier, Benjamin R. 2017][research_wernetmarkp_stiegemeierbenjaminr_2017]\] \[[Zhu et al 2017][research_zhu_tian_2017]\] \[[Al Hassan, Mohammad and Britton, Paul 2018][research_alhassanmohammad_brittonpaul_2018]\] \[[Aso and Tani 2018][research_aso_tani_2018]\] \[[Aso and Tani 2018][research_aso_tani_2018_b]\] \[[Borowski, Stanley K. et al 2018][research_borowskistanleyk_ryanstephenw_2018]\] \[[Brown, Andrew M. et al 2018][research_brownandrewm_delessiojenniferl_2018]\] \[[Chen and Wu 2018][research_chen_wu_2018]\] \[[Fernandez, Rene et al 2018][research_fernandezrene_riddlebaughjeff_2018]\] \[[Gradl, Paul R. et al 2018][research_gradlpaulr_brandsmeierwill_2018]\] \[[Greatrix 2018][research_greatrix_2018]\] \[[Jung 2018][research_jung_2018]\] \[[Kang et al 2018][research_kang_wang_2018]\] \[[Liquid Rocket Engine Thrust 2018][research_liquid_rocket_2018]\] \[[Matveev et al 2018][research_matveev_zubanov_2018]\] \[[Nardi Rezende 2018][research_nardirezende_2018]\] \[[Novozhilov et al 2018][research_novozhilov_marshakov_2018]\] \[[Shea, Patrick R. et al 2018][research_sheapatrickr_pinierjeremyt_2018]\] \[[Xiong 2018][research_xiong_2018]\] \[[Zhang et al 2018][research_zhang_tian_2018]\] \[[Zhang et al 2018][research_zhang_bi_2018]\] \[[Chan, David T. et al 2019][research_chandavidt_paulsonjohnw_2019]\] \[[Chen 2019][research_chen_2019]\] \[[Garbeff, Theodore J., II 2019][research_garbefftheodorejii_2019]\] \[[Hybrid Rocket Engines 2019][research_hybrid_rocket_2019]\] \[[Katsarelis, Colton et al 2019][research_katsareliscolton_chenpo_2019]\] \[[Liquid Rocket Engines 2019][research_liquid_rocket_2019]\] \[[Piotr et al 2019][research_piotr_karol_2019]\] \[[Podolchak 2019][research_podolchak_2019]\] \[[Rocket Nozzle Performance 2019][research_rocket_nozzle_2019]\] \[[Rocket Propulsion Classification of 2019][research_rocket_propulsion_2019]\] \[[Solid Rocket Motors 2019][research_solid_rocket_2019]\] \[[Statham, T. L. et al 2019][research_stathamtl_steinwb_2019]\] \[[Steven E Krist et al 2019][research_stevenekrist_nalinaratnayake_2019]\] \[[Tarifa and Pizzuti 2019][research_tarifa_pizzuti_2019]\] \[[Velez-Justiniano, Yo-Ann et al 2019][research_velezjustinianoyoann_stefanskiphilipl_2019]\] \[[Zhang et al 2019][research_zhang_wang_2019]\] \[[Akers, James C. and Sills, Joel W., Jr. 2020][research_akersjamesc_sillsjoelwjr_2020]\] \[[Alexis J Harroun et al 2020][research_alexisjharroun_stephendheister_2020]\] \[[Kawasaki et al 2020][research_kawasaki_yokoo_2020]\] \[[Nalin A Ratnayake et al 2020][research_nalinaratnayake_stevenekrist_2020]\] \[[Nicklaus O. Richardson et al 2020][research_nicklausorichardson_edmondwong_2020]\] \[[Paulson et al 2020][research_paulson_kimura_2020]\] \[[Roozeboom, Nettie H. et al 2020][research_roozeboomnettieh_powelljessie_2020]\] \[[Sudiana 2020][research_sudiana_2020]\] \[[Yang and Naraghi 2020][research_yang_naraghi_2020]\] \[[Basharina et al 2021][research_basharina_goncharov_2021]\] \[[Burr and Paulson 2021][research_burr_paulson_2021]\] \[[Darren C Tinker 2021][research_darrenctinker_2021]\] \[[Gieras and Gorgeri 2021][research_gieras_gorgeri_2021]\] \[[Gloger et al 2021][research_gloger_lettieri_2021]\] \[[Kato et al 2021][research_kato_yamada_2021]\] \[[Lederer 2021][research_lederer_2021]\] \[[Paxson and Perkins 2021][research_paxson_perkins_2021]\] \[[Reynolds et al 2021][research_reynolds_kokan_2021]\] \[[Trumpour 2021][research_trumpour_2021]\] \[[Tudor et al 2021][research_tudor_wang_2021]\] \[[Velliaris 2021][research_velliaris_2021]\] \[[D. et al 2022][research_d_b_2022]\] \[[Launch Vehicle Performance and 2022][research_launch_vehicle_2022_b]\] \[[Launch Vehicle Systems and 2022][research_launch_vehicle_2022]\] \[[Patil 2022][research_patil_2022]\] \[[Rocket Propulsion 2022][research_rocket_propulsion_2022]\] \[[Srivastava and Thakur 2022][research_srivastava_thakur_2022]\] \[[Zachary Muckler 2022][research_zacharymuckler_2022]\] \[[Zhang et al 2022][research_zhang_wang_2022]\] \[[Abdala et al 2023][research_abdala_burden_2023]\] \[[Chandler 2023][research_chandler_2023]\] \[[D. et al 2023][research_d_m_2023]\] \[[Emrich 2023][research_emrich_2023]\] \[[Emrich 2023][research_emrich_2023_b]\] \[[Emrich 2023][research_emrich_2023_c]\] \[[Francesco Soranna et al 2023][research_francescosoranna_patricksheaney_2023]\] \[[Gangeh et al 2023][research_gangeh_bui_2023]\] \[[Lin et al 2023][research_lin_yang_2023]\] \[[Malik et al 2023][research_malik_salauddin_2023]\] \[[Nagappa 2023][research_nagappa_2023]\] \[[Ortega et al 2023][research_ortega_amador_2023]\] \[[Zapata et al 2023][research_zapata_roncero_2023]\] \[[Abbas 2024][research_abbas_2024]\] \[[Brent Pomeroy et al 2024][research_brentpomeroy_stevenkrist_2024]\] \[[Damane and Pitot 2024][research_damane_pitot_2024]\] \[[DiZinno et al 2024][research_dizinno_reeves_2024]\] \[[Huang et al 2024][research_huang_cheng_2024]\] \[[Huang et al 2024][research_huang_cheng_2024_b]\] \[[Jha 2024][research_jha_2024]\] \[[Jin et al 2024][research_jin_shang_2024]\] \[[Karen A. Deere et al 2024][research_karenadeere_stevenekrist_2024]\] \[[Kibbey 2024][research_kibbey_2024]\] \[[Michael J Hays et al 2024][research_michaeljhays_jenniferrrobinson_2024]\] \[[Mundt et al 2024][research_mundt_knowlen_2024]\] \[[P et al 2024][research_p_p_2024]\] \[[Traudt 2024][research_traudt_2024]\] \[[Zhao et al 2024][research_zhao_yu_2024]\] \[[Atamanchuk 2025][research_atamanchuk_2025]\] \[[Borgna et al 2025][research_borgna_fusaro_2025]\] \[[Charan and Tibrewal 2025][research_charan_tibrewal_2025]\] \[[Chen et al 2025][research_chen_wang_2025_b]\] \[[Fang et al 2025][research_fang_li_2025]\] \[[Ganesan et al 2025][research_ganesan_subburayan_2025]\] \[[Huang et al 2025][research_huang_cheng_2025]\] \[[Hyde and Argueta 2025][research_hyde_argueta_2025]\] \[[Matthew Aaron Maybee 2025][research_matthewaaronmaybee_2025]\] \[[Petrenko 2025][research_petrenko_2025]\] \[[Shyam Raj et al 2025][research_shyamraj_parthasarathy_2025]\] \[[Sá Gontijo et al 2025][research_sagontijo_filho_2025]\] \[[Wang et al 2025][research_wang_cao_2025]\] \[[Callsen et al 2026][research_callsen_herberhold_2026]\] \[[Drobyshev 2026][research_drobyshev_2026]\] \[[Guenther et al 2026][research_guenther_compton_2026]\] \[[Lee 2026][research_lee_2026]\] \[[Noland et al 2026][research_noland_sanders_2026]\] \[[Pallela et al 2026][research_pallela_thakur_2026]\] \[[Seo and Kim 2026][research_seo_kim_2026]\] \[[Sukachevskyi 2026][research_sukachevskyi_2026]\] \[[Yu et al 2026][research_yu_campbell_2026]\] \[[3D printing of large][research_3d_printing]\] \[[A. S. Craig et al][research_ascraig_mjhawkins]\] \[[Andrew M Brown][research_andrewmbrown]\] \[[Anthony Scott Craig et al][research_anthonyscottcraig_jaydenehauglie]\] \[[Benjamin S Burger et al][research_benjaminsburger_caroleaddona]\] \[[Brandon L Mobley and Samantha Summers][research_brandonlmobley_samanthasummers]\] \[[Brent W Pomeroy et al][research_brentwpomeroy_stevenekrist]\] \[[Brevault][research_brevault]\] \[[Brian R. Richardson][research_brianrrichardson]\] \[[Camargo][research_camargo]\] \[[Daniel E Paxson et al][research_danielepaxson_kenjimiki]\] \[[David Chan et al][research_davidchan_patrickshea]\] \[[Devin Johnson et al][research_devinjohnson_venkatathmanathan]\] \[[Dorairajan][research_dorairajan]\] \[[Francesco Soranna et al][research_francescosoranna_patricksheaney]\] \[[Francesco Soranna et al][research_francescosoranna_patricksheaney_b]\] \[[Gibart][research_gibart]\] \[[Glaser][research_glaser]\] \[[Grondin][research_grondin]\] \[[H. Douglas Perkins][research_hdouglasperkins]\] \[[James M Ramey et al][research_jamesmramey_ianmgiles]\] \[[Jamie G. Meeroff et al][research_jamiegmeeroff_derekjdalle]\] \[[Jeremy T Pinier][research_jeremytpinier]\] \[[Joseph Hernandez-McCloskey et al][research_josephhernandezmccloskey_sethareutlinger]\] \[[Justin G. Chen et al][research_justingchen_raulrios]\] \[[Launch Vehicle Systems][research_launch_vehicle]\] \[[Lauren Griggs et al][research_laurengriggs_jacobmoseley]\] \[[Lin][research_lin]\] \[[Liquid Rocket Engine Reliability][research_liquid_rocket]\] \[[Lowe][research_lowe]\] \[[M.J. Cooper et al][research_mjcooper_depaxson]\] \[[Manish Mehta et al][research_manishmehta_markahooton]\] \[[Manish Mehta et al][research_manishmehta_andrewcolbert]\] \[[Matthew A Maybee et al][research_matthewamaybee_michaelahemming]\] \[[Michael Cooper][research_michaelcooper]\] \[[Michael James Hays et al][research_michaeljameshays_jenniferrrobinson]\] \[[Michael Lee et al][research_michaellee_derekdalle]\] \[[Patrick R Shea et al][research_patrickrshea_davidtchan]\] \[[Patrick S Heaney et al][research_patricksheaney_francescosoranna]\] \[[Patrick S. Heaney et al][research_patricksheaney_djpiatak]\] \[[Paul Gradl et al][research_paulgradl_chrisprotz]\] \[[Po-Shou Chen et al][research_poshouchen_benjaminlloydrupp]\] \[[Pourya Nikoueeyan et al][research_pouryanikoueeyan_michaeldhind]\] \[[Rekesh Ali et al][research_rekeshali_caroleaddona]\] \[[Rekesh M Ali et al][research_rekeshmali_carolejaddona]\] \[[Richard K. Moore et al][research_richardkmoore_johnhwall]\] \[[Sarotte][research_sarotte]\] \[[Seetha A Kolli][research_seethaakolli]\] \[[Space systems � Measured][research_space_systems]\] \[[Steve Hahn et al][research_stevehahn_nathanlunetta]\] \[[T J Wignall][research_tjwignall]\] \[[T J Wignall et al][research_tjwignall_morganawalker]\] \[[T.J. Wignall et al][research_tjwignall_jessegcollins]\] \[[The thermal rocket engine][research_the_thermal]\] \[[Thomas Teasley et al][research_thomasteasley_dillonpetty]\] \[[Thomas Teasley et al][research_thomasteasley_dillonpetty_b]\]

## Where the Framing Breaks Down

**The vehicle is two published numbers and this article has built a great deal on them.** A height of about 12 metres and a diameter of about 2.4 metres, both approximate, both reported at second hand from a release this article could not retrieve. **Every geometric conclusion here inherits that provenance**, including the fineness ratio, the frontal-area comparison and the static-margin argument. If either figure is wrong by twenty percent the fineness ratio moves by a quarter and the ordering against the sibling vehicle survives, which is the only robustness claim worth making.

**The error budget is a structure and not a prediction.** It says how the uncertainty in recovered thrust depends on the drag fraction and the drag-model accuracy. **It cannot say what the drag fraction was**, because that needs the vehicle's mass, its drag coefficient and its thrust, none of which is public, and the budget is therefore presented as a function of the quantity it cannot evaluate.

**The accelerometer identity assumes zero angle of attack** and says so where it is derived, but the error budget does not carry a term for the departure. A gravity turn flies at small angle of attack by design, so the omission is small and it is not zero.

**The three errors are treated as independent and they are not.** A mass bookkeeping error and a thrust error share a cause if the propellant flow measurement is the source of both, and an accelerometer's scale-factor error is correlated across the whole flight rather than random in time. **Root-sum-square is the right first move and the wrong last one**, and a real uncertainty analysis for this experiment would carry a covariance matrix that this article does not have.

**The sampling result assumes the sensors are equally spaced and that the field is a function of angle alone.** An unequally spaced ring has different aliasing and generally better, which is why unequal spacing is a standard remedy. A field varying along the annulus and across it needs a two-dimensional treatment. **The four-lobed claim also assumes the legs are the dominant azimuthal feature**, and a real vehicle has umbilicals, seams and one more of whatever the plumbing requires.

**The telemetry arithmetic uses plausible channel counts and a plausible link capacity, and neither is published for either ARISE vehicle.** The rates and volumes scale linearly in the assumed channel count and sample rate, and the deficit scales inversely in the assumed link capacity. **The conclusion that survives those assumptions is that the deficit is a factor of tens rather than a factor of two**, which holds across the whole one to twenty megabit span, and the specific factor does not survive them at all.

**And the recovery inference is the weakest thing here.** That a recoverable vehicle solves a bandwidth problem is arithmetic. **That the bandwidth problem is why the vehicle is recoverable is a guess about intent**, and the programme's own stated interest in reusability for its own sake is at least as good an explanation.

## The Source Base

### The Pool

**One sweep retrieved 23,960 records of which 23,824 were distinct.** The shared rejection store removed 1,439. The subject gate admitted 4,087 and refused 18,298. A further 33 definitions are hand-written primary documents and encyclopaedic anchors, and 64 are back-references to earlier articles in this series.

By source the admitted set is 2,236 from the journal and conference index, 1,670 from the national reports server and 181 from the defence technical registry. **This is the first article in this series whose reports-server return was correct on its first run.** [The previous article][related_post_a360_abl_space_systems_x63] found that the shared fetcher passed its page specification as a single encoded object, which that server clamps to ten records while silently ignoring the offset inside it, so every article before it read one page of every question it asked. **The repair is a parameter spelling, it is held by a test that runs offline against a fake transport, and A361 inherits it rather than discovering it.**

### What the Reports Server Was Asked, and What It Holds

**The server reports its own total against every question, so the coverage of this sweep is a measurement rather than an assumption.** Across 94 questions it reported **30,011 matching records** and returned **15,191**, which is 50.6 percent.

**That average hides a split and the split is the useful figure.** **76 of the 94 questions were taken to the bottom**, holding 8,563 records between them and returning all 8,563, which is 100.0 percent. The remaining 18 hit **this article's own walk limit of 400 rather than the server's**, holding 21,448 and returning 6,628. **Every one of the 14,820 records not taken belongs to those 18 questions**, and the broadest of them is `data acquisition system`, which holds 3,611 on its own.

**The same measurement cannot be made of the bibliographic index and this article does not pretend otherwise.** That index performs a ranked retrieval against everything it holds rather than a boolean match against a curated collection, so a total it reports is not a count of records that match. **A coverage figure is only worth quoting where the denominator is a match count.**

### The Homonyms, Measured Before the Sweep Was Written

**46 terms were put to the bibliographic index before a single query was composed**, because the vocabulary of measurement belongs to every field that measures. **This article's collisions are worse than its predecessor's and they are worse in a different way.** A360's central nouns were owned by other fields; A361's are owned by other languages and by other species.

**`fin` returns `Fin de siecle, fin d'un monde` four times over**, and `fins` returns `Les fins de traitement` and the fins of a fossil fish called *Robustichthys*. **The word for this vehicle's own stabilising surfaces is owned by French and by ichthyology.** `static margin` is owned by static noise margin in six-transistor static memory cells, so **the aerodynamic stability metric is buried under a semiconductor one**. `tip-over stability` returns wheeled and tracked mobile manipulators in every one of ten results. `reusability` is software reusability, program transformations and the STARS guidelines. `recovery` is heat-recovery ventilators and a recovery room. `aliasing` and `Nyquist` are dictionary headwords. `transducer` is ultrasonics and an IEEE interface standard.

**And the author of the method every model rocketeer uses returns nothing.** `Barrowman` gives context-aware random numbers, a book on reading the short story, and gastrointestinal lymphatics twice. **A method that circulated as a report and a handbook rather than as a paper has no presence in an index of papers**, which is a fact about the index and not about the method.

**One term measured clean and on subject, which was not expected.** `landing legs` returns leg design for propulsive rocket landing and landing simulations for reusable launch vehicles, both recent and both exactly this article's question. **The live literature on this vehicle's most distinctive feature is findable under its plainest name.**

**2 terms return nothing at all**, being `Invocon`, `Troy7`. **That is a measurement about this team rather than a failure of the probe**, and it is the reason this article is built on an award record and a register rather than on a publication record.

### The Store, and Which Families Were Opened

**A family is opened against records and never against its name**, so the cost of each candidate was measured on this pool before anything was switched off. 12 families were measured.

- `missiles` releases 312 records from this pool, 42 of which the subject gate would admit. It is **opened**.
- `hypersonics` releases 830 records from this pool, 148 of which the subject gate would admit. It is **opened**.
- `ramjet` releases 74 records from this pool, 16 of which the subject gate would admit. It is **left armed**.
- `ndt` releases 1 records from this pool, 1 of which the subject gate would admit. It is **left armed**.
- `civil-structures` releases 4 records from this pool, 3 of which the subject gate would admit. It is **left armed**.
- `composites` releases 13 records from this pool, 0 of which the subject gate would admit. It is **left armed**.
- `delamination` releases 1 records from this pool, 0 of which the subject gate would admit. It is **left armed**.
- `fracture` releases 11 records from this pool, 2 of which the subject gate would admit. It is **left armed**.
- `cost-estimation` releases 2 records from this pool, 0 of which the subject gate would admit. It is **left armed**.
- `smart-actuators` releases 2 records from this pool, 2 of which the subject gate would admit. It is **left armed**.
- `medicine` releases 103 records from this pool, 6 of which the subject gate would admit. It is **left armed**.
- `ecology` releases 0 records from this pool, 0 of which the subject gate would admit. It is **left armed**.

**The candidate that mattered is `ndt`, and no earlier article in this series had a reason to ask about it.** The lead contractor's own trade is structural health monitoring and hypervelocity impact detection, so a family earned against non-destructive testing literature is a family that could delete this article's `health` cluster wholesale. It releases 1 records here, 1 of which the gate would admit, and the decision recorded above was taken on that number rather than on the name.

**The first version of this list named four families that do not exist in the store.** `robotics`, `semiconductors`, `software` and `medical` are the tags a reader of this article's homonym section would expect, and the store's actual tags are different words. **A tag list is a claim about another file** and the repair was to read that file rather than to guess it.

### What the Award Record Was Asked, and What It Returned

**14 keywords were put to the federal award reporting system across 5 families of award type**, being procurement contracts, indefinite delivery vehicles, grants, direct payments and other financial assistance. **6 of the 14 returned nothing in any family**, and they include `X-64A`, `ARISE aerospike`, `Aerospike Rocket Integration and Suborbital Experiment` and `Affordable Responsive Modular Rocket`. **[The previous article][related_post_a360_abl_space_systems_x63] found the same silence from the other side of the same allocation**, and the announcement explains it, because the instrument was an other transaction agreement and an other transaction does not appear where procurement contracts appear.

**What did return is the three companies' own histories, and they divide the work.** The counts, the identifiers and the dollar figures are in the table above. **The one methodological finding is that `Troy7` returns nothing and `Troy 7` returns fifteen rows**, so a company invisible to a search that spells its name the way its own customer spells it is visible to one that inserts a space. **And the spaced spelling imports a collision the unspaced one avoided**, matching a router backup and a seven-inch rifle rail, so the more findable query is the less precise one and both halves of that trade have to be stated for the count to mean anything.

### Which Clusters Are Thin in Reports, and Why

**The report-primary fraction is 45.0 percent overall and it runs from 16.8 to 100.0 percent across the clusters**, which is a spread wide enough that a single figure would hide the interesting part. **[The X-63A article][related_post_a360_abl_space_systems_x63] established the test that explains such a spread**, which is to ask which publisher holds each thin cluster rather than to treat thinness as a shortfall of effort.

| Cluster | Records | Report primaries | Fraction | Median year | Largest single source |
|---|---|---|---|---|---|
| `recovery` | 518 | 87 | 16.8 percent | 2006 | doi:2514, 194 |
| `sampling` | 143 | 25 | 17.5 percent | 2015 | reports server, 25 |
| `health` | 167 | 41 | 24.6 percent | 2013 | defence registry, 22 |
| `uncertainty` | 210 | 57 | 27.1 percent | 2016 | reports server, 52 |
| `control` | 75 | 21 | 28.0 percent | 2011 | doi:2514, 20 |
| `fins` | 144 | 54 | 37.5 percent | 1997 | doi:2514, 58 |
| `sensors` | 238 | 100 | 42.0 percent | 2001 | reports server, 90 |
| `trajectory` | 165 | 73 | 44.2 percent | 1998 | reports server, 66 |
| `aerospike` | 294 | 133 | 45.2 percent | 2004 | reports server, 133 |
| `aero_shape` | 190 | 86 | 45.3 percent | 1983 | reports server, 66 |
| `prop_general` | 760 | 411 | 54.1 percent | 1997 | reports server, 320 |
| `modular` | 9 | 5 | 55.6 percent | 1996 | reports server, 3 |
| `measurement` | 181 | 105 | 58.0 percent | 2005 | reports server, 101 |
| `data_systems` | 742 | 527 | 71.0 percent | 1990 | reports server, 478 |
| `named` | 1 | 1 | 100.0 percent | 2005 | reports server, 1 |

**The answer is that the thin clusters belong to other publishers and the rich ones belong to government laboratories.** The thinnest three are `recovery` at 16.8 percent, `sampling` at 17.5 percent, `health` at 24.6 percent, and the largest single source in each is doi:2514 for `recovery`, reports server for `sampling`, defence registry for `health`. **Sampling and array processing are an institute-of-electrical-engineers literature, recovery and reusability are a conference literature, and structural health monitoring is a commercial-journal literature.** None of the three is a subject government laboratories wrote report series about.

**The richest cluster is the one this team's own trade sits in.** `data_systems` reaches 71.0 percent, with 478 of its records served by the reports server, and `measurement` reaches 58.0 percent. **Telemetry, data acquisition and in-flight performance determination are subjects the space agency and the services documented in report series for forty years**, which is why this article's primary fraction is high where its predecessor's was low.

**And the median years say the same thing from the other direction.** `data_systems` has a median year of 1990 and `sampling` has 2015, a gap of 25 years. **The report literature this article draws on is old and the journal literature is recent**, so a high primary fraction and a recent median are in tension by construction rather than by any choice made here.

### What This Article Read in Full

**Six primary documents were retrieved, saved and read end to end**, and every quotation in this article comes from one of them. They are the laboratory's background document on its rocket propulsion organisation, cleared in September 2022; the award announcement as reprinted verbatim by the base newspaper; the encyclopedia entry for this designation; and the parent vehicle's payload user's guide, which [the previous article][related_post_a360_abl_space_systems_x63] read and which supplies the reference trajectory and the comparison dimensions. **The two the primary-reference pass added are the 1967 report that is the centre-of-pressure method every later treatment rests on, whose equation 3-66 gives the body normal-force derivative this article displays, and the 1951 study of viscosity on slender inclined bodies that shows the inviscid figure to be a floor.** **Four further primaries are cited from their abstracts alone and that is said where they are used.** The reports server offers no document for the two reviews of in-flight thrust determination, for the uncertainty methodology, or for the XB-70 drag measurement, so what this article quotes from them is what their abstracts state. **An abstract is a primary statement of a paper's own claims and it is not the paper**, and the distinction is kept because the methodology criticism this article makes of its own budget rests on a list of categories an abstract enumerates rather than on the treatment behind it. **The contractor's own release about the contract award was not retrieved.** The live company site no longer carries it and the archive returned no capture, so the vehicle's dimensions and its four legs are cited at second hand from the entry that names that release as its source, and **every geometric conclusion in this article inherits that provenance**.

**The laboratory's background document is a primary this series had not used, and it was found through the encyclopedia entry's own source list rather than through any sweep.** No query in this article's 94 reports-server questions, 26 defence registry questions or 46 index questions would have returned it, because it is a public-affairs document on a laboratory web site and not a report with an identifier. **A source list at the foot of a secondary is a retrieval channel**, and it is the channel that produced the sentence this article is built on.

## Epistemic State

**Facts, taken from primary documents and stated as they appear there.** The designation, its allocation date of 20 April 2022, the three contractor names, the sponsor cell, the engines cell and the description identical to the X-63A's come from the register \[[DOD 4120.15-L Addendum][ref_mds_addendum]\]. That each company has its own launch vehicle and chosen approach, that ABL's vehicle is the X-63 and Invocon's the X-64, that the arrangement is a public private partnership, that the portfolio seeks a seventy percent reduction in development time and a fifty percent reduction in cost, and the dates and goals of the predecessor programmes come from the laboratory's background document \[[AFRL's Rocket Lab Past, Present and Future][ref_rocketlab]\]. The December 2019 award date, the three-year term, the other transaction instrument, the scope wording including `highly instrumented`, the description of the lead contractor as a veteran-owned small business providing turnkey instrumentation, the naming of the two subcontractors and the quotation from the company's president come from the award announcement \[[AFRL awards agreements under ARISE][ref_arise_award]\]. The parent vehicle's dimensions and reference mission come from its payload user's guide \[[ABL Payload User's Guide][ref_abl_pug]\]. **The award counts, the award identifiers, the dollar figures and the difference between the spellings `Troy7` and `Troy 7` were read from the federal award reporting system** \[[USAspending][ref_usaspending]\].

**Reported at second hand, and said to be.** The vehicle's height of about 12 metres, its diameter of about 2.4 metres, its recoverability and its four legs functioning as stabilising fins are reported by the encyclopedia entry, which names the contractor's own release as its source \[[Invocon X-64][ref_ds_x64]\]. **This article did not retrieve that release.** The live company site no longer carries it and the archive returned no capture. Every geometric conclusion in this article rests on those two figures at one remove.

**Four further sources are used from their abstracts alone.** The reports server offers no document for the two reviews of in-flight thrust determination, for the uncertainty methodology, or for the XB-70 drag measurement \[[In-flight thrust determination][ref_thrust_determination]\] \[[Uncertainty of in-flight thrust determination][ref_thrust_uncertainty]\] \[[Uncertainty methodology][ref_thrust_methodology]\] \[[Techniques for determining propulsion system forces][ref_propulsion_forces]\]. **What this article quotes from them is what their abstracts state.** That matters most for the criticism this article makes of its own error budget, which rests on a list of categories an abstract enumerates rather than on the treatment behind it. **And the two statements of the sampling theorem are cited without being read** \[[Shannon 1949][ref_shannon_1949]\] \[[Nyquist 1928][ref_nyquist_1928]\], the second of them from a later reprint rather than the 1928 original.

**Two primaries were read in full and both bear on a displayed relation.** The 1967 report gives the body normal-force coefficient derivative in subsonic flow as twice the ratio of the nose base area to the reference area, and requires the body to be free of discontinuities in cross-sectional area, which is why a constant-diameter cylinder contributes nothing \[[Barrowman 1967][ref_barrowman]\]. The 1951 study shows the measured normal force exceeding the potential-flow value, so the inviscid figure is a floor \[[Allen and Perkins 1951][ref_allen_perkins]\]. **Its scan is of poor quality and nothing is quoted from it verbatim.**

**One limitation of this article's central apparatus, stated because the established methodology names it.** The error budget treats three contributions as independent random terms combined in quadrature. **The methodology the in-flight thrust field settled on separates bias from precision and carries a model bias error term**, and a drag model's error is far more likely to be systematic than random because it comes from a wrong shape assumption rather than from noise \[[Uncertainty methodology][ref_thrust_methodology]\]. **So what this article presents is a sensitivity analysis and not an uncertainty statement.** It says correctly how the answer's sensitivity to each input scales, and it does not say what the uncertainty of a real measurement would have been. **A single demonstrator flight is also a single-sample experiment in the technical sense** \[[Moffat 1982][ref_moffat_1982]\], so precision estimated from repetition is unavailable to it by construction.

**Derivations, which follow from the facts by mathematics and are checked numerically.** That an accelerometer measures thrust minus drag over mass and is blind to gravity is exact. The error budget for $F = m a_s + D$ is exact given independence. The condition $v^2 \sin \gamma = 2 H_\rho \, \mathrm{d}v / \mathrm{d}t$ for peak dynamic pressure is exact for any atmosphere and trajectory, and **was checked at the computed peak of five profiles to 4.5 parts in a million**. The closed form for the density scale height was checked against a numerical difference of the density profile to better than two parts in a thousand million, and reduces exactly to the pressure scale height in an isothermal layer. The footprint anisotropy $1 / \cos(\pi / N)$ is exact. That harmonic $N$ sampled at $N$ equally spaced points has the discrete mean of harmonic zero is exact for every phase. **The static-margin consequence of fineness ratio is arithmetic on two published lengths.**

**Quantities that depend on assumptions, with the assumptions swept and the spread reported.** The ascent is a speed power law and a pitch program with the published cut-off altitude as a constraint, and across five speed exponents the peak dynamic pressure runs from 45.9 to 92.2 kilopascal at 25.0 to 70.3 seconds and 7.9 to 11.0 kilometres. The half-signal time runs from 11.9 to 28.3 seconds and the fraction of the pressure-time integral collected before the dynamic-pressure peak from 83.6 to 95.3 percent. The instrument floor of the error budget runs from 0.54 to 2.24 percent across three instrument-quality cases. **The drag fraction itself is not computed, because the mass is not public**, and the budget is stated as a function of it. **The instrumentation channel count, sample rate and telemetry capacity are likewise assumed and not published**, so the data-rate arithmetic is quoted as a span and its conclusion is the order of the deficit rather than its value.

**Inferences, marked as such where they appear.** That the recoverability serves data return. That the four legs impose a leading azimuthal harmonic equal to their count. That the programme has ended. That the two vehicles' results cannot be differenced because their drag models are not common terms. **None of these is stated as a fact anywhere in this article and each is reversible by one document.**

**Two conflicts in the sources are recorded and not resolved.** The laboratory's background document writes `into the 22nd century` twice where it means the twenty-first. And it names nitrogen tetroxide with Aerozine 50 in one sentence and nitrogen tetroxide with monomethylhydrazine in the next, which are different fuels, the Titan II having burned the first.

**One dateline limit.** This article is dated 9 December 2025. **The contractor's own web pages were read after that date** and are cited for what the company says it does. The encyclopedia entry was last revised on 11 August 2024, which is before the dateline. **No statement in the body depends on anything the company published after the dateline**, and the description of its current business is used only to observe that it does not list a launch vehicle, which was equally true in 2024 on the evidence of the award record.

**What is not known and would change things.** The vehicle's mass, thrust and drag coefficient. The channel count, sample rates and sensor placement of the instrumentation, and in particular the number of sensors on the annulus. The leg reach and the centre-of-mass height. The dollar value of the agreement. Whether any hardware was built. And whether the four legs were ever more than a rendering. **The encyclopedia entry credits two images, one to the laboratory and one to the contractor, and the one it captions is of a three-dimensional printed model** \[[Invocon X-64][ref_ds_x64]\]. **No photograph of flight hardware is identified as such in any source consulted**, which is weaker than saying none exists and is as far as the record goes.

## Out of Scope

**The aerospike nozzle itself belongs to [the previous article][related_post_a360_abl_space_systems_x63].** The conjugacy of ambient pressure and exit area, the Legendre structure of the ideal spike's thrust curve, the Bregman divergence that is a fixed nozzle's loss, the mean-in-time rule that chooses an exit area, the separation criterion and the three wake regimes are derived there and used here as given.

**The internal aerodynamics of the plug and the design of the fins are not treated.** Both need contours that are not public.

**The landing dynamics are not treated.** This article computes a static tip-over condition. A real landing is an impact with stroke, damping and a horizontal velocity component, and the legs are shock absorbers as well as a footprint.

**The descent trajectory is not treated at all.** How a vehicle of fineness five gets from cut-off back to a controlled vertical landing is a larger problem than the ascent this article models, and nothing in the record describes the intended method.

**No estimate is offered of whether the programme was worth its price.** The price is not public.

## Conclusion

**The register gives two vehicles one description, and the laboratory that paid for both says they are two designs by two teams.** Everything in this article follows from taking the laboratory at its word.

**The X-64A's team is an instrumentation house leading a propulsion house and a control house.** Eighty-one award rows for wireless instrumentation, impact detection and radiation monitoring. Fifteen for segmented and radially segmented launch vehicles, and this company holds every one of the seven rows the phrase `segmented launch vehicle` returns in the whole record. And fifteen more for hypersonic control, findable only if the company's name is spelled with a space its own customer omits. **A name is a query and a query is only as good as its spelling**, which is the same lesson a page parameter taught the article on the sibling designation in a different register.

**The vehicle is two published numbers and they say it was shaped to come back.** About 12 metres by about 2.4 gives a fineness ratio of about five against its sibling's 14.67, so its frontal area is 1.72 times as large and **one calibre of static margin costs it 20 percent of its own length against 6.8 percent for the other vehicle.** Those are the proportions of a lander, and the four legs that are fins on the way up are the aerodynamic surface a short vehicle needs put where the ground is.

**And the problem has a literature this article had to be told about rather than finding on its own.** Determining thrust in flight is a settled discipline, and its own review says in as many words that in-flight thrust is not measured but calculated from models of direct measurements \[[Uncertainty of in-flight thrust determination][ref_thrust_uncertainty]\]. **That literature is about air-breathing engines, where an inlet captures a momentum flux no body-mounted instrument can separate from drag**, which is why its method is gas-path modelling and why a rocket may use an accelerometer instead. **The inverse was done once in flight**, the XB-70's drag being measured by determining its thrust independently \[[Techniques for determining propulsion system forces][ref_propulsion_forces]\]. **Thrust minus drag is one observable and splitting it always costs a model of one side.**

**The measurement is the half of the ARISE question this vehicle exists to answer, and it turns on one identity.** An accelerometer is blind to gravity, so it reads thrust minus drag over mass, and recovering thrust needs a drag model. **The drag term is the only one no instrument on board can reduce**, it enters the error budget weighted by the drag fraction, and holding it to a tenth of a five percent effect needs a drag model good to 2.65 percent at a drag fraction of one fifth. **No pre-flight drag model of a novel configuration is that good.**

**And yet the experiment works, for a reason that has nothing to do with instruments.** Ambient pressure depends on position while drag depends on position and the square of speed, and a rocket reaches altitude before it reaches speed. **Dynamic pressure peaks 2.10 to 2.48 times later than the moment half the altitude-compensation signal has been collected, and by the time it peaks between 83.6 and 95.3 percent of that signal is already in hand.** The trajectory is the instrument, and the vehicle's shape, which raises the drag fraction by 1.72 on frontal area alone, is working against the one term the timing had already defeated.

**The rest is what a finite number of sensors on a circle can see.** Both phases of azimuthal harmonic $\mu$ need $2\mu + 1$ sensors, so a side load needs three and a four-lobed pattern needs nine. **Harmonic $N$ read by $N$ sensors has exactly the discrete mean of harmonic zero**, which means a four-legged vehicle with four taps on its annulus would report the disturbance of its own legs as a change in the thrust-bearing mean. **The regimes the flight existed to measure are changes in that mean and every sensor count recovers them**, so the undersampled ring answers the programme's question and quietly misattributes everything else.

**The legs on the ground are the same polygon the other article found in the sky.** The ratio of best to worst tip-over direction is $1 / \cos(\pi / N)$, character for character the anisotropy of differential-throttling authority, **exactly the square root of two for four legs and exactly two for three.** The footprint has $N$ sides for every count where the control polygon had $N$ or $2N$, and the difference is a half-plane truncation rather than anything geometric.

**Neither vehicle flew.** One contractor lost two rockets and left the launch business. **The other is still an instrumentation house**, and lists no launch vehicle among its products. **Whether it ever thought of itself as anything else is not something an award record can settle**, and this article does not claim it. The register still carries both numbers, allocated on the same day, with the same hundred and one characters against each, **and it still gives a reader no way to tell that the two machines behind them were never the same machine.**

## References

### Reference

- [ABL Space Systems, RS1 Payload User's Guide, 2022 version 1][ref_abl_pug]
- [Air Force Research Laboratory, ARISE and Fly][ref_afrl_arise]
- [aliasing][ref_aliasing]
- [Allen, H. J., and Perkins, E. W., A Study of Effects of Viscosity on Flow over Slender Inclined Bodies of Revolution, 1951][ref_allen_perkins]
- [Alich, AFRL awards agreements under Aerospike Rocket Integration and Sub-orbital Experiment program, Aerotech News, 14 April 2020][ref_arise_award]
- [Minzner, R. A., Defining constants, equations, and abbreviated tables of the 1975 US Standard Atmosphere, 1976][ref_atm_constants]
- [Barrowman, J. S., The Practical Calculation of the Aerodynamic Characteristics of Slender Finned Vehicles, 1967][ref_barrowman]
- [convex hull][ref_convex_hull]
- [discrete Fourier transform][ref_dft]
- [ABL Space Systems X-63, Directory of U.S. Military Rockets and Missiles, Appendix 4][ref_ds_x63]
- [Invocon X-64, Directory of U.S. Military Rockets and Missiles, Appendix 4][ref_ds_x64]
- [dynamic pressure][ref_dynamic_pressure]
- [Measurement effects on the calculation of in-flight thrust for an F404 turbofan engine, 1989][ref_f404_measurement]
- [fineness ratio][ref_fineness]
- [gravity turn][ref_gravity_turn]
- [Invocon, Incorporated, About Us, read 30 September 2026][ref_invocon_about]
- [Invocon, Incorporated, company site, read 30 September 2026][ref_invocon_home]
- [DOD 4120.15-L Addendum, MDS Designators Allocated After 19 August 1998][ref_mds_addendum]
- [Moffat, R. J., Contributions to the Theory of Single-Sample Uncertainty Analysis, Journal of Fluids Engineering, 1982][ref_moffat_1982]
- [Nyquist, H., Certain Topics in Telegraph Transmission Theory, 1928, cited from the 2002 Proceedings of the IEEE reprint][ref_nyquist_1928]
- [Arnaiz, Techniques for determining propulsion system forces for accurate high speed vehicle drag measurements in flight, 1975][ref_propulsion_forces]
- [Air Force Research Laboratory, AFRL's Rocket Lab Past, Present and Future, cleared September 2022][ref_rocketlab]
- [scale height][ref_scale_height]
- [Shannon, C. E., Communication in the Presence of Noise, Proceedings of the IRE, 1949][ref_shannon_1949]
- [proper acceleration, being what an accelerometer measures][ref_specific_force]
- [support function of a convex set][ref_support_function]
- [In-flight thrust determination, 1986][ref_thrust_determination]
- [Abernethy and Adcock, Uncertainty methodology for in-flight thrust determination, 1984][ref_thrust_methodology]
- [In-flight thrust determination on a real-time basis, 1986][ref_thrust_realtime]
- [Uncertainty of in-flight thrust determination, 1986][ref_thrust_uncertainty]
- [Application of in-flight thrust determination uncertainty, 1984][ref_thrust_uncertainty_app]
- [USAspending.gov, the federal award reporting system][ref_usaspending]
- [U.S. Standard Atmosphere, 1976, 1976][ref_usatm1976]

### Related Post

- [X-Planes: Framing and the Research Aircraft Model][related_post_a297_framing]
- [X-Planes: Bell X-1][related_post_a298_bell_x1]
- [X-Planes: Bell X-2][related_post_a299_bell_x2]
- [X-Planes: Douglas X-3 Stiletto][related_post_a300_douglas_x3]
- [X-Planes: Northrop X-4 Bantam][related_post_a301_northrop_x4]
- [X-Planes: Bell X-5][related_post_a302_bell_x5]
- [X-Planes: Convair X-6][related_post_a303_convair_x6]
- [X-Planes: Lockheed X-7][related_post_a304_lockheed_x7]
- [X-Planes: Aerojet X-8 Aerobee][related_post_a305_aerojet_x8]
- [X-Planes: Bell X-9 Shrike][related_post_a306_bell_x9]
- [X-Planes: North American X-10][related_post_a307_north_american_x10]
- [X-Planes: Convair X-11][related_post_a308_convair_x11]
- [X-Planes: Convair X-12][related_post_a309_convair_x12]
- [X-Planes: Ryan X-13 Vertijet][related_post_a310_ryan_x13]
- [X-Planes: Bell X-14][related_post_a311_bell_x14]
- [X-Planes: North American X-15][related_post_a312_north_american_x15]
- [X-Planes: Bell X-16][related_post_a313_bell_x16]
- [X-Planes: Lockheed X-17][related_post_a314_lockheed_x17]
- [X-Planes: Hiller X-18][related_post_a315_hiller_x18]
- [X-Planes: Curtiss-Wright X-19][related_post_a316_curtiss_wright_x19]
- [X-Planes: Boeing X-20 Dyna-Soar][related_post_a317_boeing_x20]
- [X-Planes: Northrop X-21][related_post_a318_northrop_x21]
- [X-Planes: Bell X-22][related_post_a319_bell_x22]
- [X-Planes: Martin Marietta X-23 PRIME and a Contested Assignment][related_post_a320_martin_marietta_x23]
- [X-Planes: Martin Marietta X-24][related_post_a321_martin_marietta_x24]
- [X-Planes: Bensen X-25][related_post_a322_bensen_x25]
- [X-Planes: Schweizer X-26 Frigate][related_post_a323_schweizer_x26]
- [X-Planes: Lockheed X-27][related_post_a324_lockheed_x27]
- [X-Planes: Osprey X-28 Sea Skimmer][related_post_a325_osprey_x28]
- [X-Planes: Grumman X-29][related_post_a326_grumman_x29]
- [X-Planes: Rockwell X-30 and the National Aero-Space Plane][related_post_a327_rockwell_x30]
- [X-Planes: Rockwell-MBB X-31][related_post_a328_rockwell_mbb_x31]
- [X-Planes: Boeing X-32][related_post_a329_boeing_x32]
- [X-Planes: Lockheed Martin X-33][related_post_a330_lockheed_martin_x33]
- [X-Planes: Orbital Sciences X-34][related_post_a331_orbital_sciences_x34]
- [X-Planes: Lockheed Martin X-35][related_post_a332_lockheed_martin_x35]
- [X-Planes: McDonnell Douglas X-36][related_post_a333_mcdonnell_douglas_x36]
- [X-Planes: Boeing X-37][related_post_a334_boeing_x37]
- [X-Planes: Scaled Composites X-38][related_post_a335_scaled_composites_x38]
- [X-Planes: X-39, Reserved but Never Assigned][related_post_a336_x39_reserved_never_assigned]
- [X-Planes: Boeing X-40][related_post_a337_boeing_x40]
- [X-Planes: X-41 Common Aero Vehicle][related_post_a338_x41_common_aero_vehicle]
- [X-Planes: Orbital Sciences X-42][related_post_a339_orbital_sciences_x42]
- [X-Planes: Micro-Craft X-43 Hyper-X][related_post_a340_micro_craft_x43]
- [X-Planes: X-44, One Designation and Two Aircraft][related_post_a341_x44_two_aircraft]
- [X-Planes: Boeing X-45][related_post_a342_boeing_x45]
- [X-Planes: Boeing X-46][related_post_a343_boeing_x46]
- [X-Planes: Northrop Grumman X-47][related_post_a344_northrop_grumman_x47]
- [X-Planes: Boeing X-48][related_post_a345_boeing_x48]
- [X-Planes: Piasecki X-49 SpeedHawk][related_post_a346_piasecki_x49]
- [X-Planes: Boeing X-50 Dragonfly][related_post_a347_boeing_x50]
- [X-Planes: Boeing X-51 Waverider][related_post_a348_boeing_x51]
- [X-Planes: X-52, the Designation Refused][related_post_a349_x52_designation_refused]
- [X-Planes: Boeing X-53 Active Aeroelastic Wing][related_post_a350_boeing_x53]
- [X-Planes: Gulfstream X-54][related_post_a351_gulfstream_x54]
- [X-Planes: Lockheed Martin X-55 ACCA][related_post_a352_lockheed_martin_x55]
- [X-Planes: Lockheed Martin X-56][related_post_a353_lockheed_martin_x56]
- [X-Planes: ESAero X-57 Maxwell][related_post_a354_esaero_x57_maxwell]
- [X-Planes: X-58, the Slot Taken by XQ-58][related_post_a355_x58_slot_taken_by_xq58]
- [X-Planes: Lockheed Martin X-59 Quesst][related_post_a356_x59_quesst]
- [X-Planes: Generation Orbit X-60][related_post_a357_generation_orbit_x60]
- [X-Planes: Dynetics X-61 Gremlins][related_post_a358_dynetics_x61_gremlins]
- [X-Planes: Lockheed Martin X-62 VISTA][related_post_a359_lockheed_martin_x62_vista]
- [X-Planes: ABL Space Systems X-63][related_post_a360_abl_space_systems_x63]

### Research

- [3D printing of large][research_3d_printing]
- [A Global Optimization Methodology 2001][research_a_global_2001]
- [A hydro-acoustic mode decomposition 2023][research_a_hydro_acoustic_2023]
- [A et al 2024][research_a_sampathkumar_2024]
- [Aaron Pearlman et al 2020][research_aaronpearlman_matthewmontanaro_2020]
- [Abbas 2024][research_abbas_2024]
- [Abbott and Walker 1970][research_abbott_walker_1970]
- [Abbott, Ira H 1937][research_abbottirah_1937]
- [Abdala et al 2023][research_abdala_burden_2023]
- [Abdelwahab, Mahmood et al 1987][research_abdelwahabmahmood_biesiadnythomasj_1987]
- [Abhayapala et al 1999][research_abhayapala_kennedy_1999]
- [Abilleira, Fernando 2013][research_abilleirafernando_2013]
- [Abilleira, Fernando et al 2019][research_abilleirafernando_halsellallen_2019]
- [Abilleira, Fernando et al 2021][research_abilleirafernando_kruizingagerard_2021]
- [Abrahamm and Valsa 2018][research_abrahamm_valsa_2018]
- [Adair, B. M. and Polge, R. J. 1967][research_adairbm_polgerj_1967]
- [Adamovsky, Grigory et al 2014][research_adamovskygrigory_mackeyjeffreyr_2014]
- [Adams et al 1983][research_adams_thompson_1983]
- [Adams et al 1983][research_adams_thompson_1983_b]
- [Adams, G. L. et al 1971][research_adamsgl_bradtaj_1971]
- [Adams, Mac C. 1951][research_adamsmacc_1951]
- [Adaptive compressive telemetry techniques 1966][research_adaptive_compressive_1966]
- [Adaptive telemetry systems Final 1968][research_adaptive_telemetry_1968]
- [Addy 1970][research_addy_1970]
- [Adkins, F. L. and Griffin, C. E. 1962][research_adkinsfl_griffince_1962]
- [Adolphsen, J. W. and Malinowski, A. B. 1964][research_adolphsenjw_malinowskiab_1964]
- [Advanced Ducted Propulsor In-Flight][research_advanced_ducted]
- [Advanced telemetry systems for 1990][research_advanced_telemetry_1990]
- [Advisory Group for Aerospace Research and Development 1979][research_advisorygroupforaerospaceresearchanddevelopment_1979]
- [Aerojet-General Corp Sacramento Ca 1963][research_aerojetgeneralcorpsacramentoca_1963]
- [Aerospike engine][research_aerospike_engine]
- [Aftosmis, Michael J. 2011][research_aftosmismichaelj_2011]
- [Agarwal 2023][research_agarwal_2023]
- [Agarwal 2026][research_agarwal_2026]
- [Agarwalla 2025][research_agarwalla_2025]
- [Ageev and Pavlenko 2016][research_ageev_pavlenko_2016]
- [Agourakis and Agourakis 2026][research_agourakis_agourakis_2026]
- [Aguilar, Robert 1999][research_aguilarrobert_1999]
- [Ahlborn et al 2009][research_ahlborn_blake_2009]
- [Ahlborn and Loehberg 1979][research_ahlborn_loehberg_1979]
- [Ahmad, Mohammad et al 2011][research_ahmadmohammad_tranthanh_2011]
- [Ahmad, Rashid A. and Cash, Stephen F. 2002][research_ahmadrashida_cashstephenf_2002]
- [Ahmed et al 2026][research_ahmed_mishra_2026]
- [Ahmed, Rafiq 1990][research_ahmedrafiq_1990]
- [Ainsleigh et al 1988][research_ainsleigh_george_1988]
- [Air Force Test Pilot School Edwards Afb Ca 1962][research_airforcetestpilotschooledwardsafbca_1962]
- [Aithani et al 2023][research_aithani_shahid_2023]
- [Aji et al 2025][research_aji_agusdian_2025]
- [Ajith et al 2016][research_ajith_s_2016]
- [Ajovalasit 2011][research_ajovalasit_2011]
- [Akbari and Pfaff 2020][research_akbari_pfaff_2020]
- [Akers, James C. and Sills, Joel W., Jr. 2020][research_akersjamesc_sillsjoelwjr_2020]
- [Akhtar et al 2009][research_akhtar_borggaard_2009]
- [Akl and Elattar 2025][research_akl_elattar_2025]
- [Alam et al 2026][research_alam_karim_2026]
- [Alam and Kumar 2018][research_alam_kumar_2018]
- [Alam and Kumar 2018][research_alam_kumar_2018_b]
- [Alam and Kumar 2020][research_alam_kumar_2020]
- [Alam and Kumar 2021][research_alam_kumar_2021]
- [Alam and Pant 2019][research_alam_pant_2019]
- [Al Bakri][research_albakri]
- [AL-Bakri and Kluever 2017][research_albakri_kluever_2017]
- [Albanese et al 2012][research_albanese_meyers_2012]
- [Alexander, Leslie et al 2008][research_alexanderleslie_chapmanjack_2008]
- [Alexis J Harroun et al 2020][research_alexisjharroun_stephendheister_2020]
- [Alghamdi et al 2018][research_alghamdi_nadeem_2018]
- [Al Hassan, Mohammad and Britton, Paul 2018][research_alhassanmohammad_brittonpaul_2018]
- [Alhorn, Dean C. et al 2001][research_alhorndeanc_howarddavide_2001]
- [Ali and Crawford 1988][research_ali_crawford_1988]
- [Ali et al 2016][research_ali_pandey_2016]
- [Ali, Aliyah N. and Borrer, Jerry L. 2013][research_alialiyahn_borrerjerryl_2013]
- [Ali, Aliyah N. and Borrer, Jerry L. 2013][research_alialiyahn_borrerjerryl_2013_b]
- [Allard 2024][research_allard_2024]
- [Allen 1981][research_allen_1981]
- [Allen 1983][research_allen_1983]
- [Allen et al 1994][research_allen_sauvageau_1994]
- [Allen, K. J. and Wrigley, W. R. 1965][research_allenkj_wrigleywr_1965]
- [Allison, Sidney G. et al 2007][research_allisonsidneyg_prosserwilliamh_2007]
- [Al Maraashli et al 2025][research_almaraashli_youseffi_2025]
- [Al-Masoud and Singh 2001][research_almasoud_singh_2001]
- [Alon and Rafaely 2014][research_alon_rafaely_2014]
- [Al-Shehabi and Newman 2002][research_alshehabi_newman_2002]
- [Alston, D. W. et al 1967][research_alstondw_barberjb_1967]
- [Alter, Stephen J. et al 2015][research_alterstephenj_brauckmanngregoryj_2015]
- [Alter, Stephen J. et al 2015][research_alterstephenj_brauckmanngregoryj_2015_b]
- [Alvord et al 2024][research_alvord_arias_2024]
- [Amer, Tahani et al 2004][research_amertahani_trippjohn_2004]
- [Amy F Fagan and Khairul BMQ Zaman][research_amyffagan_khairulbmqzaman]
- [Amy F Fagan et al 2024][research_amyffagan_khairulbmqzaman_2024]
- [Amy F Fagan et al][research_amyffagan_khairulbmqzaman_b]
- [An analytical investigation of 1966][research_an_analytical_1966]
- [An examination of the 1965][research_an_examination_1965]
- [Anandaraj et al 2019][research_anandaraj_sarkar_2019]
- [Anderson et al 2013][research_anderson_heister_2013]
- [Anderson et al 2015][research_anderson_heister_2015]
- [Anderson et al 1996][research_anderson_mcamis_1996]
- [Anderson et al 2012][research_anderson_son_2012]
- [Anderson, J. D. 1966][research_andersonjd_1966]
- [Anderson, Karl F. 1993][research_andersonkarlf_1993]
- [Anderson, Karl F. 1995][research_andersonkarlf_1995]
- [Anderson, P. G. et al 1993][research_andersonpg_chenggc_1993]
- [Anderson, P. G. et al 1992][research_andersonpg_chenys_1992]
- [Anderson, T. O. and Gallo, A. J. 1967][research_andersonto_galloaj_1967]
- [Andersson and Forsell 1979][research_andersson_forsell_1979]
- [Andrew M Brown][research_andrewmbrown]
- [Andrew Roberts and Claude Hashem 1995][research_andrewroberts_claudehashem_1995]
- [Andrews 1998][research_andrews_1998]
- [Andrie 2009][research_andrie_2009]
- [Andrieu 2026][research_andrieu_2026]
- [Anex et al 1991][research_anex_russell_1991]
- [Anima D Sabale and Erika E Gallegos 2026][research_animadsabale_erikaegallegos_2026]
- [Anima Sabale and Erika E Gallegos 2026][research_animasabale_erikaegallegos_2026]
- [Anjana et al 2022][research_anjana_renjith_2022]
- [Anson, K. W. 1977][research_ansonkw_1977]
- [Anthony Scott Craig et al][research_anthonyscottcraig_jaydenehauglie]
- [Antinone, R. et al 1969][research_antinoner_kowh_1969]
- [Antonazzi 1981][research_antonazzi_1981]
- [Antonelli et al 2020][research_antonelli_pepe_2020]
- [Anuskiewicz et al 2026][research_anuskiewicz_cave_2026]
- [Anzalone, Evan J. et al 2018][research_anzaloneevanj_johnstonhunter_2018]
- [Aogaki et al 2017][research_aogaki_kitamura_2017]
- [Aogaki et al 2019][research_aogaki_kitamura_2019]
- [Apollo 11 Telemetry Data 2010][research_apollo_11_2010]
- [Apollo mission 11, trajectory 1970][research_apollo_mission_1970]
- [Apollo/Saturn 5 Postflight Trajectory 1973][research_apollo_saturn_5_1973]
- [Appendix C Rocket Engine 1992][research_appendix_c_1992]
- [Appendix H Alternate Measurement 2026][research_appendix_h_2026]
- [Appendix K Condensed Measurement 2026][research_appendix_k_2026]
- [Appich, W. H., Jr. and Turner, K. L. 1958][research_appichwhjr_turnerkl_1958]
- [Applications of neural networks 1999][research_applications_of_1999]
- [Aprovitola et al 2019][research_aprovitola_iuspa_2019]
- [Aprovitola et al 2019][research_aprovitola_iuspa_2019_b]
- [Arcangeli, J.-P. et al 1993][research_arcangelijp_crochemorem_1993]
- [Ardalan, S.M. et al 2008][research_ardalansm_antreasianpg_2008]
- [Armstrong 1964][research_armstrong_1964]
- [Arndt, G. D. et al 1970][research_arndtgd_novosadsw_1970]
- [Arnett 1993][research_arnett_1993]
- [Arning et al 2010][research_arning_wu_2010]
- [Aronstein, David L. and Smith, J. Scott 2016][research_aronsteindavidl_smithjscott_2016]
- [Arora and Ananthasayanam 2003][research_arora_ananthasayanam_2003]
- [Arora et al 2003][research_arora_george_2003]
- [Arrington et al 1967][research_arrington_molloy_1967]
- [Arronde Pérez and Zangl 2026][research_arrondeperez_zangl_2026]
- [Arueti 1988][research_arueti_1988]
- [Aruna and Devi 2012][research_aruna_devi_2012]
- [Ascent Trajectory Analysis and 2022][research_ascent_trajectory_2022]
- [A. S. Craig et al][research_ascraig_mjhawkins]
- [Askins, Bruce and Robinson, Kimberly F. 2017][research_askinsbruce_robinsonkimberlyf_2017]
- [Aslan et al 2026][research_aslan_kara_2026]
- [Aso and Sugimoto 2005][research_aso_sugimoto_2005]
- [Aso and Tani 2018][research_aso_tani_2018]
- [Aso and Tani 2018][research_aso_tani_2018_b]
- [Astorg and Barreau, luiver, C 1995][research_astorg_barreauluiverc_1995]
- [Atamanchuk 2025][research_atamanchuk_2025]
- [Aukerman, Carl A. 1991][research_aukermancarla_1991]
- [Aul'chenko 2006][research_aulchenko_2006]
- [Austin, Robert E. and Rising, Jerry J. 1999][research_austinroberte_risingjerryj_1999]
- [Austin, Robert E. and Rising, Jerry J. 2000][research_austinroberte_risingjerryj_2000]
- [Averkin, E. G. et al 1964][research_averkineg_fryertb_1964]
- [Averyanov et al 2021][research_averyanov_kazantsev_2021]
- [Ayoung-Chee et al 2013][research_ayoungchee_mack_2013]
- [Azpurua et al 2014][research_azpurua_paez_2014]
- [B et al 2021][research_b_kasher_2021]
- [Baars, Woutijn J. et al 2011][research_baarswoutijnj_tinneycharlese_2011]
- [Baars, Woutijn J. et al 2012][research_baarswoutijnj_tinneycharlese_2012]
- [Babb, C. D. and Fuller, D. E. 1967][research_babbcd_fullerde_1967]
- [Babbitt, Norman E., III 1992][research_babbittnormaneiii_1992]
- [Babcock and Coe 1971][research_babcock_coe_1971]
- [Bach 2017][research_bach_2017]
- [Baer, J. A. and Heckler, C. H., Jr. 1966][research_baerja_hecklerchjr_1966]
- [Baer, J. A. and Heckler, C. H., Jr. 1966][research_baerja_hecklerchjr_1966_b]
- [Baetz 1974][research_baetz_1974]
- [Baetz 1975][research_baetz_1975]
- [Baggeroer 1999][research_baggeroer_1999]
- [Baghdady, E. J. 1962][research_baghdadyej_1962]
- [Bagri and Majid 2009][research_bagri_majid_2009]
- [Bai and Weng 2014][research_bai_weng_2014]
- [Bailey, J. S. et al 1964][research_baileyjs_johnsondr_1964]
- [Baker 1969][research_baker_1969]
- [Baker et al 1965][research_baker_stockton_1965]
- [Bakker et al 2026][research_bakker_madhumitha_2026]
- [Bąkowski et al 2016][research_bakowski_radziszewski_2016]
- [Bal et al 2019][research_bal_consoliverzack_2019]
- [Balach, Dean 1995][research_balachdean_1995]
- [Balageas 2002][research_balageas_2002]
- [Balaji et al 2021][research_balaji_navinkumar_2021]
- [Balcomb 1972][research_balcomb_1972]
- [Baldwin, H. A. and Freyman, R. W. 1973][research_baldwinha_freymanrw_1973]
- [Balepin 2001][research_balepin_2001]
- [Balepin et al 2001][research_balepin_czysz_2001]
- [Balepin et al 2001][research_balepin_czysz_2001_b]
- [Balepin, Vladimir et al 1999][research_balepinvladimir_pricejohn_1999]
- [Ballard 1992][research_ballard_1992]
- [Ballard, Richard O. 2003][research_ballardrichardo_2003]
- [Balusamy et al 2024][research_balusamy_a_2024]
- [Bandyopadhyay, Alak et al 2011][research_bandyopadhyayalak_hamillbrian_2011]
- [Banks, B. et al 1975][research_banksb_rawlinv_1975]
- [Bao et al 2023][research_bao_dong_2023]
- [Bao and Li 2020][research_bao_li_2020]
- [Bao et al 2019][research_bao_wang_2019]
- [Baran et al 2014][research_baran_blanchard_2014]
- [Barani][research_barani]
- [Barbosa et al 2016][research_barbosa_silva_2016]
- [Barkhoudarian et al 1988][research_barkhoudarian_szemenyei_1988]
- [Barkhoudarian, Sarkis and Kittinger, Scott 2006][research_barkhoudariansarkis_kittingerscott_2006]
- [Barnes, W. P. et al 1964][research_barneswp_billingsleyjb_1964]
- [Barraza 1962][research_barraza_1962]
- [Barraza, R. M. 1962][research_barrazarm_1962]
- [Barret, Chris 1999][research_barretchris_1999]
- [Barros et al 2026][research_barros_correia_2026]
- [Barth, Andrew et al 2015][research_barthandrew_mamichharvey_2015]
- [Barthelme, N. et al 1986][research_barthelmen_leej_1986]
- [Barthorpe and Worden 2020][research_barthorpe_worden_2020]
- [Bartoe 1982][research_bartoe_1982]
- [Basciano 1998][research_basciano_1998]
- [Basharina et al 2021][research_basharina_goncharov_2021]
- [Bassen 1967][research_bassen_1967]
- [Bassen and Jantz 1966][research_bassen_jantz_1966]
- [Bates, Lakesha and Hong, Liang 2011][research_bateslakesha_hongliang_2011]
- [Bathker, D. A. and Clauss, R. C. 1966][research_bathkerda_claussrc_1966]
- [Batill, Stephen M. 1994][research_batillstephenm_1994]
- [Batista et al 2025][research_batista_trujilho_2025]
- [Bauer 1980][research_bauer_1980]
- [Bauer, A. B. 1981][research_bauerab_1981]
- [Bauer, A. B. et al 1982][research_bauerab_kibensv_1982]
- [Baumgartner 1997][research_baumgartner_1997]
- [Bayer, Janice I. et al 1991][research_bayerjanicei_varadanvv_1991]
- [Bayir and Akbıyık 2024][research_bayir_akbiyik_2024]
- [Bazin et al 2016][research_bazin_fields_2016]
- [Bechtel, R. D. et al 1988][research_bechtelrd_mateosma_1988]
- [Bechtold, W. R. et al 1966][research_bechtoldwr_bjorntjr_1966]
- [Bechtold, W. R. et al 1965][research_bechtoldwr_medlinje_1965]
- [Beck and Beach 2003][research_beck_beach_2003]
- [Becker, H. and Hamilton, H. 1965][research_beckerh_hamiltonh_1965]
- [Becker, H. and Tang, C. N. 1966][research_beckerh_tangcn_1966]
- [Beck, P. E. 1972][research_beckpe_1972]
- [Beck, P. E. 1973][research_beckpe_1973]
- [Beebe][research_beebe]
- [Beegum et al 2020][research_beegum_chacko_2020]
- [Behera et al 2025][research_behera_panda_2025]
- [Behn et al 2016][research_behn_kisler_2016]
- [Behn and Tapken 2025][research_behn_tapken_2025]
- [Bejani et al 2025][research_bejani_mauri_2025]
- [Bejczy 1971][research_bejczy_1971]
- [Belleville, R. E. and Lange, K. O. 1971][research_bellevillere_langeko_1971]
- [Bell, G. U. et al 1969][research_bellgu_hindspl_1969]
- [Bell, H. and Strock, J. 1980][research_bellh_strockj_1980]
- [Bendot, J. G. 1974][research_bendotjg_1974]
- [Benedikt 1953][research_benedikt_1953]
- [Benedikter et al 2025][research_benedikter_dambrosio_2025]
- [Benjamin S Burger et al][research_benjaminsburger_caroleaddona]
- [Benjamin, Theodore G. et al 1993][research_benjamintheodoreg_garciaroberto_1993]
- [Benjamin, Theodore G. and Mcconnaughey, Paul K. 1991][research_benjamintheodoreg_mcconnaugheypaulk_1991]
- [Benjauthrit, B. 1976][research_benjauthritb_1976]
- [Benjauthrit, B. and Kemp, R. P. 1977][research_benjauthritb_kemprp_1977]
- [Benjauthrit, B. et al 1976][research_benjauthritb_mulhallb_1976]
- [Bennett et al 2021][research_bennett_schaub_2021]
- [Bennewitz et al 2013][research_bennewitz_lineberry_2013]
- [Bennink and Pate 1989][research_bennink_pate_1989]
- [Bennink and Pate 1992][research_bennink_pate_1992]
- [Bensimon 1973][research_bensimon_1973]
- [Benson, H. E. et al 1964][research_bensonhe_mcculloughje_1964]
- [Bentham Science Publisher 2012][research_benthamsciencepublisher_2012]
- [Bentsman, Joseph et al 1990][research_bentsmanjoseph_pearlsteinarnej_1990]
- [Bentzen 1980][research_bentzen_1980]
- [Berggren et al 1948][research_berggren_ross_1948]
- [Bergman et al 1981][research_bergman_boyd_1981]
- [Bergmann, Martin et al 1990][research_bergmannmartin_longmanrichardw_1990]
- [Berkopec 1970][research_berkopec_1970]
- [Berman, A. L. and Au, P. A. 1992][research_bermanal_aupa_1992]
- [Berman, Joshua et al 2009][research_bermanjoshua_dudamichael_2009]
- [Bernstein et al 1949][research_bernstein_linzer_1949]
- [Berrier, B. L. 1969][research_berrierbl_1969]
- [Berrier, B. L. 1972][research_berrierbl_1972]
- [Berrier, B. L. 1973][research_berrierbl_1973]
- [Berrier, B. L. and Mercer, C. E. 1967][research_berrierbl_mercerce_1967]
- [Berrier, B. L. and Mercer, C. E. 1970][research_berrierbl_mercerce_1970]
- [Berthold, III, John W. 1986][research_bertholdiiijohnw_1986]
- [Berthomieu et al 2024][research_berthomieu_salmon_2024]
- [Bessant and Knight 1992][research_bessant_knight_1992]
- [Betancourt-Zamora, Rafael J. 1999][research_betancourtzamorarafaelj_1999]
- [Bethea, Mark D. and Rosenthal, Bruce N. 1992][research_betheamarkd_rosenthalbrucen_1992]
- [Betta et al 2000][research_betta_liguori_2000]
- [Beyma 1986][research_beyma_1986]
- [Beyon, Jeffrey Y. et al 2012][research_beyonjeffreyy_kochgradyj_2012]
- [Beyon, J. Y. et al 2010][research_beyonjy_kochgj_2010]
- [Bhatia][research_bhatia]
- [Bhutiani, P. K. 1980][research_bhutianipk_1980]
- [Bich et al 2007][research_bich_dagostino_2007]
- [Bickford, R. L. et al 1990][research_bickfordrl_duncandb_1990]
- [Bickford, R. L. and Madzsar, G. 1990][research_bickfordrl_madzsarg_1990]
- [Biesiadny, T. J. et al 1978][research_biesiadnytj_leed_1978]
- [Bill Prosser][research_billprosser]
- [Bin et al 2017][research_bin_hua_2017]
- [Bindal et al 2024][research_bindal_joshi_2024]
- [Bindal et al 2024][research_bindal_kattyayan_2024]
- [Binder 1993][research_binder_1993]
- [Binder, Michael and Felder, James L. 1993][research_bindermichael_felderjamesl_1993]
- [Binder, Michael et al 1997][research_bindermichael_tomsikthomas_1997]
- [Binder, Michael P. 1995][research_bindermichaelp_1995]
- [Birkeland and Meuser 1999][research_birkeland_meuser_1999]
- [Bishop][research_bishop]
- [Biswas et al 2016][research_biswas_khorasgani_2016]
- [Biswas et al 2020][research_biswas_khorasgani_2020]
- [Bjorklund et al 1979][research_bjorklund_rogero_1979]
- [Blackshire et al 2005][research_blackshire_giurgiutiu_2005]
- [Blades and Redgrave 2000][research_blades_redgrave_2000]
- [Blair and DeGeorge 2000][research_blair_degeorge_2000]
- [Blair, A. B., Jr. 1980][research_blairabjr_1980]
- [Blair, A. B., Jr. et al 1983][research_blairabjr_allenjm_1983]
- [Blair, A. B., Jr. et al 1992][research_blairabjr_dillonjamesl_1992]
- [Blake and Cunningham 2006][research_blake_cunningham_2006]
- [Blake Stuart and Jesse McEnulty][research_blakestuart_jessemcenulty]
- [Blalock and Fordham 2016][research_blalock_fordham_2016]
- [Blanchard and Rutherford 1984][research_blanchard_rutherford_1984]
- [Blanchard and Rutherford 1985][research_blanchard_rutherford_1985]
- [Blanco et al 2016][research_blanco_rahimov_2016]
- [Block 2 Solid Rocket 1986][research_block_2_1986]
- [Bloise, Anthony 1995][research_bloiseanthony_1995]
- [Blomshield, Fred S. and Bicker, C. J. 1996][research_blomshieldfreds_bickercj_1996]
- [Bloomer, Harry E 1958][research_bloomerharrye_1958]
- [Bloomquist, C. E. and Graham, W. C. 1965][research_bloomquistce_grahamwc_1965]
- [Blosser 1997][research_blosser_1997]
- [Blue, Lisa and Crawford, Kevin 1997][research_bluelisa_crawfordkevin_1997]
- [Blum et al 1999][research_blum_wurm_1999]
- [Blumenthal, Philip Z. 1995][research_blumenthalphilipz_1995]
- [Bodra and Khairnar 2025][research_bodra_khairnar_2025]
- [Bodrucki et al 2018][research_bodrucki_broilo_2018]
- [Bogart and Yang 1992][research_bogart_yang_1992]
- [Bogoi et al 2015][research_bogoi_rugescu_2015]
- [Bohlouri et al 2014][research_bohlouri_kosari_2014]
- [Bohse, J. R. et al 1979][research_bohsejr_bewtram_1979]
- [Boldissar and Alfredson][research_boldissar_alfredson]
- [Bolhov and Klyatchenko 2026][research_bolhov_klyatchenko_2026]
- [Bollino et al 2006][research_bollino_oppenheimer_2006]
- [Bono, P. 1963][research_bonop_1963]
- [Bordachev et al 2023][research_bordachev_kolga_2023]
- [Bordi, John J. et al 2005][research_bordijohnj_antreasianpete_2005]
- [Borek, R. W. 1973][research_borekrw_1973]
- [Borek, R. W. and Richardson, R. B. 1969][research_borekrw_richardsonrb_1969]
- [Borgna et al 2025][research_borgna_fusaro_2025]
- [Borkowski 2015][research_borkowski_2015]
- [Bornstein et al 1989][research_bornstein_celmins_1989]
- [Borowski, Stanley K. 1991][research_borowskistanleyk_1991]
- [Borowski, Stanley K. 1994][research_borowskistanleyk_1994]
- [Borowski, Stanley K. et al 2018][research_borowskistanleyk_ryanstephenw_2018]
- [Bos et al 1995][research_bos_nienkemper_1995]
- [Bos and Offerman 1999][research_bos_offerman_1999]
- [Bossi and Nelson 1992][research_bossi_nelson_1992]
- [Bosworth, John T. and Burken, John J. 1997][research_bosworthjohnt_burkenjohnj_1997]
- [Botelho et al 2022][research_botelho_martinez_2022]
- [Bouslog, S. et al 1998][research_bouslogs_mammanoj_1998]
- [Bowser and Busch 1966][research_bowser_busch_1966]
- [Boyadzhyan, V. V. 1998][research_boyadzhyanvv_1998]
- [Boykin, F. M. 1985][research_boykinfm_1985]
- [Bradford et al 2004][research_bradford_charania_2004]
- [Bradford and St. Germain 2010][research_bradford_stgermain_2010]
- [Bradley, P. F. et al 1983][research_bradleypf_siemerspmiii_1983]
- [Brandon L Mobley and Samantha Summers][research_brandonlmobley_samanthasummers]
- [Brausch, J. F. 1972][research_brauschjf_1972]
- [Brazzel 1963][research_brazzel_1963]
- [Breed, Kelly S. et al 2010][research_breedkellys_powellmarkw_2010]
- [Brennen][research_brennen]
- [Brent Pomeroy et al 2024][research_brentpomeroy_stevenkrist_2024]
- [Brent W Pomeroy et al][research_brentwpomeroy_stevenekrist]
- [Breshears et al 1966][research_breshears_mccafferty_1966]
- [Bresnahan, D. L. 1968][research_bresnahandl_1968]
- [Bresnahan, D. L. 1969][research_bresnahandl_1969]
- [Bresnahan, D. L. 1972][research_bresnahandl_1972]
- [Bresnahan, D. L. and Johns, A. L. 1968][research_bresnahandl_johnsal_1968]
- [Brevault][research_brevault]
- [Brevault et al 2020][research_brevault_balesdent_2020]
- [Brian R. Richardson][research_brianrrichardson]
- [Brian Saulman and Robert Wagner][research_briansaulman_robertwagner]
- [Brinda et al 2005][research_brinda_arora_2005]
- [Brinich, P. F. et al 1965][research_brinichpf_jackjr_1965]
- [Brinton, John and Golub, Leon 2004][research_brintonjohn_golubleon_2004]
- [Briscoe 1986][research_briscoe_1986]
- [Brochot 2015][research_brochot_2015]
- [Brociek et al 2023][research_brociek_hetmaniok_2023]
- [Brock][research_brock]
- [Brock and Franke 2004][research_brock_franke_2004]
- [Brockman, M. H. 1971][research_brockmanmh_1971]
- [Brockman, M. H. 1978][research_brockmanmh_1978]
- [Brockman, M. H. and Easterling, M. F. 1981][research_brockmanmh_easterlingmf_1981]
- [Broer et al 2022][research_broer_benedictus_2022]
- [Broglio, C. J. 1973][research_brogliocj_1973]
- [Bromm, August F, Jr and Goodwin, Julia M 1953][research_brommaugustfjr_goodwinjuliam_1953]
- [Bromm, August, F, jr and Goodwin, Julia M 1956][research_brommaugustfjr_goodwinjuliam_1956]
- [Bronz et al 2017][research_bronz_garciademarina_2017]
- [Brooks 2022][research_brooks_2022]
- [Brooks and Burkhalter 1988][research_brooks_burkhalter_1988]
- [Brooks, T. F. et al 1987][research_brookstf_marcolinima_1987]
- [Brosnan, Ian G. et al 2015][research_brosnaniang_mcgarrylouisep_2015]
- [Brown et al 1995][research_brown_coleman_1995]
- [Brown and Olds 2005][research_brown_olds_2005]
- [Brown et al 2019][research_brown_sethu_2019]
- [Brown, Andrew et al 2009][research_brownandrew_rufjosephh_2009]
- [Brown, Andrew M. 2000][research_brownandrewm_2000]
- [Brown, Andrew M. 2014][research_brownandrewm_2014]
- [Brown, Andrew M. and Brunty, Joseph A. 2001][research_brownandrewm_bruntyjosepha_2001]
- [Brown, Andrew M. et al 2018][research_brownandrewm_delessiojenniferl_2018]
- [Brown, Clinton E and Parker, Hermon M 1945][research_brownclintone_parkerhermonm_1945]
- [Browning 1993][research_browning_1993]
- [Brown, M. K. et al 1966][research_brownmk_griffinma_1966]
- [Bruegge, C. and Chafin, B. 1999][research_brueggec_chafinb_1999]
- [Brummer, E. A. and Harrington, R. F. 1962][research_brummerea_harringtonrf_1962]
- [Brummer, E. A. et al 1963][research_brummerea_harringtonrf_1963]
- [Bruner, Marilyn E. et al 1989][research_brunermarilyne_brownwilliama_1989]
- [Brunner, J. J. 1966][research_brunnerjj_1966]
- [Bryant 1989][research_bryant_1989]
- [Bryant 2010][research_bryant_2010]
- [Bryant, Thomas et al 1987][research_bryantthomas_crusebryant_1987]
- [Buchanan, R. P. 1986][research_buchananrp_1986]
- [Buddhavarapu et al 2019][research_buddhavarapu_charlson_2019]
- [Bufalino 1995][research_bufalino_1995]
- [Bui et al 2005][research_bui_murray_2005]
- [Buige, A. and Goode, W. 1965][research_buigea_goodew_1965]
- [Bujes 1962][research_bujes_1962]
- [Bull, Barton et al 2001][research_bullbarton_diehljames_2001]
- [Bull, Barton et al 2002][research_bullbarton_diehljames_2002]
- [Bullinger et al 2018][research_bullinger_bodensteiner_2018]
- [Burchett][research_burchett]
- [Burdett 1946][research_burdett_1946]
- [Burkardt, Leo A. 1992][research_burkardtleoa_1992]
- [Burke, E. S. and Harris, C. W. 1971][research_burkees_harriscw_1971]
- [Burkes, Darryl A. 1998][research_burkesdarryla_1998]
- [Burkhalter and Frank 1995][research_burkhalter_frank_1995]
- [Burkhalter and Frank 1996][research_burkhalter_frank_1996]
- [Burley, R. R. and Head, V. L. 1974][research_burleyrr_headvl_1974]
- [Burley, R. R. and Johns, A. L. 1974][research_burleyrr_johnsal_1974]
- [Burley, R. R. and Samanich, N. E. 1970][research_burleyrr_samanichne_1970]
- [Burnside, Jathan J. 2012][research_burnsidejathanj_2012]
- [Burr and Paulson 2021][research_burr_paulson_2021]
- [Burrows 2008][research_burrows_2008]
- [Burrows, Dale L and Newman, Ernest E 1954][research_burrowsdalel_newmanerneste_1954]
- [Bursey and Dickinson 1990][research_bursey_dickinson_1990]
- [Burst transmission of PCM 1966][research_burst_transmission_1966]
- [Burt and Hillsamer 1964][research_burt_hillsamer_1964]
- [Burton et al 2007][research_burton_loth_2007]
- [Burt, R. 1981][research_burtr_1981]
- [Burt, R. 1982][research_burtr_1982]
- [Burt, R. W. et al 1972][research_burtrw_hamnc_1972]
- [Butman, S. et al 1971][research_butmans_savageje_1971]
- [Butman, S. and Timor, U. 1971][research_butmans_timoru_1971]
- [Butman, S. and Timor, U. 1971][research_butmans_timoru_1971_b]
- [Butman, S. and Timor, U. 1973][research_butmans_timoru_1973]
- [Butt, Adam et al 2010][research_buttadam_poppchristopherg_2010]
- [Buzuluk et al 2020][research_buzuluk_plokhikh_2020]
- [C et al 2024][research_c_vinaykumar_2024]
- [Cabrera et al 2026][research_cabrera_zouhri_2026]
- [Calderon, M. 2000][research_calderonm_2000]
- [Calhoon et al 1973][research_calhoon_kors_1973]
- [Calhoun 2000][research_calhoun_2000]
- [Calise et al 2000][research_calise_tandon_2000]
- [Callsen et al 2026][research_callsen_herberhold_2026]
- [Camacho-Sánchez et al 2025][research_camachosanchez_loritediez_2025]
- [Camacho-Sánchez et al 2026][research_camachosanchez_loritediez_2026]
- [Camargo][research_camargo]
- [Campbell 1962][research_campbell_1962]
- [Campbell 1970][research_campbell_1970]
- [Campbell 2020][research_campbell_2020]
- [Campbell and Riccio 1995][research_campbell_riccio_1995]
- [Campbell, R. L. 1965][research_campbellrl_1965]
- [Candler 2001][research_candler_2001]
- [Candler and Kelley 1999][research_candler_kelley_1999]
- [Canfil, L. W. and Nieberding, W. C. 1967][research_canfillw_nieberdingwc_1967]
- [Cannon et al 1988][research_cannon_norman_1988]
- [Cao 2012][research_cao_2012]
- [Cao et al 2024][research_cao_zhang_2024]
- [Caogen et al 2008][research_caogen_hongjun_2008]
- [Caplin][research_caplin]
- [Carey 1967][research_carey_1967]
- [Carl, C. 1967][research_carlc_1967]
- [Carlson, John R. 1996][research_carlsonjohnr_1996]
- [Carpenter and Jeffus 1962][research_carpenter_jeffus_1962]
- [Carpenter and Jeffus 1963][research_carpenter_jeffus_1963]
- [Carpenter, J. Russell and Bauer, Frank H. 2001][research_carpenterjrussell_bauerfrankh_2001]
- [Carper, Richard D. 1988][research_carperrichardd_1988]
- [Carper, Richard D. and Stallings, William H., III 1990][research_carperrichardd_stallingswilliamhiii_1990]
- [Carratù et al 2025][research_carratu_gallo_2025]
- [Carraway, Preston I., III 1988][research_carrawayprestoniiii_1988]
- [Carreno, V. A. 1982][research_carrenova_1982]
- [Carreno, V. A. 1985][research_carrenova_1985]
- [Carreno, Victor A. 1986][research_carrenovictora_1986]
- [Carroll 1970][research_carroll_1970]
- [Carroll and Cox 1983][research_carroll_cox_1983]
- [Carta, D. G. 1963][research_cartadg_1963]
- [Carter 2009][research_carter_2009]
- [Carter, R. R. and Massey, G. A. 1967][research_carterrr_masseyga_1967]
- [Case][research_case]
- [Case studies in measurement 2006][research_case_studies_2006]
- [Casey 1995][research_casey_1995]
- [Cassady, Leonard D. et al 2013][research_cassadyleonardd_rayerics_2013]
- [Cassanto, J. M. et al 1968][research_cassantojm_eichelda_1968]
- [Cassell et al 2019][research_cassell_wercinski_2019]
- [Cassell, Alan et al 2019][research_cassellalan_wercinskipaul_2019]
- [Castro-Triguero et al 2014][research_castrotriguero_saavedraflores_2014]
- [Cavalieri et al 2023][research_cavalieri_liberatori_2023]
- [Caveny, L. H. et al 1980][research_cavenylh_kuokk_1980]
- [Cawley 2018][research_cawley_2018]
- [Çelik and Demirezen 2024][research_celik_demirezen_2024]
- [Celmins 1987][research_celmins_1987]
- [Cervantes et al 2024][research_cervantes_moore_2024]
- [Cesnik 2009][research_cesnik_2009]
- [Chabukswar et al 2025][research_chabukswar_mullen_2025]
- [Chai et al 2021][research_chai_yang_2021]
- [Chalmers 1967][research_chalmers_1967]
- [Chalyy 2018][research_chalyy_2018]
- [Chambellan, R. E. and Stepka, F. S. 1971][research_chambellanre_stepkafs_1971]
- [Chamberlin, R. 1973][research_chamberlinr_1973]
- [Chamberlin, R. and Samanich, N. E. 1971][research_chamberlinr_samanichne_1971]
- [Champaigne and Sumners 2007][research_champaigne_sumners_2007]
- [Chan, David T. et al 2019][research_chandavidt_paulsonjohnw_2019]
- [Chandiramani et al 2014][research_chandiramani_bhandari_2014]
- [Chandler 2023][research_chandler_2023]
- [Chang 1998][research_chang_1998]
- [Chang 2000][research_chang_2000]
- [Chang 2002][research_chang_2002]
- [Chang 2004][research_chang_2004]
- [Chang 2011][research_chang_2011]
- [Chang et al 2011][research_chang_markmiller_2011]
- [Chang, Chen J. et al 2018][research_changchenj_liaghatijramirl_2018]
- [Chanteur 2023][research_chanteur_2023]
- [Chao-Shan et al 2014][research_chaoshan_hua_2014]
- [Chaouat and Vuillot 1992][research_chaouat_vuillot_1992]
- [Chapman, Dean R 1952][research_chapmandeanr_1952]
- [Chapter 9 Uncertainty Propagation 2013][research_chapter_9_2013]
- [Charan and Tibrewal 2025][research_charan_tibrewal_2025]
- [Charles, F. J. and Larson, F. L. 1967][research_charlesfj_larsonfl_1967]
- [Charron et al 1978][research_charron_campbell_1978]
- [Chase 1979][research_chase_1979]
- [Chase and McKinney 2005][research_chase_mckinney_2005]
- [Chattopadhyay 2006][research_chattopadhyay_2006]
- [Chattopadhyay et al 2012][research_chattopadhyay_seaver_2012]
- [Chaudhari 2017][research_chaudhari_2017]
- [Chehrzad and Khoramishad 2026][research_chehrzad_khoramishad_2026]
- [Chelner 2002][research_chelner_2002]
- [Chelner 2003][research_chelner_2003]
- [Chen 2019][research_chen_2019]
- [Chen et al 2024][research_chen_chen_2024]
- [Chen et al 2026][research_chen_du_2026]
- [Chen et al 2019][research_chen_ma_2019]
- [Chen and Ma 2019][research_chen_ma_2019_b]
- [Chen et al 2018][research_chen_mu_2018]
- [Chen et al 2025][research_chen_wang_2025]
- [Chen et al 2025][research_chen_wang_2025_b]
- [Chen and Wu 2018][research_chen_wu_2018]
- [Chen et al 2021][research_chen_xing_2021]
- [Chen et al 2013][research_chen_yang_2013]
- [Chen et al 2025][research_chen_yang_2025]
- [Chen et al 2026][research_chen_yuan_2026]
- [Cheng et al 2021][research_cheng_jing_2021]
- [Cheng et al 2024][research_cheng_jing_2024]
- [Cheng et al 2017][research_cheng_li_2017]
- [Cheng, Gary 2003][research_chenggary_2003]
- [Chenoweth, F. C. and Jeracki, R. J. 1970][research_chenowethfc_jerackirj_1970]
- [Chenoweth, F. C. and Lieberman, A. 1971][research_chenowethfc_liebermana_1971]
- [Chen, T. T. et al 1974][research_chentt_bohningod_1974]
- [Cheyne et al 2013][research_cheyne_key_2013]
- [Chiang, Kwofu V. et al 2017][research_chiangkwofuv_mcintirejeff_2017]
- [Chiang, Vincent et al 2011][research_chiangvincent_sunjunqiang_2011]
- [Chiba et al 2013][research_chiba_kanazaki_2013]
- [Chiba et al 2014][research_chiba_kanazaki_2014]
- [Chiba et al 2016][research_chiba_kanazaki_2016]
- [Chiba et al 2014][research_chiba_watanabe_2014]
- [Chiesa et al 2005][research_chiesa_grassi_2005]
- [Chik and Cheng 2012][research_chik_cheng_2012]
- [Childress-Thompson, Rhonda et al 2017][research_childressthompsonrhonda_dalethomasl_2017]
- [Childress-Thompson, Rhonda et al 2016][research_childressthompsonrhonda_thomasdale_2016]
- [China achieves first reusable 2026][research_china_achieves_2026]
- [Chinn et al 1979][research_chinn_dekany_1979]
- [Chin, T. M. et al 2003][research_chintm_grossrs_2003]
- [Chiu 1987][research_chiu_1987]
- [Chiu 2010][research_chiu_2010]
- [Chiu et al 2010][research_chiu_chang_2010]
- [Chiu et al 1990][research_chiu_kross_1990]
- [Chivers and Filmore 2024][research_chivers_filmore_2024]
- [Cho et al 2004][research_cho_kim_2004]
- [Choate, R. L. 1962][research_choaterl_1962]
- [Choi and Kim 2025][research_choi_kim_2025]
- [Choi et al 2015][research_choi_lee_2015]
- [Choi and Sweetman 2009][research_choi_sweetman_2009]
- [Chomputawat and Chatwiriya 2019][research_chomputawat_chatwiriya_2019]
- [Choo et al 2018][research_choo_mun_2018]
- [Chowdhury et al 2026][research_chowdhury_joshi_2026]
- [Chris D Karlgaard et al 2025][research_chrisdkarlgaard_rafaelalugo_2025]
- [Christensen, C. S. 1970][research_christensencs_1970]
- [Christensen, C. S. et al 1980][research_christensencs_moultrieb_1980]
- [Christenson, Rick L. et al 2003][research_christensonrickl_nelsonmichaela_2003]
- [Christenson, R. L. and Komar, D. R. 1998][research_christensonrl_komardr_1998]
- [Christopher D Karlgaard et al][research_christopherdkarlgaard_rafaelalugo]
- [Christopher D Karlgaard et al][research_christopherdkarlgaard_rafaellugo]
- [Christopher D Karlgaard et al][research_christopherdkarlgaard_rohangdeshmukh]
- [Chronister and Palazotto 2006][research_chronister_palazotto_2006]
- [Chua et al 2025][research_chua_kumar_2025]
- [Chun 1983][research_chun_1983]
- [Chung 2006][research_chung_2006]
- [Chung, J. N. et al 2006][research_chungjn_tullylandon_2006]
- [Chunovkina 2000][research_chunovkina_2000]
- [Cianci et al 2024][research_cianci_corallo_2024]
- [Cikanek 1986][research_cikanek_1986]
- [Cikanek, H. A., III 1986][research_cikanekhaiii_1986]
- [Cikanek, H. A., Jr. et al 1969][research_cikanekhajr_mcgowenjjiii_1969]
- [Cipolle, D. J. 1980][research_cipolledj_1980]
- [Citriniti and Citriniti 1997][research_citriniti_citriniti_1997]
- [Civek and Özgören 2017][research_civek_ozgoren_2017]
- [Clancy 2000][research_clancy_2000]
- [Clark, D. H. and Tenenbaum, D. M. 1967][research_clarkdh_tenenbaumdm_1967]
- [Clarke et al 1972][research_clarke_khayat_1972]
- [Clarke, R. et al 1982][research_clarker_shaned_1982]
- [Clark, J. S. et al 1970][research_clarkjs_graberej_1970]
- [Clark, J. S. and Lieberman, A. 1972][research_clarkjs_liebermana_1972]
- [Clayton 1999][research_clayton_1999]
- [Clayton, J. Louie 2001][research_claytonjlouie_2001]
- [Clayton, J. Louie 2012][research_claytonjlouie_2012]
- [Clayton, J. Louie 2017][research_claytonjlouie_2017]
- [Clayton, J. Louie 2017][research_claytonjlouie_2017_b]
- [Clayton, R. M. et al 1967][research_claytonrm_gerbrachtfg_1967]
- [Cler, Daniel L. et al 1993][research_clerdaniell_masonmaryl_1993]
- [Clubb, J. J. 1971][research_clubbjj_1971]
- [Coakley][research_coakley]
- [Cobleigh, Brent R. 1998][research_cobleighbrentr_1998]
- [CODAG sounding rocket experiment 1999][research_codag_sounding_1999]
- [Code, A. D. 1975][research_codead_1975]
- [Cohen, H. A. et al 1979][research_cohenha_shermanc_1979]
- [Cohen, Robert J 1951][research_cohenrobertj_1951]
- [Cohn 1997][research_cohn_1997]
- [Coirier et al 2014][research_coirier_stutts_2014]
- [Cole, Henry, A, jr and Abramovitz, Marvin 1952][research_colehenryajr_abramovitzmarvin_1952]
- [Colicci et al 2025][research_colicci_noonan_2025]
- [Collamore, Frank N. 1989][research_collamorefrankn_1989]
- [Collins, Aaron et al 1989][research_collinsaaron_dominycarol_1989]
- [Collins, Aaron S. 1989][research_collinsaarons_1989]
- [Combustion Instability Analysis Numerical 1995][research_combustion_instability_1995]
- [Compton, H. R. et al 1979][research_comptonhr_blanchardrc_1979]
- [Compton, H. R. et al 1981][research_comptonhr_findlayjt_1981]
- [Conference on Adaptive Telemetry 1967][research_conference_on_1967]
- [Conley et al 2003][research_conley_lee_2003]
- [Connell, Edward B. et al 1987][research_connelledwardb_howelldavidr_1987]
- [Conners and Sims 1998][research_conners_sims_1998]
- [Connolly 1965][research_connolly_1965]
- [Coogan 2015][research_coogan_2015]
- [Cook 1979][research_cook_1979]
- [Cook 1995][research_cook_1995]
- [Cook 1996][research_cook_1996]
- [Cook and Gruet 2003][research_cook_gruet_2003]
- [Cook et al 1997][research_cook_walters_1997]
- [Cook, Jerry and Lyles, Garry 2017][research_cookjerry_lylesgarry_2017]
- [Coppotelli et al 2005][research_coppotelli_marzocca_2005]
- [Corban et al 2001][research_corban_johnson_2001]
- [Cordes and Hertzfeld 1997][research_cordes_hertzfeld_1997]
- [Cortopassi, A. C. et al 2012][research_cortopassiac_martinht_2012]
- [Cortright, Edgar M, Jr and Schroeder, Albert H 1951][research_cortrightedgarmjr_schroederalberth_1951]
- [Cosens and Newton 1988][research_cosens_newton_1988]
- [Costa et al 2024][research_costa_parente_2024]
- [Costello and Agarwalla 2000][research_costello_agarwalla_2000]
- [Costello and Agarwalla 2001][research_costello_agarwalla_2001]
- [Costello and Costello 1997][research_costello_costello_1997]
- [Cote, C. E. 1966][research_cotece_1966]
- [Cote, C. E. and Cressey, J. R. 1967][research_cotece_cresseyjr_1967]
- [Cowling 2011][research_cowling_2011]
- [Cox et al 2003][research_cox_harris_2003]
- [Cox, F. B. et al 1968][research_coxfb_keipertfa_1968]
- [Cox, Jr. 1987][research_coxjr_1987]
- [Cox, Jr. 1988][research_coxjr_1988]
- [Crabtree 1962][research_crabtree_1962]
- [Craig, K. A. 1966][research_craigka_1966]
- [Cramer, K. Elliott 2016][research_cramerkelliott_2016]
- [Cramer, R. L. and Grant, T. L. 1971][research_cramerrl_granttl_1971]
- [Crawford, Kevin et al 1999][research_crawfordkevin_huberharold_1999]
- [Crawford, Kevin and Pinkleton, David 1998][research_crawfordkevin_pinkletondavid_1998]
- [Crawford, Kevin and Pinkleton, David 1999][research_crawfordkevin_pinkletondavid_1999]
- [Crawford, W. L. and Reynolds, D. R. 1969][research_crawfordwl_reynoldsdr_1969]
- [Creech, Dennis M. et al 2010][research_creechdennism_threetgradyejr_2010]
- [Creveling, C. J. 1964][research_crevelingcj_1964]
- [Creveling, C. J. 1965][research_crevelingcj_1965]
- [Creveling, C. J. 1966][research_crevelingcj_1966]
- [Creveling, C. J. 1967][research_crevelingcj_1967]
- [Cristaldi et al 2007][research_cristaldi_faifer_2007]
- [Cristaldi et al 2018][research_cristaldi_ferrero_2018]
- [Crocker, M. J. and Potter, R. C. 1966][research_crockermj_potterrc_1966]
- [Crook and Tarrant 1998][research_crook_tarrant_1998]
- [Crosswy and Kalb 1967][research_crosswy_kalb_1967]
- [Crosswy, F. L. and Hornkohl, J. O. 1973][research_crosswyfl_hornkohljo_1973]
- [Crowe 1967][research_crowe_1967]
- [Crowe et al 1968][research_crowe_babcock_1968]
- [Crowley, Tim 1999][research_crowleytim_1999]
- [Cruickshank 1984][research_cruickshank_1984]
- [Crutcher, H. L. and Guttman, N. B. 1969][research_crutcherhl_guttmannb_1969]
- [Cullen, R. E. and Ragland, K. W. 1967][research_cullenre_raglandkw_1967]
- [Culver and Rochow 1993][research_culver_rochow_1993]
- [Cummings et al 2006][research_cummings_divine_2006]
- [Cusick and Kontis 2019][research_cusick_kontis_2019]
- [Czarcinski, E. A. et al 1970][research_czarcinskiea_feinbergpm_1970]
- [Czarcinski, E. A. et al 1965][research_czarcinskiea_maxwellms_1965]
- [D. et al 2022][research_d_b_2022]
- [D. et al 2023][research_d_m_2023]
- [Dąbrowski et al 2020][research_dabrowski_pelzner_2020]
- [DAgostino, Mark et al 2001][research_dagostinomark_leeyoungc_2001]
- [Dahan et al 2012][research_dahan_morgans_2012]
- [Dahlke and Pettis 1970][research_dahlke_pettis_1970]
- [Dai et al 2017][research_dai_liu_2017]
- [Dai et al 2026][research_dai_xiao_2026]
- [Dakka and Dennison 2021][research_dakka_dennison_2021]
- [Dale A Mackall et al 1998][research_daleamackall_robertsakahara_1998]
- [Dalle, Derek J. and Rogers, Stuart E. 2015][research_dallederekj_rogersstuarte_2015]
- [Dalle, Derek J. et al 2016][research_dallederekj_rogersstuarte_2016]
- [Dalle, Derek J. et al 2018][research_dallederekj_rogersstuarte_2018]
- [Dalton, John T. 1989][research_daltonjohnt_1989]
- [Daly][research_daly]
- [Damane and Pitot 2024][research_damane_pitot_2024]
- [D'Amico 2000][research_damico_2000]
- [Dan Dorney][research_dandorney]
- [Daniel and Ramusat 2005][research_daniel_ramusat_2005]
- [Daniel et al 2004][research_daniel_tumino_2004]
- [Daniel C. Kammer et al][research_danielckammer_paulblelloch]
- [Daniel E Paxson et al][research_danielepaxson_kenjimiki]
- [Daniels 1970][research_daniels_1970]
- [Dankanich, John et al 2015][research_dankanichjohn_aaneslandane_2015]
- [Dannenberg, R. E. and Katzman, H. 1969][research_dannenbergre_katzmanh_1969]
- [D'Antona 2004][research_dantona_2004]
- [Darby Vicker 2026][research_darbyvicker_2026]
- [Darren C Tinker 2021][research_darrenctinker_2021]
- [Darwell and Leeming 1965][research_darwell_leeming_1965]
- [Das, Indu S. et al 1996][research_dasindus_khavaranabbas_1996]
- [Das, I. S. and Dosanjh, D. S. 1991][research_dasis_dosanjhds_1991]
- [Data Acquisition System DAS 1998][research_data_acquisition_1998]
- [Data-Centric Structural Health Monitoring 2023][research_data_centric_structural_2023]
- [Datnow, B. et al 1969][research_datnowb_fryertb_1969]
- [Dave et al 2011][research_dave_murty_2011]
- [David Chan et al][research_davidchan_patrickshea]
- [David Doelling et al][research_daviddoelling_conorhaney]
- [David Friedlander et al][research_davidfriedlander_michaelbozeman]
- [Davidian 1987][research_davidian_1987]
- [Davidian, Kenneth J. 1987][research_davidiankennethj_1987]
- [Davidian, Kenneth O. and Kacynski, Kenneth J. 1993][research_davidiankennetho_kacynskikennethj_1993]
- [David J. Friedlander et al 2023][research_davidjfriedlander_michaeldbozeman_2023]
- [David M Driver et al 2018][research_davidmdriver_danielphilippidis_2018]
- [David O. Sigthorsson 2006][research_davidosigthorsson_2006]
- [Davis 1996][research_davis_1996]
- [Davis et al][research_davis_denison]
- [Davis and Spicer 1965][research_davis_spicer_1965]
- [Davis, Jr. 1988][research_davisjr_1988]
- [Davison, Craig R. et al 2016][research_davisoncraigr_strappjwalter_2016]
- [Davis, W. S. et al 1993][research_davisws_eudellah_1993]
- [Davydov and Sazonov 2009][research_davydov_sazonov_2009]
- [Dawson, C. T. and Schmitt, N. M. 1971][research_dawsonct_schmittnm_1971]
- [Day, John C. 1995][research_dayjohnc_1995]
- [De Angelis, V. M. and Tang, M. H. 1969][research_deangelisvm_tangmh_1969]
- [Debiasi 2012][research_debiasi_2012]
- [Debiasi et al 2010][research_debiasi_yan_2010]
- [Debnath and Naresh Reddy 2025][research_debnath_nareshreddy_2025]
- [Deboo, G. J. and Fryer, T. B. 1965][research_deboogj_fryertb_1965]
- [Decker, Arthur J. 2004][research_deckerarthurj_2004]
- [De Filippis et al 2025][research_defilippis_cappuccio_2025]
- [DeFord et al][research_deford_craig]
- [DeForrest, Lloyd et al 2016][research_deforrestlloyd_saadatfarzad_2016]
- [Degelsmith et al 1993][research_degelsmith_freaner_1993]
- [Delcher et al 1993][research_delcher_nemeth_1993]
- [de Leeuw and Brennan 2009][research_deleeuw_brennan_2009]
- [Del Mônaco Monteiro et al 2018][research_delmonacomonteiro_machiaverni_2018]
- [Delmonte, J. 1967][research_delmontej_1967]
- [Delvaille, J. P. 1981][research_delvaillejp_1981]
- [Demas, L. J. and Kinsley, R. L. 1971][research_demaslj_kinsleyrl_1971]
- [Dembrow, D. W. and Jamieson, L. B. 1964][research_dembrowdw_jamiesonlb_1964]
- [de Mendonça et al 1969][research_demendonca_sobral_1969]
- [Demerdziev and Cundeva-Blajer 2023][research_demerdziev_cundevablajer_2023]
- [Demerdziev and Dimchev 2023][research_demerdziev_dimchev_2023]
- [Demidovich 2017][research_demidovich_2017]
- [Deming Zhang et al][research_demingzhang_guiqingchen]
- [Demis Thomas et al][research_demisthomas_caitrinduffydeno]
- [Demis Thomas et al 2025][research_demisthomas_caitrinduffydeno_2025]
- [Demspm. Erol et al 2004][research_demspmerol_valencialisam_2004]
- [Deng et al 2025][research_deng_ompusunggu_2025]
- [Deng et al 2019][research_deng_wang_2019]
- [Deng et al 2022][research_deng_xu_2022]
- [Denguir-Rekik et al 2005][research_denguirrekik_mauris_2005]
- [Dennis et al 2010][research_dennis_hernandez_2010]
- [Dennis, T. et al 1970][research_dennist_mchughd_1970]
- [Depardon 2026][research_depardon_2026]
- [Der Kiureghian 2001][research_derkiureghian_2001]
- [Derriso et al 2016][research_derriso_mccurry_2016]
- [Desai, Prasun et al 2003][research_desaiprasun_schofieldjohnt_2003]
- [Desai, Prasun N. et al 2005][research_desaiprasunn_quallsgarryd_2005]
- [Design and FLOW Simulation 2014][research_design_and_flow_2014]
- [Design of Rocket-Engine Control 1992][research_design_of_1992]
- [DeSimio et al][research_desimio_miller]
- [De Simone et al 2017][research_desimone_ciampa_2017]
- [Des Jardins, R. and Wentz, L. H., Jr. 1965][research_desjardinsr_wentzlhjr_1965]
- [Despeyroux et al 2014][research_despeyroux_desaulnier_2014]
- [DeSpirito 2012][research_despirito_2012]
- [DeSpirito 2013][research_despirito_2013]
- [DeSpirito and Sahu 2001][research_despirito_sahu_2001]
- [Determining Aliasing in Isolated 2009][research_determining_aliasing_2009]
- [Determining Measurement Uncertainty Example 2017][research_determining_measurement_2017]
- [Dethloff 1961][research_dethloff_1961]
- [Deutsch, L. J. 1982][research_deutschlj_1982]
- [Deutsch, L. J. 1983][research_deutschlj_1983]
- [Devanath and Beebi 2016][research_devanath_beebi_2016]
- [Development of an onboard 1998][research_development_of_1998]
- [Devin Johnson et al][research_devinjohnson_venkatathmanathan]
- [Devries, L. L. 1971][research_devriesll_1971]
- [Dexter Johnson et al 2022][research_dexterjohnson_joelwsills_2022]
- [Diamanti and Soutis 2010][research_diamanti_soutis_2010]
- [Diamant, Kevin D. et al 2010][research_diamantkevind_pollardjamese_2010]
- [Diamond, John K. 1989][research_diamondjohnk_1989]
- [Diaz, Carlos E., Jr. 2015][research_diazcarlosejr_2015]
- [Di Cicca et al 2023][research_dicicca_hassan_2023]
- [Di Cicca et al 2024][research_dicicca_marsilio_2024]
- [Diem, H. G. and Kirby, F. M. 1977][research_diemhg_kirbyfm_1977]
- [Dietrich and Schulze 2011][research_dietrich_schulze_2011]
- [Dietrich and Schulze 2011][research_dietrich_schulze_2011_b]
- [Di Fiore dos Santos et al 2000][research_difioredossantos_lewis_2000]
- [Difrancesco et al 1989][research_difrancesco_boorady_1989]
- [Di Leo et al 2010][research_dileo_liguori_2010]
- [Dillo 2001][research_dillo_2001]
- [Dillon, Jr. 1996][research_dillonjr_1996]
- [Dimmock, John O. 2005][research_dimmockjohno_2005]
- [Di Monaco et al 2023][research_dimonaco_dantuono_2023]
- [Dinçer and Sezer Uzol 2022][research_dincer_sezeruzol_2022]
- [Ding et al 2020][research_ding_yang_2020]
- [Dirix and Enayati 2025][research_dirix_enayati_2025]
- [Dissanayake and Karunananda 2008][research_dissanayake_karunananda_2008]
- [Dissel et al 2012][research_dissel_huseman_2012]
- [Dissel et al 2005][research_dissel_kothari_2005]
- [Dixit et al 2025][research_dixit_goplani_2025]
- [DiZinno et al 2024][research_dizinno_reeves_2024]
- [Djanal-Mann and Murugan 2025][research_djanalmann_murugan_2025]
- [Dobrodomov et al 2026][research_dobrodomov_proroka_2026]
- [Dol 2021][research_dol_2021]
- [Dombrovsky 2008][research_dombrovsky_2008]
- [Dominy, Carol T. et al 1991][research_dominycarolt_chesneyjamesr_1991]
- [Donahue et al 2008][research_donahue_weldon_2008]
- [Donaldson, H. M. et al 1966][research_donaldsonhm_griffinma_1966]
- [Donbosco and Kumar 2014][research_donbosco_kumar_2014]
- [Dong and Kim 2018][research_dong_kim_2018]
- [Dong et al 2023][research_dong_wu_2023]
- [Dongare et al 2024][research_dongare_agrawal_2024]
- [Dongare et al 2023][research_dongare_peetala_2023]
- [Dongare et al 2024][research_dongare_peetala_2024]
- [Dongare et al 2025][research_dongare_peetala_2025]
- [Dorairajan][research_dorairajan]
- [Dorosh and Leontiev 2014][research_dorosh_leontiev_2014]
- [Dorsey et al 2000][research_dorsey_myers_2000]
- [Dorsey et al 1999][research_dorsey_wu_1999]
- [Dosanjh, Darshan S. and Das, Indu S. 1987][research_dosanjhdarshans_dasindus_1987]
- [Dosanjh, Darshan S. and Das, Indu S. 1988][research_dosanjhdarshans_dasindus_1988]
- [Dosanjh, D. S. et al 1983][research_dosanjhds_dasi_1983]
- [Dosanjh, D. S. and Das, I. S. 1985][research_dosanjhds_dasis_1985]
- [Dosanjh, D. S. and Das, I. S. 1986][research_dosanjhds_dasis_1986]
- [Douard, Stephane 1994][research_douardstephane_1994]
- [Doudkin et al 2019][research_doudkin_marushko_2019]
- [Dougherty, N. Sam and Liu, Baw-Lin 1991][research_doughertynsam_liubawlin_1991]
- [Doyoro et al 2022][research_doyoro_chang_2022]
- [Dragan 2010][research_dragan_2010]
- [Dragone 2000][research_dragone_2000]
- [Drews, Michael E. et al 1998][research_drewsmichaele_formandouglasa_1998]
- [Driscoll, E. A. and Landrum, D. B. 2004][research_driscollea_landrumdb_2004]
- [Drobyshev 2026][research_drobyshev_2026]
- [Du][research_du]
- [Du 2017][research_du_2017]
- [Du et al 2022][research_du_meng_2022]
- [Du et al 2017][research_du_wang_2017]
- [Duke and Houghton 1966][research_duke_houghton_1966]
- [Dukeman, Gregory A. and Gallaher, Michael W. 1998][research_dukemangregorya_gallahermichaelw_1998]
- [Dumbacher 2002][research_dumbacher_2002]
- [Dumbacher and Klevatt 1994][research_dumbacher_klevatt_1994]
- [Dunavant, J. C. et al 1966][research_dunavantjc_schersh_1966]
- [Duncan and Ensey 1964][research_duncan_ensey_1964]
- [Dunn, Michael G. 1989][research_dunnmichaelg_1989]
- [Dunn, Michael G. 1990][research_dunnmichaelg_1990]
- [Dunn, Stuart S. and Coats, Douglas E. 1996][research_dunnstuarts_coatsdouglase_1996]
- [Du Plessis 2026][research_duplessis_2026]
- [Durgesh et al 2004][research_durgesh_naughton_2004]
- [Dutta, Soumyo and Green, Justin S. 2019][research_duttasoumyo_greenjustins_2019]
- [Dyakonov, Artem A. et al 2009][research_dyakonovartema_buckgregorym_2009]
- [Dynamic real-time radiography of 1989][research_dynamic_real_time_1989]
- [Easterling, M. F. et al 1968][research_easterlingmf_spearaj_1968]
- [Easterling, M. F. et al 1969][research_easterlingmf_spearaj_1969]
- [Easton, R. A. and Hilbert, E. E. 1973][research_eastonra_hilbertee_1973]
- [Easwer et al 2023][research_easwer_manideep_2023]
- [Eberhart 1964][research_eberhart_1964]
- [Eberhart, C. J. et al 2015][research_eberhartcj_snellgrovelm_2015]
- [Eckart, M. E. et al 2012][research_eckartme_adamsjs_2012]
- [Eckert and Oechslein 1999][research_eckert_oechslein_1999]
- [Edge and Powers 1974][research_edge_powers_1974]
- [Edge and Powers 1976][research_edge_powers_1976]
- [Effect of uniformly distributed 1959][research_effect_of_1959]
- [Effinger, Michael et al 1999][research_effingermichael_clintonrgjr_1999]
- [Egerev et al 1993][research_egerev_ovchinnikov_1993]
- [Eggers, A. J., Jr. 1965][research_eggersajjr_1965]
- [Eggers, A J, Jr et al 1957][research_eggersajjr_resnikoffmeyerm_1957]
- [Eguia et al 2017][research_eguia_lamikiz_2017]
- [Ehrlichmann et al 1993][research_ehrlichmann_habich_1993]
- [Eichelberger, R. P. 1962][research_eichelbergerrp_1962]
- [Eichelberger, R. P. and Ratner, V. A. 1962][research_eichelbergerrp_ratnerva_1962]
- [Eilers et al 2010][research_eilers_matthew_2010]
- [Eilers et al 2011][research_eilers_wilson_2011]
- [Eilers et al 2012][research_eilers_wilson_2012]
- [Eisenberger and Posner 1965][research_eisenberger_posner_1965]
- [Eisenberger and Posner 1967][research_eisenberger_posner_1967]
- [Ekici and Savun 2026][research_ekici_savun_2026]
- [Eklund 2004][research_eklund_2004]
- [Elaine Yi Jia Zheng et al][research_elaineyijiazheng_danielcellucci]
- [El-Aini, Yehia et al 2010][research_elainiyehia_parkjohn_2010]
- [Elam, S. K. 2000][research_elamsk_2000]
- [Elan M Graupe et al 2025][research_elanmgraupe_chrisdkarlgaard_2025]
- [Eldred, C. H. and Gordon, S. V. 1976][research_eldredch_gordonsv_1976]
- [Electroacoustic Transducer Calibration Method 1984][research_electroacoustic_transducer_1984]
- [Electroacoustic transducer calibration method 1984][research_electroacoustic_transducer_1984_b]
- [Eleni Mowery et al][research_elenimowery_jacobstonehill]
- [El-Ghazawi, Tarek A. et al 1994][research_elghazawitareka_pritchardjim_1994]
- [Eliassen 1965][research_eliassen_1965]
- [Elizabeth et al 2019][research_elizabeth_kumar_2019]
- [Ellis and Kearney 1982][research_ellis_kearney_1982]
- [Ellis, David L. 2013][research_ellisdavidl_2013]
- [Ellison and Williams 2003][research_ellison_williams_2003]
- [Ellis, R. R. and Gamble, M. 1972][research_ellisrr_gamblem_1972]
- [Elms, C. P. 1965][research_elmscp_1965]
- [Elsaadany and Wen-Jun 2014][research_elsaadany_wenjun_2014]
- [Elshafey 2018][research_elshafey_2018]
- [Elston 1963][research_elston_1963]
- [Elvin 1996][research_elvin_1996]
- [Emens, F. H. et al 1966][research_emensfh_frostwo_1966]
- [E Mozzi and S Roth 1965][research_emozzi_sroth_1965]
- [Emrich 2016][research_emrich_2016]
- [Emrich 2016][research_emrich_2016_b]
- [Emrich 2016][research_emrich_2016_c]
- [Emrich 2023][research_emrich_2023]
- [Emrich 2023][research_emrich_2023_b]
- [Emrich 2023][research_emrich_2023_c]
- [Enciu and Rosen 2015][research_enciu_rosen_2015]
- [Engberg, Robert and Ooi, Teng K. 2004][research_engbergrobert_ooitengk_2004]
- [Engberg, Robert C. 2005][research_engbergrobertc_2005]
- [Ennix, Kimberly A. et al 1999][research_ennixkimberlya_corpeninggriffinp_1999]
- [Epperly and Walls][research_epperly_walls]
- [Eremenko et al 2003][research_eremenko_mouton_2003]
- [Erickson et al 1980][research_erickson_craddock_1980]
- [Erickson, Gary E. 2007][research_ericksongarye_2007]
- [Erin Hubbard and Frank Semmelmayer][research_erinhubbard_franksemmelmayer]
- [Erline and Hathaway 1999][research_erline_hathaway_1999]
- [ESDU Data Item estimates 1998][research_esdu_data_1998]
- [Est and Nelson 1991][research_est_nelson_1991]
- [Esterline et al 2010][research_esterline_wright_2010]
- [Estimation of Measurement Uncertainty][research_estimation_of]
- [Estler, W. Tyler 1989][research_estlerwtyler_1989]
- [Et. al. 2021][research_etal_2021]
- [Etters and Flurchick 1981][research_etters_flurchick_1981]
- [Eugene, L. Tu 1996][research_eugeneltu_1996]
- [Eujen, E 1942][research_eujene_1942]
- [Euler, E. A. et al 1979][research_eulerea_adamsgl_1979]
- [European company is developing 2015][research_european_company_2015]
- [Evan Anzalone et al][research_evananzalone_mikefritzinger]
- [Evanchuk, V. L. 1974][research_evanchukvl_1974]
- [Evan John Anzalone et al][research_evanjohnanzalone_gregdukeman]
- [Evans and Chattlain 2016][research_evans_chattlain_2016]
- [Evans and Donati 2018][research_evans_donati_2018]
- [Evans et al 2016][research_evans_martinez_2016]
- [Evans et al 2016][research_evans_martinez_2016_b]
- [Evans et al 2017][research_evans_martinez_2017]
- [Evans, S. A. et al 1975][research_evanssa_grosskw_1975]
- [Even and Hagita 2011][research_even_hagita_2011]
- [Example Uncertainty Propagation][research_example_uncertainty]
- [Excelco Developments Inc Silver Creek Ny 1963][research_excelcodevelopmentsincsilvercreekny_1963]
- [Expendable Second Stage Reusable 1971][research_expendable_second_1971]
- [Experimental investigation of combustor 1972][research_experimental_investigation_1972]
- [External autoignition test for 1986][research_external_autoignition_1986]
- [Ezebili and Schreve 2024][research_ezebili_schreve_2024]
- [Ezell et al 1992][research_ezell_barkhoudarian_1992]
- [Fabrication of X-ray telescopes 1981][research_fabrication_of_1981]
- [Fain, L. T. and Cribb, H. E. 1974][research_fainlt_cribbhe_1974]
- [Fairall 1967][research_fairall_1967]
- [Falanga, Ralph A 1956][research_falangaralpha_1956]
- [Falanga, Ralph A and Leiss, Abraham 1956][research_falangaralpha_leissabraham_1956]
- [Falkiewicz et al 2009][research_falkiewicz_cesnik_2009]
- [Falkiewicz et al 2010][research_falkiewicz_cesnik_2010]
- [Fallon, II et al 1999][research_fallonii_taylor_1999]
- [Fan 2021][research_fan_2021]
- [Fan et al 2026][research_fan_yao_2026]
- [Fan et al 2015][research_fan_yu_2015]
- [Fancher 1985][research_fancher_1985]
- [Fanciullo and Lacefield 1994][research_fanciullo_lacefield_1994]
- [Fang et al 2025][research_fang_li_2025]
- [Fang et al 2012][research_fang_ma_2012]
- [Fang et al 2012][research_fang_yixing_2012]
- [Fang et al 2011][research_fang_zou_2011]
- [Fansler and Schmidt 1976][research_fansler_schmidt_1976]
- [Fantini, Jay A. 1998][research_fantinijaya_1998]
- [Faranosov et al 2013][research_faranosov_karabasov_2013]
- [Farmer, Richard et al 2001][research_farmerrichard_chenggary_2001]
- [Farmer, Richard C. et al 1999][research_farmerrichardc_chenggary_1999]
- [Farnham 2018][research_farnham_2018]
- [Farokhi, S. and Vertzberger, M. 1989][research_farokhis_vertzbergerm_1989]
- [Farr et al 2005][research_farr_wiley_2005]
- [Faulstich and Law 2006][research_faulstich_law_2006]
- [Favaregh, Amber L. et al 2016][research_favareghamberl_houldenheatherp_2016]
- [Feinberg, P. et al 1969][research_feinbergp_maxwellm_1969]
- [Feinberg, P. and Maxwell, M. S. 1970][research_feinbergp_maxwellms_1970]
- [Feinberg, P. M. et al 1963][research_feinbergpm_leskojgjr_1963]
- [Feinberg, P. M. et al 1964][research_feinbergpm_leskojgjr_1964]
- [Feinberg, P. M. and Townsend, M. R. 1968][research_feinbergpm_townsendmr_1968]
- [Fejjari et al 2025][research_fejjari_delavault_2025]
- [Fenfen et al 2020][research_fenfen_xubo_2020]
- [Feng et al 2024][research_feng_shi_2024]
- [Feng et al 2014][research_feng_sun_2014]
- [Fenglei 2021][research_fenglei_2021]
- [Feng Li et al 2016][research_fengli_chaowang_2016]
- [Ferguson, C. R. et al 1987][research_fergusoncr_treedr_1987]
- [Ferlauto et al 2020][research_ferlauto_ferrero_2020]
- [Ferlauto et al 2020][research_ferlauto_ferrero_2020_b]
- [Fernandes von Huelsen][research_fernandesvonhuelsen]
- [Fernandez, Rene et al 2018][research_fernandezrene_riddlebaughjeff_2018]
- [Ferrandon 1997][research_ferrandon_1997]
- [Ferrandon 1998][research_ferrandon_1998]
- [Ferreira de Moura and Borges Ribeiro 2025][research_ferreirademoura_borgesribeiro_2025]
- [Ferrero 2025][research_ferrero_2025]
- [Ferrero et al 2015][research_ferrero_prioli_2015]
- [Ferris, D. J. 1967][research_ferrisdj_1967]
- [Ferris, J. C. 1967][research_ferrisjc_1967]
- [Fichtel, Edward J. and Mcdaniel, Amos D. 1994][research_fichteledwardj_mcdanielamosd_1994]
- [Fick et al 1997][research_fick_schmucker_1997]
- [Ficker 1992][research_ficker_1992]
- [Fielhauer, K. B. and Boone, B. G. 2011][research_fielhauerkb_boonebg_2011]
- [Figueroa, Jorge et al 2003][research_figueroajorge_saintcyrwilliam_2003]
- [Figueroa, Jorge et al 2004][research_figueroajorge_stcyrwilliam_2004]
- [File S1 2016 The][research_file_s1]
- [File S2 2018 The][research_file_s2]
- [File S4 2017 The][research_file_s4]
- [Fillery and Stanton 2011][research_fillery_stanton_2011]
- [Fincannon, H. James 2002][research_fincannonhjames_2002]
- [Fincannon, H. James 2003][research_fincannonhjames_2003]
- [Finger, H. J. and Cambra, J. M. 1974][research_fingerhj_cambrajm_1974]
- [Finley, Tom and Parker, Peter 2010][research_finleytom_parkerpeter_2010]
- [Fio Rito 1964][research_fiorito_1964]
- [Fischbach, Sean 2014][research_fischbachsean_2014]
- [Fischbach, Sean R. and Kenny, R. Jeremy 2010][research_fischbachseanr_kennyrjeremy_2010]
- [Fisher and Jr 1963][research_fisher_jr_1963]
- [Fisher, J. E. et al 2002][research_fisherje_lawrenceda_2002]
- [Fitch, Jeffery T. et al 2012][research_fitchjefferyt_simonalanl_2012]
- [Fitzsimmons 1996][research_fitzsimmons_1996]
- [Flagg, Howard S. and Kalil, Lou F. 1987][research_flagghowards_kalillouf_1987]
- [Flanagan, Patrick M. 1991][research_flanaganpatrickm_1991]
- [Flávio 2020][research_flavio_2020]
- [Fleming, William A and Gabriel, David S 1955][research_flemingwilliama_gabrieldavids_1955]
- [Flight Test Data Analysis 2016][research_flight_test_2016]
- [Florendo et al 2006][research_florendo_yechout_2006]
- [Florendo et al 2007][research_florendo_yechout_2007]
- [Flores, Jr. 1986][research_floresjr_1986]
- [Flynn, R. Y. and Groves, J. R. 1964][research_flynnry_grovesjr_1964]
- [Fogel, Alvin J. 1994][research_fogelalvinj_1994]
- [Follett, W. 1996][research_follettw_1996]
- [Follett, W. et al 1996][research_follettw_ketchuma_1996]
- [Foote 2013][research_foote_2013]
- [Forester and Strom 1986][research_forester_strom_1986]
- [Fort, David et al 2003][research_fortdavid_rogstaddavid_2003]
- [Fossum et al 2024][research_fossum_bhowmik_2024]
- [Foss, Willard E, Jr et al 1958][research_fosswillardejr_runckeljackf_1958]
- [Foster, W. A., Jr. et al 1981][research_fosterwajr_sforzinirh_1981]
- [Foster, W. A., Jr. et al 1986][research_fosterwajr_shuph_1986]
- [Foster, Winfred A., Jr. et al 2014][research_fosterwinfredajr_crowderwinston_2014]
- [Fotia et al 2019][research_fotia_kaemming_2019]
- [Fotowicz 2016][research_fotowicz_2016]
- [Fournier 2001][research_fournier_2001]
- [Fox 2025][research_fox_2025]
- [Fox 2025][research_fox_2025_b]
- [France's Liquid Propellant Rocket-Engine 2006][research_france_s_liquid_2006]
- [Francesco Soranna et al][research_francescosoranna_patricksheaney]
- [Francesco Soranna et al 2023][research_francescosoranna_patricksheaney_2023]
- [Francesco Soranna et al][research_francescosoranna_patricksheaney_b]
- [Francis and Thompson 1980][research_francis_thompson_1980]
- [Francisco Pena and Erick Rossi De La Fuente 2025][research_franciscopena_erickrossidelafuente_2025]
- [Frankel et al 2025][research_frankel_vergeer_2025]
- [Frankel et al 2025][research_frankel_vergeer_2025_b]
- [Franklin and Tinsley 1970][research_franklin_tinsley_1970]
- [Franz and Hassan 2023][research_franz_hassan_2023]
- [Franz, Russ et al 2006][research_franzruss_pestanamark_2006]
- [Freeman et al 1996][research_freeman_talay_1996]
- [Freeman et al 1997][research_freeman_talay_1997]
- [Freeman, Delma C., Jr. et al 1996][research_freemandelmacjr_talaytheodorea_1996]
- [French 1987][research_french_1987]
- [French 2010][research_french_2010]
- [Fresconi 2011][research_fresconi_2011]
- [Fresconi and Harkins 2011][research_fresconi_harkins_2011]
- [Friedland 1965][research_friedland_1965]
- [Friedman et al 1967][research_friedman_hines_1967]
- [Friedman, Morris D 1951][research_friedmanmorrisd_1951]
- [Fries, J. 1973][research_friesj_1973]
- [Froning, Jr. 1996][research_froningjr_1996]
- [Frost, W. O. 1962][research_frostwo_1962]
- [Frost, W. O. 1970][research_frostwo_1970]
- [Frost, W. O. and Ellis, D. H. 1971][research_frostwo_ellisdh_1971]
- [Frost, W. O. and Norvell, D. E. 1966][research_frostwo_norvellde_1966]
- [Frost, W. O. et al 1969][research_frostwo_simpsonrs_1969]
- [Fruboese, Joachim 1987][research_fruboesejoachim_1987]
- [Fryer, T. B. 1966][research_fryertb_1966]
- [Fryer, T. B. 1968][research_fryertb_1968]
- [Fryer, T. B. 1974][research_fryertb_1974]
- [Fryer, T. B. et al 1978][research_fryertb_corbinsd_1978]
- [Fryer, T. B. et al 1978][research_fryertb_lundgf_1978]
- [Fryer, T. B. et al 1977][research_fryertb_mccutcheonep_1977]
- [Fryer, T. B. et al 1972][research_fryertb_sandlerh_1972]
- [Fryer, T. B. et al 1975][research_fryertb_sandlerh_1975]
- [Fu et al 2025][research_fu_lam_2025]
- [Fu et al 2019][research_fu_wang_2019]
- [Fuchs et al 2018][research_fuchs_haskell_2018]
- [Fuertes et al 2018][research_fuertes_pilastre_2018]
- [Fuhrmann and Dreyer 2008][research_fuhrmann_dreyer_2008]
- [Fujimoto and Fujii 2003][research_fujimoto_fujii_2003]
- [Fukushima 2011][research_fukushima_2011]
- [Fuller 1973][research_fuller_1973]
- [Fuller, D. E. 1968][research_fullerde_1968]
- [Fundamentals of Measurement Uncertainty 2026][research_fundamentals_of_2026]
- [Furstenau 1965][research_furstenau_1965]
- [Furuichi and Terao 2015][research_furuichi_terao_2015]
- [Fuzzy Variables and Measurement][research_fuzzy_variables]
- [Gabriel and Helms 1970][research_gabriel_helms_1970]
- [Gabris, E. A. et al 1970][research_gabrisea_hansenqm_1970]
- [Gaddis, Stephen W. et al 1992][research_gaddisstephenw_hudsonsusant_1992]
- [Gage and Vander Kam 2003][research_gage_vanderkam_2003]
- [Gage, Mark and Dehoff, Ronald 1991][research_gagemark_dehoffronald_1991]
- [Gai and Sharma 1981][research_gai_sharma_1981]
- [Gaitonde and Samimy 2010][research_gaitonde_samimy_2010]
- [Galanga, F. L. and Mueller, T. J. 1976][research_galangafl_muellertj_1976]
- [Galbraith et al][research_galbraith_hayward]
- [Gale and Moedt 1962][research_gale_moedt_1962]
- [Galeazzi, M. et al 2012][research_galeazzim_colliermr_2012]
- [Gallagher, James J. 1948][research_gallagherjamesj_1948]
- [Galli][research_galli]
- [Galway 1980][research_galway_1980]
- [Ganesan et al 2025][research_ganesan_subburayan_2025]
- [Gangeh et al 2023][research_gangeh_bui_2023]
- [Gao et al 2016][research_gao_dai_2016]
- [Gao and Sun 2009][research_gao_sun_2009]
- [Gao et al 2013][research_gao_zhang_2013]
- [Gao et al 2025][research_gao_zhang_2025]
- [Garanin et al 2002][research_garanin_glagolev_2002]
- [Garbeff, Theodore J., II 2019][research_garbefftheodorejii_2019]
- [Garcia and Silveira 2015][research_garcia_silveira_2015]
- [Gardinier and Taylor 1999][research_gardinier_taylor_1999]
- [Gardner and Agarwal 2019][research_gardner_agarwal_2019]
- [Gardner et al 2022][research_gardner_bull_2022]
- [Garg and Dodiyal 2009][research_garg_dodiyal_2009]
- [Garg and Schiefer 2017][research_garg_schiefer_2017]
- [Garmire, G. P. 1974][research_garmiregp_1974]
- [Gath et al 2000][research_gath_well_2000]
- [Gatz, E. C. 1976][research_gatzec_1976]
- [Gatz, E. C. 1977][research_gatzec_1977]
- [Gatz, E. C. 1979][research_gatzec_1979]
- [Gellman, David I. et al 1991][research_gellmandavidi_biggarstuartf_1991]
- [Genge, Gary G. and Marsh, Matthew W. 1999][research_gengegaryg_marshmattheww_1999]
- [George, William K. et al 1991][research_georgewilliamk_raewilliamj_1991]
- [George, W. V. 1967][research_georgewv_1967]
- [Gerlach et al 2017][research_gerlach_sanli_2017]
- [Gertsbakh 2003][research_gertsbakh_2003]
- [Ghaffarian, Benny et al 1992][research_ghaffarianbenny_majumdaralokk_1992]
- [Ghosh and Gunasekaran 2021][research_ghosh_gunasekaran_2021]
- [Ghosh et al 2008][research_ghosh_singhal_2008]
- [Ghoshal et al 2012][research_ghoshal_ayers_2012]
- [Giacconi, R. et al 1967][research_giacconir_gorensteinp_1967]
- [Gibart][research_gibart]
- [Gibart et al 2024][research_gibart_pietlahanier_2024]
- [Gibson 1985][research_gibson_1985]
- [Gibson, Lorelei S. and Sealey, Bradley S. 1993][research_gibsonloreleis_sealeybradleys_1993]
- [Giel, T. V., Jr. and Mueller, T. J. 1975][research_gieltvjr_muellertj_1975]
- [Gieras and Gorgeri 2021][research_gieras_gorgeri_2021]
- [Giglio et al 2013][research_giglio_manes_2013]
- [Gilchriest, C. et al 1970][research_gilchriestc_goldsteinr_1970]
- [Gilder, J. R. et al 1970][research_gilderjr_gillmorewfjr_1970]
- [Giles and Whitford 1980][research_giles_whitford_1980]
- [Gillespie, Warren JR 1957][research_gillespiewarrenjr_1957]
- [Gillespie, Warren, Jr. 1960][research_gillespiewarrenjr_1960]
- [Gillespie, W., Jr. 1956][research_gillespiewjr_1956]
- [Gilley, G. C. 1975][research_gilleygc_1975]
- [Gilson et al 2023][research_gilson_a_2023]
- [Giridharan, M. G. et al 1992][research_giridharanmg_leejg_1992]
- [Girouard, Forrest R. and Hopkins, Allen 1993][research_girouardforrestr_hopkinsallen_1993]
- [Giurgiutiu 2003][research_giurgiutiu_2003]
- [Giurgiutiu 2015][research_giurgiutiu_2015]
- [Giurgiutiu 2016][research_giurgiutiu_2016]
- [Giurgiutiu 2016][research_giurgiutiu_2016_b]
- [Giurgiutiu 2020][research_giurgiutiu_2020]
- [Giurgiutiu 2022][research_giurgiutiu_2022]
- [Giurgiutiu and Lin 2004][research_giurgiutiu_lin_2004]
- [Giurgiutiu and Soutis 2010][research_giurgiutiu_soutis_2010]
- [Giurgiutiu and Zagrai 2005][research_giurgiutiu_zagrai_2005]
- [Glaab, J. A. 1985][research_glaabja_1985]
- [Glagolev et al 2000][research_glagolev_zubkov_2000]
- [Glaser][research_glaser]
- [Glassburn, Robin S. and Smith, Suzanne Weaver 1994][research_glassburnrobins_smithsuzanneweaver_1994]
- [Glatt 1961][research_glatt_1961]
- [Glenn A Bever 1981][research_glennabever_1981]
- [Glenn A Bever 1984][research_glennabever_1984]
- [Glenn A Bever 1986][research_glennabever_1986]
- [Glenn A Bever 1991][research_glennabever_1991]
- [Glenn A Bever 1991][research_glennabever_1991_b]
- [Glines, A. and Lazzaro, J. A. 1970][research_glinesa_lazzaroja_1970]
- [Gloger et al 2021][research_gloger_lettieri_2021]
- [Gloss, B. B. and Sewall, W. G. 1983][research_glossbb_sewallwg_1983]
- [Glozman, Vladimir and Brillhart, Ralph D. 1990][research_glozmanvladimir_brillhartralphd_1990]
- [Gnoffo, Peter A. et al 1998][research_gnoffopetera_braunrobertd_1998]
- [Godfrey 1973][research_godfrey_1973]
- [Goertz 1995][research_goertz_1995]
- [Goetze et al 2025][research_goetze_schlippe_2025]
- [Golato et al 2015][research_golato_santhanam_2015]
- [Golden 1969][research_golden_1969]
- [Goldin, D. S. and Norgren, C. T. 1963][research_goldinds_norgrenct_1963]
- [Golliard and Mihaescu 2024][research_golliard_mihaescu_2024]
- [Golliard and Mihaescu 2024][research_golliard_mihaescu_2024_b]
- [Golliard and Mihaescu 2024][research_golliard_mihaescu_2024_c]
- [Golliard and Mihaescu 2025][research_golliard_mihaescu_2025]
- [Golliard and Mihaescu 2025][research_golliard_mihaescu_2025_b]
- [Golliard and Mihaescu 2026][research_golliard_mihaescu_2026]
- [Golubev 2008][research_golubev_2008]
- [Golub, L. 1985][research_golubl_1985]
- [Golub, Leon 1987][research_golubleon_1987]
- [Golub, Leon 1989][research_golubleon_1989]
- [Golub, Leon 1996][research_golubleon_1996]
- [Golub, Leon 1997][research_golubleon_1997]
- [Golub, Leon 1998][research_golubleon_1998]
- [Gompertz 1950][research_gompertz_1950]
- [Goncharov et al 1995][research_goncharov_orlov_1995]
- [Gong et al 2015][research_gong_bing_2015]
- [Gong et al 2014][research_gong_chen_2014]
- [Gong et al 2017][research_gong_maunder_2017]
- [Gonsalves et al 1999][research_gonsalves_ivanov_1999]
- [Gonzales et al 2022][research_gonzales_sakaue_2022]
- [Gonzales et al 2022][research_gonzales_sakaue_2022_b]
- [Goodenow, Debra 2004][research_goodenowdebra_2004]
- [Goracke et al 1997][research_goracke_levack_1997]
- [Goradia, S. H. et al 1989][research_goradiash_bobbittpj_1989]
- [Gorbunov and Kirchengast 2018][research_gorbunov_kirchengast_2018]
- [Gordan et al 2023][research_gordan_mccrum_2023]
- [Gordon and Brown 1963][research_gordon_brown_1963]
- [Gorla et al 2025][research_gorla_brewer_2025]
- [Goto et al 2021][research_goto_nakayama_2021]
- [Goto et al 2007][research_goto_obayashi_2007]
- [Goto et al 2025][research_goto_tsujimura_2025]
- [Gould, Reginald J. 1993][research_gouldreginaldj_1993]
- [Gouri et al 2025][research_gouri_krishnama_2025]
- [Gowan 2005][research_gowan_2005]
- [Gowing 1990][research_gowing_1990]
- [Goyal][research_goyal]
- [Gozuoglu and Gerçekcioğlu 2026][research_gozuoglu_gercekcioglu_2026]
- [Graber, E. J., Jr. and Clark, J. S. 1972][research_graberejjr_clarkjs_1972]
- [Grace 2001][research_grace_2001]
- [Gradl, Paul 2016][research_gradlpaul_2016]
- [Gradl, Paul R. 2016][research_gradlpaulr_2016]
- [Gradl, Paul R. 2016][research_gradlpaulr_2016_b]
- [Gradl, Paul R. et al 2018][research_gradlpaulr_brandsmeierwill_2018]
- [Gradl, Paul R. and Schmidt, Tim 2016][research_gradlpaulr_schmidttim_2016]
- [Graeve, E. and Massey, H. N. 1967][research_graevee_masseyhn_1967]
- [Graham 2010][research_graham_2010]
- [Graham, Olin L. 1987][research_grahamolinl_1987]
- [Grandhi and Tobe 2010][research_grandhi_tobe_2010]
- [Grant, M. M. et al 1964][research_grantmm_stephanidescc_1964]
- [Grassl, H. J. 1971][research_grasslhj_1971]
- [Greatrix 2018][research_greatrix_2018]
- [Green 1994][research_green_1994]
- [Greene and Desjardins 1978][research_greene_desjardins_1978]
- [Greene, E. P. 1976][research_greeneep_1976]
- [Greene, E. P. 1978][research_greeneep_1978]
- [Greene, E. P. 1978][research_greeneep_1978_b]
- [Greenhall, C. A. 1976][research_greenhallca_1976]
- [Green, Robert O. et al 2001][research_greenroberto_pavribetina_2001]
- [Gregory and Han 2003][research_gregory_han_2003]
- [Gregory, Irene M. et al 1992][research_gregoryirenem_chowdhryrajivs_1992]
- [Gregory, Irene M. et al 1993][research_gregoryirenem_mcminnjohnd_1993]
- [Grey 1953][research_grey_1953]
- [Grey 1954][research_grey_1954]
- [Grieb][research_grieb]
- [Grieb et al 2011][research_grieb_lemieux_2011]
- [Griebeler, Elmer et al 2011][research_griebelerelmer_nawashnuha_2011]
- [Griffin and Sykes 2007][research_griffin_sykes_2007]
- [Griffin, D. C., Jr. 1975][research_griffindcjr_1975]
- [Griffin, M. A. et al 1965][research_griffinma_hassellhpjr_1965]
- [Griffin, M. A. et al 1966][research_griffinma_hassellhpjr_1966]
- [Grigoryev and Burlutskiy 2021][research_grigoryev_burlutskiy_2021]
- [Griner, Carolyn and Lyles, Garry 1999][research_grinercarolyn_lylesgarry_1999]
- [Grodzovskii 1968][research_grodzovskii_1968]
- [Grondin][research_grondin]
- [Grosdemange and Schaeffer 1990][research_grosdemange_schaeffer_1990]
- [Grosshandler 1999][research_grosshandler_1999]
- [Grubelich et al 1993][research_grubelich_rowland_1993]
- [Gu et al 2021][research_gu_cho_2021]
- [Gu and Liu 1995][research_gu_liu_1995]
- [Guadagnini et al 2023][research_guadagnini_dezaiacomo_2023]
- [Guenther et al 2026][research_guenther_compton_2026]
- [Guidance for Assessing the][research_guidance_for]
- [Guidelines for Implementation of][research_guidelines_for]
- [Guidelines on measurement uncertainty 2023][research_guidelines_on_2023]
- [Guimpilevich and Vertegel][research_guimpilevich_vertegel]
- [Guimpilevich and Vertegel 2000][research_guimpilevich_vertegel_2000]
- [Gulati, S. et al 1993][research_gulatis_tawelr_1993]
- [Güler 2026][research_guler_2026]
- [Gunn 1989][research_gunn_1989]
- [Gunter, E. J. and Flack, R. D. 1981][research_gunterej_flackrd_1981]
- [Guo et al 2008][research_guo_eriksen_2008]
- [Guo and Musgrave][research_guo_musgrave]
- [Guo et al 2023][research_guo_zhao_2023]
- [Guo et al 2012][research_guo_zhu_2012]
- [Guo and Zhu 2013][research_guo_zhu_2013]
- [Guodong Ning et al][research_guodongning_shuguangzhang]
- [Guo, T.-H. et al 1990][research_guoth_merrillw_1990]
- [Guo, T. H. et al 1992][research_guoth_merrillw_1992]
- [Gupta 2011][research_gupta_2011]
- [Gupta et al 2018][research_gupta_anilkumar_2018]
- [Guy et al 2001][research_guy_mclaughlin_2001]
- [Guzik et al 2025][research_guzik_cengarle_2025]
- [Ha et al 2019][research_ha_kim_2019]
- [Ha and Kim 2022][research_ha_kim_2022]
- [Haag, Thomas W. 1989][research_haagthomasw_1989]
- [Haas, Evan and DeLuccia, Frank 2016][research_haasevan_delucciafrank_2016]
- [Haberstroh et al 2008][research_haberstroh_besnard_2008]
- [Haddock, Paul C. and Horan, Stephen 1998][research_haddockpaulc_horanstephen_1998]
- [Hadjria and D'Almeida 2019][research_hadjria_dalmeida_2019]
- [Haftka et al 2010][research_haftka_yuan_2010]
- [Hagar and Alcock 1989][research_hagar_alcock_1989]
- [Hagopian 2002][research_hagopian_2002]
- [Haidinger et al 1997][research_haidinger_weiland_1997]
- [Haldorsen 2020][research_haldorsen_2020]
- [Hale and Wang 2009][research_hale_wang_2009]
- [Hall 2005][research_hall_2005]
- [Hall 2012][research_hall_2012]
- [Hall et al 2011][research_hall_hartsfield_2011]
- [Hall and Shtessel 2005][research_hall_shtessel_2005]
- [Hall, Charles E. et al 1998][research_hallcharlese_gallahermichaelw_1998]
- [Hall, Charles E. and Panossian, Hagop V. 1999][research_hallcharlese_panossianhagopv_1999]
- [Hall, C. R., Jr. and Mueller, T. J. 1971][research_hallcrjr_muellertj_1971]
- [Hamed, Awatef 1990][research_hamedawatef_1990]
- [Hamilton, Tom and Healy, Tom 1999][research_hamiltontom_healytom_1999]
- [Hamkins, Jon and Vilnrotter, Victor 2019][research_hamkinsjon_vilnrottervictor_2019]
- [Hamkins, Jon et al 2011][research_hamkinsjon_vilnrottervictora_2011]
- [Hammond][research_hammond]
- [Hampson 1984][research_hampson_1984]
- [Hampson, M. E. and Barkhoudarian, S. 1985][research_hampsonme_barkhoudarians_1985]
- [Han et al 2012][research_han_mateescu_2012]
- [Han et al 2019][research_han_wang_2019]
- [Hanapur et al 2022][research_hanapur_hiremath_2022]
- [Handbook for space processing 1975][research_handbook_for_1975]
- [Hanford 1969][research_hanford_1969]
- [Hang, Richard 2017][research_hangrichard_2017]
- [Hanke, Jeremy L. 2011][research_hankejeremyl_2011]
- [Hannigan et al 1993][research_hannigan_sved_1993]
- [Hannum et al 1976][research_hannum_kasper_1976]
- [Han, Samuel S. 1990][research_hansamuels_1990]
- [Han, Samuel S. 1991][research_hansamuels_1991]
- [Hansen et al 1967][research_hansen_gabris_1967]
- [Hao et al 2017][research_hao_peng_2017]
- [Hara et al 2024][research_hara_mamashita_2024]
- [Harder, Keith C and Rennemann, Conrad, Jr 1956][research_harderkeithc_rennemannconradjr_1956]
- [Hardesty 1970][research_hardesty_1970]
- [Hardgrove and Krieg, Jr. 1984][research_hardgrove_kriegjr_1984]
- [Hardy et al 1993][research_hardy_eldrenkamp_1993]
- [Hardy, Terry L. and Rapp, Douglas C. 1994][research_hardyterryl_rappdouglasc_1994]
- [Harney, P. F. 1981][research_harneypf_1981]
- [Harney, P. F. and Richardson, R. B. 1968][research_harneypf_richardsonrb_1968]
- [Harrington, D. E. 1970][research_harringtonde_1970]
- [Harrington, D. E. 1970][research_harringtonde_1970_b]
- [Harrington, D. E. et al 1974][research_harringtonde_noseksm_1974]
- [Harrington, D. E. and Schloemer, J. J. 1974][research_harringtonde_schloemerjj_1974]
- [Harrington, D. E. et al 1975][research_harringtonde_schloemerjj_1975]
- [Harrington, D. E. et al 1976][research_harringtonde_schloemerjj_1976]
- [Harrington, D. E. and Wasko, R. A. 1968][research_harringtonde_waskora_1968]
- [Harris 1963][research_harris_1963]
- [Harris et al 2018][research_harris_dizaji_2018]
- [Harris, B. 1962][research_harrisb_1962]
- [Harrison and Lockman 1969][research_harrison_lockman_1969]
- [Harrje 1959][research_harrje_1959]
- [Harroun et al 2019][research_harroun_heister_2019]
- [Hart, Roger G. and Katz, Ellis R. 1949][research_hartrogerg_katzellisr_1949]
- [Harvazinski et al 2014][research_harvazinski_sankaran_2014]
- [Hase 2004][research_hase_2004]
- [Hassani and Dackermann 2023][research_hassani_dackermann_2023]
- [Hass, Neal et al 1999][research_hassneal_mizukamimasashi_1999]
- [Hattis, Philip D. and Malchow, Harvey L. 1991][research_hattisphilipd_malchowharveyl_1991]
- [Hattis, Philip D. and Malchow, Harvey L. 1992][research_hattisphilipd_malchowharveyl_1992]
- [Hauer et al 1963][research_hauer_tabata_1963]
- [Hauptschein, A. and Sommer, R. C. 1963][research_hauptscheina_sommerrc_1963]
- [Hauser and Helfrich 1963][research_hauser_helfrich_1963]
- [Havelund, Klaus and Joshi, Rajeev 2014][research_havelundklaus_joshirajeev_2014]
- [H. Douglas Perkins][research_hdouglasperkins]
- [He et al 2004][research_he_he_2004]
- [He et al 2018][research_he_li_2018]
- [He et al 2020][research_he_liu_2020]
- [He et al 2025][research_he_pan_2025]
- [He et al 2026][research_he_pan_2026]
- [He et al 2015][research_he_qin_2015]
- [He et al 2022][research_he_shi_2022]
- [He et al 2018][research_he_xu_2018]
- [He and Yuan 2024][research_he_yuan_2024]
- [Head, V. L. 1974][research_headvl_1974]
- [Heat transfer measurements and 1994][research_heat_transfer_1994]
- [Heath and Bell 2020][research_heath_bell_2020]
- [Heath, Christopher M. et al 2015][research_heathchristopherm_grayjustins_2015]
- [Heather P Houlden and Erin Hubbard][research_heatherphoulden_erinhubbard]
- [Hedrick et al 2026][research_hedrick_friman_2026]
- [Heidenreich et al 2017][research_heidenreich_gross_2017]
- [Heine, J. C. 1964][research_heinejc_1964]
- [Heister 2008][research_heister_2008]
- [Hellman 2006][research_hellman_2006]
- [Hellman et al 2013][research_hellman_pleiman_2013]
- [Hellman et al 2011][research_hellman_remillard_2011]
- [Hellman and Tejtel 2008][research_hellman_tejtel_2008]
- [Hellman et al 2011][research_hellman_wallace_2011]
- [Hemsch, Michael J. 2016][research_hemschmichaelj_2016]
- [Hemsch, Michael J. et al 2008][research_hemschmichaelj_hankejeremyl_2008]
- [Hendershot, K. C. 1966][research_hendershotkc_1966]
- [Henderson et al 2016][research_henderson_mathews_2016]
- [Hendrix, J. M. 1969][research_hendrixjm_1969]
- [Hennen, H. A. and Lambert, R. F. 1968][research_hennenha_lambertrf_1968]
- [Henning, Allen B. 1959][research_henningallenb_1959]
- [Herbell, Thomas P. and Eckel, Andrew J. 1991][research_herbellthomasp_eckelandrewj_1991]
- [Herbert, Phillip W., Sr. et al 2015][research_herbertphillipwsr_elliotalexc_2015]
- [Herbert, Phillip W., Sr. et al 2017][research_herbertphillipwsr_elliottalexc_2017]
- [Hergert et al 2017][research_hergert_brock_2017]
- [Hergert, Jakob D. et al 2017][research_hergertjakobd_brockjosephm_2017]
- [Hermance 1961][research_hermance_1961]
- [Herrera 2023][research_herrera_2023]
- [Herrick 1968][research_herrick_1968]
- [Herrick, W. D. et al 1990][research_herrickwd_penegorgt_1990]
- [Herron, Andrew J. et al 2016][research_herronandrewj_crosbywilliama_2016]
- [Hertzfeld 2000][research_hertzfeld_2000]
- [Herzog et al 1998][research_herzog_yue_1998]
- [Hess and James 1975][research_hess_james_1975]
- [Hessling 2011][research_hessling_2011]
- [Hetmaniok et al 2024][research_hetmaniok_brociek_2024]
- [Heuston et al 1967][research_heuston_fish_1967]
- [Hickam, W. M. and Sternbergh, S. A. 1966][research_hickamwm_sternberghsa_1966]
- [Hiers et al 2003][research_hiers_mackinnon_2003]
- [Higgins et al 1964][research_higgins_jacobson_1964]
- [High-Load Strain Gauge Balance 2018][research_high_load_strain_2018]
- [Hill 1963][research_hill_1963]
- [Hill, A. and Acosta, E. 2005][research_hilla_acostae_2005]
- [Hillje, E. R. and Nelson, R. L. 1981][research_hilljeer_nelsonrl_1981]
- [Hill, K. H. et al 1971][research_hillkh_leighouro_1971]
- [Hills 1985][research_hills_1985]
- [Hillsley and Robbins 1964][research_hillsley_robbins_1964]
- [Hilten 1970][research_hilten_1970]
- [Hinchey 1968][research_hinchey_1968]
- [Hinedi, S. et al 1991][research_hinedis_bevanr_1991]
- [Hinedi, Sami M. et al 1993][research_hinedisamim_bevanrolandp_1993]
- [Hines, John W. et al 1995][research_hinesjohnw_sompschris_1995]
- [Hinrichs 2006][research_hinrichs_2006]
- [Hodel, A. S. et al 2002][research_hodelas_callahanronnie_2002]
- [Hoertel 1961][research_hoertel_1961]
- [Hoff 2007][research_hoff_2007]
- [Hoff, H. L. 1965][research_hoffhl_1965]
- [Hogie, Keith et al 2004][research_hogiekeith_crisuoloed_2004]
- [Holdhusen and Perusse 1965][research_holdhusen_perusse_1965]
- [Holgersen, L. et al 1966][research_holgersenl_knutsone_1966]
- [Holmes, J. K. 1979][research_holmesjk_1979]
- [Holmes, R. G. and Stagner, H. R. 1964][research_holmesrg_stagnerhr_1964]
- [Holmes, R. G. and Stagner, H. R. 1965][research_holmesrg_stagnerhr_1965]
- [Holmes, Richard et al 1999][research_holmesrichard_ellisdavid_1999]
- [Holt, James B. et al 2015][research_holtjamesb_deespatrickd_2015]
- [Homquest, D. L. 1970][research_homquestdl_1970]
- [Honeycutt, John and Lyles, Garry 2016][research_honeycuttjohn_lylesgarry_2016]
- [Hong et al 2026][research_hong_wang_2026]
- [Hong et al 2014][research_hong_xiong_2014]
- [Hooke 1979][research_hooke_1979]
- [Hooke, Adrian J. et al 1990][research_hookeadrianj_macmedanmervynl_1990]
- [Hooke, A. J. and Greenberg, E. 1985][research_hookeaj_greenberge_1985]
- [Hopkins, P. M. 1972][research_hopkinspm_1972]
- [Hopko, Russell N 1954][research_hopkorusselln_1954]
- [Hopson, George D. and McAnelly, William B. 1966][research_hopsongeorged_mcanellywilliamb_1966]
- [Horan 2003][research_horan_2003]
- [Horiuchi, H. S. 1964][research_horiuchihs_1964]
- [Horiuchi, H. S. and Martin, N. L. 1965][research_horiuchihs_martinnl_1965]
- [Horneman and Kluever 2004][research_horneman_kluever_2004]
- [Horner, Ward and Sabia, Steve 1989][research_hornerward_sabiasteve_1989]
- [Hornstein 1965][research_hornstein_1965]
- [Horton, J. A. et al 1966][research_hortonja_masseyhn_1966]
- [Hosack 1969][research_hosack_1969]
- [Hosack and Stromsta 1969][research_hosack_stromsta_1969]
- [Houts, R. C. et al 1968][research_houtsrc_parsonsfd_1968]
- [Howard, F. G. et al 1983][research_howardfg_goodmanwl_1983]
- [Howard, F. G. and Goodman, W. L. 1984][research_howardfg_goodmanwl_1984]
- [Howard, F. G. and Goodman, W. L. 1985][research_howardfg_goodmanwl_1985]
- [Howell, Robert R. and Braslow, Albert L. 1955][research_howellrobertr_braslowalbertl_1955]
- [H S Alpert et al 2021][research_hsalpert_ramiller_2021]
- [Hu 2025][research_hu_2025]
- [Hu et al 2021][research_hu_bai_2021]
- [Hu et al 2015][research_hu_deng_2015]
- [Hu and Wang 2012][research_hu_wang_2012]
- [Huang 1974][research_huang_1974]
- [Huang 2023][research_huang_2023]
- [Huang 2026][research_huang_2026]
- [Huang et al 2024][research_huang_cheng_2024]
- [Huang et al 2024][research_huang_cheng_2024_b]
- [Huang et al 2025][research_huang_cheng_2025]
- [Huang et al 2016][research_huang_gardner_2016]
- [Huang et al 2021][research_huang_xia_2021]
- [Huang et al 2024][research_huang_xie_2024]
- [Huang and Yao 2020][research_huang_yao_2020]
- [Huang et al 2015][research_huang_zhang_2015]
- [Huang and Zhang 2026][research_huang_zhang_2026]
- [Huang et al 2017][research_huang_zhao_2017]
- [Hubbard, Erin P. 2019][research_hubbarderinp_2019]
- [Huberman et al 1970][research_huberman_kidd_1970]
- [Hudgins, J. I. and Lease, J. R. 1969][research_hudginsji_leasejr_1969]
- [Hudson et al 1981][research_hudson_brosz_1981]
- [Hudson et al 2000][research_hudson_zoladz_2000]
- [Hudson, Susan T. et al 2002][research_hudsonsusant_zoladzthomasf_2002]
- [Huegel, Fred 1998][research_huegelfred_1998]
- [Huerta 1969][research_huerta_1969]
- [Hueter, Uwe 2000][research_hueteruwe_2000]
- [Huffman, Jr. et al 1996][research_huffmanjr_tilmann_1996]
- [Hughes, Mark S. et al 2007][research_hughesmarks_davisdawnm_2007]
- [Hulka 2008][research_hulka_2008]
- [Hull 1967][research_hull_1967]
- [Hummel 1995][research_hummel_1995]
- [Hunley 2008][research_hunley_2008]
- [Hunley 2008][research_hunley_2008_b]
- [Hunley 2008][research_hunley_2008_c]
- [Hunter, Gary W. and Behbahani, Alireza 2012][research_huntergaryw_behbahanialireza_2012]
- [Huntley, S. C. and Samanich, N. E. 1969][research_huntleysc_samanichne_1969]
- [Huppi, Hal et al 2003][research_huppihal_tobiasmark_2003]
- [Hurd, W. J. et al 1988][research_hurdwj_browndh_1988]
- [Hurley, M. J. 1972][research_hurleymj_1972]
- [Hurt, G. J. and Lina, L. J. 1964][research_hurtgj_linalj_1964]
- [Husick and Ritenour 1966][research_husick_ritenour_1966]
- [Husick and Ritenour 1967][research_husick_ritenour_1967]
- [Hutchison 2011][research_hutchison_2011]
- [Huzel 1993][research_huzel_1993]
- [Hybrid Rocket Propulsion for 1991][research_hybrid_rocket_1991]
- [Hybrid Rocket Engines 2019][research_hybrid_rocket_2019]
- [Hyde 2002][research_hyde_2002]
- [Hyde and Argueta 2025][research_hyde_argueta_2025]
- [Hyde, Charles R. and Massie, Jeffrey J. 1993][research_hydecharlesr_massiejeffreyj_1993]
- [Hydrogen peroxide hybrid rocket 1994][research_hydrogen_peroxide_1994]
- [Hydrostatic bearings for cryogenic 1969][research_hydrostatic_bearings_1969]
- [Hynes, R. T. 1967][research_hynesrt_1967]
- [Hynes, R. T. 1968][research_hynesrt_1968]
- [Iaconis and D'Emilia 1994][research_iaconis_demilia_1994]
- [Iafrate et al 2025][research_iafrate_brandonisio_2025]
- [Ibell][research_ibell]
- [Idźkowski et al 2016][research_idzkowski_walendziuk_2016]
- [Iglesias et al 2015][research_iglesias_haynes_2015]
- [Iguchi and Matsuoka 2014][research_iguchi_matsuoka_2014]
- [Iliopoulou et al 2004][research_iliopoulou_denos_2004]
- [Imbaratto][research_imbaratto]
- [Imhuelse et al 2024][research_imhuelse_zydel_2024]
- [Imlach, Joseph et al 2008][research_imlachjoseph_kasardamary_2008]
- [Immich and Caporicci 1996][research_immich_caporicci_1996]
- [Implantable telemetry for small 1982][research_implantable_telemetry_1982]
- [In-Flight Thrust Determination for][research_in_flight_thrust]
- [In-Flight Thrust Determination][research_in_flight_thrust_b]
- [Inatani et al 1999][research_inatani_naruo_1999]
- [Inatomi et al 2019][research_inatomi_kitamura_2019]
- [India to launch prototype 2015][research_india_to_2015]
- [Ingels, Frank et al 1989][research_ingelsfrank_parkerglenn_1989]
- [Inokuchi 1996][research_inokuchi_1996]
- [Instability Phenomenology and Case 1995][research_instability_phenomenology_1995]
- [Instability Phenomenology and Case 1995][research_instability_phenomenology_1995_b]
- [Instability Phenomenology and Case 1995][research_instability_phenomenology_1995_c]
- [Instability Phenomenology and Case 1995][research_instability_phenomenology_1995_d]
- [Instrumentation for Telemetry, Testing 2023][research_instrumentation_for_2023]
- [Integral sensor telemetry final 1965][research_integral_sensor_1965]
- [Integrated Advanced Microwave Sounding 2000][research_integrated_advanced_2000]
- [Intelligence and Neuroscience 2023][research_intelligenceandneuroscience_2023]
- [Inturi et al 2025][research_inturi_lovaraju_2025]
- [Inui et al 2009][research_inui_kawahara_2009]
- [Irimpan et al 2015][research_irimpan_mannil_2015]
- [Irons, James R. and Irish, Richard R. 1988][research_ironsjamesr_irishrichardr_1988]
- [Ishida et al 2015][research_ishida_sekikawa_2015]
- [Ishikawa, R. et al 2018][research_ishikawar_kanor_2018]
- [Ishikawa, Ryohko et al 2019][research_ishikawaryohko_mckenziedavid_2019]
- [Ishimoto et al 2005][research_ishimoto_fujii_2005]
- [Ishimoto et al 1996][research_ishimoto_takizawa_1996]
- [Islam 2024][research_islam_2024]
- [ISRO Releases the Special 2018][research_isro_releases_the_2018]
- [Issitt et al 2026][research_issitt_mahendrakar_2026]
- [Ito and Fujii 2001][research_ito_fujii_2001]
- [Ito and Fujii 2002][research_ito_fujii_2002]
- [Ito and Fujii 2003][research_ito_fujii_2003]
- [Ito and Fujii 2003][research_ito_fujii_2003_b]
- [Ivanova and Khoroshilov 2023][research_ivanova_khoroshilov_2023]
- [Iwabuchi and Hashimoto 2025][research_iwabuchi_hashimoto_2025]
- [Jack, John R 1953][research_jackjohnr_1953]
- [Jackson, C. M., Jr. and Smith, R. S. 1969][research_jacksoncmjr_smithrs_1969]
- [Jackson, H Herbert et al 1950][research_jacksonhherbert_rumseycharlesb_1950]
- [Jackson, H Herbert et al 1954][research_jacksonhherbert_rumseycharlesb_1954]
- [Jackson, Jerry E. et al 1998][research_jacksonjerrye_espenschiederich_1998]
- [Jackson, Markus Deon 2015][research_jacksonmarkusdeon_2015]
- [Jackson, W. H. and Eaton, J. P. 1971][research_jacksonwh_eatonjp_1971]
- [Jacob 2008][research_jacob_2008]
- [Jadhav et al 2020][research_jadhav_kulkarni_2020]
- [Jain and Kumar 2022][research_jain_kumar_2022]
- [James, Carlton S. 1960][research_jamescarltons_1960]
- [James, Carlton S and Carros, Robert J 1953][research_jamescarltons_carrosrobertj_1953]
- [James, K. and Quick, B. 1984][research_jamesk_quickb_1984]
- [James M Ramey et al][research_jamesmramey_ianmgiles]
- [Jamie G. Meeroff et al][research_jamiegmeeroff_derekjdalle]
- [Jamison, D. E. 1965][research_jamisonde_1965]
- [Jamison, D. E. 1966][research_jamisonde_1966]
- [Janardan, B. A. et al 1985][research_janardanba_majjigirk_1985]
- [Jang, Jiann-Woei et al 2011][research_jangjiannwoei_alanizabran_2011]
- [Jannette, Anthony G. et al 2002][research_jannetteanthonyg_hojnickijeffreys_2002]
- [Japan's Liquid Propellant Rocket-Engine 2006][research_japan_s_liquid_2006]
- [J A Sterhardt 1965][research_jasterhardt_1965]
- [Jategaonkar et al 2006][research_jategaonkar_behr_2006]
- [Jeb S. Orr et al][research_jebsorr_timothymbarrows]
- [Jeff Hagen et al][research_jeffhagen_michaelburlone]
- [Jenke 1976][research_jenke_1976]
- [Jenkins 1970][research_jenkins_1970]
- [Jenkins, George 1986][research_jenkinsgeorge_1986]
- [Jenkins, Rhonald M. 1997][research_jenkinsrhonaldm_1997]
- [Jenkins, Rhonald M. and Foster, Winfred A., Jr. 1993][research_jenkinsrhonaldm_fosterwinfredajr_1993]
- [Jenn and Nelson 1988][research_jenn_nelson_1988]
- [Jenne 2006][research_jenne_2006]
- [Jensen 2001][research_jensen_2001]
- [Jensen 2001][research_jensen_2001_b]
- [Jensen 2002][research_jensen_2002]
- [Jensen 2003][research_jensen_2003]
- [Jensen 2005][research_jensen_2005]
- [Jensen et al 1962][research_jensen_goshgarian_1962]
- [Jeremy T Pinier][research_jeremytpinier]
- [Jernell, L. S. and Croom, D. R. 1979][research_jernellls_croomdr_1979]
- [Jet Thrust Measurement In 2003][research_jet_thrust_2003]
- [Jetevator for rocket engine 1998][research_jetevator_for_1998]
- [Jha 2024][research_jha_2024]
- [Jha et al 2013][research_jha_m_2013]
- [Jha et al 2016][research_jha_sullivan_2016]
- [Ji et al 2012][research_ji_wang_2012]
- [Jiandong et al 2020][research_jiandong_qiang_2020]
- [Jiang et al 2012][research_jiang_dong_2012]
- [Jiang et al 2023][research_jiang_jiang_2023]
- [Jiang and Ordonez 2008][research_jiang_ordonez_2008]
- [Jiang and Ordóñez 2009][research_jiang_ordonez_2009]
- [Jiang, Hui and Horan, Stephen 2000][research_jianghui_horanstephen_2000]
- [Jianguo et al 2016][research_jianguo_guoqing_2016]
- [Jiao et al 2002][research_jiao_leger_2002]
- [Jie Li et al][research_jieli_elaralash]
- [Jie Li et al][research_jieli_nettiehroozeboom]
- [Jie Li et al][research_jieli_nettiehroozeboom_b]
- [Jin et al 2024][research_jin_shang_2024]
- [Jin et al 2022][research_jin_tian_2022]
- [J J Donegan 1958][research_jjdonegan_1958]
- [Joachim Balis et al 2025][research_joachimbalis_hervelamy_2025]
- [Johan Klun et al 2020][research_johanklun_brucelipe_2020]
- [John Henry Korth][research_johnhenrykorth]
- [John Henry Korth et al][research_johnhenrykorth_jonathanmburt]
- [John Henry Korth et al 2025][research_johnhenrykorth_jonathanmburt_2025]
- [John H. Wall et al][research_johnhwall_colterwrussell]
- [Johns, A. L. 1969][research_johnsal_1969]
- [Johnson 1972][research_johnson_1972]
- [Johnson et al 2006][research_johnson_jacobs_2006]
- [Johnson and Servidio 2008][research_johnson_servidio_2008]
- [Johnson, Harold S and Hayes, William C 1953][research_johnsonharolds_hayeswilliamc_1953]
- [Johnson, Katie 2016][research_johnsonkatie_2016]
- [Johnson, Martin L. and Crawford, Kevin 2011][research_johnsonmartinl_crawfordkevin_2011]
- [John S Tripp 1999][research_johnstripp_1999]
- [Jones 2004][research_jones_2004]
- [Jones and Bergquist 1977][research_jones_bergquist_1977]
- [Jones and Jr 1993][research_jones_jr_1993]
- [Jones et al 2000][research_jones_townsend_2000]
- [Jones, Daniel S. et al 2014][research_jonesdaniels_rufjosephh_2014]
- [Jones, H. B., Jr. et al 1965][research_joneshbjr_knauerrc_1965]
- [Jones, Jonathan et al 2014][research_jonesjonathan_kibbeytim_2014]
- [Jones, Kenneth M. 1994][research_joneskennethm_1994]
- [Jones, Kenneth W. and Zoller, Lowell K. 1989][research_joneskennethw_zollerlowellk_1989]
- [Jones, Kenneth W. and Zoller, Lowell K. 1989][research_joneskennethw_zollerlowellk_1989_b]
- [Jones, R. H. 1970][research_jonesrh_1970]
- [Jones, Robert T and Margolis, Kenneth 1946][research_jonesrobertt_margoliskenneth_1946]
- [Jones, Ron et al 2017][research_jonesron_smithdan_2017]
- [Jones, R. T. and Margolis, K. 1976][research_jonesrt_margolisk_1976]
- [Joseph A Wehrmeyer 2002][research_josephawehrmeyer_2002]
- [Joseph Hernandez-McCloskey et al][research_josephhernandezmccloskey_sethareutlinger]
- [Jourdaine et al 2019][research_jourdaine_tsuboi_2019]
- [J. S. Adams et al 2020][research_jsadams_ajanderson_2020]
- [Juhlin and Jakobsson 2023][research_juhlin_jakobsson_2023]
- [Julian S. Hamilton][research_julianshamilton]
- [Junaid R and Beebi M 2015][research_junaidr_beebim_2015]
- [Jung 2018][research_jung_2018]
- [Jurist 2009][research_jurist_2009]
- [Just 1991][research_just_1991]
- [Justin G. Chen et al][research_justingchen_raulrios]
- [K A et al 2025][research_ka_parikh_2025]
- [Kachler and Beaurain 2005][research_kachler_beaurain_2005]
- [Kah 1970][research_kah_1970]
- [Kajita 2019][research_kajita_2019]
- [Kalden 2007][research_kalden_2007]
- [Kammer et al 1963][research_kammer_smith_1963]
- [Kamperman 1957][research_kamperman_1957]
- [Kanazaki et al 2016][research_kanazaki_ito_2016]
- [Kan, E. 1994][research_kane_1994]
- [Kan, Edwin P. 1994][research_kanedwinp_1994]
- [Kang et al 2018][research_kang_wang_2018]
- [Kannengieser et al 2010][research_kannengieser_colin_2010]
- [Kann, M. N. 1966][research_kannmn_1966]
- [Kanso et al 2022][research_kanso_jha_2022]
- [Kantor, A. V. et al 1974][research_kantorav_perevertkinsm_1974]
- [Kanwar 2024][research_kanwar_2024]
- [Kao, Simon A. et al 1987][research_kaosimona_laffeythomasj_1987]
- [Kaplan 2002][research_kaplan_2002]
- [Kapoor 1982][research_kapoor_1982]
- [Karel 1967][research_karel_1967]
- [Karen A. Deere et al 2024][research_karenadeere_stevenekrist_2024]
- [Kargin 2014][research_kargin_2014]
- [Karim et al 2026][research_karim_some_2026]
- [Karlgaard et al 2018][research_karlgaard_tynis_2018]
- [Karlgaard et al 2019][research_karlgaard_tynis_2019]
- [Karlgaard, Christopher D. et al 2013][research_karlgaardchristopherd_kuttyprasad_2013]
- [Karlgaard, Christopher D. et al 2005][research_karlgaardchristopherd_martinjohng_2005]
- [Karlgaard, Christopher D. et al 2004][research_karlgaardchristopherd_tartabinipaulv_2004]
- [Karras, T. J. 1969][research_karrastj_1969]
- [Karthikeyan et al 2016][research_karthikeyan_aravindhkumar_2016]
- [Karthikeyan et al 2009][research_karthikeyan_verma_2009]
- [Kassner, D. L. and Wettlaufer, B. 1977][research_kassnerdl_wettlauferb_1977]
- [Kassoy 1997][research_kassoy_1997]
- [Kato et al 2021][research_kato_yamada_2021]
- [Katsarelis, Colton et al 2019][research_katsareliscolton_chenpo_2019]
- [Katz, Ellis R 1947][research_katzellisr_1947]
- [Katz, Ellis R 1949][research_katzellisr_1949]
- [Kawai and Hasegawa 2024][research_kawai_hasegawa_2024]
- [Kawamura 1952][research_kawamura_1952]
- [Kawamura and Karashima 1957][research_kawamura_karashima_1957]
- [Kawasaki et al 2020][research_kawasaki_yokoo_2020]
- [Kawatsu et al 2020][research_kawatsu_tsutsumi_2020]
- [Kazeminejad, B. et al 2005][research_kazeminejadb_atkinsondh_2005]
- [Keast 1960][research_keast_1960]
- [Keast 1961][research_keast_1961]
- [Kegenbekov and Saparova 2022][research_kegenbekov_saparova_2022]
- [Keith 1995][research_keith_1995]
- [Keith, E. L. and Rothschild, W. J. 1998][research_keithel_rothschildwj_1998]
- [Keith, E. L. and Rothschild, W. J. 1999][research_keithel_rothschildwj_1999]
- [Kelly et al 2009][research_kelly_charania_2009]
- [Kelly, G. M. et al 1985][research_kellygm_mcconnelljg_1985]
- [Keltner et al 1988][research_keltner_bainbridge_1988]
- [Kennedy, Paul and Sims, Herb 2000][research_kennedypaul_simsherb_2000]
- [Kenneth J. Davidian et al 1987][research_kennethjdavidian_ronaldhdieck_1987]
- [Kenneth McAfee et al][research_kennethmcafee_hannahalpert]
- [Kenny, Jeremy et al 2009][research_kennyjeremy_hobbschris_2009]
- [Kenny, R. Jeremy et al 2011][research_kennyrjeremy_leeerik_2011]
- [Kent Frankovich et al][research_kentfrankovich_mahadevankrishnan]
- [Kent Frankovich et al][research_kentfrankovich_mahadevankrishnan_b]
- [Kerzhanovich, Viktor and Pichkhadze, Konstantin 2003][research_kerzhanovichviktor_pichkhadzekonstantin_2003]
- [Keyhani, M. 1993][research_keyhanim_1993]
- [Khairul BMQ Zaman and Amy F Fagan 2023][research_khairulbmqzaman_amyffagan_2023]
- [Khairul B M Q Zaman et al 2024][research_khairulbmqzaman_amyffagan_2024]
- [Khairul BMQ Zaman et al][research_khairulbmqzaman_johnhkorth]
- [Khairul B M Q Zaman et al 2025][research_khairulbmqzaman_johnhkorth_2025]
- [Khairul Zaman et al][research_khairulzaman_amyfagan]
- [Khalid et al 2025][research_khalid_qureshi_2025]
- [Khalil et al 2009][research_khalil_abdalla_2009]
- [Khamlak 2026][research_khamlak_2026]
- [Khatun et al 2013][research_khatun_laitinen_2013]
- [Khavaran, A. et al 1996][research_khavarana_dasap_1996]
- [Kibbey 2024][research_kibbey_2024]
- [Kidd 1981][research_kidd_1981]
- [Kijima et al 2013][research_kijima_mitsukura_2013]
- [Kim 2005][research_kim_2005]
- [Kim 2026][research_kim_2026]
- [Kim et al 2008][research_kim_keidar_2008]
- [Kim et al 2026][research_kim_ko_2026]
- [Kim et al 2024][research_kim_woldeyohannis_2024]
- [Kim et al 2001][research_kim_yoo_2001]
- [Kim, Jungho et al 2000][research_kimjungho_bentonjohn_2000]
- [King 1976][research_king_1976]
- [King, E. L. and Shaffer, H. W. 1968][research_kingel_shafferhw_1968]
- [King, Michael C. et al 2016][research_kingmichaelc_bognarjohn_2016]
- [Kinman, P. W. 1983][research_kinmanpw_1983]
- [Kinney, Frank 1997][research_kinneyfrank_1997]
- [Kintner, P. M. et al 1997][research_kintnerpm_arnoldyr_1997]
- [Kinzie and McLaughlin 1997][research_kinzie_mclaughlin_1997]
- [Kirby and Martinez 1977][research_kirby_martinez_1977]
- [Kirby, Randy L. et al 2003][research_kirbyrandyl_manndavid_2003]
- [Kiris, Cetin et al 2001][research_kiriscetin_chanwilliam_2001]
- [Kiris, Cetin et al 2002][research_kiriscetin_chanwilliam_2002]
- [Kiris, Cetin and Williams, Robert 2000][research_kiriscetin_williamsrobert_2000]
- [Kirkham, Harold 1992][research_kirkhamharold_1992]
- [Kirsch and Schuhmann 2012][research_kirsch_schuhmann_2012]
- [Kirschbaum and Sheridan 1966][research_kirschbaum_sheridan_1966]
- [Kitsche 2010][research_kitsche_2010]
- [Kitsios and Lygeros][research_kitsios_lygeros]
- [Kless and Aftosmis 2011][research_kless_aftosmis_2011]
- [Kluever and Horneman 2005][research_kluever_horneman_2005]
- [Kluever et al 2009][research_kluever_horneman_2009]
- [Knacke 1985][research_knacke_1985]
- [Knapp 1999][research_knapp_1999]
- [Knaur 1966][research_knaur_1966]
- [Knaur 1967][research_knaur_1967]
- [Knaur 1968][research_knaur_1968]
- [Knight and Tso 2005][research_knight_tso_2005]
- [Knipp et al 2006][research_knipp_street_2006]
- [Knopf, William P. 2007][research_knopfwilliamp_2007]
- [Knott, P. R. et al 1981][research_knottpr_blozyjt_1981]
- [Knott, P. R. et al 1980][research_knottpr_brauschjf_1980]
- [Knott, P. R. et al 1981][research_knottpr_janardanba_1981]
- [Knott, P. R. et al 1984][research_knottpr_janardanba_1984]
- [Knuth et al 1999][research_knuth_gramer_1999]
- [Kochergin et al 2009][research_kochergin_shi_2009]
- [Kochetova and Levenets 2026][research_kochetova_levenets_2026]
- [Koeberlein, Ernest, III and Pender, Shaw Exum 1994][research_koeberleinernestiii_pendershawexum_1994]
- [Koelle 1981][research_koelle_1981]
- [Koelle 1984][research_koelle_1984]
- [Koelle 1992][research_koelle_1992]
- [Koelle 1998][research_koelle_1998]
- [Koerner, M. A. 1984][research_koernerma_1984]
- [Koerner, M. A. 1989][research_koernerma_1989]
- [Koester et al 1998][research_koester_meltzer_1998]
- [Kohtake et al 2000][research_kohtake_kawabata_2000]
- [Kokuyama et al 2022][research_kokuyama_shimoda_2022]
- [Komar and Christenson 1996][research_komar_christenson_1996]
- [Konda et al 2011][research_konda_singla_2011]
- [Konigsberg, E. 1976][research_konigsberge_1976]
- [Konkin et al 2018][research_konkin_kolesenkov_2018]
- [Konno et al 1998][research_konno_kishimoto_1998]
- [Koomphati 2017][research_koomphati_2017]
- [Korkegi and Freeman 1976][research_korkegi_freeman_1976]
- [Korte 2000][research_korte_2000]
- [Korte et al 1997][research_korte_salas_1997]
- [Korte et al 2001][research_korte_salas_2001]
- [Korte, J. J. et al 1997][research_kortejj_salasao_1997]
- [Korting and Reitsma 1985][research_korting_reitsma_1985]
- [Koschel 1998][research_koschel_1998]
- [Kosmann et al 1978][research_kosmann_dionne_1978]
- [Kostromin et al 2001][research_kostromin_sokolov_2001]
- [Kothapalli 2022][research_kothapalli_2022]
- [Kothari and Webber 2010][research_kothari_webber_2010]
- [Ko, W. H. et al 1979][research_kowh_hynecekj_1979]
- [Kraft 1975][research_kraft_1975]
- [Kral et al 2009][research_kral_horn_2009]
- [Kranz et al 2016][research_kranz_english_2016]
- [Krause and Blum 2004][research_krause_blum_2004]
- [Krebs, Richard P. and Hart, Clint E. 1959][research_krebsrichardp_hartclinte_1959]
- [Krejci et al 2017][research_krejci_petri_2017]
- [Kris, Cetin C. and Kwak, Dochan 2001][research_kriscetinc_kwakdochan_2001]
- [Krishnamoorthy and Marius 2025][research_krishnamoorthy_marius_2025]
- [Krishnamurthy et al 2013][research_krishnamurthy_shende_2013]
- [Kristina Rojdev et al][research_kristinarojdev_antonywilliams]
- [Kristina Rojdev et al][research_kristinarojdev_jennydevolites]
- [Krystek 2000][research_krystek_2000]
- [Ksica et al 2018][research_ksica_hadas_2018]
- [Kubo, M. et al 2014][research_kubom_kanor_2014]
- [Kulick, J. H. 1970][research_kulickjh_1970]
- [Kulkarni and Achenbach 2008][research_kulkarni_achenbach_2008]
- [Kumakawa et al 1998][research_kumakawa_onodera_1998]
- [Kumar et al 2017][research_kumar_gopalsamy_2017]
- [Kumar et al 2012][research_kumar_mishra_2012]
- [Kumar et al 2011][research_kumar_misra_2011]
- [Kumar Mishra et al 2021][research_kumarmishra_goswami_2021]
- [Kunz 1967][research_kunz_1967]
- [Kuo et al 1993][research_kuo_kokal_1993]
- [Kuo, Kenneth K. et al 1994][research_kuokennethk_luyc_1994]
- [Kurbjun, Max C 1954][research_kurbjunmaxc_1954]
- [Kurbjun, Max C and Thompson, Jim Rogers 1952][research_kurbjunmaxc_thompsonjimrogers_1952]
- [Kurita et al 2020][research_kurita_jourdaine_2020]
- [Kurtenbach, A. J. and Wintz, P. A. 1967][research_kurtenbachaj_wintzpa_1967]
- [Kurtenbach, A. J. and Wintz, P. A. 1968][research_kurtenbachaj_wintzpa_1968]
- [Kutschera and Render 1999][research_kutschera_render_1999]
- [Kutter 2006][research_kutter_2006]
- [Kuzin et al 2009][research_kuzin_lozin_2009]
- [Kuzuu et al 2011][research_kuzuu_kitamura_2011]
- [LaBelle, Remi et al 2009][research_labelleremi_bernardoabner_2009]
- [Lacarna, R. J. and Wissinger, D. B. 1982][research_lacarnarj_wissingerdb_1982]
- [Lacefield and Sprow 1994][research_lacefield_sprow_1994]
- [Lacroix, W. P. 1973][research_lacroixwp_1973]
- [Ladeinde and Chen 2010][research_ladeinde_chen_2010]
- [Laera 2015][research_laera_2015]
- [Lagouanelle and Gall 2024][research_lagouanelle_gall_2024]
- [Lai et al 2018][research_lai_wei_2018]
- [Lakey and Schlippe 2024][research_lakey_schlippe_2024]
- [Lamb 1987][research_lamb_1987]
- [Lan and Li 2022][research_lan_li_2022]
- [Lancelle et al 2012][research_lancelle_bozic_2012]
- [Landers et al 2003][research_landers_hall_2003]
- [Landing Gear Structural Health][research_landing_gear]
- [Lane and Redman 1970][research_lane_redman_1970]
- [Lange, K. O. et al 1975][research_langeko_bellevillere_1975]
- [Langill, Jr. 1965][research_langilljr_1965]
- [Langner et al 2024][research_langner_gupta_2024]
- [Lanin 2012][research_lanin_2012]
- [Lanin 2012][research_lanin_2012_b]
- [Laporte et al 2025][research_laporte_perlin_2025]
- [Larin 2012][research_larin_2012]
- [Larina 1985][research_larina_1985]
- [Larsen 2000][research_larsen_2000]
- [Larsen 2003][research_larsen_2003]
- [Larsen 2005][research_larsen_2005]
- [Larsen, M. F. 2003][research_larsenmf_2003]
- [Larson 1973][research_larson_1973]
- [Larson, Richard R. 1999][research_larsonrichardr_1999]
- [Lash and Moeller 2015][research_lash_moeller_2015]
- [Laubacher, Brian A. 2000][research_laubacherbriana_2000]
- [Launch of SpaceX reusable 2014][research_launch_of_2014]
- [Launch Vehicle Systems][research_launch_vehicle]
- [Launch Vehicle Performance 1963][research_launch_vehicle_1963]
- [Launch Vehicle Systems and 2022][research_launch_vehicle_2022]
- [Launch Vehicle Performance and 2022][research_launch_vehicle_2022_b]
- [Lauren Griggs et al][research_laurengriggs_jacobmoseley]
- [Lawrence 2005][research_lawrence_2005]
- [Lawson, Denise L. and James, Mark L. 1989][research_lawsondenisel_jamesmarkl_1989]
- [Lawson, Denise L. and James, Mark L. 1989][research_lawsondenisel_jamesmarkl_1989_b]
- [Lazarev et al 2017][research_lazarev_tarabrin_2017]
- [Lazur et al 1999][research_lazur_sawyer_1999]
- [Lazzarin et al 2012][research_lazzarin_bellomo_2012]
- [Le and Yu 2015][research_le_yu_2015]
- [Leachman, Jonathan 2010][research_leachmanjonathan_2010]
- [Lechter, S. S. 1964][research_lechterss_1964]
- [Lederer 2021][research_lederer_2021]
- [Lee 1963][research_lee_1963]
- [Lee 1964][research_lee_1964]
- [Lee 2020][research_lee_2020]
- [Lee 2026][research_lee_2026]
- [Lee et al 2026][research_lee_jo_2026]
- [Lee and Lee 2020][research_lee_lee_2020]
- [Lee et al 1997][research_lee_olds_1997]
- [Lee and Pomerantz 2015][research_lee_pomerantz_2015]
- [Lee, Allan Y. et al 2010][research_leeallany_strahanalan_2010]
- [Lee, C. C. 1966][research_leecc_1966]
- [Lee, Hyun H. 2012][research_leehyunh_2012]
- [Lee, Jonathan A. et al 2001][research_leejonathana_elamsandy_2001]
- [Lee, R. 1976][research_leer_1976]
- [Leese 1966][research_leese_1966]
- [Lei et al 2026][research_lei_chen_2026]
- [Lei et al 2019][research_lei_hongbo_2019]
- [Lei et al 2017][research_lei_yan_2017]
- [Lei et al 2022][research_lei_zhang_2022]
- [Lei, Jih-Fen et al 1998][research_leijihfen_willherberta_1998]
- [Leitner 1986][research_leitner_1986]
- [Leland H Jorgensen et al 1962][research_lelandhjorgensen_jrichardspahr_1962]
- [Lemaster, R. A. and Runyan, R. B. 1983][research_lemasterra_runyanrb_1983]
- [Lemberger et al 1991][research_lemberger_patanchon_1991]
- [Lemieux 2009][research_lemieux_2009]
- [Lemieux and Murray 2012][research_lemieux_murray_2012]
- [Lengade 2021][research_lengade_2021]
- [Leng, Christopher and Peet, Arthur 1988][research_lengchristopher_peetarthur_1988]
- [Lerch, B. A. et al 2002][research_lerchba_nathalmv_2002]
- [Lesho, Jeffery C. and Eaton, Harry A. C. 1993][research_leshojefferyc_eatonharryac_1993]
- [Lesieutre et al 1994][research_lesieutre_lesieutre_1994]
- [Lester, Daniel 1994][research_lesterdaniel_1994]
- [Letchworth 2011][research_letchworth_2011]
- [Letchworth and Letchworth 2000][research_letchworth_letchworth_2000]
- [Levenets 2018][research_levenets_2018]
- [Levenets et al 2017][research_levenets_bogachev_2017]
- [Levine, Jack et al 1960][research_levinejack_martzcwilliam_1960]
- [Levitan and Buchsbaum 1996][research_levitan_buchsbaum_1996]
- [Lewak 1967][research_lewak_1967]
- [Lewallen, Pat 1987][research_lewallenpat_1987]
- [Lewis, Mark E. et al 2019][research_lewismarke_gibsontracyl_2019]
- [Lewis, T. L. and Dods, J. B., Jr. 1972][research_lewistl_dodsjbjr_1972]
- [Li et al 2022][research_li_an_2022]
- [Li et al 2022][research_li_chen_2022]
- [Li et al 2011][research_li_fan_2011]
- [Li et al 2022][research_li_long_2022]
- [Li et al 2026][research_li_paik_2026]
- [Li et al 2021][research_li_qiao_2021]
- [Li et al 2026][research_li_ren_2026]
- [Li et al 2002][research_li_schemel_2002]
- [Li et al 2018][research_li_sun_2018]
- [Li et al 2017][research_li_wu_2017]
- [Li et al 2020][research_li_xing_2020]
- [Li et al 2020][research_li_yang_2020]
- [Li and Yang 2020][research_li_yang_2020_b]
- [Li et al 2019][research_li_zhang_2019]
- [Li et al 2025][research_li_zhao_2025]
- [Lian et al 2013][research_lian_bai_2013]
- [Lian et al 2026][research_lian_liangji_2026]
- [Lian et al 2026][research_lian_wang_2026]
- [Liaoni Wu et al 2008][research_liaoniwu_yiminhuang_2008]
- [Lieske and Kochenderfer 1966][research_lieske_kochenderfer_1966]
- [Ligrani, P. M. et al 1989][research_ligranipm_baunlr_1989]
- [Li Guojun et al 2013][research_liguojun_shijian_2013]
- [Lijewski 1980][research_lijewski_1980]
- [Lijewski 1981][research_lijewski_1981]
- [Lijewski 1982][research_lijewski_1982]
- [Lilley, R. W. 1974][research_lilleyrw_1974]
- [Lim, Tae W. 1991][research_limtaew_1991]
- [Lim, Tae W. 1992][research_limtaew_1992]
- [Lin][research_lin]
- [Lin 1989][research_lin_1989]
- [Lin et al 2010][research_lin_figueroa_2010]
- [Lin et al 2003][research_lin_huang_2003]
- [Lin et al 2020][research_lin_wu_2020]
- [Lin et al 2023][research_lin_yang_2023]
- [Lin, C. F. et al 2009][research_lincf_figueroaf_2009]
- [Lin, Chujen et al 2007][research_linchujen_lonskeben_2007]
- [Lindgren et al 2011][research_lindgren_buynak_2011]
- [Lindsay and Jordan 1975][research_lindsay_jordan_1975]
- [Lineberry et al 2004][research_lineberry_coleman_2004]
- [Liou, Larry C. 1999][research_lioularryc_1999]
- [Liquid Propellant Rocket-Engine Organizations 2006][research_liquid_propellant_2006]
- [Liquid-Propellant Rocket Engine 2005][research_liquid_propellant_rocket_2005]
- [Liquid Rocket Engine Reliability][research_liquid_rocket]
- [Liquid rocket engine nozzles 1976][research_liquid_rocket_1976]
- [Liquid Rocket Engine Combustion 1995][research_liquid_rocket_1995]
- [Liquid Rocket Engine Thrust 2018][research_liquid_rocket_2018]
- [Liquid Rocket Engines 2019][research_liquid_rocket_2019]
- [Lisano, Michael E. and Jah, Moriba 2004][research_lisanomichaele_jahmoriba_2004]
- [Lisano, Michael E. and Jah, Moriba 2004][research_lisanomichaele_jahmoriba_2004_b]
- [Litt, Jonathan S. et al 1994][research_littjonathans_musgravejeffreyl_1994]
- [Little 1992][research_little_1992]
- [Littlefield, Alan C. and Melton, Gregory S. 1999][research_littlefieldalanc_meltongregorys_1999]
- [Littlefield, Alan C. and Melton, Gregory S. 2000][research_littlefieldalanc_meltongregorys_2000]
- [Litvin et al 2012][research_litvin_dudley_2012]
- [Liu 2009][research_liu_2009]
- [Liu 2023][research_liu_2023]
- [Liu 2024][research_liu_2024]
- [Liu et al 2022][research_liu_cheng_2022]
- [liu et al 2026][research_liu_cheng_2026]
- [Liu et al 2017][research_liu_dai_2017]
- [Liu et al 2008][research_liu_gao_2008]
- [Liu et al 2026][research_liu_guo_2026]
- [Liu et al 2026][research_liu_guo_2026_b]
- [Liu et al 2010][research_liu_hou_2010]
- [Liu et al 2025][research_liu_liu_2025]
- [Liu et al 2024][research_liu_lu_2024]
- [Liu et al 2005][research_liu_maurer_2005]
- [Liu and Tan 2024][research_liu_tan_2024]
- [Liu et al 2001][research_liu_zhang_2001]
- [Liu et al 2025][research_liu_zhang_2025]
- [Liu et al 2025][research_liu_zhu_2025]
- [Liu, Chung-Chiun 1994][research_liuchungchiun_1994]
- [Liu, G. 1985][research_liug_1985]
- [Liu, X. 2015][research_liux_2015]
- [Livingstone 1974][research_livingstone_1974]
- [Lizcano et al 2026][research_lizcano_martinez_2026]
- [Lobdell 1968][research_lobdell_1968]
- [Lobdell 1969][research_lobdell_1969]
- [Locke, Justin M. and Landrum, D. Brian 2005][research_lockejustinm_landrumdbrian_2005]
- [Loesch and Pawlowski 1973][research_loesch_pawlowski_1973]
- [Logsdon and Williamson 1997][research_logsdon_williamson_1997]
- [Lohrer, J. D. and Wright, R. D. 2016][research_lohrerjd_wrightrd_2016]
- [Lokerson, D. C. 1966][research_lokersondc_1966]
- [Lomax, Harvard 1957][research_lomaxharvard_1957]
- [London et al 2000][research_london_epstein_2000]
- [Long et al 2013][research_long_joyner_2013]
- [Long et al 2026][research_long_li_2026]
- [Longenecker and Clark 2007][research_longenecker_clark_2007]
- [Lopatoff, Mitchell 1951][research_lopatoffmitchell_1951]
- [Lopes and Silva 2005][research_lopes_silva_2005]
- [Loposer, J Dan and Mottard, Elmo J 1953][research_loposerjdan_mottardelmoj_1953]
- [Lord 1978][research_lord_1978]
- [Lorenzo 1995][research_lorenzo_1995]
- [Lorenzo et al][research_lorenzo_merrill]
- [Lorenzo, Carl F. et al 1998][research_lorenzocarlf_holmesmichaels_1998]
- [Lorenzo, Carl F. and Musgrave, Jeffrey L. 1991][research_lorenzocarlf_musgravejeffreyl_1991]
- [Lorio, L. A. 1970][research_loriola_1970]
- [Losik 2008][research_losik_2008]
- [Losik 2010][research_losik_2010]
- [Losik 2010][research_losik_2010_b]
- [Losik 2010][research_losik_2010_c]
- [Losik 2012][research_losik_2012]
- [Losik 2012][research_losik_2012_b]
- [Losik 2012][research_losik_2012_c]
- [Losik, Ph.D. 2012][research_losikphd_2012]
- [Loubeyre, Jean Philippe 1994][research_loubeyrejeanphilippe_1994]
- [Love, Eugene S et al 1952][research_loveeugenes_colettidonalde_1952]
- [Lovell, R. R. and Nieberding, W. C. 1966][research_lovellrr_nieberdingwc_1966]
- [Lowe][research_lowe]
- [Low, P. W. 1977][research_lowpw_1977]
- [Loyd, J. R. and Pickard, R. F. 1967][research_loydjr_pickardrf_1967]
- [Lu 1997][research_lu_1997]
- [Lu and Wang 2013][research_lu_wang_2013]
- [Lu and Zhou 2017][research_lu_zhou_2017]
- [Luan et al 2010][research_luan_tang_2010]
- [Luan et al 2024][research_luan_xue_2024]
- [Lucci and Hodson 1975][research_lucci_hodson_1975]
- [Lucht and Charest 1996][research_lucht_charest_1996]
- [Luckert 1973][research_luckert_1973]
- [Ludwig et al 2025][research_ludwig_gruber_2025]
- [Ludwig, George H. 1961][research_ludwiggeorgeh_1961]
- [Lugo, Rafael A. et al 2018][research_lugorafaela_karlgaardchristopherd_2018]
- [Lugo, Rafael A. et al 2013][research_lugorafaela_tolsonroberth_2013]
- [Lui, C. Y. and Mason, D. R. 1991][research_luicy_masondr_1991]
- [Luke, Gary D. and Dwyer, Harry A. 1992][research_lukegaryd_dwyerharrya_1992]
- [Lukin et al 2021][research_lukin_prisiazhnyi_2021]
- [Lumb, D. R. 1971][research_lumbdr_1971]
- [Lumb, D. R. and Viterbi, A. J. 1971][research_lumbdr_viterbiaj_1971]
- [Luo and Kareem 2021][research_luo_kareem_2021]
- [Luo et al 2019][research_luo_tan_2019]
- [Luton 1963][research_luton_1963]
- [Lv et al 2012][research_lv_yu_2012]
- [Lydon and Va 1995][research_lydon_va_1995]
- [Lynch, T. J. 1967][research_lynchtj_1967]
- [Lynch, T. J. 1967][research_lynchtj_1967_b]
- [Lyon Inc Detroit Mi 1963][research_lyonincdetroitmi_1963]
- [Lyons, J. T. 1993][research_lyonsjt_1993]
- [M et al 2025][research_m_ka_2025]
- [Ma et al 2023][research_ma_bao_2023]
- [Ma et al 2005][research_ma_deng_2005]
- [Ma et al 2022][research_ma_pan_2022]
- [Ma et al 2013][research_ma_tang_2013]
- [Ma et al 2018][research_ma_wang_2018]
- [Ma et al 2019][research_ma_wang_2019]
- [Macagno and Hsieh 1963][research_macagno_hsieh_1963]
- [Macbeth 1989][research_macbeth_1989]
- [Macconochie, Ian O. and Breiner, Charles A. 1989][research_macconochieiano_breinercharlesa_1989]
- [MacConochie, Ian O. and Briener, Charles A. 1991][research_macconochieiano_brienercharlesa_1991]
- [Macconochie, Ian O. et al 1989][research_macconochieiano_martinjamesa_1989]
- [Macgregor, C. A. 1982][research_macgregorca_1982]
- [Mach, D. M. and Koshak, W. J. 2006][research_machdm_koshakwj_2006]
- [Mach, D. M. and Koshak, W. J. 2007][research_machdm_koshakwj_2007]
- [Mackall, D. et al 1998][research_mackalld_sakaharar_1998]
- [Mackey et al 2009][research_mackey_krasowski_2009]
- [Mackey and Kulikov 2010][research_mackey_kulikov_2010]
- [Mackey, Jon et al 2014][research_mackeyjon_sehirlioglualp_2014]
- [Mackey, Jon et al 2014][research_mackeyjon_sehirlioglualp_2014_b]
- [MacLean and Rodriguez 1996][research_maclean_rodriguez_1996]
- [Macmedan, M. L. 1985][research_macmedanml_1985]
- [Madsen, Boyd D. 1987][research_madsenboydd_1987]
- [Madzsar et al 1994][research_madzsar_bickford_1994]
- [Madzsar, G. C. et al 1992][research_madzsargc_bickfordrl_1992]
- [Maestrello, L. 1978][research_maestrellol_1978]
- [Magier and Merda 2017][research_magier_merda_2017]
- [Magnani et al 2026][research_magnani_sozio_2026]
- [Mahapatra et al 2008][research_mahapatra_sriram_2008]
- [Maharaja, Rishabh 2016][research_maharajarishabh_2016]
- [Mahmood et al 2026][research_mahmood_zulfiqar_2026]
- [Mahoney, M. and Quann, J. J. 1964][research_mahoneym_quannjj_1964]
- [Mahzari, Milad and White, Todd 2017][research_mahzarimilad_whitetodd_2017]
- [Mai et al 2013][research_mai_vogt_2013]
- [Mainini 2017][research_mainini_2017]
- [Mains 2011][research_mains_2011]
- [Majumdar, Alok and Flachbart, Robin 2003][research_majumdaralok_flachbartrobin_2003]
- [Majumdar, Alok et al 2000][research_majumdaralok_polsgroverobert_2000]
- [Malik et al 2023][research_malik_salauddin_2023]
- [Mallon, Joseph R., Jr. 1992][research_mallonjosephrjr_1992]
- [Malone, Michael B. and Peavey, Charles C. 1999][research_malonemichaelb_peaveycharlesc_1999]
- [Maluf et al][research_maluf_hsu]
- [Mana and Pennecchi 2007][research_mana_pennecchi_2007]
- [Manalo, Natividad D. and Smith, G. L. 1991][research_manalonatividadd_smithgl_1991]
- [Mandal and Mukhopadhyay 2023][research_mandal_mukhopadhyay_2023]
- [Manders, A. M. and Sussman, S. M. 1964][research_mandersam_sussmansm_1964]
- [Manish Mehta et al][research_manishmehta_andrewcolbert]
- [Manish Mehta et al][research_manishmehta_markahooton]
- [Manish Mehta et al][research_manishmehta_sheldondsmith]
- [Manish Mehta and Thomas B Steva][research_manishmehta_thomasbsteva]
- [Manish Mehta and Thomas Steva][research_manishmehta_thomassteva]
- [Manop et al 2025][research_manop_tanghengjareon_2025]
- [Mansfield, D. L. 1973][research_mansfielddl_1973]
- [Manski and Fina 1994][research_manski_fina_1994]
- [Manski, Detlef and Martin, James A. 1988][research_manskidetlef_martinjamesa_1988]
- [Manusubramanian et al 2014][research_manusubramanian_sumitra_2014]
- [Mao et al 2016][research_mao_sinn_2016]
- [Mao et al 2016][research_mao_sinn_2016_b]
- [Maram 1993][research_maram_1993]
- [Maram, J. and Barkhoudarian, S. 1987][research_maramj_barkhoudarians_1987]
- [Marchese, V. P. 1974][research_marchesevp_1974]
- [Marchese, V. P. et al 1972][research_marchesevp_rakowskyel_1972]
- [Marchetti et al 2021][research_marchetti_minisci_2021]
- [Mari 2009][research_mari_2009]
- [Mario Santos et al][research_mariosantos_serhathosder]
- [Marko et al 1961][research_marko_mclennan_1961]
- [Markowsky and McManus 1974][research_markowsky_mcmanus_1974]
- [Marks 1977][research_marks_1977]
- [Markusic, T. E. et al 2004][research_markusicte_jonesje_2004]
- [Marlow 2003][research_marlow_2003]
- [Marquez 2013][research_marquez_2013]
- [Marsik, S. J. and Gawrylowicz, H. T. 1986][research_marsiksj_gawrylowiczht_1986]
- [Marsik, S. J. and Morea, S. F. 1985][research_marsiksj_moreasf_1985]
- [Marsik, S. J. and Morea, S. F. 1985][research_marsiksj_moreasf_1985_b]
- [Marsilio et al 2024][research_marsilio_resta_2024]
- [Martin 1962][research_martin_1962]
- [Martin 2006][research_martin_2006]
- [Martin and Brazzel 1970][research_martin_brazzel_1970]
- [Martin et al 2024][research_martin_stay_2024]
- [Martin, C. L. 1983][research_martincl_1983]
- [Martindale 2006][research_martindale_2006]
- [Martinez and Jortner 1964][research_martinez_jortner_1964]
- [Martinez et al 1990][research_martinez_reinert_1990]
- [Martinez, Elmain et al 2004][research_martinezelmain_mcauleymyche_2004]
- [Martin, James A. 1993][research_martinjamesa_1993]
- [Martin, James A. and Kramer, Richard D. 1990][research_martinjamesa_kramerrichardd_1990]
- [Martin, James A. and Manski, Detlef 1989][research_martinjamesa_manskidetlef_1989]
- [Martin, Lisa C. et al 2001][research_martinlisac_wrbanekjohnd_2001]
- [Mart L. Cook et al 2003][research_martlcook_laurentgruet_2003]
- [Maru et al 2026][research_maru_kobayashi_2026]
- [Maruyama et al 2006][research_maruyama_matsushima_2006]
- [Masdari et al 2018][research_masdari_tahani_2018]
- [Masilamani et al 2018][research_masilamani_kumar_2018]
- [Mason-Smith 2017][research_masonsmith_2017]
- [Masri 2000][research_masri_2000]
- [Massey, David and Corbin, Brian 1990][research_masseydavid_corbinbrian_1990]
- [Massey, D. E. 1986][research_masseyde_1986]
- [Massey, D. E. and Corbin, B. 1991][research_masseyde_corbinb_1991]
- [Massey, H. N. 1966][research_masseyhn_1966]
- [Mastrocola, N 1947][research_mastrocolan_1947]
- [Mastromatteo et al 2026][research_mastromatteo_gaverina_2026]
- [Matharu and Devi 2020][research_matharu_devi_2020]
- [Mathes, H. B. 1980][research_matheshb_1980]
- [Mathews, Charles W and Thompson, Jim Rogers 1947][research_mathewscharlesw_thompsonjimrogers_1947]
- [Mathison, R. P. 1965][research_mathisonrp_1965]
- [Matsukawa et al 2019][research_matsukawa_watanabe_2019]
- [Matsumoto, T. et al 1976][research_matsumotot_chiseldm_1976]
- [Matthew Aaron Maybee 2025][research_matthewaaronmaybee_2025]
- [Matthew A Maybee et al][research_matthewamaybee_michaelahemming]
- [Matthew P Fritz et al][research_matthewpfritz_javieradoll]
- [Matthews 1957][research_matthews_1957]
- [Matveev et al 2018][research_matveev_zubanov_2018]
- [Maughmer, M. et al 1993][research_maughmerm_ozoroskil_1993]
- [Maughmer, M. et al 1991][research_maughmerm_straussfogeld_1991]
- [Maughmer, Mark D. et al 1990][research_maughmermarkd_ozoroskil_1990]
- [Maurer 1995][research_maurer_1995]
- [Ma Xiaoli et al 2011][research_maxiaoli_wanglibin_2011]
- [Maynard 1969][research_maynard_1969]
- [Maynard, Bryon T. and Raines, Nickey G. 2010][research_maynardbryont_rainesnickeyg_2010]
- [May, Todd A. and Creech, Stephen D. 2012][research_maytodda_creechstephend_2012]
- [Mazurov and Takovitskii 2022][research_mazurov_takovitskii_2022]
- [McAmis 1995][research_mcamis_1995]
- [Mcanally and Engel 1979][research_mcanally_engel_1979]
- [McClure 1998][research_mcclure_1998]
- [McCorkel, J. et al 2015][research_mccorkelj_czaplamyersj_2015]
- [Mccoy, K. E. and Hester, J. 1985][research_mccoyke_hesterj_1985]
- [McCutcheon, David Matthew 2017][research_mccutcheondavidmatthew_2017]
- [Mccutcheon, E. P. et al 1977][research_mccutcheonep_mirandar_1977]
- [McDonald, Kathleen R. and Wooten, John R. 2000][research_mcdonaldkathleenr_wootenjohnr_2000]
- [McDowell et al 2025][research_mcdowell_raghu_2025]
- [Mcgarvey 1973][research_mcgarvey_1973]
- [Mcgarvey 1979][research_mcgarvey_1979]
- [Mcgee, R. S. and Say, M. B. 1966][research_mcgeers_saymb_1966]
- [McGrath 1996][research_mcgrath_1996]
- [Mcintosh et al 1972][research_mcintosh_knowles_1972]
- [McKenna 1981][research_mckenna_1981]
- [McKenna 1990][research_mckenna_1990]
- [McKinney, Linwood W. 1960][research_mckinneylinwoodw_1960]
- [Mclachlan, B. G. et al 1992][research_mclachlanbg_belljh_1992]
- [Mclafferty 1970][research_mclafferty_1970]
- [McLeod, Christopher 2004][research_mcleodchristopher_2004]
- [Mcmillin and Wood 1986][research_mcmillin_wood_1986]
- [McMillin and Wood 1987][research_mcmillin_wood_1987]
- [Mcnair, L. L. 1962][research_mcnairll_1962]
- [Mcnichol, Randal S. 1996][research_mcnicholrandals_1996]
- [McWhorter 2003][research_mcwhorter_2003]
- [McWhorter and Ewing 2001][research_mcwhorter_ewing_2001]
- [Mease et al 1999][research_mease_teufel_1999]
- [Measurement of neutron capture][research_measurement_of]
- [Measurement Uncertainty Applied to][research_measurement_uncertainty]
- [Measurement Uncertainty 2002][research_measurement_uncertainty_2002]
- [Measurement Uncertainty 2017][research_measurement_uncertainty_2017]
- [Measurement uncertainty concepts 2024][research_measurement_uncertainty_2024]
- [Measurement Uncertainty 2024][research_measurement_uncertainty_2024_b]
- [Meda 2020][research_meda_2020]
- [Medelius, Pedro J. et al 1994][research_medeliuspedroj_hallbergcarl_1994]
- [Medelius, Pedro J. et al 1998][research_medeliuspedroj_hallbergcarlg_1998]
- [Medical Telemetry 1978][research_medical_telemetry_1978]
- [Medlin 1965][research_medlin_1965]
- [Medukhovskii 1961][research_medukhovskii_1961]
- [M E Eckart et al 2013][research_meeckart_jsadams_2013]
- [Mehta et al 2014][research_mehta_dufrene_2014]
- [Mehta, Manish et al 2011][research_mehtamanish_canabalfrancisco_2011]
- [Mehta, Manish et al 2016][research_mehtamanish_knoxkyle_2016]
- [Meiboom 1993][research_meiboom_1993]
- [Meiboom and Geerdes 1995][research_meiboom_geerdes_1995]
- [Meigs and Stine 1969][research_meigs_stine_1969]
- [Meigs and Stine 1970][research_meigs_stine_1970]
- [Meija and Mester 2008][research_meija_mester_2008]
- [Meisl 1986][research_meisl_1986]
- [Meisl 1988][research_meisl_1988]
- [Meisl 1989][research_meisl_1989]
- [Meisl 1992][research_meisl_1992]
- [Mekid and Vaja 2008][research_mekid_vaja_2008]
- [Melchior 1990][research_melchior_1990]
- [Mellodge and Kachroo 2010][research_mellodge_kachroo_2010]
- [Mencattini et al 2009][research_mencattini_rabottino_2009]
- [Mencattini et al 2007][research_mencattini_salmeri_2007]
- [Menon 2016][research_menon_2016]
- [Ménou][research_menou]
- [Meo and Zumpano 2004][research_meo_zumpano_2004]
- [Meo and Zumpano 2005][research_meo_zumpano_2005]
- [Mercer, C. E. and Burley, J. R., II 1985][research_mercerce_burleyjrii_1985]
- [Mercer, C. E. and Salters, L. B., Jr. 1963][research_mercerce_salterslbjr_1963]
- [Meredith et al 1981][research_meredith_kelly_1981]
- [Mermagen 1964][research_mermagen_1964]
- [Mermagen 1964][research_mermagen_1964_b]
- [Merrill and Lorenzo 1988][research_merrill_lorenzo_1988]
- [Merrill, Walter C. and Lorenzo, Carl F. 1988][research_merrillwalterc_lorenzocarlf_1988]
- [Merrill, W. C. et al 1992][research_merrillwc_musgravejl_1992]
- [Merryman, H. L. and Smith, L. R. 1974][research_merrymanhl_smithlr_1974]
- [Methods of uncertainty propagation 2014][research_methods_of_2014]
- [Meyer and Elko 2008][research_meyer_elko_2008]
- [Meyer, Claudia M. 2000][research_meyerclaudiam_2000]
- [Meyers et al 2003][research_meyers_lu_2003]
- [Meyerson 1998][research_meyerson_1998]
- [Meyn 2000][research_meyn_2000]
- [Micci 1975][research_micci_1975]
- [Michael A. Bolender 2006][research_michaelabolender_2006]
- [Michael Cooper][research_michaelcooper]
- [Michael James Hays et al][research_michaeljameshays_jenniferrrobinson]
- [Michael J Hays et al 2024][research_michaeljhays_jenniferrrobinson_2024]
- [Michael Lee et al][research_michaellee_derekdalle]
- [Michaels et al 2012][research_michaels_michaels_2012]
- [Michael Zemcov et al 2025][research_michaelzemcov_jamesjbock_2025]
- [Michalski and Johnson 2007][research_michalski_johnson_2007]
- [Michigan Univ Ann Arbor 1963][research_michiganunivannarbor_1963]
- [Micklow, Gerald J. 1996][research_micklowgeraldj_1996]
- [Miele and Hull 1963][research_miele_hull_1963]
- [Mikhail 1979][research_mikhail_1979]
- [Millard et al 1982][research_millard_barton_1982]
- [Milleman 1967][research_milleman_1967]
- [Miller and Washington 1994][research_miller_washington_1994]
- [Miller, C. G. 2000][research_millercg_2000]
- [Miller, C. G., III 1982][research_millercgiii_1982]
- [Miller, E. E. 1965][research_milleree_1965]
- [Miller, E. F. et al 1968][research_milleref_nieberdingwc_1968]
- [Miller, Geoffrey et al 1996][research_millergeoffrey_richwinedavidm_1996]
- [Miller, W. et al 1967][research_millerw_mullerr_1967]
- [Miller, W. et al 1968][research_millerw_mullerr_1968]
- [Miller, W. et al 1971][research_millerw_mullerr_1971]
- [Miller, Warner H. et al 1990][research_millerwarnerh_morakisjamesc_1990]
- [Milliken 1963][research_milliken_1963]
- [Milos, Frank S. et al 2002][research_milosfranks_karunaratnek_2002]
- [Milos, Frank S. et al 2001][research_milosfranks_wattersdg_2001]
- [Minaz and Meram 2025][research_minaz_meram_2025]
- [Minderman, P. A. 1966][research_mindermanpa_1966]
- [Miniature Onboard Data Acquisition 2023][research_miniature_onboard_2023]
- [Miotto and LePome 2003][research_miotto_lepome_2003]
- [Mireles Jr. et al 2026][research_mirelesjr_jimenez_2026]
- [Mironov and Serdyuk 2012][research_mironov_serdyuk_2012]
- [Mirzabayova and Rustamov 2024][research_mirzabayova_rustamov_2024]
- [Mitra, D. et al 1998][research_mitrad_bhallapn_1998]
- [Mizukami, Masashi et al 1998][research_mizukamimasashi_corpeninggriffinp_1998]
- [M.J. Cooper et al][research_mjcooper_depaxson]
- [M. J. Quinn 1966][research_mjquinn_1966]
- [Mo et al 2022][research_mo_li_2022]
- [Mo et al 2024][research_mo_wang_2024]
- [Modular Program for Conceptual 2007][research_modular_program_2007]
- [Moeller, Trevor and Polzin, Kurt A. 2010][research_moellertrevor_polzinkurta_2010]
- [Moes et al 1996][research_moes_cobleigh_1996]
- [Moes et al 1998][research_moes_cobleigh_1998]
- [Mohammad Barani et al][research_mohammadbarani_weichaotu]
- [Mohammadikaji et al 2016][research_mohammadikaji_bergmann_2016]
- [Mohler 1965][research_mohler_1965]
- [Moix-Bonet et al 2017][research_moixbonet_schmidt_2017]
- [Mokhtar et al 2025][research_mokhtar_ibrahim_2025]
- [Mokin et al 2022][research_mokin_kalashnikov_2022]
- [Molina et al 2009][research_molina_johnson_2009]
- [Molland 1978][research_molland_1978]
- [Molleda et al 2012][research_molleda_usamentiaga_2012]
- [Monaco et al 2025][research_monaco_viscardi_2025]
- [Monnoyer et al 2026][research_monnoyer_louveaux_2026]
- [Monnoyer et al 2026][research_monnoyer_louveaux_2026_b]
- [Montesinos et al 2026][research_montesinos_davis_2026]
- [Monti et al 1992][research_monti_fortezza_1992]
- [Moog et al 1979][research_moog_bacchus_1979]
- [Moon][research_moon]
- [Mooney, James T. and Stahl, H. Phil 2005][research_mooneyjamest_stahlhphil_2005]
- [Mooney, James T. and Stahl, H. Philip 2005][research_mooneyjamest_stahlhphilip_2005]
- [Moore 2005][research_moore_2005]
- [Moore et al 2007][research_moore_kuo_2007]
- [Moore, Carleton J. 1988][research_moorecarletonj_1988]
- [Moore, Charlotte 2010][research_moorecharlotte_2010]
- [Moore, Dennis R. and Phelps, Willie J. 2011][research_mooredennisr_phelpswilliej_2011]
- [Moore, D. R. and Phelps, W. J. 2011][research_mooredr_phelpswj_2011]
- [Moore, F. G. et al 1993][research_moorefg_hymert_1993]
- [Moore, J. W. and Tcheng, P. 1969][research_moorejw_tchengp_1969]
- [Moore, Thomas C., Sr. 2004][research_moorethomascsr_2004]
- [Moore, W. M. 1963][research_moorewm_1963]
- [Moran and Beran 1995][research_moran_beran_1995]
- [Morgan 2015][research_morgan_2015]
- [Morgan, Dwayne R. et al 2001][research_morgandwayner_streichrong_2001]
- [Morin 1978][research_morin_1978]
- [Morris 1961][research_morris_1961]
- [Morris 2002][research_morris_2002]
- [Morris 2004][research_morris_2004]
- [Morris and Crowley 2016][research_morris_crowley_2016]
- [Morris, Christopher I. 2001][research_morrischristopheri_2001]
- [Morris, R. A. et al 1991][research_morrisra_powellwr_1991]
- [Morse 1968][research_morse_1968]
- [Mossman and Perkins 2001][research_mossman_perkins_2001]
- [Mottard, Elmo J and Loposer, J Dan 1954][research_mottardelmoj_loposerjdan_1954]
- [Mouneimne, Samih A. 1988][research_mouneimnesamiha_1988]
- [Moussa and Guedria 2026][research_moussa_guedria_2026]
- [Movva][research_movva]
- [Mu and Zhang 2014][research_mu_zhang_2014]
- [Mudford et al 2015][research_mudford_obyrne_2015]
- [Mudge 2023][research_mudge_2023]
- [Mudge 2025][research_mudge_2025]
- [Muehlner 1962][research_muehlner_1962]
- [Mueller 1964][research_mueller_1964]
- [Mueller 1966][research_mueller_1966]
- [Mueller et al 1999][research_mueller_bratkovich_1999]
- [Mueller and Sule 1973][research_mueller_sule_1973]
- [Mueller et al 2016][research_mueller_trigwell_2016]
- [Mueller, T. J. and Sule, W. P. 1972][research_muellertj_sulewp_1972]
- [Mufti 2002][research_mufti_2002]
- [Mukai, Ryan and Vilnrotter, Victor 2010][research_mukairyan_vilnrottervictor_2010]
- [Mukesh Reddy Dhanagari 2025][research_mukeshreddydhanagari_2025]
- [Mukhey, A. 1965][research_mukheya_1965]
- [Mukundan et al 2019][research_mukundan_maity_2019]
- [Mukundan et al 2022][research_mukundan_maity_2022]
- [Mulhall, B. D. L. et al 1975][research_mulhallbdl_benjauthritb_1975]
- [Mullen, C. R. and Kearnes, J. H. 1980][research_mullencr_kearnesjh_1980]
- [Muller, T. J. et al 1972][research_mullertj_sulewp_1972]
- [Mull, Harold R. and Algranti, Joseph S. 1960][research_mullharoldr_algrantijosephs_1960]
- [Mundt et al 2024][research_mundt_knowlen_2024]
- [Muralidhar and Bhandari 2017][research_muralidhar_bhandari_2017]
- [Muratore, John F. 1987][research_muratorejohnf_1987]
- [Murillo][research_murillo]
- [Murillo and Lu 2010][research_murillo_lu_2010]
- [Murphy, Kelly J. et al 1999][research_murphykellyj_nowakrobertj_1999]
- [Murphy, Terry 1999][research_murphyterry_1999]
- [Murray, Jonathan 1992][research_murrayjonathan_1992]
- [Murray-Krezan 2009][research_murraykrezan_2009]
- [Murthy, S. N. B. and Sheu, W. H. 1988][research_murthysnb_sheuwh_1988]
- [Musgrave 1991][research_musgrave_1991]
- [Musgrave, Jeffrey L. 1992][research_musgravejeffreyl_1992]
- [Musgrave, Jeffrey L. et al 1992][research_musgravejeffreyl_paxsondaniele_1992]
- [Myers, L. P. et al 1982][research_myerslp_mackallkg_1982]
- [Myrabo et al 2004][research_myrabo_raizer_2004]
- [Nagappa 2023][research_nagappa_2023]
- [Nagaral et al 2023][research_nagaral_r_2023]
- [Nagy, J. A. 1965][research_nagyja_1965]
- [Naik et al 2020][research_naik_holmgren_2020]
- [Nair and Kukreja 2025][research_nair_kukreja_2025]
- [Nair et al 2017][research_nair_suryan_2017]
- [Nair and Vaidyanathan 2022][research_nair_vaidyanathan_2022]
- [Najam 2014][research_najam_2014]
- [Nakabeppu and Dejima 2018][research_nakabeppu_dejima_2018]
- [Nakanishi et al 1982][research_nakanishi_sogame_1982]
- [Nakasuka et al 2006][research_nakasuka_funase_2006]
- [Nalin A Ratnayake et al 2020][research_nalinaratnayake_stevenekrist_2020]
- [Nallasamy, R. et al 2010][research_nallasamyr_kandulam_2010]
- [Namera et al 2010][research_namera_takaki_2010]
- [Naraghi, M. H. N. and Armstrong, E. S. 1988][research_naraghimhn_armstronges_1988]
- [Nardi Rezende 2018][research_nardirezende_2018]
- [Nardozzo et al 2019][research_nardozzo_popkin_2019]
- [Narimiya et al 2012][research_narimiya_tsuboi_2012]
- [Narukage, Noriyuki et al 2015][research_narukagenoriyuki_kanoryohei_2015]
- [Naseh and Alipoor 2021][research_naseh_alipoor_2021]
- [Nasution et al 2026][research_nasution_gianto_2026]
- [Nate Kelsey 2021][research_natekelsey_2021]
- [Nathaniel A Stepp 2024][research_nathanielastepp_2024]
- [Naughton, Jonathan W. et al 1996][research_naughtonjonathanw_brownjamesl_1996]
- [Naval Weapons Center China Lake Ca 1963][research_navalweaponscenterchinalakeca_1963]
- [Naval Weapons Center China Lake Ca 1964][research_navalweaponscenterchinalakeca_1964]
- [Nebiolo and Castro-Santos 2022][research_nebiolo_castrosantos_2022]
- [Needleman and Tackett 1973][research_needleman_tackett_1973]
- [Neerrukatti et al 2012][research_neerrukatti_liu_2012]
- [Negrão et al 1998][research_negrao_fanton_1998]
- [Negron-Martinez, Antonio Jose and Thomas, Taylor Walter 2018][research_negronmartinezantoniojose_thomastaylorwalter_2018]
- [Neiland, V. R. 1967][research_neilandvr_1967]
- [Nelius and Harris 1965][research_nelius_harris_1965]
- [Nelson 1988][research_nelson_1988]
- [Nelson, William J and Scott, William R 1958][research_nelsonwilliamj_scottwilliamr_1958]
- [Nelson, W. J. and Henry, B. Z., Jr. 1955][research_nelsonwj_henrybzjr_1955]
- [Nemeth, ED et al 1991][research_nemethed_andersonron_1991]
- [Nemzek, R. J. and Winckler, J. R. 1991][research_nemzekrj_wincklerjr_1991]
- [Nemzek, R. J. and Winckler, J. R. 1991][research_nemzekrj_wincklerjr_1991_b]
- [Nerlikar][research_nerlikar]
- [Nesman, Tom and Turner, James E. 2002][research_nesmantom_turnerjamese_2002]
- [Nesteruk and Cartwright 2011][research_nesteruk_cartwright_2011]
- [Nevins, C. D. 1975][research_nevinscd_1975]
- [Newcomb, A. W. 1988][research_newcombaw_1988]
- [Newman 2000][research_newman_2000]
- [Next Generation Structural Health 2024][research_next_generation_2024]
- [Next-Generation Telemetry Workstation 2008][research_next_generation_telemetry_2008]
- [Ng 1963][research_ng_1963]
- [Ngo and Blake 2003][research_ngo_blake_2003]
- [Ngo and Doman 2002][research_ngo_doman_2002]
- [Nguyen et al 2020][research_nguyen_kostiukov_2020]
- [Nguyen, Dalton 2002][research_nguyendalton_2002]
- [Nguyen, Dalton and Turner, Larry D. 2001][research_nguyendalton_turnerlarryd_2001]
- [Nguyen, Tien M. 1990][research_nguyentienm_1990]
- [Nguyen, Tien M. 1991][research_nguyentienm_1991]
- [Nguyen, Tien M. 1991][research_nguyentienm_1991_b]
- [Nguyen, Tien M. 1992][research_nguyentienm_1992]
- [Nguyen, Tien M. et al 1993][research_nguyentienm_hinedisamim_1993]
- [Nguyen, Tien Manh 1992][research_nguyentienmanh_1992]
- [Nguyen, T. M. 1988][research_nguyentm_1988]
- [Nguyen, T. M. 1990][research_nguyentm_1990]
- [Ni et al 2024][research_ni_fang_2024]
- [Ni and Fang 2024][research_ni_fang_2024_b]
- [Nicklaus O. Richardson et al 2020][research_nicklausorichardson_edmondwong_2020]
- [Nicolaides et al 1967][research_nicolaides_eikenberry_1967]
- [Nicoletti et al 2024][research_nicoletti_quarchioni_2024]
- [Niehus and Mracek 2010][research_niehus_mracek_2010]
- [Nielsen 1985][research_nielsen_1985]
- [Nielsen and Stratton 1995][research_nielsen_stratton_1995]
- [Nielsen, Jack N 1947][research_nielsenjackn_1947]
- [Niiya, Karen E. et al 1993][research_niiyakarene_walkerricharde_1993]
- [Nikbay, Melike and Heeg, Jennifer 2017][research_nikbaymelike_heegjennifer_2017]
- [Nikiforov et al 2026][research_nikiforov_tsymbalov_2026]
- [Nikolic and Jumper 2004][research_nikolic_jumper_2004]
- [Nishanth. N. R et al 2015][research_nishanthnr_rekhaks_2015]
- [Niu et al 2014][research_niu_zhao_2014]
- [Nix, Michael and Staton, Eric J. 2004][research_nixmichael_statonericj_2004]
- [Nix, Michael B. and Escher, William J. d. 1999][research_nixmichaelb_escherwilliamjd_1999]
- [Nizin et al 2016][research_nizin_antony_2016]
- [Noland et al 2026][research_noland_sanders_2026]
- [Nonaka et al 2012][research_nonaka_nishida_2012]
- [Nonaka et al 2001][research_nonaka_ogawa_2001]
- [Nonaka et al 2006][research_nonaka_watanabe_2006]
- [Nondestructive inspection and structural 2012][research_nondestructive_inspection_2012]
- [None 2017][research_none_2017]
- [Noneman 2002][research_noneman_2002]
- [Noori and Shahrokhi 2011][research_noori_shahrokhi_2011]
- [Normal Mode Decomposition Based 2017][research_normal_mode_decomposition_2017]
- [Norman et al 1988][research_norman_weiss_1988]
- [Normyle 1998][research_normyle_1998]
- [Noroozinejad Farsangi and Karimi Pour 2023][research_noroozinejadfarsangi_karimipour_2023]
- [Norris, J. S. et al 2000][research_norrisjs_backesp_2000]
- [Nosek, S. M. and Straight, D. M. 1976][research_noseksm_straightdm_1976]
- [Novozhilov et al 2018][research_novozhilov_marshakov_2018]
- [Nuclear rocket engine cycle 1963][research_nuclear_rocket_1963]
- [Numerical Method and Simulations 2016][research_numerical_method_2016]
- [Numerical Optimization on Approach 2016][research_numerical_optimization_2016]
- [Nurick, W. H. and Hines, W. S. 1973][research_nurickwh_hinesws_1973]
- [Nye 2013][research_nye_2013]
- [Obrien, Charles J. 1993][research_obriencharlesj_1993]
- [OBrien, Robin A. 2006][research_obrienrobina_2006]
- [Odom, J. B. 1972][research_odomjb_1972]
- [OFarrell, Zachary L. 2011][research_ofarrellzacharyl_2011]
- [Ogawa et al 2004][research_ogawa_nonaka_2004]
- [Ogbuji, Linus U. J. et al 2002][research_ogbujilinusuj_humphreydonaldh_2002]
- [Ogbuji, Linus U. Thomas and Humphrey, Donald L. 2002][research_ogbujilinusuthomas_humphreydonaldl_2002]
- [Ohmichi et al 2022][research_ohmichi_sugioka_2022]
- [Okabe and Wu 2016][research_okabe_wu_2016]
- [Okayasu et al 2002][research_okayasu_ohta_2002]
- [O'Keefe, Stephen A. and Bose, David M. 2010][research_okeefestephena_bosedavidm_2010]
- [Okino, Clayton et al 2006][research_okinoclayton_gaojay_2006]
- [Oktaviana et al 2026][research_oktaviana_alwan_2026]
- [Okuyama 2010][research_okuyama_2010]
- [Olds and Bellini 1998][research_olds_bellini_1998]
- [Olds and Budianto 1998][research_olds_budianto_1998]
- [Olds, Aaron D. et al 2013][research_oldsaarond_beckroger_2013]
- [Olivas et al 2026][research_olivas_vergeer_2026]
- [Olney and Shiftlett 1982][research_olney_shiftlett_1982]
- [Onodera et al 2003][research_onodera_sakamoto_2003]
- [Ooi et al 2023][research_ooi_rajan_2023]
- [Oota et al 2010][research_oota_usuda_2010]
- [Operative procedures for the 2014][research_operative_procedures_2014]
- [Optimizing the Performance of][research_optimizing_the]
- [Ortega et al 2023][research_ortega_amador_2023]
- [Osawa and Hewitt 1986][research_osawa_hewitt_1986]
- [Osborne, Robin et al 2001][research_osbornerobin_wehrmeyerjoseph_2001]
- [Othman et al 2022][research_othman_kashevnik_2022]
- [Othman et al 2022][research_othman_kashevnik_2022_b]
- [Otsuka 2026][research_otsuka_2026]
- [Otsuka 2026][research_otsuka_2026_b]
- [Otto, E. W. 1966][research_ottoew_1966]
- [Ou et al 2024][research_ou_xiao_2024]
- [Oxer and Blemings 2009][research_oxer_blemings_2009]
- [Ozelsel][research_ozelsel]
- [P et al 2024][research_p_p_2024]
- [Pace et al 2015][research_pace_eastburg_2015]
- [Pagendarm et al 1988][research_pagendarm_laurien_1988]
- [Palaniappan and Jameson 2004][research_palaniappan_jameson_2004]
- [Palaszewski, Bryan 1997][research_palaszewskibryan_1997]
- [Palaszewski, Bryan et al 1998][research_palaszewskibryan_olearyrobert_1998]
- [Palaszewski, Bryan A. 1998][research_palaszewskibryana_1998]
- [Pallela et al 2026][research_pallela_thakur_2026]
- [Pamadi, Bandu N. and Brauckmann, Gregory J. 1999][research_pamadibandun_brauckmanngregoryj_1999]
- [Pamela Poljak 2023][research_pamelapoljak_2023]
- [Pamela Poljak et al][research_pamelapoljak_aaronjohnson]
- [Pan and Bao 2025][research_pan_bao_2025]
- [Pan et al 2020][research_pan_guo_2020]
- [Pande 1994][research_pande_1994]
- [Pandey and Arora 2019][research_pandey_arora_2019]
- [Panneton, R. J. and Warren, W. B. 1969][research_pannetonrj_warrenwb_1969]
- [Pant][research_pant]
- [Parachute recovery system for 1966][research_parachute_recovery_1966]
- [Paramo and Arizpe 2024][research_paramo_arizpe_2024]
- [Parent 2004][research_parent_2004]
- [Park et al 2010][research_park_farrar_2010]
- [Park and Inman 2005][research_park_inman_2005]
- [Park et al 2025][research_park_kim_2025]
- [Parker, Hermon M 1955][research_parkerhermonm_1955]
- [Parker, Hermon M 1956][research_parkerhermonm_1956]
- [Parkes and Armbruster 2010][research_parkes_armbruster_2010]
- [Parkes et al 2014][research_parkes_mcclements_2014]
- [Parkes et al 2015][research_parkes_mcclements_2015]
- [Park, Ryan S. et al 2009][research_parkryans_bhaskaranshyam_2009]
- [Parzych, D. et al 1991][research_parzychd_boydl_1991]
- [Paschall and Brady 2012][research_paschall_brady_2012]
- [Paschke 2000][research_paschke_2000]
- [Pasternack, M. 1966][research_pasternackm_1966]
- [Pasternack, M. 1967][research_pasternackm_1967]
- [Patel, P. 1996][research_patelp_1996]
- [Patil 2022][research_patil_2022]
- [Patrick Champey][research_patrickchampey]
- [Patrick R Shea et al][research_patrickrshea_davidtchan]
- [Patrick S. Heaney et al][research_patricksheaney_djpiatak]
- [Patrick S Heaney et al][research_patricksheaney_francescosoranna]
- [Patterson, R. E. 1973][research_pattersonre_1973]
- [Paturzo et al 2009][research_paturzo_ferraro_2009]
- [Paul Gradl et al][research_paulgradl_chrisprotz]
- [Paulson et al 2020][research_paulson_kimura_2020]
- [Pavli, A. J. et al 1986][research_pavliaj_kacynskikj_1986]
- [Pavli, Albert J. et al 1987][research_pavlialbertj_kacynskikennethj_1987]
- [Paxson and Perkins 2021][research_paxson_perkins_2021]
- [Payne 1980][research_payne_1980]
- [Payne et al 1980][research_payne_hartley_1980]
- [Pearson 1976][research_pearson_1976]
- [Pedro J Medelius et al 2004][research_pedrojmedelius_carlostmata_2004]
- [Peery and Parsley 1996][research_peery_parsley_1996]
- [Pelaccio 1996][research_pelaccio_1996]
- [Pempie 2003][research_pempie_2003]
- [Penchuk and Schlundt 1969][research_penchuk_schlundt_1969]
- [Peng et al 1994][research_peng_zhang_1994]
- [Peretto et al 2005][research_peretto_sasdelli_2005]
- [Perez et al 2020][research_perez_gietler_2020]
- [Pérez Roca][research_perezroca]
- [Performance of Fusion-Fission Hybrid 1995][research_performance_of_1995]
- [Performance Optimization of Aerospike 2017][research_performance_optimization_2017]
- [Pergament, H. S. et al 1975][research_pergamenths_thorperd_1975]
- [Perkins, Edward W et al 1958][research_perkinsedwardw_jorgensenlelandh_1958]
- [Perlmutter and DePierre 1965][research_perlmutter_depierre_1965]
- [Pernet, D. F. 1966][research_pernetdf_1966]
- [Perrins 2012][research_perrins_2012]
- [Perry 1987][research_perry_1987]
- [Perry, John G. 1989][research_perryjohng_1989]
- [Perspectives on Integrating Structural][research_perspectives_on]
- [Pescetelli et al 2012][research_pescetelli_minisci_2012]
- [Peshkov and Tret'yakov 2024][research_peshkov_tretyakov_2024]
- [Peters 1981][research_peters_1981]
- [Peters et al 2006][research_peters_brost_2006]
- [Peterson, Chariya et al 1998][research_petersonchariya_rowejohn_1998]
- [Peterson, Chariya et al 1999][research_petersonchariya_rowejohn_1999]
- [Peterson, M. R. 1973][research_petersonmr_1973]
- [Peterson, M. R. 1975][research_petersonmr_1975]
- [Peterson, R. L. 1981][research_petersonrl_1981]
- [Petitjean and Musset 2026][research_petitjean_musset_2026]
- [Petrasek, Donald W. and Stephens, Joseph R. 1988][research_petrasekdonaldw_stephensjosephr_1988]
- [Petrasek, Donald W. and Stephens, Joseph R. 1989][research_petrasekdonaldw_stephensjosephr_1989]
- [Petrenko 2025][research_petrenko_2025]
- [Petrosky 1992][research_petrosky_1992]
- [Pettit et al 1999][research_pettit_barkhoudarian_1999]
- [Pettit, Richard L., Jr. 1988][research_pettitrichardljr_1988]
- [Peugeot, John et al 2014][research_peugeotjohn_garciachance_2014]
- [Philip C Calhoun et al][research_philipccalhoun_jonathanglickman]
- [Philipchuk 1953][research_philipchuk_1953]
- [Piatak, David J. et al 2015][research_piatakdavidj_sekulamartink_2015]
- [Piatak, David J. et al 2016][research_piatakdavidj_sekulamartink_2016]
- [Pickett, R. B. and Matthews, F. L. 1973][research_pickettrb_matthewsfl_1973]
- [Pidvysotskyi 2021][research_pidvysotskyi_2021]
- [Pieper, Jerry L. and Muss, Jeff 1989][research_pieperjerryl_mussjeff_1989]
- [Pierman, B. C. 1969][research_piermanbc_1969]
- [Pincus, B. R. et al 1971][research_pincusbr_stephensonjs_1971]
- [Pinier 2011][research_pinier_2011]
- [Pinier, Jeremy T. et al 2015][research_pinierjeremyt_ericksongarye_2015]
- [Piotr et al 2019][research_piotr_karol_2019]
- [Pires, Craig and Knudson, Matthew D. 2017][research_pirescraig_knudsonmatthewd_2017]
- [Pitts, K. J. 1974][research_pittskj_1974]
- [Plane 1963][research_plane_1963]
- [Plane 1964][research_plane_1964]
- [Plane 1964][research_plane_1964_b]
- [Plane 1964][research_plane_1964_c]
- [Plant, T. J. et al 1980][research_planttj_nugentj_1980]
- [Plasma propulsion for rocket 2011][research_plasma_propulsion_2011]
- [Platte et al 2017][research_platte_iwanczik_2017]
- [Plostins et al 1990][research_plostins_celmins_1990]
- [Podolchak 2019][research_podolchak_2019]
- [Pokela et al 2023][research_pokela_gustavsson_2023]
- [Poland and Schwanebeck 1970][research_poland_schwanebeck_1970]
- [Polge, R. J. and Wallace, G. R. 1969][research_polgerj_wallacegr_1969]
- [Polk, James E. et al 2013][research_polkjamese_pancottianthony_2013]
- [Pollet 1983][research_pollet_1983]
- [Polzin, Kurt A. et al 2006][research_polzinkurta_markusicthomase_2006]
- [Pomerantz, Marc et al 2015][research_pomerantzmarc_nguyenviet_2015]
- [Pomerantz, M. I. et al 2012][research_pomerantzmi_limc_2012]
- [Ponci and Johnson 2008][research_ponci_johnson_2008]
- [Popkov and Kornilov 2024][research_popkov_kornilov_2024]
- [Portell i de Mora][research_portellidemora]
- [Porter 1968][research_porter_1968]
- [Portz 2004][research_portz_2004]
- [Po-Shou Chen et al][research_poshouchen_benjaminlloydrupp]
- [Posner, E. C. et al 1969][research_posnerec_rodemicher_1969]
- [Postal, R. B. and Potts, C. M. 1966][research_postalrb_pottscm_1966]
- [Postflight Evaluation of Atlas-Centaur 1966][research_postflight_evaluation_1966]
- [Pouliquen 1978][research_pouliquen_1978]
- [Pourya Nikoueeyan et al][research_pouryanikoueeyan_michaeldhind]
- [Powell, Mark et al 2008][research_powellmark_mittmandavid_2008]
- [Powers, William T. et al 1988][research_powerswilliamt_sherrellfg_1988]
- [Prabhu, Ramadas K. 1999][research_prabhuramadask_1999]
- [Praharaj, Sarat C. and Palko, Richard L. 1986][research_praharajsaratc_palkorichardl_1986]
- [Prasad 2022][research_prasad_2022]
- [Prasad and Pal 2003][research_prasad_pal_2003]
- [Pribadi 2025][research_pribadi_2025]
- [Price, E. A. et al 1971][research_priceea_hulljj_1971]
- [Princeton Univ Nj 1952][research_princetonunivnj_1952]
- [Priskos, Alex 2016][research_priskosalex_2016]
- [Pritchard, James A. 1989][research_pritchardjamesa_1989]
- [Pritchett, Victor E. et al 2014][research_pritchettvictore_maylemelodyn_2014]
- [Problems in control system 1994][research_problems_in_1994]
- [Prognostic methodologies for remaining][research_prognostic_methodologies_for]
- [Progress made on experimental 2012][research_progress_made_2012]
- [Prokopec 1974][research_prokopec_1974]
- [Propagation of measurement uncertainty 2015][research_propagation_of_2015]
- [Propeller/Propfan In-Flight Thrust Determination][research_propeller_propfan_in_flight]
- [Prosser, William and Percy, Daniel 2003][research_prosserwilliam_percydaniel_2003]
- [Prosser, William H. et al 2004][research_prosserwilliamh_gormanmichaelr_2004]
- [Pruzan et al 2011][research_pruzan_mendenhall_2011]
- [P S Athiray et al][research_psathiray_amywinebarger]
- [P. S. Athiray et al][research_psathiray_amywinebarger_b]
- [Puening 1990][research_puening_1990]
- [Purcell et al 2025][research_purcell_wicklund_2025]
- [Purohit and Mathpal 2017][research_purohit_mathpal_2017]
- [Purser, Paul E et al 1950][research_purserpaule_thibodauxjosephg_1950]
- [Putnam, L. E. 1979][research_putnamle_1979]
- [Pyle et al 2023][research_pyle_jacobs_2023]
- [Pyle and Jacobs 2026][research_pyle_jacobs_2026]
- [Pyle and Jacobs 2026][research_pyle_jacobs_2026_b]
- [Pytanowski 1999][research_pytanowski_1999]
- [Qi et al 2022][research_qi_cheng_2022]
- [Qi and Jianliang 2017][research_qi_jianliang_2017]
- [Qi et al 2026][research_qi_meng_2026]
- [Qian et al 2013][research_qian_sun_2013]
- [Qin et al 2016][research_qin_zhang_2016]
- [Qiuhong et al 2014][research_qiuhong_zhaoying_2014]
- [Qu and Yang 2015][research_qu_yang_2015]
- [Quass, B. et al 1981][research_quassb_howardf_1981]
- [Quentmeyer, Richard J. and Roncace, Elizabeth A. 1993][research_quentmeyerrichardj_roncaceelizabetha_1993]
- [Quincy Mckown et al][research_quincymckown_markschoenenberger]
- [Quing, Xinlin et al 2011][research_quingxinlin_beardshawn_2011]
- [Quinto, P. Frank and Orie, Nettie M. 1994][research_quintopfrank_orienettiem_1994]
- [R. 1928][research_r_1928]
- [R. et al 2012][research_r_mi_2012]
- [Raab and Rohde-Brandenburger 2020][research_raab_rohdebrandenburger_2020]
- [Radhakrishnan et al 2023][research_radhakrishnan_hari_2023]
- [Rafaely et al 2007][research_rafaely_weiss_2007]
- [Rafferty 1968][research_rafferty_1968]
- [Rafi and Al-Faruk 2025][research_rafi_alfaruk_2025]
- [Ragab and Cheatwood 2015][research_ragab_cheatwood_2015]
- [Raghavan and Cesnik 2005][research_raghavan_cesnik_2005]
- [Rahaim et al 2000][research_rahaim_grage_2000]
- [Raharema et al 2026][research_raharema_sasongko_2026]
- [Rahul et al 2019][research_rahul_alokita_2019]
- [Rai et al 1999][research_rai_brunt_1999]
- [Rainee N Simons and Felix A Miranda 2003][research_raineensimons_felixamiranda_2003]
- [Raines, N. G. et al 1991][research_rainesng_bircherfe_1991]
- [Rajasegar et al 2018][research_rajasegar_choi_2018]
- [Rajendran et al 2021][research_rajendran_ramalingame_2021]
- [Rajesh et al 2012][research_rajesh_kumar_2012]
- [Raj, Sai V. and Ghosn, Louis J. 2004][research_rajsaiv_ghosnlouisj_2004]
- [Raj, Sai V. et al 2005][research_rajsaiv_robinsonraymondc_2005]
- [Rakowsky, E. L. and Marchese, V. P. 1974][research_rakowskyel_marchesevp_1974]
- [Rallabhandi and Mavris 2003][research_rallabhandi_mavris_2003]
- [Ramalingam et al 2021][research_ramalingam_thanuja_2021]
- [Raman, Ganesh et al 1991][research_ramanganesh_riceedwardj_1991]
- [R. A. Miller et al][research_ramiller_hsalpert]
- [Ranganatha][research_ranganatha]
- [Rao et al 2023][research_rao_abhinav_2023]
- [Raper, J. L. 1965][research_raperjl_1965]
- [Rappin and De Bazelaire 2000][research_rappin_debazelaire_2000]
- [Rasky et al 2006][research_rasky_pittman_2006]
- [Rasmussen et al 1967][research_rasmussen_lanzaro_1967]
- [Ratcliffe and Ratcliffe 2014][research_ratcliffe_ratcliffe_2014]
- [Ratcliffe and Ratcliffe 2014][research_ratcliffe_ratcliffe_2014_b]
- [Ratcliff, Mark L. et al 1993][research_ratcliffmarkl_athavalemaheshm_1993]
- [Ratekin, Gary 1998][research_ratekingary_1998]
- [Ratz 1960][research_ratz_1960]
- [Ravi et al 2015][research_ravi_rathod_2015]
- [Ray, Asok and Dai, Xiaowen 1995][research_rayasok_daixiaowen_1995]
- [R. C. Chapman, Jr. et al 1963][research_rcchapmanjr_gfcritchlow_1963]
- [Real time telemetry and 1975][research_real_time_1975]
- [Rébillat et al 2017][research_rebillat_hmad_2017]
- [Reed, John G. et al 2016][research_reedjohng_ragabmohamedm_2016]
- [Reeves, E. H., Jr. et al 1960][research_reevesehjr_stovalljr_1960]
- [Reeves, E. H., Jr. and Threlkeld, W. B., Jr. 1963][research_reevesehjr_threlkeldwbjr_1963]
- [Rehder, J. J. 1977][research_rehderjj_1977]
- [Rehman et al 2009][research_rehman_fidan_2009]
- [Reibman and Suthaharan 2008][research_reibman_suthaharan_2008]
- [Reichenfeld, Curtis J. and Jones, Paul G. 1999][research_reichenfeldcurtisj_jonespaulg_1999]
- [Reinel 1970][research_reinel_1970]
- [Reinersman, P. et al 1995][research_reinersmanp_carderkl_1995]
- [Reis and Sundberg 1967][research_reis_sundberg_1967]
- [Rekesh Ali et al][research_rekeshali_caroleaddona]
- [Rekesh M Ali et al][research_rekeshmali_carolejaddona]
- [Ren 2026][research_ren_2026]
- [Ren et al 2017][research_ren_he_2017]
- [Ren et al 2024][research_ren_ma_2024]
- [Ren et al 2023][research_ren_wang_2023]
- [Ren et al 2023][research_ren_yang_2023]
- [Renitha P and Sivaramapandian J 2016][research_renithap_sivaramapandianj_2016]
- [Renz, R. R. L. 1981][research_renzrrl_1981]
- [Renz, R. R. L. et al 1980][research_renzrrl_clarker_1980]
- [Research and advanced development 1967][research_research_and_1967]
- [Research, development, design, integration 1968][research_research_development_1968]
- [Research on microminiature passive 1966][research_research_on_1966]
- [Response Analysis of Landing 2026][research_response_analysis_2026]
- [Resta et al 2024][research_resta_dicicca_2024]
- [Reubush, D. E. 1973][research_reubushde_1973]
- [Reubush, D. E. and Runckel, J. F. 1973][research_reubushde_runckeljf_1973]
- [Reusable Launch Vehicle 1995][research_reusable_launch_1995]
- [Reusable Launch Vehicle Landing 2026][research_reusable_launch_2026]
- [Reusable rocket lander continues 2013][research_reusable_rocket_2013]
- [Review for "Inferring individual 2020][research_review_for_2020]
- [Rey 2000][research_rey_2000]
- [Reynolds et al 2026][research_reynolds_caillet_2026]
- [Reynolds et al 2021][research_reynolds_kokan_2021]
- [Reynolds, L. W. and Tye, F. C. 1966][research_reynoldslw_tyefc_1966]
- [Rey, R. D. and Nipper, E. J. 1978][research_reyrd_nipperej_1978]
- [Reza et al 2024][research_reza_agarwal_2024]
- [Reza and Arora 2017][research_reza_arora_2017]
- [Rhee et al 2008][research_rhee_lee_2008]
- [Rhew, Ray D. 1999][research_rhewrayd_1999]
- [Rice 1999][research_rice_1999]
- [Rice 2013][research_rice_2013]
- [Rice et al 1998][research_rice_bangsund_1998]
- [Rice, Kevin et al 2010][research_ricekevin_kizzortbrad_2010]
- [Rice, W. J. and Birchenough, A. G. 1982][research_ricewj_birchenoughag_1982]
- [Richard K. Moore et al][research_richardkmoore_johnhwall]
- [Richards, Lance et al 2014][research_richardslance_parkerallen_2014]
- [Richards, W Lance et al 2013][research_richardswlance_madaraserici_2013]
- [Richard Winski and Alejandro Pensado][research_richardwinski_alejandropensado]
- [Ricles, James M. 1991][research_riclesjamesm_1991]
- [Rieckhoff, T. J. et al 2001][research_rieckhofftj_covanma_2001]
- [Riggins et al 1998][research_riggins_nelson_1998]
- [Riggins et al 1999][research_riggins_nelson_1999]
- [Ripper et al 2009][research_ripper_dias_2009]
- [Rippere, Troy B. and Wiens, Gloria J. 2010][research_ripperetroyb_wiensgloriaj_2010]
- [Rishi 2024][research_rishi_2024]
- [R Ishikawa et al][research_rishikawa_tokamoto]
- [Rizza et al 2023][research_rizza_machado_2023]
- [Robbennolt and Munira 2026][research_robbennolt_munira_2026]
- [Robbins, H. J. and Zebrowski, Z. E. 1966][research_robbinshj_zebrowskize_1966]
- [Robert Okojie et al][research_robertokojie_christianpetrov]
- [Roberts et al 1985][research_roberts_lewis_1985]
- [Roberts et al 2007][research_roberts_stevens_2007]
- [Rochefort et al 1991][research_rochefort_oconnor_1991]
- [Rochefort and Yorra 1976][research_rochefort_yorra_1976]
- [Rocket engine propulsion 'system 1992][research_rocket_engine_1992]
- [Rocket engine seals project 1998][research_rocket_engine_1998]
- [Rocket Engine Two Hard 2000][research_rocket_engine_2000]
- [Rocket Engine One Super-Profit 2000][research_rocket_engine_2000_b]
- [Rocket Engine Nozzle Concepts 2004][research_rocket_engine_2004]
- [Rocket Engine 2005][research_rocket_engine_2005]
- [Rocket Engine Pump Feed 2009][research_rocket_engine_2009]
- [Rocket Engine Innovations Advance 2012][research_rocket_engine_2012]
- [Rocket Nozzle Performance 2019][research_rocket_nozzle_2019]
- [Rocket Propulsion Classification of 2019][research_rocket_propulsion_2019]
- [Rocket Propulsion 2022][research_rocket_propulsion_2022]
- [Rodi et al 2019][research_rodi_stoldt_2019]
- [Rodriguez et al 2006][research_rodriguez_ready_2006]
- [Rogero, S. 1969][research_rogeros_1969]
- [Rogero, S. 1972][research_rogeros_1972]
- [Rogers and Dragone 1996][research_rogers_dragone_1996]
- [Rogerson 1995][research_rogerson_1995]
- [Rogers, Rayna C. 2004][research_rogersraynac_2004]
- [Rogers, Stuart E. et al 2015][research_rogersstuarte_dallederekj_2015]
- [Rogowski, Robert S. 1990][research_rogowskiroberts_1990]
- [Rojdev, Kristina et al 2020][research_rojdevkristina_hagenjeff_2020]
- [Rollstin 1979][research_rollstin_1979]
- [Romano et al 2026][research_romano_pisano_2026]
- [Roma Rubi et al 2025][research_romarubi_kuo_2025]
- [Roncace 1991][research_roncace_1991]
- [Rooney 2003][research_rooney_2003]
- [Rooney and Wilt 1985][research_rooney_wilt_1985]
- [Roozeboom, Nettie H. et al 2020][research_roozeboomnettieh_powelljessie_2020]
- [Rosatino, S. A. and Westbrook, R. M. 1979][research_rosatinosa_westbrookrm_1979]
- [Rose 1958][research_rose_1958]
- [Roshko 1993][research_roshko_1993]
- [Roshon 1960][research_roshon_1960]
- [Ross, D. L. 1985][research_rossdl_1985]
- [Ross, D. L. 1990][research_rossdl_1990]
- [Rossi 1996][research_rossi_1996]
- [Roth, C. E. et al 1972][research_rothce_wattsll_1972]
- [Rothmund 2006][research_rothmund_2006]
- [Rothschild and Schuster 1999][research_rothschild_schuster_1999]
- [Rubin 1971][research_rubin_1971]
- [Rubin, S. et al 1988][research_rubins_searlega_1988]
- [Rubio Hervas and Reyhanoglu 2014][research_rubiohervas_reyhanoglu_2014]
- [Ruf et al 1997][research_ruf_mcconaughey_1997]
- [Ruf, J. H. et al 2003][research_rufjh_hagemanng_2003]
- [Ruf, J. H. and McDaniels, D. M. 2002][research_rufjh_mcdanielsdm_2002]
- [Ruf, Joseph H. and McDaniels, David M. 2003][research_rufjosephh_mcdanielsdavidm_2003]
- [Ruf, Joseph H. and McDaniels, David M. 2005][research_rufjosephh_mcdanielsdavidm_2005]
- [Ruixue and Zexu 2025][research_ruixue_zexu_2025]
- [Rummer, D. I. et al 1982][research_rummerdi_mosserma_1982]
- [Runkle, R. E. 1981][research_runklere_1981]
- [Rusconi et al 2026][research_rusconi_borelli_2026]
- [Rusek 1989][research_rusek_1989]
- [Rusick 2007][research_rusick_2007]
- [Russell, D. L. et al 1988][research_russelldl_blacklockk_1988]
- [Russell, Richard et al 2011][research_russellrichard_washabaughandy_2011]
- [Ruth et al 1992][research_ruth_colburn_1992]
- [Rutledge 1993][research_rutledge_1993]
- [Ryan 2000][research_ryan_2000]
- [Ryan and Verderaime 1993][research_ryan_verderaime_1993]
- [Ryan Connelly et al][research_ryanconnelly_thomassteva]
- [Ryan, H. M. et al 2000][research_ryanhm_rahmans_2000]
- [Ryohko Ishikawa et al][research_ryohkoishikawa_songdonguk]
- [Rysev and Andronov 1995][research_rysev_andronov_1995]
- [Ryu et al 2015][research_ryu_castano_2015]
- [Ryu et al 2025][research_ryu_kim_2025]
- [S. et al 2020][research_s_chauhan_2020]
- [S et al 2025][research_s_s_2025]
- [Sabatini, R. R. and Rabchevsky, G. 1970][research_sabatinirr_rabchevskyg_1970]
- [Sabia, Steve and Hand, Sarah 1988][research_sabiasteve_handsarah_1988]
- [Sabin 1955][research_sabin_1955]
- [Sabin 1956][research_sabin_1956]
- [Sabzehparvar 2005][research_sabzehparvar_2005]
- [Sachikonye 2026][research_sachikonye_2026]
- [Sachs et al 1996][research_sachs_mehlhorn_1996]
- [Saglam and Yilmaz 2018][research_saglam_yilmaz_2018]
- [Sá Gontijo et al 2025][research_sagontijo_filho_2025]
- [Sahai et al 2014][research_sahai_john_2014]
- [Sahbon et al 2023][research_sahbon_michalow_2023]
- [Sahu et al 1997][research_sahu_cooper_1997]
- [Sakagami et al 2019][research_sakagami_takeishi_2019]
- [Sakai et al 2021][research_sakai_yoshii_2021]
- [Sakala, G. G. and Raines, N. G. 1992][research_sakalagg_rainesng_1992]
- [Sakamoto et al 1999][research_sakamoto_takahashi_1999]
- [Salahudden and Ghosh 2021][research_salahudden_ghosh_2021]
- [Sale 1964][research_sale_1964]
- [Salgovic et al 2022][research_salgovic_galinski_2022]
- [Saliga, T. V. 1967][research_saligatv_1967]
- [Salikuddin, M. 1983][research_salikuddinm_1983]
- [Salinas and Ball 1973][research_salinas_ball_1973]
- [Salita, Mark 1989][research_salitamark_1989]
- [Salmi, Reino J 1956][research_salmireinoj_1956]
- [Salmi, R J and Cortright, E M, Jr 1956][research_salmirj_cortrightemjr_1956]
- [Salter, W. E. 1977][research_salterwe_1977]
- [Samanich, N. E. 1972][research_samanichne_1972]
- [Sambamurthi 1995][research_sambamurthi_1995]
- [Sanchez-Muñoz et al 2024][research_sanchezmunoz_lagarzacortes_2024]
- [Sanchini, D. J. and Kirby, F. M. 1973][research_sanchinidj_kirbyfm_1973]
- [Sander, E. J. and Leahy, J. C. 1993][research_sanderej_leahyjc_1993]
- [Sankararaman et al 2011][research_sankararaman_ling_2011]
- [Sankari Ashok Alshiya et al 2021][research_sankariashokalshiya_santhosh_2021]
- [Santi, L. Michael 2001][research_santilmichael_2001]
- [Santoro, Robert J. et al 2005][research_santororobertj_paksibtosh_2005]
- [Santoro, Robert J. and Pal, Sibtosh 1999][research_santororobertj_palsibtosh_1999]
- [Santos and Oliveira 2024][research_santos_oliveira_2024]
- [Santos, Jose A. et al 2011][research_santosjosea_oishitomo_2011]
- [Sao and Garain 2025][research_sao_garain_2025]
- [Sargsyan 2015][research_sargsyan_2015]
- [Sarigul-Klijn and Sarigul-Klijn 2003][research_sarigulklijn_sarigulklijn_2003]
- [Sarkar 2021][research_sarkar_2021]
- [Sarma et al 2016][research_sarma_sahoo_2016]
- [Sarma et al 2018][research_sarma_sahoo_2018]
- [Sarotte][research_sarotte]
- [Sarwar et al 2025][research_sarwar_nizami_2025]
- [Sarwar et al 2024][research_sarwar_rao_2024]
- [Sasoh et al 2009][research_sasoh_sekiya_2009]
- [Satheesh and Jagadeesh 2007][research_satheesh_jagadeesh_2007]
- [Satheesh and Jagadeesh 2009][research_satheesh_jagadeesh_2009]
- [Satriani et al 2025][research_satriani_abdiani_2025]
- [Sause and Jasiūnienė 2022][research_sause_jasiuniene_2022]
- [Savitha et al 2014][research_savitha_ravindra_2014]
- [Sawada et al][research_sawada_araki]
- [Sawada et al 2004][research_sawada_kunimasu_2004]
- [Sawyer and Bush 1998][research_sawyer_bush_1998]
- [Sawyer et al 1999][research_sawyer_hodge_1999]
- [Sawyer, W. C. et al 1981][research_sawyerwc_montawj_1981]
- [Sayood, Khalid and Rost, Martin C. 1989][research_sayoodkhalid_rostmartinc_1989]
- [Sazani et al 1996][research_sazani_mau_1996]
- [Sazonov 2021][research_sazonov_2021]
- [Scaffidi, C. A. et al 1971][research_scaffidica_stocklinfj_1971]
- [Scarlatella et al 2024][research_scarlatella_guadagnini_2024]
- [Scarselli and Nicassio 2025][research_scarselli_nicassio_2025]
- [Schäfer et al 1985][research_schafer_krull_1985]
- [Schalken and Chantler 2018][research_schalken_chantler_2018]
- [Scheidt, Douglas et al 2015][research_scheidtdouglas_aulterick_2015]
- [Scher and Dunavant 1966][research_scher_dunavant_1966]
- [Schierman et al 2001][research_schierman_ward_2001]
- [Schierman et al 2001][research_schierman_ward_2001_b]
- [Schiff and Sturek 1981][research_schiff_sturek_1981]
- [Schindler, Carla M. and Lansaw, John 1990][research_schindlercarlam_lansawjohn_1990]
- [Schley 1994][research_schley_1994]
- [Schmidhuber and Lopez-Delgado 2022][research_schmidhuber_lopezdelgado_2022]
- [Schmidt 1955][research_schmidt_1955]
- [Schmidt 1980][research_schmidt_1980]
- [Schmidt 1993][research_schmidt_1993]
- [Schmidt et al 1997][research_schmidt_donovan_1997]
- [Schmidt and Mann 1996][research_schmidt_mann_1996]
- [Schmitt and Burchett 2004][research_schmitt_burchett_2004]
- [Schnabel and Brophy 2018][research_schnabel_brophy_2018]
- [Schneider and Garman 1981][research_schneider_garman_1981]
- [Schneider, John R. 1992][research_schneiderjohnr_1992]
- [Schneider, W. C. and Garman, A. A. 1979][research_schneiderwc_garmanaa_1979]
- [Schoelen 1981][research_schoelen_1981]
- [Schoenekess et al 2025][research_schoenekess_volkers_2025]
- [Schoneman et al 2000][research_schoneman_buckley_2000]
- [Schorr and Speas 1995][research_schorr_speas_1995]
- [Schubert Kabban et al 2018][research_schubertkabban_uber_2018]
- [Schuelein 2008][research_schuelein_2008]
- [Schuelein 2015][research_schuelein_2015]
- [Schülein 2009][research_schulein_2009]
- [Schuler, A. E. 1967][research_schulerae_1967]
- [Schuler, A. E. 1968][research_schulerae_1968]
- [Schweikhard, Keith A. et al 2001][research_schweikhardkeitha_richardswlance_2001]
- [Schwer et al 2018][research_schwer_brophy_2018]
- [Sciacchitano and Wieneke 2016][research_sciacchitano_wieneke_2016]
- [Scott 1963][research_scott_1963]
- [Scwartz et al 2024][research_scwartz_krishnan_2024]
- [Seager and Agarwal 2017][research_seager_agarwal_2017]
- [Sea Technology Arlington Va 1998][research_seatechnologyarlingtonva_1998]
- [Seaver et al 2012][research_seaver_chattopadhyay_2012]
- [Sedillo 1990][research_sedillo_1990]
- [Sedlak, Joseph and Hashmall, Joseph 2004][research_sedlakjoseph_hashmalljoseph_2004]
- [Sedlak, Joseph et al 2003][research_sedlakjoseph_weltergary_2003]
- [Seetha A Kolli][research_seethaakolli]
- [Segal, Corin et al 1991][research_segalcorin_mcdanieljamesc_1991]
- [Seidel 1965][research_seidel_1965]
- [Seifert and Shea 1977][research_seifert_shea_1977]
- [Sekikawa and Hamada 2014][research_sekikawa_hamada_2014]
- [Sekikawa and Hamada 2015][research_sekikawa_hamada_2015]
- [Sekula, Martin K. et al 2015][research_sekulamartink_piatakdavidj_2015]
- [Selvan 2003][research_selvan_2003]
- [Semenov 1994][research_semenov_1994]
- [Semmel, Glenn S. et al 2005][research_semmelglenns_davisstevenr_2005]
- [Sen Ayush et al 2026][research_senayush_kaur_2026]
- [Senthilkumar et al 2021][research_senthilkumar_mudholkar_2021]
- [Seo and Kim 2026][research_seo_kim_2026]
- [Sepan and Lawrence 2010][research_sepan_lawrence_2010]
- [Sepcenko, Valentin et al 1990][research_sepcenkovalentin_margasahayamravi_1990]
- [Sequeira and Sanjay 2021][research_sequeira_sanjay_2021]
- [Sequence Mining of Spacecraft 2025][research_sequence_mining_of_2025]
- [Serçeoglu 2024][research_serceoglu_2024]
- [Sforzini, R. H. and Foster, W. A., Jr. 1976][research_sforzinirh_fosterwajr_1976]
- [Sha et al 2023][research_sha_wang_2023]
- [Shaffer et al 2005][research_shaffer_ross_2005]
- [Shahrokhi and Noori][research_shahrokhi_noori]
- [Shan et al 2017][research_shan_ren_2017]
- [Shang 2002][research_shang_2002]
- [Shaolin 2017][research_shaolin_2017]
- [Sharif Khodaei and Aliabadi 2023][research_sharifkhodaei_aliabadi_2023]
- [Shark et al 2010][research_shark_dennis_2010]
- [Sharma][research_sharma]
- [Shaw et al 2024][research_shaw_thakur_2024]
- [Shea, Patrick R. et al 2018][research_sheapatrickr_pinierjeremyt_2018]
- [Shelley et al 2001][research_shelley_leclaire_2001]
- [Shell, Michael T. and McElyea, Richard M. 2002][research_shellmichaelt_mcelyearichardm_2002]
- [Shelton, Joey D. et al 2005][research_sheltonjoeyd_frederickroberta_2005]
- [Shen et al 2026][research_shen_sun_2026]
- [Sheng and Hua 2011][research_sheng_hua_2011]
- [Shen, Ji Y. and Sharpe, Lonnie, Jr. 1998][research_shenjiy_sharpelonniejr_1998]
- [Shenoy et al 2020][research_shenoy_sreekumar_2020]
- [Shepperd and Staugler 1999][research_shepperd_staugler_1999]
- [Sherman, Aaron 2010][research_shermanaaron_2010]
- [Shi et al 2013][research_shi_jing_2013]
- [Shi et al 2013][research_shi_jing_2013_b]
- [Shi et al 2020][research_shi_kuschmierz_2020]
- [Shi et al 2018][research_shi_shen_2018]
- [Shibao et al 2014][research_shibao_tsuboi_2014]
- [Shi-guo et al 2011][research_shiguo_yangwang_2011]
- [Shihabi, Mazen M. et al 1994][research_shihabimazenm_nguyentienmanh_1994]
- [Shima Azimi et al 2019][research_shimaazimi_alirezabdariane_2019]
- [Shimizu et al 2008][research_shimizu_mizobuchi_2008]
- [Sholtis 2002][research_sholtis_2002]
- [Shoyama and Hirakawa 2024][research_shoyama_hirakawa_2024]
- [Shtessel et al 2000][research_shtessel_hall_2000]
- [Shtessel and Krupp][research_shtessel_krupp]
- [Shtessel and Krupp 1997][research_shtessel_krupp_1997]
- [Shtessel et al 1997][research_shtessel_tournes_1997]
- [Shtessel, Yuri B. and Hall, Charles E. 2000][research_shtesselyurib_hallcharlese_2000]
- [Shukla et al 2020][research_shukla_singh_2020]
- [Shuping Tan and Zhibin Li 2010][research_shupingtan_zhibinli_2010]
- [Shyam Raj et al 2025][research_shyamraj_parthasarathy_2025]
- [Shyy et al 2001][research_shyy_papila_2001]
- [Siddiqui and Smith 1988][research_siddiqui_smith_1988]
- [Sidorovich 1995][research_sidorovich_1995]
- [Sieder et al 2019][research_sieder_propst_2019]
- [Siewert et al 2024][research_siewert_borgzinner_2024]
- [Sihver et al 2016][research_sihver_kodaira_2016]
- [Sijtsma and Brouwer 2017][research_sijtsma_brouwer_2017]
- [Sijtsma and Brouwer 2018][research_sijtsma_brouwer_2018]
- [Silton and Bhagwandin 2012][research_silton_bhagwandin_2012]
- [Silton and Coyle 2015][research_silton_coyle_2015]
- [Silton and Coyle 2016][research_silton_coyle_2016]
- [Silton and Fresconi 2015][research_silton_fresconi_2015]
- [Silva et al 2018][research_silva_amado_2018]
- [Silva and Brójo 2024][research_silva_brojo_2024]
- [Silva-Opps and B. 2011][research_silvaopps_b_2011]
- [Silverman, J. R. 1972][research_silvermanjr_1972]
- [Simmons and Branam 2011][research_simmons_branam_2011]
- [Simmons, Charles 1994][research_simmonscharles_1994]
- [Simms, William Herbert, III et al 2014][research_simmswilliamherbertiii_varnavaskosta_2014]
- [Simon 1956][research_simon_1956]
- [Simons, Rainee N. et al 2004][research_simonsraineen_halldavidg_2004]
- [Simons, Rainee N. et al 2006][research_simonsraineen_mirandafelixa_2006]
- [Simons, Rainee N. et al 2008][research_simonsraineen_mirandafelixa_2008]
- [Simpson, R. S. and Tranter, W. H. 1968][research_simpsonrs_tranterwh_1968]
- [Simpson, Timothy W. 1998][research_simpsontimothyw_1998]
- [Sims and Hahn 1964][research_sims_hahn_1964]
- [Sims, J. D. et al 2004][research_simsjd_flandrogarya_2004]
- [Sims, Joseph D. and Coleman, Hugh W. 1998][research_simsjosephd_colemanhughw_1998]
- [Sims, William Herbert, III and Varnavas, Kosta A. 2014][research_simswilliamherbertiii_varnavaskostaa_2014]
- [Sinderson, R. L. et al 1989][research_sindersonrl_salazarga_1989]
- [Singelmann and Mueller 1948][research_singelmann_mueller_1948]
- [Singer et al 1963][research_singer_reinhardt_1963]
- [Singh et al 2024][research_singh_luyten_2024]
- [Singh, Garima et al 2016][research_singhgarima_lozijulien_2016]
- [Sippel et al 2017][research_sippel_bussler_2017]
- [Siroka et al 2021][research_siroka_foley_2021]
- [Sita, E. R. 1969][research_sitaer_1969]
- [Sithara and Shenil 2022][research_sithara_shenil_2022]
- [Siva et al 2023][research_siva_vikramasuriyan_2023]
- [Sivan and Murmu 2017][research_sivan_murmu_2017]
- [Sivan and Pandian 2018][research_sivan_pandian_2018]
- [Sixteen channel microminiature FM 1968][research_sixteen_channel_1968]
- [Skariya et al 2014][research_skariya_sebastian_2014]
- [Skinner et al 2024][research_skinner_gruber_2024]
- [Skobtsov 2024][research_skobtsov_2024]
- [Skobtsov and Novoselova 2020][research_skobtsov_novoselova_2020]
- [Slane et al 2008][research_slane_morris_2008]
- [Slater, David C. et al 1995][research_slaterdavidc_sternsalan_1995]
- [Slocumb, Travis H. and Andrews, Earl H., Jr. 1961][research_slocumbtravish_andrewsearlhjr_1961]
- [Small nuclear thermal rocket 1993][research_small_nuclear_1993]
- [Smalley, Kurt B. et al 2007][research_smalleykurtb_brownandrew_2007]
- [Smallwood 1966][research_smallwood_1966]
- [Smallwood 1967][research_smallwood_1967]
- [Smart 2015][research_smart_2015]
- [Smart Technical Textiles for 2013][research_smart_technical_2013]
- [Smeltzer, D. B. et al 1983][research_smeltzerdb_durstonda_1983]
- [Smith 1978][research_smith_1978]
- [Smith 1983][research_smith_1983]
- [Smith 2011][research_smith_2011]
- [Smith et al 1990][research_smith_adelfang_1990]
- [Smith et al 2007][research_smith_schneider_2007]
- [Smith and Scott 2001][research_smith_scott_2001]
- [Smith, Andrew and Harrison, Phil 2010][research_smithandrew_harrisonphil_2010]
- [Smith, B. P. and Dutta, S. 2017][research_smithbp_duttas_2017]
- [Smith, G. W. and Sforzini, R. H. 1972][research_smithgw_sforzinirh_1972]
- [Smith, J. D. 1966][research_smithjd_1966]
- [Smith, R. and Carr, T. 1973][research_smithr_carrt_1973]
- [Smith, S. D. 1982][research_smithsd_1982]
- [Smith, William C. et al 1992][research_smithwilliamc_leiwekerobertj_1992]
- [Snaiki and Mirfakhar 2024][research_snaiki_mirfakhar_2024]
- [Snellgrove et al 2003][research_snellgrove_griffin_2003]
- [Snider, W. J. 1974][research_sniderwj_1974]
- [Snoddy et al 2006][research_snoddy_dumbacher_2006]
- [Snowden and Levinson 2007][research_snowden_levinson_2007]
- [Sohn 2013][research_sohn_2013]
- [Soldi et al 1995][research_soldi_jr_1995]
- [Solid rocket booster performance 1974][research_solid_rocket_1974]
- [Solid Rocket Motors 2019][research_solid_rocket_2019]
- [Sommer, Simon C and Stark, James A 1952][research_sommersimonc_starkjamesa_1952]
- [Son and Sohn 2015][research_son_sohn_2015]
- [Song and Bian 2019][research_song_bian_2019]
- [Song et al 2018][research_song_cai_2018]
- [Song et al 2011][research_song_song_2011]
- [Song and Su 2015][research_song_su_2015]
- [Song et al 2020][research_song_yu_2020]
- [Song et al 2022][research_song_yu_2022]
- [Soni, Bharat 2000][research_sonibharat_2000]
- [Sophia Vedvik and Christopher D Karlgaard 2024][research_sophiavedvik_christopherdkarlgaard_2024]
- [Sorensen, Erik Mose and Ferri, Paolo 1994][research_sorensenerikmose_ferripaolo_1994]
- [Sos, J. Y. 1966][research_sosjy_1966]
- [Soumyo Dutta 2020][research_soumyodutta_2020]
- [Soumyo Dutta et al 2020][research_soumyodutta_christopherdkarlgaard_2020]
- [Sounding rocket flight of 1967][research_sounding_rocket_1967]
- [Sovey, J. S. et al 1985][research_soveyjs_penkopf_1985]
- [Sovey, J. S. et al 1985][research_soveyjs_penkopf_1985_b]
- [Sovey, J. S. et al 1986][research_soveyjs_penkopf_1986]
- [Space data and information][research_space_data]
- [Space data and information][research_space_data_b]
- [Space data and information][research_space_data_c]
- [Space data and information][research_space_data_d]
- [Space data and information][research_space_data_e]
- [Space engineering. Space data][research_space_engineering]
- [Space engineering. Space data][research_space_engineering_b]
- [Space shuttle program. Expendable 1971][research_space_shuttle_1971]
- [Space shuttle solid rocket 1973][research_space_shuttle_1973]
- [Space shuttle solid rocket 1973][research_space_shuttle_1973_b]
- [Space shuttle solid rocket 1973][research_space_shuttle_1973_c]
- [Space systems � Measured][research_space_systems]
- [Space systems. Launch-vehicle-to-spacecraft flight][research_space_systems_b]
- [Space Telemetry for the 1983][research_space_telemetry_1983]
- [Space vehicle sa-6 telemetry 1965][research_space_vehicle_1965]
- [Spacecraft telemetry and command 1968][research_spacecraft_telemetry_1968]
- [Spaceport America attracts reusable 2011][research_spaceport_america_2011]
- [SpaceX gets a rival 2013][research_spacex_gets_2013]
- [SpaceX tests legs that 2014][research_spacex_tests_2014]
- [SpaceX to cut launch 2011][research_spacex_to_2011]
- [SpaceX to test rocket 2014][research_spacex_to_2014]
- [Spahn, C. J. and Pena, C. D. 1982][research_spahncj_penacd_1982]
- [Spahr, J Richard and Dickey, Robert R 1951][research_spahrjrichard_dickeyrobertr_1951]
- [Specht, Ted and Noble, David 2006][research_spechtted_nobledavid_2006]
- [Speer, Dave 2003][research_speerdave_2003]
- [Spencer][research_spencer]
- [Spencer 1999][research_spencer_1999]
- [Spencer, B., Jr. and Fournier, R. H. 1973][research_spencerbjr_fournierrh_1973]
- [Spherical rocket motor static-test 1962][research_spherical_rocket_1962]
- [Spieth 1965][research_spieth_1965]
- [Spradley, L. W. 1975][research_spradleylw_1975]
- [Sprattling, Jr. 1967][research_sprattlingjr_1967]
- [Springer 1996][research_springer_1996]
- [Springett 1965][research_springett_1965]
- [Spurlock and Williams 2014][research_spurlock_williams_2014]
- [Spurný et al 2008][research_spurny_ploc_2008]
- [Sriganapathy et al 2022][research_sriganapathy_arjunkumara_2022]
- [Sriharsha Madhavan et al 2021][research_sriharshamadhavan_junqiangsun_2021]
- [Srijayantha, M. 1983][research_srijayantham_1983]
- [Srinath and Reddy 2010][research_srinath_reddy_2010]
- [Srinivasan, Jefferey M. and Lichten, Stephen M. 1994][research_srinivasanjeffereym_lichtenstephenm_1994]
- [Srivastava and Thakur 2022][research_srivastava_thakur_2022]
- [Stack 2022][research_stack_2022]
- [Stackpoole, M. et al 2013][research_stackpoolem_kaod_2013]
- [Stadler 1998][research_stadler_1998]
- [Stahl, H. Philip et al 2016][research_stahlhphilip_hopkinsrandallc_2016]
- [Staid, P. S. 1978][research_staidps_1978]
- [Stanboli, Alice 2013][research_stanbolialice_2013]
- [Stanboli, Alice et al 2013][research_stanbolialice_martinezelmainm_2013]
- [Stancil 1963][research_stancil_1963]
- [Stancil 1964][research_stancil_1964]
- [Staniszewski 1999][research_staniszewski_1999]
- [Staniszewski 2001][research_staniszewski_2001]
- [Stanley et al 1992][research_stanley_engelund_1992]
- [Stansbury et al 2013][research_stansbury_towhidnejead_2013]
- [Starkey 2015][research_starkey_2015]
- [Starkey et al 2014][research_starkey_cannella_2014]
- [Stark, K. W. 1972][research_starkkw_1972]
- [Starner, D. L. 1969][research_starnerdl_1969]
- [Starner, D. L. 1969][research_starnerdl_1969_b]
- [Starnone and Biesbroek 2006][research_starnone_biesbroek_2006]
- [Staszewski and Sohn 2010][research_staszewski_sohn_2010]
- [Statham, Tamara and Thompson, Seth 2017][research_stathamtamara_thompsonseth_2017]
- [Statham, T. L. et al 2019][research_stathamtl_steinwb_2019]
- [Staudinger et al][research_staudinger_hershey]
- [Stechman et al 2000][research_stechman_woll_2000]
- [Steele, W. G. et al 2005][research_steelewg_molderkj_2005]
- [Stefanski, Philip L. 2015][research_stefanskiphilipl_2015]
- [Steffen, F. W. 1970][research_steffenfw_1970]
- [Steiner and Bauer 2026][research_steiner_bauer_2026]
- [Stein, M. 1967][research_steinm_1967]
- [Steinmeyer et al 1990][research_steinmeyer_howard_1990]
- [Stenarson and Yhland 2009][research_stenarson_yhland_2009]
- [Stephen et al][research_stephen_rajanna]
- [Stephen A 2020][research_stephena_2020]
- [Stephen Corda et al 1998][research_stephencorda_bradfordaneal_1998]
- [Stephens, Julia et al 2015][research_stephensjulia_hubbarderin_2015]
- [Stephens, Julia et al 2016][research_stephensjulia_hubbarderin_2016]
- [Stephens, Julia E. et al 2016][research_stephensjuliae_hubbarderinp_2016]
- [Stephison, D. B. 1981][research_stephisondb_1981]
- [Stermer, R. L., Jr. 1978][research_stermerrljr_1978]
- [Stern, Alan S. 1996][research_sternalans_1996]
- [Steve Hahn et al][research_stevehahn_nathanlunetta]
- [Steven E Krist et al 2019][research_stevenekrist_nalinaratnayake_2019]
- [Stevens, G. L. 1980][research_stevensgl_1980]
- [Stevens, R. 1984][research_stevensr_1984]
- [Stewart][research_stewart]
- [Stewart et al 2020][research_stewart_papadopoulos_2020]
- [Stewart et al 2005][research_stewart_tang_2005]
- [Stewart, Christine E. 2013][research_stewartchristinee_2013]
- [Stewart, Eric et al 1996][research_stewarteric_mcconnaugheyp_1996]
- [Stillwater, Ryan A. 2009][research_stillwaterryana_2009]
- [Stine 1964][research_stine_1964]
- [Stoica et al 2026][research_stoica_dimarco_2026]
- [Stokes and Lombaerts 2023][research_stokes_lombaerts_2023]
- [Stokes, J. H. and Ward, S. M. 1985][research_stokesjh_wardsm_1985]
- [Stoneking et al 2010][research_stoneking_shah_2010]
- [Stoneking, Eric T. and Tsai, Dean 2009][research_stonekingerict_tsaidean_2009]
- [Storey 2023][research_storey_2023]
- [Stouffer 1979][research_stouffer_1979]
- [Straight, D. M. and Harrington, D. E. 1973][research_straightdm_harringtonde_1973]
- [Strain gauge installation in 1971][research_strain_gauge_1971]
- [Strauss 1964][research_strauss_1964]
- [Street 1970][research_street_1970]
- [Streich, Ronald C. et al 2001][research_streichronaldc_morgandwayner_2001]
- [Striepe, Scott A. et al 2007][research_striepescotta_blanchardrobertc_2007]
- [Strobel and Macneil 2024][research_strobel_macneil_2024]
- [Strome 1969][research_strome_1969]
- [Structural Health Monitoring Considerations][research_structural_health]
- [Structural Health Monitoring Person 2008][research_structural_health_2008]
- [Structural Health Monitoring OrientedModelling 2011][research_structural_health_2011]
- [Structural Health Monitoring of 2016][research_structural_health_2016]
- [Structural Health Monitoring SHM 2016][research_structural_health_2016_b]
- [Structural health monitoring SHM 2019][research_structural_health_2019]
- [Structural Health Monitoring Damage 2021][research_structural_health_2021]
- [Structural health monitoring SHM 2023][research_structural_health_2023]
- [Structural Health Monitoring/management SHM 2024][research_structural_health_2024]
- [Structural health monitoring SHM 2025][research_structural_health_2025]
- [Structural Health Monitoring 2025][research_structural_health_2025_b]
- [Study of solid rocket 1972][research_study_of_1972]
- [Study of solid rocket 1972][research_study_of_1972_b]
- [Study of solid rocket 1972][research_study_of_1972_c]
- [Study of solid rocket 1972][research_study_of_1972_d]
- [Study of solid rocket 1972][research_study_of_1972_e]
- [Study of solid rocket 1972][research_study_of_1972_f]
- [Study of solid rocket 1972][research_study_of_1972_g]
- [Study of solid rocket 1972][research_study_of_1972_h]
- [Sturdevant et al 2006][research_sturdevant_wright_2006]
- [Su et al 2021][research_su_dai_2021]
- [Su et al 2021][research_su_dai_2021_b]
- [Su and Liu 2025][research_su_liu_2025]
- [Su and Liu 2025][research_su_liu_2025_b]
- [Su and Wang 2015][research_su_wang_2015]
- [Success for SpaceX reusable 2017][research_success_for_2017]
- [Sudiana 2020][research_sudiana_2020]
- [Sue, M. K. 1981][research_suemk_1981]
- [Sue, M. K. 1982][research_suemk_1982]
- [Suit et al 1964][research_suit_kiker_1964]
- [Sukachevskyi 2026][research_sukachevskyi_2026]
- [Sule, W. P. and Mueller, T. J. 1973][research_sulewp_muellertj_1973]
- [Summerer et al 2006][research_summerer_putz_2006]
- [Summerfield 1960][research_summerfield_1960]
- [Sun][research_sun]
- [Sun and Khalid 1998][research_sun_khalid_1998]
- [Sun et al 2025][research_sun_mahmoodian_2025]
- [Sun et al 2026][research_sun_sun_2026]
- [Sundaria et al 2023][research_sundaria_bhagat_2023]
- [Sundaria et al 2023][research_sundaria_bhagat_2023_b]
- [Sung and Park 1960][research_sung_park_1960]
- [Suresh et al 2009][research_suresh_rong_2009]
- [Surko, Pamela 1994][research_surkopamela_1994]
- [Suroso et al 2019][research_suroso_gautam_2019]
- [Suzuki et al 2006][research_suzuki_nonaka_2006]
- [Suzuki et al 2007][research_suzuki_nonaka_2007]
- [Swanson, Gregory T. et al 2012][research_swansongregoryt_empeydanielm_2012]
- [Swanson, G. T. et al 2019][research_swansongt_millerra_2019]
- [Swathish and Rakesh 2024][research_swathish_rakesh_2024]
- [Swindell 2015][research_swindell_2015]
- [Swiss Students Achieve Europe's 2025][research_swiss_students_2025]
- [Szalkowski et al 2024][research_szalkowski_chrostowski_2024]
- [Szmuk and Acikmese 2018][research_szmuk_acikmese_2018]
- [T and Cm 2017][research_t_cm_2017]
- [Tabakov and Zinina 2020][research_tabakov_zinina_2020]
- [Tabakov et al 2020][research_tabakov_zinina_2020_b]
- [Takacs 2013][research_takacs_2013]
- [Takagi et al 2014][research_takagi_morozumi_2014]
- [Takahashi 2016][research_takahashi_2016]
- [Takahashi et al 1997][research_takahashi_mizobata_1997]
- [Takahashi et al 2015][research_takahashi_tomita_2015]
- [Taki et al 2026][research_taki_sergienko_2026]
- [Talley 2002][research_talley_2002]
- [Tamami 2020][research_tamami_2020]
- [Tan 2017][research_tan_2017]
- [Tanck and Steadman 1998][research_tanck_steadman_1998]
- [Tang, M. H. 1971][research_tangmh_1971]
- [Tang, M. H. and Pearson, G. P. E. 1971][research_tangmh_pearsongpe_1971]
- [Tang, M. H. et al 1978][research_tangmh_seficwj_1978]
- [Taniguchi et al 2006][research_taniguchi_mori_2006]
- [Tannen S Vanzwieten et al 2017][research_tannensvanzwieten_michaelrhannan_2017]
- [Tanner 1972][research_tanner_1972]
- [Tarapčík et al 2001][research_tarapcik_labuda_2001]
- [Tarifa and Pizzuti 2019][research_tarifa_pizzuti_2019]
- [Tarrant and Crook][research_tarrant_crook]
- [Tarrant and Crook 1996][research_tarrant_crook_1996]
- [Tarrant, Charlie and Crook, Jerry 1997][research_tarrantcharlie_crookjerry_1997]
- [Tartabini, Paul V. 2007][research_tartabinipaulv_2007]
- [Tartabini, Paul V. et al 2015][research_tartabinipaulv_beatyjamesr_2015]
- [Task four report Telemetry 1973][research_task_four_1973]
- [Tatry et al 1997][research_tatry_deneu_1997]
- [Taylor 2012][research_taylor_2012]
- [Taylor 2012][research_taylor_2012_b]
- [Taylor 2013][research_taylor_2013]
- [Taylor et al 1973][research_taylor_simmons_1973]
- [Tcheng, Ping et al 1988][research_tchengping_schotttimothyd_1988]
- [Technical report analysis and 1972][research_technical_report_1972]
- [Techniques for rocket engine 1965][research_techniques_for_1965]
- [Tedrick, R. N. 1964][research_tedrickrn_1964]
- [Tejwani, Gopal D. et al 2003][research_tejwanigopald_langfordlestera_2003]
- [Tekure et al 2021][research_tekure_pophali_2021]
- [Telemetry Boards Interpret Rocket 2009][research_telemetry_boards_2009]
- [Telemetry modulation system MSC-TS-8A 1968][research_telemetry_modulation_1968]
- [Telemetry Systems 1996][research_telemetry_systems_1996]
- [Telemetry Technology 1997][research_telemetry_technology_1997]
- [Tellier 1964][research_tellier_1964]
- [Teng 1970][research_teng_1970]
- [Terhune et al 2011][research_terhune_hollis_2011]
- [Tetervin 1963][research_tetervin_1963]
- [Tetlow et al 2000][research_tetlow_schoettle_2000]
- [Tewell 1984][research_tewell_1984]
- [Tharratt, C. E. 1975][research_tharrattce_1975]
- [The design and performance 1964][research_the_design_1964]
- [The Invention Relates to 2021][research_the_invention_2021]
- [The Measurement Uncertainty Model 2026][research_the_measurement_2026]
- [The Person of the 2014][research_the_person_2014]
- [The Structural Health Monitoring 2004][research_the_structural_2004]
- [The Structural Health Monitoring 2005][research_the_structural_2005]
- [The thermal rocket engine][research_the_thermal]
- [Theerthamalai et al 2005][research_theerthamalai_manisekaran_2005]
- [Thiele et al 2018][research_thiele_gulhan_2018]
- [Thies 2022][research_thies_2022]
- [Thin-film personal communications and 1965][research_thin_film_personal_1965]
- [Thin-Film Personal Communications and 1966][research_thin_film_personal_1966]
- [Thin-Film Personal Communications and 1966][research_thin_film_personal_1966_b]
- [Thin-Film Personal Communications and 1967][research_thin_film_personal_1967]
- [Thin-film Personal Communications and 1967][research_thin_film_personal_1967_b]
- [Thin-Film Personal Communications and 1968][research_thin_film_personal_1968]
- [Thomas 1942][research_thomas_1942]
- [Thomas, Mitchel E. and Diamond, John K. 1987][research_thomasmitchele_diamondjohnk_1987]
- [Thomas, Roger J. et al 2001][research_thomasrogerj_kankelborgcharlesc_2001]
- [Thomas, Scott R. et al 2001][research_thomasscottr_palacdonaldt_2001]
- [Thomas, Taylor Walter 2019][research_thomastaylorwalter_2019]
- [Thomas Teasley et al][research_thomasteasley_dillonpetty]
- [Thomas Teasley et al][research_thomasteasley_dillonpetty_b]
- [Thompson 2024][research_thompson_2024]
- [Thompson et al 1987][research_thompson_russell_1987]
- [Thompson, Jim Rogers 1950][research_thompsonjimrogers_1950]
- [Thompson, Jim Rogers and Kurbjun, Max C 1948][research_thompsonjimrogers_kurbjunmaxc_1948]
- [Thompson, Jim Rogers and Mathews, Charles W 1947][research_thompsonjimrogers_mathewscharlesw_1947]
- [Thomson et al 1991][research_thomson_ebbeson_1991]
- [Thornburg 2002][research_thornburg_2002]
- [Thorn, Karen E. 1993][research_thornkarene_1993]
- [Threet, Grady E. et al 2012][research_threetgradye_watersericd_2012]
- [Tiachacht et al 2023][research_tiachacht_kahouadji_2023]
- [Tian et al 2020][research_tian_guo_2020]
- [Tian et al 2024][research_tian_wang_2024]
- [Tierney 1993][research_tierney_1993]
- [Tieshan et al 2016][research_tieshan_daquan_2016]
- [Time-Dependent In-Flight Thrust Determination][research_time_dependent_in_flight]
- [Timofeev 2020][research_timofeev_2020]
- [Timothy, J. G. 1973][research_timothyjg_1973]
- [Titsworth, R. C. 1963][research_titsworthrc_1963]
- [Tiwari et al 2005][research_tiwari_kalluru_2005]
- [T J Wignall][research_tjwignall]
- [T.J. Wignall et al][research_tjwignall_jessegcollins]
- [T J Wignall et al][research_tjwignall_morganawalker]
- [Tkachenko et al 2017][research_tkachenko_salmin_2017]
- [Tkalenko 1969][research_tkalenko_1969]
- [Tobey and Bastress 1966][research_tobey_bastress_1966]
- [Toelle, R. G. et al 1973][research_toellerg_blackwelldl_1973]
- [Tolić et al 2019][research_tolic_primorac_2019]
- [Tolmadzheva, T. A. et al 1974][research_tolmadzhevata_kantorav_1974]
- [Tomita et al 2008][research_tomita_moriya_2008]
- [Tomita et al 1999][research_tomita_takahashi_1999]
- [Tomita et al 2001][research_tomita_takahashi_2001]
- [Tom Young][research_tomyoung]
- [Tong et al 2025][research_tong_shi_2025]
- [Tooth 1975][research_tooth_1975]
- [Torres et al 2008][research_torres_olea_2008]
- [Tortora et al 2022][research_tortora_cordelli_2022]
- [Toson et al 2026][research_toson_porcarelli_2026]
- [Toten et al 1991][research_toten_fong_1991]
- [Tournes and Johnson 1998][research_tournes_johnson_1998]
- [Towler and Ryu 2017][research_towler_ryu_2017]
- [Trajectory Shaping Guidance for 2025][research_trajectory_shaping_2025]
- [Tran, Ken et al 1992][research_tranken_chandanielc_1992]
- [Transducer calibration 1980][research_transducer_calibration_1980]
- [Transducer calibration tool 1983][research_transducer_calibration_1983]
- [Tranter, W. H. 1969][research_tranterwh_1969]
- [Traudt 2024][research_traudt_2024]
- [Trefny, Charles J. 2003][research_trefnycharlesj_2003]
- [Trends on research in 2014][research_trends_on_2014]
- [Trescot, C. D., Jr. et al 1973][research_trescotcdjr_fostergv_1973]
- [Trevino, Luis C. 1994][research_trevinoluisc_1994]
- [Trigg, H. W. 1966][research_trigghw_1966]
- [Trimmer 1968][research_trimmer_1968]
- [Trinh, Huu P. et al 2002][research_trinhhuup_bullardbrad_2002]
- [Tripathi et al 2018][research_tripathi_misra_2018]
- [Tripathi et al 2019][research_tripathi_sucheendran_2019]
- [Tripathi et al 2019][research_tripathi_sucheendran_2019_b]
- [Tripathi et al 2025][research_tripathi_sucheendran_2025]
- [Tripp, John S. and Tcheng, Ping 1999][research_trippjohns_tchengping_1999]
- [Tripp, John S. and Tcheng, Ping 1999][research_trippjohns_tchengping_1999_b]
- [Tripropellant Engine Technology for 2004][research_tripropellant_engine_2004]
- [Trott 1961][research_trott_1961]
- [Trott 1962][research_trott_1962]
- [Trumpour 2021][research_trumpour_2021]
- [Tsai 1995][research_tsai_1995]
- [Tsou, H. et al 1993][research_tsouh_shahb_1993]
- [Tsou, Haiping et al 1995][research_tsouhaiping_hinedisamim_1995]
- [Tsuboi et al 2018][research_tsuboi_jourdaine_2018]
- [Tsuboi et al 2011][research_tsuboi_kawakami_2011]
- [Tsukada et al 2005][research_tsukada_fujimoto_2005]
- [Tsutsumi et al 2005][research_tsutsumi_teramoto_2005]
- [Tsutsumi et al 2007][research_tsutsumi_yamaguchi_2007]
- [Tucker, P. K. and Warsi, S. A. 1993][research_tuckerpk_warsisa_1993]
- [Tudor et al 2021][research_tudor_wang_2021]
- [Tulpule 1989][research_tulpule_1989]
- [Tuohy 1998][research_tuohy_1998]
- [Turmon, Michael and Braverman, Amy 2019][research_turmonmichael_bravermanamy_2019]
- [Turpie, Kevin R. et al 2014][research_turpiekevinr_epleerobertejr_2014]
- [Tutmez 2016][research_tutmez_2016]
- [Tuttle, S. L. et al 1995][research_tuttlesl_meedj_1995]
- [Tynis et al 2019][research_tynis_karlgaard_2019]
- [Udaiyakumar et al 2020][research_udaiyakumar_iyer_2020]
- [Udd 2006][research_udd_2006]
- [Udwadia, F. E. and Garba, J. 1985][research_udwadiafe_garbaj_1985]
- [Umadevi et al 2017][research_umadevi_navas_2017]
- [Umholtz 1999][research_umholtz_1999]
- [Uncertainty Estimation, Propagation, and 2016][research_uncertainty_estimation_2016]
- [Uncertainty of In-Flight Thrust][research_uncertainty_of]
- [Uncertainty Propagation for Systems 2006][research_uncertainty_propagation_2006]
- [Uncertainty Propagation Methods 2008][research_uncertainty_propagation_2008]
- [Underwood et al 2008][research_underwood_swenson_2008]
- [Underwood, T. C., Jr. 1970][research_underwoodtcjr_1970]
- [United Launch Alliance announces 2015][research_united_launch_2015]
- [Urban 1959][research_urban_1959]
- [Urban 1963][research_urban_1963]
- [Urech, J. M. et al 1986][research_urechjm_chamarroa_1986]
- [Urschel and Cox 2003][research_urschel_cox_2003]
- [Usandizaga et al 2020][research_usandizaga_beard_2020]
- [Useller, James W and Pappas, George E 1956][research_usellerjamesw_pappasgeorgee_1956]
- [Usmonov and Kretov 2020][research_usmonov_kretov_2020]
- [Usry, J. W. and Wallace, J. W. 1971][research_usryjw_wallacejw_1971]
- [Vacuum transducer calibration 1966][research_vacuum_transducer_1966]
- [Vaglio-Laurin and Finke 1965][research_vagliolaurin_finke_1965]
- [Vaidyanathan, Rajkumar et al 2000][research_vaidyanathanrajkumar_papitanilay_2000]
- [Valdes 1992][research_valdes_1992]
- [VanZwieten, Tannen S. et al 2015][research_vanzwietentannens_gilliganerict_2015]
- [Vargas, Magda B. and Kenny, R. Jeremy 2010][research_vargasmagdab_kennyrjeremy_2010]
- [Varnavas, Kosta A. and Sims, William Herbert, III 2013][research_varnavaskostaa_simswilliamherbertiii_2013]
- [Varnavas, Kosta A. and Sims, William Herbert, III 2014][research_varnavaskostaa_simswilliamherbertiii_2014]
- [Vasil'chenko 1981][research_vasilchenko_1981]
- [Vasil'ev 1966][research_vasilev_1966]
- [Vasilevskyi and Cullinan 2026][research_vasilevskyi_cullinan_2026]
- [Vasudevan et al 2017][research_vasudevan_das_2017]
- [Vathsal][research_vathsal]
- [Vaughn et al 2007][research_vaughn_singh_2007]
- [Vdoviak, J. W. et al 1981][research_vdoviakjw_knottpr_1981]
- [V E Horn 1967][research_vehorn_1967]
- [Veidt and Liew 2013][research_veidt_liew_2013]
- [Velde et al 1969][research_velde_bentley_1969]
- [Veldman 2023][research_veldman_2023]
- [Velez-Justiniano, Yo-Ann et al 2019][research_velezjustinianoyoann_stefanskiphilipl_2019]
- [Velliaris 2021][research_velliaris_2021]
- [Ventura and WErnimont 2001][research_ventura_wernimont_2001]
- [Venukumar et al 2006][research_venukumar_jagadeesh_2006]
- [Vergallo et al 2013][research_vergallo_layekuakille_2013]
- [Verma 2008][research_verma_2008]
- [Verma 2009][research_verma_2009]
- [Vetter 1977][research_vetter_1977]
- [Vibbart 1988][research_vibbart_1988]
- [Vidya et al 2013][research_vidya_vivekananad_2013]
- [Vijayan and Suresh Babu 2015][research_vijayan_sureshbabu_2015]
- [Vincent et al 2025][research_vincent_pereira_2025]
- [Vinson, John 1998][research_vinsonjohn_1998]
- [Viscardi et al 2025][research_viscardi_monaco_2025]
- [Vishnyak 1995][research_vishnyak_1995]
- [Visscher, J. 1969][research_visscherj_1969]
- [Viterbi, Andrew 1961][research_viterbiandrew_1961]
- [Viúdez 2018][research_viudez_2018]
- [Viventi 1961][research_viventi_1961]
- [Vogel et al 2009][research_vogel_kelkar_2009]
- [Voinov and Mel'nikov 1996][research_voinov_melnikov_1996]
- [Volkov et al 2019][research_volkov_kolokutin_2019]
- [Vonderesch, A. H. 1972][research_vondereschah_1972]
- [Vorontsov and Samoilov 2012][research_vorontsov_samoilov_2012]
- [Vorozhtsov and Matvienko 2002][research_vorozhtsov_matvienko_2002]
- [Vozhdaev and Teperin 2020][research_vozhdaev_teperin_2020]
- [Vrolyk, John J. 1977][research_vrolykjohnj_1977]
- [Wadia and Wilson 1981][research_wadia_wilson_1981]
- [Wagner, Sean 2014][research_wagnersean_2014]
- [Wagner, W. R. and Waldman, B. J. 1973][research_wagnerwr_waldmanbj_1973]
- [Waldersen, Matt and Schnarr, Otto, III 2017][research_waldersenmatt_schnarrottoiii_2017]
- [Wallace et al 2003][research_wallace_olds_2003]
- [Wall, John H. et al 2014][research_walljohnh_orrjebs_2014]
- [Wall, John H. et al 2015][research_walljohnh_vanzwietentannens_2015]
- [Walt C Long 1964][research_waltclong_1964]
- [Walter and Shaw 1979][research_walter_shaw_1979]
- [Wan and Ni 2019][research_wan_ni_2019]
- [Wan et al 2013][research_wan_shu_2013]
- [Wan et al 2012][research_wan_wang_2012]
- [Wang 1998][research_wang_1998]
- [Wang 2004][research_wang_2004]
- [Wang 2015][research_wang_2015]
- [Wang et al 2021][research_wang_an_2021]
- [Wang et al 2022][research_wang_an_2022]
- [Wang et al 2025][research_wang_cao_2025]
- [Wang et al 2020][research_wang_chen_2020]
- [Wang et al 2026][research_wang_dai_2026]
- [Wang et al 2005][research_wang_ding_2005]
- [Wang et al 2015][research_wang_fan_2015]
- [Wang et al 2023][research_wang_fang_2023]
- [Wang et al 2025][research_wang_gan_2025]
- [Wang and Hsu 2023][research_wang_hsu_2023]
- [Wang et al 2023][research_wang_li_2023]
- [Wang et al 2025][research_wang_lian_2025]
- [Wang et al 2024][research_wang_liang_2024]
- [Wang et al 2006][research_wang_liu_2006]
- [Wang et al 2009][research_wang_liu_2009]
- [Wang et al 2012][research_wang_liu_2012]
- [Wang and Miao 2026][research_wang_miao_2026]
- [Wang et al 2025][research_wang_niu_2025]
- [Wang et al 2026][research_wang_pei_2026]
- [Wang et al 2007][research_wang_qin_2007]
- [Wang et al 2024][research_wang_ren_2024]
- [Wang and Song 2018][research_wang_song_2018]
- [Wang and Song 2018][research_wang_song_2018_b]
- [Wang and Song 2019][research_wang_song_2019]
- [Wang et al 2021][research_wang_song_2021]
- [Wang et al 2026][research_wang_song_2026]
- [Wang and Wang 2011][research_wang_wang_2011]
- [Wang et al 2019][research_wang_wang_2019]
- [Wang et al 2024][research_wang_wang_2024]
- [Wang et al 2022][research_wang_wei_2022]
- [Wang et al 2021][research_wang_wu_2021]
- [Wang et al 2024][research_wang_xu_2024]
- [Wang et al 2026][research_wang_xu_2026]
- [Wang et al 2021][research_wang_yang_2021]
- [Wang et al 2024][research_wang_yao_2024]
- [Wang et al 2019][research_wang_zhang_2019]
- [Wang et al 2026][research_wang_zhang_2026]
- [Wang et al 2024][research_wang_zhou_2024]
- [Wang, C. C. 1965][research_wangcc_1965]
- [Wang, Tee-See et al 2003][research_wangteesee_droegealan_2003]
- [Wang, Ten-See 1998][research_wangtensee_1998]
- [Wang, Ten-See 1998][research_wangtensee_1998_b]
- [Wang, Ten-See and Chen, Yen-Sen 1990][research_wangtensee_chenyensen_1990]
- [Wang, Ten-See et al 2003][research_wangtensee_droegealan_2003]
- [Wang, Ten-See et al 2004][research_wangtensee_droegealan_2004]
- [Wang, Ten-See et al 2001][research_wangtensee_williamsrobert_2001]
- [Wang, T.-S. 1990][research_wangts_1990]
- [Wangu and Mouyos 1998][research_wangu_mouyos_1998]
- [Ward, Jr. 1970][research_wardjr_1970]
- [Ward, P. R. 1986][research_wardpr_1986]
- [Washburn 2004][research_washburn_2004]
- [Washington et al 1993][research_washington_booth_1993]
- [Washington et al 1968][research_washington_pettis_1968]
- [Watanabe and Mikami 2010][research_watanabe_mikami_2010]
- [Waters, Eric D. et al 2013][research_watersericd_beersbenjamin_2013]
- [Watson et al 2014][research_watson_neeley_2014]
- [Watters 1973][research_watters_1973]
- [Watters, D. M. 1986][research_wattersdm_1986]
- [Way, David W. and Brugarolas, Paul 2021][research_waydavidw_brugarolaspaul_2021]
- [Weathers, G. 1975][research_weathersg_1975]
- [Webb et al 2014][research_webb_williams_2014]
- [Weber, Romann et al 2017][research_weberromann_yueyisong_2017]
- [Wechsler, E. R. 1981][research_wechslerer_1981]
- [Wehrmeyer, Joseph et al 2000][research_wehrmeyerjoseph_hartfieldroyjjr_2000]
- [Wehrmeyer, Joseph A. et al 2001][research_wehrmeyerjosepha_osbornerobinj_2001]
- [Wei and Chen 2015][research_wei_chen_2015]
- [Wei and Shao 2021][research_wei_shao_2021]
- [Weidner, Thomas J. et al 2002][research_weidnerthomasj_larsendavidv_2002]
- [Wei Jiang et al 2006][research_weijiang_yixinyang_2006]
- [Weinacht et al 1984][research_weinacht_guidos_1984]
- [Weiner, B. J. 1965][research_weinerbj_1965]
- [Weiner, B. J. 1965][research_weinerbj_1965_b]
- [Wejrzanowski et al 2021][research_wejrzanowski_tymicki_2021]
- [Well 1989][research_well_1989]
- [Weller 1982][research_weller_1982]
- [Wells, G. and Baroth, E. 1994][research_wellsg_barothe_1994]
- [Wells, George and Baroth, Edmund C. 1993][research_wellsgeorge_barothedmundc_1993]
- [Welsh 1985][research_welsh_1985]
- [Welsh, Clement J and Demoraes, Carlos A 1951][research_welshclementj_demoraescarlosa_1951]
- [Wentz, Frank J. and Lawrence, Richard J. 2003][research_wentzfrankj_lawrencerichardj_2003]
- [Wenzel, Sean et al 2021][research_wenzelsean_huangcalvin_2021]
- [Wercinski, Paul et al 2017][research_wercinskipaul_smithb_2017]
- [Wernet, Mark P. and Stiegemeier, Benjamin R. 2017][research_wernetmarkp_stiegemeierbenjaminr_2017]
- [Wessling, Francis C. and Maybee, George W. 1989][research_wesslingfrancisc_maybeegeorgew_1989]
- [Westra, Douglas G. and West, Jeffrey S. 2014][research_westradouglasg_westjeffreys_2014]
- [Wetzel][research_wetzel]
- [White 1957][research_white_1957]
- [White and Saunders 2007][research_white_saunders_2007]
- [White, H. D., Jr. 1964][research_whitehdjr_1964]
- [Whitehead 2000][research_whitehead_2000]
- [Whitelaw, Virginia A. 1987][research_whitelawvirginiaa_1987]
- [Whiteman, Donald E. et al 2005][research_whitemandonalde_valencialisam_2005]
- [Whiteman, Donald E. et al 2005][research_whitemandonalde_valencialisam_2005_b]
- [Whitlow et al 2010][research_whitlow_sundaresan_2010]
- [Whitmore et al 2001][research_whitmore_sprague_2001]
- [Whitmore, Stephen A. and Leondes, Cornelius T. 1991][research_whitmorestephena_leondescorneliust_1991]
- [Whitmore, Stephen A. and Moes, Timothy R. 1994][research_whitmorestephena_moestimothyr_1994]
- [Whitmore, Stephen A. and Moes, Timothy R. 1999][research_whitmorestephena_moestimothyr_1999]
- [Whyte et al 1985][research_whyte_hathaway_1985]
- [Wiegmann et al 2009][research_wiegmann_schulz_2009]
- [Wiesenberg 2000][research_wiesenberg_2000]
- [Wike, Jeffrey and Griffith, Paul 1989][research_wikejeffrey_griffithpaul_1989]
- [Wilcher, J. H. 1976][research_wilcherjh_1976]
- [Wilder, Michael C. et al 2015][research_wildermichaelc_redadanielc_2015]
- [Wiley, John et al 2008][research_wileyjohn_kormanvalentin_2008]
- [Wilks 2006][research_wilks_2006]
- [Williams 1965][research_williams_1965]
- [Williams 1968][research_williams_1968]
- [Williams 1986][research_williams_1986]
- [Williams 2004][research_williams_2004]
- [Williams, Glenn L. 2000][research_williamsglennl_2000]
- [Williams, Martha et al 2013][research_williamsmartha_lewismark_2013]
- [Williams, M. Susan 1989][research_williamsmsusan_1989]
- [Williamson 2016][research_williamson_2016]
- [Williams, R. Anthony and Green, Justin S. 2018][research_williamsranthony_greenjustins_2018]
- [Williams, Robert W. 1993][research_williamsrobertw_1993]
- [Williams, R. W. 1996][research_williamsrw_1996]
- [Willis, William D., III et al 2002][research_williswilliamdiii_zakrzwskicharlesm_2002]
- [Wilson 2004][research_wilson_2004]
- [Wilson et al 2009][research_wilson_clark_2009]
- [Wilson, E. 2001][research_wilsone_2001]
- [Wilson, E. J. 1973][research_wilsonej_1973]
- [Wilson, Truman and Xiong, Xiaoxiong 2016][research_wilsontruman_xiongxiaoxiong_2016]
- [Windsor 1979][research_windsor_1979]
- [Wintz, P. A. 1971][research_wintzpa_1971]
- [Wißmann et al 2026][research_wissmann_kahler_2026]
- [Witkovský 2025][research_witkovsky_2025]
- [Wnuk, S. P., Jr. and Wnuk, V. P. 1997][research_wnukspjr_wnukvp_1997]
- [Wolf 2000][research_wolf_2000]
- [Wolff, J. J., Jr. and Fitz, J. F. 1972][research_wolffjjjr_fitzjf_1972]
- [Wong and Brown 1965][research_wong_brown_1965]
- [Wong and Brown 1968][research_wong_brown_1968]
- [Wong, Andrea R. et al 2011][research_wongandrear_polzinkurta_2011]
- [Wong, Andrea R. et al 2011][research_wongandrear_toftulalexandra_2011]
- [Woodfield 1970][research_woodfield_1970]
- [Wood, G. E. and Risa, T. 1974][research_woodge_risat_1974]
- [Woods, Thomas N. and Rottman, Gary J. 1990][research_woodsthomasn_rottmangaryj_1990]
- [Woodyard 2026][research_woodyard_2026]
- [Worden and Inman 2010][research_worden_inman_2010]
- [Wrbanek, John D. and Fralick, Gustave C. 2007][research_wrbanekjohnd_fralickgustavec_2007]
- [Wu 2013][research_wu_2013]
- [Wu et al 1999][research_wu_fuller_1999]
- [Wu et al 2026][research_wu_li_2026]
- [Wu et al 2015][research_wu_liu_2015]
- [Wu et al 2020][research_wu_tian_2020]
- [Wu et al 2022][research_wu_yu_2022]
- [Wu et al 2022][research_wu_yu_2022_b]
- [Wu and Zhang 2023][research_wu_zhang_2023]
- [Wuilbercq et al 2014][research_wuilbercq_pescetelli_2014]
- [Wuye et al 2001][research_wuye_yu_2001]
- [Wye et al 1963][research_wye_teicher_1963]
- [Wyett, L. et al 1987][research_wyettl_maramj_1987]
- [X-33/RLV Program Aerospike Engines 1999][research_x_33_rlv_program_1999]
- [Xiao et al 2026][research_xiao_chang_2026]
- [Xiaowen Dai et al][research_xiaowendai_ray]
- [Xie 2010][research_xie_2010]
- [Xie et al 2020][research_xie_zhang_2020]
- [Xing et al 2024][research_xing_feng_2024]
- [Xinguo et al 2024][research_xinguo_ting_2024]
- [Xiong 2018][research_xiong_2018]
- [Xiong, Xiaoxiong et al 2018][research_xiongxiaoxiong_angalamit_2018]
- [Xiong, Xiaoxiong et al 2011][research_xiongxiaoxiong_sunjunqiang_2011]
- [Xiong, Xiaoxiong et al 2012][research_xiongxiaoxiong_wuaisheng_2012]
- [Xu 2005][research_xu_2005]
- [Xu 2009][research_xu_2009]
- [Xu et al 2025][research_xu_guo_2025]
- [Xu et al 2023][research_xu_huang_2023]
- [Xu and Lan 2018][research_xu_lan_2018]
- [Xu and Pei 2016][research_xu_pei_2016]
- [Xu and Tang 2010][research_xu_tang_2010]
- [Xu et al 2024][research_xu_zhang_2024]
- [Xu and Zhao 2016][research_xu_zhao_2016]
- [Xu et al 2019][research_xu_zhou_2019]
- [Xue et al 2025][research_xue_xie_2025]
- [Yadav et al 2018][research_yadav_bodavula_2018]
- [Yadav et al 2026][research_yadav_tripathi_2026]
- [Yairi et al][research_yairi_nakatsugaawa]
- [Yairi et al 2004][research_yairi_ogasawara_2004]
- [Yamada 2000][research_yamada_2000]
- [Yamada et al 2022][research_yamada_nagata_2022]
- [Yamakawa et al 2001][research_yamakawa_higuchi_2001]
- [Yamanishi et al 2004][research_yamanishi_kimura_2004]
- [Yamashita et al 2026][research_yamashita_nutzel_2026]
- [Yan et al 2022][research_yan_wei_2022]
- [Yang 1994][research_yang_1994]
- [Yang 2004][research_yang_2004]
- [Yang 2021][research_yang_2021]
- [Yang 2022][research_yang_2022]
- [Yang et al 2024][research_yang_gan_2024]
- [Yang et al 2006][research_yang_hu_2006]
- [Yang et al 2021][research_yang_ma_2021]
- [Yang and Naraghi 2020][research_yang_naraghi_2020]
- [Yang et al 2025][research_yang_peng_2025]
- [Yang et al 2016][research_yang_qiu_2016]
- [Yang et al 2026][research_yang_wang_2026]
- [Yang et al 2011][research_yang_zhang_2011]
- [Yang et al 2026][research_yang_zhang_2026]
- [Yang et al 2019][research_yang_zheng_2019]
- [Yao et al 2016][research_yao_liang_2016]
- [Yap, Keng C. 2010][research_yapkengc_2010]
- [Yap, Keng C. et al 2011][research_yapkengc_maciasjesus_2011]
- [Yavuz and Cihan 2026][research_yavuz_cihan_2026]
- [Ye and Law 2014][research_ye_law_2014]
- [Yellott 1982][research_yellott_1982]
- [Yerushalmi and Glick 1982][research_yerushalmi_glick_1982]
- [Yesmagambetov et al 2023][research_yesmagambetov_mussabekov_2023]
- [Ying et al 2018][research_ying_fang_2018]
- [Yoda et al 2015][research_yoda_ito_2015]
- [Yoshida et al 2016][research_yoshida_kimura_2016]
- [Young, D. R. et al 1977][research_youngdr_howardwh_1977]
- [Yu et al 2026][research_yu_campbell_2026]
- [Yu et al 2022][research_yu_fan_2022]
- [Yu et al 2021][research_yu_song_2021]
- [Yu et al 2014][research_yu_sun_2014]
- [Yu and Tian 2016][research_yu_tian_2016]
- [Yu et al 2018][research_yu_yang_2018]
- [Yu et al 2024][research_yu_yu_2024]
- [Yuan et al 2021][research_yuan_zhao_2021]
- [Yue et al 2022][research_yue_lin_2022]
- [Yuen, J. H. et al 1982][research_yuenjh_divsalard_1982]
- [Zachary Muckler 2022][research_zacharymuckler_2022]
- [Zagrai et al 2011][research_zagrai_barnes_2011]
- [Zahm, A F et al 1929][research_zahmaf_smithrh_1929]
- [Zahzah, Mohamad et al 2000][research_zahzahmohamad_korkoszgregoryj_2000]
- [Zakharov et al 2024][research_zakharov_botsiura_2024]
- [Zakrajsek, June F. 1991][research_zakrajsekjunef_1991]
- [Zaman, Afroz et al 2011][research_zamanafroz_bauchmatthew_2011]
- [Zangl and Pérez 2025][research_zangl_perez_2025]
- [Zapata et al 2023][research_zapata_roncero_2023]
- [Zappa et al 2013][research_zappa_malavasi_2013]
- [Zaragoza Prous et al 2025][research_zaragozaprous_grustangutierrez_2025]
- [Zdenek and Anthenien 2004][research_zdenek_anthenien_2004]
- [Zdravković et al 2021][research_zdravkovic_ilic_2021]
- [Zeeshan et al 2009][research_zeeshan_waheed_2009]
- [Zeidan][research_zeidan]
- [Zein-Sabatto et al 2012][research_zeinsabatto_mikhail_2012]
- [Zhang 2016][research_zhang_2016]
- [Zhang et al 2018][research_zhang_bi_2018]
- [Zhang et al 2017][research_zhang_guo_2017]
- [Zhang et al 2026][research_zhang_hu_2026]
- [Zhang et al 2018][research_zhang_huang_2018]
- [Zhang et al 2019][research_zhang_huang_2019]
- [Zhang et al 2017][research_zhang_li_2017]
- [Zhang et al 2022][research_zhang_liu_2022]
- [Zhang et al 2026][research_zhang_pan_2026]
- [Zhang and Pang][research_zhang_pang]
- [Zhang et al 2026][research_zhang_sheng_2026]
- [Zhang et al 2019][research_zhang_teng_2019]
- [Zhang et al 2018][research_zhang_tian_2018]
- [Zhang et al 2019][research_zhang_wang_2019]
- [Zhang et al 2022][research_zhang_wang_2022]
- [Zhang et al 2018][research_zhang_xu_2018]
- [Zhang et al 2022][research_zhang_xu_2022]
- [Zhang et al 2023][research_zhang_yang_2023]
- [Zhang et al 2016][research_zhang_yu_2016]
- [Zhang et al 2022][research_zhang_zhang_2022]
- [Zhang et al 2024][research_zhang_zhang_2024]
- [Zhang et al 2017][research_zhang_zong_2017]
- [Zhao 2002][research_zhao_2002]
- [Zhao 2022][research_zhao_2022]
- [Zhao et al 2018][research_zhao_cai_2018]
- [Zhao et al 2024][research_zhao_han_2024]
- [Zhao et al 2018][research_zhao_he_2018]
- [Zhao et al 2024][research_zhao_he_2024]
- [Zhao et al 2020][research_zhao_li_2020]
- [Zhao et al 2000][research_zhao_mo_2000]
- [Zhao et al 2025][research_zhao_pan_2025]
- [Zhao et al 2017][research_zhao_wu_2017]
- [Zhao et al 2024][research_zhao_yu_2024]
- [Zhao et al 2023][research_zhao_zhao_2023]
- [Zhaoqing and Hailong 2016][research_zhaoqing_hailong_2016]
- [Zhe et al 2018][research_zhe_meizhen_2018]
- [Zheng et al 2020][research_zheng_fu_2020]
- [Zheng et al 2019][research_zheng_zhao_2019]
- [Zhengxiang et al 2018][research_zhengxiang_tao_2018]
- [Zhi et al 2015][research_zhi_ran_2015]
- [Zhipeng Wang et al 2024][research_zhipengwang_juliabarsi_2024]
- [Zhong et al 2023][research_zhong_jiang_2023]
- [Zhou et al 2024][research_zhou_hu_2024]
- [Zhou et al 2014][research_zhou_lin_2014]
- [Zhou et al 2025][research_zhou_minzhao_2025]
- [Zhou et al 2024][research_zhou_wang_2024]
- [Zhou et al 2025][research_zhou_wang_2025]
- [Zhou et al 2024][research_zhou_xu_2024]
- [Zhou et al 2016][research_zhou_zhangduizhong_2016]
- [Zhou et al 2014][research_zhou_zhao_2014]
- [Zhou et al 2013][research_zhou_zhou_2013]
- [Zhu et al 2000][research_zhu_banker_2000]
- [Zhu et al 2015][research_zhu_tian_2015]
- [Zhu et al 2017][research_zhu_tian_2017]
- [Zhu et al 2023][research_zhu_yan_2023]
- [Zhuo et al 2023][research_zhuo_zhang_2023]
- [Ziegler 1963][research_ziegler_1963]
- [Ziemer and Lambert 1962][research_ziemer_lambert_1962]
- [Ziemer, J. K. 2001][research_ziemerjk_2001]
- [Zilic et al 2007][research_zilic_hitt_2007]
- [Zimmerli et al 2025][research_zimmerli_arkwright_2025]
- [Zimpfer 1999][research_zimpfer_1999]
- [Zishka and Agarwal 2015][research_zishka_agarwal_2015]
- [Zrubek, W. E. 1966][research_zrubekwe_1966]
- [Zubrin and Clapp 1996][research_zubrin_clapp_1996]
- [Zubrin and Decher 1991][research_zubrin_decher_1991]
- [Zuckerwar, Allan J. and Scott, Michael A. 2004][research_zuckerwarallanj_scottmichaela_2004]
- [Żurawka et al 2023][research_zurawka_sahbon_2023]


[ref_abl_pug]: https://ablspacesystems.com/wp-content/uploads/2022/06/ABL-Payload-Users-Guide-2022-V1.pdf
[ref_afrl_arise]: https://afresearchlab.com/technology/arise-and-fly/
[ref_aliasing]: https://en.wikipedia.org/wiki/Aliasing
[ref_allen_perkins]: https://ntrs.nasa.gov/citations/19930090962
[ref_arise_award]: https://www.aerotechnews.com/edwardsafb/2020/04/14/afrl-awards-agreements-under-aerospike-rocket-integration-and-sub-orbital-experiment-arise-program/
[ref_atm_constants]: https://ntrs.nasa.gov/citations/19760017709
[ref_barrowman]: https://ntrs.nasa.gov/citations/20010047838
[ref_convex_hull]: https://en.wikipedia.org/wiki/Convex_hull
[ref_dft]: https://en.wikipedia.org/wiki/Discrete_Fourier_transform
[ref_ds_x63]: https://www.designation-systems.net/dusrm/app4/x-63.html
[ref_ds_x64]: https://www.designation-systems.net/dusrm/app4/x-64.html
[ref_dynamic_pressure]: https://en.wikipedia.org/wiki/Dynamic_pressure
[ref_f404_measurement]: https://ntrs.nasa.gov/citations/19900002425
[ref_fineness]: https://en.wikipedia.org/wiki/Fineness_ratio
[ref_gravity_turn]: https://en.wikipedia.org/wiki/Gravity_turn
[ref_invocon_about]: https://www.invocon.com/about/
[ref_invocon_home]: https://www.invocon.com/
[ref_mds_addendum]: https://www.designation-systems.net/usmilav/412015-L(addendum).html
[ref_moffat_1982]: https://doi.org/10.1115/1.3241818
[ref_nyquist_1928]: https://doi.org/10.1109/5.989875
[ref_propulsion_forces]: https://ntrs.nasa.gov/citations/19750057617
[ref_rocketlab]: https://afresearchlab.com/wp-content/uploads/2022/09/AFRL_Rocket-Lab-background_0922.pdf
[ref_scale_height]: https://en.wikipedia.org/wiki/Scale_height
[ref_shannon_1949]: https://doi.org/10.1109/jrproc.1949.232969
[ref_specific_force]: https://en.wikipedia.org/wiki/Proper_acceleration
[ref_support_function]: https://en.wikipedia.org/wiki/Support_function
[ref_thrust_determination]: https://ntrs.nasa.gov/citations/19880028000
[ref_thrust_methodology]: https://ntrs.nasa.gov/citations/19840046665
[ref_thrust_realtime]: https://ntrs.nasa.gov/citations/19860019465
[ref_thrust_uncertainty]: https://ntrs.nasa.gov/citations/19880028001
[ref_thrust_uncertainty_app]: https://ntrs.nasa.gov/citations/19840046666
[ref_usaspending]: https://www.usaspending.gov/
[ref_usatm1976]: https://ntrs.nasa.gov/citations/19770009539
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
[related_post_a344_northrop_grumman_x47]: {% post_url 2025-11-22-x_planes_northrop_grumman_x47 %}
[related_post_a345_boeing_x48]: {% post_url 2025-11-23-x_planes_boeing_x48 %}
[related_post_a346_piasecki_x49]: {% post_url 2025-11-24-x_planes_piasecki_x49 %}
[related_post_a347_boeing_x50]: {% post_url 2025-11-25-x_planes_boeing_x50 %}
[related_post_a348_boeing_x51]: {% post_url 2025-11-26-x_planes_boeing_x51 %}
[related_post_a349_x52_designation_refused]: {% post_url 2025-11-27-x_planes_x52_designation_refused %}
[related_post_a350_boeing_x53]: {% post_url 2025-11-28-x_planes_boeing_x53_active_aeroelastic_wing %}
[related_post_a351_gulfstream_x54]: {% post_url 2025-11-29-x_planes_gulfstream_x54 %}
[related_post_a352_lockheed_martin_x55]: {% post_url 2025-11-30-x_planes_lockheed_martin_x55_acca %}
[related_post_a353_lockheed_martin_x56]: {% post_url 2025-12-01-x_planes_lockheed_martin_x56 %}
[related_post_a354_esaero_x57_maxwell]: {% post_url 2025-12-02-x_planes_esaero_x57_maxwell %}
[related_post_a355_x58_slot_taken_by_xq58]: {% post_url 2025-12-03-x_planes_x58_slot_taken_by_xq58 %}
[related_post_a356_x59_quesst]: {% post_url 2025-12-04-x_planes_lockheed_martin_x59_quesst %}
[related_post_a357_generation_orbit_x60]: {% post_url 2025-12-05-x_planes_generation_orbit_x60 %}
[related_post_a358_dynetics_x61_gremlins]: {% post_url 2025-12-06-x_planes_dynetics_x61_gremlins %}
[related_post_a359_lockheed_martin_x62_vista]: {% post_url 2025-12-07-x_planes_lockheed_martin_x62_vista %}
[related_post_a360_abl_space_systems_x63]: {% post_url 2025-12-08-x_planes_abl_space_systems_x63 %}
[research_3d_printing]: https://doi.org/10.1036/1097-8542.br1008201
[research_a_global_2001]: https://ntrs.nasa.gov/citations/20010114460
[research_a_hydro_acoustic_2023]: https://doi.org/10.1063/5.0157377
[research_a_sampathkumar_2024]: https://doi.org/10.1051/matecconf/202439303004
[research_aaronpearlman_matthewmontanaro_2020]: https://ntrs.nasa.gov/citations/20205005371
[research_abbas_2024]: https://doi.org/10.31224/4258
[research_abbott_walker_1970]: https://doi.org/10.2514/6.1970-1401
[research_abbottirah_1937]: https://ntrs.nasa.gov/citations/19930081378
[research_abdala_burden_2023]: https://doi.org/10.2514/6.2023-4386
[research_abdelwahabmahmood_biesiadnythomasj_1987]: https://ntrs.nasa.gov/citations/19870019124
[research_abhayapala_kennedy_1999]: https://doi.org/10.1049/el:19990561
[research_abilleirafernando_2013]: https://ntrs.nasa.gov/citations/20150007329
[research_abilleirafernando_halsellallen_2019]: https://ntrs.nasa.gov/citations/20190000334
[research_abilleirafernando_kruizingagerard_2021]: https://ntrs.nasa.gov/citations/20220000775
[research_abrahamm_valsa_2018]: https://doi.org/10.18520/cs/v114/i01/144-147
[research_adairbm_polgerj_1967]: https://ntrs.nasa.gov/citations/19680034576
[research_adamovskygrigory_mackeyjeffreyr_2014]: https://ntrs.nasa.gov/citations/20150017781
[research_adams_thompson_1983]: https://doi.org/10.4271/831438
[research_adams_thompson_1983_b]: https://doi.org/10.4271/831439
[research_adamsgl_bradtaj_1971]: https://ntrs.nasa.gov/citations/19720007206
[research_adamsmacc_1951]: https://ntrs.nasa.gov/citations/19690094051
[research_adaptive_compressive_1966]: https://ntrs.nasa.gov/citations/19680016330
[research_adaptive_telemetry_1968]: https://ntrs.nasa.gov/citations/19680017200
[research_addy_1970]: https://doi.org/10.21236/ad0875875
[research_adkinsfl_griffince_1962]: https://ntrs.nasa.gov/citations/19630008739
[research_adolphsenjw_malinowskiab_1964]: https://ntrs.nasa.gov/citations/19640037403
[research_advanced_ducted]: https://doi.org/10.4271/air5450
[research_advanced_telemetry_1990]: https://ntrs.nasa.gov/citations/19910007736
[research_advisorygroupforaerospaceresearchanddevelopment_1979]: https://ntrs.nasa.gov/citations/19800002041
[research_aerojetgeneralcorpsacramentoca_1963]: https://doi.org/10.21236/ad0423407
[research_aerospike_engine]: https://doi.org/10.1036/1097-8542.757478
[research_aftosmismichaelj_2011]: https://ntrs.nasa.gov/citations/20110008384
[research_agarwal_2023]: https://doi.org/10.2514/6.2023-71342
[research_agarwal_2026]: https://doi.org/10.58445/rars.4120
[research_agarwalla_2025]: https://doi.org/10.36948/ijfmr.2025.v07i05.58723
[research_ageev_pavlenko_2016]: https://doi.org/10.1108/aeat-02-2015-0052
[research_agourakis_agourakis_2026]: https://doi.org/10.22541/au.177499352.24860177/v1
[research_aguilarrobert_1999]: https://ntrs.nasa.gov/citations/19990062658
[research_ahlborn_blake_2009]: https://doi.org/10.1139/z08-144
[research_ahlborn_loehberg_1979]: https://doi.org/10.2514/6.1979-172
[research_ahmadmohammad_tranthanh_2011]: https://ntrs.nasa.gov/citations/20150008830
[research_ahmadrashida_cashstephenf_2002]: https://ntrs.nasa.gov/citations/20020090843
[research_ahmed_mishra_2026]: https://doi.org/10.2139/ssrn.6854027
[research_ahmedrafiq_1990]: https://ntrs.nasa.gov/citations/19900016050
[research_ainsleigh_george_1988]: https://doi.org/10.21236/ada204923
[research_airforcetestpilotschooledwardsafbca_1962]: https://doi.org/10.21236/ada320208
[research_aithani_shahid_2023]: https://doi.org/10.33564/ijeast.2023.v08i01.023
[research_aji_agusdian_2025]: https://doi.org/10.1109/tssa68467.2025.11303833
[research_ajith_s_2016]: https://doi.org/10.2514/6.2016-4768
[research_ajovalasit_2011]: https://doi.org/10.1111/j.1475-1305.2009.00691.x
[research_akbari_pfaff_2020]: https://doi.org/10.5194/egusphere-egu2020-12853
[research_akersjamesc_sillsjoelwjr_2020]: https://ntrs.nasa.gov/citations/20200000863
[research_akhtar_borggaard_2009]: https://doi.org/10.1115/imece2009-13090
[research_akl_elattar_2025]: https://doi.org/10.1088/1742-6596/3070/1/012021
[research_alam_karim_2026]: https://doi.org/10.1063/5.0329046
[research_alam_kumar_2018]: https://doi.org/10.1177/0142331217752041
[research_alam_kumar_2018_b]: https://doi.org/10.1016/j.measurement.2018.06.057
[research_alam_kumar_2020]: https://doi.org/10.1177/0142331220960665
[research_alam_kumar_2021]: https://doi.org/10.1115/imece2021-69072
[research_alam_pant_2019]: https://doi.org/10.2514/1.c034887
[research_albakri]: https://doi.org/10.32469/10355/70012
[research_albakri_kluever_2017]: https://doi.org/10.4236/aast.2017.24004
[research_albanese_meyers_2012]: https://doi.org/10.21236/ada571357
[research_alexanderleslie_chapmanjack_2008]: https://ntrs.nasa.gov/citations/20080036842
[research_alexisjharroun_stephendheister_2020]: https://ntrs.nasa.gov/citations/20230009329
[research_alghamdi_nadeem_2018]: https://doi.org/10.1109/glocom.2018.8647191
[research_alhassanmohammad_brittonpaul_2018]: https://ntrs.nasa.gov/citations/20180007901
[research_alhorndeanc_howarddavide_2001]: https://ntrs.nasa.gov/citations/20020005125
[research_ali_crawford_1988]: https://doi.org/10.2514/6.1988-3212
[research_ali_pandey_2016]: https://doi.org/10.3390/s16060862
[research_alialiyahn_borrerjerryl_2013]: https://ntrs.nasa.gov/citations/20140008317
[research_alialiyahn_borrerjerryl_2013_b]: https://ntrs.nasa.gov/citations/20140009987
[research_allard_2024]: https://doi.org/10.1038/s41578-024-00748-0
[research_allen_1981]: https://doi.org/10.2514/6.1981-1550
[research_allen_1983]: https://doi.org/10.2514/3.28373
[research_allen_sauvageau_1994]: https://doi.org/10.2514/6.1994-4499
[research_allenkj_wrigleywr_1965]: https://ntrs.nasa.gov/citations/19650041513
[research_allisonsidneyg_prosserwilliamh_2007]: https://ntrs.nasa.gov/citations/20070031702
[research_almaraashli_youseffi_2025]: https://doi.org/10.20944/preprints202504.0678.v1
[research_almasoud_singh_2001]: https://doi.org/10.1115/imece2001/dsc-24562
[research_alon_rafaely_2014]: https://doi.org/10.1109/hscma.2014.6843267
[research_alshehabi_newman_2002]: https://doi.org/10.2514/6.2002-4750
[research_alstondw_barberjb_1967]: https://ntrs.nasa.gov/citations/19670006335
[research_alterstephenj_brauckmanngregoryj_2015]: https://ntrs.nasa.gov/citations/20160006469
[research_alterstephenj_brauckmanngregoryj_2015_b]: https://ntrs.nasa.gov/citations/20160005934
[research_alvord_arias_2024]: https://doi.org/10.1109/aero58975.2024.10521242
[research_amertahani_trippjohn_2004]: https://ntrs.nasa.gov/citations/20040086552
[research_amyffagan_khairulbmqzaman]: https://ntrs.nasa.gov/citations/20250010664
[research_amyffagan_khairulbmqzaman_2024]: https://ntrs.nasa.gov/citations/20240013494
[research_amyffagan_khairulbmqzaman_b]: https://ntrs.nasa.gov/citations/20240014001
[research_an_analytical_1966]: https://ntrs.nasa.gov/citations/19660021027
[research_an_examination_1965]: https://ntrs.nasa.gov/citations/19650014213
[research_anandaraj_sarkar_2019]: https://doi.org/10.12783/ballistics2019/33118
[research_anderson_heister_2013]: https://doi.org/10.21236/ada577052
[research_anderson_heister_2015]: https://doi.org/10.21236/ad1001343
[research_anderson_mcamis_1996]: https://doi.org/10.2514/6.1996-2613
[research_anderson_son_2012]: https://doi.org/10.21236/ada566310
[research_andersonjd_1966]: https://ntrs.nasa.gov/citations/19660014272
[research_andersonkarlf_1993]: https://ntrs.nasa.gov/citations/19930070383
[research_andersonkarlf_1995]: https://ntrs.nasa.gov/citations/19950012320
[research_andersonpg_chenggc_1993]: https://ntrs.nasa.gov/citations/19950016993
[research_andersonpg_chenys_1992]: https://ntrs.nasa.gov/citations/19920023009
[research_andersonto_galloaj_1967]: https://ntrs.nasa.gov/citations/19680061768
[research_andersson_forsell_1979]: https://doi.org/10.2514/6.1979-518
[research_andrewmbrown]: https://ntrs.nasa.gov/citations/20190033330
[research_andrewroberts_claudehashem_1995]: https://ntrs.nasa.gov/citations/19960022498
[research_andrews_1998]: https://doi.org/10.2514/6.1998-3955
[research_andrie_2009]: https://doi.org/10.4271/2009-01-0245
[research_andrieu_2026]: https://doi.org/10.1109/lawp.2026.3714057
[research_anex_russell_1991]: https://doi.org/10.2514/6.1991-2533
[research_animadsabale_erikaegallegos_2026]: https://ntrs.nasa.gov/citations/20250011659
[research_animasabale_erikaegallegos_2026]: https://ntrs.nasa.gov/citations/20260005145
[research_anjana_renjith_2022]: https://doi.org/10.1007/978-981-19-3938-9_2
[research_ansonkw_1977]: https://ntrs.nasa.gov/citations/19770017184
[research_anthonyscottcraig_jaydenehauglie]: https://ntrs.nasa.gov/citations/20205004864
[research_antinoner_kowh_1969]: https://ntrs.nasa.gov/citations/19700005800
[research_antonazzi_1981]: https://doi.org/10.4271/811076
[research_antonelli_pepe_2020]: https://doi.org/10.1007/978-3-030-34747-5_23
[research_anuskiewicz_cave_2026]: https://doi.org/10.2514/6.2026-2476
[research_anzaloneevanj_johnstonhunter_2018]: https://ntrs.nasa.gov/citations/20180006400
[research_aogaki_kitamura_2017]: https://doi.org/10.2514/6.2017-1212
[research_aogaki_kitamura_2019]: https://doi.org/10.2322/tastj.17.104
[research_apollo_11_2010]: https://ntrs.nasa.gov/citations/20110011709
[research_apollo_mission_1970]: https://ntrs.nasa.gov/citations/19700014995
[research_apollo_saturn_5_1973]: https://ntrs.nasa.gov/citations/19760006057
[research_appendix_c_1992]: https://doi.org/10.2514/5.9781600866197.0399.0403
[research_appendix_h_2026]: https://doi.org/10.1002/9781394438303.app8
[research_appendix_k_2026]: https://doi.org/10.1002/9781394438303.app11
[research_appichwhjr_turnerkl_1958]: https://ntrs.nasa.gov/citations/19710066227
[research_applications_of_1999]: https://doi.org/10.1109/acc.1999.786112
[research_aprovitola_iuspa_2019]: https://doi.org/10.5772/intechopen.85603
[research_aprovitola_iuspa_2019_b]: https://doi.org/10.1155/2019/6069528
[research_arcangelijp_crochemorem_1993]: https://ntrs.nasa.gov/citations/19940019483
[research_ardalansm_antreasianpg_2008]: https://ntrs.nasa.gov/citations/20150014741
[research_armstrong_1964]: https://doi.org/10.2514/3.27628
[research_arndtgd_novosadsw_1970]: https://ntrs.nasa.gov/citations/19700014968
[research_arnett_1993]: https://doi.org/10.2514/6.1993-2321
[research_arning_wu_2010]: https://doi.org/10.4271/2010-01-1507
[research_aronsteindavidl_smithjscott_2016]: https://ntrs.nasa.gov/citations/20160003130
[research_arora_ananthasayanam_2003]: https://doi.org/10.2514/6.2003-5547
[research_arora_george_2003]: https://doi.org/10.2514/6.2003-5546
[research_arrington_molloy_1967]: https://doi.org/10.2514/6.1967-1309
[research_arrondeperez_zangl_2026]: https://doi.org/10.1016/j.measurement.2025.119109
[research_arueti_1988]: https://doi.org/10.1007/978-1-4613-1009-9_109
[research_aruna_devi_2012]: https://doi.org/10.1504/ijad.2012.049128
[research_ascent_trajectory_2022]: https://doi.org/10.2514/5.9781624106422.0337.0406
[research_ascraig_mjhawkins]: https://ntrs.nasa.gov/citations/20205004525
[research_askinsbruce_robinsonkimberlyf_2017]: https://ntrs.nasa.gov/citations/20170005390
[research_aslan_kara_2026]: https://doi.org/10.1016/j.ijhydene.2026.153819
[research_aso_sugimoto_2005]: https://doi.org/10.1007/978-3-540-27009-6_15
[research_aso_tani_2018]: https://doi.org/10.2514/6.2018-1415
[research_aso_tani_2018_b]: https://doi.org/10.2514/6.2018-1415.c1
[research_astorg_barreauluiverc_1995]: https://doi.org/10.2514/6.1995-1532
[research_atamanchuk_2025]: https://doi.org/10.62717/2221-4550-2025-1-024
[research_aukermancarla_1991]: https://ntrs.nasa.gov/citations/19920013861
[research_aulchenko_2006]: https://doi.org/10.1007/s10891-006-0190-2
[research_austinroberte_risingjerryj_1999]: https://ntrs.nasa.gov/citations/19990054757
[research_austinroberte_risingjerryj_2000]: https://ntrs.nasa.gov/citations/20000033992
[research_averkineg_fryertb_1964]: https://ntrs.nasa.gov/citations/19660012959
[research_averyanov_kazantsev_2021]: https://doi.org/10.18127/j20700970-202104-07
[research_ayoungchee_mack_2013]: https://doi.org/10.1097/ta.0b013e31827a0bb6
[research_azpurua_paez_2014]: https://doi.org/10.1109/isemc.2014.6898992
[research_b_kasher_2021]: https://doi.org/10.2514/6.2021-3545
[research_baarswoutijnj_tinneycharlese_2011]: https://ntrs.nasa.gov/citations/20120001479
[research_baarswoutijnj_tinneycharlese_2012]: https://ntrs.nasa.gov/citations/20120014182
[research_babbcd_fullerde_1967]: https://ntrs.nasa.gov/citations/19670020031
[research_babbittnormaneiii_1992]: https://ntrs.nasa.gov/citations/19920066309
[research_babcock_coe_1971]: https://doi.org/10.1109/temc.1971.303123
[research_bach_2017]: https://doi.org/10.26226/morressier.59c106e9d462b80292389eb7
[research_baerja_hecklerchjr_1966]: https://ntrs.nasa.gov/citations/19660029133
[research_baerja_hecklerchjr_1966_b]: https://ntrs.nasa.gov/citations/19660013622
[research_baetz_1974]: https://doi.org/10.21236/ad0783200
[research_baetz_1975]: https://doi.org/10.21236/ada020041
[research_baggeroer_1999]: https://doi.org/10.21236/ada630309
[research_baghdadyej_1962]: https://ntrs.nasa.gov/citations/19630020453
[research_bagri_majid_2009]: https://doi.org/10.1109/aero.2009.4839367
[research_bai_weng_2014]: https://doi.org/10.4028/www.scientific.net/amm.628.293
[research_baileyjs_johnsondr_1964]: https://ntrs.nasa.gov/citations/19640032206
[research_baker_1969]: https://doi.org/10.2514/6.1969-452
[research_baker_stockton_1965]: https://doi.org/10.21236/ad0624926
[research_bakker_madhumitha_2026]: https://doi.org/10.1007/978-981-95-2239-2_23
[research_bakowski_radziszewski_2016]: https://doi.org/10.4028/www.scientific.net/amm.827.77
[research_bal_consoliverzack_2019]: https://doi.org/10.1089/space.2018.0036
[research_balachdean_1995]: https://ntrs.nasa.gov/citations/19960014386
[research_balageas_2002]: https://doi.org/10.1016/s1270-9638(01)01140-3
[research_balaji_navinkumar_2021]: https://doi.org/10.1016/j.matpr.2021.03.124
[research_balcomb_1972]: https://doi.org/10.2514/6.1972-1064
[research_baldwinha_freymanrw_1973]: https://ntrs.nasa.gov/citations/19740013686
[research_balepin_2001]: https://doi.org/10.2514/6.2001-3236
[research_balepin_czysz_2001]: https://doi.org/10.2514/6.2001-1911
[research_balepin_czysz_2001_b]: https://doi.org/10.2514/2.5870
[research_balepinvladimir_pricejohn_1999]: https://ntrs.nasa.gov/citations/19990061890
[research_ballard_1992]: https://doi.org/10.2514/6.1992-3536
[research_ballardrichardo_2003]: https://ntrs.nasa.gov/citations/20030111910
[research_balusamy_a_2024]: https://doi.org/10.1108/aeat-04-2023-0088
[research_bandyopadhyayalak_hamillbrian_2011]: https://ntrs.nasa.gov/citations/20120003148
[research_banksb_rawlinv_1975]: https://ntrs.nasa.gov/citations/19750040879
[research_bao_dong_2023]: https://doi.org/10.1007/978-981-19-6613-2_566
[research_bao_li_2020]: https://doi.org/10.1177/1475921720972416
[research_bao_wang_2019]: https://doi.org/10.1109/safeprocess45799.2019.9213335
[research_baran_blanchard_2014]: https://doi.org/10.2514/6.2014-3548
[research_barani]: https://doi.org/10.33915/etd.8244
[research_barbosa_silva_2016]: https://doi.org/10.21528/cbrn2007-014
[research_barkhoudarian_szemenyei_1988]: https://doi.org/10.2514/6.1988-3113
[research_barkhoudariansarkis_kittingerscott_2006]: https://ntrs.nasa.gov/citations/20070013796
[research_barneswp_billingsleyjb_1964]: https://ntrs.nasa.gov/citations/19640019275
[research_barraza_1962]: https://doi.org/10.4271/620334
[research_barrazarm_1962]: https://ntrs.nasa.gov/citations/19730061696
[research_barretchris_1999]: https://ntrs.nasa.gov/citations/19990105819
[research_barros_correia_2026]: https://doi.org/10.3390/technologies14060353
[research_barthandrew_mamichharvey_2015]: https://ntrs.nasa.gov/citations/20150001919
[research_barthelmen_leej_1986]: https://ntrs.nasa.gov/citations/19870028442
[research_barthorpe_worden_2020]: https://doi.org/10.3390/jsan9030031
[research_bartoe_1982]: https://doi.org/10.2514/6.1982-1709
[research_basciano_1998]: https://doi.org/10.2514/6.1998-818
[research_basharina_goncharov_2021]: https://doi.org/10.26732/j.st.2021.1.01
[research_bassen_1967]: https://doi.org/10.21236/ad0653126
[research_bassen_jantz_1966]: https://doi.org/10.21236/ad0646762
[research_bateslakesha_hongliang_2011]: https://ntrs.nasa.gov/citations/20120006693
[research_bathkerda_claussrc_1966]: https://ntrs.nasa.gov/citations/19660056400
[research_batillstephenm_1994]: https://ntrs.nasa.gov/citations/19940032438
[research_batista_trujilho_2025]: https://doi.org/10.12783/shm2025/37503
[research_bauer_1980]: https://doi.org/10.21236/ada080955
[research_bauerab_1981]: https://ntrs.nasa.gov/citations/19810065338
[research_bauerab_kibensv_1982]: https://ntrs.nasa.gov/citations/19850003482
[research_baumgartner_1997]: https://doi.org/10.1063/1.51920
[research_bayerjanicei_varadanvv_1991]: https://ntrs.nasa.gov/citations/19930037972
[research_bayir_akbiyik_2024]: https://doi.org/10.36306/konjes.1474579
[research_bazin_fields_2016]: https://doi.org/10.2514/6.2016-1760
[research_bechtelrd_mateosma_1988]: https://ntrs.nasa.gov/citations/19880018414
[research_bechtoldwr_bjorntjr_1966]: https://ntrs.nasa.gov/citations/19670023684
[research_bechtoldwr_medlinje_1965]: https://ntrs.nasa.gov/citations/19660012530
[research_beck_beach_2003]: https://doi.org/10.21236/ada412349
[research_beckerh_hamiltonh_1965]: https://ntrs.nasa.gov/citations/19660001382
[research_beckerh_tangcn_1966]: https://ntrs.nasa.gov/citations/19660014171
[research_beckpe_1972]: https://ntrs.nasa.gov/citations/19730007713
[research_beckpe_1973]: https://ntrs.nasa.gov/citations/19730017165
[research_beebe]: https://doi.org/10.15368/theses.2009.136
[research_beegum_chacko_2020]: https://doi.org/10.1109/conecct50063.2020.9198525
[research_behera_panda_2025]: https://doi.org/10.54985/peeref.2501p2540962
[research_behn_kisler_2016]: https://doi.org/10.2514/6.2016-3038
[research_behn_tapken_2025]: https://doi.org/10.61782/fa.2025.0829
[research_bejani_mauri_2025]: https://doi.org/10.2139/ssrn.5533446
[research_bejczy_1971]: https://doi.org/10.2514/6.1971-903
[research_bellevillere_langeko_1971]: https://ntrs.nasa.gov/citations/19710055949
[research_bellgu_hindspl_1969]: https://ntrs.nasa.gov/citations/19690026086
[research_bellh_strockj_1980]: https://ntrs.nasa.gov/citations/19820043653
[research_bendotjg_1974]: https://ntrs.nasa.gov/citations/19740057223
[research_benedikt_1953]: https://doi.org/10.2514/8.2809
[research_benedikter_dambrosio_2025]: https://doi.org/10.2514/6.2025-2532
[research_benjaminsburger_caroleaddona]: https://ntrs.nasa.gov/citations/20205002279
[research_benjamintheodoreg_garciaroberto_1993]: https://ntrs.nasa.gov/citations/19950017197
[research_benjamintheodoreg_mcconnaugheypaulk_1991]: https://ntrs.nasa.gov/citations/19910059587
[research_benjauthritb_1976]: https://ntrs.nasa.gov/citations/19760020188
[research_benjauthritb_kemprp_1977]: https://ntrs.nasa.gov/citations/19780016238
[research_benjauthritb_mulhallb_1976]: https://ntrs.nasa.gov/citations/19770007115
[research_bennett_schaub_2021]: https://doi.org/10.1016/j.actaastro.2020.09.009
[research_bennewitz_lineberry_2013]: https://doi.org/10.2514/6.2013-3853
[research_bennink_pate_1989]: https://doi.org/10.1007/978-1-4613-0817-1_106
[research_bennink_pate_1992]: https://doi.org/10.1016/0963-8695(92)90403-4
[research_bensimon_1973]: https://doi.org/10.2514/6.1973-293
[research_bensonhe_mcculloughje_1964]: https://ntrs.nasa.gov/citations/19650025664
[research_benthamsciencepublisher_2012]: https://doi.org/10.2174/978160805024611001010133
[research_bentsmanjoseph_pearlsteinarnej_1990]: https://ntrs.nasa.gov/citations/19900053488
[research_bentzen_1980]: https://doi.org/10.2172/6693728
[research_berggren_ross_1948]: https://doi.org/10.2514/8.4200
[research_bergman_boyd_1981]: https://doi.org/10.2514/6.1981-1549
[research_bergmannmartin_longmanrichardw_1990]: https://ntrs.nasa.gov/citations/19900060705
[research_berkopec_1970]: https://doi.org/10.2514/6.1970-1126
[research_bermanal_aupa_1992]: https://ntrs.nasa.gov/citations/19920020140
[research_bermanjoshua_dudamichael_2009]: https://ntrs.nasa.gov/citations/20130012822
[research_bernstein_linzer_1949]: https://doi.org/10.2514/8.4275
[research_berrierbl_1969]: https://ntrs.nasa.gov/citations/19690012101
[research_berrierbl_1972]: https://ntrs.nasa.gov/citations/19730004272
[research_berrierbl_1973]: https://ntrs.nasa.gov/citations/19730021262
[research_berrierbl_mercerce_1967]: https://ntrs.nasa.gov/citations/19670009635
[research_berrierbl_mercerce_1970]: https://ntrs.nasa.gov/citations/19700008774
[research_bertholdiiijohnw_1986]: https://ntrs.nasa.gov/citations/20080008245
[research_berthomieu_salmon_2024]: https://doi.org/10.61782/fa.2023.1077
[research_bessant_knight_1992]: https://doi.org/10.4271/920821
[research_betancourtzamorarafaelj_1999]: https://ntrs.nasa.gov/citations/19990116773
[research_betheamarkd_rosenthalbrucen_1992]: https://ntrs.nasa.gov/citations/19930051578
[research_betta_liguori_2000]: https://doi.org/10.1016/s0263-2241(99)00068-8
[research_beyma_1986]: https://doi.org/10.2514/6.1986-2529
[research_beyonjeffreyy_kochgradyj_2012]: https://ntrs.nasa.gov/citations/20120007666
[research_beyonjy_kochgj_2010]: https://ntrs.nasa.gov/citations/20100025487
[research_bhatia]: https://doi.org/10.3990/1.9789036542371
[research_bhutianipk_1980]: https://ntrs.nasa.gov/citations/19800051798
[research_bich_dagostino_2007]: https://doi.org/10.1109/amuem.2007.4362566
[research_bickfordrl_duncandb_1990]: https://ntrs.nasa.gov/citations/19910046011
[research_bickfordrl_madzsarg_1990]: https://ntrs.nasa.gov/citations/19900060157
[research_biesiadnytj_leed_1978]: https://ntrs.nasa.gov/citations/19780013169
[research_billprosser]: https://ntrs.nasa.gov/citations/20210018566
[research_bin_hua_2017]: https://doi.org/10.1109/ciapp.2017.8167051
[research_bindal_joshi_2024]: https://doi.org/10.1007/978-981-97-4500-5_5
[research_bindal_kattyayan_2024]: https://doi.org/10.1007/978-981-97-5373-4_17
[research_binder_1993]: https://doi.org/10.2514/6.1993-2357
[research_bindermichael_felderjamesl_1993]: https://ntrs.nasa.gov/citations/19950017371
[research_bindermichael_tomsikthomas_1997]: https://ntrs.nasa.gov/citations/19970010379
[research_bindermichaelp_1995]: https://ntrs.nasa.gov/citations/19950022693
[research_birkeland_meuser_1999]: https://doi.org/10.2514/6.1999-4463
[research_bishop]: https://doi.org/10.22215/etd/2022-15171
[research_biswas_khorasgani_2016]: https://doi.org/10.36001/phmconf.2016.v8i1.2551
[research_biswas_khorasgani_2020]: https://doi.org/10.36001/ijphm.2016.v7i4.2467
[research_bjorklund_rogero_1979]: https://doi.org/10.21236/ada072125
[research_blackshire_giurgiutiu_2005]: https://doi.org/10.21236/ada525391
[research_blades_redgrave_2000]: https://doi.org/10.2514/6.2000-1778
[research_blair_degeorge_2000]: https://doi.org/10.21236/ada411290
[research_blairabjr_1980]: https://ntrs.nasa.gov/citations/19810007463
[research_blairabjr_allenjm_1983]: https://ntrs.nasa.gov/citations/19830019688
[research_blairabjr_dillonjamesl_1992]: https://ntrs.nasa.gov/citations/19920039566
[research_blake_cunningham_2006]: https://doi.org/10.2514/6.2006-828
[research_blakestuart_jessemcenulty]: https://ntrs.nasa.gov/citations/20230001023
[research_blalock_fordham_2016]: https://doi.org/10.1109/eucap.2016.7481428
[research_blanchard_rutherford_1984]: https://doi.org/10.2514/6.1984-490
[research_blanchard_rutherford_1985]: https://doi.org/10.2514/3.25775
[research_blanco_rahimov_2016]: https://doi.org/10.2118/183026-ms
[research_block_2_1986]: https://ntrs.nasa.gov/citations/19890004118
[research_bloiseanthony_1995]: https://ntrs.nasa.gov/citations/19960022502
[research_blomshieldfreds_bickercj_1996]: https://ntrs.nasa.gov/citations/19970015930
[research_bloomerharrye_1958]: https://ntrs.nasa.gov/citations/19930089853
[research_bloomquistce_grahamwc_1965]: https://ntrs.nasa.gov/citations/19660003865
[research_blosser_1997]: https://doi.org/10.1063/1.51930
[research_bluelisa_crawfordkevin_1997]: https://ntrs.nasa.gov/citations/19990098445
[research_blum_wurm_1999]: https://doi.org/10.1016/s0273-1177(99)00195-7
[research_blumenthalphilipz_1995]: https://ntrs.nasa.gov/citations/19950023646
[research_bodra_khairnar_2025]: https://doi.org/10.57017/jorit.v4.2(8).05
[research_bodrucki_broilo_2018]: https://doi.org/10.1117/12.2325372
[research_bogart_yang_1992]: https://doi.org/10.1121/1.404544
[research_bogoi_rugescu_2015]: https://doi.org/10.4028/www.scientific.net/amm.811.152
[research_bohlouri_kosari_2014]: https://doi.org/10.5267/j.esm.2014.8.005
[research_bohsejr_bewtram_1979]: https://ntrs.nasa.gov/citations/19840019180
[research_boldissar_alfredson]: https://doi.org/10.1109/aps.1984.1149366
[research_bolhov_klyatchenko_2026]: https://doi.org/10.31649/vitce/2.2026.90
[research_bollino_oppenheimer_2006]: https://doi.org/10.2514/6.2006-6691
[research_bonop_1963]: https://ntrs.nasa.gov/citations/19630022700
[research_bordachev_kolga_2023]: https://doi.org/10.31772/2712-8970-2023-24-1-64-75
[research_bordijohnj_antreasianpete_2005]: https://ntrs.nasa.gov/citations/20060042685
[research_borekrw_1973]: https://ntrs.nasa.gov/citations/19730023355
[research_borekrw_richardsonrb_1969]: https://ntrs.nasa.gov/citations/19690058007
[research_borgna_fusaro_2025]: https://doi.org/10.52202/083092-0064
[research_borkowski_2015]: https://doi.org/10.21236/ad1009765
[research_bornstein_celmins_1989]: https://doi.org/10.2514/6.1989-3395
[research_borowskistanleyk_1991]: https://ntrs.nasa.gov/citations/19910061158
[research_borowskistanleyk_1994]: https://ntrs.nasa.gov/citations/19950009268
[research_borowskistanleyk_ryanstephenw_2018]: https://ntrs.nasa.gov/citations/20180002979
[research_bos_nienkemper_1995]: https://doi.org/10.2514/6.1995-1592
[research_bos_offerman_1999]: https://doi.org/10.2514/6.1999-1704
[research_bossi_nelson_1992]: https://doi.org/10.2514/6.1992-2682
[research_bosworthjohnt_burkenjohnj_1997]: https://ntrs.nasa.gov/citations/19970027694
[research_botelho_martinez_2022]: https://doi.org/10.1007/s12567-022-00423-6
[research_bouslogs_mammanoj_1998]: https://ntrs.nasa.gov/citations/19980200836
[research_bowser_busch_1966]: https://doi.org/10.21236/ad0373294
[research_boyadzhyanvv_1998]: https://ntrs.nasa.gov/citations/20060039947
[research_boykinfm_1985]: https://ntrs.nasa.gov/citations/19850012936
[research_bradford_charania_2004]: https://doi.org/10.2514/6.2004-3514
[research_bradford_stgermain_2010]: https://doi.org/10.2514/6.2010-8672
[research_bradleypf_siemerspmiii_1983]: https://ntrs.nasa.gov/citations/19830035314
[research_brandonlmobley_samanthasummers]: https://ntrs.nasa.gov/citations/20260007712
[research_brauschjf_1972]: https://ntrs.nasa.gov/citations/19720022350
[research_brazzel_1963]: https://doi.org/10.21236/ad0423963
[research_breedkellys_powellmarkw_2010]: https://ntrs.nasa.gov/citations/20100039409
[research_brennen]: https://doi.org/10.15368/theses.2009.95
[research_brentpomeroy_stevenkrist_2024]: https://ntrs.nasa.gov/citations/20230009212
[research_brentwpomeroy_stevenekrist]: https://ntrs.nasa.gov/citations/20220015870
[research_breshears_mccafferty_1966]: https://doi.org/10.2514/6.1966-949
[research_bresnahandl_1968]: https://ntrs.nasa.gov/citations/19690004981
[research_bresnahandl_1969]: https://ntrs.nasa.gov/citations/19690012286
[research_bresnahandl_1972]: https://ntrs.nasa.gov/citations/19720019044
[research_bresnahandl_johnsal_1968]: https://ntrs.nasa.gov/citations/19680020481
[research_brevault]: https://doi.org/10.70675/34a47b90z7ae8z434fzb521zc140dbd67501
[research_brevault_balesdent_2020]: https://doi.org/10.1007/978-3-030-39126-3_12
[research_brianrrichardson]: https://ntrs.nasa.gov/citations/20240000019
[research_briansaulman_robertwagner]: https://ntrs.nasa.gov/citations/20240003010
[research_brinda_arora_2005]: https://doi.org/10.2514/6.2005-3291
[research_brinichpf_jackjr_1965]: https://ntrs.nasa.gov/citations/19650027295
[research_brintonjohn_golubleon_2004]: https://ntrs.nasa.gov/citations/20040084234
[research_briscoe_1986]: https://doi.org/10.1575/1912/7892
[research_brochot_2015]: https://doi.org/10.1255/tosf.73
[research_brociek_hetmaniok_2023]: https://doi.org/10.1016/j.applthermaleng.2022.119405
[research_brock]: https://doi.org/10.15368/theses.2015.5
[research_brock_franke_2004]: https://doi.org/10.2514/6.2004-3903
[research_brockmanmh_1971]: https://ntrs.nasa.gov/citations/19710040619
[research_brockmanmh_1978]: https://ntrs.nasa.gov/citations/19780020182
[research_brockmanmh_easterlingmf_1981]: https://ntrs.nasa.gov/citations/19800000309
[research_broer_benedictus_2022]: https://doi.org/10.3390/aerospace9040183
[research_brogliocj_1973]: https://ntrs.nasa.gov/citations/19730015456
[research_brommaugustfjr_goodwinjuliam_1953]: https://ntrs.nasa.gov/citations/19930093738
[research_brommaugustfjr_goodwinjuliam_1956]: https://ntrs.nasa.gov/citations/19930084477
[research_bronz_garciademarina_2017]: https://doi.org/10.2514/6.2017-0698
[research_brooks_2022]: https://doi.org/10.1109/mspec.2022.9754499
[research_brooks_burkhalter_1988]: https://doi.org/10.2514/6.1988-280
[research_brookstf_marcolinima_1987]: https://ntrs.nasa.gov/citations/19870042585
[research_brosnaniang_mcgarrylouisep_2015]: https://ntrs.nasa.gov/citations/20160011552
[research_brown_coleman_1995]: https://doi.org/10.2514/6.1995-3073
[research_brown_olds_2005]: https://doi.org/10.2514/6.2005-707
[research_brown_sethu_2019]: https://doi.org/10.1121/1.5096184
[research_brownandrew_rufjosephh_2009]: https://ntrs.nasa.gov/citations/20090023551
[research_brownandrewm_2000]: https://ntrs.nasa.gov/citations/20000039356
[research_brownandrewm_2014]: https://ntrs.nasa.gov/citations/20140011713
[research_brownandrewm_bruntyjosepha_2001]: https://ntrs.nasa.gov/citations/20020016609
[research_brownandrewm_delessiojenniferl_2018]: https://ntrs.nasa.gov/citations/20180002030
[research_brownclintone_parkerhermonm_1945]: https://ntrs.nasa.gov/citations/19930091887
[research_browning_1993]: https://doi.org/10.2514/6.1993-1994
[research_brownmk_griffinma_1966]: https://ntrs.nasa.gov/citations/19660025943
[research_brueggec_chafinb_1999]: https://ntrs.nasa.gov/citations/20060034117
[research_brummerea_harringtonrf_1962]: https://ntrs.nasa.gov/citations/19620002467
[research_brummerea_harringtonrf_1963]: https://ntrs.nasa.gov/citations/19640006238
[research_brunermarilyne_brownwilliama_1989]: https://ntrs.nasa.gov/citations/19900058976
[research_brunnerjj_1966]: https://ntrs.nasa.gov/citations/19660014274
[research_bryant_1989]: https://doi.org/10.2514/6.1989-2422
[research_bryant_2010]: https://doi.org/10.21236/ada640536
[research_bryantthomas_crusebryant_1987]: https://ntrs.nasa.gov/citations/19880046439
[research_buchananrp_1986]: https://ntrs.nasa.gov/citations/19870028476
[research_buddhavarapu_charlson_2019]: https://doi.org/10.2514/6.2019-0151
[research_bufalino_1995]: https://doi.org/10.2514/6.1995-3899
[research_bui_murray_2005]: https://doi.org/10.2514/6.2005-3797
[research_buigea_goodew_1965]: https://ntrs.nasa.gov/citations/19650014708
[research_bujes_1962]: https://doi.org/10.21236/ad0286961
[research_bullbarton_diehljames_2001]: https://ntrs.nasa.gov/citations/20020020446
[research_bullbarton_diehljames_2002]: https://ntrs.nasa.gov/citations/20020060112
[research_bullinger_bodensteiner_2018]: https://doi.org/10.1109/itsc.2018.8569508
[research_burchett]: https://doi.org/10.1109/acc.2005.1470279
[research_burdett_1946]: https://doi.org/10.2514/8.4117
[research_burkardtleoa_1992]: https://ntrs.nasa.gov/citations/19920012293
[research_burkees_harriscw_1971]: https://ntrs.nasa.gov/citations/19710024644
[research_burkesdarryla_1998]: https://ntrs.nasa.gov/citations/19990076703
[research_burkhalter_frank_1995]: https://doi.org/10.2514/6.1995-1894
[research_burkhalter_frank_1996]: https://doi.org/10.2514/3.55704
[research_burleyrr_headvl_1974]: https://ntrs.nasa.gov/citations/19740007352
[research_burleyrr_johnsal_1974]: https://ntrs.nasa.gov/citations/19740007353
[research_burleyrr_samanichne_1970]: https://ntrs.nasa.gov/citations/19700016380
[research_burnsidejathanj_2012]: https://ntrs.nasa.gov/citations/20120014403
[research_burr_paulson_2021]: https://doi.org/10.2514/6.2021-3682
[research_burrows_2008]: https://doi.org/10.21236/ada492443
[research_burrowsdalel_newmanerneste_1954]: https://ntrs.nasa.gov/citations/19930093747
[research_bursey_dickinson_1990]: https://doi.org/10.2514/6.1990-1906
[research_burst_transmission_1966]: https://ntrs.nasa.gov/citations/19660016285
[research_burt_hillsamer_1964]: https://doi.org/10.21236/ad0355573
[research_burton_loth_2007]: https://doi.org/10.2514/6.2007-5841
[research_burtr_1981]: https://ntrs.nasa.gov/citations/19810018587
[research_burtr_1982]: https://ntrs.nasa.gov/citations/19820017232
[research_burtrw_hamnc_1972]: https://ntrs.nasa.gov/citations/19720000089
[research_butmans_savageje_1971]: https://ntrs.nasa.gov/citations/19710054391
[research_butmans_timoru_1971]: https://ntrs.nasa.gov/citations/19710040618
[research_butmans_timoru_1971_b]: https://ntrs.nasa.gov/citations/19710054411
[research_butmans_timoru_1973]: https://ntrs.nasa.gov/citations/19730007394
[research_buttadam_poppchristopherg_2010]: https://ntrs.nasa.gov/citations/20100034921
[research_buzuluk_plokhikh_2020]: https://doi.org/10.48023/2411-7943_2020_8_3_4_25
[research_c_vinaykumar_2024]: https://doi.org/10.4271/2024-26-0434
[research_cabrera_zouhri_2026]: https://doi.org/10.1016/j.procir.2026.01.190
[research_calderonm_2000]: https://ntrs.nasa.gov/citations/20000093959
[research_calhoon_kors_1973]: https://doi.org/10.2514/6.1973-1242
[research_calhoun_2000]: https://doi.org/10.2514/6.2000-1046
[research_calise_tandon_2000]: https://doi.org/10.2514/6.2000-4261
[research_callsen_herberhold_2026]: https://doi.org/10.21203/rs.3.rs-9353704/v1
[research_camachosanchez_loritediez_2025]: https://doi.org/10.1063/5.0275586
[research_camachosanchez_loritediez_2026]: https://doi.org/10.1016/j.jfluidstructs.2026.104560
[research_camargo]: https://doi.org/10.11606/003128508
[research_campbell_1962]: https://doi.org/10.21236/ad0292258
[research_campbell_1970]: https://doi.org/10.2514/6.1970-1385
[research_campbell_2020]: https://doi.org/10.1201/9780429470622-3
[research_campbell_riccio_1995]: https://doi.org/10.2514/6.1995-2399
[research_campbellrl_1965]: https://ntrs.nasa.gov/citations/19650025373
[research_candler_2001]: https://doi.org/10.21236/ada394241
[research_candler_kelley_1999]: https://doi.org/10.2514/6.1999-418
[research_canfillw_nieberdingwc_1967]: https://ntrs.nasa.gov/citations/19680002399
[research_cannon_norman_1988]: https://doi.org/10.2514/6.1988-3242
[research_cao_2012]: https://doi.org/10.4028/www.scientific.net/amr.591-593.1260
[research_cao_zhang_2024]: https://doi.org/10.1016/j.measurement.2024.115153
[research_caogen_hongjun_2008]: https://doi.org/10.1016/j.actaastro.2007.12.059
[research_caplin]: https://doi.org/10.1109/dasc.2002.1052960
[research_carey_1967]: https://doi.org/10.2514/6.1967-506
[research_carlc_1967]: https://ntrs.nasa.gov/citations/19670058729
[research_carlsonjohnr_1996]: https://ntrs.nasa.gov/citations/19960028557
[research_carpenter_jeffus_1962]: https://doi.org/10.21236/ad0291654
[research_carpenter_jeffus_1963]: https://doi.org/10.21236/ad0296857
[research_carpenterjrussell_bauerfrankh_2001]: https://ntrs.nasa.gov/citations/20010069746
[research_carperrichardd_1988]: https://ntrs.nasa.gov/citations/19880057810
[research_carperrichardd_stallingswilliamhiii_1990]: https://ntrs.nasa.gov/citations/19910027760
[research_carratu_gallo_2025]: https://doi.org/10.1109/ojim.2025.3643040
[research_carrawayprestoniiii_1988]: https://ntrs.nasa.gov/citations/19880064690
[research_carrenova_1982]: https://ntrs.nasa.gov/citations/19820052746
[research_carrenova_1985]: https://ntrs.nasa.gov/citations/19850000039
[research_carrenovictora_1986]: https://ntrs.nasa.gov/citations/19870007430
[research_carroll_1970]: https://doi.org/10.2514/6.1970-1010
[research_carroll_cox_1983]: https://doi.org/10.2514/6.1983-1149
[research_cartadg_1963]: https://ntrs.nasa.gov/citations/19630020632
[research_carter_2009]: https://doi.org/10.1121/1.3182965
[research_carterrr_masseyga_1967]: https://ntrs.nasa.gov/citations/19680007583
[research_case]: https://doi.org/10.15368/theses.2010.86
[research_case_studies_2006]: https://doi.org/10.1017/cbo9780511755538.013
[research_casey_1995]: https://doi.org/10.2514/6.1995-2410
[research_cassadyleonardd_rayerics_2013]: https://ntrs.nasa.gov/citations/20130011529
[research_cassantojm_eichelda_1968]: https://ntrs.nasa.gov/citations/19680040432
[research_cassell_wercinski_2019]: https://doi.org/10.2514/6.2019-2896
[research_cassellalan_wercinskipaul_2019]: https://ntrs.nasa.gov/citations/20190031937
[research_castrotriguero_saavedraflores_2014]: https://doi.org/10.1002/stc.1654
[research_cavalieri_liberatori_2023]: https://doi.org/10.2514/6.2023-2148
[research_cavenylh_kuokk_1980]: https://ntrs.nasa.gov/citations/19810031480
[research_cawley_2018]: https://doi.org/10.1177/1475921717750047
[research_celik_demirezen_2024]: https://doi.org/10.1109/access.2024.3359417
[research_celmins_1987]: https://doi.org/10.21236/ada191683
[research_cervantes_moore_2024]: https://doi.org/10.2514/1.a35732
[research_cesnik_2009]: https://doi.org/10.21236/ada547291
[research_chabukswar_mullen_2025]: https://doi.org/10.12783/shm2025/37485
[research_chai_yang_2021]: https://doi.org/10.1049/cds2.12078
[research_chalmers_1967]: https://doi.org/10.1111/j.1475-1305.1967.tb00868.x
[research_chalyy_2018]: https://doi.org/10.33955/2307-2180(5)2018.47-49
[research_chambellanre_stepkafs_1971]: https://ntrs.nasa.gov/citations/19710018652
[research_chamberlinr_1973]: https://ntrs.nasa.gov/citations/19730020003
[research_chamberlinr_samanichne_1971]: https://ntrs.nasa.gov/citations/19710020807
[research_champaigne_sumners_2007]: https://doi.org/10.1109/aero.2007.352876
[research_chandavidt_paulsonjohnw_2019]: https://ntrs.nasa.gov/citations/20200002389
[research_chandiramani_bhandari_2014]: https://doi.org/10.1109/icsip.2014.35
[research_chandler_2023]: https://doi.org/10.2514/6.2023-1664
[research_chang_1998]: https://doi.org/10.21236/ada350933
[research_chang_2000]: https://doi.org/10.21236/ada384380
[research_chang_2002]: https://doi.org/10.21236/ada408694
[research_chang_2004]: https://doi.org/10.21236/ada423869
[research_chang_2011]: https://doi.org/10.1121/1.3531811
[research_chang_markmiller_2011]: https://doi.org/10.1002/9781119994053.ch26
[research_changchenj_liaghatijramirl_2018]: https://ntrs.nasa.gov/citations/20180002501
[research_chanteur_2023]: https://doi.org/10.46620/ursigass.2023.1245.blss4737
[research_chaoshan_hua_2014]: https://doi.org/10.2174/1874129001408010348
[research_chaouat_vuillot_1992]: https://doi.org/10.2514/6.1992-3507
[research_chapmandeanr_1952]: https://ntrs.nasa.gov/citations/19930092109
[research_chapter_9_2013]: https://doi.org/10.1137/1.9781611973228.ch9
[research_charan_tibrewal_2025]: https://doi.org/10.1109/aero63441.2025.11068448
[research_charlesfj_larsonfl_1967]: https://ntrs.nasa.gov/citations/19670014333
[research_charron_campbell_1978]: https://doi.org/10.21236/ada062241
[research_chase_1979]: https://doi.org/10.2514/6.1979-894
[research_chase_mckinney_2005]: https://doi.org/10.2514/6.2005-6745
[research_chattopadhyay_2006]: https://doi.org/10.21236/ada465429
[research_chattopadhyay_seaver_2012]: https://doi.org/10.21236/ada554786
[research_chaudhari_2017]: https://doi.org/10.22214/ijraset.2017.10144
[research_chehrzad_khoramishad_2026]: https://doi.org/10.1177/14759217261455647
[research_chelner_2002]: https://doi.org/10.21236/ada405070
[research_chelner_2003]: https://doi.org/10.21236/ada412607
[research_chen_2019]: https://doi.org/10.2514/6.2019-3837
[research_chen_chen_2024]: https://doi.org/10.1109/icus61736.2024.10839926
[research_chen_du_2026]: https://doi.org/10.1016/j.cja.2026.104465
[research_chen_ma_2019]: https://doi.org/10.1109/ccdc.2019.8832410
[research_chen_ma_2019_b]: https://doi.org/10.1145/3351917.3351935
[research_chen_mu_2018]: https://doi.org/10.1117/12.2317531
[research_chen_wang_2025]: https://doi.org/10.1049/icp.2024.2923
[research_chen_wang_2025_b]: https://doi.org/10.1016/j.cja.2025.103756
[research_chen_wu_2018]: https://doi.org/10.2514/6.2018-4835
[research_chen_xing_2021]: https://doi.org/10.1109/iai53119.2021.9619428
[research_chen_yang_2013]: https://doi.org/10.2514/6.2013-4062
[research_chen_yang_2025]: https://doi.org/10.34133/space.0260
[research_chen_yuan_2026]: https://doi.org/10.3390/fluids11060144
[research_cheng_jing_2021]: https://doi.org/10.1016/j.ast.2021.106965
[research_cheng_jing_2024]: https://doi.org/10.1177/09544100241232140
[research_cheng_li_2017]: https://doi.org/10.1016/j.ast.2017.02.023
[research_chenggary_2003]: https://ntrs.nasa.gov/citations/20030093607
[research_chenowethfc_jerackirj_1970]: https://ntrs.nasa.gov/citations/19700029435
[research_chenowethfc_liebermana_1971]: https://ntrs.nasa.gov/citations/19710008029
[research_chentt_bohningod_1974]: https://ntrs.nasa.gov/citations/19740062396
[research_cheyne_key_2013]: https://doi.org/10.23919/oceans.2013.6740997
[research_chiangkwofuv_mcintirejeff_2017]: https://ntrs.nasa.gov/citations/20190002259
[research_chiangvincent_sunjunqiang_2011]: https://ntrs.nasa.gov/citations/20110020728
[research_chiba_kanazaki_2013]: https://doi.org/10.1299/spacee.6.15
[research_chiba_kanazaki_2014]: https://doi.org/10.1299/jamdsm.2014jamdsm0023
[research_chiba_kanazaki_2016]: https://doi.org/10.1504/ijal.2016.074912
[research_chiba_watanabe_2014]: https://doi.org/10.1299/transjsme.2014trans0287
[research_chiesa_grassi_2005]: https://doi.org/10.2514/6.2005-3346
[research_chik_cheng_2012]: https://doi.org/10.1109/apmc.2012.6421497
[research_childressthompsonrhonda_dalethomasl_2017]: https://ntrs.nasa.gov/citations/20170008098
[research_childressthompsonrhonda_thomasdale_2016]: https://ntrs.nasa.gov/citations/20170000606
[research_china_achieves_2026]: https://doi.org/10.1016/j.xinn.2026.101526
[research_chinn_dekany_1979]: https://doi.org/10.2514/6.1979-500
[research_chintm_grossrs_2003]: https://ntrs.nasa.gov/citations/20060029393
[research_chiu_1987]: https://doi.org/10.2514/6.1987-2033
[research_chiu_2010]: https://doi.org/10.21236/ada515997
[research_chiu_chang_2010]: https://doi.org/10.21236/ada536582
[research_chiu_kross_1990]: https://doi.org/10.2514/6.1990-44
[research_chivers_filmore_2024]: https://doi.org/10.25144/23151
[research_cho_kim_2004]: https://doi.org/10.1016/j.cryogenics.2004.02.009
[research_choaterl_1962]: https://ntrs.nasa.gov/citations/19620001497
[research_choi_kim_2025]: https://doi.org/10.36227/techrxiv.176704886.62692156/v1
[research_choi_lee_2015]: https://doi.org/10.6112/kscfe.2015.20.2.016
[research_choi_sweetman_2009]: https://doi.org/10.1177/1475921709341014
[research_chomputawat_chatwiriya_2019]: https://doi.org/10.4028/www.scientific.net/amm.886.182
[research_choo_mun_2018]: https://doi.org/10.6108/kspe.2018.22.2.138
[research_chowdhury_joshi_2026]: https://doi.org/10.5220/0014326200004052
[research_chrisdkarlgaard_rafaelalugo_2025]: https://ntrs.nasa.gov/citations/20250010290
[research_christensencs_1970]: https://ntrs.nasa.gov/citations/19700050122
[research_christensencs_moultrieb_1980]: https://ntrs.nasa.gov/citations/19810004704
[research_christensonrickl_nelsonmichaela_2003]: https://ntrs.nasa.gov/citations/20030065841
[research_christensonrl_komardr_1998]: https://ntrs.nasa.gov/citations/19980218686
[research_christopherdkarlgaard_rafaelalugo]: https://ntrs.nasa.gov/citations/20250007036
[research_christopherdkarlgaard_rafaellugo]: https://ntrs.nasa.gov/citations/20250008015
[research_christopherdkarlgaard_rohangdeshmukh]: https://ntrs.nasa.gov/citations/20230017083
[research_chronister_palazotto_2006]: https://doi.org/10.1115/imece2006-16280
[research_chua_kumar_2025]: https://doi.org/10.2514/6.2025-2806
[research_chun_1983]: https://doi.org/10.1016/0273-1177(83)90244-2
[research_chung_2006]: https://doi.org/10.1049/el:20061169
[research_chungjn_tullylandon_2006]: https://ntrs.nasa.gov/citations/20060047646
[research_chunovkina_2000]: https://doi.org/10.1007/bf02503592
[research_cianci_corallo_2024]: https://doi.org/10.52202/078367-0082
[research_cikanek_1986]: https://doi.org/10.23919/acc.1986.4789241
[research_cikanekhaiii_1986]: https://ntrs.nasa.gov/citations/19870026179
[research_cikanekhajr_mcgowenjjiii_1969]: https://ntrs.nasa.gov/citations/19700002358
[research_cipolledj_1980]: https://ntrs.nasa.gov/citations/19800021872
[research_citriniti_citriniti_1997]: https://doi.org/10.2514/6.1997-1810
[research_civek_ozgoren_2017]: https://doi.org/10.2514/6.2017-5333
[research_clancy_2000]: https://doi.org/10.2514/6.2000-5329
[research_clarkdh_tenenbaumdm_1967]: https://ntrs.nasa.gov/citations/19670055200
[research_clarke_khayat_1972]: https://doi.org/10.1177/002029407200500401
[research_clarker_shaned_1982]: https://ntrs.nasa.gov/citations/19820015371
[research_clarkjs_graberej_1970]: https://ntrs.nasa.gov/citations/19700032858
[research_clarkjs_liebermana_1972]: https://ntrs.nasa.gov/citations/19720008242
[research_clayton_1999]: https://doi.org/10.2514/6.1999-2791
[research_claytonjlouie_2001]: https://ntrs.nasa.gov/citations/20020050391
[research_claytonjlouie_2012]: https://ntrs.nasa.gov/citations/20120014532
[research_claytonjlouie_2017]: https://ntrs.nasa.gov/citations/20170005378
[research_claytonjlouie_2017_b]: https://ntrs.nasa.gov/citations/20170004465
[research_claytonrm_gerbrachtfg_1967]: https://ntrs.nasa.gov/citations/19670017903
[research_clerdaniell_masonmaryl_1993]: https://ntrs.nasa.gov/citations/19930057048
[research_clubbjj_1971]: https://ntrs.nasa.gov/citations/19710019847
[research_coakley]: https://doi.org/10.15368/theses.2011.26
[research_cobleighbrentr_1998]: https://ntrs.nasa.gov/citations/19980055123
[research_codag_sounding_1999]: https://doi.org/10.1108/aeat.1999.12771cab.006
[research_codead_1975]: https://ntrs.nasa.gov/citations/19750025069
[research_cohenha_shermanc_1979]: https://ntrs.nasa.gov/citations/19790015838
[research_cohenrobertj_1951]: https://ntrs.nasa.gov/citations/19930086608
[research_cohn_1997]: https://doi.org/10.1117/12.274355
[research_coirier_stutts_2014]: https://doi.org/10.2514/6.2014-2987
[research_colehenryajr_abramovitzmarvin_1952]: https://ntrs.nasa.gov/citations/19930087033
[research_colicci_noonan_2025]: https://doi.org/10.2514/6.2025-0113
[research_collamorefrankn_1989]: https://ntrs.nasa.gov/citations/19890016837
[research_collinsaaron_dominycarol_1989]: https://ntrs.nasa.gov/citations/19900041849
[research_collinsaarons_1989]: https://ntrs.nasa.gov/citations/19910016604
[research_combustion_instability_1995]: https://doi.org/10.2514/5.9781600866371.0475.0502
[research_comptonhr_blanchardrc_1979]: https://ntrs.nasa.gov/citations/19790035613
[research_comptonhr_findlayjt_1981]: https://ntrs.nasa.gov/citations/19820030367
[research_conference_on_1967]: https://ntrs.nasa.gov/citations/19670018072
[research_conley_lee_2003]: https://doi.org/10.1016/s0094-5765(03)80019-x
[research_connelledwardb_howelldavidr_1987]: https://ntrs.nasa.gov/citations/19880046440
[research_conners_sims_1998]: https://doi.org/10.2514/6.1998-3872
[research_connolly_1965]: https://doi.org/10.21236/ad0467829
[research_coogan_2015]: https://doi.org/10.2514/6.2015-3762
[research_cook_1979]: https://doi.org/10.1121/1.383453
[research_cook_1995]: https://doi.org/10.2514/6.1995-6153
[research_cook_1996]: https://doi.org/10.2514/6.1996-4563
[research_cook_gruet_2003]: https://doi.org/10.2514/6.2003-280
[research_cook_walters_1997]: https://doi.org/10.2514/6.1997-2996
[research_cookjerry_lylesgarry_2017]: https://ntrs.nasa.gov/citations/20170012323
[research_coppotelli_marzocca_2005]: https://doi.org/10.2514/6.2005-2227
[research_corban_johnson_2001]: https://doi.org/10.2514/6.2001-4381
[research_cordes_hertzfeld_1997]: https://doi.org/10.1016/s0265-9646(97)00006-4
[research_cortopassiac_martinht_2012]: https://ntrs.nasa.gov/citations/20120015334
[research_cortrightedgarmjr_schroederalberth_1951]: https://ntrs.nasa.gov/citations/19930086724
[research_cosens_newton_1988]: https://doi.org/10.2514/6.1988-3309
[research_costa_parente_2024]: https://doi.org/10.1016/j.neucom.2024.127377
[research_costello_agarwalla_2000]: https://doi.org/10.2514/6.2000-4197
[research_costello_agarwalla_2001]: https://doi.org/10.21236/ada394484
[research_costello_costello_1997]: https://doi.org/10.2514/6.1997-3724
[research_cotece_1966]: https://ntrs.nasa.gov/citations/19660010469
[research_cotece_cresseyjr_1967]: https://ntrs.nasa.gov/citations/19670000175
[research_cowling_2011]: https://doi.org/10.2514/6.2011-2370
[research_cox_harris_2003]: https://doi.org/10.1023/b:mete.0000008439.82231.ad
[research_coxfb_keipertfa_1968]: https://ntrs.nasa.gov/citations/19680000336
[research_coxjr_1987]: https://doi.org/10.2514/6.1987-2040
[research_coxjr_1988]: https://doi.org/10.2514/6.1988-3135
[research_crabtree_1962]: https://doi.org/10.21236/ad0273836
[research_craigka_1966]: https://ntrs.nasa.gov/citations/19660000650
[research_cramerkelliott_2016]: https://ntrs.nasa.gov/citations/20160012012
[research_cramerrl_granttl_1971]: https://ntrs.nasa.gov/citations/19710020370
[research_crawfordkevin_huberharold_1999]: https://ntrs.nasa.gov/citations/19990088407
[research_crawfordkevin_pinkletondavid_1998]: https://ntrs.nasa.gov/citations/19990103147
[research_crawfordkevin_pinkletondavid_1999]: https://ntrs.nasa.gov/citations/19990102616
[research_crawfordwl_reynoldsdr_1969]: https://ntrs.nasa.gov/citations/19700059383
[research_creechdennism_threetgradyejr_2010]: https://ntrs.nasa.gov/citations/20100040512
[research_crevelingcj_1964]: https://ntrs.nasa.gov/citations/19650022522
[research_crevelingcj_1965]: https://ntrs.nasa.gov/citations/19660034294
[research_crevelingcj_1966]: https://ntrs.nasa.gov/citations/19660024681
[research_crevelingcj_1967]: https://ntrs.nasa.gov/citations/19670018083
[research_cristaldi_faifer_2007]: https://doi.org/10.1109/amuem.2007.4362586
[research_cristaldi_ferrero_2018]: https://doi.org/10.1109/i2mtc.2018.8409739
[research_crockermj_potterrc_1966]: https://ntrs.nasa.gov/citations/19660030602
[research_crook_tarrant_1998]: https://doi.org/10.2514/6.1998-5146
[research_crosswy_kalb_1967]: https://doi.org/10.21236/ad0823181
[research_crosswyfl_hornkohljo_1973]: https://ntrs.nasa.gov/citations/19730060017
[research_crowe_1967]: https://doi.org/10.2514/3.4119
[research_crowe_babcock_1968]: https://doi.org/10.21236/ad0850098
[research_crowleytim_1999]: https://ntrs.nasa.gov/citations/19990115021
[research_cruickshank_1984]: https://doi.org/10.21236/ada146247
[research_crutcherhl_guttmannb_1969]: https://ntrs.nasa.gov/citations/19690010539
[research_cullenre_raglandkw_1967]: https://ntrs.nasa.gov/citations/19670052698
[research_culver_rochow_1993]: https://doi.org/10.2514/6.1993-1812
[research_cummings_divine_2006]: https://doi.org/10.2514/6.2006-668
[research_cusick_kontis_2019]: https://doi.org/10.2514/6.2019-2929
[research_czarcinskiea_feinbergpm_1970]: https://ntrs.nasa.gov/citations/19710015148
[research_czarcinskiea_maxwellms_1965]: https://ntrs.nasa.gov/citations/19660051273
[research_d_b_2022]: https://doi.org/10.1016/j.flowmeasinst.2021.102105
[research_d_m_2023]: https://doi.org/10.1016/j.flowmeasinst.2023.102371
[research_dabrowski_pelzner_2020]: https://doi.org/10.1016/j.actaastro.2020.07.016
[research_dagostinomark_leeyoungc_2001]: https://ntrs.nasa.gov/citations/20010046959
[research_dahan_morgans_2012]: https://doi.org/10.1017/jfm.2012.246
[research_dahlke_pettis_1970]: https://doi.org/10.21236/ad0873340
[research_dai_liu_2017]: https://doi.org/10.23919/chicc.2017.8027911
[research_dai_xiao_2026]: https://doi.org/10.1088/1361-6501/ae6c50
[research_dakka_dennison_2021]: https://doi.org/10.15394/ijaaa.2021.1601
[research_daleamackall_robertsakahara_1998]: https://ntrs.nasa.gov/citations/19980236873
[research_dallederekj_rogersstuarte_2015]: https://ntrs.nasa.gov/citations/20160014674
[research_dallederekj_rogersstuarte_2016]: https://ntrs.nasa.gov/citations/20160004986
[research_dallederekj_rogersstuarte_2018]: https://ntrs.nasa.gov/citations/20190025219
[research_daltonjohnt_1989]: https://ntrs.nasa.gov/citations/19900041809
[research_daly]: https://doi.org/10.1109/acssc.2003.1292213
[research_damane_pitot_2024]: https://doi.org/10.2514/6.2024-1400
[research_damico_2000]: https://doi.org/10.21236/ada384784
[research_dandorney]: https://ntrs.nasa.gov/citations/20220002635
[research_daniel_ramusat_2005]: https://doi.org/10.2514/6.2005-6618
[research_daniel_tumino_2004]: https://doi.org/10.2514/6.2004-5825
[research_danielckammer_paulblelloch]: https://ntrs.nasa.gov/citations/20205010793
[research_danielepaxson_kenjimiki]: https://ntrs.nasa.gov/citations/20220006164
[research_daniels_1970]: https://doi.org/10.21236/ad0705986
[research_dankanichjohn_aaneslandane_2015]: https://ntrs.nasa.gov/citations/20150002944
[research_dannenbergre_katzmanh_1969]: https://ntrs.nasa.gov/citations/19690051572
[research_dantona_2004]: https://doi.org/10.1109/tim.2004.823650
[research_darbyvicker_2026]: https://ntrs.nasa.gov/citations/20260008061
[research_darrenctinker_2021]: https://ntrs.nasa.gov/citations/20210000596
[research_darwell_leeming_1965]: https://doi.org/10.2514/6.1965-161
[research_dasindus_khavaranabbas_1996]: https://ntrs.nasa.gov/citations/19970019708
[research_dasis_dosanjhds_1991]: https://ntrs.nasa.gov/citations/19910055203
[research_data_acquisition_1998]: https://ntrs.nasa.gov/citations/19990116348
[research_data_centric_structural_2023]: https://doi.org/10.1515/9783110791426
[research_datnowb_fryertb_1969]: https://ntrs.nasa.gov/citations/19690053055
[research_dave_murty_2011]: https://doi.org/10.1061/41165(397)266
[research_davidchan_patrickshea]: https://ntrs.nasa.gov/citations/20220017796
[research_daviddoelling_conorhaney]: https://ntrs.nasa.gov/citations/20200003521
[research_davidfriedlander_michaelbozeman]: https://ntrs.nasa.gov/citations/20230005954
[research_davidian_1987]: https://doi.org/10.2514/6.1987-2071
[research_davidiankennethj_1987]: https://ntrs.nasa.gov/citations/19870011082
[research_davidiankennetho_kacynskikennethj_1993]: https://ntrs.nasa.gov/citations/19930006382
[research_davidjfriedlander_michaeldbozeman_2023]: https://ntrs.nasa.gov/citations/20230010010
[research_davidmdriver_danielphilippidis_2018]: https://ntrs.nasa.gov/citations/20180007695
[research_davidosigthorsson_2006]: https://doi.org/10.1109/med.2006.235983
[research_davis_1996]: https://doi.org/10.2514/6.1996-3112
[research_davis_denison]: https://doi.org/10.1109/icsens.2004.1426160
[research_davis_spicer_1965]: https://doi.org/10.2514/6.1965-1425
[research_davisjr_1988]: https://doi.org/10.2514/6.1988-4734
[research_davisoncraigr_strappjwalter_2016]: https://ntrs.nasa.gov/citations/20170000240
[research_davisws_eudellah_1993]: https://ntrs.nasa.gov/citations/19930015508
[research_davydov_sazonov_2009]: https://doi.org/10.1134/s0010952509050098
[research_dawsonct_schmittnm_1971]: https://ntrs.nasa.gov/citations/19710055773
[research_dayjohnc_1995]: https://ntrs.nasa.gov/citations/20210001200
[research_deangelisvm_tangmh_1969]: https://ntrs.nasa.gov/citations/19710005026
[research_debiasi_2012]: https://doi.org/10.2514/6.2012-2909
[research_debiasi_yan_2010]: https://doi.org/10.2514/6.2010-4244
[research_debnath_nareshreddy_2025]: https://doi.org/10.52202/080565-0013
[research_deboogj_fryertb_1965]: https://ntrs.nasa.gov/citations/19660046505
[research_deckerarthurj_2004]: https://ntrs.nasa.gov/citations/20040040078
[research_defilippis_cappuccio_2025]: https://doi.org/10.5194/egusphere-egu24-17407
[research_deford_craig]: https://doi.org/10.1109/pac.1989.73388
[research_deforrestlloyd_saadatfarzad_2016]: https://ntrs.nasa.gov/citations/20190026926
[research_degelsmith_freaner_1993]: https://doi.org/10.2514/6.1993-2419
[research_delcher_nemeth_1993]: https://doi.org/10.2514/6.1993-2377
[research_deleeuw_brennan_2009]: https://doi.org/10.1243/09544100jaero392
[research_delmonacomonteiro_machiaverni_2018]: https://doi.org/10.1007/s40430-018-1012-0
[research_delmontej_1967]: https://ntrs.nasa.gov/citations/19670046091
[research_delvaillejp_1981]: https://ntrs.nasa.gov/citations/19810023176
[research_demaslj_kinsleyrl_1971]: https://ntrs.nasa.gov/citations/19710045811
[research_dembrowdw_jamiesonlb_1964]: https://ntrs.nasa.gov/citations/19640013420
[research_demendonca_sobral_1969]: https://doi.org/10.1029/rs004i009p00741
[research_demerdziev_cundevablajer_2023]: https://doi.org/10.21014/actaimeko.v12i3.1462
[research_demerdziev_dimchev_2023]: https://doi.org/10.21014/actaimeko.v12i3.1463
[research_demidovich_2017]: https://doi.org/10.1109/icnsurv.2017.8012003
[research_demingzhang_guiqingchen]: https://doi.org/10.1109/isscaa.2006.1627654
[research_demisthomas_caitrinduffydeno]: https://ntrs.nasa.gov/citations/20240016460
[research_demisthomas_caitrinduffydeno_2025]: https://ntrs.nasa.gov/citations/20250008974
[research_demspmerol_valencialisam_2004]: https://ntrs.nasa.gov/citations/20130011313
[research_deng_ompusunggu_2025]: https://doi.org/10.3390/aerospace12030266
[research_deng_wang_2019]: https://doi.org/10.1063/1.5086907
[research_deng_xu_2022]: https://doi.org/10.1109/isoirs57349.2022.00029
[research_denguirrekik_mauris_2005]: https://doi.org/10.1109/amuem.2005.1594598
[research_dennis_hernandez_2010]: https://doi.org/10.2514/6.2010-183
[research_dennist_mchughd_1970]: https://ntrs.nasa.gov/citations/19700064116
[research_depardon_2026]: https://doi.org/10.21741/9781644904251-94
[research_derkiureghian_2001]: https://doi.org/10.1016/s0951-8320(01)00084-9
[research_derriso_mccurry_2016]: https://doi.org/10.1016/b978-0-08-100148-6.00002-0
[research_desaiprasun_schofieldjohnt_2003]: https://ntrs.nasa.gov/citations/20040085794
[research_desaiprasunn_quallsgarryd_2005]: https://ntrs.nasa.gov/citations/20050217463
[research_design_and_flow_2014]: https://doi.org/10.15623/ijret.2014.0311019
[research_design_of_1992]: https://doi.org/10.2514/5.9781600866197.0219.0283
[research_desimio_miller]: https://doi.org/10.1109/aero.2003.1234153
[research_desimone_ciampa_2017]: https://doi.org/10.12783/shm2017/14105
[research_desjardinsr_wentzlhjr_1965]: https://ntrs.nasa.gov/citations/19660016992
[research_despeyroux_desaulnier_2014]: https://doi.org/10.2514/6.2014-3285
[research_despirito_2012]: https://doi.org/10.2514/6.2012-2907
[research_despirito_2013]: https://doi.org/10.21236/ada592880
[research_despirito_sahu_2001]: https://doi.org/10.2514/6.2001-257
[research_determining_aliasing_2009]: https://ntrs.nasa.gov/citations/20090016110
[research_determining_measurement_2017]: https://doi.org/10.1002/9781119384502.app7
[research_dethloff_1961]: https://doi.org/10.21236/ad0258305
[research_deutschlj_1982]: https://ntrs.nasa.gov/citations/19830006057
[research_deutschlj_1983]: https://ntrs.nasa.gov/citations/19830011500
[research_devanath_beebi_2016]: https://doi.org/10.1109/icaccct.2016.7831668
[research_development_of_1998]: https://doi.org/10.1016/s0389-4304(98)90277-6
[research_devinjohnson_venkatathmanathan]: https://ntrs.nasa.gov/citations/20250011621
[research_devriesll_1971]: https://ntrs.nasa.gov/citations/19710053142
[research_dexterjohnson_joelwsills_2022]: https://ntrs.nasa.gov/citations/20210009733
[research_diamanti_soutis_2010]: https://doi.org/10.1016/j.paerosci.2010.05.001
[research_diamantkevind_pollardjamese_2010]: https://ntrs.nasa.gov/citations/20100042402
[research_diamondjohnk_1989]: https://ntrs.nasa.gov/citations/19910035070
[research_diazcarlosejr_2015]: https://ntrs.nasa.gov/citations/20150016271
[research_dicicca_hassan_2023]: https://doi.org/10.1109/metroaerospace57412.2023.10189981
[research_dicicca_marsilio_2024]: https://doi.org/10.1109/metroaerospace61015.2024.10591557
[research_diemhg_kirbyfm_1977]: https://ntrs.nasa.gov/citations/19780003139
[research_dietrich_schulze_2011]: https://doi.org/10.1007/978-3-446-42955-0_7
[research_dietrich_schulze_2011_b]: https://doi.org/10.1007/978-3-446-42955-0_9
[research_difioredossantos_lewis_2000]: https://doi.org/10.4271/2000-01-3251
[research_difrancesco_boorady_1989]: https://doi.org/10.2514/6.1989-2390
[research_dileo_liguori_2010]: https://doi.org/10.1109/imtc.2010.5488057
[research_dillo_2001]: https://doi.org/10.2514/6.2001-102
[research_dillonjr_1996]: https://doi.org/10.2514/6.1996-458
[research_dimmockjohno_2005]: https://ntrs.nasa.gov/citations/20050215338
[research_dimonaco_dantuono_2023]: https://doi.org/10.2514/6.2023-2315
[research_dincer_sezeruzol_2022]: https://doi.org/10.2514/6.2022-3387
[research_ding_yang_2020]: https://doi.org/10.1016/j.jweia.2019.104051
[research_dirix_enayati_2025]: https://doi.org/10.23919/eucap63536.2025.10999761
[research_dissanayake_karunananda_2008]: https://doi.org/10.1177/1475921708090555
[research_dissel_huseman_2012]: https://doi.org/10.2514/6.2012-5281
[research_dissel_kothari_2005]: https://doi.org/10.2514/6.2005-4369
[research_dixit_goplani_2025]: https://doi.org/10.1007/978-981-96-5366-9_15
[research_dizinno_reeves_2024]: https://doi.org/10.2514/6.2024-85236
[research_djanalmann_murugan_2025]: https://doi.org/10.2514/6.2025-2632
[research_dobrodomov_proroka_2026]: https://doi.org/10.15421/452557
[research_dol_2021]: https://doi.org/10.37394/232013.2021.16.9
[research_dombrovsky_2008]: https://doi.org/10.1615/thermopedia.000179
[research_dominycarolt_chesneyjamesr_1991]: https://ntrs.nasa.gov/citations/19920064920
[research_donahue_weldon_2008]: https://doi.org/10.2514/1.29313
[research_donaldsonhm_griffinma_1966]: https://ntrs.nasa.gov/citations/19670002361
[research_donbosco_kumar_2014]: https://doi.org/10.1063/1.4902589
[research_dong_kim_2018]: https://doi.org/10.3390/aerospace5030087
[research_dong_wu_2023]: https://doi.org/10.1049/icp.2023.3008
[research_dongare_agrawal_2024]: https://doi.org/10.2139/ssrn.4964977
[research_dongare_peetala_2023]: https://doi.org/10.21203/rs.3.rs-3725840/v1
[research_dongare_peetala_2024]: https://doi.org/10.1007/s00231-024-03473-0
[research_dongare_peetala_2025]: https://doi.org/10.1016/j.tca.2025.180053
[research_dorairajan]: https://doi.org/10.31274/td-20260812-70
[research_dorosh_leontiev_2014]: https://doi.org/10.7463/1214.0740931
[research_dorsey_myers_2000]: https://doi.org/10.2514/6.2000-1043
[research_dorsey_wu_1999]: https://doi.org/10.1063/1.57503
[research_dosanjhdarshans_dasindus_1987]: https://ntrs.nasa.gov/citations/19870008051
[research_dosanjhdarshans_dasindus_1988]: https://ntrs.nasa.gov/citations/19890028736
[research_dosanjhds_dasi_1983]: https://ntrs.nasa.gov/citations/19830050107
[research_dosanjhds_dasis_1985]: https://ntrs.nasa.gov/citations/19860012837
[research_dosanjhds_dasis_1986]: https://ntrs.nasa.gov/citations/19860060695
[research_douardstephane_1994]: https://ntrs.nasa.gov/citations/19950010823
[research_doudkin_marushko_2019]: https://doi.org/10.1109/idaacs.2019.8924252
[research_doughertynsam_liubawlin_1991]: https://ntrs.nasa.gov/citations/19910034577
[research_doyoro_chang_2022]: https://doi.org/10.2139/ssrn.4206670
[research_dragan_2010]: https://doi.org/10.2478/v10164-010-0021-y
[research_dragone_2000]: https://doi.org/10.2514/6.2000-5309
[research_drewsmichaele_formandouglasa_1998]: https://ntrs.nasa.gov/citations/19980228123
[research_driscollea_landrumdb_2004]: https://ntrs.nasa.gov/citations/20040076962
[research_drobyshev_2026]: https://doi.org/10.62717/3083-7057-2026-1-024
[research_du]: https://doi.org/10.31274/etd-180810-1029
[research_du_2017]: https://doi.org/10.26226/morressier.59c106e9d462b80292389e5d
[research_du_meng_2022]: https://doi.org/10.23919/eucap53622.2022.9768970
[research_du_wang_2017]: https://doi.org/10.1109/ccdc.2017.7979227
[research_duke_houghton_1966]: https://doi.org/10.2514/6.1966-621
[research_dukemangregorya_gallahermichaelw_1998]: https://ntrs.nasa.gov/citations/19990102412
[research_dumbacher_2002]: https://doi.org/10.2514/6.2002-3613
[research_dumbacher_klevatt_1994]: https://doi.org/10.2514/6.1994-4682
[research_dunavantjc_schersh_1966]: https://ntrs.nasa.gov/citations/19660027976
[research_duncan_ensey_1964]: https://doi.org/10.21236/ad0452106
[research_dunnmichaelg_1989]: https://ntrs.nasa.gov/citations/19910015022
[research_dunnmichaelg_1990]: https://ntrs.nasa.gov/citations/19900014089
[research_dunnstuarts_coatsdouglase_1996]: https://ntrs.nasa.gov/citations/19960029260
[research_duplessis_2026]: https://doi.org/10.21741/9781644904251-45
[research_durgesh_naughton_2004]: https://doi.org/10.2514/6.2004-904
[research_duttasoumyo_greenjustins_2019]: https://ntrs.nasa.gov/citations/20200002418
[research_dyakonovartema_buckgregorym_2009]: https://ntrs.nasa.gov/citations/20090024217
[research_dynamic_real_time_1989]: https://doi.org/10.1016/0308-9126(89)90911-5
[research_easterlingmf_spearaj_1968]: https://ntrs.nasa.gov/citations/19690041136
[research_easterlingmf_spearaj_1969]: https://ntrs.nasa.gov/citations/19690012788
[research_eastonra_hilbertee_1973]: https://ntrs.nasa.gov/citations/19730000290
[research_easwer_manideep_2023]: https://doi.org/10.1063/5.0137243
[research_eberhart_1964]: https://doi.org/10.2307/3947888
[research_eberhartcj_snellgrovelm_2015]: https://ntrs.nasa.gov/citations/20150016367
[research_eckartme_adamsjs_2012]: https://ntrs.nasa.gov/citations/20120012843
[research_eckert_oechslein_1999]: https://doi.org/10.2514/6.1999-2891
[research_edge_powers_1974]: https://doi.org/10.2514/6.1974-824
[research_edge_powers_1976]: https://doi.org/10.2514/3.61478
[research_effect_of_1959]: https://doi.org/10.1016/0043-1648(59)90190-5
[research_effingermichael_clintonrgjr_1999]: https://ntrs.nasa.gov/citations/20000027528
[research_egerev_ovchinnikov_1993]: https://doi.org/10.1016/b978-0-7506-1877-9.50198-0
[research_eggersajjr_1965]: https://ntrs.nasa.gov/citations/19660043224
[research_eggersajjr_resnikoffmeyerm_1957]: https://ntrs.nasa.gov/citations/19930092299
[research_eguia_lamikiz_2017]: https://doi.org/10.1016/j.precisioneng.2016.07.001
[research_ehrlichmann_habich_1993]: https://doi.org/10.1364/ao.32.006582
[research_eichelbergerrp_1962]: https://ntrs.nasa.gov/citations/19630018655
[research_eichelbergerrp_ratnerva_1962]: https://ntrs.nasa.gov/citations/19630020461
[research_eilers_matthew_2010]: https://doi.org/10.2514/6.2010-6964
[research_eilers_wilson_2011]: https://doi.org/10.2514/6.2011-5531
[research_eilers_wilson_2012]: https://doi.org/10.2514/1.b34381
[research_eisenberger_posner_1965]: https://doi.org/10.1080/01621459.1965.10480778
[research_eisenberger_posner_1967]: https://doi.org/10.2307/2283812
[research_ekici_savun_2026]: https://doi.org/10.1140/epjp/s13360-026-08328-7
[research_eklund_2004]: https://doi.org/10.2514/6.2004-5950
[research_elaineyijiazheng_danielcellucci]: https://ntrs.nasa.gov/citations/20205010674
[research_elainiyehia_parkjohn_2010]: https://ntrs.nasa.gov/citations/20100022029
[research_elamsk_2000]: https://ntrs.nasa.gov/citations/20000037777
[research_elanmgraupe_chrisdkarlgaard_2025]: https://ntrs.nasa.gov/citations/20250008926
[research_eldredch_gordonsv_1976]: https://ntrs.nasa.gov/citations/19760019167
[research_electroacoustic_transducer_1984]: https://doi.org/10.1016/0301-5629(84)90102-9
[research_electroacoustic_transducer_1984_b]: https://doi.org/10.1016/0301-5629(84)90185-6
[research_elenimowery_jacobstonehill]: https://ntrs.nasa.gov/citations/20250004399
[research_elghazawitareka_pritchardjim_1994]: https://ntrs.nasa.gov/citations/19950010786
[research_eliassen_1965]: https://doi.org/10.1016/b978-0-08-011074-5.50008-7
[research_elizabeth_kumar_2019]: https://doi.org/10.1007/s12647-019-00341-9
[research_ellis_kearney_1982]: https://doi.org/10.21236/adb064268
[research_ellisdavidl_2013]: https://ntrs.nasa.gov/citations/20130014444
[research_ellison_williams_2003]: https://doi.org/10.1007/978-3-662-05173-3_22
[research_ellisrr_gamblem_1972]: https://ntrs.nasa.gov/citations/19720022226
[research_elmscp_1965]: https://ntrs.nasa.gov/citations/19650014187
[research_elsaadany_wenjun_2014]: https://doi.org/10.3923/itj.2014.2658.2665
[research_elshafey_2018]: https://doi.org/10.21608/ejmtc.2018.20314
[research_elston_1963]: https://doi.org/10.21236/ad0407325
[research_elvin_1996]: https://doi.org/10.1063/1.49950
[research_emensfh_frostwo_1966]: https://ntrs.nasa.gov/citations/19670033281
[research_emozzi_sroth_1965]: https://ntrs.nasa.gov/citations/19660000943
[research_emrich_2016]: https://doi.org/10.1016/b978-0-12-804474-2.00002-3
[research_emrich_2016_b]: https://doi.org/10.1016/b978-0-12-804474-2.00003-5
[research_emrich_2016_c]: https://doi.org/10.1016/b978-0-12-804474-2.00016-3
[research_emrich_2023]: https://doi.org/10.1016/b978-0-323-90030-0.00011-4
[research_emrich_2023_b]: https://doi.org/10.1016/b978-0-323-90030-0.00001-1
[research_emrich_2023_c]: https://doi.org/10.1016/b978-0-323-90030-0.00004-7
[research_enciu_rosen_2015]: https://doi.org/10.2514/1.j053241
[research_engbergrobert_ooitengk_2004]: https://ntrs.nasa.gov/citations/20040050273
[research_engbergrobertc_2005]: https://ntrs.nasa.gov/citations/20050180716
[research_ennixkimberlya_corpeninggriffinp_1999]: https://ntrs.nasa.gov/citations/19990113121
[research_epperly_walls]: https://doi.org/10.1109/aero.2001.931176
[research_eremenko_mouton_2003]: https://doi.org/10.2514/6.2003-1269
[research_erickson_craddock_1980]: https://doi.org/10.21236/ada097735
[research_ericksongarye_2007]: https://ntrs.nasa.gov/citations/20070034019
[research_erinhubbard_franksemmelmayer]: https://ntrs.nasa.gov/citations/20220004976
[research_erline_hathaway_1999]: https://doi.org/10.21236/ada361333
[research_esdu_data_1998]: https://doi.org/10.1108/aeat.1998.12770fab.033
[research_est_nelson_1991]: https://doi.org/10.2514/6.1991-3256
[research_esterline_wright_2010]: https://doi.org/10.2514/6.2010-3538
[research_estimation_of]: https://doi.org/10.4271/air4979a
[research_estlerwtyler_1989]: https://ntrs.nasa.gov/citations/19900017555
[research_etal_2021]: https://doi.org/10.17762/turcomat.v12i10.5406
[research_etters_flurchick_1981]: https://doi.org/10.2514/6.1981-677
[research_eugeneltu_1996]: https://ntrs.nasa.gov/citations/19960047050
[research_eujene_1942]: https://ntrs.nasa.gov/citations/19930094396
[research_eulerea_adamsgl_1979]: https://ntrs.nasa.gov/citations/19800012918
[research_european_company_2015]: https://doi.org/10.1063/pt.5.028935
[research_evananzalone_mikefritzinger]: https://ntrs.nasa.gov/citations/20205006580
[research_evanchukvl_1974]: https://ntrs.nasa.gov/citations/19750039849
[research_evanjohnanzalone_gregdukeman]: https://ntrs.nasa.gov/citations/20205004519
[research_evans_chattlain_2016]: https://doi.org/10.2514/6.2016-2526
[research_evans_donati_2018]: https://doi.org/10.2514/6.2018-2613
[research_evans_martinez_2016]: https://doi.org/10.2514/6.2016-2397
[research_evans_martinez_2016_b]: https://doi.org/10.2514/6.2016-2398
[research_evans_martinez_2017]: https://doi.org/10.1007/978-3-319-51941-8_4
[research_evanssa_grosskw_1975]: https://ntrs.nasa.gov/citations/19770083458
[research_even_hagita_2011]: https://doi.org/10.1109/icassp.2011.5946316
[research_example_uncertainty]: https://doi.org/10.1117/3.1002328.ch110
[research_excelcodevelopmentsincsilvercreekny_1963]: https://doi.org/10.21236/ad0424490
[research_expendable_second_1971]: https://ntrs.nasa.gov/citations/19730006149
[research_experimental_investigation_1972]: https://ntrs.nasa.gov/citations/19720026088
[research_external_autoignition_1986]: https://doi.org/10.2514/6.1986-1578
[research_ezebili_schreve_2024]: https://doi.org/10.1088/1361-6501/ad20bf
[research_ezell_barkhoudarian_1992]: https://doi.org/10.4271/921007
[research_fabrication_of_1981]: https://ntrs.nasa.gov/citations/19820009128
[research_fainlt_cribbhe_1974]: https://ntrs.nasa.gov/citations/19740000028
[research_fairall_1967]: https://doi.org/10.2172/4255004
[research_falangaralpha_1956]: https://ntrs.nasa.gov/citations/19930089157
[research_falangaralpha_leissabraham_1956]: https://ntrs.nasa.gov/citations/19930089568
[research_falkiewicz_cesnik_2009]: https://doi.org/10.2514/6.2009-6284
[research_falkiewicz_cesnik_2010]: https://doi.org/10.2514/6.2010-7928
[research_fallonii_taylor_1999]: https://doi.org/10.2514/6.1999-1720
[research_fan_2021]: https://doi.org/10.1109/isttca53489.2021.9654651
[research_fan_yao_2026]: https://doi.org/10.1145/3828836.3828875
[research_fan_yu_2015]: https://doi.org/10.4028/www.scientific.net/amm.719-720.365
[research_fancher_1985]: https://doi.org/10.1080/00423118508968832
[research_fanciullo_lacefield_1994]: https://doi.org/10.2514/6.1994-3398
[research_fang_li_2025]: https://doi.org/10.1109/comea66280.2025.11241761
[research_fang_ma_2012]: https://doi.org/10.2991/citcs.2012.242
[research_fang_yixing_2012]: https://doi.org/10.1109/phm.2012.6228775
[research_fang_zou_2011]: https://doi.org/10.1109/phm.2011.5939471
[research_fansler_schmidt_1976]: https://doi.org/10.21236/adb012784
[research_fantinijaya_1998]: https://ntrs.nasa.gov/citations/19990004344
[research_faranosov_karabasov_2013]: https://doi.org/10.2514/6.2013-2238
[research_farmerrichard_chenggary_2001]: https://ntrs.nasa.gov/citations/20010037826
[research_farmerrichardc_chenggary_1999]: https://ntrs.nasa.gov/citations/20000027515
[research_farnham_2018]: https://doi.org/10.1109/sest.2018.8495706
[research_farokhis_vertzbergerm_1989]: https://ntrs.nasa.gov/citations/19900027291
[research_farr_wiley_2005]: https://doi.org/10.2514/6.2005-4089
[research_faulstich_law_2006]: https://doi.org/10.21236/ada619554
[research_favareghamberl_houldenheatherp_2016]: https://ntrs.nasa.gov/citations/20160007692
[research_feinbergp_maxwellm_1969]: https://ntrs.nasa.gov/citations/19690063746
[research_feinbergp_maxwellms_1970]: https://ntrs.nasa.gov/citations/19710036438
[research_feinbergpm_leskojgjr_1963]: https://ntrs.nasa.gov/citations/19640006240
[research_feinbergpm_leskojgjr_1964]: https://ntrs.nasa.gov/citations/19640016628
[research_feinbergpm_townsendmr_1968]: https://ntrs.nasa.gov/citations/19710013525
[research_fejjari_delavault_2025]: https://doi.org/10.3390/app15105653
[research_fenfen_xubo_2020]: https://doi.org/10.1109/ccdc49329.2020.9164687
[research_feng_shi_2024]: https://doi.org/10.2139/ssrn.4686135
[research_feng_sun_2014]: https://doi.org/10.1002/atr.1260
[research_fenglei_2021]: https://doi.org/10.1088/1742-6596/1827/1/012012
[research_fengli_chaowang_2016]: https://doi.org/10.1109/cgncc.2016.7829056
[research_fergusoncr_treedr_1987]: https://ntrs.nasa.gov/citations/19880031282
[research_ferlauto_ferrero_2020]: https://doi.org/10.2514/6.2020-3777
[research_ferlauto_ferrero_2020_b]: https://doi.org/10.2514/6.2020-2246
[research_fernandesvonhuelsen]: https://doi.org/10.47749/t/unicamp.2024.1455904
[research_fernandezrene_riddlebaughjeff_2018]: https://ntrs.nasa.gov/citations/20190029015
[research_ferrandon_1997]: https://doi.org/10.1016/s0265-9646(97)00008-8
[research_ferrandon_1998]: https://doi.org/10.1007/978-94-011-5030-9_31
[research_ferreirademoura_borgesribeiro_2025]: https://doi.org/10.26678/abcm.cobem2025.cob2025-1499
[research_ferrero_2025]: https://doi.org/10.1201/9781003188377-29
[research_ferrero_prioli_2015]: https://doi.org/10.1109/i2mtc.2015.7151540
[research_ferrisdj_1967]: https://ntrs.nasa.gov/citations/19670062661
[research_ferrisjc_1967]: https://ntrs.nasa.gov/citations/19670020050
[research_fichteledwardj_mcdanielamosd_1994]: https://ntrs.nasa.gov/citations/19950005583
[research_fick_schmucker_1997]: https://doi.org/10.2514/6.1997-3305
[research_ficker_1992]: https://doi.org/10.1111/j.1475-1305.1992.tb00791.x
[research_fielhauerkb_boonebg_2011]: https://ntrs.nasa.gov/citations/20120006615
[research_figueroajorge_saintcyrwilliam_2003]: https://ntrs.nasa.gov/citations/20040001397
[research_figueroajorge_stcyrwilliam_2004]: https://ntrs.nasa.gov/citations/20110016667
[research_file_s1]: https://doi.org/10.7717/peerj.8785/supp-1
[research_file_s2]: https://doi.org/10.7717/peerj.8785/supp-2
[research_file_s4]: https://doi.org/10.7717/peerj.8785/supp-4
[research_fillery_stanton_2011]: https://doi.org/10.1002/9781119971009.ch13
[research_fincannonhjames_2002]: https://ntrs.nasa.gov/citations/20020081293
[research_fincannonhjames_2003]: https://ntrs.nasa.gov/citations/20050215029
[research_fingerhj_cambrajm_1974]: https://ntrs.nasa.gov/citations/19750039829
[research_finleytom_parkerpeter_2010]: https://ntrs.nasa.gov/citations/20100033606
[research_fiorito_1964]: https://doi.org/10.2514/6.1964-260
[research_fischbachsean_2014]: https://ntrs.nasa.gov/citations/20140010456
[research_fischbachseanr_kennyrjeremy_2010]: https://ntrs.nasa.gov/citations/20110007984
[research_fisher_jr_1963]: https://doi.org/10.21236/ad0421951
[research_fisherje_lawrenceda_2002]: https://ntrs.nasa.gov/citations/20020092014
[research_fitchjefferyt_simonalanl_2012]: https://ntrs.nasa.gov/citations/20120016268
[research_fitzsimmons_1996]: https://doi.org/10.2514/6.1996-4414
[research_flagghowards_kalillouf_1987]: https://ntrs.nasa.gov/citations/19880046454
[research_flanaganpatrickm_1991]: https://ntrs.nasa.gov/citations/19910059653
[research_flavio_2020]: https://doi.org/10.32614/cran.package.actel
[research_flemingwilliama_gabrieldavids_1955]: https://ntrs.nasa.gov/citations/19930088693
[research_flight_test_2016]: https://doi.org/10.21535/dnk59q51
[research_florendo_yechout_2006]: https://doi.org/10.2514/6.2006-666
[research_florendo_yechout_2007]: https://doi.org/10.2514/1.21344
[research_floresjr_1986]: https://doi.org/10.2514/6.1986-2543
[research_flynnry_grovesjr_1964]: https://ntrs.nasa.gov/citations/19650008590
[research_fogelalvinj_1994]: https://ntrs.nasa.gov/citations/19950010787
[research_follettw_1996]: https://ntrs.nasa.gov/citations/19960029142
[research_follettw_ketchuma_1996]: https://ntrs.nasa.gov/citations/19960029263
[research_foote_2013]: https://doi.org/10.4271/2013-01-2219
[research_forester_strom_1986]: https://doi.org/10.1007/978-3-642-82770-9_15
[research_fortdavid_rogstaddavid_2003]: https://ntrs.nasa.gov/citations/20110023820
[research_fossum_bhowmik_2024]: https://doi.org/10.13182/t130-44153
[research_fosswillardejr_runckeljackf_1958]: https://ntrs.nasa.gov/citations/19930093825
[research_fosterwajr_sforzinirh_1981]: https://ntrs.nasa.gov/citations/19810056571
[research_fosterwajr_shuph_1986]: https://ntrs.nasa.gov/citations/19860057864
[research_fosterwinfredajr_crowderwinston_2014]: https://ntrs.nasa.gov/citations/20140012532
[research_fotia_kaemming_2019]: https://doi.org/10.2514/6.2019-1743
[research_fotowicz_2016]: https://doi.org/10.1007/978-3-319-29357-8_67
[research_fournier_2001]: https://doi.org/10.2514/6.2001-256
[research_fox_2025]: https://doi.org/10.71236/qpvh3815
[research_fox_2025_b]: https://doi.org/10.71236/aanr8999
[research_france_s_liquid_2006]: https://doi.org/10.2514/5.9781600868870.0785.0814
[research_francescosoranna_patricksheaney]: https://ntrs.nasa.gov/citations/20220006011
[research_francescosoranna_patricksheaney_2023]: https://ntrs.nasa.gov/citations/20220018852
[research_francescosoranna_patricksheaney_b]: https://ntrs.nasa.gov/citations/20205010281
[research_francis_thompson_1980]: https://doi.org/10.2514/6.1980-1278
[research_franciscopena_erickrossidelafuente_2025]: https://ntrs.nasa.gov/citations/20250004188
[research_frankel_vergeer_2025]: https://doi.org/10.2514/1.t7197
[research_frankel_vergeer_2025_b]: https://doi.org/10.2514/6.2025-0535
[research_franklin_tinsley_1970]: https://doi.org/10.21236/ad0867628
[research_franz_hassan_2023]: https://doi.org/10.1007/978-981-19-6282-0_1
[research_franzruss_pestanamark_2006]: https://ntrs.nasa.gov/citations/20060056090
[research_freeman_talay_1996]: https://doi.org/10.1061/40177(207)52
[research_freeman_talay_1997]: https://doi.org/10.1016/s0094-5765(97)00197-5
[research_freemandelmacjr_talaytheodorea_1996]: https://ntrs.nasa.gov/citations/19960053992
[research_french_1987]: https://doi.org/10.4271/871336
[research_french_2010]: https://doi.org/10.1002/9780470686652.eae417
[research_fresconi_2011]: https://doi.org/10.21236/ada539868
[research_fresconi_harkins_2011]: https://doi.org/10.2514/6.2011-6268
[research_friedland_1965]: https://doi.org/10.2514/6.1965-533
[research_friedman_hines_1967]: https://doi.org/10.21236/ad0816546
[research_friedmanmorrisd_1951]: https://ntrs.nasa.gov/citations/19930093733
[research_friesj_1973]: https://ntrs.nasa.gov/citations/19740003571
[research_froningjr_1996]: https://doi.org/10.2514/6.1996-3178
[research_frostwo_1962]: https://ntrs.nasa.gov/citations/19630015405
[research_frostwo_1970]: https://ntrs.nasa.gov/citations/19700041319
[research_frostwo_ellisdh_1971]: https://ntrs.nasa.gov/citations/19720028737
[research_frostwo_norvellde_1966]: https://ntrs.nasa.gov/citations/19670033271
[research_frostwo_simpsonrs_1969]: https://ntrs.nasa.gov/citations/19690043810
[research_fruboesejoachim_1987]: https://ntrs.nasa.gov/citations/19870019125
[research_fryertb_1966]: https://ntrs.nasa.gov/citations/19660000622
[research_fryertb_1968]: https://ntrs.nasa.gov/citations/19680000065
[research_fryertb_1974]: https://ntrs.nasa.gov/citations/19760047272
[research_fryertb_corbinsd_1978]: https://ntrs.nasa.gov/citations/19790057387
[research_fryertb_lundgf_1978]: https://ntrs.nasa.gov/citations/19790057411
[research_fryertb_mccutcheonep_1977]: https://ntrs.nasa.gov/citations/19770000288
[research_fryertb_sandlerh_1972]: https://ntrs.nasa.gov/citations/19730029481
[research_fryertb_sandlerh_1975]: https://ntrs.nasa.gov/citations/19750058695
[research_fu_lam_2025]: https://doi.org/10.2139/ssrn.5990145
[research_fu_wang_2019]: https://doi.org/10.1109/access.2019.2947297
[research_fuchs_haskell_2018]: https://doi.org/10.2514/6.2018-0084
[research_fuertes_pilastre_2018]: https://doi.org/10.2514/6.2018-2559
[research_fuhrmann_dreyer_2008]: https://doi.org/10.1007/s12217-008-9017-4
[research_fujimoto_fujii_2003]: https://doi.org/10.1115/fedsm2003-45427
[research_fukushima_2011]: https://doi.org/10.5772/23759
[research_fuller_1973]: https://doi.org/10.2514/6.1973-1179
[research_fullerde_1968]: https://ntrs.nasa.gov/citations/19680027037
[research_fundamentals_of_2026]: https://doi.org/10.1002/9781394438303.ch2
[research_furstenau_1965]: https://doi.org/10.2514/6.1965-272
[research_furuichi_terao_2015]: https://doi.org/10.1016/j.flowmeasinst.2015.10.007
[research_fuzzy_variables]: https://doi.org/10.1007/978-0-387-46328-5_2
[research_gabriel_helms_1970]: https://doi.org/10.2514/6.1970-711
[research_gabrisea_hansenqm_1970]: https://ntrs.nasa.gov/citations/19700052306
[research_gaddisstephenw_hudsonsusant_1992]: https://ntrs.nasa.gov/citations/19930035475
[research_gage_vanderkam_2003]: https://doi.org/10.2514/6.2003-1330
[research_gagemark_dehoffronald_1991]: https://ntrs.nasa.gov/citations/19910016891
[research_gai_sharma_1981]: https://doi.org/10.1017/s0001924000029742
[research_gaitonde_samimy_2010]: https://doi.org/10.2514/6.2010-4416
[research_galangafl_muellertj_1976]: https://ntrs.nasa.gov/citations/19760050025
[research_galbraith_hayward]: https://doi.org/10.1109/ultsym.1996.584142
[research_gale_moedt_1962]: https://doi.org/10.21236/ad0295670
[research_galeazzim_colliermr_2012]: https://ntrs.nasa.gov/citations/20120011916
[research_gallagherjamesj_1948]: https://ntrs.nasa.gov/citations/20050028503
[research_galli]: https://doi.org/10.70675/97c77627zc51bz4cb0za02bzf5547129624d
[research_galway_1980]: https://doi.org/10.21236/ada090484
[research_ganesan_subburayan_2025]: https://doi.org/10.3390/engproc2025093029
[research_gangeh_bui_2023]: https://doi.org/10.2514/6.2023-72230
[research_gao_dai_2016]: https://doi.org/10.1155/2016/3846804
[research_gao_sun_2009]: https://doi.org/10.1049/iet-smt.2008.0155
[research_gao_zhang_2013]: https://doi.org/10.4028/www.scientific.net/amr.760-762.1062
[research_gao_zhang_2025]: https://doi.org/10.1109/tim.2025.3555728
[research_garanin_glagolev_2002]: https://doi.org/10.1023/a:1015822703200
[research_garbefftheodorejii_2019]: https://ntrs.nasa.gov/citations/20190002270
[research_garcia_silveira_2015]: https://doi.org/10.4271/2015-36-0160
[research_gardinier_taylor_1999]: https://doi.org/10.2514/6.1999-1757
[research_gardner_agarwal_2019]: https://doi.org/10.1063/1.5119605
[research_gardner_bull_2022]: https://doi.org/10.12783/shm2021/36243
[research_garg_dodiyal_2009]: https://doi.org/10.1109/aero.2009.4839389
[research_garg_schiefer_2017]: https://doi.org/10.1016/j.measurement.2017.07.031
[research_garmiregp_1974]: https://ntrs.nasa.gov/citations/19740027132
[research_gath_well_2000]: https://doi.org/10.2514/6.2000-4589
[research_gatzec_1976]: https://ntrs.nasa.gov/citations/19760020176
[research_gatzec_1977]: https://ntrs.nasa.gov/citations/19780016220
[research_gatzec_1979]: https://ntrs.nasa.gov/citations/19790010876
[research_gellmandavidi_biggarstuartf_1991]: https://ntrs.nasa.gov/citations/19930039595
[research_gengegaryg_marshmattheww_1999]: https://ntrs.nasa.gov/citations/20000010462
[research_georgewilliamk_raewilliamj_1991]: https://ntrs.nasa.gov/citations/19910051828
[research_georgewv_1967]: https://ntrs.nasa.gov/citations/19670000402
[research_gerlach_sanli_2017]: https://doi.org/10.5162/sensor2017/d4.2
[research_gertsbakh_2003]: https://doi.org/10.1007/978-3-662-08583-7_5
[research_ghaffarianbenny_majumdaralokk_1992]: https://ntrs.nasa.gov/citations/19920046998
[research_ghosh_gunasekaran_2021]: https://doi.org/10.2514/6.2021-2489
[research_ghosh_singhal_2008]: https://doi.org/10.2514/6.2008-6882
[research_ghoshal_ayers_2012]: https://doi.org/10.1115/smasis2012-8151
[research_giacconir_gorensteinp_1967]: https://ntrs.nasa.gov/citations/19670022531
[research_gibart]: https://doi.org/10.70675/a3daf536z34f7z4ce1zab60z57865f27ae3b
[research_gibart_pietlahanier_2024]: https://doi.org/10.23919/acc60939.2024.10644942
[research_gibson_1985]: https://doi.org/10.2514/6.1985-1324
[research_gibsonloreleis_sealeybradleys_1993]: https://ntrs.nasa.gov/citations/19930070408
[research_gieltvjr_muellertj_1975]: https://ntrs.nasa.gov/citations/19750049896
[research_gieras_gorgeri_2021]: https://doi.org/10.1016/j.jppr.2021.03.001
[research_giglio_manes_2013]: https://doi.org/10.1533/9780857096487.2.220
[research_gilchriestc_goldsteinr_1970]: https://ntrs.nasa.gov/citations/19700000008
[research_gilderjr_gillmorewfjr_1970]: https://ntrs.nasa.gov/citations/19700050123
[research_giles_whitford_1980]: https://doi.org/10.1109/taes.1980.308898
[research_gillespiewarrenjr_1957]: https://ntrs.nasa.gov/citations/19930089506
[research_gillespiewarrenjr_1960]: https://ntrs.nasa.gov/citations/20040046997
[research_gillespiewjr_1956]: https://ntrs.nasa.gov/citations/19690093428
[research_gilleygc_1975]: https://ntrs.nasa.gov/citations/19740000296
[research_gilson_a_2023]: https://doi.org/10.1109/iccc57789.2023.10165455
[research_giridharanmg_leejg_1992]: https://ntrs.nasa.gov/citations/19920071533
[research_girouardforrestr_hopkinsallen_1993]: https://ntrs.nasa.gov/citations/19930072382
[research_giurgiutiu_2003]: https://doi.org/10.1115/imece2003-43552
[research_giurgiutiu_2015]: https://doi.org/10.1016/b978-0-85709-523-7.00016-5
[research_giurgiutiu_2016]: https://doi.org/10.1016/b978-0-12-409605-9.00009-x
[research_giurgiutiu_2016_b]: https://doi.org/10.1016/b978-0-12-409605-9.00004-0
[research_giurgiutiu_2020]: https://doi.org/10.1016/b978-0-08-102679-3.00017-4
[research_giurgiutiu_2022]: https://doi.org/10.1016/b978-0-12-813308-8.00010-7
[research_giurgiutiu_lin_2004]: https://doi.org/10.1115/imece2004-60929
[research_giurgiutiu_soutis_2010]: https://doi.org/10.1002/9780470686652.eae187
[research_giurgiutiu_zagrai_2005]: https://doi.org/10.1177/1475921705049752
[research_glaabja_1985]: https://ntrs.nasa.gov/citations/19860009390
[research_glagolev_zubkov_2000]: https://doi.org/10.1007/bf02699473
[research_glaser]: https://doi.org/10.70675/f1ce8de3z843fz413bzb76czffc77f6b5ce9
[research_glassburnrobins_smithsuzanneweaver_1994]: https://ntrs.nasa.gov/citations/19950007675
[research_glatt_1961]: https://doi.org/10.21236/ad0262056
[research_glennabever_1981]: https://ntrs.nasa.gov/citations/19820030411
[research_glennabever_1984]: https://ntrs.nasa.gov/citations/19840012453
[research_glennabever_1986]: https://ntrs.nasa.gov/citations/19860000323
[research_glennabever_1991]: https://ntrs.nasa.gov/citations/19910011822
[research_glennabever_1991_b]: https://ntrs.nasa.gov/citations/19910017118
[research_glinesa_lazzaroja_1970]: https://ntrs.nasa.gov/citations/19710030221
[research_gloger_lettieri_2021]: https://doi.org/10.1115/1.0003139v
[research_glossbb_sewallwg_1983]: https://ntrs.nasa.gov/citations/19830035469
[research_glozmanvladimir_brillhartralphd_1990]: https://ntrs.nasa.gov/citations/19910009831
[research_gnoffopetera_braunrobertd_1998]: https://ntrs.nasa.gov/citations/20040090463
[research_godfrey_1973]: https://doi.org/10.2514/6.1973-441
[research_goertz_1995]: https://doi.org/10.2514/6.1995-2966
[research_goetze_schlippe_2025]: https://doi.org/10.1109/scc66396.2025.00019
[research_golato_santhanam_2015]: https://doi.org/10.1117/12.2084822
[research_golden_1969]: https://doi.org/10.21236/ad0858522
[research_goldinds_norgrenct_1963]: https://ntrs.nasa.gov/citations/19640010798
[research_golliard_mihaescu_2024]: https://doi.org/10.2514/6.2024-3032
[research_golliard_mihaescu_2024_b]: https://doi.org/10.2514/6.2024-2100.c1
[research_golliard_mihaescu_2024_c]: https://doi.org/10.2514/6.2024-2100
[research_golliard_mihaescu_2025]: https://doi.org/10.1063/5.0300850
[research_golliard_mihaescu_2025_b]: https://doi.org/10.1007/s10494-025-00700-4
[research_golliard_mihaescu_2026]: https://doi.org/10.2514/6.2026-3335
[research_golubev_2008]: https://doi.org/10.1007/s11018-008-9014-4
[research_golubl_1985]: https://ntrs.nasa.gov/citations/19850027436
[research_golubleon_1987]: https://ntrs.nasa.gov/citations/19870006616
[research_golubleon_1989]: https://ntrs.nasa.gov/citations/19890017416
[research_golubleon_1996]: https://ntrs.nasa.gov/citations/19970008135
[research_golubleon_1997]: https://ntrs.nasa.gov/citations/19970023202
[research_golubleon_1998]: https://ntrs.nasa.gov/citations/19980219480
[research_gompertz_1950]: https://doi.org/10.2514/8.4343
[research_goncharov_orlov_1995]: https://doi.org/10.2514/6.1995-3003
[research_gong_bing_2015]: https://doi.org/10.2514/6.2015-3606
[research_gong_chen_2014]: https://doi.org/10.2514/6.2014-2361
[research_gong_maunder_2017]: https://doi.org/10.2514/6.2017-5092
[research_gonsalves_ivanov_1999]: https://doi.org/10.2514/6.1999-4678
[research_gonzales_sakaue_2022]: https://doi.org/10.2514/6.2022-1661
[research_gonzales_sakaue_2022_b]: https://doi.org/10.1016/j.ast.2022.107718
[research_goodenowdebra_2004]: https://ntrs.nasa.gov/citations/20050186852
[research_goracke_levack_1997]: https://doi.org/10.2514/6.1997-2820
[research_goradiash_bobbittpj_1989]: https://ntrs.nasa.gov/citations/19900058467
[research_gorbunov_kirchengast_2018]: https://doi.org/10.5194/amt-11-111-2018
[research_gordan_mccrum_2023]: https://doi.org/10.1515/9783110791426-002
[research_gordon_brown_1963]: https://doi.org/10.21236/ad0296147
[research_gorla_brewer_2025]: https://doi.org/10.1115/vvuq2025-151983
[research_goto_nakayama_2021]: https://doi.org/10.1299/jsmehs.2021.58.g011
[research_goto_obayashi_2007]: https://doi.org/10.2514/1.23236
[research_goto_tsujimura_2025]: https://doi.org/10.1063/5.0245432
[research_gouldreginaldj_1993]: https://ntrs.nasa.gov/citations/19930070417
[research_gouri_krishnama_2025]: https://doi.org/10.1109/isbdas64762.2025.11117151
[research_gowan_2005]: https://doi.org/10.2514/6.2005-6505
[research_gowing_1990]: https://doi.org/10.21236/ada219109
[research_goyal]: https://doi.org/10.22215/etd/2017-11749
[research_gozuoglu_gercekcioglu_2026]: https://doi.org/10.2139/ssrn.6777259
[research_graberejjr_clarkjs_1972]: https://ntrs.nasa.gov/citations/19720015295
[research_grace_2001]: https://doi.org/10.21236/ada389584
[research_gradlpaul_2016]: https://ntrs.nasa.gov/citations/20160008867
[research_gradlpaulr_2016]: https://ntrs.nasa.gov/citations/20160009712
[research_gradlpaulr_2016_b]: https://ntrs.nasa.gov/citations/20160009711
[research_gradlpaulr_brandsmeierwill_2018]: https://ntrs.nasa.gov/citations/20180006324
[research_gradlpaulr_schmidttim_2016]: https://ntrs.nasa.gov/citations/20170002047
[research_graevee_masseyhn_1967]: https://ntrs.nasa.gov/citations/19680006892
[research_graham_2010]: https://doi.org/10.21236/ada532243
[research_grahamolinl_1987]: https://ntrs.nasa.gov/citations/19870015915
[research_grandhi_tobe_2010]: https://doi.org/10.21236/ada517384
[research_grantmm_stephanidescc_1964]: https://ntrs.nasa.gov/citations/19640013112
[research_grasslhj_1971]: https://ntrs.nasa.gov/citations/19720024225
[research_greatrix_2018]: https://doi.org/10.2514/6.2018-4442
[research_green_1994]: https://doi.org/10.2514/6.1994-2487
[research_greene_desjardins_1978]: https://doi.org/10.2514/6.1978-1705
[research_greeneep_1976]: https://ntrs.nasa.gov/citations/19770067032
[research_greeneep_1978]: https://ntrs.nasa.gov/citations/19780042289
[research_greeneep_1978_b]: https://ntrs.nasa.gov/citations/19790054749
[research_greenhallca_1976]: https://ntrs.nasa.gov/citations/19760020189
[research_greenroberto_pavribetina_2001]: https://ntrs.nasa.gov/citations/20020016078
[research_gregory_han_2003]: https://doi.org/10.2514/6.2003-373
[research_gregoryirenem_chowdhryrajivs_1992]: https://ntrs.nasa.gov/citations/19930003880
[research_gregoryirenem_mcminnjohnd_1993]: https://ntrs.nasa.gov/citations/19940020622
[research_grey_1953]: https://doi.org/10.21236/ad0036007
[research_grey_1954]: https://doi.org/10.21236/ad0042856
[research_grieb]: https://doi.org/10.15368/theses.2012.7
[research_grieb_lemieux_2011]: https://doi.org/10.2514/6.2011-5539
[research_griebelerelmer_nawashnuha_2011]: https://ntrs.nasa.gov/citations/20110012205
[research_griffin_sykes_2007]: https://doi.org/10.1109/eptc.2007.4469718
[research_griffindcjr_1975]: https://ntrs.nasa.gov/citations/19760031556
[research_griffinma_hassellhpjr_1965]: https://ntrs.nasa.gov/citations/19660014540
[research_griffinma_hassellhpjr_1966]: https://ntrs.nasa.gov/citations/19660025348
[research_grigoryev_burlutskiy_2021]: https://doi.org/10.31799/978-5-8088-1554-4-2021-2-182-187
[research_grinercarolyn_lylesgarry_1999]: https://ntrs.nasa.gov/citations/19990100868
[research_grodzovskii_1968]: https://doi.org/10.1007/bf01029537
[research_grondin]: https://doi.org/10.22215/etd/2009-13024
[research_grosdemange_schaeffer_1990]: https://doi.org/10.2514/6.1990-1835
[research_grosshandler_1999]: https://doi.org/10.6028/nist.ir.6424
[research_grubelich_rowland_1993]: https://doi.org/10.2514/6.1993-2265
[research_gu_cho_2021]: https://doi.org/10.1177/0020294021989740
[research_gu_liu_1995]: https://doi.org/10.2514/6.1995-2838
[research_guadagnini_dezaiacomo_2023]: https://doi.org/10.3390/aerospace11010035
[research_guenther_compton_2026]: https://doi.org/10.2514/6.2026-1970
[research_guidance_for]: https://doi.org/10.4271/arp6821
[research_guidelines_for]: https://doi.org/10.4271/arp6461a
[research_guidelines_on_2023]: https://doi.org/10.4060/cc6556en
[research_guimpilevich_vertegel]: https://doi.org/10.1109/crmico.2000.880303
[research_guimpilevich_vertegel_2000]: https://doi.org/10.1109/crmico.2000.1256193
[research_gulatis_tawelr_1993]: https://ntrs.nasa.gov/citations/19930013032
[research_guler_2026]: https://doi.org/10.18245/ijaet.1955740
[research_gunn_1989]: https://doi.org/10.2514/6.1989-2386
[research_gunterej_flackrd_1981]: https://ntrs.nasa.gov/citations/19820058263
[research_guo_eriksen_2008]: https://doi.org/10.1109/memsys.2008.4443800
[research_guo_musgrave]: https://doi.org/10.1109/acc.1995.520974
[research_guo_zhao_2023]: https://doi.org/10.23919/ccc58697.2023.10240040
[research_guo_zhu_2012]: https://doi.org/10.2514/6.2012-1179
[research_guo_zhu_2013]: https://doi.org/10.1016/j.asr.2013.06.021
[research_guodongning_shuguangzhang]: https://doi.org/10.1109/isscaa.2006.1627416
[research_guoth_merrillw_1990]: https://ntrs.nasa.gov/citations/19910046007
[research_guoth_merrillw_1992]: https://ntrs.nasa.gov/citations/19930009829
[research_gupta_2011]: https://doi.org/10.1007/978-3-642-20989-5_5
[research_gupta_anilkumar_2018]: https://doi.org/10.18520/cs/v114/i01/131-136
[research_guy_mclaughlin_2001]: https://doi.org/10.2514/6.2001-888
[research_guzik_cengarle_2025]: https://doi.org/10.21437/interspeech.2025-746
[research_ha_kim_2019]: https://doi.org/10.2514/6.2019-3881
[research_ha_kim_2022]: https://doi.org/10.1016/j.actaastro.2022.09.031
[research_haagthomasw_1989]: https://ntrs.nasa.gov/citations/19900006676
[research_haasevan_delucciafrank_2016]: https://ntrs.nasa.gov/citations/20160011562
[research_haberstroh_besnard_2008]: https://doi.org/10.2514/6.2008-4662
[research_haddockpaulc_horanstephen_1998]: https://ntrs.nasa.gov/citations/19980151081
[research_hadjria_dalmeida_2019]: https://doi.org/10.12783/shm2019/32280
[research_haftka_yuan_2010]: https://doi.org/10.21236/ada547408
[research_hagar_alcock_1989]: https://doi.org/10.2514/6.1989-2852
[research_hagopian_2002]: https://doi.org/10.2514/6.2002-t3-55
[research_haidinger_weiland_1997]: https://doi.org/10.2514/6.1997-2808
[research_haldorsen_2020]: https://doi.org/10.1190/segam2020-3421471.1
[research_hale_wang_2009]: https://doi.org/10.1109/tim.2008.2005560
[research_hall_2005]: https://doi.org/10.1109/amuem.2005.1594608
[research_hall_2012]: https://doi.org/10.4043/23218-ms
[research_hall_hartsfield_2011]: https://doi.org/10.2514/6.2011-419
[research_hall_shtessel_2005]: https://doi.org/10.2514/6.2005-6145
[research_hallcharlese_gallahermichaelw_1998]: https://ntrs.nasa.gov/citations/19980237256
[research_hallcharlese_panossianhagopv_1999]: https://ntrs.nasa.gov/citations/19990103171
[research_hallcrjr_muellertj_1971]: https://ntrs.nasa.gov/citations/19710037805
[research_hamedawatef_1990]: https://ntrs.nasa.gov/citations/19900055715
[research_hamiltontom_healytom_1999]: https://ntrs.nasa.gov/citations/19990077349
[research_hamkinsjon_vilnrottervictor_2019]: https://ntrs.nasa.gov/citations/20210005966
[research_hamkinsjon_vilnrottervictora_2011]: https://ntrs.nasa.gov/citations/20110012211
[research_hammond]: https://doi.org/10.17918/00002214
[research_hampson_1984]: https://doi.org/10.4271/841619
[research_hampsonme_barkhoudarians_1985]: https://ntrs.nasa.gov/citations/19850018596
[research_han_mateescu_2012]: https://doi.org/10.1115/smasis2012-8005
[research_han_wang_2019]: https://doi.org/10.3850/978-981-11-2730-4_0218-cd
[research_hanapur_hiremath_2022]: https://doi.org/10.1016/j.matpr.2021.07.425
[research_handbook_for_1975]: https://ntrs.nasa.gov/citations/19750009792
[research_hanford_1969]: https://doi.org/10.2514/6.1969-441
[research_hangrichard_2017]: https://ntrs.nasa.gov/citations/20170009876
[research_hankejeremyl_2011]: https://ntrs.nasa.gov/citations/20110013667
[research_hannigan_sved_1993]: https://doi.org/10.2514/6.1993-5081
[research_hannum_kasper_1976]: https://doi.org/10.2514/6.1976-685
[research_hansamuels_1990]: https://ntrs.nasa.gov/citations/19910009672
[research_hansamuels_1991]: https://ntrs.nasa.gov/citations/19920006646
[research_hansen_gabris_1967]: https://doi.org/10.2514/6.1967-1350
[research_hao_peng_2017]: https://doi.org/10.2514/6.2017-2108
[research_hara_mamashita_2024]: https://doi.org/10.2514/6.2024-3504
[research_harderkeithc_rennemannconradjr_1956]: https://ntrs.nasa.gov/citations/19930092270
[research_hardesty_1970]: https://doi.org/10.21236/ad0726118
[research_hardgrove_kriegjr_1984]: https://doi.org/10.2514/6.1984-1254
[research_hardy_eldrenkamp_1993]: https://doi.org/10.2514/6.1993-4161
[research_hardyterryl_rappdouglasc_1994]: https://ntrs.nasa.gov/citations/19940024900
[research_harneypf_1981]: https://ntrs.nasa.gov/citations/19810011546
[research_harneypf_richardsonrb_1968]: https://ntrs.nasa.gov/citations/19690041143
[research_harringtonde_1970]: https://ntrs.nasa.gov/citations/19710004544
[research_harringtonde_1970_b]: https://ntrs.nasa.gov/citations/19700033122
[research_harringtonde_noseksm_1974]: https://ntrs.nasa.gov/citations/19740027090
[research_harringtonde_schloemerjj_1974]: https://ntrs.nasa.gov/citations/19740007347
[research_harringtonde_schloemerjj_1975]: https://ntrs.nasa.gov/citations/19760003038
[research_harringtonde_schloemerjj_1976]: https://ntrs.nasa.gov/citations/19760017153
[research_harringtonde_waskora_1968]: https://ntrs.nasa.gov/citations/19680026660
[research_harris_1963]: https://doi.org/10.21236/ad0402393
[research_harris_dizaji_2018]: https://doi.org/10.1117/12.2296521
[research_harrisb_1962]: https://ntrs.nasa.gov/citations/19630018611
[research_harrison_lockman_1969]: https://doi.org/10.2514/3.29536
[research_harrje_1959]: https://doi.org/10.21236/ad0212816
[research_harroun_heister_2019]: https://doi.org/10.2514/6.2019-0197
[research_hartrogerg_katzellisr_1949]: https://ntrs.nasa.gov/citations/20050019251
[research_harvazinski_sankaran_2014]: https://doi.org/10.21236/ada611028
[research_hase_2004]: https://doi.org/10.2514/6.2004-278-126
[research_hassani_dackermann_2023]: https://doi.org/10.3390/s23063293
[research_hassneal_mizukamimasashi_1999]: https://ntrs.nasa.gov/citations/19990106559
[research_hattisphilipd_malchowharveyl_1991]: https://ntrs.nasa.gov/citations/19920002784
[research_hattisphilipd_malchowharveyl_1992]: https://ntrs.nasa.gov/citations/19930003225
[research_hauer_tabata_1963]: https://doi.org/10.2514/6.1963-1410
[research_hauptscheina_sommerrc_1963]: https://ntrs.nasa.gov/citations/19630029029
[research_hauser_helfrich_1963]: https://doi.org/10.21236/ad0406781
[research_havelundklaus_joshirajeev_2014]: https://ntrs.nasa.gov/citations/20160005627
[research_hdouglasperkins]: https://ntrs.nasa.gov/citations/20230013227
[research_he_he_2004]: https://doi.org/10.2514/6.2004-4818
[research_he_li_2018]: https://doi.org/10.1109/gncc42960.2018.9018857
[research_he_liu_2020]: https://doi.org/10.1109/icca51439.2020.9264318
[research_he_pan_2025]: https://doi.org/10.2139/ssrn.5491930
[research_he_pan_2026]: https://doi.org/10.1016/j.csite.2025.107568
[research_he_qin_2015]: https://doi.org/10.1016/j.cja.2015.06.016
[research_he_shi_2022]: https://doi.org/10.3390/electronics11172656
[research_he_xu_2018]: https://doi.org/10.1155/2018/7540129
[research_he_yuan_2024]: https://doi.org/10.1016/b978-0-443-15476-8.00007-1
[research_headvl_1974]: https://ntrs.nasa.gov/citations/19740008377
[research_heat_transfer_1994]: https://doi.org/10.2514/6.1994-3291
[research_heath_bell_2020]: https://doi.org/10.29311/2020.53
[research_heathchristopherm_grayjustins_2015]: https://ntrs.nasa.gov/citations/20150000697
[research_heatherphoulden_erinhubbard]: https://ntrs.nasa.gov/citations/20205003454
[research_hedrick_friman_2026]: https://doi.org/10.1093/icb/icag124
[research_heidenreich_gross_2017]: https://doi.org/10.1016/j.measurement.2016.06.009
[research_heinejc_1964]: https://ntrs.nasa.gov/citations/19660004825
[research_heister_2008]: https://doi.org/10.21236/ada494724
[research_hellman_2006]: https://doi.org/10.2514/6.2006-7259
[research_hellman_pleiman_2013]: https://doi.org/10.2514/6.2013-5531
[research_hellman_remillard_2011]: https://doi.org/10.21236/ada554045
[research_hellman_tejtel_2008]: https://doi.org/10.2514/6.2008-2566
[research_hellman_wallace_2011]: https://doi.org/10.21236/ada551823
[research_hemschmichaelj_2016]: https://ntrs.nasa.gov/citations/20160007695
[research_hemschmichaelj_hankejeremyl_2008]: https://ntrs.nasa.gov/citations/20080024105
[research_hendershotkc_1966]: https://ntrs.nasa.gov/citations/19990053122
[research_henderson_mathews_2016]: https://doi.org/10.21236/ad1004755
[research_hendrixjm_1969]: https://ntrs.nasa.gov/citations/19690000555
[research_hennenha_lambertrf_1968]: https://ntrs.nasa.gov/citations/19680062377
[research_henningallenb_1959]: https://ntrs.nasa.gov/citations/19980228138
[research_herbellthomasp_eckelandrewj_1991]: https://ntrs.nasa.gov/citations/19910068929
[research_herbertphillipwsr_elliotalexc_2015]: https://ntrs.nasa.gov/citations/20150010686
[research_herbertphillipwsr_elliottalexc_2017]: https://ntrs.nasa.gov/citations/20180003432
[research_hergert_brock_2017]: https://doi.org/10.2514/6.2017-4462
[research_hergertjakobd_brockjosephm_2017]: https://ntrs.nasa.gov/citations/20180006640
[research_hermance_1961]: https://doi.org/10.21236/ad0261589
[research_herrera_2023]: https://doi.org/10.58286/28691
[research_herrick_1968]: https://doi.org/10.2514/6.1968-598
[research_herrickwd_penegorgt_1990]: https://ntrs.nasa.gov/citations/19900055875
[research_herronandrewj_crosbywilliama_2016]: https://ntrs.nasa.gov/citations/20160001830
[research_hertzfeld_2000]: https://doi.org/10.2514/6.2000-5113
[research_herzog_yue_1998]: https://doi.org/10.2514/6.1998-3604
[research_hess_james_1975]: https://doi.org/10.21236/ada006588
[research_hessling_2011]: https://doi.org/10.1088/0957-0233/22/10/105105
[research_hetmaniok_brociek_2024]: https://doi.org/10.7148/2024-0261
[research_heuston_fish_1967]: https://doi.org/10.4271/670393
[research_hickamwm_sternberghsa_1966]: https://ntrs.nasa.gov/citations/19660024169
[research_hiers_mackinnon_2003]: https://doi.org/10.2514/6.2003-5183
[research_higgins_jacobson_1964]: https://doi.org/10.21236/ad0602928
[research_high_load_strain_2018]: https://doi.org/10.12968/s1478-2774(23)50053-3
[research_hill_1963]: https://doi.org/10.21236/ad0402192
[research_hilla_acostae_2005]: https://ntrs.nasa.gov/citations/20050206347
[research_hilljeer_nelsonrl_1981]: https://ntrs.nasa.gov/citations/19820030365
[research_hillkh_leighouro_1971]: https://ntrs.nasa.gov/citations/19710020620
[research_hills_1985]: https://doi.org/10.21236/ada162149
[research_hillsley_robbins_1964]: https://doi.org/10.1016/b978-1-4831-9812-5.50009-6
[research_hilten_1970]: https://doi.org/10.6028/nbs.tn.517
[research_hinchey_1968]: https://doi.org/10.2514/6.1968-345
[research_hinedis_bevanr_1991]: https://ntrs.nasa.gov/citations/19910009007
[research_hinedisamim_bevanrolandp_1993]: https://ntrs.nasa.gov/citations/19930000019
[research_hinesjohnw_sompschris_1995]: https://ntrs.nasa.gov/citations/20020022354
[research_hinrichs_2006]: https://doi.org/10.1524/teme.2006.73.5.301
[research_hodelas_callahanronnie_2002]: https://ntrs.nasa.gov/citations/20020092013
[research_hoertel_1961]: https://doi.org/10.21236/ad0259441
[research_hoff_2007]: https://doi.org/10.4271/2007-01-2542
[research_hoffhl_1965]: https://ntrs.nasa.gov/citations/19660039297
[research_hogiekeith_crisuoloed_2004]: https://ntrs.nasa.gov/citations/20040081174
[research_holdhusen_perusse_1965]: https://doi.org/10.21236/ada956154
[research_holgersenl_knutsone_1966]: https://ntrs.nasa.gov/citations/19670033079
[research_holmesjk_1979]: https://ntrs.nasa.gov/citations/19790016923
[research_holmesrg_stagnerhr_1964]: https://ntrs.nasa.gov/citations/19660009048
[research_holmesrg_stagnerhr_1965]: https://ntrs.nasa.gov/citations/19660034310
[research_holmesrichard_ellisdavid_1999]: https://ntrs.nasa.gov/citations/19990097307
[research_holtjamesb_deespatrickd_2015]: https://ntrs.nasa.gov/citations/20150021431
[research_homquestdl_1970]: https://ntrs.nasa.gov/citations/19700068265
[research_honeycuttjohn_lylesgarry_2016]: https://ntrs.nasa.gov/citations/20160006988
[research_hong_wang_2026]: https://doi.org/10.1109/taes.2026.3688220
[research_hong_xiong_2014]: https://doi.org/10.1109/chicc.2014.6896100
[research_hooke_1979]: https://doi.org/10.1117/12.957311
[research_hookeadrianj_macmedanmervynl_1990]: https://ntrs.nasa.gov/citations/19910030346
[research_hookeaj_greenberge_1985]: https://ntrs.nasa.gov/citations/19840000276
[research_hopkinspm_1972]: https://ntrs.nasa.gov/citations/19730030655
[research_hopkorusselln_1954]: https://ntrs.nasa.gov/citations/19930090504
[research_hopsongeorged_mcanellywilliamb_1966]: https://ntrs.nasa.gov/citations/19990046695
[research_horan_2003]: https://doi.org/10.1016/b978-012620861-0/50012-7
[research_horiuchihs_1964]: https://ntrs.nasa.gov/citations/19650006056
[research_horiuchihs_martinnl_1965]: https://ntrs.nasa.gov/citations/19660031835
[research_horneman_kluever_2004]: https://doi.org/10.2514/6.2004-5183
[research_hornerward_sabiasteve_1989]: https://ntrs.nasa.gov/citations/19900041851
[research_hornstein_1965]: https://doi.org/10.21236/ad0622524
[research_hortonja_masseyhn_1966]: https://ntrs.nasa.gov/citations/19660022608
[research_hosack_1969]: https://doi.org/10.2514/6.1969-473
[research_hosack_stromsta_1969]: https://doi.org/10.2514/6.1969-4
[research_houtsrc_parsonsfd_1968]: https://ntrs.nasa.gov/citations/19690001712
[research_howardfg_goodmanwl_1983]: https://ntrs.nasa.gov/citations/19830057410
[research_howardfg_goodmanwl_1984]: https://ntrs.nasa.gov/citations/19860011259
[research_howardfg_goodmanwl_1985]: https://ntrs.nasa.gov/citations/19850053436
[research_howellrobertr_braslowalbertl_1955]: https://ntrs.nasa.gov/citations/20050019382
[research_hsalpert_ramiller_2021]: https://ntrs.nasa.gov/citations/20210014000
[research_hu_2025]: https://doi.org/10.64336/001c.154674
[research_hu_bai_2021]: https://doi.org/10.1109/access.2021.3120840
[research_hu_deng_2015]: https://doi.org/10.4028/www.scientific.net/amm.719-720.324
[research_hu_wang_2012]: https://doi.org/10.4028/www.scientific.net/amm.236-237.1339
[research_huang_1974]: https://doi.org/10.2514/6.1974-1080
[research_huang_2023]: https://doi.org/10.1109/icipca59209.2023.10257687
[research_huang_2026]: https://doi.org/10.1016/j.ress.2026.112327
[research_huang_cheng_2024]: https://doi.org/10.1007/978-981-97-6485-3_7
[research_huang_cheng_2024_b]: https://doi.org/10.1007/978-981-97-6485-3_8
[research_huang_cheng_2025]: https://doi.org/10.1007/978-981-97-6485-3
[research_huang_gardner_2016]: https://doi.org/10.2514/6.2016-2057
[research_huang_xia_2021]: https://doi.org/10.1016/j.ast.2021.106969
[research_huang_xie_2024]: https://doi.org/10.1016/j.isatra.2024.08.011
[research_huang_yao_2020]: https://doi.org/10.1016/j.ijheatmasstransfer.2019.119236
[research_huang_zhang_2015]: https://doi.org/10.2991/icmmita-15.2015.257
[research_huang_zhang_2026]: https://doi.org/10.1007/s42405-026-01213-8
[research_huang_zhao_2017]: https://doi.org/10.1016/j.ast.2017.10.017
[research_hubbarderinp_2019]: https://ntrs.nasa.gov/citations/20190001452
[research_huberman_kidd_1970]: https://doi.org/10.2514/6.1970-1114
[research_hudginsji_leasejr_1969]: https://ntrs.nasa.gov/citations/19700009276
[research_hudson_brosz_1981]: https://doi.org/10.2514/6.1981-3255
[research_hudson_zoladz_2000]: https://doi.org/10.2514/6.2000-3239
[research_hudsonsusant_zoladzthomasf_2002]: https://ntrs.nasa.gov/citations/20020087939
[research_huegelfred_1998]: https://ntrs.nasa.gov/citations/19980227008
[research_huerta_1969]: https://doi.org/10.21236/ad0855156
[research_hueteruwe_2000]: https://ntrs.nasa.gov/citations/20000039349
[research_huffmanjr_tilmann_1996]: https://doi.org/10.2514/6.1996-2450
[research_hughesmarks_davisdawnm_2007]: https://ntrs.nasa.gov/citations/20070012331
[research_hulka_2008]: https://doi.org/10.2514/6.2008-5113
[research_hull_1967]: https://doi.org/10.1007/bf00932555
[research_hummel_1995]: https://doi.org/10.21236/ada301101
[research_hunley_2008]: https://doi.org/10.5744/florida/9780813031781.001.0001
[research_hunley_2008_b]: https://doi.org/10.5744/florida/9780813031774.001.0001
[research_hunley_2008_c]: https://doi.org/10.5744/florida/9780813031781.003.0009
[research_huntergaryw_behbahanialireza_2012]: https://ntrs.nasa.gov/citations/20150010128
[research_huntleysc_samanichne_1969]: https://ntrs.nasa.gov/citations/19690011401
[research_huppihal_tobiasmark_2003]: https://ntrs.nasa.gov/citations/20030065843
[research_hurdwj_browndh_1988]: https://ntrs.nasa.gov/citations/19880018800
[research_hurleymj_1972]: https://ntrs.nasa.gov/citations/19720013236
[research_hurtgj_linalj_1964]: https://ntrs.nasa.gov/citations/20070030964
[research_husick_ritenour_1966]: https://doi.org/10.1109/taes.1966.4501875
[research_husick_ritenour_1967]: https://doi.org/10.1016/b978-1-4831-9836-1.50015-0
[research_hutchison_2011]: https://doi.org/10.2514/6.2011-2296
[research_huzel_1993]: https://doi.org/10.2514/4.470721
[research_hybrid_rocket_1991]: https://ntrs.nasa.gov/citations/19920013360
[research_hybrid_rocket_2019]: https://doi.org/10.1017/9781108381376.012
[research_hyde_2002]: https://doi.org/10.21236/ada406078
[research_hyde_argueta_2025]: https://doi.org/10.2514/6.2025-0109
[research_hydecharlesr_massiejeffreyj_1993]: https://ntrs.nasa.gov/citations/19930068757
[research_hydrogen_peroxide_1994]: https://doi.org/10.2514/6.1994-3147
[research_hydrostatic_bearings_1969]: https://doi.org/10.1016/0043-1648(69)90109-4
[research_hynesrt_1967]: https://ntrs.nasa.gov/citations/19670056495
[research_hynesrt_1968]: https://ntrs.nasa.gov/citations/19680048430
[research_iaconis_demilia_1994]: https://doi.org/10.1111/j.1475-1305.1994.tb00917.x
[research_iafrate_brandonisio_2025]: https://doi.org/10.1016/j.actaastro.2024.11.028
[research_ibell]: https://doi.org/10.14264/e0978cb
[research_idzkowski_walendziuk_2016]: https://doi.org/10.3846/biomdlore.2016.05
[research_iglesias_haynes_2015]: https://doi.org/10.21236/ada618120
[research_iguchi_matsuoka_2014]: https://doi.org/10.1088/0957-0233/25/7/075803
[research_iliopoulou_denos_2004]: https://doi.org/10.1115/gt2004-53437
[research_imbaratto]: https://doi.org/10.15368/theses.2009.133
[research_imhuelse_zydel_2024]: https://doi.org/10.52202/078373-0099
[research_imlachjoseph_kasardamary_2008]: https://ntrs.nasa.gov/citations/20080048188
[research_immich_caporicci_1996]: https://doi.org/10.2514/6.1996-3113
[research_implantable_telemetry_1982]: https://ntrs.nasa.gov/citations/19820018499
[research_in_flight_thrust]: https://doi.org/10.4271/air6007
[research_in_flight_thrust_b]: https://doi.org/10.4271/air1703a
[research_inatani_naruo_1999]: https://doi.org/10.2514/6.1999-4874
[research_inatomi_kitamura_2019]: https://doi.org/10.2322/tastj.17.439
[research_india_to_2015]: https://doi.org/10.1063/pt.5.028943
[research_ingelsfrank_parkerglenn_1989]: https://ntrs.nasa.gov/citations/19900041822
[research_inokuchi_1996]: https://doi.org/10.1063/1.49968
[research_instability_phenomenology_1995]: https://doi.org/10.2514/5.9781600866371.0113.0142
[research_instability_phenomenology_1995_b]: https://doi.org/10.2514/5.9781600866371.0073.0088
[research_instability_phenomenology_1995_c]: https://doi.org/10.2514/5.9781600866371.0003.0037
[research_instability_phenomenology_1995_d]: https://doi.org/10.2514/5.9781600866371.0089.0112
[research_instrumentation_for_2023]: https://doi.org/10.12968/s1478-2774(23)50367-7
[research_integral_sensor_1965]: https://ntrs.nasa.gov/citations/19650025507
[research_integrated_advanced_2000]: https://ntrs.nasa.gov/citations/20000112924
[research_intelligenceandneuroscience_2023]: https://doi.org/10.1155/2023/9830360
[research_inturi_lovaraju_2025]: https://doi.org/10.1007/978-981-97-6783-0_19
[research_inui_kawahara_2009]: https://doi.org/10.2322/tstj.7.pf_11
[research_irimpan_mannil_2015]: https://doi.org/10.1016/j.measurement.2014.10.056
[research_ironsjamesr_irishrichardr_1988]: https://ntrs.nasa.gov/citations/19890040394
[research_ishida_sekikawa_2015]: https://doi.org/10.1109/ascc.2015.7244829
[research_ishikawar_kanor_2018]: https://ntrs.nasa.gov/citations/20180007498
[research_ishikawaryohko_mckenziedavid_2019]: https://ntrs.nasa.gov/citations/20190028985
[research_ishimoto_fujii_2005]: https://doi.org/10.1016/j.actaastro.2005.03.045
[research_ishimoto_takizawa_1996]: https://doi.org/10.2514/6.1996-3403
[research_islam_2024]: https://doi.org/10.36227/techrxiv.173108983.33145483/v1
[research_isro_releases_the_2018]: https://doi.org/10.18520/cs/v114/i08/1596-1596
[research_issitt_mahendrakar_2026]: https://doi.org/10.2514/6.2026-0789
[research_ito_fujii_2001]: https://doi.org/10.2514/6.2001-2861
[research_ito_fujii_2002]: https://doi.org/10.2514/6.2002-3119
[research_ito_fujii_2003]: https://doi.org/10.1007/978-3-642-59334-5_41
[research_ito_fujii_2003_b]: https://doi.org/10.2322/tjsass.46.17
[research_ivanova_khoroshilov_2023]: https://doi.org/10.33136/stma2023.01.041
[research_iwabuchi_hashimoto_2025]: https://doi.org/10.1007/978-981-96-5622-6_2
[research_jackjohnr_1953]: https://ntrs.nasa.gov/citations/19930083638
[research_jacksoncmjr_smithrs_1969]: https://ntrs.nasa.gov/citations/19690010571
[research_jacksonhherbert_rumseycharlesb_1950]: https://ntrs.nasa.gov/citations/19930086324
[research_jacksonhherbert_rumseycharlesb_1954]: https://ntrs.nasa.gov/citations/19930084086
[research_jacksonjerrye_espenschiederich_1998]: https://ntrs.nasa.gov/citations/19980174934
[research_jacksonmarkusdeon_2015]: https://ntrs.nasa.gov/citations/20160006903
[research_jacksonwh_eatonjp_1971]: https://ntrs.nasa.gov/citations/19730007672
[research_jacob_2008]: https://doi.org/10.2514/6.2008-1427
[research_jadhav_kulkarni_2020]: https://doi.org/10.1007/s00231-020-02887-w
[research_jain_kumar_2022]: https://doi.org/10.2514/6.2022-3861
[research_jamescarltons_1960]: https://ntrs.nasa.gov/citations/19980227205
[research_jamescarltons_carrosrobertj_1953]: https://ntrs.nasa.gov/citations/19930087740
[research_jamesk_quickb_1984]: https://ntrs.nasa.gov/citations/19850005285
[research_jamesmramey_ianmgiles]: https://ntrs.nasa.gov/citations/20220017645
[research_jamiegmeeroff_derekjdalle]: https://ntrs.nasa.gov/citations/20220018893
[research_jamisonde_1965]: https://ntrs.nasa.gov/citations/19650022946
[research_jamisonde_1966]: https://ntrs.nasa.gov/citations/19660013075
[research_janardanba_majjigirk_1985]: https://ntrs.nasa.gov/citations/19870019882
[research_jangjiannwoei_alanizabran_2011]: https://ntrs.nasa.gov/citations/20110015701
[research_jannetteanthonyg_hojnickijeffreys_2002]: https://ntrs.nasa.gov/citations/20020070612
[research_japan_s_liquid_2006]: https://doi.org/10.2514/5.9781600868870.0815.0842
[research_jasterhardt_1965]: https://ntrs.nasa.gov/citations/19660011698
[research_jategaonkar_behr_2006]: https://doi.org/10.2514/1.19602
[research_jebsorr_timothymbarrows]: https://ntrs.nasa.gov/citations/20230000427
[research_jeffhagen_michaelburlone]: https://ntrs.nasa.gov/citations/20200007987
[research_jenke_1976]: https://doi.org/10.21236/ada027027
[research_jenkins_1970]: https://doi.org/10.2514/6.1970-1405
[research_jenkinsgeorge_1986]: https://ntrs.nasa.gov/citations/19870050110
[research_jenkinsrhonaldm_1997]: https://ntrs.nasa.gov/citations/19970026201
[research_jenkinsrhonaldm_fosterwinfredajr_1993]: https://ntrs.nasa.gov/citations/19950017220
[research_jenn_nelson_1988]: https://doi.org/10.2514/3.26017
[research_jenne_2006]: https://doi.org/10.1121/1.4786202
[research_jensen_2001]: https://doi.org/10.2514/6.2001-3554
[research_jensen_2001_b]: https://doi.org/10.21236/ada416367
[research_jensen_2002]: https://doi.org/10.21236/ada416516
[research_jensen_2003]: https://doi.org/10.21236/ada416319
[research_jensen_2005]: https://doi.org/10.2514/6.2005-4566
[research_jensen_goshgarian_1962]: https://doi.org/10.21236/ad0295656
[research_jeremytpinier]: https://ntrs.nasa.gov/citations/20230016819
[research_jernellls_croomdr_1979]: https://ntrs.nasa.gov/citations/19790011930
[research_jet_thrust_2003]: https://doi.org/10.2514/5.9781600861840.0069.0074
[research_jetevator_for_1998]: https://doi.org/10.1108/aeat.1998.12770cad.013
[research_jha_2024]: https://doi.org/10.2139/ssrn.4889182
[research_jha_m_2013]: https://doi.org/10.1016/j.engfailanal.2012.08.008
[research_jha_sullivan_2016]: https://doi.org/10.1201/9781315373492-11
[research_ji_wang_2012]: https://doi.org/10.4028/www.scientific.net/amr.443-444.719
[research_jiandong_qiang_2020]: https://doi.org/10.1109/aiam50918.2020.00093
[research_jiang_dong_2012]: https://doi.org/10.1007/978-3-642-33663-8_25
[research_jiang_jiang_2023]: https://doi.org/10.1109/icn60549.2023.10426290
[research_jiang_ordonez_2008]: https://doi.org/10.1109/cca.2008.4629595
[research_jiang_ordonez_2009]: https://doi.org/10.1016/j.automatica.2009.03.017
[research_jianghui_horanstephen_2000]: https://ntrs.nasa.gov/citations/20000052714
[research_jianguo_guoqing_2016]: https://doi.org/10.1109/ccdc.2016.7532005
[research_jiao_leger_2002]: https://doi.org/10.4043/14077-ms
[research_jieli_elaralash]: https://ntrs.nasa.gov/citations/20210024355
[research_jieli_nettiehroozeboom]: https://ntrs.nasa.gov/citations/20230017201
[research_jieli_nettiehroozeboom_b]: https://ntrs.nasa.gov/citations/20230006831
[research_jin_shang_2024]: https://doi.org/10.1063/5.0236275
[research_jin_tian_2022]: https://doi.org/10.1016/j.mejo.2022.105568
[research_jjdonegan_1958]: https://ntrs.nasa.gov/citations/19740074646
[research_joachimbalis_hervelamy_2025]: https://ntrs.nasa.gov/citations/15037188328199
[research_johanklun_brucelipe_2020]: https://ntrs.nasa.gov/citations/20205001335
[research_johnhenrykorth]: https://ntrs.nasa.gov/citations/20230018211
[research_johnhenrykorth_jonathanmburt]: https://ntrs.nasa.gov/citations/20240014370
[research_johnhenrykorth_jonathanmburt_2025]: https://ntrs.nasa.gov/citations/20250006610
[research_johnhwall_colterwrussell]: https://ntrs.nasa.gov/citations/20230000649
[research_johnsal_1969]: https://ntrs.nasa.gov/citations/19690018462
[research_johnson_1972]: https://doi.org/10.21236/ad0752218
[research_johnson_jacobs_2006]: https://doi.org/10.2514/6.2006-7230
[research_johnson_servidio_2008]: https://doi.org/10.2514/6.2008-7647
[research_johnsonharolds_hayeswilliamc_1953]: https://ntrs.nasa.gov/citations/19930087757
[research_johnsonkatie_2016]: https://ntrs.nasa.gov/citations/20160010241
[research_johnsonmartinl_crawfordkevin_2011]: https://ntrs.nasa.gov/citations/20120001504
[research_johnstripp_1999]: https://ntrs.nasa.gov/citations/19990041532
[research_jones_2004]: https://doi.org/10.2514/6.2004-3742
[research_jones_bergquist_1977]: https://doi.org/10.1088/0022-3735/10/12/022
[research_jones_jr_1993]: https://doi.org/10.21236/ada308579
[research_jones_townsend_2000]: https://doi.org/10.2514/6.2000-268
[research_jonesdaniels_rufjosephh_2014]: https://ntrs.nasa.gov/citations/20140016907
[research_joneshbjr_knauerrc_1965]: https://ntrs.nasa.gov/citations/19650046519
[research_jonesjonathan_kibbeytim_2014]: https://ntrs.nasa.gov/citations/20140010983
[research_joneskennethm_1994]: https://ntrs.nasa.gov/citations/19950012573
[research_joneskennethw_zollerlowellk_1989]: https://ntrs.nasa.gov/citations/19920055603
[research_joneskennethw_zollerlowellk_1989_b]: https://ntrs.nasa.gov/citations/19890059597
[research_jonesrh_1970]: https://ntrs.nasa.gov/citations/19700028978
[research_jonesrobertt_margoliskenneth_1946]: https://ntrs.nasa.gov/citations/19930084662
[research_jonesron_smithdan_2017]: https://ntrs.nasa.gov/citations/20210007913
[research_jonesrt_margolisk_1976]: https://ntrs.nasa.gov/citations/19760011996
[research_josephawehrmeyer_2002]: https://ntrs.nasa.gov/citations/20020068838
[research_josephhernandezmccloskey_sethareutlinger]: https://ntrs.nasa.gov/citations/20240015605
[research_jourdaine_tsuboi_2019]: https://doi.org/10.1016/j.proci.2018.09.024
[research_jsadams_ajanderson_2020]: https://ntrs.nasa.gov/citations/20210010913
[research_juhlin_jakobsson_2023]: https://doi.org/10.1016/j.sigpro.2022.108679
[research_julianshamilton]: https://ntrs.nasa.gov/citations/19640056899
[research_junaidr_beebim_2015]: https://doi.org/10.70729/ijser15399
[research_jung_2018]: https://doi.org/10.11159/icmie18.108
[research_jurist_2009]: https://doi.org/10.1080/14777620902782660
[research_just_1991]: https://doi.org/10.2514/6.1991-839
[research_justingchen_raulrios]: https://ntrs.nasa.gov/citations/20220015593
[research_ka_parikh_2025]: https://doi.org/10.52202/080564-0026
[research_kachler_beaurain_2005]: https://doi.org/10.2514/6.2005-3563
[research_kah_1970]: https://doi.org/10.4271/700798
[research_kajita_2019]: https://doi.org/10.1088/2053-2563/ab0373ch2
[research_kalden_2007]: https://doi.org/10.1109/rast.2007.4283979
[research_kammer_smith_1963]: https://doi.org/10.21236/ad0430879
[research_kamperman_1957]: https://doi.org/10.1121/1.1918891
[research_kanazaki_ito_2016]: https://doi.org/10.1299/jfst.2016jfst0003
[research_kane_1994]: https://ntrs.nasa.gov/citations/20210004135
[research_kanedwinp_1994]: https://ntrs.nasa.gov/citations/19950010789
[research_kang_wang_2018]: https://doi.org/10.1016/j.actaastro.2017.12.038
[research_kannengieser_colin_2010]: https://doi.org/10.1007/s12217-010-9211-z
[research_kannmn_1966]: https://ntrs.nasa.gov/citations/19670038734
[research_kanso_jha_2022]: https://doi.org/10.1016/j.ifacol.2022.07.112
[research_kantorav_perevertkinsm_1974]: https://ntrs.nasa.gov/citations/19750002931
[research_kanwar_2024]: https://doi.org/10.69980/redvet.v25i1.728
[research_kaosimona_laffeythomasj_1987]: https://ntrs.nasa.gov/citations/19890029146
[research_kaplan_2002]: https://doi.org/10.1063/1.1449851
[research_kapoor_1982]: https://doi.org/10.2514/3.62212
[research_karel_1967]: https://doi.org/10.4271/670378
[research_karenadeere_stevenekrist_2024]: https://ntrs.nasa.gov/citations/20230018400
[research_kargin_2014]: https://doi.org/10.15622/sp.29.3
[research_karim_some_2026]: https://doi.org/10.29322/ijsrp.16.06.2026.p17413
[research_karlgaard_tynis_2018]: https://doi.org/10.2514/6.2018-3624
[research_karlgaard_tynis_2019]: https://doi.org/10.2514/6.2019-0014
[research_karlgaardchristopherd_kuttyprasad_2013]: https://ntrs.nasa.gov/citations/20130003188
[research_karlgaardchristopherd_martinjohng_2005]: https://ntrs.nasa.gov/citations/20050232845
[research_karlgaardchristopherd_tartabinipaulv_2004]: https://ntrs.nasa.gov/citations/20040111310
[research_karrastj_1969]: https://ntrs.nasa.gov/citations/19700003436
[research_karthikeyan_aravindhkumar_2016]: https://doi.org/10.14445/22315381/ijett-v36p265
[research_karthikeyan_verma_2009]: https://doi.org/10.2514/6.2009-3375
[research_kassnerdl_wettlauferb_1977]: https://ntrs.nasa.gov/citations/19770023139
[research_kassoy_1997]: https://doi.org/10.21236/ada329605
[research_kato_yamada_2021]: https://doi.org/10.1299/jsmemecj.2021.j191-04
[research_katsareliscolton_chenpo_2019]: https://ntrs.nasa.gov/citations/20200001007
[research_katzellisr_1947]: https://ntrs.nasa.gov/citations/19930085698
[research_katzellisr_1949]: https://ntrs.nasa.gov/citations/19930086060
[research_kawai_hasegawa_2024]: https://doi.org/10.1115/hvis2024-071
[research_kawamura_1952]: https://doi.org/10.1143/jpsj.7.486
[research_kawamura_karashima_1957]: https://doi.org/10.2322/jjsass1953.5.93
[research_kawasaki_yokoo_2020]: https://doi.org/10.1299/jsmemecj.2020.j19106
[research_kawatsu_tsutsumi_2020]: https://doi.org/10.2514/6.2020-1624
[research_kazeminejadb_atkinsondh_2005]: https://ntrs.nasa.gov/citations/20070014661
[research_keast_1960]: https://doi.org/10.1121/1.1935199
[research_keast_1961]: https://doi.org/10.1121/1.2369436
[research_kegenbekov_saparova_2022]: https://doi.org/10.1016/j.trpro.2022.01.067
[research_keith_1995]: https://doi.org/10.2514/6.1995-3090
[research_keithel_rothschildwj_1998]: https://ntrs.nasa.gov/citations/19990007761
[research_keithel_rothschildwj_1999]: https://ntrs.nasa.gov/citations/20000021515
[research_kelly_charania_2009]: https://doi.org/10.2514/6.2009-6484
[research_kellygm_mcconnelljg_1985]: https://ntrs.nasa.gov/citations/19870008386
[research_keltner_bainbridge_1988]: https://doi.org/10.1115/1.3250470
[research_kennedypaul_simsherb_2000]: https://ntrs.nasa.gov/citations/20000039786
[research_kennethjdavidian_ronaldhdieck_1987]: https://ntrs.nasa.gov/citations/19870019169
[research_kennethmcafee_hannahalpert]: https://ntrs.nasa.gov/citations/20250004821
[research_kennyjeremy_hobbschris_2009]: https://ntrs.nasa.gov/citations/20090023641
[research_kennyrjeremy_leeerik_2011]: https://ntrs.nasa.gov/citations/20120002611
[research_kentfrankovich_mahadevankrishnan]: https://ntrs.nasa.gov/citations/20240004696
[research_kentfrankovich_mahadevankrishnan_b]: https://ntrs.nasa.gov/citations/20240003624
[research_kerzhanovichviktor_pichkhadzekonstantin_2003]: https://ntrs.nasa.gov/citations/20060043864
[research_keyhanim_1993]: https://ntrs.nasa.gov/citations/19940022647
[research_khairulbmqzaman_amyffagan_2023]: https://ntrs.nasa.gov/citations/20230007194
[research_khairulbmqzaman_amyffagan_2024]: https://ntrs.nasa.gov/citations/20230016105
[research_khairulbmqzaman_johnhkorth]: https://ntrs.nasa.gov/citations/20240003177
[research_khairulbmqzaman_johnhkorth_2025]: https://ntrs.nasa.gov/citations/20250002232
[research_khairulzaman_amyfagan]: https://ntrs.nasa.gov/citations/20220008941
[research_khalid_qureshi_2025]: https://doi.org/10.1016/j.paerosci.2025.101132
[research_khalil_abdalla_2009]: https://doi.org/10.21608/asat.2009.23742
[research_khamlak_2026]: https://doi.org/10.37547/tajet/book-26-01
[research_khatun_laitinen_2013]: https://doi.org/10.1109/lawp.2013.2281912
[research_khavarana_dasap_1996]: https://ntrs.nasa.gov/citations/19960028090
[research_kibbey_2024]: https://doi.org/10.2514/6.2024-0212
[research_kidd_1981]: https://doi.org/10.21236/ada107729
[research_kijima_mitsukura_2013]: https://doi.org/10.1109/spc.2013.6735133
[research_kim_2005]: https://doi.org/10.1063/1.1925146
[research_kim_2026]: https://doi.org/10.5762/kais.2026.27.6.113
[research_kim_keidar_2008]: https://doi.org/10.2514/1.37395
[research_kim_ko_2026]: https://doi.org/10.2514/6.2026-1707
[research_kim_woldeyohannis_2024]: https://doi.org/10.52202/078373-0082
[research_kim_yoo_2001]: https://doi.org/10.2514/6.2001-1232
[research_kimjungho_bentonjohn_2000]: https://ntrs.nasa.gov/citations/20010020434
[research_king_1976]: https://doi.org/10.21236/adb010373
[research_kingel_shafferhw_1968]: https://ntrs.nasa.gov/citations/19690041112
[research_kingmichaelc_bognarjohn_2016]: https://ntrs.nasa.gov/citations/20170000228
[research_kinmanpw_1983]: https://ntrs.nasa.gov/citations/19830028036
[research_kinneyfrank_1997]: https://ntrs.nasa.gov/citations/19990025331
[research_kintnerpm_arnoldyr_1997]: https://ntrs.nasa.gov/citations/19980197385
[research_kinzie_mclaughlin_1997]: https://doi.org/10.1063/1.869319
[research_kirby_martinez_1977]: https://doi.org/10.2514/6.1977-968
[research_kirbyrandyl_manndavid_2003]: https://ntrs.nasa.gov/citations/20110023789
[research_kiriscetin_chanwilliam_2001]: https://ntrs.nasa.gov/citations/20020060457
[research_kiriscetin_chanwilliam_2002]: https://ntrs.nasa.gov/citations/20020073408
[research_kiriscetin_williamsrobert_2000]: https://ntrs.nasa.gov/citations/20000064625
[research_kirkhamharold_1992]: https://ntrs.nasa.gov/citations/19920000278
[research_kirsch_schuhmann_2012]: https://doi.org/10.1109/aps.2012.6348745
[research_kirschbaum_sheridan_1966]: https://doi.org/10.2514/6.1966-1005
[research_kitsche_2010]: https://doi.org/10.1007/978-3-642-10565-4_2
[research_kitsios_lygeros]: https://doi.org/10.1109/cdc.2005.1582797
[research_kless_aftosmis_2011]: https://doi.org/10.2514/6.2011-3666
[research_kluever_horneman_2005]: https://doi.org/10.2514/6.2005-6058
[research_kluever_horneman_2009]: https://doi.org/10.2514/6.2009-5766
[research_knacke_1985]: https://doi.org/10.21236/ada157839
[research_knapp_1999]: https://doi.org/10.2514/6.1999-4932
[research_knaur_1966]: https://doi.org/10.4271/660452
[research_knaur_1967]: https://doi.org/10.2514/6.1967-909
[research_knaur_1968]: https://doi.org/10.2514/3.29291
[research_knight_tso_2005]: https://doi.org/10.2514/6.2005-4735
[research_knipp_street_2006]: https://doi.org/10.1016/j.sna.2006.02.007
[research_knopfwilliamp_2007]: https://ntrs.nasa.gov/citations/20080009481
[research_knottpr_blozyjt_1981]: https://ntrs.nasa.gov/citations/19810008335
[research_knottpr_brauschjf_1980]: https://ntrs.nasa.gov/citations/19810009476
[research_knottpr_janardanba_1981]: https://ntrs.nasa.gov/citations/19830010137
[research_knottpr_janardanba_1984]: https://ntrs.nasa.gov/citations/19870001320
[research_knuth_gramer_1999]: https://doi.org/10.2514/6.1999-2491
[research_kochergin_shi_2009]: https://doi.org/10.2514/6.2009-1939
[research_kochetova_levenets_2026]: https://doi.org/10.38161/1996-3440-2026-2-39-44
[research_koeberleinernestiii_pendershawexum_1994]: https://ntrs.nasa.gov/citations/19950010790
[research_koelle_1981]: https://doi.org/10.1016/0094-5765(81)90118-1
[research_koelle_1984]: https://doi.org/10.1016/0094-5765(84)90100-0
[research_koelle_1992]: https://doi.org/10.2514/6.1992-1281
[research_koelle_1998]: https://doi.org/10.1023/a:1009916211298
[research_koernerma_1984]: https://ntrs.nasa.gov/citations/19840017833
[research_koernerma_1989]: https://ntrs.nasa.gov/citations/19890018529
[research_koester_meltzer_1998]: https://doi.org/10.2172/8701
[research_kohtake_kawabata_2000]: https://doi.org/10.1007/978-94-010-0894-5_37
[research_kokuyama_shimoda_2022]: https://doi.org/10.1016/j.measurement.2022.112044
[research_komar_christenson_1996]: https://doi.org/10.2514/6.1996-4246
[research_konda_singla_2011]: https://doi.org/10.1115/1.4004072
[research_konigsberge_1976]: https://ntrs.nasa.gov/citations/19760022259
[research_konkin_kolesenkov_2018]: https://doi.org/10.1109/meco.2018.8406068
[research_konno_kishimoto_1998]: https://doi.org/10.1063/1.54720
[research_koomphati_2017]: https://doi.org/10.1109/acdt.2017.7886174
[research_korkegi_freeman_1976]: https://doi.org/10.2514/3.7206
[research_korte_2000]: https://doi.org/10.2514/6.2000-1044
[research_korte_salas_1997]: https://doi.org/10.2514/6.1997-3374
[research_korte_salas_2001]: https://doi.org/10.2514/2.5712
[research_kortejj_salasao_1997]: https://ntrs.nasa.gov/citations/19970014941
[research_korting_reitsma_1985]: https://doi.org/10.1002/prep.19850100603
[research_koschel_1998]: https://doi.org/10.1016/s0360-3199(97)00088-8
[research_kosmann_dionne_1978]: https://doi.org/10.2514/6.1978-1076
[research_kostromin_sokolov_2001]: https://doi.org/10.2514/6.2001-1925
[research_kothapalli_2022]: https://doi.org/10.21275/sr24608141108
[research_kothari_webber_2010]: https://doi.org/10.2514/6.2010-8600
[research_kowh_hynecekj_1979]: https://ntrs.nasa.gov/citations/19790042061
[research_kraft_1975]: https://doi.org/10.6028/nbs.tn.856
[research_kral_horn_2009]: https://doi.org/10.2514/6.2009-1917
[research_kranz_english_2016]: https://doi.org/10.1109/aero.2016.7500907
[research_krause_blum_2004]: https://doi.org/10.1103/physrevlett.93.021103
[research_krebsrichardp_hartclinte_1959]: https://ntrs.nasa.gov/citations/19980232087
[research_krejci_petri_2017]: https://doi.org/10.1109/tim.2017.2749798
[research_kriscetinc_kwakdochan_2001]: https://ntrs.nasa.gov/citations/20010090466
[research_krishnamoorthy_marius_2025]: https://doi.org/10.1016/b978-0-443-22118-7.00007-5
[research_krishnamurthy_shende_2013]: https://doi.org/10.2514/6.2013-3023
[research_kristinarojdev_antonywilliams]: https://ntrs.nasa.gov/citations/20205006126
[research_kristinarojdev_jennydevolites]: https://ntrs.nasa.gov/citations/20205008338
[research_krystek_2000]: https://doi.org/10.1088/0957-0233/12/1/308
[research_ksica_hadas_2018]: https://doi.org/10.1109/metroaerospace.2018.8453610
[research_kubom_kanor_2014]: https://ntrs.nasa.gov/citations/20150001406
[research_kulickjh_1970]: https://ntrs.nasa.gov/citations/19710030292
[research_kulkarni_achenbach_2008]: https://doi.org/10.1177/1475921707081973
[research_kumakawa_onodera_1998]: https://doi.org/10.2514/6.1998-3526
[research_kumar_gopalsamy_2017]: https://doi.org/10.1109/icraae.2017.8297246
[research_kumar_mishra_2012]: https://doi.org/10.2514/1.c031254
[research_kumar_misra_2011]: https://doi.org/10.14429/dsj.61.481
[research_kumarmishra_goswami_2021]: https://doi.org/10.33564/ijeast.2021.v05i11.018
[research_kunz_1967]: https://doi.org/10.21236/ad0824527
[research_kuo_kokal_1993]: https://doi.org/10.2514/6.1993-2310
[research_kuokennethk_luyc_1994]: https://ntrs.nasa.gov/citations/19950002772
[research_kurbjunmaxc_1954]: https://ntrs.nasa.gov/citations/19930088099
[research_kurbjunmaxc_thompsonjimrogers_1952]: https://ntrs.nasa.gov/citations/19930087074
[research_kurita_jourdaine_2020]: https://doi.org/10.2514/6.2020-0688
[research_kurtenbachaj_wintzpa_1967]: https://ntrs.nasa.gov/citations/19680004479
[research_kurtenbachaj_wintzpa_1968]: https://ntrs.nasa.gov/citations/19680063940
[research_kutschera_render_1999]: https://doi.org/10.2514/6.1999-4020
[research_kutter_2006]: https://doi.org/10.2514/6.2006-7271
[research_kuzin_lozin_2009]: https://doi.org/10.2514/6.2009-6732
[research_kuzuu_kitamura_2011]: https://doi.org/10.2514/6.2011-3367
[research_labelleremi_bernardoabner_2009]: https://ntrs.nasa.gov/citations/20150011985
[research_lacarnarj_wissingerdb_1982]: https://ntrs.nasa.gov/citations/19830047988
[research_lacefield_sprow_1994]: https://doi.org/10.2514/6.1994-3397
[research_lacroixwp_1973]: https://ntrs.nasa.gov/citations/19740030199
[research_ladeinde_chen_2010]: https://doi.org/10.2514/6.2010-6593
[research_laera_2015]: https://doi.org/10.1016/j.egypro.2015.11.840
[research_lagouanelle_gall_2024]: https://doi.org/10.1109/cefc61729.2024.10585626
[research_lai_wei_2018]: https://doi.org/10.1017/jmech.2018.18
[research_lakey_schlippe_2024]: https://doi.org/10.1109/scc61854.2024.00009
[research_lamb_1987]: https://doi.org/10.21236/ada186714
[research_lan_li_2022]: https://doi.org/10.1088/1742-6596/2364/1/012013
[research_lancelle_bozic_2012]: https://doi.org/10.1109/eml.2012.6325034
[research_landers_hall_2003]: https://doi.org/10.2514/6.2003-3805
[research_landing_gear]: https://doi.org/10.4271/air6168a
[research_lane_redman_1970]: https://doi.org/10.2514/6.1970-1380
[research_langeko_bellevillere_1975]: https://ntrs.nasa.gov/citations/19750050312
[research_langilljr_1965]: https://doi.org/10.2514/6.1965-205
[research_langner_gupta_2024]: https://doi.org/10.2514/6.2024-2608
[research_lanin_2012]: https://doi.org/10.1007/978-3-642-32430-7_8
[research_lanin_2012_b]: https://doi.org/10.1007/978-3-642-32430-7_1
[research_laporte_perlin_2025]: https://doi.org/10.5194/egusphere-egu24-12248
[research_larin_2012]: https://doi.org/10.33577/2312-4458.6.2012.42-49
[research_larina_1985]: https://doi.org/10.1007/bf01091056
[research_larsen_2000]: https://doi.org/10.2514/6.2000-5114
[research_larsen_2003]: https://doi.org/10.2514/6.2003-6407
[research_larsen_2005]: https://doi.org/10.2514/6.2005-6795
[research_larsenmf_2003]: https://ntrs.nasa.gov/citations/20030053432
[research_larson_1973]: https://doi.org/10.2514/6.1973-1176
[research_larsonrichardr_1999]: https://ntrs.nasa.gov/citations/19990090017
[research_lash_moeller_2015]: https://doi.org/10.2514/6.2015-3979
[research_laubacherbriana_2000]: https://ntrs.nasa.gov/citations/20000064699
[research_launch_of_2014]: https://doi.org/10.1063/pt.5.027763
[research_launch_vehicle]: https://doi.org/10.1007/978-3-540-75553-1_3
[research_launch_vehicle_1963]: https://doi.org/10.2514/5.9781600864834.0167.0182
[research_launch_vehicle_2022]: https://doi.org/10.2514/5.9781624106422.0825.0906
[research_launch_vehicle_2022_b]: https://doi.org/10.2514/5.9781624106422.0271.0336
[research_laurengriggs_jacobmoseley]: https://ntrs.nasa.gov/citations/20230008005
[research_lawrence_2005]: https://doi.org/10.21236/ada430931
[research_lawsondenisel_jamesmarkl_1989]: https://ntrs.nasa.gov/citations/19890017223
[research_lawsondenisel_jamesmarkl_1989_b]: https://ntrs.nasa.gov/citations/19900009128
[research_lazarev_tarabrin_2017]: https://doi.org/10.1364/fio.2017.jw4a.85
[research_lazur_sawyer_1999]: https://doi.org/10.2514/6.1999-4864
[research_lazzarin_bellomo_2012]: https://doi.org/10.2514/6.2012-4174
[research_le_yu_2015]: https://doi.org/10.1117/12.2084036
[research_leachmanjonathan_2010]: https://ntrs.nasa.gov/citations/20100023366
[research_lechterss_1964]: https://ntrs.nasa.gov/citations/19650011378
[research_lederer_2021]: https://doi.org/10.25368/2022.406
[research_lee_1963]: https://doi.org/10.21236/ad0406455
[research_lee_1964]: https://doi.org/10.21236/ad0614626
[research_lee_2020]: https://doi.org/10.1117/12.2557969
[research_lee_2026]: https://doi.org/10.2514/6.2026-114331
[research_lee_jo_2026]: https://doi.org/10.3390/aerospace13010079
[research_lee_lee_2020]: https://doi.org/10.1155/2020/7515139
[research_lee_olds_1997]: https://doi.org/10.2514/6.1997-3911
[research_lee_pomerantz_2015]: https://doi.org/10.2514/6.2015-4468
[research_leeallany_strahanalan_2010]: https://ntrs.nasa.gov/citations/20150008899
[research_leecc_1966]: https://ntrs.nasa.gov/citations/19660053186
[research_leehyunh_2012]: https://ntrs.nasa.gov/citations/20130009386
[research_leejonathana_elamsandy_2001]: https://ntrs.nasa.gov/citations/20010041325
[research_leer_1976]: https://ntrs.nasa.gov/citations/19770011078
[research_leese_1966]: https://doi.org/10.21236/ad0633264
[research_lei_chen_2026]: https://doi.org/10.1016/j.ast.2026.112317
[research_lei_hongbo_2019]: https://doi.org/10.1109/cac48633.2019.8996784
[research_lei_yan_2017]: https://doi.org/10.2514/6.2017-2256
[research_lei_zhang_2022]: https://doi.org/10.1016/j.cja.2021.08.001
[research_leijihfen_willherberta_1998]: https://ntrs.nasa.gov/citations/19980237139
[research_leitner_1986]: https://doi.org/10.21236/ada522372
[research_lelandhjorgensen_jrichardspahr_1962]: https://ntrs.nasa.gov/citations/19720065133
[research_lemasterra_runyanrb_1983]: https://ntrs.nasa.gov/citations/19840007535
[research_lemberger_patanchon_1991]: https://doi.org/10.2514/6.1991-1949
[research_lemieux_2009]: https://doi.org/10.2514/6.2009-3720
[research_lemieux_murray_2012]: https://doi.org/10.2514/6.2012-4201
[research_lengade_2021]: https://doi.org/10.1115/1.0004344v
[research_lengchristopher_peetarthur_1988]: https://ntrs.nasa.gov/citations/19890043683
[research_lerchba_nathalmv_2002]: https://ntrs.nasa.gov/citations/20020061400
[research_leshojefferyc_eatonharryac_1993]: https://ntrs.nasa.gov/citations/19930012973
[research_lesieutre_lesieutre_1994]: https://doi.org/10.2514/6.1994-1913
[research_lesterdaniel_1994]: https://ntrs.nasa.gov/citations/19950015337
[research_letchworth_2011]: https://doi.org/10.2514/6.2011-7314
[research_letchworth_letchworth_2000]: https://doi.org/10.2514/6.2000-5141
[research_levenets_2018]: https://doi.org/10.1088/1742-6596/944/1/012074
[research_levenets_bogachev_2017]: https://doi.org/10.1109/sibcon.2017.7998593
[research_levinejack_martzcwilliam_1960]: https://ntrs.nasa.gov/citations/19980227768
[research_levitan_buchsbaum_1996]: https://doi.org/10.1364/josaa.13.001152
[research_lewak_1967]: https://doi.org/10.2514/6.1967-1314
[research_lewallenpat_1987]: https://ntrs.nasa.gov/citations/19880004248
[research_lewismarke_gibsontracyl_2019]: https://ntrs.nasa.gov/citations/20190025248
[research_lewistl_dodsjbjr_1972]: https://ntrs.nasa.gov/citations/19720025737
[research_li_an_2022]: https://doi.org/10.1016/j.jcp.2022.111599
[research_li_chen_2022]: https://doi.org/10.1109/icceai55464.2022.00160
[research_li_fan_2011]: https://doi.org/10.1016/j.expthermflusci.2010.09.014
[research_li_long_2022]: https://doi.org/10.1155/2022/9104823
[research_li_paik_2026]: https://doi.org/10.2514/6.2026-1709
[research_li_qiao_2021]: https://doi.org/10.1007/978-981-15-8155-7_120
[research_li_ren_2026]: https://doi.org/10.2139/ssrn.7162268
[research_li_schemel_2002]: https://doi.org/10.2514/6.2002-2521
[research_li_sun_2018]: https://doi.org/10.3390/s18082676
[research_li_wu_2017]: https://doi.org/10.1061/(asce)as.1943-5525.0000757
[research_li_xing_2020]: https://doi.org/10.1109/iai50351.2020.9262185
[research_li_yang_2020]: https://doi.org/10.12783/dtetr/amee2019/33456
[research_li_yang_2020_b]: https://doi.org/10.2174/1872212113666190110124551
[research_li_zhang_2019]: https://doi.org/10.1109/phm-qingdao46334.2019.8942998
[research_li_zhao_2025]: https://doi.org/10.52202/083090-0094
[research_lian_bai_2013]: https://doi.org/10.1109/imccc.2013.328
[research_lian_liangji_2026]: https://doi.org/10.2514/6.2026-3410
[research_lian_wang_2026]: https://doi.org/10.2139/ssrn.7267293
[research_liaoniwu_yiminhuang_2008]: https://doi.org/10.1109/isscaa.2008.4776287
[research_lieske_kochenderfer_1966]: https://doi.org/10.21236/ad0809790
[research_ligranipm_baunlr_1989]: https://ntrs.nasa.gov/citations/19890058538
[research_liguojun_shijian_2013]: https://doi.org/10.1109/mec.2013.6885497
[research_lijewski_1980]: https://doi.org/10.21236/ada104989
[research_lijewski_1981]: https://doi.org/10.2514/6.1981-222
[research_lijewski_1982]: https://doi.org/10.2514/3.56197
[research_lilleyrw_1974]: https://ntrs.nasa.gov/citations/19750003839
[research_limtaew_1991]: https://ntrs.nasa.gov/citations/19910047502
[research_limtaew_1992]: https://ntrs.nasa.gov/citations/19920049564
[research_lin]: https://doi.org/10.1109/icsmc.1989.71490
[research_lin_1989]: https://doi.org/10.2514/6.1989-3193
[research_lin_figueroa_2010]: https://doi.org/10.2514/6.2010-3356
[research_lin_huang_2003]: https://doi.org/10.2514/2.3912
[research_lin_wu_2020]: https://doi.org/10.1109/icicsp50920.2020.9232079
[research_lin_yang_2023]: https://doi.org/10.3390/aerospace10060517
[research_lincf_figueroaf_2009]: https://ntrs.nasa.gov/citations/20090040299
[research_linchujen_lonskeben_2007]: https://ntrs.nasa.gov/citations/20090041687
[research_lindgren_buynak_2011]: https://doi.org/10.21236/ada554425
[research_lindsay_jordan_1975]: https://doi.org/10.21236/ada009137
[research_lineberry_coleman_2004]: https://doi.org/10.2514/6.2004-4002
[research_lioularryc_1999]: https://ntrs.nasa.gov/citations/20050188516
[research_liquid_propellant_2006]: https://doi.org/10.2514/5.9781600868870.0293.0302
[research_liquid_propellant_rocket_2005]: https://doi.org/10.1002/0471743984.vse4619
[research_liquid_rocket]: https://doi.org/10.4271/arp4900
[research_liquid_rocket_1976]: https://ntrs.nasa.gov/citations/19770009165
[research_liquid_rocket_1995]: https://doi.org/10.2514/4.866371
[research_liquid_rocket_2018]: https://doi.org/10.4271/0768093333
[research_liquid_rocket_2019]: https://doi.org/10.1017/9781108381376.009
[research_lisanomichaele_jahmoriba_2004]: https://ntrs.nasa.gov/citations/20210001741
[research_lisanomichaele_jahmoriba_2004_b]: https://ntrs.nasa.gov/citations/20210001055
[research_littjonathans_musgravejeffreyl_1994]: https://ntrs.nasa.gov/citations/19950010859
[research_little_1992]: https://doi.org/10.1007/978-94-011-2330-3_3
[research_littlefieldalanc_meltongregorys_1999]: https://ntrs.nasa.gov/citations/20000024930
[research_littlefieldalanc_meltongregorys_2000]: https://ntrs.nasa.gov/citations/20000048412
[research_litvin_dudley_2012]: https://doi.org/10.1364/oe.20.010996
[research_liu_2009]: https://doi.org/10.1177/1475921708102144
[research_liu_2023]: https://doi.org/10.14293/p2199-8442.1.sop-.paqumr.v1
[research_liu_2024]: https://doi.org/10.2514/6.2024-83778
[research_liu_cheng_2022]: https://doi.org/10.1016/j.ast.2021.107300
[research_liu_cheng_2026]: https://doi.org/10.2139/ssrn.6931999
[research_liu_dai_2017]: https://doi.org/10.2514/6.2017-2284
[research_liu_gao_2008]: https://doi.org/10.1016/j.jsv.2008.03.026
[research_liu_guo_2026]: https://doi.org/10.1016/j.ast.2026.113118
[research_liu_guo_2026_b]: https://doi.org/10.1016/j.jppr.2026.06.003
[research_liu_hou_2010]: https://doi.org/10.1109/isscaa.2010.5633608
[research_liu_liu_2025]: https://doi.org/10.1155/ijae/7726555
[research_liu_lu_2024]: https://doi.org/10.1109/icct62411.2024.10946509
[research_liu_maurer_2005]: https://doi.org/10.1063/1.2018628
[research_liu_tan_2024]: https://doi.org/10.3390/act13090371
[research_liu_zhang_2001]: https://doi.org/10.2514/6.2001-3704
[research_liu_zhang_2025]: https://doi.org/10.1016/j.rineng.2025.107160
[research_liu_zhu_2025]: https://doi.org/10.3390/aerospace12100899
[research_liuchungchiun_1994]: https://ntrs.nasa.gov/citations/19950011480
[research_liug_1985]: https://ntrs.nasa.gov/citations/19860019800
[research_liux_2015]: https://ntrs.nasa.gov/citations/20160007329
[research_livingstone_1974]: https://doi.org/10.1111/j.1475-1305.1974.tb00091.x
[research_lizcano_martinez_2026]: https://doi.org/10.1016/j.ast.2026.113253
[research_lobdell_1968]: https://doi.org/10.1109/t-su.1968.29476
[research_lobdell_1969]: https://doi.org/10.1016/0041-624x(69)90593-9
[research_lockejustinm_landrumdbrian_2005]: https://ntrs.nasa.gov/citations/20050210090
[research_loesch_pawlowski_1973]: https://doi.org/10.2514/6.1973-759
[research_logsdon_williamson_1997]: https://doi.org/10.1016/s0265-9646(97)00010-6
[research_lohrerjd_wrightrd_2016]: https://ntrs.nasa.gov/citations/20160001838
[research_lokersondc_1966]: https://ntrs.nasa.gov/citations/19670007297
[research_lomaxharvard_1957]: https://ntrs.nasa.gov/citations/19930092292
[research_london_epstein_2000]: https://doi.org/10.2514/6.2000-3164
[research_long_joyner_2013]: https://doi.org/10.2514/6.2013-5375
[research_long_li_2026]: https://doi.org/10.1016/j.asr.2026.03.053
[research_longenecker_clark_2007]: https://doi.org/10.2514/6.2007-162
[research_lopatoffmitchell_1951]: https://ntrs.nasa.gov/citations/19930086701
[research_lopes_silva_2005]: https://doi.org/10.1002/0470869097.ch8
[research_loposerjdan_mottardelmoj_1953]: https://ntrs.nasa.gov/citations/19930083591
[research_lord_1978]: https://doi.org/10.2514/6.1978-1706
[research_lorenzo_1995]: https://doi.org/10.2514/6.1995-3123
[research_lorenzo_merrill]: https://doi.org/10.1109/acc.1995.532672
[research_lorenzocarlf_holmesmichaels_1998]: https://ntrs.nasa.gov/citations/19980174904
[research_lorenzocarlf_musgravejeffreyl_1991]: https://ntrs.nasa.gov/citations/19920004056
[research_loriola_1970]: https://ntrs.nasa.gov/citations/19700009398
[research_losik_2008]: https://doi.org/10.2514/6.2008-7698
[research_losik_2010]: https://doi.org/10.2514/6.2010-8757
[research_losik_2010_b]: https://doi.org/10.2514/6.2010-8753
[research_losik_2010_c]: https://doi.org/10.2514/6.2010-8752
[research_losik_2012]: https://doi.org/10.1109/aero.2012.6187371
[research_losik_2012_b]: https://doi.org/10.1109/aero.2012.6187384
[research_losik_2012_c]: https://doi.org/10.1109/aero.2012.6187383
[research_losikphd_2012]: https://doi.org/10.2514/6.2012-5197
[research_loubeyrejeanphilippe_1994]: https://ntrs.nasa.gov/citations/19950010831
[research_loveeugenes_colettidonalde_1952]: https://ntrs.nasa.gov/citations/19930087258
[research_lovellrr_nieberdingwc_1966]: https://ntrs.nasa.gov/citations/19660013633
[research_lowe]: https://doi.org/10.17918/00002557
[research_lowpw_1977]: https://ntrs.nasa.gov/citations/19770024265
[research_loydjr_pickardrf_1967]: https://ntrs.nasa.gov/citations/19670008673
[research_lu_1997]: https://doi.org/10.2514/2.4008
[research_lu_wang_2013]: https://doi.org/10.1504/ijmic.2013.055657
[research_lu_zhou_2017]: https://doi.org/10.1109/ccdc.2017.7978461
[research_luan_tang_2010]: https://doi.org/10.1007/978-3-642-16527-6_6
[research_luan_xue_2024]: https://doi.org/10.1109/isstc63573.2024.10824188
[research_lucci_hodson_1975]: https://doi.org/10.2514/6.1975-1238
[research_lucht_charest_1996]: https://doi.org/10.1063/1.50767
[research_luckert_1973]: https://doi.org/10.2514/6.1973-295
[research_ludwig_gruber_2025]: https://doi.org/10.1016/j.measen.2024.101790
[research_ludwiggeorgeh_1961]: https://ntrs.nasa.gov/citations/19980227785
[research_lugorafaela_karlgaardchristopherd_2018]: https://ntrs.nasa.gov/citations/20190000444
[research_lugorafaela_tolsonroberth_2013]: https://ntrs.nasa.gov/citations/20130003195
[research_luicy_masondr_1991]: https://ntrs.nasa.gov/citations/19910057123
[research_lukegaryd_dwyerharrya_1992]: https://ntrs.nasa.gov/citations/19920023002
[research_lukin_prisiazhnyi_2021]: https://doi.org/10.1088/1742-6596/1786/1/012021
[research_lumbdr_1971]: https://ntrs.nasa.gov/citations/19710000200
[research_lumbdr_viterbiaj_1971]: https://ntrs.nasa.gov/citations/19720028466
[research_luo_kareem_2021]: https://doi.org/10.1061/(asce)em.1943-7889.0001904
[research_luo_tan_2019]: https://doi.org/10.1088/1742-6596/1213/4/042065
[research_luton_1963]: https://doi.org/10.2514/6.1963-1409
[research_lv_yu_2012]: https://doi.org/10.11591/telkomnika.v10i8.1692
[research_lydon_va_1995]: https://doi.org/10.2514/6.1995-2943
[research_lynchtj_1967]: https://ntrs.nasa.gov/citations/19670060221
[research_lynchtj_1967_b]: https://ntrs.nasa.gov/citations/19670018285
[research_lyonincdetroitmi_1963]: https://doi.org/10.21236/ad0401194
[research_lyonsjt_1993]: https://ntrs.nasa.gov/citations/19930018403
[research_m_ka_2025]: https://doi.org/10.46254/in05.20250319
[research_ma_bao_2023]: https://doi.org/10.1016/j.ast.2023.108464
[research_ma_deng_2005]: https://doi.org/10.2514/6.2005-4973
[research_ma_pan_2022]: https://doi.org/10.1016/j.ast.2021.107234
[research_ma_tang_2013]: https://doi.org/10.4028/www.scientific.net/kem.562-565.166
[research_ma_wang_2018]: https://doi.org/10.1080/0305215x.2018.1472774
[research_ma_wang_2019]: https://doi.org/10.1109/ccdc.2019.8832563
[research_macagno_hsieh_1963]: https://doi.org/10.21236/ad0408685
[research_macbeth_1989]: https://doi.org/10.2514/6.1989-2403
[research_macconochieiano_breinercharlesa_1989]: https://ntrs.nasa.gov/citations/19900007465
[research_macconochieiano_brienercharlesa_1991]: https://ntrs.nasa.gov/citations/20080004393
[research_macconochieiano_martinjamesa_1989]: https://ntrs.nasa.gov/citations/19890017507
[research_macgregorca_1982]: https://ntrs.nasa.gov/citations/19820008299
[research_machdm_koshakwj_2006]: https://ntrs.nasa.gov/citations/20070001545
[research_machdm_koshakwj_2007]: https://ntrs.nasa.gov/citations/20080018897
[research_mackalld_sakaharar_1998]: https://ntrs.nasa.gov/citations/19990102220
[research_mackey_krasowski_2009]: https://doi.org/10.2514/6.2009-4974
[research_mackey_kulikov_2010]: https://doi.org/10.36001/phmconf.2010.v2i1.1803
[research_mackeyjon_sehirlioglualp_2014]: https://ntrs.nasa.gov/citations/20140010867
[research_mackeyjon_sehirlioglualp_2014_b]: https://ntrs.nasa.gov/citations/20140012564
[research_maclean_rodriguez_1996]: https://doi.org/10.2514/6.1996-3228
[research_macmedanml_1985]: https://ntrs.nasa.gov/citations/19850000287
[research_madsenboydd_1987]: https://ntrs.nasa.gov/citations/19880046412
[research_madzsar_bickford_1994]: https://doi.org/10.2514/6.1994-2985
[research_madzsargc_bickfordrl_1992]: https://ntrs.nasa.gov/citations/19920019174
[research_maestrellol_1978]: https://ntrs.nasa.gov/citations/19790005649
[research_magier_merda_2017]: https://doi.org/10.5604/01.3001.0009.8982
[research_magnani_sozio_2026]: https://doi.org/10.2514/6.2026-5053
[research_mahapatra_sriram_2008]: https://doi.org/10.1017/s0001924000590009
[research_maharajarishabh_2016]: https://ntrs.nasa.gov/citations/20160013619
[research_mahmood_zulfiqar_2026]: https://doi.org/10.2139/ssrn.6776460
[research_mahoneym_quannjj_1964]: https://ntrs.nasa.gov/citations/19670005583
[research_mahzarimilad_whitetodd_2017]: https://ntrs.nasa.gov/citations/20170011049
[research_mai_vogt_2013]: https://doi.org/10.1115/1.4025485
[research_mainini_2017]: https://doi.org/10.12783/shm2017/14035
[research_mains_2011]: https://doi.org/10.2514/6.2011-7290
[research_majumdaralok_flachbartrobin_2003]: https://ntrs.nasa.gov/citations/20030065836
[research_majumdaralok_polsgroverobert_2000]: https://ntrs.nasa.gov/citations/20000095567
[research_malik_salauddin_2023]: https://doi.org/10.2514/6.2023-1872
[research_mallonjosephrjr_1992]: https://ntrs.nasa.gov/citations/19930004488
[research_malonemichaelb_peaveycharlesc_1999]: https://ntrs.nasa.gov/citations/20000044629
[research_maluf_hsu]: https://doi.org/10.1007/978-3-540-68123-6_59
[research_mana_pennecchi_2007]: https://doi.org/10.1088/0026-1394/44/3/012
[research_manalonatividadd_smithgl_1991]: https://ntrs.nasa.gov/citations/19930039605
[research_mandal_mukhopadhyay_2023]: https://doi.org/10.1088/1361-6552/ad0778
[research_mandersam_sussmansm_1964]: https://ntrs.nasa.gov/citations/19650010281
[research_manishmehta_andrewcolbert]: https://ntrs.nasa.gov/citations/20260004164
[research_manishmehta_markahooton]: https://ntrs.nasa.gov/citations/20250005672
[research_manishmehta_sheldondsmith]: https://ntrs.nasa.gov/citations/20230017528
[research_manishmehta_thomasbsteva]: https://ntrs.nasa.gov/citations/20230018436
[research_manishmehta_thomassteva]: https://ntrs.nasa.gov/citations/20240000053
[research_manop_tanghengjareon_2025]: https://doi.org/10.21203/rs.3.rs-5981143/v1
[research_mansfielddl_1973]: https://ntrs.nasa.gov/citations/19730016345
[research_manski_fina_1994]: https://doi.org/10.2514/6.1994-3316
[research_manskidetlef_martinjamesa_1988]: https://ntrs.nasa.gov/citations/19880057472
[research_manusubramanian_sumitra_2014]: https://doi.org/10.1109/icices.2014.7034092
[research_mao_sinn_2016]: https://doi.org/10.2514/6.2016-4421
[research_mao_sinn_2016_b]: https://doi.org/10.1016/j.actaastro.2016.06.009
[research_maram_1993]: https://doi.org/10.2514/6.1993-2376
[research_maramj_barkhoudarians_1987]: https://ntrs.nasa.gov/citations/19880045641
[research_marchesevp_1974]: https://ntrs.nasa.gov/citations/19740020110
[research_marchesevp_rakowskyel_1972]: https://ntrs.nasa.gov/citations/19730028684
[research_marchetti_minisci_2021]: https://doi.org/10.1007/s11081-021-09698-w
[research_mari_2009]: https://doi.org/10.1016/j.measurement.2009.01.011
[research_mariosantos_serhathosder]: https://ntrs.nasa.gov/citations/20210022724
[research_marko_mclennan_1961]: https://doi.org/10.21236/ada280149
[research_markowsky_mcmanus_1974]: https://doi.org/10.1016/0045-7930(74)90010-3
[research_marks_1977]: https://doi.org/10.21236/adb019295
[research_markusicte_jonesje_2004]: https://ntrs.nasa.gov/citations/20040085923
[research_marlow_2003]: https://doi.org/10.2514/6.2003-5281
[research_marquez_2013]: https://doi.org/10.21236/ada589831
[research_marsiksj_gawrylowiczht_1986]: https://ntrs.nasa.gov/citations/19860015936
[research_marsiksj_moreasf_1985]: https://ntrs.nasa.gov/citations/19860007935
[research_marsiksj_moreasf_1985_b]: https://ntrs.nasa.gov/citations/19850012921
[research_marsilio_resta_2024]: https://doi.org/10.2514/6.2024-1617.c1
[research_martin_1962]: https://doi.org/10.21236/ad0273826
[research_martin_2006]: https://doi.org/10.2514/6.2006-4960
[research_martin_brazzel_1970]: https://doi.org/10.21236/ad0871913
[research_martin_stay_2024]: https://doi.org/10.1115/imece2024-142760
[research_martincl_1983]: https://ntrs.nasa.gov/citations/19830026740
[research_martindale_2006]: https://doi.org/10.21236/ada457121
[research_martinez_jortner_1964]: https://doi.org/10.2514/6.1964-383
[research_martinez_reinert_1990]: https://doi.org/10.2514/6.1990-2236
[research_martinezelmain_mcauleymyche_2004]: https://ntrs.nasa.gov/citations/20060043240
[research_martinjamesa_1993]: https://ntrs.nasa.gov/citations/19930000593
[research_martinjamesa_kramerrichardd_1990]: https://ntrs.nasa.gov/citations/19910014927
[research_martinjamesa_manskidetlef_1989]: https://ntrs.nasa.gov/citations/19890059353
[research_martinlisac_wrbanekjohnd_2001]: https://ntrs.nasa.gov/citations/20020010158
[research_martlcook_laurentgruet_2003]: https://ntrs.nasa.gov/citations/20030112368
[research_maru_kobayashi_2026]: https://doi.org/10.2514/6.2026-5032
[research_maruyama_matsushima_2006]: https://doi.org/10.2514/6.2006-3323
[research_masdari_tahani_2018]: https://doi.org/10.24200/sci.2018.5065.1072
[research_masilamani_kumar_2018]: https://doi.org/10.18520/cs/v114/i01/84-100
[research_masonsmith_2017]: https://doi.org/10.26226/morressier.59c106e9d462b80292389ec1
[research_masri_2000]: https://doi.org/10.21236/ada387071
[research_masseydavid_corbinbrian_1990]: https://ntrs.nasa.gov/citations/19900000385
[research_masseyde_1986]: https://ntrs.nasa.gov/citations/19870028449
[research_masseyde_corbinb_1991]: https://ntrs.nasa.gov/citations/19910000458
[research_masseyhn_1966]: https://ntrs.nasa.gov/citations/19660022090
[research_mastrocolan_1947]: https://ntrs.nasa.gov/citations/19930085604
[research_mastromatteo_gaverina_2026]: https://doi.org/10.58286/33864
[research_matharu_devi_2020]: https://doi.org/10.1016/j.anucene.2020.107777
[research_matheshb_1980]: https://ntrs.nasa.gov/citations/19810048444
[research_mathewscharlesw_thompsonjimrogers_1947]: https://ntrs.nasa.gov/citations/19930085806
[research_mathisonrp_1965]: https://ntrs.nasa.gov/citations/19650016545
[research_matsukawa_watanabe_2019]: https://doi.org/10.1109/gtdasia.2019.8715873
[research_matsumotot_chiseldm_1976]: https://ntrs.nasa.gov/citations/19760052310
[research_matthewaaronmaybee_2025]: https://ntrs.nasa.gov/citations/20250002850
[research_matthewamaybee_michaelahemming]: https://ntrs.nasa.gov/citations/20240015056
[research_matthewpfritz_javieradoll]: https://ntrs.nasa.gov/citations/20210023718
[research_matthews_1957]: https://doi.org/10.21236/ad0127419
[research_matveev_zubanov_2018]: https://doi.org/10.5220/0006890003650370
[research_maughmerm_ozoroskil_1993]: https://ntrs.nasa.gov/citations/19930057900
[research_maughmerm_straussfogeld_1991]: https://ntrs.nasa.gov/citations/19910062529
[research_maughmermarkd_ozoroskil_1990]: https://ntrs.nasa.gov/citations/19900012418
[research_maurer_1995]: https://doi.org/10.21236/ada300638
[research_maxiaoli_wanglibin_2011]: https://doi.org/10.1109/icetce.2011.5775965
[research_maynard_1969]: https://doi.org/10.2514/6.1969-978
[research_maynardbryont_rainesnickeyg_2010]: https://ntrs.nasa.gov/citations/20100021425
[research_maytodda_creechstephend_2012]: https://ntrs.nasa.gov/citations/20120003874
[research_mazurov_takovitskii_2022]: https://doi.org/10.1134/s0015462822010074
[research_mcamis_1995]: https://doi.org/10.2514/6.1995-2699
[research_mcanally_engel_1979]: https://doi.org/10.2514/6.1979-508
[research_mcclure_1998]: https://doi.org/10.2514/6.1998-5139
[research_mccorkelj_czaplamyersj_2015]: https://ntrs.nasa.gov/citations/20160005179
[research_mccoyke_hesterj_1985]: https://ntrs.nasa.gov/citations/19860000811
[research_mccutcheondavidmatthew_2017]: https://ntrs.nasa.gov/citations/20170005379
[research_mccutcheonep_mirandar_1977]: https://ntrs.nasa.gov/citations/19790010851
[research_mcdonaldkathleenr_wootenjohnr_2000]: https://ntrs.nasa.gov/citations/20000070411
[research_mcdowell_raghu_2025]: https://doi.org/10.1109/aero63441.2025.11068692
[research_mcgarvey_1973]: https://doi.org/10.2514/6.1973-294
[research_mcgarvey_1979]: https://doi.org/10.2514/6.1979-511
[research_mcgeers_saymb_1966]: https://ntrs.nasa.gov/citations/19670032372
[research_mcgrath_1996]: https://doi.org/10.2514/6.1996-3151
[research_mcintosh_knowles_1972]: https://doi.org/10.2514/6.1972-259
[research_mckenna_1981]: https://doi.org/10.21236/ada100267
[research_mckenna_1990]: https://doi.org/10.21236/ada233656
[research_mckinneylinwoodw_1960]: https://ntrs.nasa.gov/citations/20040047039
[research_mclachlanbg_belljh_1992]: https://ntrs.nasa.gov/citations/19940030888
[research_mclafferty_1970]: https://doi.org/10.2514/6.1970-708
[research_mcleodchristopher_2004]: https://ntrs.nasa.gov/citations/20050139065
[research_mcmillin_wood_1986]: https://doi.org/10.2514/6.1986-1799
[research_mcmillin_wood_1987]: https://doi.org/10.2514/3.45529
[research_mcnairll_1962]: https://ntrs.nasa.gov/citations/19730061697
[research_mcnicholrandals_1996]: https://ntrs.nasa.gov/citations/19960022390
[research_mcwhorter_2003]: https://doi.org/10.2514/6.2003-5107
[research_mcwhorter_ewing_2001]: https://doi.org/10.2514/6.2001-3280
[research_mease_teufel_1999]: https://doi.org/10.2514/6.1999-4160
[research_measurement_of]: https://doi.org/10.37473/dac/10.1088/1674-1137/acce28
[research_measurement_uncertainty]: https://doi.org/10.4271/air5925
[research_measurement_uncertainty_2002]: https://doi.org/10.1201/9781420038453.ch7
[research_measurement_uncertainty_2017]: https://doi.org/10.4324/9781315267913-11
[research_measurement_uncertainty_2024]: https://doi.org/10.1515/9783111453712-006
[research_measurement_uncertainty_2024_b]: https://doi.org/10.1017/9781009343657.008
[research_meda_2020]: https://doi.org/10.1088/1742-6596/1507/8/082016
[research_medeliuspedroj_hallbergcarl_1994]: https://ntrs.nasa.gov/citations/19940027954
[research_medeliuspedroj_hallbergcarlg_1998]: https://ntrs.nasa.gov/citations/19980203170
[research_medical_telemetry_1978]: https://ntrs.nasa.gov/citations/20070018908
[research_medlin_1965]: https://doi.org/10.1109/tset.1965.5009633
[research_medukhovskii_1961]: https://doi.org/10.1016/0021-8928(61)90053-3
[research_meeckart_jsadams_2013]: https://ntrs.nasa.gov/citations/20150018285
[research_mehta_dufrene_2014]: https://doi.org/10.2514/6.2014-1255
[research_mehtamanish_canabalfrancisco_2011]: https://ntrs.nasa.gov/citations/20110015765
[research_mehtamanish_knoxkyle_2016]: https://ntrs.nasa.gov/citations/20160001815
[research_meiboom_1993]: https://doi.org/10.2514/6.1993-1214
[research_meiboom_geerdes_1995]: https://doi.org/10.2514/6.1995-1591
[research_meigs_stine_1969]: https://doi.org/10.2514/6.1969-970
[research_meigs_stine_1970]: https://doi.org/10.2514/3.29999
[research_meija_mester_2008]: https://doi.org/10.1088/0026-1394/45/1/008
[research_meisl_1986]: https://doi.org/10.2514/6.1986-1408
[research_meisl_1988]: https://doi.org/10.2514/3.23039
[research_meisl_1989]: https://doi.org/10.2514/6.1989-2412
[research_meisl_1992]: https://doi.org/10.2514/6.1992-3686
[research_mekid_vaja_2008]: https://doi.org/10.1016/j.measurement.2007.07.004
[research_melchior_1990]: https://doi.org/10.2514/6.1990-2052
[research_mellodge_kachroo_2010]: https://doi.org/10.1115/1.4001705
[research_mencattini_rabottino_2009]: https://doi.org/10.1109/amuem.2009.5207603
[research_mencattini_salmeri_2007]: https://doi.org/10.1109/amuem.2007.4362562
[research_menon_2016]: https://doi.org/10.4028/www.scientific.net/aef.16.91
[research_menou]: https://doi.org/10.70675/01a02ab5zdcb3z4b95zb05czfea1b906f3dc
[research_meo_zumpano_2004]: https://doi.org/10.1117/12.540308
[research_meo_zumpano_2005]: https://doi.org/10.1016/j.engstruct.2005.03.015
[research_mercerce_burleyjrii_1985]: https://ntrs.nasa.gov/citations/19860008822
[research_mercerce_salterslbjr_1963]: https://ntrs.nasa.gov/citations/19630006421
[research_meredith_kelly_1981]: https://doi.org/10.2514/3.57843
[research_mermagen_1964]: https://doi.org/10.21236/ad0444246
[research_mermagen_1964_b]: https://doi.org/10.21236/ad0459576
[research_merrill_lorenzo_1988]: https://doi.org/10.2514/6.1988-3114
[research_merrillwalterc_lorenzocarlf_1988]: https://ntrs.nasa.gov/citations/19880017017
[research_merrillwc_musgravejl_1992]: https://ntrs.nasa.gov/citations/19930030657
[research_merrymanhl_smithlr_1974]: https://ntrs.nasa.gov/citations/19750011284
[research_methods_of_2014]: https://doi.org/10.1002/9781118763032.ch06
[research_meyer_elko_2008]: https://doi.org/10.1109/hscma.2008.4538672
[research_meyerclaudiam_2000]: https://ntrs.nasa.gov/citations/20050192361
[research_meyers_lu_2003]: https://doi.org/10.2514/6.2003-1173
[research_meyerson_1998]: https://doi.org/10.1061/40339(206)21
[research_meyn_2000]: https://doi.org/10.2514/6.2000-149
[research_micci_1975]: https://doi.org/10.2514/6.1975-219
[research_michaelabolender_2006]: https://doi.org/10.1109/med.2006.235846
[research_michaelcooper]: https://ntrs.nasa.gov/citations/20240004568
[research_michaeljameshays_jenniferrrobinson]: https://ntrs.nasa.gov/citations/20230018148
[research_michaeljhays_jenniferrrobinson_2024]: https://ntrs.nasa.gov/citations/20230016565
[research_michaellee_derekdalle]: https://ntrs.nasa.gov/citations/20230018339
[research_michaels_michaels_2012]: https://doi.org/10.21236/ada559972
[research_michaelzemcov_jamesjbock_2025]: https://ntrs.nasa.gov/citations/31172674351504
[research_michalski_johnson_2007]: https://doi.org/10.2514/6.2007-6273
[research_michiganunivannarbor_1963]: https://doi.org/10.21236/ad0410035
[research_micklowgeraldj_1996]: https://ntrs.nasa.gov/citations/19980206179
[research_miele_hull_1963]: https://doi.org/10.21236/ad0404858
[research_mikhail_1979]: https://doi.org/10.21236/ada076116
[research_millard_barton_1982]: https://doi.org/10.2514/6.1982-1726
[research_milleman_1967]: https://doi.org/10.2514/6.1967-518
[research_miller_washington_1994]: https://doi.org/10.2514/6.1994-1914
[research_millercg_2000]: https://ntrs.nasa.gov/citations/20000061448
[research_millercgiii_1982]: https://ntrs.nasa.gov/citations/19820024445
[research_milleree_1965]: https://ntrs.nasa.gov/citations/19660009122
[research_milleref_nieberdingwc_1968]: https://ntrs.nasa.gov/citations/19680022486
[research_millergeoffrey_richwinedavidm_1996]: https://ntrs.nasa.gov/citations/19960022393
[research_millerw_mullerr_1967]: https://ntrs.nasa.gov/citations/19670013548
[research_millerw_mullerr_1968]: https://ntrs.nasa.gov/citations/19680026861
[research_millerw_mullerr_1971]: https://ntrs.nasa.gov/citations/19710000322
[research_millerwarnerh_morakisjamesc_1990]: https://ntrs.nasa.gov/citations/19910030363
[research_milliken_1963]: https://doi.org/10.2514/6.1963-247
[research_milosfranks_karunaratnek_2002]: https://ntrs.nasa.gov/citations/20020073535
[research_milosfranks_wattersdg_2001]: https://ntrs.nasa.gov/citations/20010091019
[research_minaz_meram_2025]: https://doi.org/10.56753/asrel.2025.1.4
[research_mindermanpa_1966]: https://ntrs.nasa.gov/citations/19670034653
[research_miniature_onboard_2023]: https://doi.org/10.12968/s1478-2774(23)50388-4
[research_miotto_lepome_2003]: https://doi.org/10.2514/6.2003-5360
[research_mirelesjr_jimenez_2026]: https://doi.org/10.20944/preprints202602.1005.v1
[research_mironov_serdyuk_2012]: https://doi.org/10.1134/s0869864312020047
[research_mirzabayova_rustamov_2024]: https://doi.org/10.52202/078373-0075
[research_mitrad_bhallapn_1998]: https://ntrs.nasa.gov/citations/20000032212
[research_mizukamimasashi_corpeninggriffinp_1998]: https://ntrs.nasa.gov/citations/19980210501
[research_mjcooper_depaxson]: https://ntrs.nasa.gov/citations/20240003814
[research_mjquinn_1966]: https://ntrs.nasa.gov/citations/19670033268
[research_mo_li_2022]: https://doi.org/10.21203/rs.3.rs-2061133/v1
[research_mo_wang_2024]: https://doi.org/10.1117/12.3033124
[research_modular_program_2007]: https://doi.org/10.5139/jksas.2007.35.9.816
[research_moellertrevor_polzinkurta_2010]: https://ntrs.nasa.gov/citations/20100033281
[research_moes_cobleigh_1996]: https://doi.org/10.2514/6.1996-2409
[research_moes_cobleigh_1998]: https://doi.org/10.2514/6.1998-4340
[research_mohammadbarani_weichaotu]: https://ntrs.nasa.gov/citations/85772780587513
[research_mohammadikaji_bergmann_2016]: https://doi.org/10.1109/i2mtc.2016.7520324
[research_mohler_1965]: https://doi.org/10.2172/4627883
[research_moixbonet_schmidt_2017]: https://doi.org/10.1007/978-3-319-49715-0_20
[research_mokhtar_ibrahim_2025]: https://doi.org/10.1016/j.fraope.2025.100268
[research_mokin_kalashnikov_2022]: https://doi.org/10.52190/2073-2562_2022_1_5
[research_molina_johnson_2009]: https://doi.org/10.2514/6.2009-6471
[research_molland_1978]: https://doi.org/10.1111/j.1475-1305.1978.tb00258.x
[research_molleda_usamentiaga_2012]: https://doi.org/10.1109/tim.2011.2180964
[research_monaco_viscardi_2025]: https://doi.org/10.1117/12.3052996
[research_monnoyer_louveaux_2026]: https://doi.org/10.1038/s44459-026-00043-0
[research_monnoyer_louveaux_2026_b]: https://doi.org/10.1038/s44459-026-00066-7
[research_montesinos_davis_2026]: https://doi.org/10.2514/6.2026-114541
[research_monti_fortezza_1992]: https://doi.org/10.1016/0094-5765(92)90147-b
[research_moog_bacchus_1979]: https://doi.org/10.2514/6.1979-464
[research_moon]: https://doi.org/10.1109/imtc.1988.10886
[research_mooneyjamest_stahlhphil_2005]: https://ntrs.nasa.gov/citations/20050182028
[research_mooneyjamest_stahlhphilip_2005]: https://ntrs.nasa.gov/citations/20050215492
[research_moore_2005]: https://doi.org/10.1093/oso/9780195162059.003.0010
[research_moore_kuo_2007]: https://doi.org/10.2514/6.2007-5780
[research_moorecarletonj_1988]: https://ntrs.nasa.gov/citations/19880018959
[research_moorecharlotte_2010]: https://ntrs.nasa.gov/citations/20100031530
[research_mooredennisr_phelpswilliej_2011]: https://ntrs.nasa.gov/citations/20120001536
[research_mooredr_phelpswj_2011]: https://ntrs.nasa.gov/citations/20120002895
[research_moorefg_hymert_1993]: https://ntrs.nasa.gov/citations/19930064317
[research_moorejw_tchengp_1969]: https://ntrs.nasa.gov/citations/19690061642
[research_moorethomascsr_2004]: https://ntrs.nasa.gov/citations/20040075552
[research_moorewm_1963]: https://ntrs.nasa.gov/citations/19630027461
[research_moran_beran_1995]: https://doi.org/10.2514/6.1995-1899
[research_morgan_2015]: https://doi.org/10.21236/ada627622
[research_morgandwayner_streichrong_2001]: https://ntrs.nasa.gov/citations/20010027550
[research_morin_1978]: https://doi.org/10.21236/ada063254
[research_morris_1961]: https://doi.org/10.2514/8.9076
[research_morris_2002]: https://doi.org/10.2514/6.2002-3715
[research_morris_2004]: https://doi.org/10.2514/6.2004-463
[research_morris_crowley_2016]: https://doi.org/10.2514/6.2016-3500
[research_morrischristopheri_2001]: https://ntrs.nasa.gov/citations/20130014175
[research_morrisra_powellwr_1991]: https://ntrs.nasa.gov/citations/19920064885
[research_morse_1968]: https://doi.org/10.1088/0032-1028/10/6/303
[research_mossman_perkins_2001]: https://doi.org/10.21236/ada411282
[research_mottardelmoj_loposerjdan_1954]: https://ntrs.nasa.gov/citations/19930092189
[research_mouneimnesamiha_1988]: https://ntrs.nasa.gov/citations/19880020961
[research_moussa_guedria_2026]: https://doi.org/10.1109/iccad69956.2026.11643202
[research_movva]: https://doi.org/10.12794/metadc700010
[research_mu_zhang_2014]: https://doi.org/10.1155/2014/541627
[research_mudford_obyrne_2015]: https://doi.org/10.2514/1.a32887
[research_mudge_2023]: https://doi.org/10.1364/ao.486402
[research_mudge_2025]: https://doi.org/10.1364/ao.575166
[research_muehlner_1962]: https://doi.org/10.21236/ad0407379
[research_mueller_1964]: https://doi.org/10.2514/6.1964-527
[research_mueller_1966]: https://doi.org/10.2514/6.1966-924
[research_mueller_bratkovich_1999]: https://doi.org/10.21236/ada405512
[research_mueller_sule_1973]: https://doi.org/10.1115/1.3438135
[research_mueller_trigwell_2016]: https://doi.org/10.1061/9780784479971.059
[research_muellertj_sulewp_1972]: https://ntrs.nasa.gov/citations/19730031106
[research_mufti_2002]: https://doi.org/10.1177/147592170200100106
[research_mukairyan_vilnrottervictor_2010]: https://ntrs.nasa.gov/citations/20100009687
[research_mukeshreddydhanagari_2025]: https://doi.org/10.52783/jisem.v10i45s.8894
[research_mukheya_1965]: https://ntrs.nasa.gov/citations/19660039637
[research_mukundan_maity_2019]: https://doi.org/10.1016/j.ifacol.2019.11.255
[research_mukundan_maity_2022]: https://doi.org/10.1016/j.ifacol.2023.03.007
[research_mulhallbdl_benjauthritb_1975]: https://ntrs.nasa.gov/citations/19760008118
[research_mullencr_kearnesjh_1980]: https://ntrs.nasa.gov/citations/19810005645
[research_mullertj_sulewp_1972]: https://ntrs.nasa.gov/citations/19730003555
[research_mullharoldr_algrantijosephs_1960]: https://ntrs.nasa.gov/citations/19980227278
[research_mundt_knowlen_2024]: https://doi.org/10.2139/ssrn.4784743
[research_muralidhar_bhandari_2017]: https://doi.org/10.12783/ballistics2017/16804
[research_muratorejohnf_1987]: https://ntrs.nasa.gov/citations/19880025321
[research_murillo]: https://doi.org/10.31274/etd-180810-1331
[research_murillo_lu_2010]: https://doi.org/10.2514/6.2010-8173
[research_murphykellyj_nowakrobertj_1999]: https://ntrs.nasa.gov/citations/20040087108
[research_murphyterry_1999]: https://ntrs.nasa.gov/citations/20000025317
[research_murrayjonathan_1992]: https://ntrs.nasa.gov/citations/19920000131
[research_murraykrezan_2009]: https://doi.org/10.21236/ada514679
[research_murthysnb_sheuwh_1988]: https://ntrs.nasa.gov/citations/19890004026
[research_musgrave_1991]: https://doi.org/10.2514/6.1991-1999
[research_musgravejeffreyl_1992]: https://ntrs.nasa.gov/citations/19920067871
[research_musgravejeffreyl_paxsondaniele_1992]: https://ntrs.nasa.gov/citations/19920022263
[research_myerslp_mackallkg_1982]: https://ntrs.nasa.gov/citations/19820054148
[research_myrabo_raizer_2004]: https://doi.org/10.1007/s10740-005-0035-2
[research_nagappa_2023]: https://doi.org/10.1007/978-981-99-5005-8_23
[research_nagaral_r_2023]: https://doi.org/10.2514/6.2023-3101
[research_nagyja_1965]: https://ntrs.nasa.gov/citations/19650013559
[research_naik_holmgren_2020]: https://doi.org/10.1109/aero47225.2020.9172726
[research_nair_kukreja_2025]: https://doi.org/10.31224/4543
[research_nair_suryan_2017]: https://doi.org/10.1007/s11630-017-0965-0
[research_nair_vaidyanathan_2022]: https://doi.org/10.1016/j.asr.2022.03.023
[research_najam_2014]: https://doi.org/10.1089/space.2013.0027
[research_nakabeppu_dejima_2018]: https://doi.org/10.1615/ihtc16.tpm.023077
[research_nakanishi_sogame_1982]: https://doi.org/10.1016/b978-0-08-028708-9.50039-7
[research_nakasuka_funase_2006]: https://doi.org/10.1016/j.actaastro.2005.12.010
[research_nalinaratnayake_stevenekrist_2020]: https://ntrs.nasa.gov/citations/20200002780
[research_nallasamyr_kandulam_2010]: https://ntrs.nasa.gov/citations/20110008322
[research_namera_takaki_2010]: https://doi.org/10.2514/6.2010-4367
[research_naraghimhn_armstronges_1988]: https://ntrs.nasa.gov/citations/19890011654
[research_nardirezende_2018]: https://doi.org/10.4271/r-465
[research_nardozzo_popkin_2019]: https://doi.org/10.2514/6.2019-3838
[research_narimiya_tsuboi_2012]: https://doi.org/10.1299/jsmekyushu.2012.65.287
[research_narukagenoriyuki_kanoryohei_2015]: https://ntrs.nasa.gov/citations/20170005451
[research_naseh_alipoor_2021]: https://doi.org/10.30699/jsst.2023.1338
[research_nasution_gianto_2026]: https://doi.org/10.1080/15366367.2026.2705322
[research_natekelsey_2021]: https://ntrs.nasa.gov/citations/20210023627
[research_nathanielastepp_2024]: https://ntrs.nasa.gov/citations/20240010637
[research_naughtonjonathanw_brownjamesl_1996]: https://ntrs.nasa.gov/citations/20020041006
[research_navalweaponscenterchinalakeca_1963]: https://doi.org/10.21236/ad0846594
[research_navalweaponscenterchinalakeca_1964]: https://doi.org/10.21236/ad0848200
[research_nebiolo_castrosantos_2022]: https://doi.org/10.1186/s40317-022-00273-3
[research_needleman_tackett_1973]: https://doi.org/10.2514/6.1973-301
[research_neerrukatti_liu_2012]: https://doi.org/10.2514/6.2012-2448
[research_negrao_fanton_1998]: https://doi.org/10.4271/982869
[research_negronmartinezantoniojose_thomastaylorwalter_2018]: https://ntrs.nasa.gov/citations/20190001406
[research_neilandvr_1967]: https://ntrs.nasa.gov/citations/19680019858
[research_nelius_harris_1965]: https://doi.org/10.21236/ad0474410
[research_nelson_1988]: https://doi.org/10.2514/6.1988-214
[research_nelsonwilliamj_scottwilliamr_1958]: https://ntrs.nasa.gov/citations/19930090053
[research_nelsonwj_henrybzjr_1955]: https://ntrs.nasa.gov/citations/19740075338
[research_nemethed_andersonron_1991]: https://ntrs.nasa.gov/citations/19910021905
[research_nemzekrj_wincklerjr_1991]: https://ntrs.nasa.gov/citations/19910065250
[research_nemzekrj_wincklerjr_1991_b]: https://ntrs.nasa.gov/citations/19910060893
[research_nerlikar]: https://doi.org/10.70675/9d72118ez7ab4z4fd6z89ccz26ef201fce26
[research_nesmantom_turnerjamese_2002]: https://ntrs.nasa.gov/citations/20020092093
[research_nesteruk_cartwright_2011]: https://doi.org/10.1088/1742-6596/318/2/022042
[research_nevinscd_1975]: https://ntrs.nasa.gov/citations/19750061534
[research_newcombaw_1988]: https://ntrs.nasa.gov/citations/19880010890
[research_newman_2000]: https://doi.org/10.1190/1.1438561
[research_next_generation_2024]: https://doi.org/10.12968/s1478-2774(25)50019-4
[research_next_generation_telemetry_2008]: https://ntrs.nasa.gov/citations/20090022243
[research_ng_1963]: https://doi.org/10.21236/ad0402198
[research_ngo_blake_2003]: https://doi.org/10.2514/6.2003-5738
[research_ngo_doman_2002]: https://doi.org/10.1109/acc.2002.1023917
[research_nguyen_kostiukov_2020]: https://doi.org/10.3846/aviation.2020.12424
[research_nguyendalton_2002]: https://ntrs.nasa.gov/citations/20030000749
[research_nguyendalton_turnerlarryd_2001]: https://ntrs.nasa.gov/citations/20020022187
[research_nguyentienm_1990]: https://ntrs.nasa.gov/citations/19900000273
[research_nguyentienm_1991]: https://ntrs.nasa.gov/citations/19910000368
[research_nguyentienm_1991_b]: https://ntrs.nasa.gov/citations/19920033706
[research_nguyentienm_1992]: https://ntrs.nasa.gov/citations/19920051025
[research_nguyentienm_hinedisamim_1993]: https://ntrs.nasa.gov/citations/19930000759
[research_nguyentienmanh_1992]: https://ntrs.nasa.gov/citations/19920000510
[research_nguyentm_1988]: https://ntrs.nasa.gov/citations/19880018814
[research_nguyentm_1990]: https://ntrs.nasa.gov/citations/19910002671
[research_ni_fang_2024]: https://doi.org/10.1016/j.actaastro.2023.12.058
[research_ni_fang_2024_b]: https://doi.org/10.1016/j.ast.2024.109061
[research_nicklausorichardson_edmondwong_2020]: https://ntrs.nasa.gov/citations/20205000446
[research_nicolaides_eikenberry_1967]: https://doi.org/10.2514/6.1967-1327
[research_nicoletti_quarchioni_2024]: https://doi.org/10.1080/15732479.2024.2383299
[research_niehus_mracek_2010]: https://doi.org/10.2514/6.2010-8323
[research_nielsen_1985]: https://doi.org/10.2514/6.1985-449
[research_nielsen_stratton_1995]: https://doi.org/10.2514/6.1995-1258
[research_nielsenjackn_1947]: https://ntrs.nasa.gov/citations/19930082144
[research_niiyakarene_walkerricharde_1993]: https://ntrs.nasa.gov/citations/19930018343
[research_nikbaymelike_heegjennifer_2017]: https://ntrs.nasa.gov/citations/20170001232
[research_nikiforov_tsymbalov_2026]: https://doi.org/10.1109/iclo69056.2026.11624599
[research_nikolic_jumper_2004]: https://doi.org/10.2514/6.2004-217
[research_nishanthnr_rekhaks_2015]: https://doi.org/10.17577/ijertv4is030927
[research_niu_zhao_2014]: https://doi.org/10.1063/1.4856455
[research_nixmichael_statonericj_2004]: https://ntrs.nasa.gov/citations/20040075660
[research_nixmichaelb_escherwilliamjd_1999]: https://ntrs.nasa.gov/citations/19990064504
[research_nizin_antony_2016]: https://doi.org/10.1109/iicpe.2016.8079437
[research_noland_sanders_2026]: https://doi.org/10.2514/6.2026-114389
[research_nonaka_nishida_2012]: https://doi.org/10.2322/tastj.10.1
[research_nonaka_ogawa_2001]: https://doi.org/10.2514/6.2001-1898
[research_nonaka_watanabe_2006]: https://doi.org/10.2514/6.2006-256
[research_nondestructive_inspection_2012]: https://doi.org/10.1533/9780857095152.534
[research_none_2017]: https://doi.org/10.2172/1407929
[research_noneman_2002]: https://doi.org/10.2514/6.2002-t4-34
[research_noori_shahrokhi_2011]: https://doi.org/10.4028/www.scientific.net/amm.110-116.437
[research_normal_mode_decomposition_2017]: https://doi.org/10.12677/jisp.2017.64019
[research_norman_weiss_1988]: https://doi.org/10.2514/6.1988-3406
[research_normyle_1998]: https://doi.org/10.21236/ada350675
[research_noroozinejadfarsangi_karimipour_2023]: https://doi.org/10.1515/9783110791426-003
[research_norrisjs_backesp_2000]: https://ntrs.nasa.gov/citations/20060033830
[research_noseksm_straightdm_1976]: https://ntrs.nasa.gov/citations/19760011041
[research_novozhilov_marshakov_2018]: https://doi.org/10.1063/1.5081588
[research_nuclear_rocket_1963]: https://doi.org/10.2172/4139520
[research_numerical_method_2016]: https://doi.org/10.1002/9781118890035.ch8
[research_numerical_optimization_2016]: https://doi.org/10.21275/v5i6.nov164465
[research_nurickwh_hinesws_1973]: https://ntrs.nasa.gov/citations/19740010285
[research_nye_2013]: https://doi.org/10.2514/6.2013-5532
[research_obriencharlesj_1993]: https://ntrs.nasa.gov/citations/19930012902
[research_obrienrobina_2006]: https://ntrs.nasa.gov/citations/20090039493
[research_odomjb_1972]: https://ntrs.nasa.gov/citations/19730031846
[research_ofarrellzacharyl_2011]: https://ntrs.nasa.gov/citations/20110015645
[research_ogawa_nonaka_2004]: https://doi.org/10.2514/6.2004-2538
[research_ogbujilinusuj_humphreydonaldh_2002]: https://ntrs.nasa.gov/citations/20020072989
[research_ogbujilinusuthomas_humphreydonaldl_2002]: https://ntrs.nasa.gov/citations/20050210141
[research_ohmichi_sugioka_2022]: https://doi.org/10.2514/1.j061086
[research_okabe_wu_2016]: https://doi.org/10.1016/b978-0-08-100148-6.00004-4
[research_okayasu_ohta_2002]: https://doi.org/10.1016/s0094-5765(01)00163-1
[research_okeefestephena_bosedavidm_2010]: https://ntrs.nasa.gov/citations/20100031103
[research_okinoclayton_gaojay_2006]: https://ntrs.nasa.gov/citations/20060051685
[research_oktaviana_alwan_2026]: https://doi.org/10.58524/app.sci.def.v4i1.1128
[research_okuyama_2010]: https://doi.org/10.1016/j.precisioneng.2009.01.009
[research_olds_bellini_1998]: https://doi.org/10.2514/6.1998-1557
[research_olds_budianto_1998]: https://doi.org/10.2514/6.1998-302
[research_oldsaarond_beckroger_2013]: https://ntrs.nasa.gov/citations/20130013398
[research_olivas_vergeer_2026]: https://doi.org/10.2514/1.t7414
[research_olney_shiftlett_1982]: https://doi.org/10.2514/6.1982-1734
[research_onodera_sakamoto_2003]: https://doi.org/10.2514/6.2003-4755
[research_ooi_rajan_2023]: https://doi.org/10.1088/978-0-7503-4931-4ch2
[research_oota_usuda_2010]: https://doi.org/10.1016/j.measurement.2010.02.005
[research_operative_procedures_2014]: https://doi.org/10.1002/9781118763032.app1
[research_optimizing_the]: https://doi.org/10.1117/3.1002297.ch6
[research_ortega_amador_2023]: https://doi.org/10.2514/6.2023-0070
[research_osawa_hewitt_1986]: https://doi.org/10.2514/6.1986-1828
[research_osbornerobin_wehrmeyerjoseph_2001]: https://ntrs.nasa.gov/citations/20020021566
[research_othman_kashevnik_2022]: https://doi.org/10.3390/data7120181
[research_othman_kashevnik_2022_b]: https://doi.org/10.3390/data7050062
[research_otsuka_2026]: https://doi.org/10.1016/j.meadig.2026.100048
[research_otsuka_2026_b]: https://doi.org/10.2139/ssrn.6502460
[research_ottoew_1966]: https://ntrs.nasa.gov/citations/19660026628
[research_ou_xiao_2024]: https://doi.org/10.1088/1361-6501/ad30ba
[research_oxer_blemings_2009]: https://doi.org/10.1007/978-1-4302-2478-5_15
[research_ozelsel]: https://doi.org/10.31390/gradschool_disstheses.2416
[research_p_p_2024]: https://doi.org/10.2139/ssrn.4813560
[research_pace_eastburg_2015]: https://doi.org/10.21236/ada623063
[research_pagendarm_laurien_1988]: https://doi.org/10.2514/6.1988-2515
[research_palaniappan_jameson_2004]: https://doi.org/10.2514/6.2004-5383
[research_palaszewskibryan_1997]: https://ntrs.nasa.gov/citations/19970025142
[research_palaszewskibryan_olearyrobert_1998]: https://ntrs.nasa.gov/citations/19980174935
[research_palaszewskibryana_1998]: https://ntrs.nasa.gov/citations/20050177877
[research_pallela_thakur_2026]: https://doi.org/10.1186/s42774-025-00237-0
[research_pamadibandun_brauckmanngregoryj_1999]: https://ntrs.nasa.gov/citations/19990047600
[research_pamelapoljak_2023]: https://ntrs.nasa.gov/citations/20230002128
[research_pamelapoljak_aaronjohnson]: https://ntrs.nasa.gov/citations/20220013801
[research_pan_bao_2025]: https://doi.org/10.1177/14759217251322943
[research_pan_guo_2020]: https://doi.org/10.1145/3419635.3419671
[research_pande_1994]: https://doi.org/10.21236/ada413742
[research_pandey_arora_2019]: https://doi.org/10.1007/978-981-13-5934-7_24
[research_pannetonrj_warrenwb_1969]: https://ntrs.nasa.gov/citations/19700038544
[research_pant]: https://doi.org/10.22215/etd/2014-10409
[research_parachute_recovery_1966]: https://ntrs.nasa.gov/citations/19660018638
[research_paramo_arizpe_2024]: https://doi.org/10.52202/078371-0212
[research_parent_2004]: https://doi.org/10.2514/6.2004-3765
[research_park_farrar_2010]: https://doi.org/10.1002/9780470686652.eae190
[research_park_inman_2005]: https://doi.org/10.1002/0470869097.ch13
[research_park_kim_2025]: https://doi.org/10.2139/ssrn.5256134
[research_parkerhermonm_1955]: https://ntrs.nasa.gov/citations/19930092224
[research_parkerhermonm_1956]: https://ntrs.nasa.gov/citations/19930084469
[research_parkes_armbruster_2010]: https://doi.org/10.1016/j.actaastro.2009.05.016
[research_parkes_mcclements_2014]: https://doi.org/10.1109/ahs.2014.6880173
[research_parkes_mcclements_2015]: https://doi.org/10.1109/aero.2015.7119317
[research_parkryans_bhaskaranshyam_2009]: https://ntrs.nasa.gov/citations/20150011967
[research_parzychd_boydl_1991]: https://ntrs.nasa.gov/citations/19940028353
[research_paschall_brady_2012]: https://doi.org/10.1109/aero.2012.6187306
[research_paschke_2000]: https://doi.org/10.2172/754932
[research_pasternackm_1966]: https://ntrs.nasa.gov/citations/19660027858
[research_pasternackm_1967]: https://ntrs.nasa.gov/citations/19670041145
[research_patelp_1996]: https://ntrs.nasa.gov/citations/19970011648
[research_patil_2022]: https://doi.org/10.32920/ryerson.14644389.v1
[research_patrickchampey]: https://ntrs.nasa.gov/citations/20260007948
[research_patrickrshea_davidtchan]: https://ntrs.nasa.gov/citations/20220018078
[research_patricksheaney_djpiatak]: https://ntrs.nasa.gov/citations/20230018530
[research_patricksheaney_francescosoranna]: https://ntrs.nasa.gov/citations/20205002633
[research_pattersonre_1973]: https://ntrs.nasa.gov/citations/19730015507
[research_paturzo_ferraro_2009]: https://doi.org/10.1364/ao.48.005537
[research_paulgradl_chrisprotz]: https://ntrs.nasa.gov/citations/20205007409
[research_paulson_kimura_2020]: https://doi.org/10.2514/6.2020-0193
[research_pavliaj_kacynskikj_1986]: https://ntrs.nasa.gov/citations/19870014376
[research_pavlialbertj_kacynskikennethj_1987]: https://ntrs.nasa.gov/citations/19870010948
[research_paxson_perkins_2021]: https://doi.org/10.2514/6.2021-0192
[research_payne_1980]: https://doi.org/10.21236/ada087515
[research_payne_hartley_1980]: https://doi.org/10.21236/ada087514
[research_pearson_1976]: https://doi.org/10.1111/j.1475-1305.1976.tb00173.x
[research_pedrojmedelius_carlostmata_2004]: https://ntrs.nasa.gov/citations/20050051591
[research_peery_parsley_1996]: https://doi.org/10.1063/1.49964
[research_pelaccio_1996]: https://doi.org/10.1063/1.49956
[research_pempie_2003]: https://doi.org/10.2514/6.iac-03-v.2.08
[research_penchuk_schlundt_1969]: https://doi.org/10.2514/6.1969-847
[research_peng_zhang_1994]: https://doi.org/10.1080/00423119408969061
[research_peretto_sasdelli_2005]: https://doi.org/10.1109/tim.2005.858145
[research_perez_gietler_2020]: https://doi.org/10.1109/i2mtc43012.2020.9129581
[research_perezroca]: https://doi.org/10.70675/8da63282z9e21z49c0z9f67z0156f62140d8
[research_performance_of_1995]: https://doi.org/10.2514/5.9781600866357.0195.0206
[research_performance_optimization_2017]: https://doi.org/10.21090/ijaerd.34721
[research_pergamenths_thorperd_1975]: https://ntrs.nasa.gov/citations/19760011199
[research_perkinsedwardw_jorgensenlelandh_1958]: https://ntrs.nasa.gov/citations/19930091022
[research_perlmutter_depierre_1965]: https://doi.org/10.21236/ad0612646
[research_pernetdf_1966]: https://ntrs.nasa.gov/citations/19670009218
[research_perrins_2012]: https://doi.org/10.21236/ada557598
[research_perry_1987]: https://doi.org/10.1111/j.1475-1305.1987.tb00639.x
[research_perryjohng_1989]: https://ntrs.nasa.gov/citations/19900017004
[research_perspectives_on]: https://doi.org/10.4271/air6245
[research_pescetelli_minisci_2012]: https://doi.org/10.2514/6.2012-5828
[research_peshkov_tretyakov_2024]: https://doi.org/10.3103/s1068799824030097
[research_peters_1981]: https://doi.org/10.21236/ada101614
[research_peters_brost_2006]: https://doi.org/10.2514/6.2006-7201
[research_petersonchariya_rowejohn_1998]: https://ntrs.nasa.gov/citations/19990052764
[research_petersonchariya_rowejohn_1999]: https://ntrs.nasa.gov/citations/19990064160
[research_petersonmr_1973]: https://ntrs.nasa.gov/citations/19740041069
[research_petersonmr_1975]: https://ntrs.nasa.gov/citations/19760062575
[research_petersonrl_1981]: https://ntrs.nasa.gov/citations/19810020556
[research_petitjean_musset_2026]: https://doi.org/10.1088/1361-6501/aeabcc
[research_petrasekdonaldw_stephensjosephr_1988]: https://ntrs.nasa.gov/citations/19890006619
[research_petrasekdonaldw_stephensjosephr_1989]: https://ntrs.nasa.gov/citations/19890013302
[research_petrenko_2025]: https://doi.org/10.62717/2221-4550-2025-1-069
[research_petrosky_1992]: https://doi.org/10.1063/1.41868
[research_pettit_barkhoudarian_1999]: https://doi.org/10.2514/6.1999-2527
[research_pettitrichardljr_1988]: https://ntrs.nasa.gov/citations/19890043691
[research_peugeotjohn_garciachance_2014]: https://ntrs.nasa.gov/citations/20140010459
[research_philipccalhoun_jonathanglickman]: https://ntrs.nasa.gov/citations/20250000951
[research_philipchuk_1953]: https://doi.org/10.21236/ad0009072
[research_piatakdavidj_sekulamartink_2015]: https://ntrs.nasa.gov/citations/20150006848
[research_piatakdavidj_sekulamartink_2016]: https://ntrs.nasa.gov/citations/20160007661
[research_pickettrb_matthewsfl_1973]: https://ntrs.nasa.gov/citations/19750003211
[research_pidvysotskyi_2021]: https://doi.org/10.31224/osf.io/xbf8z
[research_pieperjerryl_mussjeff_1989]: https://ntrs.nasa.gov/citations/19910007814
[research_piermanbc_1969]: https://ntrs.nasa.gov/citations/19690018398
[research_pincusbr_stephensonjs_1971]: https://ntrs.nasa.gov/citations/19710016361
[research_pinier_2011]: https://doi.org/10.2514/6.2011-3167
[research_pinierjeremyt_ericksongarye_2015]: https://ntrs.nasa.gov/citations/20150006862
[research_piotr_karol_2019]: https://doi.org/10.1109/aero.2019.8741655
[research_pirescraig_knudsonmatthewd_2017]: https://ntrs.nasa.gov/citations/20180000774
[research_pittskj_1974]: https://ntrs.nasa.gov/citations/19750004690
[research_plane_1963]: https://doi.org/10.21236/ad0605853
[research_plane_1964]: https://doi.org/10.21236/ad0605491
[research_plane_1964_b]: https://doi.org/10.21236/ad0606557
[research_plane_1964_c]: https://doi.org/10.21236/ad0606515
[research_planttj_nugentj_1980]: https://ntrs.nasa.gov/citations/19800038839
[research_plasma_propulsion_2011]: https://doi.org/10.14741/ijcet/22774106/spl.4.2016.47
[research_platte_iwanczik_2017]: https://doi.org/10.1051/metrology/201714003
[research_plostins_celmins_1990]: https://doi.org/10.2514/6.1990-66
[research_podolchak_2019]: https://doi.org/10.15421/451904
[research_pokela_gustavsson_2023]: https://doi.org/10.2514/6.2023-3677
[research_poland_schwanebeck_1970]: https://doi.org/10.2514/6.1970-611
[research_polgerj_wallacegr_1969]: https://ntrs.nasa.gov/citations/19700034824
[research_polkjamese_pancottianthony_2013]: https://ntrs.nasa.gov/citations/20150008062
[research_pollet_1983]: https://doi.org/10.2514/6.1983-1314
[research_polzinkurta_markusicthomase_2006]: https://ntrs.nasa.gov/citations/20060025538
[research_pomerantzmarc_nguyenviet_2015]: https://ntrs.nasa.gov/citations/20170008239
[research_pomerantzmi_limc_2012]: https://ntrs.nasa.gov/citations/20150005569
[research_ponci_johnson_2008]: https://doi.org/10.1109/amuem.2008.4589930
[research_popkov_kornilov_2024]: https://doi.org/10.53954/9785604990131_132
[research_portellidemora]: https://doi.org/10.5821/dissertation-2117-93896
[research_porter_1968]: https://doi.org/10.21236/ad0833638
[research_portz_2004]: https://doi.org/10.2514/6.2004-3562
[research_poshouchen_benjaminlloydrupp]: https://ntrs.nasa.gov/citations/20240005751
[research_posnerec_rodemicher_1969]: https://ntrs.nasa.gov/citations/19700044683
[research_postalrb_pottscm_1966]: https://ntrs.nasa.gov/citations/19670002810
[research_postflight_evaluation_1966]: https://ntrs.nasa.gov/citations/19710070509
[research_pouliquen_1978]: https://doi.org/10.2514/6.1978-1036
[research_pouryanikoueeyan_michaeldhind]: https://ntrs.nasa.gov/citations/20220005944
[research_powellmark_mittmandavid_2008]: https://ntrs.nasa.gov/citations/20090020478
[research_powerswilliamt_sherrellfg_1988]: https://ntrs.nasa.gov/citations/19890007445
[research_prabhuramadask_1999]: https://ntrs.nasa.gov/citations/19990100643
[research_praharajsaratc_palkorichardl_1986]: https://ntrs.nasa.gov/citations/19870009172
[research_prasad_2022]: https://doi.org/10.13111/2066-8201.2022.14.1.10
[research_prasad_pal_2003]: https://doi.org/10.1080/02564602.2003.11417116
[research_pribadi_2025]: https://doi.org/10.58445/rars.2962
[research_priceea_hulljj_1971]: https://ntrs.nasa.gov/citations/19720003280
[research_princetonunivnj_1952]: https://doi.org/10.21236/ad0036008
[research_priskosalex_2016]: https://ntrs.nasa.gov/citations/20160007006
[research_pritchardjamesa_1989]: https://ntrs.nasa.gov/citations/19900041823
[research_pritchettvictore_maylemelodyn_2014]: https://ntrs.nasa.gov/citations/20140004086
[research_problems_in_1994]: https://doi.org/10.1016/0967-0661(94)91001-4
[research_prognostic_methodologies_for]: https://doi.org/10.12681/eadd/55142
[research_progress_made_2012]: https://doi.org/10.1063/pt.5.026571
[research_prokopec_1974]: https://doi.org/10.1111/j.1475-1305.1974.tb00075.x
[research_propagation_of_2015]: https://doi.org/10.36334/modsim.2015.a3.aidoo
[research_propeller_propfan_in_flight]: https://doi.org/10.4271/air4065a
[research_prosserwilliam_percydaniel_2003]: https://ntrs.nasa.gov/citations/20040034212
[research_prosserwilliamh_gormanmichaelr_2004]: https://ntrs.nasa.gov/citations/20040171467
[research_pruzan_mendenhall_2011]: https://doi.org/10.2514/6.2011-3018
[research_psathiray_amywinebarger]: https://ntrs.nasa.gov/citations/20230017937
[research_psathiray_amywinebarger_b]: https://ntrs.nasa.gov/citations/20205010798
[research_puening_1990]: https://doi.org/10.2514/6.1990-2707
[research_purcell_wicklund_2025]: https://doi.org/10.2514/6.2025-0202
[research_purohit_mathpal_2017]: https://doi.org/10.2514/6.2017-4710
[research_purserpaule_thibodauxjosephg_1950]: https://ntrs.nasa.gov/citations/19930086428
[research_putnamle_1979]: https://ntrs.nasa.gov/citations/19820007143
[research_pyle_jacobs_2023]: https://doi.org/10.2514/6.2023-1469
[research_pyle_jacobs_2026]: https://doi.org/10.2514/6.2026-1975
[research_pyle_jacobs_2026_b]: https://doi.org/10.2514/1.j066238
[research_pytanowski_1999]: https://doi.org/10.1109/rams.1999.744087
[research_qi_cheng_2022]: https://doi.org/10.3390/aerospace9120788
[research_qi_jianliang_2017]: https://doi.org/10.2514/6.2017-1248
[research_qi_meng_2026]: https://doi.org/10.2139/ssrn.7273043
[research_qian_sun_2013]: https://doi.org/10.1109/icca.2013.6564958
[research_qin_zhang_2016]: https://doi.org/10.1109/isape.2016.7833977
[research_qiuhong_zhaoying_2014]: https://doi.org/10.1109/ccdc.2014.6852246
[research_qu_yang_2015]: https://doi.org/10.1117/12.2181836
[research_quassb_howardf_1981]: https://ntrs.nasa.gov/citations/19810047204
[research_quentmeyerrichardj_roncaceelizabetha_1993]: https://ntrs.nasa.gov/citations/19940008097
[research_quincymckown_markschoenenberger]: https://ntrs.nasa.gov/citations/20205006820
[research_quingxinlin_beardshawn_2011]: https://ntrs.nasa.gov/citations/20120006702
[research_quintopfrank_orienettiem_1994]: https://ntrs.nasa.gov/citations/19940030740
[research_r_1928]: https://doi.org/10.1016/s0016-0032(28)92321-2
[research_r_mi_2012]: https://doi.org/10.1109/icdse.2012.6281894
[research_raab_rohdebrandenburger_2020]: https://doi.org/10.2514/6.2020-0512
[research_radhakrishnan_hari_2023]: https://doi.org/10.1007/s40435-023-01126-4
[research_rafaely_weiss_2007]: https://doi.org/10.1109/tsp.2006.888896
[research_rafferty_1968]: https://doi.org/10.21236/ad0827403
[research_rafi_alfaruk_2025]: https://doi.org/10.2139/ssrn.5179661
[research_ragab_cheatwood_2015]: https://doi.org/10.2514/6.2015-4490
[research_raghavan_cesnik_2005]: https://doi.org/10.1002/0470869097.ch11
[research_rahaim_grage_2000]: https://doi.org/10.2514/6.2000-4525
[research_raharema_sasongko_2026]: https://doi.org/10.1109/med70602.2026.11598409
[research_rahul_alokita_2019]: https://doi.org/10.1016/b978-0-08-102291-7.00003-4
[research_rai_brunt_1999]: https://doi.org/10.4271/1999-01-1329
[research_raineensimons_felixamiranda_2003]: https://ntrs.nasa.gov/citations/20040013356
[research_rainesng_bircherfe_1991]: https://ntrs.nasa.gov/citations/19910059686
[research_rajasegar_choi_2018]: https://doi.org/10.2514/6.2018-0147
[research_rajendran_ramalingame_2021]: https://doi.org/10.3390/s21186082
[research_rajesh_kumar_2012]: https://doi.org/10.5407/jksv.2011.10.1.047
[research_rajsaiv_ghosnlouisj_2004]: https://ntrs.nasa.gov/citations/20050192259
[research_rajsaiv_robinsonraymondc_2005]: https://ntrs.nasa.gov/citations/20050217185
[research_rakowskyel_marchesevp_1974]: https://ntrs.nasa.gov/citations/19740000202
[research_rallabhandi_mavris_2003]: https://doi.org/10.2514/6.2003-3877
[research_ramalingam_thanuja_2021]: https://doi.org/10.1007/s11277-021-08799-0
[research_ramanganesh_riceedwardj_1991]: https://ntrs.nasa.gov/citations/19920053374
[research_ramiller_hsalpert]: https://ntrs.nasa.gov/citations/20230010812
[research_ranganatha]: https://doi.org/10.18122/td/1890/boisestate
[research_rao_abhinav_2023]: https://doi.org/10.1063/5.0178773
[research_raperjl_1965]: https://ntrs.nasa.gov/citations/19650021353
[research_rappin_debazelaire_2000]: https://doi.org/10.3997/2214-4609-pdb.28.p135
[research_rasky_pittman_2006]: https://doi.org/10.2514/6.2006-7208
[research_rasmussen_lanzaro_1967]: https://doi.org/10.2514/6.1967-1349
[research_ratcliffe_ratcliffe_2014]: https://doi.org/10.1007/978-3-319-12063-8_5
[research_ratcliffe_ratcliffe_2014_b]: https://doi.org/10.1007/978-3-319-12063-8_4
[research_ratcliffmarkl_athavalemaheshm_1993]: https://ntrs.nasa.gov/citations/19930066127
[research_ratekingary_1998]: https://ntrs.nasa.gov/citations/19990026880
[research_ratz_1960]: https://doi.org/10.1109/jrproc.1960.287450
[research_ravi_rathod_2015]: https://doi.org/10.1117/12.2085000
[research_rayasok_daixiaowen_1995]: https://ntrs.nasa.gov/citations/19950016778
[research_rcchapmanjr_gfcritchlow_1963]: https://ntrs.nasa.gov/citations/19640000970
[research_real_time_1975]: https://ntrs.nasa.gov/citations/19750025051
[research_rebillat_hmad_2017]: https://doi.org/10.1177/1475921716685039
[research_reedjohng_ragabmohamedm_2016]: https://ntrs.nasa.gov/citations/20160012009
[research_reevesehjr_stovalljr_1960]: https://ntrs.nasa.gov/citations/19650002716
[research_reevesehjr_threlkeldwbjr_1963]: https://ntrs.nasa.gov/citations/19650025713
[research_rehderjj_1977]: https://ntrs.nasa.gov/citations/19780002243
[research_rehman_fidan_2009]: https://doi.org/10.2514/6.2009-7291
[research_reibman_suthaharan_2008]: https://doi.org/10.1109/icip.2008.4711972
[research_reichenfeldcurtisj_jonespaulg_1999]: https://ntrs.nasa.gov/citations/20000019589
[research_reinel_1970]: https://doi.org/10.2514/6.1970-1030
[research_reinersmanp_carderkl_1995]: https://ntrs.nasa.gov/citations/19970023033
[research_reis_sundberg_1967]: https://doi.org/10.2514/6.1967-1344
[research_rekeshali_caroleaddona]: https://ntrs.nasa.gov/citations/20250000787
[research_rekeshmali_carolejaddona]: https://ntrs.nasa.gov/citations/20250000509
[research_ren_2026]: https://doi.org/10.1117/12.3132129
[research_ren_he_2017]: https://doi.org/10.1007/978-981-10-4837-1_16
[research_ren_ma_2024]: https://doi.org/10.2139/ssrn.4783505
[research_ren_wang_2023]: https://doi.org/10.1017/aer.2023.69
[research_ren_yang_2023]: https://doi.org/10.1155/2023/9693047
[research_renithap_sivaramapandianj_2016]: https://doi.org/10.1109/iceets.2016.7583878
[research_renzrrl_1981]: https://ntrs.nasa.gov/citations/19820009604
[research_renzrrl_clarker_1980]: https://ntrs.nasa.gov/citations/19820037221
[research_research_and_1967]: https://ntrs.nasa.gov/citations/19670027857
[research_research_development_1968]: https://ntrs.nasa.gov/citations/19680027858
[research_research_on_1966]: https://ntrs.nasa.gov/citations/19670010088
[research_response_analysis_2026]: https://doi.org/10.3901/jme.260010
[research_resta_dicicca_2024]: https://doi.org/10.2514/6.2024-1617
[research_reubushde_1973]: https://ntrs.nasa.gov/citations/19730017103
[research_reubushde_runckeljf_1973]: https://ntrs.nasa.gov/citations/19730015075
[research_reusable_launch_1995]: https://doi.org/10.17226/5115
[research_reusable_launch_2026]: https://doi.org/10.3901/jme.260002
[research_reusable_rocket_2013]: https://doi.org/10.1063/pt.5.026743
[research_review_for_2020]: https://doi.org/10.1111/2041-210x.13446/v2/review1
[research_rey_2000]: https://doi.org/10.1063/1.1290921
[research_reynolds_caillet_2026]: https://doi.org/10.2514/6.2026-112867
[research_reynolds_kokan_2021]: https://doi.org/10.2514/6.2021-3269
[research_reynoldslw_tyefc_1966]: https://ntrs.nasa.gov/citations/19660010346
[research_reyrd_nipperej_1978]: https://ntrs.nasa.gov/citations/19780020190
[research_reza_agarwal_2024]: https://doi.org/10.1007/978-981-97-1306-6_43
[research_reza_arora_2017]: https://doi.org/10.1109/ictus.2017.8286122
[research_rhee_lee_2008]: https://doi.org/10.1007/s12206-008-0514-6
[research_rhewrayd_1999]: https://ntrs.nasa.gov/citations/19990072772
[research_rice_1999]: https://doi.org/10.21236/ada389435
[research_rice_2013]: https://doi.org/10.21236/ada578383
[research_rice_bangsund_1998]: https://doi.org/10.21236/ada409805
[research_ricekevin_kizzortbrad_2010]: https://ntrs.nasa.gov/citations/20100015491
[research_ricewj_birchenoughag_1982]: https://ntrs.nasa.gov/citations/19810000315
[research_richardkmoore_johnhwall]: https://ntrs.nasa.gov/citations/20230000642
[research_richardslance_parkerallen_2014]: https://ntrs.nasa.gov/citations/20140008542
[research_richardswlance_madaraserici_2013]: https://ntrs.nasa.gov/citations/20140011091
[research_richardwinski_alejandropensado]: https://ntrs.nasa.gov/citations/20230018696
[research_riclesjamesm_1991]: https://ntrs.nasa.gov/citations/19920012063
[research_rieckhofftj_covanma_2001]: https://ntrs.nasa.gov/citations/20010066069
[research_riggins_nelson_1998]: https://doi.org/10.2514/6.1998-1647
[research_riggins_nelson_1999]: https://doi.org/10.2514/2.756
[research_ripper_dias_2009]: https://doi.org/10.1016/j.measurement.2009.05.002
[research_ripperetroyb_wiensgloriaj_2010]: https://ntrs.nasa.gov/citations/20100021136
[research_rishi_2024]: https://doi.org/10.1088/978-0-7503-6462-1ch7
[research_rishikawa_tokamoto]: https://ntrs.nasa.gov/citations/20210026007
[research_rizza_machado_2023]: https://doi.org/10.21014/tc5-2022.093
[research_robbennolt_munira_2026]: https://doi.org/10.2139/ssrn.6277855
[research_robbinshj_zebrowskize_1966]: https://ntrs.nasa.gov/citations/19710015274
[research_robertokojie_christianpetrov]: https://ntrs.nasa.gov/citations/20220015212
[research_roberts_lewis_1985]: https://doi.org/10.2514/6.1985-1404
[research_roberts_stevens_2007]: https://doi.org/10.1016/j.measurement.2006.04.016
[research_rochefort_oconnor_1991]: https://doi.org/10.21236/ada241272
[research_rochefort_yorra_1976]: https://doi.org/10.21236/ada028205
[research_rocket_engine_1992]: https://doi.org/10.2514/6.1992-3421
[research_rocket_engine_1998]: https://doi.org/10.1016/s0262-1762(98)90278-4
[research_rocket_engine_2000]: https://doi.org/10.1142/9789812792273_0007
[research_rocket_engine_2000_b]: https://doi.org/10.1142/9789812792273_0006
[research_rocket_engine_2004]: https://doi.org/10.2514/5.9781600866760.0437.0467
[research_rocket_engine_2005]: https://doi.org/10.1002/0471743984.vse6185
[research_rocket_engine_2009]: https://doi.org/10.1093/acref/9780195301731.013.33875
[research_rocket_engine_2012]: https://ntrs.nasa.gov/citations/20120001874
[research_rocket_nozzle_2019]: https://doi.org/10.1017/9781108381376.005
[research_rocket_propulsion_2019]: https://doi.org/10.33564/ijeast.2019.v03i12.018
[research_rocket_propulsion_2022]: https://doi.org/10.15394/eaglepub.2022.1066.n34
[research_rodi_stoldt_2019]: https://doi.org/10.2514/6.2019-2812
[research_rodriguez_ready_2006]: https://doi.org/10.2514/6.2006-6468
[research_rogeros_1969]: https://ntrs.nasa.gov/citations/19700059369
[research_rogeros_1972]: https://ntrs.nasa.gov/citations/19720059036
[research_rogers_dragone_1996]: https://doi.org/10.2514/6.1996-1228
[research_rogerson_1995]: https://doi.org/10.2514/6.1995-2727
[research_rogersraynac_2004]: https://ntrs.nasa.gov/citations/20050186802
[research_rogersstuarte_dallederekj_2015]: https://ntrs.nasa.gov/citations/20190001990
[research_rogowskiroberts_1990]: https://ntrs.nasa.gov/citations/19920042153
[research_rojdevkristina_hagenjeff_2020]: https://ntrs.nasa.gov/citations/20200001540
[research_rollstin_1979]: https://doi.org/10.2514/6.1979-506
[research_romano_pisano_2026]: https://doi.org/10.20944/preprints202603.1386.v1
[research_romarubi_kuo_2025]: https://doi.org/10.2514/6.2025-97105
[research_roncace_1991]: https://doi.org/10.2514/6.1991-2445
[research_rooney_2003]: https://doi.org/10.2514/6.2003-2953
[research_rooney_wilt_1985]: https://doi.org/10.2514/6.1985-1405
[research_roozeboomnettieh_powelljessie_2020]: https://ntrs.nasa.gov/citations/20200000245
[research_rosatinosa_westbrookrm_1979]: https://ntrs.nasa.gov/citations/19780000375
[research_rose_1958]: https://doi.org/10.21236/ad0218493
[research_roshko_1993]: https://doi.org/10.21236/ada286316
[research_roshon_1960]: https://doi.org/10.1121/1.1936366
[research_rossdl_1985]: https://ntrs.nasa.gov/citations/19860004998
[research_rossdl_1990]: https://ntrs.nasa.gov/citations/19900012587
[research_rossi_1996]: https://doi.org/10.1016/0955-5986(95)00018-6
[research_rothce_wattsll_1972]: https://ntrs.nasa.gov/citations/19720015243
[research_rothmund_2006]: https://doi.org/10.2514/6.iac-06-e4.3.04
[research_rothschild_schuster_1999]: https://doi.org/10.2514/6.1999-2380
[research_rubin_1971]: https://doi.org/10.21236/ad0730669
[research_rubins_searlega_1988]: https://ntrs.nasa.gov/citations/19930075337
[research_rubiohervas_reyhanoglu_2014]: https://doi.org/10.1016/j.actaastro.2014.01.022
[research_ruf_mcconaughey_1997]: https://doi.org/10.2514/6.1997-3218
[research_rufjh_hagemanng_2003]: https://ntrs.nasa.gov/citations/20030066114
[research_rufjh_mcdanielsdm_2002]: https://ntrs.nasa.gov/citations/20030067717
[research_rufjosephh_mcdanielsdavidm_2003]: https://ntrs.nasa.gov/citations/20040000846
[research_rufjosephh_mcdanielsdavidm_2005]: https://ntrs.nasa.gov/citations/20050217125
[research_ruixue_zexu_2025]: https://doi.org/10.1016/j.ifacol.2025.11.221
[research_rummerdi_mosserma_1982]: https://ntrs.nasa.gov/citations/19830030685
[research_runklere_1981]: https://ntrs.nasa.gov/citations/19810005479
[research_rusconi_borelli_2026]: https://doi.org/10.2514/1.a36343
[research_rusek_1989]: https://doi.org/10.1016/s1474-6670(17)52852-9
[research_rusick_2007]: https://doi.org/10.1109/rams.2007.328117
[research_russelldl_blacklockk_1988]: https://ntrs.nasa.gov/citations/19880061266
[research_russellrichard_washabaughandy_2011]: https://ntrs.nasa.gov/citations/20120000074
[research_ruth_colburn_1992]: https://doi.org/10.21236/ada258282
[research_rutledge_1993]: https://doi.org/10.2514/6.1993-4063
[research_ryan_2000]: https://doi.org/10.21236/ada377986
[research_ryan_verderaime_1993]: https://doi.org/10.2514/6.1993-1140
[research_ryanconnelly_thomassteva]: https://ntrs.nasa.gov/citations/20260004100
[research_ryanhm_rahmans_2000]: https://ntrs.nasa.gov/citations/20040000861
[research_ryohkoishikawa_songdonguk]: https://ntrs.nasa.gov/citations/20220007743
[research_rysev_andronov_1995]: https://doi.org/10.2514/6.1995-1590
[research_ryu_castano_2015]: https://doi.org/10.12783/shm2015/275
[research_ryu_kim_2025]: https://doi.org/10.1007/s42405-025-01081-8
[research_s_chauhan_2020]: https://doi.org/10.1109/inocon50539.2020.9298264
[research_s_s_2025]: https://doi.org/10.1109/etis64005.2025.10961627
[research_sabatinirr_rabchevskyg_1970]: https://ntrs.nasa.gov/citations/19710028469
[research_sabiasteve_handsarah_1988]: https://ntrs.nasa.gov/citations/19890043661
[research_sabin_1955]: https://doi.org/10.1121/1.1918024
[research_sabin_1956]: https://doi.org/10.1121/1.1908453
[research_sabzehparvar_2005]: https://doi.org/10.2514/1.12837
[research_sachikonye_2026]: https://doi.org/10.2139/ssrn.6526580
[research_sachs_mehlhorn_1996]: https://doi.org/10.2514/6.1996-3869
[research_saglam_yilmaz_2018]: https://doi.org/10.1109/ceit.2018.8751944
[research_sagontijo_filho_2025]: https://doi.org/10.26678/abcm.cobem2023.cob2023-1931
[research_sahai_john_2014]: https://doi.org/10.2514/1.a32583
[research_sahbon_michalow_2023]: https://doi.org/10.2478/tar-2023-0007
[research_sahu_cooper_1997]: https://doi.org/10.21236/ada330375
[research_sakagami_takeishi_2019]: https://doi.org/10.2322/tastj.17.244
[research_sakai_yoshii_2021]: https://doi.org/10.1016/j.apradiso.2021.109630
[research_sakalagg_rainesng_1992]: https://ntrs.nasa.gov/citations/19920066305
[research_sakamoto_takahashi_1999]: https://doi.org/10.2514/6.1999-2761
[research_salahudden_ghosh_2021]: https://doi.org/10.1016/j.ast.2021.106823
[research_sale_1964]: https://doi.org/10.21236/ad0609001
[research_salgovic_galinski_2022]: https://doi.org/10.1109/elmar55880.2022.9899781
[research_saligatv_1967]: https://ntrs.nasa.gov/citations/19670049966
[research_salikuddinm_1983]: https://ntrs.nasa.gov/citations/19830044711
[research_salinas_ball_1973]: https://doi.org/10.21236/ad0758128
[research_salitamark_1989]: https://ntrs.nasa.gov/citations/19890037884
[research_salmireinoj_1956]: https://ntrs.nasa.gov/citations/19930089468
[research_salmirj_cortrightemjr_1956]: https://ntrs.nasa.gov/citations/19930089418
[research_salterwe_1977]: https://ntrs.nasa.gov/citations/19770000034
[research_samanichne_1972]: https://ntrs.nasa.gov/citations/19720024135
[research_sambamurthi_1995]: https://doi.org/10.2514/6.1995-2590
[research_sanchezmunoz_lagarzacortes_2024]: https://doi.org/10.20944/preprints202407.1346.v1
[research_sanchinidj_kirbyfm_1973]: https://ntrs.nasa.gov/citations/19740031717
[research_sanderej_leahyjc_1993]: https://ntrs.nasa.gov/citations/19930065949
[research_sankararaman_ling_2011]: https://doi.org/10.1109/aero.2011.5747567
[research_sankariashokalshiya_santhosh_2021]: https://doi.org/10.1016/j.matpr.2020.11.783
[research_santilmichael_2001]: https://ntrs.nasa.gov/citations/20010098760
[research_santororobertj_paksibtosh_2005]: https://ntrs.nasa.gov/citations/20050239574
[research_santororobertj_palsibtosh_1999]: https://ntrs.nasa.gov/citations/19990025912
[research_santos_oliveira_2024]: https://doi.org/10.1016/j.actaastro.2024.05.039
[research_santosjosea_oishitomo_2011]: https://ntrs.nasa.gov/citations/20110014965
[research_sao_garain_2025]: https://doi.org/10.1115/imece-india2025-161186
[research_sargsyan_2015]: https://doi.org/10.1007/978-3-319-11259-6_22-1
[research_sarigulklijn_sarigulklijn_2003]: https://doi.org/10.2514/6.2003-909
[research_sarkar_2021]: https://doi.org/10.1515/ract-2020-0085
[research_sarma_sahoo_2016]: https://doi.org/10.1007/s12046-016-0513-8
[research_sarma_sahoo_2018]: https://doi.org/10.1007/s40032-018-0458-2
[research_sarotte]: https://doi.org/10.70675/7e4e5805z21f6z4e0bz8874z44abf9aa6d38
[research_sarwar_nizami_2025]: https://doi.org/10.1134/s0015462825601974
[research_sarwar_rao_2024]: https://doi.org/10.1201/9788770046299-5
[research_sasoh_sekiya_2009]: https://doi.org/10.2514/6.2009-1533
[research_satheesh_jagadeesh_2007]: https://doi.org/10.1063/1.2565663
[research_satheesh_jagadeesh_2009]: https://doi.org/10.1007/978-3-540-85168-4_92
[research_satriani_abdiani_2025]: https://doi.org/10.37481/pkmb.v5i2.1325
[research_sause_jasiuniene_2022]: https://doi.org/10.1007/978-3-030-72192-3_11
[research_savitha_ravindra_2014]: https://doi.org/10.1109/iccic.2014.7238391
[research_sawada_araki]: https://doi.org/10.1109/icassp.2006.1661216
[research_sawada_kunimasu_2004]: https://doi.org/10.5359/jwe.29.98_159
[research_sawyer_bush_1998]: https://doi.org/10.1063/1.54711
[research_sawyer_hodge_1999]: https://doi.org/10.1063/1.57501
[research_sawyerwc_montawj_1981]: https://ntrs.nasa.gov/citations/19810036129
[research_sayoodkhalid_rostmartinc_1989]: https://ntrs.nasa.gov/citations/19890012970
[research_sazani_mau_1996]: https://doi.org/10.2514/6.1996-4355
[research_sazonov_2021]: https://doi.org/10.3103/s0278641921030055
[research_scaffidica_stocklinfj_1971]: https://ntrs.nasa.gov/citations/19720007492
[research_scarlatella_guadagnini_2024]: https://doi.org/10.2514/6.2024-2122
[research_scarselli_nicassio_2025]: https://doi.org/10.3390/s25196136
[research_schafer_krull_1985]: https://doi.org/10.4271/850375
[research_schalken_chantler_2018]: https://doi.org/10.1107/s1600577518006549
[research_scheidtdouglas_aulterick_2015]: https://ntrs.nasa.gov/citations/20170007525
[research_scher_dunavant_1966]: https://doi.org/10.2514/6.1966-1519
[research_schierman_ward_2001]: https://doi.org/10.21236/ada436263
[research_schierman_ward_2001_b]: https://doi.org/10.21236/ada436268
[research_schiff_sturek_1981]: https://doi.org/10.21236/ada106060
[research_schindlercarlam_lansawjohn_1990]: https://ntrs.nasa.gov/citations/19900055148
[research_schley_1994]: https://doi.org/10.2514/6.1994-2776
[research_schmidhuber_lopezdelgado_2022]: https://doi.org/10.1007/978-3-030-88593-9_18
[research_schmidt_1955]: https://doi.org/10.21236/ad0086529
[research_schmidt_1980]: https://doi.org/10.2514/6.1980-1589
[research_schmidt_1993]: https://doi.org/10.1016/b978-0-08-041715-8.50016-x
[research_schmidt_donovan_1997]: https://doi.org/10.2514/6.1997-424
[research_schmidt_mann_1996]: https://doi.org/10.2514/6.1996-1199
[research_schmitt_burchett_2004]: https://doi.org/10.2514/6.2004-6254
[research_schnabel_brophy_2018]: https://doi.org/10.2514/6.2018-1626
[research_schneider_garman_1981]: https://doi.org/10.1016/0094-5765(81)90051-5
[research_schneiderjohnr_1992]: https://ntrs.nasa.gov/citations/19950007748
[research_schneiderwc_garmanaa_1979]: https://ntrs.nasa.gov/citations/19790069374
[research_schoelen_1981]: https://doi.org/10.2514/6.1981-1852
[research_schoenekess_volkers_2025]: https://doi.org/10.1016/j.measen.2024.101745
[research_schoneman_buckley_2000]: https://doi.org/10.2514/6.2000-5068
[research_schorr_speas_1995]: https://doi.org/10.2514/6.1995-2722
[research_schubertkabban_uber_2018]: https://doi.org/10.3390/aerospace5020045
[research_schuelein_2008]: https://doi.org/10.2514/6.2008-4000
[research_schuelein_2015]: https://doi.org/10.2514/6.2015-2778
[research_schulein_2009]: https://doi.org/10.1007/978-3-540-85181-3_84
[research_schulerae_1967]: https://ntrs.nasa.gov/citations/19680010575
[research_schulerae_1968]: https://ntrs.nasa.gov/citations/19680062274
[research_schweikhardkeitha_richardswlance_2001]: https://ntrs.nasa.gov/citations/20030066934
[research_schwer_brophy_2018]: https://doi.org/10.2514/6.2018-4968
[research_sciacchitano_wieneke_2016]: https://doi.org/10.1088/0957-0233/27/8/084006
[research_scott_1963]: https://doi.org/10.21236/ad0410255
[research_scwartz_krishnan_2024]: https://doi.org/10.1063/5.0241808
[research_seager_agarwal_2017]: https://doi.org/10.2514/1.t4650
[research_seatechnologyarlingtonva_1998]: https://doi.org/10.21236/ada417821
[research_seaver_chattopadhyay_2012]: https://doi.org/10.21236/ada567056
[research_sedillo_1990]: https://doi.org/10.2514/6.1990-2684
[research_sedlakjoseph_hashmalljoseph_2004]: https://ntrs.nasa.gov/citations/20040171169
[research_sedlakjoseph_weltergary_2003]: https://ntrs.nasa.gov/citations/20040013169
[research_seethaakolli]: https://ntrs.nasa.gov/citations/20210010617
[research_segalcorin_mcdanieljamesc_1991]: https://ntrs.nasa.gov/citations/19910036713
[research_seidel_1965]: https://doi.org/10.21236/ad0613962
[research_seifert_shea_1977]: https://doi.org/10.21236/ada043906
[research_sekikawa_hamada_2014]: https://doi.org/10.1109/ispacs.2014.7024429
[research_sekikawa_hamada_2015]: https://doi.org/10.12720/ijsps.4.1.32-36
[research_sekulamartink_piatakdavidj_2015]: https://ntrs.nasa.gov/citations/20150006849
[research_selvan_2003]: https://doi.org/10.1109/map.2003.1203121
[research_semenov_1994]: https://doi.org/10.1051/jp4:1994550
[research_semmelglenns_davisstevenr_2005]: https://ntrs.nasa.gov/citations/20120003163
[research_senayush_kaur_2026]: https://doi.org/10.56975/jetir.v13i7.584341
[research_senthilkumar_mudholkar_2021]: https://doi.org/10.1088/1757-899x/1130/1/012074
[research_seo_kim_2026]: https://doi.org/10.20944/preprints202608.0260.v1
[research_sepan_lawrence_2010]: https://doi.org/10.2514/6.2010-8760
[research_sepcenkovalentin_margasahayamravi_1990]: https://ntrs.nasa.gov/citations/19920063293
[research_sequeira_sanjay_2021]: https://doi.org/10.1007/978-981-16-0159-0_41
[research_sequence_mining_of_2025]: https://doi.org/10.12677/jast.2025.133008
[research_serceoglu_2024]: https://doi.org/10.52202/078357-0174
[research_sforzinirh_fosterwajr_1976]: https://ntrs.nasa.gov/citations/19770021269
[research_sha_wang_2023]: https://doi.org/10.1016/j.oceaneng.2023.114188
[research_shaffer_ross_2005]: https://doi.org/10.2514/6.2005-6148
[research_shahrokhi_noori]: https://doi.org/10.1115/1.859810.paper316
[research_shan_ren_2017]: https://doi.org/10.1515/mms-2017-0039
[research_shang_2002]: https://doi.org/10.2514/2.1769
[research_shaolin_2017]: https://doi.org/10.11648/j.ijdst.20170303.11
[research_sharifkhodaei_aliabadi_2023]: https://doi.org/10.1016/b978-0-12-822944-6.00046-3
[research_shark_dennis_2010]: https://doi.org/10.2514/6.2010-6784
[research_sharma]: https://doi.org/10.70675/8d5b47a2zae04z441cza310z91b9b33ba9b3
[research_shaw_thakur_2024]: https://doi.org/10.4271/2024-26-0483
[research_sheapatrickr_pinierjeremyt_2018]: https://ntrs.nasa.gov/citations/20200002382
[research_shelley_leclaire_2001]: https://doi.org/10.21236/ada410056
[research_shellmichaelt_mcelyearichardm_2002]: https://ntrs.nasa.gov/citations/20030001567
[research_sheltonjoeyd_frederickroberta_2005]: https://ntrs.nasa.gov/citations/20050210001
[research_shen_sun_2026]: https://doi.org/10.1016/j.dsp.2025.105699
[research_sheng_hua_2011]: https://doi.org/10.1109/emeit.2011.6023563
[research_shenjiy_sharpelonniejr_1998]: https://ntrs.nasa.gov/citations/19980237706
[research_shenoy_sreekumar_2020]: https://doi.org/10.1007/978-981-15-3639-7_18
[research_shepperd_staugler_1999]: https://doi.org/10.2514/6.1999-4209
[research_shermanaaron_2010]: https://ntrs.nasa.gov/citations/20110001612
[research_shi_jing_2013]: https://doi.org/10.1109/ascc.2013.6606246
[research_shi_jing_2013_b]: https://doi.org/10.1504/ijspacese.2013.051769
[research_shi_kuschmierz_2020]: https://doi.org/10.1016/j.measurement.2020.107530
[research_shi_shen_2018]: https://doi.org/10.1109/access.2018.2872778
[research_shibao_tsuboi_2014]: https://doi.org/10.1299/jsmekyushu.2014.67._808-1_
[research_shiguo_yangwang_2011]: https://doi.org/10.1109/ccdc.2011.5968228
[research_shihabimazenm_nguyentienmanh_1994]: https://ntrs.nasa.gov/citations/19970022547
[research_shimaazimi_alirezabdariane_2019]: https://ntrs.nasa.gov/citations/20200001027
[research_shimizu_mizobuchi_2008]: https://doi.org/10.2514/6.2008-4548
[research_sholtis_2002]: https://doi.org/10.1063/1.1449853
[research_shoyama_hirakawa_2024]: https://doi.org/10.52202/078371-0065
[research_shtessel_hall_2000]: https://doi.org/10.2514/6.2000-4155
[research_shtessel_krupp]: https://doi.org/10.1109/ssst.1997.581723
[research_shtessel_krupp_1997]: https://doi.org/10.1109/acc.1997.609256
[research_shtessel_tournes_1997]: https://doi.org/10.2514/6.1997-3533
[research_shtesselyurib_hallcharlese_2000]: https://ntrs.nasa.gov/citations/20000072424
[research_shukla_singh_2020]: https://doi.org/10.1007/978-981-15-5148-2_86
[research_shupingtan_zhibinli_2010]: https://doi.org/10.1109/ccdc.2010.5498526
[research_shyamraj_parthasarathy_2025]: https://doi.org/10.1177/14680874251341024
[research_shyy_papila_2001]: https://doi.org/10.1016/s0376-0421(01)00002-1
[research_siddiqui_smith_1988]: https://doi.org/10.2514/6.1988-3353
[research_sidorovich_1995]: https://doi.org/10.21236/ada301151
[research_sieder_propst_2019]: https://doi.org/10.1051/eucass/201911529
[research_siewert_borgzinner_2024]: https://doi.org/10.1115/imece2024-140670
[research_sihver_kodaira_2016]: https://doi.org/10.1109/aero.2016.7500765
[research_sijtsma_brouwer_2017]: https://doi.org/10.2514/6.2017-3388
[research_sijtsma_brouwer_2018]: https://doi.org/10.1016/j.jsv.2018.02.029
[research_silton_bhagwandin_2012]: https://doi.org/10.2514/6.2012-2906
[research_silton_coyle_2015]: https://doi.org/10.2514/6.2015-2586
[research_silton_coyle_2016]: https://doi.org/10.2514/6.2016-0309
[research_silton_fresconi_2015]: https://doi.org/10.2514/6.2015-1924
[research_silva_amado_2018]: https://doi.org/10.1016/j.measurement.2018.05.061
[research_silva_brojo_2024]: https://doi.org/10.1007/s44245-024-00063-6
[research_silvaopps_b_2011]: https://doi.org/10.5772/25221
[research_silvermanjr_1972]: https://ntrs.nasa.gov/citations/19720018125
[research_simmons_branam_2011]: https://doi.org/10.2514/1.51534
[research_simmonscharles_1994]: https://ntrs.nasa.gov/citations/19940030564
[research_simmswilliamherbertiii_varnavaskosta_2014]: https://ntrs.nasa.gov/citations/20140012879
[research_simon_1956]: https://doi.org/10.21236/ad0088799
[research_simonsraineen_halldavidg_2004]: https://ntrs.nasa.gov/citations/20040082337
[research_simonsraineen_mirandafelixa_2006]: https://ntrs.nasa.gov/citations/20060051726
[research_simonsraineen_mirandafelixa_2008]: https://ntrs.nasa.gov/citations/20090017558
[research_simpsonrs_tranterwh_1968]: https://ntrs.nasa.gov/citations/19690001376
[research_simpsontimothyw_1998]: https://ntrs.nasa.gov/citations/19980046640
[research_sims_hahn_1964]: https://doi.org/10.21236/ad0603567
[research_simsjd_flandrogarya_2004]: https://ntrs.nasa.gov/citations/20040085915
[research_simsjosephd_colemanhughw_1998]: https://ntrs.nasa.gov/citations/19980236002
[research_simswilliamherbertiii_varnavaskostaa_2014]: https://ntrs.nasa.gov/citations/20150003313
[research_sindersonrl_salazarga_1989]: https://ntrs.nasa.gov/citations/19890000434
[research_singelmann_mueller_1948]: https://doi.org/10.21236/ada402594
[research_singer_reinhardt_1963]: https://doi.org/10.21236/ad0419322
[research_singh_luyten_2024]: https://doi.org/10.21203/rs.3.rs-4674857/v1
[research_singhgarima_lozijulien_2016]: https://ntrs.nasa.gov/citations/20190025639
[research_sippel_bussler_2017]: https://doi.org/10.2514/6.2017-2170
[research_siroka_foley_2021]: https://doi.org/10.1088/1361-6501/ac0f23
[research_sitaer_1969]: https://ntrs.nasa.gov/citations/19710004659
[research_sithara_shenil_2022]: https://doi.org/10.1109/icccis56430.2022.10037641
[research_siva_vikramasuriyan_2023]: https://doi.org/10.4273/ijvss.15.2.03
[research_sivan_murmu_2017]: https://doi.org/10.1007/s40032-017-0426-2
[research_sivan_pandian_2018]: https://doi.org/10.18520/cs/v114/i01/38-47
[research_sixteen_channel_1968]: https://ntrs.nasa.gov/citations/19680028087
[research_skariya_sebastian_2014]: https://doi.org/10.3182/20140313-3-in-3024.00064
[research_skinner_gruber_2024]: https://doi.org/10.1016/j.measurement.2024.114891
[research_skobtsov_2024]: https://doi.org/10.17586/0021-3454-2024-67-11-943-950
[research_skobtsov_novoselova_2020]: https://doi.org/10.17586/0021-3454-2020-63-11-1003-1011
[research_slane_morris_2008]: https://doi.org/10.2514/6.2008-7032
[research_slaterdavidc_sternsalan_1995]: https://ntrs.nasa.gov/citations/19960042969
[research_slocumbtravish_andrewsearlhjr_1961]: https://ntrs.nasa.gov/citations/20040006301
[research_small_nuclear_1993]: https://doi.org/10.2514/6.1993-4781
[research_smalleykurtb_brownandrew_2007]: https://ntrs.nasa.gov/citations/20070031864
[research_smallwood_1966]: https://doi.org/10.21236/ad0372384
[research_smallwood_1967]: https://doi.org/10.21236/ad0382136
[research_smart_2015]: https://doi.org/10.64628/aa.x3u3ava6h
[research_smart_technical_2013]: https://doi.org/10.14359/51686286
[research_smeltzerdb_durstonda_1983]: https://ntrs.nasa.gov/citations/19830066993
[research_smith_1978]: https://doi.org/10.21236/ada070310
[research_smith_1983]: https://doi.org/10.2514/6.1983-1547
[research_smith_2011]: https://doi.org/10.1115/imece2011-65379
[research_smith_adelfang_1990]: https://doi.org/10.2514/6.1990-481
[research_smith_schneider_2007]: https://doi.org/10.1016/j.ast.2006.08.007
[research_smith_scott_2001]: https://doi.org/10.2514/6.2001-506
[research_smithandrew_harrisonphil_2010]: https://ntrs.nasa.gov/citations/20100025979
[research_smithbp_duttas_2017]: https://ntrs.nasa.gov/citations/20170009820
[research_smithgw_sforzinirh_1972]: https://ntrs.nasa.gov/citations/19720017173
[research_smithjd_1966]: https://ntrs.nasa.gov/citations/19660030682
[research_smithr_carrt_1973]: https://ntrs.nasa.gov/citations/19730000320
[research_smithsd_1982]: https://ntrs.nasa.gov/citations/19820010442
[research_smithwilliamc_leiwekerobertj_1992]: https://ntrs.nasa.gov/citations/19930053892
[research_snaiki_mirfakhar_2024]: https://doi.org/10.1111/mice.13304
[research_snellgrove_griffin_2003]: https://doi.org/10.2514/6.2003-4918
[research_sniderwj_1974]: https://ntrs.nasa.gov/citations/19750004689
[research_snoddy_dumbacher_2006]: https://doi.org/10.2514/6.2006-5130
[research_snowden_levinson_2007]: https://doi.org/10.21236/ada474915
[research_sohn_2013]: https://doi.org/10.1177/1475921713516701
[research_soldi_jr_1995]: https://doi.org/10.21236/ada301837
[research_solid_rocket_1974]: https://ntrs.nasa.gov/citations/19770020237
[research_solid_rocket_2019]: https://doi.org/10.1017/9781108381376.008
[research_sommersimonc_starkjamesa_1952]: https://ntrs.nasa.gov/citations/19930087078
[research_son_sohn_2015]: https://doi.org/10.1016/j.fuel.2014.11.069
[research_song_bian_2019]: https://doi.org/10.1007/978-981-32-9698-5_20
[research_song_cai_2018]: https://doi.org/10.1061/(asce)as.1943-5525.0000855
[research_song_song_2011]: https://doi.org/10.1109/iceceng.2011.6057472
[research_song_su_2015]: https://doi.org/10.1016/j.proeng.2014.12.639
[research_song_yu_2020]: https://doi.org/10.1109/icsmd50554.2020.9261736
[research_song_yu_2022]: https://doi.org/10.1109/i2mtc48687.2022.9806645
[research_sonibharat_2000]: https://ntrs.nasa.gov/citations/20000116340
[research_sophiavedvik_christopherdkarlgaard_2024]: https://ntrs.nasa.gov/citations/20240001235
[research_sorensenerikmose_ferripaolo_1994]: https://ntrs.nasa.gov/citations/19950010794
[research_sosjy_1966]: https://ntrs.nasa.gov/citations/19660056408
[research_soumyodutta_2020]: https://ntrs.nasa.gov/citations/20200002925
[research_soumyodutta_christopherdkarlgaard_2020]: https://ntrs.nasa.gov/citations/20205001100
[research_sounding_rocket_1967]: https://ntrs.nasa.gov/citations/19680007444
[research_soveyjs_penkopf_1985]: https://ntrs.nasa.gov/citations/19860007955
[research_soveyjs_penkopf_1985_b]: https://ntrs.nasa.gov/citations/19850012949
[research_soveyjs_penkopf_1986]: https://ntrs.nasa.gov/citations/19870027702
[research_space_data]: https://doi.org/10.3403/01353414u
[research_space_data_b]: https://doi.org/10.3403/30337706
[research_space_data_c]: https://doi.org/10.3403/02825862u
[research_space_data_d]: https://doi.org/10.3403/01007741
[research_space_data_e]: https://doi.org/10.3403/30256704
[research_space_engineering]: https://doi.org/10.3403/30288906u
[research_space_engineering_b]: https://doi.org/10.3403/30288900u
[research_space_shuttle_1971]: https://ntrs.nasa.gov/citations/19730006140
[research_space_shuttle_1973]: https://ntrs.nasa.gov/citations/19740005466
[research_space_shuttle_1973_b]: https://ntrs.nasa.gov/citations/19740005468
[research_space_shuttle_1973_c]: https://ntrs.nasa.gov/citations/19740005467
[research_space_systems]: https://doi.org/10.3403/30441499
[research_space_systems_b]: https://doi.org/10.3403/30176278u
[research_space_telemetry_1983]: https://ntrs.nasa.gov/citations/20030001713
[research_space_vehicle_1965]: https://ntrs.nasa.gov/citations/19650021022
[research_spacecraft_telemetry_1968]: https://ntrs.nasa.gov/citations/19680027947
[research_spaceport_america_2011]: https://doi.org/10.1063/pt.5.025773
[research_spacex_gets_2013]: https://doi.org/10.1016/s0262-4079(13)62358-1
[research_spacex_tests_2014]: https://doi.org/10.1016/s0262-4079(14)60750-8
[research_spacex_to_2011]: https://doi.org/10.1063/pt.5.025616
[research_spacex_to_2014]: https://doi.org/10.1063/pt.5.027844
[research_spahncj_penacd_1982]: https://ntrs.nasa.gov/citations/19840032906
[research_spahrjrichard_dickeyrobertr_1951]: https://ntrs.nasa.gov/citations/19930083086
[research_spechtted_nobledavid_2006]: https://ntrs.nasa.gov/citations/20100021335
[research_speerdave_2003]: https://ntrs.nasa.gov/citations/20040034054
[research_spencer]: https://doi.org/10.37099/mtu.dc.etdr/1398
[research_spencer_1999]: https://doi.org/10.1063/1.57511
[research_spencerbjr_fournierrh_1973]: https://ntrs.nasa.gov/citations/19730018266
[research_spherical_rocket_1962]: https://doi.org/10.1109/ee.1962.6434361
[research_spieth_1965]: https://doi.org/10.4271/650802
[research_spradleylw_1975]: https://ntrs.nasa.gov/citations/19760003104
[research_sprattlingjr_1967]: https://doi.org/10.2514/6.1967-236
[research_springer_1996]: https://doi.org/10.2514/6.1996-196
[research_springett_1965]: https://doi.org/10.1016/b978-1-4832-2938-6.50009-x
[research_spurlock_williams_2014]: https://doi.org/10.2514/6.2014-3671
[research_spurny_ploc_2008]: https://doi.org/10.1063/1.2991185
[research_sriganapathy_arjunkumara_2022]: https://doi.org/10.17148/iarjset.2022.9607
[research_sriharshamadhavan_junqiangsun_2021]: https://ntrs.nasa.gov/citations/20210010587
[research_srijayantham_1983]: https://ntrs.nasa.gov/citations/19840003043
[research_srinath_reddy_2010]: https://doi.org/10.1260/1759-3107.1.2.93
[research_srinivasanjeffereym_lichtenstephenm_1994]: https://ntrs.nasa.gov/citations/20060038407
[research_srivastava_thakur_2022]: https://doi.org/10.4273/ijvss.14.5.24
[research_stack_2022]: https://doi.org/10.2172/2003980
[research_stackpoolem_kaod_2013]: https://ntrs.nasa.gov/citations/20140005558
[research_stadler_1998]: https://doi.org/10.2514/6.1998-1504
[research_stahlhphilip_hopkinsrandallc_2016]: https://ntrs.nasa.gov/citations/20160010328
[research_staidps_1978]: https://ntrs.nasa.gov/citations/19780013101
[research_stanbolialice_2013]: https://ntrs.nasa.gov/citations/20140001447
[research_stanbolialice_martinezelmainm_2013]: https://ntrs.nasa.gov/citations/20140001441
[research_stancil_1963]: https://doi.org/10.2514/6.1963-223
[research_stancil_1964]: https://doi.org/10.2514/3.2561
[research_staniszewski_1999]: https://doi.org/10.2514/6.1999-4826
[research_staniszewski_2001]: https://doi.org/10.2514/2.3710
[research_stanley_engelund_1992]: https://doi.org/10.2514/6.1992-3504
[research_stansbury_towhidnejead_2013]: https://doi.org/10.1109/icnsurv.2013.6548610
[research_starkey_2015]: https://doi.org/10.2514/1.a32051
[research_starkey_cannella_2014]: https://doi.org/10.2514/6.2014-3784
[research_starkkw_1972]: https://ntrs.nasa.gov/citations/19720018140
[research_starnerdl_1969]: https://ntrs.nasa.gov/citations/19710003999
[research_starnerdl_1969_b]: https://ntrs.nasa.gov/citations/19710004002
[research_starnone_biesbroek_2006]: https://doi.org/10.2514/6.iac-06-d1.p.1.04
[research_staszewski_sohn_2010]: https://doi.org/10.1002/9780470686652.eae191
[research_stathamtamara_thompsonseth_2017]: https://ntrs.nasa.gov/citations/20170012418
[research_stathamtl_steinwb_2019]: https://ntrs.nasa.gov/citations/20190000721
[research_staudinger_hershey]: https://doi.org/10.1109/aero.2000.878236
[research_stechman_woll_2000]: https://doi.org/10.2514/6.2000-3161
[research_steelewg_molderkj_2005]: https://ntrs.nasa.gov/citations/20060004818
[research_stefanskiphilipl_2015]: https://ntrs.nasa.gov/citations/20150016309
[research_steffenfw_1970]: https://ntrs.nasa.gov/citations/19700033121
[research_steiner_bauer_2026]: https://doi.org/10.2514/6.2026-2883
[research_steinm_1967]: https://ntrs.nasa.gov/citations/19670028612
[research_steinmeyer_howard_1990]: https://doi.org/10.2514/6.1990-2685
[research_stenarson_yhland_2009]: https://doi.org/10.1109/tim.2008.2008578
[research_stephen_rajanna]: https://doi.org/10.1109/icsens.2002.1037380
[research_stephena_2020]: https://doi.org/10.35840/2631-5009/7533
[research_stephencorda_bradfordaneal_1998]: https://ntrs.nasa.gov/citations/19980223961
[research_stephensjulia_hubbarderin_2015]: https://ntrs.nasa.gov/citations/20150021856
[research_stephensjulia_hubbarderin_2016]: https://ntrs.nasa.gov/citations/20160013865
[research_stephensjuliae_hubbarderinp_2016]: https://ntrs.nasa.gov/citations/20160004765
[research_stephisondb_1981]: https://ntrs.nasa.gov/citations/19820006957
[research_stermerrljr_1978]: https://ntrs.nasa.gov/citations/19790054746
[research_sternalans_1996]: https://ntrs.nasa.gov/citations/19980025532
[research_stevehahn_nathanlunetta]: https://ntrs.nasa.gov/citations/20230007261
[research_stevenekrist_nalinaratnayake_2019]: https://ntrs.nasa.gov/citations/20200002387
[research_stevensgl_1980]: https://ntrs.nasa.gov/citations/19800021831
[research_stevensr_1984]: https://ntrs.nasa.gov/citations/19840024568
[research_stewart]: https://doi.org/10.31979/etd.qwkv-999v
[research_stewart_papadopoulos_2020]: https://doi.org/10.2514/6.2020-3841
[research_stewart_tang_2005]: https://doi.org/10.2514/6.2005-357
[research_stewartchristinee_2013]: https://ntrs.nasa.gov/citations/20140003545
[research_stewarteric_mcconnaugheyp_1996]: https://ntrs.nasa.gov/citations/19960029273
[research_stillwaterryana_2009]: https://ntrs.nasa.gov/citations/20090019661
[research_stine_1964]: https://doi.org/10.21236/ad0602455
[research_stoica_dimarco_2026]: https://doi.org/10.2139/ssrn.7193348
[research_stokes_lombaerts_2023]: https://doi.org/10.2514/6.2023-1638
[research_stokesjh_wardsm_1985]: https://ntrs.nasa.gov/citations/19850027077
[research_stoneking_shah_2010]: https://doi.org/10.2514/6.2010-2248
[research_stonekingerict_tsaidean_2009]: https://ntrs.nasa.gov/citations/20090032074
[research_storey_2023]: https://doi.org/10.2514/6.2023-77003
[research_stouffer_1979]: https://doi.org/10.2514/6.1979-490
[research_straightdm_harringtonde_1973]: https://ntrs.nasa.gov/citations/19730017096
[research_strain_gauge_1971]: https://doi.org/10.1111/j.1475-1305.1971.tb01720.x
[research_strauss_1964]: https://doi.org/10.21236/ad0609492
[research_street_1970]: https://doi.org/10.21236/ad0873490
[research_streichronaldc_morgandwayner_2001]: https://ntrs.nasa.gov/citations/20010029164
[research_striepescotta_blanchardrobertc_2007]: https://ntrs.nasa.gov/citations/20070010747
[research_strobel_macneil_2024]: https://doi.org/10.52202/078379-0014
[research_strome_1969]: https://doi.org/10.21236/ad0862053
[research_structural_health]: https://doi.org/10.4271/air6892
[research_structural_health_2008]: https://doi.org/10.1177/1475921708089525
[research_structural_health_2011]: https://doi.org/10.1201/b13182-5
[research_structural_health_2016]: https://doi.org/10.1016/c2012-0-07213-4
[research_structural_health_2016_b]: https://doi.org/10.1016/c2014-0-00994-x
[research_structural_health_2019]: https://doi.org/10.1515/9783110537574-010
[research_structural_health_2021]: https://doi.org/10.1007/978-3-030-72192-3
[research_structural_health_2023]: https://doi.org/10.1515/9783110798722-010
[research_structural_health_2024]: https://doi.org/10.1016/c2022-0-00499-2
[research_structural_health_2025]: https://doi.org/10.1515/9783111621104-010
[research_structural_health_2025_b]: https://doi.org/10.3390/books978-3-7258-3706-9
[research_study_of_1972]: https://ntrs.nasa.gov/citations/19720019034
[research_study_of_1972_b]: https://ntrs.nasa.gov/citations/19720015139
[research_study_of_1972_c]: https://ntrs.nasa.gov/citations/19720015138
[research_study_of_1972_d]: https://ntrs.nasa.gov/citations/19730016074
[research_study_of_1972_e]: https://ntrs.nasa.gov/citations/19720015125
[research_study_of_1972_f]: https://ntrs.nasa.gov/citations/19730016071
[research_study_of_1972_g]: https://ntrs.nasa.gov/citations/19730021073
[research_study_of_1972_h]: https://ntrs.nasa.gov/citations/19720015117
[research_sturdevant_wright_2006]: https://doi.org/10.2514/6.2006-5608
[research_su_dai_2021]: https://doi.org/10.21203/rs.3.rs-554106/v1
[research_su_dai_2021_b]: https://doi.org/10.1016/j.ast.2021.107200
[research_su_liu_2025]: https://doi.org/10.1016/j.asoc.2024.112637
[research_su_liu_2025_b]: https://doi.org/10.1016/j.ast.2024.109839
[research_su_wang_2015]: https://doi.org/10.1016/j.neucom.2015.03.063
[research_success_for_2017]: https://doi.org/10.1088/2058-7058/30/5/20
[research_sudiana_2020]: https://doi.org/10.30536/j.jtd.2020.v18.a3351
[research_suemk_1981]: https://ntrs.nasa.gov/citations/19810010468
[research_suemk_1982]: https://ntrs.nasa.gov/citations/19820022367
[research_suit_kiker_1964]: https://doi.org/10.2514/6.1964-1304
[research_sukachevskyi_2026]: https://doi.org/10.62717/3083-7057-2026-1-034
[research_sulewp_muellertj_1973]: https://ntrs.nasa.gov/citations/19730032085
[research_summerer_putz_2006]: https://doi.org/10.2514/6.iac-06-c3.3.05
[research_summerfield_1960]: https://doi.org/10.1515/9781400879953-005
[research_sun]: https://doi.org/10.31274/rtd-180813-14281
[research_sun_khalid_1998]: https://doi.org/10.2514/6.1998-3571
[research_sun_mahmoodian_2025]: https://doi.org/10.3390/jsan14020022
[research_sun_sun_2026]: https://doi.org/10.1016/j.proci.2026.106141
[research_sundaria_bhagat_2023]: https://doi.org/10.2514/6.2023-3105
[research_sundaria_bhagat_2023_b]: https://doi.org/10.2514/6.2023-3105.c1
[research_sung_park_1960]: https://doi.org/10.2514/8.8549
[research_suresh_rong_2009]: https://doi.org/10.1109/cisda.2009.5356548
[research_surkopamela_1994]: https://ntrs.nasa.gov/citations/19950008644
[research_suroso_gautam_2019]: https://doi.org/10.21924/cst.4.1.2019.109
[research_suzuki_nonaka_2006]: https://doi.org/10.2514/6.2006-3329
[research_suzuki_nonaka_2007]: https://doi.org/10.1016/b978-044453035-6/50034-1
[research_swansongregoryt_empeydanielm_2012]: https://ntrs.nasa.gov/citations/20120011608
[research_swansongt_millerra_2019]: https://ntrs.nasa.gov/citations/20190027144
[research_swathish_rakesh_2024]: https://doi.org/10.1007/978-981-99-6343-0_51
[research_swindell_2015]: https://doi.org/10.12783/shm2015/334
[research_swiss_students_2025]: https://doi.org/10.12968/s1478-2774(25)50079-0
[research_szalkowski_chrostowski_2024]: https://doi.org/10.52202/078371-0106
[research_szmuk_acikmese_2018]: https://doi.org/10.2514/6.2018-0617
[research_t_cm_2017]: https://doi.org/10.4172/2168-9792.1000202
[research_tabakov_zinina_2020]: https://doi.org/10.34759/trd-2020-113-12
[research_tabakov_zinina_2020_b]: https://doi.org/10.34759/trd-2020-111-12
[research_takacs_2013]: https://doi.org/10.21236/ada619553
[research_takagi_morozumi_2014]: https://doi.org/10.2514/6.2014-4033
[research_takahashi_2016]: https://doi.org/10.2514/1.b35771
[research_takahashi_mizobata_1997]: https://doi.org/10.2514/6.1997-192
[research_takahashi_tomita_2015]: https://doi.org/10.2514/6.2015-1671
[research_taki_sergienko_2026]: https://doi.org/10.5194/egusphere-2026-1133
[research_talley_2002]: https://doi.org/10.21236/ada410766
[research_tamami_2020]: https://doi.org/10.31227/osf.io/9bm5g
[research_tan_2017]: https://doi.org/10.12783/dtcse/aita2016/7590
[research_tanck_steadman_1998]: https://doi.org/10.1063/1.54716
[research_tangmh_1971]: https://ntrs.nasa.gov/citations/19710015105
[research_tangmh_pearsongpe_1971]: https://ntrs.nasa.gov/citations/19710029224
[research_tangmh_seficwj_1978]: https://ntrs.nasa.gov/citations/19780025110
[research_taniguchi_mori_2006]: https://doi.org/10.3154/tvsj.26.13
[research_tannensvanzwieten_michaelrhannan_2017]: https://ntrs.nasa.gov/citations/20170006188
[research_tanner_1972]: https://doi.org/10.1017/s0001925900006284
[research_tarapcik_labuda_2001]: https://doi.org/10.1007/978-3-662-05173-3_9
[research_tarifa_pizzuti_2019]: https://doi.org/10.26678/abcm.cobem2019.cob2019-1502
[research_tarrant_crook]: https://doi.org/10.1109/dasc.1997.637278
[research_tarrant_crook_1996]: https://doi.org/10.2514/6.1996-4265
[research_tarrantcharlie_crookjerry_1997]: https://ntrs.nasa.gov/citations/19990116035
[research_tartabinipaulv_2007]: https://ntrs.nasa.gov/citations/20080013374
[research_tartabinipaulv_beatyjamesr_2015]: https://ntrs.nasa.gov/citations/20150008958
[research_task_four_1973]: https://ntrs.nasa.gov/citations/19740011687
[research_tatry_deneu_1997]: https://doi.org/10.1016/s0094-5765(97)00194-x
[research_taylor_2012]: https://doi.org/10.21236/ada566359
[research_taylor_2012_b]: https://doi.org/10.21236/ada563026
[research_taylor_2013]: https://doi.org/10.21236/ada594984
[research_taylor_simmons_1973]: https://doi.org/10.21236/ad0759177
[research_tchengping_schotttimothyd_1988]: https://ntrs.nasa.gov/citations/19890040302
[research_technical_report_1972]: https://ntrs.nasa.gov/citations/19730008042
[research_techniques_for_1965]: https://doi.org/10.1177/003754976500500526
[research_tedrickrn_1964]: https://ntrs.nasa.gov/citations/19650030182
[research_tejwanigopald_langfordlestera_2003]: https://ntrs.nasa.gov/citations/20070008237
[research_tekure_pophali_2021]: https://doi.org/10.1063/5.0066028
[research_telemetry_boards_2009]: https://ntrs.nasa.gov/citations/20090039415
[research_telemetry_modulation_1968]: https://ntrs.nasa.gov/citations/19690018650
[research_telemetry_systems_1996]: https://ntrs.nasa.gov/citations/20020079136
[research_telemetry_technology_1997]: https://ntrs.nasa.gov/citations/20020076218
[research_tellier_1964]: https://doi.org/10.21236/ad0600420
[research_teng_1970]: https://doi.org/10.21236/ad0867762
[research_terhune_hollis_2011]: https://doi.org/10.21236/ada541684
[research_tetervin_1963]: https://doi.org/10.21236/ad0400708
[research_tetlow_schoettle_2000]: https://doi.org/10.2514/6.2000-4180
[research_tewell_1984]: https://doi.org/10.2514/6.1984-781
[research_tharrattce_1975]: https://ntrs.nasa.gov/citations/19750033237
[research_the_design_1964]: https://ntrs.nasa.gov/citations/19660005240
[research_the_invention_2021]: https://doi.org/10.47939/et.v2i6.148
[research_the_measurement_2026]: https://doi.org/10.1002/9781394438303.ch3
[research_the_person_2014]: https://doi.org/10.1177/1475921713520206
[research_the_structural_2004]: https://doi.org/10.1177/1475921704049760
[research_the_structural_2005]: https://doi.org/10.1177/1475921705060441
[research_the_thermal]: https://doi.org/10.1007/978-3-540-69203-4_2
[research_theerthamalai_manisekaran_2005]: https://doi.org/10.2514/6.2005-4967
[research_thiele_gulhan_2018]: https://doi.org/10.2514/1.a34129
[research_thies_2022]: https://doi.org/10.1007/s12567-022-00456-x
[research_thin_film_personal_1965]: https://ntrs.nasa.gov/citations/19650024368
[research_thin_film_personal_1966]: https://ntrs.nasa.gov/citations/19660025028
[research_thin_film_personal_1966_b]: https://ntrs.nasa.gov/citations/19680009074
[research_thin_film_personal_1967]: https://ntrs.nasa.gov/citations/19680000952
[research_thin_film_personal_1967_b]: https://ntrs.nasa.gov/citations/19680007114
[research_thin_film_personal_1968]: https://ntrs.nasa.gov/citations/19680007701
[research_thomas_1942]: https://doi.org/10.21236/ad0494220
[research_thomasmitchele_diamondjohnk_1987]: https://ntrs.nasa.gov/citations/19870043826
[research_thomasrogerj_kankelborgcharlesc_2001]: https://ntrs.nasa.gov/citations/20020015527
[research_thomasscottr_palacdonaldt_2001]: https://ntrs.nasa.gov/citations/20010092480
[research_thomastaylorwalter_2019]: https://ntrs.nasa.gov/citations/20190002678
[research_thomasteasley_dillonpetty]: https://ntrs.nasa.gov/citations/20240000933
[research_thomasteasley_dillonpetty_b]: https://ntrs.nasa.gov/citations/20240015029
[research_thompson_2024]: https://doi.org/10.1016/j.measurement.2024.114841
[research_thompson_russell_1987]: https://doi.org/10.2514/6.1987-2365
[research_thompsonjimrogers_1950]: https://ntrs.nasa.gov/citations/19930086141
[research_thompsonjimrogers_kurbjunmaxc_1948]: https://ntrs.nasa.gov/citations/19930085355
[research_thompsonjimrogers_mathewscharlesw_1947]: https://ntrs.nasa.gov/citations/19930085802
[research_thomson_ebbeson_1991]: https://doi.org/10.1121/1.2029841
[research_thornburg_2002]: https://doi.org/10.21236/ada411890
[research_thornkarene_1993]: https://ntrs.nasa.gov/citations/19940019476
[research_threetgradye_watersericd_2012]: https://ntrs.nasa.gov/citations/20120015996
[research_tiachacht_kahouadji_2023]: https://doi.org/10.1515/9783110791426-006
[research_tian_guo_2020]: https://doi.org/10.1016/j.ast.2020.105983
[research_tian_wang_2024]: https://doi.org/10.1109/aiea62095.2024.10692458
[research_tierney_1993]: https://doi.org/10.2514/6.1993-2364
[research_tieshan_daquan_2016]: https://doi.org/10.5162/etc2016/4.6
[research_time_dependent_in_flight]: https://doi.org/10.4271/air5020
[research_timofeev_2020]: https://doi.org/10.34759/trd-2020-113-06
[research_timothyjg_1973]: https://ntrs.nasa.gov/citations/19730037303
[research_titsworthrc_1963]: https://ntrs.nasa.gov/citations/19630024958
[research_tiwari_kalluru_2005]: https://doi.org/10.2514/6.2005-5274
[research_tjwignall]: https://ntrs.nasa.gov/citations/20260002814
[research_tjwignall_jessegcollins]: https://ntrs.nasa.gov/citations/20220018101
[research_tjwignall_morganawalker]: https://ntrs.nasa.gov/citations/20220016084
[research_tkachenko_salmin_2017]: https://doi.org/10.1016/j.proeng.2017.03.301
[research_tkalenko_1969]: https://doi.org/10.1007/bf01032473
[research_tobey_bastress_1966]: https://doi.org/10.21236/ad0655792
[research_toellerg_blackwelldl_1973]: https://ntrs.nasa.gov/citations/19750012374
[research_tolic_primorac_2019]: https://doi.org/10.3390/en12061029
[research_tolmadzhevata_kantorav_1974]: https://ntrs.nasa.gov/citations/19750002928
[research_tomita_moriya_2008]: https://doi.org/10.2514/6.2008-5232
[research_tomita_takahashi_1999]: https://doi.org/10.2514/6.1999-2586
[research_tomita_takahashi_2001]: https://doi.org/10.2514/6.2001-3560
[research_tomyoung]: https://ntrs.nasa.gov/citations/20220005991
[research_tong_shi_2025]: https://doi.org/10.1016/j.measurement.2025.116786
[research_tooth_1975]: https://doi.org/10.1111/j.1475-1305.1975.tb00128.x
[research_torres_olea_2008]: https://doi.org/10.1109/aps.2008.4619241
[research_tortora_cordelli_2022]: https://doi.org/10.1109/access.2022.3216565
[research_toson_porcarelli_2026]: https://doi.org/10.1109/metroaerospace69299.2026.11646822
[research_toten_fong_1991]: https://doi.org/10.2514/6.1991-5080
[research_tournes_johnson_1998]: https://doi.org/10.2514/6.1998-4119
[research_towler_ryu_2017]: https://doi.org/10.12783/shm2017/14074
[research_trajectory_shaping_2025]: https://doi.org/10.37285/bsp.sacad2025.24
[research_tranken_chandanielc_1992]: https://ntrs.nasa.gov/citations/19930035287
[research_transducer_calibration_1980]: https://doi.org/10.1016/0141-6359(80)90019-7
[research_transducer_calibration_1983]: https://doi.org/10.1016/0308-9126(83)90057-3
[research_tranterwh_1969]: https://ntrs.nasa.gov/citations/19700020510
[research_traudt_2024]: https://doi.org/10.52202/078371-0005
[research_trefnycharlesj_2003]: https://ntrs.nasa.gov/citations/20050214850
[research_trends_on_2014]: https://doi.org/10.1177/1475921714556961
[research_trescotcdjr_fostergv_1973]: https://ntrs.nasa.gov/citations/19730018268
[research_trevinoluisc_1994]: https://ntrs.nasa.gov/citations/19950013221
[research_trigghw_1966]: https://ntrs.nasa.gov/citations/19660057910
[research_trimmer_1968]: https://doi.org/10.21236/ad0669378
[research_trinhhuup_bullardbrad_2002]: https://ntrs.nasa.gov/citations/20030065924
[research_tripathi_misra_2018]: https://doi.org/10.2514/6.2018-1761
[research_tripathi_sucheendran_2019]: https://doi.org/10.1017/aer.2019.146
[research_tripathi_sucheendran_2019_b]: https://doi.org/10.1177/0954410019872349
[research_tripathi_sucheendran_2025]: https://doi.org/10.2139/ssrn.5225190
[research_trippjohns_tchengping_1999]: https://ntrs.nasa.gov/citations/20000013442
[research_trippjohns_tchengping_1999_b]: https://ntrs.nasa.gov/citations/19990105713
[research_tripropellant_engine_2004]: https://doi.org/10.2514/5.9781600866760.0649.0682
[research_trott_1961]: https://doi.org/10.21236/ad0265449
[research_trott_1962]: https://doi.org/10.1121/1.1937067
[research_trumpour_2021]: https://doi.org/10.32920/ryerson.14644173
[research_tsai_1995]: https://doi.org/10.1108/02656719510089993
[research_tsouh_shahb_1993]: https://ntrs.nasa.gov/citations/19930015478
[research_tsouhaiping_hinedisamim_1995]: https://ntrs.nasa.gov/citations/19950070373
[research_tsuboi_jourdaine_2018]: https://doi.org/10.2514/6.2018-1885
[research_tsuboi_kawakami_2011]: https://doi.org/10.2514/6.2011-800
[research_tsukada_fujimoto_2005]: https://doi.org/10.2514/6.2005-1043
[research_tsutsumi_teramoto_2005]: https://doi.org/10.2514/6.2005-4307
[research_tsutsumi_yamaguchi_2007]: https://doi.org/10.2514/6.2007-122
[research_tuckerpk_warsisa_1993]: https://ntrs.nasa.gov/citations/19950017011
[research_tudor_wang_2021]: https://doi.org/10.2514/6.2021-3587
[research_tulpule_1989]: https://doi.org/10.2514/6.1989-2850
[research_tuohy_1998]: https://doi.org/10.2514/6.1998-4177
[research_turmonmichael_bravermanamy_2019]: https://ntrs.nasa.gov/citations/20190001902
[research_turpiekevinr_epleerobertejr_2014]: https://ntrs.nasa.gov/citations/20140017089
[research_tutmez_2016]: https://doi.org/10.1080/10589759.2016.1200575
[research_tuttlesl_meedj_1995]: https://ntrs.nasa.gov/citations/19960001678
[research_tynis_karlgaard_2019]: https://doi.org/10.2514/6.2019-2899
[research_udaiyakumar_iyer_2020]: https://doi.org/10.15866/irease.v13i4.17343
[research_udd_2006]: https://doi.org/10.1364/ofs.2006.mf2
[research_udwadiafe_garbaj_1985]: https://ntrs.nasa.gov/citations/19850022896
[research_umadevi_navas_2017]: https://doi.org/10.1007/s40032-017-0404-8
[research_umholtz_1999]: https://doi.org/10.21236/ada406104
[research_uncertainty_estimation_2016]: https://doi.org/10.1201/9781315370330-11
[research_uncertainty_of]: https://doi.org/10.4271/air1678a
[research_uncertainty_propagation_2006]: https://doi.org/10.1201/9781420011456-10
[research_uncertainty_propagation_2008]: https://doi.org/10.1002/9780470770733.ch17
[research_underwood_swenson_2008]: https://doi.org/10.1117/12.776307
[research_underwoodtcjr_1970]: https://ntrs.nasa.gov/citations/19710030220
[research_united_launch_2015]: https://doi.org/10.1063/pt.5.028795
[research_urban_1959]: https://doi.org/10.21236/ad0405443
[research_urban_1963]: https://doi.org/10.21236/ad0404648
[research_urechjm_chamarroa_1986]: https://ntrs.nasa.gov/citations/19860018821
[research_urschel_cox_2003]: https://doi.org/10.2514/6.2003-5544
[research_usandizaga_beard_2020]: https://doi.org/10.1088/1361-6501/abc027
[research_usellerjamesw_pappasgeorgee_1956]: https://ntrs.nasa.gov/citations/19930089055
[research_usmonov_kretov_2020]: https://doi.org/10.1109/icmeas51739.2020.00031
[research_usryjw_wallacejw_1971]: https://ntrs.nasa.gov/citations/19720004249
[research_vacuum_transducer_1966]: https://doi.org/10.1016/0042-207x(66)92586-3
[research_vagliolaurin_finke_1965]: https://doi.org/10.4271/650801
[research_vaidyanathanrajkumar_papitanilay_2000]: https://ntrs.nasa.gov/citations/20000089909
[research_valdes_1992]: https://doi.org/10.21236/ada257468
[research_vanzwietentannens_gilliganerict_2015]: https://ntrs.nasa.gov/citations/20150002870
[research_vargasmagdab_kennyrjeremy_2010]: https://ntrs.nasa.gov/citations/20100021054
[research_varnavaskostaa_simswilliamherbertiii_2013]: https://ntrs.nasa.gov/citations/20150003146
[research_varnavaskostaa_simswilliamherbertiii_2014]: https://ntrs.nasa.gov/citations/20150003326
[research_vasilchenko_1981]: https://doi.org/10.1007/bf01092388
[research_vasilev_1966]: https://doi.org/10.1007/bf01022289
[research_vasilevskyi_cullinan_2026]: https://doi.org/10.1201/9781003742708-2
[research_vasudevan_das_2017]: https://doi.org/10.1109/hsi.2017.8005044
[research_vathsal]: https://doi.org/10.1109/iecon.1991.239282
[research_vaughn_singh_2007]: https://doi.org/10.1109/aero.2007.352819
[research_vdoviakjw_knottpr_1981]: https://ntrs.nasa.gov/citations/19810009323
[research_vehorn_1967]: https://ntrs.nasa.gov/citations/19670010139
[research_veidt_liew_2013]: https://doi.org/10.1533/9780857093554.3.449
[research_velde_bentley_1969]: https://doi.org/10.2514/3.29833
[research_veldman_2023]: https://doi.org/10.21014/tc22-2022.025
[research_velezjustinianoyoann_stefanskiphilipl_2019]: https://ntrs.nasa.gov/citations/20190033310
[research_velliaris_2021]: https://doi.org/10.32920/ryerson.14663421.v1
[research_ventura_wernimont_2001]: https://doi.org/10.2514/6.2001-3838
[research_venukumar_jagadeesh_2006]: https://doi.org/10.1063/1.2401623
[research_vergallo_layekuakille_2013]: https://doi.org/10.2528/pier13062601
[research_verma_2008]: https://doi.org/10.2514/6.2008-5290
[research_verma_2009]: https://doi.org/10.2514/1.40302
[research_vetter_1977]: https://doi.org/10.21236/adb020024
[research_vibbart_1988]: https://doi.org/10.17764/jiet.1.31.6.fv2023573t120868
[research_vidya_vivekananad_2013]: https://doi.org/10.1109/aicera-icmicr.2013.6576044
[research_vijayan_sureshbabu_2015]: https://doi.org/10.21275/sub156759
[research_vincent_pereira_2025]: https://doi.org/10.61782/fa.2025.0628
[research_vinsonjohn_1998]: https://ntrs.nasa.gov/citations/19990004339
[research_viscardi_monaco_2025]: https://doi.org/10.1117/12.3054950
[research_vishnyak_1995]: https://doi.org/10.2514/6.1995-1593
[research_visscherj_1969]: https://ntrs.nasa.gov/citations/19690000311
[research_viterbiandrew_1961]: https://ntrs.nasa.gov/citations/19660084944
[research_viudez_2018]: https://doi.org/10.1017/jfm.2018.892
[research_viventi_1961]: https://doi.org/10.21236/ad0263599
[research_vogel_kelkar_2009]: https://doi.org/10.2514/6.2009-7383
[research_voinov_melnikov_1996]: https://doi.org/10.2514/6.1996-3218
[research_volkov_kolokutin_2019]: https://doi.org/10.1134/s0020441219020271
[research_vondereschah_1972]: https://ntrs.nasa.gov/citations/19720015124
[research_vorontsov_samoilov_2012]: https://doi.org/10.1007/s11018-012-9969-z
[research_vorozhtsov_matvienko_2002]: https://doi.org/10.2514/6.2002-786
[research_vozhdaev_teperin_2020]: https://doi.org/10.1615/tsagiscij.2020034176
[research_vrolykjohnj_1977]: https://ntrs.nasa.gov/citations/20080012226
[research_wadia_wilson_1981]: https://doi.org/10.2514/6.1981-1372
[research_wagnersean_2014]: https://ntrs.nasa.gov/citations/20160008155
[research_wagnerwr_waldmanbj_1973]: https://ntrs.nasa.gov/citations/19730022956
[research_waldersenmatt_schnarrottoiii_2017]: https://ntrs.nasa.gov/citations/20170004612
[research_wallace_olds_2003]: https://doi.org/10.2514/6.2003-5269
[research_walljohnh_orrjebs_2014]: https://ntrs.nasa.gov/citations/20140008747
[research_walljohnh_vanzwietentannens_2015]: https://ntrs.nasa.gov/citations/20150002959
[research_waltclong_1964]: https://ntrs.nasa.gov/citations/19650002605
[research_walter_shaw_1979]: https://doi.org/10.2514/6.1979-1310
[research_wan_ni_2019]: https://doi.org/10.1061/(asce)as.1943-5525.0000956
[research_wan_shu_2013]: https://doi.org/10.1016/j.physleta.2013.07.052
[research_wan_wang_2012]: https://doi.org/10.2514/6.2012-5965
[research_wang_1998]: https://doi.org/10.21236/ada387033
[research_wang_2004]: https://doi.org/10.2514/6.2004-4016
[research_wang_2015]: https://doi.org/10.7463/0115.0755072
[research_wang_an_2021]: https://doi.org/10.2139/ssrn.3994303
[research_wang_an_2022]: https://doi.org/10.2139/ssrn.4074596
[research_wang_cao_2025]: https://doi.org/10.1186/s42774-024-00192-2
[research_wang_chen_2020]: https://doi.org/10.3390/sym12091572
[research_wang_dai_2026]: https://doi.org/10.1016/j.measurement.2026.122775
[research_wang_ding_2005]: https://doi.org/10.1016/j.sna.2005.01.036
[research_wang_fan_2015]: https://doi.org/10.1016/j.energy.2014.11.017
[research_wang_fang_2023]: https://doi.org/10.1016/j.actaastro.2023.07.012
[research_wang_gan_2025]: https://doi.org/10.1109/comea66280.2025.11241251
[research_wang_hsu_2023]: https://doi.org/10.3390/engproc2023038076
[research_wang_li_2023]: https://doi.org/10.1016/j.engappai.2022.105497
[research_wang_lian_2025]: https://doi.org/10.1007/978-981-96-6235-7_10
[research_wang_liang_2024]: https://doi.org/10.3390/app14031173
[research_wang_liu_2006]: https://doi.org/10.1016/s1000-9361(11)60260-4
[research_wang_liu_2009]: https://doi.org/10.1016/j.actaastro.2008.01.045
[research_wang_liu_2012]: https://doi.org/10.4028/www.scientific.net/amm.232.194
[research_wang_miao_2026]: https://doi.org/10.3390/aerospace13090803
[research_wang_niu_2025]: https://doi.org/10.1063/5.0256511
[research_wang_pei_2026]: https://doi.org/10.1016/j.measurement.2026.121185
[research_wang_qin_2007]: https://doi.org/10.2514/6.2007-5477
[research_wang_ren_2024]: https://doi.org/10.1016/j.measurement.2024.114856
[research_wang_song_2018]: https://doi.org/10.23919/chicc.2018.8483147
[research_wang_song_2018_b]: https://doi.org/10.1109/gncc42960.2018.9019105
[research_wang_song_2019]: https://doi.org/10.1109/cac48633.2019.8997476
[research_wang_song_2021]: https://doi.org/10.1007/978-981-15-8155-7_438
[research_wang_song_2026]: https://doi.org/10.1088/2631-8695/ae3666
[research_wang_wang_2011]: https://doi.org/10.1016/j.mcm.2011.06.060
[research_wang_wang_2019]: https://doi.org/10.1007/s13320-019-0550-0
[research_wang_wang_2024]: https://doi.org/10.2139/ssrn.4819076
[research_wang_wei_2022]: https://doi.org/10.3390/app121910153
[research_wang_wu_2021]: https://doi.org/10.1109/i2mtc50364.2021.9459840
[research_wang_xu_2024]: https://doi.org/10.22541/au.172114671.13104425/v1
[research_wang_xu_2026]: https://doi.org/10.2139/ssrn.6999267
[research_wang_yang_2021]: https://doi.org/10.1155/2021/8872812
[research_wang_yao_2024]: https://doi.org/10.2139/ssrn.5064873
[research_wang_zhang_2019]: https://doi.org/10.1109/ccdc.2019.8833386
[research_wang_zhang_2026]: https://doi.org/10.1016/j.ast.2026.111917
[research_wang_zhou_2024]: https://doi.org/10.1109/cac63892.2024.10865062
[research_wangcc_1965]: https://ntrs.nasa.gov/citations/19660036675
[research_wangteesee_droegealan_2003]: https://ntrs.nasa.gov/citations/20030060643
[research_wangtensee_1998]: https://ntrs.nasa.gov/citations/19980053187
[research_wangtensee_1998_b]: https://ntrs.nasa.gov/citations/19980236891
[research_wangtensee_chenyensen_1990]: https://ntrs.nasa.gov/citations/19900053583
[research_wangtensee_droegealan_2003]: https://ntrs.nasa.gov/citations/20050111470
[research_wangtensee_droegealan_2004]: https://ntrs.nasa.gov/citations/20050165087
[research_wangtensee_williamsrobert_2001]: https://ntrs.nasa.gov/citations/20030016552
[research_wangts_1990]: https://ntrs.nasa.gov/citations/19910014933
[research_wangu_mouyos_1998]: https://doi.org/10.2514/6.1998-5239
[research_wardjr_1970]: https://doi.org/10.2514/6.1970-1386
[research_wardpr_1986]: https://ntrs.nasa.gov/citations/19870028433
[research_washburn_2004]: https://doi.org/10.21236/ada426522
[research_washington_booth_1993]: https://doi.org/10.2514/6.1993-3480
[research_washington_pettis_1968]: https://doi.org/10.21236/ad0695658
[research_watanabe_mikami_2010]: https://doi.org/10.1299/spacee.3.24
[research_watersericd_beersbenjamin_2013]: https://ntrs.nasa.gov/citations/20140003198
[research_watson_neeley_2014]: https://doi.org/10.2514/6.2014-1606
[research_watters_1973]: https://doi.org/10.1121/1.1978187
[research_wattersdm_1986]: https://ntrs.nasa.gov/citations/19860012474
[research_waydavidw_brugarolaspaul_2021]: https://ntrs.nasa.gov/citations/20230005621
[research_weathersg_1975]: https://ntrs.nasa.gov/citations/19760004124
[research_webb_williams_2014]: https://doi.org/10.2514/6.2014-4201
[research_weberromann_yueyisong_2017]: https://ntrs.nasa.gov/citations/20210007857
[research_wechslerer_1981]: https://ntrs.nasa.gov/citations/19810015470
[research_wehrmeyerjoseph_hartfieldroyjjr_2000]: https://ntrs.nasa.gov/citations/20000091021
[research_wehrmeyerjosepha_osbornerobinj_2001]: https://ntrs.nasa.gov/citations/20020020167
[research_wei_chen_2015]: https://doi.org/10.1155/2015/916328
[research_wei_shao_2021]: https://doi.org/10.1109/cac53003.2021.9727820
[research_weidnerthomasj_larsendavidv_2002]: https://ntrs.nasa.gov/citations/20020090804
[research_weijiang_yixinyang_2006]: https://doi.org/10.1109/aps.2006.1711339
[research_weinacht_guidos_1984]: https://doi.org/10.2514/6.1984-2118
[research_weinerbj_1965]: https://ntrs.nasa.gov/citations/19660016291
[research_weinerbj_1965_b]: https://ntrs.nasa.gov/citations/19660009021
[research_wejrzanowski_tymicki_2021]: https://doi.org/10.3390/s21186066
[research_well_1989]: https://doi.org/10.1016/b978-0-08-037869-5.50008-x
[research_weller_1982]: https://doi.org/10.2514/6.1982-1712
[research_wellsg_barothe_1994]: https://ntrs.nasa.gov/citations/20060037927
[research_wellsgeorge_barothedmundc_1993]: https://ntrs.nasa.gov/citations/20060038789
[research_welsh_1985]: https://doi.org/10.21236/ada161403
[research_welshclementj_demoraescarlosa_1951]: https://ntrs.nasa.gov/citations/19930086651
[research_wentzfrankj_lawrencerichardj_2003]: https://ntrs.nasa.gov/citations/20040000726
[research_wenzelsean_huangcalvin_2021]: https://ntrs.nasa.gov/citations/20230005696
[research_wercinskipaul_smithb_2017]: https://ntrs.nasa.gov/citations/20170002062
[research_wernetmarkp_stiegemeierbenjaminr_2017]: https://ntrs.nasa.gov/citations/20170010206
[research_wesslingfrancisc_maybeegeorgew_1989]: https://ntrs.nasa.gov/citations/19900023963
[research_westradouglasg_westjeffreys_2014]: https://ntrs.nasa.gov/citations/20150002584
[research_wetzel]: https://doi.org/10.31274/rtd-180813-10526
[research_white_1957]: https://doi.org/10.1121/1.1909068
[research_white_saunders_2007]: https://doi.org/10.1088/0957-0233/18/7/047
[research_whitehdjr_1964]: https://ntrs.nasa.gov/citations/19640011349
[research_whitehead_2000]: https://doi.org/10.2514/6.2000-3140
[research_whitelawvirginiaa_1987]: https://ntrs.nasa.gov/citations/19880046402
[research_whitemandonalde_valencialisam_2005]: https://ntrs.nasa.gov/citations/20050185568
[research_whitemandonalde_valencialisam_2005_b]: https://ntrs.nasa.gov/citations/20050215644
[research_whitlow_sundaresan_2010]: https://doi.org/10.2514/6.2010-3382
[research_whitmore_sprague_2001]: https://doi.org/10.2514/6.2001-252
[research_whitmorestephena_leondescorneliust_1991]: https://ntrs.nasa.gov/citations/19920037582
[research_whitmorestephena_moestimothyr_1994]: https://ntrs.nasa.gov/citations/19940032870
[research_whitmorestephena_moestimothyr_1999]: https://ntrs.nasa.gov/citations/19990026605
[research_whyte_hathaway_1985]: https://doi.org/10.2514/6.1985-106
[research_wiegmann_schulz_2009]: https://doi.org/10.1364/oe.17.011098
[research_wiesenberg_2000]: https://doi.org/10.2514/6.2000-3182
[research_wikejeffrey_griffithpaul_1989]: https://ntrs.nasa.gov/citations/19900011351
[research_wilcherjh_1976]: https://ntrs.nasa.gov/citations/19760022241
[research_wildermichaelc_redadanielc_2015]: https://ntrs.nasa.gov/citations/20150021846
[research_wileyjohn_kormanvalentin_2008]: https://ntrs.nasa.gov/citations/20090011277
[research_wilks_2006]: https://doi.org/10.21236/ada447214
[research_williams_1965]: https://doi.org/10.1016/b978-0-08-011074-5.50012-9
[research_williams_1968]: https://doi.org/10.21236/ad0847204
[research_williams_1986]: https://doi.org/10.2514/6.1986-2550
[research_williams_2004]: https://doi.org/10.21236/ada420091
[research_williamsglennl_2000]: https://ntrs.nasa.gov/citations/20020027355
[research_williamsmartha_lewismark_2013]: https://ntrs.nasa.gov/citations/20130014150
[research_williamsmsusan_1989]: https://ntrs.nasa.gov/citations/19900006642
[research_williamson_2016]: https://doi.org/10.1049/et.2016.0200
[research_williamsranthony_greenjustins_2018]: https://ntrs.nasa.gov/citations/20190000989
[research_williamsrobertw_1993]: https://ntrs.nasa.gov/citations/19950017195
[research_williamsrw_1996]: https://ntrs.nasa.gov/citations/19960029254
[research_williswilliamdiii_zakrzwskicharlesm_2002]: https://ntrs.nasa.gov/citations/20030025383
[research_wilson_2004]: https://doi.org/10.21236/ada421434
[research_wilson_clark_2009]: https://doi.org/10.2514/6.2009-5486
[research_wilsone_2001]: https://ntrs.nasa.gov/citations/20060033655
[research_wilsonej_1973]: https://ntrs.nasa.gov/citations/19730050642
[research_wilsontruman_xiongxiaoxiong_2016]: https://ntrs.nasa.gov/citations/20170004637
[research_windsor_1979]: https://doi.org/10.2514/6.1979-487
[research_wintzpa_1971]: https://ntrs.nasa.gov/citations/19710022932
[research_wissmann_kahler_2026]: https://doi.org/10.1007/s12567-026-00743-x
[research_witkovsky_2025]: https://doi.org/10.23919/measurement66999.2025.11078719
[research_wnukspjr_wnukvp_1997]: https://ntrs.nasa.gov/citations/19970012640
[research_wolf_2000]: https://doi.org/10.2514/6.2000-1611
[research_wolffjjjr_fitzjf_1972]: https://ntrs.nasa.gov/citations/19720021237
[research_wong_brown_1965]: https://doi.org/10.21236/ad0626273
[research_wong_brown_1968]: https://doi.org/10.21236/ad0681920
[research_wongandrear_polzinkurta_2011]: https://ntrs.nasa.gov/citations/20110015711
[research_wongandrear_toftulalexandra_2011]: https://ntrs.nasa.gov/citations/20110015846
[research_woodfield_1970]: https://doi.org/10.1017/s0001924000047606
[research_woodge_risat_1974]: https://ntrs.nasa.gov/citations/19750039850
[research_woodsthomasn_rottmangaryj_1990]: https://ntrs.nasa.gov/citations/19900047729
[research_woodyard_2026]: https://doi.org/10.2139/ssrn.7049719
[research_worden_inman_2010]: https://doi.org/10.1002/9780470686652.eae188
[research_wrbanekjohnd_fralickgustavec_2007]: https://ntrs.nasa.gov/citations/20070031688
[research_wu_2013]: https://doi.org/10.3923/itj.2013.8328.8331
[research_wu_fuller_1999]: https://doi.org/10.2514/6.1999-2877
[research_wu_li_2026]: https://doi.org/10.1016/j.ast.2025.111507
[research_wu_liu_2015]: https://doi.org/10.1109/cac.2015.7382480
[research_wu_tian_2020]: https://doi.org/10.23919/ccc50068.2020.9188640
[research_wu_yu_2022]: https://doi.org/10.1364/ol.450524
[research_wu_yu_2022_b]: https://doi.org/10.1364/cleopr.2022.cfa12e_03
[research_wu_zhang_2023]: https://doi.org/10.54254/2755-2721/11/20230209
[research_wuilbercq_pescetelli_2014]: https://doi.org/10.2514/6.2014-2362
[research_wuye_yu_2001]: https://doi.org/10.2514/6.2001-3237
[research_wye_teicher_1963]: https://doi.org/10.2514/6.1963-1430
[research_wyettl_maramj_1987]: https://ntrs.nasa.gov/citations/19880042590
[research_x_33_rlv_program_1999]: https://ntrs.nasa.gov/citations/19990041250
[research_xiao_chang_2026]: https://doi.org/10.1007/978-981-92-1183-8_22
[research_xiaowendai_ray]: https://doi.org/10.1109/acc.1995.529323
[research_xie_2010]: https://doi.org/10.3901/jme.2010.22.006
[research_xie_zhang_2020]: https://doi.org/10.1109/access.2020.2997235
[research_xing_feng_2024]: https://doi.org/10.1061/jaeeez.aseng-5340
[research_xinguo_ting_2024]: https://doi.org/10.1109/ccdc62350.2024.10587450
[research_xiong_2018]: https://doi.org/10.2514/6.2018-4676
[research_xiongxiaoxiong_angalamit_2018]: https://ntrs.nasa.gov/citations/20190000976
[research_xiongxiaoxiong_sunjunqiang_2011]: https://ntrs.nasa.gov/citations/20110020758
[research_xiongxiaoxiong_wuaisheng_2012]: https://ntrs.nasa.gov/citations/20120015381
[research_xu_2005]: https://doi.org/10.2514/6.2005-5996
[research_xu_2009]: https://doi.org/10.1061/(asce)0893-1321(2009)22:1(58)
[research_xu_guo_2025]: https://doi.org/10.3390/act14110565
[research_xu_huang_2023]: https://doi.org/10.1016/j.csite.2023.103189
[research_xu_lan_2018]: https://doi.org/10.1109/icmic.2018.8529840
[research_xu_pei_2016]: https://doi.org/10.1109/chicc.2016.7555031
[research_xu_tang_2010]: https://doi.org/10.1109/cmce.2010.5610293
[research_xu_zhang_2024]: https://doi.org/10.1016/b978-0-443-15476-8.00017-4
[research_xu_zhao_2016]: https://doi.org/10.1109/icsp.2016.7877872
[research_xu_zhou_2019]: https://doi.org/10.1364/oe.27.003354
[research_xue_xie_2025]: https://doi.org/10.3390/aerospace12020141
[research_yadav_bodavula_2018]: https://doi.org/10.1017/aer.2018.109
[research_yadav_tripathi_2026]: https://doi.org/10.1177/09544100261434278
[research_yairi_nakatsugaawa]: https://doi.org/10.1109/icsmc.2004.1401008
[research_yairi_ogasawara_2004]: https://doi.org/10.1007/978-3-540-24775-3_31
[research_yamada_2000]: https://doi.org/10.1007/978-94-015-9395-3_7
[research_yamada_nagata_2022]: https://doi.org/10.2514/6.2022-2712
[research_yamakawa_higuchi_2001]: https://doi.org/10.2514/6.2001-1907
[research_yamanishi_kimura_2004]: https://doi.org/10.2514/6.2004-3850
[research_yamashita_nutzel_2026]: https://doi.org/10.5194/egusphere-egu26-17205
[research_yan_wei_2022]: https://doi.org/10.1109/icspcc55723.2022.9984420
[research_yang_1994]: https://doi.org/10.2514/3.26443
[research_yang_2004]: https://doi.org/10.21236/ada428947
[research_yang_2021]: https://doi.org/10.1007/978-981-33-4737-3_6
[research_yang_2022]: https://doi.org/10.1109/tim.2021.3132064
[research_yang_gan_2024]: https://doi.org/10.20944/preprints202405.1410.v1
[research_yang_hu_2006]: https://doi.org/10.2514/6.iac-06-d2.4.03
[research_yang_ma_2021]: https://doi.org/10.1016/j.microrel.2021.114311
[research_yang_naraghi_2020]: https://doi.org/10.2514/6.2020-3817
[research_yang_peng_2025]: https://doi.org/10.1016/j.ifacol.2025.11.481
[research_yang_qiu_2016]: https://doi.org/10.1109/cgncc.2016.7829103
[research_yang_wang_2026]: https://doi.org/10.2514/1.j066459
[research_yang_zhang_2011]: https://doi.org/10.5772/24761
[research_yang_zhang_2026]: https://doi.org/10.1177/14759217261476596
[research_yang_zheng_2019]: https://doi.org/10.1016/j.apm.2018.09.034
[research_yao_liang_2016]: https://doi.org/10.3390/s16071142
[research_yapkengc_2010]: https://ntrs.nasa.gov/citations/20100042148
[research_yapkengc_maciasjesus_2011]: https://ntrs.nasa.gov/citations/20110008039
[research_yavuz_cihan_2026]: https://doi.org/10.1109/rast69551.2026.11672363
[research_ye_law_2014]: https://doi.org/10.1115/1.4026574
[research_yellott_1982]: https://doi.org/10.1016/0042-6989(82)90086-4
[research_yerushalmi_glick_1982]: https://doi.org/10.2514/6.1982-1144
[research_yesmagambetov_mussabekov_2023]: https://doi.org/10.3390/computation11060111
[research_ying_fang_2018]: https://doi.org/10.23919/chicc.2018.8483244
[research_yoda_ito_2015]: https://doi.org/10.1109/cec.2015.7256948
[research_yoshida_kimura_2016]: https://doi.org/10.1007/978-3-319-27748-6_38
[research_youngdr_howardwh_1977]: https://ntrs.nasa.gov/citations/19790026595
[research_yu_campbell_2026]: https://doi.org/10.2514/6.2026-114489
[research_yu_fan_2022]: https://doi.org/10.3390/s22083003
[research_yu_song_2021]: https://doi.org/10.1109/tim.2021.3073442
[research_yu_sun_2014]: https://doi.org/10.4028/www.scientific.net/amm.668-669.406
[research_yu_tian_2016]: https://doi.org/10.1016/b978-0-08-100148-6.00010-x
[research_yu_yang_2018]: https://doi.org/10.1061/9780784481523.219
[research_yu_yu_2024]: https://doi.org/10.1109/tii.2023.3314852
[research_yuan_zhao_2021]: https://doi.org/10.1109/cac53003.2021.9728176
[research_yue_lin_2022]: https://doi.org/10.1016/j.cja.2022.06.022
[research_yuenjh_divsalard_1982]: https://ntrs.nasa.gov/citations/19830013960
[research_zacharymuckler_2022]: https://doi.org/10.18258/27624
[research_zagrai_barnes_2011]: https://doi.org/10.21236/ada563722
[research_zahmaf_smithrh_1929]: https://ntrs.nasa.gov/citations/19930091360
[research_zahzahmohamad_korkoszgregoryj_2000]: https://ntrs.nasa.gov/citations/20080004117
[research_zakharov_botsiura_2024]: https://doi.org/10.24027/2306-7039.3.2026.372056
[research_zakrajsekjunef_1991]: https://ntrs.nasa.gov/citations/19910059658
[research_zamanafroz_bauchmatthew_2011]: https://ntrs.nasa.gov/citations/20110015387
[research_zangl_perez_2025]: https://doi.org/10.1016/j.measen.2024.101322
[research_zapata_roncero_2023]: https://doi.org/10.2139/ssrn.4513799
[research_zappa_malavasi_2013]: https://doi.org/10.1016/j.flowmeasinst.2013.02.002
[research_zaragozaprous_grustangutierrez_2025]: https://doi.org/10.3390/aerospace12020111
[research_zdenek_anthenien_2004]: https://doi.org/10.21236/ada453070
[research_zdravkovic_ilic_2021]: https://doi.org/10.1109/telsiks52058.2021.9606415
[research_zeeshan_waheed_2009]: https://doi.org/10.2514/6.2009-6091
[research_zeidan]: https://doi.org/10.70675/0e4b3962z39a6z47aezbfdczacb84e290d68
[research_zeinsabatto_mikhail_2012]: https://doi.org/10.2514/6.2012-2401
[research_zhang_2016]: https://doi.org/10.1007/978-3-662-49254-3_11
[research_zhang_bi_2018]: https://doi.org/10.5162/ettc2018/2.4
[research_zhang_guo_2017]: https://doi.org/10.2514/6.2017-2372
[research_zhang_hu_2026]: https://doi.org/10.1016/j.measurement.2026.122339
[research_zhang_huang_2018]: https://doi.org/10.1016/j.actaastro.2018.02.040
[research_zhang_huang_2019]: https://doi.org/10.1016/j.actaastro.2019.03.012
[research_zhang_li_2017]: https://doi.org/10.1109/icmsc.2017.7959475
[research_zhang_liu_2022]: https://doi.org/10.1016/j.measurement.2022.111698
[research_zhang_pan_2026]: https://doi.org/10.20944/preprints202609.0474.v1
[research_zhang_pang]: https://doi.org/10.1115/1.859810.paper235
[research_zhang_sheng_2026]: https://doi.org/10.2139/ssrn.7111326
[research_zhang_teng_2019]: https://doi.org/10.1109/fpm45753.2019.9035770
[research_zhang_tian_2018]: https://doi.org/10.1177/0020294018776442
[research_zhang_wang_2019]: https://doi.org/10.1016/j.energy.2018.10.165
[research_zhang_wang_2022]: https://doi.org/10.1016/j.measurement.2022.112171
[research_zhang_xu_2018]: https://doi.org/10.1177/0954410018804093
[research_zhang_xu_2022]: https://doi.org/10.1109/aicit55386.2022.9930173
[research_zhang_yang_2023]: https://doi.org/10.1109/cac59555.2023.10451403
[research_zhang_yu_2016]: https://doi.org/10.1108/aeat-03-2014-0030
[research_zhang_zhang_2022]: https://doi.org/10.1109/icus55513.2022.9986708
[research_zhang_zhang_2024]: https://doi.org/10.1109/taslp.2024.3410869
[research_zhang_zong_2017]: https://doi.org/10.23919/chicc.2017.8027798
[research_zhao_2002]: https://doi.org/10.3901/jme.2002.supp.070
[research_zhao_2022]: https://doi.org/10.1109/aie57029.2022.00123
[research_zhao_cai_2018]: https://doi.org/10.1109/ccdc.2018.8407903
[research_zhao_han_2024]: https://doi.org/10.1109/cac63892.2024.10865196
[research_zhao_he_2018]: https://doi.org/10.1109/gncc42960.2018.9019043
[research_zhao_he_2024]: https://doi.org/10.1061/9780784485484.006
[research_zhao_li_2020]: https://doi.org/10.1155/2020/4313758
[research_zhao_mo_2000]: https://doi.org/10.2514/6.2000-3849
[research_zhao_pan_2025]: https://doi.org/10.1016/j.actaastro.2025.04.058
[research_zhao_wu_2017]: https://doi.org/10.20855/ijav.2017.22.4489
[research_zhao_yu_2024]: https://doi.org/10.1016/j.actaastro.2024.03.018
[research_zhao_zhao_2023]: https://doi.org/10.3390/mi14030587
[research_zhaoqing_hailong_2016]: https://doi.org/10.1109/ccdc.2016.7531012
[research_zhe_meizhen_2018]: https://doi.org/10.1109/ccdc.2018.8407162
[research_zheng_fu_2020]: https://doi.org/10.1016/j.ast.2020.106285
[research_zheng_zhao_2019]: https://doi.org/10.1109/access.2019.2910121
[research_zhengxiang_tao_2018]: https://doi.org/10.1109/gncc42960.2018.9019086
[research_zhi_ran_2015]: https://doi.org/10.1016/j.proeng.2014.12.633
[research_zhipengwang_juliabarsi_2024]: https://ntrs.nasa.gov/citations/20240003638
[research_zhong_jiang_2023]: https://doi.org/10.1108/aeat-09-2022-0247
[research_zhou_hu_2024]: https://doi.org/10.52202/078373-0088
[research_zhou_lin_2014]: https://doi.org/10.4028/www.scientific.net/amm.599-601.1145
[research_zhou_minzhao_2025]: https://doi.org/10.2139/ssrn.5412587
[research_zhou_wang_2024]: https://doi.org/10.2139/ssrn.4895890
[research_zhou_wang_2025]: https://doi.org/10.1016/j.nucengdes.2025.114035
[research_zhou_xu_2024]: https://doi.org/10.1061/9780784485484.187
[research_zhou_zhangduizhong_2016]: https://doi.org/10.1109/eucap.2016.7481329
[research_zhou_zhao_2014]: https://doi.org/10.3390/s140712174
[research_zhou_zhou_2013]: https://doi.org/10.4028/www.scientific.net/amm.446-447.611
[research_zhu_banker_2000]: https://doi.org/10.2514/6.2000-4159
[research_zhu_tian_2015]: https://doi.org/10.1007/s11431-015-5849-5
[research_zhu_tian_2017]: https://doi.org/10.1016/j.cja.2017.02.009
[research_zhu_yan_2023]: https://doi.org/10.1088/1742-6596/2670/1/012016
[research_zhuo_zhang_2023]: https://doi.org/10.23919/ccc58697.2023.10240010
[research_ziegler_1963]: https://doi.org/10.21236/ad0405158
[research_ziemer_lambert_1962]: https://doi.org/10.1121/1.1918238
[research_ziemerjk_2001]: https://ntrs.nasa.gov/citations/20060031972
[research_zilic_hitt_2007]: https://doi.org/10.2514/6.2007-3984
[research_zimmerli_arkwright_2025]: https://doi.org/10.2514/6.2025-0121
[research_zimpfer_1999]: https://doi.org/10.2514/6.1999-4210
[research_zishka_agarwal_2015]: https://doi.org/10.2514/6.2015-2967
[research_zrubekwe_1966]: https://ntrs.nasa.gov/citations/19660056381
[research_zubrin_clapp_1996]: https://doi.org/10.2514/6.1996-4605
[research_zubrin_decher_1991]: https://doi.org/10.2514/6.1991-2058
[research_zuckerwarallanj_scottmichaela_2004]: https://ntrs.nasa.gov/citations/20040082211
[research_zurawka_sahbon_2023]: https://doi.org/10.1109/aero55745.2023.10115859
