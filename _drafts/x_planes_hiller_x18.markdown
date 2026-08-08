---
layout: post
mathjax: true
comments: true
title: "X-Planes: Hiller X-18"
date: 2025-10-24 09:00:00 +0000
categories: aerospace history engineering
series: x_planes
series_title: X-Planes
series_index: 19
---

<!-- A315 -->
<script>console.log("A315");</script>

The [Hiller X-18][ref_x18] tilted its entire wing to take off vertically, and the reason that is hard is not the tilting. It is that a wing pointed at the sky is a wing pointed away from the oncoming air, and a wing at ninety degrees to the flow is stalled. **The configuration works only where the propeller slipstream keeps the flow attached, and the fraction of the wing that sits in the slipstream is fixed at design time.** This article is the nineteenth in the [X-Planes series][related_post_a297_xplanes_framing], following the [X-1][related_post_a298_bell_x1], the [X-2][related_post_a299_bell_x2], the [X-3][related_post_a300_douglas_x3], the [X-4][related_post_a301_northrop_x4], the [X-5][related_post_a302_bell_x5], the [X-6][related_post_a303_convair_x6], the [X-7][related_post_a304_lockheed_x7], the [X-8][related_post_a305_aerojet_x8], the [X-9][related_post_a306_bell_x9], the [X-10][related_post_a307_north_american_x10], the [X-11][related_post_a308_convair_x11], the [X-12][related_post_a309_convair_x12], the [X-13][related_post_a310_ryan_x13], the [X-14][related_post_a311_bell_x14], the [X-15][related_post_a312_north_american_x15], the [X-16][related_post_a313_bell_x16], and the [X-17][related_post_a314_lockheed_x17].

The series has met the vertical take-off problem twice already, at the [X-13][related_post_a310_ryan_x13] and the [X-14][related_post_a311_bell_x14]. Both solved it by pointing a jet downward. **The X-18 is the first attempt in this series to solve it with a wing**, which is a different problem with a different failure mode, and the failure mode arrived.

The standard inventory entry remains [Jenkins Landis and Miller 2003 American X-Vehicles, An Inventory X-1 to X-50][book_jenkins_landis_miller_2003] and the vehicle compilation is [Miller 2001 The X-Planes, X-1 to X-45][book_miller_2001]. The configuration's own design literature is [McCormick and Mallen 1956][research_mccormick_mallen_1956] and its later textbook form [McCormick 1967 Aerodynamics of V/STOL Flight][book_mccormick_1967].

## The Research Question

The question is not whether a wing can be tilted. It obviously can. The question is **whether a continuous, controllable path exists from hover to wing-borne flight**, and for a tilt-wing that path is constrained by something the pilot cannot adjust.

### The Keystone Is Slipstream Immersion

**The keystone is the fraction of the wing that sits inside the propeller slipstream.**

At zero forward speed the aircraft is held up by propeller thrust, and the wing does nothing except get in the way. At cruise the wing does everything. In between, the wing must take over progressively, and to do that it must be generating lift at wing tilt angles far beyond any ordinary stall angle.

The only thing that permits that is the slipstream. **Air leaving a propeller disc at eighty metres per second does not care that the aircraft is stationary**, and a wing immersed in it is flying regardless. A wing outside it is not.

So the configuration divides the wing into two parts that behave completely differently through the whole conversion, and **the division is set by propeller diameter against span**, which is frozen when the aircraft is drawn.

### Why This Was the Binding Unknown in 1957

The alternatives were understood and each had a known defect. A helicopter has a low disc loading and cannot cruise efficiently. A tail-sitter, as the [X-13][related_post_a310_ryan_x13] showed, asks the pilot to land looking over his shoulder. A deflected-jet aircraft, as the [X-14][related_post_a311_bell_x14] showed, spends an enormous fraction of its thrust simply on being controllable.

**A tilt-wing promised a genuine transport aircraft**, one that hovers like a helicopter and then cruises like an aeroplane with the whole wing working. Design studies of the period compare the options directly, in [IRVIN and SWAN 1956][research_irvin_swan_1956] and [DIV 1956][research_div_1956], and the tilt-wing's commercial case is argued in [Mazzitelli 1957][research_mazzitelli_1957].

