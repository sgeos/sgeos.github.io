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

The tilt-wing and its relatives were studied continuously from the mid-1950s to the present, across [McCormick and W. 1956, COMPARATIVE STUDY OF VARIOUS TYPES][research_mccormick_w_1956_2], [FELDMAN 1956][research_feldman_1956], [Stepniewski 1957][research_stepniewski_1957], [Stuart 1957][research_stuart_1957], [Stuart 1957, Tilt Wing Propelloplane Design Req][research_stuart_1957_2], [Ward 1960][research_ward_1960], [Koenig and Quigley 1960][research_koenig_quigley_1960], [Quigley and Koenig 1960][research_quigley_koenig_1960], [Kuhn and Grunwald 1960][research_kuhn_grunwald_1960], [Tosti 1961][research_tosti_1961], [O'ROURKE and RUTHERFORD 1991][research_o_rourke_rutherford_1991], [Totah 1992][research_totah_1992], [RUTHERFORD and BASS 1992][research_rutherford_bass_1992], [Sullivan 1993][research_sullivan_1993], [Harris 2003][research_harris_2003], [Armutcuoglu et al 2004][research_armutcuoglu_2004], [Madrid et al 2007][research_madrid_2007], [Holsten et al 2011][research_holsten_2011], [Cui et al 2019][research_cui_2019], [Rohr et al 2019][research_rohr_2019], [Binz et al 2019][research_binz_2019], [Geuther et al 2020][research_geuther_2020].

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

Stall and maximum lift on wings of this kind were catalogued extensively over the same decades, across [SHARP 1950][research_sharp_1950], [Hickey and Aoyagi 1960][research_hickey_aoyagi_1960], [Feistel et al 1978][research_feistel_1978], [Nelson and Mouch 1978][research_nelson_mouch_1978], [Wang 1979][research_wang_1979], [VINCENT et al 1979][research_vincent_1979], [Smith and Levin 1981][research_smith_levin_1981], [BENNETT et al 1983][research_bennett_1983], [Anderson and Cho 1984][research_anderson_cho_1984], [Bartlett 1985][research_bartlett_1985], [Hoadley and Pederson 2001][research_hoadley_pederson_2001], [Catalano 2004][research_catalano_2004], [Delamore-Sutcliffe and Greenwell 2006][research_delamore_sutcliffe_greenwell_2006], [Uhlig and Selig 2008][research_uhlig_selig_2008], [Fan et al 2019][research_fan_2019], [S.P et al 2022][research_s_p_2022], [Xiao et al 2022][research_xiao_2022], [Goharshadi and Mirzaei 2022][research_goharshadi_mirzaei_2022].

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

That is the static case. With forward speed the induced velocity solves

$$v_i = \frac{T}{2 \rho A \sqrt{V^{2} + v_i^{2}}}$$

which reduces to the expression above at zero speed. The induced velocity **falls** as the aircraft accelerates, from 40.05 metres per second at rest to 24.71 at sixty, while the freestream rises faster, so the total dynamic pressure over the immersed panel climbs from 2,210 to 5,772 pascals through the conversion.

**The handover is helped by the physics rather than fought by it.** The immersed panel gets a more energetic flow at every stage of the conversion, not less, which is a large part of why the configuration is viable at all.

**The immersed wing is flying at about 117 knots while the aircraft is standing still.** That is the entire trick of the configuration, and it is why a tilt-wing can work at all. **The immersed wing never stops flying. The un-immersed wing never starts.**

### The Relation That Makes the Configuration Work

The article has so far asserted that the slipstream keeps the immersed panel flying without giving the relation that makes it true. That relation is the local angle of attack, and it is the most important equation here.

The propeller axis lies along the wing chord, so the slipstream adds velocity **along the chord** while the freestream arrives at the wing tilt angle. Resolving the two,

$$\alpha_{\text{local}} = \arctan\left(\frac{V \sin i_w}{V \cos i_w + v_s}\right)$$

For the un-immersed panel $v_s = 0$ and this collapses to $\alpha = i_w$, which is the claim made earlier and is now a limiting case rather than a separate assertion. For the immersed panel it does something remarkable.

| Speed | 15° tilt | 30° | 45° | 60° | 75° | 90° |
|---|---|---|---|---|---|---|
| 0 m/s | **0.0** | **0.0** | **0.0** | **0.0** | **0.0** | **0.0** |
| 10 m/s | 2.1 | 4.2 | 6.0 | 7.6 | 8.8 | 9.5 |
| 20 m/s | 3.7 | 7.4 | 10.8 | 13.9 | 16.5 | 18.4 |
| 30 m/s | 5.0 | 9.9 | 14.6 | 19.1 | 23.1 | 26.5 |
| 60 m/s | 7.5 | 15.0 | 22.5 | 30.0 | 37.5 | 45.0 |

The interference this relation idealises is the configuration's central aerodynamic subject and has its own long literature, in [THOREN and JOHNSON 1940][research_thoren_johnson_1940], [Stiesz 1940][research_stiesz_1940], [BRENCKMANN 1958][research_brenckmann_1958], [Kuhn 1959][research_kuhn_1959], [VIDAL et al 1960][research_vidal_1960], [Grunwald 1961][research_grunwald_1961], [Weiberg and Holzhauser 1961][research_weiberg_holzhauser_1961], [Kuhn and Grunwald 1961][research_kuhn_grunwald_1961], [Rizk 1980][research_rizk_1980], [RIZK 1980, Propeller slipstream/wing interact][research_rizk_1980_2], [KATZ et al 1980][research_katz_1980], [Welge et al 1981][research_welge_1981], [Meloney et al 2000][research_meloney_2000], [Moens and Gardarein 2001][research_moens_gardarein_2001], [Meloney et al 2001][research_meloney_2001], [Renooij and Slingerland 2004][research_renooij_slingerland_2004], [Wang et al 2019][research_wang_2019], [Wang et al 2019, Aerodynamic design of multi-propel][research_wang_2019_3], [Mikhalyov et al 2019][research_mikhalyov_2019], [Xue and Zhou 2020][research_xue_zhou_2020].

**At zero forward speed the immersed wing is at exactly zero angle of attack, at any tilt whatever.** The only flow it sees comes straight down its own chord. It is not stalled, not marginal, and needs no high-lift device to be unstalled. The un-immersed panel meanwhile sits at the full tilt angle at every speed in the table.

### Where the Immersed Panel Finally Does Stall

Setting $\alpha_{\text{local}}$ equal to the stall angle and solving for tilt gives the limit.

| Speed | Maximum tilt before the immersed panel stalls |
|---|---|
| 10 m/s | 90.0° |
| 20 m/s | 66.0° |
| 30 m/s | 46.2° |
| 40 m/s | 37.9° |
| 60 m/s | 30.0° |

**The tolerable tilt falls as speed rises, which is the right direction**, because a faster aircraft needs less tilt anyway. The two curves are moving the same way, and whether a corridor exists depends on whether the required tilt falls faster than the allowed one.

### What the Immersed Wing Can Carry

With 57 percent of the span immersed, the immersed area is 27.84 square metres against 21.21 outside.

| Lift coefficient | Immersed lift | Fraction of maximum weight |
|---|---|---|
| 0.8 | 11,068 lbf | 33.5 percent |
| 1.0 | 13,835 lbf | 41.9 percent |
| 1.4 | 19,370 lbf | 58.7 percent |

The wing alone cannot hover the aircraft, which is expected, because in hover the propellers carry the weight directly as thrust. **The number that matters is not whether the wing lifts the aircraft in hover but whether the handover is continuous**, and the table shows there is a substantial contribution available from the immersed panel throughout.

### The Conversion Corridor, Which Turns Out to Exist

Level flight during conversion requires

$$T \sin i_w + L = W, \qquad T \cos i_w = D$$

with the lift coming from the immersed panel at slipstream dynamic pressure and the rest of the wing at freestream dynamic pressure,

$$L = q_{\text{slip}} S_{\text{imm}} C_{L,\text{imm}} + q_\infty (S - S_{\text{imm}}) C_{L,\text{free}}$$

Solving for the tilt that balances weight at each speed, and setting it beside the tilt the immersed panel will tolerate, gives the corridor.

| Speed | Tilt required | Tilt allowed | Margin |
|---|---|---|---|
| 10 m/s | 51.9° | 90.0° | 38.1° |
| 20 m/s | 37.4° | 66.0° | 28.7° |
| 30 m/s | 26.6° | 46.2° | 19.6° |
| 40 m/s | 23.4° | 37.9° | 14.4° |
| 50 m/s | 20.5° | 33.1° | 12.6° |
| 60 m/s | 17.0° | 30.0° | 13.1° |

The transition problem and the corridor concept were the central preoccupation of the powered-lift community for decades, across [DIV 1956, COMPARATIVE STUDY OF VARIOUS TYPES][research_div_1956_2], [Smith 1958][research_smith_1958], [Loewy and Yntema 1958][research_loewy_yntema_1958], [BAXTER and FINVOLD 1958][research_baxter_finvold_1958], [Mallen and Dancik 1959][research_mallen_dancik_1959], [NACA 1960][research_naca_1960], [NACA 1960, Conference on V/Stol Aircraft a Co][research_naca_1960_2], [Tapscott 1960][research_tapscott_1960], [Tapscott 1960, Criteria for Control and Response][research_tapscott_1960_2], [Anderson 1960][research_anderson_1960], [Stapleford 1980][research_stapleford_1980], [Roberts et al 1981][research_roberts_1981], [FLUK 1981][research_fluk_1981], [HILL 1981][research_hill_1981], [Verma and Junkins 2000][research_verma_junkins_2000], [Kahne 2000][research_kahne_2000], [Kahne 2000, Research Issues in the Transition][research_kahne_2000_2], [Chana 2002][research_chana_2002], [Ng and Datta 2019][research_ng_datta_2019], [Biyela and Rawatlal 2019][research_biyela_rawatlal_2019], [Wang et al 2019, Research on Dynamic Modeling and T][research_wang_2019_2], [Wang et al 2019, Stability Analysis of Tailsitters][research_wang_2019_4].

**A corridor exists at every speed.** That is worth stating plainly, because the argument so far has emphasised what is stalled and could leave the impression that the configuration is marginal. **It is not. The tilt-wing works, with a margin of between twelve and thirty-eight degrees of tilt throughout.** The X-18 was under-equipped for the configuration rather than attempting an impossible one.

The margin is narrowest in the middle of the conversion, around forty to fifty metres per second, which is where the aircraft has neither the slipstream authority of low speed nor the freestream dynamic pressure of high speed.

### Descent Is What Closes the Corridor

The corridor above is for level flight. Descending at rate $w$ adds to the angle of attack, because the freestream arrives from below,

$$\alpha_{\text{eff}} = \alpha_{\text{local}} + \arctan\frac{w}{V}$$

so **a tilt-wing can be stalled by its own rate of descent at constant tilt and constant speed.** Computing the descent rate that consumes the whole margin at the required tilt,

| Speed | Descent that closes the corridor |
|---|---|
| 10 m/s | 1.44 m/s, or 284 ft/min |
| 20 m/s | 2.08 m/s, or 409 ft/min |
| 30 m/s | 3.26 m/s, or 643 ft/min |
| 50 m/s | 4.99 m/s, or 983 ft/min |
| 60 m/s | 6.87 m/s, or 1,351 ft/min |

**This is not a novel observation and the literature confirms it directly.** The descent capability of two-propeller tilt-wing configurations, which is the X-18's exact arrangement, was measured and reported in [James L. Hassell 1966][research_james_l_hassell_1966]. The wider subject, including the vortex ring state that a lifting rotor meets in descent and its modern computational treatment, runs through [James L. Hassell 1966][research_james_l_hassell_1966], [Johnson 1977][research_johnson_1977], [Lee 1985][research_lee_1985], [Inoue et al 1997][research_inoue_1997], [Johnson 2004][research_johnson_2004], [Johnson 2005][research_johnson_2005], [Prasad and Chen 2006][research_prasad_chen_2006], [Young 2010][research_young_2010], [Yan et al 2012][research_yan_2012], [Stalewski and Surmacz 2019][research_stalewski_surmacz_2019], [Stalewski and Surmacz 2020][research_stalewski_surmacz_2020], [Makeev et al 2021][research_makeev_2021], [MAKEEV et al 2021, Numerical investigation of full sc][research_makeev_2021_2], [Sridharan and Govindarajan 2022][research_sridharan_govindarajan_2022].

**Two hundred and eighty-four feet per minute at the slow end is a gentle descent by any normal standard**, and it exhausts the margin. That is the tilt-wing descent problem, it is why these aircraft carried restricted descent envelopes, and it explains why the approach rather than the take-off was the difficult half of the flight.

### The Cost of the Configuration, Which Is Disc Loading

$$\frac{W}{n A} = \frac{146{,}800}{2 \times 18.68} = 3{,}929\ \text{N/m}^{2} = 82.1\ \text{lb/ft}^{2}$$

against roughly 11.7 pounds per square foot for a single 60 foot helicopter rotor at the same weight. **The tilt-wing carries seven times the disc loading of a helicopter**, which is the price of having propellers small enough to fit on a wing. Hover power follows from the same momentum theory,

$$P = n\, T \sqrt{\frac{T}{2 \rho A}}$$

which evaluates to 5,879 kilowatts, or **7,883 ideal shaft horsepower**. Against an installed 11,700 horsepower from two T40 engines, that implies a figure of merit of

$$\text{FM} = \frac{P_{\text{ideal}}}{P_{\text{shaft}}} = \frac{7{,}883}{11{,}700} = 0.674$$

**which is an entirely ordinary propeller figure of merit**, and is the strongest available check that the published weight, propeller diameter, and engine power describe one consistent aircraft.

## Dependent Systems

### The Pitch Jet, Which Is the Same Answer the X-13 and X-14 Gave

The X-18 carried a turbojet in the tail whose exhaust was deflected up or down purely for pitch control at low speed. The reason is the relation the previous two vertical take-off articles both used. Aerodynamic control scales with dynamic pressure and vanishes at zero speed, while thrust does not,

$$M_{\text{aero}} = q S \bar{c}\, C_{m\delta_e} \delta_e \propto V^{2}, \qquad M_{\text{jet}} = T_{\text{jet}}\, l$$

At a tail arm of 8.64 metres, a thousand pounds force of deflected jet gives 38.4 kilonewton metres. Setting the two equal and solving for speed gives the crossover at which the elevator takes over,

$$V_{\text{cross}} = \sqrt{\frac{2 M_{\text{jet}}}{\rho S \bar{c}\, C_{m\delta_e} \delta_e}} = 30.2\ \text{m/s} = 58.6\ \text{kt}$$

The control-power requirement that makes such a system necessary was being established across the same years, in [Reeder 1958][research_reeder_1958], [Carlson 1958][research_carlson_1958], [Slaughter 1958][research_slaughter_1958], and [Crim 1959][research_crim_1959], with the underlying hovering-stability question in [McCaskill 1953][research_mccaskill_1953] and the variable-stability technique that produced much of it in [Harper and P. 1955][research_harper_p_1955].

The control-power and handling-qualities literature that establishes how much authority is enough runs through [Gray et al 1953][research_gray_1953], [DAUGHADAY and DUWALDT 1955][research_daughaday_duwaldt_1955], [Anderson 1960, HIGHLIGHTS OF HANDLING QUALITIES C][research_anderson_1960_2], [Anderson 1960, Highlights of handling qualities c][research_anderson_1960_3], [BULL 1960][research_bull_1960], [Newsom 1962][research_newsom_1962], [Newsom 1962, FORCE-TEST INVESTIGATION OF THE ST][research_newsom_1962_2], [DAM et al 1980][research_dam_1980], [HESS 1981][research_hess_1981], [Goldstein 1982][research_goldstein_1982], [NACA 1982][research_naca_1982], [Corless and Blanken 1983][research_corless_blanken_1983], [Harris et al 2000][research_harris_2000], [Teofilatto 2001][research_teofilatto_2001], [Srinathkumar 2011][research_srinathkumar_2011], [Baughman and Longeauay 2015][research_baughman_longeauay_2015], [Portapas and Cooke 2020][research_portapas_cooke_2020], [Humphreys-Jennings et al 2020][research_humphreys_jennings_2020], [Campos and Marques 2021][research_campos_marques_2021], [Guo 2021][research_guo_2021].

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

**The ailerons supply under one percent of what is needed in hover and still only four percent at thirty metres per second.** The statement in the sources that losing an engine meant losing the aircraft is therefore not a caution. **It is arithmetic**, and cross-shafting is not a refinement but the only available fix. The problem was recognised in the period literature for turboprops generally, in [KIRCHNER 1955][research_kirchner_1955], and engine failure, drive systems and the interconnecting shafting that mitigates them are treated across [Holzhauser et al 1964][research_holzhauser_1964], [Overfield and Crawford 1967][research_overfield_crawford_1967], [Bucsek 1974][research_bucsek_1974], [Johnson 1975][research_johnson_1975], [GROSVELD 1983][research_grosveld_1983], [Stewart 1987][research_stewart_1987], [Arnold et al 1987][research_arnold_1987], [Carlson et al 1999][research_carlson_1999], [Schroijen and Slingerland 2007][research_schroijen_slingerland_2007], [Wandini et al 2016][research_wandini_2016], [Harish et al 2018][research_harish_2018], [Casadei et al 2019][research_casadei_2019], [Leelaburanathanakul et al 2021][research_leelaburanathanakul_2021], [Hoogreef and Soikkeli 2022][research_hoogreef_soikkeli_2022]. The powerplant itself, including the propeller governing that failed on the final flight, appears in [Zucrow 1949][research_zucrow_1949], [MOCK 1951][research_mock_1951], [RICE 1955][research_rice_1955], [Hooker 1956][research_hooker_1956], [RASMUSSEN 1960][research_rasmussen_1960], [NACA 1978][research_naca_1978], [Hirschkron et al 1979][research_hirschkron_1979], [Hirschkron et al 1979, MARITIME Patrol Aircraft Engine St][research_hirschkron_1979_2], [BANACH and REYNOLDS 1981][research_banach_reynolds_1981], [Wynn 1982][research_wynn_1982], [STOTEN 1983][research_stoten_1983], [Scott 2009][research_scott_2009].

### The Wing and Its Devices

A tilt-wing's outer panel is stalled through most of the conversion, so every device that delays stall is worth having. The period answer was boundary layer control by blowing, investigated over flaps and combinations in [Spreemann and Kuhn 1956][research_spreemann_kuhn_1956], [Kuhn 1957][research_kuhn_1957], and [Spreemann 1958][research_spreemann_1958], and large-chord slotted arrangements in [Kirby 1956][research_kirby_1956].

Free-floating and stall-flutter behaviour of tilt-wing models was investigated later, in [Ormiston 1972][research_ormiston_1972].

High-lift and boundary-layer-control devices are the standard remedy and were investigated for exactly this application, in [Passamanick 1948][research_passamanick_1948], [Cook et al 1958][research_cook_1958], [Kelly et al 1958][research_kelly_1958], [Aoyagi and Hickey 1959][research_aoyagi_hickey_1959], [Maki 1959][research_maki_1959], [Aoyagi and Hickey 1963][research_aoyagi_hickey_1963], [Fink 1967][research_fink_1967], [Phelps et al 1973][research_phelps_1973], [Quigley et al 1974][research_quigley_1974], [CARUSO et al 1988][research_caruso_1988], [Lee and Roberts 1990][research_lee_roberts_1990], [Kondor et al 2003][research_kondor_2003], [Beck et al 2014][research_beck_2014]. The effectiveness of blowing is measured by a momentum coefficient,

$$C_\mu = \frac{\dot{m} V_j}{q_\infty S}$$

and at the low freestream dynamic pressures of a conversion even a modest jet is a large coefficient, reaching 0.125 at twenty metres per second for fifteen hundred newtons of jet momentum.

**The X-18 had none of that.** It had a wing, two propellers, and a tilt mechanism, which is the minimum experiment rather than the best aircraft.

### The Propellers

Propeller behaviour at zero and low forward speed is its own subject, and static thrust in particular is not simply the cruise propeller evaluated at zero advance ratio, as [Webb and Willer 1952][research_webb_willer_1952] sets out, with later estimation methods in [Brusse and Cronk 1965][research_brusse_cronk_1965]. Propeller design for this class of aircraft is treated in [BIERMANN 1954][research_biermann_1954] and the ducted alternative in [ZABINSKY and LASZEWSKI 1956][research_zabinsky_laszewski_1956]. The propeller also has to work across an enormous range of advance ratio,

$$J = \frac{V}{n D}$$

which is zero in hover and of order one in cruise. At 1,100 revolutions per minute on a 4.877 metre diameter, $J$ runs from 0 to 1.12 between hover and 100 metres per second, so **the same blades meet the flow at completely different angles at the two ends of the conversion.** Propeller behaviour across that range, including static thrust, blade design and contra-rotating arrangements, is treated in [LERBS 1955][research_lerbs_1955], [BOSWELL 1961][research_boswell_1961], [Tosti 1962][research_tosti_1962], [Deckert et al 1964][research_deckert_1964], [Blaurock 1975][research_blaurock_1975], [Valentine and Kader 1976][research_valentine_kader_1976], [Hampton 1980][research_hampton_1980], [Jeracki and Mitchell 1981][research_jeracki_mitchell_1981], [HANSON 1986][research_hanson_1986], [Applin et al 1994][research_applin_1994], [Campos and Lau 2006][research_campos_lau_2006], [Envia 2014][research_envia_2014], [Sree and Stephens 2014][research_sree_stephens_2014], [Ferraro et al 2014][research_ferraro_2014], [Huo et al 2019][research_huo_2019]. That is why contra-rotating variable-pitch units were used and why the pitch control system was as complex as it was, which matters because the pitch control system is what failed. Helical tip Mach number at cruise is

$$M_{\text{tip}} = \frac{\sqrt{(\pi n D)^{2} + V^{2}}}{a} = 0.844$$

so the blade tips are transonic while the aircraft is not. The interference between a propeller and the wing behind it is the configuration's defining aerodynamic problem and was measured directly, in [Winston and Huston 1962][research_winston_huston_1962], [GOLAND et al 1964][research_goland_1964], and [Butler et al 1966][research_butler_1966].

### The Downwash, Which the Article Has Not Mentioned

A disc loading of 82.1 pounds per square foot is seven times a helicopter's, and the slipstream leaving the propellers at eighty metres per second has to go somewhere. Near the ground it strikes the surface, spreads, and recirculates, which changes the lift, erodes unprepared surfaces, and can ingest debris.

**This article computes none of that and should say so.** Ground effect for a configuration of this disc loading is its own subject, in [Schuldenfrei 1942][research_schuldenfrei_1942], [Huston and Winston 1960][research_huston_winston_1960], [Obryan 1960][research_obryan_1960], [MORSE and NEWHOUSE 1960][research_morse_newhouse_1960], [Curtiss et al 1985][research_curtiss_1985], [ESHLEMEN 1985][research_eshlemen_1985], [Eshleman et al 1986][research_eshleman_1986], [Allen 2004][research_allen_2004], [Radhakrishnan and Schmitz 2005][research_radhakrishnan_schmitz_2005], [Radhakrishnan and Schmitz 2006][research_radhakrishnan_schmitz_2006], [Hwang and Kwon 2019][research_hwang_kwon_2019], [Greene 2020][research_greene_2020], and the [X-13][related_post_a310_ryan_x13] article met the same problem from the jet-lift side. **A tilt-wing at this disc loading needs a prepared surface for the same reason a tail-sitting jet does**, which is a constraint the transport mission the X-18 was built to prove would have inherited.

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

**It assumes a stall angle.** The 15 degree figure used throughout is an assumption, and every corridor and descent figure scales with it directly. A thick wing with leading edge devices stalls later, and the fraction of the conversion spent stalled moves with it.

**It treats the slipstream as uniform.** Momentum theory gives an average. A real slipstream is swirling, non-uniform, and differently deflected across the span, and the immersed wing does not see one dynamic pressure.

**It uses a single representative contraction factor.** The 0.85 is a judgement, and the immersed fraction ranges from 47 to 67 percent across defensible choices, which is a wide band on the article's central quantity.

**It treats the final flight as an aerodynamic event.** It was a control system failure. The aerodynamics explain why the consequence was severe and do not explain why the failure occurred, and no public account of the governor fault was located.

## The Source Base

Unlike the two preceding articles, **this subject has a real technical literature**. The tilt-wing was studied intensively by the National Advisory Committee for Aeronautics and its successor, and the configuration's design considerations, wind tunnel behaviour, slipstream interference, and handling qualities are all documented in primary sources.

What is scarce is documentation of **this aircraft**. NASA's technical archive returns nothing for the vehicle designation, and the flight test reports, if they exist publicly, were not located. So the pattern is the inverse of the [X-16][related_post_a313_bell_x16] and [X-17][related_post_a314_lockheed_x17] articles, where the question had a literature and the vehicle did not. **Here the configuration has a literature and the individual airframe does not**, which is a milder version of the same difficulty.

Every dimension and weight is from secondary compilation. No source disagreement of consequence was found, which is itself unusual for this series and is worth stating.

### The Shape of the Reference Base

Of 218 research references, **184 or 84.4 percent predate 2019**, so this is a primary-source article by a wide margin. The distribution runs 54 documents from before 1960, 53 from the 1960s and 1970s, 39 from the 1980s and 1990s, 38 from 2000 to 2018, and 34 from 2019 onward.

**The coverage audit found a selection problem rather than a supply problem**, which is the opposite of the preceding article. The harvest had returned every era in quantity and the draft had cited almost only pre-1960 material, so the correction was to spread the selection rather than to search again.

**One topic did need a second harvest, and the reason is worth recording.** Descent and the vortex ring state stood at three records, because the draft treated descent as a passing mention in Out of Scope. The equation pass then made it the quantity that closes the conversion corridor. **An equation pass can promote a subject from an aside to a load-bearing claim, and the reference base has to follow it**, which is a dependency between passes this series has not previously had to state.

That search found the single most apposite document in the article, a measurement of the descent capability of two-propeller tilt-wing configurations, which is the X-18's exact arrangement addressing the X-18's exact difficulty.

**Four candidate references were rejected after being read rather than matched.** Two matched high angle of attack and were missile aerodynamics, where the phrase means something else. Two matched vortex ring and were a methane diffusion flame and a study of vortex filaments in a viscous fluid. **A keyword diagnostic inside a field is useless outside it**, which is the lesson the previous two articles recorded in different vocabularies.

## Epistemic State

**Historical fact.** The X-18 was built from a Chase YC-122C fuselage with Allison T40 turboprops taken from the XFY-1 and XFV-1 programmes and a Westinghouse J34 in the tail for pitch control. First hop 11 November 1959, first flight 24 November 1959, twenty flights, last flight July 1961. A propeller pitch control problem during an attempted conversion at ten thousand feet led to a spin from which the crew recovered. The aircraft never hovered, never completed a conversion, and was later scrapped. The engines were not cross-linked. The XC-142 followed with four propellers and full cross-shafting.

**Engineering analysis, reproducible from the stated inputs.** The local angle of attack relation and its consequence that the immersed panel sits at exactly zero incidence at zero forward speed. The maximum tolerable tilt from 90 degrees at ten metres per second to 30 at sixty. **The conversion corridor, which exists at every speed with a margin between 12.6 and 38.1 degrees of tilt.** The descent rates that close it, from 284 feet per minute at the slow end to 1,351 at the fast end. The induced velocity falling from 40.05 to 24.71 metres per second across the conversion while slipstream dynamic pressure rises from 2,210 to 5,772 pascals. The advance ratio range of 0 to 1.12 and the helical tip Mach number of 0.844. The aspect ratio of 4.348 against a quoted 4.36. The immersed span fraction of 66.8 percent uncontracted, 47.2 fully contracted, and about 57 at a representative factor. The stalled fraction of the conversion at 83.3 percent. The induced velocity of 40.05 metres per second, disc loading of 82.1 pounds per square foot, and slipstream dynamic pressure equivalent to 117 knots. The immersed lift fractions. The hover power of 7,883 ideal horsepower and the implied figure of merit of 0.674. The engine-out rolling moment of 268 kilonewton metres and the aileron fractions. The tolerable thrust asymmetry figures and the 26 percent authority loss at ten thousand feet. The pitch jet crossover at 59 knots.

**Inference, and clearly labelled.** That the outer wing being stalled is the configuration's defining problem is an inference from the geometry and a stall angle, supported by the period literature on tilt-wing stall but not derived from X-18 flight data. **That a corridor exists at every speed rests on a crude lift model** in which the immersed panel is given a linear lift curve to its stall and the outer panel a constant stalled lift coefficient of 0.6. The shape of the result is robust and the individual margins are not. That the XC-142's four propellers and cross-shafting were responses to the X-18's specific failures is an inference from the design changes and their evident purpose.

**What the record does not settle.** What caused the propeller pitch control failure. Whether the X-18 would have converted successfully had it not been grounded. What immersed fraction the designers believed they had. Whether the aircraft was ever close to a hover.

**A correction made during drafting.** An elevator effectiveness coefficient of 0.02 per radian was used initially and produced a pitch jet crossover speed of 454 knots, which is absurd for an aircraft of this class. The correct order is about 1.2 per radian and gives 59 knots. **The error was caught by reading the output for plausibility rather than by any check.**

**Information postdating the editorial date.** The contemporary literature section is written from current knowledge per the series convention.

## Out of Scope

The XC-142 programme deserves its own treatment and gets a paragraph here. The V-22 and the tilt-rotor line generally are named as the surviving alternative and not analysed. The detailed aerodynamics of swirl in a propeller slipstream are cited rather than derived. No attempt is made to reconstruct the X-18's flight envelope. The vortex ring state, which is the related descent hazard for a lifting rotor and which a tilt-wing can also meet, is not treated.

## Conclusion

The X-18 asked whether a wing could be tilted through ninety degrees and flown all the way. It never found out, and the reason it never found out is contained in the arithmetic of its own geometry.

**Two sixteen-foot propellers on a forty-eight-foot wing immerse a little over half of it.** The immersed part flies at an equivalent 117 knots while the aircraft stands still. **The rest of the wing is stalled for five sixths of the conversion**, and no wing design fixes that, because the wing is pointed away from the air by construction.

That would have been survivable with margin elsewhere. There was none. **The ailerons supply under one percent of the rolling moment an engine failure produces in hover**, the engines were not cross-linked so an engine failure was available to produce it, and a few percent of thrust asymmetry exhausts the roll control during conversion. When a propeller pitch control fault duly appeared, the aircraft departed.

**The configuration was not wrong and this aeroplane was under-equipped for it, and the corridor calculation is what establishes that rather than merely asserting it.** A usable tilt margin exists at every speed, between twelve and thirty-eight degrees, so the tilt-wing is a sound idea that this particular aeroplane could not exploit. The XC-142 answered with twice the propellers, full cross-shafting, and a far larger immersed fraction, which is a list of the X-18's deficiencies written as a specification. **The X-18's contribution was to establish, expensively and at the edge of a fatal accident, what the minimum version of the idea could not do.**

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

[research_allen_2004]: https://doi.org/10.2514/6.2004-5288
[research_anderson_1960]: https://ntrs.nasa.gov/citations/19980223619
[research_anderson_1960_2]: https://ntrs.nasa.gov/citations/19630004821
[research_anderson_1960_3]: https://ntrs.nasa.gov/citations/19740076594
[research_anderson_cho_1984]: https://ntrs.nasa.gov/citations/19840051681
[research_aoyagi_hickey_1959]: https://ntrs.nasa.gov/citations/19980228317
[research_aoyagi_hickey_1963]: https://ntrs.nasa.gov/citations/19630006046
[research_applin_1994]: https://ntrs.nasa.gov/citations/19940032994
[research_armutcuoglu_2004]: https://doi.org/10.2514/1.271
[research_arnold_1987]: https://doi.org/10.4271/871851
[research_banach_reynolds_1981]: https://doi.org/10.2514/6.1981-1648
[research_bartlett_1985]: https://ntrs.nasa.gov/citations/19850022700
[research_baughman_longeauay_2015]: https://doi.org/10.21236/ada616887
[research_baxter_finvold_1958]: https://doi.org/10.4271/580070
[research_beck_2014]: https://doi.org/10.2514/6.2014-0407
[research_bennett_1983]: https://doi.org/10.2514/6.1983-1212
[research_biermann_1954]: https://doi.org/10.4271/540196
[research_binz_2019]: https://doi.org/10.1177/1756829319861370
[research_biyela_rawatlal_2019]: https://doi.org/10.1016/j.compchemeng.2019.03.025
[research_black_1956]: https://doi.org/10.1017/s0368393100132390
[research_blaurock_1975]: https://doi.org/10.5957/pss-1975-004
[research_boswell_1961]: https://doi.org/10.21236/ad0262952
[research_brenckmann_1958]: https://doi.org/10.2514/8.7650
[research_brusse_cronk_1965]: https://ntrs.nasa.gov/citations/19660010796
[research_bucsek_1974]: https://doi.org/10.21236/adb003229
[research_bull_1960]: https://doi.org/10.4271/600284
[research_butler_1966]: https://doi.org/10.21236/ad0629637
[research_campos_lau_2006]: https://doi.org/10.2514/6.2006-2605
[research_campos_marques_2021]: https://doi.org/10.3390/aerospace8030077
[research_carlson_1958]: https://doi.org/10.4050/jahs.3.11
[research_carlson_1999]: https://doi.org/10.2514/6.1999-3961
[research_caruso_1988]: https://doi.org/10.2514/6.1988-396
[research_casadei_2019]: https://doi.org/10.1016/j.ast.2019.05.034
[research_catalano_2004]: https://doi.org/10.14311/562
[research_chana_2002]: https://doi.org/10.2514/6.2002-5996
[research_cook_1958]: https://ntrs.nasa.gov/citations/19930092355
[research_corless_blanken_1983]: https://ntrs.nasa.gov/citations/19840001967
[research_crim_1959]: https://doi.org/10.4050/jahs.4.1.26
[research_cui_2019]: https://doi.org/10.2514/1.c035047
[research_curtiss_1985]: https://ntrs.nasa.gov/citations/19860063840
[research_dallas_irvin_1956]: https://doi.org/10.21236/ad0147926
[research_dam_1980]: https://doi.org/10.2514/6.1980-1870
[research_daughaday_duwaldt_1955]: https://doi.org/10.21236/ad0103817
[research_deckert_1964]: https://ntrs.nasa.gov/citations/19640021081
[research_delamore_sutcliffe_greenwell_2006]: https://doi.org/10.2514/6.2006-3477
[research_div_1956]: https://doi.org/10.21236/ad0141370
[research_div_1956_2]: https://doi.org/10.21236/ad0105750
[research_doetsch_mark_1953]: https://doi.org/10.21236/ad0016744
[research_envia_2014]: https://ntrs.nasa.gov/citations/20150002338
[research_eshleman_1986]: https://ntrs.nasa.gov/citations/19860040021
[research_eshlemen_1985]: https://doi.org/10.2514/6.1985-4033
[research_fan_2019]: https://doi.org/10.1134/s0015462819040128
[research_fei_2019]: https://ntrs.nasa.gov/citations/20200002409
[research_feistel_1978]: https://ntrs.nasa.gov/citations/19780065878
[research_feldman_1956]: https://doi.org/10.21236/ad0103342
[research_ferraro_2014]: https://doi.org/10.2514/6.2014-0564
[research_fink_1967]: https://ntrs.nasa.gov/citations/19670014464
[research_fluk_1981]: https://doi.org/10.2514/6.1981-1623
[research_geuther_2020]: https://ntrs.nasa.gov/citations/20205003178
[research_giulianetti_weiberg_1964]: https://ntrs.nasa.gov/citations/19640004814
[research_goharshadi_mirzaei_2022]: https://doi.org/10.3390/inventions7040095
[research_goland_1964]: https://doi.org/10.21236/ad0608186
[research_goldstein_1982]: https://ntrs.nasa.gov/citations/19820015335
[research_gray_1953]: https://doi.org/10.21236/ad0013280
[research_greene_2020]: https://doi.org/10.4271/01-14-01-0001
[research_grosveld_1983]: https://doi.org/10.2514/6.1983-695
[research_grunwald_1961]: https://ntrs.nasa.gov/citations/19980227988
[research_guo_2021]: https://doi.org/10.1088/1742-6596/1877/1/012022
[research_hampton_1980]: https://doi.org/10.21236/ada082843
[research_hanson_1986]: https://doi.org/10.2514/6.1986-1892
[research_harish_2018]: https://doi.org/10.2514/6.2018-3838
[research_harper_p_1955]: https://doi.org/10.21236/ad0092496
[research_harris_2000]: https://doi.org/10.1017/s0001924000028098
[research_harris_2003]: https://ntrs.nasa.gov/citations/20080022367
[research_hess_1981]: https://doi.org/10.2514/6.1981-1771
[research_hickey_1956]: https://ntrs.nasa.gov/citations/19930088539
[research_hickey_aoyagi_1960]: https://ntrs.nasa.gov/citations/19980227096
[research_hill_1981]: https://doi.org/10.2514/6.1981-2636
[research_hirschkron_1979]: https://doi.org/10.21236/ada089279
[research_hirschkron_1979_2]: https://doi.org/10.21236/ada089336
[research_hoadley_pederson_2001]: https://doi.org/10.2514/6.2001-422
[research_holsten_2011]: https://doi.org/10.1007/s13272-011-0026-4
[research_holzhauser_1964]: https://ntrs.nasa.gov/citations/19640007812
[research_hoogreef_soikkeli_2022]: https://doi.org/10.1007/s13272-022-00591-5
[research_hooker_1956]: https://doi.org/10.4271/560018
[research_humphreys_jennings_2020]: https://doi.org/10.3390/aerospace7050051
[research_huo_2019]: https://doi.org/10.1177/1756829319833686
[research_huston_winston_1960]: https://ntrs.nasa.gov/citations/19980227777
[research_hwang_kwon_2019]: https://doi.org/10.1016/j.ast.2018.10.023
[research_iii_1956]: https://doi.org/10.4050/sm_wf_1956-4684
[research_inoue_1997]: https://doi.org/10.2514/6.1997-1847
[research_irvin_swan_1956]: https://doi.org/10.21236/ad0147927
[research_james_l_hassell_1966]: https://ntrs.nasa.gov/citations/19660015321
[research_jeracki_mitchell_1981]: https://ntrs.nasa.gov/citations/19810058354
[research_johnson_1975]: https://ntrs.nasa.gov/citations/19750019978
[research_johnson_1977]: https://ntrs.nasa.gov/citations/19770019123
[research_johnson_2004]: https://ntrs.nasa.gov/citations/20100033458
[research_johnson_2005]: https://ntrs.nasa.gov/citations/20060024029
[research_kahne_2000]: https://doi.org/10.1016/s1367-5788(00)90007-5
[research_kahne_2000_2]: https://doi.org/10.1016/s1367-5788(00)00011-0
[research_katz_1980]: https://doi.org/10.2514/6.1980-1872
[research_kelly_1958]: https://ntrs.nasa.gov/citations/19930092354
[research_kirby_1956]: https://ntrs.nasa.gov/citations/19930084546
[research_kirchner_1955]: https://doi.org/10.4271/550193
[research_koenig_quigley_1960]: https://ntrs.nasa.gov/citations/19630004820
[research_kondor_2003]: https://ntrs.nasa.gov/citations/20040001424
[research_kuhn_1957]: https://ntrs.nasa.gov/citations/19930084858
[research_kuhn_1959]: https://ntrs.nasa.gov/citations/19980232082
[research_kuhn_grunwald_1960]: https://ntrs.nasa.gov/citations/19980227804
[research_kuhn_grunwald_1961]: https://ntrs.nasa.gov/citations/19980227771
[research_lee_1985]: https://ntrs.nasa.gov/citations/19860020337
[research_lee_roberts_1990]: https://ntrs.nasa.gov/citations/19900007396
[research_leelaburanathanakul_2021]: https://doi.org/10.1088/1742-6596/1733/1/012001
[research_lerbs_1955]: https://doi.org/10.21236/ad0076232
[research_loewy_yntema_1958]: https://doi.org/10.4050/jahs.3.1.35
[research_madrid_2007]: https://doi.org/10.1007/978-3-540-75867-9_9
[research_makeev_2021]: https://doi.org/10.1088/1742-6596/1925/1/012004
[research_makeev_2021_2]: https://doi.org/10.1016/j.cja.2020.12.011
[research_maki_1959]: https://ntrs.nasa.gov/citations/19980228300
[research_mallen_dancik_1959]: https://doi.org/10.4050/jahs.4.15
[research_marks_1956]: https://doi.org/10.4050/sm_wf_1956-2795
[research_mazzitelli_1957]: https://doi.org/10.4271/570357
[research_mccaskill_1953]: https://doi.org/10.21236/ad0015833
[research_mccormick_mallen_1956]: https://doi.org/10.4050/sm_wf_1956-2299
[research_mccormick_mallen_1957]: https://doi.org/10.4050/jahs.2.49
[research_mccormick_w_1956_2]: https://doi.org/10.21236/ad0159429
[research_mcveigh_1975]: https://ntrs.nasa.gov/citations/19760004918
[research_meloney_2000]: https://doi.org/10.2514/6.2000-3486
[research_meloney_2001]: https://doi.org/10.2514/6.2001-3799
[research_mikhalyov_2019]: https://doi.org/10.1051/matecconf/201930402018
[research_mock_1951]: https://doi.org/10.4271/510198
[research_moens_gardarein_2001]: https://doi.org/10.2514/6.2001-2404
[research_morse_newhouse_1960]: https://doi.org/10.21236/ad0248356
[research_naca_1960]: https://ntrs.nasa.gov/citations/19740076580
[research_naca_1960_2]: https://ntrs.nasa.gov/citations/19630004807
[research_naca_1978]: https://ntrs.nasa.gov/citations/19800005872
[research_naca_1982]: https://ntrs.nasa.gov/citations/19820015334
[research_nelson_mouch_1978]: https://doi.org/10.21236/ada056045
[research_newsom_1962]: https://ntrs.nasa.gov/citations/19620005161
[research_newsom_1962_2]: https://ntrs.nasa.gov/citations/19620005247
[research_ng_datta_2019]: https://doi.org/10.2514/1.c035218
[research_o_rourke_rutherford_1991]: https://doi.org/10.2514/6.1991-3143
[research_obryan_1960]: https://ntrs.nasa.gov/citations/19630004827
[research_ormiston_1972]: https://ntrs.nasa.gov/citations/19720018348
[research_overfield_crawford_1967]: https://doi.org/10.21236/ad0661311
[research_passamanick_1948]: https://ntrs.nasa.gov/citations/19930085382
[research_phelps_1973]: https://ntrs.nasa.gov/citations/19730013180
[research_portapas_cooke_2020]: https://doi.org/10.3846/aviation.2020.12175
[research_prasad_chen_2006]: https://doi.org/10.2514/6.2006-6632
[research_quigley_1974]: https://ntrs.nasa.gov/citations/19740014524
[research_quigley_koenig_1960]: https://ntrs.nasa.gov/citations/19740076593
[research_radhakrishnan_schmitz_2005]: https://doi.org/10.2514/6.2005-5218
[research_radhakrishnan_schmitz_2006]: https://doi.org/10.2514/6.2006-3471
[research_rasmussen_1960]: https://doi.org/10.4271/600281
[research_reeder_1958]: https://doi.org/10.4050/jahs.3.4
[research_renooij_slingerland_2004]: https://doi.org/10.2514/6.2004-214
[research_rice_1955]: https://doi.org/10.4271/550025
[research_rizk_1980]: https://ntrs.nasa.gov/citations/19800038563
[research_rizk_1980_2]: https://doi.org/10.2514/6.1980-125
[research_roberts_1981]: https://ntrs.nasa.gov/citations/19810024601
[research_rohr_2019]: https://doi.org/10.1109/lra.2019.2914340
[research_rutherford_bass_1992]: https://doi.org/10.2514/6.1992-4237
[research_s_p_2022]: https://doi.org/10.24191/jmeche.v19i1.19697
[research_schroijen_slingerland_2007]: https://doi.org/10.2514/6.2007-1046
[research_schuldenfrei_1942]: https://ntrs.nasa.gov/citations/19930092661
[research_scott_2009]: https://doi.org/10.21236/ada517800
[research_sharp_1950]: https://doi.org/10.4271/500123
[research_slaughter_1958]: https://doi.org/10.4050/jahs.3.9
[research_smith_1958]: https://ntrs.nasa.gov/citations/19980227972
[research_smith_levin_1981]: https://ntrs.nasa.gov/citations/19820026931
[research_spreemann_1958]: https://ntrs.nasa.gov/citations/19930085045
[research_spreemann_kuhn_1956]: https://ntrs.nasa.gov/citations/19930084788
[research_sree_stephens_2014]: https://ntrs.nasa.gov/citations/20150002339
[research_sridharan_govindarajan_2022]: https://doi.org/10.4050/jahs.67.022004
[research_srinathkumar_2011]: https://doi.org/10.1049/pbce074e
[research_stalewski_surmacz_2019]: https://doi.org/10.1051/matecconf/201930402011
[research_stalewski_surmacz_2020]: https://doi.org/10.1108/aeat-12-2019-0264
[research_stapleford_1980]: https://doi.org/10.4271/801206
[research_stepniewski_1957]: https://doi.org/10.1017/s2753447200003528
[research_stewart_1987]: https://ntrs.nasa.gov/citations/19870011566
[research_stiesz_1940]: https://doi.org/10.1108/eb030721
[research_stoten_1983]: https://doi.org/10.2514/6.1983-1158
[research_stuart_1957]: https://doi.org/10.4050/jahs.2.10
[research_stuart_1957_2]: https://doi.org/10.4050/jahs.2.2.10
[research_sullivan_1993]: https://doi.org/10.2514/6.1993-3939
[research_sweberg_dingeldein_1945]: https://ntrs.nasa.gov/citations/19930091906
[research_tapscott_1960]: https://ntrs.nasa.gov/citations/19630004822
[research_tapscott_1960_2]: https://ntrs.nasa.gov/citations/20150018614
[research_teofilatto_2001]: https://doi.org/10.1016/s1369-8869(00)00025-2
[research_thoren_johnson_1940]: https://doi.org/10.2514/8.1190
[research_tosti_1961]: https://ntrs.nasa.gov/citations/19980227992
[research_tosti_1962]: https://ntrs.nasa.gov/citations/19620003850
[research_totah_1992]: https://ntrs.nasa.gov/citations/19920010605
[research_uhlig_selig_2008]: https://doi.org/10.2514/6.2008-407
[research_valentine_kader_1976]: https://doi.org/10.21236/ada035756
[research_verma_junkins_2000]: https://doi.org/10.2514/6.2000-971
[research_vidal_1960]: https://doi.org/10.21236/ad0246522
[research_vincent_1979]: https://doi.org/10.2514/6.1979-1640
[research_wandini_2016]: https://doi.org/10.4028/www.scientific.net/amm.842.208
[research_wang_1979]: https://doi.org/10.21236/ada074260
[research_wang_2019]: https://doi.org/10.1108/aeat-02-2017-0066
[research_wang_2019_2]: https://doi.org/10.3390/app9224937
[research_wang_2019_3]: https://doi.org/10.1016/j.ast.2018.07.023
[research_wang_2019_4]: https://doi.org/10.2514/1.c035209
[research_ward_1960]: https://ntrs.nasa.gov/citations/19630004830
[research_webb_willer_1952]: https://doi.org/10.21236/ada075990
[research_weiberg_holzhauser_1961]: https://ntrs.nasa.gov/citations/19980228286
[research_welge_1981]: https://ntrs.nasa.gov/citations/19810021547
[research_winston_huston_1962]: https://ntrs.nasa.gov/citations/19630000659
[research_wu_2019]: https://doi.org/10.3390/math7020116
[research_wynn_1982]: https://doi.org/10.21236/ada122962
[research_xiao_2022]: https://doi.org/10.2139/ssrn.4139493
[research_xue_zhou_2020]: https://doi.org/10.1016/j.ast.2019.105556
[research_yan_2012]: https://doi.org/10.1016/j.apm.2012.01.015
[research_young_2010]: https://doi.org/10.1002/9780470686652.eae247
[research_zabinsky_laszewski_1956]: https://doi.org/10.21236/ad0102024
[research_zizkovsky_klesa_2019]: https://doi.org/10.1051/matecconf/201930402019
[research_zucrow_1949]: https://doi.org/10.2514/8.4291

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
