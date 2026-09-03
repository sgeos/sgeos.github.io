---
layout: post
mathjax: true
comments: true
title:  "X-Planes: Boeing X-51 Waverider"
date:   2025-11-26 09:00:00 +0000
categories: aerospace history engineering
series: x_planes
series_title: X-Planes
series_index: 52
---
<!-- A348 -->
<script>console.log("A348");</script>

**The X-51A Waverider flew four times, and on the flight that worked the engine under test supplied under eight percent of the vehicle's kinetic energy.** A twenty-six second rocket burn supplied the other ninety-two, and the scramjet took two hundred and ten seconds to add its share [[Boeing X-51 Waverider][ref_x51_wikipedia]] [[Boeing X-51A WaveRider sets record with successful fourth flight][ref_boeing_fourth_flight]].

This is the fifty-second article in the [X-Planes series][related_post_a297_framing], following the [X-1][related_post_a298_bell_x1], the [X-2][related_post_a299_bell_x2], the [X-3][related_post_a300_douglas_x3], the [X-4][related_post_a301_northrop_x4], the [X-5][related_post_a302_bell_x5], the [X-6][related_post_a303_convair_x6], the [X-7][related_post_a304_lockheed_x7], the [X-8][related_post_a305_aerojet_x8], the [X-9][related_post_a306_bell_x9], the [X-10][related_post_a307_north_american_x10], the [X-11][related_post_a308_convair_x11], the [X-12][related_post_a309_convair_x12], the [X-13][related_post_a310_ryan_x13], the [X-14][related_post_a311_bell_x14], the [X-15][related_post_a312_north_american_x15], the [X-16][related_post_a313_bell_x16], the [X-17][related_post_a314_lockheed_x17], the [X-18][related_post_a315_hiller_x18], the [X-19][related_post_a316_curtiss_wright_x19], the [X-20][related_post_a317_boeing_x20], the [X-21][related_post_a318_northrop_x21], the [X-22][related_post_a319_bell_x22], the [X-23][related_post_a320_martin_marietta_x23], the [X-24][related_post_a321_martin_marietta_x24], the [X-25][related_post_a322_bensen_x25], the [X-26][related_post_a323_schweizer_x26], the [X-27][related_post_a324_lockheed_x27], the [X-28][related_post_a325_osprey_x28], the [X-29][related_post_a326_grumman_x29], the [X-30][related_post_a327_rockwell_x30], the [X-31][related_post_a328_rockwell_mbb_x31], the [X-32][related_post_a329_boeing_x32], the [X-33][related_post_a330_lockheed_martin_x33], the [X-34][related_post_a331_orbital_sciences_x34], the [X-35][related_post_a332_lockheed_martin_x35], the [X-36][related_post_a333_mcdonnell_douglas_x36], the [X-37][related_post_a334_boeing_x37], the [X-38][related_post_a335_scaled_composites_x38], the [X-39][related_post_a336_x39_reserved_never_assigned], the [X-40][related_post_a337_boeing_x40], the [X-41][related_post_a338_x41_common_aero_vehicle], the [X-42][related_post_a339_orbital_sciences_x42], the [X-43][related_post_a340_micro_craft_x43], the [X-44][related_post_a341_x44_two_aircraft], the [X-45][related_post_a342_boeing_x45], the [X-46][related_post_a343_boeing_x46], the [X-47][related_post_a344_northrop_grumman_x47], the [X-48][related_post_a345_boeing_x48], the [X-49][related_post_a346_piasecki_x49], and the [X-50][related_post_a347_boeing_x50].

**That is not a criticism of the engine. It is a description of what the experiment was.** The X-51A was not built to accelerate anything. It was built to find out whether a scramjet can keep running, and the answer it returned is that at two hundred seconds the difficulty stops being combustion and becomes everything the combustion is wrapped in.

## The Question This Article Inherits

**The previous scramjet in this series left a claim unfinished.** The [X-43][related_post_a340_micro_craft_x43] reached Mach 9.6 on gaseous hydrogen [[NASA X-43][ref_x43_wikipedia]] and its engine ran for about eleven seconds, and that article recorded that eleven seconds on hydrogen has not demonstrated a propulsion system, because the thermal problem at length is a different problem.

**The X-51A is the experiment that tests that claim.** It flew slower, on a fuel an aeroplane could actually carry, for nineteen times as long.

$$
\frac{210}{11} = 19.1
$$

**And the article's finding is that the earlier claim was right, and right for a reason that is arithmetic rather than rhetorical.**

## The Research Question

**Can a supersonic combustion ramjet run long enough, on a storable fuel, to be a propulsion system rather than a demonstration.**

## Programme Origin

**The Air Force Research Laboratory had been working on hydrocarbon scramjets since the 1990s under a programme called HyTech**, and in 2004 selected a Boeing and Pratt and Whitney Rocketdyne team to build a flight demonstrator [[Air Force Research Laboratory][ref_afrl]] [[X-51 scramjet engine demonstrator, GlobalSecurity][ref_x51_globalsecurity]]. **The X-51 designation was allocated on 27 September 2005** [[Boeing X-51, Directory of U.S. Military Rockets and Missiles][ref_x51_designation]]. The Defense Advanced Research Projects Agency, the National Aeronautics and Space Administration and the Air Force all had a stake [[Defense Advanced Research Projects Agency][ref_darpa]], and that agency treated the X-51 as the predecessor of a more ambitious vehicle called Blackswift which was cancelled in October 2008 [[DARPA Blackswift][ref_blackswift]].

**Four vehicles were built and the programme cost about three hundred million dollars across nine years.** Every one of the four ended in the Pacific by design, since none carried a recovery system.

**The name is a claim about the shape.** A waverider is a configuration whose leading edge is attached to its own bow shock, so that the high pressure behind that shock stays underneath the vehicle and becomes lift instead of leaking away around the edges [[Waverider][ref_waverider]] [[Aerodynamic analysis of hypersonic waverider aircraft][research_waverider_aero_analysis]].

## What a Scramjet Is For, and Why It Cannot Slow the Air Down

**An ordinary jet engine slows the incoming air to a low subsonic speed before burning fuel in it.** That is possible up to roughly Mach 3 and impossible well before Mach 5, and the reason is a single relation.

$$
\frac{T_0}{T} = 1 + \frac{\gamma - 1}{2} M^2
$$

**Stagnation temperature is what the air arrives with and no amount of ducting changes it.** Bringing the flow to rest converts the whole of its kinetic energy into heat, and at the X-51A's cruise condition that gives

$$
T_0 = T \left( 1 + \tfrac{\gamma - 1}{2} M^2 \right) = 216.65 \times 6.202 = 1{,}343.7 \ \mathrm{K}
$$

**being 1,070.5 degrees Celsius before a drop of fuel has been added**, the static temperature at both cruise altitudes being taken from the standard atmosphere [[U.S. Standard Atmosphere][ref_us_standard_atmosphere_ref]] [[U.S. Standard Atmosphere, 1976][research_us_standard_atmosphere]]. At the X-43's Mach 9.6 the same relation gives 4,235.8 kelvin, which is 3,962.6 degrees Celsius, and

$$
\frac{T_{0,\text{X-43}}}{T_{0,\text{X-51}}} = 3.15
$$

**Air at four thousand kelvin is not air any more.** Oxygen begins to dissociate appreciably above about two thousand kelvin, and a gas whose molecules have been pulled apart absorbs the energy of combustion into reassembling itself rather than into pushing on a nozzle.

**The pressures involved are worth seeing before leaving this section.** Bringing the flow to rest isentropically would raise its pressure by

$$
\frac{p_0}{p} = \left( 1 + \frac{\gamma - 1}{2} M^2 \right)^{\!\gamma / (\gamma - 1)} = 594
$$

**and its density by a factor of 95.8.** A duct that captured that flow and stopped it would be holding six hundred atmospheres of stagnation pressure at a thousand degrees, which is a pressure vessel rather than an engine.

**The dynamic pressure has a form that needs no density at all.**

$$
q = \tfrac{1}{2} \rho V^2 = \tfrac{1}{2} \gamma p M^2
$$

**At Mach 5.1 that is 18.2 times the static pressure**, and the cruise value on the fourth flight was 2,731 pounds per square foot, against 1,622 on the first, because the fourth flight was flown ten thousand feet lower where the air is 1.63 times denser.

**So the flow is not slowed to subsonic. It is slowed a little, burned while still supersonic, and expanded.** That is the whole idea, and it is why the engine has no rotating machinery, no compressor and no turbine [[Scramjet][ref_scramjet]] [[Heiser and Pratt, Hypersonic airbreathing propulsion][book_heiser_pratt]] [[Curran and Murthy, Scramjet propulsion][book_curran_murthy]] [[Anderson, Hypersonic and high-temperature gas dynamics][book_anderson_hypersonic]].

**It is also why a scramjet cannot start from a standstill.** There is no machinery to compress anything, so the compression has to be done by going fast, and going fast has to be done by something else.

## Something Else Did Most of the Work

**The X-51A was carried to about fifty thousand feet under the wing of a B-52 and dropped.** A surplus rocket motor from an Army tactical missile then accelerated it to about Mach 4.9 in twenty-six seconds [[MGM-140 ATACMS][ref_atacms]] [[Boeing X-51A WaveRider sets record with successful fourth flight][ref_boeing_fourth_flight]].

**At that point the booster fell away and the scramjet lit, and took the vehicle from Mach 4.9 to Mach 5.1.**

**The arithmetic of that is worth doing plainly.** Kinetic energy goes as the square of speed, so the share of the final energy each stage supplied is

$$
\frac{E_{\text{boost}}}{E_{\text{cruise}}} = \left( \frac{V_{\text{boost}}}{V_{\text{cruise}}} \right)^{\!2}
= \left( \frac{4743.6}{4937.2} \right)^{\!2} = 0.923
$$

**The rocket supplied 92.3 percent of the kinetic energy in twenty-six seconds. The scramjet supplied 7.7 percent in two hundred and ten**, taking

$$
\frac{210}{26} = 8.08
$$

**times as long to do a twelfth as much.**

**This is not an indictment and the article will not pretend it is.** A cruise engine is not an accelerator, and the X-51A was demonstrating cruise. **But it does say what the vehicle was**, and it makes the eventual operational question visible, which is that an air-breathing engine which adds eight percent of the energy still needs a rocket to reach its own operating point.

## The Shape Is the Inlet

**On a hypersonic vehicle the forebody is not in front of the engine. It is part of it.** The compression the engine needs is done by the shock system standing off the underside of the vehicle, and the waverider shape exists so that the shock stays attached to the leading edge and the compressed air stays underneath [[Aerodynamic performance and flow-field characteristics of two waverider-derived hypersonic cruise configurations][research_waverider_derived_performance]] [[Interpretation of waverider performance data using computational fluid dynamics][research_waverider_cfd_interpretation]].

**The relation governing an attached oblique shock is the theta-beta-Mach relation.**

$$
\tan \theta = 2 \cot \beta \, \frac{M_1^2 \sin^2 \beta - 1}{M_1^2 (\gamma + \cos 2\beta) + 2}
$$

**What matters to the flow is not the free-stream Mach number but its component normal to the shock.**

$$
M_{n1} = M_1 \sin \beta
$$

**and it is that component alone which determines the pressure rise.**

$$
\frac{p_2}{p_1} = 1 + \frac{2 \gamma}{\gamma + 1} \left( M_{n1}^2 - 1 \right)
$$

**For a given free-stream Mach number and a given wedge angle there are two solutions and only the weaker one attaches**, and above a maximum deflection angle there is no attached solution at all and the shock stands off as a bow wave. **A waverider is a shape designed backwards from a chosen shock**, which is why the shape is unusual and why it works only near the Mach number it was cut for.

**The consequence for the engine is that the inlet has no independent existence.** A change in angle of attack moves the shock, which changes what the inlet swallows, which changes the combustor. **The forebody, the inlet, the combustor and the afterbody nozzle are one device**, and a bookkeeping error in the drag of the first is a bookkeeping error in the thrust of the last [[Anderson, Modern compressible flow][book_anderson_modern]] [[Bertin, Hypersonic aerothermodynamics][book_bertin]].

## The Second Flight Died at the Inlet

**On 13 June 2011 the second vehicle suffered an inlet unstart after booster separation.** The engine lit on ethylene, which is the easily ignited starting fuel, and did not transition to JP-7.

**An unstart is the inlet ceasing to swallow the flow it was built to swallow.** The internal contraction of a supersonic inlet can only be so large before the shock system cannot be pushed inside it, and past that limit the shock is expelled forwards, the captured mass flow collapses, and the pressure rise propagates upstream in a fraction of a second [[Two-dimensional scramjet inlet unstart model, wind-tunnel blockage and actuation systems][research_inlet_unstart_model]] [[Highlights from a Mach 4 experimental demonstration of inlet mode transition for turbine-based combined cycle hypersonic propulsion][research_inlet_mode_transition]].

**The limit is computable and it is tighter than intuition suggests.** A fixed-geometry inlet must be able to swallow its own shock system, and the test is whether the throat can pass the flow after a normal shock has stood at the entrance and destroyed most of its total pressure. The isentropic area relation

$$
\frac{A}{A^*} = \frac{1}{M} \left[ \frac{2}{\gamma + 1} \left( 1 + \frac{\gamma - 1}{2} M^2 \right) \right]^{(\gamma + 1) / 2(\gamma - 1)}
$$

**gives 27.07 at Mach 5.1**, and a normal shock at that Mach number leaves only 5.72 percent of the total pressure, which enlarges the sonic area by the inverse of that fraction. Requiring the throat to be at least the enlarged sonic area gives the Kantrowitz condition,

$$
\frac{A_{th}}{A_i} \ \geq \ \frac{1}{(p_{02}/p_{01}) \, (A/A^*)_{M_1}} = 0.646
$$

**so the throat cannot be smaller than about two thirds of the capture area, and the internal contraction cannot exceed about 1.55.** A designer wanting more compression than that has to get it outside the inlet, on the forebody, which is the other reason this vehicle is shaped the way it is.

**There is a second way to unstart an engine and it comes from the back.** Adding heat to a duct drives the flow towards Mach one whichever side of it the flow starts on, which is Rayleigh flow, and enough heat release chokes the duct thermally. **A thermal choke is a pressure rise that travels forwards**, and the transition from a light starting fuel to the real fuel is exactly a change in how much heat is being released and where.

**The isolator exists to hold that off.** It is a constant-area duct between inlet and combustor whose job is to contain a shock train, so that the pressure rise from combustion has somewhere to sit without reaching the inlet throat. **Its length is a design margin against the engine unstarting itself**, and the fuel transition the second flight failed at is precisely a change in that pressure rise.

## Heat Is a Rate, and Duration Turns It Into a Load

**This is the article's centre.**

**Stagnation-point heating scales approximately as the square root of density and the cube of velocity**, and the Sutton and Graves correlation puts a constant on it.

$$
\dot{q} = 1.7415 \times 10^{-4} \sqrt{\frac{\rho}{R_n}} \, V^3
$$

**The nose radius is not published and a waverider wants it small**, so the result is a range. At the fourth flight's condition, with density 0.1155 kilograms per cubic metre and velocity 1,504.9 metres per second,

$$
R_n = 5 \ \mathrm{mm} \Rightarrow \dot{q} = 2.85 \ \mathrm{MW/m^2} \qquad
R_n = 50 \ \mathrm{mm} \Rightarrow \dot{q} = 0.90 \ \mathrm{MW/m^2}
$$

**A surface that has to lose that by radiation alone reaches**

$$
T_{\text{rad}} = \left( \frac{\dot{q}}{\varepsilon \sigma} \right)^{\!1/4}
$$

**which is 2,543 degrees Celsius for the sharp edge and 1,839 for the blunt one**, taking emissivity as 0.8. **Both are above what any structural material will hold.**

**That is the waverider's central compromise stated as a temperature.** The shape wants a sharp leading edge, because a sharp edge is what keeps the shock attached and the compressed air underneath. **The thermal problem wants a blunt one**, because heating goes as the inverse square root of the radius. The vehicle has to be sharp enough to work and blunt enough to survive, and there is no setting of that dial that is comfortable.

**By that measure the X-43 was far worse off than the X-51.** On velocity alone,

$$
\frac{\dot{q}_{\text{X-43}}}{\dot{q}_{\text{X-51}}} \approx \left( \frac{9.6}{5.1} \right)^{\!3} = 6.67
$$

**and that is the number a comparison of the two aeroplanes usually stops at.** The X-43 flew hotter. It flew more than three times hotter in stagnation temperature and nearly seven times harder in heating rate.

**But heat is not a rate. It is the integral of a rate.**

$$
Q = \int_0^{t} \dot{q} \, \mathrm{d}t
$$

**And the two flights differ by a factor of nineteen in the upper limit.** Taking the heating rates as constant across each burn, which overstates neither case badly,

$$
\frac{Q_{\text{X-51}}}{Q_{\text{X-43}}} = \frac{19.1}{6.67} = 2.86
$$

**The slower aeroplane absorbed nearly three times as much heat.** That is the sentence the whole programme is about, and it is why an eleven second flight and a two hundred and ten second flight are not the same experiment conducted for different lengths of time. **They are different experiments.**

**The reason is that heat has to get into the structure, and how far it gets depends on the square root of time.** The diffusion length for a solid of thermal diffusivity $\alpha$ after a time $t$ is

$$
\delta \approx \sqrt{\alpha t}
$$

**and for a nickel superalloy, whose diffusivity is about 3.5 millionths of a square metre per second, the two flights differ like this.**

$$
\delta_{\text{X-43}} = \sqrt{(3.5 \times 10^{-6})(11)} = 6.2 \ \mathrm{mm} \qquad
\delta_{\text{X-51}} = \sqrt{(3.5 \times 10^{-6})(210)} = 27.1 \ \mathrm{mm}
$$

**a ratio of**

$$
\frac{\delta_{\text{X-51}}}{\delta_{\text{X-43}}} = \sqrt{\frac{210}{11}} = 4.37
$$

**Six millimetres is a skin. Twenty-seven millimetres is not something an aeroplane can carry as dead mass**, and the difference is the whole distinction between the two experiments.

**A short flight is a structures problem you can solve with heat capacity.** Put enough mass in the leading edge and the heat will not have reached the far side of it before the flight is over. **A long flight is a heat transfer problem** [[Schlichting and Gersten, Boundary-layer theory][book_schlichting]], because the heat arrives at the far side, the structure comes into equilibrium, and the energy has to go somewhere other than into the metal.

## Where the Heat Went, and What It Cost

**It went into the fuel.** The X-51A routed its JP-7 through the walls of the engine before injecting it, so the fuel cooled the structure and was itself heated and cracked on the way [[JP-7][ref_jp7]]. **Cracking a heavy hydrocarbon into lighter fragments absorbs energy** [[Hill and Peterson, Mechanics and thermodynamics of propulsion][book_hill_peterson]], which is why the fuel is described as endothermic, and it also produces a mixture that ignites more readily in a supersonic stream than the parent fuel would.

**One tank did two jobs.** The vehicle carried 270 pounds of JP-7, which is

$$
\frac{270}{4000} = 6.75\%
$$

**of its empty weight**, and that same 270 pounds was the entire heat sink aboard. **There was no other coolant and no other energy supply.**

**The fourth flight burned the tank dry and stopped because it did**, so its average consumption is a real measurement rather than an assumption.

$$
\dot{m}_f = \frac{270}{210} = 1.286 \ \mathrm{lb/s}
$$

**The cooling that buys is finite and computable.** Taking the physical and endothermic heat sink of a cracked hydrocarbon at somewhere between 1,000 and 1,500 British thermal units per pound, the cooling power available while the engine runs is

$$
P_{\text{cool}} = \dot{m}_f \, h_{\text{sink}} = 1.286 \times (1000 \ \text{to} \ 1500) = 1{,}286 \ \text{to} \ 1{,}929 \ \mathrm{Btu/s}
$$

**being between 1,357 and 2,035 kilowatts.**

**And here is the coupling that makes the configuration hard.** The same fuel releases about 18,500 British thermal units per pound when burned, so the heat it can absorb is

$$
\frac{h_{\text{sink}}}{h_{\text{combustion}}} = \frac{1000 \ \text{to} \ 1500}{18500} = 5.4\% \ \text{to} \ 8.1\%
$$

**of the heat it releases.** The coolant capacity of the system is roughly a twentieth of the energy the system is producing, and the two are the same substance, and you cannot increase one without spending the other.

## The Fuel Ran Out Before the Clock Did

**The programme's target was a three hundred second burn and no flight achieved it.** The first reached 143 seconds and the fourth reached 210, being

$$
\frac{143}{300} = 47.7\% \qquad \frac{210}{300} = 70.0\%
$$

**At the fourth flight's demonstrated consumption, three hundred seconds would have required**

$$
m_f = \dot{m}_f \, t = 1.286 \times 300 = 385.7 \ \mathrm{lb}
$$

**which is 42.9 percent more fuel than the vehicle carried.** The 300 second goal and the 270 pound tank were not compatible at the flow rate the engine actually used. **The article does not know which of the two was the later number**, and notes only that the flight which succeeded ran the tank dry rather than running out of objectives.

## What the Flight Says About the Engine

**The programme published no thrust, no specific impulse and no lift-to-drag ratio.** It published a burn time, a fuel load, two Mach numbers and an altitude, and those are enough to bound the rest.

**Start with what the fuel implies about the air.** A kerosene-class fuel burns stoichiometrically at about 0.0685 pounds of fuel per pound of air, so at an equivalence ratio of one the engine was swallowing

$$
\dot{m}_{\text{air}} = \frac{\dot{m}_f}{\phi \, f_{\text{st}}} = \frac{1.286}{0.0685} = 18.8 \ \mathrm{lb/s}
$$

**and twice that if it ran at half stoichiometric**, which a scramjet commonly does.

**Now the range relation, which for a cruising air-breather is Breguet's.**

$$
R = V \, I_{sp} \, \frac{L}{D} \, \ln \frac{W_0}{W_1}
$$

**The vehicle carried 270 pounds of fuel on a 4,000 pound empty weight**, so the mass ratio is 1.0675 and its logarithm is 0.0653. The powered distance is the cruise speed multiplied by the burn time,

$$
R = (1504.9)(210) = 316 \ \mathrm{km} = 171 \ \mathrm{nmi}
$$

**and solving the range relation for what the vehicle must have had gives a product rather than a value.**

$$
I_{sp} \, \frac{L}{D} = \frac{R}{V \ln (W_0 / W_1)} = 3{,}215
$$

**The programme published neither factor and the flight cannot separate them.** At a lift-to-drag ratio of 3, which is respectable for a waverider at this Mach number, the specific impulse is 1,072 seconds. At 2 it is 1,607 and at 4 it is 804. **All three are far better than any rocket**, which is the entire case for air-breathing propulsion.

**And now the number that matters.** The vehicle accelerated from Mach 4.9 to Mach 5.1 over the 210 seconds, so the net force it averaged was

$$
F_{\text{net}} = \frac{m \, \Delta(\tfrac{1}{2} V^2)}{t \, V} = 112 \ \mathrm{lbf}
$$

**which against the measured fuel flow is a net specific impulse of**

$$
I_{sp,\text{net}} = \frac{F_{\text{net}}}{\dot{m}_f} = \frac{112}{1.286} = 87 \ \mathrm{s}
$$

**This is a lower bound and it omits the climb**, because the altitude at booster separation is not published and any climb is energy the engine also had to supply.

**Eighty-seven seconds against an engine that was producing between eight hundred and sixteen hundred.** The difference is drag.

$$
\frac{I_{sp,\text{net}}}{I_{sp}} = 5.4\% \ \text{to} \ 10.9\%
$$

**Between 89 and 95 percent of what the engine made went into pushing the vehicle through the air rather than into speeding it up.** That is not an unusual figure for a cruise vehicle, which by definition is spending its thrust on drag. **It is stated here because it is the same finding as the rest of the article seen from the propulsion side**, which is that the engine was not the marginal component.

## The First Flight Ended at a Seal

**On 26 May 2010 the first vehicle reached Mach 5 at seventy thousand feet and ran its engine for 143 seconds, which was ten times longer than any scramjet had flown before** [[Boeing X-51A WaveRider breaks record in first flight][ref_boeing_first_flight]]. It was cut short by a thermal seal breach at the engine interface, which let hot gas that should have been making thrust leak into the rear of the vehicle.

**The engine grows about three quarters of an inch when it comes up to temperature.** Against a vehicle twenty-five feet long that is

$$
\frac{0.75}{300} = 0.25\%
$$

**of the overall length**, and a seal at that interface has to stay sealed across the whole of it while hot gas is on one side.

**The engine's own length is not published, and the growth implies it.** Thermal expansion is

$$
\Delta L = \alpha L \, \Delta T
$$

**so solving for the length that gives three quarters of an inch**, at a linear expansion coefficient of thirteen millionths per kelvin and a temperature rise of eight hundred kelvin,

$$
L = \frac{\Delta L}{\alpha \, \Delta T} = \frac{0.75}{(13 \times 10^{-6})(800)} = 72 \ \mathrm{in} = 6.0 \ \mathrm{ft}
$$

**which is a plausible engine for a twenty-five foot vehicle**, and is offered as a consistency check on the published growth rather than as a measurement of anything.

**A scramjet has no moving parts and this is what replaces them.** The absence of a compressor and a turbine is the configuration's chief virtue, and what it substitutes is a structure that changes shape by a quarter of a percent while carrying a temperature difference of a thousand degrees, at every joint, for as long as the flight lasts. **That is a duration problem and it does not appear in an eleven second flight at all.**

## The Third Flight Ended at a Latch

**On 14 August 2012 the third vehicle was lost when an upper right control fin unlocked in flight.** The vehicle became uncontrollable and was destroyed.

**A fin unlocked.** Not an unstart, not a flameout, not a thermal failure of the flowpath. A control surface that was supposed to be held in place was not held in place [[Boeing X-51 Waverider][ref_x51_wikipedia]].

## The Flight Record

| Flight | Date | Outcome | Powered seconds |
|---|---|---|---|
| 1 | 26 May 2010 | Mach 5 at 70,000 feet, cut short by a thermal seal breach | 143 |
| 2 | 13 June 2011 | Inlet unstart, no transition from ethylene to JP-7 | none sustained |
| 3 | 14 August 2012 | Upper right fin unlocked, control lost | none |
| 4 | 1 May 2013 | Mach 5.1 at 60,000 feet, tank burned dry | 210 |

**The fourth flight was flown over the Point Mugu sea range and ended in a controlled dive into the Pacific** [[Naval Air Station Point Mugu][ref_point_mugu]].

**Total powered flight across the programme was 353 seconds.** Against three hundred million dollars that is

$$
\frac{300 \times 10^6}{353} = \$849{,}858 \ \text{per second}
$$

**of scramjet operation.** The figure is offered as a measure of how expensive this kind of knowledge is and not as a judgement, since the alternative to buying it was not buying it.

## What the Programme Actually Established

**It established that a hydrocarbon-fuelled scramjet will run for two hundred and ten seconds at Mach 5 in flight, cooled by its own fuel, and that is a genuine and substantial result.** No vehicle had done it and none has done it longer since.

**It also established, without setting out to, where the difficulty in such a vehicle actually lives.** Of the four flights, one was ended by a seal, one by an inlet and a fuel transition, one by a latch, and one by the fuel running out as intended. **The combustion process the programme existed to demonstrate was never the limiting item on any flight.**

**That is the finding, and it is a finding about maturity rather than about failure.** A discipline in which the exotic component works and the ordinary components do not is a discipline whose exotic component has been solved.

## Where the Framing Breaks Down

**Five things in this article are weaker than the rest and the article would rather say so than be caught at it.**

**First, the heat load ratio is a scaling argument and not a calculation.** It treats the heating rate as constant across each burn and it uses the velocity term of a stagnation-point correlation while omitting the density term, on the grounds that the two vehicles flew at broadly comparable dynamic pressures. **The X-43's second powered flight is recorded at a dynamic pressure near a thousand pounds per square foot and the X-51A's fourth flight computes to 2,731**, so the density term is not negligible and including it would raise the X-51A's flux and therefore its load. **The direction of that omission favours the article's conclusion, which is the direction an author should be most suspicious of.**

**Second, the heat sink figure is a literature range and not a measurement of this fuel.** No source consulted gives the X-51A's own fuel heat sink, so 1,000 to 1,500 British thermal units per pound is taken from the open literature on endothermic hydrocarbons. The 5.4 to 8.1 percent result inherits that range entirely.

**Third, the energy share computation uses the boost and cruise Mach numbers of the fourth flight and treats the vehicle mass as constant.** It burned 270 pounds of a roughly four thousand pound vehicle during the cruise, so the mass falls by under seven percent, and accounting for it would move the scramjet's share slightly. **The conclusion that the rocket did the great majority of the work does not depend on that correction.**

**Fourth, six results in this article rest on material and mixture properties this vehicle never published.** The thermal penetration depths use a diffusivity for the nickel superalloy class, the implied engine length uses an expansion coefficient and a temperature rise from the same class, the heat flux and radiation temperatures use a nose radius given only as a range and an assumed emissivity, and the air flow uses a stoichiometric ratio for kerosene rather than for JP-7. **Each of those is stated where it appears and none is presented as a measurement of this aeroplane.**

**The penetration depth is the one that matters most and it is also the most robust.** Its ratio between the two flights is the square root of the ratio of burn times and depends on no material property at all, because the diffusivity cancels. **The absolute depths depend on it entirely.**

**Fifth, the specialist designation directory records plainly that no detailed design data for the X-51A has been published.** There is no published internal geometry against a design literature in which one is the starting point [[Raymer, Aircraft design, a conceptual approach][book_raymer]], no inlet contraction ratio, no combustor length, no isolator length and no engine mass. **Every statement in this article about the flowpath is therefore about scramjets in general and not about this one in particular**, and the article has tried to keep those two registers apart.

## The Contemporary Literature

| Cluster | Records |
|---|---|
| Supersonic combustion and the scramjet flowpath | 1,297 |
| Compressible aerodynamics generally | 1,250 |
| Inlets, starting and the unstart that ended a flight | 476 |
| Heat as a load rather than a rate, and where it goes | 395 |
| Flight test, instrumentation and what was actually measured | 251 |
| Ground facilities and how hypersonic flow is made on Earth | 209 |
| Fuel as coolant, and the endothermic heat sink | 206 |
| Shock and boundary layer interaction | 199 |
| The waverider shape and compression lift | 196 |
| High-temperature materials and structures | 181 |
| Airframe and propulsion as one object | 122 |
| Other hypersonic and aeronautical literature | 116 |
| Computation of hypersonic flow and its validation | 114 |
| Flight control and what the vehicle did about it | 101 |
| Real gas effects and chemical nonequilibrium | 91 |
| Boost, separation and getting to the start line | 90 |
| The atmosphere and the flight condition | 72 |
| **Total** | **5,366** |

### Supersonic combustion and the scramjet flowpath

**The largest cluster, and the thing the programme existed to demonstrate.** Supersonic combustion, isolators, shock trains, combustors, fuel injection into a crossflow, flameholding and mode transition between ramjet and scramjet operation. **This literature is large, mature and was never the limiting item on any X-51A flight**, which is the article's argument stated as a shelf of paper.

**1,297 records.** [[Abbass 2024][research_abbass_2024]] [[Abdel-Salam and Carson 2004][research_abdelsalam_carson_2004]] [[Abdel-Salam et al 2000][research_abdelsalam_tiwari_2000]] [[Abdel-Salam et al 2001][research_abdelsalam_tiwari_2001]] [[Abdel-Salam et al 2001][research_abdelsalam_tiwari_2001_b]] [[Abdollahi et al 2024][research_abdollahi_ranjbar_2024]] [[Abhishek et al 2025][research_abhishek_ramachandra_2025]] [[Acharya 2025][research_acharya_2025]] [[Acharya et al 2020][research_acharya_palies_2020]] [[Adami and Zhu 2007][research_adami_zhu_2007]] [[Adami and Zhu 2008][research_adami_zhu_2008]] [[Adams 1967][research_adams_1967]] [[Aerothermodynamics of the Dual-Mode 2001][research_aerothermodynamics_of_2001]] [[Aguilera and Yu 2017][research_aguilera_yu_2017]] [[Aguilera et al 2009][research_aguilera_pang_2009]] [[Aguilera Munoz and Yu 2014][research_aguileramunoz_yu_2014]] [[Ahmed et al 2025][research_ahmed_hossain_2025]] [[Ahuja and Hartfield 2008][research_ahuja_hartfield_2008]] [[Ahuja and Hartfield 2009][research_ahuja_hartfield_2009]] [[Akihisa et al 2002][research_akihisa_kanda_2002]] [[Aksu and Uslu 2017][research_aksu_uslu_2017]] [[Albertson, Cindy W. and Emami, Saied 2001][research_albertsoncindyw_emamisaied_2001]] [[Alex and Lijo 2021][research_alex_lijo_2021]] [[Alexander and Acharya 2024][research_alexander_acharya_2024]] [[Alexander and Acharya 2025][research_alexander_acharya_2025]] [[Alferov et al 2001][research_alferov_dmitriev_2001]] [[Ali and Fujiwara 2005][research_ali_fujiwara_2005]] [[Ali et al 2003][research_ali_ahmed_2003]] [[Allen et al 2005][research_allen_king_2005]] [[Allen et al 2007][research_allen_hauser_2007]] [[Alter, Stephen J. 2012][research_alterstephenj_2012]] [[Amati et al 2008][research_amati_bruno_2008]] [[Ambe Verma et al 2021][research_ambeverma_muraripandey_2021]] [[Ambe Verma et al 2021][research_ambeverma_muraripandey_2021_b]] [[An et al 2020][research_an_yang_2020]] [[An et al 2021][research_an_wang_2021]] [[Ananthapadmanaban][research_ananthapadmanaban]] [[Andreadis, Dean et al 2002][research_andreadisdean_drakealan_2002]] [[Andreadis, Dean et al 2003][research_andreadisdean_drakealan_2003]] [[Andrews et al 1994][research_andrews_trexler_1994]] [[Antonio Ferri 1964][research_antonioferri_1964]] [[Arad 2024][research_arad_2024]] [[Arad 2026][research_arad_2026]] [[Arens 1961][research_arens_1961]] [[Arnold et al 2023][research_arnold_pace_2023]] [[Assis et al 2019][research_assis_suppandipillai_2019]] [[Attar et al 2026][research_attar_vanderlee_2026]] [[Avasali Dineshkumar et al 2026][research_avasalidineshkumar_mrsvsaritha_2026]] [[Babu 2021][research_babu_2021]] [[Baccarella et al 2020][research_baccarella_liu_2020]] [[Bagaveyev et al 2010][research_bagaveyev_bhagwandin_2010]] [[Bakos][research_bakos]] [[Balaji and Venkatasubbaiah 2025][research_balaji_venkatasubbaiah_2025]] [[Balaji Himakar and Rao 2025][research_balajihimakar_rao_2025]] [[Balland and Vincent-Randonnier 2015][research_balland_vincentrandonnier_2015]] [[Ban et al 2026][research_ban_zhang_2026]] [[Bao et al 2012][research_bao_li_2012]] [[Bao et al 2013][research_bao_duan_2013]] [[Bao et al 2017][research_bao_zhou_2017]] [[Baranovskii and Levin 1991][research_baranovskii_levin_1991]] [[Barber et al 1997][research_barber_orszag_1997]] [[Barreto et al 2021][research_barreto_freire_2021]] [[Barth][research_barth]] [[Barth et al 2014][research_barth_wheatley_2014]] [[Barzegar Gerdroodbary 2020][research_barzegargerdroodbary_2020]] [[Bates 2004][research_bates_2004]] [[Bauer 1966][research_bauer_1966]] [[Bauer et al 1974][research_bauer_muse_1974]] [[Bauer et al 1998][research_bauer_petters_1998]] [[Baumberger et al 2026][research_baumberger_peterson_2026]] [[Baurle and Eklund 2001][research_baurle_eklund_2001]] [[Baurle and Gruber 1998][research_baurle_gruber_1998]] [[Baurle et al 1998][research_baurle_mathur_1998]] [[Baş 2026][research_bas_2026]] [[Ben-Arosh et al 1997][research_benarosh_natan_1997]] [[Ben-Arosh et al 1998][research_benarosh_natan_1998]] [[Ben-Arosh et al 1999][research_benarosh_natan_1999]] [[Ben-Yakar and Hanson 1999][research_benyakar_hanson_1999]] [[Bendot et al 1975][research_bendot_harkins_1975]] [[Benjelloun Touimi and Doom 2025][research_benjellountouimi_doom_2025]] [[Berglund and Fureby 2007][research_berglund_fureby_2007]] [[Berglund et al 2010][research_berglund_fedina_2010]] [[Besserer 1952][research_besserer_1952]] [[Bezerra et al 2024][research_bezerra_souza_2024]] [[Bezerra et al 2026][research_bezerra_desouza_2026]] [[Bhagwandin et al 2009][research_bhagwandin_engblom_2009]] [[Bhatia and Sirignano 1990][research_bhatia_sirignano_1990]] [[Billig 1992][research_billig_1992]] [[Billig 1993][research_billig_1993]] [[Billig 1995][research_billig_1995]] [[Billig et al 1979][research_billig_waltrup_1979]] [[Billig, F. S. 1967][research_billigfs_1967]] [[Billig, F. S. and Grenleski, S. E. 1970][research_billigfs_grenleskise_1970]] [[Birzer and Doolan 2007][research_birzer_doolan_2007]] [[Bogi et al 2025][research_bogi_vinay_2025]] [[Boles and Milligan 2013][research_boles_milligan_2013]] [[Bonanni and Ihme 2023][research_bonanni_ihme_2023]] [[Bordoloi et al 2021][research_bordoloi_pandey_2021]] [[Bordoloi et al 2022][research_bordoloi_pandey_2022]] [[Bordoloi et al 2022][research_bordoloi_pandey_2022_b]] [[Bormotova et al 2003][research_bormotova_volodin_2003]] [[Bouazzi et al 2025][research_bouazzi_ali_2025]] [[Bouchez 2001][research_bouchez_2001]] [[Bouchez and Beyer 2005][research_bouchez_beyer_2005]] [[Bouchez and Beyer 2006][research_bouchez_beyer_2006]] [[Bouchez and Levine 2003][research_bouchez_levine_2003]] [[Bouchez et al 2004][research_bouchez_cahuzac_2004]] [[Bouchez et al 2005][research_bouchez_roudakov_2005]] [[Bouchez et al 2011][research_bouchez_perillat_2011]] [[Boudreau et al 1993][research_boudreau_smithiii_1993]] [[Boulal and Le Pichon 2026][research_boulal_lepichon_2026]] [[Boulal et al 2026][research_boulal_genot_2026]] [[Bowcutt and Haney 1995][research_bowcutt_haney_1995]] [[Bowman et al 1990][research_bowman_hanson_1990]] [[Bowman et al 1991][research_bowman_hanson_1991]] [[Bowman et al 1992][research_bowman_hanson_1992]] [[Boyce and Paull 2001][research_boyce_paull_2001]] [[Boyce et al 2003][research_boyce_gerard_2003]] [[Brabbs, Theodore A. and Robertson, Thomas F. 1987][research_brabbstheodorea_robertsonthomasf_1987]] [[Brahmachary and Ogawa 2021][research_brahmachary_ogawa_2021]] [[Braun et al 2025][research_braun_hammack_2025]] [[Braun et al 2025][research_braun_hammack_2025_b]] [[Braun et al 2026][research_braun_hassan_2026]] [[Bravo et al 2025][research_bravo_plewacki_2025]] [[Brieschenk et al 2013][research_brieschenk_obyrne_2013]] [[Brits][research_brits]] [[Brown and Boyce 2012][research_brown_boyce_2012]] [[Brown et al 2010][research_brown_williams_2010]] [[Brummund and Scheel 2002][research_brummund_scheel_2002]] [[Bura 2017][research_bura_2017]] [[Burke and Poggie 2023][research_burke_poggie_2023]] [[Busa et al 2016][research_busa_brown_2016]] [[Bussing and Murman 1983][research_bussing_murman_1983]] [[Bustard et al 2024][research_bustard_bemis_2024]] [[Byun and Kim 2026][research_byun_kim_2026]] [[Cai et al 2016][research_cai_liu_2016]] [[Cai et al 2017][research_cai_zhou_2017]] [[Cai et al 2018][research_cai_sun_2018]] [[Cai et al 2025][research_cai_zheng_2025]] [[Cain 2002][research_cain_2002]] [[Campuzano and Dang 1995][research_campuzano_dang_1995]] [[Cann 1973][research_cann_1973]] [[Cao et al 2014][research_cao_chang_2014]] [[Cao et al 2015][research_cao_chang_2015]] [[Cao et al 2021][research_cao_brod_2021]] [[Cao et al 2023][research_cao_brod_2023]] [[Carson et al 2004][research_carson_mohieldin_2004]] [[Carter 2012][research_carter_2012]] [[Carter and Springfield 2002][research_carter_springfield_2002]] [[Carvalho et al 2020][research_carvalho_santos_2020]] [[Cavanaugh et al 2025][research_cavanaugh_stramecky_2025]] [[Cavanaugh et al 2026][research_cavanaugh_narayanaswamy_2026]] [[Centlivre 2023][research_centlivre_2023]] [[CFD optimization and test 1994][research_cfd_optimization_1994]] [[Chacon et al 2019][research_chacon_feleo_2019]] [[Chambers Jr 2007][research_chambersjr_2007]] [[Chan and Ihme 2014][research_chan_ihme_2014]] [[Chan and Ihme 2016][research_chan_ihme_2016]] [[Chandrasekhar et al 2014][research_chandrasekhar_ramanujachari_2014]] [[Chang et al 2011][research_chang_li_2011]] [[Chang et al 2014][research_chang_zheng_2014]] [[Charyulu et al 1998][research_charyulu_kurian_1998]] [[Chen et al 2003][research_chen_gu_2003]] [[Chen et al 2009][research_chen_starkey_2009]] [[Chen et al 2013][research_chen_chen_2013]] [[Chen et al 2018][research_chen_yue_2018]] [[Chen et al 2022][research_chen_tian_2022]] [[Chen et al 2024][research_chen_bonanni_2024]] [[Chen et al 2024][research_chen_zhu_2024]] [[Chen et al 2025][research_chen_wang_2025]] [[Chen et al 2025][research_chen_tian_2025]] [[Chen et al 2026][research_chen_guo_2026]] [[Chen et al 2026][research_chen_sethuraman_2026]] [[Cheng et al 2017][research_cheng_tang_2017]] [[Chern et al 2025][research_chern_rockwell_2025]] [[Chi et al 2014][research_chi_wei_2014]] [[Chiu 1987][research_chiu_1987]] [[Chiu 1987][research_chiu_1987_b]] [[Choi and Menon 2009][research_choi_menon_2009]] [[Choi and Yang 2003][research_choi_yang_2003]] [[Choi and Yang 2014][research_choi_yang_2014]] [[Choi et al 2005][research_choi_ma_2005]] [[Choi et al 2011][research_choi_noh_2011]] [[Choi et al 2026][research_choi_choi_2026]] [[Choubey and Pandey 2018][research_choubey_pandey_2018]] [[Choubey and Tiwari 2022][research_choubey_tiwari_2022]] [[Choubey and Tiwari 2022][research_choubey_tiwari_2022_b]] [[Choubey and Tiwari 2022][research_choubey_tiwari_2022_c]] [[Choubey et al 2016][research_choubey_pandey_2016]] [[Choubey et al 2021][research_choubey_yadav_2021]] [[Choubey et al 2022][research_choubey_gaud_2022]] [[Choubey et al 2023][research_choubey_solanki_2023]] [[Choubey et al 2023][research_choubey_solanki_2023_b]] [[Choubey et al 2027][research_choubey_panging_2027]] [[Cisneros-Garibay et al 2022][research_cisnerosgaribay_pantano_2022]] [[Clauser 1954][research_clauser_1954]] [[Clauss et al 1994][research_clauss_sontgen_1994]] [[Clemens 2010][research_clemens_2010]] [[Cocks et al 2013][research_cocks_donohue_2013]] [[Cohen et al 1997][research_cohen_natan_1997]] [[Cohen-Zur and Natan 1998][research_cohenzur_natan_1998]] [[Combustion of High-Energy Fuels 2001][research_combustion_of_2001]] [[Combustion Scaling in an 2012][research_combustion_scaling_2012]] [[Connolly et al 2021][research_connolly_krouse_2021]] [[Corbin et al 2008][research_corbin_wolff_2008]] [[Courtland 2010][research_courtland_2010]] [[Couture et al 2008][research_couture_dechamplain_2008]] [[Crow et al 2012][research_crow_boyd_2012]] [[Cui et al 2018][research_cui_mei_2018]] [[Culick et al 1982][research_culick_marble_1982]] [[Culick et al 1983][research_culick_marble_1983]] [[Culick et al 1985][research_culick_marble_1985]] [[Cuppoletti et al 2020][research_cuppoletti_ombrello_2020]] [[Curran 1996][research_curran_1996]] [[Curran and Craig 1973][research_curran_craig_1973]] [[Cutler, Andrew D. et al 2013][research_cutlerandrewd_magnottigaetano_2013]] [[Cymbalist and Dimotakis 2013][research_cymbalist_dimotakis_2013]] [[da Costa et al 2016][research_dacosta_rolim_2016]] [[da Costa et al 2018][research_dacosta_dasilva_2018]] [[da Silva Junior et al 2018][research_dasilvajunior_pinto_2018]] [[Dai et al 2024][research_dai_chen_2024]] [[Daniau et al 2006][research_daniau_bouchez_2006]] [[Das et al 2021][research_das_pandey_2021]] [[Das et al 2025][research_das_debnath_2025]] [[Davis 1970][research_davis_1970]] [[Davis 1993][research_davis_1993]] [[Davis 1995][research_davis_1995]] [[De Rosa et al 2026][research_derosa_gulizzi_2026]] [[de Siqueira and Ribeiro 2023][research_desiqueira_ribeiro_2023]] [[De VAULT 1957][research_devault_1957]] [[DeBoskey et al 2026][research_deboskey_sahoo_2026]] [[Deng and Kim 2017][research_deng_kim_2017]] [[Deng et al 2017][research_deng_jin_2017]] [[Denman][research_denman]] [[Depiro][research_depiro]] [[Dessornes and Scherrer 2005][research_dessornes_scherrer_2005]] [[Dessornes et al 2001][research_dessornes_scherrer_2001]] [[Dharavath et al 2014][research_dharavath_manna_2014]] [[Dharavath et al 2015][research_dharavath_manna_2015]] [[Dharavath et al 2023][research_dharavath_manna_2023]] [[Di Stefano et al 2018][research_distefano_hosder_2018]] [[Di Stefano et al 2020][research_distefano_hosder_2020]] [[Dickeson et al 2009][research_dickeson_rodriguez_2009]] [[Ding et al 2022][research_ding_zhuo_2022]] [[Do et al 2010][research_do_cappelli_2010]] [[Do et al 2011][research_do_im_2011_c]] [[Do et al 2012][research_do_passaro_2012]] [[Doherty][research_doherty]] [[Doherty][research_doherty_b]] [[Dolnik and Michaels 2025][research_dolnik_michaels_2025]] [[Domel and Thompson 1991][research_domel_thompson_1991]] [[Donbar 2012][research_donbar_2012]] [[Donbar et al 2000][research_donbar_gruber_2000]] [[Dong et al 2015][research_dong_huo_2015]] [[Donohue 2013][research_donohue_2013]] [[Donohue 2014][research_donohue_2014]] [[Donohue, James M. 2012][research_donohuejamesm_2012]] [[dos Santos et al 2025][research_dossantos_passaro_2025]] [[Doster et al 2007][research_doster_king_2007]] [[Drummond 1991][research_drummond_1991]] [[Drummond 1992][research_drummond_1992]] [[Drummond and Weidner 1981][research_drummond_weidner_1981]] [[Drummond, J. P. et al 2007][research_drummondjp_danehypaulm_2007]] [[Du et al 2018][research_du_huang_2018]] [[Du et al 2025][research_du_chen_2025]] [[Dual-Mode Combustion Scramjet 2022][research_dual_mode_combustion_2022]] [[Dubey et al 2025][research_dubey_gupta_2025]] [[Dudebout and Sislian 1994][research_dudebout_sislian_1994]] [[Dufour and Bouchez 2001][research_dufour_bouchez_2001]] [[Dugger 1959][research_dugger_1959]] [[Dutt 1980][research_dutt_1980]] [[Dutta et al 2011][research_dutta_yin_2011]] [[Ebrahimi et al 2007][research_ebrahimi_gaitonde_2007]] [[Edelman et al 1980][research_edelman_harsha_1980]] [[Edwards et al 1975][research_edwards_small_1975]] [[Edwards et al 2011][research_edwards_fulton_2011]] [[Effect of the Configuration 2017][research_effect_of_2017]] [[Effects of compression and 1993][research_effects_of_1993]] [[Eggers 2002][research_eggers_2002]] [[Eggers and Novelli 1999][research_eggers_novelli_1999]] [[Eggers et al 2001][research_eggers_novelli_2001]] [[Eklund et al 2001][research_eklund_baurle_2001]] [[El-Sayed 2016][research_elsayed_2016]] [[Elands et al 1991][research_elands_dijkstra_1991]] [[Elkowitz et al 2023][research_elkowitz_wanchek_2023]] [[Elliott et al 2019][research_elliott_houpt_2019]] [[Emami et al 1995][research_emami_rodi_1995]] [[Emami, Saied et al 1995][research_emamisaied_trexlercarla_1995]] [[Engblom et al 2005][research_engblom_frate_2005]] [[Engblom et al 2012][research_engblom_bellamkonda_2012]] [[Engelund 2001][research_engelund_2001]] [[Escher 2001][research_escher_2001]] [[Eugênio Ribeiro][research_eugenioribeiro]] [[Falempin 1999][research_falempin_1999]] [[Falempin et al 1992][research_falempin_forrat_1992]] [[Falempin et al 2009][research_falempin_minard_2009]] [[Fan et al 2017][research_fan_bing_2017]] [[Fan et al 2026][research_fan_cheng_2026]] [[Fang et al 2020][research_fang_xianyao_2020]] [[Fathauer and Rogers 1993][research_fathauer_rogers_1993]] [[Faulkner 2003][research_faulkner_2003]] [[Faulkner and Weber 1999][research_faulkner_weber_1999]] [[Feng et al 2023][research_feng_luo_2023]] [[Ferguson et al 2011][research_ferguson_dhanasar_2011]] [[Ferguson et al 2016][research_ferguson_dasque_2016]] [[Ferguson et al 2022][research_ferguson_feng_2022]] [[Ferlemann 2005][research_ferlemann_2005]] [[Ferlemann et al 2005][research_ferlemann_mcclinton_2005]] [[Ferreira et al 1996][research_ferreira_carvalhojr_1996]] [[Fischer and Olivier 2011][research_fischer_olivier_2011]] [[Fiévet et al 2015][research_fievet_koo_2015]] [[Flesberg et al 2018][research_flesberg_taghavi_2018]] [[Fletcher 1967][research_fletcher_1967]] [[Flow establishment in a 1990][research_flow_establishment_1990]] [[Foelsche et al 2006][research_foelsche_beckel_2006]] [[Fontan Moura][research_fontanmoura]] [[Fotia 2015][research_fotia_2015]] [[Fotia and Driscoll 2012][research_fotia_driscoll_2012]] [[Fotia and Driscoll 2013][research_fotia_driscoll_2013]] [[Franciscus and Lezberg 1963][research_franciscus_lezberg_1963]] [[Franciscus and Lezberg 1963][research_franciscus_lezberg_1963_b]] [[Friedauer and Segal 1996][research_friedauer_segal_1996]] [[Friedman et al 1953][research_friedman_bennet_1953]] [[Frost][research_frost]] [[Fu et al 2023][research_fu_song_2023]] [[Fu et al 2024][research_fu_song_2024]] [[Fujio and Ogawa 2021][research_fujio_ogawa_2021]] [[Fureby et al 2025][research_fureby_peterson_2025]] [[Fureby et al 2025][research_fureby_nilsson_2025]] [[Förster et al 2016][research_forster_droske_2016]] [[G.Balu et al 2005][research_gbalu_panneerselvam_2005]] [[Gaede and Lopez 1967][research_gaede_lopez_1967]] [[Gallegos et al 2024][research_gallegos_schlussel_2024]] [[Gallegos et al 2024][research_gallegos_schlussel_2024_b]] [[Gamble et al 2008][research_gamble_giel_2008]] [[Gamble et al 2009][research_gamble_haid_2009]] [[Ganapuram et al 2014][research_ganapuram_jangam_2014]] [[Gao et al 2012][research_gao_chang_2012]] [[Gao et al 2020][research_gao_zhang_2020]] [[Gao et al 2020][research_gao_zhang_2020_b]] [[Gao et al 2020][research_gao_zhang_2020_c]] [[Gardner et al 2002][research_gardner_paull_2002]] [[Geerts and Yu 2012][research_geerts_yu_2012]] [[Geerts and Yu 2013][research_geerts_yu_2013]] [[Geerts and Yu 2015][research_geerts_yu_2015]] [[Geerts and Yu 2017][research_geerts_yu_2017]] [[Gehre][research_gehre]] [[Gehre et al 2015][research_gehre_wheatley_2015]] [[Geiger et al 2024][research_geiger_strahan_2024]] [[Geiger et al 2026][research_geiger_strahan_2026]] [[Genin and Menon 2004][research_genin_menon_2004]] [[Gerbsch and Agarwal 1988][research_gerbsch_agarwal_1988]] [[Gernansky 1990][research_gernansky_1990]] [[Ghodke et al 2011][research_ghodke_choi_2011]] [[Gidzak 2015][research_gidzak_2015]] [[Girimaji and Srinivasan 2009][research_girimaji_srinivasan_2009]] [[Gokulakrishnan et al 2006][research_gokulakrishnan_pal_2006]] [[Goldfeld 2003][research_goldfeld_2003]] [[Goodwin and Maxwell 2017][research_goodwin_maxwell_2017]] [[Gopal and Wilson 2016][research_gopal_wilson_2016]] [[Goss and Cook 1948][research_goss_cook_1948]] [[Gounko and Shumskiy 2014][research_gounko_shumskiy_2014]] [[Goyne et al 2006][research_goyne_hall_2006]] [[Graham][research_graham]] [[Grohens et al 2000][research_grohens_dufour_2000]] [[Ground et al 2014][research_ground_zhu_2014]] [[Gruber et al 2004][research_gruber_donbar_2004]] [[Gruenig and Mayinger 1999][research_gruenig_mayinger_1999]] [[Gugulothu 2020][research_gugulothu_2020]] [[Gugulothu and Nutakki 2019][research_gugulothu_nutakki_2019]] [[Guizzo 2004][research_guizzo_2004]] [[Ha et al 2018][research_ha_yoon_2018]] [[Hack][research_hack]] [[Hagenmaier et al 1997][research_hagenmaier_sekar_1997]] [[Hagenmaier et al 2011][research_hagenmaier_eklund_2011]] [[Hagenmaier et al 2013][research_hagenmaier_boles_2013]] [[Hahn et al 2026][research_hahn_lax_2026]] [[Hall and Poggie 2019][research_hall_poggie_2019]] [[Hallion et al 1995][research_hallion_becker_1995]] [[Hammack and Ombrello 2021][research_hammack_ombrello_2021]] [[Han et al 2027][research_han_yang_2027]] [[Hank et al 2008][research_hank_murphy_2008]] [[Hannemann et al 2015][research_hannemann_martinezschramm_2015]] [[Hannemann et al 2017][research_hannemann_martinezschramm_2017]] [[Hao et al 2014][research_hao_chang_2014]] [[Hao et al 2016][research_hao_chang_2016]] [[Harris et al 2023][research_harris_stokes_2023]] [[Hasen et al 2019][research_hasen_karthikeyan_2019]] [[Hass et al 2011][research_hass_cabell_2011]] [[Hass, Neal E. et al 2010][research_hassneale_cabellkarenf_2010]] [[He et al 2022][research_he_tian_2022]] [[He et al 2022][research_he_wang_2022]] [[He et al 2022][research_he_chen_2022]] [[He et al 2023][research_he_liu_2023]] [[He et al 2026][research_he_zhou_2026]] [[Hegde et al 1987][research_hegde_reuter_1987]] [[Helgeson and Chinitz 1995][research_helgeson_chinitz_1995]] [[Heller et al 1998][research_heller_sachs_1998]] [[Henry 1969][research_henry_1969]] [[Heo and Sung 2017][research_heo_sung_2017]] [[Herling et al 1985][research_herling_saheli_1985]] [[Hexia et al 2014][research_hexia_huijun_2014]] [[Hiraiwa et al 1995][research_hiraiwa_tomioka_1995]] [[Hirschel et al 2025][research_hirschel_staudacher_2025]] [[Hitch and Lynch 2009][research_hitch_lynch_2009]] [[Hoeger et al 2010][research_hoeger_king_2010]] [[Hoeger et al 2011][research_hoeger_king_2011]] [[Hoegl and Duesterhaus 1988][research_hoegl_duesterhaus_1988]] [[Hohn and Guelhan 2012][research_hohn_guelhan_2012]] [[Hohn and Gülhan 2011][research_hohn_gulhan_2011]] [[Hohn and Gülhan 2017][research_hohn_gulhan_2017]] [[Hohn and Gülhan 2022][research_hohn_gulhan_2022]] [[Hojnacki 1972][research_hojnacki_1972]] [[Holland and Perkins 1991][research_holland_perkins_1991]] [[Holland and Perkins 1992][research_holland_perkins_1992]] [[Holland, Scott D. 1994][research_hollandscottd_1994]] [[Holland, Scott Douglas 1991][research_hollandscottdouglas_1991]] [[Hong et al 2005][research_hong_lee_2005]] [[Horisawa 2004][research_horisawa_2004]] [[Horisawa et al 2004][research_horisawa_tsuchiya_2004]] [[Hornbeck 1975][research_hornbeck_1975]] [[Hou et al 2020][research_hou_chang_2020]] [[Houria et al 2026][research_houria_albustanji_2026]] [[Hoying, D. et al 1990][research_hoyingd_kelblec_1990]] [[Hsia et al 1989][research_hsia_gross_1989]] [[Hsieh et al 1997][research_hsieh_yang_1997]] [[Hu and Zhu 2017][research_hu_zhu_2017]] [[Hu et al 2013][research_hu_xia_2013]] [[Hu et al 2014][research_hu_chang_2014]] [[Hu et al 2014][research_hu_bao_2014]] [[Hu et al 2015][research_hu_chang_2015]] [[Hu et al 2018][research_hu_wei_2018]] [[Hu et al 2022][research_hu_wang_2022]] [[Hu et al 2026][research_hu_li_2026]] [[Huang and Chen 2021][research_huang_chen_2021]] [[Huang and Yan 2016][research_huang_yan_2016]] [[Huang et al 2002][research_huang_spadaccini_2002]] [[Huang et al 2010][research_huang_pourkashanian_2010]] [[Huang et al 2011][research_huang_wang_2011]] [[Huang et al 2017][research_huang_lianjie_2017]] [[Huang et al 2020][research_huang_yue_2020]] [[Huang et al 2021][research_huang_zhang_2021]] [[Huang et al 2024][research_huang_yao_2024]] [[Huang et al 2025][research_huang_wang_2025]] [[Huang et al 2025][research_huang_wang_2025_b]] [[Huang et al 2026][research_huang_wang_2026]] [[Huebner and Tatum 1991][research_huebner_tatum_1991]] [[Humphrey and Culick 1987][research_humphrey_culick_1987]] [[Hunt][research_hunt]] [[Hunt and Hunt 2020][research_hunt_hunt_2020]] [[Hunt and Hunt 2021][research_hunt_hunt_2021]] [[Hunt et al 2019][research_hunt_ground_2019]] [[Hutzel et al 2011][research_hutzel_decker_2011]] [[Hutzel et al 2011][research_hutzel_decker_2011_b]] [[Hyunwoo et al 2023][research_hyunwoo_kang_2023]] [[Iannelli 2007][research_iannelli_2007_b]] [[Iannelli 2008][research_iannelli_2008]] [[Idris et al 2014][research_idris_saad_2014]] [[Idris et al 2015][research_idris_saad_2015]] [[Igra 2026][research_igra_2026]] [[Iida and Komai 1992][research_iida_komai_1992]] [[Ikawa 1989][research_ikawa_1989]] [[Ikawa 1991][research_ikawa_1991]] [[Ilie and Sullivan 2021][research_ilie_sullivan_2021]] [[Ilie et al 2023][research_ilie_chan_2023]] [[Im and Do 2018][research_im_do_2018]] [[Inamura et al 1996][research_inamura_sei_1996]] [[Influence of the rising 2023][research_influence_of_2023]] [[Ingenito 2015][research_ingenito_2015]] [[Ingenito 2021][research_ingenito_2021]] [[Ingenito 2021][research_ingenito_2021_c]] [[Ingenito 2021][research_ingenito_2021_d]] [[Ingenito 2021][research_ingenito_2021_e]] [[Ingenito 2021][research_ingenito_2021_f]] [[Introduction Special Section on 2014][research_introduction_special_2014]] [[Investigation of mixing characteristics 2023][research_investigation_of_2023]] [[Ispir and Saracoglu 2019][research_ispir_saracoglu_2019]] [[Ispir et al 2023][research_ispir_zdybal_2023]] [[Itoh 2007][research_itoh_2007]] [[Itoh et al 2002][research_itoh_ueda_2002]] [[Izard et al 2009][research_izard_lehnasch_2009]] [[Jackson et al 2015][research_jackson_gruber_2015]] [[Janarthanam and Babu 2012][research_janarthanam_babu_2012]] [[Jaskowiak, Martha H. 2004][research_jaskowiakmarthah_2004]] [[Jazra and Smart 2011][research_jazra_smart_2011]] [[Jazra et al 2013][research_jazra_preller_2013]] [[Jensen and Braendlein 1996][research_jensen_braendlein_1996]] [[Jeong et al 2008][research_jeong_obyrne_2008]] [[Jeong et al 2008][research_jeong_obyrne_2008_b]] [[Jeong et al 2020][research_jeong_obyrne_2020]] [[Ji et al 2024][research_ji_he_2024]] [[Ji et al 2025][research_ji_cai_2025]] [[Jian and Yude 2024][research_jian_yude_2024]] [[Jianchen et al 2014][research_jianchen_yuzhen_2014]] [[Jiang et al 2010][research_jiang_zhang_2010]] [[Jiang et al 2023][research_jiang_wang_2023]] [[Jiang et al 2025][research_jiang_zhan_2025]] [[Jianqiang et al 2016][research_jianqiang_jinlong_2016]] [[Jiao et al 2018][research_jiao_chang_2018]] [[Jiao et al 2021][research_jiao_song_2021]] [[Jin et al 2016][research_jin_huang_2016]] [[Jin et al 2022][research_jin_xu_2022]] [[Jin et al 2023][research_jin_choi_2023]] [[Jin et al 2024][research_jin_choi_2024]] [[Jing et al 2007][research_jing_shuo_2007]] [[Jingqi and Yulong 2024][research_jingqi_yulong_2024]] [[Jo et al 2024][research_jo_sung_2024]] [[Jo et al 2025][research_jo_sung_2025]] [[Jo et al 2026][research_jo_sung_2026]] [[Johnson et al 2022][research_johnson_jenquin_2022]] [[Juluru Sandeep and AVSS Kumara Swami Gupta 2023][research_julurusandeep_avsskumaraswamigupta_2023]] [[K et al 2020][research_k_danish_2020]] [[Kadosh and Natan 2020][research_kadosh_natan_2020]] [[Kai-li and Kun-yuan 2011][research_kaili_kunyuan_2011]] [[Kailasanath et al 1986][research_kailasanath_gardner_1986]] [[Kalra et al 2018][research_kalra_shewale_2018]] [[Kalra et al 2018][research_kalra_shewale_2018_b]] [[Kamath et al 1991][research_kamath_mao_1991]] [[Kanapathipillai and Yu 2024][research_kanapathipillai_yu_2024]] [[Kanapathipillai et al 2020][research_kanapathipillai_chang_2020]] [[Kanapathipillai et al 2020][research_kanapathipillai_chang_2020_b]] [[Kanda 1998][research_kanda_1998]] [[Kanda 1998][research_kanda_1998_b]] [[Kanda 2000][research_kanda_2000]] [[Kanda et al 1993][research_kanda_masuya_1993]] [[Kanda et al 2001][research_kanda_chinzei_2001]] [[Kanda et al 2003][research_kanda_hiraiwa_2003]] [[Kandula and Kummitha 2025][research_kandula_kummitha_2025]] [[Karanian and Kepler 1965][research_karanian_kepler_1965]] [[Kato and Im 2019][research_kato_im_2019]] [[Kato et al 2006][research_kato_kanda_2006]] [[Kay et al 1990][research_kay_peschke_1990]] [[Kay, I. W. et al 1992][research_kayiw_peschkewt_1992]] [[Kay, Ira W. 1989][research_kayiraw_1989]] [[Keanini et al 1989][research_keanini_yu_1989]] [[Kellenberger and Ciccarelli 2015][research_kellenberger_ciccarelli_2015]] [[Kenworthy 1967][research_kenworthy_1967]] [[Kepler and Champagne 1989][research_kepler_champagne_1989]] [[Keshmiri et al 2006][research_keshmiri_colgren_2006_c]] [[Khan et al 2018][research_khan_tahmid_2018]] [[Kim and Menon 1999][research_kim_menon_1999]] [[Kim et al 2004][research_kim_baek_2004]] [[Kim et al 2010][research_kim_jeon_2010]] [[Kim et al 2020][research_kim_han_2020]] [[Kim et al 2025][research_kim_seo_2025]] [[Kim et al 2025][research_kim_seo_2025_b]] [[Kimmerly][research_kimmerly]] [[Kireeti et al 2022][research_kireeti_ravikiransastry_2022]] [[Kirkby 1964][research_kirkby_1964]] [[Kishida 2006][research_kishida_2006]] [[Kishore and Sunitha 1977][research_kishore_sunitha_1977]] [[Kobayashi et al 2003][research_kobayashi_tomioka_2003]] [[Kobayashi et al 2007][research_kobayashi_kanda_2007]] [[Kodera et al 2005][research_kodera_sunami_2005]] [[Kodera et al 2007][research_kodera_yang_2007]] [[Kong et al 2020][research_kong_chang_2020]] [[Kong et al 2021][research_kong_chang_2021]] [[Krawczyk et al 1986][research_krawczyk_rajendran_1986]] [[Kubo et al 2014][research_kubo_tomioka_2014]] [[Kumar 1992][research_kumar_1992]] [[Kumar and Ghosh 2024][research_kumar_ghosh_2024]] [[Kumar et al 2022][research_kumar_iyer_2022]] [[Kumar et al 2023][research_kumar_pranaykumar_2023]] [[Kumar Gugulothu et al 2020][research_kumargugulothu_bhaskar_2020]] [[Kumm and Bitondo 1953][research_kumm_bitondo_1953]] [[Kummitha 2022][research_kummitha_2022]] [[Kummitha 2022][research_kummitha_2022_b]] [[Kummitha 2024][research_kummitha_2024]] [[Kummitha and Kandula 2026][research_kummitha_kandula_2026]] [[Kummitha and Pandey 2020][research_kummitha_pandey_2020]] [[Kummitha and Pandey 2021][research_kummitha_pandey_2021]] [[Kummitha et al 2017][research_kummitha_suneetha_2017]] [[Kurtz et al 2015][research_kurtz_aizengendler_2015]] [[Kydd and Mullaney 1961][research_kydd_mullaney_1961]] [[La Sorsa et al 2025][research_lasorsa_kotler_2025]] [[Ladeinde 2019][research_ladeinde_2019]] [[Ladeinde 2020][research_ladeinde_2020]] [[Landau and Yeneriz 1965][research_landau_yeneriz_1965]] [[Landrum and Tournes 2002][research_landrum_tournes_2002]] [[Landsberg et al 2016][research_landsberg_wheatley_2016]] [[Landsberg et al 2020][research_landsberg_vanyai_2020]] [[Landsberg et al 2021][research_landsberg_curran_2021]] [[Landsberg et al 2022][research_landsberg_curran_2022]] [[Laurence et al 2015][research_laurence_lieber_2015]] [[Law 2004][research_law_2004]] [[Le et al 2005][research_le_goyne_2005]] [[Le et al 2006][research_le_goyne_2006]] [[Le et al 2008][research_le_goyne_2008]] [[Leckie][research_leckie]] [[Lee 1995][research_lee_1995]] [[Lee 2006][research_lee_2006]] [[Lee 2006][research_lee_2006_b]] [[Lee 2012][research_lee_2012]] [[Lee and Kang 2019][research_lee_kang_2019]] [[Lee and Mitani 2003][research_lee_mitani_2003]] [[Lee and Ombrello 2024][research_lee_ombrello_2024]] [[Lee et al 2000][research_lee_kim_2000]] [[Lee et al 2001][research_lee_shin_2001]] [[Lee et al 2013][research_lee_kang_2013]] [[Lee et al 2021][research_lee_lee_2021]] [[Lee et al 2022][research_lee_lee_2022]] [[Lee et al 2026][research_lee_kim_2026]] [[Lei et al 2023][research_lei_zhang_2023]] [[Leng et al 2024][research_leng_wang_2024]] [[Leonov 2022][research_leonov_2022]] [[Leonov et al 2011][research_leonov_kochetov_2011]] [[Leonov et al 2018][research_leonov_houpt_2018]] [[Li 2022][research_li_2022]] [[Li 2022][research_li_2022_b]] [[Li and Wang 2017][research_li_wang_2017]] [[Li et al 2004][research_li_zhou_2004]] [[Li et al 2007][research_li_ma_2007]] [[Li et al 2017][research_li_liu_2017]] [[Li et al 2017][research_li_zhang_2017]] [[Li et al 2017][research_li_shen_2017]] [[Li et al 2017][research_li_jin_2017]] [[Li et al 2018][research_li_jiao_2018]] [[Li et al 2018][research_li_chang_2018]] [[Li et al 2019][research_li_xia_2019]] [[Li et al 2019][research_li_wang_2019]] [[Li et al 2019][research_li_chang_2019]] [[Li et al 2020][research_li_sun_2020]] [[Li et al 2020][research_li_xie_2020]] [[Li et al 2021][research_li_tang_2021]] [[Li et al 2021][research_li_xie_2021]] [[Li et al 2022][research_li_tang_2022]] [[Li et al 2022][research_li_lei_2022]] [[Li et al 2023][research_li_wang_2023]] [[Li et al 2023][research_li_leng_2023]] [[Li et al 2023][research_li_liang_2023]] [[Li et al 2023][research_li_ding_2023]] [[Li et al 2024][research_li_sun_2024]] [[Li et al 2024][research_li_wang_2024_c]] [[Li et al 2025][research_li_wang_2025]] [[Li et al 2025][research_li_dou_2025]] [[Li et al 2025][research_li_liu_2025]] [[Li et al 2026][research_li_li_2026]] [[Li et al 2026][research_li_wang_2026]] [[Li et al 2026][research_li_dou_2026]] [[Li et al 2026][research_li_jiao_2026]] [[Li et al 2026][research_li_liu_2026]] [[Li et al 2026][research_li_yang_2026]] [[Li et al 2026][research_li_zhan_2026]] [[Liang et al 2013][research_liang_gong_2013]] [[Liang et al 2022][research_liang_huang_2022]] [[Liang et al 2024][research_liang_guo_2024]] [[Lim et al 2006][research_lim_wang_2006]] [[Lim et al 2025][research_lim_lee_2025]] [[Limage 1996][research_limage_1996]] [[Lin et al 1991][research_lin_rao_1991]] [[Lin et al 2006][research_lin_tam_2006]] [[Lin et al 2007][research_lin_tam_2007]] [[Lin et al 2026][research_lin_wu_2026]] [[Lin et al 2026][research_lin_geng_2026]] [[Lindsey and McMullan 2006][research_lindsey_mcmullan_2006]] [[Lino et al 2024][research_lino_oliveirajunior_2024]] [[Liu 2014][research_liu_2014]] [[Liu and Brown 2012][research_liu_brown_2012]] [[Liu and Fang 2024][research_liu_fang_2024]] [[Liu and Yao 2021][research_liu_yao_2021]] [[Liu and Yao 2021][research_liu_yao_2021_b]] [[Liu et al 2005][research_liu_wang_2005]] [[Liu et al 2007][research_liu_xiao_2007]] [[Liu et al 2016][research_liu_liang_2016]] [[Liu et al 2017][research_liu_wang_2017]] [[Liu et al 2019][research_liu_gao_2019]] [[Liu et al 2019][research_liu_baccarella_2019]] [[Liu et al 2022][research_liu_wu_2022]] [[Liu et al 2022][research_liu_he_2022]] [[Liu et al 2022][research_liu_qiao_2022]] [[Liu et al 2023][research_liu_xue_2023]] [[Liu et al 2023][research_liu_han_2023]] [[Liu et al 2023][research_liu_yang_2023]] [[Liu et al 2024][research_liu_pan_2024]] [[Liu et al 2024][research_liu_bian_2024]] [[Liu et al 2025][research_liu_li_2025]] [[Liu et al 2026][research_liu_chen_2026]] [[Liu et al 2026][research_liu_zhang_2026]] [[Liu et al 2026][research_liu_yang_2026]] [[Lloyd 1959][research_lloyd_1959]] [[Longwell and Weiss 1952][research_longwell_weiss_1952]] [[Lonkar and Panda 2025][research_lonkar_panda_2025]] [[Lonkar and Panda 2026][research_lonkar_panda_2026]] [[Louis M. Edelman][research_louismedelman]] [[Lu et al 2012][research_lu_li_2012]] [[Lu et al 2016][research_lu_wang_2016]] [[Lu et al 2025][research_lu_sheng_2025]] [[Lubarsky and Levy 1998][research_lubarsky_levy_1998]] [[Lucquin and Antonik 1972][research_lucquin_antonik_1972]] [[Luo et al 2003][research_luo_luo_2003]] [[Luo et al 2022][research_luo_feng_2022]] [[Luo et al 2025][research_luo_sun_2025]] [[Luo et al 2026][research_luo_tian_2026]] [[Lv et al 2026][research_lv_li_2026]] [[Ma et al 2021][research_ma_sun_2021]] [[Macheret et al 2001][research_macheret_shneider_2001]] [[Machrafi and Cavadiasa 2008][research_machrafi_cavadiasa_2008]] [[Mack et al 2009][research_mack_steelant_2009]] [[Madden and Solomon 1993][research_madden_solomon_1993]] [[Madhumitha and Karmakar 2024][research_madhumitha_karmakar_2024]] [[Mahato et al 2023][research_mahato_sarikonda_2023]] [[Makhija et al 2026][research_makhija_bodi_2026]] [[Malsur Dharavath et al 2023][research_malsurdharavath_pmanna_2023]] [[Mane et al 2026][research_mane_pandey_2026]] [[Manna et al 2023][research_manna_dharavath_2023]] [[Marley and Driscoll 2018][research_marley_driscoll_2018]] [[Marsh and Sears 1954][research_marsh_sears_1954]] [[Marshall et al 2005][research_marshall_corpening_2005]] [[Mashio et al 2001][research_mashio_kurashina_2001]] [[Massa and Pace 2025][research_massa_pace_2025]] [[Mathur 2026][research_mathur_2026]] [[Mathur 2026][research_mathur_2026_b]] [[Mathur et al 1999][research_mathur_streby_1999]] [[Mathur et al 2001][research_mathur_gruber_2001]] [[Maxwell and Goodwin 2017][research_maxwell_goodwin_2017]] [[Mayne 1976][research_mayne_1976]] [[Mayne 1979][research_mayne_1979]] [[Mcclinton 1976][research_mcclinton_1976]] [[McClinton et al 1996][research_mcclinton_roudakov_1996]] [[McDaniel 2005][research_mcdaniel_2005]] [[McDaniel, Jr. 1998][research_mcdanieljr_1998]] [[McDonald 2025][research_mcdonald_2025]] [[McDonald et al 2017][research_mcdonald_rice_2017]] [[McRae and Edwards 2001][research_mcrae_edwards_2001]] [[McTaggart 1973][research_mctaggart_1973]] [[Measurement Techniques for Supersonic 1974][research_measurement_techniques_1974]] [[Meng et al 2020][research_meng_ye_2020]] [[Meng et al 2022][research_meng_sun_2022]] [[Meng et al 2024][research_meng_sun_2024]] [[Menon 1989][research_menon_1989]] [[Menon 1990][research_menon_1990]] [[Menon 1991][research_menon_1991]] [[Menon 1992][research_menon_1992]] [[Menon 1992][research_menon_1992_b]] [[Menon and Jou 1990][research_menon_jou_1990]] [[Menon and Jou 1991][research_menon_jou_1991]] [[Menon et al 2003][research_menon_genin_2003]] [[Mermagen and Yalamanchili 1983][research_mermagen_yalamanchili_1983]] [[Meshcheryakov and Yashina 2015][research_meshcheryakov_yashina_2015]] [[Miao et al 2020][research_miao_wang_2020]] [[Micka and Driscoll 2008][research_micka_driscoll_2008]] [[Micka and Driscoll 2009][research_micka_driscoll_2009]] [[Milligan et al 2009][research_milligan_wolff_2009]] [[Min et al 2009][research_min_hailong_2009]] [[Minard and Falempin 2008][research_minard_falempin_2008]] [[Mirmirani et al 2009][research_mirmirani_kuipers_2009]] [[Mitani 1995][research_mitani_1995]] [[Mitani 1996][research_mitani_1996]] [[Mitani and Izumikawa 2000][research_mitani_izumikawa_2000]] [[Mitani and Kouchi 2005][research_mitani_kouchi_2005]] [[Mitani et al 2003][research_mitani_tomioka_2003]] [[Miyajima et al 1992][research_miyajima_chinzei_1992]] [[Miyashita et al 2025][research_miyashita_matsuo_2025]] [[Mohamadi and Tahsini 2023][research_mohamadi_tahsini_2023]] [[Mohieldin and Carson 2003][research_mohieldin_carson_2003]] [[Mohieldin et al 2001][research_mohieldin_tiwari_2001]] [[Mohieldin, T. O. et al 2004][research_mohieldinto_tiwarisn_2004]] [[Molvik et al 1992][research_molvik_bowles_1992]] [[Molvik et al 1993][research_molvik_bowles_1993]] [[Molvik et al 1993][research_molvik_bowles_1993_b]] [[Montes et al 2005][research_montes_king_2005]] [[Moon and Sung 2015][research_moon_sung_2015]] [[Morgan and Stalker 1985][research_morgan_stalker_1985]] [[Morgan and Zander 2009][research_morgan_zander_2009]] [[Morgan et al 2012][research_morgan_duraisamy_2012]] [[Morgan et al 2014][research_morgan_duraisamy_2014]] [[Moses et al 1999][research_moses_bouchard_1999]] [[Moura and Borges Ribeiro 2025][research_moura_borgesribeiro_2025]] [[Moura et al 2019][research_moura_wheatley_2019]] [[Muhammad Haseeb 2025][research_muhammadhaseeb_2025]] [[Mura and Sabelnikov 2021][research_mura_sabelnikov_2021]] [[Murty and Chakraborty 2011][research_murty_chakraborty_2011]] [[Murugesan et al 2018][research_murugesan_chakravarthy_2018]] [[Musa et al 2018][research_musa_weixuan_2018]] [[Musa et al 2024][research_musa_huang_2024]] [[Musa et al 2025][research_musa_huang_2025]] [[Muss et al 2003][research_muss_johnson_2003]] [[Nagamatsu 1989][research_nagamatsu_1989]] [[Nagarajan Kirupakaran et al 2023][research_nagarajankirupakaran_kv_2023]] [[Nagendra Babu et al 2018][research_nagendrababu_jayakrishna_2018]] [[Nair et al 2020][research_nair_s_2020]] [[Nair et al 2022][research_nair_suryan_2022]] [[Nair et al 2023][research_nair_suryan_2023]] [[Nakagawa and Kuwahara 1992][research_nakagawa_kuwahara_1992]] [[Nakaya et al 2015][research_nakaya_hikichi_2015]] [[Nakayama et al 2018][research_nakayama_edanaga_2018]] [[Natan 1987][research_natan_1987]] [[Natan and Gany 1989][research_natan_gany_1989]] [[Nayal et al 2020][research_nayal_lamb_2020]] [[Ngo][research_ngo]] [[Ngoc Long 2016][research_ngoclong_2016]] [[Nguyen et al 2011][research_nguyen_reinartz_2011]] [[Nguyen et al 2024][research_nguyen_vo_2024]] [[Nie et al 2019][research_nie_li_2019]] [[Nikaido and Hobson 2025][research_nikaido_hobson_2025]] [[Ning 1981][research_ning_1981]] [[Nishiguchi et al 2025][research_nishiguchi_kodera_2025]] [[Niu and Chen 2024][research_niu_chen_2024]] [[Niu and Chen 2025][research_niu_chen_2025]] [[Niu and Piao 2016][research_niu_piao_2016]] [[niu and wang 2023][research_niu_wang_2023]] [[Nordin-Bates and Fureby 2015][research_nordinbates_fureby_2015]] [[Nordin-Bates et al 2017][research_nordinbates_fureby_2017]] [[Norimatsu et al 2026][research_norimatsu_katsumura_2026]] [[Norimatsu et al 2026][research_norimatsu_katsumura_2026_b]] [[Northam and Anderson 1986][research_northam_anderson_1986]] [[Northam et al 1988][research_northam_lempert_1988]] [[Numerical Simulation on Hypersonic 2015][research_numerical_simulation_2015]] [[Nusca 1989][research_nusca_1989]] [[O'Byrne et al 2005][research_obyrne_stotz_2005]] [[O'Byrne et al 2011][research_obyrne_wittig_2011]] [[O'Neill and Lewis 1992][research_oneill_lewis_1992]] [[O'Neill and Lewis 1993][research_oneill_lewis_1993]] [[Oamjee and Sadanandan 2020][research_oamjee_sadanandan_2020]] [[Oamjee and Sadanandan 2020][research_oamjee_sadanandan_2020_b]] [[Ogawa and Boyce 2013][research_ogawa_boyce_2013]] [[Ogawa et al 2009][research_ogawa_grainger_2009]] [[Ogawa et al 2010][research_ogawa_grainger_2010]] [[Olivon et al 2024][research_olivon_durand_2024]] [[Olivon et al 2026][research_olivon_genot_2026]] [[Ombrello et al 2015][research_ombrello_carter_2015]] [[Optimization of parameters of 2005][research_optimization_of_2005]] [[Osgerby et al 1969][research_osgerby_smithson_1969]] [[Osgerby et al 1969][research_osgerby_smithson_1969_b]] [[Ou et al 2024][research_ou_xiong_2024]] [[Ou-zi and Jin-sheng 2011][research_ouzi_jinsheng_2011]] [[Oveissi et al 2024][research_oveissi_goel_2024]] [[Pace and Massa 2022][research_pace_massa_2022]] [[Pagan et al 2001][research_pagan_benoit_2001]] [[Pagel and Warmbold 1968][research_pagel_warmbold_1968]] [[Pagel and Warmbold 1969][research_pagel_warmbold_1969]] [[Pandey and Sivasakthivel 2011][research_pandey_sivasakthivel_2011]] [[Pandey and Sivasakthivel 2011][research_pandey_sivasakthivel_2011_b]] [[Papinczak][research_papinczak]] [[Park and Busch 2017][research_park_busch_2017]] [[Parmar et al 2026][research_parmar_jp_2026]] [[Parsons and Richmond 1969][research_parsons_richmond_1969]] [[Pasha et al 2012][research_pasha_vadivelan_2012]] [[Paull 1999][research_paull_1999]] [[Paull et al 1995][research_paull_stalker_1995]] [[Pei and Hou 2014][research_pei_hou_2014]] [[Pein and Vinnemeier 1989][research_pein_vinnemeier_1989]] [[Pellett et al 2002][research_pellett_bruno_2002]] [[Peng et al 2026][research_peng_chen_2026]] [[Perchonok 1960][research_perchonok_1960]] [[Performance analysis of hydrocarbon-fueled 1999][research_performance_analysis_1999]] [[Peri et al 2024][research_peri_armani_2024]] [[Peterson and Hassan 2017][research_peterson_hassan_2017]] [[Peterson and Hassan 2018][research_peterson_hassan_2018]] [[Petha Sethuraman et al 2020][research_pethasethuraman_kim_2020]] [[Petha Sethuraman et al 2023][research_pethasethuraman_yang_2023]] [[Pettinari et al 2012][research_pettinari_corradini_2012]] [[Pezzella et al 2014][research_pezzella_marini_2014]] [[Pichler 2023][research_pichler_2023]] [[Pinheiro Maia et al 2020][research_pinheiromaia_souza_2020]] [[Piscopo et al 2024][research_piscopo_depaepe_2024]] [[Pitman][research_pitman]] [[Potapkin and Moskvichev 2008][research_potapkin_moskvichev_2008]] [[Potturi and Edwards 2013][research_potturi_edwards_2013]] [[Powers et al 1986][research_powers_zaretzky_1986]] [[Prakash et al 2024][research_prakash_g_2024]] [[Pratt and Heiser 1993][research_pratt_heiser_1993]] [[Prokesch et al 2024][research_prokesch_duran_2024]] [[Pu et al 2017][research_pu_huang_2017]] [[Pulsonetti][research_pulsonetti]] [[Qi et al 2015][research_qi_bao_2015]] [[Qin et al 2012][research_qin_bao_2012]] [[Qin et al 2015][research_qin_chang_2015]] [[Qin et al 2019][research_qin_agarwal_2019]] [[Qiu et al 2021][research_qiu_zhang_2021]] [[Quan et al 2024][research_quan_chang_2024]] [[Quinlan][research_quinlan]] [[Quinlan, Jesse R. et al 2014][research_quinlanjesser_mcdanieljamesc_2014]] [[Rabadan and Weigand 2013][research_rabadan_weigand_2013]] [[Rabadan Santana and Weigand 2012][research_rabadansantana_weigand_2012]] [[Rajamanohar and Kurian 1996][research_rajamanohar_kurian_1996]] [[Ram and Kim 2019][research_ram_kim_2019]] [[Ramakrishnan and Singh 1993][research_ramakrishnan_singh_1993]] [[Ramanujachari 2022][research_ramanujachari_2022]] [[Ramaty et al 1982][research_ramaty_spiegler_1982]] [[Ramjet supersonic "flight tests" 1958][research_ramjet_supersonic_1958]] [[Rana et al 2011][research_rana_thornber_2011]] [[Rana et al 2013][research_rana_thornber_2013]] [[Rasmussen et al 2007][research_rasmussen_dhanuka_2007]] [[Ravindran et al 2019][research_ravindran_bricalli_2019]] [[Razzaqi and Smart 2009][research_razzaqi_smart_2009]] [[Reddecliff and Weber 1998][research_reddecliff_weber_1998]] [[Relangi et al 2021][research_relangi_ingenito_2021]] [[Relangi et al 2023][research_relangi_ingenito_2023]] [[Reynolds 1977][research_reynolds_1977]] [[Rice][research_rice]] [[Rice et al 2014][research_rice_goyne_2014]] [[Rich and Mellor 1995][research_rich_mellor_1995]] [[Rigamonti et al 2026][research_rigamonti_shoesmith_2026]] [[Rigamonti et al 2026][research_rigamonti_vicocantero_2026]] [[Riggins et al 1992][research_riggins_mcclinton_1992]] [[Riggins et al 2006][research_riggins_tackett_2006]] [[Riis et al 2024][research_riis_piscopo_2024]] [[Riley et al 2015][research_riley_gaitonde_2015]] [[Riley et al 2016][research_riley_hagenmaier_2016]] [[Riley et al 2017][research_riley_hagenmaier_2017]] [[Risha 2000][research_risha_2000]] [[Rocci Denis et al 2003][research_roccidenis_brandstetter_2003]] [[Rockwell et al 2010][research_rockwell_goyne_2010]] [[Rockwell et al 2023][research_rockwell_goyne_2023]] [[Rodi 2012][research_rodi_2012]] [[Rodriguez, C. G. et al 2000][research_rodriguezcg_rigginsdw_2000]] [[Rodríguez Fuentes and Parent 2022][research_rodriguezfuentes_parent_2022]] [[Roga 2019][research_roga_2019]] [[Roga 2019][research_roga_2019_b]] [[Roga 2023][research_roga_2023]] [[Rogers, R. Clayton et al 1998][research_rogersrclayton_capriottidiegop_1998]] [[Rogg et al 2020][research_rogg_bricalli_2020]] [[Roos et al 2020][research_roos_pudsey_2020]] [[Rotating detonation combustion of 2023][research_rotating_detonation_2023]] [[Roudakov et al 1996][research_roudakov_semenov_1996]] [[Roudakov et al 1998][research_roudakov_semenov_1998]] [[Roundy 1979][research_roundy_1979]] [[Rowan][research_rowan]] [[Rowan and Paull 2005][research_rowan_paull_2005]] [[Rowan and Paull 2006][research_rowan_paull_2006]] [[Ruan][research_ruan]] [[Ruan et al 2020][research_ruan_domingo_2020]] [[Sabelnikov and Vlasenko 2017][research_sabelnikov_vlasenko_2017]] [[Sacher and Zellner 1995][research_sacher_zellner_1995]] [[Sachs et al 1991][research_sachs_bayer_1991]] [[Sachs et al 1996][research_sachs_heller_1996]] [[Sahut et al 2024][research_sahut_nilsson_2024]] [[Saito et al 2004][research_saito_ono_2004]] [[Saito et al 2005][research_saito_ono_2005]] [[Salloum et al 2018][research_salloum_candon_2018]] [[Salloum et al 2018][research_salloum_candon_2018_b]] [[San Martin et al 2025][research_sanmartin_plewacki_2025]] [[San Martin et al 2025][research_sanmartin_plewacki_2025_b]] [[Sanaka et al 2023][research_sanaka_kandula_2023]] [[Sandeep 2023][research_sandeep_2023]] [[Santos and Borges Ribeiro 2025][research_santos_borgesribeiro_2025]] [[Sargent and Bielawski 1970][research_sargent_bielawski_1970]] [[Sarosh 2021][research_sarosh_2021]] [[Sarout and Paramasivam 2020][research_sarout_paramasivam_2020]] [[Sarout et al 2020][research_sarout_r_2020]] [[Sathiyamoorthy et al 2018][research_sathiyamoorthy_danish_2018]] [[Sato et al 1997][research_sato_izumikawa_1997]] [[Sato et al 2019][research_sato_fukui_2019]] [[Savelkin et al 2015][research_savelkin_yarantsev_2015]] [[Savino and Pezzella 2003][research_savino_pezzella_2003]] [[Schetz et al 1980][research_schetz_billig_1980]] [[Schetz et al 1982][research_schetz_billig_1982]] [[Schindel 1989][research_schindel_1989]] [[Schindel 1999][research_schindel_1999]] [[Schneider and Reed 2003][research_schneider_reed_2003]] [[Schneider et al][research_schneider_gerlinger]] [[Schneider et al 2003][research_schneider_matsumura_2003]] [[Scotti et al 1988][research_scotti_martin_1988]] [[Scramjet Combustion 2022][research_scramjet_combustion_2022]] [[Scramjet Combustor 2022][research_scramjet_combustor_2022]] [[Scramjet Engine Research athe 2001][research_scramjet_engine_2001]] [[Scramjet Inlet/Forebody and Isolator 2022][research_scramjet_inlet_forebody_2022]] [[Seckin and Yuceil 2013][research_seckin_yuceil_2013]] [[Segal 2009][research_segal_2009]] [[Segal 2010][research_segal_2010]] [[Sekar and Vaidyanathan 2025][research_sekar_vaidyanathan_2025]] [[Semenov et al 1998][research_semenov_romankov_1998]] [[Serre and Falempin 2001][research_serre_falempin_2001]] [[Seshadri 2008][research_seshadri_2008]] [[Shajahan et al 2025][research_shajahan_gugulothu_2025]] [[Shang 2008][research_shang_2008]] [[Shaohua and Xu 2017][research_shaohua_xu_2017]] [[Sharma et al 2022][research_sharma_eswaran_2022]] [[Shen et al 2020][research_shen_huang_2020]] [[Shen et al 2021][research_shen_huang_2021]] [[Shepard et al 2021][research_shepard_feleo_2021]] [[Shetty et al 2025][research_shetty_cardenas_2025]] [[Shi 2016][research_shi_2016]] [[Shi et al 2017][research_shi_song_2017]] [[Shi et al 2017][research_shi_song_2017_b]] [[Shikman et al 2001][research_shikman_vinogradov_2001]] [[Shneider and Macheret 2004][research_shneider_macheret_2004]] [[Shock tunnel and numerical 2012][research_shock_tunnel_2012]] [[Shubhankar Bhakta et al., 2018][research_shubhankarbhaktaetal_2018]] [[Sicard et al 2006][research_sicard_raepsaet_2006]] [[Siebenhaar and Bogar 2006][research_siebenhaar_bogar_2006]] [[Siebenhaar et al 1999][research_siebenhaar_chen_1999]] [[Simone and Bruno 2009][research_simone_bruno_2009]] [[Simone and Bruno 2010][research_simone_bruno_2010]] [[Simsont et al 2012][research_simsont_gerlinger_2012]] [[Singh and Rajagopal 2026][research_singh_rajagopal_2026]] [[Singh et al 1990][research_singh_tiwari_1990]] [[Singh et al 2018][research_singh_babu_2018]] [[Singh et al 2023][research_singh_g_2023]] [[Singh et al 2025][research_singh_sharma_2025]] [[Siqueira et al 2019][research_siqueira_rosa_2019]] [[Sislian et al 2000][research_sislian_dudebout_2000]] [[Sitaraman et al 2021][research_sitaraman_yellapantula_2021]] [[Situ et al 1999][research_situ_sun_1999]] [[Situ et al 2001][research_situ_wang_2001]] [[Situ et al 2002][research_situ_wang_2002]] [[Slutsky et al 1969][research_slutsky_williams_1969]] [[Smart et al 2006][research_smart_hass_2006]] [[Smayda][research_smayda]] [[Smayda and Goyne 2011][research_smayda_goyne_2011]] [[Smeets and Quenett 1997][research_smeets_quenett_1997]] [[Smith and Farokhi 2015][research_smith_farokhi_2015]] [[Smith and Farokhi 2015][research_smith_farokhi_2015_b]] [[Smith and Farokhi 2015][research_smith_farokhi_2015_c]] [[Smith and Farokhi 2018][research_smith_farokhi_2018]] [[Smith and Good 1979][research_smith_good_1979]] [[Son et al 2024][research_son_ko_2024]] [[Son et al 2024][research_son_ko_2024_b]] [[Song et al 2006][research_song_choi_2006]] [[Song et al 2019][research_song_wang_2019]] [[Song et al 2026][research_song_cai_2026]] [[Song et al 2026][research_song_zhang_2026]] [[Soni and De 2017][research_soni_de_2017]] [[Sridharan and Rodriguez 2013][research_sridharan_rodriguez_2013]] [[Srikant et al 2010][research_srikant_wagner_2010]] [[Stalker et al 1988][research_stalker_morgan_1988]] [[Stalker et al 1994][research_stalker_simmons_1994]] [[Starikovskiy et al 2024][research_starikovskiy_ju_2024]] [[Starkey 2009][research_starkey_2009]] [[Starkey 2014][research_starkey_2014]] [[Starkey and Lewis 1999][research_starkey_lewis_1999_b]] [[Stefaniya et al 2025][research_stefaniya_pushpalatha_2025]] [[Steva][research_steva]] [[Stewart and Quigg 1963][research_stewart_quigg_1963]] [[Stokes and Acharya 2023][research_stokes_acharya_2023]] [[Stokes et al 2023][research_stokes_acharya_2023_b]] [[Stoukov et al 1997][research_stoukov_gorokhovski_1997]] [[Strauss et al 2025][research_strauss_manassis_2025]] [[Strauss et al 2026][research_strauss_fischer_2026]] [[Streiff 1953][research_streiff_1953]] [[Su et al 2018][research_su_chen_2018]] [[Subbiah and Stefaniya 2025][research_subbiah_stefaniya_2025]] [[Subramanian et al 2025][research_subramanian_thangadurai_2025]] [[Suetin and Kartsev 1993][research_suetin_kartsev_1993]] [[Sullins 1993][research_sullins_1993]] [[Sullins et al 1991][research_sullins_carpenter_1991]] [[Sullivan and Gaitonde 2022][research_sullivan_gaitonde_2022]] [[Summors][research_summors]] [[Sun 2008][research_sun_2008]] [[Sun et al 2008][research_sun_geng_2008]] [[Sun et al 2016][research_sun_zhong_2016]] [[Sun et al 2020][research_sun_wang_2020]] [[Sun et al 2020][research_sun_wang_2020_b]] [[Sun et al 2021][research_sun_li_2021]] [[Suneetha et al 2019][research_suneetha_randive_2019]] [[Sung et al 2001][research_sung_hsieh_2001]] [[Sung et al 2001][research_sung_hsieh_2001_b]] [[Sung et al 2026][research_sung_jo_2026]] [[Supersonic Combustion Flowfield Studies 1977][research_supersonic_combustion_1977]] [[Supersonic Combustion Processes 2009][research_supersonic_combustion_2009]] [[Surzhikov et al 2013][research_surzhikov_shang_2013]] [[Sushma et al 2025][research_sushma_rani_2025]] [[Swain et al 2020][research_swain_p_2020]] [[Swithebank and Chigier 1969][research_swithebank_chigier_1969]] [[Swithenbank and Jaques 1970][research_swithenbank_jaques_1970]] [[Swithenbank et al 1992][research_swithenbank_ewan_1992]] [[Sykes][research_sykes]] [[T Sailor Koeplinger et al][research_tsailorkoeplinger_calebhash]] [[Taha et al 2001][research_taha_tiwari_2001]] [[Takahashi et al 1998][research_takahashi_wakai_1998]] [[Takahashi et al 2005][research_takahashi_sunami_2005]] [[Takahashi et al 2007][research_takahashi_komuro_2007]] [[Takegoshi et al 2012][research_takegoshi_tomioka_2012]] [[Talantov 1959][research_talantov_1959]] [[Tam et al 2005][research_tam_eklund_2005]] [[Tam et al 2006][research_tam_lin_2006]] [[Tam et al 2007][research_tam_hsu_2007]] [[Tam et al 2008][research_tam_hsu_2008]] [[Tam et al 2008][research_tam_eklund_2008]] [[Tam et al 2011][research_tam_hsu_2011]] [[Tam et al 2012][research_tam_hsu_2012]] [[Tan and Wang 2015][research_tan_wang_2015]] [[Tani et al 2000][research_tani_kanda_2000]] [[Tanno and Tanno 2021][research_tanno_tanno_2021]] [[Tao 1995][research_tao_1995]] [[Tao et al 2008][research_tao_daren_2008]] [[Tarnavskii 2005][research_tarnavskii_2005]] [[Tatman][research_tatman]] [[Teng et al 2017][research_teng_zhou_2017]] [[Tetlow and Doolan][research_tetlow_doolan]] [[The Theoretical Study of 2012][research_the_theoretical_2012]] [[Thomas and Guy 1982][research_thomas_guy_1982]] [[Thomas et al 1987][research_thomas_voland_1987]] [[Tian et al 2016][research_tian_yang_2016]] [[Tian et al 2026][research_tian_zhang_2026]] [[Tian et al 2026][research_tian_wan_2026]] [[Tietz et al 2006][research_tietz_chun_2006]] [[Timnat 1987][research_timnat_1987]] [[Tirtey and Boyce 2009][research_tirtey_boyce_2009]] [[Tishkoff et al 1997][research_tishkoff_drummond_1997]] [[Tiwari et al 2001][research_tiwari_abdelsalam_2001]] [[Tiwari et al 2002][research_tiwari_taha_2002]] [[Tomczak 2026][research_tomczak_2026]] [[Tomioka et al 1998][research_tomioka_kanda_1998]] [[Tomioka et al 2007][research_tomioka_hiraiwa_2007]] [[Tomioka et al 2007][research_tomioka_ueda_2007]] [[Tomioka et al 2016][research_tomioka_takahashi_2016]] [[Tomioka et al 2018][research_tomioka_takahashi_2018]] [[Torrez et al 2010][research_torrez_dalle_2010]] [[Torrez et al 2011][research_torrez_dalle_2011]] [[Trefny and Dippold 2010][research_trefny_dippold_2010]] [[Tretyakov et al 2021][research_tretyakov_tupikin_2021]] [[Trexler 1988][research_trexler_1988]] [[Tsujikawa 1996][research_tsujikawa_1996]] [[Tunik 2020][research_tunik_2020]] [[Tunik and Mayorov 2022][research_tunik_mayorov_2022]] [[Tunik and Mayorov 2022][research_tunik_mayorov_2022_b]] [[Tunik et al 2022][research_tunik_gerasimov_2022]] [[Two-dimensional scramjet inlet unstart model, wind-tunnel blockage and actuation systems][research_inlet_unstart_model]] [[Tyll et al 2000][research_tyll_bakos_2000]] [[Ueda et al 2006][research_ueda_takegoshi_2006]] [[Ueda et al 2009][research_ueda_kouchi_2009]] [[Ullman and Raman 2023][research_ullman_raman_2023]] [[Unterberg 1957][research_unterberg_1957]] [[Valdivia et al 2014][research_valdivia_yuceil_2014]] [[Van den Borre et al 2023][research_vandenborre_saracoglu_2023]] [[Van Der Geld et al 1990][research_vandergeld_korting_1990]] [[Van der lee et al 2021][research_vanderlee_yokev_2021]] [[van der Lee et al 2023][research_vanderlee_michaels_2023]] [[van der Lee et al 2026][research_vanderlee_seniortybora_2026]] [[van der Lee et al 2026][research_vanderlee_kaner_2026]] [[Van Wie 1992][research_vanwie_1992]] [[Vanamamalai and Panneerselvam 2024][research_vanamamalai_panneerselvam_2024]] [[Vander Schaaf et al 2025][research_vanderschaaf_acharya_2025]] [[Vanstone et al 2017][research_vanstone_hashemi_2017]] [[Vanstone et al 2018][research_vanstone_lingren_2018]] [[Vanstone et al 2018][research_vanstone_hashemi_2018]] [[Vanyai et al 2018][research_vanyai_grieve_2018]] [[Vanyai et al 2019][research_vanyai_grieve_2019]] [[Vanyai et al 2020][research_vanyai_grieve_2020]] [[Vanyai et al 2021][research_vanyai_brieschenk_2021]] [[Varshney and Baig 2019][research_varshney_baig_2019]] [[Varshney et al 2020][research_varshney_varshney_2020]] [[Varshney et al 2020][research_varshney_varshney_2020_b]] [[Venkatapathy, E. et al 1995][research_venkatapathye_tokarcikpolskys_1995]] [[Venkateshwaran and Padmanathan 2026][research_venkateshwaran_padmanathan_2026]] [[Venkateswarlu et al 2025][research_venkateswarlu_kolhe_2025]] [[Verma 2010][research_verma_2010]] [[Verma and Shukla 2021][research_verma_shukla_2021]] [[Verma et al 2019][research_verma_shukla_2019]] [[Verma et al 2021][research_verma_kapayeva_2021]] [[Verma et al 2021][research_verma_pandey_2021]] [[Verma et al 2022][research_verma_pandey_2022]] [[Verma et al 2022][research_verma_sharma_2022]] [[Vijayakumar 2020][research_vijayakumar_2020]] [[Vijayakumar et al 2014][research_vijayakumar_wilson_2014]] [[Vincent-Randonnier et al 2008][research_vincentrandonnier_rouxel_2008]] [[Vinogradov et al 1990][research_vinogradov_grachev_1990]] [[Voland 1990][research_voland_1990]] [[Voland et al 1999][research_voland_auslender_1999]] [[Wagner et al 2008][research_wagner_yuceil_2008]] [[Wagner et al 2009][research_wagner_yuceil_2009]] [[Wagner et al 2010][research_wagner_yuceil_2010]] [[Waidmann et al 2024][research_waidmann_brummund_2024]] [[Walker 1949][research_walker_1949]] [[Walker 1952][research_walker_1952]] [[Walker et al 2006][research_walker_kennedy_2006]] [[Waltrup and Billig 1972][research_waltrup_billig_1972]] [[Waltrup et al 1980][research_waltrup_billig_1980]] [[Waltrup et al 1981][research_waltrup_billig_1981]] [[Waltrup et al 1996][research_waltrup_white_1996]] [[Wang and Le 2000][research_wang_le_2000]] [[Wang et al 2005][research_wang_zhang_2005]] [[Wang et al 2013][research_wang_wang_2013]] [[Wang et al 2013][research_wang_wang_2013_b]] [[Wang et al 2013][research_wang_wang_2013_c]] [[Wang et al 2013][research_wang_wang_2013_d]] [[Wang et al 2013][research_wang_wang_2013_e]] [[Wang et al 2016][research_wang_xiao_2016]] [[Wang et al 2017][research_wang_song_2017]] [[Wang et al 2018][research_wang_pan_2018]] [[Wang et al 2021][research_wang_he_2021]] [[Wang et al 2021][research_wang_chang_2021]] [[Wang et al 2022][research_wang_xin_2022]] [[Wang et al 2023][research_wang_xu_2023]] [[Wang et al 2023][research_wang_wang_2023]] [[Wang et al 2023][research_wang_huang_2023]] [[Wang et al 2023][research_wang_xin_2023]] [[Wang et al 2024][research_wang_wang_2024]] [[Wang et al 2024][research_wang_yao_2024]] [[Wang et al 2024][research_wang_yao_2024_b]] [[Wang et al 2024][research_wang_wang_2024_b]] [[Wang et al 2024][research_wang_wang_2024_c]] [[Wang et al 2025][research_wang_an_2025]] [[Wang et al 2025][research_wang_yao_2025]] [[Wang et al 2025][research_wang_liu_2025]] [[Wang et al 2025][research_wang_he_2025]] [[Wang et al 2025][research_wang_chen_2025]] [[Wang et al 2025][research_wang_tang_2025]] [[Wang et al 2025][research_wang_feng_2025]] [[Wang et al 2026][research_wang_liu_2026]] [[Wang et al 2026][research_wang_liu_2026_b]] [[Weeratunga and Menon 1993][research_weeratunga_menon_1993]] [[Wei et al 2024][research_wei_zhang_2024]] [[Weidner et al 1976][research_weidner_small_1976]] [[Weissman 1990][research_weissman_1990]] [[Wendel and Gaitonde 2026][research_wendel_gaitonde_2026]] [[Wendel et al 2025][research_wendel_gaitonde_2025]] [[Wendt][research_wendt]] [[Whitehurst et al 1992][research_whitehurst_krauss_1992]] [[Whitney 1963][research_whitney_1963]] [[Whitside][research_whitside]] [[Wieting 1990][research_wieting_1990]] [[Wieting and Guy 1976][research_wieting_guy_1976]] [[Willard et al 2009][research_willard_giel_2009]] [[Wise][research_wise]] [[Wolf et al 1951][research_wolf_mullen_1951]] [[Wu and Wei 2022][research_wu_wei_2022]] [[Wu and Wei 2023][research_wu_wei_2023]] [[Wu et al 2013][research_wu_ding_2013]] [[Wu et al 2021][research_wu_song_2021]] [[Wu et al 2023][research_wu_fan_2023]] [[Wu et al 2026][research_wu_wu_2026]] [[Wu et al 2026][research_wu_fan_2026]] [[Xi et al 2026][research_xi_yao_2026]] [[Xia et al 2025][research_xia_sun_2025]] [[Xia et al 2026][research_xia_han_2026]] [[Xianyu et al 2007][research_xianyu_xiaoshan_2007]] [[Xianyu et al 2007][research_xianyu_xiaoshan_2007_b]] [[Xiao et al 2026][research_xiao_jin_2026]] [[Xie et al 2016][research_xie_ge_2016]] [[Xing et al 2017][research_xing_ruan_2017]] [[Xiong et al 2017][research_xiong_wang_2017]] [[Xiong et al 2021][research_xiong_zheng_2021]] [[Xiong et al 2022][research_xiong_qin_2022]] [[Xu et al 2018][research_xu_chang_2018]] [[Xu et al 2021][research_xu_lin_2021]] [[Xu et al 2023][research_xu_cheng_2023]] [[Xue et al 2017][research_xue_wei_2017]] [[Yan et al 2014][research_yan_yuzhen_2014]] [[Yan et al 2014][research_yan_bing_2014]] [[Yan et al 2014][research_yan_yuzhen_2014_b]] [[Yan et al 2016][research_yan_shaohua_2016]] [[Yan et al 2022][research_yan_liu_2022]] [[Yan et al 2022][research_yan_fan_2022]] [[Yan et al 2024][research_yan_sun_2024]] [[Yan et al 2025][research_yan_zhu_2025]] [[Yan et al 2025][research_yan_tian_2025]] [[yang and culick 1986][research_yang_culick_1986]] [[Yang and Yuh-Yih Wu 1994][research_yang_yuhyihwu_1994]] [[Yang et al 2014][research_yang_chang_2014]] [[Yang et al 2014][research_yang_lee_2014]] [[Yang et al 2014][research_yang_chang_2014_b]] [[Yang et al 2016][research_yang_lee_2016]] [[Yang et al 2017][research_yang_bao_2017]] [[Yang et al 2017][research_yang_wang_2017]] [[Yang et al 2020][research_yang_lee_2020]] [[Yarantsev et al 2019][research_yarantsev_firsov_2019]] [[Yatsuyanagi 2009][research_yatsuyanagi_2009]] [[Yentsch and Gaitonde 2013][research_yentsch_gaitonde_2013]] [[Yentsch and Gaitonde 2014][research_yentsch_gaitonde_2014]] [[Yip et al 1990][research_yip_strawa_1990]] [[Yonggang et al 2019][research_yonggang_yang_2019]] [[You et al 2013][research_you_luedeke_2013]] [[Young et al 2006][research_young_balar_2006]] [[Yu et al 1999][research_yu_wilson_1999]] [[Yu et al 2002][research_yu_li_2002]] [[Yu et al 2005][research_yu_kim_2005]] [[Yu et al 2015][research_yu_huang_2015]] [[Yu et al 2022][research_yu_liu_2022]] [[Yu et al 2022][research_yu_zhou_2022]] [[Yuan et al 2026][research_yuan_liu_2026]] [[Yue et al 2017][research_yue_lu_2017]] [[Yun et al 2022][research_yun_cole_2022]] [[Yun et al 2022][research_yun_cole_2022_b]] [[Yun et al 2026][research_yun_kim_2026]] [[Yungster et al 2014][research_yungster_paxson_2014]] [[Zander][research_zander]] [[Zelinski et al 1960][research_zelinski_matthews_1960]] [[Zeng et al 2026][research_zeng_luo_2026]] [[Zettervall and Fureby 2018][research_zettervall_fureby_2018]] [[Zhang et al 2015][research_zhang_yang_2015]] [[Zhang et al 2016][research_zhang_feng_2016]] [[Zhang et al 2016][research_zhang_feng_2016_b]] [[Zhang et al 2017][research_zhang_chang_2017]] [[Zhang et al 2019][research_zhang_yue_2019]] [[Zhang et al 2021][research_zhang_jin_2021]] [[Zhang et al 2023][research_zhang_zhao_2023]] [[Zhang et al 2025][research_zhang_jingfeng_2025]] [[Zhang et al 2025][research_zhang_xie_2025]] [[Zhang et al 2026][research_zhang_chen_2026]] [[Zhao 2023][research_zhao_2023]] [[Zhao et al 2018][research_zhao_xia_2018]] [[Zhao et al 2023][research_zhao_tian_2023]] [[Zhao et al 2026][research_zhao_sha_2026]] [[Zheng and Bray 1994][research_zheng_bray_1994]] [[Zhou et al 2017][research_zhou_teng_2017]] [[Zhou et al 2023][research_zhou_li_2023]] [[Zhou et al 2025][research_zhou_tian_2025]] [[Zhou et al 2026][research_zhou_zhang_2026]] [[Zhu and Xu 2017][research_zhu_xu_2017]] [[Zhu et al 2025][research_zhu_pethasethuraman_2025]] [[Zinnecker et al 2012][research_zinnecker_serrani_2012]] [[Zou et al 2026][research_zou_pan_2026]] [[Zou et al 2026][research_zou_pan_2026_b]] [[Zucro 1950][research_zucro_1950]]

### Compressible aerodynamics generally

**The general literature of flow that knows it is being compressed.** Shocks, expansions, Mach number effects, boundary layers and the ordinary business of supersonic and hypersonic aerodynamics. **Every article in this series about a fast aeroplane draws on this cluster**, and at Mach 5 it is not background but the subject of the airframe.

**1,250 records.** [[A Hypersonic Test Capabilities 2002][research_a_hypersonic_2002]] [[Abarbanel 1977][research_abarbanel_1977]] [[Abolhassani et al 1987][research_abolhassani_tiwari_1987]] [[Abuaf 1976][research_abuaf_1976]] [[Adams et al 1973][research_adams_johnc_1973]] [[Aditya et al 2016][research_aditya_balas_2016]] [[Advanced Fuel Research Inc East Hartford Ct 1957][research_advancedfuelresearchinceasthartfordct_1957]] [[Advisory Group for Aerospace Research and Development 1997][research_advisorygroupforaerospaceresearchanddevelopment_1997]] [[Aftosmis and Baron 1989][research_aftosmis_baron_1989]] [[Aiello 1962][research_aiello_1962]] [[Aiello 1963][research_aiello_1963]] [[Air Force Test Pilot School Edwards Afb Ca 1987][research_airforcetestpilotschooledwardsafbca_1987]] [[Airbreathing Hypersonic Aircraft and 1997][research_airbreathing_hypersonic_1997]] [[Alam et al 2006][research_alam_matsuo_2006]] [[Alberico 1992][research_alberico_1992]] [[Alferov and Marchenko 2012][research_alferov_marchenko_2012]] [[Alferov et al 2007][research_alferov_bushmin_2007]] [[Alkamhawi, Hani et al 1990][research_alkamhawihani_greinertom_1990]] [[Almeida 2021][research_almeida_2021]] [[Alsalihi and Deconinck 1991][research_alsalihi_deconinck_1991]] [[Alvi 2005][research_alvi_2005]] [[An Assessment of Our 1964][research_an_assessment_1964]] [[An et al 2017][research_an_wang_2017]] [[Anderson 1958][research_anderson_1958]] [[Anderson 1959][research_anderson_1959]] [[Anderson 1960][research_anderson_1960]] [[Anderson 1990][research_anderson_1990]] [[Anderson 1996][research_anderson_1996]] [[Anderson 2019][research_anderson_2019]] [[Anderson Jr. 2006][research_andersonjr_2006]] [[Anhtuan D. Ngo][research_anhtuandngo]] [[Appleby and Adams 1991][research_appleby_adams_1991]] [[Arai et al 2008][research_arai_taguchi_2008]] [[Araújo et al 2024][research_araujo_tanaka_2024]] [[Armstrong 1979][research_armstrong_1979]] [[Army War Coll Carlisle Barracks Pa 1952][research_armywarcollcarlislebarrackspa_1952]] [[Asma and Van der Haegen 2010][research_asma_vanderhaegen_2010]] [[Asma et al 2009][research_asma_tirtey_2009]] [[Atkins 2026][research_atkins_2026]] [[August and Joshi 1997][research_august_joshi_1997]] [[Auslender et al 2009][research_auslender_suder_2009]] [[Avcilar and Celik 2026][research_avcilar_celik_2026]] [[Avidor and Lederman 1971][research_avidor_lederman_1971]] [[Azevedo and Korzenowski 1998][research_azevedo_korzenowski_1998]] [[Baer 1961][research_baer_1961]] [[Baer 1966][research_baer_1966]] [[Baganoff 1990][research_baganoff_1990]] [[Bai et al 2014][research_bai_ren_2014]] [[Balakrishnan et al 1997][research_balakrishnan_shen_1997]] [[Balland et al 2015][research_balland_fernandezvillace_2015]] [[Bansal et al 2010][research_bansal_modest_2010]] [[Bansal et al 2010][research_bansal_modest_2010_b]] [[Baranovskii and Levin 1990][research_baranovskii_levin_1990]] [[Barnes and Segal 2015][research_barnes_segal_2015]] [[Barr et al 2026][research_barr_figueroa_2026]] [[Barrett 2025][research_barrett_2025]] [[Bartusiak et al 2022][research_bartusiak_hao_2022]] [[Baruzzi et al 2021][research_baruzzi_karchani_2021]] [[Barz 2026][research_barz_2026]] [[Bauer 1967][research_bauer_1967]] [[Bauer 2004][research_bauer_2004]] [[Baysal and Luo 1998][research_baysal_luo_1998]] [[Bedarev and Fedorova 2001][research_bedarev_fedorova_2001]] [[Bencze 1972][research_bencze_1972]] [[Bencze and Sorensen 1970][research_bencze_sorensen_1970]] [[Bennett 1971][research_bennett_1971]] [[Bensassi et al 2010][research_bensassi_lani_2010]] [[Bensassi et al 2013][research_bensassi_lani_2013]] [[Benson et al 1976][research_benson_sedgwick_1976]] [[Benstein 1989][research_benstein_1989]] [[Benton 1990][research_benton_1990]] [[Berthelot et al 2026][research_berthelot_craft_2026]] [[Bertin et al 1997][research_bertin_towne_1997]] [[Bestman 1991][research_bestman_1991]] [[Bhat and Lind 2009][research_bhat_lind_2009]] [[Bhungalia et al 2000][research_bhungalia_zweber_2000]] [[Bhutta and Lewis 1988][research_bhutta_lewis_1988]] [[Bilchenko 2015][research_bilchenko_2015]] [[Billig 1967][research_billig_1967]] [[Bin and Hongxin 2006][research_bin_hongxin_2006]] [[Bityurin and Bocharov 2010][research_bityurin_bocharov_2010]] [[Boeing Scientific Research Labs Seattle Wa 1963][research_boeingscientificresearchlabsseattlewa_1963]] [[Bogdanoff and Christiansen 1978][research_bogdanoff_christiansen_1978]] [[Bogdnoff 1953][research_bogdnoff_1953]] [[Bogdonoff 1970][research_bogdonoff_1970]] [[Bogdonoff 1999][research_bogdonoff_1999]] [[Bokor et al 2026][research_bokor_chamarthi_2026]] [[Boland et al 2023][research_boland_hinkle_2023]] [[Bolender and Doman 2005][research_bolender_doman_2005]] [[Bolender and Doman 2006][research_bolender_doman_2006]] [[Bolender et al 2007][research_bolender_oppenheimer_2007]] [[Bonelli et al 2011][research_bonelli_cutrone_2011]] [[Boppe and Davis 1989][research_boppe_davis_1989]] [[Borovikov et al 1996][research_borovikov_gavriliouk_1996]] [[Borrelli et al 1998][research_borrelli_marini_1998]] [[Bowcutt 2001][research_bowcutt_2001]] [[Bowman 1995][research_bowman_1995]] [[Bowman et al 1997][research_bowman_hanson_1997]] [[Boyd 1999][research_boyd_1999]] [[Boyd 2001][research_boyd_2001]] [[Boyd 2002][research_boyd_2002]] [[Boyd 2008][research_boyd_2008]] [[Boyd 2013][research_boyd_2013]] [[Boyd 2015][research_boyd_2015]] [[Boyd 2024][research_boyd_2024]] [[Boyer 1965][research_boyer_1965]] [[Boyer et al 1960][research_boyer_eschenroeder_1960]] [[Bricker et al 1989][research_bricker_numbers_1989]] [[Brodsky 1970][research_brodsky_1970]] [[Brown 1978][research_brown_1978]] [[Brown and Donbar 2013][research_brown_donbar_2013]] [[Brown and Donbar 2015][research_brown_donbar_2015]] [[Brown et al 1963][research_brown_kramer_1963]] [[Bruno 2023][research_bruno_2023]] [[Bruno 2023][research_bruno_2023_b]] [[Bruno 2023][research_bruno_2023_c]] [[Bruno 2023][research_bruno_2023_d]] [[Brykina 1996][research_brykina_1996]] [[Bu and Lei 2018][research_bu_lei_2018]] [[Burnett and Czysz 1963][research_burnett_czysz_1963]] [[Butler et al 2022][research_butler_benitez_2022]] [[Butler et al 2023][research_butler_benitez_2023]] [[Butt 2013][research_butt_2013]] [[Butt et al 2010][research_butt_yan_2010]] [[Butt et al 2011][research_butt_yan_2011]] [[Cai and Huang 2022][research_cai_huang_2022]] [[Cai and Zhuang 2025][research_cai_zhuang_2025]] [[Cai et al 2026][research_cai_zhuang_2026]] [[Caledonia and Krech 1994][research_caledonia_krech_1994]] [[Calise and Bae 1987][research_calise_bae_1987]] [[Calligeros and Dugundji 1961][research_calligeros_dugundji_1961]] [[Cambier and Adelman 1997][research_cambier_adelman_1997]] [[Candler 1989][research_candler_1989_b]] [[Candler 2001][research_candler_2001]] [[Candler 2010][research_candler_2010]] [[Candler, Graham and Park, Chul 1988][research_candlergraham_parkchul_1988]] [[Cangelosi et al 2024][research_cangelosi_heinkenschloss_2024]] [[Cao et al 2019][research_cao_he_2019]] [[Carlomagno et al 1993][research_carlomagno_luca_1993]] [[Cassanova 1967][research_cassanova_1967]] [[Casseau et al 2022][research_casseau_zhang_2022]] [[Cassidy and Halley 1991][research_cassidy_halley_1991]] [[Catalano and Sturek 2001][research_catalano_sturek_2001]] [[Cavity-actuated supersonic mixing and 1995][research_cavity_actuated_supersonic_1995]] [[Cazier, Jr. and Ricketts 1991][research_cazierjr_ricketts_1991]] [[Celmins 1990][research_celmins_1990]] [[Chakravarthy et al 1988][research_chakravarthy_szema_1988]] [[Chamberlain and Baltar 1993][research_chamberlain_baltar_1993]] [[Chang 1962][research_chang_1962]] [[Chang 2025][research_chang_2025]] [[Chang and Choudhari 2010][research_chang_choudhari_2010]] [[Chao Song et al 2011][research_chaosong_guorongzhao_2011]] [[Chapter 5 Physicochemical Models 2013][research_chapter_5_2013]] [[Che and Tang 2008][research_che_tang_2008]] [[Chen et al 2006][research_chen_williamson_2006]] [[Chen et al 2008][research_chen_agarwal_2008]] [[Chen et al 2016][research_chen_liu_2016]] [[Chen et al 2017][research_chen_guo_2017]] [[Chen et al 2017][research_chen_ni_2017]] [[Chen et al 2018][research_chen_yan_2018]] [[Chen et al 2018][research_chen_jing_2018]] [[Chen et al 2018][research_chen_niu_2018]] [[Chen et al 2020][research_chen_fan_2020]] [[Chen et al 2020][research_chen_fan_2020_b]] [[Chen et al 2020][research_chen_zhou_2020]] [[Chen et al 2020][research_chen_zhou_2020_b]] [[Chen et al 2025][research_chen_lu_2025]] [[Cheng 1960][research_cheng_1960]] [[Cheng 1993][research_cheng_1993]] [[Cheng and Liu 2015][research_cheng_liu_2015]] [[Cheng et al 2018][research_cheng_wang_2018]] [[Cheng et al 2019][research_cheng_yan_2019]] [[Cheng et al 2021][research_cheng_yan_2021]] [[Chengbin Lian et al 2012][research_chengbinlian_zhangren_2012]] [[Chi et al 2021][research_chi_wang_2021]] [[Choi and Driscoll 2024][research_choi_driscoll_2024]] [[Chourushi et al 2021][research_chourushi_singh_2021]] [[Chow 1979][research_chow_1979]] [[Chuang and Morimoto 1996][research_chuang_morimoto_1996]] [[Chuang and Morimoto 1997][research_chuang_morimoto_1997]] [[Chudej 1993][research_chudej_1993]] [[Chudoba et al 2015][research_chudoba_haney_2015]] [[Clark 1966][research_clark_1966]] [[Clark et al 2006][research_clark_mirmirani_2006]] [[Clarke 1989][research_clarke_1989]] [[Cole 1988][research_cole_1988]] [[Cole et al 1980][research_cole_cook_1980]] [[Colwill et al 1969][research_colwill_curran_1969]] [[Combustion in Supersonic Flows 2006][research_combustion_in_2006]] [[Congress will hasten US 2024][research_congress_will_2024]] [[Connolly and Loth 2020][research_connolly_loth_2020]] [[Connolly and Loth 2021][research_connolly_loth_2021]] [[Cookson 1976][research_cookson_1976]] [[Cornell Aeronautical Lab Inc Buffalo Ny 1963][research_cornellaeronauticallabincbuffalony_1963]] [[Correction to "Shape Optimization 2026][research_correction_to_2026]] [[Coupled dynamic model of 2018][research_coupled_dynamic_2018]] [[Creating Hypersonic Flow in 2019][research_creating_hypersonic_2019]] [[Creating Hypersonic Flow in 2019][research_creating_hypersonic_2019_b]] [[Cresci 1966][research_cresci_1966]] [[Crown 1950][research_crown_1950]] [[Cubbage et al 1970][research_cubbage_johnston_1970]] [[Culler and McNamara 2011][research_culler_mcnamara_2011]] [[Curran et al 2003][research_curran_hunt_2003]] [[Cvrlje 1999][research_cvrlje_1999]] [[Cvrlje and Laschka 2001][research_cvrlje_laschka_2001]] [[Czysz 1963][research_czysz_1963]] [[Czysz 1963][research_czysz_1963_b]] [[Dalle and Driscoll 2012][research_dalle_driscoll_2012]] [[Dalle et al 2010][research_dalle_frendreis_2010]] [[Dalle et al 2011][research_dalle_torrez_2011]] [[Danberg 1961][research_danberg_1961]] [[Danehy et al 2015][research_danehy_bathel_2015]] [[Das et al 2015][research_das_kim_2015]] [[Daub et al 2020][research_daub_esser_2020]] [[David O. Sigthorsson 2006][research_davidosigthorsson_2006]] [[Decker 2010][research_decker_2010]] [[Decker and Laschka 2001][research_decker_laschka_2001]] [[DeMange et al 2007][research_demange_dunlap_2007]] [[Demetriades 1975][research_demetriades_1975]] [[Demetriades 1983][research_demetriades_1983]] [[Demetriades 1985][research_demetriades_1985]] [[Dendy et al 2026][research_dendy_hayes_2026]] [[Deng 2026][research_deng_2026]] [[Deng and Zhao 2026][research_deng_zhao_2026]] [[DeSpirito 2013][research_despirito_2013]] [[Dewell and Speyer 1993][research_dewell_speyer_1993]] [[Dietrick 2013][research_dietrick_2013]] [[Dimotakis and Leonard 1998][research_dimotakis_leonard_1998]] [[Ding et al 2020][research_ding_wang_2020]] [[Ding et al 2023][research_ding_li_2023]] [[Disturbance Rejection For Airbreathing 2016][research_disturbance_rejection_2016]] [[Dong and Cai 2017][research_dong_cai_2017]] [[Dong et al 2021][research_dong_guo_2021]] [[Dong et al 2023][research_dong_huang_2023]] [[Doolan 2006][research_doolan_2006]] [[Doronzo 2026][research_doronzo_2026]] [[Dou et al 2024][research_dou_yu_2024]] [[Douglas and Bhushan 2025][research_douglas_bhushan_2025]] [[Douglas and Bhushan 2025][research_douglas_bhushan_2025_b]] [[Douglas and Lindgren 1999][research_douglas_lindgren_1999]] [[Drummond, J. Philip et al 1989][research_drummondjphilip_carpentermarkh_1989]] [[Du et al 2023][research_du_wang_2023]] [[Du et al 2026][research_du_li_2026]] [[Duan and Zhang 2016][research_duan_zhang_2016]] [[Duan et al 2011][research_duan_sun_2011]] [[Duan et al 2024][research_duan_xu_2024]] [[Dudin 2002][research_dudin_2002]] [[Dudley and Ukeiley 2011][research_dudley_ukeiley_2011]] [[Dugundji 1965][research_dugundji_1965]] [[Durant et al 2015][research_durant_andre_2015]] [[Dvořák 1965][research_dvorak_1965]] [[Dwoyer 1973][research_dwoyer_1973]] [[Dwoyer and Kumar 1987][research_dwoyer_kumar_1987]] [[Dyakonov et al 2012][research_dyakonov_schoenenberger_2012]] [[Eason and Spottswood 2013][research_eason_spottswood_2013]] [[Edwards and Babikian 1987][research_edwards_babikian_1987]] [[Edwards et al 2024][research_edwards_arbolino_2024]] [[Egorov and Erofeev 1997][research_egorov_erofeev_1997]] [[El-Askary 2011][research_elaskary_2011]] [[Elliott 1968][research_elliott_1968]] [[Ely][research_ely]] [[Enkenhus 1969][research_enkenhus_1969]] [[Epstein 1954][research_epstein_1954]] [[Ericsson 1968][research_ericsson_1968]] [[Ericsson 1977][research_ericsson_1977]] [[Ericsson 1977][research_ericsson_1977_b]] [[Ericsson 1978][research_ericsson_1978]] [[Ericsson and Scholnick 1968][research_ericsson_scholnick_1968]] [[Escher 1996][research_escher_1996]] [[Escher and Ehrlic 2000][research_escher_ehrlic_2000]] [[Espinosa 2003][research_espinosa_2003]] [[Evans et al 2011][research_evans_zok_2011]] [[Evolution of Disturbances from 2024][research_evolution_of_disturbances_2024]] [[Facility Requirements for Hypersonic 1991][research_facility_requirements_1991]] [[Fain et al 2026][research_fain_lambert_2026]] [[Falempin and Serre 2006][research_falempin_serre_2006_b]] [[Falkiewicz et al 2010][research_falkiewicz_cesnik_2010]] [[Fan et al 2009][research_fan_liu_2009]] [[Fan et al 2016][research_fan_zhu_2016]] [[Fan et al 2016][research_fan_yan_2016]] [[Fan et al 2017][research_fan_wu_2017]] [[Fan et al 2017][research_fan_lu_2017]] [[Fan et al 2017][research_fan_yan_2017]] [[Fan et al 2024][research_fan_qi_2024]] [[Fang et al 2024][research_fang_jiang_2024]] [[Fedorov and Khokhlov 2001][research_fedorov_khokhlov_2001]] [[Fedorov and Khokhlov 2002][research_fedorov_khokhlov_2002]] [[Feie and Kretz 2008][research_feie_kretz_2008]] [[Fejer et al 1964][research_fejer_heath_1964]] [[Fenfen et al 2020][research_fenfen_xubo_2020]] [[Feng 2022][research_feng_2022]] [[Feng and Zhang 2016][research_feng_zhang_2016]] [[Feng et al 2017][research_feng_tan_2017]] [[Feng et al 2020][research_feng_lv_2020]] [[Feng et al 2022][research_feng_wang_2022]] [[Feng et al 2026][research_feng_tang_2026]] [[Ferguson et al 2018][research_ferguson_dasque_2018]] [[Fergusson][research_fergusson]] [[Fermen-Coker and Johnson 1999][research_fermencoker_johnson_1999]] [[Ferrier et al 2008][research_ferrier_orlik_2008]] [[Fetterhoff and Burfitt 2011][research_fetterhoff_burfitt_2011]] [[Finley 1990][research_finley_1990]] [[Fiorentini and Serrani 2012][research_fiorentini_serrani_2012]] [[Fiorentini et al 2009][research_fiorentini_serrani_2009]] [[Flaherty et al 2010][research_flaherty_andrews_2010]] [[Forbes 2012][research_forbes_2012]] [[Forbes-Spyratos et al 2014][research_forbesspyratos_jahn_2014]] [[Foreman 1963][research_foreman_1963]] [[Forsythe et al 1961][research_forsythe_melfi_1961]] [[Franciscus 1981][research_franciscus_1981]] [[Franciscus 1981][research_franciscus_1981_b]] [[Froning 2006][research_froning_2006]] [[Froning, Jr. and Bussard 1993][research_froningjr_bussard_1993]] [[Froning, Jr. and Roach 1999][research_froningjr_roach_1999]] [[Fu et al 2015][research_fu_wang_2015]] [[Fu et al 2018][research_fu_li_2018]] [[Fu et al 2024][research_fu_song_2024_b]] [[Fu et al 2024][research_fu_wan_2024]] [[Fuels for Hypersonic Air-Breathing 2022][research_fuels_for_2022]] [[Fukuzawa et al 2025][research_fukuzawa_iguchi_2025]] [[Fulmer and Wirtz 1964][research_fulmer_wirtz_1964]] [[Fusaro and Viola 2020][research_fusaro_viola_2020]] [[Gager and Schleter 1949][research_gager_schleter_1949]] [[Gaiduchenko and Gritsyk 2019][research_gaiduchenko_gritsyk_2019]] [[Galaktionov et al 2006][research_galaktionov_lapygin_2006]] [[Galli et al 2004][research_galli_corbel_2004]] [[Gamertsfelder et al 2022][research_gamertsfelder_khare_2022]] [[Gao 2023][research_gao_2023]] [[Gao et al 2014][research_gao_li_2014]] [[Gao et al 2018][research_gao_chen_2018]] [[Gao et al 2020][research_gao_chen_2020]] [[Gao et al 2026][research_gao_liu_2026]] [[Gartling 1970][research_gartling_1970]] [[Geng et al 2017][research_geng_liu_2017]] [[Geshele et al 2013][research_geshele_polezhaev_2013]] [[Ghenai et al 2005][research_ghenai_philippidis_2005]] [[Giehler][research_giehler]] [[Gimelshein 2019][research_gimelshein_2019]] [[Ginoux 1966][research_ginoux_1966]] [[Gladden et al 1990][research_gladden_melis_1990]] [[Glass and Glass 2002][research_glass_glass_2002]] [[Gnoffo 1989][research_gnoffo_1989]] [[Gnoffo 2007][research_gnoffo_2007]] [[Gnoffo, Peter A. et al 1987][research_gnoffopetera_mccandlessronalds_1987]] [[Gockel 1993][research_gockel_1993]] [[Gogineni 1991][research_gogineni_1991]] [[Gol'dfel'd 1985][research_goldfeld_1985]] [[Goldberg and Scala 1965][research_goldberg_scala_1965]] [[Gollan and Smart 2013][research_gollan_smart_2013]] [[Gollan, Rowan J. and Smart, Michael K. 2010][research_gollanrowanj_smartmichaelk_2010]] [[Golovachev 1979][research_golovachev_1979]] [[Golovachev 1979][research_golovachev_1979_b]] [[Golovachev 1981][research_golovachev_1981]] [[Golubinskii and Golubkin 1983][research_golubinskii_golubkin_1983]] [[Golubkin 1992][research_golubkin_1992]] [[Golubkin and Negoda 1995][research_golubkin_negoda_1995]] [[Golubkin and Postnov 2000][research_golubkin_postnov_2000]] [[Gong et al 2006][research_gong_yuan_2006]] [[Gorshkov and Lunev 2002][research_gorshkov_lunev_2002]] [[Gottlieb and Don 2008][research_gottlieb_don_2008]] [[Goyal et al 2023][research_goyal_prasad_2023]] [[Goz and Theodoulis 2025][research_goz_theodoulis_2025]] [[Grady and Madzsar 1998][research_grady_madzsar_1998]] [[Grady et al 2016][research_grady_pitz_2016]] [[Grant 2013][research_grant_2013]] [[Gray 1965][research_gray_1965]] [[Green][research_green]] [[Gringorten 1967][research_gringorten_1967]] [[Gringorten and Tattelman 1970][research_gringorten_tattelman_1970]] [[Groves et al 2005][research_groves_serrani_2005]] [[Guan et al 2013][research_guan_wang_2013]] [[Guan Ping et al 2012][research_guanping_xueli_2012]] [[Guangbin Cai et al 2010][research_guangbincai_guangrenduan_2010]] [[Guangren et al 2015][research_guangren_yanmei_2015]] [[Guderley 1987][research_guderley_1987]] [[Guderley 1988][research_guderley_1988]] [[Gunderson 1963][research_gunderson_1963]] [[Guo and Liu 2024][research_guo_liu_2024]] [[Guo et al 2016][research_guo_wang_2016]] [[Guo et al 2023][research_guo_yang_2023]] [[Guotong Sun and Shuo Tang 2010][research_guotongsun_shuotang_2010]] [[Gusev et al 1993][research_gusev_blagoveshchenskij_1993]] [[Gülçat 2010][research_gulcat_2010]] [[Gülçat 2015][research_gulcat_2015]] [[GÜlçat 2021][research_gulcat_2021]] [[H Julian Allen 1958][research_hjulianallen_1958]] [[Hall et al 2026][research_hall_schemmel_2026]] [[Hallion 1998][research_hallion_1998]] [[Halter and Cliff 1991][research_halter_cliff_1991]] [[Han et al 2024][research_han_wang_2024_b]] [[Hanquist and Boyd 2018][research_hanquist_boyd_2018]] [[Hao and Yongqi 2024][research_hao_yongqi_2024]] [[Harloff 1987][research_harloff_1987]] [[Harney 1963][research_harney_1963]] [[Hassan et al 2001][research_hassan_kuntz_2001]] [[Hawkins and Richardson 1991][research_hawkins_richardson_1991]] [[Hayes 1959][research_hayes_1959]] [[He et al 2016][research_he_liu_2016]] [[He et al 2017][research_he_liu_2017]] [[He et al 2021][research_he_gao_2021]] [[Heathman and Kelly 1966][research_heathman_kelly_1966]] [[Heiser et al 1994][research_heiser_pratt_1994]] [[Heitmeier and Bissinger 1995][research_heitmeier_bissinger_1995]] [[Heitmeir et al 1992][research_heitmeir_lederer_1992]] [[Hejranfar et al 2011][research_hejranfar_najafi_2011]] [[Heller et al 2000][research_heller_holzapfel_2000]] [[Hemming 1966][research_hemming_1966]] [[Henderson 1991][research_henderson_1991]] [[Henson and Robertson 1962][research_henson_robertson_1962]] [[Herbert 1992][research_herbert_1992]] [[Herdy 2025][research_herdy_2025]] [[Herdy 2025][research_herdy_2025_b]] [[Hermann and Schmidt 1995][research_hermann_schmidt_1995]] [[Hermann, R. 1965][research_hermannr_1965]] [[Herrlin and Gelderloos 1988][research_herrlin_gelderloos_1988]] [[Herrmann et al 2025][research_herrmann_cox_2025]] [[Hersh and Gerstein 1970][research_hersh_gerstein_1970]] [[Higgins et al 2002][research_higgins_inger_2002]] [[High-Temperature Gas Dynamics and 2009][research_high_temperature_gas_2009]] [[Hinderks et al 2004][research_hinderks_gulhan_2004]] [[Hirschel and Meier 2004][research_hirschel_meier_2004]] [[Hirschel and Weiland 2009][research_hirschel_weiland_2009_b]] [[Hoffert 1968][research_hoffert_1968]] [[Hoffmann 2000][research_hoffmann_2000]] [[Hollanders et al 1992][research_hollanders_laval_1992]] [[Holm-Hansen et al 2010][research_holmhansen_lee_2010]] [[Hommel 1989][research_hommel_1989]] [[Hong et al 2014][research_hong_xiong_2014]] [[Hong Qian. Lu et al 2011][research_hongqianlu_dongmingge_2011]] [[Hongbo and Yongyuan 2016][research_hongbo_yongyuan_2016]] [[Hopkins][research_hopkins]] [[Hornung 2001][research_hornung_2001]] [[Hornung et al 2003][research_hornung_ponchaut_2003]] [[Hostetler 2005][research_hostetler_2005]] [[Hou et al 2015][research_hou_wang_2015]] [[Hromas and Lees 1962][research_hromas_lees_1962]] [[Hsu et al 2007][research_hsu_carter_2007]] [[Hsu et al 2010][research_hsu_carter_2010]] [[Hu and Liu 2013][research_hu_liu_2013]] [[Hu et al 2008][research_hu_bodson_2008]] [[Hu et al 2010][research_hu_sun_2010]] [[Hu et al 2018][research_hu_li_2018]] [[Hu et al 2021][research_hu_chen_2021]] [[Hu et al 2022][research_hu_dong_2022]] [[Hu et al 2022][research_hu_guo_2022]] [[Hu et al 2022][research_hu_yang_2022]] [[Hu et al 2025][research_hu_liu_2025]] [[Huang and Xing 2005][research_huang_xing_2005]] [[Huang et al 2017][research_huang_zhang_2017]] [[Huang et al 2018][research_huang_zhang_2018]] [[Huang et al 2018][research_huang_yang_2018]] [[Huang et al 2026][research_huang_zhang_2026]] [[Huebner et al 2003][research_huebner_witte_2003]] [[Hughes and Wu 2010][research_hughes_wu_2010]] [[Hughes and Wu 2012][research_hughes_wu_2012]] [[Hui and Hu 2006][research_hui_hu_2006]] [[Human 2002][research_human_2002]] [[Hunt 1989][research_hunt_1989]] [[Hunt and Eiswirth 1996][research_hunt_eiswirth_1996]] [[Hunt and Rausch 1998][research_hunt_rausch_1998]] [[Hunt et al 1978][research_hunt_lawing_1978]] [[Hunt et al 1979][research_hunt_lawing_1979]] [[Hunt et al 1997][research_hunt_lockwood_1997]] [[Hunt, J. L. et al 1978][research_huntjl_lawingpl_1978]] [[Huo et al 2006][research_huo_mirmirani_2006]] [[Hutt 1987][research_hutt_1987]] [[Hutt and East 1983][research_hutt_east_1983]] [[Hypersonic Aerodynamics 1988][research_hypersonic_aerodynamics_1988]] [[Hypersonic Aerodynamics 2016][research_hypersonic_aerodynamics_2016]] [[Hypersonic Aerodynamics on the 2019][research_hypersonic_aerodynamics_2019]] [[Hypersonic Aerodynamics Slender Bodies 2025][research_hypersonic_aerodynamics_2025]] [[Hypersonic and Supersonic Flight 2023][research_hypersonic_and_2023]] [[Hypersonic Flight 2025][research_hypersonic_flight_2025]] [[Hypersonic flow in a 1989][research_hypersonic_flow_1989]] [[Hypersonic Flow Past Thin 2009][research_hypersonic_flow_2009]] [[Hypersonic Flows 2021][research_hypersonic_flows_2021]] [[Hypersonic Flows 2025][research_hypersonic_flows_2025]] [[Hypersonic Inviscid Flowfields Approximate 2006][research_hypersonic_inviscid_2006]] [[Hypersonic Inviscid Flowfields Approximate 2019][research_hypersonic_inviscid_2019]] [[Hypersonic Inviscid Flowfields Exact 2006][research_hypersonic_inviscid_2006_b]] [[Hypersonic Inviscid Flowfields Exact 2019][research_hypersonic_inviscid_2019_b]] [[Hypersonic Nonequilibrium Flows Fundamentals 2015][research_hypersonic_nonequilibrium_2015]] [[Hypersonic plane makes brief 2011][research_hypersonic_plane_2011]] [[Hypersonic Shock and Expansion-Wave 2006][research_hypersonic_shock_2006]] [[Hypersonic Shock and Expansion-Wave 2019][research_hypersonic_shock_2019]] [[Hypersonic Thin Viscous Shock 2018][research_hypersonic_thin_2018]] [[Ide et al 1989][research_ide_armstrong_1989]] [[Iliff, Kenneth W. and Shafer, Mary F. 1993][research_iliffkennethw_shafermaryf_1993]] [[Iliff, Kenneth W. and Shafer, Mary F. 1995][research_iliffkennethw_shafermaryf_1995]] [[Ingenito 2021][research_ingenito_2021_b]] [[Ingenito et al 2009][research_ingenito_bruno_2009]] [[Inger 1986][research_inger_1986]] [[Inger 1989][research_inger_1989]] [[Inger 1995][research_inger_1995]] [[Inger 2008][research_inger_2008]] [[Inger et al 2001][research_inger_higgins_2001]] [[Introduction to Hypersonic Air-Breathing 2022][research_introduction_to_2022]] [[Investigation of the Use 1974][research_investigation_of_1974]] [[Isbell][research_isbell]] [[Itabashi et al 1995][research_itabashi_honma_1995]] [[Jaeger and Hemati 2025][research_jaeger_hemati_2025]] [[Jammalamadaka et al 2014][research_jammalamadaka_li_2014]] [[Jasa et al 2018][research_jasa_mader_2018]] [[Ji and Zhou 2017][research_ji_zhou_2017]] [[Ji and Zhou 2018][research_ji_zhou_2018]] [[Ji et al 2019][research_ji_zhou_2019]] [[Jia et al 2004][research_jia_wenxiu_2004]] [[Jiang et al 2018][research_jiang_chen_2018]] [[Jiang et al 2020][research_jiang_zhou_2020]] [[Jiang et al 2024][research_jiang_liu_2024]] [[Jianguo et al 2018][research_jianguo_yifei_2018]] [[Jinchuan Hu et al 2015][research_jinchuanhu_jinglinli_2015]] [[Jing and Shuo 2008][research_jing_shuo_2008]] [[Jing and Yuan-pei 2015][research_jing_yuanpei_2015]] [[Jing-guang and Shen-min 2017][research_jingguang_shenmin_2017]] [[Jingang et al 2026][research_jingang_haotian_2026]] [[Jischke 1978][research_jischke_1978]] [[Johnson III and Wu 1974][research_johnsoniii_wu_1974]] [[Johnston et al 1971][research_johnston_cubbage_1971]] [[Jones, R. A. and Huber, P. W. 1978][research_jonesra_huberpw_1978]] [[Josyula and Bailey 2003][research_josyula_bailey_2003]] [[Josyula and Shang 1990][research_josyula_shang_1990]] [[Josyula and Vedula 2015][research_josyula_vedula_2015]] [[Kaiser and Fluegge-Lotz 1968][research_kaiser_flueggelotz_1968]] [[Kakatsios and Houzouris 1998][research_kakatsios_houzouris_1998]] [[Kanda et al 2003][research_kanda_kato_2003]] [[Kanda et al 2007][research_kanda_kato_2007]] [[Kang et al 2008][research_kang_tang_2008]] [[Kannaiyan 2020][research_kannaiyan_2020]] [[Kantrowitz and Petschek 1964][research_kantrowitz_petschek_1964]] [[Kauffman et al 1991][research_kauffman_grandhi_1991]] [[Kaushik 2018][research_kaushik_2018]] [[Kazmar 2005][research_kazmar_2005]] [[Kelly 1973][research_kelly_1973]] [[Keshmiri 2008][research_keshmiri_2008]] [[Keshmiri et al 2005][research_keshmiri_colgren_2005]] [[Keshmiri et al 2006][research_keshmiri_colgren_2006]] [[Keshmiri et al 2006][research_keshmiri_colgren_2006_b]] [[Keshmiri et al 2007][research_keshmiri_farokhi_2007]] [[Keshmiri et al 2007][research_keshmiri_colgren_2007]] [[Khairul Habib Pulok and Chakravarty 2021][research_khairulhabibpulok_chakravarty_2021]] [[Khambaswadkar 2024][research_khambaswadkar_2024]] [[Khorrami and Chang 1997][research_khorrami_chang_1997]] [[Khorunzhenko et al 2002][research_khorunzhenko_roupassov_2002]] [[Khurana and Suzuki 2013][research_khurana_suzuki_2013]] [[Kim 2003][research_kim_2003]] [[Kimmel 1993][research_kimmel_1993]] [[Kimmel and Poggie 1997][research_kimmel_poggie_1997]] [[Kimmel et al 2005][research_kimmel_hayes_2005]] [[King 1962][research_king_1962]] [[Kinslow and Busby 1973][research_kinslow_busby_1973]] [[Kirkpatrick][research_kirkpatrick]] [[Kitamura and Shima 2011][research_kitamura_shima_2011]] [[Klock and Cesnik 2015][research_klock_cesnik_2015]] [[Klock and Cesnik 2016][research_klock_cesnik_2016]] [[Knott 1974][research_knott_1974]] [[Ko and Jackson 1992][research_ko_jackson_1992]] [[Kokan et al 2004][research_kokan_olds_2004]] [[Kopp et al 1999][research_kopp_hollmeier_1999]] [[Korte and Mcrae 1989][research_korte_mcrae_1989]] [[Koschel and Rick 1991][research_koschel_rick_1991]] [[Koschel et al 1998][research_koschel_link_1998]] [[Kostoff et al 2003][research_kostoff_eberhart_2003]] [[Kostyk, Chris and Risch, Tim 2013][research_kostykchris_rischtim_2013]] [[Kotel'nikov et al 2020][research_kotelnikov_kotelnikov_2020]] [[Kothari et al 1996][research_kothari_tarpley_1996]] [[Kothari et al 2010][research_kothari_livingston_2010]] [[Krause et al 1991][research_krause_hartmann_1991]] [[Kremeyer and Pakhomov 2008][research_kremeyer_pakhomov_2008]] [[Krothapalli et al 2003][research_krothapalli_alvi_2003]] [[Kubota and Berg 1977][research_kubota_berg_1977]] [[Kudryavtsev et al 2009][research_kudryavtsev_mironov_2009]] [[Kuipers et al 2007][research_kuipers_mirmirani_2007]] [[Kuipers et al 2008][research_kuipers_ioannou_2008]] [[Kuipers et al 2009][research_kuipers_ioannou_2009]] [[Kulkarni and Phan 2003][research_kulkarni_phan_2003]] [[Kumar, Ajay et al 2001][research_kumarajay_drummondjphilip_2001]] [[Kuranov and Korabelnikov 2008][research_kuranov_korabelnikov_2008]] [[Kuranov and Korabelnikov 2008][research_kuranov_korabelnikov_2008_b]] [[Kurilova and Li 2026][research_kurilova_li_2026]] [[Kuznetsov 1992][research_kuznetsov_1992]] [[Kwak and Kiris 2003][research_kwak_kiris_2003]] [[Ladeinde 2020][research_ladeinde_2020_b]] [[Laderman 1979][research_laderman_1979]] [[Laderman and Demetriades 1977][research_laderman_demetriades_1977]] [[Ladyzhenskij 1963][research_ladyzhenskij_1963]] [[Lago et al 2012][research_lago_chpoun_2012]] [[Lahaye and Heckman 1968][research_lahaye_heckman_1968]] [[Lambert and Coughlin 1967][research_lambert_coughlin_1967]] [[Landesman and Basinski 1963][research_landesman_basinski_1963]] [[Latvala and Anderson 1959][research_latvala_anderson_1959]] [[Lawrence 1991][research_lawrence_1991]] [[Lawrence 1992][research_lawrence_1992]] [[Le et al 2012][research_le_greenshields_2012]] [[Le et al 2023][research_le_liu_2023]] [[Lederer et al 1991][research_lederer_schwab_1991]] [[Lee][research_lee]] [[Lee and James T. 1963][research_lee_jamest_1963]] [[Lee and Rasmussen 1978][research_lee_rasmussen_1978]] [[Lee and Van Dalsem 1981][research_lee_vandalsem_1981]] [[Lee et al 2007][research_lee_reiman_2007]] [[Lees and Hromas 1961][research_lees_hromas_1961]] [[Lees and Kubota 1972][research_lees_kubota_1972]] [[Lees and Reeves 1964][research_lees_reeves_1964]] [[Lempert and Miles 1995][research_lempert_miles_1995]] [[Lenard et al 1962][research_lenard_long_1962]] [[Leonov et al 2009][research_leonov_yarantsev_2009]] [[Levermore and Brio 1994][research_levermore_brio_1994]] [[Levin 2015][research_levin_2015]] [[Levin et al 2008][research_levin_ioannou_2008]] [[Lewis 2001][research_lewis_2001]] [[Lewis 2003][research_lewis_2003]] [[Leyland 1992][research_leyland_1992]] [[Li 1974][research_li_1974]] [[Li 2021][research_li_2021]] [[Li and Fu 2010][research_li_fu_2010]] [[Li and Nagamatsu 1953][research_li_nagamatsu_1953]] [[Li et al 2014][research_li_wu_2014]] [[Li et al 2015][research_li_zhang_2015]] [[Li et al 2016][research_li_yang_2016]] [[Li et al 2017][research_li_chen_2017]] [[Li et al 2018][research_li_hu_2018]] [[Li et al 2020][research_li_chen_2020]] [[Li et al 2020][research_li_yang_2020]] [[Li et al 2020][research_li_yang_2020_b]] [[Li et al 2021][research_li_jiang_2021]] [[Li et al 2021][research_li_zhou_2021]] [[Li et al 2021][research_li_jiang_2021_b]] [[Li et al 2022][research_li_li_2022]] [[Li et al 2022][research_li_zhou_2022]] [[Li et al 2026][research_li_zhao_2026]] [[Lian et al 2012][research_lian_shi_2012]] [[Lian et al 2013][research_lian_bai_2013_b]] [[Liang et al 2021][research_liang_xu_2021]] [[Liang et al 2025][research_liang_gao_2025]] [[Liang et al 2025][research_liang_wen_2025]] [[Light High-Temperature Aluminum Alloys 1992][research_light_high_temperature_1992]] [[Lijewski 1980][research_lijewski_1980]] [[Lin et al 1995][research_lin_shen_1995]] [[Lind et al 1999][research_lind_buffington_1999]] [[Linqi et al 2015][research_linqi_qun_2015]] [[Liu and Shen 2015][research_liu_shen_2015]] [[Liu et al 2005][research_liu_zhao_2005]] [[Liu et al 2009][research_liu_wang_2009]] [[Liu et al 2010][research_liu_hou_2010]] [[Liu et al 2014][research_liu_wang_2014]] [[Liu et al 2020][research_liu_luo_2020]] [[Liu et al 2020][research_liu_luo_2020_b]] [[Liu et al 2021][research_liu_xie_2021]] [[Liu et al 2022][research_liu_manzie_2022]] [[Liu et al 2022][research_liu_pang_2022]] [[Liu et al 2023][research_liu_cai_2023]] [[Liu et al 2025][research_liu_zhang_2025]] [[Lock et al 2025][research_lock_oberman_2025]] [[Lockwood et al 1996][research_lockwood_petley_1996]] [[Lockwood et al 1999][research_lockwood_petley_1999]] [[Loh and Hui 1991][research_loh_hui_1991]] [[Loper and Lightsey 1967][research_loper_lightsey_1967]] [[Lu and Jiang 2019][research_lu_jiang_2019]] [[Lu and Liu 2011][research_lu_liu_2011]] [[Lu et al 2016][research_lu_zhang_2016_b]] [[Lubing et al 2017][research_lubing_yang_2017]] [[Lubing et al 2020][research_lubing_yangfei_2020]] [[Luboński 1964][research_lubonski_1964]] [[Lukasiewicz 1961][research_lukasiewicz_1961]] [[Luo 1999][research_luo_1999]] [[Luo and Bray 1998][research_luo_bray_1998]] [[Lv and Zhou 2023][research_lv_zhou_2023]] [[Lüdeke and Schülein 2003][research_ludeke_schulein_2003]] [[Ma et al 2006][research_ma_yuan_2006]] [[Ma et al 2020][research_ma_wu_2020]] [[Ma et al 2023][research_ma_liu_2023]] [[Maccormack 1989][research_maccormack_1989]] [[Mackle][research_mackle]] [[Mackle and Jahn 2024][research_mackle_jahn_2024]] [[Mackle et al 2024][research_mackle_lock_2024]] [[Mahmoud et al 2017][research_mahmoud_hao_2017]] [[Maisaia 2023][research_maisaia_2023]] [[Maita et al 1990][research_maita_ohkami_1990]] [[Mallikarjun et al 2023][research_mallikarjun_casseau_2023]] [[Manke 2005][research_manke_2005]] [[Maorui Zhang et al 2010][research_maoruizhang_yongsun_2010]] [[Marconi, F. et al 1976][research_marconif_salasm_1976]] [[Marcum 2001][research_marcum_2001]] [[Marren et al 2001][research_marren_lewis_2001]] [[Marshall et al 2014][research_marshall_cox_2014]] [[Martin and Gerber 1953][research_martin_gerber_1953]] [[Martin et al 1998][research_martin_karasi_1998]] [[Mashburn 1969][research_mashburn_1969]] [[Maslov 2001][research_maslov_2001]] [[Masson et al 1989][research_masson_jumper_1989]] [[Matsuyama et al 2003][research_matsuyama_ohnishi_2003]] [[Mayrhofer and Sachs 1999][research_mayrhofer_sachs_1999]] [[Mbagwu et al 2018][research_mbagwu_driscoll_2018]] [[McClinton et al 1999][research_mcclinton_hunt_1999]] [[McCOWN et al 1966][research_mccown_barrett_1966]] [[McDonald and Mavris 2000][research_mcdonald_mavris_2000]] [[Mcintosh, Jr. 1964][research_mcintoshjr_1964]] [[Mcintosh, Jr. 1972][research_mcintoshjr_1972]] [[McRuer 1991][research_mcruer_1991]] [[Mease and Vinh 1988][research_mease_vinh_1988]] [[Measuring kinematic parameters of 1998][research_measuring_kinematic_1998]] [[Meng et al 2021][research_meng_tian_2021]] [[Merkli 1975][research_merkli_1975]] [[Merz 1968][research_merz_1968]] [[Messersmith 1995][research_messersmith_1995]] [[Messitt et al 1992][research_messitt_dallemagne_1992]] [[Mestwerdt and Rambauske 1961][research_mestwerdt_rambauske_1961]] [[Metghalchi 2009][research_metghalchi_2009]] [[Meuwly 2014][research_meuwly_2014]] [[Meyer 1969][research_meyer_1969]] [[Meyer et al 1997][research_meyer_butler_1997]] [[Miele 1962][research_miele_1962]] [[Miele and Hull 1963][research_miele_hull_1963]] [[Miele and Pritchard 1963][research_miele_pritchard_1963]] [[Miele and Saaris 1963][research_miele_saaris_1963]] [[Miles 1998][research_miles_1998]] [[Miles 2001][research_miles_2001]] [[Miles and Macheret 2006][research_miles_macheret_2006]] [[Millerd][research_millerd]] [[Mirmirani et al 2005][research_mirmirani_wu_2005]] [[Mironov and Aniskin 2004][research_mironov_aniskin_2004]] [[Misra 1994][research_misra_1994]] [[Moga 1980][research_moga_1980]] [[Montgomery and Garrard 2005][research_montgomery_garrard_2005]] [[Moran and Kolb 1977][research_moran_kolb_1977]] [[Moreira and Azevedo 2005][research_moreira_azevedo_2005]] [[Mori et al 2001][research_mori_maita_2001]] [[Morimoto and Chuang 1998][research_morimoto_chuang_1998]] [[Morinishi 1999][research_morinishi_1999]] [[Moss and Simmonds 1987][research_moss_simmonds_1987]] [[Moss et al 2006][research_moss_boyles_2006]] [[Moura and Ribeiro 2024][research_moura_ribeiro_2024]] [[Mueller 1989][research_mueller_1989]] [[Mungal 1998][research_mungal_1998]] [[Munipalli et al 2005][research_munipalli_subbarao_2005]] [[Murbach 1993][research_murbach_1993]] [[Murray 2012][research_murray_2012]] [[Murray and Steelant 2009][research_murray_steelant_2009]] [[Murray et al 2014][research_murray_tinney_2014]] [[Musal 1962][research_musal_1962]] [[Musal et al 1964][research_musal_hm_1964]] [[Musielak and Musielak 1997][research_musielak_musielak_1997]] [[Muslubas and Eyi 2015][research_muslubas_eyi_2015]] [[Myong 1999][research_myong_1999]] [[Myrabo 2004][research_myrabo_2004]] [[Myrabo et al 1995][research_myrabo_head_1995]] [[Nagdewe and Shevare 2006][research_nagdewe_shevare_2006]] [[Nagel and Becker 1973][research_nagel_becker_1973]] [[Nakamori and Nakamura 1995][research_nakamori_nakamura_1995]] [[Nance 2013][research_nance_2013]] [[Nangia 2011][research_nangia_2011]] [[Narayan 1994][research_narayan_1994]] [[Naval Ordnance Systems Command Washington Dc 1957][research_navalordnancesystemscommandwashingtondc_1957]] [[Neuwerth et al 1998][research_neuwerth_peiter_1998]] [[Neuwerth et al 1999][research_neuwerth_peiter_1999]] [[New-Generation Hypersonic Adiabatic Compression 2002][research_new_generation_hypersonic_2002]] [[Newell and Zakharov 2007][research_newell_zakharov_2007]] [[Newman et al 1992][research_newman_fulcher_1992]] [[Ng and Dressler 2002][research_ng_dressler_2002]] [[Nguyen-Bui and Duffa 2004][research_nguyenbui_duffa_2004]] [[Nicholas J DiGregorio et al][research_nicholasjdigregorio_thomaskwestiv]] [[Nickerson et al 1988][research_nickerson_dunn_1988]] [[Nicolaides and Brady 1959][research_nicolaides_brady_1959]] [[Nicoll 1962][research_nicoll_1962]] [[Nietubicz 1975][research_nietubicz_1975]] [[Nishida 2011][research_nishida_2011]] [[Nishino 1993][research_nishino_1993]] [[Nishio 1996][research_nishio_1996]] [[Nishio and Hagiwara 1998][research_nishio_hagiwara_1998]] [[Nompelis et al 2005][research_nompelis_drayna_2005]] [[Nompelis et al 2006][research_nompelis_drayna_2006]] [[Nompelis et al 2007][research_nompelis_wan_2007]] [[Nompelis et al 2011][research_nompelis_bender_2011]] [[Noori and Karimian 2008][research_noori_karimian_2008]] [[Noren 2008][research_noren_2008]] [[North American Aviation Inc Los Angeles Ca 1964][research_northamericanaviationinclosangelesca_1964]] [[Northam, G. B. 1985][research_northamgb_1985]] [[Novelli and Koschel 2001][research_novelli_koschel_2001]] [[Nydick et al 1995][research_nydick_friedmann_1995]] [[O'Brien and Lewis 2001][research_obrien_lewis_2001]] [[O'Byrne et al 2014][research_obyrne_gai_2014]] [[O'Neal et al 2026][research_oneal_desilva_2026]] [[Ocheltree 1993][research_ocheltree_1993]] [[Odabas and Sarigul-Klijn 1992][research_odabas_sarigulklijn_1992]] [[Ognjanovic et al 2017][research_ognjanovic_maksimovic_2017]] [[Okuno and Watanabe 1992][research_okuno_watanabe_1992]] [[Olsen 1965][research_olsen_1965]] [[Opalka 1968][research_opalka_1968]] [[Oppenheimer and Doman][research_oppenheimer_doman]] [[Oppenheimer and Doman 2006][research_oppenheimer_doman_2006]] [[Oppenheimer et al 2007][research_oppenheimer_skujins_2007]] [[Oppenheimer et al 2008][research_oppenheimer_doman_2008]] [[Oppenheimer et al 2008][research_oppenheimer_skujins_2008]] [[Optimal Aerodynamic Shapes Of 1996][research_optimal_aerodynamic_1996]] [[Ormsbee 1962][research_ormsbee_1962]] [[Ortloff 1968][research_ortloff_1968]] [[Ouzts 2008][research_ouzts_2008]] [[Owen and Owen 2007][research_owen_owen_2007]] [[Owotunse et al 2023][research_owotunse_ogwumike_2023]] [[Padmapriya and Reddy 1998][research_padmapriya_reddy_1998]] [[Palmer and Venkatapathy 1993][research_palmer_venkatapathy_1993]] [[Paquette and Palko 2004][research_paquette_palko_2004]] [[Paredes et al 2017][research_paredes_choudhari_2017]] [[Parker 2022][research_parker_2022]] [[Parthasarathy et al 2014][research_parthasarathy_cinibulk_2014]] [[Paul et al 2014][research_paul_binner_2014]] [[Peng et al 2014][research_peng_peng_2014]] [[Peng et al 2019][research_peng_feng_2019]] [[Peng et al 2019][research_peng_qi_2019]] [[Perlini et al 2026][research_perlini_bertolini_2026]] [[Perminov 1969][research_perminov_1969]] [[Perrier et al 1995][research_perrier_rostand_1995]] [[Perrier et al 1996][research_perrier_rapuc_1996]] [[Peters and Phares 1976][research_peters_phares_1976]] [[Peterson 2019][research_peterson_2019]] [[Petley and Dziedzic 1993][research_petley_dziedzic_1993]] [[Pfaff 1965][research_pfaff_1965]] [[Phillips and Cruz 1991][research_phillips_cruz_1991]] [[Phillips and Cruz 1993][research_phillips_cruz_1993]] [[Piao et al 2019][research_piao_zhang_2019]] [[Pike 2006][research_pike_2006]] [[Pinto et al 2023][research_pinto_whyman_2023]] [[Pipko 1966][research_pipko_1966]] [[Piscitelli et al 2017][research_piscitelli_cutrone_2017]] [[Platou 1959][research_platou_1959]] [[Poplavskaya 2002][research_poplavskaya_2002]] [[Porter 1965][research_porter_1965]] [[Portis et al 2024][research_portis_dambrosio_2024]] [[Poulain et al 2009][research_poulain_pietlahanie_2009]] [[Pozefsky 1989][research_pozefsky_1989]] [[Prabhu 1995][research_prabhu_1995]] [[Prakash and Singh 2021][research_prakash_singh_2021]] [[Prakash et al 2010][research_prakash_parsons_2010]] [[Pratt 1971][research_pratt_1971]] [[Preller][research_preller]] [[Priyamvada et al 2015][research_priyamvada_singh_2015]] [[Probstein 1953][research_probstein_1953]] [[Pulok and Chakravarty 2020][research_pulok_chakravarty_2020]] [[Qi and Jianliang 2017][research_qi_jianliang_2017]] [[Qiao Yongjie et al 2011][research_qiaoyongjie_liujinrong_2011]] [[Qin Changmao et al 2010][research_qinchangmao_qinaiming_2010]] [[Qin et al 2013][research_qin_zhu_2013]] [[Quick et al 2005][research_quick_king_2005]] [[R Wayne Guy 1990][research_rwayneguy_1990]] [[Radiation Properties of Hypersonic 2018][research_radiation_properties_2018]] [[Raghunandan and Ruffin 2016][research_raghunandan_ruffin_2016]] [[Ramasubramanian et al 2008][research_ramasubramanian_starkey_2008]] [[Ramunno et al 2021][research_ramunno_boyd_2021]] [[Ramunno et al 2022][research_ramunno_boyd_2022]] [[Raney et al 1993][research_raney_mcminn_1993]] [[Rasmussen 1978][research_rasmussen_1978]] [[Rasmussen et al 2005][research_rasmussen_driscoll_2005]] [[Rataczak et al 2023][research_rataczak_mcmahon_2023]] [[Rataczak et al 2024][research_rataczak_chaudhry_2024]] [[Rathakrishnan 2025][research_rathakrishnan_2025]] [[Rauh et al 2026][research_rauh_reimer_2026]] [[Reed 1997][research_reed_1997]] [[Reed 2013][research_reed_2013]] [[Regan 1964][research_regan_1964]] [[Rehman et al 2009][research_rehman_fidan_2009]] [[Rehman et al 2010][research_rehman_petersen_2010]] [[Reimer et al 2026][research_reimer_dimartino_2026]] [[Reklis and Conti 1984][research_reklis_conti_1984]] [[Ren 2009][research_ren_2009]] [[Ren and Yang 2017][research_ren_yang_2017]] [[Ren et al 2017][research_ren_fu_2017]] [[Ren et al 2023][research_ren_wu_2023]] [[Research and Technology Organisation RTO 2005][research_researchandtechnologyorganisationrto_2005]] [[Research Progress in Active 2026][research_research_progress_2026]] [[Response of Miniature Pressure 1974][research_response_of_1974]] [[Reviznikov et al 2018][research_reviznikov_sposobin_2018]] [[Rhudy et al 1960][research_rhudy_hiers_1960]] [[Riabov 2002][research_riabov_2002]] [[Riabov 2003][research_riabov_2003]] [[Riabov 2011][research_riabov_2011]] [[Riabov and Botin 1999][research_riabov_botin_1999]] [[Riabov and Riabov 1997][research_riabov_riabov_1997]] [[Ricciardi 1991][research_ricciardi_1991]] [[Richardson and Herrmann 1966][research_richardson_herrmann_1966]] [[Riedelbauch and Brenner 1990][research_riedelbauch_brenner_1990]] [[Riedelbauch et al 1989][research_riedelbauch_brenner_1989]] [[Righi 2015][research_righi_2015]] [[Rodighiero][research_rodighiero]] [[Rodriguez-Segade et al 2020][research_rodriguezsegade_hernandez_2020]] [[Rom 1965][research_rom_1965]] [[Rose and Teare 1964][research_rose_teare_1964]] [[Rose et al 2009][research_rose_thoma_2009]] [[Roth and Mavris 1999][research_roth_mavris_1999]] [[Rotta 1966][research_rotta_1966]] [[Rowan Gollan][research_rowangollan]] [[Ruble 1964][research_ruble_1964]] [[Rudiments and Methodology for 2001][research_rudiments_and_2001]] [[Rued et al 1991][research_rued_mark_1991]] [[Ruimin and Jianguo 2018][research_ruimin_jianguo_2018]] [[Sachs et al 1995][research_sachs_schoder_1995]] [[Sahu 1986][research_sahu_1986]] [[Sahu 2007][research_sahu_2007]] [[Sahu et al 2024][research_sahu_vasile_2024]] [[Saida 1986][research_saida_1986]] [[Salvador et al 2009][research_salvador_myrabo_2009]] [[Salvador et al 2013][research_salvador_myrabo_2013]] [[Santos et al 2020][research_santos_hosder_2020]] [[Sapunkov 1966][research_sapunkov_1966]] [[Sawley and Wüthrich 1995][research_sawley_wuthrich_1995]] [[Sayapin 1966][research_sayapin_1966]] [[Scaggs 1966][research_scaggs_1966]] [[Schaber et al 1991][research_schaber_schwab_1991]] [[Schindel 1991][research_schindel_1991]] [[Schmidt 1988][research_schmidt_1988]] [[Schmidt and Plostins 1983][research_schmidt_plostins_1983]] [[Schueler 1963][research_schueler_1963]] [[Schwartzentruber and Boyd 2013][research_schwartzentruber_boyd_2013]] [[Schwartzentruber et al 2012][research_schwartzentruber_tadmor_2012]] [[Schwelkart and Hallion 1997][research_schwelkart_hallion_1997]] [[Scigliano et al 2020][research_scigliano_desimone_2020]] [[Scott 1968][research_scott_1968]] [[Scuderi et al 1998][research_scuderi_orton_1998]] [[Segal 2010][research_segal_2010_b]] [[Segal and Thakur 2005][research_segal_thakur_2005]] [[Segal et al 1997][research_segal_owens_1997]] [[Segura 2007][research_segura_2007]] [[Serrani and Bolender 2014][research_serrani_bolender_2014]] [[Sethi 2025][research_sethi_2025]] [[Sevigny et al 1972][research_sevigny_heckman_1972]] [[Sforza 1967][research_sforza_1967]] [[Shachar et al 2025][research_shachar_benasher_2025]] [[Shakiba and Serrani 2011][research_shakiba_serrani_2011]] [[Shang 2005][research_shang_2005]] [[Shang* 2009][research_shang_2009]] [[Shen et al 2014][research_shen_yu_2014]] [[Shi et al 2012][research_shi_zhou_2012]] [[Shi et al 2020][research_shi_feng_2020]] [[Shilnikov and Elizarova 2018][research_shilnikov_elizarova_2018]] [[Shock Waves in Bubbly][research_shock_waves]] [[Shorenstein 1971][research_shorenstein_1971]] [[Short 1961][research_short_1961]] [[Shuai et al 2022][research_shuai_daqian_2022]] [[Shuguang et al 2015][research_shuguang_yangwang_2015]] [[Shuping Tan and Zhibin Li 2010][research_shupingtan_zhibinli_2010]] [[Sidharth and Dwivedi 2026][research_sidharth_dwivedi_2026_b]] [[Silva Marques Soares et al 2021][research_silvamarquessoares_paulobatistadearaujo_2021]] [[Simmons et al 1989][research_simmons_nelson_1989]] [[Simons 1975][research_simons_1975]] [[Sims 1963][research_sims_1963]] [[Sims and Hahn 1964][research_sims_hahn_1964]] [[Singh et al 2023][research_singh_prakash_2023]] [[Sippel 2006][research_sippel_2006]] [[Sivells and Payne 1959][research_sivells_payne_1959]] [[Skews 1994][research_skews_1994]] [[Skujins and Cesnik 2010][research_skujins_cesnik_2010]] [[Skujins and Cesnik 2011][research_skujins_cesnik_2011]] [[Smalley et al 1977][research_smalley_wharton_1977]] [[Smarslok 2015][research_smarslok_2015]] [[Smart and Tetlow 2006][research_smart_tetlow_2006]] [[Smiley and Camberos 2024][research_smiley_camberos_2024]] [[Smirnov 2019][research_smirnov_2019]] [[Smits 1988][research_smits_1988]] [[Sobel and Nawaz 1972][research_sobel_nawaz_1972]] [[Sobieczky 1991][research_sobieczky_1991]] [[Sobieczky 2026][research_sobieczky_2026]] [[Song and Choi 2020][research_song_choi_2020]] [[Speyer et al 1980][research_speyer_dannemiller_1980]] [[Spring 1972][research_spring_1972]] [[Srinivas 1992][research_srinivas_1992]] [[Stalker and Morgan 1984][research_stalker_morgan_1984]] [[Starkey and Lewis 2000][research_starkey_lewis_2000]] [[Starkey and Lewis 2003][research_starkey_lewis_2003]] [[Starkey et al 2006][research_starkey_rankins_2006]] [[Stebbins and Loth 2024][research_stebbins_loth_2024]] [[Steinetz, Bruce M. et al 1992][research_steinetzbrucem_mutharasanrajakkannu_1992]] [[Stemmer and Adams][research_stemmer_adams]] [[Stenzel and Urrutia 2014][research_stenzel_urrutia_2014]] [[Sternberg 2010][research_sternberg_2010]] [[Stokes and Lombaerts 2023][research_stokes_lombaerts_2023]] [[Stone 1945][research_stone_1945]] [[Strome 1969][research_strome_1969]] [[Stuckey and Lewis 1999][research_stuckey_lewis_1999]] [[Sturek and Schiff 1981][research_sturek_schiff_1981]] [[Su et al 2024][research_su_zhao_2024]] [[Subsonic and Supersonic Jets 1975][research_subsonic_and_1975]] [[Suchomel et al 2006][research_suchomel_vanwie_2006]] [[Sudalagunta et al 2018][research_sudalagunta_sultan_2018]] [[Sugarno et al 2022][research_sugarno_sriram_2022]] [[Sun and Xin 2014][research_sun_xin_2014]] [[Sun and Zhang 2011][research_sun_zhang_2011]] [[Sun et al 2013][research_sun_li_2013]] [[Sun et al 2020][research_sun_wang_2020_c]] [[Sun et al 2020][research_sun_wang_2020_d]] [[Sun et al 2020][research_sun_wang_2020_e]] [[Sun et al 2023][research_sun_wu_2023]] [[Sun et al 2024][research_sun_ma_2024]] [[Sun et al 2025][research_sun_ran_2025]] [[Sun et al 2026][research_sun_li_2026]] [[Sun et al 2026][research_sun_li_2026_b]] [[Sung et al 2025][research_sung_jo_2025]] [[Supersonic jet excitation using 1994][research_supersonic_jet_1994]] [[Surzhikov 2009][research_surzhikov_2009]] [[Surzhikov 2013][research_surzhikov_2013]] [[Swanson et al 2007][research_swanson_caghlan_2007]] [[Swigart 1962][research_swigart_1962]] [[Tachinina et al 2018][research_tachinina_lysenko_2018]] [[Tahir et al][research_tahir_timofeev]] [[Takahashi et al 2020][research_takahashi_kodera_2020]] [[Tang et al 2005][research_tang_zheng_2005]] [[Tang et al 2020][research_tang_zhai_2020]] [[Tang et al 2021][research_tang_gao_2021]] [[Tang et al 2023][research_tang_hu_2023]] [[Tao et al 2016][research_tao_li_2016]] [[Tchuen and Burtschell 2011][research_tchuen_burtschell_2011]] [[Tchuen et al 2008][research_tchuen_burtschell_2008]] [[Teng et al 2016][research_teng_yang_2016]] [[Thakur and Segal 2003][research_thakur_segal_2003]] [[Thakur and Segal 2004][research_thakur_segal_2004]] [[Thakur and Segal 2006][research_thakur_segal_2006]] [[Thibodeaux 2002][research_thibodeaux_2002]] [[Thirunavukkarasu and Ghosh 2023][research_thirunavukkarasu_ghosh_2023]] [[Thomas 1942][research_thomas_1942]] [[Tian and Fan 2013][research_tian_fan_2013]] [[Tieshan et al 2021][research_tieshan_zhiyao_2021]] [[Tilmann 1998][research_tilmann_1998]] [[Timofeev et al 2008][research_timofeev_tahir_2008]] [[Ting and Libby 1960][research_ting_libby_1960]] [[Tinney and Panickar 2013][research_tinney_panickar_2013]] [[Tiwari et al 2026][research_tiwari_soman_2026]] [[Tong and Steinetz 1991][research_tong_steinetz_1991]] [[Toong 1978][research_toong_1978]] [[Trella and Vaglio-Laurin 1964][research_trella_vagliolaurin_1964]] [[Triantafillou et al 1998][research_triantafillou_schwendeman_1998]] [[Trunin et al 2004][research_trunin_krupnikov_2004]] [[Tsuboi et al 2008][research_tsuboi_matsumoto_2008]] [[Tumin 1996][research_tumin_1996]] [[Turner 1965][research_turner_1965]] [[Ueno et al 2011][research_ueno_imamura_2011]] [[Unnikrishnan and Gaitonde 2021][research_unnikrishnan_gaitonde_2021]] [[Upadhyay et al 2019][research_upadhyay_kumar_2019]] [[US tests hypersonic flying 2011][research_us_tests_2011]] [[Van 1963][research_van_1963]] [[Van Camp and Williams 1974][research_vancamp_williams_1974]] [[van der Heide et al 2026][research_vanderheide_bone_2026]] [[Van Der Kreek][research_vanderkreek]] [[Varner 1976][research_varner_1976]] [[Verhoff and O'Neil 1987][research_verhoff_oneil_1987]] [[Vidal, R. J. 1974][research_vidalrj_1974]] [[Vijayakumar et al 2020][research_vijayakumar_narendar_2020]] [[Viviand 1991][research_viviand_1991]] [[Vogel et al 2009][research_vogel_kelkar_2009]] [[Volkov 2023][research_volkov_2023]] [[von Lavante et al 2000][research_vonlavante_kallenberg_2000]] [[Wada 2026][research_wada_2026]] [[Walchner 1974][research_walchner_1974]] [[Walker 1955][research_walker_1955]] [[Walker and Oberkampf 1991][research_walker_oberkampf_1991]] [[Walters 1984][research_walters_1984]] [[Walters 1992][research_walters_1992]] [[Wan and Chen 2022][research_wan_chen_2022]] [[Wan et al 2012][research_wan_wang_2012]] [[Wang 1998][research_wang_1998]] [[Wang 1998][research_wang_1998_b]] [[Wang 2019][research_wang_2019]] [[Wang and Gao 2013][research_wang_gao_2013]] [[Wang and Prakash 2024][research_wang_prakash_2024]] [[Wang and Wu 2017][research_wang_wu_2017]] [[Wang and Xia 2022][research_wang_xia_2022]] [[Wang and Zhang 1992][research_wang_zhang_1992]] [[Wang and Zhang 2021][research_wang_zhang_2021]] [[Wang et al 1980][research_wang_zakkay_1980]] [[Wang et al 2012][research_wang_sun_2012]] [[Wang et al 2012][research_wang_xu_2012]] [[Wang et al 2012][research_wang_liu_2012]] [[Wang et al 2015][research_wang_wu_2015]] [[Wang et al 2017][research_wang_zhang_2017]] [[Wang et al 2017][research_wang_qin_2017]] [[Wang et al 2017][research_wang_li_2017]] [[Wang et al 2017][research_wang_li_2017_b]] [[Wang et al 2018][research_wang_hou_2018]] [[Wang et al 2018][research_wang_chen_2018]] [[Wang et al 2019][research_wang_hou_2019]] [[Wang et al 2019][research_wang_hou_2019_b]] [[Wang et al 2020][research_wang_xu_2020]] [[Wang et al 2022][research_wang_feng_2022]] [[Wang et al 2023][research_wang_zhang_2023]] [[Wang et al 2025][research_wang_liu_2025_b]] [[Wang et al 2025][research_wang_tang_2025_b]] [[Wang et al 2025][research_wang_li_2025]] [[Wang et al 2026][research_wang_liu_2026_c]] [[Ward and Smart 2026][research_ward_smart_2026]] [[Wartemann et al 2009][research_wartemann_ludeke_2009]] [[Washington and Humphrey 1969][research_washington_humphrey_1969]] [[Wasserman 1952][research_wasserman_1952]] [[Waszkowski and Pisani 2025][research_waszkowski_pisani_2025]] [[Watmuff and Smits 1987][research_watmuff_smits_1987]] [[Weatherill and Zartarian 1958][research_weatherill_zartarian_1958]] [[Weatherston 1969][research_weatherston_1969]] [[Wegener 1977][research_wegener_1977]] [[Wei et al 2012][research_wei_peers_2012]] [[Wei et al 2016][research_wei_wang_2016]] [[Wei et al 2019][research_wei_hu_2019]] [[Weidong et al 2015][research_weidong_xianlin_2015]] [[Weiland 2019][research_weiland_2019]] [[Weilmuenster et al 1995][research_weilmuenster_gnoffo_1995]] [[Weilmuenster et al 1996][research_weilmuenster_gnoffo_1996]] [[Weinacht 2014][research_weinacht_2014]] [[Wenbiao et al 2014][research_wenbiao_dong_2014]] [[Wenfeng et al 2017][research_wenfeng_peng_2017]] [[Wenkai et al 2017][research_wenkai_zhongxi_2017]] [[Wenkai et al 2017][research_wenkai_hou_2017]] [[Wenkai et al 2017][research_wenkai_hou_2017_b]] [[Wepler et al 2001][research_wepler_huhn_2001]] [[West 2005][research_west_2005]] [[Wexler and Idan 2026][research_wexler_idan_2026]] [[Weyl 1998][research_weyl_1998]] [[White et al 1961][research_white_richardp_1961]] [[Wiese et al 2013][research_wiese_annaswamy_2013]] [[Wilks 2006][research_wilks_2006]] [[Williams 1965][research_williams_1965]] [[Williams 2021][research_williams_2021]] [[Williams and Lewis 1975][research_williams_lewis_1975]] [[Williams et al 2024][research_williams_bartkowicz_2024]] [[Wilson 1966][research_wilson_1966]] [[Wilson et al 2009][research_wilson_agarwal_2009]] [[Wingfield, III 2001][research_wingfieldiii_2001]] [[Wolfe 1964][research_wolfe_1964]] [[Wollrab 1966][research_wollrab_1966]] [[Wright 2022][research_wright_2022]] [[Wu and Wang 2015][research_wu_wang_2015]] [[Wu and Yu 2018][research_wu_yu_2018]] [[Wu et al 2015][research_wu_liu_2015]] [[Wu et al 2015][research_wu_wang_2015_b]] [[Wu et al 2020][research_wu_lin_2020]] [[Wu Liaoni and Wang Mengmeng 2012][research_wuliaoni_wangmengmeng_2012]] [[Wurster and Marrone 1962][research_wurster_marrone_1962]] [[Wächter and Sachs 2006][research_wachter_sachs_2006]] [[X-43 hypersonic vehicle technology development][research_x43_technology]] [[Xian Lin Huang and Dong Ming Ge 2010][research_xianlinhuang_dongmingge_2010]] [[Xie et al 2021][research_xie_zhuang_2021]] [[Xin and Zhang 2011][research_xin_zhang_2011]] [[Xin Wang and Shijie Sun 2010][research_xinwang_shijiesun_2010]] [[Xin Wang et al 2008][research_xinwang_dongzhufeng_2008]] [[Xiong Luo et al 2008][research_xiongluo_zengqisun_2008]] [[Xu 2015][research_xu_2015]] [[Xu and Cai 2011][research_xu_cai_2011]] [[Xu and Mao][research_xu_mao]] [[Xu and Zhang 2015][research_xu_zhang_2015]] [[Xu et al 1996][research_xu_kim_1996]] [[Xu et al 2004][research_xu_mirmirani_2004]] [[Xu et al 2012][research_xu_wang_2012]] [[Xu et al 2012][research_xu_sun_2012]] [[Xu et al 2017][research_xu_yu_2017]] [[Xue and Haibin 2017][research_xue_haibin_2017]] [[Xue et al 2023][research_xue_huang_2023]] [[Ya-Long et al 2014][research_yalong_guangbin_2014]] [[Yahalom 1971][research_yahalom_1971]] [[Yahui et al 2021][research_yahui_yitao_2021]] [[Yamamoto and Kano 1996][research_yamamoto_kano_1996]] [[Yan 2014][research_yan_2014]] [[Yan and Fu 2026][research_yan_fu_2026]] [[Yan and Wang 2012][research_yan_wang_2012]] [[Yan Binbin et al 2009][research_yanbinbin_lucunkan_2009]] [[Yan et al 2008][research_yan_pan_2008]] [[Yan et al 2017][research_yan_fan_2017]] [[Yang and Li 2023][research_yang_li_2023]] [[Yang and Qi 2016][research_yang_qi_2016]] [[Yang and Wang 2021][research_yang_wang_2021]] [[Yang et al 2013][research_yang_yuan_2013]] [[Yang et al 2014][research_yang_yu_2014]] [[Yang et al 2017][research_yang_li_2017]] [[Yang et al 2026][research_yang_cai_2026]] [[Yang et al 2026][research_yang_cheng_2026]] [[Yao et al 2009][research_yao_bao_2009]] [[Yao et al 2017][research_yao_chaoyang_2017]] [[Yao et al 2023][research_yao_hu_2023]] [[Yao et al 2025][research_yao_wu_2025]] [[Yaosheng 2018][research_yaosheng_2018]] [[Yeneriz et al 1989][research_yeneriz_davis_1989]] [[Yeneriz et al 1991][research_yeneriz_davis_1991]] [[Yin et al 2017][research_yin_qin_2017]] [[Ying et al 2018][research_ying_fang_2018]] [[Young 1966][research_young_1966]] [[Young and Goldstein 1999][research_young_goldstein_1999]] [[Young et al 2006][research_young_kokan_2006]] [[Youssef et al 2008][research_youssef_reiman_2008]] [[Youssef et al 2009][research_youssef_reiman_2009]] [[Yu 2026][research_yu_2026]] [[Yu and Schadow 1994][research_yu_schadow_1994]] [[Yu et al 2014][research_yu_zhang_2014]] [[Yu et al 2021][research_yu_ao_2021]] [[Yu et al 2022][research_yu_ni_2022]] [[Yuan et al 2026][research_yuan_gao_2026]] [[Yulian and Bin 2014][research_yulian_bin_2014]] [[Zartarian 1956][research_zartarian_1956]] [[Zartarian and Hsu 1955][research_zartarian_hsu_1955]] [[Zeng et al 2021][research_zeng_zhuang_2021]] [[Zerilli and Armstrong 1992][research_zerilli_armstrong_1992]] [[Zhai et al 2016][research_zhai_qi_2016]] [[Zhai et al 2018][research_zhai_yang_2018]] [[Zhang 2020][research_zhang_2020_e]] [[Zhang 2020][research_zhang_2020_f]] [[Zhang 2020][research_zhang_2020_g]] [[Zhang and Chen 2011][research_zhang_chen_2011]] [[Zhang and Tang 2012][research_zhang_tang_2012]] [[Zhang and Tang 2015][research_zhang_tang_2015]] [[Zhang et al 2012][research_zhang_xu_2012]] [[Zhang et al 2016][research_zhang_li_2016]] [[Zhang et al 2017][research_zhang_liu_2017]] [[Zhang et al 2017][research_zhang_xia_2017]] [[Zhang et al 2018][research_zhang_yu_2018]] [[Zhang et al 2019][research_zhang_wang_2019]] [[Zhang et al 2019][research_zhang_wang_2019_b]] [[Zhang et al 2022][research_zhang_sun_2022]] [[Zhang et al 2022][research_zhang_xiong_2022]] [[Zhang et al 2022][research_zhang_xiong_2022_b]] [[Zhang et al 2022][research_zhang_huang_2022]] [[Zhang et al 2022][research_zhang_zhang_2022_b]] [[Zhang et al 2023][research_zhang_ju_2023]] [[Zhang et al 2023][research_zhang_chen_2023]] [[Zhang et al 2026][research_zhang_chen_2026_c]] [[Zhang et al 2026][research_zhang_liao_2026]] [[Zhang Zhikai et al 2015][research_zhangzhikai_duanguangren_2015]] [[Zhao 2021][research_zhao_2021]] [[Zhao 2021][research_zhao_2021_b]] [[Zhao 2023][research_zhao_2023_b]] [[Zhao et al 2018][research_zhao_cai_2018]] [[Zhao et al 2019][research_zhao_sun_2019]] [[Zhao et al 2019][research_zhao_chen_2019]] [[Zhapbasbaev and Makashev 2003][research_zhapbasbaev_makashev_2003]] [[Zheng and Bray 1997][research_zheng_bray_1997]] [[Zheng et al 2025][research_zheng_zhao_2025]] [[Zhengdong et al 2013][research_zhengdong_man_2013]] [[Zhi and Yang 2015][research_zhi_yang_2015]] [[Zhi et al 2015][research_zhi_liang_2015]] [[Zhikharev 1993][research_zhikharev_1993]] [[Zhong 2009][research_zhong_2009]] [[Zhong and Furumoto 1998][research_zhong_furumoto_1998]] [[Zhong et al 2001][research_zhong_whang_2001]] [[Zhongjie Meng et al 2008][research_zhongjiemeng_panfenghuang_2008]] [[Zhongjie Meng et al 2010][research_zhongjiemeng_jianzhongdong_2010]] [[Zhou 2018][research_zhou_2018]] [[Zhou 2023][research_zhou_2023]] [[Zhou et al 2016][research_zhou_gao_2016]] [[Zhou et al 2017][research_zhou_lu_2017]] [[Zhou et al 2019][research_zhou_wang_2019]] [[Zhou et al 2020][research_zhou_liu_2020]] [[Zhou et al 2026][research_zhou_wang_2026]] [[Zhu and Liu 2015][research_zhu_liu_2015_b]] [[Zhu and Shen 2015][research_zhu_shen_2015]] [[Zhu et al 2024][research_zhu_gao_2024]] [[Zhu et al 2025][research_zhu_chen_2025]] [[Zivanovic 1963][research_zivanovic_1963]] [[Zweber et al 2002][research_zweber_kabis_2002]]

### Inlets, starting and the unstart that ended a flight

**The second flight is in this cluster.** Inlet starting, contraction ratio limits, the Kantrowitz criterion, mass capture, buzz and unstart. **An unstart is the inlet ceasing to swallow the flow it was designed to swallow**, and it happens fast, and the engine behind it stops being an engine.

**476 records.** [[Abedi et al 2020][research_abedi_askari_2020]] [[Adams, Jr. et al 1984][research_adamsjr_martindale_1984]] [[Agarwal and Deb 2001][research_agarwal_deb_2001]] [[Agnone 1987][research_agnone_1987]] [[Aiello 1977][research_aiello_1977]] [[Ala and Ye 2024][research_ala_ye_2024]] [[Albertson, Cindy w. et al 2006][research_albertsoncindyw_emamisaied_2006]] [[Alhussan and Garris 2005][research_alhussan_garris_2005]] [[Ali et al 2000][research_ali_fujiwara_2000]] [[Amemiya and Toriyama 2018][research_amemiya_toriyama_2018]] [[An Ultrasonic Turbine Inlet 1974][research_an_ultrasonic_1974]] [[Ananthapadmanaban and Murganandam 2016][research_ananthapadmanaban_murganandam_2016]] [[Anderson 2014][research_anderson_2014]] [[Aubrey and Speer 1983][research_aubrey_speer_1983]] [[Automatic Detection and Suppression 1974][research_automatic_detection_1974]] [[Babinsky 2014][research_babinsky_2014]] [[Bachchan and Hillier 2004][research_bachchan_hillier_2004]] [[Bahuguna et al 2023][research_bahuguna_kolluru_2023]] [[Balent and Kutschenreuter, Jr. 1964][research_balent_kutschenreuterjr_1964]] [[Ball et al 1981][research_ball_syberg_1981]] [[Bao et al 2010][research_bao_li_2010]] [[Barber et al 2006][research_barber_heitt_2006]] [[Batill and Hoffman 1984][research_batill_hoffman_1984]] [[Baye-Wallace and Krouse 2022][research_bayewallace_krouse_2022]] [[Bennett and Edwards 1990][research_bennett_edwards_1990]] [[Benson and Maslowe 1965][research_benson_maslowe_1965]] [[Benson and Mcrae 1993][research_benson_mcrae_1993]] [[Benson et al 2009][research_benson_liou_2009]] [[Berens and Bissinger 1996][research_berens_bissinger_1996]] [[Berens and Bissinger 1998][research_berens_bissinger_1998]] [[Berger et al 2019][research_berger_gourdain_2019]] [[Berkner 1990][research_berkner_1990]] [[Bissinger et al 1998][research_bissinger_blagoveshchensky_1998]] [[Blaine et al 2005][research_blaine_keeling_2005]] [[Bogue et al 1995][research_bogue_bagley_1995]] [[Bolender et al 2009][research_bolender_wilkin_2009]] [[Boon and Hillier 2006][research_boon_hillier_2006]] [[Boon and Hillier 2006][research_boon_hillier_2006_b]] [[Borovoy et al 2015][research_borovoy_egorov_2015]] [[Brenneis and Wanie 1991][research_brenneis_wanie_1991]] [[Bretherton][research_bretherton]] [[Brocanelli et al 2012][research_brocanelli_gunbatar_2012]] [[Brophy and Hawk 1990][research_brophy_hawk_1990]] [[Brutsche and McFall 2015][research_brutsche_mcfall_2015]] [[Bullen et al 1988][research_bullen_cheeseman_1988]] [[Burr 1968][research_burr_1968]] [[Burris 1966][research_burris_1966]] [[Burrows et al 2017][research_burrows_vukasinovic_2017]] [[Buzz Suppression of Supersonic 2005][research_buzz_suppression_2005]] [[Calogeras 1969][research_calogeras_1969]] [[Cao et al 2026][research_cao_zhang_2026]] [[Caraballo et al 2009][research_caraballo_webb_2009]] [[Carbajosa et al 2025][research_carbajosa_sanzandres_2025]] [[Carbajosa et al 2026][research_carbajosa_sanzandres_2026]] [[Castner et al 2018][research_castner_simerly_2018]] [[Cavanaugh and Narayanaswamy 2024][research_cavanaugh_narayanaswamy_2024]] [[Caylor and Batill 1984][research_caylor_batill_1984]] [[Chang et al 2008][research_chang_yu_2008]] [[Chang et al 2008][research_chang_yu_2008_b]] [[Chang et al 2009][research_chang_yu_2009]] [[Chang et al 2010][research_chang_fan_2010]] [[Chang et al 2011][research_chang_hu_2011]] [[Chang et al 2012][research_chang_wang_2012]] [[Chang et al 2014][research_chang_wang_2014]] [[Chang et al 2017][research_chang_li_2017]] [[Chaouat 2017][research_chaouat_2017]] [[Cheadle and DiZinno 2026][research_cheadle_dizinno_2026]] [[Chen and Tan 2019][research_chen_tan_2019]] [[Chen et al 2018][research_chen_tan_2018]] [[Chen et al 2019][research_chen_tan_2019_b]] [[Chen et al 2024][research_chen_chen_2024]] [[Chen et al 2025][research_chen_martinez_2025]] [[Chien 1977][research_chien_1977]] [[Chima 2011][research_chima_2011]] [[Choe and Kim 2016][research_choe_kim_2016]] [[Choe et al 2020][research_choe_kim_2020]] [[Chun and Burr 1969][research_chun_burr_1969]] [[Coats 1981][research_coats_1981]] [[Cockrell, Jr. and Huebner 1991][research_cockrelljr_huebner_1991]] [[Control system design using 1976][research_control_system_1976]] [[Cousin 1967][research_cousin_1967]] [[Cox et al 1995][research_cox_lewis_1995]] [[Cui et al 2011][research_cui_lv_2011]] [[Daliri et al 2018][research_daliri_farahani_2018]] [[Dalle et al 2015][research_dalle_driscoll_2015]] [[DePalma 1976][research_depalma_1976]] [[Di Febo and Pasquale 2016][research_difebo_pasquale_2016]] [[Ding et al 2015][research_ding_liu_2015]] [[Ding et al 2018][research_ding_liu_2018]] [[Ding et al 2021][research_ding_liu_2021]] [[Do et al 2010][research_do_im_2010]] [[Do et al 2011][research_do_im_2011]] [[Do et al 2011][research_do_im_2011_b]] [[Do et al 2011][research_do_im_2011_d]] [[Do et al 2024][research_do_nguyen_2024]] [[Domack 1991][research_domack_1991]] [[Duffy 1968][research_duffy_1968]] [[Duffy and Shattuck 1975][research_duffy_shattuck_1975]] [[Duffy and Shattuck 1975][research_duffy_shattuck_1975_b]] [[Dutczak 2006][research_dutczak_2006]] [[Effect of Inlet Velocity 2016][research_effect_of_2016]] [[Effects of Feeding Mode 2021][research_effects_of_2021]] [[Egusquiza and Virto 1982][research_egusquiza_virto_1982]] [[Elgar and Raubenheimer 2011][research_elgar_raubenheimer_2011]] [[Ertunç and Durst 2008][research_ertunc_durst_2008]] [[Eves and Valasek 2024][research_eves_valasek_2024]] [[Experimental Study of the 2022][research_experimental_study_2022]] [[Famularo et al 2018][research_famularo_whitney_2018]] [[Fan and Chang 2009][research_fan_chang_2009]] [[Fan et al 2010][research_fan_chang_2010]] [[Farahani et al 2019][research_farahani_daliri_2019]] [[Ferrero 2020][research_ferrero_2020]] [[Forner and Manter 1982][research_forner_manter_1982]] [[Freed et al 2001][research_freed_dedecker_2001]] [[Frey 2014][research_frey_2014]] [[Frey et al 2025][research_frey_jamme_2025]] [[Fu et al 2021][research_fu_bose_2021]] [[Fu et al 2022][research_fu_qu_2022]] [[Fu et al 2026][research_fu_gong_2026]] [[Fujimatsu et al 2019][research_fujimatsu_kito_2019]] [[Fujio and Taguchi 2026][research_fujio_taguchi_2026]] [[Fukuda et al 1975][research_fukuda_reshotko_1975]] [[Fukutani and Watanabe 1986][research_fukutani_watanabe_1986]] [[G et al 2017][research_g_kaushik_2017]] [[G et al 2017][research_g_kaushik_2017_b]] [[G.K. Suryanarayana et al 2026][research_gksuryanarayana_dbsingh_2026]] [[Gallo et al 1966][research_gallo_gnos_1966]] [[Gao et al 2015][research_gao_li_2015]] [[Gao et al 2024][research_gao_zhang_2024]] [[Garavello et al 2024][research_garavello_kneish_2024]] [[Gas Temperature-Density GTD Sensor 1974][research_gas_temperature_density_1974]] [[Gilinsky et al 2003][research_gilinsky_gonor_2003]] [[Glenning and Bond 1962][research_glenning_bond_1962]] [[Goldfeld 2019][research_goldfeld_2019]] [[Goldfeld and Nestoulia 2003][research_goldfeld_nestoulia_2003]] [[Goldfeld et al 2019][research_goldfeld_korotaeva_2019]] [[Gollan et al 2011][research_gollan_gollan_2011]] [[Gong et al 2024][research_gong_long_2024]] [[Gonzalez 1996][research_gonzalez_1996]] [[Goonko et al 2003][research_goonko_latypov_2003]] [[Grainger et al 2014][research_grainger_brieschenk_2014]] [[Grolmes 1968][research_grolmes_1968]] [[Gruhn and Gülhan 2011][research_gruhn_gulhan_2011]] [[Gu et al 2009][research_gu_xu_2009]] [[Gu et al 2010][research_gu_xu_2010]] [[Guan and Yarng 1987][research_guan_yarng_1987]] [[Guo et al 2017][research_guo_gao_2017]] [[Guza and Feddersen 2015][research_guza_feddersen_2015]] [[Haas and Karanian 1980][research_haas_karanian_1980]] [[Halas 1979][research_halas_1979]] [[Hamed 1990][research_hamed_1990]] [[Hanafi][research_hanafi]] [[Hao et al 2016][research_hao_chang_2016_b]] [[Hardie and O'Byrne 2025][research_hardie_obyrne_2025]] [[Hawkins and Marquart 1995][research_hawkins_marquart_1995]] [[He 2015][research_he_2015]] [[Heberling 2020][research_heberling_2020]] [[Hedges et al 1996][research_hedges_lewis_1996]] [[Heinrich 1954][research_heinrich_1954]] [[Henderson 1999][research_henderson_1999]] [[Henson 2017][research_henson_2017]] [[Herges et al 2012][research_herges_dutton_2012]] [[Herrmann and Gülhan 2015][research_herrmann_gulhan_2015]] [[Herrmann et al 2013][research_herrmann_siebe_2013]] [[Highlights from a Mach 4 experimental demonstration of inlet mode transition for turbine-based combined cycle hypersonic propulsion][research_inlet_mode_transition]] [[Hoang et al 2024][research_hoang_nguyen_2024]] [[Holdo̸ and de With 2004][research_holdo_dewith_2004]] [[Hong and Kim 2011][research_hong_kim_2011]] [[Hu et al 2013][research_hu_chang_2013]] [[Huang and Murray 2003][research_huang_murray_2003]] [[Huang et al 2011][research_huang_zhou_2011]] [[Huang et al 2018][research_huang_zuo_2018]] [[Huang et al 2025][research_huang_lv_2025]] [[Hube 1968][research_hube_1968]] [[Hughes 2000][research_hughes_2000]] [[Hughes and Pizzo 2003][research_hughes_pizzo_2003]] [[Hutchins et al 2012][research_hutchins_akella_2012]] [[Hutchins et al 2014][research_hutchins_akella_2014]] [[Iannelli 2007][research_iannelli_2007]] [[Influence of Plasma on 2024][research_influence_of_2024]] [[Ingenito et al 2009][research_ingenito_bruno_2009_b]] [[Inger 1994][research_inger_1994]] [[Instrumentation for In-Flight Determination 1974][research_instrumentation_for_1974_b]] [[Jacocks and Kneile 1975][research_jacocks_kneile_1975]] [[Jamie 2015][research_jamie_2015]] [[Jee][research_jee]] [[Jiao et al 2015][research_jiao_chang_2015]] [[Jiao et al 2016][research_jiao_chang_2016]] [[Jiao et al 2017][research_jiao_chang_2017]] [[Jin and Yao 2023][research_jin_yao_2023]] [[Jin et al 2022][research_jin_sun_2022]] [[Jin et al 2023][research_jin_tan_2023]] [[Jin et al 2023][research_jin_zhang_2023]] [[Jin et al 2026][research_jin_zhang_2026]] [[Johnson and Narayanaswamy 2024][research_johnson_narayanaswamy_2024]] [[Johnson and Narayanaswamy 2026][research_johnson_narayanaswamy_2026]] [[Johnston and Powars 1969][research_johnston_powars_1969]] [[Kai-li and Kun-yuan 2010][research_kaili_kunyuan_2010]] [[Kaltreider 1951][research_kaltreider_1951]] [[Kantrowitz 2002][research_kantrowitz_2002]] [[Kantrowitz, Arthur on 1984 2025][research_kantrowitz_arthur_2025]] [[Kantrowitz, Arthur on 2006 2025][research_kantrowitz_arthur_2025_b]] [[karciauskas and Peters 2024][research_karciauskas_peters_2024]] [[Kaushik 2023][research_kaushik_2023]] [[Khobragade and Kumar 2022][research_khobragade_kumar_2022]] [[Kim and Lee 2022][research_kim_lee_2022]] [[Kim and Park 2026][research_kim_park_2026]] [[Klepper et al 2017][research_klepper_sirbaugh_2017]] [[Kline et al 2014][research_kline_palacios_2014]] [[Kline et al 2014][research_kline_palacios_2014_b]] [[Kodama and Kogiso 2017][research_kodama_kogiso_2017]] [[Kohl 1993][research_kohl_1993]] [[Kojima et al 2015][research_kojima_taguchi_2015]] [[Kontogiannis et al 2016][research_kontogiannis_taylor_2016]] [[Kumar 2022][research_kumar_2022]] [[Kumar and Anderson 1986][research_kumar_anderson_1986]] [[Kutschenreuter et al 1966][research_kutschenreuter_paulh_1966]] [[Kwak and Lee 2011][research_kwak_lee_2011]] [[Kwak and Lee 2013][research_kwak_lee_2013]] [[Kwak and Lee 2013][research_kwak_lee_2013_b]] [[Kwak et al 2013][research_kwak_lee_2013_c]] [[L. et al 2012][research_l_r_2012]] [[Lee and Jeung 2009][research_lee_jeung_2009]] [[Lehtinen and Zeller 1972][research_lehtinen_zeller_1972]] [[Lei and Zha 2022][research_lei_zha_2022]] [[Lei and Zha 2022][research_lei_zha_2022_b]] [[Lei et al 2012][research_lei_kunyuan_2012]] [[Leonov et al 2007][research_leonov_yarantsev_2007]] [[Leonov et al 2012][research_leonov_yarantsev_2012]] [[Li et al 1999][research_li_freed_1999]] [[Li et al 2014][research_li_an_2014]] [[Li et al 2015][research_li_han_2015]] [[Li et al 2022][research_li_chen_2022]] [[Li et al 2023][research_li_ren_2023]] [[Li et al 2024][research_li_huang_2024]] [[Li et al 2024][research_li_wang_2024]] [[Li et al 2024][research_li_sun_2024_b]] [[Li et al 2025][research_li_wu_2025]] [[Lian et al 2025][research_lian_xiong_2025]] [[Libby et al 1963][research_libby_fox_1963]] [[Limage 1978][research_limage_1978]] [[Liou et al 2010][research_liou_benson_2010]] [[Liu et al 2019][research_liu_fan_2019]] [[Liu et al 2022][research_liu_chen_2022]] [[Liu et al 2025][research_liu_zhu_2025]] [[Loth et al 2016][research_loth_candon_2016]] [[Luján et al 2016][research_lujan_climent_2016]] [[Luo and Wang 2015][research_luo_wang_2015]] [[Luo et al 2020][research_luo_wei_2020]] [[Luo et al 2024][research_luo_tao_2024]] [[MacMahan and Reniers 2012][research_macmahan_reniers_2012]] [[Manimaran 2016][research_manimaran_2016]] [[Mann and Garner 1977][research_mann_garner_1977]] [[Manoj Prabakar and Muruganandam 2019][research_manojprabakar_muruganandam_2019]] [[Marlina 2018][research_marlina_2018]] [[Marquart 1991][research_marquart_1991]] [[Marvin 1968][research_marvin_1968]] [[Matthews and Jones 2005][research_matthews_jones_2005]] [[Mayer and Paynter 1994][research_mayer_paynter_1994]] [[Mayer and Paynter 1995][research_mayer_paynter_1995]] [[McClure and Sirbaugh 1991][research_mcclure_sirbaugh_1991]] [[McRae and Neaves 1998][research_mcrae_neaves_1998]] [[Medina et al 2021][research_medina_patel_2021]] [[Meng et al 2024][research_meng_jin_2024]] [[Miller 1965][research_miller_1965]] [[Miller and Smith 2003][research_miller_smith_2003]] [[Min et al 2024][research_min_hong_2024]] [[Min et al 2026][research_min_sun_2026]] [[Mirhosseini et al 2025][research_mirhosseini_najafi_2025]] [[Moin and Lele 1998][research_moin_lele_1998]] [[Mondal and Jagtap 2026][research_mondal_jagtap_2026]] [[Moss et al 2026][research_moss_vasile_2026]] [[Mrozinski and Hayes 1999][research_mrozinski_hayes_1999]] [[Mu et al 2022][research_mu_wang_2022]] [[Murzionak][research_murzionak]] [[Musa et al 2022][research_musa_huang_2022]] [[Myrabo and Nagamatsu 1991][research_myrabo_nagamatsu_1991]] [[Mysko et al 1993][research_mysko_chyu_1993]] [[Nagao et al 2019][research_nagao_yoshida_2019]] [[Nair et al 2003][research_nair_kumar_2003]] [[Nair et al 2005][research_nair_kumar_2005]] [[NamKoung et al 2012][research_namkoung_hong_2012]] [[Neaves and McRae 1995][research_neaves_mcrae_1995]] [[Neaves et al 2001][research_neaves_mcrae_2001]] [[Newberry et al 1988][research_newberry_dresser_1988]] [[Nicolae Tudosie 2018][research_nicolaetudosie_2018]] [[Ning][research_ning]] [[Noftz and Jewell 2025][research_noftz_jewell_2025]] [[Numerical Research of Three-Dimensional 2008][research_numerical_research_2008]] [[O'Rorke and Cuppoletti 2024][research_ororke_cuppoletti_2024]] [[Obikane 1984][research_obikane_1984]] [[Obituary of Arthur Kantrowitz 2008][research_obituary_of_2008]] [[Oka et al 2015][research_oka_hidema_2015]] [[Ortwerth and Goldman 1996][research_ortwerth_goldman_1996]] [[Pan et al 2009][research_pan_tian_2009]] [[Paynter 1994][research_paynter_1994]] [[Paynter and Chen 1983][research_paynter_chen_1983]] [[Peng et al 2024][research_peng_xu_2024]] [[Pollock and Brutsche 2015][research_pollock_brutsche_2015]] [[Pollock and Wild 2024][research_pollock_wild_2024]] [[Pruitt and Bates 1992][research_pruitt_bates_1992]] [[Qifan et al 2014][research_qifan_huijun_2014]] [[Qin et al 2026][research_qin_huang_2026]] [[Raghuram and Ramesh 2021][research_raghuram_ramesh_2021]] [[Ramaswami et al 2019][research_ramaswami_velmurugan_2019]] [[Ramprakash and Muruganandam 2016][research_ramprakash_muruganandam_2016]] [[Ranard and Davison 1961][research_ranard_davison_1961]] [[Ratchford et al 2025][research_ratchford_redding_2025]] [[Raubenheimer and Elgar 2012][research_raubenheimer_elgar_2012]] [[Reardon et al 2021][research_reardon_schetz_2021]] [[Reddy et al 1989][research_reddy_smith_1989]] [[Review of Inlet/Airframe Integration 1986][research_review_of_1986]] [[Rice and Heidelberg 1980][research_rice_heidelberg_1980]] [[Rizzetta 1991][research_rizzetta_1991]] [[Sabean and Lewis 1999][research_sabean_lewis_1999]] [[Saheby et al 2015][research_saheby_huang_2015]] [[Samimy et al 2011][research_samimy_webb_2011]] [[Sanders, Bobby W. and Weir, Lois J. 1999][research_sandersbobbyw_weirloisj_1999]] [[Sanders, Bobby W. and Weir, Lois J. 2008][research_sandersbobbyw_weirloisj_2008]] [[Sarosh et al 2012][research_sarosh_yunfeng_2012]] [[Schram and Narayanaswamy 2026][research_schram_narayanaswamy_2026]] [[Schram et al 2025][research_schram_stramecky_2025]] [[Schulte-Roedding and Olivier 1998][research_schulteroedding_olivier_1998]] [[Scribben and Withrow 2006][research_scribben_withrow_2006]] [[Seabergh et al 2001][research_seabergh_king_2001]] [[Sedlock 1985][research_sedlock_1985]] [[Seebaugh, W. R. 1973][research_seebaughwr_1973]] [[Self-starting Simulation of a 2020][research_self_starting_simulation_2020]] [[Sepahi-Younsi 2025][research_sepahiyounsi_2025]] [[Sepahi-Younsi and Esmaeili 2023][research_sepahiyounsi_esmaeili_2023]] [[Shahrokhi and Davis, Jr 1995][research_shahrokhi_davisjr_1995]] [[Shang 2008][research_shang_2008_b]] [[Shang and Chang 2007][research_shang_chang_2007]] [[Shang et al 2006][research_shang_menart_2006]] [[Shang et al 2007][research_shang_chang_2007_b]] [[Shi et al 2010][research_shi_chang_2010]] [[Shimura et al 1996][research_shimura_sakuranaka_1996]] [[Shope 1975][research_shope_1975]] [[Shovlin 1978][research_shovlin_1978]] [[Shucheng and Xijun 1994][research_shucheng_xijun_1994]] [[Singh and Gahlot 2023][research_singh_gahlot_2023]] [[Slater 2016][research_slater_2016]] [[Slater and Saunders 2009][research_slater_saunders_2009]] [[Slater, John W. and Gruber, Christopher R. 2005][research_slaterjohnw_gruberchristopherr_2005]] [[Smart 1999][research_smart_1999]] [[Smeltzer and Sorensen 1972][research_smeltzer_sorensen_1972]] [[Smith et al 2007][research_smith_scribben_2007]] [[Snyder et al 1999][research_snyder_vilendrer_1999]] [[Soltani et al 2011][research_soltani_farahani_2011]] [[Sorensen and Bencze 1973][research_sorensen_bencze_1973]] [[Speer et al 1982][research_speer_aubrey_1982]] [[Srinivasan and Newman 2013][research_srinivasan_newman_2013]] [[Stabe et al 1984][research_stabe_whitney_1984]] [[Street][research_street]] [[Sun and Zhang 2016][research_sun_zhang_2016]] [[Sun et al 2009][research_sun_zhang_2009]] [[Sun et al 2017][research_sun_wang_2017]] [[sun et al 2026][research_sun_yu_2026]] [[Surber 1975][research_surber_1975]] [[Surber and Robinson 1983][research_surber_robinson_1983]] [[Surber and Sedlock 1978][research_surber_sedlock_1978]] [[Syberg et al 1980][research_syberg_koncsek_1980]] [[System for Evaluation of 1974][research_system_for_1974]] [[Tabanli and Yuceil 2018][research_tabanli_yuceil_2018]] [[Taghi-Abad et al 2026][research_taghiabad_esfandabadi_2026]] [[Tahir 2021][research_tahir_2021]] [[Takasaki et al 1998][research_takasaki_fujimoto_1998]] [[Takashima, N. and Kothari, A. P. 1998][research_takashiman_kothariap_1998]] [[Tan et al 2009][research_tan_sun_2009]] [[Tan et al 2011][research_tan_li_2011]] [[Tang et al 2023][research_tang_xiong_2023]] [[Tang et al 2024][research_tang_xiong_2024]] [[Tang et al 2025][research_tang_zhang_2025]] [[Tang et al 2025][research_tang_cai_2025]] [[Tang et al 2025][research_tang_cai_2025_b]] [[Tang et al 2026][research_tang_fan_2026]] [[Tao et al 2008][research_tao_daren_2008_b]] [[Tao et al 2009][research_tao_daren_2009]] [[Theocaris and Koroneos 1963][research_theocaris_koroneos_1963]] [[Timofeev et al 2001][research_timofeev_voinovich_2001]] [[Tong et al 2023][research_tong_yue_2023]] [[Trainini and Cabrera Fischer 2026][research_trainini_cabrerafischer_2026]] [[Trapier et al][research_trapier_deck]] [[Trapier et al 2006][research_trapier_duveau_2006]] [[Trapier et al 2007][research_trapier_deck_2007]] [[Trapier et al 2007][research_trapier_deck_2007_b]] [[Trapier et al 2008][research_trapier_deck_2008]] [[Trefny 2020][research_trefny_2020]] [[Tudosie 2017][research_tudosie_2017]] [[Tudosie 2017][research_tudosie_2017_b]] [[Tudosie 2018][research_tudosie_2018]] [[Tudosie 2022][research_tudosie_2022]] [[Tudosie and Prisacariu 2022][research_tudosie_prisacariu_2022]] [[Tudosie and Păunescu 2017][research_tudosie_paunescu_2017]] [[Tudosie et al 2019][research_tudosie_dumitru_2019]] [[Türkkahraman et al 2024][research_turkkahraman_ozcan_2024]] [[Utomo and Bura 2019][research_utomo_bura_2019]] [[V and Rao 2023][research_v_rao_2023]] [[Vaca-Rios and Cerón-Muñoz 2025][research_vacarios_ceronmunoz_2025]] [[van Keuk et al 1998][research_vankeuk_ballmann_1998]] [[Van Wie and Molder 1992][research_vanwie_molder_1992]] [[Wagner et al 2007][research_wagner_valdivia_2007]] [[Wainwright 1962][research_wainwright_1962]] [[Wang and Cai 2016][research_wang_cai_2016]] [[Wang and Guo 2013][research_wang_guo_2013]] [[Wang et al 2011][research_wang_xie_2011]] [[Wang et al 2014][research_wang_wang_2014]] [[Wang et al 2019][research_wang_xue_2019]] [[Wang et al 2020][research_wang_li_2020]] [[Wang et al 2022][research_wang_fan_2022]] [[Wang et al 2022][research_wang_zhao_2022]] [[Wang et al 2023][research_wang_fan_2023]] [[Wang et al 2023][research_wang_zhao_2023]] [[Wang et al 2023][research_wang_wang_2023_b]] [[Wang et al 2025][research_wang_zhao_2025]] [[Wang et al 2026][research_wang_zhang_2026]] [[Wang et al 2026][research_wang_rajan_2026]] [[Wang et al 2026][research_wang_huang_2026]] [[Weinberg 1952][research_weinberg_1952]] [[West and Bynum 2024][research_west_bynum_2024]] [[White and Rhie 1988][research_white_rhie_1988]] [[White and Rhie 1992][research_white_rhie_1992]] [[Woodward et al 1983][research_woodward_glaser_1983]] [[Wu and He 2022][research_wu_he_2022]] [[Xiao and Yang 2025][research_xiao_yang_2025]] [[Xiao et al 2006][research_xiao_liu_2006]] [[Xiao et al 2008][research_xiao_yue_2008]] [[Xie et al 2026][research_xie_zeng_2026]] [[Xiong et al 2019][research_xiong_bai_2019]] [[Xu et al 2019][research_xu_wang_2019]] [[Xu et al 2022][research_xu_wang_2022]] [[Xu et al 2022][research_xu_wang_2022_b]] [[Yamamoto et al 2020][research_yamamoto_kojima_2020]] [[Yan 2013][research_yan_2013]] [[Yang and Xiao 2026][research_yang_xiao_2026]] [[Yang et al 2024][research_yang_xie_2024]] [[Yang et al 2024][research_yang_tian_2024]] [[Yang et al 2025][research_yang_xie_2025]] [[Yang et al 2025][research_yang_xie_2025_b]] [[Yang et al 2025][research_yang_liu_2025]] [[Yang et al 2026][research_yang_wang_2026]] [[Yarng and Guan 1988][research_yarng_guan_1988]] [[Yi et al 2009][research_yi_jianhan_2009]] [[Yin et al 2024][research_yin_nakamura_2024]] [[You and Liang 2009][research_you_liang_2009]] [[You and Liang 2009][research_you_liang_2009_b]] [[You et al 2009][research_you_zhu_2009]] [[Yu et al 2007][research_yu_chang_2007]] [[Yu, Sheng-Tao et al 1988][research_yushengtao_hsiehkwangchung_1988]] [[Yuan et al 2019][research_yuan_kawano_2019]] [[Yuceil et al 2009][research_yuceil_valdivia_2009]] [[Yue et al 2009][research_yue_xiao_2009]] [[Zanchetta and Cain 1998][research_zanchetta_cain_1998]] [[Zarillo and Militello 1999][research_zarillo_militello_1999]] [[Zeng et al 2026][research_zeng_wang_2026]] [[Zha et al 1998][research_zha_knight_1998]] [[Zha et al 1998][research_zha_knight_1998_b]] [[Zhai et al 2020][research_zhai_zhang_2020]] [[Zhang 2015][research_zhang_2015]] [[Zhang 2020][research_zhang_2020]] [[Zhang 2020][research_zhang_2020_b]] [[Zhang 2020][research_zhang_2020_c]] [[Zhang 2020][research_zhang_2020_d]] [[Zhang et al 2015][research_zhang_zhang_2015]] [[Zhang et al 2016][research_zhang_tan_2016]] [[Zhang et al 2016][research_zhang_tan_2016_b]] [[Zhang et al 2018][research_zhang_liu_2018]] [[Zhang et al 2021][research_zhang_ge_2021]] [[Zhang et al 2023][research_zhang_li_2023]] [[Zhang et al 2024][research_zhang_xie_2024]] [[Zhang et al 2026][research_zhang_chen_2026_b]] [[Zheng et al 2013][research_zheng_chang_2013]] [[Zhou et al 2022][research_zhou_xu_2022]] [[Zhu et al 2020][research_zhu_luo_2020]] [[Zhu et al 2026][research_zhu_liu_2026]] [[Zoccoli 1977][research_zoccoli_1977]]

### Heat as a load rather than a rate, and where it goes

**The article's argument lives here.** Aerodynamic heating, heat flux, stagnation temperature, thermal protection, ablation and hot structures. **A heat flux is a rate and a heat load is its integral**, and a vehicle that flies nineteen times longer than its predecessor at a third of the heating rate still absorbs nearly three times as much heat.

**395 records.** [[Achambath et al 2019][research_achambath_ramjatan_2019]] [[Acheson and Rothnie 2009][research_acheson_rothnie_2009]] [[Aerodynamic Heating to the 1979][research_aerodynamic_heating_1979]] [[Aerothermodynamics Research in the 2002][research_aerothermodynamics_research_2002]] [[Agarwal 2011][research_agarwal_2011]] [[Agrawal et al 2012][research_agrawal_sepka_2012]] [[Aksonov 2023][research_aksonov_2023]] [[Albano et al 2013][research_albano_micheli_2013]] [[Analysis on temperature and 1998][research_analysis_on_1998]] [[Appar and Kumar 2021][research_appar_kumar_2021]] [[Aprovitola et al 2019][research_aprovitola_iuspa_2019]] [[Ardema, Mark D. 1995][research_ardemamarkd_1995]] [[Aronov and Klyagin 2021][research_aronov_klyagin_2021]] [[Arons and Macnair 1970][research_arons_macnair_1970]] [[Aso et al 1993][research_aso_kumamoto_1993]] [[Aso et al 2002][research_aso_hayashi_2002]] [[Assessment of Key Aerothermal 1992][research_assessment_of_1992]] [[Atay et al 2026][research_atay_kumartaslioglu_2026]] [[Auxer 1968][research_auxer_1968]] [[Avery, D. E. 1981][research_averyde_1981]] [[B. 2011][research_b_2011]] [[Bano et al 2026][research_bano_fraser_2026]] [[Barone et al 2022][research_barone_nicholson_2022]] [[Bates et al 2004][research_bates_maas_2004]] [[Bein et al 1993][research_bein_friedmann_1993]] [[Bettis and Hosder 2010][research_bettis_hosder_2010]] [[Blosser, M. L. 1987][research_blosserml_1987]] [[Blosser, M. L. and Mcwithey, R. R. 1983][research_blosserml_mcwitheyrr_1983]] [[Blosser, Max L. 1988][research_blossermaxl_1988]] [[Bogart et al 1981][research_bogart_breckenridge_1981]] [[Bowles et al 1998][research_bowles_roberts_1998]] [[Brociek et al 2023][research_brociek_hetmaniok_2023]] [[Brody K Bessire][research_brodykbessire]] [[Brooke 1957][research_brooke_1957]] [[Brune et al 2016][research_brune_hosder_2016]] [[Brunner 1959][research_brunner_1959]] [[Candler et al 2015][research_candler_subbareddy_2015]] [[Carman and J. B. 1966][research_carman_jb_1966]] [[Chang 1966][research_chang_1966]] [[Chang et al 2022][research_chang_huang_2022]] [[Chapter 1 Asymptotically Simplified 2013][research_chapter_1_2013]] [[Chapter 10 Numerical Modeling 2013][research_chapter_10_2013]] [[Chapter 13 Numerical Modeling 2013][research_chapter_13_2013]] [[Chapter 6 Modeling of 2013][research_chapter_6_2013]] [[Chapter 8 Numerical Study 2013][research_chapter_8_2013]] [[Chauvin et al 1968][research_chauvin_erb_1968]] [[Chen 1958][research_chen_1958]] [[Chen and He 2025][research_chen_he_2025]] [[Chen and Henline 1993][research_chen_henline_1993]] [[Chen and Milos 1996][research_chen_milos_1996]] [[Chen et al 2014][research_chen_ai_2014]] [[Chen et al 2015][research_chen_liu_2015]] [[Chen et al 2016][research_chen_chen_2016]] [[Cheung et al 1974][research_cheung_chen_1974]] [[Choi and Gamba 2026][research_choi_gamba_2026]] [[Chou and Smith 1974][research_chou_smith_1974]] [[Chun 1991][research_chun_1991]] [[Clarke 2008][research_clarke_2008]] [[Cohen 2011][research_cohen_2011]] [[Collins, Timothy J. et al 2005][research_collinstimothyj_congdonwilliamm_2005]] [[Comstock][research_comstock]] [[Cook][research_cook]] [[Cristiano Paulino Pereira et al 2021][research_cristianopaulinopereira_marinho_2021]] [[Culler et al 2007][research_culler_williams_2007]] [[Dai et al 2023][research_dai_zhao_2023]] [[Dajun et al 2006][research_dajun_guobiao_2006]] [[Daryabeigi, Kamran et al 2006][research_daryabeigikamran_blossermaxl_2006]] [[David E Glass][research_davideglass]] [[David E Glass][research_davideglass_b]] [[David E Glass][research_davideglass_c]] [[Dec and Mitcheltree 2002][research_dec_mitcheltree_2002]] [[Design Considerations for a 1963][research_design_considerations_1963]] [[Di Clemente et al 2009][research_diclemente_rufolo_2009]] [[Dicristina 1979][research_dicristina_1979]] [[Dolan 1970][research_dolan_1970]] [[Drummond, J. Philip et al 2002][research_drummondjphilip_cockrellcharlesejr_2002]] [[Du et al 2017][research_du_wan_2017]] [[Duston et al 2004][research_duston_seghi_2004]] [[Eagle and Ross 1955][research_eagle_ross_1955]] [[Economos 1962][research_economos_1962]] [[Elizabeth F Rieken et al 2020][research_elizabethfrieken_scottaberry_2020]] [[Farmakovsky et al 2005][research_farmakovsky_vinogradova_2005]] [[Fatemi and Lemmen 2006][research_fatemi_lemmen_2006]] [[Feldman, Jay et al 2019][research_feldmanjay_stewartdavid_2019]] [[Feng et al 2014][research_feng_tang_2014]] [[Filipkovskyi 2026][research_filipkovskyi_2026]] [[Finkler and Weiser 1994][research_finkler_weiser_1994]] [[Flanagan, Jr. 1993][research_flanaganjr_1993]] [[Florence 1979][research_florence_1979]] [[Frisch and Giedt 1965][research_frisch_giedt_1965]] [[Frisch and Giedt 1965][research_frisch_giedt_1965_b]] [[Fujii and Inoue 1998][research_fujii_inoue_1998]] [[Fujii et al 2000][research_fujii_watanabe_2000]] [[Fujii et al 2001][research_fujii_watanabe_2001]] [[Gally and Campbell 2002][research_gally_campbell_2002]] [[Gao et al 2021][research_gao_gou_2021]] [[Gao et al 2021][research_gao_song_2021]] [[Gao et al 2024][research_gao_li_2024]] [[Gao et al 2026][research_gao_he_2026]] [[Gladden and Melis 1994][research_gladden_melis_1994]] [[Glass 2008][research_glass_2008]] [[Glass 2018][research_glass_2018]] [[Gnoffo, Peter A. 2001][research_gnoffopetera_2001]] [[Godi 2024][research_godi_2024]] [[Gong Weijie and Tang Shuo 2010][research_gongweijie_tangshuo_2010]] [[Gonzalez et al 2025][research_gonzalez_castillo_2025]] [[Goshima and Miyao 1991][research_goshima_miyao_1991]] [[Gregory 2005][research_gregory_2005]] [[Gros 1963][research_gros_1963]] [[Gudimella et al 2018][research_gudimella_sinha_2018]] [[Gusev 1990][research_gusev_1990]] [[Han and Han 2024][research_han_han_2024]] [[Han et al 2020][research_han_sun_2020]] [[Hanai et al 2007][research_hanai_ozawa_2007]] [[Hannah and Muessig 1970][research_hannah_muessig_1970]] [[Harloff and Petrie 1987][research_harloff_petrie_1987]] [[Harri 1964][research_harri_1964]] [[Hayashi and Aso 1988][research_hayashi_aso_1988]] [[He et al 2026][research_he_zhang_2026]] [[Heat transfer to endothermic 1991][research_heat_transfer_1991]] [[Hirschel and Weiland 2009][research_hirschel_weiland_2009]] [[Holden 1993][research_holden_1993]] [[Holifield and Tufts 2024][research_holifield_tufts_2024]] [[Holifield and Tufts 2024][research_holifield_tufts_2024_b]] [[Hossain 2025][research_hossain_2025]] [[Hoter et al 2026][research_hoter_nastac_2026]] [[Huang et al 2022][research_huang_liu_2022]] [[Huang et al 2025][research_huang_li_2025]] [[Huang et al 2025][research_huang_li_2025_b]] [[Huber 1966][research_huber_1966]] [[Hypersonic Materials for Thermal 2023][research_hypersonic_materials_2023]] [[Ibrahim 1967][research_ibrahim_1967]] [[Ikenson 2025][research_ikenson_2025]] [[Iliff, Kenneth W. and Shafer, Mary F. 1993][research_iliffkennethw_shafermaryf_1993_b]] [[Inger 1991][research_inger_1991]] [[Inger 1995][research_inger_1995_b]] [[Inger 1995][research_inger_1995_c]] [[Initial Shuttle External Tank 1983][research_initial_shuttle_1983]] [[Inokuma et al 2025][research_inokuma_yakeno_2025]] [[Jackson and Anderson 1967][research_jackson_anderson_1967]] [[Jagadeesh et al 1998][research_jagadeesh_reddy_1998]] [[Jay D Feldman][research_jaydfeldman]] [[Ji 2017][research_ji_2017]] [[Jing et al 2026][research_jing_song_2026]] [[Jo 2026][research_jo_2026]] [[John Michael Thornton et al][research_johnmichaelthornton_jeremiebernarderwinmeurisse]] [[Johnson 1967][research_johnson_1967]] [[Johnson, Sylvia and Conley, Joe 2015][research_johnsonsylvia_conleyjoe_2015]] [[Johnston 1969][research_johnston_1969]] [[Kai and Ohtake 1996][research_kai_ohtake_1996]] [[Kamezawa and Ruffin 2018][research_kamezawa_ruffin_2018]] [[Kanderpalli et al 2014][research_kanderpalli_selvaraj_2014]] [[Karimi and Oboodi 2018][research_karimi_oboodi_2018]] [[Kaufman 1963][research_kaufman_1963]] [[Khrapko 2018][research_khrapko_2018]] [[Kidd and Adams, Jr. 2000][research_kidd_adamsjr_2000]] [[Kim 2017][research_kim_2017]] [[Kkn and Reddy 2016][research_kkn_reddy_2016]] [[Knight et al 2026][research_knight_kildare_2026]] [[Kojima et al 2012][research_kojima_taguchi_2012]] [[Kontinos 1996][research_kontinos_1996]] [[Kopp and Garbers 2014][research_kopp_garbers_2014]] [[Korabelnikov and Kuranov 2002][research_korabelnikov_kuranov_2002]] [[Korabelnikov and Kuranov 2005][research_korabelnikov_kuranov_2005]] [[Kourtides et al 1988][research_kourtides_pitts_1988]] [[Kubota and Uchida 1999][research_kubota_uchida_1999]] [[Kumar and Mahulikar 2017][research_kumar_mahulikar_2017]] [[Kundu 2013][research_kundu_2013]] [[Kuo 1976][research_kuo_1976]] [[Kuranov et al 2012][research_kuranov_korabelnikov_2012]] [[Kuranov et al 2016][research_kuranov_korabelnikov_2016]] [[Lambert][research_lambert]] [[Lane, Jr. and Kirlin 1978][research_lanejr_kirlin_1978]] [[Lee et al 2015][research_lee_kim_2015]] [[Lee et al 2026][research_lee_kim_2026_b]] [[Leontiev et al 2000][research_leontiev_nosatov_2000]] [[Li and Han 2025][research_li_han_2025]] [[Li and Zhao 2014][research_li_zhao_2014]] [[Li and Zhu 2012][research_li_zhu_2012]] [[Li et al 2017][research_li_chen_2017_b]] [[Li et al 2021][research_li_wang_2021]] [[Li et al 2024][research_li_wang_2024_b]] [[Li et al 2026][research_li_ding_2026]] [[Lippitt et al 1983][research_lippitt_jr_1983]] [[Liu and Cao 2017][research_liu_cao_2017]] [[Liu and Jiang 2013][research_liu_jiang_2013]] [[Liu et al 2002][research_liu_chen_2002]] [[Liu et al 2018][research_liu_shi_2018]] [[Liu et al 2019][research_liu_zhang_2019]] [[Liu et al 2023][research_liu_fang_2023]] [[Liu et al 2025][research_liu_lyu_2025]] [[Lu and Liu 2012][research_lu_liu_2012]] [[Lu et al 2016][research_lu_zhang_2016]] [[Lu et al 2025][research_lu_zhang_2025]] [[Luce and Jr 1949][research_luce_jr_1949]] [[M. A. Al-Nimr, Naser S. Al-Huniti 2000][research_maalnimrnasersalhuniti_2000]] [[Ma et al 2022][research_ma_xie_2022]] [[Maas et al 2004][research_maas_irvine_2004]] [[Maccallum 1969][research_maccallum_1969]] [[Mahlmeister et al 1955][research_mahlmeister_ishimoto_1955]] [[Mahulikar et al 2008][research_mahulikar_khurana_2008]] [[Manor et al 2002][research_manor_lau_2002]] [[Marley and Driscoll 2017][research_marley_driscoll_2017]] [[Marley and Driscoll 2022][research_marley_driscoll_2022]] [[Marston 1965][research_marston_1965]] [[Massa 2022][research_massa_2022]] [[Matheny and Smith 2026][research_matheny_smith_2026]] [[Matsunaga et al 2017][research_matsunaga_takahashi_2017]] [[Matthews 1993][research_matthews_1993]] [[Maxwell and Hoang 2016][research_maxwell_hoang_2016]] [[Mehta et al 2025][research_mehta_brewer_2025]] [[Melis and Gladden 1990][research_melis_gladden_1990]] [[Menssen 2026][research_menssen_2026]] [[Mifsud et al 2012][research_mifsud_estruchsamper_2012]] [[Miyashita et al 2025][research_miyashita_sugihara_2025]] [[Molina et al 1996][research_molina_simeonides_1996]] [[Mooij 2023][research_mooij_2023]] [[Mori 1965][research_mori_1965]] [[Mori et al 2012][research_mori_ishibashi_2012]] [[Mudaliar et al 2022][research_mudaliar_gomes_2022]] [[Nagamatsu et al 1960][research_nagamatsu_workman_1960]] [[Najafiyazdi 2005][research_najafiyazdi_2005]] [[Najafiyazdi 2005][research_najafiyazdi_2005_b]] [[Nardo and Sadler 1962][research_nardo_sadler_1962]] [[Nestler 1970][research_nestler_1970]] [[Neumann 1993][research_neumann_1993]] [[Neumann et al 1978][research_neumann_patterson_1978]] [[Nguyen and Massa 2023][research_nguyen_massa_2023]] [[Nguyen and Massa 2023][research_nguyen_massa_2023_b]] [[Nguyen and Massa 2024][research_nguyen_massa_2024]] [[Nie and Liu 2013][research_nie_liu_2013]] [[Noda 1988][research_noda_1988]] [[Nonequilibrium Stagnation Region Aerodynamic 1975][research_nonequilibrium_stagnation_1975]] [[North 1983][research_north_1983]] [[Oliveira Júnior et al 2021][research_oliveirajunior_marinho_2021]] [[Ootao and Ishihara 2012][research_ootao_ishihara_2012]] [[Ootao and Ishihara 2013][research_ootao_ishihara_2013]] [[Ootao and Tanigawa 2005][research_ootao_tanigawa_2005]] [[Ozawa et al 2008][research_ozawa_hanai_2008]] [[Parsons et al 2023][research_parsons_armstrong_2023]] [[Parton 2018][research_parton_2018]] [[Pendergast and Mollendorf 2008][research_pendergast_mollendorf_2008]] [[Persh 1955][research_persh_1955]] [[Persova et al 2017][research_persova_soloveichik_2017]] [[Pionessa and Kinzel 2024][research_pionessa_kinzel_2024]] [[Pionessa and Kinzel 2024][research_pionessa_kinzel_2024_b]] [[Pollock et al 2023][research_pollock_moran_2023]] [[Porro and Hingst 1993][research_porro_hingst_1993]] [[Preliminary Design of the 1983][research_preliminary_design_1983]] [[Qiao et al 2024][research_qiao_liu_2024]] [[Qiu et al 2017][research_qiu_zhang_2017]] [[Qu et al 2019][research_qu_kong_2019]] [[Quinn, Robert D. and Gong, Leslie 1990][research_quinnrobertd_gongleslie_1990]] [[Radiative Heat Transfer In 2018][research_radiative_heat_2018]] [[Rafla 2019][research_rafla_2019]] [[Rafla 2019][research_rafla_2019_b]] [[Rasky, Daniel J. et al 1998][research_raskydanielj_tranhuyk_1998]] [[Ravichandran et al 2023][research_ravichandran_doherty_2023]] [[Ravichandran et al 2023][research_ravichandran_doherty_2023_b]] [[Reba 1964][research_reba_1964]] [[Reba and Christian 1963][research_reba_christian_1963]] [[Reimer et al 2023][research_reimer_dimartino_2023]] [[Rhisat and Molki 2024][research_rhisat_molki_2024]] [[Riabov 1994][research_riabov_1994]] [[Riley and Dejarnette 1992][research_riley_dejarnette_1992]] [[Rizk 1993][research_rizk_1993]] [[Roach et al 1996][research_roach_caldarella_1996]] [[Rong 2017][research_rong_2017]] [[Rong et al 2016][research_rong_wei_2016]] [[Rosner and Cibrian 1974][research_rosner_cibrian_1974]] [[Ruoling et al 2012][research_ruoling_jin_2012]] [[Sabry and Hussin 2026][research_sabry_hussin_2026]] [[Sai Naga Bharghava et al 2024][research_sainagabharghava_krishnatmali_2024]] [[Santos and Lewis 2003][research_santos_lewis_2003]] [[Savino et al 2004][research_savino_fumo_2004]] [[Scala 1962][research_scala_1962]] [[Scala and Nolan 1960][research_scala_nolan_1960]] [[Schettino and Borrelli 1998][research_schettino_borrelli_1998]] [[Schiavazzi and Juliano 2020][research_schiavazzi_juliano_2020]] [[Schoeler 1978][research_schoeler_1978]] [[Schwanekamp 2014][research_schwanekamp_2014]] [[Shang 2009][research_shang_2009_b]] [[Shang and Surzhikov 2011][research_shang_surzhikov_2011]] [[Shanmugam and Sun Park 2024][research_shanmugam_sunpark_2024]] [[Sheng et al 2021][research_sheng_lu_2021]] [[Shevelev 2018][research_shevelev_2018]] [[Shi et al 2015][research_shi_dai_2015]] [[Shi et al 2021][research_shi_zha_2021]] [[Shih et al 1988][research_shih_zwan_1988]] [[Si et al 2019][research_si_huang_2019]] [[Silver et al 2024][research_silver_brooks_2024]] [[Simmons and Meritt 2022][research_simmons_meritt_2022]] [[Smith 2021][research_smith_2021]] [[Smith and Baxter][research_smith_baxter]] [[Song et al 2023][research_song_qin_2023]] [[Stanley, Thomas Troy et al 2000][research_stanleythomastroy_alexanderreginald_2000]] [[Static and dynamic flow 2005][research_static_and_2005]] [[Sternberg 1964][research_sternberg_1964]] [[Stevens 2014][research_stevens_2014]] [[Stoll 1961][research_stoll_1961]] [[Stoll et al 1975][research_stoll_munroe_1975]] [[Sun and Zhu 2019][research_sun_zhu_2019]] [[Sun et al 2020][research_sun_yang_2020]] [[Sun et al 2023][research_sun_zhu_2023]] [[Sun et al 2025][research_sun_li_2025]] [[Sun Jian and Liu Wei-Qiang 2014][research_sunjian_liuweiqiang_2014]] [[Sundén and Fu 2017][research_sunden_fu_2017]] [[Sutton et al 1995][research_sutton_troiler_1995]] [[Suzuki and Watanabe 2013][research_suzuki_watanabe_2013]] [[Taguchi and Kashitani 2025][research_taguchi_kashitani_2025]] [[Takahashi et al 2013][research_takahashi_yamada_2013]] [[Tanigawa 1999][research_tanigawa_1999]] [[Tatsuta et al 2025][research_tatsuta_yamada_2025]] [[Taylor and Stringer 2024][research_taylor_stringer_2024]] [[Thermal Protection Methods for 2009][research_thermal_protection_2009]] [[Thielman 1995][research_thielman_1995]] [[Thivet and Pélissier 2003][research_thivet_pelissier_2003]] [[Thomas et al 1985][research_thomas_singh_1985]] [[Thomas et al 1998][research_thomas_hyde_1998]] [[Thomas et al 2022][research_thomas_marayikkottuvijayan_2022]] [[Thornton et al 1989][research_thornton_oden_1989]] [[Tian et al 2023][research_tian_duan_2023]] [[Tile-Gap Flow in the 1983][research_tile_gap_flow_1983]] [[Tirskii 1993][research_tirskii_1993]] [[Tirsky 1993][research_tirsky_1993]] [[Tobe and Grandhi 2013][research_tobe_grandhi_2013]] [[Tobin and Dec 2015][research_tobin_dec_2015]] [[Tong and Giedt 1963][research_tong_giedt_1963]] [[Tong et al 2022][research_tong_yuan_2022]] [[Tong et al 2024][research_tong_ji_2024]] [[Tran and Chen 1998][research_tran_chen_1998]] [[Trimmer 1968][research_trimmer_1968]] [[Truitt, R. W. 1968][research_truittrw_1968]] [[Two-phase flow in high-heat-flux 2006][research_two_phase_flow_2006]] [[Two-phase flow in high-heat-flux 2006][research_two_phase_flow_2006_b]] [[Türkoğlu et al 2026][research_turkoglu_donmez_2026]] [[ul Islam Rizvi et al 2015][research_ulislamrizvi_linshu_2015]] [[Utyuzhnikov and Tirskiy 2013][research_utyuzhnikov_tirskiy_2013]] [[Vahl and Edwards 1978][research_vahl_edwards_1978]] [[Valaik et al 1997][research_valaik_hyde_1997]] [[Valaik et al 1998][research_valaik_bowman_1998]] [[van der Heide et al 2025][research_vanderheide_lock_2025]] [[Varghese et al 2018][research_varghese_b_2018]] [[Vasilevsky 2022][research_vasilevsky_2022]] [[Veraar 2008][research_veraar_2008]] [[Veraar 2009][research_veraar_2009]] [[Viscous Flow Basic Aspects 2006][research_viscous_flow_2006]] [[Viscous Flow Basic Aspects 2019][research_viscous_flow_2019]] [[Wang and Luo 2022][research_wang_luo_2022]] [[Wang and Zhang 2025][research_wang_zhang_2025]] [[Wang et al 2017][research_wang_hao_2017]] [[Wang et al 2022][research_wang_zhang_2022]] [[Wang et al 2024][research_wang_wang_2024_d]] [[Wassel et al 1984][research_wassel_shih_1984]] [[Way et al 2024][research_way_sescu_2024]] [[Weiler et al 1972][research_weiler_derbidge_1972]] [[Williams et al 2006][research_williams_bolender_2006]] [[Williams et al 2026][research_williams_davuluri_2026]] [[Winkler 1954][research_winkler_1954]] [[Wittliff and Wilson 1961][research_wittliff_wilson_1961]] [[Wurster 1981][research_wurster_1981]] [[Xie et al 2020][research_xie_dong_2020]] [[Xin et al 2023][research_xin_zhang_2023]] [[Xin et al 2025][research_xin_li_2025]] [[Xu and Fang 2022][research_xu_fang_2022]] [[Xu et al 2018][research_xu_sun_2018]] [[Yakimov 2018][research_yakimov_2018]] [[Yakimov 2018][research_yakimov_2018_b]] [[Yakimov 2018][research_yakimov_2018_c]] [[Yakubayev et al 2026][research_yakubayev_gschwend_2026]] [[Yang and Liu 2017][research_yang_liu_2017]] [[Yang et al 2014][research_yang_duan_2014]] [[Yang et al 2024][research_yang_zhao_2024]] [[Yang et al 2024][research_yang_yuan_2024]] [[Yao et al 2023][research_yao_wang_2023]] [[Yu et al 2025][research_yu_wang_2025]] [[Yu et al 2025][research_yu_wang_2025_b]] [[Yuan et al 2020][research_yuan_sivasankaran_2020]] [[Yue et al 2016][research_yue_wu_2016]] [[Yumusak and Eyi 2013][research_yumusak_eyi_2013]] [[Zapp and Bermejo-Moreno 2026][research_zapp_bermejomoreno_2026]] [[Zapp and Bermejo-Moreno 2026][research_zapp_bermejomoreno_2026_b]] [[Zhang et al 2015][research_zhang_zhao_2015]] [[Zhang et al 2024][research_zhang_zhang_2024]] [[Zhao 2011][research_zhao_2011]] [[Zhao 2021][research_zhao_2021_c]] [[Zhao et al 2009][research_zhao_zhang_2009]] [[Zhao et al 2023][research_zhao_gao_2023]] [[Zhou et al 2008][research_zhou_bao_2008]] [[Zhou et al 2022][research_zhou_du_2022]] [[Zhu and Yin 2026][research_zhu_yin_2026]] [[Zhu et al 2016][research_zhu_zhao_2016]] [[Zohar R Hoter et al][research_zoharrhoter_gabrielcnastac]] [[Zuchowski 2013][research_zuchowski_2013]] [[Ösün et al 2026][research_osun_james_2026]]

### Flight test, instrumentation and what was actually measured

**Four flights, and telemetry for 370 seconds on the last of them.** Flight experiment design, instrumentation, telemetry and flight-derived data. **A hypersonic demonstrator returns data or it returns nothing**, since there is no vehicle to inspect afterwards and every X-51A ended in the Pacific by design.

**251 records.** [[1st Flight Test Conference 1981][research_1st_flight_1981]] [[4th Flight Test Conference 1988][research_4th_flight_1988]] [[A global telemetry data 1988][research_a_global_1988]] [[Adolph 1981][research_adolph_1981]] [[Ahn et al 2026][research_ahn_yu_2026]] [[Air Force Flight Test Center Edwards Afb Ca 1970][research_airforceflighttestcenteredwardsafbca_1970]] [[Air Force Flight Test Center Edwards Afb Ca 2002][research_airforceflighttestcenteredwardsafbca_2002]] [[Air Force Test Pilot School Edwards Afb Ca 1962][research_airforcetestpilotschooledwardsafbca_1962]] [[Air Force Test Pilot School Edwards Afb Ca 1990][research_airforcetestpilotschooledwardsafbca_1990]] [[Air Force Test Pilot School Edwards Afb Ca 1990][research_airforcetestpilotschooledwardsafbca_1990_b]] [[Air Force Test Pilot School Edwards Afb Ca 1993][research_airforcetestpilotschooledwardsafbca_1993]] [[Aircraft and Flight Test 2021][research_aircraft_and_2021]] [[Alich and Castillo 2007][research_alich_castillo_2007]] [[Andrews and Gordon 1981][research_andrews_gordon_1981]] [[Approximate Method of Predicting 1983][research_approximate_method_1983]] [[Arent and Falatko 1992][research_arent_falatko_1992]] [[Arnold 1981][research_arnold_1981]] [[Bartolome Calvo and Eggers 2011][research_bartolomecalvo_eggers_2011]] [[Bender 1969][research_bender_1969]] [[Berens and Bissinger 1998][research_berens_bissinger_1998_b]] [[Bertelrud et al 1999][research_bertelrud_budd_1999]] [[Bever 1992][research_bever_1992]] [[Biennial Flight Test Conference 1994][research_biennial_flight_1994]] [[Biggi et al 2024][research_biggi_abdelnour_2024]] [[Bleimeyer 1981][research_bleimeyer_1981]] [[Boeing to use X-43A 2005][research_boeing_to_2005]] [[Bogue 1992][research_bogue_1992]] [[Boirun 1979][research_boirun_1979]] [[Bolt 1981][research_bolt_1981]] [[Borg et al 2025][research_borg_adamczak_2025]] [[Brooks 1986][research_brooks_1986]] [[Brown 2012][research_brown_2012]] [[Brown and Bradley 1981][research_brown_bradley_1981]] [[Bryan 1953][research_bryan_1953]] [[Burnett 2002][research_burnett_2002]] [[Burton 1987][research_burton_1987]] [[Cain and Walton 2003][research_cain_walton_2003]] [[Campbell and Kresge 2003][research_campbell_kresge_2003]] [[Carpenter et al 2025][research_carpenter_hantsche_2025]] [[Carroll et al 1981][research_carroll_kerlin_1981]] [[Cassanto 1971][research_cassanto_1971]] [[Cassanto 1972][research_cassanto_1972]] [[Cenkci 1991][research_cenkci_1991]] [[Cenko 1992][research_cenko_1992]] [[Cenko et al 2003][research_cenko_cenko_2003]] [[Chase and Rust 1980][research_chase_rust_1980]] [[Chen, Fang-Jeng Frank and Berry, Scott A. 2010][research_chenfangjengfrank_berryscotta_2010]] [[Cheney 1988][research_cheney_1988]] [[Clark 1965][research_clark_1965]] [[Comparison of Orbiter STS-2 1983][research_comparison_of_1983]] [[Cook 1981][research_cook_1981]] [[Craig and Reich 1981][research_craig_reich_1981]] [[Cusimano and Johnson 1994][research_cusimano_johnson_1994]] [[Czysz and Murthy 1996][research_czysz_murthy_1996]] [[Czysz et al 1997][research_czysz_froning_1997]] [[D'Amico et al 2004][research_damico_simon_2004]] [[Dalle et al 2011][research_dalle_torrez_2011_b]] [[Dasgupta et al 2012][research_dasgupta_choudhury_2012]] [[Dassoulas 1963][research_dassoulas_1963]] [[de Boer et al 2015][research_deboer_flourens_2015]] [[Demo 1986][research_demo_1986]] [[Dickhudt 1983][research_dickhudt_1983]] [[Dobronski 1988][research_dobronski_1988]] [[Dolvin 2009][research_dolvin_2009]] [[Donelson et al 1989][research_donelson_lewerenz_1989]] [[Draper et al 1977][research_draper_lanejr_1977]] [[Durbin 1959][research_durbin_1959]] [[Dwyer 1994][research_dwyer_1994]] [[E. C. Schwegler - Lanl and A. Place - Honeywell 2000][research_ecschweglerlanl_aplacehoneywell_2000]] [[ECO Demonstrator Begins Flight 2018][research_eco_demonstrator_2018]] [[Edquist 2006][research_edquist_2006]] [[Eglin et al 2025][research_eglin_embacher_2025]] [[Evaluation of turbulent heating 1973][research_evaluation_of_1973]] [[Falempin and Serre 2003][research_falempin_serre_2003]] [[Falempin and Serre 2006][research_falempin_serre_2006]] [[Falempin and Serre 2008][research_falempin_serre_2008]] [[Falempin et al 1995][research_falempin_thevenot_1995]] [[Faulstich and Law 2006][research_faulstich_law_2006]] [[Fechter and Mills 1988][research_fechter_mills_1988]] [[Fletcher 1994][research_fletcher_1994]] [[Flight Test Instrumentation 1965][research_flight_test_1965]] [[Flight TEST Manual 1959][research_flight_test_1959]] [[Flight Test Planning 2021][research_flight_test_2021]] [[French 1988][research_french_1988]] [[Fuel cell demonstrator aeroplane 2007][research_fuel_cell_2007]] [[Furstenau 1965][research_furstenau_1965]] [[Further development and flight 1994][research_further_development_1994]] [[Förder and Steiner 2020][research_forder_steiner_2020]] [[General Dynamics/Astronautics San Diego Ca 1961][research_generaldynamicsastronauticssandiegoca_1961_b]] [[General Dynamics/Astronautics San Diego Ca 1962][research_generaldynamicsastronauticssandiegoca_1962]] [[General Dynamics/Astronautics San Diegoca 1961][research_generaldynamicsastronauticssandiegoca_1961]] [[Gibson et al 2002][research_gibson_neidhoefer_2002]] [[Grantz et al 1993][research_grantz_cervisi_1993]] [[Green and Fernandez 1994][research_green_fernandez_1994]] [[Guelhan et al 2012][research_guelhan_siebe_2012]] [[Hall, J. L. 2002][research_halljl_2002]] [[Hammond 1965][research_hammond_1965]] [[Harris et al 1994][research_harris_hines_1994]] [[Hart 1992][research_hart_1992]] [[Head 1981][research_head_1981]] [[Hicks, John W. 1992][research_hicksjohnw_1992]] [[Hildebrand 1979][research_hildebrand_1979]] [[Hillaker 1983][research_hillaker_1983]] [[Ho 2006][research_ho_2006]] [[Hoadley 1988][research_hoadley_1988]] [[Holberg and Grabowsky 1981][research_holberg_grabowsky_1981]] [[Hoult et al 2003][research_hoult_starkey_2003]] [[Howell 1988][research_howell_1988]] [[Howland 1953][research_howland_1953]] [[Hypersonic Air-Breathing Flight Testing 2022][research_hypersonic_air_breathing_2022]] [[Iliff and Shafer 1992][research_iliff_shafer_1992]] [[Ince 1967][research_ince_1967]] [[Incorporating agility flight test 1994][research_incorporating_agility_1994]] [[James 2022][research_james_2022]] [[Jann and Yakimenko 2015][research_jann_yakimenko_2015]] [[Jategaonkar et al 2005][research_jategaonkar_behr_2005]] [[Jessica Lux-Baumann and Darryl A Burkes 2005][research_jessicaluxbaumann_darrylaburkes_2005]] [[Jiang et al 2017][research_jiang_song_2017]] [[Jones and Laurence 2025][research_jones_laurence_2025]] [[Jordan 1974][research_jordan_1974]] [[Kao and Anderson 1981][research_kao_anderson_1981]] [[Kelly 1988][research_kelly_1988]] [[Kelso 1993][research_kelso_1993]] [[Kennedy 1986][research_kennedy_1986]] [[Klingenberg et al 2026][research_klingenberg_willems_2026]] [[Knighton 1992][research_knighton_1992]] [[Kobayashi et al 2008][research_kobayashi_sawai_2008]] [[Kramer et al 2018][research_kramer_williams_2018]] [[Krumenacker and Pellicano 1992][research_krumenacker_pellicano_1992]] [[Kuppuswamy and Kiran 1981][research_kuppuswamy_kiran_1981]] [[Lamy 1983][research_lamy_1983]] [[Lang 1981][research_lang_1981]] [[Large et al 1981][research_large_may_1981]] [[Ledu and Pollak 1968][research_ledu_pollak_1968]] [[Lewerenz 1987][research_lewerenz_1987]] [[Li and Wey 1988][research_li_wey_1988]] [[Lightweight low-cost flight test 2007][research_lightweight_low_cost_2007]] [[Liu et al 2025][research_liu_shan_2025]] [[Losik 2008][research_losik_2008]] [[Luecke 1957][research_luecke_1957]] [[Lux, Jessica and Burkes, Darryl A. 2008][research_luxjessica_burkesdarryla_2008]] [[Lux-Baumann, Jessica and Burkes, Darryl 2006][research_luxbaumannjessica_burkesdarryl_2006]] [[Machnik et al 2022][research_machnik_decker_2022]] [[Macmillan 1981][research_macmillan_1981]] [[Mannai 1962][research_mannai_1962]] [[Manning et al 1992][research_manning_baum_1992]] [[Martínez Morán 2018][research_martinezmoran_2018]] [[Matheny and Panageas 1981][research_matheny_panageas_1981]] [[Maydew 1964][research_maydew_1964]] [[Mayer and Chalfant 2023][research_mayer_chalfant_2023]] [[Mckenzie 1973][research_mckenzie_1973]] [[McQuellin et al 2020][research_mcquellin_neely_2020]] [[Mehta, Unmeel B. and Kutler, Paul 1994][research_mehtaunmeelb_kutlerpaul_1994]] [[Mermagen 1964][research_mermagen_1964]] [[Mertaugh 1998][research_mertaugh_1998]] [[Monteil 2024][research_monteil_2024]] [[Moore 1965][research_moore_1965]] [[Moorhouse 1990][research_moorhouse_1990]] [[Morger 1988][research_morger_1988]] [[Mori et al 2002][research_mori_tsuchiya_2002]] [[Morris and Tigner 1995][research_morris_tigner_1995]] [[Nardozzo et al 2019][research_nardozzo_popkin_2019]] [[Neely and Tjong 2008][research_neely_tjong_2008]] [[Neely and Tracy 2006][research_neely_tracy_2006]] [[Neumann 2005][research_neumann_2005]] [[Niewöhner 2018][research_niewohner_2018]] [[Okojie et al 2009][research_okojie_danehy_2009]] [[Olguin 2019][research_olguin_2019]] [[Palomino 2022][research_palomino_2022]] [[Papa and Stoliker 1988][research_papa_stoliker_1988]] [[Pashai et al 2022][research_pashai_hurst_2022]] [[Pawlak 1994][research_pawlak_1994]] [[Petersen 1981][research_petersen_1981]] [[Platou 1968][research_platou_1968]] [[Platz and Bounajem 1992][research_platz_bounajem_1992]] [[Rediess and Melton 1994][research_rediess_melton_1994]] [[Reimer et al 2025][research_reimer_dimartino_2025]] [[Rempt 1981][research_rempt_1981]] [[Rhea and Moore 1988][research_rhea_moore_1988]] [[Ricciardi and Minwalla 2016][research_ricciardi_minwalla_2016]] [[Rice and Hazlwood 1994][research_rice_hazlwood_1994]] [[Roberts 1988][research_roberts_1988]] [[Roberts 1988][research_roberts_1988_b]] [[Roberts and Brown 1988][research_roberts_brown_1988]] [[Roberts and Shawler 1994][research_roberts_shawler_1994]] [[Robertson and Hartfield 1992][research_robertson_hartfield_1992]] [[Rooker 1970][research_rooker_1970]] [[Roseberry 2025][research_roseberry_2025]] [[Sanderson 1965][research_sanderson_1965]] [[Sanderson 1987][research_sanderson_1987]] [[Sanderson 2003][research_sanderson_2003]] [[Sanderson 2010][research_sanderson_2010]] [[Sandoz and Klaeyle 2021][research_sandoz_klaeyle_2021]] [[Sandoz et al 2024][research_sandoz_blanc_2024]] [[Sawai et al 2003][research_sawai_sato_2003]] [[Schweikhard 1983][research_schweikhard_1983]] [[Serre 2009][research_serre_2009]] [[Serre and Falempin 2008][research_serre_falempin_2008]] [[Serre et al 2011][research_serre_denis_2011]] [[Shields 1981][research_shields_1981]] [[Shou and Li 2026][research_shou_li_2026]] [[Siddiqi and Abraham 1988][research_siddiqi_abraham_1988]] [[Simulation in support of 1988][research_simulation_in_1988]] [[Smith and Pellicano 1992][research_smith_pellicano_1992]] [[Smith et al 2011][research_smith_bowcutt_2011]] [[Snyder 2003][research_snyder_2003]] [[Spravka and Jorris 2015][research_spravka_jorris_2015]] [[Spravka and Jorris 2015][research_spravka_jorris_2015_b]] [[Starkey et al 2014][research_starkey_cannella_2014]] [[Stenberg 1983][research_stenberg_1983]] [[Strock 1983][research_strock_1983]] [[Svec 1981][research_svec_1981]] [[Svendsen 1994][research_svendsen_1994]] [[Taguchi et al 2009][research_taguchi_harada_2009]] [[Takagi et al 2014][research_takagi_morozumi_2014]] [[Takahashi et al 2025][research_takahashi_hirotani_2025]] [[Talmage 2008][research_talmage_2008]] [[Taylor 1959][research_taylor_1959]] [[The Agard Flight TEST 1959][research_the_agard_1959]] [[Thornton 1994][research_thornton_1994]] [[Thornton and Lamy 1992][research_thornton_lamy_1992]] [[Tracy 1981][research_tracy_1981]] [[Transonic flight test of 1994][research_transonic_flight_1994]] [[Trittler et al 2008][research_trittler_fichter_2008]] [[Turner et al 2006][research_turner_hoerschgen_2006]] [[Ueno et al 2004][research_ueno_sarae_2004]] [[Van Pelt 1981][research_vanpelt_1981]] [[Vanatta and Inderhees 1988][research_vanatta_inderhees_1988]] [[Vaughn and Lindsay 1988][research_vaughn_lindsay_1988]] [[Veletas 2026][research_veletas_2026]] [[Walker et al 2008][research_walker_sherk_2008]] [[Walker et al 2008][research_walker_rodgers_2008]] [[Ward 1988][research_ward_1988]] [[Ward and Myers 1967][research_ward_myers_1967]] [[Watanabe et al 1996][research_watanabe_ishimoto_1996]] [[Wells, William L. 1987][research_wellswilliaml_1987]] [[Wittliff et al 1992][research_wittliff_oconnor_1992]] [[Wolf and Bossert 2001][research_wolf_bossert_2001]] [[Wulff and Zoellner 1991][research_wulff_zoellner_1991]] [[Wygle 1981][research_wygle_1981]] [[Xin 2023][research_xin_2023]] [[Yamato et al 1988][research_yamato_okada_1988]] [[Yanagihara et al 2003][research_yanagihara_nishizawa_2003]] [[Yang 2021][research_yang_2021]] [[Yang 2021][research_yang_2021_b]] [[Yang 2021][research_yang_2021_c]] [[Yang 2021][research_yang_2021_d]] [[Yang 2021][research_yang_2021_e]] [[Yechout 1988][research_yechout_1988]] [[Yergensen and Rhea 1988][research_yergensen_rhea_1988]] [[Zalesak, Sr. 1981][research_zalesaksr_1981]]

### Ground facilities and how hypersonic flow is made on Earth

**Where almost all of this subject's knowledge comes from.** Shock tunnels, arc-heated and combustion-heated facilities, free-jet and direct-connect testing, and the flow-quality and vitiation problems that make ground data hard to trust. **A ground facility that reproduces the Mach number does not reproduce the enthalpy, or reproduces it with the wrong gas**, which is why flight test exists at all.

**209 records.** [[A Hypersonic Ground-Test Facility 2002][research_a_hypersonic_2002_b]] [[A. 2013][research_a_2013]] [[Abgrall 1991][research_abgrall_1991]] [[Adams and Rubin 1958][research_adams_rubin_1958]] [[Alkandry et al 2009][research_alkandry_boyd_2009]] [[Anderson et al 1999][research_anderson_brown_1999]] [[Andrews and Poggie 2023][research_andrews_poggie_2023]] [[Asami 1999][research_asami_1999]] [[Best et al 2001][research_best_fetterhoff_2001]] [[Bhakta et al 2025][research_bhakta_sims_2025]] [[Biagioni et al 1998][research_biagioni_scortecci_1998]] [[Bissinger and Schmitz 1993][research_bissinger_schmitz_1993]] [[Borg et al 2012][research_borg_kimmel_2012]] [[Borg et al 2013][research_borg_kimmel_2013]] [[Bouchard and Chambers 1966][research_bouchard_chambers_1966]] [[Boyd et al 1993][research_boyd_phamvandiep_1993]] [[Bradley et al 1981][research_bradley_siemersiii_1981]] [[Briardy and Head 1968][research_briardy_head_1968]] [[Britcher and Landman 2024][research_britcher_landman_2024]] [[Britcher and Landman 2024][research_britcher_landman_2024_b]] [[Britcher and Landman 2024][research_britcher_landman_2024_c]] [[Britcher and Landman 2024][research_britcher_landman_2024_d]] [[Britcher and Landman 2024][research_britcher_landman_2024_e]] [[Britcher and Landman 2024][research_britcher_landman_2024_f]] [[Buchanan and Crosby 1983][research_buchanan_crosby_1983]] [[Buck and Draper][research_buck_draper]] [[Buonadonna et al 1973][research_buonadonna_knight_1973]] [[Burns 1970][research_burns_1970]] [[Butler 1976][research_butler_1976]] [[Buttsworth et al 2017][research_buttsworth_stern_2017]] [[C. et al 2011][research_c_battista_2011]] [[Calder et al 2026][research_calder_yackoub_2026]] [[Callan and Marusic 2000][research_callan_marusic_2000]] [[Callan and Marusic 2001][research_callan_marusic_2001]] [[Carroll 1982][research_carroll_1982]] [[Chen 2017][research_chen_2017_b]] [[Chen and Bultman 2004][research_chen_bultman_2004]] [[Chen and Liu 2014][research_chen_liu_2014]] [[Cheng et al 2017][research_cheng_dong_2017]] [[Chokani 2001][research_chokani_2001]] [[Chrusciel 1976][research_chrusciel_1976]] [[Craig 2022][research_craig_2022]] [[Crumpton 2024][research_crumpton_2024]] [[Danberg et al 1964][research_danberg_schroth_1964]] [[Daum 1963][research_daum_1963]] [[Deegan et al 2018][research_deegan_duan_2018]] [[Deepak et al 2006][research_deepak_jagadeesh_2006]] [[Development of the Shock 1962][research_development_of_1962]] [[Diagnostic Studies of a 1962][research_diagnostic_studies_1962]] [[Diggins 1951][research_diggins_1951]] [[Draper and Lee 2019][research_draper_lee_2019]] [[Dukowicz 1968][research_dukowicz_1968]] [[Edelman and Spadaccini 1969][research_edelman_spadaccini_1969]] [[Enkenhus and Parazzoli 1969][research_enkenhus_parazzoli_1969]] [[Erdos 1998][research_erdos_1998]] [[Eschenbach and Skinner 1961][research_eschenbach_skinner_1961]] [[Fitch 1966][research_fitch_1966]] [[Folck and Smith 1969][research_folck_smith_1969]] [[Fujita et al 2011][research_fujita_suzuki_2011]] [[Gates et al 1999][research_gates_adrezin_1999]] [[Giant liquid rheostat for 1955][research_giant_liquid_1955]] [[Goldbaum 1956][research_goldbaum_1956]] [[Gregorek and Lee 1962][research_gregorek_lee_1962]] [[Grossir 2015][research_grossir_2015]] [[Grossir and Rambaud 2014][research_grossir_rambaud_2014]] [[Hackett 1992][research_hackett_1992]] [[Hamner 2003][research_hamner_2003]] [[Harris and Albacete 1964][research_harris_albacete_1964]] [[Hasegawa 2025][research_hasegawa_2025]] [[Henckels and Maurer][research_henckels_maurer]] [[Henshall and Brower 1962][research_henshall_brower_1962]] [[Herdy 2026][research_herdy_2026]] [[Hermann 1950][research_hermann_1950]] [[Hertzberg et al 1961][research_hertzberg_wittliff_1961]] [[Hirsch et al 2023][research_hirsch_grossir_2023]] [[Hyper-X flight engine ground testing for X-43 flight risk reduction][research_hyperx_ground_test]] [[Hypersonic Ground Test Requirements 2002][research_hypersonic_ground_2002]] [[Hypersonic Wind Tunnel 1949][research_hypersonic_wind_1949]] [[Initial Results from a 1962][research_initial_results_1962]] [[Johnson et al 1970][research_johnson_josepha_1970]] [[Kalkhoran and Otugen 1994][research_kalkhoran_otugen_1994]] [[Kennell et al 2015][research_kennell_neely_2015]] [[Knauss et al 1999][research_knauss_riedel_1999]] [[Knight and Naiman 2009][research_knight_naiman_2009]] [[Koppenwallner 1968][research_koppenwallner_1968]] [[Korte 1992][research_korte_1992]] [[Korte 2000][research_korte_2000]] [[Korte and Hodge 1994][research_korte_hodge_1994]] [[Korte et al 1991][research_korte_kumar_1991]] [[Legge 1995][research_legge_1995]] [[Leighton 1964][research_leighton_1964]] [[Li et al 2011][research_li_huang_2011]] [[Li et al 2022][research_li_liu_2022]] [[Liu et al 2019][research_liu_song_2019]] [[Liu et al 2019][research_liu_li_2019]] [[Liu et al 2025][research_liu_xu_2025]] [[Lobb et al 1955][research_lobb_winkler_1955]] [[Lockman, W. K. 1967][research_lockmanwk_1967]] [[MacKenzie 1967][research_mackenzie_1967]] [[Maddalena and Gopal 2023][research_maddalena_gopal_2023]] [[Markova et al 2017][research_markova_aksenov_2017]] [[Matthews 1992][research_matthews_1992]] [[Matthews and Trimmer 1969][research_matthews_trimmer_1969]] [[Maxwell 2017][research_maxwell_2017_b]] [[Maxwell 2019][research_maxwell_2019]] [[Maxwell and Goodwin 2018][research_maxwell_goodwin_2018]] [[Maxwell and Goodwin 2018][research_maxwell_goodwin_2018_b]] [[Maxwell and Goodwin 2018][research_maxwell_goodwin_2018_c]] [[McConnell 2004][research_mcconnell_2004]] [[McKenzie and Fletcher 1993][research_mckenzie_fletcher_1993]] [[McQuellin and Buttsworth 2024][research_mcquellin_buttsworth_2024]] [[Measurement of wind pressure 2015][research_measurement_of_2015]] [[Meyer 1958][research_meyer_1958]] [[Mikkelsen and Long 2005][research_mikkelsen_long_2005]] [[Miles 2003][research_miles_2003]] [[Miles and Brown 2002][research_miles_brown_2002]] [[Nagamatsu et al 1961][research_nagamatsu_sheer_1961]] [[NASA Glenn Research Center's 2002][research_nasa_glenn_2002]] [[Nelson 1967][research_nelson_1967]] [[Nishimura 2014][research_nishimura_2014]] [[Norfleet and Loper 1966][research_norfleet_loper_1966]] [[Ozawa et al 2014][research_ozawa_suzuki_2014]] [[Panfilov et al 2021][research_panfilov_sevchenko_2021]] [[Parise 1992][research_parise_1992]] [[Payne and McConnell 2004][research_payne_mcconnell_2004]] [[Penland and Romeo 1971][research_penland_romeo_1971]] [[Pope and Maydew 1959][research_pope_maydew_1959]] [[Principles of Hypersonic Test 2002][research_principles_of_2002]] [[Radiatively driven hypersonic wind 1994][research_radiatively_driven_1994]] [[Rault 1992][research_rault_1992_b]] [[Resch et al 1992][research_resch_hedlund_1992]] [[Research Instrumentation Requirements for 1974][research_research_instrumentation_1974]] [[Richards 1979][research_richards_1979]] [[Scaggs et al 1963][research_scaggs_burggraf_1963]] [[Scaggs et al 1992][research_scaggs_neumann_1992]] [[Schindel 2005][research_schindel_2005]] [[Schneider 2000][research_schneider_2000]] [[Schneider 2009][research_schneider_2009]] [[Segal 2011][research_segal_2011]] [[Shang][research_shang]] [[Shantz 1953][research_shantz_1953]] [[Shepheard 1965][research_shepheard_1965]] [[Shope 2006][research_shope_2006]] [[Shreeve et al 1961][research_shreeve_lord_1961]] [[Simmons 2000][research_simmons_2000]] [[Simmons et al 1992][research_simmons_nelson_1992]] [[Simmons et al 1995][research_simmons_nelson_1995]] [[Sivells 1963][research_sivells_1963]] [[Sivells 1969][research_sivells_1969]] [[Slavick and Hiremath 2023][research_slavick_hiremath_2023]] [[Smith 1953][research_smith_1953]] [[Smith and Carver 1993][research_smith_carver_1993]] [[Spearman 2003][research_spearman_2003]] [[Specker and Brinkley 1983][research_specker_brinkley_1983]] [[Spekreijse 1991][research_spekreijse_1991]] [[Staack and De 2000][research_staack_de_2000]] [[Stalker 1992][research_stalker_1992]] [[Stallings and Hartman 1981][research_stallings_hartman_1981]] [[Stetson and Sawyer 1977][research_stetson_sawyer_1977]] [[Summerfield 1992][research_summerfield_1992]] [[Suppe 2000][research_suppe_2000]] [[Surget and Dunet 1993][research_surget_dunet_1993]] [[Surzhikov 2021][research_surzhikov_2021]] [[Surzhikov 2021][research_surzhikov_2021_b]] [[Sylvester 1967][research_sylvester_1967]] [[Taguchi et al 2014][research_taguchi_harada_2014]] [[Takahashi et al 2023][research_takahashi_oki_2023]] [[Tanno et al 2015][research_tanno_komuro_2015]] [[Test Method for Wind][research_test_method]] [[Test Method for Wind 1900][research_test_method_1900]] [[Test Method for Wind 2009][research_test_method_2009]] [[Testing Methods and Wind 2009][research_testing_methods_2009]] [[The AEDC Hypervelocity Wind 2002][research_the_aedc_2002]] [[The ONERA F4 High-Enthalpy 2002][research_the_onera_2002]] [[The SCIROCCO 70-MW Plasma 2002][research_the_scirocco_2002]] [[Thomas and Perlbachs 1967][research_thomas_perlbachs_1967]] [[Thomas et al 1969][research_thomas_martellucci_1969]] [[Tirres et al 2002][research_tirres_bradley_2002]] [[Tirtey et al 2006][research_tirtey_walpot_2006]] [[Trimmer et al 1986][research_trimmer_caryjr_1986]] [[Tuohy 2006][research_tuohy_2006]] [[van Hoffen 2024][research_vanhoffen_2024]] [[van Hoffen et al 2024][research_vanhoffen_buttsworth_2024]] [[Varwig 1963][research_varwig_1963]] [[Vicente and Foy 1963][research_vicente_foy_1963]] [[Vicente and Foy 1963][research_vicente_foy_1963_b]] [[Wagner and Dale 1985][research_wagner_dale_1985]] [[Walchner et al 1969][research_walchner_sawyer_1969]] [[Wang 2017][research_wang_2017]] [[Ward et al 1977][research_ward_baltakis_1977]] [[Watari et al 2006][research_watari_hirabayashi_2006]] [[Watt and Aronson 1964][research_watt_aronson_1964]] [[Weeks 1969][research_weeks_1969]] [[Weeks 1970][research_weeks_1970]] [[Wegener and Lobb 1952][research_wegener_lobb_1952]] [[Wilkinson and Wilkinson 1997][research_wilkinson_wilkinson_1997]] [[Wilson 1990][research_wilson_1990]] [[Wind Tunnel Test Techniques 2024][research_wind_tunnel_2024]] [[Wing][research_wing]] [[Winkler 1952][research_winkler_1952]] [[Yang et al 2020][research_yang_zhou_2020]] [[Yang et al 2024][research_yang_wang_2024]] [[Yorita 2016][research_yorita_2016]] [[Yu and Newman 2003][research_yu_newman_2003]] [[Zeitoun et al 1991][research_zeitoun_colas_1991]] [[Zhao 2013][research_zhao_2013]] [[Zhao 2021][research_zhao_2021_e]] [[Zhu and Li 2023][research_zhu_li_2023]] [[Zou et al 2021][research_zou_zhang_2021]]

### Fuel as coolant, and the endothermic heat sink

**The coupling that makes a hydrocarbon scramjet possible and nearly impossible at once.** Endothermic fuels, catalytic cracking, coking, thermal stability and regenerative cooling. **The X-51A carried 270 pounds of JP-7 and that same 270 pounds was the entire heat sink aboard**, so the fuel had to cool the engine on its way to being burned in it.

**206 records.** [[Aircraft Thermal Management System][research_aircraft_thermal]] [[Appeldoorn and Tao 1966][research_appeldoorn_tao_1966]] [[Appeldoorn and Tao 1967][research_appeldoorn_tao_1967]] [[Beery et al 1975][research_beery_clodfelter_1975]] [[Bejan 2010][research_bejan_2010]] [[Berezovik and Tikhonov 1980][research_berezovik_tikhonov_1980]] [[Bergholz and Hitch 1992][research_bergholz_hitch_1992]] [[Billingsley et al 2010][research_billingsley_edwards_2010]] [[Bouchez and Beyer 2008][research_bouchez_beyer_2008]] [[Bouchez and Beyer 2009][research_bouchez_beyer_2009]] [[Bouchez et al 1998][research_bouchez_montazel_1998]] [[Browne et al 2021][research_browne_rasmussen_2021]] [[Bucher and Bradley 1975][research_bucher_bradley_1975]] [[Cairns and Tevebaugh 1963][research_cairns_tevebaugh_1963]] [[Cao et al 2022][research_cao_lee_2022]] [[Capparelli et al 2026][research_capparelli_unternbaumen_2026]] [[Carrico 2009][research_carrico_2009]] [[Castaldi et al 2006][research_castaldi_leylegian_2006]] [[Chen 2023][research_chen_2023]] [[Chen et al 2026][research_chen_zheng_2026]] [[Cisneros-Garibay et al 2020][research_cisnerosgaribay_buchta_2020]] [[Colman et al 1968][research_colman_mayell_1968]] [[Conversion of coal to 2004][research_conversion_of_2004]] [[Corso and V. 1966][research_corso_v_1966]] [[Coutant and Keigley 1988][research_coutant_keigley_1988]] [[Crachi et al 2024][research_crachi_pizzarelli_2024]] [[Dai et al 2024][research_dai_li_2024]] [[Darrah 1988][research_darrah_1988]] [[Dinda et al 2021][research_dinda_vuchuru_2021]] [[Diskin, Glenn S. et al 1987][research_diskinglenns_jachimowskicj_1987]] [[Dittert and Kütemeyer 2017][research_dittert_kutemeyer_2017]] [[Dubinin et al 2009][research_dubinin_fink_2009]] [[Duvall et al 1985][research_duvall_hale_1985]] [[Edwards et al 2006][research_edwards_dewitt_2006]] [[Efficient thermal management of 2002][research_efficient_thermal_2002]] [[Endothermic Reactions][research_endothermic_reactions]] [[Endothermic Reactions 2006][research_endothermic_reactions_2006]] [[Endothermic reactors for an 1996][research_endothermic_reactors_1996]] [[Felderman et al 2003][research_felderman_shope_2003]] [[Fischer 2006][research_fischer_2006]] [[Fujioka et al 2017][research_fujioka_hirokawa_2017]] [[Gabrys and Smith 1974][research_gabrys_smith_1974]] [[Gao et al 2024][research_gao_sun_2024]] [[Gasner et al 1992][research_gasner_foster_1992]] [[George 1963][research_george_1963]] [[Gibbons et al 2021][research_gibbons_damm_2021]] [[Glassman 1998][research_glassman_1998]] [[Glickstein, M. R. and Spadaccini, L. J. 1997][research_glicksteinmr_spadaccinilj_1997]] [[Gopinath et al 2015][research_gopinath_vignesh_2015]] [[Gunning et al 1954][research_gunning_luner_1954]] [[Gunning et al 1954][research_gunning_luner_1954_b]] [[Guo et al 2022][research_guo_pang_2022]] [[Guo et al 2023][research_guo_pang_2023]] [[Guoliang et al 2017][research_guoliang_cong_2017]] [[Guven et al 1996][research_guven_dane_1996]] [[Gyulikhandanov and Khoroshailov 1971][research_gyulikhandanov_khoroshailov_1971]] [[Habrard et al 2025][research_habrard_pommierbudinger_2025]] [[Han et al 2024][research_han_wang_2024]] [[Harris 2004][research_harris_2004]] [[Hazarika and Ahmed 2021][research_hazarika_ahmed_2021]] [[He et al 2015][research_he_li_2015]] [[Heinrich et al 2001][research_heinrich_lucbouhali_2001]] [[Holography of JP-4 Droplets 1974][research_holography_of_1974]] [[Huang and Spadaccini 2001][research_huang_spadaccini_2001]] [[Huang and Spadaccini 2004][research_huang_spadaccini_2004]] [[Huang et al 2002][research_huang_spadaccini_2002_b]] [[Huang et al 2004][research_huang_spadaccini_2004_b]] [[Huang et al 2012][research_huang_tang_2012]] [[Hui-Sheng and Bei-Jing 2021][research_huisheng_beijing_2021]] [[Hummell and Beck 1966][research_hummell_beck_1966]] [[Impact of Copper Contamination][research_impact_of]] [[Investigation of bubble-point vapor 2005][research_investigation_of_2005]] [[Jackson et al 1995][research_jackson_corporan_1995]] [[Jeon and Park 2023][research_jeon_park_2023]] [[Jiang et al 2021][research_jiang_liu_2021]] [[Jing et al 2023][research_jing_zhang_2023]] [[Jing et al 2025][research_jing_zhang_2025]] [[Johnson et al 2001][research_johnson_bogar_2001]] [[Johnson et al 2015][research_johnson_niedbalski_2015]] [[Johnson et al 2017][research_johnson_niedbalski_2017]] [[Johnston et al 1970][research_johnston_monita_1970]] [[Kalyan et al 2022][research_kalyan_konda_2022]] [[Kanda et al 1994][research_kanda_masuya_1994]] [[Kang and Sun 2011][research_kang_sun_2011]] [[Kang et al 2025][research_kang_sung_2025]] [[Kellermann et al 2020][research_kellermann_habermann_2020]] [[Kittredge et al 1961][research_kittredge_streets_1961]] [[Kominek 2017][research_kominek_2017]] [[Kose and Celik 2023][research_kose_celik_2023]] [[Kuranov et al 2017][research_kuranov_korabelnikov_2017]] [[Lander 1968][research_lander_1968]] [[Lander and Nixon 1971][research_lander_nixon_1971]] [[Levikhin and Musteikis 2025][research_levikhin_musteikis_2025]] [[Li et al 2019][research_li_qin_2019]] [[Li et al 2021][research_li_jin_2021]] [[Li et al 2021][research_li_guo_2021]] [[Li et al 2021][research_li_hang_2021]] [[Li et al 2026][research_li_ling_2026]] [[Lillis 1987][research_lillis_1987]] [[Liquid Hydrocarbon Fuels for 2001][research_liquid_hydrocarbon_2001]] [[Liquid-Phase Reactions of Vaporizing 1978][research_liquid_phase_reactions_1978]] [[Liu and Liu 2022][research_liu_liu_2022]] [[Liu et al 2015][research_liu_bi_2015]] [[Liu et al 2022][research_liu_pan_2022]] [[Lyon 1992][research_lyon_1992]] [[Maleque 2016][research_maleque_2016]] [[Marchand 1989][research_marchand_1989]] [[Martel 1970][research_martel_1970]] [[Martel 1988][research_martel_1988]] [[Martin and Peter 2026][research_martin_peter_2026]] [[Medwick et al 1999][research_medwick_castro_1999]] [[Mi et al 2025][research_mi_wang_2025]] [[Mikhaylov 2013][research_mikhaylov_2013]] [[Mills 2001][research_mills_2001]] [[Mills 2002][research_mills_2002]] [[Minato et al 2009][research_minato_higashino_2009]] [[Minato et al 2012][research_minato_higashino_2012]] [[Miyaura et al 2018][research_miyaura_daimon_2018]] [[Modelling endothermic reactions in 1997][research_modelling_endothermic_1997]] [[Montgomery et al 2006][research_montgomery_cremer_2006]] [[Mori et al 1993][research_mori_masutani_1993]] [[Morris et al 2002][research_morris_jr_2002]] [[Moszee and Moszee 1997][research_moszee_moszee_1997]] [[Muddasar 2022][research_muddasar_2022]] [[Nalabala and Dinda 2024][research_nalabala_dinda_2024]] [[Negishi et al 2015][research_negishi_daimon_2015]] [[Nicolosi et al 2026][research_nicolosi_melone_2026]] [[Nixon and Henderson 1966][research_nixon_henderson_1966]] [[Nursal et al 2022][research_nursal_khalid_2022]] [[Oba and Gonda 2014][research_oba_gonda_2014]] [[Oster 2010][research_oster_2010]] [[Palej and Palacz 2018][research_palej_palacz_2018]] [[Palmer][research_palmer]] [[Palmer 2020][research_palmer_2020]] [[Park and Jeon 2024][research_park_jeon_2024]] [[Pelevin and Ponomarev 2018][research_pelevin_ponomarev_2018]] [[Pelevin and Ponomarev 2021][research_pelevin_ponomarev_2021]] [[Peng 2023][research_peng_2023]] [[Peng and Zhong 2022][research_peng_zhong_2022]] [[Petley and Jones 1990][research_petley_jones_1990]] [[Petley and Jones 1992][research_petley_jones_1992]] [[Price][research_price]] [[Qian et al 2016][research_qian_nan_2016]] [[Qin et al 2008][research_qin_bao_2008]] [[Qin et al 2013][research_qin_zhang_2013]] [[Ramalingam et al 2003][research_ramalingam_mahefkey_2003]] [[Reghu et al 2025][research_reghu_j_2025]] [[Robinson and McDougal 2000][research_robinson_mcdougal_2000]] [[Rogers and Kaplan 1963][research_rogers_kaplan_1963]] [[Rohl and Cowling 1965][research_rohl_cowling_1965]] [[Roland and Rumpfkeil 2017][research_roland_rumpfkeil_2017]] [[Rubey 1985][research_rubey_1985]] [[Rubey 1985][research_rubey_1985_b]] [[Ruhnke et al 1965][research_ruhnke_will_1965]] [[Schneider and Myers 1979][research_schneider_myers_1979]] [[Schneider et al 2003][research_schneider_dreizler_2003]] [[Seymour 2009][research_seymour_2009]] [[Shumway 2000][research_shumway_2000]] [[Sicard et al 2008][research_sicard_grill_2008]] [[Smits 1986][research_smits_1986]] [[Southwest Research Inst San Antonio Tx 1963][research_southwestresearchinstsanantoniotx_1963]] [[Stickels 1986][research_stickels_1986]] [[Streby et al 1999][research_streby_mathur_1999]] [[Striebich et al 2008][research_striebich_shafer_2008]] [[Sun et al 2005][research_sun_fang_2005]] [[Sun et al 2019][research_sun_li_2019]] [[Taylor and Jackson 1977][research_taylor_jackson_1977]] [[Taylor and Jackson 1978][research_taylor_jackson_1978]] [[Thomas et al 1994][research_thomas_harrison_1994]] [[Titov 1961][research_titov_1961]] [[Tomasi et al][research_tomasi_mutri]] [[Torres et al 2009][research_torres_stefanini_2009]] [[Trulove 2008][research_trulove_2008]] [[Violi 2013][research_violi_2013]] [[Vishwakarma and Rana 2025][research_vishwakarma_rana_2025]] [[Von Eckartsberg et al 2025][research_voneckartsberg_goldman_2025]] [[Vuchuru and Dinda 2024][research_vuchuru_dinda_2024]] [[Wang 2004][research_wang_2004]] [[Wang 2004][research_wang_2004_b]] [[Wang and Zhai 2023][research_wang_zhai_2023]] [[Wang et al 2006][research_wang_fang_2006]] [[Wang et al 2013][research_wang_ge_2013]] [[Wang et al 2020][research_wang_yang_2020]] [[Wang et al 2023][research_wang_liu_2023]] [[Wang et al 2024][research_wang_vohs_2024]] [[Wang et al 2025][research_wang_feng_2025_b]] [[Wang et al 2025][research_wang_yao_2025_b]] [[Wickham et al 1999][research_wickham_alptekin_1999]] [[Wickham et al 2002][research_wickham_engel_2002]] [[Wickham et al 2005][research_wickham_engel_2005]] [[Wickham et al 2008][research_wickham_engel_2008]] [[Witzmann 2006][research_witzmann_2006]] [[Xie et al 2025][research_xie_li_2025]] [[Xu et al 2023][research_xu_luan_2023]] [[Yang et al 2024][research_yang_lin_2024]] [[Yang et al 2025][research_yang_lin_2025]] [[Yang et al 2025][research_yang_gou_2025]] [[Yeh et al 2017][research_yeh_tsai_2017]] [[Yin et al 2024][research_yin_zeng_2024]] [[Yong-sheng and Rui-sen 2005][research_yongsheng_ruisen_2005]] [[Yost and Frame 2015][research_yost_frame_2015]] [[Yue et al 2010][research_yue_guiping_2010]] [[Zhang et al 2023][research_zhang_jing_2023]] [[Zhang et al 2024][research_zhang_wang_2024]] [[Zhao et al 2018][research_zhao_zhang_2018]] [[Zheng et al 2021][research_zheng_xiao_2021]]

### Shock and boundary layer interaction

**Where the flowpath's difficulties actually live.** Shock impingement on boundary layers, separation, viscous interaction and the entropy layer. **An isolator exists because this interaction exists**, and its length is chosen so that a shock train has somewhere to sit without reaching the inlet throat.

**199 records.** [[A computational study on 1994][research_a_computational_1994]] [[Adams, J. C., Jr. et al 1976][research_adamsjcjr_martindalewr_1976]] [[Agostini et al 2013][research_agostini_larcheveque_2013]] [[Altstatt 1977][research_altstatt_1977]] [[Ardonceau 1984][research_ardonceau_1984]] [[Aso et al 1992][research_aso_okuyama_1992]] [[Babinsky 2002][research_babinsky_2002]] [[Babinsky 2007][research_babinsky_2007]] [[Babinsky and Délery 2011][research_babinsky_delery_2011]] [[Ballaro and Anderson, Jr. 1991][research_ballaro_andersonjr_1991]] [[Barberis and Molton 1995][research_barberis_molton_1995]] [[Barnhart et al 1988][research_barnhart_greber_1988]] [[Batcho and Sullivan 1988][research_batcho_sullivan_1988]] [[Beketaeva et al 2016][research_beketaeva_moisseyeva_2016]] [[Benay 2003][research_benay_2003]] [[Benay and Pot 1986][research_benay_pot_1986]] [[Bergier][research_bergier]] [[Bhagwandin and DeSpirito 2011][research_bhagwandin_despirito_2011]] [[Bhanderi and Babinsky 2005][research_bhanderi_babinsky_2005]] [[Bogdonoff 1990][research_bogdonoff_1990]] [[Bohning and Doerffer 2002][research_bohning_doerffer_2002]] [[Bourgoing and Benay 2005][research_bourgoing_benay_2005]] [[Boyd 2004][research_boyd_2004]] [[Brown et al 1986][research_brown_kussoy_1986]] [[Brown, James L. 2014][research_brownjamesl_2014]] [[Bur et al 2002][research_bur_benay_2002]] [[Burt and Josyula 2013][research_burt_josyula_2013]] [[Candler 2011][research_candler_2011]] [[Canoville and Lewis 2025][research_canoville_lewis_2025]] [[Carroll and Dutton 1989][research_carroll_dutton_1989]] [[Chakravarty and Narayanaswamy 2026][research_chakravarty_narayanaswamy_2026]] [[Chandler 2003][research_chandler_2003]] [[Chen et al 2016][research_chen_yao_2016]] [[Chen et al 2026][research_chen_mao_2026]] [[Chern et al 2014][research_chern_lobser_2014]] [[Comfort and Todisco 1969][research_comfort_todisco_1969]] [[Comparison of flowfield surveys 1994][research_comparison_of_1994]] [[Cresci and Rubin 1980][research_cresci_rubin_1980]] [[Cui et al 2022][research_cui_jia_2022]] [[Damazo et al 2012][research_damazo_ziegler_2012]] [[Davis 2015][research_davis_2015]] [[De Tullio and Sandham 2012][research_detullio_sandham_2012]] [[Debiève and Dupont 2009][research_debieve_dupont_2009]] [[Degrez and Ginoux 1983][research_degrez_ginoux_1983]] [[Degrez and Ginoux 1987][research_degrez_ginoux_1987]] [[Deshpande and Poggie 2017][research_deshpande_poggie_2017]] [[Deshpande and Poggie 2020][research_deshpande_poggie_2020]] [[Deshpande and Poggie 2021][research_deshpande_poggie_2021]] [[Direct numerical simulations of 2023][research_direct_numerical_2023]] [[Dolling 1993][research_dolling_1993]] [[Dolling 2000][research_dolling_2000]] [[Dolling and Gramann 1986][research_dolling_gramann_1986]] [[Drikakis and Rana 2015][research_drikakis_rana_2015]] [[Du et al 2022][research_du_shen_2022]] [[Dunagan][research_dunagan]] [[Dupont et al 2011][research_dupont_debieve_2011]] [[Effects of chemical nonequilibrium 1969][research_effects_of_1969]] [[Effects of wind-tunnel disturbances 1972][research_effects_of_1972]] [[Erb and Hosder 2018][research_erb_hosder_2018]] [[Fedioun and Orlik 2012][research_fedioun_orlik_2012]] [[Felippe da Silva Lui][research_felippedasilvalui]] [[Ferrier et al 2006][research_ferrier_fedioun_2006]] [[Gaglio and Bevilacqua 2026][research_gaglio_bevilacqua_2026]] [[Garrison et al 1994][research_garrison_settles_1994]] [[Gawehn et al 2022][research_gawehn_schleutker_2022]] [[Ge and Gan 2026][research_ge_gan_2026]] [[Gerolymos et al 2003][research_gerolymos_sauret_2003]] [[Giehler et al 2023][research_giehler_grenson_2023]] [[Glass 2003][research_glass_2003]] [[Grasso and Falconi 1993][research_grasso_falconi_1993]] [[Gupta][research_gupta_b]] [[Hadjadj and Dussauge 2009][research_hadjadj_dussauge_2009]] [[Hallgren and Anderson, Jr. 1991][research_hallgren_andersonjr_1991]] [[Hamed, A. and Kumar, Ajay 1992][research_hameda_kumarajay_1992]] [[Harney and Petrie 1971][research_harney_petrie_1971]] [[Harvey 2011][research_harvey_2011]] [[Hatayama et al 2025][research_hatayama_tanaka_2025]] [[Hillier and Netterfield 1990][research_hillier_netterfield_1990]] [[Holden 1970][research_holden_1970]] [[Holden 1972][research_holden_1972]] [[Holden 1977][research_holden_1977]] [[Holden 2000][research_holden_2000]] [[Holden 2011][research_holden_2011]] [[Holden et al 2001][research_holden_wadhams_2001]] [[Holden et al 2010][research_holden_wadhams_2010]] [[Horstman 1987][research_horstman_1987]] [[Horstman 1991][research_horstman_1991]] [[Hung and Buning 1984][research_hung_buning_1984]] [[Hung and Maccormack 1978][research_hung_maccormack_1978]] [[Hunt and Nixon 1995][research_hunt_nixon_1995]] [[Hypersonic Viscous Interactions 2006][research_hypersonic_viscous_2006]] [[Hypersonic Viscous Interactions 2019][research_hypersonic_viscous_2019]] [[Inger 1984][research_inger_1984]] [[Inger 1995][research_inger_1995_d]] [[Inger 2011][research_inger_2011]] [[Johnston and Candler 2023][research_johnston_candler_2023]] [[Kaneko and Nakamura 1999][research_kaneko_nakamura_1999]] [[Kaneko et al 2000][research_kaneko_menshov_2000]] [[Kendall 1974][research_kendall_1974]] [[Kimmel et al 2011][research_kimmel_adamczak_2011]] [[Kimmel, Roger L. and Prabhu, Dinesh 2015][research_kimmelrogerl_prabhudinesh_2015]] [[Knight 2015][research_knight_2015]] [[Knight and Kianvashrad 2023][research_knight_kianvashrad_2023]] [[Knight and Zheltovodov 2011][research_knight_zheltovodov_2011]] [[Kokkinakis et al 2023][research_kokkinakis_khujadze_2023]] [[Kong et al 2024][research_kong_liang_2024]] [[Kuntz et al 1986][research_kuntz_amatucci_1986]] [[Kuntz et al 1987][research_kuntz_amatucci_1987]] [[Kussoy, M. I. et al 1993][research_kussoymi_horstmankc_1993]] [[Kussoy, Marvin I. and Horstman, Clifford C. 1989][research_kussoymarvini_horstmancliffordc_1989]] [[Lau 2007][research_lau_2007]] [[Law 1975][research_law_1975]] [[Law 1976][research_law_1976]] [[Lee and Gross 2021][research_lee_gross_2021]] [[Lee and Gross 2022][research_lee_gross_2022]] [[Lee et al 2005][research_lee_kawamura_2005]] [[Leger and Poggie 2014][research_leger_poggie_2014]] [[Levy et al 1977][research_levy_shamroth_1977]] [[Li 1977][research_li_1977]] [[Li 2019][research_li_2019]] [[Li and Shi 1993][research_li_shi_1993]] [[Liou et al 2000][research_liou_huang_2000]] [[Liu and Squire 1986][research_liu_squire_1986]] [[Liu et al 2023][research_liu_cao_2023]] [[Louda and Příhoda 2018][research_louda_prihoda_2018]] [[Lugrin][research_lugrin]] [[Malik][research_malik]] [[Mateer et al 1976][research_mateer_brosh_1976]] [[Matsuo et al 2023][research_matsuo_kim_2023]] [[McElderry 1973][research_mcelderry_1973]] [[McLean and Matoi 1986][research_mclean_matoi_1986]] [[Mee][research_mee]] [[Mikulla and Horstman 1976][research_mikulla_horstman_1976]] [[Mittal et al 2026][research_mittal_shahriar_2026]] [[Moulic 1963][research_moulic_1963]] [[Munuswamy and Govardhan 2022][research_munuswamy_govardhan_2022]] [[Murray and Hillier 2009][research_murray_hillier_2009]] [[Murugan and Govardhan 2016][research_murugan_govardhan_2016]] [[Namatsaliuk et al 2025][research_namatsaliuk_donato_2025]] [[Numerical Analysis of Two-Dimensional 2015][research_numerical_analysis_of_2015]] [[Ogawa and Babinsky 2008][research_ogawa_babinsky_2008]] [[Optimization design of dual 2023][research_optimization_design_2023]] [[Orlik et al 2009][research_orlik_fedioun_2009]] [[Orlik et al 2011][research_orlik_fedioun_2011]] [[Pal and Roy 2024][research_pal_roy_2024]] [[Pane][research_pane]] [[Peake][research_peake]] [[Perrot and Hadjadj 2005][research_perrot_hadjadj_2005]] [[Poggie 2006][research_poggie_2006]] [[Poggie 2008][research_poggie_2008]] [[Polivanov et al 2010][research_polivanov_sidorenko_2010]] [[Polivanov et al 2016][research_polivanov_sidorenko_2016]] [[Popinski 2019][research_popinski_2019]] [[Porter and Poggie 2017][research_porter_poggie_2017]] [[Povitsky et al 2021][research_povitsky_miller_2021]] [[Quadros and Bernardini 2018][research_quadros_bernardini_2018]] [[Raghunathan and McAdam 1983][research_raghunathan_mcadam_1983]] [[Reda 1977][research_reda_1977]] [[Reshotko 1987][research_reshotko_1987]] [[Samtaney and Pullin 1998][research_samtaney_pullin_1998]] [[Sandham 2026][research_sandham_2026]] [[Schneider 2006][research_schneider_2006]] [[Schuelein 2014][research_schuelein_2014]] [[Scuderi 1978][research_scuderi_1978]] [[Settles and Dodson 1994][research_settles_dodson_1994]] [[Shang et al 1976][research_shang_hankeyjr_1976]] [[Shock Wave-Boundary Layer Interactions][research_shock_wave_boundary]] [[Sidharth and Dwivedi 2026][research_sidharth_dwivedi_2026]] [[Simeonides][research_simeonides]] [[Simmons 1989][research_simmons_1989]] [[Singh et al 1989][research_singh_tiwari_1989]] [[Stetson 1990][research_stetson_1990]] [[Stollery 1990][research_stollery_1990]] [[Szwaba and Doerffer 2017][research_szwaba_doerffer_2017]] [[Tan and Bogdonoff 1985][research_tan_bogdonoff_1985]] [[Tang et al 2025][research_tang_li_2025]] [[Threadgill and Bruce 2015][research_threadgill_bruce_2015]] [[Tong et al 2022][research_tong_duan_2022]] [[Touré and Schuelein 2017][research_toure_schuelein_2017]] [[Van Driest and Blumer 1961][research_vandriest_blumer_1961]] [[Verma et al 2014][research_verma_manisankar_2014]] [[Volpiani 2021][research_volpiani_2021]] [[Votta et al 2011][research_votta_ranuzzi_2011]] [[Wang et al 1996][research_wang_yu_1996]] [[Wang et al 2024][research_wang_gan_2024]] [[Warning and McQuilling 2022][research_warning_mcquilling_2022]] [[Wei et al 2026][research_wei_ye_2026]] [[Wideman et al 1994][research_wideman_miles_1994]] [[Wideman et al 1995][research_wideman_brown_1995]] [[Wu et al 2024][research_wu_laguarda_2024]] [[Wu et al 2026][research_wu_lagurada_2026]] [[Yan et al 2020][research_yan_wu_2020]] [[Yoon and Chung 1996][research_yoon_chung_1996]] [[Zhang et al 2020][research_zhang_chen_2020]] [[Zhang et al 2026][research_zhang_zong_2026]] [[Zhang et al 2026][research_zhang_zong_2026_b]] [[Zheltovodov and Knight 2011][research_zheltovodov_knight_2011]] [[Zhong and Lee 1996][research_zhong_lee_1996]] [[Zuo et al 2023][research_zuo_cui_2023]]

### The waverider shape and compression lift

**The name on the aeroplane, and a smaller literature than the name suggests.** Waverider generation from conical and osculating flowfields, compression lift, shock-attached leading edges and the lift-to-drag ratio such shapes reach. **The shape exists to ride its own shock**, which is a statement about lift and a statement about where the engine's air comes from.

**196 records.** [[Aerodynamic analysis of hypersonic waverider aircraft][research_waverider_aero_analysis]] [[Aerodynamic performance and flow-field characteristics of two waverider-derived hypersonic cruise configurations][research_waverider_derived_performance]] [[Ames and Tang 2021][research_ames_tang_2021]] [[Appendix C Oblique Shock 2015][research_appendix_c_2015]] [[Armstrong and Latimer 1969][research_armstrong_latimer_1969]] [[Autenrieb 2023][research_autenrieb_2023]] [[Autenrieb and Fezans 2024][research_autenrieb_fezans_2024]] [[Babu 2020][research_babu_2020]] [[Baron and Efrat 1979][research_baron_efrat_1979]] [[Bedanand Mandal 2025][research_bedanandmandal_2025]] [[Ben-Dor 1978][research_bendor_1978]] [[Ben-Dor 1978][research_bendor_1978_b]] [[Ben-Dor 2001][research_bendor_2001]] [[Bielawski 2026][research_bielawski_2026]] [[Blankson and Hagseth 1993][research_blankson_hagseth_1993]] [[Blankson et al 1998][research_blankson_lewis_1998]] [[Borovoi et al 1996][research_borovoi_chinilov_1996]] [[Broadaway 1984][research_broadaway_1984]] [[Brown and Ravichandran 2013][research_brown_ravichandran_2013]] [[Buttsworth and Morgan 1995][research_buttsworth_morgan_1995]] [[Buzjurkin and Kiselev 2002][research_buzjurkin_kiselev_2002]] [[Bykerk et al 2020][research_bykerk_verstraete_2020]] [[Cao et al 2007][research_cao_zhang_2007]] [[Center et al 1991][research_center_sobieczky_1991]] [[Chauffour and Lewis 2003][research_chauffour_lewis_2003]] [[Chen et al 2019][research_chen_guo_2019]] [[Cheng and Aslam 2020][research_cheng_aslam_2020]] [[Chou et al 1996][research_chou_shen_1996]] [[Chuanzhen et al 2022][research_chuanzhen_xufei_2022]] [[Chuck and Eberhardt 1990][research_chuck_eberhardt_1990]] [[Cockrell, Charles E., Jr. 1993][research_cockrellcharlesejr_1993]] [[Cockrell, Charles E., Jr. 1994][research_cockrellcharlesejr_1994]] [[Cockrell, Charles Edward, Jr. 1994][research_cockrellcharlesedwardjr_1994]] [[Cockrell, s E, Jr et al 1995][research_cockrellsejr_huebner_1995]] [[Cramer 2001][research_cramer_2001]] [[Cui 2021][research_cui_2021]] [[Cui et al 2015][research_cui_hu_2015]] [[Dan et al 1994][research_dan_tanabe_1994]] [[de Moura and Ribeiro 2026][research_demoura_ribeiro_2026]] [[Desbordes et al 1995][research_desbordes_hamada_1995]] [[Design of a hypersonic 1993][research_design_of_1993]] [[Drummond 1958][research_drummond_1958]] [[Duran and Zeng 2026][research_duran_zeng_2026]] [[Edquist and Lewis 1993][research_edquist_lewis_1993]] [[Emanuel 1992][research_emanuel_1992]] [[Emanuel 1992][research_emanuel_1992_b]] [[Emanuel and Yi 2000][research_emanuel_yi_2000]] [[Ferguson and Anderson, Jr. 1993][research_ferguson_andersonjr_1993]] [[Ferguson et al 2015][research_ferguson_dasque_2015]] [[Ferguson et al 2015][research_ferguson_dhanasar_2015]] [[Finley and Cockrell 1995][research_finley_cockrell_1995]] [[Fort and Pratt 1990][research_fort_pratt_1990]] [[Ghosh and Ogawa 2022][research_ghosh_ogawa_2022]] [[Giampetro 2026][research_giampetro_2026]] [[Giampetro et al 2026][research_giampetro_lindau_2026]] [[Gillum et al 1994][research_gillum_kammeyer_1994]] [[Glass and Sislian 1994][research_glass_sislian_1994]] [[Gusev and Chinilov 2003][research_gusev_chinilov_2003]] [[Guzmán-Bohórquez et al 2025][research_guzmanbohorquez_greco_2025]] [[Hagseth, Paul E. and Blankson, Isaiah M. 1993][research_hagsethpaule_blanksonisaiahm_1993]] [[Hamed 1993][research_hamed_1993]] [[Han et al 2025][research_han_yu_2025]] [[Haney 1995][research_haney_1995]] [[Haney et al 1993][research_haney_cervisi_1993]] [[Harloff 1984][research_harloff_1984]] [[He et al 2009][research_he_le_2009]] [[Hemanth et al 2009][research_hemanth_jagadeesh_2009]] [[Higashino et al 1995][research_higashino_matsuo_1995]] [[Hossain Joy et al 2017][research_hossainjoy_rahman_2017]] [[Hu et al 2018][research_hu_jiang_2018]] [[Hugo and Lago 2022][research_hugo_lago_2022]] [[Hung 1982][research_hung_1982]] [[Inger and Rangwalla 1988][research_inger_rangwalla_1988]] [[Interpretation of waverider performance data using computational fluid dynamics][research_waverider_cfd_interpretation]] [[Isaac and Miles 1990][research_isaac_miles_1990]] [[Jade et al 2025][research_jade_jimmyjohnoe_2025]] [[Javaid and Serghides 2003][research_javaid_serghides_2003]] [[Javaid and Serghides 2004][research_javaid_serghides_2004]] [[Javaid and Serghides 2005][research_javaid_serghides_2005]] [[Kakatsios and Houzouris 1995][research_kakatsios_houzouris_1995]] [[Kim et al 1982][research_kim_rasmussen_1982]] [[Klothakis and Nikolos 2024][research_klothakis_nikolos_2024]] [[Kluwick and Stross 1984][research_kluwick_stross_1984]] [[Knittel and Lewis 2012][research_knittel_lewis_2012]] [[Kobayashi and Adachi 2015][research_kobayashi_adachi_2015]] [[Kobayashi and Adachi 2017][research_kobayashi_adachi_2017]] [[Kobayashi et al 2018][research_kobayashi_hemmi_2018]] [[Kostyukov 1980][research_kostyukov_1980]] [[Lee and Chung 2024][research_lee_chung_2024]] [[Lee and Glass 1982][research_lee_glass_1982]] [[Lewis 1991][research_lewis_1991]] [[Li 2007][research_li_2007]] [[Li and Chen 2011][research_li_chen_2011]] [[Li and Wang 2011][research_li_wang_2011]] [[Li et al 2020][research_li_cui_2020]] [[Lin and Luo 1995][research_lin_luo_1995]] [[Lin and Shen 1997][research_lin_shen_1997]] [[Ling et al 2025][research_ling_wang_2025]] [[Liu 1995][research_liu_1995]] [[Liu et al 2014][research_liu_ding_2014]] [[Liu et al 2016][research_liu_jun_2016]] [[Liu et al 2018][research_liu_zhang_2018]] [[Liu et al 2020][research_liu_bai_2020]] [[Lobbia 2015][research_lobbia_2015]] [[Lobbia and Suzuki 2003][research_lobbia_suzuki_2003]] [[Lunan 2015][research_lunan_2015]] [[Luo et al 2025][research_luo_he_2025]] [[Mani and Haney 1994][research_mani_haney_1994]] [[Maxwell 2016][research_maxwell_2016]] [[Maxwell 2017][research_maxwell_2017]] [[Maxwell and Phoenix 2017][research_maxwell_phoenix_2017]] [[Miers et al 2020][research_miers_alshehab_2020]] [[Miller et al 1997][research_miller_argrow_1997]] [[Moran et al 2023][research_moran_mcquellin_2023]] [[Morita et al 2020][research_morita_tsuchiya_2020]] [[Moura and Borges Ribeiro 2025][research_moura_borgesribeiro_2025_b]] [[Moura and Borges Ribeiro 2025][research_moura_borgesribeiro_2025_c]] [[Moura and Borges Ribeiro 2025][research_moura_borgesribeiro_2025_d]] [[Moura and Borges Ribeiro 2025][research_moura_borgesribeiro_2025_e]] [[Mursenkova et al 2021][research_mursenkova_liao_2021]] [[Mursenkova et al 2022][research_mursenkova_ivanov_2022]] [[Mursenkova et al 2023][research_mursenkova_ivanov_2023]] [[Muruganandam et al 2026][research_muruganandam_hemchandra_2026]] [[Noraml and Oblique Shock 1986][research_noraml_and_1986]] [[Normal and Oblique Shock 1986][research_normal_and_1986]] [[Norris 2006][research_norris_2006]] [[Numerical Simulations of Oblique 2006][research_numerical_simulations_2006]] [[O'Brien and Lewis 2000][research_obrien_lewis_2000]] [[Oblique Shock and Expansion 2019][research_oblique_shock_2019]] [[Oblique Shock Wave Angle 2000][research_oblique_shock_2000]] [[Oblique Shock Wave Angle 2015][research_oblique_shock_2015]] [[Oblique Shock Waves 2013][research_oblique_shock_2013]] [[Oblique Shock Waves in 1983][research_oblique_shock_1983]] [[Oblique-Shock Chart 2017][research_oblique_shock_chart_2017]] [[Olfe 1964][research_olfe_1964]] [[Palomero][research_palomero]] [[Pfaff 1968][research_pfaff_1968]] [[Piccirillo et al 2023][research_piccirillo_viola_2023]] [[Ping Li et al 2010][research_pingli_wanchunchen_2010]] [[Pisano and Whitfield 2024][research_pisano_whitfield_2024]] [[Qiao et al 2025][research_qiao_ma_2025]] [[Rahman et al 2017][research_rahman_joy_2017]] [[Rao et al 2023][research_rao_siddharth_2023]] [[Rasmussen and Stevens 1987][research_rasmussen_stevens_1987]] [[Rault 1992][research_rault_1992]] [[Rizzetta 1994][research_rizzetta_1994]] [[Rizzetta 1996][research_rizzetta_1996]] [[Rodi 2012][research_rodi_2012_b]] [[Rodi 2018][research_rodi_2018]] [[Rodi 2020][research_rodi_2020]] [[Rubins and Rhode 1963][research_rubins_rhode_1963]] [[Saheby et al 2017][research_saheby_huang_2017]] [[Santos 2008][research_santos_2008]] [[Santos 2011][research_santos_2011]] [[Santos 2012][research_santos_2012]] [[Saqib and Linshu 2007][research_saqib_linshu_2007]] [[Shi et al 1994][research_shi_tsai_1994]] [[Shi et al 2023][research_shi_niu_2023]] [[Shinde and Gaitonde 2022][research_shinde_gaitonde_2022]] [[Shvets et al 2005][research_shvets_voronin_2005]] [[Silvester and Morgan 2004][research_silvester_morgan_2004]] [[Smart and Kalkhoran 1995][research_smart_kalkhoran_1995]] [[Smart and Kalkhoran 1995][research_smart_kalkhoran_1995_b]] [[Smart et al 1998][research_smart_kalkhoran_1998]] [[Son et al 2022][research_son_son_2022]] [[Srivastava 1994][research_srivastava_1994]] [[Srivastava 1994][research_srivastava_1994_b]] [[Starkey and Lewis 1999][research_starkey_lewis_1999]] [[Starkey et al 2005][research_starkey_rankins_2005]] [[Stecklein et al 1993][research_stecklein_hasen_1993]] [[Steelant and van Duijn 2011][research_steelant_vanduijn_2011]] [[Takama 2011][research_takama_2011]] [[Takashima and Lewis 1995][research_takashima_lewis_1995]] [[Takashima and Lewis 1996][research_takashima_lewis_1996_b]] [[Takashima and Lewis 1999][research_takashima_lewis_1999]] [[Takashima et al 1996][research_takashima_lewis_1996]] [[Tarpley and Lewis 1993][research_tarpley_lewis_1993]] [[Tarpley and Lewis 1995][research_tarpley_lewis_1995]] [[Tarpley and Lewis 1995][research_tarpley_lewis_1995_b]] [[Tarpley et al 1996][research_tarpley_pines_1996]] [[Tincher and Burnett 1992][research_tincher_burnett_1992]] [[Tinney 2014][research_tinney_2014]] [[Tsai et al 1992][research_tsai_miles_1992]] [[Utheza et al 1996][research_utheza_saurel_1996]] [[Wang et al 2024][research_wang_xu_2024]] [[Waverider Aerodynamics 1986][research_waverider_aerodynamics_1986]] [[Weaver and Hunsaker 2025][research_weaver_hunsaker_2025]] [[Wu and Xiao 2009][research_wu_xiao_2009]] [[Xiao-Qing et al 2011][research_xiaoqing_zhongxi_2011]] [[Xiaoqing et al 2010][research_xiaoqing_zhongxi_2010]] [[Yan et al 2016][research_yan_liu_2016]] [[Yan et al 2018][research_yan_liu_2018]] [[Yankui et al 2005][research_yankui_dongjun_2005]] [[Yao et al 2017][research_yao_cui_2017]] [[Yatsukhno 2020][research_yatsukhno_2020]] [[Yoon, Bok-Hyun and Rasmussen, Maurice L. 1991][research_yoonbokhyun_rasmussenmauricel_1991]]

### High-temperature materials and structures

**What the vehicle is actually made of, and it is the cluster the first flight ended in.** Refractory alloys, ceramic matrix and carbon-carbon composites, coatings, thermal stress and hot structures. **The engine grew about three quarters of an inch when it got hot**, and the seal that had to accommodate that growth is what ended the first flight early.

**181 records.** [[Abdusalyamova and Rakhmatov 2002][research_abdusalyamova_rakhmatov_2002]] [[Abolhasani et al 2024][research_abolhasani_lee_2024]] [[Ali Hussein 2019][research_alihussein_2019]] [[Ault, G. M. 1965][research_aultgm_1965]] [[Barnett and Starrett 1994][research_barnett_starrett_1994]] [[Bell 1993][research_bell_1993]] [[Bendix Corp Eatontown Nj 1963][research_bendixcorpeatontownnj_1963]] [[Berkovits 1973][research_berkovits_1973]] [[Berthelot 1994][research_berthelot_1994]] [[Berthold et al 1976][research_berthold_iii_1976]] [[Blanchard 1983][research_blanchard_1983]] [[Blum 2006][research_blum_2006]] [[Bodryakov 2014][research_bodryakov_2014]] [[Bodryakov 2015][research_bodryakov_2015]] [[Bodryakov 2018][research_bodryakov_2018]] [[Boettinger 1988][research_boettinger_1988]] [[Bonnell 2000][research_bonnell_2000]] [[Bowman and Nereson 1974][research_bowman_nereson_1974]] [[Bronnikov and Vettegren 1997][research_bronnikov_vettegren_1997]] [[Chang et al 2023][research_chang_sasaki_2023]] [[Characterization of High-Temperature Materials 2014][research_characterization_of_2014]] [[Chatterjee and Venkateswararao 1982][research_chatterjee_venkateswararao_1982]] [[Chekhovskoi 2000][research_chekhovskoi_2000]] [[Choi and Alexander 2008][research_choi_alexander_2008]] [[Cámara et al 2011][research_camara_gatta_2011]] [[Dane 1942][research_dane_1942]] [[Danquah et al][research_danquah_mensah]] [[Dasgupta, et al 2001][research_dasgupta_krishnamoorthy_2001]] [[Davis 1984][research_davis_1984_b]] [[Delale and Liaw 1989][research_delale_liaw_1989]] [[Development of friction-seal materials 1957][research_development_of_1957]] [[Dismountable, slidable tube support 1996][research_dismountable_slidable_1996]] [[Diver and Pavlovic 1984][research_diver_pavlovic_1984]] [[Ds 2021][research_ds_2021]] [[Duesbery and Louat 1992][research_duesbery_louat_1992]] [[Duesbery and Louat 1994][research_duesbery_louat_1994]] [[Dvorák et al 2010][research_dvorak_kavecky_2010]] [[Dzhafarov et al 1996][research_dzhafarov_altunbas_1996]] [[Eckert and Bradt 1984][research_eckert_bradt_1984]] [[Edwards et al 1951][research_edwards_speiser_1951]] [[Eldridge 1988][research_eldridge_1988]] [[Fokin 2012][research_fokin_2012]] [[Fokin 2020][research_fokin_2020]] [[Folweiler 1962][research_folweiler_1962]] [[Franklin and Bennett 1971][research_franklin_bennett_1971]] [[Gaal 1974][research_gaal_1974]] [[Gao et al 2023][research_gao_wang_2023]] [[Gardi et al 2015][research_gardi_delvecchio_2015]] [[Gardner 1964][research_gardner_1964]] [[Glazov and Pashinkin 2001][research_glazov_pashinkin_2001]] [[Glazov et al 2002][research_glazov_pashinkin_2002]] [[Gopinath et al 2019][research_gopinath_jagadeesh_2019]] [[Gospodarev et al 1990][research_gospodarev_isakina_1990]] [[Hagy 1986][research_hagy_1986]] [[Halvarsson 1995][research_halvarsson_1995]] [[Harrison 1976][research_harrison_1976]] [[High temperature materials][research_high_temperature]] [[High-temperature investigations of the 2018][research_high_temperature_investigations_2018]] [[High-Temperature Materials and Mechanisms 2014][research_high_temperature_materials_2014_c]] [[High-Temperature Materials Chemistry and 2014][research_high_temperature_materials_2014_b]] [[High-Temperature Materials Processing 2014][research_high_temperature_materials_2014]] [[Hoch and Momin 1968][research_hoch_momin_1968]] [[Hoch and Vernardakis 1975][research_hoch_vernardakis_1975]] [[Hou et al 2024][research_hou_he_2024]] [[Huang and Kieffer 2005][research_huang_kieffer_2005]] [[Huang et al 2025][research_huang_feng_2025]] [[Huilong et al 2015][research_huilong_qiang_2015]] [[Hunter 1981][research_hunter_1981]] [[Hyers 2009][research_hyers_2009]] [[Ifflnder and Keller][research_ifflnder_keller]] [[Igari 2019][research_igari_2019]] [[Isakina et al 2000][research_isakina_prokhvatilov_2000]] [[Iwashita 2015][research_iwashita_2015]] [[Iwashita 2026][research_iwashita_2026]] [[Jardine 1930][research_jardine_1930]] [[Jayachandran and Menon 1996][research_jayachandran_menon_1996]] [[Kang and Won Kim 2019][research_kang_wonkim_2019]] [[Kelly 1972][research_kelly_1972]] [[Kelly 1972][research_kelly_1972_b]] [[Kerans 2002][research_kerans_2002]] [[Kerstan et al 2014][research_kerstan_muller_2014]] [[Kessler et al 2015][research_kessler_li_2015]] [[Khmyrov et al 2025][research_khmyrov_grigoriev_2025]] [[Kiyohashi 1998][research_kiyohashi_1998]] [[Knott 1984][research_knott_1984]] [[Konovalikhin et al 2018][research_konovalikhin_kovalev_2018]] [[Kozlovskii and Stankus 2014][research_kozlovskii_stankus_2014]] [[Kozlovskii and Stankus 2015][research_kozlovskii_stankus_2015]] [[Krikorian 1960][research_krikorian_1960]] [[Lacorre et al 2022][research_lacorre_barre_2022]] [[Li 2008][research_li_2008]] [[Li et al 2021][research_li_sun_2021]] [[Long and Jr 1992][research_long_jr_1992]] [[Low Temperature Thermal Expansion 2016][research_low_temperature_2016]] [[Lowell 1963][research_lowell_1963]] [[Magomedov 2009][research_magomedov_2009]] [[Marin et al 2021][research_marin_tombolesi_2021]] [[Marschall 2011][research_marschall_2011]] [[Marshall and Davis 2001][research_marshall_davis_2001]] [[Mazdiyasni 1989][research_mazdiyasni_1989]] [[Mazdiyasni and Chen 1988][research_mazdiyasni_chen_1988]] [[Mazdiyasni et al 1991][research_mazdiyasni_chen_1991]] [[McCarthy 2008][research_mccarthy_2008]] [[McDonald 1960][research_mcdonald_1960]] [[McLean][research_mclean]] [[McMillin 1969][research_mcmillin_1969]] [[Meier 1984][research_meier_1984]] [[Meisel and Cote 1985][research_meisel_cote_1985]] [[Mendiratta and Choudhury 1978][research_mendiratta_choudhury_1978]] [[Merriam et al 1962][research_merriam_smoluchowski_1962]] [[Merryman 1962][research_merryman_1962]] [[Metallic SEAL Rings for][research_metallic_seal]] [[Miller 1999][research_miller_1999]] [[Miller et al 2011][research_miller_nagpal_2011]] [[Miyazaki et al 1986][research_miyazaki_yoshida_1986]] [[Mu et al 2008][research_mu_zheng_2008]] [[Mukherjee and Thomson 2009][research_mukherjee_thomson_2009]] [[Nadler 2003][research_nadler_2003]] [[NbO2 crystal structure, thermal][research_nbo2_crystal]] [[Newnham 2004][research_newnham_2004]] [[Nondestructive Evaluation and Health 2014][research_nondestructive_evaluation_2014]] [[Otte et al 1963][research_otte_welch_1963]] [[Patra and Lee 2018][research_patra_lee_2018]] [[Pavlova et al 2011][research_pavlova_shtern_2011]] [[Petrov et al 1998][research_petrov_clyndyuck_1998]] [[Preliminary Thermal/Structural Analysis of 1992][research_preliminary_thermal_structural_1992]] [[Priyanka Agrawal et al 2026][research_priyankaagrawal_amitkumarsingh_2026]] [[Rabadanov and Ataev 2002][research_rabadanov_ataev_2002]] [[Rahimi et al 2026][research_rahimi_svolos_2026]] [[Raj 1987][research_raj_1987]] [[Rao 1974][research_rao_1974]] [[Rogers, D. C. et al 1976][research_rogersdc_scottro_1976]] [[Rowley and Thornton 1994][research_rowley_thornton_1994]] [[Sacks 1996][research_sacks_1996]] [[Saito 1965][research_saito_1965]] [[Sankar and Kelkar 1995][research_sankar_kelkar_1995]] [[Santhy et al 2022][research_santhy_sivakumar_2022]] [[Schnelle et al 1992][research_schnelle_hoffels_1992]] [[Schuch and Laquer 1952][research_schuch_laquer_1952]] [[Schulmeister et al 1977][research_schulmeister_hostetler_1977]] [[Seal between two elements 2011][research_seal_between_2011]] [[Seal for high-temperature applications 2019][research_seal_for_2019]] [[Sharov M. K. 2022][research_sharovmk_2022]] [[Shen et al 2025][research_shen_dongliang_2025]] [[Shirai et al 2014][research_shirai_hashimoto_2014]] [[Skinner and Johnston 1953][research_skinner_johnston_1953]] [[Smaardyk 1954][research_smaardyk_1954]] [[Smith 2011][research_smith_2011]] [[Smith and Finlayson 1978][research_smith_finlayson_1978]] [[Spedding et al 1960][research_spedding_hanak_1960]] [[Steinetz, Bruce M. 1992][research_steinetzbrucem_1992]] [[Stoloff and Jone 1997][research_stoloff_jone_1997]] [[Stroud, C. W. and Rummler, D. R. 1980][research_stroudcw_rummlerdr_1980]] [[Study on Self-compensation Design 2021][research_study_on_2021]] [[Su and Liu 2021][research_su_liu_2021]] [[Sutton et al 1997][research_sutton_chao_1997]] [[Takahashi 2012][research_takahashi_2012]] [[Tandon et al 2006][research_tandon_dumm_2006]] [[Tang et al 1991][research_tang_zhou_1991]] [[Teng et al 2012][research_teng_yu_2012]] [[Terekhov 2023][research_terekhov_2023]] [[Thermal Physics Temperature, Heat 2013][research_thermal_physics_2013]] [[Thiéblot et al 1998][research_thieblot_roux_1998]] [[Tomar 2012][research_tomar_2012]] [[Turcotte 1987][research_turcotte_1987]] [[Tyagi and Achary 2017][research_tyagi_achary_2017]] [[Uhlenbruck and Tietz 2004][research_uhlenbruck_tietz_2004]] [[Vaughan and Schwartz 1962][research_vaughan_schwartz_1962]] [[Vedula 1989][research_vedula_1989]] [[Voake et al 2024][research_voake_nermoen_2024]] [[Wakamatsu et al 2009][research_wakamatsu_kuno_2009]] [[Weber et al 1997][research_weber_kriven_1997]] [[Westinghouse Electric Corp Pittsburgh Pa 1967][research_westinghouseelectriccorppittsburghpa_1967]] [[White 2004][research_white_2004]] [[White and Andrikidis 1996][research_white_andrikidis_1996]] [[Wiedemeier and Siemers 1975][research_wiedemeier_siemers_1975]] [[Wimber 1976][research_wimber_1976]] [[Wohlleben et al 1991][research_wohlleben_schnell_1991]] [[Wu and Cheng 2005][research_wu_cheng_2005]] [[Yan 2023][research_yan_2023]] [[Yukhno et al 2021][research_yukhno_volkov_2021]]

### Airframe and propulsion as one object

**A hypersonic vehicle has no separable engine.** Airframe and propulsion integration, nozzle and afterbody expansion, installed thrust and specific impulse. **The forebody is the inlet and the afterbody is the nozzle**, so a drag bookkeeping error and a thrust bookkeeping error are the same error.

**122 records.** [[Aarnes and White 1975][research_aarnes_white_1975]] [[Aarnes and White 1975][research_aarnes_white_1975_b]] [[Anne Charmeau et al 2009][research_annecharmeau_brandoncunningham_2009]] [[Anthoine et al 2014][research_anthoine_lestrade_2014]] [[Bac 1993][research_bac_1993]] [[Barrett 1963][research_barrett_1963]] [[Bennett and Connors 1964][research_bennett_connors_1964]] [[Boswell et al 2004][research_boswell_sutherland_2004]] [[Bowman and Foy 1961][research_bowman_foy_1961]] [[Casalino and Colasurdo 2002][research_casalino_colasurdo_2002]] [[Chambers et al 2019][research_chambers_titchener_2019]] [[Chudoba 2019][research_chudoba_2019_b]] [[Clark et al 2006][research_clark_wu_2006]] [[Comparative Applicability Of Storable 1960][research_comparative_applicability_1960]] [[Coniglio][research_coniglio]] [[Dafler 1962][research_dafler_1962]] [[Daines et al 1975][research_daines_boardman_1975]] [[Davis 1984][research_davis_1984]] [[Davis 1985][research_davis_1985]] [[Denney et al 2012][research_denney_tai_2012]] [[Doty et al 2011][research_doty_camberos_2011]] [[Ducati and Giannini 1964][research_ducati_giannini_1964]] [[Ducati et al 1965][research_ducati_giannini_1965]] [[Díaz 1999][research_diaz_1999]] [[Early 2000][research_early_2000]] [[Elkoby 2005][research_elkoby_2005]] [[Estimation of Ideal Specific 2025][research_estimation_of_ideal_2025]] [[Feifel and Kerkam 1992][research_feifel_kerkam_1992]] [[Fleming et al 2004][research_fleming_olcman_2004]] [[Forrette 1964][research_forrette_1964]] [[Froning, Jr. 1986][research_froningjr_1986]] [[Fuel in high-energy rocket 1998][research_fuel_in_1998]] [[Gary and McDonald 2014][research_gary_mcdonald_2014]] [[Gregory et al 1967][research_gregory_wilcox_1967]] [[Gronland et al 1997][research_gronland_cambier_1997]] [[Hahn 2012][research_hahn_2012]] [[Hanumantha Rao 2023][research_hanumantharao_2023]] [[Hartill, W. R. et al 1978][research_hartillwr_goebeltp_1978]] [[Heiser 2007][research_heiser_2007]] [[Henderson 1987][research_henderson_1987]] [[High specific impulse propulsion 1987][research_high_specific_1987]] [[Hill et al 2004][research_hill_brown_2004]] [[Hirschel et al 2025][research_hirschel_staudacher_2025_b]] [[Howe et al 2022][research_howe_howe_2022]] [[Ignatowicz and Dąbrowski 2025][research_ignatowicz_dabrowski_2025]] [[Ilin et al 1999][research_ilin_diaz_1999]] [[Imrak et al 2021][research_imrak_karaselvi_2021]] [[Jones et al 2021][research_jones_saxer_2021]] [[Kambrath and Thuluvath 2025][research_kambrath_thuluvath_2025]] [[Kascak 1971][research_kascak_1971]] [[Klotz 1963][research_klotz_1963]] [[Lamorte et al 2011][research_lamorte_friedmann_2011]] [[Lamorte et al 2015][research_lamorte_friedmann_2015]] [[Landsbaum et al 1979][research_landsbaum_salinas_1979]] [[Langhenry and Parks 1991][research_langhenry_parks_1991]] [[Langill, Jr. 1965][research_langilljr_1965]] [[Lee et al 2018][research_lee_liou_2018]] [[Lempert and Dorofeenko 2013][research_lempert_dorofeenko_2013]] [[Lestrade et al 2017][research_lestrade_anthoine_2017]] [[Lewis 2003][research_lewis_2003_b]] [[Lewis 2010][research_lewis_2010]] [[Li and Geiselhart 2024][research_li_geiselhart_2024]] [[Li et al 2017][research_li_tan_2017]] [[Liu 1992][research_liu_1992]] [[Luce and Flowers 1961][research_luce_flowers_1961]] [[Lushchik et al 1993][research_lushchik_sizov_1993]] [[Mao 2023][research_mao_2023]] [[Marinho and de Farias 2020][research_marinho_defarias_2020]] [[May and Richey 1979][research_may_richey_1979]] [[Meintanis et al 2002][research_meintanis_bengtson_2002]] [[Mikhail 1979][research_mikhail_1979]] [[Muddamarri and M. Badgujar 2024][research_muddamarri_mbadgujar_2024]] [[Narayan and Kumar 1989][research_narayan_kumar_1989]] [[Nnenna et al 2026][research_nnenna_matthew_2026]] [[Orlin and Orlov 2019][research_orlin_orlov_2019]] [[Palumbo et al 2022][research_palumbo_palmer_2022]] [[Pande 1994][research_pande_1994]] [[Patel and Chudoba 2026][research_patel_chudoba_2026]] [[Platt and Hanner 1965][research_platt_hanner_1965]] [[Polsgrove and Adams 2002][research_polsgrove_adams_2002]] [[Polsgrove and Adams 2002][research_polsgrove_adams_2002_b]] [[Powers 1960][research_powers_1960]] [[Richey et al 1968][research_richey_stava_1968]] [[Richey et al 1983][research_richey_surber_1983]] [[Rodriguez 2007][research_rodriguez_2007]] [[Ross 1960][research_ross_1960]] [[Sankaran et al 2023][research_sankaran_venkatesh_2023]] [[Sato et al 2006][research_sato_matsuo_2006]] [[Sharma and Shenvi 2025][research_sharma_shenvi_2025]] [[Sharma and Shenvi 2026][research_sharma_shenvi_2026]] [[Sheffer and Dulikravich 1993][research_sheffer_dulikravich_1993]] [[Sheth et al 2012][research_sheth_ungar_2012]] [[Sliusariev and Bilotserkovsky 2024][research_sliusariev_bilotserkovsky_2024]] [[Smith et al 2004][research_smith_bergmann_2004]] [[Smith-Kent et al 1993][research_smithkent_ridder_1993]] [[Solomonov et al 2010][research_solomonov_milekhin_2010]] [[Specific Impulse][research_specific_impulse]] [[Specific Impulse 2008][research_specific_impulse_2008]] [[Specific Impulse 2015][research_specific_impulse_2015]] [[Squire et al 1999][research_squire_diaz_1999]] [[Sultanov and Glebov 2021][research_sultanov_glebov_2021]] [[Taheri 2020][research_taheri_2020]] [[Takahashi 2005][research_takahashi_2005]] [[Test Method for Solid][research_test_method_b]] [[Thomas et al 2010][research_thomas_czech_2010]] [[Wang and Ma 2024][research_wang_ma_2024]] [[Wang et al 1959][research_wang_anthony_1959]] [[Watson 1969][research_watson_1969]] [[Weber and Karemaa 1972][research_weber_karemaa_1972]] [[Weidner 1980][research_weidner_1980]] [[Weidner, John P. 1992][research_weidnerjohnp_1992]] [[White et al 1983][research_white_janssen_1983]] [[Wilson and Benson 1978][research_wilson_benson_1978]] [[Witte et al 2003][research_witte_huebner_2003]] [[Wright et al 2000][research_wright_foley_2000]] [[Yang et al 2025][research_yang_wang_2025]] [[Yang et al 2025][research_yang_zhang_2025]] [[Yao et al 2009][research_yao_bao_2009_b]] [[Zakharov 1994][research_zakharov_1994]] [[Zeng et al 2025][research_zeng_wang_2025]] [[Zheng et al 2019][research_zheng_zhang_2019]] [[Zolotukhin et al 2025][research_zolotukhin_price_2025]]

### Other hypersonic and aeronautical literature

**The residual, reported and not hidden.** On-subject work belonging to no cluster above. **It is unusually small for this series at roughly two percent**, which is a fact about how tightly this subject is bounded rather than a claim about the sweep.

**116 records.** [[Airbreathing Propulsion][research_airbreathing_propulsion]] [[Axdahl et al 2011][research_axdahl_kumar_2011]] [[Axdahl et al 2012][research_axdahl_kumar_2012]] [[Barlow and Wood 1987][research_barlow_wood_1987]] [[Barlow et al 1988][research_barlow_wood_1988]] [[Berger 1971][research_berger_1971]] [[Bestion 2017][research_bestion_2017]] [[Bestion 2024][research_bestion_2024]] [[Boiocchi et al 2018][research_boiocchi_galfetti_2018]] [[Bonnefond et al 1996][research_bonnefond_falempin_1996]] [[Bootle 1999][research_bootle_1999]] [[Bose 2012][research_bose_2012]] [[Bowes 1978][research_bowes_1978]] [[Bradford and Olds 1999][research_bradford_olds_1999]] [[Bucknell 1987][research_bucknell_1987]] [[Bucknell 1989][research_bucknell_1989]] [[Builder 1964][research_builder_1964]] [[Bulman and Siebenhaar 1995][research_bulman_siebenhaar_1995]] [[Burton and Carroll 2025][research_burton_carroll_2025]] [[Chen et al 2024][research_chen_liu_2024]] [[Choi et al 2002][research_choi_sasoh_2002]] [[Cohen 1968][research_cohen_1968]] [[Combustion Chemistry of Chain 1978][research_combustion_chemistry_1978]] [[Corton 1966][research_corton_1966]] [[Cox et al 1973][research_cox_cairns_1973]] [[Czysz 1988][research_czysz_1988]] [[Daines and Segal 1998][research_daines_segal_1998]] [[Dodd 1980][research_dodd_1980]] [[Dong and Li 2012][research_dong_li_2012]] [[Dugan, Jr. 1969][research_duganjr_1969]] [[Dunn 1980][research_dunn_1980]] [[Elements of Computational Engine/Airframe 1986][research_elements_of_1986]] [[Engine/Airframe Performance Matching 1989][research_engine_airframe_performance_1989]] [[Falempin and Serre 2003][research_falempin_serre_2003_b]] [[Fontijn 1987][research_fontijn_1987]] [[Friedman 1965][research_friedman_1965]] [[Friedman et al 1967][research_friedman_griffith_1967]] [[Fry, Ronald S. and Becker, Dorothy L. 2000][research_fryronalds_beckerdorothyl_2000]] [[Fry, Ronald S. and Gannaway, Mary T. 2002][research_fryronalds_gannawaymaryt_2002]] [[Fry, Ronald S. et al 1998][research_fryronalds_gannawaymaryt_1998]] [[Gany 2006][research_gany_2006]] [[Glassman and Nosek 1971][research_glassman_nosek_1971]] [[Glickstein and Powell 1987][research_glickstein_powell_1987]] [[Gubanov 2019][research_gubanov_2019]] [[Gurtin and Soner 1990][research_gurtin_soner_1990]] [[Hall 1994][research_hall_1994]] [[Heiser and Pratt 2005][research_heiser_pratt_2005]] [[Helicopter Engine/Airframe Interface Document][research_helicopter_engine_airframe]] [[Hucknall 1985][research_hucknall_1985]] [[Hucknall 1985][research_hucknall_1985_b]] [[Hueter 1999][research_hueter_1999]] [[Hutt, John J. et al 2001][research_huttjohnj_mcarthurcraig_2001]] [[Instrumentation for Airbreathing Propulsion 1974][research_instrumentation_for_1974]] [[Integrated transient thermal-structural finite 1981][research_integrated_transient_1981]] [[Kitowski 1992][research_kitowski_1992]] [[Klineberg, John M. 1989][research_klinebergjohnm_1989]] [[Kobayashi et al 2001][research_kobayashi_sato_2001]] [[Koschel 1996][research_koschel_1996]] [[Kramer and Buhler 1980][research_kramer_buhler_1980]] [[Kydd 1959][research_kydd_1959]] [[Lead-Cooled Fast Reactor LFR][research_lead_cooled_fast]] [[Levy 1982][research_levy_1982]] [[Liston and Small 1992][research_liston_small_1992]] [[Lohner and Yang 2002][research_lohner_yang_2002]] [[Lu and Mahapatra 2008][research_lu_mahapatra_2008]] [[Lynch 1968][research_lynch_1968]] [[Mace and Nyberg 1992][research_mace_nyberg_1992]] [[Mahapatra et al 2008][research_mahapatra_lu_2008]] [[McCracken 1970][research_mccracken_1970]] [[Meriwether 2005][research_meriwether_2005]] [[Michalski et al 2018][research_michalski_boust_2018]] [[Mishler and Wilkinson 1992][research_mishler_wilkinson_1992]] [[Nichols and Heikkinen 2010][research_nichols_heikkinen_2010]] [[Numerical Modeling of Combustion 1991][research_numerical_modeling_1991]] [[Ouzts et al 1992][research_ouzts_lorenzo_1992]] [[Ouzts, Peter J. et al 1993][research_ouztspeterj_lorenzocarlf_1993]] [[Powers and Robinson 1992][research_powers_robinson_1992]] [[Qi et al 1998][research_qi_wang_1998]] [[Quinn 1978][research_quinn_1978]] [[Riggins 2004][research_riggins_2004]] [[Salooja 1968][research_salooja_1968]] [[Schunk and Chung 2000][research_schunk_chung_2000]] [[Seshadri 1990][research_seshadri_1990]] [[Sforza 2017][research_sforza_2017]] [[Sforza 2017][research_sforza_2017_b]] [[Sforza 2017][research_sforza_2017_c]] [[Sforza 2017][research_sforza_2017_d]] [[Shaikh et al 2017][research_shaikh_patidar_2017]] [[Shirasu et al 1996][research_shirasu_south_1996]] [[Shklovskii and Kurt 1961][research_shklovskii_kurt_1961]] [[Stern 1983][research_stern_1983]] [[Stewart 1981][research_stewart_1981]] [[Stilp][research_stilp]] [[Strutjet Rocket-Based Combined-Cycle Engine 2001][research_strutjet_rocket_based_2001]] [[Sullins and Billig 1987][research_sullins_billig_1987]] [[Sutliff 1973][research_sutliff_1973]] [[Szema et al 2010][research_szema_liu_2010]] [[Tanatsugu and Carrick 2003][research_tanatsugu_carrick_2003]] [[Thermal Properties and Transient 1998][research_thermal_properties_1998]] [[Thermal Structural Analysis of 1992][research_thermal_structural_1992]] [[Thompson 2015][research_thompson_2015]] [[Thornton and Dechaumphai 1986][research_thornton_dechaumphai_1986]] [[Transient Thermal-Structural Analysis Using 1992][research_transient_thermal_structural_1992]] [[Transient Thermal-Structural Response of 1995][research_transient_thermal_structural_1995]] [[Turns and Kraige][research_turns_kraige]] [[Variation of natural radioactivity 1956][research_variation_of_1956]] [[Vlach 2014][research_vlach_2014]] [[Wang et al 2026][research_wang_li_2026]] [[Ward and Hewitt 1988][research_ward_hewitt_1988]] [[Weirich et al 1996][research_weirich_fogarty_1996]] [[Wilson and Wright 1977][research_wilson_wright_1977]] [[Woodward and Mesrobain 1953][research_woodward_mesrobain_1953]] [[Xue et al 1994][research_xue_bostic_1994]] [[Yan and Zhang 2026][research_yan_zhang_2026]] [[You-Quan Chang 2009][research_youquanchang_2009]] [[Zarlingo 1988][research_zarlingo_1988]]

### Computation of hypersonic flow and its validation

**How the flowpath is designed, since it cannot be flown first.** Navier-Stokes and Euler solvers, large eddy simulation, turbulence and chemistry models, grid convergence and validation against experiment. **A scramjet combustor is a turbulent reacting supersonic flow**, which is close to the hardest thing this discipline asks a code to do.

**114 records.** [[Abbass 2024][research_abbass_2024_b]] [[Abou Hweij and Azizi 2020][research_abouhweij_azizi_2020]] [[Adams 1998][research_adams_1998]] [[Advisory Group for Aerospace Research and Development 1993][research_advisorygroupforaerospaceresearchanddevelopment_1993]] [[Aiken et al 2002][research_aiken_moore_2002]] [[Aiken et al 2003][research_aiken_moore_2003]] [[Alliney et al 2025][research_alliney_dambrosio_2025]] [[Amato et al 2026][research_amato_giannino_2026]] [[Barber and Cox 1989][research_barber_cox_1989]] [[Barber and Cox, Jr. 1988][research_barber_coxjr_1988]] [[Bardina and Lombard 1987][research_bardina_lombard_1987]] [[Borelli et al 2018][research_borelli_repetto_2018]] [[Brief Review of Computational 2024][research_brief_review_2024]] [[Candler and Leyva 2022][research_candler_leyva_2022]] [[Candler and Nompelis 2002][research_candler_nompelis_2002]] [[CFD Applications to Engine/Airframe 1986][research_cfd_applications_1986]] [[Chapter 18 Near-Wall Domain 2013][research_chapter_18_2013]] [[Chapter 7 Navier-Stokes-Based Numerical 2013][research_chapter_7_2013]] [[Cherukat et al 1998][research_cherukat_na_1998]] [[Chow and Gao 2004][research_chow_gao_2004]] [[Clement 2018][research_clement_2018]] [[Computational Fluid Dynamic Methods 2009][research_computational_fluid_2009]] [[Computational Fluid Dynamics Continuity 2000][research_computational_fluid_2000_b]] [[Computational Fluid Dynamics Design 1990][research_computational_fluid_1990]] [[Computational fluid dynamics Free 2014][research_computational_fluid_2014]] [[Computational Fluid Dynamics Using 2000][research_computational_fluid_2000]] [[Computational-Fluid-Dynamic Solutions of Hypersonic 2006][research_computational_fluid_dynamic_solutions_2006]] [[Computational-Fluid-Dynamic Solutions of Hypersonic 2019][research_computational_fluid_dynamic_solutions_2019]] [[Connelly 2008][research_connelly_2008]] [[Conway and Johansson 2001][research_conway_johansson_2001]] [[Cutrone 2023][research_cutrone_2023]] [[Cutrone and Schettino 2024][research_cutrone_schettino_2024]] [[Cvrlje et al 2000][research_cvrlje_breitsamter_2000]] [[Davis 1988][research_davis_1988]] [[Daywitt et al 1993][research_daywitt_bhutta_1993]] [[Debtera 2022][research_debtera_2022]] [[DeSpirito 2009][research_despirito_2009]] [[DeSpirito 2014][research_despirito_2014]] [[Dharavath et al 2015][research_dharavath_manna_2015_b]] [[Di Giovanni and Stemmer 2018][research_digiovanni_stemmer_2018]] [[Doulati et al 2011][research_doulati_baafi_2011]] [[Edwards 2014][research_edwards_2014]] [[Farrell and Martin 1998][research_farrell_martin_1998]] [[Ferziger and Leslie 1979][research_ferziger_leslie_1979]] [[Galera et al 2006][research_galera_mohammadi_2006]] [[Garman and Visintainer 2022][research_garman_visintainer_2022]] [[Gibson et al 2016][research_gibson_armiger_2016]] [[Haley and Zhong 2017][research_haley_zhong_2017]] [[Hamba 2001][research_hamba_2001]] [[Hamba 2003][research_hamba_2003]] [[Hao and Chung 1994][research_hao_chung_1994]] [[Hejranfar and Moghadam 2011][research_hejranfar_moghadam_2011]] [[Hodge 1976][research_hodge_1976]] [[Holden et al 2008][research_holden_smolinski_2008]] [[Hooper][research_hooper]] [[Hutcheson 1976][research_hutcheson_1976]] [[Hwang 2024][research_hwang_2024]] [[Hwang and Yeo 2023][research_hwang_yeo_2023]] [[Ilie et al 2023][research_ilie_mcafee_2023]] [[Intranasal flow field, in 2015][research_intranasal_flow_2015]] [[Javadi and Aidun 2024][research_javadi_aidun_2024]] [[Jordan and Ragab 1996][research_jordan_ragab_1996]] [[Kamari et al 2020][research_kamari_tadjfar_2020]] [[Kitamura et al 2007][research_kitamura_roe_2007]] [[Knight 2002][research_knight_2002]] [[Knight and Yan 2000][research_knight_yan_2000]] [[Kong et al 2026][research_kong_chen_2026]] [[Kumar][research_kumar]] [[Kumar Sulur Loganathan 2023][research_kumarsulurloganathan_2023]] [[Labbé et al 1999][research_labbe_ryan_1999]] [[Lasseur][research_lasseur]] [[Li et al 2000][research_li_li_2000]] [[Li et al 2025][research_li_ning_2025]] [[Liu 2023][research_liu_2023]] [[Liu and Lu 2011][research_liu_lu_2011]] [[Lofthouse et al 2002][research_lofthouse_hughson_2002]] [[Majumdar 2011][research_majumdar_2011]] [[Mary and Sagaut 2001][research_mary_sagaut_2001]] [[Matsukawa 2011][research_matsukawa_2011]] [[McGrory 2001][research_mcgrory_2001]] [[Merkle 2007][research_merkle_2007]] [[Mitran 2001][research_mitran_2001]] [[Navier-Stokes Equations for Partially 2018][research_navier_stokes_equations_2018]] [[Neitzke et al 2005][research_neitzke_rudnik_2005]] [[Nichols et al 2011][research_nichols_denny_2011]] [[Nichols et al 2015][research_nichols_mcdaniel_2015]] [[Perrier and Rostand 1994][research_perrier_rostand_1994]] [[Piller][research_piller]] [[Povinelli 1991][research_povinelli_1991]] [[Pruett and Chang 1998][research_pruett_chang_1998]] [[Rizzetta and Garmann 2022][research_rizzetta_garmann_2022]] [[Rizzetta and Garmann 2023][research_rizzetta_garmann_2023]] [[Rizzetta and Visbal † 2004][research_rizzetta_visbal_2004]] [[Saric 2012][research_saric_2012]] [[Schaupp and Friedrich 2010][research_schaupp_friedrich_2010]] [[Schioppa et al 2025][research_schioppa_taywochong_2025]] [[Schmatz 1989][research_schmatz_1989]] [[Sharma et al 2020][research_sharma_ghia_2020]] [[Shvydkyi 2023][research_shvydkyi_2023]] [[Siaka and Zhang 2022][research_siaka_zhang_2022]] [[Stewart et al 1992][research_stewart_smith_1992]] [[Tanjung 2022][research_tanjung_2022]] [[Thomas et al 1991][research_thomas_dwoyer_1991]] [[Thome et al 2018][research_thome_dwivedi_2018]] [[Thompson 2025][research_thompson_2025]] [[Wang et al 2007][research_wang_feng_2007]] [[White 1993][research_white_1993]] [[Williams et al 2001][research_williams_edwards_2001]] [[Xu et al 2003][research_xu_khalid_2003]] [[Yao et al 2001][research_yao_thomas_2001]] [[Yao et al 2006][research_yao_petty_2006]] [[Zhao 2021][research_zhao_2021_d]] [[Zhong 2007][research_zhong_2007]] [[Zhou and Davidson 1995][research_zhou_davidson_1995]]

### Flight control and what the vehicle did about it

**The third flight is in this cluster.** Control surfaces, actuators, control authority, guidance and stability augmentation. **The third vehicle was lost when an upper right fin unlocked**, which is a latch rather than an aerodynamic limit and is the article's plainest example of its own thesis.

**101 records.** [[Air Force Flight Test Center Edwards Afb Ca 1974][research_airforceflighttestcenteredwardsafbca_1974]] [[Air Force Flight Test Center Edwards Afb Ca 1974][research_airforceflighttestcenteredwardsafbca_1974_b]] [[Aircraft Flight Control Actuation][research_aircraft_flight_b]] [[Aircraft Flight Control Systems][research_aircraft_flight]] [[Alvi 2012][research_alvi_2012]] [[Austin][research_austin]] [[Bahambari and Khankalantary 2023][research_bahambari_khankalantary_2023]] [[Bahm, Catherine et al 2005][research_bahmcatherine_baumannethan_2005]] [[Bao et al 2021][research_bao_wang_2021]] [[Barbera 1980][research_barbera_1980]] [[Bowles 1980][research_bowles_1980]] [[Brinda et al 2006][research_brinda_dasgupta_2006]] [[Burns 1965][research_burns_1965]] [[Cao et al 2022][research_cao_gong_2022]] [[Chang et al 2026][research_chang_seo_2026]] [[Chaussee and Rizk 1982][research_chaussee_rizk_1982]] [[Chen et al 2016][research_chen_gao_2016]] [[Chen et al 2020][research_chen_zhou_2020_c]] [[Chen et al 2021][research_chen_zhou_2021]] [[Chudoba 2019][research_chudoba_2019]] [[Cliff and Well 1991][research_cliff_well_1991]] [[Cliff et al 1992][research_cliff_well_1992]] [[Cong and Kunfeng 2017][research_cong_kunfeng_2017]] [[Davidson, J. et al 1999][research_davidsonj_lallmanf_1999]] [[Demir et al 2025][research_demir_ozturkmen_2025]] [[Diao et al 2022][research_diao_lu_2022]] [[Djanal-Mann and Murugan 2025][research_djanalmann_murugan_2025]] [[Duran 2026][research_duran_2026]] [[Falkiewicz et al 2009][research_falkiewicz_cesnik_2009]] [[Falkiewicz et al 2011][research_falkiewicz_frendreis_2011]] [[Flight Sciences Lab Inc Buffalo Ny 1964][research_flightscienceslabincbuffalony_1964]] [[Flora et al 2019][research_flora_capasso_2019]] [[Gao et al 2021][research_gao_an_2021]] [[Ghori et al 2023][research_ghori_narendar_2023]] [[Grimm 1993][research_grimm_1993]] [[Gupta][research_gupta]] [[Hattis 1990][research_hattis_1990]] [[Imado and Kuroda 1992][research_imado_kuroda_1992]] [[Ishimoto et al 1996][research_ishimoto_takizawa_1996]] [[Jackson and Coyle 1983][research_jackson_coyle_1983]] [[Janardanan and Jayakumar 2006][research_janardanan_jayakumar_2006]] [[Jeffrie and Rolston 1972][research_jeffrie_rolston_1972]] [[Ji et al 2023][research_ji_zhao_2023]] [[Jian-bo et al 2017][research_jianbo_xinghua_2017]] [[Jiang et al 2022][research_jiang_nan_2022]] [[Jie Wang et al 2012][research_jiewang_qunzong_2012]] [[Johnson et al 1981][research_johnson_portalatin_1981]] [[Kauffman et al 1990][research_kauffman_grandhi_1990]] [[Kulkarni et al 2024][research_kulkarni_shrekhar_2024]] [[Lazur et al 1999][research_lazur_sawyer_1999]] [[Li et al 2017][research_li_yu_2017]] [[Li et al 2024][research_li_ma_2024]] [[Lian et al 2013][research_lian_bai_2013]] [[Liqun et al 2017][research_liqun_chaoyang_2017]] [[Liu et al 2014][research_liu_hong_2014]] [[Liu et al 2016][research_liu_wang_2016]] [[Liu et al 2016][research_liu_liu_2016]] [[Lu 1991][research_lu_1991]] [[Lu and Zhou 2017][research_lu_zhou_2017]] [[Methodology for Investigation of][research_methodology_for]] [[Miyazawa 2000][research_miyazawa_2000]] [[Morelli 2008][research_morelli_2008]] [[Niu et al 2018][research_niu_chen_2018]] [[Ochi 2004][research_ochi_2004]] [[On ascent guidance of 1994][research_on_ascent_1994]] [[Ossmann et al 2019][research_ossmann_luspay_2019]] [[Paus and Well 1996][research_paus_well_1996]] [[Piet-Lahanier and Serre 2017][research_pietlahanier_serre_2017]] [[Preller and Smart 2012][research_preller_smart_2012]] [[Primary Flight Control Hydraulic][research_primary_flight]] [[Qian et al 2013][research_qian_sun_2013]] [[Saranathan and Grant 2016][research_saranathan_grant_2016]] [[Sayir 2006][research_sayir_2006]] [[Sayir and Sehirlioglu 2009][research_sayir_sehirlioglu_2009]] [[Schmidt and Velapoldi 1999][research_schmidt_velapoldi_1999]] [[Simon and Savage 1975][research_simon_savage_1975]] [[Strand and Ennis 2012][research_strand_ennis_2012]] [[Swann et al 1981][research_swann_duke_1981]] [[Tang et al 2018][research_tang_long_2018]] [[Vartio et al 2008][research_vartio_shaw_2008]] [[Walchner et al 1967][research_walchner_sawyer_1967]] [[Wang and Wang 2020][research_wang_wang_2020]] [[Wang et al 2015][research_wang_liu_2015]] [[Warsop and Crowther 2019][research_warsop_crowther_2019]] [[Wei-wei et al 2013][research_weiwei_leping_2013]] [[Wu and Guo 2018][research_wu_guo_2018]] [[Wu et al 2025][research_wu_yuan_2025]] [[Xia et al 2020][research_xia_chen_2020]] [[Xu Mingliang et al 2010][research_xumingliang_liuluhua_2010]] [[Xudong Liu et al 2016][research_xudongliu_lincheng_2016]] [[Xue et al 2018][research_xue_guodong_2018]] [[Yang et al 2013][research_yang_li_2013]] [[Yang et al 2014][research_yang_zhao_2014]] [[Yao and Xia 2023][research_yao_xia_2023]] [[Yoshikawa and Pan 1998][research_yoshikawa_pan_1998]] [[Yu and Chen 2011][research_yu_chen_2011]] [[Zhang and Ding 2023][research_zhang_ding_2023]] [[Zhang et al 2012][research_zhang_fan_2012]] [[Zhang et al 2022][research_zhang_zhang_2022]] [[Zhang et al 2026][research_zhang_deng_2026]] [[Zhu and Liu 2015][research_zhu_liu_2015]]

### Real gas effects and chemical nonequilibrium

**Why the combustion has to stay supersonic.** Dissociation, vibrational relaxation, chemical kinetics, high-enthalpy flow and reaction mechanisms. **Slowing Mach 5 air to subsonic before burning it would leave the stagnation temperature where it is** and put the static temperature where diatomic gases come apart, and a gas that has come apart will not release its energy again on the way out.

**91 records.** [[Agarwal 2002][research_agarwal_2002]] [[Allouche and Haoui 2006][research_allouche_haoui_2006]] [[Bellan 2012][research_bellan_2012]] [[Bhagwandin and Sahu 2023][research_bhagwandin_sahu_2023]] [[Birrer and Stemmer 2012][research_birrer_stemmer_2012]] [[Bortner 1964][research_bortner_1964]] [[Boyd 1990][research_boyd_1990]] [[Bradley and Magee 1995][research_bradley_magee_1995]] [[Bruno 1989][research_bruno_1989]] [[California Inst Of Tech Pasadena 1990][research_californiainstoftechpasadena_1990]] [[Candler 1989][research_candler_1989]] [[Candler, Graham 1989][research_candlergraham_1989]] [[Catoire 2009][research_catoire_2009]] [[Chapter 9 Model of 2013][research_chapter_9_2013]] [[Chemical and Vibrational Nonequilibrium 2006][research_chemical_and_2006]] [[Chemical and Vibrational Nonequilibrium 2019][research_chemical_and_2019]] [[Chemical Kinetics of High 1962][research_chemical_kinetics_1962]] [[Chen and Wu 2018][research_chen_wu_2018]] [[Chen et al 2012][research_chen_hu_2012]] [[Chen et al 2021][research_chen_wang_2021]] [[Chen et al 2021][research_chen_wang_2021_b]] [[Clarey and Greendyke 2018][research_clarey_greendyke_2018]] [[Combustion and Chemical Kinetics 1978][research_combustion_and_1978]] [[Elder 1980][research_elder_1980]] [[Ellison, J. C. and Johnson, C. B. 1964][research_ellisonjc_johnsoncb_1964]] [[Gao et al 2014][research_gao_jiang_2014]] [[Gay and Brehm 2025][research_gay_brehm_2025]] [[Gazaix 1992][research_gazaix_1992]] [[George S. Delwert and Georg Eltetberg 1998][research_georgesdelwert_georgeltetberg_1998]] [[Goin 1961][research_goin_1961]] [[Graber 1964][research_graber_1964]] [[Grossman, B. and Cinnella, P. 1990][research_grossmanb_cinnellap_1990]] [[Grunbok et al 2023][research_grunbok_miles_2023]] [[Gupta and Agarwal 2001][research_gupta_agarwal_2001]] [[Hansen, C. Frederick 1991][research_hansencfrederick_1991]] [[Hao et al 2016][research_hao_wang_2016]] [[Hassan et al 1992][research_hassan_candler_1992]] [[Heinbockel, J. H. and Landry, J. G. 1995][research_heinbockeljh_landryjg_1995]] [[Hornung 1991][research_hornung_1991]] [[Huffman and Davidson 1958][research_huffman_davidson_1958]] [[Josyula and Shang 1992][research_josyula_shang_1992]] [[Kang and Dunn 1972][research_kang_dunn_1972]] [[Lehoczky 1977][research_lehoczky_1977]] [[Lenard and Long 1964][research_lenard_long_1964]] [[Levy 1976][research_levy_1976]] [[Lindstedt and Markaki 2009][research_lindstedt_markaki_2009]] [[Ludwig and Sulzmann 1961][research_ludwig_sulzmann_1961]] [[Lumpkin, Iii and Chapman 1991][research_lumpkiniii_chapman_1991]] [[Ma and Zhong 1999][research_ma_zhong_1999]] [[Margaritis et al 2024][research_margaritis_scherding_2024]] [[Maus et al 1983][research_maus_griffith_1983]] [[McQuaid 2013][research_mcquaid_2013]] [[Menne et al 1994][research_menne_weiland_1994]] [[Miner and Lewis 1974][research_miner_lewis_1974]] [[Molvik, Gregory A. and Merkle, Charles L. 1989][research_molvikgregorya_merklecharlesl_1989]] [[Montagne, J.-L. et al 1988][research_montagnejl_yeehc_1988]] [[Montagne, J.-L. et al 1989][research_montagnejl_yeehc_1989]] [[Moretti and Byrne 1964][research_moretti_byrne_1964]] [[Mott and Oran 2001][research_mott_oran_2001]] [[Naumann et al 1993][research_naumann_ende_1993]] [[Non-empirical analytical model of 2019][research_non_empirical_analytical_2019]] [[Olivier et al 1993][research_olivier_vetter_1993]] [[Oswald et al 1995][research_oswald_demargne_1995]] [[Park 1996][research_park_1996]] [[Petrie 1965][research_petrie_1965]] [[Prabhu, D. K. and Tannehill, J. C. 1984][research_prabhudk_tannehilljc_1984]] [[Rajan 1970][research_rajan_1970]] [[Rouel and Richards 1975][research_rouel_richards_1975]] [[Rouel and Richards 1975][research_rouel_richards_1975_b]] [[Roy 2008][research_roy_2008]] [[Roy et al 2011][research_roy_wang_2011]] [[Sardeshmukh et al 2014][research_sardeshmukh_andersonlmatthewe_2014]] [[Scherding][research_scherding]] [[Scherding et al 2024][research_scherding_rigas_2024]] [[Stalker 1989][research_stalker_1989]] [[Stone 2024][research_stone_2024]] [[Subrata 2007][research_subrata_2007]] [[Surzhikov and Surzhikov 1997][research_surzhikov_surzhikov_1997]] [[Swigart 1963][research_swigart_1963]] [[Tam and Li 1989][research_tam_li_1989]] [[Thermodynamics of Real Gas 2010][research_thermodynamics_of_2010]] [[Varma and Zhong 2022][research_varma_zhong_2022]] [[Viscous Shock-Layer Predictions for 1983][research_viscous_shock_layer_1983]] [[von Elbe 1955][research_vonelbe_1955]] [[Wang 2007][research_wang_2007]] [[Wang 2014][research_wang_2014]] [[Wang 2014][research_wang_2014_b]] [[Welsh et al 1979][research_welsh_lawrence_1979]] [[Windisch et al 2012][research_windisch_reinartz_2012]] [[Yeh et al 2023][research_yeh_veals_2023]] [[Zhong 2000][research_zhong_2000]]

### Boost, separation and getting to the start line

**A scramjet cannot start from rest and this cluster is how the X-51A got to where it could work.** Stage and booster separation, staging dynamics and solid rocket acceleration. **A twenty-six second rocket burn supplied ninety-two percent of the vehicle's kinetic energy**, and the engine under test supplied the rest across two hundred and ten seconds.

**90 records.** [[Acton 2015][research_acton_2015]] [[Albertson et al 2012][research_albertson_tartabini_2012]] [[Allen 1964][research_allen_1964]] [[Aso et al 2018][research_aso_tani_2018]] [[Balachandar 2003][research_balachandar_2003]] [[Bertelrud et al 1992][research_bertelrud_kolodziej_1992]] [[Bing and Gong 2015][research_bing_gong_2015]] [[Bonavita et al 2026][research_bonavita_zollars_2026]] [[Bordelon et al 2003][research_bordelon_frost_2003]] [[Breitsamter et al 2001][research_breitsamter_laschka_2001]] [[Brockmann and Stefanovich 2022][research_brockmann_stefanovich_2022]] [[Burns 2020][research_burns_2020]] [[Chase et al 1978][research_chase_fisher_1978]] [[Chen 2017][research_chen_2017]] [[Chen et al 2020][research_chen_zhou_2020_d]] [[Chen et al 2020][research_chen_shen_2020]] [[Chen et al 2021][research_chen_pei_2021]] [[Choi et al 2009][research_choi_yoon_2009]] [[Dalle et al 2016][research_dalle_rogers_2016]] [[Dettling and Mcintyre 1978][research_dettling_mcintyre_1978]] [[Eggers 2003][research_eggers_2003]] [[Eklund 2004][research_eklund_2004]] [[Elchert 1982][research_elchert_1982]] [[Froning, Jr. et al 1996][research_froningjr_mckinney_1996]] [[Gea and Vicker][research_gea_vicker]] [[Gong et al 2017][research_gong_bing_2017]] [[Gottlieb et al 2024][research_gottlieb_mines_2024]] [[Guo et al 2025][research_guo_fu_2025]] [[Hank et al 2006][research_hank_franke_2006]] [[Hohn and Guelhan 2015][research_hohn_guelhan_2015]] [[Hou et al 2023][research_hou_liu_2023]] [[Jayanthi and Jain 2019][research_jayanthi_jain_2019]] [[Jeyakumar et al 2005][research_jeyakumar_biswas_2005]] [[Johnson and Sorenson 2006][research_johnson_sorenson_2006]] [[Kim et al 2023][research_kim_kim_2023]] [[Kumar et al 2018][research_kumar_penchalaiah_2018]] [[Kumar et al 2018][research_kumar_sarkar_2018]] [[Lanshin et al 1996][research_lanshin_dulepov_1996]] [[Lepsch and Naftel 1993][research_lepsch_naftel_1993]] [[Lepsch, Jr. and Naftel 1992][research_lepschjr_naftel_1992]] [[Li and Cui 2009][research_li_cui_2009]] [[Li et al 2009][research_li_cui_2009_b]] [[Li et al 2012][research_li_eggers_2012]] [[Liao et al 2023][research_liao_chu_2023]] [[Liever et al 2004][research_liever_habchi_2004]] [[Luo and Baysal 1999][research_luo_baysal_1999]] [[Maynard et al 2025][research_maynard_patel_2025]] [[McCormick et al 2010][research_mccormick_wakayama_2010]] [[McGill 2000][research_mcgill_2000]] [[Mehta et al 2012][research_mehta_bowles_2012]] [[Melville and Helmich 2021][research_melville_helmich_2021]] [[Midea 1991][research_midea_1991]] [[Morani et al 2026][research_morani_fruncillo_2026]] [[Murphy et al 2004][research_murphy_buning_2004]] [[Naftel et al 1986][research_naftel_wilhite_1986]] [[Niu et al 2017][research_niu_yuan_2017]] [[Okamoto et al 2002][research_okamoto_yamamoto_2002]] [[Pamadi et al 2004][research_pamadi_tartabini_2004]] [[Pamadi et al 2006][research_pamadi_hotchko_2006]] [[Pamadi et al 2009][research_pamadi_tartabini_2009]] [[Peng and Smith 1996][research_peng_smith_1996]] [[Qiu et al 2016][research_qiu_jia_2016]] [[Ragnoli et al 2024][research_ragnoli_savino_2024]] [[Reubush 1999][research_reubush_1999]] [[Reubush et al 2001][research_reubush_martin_2001]] [[Rizvi et al 2017][research_rizvi_linshu_2017]] [[Rothschild and Schuster 1999][research_rothschild_schuster_1999]] [[Smith and Chase 1976][research_smith_chase_1976]] [[Space systems. Launch-vehicle-to-spacecraft flight][research_space_systems]] [[Suzuki 2016][research_suzuki_2016]] [[Tarfeld 2003][research_tarfeld_2003]] [[Tracy and Wright 2020][research_tracy_wright_2020]] [[Tsukamoto et al 2003][research_tsukamoto_deturris_2003]] [[Unsteady interaction mechanism of 2023][research_unsteady_interaction_2023]] [[Wang and Wang 1997][research_wang_wang_1997]] [[Wang and Wang 2024][research_wang_wang_2024_e]] [[Wang et al 2023][research_wang_wang_2023_c]] [[Wang et al 2026][research_wang_liu_2026_d]] [[Wen et al 2027][research_wen_sun_2027]] [[Williamson et al 2026][research_williamson_pascoe_2026]] [[Wright 2015][research_wright_2015]] [[Xu et al 2015][research_xu_wu_2015]] [[Yu Li and Nai-gang Cui 2008][research_yuli_naigangcui_2008]] [[Zaehringer et al 2003][research_zaehringer_heller_2003]] [[Zhai and Yang 2020][research_zhai_yang_2020]] [[Zhang et al 2017][research_zhang_he_2017]] [[Zhang et al 2025][research_zhang_li_2025]] [[Zhao et al 2011][research_zhao_qian_2011]] [[Zhong and Wu 2021][research_zhong_wu_2021]] [[Zope et al 2026][research_zope_bhushan_2026]]

### The atmosphere and the flight condition

**The medium, named rather than assumed, and it matters more here than usual.** Standard atmosphere properties, density altitude and the speed of sound. **The two powered flights cruised at 70,000 and 60,000 feet**, a factor of 1.63 in density, so a comparison that averages them away is not a comparison.

**72 records.** [[A Properties of Standard 2006][research_a_properties_2006]] [[Appendix A Standard Atmosphere 2021][research_appendix_a_2021]] [[Appendix A. The Standard 2011][research_appendix_a_2011]] [[Appendix B Properties of 2003][research_appendix_b_2003]] [[Atmosphere standard atmosphere 2006][research_atmosphere_standard_2006]] [[B-34. U. S. Standard 1963][research_b_34_u_1963]] [[Calabia and Jin 2020][research_calabia_jin_2020]] [[Comparison of high-altitude rocket 1960][research_comparison_of_1960]] [[Comparison of high-altitude rocket 1960][research_comparison_of_1960_b]] [[Definition of the standard 1954][research_definition_of_1954]] [[Dennis P. Dykstra 1980][research_dennispdykstra_1980]] [[El-Kebir and Ornik 2020][research_elkebir_ornik_2020]] [[Essenhigh 2006][research_essenhigh_2006]] [[Everett et al 1972][research_everett_cashwell_1972]] [[Fulton 1966][research_fulton_1966]] [[Gooch 2011][research_gooch_2011]] [[Gooch 2011][research_gooch_2011_b]] [[Herbert][research_herbert]] [[High-altitude atmospheric density 1960][research_high_altitude_atmospheric_1960]] [[Hïgh-altitude atmospheric density 1960][research_high_altitude_atmospheric_1960_b]] [[ICAO Standard Atmosphere 2021][research_icao_standard_2021]] [[International Standard Atmosphere 2010][research_international_standard_2010]] [[Kang et al 2023][research_kang_zhao_2023]] [[Kang et al 2023][research_kang_meng_2023]] [[Kaushik 2018][research_kaushik_2018_b]] [[Kim 2000][research_kim_2000]] [[Kodikara 2020][research_kodikara_2020]] [[Kurzke and Halliwell 2018][research_kurzke_halliwell_2018]] [[Kurzke et al 2025][research_kurzke_halliwell_2025]] [[Lee and Aldredge 2015][research_lee_aldredge_2015]] [[Lidar complex of a 2020][research_lidar_complex_2020]] [[Minimum Performance Standard for][research_minimum_performance]] [[Minimum Performance Standard for][research_minimum_performance_b]] [[Paper, board and pulps][research_paper_board]] [[Pressures and Temperatures for 2000][research_pressures_and_2000]] [[Properties of the U.S 2014][research_properties_of_2014]] [[Properties of the U.S 2024][research_properties_of_2024]] [[Report No. 538, altitude-pressure 1935][research_report_no_1935]] [[Ross et al 1993][research_ross_law_1993]] [[Science Communication Inc Mclean Va 1960][research_sciencecommunicationincmcleanva_1960]] [[Sellers and Hunerwadel 1977][research_sellers_hunerwadel_1977]] [[Singer 1956][research_singer_1956]] [[Space environment natural and][research_space_environment]] [[Sprangle and Johnson 2015][research_sprangle_johnson_2015]] [[Standard Atmosphere][research_standard_atmosphere]] [[Standard Atmosphere 1997][research_standard_atmosphere_1997]] [[Standard Atmosphere 2005][research_standard_atmosphere_2005]] [[Standard atmosphere 2007][research_standard_atmosphere_2007]] [[standard atmosphere 2014][research_standard_atmosphere_2014]] [[Standard Atmosphere 2023][research_standard_atmosphere_2023]] [[Standard Atmosphere 2024][research_standard_atmosphere_2024]] [[Standard atmosphere chart 1927][research_standard_atmosphere_1927]] [[Standard atmosphere chart supersedes 1927][research_standard_atmosphere_1927_b]] [[Standard Atmosphere Data 1992][research_standard_atmosphere_1992]] [[standard atmosphere for preconditioning 2021][research_standard_atmosphere_2021]] [[standard atmosphere for testing 2021][research_standard_atmosphere_2021_b]] [[Standard Atmospheric Profilesa aSource 2002][research_standard_atmospheric_2002]] [[Sterne 1958][research_sterne_1958]] [[Sterne 1958][research_sterne_1958_b]] [[The Flight Environment Standard 2021][research_the_flight_2021]] [[The International Standard Atmosphere 2017][research_the_international_2017]] [[The international standard atmosphere 2026][research_the_international_2026]] [[The Standard Atmosphere 1964][research_the_standard_1964]] [[The Standard Atmosphere 1976][research_the_standard_1976]] [[U.S. Standard Atmosphere, 1976][research_us_standard_atmosphere]] [[Upper Atmosphere Re-Entry Study 1961][research_upper_atmosphere_1961]] [[US Standard Atmosphere Model 2014][research_us_standard_2014]] [[Vaughan 2003][research_vaughan_2003]] [[Wang et al 2022][research_wang_jin_2022]] [[Weimer 2022][research_weimer_2022]] [[Yager 2013][research_yager_2013]] [[Yang et al 2015][research_yang_wang_2015]]


## The Source Base

**The survey rests on 5,366 research records assembled from Crossref, the NASA Technical Reports Server and the Defense Technical Information Center**, of which 762 are report primaries, being 14.2 percent, split 134 from the first and 628 from the second. **Primacy is derived from the identifier rather than from which sweep returned the record**, after A345 found 133 of its own report primaries counted as secondary because the label was inherited from the harvest.

### Three Sweep-Store Patterns Had to Be Switched Off, and the Warning to Do So Was Written One Article Ago

**This corpus keeps a shared store of homonym patterns, and a pattern earned in one article is not automatically valid in the next.** A346 recorded `ramjet` as a contaminant, because a survey of helicopter ducted propulsors kept returning solid ducted rockets. A347 recorded `hypersonic`, `scramjet` and `missile` as contaminants of a rotorcraft survey.

**Both entries carried a written warning that they must not be reused in the articles where they are the subject**, and both named this series' hypersonic articles specifically.

**Those three patterns would have deleted 3,408 records from this article's pool, being 48.1 percent of everything harvested.** The sample includes scramjet combustor flameholding, ramjet to scramjet mode transition, waverider aerodynamics and inlet unstart prediction, which is to say the article.

**A warning addressed to a reader is not a mechanism.** The three patterns now carry tags, a caller switches them off by name, and an unknown tag raises rather than being ignored, so a typo cannot silently leave a filter armed against the article's own subject. **Every other pattern in the store stayed armed**, because turbomachinery, wind energy and atmospheric chemistry are contaminants here too.

### The Instrument Built for the Previous Article Caught Six Errors in This One

**A347 found that nine of ten inherited book identifiers pointed at unrelated works** and wrote `_lib/booklinks.py` to compare a citation's claimed title against the repository.

**It was run against this article's book list before assembly and found six of eight wrong.** The two that were right are the two carried forward from A347's verified set. **A hand-typed identifier is wrong almost every time and a verified one stays right**, which is an argument for the instrument rather than for care.

### The Aeroplane Has Almost No Literature of Its Own

**One record in 5,366 names the X-51 specifically.** That is the same finding A346 reported for the X-49 and it is a fact about programme literature rather than about the sweep. **The waverider shape has 196 records, supersonic combustion has 1,297, and the aeroplane that used both has one.**

**The programme's own report exists and could not be retrieved.** The Defense Technical Information Center holds a scramjet engine demonstrator programme report, and that repository refuses automated requests, returning a refusal rather than a document [[X-51A scramjet engine demonstrator program, Defense Technical Information Center][ref_x51_dtic_report]]. **It is cited because it exists and is named as unread.**

### The Results Probe Was Run Before the Article Was Written

**A340 through A346 all discovered at their fourth pass that the survey under-covered their own conclusions, and A347 moved that probe to the draft pass.** It was run here in both phrasings before any prose existed.

**Ten conclusions were probed and nine opened by large factors on rephrasing alone**, which is the ninth consecutive article to find that a thin measurement is usually a question about wording. **Three stayed thin enough to harvest for**, being the seal and its thermal growth at 11 records, real gas effects at 40 and high-temperature materials at 57. A supplementary sweep raised those to 126, 120 and 212.

**The first of those is the first flight's cause**, and a survey holding eleven records touching it would have been silent on this article's most concrete example of its own thesis.

## Epistemic State

### Historical Fact

The programme dates and cost, the designation date, the participating organisations, the vehicle dimensions and fuel load, the launch and boost arrangement, the four flight dates with their outcomes and recorded causes, and the burn durations. These come from the manufacturer's announcements, the specialist designation directory, the Air Force and the general press, and are consistent across them except where noted.

### Verified by Independent Derivation

**Everything in this article expressed as a number is computed from published inputs and is reproducible from them.** That covers the stagnation temperatures and their ratio, the isentropic stagnation pressure and density ratios, the dynamic pressures at both cruise conditions and the density ratio between them, the burn ratio against the X-43, the heating rate and heat load ratios, the Sutton and Graves heat flux across a range of nose radii and the radiation equilibrium temperatures it implies, the thermal penetration depths and their ratio, the isentropic area ratio and the Kantrowitz throat limit, the fuel flow rate and the air flow it implies at stoichiometric, the cooling power and its share of the fuel's combustion energy, the fuel required for a three hundred second burn, the kinetic energy shares of the booster and the scramjet, the engine growth as a fraction of vehicle length and the engine length that growth implies, the powered distance, the product of specific impulse and lift-to-drag ratio the range relation yields, the net force and net specific impulse the flight realised, the burn fractions against the plan, and the programme arithmetic.

**Seventy-two of those values are recomputed by a checker and compared against the article rather than searched for in it.**

### Analysis

The reading of duration as the quantity that converts a propulsion demonstration into a thermal one. The identification of the fuel's dual role as the configuration's binding constraint. The claim that the forebody, inlet, combustor and nozzle are one device rather than four.

### Inference

That the difficulty in this class of vehicle has moved from the engine to the structure around it, which is inferred from four flights and three failure causes and is a small sample. **Three flights is not a distribution.**

### What the Record Does Not Settle

Whether a scramjet can run for the hours an operational aircraft would need. **Two hundred and ten seconds is the longest anyone has managed and it is three and a half minutes.** Nothing in this record bears on the step from minutes to hours, and this article makes no claim about it.

## Out of Scope

Rocket propulsion other than as the booster that got this vehicle to its start line, hypersonic weapons policy and doctrine, the boost-glide vehicles that carry no engine at all, and the turbine-based combined cycle work aimed at making such a vehicle take off from a runway.

## Conclusion

**The X-51A Waverider set out to show that a scramjet could run on a fuel you can put in a tank, and it did, for two hundred and ten seconds at Mach 5.**

**What it also showed, by failing three times in three different ways, is that the engine was the part that worked.** A thermal seal, an inlet, and a fin latch ended the other flights. **The supersonic combustion the programme was named for was never the thing that stopped.**

**The reason is arithmetic and this article has done it.** A flight nineteen times longer than the X-43's, at a third the stagnation temperature and a seventh the heating rate, still absorbs nearly three times the heat. **Duration is not a scaling of the same problem. It is the arrival of a different one**, in which the structure reaches equilibrium, every joint has to hold while the engine grows a quarter of a percent, and the only coolant aboard is the fuel you are trying to burn, whose capacity to absorb heat is about a twentieth of the heat it makes.

**And after all of it, the engine added under eight percent of the vehicle's energy while a rocket added ninety-two.** That is what a cruise demonstration looks like, and it is also the size of the gap between demonstrating cruise and having an aircraft.

## References

### Books

- [Anderson, Hypersonic and high-temperature gas dynamics][book_anderson_hypersonic]
- [Anderson, Modern compressible flow][book_anderson_modern]
- [Bertin, Hypersonic aerothermodynamics][book_bertin]
- [Curran and Murthy, Scramjet propulsion][book_curran_murthy]
- [Heiser and Pratt, Hypersonic airbreathing propulsion][book_heiser_pratt]
- [Hill and Peterson, Mechanics and thermodynamics of propulsion][book_hill_peterson]
- [Raymer, Aircraft design, a conceptual approach][book_raymer]
- [Schlichting and Gersten, Boundary-layer theory][book_schlichting]

[book_anderson_hypersonic]: https://openlibrary.org/works/OL1993330W
[book_anderson_modern]: https://openlibrary.org/works/OL1993329W
[book_bertin]: https://openlibrary.org/works/OL3287053W
[book_curran_murthy]: https://openlibrary.org/works/OL23791670W
[book_heiser_pratt]: https://openlibrary.org/works/OL3932490W
[book_hill_peterson]: https://openlibrary.org/works/OL4616004W
[book_raymer]: https://openlibrary.org/works/OL17855977W
[book_schlichting]: https://openlibrary.org/works/OL11833044W

### Reference

- [Air Force Research Laboratory][ref_afrl]
- [Boeing X-51 Waverider][ref_x51_wikipedia]
- [Boeing X-51, Directory of U.S. Military Rockets and Missiles][ref_x51_designation]
- [Boeing X-51A WaveRider breaks record in first flight][ref_boeing_first_flight]
- [Boeing X-51A WaveRider sets record with successful fourth flight][ref_boeing_fourth_flight]
- [DARPA Blackswift][ref_blackswift]
- [Defense Advanced Research Projects Agency][ref_darpa]
- [Jp-7][ref_jp7]
- [Mgm-140 atacms][ref_atacms]
- [Nasa x-43][ref_x43_wikipedia]
- [Naval Air Station Point Mugu][ref_point_mugu]
- [Scramjet][ref_scramjet]
- [U.S. Standard Atmosphere][ref_us_standard_atmosphere_ref]
- [Waverider][ref_waverider]
- [X-51 scramjet engine demonstrator, GlobalSecurity][ref_x51_globalsecurity]
- [X-51A scramjet engine demonstrator program, Defense Technical Information Center][ref_x51_dtic_report]

[ref_afrl]: https://en.wikipedia.org/wiki/Air_Force_Research_Laboratory
[ref_atacms]: https://en.wikipedia.org/wiki/MGM-140_ATACMS
[ref_blackswift]: https://en.wikipedia.org/wiki/Blackswift
[ref_boeing_first_flight]: https://boeing.mediaroom.com/2010-05-26-Boeing-X-51A-WaveRider-Breaks-Record-in-1st-Flight
[ref_boeing_fourth_flight]: https://boeing.mediaroom.com/2013-05-03-Boeing-X-51A-WaveRider-Sets-Record-with-Successful-4th-Flight
[ref_darpa]: https://en.wikipedia.org/wiki/DARPA
[ref_jp7]: https://en.wikipedia.org/wiki/JP-7
[ref_point_mugu]: https://en.wikipedia.org/wiki/Naval_Air_Station_Point_Mugu
[ref_scramjet]: https://en.wikipedia.org/wiki/Scramjet
[ref_us_standard_atmosphere_ref]: https://en.wikipedia.org/wiki/U.S._Standard_Atmosphere
[ref_waverider]: https://en.wikipedia.org/wiki/Waverider
[ref_x43_wikipedia]: https://en.wikipedia.org/wiki/NASA_X-43
[ref_x51_designation]: https://www.designation-systems.net/dusrm/app4/x-51.html
[ref_x51_dtic_report]: https://apps.dtic.mil/sti/citations/ADA593742
[ref_x51_globalsecurity]: https://www.globalsecurity.org/military/systems/aircraft/x-51.htm
[ref_x51_wikipedia]: https://en.wikipedia.org/wiki/Boeing_X-51_Waverider

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
- [X-Planes: Boeing X-48][related_post_a345_boeing_x48]
- [X-Planes: Boeing X-50 Dragonfly][related_post_a347_boeing_x50]
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
- [X-Planes: Northrop Grumman X-47][related_post_a344_northrop_grumman_x47]
- [X-Planes: Northrop X-21][related_post_a318_northrop_x21]
- [X-Planes: Northrop X-4 Bantam][related_post_a301_northrop_x4]
- [X-Planes: Orbital Sciences X-34][related_post_a331_orbital_sciences_x34]
- [X-Planes: Orbital Sciences X-42][related_post_a339_orbital_sciences_x42]
- [X-Planes: Osprey X-28 Sea Skimmer][related_post_a325_osprey_x28]
- [X-Planes: Piasecki X-49 SpeedHawk][related_post_a346_piasecki_x49]
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
[related_post_a344_northrop_grumman_x47]: {% post_url 2025-11-22-x_planes_northrop_grumman_x47 %}
[related_post_a345_boeing_x48]: {% post_url 2025-11-23-x_planes_boeing_x48 %}
[related_post_a346_piasecki_x49]: {% post_url 2025-11-24-x_planes_piasecki_x49 %}
[related_post_a347_boeing_x50]: {% post_url 2025-11-25-x_planes_boeing_x50 %}

### Research

- [1st Flight Test Conference 1981][research_1st_flight_1981]
- [4th Flight Test Conference 1988][research_4th_flight_1988]
- [A computational study on 1994][research_a_computational_1994]
- [A global telemetry data 1988][research_a_global_1988]
- [A Hypersonic Ground-Test Facility 2002][research_a_hypersonic_2002_b]
- [A Hypersonic Test Capabilities 2002][research_a_hypersonic_2002]
- [A Properties of Standard 2006][research_a_properties_2006]
- [A. 2013][research_a_2013]
- [Aarnes and White 1975][research_aarnes_white_1975]
- [Aarnes and White 1975][research_aarnes_white_1975_b]
- [Abarbanel 1977][research_abarbanel_1977]
- [Abbass 2024][research_abbass_2024]
- [Abbass 2024][research_abbass_2024_b]
- [Abdel-Salam and Carson 2004][research_abdelsalam_carson_2004]
- [Abdel-Salam et al 2000][research_abdelsalam_tiwari_2000]
- [Abdel-Salam et al 2001][research_abdelsalam_tiwari_2001]
- [Abdel-Salam et al 2001][research_abdelsalam_tiwari_2001_b]
- [Abdollahi et al 2024][research_abdollahi_ranjbar_2024]
- [Abdusalyamova and Rakhmatov 2002][research_abdusalyamova_rakhmatov_2002]
- [Abedi et al 2020][research_abedi_askari_2020]
- [Abgrall 1991][research_abgrall_1991]
- [Abhishek et al 2025][research_abhishek_ramachandra_2025]
- [Abolhasani et al 2024][research_abolhasani_lee_2024]
- [Abolhassani et al 1987][research_abolhassani_tiwari_1987]
- [Abou Hweij and Azizi 2020][research_abouhweij_azizi_2020]
- [Abuaf 1976][research_abuaf_1976]
- [Achambath et al 2019][research_achambath_ramjatan_2019]
- [Acharya 2025][research_acharya_2025]
- [Acharya et al 2020][research_acharya_palies_2020]
- [Acheson and Rothnie 2009][research_acheson_rothnie_2009]
- [Acton 2015][research_acton_2015]
- [Adami and Zhu 2007][research_adami_zhu_2007]
- [Adami and Zhu 2008][research_adami_zhu_2008]
- [Adams 1967][research_adams_1967]
- [Adams 1998][research_adams_1998]
- [Adams and Rubin 1958][research_adams_rubin_1958]
- [Adams et al 1973][research_adams_johnc_1973]
- [Adams, J. C., Jr. et al 1976][research_adamsjcjr_martindalewr_1976]
- [Adams, Jr. et al 1984][research_adamsjr_martindale_1984]
- [Aditya et al 2016][research_aditya_balas_2016]
- [Adolph 1981][research_adolph_1981]
- [Advanced Fuel Research Inc East Hartford Ct 1957][research_advancedfuelresearchinceasthartfordct_1957]
- [Advisory Group for Aerospace Research and Development 1993][research_advisorygroupforaerospaceresearchanddevelopment_1993]
- [Advisory Group for Aerospace Research and Development 1997][research_advisorygroupforaerospaceresearchanddevelopment_1997]
- [Aerodynamic analysis of hypersonic waverider aircraft][research_waverider_aero_analysis]
- [Aerodynamic Heating to the 1979][research_aerodynamic_heating_1979]
- [Aerodynamic performance and flow-field characteristics of two waverider-derived hypersonic cruise configurations][research_waverider_derived_performance]
- [Aerothermodynamics of the Dual-Mode 2001][research_aerothermodynamics_of_2001]
- [Aerothermodynamics Research in the 2002][research_aerothermodynamics_research_2002]
- [Aftosmis and Baron 1989][research_aftosmis_baron_1989]
- [Agarwal 2002][research_agarwal_2002]
- [Agarwal 2011][research_agarwal_2011]
- [Agarwal and Deb 2001][research_agarwal_deb_2001]
- [Agnone 1987][research_agnone_1987]
- [Agostini et al 2013][research_agostini_larcheveque_2013]
- [Agrawal et al 2012][research_agrawal_sepka_2012]
- [Aguilera and Yu 2017][research_aguilera_yu_2017]
- [Aguilera et al 2009][research_aguilera_pang_2009]
- [Aguilera Munoz and Yu 2014][research_aguileramunoz_yu_2014]
- [Ahmed et al 2025][research_ahmed_hossain_2025]
- [Ahn et al 2026][research_ahn_yu_2026]
- [Ahuja and Hartfield 2008][research_ahuja_hartfield_2008]
- [Ahuja and Hartfield 2009][research_ahuja_hartfield_2009]
- [Aiello 1962][research_aiello_1962]
- [Aiello 1963][research_aiello_1963]
- [Aiello 1977][research_aiello_1977]
- [Aiken et al 2002][research_aiken_moore_2002]
- [Aiken et al 2003][research_aiken_moore_2003]
- [Air Force Flight Test Center Edwards Afb Ca 1970][research_airforceflighttestcenteredwardsafbca_1970]
- [Air Force Flight Test Center Edwards Afb Ca 1974][research_airforceflighttestcenteredwardsafbca_1974]
- [Air Force Flight Test Center Edwards Afb Ca 1974][research_airforceflighttestcenteredwardsafbca_1974_b]
- [Air Force Flight Test Center Edwards Afb Ca 2002][research_airforceflighttestcenteredwardsafbca_2002]
- [Air Force Test Pilot School Edwards Afb Ca 1962][research_airforcetestpilotschooledwardsafbca_1962]
- [Air Force Test Pilot School Edwards Afb Ca 1987][research_airforcetestpilotschooledwardsafbca_1987]
- [Air Force Test Pilot School Edwards Afb Ca 1990][research_airforcetestpilotschooledwardsafbca_1990]
- [Air Force Test Pilot School Edwards Afb Ca 1990][research_airforcetestpilotschooledwardsafbca_1990_b]
- [Air Force Test Pilot School Edwards Afb Ca 1993][research_airforcetestpilotschooledwardsafbca_1993]
- [Airbreathing Hypersonic Aircraft and 1997][research_airbreathing_hypersonic_1997]
- [Airbreathing Propulsion][research_airbreathing_propulsion]
- [Aircraft and Flight Test 2021][research_aircraft_and_2021]
- [Aircraft Flight Control Actuation][research_aircraft_flight_b]
- [Aircraft Flight Control Systems][research_aircraft_flight]
- [Aircraft Thermal Management System][research_aircraft_thermal]
- [Akihisa et al 2002][research_akihisa_kanda_2002]
- [Aksonov 2023][research_aksonov_2023]
- [Aksu and Uslu 2017][research_aksu_uslu_2017]
- [Ala and Ye 2024][research_ala_ye_2024]
- [Alam et al 2006][research_alam_matsuo_2006]
- [Albano et al 2013][research_albano_micheli_2013]
- [Alberico 1992][research_alberico_1992]
- [Albertson et al 2012][research_albertson_tartabini_2012]
- [Albertson, Cindy W. and Emami, Saied 2001][research_albertsoncindyw_emamisaied_2001]
- [Albertson, Cindy w. et al 2006][research_albertsoncindyw_emamisaied_2006]
- [Alex and Lijo 2021][research_alex_lijo_2021]
- [Alexander and Acharya 2024][research_alexander_acharya_2024]
- [Alexander and Acharya 2025][research_alexander_acharya_2025]
- [Alferov and Marchenko 2012][research_alferov_marchenko_2012]
- [Alferov et al 2001][research_alferov_dmitriev_2001]
- [Alferov et al 2007][research_alferov_bushmin_2007]
- [Alhussan and Garris 2005][research_alhussan_garris_2005]
- [Ali and Fujiwara 2005][research_ali_fujiwara_2005]
- [Ali et al 2000][research_ali_fujiwara_2000]
- [Ali et al 2003][research_ali_ahmed_2003]
- [Ali Hussein 2019][research_alihussein_2019]
- [Alich and Castillo 2007][research_alich_castillo_2007]
- [Alkamhawi, Hani et al 1990][research_alkamhawihani_greinertom_1990]
- [Alkandry et al 2009][research_alkandry_boyd_2009]
- [Allen 1964][research_allen_1964]
- [Allen et al 2005][research_allen_king_2005]
- [Allen et al 2007][research_allen_hauser_2007]
- [Alliney et al 2025][research_alliney_dambrosio_2025]
- [Allouche and Haoui 2006][research_allouche_haoui_2006]
- [Almeida 2021][research_almeida_2021]
- [Alsalihi and Deconinck 1991][research_alsalihi_deconinck_1991]
- [Alter, Stephen J. 2012][research_alterstephenj_2012]
- [Altstatt 1977][research_altstatt_1977]
- [Alvi 2005][research_alvi_2005]
- [Alvi 2012][research_alvi_2012]
- [Amati et al 2008][research_amati_bruno_2008]
- [Amato et al 2026][research_amato_giannino_2026]
- [Ambe Verma et al 2021][research_ambeverma_muraripandey_2021]
- [Ambe Verma et al 2021][research_ambeverma_muraripandey_2021_b]
- [Amemiya and Toriyama 2018][research_amemiya_toriyama_2018]
- [Ames and Tang 2021][research_ames_tang_2021]
- [An Assessment of Our 1964][research_an_assessment_1964]
- [An et al 2017][research_an_wang_2017]
- [An et al 2020][research_an_yang_2020]
- [An et al 2021][research_an_wang_2021]
- [An Ultrasonic Turbine Inlet 1974][research_an_ultrasonic_1974]
- [Analysis on temperature and 1998][research_analysis_on_1998]
- [Ananthapadmanaban][research_ananthapadmanaban]
- [Ananthapadmanaban and Murganandam 2016][research_ananthapadmanaban_murganandam_2016]
- [Anderson 1958][research_anderson_1958]
- [Anderson 1959][research_anderson_1959]
- [Anderson 1960][research_anderson_1960]
- [Anderson 1990][research_anderson_1990]
- [Anderson 1996][research_anderson_1996]
- [Anderson 2014][research_anderson_2014]
- [Anderson 2019][research_anderson_2019]
- [Anderson et al 1999][research_anderson_brown_1999]
- [Anderson Jr. 2006][research_andersonjr_2006]
- [Andreadis, Dean et al 2002][research_andreadisdean_drakealan_2002]
- [Andreadis, Dean et al 2003][research_andreadisdean_drakealan_2003]
- [Andrews and Gordon 1981][research_andrews_gordon_1981]
- [Andrews and Poggie 2023][research_andrews_poggie_2023]
- [Andrews et al 1994][research_andrews_trexler_1994]
- [Anhtuan D. Ngo][research_anhtuandngo]
- [Anne Charmeau et al 2009][research_annecharmeau_brandoncunningham_2009]
- [Anthoine et al 2014][research_anthoine_lestrade_2014]
- [Antonio Ferri 1964][research_antonioferri_1964]
- [Appar and Kumar 2021][research_appar_kumar_2021]
- [Appeldoorn and Tao 1966][research_appeldoorn_tao_1966]
- [Appeldoorn and Tao 1967][research_appeldoorn_tao_1967]
- [Appendix A Standard Atmosphere 2021][research_appendix_a_2021]
- [Appendix A. The Standard 2011][research_appendix_a_2011]
- [Appendix B Properties of 2003][research_appendix_b_2003]
- [Appendix C Oblique Shock 2015][research_appendix_c_2015]
- [Appleby and Adams 1991][research_appleby_adams_1991]
- [Approximate Method of Predicting 1983][research_approximate_method_1983]
- [Aprovitola et al 2019][research_aprovitola_iuspa_2019]
- [Arad 2024][research_arad_2024]
- [Arad 2026][research_arad_2026]
- [Arai et al 2008][research_arai_taguchi_2008]
- [Araújo et al 2024][research_araujo_tanaka_2024]
- [Ardema, Mark D. 1995][research_ardemamarkd_1995]
- [Ardonceau 1984][research_ardonceau_1984]
- [Arens 1961][research_arens_1961]
- [Arent and Falatko 1992][research_arent_falatko_1992]
- [Armstrong 1979][research_armstrong_1979]
- [Armstrong and Latimer 1969][research_armstrong_latimer_1969]
- [Army War Coll Carlisle Barracks Pa 1952][research_armywarcollcarlislebarrackspa_1952]
- [Arnold 1981][research_arnold_1981]
- [Arnold et al 2023][research_arnold_pace_2023]
- [Aronov and Klyagin 2021][research_aronov_klyagin_2021]
- [Arons and Macnair 1970][research_arons_macnair_1970]
- [Asami 1999][research_asami_1999]
- [Asma and Van der Haegen 2010][research_asma_vanderhaegen_2010]
- [Asma et al 2009][research_asma_tirtey_2009]
- [Aso et al 1992][research_aso_okuyama_1992]
- [Aso et al 1993][research_aso_kumamoto_1993]
- [Aso et al 2002][research_aso_hayashi_2002]
- [Aso et al 2018][research_aso_tani_2018]
- [Assessment of Key Aerothermal 1992][research_assessment_of_1992]
- [Assis et al 2019][research_assis_suppandipillai_2019]
- [Atay et al 2026][research_atay_kumartaslioglu_2026]
- [Atkins 2026][research_atkins_2026]
- [Atmosphere standard atmosphere 2006][research_atmosphere_standard_2006]
- [Attar et al 2026][research_attar_vanderlee_2026]
- [Aubrey and Speer 1983][research_aubrey_speer_1983]
- [August and Joshi 1997][research_august_joshi_1997]
- [Ault, G. M. 1965][research_aultgm_1965]
- [Auslender et al 2009][research_auslender_suder_2009]
- [Austin][research_austin]
- [Autenrieb 2023][research_autenrieb_2023]
- [Autenrieb and Fezans 2024][research_autenrieb_fezans_2024]
- [Automatic Detection and Suppression 1974][research_automatic_detection_1974]
- [Auxer 1968][research_auxer_1968]
- [Avasali Dineshkumar et al 2026][research_avasalidineshkumar_mrsvsaritha_2026]
- [Avcilar and Celik 2026][research_avcilar_celik_2026]
- [Avery, D. E. 1981][research_averyde_1981]
- [Avidor and Lederman 1971][research_avidor_lederman_1971]
- [Axdahl et al 2011][research_axdahl_kumar_2011]
- [Axdahl et al 2012][research_axdahl_kumar_2012]
- [Azevedo and Korzenowski 1998][research_azevedo_korzenowski_1998]
- [B-34. U. S. Standard 1963][research_b_34_u_1963]
- [B. 2011][research_b_2011]
- [Babinsky 2002][research_babinsky_2002]
- [Babinsky 2007][research_babinsky_2007]
- [Babinsky 2014][research_babinsky_2014]
- [Babinsky and Délery 2011][research_babinsky_delery_2011]
- [Babu 2020][research_babu_2020]
- [Babu 2021][research_babu_2021]
- [Bac 1993][research_bac_1993]
- [Baccarella et al 2020][research_baccarella_liu_2020]
- [Bachchan and Hillier 2004][research_bachchan_hillier_2004]
- [Baer 1961][research_baer_1961]
- [Baer 1966][research_baer_1966]
- [Baganoff 1990][research_baganoff_1990]
- [Bagaveyev et al 2010][research_bagaveyev_bhagwandin_2010]
- [Bahambari and Khankalantary 2023][research_bahambari_khankalantary_2023]
- [Bahm, Catherine et al 2005][research_bahmcatherine_baumannethan_2005]
- [Bahuguna et al 2023][research_bahuguna_kolluru_2023]
- [Bai et al 2014][research_bai_ren_2014]
- [Bakos][research_bakos]
- [Balachandar 2003][research_balachandar_2003]
- [Balaji and Venkatasubbaiah 2025][research_balaji_venkatasubbaiah_2025]
- [Balaji Himakar and Rao 2025][research_balajihimakar_rao_2025]
- [Balakrishnan et al 1997][research_balakrishnan_shen_1997]
- [Balent and Kutschenreuter, Jr. 1964][research_balent_kutschenreuterjr_1964]
- [Ball et al 1981][research_ball_syberg_1981]
- [Balland and Vincent-Randonnier 2015][research_balland_vincentrandonnier_2015]
- [Balland et al 2015][research_balland_fernandezvillace_2015]
- [Ballaro and Anderson, Jr. 1991][research_ballaro_andersonjr_1991]
- [Ban et al 2026][research_ban_zhang_2026]
- [Bano et al 2026][research_bano_fraser_2026]
- [Bansal et al 2010][research_bansal_modest_2010]
- [Bansal et al 2010][research_bansal_modest_2010_b]
- [Bao et al 2010][research_bao_li_2010]
- [Bao et al 2012][research_bao_li_2012]
- [Bao et al 2013][research_bao_duan_2013]
- [Bao et al 2017][research_bao_zhou_2017]
- [Bao et al 2021][research_bao_wang_2021]
- [Baranovskii and Levin 1990][research_baranovskii_levin_1990]
- [Baranovskii and Levin 1991][research_baranovskii_levin_1991]
- [Barber and Cox 1989][research_barber_cox_1989]
- [Barber and Cox, Jr. 1988][research_barber_coxjr_1988]
- [Barber et al 1997][research_barber_orszag_1997]
- [Barber et al 2006][research_barber_heitt_2006]
- [Barbera 1980][research_barbera_1980]
- [Barberis and Molton 1995][research_barberis_molton_1995]
- [Bardina and Lombard 1987][research_bardina_lombard_1987]
- [Barlow and Wood 1987][research_barlow_wood_1987]
- [Barlow et al 1988][research_barlow_wood_1988]
- [Barnes and Segal 2015][research_barnes_segal_2015]
- [Barnett and Starrett 1994][research_barnett_starrett_1994]
- [Barnhart et al 1988][research_barnhart_greber_1988]
- [Baron and Efrat 1979][research_baron_efrat_1979]
- [Barone et al 2022][research_barone_nicholson_2022]
- [Barr et al 2026][research_barr_figueroa_2026]
- [Barreto et al 2021][research_barreto_freire_2021]
- [Barrett 1963][research_barrett_1963]
- [Barrett 2025][research_barrett_2025]
- [Barth][research_barth]
- [Barth et al 2014][research_barth_wheatley_2014]
- [Bartolome Calvo and Eggers 2011][research_bartolomecalvo_eggers_2011]
- [Bartusiak et al 2022][research_bartusiak_hao_2022]
- [Baruzzi et al 2021][research_baruzzi_karchani_2021]
- [Barz 2026][research_barz_2026]
- [Barzegar Gerdroodbary 2020][research_barzegargerdroodbary_2020]
- [Batcho and Sullivan 1988][research_batcho_sullivan_1988]
- [Bates 2004][research_bates_2004]
- [Bates et al 2004][research_bates_maas_2004]
- [Batill and Hoffman 1984][research_batill_hoffman_1984]
- [Bauer 1966][research_bauer_1966]
- [Bauer 1967][research_bauer_1967]
- [Bauer 2004][research_bauer_2004]
- [Bauer et al 1974][research_bauer_muse_1974]
- [Bauer et al 1998][research_bauer_petters_1998]
- [Baumberger et al 2026][research_baumberger_peterson_2026]
- [Baurle and Eklund 2001][research_baurle_eklund_2001]
- [Baurle and Gruber 1998][research_baurle_gruber_1998]
- [Baurle et al 1998][research_baurle_mathur_1998]
- [Baye-Wallace and Krouse 2022][research_bayewallace_krouse_2022]
- [Baysal and Luo 1998][research_baysal_luo_1998]
- [Baş 2026][research_bas_2026]
- [Bedanand Mandal 2025][research_bedanandmandal_2025]
- [Bedarev and Fedorova 2001][research_bedarev_fedorova_2001]
- [Beery et al 1975][research_beery_clodfelter_1975]
- [Bein et al 1993][research_bein_friedmann_1993]
- [Bejan 2010][research_bejan_2010]
- [Beketaeva et al 2016][research_beketaeva_moisseyeva_2016]
- [Bell 1993][research_bell_1993]
- [Bellan 2012][research_bellan_2012]
- [Ben-Arosh et al 1997][research_benarosh_natan_1997]
- [Ben-Arosh et al 1998][research_benarosh_natan_1998]
- [Ben-Arosh et al 1999][research_benarosh_natan_1999]
- [Ben-Dor 1978][research_bendor_1978]
- [Ben-Dor 1978][research_bendor_1978_b]
- [Ben-Dor 2001][research_bendor_2001]
- [Ben-Yakar and Hanson 1999][research_benyakar_hanson_1999]
- [Benay 2003][research_benay_2003]
- [Benay and Pot 1986][research_benay_pot_1986]
- [Bencze 1972][research_bencze_1972]
- [Bencze and Sorensen 1970][research_bencze_sorensen_1970]
- [Bender 1969][research_bender_1969]
- [Bendix Corp Eatontown Nj 1963][research_bendixcorpeatontownnj_1963]
- [Bendot et al 1975][research_bendot_harkins_1975]
- [Benjelloun Touimi and Doom 2025][research_benjellountouimi_doom_2025]
- [Bennett 1971][research_bennett_1971]
- [Bennett and Connors 1964][research_bennett_connors_1964]
- [Bennett and Edwards 1990][research_bennett_edwards_1990]
- [Bensassi et al 2010][research_bensassi_lani_2010]
- [Bensassi et al 2013][research_bensassi_lani_2013]
- [Benson and Maslowe 1965][research_benson_maslowe_1965]
- [Benson and Mcrae 1993][research_benson_mcrae_1993]
- [Benson et al 1976][research_benson_sedgwick_1976]
- [Benson et al 2009][research_benson_liou_2009]
- [Benstein 1989][research_benstein_1989]
- [Benton 1990][research_benton_1990]
- [Berens and Bissinger 1996][research_berens_bissinger_1996]
- [Berens and Bissinger 1998][research_berens_bissinger_1998]
- [Berens and Bissinger 1998][research_berens_bissinger_1998_b]
- [Berezovik and Tikhonov 1980][research_berezovik_tikhonov_1980]
- [Berger 1971][research_berger_1971]
- [Berger et al 2019][research_berger_gourdain_2019]
- [Bergholz and Hitch 1992][research_bergholz_hitch_1992]
- [Bergier][research_bergier]
- [Berglund and Fureby 2007][research_berglund_fureby_2007]
- [Berglund et al 2010][research_berglund_fedina_2010]
- [Berkner 1990][research_berkner_1990]
- [Berkovits 1973][research_berkovits_1973]
- [Bertelrud et al 1992][research_bertelrud_kolodziej_1992]
- [Bertelrud et al 1999][research_bertelrud_budd_1999]
- [Berthelot 1994][research_berthelot_1994]
- [Berthelot et al 2026][research_berthelot_craft_2026]
- [Berthold et al 1976][research_berthold_iii_1976]
- [Bertin et al 1997][research_bertin_towne_1997]
- [Besserer 1952][research_besserer_1952]
- [Best et al 2001][research_best_fetterhoff_2001]
- [Bestion 2017][research_bestion_2017]
- [Bestion 2024][research_bestion_2024]
- [Bestman 1991][research_bestman_1991]
- [Bettis and Hosder 2010][research_bettis_hosder_2010]
- [Bever 1992][research_bever_1992]
- [Bezerra et al 2024][research_bezerra_souza_2024]
- [Bezerra et al 2026][research_bezerra_desouza_2026]
- [Bhagwandin and DeSpirito 2011][research_bhagwandin_despirito_2011]
- [Bhagwandin and Sahu 2023][research_bhagwandin_sahu_2023]
- [Bhagwandin et al 2009][research_bhagwandin_engblom_2009]
- [Bhakta et al 2025][research_bhakta_sims_2025]
- [Bhanderi and Babinsky 2005][research_bhanderi_babinsky_2005]
- [Bhat and Lind 2009][research_bhat_lind_2009]
- [Bhatia and Sirignano 1990][research_bhatia_sirignano_1990]
- [Bhungalia et al 2000][research_bhungalia_zweber_2000]
- [Bhutta and Lewis 1988][research_bhutta_lewis_1988]
- [Biagioni et al 1998][research_biagioni_scortecci_1998]
- [Bielawski 2026][research_bielawski_2026]
- [Biennial Flight Test Conference 1994][research_biennial_flight_1994]
- [Biggi et al 2024][research_biggi_abdelnour_2024]
- [Bilchenko 2015][research_bilchenko_2015]
- [Billig 1967][research_billig_1967]
- [Billig 1992][research_billig_1992]
- [Billig 1993][research_billig_1993]
- [Billig 1995][research_billig_1995]
- [Billig et al 1979][research_billig_waltrup_1979]
- [Billig, F. S. 1967][research_billigfs_1967]
- [Billig, F. S. and Grenleski, S. E. 1970][research_billigfs_grenleskise_1970]
- [Billingsley et al 2010][research_billingsley_edwards_2010]
- [Bin and Hongxin 2006][research_bin_hongxin_2006]
- [Bing and Gong 2015][research_bing_gong_2015]
- [Birrer and Stemmer 2012][research_birrer_stemmer_2012]
- [Birzer and Doolan 2007][research_birzer_doolan_2007]
- [Bissinger and Schmitz 1993][research_bissinger_schmitz_1993]
- [Bissinger et al 1998][research_bissinger_blagoveshchensky_1998]
- [Bityurin and Bocharov 2010][research_bityurin_bocharov_2010]
- [Blaine et al 2005][research_blaine_keeling_2005]
- [Blanchard 1983][research_blanchard_1983]
- [Blankson and Hagseth 1993][research_blankson_hagseth_1993]
- [Blankson et al 1998][research_blankson_lewis_1998]
- [Bleimeyer 1981][research_bleimeyer_1981]
- [Blosser, M. L. 1987][research_blosserml_1987]
- [Blosser, M. L. and Mcwithey, R. R. 1983][research_blosserml_mcwitheyrr_1983]
- [Blosser, Max L. 1988][research_blossermaxl_1988]
- [Blum 2006][research_blum_2006]
- [Bodryakov 2014][research_bodryakov_2014]
- [Bodryakov 2015][research_bodryakov_2015]
- [Bodryakov 2018][research_bodryakov_2018]
- [Boeing Scientific Research Labs Seattle Wa 1963][research_boeingscientificresearchlabsseattlewa_1963]
- [Boeing to use X-43A 2005][research_boeing_to_2005]
- [Boettinger 1988][research_boettinger_1988]
- [Bogart et al 1981][research_bogart_breckenridge_1981]
- [Bogdanoff and Christiansen 1978][research_bogdanoff_christiansen_1978]
- [Bogdnoff 1953][research_bogdnoff_1953]
- [Bogdonoff 1970][research_bogdonoff_1970]
- [Bogdonoff 1990][research_bogdonoff_1990]
- [Bogdonoff 1999][research_bogdonoff_1999]
- [Bogi et al 2025][research_bogi_vinay_2025]
- [Bogue 1992][research_bogue_1992]
- [Bogue et al 1995][research_bogue_bagley_1995]
- [Bohning and Doerffer 2002][research_bohning_doerffer_2002]
- [Boiocchi et al 2018][research_boiocchi_galfetti_2018]
- [Boirun 1979][research_boirun_1979]
- [Bokor et al 2026][research_bokor_chamarthi_2026]
- [Boland et al 2023][research_boland_hinkle_2023]
- [Bolender and Doman 2005][research_bolender_doman_2005]
- [Bolender and Doman 2006][research_bolender_doman_2006]
- [Bolender et al 2007][research_bolender_oppenheimer_2007]
- [Bolender et al 2009][research_bolender_wilkin_2009]
- [Boles and Milligan 2013][research_boles_milligan_2013]
- [Bolt 1981][research_bolt_1981]
- [Bonanni and Ihme 2023][research_bonanni_ihme_2023]
- [Bonavita et al 2026][research_bonavita_zollars_2026]
- [Bonelli et al 2011][research_bonelli_cutrone_2011]
- [Bonnefond et al 1996][research_bonnefond_falempin_1996]
- [Bonnell 2000][research_bonnell_2000]
- [Boon and Hillier 2006][research_boon_hillier_2006]
- [Boon and Hillier 2006][research_boon_hillier_2006_b]
- [Bootle 1999][research_bootle_1999]
- [Boppe and Davis 1989][research_boppe_davis_1989]
- [Bordelon et al 2003][research_bordelon_frost_2003]
- [Bordoloi et al 2021][research_bordoloi_pandey_2021]
- [Bordoloi et al 2022][research_bordoloi_pandey_2022]
- [Bordoloi et al 2022][research_bordoloi_pandey_2022_b]
- [Borelli et al 2018][research_borelli_repetto_2018]
- [Borg et al 2012][research_borg_kimmel_2012]
- [Borg et al 2013][research_borg_kimmel_2013]
- [Borg et al 2025][research_borg_adamczak_2025]
- [Bormotova et al 2003][research_bormotova_volodin_2003]
- [Borovikov et al 1996][research_borovikov_gavriliouk_1996]
- [Borovoi et al 1996][research_borovoi_chinilov_1996]
- [Borovoy et al 2015][research_borovoy_egorov_2015]
- [Borrelli et al 1998][research_borrelli_marini_1998]
- [Bortner 1964][research_bortner_1964]
- [Bose 2012][research_bose_2012]
- [Boswell et al 2004][research_boswell_sutherland_2004]
- [Bouazzi et al 2025][research_bouazzi_ali_2025]
- [Bouchard and Chambers 1966][research_bouchard_chambers_1966]
- [Bouchez 2001][research_bouchez_2001]
- [Bouchez and Beyer 2005][research_bouchez_beyer_2005]
- [Bouchez and Beyer 2006][research_bouchez_beyer_2006]
- [Bouchez and Beyer 2008][research_bouchez_beyer_2008]
- [Bouchez and Beyer 2009][research_bouchez_beyer_2009]
- [Bouchez and Levine 2003][research_bouchez_levine_2003]
- [Bouchez et al 1998][research_bouchez_montazel_1998]
- [Bouchez et al 2004][research_bouchez_cahuzac_2004]
- [Bouchez et al 2005][research_bouchez_roudakov_2005]
- [Bouchez et al 2011][research_bouchez_perillat_2011]
- [Boudreau et al 1993][research_boudreau_smithiii_1993]
- [Boulal and Le Pichon 2026][research_boulal_lepichon_2026]
- [Boulal et al 2026][research_boulal_genot_2026]
- [Bourgoing and Benay 2005][research_bourgoing_benay_2005]
- [Bowcutt 2001][research_bowcutt_2001]
- [Bowcutt and Haney 1995][research_bowcutt_haney_1995]
- [Bowes 1978][research_bowes_1978]
- [Bowles 1980][research_bowles_1980]
- [Bowles et al 1998][research_bowles_roberts_1998]
- [Bowman 1995][research_bowman_1995]
- [Bowman and Foy 1961][research_bowman_foy_1961]
- [Bowman and Nereson 1974][research_bowman_nereson_1974]
- [Bowman et al 1990][research_bowman_hanson_1990]
- [Bowman et al 1991][research_bowman_hanson_1991]
- [Bowman et al 1992][research_bowman_hanson_1992]
- [Bowman et al 1997][research_bowman_hanson_1997]
- [Boyce and Paull 2001][research_boyce_paull_2001]
- [Boyce et al 2003][research_boyce_gerard_2003]
- [Boyd 1990][research_boyd_1990]
- [Boyd 1999][research_boyd_1999]
- [Boyd 2001][research_boyd_2001]
- [Boyd 2002][research_boyd_2002]
- [Boyd 2004][research_boyd_2004]
- [Boyd 2008][research_boyd_2008]
- [Boyd 2013][research_boyd_2013]
- [Boyd 2015][research_boyd_2015]
- [Boyd 2024][research_boyd_2024]
- [Boyd et al 1993][research_boyd_phamvandiep_1993]
- [Boyer 1965][research_boyer_1965]
- [Boyer et al 1960][research_boyer_eschenroeder_1960]
- [Brabbs, Theodore A. and Robertson, Thomas F. 1987][research_brabbstheodorea_robertsonthomasf_1987]
- [Bradford and Olds 1999][research_bradford_olds_1999]
- [Bradley and Magee 1995][research_bradley_magee_1995]
- [Bradley et al 1981][research_bradley_siemersiii_1981]
- [Brahmachary and Ogawa 2021][research_brahmachary_ogawa_2021]
- [Braun et al 2025][research_braun_hammack_2025]
- [Braun et al 2025][research_braun_hammack_2025_b]
- [Braun et al 2026][research_braun_hassan_2026]
- [Bravo et al 2025][research_bravo_plewacki_2025]
- [Breitsamter et al 2001][research_breitsamter_laschka_2001]
- [Brenneis and Wanie 1991][research_brenneis_wanie_1991]
- [Bretherton][research_bretherton]
- [Briardy and Head 1968][research_briardy_head_1968]
- [Bricker et al 1989][research_bricker_numbers_1989]
- [Brief Review of Computational 2024][research_brief_review_2024]
- [Brieschenk et al 2013][research_brieschenk_obyrne_2013]
- [Brinda et al 2006][research_brinda_dasgupta_2006]
- [Britcher and Landman 2024][research_britcher_landman_2024]
- [Britcher and Landman 2024][research_britcher_landman_2024_b]
- [Britcher and Landman 2024][research_britcher_landman_2024_c]
- [Britcher and Landman 2024][research_britcher_landman_2024_d]
- [Britcher and Landman 2024][research_britcher_landman_2024_e]
- [Britcher and Landman 2024][research_britcher_landman_2024_f]
- [Brits][research_brits]
- [Broadaway 1984][research_broadaway_1984]
- [Brocanelli et al 2012][research_brocanelli_gunbatar_2012]
- [Brociek et al 2023][research_brociek_hetmaniok_2023]
- [Brockmann and Stefanovich 2022][research_brockmann_stefanovich_2022]
- [Brodsky 1970][research_brodsky_1970]
- [Brody K Bessire][research_brodykbessire]
- [Bronnikov and Vettegren 1997][research_bronnikov_vettegren_1997]
- [Brooke 1957][research_brooke_1957]
- [Brooks 1986][research_brooks_1986]
- [Brophy and Hawk 1990][research_brophy_hawk_1990]
- [Brown 1978][research_brown_1978]
- [Brown 2012][research_brown_2012]
- [Brown and Boyce 2012][research_brown_boyce_2012]
- [Brown and Bradley 1981][research_brown_bradley_1981]
- [Brown and Donbar 2013][research_brown_donbar_2013]
- [Brown and Donbar 2015][research_brown_donbar_2015]
- [Brown and Ravichandran 2013][research_brown_ravichandran_2013]
- [Brown et al 1963][research_brown_kramer_1963]
- [Brown et al 1986][research_brown_kussoy_1986]
- [Brown et al 2010][research_brown_williams_2010]
- [Brown, James L. 2014][research_brownjamesl_2014]
- [Browne et al 2021][research_browne_rasmussen_2021]
- [Brummund and Scheel 2002][research_brummund_scheel_2002]
- [Brune et al 2016][research_brune_hosder_2016]
- [Brunner 1959][research_brunner_1959]
- [Bruno 1989][research_bruno_1989]
- [Bruno 2023][research_bruno_2023]
- [Bruno 2023][research_bruno_2023_b]
- [Bruno 2023][research_bruno_2023_c]
- [Bruno 2023][research_bruno_2023_d]
- [Brutsche and McFall 2015][research_brutsche_mcfall_2015]
- [Bryan 1953][research_bryan_1953]
- [Brykina 1996][research_brykina_1996]
- [Bu and Lei 2018][research_bu_lei_2018]
- [Buchanan and Crosby 1983][research_buchanan_crosby_1983]
- [Bucher and Bradley 1975][research_bucher_bradley_1975]
- [Buck and Draper][research_buck_draper]
- [Bucknell 1987][research_bucknell_1987]
- [Bucknell 1989][research_bucknell_1989]
- [Builder 1964][research_builder_1964]
- [Bullen et al 1988][research_bullen_cheeseman_1988]
- [Bulman and Siebenhaar 1995][research_bulman_siebenhaar_1995]
- [Buonadonna et al 1973][research_buonadonna_knight_1973]
- [Bur et al 2002][research_bur_benay_2002]
- [Bura 2017][research_bura_2017]
- [Burke and Poggie 2023][research_burke_poggie_2023]
- [Burnett 2002][research_burnett_2002]
- [Burnett and Czysz 1963][research_burnett_czysz_1963]
- [Burns 1965][research_burns_1965]
- [Burns 1970][research_burns_1970]
- [Burns 2020][research_burns_2020]
- [Burr 1968][research_burr_1968]
- [Burris 1966][research_burris_1966]
- [Burrows et al 2017][research_burrows_vukasinovic_2017]
- [Burt and Josyula 2013][research_burt_josyula_2013]
- [Burton 1987][research_burton_1987]
- [Burton and Carroll 2025][research_burton_carroll_2025]
- [Busa et al 2016][research_busa_brown_2016]
- [Bussing and Murman 1983][research_bussing_murman_1983]
- [Bustard et al 2024][research_bustard_bemis_2024]
- [Butler 1976][research_butler_1976]
- [Butler et al 2022][research_butler_benitez_2022]
- [Butler et al 2023][research_butler_benitez_2023]
- [Butt 2013][research_butt_2013]
- [Butt et al 2010][research_butt_yan_2010]
- [Butt et al 2011][research_butt_yan_2011]
- [Buttsworth and Morgan 1995][research_buttsworth_morgan_1995]
- [Buttsworth et al 2017][research_buttsworth_stern_2017]
- [Buzjurkin and Kiselev 2002][research_buzjurkin_kiselev_2002]
- [Buzz Suppression of Supersonic 2005][research_buzz_suppression_2005]
- [Bykerk et al 2020][research_bykerk_verstraete_2020]
- [Byun and Kim 2026][research_byun_kim_2026]
- [C. et al 2011][research_c_battista_2011]
- [Cai and Huang 2022][research_cai_huang_2022]
- [Cai and Zhuang 2025][research_cai_zhuang_2025]
- [Cai et al 2016][research_cai_liu_2016]
- [Cai et al 2017][research_cai_zhou_2017]
- [Cai et al 2018][research_cai_sun_2018]
- [Cai et al 2025][research_cai_zheng_2025]
- [Cai et al 2026][research_cai_zhuang_2026]
- [Cain 2002][research_cain_2002]
- [Cain and Walton 2003][research_cain_walton_2003]
- [Cairns and Tevebaugh 1963][research_cairns_tevebaugh_1963]
- [Calabia and Jin 2020][research_calabia_jin_2020]
- [Calder et al 2026][research_calder_yackoub_2026]
- [Caledonia and Krech 1994][research_caledonia_krech_1994]
- [California Inst Of Tech Pasadena 1990][research_californiainstoftechpasadena_1990]
- [Calise and Bae 1987][research_calise_bae_1987]
- [Callan and Marusic 2000][research_callan_marusic_2000]
- [Callan and Marusic 2001][research_callan_marusic_2001]
- [Calligeros and Dugundji 1961][research_calligeros_dugundji_1961]
- [Calogeras 1969][research_calogeras_1969]
- [Cambier and Adelman 1997][research_cambier_adelman_1997]
- [Campbell and Kresge 2003][research_campbell_kresge_2003]
- [Campuzano and Dang 1995][research_campuzano_dang_1995]
- [Candler 1989][research_candler_1989]
- [Candler 1989][research_candler_1989_b]
- [Candler 2001][research_candler_2001]
- [Candler 2010][research_candler_2010]
- [Candler 2011][research_candler_2011]
- [Candler and Leyva 2022][research_candler_leyva_2022]
- [Candler and Nompelis 2002][research_candler_nompelis_2002]
- [Candler et al 2015][research_candler_subbareddy_2015]
- [Candler, Graham 1989][research_candlergraham_1989]
- [Candler, Graham and Park, Chul 1988][research_candlergraham_parkchul_1988]
- [Cangelosi et al 2024][research_cangelosi_heinkenschloss_2024]
- [Cann 1973][research_cann_1973]
- [Canoville and Lewis 2025][research_canoville_lewis_2025]
- [Cao et al 2007][research_cao_zhang_2007]
- [Cao et al 2014][research_cao_chang_2014]
- [Cao et al 2015][research_cao_chang_2015]
- [Cao et al 2019][research_cao_he_2019]
- [Cao et al 2021][research_cao_brod_2021]
- [Cao et al 2022][research_cao_gong_2022]
- [Cao et al 2022][research_cao_lee_2022]
- [Cao et al 2023][research_cao_brod_2023]
- [Cao et al 2026][research_cao_zhang_2026]
- [Capparelli et al 2026][research_capparelli_unternbaumen_2026]
- [Caraballo et al 2009][research_caraballo_webb_2009]
- [Carbajosa et al 2025][research_carbajosa_sanzandres_2025]
- [Carbajosa et al 2026][research_carbajosa_sanzandres_2026]
- [Carlomagno et al 1993][research_carlomagno_luca_1993]
- [Carman and J. B. 1966][research_carman_jb_1966]
- [Carpenter et al 2025][research_carpenter_hantsche_2025]
- [Carrico 2009][research_carrico_2009]
- [Carroll 1982][research_carroll_1982]
- [Carroll and Dutton 1989][research_carroll_dutton_1989]
- [Carroll et al 1981][research_carroll_kerlin_1981]
- [Carson et al 2004][research_carson_mohieldin_2004]
- [Carter 2012][research_carter_2012]
- [Carter and Springfield 2002][research_carter_springfield_2002]
- [Carvalho et al 2020][research_carvalho_santos_2020]
- [Casalino and Colasurdo 2002][research_casalino_colasurdo_2002]
- [Cassanova 1967][research_cassanova_1967]
- [Cassanto 1971][research_cassanto_1971]
- [Cassanto 1972][research_cassanto_1972]
- [Casseau et al 2022][research_casseau_zhang_2022]
- [Cassidy and Halley 1991][research_cassidy_halley_1991]
- [Castaldi et al 2006][research_castaldi_leylegian_2006]
- [Castner et al 2018][research_castner_simerly_2018]
- [Catalano and Sturek 2001][research_catalano_sturek_2001]
- [Catoire 2009][research_catoire_2009]
- [Cavanaugh and Narayanaswamy 2024][research_cavanaugh_narayanaswamy_2024]
- [Cavanaugh et al 2025][research_cavanaugh_stramecky_2025]
- [Cavanaugh et al 2026][research_cavanaugh_narayanaswamy_2026]
- [Cavity-actuated supersonic mixing and 1995][research_cavity_actuated_supersonic_1995]
- [Caylor and Batill 1984][research_caylor_batill_1984]
- [Cazier, Jr. and Ricketts 1991][research_cazierjr_ricketts_1991]
- [Celmins 1990][research_celmins_1990]
- [Cenkci 1991][research_cenkci_1991]
- [Cenko 1992][research_cenko_1992]
- [Cenko et al 2003][research_cenko_cenko_2003]
- [Center et al 1991][research_center_sobieczky_1991]
- [Centlivre 2023][research_centlivre_2023]
- [CFD Applications to Engine/Airframe 1986][research_cfd_applications_1986]
- [CFD optimization and test 1994][research_cfd_optimization_1994]
- [Chacon et al 2019][research_chacon_feleo_2019]
- [Chakravarthy et al 1988][research_chakravarthy_szema_1988]
- [Chakravarty and Narayanaswamy 2026][research_chakravarty_narayanaswamy_2026]
- [Chamberlain and Baltar 1993][research_chamberlain_baltar_1993]
- [Chambers et al 2019][research_chambers_titchener_2019]
- [Chambers Jr 2007][research_chambersjr_2007]
- [Chan and Ihme 2014][research_chan_ihme_2014]
- [Chan and Ihme 2016][research_chan_ihme_2016]
- [Chandler 2003][research_chandler_2003]
- [Chandrasekhar et al 2014][research_chandrasekhar_ramanujachari_2014]
- [Chang 1962][research_chang_1962]
- [Chang 1966][research_chang_1966]
- [Chang 2025][research_chang_2025]
- [Chang and Choudhari 2010][research_chang_choudhari_2010]
- [Chang et al 2008][research_chang_yu_2008]
- [Chang et al 2008][research_chang_yu_2008_b]
- [Chang et al 2009][research_chang_yu_2009]
- [Chang et al 2010][research_chang_fan_2010]
- [Chang et al 2011][research_chang_hu_2011]
- [Chang et al 2011][research_chang_li_2011]
- [Chang et al 2012][research_chang_wang_2012]
- [Chang et al 2014][research_chang_wang_2014]
- [Chang et al 2014][research_chang_zheng_2014]
- [Chang et al 2017][research_chang_li_2017]
- [Chang et al 2022][research_chang_huang_2022]
- [Chang et al 2023][research_chang_sasaki_2023]
- [Chang et al 2026][research_chang_seo_2026]
- [Chao Song et al 2011][research_chaosong_guorongzhao_2011]
- [Chaouat 2017][research_chaouat_2017]
- [Chapter 1 Asymptotically Simplified 2013][research_chapter_1_2013]
- [Chapter 10 Numerical Modeling 2013][research_chapter_10_2013]
- [Chapter 13 Numerical Modeling 2013][research_chapter_13_2013]
- [Chapter 18 Near-Wall Domain 2013][research_chapter_18_2013]
- [Chapter 5 Physicochemical Models 2013][research_chapter_5_2013]
- [Chapter 6 Modeling of 2013][research_chapter_6_2013]
- [Chapter 7 Navier-Stokes-Based Numerical 2013][research_chapter_7_2013]
- [Chapter 8 Numerical Study 2013][research_chapter_8_2013]
- [Chapter 9 Model of 2013][research_chapter_9_2013]
- [Characterization of High-Temperature Materials 2014][research_characterization_of_2014]
- [Charyulu et al 1998][research_charyulu_kurian_1998]
- [Chase and Rust 1980][research_chase_rust_1980]
- [Chase et al 1978][research_chase_fisher_1978]
- [Chatterjee and Venkateswararao 1982][research_chatterjee_venkateswararao_1982]
- [Chauffour and Lewis 2003][research_chauffour_lewis_2003]
- [Chaussee and Rizk 1982][research_chaussee_rizk_1982]
- [Chauvin et al 1968][research_chauvin_erb_1968]
- [Che and Tang 2008][research_che_tang_2008]
- [Cheadle and DiZinno 2026][research_cheadle_dizinno_2026]
- [Chekhovskoi 2000][research_chekhovskoi_2000]
- [Chemical and Vibrational Nonequilibrium 2006][research_chemical_and_2006]
- [Chemical and Vibrational Nonequilibrium 2019][research_chemical_and_2019]
- [Chemical Kinetics of High 1962][research_chemical_kinetics_1962]
- [Chen 1958][research_chen_1958]
- [Chen 2017][research_chen_2017]
- [Chen 2017][research_chen_2017_b]
- [Chen 2023][research_chen_2023]
- [Chen and Bultman 2004][research_chen_bultman_2004]
- [Chen and He 2025][research_chen_he_2025]
- [Chen and Henline 1993][research_chen_henline_1993]
- [Chen and Liu 2014][research_chen_liu_2014]
- [Chen and Milos 1996][research_chen_milos_1996]
- [Chen and Tan 2019][research_chen_tan_2019]
- [Chen and Wu 2018][research_chen_wu_2018]
- [Chen et al 2003][research_chen_gu_2003]
- [Chen et al 2006][research_chen_williamson_2006]
- [Chen et al 2008][research_chen_agarwal_2008]
- [Chen et al 2009][research_chen_starkey_2009]
- [Chen et al 2012][research_chen_hu_2012]
- [Chen et al 2013][research_chen_chen_2013]
- [Chen et al 2014][research_chen_ai_2014]
- [Chen et al 2015][research_chen_liu_2015]
- [Chen et al 2016][research_chen_chen_2016]
- [Chen et al 2016][research_chen_gao_2016]
- [Chen et al 2016][research_chen_liu_2016]
- [Chen et al 2016][research_chen_yao_2016]
- [Chen et al 2017][research_chen_guo_2017]
- [Chen et al 2017][research_chen_ni_2017]
- [Chen et al 2018][research_chen_jing_2018]
- [Chen et al 2018][research_chen_niu_2018]
- [Chen et al 2018][research_chen_tan_2018]
- [Chen et al 2018][research_chen_yan_2018]
- [Chen et al 2018][research_chen_yue_2018]
- [Chen et al 2019][research_chen_guo_2019]
- [Chen et al 2019][research_chen_tan_2019_b]
- [Chen et al 2020][research_chen_fan_2020]
- [Chen et al 2020][research_chen_fan_2020_b]
- [Chen et al 2020][research_chen_shen_2020]
- [Chen et al 2020][research_chen_zhou_2020]
- [Chen et al 2020][research_chen_zhou_2020_b]
- [Chen et al 2020][research_chen_zhou_2020_c]
- [Chen et al 2020][research_chen_zhou_2020_d]
- [Chen et al 2021][research_chen_pei_2021]
- [Chen et al 2021][research_chen_wang_2021]
- [Chen et al 2021][research_chen_wang_2021_b]
- [Chen et al 2021][research_chen_zhou_2021]
- [Chen et al 2022][research_chen_tian_2022]
- [Chen et al 2024][research_chen_bonanni_2024]
- [Chen et al 2024][research_chen_chen_2024]
- [Chen et al 2024][research_chen_liu_2024]
- [Chen et al 2024][research_chen_zhu_2024]
- [Chen et al 2025][research_chen_lu_2025]
- [Chen et al 2025][research_chen_martinez_2025]
- [Chen et al 2025][research_chen_tian_2025]
- [Chen et al 2025][research_chen_wang_2025]
- [Chen et al 2026][research_chen_guo_2026]
- [Chen et al 2026][research_chen_mao_2026]
- [Chen et al 2026][research_chen_sethuraman_2026]
- [Chen et al 2026][research_chen_zheng_2026]
- [Chen, Fang-Jeng Frank and Berry, Scott A. 2010][research_chenfangjengfrank_berryscotta_2010]
- [Cheney 1988][research_cheney_1988]
- [Cheng 1960][research_cheng_1960]
- [Cheng 1993][research_cheng_1993]
- [Cheng and Aslam 2020][research_cheng_aslam_2020]
- [Cheng and Liu 2015][research_cheng_liu_2015]
- [Cheng et al 2017][research_cheng_dong_2017]
- [Cheng et al 2017][research_cheng_tang_2017]
- [Cheng et al 2018][research_cheng_wang_2018]
- [Cheng et al 2019][research_cheng_yan_2019]
- [Cheng et al 2021][research_cheng_yan_2021]
- [Chengbin Lian et al 2012][research_chengbinlian_zhangren_2012]
- [Chern et al 2014][research_chern_lobser_2014]
- [Chern et al 2025][research_chern_rockwell_2025]
- [Cherukat et al 1998][research_cherukat_na_1998]
- [Cheung et al 1974][research_cheung_chen_1974]
- [Chi et al 2014][research_chi_wei_2014]
- [Chi et al 2021][research_chi_wang_2021]
- [Chien 1977][research_chien_1977]
- [Chima 2011][research_chima_2011]
- [Chiu 1987][research_chiu_1987]
- [Chiu 1987][research_chiu_1987_b]
- [Choe and Kim 2016][research_choe_kim_2016]
- [Choe et al 2020][research_choe_kim_2020]
- [Choi and Alexander 2008][research_choi_alexander_2008]
- [Choi and Driscoll 2024][research_choi_driscoll_2024]
- [Choi and Gamba 2026][research_choi_gamba_2026]
- [Choi and Menon 2009][research_choi_menon_2009]
- [Choi and Yang 2003][research_choi_yang_2003]
- [Choi and Yang 2014][research_choi_yang_2014]
- [Choi et al 2002][research_choi_sasoh_2002]
- [Choi et al 2005][research_choi_ma_2005]
- [Choi et al 2009][research_choi_yoon_2009]
- [Choi et al 2011][research_choi_noh_2011]
- [Choi et al 2026][research_choi_choi_2026]
- [Chokani 2001][research_chokani_2001]
- [Chou and Smith 1974][research_chou_smith_1974]
- [Chou et al 1996][research_chou_shen_1996]
- [Choubey and Pandey 2018][research_choubey_pandey_2018]
- [Choubey and Tiwari 2022][research_choubey_tiwari_2022]
- [Choubey and Tiwari 2022][research_choubey_tiwari_2022_b]
- [Choubey and Tiwari 2022][research_choubey_tiwari_2022_c]
- [Choubey et al 2016][research_choubey_pandey_2016]
- [Choubey et al 2021][research_choubey_yadav_2021]
- [Choubey et al 2022][research_choubey_gaud_2022]
- [Choubey et al 2023][research_choubey_solanki_2023]
- [Choubey et al 2023][research_choubey_solanki_2023_b]
- [Choubey et al 2027][research_choubey_panging_2027]
- [Chourushi et al 2021][research_chourushi_singh_2021]
- [Chow 1979][research_chow_1979]
- [Chow and Gao 2004][research_chow_gao_2004]
- [Chrusciel 1976][research_chrusciel_1976]
- [Chuang and Morimoto 1996][research_chuang_morimoto_1996]
- [Chuang and Morimoto 1997][research_chuang_morimoto_1997]
- [Chuanzhen et al 2022][research_chuanzhen_xufei_2022]
- [Chuck and Eberhardt 1990][research_chuck_eberhardt_1990]
- [Chudej 1993][research_chudej_1993]
- [Chudoba 2019][research_chudoba_2019]
- [Chudoba 2019][research_chudoba_2019_b]
- [Chudoba et al 2015][research_chudoba_haney_2015]
- [Chun 1991][research_chun_1991]
- [Chun and Burr 1969][research_chun_burr_1969]
- [Cisneros-Garibay et al 2020][research_cisnerosgaribay_buchta_2020]
- [Cisneros-Garibay et al 2022][research_cisnerosgaribay_pantano_2022]
- [Clarey and Greendyke 2018][research_clarey_greendyke_2018]
- [Clark 1965][research_clark_1965]
- [Clark 1966][research_clark_1966]
- [Clark et al 2006][research_clark_mirmirani_2006]
- [Clark et al 2006][research_clark_wu_2006]
- [Clarke 1989][research_clarke_1989]
- [Clarke 2008][research_clarke_2008]
- [Clauser 1954][research_clauser_1954]
- [Clauss et al 1994][research_clauss_sontgen_1994]
- [Clemens 2010][research_clemens_2010]
- [Clement 2018][research_clement_2018]
- [Cliff and Well 1991][research_cliff_well_1991]
- [Cliff et al 1992][research_cliff_well_1992]
- [Coats 1981][research_coats_1981]
- [Cockrell, Charles E., Jr. 1993][research_cockrellcharlesejr_1993]
- [Cockrell, Charles E., Jr. 1994][research_cockrellcharlesejr_1994]
- [Cockrell, Charles Edward, Jr. 1994][research_cockrellcharlesedwardjr_1994]
- [Cockrell, Jr. and Huebner 1991][research_cockrelljr_huebner_1991]
- [Cockrell, s E, Jr et al 1995][research_cockrellsejr_huebner_1995]
- [Cocks et al 2013][research_cocks_donohue_2013]
- [Cohen 1968][research_cohen_1968]
- [Cohen 2011][research_cohen_2011]
- [Cohen et al 1997][research_cohen_natan_1997]
- [Cohen-Zur and Natan 1998][research_cohenzur_natan_1998]
- [Cole 1988][research_cole_1988]
- [Cole et al 1980][research_cole_cook_1980]
- [Collins, Timothy J. et al 2005][research_collinstimothyj_congdonwilliamm_2005]
- [Colman et al 1968][research_colman_mayell_1968]
- [Colwill et al 1969][research_colwill_curran_1969]
- [Combustion and Chemical Kinetics 1978][research_combustion_and_1978]
- [Combustion Chemistry of Chain 1978][research_combustion_chemistry_1978]
- [Combustion in Supersonic Flows 2006][research_combustion_in_2006]
- [Combustion of High-Energy Fuels 2001][research_combustion_of_2001]
- [Combustion Scaling in an 2012][research_combustion_scaling_2012]
- [Comfort and Todisco 1969][research_comfort_todisco_1969]
- [Comparative Applicability Of Storable 1960][research_comparative_applicability_1960]
- [Comparison of flowfield surveys 1994][research_comparison_of_1994]
- [Comparison of high-altitude rocket 1960][research_comparison_of_1960]
- [Comparison of high-altitude rocket 1960][research_comparison_of_1960_b]
- [Comparison of Orbiter STS-2 1983][research_comparison_of_1983]
- [Computational Fluid Dynamic Methods 2009][research_computational_fluid_2009]
- [Computational Fluid Dynamics Continuity 2000][research_computational_fluid_2000_b]
- [Computational Fluid Dynamics Design 1990][research_computational_fluid_1990]
- [Computational fluid dynamics Free 2014][research_computational_fluid_2014]
- [Computational Fluid Dynamics Using 2000][research_computational_fluid_2000]
- [Computational-Fluid-Dynamic Solutions of Hypersonic 2006][research_computational_fluid_dynamic_solutions_2006]
- [Computational-Fluid-Dynamic Solutions of Hypersonic 2019][research_computational_fluid_dynamic_solutions_2019]
- [Comstock][research_comstock]
- [Cong and Kunfeng 2017][research_cong_kunfeng_2017]
- [Congress will hasten US 2024][research_congress_will_2024]
- [Coniglio][research_coniglio]
- [Connelly 2008][research_connelly_2008]
- [Connolly and Loth 2020][research_connolly_loth_2020]
- [Connolly and Loth 2021][research_connolly_loth_2021]
- [Connolly et al 2021][research_connolly_krouse_2021]
- [Control system design using 1976][research_control_system_1976]
- [Conversion of coal to 2004][research_conversion_of_2004]
- [Conway and Johansson 2001][research_conway_johansson_2001]
- [Cook][research_cook]
- [Cook 1981][research_cook_1981]
- [Cookson 1976][research_cookson_1976]
- [Corbin et al 2008][research_corbin_wolff_2008]
- [Cornell Aeronautical Lab Inc Buffalo Ny 1963][research_cornellaeronauticallabincbuffalony_1963]
- [Correction to "Shape Optimization 2026][research_correction_to_2026]
- [Corso and V. 1966][research_corso_v_1966]
- [Corton 1966][research_corton_1966]
- [Coupled dynamic model of 2018][research_coupled_dynamic_2018]
- [Courtland 2010][research_courtland_2010]
- [Cousin 1967][research_cousin_1967]
- [Coutant and Keigley 1988][research_coutant_keigley_1988]
- [Couture et al 2008][research_couture_dechamplain_2008]
- [Cox et al 1973][research_cox_cairns_1973]
- [Cox et al 1995][research_cox_lewis_1995]
- [Crachi et al 2024][research_crachi_pizzarelli_2024]
- [Craig 2022][research_craig_2022]
- [Craig and Reich 1981][research_craig_reich_1981]
- [Cramer 2001][research_cramer_2001]
- [Creating Hypersonic Flow in 2019][research_creating_hypersonic_2019]
- [Creating Hypersonic Flow in 2019][research_creating_hypersonic_2019_b]
- [Cresci 1966][research_cresci_1966]
- [Cresci and Rubin 1980][research_cresci_rubin_1980]
- [Cristiano Paulino Pereira et al 2021][research_cristianopaulinopereira_marinho_2021]
- [Crow et al 2012][research_crow_boyd_2012]
- [Crown 1950][research_crown_1950]
- [Crumpton 2024][research_crumpton_2024]
- [Cubbage et al 1970][research_cubbage_johnston_1970]
- [Cui 2021][research_cui_2021]
- [Cui et al 2011][research_cui_lv_2011]
- [Cui et al 2015][research_cui_hu_2015]
- [Cui et al 2018][research_cui_mei_2018]
- [Cui et al 2022][research_cui_jia_2022]
- [Culick et al 1982][research_culick_marble_1982]
- [Culick et al 1983][research_culick_marble_1983]
- [Culick et al 1985][research_culick_marble_1985]
- [Culler and McNamara 2011][research_culler_mcnamara_2011]
- [Culler et al 2007][research_culler_williams_2007]
- [Cuppoletti et al 2020][research_cuppoletti_ombrello_2020]
- [Curran 1996][research_curran_1996]
- [Curran and Craig 1973][research_curran_craig_1973]
- [Curran et al 2003][research_curran_hunt_2003]
- [Cusimano and Johnson 1994][research_cusimano_johnson_1994]
- [Cutler, Andrew D. et al 2013][research_cutlerandrewd_magnottigaetano_2013]
- [Cutrone 2023][research_cutrone_2023]
- [Cutrone and Schettino 2024][research_cutrone_schettino_2024]
- [Cvrlje 1999][research_cvrlje_1999]
- [Cvrlje and Laschka 2001][research_cvrlje_laschka_2001]
- [Cvrlje et al 2000][research_cvrlje_breitsamter_2000]
- [Cymbalist and Dimotakis 2013][research_cymbalist_dimotakis_2013]
- [Czysz 1963][research_czysz_1963]
- [Czysz 1963][research_czysz_1963_b]
- [Czysz 1988][research_czysz_1988]
- [Czysz and Murthy 1996][research_czysz_murthy_1996]
- [Czysz et al 1997][research_czysz_froning_1997]
- [Cámara et al 2011][research_camara_gatta_2011]
- [D'Amico et al 2004][research_damico_simon_2004]
- [da Costa et al 2016][research_dacosta_rolim_2016]
- [da Costa et al 2018][research_dacosta_dasilva_2018]
- [da Silva Junior et al 2018][research_dasilvajunior_pinto_2018]
- [Dafler 1962][research_dafler_1962]
- [Dai et al 2023][research_dai_zhao_2023]
- [Dai et al 2024][research_dai_chen_2024]
- [Dai et al 2024][research_dai_li_2024]
- [Daines and Segal 1998][research_daines_segal_1998]
- [Daines et al 1975][research_daines_boardman_1975]
- [Dajun et al 2006][research_dajun_guobiao_2006]
- [Daliri et al 2018][research_daliri_farahani_2018]
- [Dalle and Driscoll 2012][research_dalle_driscoll_2012]
- [Dalle et al 2010][research_dalle_frendreis_2010]
- [Dalle et al 2011][research_dalle_torrez_2011]
- [Dalle et al 2011][research_dalle_torrez_2011_b]
- [Dalle et al 2015][research_dalle_driscoll_2015]
- [Dalle et al 2016][research_dalle_rogers_2016]
- [Damazo et al 2012][research_damazo_ziegler_2012]
- [Dan et al 1994][research_dan_tanabe_1994]
- [Danberg 1961][research_danberg_1961]
- [Danberg et al 1964][research_danberg_schroth_1964]
- [Dane 1942][research_dane_1942]
- [Danehy et al 2015][research_danehy_bathel_2015]
- [Daniau et al 2006][research_daniau_bouchez_2006]
- [Danquah et al][research_danquah_mensah]
- [Darrah 1988][research_darrah_1988]
- [Daryabeigi, Kamran et al 2006][research_daryabeigikamran_blossermaxl_2006]
- [Das et al 2015][research_das_kim_2015]
- [Das et al 2021][research_das_pandey_2021]
- [Das et al 2025][research_das_debnath_2025]
- [Dasgupta et al 2012][research_dasgupta_choudhury_2012]
- [Dasgupta, et al 2001][research_dasgupta_krishnamoorthy_2001]
- [Dassoulas 1963][research_dassoulas_1963]
- [Daub et al 2020][research_daub_esser_2020]
- [Daum 1963][research_daum_1963]
- [David E Glass][research_davideglass]
- [David E Glass][research_davideglass_b]
- [David E Glass][research_davideglass_c]
- [David O. Sigthorsson 2006][research_davidosigthorsson_2006]
- [Davidson, J. et al 1999][research_davidsonj_lallmanf_1999]
- [Davis 1970][research_davis_1970]
- [Davis 1984][research_davis_1984]
- [Davis 1984][research_davis_1984_b]
- [Davis 1985][research_davis_1985]
- [Davis 1988][research_davis_1988]
- [Davis 1993][research_davis_1993]
- [Davis 1995][research_davis_1995]
- [Davis 2015][research_davis_2015]
- [Daywitt et al 1993][research_daywitt_bhutta_1993]
- [de Boer et al 2015][research_deboer_flourens_2015]
- [de Moura and Ribeiro 2026][research_demoura_ribeiro_2026]
- [De Rosa et al 2026][research_derosa_gulizzi_2026]
- [de Siqueira and Ribeiro 2023][research_desiqueira_ribeiro_2023]
- [De Tullio and Sandham 2012][research_detullio_sandham_2012]
- [De VAULT 1957][research_devault_1957]
- [Debiève and Dupont 2009][research_debieve_dupont_2009]
- [DeBoskey et al 2026][research_deboskey_sahoo_2026]
- [Debtera 2022][research_debtera_2022]
- [Dec and Mitcheltree 2002][research_dec_mitcheltree_2002]
- [Decker 2010][research_decker_2010]
- [Decker and Laschka 2001][research_decker_laschka_2001]
- [Deegan et al 2018][research_deegan_duan_2018]
- [Deepak et al 2006][research_deepak_jagadeesh_2006]
- [Definition of the standard 1954][research_definition_of_1954]
- [Degrez and Ginoux 1983][research_degrez_ginoux_1983]
- [Degrez and Ginoux 1987][research_degrez_ginoux_1987]
- [Delale and Liaw 1989][research_delale_liaw_1989]
- [DeMange et al 2007][research_demange_dunlap_2007]
- [Demetriades 1975][research_demetriades_1975]
- [Demetriades 1983][research_demetriades_1983]
- [Demetriades 1985][research_demetriades_1985]
- [Demir et al 2025][research_demir_ozturkmen_2025]
- [Demo 1986][research_demo_1986]
- [Dendy et al 2026][research_dendy_hayes_2026]
- [Deng 2026][research_deng_2026]
- [Deng and Kim 2017][research_deng_kim_2017]
- [Deng and Zhao 2026][research_deng_zhao_2026]
- [Deng et al 2017][research_deng_jin_2017]
- [Denman][research_denman]
- [Denney et al 2012][research_denney_tai_2012]
- [Dennis P. Dykstra 1980][research_dennispdykstra_1980]
- [DePalma 1976][research_depalma_1976]
- [Depiro][research_depiro]
- [Desbordes et al 1995][research_desbordes_hamada_1995]
- [Deshpande and Poggie 2017][research_deshpande_poggie_2017]
- [Deshpande and Poggie 2020][research_deshpande_poggie_2020]
- [Deshpande and Poggie 2021][research_deshpande_poggie_2021]
- [Design Considerations for a 1963][research_design_considerations_1963]
- [Design of a hypersonic 1993][research_design_of_1993]
- [DeSpirito 2009][research_despirito_2009]
- [DeSpirito 2013][research_despirito_2013]
- [DeSpirito 2014][research_despirito_2014]
- [Dessornes and Scherrer 2005][research_dessornes_scherrer_2005]
- [Dessornes et al 2001][research_dessornes_scherrer_2001]
- [Dettling and Mcintyre 1978][research_dettling_mcintyre_1978]
- [Development of friction-seal materials 1957][research_development_of_1957]
- [Development of the Shock 1962][research_development_of_1962]
- [Dewell and Speyer 1993][research_dewell_speyer_1993]
- [Dharavath et al 2014][research_dharavath_manna_2014]
- [Dharavath et al 2015][research_dharavath_manna_2015]
- [Dharavath et al 2015][research_dharavath_manna_2015_b]
- [Dharavath et al 2023][research_dharavath_manna_2023]
- [Di Clemente et al 2009][research_diclemente_rufolo_2009]
- [Di Febo and Pasquale 2016][research_difebo_pasquale_2016]
- [Di Giovanni and Stemmer 2018][research_digiovanni_stemmer_2018]
- [Di Stefano et al 2018][research_distefano_hosder_2018]
- [Di Stefano et al 2020][research_distefano_hosder_2020]
- [Diagnostic Studies of a 1962][research_diagnostic_studies_1962]
- [Diao et al 2022][research_diao_lu_2022]
- [Dickeson et al 2009][research_dickeson_rodriguez_2009]
- [Dickhudt 1983][research_dickhudt_1983]
- [Dicristina 1979][research_dicristina_1979]
- [Dietrick 2013][research_dietrick_2013]
- [Diggins 1951][research_diggins_1951]
- [Dimotakis and Leonard 1998][research_dimotakis_leonard_1998]
- [Dinda et al 2021][research_dinda_vuchuru_2021]
- [Ding et al 2015][research_ding_liu_2015]
- [Ding et al 2018][research_ding_liu_2018]
- [Ding et al 2020][research_ding_wang_2020]
- [Ding et al 2021][research_ding_liu_2021]
- [Ding et al 2022][research_ding_zhuo_2022]
- [Ding et al 2023][research_ding_li_2023]
- [Direct numerical simulations of 2023][research_direct_numerical_2023]
- [Diskin, Glenn S. et al 1987][research_diskinglenns_jachimowskicj_1987]
- [Dismountable, slidable tube support 1996][research_dismountable_slidable_1996]
- [Disturbance Rejection For Airbreathing 2016][research_disturbance_rejection_2016]
- [Dittert and Kütemeyer 2017][research_dittert_kutemeyer_2017]
- [Diver and Pavlovic 1984][research_diver_pavlovic_1984]
- [Djanal-Mann and Murugan 2025][research_djanalmann_murugan_2025]
- [Do et al 2010][research_do_cappelli_2010]
- [Do et al 2010][research_do_im_2010]
- [Do et al 2011][research_do_im_2011]
- [Do et al 2011][research_do_im_2011_b]
- [Do et al 2011][research_do_im_2011_c]
- [Do et al 2011][research_do_im_2011_d]
- [Do et al 2012][research_do_passaro_2012]
- [Do et al 2024][research_do_nguyen_2024]
- [Dobronski 1988][research_dobronski_1988]
- [Dodd 1980][research_dodd_1980]
- [Doherty][research_doherty]
- [Doherty][research_doherty_b]
- [Dolan 1970][research_dolan_1970]
- [Dolling 1993][research_dolling_1993]
- [Dolling 2000][research_dolling_2000]
- [Dolling and Gramann 1986][research_dolling_gramann_1986]
- [Dolnik and Michaels 2025][research_dolnik_michaels_2025]
- [Dolvin 2009][research_dolvin_2009]
- [Domack 1991][research_domack_1991]
- [Domel and Thompson 1991][research_domel_thompson_1991]
- [Donbar 2012][research_donbar_2012]
- [Donbar et al 2000][research_donbar_gruber_2000]
- [Donelson et al 1989][research_donelson_lewerenz_1989]
- [Dong and Cai 2017][research_dong_cai_2017]
- [Dong and Li 2012][research_dong_li_2012]
- [Dong et al 2015][research_dong_huo_2015]
- [Dong et al 2021][research_dong_guo_2021]
- [Dong et al 2023][research_dong_huang_2023]
- [Donohue 2013][research_donohue_2013]
- [Donohue 2014][research_donohue_2014]
- [Donohue, James M. 2012][research_donohuejamesm_2012]
- [Doolan 2006][research_doolan_2006]
- [Doronzo 2026][research_doronzo_2026]
- [dos Santos et al 2025][research_dossantos_passaro_2025]
- [Doster et al 2007][research_doster_king_2007]
- [Doty et al 2011][research_doty_camberos_2011]
- [Dou et al 2024][research_dou_yu_2024]
- [Douglas and Bhushan 2025][research_douglas_bhushan_2025]
- [Douglas and Bhushan 2025][research_douglas_bhushan_2025_b]
- [Douglas and Lindgren 1999][research_douglas_lindgren_1999]
- [Doulati et al 2011][research_doulati_baafi_2011]
- [Draper and Lee 2019][research_draper_lee_2019]
- [Draper et al 1977][research_draper_lanejr_1977]
- [Drikakis and Rana 2015][research_drikakis_rana_2015]
- [Drummond 1958][research_drummond_1958]
- [Drummond 1991][research_drummond_1991]
- [Drummond 1992][research_drummond_1992]
- [Drummond and Weidner 1981][research_drummond_weidner_1981]
- [Drummond, J. P. et al 2007][research_drummondjp_danehypaulm_2007]
- [Drummond, J. Philip et al 1989][research_drummondjphilip_carpentermarkh_1989]
- [Drummond, J. Philip et al 2002][research_drummondjphilip_cockrellcharlesejr_2002]
- [Ds 2021][research_ds_2021]
- [Du et al 2017][research_du_wan_2017]
- [Du et al 2018][research_du_huang_2018]
- [Du et al 2022][research_du_shen_2022]
- [Du et al 2023][research_du_wang_2023]
- [Du et al 2025][research_du_chen_2025]
- [Du et al 2026][research_du_li_2026]
- [Dual-Mode Combustion Scramjet 2022][research_dual_mode_combustion_2022]
- [Duan and Zhang 2016][research_duan_zhang_2016]
- [Duan et al 2011][research_duan_sun_2011]
- [Duan et al 2024][research_duan_xu_2024]
- [Dubey et al 2025][research_dubey_gupta_2025]
- [Dubinin et al 2009][research_dubinin_fink_2009]
- [Ducati and Giannini 1964][research_ducati_giannini_1964]
- [Ducati et al 1965][research_ducati_giannini_1965]
- [Dudebout and Sislian 1994][research_dudebout_sislian_1994]
- [Dudin 2002][research_dudin_2002]
- [Dudley and Ukeiley 2011][research_dudley_ukeiley_2011]
- [Duesbery and Louat 1992][research_duesbery_louat_1992]
- [Duesbery and Louat 1994][research_duesbery_louat_1994]
- [Duffy 1968][research_duffy_1968]
- [Duffy and Shattuck 1975][research_duffy_shattuck_1975]
- [Duffy and Shattuck 1975][research_duffy_shattuck_1975_b]
- [Dufour and Bouchez 2001][research_dufour_bouchez_2001]
- [Dugan, Jr. 1969][research_duganjr_1969]
- [Dugger 1959][research_dugger_1959]
- [Dugundji 1965][research_dugundji_1965]
- [Dukowicz 1968][research_dukowicz_1968]
- [Dunagan][research_dunagan]
- [Dunn 1980][research_dunn_1980]
- [Dupont et al 2011][research_dupont_debieve_2011]
- [Duran 2026][research_duran_2026]
- [Duran and Zeng 2026][research_duran_zeng_2026]
- [Durant et al 2015][research_durant_andre_2015]
- [Durbin 1959][research_durbin_1959]
- [Duston et al 2004][research_duston_seghi_2004]
- [Dutczak 2006][research_dutczak_2006]
- [Dutt 1980][research_dutt_1980]
- [Dutta et al 2011][research_dutta_yin_2011]
- [Duvall et al 1985][research_duvall_hale_1985]
- [Dvorák et al 2010][research_dvorak_kavecky_2010]
- [Dvořák 1965][research_dvorak_1965]
- [Dwoyer 1973][research_dwoyer_1973]
- [Dwoyer and Kumar 1987][research_dwoyer_kumar_1987]
- [Dwyer 1994][research_dwyer_1994]
- [Dyakonov et al 2012][research_dyakonov_schoenenberger_2012]
- [Dzhafarov et al 1996][research_dzhafarov_altunbas_1996]
- [Díaz 1999][research_diaz_1999]
- [E. C. Schwegler - Lanl and A. Place - Honeywell 2000][research_ecschweglerlanl_aplacehoneywell_2000]
- [Eagle and Ross 1955][research_eagle_ross_1955]
- [Early 2000][research_early_2000]
- [Eason and Spottswood 2013][research_eason_spottswood_2013]
- [Ebrahimi et al 2007][research_ebrahimi_gaitonde_2007]
- [Eckert and Bradt 1984][research_eckert_bradt_1984]
- [ECO Demonstrator Begins Flight 2018][research_eco_demonstrator_2018]
- [Economos 1962][research_economos_1962]
- [Edelman and Spadaccini 1969][research_edelman_spadaccini_1969]
- [Edelman et al 1980][research_edelman_harsha_1980]
- [Edquist 2006][research_edquist_2006]
- [Edquist and Lewis 1993][research_edquist_lewis_1993]
- [Edwards 2014][research_edwards_2014]
- [Edwards and Babikian 1987][research_edwards_babikian_1987]
- [Edwards et al 1951][research_edwards_speiser_1951]
- [Edwards et al 1975][research_edwards_small_1975]
- [Edwards et al 2006][research_edwards_dewitt_2006]
- [Edwards et al 2011][research_edwards_fulton_2011]
- [Edwards et al 2024][research_edwards_arbolino_2024]
- [Effect of Inlet Velocity 2016][research_effect_of_2016]
- [Effect of the Configuration 2017][research_effect_of_2017]
- [Effects of chemical nonequilibrium 1969][research_effects_of_1969]
- [Effects of compression and 1993][research_effects_of_1993]
- [Effects of Feeding Mode 2021][research_effects_of_2021]
- [Effects of wind-tunnel disturbances 1972][research_effects_of_1972]
- [Efficient thermal management of 2002][research_efficient_thermal_2002]
- [Eggers 2002][research_eggers_2002]
- [Eggers 2003][research_eggers_2003]
- [Eggers and Novelli 1999][research_eggers_novelli_1999]
- [Eggers et al 2001][research_eggers_novelli_2001]
- [Eglin et al 2025][research_eglin_embacher_2025]
- [Egorov and Erofeev 1997][research_egorov_erofeev_1997]
- [Egusquiza and Virto 1982][research_egusquiza_virto_1982]
- [Eklund 2004][research_eklund_2004]
- [Eklund et al 2001][research_eklund_baurle_2001]
- [El-Askary 2011][research_elaskary_2011]
- [El-Kebir and Ornik 2020][research_elkebir_ornik_2020]
- [El-Sayed 2016][research_elsayed_2016]
- [Elands et al 1991][research_elands_dijkstra_1991]
- [Elchert 1982][research_elchert_1982]
- [Elder 1980][research_elder_1980]
- [Eldridge 1988][research_eldridge_1988]
- [Elements of Computational Engine/Airframe 1986][research_elements_of_1986]
- [Elgar and Raubenheimer 2011][research_elgar_raubenheimer_2011]
- [Elizabeth F Rieken et al 2020][research_elizabethfrieken_scottaberry_2020]
- [Elkoby 2005][research_elkoby_2005]
- [Elkowitz et al 2023][research_elkowitz_wanchek_2023]
- [Elliott 1968][research_elliott_1968]
- [Elliott et al 2019][research_elliott_houpt_2019]
- [Ellison, J. C. and Johnson, C. B. 1964][research_ellisonjc_johnsoncb_1964]
- [Ely][research_ely]
- [Emami et al 1995][research_emami_rodi_1995]
- [Emami, Saied et al 1995][research_emamisaied_trexlercarla_1995]
- [Emanuel 1992][research_emanuel_1992]
- [Emanuel 1992][research_emanuel_1992_b]
- [Emanuel and Yi 2000][research_emanuel_yi_2000]
- [Endothermic Reactions][research_endothermic_reactions]
- [Endothermic Reactions 2006][research_endothermic_reactions_2006]
- [Endothermic reactors for an 1996][research_endothermic_reactors_1996]
- [Engblom et al 2005][research_engblom_frate_2005]
- [Engblom et al 2012][research_engblom_bellamkonda_2012]
- [Engelund 2001][research_engelund_2001]
- [Engine/Airframe Performance Matching 1989][research_engine_airframe_performance_1989]
- [Enkenhus 1969][research_enkenhus_1969]
- [Enkenhus and Parazzoli 1969][research_enkenhus_parazzoli_1969]
- [Epstein 1954][research_epstein_1954]
- [Erb and Hosder 2018][research_erb_hosder_2018]
- [Erdos 1998][research_erdos_1998]
- [Ericsson 1968][research_ericsson_1968]
- [Ericsson 1977][research_ericsson_1977]
- [Ericsson 1977][research_ericsson_1977_b]
- [Ericsson 1978][research_ericsson_1978]
- [Ericsson and Scholnick 1968][research_ericsson_scholnick_1968]
- [Ertunç and Durst 2008][research_ertunc_durst_2008]
- [Eschenbach and Skinner 1961][research_eschenbach_skinner_1961]
- [Escher 1996][research_escher_1996]
- [Escher 2001][research_escher_2001]
- [Escher and Ehrlic 2000][research_escher_ehrlic_2000]
- [Espinosa 2003][research_espinosa_2003]
- [Essenhigh 2006][research_essenhigh_2006]
- [Estimation of Ideal Specific 2025][research_estimation_of_ideal_2025]
- [Eugênio Ribeiro][research_eugenioribeiro]
- [Evaluation of turbulent heating 1973][research_evaluation_of_1973]
- [Evans et al 2011][research_evans_zok_2011]
- [Everett et al 1972][research_everett_cashwell_1972]
- [Eves and Valasek 2024][research_eves_valasek_2024]
- [Evolution of Disturbances from 2024][research_evolution_of_disturbances_2024]
- [Experimental Study of the 2022][research_experimental_study_2022]
- [Facility Requirements for Hypersonic 1991][research_facility_requirements_1991]
- [Fain et al 2026][research_fain_lambert_2026]
- [Falempin 1999][research_falempin_1999]
- [Falempin and Serre 2003][research_falempin_serre_2003]
- [Falempin and Serre 2003][research_falempin_serre_2003_b]
- [Falempin and Serre 2006][research_falempin_serre_2006]
- [Falempin and Serre 2006][research_falempin_serre_2006_b]
- [Falempin and Serre 2008][research_falempin_serre_2008]
- [Falempin et al 1992][research_falempin_forrat_1992]
- [Falempin et al 1995][research_falempin_thevenot_1995]
- [Falempin et al 2009][research_falempin_minard_2009]
- [Falkiewicz et al 2009][research_falkiewicz_cesnik_2009]
- [Falkiewicz et al 2010][research_falkiewicz_cesnik_2010]
- [Falkiewicz et al 2011][research_falkiewicz_frendreis_2011]
- [Famularo et al 2018][research_famularo_whitney_2018]
- [Fan and Chang 2009][research_fan_chang_2009]
- [Fan et al 2009][research_fan_liu_2009]
- [Fan et al 2010][research_fan_chang_2010]
- [Fan et al 2016][research_fan_yan_2016]
- [Fan et al 2016][research_fan_zhu_2016]
- [Fan et al 2017][research_fan_bing_2017]
- [Fan et al 2017][research_fan_lu_2017]
- [Fan et al 2017][research_fan_wu_2017]
- [Fan et al 2017][research_fan_yan_2017]
- [Fan et al 2024][research_fan_qi_2024]
- [Fan et al 2026][research_fan_cheng_2026]
- [Fang et al 2020][research_fang_xianyao_2020]
- [Fang et al 2024][research_fang_jiang_2024]
- [Farahani et al 2019][research_farahani_daliri_2019]
- [Farmakovsky et al 2005][research_farmakovsky_vinogradova_2005]
- [Farrell and Martin 1998][research_farrell_martin_1998]
- [Fatemi and Lemmen 2006][research_fatemi_lemmen_2006]
- [Fathauer and Rogers 1993][research_fathauer_rogers_1993]
- [Faulkner 2003][research_faulkner_2003]
- [Faulkner and Weber 1999][research_faulkner_weber_1999]
- [Faulstich and Law 2006][research_faulstich_law_2006]
- [Fechter and Mills 1988][research_fechter_mills_1988]
- [Fedioun and Orlik 2012][research_fedioun_orlik_2012]
- [Fedorov and Khokhlov 2001][research_fedorov_khokhlov_2001]
- [Fedorov and Khokhlov 2002][research_fedorov_khokhlov_2002]
- [Feie and Kretz 2008][research_feie_kretz_2008]
- [Feifel and Kerkam 1992][research_feifel_kerkam_1992]
- [Fejer et al 1964][research_fejer_heath_1964]
- [Felderman et al 2003][research_felderman_shope_2003]
- [Feldman, Jay et al 2019][research_feldmanjay_stewartdavid_2019]
- [Felippe da Silva Lui][research_felippedasilvalui]
- [Fenfen et al 2020][research_fenfen_xubo_2020]
- [Feng 2022][research_feng_2022]
- [Feng and Zhang 2016][research_feng_zhang_2016]
- [Feng et al 2014][research_feng_tang_2014]
- [Feng et al 2017][research_feng_tan_2017]
- [Feng et al 2020][research_feng_lv_2020]
- [Feng et al 2022][research_feng_wang_2022]
- [Feng et al 2023][research_feng_luo_2023]
- [Feng et al 2026][research_feng_tang_2026]
- [Ferguson and Anderson, Jr. 1993][research_ferguson_andersonjr_1993]
- [Ferguson et al 2011][research_ferguson_dhanasar_2011]
- [Ferguson et al 2015][research_ferguson_dasque_2015]
- [Ferguson et al 2015][research_ferguson_dhanasar_2015]
- [Ferguson et al 2016][research_ferguson_dasque_2016]
- [Ferguson et al 2018][research_ferguson_dasque_2018]
- [Ferguson et al 2022][research_ferguson_feng_2022]
- [Fergusson][research_fergusson]
- [Ferlemann 2005][research_ferlemann_2005]
- [Ferlemann et al 2005][research_ferlemann_mcclinton_2005]
- [Fermen-Coker and Johnson 1999][research_fermencoker_johnson_1999]
- [Ferreira et al 1996][research_ferreira_carvalhojr_1996]
- [Ferrero 2020][research_ferrero_2020]
- [Ferrier et al 2006][research_ferrier_fedioun_2006]
- [Ferrier et al 2008][research_ferrier_orlik_2008]
- [Ferziger and Leslie 1979][research_ferziger_leslie_1979]
- [Fetterhoff and Burfitt 2011][research_fetterhoff_burfitt_2011]
- [Filipkovskyi 2026][research_filipkovskyi_2026]
- [Finkler and Weiser 1994][research_finkler_weiser_1994]
- [Finley 1990][research_finley_1990]
- [Finley and Cockrell 1995][research_finley_cockrell_1995]
- [Fiorentini and Serrani 2012][research_fiorentini_serrani_2012]
- [Fiorentini et al 2009][research_fiorentini_serrani_2009]
- [Fischer 2006][research_fischer_2006]
- [Fischer and Olivier 2011][research_fischer_olivier_2011]
- [Fitch 1966][research_fitch_1966]
- [Fiévet et al 2015][research_fievet_koo_2015]
- [Flaherty et al 2010][research_flaherty_andrews_2010]
- [Flanagan, Jr. 1993][research_flanaganjr_1993]
- [Fleming et al 2004][research_fleming_olcman_2004]
- [Flesberg et al 2018][research_flesberg_taghavi_2018]
- [Fletcher 1967][research_fletcher_1967]
- [Fletcher 1994][research_fletcher_1994]
- [Flight Sciences Lab Inc Buffalo Ny 1964][research_flightscienceslabincbuffalony_1964]
- [Flight Test Instrumentation 1965][research_flight_test_1965]
- [Flight TEST Manual 1959][research_flight_test_1959]
- [Flight Test Planning 2021][research_flight_test_2021]
- [Flora et al 2019][research_flora_capasso_2019]
- [Florence 1979][research_florence_1979]
- [Flow establishment in a 1990][research_flow_establishment_1990]
- [Foelsche et al 2006][research_foelsche_beckel_2006]
- [Fokin 2012][research_fokin_2012]
- [Fokin 2020][research_fokin_2020]
- [Folck and Smith 1969][research_folck_smith_1969]
- [Folweiler 1962][research_folweiler_1962]
- [Fontan Moura][research_fontanmoura]
- [Fontijn 1987][research_fontijn_1987]
- [Forbes 2012][research_forbes_2012]
- [Forbes-Spyratos et al 2014][research_forbesspyratos_jahn_2014]
- [Foreman 1963][research_foreman_1963]
- [Forner and Manter 1982][research_forner_manter_1982]
- [Forrette 1964][research_forrette_1964]
- [Forsythe et al 1961][research_forsythe_melfi_1961]
- [Fort and Pratt 1990][research_fort_pratt_1990]
- [Fotia 2015][research_fotia_2015]
- [Fotia and Driscoll 2012][research_fotia_driscoll_2012]
- [Fotia and Driscoll 2013][research_fotia_driscoll_2013]
- [Franciscus 1981][research_franciscus_1981]
- [Franciscus 1981][research_franciscus_1981_b]
- [Franciscus and Lezberg 1963][research_franciscus_lezberg_1963]
- [Franciscus and Lezberg 1963][research_franciscus_lezberg_1963_b]
- [Franklin and Bennett 1971][research_franklin_bennett_1971]
- [Freed et al 2001][research_freed_dedecker_2001]
- [French 1988][research_french_1988]
- [Frey 2014][research_frey_2014]
- [Frey et al 2025][research_frey_jamme_2025]
- [Friedauer and Segal 1996][research_friedauer_segal_1996]
- [Friedman 1965][research_friedman_1965]
- [Friedman et al 1953][research_friedman_bennet_1953]
- [Friedman et al 1967][research_friedman_griffith_1967]
- [Frisch and Giedt 1965][research_frisch_giedt_1965]
- [Frisch and Giedt 1965][research_frisch_giedt_1965_b]
- [Froning 2006][research_froning_2006]
- [Froning, Jr. 1986][research_froningjr_1986]
- [Froning, Jr. and Bussard 1993][research_froningjr_bussard_1993]
- [Froning, Jr. and Roach 1999][research_froningjr_roach_1999]
- [Froning, Jr. et al 1996][research_froningjr_mckinney_1996]
- [Frost][research_frost]
- [Fry, Ronald S. and Becker, Dorothy L. 2000][research_fryronalds_beckerdorothyl_2000]
- [Fry, Ronald S. and Gannaway, Mary T. 2002][research_fryronalds_gannawaymaryt_2002]
- [Fry, Ronald S. et al 1998][research_fryronalds_gannawaymaryt_1998]
- [Fu et al 2015][research_fu_wang_2015]
- [Fu et al 2018][research_fu_li_2018]
- [Fu et al 2021][research_fu_bose_2021]
- [Fu et al 2022][research_fu_qu_2022]
- [Fu et al 2023][research_fu_song_2023]
- [Fu et al 2024][research_fu_song_2024]
- [Fu et al 2024][research_fu_song_2024_b]
- [Fu et al 2024][research_fu_wan_2024]
- [Fu et al 2026][research_fu_gong_2026]
- [Fuel cell demonstrator aeroplane 2007][research_fuel_cell_2007]
- [Fuel in high-energy rocket 1998][research_fuel_in_1998]
- [Fuels for Hypersonic Air-Breathing 2022][research_fuels_for_2022]
- [Fujii and Inoue 1998][research_fujii_inoue_1998]
- [Fujii et al 2000][research_fujii_watanabe_2000]
- [Fujii et al 2001][research_fujii_watanabe_2001]
- [Fujimatsu et al 2019][research_fujimatsu_kito_2019]
- [Fujio and Ogawa 2021][research_fujio_ogawa_2021]
- [Fujio and Taguchi 2026][research_fujio_taguchi_2026]
- [Fujioka et al 2017][research_fujioka_hirokawa_2017]
- [Fujita et al 2011][research_fujita_suzuki_2011]
- [Fukuda et al 1975][research_fukuda_reshotko_1975]
- [Fukutani and Watanabe 1986][research_fukutani_watanabe_1986]
- [Fukuzawa et al 2025][research_fukuzawa_iguchi_2025]
- [Fulmer and Wirtz 1964][research_fulmer_wirtz_1964]
- [Fulton 1966][research_fulton_1966]
- [Fureby et al 2025][research_fureby_nilsson_2025]
- [Fureby et al 2025][research_fureby_peterson_2025]
- [Furstenau 1965][research_furstenau_1965]
- [Further development and flight 1994][research_further_development_1994]
- [Fusaro and Viola 2020][research_fusaro_viola_2020]
- [Förder and Steiner 2020][research_forder_steiner_2020]
- [Förster et al 2016][research_forster_droske_2016]
- [G et al 2017][research_g_kaushik_2017]
- [G et al 2017][research_g_kaushik_2017_b]
- [G.Balu et al 2005][research_gbalu_panneerselvam_2005]
- [G.K. Suryanarayana et al 2026][research_gksuryanarayana_dbsingh_2026]
- [Gaal 1974][research_gaal_1974]
- [Gabrys and Smith 1974][research_gabrys_smith_1974]
- [Gaede and Lopez 1967][research_gaede_lopez_1967]
- [Gager and Schleter 1949][research_gager_schleter_1949]
- [Gaglio and Bevilacqua 2026][research_gaglio_bevilacqua_2026]
- [Gaiduchenko and Gritsyk 2019][research_gaiduchenko_gritsyk_2019]
- [Galaktionov et al 2006][research_galaktionov_lapygin_2006]
- [Galera et al 2006][research_galera_mohammadi_2006]
- [Gallegos et al 2024][research_gallegos_schlussel_2024]
- [Gallegos et al 2024][research_gallegos_schlussel_2024_b]
- [Galli et al 2004][research_galli_corbel_2004]
- [Gallo et al 1966][research_gallo_gnos_1966]
- [Gally and Campbell 2002][research_gally_campbell_2002]
- [Gamble et al 2008][research_gamble_giel_2008]
- [Gamble et al 2009][research_gamble_haid_2009]
- [Gamertsfelder et al 2022][research_gamertsfelder_khare_2022]
- [Ganapuram et al 2014][research_ganapuram_jangam_2014]
- [Gany 2006][research_gany_2006]
- [Gao 2023][research_gao_2023]
- [Gao et al 2012][research_gao_chang_2012]
- [Gao et al 2014][research_gao_jiang_2014]
- [Gao et al 2014][research_gao_li_2014]
- [Gao et al 2015][research_gao_li_2015]
- [Gao et al 2018][research_gao_chen_2018]
- [Gao et al 2020][research_gao_chen_2020]
- [Gao et al 2020][research_gao_zhang_2020]
- [Gao et al 2020][research_gao_zhang_2020_b]
- [Gao et al 2020][research_gao_zhang_2020_c]
- [Gao et al 2021][research_gao_an_2021]
- [Gao et al 2021][research_gao_gou_2021]
- [Gao et al 2021][research_gao_song_2021]
- [Gao et al 2023][research_gao_wang_2023]
- [Gao et al 2024][research_gao_li_2024]
- [Gao et al 2024][research_gao_sun_2024]
- [Gao et al 2024][research_gao_zhang_2024]
- [Gao et al 2026][research_gao_he_2026]
- [Gao et al 2026][research_gao_liu_2026]
- [Garavello et al 2024][research_garavello_kneish_2024]
- [Gardi et al 2015][research_gardi_delvecchio_2015]
- [Gardner 1964][research_gardner_1964]
- [Gardner et al 2002][research_gardner_paull_2002]
- [Garman and Visintainer 2022][research_garman_visintainer_2022]
- [Garrison et al 1994][research_garrison_settles_1994]
- [Gartling 1970][research_gartling_1970]
- [Gary and McDonald 2014][research_gary_mcdonald_2014]
- [Gas Temperature-Density GTD Sensor 1974][research_gas_temperature_density_1974]
- [Gasner et al 1992][research_gasner_foster_1992]
- [Gates et al 1999][research_gates_adrezin_1999]
- [Gawehn et al 2022][research_gawehn_schleutker_2022]
- [Gay and Brehm 2025][research_gay_brehm_2025]
- [Gazaix 1992][research_gazaix_1992]
- [Ge and Gan 2026][research_ge_gan_2026]
- [Gea and Vicker][research_gea_vicker]
- [Geerts and Yu 2012][research_geerts_yu_2012]
- [Geerts and Yu 2013][research_geerts_yu_2013]
- [Geerts and Yu 2015][research_geerts_yu_2015]
- [Geerts and Yu 2017][research_geerts_yu_2017]
- [Gehre][research_gehre]
- [Gehre et al 2015][research_gehre_wheatley_2015]
- [Geiger et al 2024][research_geiger_strahan_2024]
- [Geiger et al 2026][research_geiger_strahan_2026]
- [General Dynamics/Astronautics San Diego Ca 1961][research_generaldynamicsastronauticssandiegoca_1961_b]
- [General Dynamics/Astronautics San Diego Ca 1962][research_generaldynamicsastronauticssandiegoca_1962]
- [General Dynamics/Astronautics San Diegoca 1961][research_generaldynamicsastronauticssandiegoca_1961]
- [Geng et al 2017][research_geng_liu_2017]
- [Genin and Menon 2004][research_genin_menon_2004]
- [George 1963][research_george_1963]
- [George S. Delwert and Georg Eltetberg 1998][research_georgesdelwert_georgeltetberg_1998]
- [Gerbsch and Agarwal 1988][research_gerbsch_agarwal_1988]
- [Gernansky 1990][research_gernansky_1990]
- [Gerolymos et al 2003][research_gerolymos_sauret_2003]
- [Geshele et al 2013][research_geshele_polezhaev_2013]
- [Ghenai et al 2005][research_ghenai_philippidis_2005]
- [Ghodke et al 2011][research_ghodke_choi_2011]
- [Ghori et al 2023][research_ghori_narendar_2023]
- [Ghosh and Ogawa 2022][research_ghosh_ogawa_2022]
- [Giampetro 2026][research_giampetro_2026]
- [Giampetro et al 2026][research_giampetro_lindau_2026]
- [Giant liquid rheostat for 1955][research_giant_liquid_1955]
- [Gibbons et al 2021][research_gibbons_damm_2021]
- [Gibson et al 2002][research_gibson_neidhoefer_2002]
- [Gibson et al 2016][research_gibson_armiger_2016]
- [Gidzak 2015][research_gidzak_2015]
- [Giehler][research_giehler]
- [Giehler et al 2023][research_giehler_grenson_2023]
- [Gilinsky et al 2003][research_gilinsky_gonor_2003]
- [Gillum et al 1994][research_gillum_kammeyer_1994]
- [Gimelshein 2019][research_gimelshein_2019]
- [Ginoux 1966][research_ginoux_1966]
- [Girimaji and Srinivasan 2009][research_girimaji_srinivasan_2009]
- [Gladden and Melis 1994][research_gladden_melis_1994]
- [Gladden et al 1990][research_gladden_melis_1990]
- [Glass 2003][research_glass_2003]
- [Glass 2008][research_glass_2008]
- [Glass 2018][research_glass_2018]
- [Glass and Glass 2002][research_glass_glass_2002]
- [Glass and Sislian 1994][research_glass_sislian_1994]
- [Glassman 1998][research_glassman_1998]
- [Glassman and Nosek 1971][research_glassman_nosek_1971]
- [Glazov and Pashinkin 2001][research_glazov_pashinkin_2001]
- [Glazov et al 2002][research_glazov_pashinkin_2002]
- [Glenning and Bond 1962][research_glenning_bond_1962]
- [Glickstein and Powell 1987][research_glickstein_powell_1987]
- [Glickstein, M. R. and Spadaccini, L. J. 1997][research_glicksteinmr_spadaccinilj_1997]
- [Gnoffo 1989][research_gnoffo_1989]
- [Gnoffo 2007][research_gnoffo_2007]
- [Gnoffo, Peter A. 2001][research_gnoffopetera_2001]
- [Gnoffo, Peter A. et al 1987][research_gnoffopetera_mccandlessronalds_1987]
- [Gockel 1993][research_gockel_1993]
- [Godi 2024][research_godi_2024]
- [Gogineni 1991][research_gogineni_1991]
- [Goin 1961][research_goin_1961]
- [Gokulakrishnan et al 2006][research_gokulakrishnan_pal_2006]
- [Gol'dfel'd 1985][research_goldfeld_1985]
- [Goldbaum 1956][research_goldbaum_1956]
- [Goldberg and Scala 1965][research_goldberg_scala_1965]
- [Goldfeld 2003][research_goldfeld_2003]
- [Goldfeld 2019][research_goldfeld_2019]
- [Goldfeld and Nestoulia 2003][research_goldfeld_nestoulia_2003]
- [Goldfeld et al 2019][research_goldfeld_korotaeva_2019]
- [Gollan and Smart 2013][research_gollan_smart_2013]
- [Gollan et al 2011][research_gollan_gollan_2011]
- [Gollan, Rowan J. and Smart, Michael K. 2010][research_gollanrowanj_smartmichaelk_2010]
- [Golovachev 1979][research_golovachev_1979]
- [Golovachev 1979][research_golovachev_1979_b]
- [Golovachev 1981][research_golovachev_1981]
- [Golubinskii and Golubkin 1983][research_golubinskii_golubkin_1983]
- [Golubkin 1992][research_golubkin_1992]
- [Golubkin and Negoda 1995][research_golubkin_negoda_1995]
- [Golubkin and Postnov 2000][research_golubkin_postnov_2000]
- [Gong et al 2006][research_gong_yuan_2006]
- [Gong et al 2017][research_gong_bing_2017]
- [Gong et al 2024][research_gong_long_2024]
- [Gong Weijie and Tang Shuo 2010][research_gongweijie_tangshuo_2010]
- [Gonzalez 1996][research_gonzalez_1996]
- [Gonzalez et al 2025][research_gonzalez_castillo_2025]
- [Gooch 2011][research_gooch_2011]
- [Gooch 2011][research_gooch_2011_b]
- [Goodwin and Maxwell 2017][research_goodwin_maxwell_2017]
- [Goonko et al 2003][research_goonko_latypov_2003]
- [Gopal and Wilson 2016][research_gopal_wilson_2016]
- [Gopinath et al 2015][research_gopinath_vignesh_2015]
- [Gopinath et al 2019][research_gopinath_jagadeesh_2019]
- [Gorshkov and Lunev 2002][research_gorshkov_lunev_2002]
- [Goshima and Miyao 1991][research_goshima_miyao_1991]
- [Gospodarev et al 1990][research_gospodarev_isakina_1990]
- [Goss and Cook 1948][research_goss_cook_1948]
- [Gottlieb and Don 2008][research_gottlieb_don_2008]
- [Gottlieb et al 2024][research_gottlieb_mines_2024]
- [Gounko and Shumskiy 2014][research_gounko_shumskiy_2014]
- [Goyal et al 2023][research_goyal_prasad_2023]
- [Goyne et al 2006][research_goyne_hall_2006]
- [Goz and Theodoulis 2025][research_goz_theodoulis_2025]
- [Graber 1964][research_graber_1964]
- [Grady and Madzsar 1998][research_grady_madzsar_1998]
- [Grady et al 2016][research_grady_pitz_2016]
- [Graham][research_graham]
- [Grainger et al 2014][research_grainger_brieschenk_2014]
- [Grant 2013][research_grant_2013]
- [Grantz et al 1993][research_grantz_cervisi_1993]
- [Grasso and Falconi 1993][research_grasso_falconi_1993]
- [Gray 1965][research_gray_1965]
- [Green][research_green]
- [Green and Fernandez 1994][research_green_fernandez_1994]
- [Gregorek and Lee 1962][research_gregorek_lee_1962]
- [Gregory 2005][research_gregory_2005]
- [Gregory et al 1967][research_gregory_wilcox_1967]
- [Grimm 1993][research_grimm_1993]
- [Gringorten 1967][research_gringorten_1967]
- [Gringorten and Tattelman 1970][research_gringorten_tattelman_1970]
- [Grohens et al 2000][research_grohens_dufour_2000]
- [Grolmes 1968][research_grolmes_1968]
- [Gronland et al 1997][research_gronland_cambier_1997]
- [Gros 1963][research_gros_1963]
- [Grossir 2015][research_grossir_2015]
- [Grossir and Rambaud 2014][research_grossir_rambaud_2014]
- [Grossman, B. and Cinnella, P. 1990][research_grossmanb_cinnellap_1990]
- [Ground et al 2014][research_ground_zhu_2014]
- [Groves et al 2005][research_groves_serrani_2005]
- [Gruber et al 2004][research_gruber_donbar_2004]
- [Gruenig and Mayinger 1999][research_gruenig_mayinger_1999]
- [Gruhn and Gülhan 2011][research_gruhn_gulhan_2011]
- [Grunbok et al 2023][research_grunbok_miles_2023]
- [Gu et al 2009][research_gu_xu_2009]
- [Gu et al 2010][research_gu_xu_2010]
- [Guan and Yarng 1987][research_guan_yarng_1987]
- [Guan et al 2013][research_guan_wang_2013]
- [Guan Ping et al 2012][research_guanping_xueli_2012]
- [Guangbin Cai et al 2010][research_guangbincai_guangrenduan_2010]
- [Guangren et al 2015][research_guangren_yanmei_2015]
- [Gubanov 2019][research_gubanov_2019]
- [Guderley 1987][research_guderley_1987]
- [Guderley 1988][research_guderley_1988]
- [Gudimella et al 2018][research_gudimella_sinha_2018]
- [Guelhan et al 2012][research_guelhan_siebe_2012]
- [Gugulothu 2020][research_gugulothu_2020]
- [Gugulothu and Nutakki 2019][research_gugulothu_nutakki_2019]
- [Guizzo 2004][research_guizzo_2004]
- [Gunderson 1963][research_gunderson_1963]
- [Gunning et al 1954][research_gunning_luner_1954]
- [Gunning et al 1954][research_gunning_luner_1954_b]
- [Guo and Liu 2024][research_guo_liu_2024]
- [Guo et al 2016][research_guo_wang_2016]
- [Guo et al 2017][research_guo_gao_2017]
- [Guo et al 2022][research_guo_pang_2022]
- [Guo et al 2023][research_guo_pang_2023]
- [Guo et al 2023][research_guo_yang_2023]
- [Guo et al 2025][research_guo_fu_2025]
- [Guoliang et al 2017][research_guoliang_cong_2017]
- [Guotong Sun and Shuo Tang 2010][research_guotongsun_shuotang_2010]
- [Gupta][research_gupta]
- [Gupta][research_gupta_b]
- [Gupta and Agarwal 2001][research_gupta_agarwal_2001]
- [Gurtin and Soner 1990][research_gurtin_soner_1990]
- [Gusev 1990][research_gusev_1990]
- [Gusev and Chinilov 2003][research_gusev_chinilov_2003]
- [Gusev et al 1993][research_gusev_blagoveshchenskij_1993]
- [Guven et al 1996][research_guven_dane_1996]
- [Guza and Feddersen 2015][research_guza_feddersen_2015]
- [Guzmán-Bohórquez et al 2025][research_guzmanbohorquez_greco_2025]
- [Gyulikhandanov and Khoroshailov 1971][research_gyulikhandanov_khoroshailov_1971]
- [Gülçat 2010][research_gulcat_2010]
- [Gülçat 2015][research_gulcat_2015]
- [GÜlçat 2021][research_gulcat_2021]
- [H Julian Allen 1958][research_hjulianallen_1958]
- [Ha et al 2018][research_ha_yoon_2018]
- [Haas and Karanian 1980][research_haas_karanian_1980]
- [Habrard et al 2025][research_habrard_pommierbudinger_2025]
- [Hack][research_hack]
- [Hackett 1992][research_hackett_1992]
- [Hadjadj and Dussauge 2009][research_hadjadj_dussauge_2009]
- [Hagenmaier et al 1997][research_hagenmaier_sekar_1997]
- [Hagenmaier et al 2011][research_hagenmaier_eklund_2011]
- [Hagenmaier et al 2013][research_hagenmaier_boles_2013]
- [Hagseth, Paul E. and Blankson, Isaiah M. 1993][research_hagsethpaule_blanksonisaiahm_1993]
- [Hagy 1986][research_hagy_1986]
- [Hahn 2012][research_hahn_2012]
- [Hahn et al 2026][research_hahn_lax_2026]
- [Halas 1979][research_halas_1979]
- [Haley and Zhong 2017][research_haley_zhong_2017]
- [Hall 1994][research_hall_1994]
- [Hall and Poggie 2019][research_hall_poggie_2019]
- [Hall et al 2026][research_hall_schemmel_2026]
- [Hall, J. L. 2002][research_halljl_2002]
- [Hallgren and Anderson, Jr. 1991][research_hallgren_andersonjr_1991]
- [Hallion 1998][research_hallion_1998]
- [Hallion et al 1995][research_hallion_becker_1995]
- [Halter and Cliff 1991][research_halter_cliff_1991]
- [Halvarsson 1995][research_halvarsson_1995]
- [Hamba 2001][research_hamba_2001]
- [Hamba 2003][research_hamba_2003]
- [Hamed 1990][research_hamed_1990]
- [Hamed 1993][research_hamed_1993]
- [Hamed, A. and Kumar, Ajay 1992][research_hameda_kumarajay_1992]
- [Hammack and Ombrello 2021][research_hammack_ombrello_2021]
- [Hammond 1965][research_hammond_1965]
- [Hamner 2003][research_hamner_2003]
- [Han and Han 2024][research_han_han_2024]
- [Han et al 2020][research_han_sun_2020]
- [Han et al 2024][research_han_wang_2024]
- [Han et al 2024][research_han_wang_2024_b]
- [Han et al 2025][research_han_yu_2025]
- [Han et al 2027][research_han_yang_2027]
- [Hanafi][research_hanafi]
- [Hanai et al 2007][research_hanai_ozawa_2007]
- [Haney 1995][research_haney_1995]
- [Haney et al 1993][research_haney_cervisi_1993]
- [Hank et al 2006][research_hank_franke_2006]
- [Hank et al 2008][research_hank_murphy_2008]
- [Hannah and Muessig 1970][research_hannah_muessig_1970]
- [Hannemann et al 2015][research_hannemann_martinezschramm_2015]
- [Hannemann et al 2017][research_hannemann_martinezschramm_2017]
- [Hanquist and Boyd 2018][research_hanquist_boyd_2018]
- [Hansen, C. Frederick 1991][research_hansencfrederick_1991]
- [Hanumantha Rao 2023][research_hanumantharao_2023]
- [Hao and Chung 1994][research_hao_chung_1994]
- [Hao and Yongqi 2024][research_hao_yongqi_2024]
- [Hao et al 2014][research_hao_chang_2014]
- [Hao et al 2016][research_hao_chang_2016]
- [Hao et al 2016][research_hao_chang_2016_b]
- [Hao et al 2016][research_hao_wang_2016]
- [Hardie and O'Byrne 2025][research_hardie_obyrne_2025]
- [Harloff 1984][research_harloff_1984]
- [Harloff 1987][research_harloff_1987]
- [Harloff and Petrie 1987][research_harloff_petrie_1987]
- [Harney 1963][research_harney_1963]
- [Harney and Petrie 1971][research_harney_petrie_1971]
- [Harri 1964][research_harri_1964]
- [Harris 2004][research_harris_2004]
- [Harris and Albacete 1964][research_harris_albacete_1964]
- [Harris et al 1994][research_harris_hines_1994]
- [Harris et al 2023][research_harris_stokes_2023]
- [Harrison 1976][research_harrison_1976]
- [Hart 1992][research_hart_1992]
- [Hartill, W. R. et al 1978][research_hartillwr_goebeltp_1978]
- [Harvey 2011][research_harvey_2011]
- [Hasegawa 2025][research_hasegawa_2025]
- [Hasen et al 2019][research_hasen_karthikeyan_2019]
- [Hass et al 2011][research_hass_cabell_2011]
- [Hass, Neal E. et al 2010][research_hassneale_cabellkarenf_2010]
- [Hassan et al 1992][research_hassan_candler_1992]
- [Hassan et al 2001][research_hassan_kuntz_2001]
- [Hatayama et al 2025][research_hatayama_tanaka_2025]
- [Hattis 1990][research_hattis_1990]
- [Hawkins and Marquart 1995][research_hawkins_marquart_1995]
- [Hawkins and Richardson 1991][research_hawkins_richardson_1991]
- [Hayashi and Aso 1988][research_hayashi_aso_1988]
- [Hayes 1959][research_hayes_1959]
- [Hazarika and Ahmed 2021][research_hazarika_ahmed_2021]
- [He 2015][research_he_2015]
- [He et al 2009][research_he_le_2009]
- [He et al 2015][research_he_li_2015]
- [He et al 2016][research_he_liu_2016]
- [He et al 2017][research_he_liu_2017]
- [He et al 2021][research_he_gao_2021]
- [He et al 2022][research_he_chen_2022]
- [He et al 2022][research_he_tian_2022]
- [He et al 2022][research_he_wang_2022]
- [He et al 2023][research_he_liu_2023]
- [He et al 2026][research_he_zhang_2026]
- [He et al 2026][research_he_zhou_2026]
- [Head 1981][research_head_1981]
- [Heat transfer to endothermic 1991][research_heat_transfer_1991]
- [Heathman and Kelly 1966][research_heathman_kelly_1966]
- [Heberling 2020][research_heberling_2020]
- [Hedges et al 1996][research_hedges_lewis_1996]
- [Hegde et al 1987][research_hegde_reuter_1987]
- [Heinbockel, J. H. and Landry, J. G. 1995][research_heinbockeljh_landryjg_1995]
- [Heinrich 1954][research_heinrich_1954]
- [Heinrich et al 2001][research_heinrich_lucbouhali_2001]
- [Heiser 2007][research_heiser_2007]
- [Heiser and Pratt 2005][research_heiser_pratt_2005]
- [Heiser et al 1994][research_heiser_pratt_1994]
- [Heitmeier and Bissinger 1995][research_heitmeier_bissinger_1995]
- [Heitmeir et al 1992][research_heitmeir_lederer_1992]
- [Hejranfar and Moghadam 2011][research_hejranfar_moghadam_2011]
- [Hejranfar et al 2011][research_hejranfar_najafi_2011]
- [Helgeson and Chinitz 1995][research_helgeson_chinitz_1995]
- [Helicopter Engine/Airframe Interface Document][research_helicopter_engine_airframe]
- [Heller et al 1998][research_heller_sachs_1998]
- [Heller et al 2000][research_heller_holzapfel_2000]
- [Hemanth et al 2009][research_hemanth_jagadeesh_2009]
- [Hemming 1966][research_hemming_1966]
- [Henckels and Maurer][research_henckels_maurer]
- [Henderson 1987][research_henderson_1987]
- [Henderson 1991][research_henderson_1991]
- [Henderson 1999][research_henderson_1999]
- [Henry 1969][research_henry_1969]
- [Henshall and Brower 1962][research_henshall_brower_1962]
- [Henson 2017][research_henson_2017]
- [Henson and Robertson 1962][research_henson_robertson_1962]
- [Heo and Sung 2017][research_heo_sung_2017]
- [Herbert][research_herbert]
- [Herbert 1992][research_herbert_1992]
- [Herdy 2025][research_herdy_2025]
- [Herdy 2025][research_herdy_2025_b]
- [Herdy 2026][research_herdy_2026]
- [Herges et al 2012][research_herges_dutton_2012]
- [Herling et al 1985][research_herling_saheli_1985]
- [Hermann 1950][research_hermann_1950]
- [Hermann and Schmidt 1995][research_hermann_schmidt_1995]
- [Hermann, R. 1965][research_hermannr_1965]
- [Herrlin and Gelderloos 1988][research_herrlin_gelderloos_1988]
- [Herrmann and Gülhan 2015][research_herrmann_gulhan_2015]
- [Herrmann et al 2013][research_herrmann_siebe_2013]
- [Herrmann et al 2025][research_herrmann_cox_2025]
- [Hersh and Gerstein 1970][research_hersh_gerstein_1970]
- [Hertzberg et al 1961][research_hertzberg_wittliff_1961]
- [Hexia et al 2014][research_hexia_huijun_2014]
- [Hicks, John W. 1992][research_hicksjohnw_1992]
- [Higashino et al 1995][research_higashino_matsuo_1995]
- [Higgins et al 2002][research_higgins_inger_2002]
- [High specific impulse propulsion 1987][research_high_specific_1987]
- [High temperature materials][research_high_temperature]
- [High-altitude atmospheric density 1960][research_high_altitude_atmospheric_1960]
- [High-Temperature Gas Dynamics and 2009][research_high_temperature_gas_2009]
- [High-temperature investigations of the 2018][research_high_temperature_investigations_2018]
- [High-Temperature Materials and Mechanisms 2014][research_high_temperature_materials_2014_c]
- [High-Temperature Materials Chemistry and 2014][research_high_temperature_materials_2014_b]
- [High-Temperature Materials Processing 2014][research_high_temperature_materials_2014]
- [Highlights from a Mach 4 experimental demonstration of inlet mode transition for turbine-based combined cycle hypersonic propulsion][research_inlet_mode_transition]
- [Hildebrand 1979][research_hildebrand_1979]
- [Hill et al 2004][research_hill_brown_2004]
- [Hillaker 1983][research_hillaker_1983]
- [Hillier and Netterfield 1990][research_hillier_netterfield_1990]
- [Hinderks et al 2004][research_hinderks_gulhan_2004]
- [Hiraiwa et al 1995][research_hiraiwa_tomioka_1995]
- [Hirsch et al 2023][research_hirsch_grossir_2023]
- [Hirschel and Meier 2004][research_hirschel_meier_2004]
- [Hirschel and Weiland 2009][research_hirschel_weiland_2009]
- [Hirschel and Weiland 2009][research_hirschel_weiland_2009_b]
- [Hirschel et al 2025][research_hirschel_staudacher_2025]
- [Hirschel et al 2025][research_hirschel_staudacher_2025_b]
- [Hitch and Lynch 2009][research_hitch_lynch_2009]
- [Ho 2006][research_ho_2006]
- [Hoadley 1988][research_hoadley_1988]
- [Hoang et al 2024][research_hoang_nguyen_2024]
- [Hoch and Momin 1968][research_hoch_momin_1968]
- [Hoch and Vernardakis 1975][research_hoch_vernardakis_1975]
- [Hodge 1976][research_hodge_1976]
- [Hoeger et al 2010][research_hoeger_king_2010]
- [Hoeger et al 2011][research_hoeger_king_2011]
- [Hoegl and Duesterhaus 1988][research_hoegl_duesterhaus_1988]
- [Hoffert 1968][research_hoffert_1968]
- [Hoffmann 2000][research_hoffmann_2000]
- [Hohn and Guelhan 2012][research_hohn_guelhan_2012]
- [Hohn and Guelhan 2015][research_hohn_guelhan_2015]
- [Hohn and Gülhan 2011][research_hohn_gulhan_2011]
- [Hohn and Gülhan 2017][research_hohn_gulhan_2017]
- [Hohn and Gülhan 2022][research_hohn_gulhan_2022]
- [Hojnacki 1972][research_hojnacki_1972]
- [Holberg and Grabowsky 1981][research_holberg_grabowsky_1981]
- [Holden 1970][research_holden_1970]
- [Holden 1972][research_holden_1972]
- [Holden 1977][research_holden_1977]
- [Holden 1993][research_holden_1993]
- [Holden 2000][research_holden_2000]
- [Holden 2011][research_holden_2011]
- [Holden et al 2001][research_holden_wadhams_2001]
- [Holden et al 2008][research_holden_smolinski_2008]
- [Holden et al 2010][research_holden_wadhams_2010]
- [Holdo̸ and de With 2004][research_holdo_dewith_2004]
- [Holifield and Tufts 2024][research_holifield_tufts_2024]
- [Holifield and Tufts 2024][research_holifield_tufts_2024_b]
- [Holland and Perkins 1991][research_holland_perkins_1991]
- [Holland and Perkins 1992][research_holland_perkins_1992]
- [Holland, Scott D. 1994][research_hollandscottd_1994]
- [Holland, Scott Douglas 1991][research_hollandscottdouglas_1991]
- [Hollanders et al 1992][research_hollanders_laval_1992]
- [Holm-Hansen et al 2010][research_holmhansen_lee_2010]
- [Holography of JP-4 Droplets 1974][research_holography_of_1974]
- [Hommel 1989][research_hommel_1989]
- [Hong and Kim 2011][research_hong_kim_2011]
- [Hong et al 2005][research_hong_lee_2005]
- [Hong et al 2014][research_hong_xiong_2014]
- [Hong Qian. Lu et al 2011][research_hongqianlu_dongmingge_2011]
- [Hongbo and Yongyuan 2016][research_hongbo_yongyuan_2016]
- [Hooper][research_hooper]
- [Hopkins][research_hopkins]
- [Horisawa 2004][research_horisawa_2004]
- [Horisawa et al 2004][research_horisawa_tsuchiya_2004]
- [Hornbeck 1975][research_hornbeck_1975]
- [Hornung 1991][research_hornung_1991]
- [Hornung 2001][research_hornung_2001]
- [Hornung et al 2003][research_hornung_ponchaut_2003]
- [Horstman 1987][research_horstman_1987]
- [Horstman 1991][research_horstman_1991]
- [Hossain 2025][research_hossain_2025]
- [Hossain Joy et al 2017][research_hossainjoy_rahman_2017]
- [Hostetler 2005][research_hostetler_2005]
- [Hoter et al 2026][research_hoter_nastac_2026]
- [Hou et al 2015][research_hou_wang_2015]
- [Hou et al 2020][research_hou_chang_2020]
- [Hou et al 2023][research_hou_liu_2023]
- [Hou et al 2024][research_hou_he_2024]
- [Hoult et al 2003][research_hoult_starkey_2003]
- [Houria et al 2026][research_houria_albustanji_2026]
- [Howe et al 2022][research_howe_howe_2022]
- [Howell 1988][research_howell_1988]
- [Howland 1953][research_howland_1953]
- [Hoying, D. et al 1990][research_hoyingd_kelblec_1990]
- [Hromas and Lees 1962][research_hromas_lees_1962]
- [Hsia et al 1989][research_hsia_gross_1989]
- [Hsieh et al 1997][research_hsieh_yang_1997]
- [Hsu et al 2007][research_hsu_carter_2007]
- [Hsu et al 2010][research_hsu_carter_2010]
- [Hu and Liu 2013][research_hu_liu_2013]
- [Hu and Zhu 2017][research_hu_zhu_2017]
- [Hu et al 2008][research_hu_bodson_2008]
- [Hu et al 2010][research_hu_sun_2010]
- [Hu et al 2013][research_hu_chang_2013]
- [Hu et al 2013][research_hu_xia_2013]
- [Hu et al 2014][research_hu_bao_2014]
- [Hu et al 2014][research_hu_chang_2014]
- [Hu et al 2015][research_hu_chang_2015]
- [Hu et al 2018][research_hu_jiang_2018]
- [Hu et al 2018][research_hu_li_2018]
- [Hu et al 2018][research_hu_wei_2018]
- [Hu et al 2021][research_hu_chen_2021]
- [Hu et al 2022][research_hu_dong_2022]
- [Hu et al 2022][research_hu_guo_2022]
- [Hu et al 2022][research_hu_wang_2022]
- [Hu et al 2022][research_hu_yang_2022]
- [Hu et al 2025][research_hu_liu_2025]
- [Hu et al 2026][research_hu_li_2026]
- [Huang and Chen 2021][research_huang_chen_2021]
- [Huang and Kieffer 2005][research_huang_kieffer_2005]
- [Huang and Murray 2003][research_huang_murray_2003]
- [Huang and Spadaccini 2001][research_huang_spadaccini_2001]
- [Huang and Spadaccini 2004][research_huang_spadaccini_2004]
- [Huang and Xing 2005][research_huang_xing_2005]
- [Huang and Yan 2016][research_huang_yan_2016]
- [Huang et al 2002][research_huang_spadaccini_2002]
- [Huang et al 2002][research_huang_spadaccini_2002_b]
- [Huang et al 2004][research_huang_spadaccini_2004_b]
- [Huang et al 2010][research_huang_pourkashanian_2010]
- [Huang et al 2011][research_huang_wang_2011]
- [Huang et al 2011][research_huang_zhou_2011]
- [Huang et al 2012][research_huang_tang_2012]
- [Huang et al 2017][research_huang_lianjie_2017]
- [Huang et al 2017][research_huang_zhang_2017]
- [Huang et al 2018][research_huang_yang_2018]
- [Huang et al 2018][research_huang_zhang_2018]
- [Huang et al 2018][research_huang_zuo_2018]
- [Huang et al 2020][research_huang_yue_2020]
- [Huang et al 2021][research_huang_zhang_2021]
- [Huang et al 2022][research_huang_liu_2022]
- [Huang et al 2024][research_huang_yao_2024]
- [Huang et al 2025][research_huang_feng_2025]
- [Huang et al 2025][research_huang_li_2025]
- [Huang et al 2025][research_huang_li_2025_b]
- [Huang et al 2025][research_huang_lv_2025]
- [Huang et al 2025][research_huang_wang_2025]
- [Huang et al 2025][research_huang_wang_2025_b]
- [Huang et al 2026][research_huang_wang_2026]
- [Huang et al 2026][research_huang_zhang_2026]
- [Hube 1968][research_hube_1968]
- [Huber 1966][research_huber_1966]
- [Hucknall 1985][research_hucknall_1985]
- [Hucknall 1985][research_hucknall_1985_b]
- [Huebner and Tatum 1991][research_huebner_tatum_1991]
- [Huebner et al 2003][research_huebner_witte_2003]
- [Hueter 1999][research_hueter_1999]
- [Huffman and Davidson 1958][research_huffman_davidson_1958]
- [Hughes 2000][research_hughes_2000]
- [Hughes and Pizzo 2003][research_hughes_pizzo_2003]
- [Hughes and Wu 2010][research_hughes_wu_2010]
- [Hughes and Wu 2012][research_hughes_wu_2012]
- [Hugo and Lago 2022][research_hugo_lago_2022]
- [Hui and Hu 2006][research_hui_hu_2006]
- [Hui-Sheng and Bei-Jing 2021][research_huisheng_beijing_2021]
- [Huilong et al 2015][research_huilong_qiang_2015]
- [Human 2002][research_human_2002]
- [Hummell and Beck 1966][research_hummell_beck_1966]
- [Humphrey and Culick 1987][research_humphrey_culick_1987]
- [Hung 1982][research_hung_1982]
- [Hung and Buning 1984][research_hung_buning_1984]
- [Hung and Maccormack 1978][research_hung_maccormack_1978]
- [Hunt][research_hunt]
- [Hunt 1989][research_hunt_1989]
- [Hunt and Eiswirth 1996][research_hunt_eiswirth_1996]
- [Hunt and Hunt 2020][research_hunt_hunt_2020]
- [Hunt and Hunt 2021][research_hunt_hunt_2021]
- [Hunt and Nixon 1995][research_hunt_nixon_1995]
- [Hunt and Rausch 1998][research_hunt_rausch_1998]
- [Hunt et al 1978][research_hunt_lawing_1978]
- [Hunt et al 1979][research_hunt_lawing_1979]
- [Hunt et al 1997][research_hunt_lockwood_1997]
- [Hunt et al 2019][research_hunt_ground_2019]
- [Hunt, J. L. et al 1978][research_huntjl_lawingpl_1978]
- [Hunter 1981][research_hunter_1981]
- [Huo et al 2006][research_huo_mirmirani_2006]
- [Hutcheson 1976][research_hutcheson_1976]
- [Hutchins et al 2012][research_hutchins_akella_2012]
- [Hutchins et al 2014][research_hutchins_akella_2014]
- [Hutt 1987][research_hutt_1987]
- [Hutt and East 1983][research_hutt_east_1983]
- [Hutt, John J. et al 2001][research_huttjohnj_mcarthurcraig_2001]
- [Hutzel et al 2011][research_hutzel_decker_2011]
- [Hutzel et al 2011][research_hutzel_decker_2011_b]
- [Hwang 2024][research_hwang_2024]
- [Hwang and Yeo 2023][research_hwang_yeo_2023]
- [Hyers 2009][research_hyers_2009]
- [Hyper-X flight engine ground testing for X-43 flight risk reduction][research_hyperx_ground_test]
- [Hypersonic Aerodynamics 1988][research_hypersonic_aerodynamics_1988]
- [Hypersonic Aerodynamics 2016][research_hypersonic_aerodynamics_2016]
- [Hypersonic Aerodynamics on the 2019][research_hypersonic_aerodynamics_2019]
- [Hypersonic Aerodynamics Slender Bodies 2025][research_hypersonic_aerodynamics_2025]
- [Hypersonic Air-Breathing Flight Testing 2022][research_hypersonic_air_breathing_2022]
- [Hypersonic and Supersonic Flight 2023][research_hypersonic_and_2023]
- [Hypersonic Flight 2025][research_hypersonic_flight_2025]
- [Hypersonic flow in a 1989][research_hypersonic_flow_1989]
- [Hypersonic Flow Past Thin 2009][research_hypersonic_flow_2009]
- [Hypersonic Flows 2021][research_hypersonic_flows_2021]
- [Hypersonic Flows 2025][research_hypersonic_flows_2025]
- [Hypersonic Ground Test Requirements 2002][research_hypersonic_ground_2002]
- [Hypersonic Inviscid Flowfields Approximate 2006][research_hypersonic_inviscid_2006]
- [Hypersonic Inviscid Flowfields Approximate 2019][research_hypersonic_inviscid_2019]
- [Hypersonic Inviscid Flowfields Exact 2006][research_hypersonic_inviscid_2006_b]
- [Hypersonic Inviscid Flowfields Exact 2019][research_hypersonic_inviscid_2019_b]
- [Hypersonic Materials for Thermal 2023][research_hypersonic_materials_2023]
- [Hypersonic Nonequilibrium Flows Fundamentals 2015][research_hypersonic_nonequilibrium_2015]
- [Hypersonic plane makes brief 2011][research_hypersonic_plane_2011]
- [Hypersonic Shock and Expansion-Wave 2006][research_hypersonic_shock_2006]
- [Hypersonic Shock and Expansion-Wave 2019][research_hypersonic_shock_2019]
- [Hypersonic Thin Viscous Shock 2018][research_hypersonic_thin_2018]
- [Hypersonic Viscous Interactions 2006][research_hypersonic_viscous_2006]
- [Hypersonic Viscous Interactions 2019][research_hypersonic_viscous_2019]
- [Hypersonic Wind Tunnel 1949][research_hypersonic_wind_1949]
- [Hyunwoo et al 2023][research_hyunwoo_kang_2023]
- [Hïgh-altitude atmospheric density 1960][research_high_altitude_atmospheric_1960_b]
- [Iannelli 2007][research_iannelli_2007]
- [Iannelli 2007][research_iannelli_2007_b]
- [Iannelli 2008][research_iannelli_2008]
- [Ibrahim 1967][research_ibrahim_1967]
- [ICAO Standard Atmosphere 2021][research_icao_standard_2021]
- [Ide et al 1989][research_ide_armstrong_1989]
- [Idris et al 2014][research_idris_saad_2014]
- [Idris et al 2015][research_idris_saad_2015]
- [Ifflnder and Keller][research_ifflnder_keller]
- [Igari 2019][research_igari_2019]
- [Ignatowicz and Dąbrowski 2025][research_ignatowicz_dabrowski_2025]
- [Igra 2026][research_igra_2026]
- [Iida and Komai 1992][research_iida_komai_1992]
- [Ikawa 1989][research_ikawa_1989]
- [Ikawa 1991][research_ikawa_1991]
- [Ikenson 2025][research_ikenson_2025]
- [Ilie and Sullivan 2021][research_ilie_sullivan_2021]
- [Ilie et al 2023][research_ilie_chan_2023]
- [Ilie et al 2023][research_ilie_mcafee_2023]
- [Iliff and Shafer 1992][research_iliff_shafer_1992]
- [Iliff, Kenneth W. and Shafer, Mary F. 1993][research_iliffkennethw_shafermaryf_1993]
- [Iliff, Kenneth W. and Shafer, Mary F. 1993][research_iliffkennethw_shafermaryf_1993_b]
- [Iliff, Kenneth W. and Shafer, Mary F. 1995][research_iliffkennethw_shafermaryf_1995]
- [Ilin et al 1999][research_ilin_diaz_1999]
- [Im and Do 2018][research_im_do_2018]
- [Imado and Kuroda 1992][research_imado_kuroda_1992]
- [Impact of Copper Contamination][research_impact_of]
- [Imrak et al 2021][research_imrak_karaselvi_2021]
- [Inamura et al 1996][research_inamura_sei_1996]
- [Ince 1967][research_ince_1967]
- [Incorporating agility flight test 1994][research_incorporating_agility_1994]
- [Influence of Plasma on 2024][research_influence_of_2024]
- [Influence of the rising 2023][research_influence_of_2023]
- [Ingenito 2015][research_ingenito_2015]
- [Ingenito 2021][research_ingenito_2021]
- [Ingenito 2021][research_ingenito_2021_b]
- [Ingenito 2021][research_ingenito_2021_c]
- [Ingenito 2021][research_ingenito_2021_d]
- [Ingenito 2021][research_ingenito_2021_e]
- [Ingenito 2021][research_ingenito_2021_f]
- [Ingenito et al 2009][research_ingenito_bruno_2009]
- [Ingenito et al 2009][research_ingenito_bruno_2009_b]
- [Inger 1984][research_inger_1984]
- [Inger 1986][research_inger_1986]
- [Inger 1989][research_inger_1989]
- [Inger 1991][research_inger_1991]
- [Inger 1994][research_inger_1994]
- [Inger 1995][research_inger_1995]
- [Inger 1995][research_inger_1995_b]
- [Inger 1995][research_inger_1995_c]
- [Inger 1995][research_inger_1995_d]
- [Inger 2008][research_inger_2008]
- [Inger 2011][research_inger_2011]
- [Inger and Rangwalla 1988][research_inger_rangwalla_1988]
- [Inger et al 2001][research_inger_higgins_2001]
- [Initial Results from a 1962][research_initial_results_1962]
- [Initial Shuttle External Tank 1983][research_initial_shuttle_1983]
- [Inokuma et al 2025][research_inokuma_yakeno_2025]
- [Instrumentation for Airbreathing Propulsion 1974][research_instrumentation_for_1974]
- [Instrumentation for In-Flight Determination 1974][research_instrumentation_for_1974_b]
- [Integrated transient thermal-structural finite 1981][research_integrated_transient_1981]
- [International Standard Atmosphere 2010][research_international_standard_2010]
- [Interpretation of waverider performance data using computational fluid dynamics][research_waverider_cfd_interpretation]
- [Intranasal flow field, in 2015][research_intranasal_flow_2015]
- [Introduction Special Section on 2014][research_introduction_special_2014]
- [Introduction to Hypersonic Air-Breathing 2022][research_introduction_to_2022]
- [Investigation of bubble-point vapor 2005][research_investigation_of_2005]
- [Investigation of mixing characteristics 2023][research_investigation_of_2023]
- [Investigation of the Use 1974][research_investigation_of_1974]
- [Isaac and Miles 1990][research_isaac_miles_1990]
- [Isakina et al 2000][research_isakina_prokhvatilov_2000]
- [Isbell][research_isbell]
- [Ishimoto et al 1996][research_ishimoto_takizawa_1996]
- [Ispir and Saracoglu 2019][research_ispir_saracoglu_2019]
- [Ispir et al 2023][research_ispir_zdybal_2023]
- [Itabashi et al 1995][research_itabashi_honma_1995]
- [Itoh 2007][research_itoh_2007]
- [Itoh et al 2002][research_itoh_ueda_2002]
- [Iwashita 2015][research_iwashita_2015]
- [Iwashita 2026][research_iwashita_2026]
- [Izard et al 2009][research_izard_lehnasch_2009]
- [Jackson and Anderson 1967][research_jackson_anderson_1967]
- [Jackson and Coyle 1983][research_jackson_coyle_1983]
- [Jackson et al 1995][research_jackson_corporan_1995]
- [Jackson et al 2015][research_jackson_gruber_2015]
- [Jacocks and Kneile 1975][research_jacocks_kneile_1975]
- [Jade et al 2025][research_jade_jimmyjohnoe_2025]
- [Jaeger and Hemati 2025][research_jaeger_hemati_2025]
- [Jagadeesh et al 1998][research_jagadeesh_reddy_1998]
- [James 2022][research_james_2022]
- [Jamie 2015][research_jamie_2015]
- [Jammalamadaka et al 2014][research_jammalamadaka_li_2014]
- [Janardanan and Jayakumar 2006][research_janardanan_jayakumar_2006]
- [Janarthanam and Babu 2012][research_janarthanam_babu_2012]
- [Jann and Yakimenko 2015][research_jann_yakimenko_2015]
- [Jardine 1930][research_jardine_1930]
- [Jasa et al 2018][research_jasa_mader_2018]
- [Jaskowiak, Martha H. 2004][research_jaskowiakmarthah_2004]
- [Jategaonkar et al 2005][research_jategaonkar_behr_2005]
- [Javadi and Aidun 2024][research_javadi_aidun_2024]
- [Javaid and Serghides 2003][research_javaid_serghides_2003]
- [Javaid and Serghides 2004][research_javaid_serghides_2004]
- [Javaid and Serghides 2005][research_javaid_serghides_2005]
- [Jay D Feldman][research_jaydfeldman]
- [Jayachandran and Menon 1996][research_jayachandran_menon_1996]
- [Jayanthi and Jain 2019][research_jayanthi_jain_2019]
- [Jazra and Smart 2011][research_jazra_smart_2011]
- [Jazra et al 2013][research_jazra_preller_2013]
- [Jee][research_jee]
- [Jeffrie and Rolston 1972][research_jeffrie_rolston_1972]
- [Jensen and Braendlein 1996][research_jensen_braendlein_1996]
- [Jeon and Park 2023][research_jeon_park_2023]
- [Jeong et al 2008][research_jeong_obyrne_2008]
- [Jeong et al 2008][research_jeong_obyrne_2008_b]
- [Jeong et al 2020][research_jeong_obyrne_2020]
- [Jessica Lux-Baumann and Darryl A Burkes 2005][research_jessicaluxbaumann_darrylaburkes_2005]
- [Jeyakumar et al 2005][research_jeyakumar_biswas_2005]
- [Ji 2017][research_ji_2017]
- [Ji and Zhou 2017][research_ji_zhou_2017]
- [Ji and Zhou 2018][research_ji_zhou_2018]
- [Ji et al 2019][research_ji_zhou_2019]
- [Ji et al 2023][research_ji_zhao_2023]
- [Ji et al 2024][research_ji_he_2024]
- [Ji et al 2025][research_ji_cai_2025]
- [Jia et al 2004][research_jia_wenxiu_2004]
- [Jian and Yude 2024][research_jian_yude_2024]
- [Jian-bo et al 2017][research_jianbo_xinghua_2017]
- [Jianchen et al 2014][research_jianchen_yuzhen_2014]
- [Jiang et al 2010][research_jiang_zhang_2010]
- [Jiang et al 2017][research_jiang_song_2017]
- [Jiang et al 2018][research_jiang_chen_2018]
- [Jiang et al 2020][research_jiang_zhou_2020]
- [Jiang et al 2021][research_jiang_liu_2021]
- [Jiang et al 2022][research_jiang_nan_2022]
- [Jiang et al 2023][research_jiang_wang_2023]
- [Jiang et al 2024][research_jiang_liu_2024]
- [Jiang et al 2025][research_jiang_zhan_2025]
- [Jianguo et al 2018][research_jianguo_yifei_2018]
- [Jianqiang et al 2016][research_jianqiang_jinlong_2016]
- [Jiao et al 2015][research_jiao_chang_2015]
- [Jiao et al 2016][research_jiao_chang_2016]
- [Jiao et al 2017][research_jiao_chang_2017]
- [Jiao et al 2018][research_jiao_chang_2018]
- [Jiao et al 2021][research_jiao_song_2021]
- [Jie Wang et al 2012][research_jiewang_qunzong_2012]
- [Jin and Yao 2023][research_jin_yao_2023]
- [Jin et al 2016][research_jin_huang_2016]
- [Jin et al 2022][research_jin_sun_2022]
- [Jin et al 2022][research_jin_xu_2022]
- [Jin et al 2023][research_jin_choi_2023]
- [Jin et al 2023][research_jin_tan_2023]
- [Jin et al 2023][research_jin_zhang_2023]
- [Jin et al 2024][research_jin_choi_2024]
- [Jin et al 2026][research_jin_zhang_2026]
- [Jinchuan Hu et al 2015][research_jinchuanhu_jinglinli_2015]
- [Jing and Shuo 2008][research_jing_shuo_2008]
- [Jing and Yuan-pei 2015][research_jing_yuanpei_2015]
- [Jing et al 2007][research_jing_shuo_2007]
- [Jing et al 2023][research_jing_zhang_2023]
- [Jing et al 2025][research_jing_zhang_2025]
- [Jing et al 2026][research_jing_song_2026]
- [Jing-guang and Shen-min 2017][research_jingguang_shenmin_2017]
- [Jingang et al 2026][research_jingang_haotian_2026]
- [Jingqi and Yulong 2024][research_jingqi_yulong_2024]
- [Jischke 1978][research_jischke_1978]
- [Jo 2026][research_jo_2026]
- [Jo et al 2024][research_jo_sung_2024]
- [Jo et al 2025][research_jo_sung_2025]
- [Jo et al 2026][research_jo_sung_2026]
- [John Michael Thornton et al][research_johnmichaelthornton_jeremiebernarderwinmeurisse]
- [Johnson 1967][research_johnson_1967]
- [Johnson and Narayanaswamy 2024][research_johnson_narayanaswamy_2024]
- [Johnson and Narayanaswamy 2026][research_johnson_narayanaswamy_2026]
- [Johnson and Sorenson 2006][research_johnson_sorenson_2006]
- [Johnson et al 1970][research_johnson_josepha_1970]
- [Johnson et al 1981][research_johnson_portalatin_1981]
- [Johnson et al 2001][research_johnson_bogar_2001]
- [Johnson et al 2015][research_johnson_niedbalski_2015]
- [Johnson et al 2017][research_johnson_niedbalski_2017]
- [Johnson et al 2022][research_johnson_jenquin_2022]
- [Johnson III and Wu 1974][research_johnsoniii_wu_1974]
- [Johnson, Sylvia and Conley, Joe 2015][research_johnsonsylvia_conleyjoe_2015]
- [Johnston 1969][research_johnston_1969]
- [Johnston and Candler 2023][research_johnston_candler_2023]
- [Johnston and Powars 1969][research_johnston_powars_1969]
- [Johnston et al 1970][research_johnston_monita_1970]
- [Johnston et al 1971][research_johnston_cubbage_1971]
- [Jones and Laurence 2025][research_jones_laurence_2025]
- [Jones et al 2021][research_jones_saxer_2021]
- [Jones, R. A. and Huber, P. W. 1978][research_jonesra_huberpw_1978]
- [Jordan 1974][research_jordan_1974]
- [Jordan and Ragab 1996][research_jordan_ragab_1996]
- [Josyula and Bailey 2003][research_josyula_bailey_2003]
- [Josyula and Shang 1990][research_josyula_shang_1990]
- [Josyula and Shang 1992][research_josyula_shang_1992]
- [Josyula and Vedula 2015][research_josyula_vedula_2015]
- [Juluru Sandeep and AVSS Kumara Swami Gupta 2023][research_julurusandeep_avsskumaraswamigupta_2023]
- [K et al 2020][research_k_danish_2020]
- [Kadosh and Natan 2020][research_kadosh_natan_2020]
- [Kai and Ohtake 1996][research_kai_ohtake_1996]
- [Kai-li and Kun-yuan 2010][research_kaili_kunyuan_2010]
- [Kai-li and Kun-yuan 2011][research_kaili_kunyuan_2011]
- [Kailasanath et al 1986][research_kailasanath_gardner_1986]
- [Kaiser and Fluegge-Lotz 1968][research_kaiser_flueggelotz_1968]
- [Kakatsios and Houzouris 1995][research_kakatsios_houzouris_1995]
- [Kakatsios and Houzouris 1998][research_kakatsios_houzouris_1998]
- [Kalkhoran and Otugen 1994][research_kalkhoran_otugen_1994]
- [Kalra et al 2018][research_kalra_shewale_2018]
- [Kalra et al 2018][research_kalra_shewale_2018_b]
- [Kaltreider 1951][research_kaltreider_1951]
- [Kalyan et al 2022][research_kalyan_konda_2022]
- [Kamari et al 2020][research_kamari_tadjfar_2020]
- [Kamath et al 1991][research_kamath_mao_1991]
- [Kambrath and Thuluvath 2025][research_kambrath_thuluvath_2025]
- [Kamezawa and Ruffin 2018][research_kamezawa_ruffin_2018]
- [Kanapathipillai and Yu 2024][research_kanapathipillai_yu_2024]
- [Kanapathipillai et al 2020][research_kanapathipillai_chang_2020]
- [Kanapathipillai et al 2020][research_kanapathipillai_chang_2020_b]
- [Kanda 1998][research_kanda_1998]
- [Kanda 1998][research_kanda_1998_b]
- [Kanda 2000][research_kanda_2000]
- [Kanda et al 1993][research_kanda_masuya_1993]
- [Kanda et al 1994][research_kanda_masuya_1994]
- [Kanda et al 2001][research_kanda_chinzei_2001]
- [Kanda et al 2003][research_kanda_hiraiwa_2003]
- [Kanda et al 2003][research_kanda_kato_2003]
- [Kanda et al 2007][research_kanda_kato_2007]
- [Kanderpalli et al 2014][research_kanderpalli_selvaraj_2014]
- [Kandula and Kummitha 2025][research_kandula_kummitha_2025]
- [Kaneko and Nakamura 1999][research_kaneko_nakamura_1999]
- [Kaneko et al 2000][research_kaneko_menshov_2000]
- [Kang and Dunn 1972][research_kang_dunn_1972]
- [Kang and Sun 2011][research_kang_sun_2011]
- [Kang and Won Kim 2019][research_kang_wonkim_2019]
- [Kang et al 2008][research_kang_tang_2008]
- [Kang et al 2023][research_kang_meng_2023]
- [Kang et al 2023][research_kang_zhao_2023]
- [Kang et al 2025][research_kang_sung_2025]
- [Kannaiyan 2020][research_kannaiyan_2020]
- [Kantrowitz 2002][research_kantrowitz_2002]
- [Kantrowitz and Petschek 1964][research_kantrowitz_petschek_1964]
- [Kantrowitz, Arthur on 1984 2025][research_kantrowitz_arthur_2025]
- [Kantrowitz, Arthur on 2006 2025][research_kantrowitz_arthur_2025_b]
- [Kao and Anderson 1981][research_kao_anderson_1981]
- [Karanian and Kepler 1965][research_karanian_kepler_1965]
- [karciauskas and Peters 2024][research_karciauskas_peters_2024]
- [Karimi and Oboodi 2018][research_karimi_oboodi_2018]
- [Kascak 1971][research_kascak_1971]
- [Kato and Im 2019][research_kato_im_2019]
- [Kato et al 2006][research_kato_kanda_2006]
- [Kauffman et al 1990][research_kauffman_grandhi_1990]
- [Kauffman et al 1991][research_kauffman_grandhi_1991]
- [Kaufman 1963][research_kaufman_1963]
- [Kaushik 2018][research_kaushik_2018]
- [Kaushik 2018][research_kaushik_2018_b]
- [Kaushik 2023][research_kaushik_2023]
- [Kay et al 1990][research_kay_peschke_1990]
- [Kay, I. W. et al 1992][research_kayiw_peschkewt_1992]
- [Kay, Ira W. 1989][research_kayiraw_1989]
- [Kazmar 2005][research_kazmar_2005]
- [Keanini et al 1989][research_keanini_yu_1989]
- [Kellenberger and Ciccarelli 2015][research_kellenberger_ciccarelli_2015]
- [Kellermann et al 2020][research_kellermann_habermann_2020]
- [Kelly 1972][research_kelly_1972]
- [Kelly 1972][research_kelly_1972_b]
- [Kelly 1973][research_kelly_1973]
- [Kelly 1988][research_kelly_1988]
- [Kelso 1993][research_kelso_1993]
- [Kendall 1974][research_kendall_1974]
- [Kennedy 1986][research_kennedy_1986]
- [Kennell et al 2015][research_kennell_neely_2015]
- [Kenworthy 1967][research_kenworthy_1967]
- [Kepler and Champagne 1989][research_kepler_champagne_1989]
- [Kerans 2002][research_kerans_2002]
- [Kerstan et al 2014][research_kerstan_muller_2014]
- [Keshmiri 2008][research_keshmiri_2008]
- [Keshmiri et al 2005][research_keshmiri_colgren_2005]
- [Keshmiri et al 2006][research_keshmiri_colgren_2006]
- [Keshmiri et al 2006][research_keshmiri_colgren_2006_b]
- [Keshmiri et al 2006][research_keshmiri_colgren_2006_c]
- [Keshmiri et al 2007][research_keshmiri_colgren_2007]
- [Keshmiri et al 2007][research_keshmiri_farokhi_2007]
- [Kessler et al 2015][research_kessler_li_2015]
- [Khairul Habib Pulok and Chakravarty 2021][research_khairulhabibpulok_chakravarty_2021]
- [Khambaswadkar 2024][research_khambaswadkar_2024]
- [Khan et al 2018][research_khan_tahmid_2018]
- [Khmyrov et al 2025][research_khmyrov_grigoriev_2025]
- [Khobragade and Kumar 2022][research_khobragade_kumar_2022]
- [Khorrami and Chang 1997][research_khorrami_chang_1997]
- [Khorunzhenko et al 2002][research_khorunzhenko_roupassov_2002]
- [Khrapko 2018][research_khrapko_2018]
- [Khurana and Suzuki 2013][research_khurana_suzuki_2013]
- [Kidd and Adams, Jr. 2000][research_kidd_adamsjr_2000]
- [Kim 2000][research_kim_2000]
- [Kim 2003][research_kim_2003]
- [Kim 2017][research_kim_2017]
- [Kim and Lee 2022][research_kim_lee_2022]
- [Kim and Menon 1999][research_kim_menon_1999]
- [Kim and Park 2026][research_kim_park_2026]
- [Kim et al 1982][research_kim_rasmussen_1982]
- [Kim et al 2004][research_kim_baek_2004]
- [Kim et al 2010][research_kim_jeon_2010]
- [Kim et al 2020][research_kim_han_2020]
- [Kim et al 2023][research_kim_kim_2023]
- [Kim et al 2025][research_kim_seo_2025]
- [Kim et al 2025][research_kim_seo_2025_b]
- [Kimmel 1993][research_kimmel_1993]
- [Kimmel and Poggie 1997][research_kimmel_poggie_1997]
- [Kimmel et al 2005][research_kimmel_hayes_2005]
- [Kimmel et al 2011][research_kimmel_adamczak_2011]
- [Kimmel, Roger L. and Prabhu, Dinesh 2015][research_kimmelrogerl_prabhudinesh_2015]
- [Kimmerly][research_kimmerly]
- [King 1962][research_king_1962]
- [Kinslow and Busby 1973][research_kinslow_busby_1973]
- [Kireeti et al 2022][research_kireeti_ravikiransastry_2022]
- [Kirkby 1964][research_kirkby_1964]
- [Kirkpatrick][research_kirkpatrick]
- [Kishida 2006][research_kishida_2006]
- [Kishore and Sunitha 1977][research_kishore_sunitha_1977]
- [Kitamura and Shima 2011][research_kitamura_shima_2011]
- [Kitamura et al 2007][research_kitamura_roe_2007]
- [Kitowski 1992][research_kitowski_1992]
- [Kittredge et al 1961][research_kittredge_streets_1961]
- [Kiyohashi 1998][research_kiyohashi_1998]
- [Kkn and Reddy 2016][research_kkn_reddy_2016]
- [Klepper et al 2017][research_klepper_sirbaugh_2017]
- [Kline et al 2014][research_kline_palacios_2014]
- [Kline et al 2014][research_kline_palacios_2014_b]
- [Klineberg, John M. 1989][research_klinebergjohnm_1989]
- [Klingenberg et al 2026][research_klingenberg_willems_2026]
- [Klock and Cesnik 2015][research_klock_cesnik_2015]
- [Klock and Cesnik 2016][research_klock_cesnik_2016]
- [Klothakis and Nikolos 2024][research_klothakis_nikolos_2024]
- [Klotz 1963][research_klotz_1963]
- [Kluwick and Stross 1984][research_kluwick_stross_1984]
- [Knauss et al 1999][research_knauss_riedel_1999]
- [Knight 2002][research_knight_2002]
- [Knight 2015][research_knight_2015]
- [Knight and Kianvashrad 2023][research_knight_kianvashrad_2023]
- [Knight and Naiman 2009][research_knight_naiman_2009]
- [Knight and Yan 2000][research_knight_yan_2000]
- [Knight and Zheltovodov 2011][research_knight_zheltovodov_2011]
- [Knight et al 2026][research_knight_kildare_2026]
- [Knighton 1992][research_knighton_1992]
- [Knittel and Lewis 2012][research_knittel_lewis_2012]
- [Knott 1974][research_knott_1974]
- [Knott 1984][research_knott_1984]
- [Ko and Jackson 1992][research_ko_jackson_1992]
- [Kobayashi and Adachi 2015][research_kobayashi_adachi_2015]
- [Kobayashi and Adachi 2017][research_kobayashi_adachi_2017]
- [Kobayashi et al 2001][research_kobayashi_sato_2001]
- [Kobayashi et al 2003][research_kobayashi_tomioka_2003]
- [Kobayashi et al 2007][research_kobayashi_kanda_2007]
- [Kobayashi et al 2008][research_kobayashi_sawai_2008]
- [Kobayashi et al 2018][research_kobayashi_hemmi_2018]
- [Kodama and Kogiso 2017][research_kodama_kogiso_2017]
- [Kodera et al 2005][research_kodera_sunami_2005]
- [Kodera et al 2007][research_kodera_yang_2007]
- [Kodikara 2020][research_kodikara_2020]
- [Kohl 1993][research_kohl_1993]
- [Kojima et al 2012][research_kojima_taguchi_2012]
- [Kojima et al 2015][research_kojima_taguchi_2015]
- [Kokan et al 2004][research_kokan_olds_2004]
- [Kokkinakis et al 2023][research_kokkinakis_khujadze_2023]
- [Kominek 2017][research_kominek_2017]
- [Kong et al 2020][research_kong_chang_2020]
- [Kong et al 2021][research_kong_chang_2021]
- [Kong et al 2024][research_kong_liang_2024]
- [Kong et al 2026][research_kong_chen_2026]
- [Konovalikhin et al 2018][research_konovalikhin_kovalev_2018]
- [Kontinos 1996][research_kontinos_1996]
- [Kontogiannis et al 2016][research_kontogiannis_taylor_2016]
- [Kopp and Garbers 2014][research_kopp_garbers_2014]
- [Kopp et al 1999][research_kopp_hollmeier_1999]
- [Koppenwallner 1968][research_koppenwallner_1968]
- [Korabelnikov and Kuranov 2002][research_korabelnikov_kuranov_2002]
- [Korabelnikov and Kuranov 2005][research_korabelnikov_kuranov_2005]
- [Korte 1992][research_korte_1992]
- [Korte 2000][research_korte_2000]
- [Korte and Hodge 1994][research_korte_hodge_1994]
- [Korte and Mcrae 1989][research_korte_mcrae_1989]
- [Korte et al 1991][research_korte_kumar_1991]
- [Koschel 1996][research_koschel_1996]
- [Koschel and Rick 1991][research_koschel_rick_1991]
- [Koschel et al 1998][research_koschel_link_1998]
- [Kose and Celik 2023][research_kose_celik_2023]
- [Kostoff et al 2003][research_kostoff_eberhart_2003]
- [Kostyk, Chris and Risch, Tim 2013][research_kostykchris_rischtim_2013]
- [Kostyukov 1980][research_kostyukov_1980]
- [Kotel'nikov et al 2020][research_kotelnikov_kotelnikov_2020]
- [Kothari et al 1996][research_kothari_tarpley_1996]
- [Kothari et al 2010][research_kothari_livingston_2010]
- [Kourtides et al 1988][research_kourtides_pitts_1988]
- [Kozlovskii and Stankus 2014][research_kozlovskii_stankus_2014]
- [Kozlovskii and Stankus 2015][research_kozlovskii_stankus_2015]
- [Kramer and Buhler 1980][research_kramer_buhler_1980]
- [Kramer et al 2018][research_kramer_williams_2018]
- [Krause et al 1991][research_krause_hartmann_1991]
- [Krawczyk et al 1986][research_krawczyk_rajendran_1986]
- [Kremeyer and Pakhomov 2008][research_kremeyer_pakhomov_2008]
- [Krikorian 1960][research_krikorian_1960]
- [Krothapalli et al 2003][research_krothapalli_alvi_2003]
- [Krumenacker and Pellicano 1992][research_krumenacker_pellicano_1992]
- [Kubo et al 2014][research_kubo_tomioka_2014]
- [Kubota and Berg 1977][research_kubota_berg_1977]
- [Kubota and Uchida 1999][research_kubota_uchida_1999]
- [Kudryavtsev et al 2009][research_kudryavtsev_mironov_2009]
- [Kuipers et al 2007][research_kuipers_mirmirani_2007]
- [Kuipers et al 2008][research_kuipers_ioannou_2008]
- [Kuipers et al 2009][research_kuipers_ioannou_2009]
- [Kulkarni and Phan 2003][research_kulkarni_phan_2003]
- [Kulkarni et al 2024][research_kulkarni_shrekhar_2024]
- [Kumar][research_kumar]
- [Kumar 1992][research_kumar_1992]
- [Kumar 2022][research_kumar_2022]
- [Kumar and Anderson 1986][research_kumar_anderson_1986]
- [Kumar and Ghosh 2024][research_kumar_ghosh_2024]
- [Kumar and Mahulikar 2017][research_kumar_mahulikar_2017]
- [Kumar et al 2018][research_kumar_penchalaiah_2018]
- [Kumar et al 2018][research_kumar_sarkar_2018]
- [Kumar et al 2022][research_kumar_iyer_2022]
- [Kumar et al 2023][research_kumar_pranaykumar_2023]
- [Kumar Gugulothu et al 2020][research_kumargugulothu_bhaskar_2020]
- [Kumar Sulur Loganathan 2023][research_kumarsulurloganathan_2023]
- [Kumar, Ajay et al 2001][research_kumarajay_drummondjphilip_2001]
- [Kumm and Bitondo 1953][research_kumm_bitondo_1953]
- [Kummitha 2022][research_kummitha_2022]
- [Kummitha 2022][research_kummitha_2022_b]
- [Kummitha 2024][research_kummitha_2024]
- [Kummitha and Kandula 2026][research_kummitha_kandula_2026]
- [Kummitha and Pandey 2020][research_kummitha_pandey_2020]
- [Kummitha and Pandey 2021][research_kummitha_pandey_2021]
- [Kummitha et al 2017][research_kummitha_suneetha_2017]
- [Kundu 2013][research_kundu_2013]
- [Kuntz et al 1986][research_kuntz_amatucci_1986]
- [Kuntz et al 1987][research_kuntz_amatucci_1987]
- [Kuo 1976][research_kuo_1976]
- [Kuppuswamy and Kiran 1981][research_kuppuswamy_kiran_1981]
- [Kuranov and Korabelnikov 2008][research_kuranov_korabelnikov_2008]
- [Kuranov and Korabelnikov 2008][research_kuranov_korabelnikov_2008_b]
- [Kuranov et al 2012][research_kuranov_korabelnikov_2012]
- [Kuranov et al 2016][research_kuranov_korabelnikov_2016]
- [Kuranov et al 2017][research_kuranov_korabelnikov_2017]
- [Kurilova and Li 2026][research_kurilova_li_2026]
- [Kurtz et al 2015][research_kurtz_aizengendler_2015]
- [Kurzke and Halliwell 2018][research_kurzke_halliwell_2018]
- [Kurzke et al 2025][research_kurzke_halliwell_2025]
- [Kussoy, M. I. et al 1993][research_kussoymi_horstmankc_1993]
- [Kussoy, Marvin I. and Horstman, Clifford C. 1989][research_kussoymarvini_horstmancliffordc_1989]
- [Kutschenreuter et al 1966][research_kutschenreuter_paulh_1966]
- [Kuznetsov 1992][research_kuznetsov_1992]
- [Kwak and Kiris 2003][research_kwak_kiris_2003]
- [Kwak and Lee 2011][research_kwak_lee_2011]
- [Kwak and Lee 2013][research_kwak_lee_2013]
- [Kwak and Lee 2013][research_kwak_lee_2013_b]
- [Kwak et al 2013][research_kwak_lee_2013_c]
- [Kydd 1959][research_kydd_1959]
- [Kydd and Mullaney 1961][research_kydd_mullaney_1961]
- [L. et al 2012][research_l_r_2012]
- [La Sorsa et al 2025][research_lasorsa_kotler_2025]
- [Labbé et al 1999][research_labbe_ryan_1999]
- [Lacorre et al 2022][research_lacorre_barre_2022]
- [Ladeinde 2019][research_ladeinde_2019]
- [Ladeinde 2020][research_ladeinde_2020]
- [Ladeinde 2020][research_ladeinde_2020_b]
- [Laderman 1979][research_laderman_1979]
- [Laderman and Demetriades 1977][research_laderman_demetriades_1977]
- [Ladyzhenskij 1963][research_ladyzhenskij_1963]
- [Lago et al 2012][research_lago_chpoun_2012]
- [Lahaye and Heckman 1968][research_lahaye_heckman_1968]
- [Lambert][research_lambert]
- [Lambert and Coughlin 1967][research_lambert_coughlin_1967]
- [Lamorte et al 2011][research_lamorte_friedmann_2011]
- [Lamorte et al 2015][research_lamorte_friedmann_2015]
- [Lamy 1983][research_lamy_1983]
- [Landau and Yeneriz 1965][research_landau_yeneriz_1965]
- [Lander 1968][research_lander_1968]
- [Lander and Nixon 1971][research_lander_nixon_1971]
- [Landesman and Basinski 1963][research_landesman_basinski_1963]
- [Landrum and Tournes 2002][research_landrum_tournes_2002]
- [Landsbaum et al 1979][research_landsbaum_salinas_1979]
- [Landsberg et al 2016][research_landsberg_wheatley_2016]
- [Landsberg et al 2020][research_landsberg_vanyai_2020]
- [Landsberg et al 2021][research_landsberg_curran_2021]
- [Landsberg et al 2022][research_landsberg_curran_2022]
- [Lane, Jr. and Kirlin 1978][research_lanejr_kirlin_1978]
- [Lang 1981][research_lang_1981]
- [Langhenry and Parks 1991][research_langhenry_parks_1991]
- [Langill, Jr. 1965][research_langilljr_1965]
- [Lanshin et al 1996][research_lanshin_dulepov_1996]
- [Large et al 1981][research_large_may_1981]
- [Lasseur][research_lasseur]
- [Latvala and Anderson 1959][research_latvala_anderson_1959]
- [Lau 2007][research_lau_2007]
- [Laurence et al 2015][research_laurence_lieber_2015]
- [Law 1975][research_law_1975]
- [Law 1976][research_law_1976]
- [Law 2004][research_law_2004]
- [Lawrence 1991][research_lawrence_1991]
- [Lawrence 1992][research_lawrence_1992]
- [Lazur et al 1999][research_lazur_sawyer_1999]
- [Le et al 2005][research_le_goyne_2005]
- [Le et al 2006][research_le_goyne_2006]
- [Le et al 2008][research_le_goyne_2008]
- [Le et al 2012][research_le_greenshields_2012]
- [Le et al 2023][research_le_liu_2023]
- [Lead-Cooled Fast Reactor LFR][research_lead_cooled_fast]
- [Leckie][research_leckie]
- [Lederer et al 1991][research_lederer_schwab_1991]
- [Ledu and Pollak 1968][research_ledu_pollak_1968]
- [Lee][research_lee]
- [Lee 1995][research_lee_1995]
- [Lee 2006][research_lee_2006]
- [Lee 2006][research_lee_2006_b]
- [Lee 2012][research_lee_2012]
- [Lee and Aldredge 2015][research_lee_aldredge_2015]
- [Lee and Chung 2024][research_lee_chung_2024]
- [Lee and Glass 1982][research_lee_glass_1982]
- [Lee and Gross 2021][research_lee_gross_2021]
- [Lee and Gross 2022][research_lee_gross_2022]
- [Lee and James T. 1963][research_lee_jamest_1963]
- [Lee and Jeung 2009][research_lee_jeung_2009]
- [Lee and Kang 2019][research_lee_kang_2019]
- [Lee and Mitani 2003][research_lee_mitani_2003]
- [Lee and Ombrello 2024][research_lee_ombrello_2024]
- [Lee and Rasmussen 1978][research_lee_rasmussen_1978]
- [Lee and Van Dalsem 1981][research_lee_vandalsem_1981]
- [Lee et al 2000][research_lee_kim_2000]
- [Lee et al 2001][research_lee_shin_2001]
- [Lee et al 2005][research_lee_kawamura_2005]
- [Lee et al 2007][research_lee_reiman_2007]
- [Lee et al 2013][research_lee_kang_2013]
- [Lee et al 2015][research_lee_kim_2015]
- [Lee et al 2018][research_lee_liou_2018]
- [Lee et al 2021][research_lee_lee_2021]
- [Lee et al 2022][research_lee_lee_2022]
- [Lee et al 2026][research_lee_kim_2026]
- [Lee et al 2026][research_lee_kim_2026_b]
- [Lees and Hromas 1961][research_lees_hromas_1961]
- [Lees and Kubota 1972][research_lees_kubota_1972]
- [Lees and Reeves 1964][research_lees_reeves_1964]
- [Leger and Poggie 2014][research_leger_poggie_2014]
- [Legge 1995][research_legge_1995]
- [Lehoczky 1977][research_lehoczky_1977]
- [Lehtinen and Zeller 1972][research_lehtinen_zeller_1972]
- [Lei and Zha 2022][research_lei_zha_2022]
- [Lei and Zha 2022][research_lei_zha_2022_b]
- [Lei et al 2012][research_lei_kunyuan_2012]
- [Lei et al 2023][research_lei_zhang_2023]
- [Leighton 1964][research_leighton_1964]
- [Lempert and Dorofeenko 2013][research_lempert_dorofeenko_2013]
- [Lempert and Miles 1995][research_lempert_miles_1995]
- [Lenard and Long 1964][research_lenard_long_1964]
- [Lenard et al 1962][research_lenard_long_1962]
- [Leng et al 2024][research_leng_wang_2024]
- [Leonov 2022][research_leonov_2022]
- [Leonov et al 2007][research_leonov_yarantsev_2007]
- [Leonov et al 2009][research_leonov_yarantsev_2009]
- [Leonov et al 2011][research_leonov_kochetov_2011]
- [Leonov et al 2012][research_leonov_yarantsev_2012]
- [Leonov et al 2018][research_leonov_houpt_2018]
- [Leontiev et al 2000][research_leontiev_nosatov_2000]
- [Lepsch and Naftel 1993][research_lepsch_naftel_1993]
- [Lepsch, Jr. and Naftel 1992][research_lepschjr_naftel_1992]
- [Lestrade et al 2017][research_lestrade_anthoine_2017]
- [Levermore and Brio 1994][research_levermore_brio_1994]
- [Levikhin and Musteikis 2025][research_levikhin_musteikis_2025]
- [Levin 2015][research_levin_2015]
- [Levin et al 2008][research_levin_ioannou_2008]
- [Levy 1976][research_levy_1976]
- [Levy 1982][research_levy_1982]
- [Levy et al 1977][research_levy_shamroth_1977]
- [Lewerenz 1987][research_lewerenz_1987]
- [Lewis 1991][research_lewis_1991]
- [Lewis 2001][research_lewis_2001]
- [Lewis 2003][research_lewis_2003]
- [Lewis 2003][research_lewis_2003_b]
- [Lewis 2010][research_lewis_2010]
- [Leyland 1992][research_leyland_1992]
- [Li 1974][research_li_1974]
- [Li 1977][research_li_1977]
- [Li 2007][research_li_2007]
- [Li 2008][research_li_2008]
- [Li 2019][research_li_2019]
- [Li 2021][research_li_2021]
- [Li 2022][research_li_2022]
- [Li 2022][research_li_2022_b]
- [Li and Chen 2011][research_li_chen_2011]
- [Li and Cui 2009][research_li_cui_2009]
- [Li and Fu 2010][research_li_fu_2010]
- [Li and Geiselhart 2024][research_li_geiselhart_2024]
- [Li and Han 2025][research_li_han_2025]
- [Li and Nagamatsu 1953][research_li_nagamatsu_1953]
- [Li and Shi 1993][research_li_shi_1993]
- [Li and Wang 2011][research_li_wang_2011]
- [Li and Wang 2017][research_li_wang_2017]
- [Li and Wey 1988][research_li_wey_1988]
- [Li and Zhao 2014][research_li_zhao_2014]
- [Li and Zhu 2012][research_li_zhu_2012]
- [Li et al 1999][research_li_freed_1999]
- [Li et al 2000][research_li_li_2000]
- [Li et al 2004][research_li_zhou_2004]
- [Li et al 2007][research_li_ma_2007]
- [Li et al 2009][research_li_cui_2009_b]
- [Li et al 2011][research_li_huang_2011]
- [Li et al 2012][research_li_eggers_2012]
- [Li et al 2014][research_li_an_2014]
- [Li et al 2014][research_li_wu_2014]
- [Li et al 2015][research_li_han_2015]
- [Li et al 2015][research_li_zhang_2015]
- [Li et al 2016][research_li_yang_2016]
- [Li et al 2017][research_li_chen_2017]
- [Li et al 2017][research_li_chen_2017_b]
- [Li et al 2017][research_li_jin_2017]
- [Li et al 2017][research_li_liu_2017]
- [Li et al 2017][research_li_shen_2017]
- [Li et al 2017][research_li_tan_2017]
- [Li et al 2017][research_li_yu_2017]
- [Li et al 2017][research_li_zhang_2017]
- [Li et al 2018][research_li_chang_2018]
- [Li et al 2018][research_li_hu_2018]
- [Li et al 2018][research_li_jiao_2018]
- [Li et al 2019][research_li_chang_2019]
- [Li et al 2019][research_li_qin_2019]
- [Li et al 2019][research_li_wang_2019]
- [Li et al 2019][research_li_xia_2019]
- [Li et al 2020][research_li_chen_2020]
- [Li et al 2020][research_li_cui_2020]
- [Li et al 2020][research_li_sun_2020]
- [Li et al 2020][research_li_xie_2020]
- [Li et al 2020][research_li_yang_2020]
- [Li et al 2020][research_li_yang_2020_b]
- [Li et al 2021][research_li_guo_2021]
- [Li et al 2021][research_li_hang_2021]
- [Li et al 2021][research_li_jiang_2021]
- [Li et al 2021][research_li_jiang_2021_b]
- [Li et al 2021][research_li_jin_2021]
- [Li et al 2021][research_li_sun_2021]
- [Li et al 2021][research_li_tang_2021]
- [Li et al 2021][research_li_wang_2021]
- [Li et al 2021][research_li_xie_2021]
- [Li et al 2021][research_li_zhou_2021]
- [Li et al 2022][research_li_chen_2022]
- [Li et al 2022][research_li_lei_2022]
- [Li et al 2022][research_li_li_2022]
- [Li et al 2022][research_li_liu_2022]
- [Li et al 2022][research_li_tang_2022]
- [Li et al 2022][research_li_zhou_2022]
- [Li et al 2023][research_li_ding_2023]
- [Li et al 2023][research_li_leng_2023]
- [Li et al 2023][research_li_liang_2023]
- [Li et al 2023][research_li_ren_2023]
- [Li et al 2023][research_li_wang_2023]
- [Li et al 2024][research_li_huang_2024]
- [Li et al 2024][research_li_ma_2024]
- [Li et al 2024][research_li_sun_2024]
- [Li et al 2024][research_li_sun_2024_b]
- [Li et al 2024][research_li_wang_2024]
- [Li et al 2024][research_li_wang_2024_b]
- [Li et al 2024][research_li_wang_2024_c]
- [Li et al 2025][research_li_dou_2025]
- [Li et al 2025][research_li_liu_2025]
- [Li et al 2025][research_li_ning_2025]
- [Li et al 2025][research_li_wang_2025]
- [Li et al 2025][research_li_wu_2025]
- [Li et al 2026][research_li_ding_2026]
- [Li et al 2026][research_li_dou_2026]
- [Li et al 2026][research_li_jiao_2026]
- [Li et al 2026][research_li_li_2026]
- [Li et al 2026][research_li_ling_2026]
- [Li et al 2026][research_li_liu_2026]
- [Li et al 2026][research_li_wang_2026]
- [Li et al 2026][research_li_yang_2026]
- [Li et al 2026][research_li_zhan_2026]
- [Li et al 2026][research_li_zhao_2026]
- [Lian et al 2012][research_lian_shi_2012]
- [Lian et al 2013][research_lian_bai_2013]
- [Lian et al 2013][research_lian_bai_2013_b]
- [Lian et al 2025][research_lian_xiong_2025]
- [Liang et al 2013][research_liang_gong_2013]
- [Liang et al 2021][research_liang_xu_2021]
- [Liang et al 2022][research_liang_huang_2022]
- [Liang et al 2024][research_liang_guo_2024]
- [Liang et al 2025][research_liang_gao_2025]
- [Liang et al 2025][research_liang_wen_2025]
- [Liao et al 2023][research_liao_chu_2023]
- [Libby et al 1963][research_libby_fox_1963]
- [Lidar complex of a 2020][research_lidar_complex_2020]
- [Liever et al 2004][research_liever_habchi_2004]
- [Light High-Temperature Aluminum Alloys 1992][research_light_high_temperature_1992]
- [Lightweight low-cost flight test 2007][research_lightweight_low_cost_2007]
- [Lijewski 1980][research_lijewski_1980]
- [Lillis 1987][research_lillis_1987]
- [Lim et al 2006][research_lim_wang_2006]
- [Lim et al 2025][research_lim_lee_2025]
- [Limage 1978][research_limage_1978]
- [Limage 1996][research_limage_1996]
- [Lin and Luo 1995][research_lin_luo_1995]
- [Lin and Shen 1997][research_lin_shen_1997]
- [Lin et al 1991][research_lin_rao_1991]
- [Lin et al 1995][research_lin_shen_1995]
- [Lin et al 2006][research_lin_tam_2006]
- [Lin et al 2007][research_lin_tam_2007]
- [Lin et al 2026][research_lin_geng_2026]
- [Lin et al 2026][research_lin_wu_2026]
- [Lind et al 1999][research_lind_buffington_1999]
- [Lindsey and McMullan 2006][research_lindsey_mcmullan_2006]
- [Lindstedt and Markaki 2009][research_lindstedt_markaki_2009]
- [Ling et al 2025][research_ling_wang_2025]
- [Lino et al 2024][research_lino_oliveirajunior_2024]
- [Linqi et al 2015][research_linqi_qun_2015]
- [Liou et al 2000][research_liou_huang_2000]
- [Liou et al 2010][research_liou_benson_2010]
- [Lippitt et al 1983][research_lippitt_jr_1983]
- [Liquid Hydrocarbon Fuels for 2001][research_liquid_hydrocarbon_2001]
- [Liquid-Phase Reactions of Vaporizing 1978][research_liquid_phase_reactions_1978]
- [Liqun et al 2017][research_liqun_chaoyang_2017]
- [Liston and Small 1992][research_liston_small_1992]
- [Liu 1992][research_liu_1992]
- [Liu 1995][research_liu_1995]
- [Liu 2014][research_liu_2014]
- [Liu 2023][research_liu_2023]
- [Liu and Brown 2012][research_liu_brown_2012]
- [Liu and Cao 2017][research_liu_cao_2017]
- [Liu and Fang 2024][research_liu_fang_2024]
- [Liu and Jiang 2013][research_liu_jiang_2013]
- [Liu and Liu 2022][research_liu_liu_2022]
- [Liu and Lu 2011][research_liu_lu_2011]
- [Liu and Shen 2015][research_liu_shen_2015]
- [Liu and Squire 1986][research_liu_squire_1986]
- [Liu and Yao 2021][research_liu_yao_2021]
- [Liu and Yao 2021][research_liu_yao_2021_b]
- [Liu et al 2002][research_liu_chen_2002]
- [Liu et al 2005][research_liu_wang_2005]
- [Liu et al 2005][research_liu_zhao_2005]
- [Liu et al 2007][research_liu_xiao_2007]
- [Liu et al 2009][research_liu_wang_2009]
- [Liu et al 2010][research_liu_hou_2010]
- [Liu et al 2014][research_liu_ding_2014]
- [Liu et al 2014][research_liu_hong_2014]
- [Liu et al 2014][research_liu_wang_2014]
- [Liu et al 2015][research_liu_bi_2015]
- [Liu et al 2016][research_liu_jun_2016]
- [Liu et al 2016][research_liu_liang_2016]
- [Liu et al 2016][research_liu_liu_2016]
- [Liu et al 2016][research_liu_wang_2016]
- [Liu et al 2017][research_liu_wang_2017]
- [Liu et al 2018][research_liu_shi_2018]
- [Liu et al 2018][research_liu_zhang_2018]
- [Liu et al 2019][research_liu_baccarella_2019]
- [Liu et al 2019][research_liu_fan_2019]
- [Liu et al 2019][research_liu_gao_2019]
- [Liu et al 2019][research_liu_li_2019]
- [Liu et al 2019][research_liu_song_2019]
- [Liu et al 2019][research_liu_zhang_2019]
- [Liu et al 2020][research_liu_bai_2020]
- [Liu et al 2020][research_liu_luo_2020]
- [Liu et al 2020][research_liu_luo_2020_b]
- [Liu et al 2021][research_liu_xie_2021]
- [Liu et al 2022][research_liu_chen_2022]
- [Liu et al 2022][research_liu_he_2022]
- [Liu et al 2022][research_liu_manzie_2022]
- [Liu et al 2022][research_liu_pan_2022]
- [Liu et al 2022][research_liu_pang_2022]
- [Liu et al 2022][research_liu_qiao_2022]
- [Liu et al 2022][research_liu_wu_2022]
- [Liu et al 2023][research_liu_cai_2023]
- [Liu et al 2023][research_liu_cao_2023]
- [Liu et al 2023][research_liu_fang_2023]
- [Liu et al 2023][research_liu_han_2023]
- [Liu et al 2023][research_liu_xue_2023]
- [Liu et al 2023][research_liu_yang_2023]
- [Liu et al 2024][research_liu_bian_2024]
- [Liu et al 2024][research_liu_pan_2024]
- [Liu et al 2025][research_liu_li_2025]
- [Liu et al 2025][research_liu_lyu_2025]
- [Liu et al 2025][research_liu_shan_2025]
- [Liu et al 2025][research_liu_xu_2025]
- [Liu et al 2025][research_liu_zhang_2025]
- [Liu et al 2025][research_liu_zhu_2025]
- [Liu et al 2026][research_liu_chen_2026]
- [Liu et al 2026][research_liu_yang_2026]
- [Liu et al 2026][research_liu_zhang_2026]
- [Lloyd 1959][research_lloyd_1959]
- [Lobb et al 1955][research_lobb_winkler_1955]
- [Lobbia 2015][research_lobbia_2015]
- [Lobbia and Suzuki 2003][research_lobbia_suzuki_2003]
- [Lock et al 2025][research_lock_oberman_2025]
- [Lockman, W. K. 1967][research_lockmanwk_1967]
- [Lockwood et al 1996][research_lockwood_petley_1996]
- [Lockwood et al 1999][research_lockwood_petley_1999]
- [Lofthouse et al 2002][research_lofthouse_hughson_2002]
- [Loh and Hui 1991][research_loh_hui_1991]
- [Lohner and Yang 2002][research_lohner_yang_2002]
- [Long and Jr 1992][research_long_jr_1992]
- [Longwell and Weiss 1952][research_longwell_weiss_1952]
- [Lonkar and Panda 2025][research_lonkar_panda_2025]
- [Lonkar and Panda 2026][research_lonkar_panda_2026]
- [Loper and Lightsey 1967][research_loper_lightsey_1967]
- [Losik 2008][research_losik_2008]
- [Loth et al 2016][research_loth_candon_2016]
- [Louda and Příhoda 2018][research_louda_prihoda_2018]
- [Louis M. Edelman][research_louismedelman]
- [Low Temperature Thermal Expansion 2016][research_low_temperature_2016]
- [Lowell 1963][research_lowell_1963]
- [Lu 1991][research_lu_1991]
- [Lu and Jiang 2019][research_lu_jiang_2019]
- [Lu and Liu 2011][research_lu_liu_2011]
- [Lu and Liu 2012][research_lu_liu_2012]
- [Lu and Mahapatra 2008][research_lu_mahapatra_2008]
- [Lu and Zhou 2017][research_lu_zhou_2017]
- [Lu et al 2012][research_lu_li_2012]
- [Lu et al 2016][research_lu_wang_2016]
- [Lu et al 2016][research_lu_zhang_2016]
- [Lu et al 2016][research_lu_zhang_2016_b]
- [Lu et al 2025][research_lu_sheng_2025]
- [Lu et al 2025][research_lu_zhang_2025]
- [Lubarsky and Levy 1998][research_lubarsky_levy_1998]
- [Lubing et al 2017][research_lubing_yang_2017]
- [Lubing et al 2020][research_lubing_yangfei_2020]
- [Luboński 1964][research_lubonski_1964]
- [Luce and Flowers 1961][research_luce_flowers_1961]
- [Luce and Jr 1949][research_luce_jr_1949]
- [Lucquin and Antonik 1972][research_lucquin_antonik_1972]
- [Ludwig and Sulzmann 1961][research_ludwig_sulzmann_1961]
- [Luecke 1957][research_luecke_1957]
- [Lugrin][research_lugrin]
- [Luján et al 2016][research_lujan_climent_2016]
- [Lukasiewicz 1961][research_lukasiewicz_1961]
- [Lumpkin, Iii and Chapman 1991][research_lumpkiniii_chapman_1991]
- [Lunan 2015][research_lunan_2015]
- [Luo 1999][research_luo_1999]
- [Luo and Baysal 1999][research_luo_baysal_1999]
- [Luo and Bray 1998][research_luo_bray_1998]
- [Luo and Wang 2015][research_luo_wang_2015]
- [Luo et al 2003][research_luo_luo_2003]
- [Luo et al 2020][research_luo_wei_2020]
- [Luo et al 2022][research_luo_feng_2022]
- [Luo et al 2024][research_luo_tao_2024]
- [Luo et al 2025][research_luo_he_2025]
- [Luo et al 2025][research_luo_sun_2025]
- [Luo et al 2026][research_luo_tian_2026]
- [Lushchik et al 1993][research_lushchik_sizov_1993]
- [Lux, Jessica and Burkes, Darryl A. 2008][research_luxjessica_burkesdarryla_2008]
- [Lux-Baumann, Jessica and Burkes, Darryl 2006][research_luxbaumannjessica_burkesdarryl_2006]
- [Lv and Zhou 2023][research_lv_zhou_2023]
- [Lv et al 2026][research_lv_li_2026]
- [Lynch 1968][research_lynch_1968]
- [Lyon 1992][research_lyon_1992]
- [Lüdeke and Schülein 2003][research_ludeke_schulein_2003]
- [M. A. Al-Nimr, Naser S. Al-Huniti 2000][research_maalnimrnasersalhuniti_2000]
- [Ma and Zhong 1999][research_ma_zhong_1999]
- [Ma et al 2006][research_ma_yuan_2006]
- [Ma et al 2020][research_ma_wu_2020]
- [Ma et al 2021][research_ma_sun_2021]
- [Ma et al 2022][research_ma_xie_2022]
- [Ma et al 2023][research_ma_liu_2023]
- [Maas et al 2004][research_maas_irvine_2004]
- [Maccallum 1969][research_maccallum_1969]
- [Maccormack 1989][research_maccormack_1989]
- [Mace and Nyberg 1992][research_mace_nyberg_1992]
- [Macheret et al 2001][research_macheret_shneider_2001]
- [Machnik et al 2022][research_machnik_decker_2022]
- [Machrafi and Cavadiasa 2008][research_machrafi_cavadiasa_2008]
- [Mack et al 2009][research_mack_steelant_2009]
- [MacKenzie 1967][research_mackenzie_1967]
- [Mackle][research_mackle]
- [Mackle and Jahn 2024][research_mackle_jahn_2024]
- [Mackle et al 2024][research_mackle_lock_2024]
- [MacMahan and Reniers 2012][research_macmahan_reniers_2012]
- [Macmillan 1981][research_macmillan_1981]
- [Maddalena and Gopal 2023][research_maddalena_gopal_2023]
- [Madden and Solomon 1993][research_madden_solomon_1993]
- [Madhumitha and Karmakar 2024][research_madhumitha_karmakar_2024]
- [Magomedov 2009][research_magomedov_2009]
- [Mahapatra et al 2008][research_mahapatra_lu_2008]
- [Mahato et al 2023][research_mahato_sarikonda_2023]
- [Mahlmeister et al 1955][research_mahlmeister_ishimoto_1955]
- [Mahmoud et al 2017][research_mahmoud_hao_2017]
- [Mahulikar et al 2008][research_mahulikar_khurana_2008]
- [Maisaia 2023][research_maisaia_2023]
- [Maita et al 1990][research_maita_ohkami_1990]
- [Majumdar 2011][research_majumdar_2011]
- [Makhija et al 2026][research_makhija_bodi_2026]
- [Maleque 2016][research_maleque_2016]
- [Malik][research_malik]
- [Mallikarjun et al 2023][research_mallikarjun_casseau_2023]
- [Malsur Dharavath et al 2023][research_malsurdharavath_pmanna_2023]
- [Mane et al 2026][research_mane_pandey_2026]
- [Mani and Haney 1994][research_mani_haney_1994]
- [Manimaran 2016][research_manimaran_2016]
- [Manke 2005][research_manke_2005]
- [Mann and Garner 1977][research_mann_garner_1977]
- [Manna et al 2023][research_manna_dharavath_2023]
- [Mannai 1962][research_mannai_1962]
- [Manning et al 1992][research_manning_baum_1992]
- [Manoj Prabakar and Muruganandam 2019][research_manojprabakar_muruganandam_2019]
- [Manor et al 2002][research_manor_lau_2002]
- [Mao 2023][research_mao_2023]
- [Maorui Zhang et al 2010][research_maoruizhang_yongsun_2010]
- [Marchand 1989][research_marchand_1989]
- [Marconi, F. et al 1976][research_marconif_salasm_1976]
- [Marcum 2001][research_marcum_2001]
- [Margaritis et al 2024][research_margaritis_scherding_2024]
- [Marin et al 2021][research_marin_tombolesi_2021]
- [Marinho and de Farias 2020][research_marinho_defarias_2020]
- [Markova et al 2017][research_markova_aksenov_2017]
- [Marley and Driscoll 2017][research_marley_driscoll_2017]
- [Marley and Driscoll 2018][research_marley_driscoll_2018]
- [Marley and Driscoll 2022][research_marley_driscoll_2022]
- [Marlina 2018][research_marlina_2018]
- [Marquart 1991][research_marquart_1991]
- [Marren et al 2001][research_marren_lewis_2001]
- [Marschall 2011][research_marschall_2011]
- [Marsh and Sears 1954][research_marsh_sears_1954]
- [Marshall and Davis 2001][research_marshall_davis_2001]
- [Marshall et al 2005][research_marshall_corpening_2005]
- [Marshall et al 2014][research_marshall_cox_2014]
- [Marston 1965][research_marston_1965]
- [Martel 1970][research_martel_1970]
- [Martel 1988][research_martel_1988]
- [Martin and Gerber 1953][research_martin_gerber_1953]
- [Martin and Peter 2026][research_martin_peter_2026]
- [Martin et al 1998][research_martin_karasi_1998]
- [Martínez Morán 2018][research_martinezmoran_2018]
- [Marvin 1968][research_marvin_1968]
- [Mary and Sagaut 2001][research_mary_sagaut_2001]
- [Mashburn 1969][research_mashburn_1969]
- [Mashio et al 2001][research_mashio_kurashina_2001]
- [Maslov 2001][research_maslov_2001]
- [Massa 2022][research_massa_2022]
- [Massa and Pace 2025][research_massa_pace_2025]
- [Masson et al 1989][research_masson_jumper_1989]
- [Mateer et al 1976][research_mateer_brosh_1976]
- [Matheny and Panageas 1981][research_matheny_panageas_1981]
- [Matheny and Smith 2026][research_matheny_smith_2026]
- [Mathur 2026][research_mathur_2026]
- [Mathur 2026][research_mathur_2026_b]
- [Mathur et al 1999][research_mathur_streby_1999]
- [Mathur et al 2001][research_mathur_gruber_2001]
- [Matsukawa 2011][research_matsukawa_2011]
- [Matsunaga et al 2017][research_matsunaga_takahashi_2017]
- [Matsuo et al 2023][research_matsuo_kim_2023]
- [Matsuyama et al 2003][research_matsuyama_ohnishi_2003]
- [Matthews 1992][research_matthews_1992]
- [Matthews 1993][research_matthews_1993]
- [Matthews and Jones 2005][research_matthews_jones_2005]
- [Matthews and Trimmer 1969][research_matthews_trimmer_1969]
- [Maus et al 1983][research_maus_griffith_1983]
- [Maxwell 2016][research_maxwell_2016]
- [Maxwell 2017][research_maxwell_2017]
- [Maxwell 2017][research_maxwell_2017_b]
- [Maxwell 2019][research_maxwell_2019]
- [Maxwell and Goodwin 2017][research_maxwell_goodwin_2017]
- [Maxwell and Goodwin 2018][research_maxwell_goodwin_2018]
- [Maxwell and Goodwin 2018][research_maxwell_goodwin_2018_b]
- [Maxwell and Goodwin 2018][research_maxwell_goodwin_2018_c]
- [Maxwell and Hoang 2016][research_maxwell_hoang_2016]
- [Maxwell and Phoenix 2017][research_maxwell_phoenix_2017]
- [May and Richey 1979][research_may_richey_1979]
- [Maydew 1964][research_maydew_1964]
- [Mayer and Chalfant 2023][research_mayer_chalfant_2023]
- [Mayer and Paynter 1994][research_mayer_paynter_1994]
- [Mayer and Paynter 1995][research_mayer_paynter_1995]
- [Maynard et al 2025][research_maynard_patel_2025]
- [Mayne 1976][research_mayne_1976]
- [Mayne 1979][research_mayne_1979]
- [Mayrhofer and Sachs 1999][research_mayrhofer_sachs_1999]
- [Mazdiyasni 1989][research_mazdiyasni_1989]
- [Mazdiyasni and Chen 1988][research_mazdiyasni_chen_1988]
- [Mazdiyasni et al 1991][research_mazdiyasni_chen_1991]
- [Mbagwu et al 2018][research_mbagwu_driscoll_2018]
- [McCarthy 2008][research_mccarthy_2008]
- [Mcclinton 1976][research_mcclinton_1976]
- [McClinton et al 1996][research_mcclinton_roudakov_1996]
- [McClinton et al 1999][research_mcclinton_hunt_1999]
- [McClure and Sirbaugh 1991][research_mcclure_sirbaugh_1991]
- [McConnell 2004][research_mcconnell_2004]
- [McCormick et al 2010][research_mccormick_wakayama_2010]
- [McCOWN et al 1966][research_mccown_barrett_1966]
- [McCracken 1970][research_mccracken_1970]
- [McDaniel 2005][research_mcdaniel_2005]
- [McDaniel, Jr. 1998][research_mcdanieljr_1998]
- [McDonald 1960][research_mcdonald_1960]
- [McDonald 2025][research_mcdonald_2025]
- [McDonald and Mavris 2000][research_mcdonald_mavris_2000]
- [McDonald et al 2017][research_mcdonald_rice_2017]
- [McElderry 1973][research_mcelderry_1973]
- [McGill 2000][research_mcgill_2000]
- [McGrory 2001][research_mcgrory_2001]
- [Mcintosh, Jr. 1964][research_mcintoshjr_1964]
- [Mcintosh, Jr. 1972][research_mcintoshjr_1972]
- [Mckenzie 1973][research_mckenzie_1973]
- [McKenzie and Fletcher 1993][research_mckenzie_fletcher_1993]
- [McLean][research_mclean]
- [McLean and Matoi 1986][research_mclean_matoi_1986]
- [McMillin 1969][research_mcmillin_1969]
- [McQuaid 2013][research_mcquaid_2013]
- [McQuellin and Buttsworth 2024][research_mcquellin_buttsworth_2024]
- [McQuellin et al 2020][research_mcquellin_neely_2020]
- [McRae and Edwards 2001][research_mcrae_edwards_2001]
- [McRae and Neaves 1998][research_mcrae_neaves_1998]
- [McRuer 1991][research_mcruer_1991]
- [McTaggart 1973][research_mctaggart_1973]
- [Mease and Vinh 1988][research_mease_vinh_1988]
- [Measurement of wind pressure 2015][research_measurement_of_2015]
- [Measurement Techniques for Supersonic 1974][research_measurement_techniques_1974]
- [Measuring kinematic parameters of 1998][research_measuring_kinematic_1998]
- [Medina et al 2021][research_medina_patel_2021]
- [Medwick et al 1999][research_medwick_castro_1999]
- [Mee][research_mee]
- [Mehta et al 2012][research_mehta_bowles_2012]
- [Mehta et al 2025][research_mehta_brewer_2025]
- [Mehta, Unmeel B. and Kutler, Paul 1994][research_mehtaunmeelb_kutlerpaul_1994]
- [Meier 1984][research_meier_1984]
- [Meintanis et al 2002][research_meintanis_bengtson_2002]
- [Meisel and Cote 1985][research_meisel_cote_1985]
- [Melis and Gladden 1990][research_melis_gladden_1990]
- [Melville and Helmich 2021][research_melville_helmich_2021]
- [Mendiratta and Choudhury 1978][research_mendiratta_choudhury_1978]
- [Meng et al 2020][research_meng_ye_2020]
- [Meng et al 2021][research_meng_tian_2021]
- [Meng et al 2022][research_meng_sun_2022]
- [Meng et al 2024][research_meng_jin_2024]
- [Meng et al 2024][research_meng_sun_2024]
- [Menne et al 1994][research_menne_weiland_1994]
- [Menon 1989][research_menon_1989]
- [Menon 1990][research_menon_1990]
- [Menon 1991][research_menon_1991]
- [Menon 1992][research_menon_1992]
- [Menon 1992][research_menon_1992_b]
- [Menon and Jou 1990][research_menon_jou_1990]
- [Menon and Jou 1991][research_menon_jou_1991]
- [Menon et al 2003][research_menon_genin_2003]
- [Menssen 2026][research_menssen_2026]
- [Meriwether 2005][research_meriwether_2005]
- [Merkle 2007][research_merkle_2007]
- [Merkli 1975][research_merkli_1975]
- [Mermagen 1964][research_mermagen_1964]
- [Mermagen and Yalamanchili 1983][research_mermagen_yalamanchili_1983]
- [Merriam et al 1962][research_merriam_smoluchowski_1962]
- [Merryman 1962][research_merryman_1962]
- [Mertaugh 1998][research_mertaugh_1998]
- [Merz 1968][research_merz_1968]
- [Meshcheryakov and Yashina 2015][research_meshcheryakov_yashina_2015]
- [Messersmith 1995][research_messersmith_1995]
- [Messitt et al 1992][research_messitt_dallemagne_1992]
- [Mestwerdt and Rambauske 1961][research_mestwerdt_rambauske_1961]
- [Metallic SEAL Rings for][research_metallic_seal]
- [Metghalchi 2009][research_metghalchi_2009]
- [Methodology for Investigation of][research_methodology_for]
- [Meuwly 2014][research_meuwly_2014]
- [Meyer 1958][research_meyer_1958]
- [Meyer 1969][research_meyer_1969]
- [Meyer et al 1997][research_meyer_butler_1997]
- [Mi et al 2025][research_mi_wang_2025]
- [Miao et al 2020][research_miao_wang_2020]
- [Michalski et al 2018][research_michalski_boust_2018]
- [Micka and Driscoll 2008][research_micka_driscoll_2008]
- [Micka and Driscoll 2009][research_micka_driscoll_2009]
- [Midea 1991][research_midea_1991]
- [Miele 1962][research_miele_1962]
- [Miele and Hull 1963][research_miele_hull_1963]
- [Miele and Pritchard 1963][research_miele_pritchard_1963]
- [Miele and Saaris 1963][research_miele_saaris_1963]
- [Miers et al 2020][research_miers_alshehab_2020]
- [Mifsud et al 2012][research_mifsud_estruchsamper_2012]
- [Mikhail 1979][research_mikhail_1979]
- [Mikhaylov 2013][research_mikhaylov_2013]
- [Mikkelsen and Long 2005][research_mikkelsen_long_2005]
- [Mikulla and Horstman 1976][research_mikulla_horstman_1976]
- [Miles 1998][research_miles_1998]
- [Miles 2001][research_miles_2001]
- [Miles 2003][research_miles_2003]
- [Miles and Brown 2002][research_miles_brown_2002]
- [Miles and Macheret 2006][research_miles_macheret_2006]
- [Miller 1965][research_miller_1965]
- [Miller 1999][research_miller_1999]
- [Miller and Smith 2003][research_miller_smith_2003]
- [Miller et al 1997][research_miller_argrow_1997]
- [Miller et al 2011][research_miller_nagpal_2011]
- [Millerd][research_millerd]
- [Milligan et al 2009][research_milligan_wolff_2009]
- [Mills 2001][research_mills_2001]
- [Mills 2002][research_mills_2002]
- [Min et al 2009][research_min_hailong_2009]
- [Min et al 2024][research_min_hong_2024]
- [Min et al 2026][research_min_sun_2026]
- [Minard and Falempin 2008][research_minard_falempin_2008]
- [Minato et al 2009][research_minato_higashino_2009]
- [Minato et al 2012][research_minato_higashino_2012]
- [Miner and Lewis 1974][research_miner_lewis_1974]
- [Minimum Performance Standard for][research_minimum_performance]
- [Minimum Performance Standard for][research_minimum_performance_b]
- [Mirhosseini et al 2025][research_mirhosseini_najafi_2025]
- [Mirmirani et al 2005][research_mirmirani_wu_2005]
- [Mirmirani et al 2009][research_mirmirani_kuipers_2009]
- [Mironov and Aniskin 2004][research_mironov_aniskin_2004]
- [Mishler and Wilkinson 1992][research_mishler_wilkinson_1992]
- [Misra 1994][research_misra_1994]
- [Mitani 1995][research_mitani_1995]
- [Mitani 1996][research_mitani_1996]
- [Mitani and Izumikawa 2000][research_mitani_izumikawa_2000]
- [Mitani and Kouchi 2005][research_mitani_kouchi_2005]
- [Mitani et al 2003][research_mitani_tomioka_2003]
- [Mitran 2001][research_mitran_2001]
- [Mittal et al 2026][research_mittal_shahriar_2026]
- [Miyajima et al 1992][research_miyajima_chinzei_1992]
- [Miyashita et al 2025][research_miyashita_matsuo_2025]
- [Miyashita et al 2025][research_miyashita_sugihara_2025]
- [Miyaura et al 2018][research_miyaura_daimon_2018]
- [Miyazaki et al 1986][research_miyazaki_yoshida_1986]
- [Miyazawa 2000][research_miyazawa_2000]
- [Modelling endothermic reactions in 1997][research_modelling_endothermic_1997]
- [Moga 1980][research_moga_1980]
- [Mohamadi and Tahsini 2023][research_mohamadi_tahsini_2023]
- [Mohieldin and Carson 2003][research_mohieldin_carson_2003]
- [Mohieldin et al 2001][research_mohieldin_tiwari_2001]
- [Mohieldin, T. O. et al 2004][research_mohieldinto_tiwarisn_2004]
- [Moin and Lele 1998][research_moin_lele_1998]
- [Molina et al 1996][research_molina_simeonides_1996]
- [Molvik et al 1992][research_molvik_bowles_1992]
- [Molvik et al 1993][research_molvik_bowles_1993]
- [Molvik et al 1993][research_molvik_bowles_1993_b]
- [Molvik, Gregory A. and Merkle, Charles L. 1989][research_molvikgregorya_merklecharlesl_1989]
- [Mondal and Jagtap 2026][research_mondal_jagtap_2026]
- [Montagne, J.-L. et al 1988][research_montagnejl_yeehc_1988]
- [Montagne, J.-L. et al 1989][research_montagnejl_yeehc_1989]
- [Monteil 2024][research_monteil_2024]
- [Montes et al 2005][research_montes_king_2005]
- [Montgomery and Garrard 2005][research_montgomery_garrard_2005]
- [Montgomery et al 2006][research_montgomery_cremer_2006]
- [Mooij 2023][research_mooij_2023]
- [Moon and Sung 2015][research_moon_sung_2015]
- [Moore 1965][research_moore_1965]
- [Moorhouse 1990][research_moorhouse_1990]
- [Moran and Kolb 1977][research_moran_kolb_1977]
- [Moran et al 2023][research_moran_mcquellin_2023]
- [Morani et al 2026][research_morani_fruncillo_2026]
- [Moreira and Azevedo 2005][research_moreira_azevedo_2005]
- [Morelli 2008][research_morelli_2008]
- [Moretti and Byrne 1964][research_moretti_byrne_1964]
- [Morgan and Stalker 1985][research_morgan_stalker_1985]
- [Morgan and Zander 2009][research_morgan_zander_2009]
- [Morgan et al 2012][research_morgan_duraisamy_2012]
- [Morgan et al 2014][research_morgan_duraisamy_2014]
- [Morger 1988][research_morger_1988]
- [Mori 1965][research_mori_1965]
- [Mori et al 1993][research_mori_masutani_1993]
- [Mori et al 2001][research_mori_maita_2001]
- [Mori et al 2002][research_mori_tsuchiya_2002]
- [Mori et al 2012][research_mori_ishibashi_2012]
- [Morimoto and Chuang 1998][research_morimoto_chuang_1998]
- [Morinishi 1999][research_morinishi_1999]
- [Morita et al 2020][research_morita_tsuchiya_2020]
- [Morris and Tigner 1995][research_morris_tigner_1995]
- [Morris et al 2002][research_morris_jr_2002]
- [Moses et al 1999][research_moses_bouchard_1999]
- [Moss and Simmonds 1987][research_moss_simmonds_1987]
- [Moss et al 2006][research_moss_boyles_2006]
- [Moss et al 2026][research_moss_vasile_2026]
- [Moszee and Moszee 1997][research_moszee_moszee_1997]
- [Mott and Oran 2001][research_mott_oran_2001]
- [Moulic 1963][research_moulic_1963]
- [Moura and Borges Ribeiro 2025][research_moura_borgesribeiro_2025]
- [Moura and Borges Ribeiro 2025][research_moura_borgesribeiro_2025_b]
- [Moura and Borges Ribeiro 2025][research_moura_borgesribeiro_2025_c]
- [Moura and Borges Ribeiro 2025][research_moura_borgesribeiro_2025_d]
- [Moura and Borges Ribeiro 2025][research_moura_borgesribeiro_2025_e]
- [Moura and Ribeiro 2024][research_moura_ribeiro_2024]
- [Moura et al 2019][research_moura_wheatley_2019]
- [Mrozinski and Hayes 1999][research_mrozinski_hayes_1999]
- [Mu et al 2008][research_mu_zheng_2008]
- [Mu et al 2022][research_mu_wang_2022]
- [Mudaliar et al 2022][research_mudaliar_gomes_2022]
- [Muddamarri and M. Badgujar 2024][research_muddamarri_mbadgujar_2024]
- [Muddasar 2022][research_muddasar_2022]
- [Mueller 1989][research_mueller_1989]
- [Muhammad Haseeb 2025][research_muhammadhaseeb_2025]
- [Mukherjee and Thomson 2009][research_mukherjee_thomson_2009]
- [Mungal 1998][research_mungal_1998]
- [Munipalli et al 2005][research_munipalli_subbarao_2005]
- [Munuswamy and Govardhan 2022][research_munuswamy_govardhan_2022]
- [Mura and Sabelnikov 2021][research_mura_sabelnikov_2021]
- [Murbach 1993][research_murbach_1993]
- [Murphy et al 2004][research_murphy_buning_2004]
- [Murray 2012][research_murray_2012]
- [Murray and Hillier 2009][research_murray_hillier_2009]
- [Murray and Steelant 2009][research_murray_steelant_2009]
- [Murray et al 2014][research_murray_tinney_2014]
- [Mursenkova et al 2021][research_mursenkova_liao_2021]
- [Mursenkova et al 2022][research_mursenkova_ivanov_2022]
- [Mursenkova et al 2023][research_mursenkova_ivanov_2023]
- [Murty and Chakraborty 2011][research_murty_chakraborty_2011]
- [Murugan and Govardhan 2016][research_murugan_govardhan_2016]
- [Muruganandam et al 2026][research_muruganandam_hemchandra_2026]
- [Murugesan et al 2018][research_murugesan_chakravarthy_2018]
- [Murzionak][research_murzionak]
- [Musa et al 2018][research_musa_weixuan_2018]
- [Musa et al 2022][research_musa_huang_2022]
- [Musa et al 2024][research_musa_huang_2024]
- [Musa et al 2025][research_musa_huang_2025]
- [Musal 1962][research_musal_1962]
- [Musal et al 1964][research_musal_hm_1964]
- [Musielak and Musielak 1997][research_musielak_musielak_1997]
- [Muslubas and Eyi 2015][research_muslubas_eyi_2015]
- [Muss et al 2003][research_muss_johnson_2003]
- [Myong 1999][research_myong_1999]
- [Myrabo 2004][research_myrabo_2004]
- [Myrabo and Nagamatsu 1991][research_myrabo_nagamatsu_1991]
- [Myrabo et al 1995][research_myrabo_head_1995]
- [Mysko et al 1993][research_mysko_chyu_1993]
- [Nadler 2003][research_nadler_2003]
- [Naftel et al 1986][research_naftel_wilhite_1986]
- [Nagamatsu 1989][research_nagamatsu_1989]
- [Nagamatsu et al 1960][research_nagamatsu_workman_1960]
- [Nagamatsu et al 1961][research_nagamatsu_sheer_1961]
- [Nagao et al 2019][research_nagao_yoshida_2019]
- [Nagarajan Kirupakaran et al 2023][research_nagarajankirupakaran_kv_2023]
- [Nagdewe and Shevare 2006][research_nagdewe_shevare_2006]
- [Nagel and Becker 1973][research_nagel_becker_1973]
- [Nagendra Babu et al 2018][research_nagendrababu_jayakrishna_2018]
- [Nair et al 2003][research_nair_kumar_2003]
- [Nair et al 2005][research_nair_kumar_2005]
- [Nair et al 2020][research_nair_s_2020]
- [Nair et al 2022][research_nair_suryan_2022]
- [Nair et al 2023][research_nair_suryan_2023]
- [Najafiyazdi 2005][research_najafiyazdi_2005]
- [Najafiyazdi 2005][research_najafiyazdi_2005_b]
- [Nakagawa and Kuwahara 1992][research_nakagawa_kuwahara_1992]
- [Nakamori and Nakamura 1995][research_nakamori_nakamura_1995]
- [Nakaya et al 2015][research_nakaya_hikichi_2015]
- [Nakayama et al 2018][research_nakayama_edanaga_2018]
- [Nalabala and Dinda 2024][research_nalabala_dinda_2024]
- [Namatsaliuk et al 2025][research_namatsaliuk_donato_2025]
- [NamKoung et al 2012][research_namkoung_hong_2012]
- [Nance 2013][research_nance_2013]
- [Nangia 2011][research_nangia_2011]
- [Narayan 1994][research_narayan_1994]
- [Narayan and Kumar 1989][research_narayan_kumar_1989]
- [Nardo and Sadler 1962][research_nardo_sadler_1962]
- [Nardozzo et al 2019][research_nardozzo_popkin_2019]
- [NASA Glenn Research Center's 2002][research_nasa_glenn_2002]
- [Natan 1987][research_natan_1987]
- [Natan and Gany 1989][research_natan_gany_1989]
- [Naumann et al 1993][research_naumann_ende_1993]
- [Naval Ordnance Systems Command Washington Dc 1957][research_navalordnancesystemscommandwashingtondc_1957]
- [Navier-Stokes Equations for Partially 2018][research_navier_stokes_equations_2018]
- [Nayal et al 2020][research_nayal_lamb_2020]
- [NbO2 crystal structure, thermal][research_nbo2_crystal]
- [Neaves and McRae 1995][research_neaves_mcrae_1995]
- [Neaves et al 2001][research_neaves_mcrae_2001]
- [Neely and Tjong 2008][research_neely_tjong_2008]
- [Neely and Tracy 2006][research_neely_tracy_2006]
- [Negishi et al 2015][research_negishi_daimon_2015]
- [Neitzke et al 2005][research_neitzke_rudnik_2005]
- [Nelson 1967][research_nelson_1967]
- [Nestler 1970][research_nestler_1970]
- [Neumann 1993][research_neumann_1993]
- [Neumann 2005][research_neumann_2005]
- [Neumann et al 1978][research_neumann_patterson_1978]
- [Neuwerth et al 1998][research_neuwerth_peiter_1998]
- [Neuwerth et al 1999][research_neuwerth_peiter_1999]
- [New-Generation Hypersonic Adiabatic Compression 2002][research_new_generation_hypersonic_2002]
- [Newberry et al 1988][research_newberry_dresser_1988]
- [Newell and Zakharov 2007][research_newell_zakharov_2007]
- [Newman et al 1992][research_newman_fulcher_1992]
- [Newnham 2004][research_newnham_2004]
- [Ng and Dressler 2002][research_ng_dressler_2002]
- [Ngo][research_ngo]
- [Ngoc Long 2016][research_ngoclong_2016]
- [Nguyen and Massa 2023][research_nguyen_massa_2023]
- [Nguyen and Massa 2023][research_nguyen_massa_2023_b]
- [Nguyen and Massa 2024][research_nguyen_massa_2024]
- [Nguyen et al 2011][research_nguyen_reinartz_2011]
- [Nguyen et al 2024][research_nguyen_vo_2024]
- [Nguyen-Bui and Duffa 2004][research_nguyenbui_duffa_2004]
- [Nicholas J DiGregorio et al][research_nicholasjdigregorio_thomaskwestiv]
- [Nichols and Heikkinen 2010][research_nichols_heikkinen_2010]
- [Nichols et al 2011][research_nichols_denny_2011]
- [Nichols et al 2015][research_nichols_mcdaniel_2015]
- [Nickerson et al 1988][research_nickerson_dunn_1988]
- [Nicolae Tudosie 2018][research_nicolaetudosie_2018]
- [Nicolaides and Brady 1959][research_nicolaides_brady_1959]
- [Nicoll 1962][research_nicoll_1962]
- [Nicolosi et al 2026][research_nicolosi_melone_2026]
- [Nie and Liu 2013][research_nie_liu_2013]
- [Nie et al 2019][research_nie_li_2019]
- [Nietubicz 1975][research_nietubicz_1975]
- [Niewöhner 2018][research_niewohner_2018]
- [Nikaido and Hobson 2025][research_nikaido_hobson_2025]
- [Ning][research_ning]
- [Ning 1981][research_ning_1981]
- [Nishida 2011][research_nishida_2011]
- [Nishiguchi et al 2025][research_nishiguchi_kodera_2025]
- [Nishimura 2014][research_nishimura_2014]
- [Nishino 1993][research_nishino_1993]
- [Nishio 1996][research_nishio_1996]
- [Nishio and Hagiwara 1998][research_nishio_hagiwara_1998]
- [Niu and Chen 2024][research_niu_chen_2024]
- [Niu and Chen 2025][research_niu_chen_2025]
- [Niu and Piao 2016][research_niu_piao_2016]
- [niu and wang 2023][research_niu_wang_2023]
- [Niu et al 2017][research_niu_yuan_2017]
- [Niu et al 2018][research_niu_chen_2018]
- [Nixon and Henderson 1966][research_nixon_henderson_1966]
- [Nnenna et al 2026][research_nnenna_matthew_2026]
- [Noda 1988][research_noda_1988]
- [Noftz and Jewell 2025][research_noftz_jewell_2025]
- [Nompelis et al 2005][research_nompelis_drayna_2005]
- [Nompelis et al 2006][research_nompelis_drayna_2006]
- [Nompelis et al 2007][research_nompelis_wan_2007]
- [Nompelis et al 2011][research_nompelis_bender_2011]
- [Non-empirical analytical model of 2019][research_non_empirical_analytical_2019]
- [Nondestructive Evaluation and Health 2014][research_nondestructive_evaluation_2014]
- [Nonequilibrium Stagnation Region Aerodynamic 1975][research_nonequilibrium_stagnation_1975]
- [Noori and Karimian 2008][research_noori_karimian_2008]
- [Noraml and Oblique Shock 1986][research_noraml_and_1986]
- [Nordin-Bates and Fureby 2015][research_nordinbates_fureby_2015]
- [Nordin-Bates et al 2017][research_nordinbates_fureby_2017]
- [Noren 2008][research_noren_2008]
- [Norfleet and Loper 1966][research_norfleet_loper_1966]
- [Norimatsu et al 2026][research_norimatsu_katsumura_2026]
- [Norimatsu et al 2026][research_norimatsu_katsumura_2026_b]
- [Normal and Oblique Shock 1986][research_normal_and_1986]
- [Norris 2006][research_norris_2006]
- [North 1983][research_north_1983]
- [North American Aviation Inc Los Angeles Ca 1964][research_northamericanaviationinclosangelesca_1964]
- [Northam and Anderson 1986][research_northam_anderson_1986]
- [Northam et al 1988][research_northam_lempert_1988]
- [Northam, G. B. 1985][research_northamgb_1985]
- [Novelli and Koschel 2001][research_novelli_koschel_2001]
- [Numerical Analysis of Two-Dimensional 2015][research_numerical_analysis_of_2015]
- [Numerical Modeling of Combustion 1991][research_numerical_modeling_1991]
- [Numerical Research of Three-Dimensional 2008][research_numerical_research_2008]
- [Numerical Simulation on Hypersonic 2015][research_numerical_simulation_2015]
- [Numerical Simulations of Oblique 2006][research_numerical_simulations_2006]
- [Nursal et al 2022][research_nursal_khalid_2022]
- [Nusca 1989][research_nusca_1989]
- [Nydick et al 1995][research_nydick_friedmann_1995]
- [O'Brien and Lewis 2000][research_obrien_lewis_2000]
- [O'Brien and Lewis 2001][research_obrien_lewis_2001]
- [O'Byrne et al 2005][research_obyrne_stotz_2005]
- [O'Byrne et al 2011][research_obyrne_wittig_2011]
- [O'Byrne et al 2014][research_obyrne_gai_2014]
- [O'Neal et al 2026][research_oneal_desilva_2026]
- [O'Neill and Lewis 1992][research_oneill_lewis_1992]
- [O'Neill and Lewis 1993][research_oneill_lewis_1993]
- [O'Rorke and Cuppoletti 2024][research_ororke_cuppoletti_2024]
- [Oamjee and Sadanandan 2020][research_oamjee_sadanandan_2020]
- [Oamjee and Sadanandan 2020][research_oamjee_sadanandan_2020_b]
- [Oba and Gonda 2014][research_oba_gonda_2014]
- [Obikane 1984][research_obikane_1984]
- [Obituary of Arthur Kantrowitz 2008][research_obituary_of_2008]
- [Oblique Shock and Expansion 2019][research_oblique_shock_2019]
- [Oblique Shock Wave Angle 2000][research_oblique_shock_2000]
- [Oblique Shock Wave Angle 2015][research_oblique_shock_2015]
- [Oblique Shock Waves 2013][research_oblique_shock_2013]
- [Oblique Shock Waves in 1983][research_oblique_shock_1983]
- [Oblique-Shock Chart 2017][research_oblique_shock_chart_2017]
- [Ocheltree 1993][research_ocheltree_1993]
- [Ochi 2004][research_ochi_2004]
- [Odabas and Sarigul-Klijn 1992][research_odabas_sarigulklijn_1992]
- [Ogawa and Babinsky 2008][research_ogawa_babinsky_2008]
- [Ogawa and Boyce 2013][research_ogawa_boyce_2013]
- [Ogawa et al 2009][research_ogawa_grainger_2009]
- [Ogawa et al 2010][research_ogawa_grainger_2010]
- [Ognjanovic et al 2017][research_ognjanovic_maksimovic_2017]
- [Oka et al 2015][research_oka_hidema_2015]
- [Okamoto et al 2002][research_okamoto_yamamoto_2002]
- [Okojie et al 2009][research_okojie_danehy_2009]
- [Okuno and Watanabe 1992][research_okuno_watanabe_1992]
- [Olfe 1964][research_olfe_1964]
- [Olguin 2019][research_olguin_2019]
- [Oliveira Júnior et al 2021][research_oliveirajunior_marinho_2021]
- [Olivier et al 1993][research_olivier_vetter_1993]
- [Olivon et al 2024][research_olivon_durand_2024]
- [Olivon et al 2026][research_olivon_genot_2026]
- [Olsen 1965][research_olsen_1965]
- [Ombrello et al 2015][research_ombrello_carter_2015]
- [On ascent guidance of 1994][research_on_ascent_1994]
- [Ootao and Ishihara 2012][research_ootao_ishihara_2012]
- [Ootao and Ishihara 2013][research_ootao_ishihara_2013]
- [Ootao and Tanigawa 2005][research_ootao_tanigawa_2005]
- [Opalka 1968][research_opalka_1968]
- [Oppenheimer and Doman][research_oppenheimer_doman]
- [Oppenheimer and Doman 2006][research_oppenheimer_doman_2006]
- [Oppenheimer et al 2007][research_oppenheimer_skujins_2007]
- [Oppenheimer et al 2008][research_oppenheimer_doman_2008]
- [Oppenheimer et al 2008][research_oppenheimer_skujins_2008]
- [Optimal Aerodynamic Shapes Of 1996][research_optimal_aerodynamic_1996]
- [Optimization design of dual 2023][research_optimization_design_2023]
- [Optimization of parameters of 2005][research_optimization_of_2005]
- [Orlik et al 2009][research_orlik_fedioun_2009]
- [Orlik et al 2011][research_orlik_fedioun_2011]
- [Orlin and Orlov 2019][research_orlin_orlov_2019]
- [Ormsbee 1962][research_ormsbee_1962]
- [Ortloff 1968][research_ortloff_1968]
- [Ortwerth and Goldman 1996][research_ortwerth_goldman_1996]
- [Osgerby et al 1969][research_osgerby_smithson_1969]
- [Osgerby et al 1969][research_osgerby_smithson_1969_b]
- [Ossmann et al 2019][research_ossmann_luspay_2019]
- [Oster 2010][research_oster_2010]
- [Oswald et al 1995][research_oswald_demargne_1995]
- [Otte et al 1963][research_otte_welch_1963]
- [Ou et al 2024][research_ou_xiong_2024]
- [Ou-zi and Jin-sheng 2011][research_ouzi_jinsheng_2011]
- [Ouzts 2008][research_ouzts_2008]
- [Ouzts et al 1992][research_ouzts_lorenzo_1992]
- [Ouzts, Peter J. et al 1993][research_ouztspeterj_lorenzocarlf_1993]
- [Oveissi et al 2024][research_oveissi_goel_2024]
- [Owen and Owen 2007][research_owen_owen_2007]
- [Owotunse et al 2023][research_owotunse_ogwumike_2023]
- [Ozawa et al 2008][research_ozawa_hanai_2008]
- [Ozawa et al 2014][research_ozawa_suzuki_2014]
- [Pace and Massa 2022][research_pace_massa_2022]
- [Padmapriya and Reddy 1998][research_padmapriya_reddy_1998]
- [Pagan et al 2001][research_pagan_benoit_2001]
- [Pagel and Warmbold 1968][research_pagel_warmbold_1968]
- [Pagel and Warmbold 1969][research_pagel_warmbold_1969]
- [Pal and Roy 2024][research_pal_roy_2024]
- [Palej and Palacz 2018][research_palej_palacz_2018]
- [Palmer][research_palmer]
- [Palmer 2020][research_palmer_2020]
- [Palmer and Venkatapathy 1993][research_palmer_venkatapathy_1993]
- [Palomero][research_palomero]
- [Palomino 2022][research_palomino_2022]
- [Palumbo et al 2022][research_palumbo_palmer_2022]
- [Pamadi et al 2004][research_pamadi_tartabini_2004]
- [Pamadi et al 2006][research_pamadi_hotchko_2006]
- [Pamadi et al 2009][research_pamadi_tartabini_2009]
- [Pan et al 2009][research_pan_tian_2009]
- [Pande 1994][research_pande_1994]
- [Pandey and Sivasakthivel 2011][research_pandey_sivasakthivel_2011]
- [Pandey and Sivasakthivel 2011][research_pandey_sivasakthivel_2011_b]
- [Pane][research_pane]
- [Panfilov et al 2021][research_panfilov_sevchenko_2021]
- [Papa and Stoliker 1988][research_papa_stoliker_1988]
- [Paper, board and pulps][research_paper_board]
- [Papinczak][research_papinczak]
- [Paquette and Palko 2004][research_paquette_palko_2004]
- [Paredes et al 2017][research_paredes_choudhari_2017]
- [Parise 1992][research_parise_1992]
- [Park 1996][research_park_1996]
- [Park and Busch 2017][research_park_busch_2017]
- [Park and Jeon 2024][research_park_jeon_2024]
- [Parker 2022][research_parker_2022]
- [Parmar et al 2026][research_parmar_jp_2026]
- [Parsons and Richmond 1969][research_parsons_richmond_1969]
- [Parsons et al 2023][research_parsons_armstrong_2023]
- [Parthasarathy et al 2014][research_parthasarathy_cinibulk_2014]
- [Parton 2018][research_parton_2018]
- [Pasha et al 2012][research_pasha_vadivelan_2012]
- [Pashai et al 2022][research_pashai_hurst_2022]
- [Patel and Chudoba 2026][research_patel_chudoba_2026]
- [Patra and Lee 2018][research_patra_lee_2018]
- [Paul et al 2014][research_paul_binner_2014]
- [Paull 1999][research_paull_1999]
- [Paull et al 1995][research_paull_stalker_1995]
- [Paus and Well 1996][research_paus_well_1996]
- [Pavlova et al 2011][research_pavlova_shtern_2011]
- [Pawlak 1994][research_pawlak_1994]
- [Payne and McConnell 2004][research_payne_mcconnell_2004]
- [Paynter 1994][research_paynter_1994]
- [Paynter and Chen 1983][research_paynter_chen_1983]
- [Peake][research_peake]
- [Pei and Hou 2014][research_pei_hou_2014]
- [Pein and Vinnemeier 1989][research_pein_vinnemeier_1989]
- [Pelevin and Ponomarev 2018][research_pelevin_ponomarev_2018]
- [Pelevin and Ponomarev 2021][research_pelevin_ponomarev_2021]
- [Pellett et al 2002][research_pellett_bruno_2002]
- [Pendergast and Mollendorf 2008][research_pendergast_mollendorf_2008]
- [Peng 2023][research_peng_2023]
- [Peng and Smith 1996][research_peng_smith_1996]
- [Peng and Zhong 2022][research_peng_zhong_2022]
- [Peng et al 2014][research_peng_peng_2014]
- [Peng et al 2019][research_peng_feng_2019]
- [Peng et al 2019][research_peng_qi_2019]
- [Peng et al 2024][research_peng_xu_2024]
- [Peng et al 2026][research_peng_chen_2026]
- [Penland and Romeo 1971][research_penland_romeo_1971]
- [Perchonok 1960][research_perchonok_1960]
- [Performance analysis of hydrocarbon-fueled 1999][research_performance_analysis_1999]
- [Peri et al 2024][research_peri_armani_2024]
- [Perlini et al 2026][research_perlini_bertolini_2026]
- [Perminov 1969][research_perminov_1969]
- [Perrier and Rostand 1994][research_perrier_rostand_1994]
- [Perrier et al 1995][research_perrier_rostand_1995]
- [Perrier et al 1996][research_perrier_rapuc_1996]
- [Perrot and Hadjadj 2005][research_perrot_hadjadj_2005]
- [Persh 1955][research_persh_1955]
- [Persova et al 2017][research_persova_soloveichik_2017]
- [Peters and Phares 1976][research_peters_phares_1976]
- [Petersen 1981][research_petersen_1981]
- [Peterson 2019][research_peterson_2019]
- [Peterson and Hassan 2017][research_peterson_hassan_2017]
- [Peterson and Hassan 2018][research_peterson_hassan_2018]
- [Petha Sethuraman et al 2020][research_pethasethuraman_kim_2020]
- [Petha Sethuraman et al 2023][research_pethasethuraman_yang_2023]
- [Petley and Dziedzic 1993][research_petley_dziedzic_1993]
- [Petley and Jones 1990][research_petley_jones_1990]
- [Petley and Jones 1992][research_petley_jones_1992]
- [Petrie 1965][research_petrie_1965]
- [Petrov et al 1998][research_petrov_clyndyuck_1998]
- [Pettinari et al 2012][research_pettinari_corradini_2012]
- [Pezzella et al 2014][research_pezzella_marini_2014]
- [Pfaff 1965][research_pfaff_1965]
- [Pfaff 1968][research_pfaff_1968]
- [Phillips and Cruz 1991][research_phillips_cruz_1991]
- [Phillips and Cruz 1993][research_phillips_cruz_1993]
- [Piao et al 2019][research_piao_zhang_2019]
- [Piccirillo et al 2023][research_piccirillo_viola_2023]
- [Pichler 2023][research_pichler_2023]
- [Piet-Lahanier and Serre 2017][research_pietlahanier_serre_2017]
- [Pike 2006][research_pike_2006]
- [Piller][research_piller]
- [Ping Li et al 2010][research_pingli_wanchunchen_2010]
- [Pinheiro Maia et al 2020][research_pinheiromaia_souza_2020]
- [Pinto et al 2023][research_pinto_whyman_2023]
- [Pionessa and Kinzel 2024][research_pionessa_kinzel_2024]
- [Pionessa and Kinzel 2024][research_pionessa_kinzel_2024_b]
- [Pipko 1966][research_pipko_1966]
- [Pisano and Whitfield 2024][research_pisano_whitfield_2024]
- [Piscitelli et al 2017][research_piscitelli_cutrone_2017]
- [Piscopo et al 2024][research_piscopo_depaepe_2024]
- [Pitman][research_pitman]
- [Platou 1959][research_platou_1959]
- [Platou 1968][research_platou_1968]
- [Platt and Hanner 1965][research_platt_hanner_1965]
- [Platz and Bounajem 1992][research_platz_bounajem_1992]
- [Poggie 2006][research_poggie_2006]
- [Poggie 2008][research_poggie_2008]
- [Polivanov et al 2010][research_polivanov_sidorenko_2010]
- [Polivanov et al 2016][research_polivanov_sidorenko_2016]
- [Pollock and Brutsche 2015][research_pollock_brutsche_2015]
- [Pollock and Wild 2024][research_pollock_wild_2024]
- [Pollock et al 2023][research_pollock_moran_2023]
- [Polsgrove and Adams 2002][research_polsgrove_adams_2002]
- [Polsgrove and Adams 2002][research_polsgrove_adams_2002_b]
- [Pope and Maydew 1959][research_pope_maydew_1959]
- [Popinski 2019][research_popinski_2019]
- [Poplavskaya 2002][research_poplavskaya_2002]
- [Porro and Hingst 1993][research_porro_hingst_1993]
- [Porter 1965][research_porter_1965]
- [Porter and Poggie 2017][research_porter_poggie_2017]
- [Portis et al 2024][research_portis_dambrosio_2024]
- [Potapkin and Moskvichev 2008][research_potapkin_moskvichev_2008]
- [Potturi and Edwards 2013][research_potturi_edwards_2013]
- [Poulain et al 2009][research_poulain_pietlahanie_2009]
- [Povinelli 1991][research_povinelli_1991]
- [Povitsky et al 2021][research_povitsky_miller_2021]
- [Powers 1960][research_powers_1960]
- [Powers and Robinson 1992][research_powers_robinson_1992]
- [Powers et al 1986][research_powers_zaretzky_1986]
- [Pozefsky 1989][research_pozefsky_1989]
- [Prabhu 1995][research_prabhu_1995]
- [Prabhu, D. K. and Tannehill, J. C. 1984][research_prabhudk_tannehilljc_1984]
- [Prakash and Singh 2021][research_prakash_singh_2021]
- [Prakash et al 2010][research_prakash_parsons_2010]
- [Prakash et al 2024][research_prakash_g_2024]
- [Pratt 1971][research_pratt_1971]
- [Pratt and Heiser 1993][research_pratt_heiser_1993]
- [Preliminary Design of the 1983][research_preliminary_design_1983]
- [Preliminary Thermal/Structural Analysis of 1992][research_preliminary_thermal_structural_1992]
- [Preller][research_preller]
- [Preller and Smart 2012][research_preller_smart_2012]
- [Pressures and Temperatures for 2000][research_pressures_and_2000]
- [Price][research_price]
- [Primary Flight Control Hydraulic][research_primary_flight]
- [Principles of Hypersonic Test 2002][research_principles_of_2002]
- [Priyamvada et al 2015][research_priyamvada_singh_2015]
- [Priyanka Agrawal et al 2026][research_priyankaagrawal_amitkumarsingh_2026]
- [Probstein 1953][research_probstein_1953]
- [Prokesch et al 2024][research_prokesch_duran_2024]
- [Properties of the U.S 2014][research_properties_of_2014]
- [Properties of the U.S 2024][research_properties_of_2024]
- [Pruett and Chang 1998][research_pruett_chang_1998]
- [Pruitt and Bates 1992][research_pruitt_bates_1992]
- [Pu et al 2017][research_pu_huang_2017]
- [Pulok and Chakravarty 2020][research_pulok_chakravarty_2020]
- [Pulsonetti][research_pulsonetti]
- [Qi and Jianliang 2017][research_qi_jianliang_2017]
- [Qi et al 1998][research_qi_wang_1998]
- [Qi et al 2015][research_qi_bao_2015]
- [Qian et al 2013][research_qian_sun_2013]
- [Qian et al 2016][research_qian_nan_2016]
- [Qiao et al 2024][research_qiao_liu_2024]
- [Qiao et al 2025][research_qiao_ma_2025]
- [Qiao Yongjie et al 2011][research_qiaoyongjie_liujinrong_2011]
- [Qifan et al 2014][research_qifan_huijun_2014]
- [Qin Changmao et al 2010][research_qinchangmao_qinaiming_2010]
- [Qin et al 2008][research_qin_bao_2008]
- [Qin et al 2012][research_qin_bao_2012]
- [Qin et al 2013][research_qin_zhang_2013]
- [Qin et al 2013][research_qin_zhu_2013]
- [Qin et al 2015][research_qin_chang_2015]
- [Qin et al 2019][research_qin_agarwal_2019]
- [Qin et al 2026][research_qin_huang_2026]
- [Qiu et al 2016][research_qiu_jia_2016]
- [Qiu et al 2017][research_qiu_zhang_2017]
- [Qiu et al 2021][research_qiu_zhang_2021]
- [Qu et al 2019][research_qu_kong_2019]
- [Quadros and Bernardini 2018][research_quadros_bernardini_2018]
- [Quan et al 2024][research_quan_chang_2024]
- [Quick et al 2005][research_quick_king_2005]
- [Quinlan][research_quinlan]
- [Quinlan, Jesse R. et al 2014][research_quinlanjesser_mcdanieljamesc_2014]
- [Quinn 1978][research_quinn_1978]
- [Quinn, Robert D. and Gong, Leslie 1990][research_quinnrobertd_gongleslie_1990]
- [R Wayne Guy 1990][research_rwayneguy_1990]
- [Rabadan and Weigand 2013][research_rabadan_weigand_2013]
- [Rabadan Santana and Weigand 2012][research_rabadansantana_weigand_2012]
- [Rabadanov and Ataev 2002][research_rabadanov_ataev_2002]
- [Radiation Properties of Hypersonic 2018][research_radiation_properties_2018]
- [Radiative Heat Transfer In 2018][research_radiative_heat_2018]
- [Radiatively driven hypersonic wind 1994][research_radiatively_driven_1994]
- [Rafla 2019][research_rafla_2019]
- [Rafla 2019][research_rafla_2019_b]
- [Raghunandan and Ruffin 2016][research_raghunandan_ruffin_2016]
- [Raghunathan and McAdam 1983][research_raghunathan_mcadam_1983]
- [Raghuram and Ramesh 2021][research_raghuram_ramesh_2021]
- [Ragnoli et al 2024][research_ragnoli_savino_2024]
- [Rahimi et al 2026][research_rahimi_svolos_2026]
- [Rahman et al 2017][research_rahman_joy_2017]
- [Raj 1987][research_raj_1987]
- [Rajamanohar and Kurian 1996][research_rajamanohar_kurian_1996]
- [Rajan 1970][research_rajan_1970]
- [Ram and Kim 2019][research_ram_kim_2019]
- [Ramakrishnan and Singh 1993][research_ramakrishnan_singh_1993]
- [Ramalingam et al 2003][research_ramalingam_mahefkey_2003]
- [Ramanujachari 2022][research_ramanujachari_2022]
- [Ramasubramanian et al 2008][research_ramasubramanian_starkey_2008]
- [Ramaswami et al 2019][research_ramaswami_velmurugan_2019]
- [Ramaty et al 1982][research_ramaty_spiegler_1982]
- [Ramjet supersonic "flight tests" 1958][research_ramjet_supersonic_1958]
- [Ramprakash and Muruganandam 2016][research_ramprakash_muruganandam_2016]
- [Ramunno et al 2021][research_ramunno_boyd_2021]
- [Ramunno et al 2022][research_ramunno_boyd_2022]
- [Rana et al 2011][research_rana_thornber_2011]
- [Rana et al 2013][research_rana_thornber_2013]
- [Ranard and Davison 1961][research_ranard_davison_1961]
- [Raney et al 1993][research_raney_mcminn_1993]
- [Rao 1974][research_rao_1974]
- [Rao et al 2023][research_rao_siddharth_2023]
- [Rasky, Daniel J. et al 1998][research_raskydanielj_tranhuyk_1998]
- [Rasmussen 1978][research_rasmussen_1978]
- [Rasmussen and Stevens 1987][research_rasmussen_stevens_1987]
- [Rasmussen et al 2005][research_rasmussen_driscoll_2005]
- [Rasmussen et al 2007][research_rasmussen_dhanuka_2007]
- [Rataczak et al 2023][research_rataczak_mcmahon_2023]
- [Rataczak et al 2024][research_rataczak_chaudhry_2024]
- [Ratchford et al 2025][research_ratchford_redding_2025]
- [Rathakrishnan 2025][research_rathakrishnan_2025]
- [Raubenheimer and Elgar 2012][research_raubenheimer_elgar_2012]
- [Rauh et al 2026][research_rauh_reimer_2026]
- [Rault 1992][research_rault_1992]
- [Rault 1992][research_rault_1992_b]
- [Ravichandran et al 2023][research_ravichandran_doherty_2023]
- [Ravichandran et al 2023][research_ravichandran_doherty_2023_b]
- [Ravindran et al 2019][research_ravindran_bricalli_2019]
- [Razzaqi and Smart 2009][research_razzaqi_smart_2009]
- [Reardon et al 2021][research_reardon_schetz_2021]
- [Reba 1964][research_reba_1964]
- [Reba and Christian 1963][research_reba_christian_1963]
- [Reda 1977][research_reda_1977]
- [Reddecliff and Weber 1998][research_reddecliff_weber_1998]
- [Reddy et al 1989][research_reddy_smith_1989]
- [Rediess and Melton 1994][research_rediess_melton_1994]
- [Reed 1997][research_reed_1997]
- [Reed 2013][research_reed_2013]
- [Regan 1964][research_regan_1964]
- [Reghu et al 2025][research_reghu_j_2025]
- [Rehman et al 2009][research_rehman_fidan_2009]
- [Rehman et al 2010][research_rehman_petersen_2010]
- [Reimer et al 2023][research_reimer_dimartino_2023]
- [Reimer et al 2025][research_reimer_dimartino_2025]
- [Reimer et al 2026][research_reimer_dimartino_2026]
- [Reklis and Conti 1984][research_reklis_conti_1984]
- [Relangi et al 2021][research_relangi_ingenito_2021]
- [Relangi et al 2023][research_relangi_ingenito_2023]
- [Rempt 1981][research_rempt_1981]
- [Ren 2009][research_ren_2009]
- [Ren and Yang 2017][research_ren_yang_2017]
- [Ren et al 2017][research_ren_fu_2017]
- [Ren et al 2023][research_ren_wu_2023]
- [Report No. 538, altitude-pressure 1935][research_report_no_1935]
- [Resch et al 1992][research_resch_hedlund_1992]
- [Research and Technology Organisation RTO 2005][research_researchandtechnologyorganisationrto_2005]
- [Research Instrumentation Requirements for 1974][research_research_instrumentation_1974]
- [Research Progress in Active 2026][research_research_progress_2026]
- [Reshotko 1987][research_reshotko_1987]
- [Response of Miniature Pressure 1974][research_response_of_1974]
- [Reubush 1999][research_reubush_1999]
- [Reubush et al 2001][research_reubush_martin_2001]
- [Review of Inlet/Airframe Integration 1986][research_review_of_1986]
- [Reviznikov et al 2018][research_reviznikov_sposobin_2018]
- [Reynolds 1977][research_reynolds_1977]
- [Rhea and Moore 1988][research_rhea_moore_1988]
- [Rhisat and Molki 2024][research_rhisat_molki_2024]
- [Rhudy et al 1960][research_rhudy_hiers_1960]
- [Riabov 1994][research_riabov_1994]
- [Riabov 2002][research_riabov_2002]
- [Riabov 2003][research_riabov_2003]
- [Riabov 2011][research_riabov_2011]
- [Riabov and Botin 1999][research_riabov_botin_1999]
- [Riabov and Riabov 1997][research_riabov_riabov_1997]
- [Ricciardi 1991][research_ricciardi_1991]
- [Ricciardi and Minwalla 2016][research_ricciardi_minwalla_2016]
- [Rice][research_rice]
- [Rice and Hazlwood 1994][research_rice_hazlwood_1994]
- [Rice and Heidelberg 1980][research_rice_heidelberg_1980]
- [Rice et al 2014][research_rice_goyne_2014]
- [Rich and Mellor 1995][research_rich_mellor_1995]
- [Richards 1979][research_richards_1979]
- [Richardson and Herrmann 1966][research_richardson_herrmann_1966]
- [Richey et al 1968][research_richey_stava_1968]
- [Richey et al 1983][research_richey_surber_1983]
- [Riedelbauch and Brenner 1990][research_riedelbauch_brenner_1990]
- [Riedelbauch et al 1989][research_riedelbauch_brenner_1989]
- [Rigamonti et al 2026][research_rigamonti_shoesmith_2026]
- [Rigamonti et al 2026][research_rigamonti_vicocantero_2026]
- [Riggins 2004][research_riggins_2004]
- [Riggins et al 1992][research_riggins_mcclinton_1992]
- [Riggins et al 2006][research_riggins_tackett_2006]
- [Righi 2015][research_righi_2015]
- [Riis et al 2024][research_riis_piscopo_2024]
- [Riley and Dejarnette 1992][research_riley_dejarnette_1992]
- [Riley et al 2015][research_riley_gaitonde_2015]
- [Riley et al 2016][research_riley_hagenmaier_2016]
- [Riley et al 2017][research_riley_hagenmaier_2017]
- [Risha 2000][research_risha_2000]
- [Rizk 1993][research_rizk_1993]
- [Rizvi et al 2017][research_rizvi_linshu_2017]
- [Rizzetta 1991][research_rizzetta_1991]
- [Rizzetta 1994][research_rizzetta_1994]
- [Rizzetta 1996][research_rizzetta_1996]
- [Rizzetta and Garmann 2022][research_rizzetta_garmann_2022]
- [Rizzetta and Garmann 2023][research_rizzetta_garmann_2023]
- [Rizzetta and Visbal † 2004][research_rizzetta_visbal_2004]
- [Roach et al 1996][research_roach_caldarella_1996]
- [Roberts 1988][research_roberts_1988]
- [Roberts 1988][research_roberts_1988_b]
- [Roberts and Brown 1988][research_roberts_brown_1988]
- [Roberts and Shawler 1994][research_roberts_shawler_1994]
- [Robertson and Hartfield 1992][research_robertson_hartfield_1992]
- [Robinson and McDougal 2000][research_robinson_mcdougal_2000]
- [Rocci Denis et al 2003][research_roccidenis_brandstetter_2003]
- [Rockwell et al 2010][research_rockwell_goyne_2010]
- [Rockwell et al 2023][research_rockwell_goyne_2023]
- [Rodi 2012][research_rodi_2012]
- [Rodi 2012][research_rodi_2012_b]
- [Rodi 2018][research_rodi_2018]
- [Rodi 2020][research_rodi_2020]
- [Rodighiero][research_rodighiero]
- [Rodriguez 2007][research_rodriguez_2007]
- [Rodriguez, C. G. et al 2000][research_rodriguezcg_rigginsdw_2000]
- [Rodriguez-Segade et al 2020][research_rodriguezsegade_hernandez_2020]
- [Rodríguez Fuentes and Parent 2022][research_rodriguezfuentes_parent_2022]
- [Roga 2019][research_roga_2019]
- [Roga 2019][research_roga_2019_b]
- [Roga 2023][research_roga_2023]
- [Rogers and Kaplan 1963][research_rogers_kaplan_1963]
- [Rogers, D. C. et al 1976][research_rogersdc_scottro_1976]
- [Rogers, R. Clayton et al 1998][research_rogersrclayton_capriottidiegop_1998]
- [Rogg et al 2020][research_rogg_bricalli_2020]
- [Rohl and Cowling 1965][research_rohl_cowling_1965]
- [Roland and Rumpfkeil 2017][research_roland_rumpfkeil_2017]
- [Rom 1965][research_rom_1965]
- [Rong 2017][research_rong_2017]
- [Rong et al 2016][research_rong_wei_2016]
- [Rooker 1970][research_rooker_1970]
- [Roos et al 2020][research_roos_pudsey_2020]
- [Rose and Teare 1964][research_rose_teare_1964]
- [Rose et al 2009][research_rose_thoma_2009]
- [Roseberry 2025][research_roseberry_2025]
- [Rosner and Cibrian 1974][research_rosner_cibrian_1974]
- [Ross 1960][research_ross_1960]
- [Ross et al 1993][research_ross_law_1993]
- [Rotating detonation combustion of 2023][research_rotating_detonation_2023]
- [Roth and Mavris 1999][research_roth_mavris_1999]
- [Rothschild and Schuster 1999][research_rothschild_schuster_1999]
- [Rotta 1966][research_rotta_1966]
- [Roudakov et al 1996][research_roudakov_semenov_1996]
- [Roudakov et al 1998][research_roudakov_semenov_1998]
- [Rouel and Richards 1975][research_rouel_richards_1975]
- [Rouel and Richards 1975][research_rouel_richards_1975_b]
- [Roundy 1979][research_roundy_1979]
- [Rowan][research_rowan]
- [Rowan and Paull 2005][research_rowan_paull_2005]
- [Rowan and Paull 2006][research_rowan_paull_2006]
- [Rowan Gollan][research_rowangollan]
- [Rowley and Thornton 1994][research_rowley_thornton_1994]
- [Roy 2008][research_roy_2008]
- [Roy et al 2011][research_roy_wang_2011]
- [Ruan][research_ruan]
- [Ruan et al 2020][research_ruan_domingo_2020]
- [Rubey 1985][research_rubey_1985]
- [Rubey 1985][research_rubey_1985_b]
- [Rubins and Rhode 1963][research_rubins_rhode_1963]
- [Ruble 1964][research_ruble_1964]
- [Rudiments and Methodology for 2001][research_rudiments_and_2001]
- [Rued et al 1991][research_rued_mark_1991]
- [Ruhnke et al 1965][research_ruhnke_will_1965]
- [Ruimin and Jianguo 2018][research_ruimin_jianguo_2018]
- [Ruoling et al 2012][research_ruoling_jin_2012]
- [Sabean and Lewis 1999][research_sabean_lewis_1999]
- [Sabelnikov and Vlasenko 2017][research_sabelnikov_vlasenko_2017]
- [Sabry and Hussin 2026][research_sabry_hussin_2026]
- [Sacher and Zellner 1995][research_sacher_zellner_1995]
- [Sachs et al 1991][research_sachs_bayer_1991]
- [Sachs et al 1995][research_sachs_schoder_1995]
- [Sachs et al 1996][research_sachs_heller_1996]
- [Sacks 1996][research_sacks_1996]
- [Saheby et al 2015][research_saheby_huang_2015]
- [Saheby et al 2017][research_saheby_huang_2017]
- [Sahu 1986][research_sahu_1986]
- [Sahu 2007][research_sahu_2007]
- [Sahu et al 2024][research_sahu_vasile_2024]
- [Sahut et al 2024][research_sahut_nilsson_2024]
- [Sai Naga Bharghava et al 2024][research_sainagabharghava_krishnatmali_2024]
- [Saida 1986][research_saida_1986]
- [Saito 1965][research_saito_1965]
- [Saito et al 2004][research_saito_ono_2004]
- [Saito et al 2005][research_saito_ono_2005]
- [Salloum et al 2018][research_salloum_candon_2018]
- [Salloum et al 2018][research_salloum_candon_2018_b]
- [Salooja 1968][research_salooja_1968]
- [Salvador et al 2009][research_salvador_myrabo_2009]
- [Salvador et al 2013][research_salvador_myrabo_2013]
- [Samimy et al 2011][research_samimy_webb_2011]
- [Samtaney and Pullin 1998][research_samtaney_pullin_1998]
- [San Martin et al 2025][research_sanmartin_plewacki_2025]
- [San Martin et al 2025][research_sanmartin_plewacki_2025_b]
- [Sanaka et al 2023][research_sanaka_kandula_2023]
- [Sandeep 2023][research_sandeep_2023]
- [Sanders, Bobby W. and Weir, Lois J. 1999][research_sandersbobbyw_weirloisj_1999]
- [Sanders, Bobby W. and Weir, Lois J. 2008][research_sandersbobbyw_weirloisj_2008]
- [Sanderson 1965][research_sanderson_1965]
- [Sanderson 1987][research_sanderson_1987]
- [Sanderson 2003][research_sanderson_2003]
- [Sanderson 2010][research_sanderson_2010]
- [Sandham 2026][research_sandham_2026]
- [Sandoz and Klaeyle 2021][research_sandoz_klaeyle_2021]
- [Sandoz et al 2024][research_sandoz_blanc_2024]
- [Sankar and Kelkar 1995][research_sankar_kelkar_1995]
- [Sankaran et al 2023][research_sankaran_venkatesh_2023]
- [Santhy et al 2022][research_santhy_sivakumar_2022]
- [Santos 2008][research_santos_2008]
- [Santos 2011][research_santos_2011]
- [Santos 2012][research_santos_2012]
- [Santos and Borges Ribeiro 2025][research_santos_borgesribeiro_2025]
- [Santos and Lewis 2003][research_santos_lewis_2003]
- [Santos et al 2020][research_santos_hosder_2020]
- [Sapunkov 1966][research_sapunkov_1966]
- [Saqib and Linshu 2007][research_saqib_linshu_2007]
- [Saranathan and Grant 2016][research_saranathan_grant_2016]
- [Sardeshmukh et al 2014][research_sardeshmukh_andersonlmatthewe_2014]
- [Sargent and Bielawski 1970][research_sargent_bielawski_1970]
- [Saric 2012][research_saric_2012]
- [Sarosh 2021][research_sarosh_2021]
- [Sarosh et al 2012][research_sarosh_yunfeng_2012]
- [Sarout and Paramasivam 2020][research_sarout_paramasivam_2020]
- [Sarout et al 2020][research_sarout_r_2020]
- [Sathiyamoorthy et al 2018][research_sathiyamoorthy_danish_2018]
- [Sato et al 1997][research_sato_izumikawa_1997]
- [Sato et al 2006][research_sato_matsuo_2006]
- [Sato et al 2019][research_sato_fukui_2019]
- [Savelkin et al 2015][research_savelkin_yarantsev_2015]
- [Savino and Pezzella 2003][research_savino_pezzella_2003]
- [Savino et al 2004][research_savino_fumo_2004]
- [Sawai et al 2003][research_sawai_sato_2003]
- [Sawley and Wüthrich 1995][research_sawley_wuthrich_1995]
- [Sayapin 1966][research_sayapin_1966]
- [Sayir 2006][research_sayir_2006]
- [Sayir and Sehirlioglu 2009][research_sayir_sehirlioglu_2009]
- [Scaggs 1966][research_scaggs_1966]
- [Scaggs et al 1963][research_scaggs_burggraf_1963]
- [Scaggs et al 1992][research_scaggs_neumann_1992]
- [Scala 1962][research_scala_1962]
- [Scala and Nolan 1960][research_scala_nolan_1960]
- [Schaber et al 1991][research_schaber_schwab_1991]
- [Schaupp and Friedrich 2010][research_schaupp_friedrich_2010]
- [Scherding][research_scherding]
- [Scherding et al 2024][research_scherding_rigas_2024]
- [Schettino and Borrelli 1998][research_schettino_borrelli_1998]
- [Schetz et al 1980][research_schetz_billig_1980]
- [Schetz et al 1982][research_schetz_billig_1982]
- [Schiavazzi and Juliano 2020][research_schiavazzi_juliano_2020]
- [Schindel 1989][research_schindel_1989]
- [Schindel 1991][research_schindel_1991]
- [Schindel 1999][research_schindel_1999]
- [Schindel 2005][research_schindel_2005]
- [Schioppa et al 2025][research_schioppa_taywochong_2025]
- [Schmatz 1989][research_schmatz_1989]
- [Schmidt 1988][research_schmidt_1988]
- [Schmidt and Plostins 1983][research_schmidt_plostins_1983]
- [Schmidt and Velapoldi 1999][research_schmidt_velapoldi_1999]
- [Schneider 2000][research_schneider_2000]
- [Schneider 2006][research_schneider_2006]
- [Schneider 2009][research_schneider_2009]
- [Schneider and Myers 1979][research_schneider_myers_1979]
- [Schneider and Reed 2003][research_schneider_reed_2003]
- [Schneider et al][research_schneider_gerlinger]
- [Schneider et al 2003][research_schneider_dreizler_2003]
- [Schneider et al 2003][research_schneider_matsumura_2003]
- [Schnelle et al 1992][research_schnelle_hoffels_1992]
- [Schoeler 1978][research_schoeler_1978]
- [Schram and Narayanaswamy 2026][research_schram_narayanaswamy_2026]
- [Schram et al 2025][research_schram_stramecky_2025]
- [Schuch and Laquer 1952][research_schuch_laquer_1952]
- [Schuelein 2014][research_schuelein_2014]
- [Schueler 1963][research_schueler_1963]
- [Schulmeister et al 1977][research_schulmeister_hostetler_1977]
- [Schulte-Roedding and Olivier 1998][research_schulteroedding_olivier_1998]
- [Schunk and Chung 2000][research_schunk_chung_2000]
- [Schwanekamp 2014][research_schwanekamp_2014]
- [Schwartzentruber and Boyd 2013][research_schwartzentruber_boyd_2013]
- [Schwartzentruber et al 2012][research_schwartzentruber_tadmor_2012]
- [Schweikhard 1983][research_schweikhard_1983]
- [Schwelkart and Hallion 1997][research_schwelkart_hallion_1997]
- [Science Communication Inc Mclean Va 1960][research_sciencecommunicationincmcleanva_1960]
- [Scigliano et al 2020][research_scigliano_desimone_2020]
- [Scott 1968][research_scott_1968]
- [Scotti et al 1988][research_scotti_martin_1988]
- [Scramjet Combustion 2022][research_scramjet_combustion_2022]
- [Scramjet Combustor 2022][research_scramjet_combustor_2022]
- [Scramjet Engine Research athe 2001][research_scramjet_engine_2001]
- [Scramjet Inlet/Forebody and Isolator 2022][research_scramjet_inlet_forebody_2022]
- [Scribben and Withrow 2006][research_scribben_withrow_2006]
- [Scuderi 1978][research_scuderi_1978]
- [Scuderi et al 1998][research_scuderi_orton_1998]
- [Seabergh et al 2001][research_seabergh_king_2001]
- [Seal between two elements 2011][research_seal_between_2011]
- [Seal for high-temperature applications 2019][research_seal_for_2019]
- [Seckin and Yuceil 2013][research_seckin_yuceil_2013]
- [Sedlock 1985][research_sedlock_1985]
- [Seebaugh, W. R. 1973][research_seebaughwr_1973]
- [Segal 2009][research_segal_2009]
- [Segal 2010][research_segal_2010]
- [Segal 2010][research_segal_2010_b]
- [Segal 2011][research_segal_2011]
- [Segal and Thakur 2005][research_segal_thakur_2005]
- [Segal et al 1997][research_segal_owens_1997]
- [Segura 2007][research_segura_2007]
- [Sekar and Vaidyanathan 2025][research_sekar_vaidyanathan_2025]
- [Self-starting Simulation of a 2020][research_self_starting_simulation_2020]
- [Sellers and Hunerwadel 1977][research_sellers_hunerwadel_1977]
- [Semenov et al 1998][research_semenov_romankov_1998]
- [Sepahi-Younsi 2025][research_sepahiyounsi_2025]
- [Sepahi-Younsi and Esmaeili 2023][research_sepahiyounsi_esmaeili_2023]
- [Serrani and Bolender 2014][research_serrani_bolender_2014]
- [Serre 2009][research_serre_2009]
- [Serre and Falempin 2001][research_serre_falempin_2001]
- [Serre and Falempin 2008][research_serre_falempin_2008]
- [Serre et al 2011][research_serre_denis_2011]
- [Seshadri 1990][research_seshadri_1990]
- [Seshadri 2008][research_seshadri_2008]
- [Sethi 2025][research_sethi_2025]
- [Settles and Dodson 1994][research_settles_dodson_1994]
- [Sevigny et al 1972][research_sevigny_heckman_1972]
- [Seymour 2009][research_seymour_2009]
- [Sforza 1967][research_sforza_1967]
- [Sforza 2017][research_sforza_2017]
- [Sforza 2017][research_sforza_2017_b]
- [Sforza 2017][research_sforza_2017_c]
- [Sforza 2017][research_sforza_2017_d]
- [Shachar et al 2025][research_shachar_benasher_2025]
- [Shahrokhi and Davis, Jr 1995][research_shahrokhi_davisjr_1995]
- [Shaikh et al 2017][research_shaikh_patidar_2017]
- [Shajahan et al 2025][research_shajahan_gugulothu_2025]
- [Shakiba and Serrani 2011][research_shakiba_serrani_2011]
- [Shang][research_shang]
- [Shang 2005][research_shang_2005]
- [Shang 2008][research_shang_2008]
- [Shang 2008][research_shang_2008_b]
- [Shang 2009][research_shang_2009_b]
- [Shang and Chang 2007][research_shang_chang_2007]
- [Shang and Surzhikov 2011][research_shang_surzhikov_2011]
- [Shang et al 1976][research_shang_hankeyjr_1976]
- [Shang et al 2006][research_shang_menart_2006]
- [Shang et al 2007][research_shang_chang_2007_b]
- [Shang* 2009][research_shang_2009]
- [Shanmugam and Sun Park 2024][research_shanmugam_sunpark_2024]
- [Shantz 1953][research_shantz_1953]
- [Shaohua and Xu 2017][research_shaohua_xu_2017]
- [Sharma and Shenvi 2025][research_sharma_shenvi_2025]
- [Sharma and Shenvi 2026][research_sharma_shenvi_2026]
- [Sharma et al 2020][research_sharma_ghia_2020]
- [Sharma et al 2022][research_sharma_eswaran_2022]
- [Sharov M. K. 2022][research_sharovmk_2022]
- [Sheffer and Dulikravich 1993][research_sheffer_dulikravich_1993]
- [Shen et al 2014][research_shen_yu_2014]
- [Shen et al 2020][research_shen_huang_2020]
- [Shen et al 2021][research_shen_huang_2021]
- [Shen et al 2025][research_shen_dongliang_2025]
- [Sheng et al 2021][research_sheng_lu_2021]
- [Shepard et al 2021][research_shepard_feleo_2021]
- [Shepheard 1965][research_shepheard_1965]
- [Sheth et al 2012][research_sheth_ungar_2012]
- [Shetty et al 2025][research_shetty_cardenas_2025]
- [Shevelev 2018][research_shevelev_2018]
- [Shi 2016][research_shi_2016]
- [Shi et al 1994][research_shi_tsai_1994]
- [Shi et al 2010][research_shi_chang_2010]
- [Shi et al 2012][research_shi_zhou_2012]
- [Shi et al 2015][research_shi_dai_2015]
- [Shi et al 2017][research_shi_song_2017]
- [Shi et al 2017][research_shi_song_2017_b]
- [Shi et al 2020][research_shi_feng_2020]
- [Shi et al 2021][research_shi_zha_2021]
- [Shi et al 2023][research_shi_niu_2023]
- [Shields 1981][research_shields_1981]
- [Shih et al 1988][research_shih_zwan_1988]
- [Shikman et al 2001][research_shikman_vinogradov_2001]
- [Shilnikov and Elizarova 2018][research_shilnikov_elizarova_2018]
- [Shimura et al 1996][research_shimura_sakuranaka_1996]
- [Shinde and Gaitonde 2022][research_shinde_gaitonde_2022]
- [Shirai et al 2014][research_shirai_hashimoto_2014]
- [Shirasu et al 1996][research_shirasu_south_1996]
- [Shklovskii and Kurt 1961][research_shklovskii_kurt_1961]
- [Shneider and Macheret 2004][research_shneider_macheret_2004]
- [Shock tunnel and numerical 2012][research_shock_tunnel_2012]
- [Shock Wave-Boundary Layer Interactions][research_shock_wave_boundary]
- [Shock Waves in Bubbly][research_shock_waves]
- [Shope 1975][research_shope_1975]
- [Shope 2006][research_shope_2006]
- [Shorenstein 1971][research_shorenstein_1971]
- [Short 1961][research_short_1961]
- [Shou and Li 2026][research_shou_li_2026]
- [Shovlin 1978][research_shovlin_1978]
- [Shreeve et al 1961][research_shreeve_lord_1961]
- [Shuai et al 2022][research_shuai_daqian_2022]
- [Shubhankar Bhakta et al., 2018][research_shubhankarbhaktaetal_2018]
- [Shucheng and Xijun 1994][research_shucheng_xijun_1994]
- [Shuguang et al 2015][research_shuguang_yangwang_2015]
- [Shumway 2000][research_shumway_2000]
- [Shuping Tan and Zhibin Li 2010][research_shupingtan_zhibinli_2010]
- [Shvets et al 2005][research_shvets_voronin_2005]
- [Shvydkyi 2023][research_shvydkyi_2023]
- [Si et al 2019][research_si_huang_2019]
- [Siaka and Zhang 2022][research_siaka_zhang_2022]
- [Sicard et al 2006][research_sicard_raepsaet_2006]
- [Sicard et al 2008][research_sicard_grill_2008]
- [Siddiqi and Abraham 1988][research_siddiqi_abraham_1988]
- [Sidharth and Dwivedi 2026][research_sidharth_dwivedi_2026]
- [Sidharth and Dwivedi 2026][research_sidharth_dwivedi_2026_b]
- [Siebenhaar and Bogar 2006][research_siebenhaar_bogar_2006]
- [Siebenhaar et al 1999][research_siebenhaar_chen_1999]
- [Silva Marques Soares et al 2021][research_silvamarquessoares_paulobatistadearaujo_2021]
- [Silver et al 2024][research_silver_brooks_2024]
- [Silvester and Morgan 2004][research_silvester_morgan_2004]
- [Simeonides][research_simeonides]
- [Simmons 1989][research_simmons_1989]
- [Simmons 2000][research_simmons_2000]
- [Simmons and Meritt 2022][research_simmons_meritt_2022]
- [Simmons et al 1989][research_simmons_nelson_1989]
- [Simmons et al 1992][research_simmons_nelson_1992]
- [Simmons et al 1995][research_simmons_nelson_1995]
- [Simon and Savage 1975][research_simon_savage_1975]
- [Simone and Bruno 2009][research_simone_bruno_2009]
- [Simone and Bruno 2010][research_simone_bruno_2010]
- [Simons 1975][research_simons_1975]
- [Sims 1963][research_sims_1963]
- [Sims and Hahn 1964][research_sims_hahn_1964]
- [Simsont et al 2012][research_simsont_gerlinger_2012]
- [Simulation in support of 1988][research_simulation_in_1988]
- [Singer 1956][research_singer_1956]
- [Singh and Gahlot 2023][research_singh_gahlot_2023]
- [Singh and Rajagopal 2026][research_singh_rajagopal_2026]
- [Singh et al 1989][research_singh_tiwari_1989]
- [Singh et al 1990][research_singh_tiwari_1990]
- [Singh et al 2018][research_singh_babu_2018]
- [Singh et al 2023][research_singh_g_2023]
- [Singh et al 2023][research_singh_prakash_2023]
- [Singh et al 2025][research_singh_sharma_2025]
- [Sippel 2006][research_sippel_2006]
- [Siqueira et al 2019][research_siqueira_rosa_2019]
- [Sislian et al 2000][research_sislian_dudebout_2000]
- [Sitaraman et al 2021][research_sitaraman_yellapantula_2021]
- [Situ et al 1999][research_situ_sun_1999]
- [Situ et al 2001][research_situ_wang_2001]
- [Situ et al 2002][research_situ_wang_2002]
- [Sivells 1963][research_sivells_1963]
- [Sivells 1969][research_sivells_1969]
- [Sivells and Payne 1959][research_sivells_payne_1959]
- [Skews 1994][research_skews_1994]
- [Skinner and Johnston 1953][research_skinner_johnston_1953]
- [Skujins and Cesnik 2010][research_skujins_cesnik_2010]
- [Skujins and Cesnik 2011][research_skujins_cesnik_2011]
- [Slater 2016][research_slater_2016]
- [Slater and Saunders 2009][research_slater_saunders_2009]
- [Slater, John W. and Gruber, Christopher R. 2005][research_slaterjohnw_gruberchristopherr_2005]
- [Slavick and Hiremath 2023][research_slavick_hiremath_2023]
- [Sliusariev and Bilotserkovsky 2024][research_sliusariev_bilotserkovsky_2024]
- [Slutsky et al 1969][research_slutsky_williams_1969]
- [Smaardyk 1954][research_smaardyk_1954]
- [Smalley et al 1977][research_smalley_wharton_1977]
- [Smarslok 2015][research_smarslok_2015]
- [Smart 1999][research_smart_1999]
- [Smart and Kalkhoran 1995][research_smart_kalkhoran_1995]
- [Smart and Kalkhoran 1995][research_smart_kalkhoran_1995_b]
- [Smart and Tetlow 2006][research_smart_tetlow_2006]
- [Smart et al 1998][research_smart_kalkhoran_1998]
- [Smart et al 2006][research_smart_hass_2006]
- [Smayda][research_smayda]
- [Smayda and Goyne 2011][research_smayda_goyne_2011]
- [Smeets and Quenett 1997][research_smeets_quenett_1997]
- [Smeltzer and Sorensen 1972][research_smeltzer_sorensen_1972]
- [Smiley and Camberos 2024][research_smiley_camberos_2024]
- [Smirnov 2019][research_smirnov_2019]
- [Smith 1953][research_smith_1953]
- [Smith 2011][research_smith_2011]
- [Smith 2021][research_smith_2021]
- [Smith and Baxter][research_smith_baxter]
- [Smith and Carver 1993][research_smith_carver_1993]
- [Smith and Chase 1976][research_smith_chase_1976]
- [Smith and Farokhi 2015][research_smith_farokhi_2015]
- [Smith and Farokhi 2015][research_smith_farokhi_2015_b]
- [Smith and Farokhi 2015][research_smith_farokhi_2015_c]
- [Smith and Farokhi 2018][research_smith_farokhi_2018]
- [Smith and Finlayson 1978][research_smith_finlayson_1978]
- [Smith and Good 1979][research_smith_good_1979]
- [Smith and Pellicano 1992][research_smith_pellicano_1992]
- [Smith et al 2004][research_smith_bergmann_2004]
- [Smith et al 2007][research_smith_scribben_2007]
- [Smith et al 2011][research_smith_bowcutt_2011]
- [Smith-Kent et al 1993][research_smithkent_ridder_1993]
- [Smits 1986][research_smits_1986]
- [Smits 1988][research_smits_1988]
- [Snyder 2003][research_snyder_2003]
- [Snyder et al 1999][research_snyder_vilendrer_1999]
- [Sobel and Nawaz 1972][research_sobel_nawaz_1972]
- [Sobieczky 1991][research_sobieczky_1991]
- [Sobieczky 2026][research_sobieczky_2026]
- [Solomonov et al 2010][research_solomonov_milekhin_2010]
- [Soltani et al 2011][research_soltani_farahani_2011]
- [Son et al 2022][research_son_son_2022]
- [Son et al 2024][research_son_ko_2024]
- [Son et al 2024][research_son_ko_2024_b]
- [Song and Choi 2020][research_song_choi_2020]
- [Song et al 2006][research_song_choi_2006]
- [Song et al 2019][research_song_wang_2019]
- [Song et al 2023][research_song_qin_2023]
- [Song et al 2026][research_song_cai_2026]
- [Song et al 2026][research_song_zhang_2026]
- [Soni and De 2017][research_soni_de_2017]
- [Sorensen and Bencze 1973][research_sorensen_bencze_1973]
- [Southwest Research Inst San Antonio Tx 1963][research_southwestresearchinstsanantoniotx_1963]
- [Space environment natural and][research_space_environment]
- [Space systems. Launch-vehicle-to-spacecraft flight][research_space_systems]
- [Spearman 2003][research_spearman_2003]
- [Specific Impulse][research_specific_impulse]
- [Specific Impulse 2008][research_specific_impulse_2008]
- [Specific Impulse 2015][research_specific_impulse_2015]
- [Specker and Brinkley 1983][research_specker_brinkley_1983]
- [Spedding et al 1960][research_spedding_hanak_1960]
- [Speer et al 1982][research_speer_aubrey_1982]
- [Spekreijse 1991][research_spekreijse_1991]
- [Speyer et al 1980][research_speyer_dannemiller_1980]
- [Sprangle and Johnson 2015][research_sprangle_johnson_2015]
- [Spravka and Jorris 2015][research_spravka_jorris_2015]
- [Spravka and Jorris 2015][research_spravka_jorris_2015_b]
- [Spring 1972][research_spring_1972]
- [Squire et al 1999][research_squire_diaz_1999]
- [Sridharan and Rodriguez 2013][research_sridharan_rodriguez_2013]
- [Srikant et al 2010][research_srikant_wagner_2010]
- [Srinivas 1992][research_srinivas_1992]
- [Srinivasan and Newman 2013][research_srinivasan_newman_2013]
- [Srivastava 1994][research_srivastava_1994]
- [Srivastava 1994][research_srivastava_1994_b]
- [Staack and De 2000][research_staack_de_2000]
- [Stabe et al 1984][research_stabe_whitney_1984]
- [Stalker 1989][research_stalker_1989]
- [Stalker 1992][research_stalker_1992]
- [Stalker and Morgan 1984][research_stalker_morgan_1984]
- [Stalker et al 1988][research_stalker_morgan_1988]
- [Stalker et al 1994][research_stalker_simmons_1994]
- [Stallings and Hartman 1981][research_stallings_hartman_1981]
- [Standard Atmosphere][research_standard_atmosphere]
- [Standard Atmosphere 1997][research_standard_atmosphere_1997]
- [Standard Atmosphere 2005][research_standard_atmosphere_2005]
- [Standard atmosphere 2007][research_standard_atmosphere_2007]
- [standard atmosphere 2014][research_standard_atmosphere_2014]
- [Standard Atmosphere 2023][research_standard_atmosphere_2023]
- [Standard Atmosphere 2024][research_standard_atmosphere_2024]
- [Standard atmosphere chart 1927][research_standard_atmosphere_1927]
- [Standard atmosphere chart supersedes 1927][research_standard_atmosphere_1927_b]
- [Standard Atmosphere Data 1992][research_standard_atmosphere_1992]
- [standard atmosphere for preconditioning 2021][research_standard_atmosphere_2021]
- [standard atmosphere for testing 2021][research_standard_atmosphere_2021_b]
- [Standard Atmospheric Profilesa aSource 2002][research_standard_atmospheric_2002]
- [Stanley, Thomas Troy et al 2000][research_stanleythomastroy_alexanderreginald_2000]
- [Starikovskiy et al 2024][research_starikovskiy_ju_2024]
- [Starkey 2009][research_starkey_2009]
- [Starkey 2014][research_starkey_2014]
- [Starkey and Lewis 1999][research_starkey_lewis_1999]
- [Starkey and Lewis 1999][research_starkey_lewis_1999_b]
- [Starkey and Lewis 2000][research_starkey_lewis_2000]
- [Starkey and Lewis 2003][research_starkey_lewis_2003]
- [Starkey et al 2005][research_starkey_rankins_2005]
- [Starkey et al 2006][research_starkey_rankins_2006]
- [Starkey et al 2014][research_starkey_cannella_2014]
- [Static and dynamic flow 2005][research_static_and_2005]
- [Stebbins and Loth 2024][research_stebbins_loth_2024]
- [Stecklein et al 1993][research_stecklein_hasen_1993]
- [Steelant and van Duijn 2011][research_steelant_vanduijn_2011]
- [Stefaniya et al 2025][research_stefaniya_pushpalatha_2025]
- [Steinetz, Bruce M. 1992][research_steinetzbrucem_1992]
- [Steinetz, Bruce M. et al 1992][research_steinetzbrucem_mutharasanrajakkannu_1992]
- [Stemmer and Adams][research_stemmer_adams]
- [Stenberg 1983][research_stenberg_1983]
- [Stenzel and Urrutia 2014][research_stenzel_urrutia_2014]
- [Stern 1983][research_stern_1983]
- [Sternberg 1964][research_sternberg_1964]
- [Sternberg 2010][research_sternberg_2010]
- [Sterne 1958][research_sterne_1958]
- [Sterne 1958][research_sterne_1958_b]
- [Stetson 1990][research_stetson_1990]
- [Stetson and Sawyer 1977][research_stetson_sawyer_1977]
- [Steva][research_steva]
- [Stevens 2014][research_stevens_2014]
- [Stewart 1981][research_stewart_1981]
- [Stewart and Quigg 1963][research_stewart_quigg_1963]
- [Stewart et al 1992][research_stewart_smith_1992]
- [Stickels 1986][research_stickels_1986]
- [Stilp][research_stilp]
- [Stokes and Acharya 2023][research_stokes_acharya_2023]
- [Stokes and Lombaerts 2023][research_stokes_lombaerts_2023]
- [Stokes et al 2023][research_stokes_acharya_2023_b]
- [Stoll 1961][research_stoll_1961]
- [Stoll et al 1975][research_stoll_munroe_1975]
- [Stollery 1990][research_stollery_1990]
- [Stoloff and Jone 1997][research_stoloff_jone_1997]
- [Stone 1945][research_stone_1945]
- [Stone 2024][research_stone_2024]
- [Stoukov et al 1997][research_stoukov_gorokhovski_1997]
- [Strand and Ennis 2012][research_strand_ennis_2012]
- [Strauss et al 2025][research_strauss_manassis_2025]
- [Strauss et al 2026][research_strauss_fischer_2026]
- [Streby et al 1999][research_streby_mathur_1999]
- [Street][research_street]
- [Streiff 1953][research_streiff_1953]
- [Striebich et al 2008][research_striebich_shafer_2008]
- [Strock 1983][research_strock_1983]
- [Strome 1969][research_strome_1969]
- [Stroud, C. W. and Rummler, D. R. 1980][research_stroudcw_rummlerdr_1980]
- [Strutjet Rocket-Based Combined-Cycle Engine 2001][research_strutjet_rocket_based_2001]
- [Stuckey and Lewis 1999][research_stuckey_lewis_1999]
- [Study on Self-compensation Design 2021][research_study_on_2021]
- [Sturek and Schiff 1981][research_sturek_schiff_1981]
- [Su and Liu 2021][research_su_liu_2021]
- [Su et al 2018][research_su_chen_2018]
- [Su et al 2024][research_su_zhao_2024]
- [Subbiah and Stefaniya 2025][research_subbiah_stefaniya_2025]
- [Subramanian et al 2025][research_subramanian_thangadurai_2025]
- [Subrata 2007][research_subrata_2007]
- [Subsonic and Supersonic Jets 1975][research_subsonic_and_1975]
- [Suchomel et al 2006][research_suchomel_vanwie_2006]
- [Sudalagunta et al 2018][research_sudalagunta_sultan_2018]
- [Suetin and Kartsev 1993][research_suetin_kartsev_1993]
- [Sugarno et al 2022][research_sugarno_sriram_2022]
- [Sullins 1993][research_sullins_1993]
- [Sullins and Billig 1987][research_sullins_billig_1987]
- [Sullins et al 1991][research_sullins_carpenter_1991]
- [Sullivan and Gaitonde 2022][research_sullivan_gaitonde_2022]
- [Sultanov and Glebov 2021][research_sultanov_glebov_2021]
- [Summerfield 1992][research_summerfield_1992]
- [Summors][research_summors]
- [Sun 2008][research_sun_2008]
- [Sun and Xin 2014][research_sun_xin_2014]
- [Sun and Zhang 2011][research_sun_zhang_2011]
- [Sun and Zhang 2016][research_sun_zhang_2016]
- [Sun and Zhu 2019][research_sun_zhu_2019]
- [Sun et al 2005][research_sun_fang_2005]
- [Sun et al 2008][research_sun_geng_2008]
- [Sun et al 2009][research_sun_zhang_2009]
- [Sun et al 2013][research_sun_li_2013]
- [Sun et al 2016][research_sun_zhong_2016]
- [Sun et al 2017][research_sun_wang_2017]
- [Sun et al 2019][research_sun_li_2019]
- [Sun et al 2020][research_sun_wang_2020]
- [Sun et al 2020][research_sun_wang_2020_b]
- [Sun et al 2020][research_sun_wang_2020_c]
- [Sun et al 2020][research_sun_wang_2020_d]
- [Sun et al 2020][research_sun_wang_2020_e]
- [Sun et al 2020][research_sun_yang_2020]
- [Sun et al 2021][research_sun_li_2021]
- [Sun et al 2023][research_sun_wu_2023]
- [Sun et al 2023][research_sun_zhu_2023]
- [Sun et al 2024][research_sun_ma_2024]
- [Sun et al 2025][research_sun_li_2025]
- [Sun et al 2025][research_sun_ran_2025]
- [Sun et al 2026][research_sun_li_2026]
- [Sun et al 2026][research_sun_li_2026_b]
- [sun et al 2026][research_sun_yu_2026]
- [Sun Jian and Liu Wei-Qiang 2014][research_sunjian_liuweiqiang_2014]
- [Sundén and Fu 2017][research_sunden_fu_2017]
- [Suneetha et al 2019][research_suneetha_randive_2019]
- [Sung et al 2001][research_sung_hsieh_2001]
- [Sung et al 2001][research_sung_hsieh_2001_b]
- [Sung et al 2025][research_sung_jo_2025]
- [Sung et al 2026][research_sung_jo_2026]
- [Supersonic Combustion Flowfield Studies 1977][research_supersonic_combustion_1977]
- [Supersonic Combustion Processes 2009][research_supersonic_combustion_2009]
- [Supersonic jet excitation using 1994][research_supersonic_jet_1994]
- [Suppe 2000][research_suppe_2000]
- [Surber 1975][research_surber_1975]
- [Surber and Robinson 1983][research_surber_robinson_1983]
- [Surber and Sedlock 1978][research_surber_sedlock_1978]
- [Surget and Dunet 1993][research_surget_dunet_1993]
- [Surzhikov 2009][research_surzhikov_2009]
- [Surzhikov 2013][research_surzhikov_2013]
- [Surzhikov 2021][research_surzhikov_2021]
- [Surzhikov 2021][research_surzhikov_2021_b]
- [Surzhikov and Surzhikov 1997][research_surzhikov_surzhikov_1997]
- [Surzhikov et al 2013][research_surzhikov_shang_2013]
- [Sushma et al 2025][research_sushma_rani_2025]
- [Sutliff 1973][research_sutliff_1973]
- [Sutton et al 1995][research_sutton_troiler_1995]
- [Sutton et al 1997][research_sutton_chao_1997]
- [Suzuki 2016][research_suzuki_2016]
- [Suzuki and Watanabe 2013][research_suzuki_watanabe_2013]
- [Svec 1981][research_svec_1981]
- [Svendsen 1994][research_svendsen_1994]
- [Swain et al 2020][research_swain_p_2020]
- [Swann et al 1981][research_swann_duke_1981]
- [Swanson et al 2007][research_swanson_caghlan_2007]
- [Swigart 1962][research_swigart_1962]
- [Swigart 1963][research_swigart_1963]
- [Swithebank and Chigier 1969][research_swithebank_chigier_1969]
- [Swithenbank and Jaques 1970][research_swithenbank_jaques_1970]
- [Swithenbank et al 1992][research_swithenbank_ewan_1992]
- [Syberg et al 1980][research_syberg_koncsek_1980]
- [Sykes][research_sykes]
- [Sylvester 1967][research_sylvester_1967]
- [System for Evaluation of 1974][research_system_for_1974]
- [Szema et al 2010][research_szema_liu_2010]
- [Szwaba and Doerffer 2017][research_szwaba_doerffer_2017]
- [T Sailor Koeplinger et al][research_tsailorkoeplinger_calebhash]
- [Tabanli and Yuceil 2018][research_tabanli_yuceil_2018]
- [Tachinina et al 2018][research_tachinina_lysenko_2018]
- [Taghi-Abad et al 2026][research_taghiabad_esfandabadi_2026]
- [Taguchi and Kashitani 2025][research_taguchi_kashitani_2025]
- [Taguchi et al 2009][research_taguchi_harada_2009]
- [Taguchi et al 2014][research_taguchi_harada_2014]
- [Taha et al 2001][research_taha_tiwari_2001]
- [Taheri 2020][research_taheri_2020]
- [Tahir 2021][research_tahir_2021]
- [Tahir et al][research_tahir_timofeev]
- [Takagi et al 2014][research_takagi_morozumi_2014]
- [Takahashi 2005][research_takahashi_2005]
- [Takahashi 2012][research_takahashi_2012]
- [Takahashi et al 1998][research_takahashi_wakai_1998]
- [Takahashi et al 2005][research_takahashi_sunami_2005]
- [Takahashi et al 2007][research_takahashi_komuro_2007]
- [Takahashi et al 2013][research_takahashi_yamada_2013]
- [Takahashi et al 2020][research_takahashi_kodera_2020]
- [Takahashi et al 2023][research_takahashi_oki_2023]
- [Takahashi et al 2025][research_takahashi_hirotani_2025]
- [Takama 2011][research_takama_2011]
- [Takasaki et al 1998][research_takasaki_fujimoto_1998]
- [Takashima and Lewis 1995][research_takashima_lewis_1995]
- [Takashima and Lewis 1996][research_takashima_lewis_1996_b]
- [Takashima and Lewis 1999][research_takashima_lewis_1999]
- [Takashima et al 1996][research_takashima_lewis_1996]
- [Takashima, N. and Kothari, A. P. 1998][research_takashiman_kothariap_1998]
- [Takegoshi et al 2012][research_takegoshi_tomioka_2012]
- [Talantov 1959][research_talantov_1959]
- [Talmage 2008][research_talmage_2008]
- [Tam and Li 1989][research_tam_li_1989]
- [Tam et al 2005][research_tam_eklund_2005]
- [Tam et al 2006][research_tam_lin_2006]
- [Tam et al 2007][research_tam_hsu_2007]
- [Tam et al 2008][research_tam_eklund_2008]
- [Tam et al 2008][research_tam_hsu_2008]
- [Tam et al 2011][research_tam_hsu_2011]
- [Tam et al 2012][research_tam_hsu_2012]
- [Tan and Bogdonoff 1985][research_tan_bogdonoff_1985]
- [Tan and Wang 2015][research_tan_wang_2015]
- [Tan et al 2009][research_tan_sun_2009]
- [Tan et al 2011][research_tan_li_2011]
- [Tanatsugu and Carrick 2003][research_tanatsugu_carrick_2003]
- [Tandon et al 2006][research_tandon_dumm_2006]
- [Tang et al 1991][research_tang_zhou_1991]
- [Tang et al 2005][research_tang_zheng_2005]
- [Tang et al 2018][research_tang_long_2018]
- [Tang et al 2020][research_tang_zhai_2020]
- [Tang et al 2021][research_tang_gao_2021]
- [Tang et al 2023][research_tang_hu_2023]
- [Tang et al 2023][research_tang_xiong_2023]
- [Tang et al 2024][research_tang_xiong_2024]
- [Tang et al 2025][research_tang_cai_2025]
- [Tang et al 2025][research_tang_cai_2025_b]
- [Tang et al 2025][research_tang_li_2025]
- [Tang et al 2025][research_tang_zhang_2025]
- [Tang et al 2026][research_tang_fan_2026]
- [Tani et al 2000][research_tani_kanda_2000]
- [Tanigawa 1999][research_tanigawa_1999]
- [Tanjung 2022][research_tanjung_2022]
- [Tanno and Tanno 2021][research_tanno_tanno_2021]
- [Tanno et al 2015][research_tanno_komuro_2015]
- [Tao 1995][research_tao_1995]
- [Tao et al 2008][research_tao_daren_2008]
- [Tao et al 2008][research_tao_daren_2008_b]
- [Tao et al 2009][research_tao_daren_2009]
- [Tao et al 2016][research_tao_li_2016]
- [Tarfeld 2003][research_tarfeld_2003]
- [Tarnavskii 2005][research_tarnavskii_2005]
- [Tarpley and Lewis 1993][research_tarpley_lewis_1993]
- [Tarpley and Lewis 1995][research_tarpley_lewis_1995]
- [Tarpley and Lewis 1995][research_tarpley_lewis_1995_b]
- [Tarpley et al 1996][research_tarpley_pines_1996]
- [Tatman][research_tatman]
- [Tatsuta et al 2025][research_tatsuta_yamada_2025]
- [Taylor 1959][research_taylor_1959]
- [Taylor and Jackson 1977][research_taylor_jackson_1977]
- [Taylor and Jackson 1978][research_taylor_jackson_1978]
- [Taylor and Stringer 2024][research_taylor_stringer_2024]
- [Tchuen and Burtschell 2011][research_tchuen_burtschell_2011]
- [Tchuen et al 2008][research_tchuen_burtschell_2008]
- [Teng et al 2012][research_teng_yu_2012]
- [Teng et al 2016][research_teng_yang_2016]
- [Teng et al 2017][research_teng_zhou_2017]
- [Terekhov 2023][research_terekhov_2023]
- [Test Method for Solid][research_test_method_b]
- [Test Method for Wind][research_test_method]
- [Test Method for Wind 1900][research_test_method_1900]
- [Test Method for Wind 2009][research_test_method_2009]
- [Testing Methods and Wind 2009][research_testing_methods_2009]
- [Tetlow and Doolan][research_tetlow_doolan]
- [Thakur and Segal 2003][research_thakur_segal_2003]
- [Thakur and Segal 2004][research_thakur_segal_2004]
- [Thakur and Segal 2006][research_thakur_segal_2006]
- [The AEDC Hypervelocity Wind 2002][research_the_aedc_2002]
- [The Agard Flight TEST 1959][research_the_agard_1959]
- [The Flight Environment Standard 2021][research_the_flight_2021]
- [The International Standard Atmosphere 2017][research_the_international_2017]
- [The international standard atmosphere 2026][research_the_international_2026]
- [The ONERA F4 High-Enthalpy 2002][research_the_onera_2002]
- [The SCIROCCO 70-MW Plasma 2002][research_the_scirocco_2002]
- [The Standard Atmosphere 1964][research_the_standard_1964]
- [The Standard Atmosphere 1976][research_the_standard_1976]
- [The Theoretical Study of 2012][research_the_theoretical_2012]
- [Theocaris and Koroneos 1963][research_theocaris_koroneos_1963]
- [Thermal Physics Temperature, Heat 2013][research_thermal_physics_2013]
- [Thermal Properties and Transient 1998][research_thermal_properties_1998]
- [Thermal Protection Methods for 2009][research_thermal_protection_2009]
- [Thermal Structural Analysis of 1992][research_thermal_structural_1992]
- [Thermodynamics of Real Gas 2010][research_thermodynamics_of_2010]
- [Thibodeaux 2002][research_thibodeaux_2002]
- [Thielman 1995][research_thielman_1995]
- [Thirunavukkarasu and Ghosh 2023][research_thirunavukkarasu_ghosh_2023]
- [Thivet and Pélissier 2003][research_thivet_pelissier_2003]
- [Thiéblot et al 1998][research_thieblot_roux_1998]
- [Thomas 1942][research_thomas_1942]
- [Thomas and Guy 1982][research_thomas_guy_1982]
- [Thomas and Perlbachs 1967][research_thomas_perlbachs_1967]
- [Thomas et al 1969][research_thomas_martellucci_1969]
- [Thomas et al 1985][research_thomas_singh_1985]
- [Thomas et al 1987][research_thomas_voland_1987]
- [Thomas et al 1991][research_thomas_dwoyer_1991]
- [Thomas et al 1994][research_thomas_harrison_1994]
- [Thomas et al 1998][research_thomas_hyde_1998]
- [Thomas et al 2010][research_thomas_czech_2010]
- [Thomas et al 2022][research_thomas_marayikkottuvijayan_2022]
- [Thome et al 2018][research_thome_dwivedi_2018]
- [Thompson 2015][research_thompson_2015]
- [Thompson 2025][research_thompson_2025]
- [Thornton 1994][research_thornton_1994]
- [Thornton and Dechaumphai 1986][research_thornton_dechaumphai_1986]
- [Thornton and Lamy 1992][research_thornton_lamy_1992]
- [Thornton et al 1989][research_thornton_oden_1989]
- [Threadgill and Bruce 2015][research_threadgill_bruce_2015]
- [Tian and Fan 2013][research_tian_fan_2013]
- [Tian et al 2016][research_tian_yang_2016]
- [Tian et al 2023][research_tian_duan_2023]
- [Tian et al 2026][research_tian_wan_2026]
- [Tian et al 2026][research_tian_zhang_2026]
- [Tieshan et al 2021][research_tieshan_zhiyao_2021]
- [Tietz et al 2006][research_tietz_chun_2006]
- [Tile-Gap Flow in the 1983][research_tile_gap_flow_1983]
- [Tilmann 1998][research_tilmann_1998]
- [Timnat 1987][research_timnat_1987]
- [Timofeev et al 2001][research_timofeev_voinovich_2001]
- [Timofeev et al 2008][research_timofeev_tahir_2008]
- [Tincher and Burnett 1992][research_tincher_burnett_1992]
- [Ting and Libby 1960][research_ting_libby_1960]
- [Tinney 2014][research_tinney_2014]
- [Tinney and Panickar 2013][research_tinney_panickar_2013]
- [Tirres et al 2002][research_tirres_bradley_2002]
- [Tirskii 1993][research_tirskii_1993]
- [Tirsky 1993][research_tirsky_1993]
- [Tirtey and Boyce 2009][research_tirtey_boyce_2009]
- [Tirtey et al 2006][research_tirtey_walpot_2006]
- [Tishkoff et al 1997][research_tishkoff_drummond_1997]
- [Titov 1961][research_titov_1961]
- [Tiwari et al 2001][research_tiwari_abdelsalam_2001]
- [Tiwari et al 2002][research_tiwari_taha_2002]
- [Tiwari et al 2026][research_tiwari_soman_2026]
- [Tobe and Grandhi 2013][research_tobe_grandhi_2013]
- [Tobin and Dec 2015][research_tobin_dec_2015]
- [Tomar 2012][research_tomar_2012]
- [Tomasi et al][research_tomasi_mutri]
- [Tomczak 2026][research_tomczak_2026]
- [Tomioka et al 1998][research_tomioka_kanda_1998]
- [Tomioka et al 2007][research_tomioka_hiraiwa_2007]
- [Tomioka et al 2007][research_tomioka_ueda_2007]
- [Tomioka et al 2016][research_tomioka_takahashi_2016]
- [Tomioka et al 2018][research_tomioka_takahashi_2018]
- [Tong and Giedt 1963][research_tong_giedt_1963]
- [Tong and Steinetz 1991][research_tong_steinetz_1991]
- [Tong et al 2022][research_tong_duan_2022]
- [Tong et al 2022][research_tong_yuan_2022]
- [Tong et al 2023][research_tong_yue_2023]
- [Tong et al 2024][research_tong_ji_2024]
- [Toong 1978][research_toong_1978]
- [Torres et al 2009][research_torres_stefanini_2009]
- [Torrez et al 2010][research_torrez_dalle_2010]
- [Torrez et al 2011][research_torrez_dalle_2011]
- [Touré and Schuelein 2017][research_toure_schuelein_2017]
- [Tracy 1981][research_tracy_1981]
- [Tracy and Wright 2020][research_tracy_wright_2020]
- [Trainini and Cabrera Fischer 2026][research_trainini_cabrerafischer_2026]
- [Tran and Chen 1998][research_tran_chen_1998]
- [Transient Thermal-Structural Analysis Using 1992][research_transient_thermal_structural_1992]
- [Transient Thermal-Structural Response of 1995][research_transient_thermal_structural_1995]
- [Transonic flight test of 1994][research_transonic_flight_1994]
- [Trapier et al][research_trapier_deck]
- [Trapier et al 2006][research_trapier_duveau_2006]
- [Trapier et al 2007][research_trapier_deck_2007]
- [Trapier et al 2007][research_trapier_deck_2007_b]
- [Trapier et al 2008][research_trapier_deck_2008]
- [Trefny 2020][research_trefny_2020]
- [Trefny and Dippold 2010][research_trefny_dippold_2010]
- [Trella and Vaglio-Laurin 1964][research_trella_vagliolaurin_1964]
- [Tretyakov et al 2021][research_tretyakov_tupikin_2021]
- [Trexler 1988][research_trexler_1988]
- [Triantafillou et al 1998][research_triantafillou_schwendeman_1998]
- [Trimmer 1968][research_trimmer_1968]
- [Trimmer et al 1986][research_trimmer_caryjr_1986]
- [Trittler et al 2008][research_trittler_fichter_2008]
- [Truitt, R. W. 1968][research_truittrw_1968]
- [Trulove 2008][research_trulove_2008]
- [Trunin et al 2004][research_trunin_krupnikov_2004]
- [Tsai et al 1992][research_tsai_miles_1992]
- [Tsuboi et al 2008][research_tsuboi_matsumoto_2008]
- [Tsujikawa 1996][research_tsujikawa_1996]
- [Tsukamoto et al 2003][research_tsukamoto_deturris_2003]
- [Tudosie 2017][research_tudosie_2017]
- [Tudosie 2017][research_tudosie_2017_b]
- [Tudosie 2018][research_tudosie_2018]
- [Tudosie 2022][research_tudosie_2022]
- [Tudosie and Prisacariu 2022][research_tudosie_prisacariu_2022]
- [Tudosie and Păunescu 2017][research_tudosie_paunescu_2017]
- [Tudosie et al 2019][research_tudosie_dumitru_2019]
- [Tumin 1996][research_tumin_1996]
- [Tunik 2020][research_tunik_2020]
- [Tunik and Mayorov 2022][research_tunik_mayorov_2022]
- [Tunik and Mayorov 2022][research_tunik_mayorov_2022_b]
- [Tunik et al 2022][research_tunik_gerasimov_2022]
- [Tuohy 2006][research_tuohy_2006]
- [Turcotte 1987][research_turcotte_1987]
- [Turner 1965][research_turner_1965]
- [Turner et al 2006][research_turner_hoerschgen_2006]
- [Turns and Kraige][research_turns_kraige]
- [Two-dimensional scramjet inlet unstart model, wind-tunnel blockage and actuation systems][research_inlet_unstart_model]
- [Two-phase flow in high-heat-flux 2006][research_two_phase_flow_2006]
- [Two-phase flow in high-heat-flux 2006][research_two_phase_flow_2006_b]
- [Tyagi and Achary 2017][research_tyagi_achary_2017]
- [Tyll et al 2000][research_tyll_bakos_2000]
- [Türkkahraman et al 2024][research_turkkahraman_ozcan_2024]
- [Türkoğlu et al 2026][research_turkoglu_donmez_2026]
- [U.S. Standard Atmosphere, 1976][research_us_standard_atmosphere]
- [Ueda et al 2006][research_ueda_takegoshi_2006]
- [Ueda et al 2009][research_ueda_kouchi_2009]
- [Ueno et al 2004][research_ueno_sarae_2004]
- [Ueno et al 2011][research_ueno_imamura_2011]
- [Uhlenbruck and Tietz 2004][research_uhlenbruck_tietz_2004]
- [ul Islam Rizvi et al 2015][research_ulislamrizvi_linshu_2015]
- [Ullman and Raman 2023][research_ullman_raman_2023]
- [Unnikrishnan and Gaitonde 2021][research_unnikrishnan_gaitonde_2021]
- [Unsteady interaction mechanism of 2023][research_unsteady_interaction_2023]
- [Unterberg 1957][research_unterberg_1957]
- [Upadhyay et al 2019][research_upadhyay_kumar_2019]
- [Upper Atmosphere Re-Entry Study 1961][research_upper_atmosphere_1961]
- [US Standard Atmosphere Model 2014][research_us_standard_2014]
- [US tests hypersonic flying 2011][research_us_tests_2011]
- [Utheza et al 1996][research_utheza_saurel_1996]
- [Utomo and Bura 2019][research_utomo_bura_2019]
- [Utyuzhnikov and Tirskiy 2013][research_utyuzhnikov_tirskiy_2013]
- [V and Rao 2023][research_v_rao_2023]
- [Vaca-Rios and Cerón-Muñoz 2025][research_vacarios_ceronmunoz_2025]
- [Vahl and Edwards 1978][research_vahl_edwards_1978]
- [Valaik et al 1997][research_valaik_hyde_1997]
- [Valaik et al 1998][research_valaik_bowman_1998]
- [Valdivia et al 2014][research_valdivia_yuceil_2014]
- [Van 1963][research_van_1963]
- [Van Camp and Williams 1974][research_vancamp_williams_1974]
- [Van den Borre et al 2023][research_vandenborre_saracoglu_2023]
- [Van Der Geld et al 1990][research_vandergeld_korting_1990]
- [van der Heide et al 2025][research_vanderheide_lock_2025]
- [van der Heide et al 2026][research_vanderheide_bone_2026]
- [Van Der Kreek][research_vanderkreek]
- [Van der lee et al 2021][research_vanderlee_yokev_2021]
- [van der Lee et al 2023][research_vanderlee_michaels_2023]
- [van der Lee et al 2026][research_vanderlee_kaner_2026]
- [van der Lee et al 2026][research_vanderlee_seniortybora_2026]
- [Van Driest and Blumer 1961][research_vandriest_blumer_1961]
- [van Hoffen 2024][research_vanhoffen_2024]
- [van Hoffen et al 2024][research_vanhoffen_buttsworth_2024]
- [van Keuk et al 1998][research_vankeuk_ballmann_1998]
- [Van Pelt 1981][research_vanpelt_1981]
- [Van Wie 1992][research_vanwie_1992]
- [Van Wie and Molder 1992][research_vanwie_molder_1992]
- [Vanamamalai and Panneerselvam 2024][research_vanamamalai_panneerselvam_2024]
- [Vanatta and Inderhees 1988][research_vanatta_inderhees_1988]
- [Vander Schaaf et al 2025][research_vanderschaaf_acharya_2025]
- [Vanstone et al 2017][research_vanstone_hashemi_2017]
- [Vanstone et al 2018][research_vanstone_hashemi_2018]
- [Vanstone et al 2018][research_vanstone_lingren_2018]
- [Vanyai et al 2018][research_vanyai_grieve_2018]
- [Vanyai et al 2019][research_vanyai_grieve_2019]
- [Vanyai et al 2020][research_vanyai_grieve_2020]
- [Vanyai et al 2021][research_vanyai_brieschenk_2021]
- [Varghese et al 2018][research_varghese_b_2018]
- [Variation of natural radioactivity 1956][research_variation_of_1956]
- [Varma and Zhong 2022][research_varma_zhong_2022]
- [Varner 1976][research_varner_1976]
- [Varshney and Baig 2019][research_varshney_baig_2019]
- [Varshney et al 2020][research_varshney_varshney_2020]
- [Varshney et al 2020][research_varshney_varshney_2020_b]
- [Vartio et al 2008][research_vartio_shaw_2008]
- [Varwig 1963][research_varwig_1963]
- [Vasilevsky 2022][research_vasilevsky_2022]
- [Vaughan 2003][research_vaughan_2003]
- [Vaughan and Schwartz 1962][research_vaughan_schwartz_1962]
- [Vaughn and Lindsay 1988][research_vaughn_lindsay_1988]
- [Vedula 1989][research_vedula_1989]
- [Veletas 2026][research_veletas_2026]
- [Venkatapathy, E. et al 1995][research_venkatapathye_tokarcikpolskys_1995]
- [Venkateshwaran and Padmanathan 2026][research_venkateshwaran_padmanathan_2026]
- [Venkateswarlu et al 2025][research_venkateswarlu_kolhe_2025]
- [Veraar 2008][research_veraar_2008]
- [Veraar 2009][research_veraar_2009]
- [Verhoff and O'Neil 1987][research_verhoff_oneil_1987]
- [Verma 2010][research_verma_2010]
- [Verma and Shukla 2021][research_verma_shukla_2021]
- [Verma et al 2014][research_verma_manisankar_2014]
- [Verma et al 2019][research_verma_shukla_2019]
- [Verma et al 2021][research_verma_kapayeva_2021]
- [Verma et al 2021][research_verma_pandey_2021]
- [Verma et al 2022][research_verma_pandey_2022]
- [Verma et al 2022][research_verma_sharma_2022]
- [Vicente and Foy 1963][research_vicente_foy_1963]
- [Vicente and Foy 1963][research_vicente_foy_1963_b]
- [Vidal, R. J. 1974][research_vidalrj_1974]
- [Vijayakumar 2020][research_vijayakumar_2020]
- [Vijayakumar et al 2014][research_vijayakumar_wilson_2014]
- [Vijayakumar et al 2020][research_vijayakumar_narendar_2020]
- [Vincent-Randonnier et al 2008][research_vincentrandonnier_rouxel_2008]
- [Vinogradov et al 1990][research_vinogradov_grachev_1990]
- [Violi 2013][research_violi_2013]
- [Viscous Flow Basic Aspects 2006][research_viscous_flow_2006]
- [Viscous Flow Basic Aspects 2019][research_viscous_flow_2019]
- [Viscous Shock-Layer Predictions for 1983][research_viscous_shock_layer_1983]
- [Vishwakarma and Rana 2025][research_vishwakarma_rana_2025]
- [Viviand 1991][research_viviand_1991]
- [Vlach 2014][research_vlach_2014]
- [Voake et al 2024][research_voake_nermoen_2024]
- [Vogel et al 2009][research_vogel_kelkar_2009]
- [Voland 1990][research_voland_1990]
- [Voland et al 1999][research_voland_auslender_1999]
- [Volkov 2023][research_volkov_2023]
- [Volpiani 2021][research_volpiani_2021]
- [Von Eckartsberg et al 2025][research_voneckartsberg_goldman_2025]
- [von Elbe 1955][research_vonelbe_1955]
- [von Lavante et al 2000][research_vonlavante_kallenberg_2000]
- [Votta et al 2011][research_votta_ranuzzi_2011]
- [Vuchuru and Dinda 2024][research_vuchuru_dinda_2024]
- [Wada 2026][research_wada_2026]
- [Wagner and Dale 1985][research_wagner_dale_1985]
- [Wagner et al 2007][research_wagner_valdivia_2007]
- [Wagner et al 2008][research_wagner_yuceil_2008]
- [Wagner et al 2009][research_wagner_yuceil_2009]
- [Wagner et al 2010][research_wagner_yuceil_2010]
- [Waidmann et al 2024][research_waidmann_brummund_2024]
- [Wainwright 1962][research_wainwright_1962]
- [Wakamatsu et al 2009][research_wakamatsu_kuno_2009]
- [Walchner 1974][research_walchner_1974]
- [Walchner et al 1967][research_walchner_sawyer_1967]
- [Walchner et al 1969][research_walchner_sawyer_1969]
- [Walker 1949][research_walker_1949]
- [Walker 1952][research_walker_1952]
- [Walker 1955][research_walker_1955]
- [Walker and Oberkampf 1991][research_walker_oberkampf_1991]
- [Walker et al 2006][research_walker_kennedy_2006]
- [Walker et al 2008][research_walker_rodgers_2008]
- [Walker et al 2008][research_walker_sherk_2008]
- [Walters 1984][research_walters_1984]
- [Walters 1992][research_walters_1992]
- [Waltrup and Billig 1972][research_waltrup_billig_1972]
- [Waltrup et al 1980][research_waltrup_billig_1980]
- [Waltrup et al 1981][research_waltrup_billig_1981]
- [Waltrup et al 1996][research_waltrup_white_1996]
- [Wan and Chen 2022][research_wan_chen_2022]
- [Wan et al 2012][research_wan_wang_2012]
- [Wang 1998][research_wang_1998]
- [Wang 1998][research_wang_1998_b]
- [Wang 2004][research_wang_2004]
- [Wang 2004][research_wang_2004_b]
- [Wang 2007][research_wang_2007]
- [Wang 2014][research_wang_2014]
- [Wang 2014][research_wang_2014_b]
- [Wang 2017][research_wang_2017]
- [Wang 2019][research_wang_2019]
- [Wang and Cai 2016][research_wang_cai_2016]
- [Wang and Gao 2013][research_wang_gao_2013]
- [Wang and Guo 2013][research_wang_guo_2013]
- [Wang and Le 2000][research_wang_le_2000]
- [Wang and Luo 2022][research_wang_luo_2022]
- [Wang and Ma 2024][research_wang_ma_2024]
- [Wang and Prakash 2024][research_wang_prakash_2024]
- [Wang and Wang 1997][research_wang_wang_1997]
- [Wang and Wang 2020][research_wang_wang_2020]
- [Wang and Wang 2024][research_wang_wang_2024_e]
- [Wang and Wu 2017][research_wang_wu_2017]
- [Wang and Xia 2022][research_wang_xia_2022]
- [Wang and Zhai 2023][research_wang_zhai_2023]
- [Wang and Zhang 1992][research_wang_zhang_1992]
- [Wang and Zhang 2021][research_wang_zhang_2021]
- [Wang and Zhang 2025][research_wang_zhang_2025]
- [Wang et al 1959][research_wang_anthony_1959]
- [Wang et al 1980][research_wang_zakkay_1980]
- [Wang et al 1996][research_wang_yu_1996]
- [Wang et al 2005][research_wang_zhang_2005]
- [Wang et al 2006][research_wang_fang_2006]
- [Wang et al 2007][research_wang_feng_2007]
- [Wang et al 2011][research_wang_xie_2011]
- [Wang et al 2012][research_wang_liu_2012]
- [Wang et al 2012][research_wang_sun_2012]
- [Wang et al 2012][research_wang_xu_2012]
- [Wang et al 2013][research_wang_ge_2013]
- [Wang et al 2013][research_wang_wang_2013]
- [Wang et al 2013][research_wang_wang_2013_b]
- [Wang et al 2013][research_wang_wang_2013_c]
- [Wang et al 2013][research_wang_wang_2013_d]
- [Wang et al 2013][research_wang_wang_2013_e]
- [Wang et al 2014][research_wang_wang_2014]
- [Wang et al 2015][research_wang_liu_2015]
- [Wang et al 2015][research_wang_wu_2015]
- [Wang et al 2016][research_wang_xiao_2016]
- [Wang et al 2017][research_wang_hao_2017]
- [Wang et al 2017][research_wang_li_2017]
- [Wang et al 2017][research_wang_li_2017_b]
- [Wang et al 2017][research_wang_qin_2017]
- [Wang et al 2017][research_wang_song_2017]
- [Wang et al 2017][research_wang_zhang_2017]
- [Wang et al 2018][research_wang_chen_2018]
- [Wang et al 2018][research_wang_hou_2018]
- [Wang et al 2018][research_wang_pan_2018]
- [Wang et al 2019][research_wang_hou_2019]
- [Wang et al 2019][research_wang_hou_2019_b]
- [Wang et al 2019][research_wang_xue_2019]
- [Wang et al 2020][research_wang_li_2020]
- [Wang et al 2020][research_wang_xu_2020]
- [Wang et al 2020][research_wang_yang_2020]
- [Wang et al 2021][research_wang_chang_2021]
- [Wang et al 2021][research_wang_he_2021]
- [Wang et al 2022][research_wang_fan_2022]
- [Wang et al 2022][research_wang_feng_2022]
- [Wang et al 2022][research_wang_jin_2022]
- [Wang et al 2022][research_wang_xin_2022]
- [Wang et al 2022][research_wang_zhang_2022]
- [Wang et al 2022][research_wang_zhao_2022]
- [Wang et al 2023][research_wang_fan_2023]
- [Wang et al 2023][research_wang_huang_2023]
- [Wang et al 2023][research_wang_liu_2023]
- [Wang et al 2023][research_wang_wang_2023]
- [Wang et al 2023][research_wang_wang_2023_b]
- [Wang et al 2023][research_wang_wang_2023_c]
- [Wang et al 2023][research_wang_xin_2023]
- [Wang et al 2023][research_wang_xu_2023]
- [Wang et al 2023][research_wang_zhang_2023]
- [Wang et al 2023][research_wang_zhao_2023]
- [Wang et al 2024][research_wang_gan_2024]
- [Wang et al 2024][research_wang_vohs_2024]
- [Wang et al 2024][research_wang_wang_2024]
- [Wang et al 2024][research_wang_wang_2024_b]
- [Wang et al 2024][research_wang_wang_2024_c]
- [Wang et al 2024][research_wang_wang_2024_d]
- [Wang et al 2024][research_wang_xu_2024]
- [Wang et al 2024][research_wang_yao_2024]
- [Wang et al 2024][research_wang_yao_2024_b]
- [Wang et al 2025][research_wang_an_2025]
- [Wang et al 2025][research_wang_chen_2025]
- [Wang et al 2025][research_wang_feng_2025]
- [Wang et al 2025][research_wang_feng_2025_b]
- [Wang et al 2025][research_wang_he_2025]
- [Wang et al 2025][research_wang_li_2025]
- [Wang et al 2025][research_wang_liu_2025]
- [Wang et al 2025][research_wang_liu_2025_b]
- [Wang et al 2025][research_wang_tang_2025]
- [Wang et al 2025][research_wang_tang_2025_b]
- [Wang et al 2025][research_wang_yao_2025]
- [Wang et al 2025][research_wang_yao_2025_b]
- [Wang et al 2025][research_wang_zhao_2025]
- [Wang et al 2026][research_wang_huang_2026]
- [Wang et al 2026][research_wang_li_2026]
- [Wang et al 2026][research_wang_liu_2026]
- [Wang et al 2026][research_wang_liu_2026_b]
- [Wang et al 2026][research_wang_liu_2026_c]
- [Wang et al 2026][research_wang_liu_2026_d]
- [Wang et al 2026][research_wang_rajan_2026]
- [Wang et al 2026][research_wang_zhang_2026]
- [Ward 1988][research_ward_1988]
- [Ward and Hewitt 1988][research_ward_hewitt_1988]
- [Ward and Myers 1967][research_ward_myers_1967]
- [Ward and Smart 2026][research_ward_smart_2026]
- [Ward et al 1977][research_ward_baltakis_1977]
- [Warning and McQuilling 2022][research_warning_mcquilling_2022]
- [Warsop and Crowther 2019][research_warsop_crowther_2019]
- [Wartemann et al 2009][research_wartemann_ludeke_2009]
- [Washington and Humphrey 1969][research_washington_humphrey_1969]
- [Wassel et al 1984][research_wassel_shih_1984]
- [Wasserman 1952][research_wasserman_1952]
- [Waszkowski and Pisani 2025][research_waszkowski_pisani_2025]
- [Watanabe et al 1996][research_watanabe_ishimoto_1996]
- [Watari et al 2006][research_watari_hirabayashi_2006]
- [Watmuff and Smits 1987][research_watmuff_smits_1987]
- [Watson 1969][research_watson_1969]
- [Watt and Aronson 1964][research_watt_aronson_1964]
- [Waverider Aerodynamics 1986][research_waverider_aerodynamics_1986]
- [Way et al 2024][research_way_sescu_2024]
- [Weatherill and Zartarian 1958][research_weatherill_zartarian_1958]
- [Weatherston 1969][research_weatherston_1969]
- [Weaver and Hunsaker 2025][research_weaver_hunsaker_2025]
- [Weber and Karemaa 1972][research_weber_karemaa_1972]
- [Weber et al 1997][research_weber_kriven_1997]
- [Weeks 1969][research_weeks_1969]
- [Weeks 1970][research_weeks_1970]
- [Weeratunga and Menon 1993][research_weeratunga_menon_1993]
- [Wegener 1977][research_wegener_1977]
- [Wegener and Lobb 1952][research_wegener_lobb_1952]
- [Wei et al 2012][research_wei_peers_2012]
- [Wei et al 2016][research_wei_wang_2016]
- [Wei et al 2019][research_wei_hu_2019]
- [Wei et al 2024][research_wei_zhang_2024]
- [Wei et al 2026][research_wei_ye_2026]
- [Wei-wei et al 2013][research_weiwei_leping_2013]
- [Weidner 1980][research_weidner_1980]
- [Weidner et al 1976][research_weidner_small_1976]
- [Weidner, John P. 1992][research_weidnerjohnp_1992]
- [Weidong et al 2015][research_weidong_xianlin_2015]
- [Weiland 2019][research_weiland_2019]
- [Weiler et al 1972][research_weiler_derbidge_1972]
- [Weilmuenster et al 1995][research_weilmuenster_gnoffo_1995]
- [Weilmuenster et al 1996][research_weilmuenster_gnoffo_1996]
- [Weimer 2022][research_weimer_2022]
- [Weinacht 2014][research_weinacht_2014]
- [Weinberg 1952][research_weinberg_1952]
- [Weirich et al 1996][research_weirich_fogarty_1996]
- [Weissman 1990][research_weissman_1990]
- [Wells, William L. 1987][research_wellswilliaml_1987]
- [Welsh et al 1979][research_welsh_lawrence_1979]
- [Wen et al 2027][research_wen_sun_2027]
- [Wenbiao et al 2014][research_wenbiao_dong_2014]
- [Wendel and Gaitonde 2026][research_wendel_gaitonde_2026]
- [Wendel et al 2025][research_wendel_gaitonde_2025]
- [Wendt][research_wendt]
- [Wenfeng et al 2017][research_wenfeng_peng_2017]
- [Wenkai et al 2017][research_wenkai_hou_2017]
- [Wenkai et al 2017][research_wenkai_hou_2017_b]
- [Wenkai et al 2017][research_wenkai_zhongxi_2017]
- [Wepler et al 2001][research_wepler_huhn_2001]
- [West 2005][research_west_2005]
- [West and Bynum 2024][research_west_bynum_2024]
- [Westinghouse Electric Corp Pittsburgh Pa 1967][research_westinghouseelectriccorppittsburghpa_1967]
- [Wexler and Idan 2026][research_wexler_idan_2026]
- [Weyl 1998][research_weyl_1998]
- [White 1993][research_white_1993]
- [White 2004][research_white_2004]
- [White and Andrikidis 1996][research_white_andrikidis_1996]
- [White and Rhie 1988][research_white_rhie_1988]
- [White and Rhie 1992][research_white_rhie_1992]
- [White et al 1961][research_white_richardp_1961]
- [White et al 1983][research_white_janssen_1983]
- [Whitehurst et al 1992][research_whitehurst_krauss_1992]
- [Whitney 1963][research_whitney_1963]
- [Whitside][research_whitside]
- [Wickham et al 1999][research_wickham_alptekin_1999]
- [Wickham et al 2002][research_wickham_engel_2002]
- [Wickham et al 2005][research_wickham_engel_2005]
- [Wickham et al 2008][research_wickham_engel_2008]
- [Wideman et al 1994][research_wideman_miles_1994]
- [Wideman et al 1995][research_wideman_brown_1995]
- [Wiedemeier and Siemers 1975][research_wiedemeier_siemers_1975]
- [Wiese et al 2013][research_wiese_annaswamy_2013]
- [Wieting 1990][research_wieting_1990]
- [Wieting and Guy 1976][research_wieting_guy_1976]
- [Wilkinson and Wilkinson 1997][research_wilkinson_wilkinson_1997]
- [Wilks 2006][research_wilks_2006]
- [Willard et al 2009][research_willard_giel_2009]
- [Williams 1965][research_williams_1965]
- [Williams 2021][research_williams_2021]
- [Williams and Lewis 1975][research_williams_lewis_1975]
- [Williams et al 2001][research_williams_edwards_2001]
- [Williams et al 2006][research_williams_bolender_2006]
- [Williams et al 2024][research_williams_bartkowicz_2024]
- [Williams et al 2026][research_williams_davuluri_2026]
- [Williamson et al 2026][research_williamson_pascoe_2026]
- [Wilson 1966][research_wilson_1966]
- [Wilson 1990][research_wilson_1990]
- [Wilson and Benson 1978][research_wilson_benson_1978]
- [Wilson and Wright 1977][research_wilson_wright_1977]
- [Wilson et al 2009][research_wilson_agarwal_2009]
- [Wimber 1976][research_wimber_1976]
- [Wind Tunnel Test Techniques 2024][research_wind_tunnel_2024]
- [Windisch et al 2012][research_windisch_reinartz_2012]
- [Wing][research_wing]
- [Wingfield, III 2001][research_wingfieldiii_2001]
- [Winkler 1952][research_winkler_1952]
- [Winkler 1954][research_winkler_1954]
- [Wise][research_wise]
- [Witte et al 2003][research_witte_huebner_2003]
- [Wittliff and Wilson 1961][research_wittliff_wilson_1961]
- [Wittliff et al 1992][research_wittliff_oconnor_1992]
- [Witzmann 2006][research_witzmann_2006]
- [Wohlleben et al 1991][research_wohlleben_schnell_1991]
- [Wolf and Bossert 2001][research_wolf_bossert_2001]
- [Wolf et al 1951][research_wolf_mullen_1951]
- [Wolfe 1964][research_wolfe_1964]
- [Wollrab 1966][research_wollrab_1966]
- [Woodward and Mesrobain 1953][research_woodward_mesrobain_1953]
- [Woodward et al 1983][research_woodward_glaser_1983]
- [Wright 2015][research_wright_2015]
- [Wright 2022][research_wright_2022]
- [Wright et al 2000][research_wright_foley_2000]
- [Wu and Cheng 2005][research_wu_cheng_2005]
- [Wu and Guo 2018][research_wu_guo_2018]
- [Wu and He 2022][research_wu_he_2022]
- [Wu and Wang 2015][research_wu_wang_2015]
- [Wu and Wei 2022][research_wu_wei_2022]
- [Wu and Wei 2023][research_wu_wei_2023]
- [Wu and Xiao 2009][research_wu_xiao_2009]
- [Wu and Yu 2018][research_wu_yu_2018]
- [Wu et al 2013][research_wu_ding_2013]
- [Wu et al 2015][research_wu_liu_2015]
- [Wu et al 2015][research_wu_wang_2015_b]
- [Wu et al 2020][research_wu_lin_2020]
- [Wu et al 2021][research_wu_song_2021]
- [Wu et al 2023][research_wu_fan_2023]
- [Wu et al 2024][research_wu_laguarda_2024]
- [Wu et al 2025][research_wu_yuan_2025]
- [Wu et al 2026][research_wu_fan_2026]
- [Wu et al 2026][research_wu_lagurada_2026]
- [Wu et al 2026][research_wu_wu_2026]
- [Wu Liaoni and Wang Mengmeng 2012][research_wuliaoni_wangmengmeng_2012]
- [Wulff and Zoellner 1991][research_wulff_zoellner_1991]
- [Wurster 1981][research_wurster_1981]
- [Wurster and Marrone 1962][research_wurster_marrone_1962]
- [Wygle 1981][research_wygle_1981]
- [Wächter and Sachs 2006][research_wachter_sachs_2006]
- [X-43 hypersonic vehicle technology development][research_x43_technology]
- [Xi et al 2026][research_xi_yao_2026]
- [Xia et al 2020][research_xia_chen_2020]
- [Xia et al 2025][research_xia_sun_2025]
- [Xia et al 2026][research_xia_han_2026]
- [Xian Lin Huang and Dong Ming Ge 2010][research_xianlinhuang_dongmingge_2010]
- [Xianyu et al 2007][research_xianyu_xiaoshan_2007]
- [Xianyu et al 2007][research_xianyu_xiaoshan_2007_b]
- [Xiao and Yang 2025][research_xiao_yang_2025]
- [Xiao et al 2006][research_xiao_liu_2006]
- [Xiao et al 2008][research_xiao_yue_2008]
- [Xiao et al 2026][research_xiao_jin_2026]
- [Xiao-Qing et al 2011][research_xiaoqing_zhongxi_2011]
- [Xiaoqing et al 2010][research_xiaoqing_zhongxi_2010]
- [Xie et al 2016][research_xie_ge_2016]
- [Xie et al 2020][research_xie_dong_2020]
- [Xie et al 2021][research_xie_zhuang_2021]
- [Xie et al 2025][research_xie_li_2025]
- [Xie et al 2026][research_xie_zeng_2026]
- [Xin 2023][research_xin_2023]
- [Xin and Zhang 2011][research_xin_zhang_2011]
- [Xin et al 2023][research_xin_zhang_2023]
- [Xin et al 2025][research_xin_li_2025]
- [Xin Wang and Shijie Sun 2010][research_xinwang_shijiesun_2010]
- [Xin Wang et al 2008][research_xinwang_dongzhufeng_2008]
- [Xing et al 2017][research_xing_ruan_2017]
- [Xiong et al 2017][research_xiong_wang_2017]
- [Xiong et al 2019][research_xiong_bai_2019]
- [Xiong et al 2021][research_xiong_zheng_2021]
- [Xiong et al 2022][research_xiong_qin_2022]
- [Xiong Luo et al 2008][research_xiongluo_zengqisun_2008]
- [Xu 2015][research_xu_2015]
- [Xu and Cai 2011][research_xu_cai_2011]
- [Xu and Fang 2022][research_xu_fang_2022]
- [Xu and Mao][research_xu_mao]
- [Xu and Zhang 2015][research_xu_zhang_2015]
- [Xu et al 1996][research_xu_kim_1996]
- [Xu et al 2003][research_xu_khalid_2003]
- [Xu et al 2004][research_xu_mirmirani_2004]
- [Xu et al 2012][research_xu_sun_2012]
- [Xu et al 2012][research_xu_wang_2012]
- [Xu et al 2015][research_xu_wu_2015]
- [Xu et al 2017][research_xu_yu_2017]
- [Xu et al 2018][research_xu_chang_2018]
- [Xu et al 2018][research_xu_sun_2018]
- [Xu et al 2019][research_xu_wang_2019]
- [Xu et al 2021][research_xu_lin_2021]
- [Xu et al 2022][research_xu_wang_2022]
- [Xu et al 2022][research_xu_wang_2022_b]
- [Xu et al 2023][research_xu_cheng_2023]
- [Xu et al 2023][research_xu_luan_2023]
- [Xu Mingliang et al 2010][research_xumingliang_liuluhua_2010]
- [Xudong Liu et al 2016][research_xudongliu_lincheng_2016]
- [Xue and Haibin 2017][research_xue_haibin_2017]
- [Xue et al 1994][research_xue_bostic_1994]
- [Xue et al 2017][research_xue_wei_2017]
- [Xue et al 2018][research_xue_guodong_2018]
- [Xue et al 2023][research_xue_huang_2023]
- [Ya-Long et al 2014][research_yalong_guangbin_2014]
- [Yager 2013][research_yager_2013]
- [Yahalom 1971][research_yahalom_1971]
- [Yahui et al 2021][research_yahui_yitao_2021]
- [Yakimov 2018][research_yakimov_2018]
- [Yakimov 2018][research_yakimov_2018_b]
- [Yakimov 2018][research_yakimov_2018_c]
- [Yakubayev et al 2026][research_yakubayev_gschwend_2026]
- [Yamamoto and Kano 1996][research_yamamoto_kano_1996]
- [Yamamoto et al 2020][research_yamamoto_kojima_2020]
- [Yamato et al 1988][research_yamato_okada_1988]
- [Yan 2013][research_yan_2013]
- [Yan 2014][research_yan_2014]
- [Yan 2023][research_yan_2023]
- [Yan and Fu 2026][research_yan_fu_2026]
- [Yan and Wang 2012][research_yan_wang_2012]
- [Yan and Zhang 2026][research_yan_zhang_2026]
- [Yan Binbin et al 2009][research_yanbinbin_lucunkan_2009]
- [Yan et al 2008][research_yan_pan_2008]
- [Yan et al 2014][research_yan_bing_2014]
- [Yan et al 2014][research_yan_yuzhen_2014]
- [Yan et al 2014][research_yan_yuzhen_2014_b]
- [Yan et al 2016][research_yan_liu_2016]
- [Yan et al 2016][research_yan_shaohua_2016]
- [Yan et al 2017][research_yan_fan_2017]
- [Yan et al 2018][research_yan_liu_2018]
- [Yan et al 2020][research_yan_wu_2020]
- [Yan et al 2022][research_yan_fan_2022]
- [Yan et al 2022][research_yan_liu_2022]
- [Yan et al 2024][research_yan_sun_2024]
- [Yan et al 2025][research_yan_tian_2025]
- [Yan et al 2025][research_yan_zhu_2025]
- [Yanagihara et al 2003][research_yanagihara_nishizawa_2003]
- [Yang 2021][research_yang_2021]
- [Yang 2021][research_yang_2021_b]
- [Yang 2021][research_yang_2021_c]
- [Yang 2021][research_yang_2021_d]
- [Yang 2021][research_yang_2021_e]
- [yang and culick 1986][research_yang_culick_1986]
- [Yang and Li 2023][research_yang_li_2023]
- [Yang and Liu 2017][research_yang_liu_2017]
- [Yang and Qi 2016][research_yang_qi_2016]
- [Yang and Wang 2021][research_yang_wang_2021]
- [Yang and Xiao 2026][research_yang_xiao_2026]
- [Yang and Yuh-Yih Wu 1994][research_yang_yuhyihwu_1994]
- [Yang et al 2013][research_yang_li_2013]
- [Yang et al 2013][research_yang_yuan_2013]
- [Yang et al 2014][research_yang_chang_2014]
- [Yang et al 2014][research_yang_chang_2014_b]
- [Yang et al 2014][research_yang_duan_2014]
- [Yang et al 2014][research_yang_lee_2014]
- [Yang et al 2014][research_yang_yu_2014]
- [Yang et al 2014][research_yang_zhao_2014]
- [Yang et al 2015][research_yang_wang_2015]
- [Yang et al 2016][research_yang_lee_2016]
- [Yang et al 2017][research_yang_bao_2017]
- [Yang et al 2017][research_yang_li_2017]
- [Yang et al 2017][research_yang_wang_2017]
- [Yang et al 2020][research_yang_lee_2020]
- [Yang et al 2020][research_yang_zhou_2020]
- [Yang et al 2024][research_yang_lin_2024]
- [Yang et al 2024][research_yang_tian_2024]
- [Yang et al 2024][research_yang_wang_2024]
- [Yang et al 2024][research_yang_xie_2024]
- [Yang et al 2024][research_yang_yuan_2024]
- [Yang et al 2024][research_yang_zhao_2024]
- [Yang et al 2025][research_yang_gou_2025]
- [Yang et al 2025][research_yang_lin_2025]
- [Yang et al 2025][research_yang_liu_2025]
- [Yang et al 2025][research_yang_wang_2025]
- [Yang et al 2025][research_yang_xie_2025]
- [Yang et al 2025][research_yang_xie_2025_b]
- [Yang et al 2025][research_yang_zhang_2025]
- [Yang et al 2026][research_yang_cai_2026]
- [Yang et al 2026][research_yang_cheng_2026]
- [Yang et al 2026][research_yang_wang_2026]
- [Yankui et al 2005][research_yankui_dongjun_2005]
- [Yao and Xia 2023][research_yao_xia_2023]
- [Yao et al 2001][research_yao_thomas_2001]
- [Yao et al 2006][research_yao_petty_2006]
- [Yao et al 2009][research_yao_bao_2009]
- [Yao et al 2009][research_yao_bao_2009_b]
- [Yao et al 2017][research_yao_chaoyang_2017]
- [Yao et al 2017][research_yao_cui_2017]
- [Yao et al 2023][research_yao_hu_2023]
- [Yao et al 2023][research_yao_wang_2023]
- [Yao et al 2025][research_yao_wu_2025]
- [Yaosheng 2018][research_yaosheng_2018]
- [Yarantsev et al 2019][research_yarantsev_firsov_2019]
- [Yarng and Guan 1988][research_yarng_guan_1988]
- [Yatsukhno 2020][research_yatsukhno_2020]
- [Yatsuyanagi 2009][research_yatsuyanagi_2009]
- [Yechout 1988][research_yechout_1988]
- [Yeh et al 2017][research_yeh_tsai_2017]
- [Yeh et al 2023][research_yeh_veals_2023]
- [Yeneriz et al 1989][research_yeneriz_davis_1989]
- [Yeneriz et al 1991][research_yeneriz_davis_1991]
- [Yentsch and Gaitonde 2013][research_yentsch_gaitonde_2013]
- [Yentsch and Gaitonde 2014][research_yentsch_gaitonde_2014]
- [Yergensen and Rhea 1988][research_yergensen_rhea_1988]
- [Yi et al 2009][research_yi_jianhan_2009]
- [Yin et al 2017][research_yin_qin_2017]
- [Yin et al 2024][research_yin_nakamura_2024]
- [Yin et al 2024][research_yin_zeng_2024]
- [Ying et al 2018][research_ying_fang_2018]
- [Yip et al 1990][research_yip_strawa_1990]
- [Yong-sheng and Rui-sen 2005][research_yongsheng_ruisen_2005]
- [Yonggang et al 2019][research_yonggang_yang_2019]
- [Yoon and Chung 1996][research_yoon_chung_1996]
- [Yoon, Bok-Hyun and Rasmussen, Maurice L. 1991][research_yoonbokhyun_rasmussenmauricel_1991]
- [Yorita 2016][research_yorita_2016]
- [Yoshikawa and Pan 1998][research_yoshikawa_pan_1998]
- [Yost and Frame 2015][research_yost_frame_2015]
- [You and Liang 2009][research_you_liang_2009]
- [You and Liang 2009][research_you_liang_2009_b]
- [You et al 2009][research_you_zhu_2009]
- [You et al 2013][research_you_luedeke_2013]
- [You-Quan Chang 2009][research_youquanchang_2009]
- [Young 1966][research_young_1966]
- [Young and Goldstein 1999][research_young_goldstein_1999]
- [Young et al 2006][research_young_balar_2006]
- [Young et al 2006][research_young_kokan_2006]
- [Youssef et al 2008][research_youssef_reiman_2008]
- [Youssef et al 2009][research_youssef_reiman_2009]
- [Yu 2026][research_yu_2026]
- [Yu and Chen 2011][research_yu_chen_2011]
- [Yu and Newman 2003][research_yu_newman_2003]
- [Yu and Schadow 1994][research_yu_schadow_1994]
- [Yu et al 1999][research_yu_wilson_1999]
- [Yu et al 2002][research_yu_li_2002]
- [Yu et al 2005][research_yu_kim_2005]
- [Yu et al 2007][research_yu_chang_2007]
- [Yu et al 2014][research_yu_zhang_2014]
- [Yu et al 2015][research_yu_huang_2015]
- [Yu et al 2021][research_yu_ao_2021]
- [Yu et al 2022][research_yu_liu_2022]
- [Yu et al 2022][research_yu_ni_2022]
- [Yu et al 2022][research_yu_zhou_2022]
- [Yu et al 2025][research_yu_wang_2025]
- [Yu et al 2025][research_yu_wang_2025_b]
- [Yu Li and Nai-gang Cui 2008][research_yuli_naigangcui_2008]
- [Yu, Sheng-Tao et al 1988][research_yushengtao_hsiehkwangchung_1988]
- [Yuan et al 2019][research_yuan_kawano_2019]
- [Yuan et al 2020][research_yuan_sivasankaran_2020]
- [Yuan et al 2026][research_yuan_gao_2026]
- [Yuan et al 2026][research_yuan_liu_2026]
- [Yuceil et al 2009][research_yuceil_valdivia_2009]
- [Yue et al 2009][research_yue_xiao_2009]
- [Yue et al 2010][research_yue_guiping_2010]
- [Yue et al 2016][research_yue_wu_2016]
- [Yue et al 2017][research_yue_lu_2017]
- [Yukhno et al 2021][research_yukhno_volkov_2021]
- [Yulian and Bin 2014][research_yulian_bin_2014]
- [Yumusak and Eyi 2013][research_yumusak_eyi_2013]
- [Yun et al 2022][research_yun_cole_2022]
- [Yun et al 2022][research_yun_cole_2022_b]
- [Yun et al 2026][research_yun_kim_2026]
- [Yungster et al 2014][research_yungster_paxson_2014]
- [Zaehringer et al 2003][research_zaehringer_heller_2003]
- [Zakharov 1994][research_zakharov_1994]
- [Zalesak, Sr. 1981][research_zalesaksr_1981]
- [Zanchetta and Cain 1998][research_zanchetta_cain_1998]
- [Zander][research_zander]
- [Zapp and Bermejo-Moreno 2026][research_zapp_bermejomoreno_2026]
- [Zapp and Bermejo-Moreno 2026][research_zapp_bermejomoreno_2026_b]
- [Zarillo and Militello 1999][research_zarillo_militello_1999]
- [Zarlingo 1988][research_zarlingo_1988]
- [Zartarian 1956][research_zartarian_1956]
- [Zartarian and Hsu 1955][research_zartarian_hsu_1955]
- [Zeitoun et al 1991][research_zeitoun_colas_1991]
- [Zelinski et al 1960][research_zelinski_matthews_1960]
- [Zeng et al 2021][research_zeng_zhuang_2021]
- [Zeng et al 2025][research_zeng_wang_2025]
- [Zeng et al 2026][research_zeng_luo_2026]
- [Zeng et al 2026][research_zeng_wang_2026]
- [Zerilli and Armstrong 1992][research_zerilli_armstrong_1992]
- [Zettervall and Fureby 2018][research_zettervall_fureby_2018]
- [Zha et al 1998][research_zha_knight_1998]
- [Zha et al 1998][research_zha_knight_1998_b]
- [Zhai and Yang 2020][research_zhai_yang_2020]
- [Zhai et al 2016][research_zhai_qi_2016]
- [Zhai et al 2018][research_zhai_yang_2018]
- [Zhai et al 2020][research_zhai_zhang_2020]
- [Zhang 2015][research_zhang_2015]
- [Zhang 2020][research_zhang_2020]
- [Zhang 2020][research_zhang_2020_b]
- [Zhang 2020][research_zhang_2020_c]
- [Zhang 2020][research_zhang_2020_d]
- [Zhang 2020][research_zhang_2020_e]
- [Zhang 2020][research_zhang_2020_f]
- [Zhang 2020][research_zhang_2020_g]
- [Zhang and Chen 2011][research_zhang_chen_2011]
- [Zhang and Ding 2023][research_zhang_ding_2023]
- [Zhang and Tang 2012][research_zhang_tang_2012]
- [Zhang and Tang 2015][research_zhang_tang_2015]
- [Zhang et al 2012][research_zhang_fan_2012]
- [Zhang et al 2012][research_zhang_xu_2012]
- [Zhang et al 2015][research_zhang_yang_2015]
- [Zhang et al 2015][research_zhang_zhang_2015]
- [Zhang et al 2015][research_zhang_zhao_2015]
- [Zhang et al 2016][research_zhang_feng_2016]
- [Zhang et al 2016][research_zhang_feng_2016_b]
- [Zhang et al 2016][research_zhang_li_2016]
- [Zhang et al 2016][research_zhang_tan_2016]
- [Zhang et al 2016][research_zhang_tan_2016_b]
- [Zhang et al 2017][research_zhang_chang_2017]
- [Zhang et al 2017][research_zhang_he_2017]
- [Zhang et al 2017][research_zhang_liu_2017]
- [Zhang et al 2017][research_zhang_xia_2017]
- [Zhang et al 2018][research_zhang_liu_2018]
- [Zhang et al 2018][research_zhang_yu_2018]
- [Zhang et al 2019][research_zhang_wang_2019]
- [Zhang et al 2019][research_zhang_wang_2019_b]
- [Zhang et al 2019][research_zhang_yue_2019]
- [Zhang et al 2020][research_zhang_chen_2020]
- [Zhang et al 2021][research_zhang_ge_2021]
- [Zhang et al 2021][research_zhang_jin_2021]
- [Zhang et al 2022][research_zhang_huang_2022]
- [Zhang et al 2022][research_zhang_sun_2022]
- [Zhang et al 2022][research_zhang_xiong_2022]
- [Zhang et al 2022][research_zhang_xiong_2022_b]
- [Zhang et al 2022][research_zhang_zhang_2022]
- [Zhang et al 2022][research_zhang_zhang_2022_b]
- [Zhang et al 2023][research_zhang_chen_2023]
- [Zhang et al 2023][research_zhang_jing_2023]
- [Zhang et al 2023][research_zhang_ju_2023]
- [Zhang et al 2023][research_zhang_li_2023]
- [Zhang et al 2023][research_zhang_zhao_2023]
- [Zhang et al 2024][research_zhang_wang_2024]
- [Zhang et al 2024][research_zhang_xie_2024]
- [Zhang et al 2024][research_zhang_zhang_2024]
- [Zhang et al 2025][research_zhang_jingfeng_2025]
- [Zhang et al 2025][research_zhang_li_2025]
- [Zhang et al 2025][research_zhang_xie_2025]
- [Zhang et al 2026][research_zhang_chen_2026]
- [Zhang et al 2026][research_zhang_chen_2026_b]
- [Zhang et al 2026][research_zhang_chen_2026_c]
- [Zhang et al 2026][research_zhang_deng_2026]
- [Zhang et al 2026][research_zhang_liao_2026]
- [Zhang et al 2026][research_zhang_zong_2026]
- [Zhang et al 2026][research_zhang_zong_2026_b]
- [Zhang Zhikai et al 2015][research_zhangzhikai_duanguangren_2015]
- [Zhao 2011][research_zhao_2011]
- [Zhao 2013][research_zhao_2013]
- [Zhao 2021][research_zhao_2021]
- [Zhao 2021][research_zhao_2021_b]
- [Zhao 2021][research_zhao_2021_c]
- [Zhao 2021][research_zhao_2021_d]
- [Zhao 2021][research_zhao_2021_e]
- [Zhao 2023][research_zhao_2023]
- [Zhao 2023][research_zhao_2023_b]
- [Zhao et al 2009][research_zhao_zhang_2009]
- [Zhao et al 2011][research_zhao_qian_2011]
- [Zhao et al 2018][research_zhao_cai_2018]
- [Zhao et al 2018][research_zhao_xia_2018]
- [Zhao et al 2018][research_zhao_zhang_2018]
- [Zhao et al 2019][research_zhao_chen_2019]
- [Zhao et al 2019][research_zhao_sun_2019]
- [Zhao et al 2023][research_zhao_gao_2023]
- [Zhao et al 2023][research_zhao_tian_2023]
- [Zhao et al 2026][research_zhao_sha_2026]
- [Zhapbasbaev and Makashev 2003][research_zhapbasbaev_makashev_2003]
- [Zheltovodov and Knight 2011][research_zheltovodov_knight_2011]
- [Zheng and Bray 1994][research_zheng_bray_1994]
- [Zheng and Bray 1997][research_zheng_bray_1997]
- [Zheng et al 2013][research_zheng_chang_2013]
- [Zheng et al 2019][research_zheng_zhang_2019]
- [Zheng et al 2021][research_zheng_xiao_2021]
- [Zheng et al 2025][research_zheng_zhao_2025]
- [Zhengdong et al 2013][research_zhengdong_man_2013]
- [Zhi and Yang 2015][research_zhi_yang_2015]
- [Zhi et al 2015][research_zhi_liang_2015]
- [Zhikharev 1993][research_zhikharev_1993]
- [Zhong 2000][research_zhong_2000]
- [Zhong 2007][research_zhong_2007]
- [Zhong 2009][research_zhong_2009]
- [Zhong and Furumoto 1998][research_zhong_furumoto_1998]
- [Zhong and Lee 1996][research_zhong_lee_1996]
- [Zhong and Wu 2021][research_zhong_wu_2021]
- [Zhong et al 2001][research_zhong_whang_2001]
- [Zhongjie Meng et al 2008][research_zhongjiemeng_panfenghuang_2008]
- [Zhongjie Meng et al 2010][research_zhongjiemeng_jianzhongdong_2010]
- [Zhou 2018][research_zhou_2018]
- [Zhou 2023][research_zhou_2023]
- [Zhou and Davidson 1995][research_zhou_davidson_1995]
- [Zhou et al 2008][research_zhou_bao_2008]
- [Zhou et al 2016][research_zhou_gao_2016]
- [Zhou et al 2017][research_zhou_lu_2017]
- [Zhou et al 2017][research_zhou_teng_2017]
- [Zhou et al 2019][research_zhou_wang_2019]
- [Zhou et al 2020][research_zhou_liu_2020]
- [Zhou et al 2022][research_zhou_du_2022]
- [Zhou et al 2022][research_zhou_xu_2022]
- [Zhou et al 2023][research_zhou_li_2023]
- [Zhou et al 2025][research_zhou_tian_2025]
- [Zhou et al 2026][research_zhou_wang_2026]
- [Zhou et al 2026][research_zhou_zhang_2026]
- [Zhu and Li 2023][research_zhu_li_2023]
- [Zhu and Liu 2015][research_zhu_liu_2015]
- [Zhu and Liu 2015][research_zhu_liu_2015_b]
- [Zhu and Shen 2015][research_zhu_shen_2015]
- [Zhu and Xu 2017][research_zhu_xu_2017]
- [Zhu and Yin 2026][research_zhu_yin_2026]
- [Zhu et al 2016][research_zhu_zhao_2016]
- [Zhu et al 2020][research_zhu_luo_2020]
- [Zhu et al 2024][research_zhu_gao_2024]
- [Zhu et al 2025][research_zhu_chen_2025]
- [Zhu et al 2025][research_zhu_pethasethuraman_2025]
- [Zhu et al 2026][research_zhu_liu_2026]
- [Zinnecker et al 2012][research_zinnecker_serrani_2012]
- [Zivanovic 1963][research_zivanovic_1963]
- [Zoccoli 1977][research_zoccoli_1977]
- [Zohar R Hoter et al][research_zoharrhoter_gabrielcnastac]
- [Zolotukhin et al 2025][research_zolotukhin_price_2025]
- [Zope et al 2026][research_zope_bhushan_2026]
- [Zou et al 2021][research_zou_zhang_2021]
- [Zou et al 2026][research_zou_pan_2026]
- [Zou et al 2026][research_zou_pan_2026_b]
- [Zuchowski 2013][research_zuchowski_2013]
- [Zucro 1950][research_zucro_1950]
- [Zuo et al 2023][research_zuo_cui_2023]
- [Zweber et al 2002][research_zweber_kabis_2002]
- [Ösün et al 2026][research_osun_james_2026]

[research_1st_flight_1981]: https://doi.org/10.2514/mftc81
[research_4th_flight_1988]: https://doi.org/10.2514/mftc88
[research_a_2013]: https://doi.org/10.5772/52989
[research_a_computational_1994]: https://doi.org/10.2514/6.1994-2276
[research_a_global_1988]: https://doi.org/10.2514/6.1988-2164
[research_a_hypersonic_2002]: https://doi.org/10.2514/5.9781600866678.0499.0530
[research_a_hypersonic_2002_b]: https://doi.org/10.2514/5.9781600866678.0479.0497
[research_a_properties_2006]: https://doi.org/10.1002/9780470117859.app1
[research_aarnes_white_1975]: https://doi.org/10.2514/6.1975-1310
[research_aarnes_white_1975_b]: https://doi.org/10.2514/3.44438
[research_abarbanel_1977]: https://doi.org/10.21236/ada035568
[research_abbass_2024]: https://doi.org/10.61552/jmes.2024.02.002
[research_abbass_2024_b]: https://doi.org/10.2139/ssrn.4913830
[research_abdelsalam_carson_2004]: https://doi.org/10.2514/6.2004-2384
[research_abdelsalam_tiwari_2000]: https://doi.org/10.2514/6.2000-3709
[research_abdelsalam_tiwari_2001]: https://doi.org/10.2514/6.2001-2966
[research_abdelsalam_tiwari_2001_b]: https://doi.org/10.2514/6.2001-3194
[research_abdollahi_ranjbar_2024]: https://doi.org/10.1016/j.energy.2024.133089
[research_abdusalyamova_rakhmatov_2002]: https://doi.org/10.1023/a:1019691819784
[research_abedi_askari_2020]: https://doi.org/10.1016/j.ast.2019.105547
[research_abgrall_1991]: https://doi.org/10.1007/978-3-642-76527-8_74
[research_abhishek_ramachandra_2025]: https://doi.org/10.1007/978-981-96-4771-2_30
[research_abolhasani_lee_2024]: https://doi.org/10.2139/ssrn.5013871
[research_abolhassani_tiwari_1987]: https://doi.org/10.2514/6.1987-1169
[research_abouhweij_azizi_2020]: https://doi.org/10.1115/fedsm2020-20120
[research_abuaf_1976]: https://doi.org/10.21236/ada037674
[research_achambath_ramjatan_2019]: https://doi.org/10.2514/6.2019-1283
[research_acharya_2025]: https://doi.org/10.3390/aerospace12060503
[research_acharya_palies_2020]: https://doi.org/10.2514/6.2020-2434
[research_acheson_rothnie_2009]: https://doi.org/10.2514/6.2009-3632
[research_acton_2015]: https://doi.org/10.1080/08929882.2015.1087242
[research_adami_zhu_2007]: https://doi.org/10.2514/6.2007-6328
[research_adami_zhu_2008]: https://doi.org/10.2514/6.2008-7464
[research_adams_1967]: https://doi.org/10.2514/6.1967-226
[research_adams_1998]: https://doi.org/10.1007/s001620050102
[research_adams_johnc_1973]: https://doi.org/10.21236/ad0756499
[research_adams_rubin_1958]: https://doi.org/10.21236/ad0200634
[research_adamsjcjr_martindalewr_1976]: https://ntrs.nasa.gov/citations/19760054044
[research_adamsjr_martindale_1984]: https://doi.org/10.2514/6.1984-439
[research_aditya_balas_2016]: https://doi.org/10.1109/aero.2016.7500532
[research_adolph_1981]: https://doi.org/10.2514/6.1981-2487
[research_advancedfuelresearchinceasthartfordct_1957]: https://doi.org/10.21236/ada390317
[research_advisorygroupforaerospaceresearchanddevelopment_1993]: https://ntrs.nasa.gov/citations/19940024743
[research_advisorygroupforaerospaceresearchanddevelopment_1997]: https://ntrs.nasa.gov/citations/19980018672
[research_aerodynamic_heating_1979]: https://doi.org/10.2514/5.9781600865398.0192.0214
[research_aerothermodynamics_of_2001]: https://doi.org/10.2514/5.9781600866609.0569.0595
[research_aerothermodynamics_research_2002]: https://doi.org/10.2514/5.9781600866678.0205.0237
[research_aftosmis_baron_1989]: https://doi.org/10.2514/6.1989-1652
[research_agarwal_2002]: https://doi.org/10.21236/ada409344
[research_agarwal_2011]: https://doi.org/10.1080/10618562.2011.633490
[research_agarwal_deb_2001]: https://doi.org/10.1142/9789812810793_0013
[research_agnone_1987]: https://doi.org/10.2514/6.1987-159
[research_agostini_larcheveque_2013]: https://doi.org/10.1615/tsfp8.530
[research_agrawal_sepka_2012]: https://doi.org/10.2514/6.2012-3010
[research_aguilera_pang_2009]: https://doi.org/10.2514/6.2009-5415
[research_aguilera_yu_2017]: https://doi.org/10.1016/j.proci.2016.06.113
[research_aguileramunoz_yu_2014]: https://doi.org/10.2514/6.2014-3945
[research_ahmed_hossain_2025]: https://doi.org/10.1177/14680874251323414
[research_ahn_yu_2026]: https://doi.org/10.1016/j.measurement.2026.122820
[research_ahuja_hartfield_2008]: https://doi.org/10.2514/6.2008-5925
[research_ahuja_hartfield_2009]: https://doi.org/10.2514/6.2009-5195
[research_aiello_1962]: https://doi.org/10.21236/ad0294975
[research_aiello_1963]: https://doi.org/10.21236/ad0403486
[research_aiello_1977]: https://doi.org/10.1063/1.861687
[research_aiken_moore_2002]: https://doi.org/10.21236/ada628329
[research_aiken_moore_2003]: https://doi.org/10.21236/ada619759
[research_airbreathing_hypersonic_1997]: https://doi.org/10.2514/5.9781600866449.0297.0371
[research_airbreathing_propulsion]: https://doi.org/10.1007/978-0-8176-4438-3_11
[research_aircraft_and_2021]: https://doi.org/10.1002/9781118949818.ch3
[research_aircraft_flight]: https://doi.org/10.4271/air4094
[research_aircraft_flight_b]: https://doi.org/10.4271/air5273a
[research_aircraft_thermal]: https://doi.org/10.4271/air5744
[research_airforceflighttestcenteredwardsafbca_1970]: https://doi.org/10.21236/ada529707
[research_airforceflighttestcenteredwardsafbca_1974]: https://doi.org/10.21236/ada011561
[research_airforceflighttestcenteredwardsafbca_1974_b]: https://doi.org/10.21236/ada011562
[research_airforceflighttestcenteredwardsafbca_2002]: https://doi.org/10.21236/ada402888
[research_airforcetestpilotschooledwardsafbca_1962]: https://doi.org/10.21236/ada320208
[research_airforcetestpilotschooledwardsafbca_1987]: https://doi.org/10.21236/ada320212
[research_airforcetestpilotschooledwardsafbca_1990]: https://doi.org/10.21236/ada320062
[research_airforcetestpilotschooledwardsafbca_1990_b]: https://doi.org/10.21236/ada320058
[research_airforcetestpilotschooledwardsafbca_1993]: https://doi.org/10.21236/ada320063
[research_akihisa_kanda_2002]: https://doi.org/10.2514/2.6051
[research_aksonov_2023]: https://doi.org/10.15421/452303
[research_aksu_uslu_2017]: https://doi.org/10.2514/6.2017-0559
[research_ala_ye_2024]: https://doi.org/10.1115/icone31-135587
[research_alam_matsuo_2006]: https://doi.org/10.1299/jsmemecjo.2006.2.0_83
[research_albano_micheli_2013]: https://doi.org/10.1016/j.actaastro.2013.02.003
[research_alberico_1992]: https://doi.org/10.2514/6.1992-5076
[research_albertson_tartabini_2012]: https://doi.org/10.2514/6.2012-4863
[research_albertsoncindyw_emamisaied_2001]: https://ntrs.nasa.gov/citations/20010061808
[research_albertsoncindyw_emamisaied_2006]: https://ntrs.nasa.gov/citations/20060055388
[research_alex_lijo_2021]: https://doi.org/10.1115/imece2021-69420
[research_alexander_acharya_2024]: https://doi.org/10.2514/6.2024-3978
[research_alexander_acharya_2025]: https://doi.org/10.2514/6.2025-0097
[research_alferov_bushmin_2007]: https://doi.org/10.1134/s0018151x07030157
[research_alferov_dmitriev_2001]: https://doi.org/10.1023/a:1012376910053
[research_alferov_marchenko_2012]: https://doi.org/10.1134/s0018151x12040013
[research_alhussan_garris_2005]: https://doi.org/10.2514/6.2005-519
[research_ali_ahmed_2003]: https://doi.org/10.1007/s11630-003-0047-3
[research_ali_fujiwara_2000]: https://doi.org/10.1016/s0020-7225(99)00074-9
[research_ali_fujiwara_2005]: https://doi.org/10.1017/s0001924000000774
[research_alich_castillo_2007]: https://doi.org/10.2514/6.2007-1608
[research_alihussein_2019]: https://doi.org/10.36478/jeasci.2019.7241.7247
[research_alkamhawihani_greinertom_1990]: https://ntrs.nasa.gov/citations/19910003348
[research_alkandry_boyd_2009]: https://doi.org/10.2514/6.2009-3918
[research_allen_1964]: https://doi.org/10.2514/6.1964-543
[research_allen_hauser_2007]: https://doi.org/10.2514/6.2007-115
[research_allen_king_2005]: https://doi.org/10.2514/6.2005-4105
[research_alliney_dambrosio_2025]: https://doi.org/10.2514/6.2025-3436
[research_allouche_haoui_2006]: https://doi.org/10.2514/6.2006-8154
[research_almeida_2021]: https://doi.org/10.2514/6.2021-1566
[research_alsalihi_deconinck_1991]: https://doi.org/10.1007/978-3-642-76527-8_15
[research_alterstephenj_2012]: https://ntrs.nasa.gov/citations/20120014307
[research_altstatt_1977]: https://doi.org/10.21236/ada040023
[research_alvi_2005]: https://doi.org/10.21236/ada458295
[research_alvi_2012]: https://doi.org/10.21236/ada563916
[research_amati_bruno_2008]: https://doi.org/10.1016/j.energy.2007.08.012
[research_amato_giannino_2026]: https://doi.org/10.2514/6.2026-5098
[research_ambeverma_muraripandey_2021]: https://doi.org/10.1016/j.energy.2020.119511
[research_ambeverma_muraripandey_2021_b]: https://doi.org/10.1016/j.matpr.2020.11.787
[research_amemiya_toriyama_2018]: https://doi.org/10.1299/jsmeyamanashi.2018.yc2018-092
[research_ames_tang_2021]: https://doi.org/10.1201/9781003042945-4
[research_an_assessment_1964]: https://doi.org/10.1016/b978-1-4831-9828-6.50041-2
[research_an_ultrasonic_1974]: https://doi.org/10.2514/5.9781600865077.0437.0452
[research_an_wang_2017]: https://doi.org/10.1016/j.actaastro.2017.06.026
[research_an_wang_2021]: https://doi.org/10.1016/j.ast.2021.106951
[research_an_yang_2020]: https://doi.org/10.1016/j.combustflame.2019.10.030
[research_analysis_on_1998]: https://doi.org/10.1016/s0140-6701(98)93953-4
[research_ananthapadmanaban]: https://doi.org/10.14264/243832b
[research_ananthapadmanaban_murganandam_2016]: https://doi.org/10.2514/6.2016-5072
[research_anderson_1958]: https://doi.org/10.21236/ad0305026
[research_anderson_1959]: https://doi.org/10.21236/ad0312275
[research_anderson_1960]: https://doi.org/10.21236/ad0315671
[research_anderson_1990]: https://doi.org/10.2514/6.1990-2151
[research_anderson_1996]: https://doi.org/10.1002/9780470172636.ch10
[research_anderson_2014]: https://doi.org/10.2514/6.2014-3799
[research_anderson_2019]: https://doi.org/10.2514/4.105142
[research_anderson_brown_1999]: https://doi.org/10.2514/6.1999-822
[research_andersonjr_2006]: https://doi.org/10.2514/4.861956
[research_andreadisdean_drakealan_2002]: https://ntrs.nasa.gov/citations/20030068741
[research_andreadisdean_drakealan_2003]: https://ntrs.nasa.gov/citations/20030067926
[research_andrews_gordon_1981]: https://doi.org/10.2514/6.1981-2452
[research_andrews_poggie_2023]: https://doi.org/10.2514/6.2023-3555
[research_andrews_trexler_1994]: https://doi.org/10.2514/6.1994-2817
[research_anhtuandngo]: https://doi.org/10.1109/aero.2004.1368066
[research_annecharmeau_brandoncunningham_2009]: https://doi.org/10.2172/950459
[research_anthoine_lestrade_2014]: https://doi.org/10.2514/6.2014-3951
[research_antonioferri_1964]: https://ntrs.nasa.gov/citations/19780002064
[research_appar_kumar_2021]: https://doi.org/10.1080/10618562.2021.2017900
[research_appeldoorn_tao_1966]: https://doi.org/10.21236/ad0808673
[research_appeldoorn_tao_1967]: https://doi.org/10.21236/ad0822760
[research_appendix_a_2011]: https://doi.org/10.1515/9781400839063-017
[research_appendix_a_2021]: https://doi.org/10.1002/9781118949818.app1
[research_appendix_b_2003]: https://doi.org/10.2514/5.9781600862069.0573.0576
[research_appendix_c_2015]: https://doi.org/10.1201/9781315148076-38
[research_appleby_adams_1991]: https://doi.org/10.2514/6.1991-2689
[research_approximate_method_1983]: https://doi.org/10.2514/5.9781600865626.0021.0053
[research_aprovitola_iuspa_2019]: https://doi.org/10.5772/intechopen.85603
[research_arad_2024]: https://doi.org/10.2514/6.2024-3894
[research_arad_2026]: https://doi.org/10.2514/6.2026-4173
[research_arai_taguchi_2008]: https://doi.org/10.2514/6.2008-2579
[research_araujo_tanaka_2024]: https://doi.org/10.1063/5.0181366
[research_ardemamarkd_1995]: https://ntrs.nasa.gov/citations/19960000793
[research_ardonceau_1984]: https://doi.org/10.2514/3.48565
[research_arens_1961]: https://doi.org/10.4271/610076
[research_arent_falatko_1992]: https://doi.org/10.2514/6.1992-4099
[research_armstrong_1979]: https://doi.org/10.21236/ada063518
[research_armstrong_latimer_1969]: https://doi.org/10.21236/ad0691227
[research_armywarcollcarlislebarrackspa_1952]: https://doi.org/10.21236/ada390507
[research_arnold_1981]: https://doi.org/10.2514/6.1981-2444
[research_arnold_pace_2023]: https://doi.org/10.2514/6.2023-0926
[research_aronov_klyagin_2021]: https://doi.org/10.34759/tpt-2021-13-10-456-466
[research_arons_macnair_1970]: https://doi.org/10.21236/ad0722913
[research_asami_1999]: https://doi.org/10.5359/jawe.1999.49
[research_asma_tirtey_2009]: https://doi.org/10.2514/6.2009-3944
[research_asma_vanderhaegen_2010]: https://doi.org/10.2514/6.2010-4963
[research_aso_hayashi_2002]: https://doi.org/10.2514/6.2002-646
[research_aso_kumamoto_1993]: https://doi.org/10.2514/6.1993-2984
[research_aso_okuyama_1992]: https://doi.org/10.1007/978-3-642-77648-9_110
[research_aso_tani_2018]: https://doi.org/10.2514/6.2018-0278
[research_assessment_of_1992]: https://doi.org/10.2514/5.9781600866128.0059.0091
[research_assis_suppandipillai_2019]: https://doi.org/10.1515/tjj-2019-0022
[research_atay_kumartaslioglu_2026]: https://doi.org/10.2514/6.2026-5130
[research_atkins_2026]: https://doi.org/10.2514/6.2026-115362
[research_atmosphere_standard_2006]: https://doi.org/10.1007/978-0-387-30160-0_849
[research_attar_vanderlee_2026]: https://doi.org/10.2514/6.2026-0596
[research_aubrey_speer_1983]: https://doi.org/10.21236/ada131388
[research_august_joshi_1997]: https://doi.org/10.1117/12.274702
[research_aultgm_1965]: https://ntrs.nasa.gov/citations/19660037210
[research_auslender_suder_2009]: https://doi.org/10.2514/6.2009-7277
[research_austin]: https://doi.org/10.14264/105958
[research_autenrieb_2023]: https://doi.org/10.2514/6.2023-1997
[research_autenrieb_fezans_2024]: https://doi.org/10.1007/s12567-024-00544-0
[research_automatic_detection_1974]: https://doi.org/10.2514/5.9781600865077.0453.0460
[research_auxer_1968]: https://doi.org/10.2514/6.1968-673
[research_avasalidineshkumar_mrsvsaritha_2026]: https://doi.org/10.62643/ijerst.2026.v22.n3.4211
[research_avcilar_celik_2026]: https://doi.org/10.2514/6.2026-5057
[research_averyde_1981]: https://ntrs.nasa.gov/citations/19810012587
[research_avidor_lederman_1971]: https://doi.org/10.21236/ad0729798
[research_axdahl_kumar_2011]: https://doi.org/10.2514/6.2011-5790
[research_axdahl_kumar_2012]: https://doi.org/10.2514/6.2012-3924
[research_azevedo_korzenowski_1998]: https://doi.org/10.2514/6.1998-2629
[research_b_2011]: https://doi.org/10.5772/13890
[research_b_34_u_1963]: https://doi.org/10.1016/0019-1035(63)90063-0
[research_babinsky_2002]: https://doi.org/10.1007/978-3-540-45856-2_5
[research_babinsky_2007]: https://doi.org/10.21236/ada476419
[research_babinsky_2014]: https://doi.org/10.21236/ada602774
[research_babinsky_delery_2011]: https://doi.org/10.1017/cbo9780511842757.003
[research_babu_2020]: https://doi.org/10.1007/978-3-030-60819-4_7
[research_babu_2021]: https://doi.org/10.1007/978-3-030-79945-8_8
[research_bac_1993]: https://doi.org/10.1016/b978-0-08-040999-3.50008-4
[research_baccarella_liu_2020]: https://doi.org/10.2514/6.2020-2428
[research_bachchan_hillier_2004]: https://doi.org/10.2514/6.2004-5380
[research_baer_1961]: https://doi.org/10.21236/ad0261501
[research_baer_1966]: https://doi.org/10.21236/ad0477832
[research_baganoff_1990]: https://doi.org/10.21236/ada222704
[research_bagaveyev_bhagwandin_2010]: https://doi.org/10.2514/6.2010-942
[research_bahambari_khankalantary_2023]: https://doi.org/10.1109/icee59167.2023.10334860
[research_bahmcatherine_baumannethan_2005]: https://ntrs.nasa.gov/citations/20050182778
[research_bahuguna_kolluru_2023]: https://doi.org/10.2514/6.2023-3055
[research_bai_ren_2014]: https://doi.org/10.1109/chicc.2014.6896993
[research_bakos]: https://doi.org/10.14264/366376
[research_balachandar_2003]: https://doi.org/10.2514/6.2003-3700
[research_balaji_venkatasubbaiah_2025]: https://doi.org/10.1016/j.euromechflu.2025.204290
[research_balajihimakar_rao_2025]: https://doi.org/10.1007/978-981-96-4771-2_37
[research_balakrishnan_shen_1997]: https://doi.org/10.2514/6.1997-3531
[research_balent_kutschenreuterjr_1964]: https://doi.org/10.2514/6.1964-540
[research_ball_syberg_1981]: https://doi.org/10.2514/6.1981-1397
[research_balland_fernandezvillace_2015]: https://doi.org/10.2514/6.2015-3557
[research_balland_vincentrandonnier_2015]: https://doi.org/10.2514/6.2015-3629
[research_ballaro_andersonjr_1991]: https://doi.org/10.2514/6.1991-250
[research_ban_zhang_2026]: https://doi.org/10.1016/j.combustflame.2025.114620
[research_bano_fraser_2026]: https://doi.org/10.2514/6.2026-5113
[research_bansal_modest_2010]: https://doi.org/10.2514/6.2010-234
[research_bansal_modest_2010_b]: https://doi.org/10.1615/ichmt.2010.rad-6.330
[research_bao_duan_2013]: https://doi.org/10.1177/0954410013479730
[research_bao_li_2010]: https://doi.org/10.1016/j.actaastro.2010.04.022
[research_bao_li_2012]: https://doi.org/10.1016/j.applthermaleng.2011.09.036
[research_bao_wang_2021]: https://doi.org/10.1016/j.cja.2020.11.009
[research_bao_zhou_2017]: https://doi.org/10.1016/j.actaastro.2016.11.046
[research_baranovskii_levin_1990]: https://doi.org/10.2514/6.1990-5268
[research_baranovskii_levin_1991]: https://doi.org/10.2514/6.1991-5094
[research_barber_cox_1989]: https://doi.org/10.2514/3.23181
[research_barber_coxjr_1988]: https://doi.org/10.2514/6.1988-475
[research_barber_heitt_2006]: https://doi.org/10.2514/6.2006-123
[research_barber_orszag_1997]: https://doi.org/10.2514/6.1997-2638
[research_barbera_1980]: https://doi.org/10.2514/6.1980-1576
[research_barberis_molton_1995]: https://doi.org/10.2514/6.1995-227
[research_bardina_lombard_1987]: https://doi.org/10.2514/6.1987-1114
[research_barlow_wood_1987]: https://doi.org/10.2514/6.1987-1870
[research_barlow_wood_1988]: https://doi.org/10.2514/6.1988-2975
[research_barnes_segal_2015]: https://doi.org/10.1016/j.paerosci.2015.04.002
[research_barnett_starrett_1994]: https://doi.org/10.21236/ada281582
[research_barnhart_greber_1988]: https://doi.org/10.2514/6.1988-308
[research_baron_efrat_1979]: https://doi.org/10.21236/ada068819
[research_barone_nicholson_2022]: https://doi.org/10.1103/physrevfluids.7.084604
[research_barr_figueroa_2026]: https://doi.org/10.2514/6.2026-1691
[research_barreto_freire_2021]: https://doi.org/10.26678/abcm.cobem2021.cob2021-0572
[research_barrett_1963]: https://doi.org/10.2514/3.2141
[research_barrett_2025]: https://doi.org/10.12783/ballistics25/37108
[research_barth]: https://doi.org/10.14264/uql.2014.614
[research_barth_wheatley_2014]: https://doi.org/10.2514/6.2014-1159
[research_bartolomecalvo_eggers_2011]: https://doi.org/10.2514/6.2011-2323
[research_bartusiak_hao_2022]: https://doi.org/10.1109/aero53065.2022.9843362
[research_baruzzi_karchani_2021]: https://doi.org/10.1080/10618562.2021.1967620
[research_barz_2026]: https://doi.org/10.2514/6.2026-5022
[research_barzegargerdroodbary_2020]: https://doi.org/10.1016/b978-0-12-821138-0.00003-3
[research_bas_2026]: https://doi.org/10.54287/gujsa.1810054
[research_batcho_sullivan_1988]: https://doi.org/10.2514/6.1988-307
[research_bates_2004]: https://doi.org/10.2514/1.6241
[research_bates_maas_2004]: https://doi.org/10.21236/ada422733
[research_batill_hoffman_1984]: https://doi.org/10.2514/6.1984-416
[research_bauer_1966]: https://doi.org/10.2514/6.1966-648
[research_bauer_1967]: https://doi.org/10.21236/ad0650950
[research_bauer_2004]: https://doi.org/10.1063/1.1780435
[research_bauer_muse_1974]: https://doi.org/10.21236/ad0783244
[research_bauer_petters_1998]: https://doi.org/10.2514/6.1998-3426
[research_baumberger_peterson_2026]: https://doi.org/10.2514/6.2026-4105
[research_baurle_eklund_2001]: https://doi.org/10.2514/6.2001-3299
[research_baurle_gruber_1998]: https://doi.org/10.2514/6.1998-938
[research_baurle_mathur_1998]: https://doi.org/10.2514/6.1998-3121
[research_bayewallace_krouse_2022]: https://doi.org/10.2514/6.2022-0402
[research_baysal_luo_1998]: https://doi.org/10.2514/6.1998-2412
[research_bedanandmandal_2025]: https://doi.org/10.61359/11.2106-2554
[research_bedarev_fedorova_2001]: https://doi.org/10.1007/978-3-642-56535-9_130
[research_beery_clodfelter_1975]: https://doi.org/10.21236/ada016763
[research_bein_friedmann_1993]: https://doi.org/10.2514/6.1993-1318
[research_bejan_2010]: https://doi.org/10.21236/ada593178
[research_beketaeva_moisseyeva_2016]: https://doi.org/10.1134/s0869864316020037
[research_bell_1993]: https://doi.org/10.2172/1031792
[research_bellan_2012]: https://doi.org/10.21236/ada559334
[research_benarosh_natan_1997]: https://doi.org/10.2514/6.1997-3119
[research_benarosh_natan_1998]: https://doi.org/10.1515/tjj.1998.15.3.223
[research_benarosh_natan_1999]: https://doi.org/10.1016/s0094-5765(99)00113-7
[research_benay_2003]: https://doi.org/10.2514/6.2003-6966
[research_benay_pot_1986]: https://doi.org/10.1007/978-3-642-82770-9_22
[research_bencze_1972]: https://doi.org/10.2514/6.1972-1113
[research_bencze_sorensen_1970]: https://doi.org/10.2514/6.1970-687
[research_bender_1969]: https://doi.org/10.2514/6.1969-318
[research_bendixcorpeatontownnj_1963]: https://doi.org/10.21236/ad0402679
[research_bendor_1978]: https://doi.org/10.21236/ada068759
[research_bendor_1978_b]: https://doi.org/10.21236/ada064967
[research_bendor_2001]: https://doi.org/10.1016/b978-012086430-0/50022-1
[research_bendot_harkins_1975]: https://doi.org/10.21236/ada016430
[research_benjellountouimi_doom_2025]: https://doi.org/10.2514/6.2025-2257
[research_bennett_1971]: https://doi.org/10.2514/6.1971-327
[research_bennett_connors_1964]: https://doi.org/10.2514/6.1964-669
[research_bennett_edwards_1990]: https://doi.org/10.2514/6.1990-1493
[research_bensassi_lani_2010]: https://doi.org/10.2514/6.2010-4857
[research_bensassi_lani_2013]: https://doi.org/10.2514/6.2013-2694
[research_benson_liou_2009]: https://doi.org/10.2514/6.2009-711
[research_benson_maslowe_1965]: https://doi.org/10.2514/6.1965-617
[research_benson_mcrae_1993]: https://doi.org/10.2514/6.1993-2239
[research_benson_sedgwick_1976]: https://doi.org/10.2514/6.1976-756
[research_benstein_1989]: https://doi.org/10.2514/6.1989-2471
[research_benton_1990]: https://doi.org/10.2514/6.1990-297
[research_benyakar_hanson_1999]: https://doi.org/10.2514/6.1999-484
[research_berens_bissinger_1996]: https://doi.org/10.2514/6.1996-4531
[research_berens_bissinger_1998]: https://doi.org/10.2514/3.26994
[research_berens_bissinger_1998_b]: https://doi.org/10.2514/6.1998-1574
[research_berezovik_tikhonov_1980]: https://doi.org/10.1007/bf00693258
[research_berger_1971]: https://doi.org/10.2514/6.1971-1723
[research_berger_gourdain_2019]: https://doi.org/10.2514/6.2019-3497
[research_bergholz_hitch_1992]: https://doi.org/10.2514/6.1992-515
[research_bergier]: https://doi.org/10.70675/6e6752d9z395bz4da8z8691z37734dd62f09
[research_berglund_fedina_2010]: https://doi.org/10.2514/1.43746
[research_berglund_fureby_2007]: https://doi.org/10.1016/j.proci.2006.07.074
[research_berkner_1990]: https://doi.org/10.21236/adb159687
[research_berkovits_1973]: https://doi.org/10.2514/6.1973-386
[research_bertelrud_budd_1999]: https://doi.org/10.2514/6.1999-4849
[research_bertelrud_kolodziej_1992]: https://doi.org/10.2514/6.1992-4104
[research_berthelot_1994]: https://doi.org/10.21236/ada276955
[research_berthelot_craft_2026]: https://doi.org/10.2514/6.2026-112174
[research_berthold_iii_1976]: https://doi.org/10.21236/ada339211
[research_bertin_towne_1997]: https://doi.org/10.2514/6.1997-766
[research_besserer_1952]: https://doi.org/10.21236/ad0036272
[research_best_fetterhoff_2001]: https://doi.org/10.2514/6.2001-1859
[research_bestion_2017]: https://doi.org/10.1016/b978-0-08-100662-7.00011-7
[research_bestion_2024]: https://doi.org/10.1016/b978-0-323-85610-2.00019-3
[research_bestman_1991]: https://doi.org/10.1007/bf00646939
[research_bettis_hosder_2010]: https://doi.org/10.2514/6.2010-4642
[research_bever_1992]: https://doi.org/10.2514/6.1992-4113
[research_bezerra_desouza_2026]: https://doi.org/10.1007/s40430-026-06600-6
[research_bezerra_souza_2024]: https://doi.org/10.2139/ssrn.4919975
[research_bhagwandin_despirito_2011]: https://doi.org/10.2514/6.2011-859
[research_bhagwandin_engblom_2009]: https://doi.org/10.2514/6.2009-5382
[research_bhagwandin_sahu_2023]: https://doi.org/10.21236/ad1216596
[research_bhakta_sims_2025]: https://doi.org/10.2172/3362909
[research_bhanderi_babinsky_2005]: https://doi.org/10.2514/6.2005-4896
[research_bhat_lind_2009]: https://doi.org/10.1109/acc.2009.5160180
[research_bhatia_sirignano_1990]: https://doi.org/10.2514/6.1990-271
[research_bhungalia_zweber_2000]: https://doi.org/10.1115/detc2000/dac-14267
[research_bhutta_lewis_1988]: https://doi.org/10.2514/6.1988-2568
[research_biagioni_scortecci_1998]: https://doi.org/10.2514/6.1998-1508
[research_bielawski_2026]: https://doi.org/10.2514/6.2026-2736
[research_biennial_flight_1994]: https://doi.org/10.2514/mbft94
[research_biggi_abdelnour_2024]: https://doi.org/10.2514/6.2024-1491
[research_bilchenko_2015]: https://doi.org/10.1109/scp.2015.7342145
[research_billig_1967]: https://doi.org/10.21236/ad0655460
[research_billig_1992]: https://doi.org/10.2514/6.1992-1
[research_billig_1993]: https://doi.org/10.2514/6.1993-2329
[research_billig_1995]: https://doi.org/10.2514/3.23952
[research_billig_waltrup_1979]: https://doi.org/10.2514/6.1979-7044
[research_billigfs_1967]: https://ntrs.nasa.gov/citations/19670024055
[research_billigfs_grenleskise_1970]: https://ntrs.nasa.gov/citations/19710034788
[research_billingsley_edwards_2010]: https://doi.org/10.21236/ada556024
[research_bin_hongxin_2006]: https://doi.org/10.1109/chicc.2006.4346800
[research_bing_gong_2015]: https://doi.org/10.2514/6.2015-3641
[research_birrer_stemmer_2012]: https://doi.org/10.1051/eucass/201203267
[research_birzer_doolan_2007]: https://doi.org/10.2514/6.2007-4314
[research_bissinger_blagoveshchensky_1998]: https://doi.org/10.1016/s1270-9638(99)80009-1
[research_bissinger_schmitz_1993]: https://doi.org/10.2514/6.1993-5042
[research_bityurin_bocharov_2010]: https://doi.org/10.1134/s0018151x10060143
[research_blaine_keeling_2005]: https://doi.org/10.5194/acpd-5-11899-2005
[research_blanchard_1983]: https://doi.org/10.1119/1.2341299
[research_blankson_hagseth_1993]: https://doi.org/10.2514/6.1993-506
[research_blankson_lewis_1998]: https://doi.org/10.2514/6.1998-1550
[research_bleimeyer_1981]: https://doi.org/10.2514/6.1981-2515
[research_blossermaxl_1988]: https://ntrs.nasa.gov/citations/19880013054
[research_blosserml_1987]: https://ntrs.nasa.gov/citations/19870018635
[research_blosserml_mcwitheyrr_1983]: https://ntrs.nasa.gov/citations/19840005546
[research_blum_2006]: https://doi.org/10.21236/ada448163
[research_bodryakov_2014]: https://doi.org/10.1134/s0018151x14040051
[research_bodryakov_2015]: https://doi.org/10.1134/s0018151x15040069
[research_bodryakov_2018]: https://doi.org/10.1134/s0018151x18020049
[research_boeing_to_2005]: https://doi.org/10.1108/aeat.2005.12777baf.006
[research_boeingscientificresearchlabsseattlewa_1963]: https://doi.org/10.21236/ad0414555
[research_boettinger_1988]: https://doi.org/10.21236/ada202614
[research_bogart_breckenridge_1981]: https://doi.org/10.21236/ada106728
[research_bogdanoff_christiansen_1978]: https://doi.org/10.21236/ada062390
[research_bogdnoff_1953]: https://doi.org/10.21236/ad0009823
[research_bogdonoff_1970]: https://doi.org/10.21236/ad0708757
[research_bogdonoff_1990]: https://doi.org/10.2514/6.1990-766
[research_bogdonoff_1999]: https://doi.org/10.21236/ada370547
[research_bogi_vinay_2025]: https://doi.org/10.2514/6.2025-0945
[research_bogue_1992]: https://doi.org/10.2514/6.1992-4086
[research_bogue_bagley_1995]: https://doi.org/10.1117/12.211479
[research_bohning_doerffer_2002]: https://doi.org/10.1007/978-3-540-45856-2_4
[research_boiocchi_galfetti_2018]: https://doi.org/10.2514/1.b36307
[research_boirun_1979]: https://doi.org/10.4050/jahs.24.51
[research_bokor_chamarthi_2026]: https://doi.org/10.2514/6.2026-0993
[research_boland_hinkle_2023]: https://doi.org/10.2514/6.2023-3694
[research_bolender_doman_2005]: https://doi.org/10.21236/ada444974
[research_bolender_doman_2006]: https://doi.org/10.2514/6.2006-6646
[research_bolender_oppenheimer_2007]: https://doi.org/10.2514/6.2007-6397
[research_bolender_wilkin_2009]: https://doi.org/10.2514/6.2009-7292
[research_boles_milligan_2013]: https://doi.org/10.21236/ada586382
[research_bolt_1981]: https://doi.org/10.2514/6.1981-2394
[research_bonanni_ihme_2023]: https://doi.org/10.2514/6.2023-1466
[research_bonavita_zollars_2026]: https://doi.org/10.2514/1.c038065
[research_bonelli_cutrone_2011]: https://doi.org/10.2514/6.2011-2319
[research_bonnefond_falempin_1996]: https://doi.org/10.2514/6.1996-4490
[research_bonnell_2000]: https://doi.org/10.21236/ada383580
[research_boon_hillier_2006]: https://doi.org/10.2514/6.2006-3036
[research_boon_hillier_2006_b]: https://doi.org/10.2514/6.2006-12
[research_bootle_1999]: https://doi.org/10.21236/ada379694
[research_boppe_davis_1989]: https://doi.org/10.4271/892345
[research_bordelon_frost_2003]: https://doi.org/10.2514/6.2003-4227
[research_bordoloi_pandey_2021]: https://doi.org/10.1016/j.matpr.2020.12.669
[research_bordoloi_pandey_2022]: https://doi.org/10.1615/interjfluidmechres.2022043291
[research_bordoloi_pandey_2022_b]: https://doi.org/10.2139/ssrn.4051685
[research_borelli_repetto_2018]: https://doi.org/10.1016/j.tsep.2018.03.002
[research_borg_adamczak_2025]: https://doi.org/10.2514/6.2025-0733
[research_borg_kimmel_2012]: https://doi.org/10.2514/6.2012-2821
[research_borg_kimmel_2013]: https://doi.org/10.2514/6.2013-2737
[research_bormotova_volodin_2003]: https://doi.org/10.1023/a:1024259130915
[research_borovikov_gavriliouk_1996]: https://doi.org/10.2514/6.1996-4549
[research_borovoi_chinilov_1996]: https://doi.org/10.2514/6.1996-2046
[research_borovoy_egorov_2015]: https://doi.org/10.1051/eucass/201507419
[research_borrelli_marini_1998]: https://doi.org/10.2514/6.1998-1577
[research_bortner_1964]: https://doi.org/10.21236/ad0603437
[research_bose_2012]: https://doi.org/10.1007/978-1-4614-3532-7
[research_boswell_sutherland_2004]: https://doi.org/10.1063/1.1803579
[research_bouazzi_ali_2025]: https://doi.org/10.1016/j.ijhydene.2025.03.078
[research_bouchard_chambers_1966]: https://doi.org/10.21236/ad0632234
[research_bouchez_2001]: https://doi.org/10.2514/6.2001-1918
[research_bouchez_beyer_2005]: https://doi.org/10.2514/6.2005-3434
[research_bouchez_beyer_2006]: https://doi.org/10.2514/6.2006-8072
[research_bouchez_beyer_2008]: https://doi.org/10.2514/6.2008-2626
[research_bouchez_beyer_2009]: https://doi.org/10.1051/eucass/200901627
[research_bouchez_cahuzac_2004]: https://doi.org/10.2514/6.2004-3653
[research_bouchez_levine_2003]: https://doi.org/10.2514/6.2003-7004
[research_bouchez_montazel_1998]: https://doi.org/10.2514/6.1998-3729
[research_bouchez_perillat_2011]: https://doi.org/10.2514/6.2011-2313
[research_bouchez_roudakov_2005]: https://doi.org/10.2514/6.2005-3320
[research_boudreau_smithiii_1993]: https://doi.org/10.2514/6.1993-5121
[research_boulal_genot_2026]: https://doi.org/10.1016/j.combustflame.2025.114535
[research_boulal_lepichon_2026]: https://doi.org/10.1016/j.proci.2026.106124
[research_bourgoing_benay_2005]: https://doi.org/10.5589/q05-007
[research_bowcutt_2001]: https://doi.org/10.2514/2.5893
[research_bowcutt_haney_1995]: https://doi.org/10.2514/6.1995-850
[research_bowes_1978]: https://doi.org/10.21236/ada058197
[research_bowles_1980]: https://doi.org/10.21236/ada389393
[research_bowles_roberts_1998]: https://doi.org/10.2514/6.1998-1610
[research_bowman_1995]: https://doi.org/10.21236/ada297936
[research_bowman_foy_1961]: https://doi.org/10.21236/ad0267505
[research_bowman_hanson_1990]: https://doi.org/10.21236/ada221793
[research_bowman_hanson_1991]: https://doi.org/10.21236/ada236759
[research_bowman_hanson_1992]: https://doi.org/10.21236/ada251065
[research_bowman_hanson_1997]: https://doi.org/10.21236/ada325760
[research_bowman_nereson_1974]: https://doi.org/10.1063/1.2945933
[research_boyce_gerard_2003]: https://doi.org/10.2514/6.2003-7029
[research_boyce_paull_2001]: https://doi.org/10.2514/6.2001-1891
[research_boyd_1990]: https://doi.org/10.2514/6.1990-145
[research_boyd_1999]: https://doi.org/10.2514/6.1999-3634
[research_boyd_2001]: https://doi.org/10.1142/9789812811882_0003
[research_boyd_2002]: https://doi.org/10.21236/ada414031
[research_boyd_2004]: https://doi.org/10.21236/ada422121
[research_boyd_2008]: https://doi.org/10.21236/ada573606
[research_boyd_2013]: https://doi.org/10.2514/6.2013-2557
[research_boyd_2015]: https://doi.org/10.2514/5.9781624103292.0045.0102
[research_boyd_2024]: https://doi.org/10.52843/cassyni.fzpzjb
[research_boyd_phamvandiep_1993]: https://doi.org/10.2514/6.1993-2871
[research_boyer_1965]: https://doi.org/10.21236/ad0621447
[research_boyer_eschenroeder_1960]: https://doi.org/10.21236/ad0246226
[research_brabbstheodorea_robertsonthomasf_1987]: https://ntrs.nasa.gov/citations/19880005654
[research_bradford_olds_1999]: https://doi.org/10.2514/6.1999-2104
[research_bradley_magee_1995]: https://doi.org/10.2514/6.1995-624
[research_bradley_siemersiii_1981]: https://doi.org/10.2514/6.1981-2477
[research_brahmachary_ogawa_2021]: https://doi.org/10.2514/6.2021-1960
[research_braun_hammack_2025]: https://doi.org/10.2514/1.b39579
[research_braun_hammack_2025_b]: https://doi.org/10.2514/6.2025-1529
[research_braun_hassan_2026]: https://doi.org/10.1016/j.proci.2026.106149
[research_bravo_plewacki_2025]: https://doi.org/10.2139/ssrn.5759944
[research_breitsamter_laschka_2001]: https://doi.org/10.2514/6.2001-1811
[research_brenneis_wanie_1991]: https://doi.org/10.2514/6.1991-2472
[research_bretherton]: https://doi.org/10.14264/64f3ccb
[research_briardy_head_1968]: https://doi.org/10.21236/ad0673964
[research_bricker_numbers_1989]: https://doi.org/10.2514/6.1989-2353
[research_brief_review_2024]: https://doi.org/10.1002/9781119910381.ch3
[research_brieschenk_obyrne_2013]: https://doi.org/10.1016/j.combustflame.2012.08.011
[research_brinda_dasgupta_2006]: https://doi.org/10.2514/6.2006-7997
[research_britcher_landman_2024]: https://doi.org/10.1016/b978-0-12-818099-0.00009-4
[research_britcher_landman_2024_b]: https://doi.org/10.1016/b978-0-12-818099-0.00012-4
[research_britcher_landman_2024_c]: https://doi.org/10.1016/b978-0-12-818099-0.00022-7
[research_britcher_landman_2024_d]: https://doi.org/10.1016/b978-0-12-818099-0.00017-3
[research_britcher_landman_2024_e]: https://doi.org/10.1016/b978-0-12-818099-0.00002-1
[research_britcher_landman_2024_f]: https://doi.org/10.1016/b978-0-12-818099-0.00011-2
[research_brits]: https://doi.org/10.14264/6ce91dd
[research_broadaway_1984]: https://doi.org/10.2514/6.1984-85
[research_brocanelli_gunbatar_2012]: https://doi.org/10.2514/6.2012-4698
[research_brociek_hetmaniok_2023]: https://doi.org/10.1016/j.applthermaleng.2022.119405
[research_brockmann_stefanovich_2022]: https://doi.org/10.55163/bdyx5243
[research_brodsky_1970]: https://doi.org/10.21236/ad0716026
[research_brodykbessire]: https://ntrs.nasa.gov/citations/20240012307
[research_bronnikov_vettegren_1997]: https://doi.org/10.1068/htec34
[research_brooke_1957]: https://doi.org/10.21236/ad0154531
[research_brooks_1986]: https://doi.org/10.2514/6.1986-9796
[research_brophy_hawk_1990]: https://doi.org/10.21236/ada378098
[research_brown_1978]: https://doi.org/10.2514/6.1978-1049
[research_brown_2012]: https://doi.org/10.31274/ahac.8318
[research_brown_boyce_2012]: https://doi.org/10.2514/6.2012-5890
[research_brown_bradley_1981]: https://doi.org/10.2514/6.1981-2390
[research_brown_donbar_2013]: https://doi.org/10.21236/ada578570
[research_brown_donbar_2015]: https://doi.org/10.21236/ada613800
[research_brown_kramer_1963]: https://doi.org/10.21236/ad0435740
[research_brown_kussoy_1986]: https://doi.org/10.1007/978-3-642-82770-9_12
[research_brown_ravichandran_2013]: https://doi.org/10.1007/s00193-013-0484-1
[research_brown_williams_2010]: https://doi.org/10.21236/ada522512
[research_browne_rasmussen_2021]: https://doi.org/10.2514/6.2021-0049
[research_brownjamesl_2014]: https://ntrs.nasa.gov/citations/20140011158
[research_brummund_scheel_2002]: https://doi.org/10.1615/intjenergeticmaterialschemprop.v5.i1-6.790
[research_brune_hosder_2016]: https://doi.org/10.2514/6.2016-3535
[research_brunner_1959]: https://doi.org/10.1115/1.4008191
[research_bruno_1989]: https://doi.org/10.1007/978-1-4684-9187-6_7
[research_bruno_2023]: https://doi.org/10.1007/978-981-19-7927-9_4
[research_bruno_2023_b]: https://doi.org/10.1007/978-981-19-7927-9_1
[research_bruno_2023_c]: https://doi.org/10.1007/978-981-19-7927-9_7
[research_bruno_2023_d]: https://doi.org/10.1007/978-981-19-7927-9
[research_brutsche_mcfall_2015]: https://doi.org/10.21236/ad1001469
[research_bryan_1953]: https://doi.org/10.1109/irepg-i.1953.5007337
[research_brykina_1996]: https://doi.org/10.1007/978-94-009-0267-1_38
[research_bu_lei_2018]: https://doi.org/10.1007/s11071-018-4447-z
[research_buchanan_crosby_1983]: https://doi.org/10.21236/ada136439
[research_bucher_bradley_1975]: https://doi.org/10.21236/ada007662
[research_buck_draper]: https://doi.org/10.1109/iciasf.1989.77655
[research_bucknell_1987]: https://doi.org/10.2514/6.1987-1711
[research_bucknell_1989]: https://doi.org/10.2514/3.23124
[research_builder_1964]: https://doi.org/10.2514/6.1964-243
[research_bullen_cheeseman_1988]: https://doi.org/10.1016/0142-727x(88)90012-4
[research_bulman_siebenhaar_1995]: https://doi.org/10.2514/6.1995-2475
[research_buonadonna_knight_1973]: https://doi.org/10.2514/6.1973-211
[research_bur_benay_2002]: https://doi.org/10.1007/978-3-540-45856-2_3
[research_bura_2017]: https://doi.org/10.2514/6.2017-2392
[research_burke_poggie_2023]: https://doi.org/10.2514/6.2023-1467
[research_burnett_2002]: https://doi.org/10.2514/6.2002-4478
[research_burnett_czysz_1963]: https://doi.org/10.21236/ad0408988
[research_burns_1965]: https://doi.org/10.1016/b978-0-08-011074-5.50005-1
[research_burns_1970]: https://doi.org/10.2514/6.1970-587
[research_burns_2020]: https://doi.org/10.2172/1829235
[research_burr_1968]: https://doi.org/10.2514/6.1968-581
[research_burris_1966]: https://doi.org/10.2514/6.1966-741
[research_burrows_vukasinovic_2017]: https://doi.org/10.2514/6.2017-4304
[research_burt_josyula_2013]: https://doi.org/10.2514/6.2013-2782
[research_burton_1987]: https://doi.org/10.1088/0022-3735/20/11/001
[research_burton_carroll_2025]: https://doi.org/10.1016/j.actaastro.2025.09.001
[research_busa_brown_2016]: https://doi.org/10.2514/6.2016-0659
[research_bussing_murman_1983]: https://doi.org/10.2514/6.1983-422
[research_bustard_bemis_2024]: https://doi.org/10.2514/6.2024-3893
[research_butler_1976]: https://doi.org/10.21236/ada023690
[research_butler_benitez_2022]: https://doi.org/10.2514/6.2022-1905
[research_butler_benitez_2023]: https://doi.org/10.2514/6.2023-1539
[research_butt_2013]: https://doi.org/10.21307/ijssis-2017-560
[research_butt_yan_2010]: https://doi.org/10.1109/cdc.2010.5717701
[research_butt_yan_2011]: https://doi.org/10.1002/asjc.450
[research_buttsworth_morgan_1995]: https://doi.org/10.1007/978-3-642-78829-1_12
[research_buttsworth_stern_2017]: https://doi.org/10.2514/6.2017-0261
[research_buzjurkin_kiselev_2002]: https://doi.org/10.1007/s001930200122
[research_buzz_suppression_2005]: https://doi.org/10.5139/jksas.2005.33.3.010
[research_bykerk_verstraete_2020]: https://doi.org/10.1016/j.ast.2019.105531
[research_byun_kim_2026]: https://doi.org/10.1016/j.ast.2026.112144
[research_c_battista_2011]: https://doi.org/10.5772/17168
[research_cai_huang_2022]: https://doi.org/10.3389/fenrg.2022.884624
[research_cai_liu_2016]: https://doi.org/10.1016/j.actaastro.2016.05.010
[research_cai_sun_2018]: https://doi.org/10.1016/j.ast.2018.07.028
[research_cai_zheng_2025]: https://doi.org/10.1063/5.0267595
[research_cai_zhou_2017]: https://doi.org/10.1016/j.actaastro.2017.10.013
[research_cai_zhuang_2025]: https://doi.org/10.1016/j.dt.2024.11.001
[research_cai_zhuang_2026]: https://doi.org/10.1016/j.ast.2026.112222
[research_cain_2002]: https://doi.org/10.2514/6.2002-3877
[research_cain_walton_2003]: https://doi.org/10.2514/6.2003-7030
[research_cairns_tevebaugh_1963]: https://doi.org/10.21236/ad0615885
[research_calabia_jin_2020]: https://doi.org/10.1002/essoar.10504517.1
[research_calder_yackoub_2026]: https://doi.org/10.2514/6.2026-0873
[research_caledonia_krech_1994]: https://doi.org/10.21236/ada281452
[research_californiainstoftechpasadena_1990]: https://doi.org/10.21236/ada229217
[research_calise_bae_1987]: https://doi.org/10.2514/6.1987-2568
[research_callan_marusic_2000]: https://doi.org/10.2514/6.2000-2461
[research_callan_marusic_2001]: https://doi.org/10.2514/2.1513
[research_calligeros_dugundji_1961]: https://doi.org/10.21236/ad0253970
[research_calogeras_1969]: https://doi.org/10.2514/6.1969-487
[research_camara_gatta_2011]: https://doi.org/10.1007/s00269-011-0457-9
[research_cambier_adelman_1997]: https://doi.org/10.1007/978-94-011-5432-1_23
[research_campbell_kresge_2003]: https://doi.org/10.1109/dasc.2003.1245892
[research_campuzano_dang_1995]: https://doi.org/10.2514/6.1995-2449
[research_candler_1989]: https://doi.org/10.2514/6.1989-1739
[research_candler_1989_b]: https://doi.org/10.2514/6.1989-312
[research_candler_2001]: https://doi.org/10.21236/ada387503
[research_candler_2010]: https://doi.org/10.1002/9780470686652.eae038
[research_candler_2011]: https://doi.org/10.1017/cbo9780511842757.007
[research_candler_leyva_2022]: https://doi.org/10.1080/08929882.2022.2145777
[research_candler_nompelis_2002]: https://doi.org/10.2514/6.2002-434
[research_candler_subbareddy_2015]: https://doi.org/10.2514/5.9781624103292.0203.0238
[research_candlergraham_1989]: https://ntrs.nasa.gov/citations/19910001585
[research_candlergraham_parkchul_1988]: https://ntrs.nasa.gov/citations/19880057368
[research_cangelosi_heinkenschloss_2024]: https://doi.org/10.2514/6.2024-0375
[research_cann_1973]: https://doi.org/10.21236/ad0759290
[research_canoville_lewis_2025]: https://doi.org/10.2139/ssrn.5336052
[research_cao_brod_2021]: https://doi.org/10.1016/j.combustflame.2021.111562
[research_cao_brod_2023]: https://doi.org/10.1016/j.proci.2022.10.012
[research_cao_chang_2014]: https://doi.org/10.1016/j.ijhydene.2014.10.082
[research_cao_chang_2015]: https://doi.org/10.1016/j.ast.2014.11.001
[research_cao_gong_2022]: https://doi.org/10.21203/rs.3.rs-1969506/v1
[research_cao_he_2019]: https://doi.org/10.1016/j.proci.2018.06.213
[research_cao_lee_2022]: https://doi.org/10.1016/j.fuel.2021.123063
[research_cao_zhang_2007]: https://doi.org/10.1007/978-3-540-75995-9_86
[research_cao_zhang_2026]: https://doi.org/10.3390/aerospace13070631
[research_capparelli_unternbaumen_2026]: https://doi.org/10.18372/kai.2026.conf02.a8
[research_caraballo_webb_2009]: https://doi.org/10.2514/6.2009-924
[research_carbajosa_sanzandres_2025]: https://doi.org/10.1016/j.actaastro.2025.05.006
[research_carbajosa_sanzandres_2026]: https://doi.org/10.2139/ssrn.7042879
[research_carlomagno_luca_1993]: https://doi.org/10.1007/978-94-011-1828-6_44
[research_carman_jb_1966]: https://doi.org/10.21236/ad0632514
[research_carpenter_hantsche_2025]: https://doi.org/10.2514/6.2025-0194
[research_carrico_2009]: https://doi.org/10.21236/ada540172
[research_carroll_1982]: https://doi.org/10.2514/6.1982-578
[research_carroll_dutton_1989]: https://doi.org/10.2514/6.1989-355
[research_carroll_kerlin_1981]: https://doi.org/10.2172/6705254
[research_carson_mohieldin_2004]: https://doi.org/10.2514/6.2004-1035
[research_carter_2012]: https://doi.org/10.21236/ada563331
[research_carter_springfield_2002]: https://doi.org/10.21236/ada413060
[research_carvalho_santos_2020]: https://doi.org/10.26678/abcm.encit2020.cit20-0547
[research_casalino_colasurdo_2002]: https://doi.org/10.2514/6.2002-4897
[research_cassanova_1967]: https://doi.org/10.21236/ad0659372
[research_cassanto_1971]: https://doi.org/10.2514/6.1971-134
[research_cassanto_1972]: https://doi.org/10.2514/3.50095
[research_casseau_zhang_2022]: https://doi.org/10.1080/10618562.2022.2094917
[research_cassidy_halley_1991]: https://doi.org/10.2514/6.1991-3177
[research_castaldi_leylegian_2006]: https://doi.org/10.2514/6.2006-4403
[research_castner_simerly_2018]: https://doi.org/10.2514/6.2018-2850
[research_catalano_sturek_2001]: https://doi.org/10.21236/ada395936
[research_catoire_2009]: https://doi.org/10.21236/ada506353
[research_cavanaugh_narayanaswamy_2024]: https://doi.org/10.2514/6.2024-0112
[research_cavanaugh_narayanaswamy_2026]: https://doi.org/10.2514/6.2026-4174
[research_cavanaugh_stramecky_2025]: https://doi.org/10.2514/6.2025-0333
[research_cavity_actuated_supersonic_1995]: https://doi.org/10.1016/0140-6701(95)93351-4
[research_caylor_batill_1984]: https://doi.org/10.2514/6.1984-618
[research_cazierjr_ricketts_1991]: https://doi.org/10.2514/6.1991-1255
[research_celmins_1990]: https://doi.org/10.21236/ada224217
[research_cenkci_1991]: https://doi.org/10.21236/ada241143
[research_cenko_1992]: https://doi.org/10.2514/6.1992-4110
[research_cenko_cenko_2003]: https://doi.org/10.2514/6.2003-4225
[research_center_sobieczky_1991]: https://doi.org/10.2514/6.1991-1697
[research_centlivre_2023]: https://doi.org/10.2514/6.2023-0010
[research_cfd_applications_1986]: https://doi.org/10.2514/5.9781600865763.0219.0255
[research_cfd_optimization_1994]: https://doi.org/10.2514/6.1994-2951
[research_chacon_feleo_2019]: https://doi.org/10.2514/6.2019-4450
[research_chakravarthy_szema_1988]: https://doi.org/10.2514/6.1988-2564
[research_chakravarty_narayanaswamy_2026]: https://doi.org/10.2514/6.2026-1244
[research_chamberlain_baltar_1993]: https://doi.org/10.2514/6.1993-317
[research_chambers_titchener_2019]: https://doi.org/10.2514/6.2019-2101
[research_chambersjr_2007]: https://doi.org/10.21236/ada463441
[research_chan_ihme_2014]: https://doi.org/10.2514/6.2014-1161
[research_chan_ihme_2016]: https://doi.org/10.2514/6.2016-1900
[research_chandler_2003]: https://doi.org/10.21236/ada428392
[research_chandrasekhar_ramanujachari_2014]: https://doi.org/10.14429/dsj.64.2733
[research_chang_1962]: https://doi.org/10.21236/ad0274359
[research_chang_1966]: https://doi.org/10.21236/ad0632797
[research_chang_2025]: https://doi.org/10.2514/6.2025-2542
[research_chang_choudhari_2010]: https://doi.org/10.1007/s00162-010-0191-9
[research_chang_fan_2010]: https://doi.org/10.1016/j.actaastro.2009.05.021
[research_chang_hu_2011]: https://doi.org/10.1016/j.actaastro.2011.05.035
[research_chang_huang_2022]: https://doi.org/10.3390/aerospace10010001
[research_chang_li_2011]: https://doi.org/10.1177/0954410011422981
[research_chang_li_2017]: https://doi.org/10.1016/j.paerosci.2016.12.001
[research_chang_sasaki_2023]: https://doi.org/10.2139/ssrn.4391405
[research_chang_seo_2026]: https://doi.org/10.2514/6.2026-5119
[research_chang_wang_2012]: https://doi.org/10.2514/6.2012-4150
[research_chang_wang_2014]: https://doi.org/10.1177/0954410014539289
[research_chang_yu_2008]: https://doi.org/10.2514/6.2008-4586
[research_chang_yu_2008_b]: https://doi.org/10.1017/s0001924000002505
[research_chang_yu_2009]: https://doi.org/10.1017/s0001924000002931
[research_chang_zheng_2014]: https://doi.org/10.1016/j.actaastro.2013.10.010
[research_chaosong_guorongzhao_2011]: https://doi.org/10.1109/iccrd.2011.5763877
[research_chaouat_2017]: https://doi.org/10.1007/s10494-016-9794-6
[research_chapter_10_2013]: https://doi.org/10.1615/978-1-56700-309-3.192
[research_chapter_13_2013]: https://doi.org/10.1615/978-1-56700-309-3.236
[research_chapter_18_2013]: https://doi.org/10.1615/978-1-56700-309-3.325
[research_chapter_1_2013]: https://doi.org/10.1615/978-1-56700-309-3.78
[research_chapter_5_2013]: https://doi.org/10.1615/978-1-56700-309-3.134
[research_chapter_6_2013]: https://doi.org/10.1615/978-1-56700-309-3.153
[research_chapter_7_2013]: https://doi.org/10.1615/978-1-56700-309-3.163
[research_chapter_8_2013]: https://doi.org/10.1615/978-1-56700-309-3.172
[research_chapter_9_2013]: https://doi.org/10.1615/978-1-56700-309-3.183
[research_characterization_of_2014]: https://doi.org/10.1201/b16545-11
[research_charyulu_kurian_1998]: https://doi.org/10.1080/00102209808952008
[research_chase_fisher_1978]: https://doi.org/10.2514/6.1978-983
[research_chase_rust_1980]: https://doi.org/10.2514/6.1980-1607
[research_chatterjee_venkateswararao_1982]: https://doi.org/10.1007/978-1-4684-8267-6_5
[research_chauffour_lewis_2003]: https://doi.org/10.2514/6.2003-7060
[research_chaussee_rizk_1982]: https://doi.org/10.2514/6.1982-291
[research_chauvin_erb_1968]: https://doi.org/10.2514/6.1968-1142
[research_che_tang_2008]: https://doi.org/10.1016/j.ast.2008.01.008
[research_cheadle_dizinno_2026]: https://doi.org/10.1615/tfec2026.fna.061757
[research_chekhovskoi_2000]: https://doi.org/10.1007/bf02755945
[research_chemical_and_2006]: https://doi.org/10.2514/5.9781600861956.0575.0598
[research_chemical_and_2019]: https://doi.org/10.2514/5.9781624105142.0595.0618
[research_chemical_kinetics_1962]: https://doi.org/10.2514/5.9781600864810.0181.0204
[research_chen_1958]: https://doi.org/10.1115/1.4012730
[research_chen_2017]: https://doi.org/10.2514/6.2017-2174
[research_chen_2017_b]: https://doi.org/10.2514/6.2017-2334
[research_chen_2023]: https://doi.org/10.22541/au.167451375.50160138/v1
[research_chen_agarwal_2008]: https://doi.org/10.1063/1.3076525
[research_chen_ai_2014]: https://doi.org/10.1615/heatpipescietech.v5.i1-4.590
[research_chen_bonanni_2024]: https://doi.org/10.2514/6.2024-3809
[research_chen_bultman_2004]: https://doi.org/10.1115/ht-fed2004-56182
[research_chen_chen_2013]: https://doi.org/10.1016/j.proeng.2013.12.014
[research_chen_chen_2016]: https://doi.org/10.2514/6.2016-1252
[research_chen_chen_2024]: https://doi.org/10.1088/1742-6596/2816/1/012073
[research_chen_fan_2020]: https://doi.org/10.1016/j.actaastro.2020.05.031
[research_chen_fan_2020_b]: https://doi.org/10.1016/j.actaastro.2019.10.047
[research_chen_gao_2016]: https://doi.org/10.1109/chicc.2016.7554180
[research_chen_gu_2003]: https://doi.org/10.2514/6.2003-7043
[research_chen_guo_2017]: https://doi.org/10.2514/6.2017-4316
[research_chen_guo_2019]: https://doi.org/10.1109/access.2019.2907806
[research_chen_guo_2026]: https://doi.org/10.2139/ssrn.7019804
[research_chen_he_2025]: https://doi.org/10.1177/16878132251348391
[research_chen_henline_1993]: https://doi.org/10.2514/6.1993-2836
[research_chen_hu_2012]: https://doi.org/10.1063/1.4769718
[research_chen_jing_2018]: https://doi.org/10.1109/icmae.2018.8467711
[research_chen_liu_2014]: https://doi.org/10.4028/www.scientific.net/amm.574.480
[research_chen_liu_2015]: https://doi.org/10.2514/6.2015-3670
[research_chen_liu_2016]: https://doi.org/10.1109/icca.2016.7505311
[research_chen_liu_2024]: https://doi.org/10.20944/preprints202402.0049.v1
[research_chen_lu_2025]: https://doi.org/10.1109/cac67268.2025.11487931
[research_chen_mao_2026]: https://doi.org/10.1063/5.0335632
[research_chen_martinez_2025]: https://doi.org/10.64631/abcd8901
[research_chen_milos_1996]: https://doi.org/10.2514/6.1996-615
[research_chen_ni_2017]: https://doi.org/10.2514/6.2017-2338
[research_chen_niu_2018]: https://doi.org/10.1109/access.2018.2820008
[research_chen_pei_2021]: https://doi.org/10.3390/aerospace8050124
[research_chen_sethuraman_2026]: https://doi.org/10.1016/j.ast.2025.111260
[research_chen_shen_2020]: https://doi.org/10.1155/2020/7503272
[research_chen_starkey_2009]: https://doi.org/10.21236/ada590178
[research_chen_tan_2018]: https://doi.org/10.2514/1.j056674
[research_chen_tan_2019]: https://doi.org/10.1016/j.ast.2019.105471
[research_chen_tan_2019_b]: https://doi.org/10.2514/1.j057811
[research_chen_tian_2022]: https://doi.org/10.21203/rs.3.rs-1794933/v1
[research_chen_tian_2025]: https://doi.org/10.1016/j.expthermflusci.2025.111428
[research_chen_wang_2021]: https://doi.org/10.2514/1.j059994
[research_chen_wang_2021_b]: https://doi.org/10.1063/5.0045184
[research_chen_wang_2025]: https://doi.org/10.1016/j.applthermaleng.2025.127968
[research_chen_williamson_2006]: https://doi.org/10.2514/6.2006-6563
[research_chen_wu_2018]: https://doi.org/10.12783/dtetr/ecame2017/18452
[research_chen_yan_2018]: https://doi.org/10.1016/j.ijheatmasstransfer.2018.06.121
[research_chen_yao_2016]: https://doi.org/10.1117/12.2244508
[research_chen_yue_2018]: https://doi.org/10.2514/1.b36702
[research_chen_zheng_2026]: https://doi.org/10.3390/batteries12010027
[research_chen_zhou_2020]: https://doi.org/10.1007/978-981-15-8901-0_9
[research_chen_zhou_2020_b]: https://doi.org/10.1007/978-981-15-8901-0_3
[research_chen_zhou_2020_c]: https://doi.org/10.1007/978-981-15-8901-0_11
[research_chen_zhou_2020_d]: https://doi.org/10.1016/j.ast.2020.105679
[research_chen_zhou_2021]: https://doi.org/10.1007/978-981-15-8901-0
[research_chen_zhu_2024]: https://doi.org/10.2139/ssrn.4871447
[research_cheney_1988]: https://doi.org/10.2514/6.1988-2125
[research_chenfangjengfrank_berryscotta_2010]: https://ntrs.nasa.gov/citations/20100027425
[research_cheng_1960]: https://doi.org/10.21236/ad0243140
[research_cheng_1993]: https://doi.org/10.21236/ada267384
[research_cheng_aslam_2020]: https://doi.org/10.1063/12.0000944
[research_cheng_dong_2017]: https://doi.org/10.20944/preprints201710.0046.v1
[research_cheng_liu_2015]: https://doi.org/10.1109/icinfa.2015.7279772
[research_cheng_tang_2017]: https://doi.org/10.2514/6.2017-2273
[research_cheng_wang_2018]: https://doi.org/10.1109/ccdc.2018.8407688
[research_cheng_yan_2019]: https://doi.org/10.1051/jnwpu/20193761102
[research_cheng_yan_2021]: https://doi.org/10.1016/j.ast.2021.106529
[research_chengbinlian_zhangren_2012]: https://doi.org/10.1049/cp.2012.1300
[research_chern_lobser_2014]: https://doi.org/10.2514/6.2014-0437
[research_chern_rockwell_2025]: https://doi.org/10.2514/6.2025-0228
[research_cherukat_na_1998]: https://doi.org/10.1007/s001620050083
[research_cheung_chen_1974]: https://doi.org/10.1115/1.3423485
[research_chi_wang_2021]: https://doi.org/10.23919/ccc52363.2021.9550037
[research_chi_wei_2014]: https://doi.org/10.2514/6.2014-3451
[research_chien_1977]: https://doi.org/10.21236/ada044948
[research_chima_2011]: https://doi.org/10.2514/6.2011-3801
[research_chiu_1987]: https://doi.org/10.2514/6.1987-67
[research_chiu_1987_b]: https://doi.org/10.2514/6.1987-2037
[research_choe_kim_2016]: https://doi.org/10.2514/6.2016-3564
[research_choe_kim_2020]: https://doi.org/10.2514/1.b37474
[research_choi_alexander_2008]: https://doi.org/10.21236/ada481757
[research_choi_choi_2026]: https://doi.org/10.2139/ssrn.6438819
[research_choi_driscoll_2024]: https://doi.org/10.2514/1.b39553
[research_choi_gamba_2026]: https://doi.org/10.2514/6.2026-5096
[research_choi_ma_2005]: https://doi.org/10.1016/j.proci.2004.08.250
[research_choi_menon_2009]: https://doi.org/10.2514/6.2009-5383
[research_choi_noh_2011]: https://doi.org/10.2514/6.2011-2395
[research_choi_sasoh_2002]: https://doi.org/10.2514/6.2002-2202
[research_choi_yang_2003]: https://doi.org/10.2514/6.2003-4515
[research_choi_yang_2014]: https://doi.org/10.2514/6.2014-3744
[research_choi_yoon_2009]: https://doi.org/10.2514/6.2009-5430
[research_chokani_2001]: https://doi.org/10.2514/6.2001-211
[research_chou_shen_1996]: https://doi.org/10.2514/6.1996-2892
[research_chou_smith_1974]: https://doi.org/10.21236/ada001135
[research_choubey_gaud_2022]: https://doi.org/10.1016/j.fuel.2021.122847
[research_choubey_pandey_2016]: https://doi.org/10.1016/j.pisc.2016.04.032
[research_choubey_pandey_2018]: https://doi.org/10.1016/j.actaastro.2018.01.034
[research_choubey_panging_2027]: https://doi.org/10.1016/j.fuel.2026.140782
[research_choubey_solanki_2023]: https://doi.org/10.1016/j.fuel.2023.128972
[research_choubey_solanki_2023_b]: https://doi.org/10.1016/j.actaastro.2022.10.055
[research_choubey_tiwari_2022]: https://doi.org/10.1016/b978-0-323-99565-8.00005-7
[research_choubey_tiwari_2022_b]: https://doi.org/10.1016/b978-0-323-99565-8.00006-9
[research_choubey_tiwari_2022_c]: https://doi.org/10.1016/b978-0-323-99565-8.00002-1
[research_choubey_yadav_2021]: https://doi.org/10.1016/j.actaastro.2021.08.008
[research_chourushi_singh_2021]: https://doi.org/10.1080/10618562.2022.2032680
[research_chow_1979]: https://doi.org/10.21236/ada071899
[research_chow_gao_2004]: https://doi.org/10.1080/10618560410001694170
[research_chrusciel_1976]: https://doi.org/10.2514/6.1976-94
[research_chuang_morimoto_1996]: https://doi.org/10.2514/6.1996-3876
[research_chuang_morimoto_1997]: https://doi.org/10.2514/2.3205
[research_chuanzhen_xufei_2022]: https://doi.org/10.1016/j.actaastro.2022.08.004
[research_chuck_eberhardt_1990]: https://doi.org/10.2514/6.1990-149
[research_chudej_1993]: https://doi.org/10.1007/978-3-0348-7539-4_23
[research_chudoba_2019]: https://doi.org/10.1007/978-3-030-16856-8_5
[research_chudoba_2019_b]: https://doi.org/10.1007/978-3-030-16856-8
[research_chudoba_haney_2015]: https://doi.org/10.1017/s0001924000010241
[research_chun_1991]: https://doi.org/10.1007/978-3-642-76527-8_67
[research_chun_burr_1969]: https://doi.org/10.2514/3.44056
[research_cisnerosgaribay_buchta_2020]: https://doi.org/10.2514/6.2020-1843
[research_cisnerosgaribay_pantano_2022]: https://doi.org/10.2514/1.j061533
[research_clarey_greendyke_2018]: https://doi.org/10.2514/6.2018-0744
[research_clark_1965]: https://doi.org/10.2172/4595258
[research_clark_1966]: https://doi.org/10.21236/ad0804001
[research_clark_mirmirani_2006]: https://doi.org/10.2514/6.2006-6560
[research_clark_wu_2006]: https://doi.org/10.2514/6.2006-218
[research_clarke_1989]: https://doi.org/10.1007/978-1-4684-9187-6_6
[research_clarke_2008]: https://doi.org/10.21236/ada500739
[research_clauser_1954]: https://doi.org/10.2514/8.6460
[research_clauss_sontgen_1994]: https://doi.org/10.1615/intjenergeticmaterialschemprop..v3.i1-6.140
[research_clemens_2010]: https://doi.org/10.21236/ada525600
[research_clement_2018]: https://doi.org/10.1201/b22066-11
[research_cliff_well_1991]: https://doi.org/10.2514/6.1991-5065
[research_cliff_well_1992]: https://doi.org/10.2514/6.1992-4301
[research_coats_1981]: https://doi.org/10.2514/6.1981-36
[research_cockrellcharlesedwardjr_1994]: https://ntrs.nasa.gov/citations/19940029612
[research_cockrellcharlesejr_1993]: https://ntrs.nasa.gov/citations/19930064125
[research_cockrellcharlesejr_1994]: https://ntrs.nasa.gov/citations/19950037643
[research_cockrelljr_huebner_1991]: https://doi.org/10.2514/6.1991-3209
[research_cockrellsejr_huebner_1995]: https://doi.org/10.2514/6.1995-736
[research_cocks_donohue_2013]: https://doi.org/10.2514/6.2013-116
[research_cohen_1968]: https://doi.org/10.2514/6.1968-96
[research_cohen_2011]: https://doi.org/10.21236/ada553570
[research_cohen_natan_1997]: https://doi.org/10.2514/6.1997-3237
[research_cohenzur_natan_1998]: https://doi.org/10.2514/2.5379
[research_cole_1988]: https://doi.org/10.21236/ada196247
[research_cole_cook_1980]: https://doi.org/10.21236/ada207109
[research_collinstimothyj_congdonwilliamm_2005]: https://ntrs.nasa.gov/citations/20060002549
[research_colman_mayell_1968]: https://doi.org/10.21236/ad0835971
[research_colwill_curran_1969]: https://doi.org/10.2514/6.1969-546
[research_combustion_and_1978]: https://doi.org/10.2514/5.9781600865367.0160.0179
[research_combustion_chemistry_1978]: https://doi.org/10.2514/5.9781600865367.0255.0306
[research_combustion_in_2006]: https://doi.org/10.1017/cbo9780511754517.016
[research_combustion_of_2001]: https://doi.org/10.1201/9781420040685-9
[research_combustion_scaling_2012]: https://doi.org/10.2514/6.2012-5811
[research_comfort_todisco_1969]: https://doi.org/10.2514/6.1969-8
[research_comparative_applicability_1960]: https://doi.org/10.2514/5.9781600864759.0471.0493
[research_comparison_of_1960]: https://doi.org/10.1016/0042-207x(60)90305-5
[research_comparison_of_1960_b]: https://doi.org/10.1016/0042-207x(60)90213-x
[research_comparison_of_1983]: https://doi.org/10.2514/5.9781600865626.0234.0254
[research_comparison_of_1994]: https://doi.org/10.2514/6.1994-2273
[research_computational_fluid_1990]: https://doi.org/10.2514/5.9781600865985.0817.0838
[research_computational_fluid_2000]: https://doi.org/10.1017/cbo9780511574474.010
[research_computational_fluid_2000_b]: https://doi.org/10.1017/cbo9780511574474.009
[research_computational_fluid_2009]: https://doi.org/10.1017/cbo9780511627019.009
[research_computational_fluid_2014]: https://doi.org/10.1201/b17494-106
[research_computational_fluid_dynamic_solutions_2006]: https://doi.org/10.2514/5.9781600861956.0415.0448
[research_computational_fluid_dynamic_solutions_2019]: https://doi.org/10.2514/5.9781624105142.0429.0460
[research_comstock]: https://doi.org/10.15368/theses.2020.170
[research_cong_kunfeng_2017]: https://doi.org/10.23919/chicc.2017.8027876
[research_congress_will_2024]: https://doi.org/10.1108/oxan-db290424
[research_coniglio]: https://doi.org/10.70675/700187afz7d1az4fd8zb4afz1801f1f181aa
[research_connelly_2008]: https://doi.org/10.1094/cfw-53-4-0198
[research_connolly_krouse_2021]: https://doi.org/10.2514/6.2021-3538
[research_connolly_loth_2020]: https://doi.org/10.2514/6.2020-2406
[research_connolly_loth_2021]: https://doi.org/10.2514/1.j059552
[research_control_system_1976]: https://doi.org/10.1016/0010-4485(76)90126-3
[research_conversion_of_2004]: https://doi.org/10.1016/s0140-6701(04)93092-5
[research_conway_johansson_2001]: https://doi.org/10.2514/6.2001-3201
[research_cook]: https://doi.org/10.31274/rtd-180815-4335
[research_cook_1981]: https://doi.org/10.2514/6.1981-2380
[research_cookson_1976]: https://doi.org/10.21236/ada035309
[research_corbin_wolff_2008]: https://doi.org/10.2514/6.2008-2644
[research_cornellaeronauticallabincbuffalony_1963]: https://doi.org/10.21236/ad0402819
[research_correction_to_2026]: https://doi.org/10.1155/ijae/9841723
[research_corso_v_1966]: https://doi.org/10.21236/ad0632531
[research_corton_1966]: https://doi.org/10.21236/ad0489565
[research_coupled_dynamic_2018]: https://doi.org/10.21629/jsee.2018.06.15
[research_courtland_2010]: https://doi.org/10.1016/s0262-4079(10)61192-x
[research_cousin_1967]: https://doi.org/10.2514/6.1967-451
[research_coutant_keigley_1988]: https://doi.org/10.21236/ada201721
[research_couture_dechamplain_2008]: https://doi.org/10.2514/6.2008-5171
[research_cox_cairns_1973]: https://doi.org/10.21236/ad0766151
[research_cox_lewis_1995]: https://doi.org/10.2514/6.1995-6018
[research_crachi_pizzarelli_2024]: https://doi.org/10.52202/078371-0147
[research_craig_2022]: https://doi.org/10.2514/1.j061853
[research_craig_reich_1981]: https://doi.org/10.2514/6.1981-2423
[research_cramer_2001]: https://doi.org/10.2514/6.2001-2751
[research_creating_hypersonic_2019]: https://doi.org/10.2514/5.9781624105142.0829.0836
[research_creating_hypersonic_2019_b]: https://doi.org/10.2514/5.9781624105142.0811.0828
[research_cresci_1966]: https://doi.org/10.21236/ad0633949
[research_cresci_rubin_1980]: https://doi.org/10.21236/ada095817
[research_cristianopaulinopereira_marinho_2021]: https://doi.org/10.26678/abcm.cobem2021.cob2021-1706
[research_crow_boyd_2012]: https://doi.org/10.2514/6.2012-2751
[research_crown_1950]: https://doi.org/10.21236/ad0062509
[research_crumpton_2024]: https://doi.org/10.2514/6.2024-0861
[research_cubbage_johnston_1970]: https://doi.org/10.2514/6.1970-542
[research_cui_2021]: https://doi.org/10.1063/5.0057700
[research_cui_hu_2015]: https://doi.org/10.2514/6.2015-3646
[research_cui_jia_2022]: https://doi.org/10.3390/aerospace9100619
[research_cui_lv_2011]: https://doi.org/10.2514/1.b34235
[research_cui_mei_2018]: https://doi.org/10.1016/j.applthermaleng.2018.02.038
[research_culick_marble_1982]: https://doi.org/10.21236/ada133977
[research_culick_marble_1983]: https://doi.org/10.21236/ada147818
[research_culick_marble_1985]: https://doi.org/10.21236/ada172546
[research_culler_mcnamara_2011]: https://doi.org/10.2514/6.2011-1965
[research_culler_williams_2007]: https://doi.org/10.2514/6.2007-6395
[research_cuppoletti_ombrello_2020]: https://doi.org/10.1016/j.combustflame.2020.01.030
[research_curran_1996]: https://doi.org/10.1146/annurev.fluid.28.1.323
[research_curran_craig_1973]: https://doi.org/10.21236/ad0769481
[research_curran_hunt_2003]: https://doi.org/10.2514/6.2003-5265
[research_cusimano_johnson_1994]: https://doi.org/10.2514/6.1994-2120
[research_cutlerandrewd_magnottigaetano_2013]: https://ntrs.nasa.gov/citations/20130003230
[research_cutrone_2023]: https://doi.org/10.21741/9781644902813-36
[research_cutrone_schettino_2024]: https://doi.org/10.1007/s42496-024-00201-z
[research_cvrlje_1999]: https://doi.org/10.2514/6.1999-3412
[research_cvrlje_breitsamter_2000]: https://doi.org/10.2514/2.3552
[research_cvrlje_laschka_2001]: https://doi.org/10.2514/6.2001-1850
[research_cymbalist_dimotakis_2013]: https://doi.org/10.2514/6.2013-2978
[research_czysz_1963]: https://doi.org/10.21236/ad0408922
[research_czysz_1963_b]: https://doi.org/10.21236/ad0410539
[research_czysz_1988]: https://doi.org/10.4271/881203
[research_czysz_froning_1997]: https://doi.org/10.2514/6.1997-3394
[research_czysz_murthy_1996]: https://doi.org/10.2514/6.1996-4574
[research_dacosta_dasilva_2018]: https://doi.org/10.2514/6.2018-5386
[research_dacosta_rolim_2016]: https://doi.org/10.26678/abcm.encit2016.cit2016-0657
[research_dafler_1962]: https://doi.org/10.1119/1.1941784
[research_dai_chen_2024]: https://doi.org/10.1016/j.ijhydene.2024.10.303
[research_dai_li_2024]: https://doi.org/10.1016/j.fuel.2023.129852
[research_dai_zhao_2023]: https://doi.org/10.2514/1.t6675
[research_daines_boardman_1975]: https://doi.org/10.2514/6.1975-1277
[research_daines_segal_1998]: https://doi.org/10.2514/2.5352
[research_dajun_guobiao_2006]: https://doi.org/10.2514/6.iac-06-c2.p.2.05
[research_daliri_farahani_2018]: https://doi.org/10.2514/1.b36760
[research_dalle_driscoll_2012]: https://doi.org/10.2514/6.2012-4958
[research_dalle_driscoll_2015]: https://doi.org/10.2514/1.c032801
[research_dalle_frendreis_2010]: https://doi.org/10.2514/6.2010-7930
[research_dalle_rogers_2016]: https://doi.org/10.2514/6.2016-0797
[research_dalle_torrez_2011]: https://doi.org/10.2514/6.2011-6300
[research_dalle_torrez_2011_b]: https://doi.org/10.2514/6.2011-2368
[research_damazo_ziegler_2012]: https://doi.org/10.1007/978-3-642-25685-1_114
[research_damico_simon_2004]: https://doi.org/10.2514/6.2004-2294
[research_dan_tanabe_1994]: https://doi.org/10.2497/jjspm.41.1144
[research_danberg_1961]: https://doi.org/10.21236/ad0439624
[research_danberg_schroth_1964]: https://doi.org/10.21236/ad0448220
[research_dane_1942]: https://doi.org/10.1130/spe36-p27
[research_danehy_bathel_2015]: https://doi.org/10.2514/5.9781624103292.0343.0470
[research_daniau_bouchez_2006]: https://doi.org/10.2514/6.2006-7975
[research_danquah_mensah]: https://doi.org/10.18260/1-2-620-38583
[research_darrah_1988]: https://doi.org/10.21236/ada205006
[research_daryabeigikamran_blossermaxl_2006]: https://ntrs.nasa.gov/citations/20060022542
[research_das_debnath_2025]: https://doi.org/10.1007/s40997-025-00895-x
[research_das_kim_2015]: https://doi.org/10.1007/s11630-015-0769-z
[research_das_pandey_2021]: https://doi.org/10.1016/j.matpr.2020.12.1035
[research_dasgupta_choudhury_2012]: https://doi.org/10.2514/6.2012-5900
[research_dasgupta_krishnamoorthy_2001]: https://doi.org/10.1515/htmp.2001.20.5-6.367
[research_dasilvajunior_pinto_2018]: https://doi.org/10.26678/abcm.encit2018.cit18-0186
[research_dassoulas_1963]: https://doi.org/10.2514/6.1963-105
[research_daub_esser_2020]: https://doi.org/10.2514/1.j059150
[research_daum_1963]: https://doi.org/10.2514/3.1722
[research_davideglass]: https://ntrs.nasa.gov/citations/20210024803
[research_davideglass_b]: https://ntrs.nasa.gov/citations/20200003620
[research_davideglass_c]: https://ntrs.nasa.gov/citations/20260005305
[research_davidosigthorsson_2006]: https://doi.org/10.1109/med.2006.235983
[research_davidsonj_lallmanf_1999]: https://ntrs.nasa.gov/citations/20040086945
[research_davis_1970]: https://doi.org/10.21236/ad0705129
[research_davis_1984]: https://doi.org/10.2514/6.1984-1441
[research_davis_1984_b]: https://doi.org/10.21236/ada397339
[research_davis_1985]: https://doi.org/10.2514/6.1985-1434
[research_davis_1988]: https://doi.org/10.2514/6.1988-370
[research_davis_1993]: https://doi.org/10.2514/6.1993-2139
[research_davis_1995]: https://doi.org/10.2514/6.1995-2716
[research_davis_2015]: https://doi.org/10.1115/ajkfluids2015-6342
[research_daywitt_bhutta_1993]: https://doi.org/10.2514/6.1993-2948
[research_debieve_dupont_2009]: https://doi.org/10.1007/s00193-009-0232-8
[research_deboer_flourens_2015]: https://doi.org/10.1049/ic.2015.0198
[research_deboskey_sahoo_2026]: https://doi.org/10.1080/00102202.2026.2629994
[research_debtera_2022]: https://doi.org/10.2139/ssrn.4201717
[research_dec_mitcheltree_2002]: https://doi.org/10.2514/6.2002-910
[research_decker_2010]: https://doi.org/10.2514/6.2010-5071
[research_decker_laschka_2001]: https://doi.org/10.2514/6.2001-1852
[research_deegan_duan_2018]: https://doi.org/10.2514/6.2018-3219
[research_deepak_jagadeesh_2006]: https://doi.org/10.2514/6.2006-8155
[research_definition_of_1954]: https://doi.org/10.59161/cgpm1954res4e
[research_degrez_ginoux_1983]: https://doi.org/10.2514/6.1983-1755
[research_degrez_ginoux_1987]: https://doi.org/10.21236/ada187334
[research_delale_liaw_1989]: https://doi.org/10.21236/ada218516
[research_demange_dunlap_2007]: https://doi.org/10.2514/6.2007-5743
[research_demetriades_1975]: https://doi.org/10.21236/ada016536
[research_demetriades_1983]: https://doi.org/10.21236/ada137056
[research_demetriades_1985]: https://doi.org/10.21236/ada179580
[research_demir_ozturkmen_2025]: https://doi.org/10.2514/6.2025-0875
[research_demo_1986]: https://doi.org/10.2514/6.1986-9797
[research_demoura_ribeiro_2026]: https://doi.org/10.1007/s42401-026-00510-0
[research_dendy_hayes_2026]: https://doi.org/10.2514/6.2026-112635
[research_deng_2026]: https://doi.org/10.1088/1742-6596/3240/1/012025
[research_deng_jin_2017]: https://doi.org/10.1007/s12206-017-0121-5
[research_deng_kim_2017]: https://doi.org/10.1007/s12206-017-1025-0
[research_deng_zhao_2026]: https://doi.org/10.1088/1742-6596/3207/1/012079
[research_denman]: https://doi.org/10.14264/uql.2018.8
[research_denney_tai_2012]: https://doi.org/10.2514/6.2012-548
[research_dennispdykstra_1980]: https://doi.org/10.13031/2013.34619
[research_depalma_1976]: https://doi.org/10.21236/ada028786
[research_depiro]: https://doi.org/10.18130/v3h292
[research_derosa_gulizzi_2026]: https://doi.org/10.2514/6.2026-5045
[research_desbordes_hamada_1995]: https://doi.org/10.1007/bf01413876
[research_deshpande_poggie_2017]: https://doi.org/10.2514/6.2017-3479
[research_deshpande_poggie_2020]: https://doi.org/10.2514/6.2020-0581
[research_deshpande_poggie_2021]: https://doi.org/10.2514/6.2021-1097
[research_design_considerations_1963]: https://doi.org/10.2514/5.9781600864834.0761.0782
[research_design_of_1993]: https://doi.org/10.2514/6.1993-401
[research_desiqueira_ribeiro_2023]: https://doi.org/10.1016/j.tsep.2023.102174
[research_despirito_2009]: https://doi.org/10.21236/ada508090
[research_despirito_2013]: https://doi.org/10.21236/ada592880
[research_despirito_2014]: https://doi.org/10.21236/ada606669
[research_dessornes_scherrer_2001]: https://doi.org/10.2514/6.2001-1886
[research_dessornes_scherrer_2005]: https://doi.org/10.1016/j.ast.2005.01.007
[research_dettling_mcintyre_1978]: https://doi.org/10.2514/6.1978-955
[research_detullio_sandham_2012]: https://doi.org/10.1007/978-3-642-25685-1_66
[research_devault_1957]: https://doi.org/10.4271/570206
[research_development_of_1957]: https://doi.org/10.1016/0043-1648(57)90159-x
[research_development_of_1962]: https://doi.org/10.2514/5.9781600864810.0701.0758
[research_dewell_speyer_1993]: https://doi.org/10.2514/6.1993-3753
[research_dharavath_manna_2014]: https://doi.org/10.14429/dsj.64.5191
[research_dharavath_manna_2015]: https://doi.org/10.1016/j.actaastro.2015.08.014
[research_dharavath_manna_2015_b]: https://doi.org/10.2514/1.b35686
[research_dharavath_manna_2023]: https://doi.org/10.61653/joast.v67i3.2015.381
[research_diagnostic_studies_1962]: https://doi.org/10.2514/5.9781600864810.0581.0598
[research_diao_lu_2022]: https://doi.org/10.5220/0012010400003612
[research_diaz_1999]: https://doi.org/10.13182/fst99-a11963830
[research_dickeson_rodriguez_2009]: https://doi.org/10.2514/6.2009-6281
[research_dickhudt_1983]: https://doi.org/10.2514/6.1983-2755
[research_diclemente_rufolo_2009]: https://doi.org/10.2514/6.2009-7236
[research_dicristina_1979]: https://doi.org/10.21236/ada065645
[research_dietrick_2013]: https://doi.org/10.21236/ad1018856
[research_difebo_pasquale_2016]: https://doi.org/10.1016/s0262-1762(16)30318-2
[research_diggins_1951]: https://doi.org/10.21236/ad0895227
[research_digiovanni_stemmer_2018]: https://doi.org/10.2514/6.2018-4046
[research_dimotakis_leonard_1998]: https://doi.org/10.21236/ada353373
[research_dinda_vuchuru_2021]: https://doi.org/10.1021/acsomega.1c04218
[research_ding_li_2023]: https://doi.org/10.2174/9789815050028123040003
[research_ding_liu_2015]: https://doi.org/10.1016/j.actaastro.2015.02.016
[research_ding_liu_2018]: https://doi.org/10.1016/j.actaastro.2018.09.002
[research_ding_liu_2021]: https://doi.org/10.1016/j.actaastro.2021.09.018
[research_ding_wang_2020]: https://doi.org/10.1016/j.applthermaleng.2020.114949
[research_ding_zhuo_2022]: https://doi.org/10.1016/j.fuel.2022.125088
[research_direct_numerical_2023]: https://doi.org/10.1063/5.0146651
[research_diskinglenns_jachimowskicj_1987]: https://ntrs.nasa.gov/citations/19880016184
[research_dismountable_slidable_1996]: https://doi.org/10.1016/s0038-092x(97)81370-9
[research_distefano_hosder_2018]: https://doi.org/10.2514/6.2018-5262
[research_distefano_hosder_2020]: https://doi.org/10.2514/1.b37597
[research_disturbance_rejection_2016]: https://doi.org/10.1201/b16570-28
[research_dittert_kutemeyer_2017]: https://doi.org/10.1002/9781119407270.ch37
[research_diver_pavlovic_1984]: https://doi.org/10.1007/978-1-4899-5004-8_14
[research_djanalmann_murugan_2025]: https://doi.org/10.2514/6.2025-2632
[research_do_cappelli_2010]: https://doi.org/10.1016/j.combustflame.2010.03.009
[research_do_im_2010]: https://doi.org/10.1007/s00348-010-1028-4
[research_do_im_2011]: https://doi.org/10.2514/6.2011-2349
[research_do_im_2011_b]: https://doi.org/10.1615/tsfp7.1670
[research_do_im_2011_c]: https://doi.org/10.2514/6.2011-68
[research_do_im_2011_d]: https://doi.org/10.1007/s00348-011-1077-3
[research_do_nguyen_2024]: https://doi.org/10.1002/htj.23066
[research_do_passaro_2012]: https://doi.org/10.2514/6.2012-5929
[research_dobronski_1988]: https://doi.org/10.2514/6.1988-2119
[research_dodd_1980]: https://doi.org/10.21236/ada095359
[research_doherty]: https://doi.org/10.14264/uql.2014.382
[research_doherty_b]: https://doi.org/10.14264/346509
[research_dolan_1970]: https://doi.org/10.2514/6.1970-277
[research_dolling_1993]: https://doi.org/10.2514/6.1993-284
[research_dolling_2000]: https://doi.org/10.2514/6.2000-2596
[research_dolling_gramann_1986]: https://doi.org/10.2514/6.1986-1033
[research_dolnik_michaels_2025]: https://doi.org/10.2514/6.2025-0956
[research_dolvin_2009]: https://doi.org/10.2514/6.2009-7228
[research_domack_1991]: https://doi.org/10.2514/6.1991-3327
[research_domel_thompson_1991]: https://doi.org/10.2514/6.1991-377
[research_donbar_2012]: https://doi.org/10.2514/6.2012-4145
[research_donbar_gruber_2000]: https://doi.org/10.1016/s0082-0784(00)80269-6
[research_donelson_lewerenz_1989]: https://doi.org/10.2514/6.1989-2582
[research_dong_cai_2017]: https://doi.org/10.1061/(asce)as.1943-5525.0000727
[research_dong_guo_2021]: https://doi.org/10.1155/2021/3676810
[research_dong_huang_2023]: https://doi.org/10.23919/ccc58697.2023.10239805
[research_dong_huo_2015]: https://doi.org/10.1360/n092014-00262
[research_dong_li_2012]: https://doi.org/10.2514/6.2012-5946
[research_donohue_2013]: https://doi.org/10.2514/6.2013-698
[research_donohue_2014]: https://doi.org/10.2514/1.b35016
[research_donohuejamesm_2012]: https://ntrs.nasa.gov/citations/20140005746
[research_doolan_2006]: https://doi.org/10.2514/6.2006-222
[research_doronzo_2026]: https://doi.org/10.4236/aast.2026.113005
[research_dossantos_passaro_2025]: https://doi.org/10.1016/j.tsep.2024.103172
[research_doster_king_2007]: https://doi.org/10.2514/6.2007-5404
[research_doty_camberos_2011]: https://doi.org/10.4271/2011-01-2542
[research_dou_yu_2024]: https://doi.org/10.2139/ssrn.4750679
[research_douglas_bhushan_2025]: https://doi.org/10.2514/6.2025-3818
[research_douglas_bhushan_2025_b]: https://doi.org/10.2514/6.2025-3818.c1
[research_douglas_lindgren_1999]: https://doi.org/10.21236/ada361137
[research_doulati_baafi_2011]: https://doi.org/10.5772/16927
[research_draper_lanejr_1977]: https://doi.org/10.2514/6.1977-1165
[research_draper_lee_2019]: https://doi.org/10.2514/6.2019-0940
[research_drikakis_rana_2015]: https://doi.org/10.2514/6.2015-1294
[research_drummond_1958]: https://doi.org/10.1063/1.1723059
[research_drummond_1991]: https://doi.org/10.2514/6.1991-1914
[research_drummond_1992]: https://doi.org/10.1007/978-1-4612-2884-4_27
[research_drummond_weidner_1981]: https://doi.org/10.2514/6.1981-186
[research_drummondjp_danehypaulm_2007]: https://ntrs.nasa.gov/citations/20080013391
[research_drummondjphilip_carpentermarkh_1989]: https://ntrs.nasa.gov/citations/19900057355
[research_drummondjphilip_cockrellcharlesejr_2002]: https://ntrs.nasa.gov/citations/20030002653
[research_ds_2021]: https://doi.org/10.31031/acsr.2021.03.000552
[research_du_chen_2025]: https://doi.org/10.1016/j.combustflame.2025.114142
[research_du_huang_2018]: https://doi.org/10.1016/j.actaastro.2018.08.030
[research_du_li_2026]: https://doi.org/10.1088/1742-6596/3207/1/012059
[research_du_shen_2022]: https://doi.org/10.1063/5.0100940
[research_du_wan_2017]: https://doi.org/10.2514/6.2017-1938
[research_du_wang_2023]: https://doi.org/10.23919/ccc58697.2023.10240184
[research_dual_mode_combustion_2022]: https://doi.org/10.1002/9781119640646.ch7
[research_duan_sun_2011]: https://doi.org/10.1109/ccdc.2011.5968400
[research_duan_xu_2024]: https://doi.org/10.1088/1742-6596/2820/1/012040
[research_duan_zhang_2016]: https://doi.org/10.1109/wcica.2016.7578837
[research_dubey_gupta_2025]: https://doi.org/10.2514/6.2025-2135
[research_dubinin_fink_2009]: https://doi.org/10.1007/s11041-010-9203-z
[research_ducati_giannini_1964]: https://doi.org/10.2514/6.1964-668
[research_ducati_giannini_1965]: https://doi.org/10.2514/6.1965-96
[research_dudebout_sislian_1994]: https://doi.org/10.2514/6.1994-3098
[research_dudin_2002]: https://doi.org/10.1023/a:1015826804108
[research_dudley_ukeiley_2011]: https://doi.org/10.2514/6.2011-3844
[research_duesbery_louat_1992]: https://doi.org/10.21236/ada258404
[research_duesbery_louat_1994]: https://doi.org/10.21236/ada282457
[research_duffy_1968]: https://doi.org/10.21236/ad0678493
[research_duffy_shattuck_1975]: https://doi.org/10.21236/ada015064
[research_duffy_shattuck_1975_b]: https://doi.org/10.21236/ada013834
[research_dufour_bouchez_2001]: https://doi.org/10.2514/6.2001-1817
[research_duganjr_1969]: https://doi.org/10.2514/6.1969-774
[research_dugger_1959]: https://doi.org/10.2514/8.4917
[research_dugundji_1965]: https://doi.org/10.21236/ad0624995
[research_dukowicz_1968]: https://doi.org/10.2514/6.1968-728
[research_dunagan]: https://doi.org/10.32469/10355/98343
[research_dunn_1980]: https://doi.org/10.21236/ada092229
[research_dupont_debieve_2011]: https://doi.org/10.1017/cbo9780511842757.009
[research_duran_2026]: https://doi.org/10.2514/6.2026-2637
[research_duran_zeng_2026]: https://doi.org/10.2514/6.2026-109216
[research_durant_andre_2015]: https://doi.org/10.2514/6.2015-3575
[research_durbin_1959]: https://doi.org/10.1016/b978-1-4831-9728-9.50011-4
[research_duston_seghi_2004]: https://doi.org/10.21236/ada461309
[research_dutczak_2006]: https://doi.org/10.19206/ce-117349
[research_dutt_1980]: https://doi.org/10.21236/ada102554
[research_dutta_yin_2011]: https://doi.org/10.1016/j.combustflame.2010.12.023
[research_duvall_hale_1985]: https://doi.org/10.21236/ada171495
[research_dvorak_1965]: https://doi.org/10.1016/b978-0-08-011860-4.50007-0
[research_dvorak_kavecky_2010]: https://doi.org/10.4028/www.scientific.net/ddf.297-301.844
[research_dwoyer_1973]: https://doi.org/10.2514/6.1973-3007
[research_dwoyer_kumar_1987]: https://doi.org/10.2514/6.1987-279
[research_dwyer_1994]: https://doi.org/10.2514/6.1994-2158
[research_dyakonov_schoenenberger_2012]: https://doi.org/10.2514/6.2012-2999
[research_dzhafarov_altunbas_1996]: https://doi.org/10.1016/0921-4534(96)00357-7
[research_eagle_ross_1955]: https://doi.org/10.2172/4240259
[research_early_2000]: https://doi.org/10.1017/s0001924000064010
[research_eason_spottswood_2013]: https://doi.org/10.2514/6.2013-1747
[research_ebrahimi_gaitonde_2007]: https://doi.org/10.2514/6.2007-645
[research_eckert_bradt_1984]: https://doi.org/10.1007/978-1-4899-5004-8_6
[research_eco_demonstrator_2018]: https://doi.org/10.12968/s1478-2774(23)50032-6
[research_economos_1962]: https://doi.org/10.2514/8.6208
[research_ecschweglerlanl_aplacehoneywell_2000]: https://doi.org/10.2172/764597
[research_edelman_harsha_1980]: https://doi.org/10.2514/6.1980-1190
[research_edelman_spadaccini_1969]: https://doi.org/10.2514/6.1969-456
[research_edquist_2006]: https://doi.org/10.2514/6.2006-6137
[research_edquist_lewis_1993]: https://doi.org/10.2514/6.1993-403
[research_edwards_2014]: https://doi.org/10.21236/ada605092
[research_edwards_arbolino_2024]: https://doi.org/10.2514/6.2024-1896
[research_edwards_babikian_1987]: https://doi.org/10.2514/6.1987-1520
[research_edwards_dewitt_2006]: https://doi.org/10.2514/6.2006-7973
[research_edwards_fulton_2011]: https://doi.org/10.2514/6.2011-3714
[research_edwards_small_1975]: https://doi.org/10.2514/6.1975-58
[research_edwards_speiser_1951]: https://doi.org/10.1063/1.1699977
[research_effect_of_2016]: https://doi.org/10.15242/iae.iae1116456
[research_effect_of_2017]: https://doi.org/10.15372/fgv20170104
[research_effects_of_1969]: https://doi.org/10.2514/6.1969-168
[research_effects_of_1972]: https://doi.org/10.2514/6.1972-181
[research_effects_of_1993]: https://doi.org/10.2514/6.1993-609
[research_effects_of_2021]: https://doi.org/10.47176/jafm.14.03.31766
[research_efficient_thermal_2002]: https://doi.org/10.1016/s1464-2859(02)80675-7
[research_eggers_2002]: https://doi.org/10.1007/978-3-540-45466-3_17
[research_eggers_2003]: https://doi.org/10.2514/6.2003-7055
[research_eggers_novelli_1999]: https://doi.org/10.2514/6.1999-4877
[research_eggers_novelli_2001]: https://doi.org/10.2514/6.2001-1921
[research_eglin_embacher_2025]: https://doi.org/10.4050/f-0081-2025-0182
[research_egorov_erofeev_1997]: https://doi.org/10.1007/bf02697944
[research_egusquiza_virto_1982]: https://doi.org/10.4271/820158
[research_eklund_2004]: https://doi.org/10.2514/6.2004-5950
[research_eklund_baurle_2001]: https://doi.org/10.2514/6.2001-379
[research_elands_dijkstra_1991]: https://doi.org/10.2514/6.1991-1869
[research_elaskary_2011]: https://doi.org/10.1080/10618562.2011.618455
[research_elchert_1982]: https://doi.org/10.2514/6.1982-1556
[research_elder_1980]: https://doi.org/10.2514/6.1980-313
[research_eldridge_1988]: https://doi.org/10.1007/bf00504240
[research_elements_of_1986]: https://doi.org/10.2514/5.9781600865763.0127.0168
[research_elgar_raubenheimer_2011]: https://doi.org/10.21236/ada545009
[research_elizabethfrieken_scottaberry_2020]: https://ntrs.nasa.gov/citations/20200003493
[research_elkebir_ornik_2020]: https://doi.org/10.2514/6.2020-2412
[research_elkoby_2005]: https://doi.org/10.2514/6.2005-2807
[research_elkowitz_wanchek_2023]: https://doi.org/10.1364/opticaopen.24317149
[research_elliott_1968]: https://doi.org/10.2514/6.1968-1157
[research_elliott_houpt_2019]: https://doi.org/10.2514/6.2019-3925
[research_ellisonjc_johnsoncb_1964]: https://ntrs.nasa.gov/citations/19650001351
[research_elsayed_2016]: https://doi.org/10.1007/978-1-4471-6796-9_5
[research_ely]: https://doi.org/10.1109/naecon.1988.195222
[research_emami_rodi_1995]: https://doi.org/10.2514/6.1995-37
[research_emamisaied_trexlercarla_1995]: https://ntrs.nasa.gov/citations/19950021922
[research_emanuel_1992]: https://doi.org/10.1007/bf01414417
[research_emanuel_1992_b]: https://doi.org/10.1007/bf01414763
[research_emanuel_yi_2000]: https://doi.org/10.1007/s001930050184
[research_endothermic_reactions]: https://doi.org/10.1615/atoz.e.endothermic_reactions
[research_endothermic_reactions_2006]: https://doi.org/10.1615/atoz.e.endrea
[research_endothermic_reactors_1996]: https://doi.org/10.1016/0140-6701(96)89839-0
[research_engblom_bellamkonda_2012]: https://doi.org/10.2514/6.2012-3291
[research_engblom_frate_2005]: https://doi.org/10.2514/6.2005-1000
[research_engelund_2001]: https://doi.org/10.2514/2.3757
[research_engine_airframe_performance_1989]: https://doi.org/10.2514/5.9781600861499.0167.0237
[research_enkenhus_1969]: https://doi.org/10.2514/6.1969-333
[research_enkenhus_parazzoli_1969]: https://doi.org/10.2514/6.1969-169
[research_epstein_1954]: https://doi.org/10.21236/ad0037709
[research_erb_hosder_2018]: https://doi.org/10.2514/6.2018-5195
[research_erdos_1998]: https://doi.org/10.2514/6.1998-2494
[research_ericsson_1968]: https://doi.org/10.2514/6.1968-1158
[research_ericsson_1977]: https://doi.org/10.2514/6.1977-5
[research_ericsson_1977_b]: https://doi.org/10.2514/6.1977-449
[research_ericsson_1978]: https://doi.org/10.2514/6.1978-1181
[research_ericsson_scholnick_1968]: https://doi.org/10.2514/6.1968-889
[research_ertunc_durst_2008]: https://doi.org/10.1063/1.2837173
[research_eschenbach_skinner_1961]: https://doi.org/10.21236/ad0266907
[research_escher_1996]: https://doi.org/10.2514/6.1996-2684
[research_escher_2001]: https://doi.org/10.2514/6.2001-3240
[research_escher_ehrlic_2000]: https://doi.org/10.2514/6.2000-5602
[research_espinosa_2003]: https://doi.org/10.2514/6.2003-4408
[research_essenhigh_2006]: https://doi.org/10.1021/ef050276y
[research_estimation_of_ideal_2025]: https://doi.org/10.36948/ijfmr.2025.v07i01.35495
[research_eugenioribeiro]: https://doi.org/10.70675/71fb3bbazace2z4d12z9c65z6f46972309c9
[research_evaluation_of_1973]: https://doi.org/10.2514/6.1973-213
[research_evans_zok_2011]: https://doi.org/10.21236/ada552599
[research_everett_cashwell_1972]: https://doi.org/10.2172/4635208
[research_eves_valasek_2024]: https://doi.org/10.2514/6.2024-2874
[research_evolution_of_disturbances_2024]: https://doi.org/10.15372/pmtf202415475
[research_experimental_study_2022]: https://doi.org/10.47176/jafm.15.02.33220
[research_facility_requirements_1991]: https://doi.org/10.2514/5.9781600866104.0481.0526
[research_fain_lambert_2026]: https://doi.org/10.2514/6.2026-5087
[research_falempin_1999]: https://doi.org/10.2514/6.1999-2377
[research_falempin_forrat_1992]: https://doi.org/10.2514/6.1992-5052
[research_falempin_minard_2009]: https://doi.org/10.2514/6.2009-7378
[research_falempin_serre_2003]: https://doi.org/10.2514/6.2003-7031
[research_falempin_serre_2003_b]: https://doi.org/10.2514/6.2003-2733
[research_falempin_serre_2006]: https://doi.org/10.2514/6.2006-7925
[research_falempin_serre_2006_b]: https://doi.org/10.2514/6.2006-5190
[research_falempin_serre_2008]: https://doi.org/10.2514/6.2008-2541
[research_falempin_thevenot_1995]: https://doi.org/10.2514/6.1995-6013
[research_falkiewicz_cesnik_2009]: https://doi.org/10.2514/6.2009-6284
[research_falkiewicz_cesnik_2010]: https://doi.org/10.2514/6.2010-7928
[research_falkiewicz_frendreis_2011]: https://doi.org/10.2514/6.2011-6378
[research_famularo_whitney_2018]: https://doi.org/10.2514/5.9781624104794.0289.0336
[research_fan_bing_2017]: https://doi.org/10.2514/6.2017-2115
[research_fan_chang_2009]: https://doi.org/10.2514/6.2009-3507
[research_fan_chang_2010]: https://doi.org/10.1017/s0001924000003924
[research_fan_cheng_2026]: https://doi.org/10.21203/rs.3.rs-9627450/v1
[research_fan_liu_2009]: https://doi.org/10.2514/6.2009-7334
[research_fan_lu_2017]: https://doi.org/10.3390/app7020159
[research_fan_qi_2024]: https://doi.org/10.1049/icp.2024.0651
[research_fan_wu_2017]: https://doi.org/10.2514/6.2017-2111
[research_fan_yan_2016]: https://doi.org/10.1155/2016/2402794
[research_fan_yan_2017]: https://doi.org/10.1177/1729881417699147
[research_fan_zhu_2016]: https://doi.org/10.3390/app6100312
[research_fang_jiang_2024]: https://doi.org/10.1109/ccssta62096.2024.10691869
[research_fang_xianyao_2020]: https://doi.org/10.1088/1757-899x/887/1/012031
[research_farahani_daliri_2019]: https://doi.org/10.1016/j.ast.2019.02.002
[research_farmakovsky_vinogradova_2005]: https://doi.org/10.2514/6.2005-920
[research_farrell_martin_1998]: https://doi.org/10.2514/6.1998-1539
[research_fatemi_lemmen_2006]: https://doi.org/10.2514/6.2006-8121
[research_fathauer_rogers_1993]: https://doi.org/10.2514/6.1993-2994
[research_faulkner_2003]: https://doi.org/10.2514/6.2003-7005
[research_faulkner_weber_1999]: https://doi.org/10.2514/6.1999-4922
[research_faulstich_law_2006]: https://doi.org/10.21236/ada619554
[research_fechter_mills_1988]: https://doi.org/10.2514/6.1988-2174
[research_fedioun_orlik_2012]: https://doi.org/10.2514/6.2012-5864
[research_fedorov_khokhlov_2001]: https://doi.org/10.1007/s001620100038
[research_fedorov_khokhlov_2002]: https://doi.org/10.1007/s001620100052
[research_feie_kretz_2008]: https://doi.org/10.21236/ada488092
[research_feifel_kerkam_1992]: https://doi.org/10.2514/6.1992-82
[research_fejer_heath_1964]: https://doi.org/10.21236/ad0603313
[research_felderman_shope_2003]: https://doi.org/10.2514/6.2003-7002
[research_feldmanjay_stewartdavid_2019]: https://ntrs.nasa.gov/citations/20190030273
[research_felippedasilvalui]: https://doi.org/10.47749/t/unicamp.2024.1384563
[research_fenfen_xubo_2020]: https://doi.org/10.1109/ccdc49329.2020.9164687
[research_feng_2022]: https://doi.org/10.1109/ccdc55256.2022.10033500
[research_feng_luo_2023]: https://doi.org/10.1016/j.applthermaleng.2022.119842
[research_feng_lv_2020]: https://doi.org/10.1007/s42401-020-00069-4
[research_feng_tan_2017]: https://doi.org/10.23919/chicc.2017.8028225
[research_feng_tang_2014]: https://doi.org/10.1007/s11434-014-0534-9
[research_feng_tang_2026]: https://doi.org/10.2139/ssrn.7359960
[research_feng_wang_2022]: https://doi.org/10.1109/ccdc55256.2022.10034211
[research_feng_zhang_2016]: https://doi.org/10.2991/icamcs-16.2016.138
[research_ferguson_andersonjr_1993]: https://doi.org/10.2514/6.1993-505
[research_ferguson_dasque_2015]: https://doi.org/10.2514/6.2015-1008
[research_ferguson_dasque_2016]: https://doi.org/10.2514/6.2016-0913
[research_ferguson_dasque_2018]: https://doi.org/10.2514/6.2018-0637
[research_ferguson_dhanasar_2011]: https://doi.org/10.2514/6.2011-404
[research_ferguson_dhanasar_2015]: https://doi.org/10.2514/6.2015-3508
[research_ferguson_feng_2022]: https://doi.org/10.1115/imece2022-96157
[research_fergusson]: https://doi.org/10.22215/etd/2019-13625
[research_ferlemann_2005]: https://doi.org/10.2514/6.2005-3352
[research_ferlemann_mcclinton_2005]: https://doi.org/10.2514/6.2005-3322
[research_fermencoker_johnson_1999]: https://doi.org/10.2514/6.1999-1430
[research_ferreira_carvalhojr_1996]: https://doi.org/10.2514/6.1996-2698
[research_ferrero_2020]: https://doi.org/10.3390/aerospace7030032
[research_ferrier_fedioun_2006]: https://doi.org/10.2514/6.2006-8092
[research_ferrier_orlik_2008]: https://doi.org/10.2514/6.2008-2599
[research_ferziger_leslie_1979]: https://doi.org/10.2514/6.1979-1471
[research_fetterhoff_burfitt_2011]: https://doi.org/10.2514/6.2011-2279
[research_fievet_koo_2015]: https://doi.org/10.2514/6.2015-3418
[research_filipkovskyi_2026]: https://doi.org/10.15421/472606
[research_finkler_weiser_1994]: https://doi.org/10.1364/iodc.1994.atpm.112
[research_finley_1990]: https://doi.org/10.2514/6.1990-5222
[research_finley_cockrell_1995]: https://doi.org/10.2514/6.1995-1831
[research_fiorentini_serrani_2009]: https://doi.org/10.1109/acc.2009.5160211
[research_fiorentini_serrani_2012]: https://doi.org/10.1016/j.automatica.2012.04.006
[research_fischer_2006]: https://doi.org/10.2514/6.2006-4026
[research_fischer_olivier_2011]: https://doi.org/10.2514/6.2011-2220
[research_fitch_1966]: https://doi.org/10.21236/ad0632828
[research_flaherty_andrews_2010]: https://doi.org/10.2514/1.43750
[research_flanaganjr_1993]: https://doi.org/10.2514/6.1993-2766
[research_fleming_olcman_2004]: https://doi.org/10.2514/6.2004-1200
[research_flesberg_taghavi_2018]: https://doi.org/10.2514/6.2018-5381
[research_fletcher_1967]: https://doi.org/10.1016/s0082-0784(67)80198-x
[research_fletcher_1994]: https://doi.org/10.2514/6.1994-2146
[research_flight_test_1959]: https://doi.org/10.1016/b978-1-4831-9727-2.50001-6
[research_flight_test_1965]: https://doi.org/10.1016/c2013-0-01867-1
[research_flight_test_2021]: https://doi.org/10.1002/9781118949818.ch6
[research_flightscienceslabincbuffalony_1964]: https://doi.org/10.21236/ad0442900
[research_flora_capasso_2019]: https://doi.org/10.1051/matecconf/201930402021
[research_florence_1979]: https://doi.org/10.2514/6.1979-1627
[research_flow_establishment_1990]: https://doi.org/10.2514/6.1990-2096
[research_foelsche_beckel_2006]: https://doi.org/10.2514/6.2006-8119
[research_fokin_2012]: https://doi.org/10.1134/s0018151x12030091
[research_fokin_2020]: https://doi.org/10.1134/s0018151x20020054
[research_folck_smith_1969]: https://doi.org/10.21236/ad0694516
[research_folweiler_1962]: https://doi.org/10.21236/ad0296433
[research_fontanmoura]: https://doi.org/10.14264/uql.2019.413
[research_fontijn_1987]: https://doi.org/10.1016/0010-2180(87)90072-1
[research_forbes_2012]: https://doi.org/10.1007/978-3-642-32535-9_12
[research_forbesspyratos_jahn_2014]: https://doi.org/10.2514/6.2014-2954
[research_forder_steiner_2020]: https://doi.org/10.5162/ettc2020/2.1
[research_foreman_1963]: https://doi.org/10.2514/6.1963-110
[research_forner_manter_1982]: https://doi.org/10.2514/6.1982-1085
[research_forrette_1964]: https://doi.org/10.2514/3.2273
[research_forster_droske_2016]: https://doi.org/10.1016/j.combustflame.2016.03.010
[research_forsythe_melfi_1961]: https://doi.org/10.21236/ad0672194
[research_fort_pratt_1990]: https://doi.org/10.2514/6.1990-735
[research_fotia_2015]: https://doi.org/10.2514/1.b35171
[research_fotia_driscoll_2012]: https://doi.org/10.2514/1.b34367
[research_fotia_driscoll_2013]: https://doi.org/10.2514/1.b34486
[research_franciscus_1981]: https://doi.org/10.2514/6.1981-1596
[research_franciscus_1981_b]: https://doi.org/10.2514/6.1981-1599
[research_franciscus_lezberg_1963]: https://doi.org/10.2514/6.1963-119
[research_franciscus_lezberg_1963_b]: https://doi.org/10.2514/6.1963-118
[research_franklin_bennett_1971]: https://doi.org/10.21236/ad0730089
[research_freed_dedecker_2001]: https://doi.org/10.1097/00002480-200103000-00052
[research_french_1988]: https://doi.org/10.2514/6.1988-2139
[research_frey_2014]: https://doi.org/10.21236/ada622072
[research_frey_jamme_2025]: https://doi.org/10.1007/978-981-96-4767-5_2
[research_friedauer_segal_1996]: https://doi.org/10.2514/6.1996-3239
[research_friedman_1965]: https://doi.org/10.21236/ad0474140
[research_friedman_bennet_1953]: https://doi.org/10.1016/s0082-0784(53)80099-8
[research_friedman_griffith_1967]: https://doi.org/10.21236/ad0815931
[research_frisch_giedt_1965]: https://doi.org/10.2172/4585585
[research_frisch_giedt_1965_b]: https://doi.org/10.2172/4598505
[research_froning_2006]: https://doi.org/10.2514/6.2006-8014
[research_froningjr_1986]: https://doi.org/10.2514/6.1986-444
[research_froningjr_bussard_1993]: https://doi.org/10.2514/6.1993-2611
[research_froningjr_mckinney_1996]: https://doi.org/10.2514/6.1996-4519
[research_froningjr_roach_1999]: https://doi.org/10.2514/6.1999-4878
[research_frost]: https://doi.org/10.14264/uql.2020.593
[research_fryronalds_beckerdorothyl_2000]: https://ntrs.nasa.gov/citations/20010036862
[research_fryronalds_gannawaymaryt_1998]: https://ntrs.nasa.gov/citations/19990114846
[research_fryronalds_gannawaymaryt_2002]: https://ntrs.nasa.gov/citations/20020073093
[research_fu_bose_2021]: https://doi.org/10.1007/s00162-021-00587-7
[research_fu_gong_2026]: https://doi.org/10.1063/5.0323065
[research_fu_li_2018]: https://doi.org/10.1109/ccdc.2018.8407404
[research_fu_qu_2022]: https://doi.org/10.1016/j.ast.2022.107470
[research_fu_song_2023]: https://doi.org/10.1016/j.energy.2022.126438
[research_fu_song_2024]: https://doi.org/10.1016/j.actaastro.2023.12.029
[research_fu_song_2024_b]: https://doi.org/10.1515/tjj-2024-0085
[research_fu_wan_2024]: https://doi.org/10.1590/jatm.v16.1355
[research_fu_wang_2015]: https://doi.org/10.1155/2015/293480
[research_fuel_cell_2007]: https://doi.org/10.1108/aeat.2007.12779daf.013
[research_fuel_in_1998]: https://doi.org/10.1016/s0140-6701(98)93568-8
[research_fuels_for_2022]: https://doi.org/10.1002/9781119640646.ch6
[research_fujii_inoue_1998]: https://doi.org/10.2514/6.1998-605
[research_fujii_watanabe_2000]: https://doi.org/10.2514/6.2000-267
[research_fujii_watanabe_2001]: https://doi.org/10.2514/2.3665
[research_fujimatsu_kito_2019]: https://doi.org/10.2495/mpf190061
[research_fujio_ogawa_2021]: https://doi.org/10.2514/6.2021-1961
[research_fujio_taguchi_2026]: https://doi.org/10.1007/s12567-026-00722-2
[research_fujioka_hirokawa_2017]: https://doi.org/10.1115/icone25-67999
[research_fujita_suzuki_2011]: https://doi.org/10.1063/1.3562682
[research_fukuda_reshotko_1975]: https://doi.org/10.2514/6.1975-1182
[research_fukutani_watanabe_1986]: https://doi.org/10.4271/860035
[research_fukuzawa_iguchi_2025]: https://doi.org/10.52202/083090-0142
[research_fulmer_wirtz_1964]: https://doi.org/10.21236/ad0618368
[research_fulton_1966]: https://doi.org/10.1128/am.14.2.237-240.1966
[research_fureby_nilsson_2025]: https://doi.org/10.2514/1.j064432
[research_fureby_peterson_2025]: https://doi.org/10.2514/6.2025-0391
[research_furstenau_1965]: https://doi.org/10.2514/6.1965-272
[research_further_development_1994]: https://doi.org/10.2514/6.1994-2141
[research_fusaro_viola_2020]: https://doi.org/10.2514/6.2020-1106
[research_g_kaushik_2017]: https://doi.org/10.2514/6.2017-3911
[research_g_kaushik_2017_b]: https://doi.org/10.2514/6.2017-4124
[research_gaal_1974]: https://doi.org/10.1063/1.2945915
[research_gabrys_smith_1974]: https://doi.org/10.21236/ada008893
[research_gaede_lopez_1967]: https://doi.org/10.2514/6.1967-453
[research_gager_schleter_1949]: https://doi.org/10.21236/ada472247
[research_gaglio_bevilacqua_2026]: https://doi.org/10.2514/6.2026-3119
[research_gaiduchenko_gritsyk_2019]: https://doi.org/10.1109/ent47717.2019.9030537
[research_galaktionov_lapygin_2006]: https://doi.org/10.2514/6.iac-06-d2.3.07
[research_galera_mohammadi_2006]: https://doi.org/10.1080/10618560600835280
[research_gallegos_schlussel_2024]: https://doi.org/10.2514/6.2024-1414
[research_gallegos_schlussel_2024_b]: https://doi.org/10.2514/1.j063964
[research_galli_corbel_2004]: https://doi.org/10.2514/6.2004-5199
[research_gallo_gnos_1966]: https://doi.org/10.2514/6.1966-606
[research_gally_campbell_2002]: https://doi.org/10.2514/6.2002-3139
[research_gamble_giel_2008]: https://doi.org/10.2514/6.2008-5173
[research_gamble_haid_2009]: https://doi.org/10.2514/6.2009-5298
[research_gamertsfelder_khare_2022]: https://doi.org/10.21236/ad1160084
[research_ganapuram_jangam_2014]: https://doi.org/10.1115/gt2014-25296
[research_gany_2006]: https://doi.org/10.2514/6.2006-4567
[research_gao_2023]: https://doi.org/10.54254/2753-8818/11/20230391
[research_gao_an_2021]: https://doi.org/10.1016/b978-0-12-822990-3.00008-5
[research_gao_chang_2012]: https://doi.org/10.4028/www.scientific.net/amr.468-471.2620
[research_gao_chen_2018]: https://doi.org/10.12783/dtcse/pcmm2018/23663
[research_gao_chen_2020]: https://doi.org/10.1016/j.conengprac.2020.104426
[research_gao_gou_2021]: https://doi.org/10.1016/j.compstruct.2021.113962
[research_gao_he_2026]: https://doi.org/10.1063/5.0322431
[research_gao_jiang_2014]: https://doi.org/10.2514/6.2014-4415
[research_gao_li_2014]: https://doi.org/10.1109/cgncc.2014.7007365
[research_gao_li_2015]: https://doi.org/10.1007/s11433-015-5710-7
[research_gao_li_2024]: https://doi.org/10.1109/aaac63570.2024.11027380
[research_gao_liu_2026]: https://doi.org/10.2514/1.g009823
[research_gao_song_2021]: https://doi.org/10.1115/imece2021-73853
[research_gao_sun_2024]: https://doi.org/10.1016/j.actaastro.2024.09.037
[research_gao_wang_2023]: https://doi.org/10.1016/j.undsp.2022.03.007
[research_gao_zhang_2020]: https://doi.org/10.1051/matecconf/202031603002
[research_gao_zhang_2020_b]: https://doi.org/10.1088/1742-6596/1634/1/012157
[research_gao_zhang_2020_c]: https://doi.org/10.1088/1742-6596/1634/1/012159
[research_gao_zhang_2024]: https://doi.org/10.1109/epee63731.2024.10875497
[research_garavello_kneish_2024]: https://doi.org/10.21203/rs.3.rs-4750685/v1
[research_gardi_delvecchio_2015]: https://doi.org/10.2514/6.2015-3640
[research_gardner_1964]: https://doi.org/10.21236/ad0608653
[research_gardner_paull_2002]: https://doi.org/10.1007/s001930200120
[research_garman_visintainer_2022]: https://doi.org/10.1115/fedsm2022-87040
[research_garrison_settles_1994]: https://doi.org/10.2514/6.1994-2274
[research_gartling_1970]: https://doi.org/10.21236/ad0734154
[research_gary_mcdonald_2014]: https://doi.org/10.2514/6.2014-0553
[research_gas_temperature_density_1974]: https://doi.org/10.2514/5.9781600865077.0355.0370
[research_gasner_foster_1992]: https://doi.org/10.2514/6.1992-3721
[research_gates_adrezin_1999]: https://doi.org/10.2514/6.1999-836
[research_gawehn_schleutker_2022]: https://doi.org/10.1007/s00348-022-03392-y
[research_gay_brehm_2025]: https://doi.org/10.2514/6.2025-100189
[research_gazaix_1992]: https://doi.org/10.1007/978-3-642-77922-0_56
[research_gbalu_panneerselvam_2005]: https://doi.org/10.1515/tjj.2005.22.4.255
[research_ge_gan_2026]: https://doi.org/10.2139/ssrn.6796508
[research_gea_vicker]: https://doi.org/10.1007/3-540-31801-1_30
[research_geerts_yu_2012]: https://doi.org/10.2514/6.2012-5891
[research_geerts_yu_2013]: https://doi.org/10.2514/6.2013-3102
[research_geerts_yu_2015]: https://doi.org/10.2514/6.2015-1486
[research_geerts_yu_2017]: https://doi.org/10.2514/1.j054991
[research_gehre]: https://doi.org/10.14264/uql.2015.772
[research_gehre_wheatley_2015]: https://doi.org/10.2514/6.2015-3507
[research_geiger_strahan_2024]: https://doi.org/10.2514/6.2024-1191
[research_geiger_strahan_2026]: https://doi.org/10.2514/1.j067064
[research_generaldynamicsastronauticssandiegoca_1961]: https://doi.org/10.21236/ad0843112
[research_generaldynamicsastronauticssandiegoca_1961_b]: https://doi.org/10.21236/ad0843200
[research_generaldynamicsastronauticssandiegoca_1962]: https://doi.org/10.21236/ad0852659
[research_geng_liu_2017]: https://doi.org/10.12783/dtmse/icmea2015/7363
[research_genin_menon_2004]: https://doi.org/10.2514/6.2004-4132
[research_george_1963]: https://doi.org/10.21236/ad0296089
[research_georgesdelwert_georgeltetberg_1998]: https://ntrs.nasa.gov/citations/19990024921
[research_gerbsch_agarwal_1988]: https://doi.org/10.2514/6.1988-2828
[research_gernansky_1990]: https://doi.org/10.21236/ada218666
[research_gerolymos_sauret_2003]: https://doi.org/10.2514/6.2003-3465
[research_geshele_polezhaev_2013]: https://doi.org/10.1134/s0018151x13050076
[research_ghenai_philippidis_2005]: https://doi.org/10.21236/ada443378
[research_ghodke_choi_2011]: https://doi.org/10.2514/6.2011-323
[research_ghori_narendar_2023]: https://doi.org/10.4028/p-oah3jt
[research_ghosh_ogawa_2022]: https://doi.org/10.2514/6.2022-2734
[research_giampetro_2026]: https://doi.org/10.2514/6.2026-110256
[research_giampetro_lindau_2026]: https://doi.org/10.2514/6.2026-4398
[research_giant_liquid_1955]: https://doi.org/10.1016/0016-0032(55)90724-9
[research_gibbons_damm_2021]: https://doi.org/10.2514/6.2021-4141
[research_gibson_armiger_2016]: https://doi.org/10.21236/ad1013367
[research_gibson_neidhoefer_2002]: https://doi.org/10.2514/6.2002-3462
[research_gidzak_2015]: https://doi.org/10.2514/6.2015-3590
[research_giehler]: https://doi.org/10.70675/f89d404azf4a7z42e9zbf45z2c5ddd55317f
[research_giehler_grenson_2023]: https://doi.org/10.21203/rs.3.rs-2533029/v1
[research_gilinsky_gonor_2003]: https://doi.org/10.2514/6.2003-7044
[research_gillum_kammeyer_1994]: https://doi.org/10.2514/6.1994-2476
[research_gimelshein_2019]: https://doi.org/10.2514/6.2019-2063
[research_ginoux_1966]: https://doi.org/10.21236/ad0647819
[research_girimaji_srinivasan_2009]: https://doi.org/10.2514/6.2009-134
[research_gksuryanarayana_dbsingh_2026]: https://doi.org/10.14429/dsj.20972
[research_gladden_melis_1990]: https://doi.org/10.2514/6.1990-53
[research_gladden_melis_1994]: https://doi.org/10.1115/imece1994-1617
[research_glass_2003]: https://doi.org/10.2514/6.2003-3772
[research_glass_2008]: https://doi.org/10.2514/6.2008-2682
[research_glass_2018]: https://doi.org/10.2514/5.9781624104893.0531.0578
[research_glass_glass_2002]: https://doi.org/10.2514/6.2002-5137
[research_glass_sislian_1994]: https://doi.org/10.1093/oso/9780198593881.003.0007
[research_glassman_1998]: https://doi.org/10.21236/ada353435
[research_glassman_nosek_1971]: https://doi.org/10.2514/6.1971-662
[research_glazov_pashinkin_2001]: https://doi.org/10.1023/a:1017562709942
[research_glazov_pashinkin_2002]: https://doi.org/10.1023/a:1016059923422
[research_glenning_bond_1962]: https://doi.org/10.1111/j.1479-828x.1962.tb00187.x
[research_glickstein_powell_1987]: https://doi.org/10.2514/6.1987-2003
[research_glicksteinmr_spadaccinilj_1997]: https://ntrs.nasa.gov/citations/19990028568
[research_gnoffo_1989]: https://doi.org/10.2514/6.1989-1972
[research_gnoffo_2007]: https://doi.org/10.2514/6.2007-3960
[research_gnoffopetera_2001]: https://ntrs.nasa.gov/citations/20010071532
[research_gnoffopetera_mccandlessronalds_1987]: https://ntrs.nasa.gov/citations/19870035258
[research_gockel_1993]: https://doi.org/10.2514/6.1993-5090
[research_godi_2024]: https://doi.org/10.2139/ssrn.4823483
[research_gogineni_1991]: https://doi.org/10.2514/6.1991-1704
[research_goin_1961]: https://doi.org/10.21236/ad0262842
[research_gokulakrishnan_pal_2006]: https://doi.org/10.2514/6.2006-5092
[research_goldbaum_1956]: https://doi.org/10.21236/ad0092263
[research_goldberg_scala_1965]: https://doi.org/10.21236/ad0623553
[research_goldfeld_1985]: https://doi.org/10.1007/bf01050086
[research_goldfeld_2003]: https://doi.org/10.2514/6.2003-4247
[research_goldfeld_2019]: https://doi.org/10.1088/1742-6596/1382/1/012076
[research_goldfeld_korotaeva_2019]: https://doi.org/10.1134/s0869864319050020
[research_goldfeld_nestoulia_2003]: https://doi.org/10.2514/6.2003-14
[research_gollan_gollan_2011]: https://doi.org/10.2514/6.2011-2254
[research_gollan_smart_2013]: https://doi.org/10.2514/1.b34672
[research_gollanrowanj_smartmichaelk_2010]: https://ntrs.nasa.gov/citations/20100002815
[research_golovachev_1979]: https://doi.org/10.1007/bf01409832
[research_golovachev_1979_b]: https://doi.org/10.1007/bf01052007
[research_golovachev_1981]: https://doi.org/10.1007/bf01094832
[research_golubinskii_golubkin_1983]: https://doi.org/10.1007/bf01090751
[research_golubkin_1992]: https://doi.org/10.1007/bf01051615
[research_golubkin_negoda_1995]: https://doi.org/10.1007/bf00312398
[research_golubkin_postnov_2000]: https://doi.org/10.1007/bf02831438
[research_gong_bing_2017]: https://doi.org/10.2514/6.2017-2318
[research_gong_long_2024]: https://doi.org/10.1186/s42774-024-00181-5
[research_gong_yuan_2006]: https://doi.org/10.2514/6.2006-7994
[research_gongweijie_tangshuo_2010]: https://doi.org/10.1109/iccda.2010.5541259
[research_gonzalez_1996]: https://doi.org/10.2514/6.1996-4560
[research_gonzalez_castillo_2025]: https://doi.org/10.2514/6.2025-2634
[research_gooch_2011]: https://doi.org/10.1007/978-1-4419-6247-8_879
[research_gooch_2011_b]: https://doi.org/10.1007/978-1-4419-6247-8_11129
[research_goodwin_maxwell_2017]: https://doi.org/10.2514/6.2017-4651
[research_goonko_latypov_2003]: https://doi.org/10.2514/2.1965
[research_gopal_wilson_2016]: https://doi.org/10.2514/6.2016-1167
[research_gopinath_jagadeesh_2019]: https://doi.org/10.1111/jace.16548
[research_gopinath_vignesh_2015]: https://doi.org/10.2514/6.2015-3558
[research_gorshkov_lunev_2002]: https://doi.org/10.1023/a:1021380605136
[research_goshima_miyao_1991]: https://doi.org/10.1016/0029-5493(91)90030-l
[research_gospodarev_isakina_1990]: https://doi.org/10.1063/10.0032615
[research_goss_cook_1948]: https://doi.org/10.4271/480228
[research_gottlieb_don_2008]: https://doi.org/10.21236/ada483410
[research_gottlieb_mines_2024]: https://doi.org/10.2514/6.2024-0373
[research_gounko_shumskiy_2014]: https://doi.org/10.1134/s0869864314040106
[research_goyal_prasad_2023]: https://doi.org/10.2514/6.2023-3022
[research_goyne_hall_2006]: https://doi.org/10.2514/6.2006-7901
[research_goz_theodoulis_2025]: https://doi.org/10.2514/6.2025-2266
[research_graber_1964]: https://doi.org/10.21236/ad0608869
[research_grady_madzsar_1998]: https://doi.org/10.2514/6.1998-3773
[research_grady_pitz_2016]: https://doi.org/10.1016/j.combustflame.2015.12.014
[research_graham]: https://doi.org/10.14264/f62a6ba
[research_grainger_brieschenk_2014]: https://doi.org/10.2514/6.2014-3230
[research_grant_2013]: https://doi.org/10.2514/6.2013-4503
[research_grantz_cervisi_1993]: https://doi.org/10.2514/6.1993-511
[research_grasso_falconi_1993]: https://doi.org/10.2514/6.1993-778
[research_gray_1965]: https://doi.org/10.21236/ad0609841
[research_green]: https://doi.org/10.18130/v3w65b
[research_green_fernandez_1994]: https://doi.org/10.2514/6.1994-2107
[research_gregorek_lee_1962]: https://doi.org/10.21236/ad0288297
[research_gregory_2005]: https://doi.org/10.1063/1.1925177
[research_gregory_wilcox_1967]: https://doi.org/10.2514/6.1967-493
[research_grimm_1993]: https://doi.org/10.1016/b978-0-08-041715-8.50072-9
[research_gringorten_1967]: https://doi.org/10.21236/ad0656309
[research_gringorten_tattelman_1970]: https://doi.org/10.21236/ad0712017
[research_grohens_dufour_2000]: https://doi.org/10.2514/6.2000-3345
[research_grolmes_1968]: https://doi.org/10.2172/5021859
[research_gronland_cambier_1997]: https://doi.org/10.2514/6.1997-3166
[research_gros_1963]: https://doi.org/10.21236/ad0436090
[research_grossir_2015]: https://doi.org/10.35294/phdt201505
[research_grossir_rambaud_2014]: https://doi.org/10.2514/6.2014-1153
[research_grossmanb_cinnellap_1990]: https://ntrs.nasa.gov/citations/19900047492
[research_ground_zhu_2014]: https://doi.org/10.2514/6.2014-2952
[research_groves_serrani_2005]: https://doi.org/10.21236/ada444973
[research_gruber_donbar_2004]: https://doi.org/10.2514/1.5360
[research_gruenig_mayinger_1999]: https://doi.org/10.1080/00102209908924205
[research_gruhn_gulhan_2011]: https://doi.org/10.2514/1.50347
[research_grunbok_miles_2023]: https://doi.org/10.2514/6.2023-2052
[research_gu_xu_2009]: https://doi.org/10.2514/6.2009-7350
[research_gu_xu_2010]: https://doi.org/10.2514/6.2010-7070
[research_guan_wang_2013]: https://doi.org/10.1109/ccdc.2013.6560923
[research_guan_yarng_1987]: https://doi.org/10.2514/6.1987-2053
[research_guangbincai_guangrenduan_2010]: https://doi.org/10.1109/isscaa.2010.5633419
[research_guangren_yanmei_2015]: https://doi.org/10.1109/chicc.2015.7260541
[research_guanping_xueli_2012]: https://doi.org/10.1109/ccdc.2012.6243059
[research_gubanov_2019]: https://doi.org/10.1186/s42774-019-0013-8
[research_guderley_1987]: https://doi.org/10.21236/ada193773
[research_guderley_1988]: https://doi.org/10.21236/ada191408
[research_gudimella_sinha_2018]: https://doi.org/10.1615/ihmtc-2017.1410
[research_guelhan_siebe_2012]: https://doi.org/10.2514/6.2012-5819
[research_gugulothu_2020]: https://doi.org/10.1002/htj.21856
[research_gugulothu_nutakki_2019]: https://doi.org/10.1016/j.csite.2019.100448
[research_guizzo_2004]: https://doi.org/10.1109/mspec.2004.1317885
[research_gulcat_2010]: https://doi.org/10.1007/978-3-642-14761-6_7
[research_gulcat_2015]: https://doi.org/10.1007/978-981-10-0018-8_7
[research_gulcat_2021]: https://doi.org/10.1007/978-3-030-60777-7_7
[research_gunderson_1963]: https://doi.org/10.2514/3.1574
[research_gunning_luner_1954]: https://doi.org/10.21236/ad0035690
[research_gunning_luner_1954_b]: https://doi.org/10.21236/ad0040238
[research_guo_fu_2025]: https://doi.org/10.3390/aerospace12040286
[research_guo_gao_2017]: https://doi.org/10.1007/978-3-319-46213-4_25
[research_guo_liu_2024]: https://doi.org/10.1360/ssi-2023-0285
[research_guo_pang_2022]: https://doi.org/10.3390/en15155332
[research_guo_pang_2023]: https://doi.org/10.1016/j.cja.2022.07.012
[research_guo_wang_2016]: https://doi.org/10.1109/chicc.2016.7555084
[research_guo_yang_2023]: https://doi.org/10.23919/ccc58697.2023.10240784
[research_guoliang_cong_2017]: https://doi.org/10.2514/6.2017-2129
[research_guotongsun_shuotang_2010]: https://doi.org/10.1109/icent.2010.5532272
[research_gupta]: https://doi.org/10.14264/923d57d
[research_gupta_agarwal_2001]: https://doi.org/10.2514/6.2001-199
[research_gupta_b]: https://doi.org/10.70675/80705d16zf54cz4d27z8ea2z49d17cd6100b
[research_gurtin_soner_1990]: https://doi.org/10.21236/ada244289
[research_gusev_1990]: https://doi.org/10.2514/6.1990-5271
[research_gusev_blagoveshchenskij_1993]: https://doi.org/10.2514/6.1993-5034
[research_gusev_chinilov_2003]: https://doi.org/10.1023/a:1026334113926
[research_guven_dane_1996]: https://doi.org/10.21236/ada327247
[research_guza_feddersen_2015]: https://doi.org/10.21236/ada614273
[research_guzmanbohorquez_greco_2025]: https://doi.org/10.26678/abcm.cobem2023.cob2023-2028
[research_gyulikhandanov_khoroshailov_1971]: https://doi.org/10.1007/bf00651783
[research_ha_yoon_2018]: https://doi.org/10.6108/kspe.2018.22.1.045
[research_haas_karanian_1980]: https://doi.org/10.2514/6.1980-1145
[research_habrard_pommierbudinger_2025]: https://doi.org/10.3390/aerospace12050377
[research_hack]: https://doi.org/10.14264/c0880c7
[research_hackett_1992]: https://doi.org/10.2514/6.1992-4011
[research_hadjadj_dussauge_2009]: https://doi.org/10.1007/s00193-009-0238-2
[research_hagenmaier_boles_2013]: https://doi.org/10.21236/ada589252
[research_hagenmaier_eklund_2011]: https://doi.org/10.21236/ada543745
[research_hagenmaier_sekar_1997]: https://doi.org/10.2514/6.1997-3390
[research_hagsethpaule_blanksonisaiahm_1993]: https://ntrs.nasa.gov/citations/19930041524
[research_hagy_1986]: https://doi.org/10.1364/oam.1986.ws6
[research_hahn_2012]: https://doi.org/10.2514/6.2012-547
[research_hahn_lax_2026]: https://doi.org/10.2514/1.j065811
[research_halas_1979]: https://doi.org/10.1088/0022-3735/12/5/020
[research_haley_zhong_2017]: https://doi.org/10.2514/6.2017-4514
[research_hall_1994]: https://doi.org/10.21236/ada279665
[research_hall_poggie_2019]: https://doi.org/10.2514/6.2019-0946
[research_hall_schemmel_2026]: https://doi.org/10.2514/6.2026-4402
[research_hallgren_andersonjr_1991]: https://doi.org/10.2514/6.1991-3323
[research_hallion_1998]: https://doi.org/10.21236/ada441127
[research_hallion_becker_1995]: https://doi.org/10.21236/ada302634
[research_halljl_2002]: https://ntrs.nasa.gov/citations/20060029898
[research_halter_cliff_1991]: https://doi.org/10.2514/6.1991-2713
[research_halvarsson_1995]: https://doi.org/10.1016/02578-9729(50)25588-
[research_hamba_2001]: https://doi.org/10.1007/s001620050143
[research_hamba_2003]: https://doi.org/10.1007/s00162-003-0089-x
[research_hamed_1990]: https://doi.org/10.2514/6.1990-1928
[research_hamed_1993]: https://doi.org/10.21236/ada268106
[research_hameda_kumarajay_1992]: https://ntrs.nasa.gov/citations/19930035432
[research_hammack_ombrello_2021]: https://doi.org/10.1016/j.proci.2020.06.372
[research_hammond_1965]: https://doi.org/10.2172/4597267
[research_hamner_2003]: https://doi.org/10.2514/6.2003-6962
[research_han_han_2024]: https://doi.org/10.1063/5.0196415
[research_han_sun_2020]: https://doi.org/10.1016/j.ast.2019.105673
[research_han_wang_2024]: https://doi.org/10.2139/ssrn.4853594
[research_han_wang_2024_b]: https://doi.org/10.23919/ccc63176.2024.10661992
[research_han_yang_2027]: https://doi.org/10.1016/j.fuel.2026.140421
[research_han_yu_2025]: https://doi.org/10.2139/ssrn.5527236
[research_hanafi]: https://doi.org/10.22215/etd/1974-13047
[research_hanai_ozawa_2007]: https://doi.org/10.2514/6.2007-4220
[research_haney_1995]: https://doi.org/10.2514/6.1995-6162
[research_haney_cervisi_1993]: https://doi.org/10.2514/6.1993-402
[research_hank_franke_2006]: https://doi.org/10.2514/6.2006-4962
[research_hank_murphy_2008]: https://doi.org/10.2514/6.2008-2540
[research_hannah_muessig_1970]: https://doi.org/10.21236/ada955972
[research_hannemann_martinezschramm_2015]: https://doi.org/10.2514/6.2015-3608
[research_hannemann_martinezschramm_2017]: https://doi.org/10.2514/6.2017-2235
[research_hanquist_boyd_2018]: https://doi.org/10.2514/6.2018-1714
[research_hansencfrederick_1991]: https://ntrs.nasa.gov/citations/19910034691
[research_hanumantharao_2023]: https://doi.org/10.22211/cejem/176917
[research_hao_chang_2014]: https://doi.org/10.1109/chicc.2014.6896749
[research_hao_chang_2016]: https://doi.org/10.1016/j.ast.2015.12.001
[research_hao_chang_2016_b]: https://doi.org/10.2514/6.2016-1020
[research_hao_chung_1994]: https://doi.org/10.1080/10618569408904487
[research_hao_wang_2016]: https://doi.org/10.1016/j.actaastro.2016.04.014
[research_hao_yongqi_2024]: https://doi.org/10.23919/ccc63176.2024.10662106
[research_hardie_obyrne_2025]: https://doi.org/10.2514/6.2025-106569
[research_harloff_1984]: https://doi.org/10.2172/5248985
[research_harloff_1987]: https://doi.org/10.2514/6.1987-2548
[research_harloff_petrie_1987]: https://doi.org/10.2514/6.1987-2545
[research_harney_1963]: https://doi.org/10.21236/ad0295147
[research_harney_petrie_1971]: https://doi.org/10.2514/6.1971-252
[research_harri_1964]: https://doi.org/10.2172/4597699
[research_harris_2004]: https://doi.org/10.21236/ada426816
[research_harris_albacete_1964]: https://doi.org/10.21236/ad0601590
[research_harris_hines_1994]: https://doi.org/10.2514/6.1994-2149
[research_harris_stokes_2023]: https://doi.org/10.2514/6.2023-0711
[research_harrison_1976]: https://doi.org/10.1016/0008-6223(76)90253-0
[research_hart_1992]: https://doi.org/10.2514/6.1992-4118
[research_hartillwr_goebeltp_1978]: https://ntrs.nasa.gov/citations/19780011153
[research_harvey_2011]: https://doi.org/10.1017/cbo9780511842757.008
[research_hasegawa_2025]: https://doi.org/10.2514/6.2025-1335
[research_hasen_karthikeyan_2019]: https://doi.org/10.4273/ijvss.11.2.22
[research_hass_cabell_2011]: https://doi.org/10.2514/6.2011-2248
[research_hassan_candler_1992]: https://doi.org/10.2514/6.1992-2877
[research_hassan_kuntz_2001]: https://doi.org/10.2514/6.2001-2903
[research_hassneale_cabellkarenf_2010]: https://ntrs.nasa.gov/citations/20100002215
[research_hatayama_tanaka_2025]: https://doi.org/10.2139/ssrn.5433522
[research_hattis_1990]: https://doi.org/10.23919/acc.1990.4791043
[research_hawkins_marquart_1995]: https://doi.org/10.2514/6.1995-6019
[research_hawkins_richardson_1991]: https://doi.org/10.2514/6.1991-3179
[research_hayashi_aso_1988]: https://doi.org/10.2514/6.1988-426
[research_hayes_1959]: https://doi.org/10.1016/b978-1-4831-9832-3.50009-7
[research_hazarika_ahmed_2021]: https://doi.org/10.48048/wjst.2021.22834
[research_he_2015]: https://doi.org/10.2514/6.2015-3685
[research_he_chen_2022]: https://doi.org/10.1063/5.0095277
[research_he_gao_2021]: https://doi.org/10.1186/s42774-021-00070-1
[research_he_le_2009]: https://doi.org/10.2514/6.2009-7423
[research_he_li_2015]: https://doi.org/10.1016/j.fuel.2015.08.066
[research_he_liu_2016]: https://doi.org/10.1109/chicc.2016.7554181
[research_he_liu_2017]: https://doi.org/10.1109/ccdc.2017.7978630
[research_he_liu_2023]: https://doi.org/10.3390/en16031025
[research_he_tian_2022]: https://doi.org/10.1016/j.actaastro.2022.01.012
[research_he_wang_2022]: https://doi.org/10.3390/aerospace9100566
[research_he_zhang_2026]: https://doi.org/10.1016/j.applthermaleng.2026.130658
[research_he_zhou_2026]: https://doi.org/10.2139/ssrn.6926147
[research_head_1981]: https://doi.org/10.2514/6.1981-2506
[research_heat_transfer_1991]: https://doi.org/10.1016/0890-4332(91)90158-z
[research_heathman_kelly_1966]: https://doi.org/10.2514/6.1966-1740
[research_heberling_2020]: https://doi.org/10.2514/6.2020-2757
[research_hedges_lewis_1996]: https://doi.org/10.2514/6.1996-493
[research_hegde_reuter_1987]: https://doi.org/10.2514/6.1987-216
[research_heinbockeljh_landryjg_1995]: https://ntrs.nasa.gov/citations/19960000685
[research_heinrich_1954]: https://doi.org/10.21236/ad0041737
[research_heinrich_lucbouhali_2001]: https://doi.org/10.2514/6.2001-1785
[research_heiser_2007]: https://doi.org/10.2514/1.23962
[research_heiser_pratt_1994]: https://doi.org/10.2514/4.470356
[research_heiser_pratt_2005]: https://doi.org/10.2514/1.b4775tc
[research_heitmeier_bissinger_1995]: https://doi.org/10.2514/6.1995-6027
[research_heitmeir_lederer_1992]: https://doi.org/10.2514/6.1992-5057
[research_hejranfar_moghadam_2011]: https://doi.org/10.1007/978-3-642-17884-9_60
[research_hejranfar_najafi_2011]: https://doi.org/10.1007/978-3-642-17884-9_44
[research_helgeson_chinitz_1995]: https://doi.org/10.2514/6.1995-2768
[research_helicopter_engine_airframe]: https://doi.org/10.4271/arp1507b
[research_heller_holzapfel_2000]: https://doi.org/10.2514/6.2000-4248
[research_heller_sachs_1998]: https://doi.org/10.2514/6.1998-1521
[research_hemanth_jagadeesh_2009]: https://doi.org/10.1007/978-3-540-85168-4_113
[research_hemming_1966]: https://doi.org/10.1108/eb034116
[research_henckels_maurer]: https://doi.org/10.1109/iciasf.1989.77708
[research_henderson_1987]: https://doi.org/10.4271/872411
[research_henderson_1991]: https://doi.org/10.1115/1.2906530
[research_henderson_1999]: https://doi.org/10.2514/6.1999-369
[research_henry_1969]: https://doi.org/10.1016/s0082-0784(69)80494-7
[research_henshall_brower_1962]: https://doi.org/10.1007/978-1-4757-0531-7_9
[research_henson_2017]: https://doi.org/10.4050/f-0073-2017-12151
[research_henson_robertson_1962]: https://doi.org/10.21236/ad0275641
[research_heo_sung_2017]: https://doi.org/10.2514/6.2017-2240
[research_herbert]: https://doi.org/10.1007/10339647_21
[research_herbert_1992]: https://doi.org/10.21236/ada250900
[research_herdy_2025]: https://doi.org/10.2514/6.2025-1325
[research_herdy_2025_b]: https://doi.org/10.2514/6.2025-3680
[research_herdy_2026]: https://doi.org/10.2514/6.2026-2174
[research_herges_dutton_2012]: https://doi.org/10.2514/6.2012-4146
[research_herling_saheli_1985]: https://doi.org/10.2514/6.1985-1121
[research_hermann_1950]: https://doi.org/10.21236/ada377566
[research_hermann_schmidt_1995]: https://doi.org/10.2514/6.1995-3372
[research_hermannr_1965]: https://ntrs.nasa.gov/citations/19660012369
[research_herrlin_gelderloos_1988]: https://doi.org/10.2514/6.1988-3877
[research_herrmann_cox_2025]: https://doi.org/10.2514/6.2025-1338
[research_herrmann_gulhan_2015]: https://doi.org/10.2514/1.b35339
[research_herrmann_siebe_2013]: https://doi.org/10.2514/1.b34629
[research_hersh_gerstein_1970]: https://doi.org/10.21236/ad0714109
[research_hertzberg_wittliff_1961]: https://doi.org/10.21236/ad0260731
[research_hexia_huijun_2014]: https://doi.org/10.2514/6.2014-3846
[research_hicksjohnw_1992]: https://ntrs.nasa.gov/citations/19930030641
[research_higashino_matsuo_1995]: https://doi.org/10.1007/978-3-642-79532-9_34
[research_higgins_inger_2002]: https://doi.org/10.2514/6.2002-3312
[research_high_altitude_atmospheric_1960]: https://doi.org/10.1016/0042-207x(60)90304-3
[research_high_altitude_atmospheric_1960_b]: https://doi.org/10.1016/0042-207x(60)90212-8
[research_high_specific_1987]: https://doi.org/10.2514/6.1987-2051
[research_high_temperature]: https://doi.org/10.1887/0750307420/b873c19
[research_high_temperature_gas_2009]: https://doi.org/10.1017/cbo9780511627019.004
[research_high_temperature_investigations_2018]: https://doi.org/10.26902/jsc20180831
[research_high_temperature_materials_2014]: https://doi.org/10.1201/b16545-10
[research_high_temperature_materials_2014_b]: https://doi.org/10.1201/b16545-6
[research_high_temperature_materials_2014_c]: https://doi.org/10.1201/b16545-21
[research_hildebrand_1979]: https://doi.org/10.2514/6.1979-1787
[research_hill_brown_2004]: https://doi.org/10.2514/6.2004-6403
[research_hillaker_1983]: https://doi.org/10.2514/6.1983-2730
[research_hillier_netterfield_1990]: https://doi.org/10.1063/1.39454
[research_hinderks_gulhan_2004]: https://doi.org/10.2514/6.2004-2238
[research_hiraiwa_tomioka_1995]: https://doi.org/10.2514/6.1995-2579
[research_hirsch_grossir_2023]: https://doi.org/10.2514/6.2023-1816
[research_hirschel_meier_2004]: https://doi.org/10.1007/978-3-642-18484-0_16
[research_hirschel_staudacher_2025]: https://doi.org/10.1007/978-3-031-94219-8_4
[research_hirschel_staudacher_2025_b]: https://doi.org/10.1007/978-3-031-94219-8_5
[research_hirschel_weiland_2009]: https://doi.org/10.1007/978-3-540-89974-7_4
[research_hirschel_weiland_2009_b]: https://doi.org/10.1007/978-3-540-89974-7_9
[research_hitch_lynch_2009]: https://doi.org/10.2514/6.2009-5384
[research_hjulianallen_1958]: https://ntrs.nasa.gov/citations/20150019982
[research_ho_2006]: https://doi.org/10.2514/6.2006-8070
[research_hoadley_1988]: https://doi.org/10.2514/6.1988-2205
[research_hoang_nguyen_2024]: https://doi.org/10.1088/1361-6439/ad6f1b
[research_hoch_momin_1968]: https://doi.org/10.21236/ad0680052
[research_hoch_vernardakis_1975]: https://doi.org/10.1016/0036-9748(75)90392-0
[research_hodge_1976]: https://doi.org/10.21236/ada029544
[research_hoeger_king_2010]: https://doi.org/10.2514/6.2010-6556
[research_hoeger_king_2011]: https://doi.org/10.2514/6.2011-2221
[research_hoegl_duesterhaus_1988]: https://doi.org/10.2514/6.1988-3045
[research_hoffert_1968]: https://doi.org/10.2514/6.1968-718
[research_hoffmann_2000]: https://doi.org/10.21236/ada422319
[research_hohn_guelhan_2012]: https://doi.org/10.2514/6.2012-5975
[research_hohn_guelhan_2015]: https://doi.org/10.2514/6.2015-3679
[research_hohn_gulhan_2011]: https://doi.org/10.2514/6.2011-2350
[research_hohn_gulhan_2017]: https://doi.org/10.2514/1.b36054
[research_hohn_gulhan_2022]: https://doi.org/10.2514/1.b38315
[research_hojnacki_1972]: https://doi.org/10.21236/ad0754852
[research_holberg_grabowsky_1981]: https://doi.org/10.2514/6.1981-2492
[research_holden_1970]: https://doi.org/10.21236/ad0706135
[research_holden_1972]: https://doi.org/10.2514/6.1972-74
[research_holden_1977]: https://doi.org/10.2514/6.1977-45
[research_holden_1993]: https://doi.org/10.1007/978-94-011-1828-6_6
[research_holden_2000]: https://doi.org/10.2514/6.2000-930
[research_holden_2011]: https://doi.org/10.1017/cbo9780511842757.006
[research_holden_smolinski_2008]: https://doi.org/10.2514/6.2008-642
[research_holden_wadhams_2001]: https://doi.org/10.21236/ada400749
[research_holden_wadhams_2010]: https://doi.org/10.2514/6.2010-4468
[research_holdo_dewith_2004]: https://doi.org/10.1115/ht-fed2004-56866
[research_holifield_tufts_2024]: https://doi.org/10.2514/6.2024-0672
[research_holifield_tufts_2024_b]: https://doi.org/10.2514/6.2024-0672.c1
[research_holland_perkins_1991]: https://doi.org/10.2514/6.1991-1708
[research_holland_perkins_1992]: https://doi.org/10.2514/6.1992-3099
[research_hollanders_laval_1992]: https://doi.org/10.2514/6.1992-5027
[research_hollandscottd_1994]: https://ntrs.nasa.gov/citations/19950009483
[research_hollandscottdouglas_1991]: https://ntrs.nasa.gov/citations/19910021769
[research_holmhansen_lee_2010]: https://doi.org/10.2514/6.2010-7868
[research_holography_of_1974]: https://doi.org/10.2514/5.9781600865077.0297.0313
[research_hommel_1989]: https://doi.org/10.2514/6.1989-1976
[research_hong_kim_2011]: https://doi.org/10.2514/6.2011-3967
[research_hong_lee_2005]: https://doi.org/10.1017/s172771910000054x
[research_hong_xiong_2014]: https://doi.org/10.1109/chicc.2014.6896100
[research_hongbo_yongyuan_2016]: https://doi.org/10.1504/ijscom.2016.076405
[research_hongqianlu_dongmingge_2011]: https://doi.org/10.1109/icacc.2011.6016487
[research_hooper]: https://doi.org/10.14264/340222
[research_hopkins]: https://doi.org/10.14264/29f29b3
[research_horisawa_2004]: https://doi.org/10.1063/1.1721022
[research_horisawa_tsuchiya_2004]: https://doi.org/10.1117/12.548344
[research_hornbeck_1975]: https://doi.org/10.21236/ada023471
[research_hornung_1991]: https://doi.org/10.1007/978-3-642-84580-2_12
[research_hornung_2001]: https://doi.org/10.2514/6.2001-2776
[research_hornung_ponchaut_2003]: https://doi.org/10.21236/ada422106
[research_horstman_1987]: https://doi.org/10.2514/6.1987-1367
[research_horstman_1991]: https://doi.org/10.2514/6.1991-1760
[research_hossain_2025]: https://doi.org/10.31224/5900
[research_hossainjoy_rahman_2017]: https://doi.org/10.1115/1.4038214
[research_hostetler_2005]: https://doi.org/10.4271/2005-01-3379
[research_hoter_nastac_2026]: https://doi.org/10.2514/6.2026-5115
[research_hou_chang_2020]: https://doi.org/10.1016/j.ast.2020.106129
[research_hou_he_2024]: https://doi.org/10.2139/ssrn.5049615
[research_hou_liu_2023]: https://doi.org/10.3390/aerospace10121008
[research_hou_wang_2015]: https://doi.org/10.1109/jas.2015.7081658
[research_hoult_starkey_2003]: https://doi.org/10.2514/6.2003-6964
[research_houria_albustanji_2026]: https://doi.org/10.1016/j.icheatmasstransfer.2026.112130
[research_howe_howe_2022]: https://doi.org/10.1016/j.actaastro.2022.03.020
[research_howell_1988]: https://doi.org/10.2514/6.1988-2185
[research_howland_1953]: https://doi.org/10.4271/530162
[research_hoyingd_kelblec_1990]: https://ntrs.nasa.gov/citations/19910000748
[research_hromas_lees_1962]: https://doi.org/10.21236/ad0400700
[research_hsia_gross_1989]: https://doi.org/10.2514/6.1989-2681
[research_hsieh_yang_1997]: https://doi.org/10.2514/6.1997-396
[research_hsu_carter_2007]: https://doi.org/10.2514/6.2007-5394
[research_hsu_carter_2010]: https://doi.org/10.2514/1.45767
[research_hu_bao_2014]: https://doi.org/10.2514/1.b35239
[research_hu_bodson_2008]: https://doi.org/10.2514/6.2008-6375
[research_hu_chang_2013]: https://doi.org/10.1155/2013/254376
[research_hu_chang_2014]: https://doi.org/10.1016/j.actaastro.2014.07.012
[research_hu_chang_2015]: https://doi.org/10.1061/(asce)as.1943-5525.0000389
[research_hu_chen_2021]: https://doi.org/10.1007/s12555-019-0474-x
[research_hu_dong_2022]: https://doi.org/10.1109/indin51773.2022.9976071
[research_hu_guo_2022]: https://doi.org/10.1002/asjc.2822
[research_hu_jiang_2018]: https://doi.org/10.2514/1.j055860
[research_hu_li_2018]: https://doi.org/10.1016/j.neucom.2018.01.031
[research_hu_li_2026]: https://doi.org/10.1016/j.ijheatmasstransfer.2026.129036
[research_hu_liu_2013]: https://doi.org/10.1109/ccdc.2013.6560962
[research_hu_liu_2025]: https://doi.org/10.1016/j.ast.2024.109856
[research_hu_sun_2010]: https://doi.org/10.1504/ijmic.2010.035283
[research_hu_wang_2022]: https://doi.org/10.1109/ccdc55256.2022.10033433
[research_hu_wei_2018]: https://doi.org/10.1016/j.actaastro.2018.05.021
[research_hu_xia_2013]: https://doi.org/10.2322/tjsass.56.337
[research_hu_yang_2022]: https://doi.org/10.3390/s22041523
[research_hu_zhu_2017]: https://doi.org/10.1109/smc.2017.8122853
[research_huang_chen_2021]: https://doi.org/10.1016/j.csite.2021.100893
[research_huang_feng_2025]: https://doi.org/10.1016/j.applthermaleng.2025.125795
[research_huang_kieffer_2005]: https://doi.org/10.1103/physrevlett.95.215901
[research_huang_li_2025]: https://doi.org/10.1016/j.ast.2025.110283
[research_huang_li_2025_b]: https://doi.org/10.2514/1.a36290
[research_huang_lianjie_2017]: https://doi.org/10.2514/6.2017-2436
[research_huang_liu_2022]: https://doi.org/10.1016/j.fpc.2022.03.001
[research_huang_lv_2025]: https://doi.org/10.1016/j.energy.2025.135239
[research_huang_murray_2003]: https://doi.org/10.21236/ada592255
[research_huang_pourkashanian_2010]: https://doi.org/10.1007/s12650-010-0064-8
[research_huang_spadaccini_2001]: https://doi.org/10.1115/2001-gt-0073
[research_huang_spadaccini_2002]: https://doi.org/10.2514/6.2002-3871
[research_huang_spadaccini_2002_b]: https://doi.org/10.1115/gt2002-30070
[research_huang_spadaccini_2004]: https://doi.org/10.1021/ie0401760
[research_huang_spadaccini_2004_b]: https://doi.org/10.1115/1.1689361
[research_huang_tang_2012]: https://doi.org/10.1115/gt2012-68012
[research_huang_wang_2011]: https://doi.org/10.1016/j.actaastro.2010.12.011
[research_huang_wang_2025]: https://doi.org/10.2139/ssrn.5203126
[research_huang_wang_2025_b]: https://doi.org/10.1063/5.0282133
[research_huang_wang_2026]: https://doi.org/10.1016/j.ast.2026.112309
[research_huang_xing_2005]: https://doi.org/10.2514/6.2005-4285
[research_huang_yan_2016]: https://doi.org/10.1016/j.ijhydene.2016.01.062
[research_huang_yang_2018]: https://doi.org/10.1109/ccdc.2018.8407432
[research_huang_yao_2024]: https://doi.org/10.1063/5.0182681
[research_huang_yue_2020]: https://doi.org/10.1016/j.cja.2020.04.019
[research_huang_zhang_2017]: https://doi.org/10.1109/ccdc.2017.7978679
[research_huang_zhang_2018]: https://doi.org/10.1088/1742-6596/1060/1/012088
[research_huang_zhang_2021]: https://doi.org/10.2514/1.j060051
[research_huang_zhang_2026]: https://doi.org/10.2139/ssrn.6136990
[research_huang_zhou_2011]: https://doi.org/10.2514/6.2011-5828
[research_huang_zuo_2018]: https://doi.org/10.1016/j.ast.2018.01.012
[research_hube_1968]: https://doi.org/10.21236/ad0388036
[research_huber_1966]: https://doi.org/10.2514/6.1966-750
[research_hucknall_1985]: https://doi.org/10.1007/978-94-009-4852-5_2
[research_hucknall_1985_b]: https://doi.org/10.1007/978-94-009-4852-5_3
[research_huebner_tatum_1991]: https://doi.org/10.2514/6.1991-1709
[research_huebner_witte_2003]: https://doi.org/10.2514/6.2003-7001
[research_hueter_1999]: https://doi.org/10.2514/6.1999-4925
[research_huffman_davidson_1958]: https://doi.org/10.21236/ad0204817
[research_hughes_2000]: https://doi.org/10.21236/ada482531
[research_hughes_pizzo_2003]: https://doi.org/10.21236/ada416791
[research_hughes_wu_2010]: https://doi.org/10.2514/6.2010-8281
[research_hughes_wu_2012]: https://doi.org/10.1007/978-1-4614-1833-7_16
[research_hugo_lago_2022]: https://doi.org/10.5772/intechopen.100328
[research_hui_hu_2006]: https://doi.org/10.1080/10618560600578476
[research_huilong_qiang_2015]: https://doi.org/10.1115/ajkfluids2015-09770
[research_huisheng_beijing_2021]: https://doi.org/10.1115/1.4053068
[research_human_2002]: https://doi.org/10.2514/6.2002-2136
[research_hummell_beck_1966]: https://doi.org/10.21236/ad0637953
[research_humphrey_culick_1987]: https://doi.org/10.2514/6.1987-1872
[research_hung_1982]: https://doi.org/10.2514/6.1982-25
[research_hung_buning_1984]: https://doi.org/10.2514/6.1984-457
[research_hung_maccormack_1978]: https://doi.org/10.2514/6.1978-161
[research_hunt]: https://doi.org/10.14264/uql.2014.194
[research_hunt_1989]: https://doi.org/10.1007/978-1-4684-9187-6_5
[research_hunt_eiswirth_1996]: https://doi.org/10.2514/6.1996-4591
[research_hunt_ground_2019]: https://doi.org/10.2514/6.2019-4016
[research_hunt_hunt_2020]: https://doi.org/10.2514/6.2020-3715
[research_hunt_hunt_2021]: https://doi.org/10.2514/1.b38334
[research_hunt_lawing_1978]: https://doi.org/10.2514/6.1978-6
[research_hunt_lawing_1979]: https://doi.org/10.2514/3.58587
[research_hunt_lockwood_1997]: https://doi.org/10.1063/1.51938
[research_hunt_nixon_1995]: https://doi.org/10.2514/6.1995-2212
[research_hunt_rausch_1998]: https://doi.org/10.2514/6.1998-1641
[research_hunter_1981]: https://doi.org/10.1115/1.3244511
[research_huntjl_lawingpl_1978]: https://ntrs.nasa.gov/citations/19780024225
[research_huo_mirmirani_2006]: https://doi.org/10.2514/6.2006-6695
[research_hutcheson_1976]: https://doi.org/10.21236/ada033302
[research_hutchins_akella_2012]: https://doi.org/10.2514/6.2012-2808
[research_hutchins_akella_2014]: https://doi.org/10.2514/1.b35230
[research_hutt_1987]: https://doi.org/10.1177/014233128700900404
[research_hutt_east_1983]: https://doi.org/10.2514/6.1983-215
[research_huttjohnj_mcarthurcraig_2001]: https://ntrs.nasa.gov/citations/20020022506
[research_hutzel_decker_2011]: https://doi.org/10.2514/6.2011-2223
[research_hutzel_decker_2011_b]: https://doi.org/10.2514/6.2011-402
[research_hwang_2024]: https://doi.org/10.6028/nist.tn.2275-upd1
[research_hwang_yeo_2023]: https://doi.org/10.6028/nist.tn.2275
[research_hyers_2009]: https://doi.org/10.21236/ada524249
[research_hypersonic_aerodynamics_1988]: https://doi.org/10.2514/5.9781600862342.0051.0080
[research_hypersonic_aerodynamics_2016]: https://doi.org/10.1016/b978-0-12-804425-4.00023-4
[research_hypersonic_aerodynamics_2019]: https://doi.org/10.2514/5.9781624105142.0837.0846
[research_hypersonic_aerodynamics_2025]: https://doi.org/10.1002/9781394285662.ch2
[research_hypersonic_air_breathing_2022]: https://doi.org/10.1002/9781119640646.ch13
[research_hypersonic_and_2023]: https://doi.org/10.5772/intechopen.104045
[research_hypersonic_flight_2025]: https://doi.org/10.1002/9781394309290.ch9
[research_hypersonic_flow_1989]: https://doi.org/10.2514/6.1989-1876
[research_hypersonic_flow_2009]: https://doi.org/10.1201/9781439804667.ch8
[research_hypersonic_flows_2021]: https://doi.org/10.1017/9781009105842.013
[research_hypersonic_flows_2025]: https://doi.org/10.1017/9781009501293.013
[research_hypersonic_ground_2002]: https://doi.org/10.2514/5.9781600866678.0001.0015
[research_hypersonic_inviscid_2006]: https://doi.org/10.2514/5.9781600861956.0103.0178
[research_hypersonic_inviscid_2006_b]: https://doi.org/10.2514/5.9781600861956.0179.0260
[research_hypersonic_inviscid_2019]: https://doi.org/10.2514/5.9781624105142.0107.0182
[research_hypersonic_inviscid_2019_b]: https://doi.org/10.2514/5.9781624105142.0183.0266
[research_hypersonic_materials_2023]: https://doi.org/10.12968/s1478-2774(24)50016-3
[research_hypersonic_nonequilibrium_2015]: https://doi.org/10.2514/4.103292
[research_hypersonic_plane_2011]: https://doi.org/10.1063/pt.5.025508
[research_hypersonic_shock_2006]: https://doi.org/10.2514/5.9781600861956.0035.0050
[research_hypersonic_shock_2019]: https://doi.org/10.2514/5.9781624105142.0039.0054
[research_hypersonic_thin_2018]: https://doi.org/10.1201/9780203737972-3
[research_hypersonic_viscous_2006]: https://doi.org/10.2514/5.9781600861956.0375.0414
[research_hypersonic_viscous_2019]: https://doi.org/10.2514/5.9781624105142.0389.0428
[research_hypersonic_wind_1949]: https://doi.org/10.2307/3926640
[research_hyperx_ground_test]: https://ntrs.nasa.gov/citations/20010047675
[research_hyunwoo_kang_2023]: https://doi.org/10.2514/6.2023-3039
[research_iannelli_2007]: https://doi.org/10.2514/6.2007-522
[research_iannelli_2007_b]: https://doi.org/10.2514/6.2007-5071
[research_iannelli_2008]: https://doi.org/10.2514/6.2008-65
[research_ibrahim_1967]: https://doi.org/10.21236/ad0658345
[research_icao_standard_2021]: https://doi.org/10.1017/9781108691055.016
[research_ide_armstrong_1989]: https://doi.org/10.2514/6.1989-2182
[research_idris_saad_2014]: https://doi.org/10.3390/s140406606
[research_idris_saad_2015]: https://doi.org/10.1007/978-3-319-16838-8_30
[research_ifflnder_keller]: https://doi.org/10.1002/9780470294437.ch70
[research_igari_2019]: https://doi.org/10.1299/jsmemecj.2019.f04204
[research_ignatowicz_dabrowski_2025]: https://doi.org/10.12913/22998624/207553
[research_igra_2026]: https://doi.org/10.2514/6.2026-4172
[research_iida_komai_1992]: https://doi.org/10.2514/6.1992-3728
[research_ikawa_1989]: https://doi.org/10.2514/6.1989-2682
[research_ikawa_1991]: https://doi.org/10.2514/3.23345
[research_ikenson_2025]: https://doi.org/10.1063/10.0039841
[research_ilie_chan_2023]: https://doi.org/10.2514/6.2023-1648
[research_ilie_mcafee_2023]: https://doi.org/10.2514/6.2023-4136
[research_ilie_sullivan_2021]: https://doi.org/10.2514/6.2021-1572
[research_iliff_shafer_1992]: https://doi.org/10.2514/6.1992-3988
[research_iliffkennethw_shafermaryf_1993]: https://ntrs.nasa.gov/citations/19930039009
[research_iliffkennethw_shafermaryf_1993_b]: https://ntrs.nasa.gov/citations/19940006365
[research_iliffkennethw_shafermaryf_1995]: https://ntrs.nasa.gov/citations/19960003513
[research_ilin_diaz_1999]: https://doi.org/10.13182/fst99-a11963878
[research_im_do_2018]: https://doi.org/10.1016/j.paerosci.2017.12.001
[research_imado_kuroda_1992]: https://doi.org/10.2514/6.1992-4531
[research_impact_of]: https://doi.org/10.4271/air6443a
[research_imrak_karaselvi_2021]: https://doi.org/10.2514/6.2021-2469
[research_inamura_sei_1996]: https://doi.org/10.2514/6.1996-2665
[research_ince_1967]: https://doi.org/10.1016/b978-1-4831-9836-1.50014-9
[research_incorporating_agility_1994]: https://doi.org/10.2514/6.1994-2135
[research_influence_of_2023]: https://doi.org/10.1063/5.0150253
[research_influence_of_2024]: https://doi.org/10.47176/jafm.17.8.2512
[research_ingenito_2015]: https://doi.org/10.1016/j.ijhydene.2014.12.014
[research_ingenito_2021]: https://doi.org/10.1007/978-3-030-66881-5_4
[research_ingenito_2021_b]: https://doi.org/10.1007/978-3-030-66881-5_3
[research_ingenito_2021_c]: https://doi.org/10.1007/978-3-030-66881-5_2
[research_ingenito_2021_d]: https://doi.org/10.1007/978-3-030-66881-5_11
[research_ingenito_2021_e]: https://doi.org/10.1007/978-3-030-66881-5
[research_ingenito_2021_f]: https://doi.org/10.1007/978-3-030-66881-5_6
[research_ingenito_bruno_2009]: https://doi.org/10.2514/6.2009-5186
[research_ingenito_bruno_2009_b]: https://doi.org/10.2514/6.2009-7419
[research_inger_1984]: https://doi.org/10.2514/6.1984-1555
[research_inger_1986]: https://doi.org/10.1007/978-3-642-82770-9_24
[research_inger_1989]: https://doi.org/10.2514/6.1989-2181
[research_inger_1991]: https://doi.org/10.2514/6.1991-3324
[research_inger_1994]: https://doi.org/10.2514/6.1994-2351
[research_inger_1995]: https://doi.org/10.2514/6.1995-1804
[research_inger_1995_b]: https://doi.org/10.2514/3.713
[research_inger_1995_c]: https://doi.org/10.1016/0094-5765(95)00101-5
[research_inger_1995_d]: https://doi.org/10.2514/6.1995-229
[research_inger_2008]: https://doi.org/10.2514/6.2008-2669
[research_inger_2011]: https://doi.org/10.1017/cbo9780511842757.010
[research_inger_higgins_2001]: https://doi.org/10.2514/6.2001-812
[research_inger_rangwalla_1988]: https://doi.org/10.2514/6.1988-603
[research_initial_results_1962]: https://doi.org/10.2514/5.9781600864810.0599.0624
[research_initial_shuttle_1983]: https://doi.org/10.2514/5.9781600865626.0325.0348
[research_inlet_mode_transition]: https://ntrs.nasa.gov/citations/20130003353
[research_inlet_unstart_model]: https://ntrs.nasa.gov/citations/19950009484
[research_inokuma_yakeno_2025]: https://doi.org/10.1615/thmt-25.690
[research_instrumentation_for_1974]: https://doi.org/10.2514/4.865077
[research_instrumentation_for_1974_b]: https://doi.org/10.2514/5.9781600865077.0041.0058
[research_integrated_transient_1981]: https://doi.org/10.2514/6.1981-480
[research_international_standard_2010]: https://doi.org/10.1017/cbo9780511844652.021
[research_intranasal_flow_2015]: https://doi.org/10.1055/b-0035-104255
[research_introduction_special_2014]: https://doi.org/10.2514/1.b35394
[research_introduction_to_2022]: https://doi.org/10.1002/9781119640646.ch1
[research_investigation_of_1974]: https://doi.org/10.2514/5.9781600865077.0095.0106
[research_investigation_of_2005]: https://doi.org/10.1016/s0140-6701(05)82918-2
[research_investigation_of_2023]: https://doi.org/10.1063/5.0148331
[research_isaac_miles_1990]: https://doi.org/10.2514/6.1990-3066
[research_isakina_prokhvatilov_2000]: https://doi.org/10.1063/1.593926
[research_isbell]: https://doi.org/10.1007/3-540-27168-6_9
[research_ishimoto_takizawa_1996]: https://doi.org/10.2514/6.1996-3403
[research_ispir_saracoglu_2019]: https://doi.org/10.2514/6.2019-3842
[research_ispir_zdybal_2023]: https://doi.org/10.1016/j.actaastro.2022.11.013
[research_itabashi_honma_1995]: https://doi.org/10.1007/978-3-642-79532-9_30
[research_itoh_2007]: https://doi.org/10.2514/6.2007-1041
[research_itoh_ueda_2002]: https://doi.org/10.1007/s00193-002-0147-0
[research_iwashita_2015]: https://doi.org/10.1016/j.carbon.2015.07.018
[research_iwashita_2026]: https://doi.org/10.1016/j.carbon.2026.121740
[research_izard_lehnasch_2009]: https://doi.org/10.1080/00102200903181892
[research_jackson_anderson_1967]: https://doi.org/10.1007/978-1-4757-0489-1_15
[research_jackson_corporan_1995]: https://doi.org/10.2514/6.1995-6028
[research_jackson_coyle_1983]: https://doi.org/10.2514/6.1983-2724
[research_jackson_gruber_2015]: https://doi.org/10.2514/1.b35350
[research_jacocks_kneile_1975]: https://doi.org/10.21236/ada004104
[research_jade_jimmyjohnoe_2025]: https://doi.org/10.2139/ssrn.5933059
[research_jaeger_hemati_2025]: https://doi.org/10.2514/6.2025-97945
[research_jagadeesh_reddy_1998]: https://doi.org/10.2514/6.1998-2601
[research_james_2022]: https://doi.org/10.64628/aa.36gmcnkfy
[research_jamie_2015]: https://doi.org/10.3366/edinburgh/9780748696000.003.0002
[research_jammalamadaka_li_2014]: https://doi.org/10.1063/1.4873495
[research_janardanan_jayakumar_2006]: https://doi.org/10.2514/6.2006-8076
[research_janarthanam_babu_2012]: https://doi.org/10.1017/s0001924000007302
[research_jann_yakimenko_2015]: https://doi.org/10.2514/5.9781624101960.0685.0740
[research_jardine_1930]: https://doi.org/10.4271/300010
[research_jasa_mader_2018]: https://doi.org/10.2514/6.2018-3884
[research_jaskowiakmarthah_2004]: https://ntrs.nasa.gov/citations/20050192189
[research_jategaonkar_behr_2005]: https://doi.org/10.2514/6.2005-6129
[research_javadi_aidun_2024]: https://doi.org/10.1115/fedsm2024-131920
[research_javaid_serghides_2003]: https://doi.org/10.2514/6.2003-6953
[research_javaid_serghides_2004]: https://doi.org/10.2514/6.2004-1201
[research_javaid_serghides_2005]: https://doi.org/10.2514/1.8782
[research_jayachandran_menon_1996]: https://doi.org/10.1006/jssc.1996.0177
[research_jayanthi_jain_2019]: https://doi.org/10.12783/ballistics2019/33142
[research_jaydfeldman]: https://ntrs.nasa.gov/citations/20210022886
[research_jazra_preller_2013]: https://doi.org/10.2514/1.a32381
[research_jazra_smart_2011]: https://doi.org/10.2514/6.2011-2377
[research_jee]: https://doi.org/10.22215/etd/2018-13341
[research_jeffrie_rolston_1972]: https://doi.org/10.2514/6.1972-761
[research_jensen_braendlein_1996]: https://doi.org/10.2514/6.1996-3037
[research_jeon_park_2023]: https://doi.org/10.6108/kspe.2023.27.6.009
[research_jeong_obyrne_2008]: https://doi.org/10.2514/6.2008-4576
[research_jeong_obyrne_2008_b]: https://doi.org/10.2514/1.36519
[research_jeong_obyrne_2020]: https://doi.org/10.3390/en13010193
[research_jessicaluxbaumann_darrylaburkes_2005]: https://ntrs.nasa.gov/citations/20050237906
[research_jeyakumar_biswas_2005]: https://doi.org/10.1016/j.mcm.2005.02.001
[research_ji_2017]: https://doi.org/10.2514/6.2017-2184
[research_ji_cai_2025]: https://doi.org/10.1016/j.applthermaleng.2025.128683
[research_ji_he_2024]: https://doi.org/10.2139/ssrn.4811591
[research_ji_zhao_2023]: https://doi.org/10.23919/ccc58697.2023.10240358
[research_ji_zhou_2017]: https://doi.org/10.23919/chicc.2017.8028356
[research_ji_zhou_2018]: https://doi.org/10.1109/gncc42960.2018.9019124
[research_ji_zhou_2019]: https://doi.org/10.23919/chicc.2019.8865421
[research_jia_wenxiu_2004]: https://doi.org/10.1007/bf02437297
[research_jian_yude_2024]: https://doi.org/10.1016/j.ijhydene.2023.07.014
[research_jianbo_xinghua_2017]: https://doi.org/10.23919/chicc.2017.8028297
[research_jianchen_yuzhen_2014]: https://doi.org/10.2514/6.2014-3947
[research_jiang_chen_2018]: https://doi.org/10.1109/gncc42960.2018.9018655
[research_jiang_liu_2021]: https://doi.org/10.3390/aerospace8090238
[research_jiang_liu_2024]: https://doi.org/10.23919/ccc63176.2024.10661464
[research_jiang_nan_2022]: https://doi.org/10.3390/aerospace9080424
[research_jiang_song_2017]: https://doi.org/10.2514/6.2017-2262
[research_jiang_wang_2023]: https://doi.org/10.1080/10407782.2023.2174627
[research_jiang_zhan_2025]: https://doi.org/10.1016/j.energy.2025.138187
[research_jiang_zhang_2010]: https://doi.org/10.5539/mas.v4n6p30
[research_jiang_zhou_2020]: https://doi.org/10.1080/21642583.2020.1747567
[research_jianguo_yifei_2018]: https://doi.org/10.1109/ccdc.2018.8407770
[research_jianqiang_jinlong_2016]: https://doi.org/10.1063/1.4964090
[research_jiao_chang_2015]: https://doi.org/10.2514/1.j053913
[research_jiao_chang_2016]: https://doi.org/10.1016/j.ast.2016.09.008
[research_jiao_chang_2017]: https://doi.org/10.1016/j.actaastro.2016.10.027
[research_jiao_chang_2018]: https://doi.org/10.1016/j.actaastro.2017.12.005
[research_jiao_song_2021]: https://doi.org/10.1016/j.fuel.2021.120239
[research_jiewang_qunzong_2012]: https://doi.org/10.1109/ccdc.2012.6243034
[research_jin_choi_2023]: https://doi.org/10.2139/ssrn.4459211
[research_jin_choi_2024]: https://doi.org/10.1016/j.expthermflusci.2023.111050
[research_jin_huang_2016]: https://doi.org/10.1115/gt2016-56083
[research_jin_sun_2022]: https://doi.org/10.2514/1.j061685
[research_jin_tan_2023]: https://doi.org/10.1016/j.cja.2023.08.004
[research_jin_xu_2022]: https://doi.org/10.2514/1.j061326
[research_jin_yao_2023]: https://doi.org/10.2514/6.2023-4444
[research_jin_zhang_2023]: https://doi.org/10.1061/jaeeez.aseng-4615
[research_jin_zhang_2026]: https://doi.org/10.1088/1742-6596/3170/1/012036
[research_jinchuanhu_jinglinli_2015]: https://doi.org/10.1109/iccais.2015.7338676
[research_jing_shuo_2007]: https://doi.org/10.2514/6.2007-642
[research_jing_shuo_2008]: https://doi.org/10.2514/6.2008-142
[research_jing_song_2026]: https://doi.org/10.1016/j.applthermaleng.2026.130617
[research_jing_yuanpei_2015]: https://doi.org/10.2514/6.2015-3242
[research_jing_zhang_2023]: https://doi.org/10.2139/ssrn.4423861
[research_jing_zhang_2025]: https://doi.org/10.1016/j.applthermaleng.2024.125282
[research_jingang_haotian_2026]: https://doi.org/10.23919/jsee.2026.000076
[research_jingguang_shenmin_2017]: https://doi.org/10.23919/chicc.2017.8027411
[research_jingqi_yulong_2024]: https://doi.org/10.1016/j.energy.2024.132763
[research_jischke_1978]: https://doi.org/10.21236/ada068004
[research_jo_2026]: https://doi.org/10.2514/6.2026-115448
[research_jo_sung_2024]: https://doi.org/10.2514/6.2024-1249
[research_jo_sung_2025]: https://doi.org/10.2514/6.2025-2487
[research_jo_sung_2026]: https://doi.org/10.2514/6.2026-2738
[research_johnmichaelthornton_jeremiebernarderwinmeurisse]: https://ntrs.nasa.gov/citations/20210023171
[research_johnson_1967]: https://doi.org/10.2514/6.1967-297
[research_johnson_bogar_2001]: https://doi.org/10.2514/6.2001-1926
[research_johnson_jenquin_2022]: https://doi.org/10.2514/6.2022-3478
[research_johnson_josepha_1970]: https://doi.org/10.21236/ad0702806
[research_johnson_narayanaswamy_2024]: https://doi.org/10.2514/1.j064324
[research_johnson_narayanaswamy_2026]: https://doi.org/10.1063/5.0313906
[research_johnson_niedbalski_2015]: https://doi.org/10.1016/j.ijheatmasstransfer.2015.07.073
[research_johnson_niedbalski_2017]: https://doi.org/10.1016/j.applthermaleng.2017.04.126
[research_johnson_portalatin_1981]: https://doi.org/10.2514/6.1981-964
[research_johnson_sorenson_2006]: https://doi.org/10.2514/6.2006-8117
[research_johnsoniii_wu_1974]: https://doi.org/10.21236/ada017631
[research_johnsonsylvia_conleyjoe_2015]: https://ntrs.nasa.gov/citations/20160001278
[research_johnston_1969]: https://doi.org/10.1016/0029-5493(69)90031-4
[research_johnston_candler_2023]: https://doi.org/10.2514/6.2023-0084
[research_johnston_cubbage_1971]: https://doi.org/10.2514/3.59129
[research_johnston_monita_1970]: https://doi.org/10.21236/ad0869660
[research_johnston_powars_1969]: https://doi.org/10.1115/1.3571180
[research_jones_laurence_2025]: https://doi.org/10.2514/6.2025-99832
[research_jones_saxer_2021]: https://doi.org/10.2514/6.2021-1108
[research_jonesra_huberpw_1978]: https://ntrs.nasa.gov/citations/19790036073
[research_jordan_1974]: https://doi.org/10.2514/6.1974-941
[research_jordan_ragab_1996]: https://doi.org/10.1080/10618569608940790
[research_josyula_bailey_2003]: https://doi.org/10.2514/6.2003-3778
[research_josyula_shang_1990]: https://doi.org/10.2514/6.1990-1490
[research_josyula_shang_1992]: https://doi.org/10.2514/6.1992-2874
[research_josyula_vedula_2015]: https://doi.org/10.2514/5.9781624103292.0001.0044
[research_julurusandeep_avsskumaraswamigupta_2023]: https://doi.org/10.37934/arfmts.101.1.7389
[research_k_danish_2020]: https://doi.org/10.1016/j.actaastro.2020.05.039
[research_kadosh_natan_2020]: https://doi.org/10.1080/00102202.2020.1755276
[research_kai_ohtake_1996]: https://doi.org/10.2514/6.1996-4526
[research_kailasanath_gardner_1986]: https://doi.org/10.21236/ada170936
[research_kaili_kunyuan_2010]: https://doi.org/10.2514/6.2010-7034
[research_kaili_kunyuan_2011]: https://doi.org/10.2514/6.2011-2348
[research_kaiser_flueggelotz_1968]: https://doi.org/10.21236/ad0669578
[research_kakatsios_houzouris_1995]: https://doi.org/10.1007/s004190050013
[research_kakatsios_houzouris_1998]: https://doi.org/10.1016/s0196-8904(97)00022-8
[research_kalkhoran_otugen_1994]: https://doi.org/10.21236/ada299229
[research_kalra_shewale_2018]: https://doi.org/10.2514/6.2018-4935.c1
[research_kalra_shewale_2018_b]: https://doi.org/10.2514/6.2018-4935
[research_kaltreider_1951]: https://doi.org/10.1016/0002-9378(51)91159-3
[research_kalyan_konda_2022]: https://doi.org/10.1016/j.jfueco.2022.100075
[research_kamari_tadjfar_2020]: https://doi.org/10.1115/fedsm2020-20247
[research_kamath_mao_1991]: https://doi.org/10.2514/6.1991-1412
[research_kambrath_thuluvath_2025]: https://doi.org/10.22214/ijraset.2025.66708
[research_kamezawa_ruffin_2018]: https://doi.org/10.2514/6.2018-0244
[research_kanapathipillai_chang_2020]: https://doi.org/10.2514/6.2020-3723
[research_kanapathipillai_chang_2020_b]: https://doi.org/10.2514/6.2020-3723.c1
[research_kanapathipillai_yu_2024]: https://doi.org/10.1016/j.proci.2024.105414
[research_kanda_1998]: https://doi.org/10.2514/6.1998-3427
[research_kanda_1998_b]: https://doi.org/10.2514/6.1998-3123
[research_kanda_2000]: https://doi.org/10.2514/6.2000-3705
[research_kanda_chinzei_2001]: https://doi.org/10.2514/6.2001-1816
[research_kanda_hiraiwa_2003]: https://doi.org/10.2514/6.2003-11
[research_kanda_kato_2003]: https://doi.org/10.2514/6.2003-3420
[research_kanda_kato_2007]: https://doi.org/10.2514/1.29815
[research_kanda_masuya_1993]: https://doi.org/10.2514/6.1993-739
[research_kanda_masuya_1994]: https://doi.org/10.2514/3.23741
[research_kanderpalli_selvaraj_2014]: https://doi.org/10.2514/6.2014-2507
[research_kandula_kummitha_2025]: https://doi.org/10.1080/00102202.2025.2580323
[research_kaneko_menshov_2000]: https://doi.org/10.2514/6.2000-2600
[research_kaneko_nakamura_1999]: https://doi.org/10.2514/6.1999-3529
[research_kang_dunn_1972]: https://doi.org/10.2514/3.6621
[research_kang_meng_2023]: https://doi.org/10.3390/atmos14101577
[research_kang_sun_2011]: https://doi.org/10.2514/1.47701
[research_kang_sung_2025]: https://doi.org/10.2514/6.2025-2703
[research_kang_tang_2008]: https://doi.org/10.2514/6.2008-2595
[research_kang_wonkim_2019]: https://doi.org/10.32908/hthp.v48.701
[research_kang_zhao_2023]: https://doi.org/10.3390/atmos14121784
[research_kannaiyan_2020]: https://doi.org/10.1016/j.jocs.2020.101243
[research_kantrowitz_2002]: https://doi.org/10.1177/00030651020500021703
[research_kantrowitz_arthur_2025]: https://doi.org/10.1063/nbla.wqbs.njnn
[research_kantrowitz_arthur_2025_b]: https://doi.org/10.1063/nbla.ufnb.otsf
[research_kantrowitz_petschek_1964]: https://doi.org/10.21236/ad0603951
[research_kao_anderson_1981]: https://doi.org/10.2514/6.1981-2419
[research_karanian_kepler_1965]: https://doi.org/10.2514/6.1965-588
[research_karciauskas_peters_2024]: https://doi.org/10.2139/ssrn.4835625
[research_karimi_oboodi_2018]: https://doi.org/10.1007/s00231-018-2416-1
[research_kascak_1971]: https://doi.org/10.2514/6.1971-1527
[research_kato_im_2019]: https://doi.org/10.2514/6.2019-3222
[research_kato_kanda_2006]: https://doi.org/10.2514/1.17547
[research_kauffman_grandhi_1990]: https://doi.org/10.2514/6.1990-2471
[research_kauffman_grandhi_1991]: https://doi.org/10.2514/6.1991-472
[research_kaufman_1963]: https://doi.org/10.21236/ad0421859
[research_kaushik_2018]: https://doi.org/10.1007/978-981-13-1678-4_10
[research_kaushik_2018_b]: https://doi.org/10.1007/978-981-13-1678-4_1
[research_kaushik_2023]: https://doi.org/10.1201/9781003139447-8
[research_kay_peschke_1990]: https://doi.org/10.2514/6.1990-2337
[research_kayiraw_1989]: https://ntrs.nasa.gov/citations/19900018618
[research_kayiw_peschkewt_1992]: https://ntrs.nasa.gov/citations/19920045911
[research_kazmar_2005]: https://doi.org/10.2514/6.2005-3256
[research_keanini_yu_1989]: https://doi.org/10.2514/6.1989-624
[research_kellenberger_ciccarelli_2015]: https://doi.org/10.1016/j.proci.2014.08.002
[research_kellermann_habermann_2020]: https://doi.org/10.1016/j.applthermaleng.2020.114985
[research_kelly_1972]: https://doi.org/10.1016/0008-6223(72)90060-7
[research_kelly_1972_b]: https://doi.org/10.1016/0008-6223(72)90498-8
[research_kelly_1973]: https://doi.org/10.21236/ad0771157
[research_kelly_1988]: https://doi.org/10.2514/6.1988-2129
[research_kelso_1993]: https://doi.org/10.2514/6.1993-2688
[research_kendall_1974]: https://doi.org/10.2514/6.1974-133
[research_kennedy_1986]: https://doi.org/10.2514/6.1986-9739
[research_kennell_neely_2015]: https://doi.org/10.2514/6.2015-3690
[research_kenworthy_1967]: https://doi.org/10.2514/6.1967-223
[research_kepler_champagne_1989]: https://doi.org/10.2514/6.1989-10
[research_kerans_2002]: https://doi.org/10.21236/ada409403
[research_kerstan_muller_2014]: https://doi.org/10.1016/j.solidstatesciences.2014.10.010
[research_keshmiri_2008]: https://doi.org/10.2514/6.2008-2531
[research_keshmiri_colgren_2005]: https://doi.org/10.2514/6.2005-6257
[research_keshmiri_colgren_2006]: https://doi.org/10.2514/6.2006-8087
[research_keshmiri_colgren_2006_b]: https://doi.org/10.2514/6.2006-8157
[research_keshmiri_colgren_2006_c]: https://doi.org/10.2514/6.2006-8158
[research_keshmiri_colgren_2007]: https://doi.org/10.2514/6.2007-6626
[research_keshmiri_farokhi_2007]: https://doi.org/10.2514/6.2007-5373
[research_kessler_li_2015]: https://doi.org/10.21236/ada626568
[research_khairulhabibpulok_chakravarty_2021]: https://doi.org/10.1115/1.0004275v
[research_khambaswadkar_2024]: https://doi.org/10.58445/rars.2094
[research_khan_tahmid_2018]: https://doi.org/10.1063/1.5044323
[research_khmyrov_grigoriev_2025]: https://doi.org/10.1615/hightempmatproc.2025062107
[research_khobragade_kumar_2022]: https://doi.org/10.1007/s00193-022-01091-5
[research_khorrami_chang_1997]: https://doi.org/10.21236/ada325675
[research_khorunzhenko_roupassov_2002]: https://doi.org/10.2514/6.2002-3569
[research_khrapko_2018]: https://doi.org/10.18502/keg.v3i3.1647
[research_khurana_suzuki_2013]: https://doi.org/10.2514/6.2013-2513
[research_kidd_adamsjr_2000]: https://doi.org/10.2514/6.2000-2514
[research_kim_2000]: https://doi.org/10.1006/icar.2000.6481
[research_kim_2003]: https://doi.org/10.1063/1.1582105
[research_kim_2017]: https://doi.org/10.1007/s10765-017-2285-8
[research_kim_baek_2004]: https://doi.org/10.1016/j.ijheatmasstransfer.2003.07.004
[research_kim_han_2020]: https://doi.org/10.6112/kscfe.2020.25.4.065
[research_kim_jeon_2010]: https://doi.org/10.5139/jksas.2010.38.6.586
[research_kim_kim_2023]: https://doi.org/10.5139/jksas.2023.51.10.661
[research_kim_lee_2022]: https://doi.org/10.5139/jksas.2022.50.5.297
[research_kim_menon_1999]: https://doi.org/10.2514/6.1999-200
[research_kim_park_2026]: https://doi.org/10.6112/kscfe.2026.31.2.084
[research_kim_rasmussen_1982]: https://doi.org/10.2514/6.1982-1299
[research_kim_seo_2025]: https://doi.org/10.1016/j.ast.2025.109978
[research_kim_seo_2025_b]: https://doi.org/10.1016/j.ijheatmasstransfer.2025.126901
[research_kimmel_1993]: https://doi.org/10.21236/ada288483
[research_kimmel_adamczak_2011]: https://doi.org/10.21236/ada548272
[research_kimmel_hayes_2005]: https://doi.org/10.21236/ada457024
[research_kimmel_poggie_1997]: https://doi.org/10.21236/ada417303
[research_kimmelrogerl_prabhudinesh_2015]: https://ntrs.nasa.gov/citations/20160003109
[research_kimmerly]: https://doi.org/10.14264/345542
[research_king_1962]: https://doi.org/10.21236/ad0295154
[research_kinslow_busby_1973]: https://doi.org/10.21236/ad0756680
[research_kireeti_ravikiransastry_2022]: https://doi.org/10.1016/j.fuel.2022.124528
[research_kirkby_1964]: https://doi.org/10.1016/0010-2180(64)90103-8
[research_kirkpatrick]: https://doi.org/10.31274/etd-180810-3712
[research_kishida_2006]: https://doi.org/10.1063/1.2204542
[research_kishore_sunitha_1977]: https://doi.org/10.1002/prep.19770020504
[research_kitamura_roe_2007]: https://doi.org/10.2514/6.2007-4465
[research_kitamura_shima_2011]: https://doi.org/10.2514/6.2011-3056
[research_kitowski_1992]: https://doi.org/10.2514/6.1992-3332
[research_kittredge_streets_1961]: https://doi.org/10.21236/ad0262338
[research_kiyohashi_1998]: https://doi.org/10.4131/jshpreview.7.1475
[research_kkn_reddy_2016]: https://doi.org/10.2514/6.2016-4143
[research_klepper_sirbaugh_2017]: https://doi.org/10.1115/gt2017-63072
[research_kline_palacios_2014]: https://doi.org/10.2514/6.2014-3228
[research_kline_palacios_2014_b]: https://doi.org/10.2514/6.2014-3228.c1
[research_klinebergjohnm_1989]: https://ntrs.nasa.gov/citations/19890014094
[research_klingenberg_willems_2026]: https://doi.org/10.2514/6.2026-5043
[research_klock_cesnik_2015]: https://doi.org/10.2514/6.2015-2711
[research_klock_cesnik_2016]: https://doi.org/10.2514/6.2016-1322
[research_klothakis_nikolos_2024]: https://doi.org/10.3390/computation12070140
[research_klotz_1963]: https://doi.org/10.2514/6.1963-198
[research_kluwick_stross_1984]: https://doi.org/10.1007/bf01176249
[research_knauss_riedel_1999]: https://doi.org/10.2514/6.1999-4959
[research_knight_2002]: https://doi.org/10.2514/6.2002-433
[research_knight_2015]: https://doi.org/10.21236/ada627597
[research_knight_kianvashrad_2023]: https://doi.org/10.1088/978-0-7503-5002-0ch7
[research_knight_kildare_2026]: https://doi.org/10.2514/6.2026-2509
[research_knight_naiman_2009]: https://doi.org/10.21236/ada498212
[research_knight_yan_2000]: https://doi.org/10.21236/ada386842
[research_knight_zheltovodov_2011]: https://doi.org/10.1017/cbo9780511842757.004
[research_knighton_1992]: https://doi.org/10.2514/6.1992-4072
[research_knittel_lewis_2012]: https://doi.org/10.2514/6.2012-5809
[research_knott_1974]: https://doi.org/10.21236/ad0786467
[research_knott_1984]: https://doi.org/10.4271/841147
[research_ko_jackson_1992]: https://doi.org/10.2514/6.1992-2487
[research_kobayashi_adachi_2015]: https://doi.org/10.1007/978-3-319-16838-8_79
[research_kobayashi_adachi_2017]: https://doi.org/10.1007/978-3-319-46213-4_104
[research_kobayashi_hemmi_2018]: https://doi.org/10.1007/978-3-319-73180-3_10
[research_kobayashi_kanda_2007]: https://doi.org/10.2322/tjsass.49.246
[research_kobayashi_sato_2001]: https://doi.org/10.2514/6.2001-1912
[research_kobayashi_sawai_2008]: https://doi.org/10.2514/6.2008-2620
[research_kobayashi_tomioka_2003]: https://doi.org/10.2514/6.2003-4737
[research_kodama_kogiso_2017]: https://doi.org/10.23919/acc.2017.7963765
[research_kodera_sunami_2005]: https://doi.org/10.2514/6.2005-3355
[research_kodera_yang_2007]: https://doi.org/10.2514/6.2007-5407
[research_kodikara_2020]: https://doi.org/10.5194/egusphere-egu2020-13024
[research_kohl_1993]: https://doi.org/10.1007/978-94-011-1828-6_15
[research_kojima_taguchi_2012]: https://doi.org/10.2514/6.2012-5973
[research_kojima_taguchi_2015]: https://doi.org/10.2514/6.2015-3595
[research_kokan_olds_2004]: https://doi.org/10.2514/6.2004-3728
[research_kokkinakis_khujadze_2023]: https://doi.org/10.1063/5.0153863
[research_kominek_2017]: https://doi.org/10.31399/asm.cp.ht2017p0149
[research_kong_chang_2020]: https://doi.org/10.2514/1.j059302
[research_kong_chang_2021]: https://doi.org/10.1063/5.0039537
[research_kong_chen_2026]: https://doi.org/10.3390/atmos17090847
[research_kong_liang_2024]: https://doi.org/10.1109/icops58192.2024.10627738
[research_konovalikhin_kovalev_2018]: https://doi.org/10.1134/s0018151x18050140
[research_kontinos_1996]: https://doi.org/10.2514/6.1996-1808
[research_kontogiannis_taylor_2016]: https://doi.org/10.2514/6.2016-0915
[research_kopp_garbers_2014]: https://doi.org/10.2514/6.2014-2531
[research_kopp_hollmeier_1999]: https://doi.org/10.2514/6.1999-4813
[research_koppenwallner_1968]: https://doi.org/10.2514/6.1968-49
[research_korabelnikov_kuranov_2002]: https://doi.org/10.2514/6.2002-913
[research_korabelnikov_kuranov_2005]: https://doi.org/10.2514/6.2005-3368
[research_korte_1992]: https://doi.org/10.2514/6.1992-332
[research_korte_2000]: https://doi.org/10.2514/6.2000-677
[research_korte_hodge_1994]: https://doi.org/10.2514/6.1994-2544
[research_korte_kumar_1991]: https://doi.org/10.2514/6.1991-2273
[research_korte_mcrae_1989]: https://doi.org/10.2514/6.1989-1829
[research_koschel_1996]: https://doi.org/10.2514/6.1996-4579
[research_koschel_link_1998]: https://doi.org/10.2514/6.1998-1601
[research_koschel_rick_1991]: https://doi.org/10.2514/6.1991-5019
[research_kose_celik_2023]: https://doi.org/10.3390/app14010071
[research_kostoff_eberhart_2003]: https://doi.org/10.21236/ada418717
[research_kostykchris_rischtim_2013]: https://ntrs.nasa.gov/citations/20140008322
[research_kostyukov_1980]: https://doi.org/10.1007/bf00794931
[research_kotelnikov_kotelnikov_2020]: https://doi.org/10.1134/s0018151x2002011x
[research_kothari_livingston_2010]: https://doi.org/10.2514/6.2010-8905
[research_kothari_tarpley_1996]: https://doi.org/10.2514/6.1996-2552
[research_kourtides_pitts_1988]: https://doi.org/10.1177/073490418800600501
[research_kozlovskii_stankus_2014]: https://doi.org/10.1134/s0018151x1403016x
[research_kozlovskii_stankus_2015]: https://doi.org/10.1134/s0018151x1505020x
[research_kramer_buhler_1980]: https://doi.org/10.2514/3.57746
[research_kramer_williams_2018]: https://doi.org/10.2514/6.2018-3411
[research_krause_hartmann_1991]: https://doi.org/10.23919/acc.1991.4791945
[research_krawczyk_rajendran_1986]: https://doi.org/10.2514/6.1986-1596
[research_kremeyer_pakhomov_2008]: https://doi.org/10.1063/1.2931905
[research_krikorian_1960]: https://doi.org/10.2172/4137098
[research_krothapalli_alvi_2003]: https://doi.org/10.21236/ada414914
[research_krumenacker_pellicano_1992]: https://doi.org/10.2514/6.1992-4108
[research_kubo_tomioka_2014]: https://doi.org/10.2514/6.2014-3873
[research_kubota_berg_1977]: https://doi.org/10.21236/ada042141
[research_kubota_uchida_1999]: https://doi.org/10.1615/jpormedia.v2.i1.50
[research_kudryavtsev_mironov_2009]: https://doi.org/10.1007/978-3-540-92779-2_111
[research_kuipers_ioannou_2008]: https://doi.org/10.2514/6.2008-7142
[research_kuipers_ioannou_2009]: https://doi.org/10.1109/acc.2009.5160574
[research_kuipers_mirmirani_2007]: https://doi.org/10.2514/6.2007-6326
[research_kulkarni_phan_2003]: https://doi.org/10.2514/6.2003-5497
[research_kulkarni_shrekhar_2024]: https://doi.org/10.2514/6.2024-1591
[research_kumar]: https://doi.org/10.1007/3-540-51048-6_4
[research_kumar_1992]: https://doi.org/10.1007/978-3-642-77922-0_15
[research_kumar_2022]: https://doi.org/10.26706/jtfs.3.1.20211202
[research_kumar_anderson_1986]: https://doi.org/10.2514/6.1986-1426
[research_kumar_ghosh_2024]: https://doi.org/10.1017/aer.2024.109
[research_kumar_iyer_2022]: https://doi.org/10.2514/6.2022-3863
[research_kumar_mahulikar_2017]: https://doi.org/10.2514/1.a33688
[research_kumar_penchalaiah_2018]: https://doi.org/10.1016/j.ifacol.2018.05.020
[research_kumar_pranaykumar_2023]: https://doi.org/10.2514/6.2023-4138
[research_kumar_sarkar_2018]: https://doi.org/10.1177/0954410018795265
[research_kumarajay_drummondjphilip_2001]: https://ntrs.nasa.gov/citations/20020011010
[research_kumargugulothu_bhaskar_2020]: https://doi.org/10.5772/intechopen.92555
[research_kumarsulurloganathan_2023]: https://doi.org/10.5772/intechopen.107841
[research_kumm_bitondo_1953]: https://doi.org/10.21236/ad0025105
[research_kummitha_2022]: https://doi.org/10.1016/j.ijhydene.2022.06.263
[research_kummitha_2022_b]: https://doi.org/10.1016/j.ijhydene.2022.06.103
[research_kummitha_2024]: https://doi.org/10.1016/j.ijhydene.2024.06.133
[research_kummitha_kandula_2026]: https://doi.org/10.1080/00102202.2026.2720216
[research_kummitha_pandey_2020]: https://doi.org/10.1093/jcde/qwaa084
[research_kummitha_pandey_2021]: https://doi.org/10.1016/j.fuel.2021.121425
[research_kummitha_suneetha_2017]: https://doi.org/10.1016/j.ijhydene.2017.01.213
[research_kundu_2013]: https://doi.org/10.21236/ada582581
[research_kuntz_amatucci_1986]: https://doi.org/10.2514/6.1986-348
[research_kuntz_amatucci_1987]: https://doi.org/10.2514/3.9681
[research_kuo_1976]: https://doi.org/10.2514/6.1976-1531
[research_kuppuswamy_kiran_1981]: https://doi.org/10.2514/6.1981-2381
[research_kuranov_korabelnikov_2008]: https://doi.org/10.2514/6.2008-2524
[research_kuranov_korabelnikov_2008_b]: https://doi.org/10.2514/1.24684
[research_kuranov_korabelnikov_2012]: https://doi.org/10.2514/6.2012-5879
[research_kuranov_korabelnikov_2016]: https://doi.org/10.1134/s0018151x16030093
[research_kuranov_korabelnikov_2017]: https://doi.org/10.1134/s1063784217010157
[research_kurilova_li_2026]: https://doi.org/10.1109/aero66936.2026.11519972
[research_kurtz_aizengendler_2015]: https://doi.org/10.2514/6.2015-0110
[research_kurzke_halliwell_2018]: https://doi.org/10.1007/978-3-319-75979-1_14
[research_kurzke_halliwell_2025]: https://doi.org/10.1007/978-3-031-65026-0_20
[research_kussoymarvini_horstmancliffordc_1989]: https://ntrs.nasa.gov/citations/19890010729
[research_kussoymi_horstmankc_1993]: https://ntrs.nasa.gov/citations/19930040866
[research_kutschenreuter_paulh_1966]: https://doi.org/10.21236/ad0636981
[research_kuznetsov_1992]: https://doi.org/10.1016/b978-0-444-89732-9.50051-0
[research_kwak_kiris_2003]: https://doi.org/10.2514/6.2003-3440
[research_kwak_lee_2011]: https://doi.org/10.2514/6.2011-3362
[research_kwak_lee_2013]: https://doi.org/10.2514/6.2013-3025
[research_kwak_lee_2013_b]: https://doi.org/10.6112/kscfe.2013.18.4.082
[research_kwak_lee_2013_c]: https://doi.org/10.6112/kscfe.2013.18.2.078
[research_kydd_1959]: https://doi.org/10.1016/0010-2180(59)90017-3
[research_kydd_mullaney_1961]: https://doi.org/10.1016/0010-2180(61)90112-2
[research_l_r_2012]: https://doi.org/10.2514/6.2012-5937
[research_labbe_ryan_1999]: https://doi.org/10.1080/10618569908940880
[research_lacorre_barre_2022]: https://doi.org/10.2139/ssrn.4257937
[research_ladeinde_2019]: https://doi.org/10.2514/6.2019-4419
[research_ladeinde_2020]: https://doi.org/10.2514/6.2020-3711
[research_ladeinde_2020_b]: https://doi.org/10.2514/6.2020-0874
[research_laderman_1979]: https://doi.org/10.21236/ada070254
[research_laderman_demetriades_1977]: https://doi.org/10.21236/ada046365
[research_ladyzhenskij_1963]: https://doi.org/10.21236/ad0295787
[research_lago_chpoun_2012]: https://doi.org/10.1007/978-3-642-25119-1_8
[research_lahaye_heckman_1968]: https://doi.org/10.21236/ad0679181
[research_lambert]: https://doi.org/10.31274/rtd-180817-4276
[research_lambert_coughlin_1967]: https://doi.org/10.2172/4378701
[research_lamorte_friedmann_2011]: https://doi.org/10.2514/6.2011-2394
[research_lamorte_friedmann_2015]: https://doi.org/10.2514/1.b35122
[research_lamy_1983]: https://doi.org/10.2514/6.1983-2736
[research_landau_yeneriz_1965]: https://doi.org/10.2514/6.1965-446
[research_lander_1968]: https://doi.org/10.2514/6.1968-997
[research_lander_nixon_1971]: https://doi.org/10.2514/3.44255
[research_landesman_basinski_1963]: https://doi.org/10.21236/ad0420822
[research_landrum_tournes_2002]: https://doi.org/10.2514/6.2002-2135
[research_landsbaum_salinas_1979]: https://doi.org/10.2514/6.1979-1359
[research_landsberg_curran_2021]: https://doi.org/10.2514/6.2021-4163
[research_landsberg_curran_2022]: https://doi.org/10.1016/j.ast.2022.107622
[research_landsberg_vanyai_2020]: https://doi.org/10.2514/1.j059856
[research_landsberg_wheatley_2016]: https://doi.org/10.2514/1.j054815
[research_lanejr_kirlin_1978]: https://doi.org/10.2514/6.1978-478
[research_lang_1981]: https://doi.org/10.2514/6.1981-2416
[research_langhenry_parks_1991]: https://doi.org/10.2514/6.1991-2428
[research_langilljr_1965]: https://doi.org/10.2514/6.1965-205
[research_lanshin_dulepov_1996]: https://doi.org/10.2514/6.1996-4499
[research_large_may_1981]: https://doi.org/10.2514/6.1981-2395
[research_lasorsa_kotler_2025]: https://doi.org/10.2514/6.2025-1528
[research_lasseur]: https://doi.org/10.70675/a016a39fzcf98z4a02z8727z2de51c059ff9
[research_latvala_anderson_1959]: https://doi.org/10.21236/ad0208546
[research_lau_2007]: https://doi.org/10.2514/6.2007-310
[research_laurence_lieber_2015]: https://doi.org/10.1016/j.combustflame.2014.09.016
[research_law_1975]: https://doi.org/10.2514/6.1975-832
[research_law_1976]: https://doi.org/10.2514/3.61413
[research_law_2004]: https://doi.org/10.21236/ada429385
[research_lawrence_1991]: https://doi.org/10.2514/6.1991-1695
[research_lawrence_1992]: https://doi.org/10.2514/6.1992-5030
[research_lazur_sawyer_1999]: https://doi.org/10.2514/6.1999-4864
[research_le_goyne_2005]: https://doi.org/10.2514/6.2005-23
[research_le_goyne_2006]: https://doi.org/10.2514/6.2006-815
[research_le_goyne_2008]: https://doi.org/10.2514/1.32592
[research_le_greenshields_2012]: https://doi.org/10.1051/eucass/201203217
[research_le_liu_2023]: https://doi.org/10.3390/drones7020119
[research_lead_cooled_fast]: https://doi.org/10.1007/springerreference_186939
[research_leckie]: https://doi.org/10.14264/a2fc89c
[research_lederer_schwab_1991]: https://doi.org/10.2514/6.1991-5040
[research_ledu_pollak_1968]: https://doi.org/10.2514/6.1968-1145
[research_lee]: https://doi.org/10.31274/etd-180810-3950
[research_lee_1995]: https://doi.org/10.2514/6.1995-2416
[research_lee_2006]: https://doi.org/10.2514/1.14180
[research_lee_2006_b]: https://doi.org/10.2514/1.14185
[research_lee_2012]: https://doi.org/10.2514/1.b34220
[research_lee_aldredge_2015]: https://doi.org/10.1016/j.ast.2015.08.004
[research_lee_chung_2024]: https://doi.org/10.1063/5.0214766
[research_lee_glass_1982]: https://doi.org/10.21236/ada127785
[research_lee_gross_2021]: https://doi.org/10.2514/6.2021-2765
[research_lee_gross_2022]: https://doi.org/10.2514/6.2022-3988
[research_lee_jamest_1963]: https://doi.org/10.21236/ad0406459
[research_lee_jeung_2009]: https://doi.org/10.1007/978-3-540-85181-3_51
[research_lee_kang_2013]: https://doi.org/10.2514/1.b34827
[research_lee_kang_2019]: https://doi.org/10.1371/journal.pone.0224994
[research_lee_kawamura_2005]: https://doi.org/10.2514/6.2005-1108
[research_lee_kim_2000]: https://doi.org/10.2514/6.2000-90
[research_lee_kim_2015]: https://doi.org/10.2514/6.2015-3503
[research_lee_kim_2026]: https://doi.org/10.2514/6.2026-5088
[research_lee_kim_2026_b]: https://doi.org/10.2514/6.2026-5074
[research_lee_lee_2021]: https://doi.org/10.1007/s12206-021-0543-y
[research_lee_lee_2022]: https://doi.org/10.3390/aerospace9030162
[research_lee_liou_2018]: https://doi.org/10.2514/6.2018-3954
[research_lee_mitani_2003]: https://doi.org/10.2514/2.6087
[research_lee_ombrello_2024]: https://doi.org/10.1016/j.proci.2024.105268
[research_lee_rasmussen_1978]: https://doi.org/10.21236/ada068002
[research_lee_reiman_2007]: https://doi.org/10.2514/6.2007-6685
[research_lee_shin_2001]: https://doi.org/10.2514/6.2001-384
[research_lee_vandalsem_1981]: https://doi.org/10.2514/6.1981-1002
[research_lees_hromas_1961]: https://doi.org/10.21236/ad0600632
[research_lees_kubota_1972]: https://doi.org/10.21236/ad0755276
[research_lees_reeves_1964]: https://doi.org/10.2514/6.1964-4
[research_leger_poggie_2014]: https://doi.org/10.2514/6.2014-0951
[research_legge_1995]: https://doi.org/10.2514/6.1995-2140
[research_lehoczky_1977]: https://doi.org/10.21236/ada044573
[research_lehtinen_zeller_1972]: https://doi.org/10.1016/0005-1098(72)90027-1
[research_lei_kunyuan_2012]: https://doi.org/10.2514/6.2012-5959
[research_lei_zha_2022]: https://doi.org/10.2514/6.2022-2234
[research_lei_zha_2022_b]: https://doi.org/10.2514/6.2022-2234.c1
[research_lei_zhang_2023]: https://doi.org/10.1016/j.tsep.2023.102255
[research_leighton_1964]: https://doi.org/10.5594/j07201
[research_lempert_dorofeenko_2013]: https://doi.org/10.1134/s0010508213040102
[research_lempert_miles_1995]: https://doi.org/10.21236/ada297721
[research_lenard_long_1962]: https://doi.org/10.21236/ad0294819
[research_lenard_long_1964]: https://doi.org/10.2514/3.27640
[research_leng_wang_2024]: https://doi.org/10.1016/j.energy.2024.132076
[research_leonov_2022]: https://doi.org/10.30826/icpcd13a04
[research_leonov_houpt_2018]: https://doi.org/10.2514/1.b36811
[research_leonov_kochetov_2011]: https://doi.org/10.1109/tps.2010.2091512
[research_leonov_yarantsev_2007]: https://doi.org/10.2514/6.2007-3890
[research_leonov_yarantsev_2009]: https://doi.org/10.2514/1.38002
[research_leonov_yarantsev_2012]: https://doi.org/10.1051/eucass/201203557
[research_leontiev_nosatov_2000]: https://doi.org/10.1615/heattransres.v31.i6-8.20
[research_lepsch_naftel_1993]: https://doi.org/10.2514/3.26368
[research_lepschjr_naftel_1992]: https://doi.org/10.2514/6.1992-3500
[research_lestrade_anthoine_2017]: https://doi.org/10.2514/1.a33467
[research_levermore_brio_1994]: https://doi.org/10.21236/ada295493
[research_levikhin_musteikis_2025]: https://doi.org/10.52467/2949-401x-2025-3-3-443-457
[research_levin_2015]: https://doi.org/10.2514/5.9781624103292.0159.0202
[research_levin_ioannou_2008]: https://doi.org/10.2514/6.2008-7137
[research_levy_1976]: https://doi.org/10.21236/ada029747
[research_levy_1982]: https://doi.org/10.1016/0010-2180(82)90003-7
[research_levy_shamroth_1977]: https://doi.org/10.21236/ada040843
[research_lewerenz_1987]: https://doi.org/10.2514/6.1987-1732
[research_lewis_1991]: https://doi.org/10.2514/6.1991-3304
[research_lewis_2001]: https://doi.org/10.2514/2.5866
[research_lewis_2003]: https://doi.org/10.2514/6.2003-7020
[research_lewis_2003_b]: https://doi.org/10.2514/6.2003-4405
[research_lewis_2010]: https://doi.org/10.1002/9780470686652.eae585
[research_leyland_1992]: https://doi.org/10.1007/978-3-642-77922-0_39
[research_li_1974]: https://doi.org/10.2514/6.1974-173
[research_li_1977]: https://doi.org/10.2514/6.1977-168
[research_li_2007]: https://doi.org/10.1063/1.2821982
[research_li_2008]: https://doi.org/10.21236/ada482157
[research_li_2019]: https://doi.org/10.1007/s42405-019-00220-2
[research_li_2021]: https://doi.org/10.23919/ccc52363.2021.9549545
[research_li_2022]: https://doi.org/10.1016/j.actaastro.2021.10.019
[research_li_2022_b]: https://doi.org/10.1063/5.0074757
[research_li_an_2014]: https://doi.org/10.2514/6.2014-3229
[research_li_chang_2018]: https://doi.org/10.1063/1.5053451
[research_li_chang_2019]: https://doi.org/10.1016/j.expthermflusci.2019.01.033
[research_li_chen_2011]: https://doi.org/10.4028/www.scientific.net/amm.110-116.5118
[research_li_chen_2017]: https://doi.org/10.23919/chicc.2017.8029006
[research_li_chen_2017_b]: https://doi.org/10.1016/j.expthermflusci.2017.04.011
[research_li_chen_2020]: https://doi.org/10.12783/dtetr/amee2019/33499
[research_li_chen_2022]: https://doi.org/10.2514/1.j061392
[research_li_cui_2009]: https://doi.org/10.1109/icma.2009.5246695
[research_li_cui_2009_b]: https://doi.org/10.1108/00022660910926854
[research_li_cui_2020]: https://doi.org/10.1007/s11433-019-1487-7
[research_li_ding_2023]: https://doi.org/10.1016/j.ast.2023.108667
[research_li_ding_2026]: https://doi.org/10.1016/j.applthermaleng.2026.130058
[research_li_dou_2025]: https://doi.org/10.2139/ssrn.5851127
[research_li_dou_2026]: https://doi.org/10.1016/j.ast.2026.111893
[research_li_eggers_2012]: https://doi.org/10.2514/6.2012-5820
[research_li_freed_1999]: https://doi.org/10.1097/00002480-199903000-00118
[research_li_fu_2010]: https://doi.org/10.1109/car.2010.5456775
[research_li_geiselhart_2024]: https://doi.org/10.2514/1.c037310
[research_li_guo_2021]: https://doi.org/10.1016/j.fuel.2020.119477
[research_li_han_2015]: https://doi.org/10.2514/6.2015-3592
[research_li_han_2025]: https://doi.org/10.2139/ssrn.5290673
[research_li_hang_2021]: https://doi.org/10.3390/app12010279
[research_li_hu_2018]: https://doi.org/10.1016/j.ast.2018.01.033
[research_li_huang_2011]: https://doi.org/10.2514/6.2011-2308
[research_li_huang_2024]: https://doi.org/10.21203/rs.3.rs-4475483/v1
[research_li_jiang_2021]: https://doi.org/10.21203/rs.3.rs-119435/v2
[research_li_jiang_2021_b]: https://doi.org/10.1109/iaecst54258.2021.9695560
[research_li_jiao_2018]: https://doi.org/10.1080/00102202.2018.1472086
[research_li_jiao_2026]: https://doi.org/10.1016/j.ast.2025.111255
[research_li_jin_2017]: https://doi.org/10.1080/00102202.2017.1376190
[research_li_jin_2021]: https://doi.org/10.1016/j.jaap.2021.105084
[research_li_lei_2022]: https://doi.org/10.3390/aerospace9040214
[research_li_leng_2023]: https://doi.org/10.1016/j.icheatmasstransfer.2022.106514
[research_li_li_2000]: https://doi.org/10.2514/6.2000-2228
[research_li_li_2022]: https://doi.org/10.1109/access.2021.3136612
[research_li_li_2026]: https://doi.org/10.2139/ssrn.6595195
[research_li_liang_2023]: https://doi.org/10.1016/j.ast.2023.108636
[research_li_ling_2026]: https://doi.org/10.1016/j.ijheatmasstransfer.2025.127808
[research_li_liu_2017]: https://doi.org/10.1016/j.actaastro.2017.05.036
[research_li_liu_2022]: https://doi.org/10.1109/tim.2022.3162287
[research_li_liu_2025]: https://doi.org/10.1063/5.0298885
[research_li_liu_2026]: https://doi.org/10.1016/j.actaastro.2026.08.053
[research_li_ma_2007]: https://doi.org/10.2514/6.2007-836
[research_li_ma_2024]: https://doi.org/10.1016/j.ast.2024.109461
[research_li_nagamatsu_1953]: https://doi.org/10.21236/ada278404
[research_li_ning_2025]: https://doi.org/10.3390/atmos16101120
[research_li_qin_2019]: https://doi.org/10.1016/j.actaastro.2018.11.021
[research_li_ren_2023]: https://doi.org/10.2139/ssrn.4552010
[research_li_shen_2017]: https://doi.org/10.2514/6.2017-2117
[research_li_shi_1993]: https://doi.org/10.2514/6.1993-3249
[research_li_sun_2020]: https://doi.org/10.3390/en13184801
[research_li_sun_2021]: https://doi.org/10.1002/suco.202100088
[research_li_sun_2024]: https://doi.org/10.1016/j.cja.2023.11.021
[research_li_sun_2024_b]: https://doi.org/10.3390/aerospace11070553
[research_li_tan_2017]: https://doi.org/10.2514/6.2017-2342
[research_li_tang_2021]: https://doi.org/10.1016/j.ast.2021.107080
[research_li_tang_2022]: https://doi.org/10.1016/j.ast.2022.107676
[research_li_wang_2011]: https://doi.org/10.5772/23528
[research_li_wang_2017]: https://doi.org/10.1016/j.ast.2017.02.021
[research_li_wang_2019]: https://doi.org/10.1080/00102202.2019.1594800
[research_li_wang_2021]: https://doi.org/10.1016/j.ces.2021.116806
[research_li_wang_2023]: https://doi.org/10.1016/j.fuel.2023.128659
[research_li_wang_2024]: https://doi.org/10.2139/ssrn.5071655
[research_li_wang_2024_b]: https://doi.org/10.2139/ssrn.4929935
[research_li_wang_2024_c]: https://doi.org/10.2298/tsci231223114l
[research_li_wang_2025]: https://doi.org/10.2139/ssrn.5360749
[research_li_wang_2026]: https://doi.org/10.1016/j.ast.2025.111576
[research_li_wey_1988]: https://doi.org/10.2514/6.1988-2675
[research_li_wu_2014]: https://doi.org/10.1063/1.4902579
[research_li_wu_2025]: https://doi.org/10.1016/j.ast.2025.110401
[research_li_xia_2019]: https://doi.org/10.3390/en12071235
[research_li_xie_2020]: https://doi.org/10.1016/j.applthermaleng.2020.115695
[research_li_xie_2021]: https://doi.org/10.1016/j.ijheatmasstransfer.2020.120836
[research_li_yang_2016]: https://doi.org/10.1155/2016/9407238
[research_li_yang_2020]: https://doi.org/10.1109/ccdc49329.2020.9164233
[research_li_yang_2020_b]: https://doi.org/10.1016/j.corsci.2019.108231
[research_li_yang_2026]: https://doi.org/10.1016/j.ast.2025.111088
[research_li_yu_2017]: https://doi.org/10.23919/chicc.2017.8028500
[research_li_zhan_2026]: https://doi.org/10.1016/j.icheatmasstransfer.2026.111695
[research_li_zhang_2015]: https://doi.org/10.2514/6.2015-3559
[research_li_zhang_2017]: https://doi.org/10.12783/dtmse/icmsea/mce2017/10838
[research_li_zhao_2014]: https://doi.org/10.2514/6.2014-2818
[research_li_zhao_2026]: https://doi.org/10.1088/1742-6596/3207/1/012072
[research_li_zhou_2004]: https://doi.org/10.2514/6.2004-3657
[research_li_zhou_2021]: https://doi.org/10.3390/app11209565
[research_li_zhou_2022]: https://doi.org/10.1155/2022/4625001
[research_li_zhu_2012]: https://doi.org/10.21611/qirt.2012.303
[research_lian_bai_2013]: https://doi.org/10.1109/imccc.2013.328
[research_lian_bai_2013_b]: https://doi.org/10.4028/www.scientific.net/amm.427-429.913
[research_lian_shi_2012]: https://doi.org/10.1007/978-3-642-34381-0_16
[research_lian_xiong_2025]: https://doi.org/10.1088/1742-6596/3085/1/012011
[research_liang_gao_2025]: https://doi.org/10.1007/s42064-024-0257-x
[research_liang_gong_2013]: https://doi.org/10.2514/6.2013-3698
[research_liang_guo_2024]: https://doi.org/10.1063/5.0187459
[research_liang_huang_2022]: https://doi.org/10.1063/5.0120400
[research_liang_wen_2025]: https://doi.org/10.23919/ccc64809.2025.11178558
[research_liang_xu_2021]: https://doi.org/10.1016/j.ast.2021.106566
[research_liao_chu_2023]: https://doi.org/10.1016/j.cja.2023.11.020
[research_libby_fox_1963]: https://doi.org/10.2514/6.1963-115
[research_lidar_complex_2020]: https://doi.org/10.15372/aoo20200510
[research_liever_habchi_2004]: https://doi.org/10.2514/6.2004-4725
[research_light_high_temperature_1992]: https://doi.org/10.2514/5.9781600866128.0141.0160
[research_lightweight_low_cost_2007]: https://doi.org/10.1108/aeat.2007.12779aad.010
[research_lijewski_1980]: https://doi.org/10.21236/ada104989
[research_lillis_1987]: https://doi.org/10.21236/ada182118
[research_lim_lee_2025]: https://doi.org/10.2514/6.2025-0469
[research_lim_wang_2006]: https://doi.org/10.2514/6.2006-6935
[research_limage_1978]: https://doi.org/10.2514/6.1978-1079
[research_limage_1996]: https://doi.org/10.2514/6.1996-2916
[research_lin_geng_2026]: https://doi.org/10.1016/j.icheatmasstransfer.2026.112304
[research_lin_luo_1995]: https://doi.org/10.2514/6.1995-1849
[research_lin_rao_1991]: https://doi.org/10.2514/6.1991-2162
[research_lin_shen_1995]: https://doi.org/10.2514/6.1995-1827
[research_lin_shen_1997]: https://doi.org/10.1016/s0045-7930(96)00026-6
[research_lin_tam_2006]: https://doi.org/10.2514/6.2006-816
[research_lin_tam_2007]: https://doi.org/10.2514/6.2007-5378
[research_lin_wu_2026]: https://doi.org/10.1016/j.ast.2026.113363
[research_lind_buffington_1999]: https://doi.org/10.2514/6.1999-4123
[research_lindsey_mcmullan_2006]: https://doi.org/10.2514/6.2006-371
[research_lindstedt_markaki_2009]: https://doi.org/10.21236/ada525798
[research_ling_wang_2025]: https://doi.org/10.1109/rcae66389.2025.11355185
[research_lino_oliveirajunior_2024]: https://doi.org/10.26678/abcm.conem2024.con24-1723
[research_linqi_qun_2015]: https://doi.org/10.1109/chicc.2015.7259769
[research_liou_benson_2010]: https://doi.org/10.2514/6.2010-1226
[research_liou_huang_2000]: https://doi.org/10.1016/s0045-7930(99)00010-9
[research_lippitt_jr_1983]: https://doi.org/10.21236/ada130685
[research_liquid_hydrocarbon_2001]: https://doi.org/10.2514/5.9781600866609.0757.0822
[research_liquid_phase_reactions_1978]: https://doi.org/10.2514/5.9781600865367.0307.0331
[research_liqun_chaoyang_2017]: https://doi.org/10.1109/ccdc.2017.7979401
[research_liston_small_1992]: https://doi.org/10.2514/6.1992-3337
[research_liu_1992]: https://doi.org/10.2514/6.1992-3512
[research_liu_1995]: https://doi.org/10.1007/978-3-642-79532-9_26
[research_liu_2014]: https://doi.org/10.2514/6.2014-3871
[research_liu_2023]: https://doi.org/10.54254/2755-2721/12/20230328
[research_liu_baccarella_2019]: https://doi.org/10.1016/j.proci.2018.08.037
[research_liu_bai_2020]: https://doi.org/10.2514/6.2020-2424
[research_liu_bi_2015]: https://doi.org/10.1016/j.fuel.2015.05.068
[research_liu_bian_2024]: https://doi.org/10.1016/j.icheatmasstransfer.2024.107322
[research_liu_brown_2012]: https://doi.org/10.2514/6.2012-3775
[research_liu_cai_2023]: https://doi.org/10.1109/cac59555.2023.10450472
[research_liu_cao_2017]: https://doi.org/10.1016/j.ijheatmasstransfer.2017.04.001
[research_liu_cao_2023]: https://doi.org/10.1016/j.energy.2022.125662
[research_liu_chen_2002]: https://doi.org/10.21236/ada403577
[research_liu_chen_2022]: https://doi.org/10.3390/aerospace9120811
[research_liu_chen_2026]: https://doi.org/10.1016/j.cja.2025.104000
[research_liu_ding_2014]: https://doi.org/10.1016/j.actaastro.2014.04.024
[research_liu_fan_2019]: https://doi.org/10.1016/j.actaastro.2019.04.041
[research_liu_fang_2023]: https://doi.org/10.1088/1742-6596/2636/1/012047
[research_liu_fang_2024]: https://doi.org/10.1088/1742-6596/2882/1/012049
[research_liu_gao_2019]: https://doi.org/10.1016/j.ast.2019.105391
[research_liu_han_2023]: https://doi.org/10.1016/j.energy.2023.129003
[research_liu_he_2022]: https://doi.org/10.1016/j.ijhydene.2021.12.126
[research_liu_hong_2014]: https://doi.org/10.1109/chicc.2014.6896035
[research_liu_hou_2010]: https://doi.org/10.1109/isscaa.2010.5633608
[research_liu_jiang_2013]: https://doi.org/10.2514/1.j051875
[research_liu_jun_2016]: https://doi.org/10.1115/gt2016-56929
[research_liu_li_2019]: https://doi.org/10.1016/j.measurement.2019.05.017
[research_liu_li_2025]: https://doi.org/10.1016/j.fuel.2025.134408
[research_liu_liang_2016]: https://doi.org/10.2514/1.a33348
[research_liu_liu_2016]: https://doi.org/10.1016/j.actaastro.2015.10.015
[research_liu_liu_2022]: https://doi.org/10.1049/icp.2022.1585
[research_liu_lu_2011]: https://doi.org/10.21236/ada564811
[research_liu_luo_2020]: https://doi.org/10.1109/cac51589.2020.9327809
[research_liu_luo_2020_b]: https://doi.org/10.1007/s42401-020-00061-y
[research_liu_lyu_2025]: https://doi.org/10.1016/j.cja.2024.103339
[research_liu_manzie_2022]: https://doi.org/10.23919/acc53348.2022.9867349
[research_liu_pan_2022]: https://doi.org/10.1016/j.fuel.2022.124688
[research_liu_pan_2024]: https://doi.org/10.1016/j.fuel.2023.129466
[research_liu_pang_2022]: https://doi.org/10.1016/j.flowmeasinst.2022.102264
[research_liu_qiao_2022]: https://doi.org/10.2514/6.2022-0202
[research_liu_shan_2025]: https://doi.org/10.1117/12.3060755
[research_liu_shen_2015]: https://doi.org/10.1007/s10957-015-0831-8
[research_liu_shi_2018]: https://doi.org/10.1615/ihtc16.tpm.022494
[research_liu_song_2019]: https://doi.org/10.1007/978-981-13-3305-7_69
[research_liu_squire_1986]: https://doi.org/10.1007/978-3-642-82770-9_8
[research_liu_wang_2005]: https://doi.org/10.1007/978-3-540-27009-6_21
[research_liu_wang_2009]: https://doi.org/10.2514/6.2009-5299
[research_liu_wang_2014]: https://doi.org/10.1109/chicc.2014.6896504
[research_liu_wang_2016]: https://doi.org/10.1109/chicc.2016.7555029
[research_liu_wang_2017]: https://doi.org/10.1016/j.ijhydene.2017.09.179
[research_liu_wu_2022]: https://doi.org/10.1063/5.0123724
[research_liu_xiao_2007]: https://doi.org/10.2514/6.2007-5413
[research_liu_xie_2021]: https://doi.org/10.1109/cacre52464.2021.9501317
[research_liu_xu_2025]: https://doi.org/10.2139/ssrn.5079936
[research_liu_xue_2023]: https://doi.org/10.1016/j.applthermaleng.2023.121017
[research_liu_yang_2023]: https://doi.org/10.1016/j.cja.2022.09.024
[research_liu_yang_2026]: https://doi.org/10.1088/1742-6596/3207/1/012046
[research_liu_yao_2021]: https://doi.org/10.2514/6.2021-3536
[research_liu_yao_2021_b]: https://doi.org/10.2514/6.2021-3536.c1
[research_liu_zhang_2018]: https://doi.org/10.1360/n092017-00373
[research_liu_zhang_2019]: https://doi.org/10.1016/j.ijheatmasstransfer.2019.06.023
[research_liu_zhang_2025]: https://doi.org/10.1109/cac67268.2025.11487632
[research_liu_zhang_2026]: https://doi.org/10.2139/ssrn.6075813
[research_liu_zhao_2005]: https://doi.org/10.2514/6.2005-5250
[research_liu_zhu_2025]: https://doi.org/10.1109/tim.2025.3547093
[research_lloyd_1959]: https://doi.org/10.1016/0010-2180(59)90027-6
[research_lobb_winkler_1955]: https://doi.org/10.21236/ad0068499
[research_lobbia_2015]: https://doi.org/10.2514/6.2015-0757
[research_lobbia_suzuki_2003]: https://doi.org/10.2514/6.2003-3804
[research_lock_oberman_2025]: https://doi.org/10.2514/6.2025-1337
[research_lockmanwk_1967]: https://ntrs.nasa.gov/citations/19670060153
[research_lockwood_petley_1996]: https://doi.org/10.2514/6.1996-381
[research_lockwood_petley_1999]: https://doi.org/10.1016/s0376-0421(98)00008-6
[research_lofthouse_hughson_2002]: https://doi.org/10.2514/6.2002-306
[research_loh_hui_1991]: https://doi.org/10.2514/6.1991-1546
[research_lohner_yang_2002]: https://doi.org/10.21236/ada419909
[research_long_jr_1992]: https://doi.org/10.21236/ada248159
[research_longwell_weiss_1952]: https://doi.org/10.21236/ad0041743
[research_lonkar_panda_2025]: https://doi.org/10.2139/ssrn.5902346
[research_lonkar_panda_2026]: https://doi.org/10.1016/j.ast.2026.112194
[research_loper_lightsey_1967]: https://doi.org/10.21236/ad0645107
[research_losik_2008]: https://doi.org/10.2514/6.2008-7698
[research_loth_candon_2016]: https://doi.org/10.2514/6.2016-0532
[research_louda_prihoda_2018]: https://doi.org/10.1063/1.5043663
[research_louismedelman]: https://ntrs.nasa.gov/citations/20240008352
[research_low_temperature_2016]: https://doi.org/10.21275/v5i1.nov152922
[research_lowell_1963]: https://doi.org/10.21236/ad0427185
[research_lu_1991]: https://doi.org/10.2514/6.1991-5068
[research_lu_jiang_2019]: https://doi.org/10.1145/3387304.3387311
[research_lu_li_2012]: https://doi.org/10.2514/6.2012-5878
[research_lu_liu_2011]: https://doi.org/10.4028/www.scientific.net/amm.108.41
[research_lu_liu_2012]: https://doi.org/10.1016/j.proeng.2012.01.626
[research_lu_mahapatra_2008]: https://doi.org/10.1063/1.2979323
[research_lu_sheng_2025]: https://doi.org/10.1016/j.fuel.2024.134216
[research_lu_wang_2016]: https://doi.org/10.2514/6.2016-4708
[research_lu_zhang_2016]: https://doi.org/10.2991/imst-16.2016.15
[research_lu_zhang_2016_b]: https://doi.org/10.1109/cgncc.2016.7828815
[research_lu_zhang_2025]: https://doi.org/10.3390/math13030380
[research_lu_zhou_2017]: https://doi.org/10.1109/ccdc.2017.7978461
[research_lubarsky_levy_1998]: https://doi.org/10.1016/s0082-0784(98)80049-0
[research_lubing_yang_2017]: https://doi.org/10.23919/chicc.2017.8027532
[research_lubing_yangfei_2020]: https://doi.org/10.23919/ccc50068.2020.9189249
[research_lubonski_1964]: https://doi.org/10.1016/b978-0-08-011007-3.50017-2
[research_luce_flowers_1961]: https://doi.org/10.2172/4031729
[research_luce_jr_1949]: https://doi.org/10.21236/ada278113
[research_lucquin_antonik_1972]: https://doi.org/10.1016/s0010-2180(72)80224-4
[research_ludeke_schulein_2003]: https://doi.org/10.1007/978-3-642-59334-5_113
[research_ludwig_sulzmann_1961]: https://doi.org/10.21236/ad0257971
[research_luecke_1957]: https://doi.org/10.1109/irettrc.1957.6541492
[research_lugrin]: https://doi.org/10.70675/b81b1038z2459z47dczbe4fz2d427e9ae52d
[research_lujan_climent_2016]: https://doi.org/10.1016/j.applthermaleng.2016.03.028
[research_lukasiewicz_1961]: https://doi.org/10.21236/ad0259455
[research_lumpkiniii_chapman_1991]: https://doi.org/10.2514/6.1991-771
[research_lunan_2015]: https://doi.org/10.2514/6.2015-3529
[research_luo_1999]: https://doi.org/10.1016/s0010-2180(99)00074-7
[research_luo_baysal_1999]: https://doi.org/10.2514/6.1999-4807
[research_luo_bray_1998]: https://doi.org/10.1016/s0082-0784(98)80065-9
[research_luo_feng_2022]: https://doi.org/10.1016/j.ast.2022.107798
[research_luo_he_2025]: https://doi.org/10.1109/tits.2025.3579130
[research_luo_luo_2003]: https://doi.org/10.2514/6.2003-5193
[research_luo_sun_2025]: https://doi.org/10.1016/j.combustflame.2025.113999
[research_luo_tao_2024]: https://doi.org/10.1061/jaeeez.aseng-5388
[research_luo_tian_2026]: https://doi.org/10.2139/ssrn.7128243
[research_luo_wang_2015]: https://doi.org/10.2991/ifeesm-15.2015.156
[research_luo_wei_2020]: https://doi.org/10.3390/en13010217
[research_lushchik_sizov_1993]: https://doi.org/10.1007/bf01342684
[research_luxbaumannjessica_burkesdarryl_2006]: https://ntrs.nasa.gov/citations/20090007796
[research_luxjessica_burkesdarryla_2008]: https://ntrs.nasa.gov/citations/20080007525
[research_lv_li_2026]: https://doi.org/10.2139/ssrn.6351266
[research_lv_zhou_2023]: https://doi.org/10.1142/s2737480723500115
[research_lynch_1968]: https://doi.org/10.4271/680369
[research_lyon_1992]: https://doi.org/10.1520/stp15041s
[research_ma_liu_2023]: https://doi.org/10.1109/ccdc58219.2023.10327666
[research_ma_sun_2021]: https://doi.org/10.1016/j.actaastro.2021.02.020
[research_ma_wu_2020]: https://doi.org/10.1109/icca51439.2020.9264516
[research_ma_xie_2022]: https://doi.org/10.2139/ssrn.3983112
[research_ma_yuan_2006]: https://doi.org/10.2514/6.2006-7990
[research_ma_zhong_1999]: https://doi.org/10.2514/6.1999-416
[research_maalnimrnasersalhuniti_2000]: https://doi.org/10.1080/01495730050192383
[research_maas_irvine_2004]: https://doi.org/10.21236/ada433721
[research_maccallum_1969]: https://doi.org/10.1243/pime_conf_1969_184_179_02
[research_maccormack_1989]: https://doi.org/10.2514/6.1989-461
[research_mace_nyberg_1992]: https://doi.org/10.2514/6.1992-3333
[research_macheret_shneider_2001]: https://doi.org/10.2514/6.2001-492
[research_machnik_decker_2022]: https://doi.org/10.5162/ettc2022/4.2
[research_machrafi_cavadiasa_2008]: https://doi.org/10.1016/j.fuproc.2008.05.019
[research_mack_steelant_2009]: https://doi.org/10.1007/978-3-540-85168-4_99
[research_mackenzie_1967]: https://doi.org/10.2172/4491453
[research_mackle]: https://doi.org/10.14264/f113470
[research_mackle_jahn_2024]: https://doi.org/10.2514/6.2024-2838
[research_mackle_lock_2024]: https://doi.org/10.2514/6.2024-0238
[research_macmahan_reniers_2012]: https://doi.org/10.21236/ada572941
[research_macmillan_1981]: https://doi.org/10.2514/6.1981-2350
[research_maddalena_gopal_2023]: https://doi.org/10.2514/6.2023-3043
[research_madden_solomon_1993]: https://doi.org/10.2514/6.1993-2143
[research_madhumitha_karmakar_2024]: https://doi.org/10.1016/j.fpc.2023.07.003
[research_magomedov_2009]: https://doi.org/10.1134/s0018151x09020114
[research_mahapatra_lu_2008]: https://doi.org/10.1007/s00339-008-4926-z
[research_mahato_sarikonda_2023]: https://doi.org/10.2514/6.2023-3035
[research_mahlmeister_ishimoto_1955]: https://doi.org/10.21236/ad0093337
[research_mahmoud_hao_2017]: https://doi.org/10.1109/iccairo.2017.35
[research_mahulikar_khurana_2008]: https://doi.org/10.1007/bf03256567
[research_maisaia_2023]: https://doi.org/10.2514/6.2023-3234
[research_maita_ohkami_1990]: https://doi.org/10.2514/6.1990-5225
[research_majumdar_2011]: https://doi.org/10.5772/16284
[research_makhija_bodi_2026]: https://doi.org/10.2139/ssrn.7181476
[research_maleque_2016]: https://doi.org/10.7726/ajhmt.2016.1011
[research_malik]: https://doi.org/10.14264/2bac077
[research_mallikarjun_casseau_2023]: https://doi.org/10.1080/10618562.2024.2306946
[research_malsurdharavath_pmanna_2023]: https://doi.org/10.61653/joast.v70i2.2018.358
[research_mane_pandey_2026]: https://doi.org/10.1016/j.ijhydene.2026.155887
[research_mani_haney_1994]: https://doi.org/10.2514/6.1994-156
[research_manimaran_2016]: https://doi.org/10.1016/j.energy.2016.04.005
[research_manke_2005]: https://doi.org/10.21236/ada430093
[research_mann_garner_1977]: https://doi.org/10.21236/ada040707
[research_manna_dharavath_2023]: https://doi.org/10.61653/joast.v61i4.2009.589
[research_mannai_1962]: https://doi.org/10.1016/0016-0032(62)91055-4
[research_manning_baum_1992]: https://doi.org/10.2514/6.1992-4115
[research_manojprabakar_muruganandam_2019]: https://doi.org/10.1007/978-3-319-91017-8_139
[research_manor_lau_2002]: https://doi.org/10.2514/6.2002-5160
[research_mao_2023]: https://doi.org/10.54254/2755-2721/25/20230774
[research_maoruizhang_yongsun_2010]: https://doi.org/10.1109/wcica.2010.5554588
[research_marchand_1989]: https://doi.org/10.21236/ada210195
[research_marconif_salasm_1976]: https://ntrs.nasa.gov/citations/19760015406
[research_marcum_2001]: https://doi.org/10.21236/ada387492
[research_margaritis_scherding_2024]: https://doi.org/10.2139/ssrn.4952314
[research_marin_tombolesi_2021]: https://doi.org/10.26434/chemrxiv-2021-2kfrp
[research_marinho_defarias_2020]: https://doi.org/10.26434/chemrxiv.12921455.v1
[research_markova_aksenov_2017]: https://doi.org/10.1134/s0018151x17020092
[research_marley_driscoll_2017]: https://doi.org/10.2514/6.2017-0118
[research_marley_driscoll_2018]: https://doi.org/10.2514/6.2018-0280
[research_marley_driscoll_2022]: https://doi.org/10.2514/1.c036411
[research_marlina_2018]: https://doi.org/10.31851/redoks.v1i1.2016
[research_marquart_1991]: https://doi.org/10.2514/6.1991-3320
[research_marren_lewis_2001]: https://doi.org/10.2514/2.5888
[research_marschall_2011]: https://doi.org/10.21236/ada553782
[research_marsh_sears_1954]: https://doi.org/10.2514/8.6480
[research_marshall_corpening_2005]: https://doi.org/10.2514/6.2005-3332
[research_marshall_cox_2014]: https://doi.org/10.21236/ada609952
[research_marshall_davis_2001]: https://doi.org/10.21236/ada389369
[research_marston_1965]: https://doi.org/10.21236/ad0454992
[research_martel_1970]: https://doi.org/10.21236/ad0712368
[research_martel_1988]: https://doi.org/10.21236/ada197270
[research_martin_gerber_1953]: https://doi.org/10.21236/ad0014217
[research_martin_karasi_1998]: https://doi.org/10.2514/6.1998-5261
[research_martin_peter_2026]: https://doi.org/10.33737/jgpps/213543
[research_martinezmoran_2018]: https://doi.org/10.5162/ettc2018/11.1
[research_marvin_1968]: https://doi.org/10.2514/6.1968-648
[research_mary_sagaut_2001]: https://doi.org/10.2514/6.2001-2559
[research_mashburn_1969]: https://doi.org/10.21236/ad0690947
[research_mashio_kurashina_2001]: https://doi.org/10.2514/6.2001-1887
[research_maslov_2001]: https://doi.org/10.21236/ada408241
[research_massa_2022]: https://doi.org/10.1016/j.ijheatmasstransfer.2022.122772
[research_massa_pace_2025]: https://doi.org/10.2514/6.2025-0390
[research_masson_jumper_1989]: https://doi.org/10.2514/6.1989-1920
[research_mateer_brosh_1976]: https://doi.org/10.2514/6.1976-161
[research_matheny_panageas_1981]: https://doi.org/10.2514/6.1981-2433
[research_matheny_smith_2026]: https://doi.org/10.2514/6.2026-112162
[research_mathur_2026]: https://doi.org/10.2514/6.2026-5016
[research_mathur_2026_b]: https://doi.org/10.2514/6.2026-5016.c1
[research_mathur_gruber_2001]: https://doi.org/10.2514/2.5879
[research_mathur_streby_1999]: https://doi.org/10.2514/6.1999-2102
[research_matsukawa_2011]: https://doi.org/10.1080/10618562.2011.555334
[research_matsunaga_takahashi_2017]: https://doi.org/10.2514/6.2017-0263
[research_matsuo_kim_2023]: https://doi.org/10.1615/istp-vi.940
[research_matsuyama_ohnishi_2003]: https://doi.org/10.1016/b978-044450680-1/50062-0
[research_matthews_1992]: https://doi.org/10.1007/978-1-4612-0379-7_3
[research_matthews_1993]: https://doi.org/10.1007/978-94-011-1828-6_41
[research_matthews_jones_2005]: https://doi.org/10.2514/6.2005-3379
[research_matthews_trimmer_1969]: https://doi.org/10.21236/ad0854309
[research_maus_griffith_1983]: https://doi.org/10.2514/6.1983-343
[research_maxwell_2016]: https://doi.org/10.2514/6.2016-4706
[research_maxwell_2017]: https://doi.org/10.2514/6.2017-4880
[research_maxwell_2017_b]: https://doi.org/10.2514/6.2017-3983
[research_maxwell_2019]: https://doi.org/10.2514/6.2019-3597
[research_maxwell_goodwin_2017]: https://doi.org/10.2514/6.2017-1385
[research_maxwell_goodwin_2018]: https://doi.org/10.2514/6.2018-3564
[research_maxwell_goodwin_2018_b]: https://doi.org/10.2514/6.2018-3564.c1
[research_maxwell_goodwin_2018_c]: https://doi.org/10.2514/6.2018-3545
[research_maxwell_hoang_2016]: https://doi.org/10.2514/6.2016-4149
[research_maxwell_phoenix_2017]: https://doi.org/10.2514/6.2017-5357
[research_may_richey_1979]: https://doi.org/10.2514/6.1979-1120
[research_maydew_1964]: https://doi.org/10.2172/4000106
[research_mayer_chalfant_2023]: https://doi.org/10.61653/joast.v61i1.2009.648
[research_mayer_paynter_1994]: https://doi.org/10.2514/6.1994-580
[research_mayer_paynter_1995]: https://doi.org/10.2514/3.12418
[research_maynard_patel_2025]: https://doi.org/10.2514/1.a36296
[research_mayne_1976]: https://doi.org/10.1177/058310247600800108
[research_mayne_1979]: https://doi.org/10.1177/058310247901101004
[research_mayrhofer_sachs_1999]: https://doi.org/10.2514/6.1999-4886
[research_mazdiyasni_1989]: https://doi.org/10.21236/ada211070
[research_mazdiyasni_chen_1988]: https://doi.org/10.21236/ada202867
[research_mazdiyasni_chen_1991]: https://doi.org/10.21236/ada239813
[research_mbagwu_driscoll_2018]: https://doi.org/10.2514/1.b36479
[research_mccarthy_2008]: https://doi.org/10.1016/s1350-4789(08)70606-8
[research_mcclinton_1976]: https://doi.org/10.2514/6.1976-47
[research_mcclinton_hunt_1999]: https://doi.org/10.2514/6.1999-4978
[research_mcclinton_roudakov_1996]: https://doi.org/10.2514/6.1996-4571
[research_mcclure_sirbaugh_1991]: https://doi.org/10.21236/ada232101
[research_mcconnell_2004]: https://doi.org/10.2514/6.2004-5048
[research_mccormick_wakayama_2010]: https://doi.org/10.2514/6.2010-8906
[research_mccown_barrett_1966]: https://doi.org/10.2514/3.28514
[research_mccracken_1970]: https://doi.org/10.21236/ad0714674
[research_mcdaniel_2005]: https://doi.org/10.1063/1.1941709
[research_mcdanieljr_1998]: https://doi.org/10.2514/6.1998-1646
[research_mcdonald_1960]: https://doi.org/10.2172/4181737
[research_mcdonald_2025]: https://doi.org/10.2139/ssrn.5239646
[research_mcdonald_mavris_2000]: https://doi.org/10.2514/6.2000-5559
[research_mcdonald_rice_2017]: https://doi.org/10.1016/j.combustflame.2016.10.012
[research_mcelderry_1973]: https://doi.org/10.21236/ada377039
[research_mcgill_2000]: https://doi.org/10.2514/6.2000-939
[research_mcgrory_2001]: https://doi.org/10.21236/ada399497
[research_mcintoshjr_1964]: https://doi.org/10.2514/6.1964-1027
[research_mcintoshjr_1972]: https://doi.org/10.2514/6.1972-345
[research_mckenzie_1973]: https://doi.org/10.2514/6.1973-782
[research_mckenzie_fletcher_1993]: https://doi.org/10.1007/978-94-011-1828-6_21
[research_mclean]: https://doi.org/10.31274/rtd-180816-406
[research_mclean_matoi_1986]: https://doi.org/10.1007/978-3-642-82770-9_25
[research_mcmillin_1969]: https://doi.org/10.21236/ad0863198
[research_mcquaid_2013]: https://doi.org/10.21236/ada588893
[research_mcquellin_buttsworth_2024]: https://doi.org/10.2514/6.2024-2889
[research_mcquellin_neely_2020]: https://doi.org/10.2514/6.2020-2419
[research_mcrae_edwards_2001]: https://doi.org/10.21236/ada399718
[research_mcrae_neaves_1998]: https://doi.org/10.21236/ada336232
[research_mcruer_1991]: https://doi.org/10.23919/acc.1991.4791471
[research_mctaggart_1973]: https://doi.org/10.21236/ad0769043
[research_mease_vinh_1988]: https://doi.org/10.2514/6.1988-4341
[research_measurement_of_2015]: https://doi.org/10.13031/aim.20152190521
[research_measurement_techniques_1974]: https://doi.org/10.2514/5.9781600865077.0263.0282
[research_measuring_kinematic_1998]: https://doi.org/10.1017/cbo9780511599835.003
[research_medina_patel_2021]: https://doi.org/10.2514/6.2021-4096
[research_medwick_castro_1999]: https://doi.org/10.21236/ada373274
[research_mee]: https://doi.org/10.14264/284113
[research_mehta_bowles_2012]: https://doi.org/10.2514/6.2012-5874
[research_mehta_brewer_2025]: https://doi.org/10.2514/6.2025-1041
[research_mehtaunmeelb_kutlerpaul_1994]: https://ntrs.nasa.gov/citations/20020010588
[research_meier_1984]: https://doi.org/10.2172/6510753
[research_meintanis_bengtson_2002]: https://doi.org/10.1061/40625(203)3
[research_meisel_cote_1985]: https://doi.org/10.21236/ada152477
[research_melis_gladden_1990]: https://doi.org/10.2514/6.1990-5228
[research_melville_helmich_2021]: https://doi.org/10.2172/1892153
[research_mendiratta_choudhury_1978]: https://doi.org/10.21236/ada060386
[research_meng_jin_2024]: https://doi.org/10.3390/aerospace11110941
[research_meng_sun_2022]: https://doi.org/10.3390/aerospace9120826
[research_meng_sun_2024]: https://doi.org/10.1063/5.0193282
[research_meng_tian_2021]: https://doi.org/10.1109/icras52289.2021.9476537
[research_meng_ye_2020]: https://doi.org/10.1016/j.actaastro.2019.09.035
[research_menne_weiland_1994]: https://doi.org/10.2514/3.46540
[research_menon_1989]: https://doi.org/10.2514/6.1989-104
[research_menon_1990]: https://doi.org/10.2514/6.1990-3930
[research_menon_1991]: https://doi.org/10.2514/6.1991-411
[research_menon_1992]: https://doi.org/10.21236/ada255226
[research_menon_1992_b]: https://doi.org/10.1080/00102209208951845
[research_menon_genin_2003]: https://doi.org/10.2514/6.2003-7035
[research_menon_jou_1990]: https://doi.org/10.2514/6.1990-267
[research_menon_jou_1991]: https://doi.org/10.1080/00102209108924078
[research_menssen_2026]: https://doi.org/10.2514/6.2026-111626
[research_meriwether_2005]: https://doi.org/10.21236/ada438584
[research_merkle_2007]: https://doi.org/10.21236/ada475651
[research_merkli_1975]: https://doi.org/10.21236/ada033630
[research_mermagen_1964]: https://doi.org/10.21236/ad0444246
[research_mermagen_yalamanchili_1983]: https://doi.org/10.21236/ada130598
[research_merriam_smoluchowski_1962]: https://doi.org/10.1103/physrev.125.65
[research_merryman_1962]: https://doi.org/10.2172/4051459
[research_mertaugh_1998]: https://doi.org/10.21236/ada350674
[research_merz_1968]: https://doi.org/10.21236/ad0830135
[research_meshcheryakov_yashina_2015]: https://doi.org/10.1615/tsagiscij.v46.i5.40
[research_messersmith_1995]: https://doi.org/10.2514/6.1995-3058
[research_messitt_dallemagne_1992]: https://doi.org/10.2514/6.1992-3808
[research_mestwerdt_rambauske_1961]: https://doi.org/10.21236/ad0262000
[research_metallic_seal]: https://doi.org/10.4271/air1077
[research_metghalchi_2009]: https://doi.org/10.21236/ada516408
[research_methodology_for]: https://doi.org/10.4271/air5875
[research_meuwly_2014]: https://doi.org/10.21236/ada611797
[research_meyer_1958]: https://doi.org/10.21236/ad0208856
[research_meyer_1969]: https://doi.org/10.2514/6.1969-707
[research_meyer_butler_1997]: https://doi.org/10.2514/6.1997-427
[research_mi_wang_2025]: https://doi.org/10.1016/j.fuel.2024.134055
[research_miao_wang_2020]: https://doi.org/10.1016/j.applthermaleng.2020.115751
[research_michalski_boust_2018]: https://doi.org/10.2514/6.2018-4478
[research_micka_driscoll_2008]: https://doi.org/10.2514/6.2008-5071
[research_micka_driscoll_2009]: https://doi.org/10.1016/j.proci.2008.06.192
[research_midea_1991]: https://doi.org/10.2514/6.1991-3196
[research_miele_1962]: https://doi.org/10.21236/ad0296177
[research_miele_hull_1963]: https://doi.org/10.21236/ad0404858
[research_miele_pritchard_1963]: https://doi.org/10.21236/ad0403460
[research_miele_saaris_1963]: https://doi.org/10.21236/ad0407784
[research_miers_alshehab_2020]: https://doi.org/10.1063/12.0001096
[research_mifsud_estruchsamper_2012]: https://doi.org/10.1017/s0001924000007338
[research_mikhail_1979]: https://doi.org/10.21236/ada076116
[research_mikhaylov_2013]: https://doi.org/10.1088/1742-6596/461/1/012035
[research_mikkelsen_long_2005]: https://doi.org/10.2514/6.2005-692
[research_mikulla_horstman_1976]: https://doi.org/10.2514/6.1976-162
[research_miles_1998]: https://doi.org/10.21236/ada389059
[research_miles_2001]: https://doi.org/10.21236/ada389151
[research_miles_2003]: https://doi.org/10.2514/6.2003-90
[research_miles_brown_2002]: https://doi.org/10.21236/ada403037
[research_miles_macheret_2006]: https://doi.org/10.21236/ada458308
[research_miller_1965]: https://doi.org/10.2514/6.1965-605
[research_miller_1999]: https://doi.org/10.1115/imece1999-0149
[research_miller_argrow_1997]: https://doi.org/10.2514/6.1997-189
[research_miller_nagpal_2011]: https://doi.org/10.21236/ada537783
[research_miller_smith_2003]: https://doi.org/10.1115/fedsm2003-45471
[research_millerd]: https://doi.org/10.14264/fc09cc4
[research_milligan_wolff_2009]: https://doi.org/10.2514/6.2009-1254
[research_mills_2001]: https://doi.org/10.21236/ada410750
[research_mills_2002]: https://doi.org/10.21236/ada410680
[research_min_hailong_2009]: https://doi.org/10.1016/s1000-9361(08)60130-2
[research_min_hong_2024]: https://doi.org/10.1155/2024/2284914
[research_min_sun_2026]: https://doi.org/10.2139/ssrn.7133946
[research_minard_falempin_2008]: https://doi.org/10.2514/6.2008-2650
[research_minato_higashino_2009]: https://doi.org/10.2514/6.2009-7392
[research_minato_higashino_2012]: https://doi.org/10.5772/34146
[research_miner_lewis_1974]: https://doi.org/10.2514/3.49179
[research_minimum_performance]: https://doi.org/10.4271/as855
[research_minimum_performance_b]: https://doi.org/10.4271/as8003
[research_mirhosseini_najafi_2025]: https://doi.org/10.1016/j.injury.2025.112448
[research_mirmirani_kuipers_2009]: https://doi.org/10.1109/acc.2009.5160500
[research_mirmirani_wu_2005]: https://doi.org/10.2514/6.2005-6256
[research_mironov_aniskin_2004]: https://doi.org/10.1016/j.crme.2004.04.007
[research_mishler_wilkinson_1992]: https://doi.org/10.2514/6.1992-3335
[research_misra_1994]: https://doi.org/10.21236/ada283201
[research_mitani_1995]: https://doi.org/10.1016/0010-2180(94)00218-h
[research_mitani_1996]: https://doi.org/10.1016/s0082-0784(96)80133-0
[research_mitani_izumikawa_2000]: https://doi.org/10.1016/s0082-0784(00)80270-2
[research_mitani_kouchi_2005]: https://doi.org/10.1016/j.combustflame.2004.10.004
[research_mitani_tomioka_2003]: https://doi.org/10.2514/6.2003-7009
[research_mitran_2001]: https://doi.org/10.2514/6.2001-2908
[research_mittal_shahriar_2026]: https://doi.org/10.2514/6.2026-2676
[research_miyajima_chinzei_1992]: https://doi.org/10.2514/6.1992-5094
[research_miyashita_matsuo_2025]: https://doi.org/10.2514/6.2025-0947
[research_miyashita_sugihara_2025]: https://doi.org/10.1063/5.0250348
[research_miyaura_daimon_2018]: https://doi.org/10.1299/jsmemecj.2018.g0600205
[research_miyazaki_yoshida_1986]: https://doi.org/10.7209/tanso.1986.18
[research_miyazawa_2000]: https://doi.org/10.2514/6.2000-4256
[research_modelling_endothermic_1997]: https://doi.org/10.1016/s0140-6701(97)80085-9
[research_moga_1980]: https://doi.org/10.21236/ada091235
[research_mohamadi_tahsini_2023]: https://doi.org/10.1108/aeat-02-2023-0030
[research_mohieldin_carson_2003]: https://doi.org/10.2514/6.2003-7036
[research_mohieldin_tiwari_2001]: https://doi.org/10.2514/6.2001-3296
[research_mohieldinto_tiwarisn_2004]: https://ntrs.nasa.gov/citations/20050041724
[research_moin_lele_1998]: https://doi.org/10.21236/ada343835
[research_molina_simeonides_1996]: https://doi.org/10.2514/6.1996-2468
[research_molvik_bowles_1992]: https://doi.org/10.2514/6.1992-3425
[research_molvik_bowles_1993]: https://doi.org/10.2514/6.1993-509
[research_molvik_bowles_1993_b]: https://doi.org/10.2514/6.1993-5097
[research_molvikgregorya_merklecharlesl_1989]: https://ntrs.nasa.gov/citations/19890037803
[research_mondal_jagtap_2026]: https://doi.org/10.1063/5.0324870
[research_montagnejl_yeehc_1988]: https://ntrs.nasa.gov/citations/19880008960
[research_montagnejl_yeehc_1989]: https://ntrs.nasa.gov/citations/19890061394
[research_monteil_2024]: https://doi.org/10.5162/ettc2024/a1.4
[research_montes_king_2005]: https://doi.org/10.2514/6.2005-3913
[research_montgomery_cremer_2006]: https://doi.org/10.21236/ada445989
[research_montgomery_garrard_2005]: https://doi.org/10.2514/6.2005-3900
[research_mooij_2023]: https://doi.org/10.2514/6.2023-2499
[research_moon_sung_2015]: https://doi.org/10.2514/6.2015-3526
[research_moore_1965]: https://doi.org/10.2514/6.1965-196
[research_moorhouse_1990]: https://doi.org/10.2514/6.1990-3306
[research_moran_kolb_1977]: https://doi.org/10.21236/ada041779
[research_moran_mcquellin_2023]: https://doi.org/10.2514/6.2023-1385
[research_morani_fruncillo_2026]: https://doi.org/10.2514/6.2026-5046
[research_moreira_azevedo_2005]: https://doi.org/10.2514/6.2005-5225
[research_morelli_2008]: https://doi.org/10.2514/6.2008-1682
[research_moretti_byrne_1964]: https://doi.org/10.1016/b978-1-4831-9828-6.50013-8
[research_morgan_duraisamy_2012]: https://doi.org/10.2514/6.2012-1094
[research_morgan_duraisamy_2014]: https://doi.org/10.2514/1.j052348
[research_morgan_stalker_1985]: https://doi.org/10.2514/6.1985-908
[research_morgan_zander_2009]: https://doi.org/10.1007/978-3-540-85181-3_55
[research_morger_1988]: https://doi.org/10.2514/6.1988-2091
[research_mori_1965]: https://doi.org/10.1299/jsmemag.68.562_1587
[research_mori_ishibashi_2012]: https://doi.org/10.2514/6.2012-3008
[research_mori_maita_2001]: https://doi.org/10.2514/6.2001-1803
[research_mori_masutani_1993]: https://doi.org/10.1016/0016-2361(93)90128-o
[research_mori_tsuchiya_2002]: https://doi.org/10.2514/6.2002-5221
[research_morimoto_chuang_1998]: https://doi.org/10.2514/6.1998-4122
[research_morinishi_1999]: https://doi.org/10.1016/b978-044482850-7/50097-8
[research_morita_tsuchiya_2020]: https://doi.org/10.2514/6.2020-2402
[research_morris_jr_2002]: https://doi.org/10.21236/ada410074
[research_morris_tigner_1995]: https://doi.org/10.2514/6.1995-3327
[research_moses_bouchard_1999]: https://doi.org/10.2514/6.1999-4948
[research_moss_boyles_2006]: https://doi.org/10.2514/6.2006-8081
[research_moss_simmonds_1987]: https://doi.org/10.2514/6.1987-404
[research_moss_vasile_2026]: https://doi.org/10.2514/6.2026-4177
[research_moszee_moszee_1997]: https://doi.org/10.2514/6.1997-3395
[research_mott_oran_2001]: https://doi.org/10.21236/ada385560
[research_moulic_1963]: https://doi.org/10.21236/ad0402416
[research_moura_borgesribeiro_2025]: https://doi.org/10.26678/abcm.cobem2025.cob2025-1480
[research_moura_borgesribeiro_2025_b]: https://doi.org/10.26678/abcm.cobem2025.cob2025-0300
[research_moura_borgesribeiro_2025_c]: https://doi.org/10.26678/abcm.cobem2025.cob2025-1507
[research_moura_borgesribeiro_2025_d]: https://doi.org/10.26678/abcm.cobem2025.cob2025-0360
[research_moura_borgesribeiro_2025_e]: https://doi.org/10.26678/abcm.cobem2025.cob2025-1499
[research_moura_ribeiro_2024]: https://doi.org/10.26678/abcm.encit2024.cit24-0501
[research_moura_wheatley_2019]: https://doi.org/10.1007/s00193-019-00908-0
[research_mrozinski_hayes_1999]: https://doi.org/10.2514/6.1999-899
[research_mu_wang_2022]: https://doi.org/10.2514/6.2022-0203
[research_mu_zheng_2008]: https://doi.org/10.1115/pvp2008-61895
[research_mudaliar_gomes_2022]: https://doi.org/10.4273/ijvss.14.1.23
[research_muddamarri_mbadgujar_2024]: https://doi.org/10.2139/ssrn.4715358
[research_muddasar_2022]: https://doi.org/10.20944/preprints202201.0051.v1
[research_mueller_1989]: https://doi.org/10.2514/6.1989-1977
[research_muhammadhaseeb_2025]: https://doi.org/10.12732/ijam.v38i10s.945
[research_mukherjee_thomson_2009]: https://doi.org/10.21236/ada498597
[research_mungal_1998]: https://doi.org/10.21236/ada354071
[research_munipalli_subbarao_2005]: https://doi.org/10.21236/ada435356
[research_munuswamy_govardhan_2022]: https://doi.org/10.1007/s00348-022-03488-5
[research_mura_sabelnikov_2021]: https://doi.org/10.1017/9781108671422.008
[research_murbach_1993]: https://doi.org/10.2514/6.1993-313
[research_murphy_buning_2004]: https://doi.org/10.2514/6.2004-2595
[research_murray_2012]: https://doi.org/10.21236/ada556126
[research_murray_hillier_2009]: https://doi.org/10.1007/978-3-540-85181-3_69
[research_murray_steelant_2009]: https://doi.org/10.2514/6.2009-7399
[research_murray_tinney_2014]: https://doi.org/10.21236/ada603766
[research_mursenkova_ivanov_2022]: https://doi.org/10.3390/en15062189
[research_mursenkova_ivanov_2023]: https://doi.org/10.1134/s1063780x22601468
[research_mursenkova_liao_2021]: https://doi.org/10.26583/sv.13.3.05
[research_murty_chakraborty_2011]: https://doi.org/10.1260/1759-3107.2.1.15
[research_murugan_govardhan_2016]: https://doi.org/10.1017/jfm.2016.574
[research_muruganandam_hemchandra_2026]: https://doi.org/10.2514/6.2026-2341
[research_murugesan_chakravarthy_2018]: https://doi.org/10.2514/6.2018-4959
[research_murzionak]: https://doi.org/10.22215/etd/2013-06868
[research_musa_huang_2022]: https://doi.org/10.1016/j.actaastro.2022.09.001
[research_musa_huang_2024]: https://doi.org/10.1063/5.0239660
[research_musa_huang_2025]: https://doi.org/10.2514/6.2025-0753
[research_musa_weixuan_2018]: https://doi.org/10.1016/j.actaastro.2018.04.055
[research_musal_1962]: https://doi.org/10.21236/ad0294472
[research_musal_hm_1964]: https://doi.org/10.21236/ad0449823
[research_musielak_musielak_1997]: https://doi.org/10.2514/6.1997-3268
[research_muslubas_eyi_2015]: https://doi.org/10.2514/6.2015-2458
[research_muss_johnson_2003]: https://doi.org/10.21236/ada416416
[research_myong_1999]: https://doi.org/10.2514/6.1999-3578
[research_myrabo_2004]: https://doi.org/10.1063/1.1721031
[research_myrabo_head_1995]: https://doi.org/10.2514/6.1995-2575
[research_myrabo_nagamatsu_1991]: https://doi.org/10.2514/6.1991-2547
[research_mysko_chyu_1993]: https://doi.org/10.2514/6.1993-3057
[research_nadler_2003]: https://doi.org/10.21236/ada420247
[research_naftel_wilhite_1986]: https://doi.org/10.2514/6.1986-195
[research_nagamatsu_1989]: https://doi.org/10.2514/6.1989-3
[research_nagamatsu_sheer_1961]: https://doi.org/10.21236/ad0600345
[research_nagamatsu_workman_1960]: https://doi.org/10.2514/8.5173
[research_nagao_yoshida_2019]: https://doi.org/10.2322/astj.jsass-d-18-00007
[research_nagarajankirupakaran_kv_2023]: https://doi.org/10.2514/6.2023-3090
[research_nagdewe_shevare_2006]: https://doi.org/10.2514/6.2006-8088
[research_nagel_becker_1973]: https://doi.org/10.2514/6.1973-58
[research_nagendrababu_jayakrishna_2018]: https://doi.org/10.1016/j.matpr.2017.11.474
[research_nair_kumar_2003]: https://doi.org/10.2514/6.2003-7067
[research_nair_kumar_2005]: https://doi.org/10.2514/1.2839
[research_nair_s_2020]: https://doi.org/10.1002/er.5257
[research_nair_suryan_2022]: https://doi.org/10.1016/j.ijhydene.2022.08.061
[research_nair_suryan_2023]: https://doi.org/10.1063/5.0151676
[research_najafiyazdi_2005]: https://doi.org/10.2514/6.2005-4827
[research_najafiyazdi_2005_b]: https://doi.org/10.2514/6.2005-510
[research_nakagawa_kuwahara_1992]: https://doi.org/10.2514/6.1992-3727
[research_nakamori_nakamura_1995]: https://doi.org/10.2514/6.1995-1732
[research_nakaya_hikichi_2015]: https://doi.org/10.1016/j.proci.2014.07.023
[research_nakayama_edanaga_2018]: https://doi.org/10.2514/6.2018-4452
[research_nalabala_dinda_2024]: https://doi.org/10.1016/j.energy.2023.129993
[research_namatsaliuk_donato_2025]: https://doi.org/10.2514/6.2025-3827
[research_namkoung_hong_2012]: https://doi.org/10.5139/ijass.2012.13.3.296
[research_nance_2013]: https://doi.org/10.21236/ada571259
[research_nangia_2011]: https://doi.org/10.21236/ada548732
[research_narayan_1994]: https://doi.org/10.2514/6.1994-2948
[research_narayan_kumar_1989]: https://doi.org/10.2514/6.1989-30
[research_nardo_sadler_1962]: https://doi.org/10.21236/ad0273837
[research_nardozzo_popkin_2019]: https://doi.org/10.2514/6.2019-3838
[research_nasa_glenn_2002]: https://doi.org/10.2514/5.9781600866678.0427.0439
[research_natan_1987]: https://doi.org/10.2514/6.1987-2034
[research_natan_gany_1989]: https://doi.org/10.2514/6.1989-2886
[research_naumann_ende_1993]: https://doi.org/10.1007/978-94-011-1828-6_28
[research_navalordnancesystemscommandwashingtondc_1957]: https://doi.org/10.21236/ada278207
[research_navier_stokes_equations_2018]: https://doi.org/10.1201/9780203737972-2
[research_nayal_lamb_2020]: https://doi.org/10.1088/1757-899x/814/1/012018
[research_nbo2_crystal]: https://doi.org/10.1007/10681735_369
[research_neaves_mcrae_1995]: https://doi.org/10.1115/imece1995-0407
[research_neaves_mcrae_2001]: https://doi.org/10.2514/6.2001-825
[research_neely_tjong_2008]: https://doi.org/10.2514/6.2008-2664
[research_neely_tracy_2006]: https://doi.org/10.2514/6.2006-8000
[research_negishi_daimon_2015]: https://doi.org/10.2514/6.2015-3760
[research_neitzke_rudnik_2005]: https://doi.org/10.2514/6.2005-3704
[research_nelson_1967]: https://doi.org/10.2172/4363750
[research_nestler_1970]: https://doi.org/10.1615/ihtc4.2330
[research_neumann_1993]: https://doi.org/10.1007/978-94-011-1828-6_38
[research_neumann_2005]: https://doi.org/10.3320/1.2758668
[research_neumann_patterson_1978]: https://doi.org/10.2514/6.1978-37
[research_neuwerth_peiter_1998]: https://doi.org/10.2514/6.1998-1578
[research_neuwerth_peiter_1999]: https://doi.org/10.2514/2.3441
[research_new_generation_hypersonic_2002]: https://doi.org/10.2514/5.9781600866678.0585.0619
[research_newberry_dresser_1988]: https://doi.org/10.2514/6.1988-479
[research_newell_zakharov_2007]: https://doi.org/10.21236/ada479049
[research_newman_fulcher_1992]: https://doi.org/10.2514/6.1992-2722
[research_newnham_2004]: https://doi.org/10.1093/oso/9780198520757.003.0013
[research_ng_dressler_2002]: https://doi.org/10.21236/ada408719
[research_ngo]: https://doi.org/10.14264/uql.2017.193
[research_ngoclong_2016]: https://doi.org/10.11648/j.ijmea.20160405.14
[research_nguyen_massa_2023]: https://doi.org/10.2514/6.2023-1728
[research_nguyen_massa_2023_b]: https://doi.org/10.2514/6.2023-1728.c1
[research_nguyen_massa_2024]: https://doi.org/10.2514/6.2024-1903
[research_nguyen_reinartz_2011]: https://doi.org/10.2514/6.2011-2256
[research_nguyen_vo_2024]: https://doi.org/10.1080/00102202.2024.2323573
[research_nguyenbui_duffa_2004]: https://doi.org/10.2514/6.2004-2339
[research_nicholasjdigregorio_thomaskwestiv]: https://ntrs.nasa.gov/citations/20220006204
[research_nichols_denny_2011]: https://doi.org/10.2514/6.2011-5970
[research_nichols_heikkinen_2010]: https://doi.org/10.2514/6.2010-1720
[research_nichols_mcdaniel_2015]: https://doi.org/10.2514/6.2015-0043
[research_nickerson_dunn_1988]: https://doi.org/10.2514/6.1988-3161
[research_nicolaetudosie_2018]: https://doi.org/10.1109/iccairo.2018.00010
[research_nicolaides_brady_1959]: https://doi.org/10.21236/ad0219843
[research_nicoll_1962]: https://doi.org/10.21236/ada952020
[research_nicolosi_melone_2026]: https://doi.org/10.2514/6.2026-1384
[research_nie_li_2019]: https://doi.org/10.3850/978-981-11-2730-4_0155-cd
[research_nie_liu_2013]: https://doi.org/10.4028/www.scientific.net/amm.291-294.1636
[research_nietubicz_1975]: https://doi.org/10.21236/ada009704
[research_niewohner_2018]: https://doi.org/10.5162/ettc2018/6.2
[research_nikaido_hobson_2025]: https://doi.org/10.2514/6.2025-0335
[research_ning]: https://doi.org/10.22215/etd/2026-17071
[research_ning_1981]: https://doi.org/10.1016/s0082-0784(81)80195-6
[research_nishida_2011]: https://doi.org/10.1007/978-3-642-17884-9_86
[research_nishiguchi_kodera_2025]: https://doi.org/10.3390/aerospace12010066
[research_nishimura_2014]: https://doi.org/10.5359/jawe.39.333
[research_nishino_1993]: https://doi.org/10.2514/6.1993-3440
[research_nishio_1996]: https://doi.org/10.2514/6.1996-2392
[research_nishio_hagiwara_1998]: https://doi.org/10.2514/6.1998-1620
[research_niu_chen_2018]: https://doi.org/10.1007/s11071-018-4127-z
[research_niu_chen_2024]: https://doi.org/10.1016/j.actaastro.2024.09.001
[research_niu_chen_2025]: https://doi.org/10.1007/s44270-025-00024-8
[research_niu_piao_2016]: https://doi.org/10.2514/6.2016-3959
[research_niu_wang_2023]: https://doi.org/10.21203/rs.3.rs-2333969/v1
[research_niu_yuan_2017]: https://doi.org/10.1016/j.ast.2017.10.026
[research_nixon_henderson_1966]: https://doi.org/10.1021/i360017a018
[research_nnenna_matthew_2026]: https://doi.org/10.30574/gjeta.2026.28.2.0230
[research_noda_1988]: https://doi.org/10.1080/01495738808961926
[research_noftz_jewell_2025]: https://doi.org/10.2514/6.2025-3620
[research_nompelis_bender_2011]: https://doi.org/10.2514/6.2011-3547
[research_nompelis_drayna_2005]: https://doi.org/10.2514/6.2005-4867
[research_nompelis_drayna_2006]: https://doi.org/10.1016/b978-044452206-1/50047-1
[research_nompelis_wan_2007]: https://doi.org/10.2514/6.2007-4334
[research_non_empirical_analytical_2019]: https://doi.org/10.1088/2053-2563/aae894ch17
[research_nondestructive_evaluation_2014]: https://doi.org/10.1201/b16545-12
[research_nonequilibrium_stagnation_1975]: https://doi.org/10.2514/5.9781600865138.0415.0435
[research_noori_karimian_2008]: https://doi.org/10.1080/10618560802216297
[research_noraml_and_1986]: https://doi.org/10.2514/5.9781600861871.0049.0068
[research_nordinbates_fureby_2015]: https://doi.org/10.2514/6.2015-3838
[research_nordinbates_fureby_2017]: https://doi.org/10.1016/j.proci.2016.07.118
[research_noren_2008]: https://doi.org/10.21236/ada495427
[research_norfleet_loper_1966]: https://doi.org/10.21236/ad0633656
[research_norimatsu_katsumura_2026]: https://doi.org/10.1016/j.actaastro.2026.02.022
[research_norimatsu_katsumura_2026_b]: https://doi.org/10.1299/jtst.25-00382
[research_normal_and_1986]: https://doi.org/10.2514/5.9781600861871.0423.0424
[research_norris_2006]: https://doi.org/10.2514/6.2006-2815
[research_north_1983]: https://doi.org/10.2514/6.1983-1559
[research_northam_anderson_1986]: https://doi.org/10.2514/6.1986-159
[research_northam_lempert_1988]: https://doi.org/10.2514/6.1988-3293
[research_northamericanaviationinclosangelesca_1964]: https://doi.org/10.21236/ad0607252
[research_northamgb_1985]: https://ntrs.nasa.gov/citations/19860018775
[research_novelli_koschel_2001]: https://doi.org/10.2514/6.2001-1870
[research_numerical_analysis_of_2015]: https://doi.org/10.20535/2219-380412201551164
[research_numerical_modeling_1991]: https://doi.org/10.2514/5.9781600866081.0057.0081
[research_numerical_research_2008]: https://doi.org/10.2514/6.2008-4708
[research_numerical_simulation_2015]: https://doi.org/10.4028/www.scientific.net/amm.766-767.1044
[research_numerical_simulations_2006]: https://doi.org/10.1142/9789812707130_0005
[research_nursal_khalid_2022]: https://doi.org/10.2139/ssrn.4046429
[research_nusca_1989]: https://doi.org/10.2514/6.1989-2797
[research_nydick_friedmann_1995]: https://doi.org/10.2514/6.1995-1485
[research_oamjee_sadanandan_2020]: https://doi.org/10.1063/5.0026125
[research_oamjee_sadanandan_2020_b]: https://doi.org/10.1080/00102202.2020.1801657
[research_oba_gonda_2014]: https://doi.org/10.1115/gt2014-26809
[research_obikane_1984]: https://doi.org/10.2514/6.1984-1364
[research_obituary_of_2008]: https://doi.org/10.1063/pt.4.1974
[research_oblique_shock_1983]: https://doi.org/10.2514/5.9781600865602.0022.0040
[research_oblique_shock_2000]: https://doi.org/10.1201/9781420036596.axc
[research_oblique_shock_2013]: https://doi.org/10.1201/b15414-11
[research_oblique_shock_2015]: https://doi.org/10.1201/b19392-38
[research_oblique_shock_2019]: https://doi.org/10.1002/9781119500377.ch4
[research_oblique_shock_chart_2017]: https://doi.org/10.1017/9781316014288.018
[research_obrien_lewis_2000]: https://doi.org/10.2514/6.2000-3823
[research_obrien_lewis_2001]: https://doi.org/10.2514/6.2001-1919
[research_obyrne_gai_2014]: https://doi.org/10.21236/ada614176
[research_obyrne_stotz_2005]: https://doi.org/10.2514/6.2005-3357
[research_obyrne_wittig_2011]: https://doi.org/10.21236/ada544361
[research_ocheltree_1993]: https://doi.org/10.1007/978-94-011-1828-6_49
[research_ochi_2004]: https://doi.org/10.1111/j.1934-6093.2004.tb00211.x
[research_odabas_sarigulklijn_1992]: https://doi.org/10.2514/6.1992-5018
[research_ogawa_babinsky_2008]: https://doi.org/10.2514/6.2008-599
[research_ogawa_boyce_2013]: https://doi.org/10.2514/6.2013-115
[research_ogawa_grainger_2009]: https://doi.org/10.2514/6.2009-7401
[research_ogawa_grainger_2010]: https://doi.org/10.2514/1.48284
[research_ognjanovic_maksimovic_2017]: https://doi.org/10.2298/tsci160919318o
[research_oka_hidema_2015]: https://doi.org/10.1115/ajkfluids2015-18556
[research_okamoto_yamamoto_2002]: https://doi.org/10.2514/6.2002-5193
[research_okojie_danehy_2009]: https://doi.org/10.2514/6.2009-7279
[research_okuno_watanabe_1992]: https://doi.org/10.2514/6.1992-4302
[research_olfe_1964]: https://doi.org/10.2514/6.1964-69
[research_olguin_2019]: https://doi.org/10.2172/1630998
[research_oliveirajunior_marinho_2021]: https://doi.org/10.26678/abcm.cobem2021.cob2021-0818
[research_olivier_vetter_1993]: https://doi.org/10.1007/978-94-011-1828-6_42
[research_olivon_durand_2024]: https://doi.org/10.2514/6.2024-3114
[research_olivon_genot_2026]: https://doi.org/10.2514/6.2026-3437
[research_olsen_1965]: https://doi.org/10.21236/ad0626928
[research_ombrello_carter_2015]: https://doi.org/10.1016/j.proci.2014.07.068
[research_on_ascent_1994]: https://doi.org/10.1016/0967-0661(94)91057-x
[research_oneal_desilva_2026]: https://doi.org/10.2514/6.2026-4592
[research_oneill_lewis_1992]: https://doi.org/10.2514/3.56866
[research_oneill_lewis_1993]: https://doi.org/10.2514/3.46438
[research_ootao_ishihara_2012]: https://doi.org/10.1080/01495739.2012.674781
[research_ootao_ishihara_2013]: https://doi.org/10.12989/sem.2013.47.3.421
[research_ootao_tanigawa_2005]: https://doi.org/10.12989/sem.2005.20.5.559
[research_opalka_1968]: https://doi.org/10.21236/ad0393552
[research_oppenheimer_doman]: https://doi.org/10.1109/aero.2006.1655985
[research_oppenheimer_doman_2006]: https://doi.org/10.2514/6.2006-6637
[research_oppenheimer_doman_2008]: https://doi.org/10.2514/6.2008-6382
[research_oppenheimer_skujins_2007]: https://doi.org/10.2514/6.2007-6396
[research_oppenheimer_skujins_2008]: https://doi.org/10.2514/6.2008-6383
[research_optimal_aerodynamic_1996]: https://doi.org/10.2514/5.9781600866401.0017.0049
[research_optimization_design_2023]: https://doi.org/10.1063/5.0149490
[research_optimization_of_2005]: https://doi.org/10.1109/phycon.2005.1514002
[research_orlik_fedioun_2009]: https://doi.org/10.2514/6.2009-7352
[research_orlik_fedioun_2011]: https://doi.org/10.2514/1.51570
[research_orlin_orlov_2019]: https://doi.org/10.18698/2308-6033-2019-11-1935
[research_ormsbee_1962]: https://doi.org/10.21236/ad0295993
[research_ororke_cuppoletti_2024]: https://doi.org/10.2514/6.2024-0114
[research_ortloff_1968]: https://doi.org/10.21236/ad0830727
[research_ortwerth_goldman_1996]: https://doi.org/10.2514/6.1996-3039
[research_osgerby_smithson_1969]: https://doi.org/10.21236/ad0692466
[research_osgerby_smithson_1969_b]: https://doi.org/10.2514/6.1969-827
[research_ossmann_luspay_2019]: https://doi.org/10.1109/aero.2019.8741853
[research_oster_2010]: https://doi.org/10.21236/ada546852
[research_osun_james_2026]: https://doi.org/10.2514/6.2026-5040
[research_oswald_demargne_1995]: https://doi.org/10.2514/6.1995-2271
[research_otte_welch_1963]: https://doi.org/10.21236/ad0410258
[research_ou_xiong_2024]: https://doi.org/10.1007/s12650-024-01004-x
[research_ouzi_jinsheng_2011]: https://doi.org/10.1016/j.egypro.2011.12.497
[research_ouzts_2008]: https://doi.org/10.2514/6.2008-2621
[research_ouzts_lorenzo_1992]: https://doi.org/10.2514/6.1992-3320
[research_ouztspeterj_lorenzocarlf_1993]: https://ntrs.nasa.gov/citations/19930015890
[research_oveissi_goel_2024]: https://doi.org/10.2514/6.2024-0743
[research_owen_owen_2007]: https://doi.org/10.1109/iciasf.2007.4380898
[research_owotunse_ogwumike_2023]: https://doi.org/10.1109/swc57546.2023.10448888
[research_ozawa_hanai_2008]: https://doi.org/10.2514/6.2008-2671
[research_ozawa_suzuki_2014]: https://doi.org/10.1063/1.4902739
[research_pace_massa_2022]: https://doi.org/10.2514/6.2022-3996
[research_padmapriya_reddy_1998]: https://doi.org/10.2514/6.1998-2627
[research_pagan_benoit_2001]: https://doi.org/10.2514/6.2001-3293
[research_pagel_warmbold_1968]: https://doi.org/10.2514/6.1968-1091
[research_pagel_warmbold_1969]: https://doi.org/10.2514/3.44088
[research_pal_roy_2024]: https://doi.org/10.1063/5.0225469
[research_palej_palacz_2018]: https://doi.org/10.2478/tar-2018-0024
[research_palmer]: https://doi.org/10.14264/bd53932
[research_palmer_2020]: https://doi.org/10.2514/6.2020-0116
[research_palmer_venkatapathy_1993]: https://doi.org/10.2514/6.1993-2861
[research_palomero]: https://doi.org/10.11606/003273223
[research_palomino_2022]: https://doi.org/10.5162/ettc2022/2.4
[research_palumbo_palmer_2022]: https://doi.org/10.2514/6.2022-2481
[research_pamadi_hotchko_2006]: https://doi.org/10.2514/6.2006-8033
[research_pamadi_tartabini_2004]: https://doi.org/10.2514/6.2004-876
[research_pamadi_tartabini_2009]: https://doi.org/10.2514/6.2009-5842
[research_pan_tian_2009]: https://doi.org/10.2514/6.2009-7370
[research_pande_1994]: https://doi.org/10.21236/ada413742
[research_pandey_sivasakthivel_2011]: https://doi.org/10.7763/ijesd.2011.v2.105
[research_pandey_sivasakthivel_2011_b]: https://doi.org/10.7763/ijet.2011.v3.268
[research_pane]: https://doi.org/10.14264/c671a2a
[research_panfilov_sevchenko_2021]: https://doi.org/10.34759/trd-2021-118-03
[research_papa_stoliker_1988]: https://doi.org/10.2514/6.1988-2105
[research_paper_board]: https://doi.org/10.3403/30408899u
[research_papinczak]: https://doi.org/10.14264/uql.2017.262
[research_paquette_palko_2004]: https://doi.org/10.2514/6.2004-3888
[research_paredes_choudhari_2017]: https://doi.org/10.1103/physrevfluids.2.053903
[research_parise_1992]: https://doi.org/10.2514/6.1992-202
[research_park_1996]: https://doi.org/10.1007/978-94-009-0267-1_44
[research_park_busch_2017]: https://doi.org/10.1177/1468087417728630
[research_park_jeon_2024]: https://doi.org/10.2139/ssrn.4801252
[research_parker_2022]: https://doi.org/10.21236/ad1180064
[research_parmar_jp_2026]: https://doi.org/10.1016/j.ast.2026.112964
[research_parsons_armstrong_2023]: https://doi.org/10.1063/12.0020357
[research_parsons_richmond_1969]: https://doi.org/10.2514/6.1969-84
[research_parthasarathy_cinibulk_2014]: https://doi.org/10.1002/9781118700853.ch11
[research_parton_2018]: https://doi.org/10.1201/9780203737972
[research_pasha_vadivelan_2012]: https://doi.org/10.1007/978-3-642-25685-1_72
[research_pashai_hurst_2022]: https://doi.org/10.1109/aero53065.2022.9843722
[research_patel_chudoba_2026]: https://doi.org/10.1108/aeat-01-2025-0015
[research_patra_lee_2018]: https://doi.org/10.1021/acsanm.8b00781
[research_paul_binner_2014]: https://doi.org/10.1002/9781118700853.ch7
[research_paull_1999]: https://doi.org/10.2514/6.1999-2450
[research_paull_stalker_1995]: https://doi.org/10.1017/s0022112095002096
[research_paus_well_1996]: https://doi.org/10.2514/6.1996-3901
[research_pavlova_shtern_2011]: https://doi.org/10.1134/s0018151x1103014x
[research_pawlak_1994]: https://doi.org/10.2514/6.1994-2116
[research_payne_mcconnell_2004]: https://doi.org/10.2514/6.2004-5050
[research_paynter_1994]: https://doi.org/10.2514/6.1994-465
[research_paynter_chen_1983]: https://doi.org/10.2514/6.1983-1371
[research_peake]: https://doi.org/10.22215/etd/1975-00296
[research_pei_hou_2014]: https://doi.org/10.1016/j.actaastro.2014.09.009
[research_pein_vinnemeier_1989]: https://doi.org/10.2514/6.1989-2885
[research_pelevin_ponomarev_2018]: https://doi.org/10.3103/s1068799818010117
[research_pelevin_ponomarev_2021]: https://doi.org/10.33950/spacetech-2308-7625-2020-4-65-77
[research_pellett_bruno_2002]: https://doi.org/10.2514/6.2002-3880
[research_pendergast_mollendorf_2008]: https://doi.org/10.21236/ada482231
[research_peng_2023]: https://doi.org/10.1016/j.csite.2023.103620
[research_peng_chen_2026]: https://doi.org/10.1016/j.ast.2026.112119
[research_peng_feng_2019]: https://doi.org/10.1109/access.2019.2923014
[research_peng_peng_2014]: https://doi.org/10.1109/cgncc.2014.7007351
[research_peng_qi_2019]: https://doi.org/10.1109/ccdc.2019.8832538
[research_peng_smith_1996]: https://doi.org/10.2514/6.1996-1208
[research_peng_xu_2024]: https://doi.org/10.1088/1742-6596/2882/1/012097
[research_peng_zhong_2022]: https://doi.org/10.1016/j.fuel.2022.125547
[research_penland_romeo_1971]: https://doi.org/10.2514/6.1971-132
[research_perchonok_1960]: https://doi.org/10.1016/b978-1-4831-9626-8.50018-0
[research_performance_analysis_1999]: https://doi.org/10.1016/s0140-6701(99)92452-9
[research_peri_armani_2024]: https://doi.org/10.52202/078371-0205
[research_perlini_bertolini_2026]: https://doi.org/10.2514/6.2026-5058
[research_perminov_1969]: https://doi.org/10.1007/bf01032472
[research_perrier_rapuc_1996]: https://doi.org/10.2514/6.1996-4548
[research_perrier_rostand_1994]: https://doi.org/10.2514/6.1994-3090
[research_perrier_rostand_1995]: https://doi.org/10.2514/6.1995-6100
[research_perrot_hadjadj_2005]: https://doi.org/10.2514/6.2005-4309
[research_persh_1955]: https://doi.org/10.21236/ad0075320
[research_persova_soloveichik_2017]: https://doi.org/10.1016/j.actaastro.2017.02.021
[research_peters_phares_1976]: https://doi.org/10.21236/ada030015
[research_petersen_1981]: https://doi.org/10.2514/6.1981-2417
[research_peterson_2019]: https://doi.org/10.2514/6.2019-0448
[research_peterson_hassan_2017]: https://doi.org/10.2514/6.2017-0339
[research_peterson_hassan_2018]: https://doi.org/10.2514/6.2018-1144
[research_pethasethuraman_kim_2020]: https://doi.org/10.1177/0954410020967537
[research_pethasethuraman_yang_2023]: https://doi.org/10.1063/5.0137481
[research_petley_dziedzic_1993]: https://doi.org/10.2514/6.1993-1984
[research_petley_jones_1990]: https://doi.org/10.2514/6.1990-3284
[research_petley_jones_1992]: https://doi.org/10.2514/3.46173
[research_petrie_1965]: https://doi.org/10.21236/ad0621574
[research_petrov_clyndyuck_1998]: https://doi.org/10.1068/htec59
[research_pettinari_corradini_2012]: https://doi.org/10.1109/acc.2012.6315223
[research_pezzella_marini_2014]: https://doi.org/10.2514/6.2014-2844
[research_pfaff_1965]: https://doi.org/10.21236/ad0467448
[research_pfaff_1968]: https://doi.org/10.21236/ad0832104
[research_phillips_cruz_1991]: https://doi.org/10.2514/6.1991-1694
[research_phillips_cruz_1993]: https://doi.org/10.2514/6.1993-3443
[research_piao_zhang_2019]: https://doi.org/10.1177/1077546319849775
[research_piccirillo_viola_2023]: https://doi.org/10.2514/6.2023-3098
[research_pichler_2023]: https://doi.org/10.31224/3206
[research_pietlahanier_serre_2017]: https://doi.org/10.2514/6.2017-2197
[research_pike_2006]: https://doi.org/10.1017/s0001924000001287
[research_piller]: https://doi.org/10.1007/3-540-31801-1_140
[research_pingli_wanchunchen_2010]: https://doi.org/10.1109/icmet.2010.5598391
[research_pinheiromaia_souza_2020]: https://doi.org/10.26678/abcm.encit2020.cit20-0230
[research_pinto_whyman_2023]: https://doi.org/10.1049/rsn2.12432
[research_pionessa_kinzel_2024]: https://doi.org/10.2514/6.2024-1971
[research_pionessa_kinzel_2024_b]: https://doi.org/10.2514/6.2024-1971.c1
[research_pipko_1966]: https://doi.org/10.21236/ad0646293
[research_pisano_whitfield_2024]: https://doi.org/10.2514/6.2024-2330
[research_piscitelli_cutrone_2017]: https://doi.org/10.1016/j.actaastro.2017.03.007
[research_piscopo_depaepe_2024]: https://doi.org/10.1016/j.rineng.2024.102834
[research_pitman]: https://doi.org/10.14264/300087
[research_platou_1959]: https://doi.org/10.21236/ad0212064
[research_platou_1968]: https://doi.org/10.2514/6.1968-388
[research_platt_hanner_1965]: https://doi.org/10.2172/1068247
[research_platz_bounajem_1992]: https://doi.org/10.2514/6.1992-4071
[research_poggie_2006]: https://doi.org/10.2514/6.2006-1007
[research_poggie_2008]: https://doi.org/10.2514/6.2008-1090
[research_polivanov_sidorenko_2010]: https://doi.org/10.1007/s00193-010-0286-7
[research_polivanov_sidorenko_2016]: https://doi.org/10.1063/1.4963993
[research_pollock_brutsche_2015]: https://doi.org/10.21236/ada622103
[research_pollock_moran_2023]: https://doi.org/10.31224/3008
[research_pollock_wild_2024]: https://doi.org/10.31224/3817
[research_polsgrove_adams_2002]: https://doi.org/10.2514/6.2002-4233
[research_polsgrove_adams_2002_b]: https://doi.org/10.2514/6.2002-2199
[research_pope_maydew_1959]: https://doi.org/10.2172/4233184
[research_popinski_2019]: https://doi.org/10.1615/ihtc3.1880
[research_poplavskaya_2002]: https://doi.org/10.1023/a:1015203206949
[research_porro_hingst_1993]: https://doi.org/10.2514/6.1993-775
[research_porter_1965]: https://doi.org/10.1016/b978-0-08-011074-5.50011-7
[research_porter_poggie_2017]: https://doi.org/10.2514/6.2017-0533
[research_portis_dambrosio_2024]: https://doi.org/10.52202/078369-0104
[research_potapkin_moskvichev_2008]: https://doi.org/10.1134/s0869864308030165
[research_potturi_edwards_2013]: https://doi.org/10.2514/6.2013-2461
[research_poulain_pietlahanie_2009]: https://doi.org/10.2514/6.2009-7290
[research_povinelli_1991]: https://doi.org/10.1007/978-3-642-84580-2_11
[research_povitsky_miller_2021]: https://doi.org/10.2514/6.2021-1311
[research_powers_1960]: https://doi.org/10.1016/b978-0-12-395519-7.50008-2
[research_powers_robinson_1992]: https://doi.org/10.2514/6.1992-3334
[research_powers_zaretzky_1986]: https://doi.org/10.2514/6.1986-1761
[research_pozefsky_1989]: https://doi.org/10.2514/6.1989-1103
[research_prabhu_1995]: https://doi.org/10.1007/bf02744410
[research_prabhudk_tannehilljc_1984]: https://ntrs.nasa.gov/citations/19840056580
[research_prakash_g_2024]: https://doi.org/10.2139/ssrn.4757510
[research_prakash_parsons_2010]: https://doi.org/10.2514/6.2010-4997
[research_prakash_singh_2021]: https://doi.org/10.2514/6.2021-3271
[research_pratt_1971]: https://doi.org/10.21236/ad0723961
[research_pratt_heiser_1993]: https://doi.org/10.2514/6.1993-358
[research_preliminary_design_1983]: https://doi.org/10.2514/5.9781600865626.0385.0415
[research_preliminary_thermal_structural_1992]: https://doi.org/10.2514/5.9781600866128.0301.0322
[research_preller]: https://doi.org/10.14264/uql.2018.437
[research_preller_smart_2012]: https://doi.org/10.2514/6.2012-5825
[research_pressures_and_2000]: https://doi.org/10.1016/b978-012257060-5/50023-x
[research_price]: https://doi.org/10.1109/stherm.2003.1194383
[research_primary_flight]: https://doi.org/10.4271/air4922
[research_principles_of_2002]: https://doi.org/10.2514/5.9781600866678.0017.0027
[research_priyamvada_singh_2015]: https://doi.org/10.2514/6.2015-3678
[research_priyankaagrawal_amitkumarsingh_2026]: https://ntrs.nasa.gov/citations/20250010365
[research_probstein_1953]: https://doi.org/10.21236/ad0009822
[research_prokesch_duran_2024]: https://doi.org/10.1016/j.actaastro.2024.08.036
[research_properties_of_2014]: https://doi.org/10.2514/5.9781624102547.0625.0632
[research_properties_of_2024]: https://doi.org/10.2514/5.9781624107252.0695.0702
[research_pruett_chang_1998]: https://doi.org/10.1007/s001620050080
[research_pruitt_bates_1992]: https://doi.org/10.2514/6.1992-5091
[research_pu_huang_2017]: https://doi.org/10.2514/6.2017-2415
[research_pulok_chakravarty_2020]: https://doi.org/10.1115/imece2020-23663
[research_pulsonetti]: https://doi.org/10.14264/uql.2018.537
[research_qi_bao_2015]: https://doi.org/10.1016/j.jfranklin.2015.08.020
[research_qi_jianliang_2017]: https://doi.org/10.2514/6.2017-1248
[research_qi_wang_1998]: https://doi.org/10.2514/2.5353
[research_qian_nan_2016]: https://doi.org/10.1109/aus.2016.7748157
[research_qian_sun_2013]: https://doi.org/10.1109/icca.2013.6564958
[research_qiao_liu_2024]: https://doi.org/10.1016/j.energy.2024.130906
[research_qiao_ma_2025]: https://doi.org/10.1016/j.ast.2025.109941
[research_qiaoyongjie_liujinrong_2011]: https://doi.org/10.1109/cie-radar.2011.6159904
[research_qifan_huijun_2014]: https://doi.org/10.2514/6.2014-3847
[research_qin_agarwal_2019]: https://doi.org/10.1016/j.combustflame.2019.08.038
[research_qin_bao_2008]: https://doi.org/10.2514/6.2008-5178
[research_qin_bao_2012]: https://doi.org/10.2514/1.t3820
[research_qin_chang_2015]: https://doi.org/10.2514/1.j053547
[research_qin_huang_2026]: https://doi.org/10.1016/j.ast.2025.111044
[research_qin_zhang_2013]: https://doi.org/10.1016/j.fuel.2012.10.077
[research_qin_zhu_2013]: https://doi.org/10.2991/iccnce.2013.8
[research_qinchangmao_qinaiming_2010]: https://doi.org/10.1109/cmce.2010.5610285
[research_qiu_jia_2016]: https://doi.org/10.1177/0954410016649208
[research_qiu_zhang_2017]: https://doi.org/10.2514/6.2017-2381
[research_qiu_zhang_2021]: https://doi.org/10.1016/j.ast.2020.106376
[research_qu_kong_2019]: https://doi.org/10.1007/s11433-018-9347-6
[research_quadros_bernardini_2018]: https://doi.org/10.2514/1.j056650
[research_quan_chang_2024]: https://doi.org/10.1016/j.applthermaleng.2023.121527
[research_quick_king_2005]: https://doi.org/10.2514/6.2005-3709
[research_quinlan]: https://doi.org/10.18130/v3g26m
[research_quinlanjesser_mcdanieljamesc_2014]: https://ntrs.nasa.gov/citations/20150001235
[research_quinn_1978]: https://doi.org/10.2514/6.1978-44
[research_quinnrobertd_gongleslie_1990]: https://ntrs.nasa.gov/citations/19900019499
[research_rabadan_weigand_2013]: https://doi.org/10.1051/eucass/201304373
[research_rabadanov_ataev_2002]: https://doi.org/10.1134/1.1481919
[research_rabadansantana_weigand_2012]: https://doi.org/10.2514/6.2012-5926
[research_radiation_properties_2018]: https://doi.org/10.1201/9780203737972-13
[research_radiative_heat_2018]: https://doi.org/10.1201/9780203737972-15
[research_radiatively_driven_1994]: https://doi.org/10.2514/6.1994-2472
[research_rafla_2019]: https://doi.org/10.2514/6.2019-3132
[research_rafla_2019_b]: https://doi.org/10.2514/6.2019-3132.c1
[research_raghunandan_ruffin_2016]: https://doi.org/10.2514/6.2016-4314
[research_raghunathan_mcadam_1983]: https://doi.org/10.2514/3.8251
[research_raghuram_ramesh_2021]: https://doi.org/10.1007/s00348-021-03233-4
[research_ragnoli_savino_2024]: https://doi.org/10.2139/ssrn.4687892
[research_rahimi_svolos_2026]: https://doi.org/10.1016/j.engfracmech.2025.111794
[research_rahman_joy_2017]: https://doi.org/10.1063/1.4984732
[research_raj_1987]: https://doi.org/10.21236/ada182904
[research_rajamanohar_kurian_1996]: https://doi.org/10.2514/3.24046
[research_rajan_1970]: https://doi.org/10.21236/ad0706850
[research_ram_kim_2019]: https://doi.org/10.3850/978-981-11-2730-4_0435-cd
[research_ramakrishnan_singh_1993]: https://doi.org/10.2514/6.1993-355
[research_ramalingam_mahefkey_2003]: https://doi.org/10.1115/imece2003-55055
[research_ramanujachari_2022]: https://doi.org/10.1201/9781003049005-8
[research_ramasubramanian_starkey_2008]: https://doi.org/10.2514/6.2008-7497
[research_ramaswami_velmurugan_2019]: https://doi.org/10.3139/120.111314
[research_ramaty_spiegler_1982]: https://doi.org/10.1016/s0082-0784(82)80228-2
[research_ramjet_supersonic_1958]: https://doi.org/10.1016/0016-0032(58)90466-6
[research_ramprakash_muruganandam_2016]: https://doi.org/10.1109/icmae.2016.7549585
[research_ramunno_boyd_2021]: https://doi.org/10.2514/6.2021-2440
[research_ramunno_boyd_2022]: https://doi.org/10.2514/1.b38573
[research_rana_thornber_2011]: https://doi.org/10.2514/6.2011-506
[research_rana_thornber_2013]: https://doi.org/10.1080/19942060.2013.11015451
[research_ranard_davison_1961]: https://doi.org/10.4271/610097
[research_raney_mcminn_1993]: https://doi.org/10.2514/6.1993-1367
[research_rao_1974]: https://doi.org/10.1063/1.2945925
[research_rao_siddharth_2023]: https://doi.org/10.1063/5.0127034
[research_raskydanielj_tranhuyk_1998]: https://ntrs.nasa.gov/citations/20020064967
[research_rasmussen_1978]: https://doi.org/10.21236/ada068003
[research_rasmussen_dhanuka_2007]: https://doi.org/10.1016/j.proci.2006.08.007
[research_rasmussen_driscoll_2005]: https://doi.org/10.1016/j.proci.2004.08.185
[research_rasmussen_stevens_1987]: https://doi.org/10.2514/6.1987-2550
[research_rataczak_chaudhry_2024]: https://doi.org/10.2514/1.a35764
[research_rataczak_mcmahon_2023]: https://doi.org/10.2514/6.2023-1172
[research_ratchford_redding_2025]: https://doi.org/10.1063/5.0299691
[research_rathakrishnan_2025]: https://doi.org/10.1002/9781394285662
[research_raubenheimer_elgar_2012]: https://doi.org/10.21236/ada572952
[research_rauh_reimer_2026]: https://doi.org/10.2514/6.2026-5085
[research_rault_1992]: https://doi.org/10.2514/6.1992-306
[research_rault_1992_b]: https://doi.org/10.1007/978-3-642-77922-0_72
[research_ravichandran_doherty_2023]: https://doi.org/10.2514/6.2023-0437
[research_ravichandran_doherty_2023_b]: https://doi.org/10.2514/6.2023-0437.c1
[research_ravindran_bricalli_2019]: https://doi.org/10.1016/j.actaastro.2019.06.010
[research_razzaqi_smart_2009]: https://doi.org/10.2514/6.2009-7429
[research_reardon_schetz_2021]: https://doi.org/10.2514/1.b38214
[research_reba_1964]: https://doi.org/10.21236/ad0444094
[research_reba_christian_1963]: https://doi.org/10.21236/ad0297092
[research_reda_1977]: https://doi.org/10.21236/ada054591
[research_reddecliff_weber_1998]: https://doi.org/10.2514/6.1998-1613
[research_reddy_smith_1989]: https://doi.org/10.2514/6.1989-4
[research_rediess_melton_1994]: https://doi.org/10.2514/6.1994-2172
[research_reed_1997]: https://doi.org/10.21236/ada329724
[research_reed_2013]: https://doi.org/10.2514/6.2013-2556
[research_regan_1964]: https://doi.org/10.21236/ad0600975
[research_reghu_j_2025]: https://doi.org/10.2514/6.2025-0471
[research_rehman_fidan_2009]: https://doi.org/10.2514/6.2009-7291
[research_rehman_petersen_2010]: https://doi.org/10.1109/cdc.2010.5717754
[research_reimer_dimartino_2023]: https://doi.org/10.2514/6.2023-3089
[research_reimer_dimartino_2025]: https://doi.org/10.2514/6.2025-1342
[research_reimer_dimartino_2026]: https://doi.org/10.2514/6.2026-5141
[research_reklis_conti_1984]: https://doi.org/10.2514/6.1984-1579
[research_relangi_ingenito_2021]: https://doi.org/10.3390/en14092626
[research_relangi_ingenito_2023]: https://doi.org/10.1063/5.0128132
[research_rempt_1981]: https://doi.org/10.2514/6.1981-2479
[research_ren_2009]: https://doi.org/10.2514/6.2009-7321
[research_ren_fu_2017]: https://doi.org/10.1177/1687814017703900
[research_ren_wu_2023]: https://doi.org/10.1109/taes.2023.3322977
[research_ren_yang_2017]: https://doi.org/10.1177/1729881416686953
[research_report_no_1935]: https://doi.org/10.1016/s0016-0032(35)90062-x
[research_resch_hedlund_1992]: https://doi.org/10.2514/6.1992-2757
[research_research_instrumentation_1974]: https://doi.org/10.2514/5.9781600865077.0019.0039
[research_research_progress_2026]: https://doi.org/10.3901/jme.260073
[research_researchandtechnologyorganisationrto_2005]: https://ntrs.nasa.gov/citations/20060010486
[research_reshotko_1987]: https://doi.org/10.21236/ada185764
[research_response_of_1974]: https://doi.org/10.2514/5.9781600865077.0003.0018
[research_reubush_1999]: https://doi.org/10.2514/6.1999-4818
[research_reubush_martin_2001]: https://doi.org/10.2514/6.2001-1802
[research_review_of_1986]: https://doi.org/10.2514/5.9781600865763.0481.0502
[research_reviznikov_sposobin_2018]: https://doi.org/10.1134/s0018151x18050218
[research_reynolds_1977]: https://doi.org/10.21236/ada054856
[research_rhea_moore_1988]: https://doi.org/10.2514/6.1988-2087
[research_rhisat_molki_2024]: https://doi.org/10.1115/imece2024-144718
[research_rhudy_hiers_1960]: https://doi.org/10.21236/ad0221626
[research_riabov_1994]: https://doi.org/10.2514/6.1994-2478
[research_riabov_2002]: https://doi.org/10.2514/6.2002-3298
[research_riabov_2003]: https://doi.org/10.1063/1.1581586
[research_riabov_2011]: https://doi.org/10.1063/1.3562828
[research_riabov_botin_1999]: https://doi.org/10.2514/6.1999-3207
[research_riabov_riabov_1997]: https://doi.org/10.2514/6.1997-2226
[research_ricciardi_1991]: https://doi.org/10.2514/6.1991-1920
[research_ricciardi_minwalla_2016]: https://doi.org/10.2514/6.2016-1435
[research_rice]: https://doi.org/10.18130/v38v6p
[research_rice_goyne_2014]: https://doi.org/10.2514/6.2014-0986
[research_rice_hazlwood_1994]: https://doi.org/10.2514/6.1994-2166
[research_rice_heidelberg_1980]: https://doi.org/10.2514/6.1980-100
[research_rich_mellor_1995]: https://doi.org/10.1115/95-gt-067
[research_richards_1979]: https://doi.org/10.21236/ada088129
[research_richardson_herrmann_1966]: https://doi.org/10.21236/ada023213
[research_richey_stava_1968]: https://doi.org/10.4271/680288
[research_richey_surber_1983]: https://doi.org/10.2514/6.1983-84
[research_riedelbauch_brenner_1989]: https://doi.org/10.2514/6.1989-1840
[research_riedelbauch_brenner_1990]: https://doi.org/10.2514/6.1990-1492
[research_rigamonti_shoesmith_2026]: https://doi.org/10.2514/6.2026-2743
[research_rigamonti_vicocantero_2026]: https://doi.org/10.2514/6.2026-5031
[research_riggins_2004]: https://doi.org/10.2514/1.4980
[research_riggins_mcclinton_1992]: https://doi.org/10.2514/6.1992-5097
[research_riggins_tackett_2006]: https://doi.org/10.2514/6.2006-8059
[research_righi_2015]: https://doi.org/10.2514/6.2015-3341
[research_riis_piscopo_2024]: https://doi.org/10.2139/ssrn.4887318
[research_riley_dejarnette_1992]: https://doi.org/10.2514/6.1992-499
[research_riley_gaitonde_2015]: https://doi.org/10.2514/6.2015-4206
[research_riley_hagenmaier_2016]: https://doi.org/10.2514/6.2016-1901
[research_riley_hagenmaier_2017]: https://doi.org/10.2514/6.2017-0554
[research_risha_2000]: https://doi.org/10.2514/6.2000-618
[research_rizk_1993]: https://doi.org/10.1016/0013-7944(93)90274-v
[research_rizvi_linshu_2017]: https://doi.org/10.1017/aer.2017.11
[research_rizzetta_1991]: https://doi.org/10.2514/6.1991-128
[research_rizzetta_1994]: https://doi.org/10.2514/6.1994-2304
[research_rizzetta_1996]: https://doi.org/10.2514/6.1996-39
[research_rizzetta_garmann_2022]: https://doi.org/10.1080/10618562.2022.2087873
[research_rizzetta_garmann_2023]: https://doi.org/10.1080/10618562.2023.2246391
[research_rizzetta_visbal_2004]: https://doi.org/10.1080/10618560310001614926
[research_roach_caldarella_1996]: https://doi.org/10.21236/ada354038
[research_roberts_1988]: https://doi.org/10.2514/6.1988-2077
[research_roberts_1988_b]: https://doi.org/10.2514/6.1988-2113
[research_roberts_brown_1988]: https://doi.org/10.2514/6.1988-2083
[research_roberts_shawler_1994]: https://doi.org/10.2514/6.1994-2181
[research_robertson_hartfield_1992]: https://doi.org/10.2514/6.1992-4076
[research_robinson_mcdougal_2000]: https://doi.org/10.21236/ada453171
[research_roccidenis_brandstetter_2003]: https://doi.org/10.2514/6.2003-7048
[research_rockwell_goyne_2010]: https://doi.org/10.2514/6.2010-1126
[research_rockwell_goyne_2023]: https://doi.org/10.2514/1.b38827
[research_rodi_2012]: https://doi.org/10.2514/6.2012-3223
[research_rodi_2012_b]: https://doi.org/10.2514/6.2012-3222
[research_rodi_2018]: https://doi.org/10.2514/6.2018-3817
[research_rodi_2020]: https://doi.org/10.2514/6.2020-2423
[research_rodighiero]: https://doi.org/10.14264/5b16d36
[research_rodriguez_2007]: https://doi.org/10.2514/6.2007-1048
[research_rodriguezcg_rigginsdw_2000]: https://ntrs.nasa.gov/citations/20000034102
[research_rodriguezfuentes_parent_2022]: https://doi.org/10.2514/6.2022-3442
[research_rodriguezsegade_hernandez_2020]: https://doi.org/10.2514/6.2020-1107
[research_roga_2019]: https://doi.org/10.1088/1742-6596/1276/1/012041
[research_roga_2019_b]: https://doi.org/10.1088/1742-6596/1276/1/012038
[research_roga_2023]: https://doi.org/10.21203/rs.3.rs-3606519/v1
[research_rogers_kaplan_1963]: https://doi.org/10.21236/ad0410519
[research_rogersdc_scottro_1976]: https://ntrs.nasa.gov/citations/19770053840
[research_rogersrclayton_capriottidiegop_1998]: https://ntrs.nasa.gov/citations/20040090464
[research_rogg_bricalli_2020]: https://doi.org/10.2514/6.2020-2436
[research_rohl_cowling_1965]: https://doi.org/10.21236/ad0620170
[research_roland_rumpfkeil_2017]: https://doi.org/10.2514/1.c033958
[research_rom_1965]: https://doi.org/10.21236/ad0617943
[research_rong_2017]: https://doi.org/10.12783/dtetr/apetc2017/11122
[research_rong_wei_2016]: https://doi.org/10.1051/matecconf/20166104008
[research_rooker_1970]: https://doi.org/10.2514/6.1970-376
[research_roos_pudsey_2020]: https://doi.org/10.1016/j.actaastro.2020.08.022
[research_rose_teare_1964]: https://doi.org/10.1016/b978-1-4831-9828-6.50027-8
[research_rose_thoma_2009]: https://doi.org/10.21236/ada498289
[research_roseberry_2025]: https://doi.org/10.12968/s1478-2774(25)50035-2
[research_rosner_cibrian_1974]: https://doi.org/10.2514/6.1974-755
[research_ross_1960]: https://doi.org/10.21236/ad0286077
[research_ross_law_1993]: https://doi.org/10.2514/6.1993-4385
[research_rotating_detonation_2023]: https://doi.org/10.1063/5.0157988
[research_roth_mavris_1999]: https://doi.org/10.21236/ada396843
[research_rothschild_schuster_1999]: https://doi.org/10.2514/6.1999-2380
[research_rotta_1966]: https://doi.org/10.21236/ad0645668
[research_roudakov_semenov_1996]: https://doi.org/10.2514/6.1996-4572
[research_roudakov_semenov_1998]: https://doi.org/10.2514/6.1998-1643
[research_rouel_richards_1975]: https://doi.org/10.21236/ada004102
[research_rouel_richards_1975_b]: https://doi.org/10.21236/ada012550
[research_roundy_1979]: https://doi.org/10.21236/ada078529
[research_rowan]: https://doi.org/10.14264/106385
[research_rowan_paull_2005]: https://doi.org/10.2514/6.2005-615
[research_rowan_paull_2006]: https://doi.org/10.2514/1.18744
[research_rowangollan]: https://doi.org/10.14264/178818
[research_rowley_thornton_1994]: https://doi.org/10.2514/6.1994-1593
[research_roy_2008]: https://doi.org/10.21236/ada502748
[research_roy_wang_2011]: https://doi.org/10.21236/ada564235
[research_ruan]: https://doi.org/10.70675/ed3621b3z6047z4a96za7b7z57b7e30c7453
[research_ruan_domingo_2020]: https://doi.org/10.1016/j.combustflame.2020.01.034
[research_rubey_1985]: https://doi.org/10.21236/ada162660
[research_rubey_1985_b]: https://doi.org/10.21236/ada156154
[research_rubins_rhode_1963]: https://doi.org/10.2514/6.1963-117
[research_ruble_1964]: https://doi.org/10.2514/6.1964-291
[research_rudiments_and_2001]: https://doi.org/10.2514/5.9781600866609.0939.0978
[research_rued_mark_1991]: https://doi.org/10.2514/6.1991-2493
[research_ruhnke_will_1965]: https://doi.org/10.21236/ad0630889
[research_ruimin_jianguo_2018]: https://doi.org/10.1109/iccre.2018.8376433
[research_ruoling_jin_2012]: https://doi.org/10.2514/6.2012-5957
[research_rwayneguy_1990]: https://ntrs.nasa.gov/citations/19910013840
[research_sabean_lewis_1999]: https://doi.org/10.2514/6.1999-612
[research_sabelnikov_vlasenko_2017]: https://doi.org/10.1007/978-981-10-7410-3_20
[research_sabry_hussin_2026]: https://doi.org/10.1016/j.ijthermalsci.2026.110810
[research_sacher_zellner_1995]: https://doi.org/10.2514/6.1995-6014
[research_sachs_bayer_1991]: https://doi.org/10.2514/6.1991-5074
[research_sachs_heller_1996]: https://doi.org/10.2514/6.1996-3728
[research_sachs_schoder_1995]: https://doi.org/10.2514/6.1995-6061
[research_sacks_1996]: https://doi.org/10.21236/ada316511
[research_saheby_huang_2015]: https://doi.org/10.2514/6.2015-3618
[research_saheby_huang_2017]: https://doi.org/10.2514/6.2017-2177
[research_sahu_1986]: https://doi.org/10.21236/ada171462
[research_sahu_2007]: https://doi.org/10.21236/ada471736
[research_sahu_vasile_2024]: https://doi.org/10.2514/6.2024-4338
[research_sahut_nilsson_2024]: https://doi.org/10.2514/6.2024-0580
[research_saida_1986]: https://doi.org/10.1007/978-3-642-82770-9_20
[research_sainagabharghava_krishnatmali_2024]: https://doi.org/10.1016/j.ijheatfluidflow.2024.109413
[research_saito_1965]: https://doi.org/10.1246/bcsj.38.2008
[research_saito_ono_2004]: https://doi.org/10.2514/6.2004-2174
[research_saito_ono_2005]: https://doi.org/10.2514/6.2005-3821
[research_salloum_candon_2018]: https://doi.org/10.2514/6.2018-0886
[research_salloum_candon_2018_b]: https://doi.org/10.2514/6.2018-0886.c1
[research_salooja_1968]: https://doi.org/10.1016/0010-2180(68)90051-5
[research_salvador_myrabo_2009]: https://doi.org/10.2514/6.2009-4873
[research_salvador_myrabo_2013]: https://doi.org/10.2514/1.b34598
[research_samimy_webb_2011]: https://doi.org/10.21236/ada564713
[research_samtaney_pullin_1998]: https://doi.org/10.1007/s001930050122
[research_sanaka_kandula_2023]: https://doi.org/10.1515/tjeng-2023-0029
[research_sandeep_2023]: https://doi.org/10.5772/intechopen.107840
[research_sandersbobbyw_weirloisj_1999]: https://ntrs.nasa.gov/citations/20000012394
[research_sandersbobbyw_weirloisj_2008]: https://ntrs.nasa.gov/citations/20080030791
[research_sanderson_1965]: https://doi.org/10.1016/b978-0-08-011074-5.50017-8
[research_sanderson_1987]: https://doi.org/10.1016/b978-0-408-01234-8.50010-3
[research_sanderson_2003]: https://doi.org/10.1016/b978-075067123-1/50033-8
[research_sanderson_2010]: https://doi.org/10.1016/b978-0-7506-8308-1.00040-1
[research_sandham_2026]: https://doi.org/10.1016/b978-0-44-318785-8.00017-1
[research_sandoz_blanc_2024]: https://doi.org/10.5162/ettc2024/b7.6
[research_sandoz_klaeyle_2021]: https://doi.org/10.1109/icort52730.2021.9581417
[research_sankar_kelkar_1995]: https://doi.org/10.21236/ada319913
[research_sankaran_venkatesh_2023]: https://doi.org/10.1007/978-981-19-6270-7_8
[research_sanmartin_plewacki_2025]: https://doi.org/10.2514/6.2025-1464
[research_sanmartin_plewacki_2025_b]: https://doi.org/10.2514/6.2025-1464.c1
[research_santhy_sivakumar_2022]: https://doi.org/10.2139/ssrn.4226387
[research_santos_2008]: https://doi.org/10.2514/6.2008-1183
[research_santos_2011]: https://doi.org/10.2514/6.2011-2321
[research_santos_2012]: https://doi.org/10.2514/6.2012-5802
[research_santos_borgesribeiro_2025]: https://doi.org/10.26678/abcm.cobem2023.cob2023-0400
[research_santos_hosder_2020]: https://doi.org/10.2514/6.2020-2724
[research_santos_lewis_2003]: https://doi.org/10.2514/6.2003-3894
[research_sapunkov_1966]: https://doi.org/10.1007/bf01016280
[research_saqib_linshu_2007]: https://doi.org/10.2514/6.2007-853
[research_saranathan_grant_2016]: https://doi.org/10.2514/6.2016-3245
[research_sardeshmukh_andersonlmatthewe_2014]: https://doi.org/10.21236/ada613690
[research_sargent_bielawski_1970]: https://doi.org/10.21236/ad0871448
[research_saric_2012]: https://doi.org/10.21236/ada563785
[research_sarosh_2021]: https://doi.org/10.20935/al2998
[research_sarosh_yunfeng_2012]: https://doi.org/10.4028/www.scientific.net/amm.245.277
[research_sarout_paramasivam_2020]: https://doi.org/10.2514/6.2020-2440
[research_sarout_r_2020]: https://doi.org/10.2514/6.2020-0650
[research_sathiyamoorthy_danish_2018]: https://doi.org/10.1016/j.actaastro.2018.05.014
[research_sato_fukui_2019]: https://doi.org/10.2514/6.2019-0678
[research_sato_izumikawa_1997]: https://doi.org/10.2514/6.1997-3021
[research_sato_matsuo_2006]: https://doi.org/10.2514/1.9514
[research_savelkin_yarantsev_2015]: https://doi.org/10.1016/j.combustflame.2014.08.012
[research_savino_fumo_2004]: https://doi.org/10.1557/proc-851-nn11.5
[research_savino_pezzella_2003]: https://doi.org/10.1002/fld.602
[research_sawai_sato_2003]: https://doi.org/10.2514/6.2003-7027
[research_sawley_wuthrich_1995]: https://doi.org/10.1080/10618569508904520
[research_sayapin_1966]: https://doi.org/10.1007/bf01022283
[research_sayir_2006]: https://doi.org/10.21236/ada589651
[research_sayir_sehirlioglu_2009]: https://doi.org/10.21236/ada583233
[research_scaggs_1966]: https://doi.org/10.21236/ad0648906
[research_scaggs_burggraf_1963]: https://doi.org/10.21236/ad0427751
[research_scaggs_neumann_1992]: https://doi.org/10.2514/6.1992-4012
[research_scala_1962]: https://doi.org/10.21236/ad0294982
[research_scala_nolan_1960]: https://doi.org/10.1016/b978-1-4832-2885-3.50007-6
[research_schaber_schwab_1991]: https://doi.org/10.2514/6.1991-2492
[research_schaupp_friedrich_2010]: https://doi.org/10.1080/10618562.2010.533121
[research_scherding]: https://doi.org/10.70675/147c27c8z3847z4b40za466zf27b21ee23db
[research_scherding_rigas_2024]: https://doi.org/10.2139/ssrn.4714073
[research_schettino_borrelli_1998]: https://doi.org/10.2514/6.1998-1509
[research_schetz_billig_1980]: https://doi.org/10.2514/6.1980-1256
[research_schetz_billig_1982]: https://doi.org/10.2514/3.51187
[research_schiavazzi_juliano_2020]: https://doi.org/10.2514/6.2020-1652
[research_schindel_1989]: https://doi.org/10.2514/6.1989-379
[research_schindel_1991]: https://doi.org/10.2514/6.1991-202
[research_schindel_1999]: https://doi.org/10.2514/6.1999-883
[research_schindel_2005]: https://doi.org/10.2514/6.2005-7613
[research_schioppa_taywochong_2025]: https://doi.org/10.1115/gt2025-152020
[research_schmatz_1989]: https://doi.org/10.2514/6.1989-2183
[research_schmidt_1988]: https://doi.org/10.21236/ada196136
[research_schmidt_plostins_1983]: https://doi.org/10.21236/ada130011
[research_schmidt_velapoldi_1999]: https://doi.org/10.2514/6.1999-4122
[research_schneider_2000]: https://doi.org/10.2172/759452
[research_schneider_2006]: https://doi.org/10.21236/ada448081
[research_schneider_2009]: https://doi.org/10.21236/ada500049
[research_schneider_dreizler_2003]: https://doi.org/10.1016/s0010-2180(03)00150-0
[research_schneider_gerlinger]: https://doi.org/10.1007/3-540-26589-9_22
[research_schneider_matsumura_2003]: https://doi.org/10.2514/6.2003-1130
[research_schneider_myers_1979]: https://doi.org/10.21236/ada080749
[research_schneider_reed_2003]: https://doi.org/10.21236/ada413763
[research_schnelle_hoffels_1992]: https://doi.org/10.1007/978-94-011-2462-1_12
[research_schoeler_1978]: https://doi.org/10.2514/6.1978-777
[research_schram_narayanaswamy_2026]: https://doi.org/10.1007/s00348-026-04215-0
[research_schram_stramecky_2025]: https://doi.org/10.2514/1.j064532
[research_schuch_laquer_1952]: https://doi.org/10.2172/4405871
[research_schuelein_2014]: https://doi.org/10.2514/6.2014-3332
[research_schueler_1963]: https://doi.org/10.21236/ad0299290
[research_schulmeister_hostetler_1977]: https://doi.org/10.21236/ada050698
[research_schulteroedding_olivier_1998]: https://doi.org/10.2514/6.1998-1528
[research_schunk_chung_2000]: https://doi.org/10.2514/6.2000-3467
[research_schwanekamp_2014]: https://doi.org/10.2514/6.2014-2372
[research_schwartzentruber_boyd_2013]: https://doi.org/10.2514/6.2013-2613
[research_schwartzentruber_tadmor_2012]: https://doi.org/10.21236/ada567529
[research_schweikhard_1983]: https://doi.org/10.2514/6.1983-2715
[research_schwelkart_hallion_1997]: https://doi.org/10.21236/ada441126
[research_sciencecommunicationincmcleanva_1960]: https://doi.org/10.21236/ad0243886
[research_scigliano_desimone_2020]: https://doi.org/10.2514/6.2020-2422
[research_scott_1968]: https://doi.org/10.21236/ad0668682
[research_scotti_martin_1988]: https://doi.org/10.2514/6.1988-2265
[research_scramjet_combustion_2022]: https://doi.org/10.1016/c2021-0-02204-5
[research_scramjet_combustor_2022]: https://doi.org/10.1002/9781119640646.ch5
[research_scramjet_engine_2001]: https://doi.org/10.2514/5.9781600866609.0159.0222
[research_scramjet_inlet_forebody_2022]: https://doi.org/10.1002/9781119640646.ch4
[research_scribben_withrow_2006]: https://doi.org/10.21236/ada463634
[research_scuderi_1978]: https://doi.org/10.2514/6.1978-162
[research_scuderi_orton_1998]: https://doi.org/10.2514/6.1998-1584
[research_seabergh_king_2001]: https://doi.org/10.21236/ada397931
[research_seal_between_2011]: https://doi.org/10.1016/s1350-4789(11)70393-2
[research_seal_for_2019]: https://doi.org/10.1016/s1350-4789(19)30158-8
[research_seckin_yuceil_2013]: https://doi.org/10.1051/epjconf/20134501099
[research_sedlock_1985]: https://doi.org/10.21236/ada153767
[research_seebaughwr_1973]: https://ntrs.nasa.gov/citations/19730034387
[research_segal_2009]: https://doi.org/10.1017/cbo9780511627019
[research_segal_2010]: https://doi.org/10.1002/9780470686652.eae098
[research_segal_2010_b]: https://doi.org/10.1002/9780470686652.eae547
[research_segal_2011]: https://doi.org/10.2514/6.2011-2278
[research_segal_owens_1997]: https://doi.org/10.2514/6.1997-2888
[research_segal_thakur_2005]: https://doi.org/10.2514/6.2005-3391
[research_segura_2007]: https://doi.org/10.21236/ada474770
[research_sekar_vaidyanathan_2025]: https://doi.org/10.1080/00102202.2025.2491102
[research_self_starting_simulation_2020]: https://doi.org/10.36884/jafm.13.06.31389
[research_sellers_hunerwadel_1977]: https://doi.org/10.21236/ada055773
[research_semenov_romankov_1998]: https://doi.org/10.2514/6.1998-1514
[research_sepahiyounsi_2025]: https://doi.org/10.1016/j.ast.2025.110346
[research_sepahiyounsi_esmaeili_2023]: https://doi.org/10.1016/j.ast.2023.108334
[research_serrani_bolender_2014]: https://doi.org/10.1109/acc.2014.6858885
[research_serre_2009]: https://doi.org/10.2514/6.2009-7358
[research_serre_denis_2011]: https://doi.org/10.2514/6.2011-2264
[research_serre_falempin_2001]: https://doi.org/10.2514/6.2001-1871
[research_serre_falempin_2008]: https://doi.org/10.2514/6.2008-2651
[research_seshadri_1990]: https://doi.org/10.21236/ada230709
[research_seshadri_2008]: https://doi.org/10.21236/ada501168
[research_sethi_2025]: https://doi.org/10.14293/pr2199.001888.v1
[research_settles_dodson_1994]: https://doi.org/10.2514/3.12205
[research_sevigny_heckman_1972]: https://doi.org/10.21236/ad0759158
[research_seymour_2009]: https://doi.org/10.21236/ada540165
[research_sforza_1967]: https://doi.org/10.21236/ad0653875
[research_sforza_2017]: https://doi.org/10.1016/b978-0-12-809326-9.00005-1
[research_sforza_2017_b]: https://doi.org/10.1016/b978-0-12-809326-9.00006-3
[research_sforza_2017_c]: https://doi.org/10.1016/b978-0-12-809326-9.00004-x
[research_sforza_2017_d]: https://doi.org/10.1016/b978-0-12-809326-9.00009-9
[research_shachar_benasher_2025]: https://doi.org/10.2514/1.g008439
[research_shahrokhi_davisjr_1995]: https://doi.org/10.2514/6.1995-301
[research_shaikh_patidar_2017]: https://doi.org/10.1016/j.applthermaleng.2016.08.222
[research_shajahan_gugulothu_2025]: https://doi.org/10.1016/j.ijhydene.2025.150342
[research_shakiba_serrani_2011]: https://doi.org/10.2514/6.2011-6227
[research_shang]: https://doi.org/10.14264/e478e68
[research_shang_2005]: https://doi.org/10.1142/9789812703187_0016
[research_shang_2008]: https://doi.org/10.2514/6.2008-722
[research_shang_2008_b]: https://doi.org/10.4208/cicp.2008.v4.p838
[research_shang_2009]: https://doi.org/10.1007/978-3-540-92779-2_115
[research_shang_2009_b]: https://doi.org/10.2514/6.2009-4051
[research_shang_chang_2007]: https://doi.org/10.2514/6.2007-3885
[research_shang_chang_2007_b]: https://doi.org/10.2514/1.26086
[research_shang_hankeyjr_1976]: https://doi.org/10.2514/6.1976-95
[research_shang_menart_2006]: https://doi.org/10.2514/6.2006-764
[research_shang_surzhikov_2011]: https://doi.org/10.2514/6.2011-2258
[research_shanmugam_sunpark_2024]: https://doi.org/10.1016/j.applthermaleng.2023.121451
[research_shantz_1953]: https://doi.org/10.21236/ad0037850
[research_shaohua_xu_2017]: https://doi.org/10.1177/0954410017708213
[research_sharma_eswaran_2022]: https://doi.org/10.1016/j.ast.2022.107900
[research_sharma_ghia_2020]: https://doi.org/10.1115/fedsm2020-20165
[research_sharma_shenvi_2025]: https://doi.org/10.13182/t133-48927
[research_sharma_shenvi_2026]: https://doi.org/10.12688/nuclscitechnolopenres.17734.1
[research_sharovmk_2022]: https://doi.org/10.21883/pss.2022.07.54581.073
[research_sheffer_dulikravich_1993]: https://doi.org/10.2514/6.1993-39
[research_shen_dongliang_2025]: https://doi.org/10.2139/ssrn.5717181
[research_shen_huang_2020]: https://doi.org/10.1016/j.ast.2020.105779
[research_shen_huang_2021]: https://doi.org/10.1016/j.csite.2021.101104
[research_shen_yu_2014]: https://doi.org/10.4028/www.scientific.net/amm.716-717.1624
[research_sheng_lu_2021]: https://doi.org/10.1109/icmae52228.2021.9522459
[research_shepard_feleo_2021]: https://doi.org/10.2514/6.2021-3676
[research_shepheard_1965]: https://doi.org/10.21236/ad0630924
[research_sheth_ungar_2012]: https://doi.org/10.2514/6.2012-3497
[research_shetty_cardenas_2025]: https://doi.org/10.1016/j.combustflame.2025.114408
[research_shevelev_2018]: https://doi.org/10.5772/intechopen.71666
[research_shi_2016]: https://doi.org/10.2514/6.2016-4874
[research_shi_chang_2010]: https://doi.org/10.1243/09544100jaero687
[research_shi_dai_2015]: https://doi.org/10.2514/6.2015-3553
[research_shi_feng_2020]: https://doi.org/10.23919/ccc50068.2020.9189333
[research_shi_niu_2023]: https://doi.org/10.1109/yac59482.2023.10401454
[research_shi_song_2017]: https://doi.org/10.1515/tjj-2015-0058
[research_shi_song_2017_b]: https://doi.org/10.2514/6.2017-2189
[research_shi_tsai_1994]: https://doi.org/10.2514/6.1994-1822
[research_shi_zha_2021]: https://doi.org/10.1016/j.jeurceramsoc.2021.03.015
[research_shi_zhou_2012]: https://doi.org/10.1007/978-3-642-34381-0_29
[research_shields_1981]: https://doi.org/10.2514/6.1981-2351
[research_shih_zwan_1988]: https://doi.org/10.2514/6.1988-2739
[research_shikman_vinogradov_2001]: https://doi.org/10.2514/6.2001-1787
[research_shilnikov_elizarova_2018]: https://doi.org/10.1615/hightempmatproc.2018024713
[research_shimura_sakuranaka_1996]: https://doi.org/10.2514/6.1996-3242
[research_shinde_gaitonde_2022]: https://doi.org/10.2514/6.2022-1975
[research_shirai_hashimoto_2014]: https://doi.org/10.1016/j.ssi.2013.12.042
[research_shirasu_south_1996]: https://doi.org/10.2514/6.1996-3109
[research_shklovskii_kurt_1961]: https://doi.org/10.1007/978-1-4899-5929-4_8
[research_shneider_macheret_2004]: https://doi.org/10.2514/6.2004-2662
[research_shock_tunnel_2012]: https://doi.org/10.2514/6.2012-5901
[research_shock_wave_boundary]: https://doi.org/10.1007/0-387-26305-5_10
[research_shock_waves]: https://doi.org/10.1007/3-540-28563-6_6
[research_shope_1975]: https://doi.org/10.21236/ada018653
[research_shope_2006]: https://doi.org/10.2514/6.2006-3665
[research_shorenstein_1971]: https://doi.org/10.21236/ad0731696
[research_short_1961]: https://doi.org/10.21236/ad0261073
[research_shou_li_2026]: https://doi.org/10.1109/aetcse69203.2026.11504439
[research_shovlin_1978]: https://doi.org/10.2514/6.1978-959
[research_shreeve_lord_1961]: https://doi.org/10.21236/ad0611132
[research_shuai_daqian_2022]: https://doi.org/10.1109/docs55193.2022.9967480
[research_shubhankarbhaktaetal_2018]: https://doi.org/10.24247/ijmperdapr2018102
[research_shucheng_xijun_1994]: https://doi.org/10.21236/ada289590
[research_shuguang_yangwang_2015]: https://doi.org/10.1109/chicc.2015.7260118
[research_shumway_2000]: https://doi.org/10.21236/ada390641
[research_shupingtan_zhibinli_2010]: https://doi.org/10.1109/ccdc.2010.5498526
[research_shvets_voronin_2005]: https://doi.org/10.2514/6.2005-512
[research_shvydkyi_2023]: https://doi.org/10.22541/au.169589352.24446904/v1
[research_si_huang_2019]: https://doi.org/10.1063/1.5098543
[research_siaka_zhang_2022]: https://doi.org/10.1115/fedsm2022-87027
[research_sicard_grill_2008]: https://doi.org/10.2514/6.2008-2622
[research_sicard_raepsaet_2006]: https://doi.org/10.2514/6.2006-7974
[research_siddiqi_abraham_1988]: https://doi.org/10.2514/6.1988-2170
[research_sidharth_dwivedi_2026]: https://doi.org/10.2514/6.2026-1149
[research_sidharth_dwivedi_2026_b]: https://doi.org/10.2514/6.2026-4301
[research_siebenhaar_bogar_2006]: https://doi.org/10.2514/6.2006-7986
[research_siebenhaar_chen_1999]: https://doi.org/10.2514/6.1999-4909
[research_silvamarquessoares_paulobatistadearaujo_2021]: https://doi.org/10.26678/abcm.cobem2021.cob2021-0495
[research_silver_brooks_2024]: https://doi.org/10.2514/6.2024-0351
[research_silvester_morgan_2004]: https://doi.org/10.2514/6.2004-3848
[research_simeonides]: https://doi.org/10.12681/eadd/28688
[research_simmons_1989]: https://doi.org/10.2514/6.1989-457
[research_simmons_2000]: https://doi.org/10.21236/ada397435
[research_simmons_meritt_2022]: https://doi.org/10.2514/6.2022-3582
[research_simmons_nelson_1989]: https://doi.org/10.2514/6.1989-2535
[research_simmons_nelson_1992]: https://doi.org/10.2514/6.1992-3994
[research_simmons_nelson_1995]: https://doi.org/10.2514/6.1995-2720
[research_simon_savage_1975]: https://doi.org/10.4050/vfs-f31-036
[research_simone_bruno_2009]: https://doi.org/10.2514/6.2009-813
[research_simone_bruno_2010]: https://doi.org/10.2322/tastj.8.pa_47
[research_simons_1975]: https://doi.org/10.21236/ada019517
[research_sims_1963]: https://doi.org/10.21236/ad0334868
[research_sims_hahn_1964]: https://doi.org/10.21236/ad0603567
[research_simsont_gerlinger_2012]: https://doi.org/10.1007/978-3-642-33374-3_15
[research_simulation_in_1988]: https://doi.org/10.2514/6.1988-2130
[research_singer_1956]: https://doi.org/10.1016/0083-6656(56)90015-0
[research_singh_babu_2018]: https://doi.org/10.1615/ihmtc-2017.3240
[research_singh_g_2023]: https://doi.org/10.2514/6.2023-3012
[research_singh_gahlot_2023]: https://doi.org/10.1109/iccmso59960.2023.00043
[research_singh_prakash_2023]: https://doi.org/10.5937/fme2302221s
[research_singh_rajagopal_2026]: https://doi.org/10.1063/5.0347530
[research_singh_sharma_2025]: https://doi.org/10.2514/6.2025-2486
[research_singh_tiwari_1989]: https://doi.org/10.2514/6.1989-2184
[research_singh_tiwari_1990]: https://doi.org/10.2514/6.1990-529
[research_sippel_2006]: https://doi.org/10.2514/6.2006-7976
[research_siqueira_rosa_2019]: https://doi.org/10.26678/abcm.cobem2019.cob2019-0116
[research_sislian_dudebout_2000]: https://doi.org/10.2514/2.5529
[research_sitaraman_yellapantula_2021]: https://doi.org/10.1016/j.combustflame.2021.111531
[research_situ_sun_1999]: https://doi.org/10.2514/6.1999-2245
[research_situ_wang_2001]: https://doi.org/10.2514/6.2001-523
[research_situ_wang_2002]: https://doi.org/10.2514/6.2002-804
[research_sivells_1963]: https://doi.org/10.21236/ad0299774
[research_sivells_1969]: https://doi.org/10.2514/6.1969-337
[research_sivells_payne_1959]: https://doi.org/10.21236/ad0208774
[research_skews_1994]: https://doi.org/10.1007/bf01417430
[research_skinner_johnston_1953]: https://doi.org/10.21236/ad0004340
[research_skujins_cesnik_2010]: https://doi.org/10.2514/6.2010-8127
[research_skujins_cesnik_2011]: https://doi.org/10.2514/6.2011-2341
[research_slater_2016]: https://doi.org/10.2514/6.2016-0530
[research_slater_saunders_2009]: https://doi.org/10.2514/6.2009-7349
[research_slaterjohnw_gruberchristopherr_2005]: https://ntrs.nasa.gov/citations/20050216399
[research_slavick_hiremath_2023]: https://doi.org/10.2514/6.2023-0013
[research_sliusariev_bilotserkovsky_2024]: https://doi.org/10.15421/472408
[research_slutsky_williams_1969]: https://doi.org/10.21236/ad0855766
[research_smaardyk_1954]: https://doi.org/10.2172/4393986
[research_smalley_wharton_1977]: https://doi.org/10.21236/ada045167
[research_smarslok_2015]: https://doi.org/10.21236/ada615850
[research_smart_1999]: https://doi.org/10.2514/6.1999-85
[research_smart_hass_2006]: https://doi.org/10.2514/1.20661
[research_smart_kalkhoran_1995]: https://doi.org/10.2514/6.1995-98
[research_smart_kalkhoran_1995_b]: https://doi.org/10.2514/3.12958
[research_smart_kalkhoran_1998]: https://doi.org/10.1007/s001930050117
[research_smart_tetlow_2006]: https://doi.org/10.2514/6.2006-8019
[research_smayda]: https://doi.org/10.18130/v3dr44
[research_smayda_goyne_2011]: https://doi.org/10.2514/6.2011-2324
[research_smeets_quenett_1997]: https://doi.org/10.1007/978-94-011-5432-1_14
[research_smeltzer_sorensen_1972]: https://doi.org/10.2514/6.1972-45
[research_smiley_camberos_2024]: https://doi.org/10.2514/6.2024-0167
[research_smirnov_2019]: https://doi.org/10.38013/2542-0542-2019-1-18-23
[research_smith_1953]: https://doi.org/10.21236/ad0007625
[research_smith_2011]: https://doi.org/10.2514/6.2011-2280
[research_smith_2021]: https://doi.org/10.1063/pt.3.4888
[research_smith_baxter]: https://doi.org/10.1109/iciasf.1989.77663
[research_smith_bergmann_2004]: https://doi.org/10.2514/6.2004-6819
[research_smith_bowcutt_2011]: https://doi.org/10.2514/6.2011-2275
[research_smith_carver_1993]: https://doi.org/10.2514/6.1993-2782
[research_smith_chase_1976]: https://doi.org/10.2514/6.1976-772
[research_smith_farokhi_2015]: https://doi.org/10.2514/6.2015-1108
[research_smith_farokhi_2015_b]: https://doi.org/10.2514/6.2015-4140
[research_smith_farokhi_2015_c]: https://doi.org/10.2514/6.2015-3624
[research_smith_farokhi_2018]: https://doi.org/10.1515/tjj-2016-0042
[research_smith_finlayson_1978]: https://doi.org/10.1007/978-1-4684-3351-7_21
[research_smith_good_1979]: https://doi.org/10.2514/3.61244
[research_smith_pellicano_1992]: https://doi.org/10.2514/6.1992-4080
[research_smith_scribben_2007]: https://doi.org/10.21236/ada470860
[research_smithkent_ridder_1993]: https://doi.org/10.2514/6.1993-1926
[research_smits_1986]: https://doi.org/10.21236/ada178559
[research_smits_1988]: https://doi.org/10.21236/ada191494
[research_snyder_2003]: https://doi.org/10.2514/6.2003-7026
[research_snyder_vilendrer_1999]: https://doi.org/10.1097/00002480-199903000-00117
[research_sobel_nawaz_1972]: https://doi.org/10.21236/ad0762579
[research_sobieczky_1991]: https://doi.org/10.2514/6.1991-3301
[research_sobieczky_2026]: https://doi.org/10.1201/9781003760528-10
[research_solomonov_milekhin_2010]: https://doi.org/10.1007/s10573-010-0078-5
[research_soltani_farahani_2011]: https://doi.org/10.1016/j.scient.2011.03.019
[research_son_ko_2024]: https://doi.org/10.2139/ssrn.4795428
[research_son_ko_2024_b]: https://doi.org/10.2514/6.2024-3892
[research_son_son_2022]: https://doi.org/10.3390/aerospace9070348
[research_song_cai_2026]: https://doi.org/10.1016/j.ijhydene.2026.157041
[research_song_choi_2006]: https://doi.org/10.2514/1.11300
[research_song_choi_2020]: https://doi.org/10.1016/j.ifacol.2020.12.1900
[research_song_qin_2023]: https://doi.org/10.1016/j.fuel.2023.128349
[research_song_wang_2019]: https://doi.org/10.1016/j.actaastro.2019.02.012
[research_song_zhang_2026]: https://doi.org/10.3390/aerospace13070593
[research_soni_de_2017]: https://doi.org/10.1007/s12206-017-0215-0
[research_sorensen_bencze_1973]: https://doi.org/10.2514/6.1973-1271
[research_southwestresearchinstsanantoniotx_1963]: https://doi.org/10.21236/ad0426127
[research_space_environment]: https://doi.org/10.3403/30237419
[research_space_systems]: https://doi.org/10.3403/30176278u
[research_spearman_2003]: https://doi.org/10.2514/6.2003-7061
[research_specific_impulse]: https://doi.org/10.1007/springerreference_67673
[research_specific_impulse_2008]: https://doi.org/10.1007/978-0-387-48998-8_1439
[research_specific_impulse_2015]: https://doi.org/10.1007/978-1-4614-5491-5_200248
[research_specker_brinkley_1983]: https://doi.org/10.21236/ada360100
[research_spedding_hanak_1960]: https://doi.org/10.2172/1114463
[research_speer_aubrey_1982]: https://doi.org/10.21236/ada119916
[research_spekreijse_1991]: https://doi.org/10.1007/978-3-642-76527-8_76
[research_speyer_dannemiller_1980]: https://doi.org/10.2514/6.1980-1777
[research_sprangle_johnson_2015]: https://doi.org/10.21236/ada614567
[research_spravka_jorris_2015]: https://doi.org/10.2514/6.2015-3224
[research_spravka_jorris_2015_b]: https://doi.org/10.21236/ada619521
[research_spring_1972]: https://doi.org/10.21236/ad0753358
[research_squire_diaz_1999]: https://doi.org/10.13182/fst99-a11963860
[research_sridharan_rodriguez_2013]: https://doi.org/10.2514/6.2013-5166
[research_srikant_wagner_2010]: https://doi.org/10.2514/1.46937
[research_srinivas_1992]: https://doi.org/10.1007/978-3-642-77922-0_34
[research_srinivasan_newman_2013]: https://doi.org/10.1115/gtindia2013-3586
[research_srivastava_1994]: https://doi.org/10.1007/978-94-011-1086-0_4
[research_srivastava_1994_b]: https://doi.org/10.1007/978-94-011-1086-0_6
[research_staack_de_2000]: https://doi.org/10.2514/6.2000-4
[research_stabe_whitney_1984]: https://doi.org/10.2514/6.1984-1161
[research_stalker_1989]: https://doi.org/10.1146/annurev.fluid.21.1.37
[research_stalker_1992]: https://doi.org/10.1007/978-3-642-77922-0_17
[research_stalker_morgan_1984]: https://doi.org/10.1016/0010-2180(84)90137-8
[research_stalker_morgan_1988]: https://doi.org/10.1016/0010-2180(88)90106-x
[research_stalker_simmons_1994]: https://doi.org/10.2514/6.1994-2516
[research_stallings_hartman_1981]: https://doi.org/10.21236/ada103383
[research_standard_atmosphere]: https://doi.org/10.1007/springerreference_29038
[research_standard_atmosphere_1927]: https://doi.org/10.6028/nbs.mp.78
[research_standard_atmosphere_1927_b]: https://doi.org/10.6028/nbs.mp.82
[research_standard_atmosphere_1992]: https://doi.org/10.1016/b978-0-12-354355-4.50022-x
[research_standard_atmosphere_1997]: https://doi.org/10.2514/5.9781600861345.0435.0437
[research_standard_atmosphere_2005]: https://doi.org/10.1017/cbo9780511807138.014
[research_standard_atmosphere_2007]: https://doi.org/10.1007/978-0-387-30160-0_10930
[research_standard_atmosphere_2014]: https://doi.org/10.1351/goldbook.s05906
[research_standard_atmosphere_2021]: https://doi.org/10.5040/9781501365072.15547
[research_standard_atmosphere_2021_b]: https://doi.org/10.5040/9781501365072.15548
[research_standard_atmosphere_2023]: https://doi.org/10.1017/9781009043076.015
[research_standard_atmosphere_2024]: https://doi.org/10.2514/5.9781624107290.1007.1012
[research_standard_atmospheric_2002]: https://doi.org/10.1016/s0074-6142(02)80030-4
[research_stanleythomastroy_alexanderreginald_2000]: https://ntrs.nasa.gov/citations/20000021504
[research_starikovskiy_ju_2024]: https://doi.org/10.2514/6.2024-0183
[research_starkey_2009]: https://doi.org/10.2514/6.2009-4941
[research_starkey_2014]: https://doi.org/10.2514/6.2014-3111
[research_starkey_cannella_2014]: https://doi.org/10.2514/6.2014-3784
[research_starkey_lewis_1999]: https://doi.org/10.2514/6.1999-4953
[research_starkey_lewis_1999_b]: https://doi.org/10.2514/6.1999-2378
[research_starkey_lewis_2000]: https://doi.org/10.2514/6.2000-3312
[research_starkey_lewis_2003]: https://doi.org/10.2514/2.6084
[research_starkey_rankins_2005]: https://doi.org/10.2514/6.2005-530
[research_starkey_rankins_2006]: https://doi.org/10.2514/6.2006-337
[research_static_and_2005]: https://doi.org/10.1016/s0140-6701(05)81337-2
[research_stebbins_loth_2024]: https://doi.org/10.2514/6.2024-0887
[research_stecklein_hasen_1993]: https://doi.org/10.2514/6.1993-320
[research_steelant_vanduijn_2011]: https://doi.org/10.2514/6.2011-2336
[research_stefaniya_pushpalatha_2025]: https://doi.org/10.1134/s001546282560227x
[research_steinetzbrucem_1992]: https://ntrs.nasa.gov/citations/19920011573
[research_steinetzbrucem_mutharasanrajakkannu_1992]: https://ntrs.nasa.gov/citations/19920007118
[research_stemmer_adams]: https://doi.org/10.1007/3-540-29064-8_9
[research_stenberg_1983]: https://doi.org/10.2514/6.1983-1055
[research_stenzel_urrutia_2014]: https://doi.org/10.21236/ada601481
[research_stern_1983]: https://doi.org/10.2514/6.1983-2158
[research_sternberg_1964]: https://doi.org/10.1016/b978-0-08-010580-2.50015-3
[research_sternberg_2010]: https://doi.org/10.21236/ada518365
[research_sterne_1958]: https://doi.org/10.1063/1.1724338
[research_sterne_1958_b]: https://doi.org/10.1063/1.1724383
[research_stetson_1990]: https://doi.org/10.21236/ada227242
[research_stetson_sawyer_1977]: https://doi.org/10.2514/6.1977-690
[research_steva]: https://doi.org/10.18130/v3hm1j
[research_stevens_2014]: https://doi.org/10.2514/6.2014-2184
[research_stewart_1981]: https://doi.org/10.1016/0360-1323(81)90024-x
[research_stewart_quigg_1963]: https://doi.org/10.1016/s0082-0784(63)80097-1
[research_stewart_smith_1992]: https://doi.org/10.2514/6.1992-836
[research_stickels_1986]: https://doi.org/10.1007/bf02833090
[research_stilp]: https://doi.org/10.1007/3-540-27168-6_5
[research_stokes_acharya_2023]: https://doi.org/10.2514/6.2023-3075
[research_stokes_acharya_2023_b]: https://doi.org/10.2514/6.2023-0712
[research_stokes_lombaerts_2023]: https://doi.org/10.2514/6.2023-1638
[research_stoll_1961]: https://doi.org/10.21236/ad0259076
[research_stoll_munroe_1975]: https://doi.org/10.21236/ada021234
[research_stollery_1990]: https://doi.org/10.1063/1.39449
[research_stoloff_jone_1997]: https://doi.org/10.21236/ada329848
[research_stone_1945]: https://doi.org/10.21236/ada801302
[research_stone_2024]: https://doi.org/10.21236/ad1227418
[research_stoukov_gorokhovski_1997]: https://doi.org/10.1007/978-94-011-5432-1_10
[research_strand_ennis_2012]: https://doi.org/10.1109/aero.2012.6187310
[research_strauss_fischer_2026]: https://doi.org/10.2514/6.2026-5146
[research_strauss_manassis_2025]: https://doi.org/10.2514/6.2025-1142
[research_streby_mathur_1999]: https://doi.org/10.21236/ada372847
[research_street]: https://doi.org/10.14264/340dbcb
[research_streiff_1953]: https://doi.org/10.21236/ad0041742
[research_striebich_shafer_2008]: https://doi.org/10.21236/ada504691
[research_strock_1983]: https://doi.org/10.2514/6.1983-2759
[research_strome_1969]: https://doi.org/10.21236/ad0865977
[research_stroudcw_rummlerdr_1980]: https://ntrs.nasa.gov/citations/19800017901
[research_strutjet_rocket_based_2001]: https://doi.org/10.2514/5.9781600866609.0697.0755
[research_stuckey_lewis_1999]: https://doi.org/10.2514/6.1999-4929
[research_study_on_2021]: https://doi.org/10.47939/et.v2i8.160
[research_sturek_schiff_1981]: https://doi.org/10.21236/ada110016
[research_su_chen_2018]: https://doi.org/10.1016/j.actaastro.2017.10.040
[research_su_liu_2021]: https://doi.org/10.32908/hthp.v50.957
[research_su_zhao_2024]: https://doi.org/10.1088/1742-6596/2764/1/012069
[research_subbiah_stefaniya_2025]: https://doi.org/10.1063/5.0262244
[research_subramanian_thangadurai_2025]: https://doi.org/10.2514/6.2025-0094
[research_subrata_2007]: https://doi.org/10.21236/ada474248
[research_subsonic_and_1975]: https://doi.org/10.2514/5.9781600865114.0125.0151
[research_suchomel_vanwie_2006]: https://doi.org/10.2514/6.2006-398
[research_sudalagunta_sultan_2018]: https://doi.org/10.2514/1.g002777
[research_suetin_kartsev_1993]: https://doi.org/10.2514/6.1993-2483
[research_sugarno_sriram_2022]: https://doi.org/10.1063/5.0075583
[research_sullins_1993]: https://doi.org/10.2514/3.23653
[research_sullins_billig_1987]: https://doi.org/10.2514/6.1987-1965
[research_sullins_carpenter_1991]: https://doi.org/10.2514/6.1991-2395
[research_sullivan_gaitonde_2022]: https://doi.org/10.1115/imece2022-94316
[research_sultanov_glebov_2021]: https://doi.org/10.18698/0236-3941-2021-3-98-107
[research_summerfield_1992]: https://doi.org/10.2514/6.1992-5045
[research_summors]: https://doi.org/10.14264/c50b272
[research_sun_2008]: https://doi.org/10.2514/6.2008-6927
[research_sun_fang_2005]: https://doi.org/10.1016/j.fuel.2004.12.006
[research_sun_geng_2008]: https://doi.org/10.1007/s10494-008-9178-7
[research_sun_li_2013]: https://doi.org/10.1109/jsee.2013.00057
[research_sun_li_2019]: https://doi.org/10.1016/j.fuel.2018.11.003
[research_sun_li_2021]: https://doi.org/10.1016/j.ast.2021.106901
[research_sun_li_2025]: https://doi.org/10.1016/j.icheatmasstransfer.2024.108564
[research_sun_li_2026]: https://doi.org/10.1109/taes.2026.3687820
[research_sun_li_2026_b]: https://doi.org/10.1016/j.ast.2026.111909
[research_sun_ma_2024]: https://doi.org/10.1109/taes.2024.3417425
[research_sun_ran_2025]: https://doi.org/10.1109/jsen.2025.3598737
[research_sun_wang_2017]: https://doi.org/10.23919/chicc.2017.8028063
[research_sun_wang_2020]: https://doi.org/10.1007/978-981-15-3595-6_4
[research_sun_wang_2020_b]: https://doi.org/10.1007/978-981-15-3595-6_2
[research_sun_wang_2020_c]: https://doi.org/10.1007/978-981-15-3595-6_5
[research_sun_wang_2020_d]: https://doi.org/10.1007/978-981-15-3595-6_3
[research_sun_wang_2020_e]: https://doi.org/10.1007/978-981-15-3595-6_6
[research_sun_wu_2023]: https://doi.org/10.1049/icp.2022.3063
[research_sun_xin_2014]: https://doi.org/10.2514/6.2014-2383
[research_sun_yang_2020]: https://doi.org/10.12783/dtcse/cmso2019/33628
[research_sun_yu_2026]: https://doi.org/10.2139/ssrn.6182785
[research_sun_zhang_2009]: https://doi.org/10.2514/6.2009-7424
[research_sun_zhang_2011]: https://doi.org/10.1109/icicip.2011.6008304
[research_sun_zhang_2016]: https://doi.org/10.2322/tjsass.59.349
[research_sun_zhong_2016]: https://doi.org/10.1016/j.actaastro.2016.05.035
[research_sun_zhu_2019]: https://doi.org/10.1063/1.5083820
[research_sun_zhu_2023]: https://doi.org/10.3390/aerospace10030310
[research_sunden_fu_2017]: https://doi.org/10.1016/b978-0-12-809760-1.00003-x
[research_suneetha_randive_2019]: https://doi.org/10.1016/j.matpr.2019.06.282
[research_sung_hsieh_2001]: https://doi.org/10.2514/6.2001-3192
[research_sung_hsieh_2001_b]: https://doi.org/10.2514/6.2001-3460
[research_sung_jo_2025]: https://doi.org/10.6108/jpne.2025.5.1.022
[research_sung_jo_2026]: https://doi.org/10.2514/1.b40184
[research_sunjian_liuweiqiang_2014]: https://doi.org/10.7498/aps.63.094401
[research_supersonic_combustion_1977]: https://doi.org/10.2514/5.9781600865275.0227.0242
[research_supersonic_combustion_2009]: https://doi.org/10.1017/cbo9780511627019.007
[research_supersonic_jet_1994]: https://doi.org/10.2514/6.1994-185
[research_suppe_2000]: https://doi.org/10.1007/978-94-011-4379-0_3
[research_surber_1975]: https://doi.org/10.2514/6.1975-1183
[research_surber_robinson_1983]: https://doi.org/10.2514/6.1983-1164
[research_surber_sedlock_1978]: https://doi.org/10.2514/6.1978-960
[research_surget_dunet_1993]: https://doi.org/10.1007/978-94-011-1828-6_10
[research_surzhikov_2009]: https://doi.org/10.1134/s0018151x09040026
[research_surzhikov_2013]: https://doi.org/10.1134/s0018151x13010185
[research_surzhikov_2021]: https://doi.org/10.33257/phchgd.22.1.931
[research_surzhikov_2021_b]: https://doi.org/10.33257/phchgd.22.1.930
[research_surzhikov_shang_2013]: https://doi.org/10.2514/6.2013-2642
[research_surzhikov_surzhikov_1997]: https://doi.org/10.2514/6.1997-2229
[research_sushma_rani_2025]: https://doi.org/10.4273/ijvss.17.6.11
[research_sutliff_1973]: https://doi.org/10.1115/73-gt-76
[research_sutton_chao_1997]: https://doi.org/10.21236/ada340457
[research_sutton_troiler_1995]: https://doi.org/10.2514/6.1995-2014
[research_suzuki_2016]: https://doi.org/10.2322/tastj.14.pe_71
[research_suzuki_watanabe_2013]: https://doi.org/10.2514/6.2013-2773
[research_svec_1981]: https://doi.org/10.2514/6.1981-2498
[research_svendsen_1994]: https://doi.org/10.2514/6.1994-2160
[research_swain_p_2020]: https://doi.org/10.1080/00102202.2020.1791838
[research_swann_duke_1981]: https://doi.org/10.2514/6.1981-2504
[research_swanson_caghlan_2007]: https://doi.org/10.2514/6.2007-1670
[research_swigart_1962]: https://doi.org/10.21236/ad0274612
[research_swigart_1963]: https://doi.org/10.2514/3.2133
[research_swithebank_chigier_1969]: https://doi.org/10.1016/s0082-0784(69)80492-3
[research_swithenbank_ewan_1992]: https://doi.org/10.1007/978-1-4612-2884-4_26
[research_swithenbank_jaques_1970]: https://doi.org/10.21236/ad0709222
[research_syberg_koncsek_1980]: https://doi.org/10.2514/6.1980-1106
[research_sykes]: https://doi.org/10.15368/theses.2014.182
[research_sylvester_1967]: https://doi.org/10.21236/ad0656445
[research_system_for_1974]: https://doi.org/10.2514/5.9781600865077.0059.0076
[research_szema_liu_2010]: https://doi.org/10.2514/6.2010-4362
[research_szwaba_doerffer_2017]: https://doi.org/10.1007/978-3-319-44866-4_60
[research_tabanli_yuceil_2018]: https://doi.org/10.1007/978-94-024-1544-5_27
[research_tachinina_lysenko_2018]: https://doi.org/10.1109/msnmc.2018.8576319
[research_taghiabad_esfandabadi_2026]: https://doi.org/10.1016/j.ast.2025.110963
[research_taguchi_harada_2009]: https://doi.org/10.2514/6.2009-7311
[research_taguchi_harada_2014]: https://doi.org/10.2514/6.2014-2790
[research_taguchi_kashitani_2025]: https://doi.org/10.2514/6.2025-0489
[research_taha_tiwari_2001]: https://doi.org/10.1016/b978-008043944-0/50923-9
[research_taheri_2020]: https://doi.org/10.2514/6.2020-2184
[research_tahir_2021]: https://doi.org/10.32920/ryerson.14644473.v1
[research_tahir_timofeev]: https://doi.org/10.1007/3-540-31801-1_141
[research_takagi_morozumi_2014]: https://doi.org/10.2514/6.2014-4033
[research_takahashi_2005]: https://doi.org/10.2514/6.2005-4556
[research_takahashi_2012]: https://doi.org/10.1179/096034012x13481643330388
[research_takahashi_hirotani_2025]: https://doi.org/10.2514/6.2025-1340
[research_takahashi_kodera_2020]: https://doi.org/10.2514/1.j059429
[research_takahashi_komuro_2007]: https://doi.org/10.2514/6.2007-5395
[research_takahashi_oki_2023]: https://doi.org/10.2514/6.2023-3029
[research_takahashi_sunami_2005]: https://doi.org/10.2514/6.2005-3350
[research_takahashi_wakai_1998]: https://doi.org/10.1016/s0082-0784(98)80062-3
[research_takahashi_yamada_2013]: https://doi.org/10.2514/6.2013-1303
[research_takama_2011]: https://doi.org/10.2514/6.2011-2300
[research_takasaki_fujimoto_1998]: https://doi.org/10.2514/6.1998-5546
[research_takashima_lewis_1995]: https://doi.org/10.2514/6.1995-846
[research_takashima_lewis_1996]: https://doi.org/10.2514/6.1996-4593
[research_takashima_lewis_1996_b]: https://doi.org/10.2514/6.1996-2551
[research_takashima_lewis_1999]: https://doi.org/10.2514/2.2430
[research_takashiman_kothariap_1998]: https://ntrs.nasa.gov/citations/19990079881
[research_takegoshi_tomioka_2012]: https://doi.org/10.2514/6.2012-5915
[research_talantov_1959]: https://doi.org/10.2514/8.4899
[research_talmage_2008]: https://doi.org/10.2514/6.2008-2659
[research_tam_eklund_2005]: https://doi.org/10.2514/6.2005-3286
[research_tam_eklund_2008]: https://doi.org/10.2514/6.2008-6929
[research_tam_hsu_2007]: https://doi.org/10.2514/6.2007-5403
[research_tam_hsu_2008]: https://doi.org/10.2514/6.2008-6925
[research_tam_hsu_2011]: https://doi.org/10.2514/6.2011-5540
[research_tam_hsu_2012]: https://doi.org/10.2514/6.2012-3224
[research_tam_li_1989]: https://doi.org/10.2514/6.1989-1860
[research_tam_lin_2006]: https://doi.org/10.2514/6.2006-4509
[research_tan_bogdonoff_1985]: https://doi.org/10.2514/6.1985-125
[research_tan_li_2011]: https://doi.org/10.2514/1.j050200
[research_tan_sun_2009]: https://doi.org/10.2514/1.37914
[research_tan_wang_2015]: https://doi.org/10.2514/1.b35263
[research_tanatsugu_carrick_2003]: https://doi.org/10.2514/6.2003-2586
[research_tandon_dumm_2006]: https://doi.org/10.2172/887260
[research_tang_cai_2025]: https://doi.org/10.1063/5.0277814
[research_tang_cai_2025_b]: https://doi.org/10.1063/5.0297492
[research_tang_fan_2026]: https://doi.org/10.1016/j.ast.2026.111869
[research_tang_gao_2021]: https://doi.org/10.1109/cac53003.2021.9728007
[research_tang_hu_2023]: https://doi.org/10.23919/ccc58697.2023.10240416
[research_tang_li_2025]: https://doi.org/10.2139/ssrn.5295009
[research_tang_long_2018]: https://doi.org/10.3103/s0146411618030100
[research_tang_xiong_2023]: https://doi.org/10.3390/app13179752
[research_tang_xiong_2024]: https://doi.org/10.1016/j.ast.2024.109189
[research_tang_zhai_2020]: https://doi.org/10.1016/j.ins.2019.08.012
[research_tang_zhang_2025]: https://doi.org/10.1007/978-981-96-2240-5_40
[research_tang_zheng_2005]: https://doi.org/10.2514/6.2005-3220
[research_tang_zhou_1991]: https://doi.org/10.1063/1.105755
[research_tani_kanda_2000]: https://doi.org/10.2514/6.2000-620
[research_tanigawa_1999]: https://doi.org/10.1080/014957399281048
[research_tanjung_2022]: https://doi.org/10.2139/ssrn.3959297
[research_tanno_komuro_2015]: https://doi.org/10.2514/6.2015-3655
[research_tanno_tanno_2021]: https://doi.org/10.1007/s00348-021-03229-0
[research_tao_1995]: https://doi.org/10.2514/6.1995-4
[research_tao_daren_2008]: https://doi.org/10.1017/s0001924000002517
[research_tao_daren_2008_b]: https://doi.org/10.2514/1.34125
[research_tao_daren_2009]: https://doi.org/10.2514/1.38926
[research_tao_li_2016]: https://doi.org/10.1016/j.ins.2015.08.033
[research_tarfeld_2003]: https://doi.org/10.2514/6.2003-7056
[research_tarnavskii_2005]: https://doi.org/10.1007/pl00021856
[research_tarpley_lewis_1993]: https://doi.org/10.2514/6.1993-508
[research_tarpley_lewis_1995]: https://doi.org/10.2514/6.1995-848
[research_tarpley_lewis_1995_b]: https://doi.org/10.2514/3.46793
[research_tarpley_pines_1996]: https://doi.org/10.2514/6.1996-4596
[research_tatman]: https://doi.org/10.18130/v3g36z
[research_tatsuta_yamada_2025]: https://doi.org/10.21203/rs.3.rs-7500874/v1
[research_taylor_1959]: https://doi.org/10.1016/b978-1-4831-9728-9.50029-1
[research_taylor_jackson_1977]: https://doi.org/10.2514/6.1977-392
[research_taylor_jackson_1978]: https://doi.org/10.2514/3.58342
[research_taylor_stringer_2024]: https://doi.org/10.2514/6.2024-3580
[research_tchuen_burtschell_2008]: https://doi.org/10.1080/10618560701766525
[research_tchuen_burtschell_2011]: https://doi.org/10.5772/18941
[research_teng_yang_2016]: https://doi.org/10.1177/1729881416678140
[research_teng_yu_2012]: https://doi.org/10.2514/6.2012-1648
[research_teng_zhou_2017]: https://doi.org/10.2514/6.2017-2146
[research_terekhov_2023]: https://doi.org/10.1134/s0018151x23050188
[research_test_method]: https://doi.org/10.1520/c1569-22
[research_test_method_1900]: https://doi.org/10.1520/c1569
[research_test_method_2009]: https://doi.org/10.1520/c1569-03r09
[research_test_method_b]: https://doi.org/10.1520/d2508-93
[research_testing_methods_2009]: https://doi.org/10.1017/cbo9780511627019.008
[research_tetlow_doolan]: https://doi.org/10.1109/aero.2006.1656161
[research_thakur_segal_2003]: https://doi.org/10.2514/6.2003-6909
[research_thakur_segal_2004]: https://doi.org/10.2514/6.2004-3831
[research_thakur_segal_2006]: https://doi.org/10.2514/6.2006-1380
[research_the_aedc_2002]: https://doi.org/10.2514/5.9781600866678.0467.0478
[research_the_agard_1959]: https://doi.org/10.1016/b978-1-4831-9727-2.50003-x
[research_the_flight_2021]: https://doi.org/10.1002/9781118949818.ch2
[research_the_international_2017]: https://doi.org/10.1016/b978-0-08-100194-3.00017-1
[research_the_international_2026]: https://doi.org/10.1016/b978-0-32-399544-3.00016-5
[research_the_onera_2002]: https://doi.org/10.2514/5.9781600866678.0441.0466
[research_the_scirocco_2002]: https://doi.org/10.2514/5.9781600866678.0315.0351
[research_the_standard_1964]: https://doi.org/10.1016/b978-0-12-634450-9.50033-6
[research_the_standard_1976]: https://doi.org/10.1016/b978-0-08-020414-7.50016-2
[research_the_theoretical_2012]: https://doi.org/10.2514/6.2012-5911
[research_theocaris_koroneos_1963]: https://doi.org/10.1080/14786436308209080
[research_thermal_physics_2013]: https://doi.org/10.1201/b16193-13
[research_thermal_properties_1998]: https://doi.org/10.14359/373
[research_thermal_protection_2009]: https://doi.org/10.1109/9780470544884.ch13
[research_thermal_structural_1992]: https://doi.org/10.2514/5.9781600866128.0279.0299
[research_thermodynamics_of_2010]: https://doi.org/10.1142/9789814295123_0011
[research_thibodeaux_2002]: https://doi.org/10.2514/6.2002-2109
[research_thieblot_roux_1998]: https://doi.org/10.1127/ejm/10/1/0007
[research_thielman_1995]: https://doi.org/10.4271/951443
[research_thirunavukkarasu_ghosh_2023]: https://doi.org/10.1063/5.0175415
[research_thivet_pelissier_2003]: https://doi.org/10.2514/6.2003-7013
[research_thomas_1942]: https://doi.org/10.21236/ad0494220
[research_thomas_czech_2010]: https://doi.org/10.2514/6.2010-3912
[research_thomas_dwoyer_1991]: https://doi.org/10.1007/978-3-642-84580-2_6
[research_thomas_guy_1982]: https://doi.org/10.2514/6.1982-1240
[research_thomas_harrison_1994]: https://doi.org/10.21236/ada282798
[research_thomas_hyde_1998]: https://doi.org/10.21236/ada451482
[research_thomas_marayikkottuvijayan_2022]: https://doi.org/10.2514/6.2022-1499
[research_thomas_martellucci_1969]: https://doi.org/10.2514/6.1969-349
[research_thomas_perlbachs_1967]: https://doi.org/10.21236/ad0655383
[research_thomas_singh_1985]: https://doi.org/10.1080/01495738508942233
[research_thomas_voland_1987]: https://doi.org/10.2514/6.1987-2165
[research_thome_dwivedi_2018]: https://doi.org/10.2514/6.2018-2894
[research_thompson_2015]: https://doi.org/10.21236/ada624250
[research_thompson_2025]: https://doi.org/10.64631/thomp9901
[research_thornton_1994]: https://doi.org/10.2514/6.1994-2163
[research_thornton_dechaumphai_1986]: https://doi.org/10.2514/6.1986-911
[research_thornton_lamy_1992]: https://doi.org/10.2514/6.1992-4070
[research_thornton_oden_1989]: https://doi.org/10.2514/6.1989-1226
[research_threadgill_bruce_2015]: https://doi.org/10.2514/6.2015-1977
[research_tian_duan_2023]: https://doi.org/10.1155/2023/1920270
[research_tian_fan_2013]: https://doi.org/10.1109/icca.2013.6565039
[research_tian_wan_2026]: https://doi.org/10.1016/j.proci.2026.106308
[research_tian_yang_2016]: https://doi.org/10.1016/j.ast.2016.02.027
[research_tian_zhang_2026]: https://doi.org/10.1016/j.applthermaleng.2025.129641
[research_tieshan_zhiyao_2021]: https://doi.org/10.1109/ccdc52312.2021.9601884
[research_tietz_chun_2006]: https://doi.org/10.2514/6.iac-06-c4.5.05
[research_tile_gap_flow_1983]: https://doi.org/10.2514/5.9781600865626.0271.0299
[research_tilmann_1998]: https://doi.org/10.21236/ada359861
[research_timnat_1987]: https://doi.org/10.2514/6.1987-1787
[research_timofeev_tahir_2008]: https://doi.org/10.2514/6.2008-2512
[research_timofeev_voinovich_2001]: https://doi.org/10.2514/6.2001-1896
[research_tincher_burnett_1992]: https://doi.org/10.2514/6.1992-308
[research_ting_libby_1960]: https://doi.org/10.21236/ad0404542
[research_tinney_2014]: https://doi.org/10.21236/ada613848
[research_tinney_panickar_2013]: https://doi.org/10.21236/ada627137
[research_tirres_bradley_2002]: https://doi.org/10.2514/6.2002-2706
[research_tirskii_1993]: https://doi.org/10.1007/bf00570739
[research_tirsky_1993]: https://doi.org/10.1146/annurev.fl.25.010193.001055
[research_tirtey_boyce_2009]: https://doi.org/10.2514/6.2009-7295
[research_tirtey_walpot_2006]: https://doi.org/10.2514/6.2006-7940
[research_tishkoff_drummond_1997]: https://doi.org/10.2514/6.1997-1017
[research_titov_1961]: https://doi.org/10.1007/bf00814550
[research_tiwari_abdelsalam_2001]: https://doi.org/10.2514/6.2001-380
[research_tiwari_soman_2026]: https://doi.org/10.2514/6.2026-5121
[research_tiwari_taha_2002]: https://doi.org/10.2514/6.2002-806
[research_tobe_grandhi_2013]: https://doi.org/10.1016/j.ast.2012.11.001
[research_tobin_dec_2015]: https://doi.org/10.2514/6.2015-1895
[research_tomar_2012]: https://doi.org/10.21236/ada581368
[research_tomasi_mutri]: https://doi.org/10.1007/1-4020-3498-9_40
[research_tomczak_2026]: https://doi.org/10.21741/9781644904251-111
[research_tomioka_hiraiwa_2007]: https://doi.org/10.2514/1.28149
[research_tomioka_kanda_1998]: https://doi.org/10.2514/6.1998-3134
[research_tomioka_takahashi_2016]: https://doi.org/10.2514/6.2016-4758
[research_tomioka_takahashi_2018]: https://doi.org/10.2514/6.2018-4453
[research_tomioka_ueda_2007]: https://doi.org/10.2514/6.2007-1040
[research_tong_duan_2022]: https://doi.org/10.1016/j.cja.2021.10.013
[research_tong_giedt_1963]: https://doi.org/10.21236/ad0403711
[research_tong_ji_2024]: https://doi.org/10.1016/j.compfluid.2024.106444
[research_tong_steinetz_1991]: https://doi.org/10.2514/6.1991-2494
[research_tong_yuan_2022]: https://doi.org/10.1063/5.0094070
[research_tong_yue_2023]: https://doi.org/10.2514/1.j061874
[research_toong_1978]: https://doi.org/10.21236/ada061976
[research_torres_stefanini_2009]: https://doi.org/10.1051/eucass/200901171
[research_torrez_dalle_2010]: https://doi.org/10.2514/6.2010-6957
[research_torrez_dalle_2011]: https://doi.org/10.2514/6.2011-5757
[research_toure_schuelein_2017]: https://doi.org/10.2514/6.2017-4123
[research_tracy_1981]: https://doi.org/10.2514/6.1981-2464
[research_tracy_wright_2020]: https://doi.org/10.1080/08929882.2020.1864945
[research_trainini_cabrerafischer_2026]: https://doi.org/10.7775/x55kpk55
[research_tran_chen_1998]: https://doi.org/10.2514/6.1998-3762
[research_transient_thermal_structural_1992]: https://doi.org/10.2514/5.9781600866128.0205.0227
[research_transient_thermal_structural_1995]: https://doi.org/10.2514/5.9781600866364.0096.0115
[research_transonic_flight_1994]: https://doi.org/10.2514/6.1994-2142
[research_trapier_deck]: https://doi.org/10.1007/978-3-540-77815-8_25
[research_trapier_deck_2007]: https://doi.org/10.2514/6.2007-4353
[research_trapier_deck_2007_b]: https://doi.org/10.2514/1.29196
[research_trapier_deck_2008]: https://doi.org/10.2514/1.32187
[research_trapier_duveau_2006]: https://doi.org/10.2514/1.20451
[research_trefny_2020]: https://doi.org/10.2514/6.2020-3771
[research_trefny_dippold_2010]: https://doi.org/10.2514/6.2010-6643
[research_trella_vagliolaurin_1964]: https://doi.org/10.21236/ad0451726
[research_tretyakov_tupikin_2021]: https://doi.org/10.1134/s0010508221060010
[research_trexler_1988]: https://doi.org/10.2514/6.1988-3257
[research_triantafillou_schwendeman_1998]: https://doi.org/10.1007/s001620050107
[research_trimmer_1968]: https://doi.org/10.21236/ad0669378
[research_trimmer_caryjr_1986]: https://doi.org/10.2514/6.1986-739
[research_trittler_fichter_2008]: https://doi.org/10.2514/6.2008-6896
[research_truittrw_1968]: https://ntrs.nasa.gov/citations/19700009384
[research_trulove_2008]: https://doi.org/10.21236/ada521096
[research_trunin_krupnikov_2004]: https://doi.org/10.1007/978-1-4757-4048-6_5
[research_tsai_miles_1992]: https://doi.org/10.2514/6.1992-2726
[research_tsailorkoeplinger_calebhash]: https://ntrs.nasa.gov/citations/20260000615
[research_tsuboi_matsumoto_2008]: https://doi.org/10.1063/1.3076536
[research_tsujikawa_1996]: https://doi.org/10.1016/0360-3199(95)00077-1
[research_tsukamoto_deturris_2003]: https://doi.org/10.2514/6.2003-911
[research_tudosie_2017]: https://doi.org/10.19062/2247-3173.2017.19.1.26
[research_tudosie_2017_b]: https://doi.org/10.19062/1842-9238.2017.15.1.16
[research_tudosie_2018]: https://doi.org/10.19062/2247-3173.2018.20.33
[research_tudosie_2022]: https://doi.org/10.1109/codit55151.2022.9803926
[research_tudosie_dumitru_2019]: https://doi.org/10.19062/2247-3173.2019.21.27
[research_tudosie_paunescu_2017]: https://doi.org/10.19062/2247-3173.2017.19.1.27
[research_tudosie_prisacariu_2022]: https://doi.org/10.19062/2247-3173.2021.22.19
[research_tumin_1996]: https://doi.org/10.1063/1.869037
[research_tunik_2020]: https://doi.org/10.33257/phchgd.21.1.871
[research_tunik_gerasimov_2022]: https://doi.org/10.1016/j.actaastro.2022.06.027
[research_tunik_mayorov_2022]: https://doi.org/10.1016/j.actaastro.2021.09.038
[research_tunik_mayorov_2022_b]: https://doi.org/10.1016/j.ijhydene.2022.05.023
[research_tuohy_2006]: https://doi.org/10.2514/6.2006-7909
[research_turcotte_1987]: https://doi.org/10.21236/ada204630
[research_turkkahraman_ozcan_2024]: https://doi.org/10.2339/politeknik.1247300
[research_turkoglu_donmez_2026]: https://doi.org/10.2139/ssrn.6570198
[research_turner_1965]: https://doi.org/10.1016/b978-0-08-011074-5.50015-4
[research_turner_hoerschgen_2006]: https://doi.org/10.2514/6.2006-8115
[research_turns_kraige]: https://doi.org/10.1017/cbo9780511813696.014
[research_two_phase_flow_2006]: https://doi.org/10.1016/s0140-6701(06)80798-8
[research_two_phase_flow_2006_b]: https://doi.org/10.1016/s0140-6701(06)80797-6
[research_tyagi_achary_2017]: https://doi.org/10.1016/b978-0-12-801300-7.00013-9
[research_tyll_bakos_2000]: https://doi.org/10.2514/6.2000-2442
[research_ueda_kouchi_2009]: https://doi.org/10.1007/978-3-540-85181-3_54
[research_ueda_takegoshi_2006]: https://doi.org/10.2514/6.iac-06-c4.5.04
[research_ueno_imamura_2011]: https://doi.org/10.2514/6.2011-2340
[research_ueno_sarae_2004]: https://doi.org/10.2514/6.2004-4943
[research_uhlenbruck_tietz_2004]: https://doi.org/10.1016/j.mseb.2003.11.018
[research_ulislamrizvi_linshu_2015]: https://doi.org/10.1108/aeat-04-2013-0079
[research_ullman_raman_2023]: https://doi.org/10.1080/00102202.2023.2239447
[research_unnikrishnan_gaitonde_2021]: https://doi.org/10.1080/10618562.2021.1976758
[research_unsteady_interaction_2023]: https://doi.org/10.1063/5.0151663
[research_unterberg_1957]: https://doi.org/10.2514/8.12848
[research_upadhyay_kumar_2019]: https://doi.org/10.33564/ijeast.2019.v04i07.025
[research_upper_atmosphere_1961]: https://doi.org/10.2172/4791901
[research_us_standard_2014]: https://doi.org/10.1016/b978-0-12-419953-8.00019-x
[research_us_standard_atmosphere]: https://ntrs.nasa.gov/citations/19770009539
[research_us_tests_2011]: https://doi.org/10.1063/pt.5.025721
[research_utheza_saurel_1996]: https://doi.org/10.1007/pl00003875
[research_utomo_bura_2019]: https://doi.org/10.23960/ins.v2i2.90
[research_utyuzhnikov_tirskiy_2013]: https://doi.org/10.1615/978-1-56700-309-3.0
[research_v_rao_2023]: https://doi.org/10.2514/6.2023-3042
[research_vacarios_ceronmunoz_2025]: https://doi.org/10.1016/j.ast.2025.110135
[research_vahl_edwards_1978]: https://doi.org/10.2514/6.1978-38
[research_valaik_bowman_1998]: https://doi.org/10.21236/ada363542
[research_valaik_hyde_1997]: https://doi.org/10.21236/ada384687
[research_valdivia_yuceil_2014]: https://doi.org/10.2514/1.j052214
[research_van_1963]: https://doi.org/10.21236/ad0408349
[research_vanamamalai_panneerselvam_2024]: https://doi.org/10.24425/ather.2024.151227
[research_vanatta_inderhees_1988]: https://doi.org/10.2514/6.1988-2121
[research_vancamp_williams_1974]: https://doi.org/10.2514/6.1974-990
[research_vandenborre_saracoglu_2023]: https://doi.org/10.2514/6.2023-0499
[research_vandergeld_korting_1990]: https://doi.org/10.1016/0010-2180(90)90141-d
[research_vanderheide_bone_2026]: https://doi.org/10.2514/6.2026-0369
[research_vanderheide_lock_2025]: https://doi.org/10.2514/6.2025-0955
[research_vanderkreek]: https://doi.org/10.14264/9c396bd
[research_vanderlee_kaner_2026]: https://doi.org/10.2514/1.b40338
[research_vanderlee_michaels_2023]: https://doi.org/10.2514/6.2023-1647
[research_vanderlee_seniortybora_2026]: https://doi.org/10.1016/j.expthermflusci.2025.111629
[research_vanderlee_yokev_2021]: https://doi.org/10.2514/6.2021-4165
[research_vanderschaaf_acharya_2025]: https://doi.org/10.2514/6.2025-0673
[research_vandriest_blumer_1961]: https://doi.org/10.21236/ad0265237
[research_vanhoffen_2024]: https://doi.org/10.2514/6.2024-2888
[research_vanhoffen_buttsworth_2024]: https://doi.org/10.2514/6.2024-2888.c1
[research_vankeuk_ballmann_1998]: https://doi.org/10.2514/6.1998-1526
[research_vanpelt_1981]: https://doi.org/10.2514/6.1981-2375
[research_vanstone_hashemi_2017]: https://doi.org/10.2514/6.2017-1536
[research_vanstone_hashemi_2018]: https://doi.org/10.2514/1.b36743
[research_vanstone_lingren_2018]: https://doi.org/10.2514/6.2018-1618
[research_vanwie_1992]: https://doi.org/10.2514/6.1992-5104
[research_vanwie_molder_1992]: https://doi.org/10.2514/6.1992-1210
[research_vanyai_brieschenk_2021]: https://doi.org/10.1016/j.ast.2021.106499
[research_vanyai_grieve_2018]: https://doi.org/10.2514/6.2018-5201
[research_vanyai_grieve_2019]: https://doi.org/10.2514/1.b37472
[research_vanyai_grieve_2020]: https://doi.org/10.2514/1.b37472.c1
[research_varghese_b_2018]: https://doi.org/10.1615/ihmtc-2017.1450
[research_variation_of_1956]: https://doi.org/10.1029/tr037i002p00177
[research_varma_zhong_2022]: https://doi.org/10.2514/6.2022-0735
[research_varner_1976]: https://doi.org/10.21236/ada032725
[research_varshney_baig_2019]: https://doi.org/10.2514/6.2019-0297
[research_varshney_varshney_2020]: https://doi.org/10.2514/6.2020-2055
[research_varshney_varshney_2020_b]: https://doi.org/10.2514/6.2020-2055.c1
[research_vartio_shaw_2008]: https://doi.org/10.2514/6.2008-7192
[research_varwig_1963]: https://doi.org/10.21236/ad0403052
[research_vasilevsky_2022]: https://doi.org/10.31772/2712-8970-2022-23-4-671-687
[research_vaughan_2003]: https://doi.org/10.1016/b0-12-227090-8/00379-1
[research_vaughan_schwartz_1962]: https://doi.org/10.1007/978-1-4684-7606-4_23
[research_vaughn_lindsay_1988]: https://doi.org/10.2514/6.1988-2102
[research_vedula_1989]: https://doi.org/10.21236/ada230593
[research_veletas_2026]: https://doi.org/10.2514/6.2026-2636
[research_venkatapathye_tokarcikpolskys_1995]: https://ntrs.nasa.gov/citations/20020038842
[research_venkateshwaran_padmanathan_2026]: https://doi.org/10.1016/j.rineng.2026.110667
[research_venkateswarlu_kolhe_2025]: https://doi.org/10.1177/09544062251342080
[research_veraar_2008]: https://doi.org/10.2514/6.2008-2670
[research_veraar_2009]: https://doi.org/10.2514/6.2009-7379
[research_verhoff_oneil_1987]: https://doi.org/10.2514/6.1987-1165
[research_verma_2010]: https://doi.org/10.7763/ijet.2010.v2.187
[research_verma_kapayeva_2021]: https://doi.org/10.1016/j.matpr.2021.01.879
[research_verma_manisankar_2014]: https://doi.org/10.1007/s00193-014-0508-5
[research_verma_pandey_2021]: https://doi.org/10.1016/j.matpr.2020.07.388
[research_verma_pandey_2022]: https://doi.org/10.2139/ssrn.4051686
[research_verma_sharma_2022]: https://doi.org/10.1007/978-981-19-3266-3_41
[research_verma_shukla_2019]: https://doi.org/10.2514/6.2019-3221
[research_verma_shukla_2021]: https://doi.org/10.2514/6.2021-0837
[research_vicente_foy_1963]: https://doi.org/10.21236/ad0405493
[research_vicente_foy_1963_b]: https://doi.org/10.21236/ad0458212
[research_vidalrj_1974]: https://ntrs.nasa.gov/citations/19750012378
[research_vijayakumar_2020]: https://doi.org/10.1007/978-981-15-1201-8_31
[research_vijayakumar_narendar_2020]: https://doi.org/10.1007/978-981-15-1201-8_33
[research_vijayakumar_wilson_2014]: https://doi.org/10.2514/6.2014-3845
[research_vincentrandonnier_rouxel_2008]: https://doi.org/10.2514/6.2008-2676
[research_vinogradov_grachev_1990]: https://doi.org/10.2514/6.1990-5269
[research_violi_2013]: https://doi.org/10.21236/ada582596
[research_viscous_flow_2006]: https://doi.org/10.2514/5.9781600861956.0261.0374
[research_viscous_flow_2019]: https://doi.org/10.2514/5.9781624105142.0267.0388
[research_viscous_shock_layer_1983]: https://doi.org/10.2514/5.9781600865626.0054.0077
[research_vishwakarma_rana_2025]: https://doi.org/10.1109/sefet65155.2025.11255088
[research_viviand_1991]: https://doi.org/10.1007/978-3-642-84580-2_7
[research_vlach_2014]: https://doi.org/10.1007/978-3-319-02294-9_63
[research_voake_nermoen_2024]: https://doi.org/10.2139/ssrn.4765327
[research_vogel_kelkar_2009]: https://doi.org/10.2514/6.2009-7383
[research_voland_1990]: https://doi.org/10.2514/6.1990-2340
[research_voland_auslender_1999]: https://doi.org/10.2514/6.1999-4848
[research_volkov_2023]: https://doi.org/10.5772/intechopen.109268
[research_volpiani_2021]: https://doi.org/10.1007/s00193-021-01018-6
[research_voneckartsberg_goldman_2025]: https://doi.org/10.52202/083090-0116
[research_vonelbe_1955]: https://doi.org/10.1016/s0082-0784(55)80015-x
[research_vonlavante_kallenberg_2000]: https://doi.org/10.1007/978-3-642-59686-5_25
[research_votta_ranuzzi_2011]: https://doi.org/10.5772/17298
[research_vuchuru_dinda_2024]: https://doi.org/10.1016/j.joei.2024.101621
[research_wachter_sachs_2006]: https://doi.org/10.1111/j.1934-6093.2006.tb00282.x
[research_wada_2026]: https://doi.org/10.1201/9781003760528-11
[research_wagner_dale_1985]: https://doi.org/10.21236/ada379715
[research_wagner_valdivia_2007]: https://doi.org/10.2514/6.2007-4352
[research_wagner_yuceil_2008]: https://doi.org/10.2514/6.2008-3849
[research_wagner_yuceil_2009]: https://doi.org/10.2514/6.2009-4209
[research_wagner_yuceil_2010]: https://doi.org/10.2514/1.j050037
[research_waidmann_brummund_2024]: https://doi.org/10.1201/9780203735138-143
[research_wainwright_1962]: https://doi.org/10.21236/ad0297175
[research_wakamatsu_kuno_2009]: https://doi.org/10.5796/electrochemistry.77.127
[research_walchner_1974]: https://doi.org/10.21236/ada007045
[research_walchner_sawyer_1967]: https://doi.org/10.21236/ad0657027
[research_walchner_sawyer_1969]: https://doi.org/10.21236/ad0700062
[research_walker_1949]: https://doi.org/10.4271/490123
[research_walker_1952]: https://doi.org/10.21236/ad0041745
[research_walker_1955]: https://doi.org/10.1017/s036839310011689x
[research_walker_kennedy_2006]: https://doi.org/10.2514/6.2006-7927
[research_walker_oberkampf_1991]: https://doi.org/10.2514/6.1991-321
[research_walker_rodgers_2008]: https://doi.org/10.2514/6.2008-2580
[research_walker_sherk_2008]: https://doi.org/10.2514/6.2008-2539
[research_walters_1984]: https://doi.org/10.21236/ada142645
[research_walters_1992]: https://doi.org/10.1016/b978-0-444-89732-9.50243-0
[research_waltrup_billig_1972]: https://doi.org/10.2514/6.1972-1181
[research_waltrup_billig_1980]: https://doi.org/10.2514/6.1980-1284
[research_waltrup_billig_1981]: https://doi.org/10.2514/3.28060
[research_waltrup_white_1996]: https://doi.org/10.2514/6.1996-3152
[research_wan_chen_2022]: https://doi.org/10.1109/isas55863.2022.9757294
[research_wan_wang_2012]: https://doi.org/10.2514/6.2012-5965
[research_wang_1998]: https://doi.org/10.2514/6.1998-1842
[research_wang_1998_b]: https://doi.org/10.21236/ada391459
[research_wang_2004]: https://doi.org/10.21236/ada422042
[research_wang_2004_b]: https://doi.org/10.21236/ada430011
[research_wang_2007]: https://doi.org/10.21236/ada464234
[research_wang_2014]: https://doi.org/10.1007/978-3-662-44365-1_3
[research_wang_2014_b]: https://doi.org/10.1007/978-3-662-44365-1_4
[research_wang_2017]: https://doi.org/10.2514/6.2017-2236
[research_wang_2019]: https://doi.org/10.2514/6.2019-0262
[research_wang_an_2025]: https://doi.org/10.1063/5.0295712
[research_wang_anthony_1959]: https://doi.org/10.2514/8.4766
[research_wang_cai_2016]: https://doi.org/10.2514/6.2016-1019
[research_wang_chang_2021]: https://doi.org/10.1063/5.0047665
[research_wang_chen_2018]: https://doi.org/10.1109/access.2018.2809515
[research_wang_chen_2025]: https://doi.org/10.1063/5.0268520
[research_wang_fan_2022]: https://doi.org/10.23919/jsee.2022.000019
[research_wang_fan_2023]: https://doi.org/10.1016/j.actaastro.2023.06.043
[research_wang_fang_2006]: https://doi.org/10.1016/j.fuel.2006.02.011
[research_wang_feng_2007]: https://doi.org/10.1109/iciea.2007.4318625
[research_wang_feng_2022]: https://doi.org/10.23919/ccc55666.2022.9902115
[research_wang_feng_2025]: https://doi.org/10.1016/j.energy.2024.134166
[research_wang_feng_2025_b]: https://doi.org/10.1016/j.ijheatmasstransfer.2025.127416
[research_wang_gan_2024]: https://doi.org/10.2139/ssrn.4899147
[research_wang_gao_2013]: https://doi.org/10.4028/www.scientific.net/amr.756-759.4626
[research_wang_ge_2013]: https://doi.org/10.1115/icone21-16503
[research_wang_guo_2013]: https://doi.org/10.1016/j.cja.2013.04.018
[research_wang_hao_2017]: https://doi.org/10.2514/6.2017-2222
[research_wang_he_2021]: https://doi.org/10.1016/j.actaastro.2021.06.050
[research_wang_he_2025]: https://doi.org/10.1371/journal.pone.0328630
[research_wang_hou_2018]: https://doi.org/10.1088/1757-899x/449/1/012006
[research_wang_hou_2019]: https://doi.org/10.1109/access.2019.2913989
[research_wang_hou_2019_b]: https://doi.org/10.1109/access.2018.2885597
[research_wang_huang_2023]: https://doi.org/10.1016/j.ast.2023.108309
[research_wang_huang_2026]: https://doi.org/10.2139/ssrn.6926150
[research_wang_jin_2022]: https://doi.org/10.3390/atmos13111891
[research_wang_le_2000]: https://doi.org/10.1007/s11630-000-0073-3
[research_wang_li_2017]: https://doi.org/10.2514/6.2017-2335
[research_wang_li_2017_b]: https://doi.org/10.1109/ccdc.2017.7979050
[research_wang_li_2020]: https://doi.org/10.1051/jnwpu/20203810170
[research_wang_li_2025]: https://doi.org/10.1109/cac67268.2025.11487377
[research_wang_li_2026]: https://doi.org/10.1016/j.combustflame.2025.114590
[research_wang_liu_2012]: https://doi.org/10.4028/www.scientific.net/amm.232.194
[research_wang_liu_2015]: https://doi.org/10.1109/chicc.2015.7259715
[research_wang_liu_2023]: https://doi.org/10.1016/j.fuel.2022.125732
[research_wang_liu_2025]: https://doi.org/10.1080/01457632.2025.2571269
[research_wang_liu_2025_b]: https://doi.org/10.1016/j.tsep.2025.103659
[research_wang_liu_2026]: https://doi.org/10.1016/j.ast.2026.111723
[research_wang_liu_2026_b]: https://doi.org/10.1016/j.actaastro.2025.11.017
[research_wang_liu_2026_c]: https://doi.org/10.1109/fasta70174.2026.11549484
[research_wang_liu_2026_d]: https://doi.org/10.3390/jmse14161472
[research_wang_luo_2022]: https://doi.org/10.3390/app122110734
[research_wang_ma_2024]: https://doi.org/10.1109/isas61044.2024.10552537
[research_wang_pan_2018]: https://doi.org/10.1088/1742-6596/1064/1/012001
[research_wang_prakash_2024]: https://doi.org/10.1063/5.0190060
[research_wang_qin_2017]: https://doi.org/10.2514/6.2017-2376
[research_wang_rajan_2026]: https://doi.org/10.2514/6.2026-4175
[research_wang_song_2017]: https://doi.org/10.1016/j.actaastro.2017.08.014
[research_wang_sun_2012]: https://doi.org/10.1007/s10494-012-9434-8
[research_wang_tang_2025]: https://doi.org/10.1088/1742-6596/3041/1/012024
[research_wang_tang_2025_b]: https://doi.org/10.23919/ccc64809.2025.11179003
[research_wang_vohs_2024]: https://doi.org/10.1016/j.fuel.2023.129780
[research_wang_wang_1997]: https://doi.org/10.2514/6.1997-2944
[research_wang_wang_2013]: https://doi.org/10.1016/j.proci.2012.06.049
[research_wang_wang_2013_b]: https://doi.org/10.1016/j.ijhydene.2013.06.132
[research_wang_wang_2013_c]: https://doi.org/10.1007/s11431-013-5198-1
[research_wang_wang_2013_d]: https://doi.org/10.1007/s00231-013-1227-7
[research_wang_wang_2013_e]: https://doi.org/10.1016/j.ijhydene.2013.02.100
[research_wang_wang_2014]: https://doi.org/10.2514/1.b35289
[research_wang_wang_2020]: https://doi.org/10.1109/auteee50969.2020.9315589
[research_wang_wang_2023]: https://doi.org/10.2514/1.j062051
[research_wang_wang_2023_b]: https://doi.org/10.1017/aer.2023.19
[research_wang_wang_2023_c]: https://doi.org/10.2514/1.a35390
[research_wang_wang_2024]: https://doi.org/10.3390/app14114916
[research_wang_wang_2024_b]: https://doi.org/10.1063/5.0212969
[research_wang_wang_2024_c]: https://doi.org/10.1109/cac63892.2024.10865158
[research_wang_wang_2024_d]: https://doi.org/10.1038/s41598-024-61900-y
[research_wang_wang_2024_e]: https://doi.org/10.1016/j.actaastro.2024.01.002
[research_wang_wu_2015]: https://doi.org/10.1007/s11071-015-2083-4
[research_wang_wu_2017]: https://doi.org/10.1016/j.ast.2017.03.005
[research_wang_xia_2022]: https://doi.org/10.1109/oncon56984.2022.10126719
[research_wang_xiao_2016]: https://doi.org/10.1016/j.ast.2016.07.004
[research_wang_xie_2011]: https://doi.org/10.2514/6.2011-2306
[research_wang_xin_2022]: https://doi.org/10.1016/j.actaastro.2022.07.057
[research_wang_xin_2023]: https://doi.org/10.1016/j.euromechflu.2023.04.013
[research_wang_xu_2012]: https://doi.org/10.1109/isdea.2012.641
[research_wang_xu_2020]: https://doi.org/10.1360/sst-2020-0211
[research_wang_xu_2023]: https://doi.org/10.2139/ssrn.4435085
[research_wang_xu_2024]: https://doi.org/10.1017/jfm.2023.988
[research_wang_xue_2019]: https://doi.org/10.2514/1.j057352
[research_wang_yang_2020]: https://doi.org/10.1016/j.fuproc.2019.106229
[research_wang_yao_2024]: https://doi.org/10.2514/6.2024-4412
[research_wang_yao_2024_b]: https://doi.org/10.2514/6.2024-4412.c1
[research_wang_yao_2025]: https://doi.org/10.2514/1.j064599
[research_wang_yao_2025_b]: https://doi.org/10.1109/aim64088.2025.11175761
[research_wang_yu_1996]: https://doi.org/10.1007/bf02653230
[research_wang_zakkay_1980]: https://doi.org/10.2514/6.1980-4
[research_wang_zhai_2023]: https://doi.org/10.3390/en16104196
[research_wang_zhang_1992]: https://doi.org/10.1016/b978-0-444-89732-9.50035-2
[research_wang_zhang_2005]: https://doi.org/10.2514/6.2005-24
[research_wang_zhang_2017]: https://doi.org/10.1109/ccsse.2017.8087909
[research_wang_zhang_2021]: https://doi.org/10.2514/1.a34728
[research_wang_zhang_2022]: https://doi.org/10.1061/(asce)as.1943-5525.0001374
[research_wang_zhang_2023]: https://doi.org/10.1109/yac59482.2023.10401618
[research_wang_zhang_2025]: https://doi.org/10.2139/ssrn.5151593
[research_wang_zhang_2026]: https://doi.org/10.1016/j.ast.2026.111678
[research_wang_zhao_2022]: https://doi.org/10.1016/j.ast.2022.107883
[research_wang_zhao_2023]: https://doi.org/10.1016/j.ast.2023.108420
[research_wang_zhao_2025]: https://doi.org/10.1016/j.eswa.2025.126782
[research_ward_1988]: https://doi.org/10.2514/6.1988-2116
[research_ward_baltakis_1977]: https://doi.org/10.21236/adb018467
[research_ward_hewitt_1988]: https://doi.org/10.2514/6.1988-3069
[research_ward_myers_1967]: https://doi.org/10.21236/ad0815090
[research_ward_smart_2026]: https://doi.org/10.2514/6.2026-5107
[research_warning_mcquilling_2022]: https://doi.org/10.2514/6.2022-0603
[research_warsop_crowther_2019]: https://doi.org/10.2514/6.2019-0282
[research_wartemann_ludeke_2009]: https://doi.org/10.2514/6.2009-7202
[research_washington_humphrey_1969]: https://doi.org/10.21236/ad0699359
[research_wassel_shih_1984]: https://doi.org/10.2514/6.1984-631
[research_wasserman_1952]: https://doi.org/10.21236/ad0015929
[research_waszkowski_pisani_2025]: https://doi.org/10.2514/6.2025-99583
[research_watanabe_ishimoto_1996]: https://doi.org/10.2514/6.1996-4527
[research_watari_hirabayashi_2006]: https://doi.org/10.2514/6.2006-8047
[research_watmuff_smits_1987]: https://doi.org/10.21236/ada186366
[research_watson_1969]: https://doi.org/10.2514/6.1969-278
[research_watt_aronson_1964]: https://doi.org/10.21236/ad0447153
[research_waverider_aero_analysis]: https://ntrs.nasa.gov/citations/19930017904
[research_waverider_aerodynamics_1986]: https://doi.org/10.2514/5.9781600861871.0399.0414
[research_waverider_cfd_interpretation]: https://ntrs.nasa.gov/citations/20040129597
[research_waverider_derived_performance]: https://ntrs.nasa.gov/citations/20040111231
[research_way_sescu_2024]: https://doi.org/10.2514/6.2024-4107
[research_weatherill_zartarian_1958]: https://doi.org/10.21236/ad0142154
[research_weatherston_1969]: https://doi.org/10.2514/6.1969-332
[research_weaver_hunsaker_2025]: https://doi.org/10.2514/6.2025-0224
[research_weber_karemaa_1972]: https://doi.org/10.1115/72-gt-106
[research_weber_kriven_1997]: https://doi.org/10.21236/ada333768
[research_weeks_1969]: https://doi.org/10.2514/6.1969-331
[research_weeks_1970]: https://doi.org/10.2514/3.5926
[research_weeratunga_menon_1993]: https://doi.org/10.2514/6.1993-1914
[research_wegener_1977]: https://doi.org/10.21236/ada038280
[research_wegener_lobb_1952]: https://doi.org/10.21236/ad0012779
[research_wei_hu_2019]: https://doi.org/10.23919/chicc.2019.8866177
[research_wei_peers_2012]: https://doi.org/10.2514/6.2012-4581
[research_wei_wang_2016]: https://doi.org/10.2316/p.2016.830-040
[research_wei_ye_2026]: https://doi.org/10.1016/j.ast.2026.113529
[research_wei_zhang_2024]: https://doi.org/10.1016/j.cja.2024.04.023
[research_weidner_1980]: https://doi.org/10.2514/6.1980-111
[research_weidner_small_1976]: https://doi.org/10.2514/6.1976-755
[research_weidnerjohnp_1992]: https://ntrs.nasa.gov/citations/19920012279
[research_weidong_xianlin_2015]: https://doi.org/10.1109/chicc.2015.7260001
[research_weiland_2019]: https://doi.org/10.1007/s12567-019-00264-w
[research_weiler_derbidge_1972]: https://doi.org/10.21236/ad0783359
[research_weilmuenster_gnoffo_1995]: https://doi.org/10.2514/6.1995-1850
[research_weilmuenster_gnoffo_1996]: https://doi.org/10.2514/6.1996-609
[research_weimer_2022]: https://doi.org/10.33548/scientia821
[research_weinacht_2014]: https://doi.org/10.21236/ada607593
[research_weinberg_1952]: https://doi.org/10.1016/s0002-9378(16)38893-7
[research_weirich_fogarty_1996]: https://doi.org/10.2514/6.1996-4594
[research_weissman_1990]: https://doi.org/10.2514/6.1990-527
[research_weiwei_leping_2013]: https://doi.org/10.1109/ccdc.2013.6560984
[research_wellswilliaml_1987]: https://ntrs.nasa.gov/citations/19870062319
[research_welsh_lawrence_1979]: https://doi.org/10.21236/ada075526
[research_wen_sun_2027]: https://doi.org/10.1016/j.ast.2026.113659
[research_wenbiao_dong_2014]: https://doi.org/10.1109/cgncc.2014.7007458
[research_wendel_gaitonde_2025]: https://doi.org/10.2514/6.2025-3617
[research_wendel_gaitonde_2026]: https://doi.org/10.2514/6.2026-4488
[research_wendt]: https://doi.org/10.14264/366370
[research_wenfeng_peng_2017]: https://doi.org/10.23919/chicc.2017.8027899
[research_wenkai_hou_2017]: https://doi.org/10.2514/6.2017-4004
[research_wenkai_hou_2017_b]: https://doi.org/10.2514/6.2017-2156
[research_wenkai_zhongxi_2017]: https://doi.org/10.23919/chicc.2017.8027732
[research_wepler_huhn_2001]: https://doi.org/10.1007/978-3-540-44567-8_13
[research_west_2005]: https://doi.org/10.21236/ada434078
[research_west_bynum_2024]: https://doi.org/10.2514/1.b39108
[research_westinghouseelectriccorppittsburghpa_1967]: https://doi.org/10.21236/ad0824924
[research_wexler_idan_2026]: https://doi.org/10.2514/6.2026-5048
[research_weyl_1998]: https://doi.org/10.1007/978-1-4612-2218-7_12
[research_white_1993]: https://doi.org/10.2514/6.1993-971
[research_white_2004]: https://doi.org/10.21236/ada430835
[research_white_andrikidis_1996]: https://doi.org/10.1103/physrevb.53.8145
[research_white_janssen_1983]: https://doi.org/10.2514/6.1983-1123
[research_white_rhie_1988]: https://doi.org/10.2514/6.1988-3077
[research_white_rhie_1992]: https://doi.org/10.2514/3.23471
[research_white_richardp_1961]: https://doi.org/10.21236/ad0328509
[research_whitehurst_krauss_1992]: https://doi.org/10.2514/6.1992-3424
[research_whitney_1963]: https://doi.org/10.21236/ad0423790
[research_whitside]: https://doi.org/10.14264/1e68f80
[research_wickham_alptekin_1999]: https://doi.org/10.2514/6.1999-2215
[research_wickham_engel_2002]: https://doi.org/10.2514/6.2002-3872
[research_wickham_engel_2005]: https://doi.org/10.2514/6.2005-3916
[research_wickham_engel_2008]: https://doi.org/10.2514/1.24336
[research_wideman_brown_1995]: https://doi.org/10.2514/3.12503
[research_wideman_miles_1994]: https://doi.org/10.2514/6.1994-314
[research_wiedemeier_siemers_1975]: https://doi.org/10.1002/chin.197507016
[research_wiese_annaswamy_2013]: https://doi.org/10.2514/6.2013-4514
[research_wieting_1990]: https://doi.org/10.2514/6.1990-5238
[research_wieting_guy_1976]: https://doi.org/10.2514/3.58649
[research_wilkinson_wilkinson_1997]: https://doi.org/10.2514/6.1997-1819
[research_wilks_2006]: https://doi.org/10.21236/ada447214
[research_willard_giel_2009]: https://doi.org/10.2514/6.2009-5184
[research_williams_1965]: https://doi.org/10.1016/b978-0-08-011074-5.50012-9
[research_williams_2021]: https://doi.org/10.4324/9781003179917-8
[research_williams_bartkowicz_2024]: https://doi.org/10.2514/6.2024-0562
[research_williams_bolender_2006]: https://doi.org/10.2514/6.2006-6647
[research_williams_davuluri_2026]: https://doi.org/10.2514/6.2026-2695
[research_williams_edwards_2001]: https://doi.org/10.2514/6.2001-4066
[research_williams_lewis_1975]: https://doi.org/10.21236/ada012877
[research_williamson_pascoe_2026]: https://doi.org/10.2514/6.2026-5003
[research_wilson_1966]: https://doi.org/10.21236/ad0632714
[research_wilson_1990]: https://doi.org/10.2514/6.1990-1381
[research_wilson_agarwal_2009]: https://doi.org/10.2514/6.2009-3836
[research_wilson_benson_1978]: https://doi.org/10.2514/6.1978-1053
[research_wilson_wright_1977]: https://doi.org/10.2514/6.1977-798
[research_wimber_1976]: https://doi.org/10.1063/1.322479
[research_wind_tunnel_2024]: https://doi.org/10.1016/c2018-0-02200-8
[research_windisch_reinartz_2012]: https://doi.org/10.2514/6.2012-5918
[research_wing]: https://doi.org/10.14264/0c95d3b
[research_wingfieldiii_2001]: https://doi.org/10.2514/6.2001-1815
[research_winkler_1952]: https://doi.org/10.21236/ad0001030
[research_winkler_1954]: https://doi.org/10.21236/ad0058826
[research_wise]: https://doi.org/10.14264/uql.2015.465
[research_witte_huebner_2003]: https://doi.org/10.2514/6.2003-4406
[research_wittliff_oconnor_1992]: https://doi.org/10.2514/6.1992-3906
[research_wittliff_wilson_1961]: https://doi.org/10.21236/ad0266413
[research_witzmann_2006]: https://doi.org/10.21236/ada444336
[research_wohlleben_schnell_1991]: https://doi.org/10.1007/978-1-4615-3338-2_50
[research_wolf_bossert_2001]: https://doi.org/10.2514/6.2001-4313
[research_wolf_mullen_1951]: https://doi.org/10.21236/ad0036130
[research_wolfe_1964]: https://doi.org/10.1016/b978-0-08-010580-2.50018-9
[research_wollrab_1966]: https://doi.org/10.21236/ad0651159
[research_woodward_glaser_1983]: https://doi.org/10.2514/6.1983-1415
[research_woodward_mesrobain_1953]: https://doi.org/10.21236/ad0008410
[research_wright_2015]: https://doi.org/10.1080/08929882.2015.1088734
[research_wright_2022]: https://doi.org/10.55163/qvhv3959
[research_wright_foley_2000]: https://doi.org/10.2514/6.2000-3885
[research_wu_cheng_2005]: https://doi.org/10.1088/0022-3727/38/24/006
[research_wu_ding_2013]: https://doi.org/10.4028/www.scientific.net/amm.390.370
[research_wu_fan_2023]: https://doi.org/10.1117/12.3006407
[research_wu_fan_2026]: https://doi.org/10.1017/jfm.2026.11140
[research_wu_guo_2018]: https://doi.org/10.1155/2018/2198423
[research_wu_he_2022]: https://doi.org/10.2139/ssrn.4074438
[research_wu_laguarda_2024]: https://doi.org/10.21203/rs.3.rs-4189984/v1
[research_wu_lagurada_2026]: https://doi.org/10.2139/ssrn.6881193
[research_wu_lin_2020]: https://doi.org/10.1016/j.ceramint.2020.02.241
[research_wu_liu_2015]: https://doi.org/10.1109/cac.2015.7382480
[research_wu_song_2021]: https://doi.org/10.1016/j.actaastro.2021.04.015
[research_wu_wang_2015]: https://doi.org/10.1155/2015/506906
[research_wu_wang_2015_b]: https://doi.org/10.21595/jve.2015.15776
[research_wu_wei_2022]: https://doi.org/10.3390/app13010480
[research_wu_wei_2023]: https://doi.org/10.1016/j.actaastro.2022.11.034
[research_wu_wu_2026]: https://doi.org/10.1016/j.applthermaleng.2026.130740
[research_wu_xiao_2009]: https://doi.org/10.5539/mas.v3n2p117
[research_wu_yu_2018]: https://doi.org/10.5220/0006969302880293
[research_wu_yuan_2025]: https://doi.org/10.3934/jimo.2025010
[research_wulff_zoellner_1991]: https://doi.org/10.2514/6.1991-2852
[research_wuliaoni_wangmengmeng_2012]: https://doi.org/10.1049/cp.2012.1330
[research_wurster_1981]: https://doi.org/10.2514/6.1981-1090
[research_wurster_marrone_1962]: https://doi.org/10.21236/ad0273865
[research_wygle_1981]: https://doi.org/10.2514/6.1981-2378
[research_x43_technology]: https://ntrs.nasa.gov/citations/20050239566
[research_xi_yao_2026]: https://doi.org/10.1016/j.ast.2026.113378
[research_xia_chen_2020]: https://doi.org/10.1016/j.neucom.2019.10.038
[research_xia_han_2026]: https://doi.org/10.1063/5.0332049
[research_xia_sun_2025]: https://doi.org/10.3390/aerospace12030173
[research_xianlinhuang_dongmingge_2010]: https://doi.org/10.1109/isscaa.2010.5633123
[research_xianyu_xiaoshan_2007]: https://doi.org/10.2514/6.2007-5421
[research_xianyu_xiaoshan_2007_b]: https://doi.org/10.1016/s1000-9361(07)60072-7
[research_xiao_jin_2026]: https://doi.org/10.2139/ssrn.6103773
[research_xiao_liu_2006]: https://doi.org/10.2514/6.2006-8090
[research_xiao_yang_2025]: https://doi.org/10.2139/ssrn.5902345
[research_xiao_yue_2008]: https://doi.org/10.2514/6.2008-2634
[research_xiaoqing_zhongxi_2010]: https://doi.org/10.2514/6.2010-7931
[research_xiaoqing_zhongxi_2011]: https://doi.org/10.1017/s0001924000005844
[research_xie_dong_2020]: https://doi.org/10.1016/j.ast.2020.106170
[research_xie_ge_2016]: https://doi.org/10.1016/j.ast.2016.03.025
[research_xie_li_2025]: https://doi.org/10.1049/icp.2024.3367
[research_xie_zeng_2026]: https://doi.org/10.2139/ssrn.6770201
[research_xie_zhuang_2021]: https://doi.org/10.1109/access.2021.3092515
[research_xin_2023]: https://doi.org/10.1109/icccs57501.2023.10150541
[research_xin_li_2025]: https://doi.org/10.3390/aerospace12111020
[research_xin_zhang_2011]: https://doi.org/10.1109/iceceng.2011.6057682
[research_xin_zhang_2023]: https://doi.org/10.1109/icmae59650.2023.10424510
[research_xing_ruan_2017]: https://doi.org/10.1016/j.ast.2016.11.007
[research_xinwang_dongzhufeng_2008]: https://doi.org/10.1109/isscaa.2008.4776354
[research_xinwang_shijiesun_2010]: https://doi.org/10.1109/ccdc.2010.5498090
[research_xiong_bai_2019]: https://doi.org/10.1007/978-3-319-91017-8_133
[research_xiong_qin_2022]: https://doi.org/10.1155/2022/9931498
[research_xiong_wang_2017]: https://doi.org/10.2514/1.b36291
[research_xiong_zheng_2021]: https://doi.org/10.1016/j.ast.2020.106414
[research_xiongluo_zengqisun_2008]: https://doi.org/10.1109/wcica.2008.4593311
[research_xu_2015]: https://doi.org/10.1007/s11071-015-1958-8
[research_xu_cai_2011]: https://doi.org/10.1109/ist.2011.5962219
[research_xu_chang_2018]: https://doi.org/10.1016/j.euromechflu.2018.07.015
[research_xu_cheng_2023]: https://doi.org/10.1016/j.energy.2023.127488
[research_xu_fang_2022]: https://doi.org/10.1145/3547578.3547593
[research_xu_khalid_2003]: https://doi.org/10.1080/1061856031000083477
[research_xu_kim_1996]: https://doi.org/10.1080/10618569608940763
[research_xu_lin_2021]: https://doi.org/10.1016/j.applthermaleng.2021.117616
[research_xu_luan_2023]: https://doi.org/10.1109/icmae59650.2023.10424615
[research_xu_mao]: https://doi.org/10.1007/3-540-31801-1_23
[research_xu_mirmirani_2004]: https://doi.org/10.2514/1.12596
[research_xu_sun_2012]: https://doi.org/10.1049/iet-cta.2011.0026
[research_xu_sun_2018]: https://doi.org/10.1016/j.ijthermalsci.2018.06.008
[research_xu_wang_2012]: https://doi.org/10.1007/s11071-012-0451-x
[research_xu_wang_2019]: https://doi.org/10.1016/j.cja.2019.04.010
[research_xu_wang_2022]: https://doi.org/10.1016/j.ast.2022.107884
[research_xu_wang_2022_b]: https://doi.org/10.1016/j.ast.2022.107621
[research_xu_wu_2015]: https://doi.org/10.1117/12.2216033
[research_xu_yu_2017]: https://doi.org/10.2514/6.2017-2112
[research_xu_zhang_2015]: https://doi.org/10.1016/j.neucom.2014.11.059
[research_xudongliu_lincheng_2016]: https://doi.org/10.1109/cgncc.2016.7828785
[research_xue_bostic_1994]: https://doi.org/10.2514/6.1994-1594
[research_xue_guodong_2018]: https://doi.org/10.1109/gncc42960.2018.9018943
[research_xue_haibin_2017]: https://doi.org/10.1108/aeat-01-2015-0007
[research_xue_huang_2023]: https://doi.org/10.1049/rsn2.12400
[research_xue_wei_2017]: https://doi.org/10.1016/j.ijheatmasstransfer.2017.06.074
[research_xumingliang_liuluhua_2010]: https://doi.org/10.1109/isscaa.2010.5633205
[research_yager_2013]: https://doi.org/10.21236/ada588839
[research_yahalom_1971]: https://doi.org/10.21236/ad0728233
[research_yahui_yitao_2021]: https://doi.org/10.1088/1742-6596/1738/1/012084
[research_yakimov_2018]: https://doi.org/10.1007/978-3-319-78217-1_1
[research_yakimov_2018_b]: https://doi.org/10.1007/978-3-319-78217-1_2
[research_yakimov_2018_c]: https://doi.org/10.1007/978-3-319-78217-1_3
[research_yakubayev_gschwend_2026]: https://doi.org/10.2514/6.2026-1095
[research_yalong_guangbin_2014]: https://doi.org/10.1109/cgncc.2014.7007369
[research_yamamoto_kano_1996]: https://doi.org/10.2514/6.1996-2152
[research_yamamoto_kojima_2020]: https://doi.org/10.1016/j.ast.2019.105523
[research_yamato_okada_1988]: https://doi.org/10.2514/6.1988-2180
[research_yan_2013]: https://doi.org/10.2514/6.2013-530
[research_yan_2014]: https://doi.org/10.12720/joace.2.3.294-301
[research_yan_2023]: https://doi.org/10.21203/rs.3.rs-2749229/v1
[research_yan_bing_2014]: https://doi.org/10.1016/j.actaastro.2014.06.006
[research_yan_fan_2017]: https://doi.org/10.23919/chicc.2017.8027935
[research_yan_fan_2022]: https://doi.org/10.3390/aerospace10010002
[research_yan_fu_2026]: https://doi.org/10.2139/ssrn.6248882
[research_yan_liu_2016]: https://doi.org/10.2514/6.2016-3776
[research_yan_liu_2018]: https://doi.org/10.2514/1.j056107
[research_yan_liu_2022]: https://doi.org/10.1016/j.ast.2022.107637
[research_yan_pan_2008]: https://doi.org/10.2514/6.2008-176
[research_yan_shaohua_2016]: https://doi.org/10.1016/j.actaastro.2016.07.025
[research_yan_sun_2024]: https://doi.org/10.1016/j.proci.2024.105306
[research_yan_tian_2025]: https://doi.org/10.1016/j.combustflame.2025.114485
[research_yan_wang_2012]: https://doi.org/10.2514/6.2012-5897
[research_yan_wu_2020]: https://doi.org/10.1016/j.actaastro.2020.04.003
[research_yan_yuzhen_2014]: https://doi.org/10.2514/6.2014-3748
[research_yan_yuzhen_2014_b]: https://doi.org/10.2514/6.2014-3749
[research_yan_zhang_2026]: https://doi.org/10.1016/j.istruc.2026.111138
[research_yan_zhu_2025]: https://doi.org/10.1063/5.0286055
[research_yanagihara_nishizawa_2003]: https://doi.org/10.2514/6.2003-6980
[research_yanbinbin_lucunkan_2009]: https://doi.org/10.1109/iciea.2009.5138209
[research_yang_2021]: https://doi.org/10.1007/978-981-33-4737-3_2
[research_yang_2021_b]: https://doi.org/10.1007/978-981-33-4737-3_5
[research_yang_2021_c]: https://doi.org/10.1007/978-981-33-4737-3_8
[research_yang_2021_d]: https://doi.org/10.1007/978-981-33-4737-3_6
[research_yang_2021_e]: https://doi.org/10.1007/978-981-33-4737-3
[research_yang_bao_2017]: https://doi.org/10.1016/j.cja.2017.02.013
[research_yang_cai_2026]: https://doi.org/10.1016/j.combustflame.2026.115090
[research_yang_chang_2014]: https://doi.org/10.1155/2014/614189
[research_yang_chang_2014_b]: https://doi.org/10.1016/j.energy.2014.08.052
[research_yang_cheng_2026]: https://doi.org/10.3390/aerospace13050477
[research_yang_culick_1986]: https://doi.org/10.1080/00102208608923839
[research_yang_duan_2014]: https://doi.org/10.2514/6.2014-1393
[research_yang_gou_2025]: https://doi.org/10.2139/ssrn.5201417
[research_yang_lee_2014]: https://doi.org/10.2514/1.b35025
[research_yang_lee_2016]: https://doi.org/10.6108/kspe.2016.20.6.083
[research_yang_lee_2020]: https://doi.org/10.6108/kspe.2020.24.5.013
[research_yang_li_2013]: https://doi.org/10.1109/taes.2013.6494412
[research_yang_li_2017]: https://doi.org/10.2991/ifmca-16.2017.136
[research_yang_li_2023]: https://doi.org/10.3390/pr11010263
[research_yang_lin_2024]: https://doi.org/10.1016/j.applthermaleng.2024.122880
[research_yang_lin_2025]: https://doi.org/10.2139/ssrn.5210331
[research_yang_liu_2017]: https://doi.org/10.1016/j.actaastro.2016.11.043
[research_yang_liu_2025]: https://doi.org/10.3390/aerospace12090763
[research_yang_qi_2016]: https://doi.org/10.1109/chicc.2016.7554207
[research_yang_tian_2024]: https://doi.org/10.1063/5.0212881
[research_yang_wang_2015]: https://doi.org/10.3390/atmos6111633
[research_yang_wang_2017]: https://doi.org/10.1063/1.4972767
[research_yang_wang_2021]: https://doi.org/10.23919/ccc52363.2021.9549492
[research_yang_wang_2024]: https://doi.org/10.1016/j.tsep.2024.102947
[research_yang_wang_2025]: https://doi.org/10.1063/5.0257788
[research_yang_wang_2026]: https://doi.org/10.1016/j.ijheatfluidflow.2026.110376
[research_yang_xiao_2026]: https://doi.org/10.1016/j.ast.2026.111922
[research_yang_xie_2024]: https://doi.org/10.1063/5.0222577
[research_yang_xie_2025]: https://doi.org/10.1016/j.actaastro.2025.07.024
[research_yang_xie_2025_b]: https://doi.org/10.2139/ssrn.5148232
[research_yang_yu_2014]: https://doi.org/10.4028/www.scientific.net/amm.716-717.724
[research_yang_yuan_2013]: https://doi.org/10.1109/icicip.2013.6568142
[research_yang_yuan_2024]: https://doi.org/10.1016/j.compstruct.2024.118337
[research_yang_yuhyihwu_1994]: https://doi.org/10.1016/s0082-0784(06)80806-4
[research_yang_zhang_2025]: https://doi.org/10.7498/aps.74.20251170
[research_yang_zhao_2014]: https://doi.org/10.1080/00207179.2014.896477
[research_yang_zhao_2024]: https://doi.org/10.2139/ssrn.4713390
[research_yang_zhou_2020]: https://doi.org/10.1016/j.cja.2019.07.021
[research_yankui_dongjun_2005]: https://doi.org/10.2514/6.2005-6040
[research_yao_bao_2009]: https://doi.org/10.2514/6.2009-5431
[research_yao_bao_2009_b]: https://doi.org/10.1243/09544100jaero618
[research_yao_chaoyang_2017]: https://doi.org/10.1109/ccdc.2017.7979314
[research_yao_cui_2017]: https://doi.org/10.2514/6.2017-2315
[research_yao_hu_2023]: https://doi.org/10.5220/0012150900003562
[research_yao_petty_2006]: https://doi.org/10.1080/10618560600909945
[research_yao_thomas_2001]: https://doi.org/10.1007/s001620050144
[research_yao_wang_2023]: https://doi.org/10.1016/j.ijthermalsci.2022.107967
[research_yao_wu_2025]: https://doi.org/10.1049/icp.2025.3470
[research_yao_xia_2023]: https://doi.org/10.20944/preprints202308.0039.v1
[research_yaosheng_2018]: https://doi.org/10.1109/icomssc45026.2018.8941700
[research_yarantsev_firsov_2019]: https://doi.org/10.2514/6.2019-0676
[research_yarng_guan_1988]: https://doi.org/10.2514/3.20283
[research_yatsukhno_2020]: https://doi.org/10.33257/phchgd.21.2.907
[research_yatsuyanagi_2009]: https://doi.org/10.2322/tjsass.51.259
[research_yechout_1988]: https://doi.org/10.2514/6.1988-2201
[research_yeh_tsai_2017]: https://doi.org/10.1021/acs.iecr.7b01006
[research_yeh_veals_2023]: https://doi.org/10.21236/ad1182193
[research_yeneriz_davis_1989]: https://doi.org/10.2514/6.1989-2548
[research_yeneriz_davis_1991]: https://doi.org/10.2514/6.1991-2097
[research_yentsch_gaitonde_2013]: https://doi.org/10.2514/6.2013-3753
[research_yentsch_gaitonde_2014]: https://doi.org/10.2514/6.2014-0625
[research_yergensen_rhea_1988]: https://doi.org/10.2514/6.1988-2200
[research_yi_jianhan_2009]: https://doi.org/10.2514/6.2009-7404
[research_yin_nakamura_2024]: https://doi.org/10.1063/5.0245100
[research_yin_qin_2017]: https://doi.org/10.2514/6.2017-2304
[research_yin_zeng_2024]: https://doi.org/10.2139/ssrn.4930788
[research_ying_fang_2018]: https://doi.org/10.23919/chicc.2018.8483244
[research_yip_strawa_1990]: https://doi.org/10.2514/6.1990-2339
[research_yonggang_yang_2019]: https://doi.org/10.1016/j.actaastro.2019.08.005
[research_yongsheng_ruisen_2005]: https://doi.org/10.1631/jzus.2005.a0632
[research_yoon_chung_1996]: https://doi.org/10.2514/6.1996-2005
[research_yoonbokhyun_rasmussenmauricel_1991]: https://ntrs.nasa.gov/citations/19930005578
[research_yorita_2016]: https://doi.org/10.2514/6.2016-0649
[research_yoshikawa_pan_1998]: https://doi.org/10.21236/ada341698
[research_yost_frame_2015]: https://doi.org/10.21236/ada625466
[research_you_liang_2009]: https://doi.org/10.2514/6.2009-4214
[research_you_liang_2009_b]: https://doi.org/10.2514/6.2009-4215
[research_you_luedeke_2013]: https://doi.org/10.1016/j.proci.2012.10.001
[research_you_zhu_2009]: https://doi.org/10.2514/6.2009-7421
[research_young_1966]: https://doi.org/10.1038/2091163b0
[research_young_balar_2006]: https://doi.org/10.2514/6.2006-1377
[research_young_goldstein_1999]: https://doi.org/10.2514/6.1999-3379
[research_young_kokan_2006]: https://doi.org/10.2514/6.2006-8099
[research_youquanchang_2009]: https://doi.org/10.1109/impact.2009.5382297
[research_youssef_reiman_2008]: https://doi.org/10.2514/6.2008-7466
[research_youssef_reiman_2009]: https://doi.org/10.2514/6.2009-6185
[research_yu_2026]: https://doi.org/10.46226/jss.2026.7.33.2.327
[research_yu_ao_2021]: https://doi.org/10.1109/icceic54227.2021.00034
[research_yu_chang_2007]: https://doi.org/10.2514/1.24640
[research_yu_chen_2011]: https://doi.org/10.2514/6.2011-6714
[research_yu_huang_2015]: https://doi.org/10.2514/6.2015-3612
[research_yu_kim_2005]: https://doi.org/10.21236/ada439707
[research_yu_li_2002]: https://doi.org/10.1080/713712992
[research_yu_liu_2022]: https://doi.org/10.1016/j.precisioneng.2022.07.006
[research_yu_newman_2003]: https://doi.org/10.2514/6.2003-1966
[research_yu_ni_2022]: https://doi.org/10.1016/j.infrared.2022.104020
[research_yu_schadow_1994]: https://doi.org/10.1016/0010-2180(94)90134-1
[research_yu_wang_2025]: https://doi.org/10.1109/cac67268.2025.11487716
[research_yu_wang_2025_b]: https://doi.org/10.1007/s12567-025-00672-1
[research_yu_wilson_1999]: https://doi.org/10.2514/6.1999-2638
[research_yu_zhang_2014]: https://doi.org/10.1109/chicc.2014.6895661
[research_yu_zhou_2022]: https://doi.org/10.1016/j.actaastro.2022.02.025
[research_yuan_gao_2026]: https://doi.org/10.3390/aerospace13080705
[research_yuan_kawano_2019]: https://doi.org/10.1109/iros40897.2019.8968281
[research_yuan_liu_2026]: https://doi.org/10.1063/5.0338458
[research_yuan_sivasankaran_2020]: https://doi.org/10.1016/j.applthermaleng.2019.114525
[research_yuceil_valdivia_2009]: https://doi.org/10.2514/6.2009-4022
[research_yue_guiping_2010]: https://doi.org/10.2514/6.2010-8087
[research_yue_lu_2017]: https://doi.org/10.1007/978-3-319-46213-4_72
[research_yue_wu_2016]: https://doi.org/10.1016/j.fuproc.2016.04.017
[research_yue_xiao_2009]: https://doi.org/10.2514/6.2009-7422
[research_yukhno_volkov_2021]: https://doi.org/10.1016/j.solidstatesciences.2021.106726
[research_yuli_naigangcui_2008]: https://doi.org/10.1109/isscaa.2008.4776361
[research_yulian_bin_2014]: https://doi.org/10.1109/ccdc.2014.6852297
[research_yumusak_eyi_2013]: https://doi.org/10.2514/6.2013-2693
[research_yun_cole_2022]: https://doi.org/10.2514/6.2022-0286.c1
[research_yun_cole_2022_b]: https://doi.org/10.2514/6.2022-0286
[research_yun_kim_2026]: https://doi.org/10.1016/j.ast.2026.111990
[research_yungster_paxson_2014]: https://doi.org/10.2514/6.2014-3728
[research_yushengtao_hsiehkwangchung_1988]: https://ntrs.nasa.gov/citations/19880040490
[research_zaehringer_heller_2003]: https://doi.org/10.2514/6.2003-7080
[research_zakharov_1994]: https://doi.org/10.4271/942122
[research_zalesaksr_1981]: https://doi.org/10.2514/6.1981-2405
[research_zanchetta_cain_1998]: https://doi.org/10.2514/6.1998-1525
[research_zander]: https://doi.org/10.14264/345636
[research_zapp_bermejomoreno_2026]: https://doi.org/10.2514/6.2026-0288
[research_zapp_bermejomoreno_2026_b]: https://doi.org/10.2514/6.2026-0288.c1
[research_zarillo_militello_1999]: https://doi.org/10.21236/ada362897
[research_zarlingo_1988]: https://doi.org/10.2514/6.1988-3070
[research_zartarian_1956]: https://doi.org/10.21236/ad0110592
[research_zartarian_hsu_1955]: https://doi.org/10.21236/ad0110591
[research_zeitoun_colas_1991]: https://doi.org/10.1007/978-3-642-76527-8_77
[research_zelinski_matthews_1960]: https://doi.org/10.1016/s0010-2180(60)80047-8
[research_zeng_luo_2026]: https://doi.org/10.1063/5.0335102
[research_zeng_wang_2025]: https://doi.org/10.1109/icus66297.2025.11294882
[research_zeng_wang_2026]: https://doi.org/10.1016/j.ast.2026.113306
[research_zeng_zhuang_2021]: https://doi.org/10.1109/icus52573.2021.9641452
[research_zerilli_armstrong_1992]: https://doi.org/10.1016/b978-0-444-89732-9.50058-3
[research_zettervall_fureby_2018]: https://doi.org/10.2514/6.2018-1146
[research_zha_knight_1998]: https://doi.org/10.2514/6.1998-3583
[research_zha_knight_1998_b]: https://doi.org/10.2514/2.2404
[research_zhai_qi_2016]: https://doi.org/10.1109/chicc.2016.7554394
[research_zhai_yang_2018]: https://doi.org/10.23919/chicc.2018.8483797
[research_zhai_yang_2020]: https://doi.org/10.1016/j.jfranklin.2020.03.002
[research_zhai_zhang_2020]: https://doi.org/10.1142/s0217979220400743
[research_zhang_2015]: https://doi.org/10.2514/6.2015-3647
[research_zhang_2020]: https://doi.org/10.1007/978-981-15-0727-4_8
[research_zhang_2020_b]: https://doi.org/10.1007/978-981-15-0727-4_9
[research_zhang_2020_c]: https://doi.org/10.1007/978-981-15-0727-4_7
[research_zhang_2020_d]: https://doi.org/10.1007/978-981-15-0727-4
[research_zhang_2020_e]: https://doi.org/10.1007/978-981-15-0727-4_3
[research_zhang_2020_f]: https://doi.org/10.1007/978-981-15-0727-4_5
[research_zhang_2020_g]: https://doi.org/10.1007/978-981-15-0727-4_2
[research_zhang_chang_2017]: https://doi.org/10.1016/j.actaastro.2017.01.031
[research_zhang_chen_2011]: https://doi.org/10.4028/www.scientific.net/amm.110-116.5223
[research_zhang_chen_2020]: https://doi.org/10.1007/s12650-020-00692-5
[research_zhang_chen_2023]: https://doi.org/10.1007/978-981-19-6613-2_436
[research_zhang_chen_2026]: https://doi.org/10.2139/ssrn.6359187
[research_zhang_chen_2026_b]: https://doi.org/10.3390/aerospace13020173
[research_zhang_chen_2026_c]: https://doi.org/10.1007/s42401-026-00511-z
[research_zhang_deng_2026]: https://doi.org/10.1088/1742-6596/3254/3/032040
[research_zhang_ding_2023]: https://doi.org/10.1177/00202940231154856
[research_zhang_fan_2012]: https://doi.org/10.4028/www.scientific.net/amr.562-564.1682
[research_zhang_feng_2016]: https://doi.org/10.1016/j.ijhydene.2016.03.176
[research_zhang_feng_2016_b]: https://doi.org/10.2514/1.b35887
[research_zhang_ge_2021]: https://doi.org/10.1080/19392699.2021.1990892
[research_zhang_he_2017]: https://doi.org/10.23919/chicc.2017.8028140
[research_zhang_huang_2022]: https://doi.org/10.1109/yac57282.2022.10023597
[research_zhang_jin_2021]: https://doi.org/10.1007/s11771-021-4604-2
[research_zhang_jing_2023]: https://doi.org/10.1016/j.applthermaleng.2022.119384
[research_zhang_jingfeng_2025]: https://doi.org/10.2139/ssrn.5233781
[research_zhang_ju_2023]: https://doi.org/10.1364/oe.496783
[research_zhang_li_2016]: https://doi.org/10.1016/j.ins.2016.02.012
[research_zhang_li_2023]: https://doi.org/10.1049/icp.2022.2954
[research_zhang_li_2025]: https://doi.org/10.1109/taes.2025.3539639
[research_zhang_liao_2026]: https://doi.org/10.2139/ssrn.6025085
[research_zhang_liu_2017]: https://doi.org/10.23919/chicc.2017.8027759
[research_zhang_liu_2018]: https://doi.org/10.1016/j.actaastro.2018.05.017
[research_zhang_sun_2022]: https://doi.org/10.1109/icus55513.2022.9986788
[research_zhang_tan_2016]: https://doi.org/10.2514/1.j055005
[research_zhang_tan_2016_b]: https://doi.org/10.2514/1.j054095
[research_zhang_tang_2012]: https://doi.org/10.1109/ihmsc.2012.19
[research_zhang_tang_2015]: https://doi.org/10.2514/6.2015-3667
[research_zhang_wang_2019]: https://doi.org/10.1115/1.4043511
[research_zhang_wang_2019_b]: https://doi.org/10.1177/1077546319856142
[research_zhang_wang_2024]: https://doi.org/10.1109/aim55361.2024.10637004
[research_zhang_xia_2017]: https://doi.org/10.23919/chicc.2017.8028337
[research_zhang_xie_2024]: https://doi.org/10.1007/978-981-97-3998-1_9
[research_zhang_xie_2025]: https://doi.org/10.1016/j.icheatmasstransfer.2025.109733
[research_zhang_xiong_2022]: https://doi.org/10.1109/access.2022.3150830
[research_zhang_xiong_2022_b]: https://doi.org/10.1109/jsen.2022.3143705
[research_zhang_xu_2012]: https://doi.org/10.4028/www.scientific.net/amm.198-199.207
[research_zhang_yang_2015]: https://doi.org/10.1016/j.actaastro.2014.11.023
[research_zhang_yu_2018]: https://doi.org/10.1109/gncc42960.2018.9018888
[research_zhang_yue_2019]: https://doi.org/10.1016/j.ast.2019.105420
[research_zhang_zhang_2015]: https://doi.org/10.2514/6.2015-3669
[research_zhang_zhang_2022]: https://doi.org/10.23919/ccc55666.2022.9901754
[research_zhang_zhang_2022_b]: https://doi.org/10.1186/s42774-022-00125-x
[research_zhang_zhang_2024]: https://doi.org/10.2139/ssrn.4789185
[research_zhang_zhao_2015]: https://doi.org/10.2514/6.2015-3621
[research_zhang_zhao_2023]: https://doi.org/10.1088/1742-6596/2489/1/012010
[research_zhang_zong_2026]: https://doi.org/10.1016/j.ast.2026.112616
[research_zhang_zong_2026_b]: https://doi.org/10.1063/5.0338245
[research_zhangzhikai_duanguangren_2015]: https://doi.org/10.1109/ascc.2015.7244862
[research_zhao_2011]: https://doi.org/10.2514/6.2011-3858
[research_zhao_2013]: https://doi.org/10.2514/6.2013-2928
[research_zhao_2021]: https://doi.org/10.1007/978-981-33-6526-1_4
[research_zhao_2021_b]: https://doi.org/10.1007/978-981-33-6526-1_2
[research_zhao_2021_c]: https://doi.org/10.1007/978-981-33-6526-1_1
[research_zhao_2021_d]: https://doi.org/10.1007/978-981-33-6526-1
[research_zhao_2021_e]: https://doi.org/10.1007/978-981-33-6526-1_7
[research_zhao_2023]: https://doi.org/10.1016/b978-0-323-89910-9.00015-6
[research_zhao_2023_b]: https://doi.org/10.21203/rs.3.rs-2486979/v1
[research_zhao_cai_2018]: https://doi.org/10.1109/ccdc.2018.8407903
[research_zhao_chen_2019]: https://doi.org/10.1007/s11071-019-04897-8
[research_zhao_gao_2023]: https://doi.org/10.1088/1742-6596/2633/1/012011
[research_zhao_qian_2011]: https://doi.org/10.2514/6.2011-2322
[research_zhao_sha_2026]: https://doi.org/10.1061/jaeeez.aseng-6987
[research_zhao_sun_2019]: https://doi.org/10.1016/j.actaastro.2018.12.011
[research_zhao_tian_2023]: https://doi.org/10.1016/j.ast.2023.108529
[research_zhao_xia_2018]: https://doi.org/10.1016/j.ast.2017.12.024
[research_zhao_zhang_2009]: https://doi.org/10.1016/j.ijthermalsci.2008.11.004
[research_zhao_zhang_2018]: https://doi.org/10.1016/j.fuel.2018.06.034
[research_zhapbasbaev_makashev_2003]: https://doi.org/10.1023/a:1024730720612
[research_zheltovodov_knight_2011]: https://doi.org/10.1017/cbo9780511842757.005
[research_zheng_bray_1994]: https://doi.org/10.1016/0010-2180(94)90151-1
[research_zheng_bray_1997]: https://doi.org/10.1007/978-94-011-5432-1_9
[research_zheng_chang_2013]: https://doi.org/10.4028/www.scientific.net/amm.274.200
[research_zheng_xiao_2021]: https://doi.org/10.1016/j.fuel.2020.119371
[research_zheng_zhang_2019]: https://doi.org/10.5772/intechopen.85187
[research_zheng_zhao_2025]: https://doi.org/10.2139/ssrn.5239640
[research_zhengdong_man_2013]: https://doi.org/10.1155/2013/369092
[research_zhi_liang_2015]: https://doi.org/10.1016/j.proeng.2014.12.559
[research_zhi_yang_2015]: https://doi.org/10.1007/s11432-015-5351-5
[research_zhikharev_1993]: https://doi.org/10.1007/bf00417928
[research_zhong_2000]: https://doi.org/10.21236/ada378988
[research_zhong_2007]: https://doi.org/10.21236/ada467163
[research_zhong_2009]: https://doi.org/10.21236/ada517055
[research_zhong_furumoto_1998]: https://doi.org/10.1142/9789812812957_0042
[research_zhong_lee_1996]: https://doi.org/10.2514/6.1996-1856
[research_zhong_whang_2001]: https://doi.org/10.1142/9789812810793_0019
[research_zhong_wu_2021]: https://doi.org/10.1155/2021/2115641
[research_zhongjiemeng_jianzhongdong_2010]: https://doi.org/10.1109/wcica.2010.5554861
[research_zhongjiemeng_panfenghuang_2008]: https://doi.org/10.1109/aim.2008.4601825
[research_zhou_2018]: https://doi.org/10.5772/intechopen.70863
[research_zhou_2023]: https://doi.org/10.4273/ijvss.15.2.22
[research_zhou_bao_2008]: https://doi.org/10.2514/6.2008-5177
[research_zhou_davidson_1995]: https://doi.org/10.1080/10618569508940741
[research_zhou_du_2022]: https://doi.org/10.3390/e24101325
[research_zhou_gao_2016]: https://doi.org/10.1109/ccdc.2016.7531502
[research_zhou_li_2023]: https://doi.org/10.1063/5.0136170
[research_zhou_liu_2020]: https://doi.org/10.1002/oca.2584
[research_zhou_lu_2017]: https://doi.org/10.2514/6.2017-2343
[research_zhou_teng_2017]: https://doi.org/10.2514/6.2017-2327
[research_zhou_tian_2025]: https://doi.org/10.1016/j.applthermaleng.2025.127851
[research_zhou_wang_2019]: https://doi.org/10.1016/j.actaastro.2019.08.012
[research_zhou_wang_2026]: https://doi.org/10.1109/taes.2026.3705024
[research_zhou_xu_2022]: https://doi.org/10.3390/app12147127
[research_zhou_zhang_2026]: https://doi.org/10.1016/j.ast.2026.112677
[research_zhu_chen_2025]: https://doi.org/10.1063/5.0307286
[research_zhu_gao_2024]: https://doi.org/10.2139/ssrn.4675586
[research_zhu_li_2023]: https://doi.org/10.1007/978-981-99-5877-1_4
[research_zhu_liu_2015]: https://doi.org/10.1109/ccdc.2015.7162611
[research_zhu_liu_2015_b]: https://doi.org/10.1109/ccdc.2015.7162436
[research_zhu_liu_2026]: https://doi.org/10.1109/jsen.2026.3720626
[research_zhu_luo_2020]: https://doi.org/10.3390/en13082048
[research_zhu_pethasethuraman_2025]: https://doi.org/10.2139/ssrn.5148231
[research_zhu_shen_2015]: https://doi.org/10.1016/j.proeng.2014.12.646
[research_zhu_xu_2017]: https://doi.org/10.1061/(asce)as.1943-5525.0000740
[research_zhu_yin_2026]: https://doi.org/10.2139/ssrn.6944783
[research_zhu_zhao_2016]: https://doi.org/10.1016/j.actaastro.2016.01.028
[research_zinnecker_serrani_2012]: https://doi.org/10.2514/6.2012-4813
[research_zivanovic_1963]: https://doi.org/10.21236/ad0423930
[research_zoccoli_1977]: https://doi.org/10.21236/ada047872
[research_zoharrhoter_gabrielcnastac]: https://ntrs.nasa.gov/citations/20260004751
[research_zolotukhin_price_2025]: https://doi.org/10.1007/s44205-025-00175-5
[research_zope_bhushan_2026]: https://doi.org/10.2514/6.2026-1143
[research_zou_pan_2026]: https://doi.org/10.1016/j.applthermaleng.2026.132000
[research_zou_pan_2026_b]: https://doi.org/10.1016/j.ast.2026.112924
[research_zou_zhang_2021]: https://doi.org/10.1109/cac53003.2021.9727431
[research_zuchowski_2013]: https://doi.org/10.2514/6.2013-1457
[research_zucro_1950]: https://doi.org/10.21236/ad0001828
[research_zuo_cui_2023]: https://doi.org/10.1016/j.applthermaleng.2023.119989
[research_zweber_kabis_2002]: https://doi.org/10.2514/6.2002-5172