The configuration's own design requirements were being written at the same time, in [III 1956][research_iii_1956], [DALLAS and IRVIN 1956][research_dallas_irvin_1956], and the successive treatments of [McCormick and Mallen 1957][research_mccormick_mallen_1957]. Earlier convertiplane flight experience is recorded in [Marks 1956][research_marks_1956] and the critical advance ratio problem in [DOETSCH and MARK 1953][research_doetsch_mark_1953].

What nobody had was flight evidence that the conversion was flyable at full scale. **That is what the X-18 was built to obtain, and it is what the X-18 failed to obtain.**

## Programme Origin

The X-18 is the most conspicuously improvised aircraft in this series. Hiller built it from parts that already existed. The fuselage came from a [Chase YC-122C Avitruc][ref_yc122] assault transport. The turboprops came from two cancelled tail-sitting fighter programmes, the [Convair XFY-1 Pogo][ref_xfy1] and the [Lockheed XFV-1][ref_xfv1], which had used the same [Allison T40][ref_t40] driving contra-rotating propellers. A [Westinghouse J34][ref_j34] turbojet went in the tail.

**That is a research aircraft assembled from the wreckage of the previous generation of answers to the same question**, which is worth noting because the components carried their assumptions with them. The propellers were sized for a tail-sitter, not for a tilt-wing.

### The Vehicle

Sources give a span of 47 feet 11 inches, a wing area of 528 square feet, a length of 63 feet, an empty weight of 27,052 pounds, and a maximum take-off weight of 33,000 pounds. The two contra-rotating propellers are 16 feet in diameter. The first hop was on 11 November 1959 and the first flight on 24 November, and 20 flights followed to July 1961.

The published figures are internally consistent, which is worth checking before relying on them. Aspect ratio from span and area is

$$A = \frac{b^{2}}{S} = \frac{47.92^{2}}{528} = 4.348$$

against a quoted 4.36, and the wing loading at maximum weight is

$$\frac{W}{S} = \frac{33{,}000}{528} = 62.50\ \text{lb/ft}^{2}$$

## Sizing From First Principles

### How Much of the Wing Is Immersed

The raw geometric ratio is two propeller diameters against the span,

$$f_{\text{raw}} = \frac{n D_p}{b} = \frac{2 \times 16}{47.92} = 0.668$$

so two thirds of the span sits behind a propeller. **That figure is optimistic, because a slipstream contracts.** Momentum theory gives the fully developed slipstream area as half the disc area, so the diameter contracts by the square root of two,

$$D_{\text{slip}} = \frac{D_p}{\sqrt{2}} = \frac{4.877}{1.414} = 3.448\ \text{m} = 11.31\ \text{ft}$$

which would immerse only 47.2 percent of the span. The wing sits close behind the disc, where contraction is partial, so the true figure lies between.

| Station | Diameter factor | Immersed span |
|---|---|---|
| At the disc | 1.000 | 66.8 percent |
| Just behind the disc | 0.850 | 56.8 percent |
| Fully developed | 0.707 | 47.2 percent |

**Taking a representative value, about 57 percent of the span is immersed and about 43 percent is not.** That number is the whole article.

### Is the Un-Immersed Wing Actually Stalled

The outer wing meets the freestream at an angle of attack equal to the wing tilt plus the fuselage attitude. With the fuselage level,

$$\alpha_{\text{free}} = i_w$$

and taking a stall angle of 15 degrees, which is an assumption and a generous one for a thick unswept wing, the outer panel is stalled for any tilt above 15 degrees. A conversion runs from zero tilt to about ninety, so the stalled fraction of the conversion is

$$\frac{90 - 15}{90} = 0.833$$

Maximum lift and stalling behaviour of full-scale wings had been catalogued since [Sweberg and Dingeldein 1945][research_sweberg_dingeldein_1945], and the leading-edge stall mechanism at high incidence in [Black 1956][research_black_1956], so the designers were not working blind about the stall itself. They were working blind about what a propeller does to it.

**The outer wing is stalled for five sixths of the conversion.** That is geometric rather than aerodynamic, and no amount of section design removes it, because the wing is pointed away from the oncoming air by construction. The stall behaviour of exactly this configuration was measured, in [Giulianetti and Weiberg 1964][research_giulianetti_weiberg_1964], and the prediction of span loading on a propeller-blown wing up to stall is the subject of [Mcveigh et al 1975][research_mcveigh_1975].

### What the Slipstream Buys

Momentum theory for an actuator disc at static thrust gives the induced velocity at the disc and the fully developed slipstream behind it,

$$v_i = \sqrt{\frac{T}{2 \rho A}}, \qquad v_s = 2 v_i$$

At maximum weight each propeller carries half of it,

$$T = \frac{33{,}000}{2} = 16{,}500\ \text{lbf} = 73.4\ \text{kN}$$

over a disc area of 18.68 square metres, which is a disc loading of

$$\frac{T}{A} = \frac{73{,}400}{18.68} = 3{,}929\ \text{N/m}^{2} = 82.1\ \text{lb/ft}^{2}$$

and gives

$$v_i = \sqrt{\frac{73{,}400}{2 \times 1.225 \times 18.68}} = 40.05\ \text{m/s}$$

with a fully developed slipstream at 80.09 metres per second. Taking a part-developed value of $1.5 v_i$ at the wing, the dynamic pressure over the immersed panel at **zero forward speed** is

$$q_{\text{slip}} = \tfrac{1}{2} \rho (1.5 v_i)^{2} = \tfrac{1}{2} \times 1.225 \times 60.07^{2} = 2{,}210\ \text{Pa}$$

which corresponds to an equivalent airspeed of

$$V_{\text{eq}} = \sqrt{\frac{2 q_{\text{slip}}}{\rho}} = 60.1\ \text{m/s} = 117\ \text{kt}$$

**The immersed wing is flying at about 117 knots while the aircraft is standing still.** That is the entire trick of the configuration, and it is why a tilt-wing can work at all. **The immersed wing never stops flying. The un-immersed wing never starts.**

### What the Immersed Wing Can Carry

With 57 percent of the span immersed, the immersed area is 27.84 square metres against 21.21 outside.

| Lift coefficient | Immersed lift | Fraction of maximum weight |
|---|---|---|
| 0.8 | 11,068 lbf | 33.5 percent |
| 1.0 | 13,835 lbf | 41.9 percent |
| 1.4 | 19,370 lbf | 58.7 percent |

The wing alone cannot hover the aircraft, which is expected, because in hover the propellers carry the weight directly as thrust. **The number that matters is not whether the wing lifts the aircraft in hover but whether the handover is continuous**, and the table shows there is a substantial contribution available from the immersed panel throughout.

### The Cost of the Configuration, Which Is Disc Loading

$$\frac{W}{n A} = \frac{146{,}800}{2 \times 18.68} = 3{,}929\ \text{N/m}^{2} = 82.1\ \text{lb/ft}^{2}$$

against roughly 11.7 pounds per square foot for a single 60 foot helicopter rotor at the same weight. **The tilt-wing carries seven times the disc loading of a helicopter**, which is the price of having propellers small enough to fit on a wing. Hover power follows from the same momentum theory,

$$P = n\, T \sqrt{\frac{T}{2 \rho A}}$$

which evaluates to 5,879 kilowatts, or **7,883 ideal shaft horsepower**. Against an installed 11,700 horsepower from two T40 engines, that implies a figure of merit of

$$\text{FM} = \frac{7{,}883}{11{,}700} = 0.674$$

**which is an entirely ordinary propeller figure of merit**, and is the strongest available check that the published weight, propeller diameter, and engine power describe one consistent aircraft.

## Dependent Systems

### The Pitch Jet, Which Is the Same Answer the X-13 and X-14 Gave

The X-18 carried a turbojet in the tail whose exhaust was deflected up or down purely for pitch control at low speed. The reason is the relation the previous two vertical take-off articles both used. Aerodynamic control scales with dynamic pressure and vanishes at zero speed, while thrust does not,

$$M_{\text{aero}} = q S \bar{c}\, C_{m\delta_e} \delta_e \propto V^{2}, \qquad M_{\text{jet}} = T_{\text{jet}}\, l$$

At a tail arm of 8.64 metres, a thousand pounds force of deflected jet gives 38.4 kilonewton metres. Setting the two equal and solving for speed gives the crossover at which the elevator takes over,

$$V_{\text{cross}} = \sqrt{\frac{2 M_{\text{jet}}}{\rho S \bar{c}\, C_{m\delta_e} \delta_e}} = 30.2\ \text{m/s} = 58.6\ \text{kt}$$

The control-power requirement that makes such a system necessary was being established across the same years, in [Reeder 1958][research_reeder_1958], [Carlson 1958][research_carlson_1958], [Slaughter 1958][research_slaughter_1958], and [Crim 1959][research_crim_1959], with the underlying hovering-stability question in [McCaskill 1953][research_mccaskill_1953] and the variable-stability technique that produced much of it in [Harper and P. 1955][research_harper_p_1955].

**Below about sixty knots the jet is doing the work.** That is the third time in this series that a vertical take-off aircraft has had to carry a separate thrust-based control system for exactly this reason, and it is the clearest recurring result the series has produced.

### The Engines, and the Thing That Was Missing

Sources state that the two turboprops were **not cross-linked**, so the failure of one removed that propeller's thrust entirely. In hover that is half the lift, applied at the propeller's lateral station. Taking the propeller at a quarter span,

$$M_{\text{roll}} = T y = 73.4 \times 3.65 = 268\ \text{kN m}$$

Against that, roll control comes from the ailerons, whose effectiveness scales with dynamic pressure,

$$L_{\delta_a} = q S b\, C_{l\delta_a} \delta_a$$

| Freestream | Aileron moment | Fraction of the upset |
|---|---|---|
| 0 m/s | 0.0 kN m | 0.00 percent |
| 10 m/s | 1.2 kN m | 0.46 percent |
| 20 m/s | 4.9 kN m | 1.83 percent |
| 30 m/s | 11.0 kN m | 4.12 percent |

**The ailerons supply under one percent of what is needed in hover and still only four percent at thirty metres per second.** The statement in the sources that losing an engine meant losing the aircraft is therefore not a caution. **It is arithmetic**, and cross-shafting is not a refinement but the only available fix. The problem was recognised in the period literature for turboprops generally, in [KIRCHNER 1955][research_kirchner_1955].

### The Wing and Its Devices

A tilt-wing's outer panel is stalled through most of the conversion, so every device that delays stall is worth having. The period answer was boundary layer control by blowing, investigated over flaps and combinations in [Spreemann and Kuhn 1956][research_spreemann_kuhn_1956], [Kuhn 1957][research_kuhn_1957], and [Spreemann 1958][research_spreemann_1958], and large-chord slotted arrangements in [Kirby 1956][research_kirby_1956].

Free-floating and stall-flutter behaviour of tilt-wing models was investigated later, in [Ormiston 1972][research_ormiston_1972].

**The X-18 had none of that.** It had a wing, two propellers, and a tilt mechanism, which is the minimum experiment rather than the best aircraft.

### The Propellers

Propeller behaviour at zero and low forward speed is its own subject, and static thrust in particular is not simply the cruise propeller evaluated at zero advance ratio, as [Webb and Willer 1952][research_webb_willer_1952] sets out, with later estimation methods in [Brusse and Cronk 1965][research_brusse_cronk_1965]. Propeller design for this class of aircraft is treated in [BIERMANN 1954][research_biermann_1954] and the ducted alternative in [ZABINSKY and LASZEWSKI 1956][research_zabinsky_laszewski_1956]. The interference between a propeller and the wing behind it is the configuration's defining aerodynamic problem and was measured directly, in [Winston and Huston 1962][research_winston_huston_1962], [GOLAND et al 1964][research_goland_1964], and [Butler et al 1966][research_butler_1966].

## The Flight Test Record

Twenty flights between November 1959 and July 1961. **The X-18 never completed a full conversion and never hovered.** The wing was tilted in flight, but the programme did not reach the vertical.

On the twentieth flight, in July 1961, a propeller pitch control problem occurred while the aircraft was attempting to convert toward a hover at ten thousand feet. The aircraft entered a spin. The crew recovered and landed, and **the X-18 never flew again.** It was grounded and later scrapped.

### How Much Asymmetry That Took

Asymmetric propeller pitch is asymmetric thrust, which is both a direct rolling moment and an asymmetric slipstream, so the two wings stall at different times. A fractional thrust difference $\varepsilon$ gives

$$M_{\text{roll}} = \varepsilon\, T y$$

and the aileron authority available must exceed it. At ten thousand feet, where the density is 0.9046 kilogrammes per cubic metre or 73.8 percent of sea level,

| Speed | Aileron moment | Tolerable thrust asymmetry |
|---|---|---|
| 30 m/s | 8.1 kN m | 3.04 percent |
| 40 m/s | 14.5 kN m | 5.40 percent |
| 50 m/s | 22.6 kN m | 8.44 percent |

**A few percent of thrust asymmetry exhausts the roll control.** A pitch control failure on a propeller is not a small disturbance, so a departure is the expected outcome rather than bad luck.

There is a further and slightly bitter point. The same asymmetry at sea level would be tolerable up to 4.12 percent at thirty metres per second rather than 3.04, because

$$\frac{\varepsilon_{\text{SL}}}{\varepsilon_{10{,}000}} = \frac{\rho_{\text{SL}}}{\rho_{10{,}000}} = 1.354$$

**Converting at ten thousand feet rather than near the ground cost about 26 percent of the available roll authority.** The altitude was chosen for safety, to give room to recover, and it made the departure more likely while making it more survivable. Both of those are true and the programme got the survivable half.

## Comparison With Ground Prediction

The tilt-wing was tested extensively in wind tunnels before and during the X-18's life, including full-scale longitudinal stability work in [Hickey 1956][research_hickey_1956] and the large-scale unswept tilt-wing tests of [Giulianetti and Weiberg 1964][research_giulianetti_weiberg_1964]. The smaller [Vertol VZ-2][ref_vz2] flew the configuration first and its flight results are summarised in the period literature.

**What the ground testing did not predict, and arguably could not, is the consequence of a control failure during conversion.** A wind tunnel measures the vehicle's aerodynamics. It does not measure what happens when a propeller governor misbehaves at a moment when the aircraft has almost no roll authority. **The X-18's loss was a systems failure expressed through an aerodynamic vulnerability**, and only the second half of that is testable on the ground.

## What the Data Changed

**The configuration went forward and the aircraft did not.** The [LTV XC-142][ref_xc142] followed directly, with four propellers rather than two, full cross-shafting between all engines, and a much larger immersed fraction of the wing. **Every one of those changes addresses something this article has computed.**

Four propellers on a wing immerse more of it than two. Cross-shafting removes the engine-out roll upset entirely, because a failed engine no longer removes a propeller. **The X-18's contribution is a demonstration of what a minimum tilt-wing cannot do**, and the next aircraft was designed against exactly that list.

What it did not change is the underlying limit. **The outer wing is still stalled during conversion on any tilt-wing**, and the XC-142 had its own difficulties in descent for related reasons. The configuration was eventually abandoned in favour of the tilt-rotor, which keeps the wing pointed into the wind and tilts only the rotors, and which is the arrangement that survives today in the [V-22][ref_v22].

## The Contemporary Literature

The tilt-wing was abandoned and has returned, which makes this a live subject rather than a historical one.

### Propeller and Wing Interaction Became Computable

The interference the X-18 could only measure is now simulated, in [Fei 2019][research_fei_2019] and [Zizkovsky and Klesa 2019][research_zizkovsky_klesa_2019], with transient rotor and wing interaction for tiltrotors in [Wu et al 2019][research_wu_2019].

**The quantity this article treats with momentum theory and a contraction factor is exactly what those methods compute properly.** The immersed fraction is no longer a ratio of diameters but a computed pressure field.

### Distributed Electric Propulsion Changes the Immersed Fraction

The X-18's fundamental limitation was that two propellers immerse only part of a wing. **Electric propulsion removes the reason there were only two.** A distributed arrangement of many small propellers can immerse essentially the whole span, which dissolves the keystone rather than solving it.

### The Configuration Returned Because the Constraint Changed

Electric vertical take-off aircraft have revived tilting configurations at small scale, where the engine-out case is managed by having many motors rather than by cross-shafting two, and where the certification question rather than the aerodynamic one is now binding.

## Where the Framing Breaks Down

**It assumes a stall angle.** The 15 degree figure used throughout is an assumption. A thick wing with leading edge devices stalls later, and the fraction of the conversion spent stalled moves with it.

**It treats the slipstream as uniform.** Momentum theory gives an average. A real slipstream is swirling, non-uniform, and differently deflected across the span, and the immersed wing does not see one dynamic pressure.

**It uses a single representative contraction factor.** The 0.85 is a judgement, and the immersed fraction ranges from 47 to 67 percent across defensible choices, which is a wide band on the article's central quantity.

**It treats the final flight as an aerodynamic event.** It was a control system failure. The aerodynamics explain why the consequence was severe and do not explain why the failure occurred, and no public account of the governor fault was located.

## The Source Base

Unlike the two preceding articles, **this subject has a real technical literature**. The tilt-wing was studied intensively by the National Advisory Committee for Aeronautics and its successor, and the configuration's design considerations, wind tunnel behaviour, slipstream interference, and handling qualities are all documented in primary sources.

What is scarce is documentation of **this aircraft**. NASA's technical archive returns nothing for the vehicle designation, and the flight test reports, if they exist publicly, were not located. So the pattern is the inverse of the [X-16][related_post_a313_bell_x16] and [X-17][related_post_a314_lockheed_x17] articles, where the question had a literature and the vehicle did not. **Here the configuration has a literature and the individual airframe does not**, which is a milder version of the same difficulty.

Every dimension and weight is from secondary compilation. No source disagreement of consequence was found, which is itself unusual for this series and is worth stating.

## Epistemic State

**Historical fact.** The X-18 was built from a Chase YC-122C fuselage with Allison T40 turboprops taken from the XFY-1 and XFV-1 programmes and a Westinghouse J34 in the tail for pitch control. First hop 11 November 1959, first flight 24 November 1959, twenty flights, last flight July 1961. A propeller pitch control problem during an attempted conversion at ten thousand feet led to a spin from which the crew recovered. The aircraft never hovered, never completed a conversion, and was later scrapped. The engines were not cross-linked. The XC-142 followed with four propellers and full cross-shafting.

**Engineering analysis, reproducible from the stated inputs.** The aspect ratio of 4.348 against a quoted 4.36. The immersed span fraction of 66.8 percent uncontracted, 47.2 fully contracted, and about 57 at a representative factor. The stalled fraction of the conversion at 83.3 percent. The induced velocity of 40.05 metres per second, disc loading of 82.1 pounds per square foot, and slipstream dynamic pressure equivalent to 117 knots. The immersed lift fractions. The hover power of 7,883 ideal horsepower and the implied figure of merit of 0.674. The engine-out rolling moment of 268 kilonewton metres and the aileron fractions. The tolerable thrust asymmetry figures and the 26 percent authority loss at ten thousand feet. The pitch jet crossover at 59 knots.

**Inference, and clearly labelled.** That the outer wing being stalled is the configuration's defining problem is an inference from the geometry and a stall angle, supported by the period literature on tilt-wing stall but not derived from X-18 flight data. That the XC-142's four propellers and cross-shafting were responses to the X-18's specific failures is an inference from the design changes and their evident purpose.

**What the record does not settle.** What caused the propeller pitch control failure. Whether the X-18 would have converted successfully had it not been grounded. What immersed fraction the designers believed they had. Whether the aircraft was ever close to a hover.

**A correction made during drafting.** An elevator effectiveness coefficient of 0.02 per radian was used initially and produced a pitch jet crossover speed of 454 knots, which is absurd for an aircraft of this class. The correct order is about 1.2 per radian and gives 59 knots. **The error was caught by reading the output for plausibility rather than by any check.**

**Information postdating the editorial date.** The contemporary literature section is written from current knowledge per the series convention.

## Out of Scope

The XC-142 programme deserves its own treatment and gets a paragraph here. The V-22 and the tilt-rotor line generally are named as the surviving alternative and not analysed. The detailed aerodynamics of swirl in a propeller slipstream are cited rather than derived. No attempt is made to reconstruct the X-18's flight envelope, and the descent problem that troubled tilt-wings, in which the wing can be stalled by its own descent rate independently of tilt, is named and left for a fuller treatment.

## Conclusion

The X-18 asked whether a wing could be tilted through ninety degrees and flown all the way. It never found out, and the reason it never found out is contained in the arithmetic of its own geometry.

**Two sixteen-foot propellers on a forty-eight-foot wing immerse a little over half of it.** The immersed part flies at an equivalent 117 knots while the aircraft stands still. **The rest of the wing is stalled for five sixths of the conversion**, and no wing design fixes that, because the wing is pointed away from the air by construction.

That would have been survivable with margin elsewhere. There was none. **The ailerons supply under one percent of the rolling moment an engine failure produces in hover**, the engines were not cross-linked so an engine failure was available to produce it, and a few percent of thrust asymmetry exhausts the roll control during conversion. When a propeller pitch control fault duly appeared, the aircraft departed.

**The configuration was not wrong and this aeroplane was under-equipped for it.** The XC-142 answered with twice the propellers, full cross-shafting, and a far larger immersed fraction, which is a list of the X-18's deficiencies written as a specification. **The X-18's contribution was to establish, expensively and at the edge of a fatal accident, what the minimum version of the idea could not do.**

## References

### Books

[book_jenkins_landis_miller_2003]: https://openlibrary.org/search?q=Jenkins+Landis+Miller+American+X+Vehicles
[book_mccormick_1967]: https://openlibrary.org/search?q=McCormick+Aerodynamics+of+V+STOL+Flight
[book_miller_2001]: https://openlibrary.org/search?q=Miller+The+X+Planes+X-1+to+X-45

### Reference

[ref_j34]: https://en.wikipedia.org/wiki/Westinghouse_J34
[ref_t40]: https://en.wikipedia.org/wiki/Allison_T40
[ref_v22]: https://en.wikipedia.org/wiki/Bell_Boeing_V-22_Osprey
[ref_vz2]: https://en.wikipedia.org/wiki/Vertol_VZ-2
[ref_x18]: https://en.wikipedia.org/wiki/Hiller_X-18
[ref_xc142]: https://en.wikipedia.org/wiki/LTV_XC-142
[ref_xfv1]: https://en.wikipedia.org/wiki/Lockheed_XFV
[ref_xfy1]: https://en.wikipedia.org/wiki/Convair_XFY_Pogo
[ref_yc122]: https://en.wikipedia.org/wiki/Chase_XCG-20

### Research

[research_biermann_1954]: https://doi.org/10.4271/540196
[research_black_1956]: https://doi.org/10.1017/s0368393100132390
[research_brusse_cronk_1965]: https://ntrs.nasa.gov/citations/19660010796
[research_butler_1966]: https://doi.org/10.21236/ad0629637
[research_carlson_1958]: https://doi.org/10.4050/jahs.3.11
[research_crim_1959]: https://doi.org/10.4050/jahs.4.1.26
[research_dallas_irvin_1956]: https://doi.org/10.21236/ad0147926
[research_div_1956]: https://doi.org/10.21236/ad0141370
[research_doetsch_mark_1953]: https://doi.org/10.21236/ad0016744
[research_fei_2019]: https://ntrs.nasa.gov/citations/20200002409
[research_giulianetti_weiberg_1964]: https://ntrs.nasa.gov/citations/19640004814
[research_goland_1964]: https://doi.org/10.21236/ad0608186
[research_harper_p_1955]: https://doi.org/10.21236/ad0092496
[research_hickey_1956]: https://ntrs.nasa.gov/citations/19930088539
[research_iii_1956]: https://doi.org/10.4050/sm_wf_1956-4684
[research_irvin_swan_1956]: https://doi.org/10.21236/ad0147927
[research_kirby_1956]: https://ntrs.nasa.gov/citations/19930084546
[research_kirchner_1955]: https://doi.org/10.4271/550193
[research_kuhn_1957]: https://ntrs.nasa.gov/citations/19930084858
[research_marks_1956]: https://doi.org/10.4050/sm_wf_1956-2795
[research_mazzitelli_1957]: https://doi.org/10.4271/570357
[research_mccaskill_1953]: https://doi.org/10.21236/ad0015833
[research_mccormick_mallen_1956]: https://doi.org/10.4050/sm_wf_1956-2299
[research_mccormick_mallen_1957]: https://doi.org/10.4050/jahs.2.49
[research_mcveigh_1975]: https://ntrs.nasa.gov/citations/19760004918
[research_ormiston_1972]: https://ntrs.nasa.gov/citations/19720018348
[research_reeder_1958]: https://doi.org/10.4050/jahs.3.4
[research_slaughter_1958]: https://doi.org/10.4050/jahs.3.9
[research_spreemann_1958]: https://ntrs.nasa.gov/citations/19930085045
[research_spreemann_kuhn_1956]: https://ntrs.nasa.gov/citations/19930084788
[research_sweberg_dingeldein_1945]: https://ntrs.nasa.gov/citations/19930091906
[research_webb_willer_1952]: https://doi.org/10.21236/ada075990
[research_winston_huston_1962]: https://ntrs.nasa.gov/citations/19630000659
[research_wu_2019]: https://doi.org/10.3390/math7020116
[research_zabinsky_laszewski_1956]: https://doi.org/10.21236/ad0102024
[research_zizkovsky_klesa_2019]: https://doi.org/10.1051/matecconf/201930402019

### Related Post

[related_post_a297_xplanes_framing]: {% post_url 2025-10-06-x_planes_framing %}
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
